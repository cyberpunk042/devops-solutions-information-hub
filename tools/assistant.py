#!/usr/bin/env python3
"""
tools/assistant.py — Per-Project AI Assistant lifecycle management.

The operator-named meta-tool that brings a Profile from "file on disk" to
"live running AI assistant the operator can interact with". Per operator
2026-05-09 turn 7: "you are not done, till I cannot just call a script
and be ready to interact with my live running AI assistant".

USAGE
=====
    .venv/bin/python -m tools.assistant <subcommand> [args]

    install <profile>      Full install: profile validation + vendor merge +
                           cron registration + systemd persistence + surfaces.
                           One command from zero to ready-to-start.

    up <profile>           Start the assistant (after install). Live + ready.
    down <profile>         Stop the assistant.
    restart <profile>      Restart cleanly.
    status [profile]       Status across all surfaces (per profile or all).
    logs <profile>         Tail logs.

    config show <profile>          Show current vendor config.
    config edit <profile> <vendor> Open vendor config in $EDITOR.
    config sync <profile>          Re-merge profile changes into vendor configs.

    cron list <profile|--global>   List configured cron jobs.
    cron enable <profile> <job>    Enable a cron job.
    cron disable <profile> <job>   Disable a cron job.
    cron status <profile|--global> Status of cron jobs (last run, next run).
    cron install-global            Install global cross-profile cron jobs.

    surfaces list                  Show available surfaces (multica/wiki/docs/...).
    surfaces enable <profile> <surface>  Wire a surface to a profile.
    surfaces disable <profile> <surface> Unwire.

    uninstall <profile>    Reverse install (preserves the Profile YAML).

    profiles               List all known profiles in .assistant/.
    help [subcommand]      Detailed help.

ARCHITECTURE
============
    .assistant/
        <name>.yaml                — the abstract Profile (tool-agnostic)
        <name>.openclaw.json5      — OpenClaw vendor config (consumes the Profile)
        <name>.openclaw.json       — same, stripped to pure JSON (deploy form)
        <name>.cron.yaml           — per-profile CRON jobs
        _global/
            cron.yaml              — cross-profile CRON jobs
            surfaces.yaml          — surface integrations config
        _templates/
            assistant.service.template — systemd unit template
            assistant-cron.service.template
            assistant-cron.timer.template
        _state/                    — runtime state (gitignored)

    Reboot-persistence: systemd user services in ~/.config/systemd/user/.
    Slash-command equivalents: .claude/commands/assistant-*.md.

SAFETY
======
    Never edits operator-territory files (CLAUDE.md, AGENTS.md, methodology.yaml,
    wiki-schema.yaml). Operator approval required for: schema codification,
    spine super-model edits, cross-project work. Surfaces enable/disable is
    additive (never removes operator's prior config).
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any

# ───────────────────────────────────────────────────────────────────────
# Paths + Constants
# ───────────────────────────────────────────────────────────────────────

PROJECT_ROOT = Path(os.environ.get("CLAUDE_PROJECT_DIR", "/home/jfortin/devops-solutions-information-hub"))
ASSISTANT_DIR = PROJECT_ROOT / ".assistant"
TEMPLATES_DIR = ASSISTANT_DIR / "_templates"
GLOBAL_DIR = ASSISTANT_DIR / "_global"
STATE_DIR = ASSISTANT_DIR / "_state"
SYSTEMD_USER_DIR = Path.home() / ".config" / "systemd" / "user"
OPENCLAW_CONFIG = Path.home() / ".openclaw" / "openclaw.json"

VENDORS = ("openclaw", "multica", "claude-code-cli-p", "hermes", "opencode", "claude-os")

# Workspace modes — declared in Profile YAML as `workspace_mode: <mode>`.
#
# CRITICAL safety note (2026-05-15): the OpenClaw `workspace` field is the dir where
# the runtime scaffolds files (IDENTITY.md/HEARTBEAT.md/SOUL.md/USER.md) AND is the
# dir `openclaw agents delete` tries to delete. Workspace MUST NEVER be the project
# root. All three modes use an isolated workspace dir under ~/.openclaw/agents/<name>/.
# Difference between modes is WHERE the agent's TOOLS target their work — NOT where
# the workspace dir lives.
WORKSPACE_MODES = {
    "shared": {
        "description": "Workspace dir is isolated under ~/.openclaw/agents/<name>/workspace/ — but the agent's tools target the operator's project (cwd=PROJECT_ROOT). Writes land in the project, visible to operator immediately.",
        "writes_visible_immediately": True,
        "git_isolation": False,
        "best_for": "Live observable work — synthesis, research surfacing, ingestion — where operator wants to see + correct in real time.",
    },
    "worktree": {
        "description": "Workspace dir is a `git worktree add` checkout under ~/.openclaw/agents/<name>/worktree/ on its own branch `assistant/<name>`. Tools target the worktree; operator merges the branch back when ready.",
        "writes_visible_immediately": False,
        "git_isolation": True,
        "best_for": "Longer autonomous runs without interleaving operator's work; merge back when ready.",
    },
    "own-workspace": {
        "description": "Workspace dir is a separate clone at ~/.openclaw/agents/<name>/own-workspace/. Sync via git push/pull.",
        "writes_visible_immediately": False,
        "git_isolation": True,
        "best_for": "Remote / sandboxed / untrusted contexts where full isolation is required.",
    },
}


_WEEKDAYS = {"Mon": 1, "Tue": 2, "Wed": 3, "Thu": 4, "Fri": 5, "Sat": 6, "Sun": 0}


def translate_schedule(schedule: str) -> tuple[str, str] | None:
    """
    Translate a systemd-OnCalendar-style schedule (used in our cron.yaml) into
    arguments for `openclaw cron add`.

    Returns (flag_name, flag_value) where flag_name is "--every" or "--cron",
    or None if the pattern is not recognized.

    Handles the patterns we use in .assistant/<name>.cron.yaml:
      "hourly"               → ("--every", "1h")
      "daily"                → ("--every", "1d")
      "weekly"               → ("--every", "7d")
      "*-*-* HH:MM:SS"       → ("--cron", "M H * * *")
      "DOW *-*-* HH:MM:SS"   → ("--cron", "M H * * D")   (Mon/Tue/.../Sun)
      "*-*-DD HH:MM:SS"      → ("--cron", "M H D * *")
    """
    s = schedule.strip()
    if s == "hourly":
        return ("--every", "1h")
    if s == "daily":
        return ("--every", "1d")
    if s == "weekly":
        return ("--every", "7d")
    # *-*-* HH:MM:SS  (daily at HH:MM)
    m = re.fullmatch(r"\*-\*-\* (\d{2}):(\d{2}):\d{2}", s)
    if m:
        return ("--cron", f"{int(m.group(2))} {int(m.group(1))} * * *")
    # DOW *-*-* HH:MM:SS  (weekly on DOW at HH:MM)
    m = re.fullmatch(r"(Mon|Tue|Wed|Thu|Fri|Sat|Sun) \*-\*-\* (\d{2}):(\d{2}):\d{2}", s)
    if m:
        dow = _WEEKDAYS[m.group(1)]
        return ("--cron", f"{int(m.group(3))} {int(m.group(2))} * * {dow}")
    # *-*-DD HH:MM:SS  (monthly on day DD at HH:MM)
    m = re.fullmatch(r"\*-\*-(\d{2}) (\d{2}):(\d{2}):\d{2}", s)
    if m:
        return ("--cron", f"{int(m.group(3))} {int(m.group(2))} {int(m.group(1))} * *")
    return None


def compute_workspace_path(name: str, mode: str) -> Path:
    """Return the absolute OpenClaw workspace path (NEVER the project root — see safety note)."""
    base = Path.home() / ".openclaw" / "agents" / name
    if mode == "shared":
        return base / "workspace"
    elif mode == "worktree":
        return base / "worktree"
    elif mode == "own-workspace":
        return base / "own-workspace"
    else:
        raise ValueError(f"Unknown workspace_mode: {mode}. Valid: {sorted(WORKSPACE_MODES.keys())}")


def compute_operating_root(mode: str) -> Path:
    """Return the dir the agent's tools target (cwd for shell commands, MCP cwd, etc.).

    `shared` mode → PROJECT_ROOT (writes land in the project, visible to operator).
    `worktree` / `own-workspace` → the workspace dir itself (writes stay isolated).
    """
    if mode == "shared":
        return PROJECT_ROOT
    # Worktree / own-workspace: operating root is the workspace dir itself
    return None  # caller substitutes compute_workspace_path(name, mode)


def ensure_workspace(name: str, mode: str, dry_run: bool = False) -> Path:
    """Materialize the workspace per mode. Idempotent. Returns the absolute path."""
    path = compute_workspace_path(name, mode)
    if path.exists():
        ok(f"workspace already exists at {path}")
        return path
    if dry_run:
        info(f"DRY RUN — would create workspace at {path} ({mode} mode)")
        return path
    if mode == "shared":
        # Isolated empty workspace dir — OpenClaw will scaffold its own behavioral files here
        path.mkdir(parents=True, exist_ok=True)
        ok(f"isolated workspace dir created at {path}")
    elif mode == "worktree":
        path.parent.mkdir(parents=True, exist_ok=True)
        branch = f"assistant/{name}"
        info(f"Creating git worktree at {path} on branch {branch}")
        proc = run(["git", "-C", str(PROJECT_ROOT), "rev-parse", "--verify", branch], check=False)
        if proc.returncode != 0:
            info(f"Branch {branch} does not exist; creating from HEAD")
            run(["git", "-C", str(PROJECT_ROOT), "worktree", "add", "-b", branch, str(path)], check=False)
        else:
            run(["git", "-C", str(PROJECT_ROOT), "worktree", "add", str(path), branch], check=False)
        ok(f"worktree ready at {path}")
    elif mode == "own-workspace":
        path.parent.mkdir(parents=True, exist_ok=True)
        info(f"Cloning {PROJECT_ROOT} into {path}")
        run(["git", "clone", str(PROJECT_ROOT), str(path)], check=False)
        ok(f"own workspace ready at {path}")
    return path

# ANSI for stage explanations (operator: "everything must be explained to me at each stage properly")
BOLD = "\033[1m"
DIM = "\033[2m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RED = "\033[31m"
BLUE = "\033[34m"
RESET = "\033[0m"


def stage(msg: str) -> None:
    print(f"{BOLD}{BLUE}━━━ {msg}{RESET}")


def ok(msg: str) -> None:
    print(f"  {GREEN}✓{RESET} {msg}")


def warn(msg: str) -> None:
    print(f"  {YELLOW}!{RESET} {msg}")


def err(msg: str) -> None:
    print(f"  {RED}✗{RESET} {msg}", file=sys.stderr)


def info(msg: str) -> None:
    print(f"  {DIM}{msg}{RESET}")


# ───────────────────────────────────────────────────────────────────────
# Helpers
# ───────────────────────────────────────────────────────────────────────


def have(cmd: str) -> bool:
    return shutil.which(cmd) is not None


def run(cmd: list[str], check: bool = True, capture: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, check=check, capture_output=capture, text=True)


def load_yaml(path: Path) -> dict:
    try:
        import yaml
    except ImportError:
        err("PyYAML not installed; install via .venv/bin/pip install pyyaml")
        sys.exit(2)
    if not path.exists():
        return {}
    with open(path) as f:
        return yaml.safe_load(f) or {}


def load_json5(path: Path) -> dict:
    """Read a JSON5 file. Tries pyjson5; falls back to npx json5 → pure JSON."""
    if not path.exists():
        return {}
    try:
        import pyjson5  # type: ignore
        with open(path) as f:
            return pyjson5.load(f)
    except ImportError:
        pass
    # Fallback: shell out to `npx json5` to convert
    if have("npx"):
        proc = run(["npx", "--yes", "json5", str(path)])
        return json.loads(proc.stdout)
    err(f"Cannot parse JSON5 at {path}: install pyjson5 (.venv/bin/pip install pyjson5) OR ensure npx is on PATH")
    sys.exit(2)


def load_openclaw_config() -> dict:
    if OPENCLAW_CONFIG.exists():
        with open(OPENCLAW_CONFIG) as f:
            return json.load(f)
    return {}


def save_openclaw_config(data: dict) -> None:
    OPENCLAW_CONFIG.parent.mkdir(parents=True, exist_ok=True)
    with open(OPENCLAW_CONFIG, "w") as f:
        json.dump(data, f, indent=2)
    OPENCLAW_CONFIG.chmod(0o600)


def profile_path(name: str) -> Path:
    return ASSISTANT_DIR / f"{name}.yaml"


def vendor_path(name: str, vendor: str, ext: str | None = None) -> Path:
    """Vendor config path. Default: <name>.<vendor>.json5 for openclaw, .yaml otherwise."""
    if ext is None:
        ext = "json5" if vendor == "openclaw" else "yaml"
    return ASSISTANT_DIR / f"{name}.{vendor}.{ext}"


def list_profiles() -> list[str]:
    if not ASSISTANT_DIR.exists():
        return []
    return sorted(p.stem for p in ASSISTANT_DIR.glob("*.yaml") if "." not in p.stem)


# ───────────────────────────────────────────────────────────────────────
# Subcommand: profiles (list known)
# ───────────────────────────────────────────────────────────────────────


def cmd_profiles(_args: argparse.Namespace) -> int:
    stage("Known Profiles in .assistant/")
    names = list_profiles()
    if not names:
        warn("No profiles found.")
        info(f"Create one at: {ASSISTANT_DIR}/<name>.yaml")
        return 0
    for name in names:
        profile = load_yaml(profile_path(name))
        job = profile.get("job", "(no job)")
        focus = profile.get("focus", "")
        vendor_files = sorted(p.name for p in ASSISTANT_DIR.glob(f"{name}.*.*"))
        ok(f"{BOLD}{name}{RESET}  —  {job}")
        info(f"     focus: {focus}")
        info(f"     vendor configs: {', '.join(vendor_files) if vendor_files else '(none yet)'}")
    return 0


# ───────────────────────────────────────────────────────────────────────
# Subcommand: install
# ───────────────────────────────────────────────────────────────────────


def cmd_install(args: argparse.Namespace) -> int:
    name = args.profile
    stage(f"Install assistant Profile: {name}")
    info("Stages: 1) validate profile + workspace · 2) validate vendor config · 3) register")
    info("        agent via `openclaw agents add` · 3b) wire project MCP server")
    info("        · 4) register cron jobs via `openclaw cron add` · 5) install systemd unit")
    info("        for the gateway daemon · 6) wire surfaces. Idempotent: re-running is safe.")
    print()

    # 1. validate profile
    stage("[1/6] Validate Profile YAML")
    p = profile_path(name)
    if not p.exists():
        err(f"Profile not found at {p}")
        info(f"Create it first. See: wiki/spine/standards/per-project-assistant-profile-standards.md")
        return 1
    profile = load_yaml(p)
    required_top = {"profile_version", "profile_name", "project", "job", "identity",
                    "knowledge_scope", "action_surface", "model_routing",
                    "prompt_templates", "success_criteria"}
    missing = required_top - set(profile.keys())
    if missing:
        err(f"Profile missing required top-level keys: {sorted(missing)}")
        return 1
    ok(f"Profile valid: {profile['profile_name']} — {profile['job']}")

    # 1b. Resolve workspace_mode + materialize workspace
    workspace_mode = profile.get("workspace_mode", "shared")
    if workspace_mode not in WORKSPACE_MODES:
        err(f"Invalid workspace_mode '{workspace_mode}'. Valid: {sorted(WORKSPACE_MODES.keys())}")
        return 1
    ok(f"workspace_mode: {workspace_mode} — {WORKSPACE_MODES[workspace_mode]['description']}")
    workspace_path = ensure_workspace(name, workspace_mode, dry_run=args.dry_run)
    ok(f"workspace resolved: {workspace_path}")

    # 2. validate openclaw vendor config
    stage("[2/6] Validate OpenClaw vendor config")
    vp = vendor_path(name, "openclaw", "json5")
    if not vp.exists():
        warn(f"No OpenClaw vendor config at {vp}")
        info(f"Skip OpenClaw stages or author the vendor config first.")
        if not args.no_openclaw:
            return 1
    else:
        agent = load_json5(vp)
        if "id" not in agent or "name" not in agent:
            err("OpenClaw config missing required id/name")
            return 1
        ok(f"OpenClaw agent: id={agent['id']}, name={agent['name']}")

    # 3. register agent via `openclaw agents add` (OpenClaw 2026.5.12+)
    if vp.exists() and not args.no_openclaw:
        stage("[3/6] Register agent via `openclaw agents add`")
        # Pull the registration fields from the vendor json5 (we still use it as a
        # documentation transcript — but ONLY `id`, `name`, `agentDir`, `model.primary`
        # are consumed by the install path now. The behavioral fields
        # (systemPromptOverride, skills, tools.allow/deny, heartbeat, contextLimits,
        # compaction, etc.) belong to the workspace markdown files now and to
        # per-agent config; those flow in via subsequent steps + manual operator review.
        agent_id = agent["id"]
        agent_dir = os.path.expanduser(agent.get("agentDir", f"~/.openclaw/agents/{name}/agent"))
        model_id = agent.get("model", {}).get("primary", "anthropic/claude-opus-4-7")
        if not have("openclaw"):
            err("openclaw CLI not on PATH — cannot register agent. Install OpenClaw first.")
            return 1
        # Check if agent already exists (idempotent re-run)
        proc = run(["openclaw", "agents", "list"], check=False)
        already_registered = bool(proc.stdout and f"- {agent_id} " in proc.stdout)
        if already_registered:
            info(f"agent '{agent_id}' already registered in gateway — skipping add (idempotent)")
            ok(f"agent registered: {agent_id} (workspace={workspace_path}, model={model_id})")
        else:
            cmd = [
                "openclaw", "agents", "add", agent_id,
                "--workspace", str(workspace_path),
                "--agent-dir", agent_dir,
                "--model", model_id,
                "--non-interactive",
                "--json",
            ]
            info(f"$ {' '.join(cmd)}")
            if args.dry_run:
                info("DRY RUN — not invoking openclaw agents add")
            else:
                proc = run(cmd, check=False)
                if proc.returncode == 0:
                    ok(f"agent registered: {agent_id} (workspace_mode={workspace_mode})")
                    info(f"output: {proc.stdout.strip()}")
                else:
                    err(f"openclaw agents add failed: {proc.stderr.strip()}")
                    info(f"stdout: {proc.stdout.strip()}")
                    return 1
        # Note for operator: per-agent behavioral overrides (system prompt, tools.allow/deny,
        # heartbeat, etc.) that were in the .openclaw.json5 vendor config don't apply in
        # the modern OpenClaw schema. Behavior comes from workspace markdown files
        # (AGENTS.md, IDENTITY.md, HEARTBEAT.md, TOOLS.md, BOOTSTRAP.md, SOUL.md, USER.md)
        # and from MCP server registration (step [3b]).
        info(f"workspace markdown files at {workspace_path} drive agent behavior")
        info(f"  AGENTS.md present: {(workspace_path / 'AGENTS.md').exists()}")
        info(f"  IDENTITY.md present: {(workspace_path / 'IDENTITY.md').exists()}")
        info(f"  HEARTBEAT.md present: {(workspace_path / 'HEARTBEAT.md').exists()}")
        info(f"  TOOLS.md present: {(workspace_path / 'TOOLS.md').exists()}")

    # 3b. Wire project's MCP server (this project's wiki tools — 28 tools)
    if not args.no_mcp and have("openclaw"):
        stage("[3b/6] Wire project MCP server (`openclaw mcp set wiki-llm`)")
        # Check if already registered
        proc = run(["openclaw", "mcp", "list"], check=False)
        if proc.stdout and "wiki-llm" in proc.stdout:
            ok("MCP server 'wiki-llm' already registered — skipping (idempotent)")
        else:
            mcp_spec = {
                "command": str(PROJECT_ROOT / ".venv" / "bin" / "python"),
                "args": ["-m", "tools.mcp_server"],
                "cwd": str(PROJECT_ROOT),
            }
            mcp_json = json.dumps(mcp_spec)
            cmd = ["openclaw", "mcp", "set", "wiki-llm", mcp_json]
            info(f"$ openclaw mcp set wiki-llm '{mcp_json}'")
            if args.dry_run:
                info("DRY RUN — not invoking openclaw mcp set")
            else:
                proc = run(cmd, check=False)
                if proc.returncode == 0:
                    ok("MCP server 'wiki-llm' registered (28 wiki_* tools now available to all agents)")
                else:
                    warn(f"openclaw mcp set failed: {proc.stderr.strip()}")
                    info("  Manual fallback: openclaw mcp set wiki-llm '<json>'")
    else:
        info("[3b/6] Skipped (--no-mcp or openclaw not on PATH)")

    # 4. cron jobs → gateway-managed via `openclaw cron add`
    stage("[4/6] Register per-profile CRON jobs via `openclaw cron add`")
    cron_path = ASSISTANT_DIR / f"{name}.cron.yaml"
    if not cron_path.exists():
        info(f"No cron file at {cron_path} — skipping cron registration")
    elif args.no_cron or not have("openclaw"):
        info("[4/6] Skipped (--no-cron or openclaw not on PATH)")
    else:
        cron = load_yaml(cron_path)
        jobs = cron.get("jobs", [])
        ok(f"Found {len(jobs)} cron job(s) defined for this profile")
        # List existing gateway jobs once so re-runs skip already-registered ones
        proc = run(["openclaw", "cron", "list"], check=False)
        existing_jobs_output = proc.stdout if proc.returncode == 0 else ""
        for j in jobs:
            job_name = f"{name}-{j['name']}"  # namespace by profile (continuous-research-morning-scan, etc.)
            schedule = j.get("schedule", "")
            description = j.get("description", "")
            trigger = j.get("trigger", {})
            prompt = trigger.get("prompt", "").strip()
            enabled_in_yaml = j.get("enabled", False)
            # Translate schedule → openclaw cron flag pair
            translated = translate_schedule(schedule)
            if not translated:
                warn(f"  - {j['name']}: unrecognized schedule '{schedule}' — skipping (translate manually with `openclaw cron add ...`)")
                continue
            flag, value = translated
            # Idempotent: skip if already registered
            if job_name in existing_jobs_output:
                info(f"  - {job_name}: already registered in gateway — skipping (idempotent)")
                continue
            cmd = [
                "openclaw", "cron", "add",
                "--name", job_name,
                flag, value,
                "--agent", name,
                "--message", prompt or f"Run {j['name']} task",
                "--description", description,
                "--session", "isolated",  # cron-driven runs use isolated sessions, not main
                "--expect-final",         # wait for agent response
            ]
            if not enabled_in_yaml:
                cmd.append("--disabled")
            info(f"  - {job_name}: {schedule} → {flag} {value}  ({'enabled' if enabled_in_yaml else 'disabled'})")
            if args.dry_run:
                info(f"    DRY RUN — would run: openclaw cron add --name {job_name} {flag} {value} --agent {name} ...")
            else:
                proc = run(cmd, check=False)
                if proc.returncode == 0:
                    ok(f"    registered: {job_name}")
                else:
                    warn(f"    openclaw cron add failed for {job_name}: {proc.stderr.strip()[:200]}")
        info("Jobs registered DISABLED by default. Enable via `bin/assistant cron enable <profile> <job>` or directly: `openclaw cron enable <job-name>`")

    # 5. systemd unit
    stage("[5/6] Install systemd user service (reboot persistence)")
    if not have("systemctl"):
        warn("systemctl not found — skipping systemd. (Manual start via `openclaw daemon` works.)")
    else:
        unit_template = TEMPLATES_DIR / "assistant.service.template"
        if not unit_template.exists():
            warn(f"systemd template not at {unit_template} — install will skip systemd")
        else:
            unit_content = unit_template.read_text().replace("{{PROFILE_NAME}}", name).replace(
                "{{PROJECT_ROOT}}", str(PROJECT_ROOT))
            unit_dest = SYSTEMD_USER_DIR / f"assistant-{name}.service"
            if args.dry_run:
                info(f"DRY RUN — would write {unit_dest}")
            else:
                SYSTEMD_USER_DIR.mkdir(parents=True, exist_ok=True)
                unit_dest.write_text(unit_content)
                ok(f"Wrote {unit_dest}")
                run(["systemctl", "--user", "daemon-reload"], check=False)
                ok("systemd user daemon reloaded")
                info("Enable for reboot: systemctl --user enable assistant-" + name)
                info("Start now:        systemctl --user start  assistant-" + name)

    # 6. surfaces
    stage("[6/6] Wire surfaces (multica · wiki · docs · claude-os · etc.)")
    surfaces_path = GLOBAL_DIR / "surfaces.yaml"
    if surfaces_path.exists():
        surfaces = load_yaml(surfaces_path)
        available = []
        for sname, sdef in surfaces.get("surfaces", {}).items():
            detect_cmd = sdef.get("detect")
            present = bool(detect_cmd and have(detect_cmd.split()[0])) if detect_cmd else False
            if present:
                available.append(sname)
                ok(f"surface DETECTED: {sname}")
            else:
                info(f"surface absent:  {sname} (skipped)")
        info(f"Detected {len(available)} surface(s). Configure per-profile via `assistant surfaces enable {name} <surface>`")
    else:
        info(f"No surfaces config at {surfaces_path} — skipping surface wiring")

    print()
    stage(f"Install complete for {name}")
    info(f"Next: {BOLD}{sys.argv[0]} up {name}{RESET}  (start the assistant)")
    info(f"Then: interact via your usual OpenClaw channels (Slack/Discord/Telegram/CLI)")
    info(f"Reboot-persist: systemctl --user enable assistant-{name}")
    return 0


# ───────────────────────────────────────────────────────────────────────
# Subcommand: up / down / restart / status / logs
# ───────────────────────────────────────────────────────────────────────


def cmd_up(args: argparse.Namespace) -> int:
    name = args.profile
    stage(f"Start assistant: {name}")
    # Check assistant is installed in openclaw config
    cfg = load_openclaw_config()
    agents = cfg.get("agents", {}).get("list", [])
    if not any(a.get("id") == name for a in agents):
        err(f"Profile '{name}' not installed in ~/.openclaw/openclaw.json")
        info(f"Run: {sys.argv[0]} install {name}")
        return 1
    ok(f"Agent entry present in OpenClaw config")
    # Try systemd first; fall back to direct openclaw daemon
    unit = f"assistant-{name}"
    if have("systemctl"):
        proc = run(["systemctl", "--user", "start", unit], check=False)
        if proc.returncode == 0:
            ok(f"Started via systemd: {unit}")
            info(f"Status: systemctl --user status {unit}")
            info(f"Logs:   journalctl --user -u {unit} -f")
            return 0
        else:
            warn(f"systemd start failed: {proc.stderr.strip()} — falling back to direct daemon")
    # Direct daemon — but OpenClaw's daemon is one process per ~/.openclaw/openclaw.json
    # If a daemon is already running for another agent, this is a no-op (the existing daemon
    # will pick up the new agent on its next config reload).
    info("OpenClaw daemon is shared across all agents in ~/.openclaw/openclaw.json.")
    info("Starting (or signaling reload of) the daemon...")
    if have("openclaw"):
        proc = run(["openclaw", "daemon", "start"], check=False)
        if proc.returncode == 0:
            ok("OpenClaw daemon started (or already running)")
        else:
            warn(f"openclaw daemon start: {proc.stderr.strip()}")
            info("Some OpenClaw builds may use a different command. Try: openclaw start | openclaw run")
    return 0


def cmd_down(args: argparse.Namespace) -> int:
    name = args.profile
    stage(f"Stop assistant: {name}")
    unit = f"assistant-{name}"
    if have("systemctl"):
        proc = run(["systemctl", "--user", "stop", unit], check=False)
        if proc.returncode == 0:
            ok(f"Stopped via systemd: {unit}")
        else:
            info(f"systemd stop: {proc.stderr.strip()}")
    # Note: NOT stopping the OpenClaw daemon — it's shared across all agents.
    # To stop, the agent entry is removed/disabled in the config; daemon stays running for others.
    info("OpenClaw daemon is shared; not stopping it. To deactivate the agent")
    info(f"entry, use: {sys.argv[0]} uninstall {name}  (preserves Profile YAML).")
    return 0


def cmd_restart(args: argparse.Namespace) -> int:
    cmd_down(args)
    return cmd_up(args)


def cmd_status(args: argparse.Namespace) -> int:
    stage("Assistant Status")
    # Pull gateway state once per status call
    gateway_agents = ""
    gateway_mcp = ""
    gateway_cron = ""
    if have("openclaw"):
        proc = run(["openclaw", "agents", "list"], check=False)
        gateway_agents = proc.stdout if proc.returncode == 0 else ""
        proc = run(["openclaw", "mcp", "list"], check=False)
        gateway_mcp = proc.stdout if proc.returncode == 0 else ""
        proc = run(["openclaw", "cron", "list"], check=False)
        gateway_cron = proc.stdout if proc.returncode == 0 else ""
    if args.profile:
        names = [args.profile]
    else:
        names = list_profiles()
    # Print a one-time gateway summary at the top
    print()
    print(f"{BOLD}OpenClaw gateway{RESET}")
    if gateway_mcp and "wiki-llm" in gateway_mcp:
        ok("project MCP server 'wiki-llm': registered (wiki_* tools available to all agents)")
    elif have("openclaw"):
        warn("project MCP server 'wiki-llm': NOT registered (run install to wire it)")
    else:
        info("openclaw CLI not on PATH")
    for name in names:
        print()
        print(f"{BOLD}{name}{RESET}")
        # 1. Profile YAML present + workspace_mode resolved?
        if profile_path(name).exists():
            ok(f"Profile YAML: present ({profile_path(name).name})")
            profile = load_yaml(profile_path(name))
            ws_mode = profile.get("workspace_mode", "shared")
            ws_path = compute_workspace_path(name, ws_mode) if ws_mode in WORKSPACE_MODES else None
            if ws_mode in WORKSPACE_MODES:
                ok(f"workspace_mode: {ws_mode}")
                exists = ws_path and ws_path.exists()
                marker = "exists" if exists else "NOT materialized (run install)"
                ok(f"workspace path: {ws_path} ({marker})")
            else:
                err(f"workspace_mode INVALID: {ws_mode} (must be one of {sorted(WORKSPACE_MODES.keys())})")
        else:
            err("Profile YAML: missing")
            continue
        # 2. OpenClaw vendor config?
        vp = vendor_path(name, "openclaw", "json5")
        if vp.exists():
            ok(f"OpenClaw vendor config: present ({vp.name})")
        else:
            warn("OpenClaw vendor config: absent")
        # 3. Agent registered in OpenClaw gateway?
        if gateway_agents and f"- {name} " in gateway_agents:
            ok("Agent registered in OpenClaw gateway: YES")
        else:
            warn("Agent registered in OpenClaw gateway: NO  (run `bin/assistant install`)")
        # 4. Cron jobs registered in gateway?
        cron_path = ASSISTANT_DIR / f"{name}.cron.yaml"
        if cron_path.exists():
            cron = load_yaml(cron_path)
            jobs = cron.get("jobs", [])
            yaml_count = len(jobs)
            gw_count = sum(1 for j in jobs if f"{name}-{j['name']}" in gateway_cron)
            ok(f"Cron jobs: {yaml_count} defined in yaml, {gw_count} registered in gateway")
        else:
            info("Cron jobs: none defined")
        # 5. Gateway daemon systemd unit (now refers to OpenClaw's own gateway service, not per-agent)
        if have("systemctl"):
            proc = run(["systemctl", "--user", "is-active", "openclaw-gateway"], check=False)
            state = proc.stdout.strip()
            if state == "active":
                ok(f"OpenClaw gateway service: {state}")
            else:
                info(f"OpenClaw gateway service: {state}")
    return 0


def cmd_logs(args: argparse.Namespace) -> int:
    name = args.profile
    unit = f"assistant-{name}"
    if not have("journalctl"):
        err("journalctl not available")
        return 1
    info(f"Following logs for {unit} (Ctrl+C to exit)...")
    os.execvp("journalctl", ["journalctl", "--user", "-u", unit, "-f", "-n", "200"])


# ───────────────────────────────────────────────────────────────────────
# Subcommand: config
# ───────────────────────────────────────────────────────────────────────


def cmd_config(args: argparse.Namespace) -> int:
    if args.action == "show":
        name = args.profile
        p = profile_path(name)
        if p.exists():
            stage(f"Profile YAML: {p}")
            print(p.read_text())
        for vendor in VENDORS:
            for ext in ("json5", "yaml", "json", "toml"):
                vp = ASSISTANT_DIR / f"{name}.{vendor}.{ext}"
                if vp.exists():
                    stage(f"Vendor config ({vendor}): {vp}")
                    print(vp.read_text())
        return 0
    elif args.action == "edit":
        name = args.profile
        vendor = args.vendor
        # Find file
        for ext in ("json5", "yaml", "json", "toml"):
            vp = ASSISTANT_DIR / f"{name}.{vendor}.{ext}"
            if vp.exists():
                editor = os.environ.get("EDITOR", "nano")
                os.execvp(editor, [editor, str(vp)])
        err(f"No vendor config for {name}.{vendor}")
        return 1
    elif args.action == "sync":
        warn("config sync not yet implemented (planned: re-render vendor configs from Profile)")
        return 0
    return 1


# ───────────────────────────────────────────────────────────────────────
# Subcommand: cron
# ───────────────────────────────────────────────────────────────────────


def cmd_cron(args: argparse.Namespace) -> int:
    if args.action == "list":
        if args.profile_or_global == "--global":
            cron_path = GLOBAL_DIR / "cron.yaml"
            scope = "GLOBAL"
        else:
            cron_path = ASSISTANT_DIR / f"{args.profile_or_global}.cron.yaml"
            scope = args.profile_or_global
        stage(f"Cron jobs ({scope})")
        if not cron_path.exists():
            warn(f"No cron file at {cron_path}")
            return 0
        cron = load_yaml(cron_path)
        # Pull gateway-registered jobs once to mark which yaml jobs are live
        gateway_output = ""
        if have("openclaw"):
            proc = run(["openclaw", "cron", "list"], check=False)
            gateway_output = proc.stdout if proc.returncode == 0 else ""
        for j in cron.get("jobs", []):
            yaml_enabled = j.get("enabled", False)
            gateway_job_name = f"{args.profile_or_global}-{j['name']}" if scope != "GLOBAL" else j["name"]
            in_gateway = gateway_job_name in gateway_output
            yaml_mark = f"{GREEN}●{RESET}" if yaml_enabled else f"{DIM}○{RESET}"
            gw_mark = f"{GREEN}gateway:✓{RESET}" if in_gateway else f"{DIM}gateway:—{RESET}"
            print(f"  {yaml_mark} {BOLD}{j['name']}{RESET} — {j.get('schedule')}  [{gw_mark}]")
            print(f"     {j.get('description', '')}")
        return 0
    elif args.action in ("enable", "disable"):
        cron_path = ASSISTANT_DIR / f"{args.profile_or_global}.cron.yaml"
        if not cron_path.exists():
            err(f"No cron file at {cron_path}")
            return 1
        cron = load_yaml(cron_path)
        jobs = cron.get("jobs", [])
        target = next((j for j in jobs if j["name"] == args.job), None)
        if not target:
            err(f"Job not found: {args.job}")
            return 1
        target["enabled"] = (args.action == "enable")
        try:
            import yaml
            with open(cron_path, "w") as f:
                yaml.dump(cron, f, sort_keys=False)
            ok(f"yaml: set {args.job} → enabled={target['enabled']}")
        except ImportError:
            err("PyYAML required")
            return 2
        # Propagate to gateway if openclaw is on PATH and the job is already registered
        if have("openclaw"):
            gateway_job_name = f"{args.profile_or_global}-{args.job}"
            proc = run(["openclaw", "cron", args.action, gateway_job_name], check=False)
            if proc.returncode == 0:
                ok(f"gateway: openclaw cron {args.action} {gateway_job_name}")
            else:
                info(f"gateway: openclaw cron {args.action} {gateway_job_name} → {proc.stderr.strip()[:120]}")
                info(f"  (Job may not be registered in gateway yet — run `bin/assistant install {args.profile_or_global}` first)")
        return 0
    elif args.action == "status":
        # Gateway cron status
        if not have("openclaw"):
            warn("openclaw not on PATH")
            return 1
        stage("Gateway cron status (`openclaw cron status`)")
        proc = run(["openclaw", "cron", "status"], check=False, capture=False)
        return proc.returncode
    elif args.action == "install":
        if args.profile_or_global == "--global":
            # Reuse cmd_cron_install_global; need to fake dry_run attr
            class _A: dry_run = False
            return cmd_cron_install_global(_A())
        info("Profile cron registration is now done in `bin/assistant install <profile>` step [4/6].")
        info(f"Run: bin/assistant install {args.profile_or_global}")
        return 0
    return 1


# ───────────────────────────────────────────────────────────────────────
# Subcommand: surfaces
# ───────────────────────────────────────────────────────────────────────


def cmd_surfaces(args: argparse.Namespace) -> int:
    surfaces_path = GLOBAL_DIR / "surfaces.yaml"
    if args.action == "list":
        stage("Available surfaces")
        if not surfaces_path.exists():
            warn(f"No surfaces config at {surfaces_path}")
            return 0
        surfaces = load_yaml(surfaces_path)
        for sname, sdef in surfaces.get("surfaces", {}).items():
            detect = sdef.get("detect", "")
            present = bool(detect and have(detect.split()[0])) if detect else False
            mark = f"{GREEN}●{RESET}" if present else f"{DIM}○{RESET}"
            print(f"  {mark} {BOLD}{sname}{RESET} — {sdef.get('description', '')}")
            print(f"     detect: {detect or '(none)'}")
        return 0
    warn(f"surface {args.action} not yet wired (planned)")
    return 0


# ───────────────────────────────────────────────────────────────────────
# Subcommand: uninstall
# ───────────────────────────────────────────────────────────────────────


def cmd_uninstall(args: argparse.Namespace) -> int:
    name = args.profile
    stage(f"Uninstall {name} (preserves Profile YAML + vendor configs)")
    # Determine workspace_mode from Profile (need it to decide whether to remove worktree/clone)
    profile = load_yaml(profile_path(name)) if profile_path(name).exists() else {}
    ws_mode = profile.get("workspace_mode", "shared")
    # Remove from openclaw config
    cfg = load_openclaw_config()
    agents = cfg.get("agents", {}).get("list", [])
    before = len(agents)
    cfg["agents"]["list"] = [a for a in agents if a.get("id") != name]
    if len(cfg["agents"]["list"]) < before:
        save_openclaw_config(cfg)
        ok(f"Removed agent entry from {OPENCLAW_CONFIG}")
    else:
        info("Agent entry not present in OpenClaw config")
    # Disable + remove systemd unit
    unit = f"assistant-{name}"
    if have("systemctl"):
        run(["systemctl", "--user", "stop", unit], check=False)
        run(["systemctl", "--user", "disable", unit], check=False)
    unit_file = SYSTEMD_USER_DIR / f"{unit}.service"
    if unit_file.exists():
        unit_file.unlink()
        ok(f"Removed {unit_file}")
        run(["systemctl", "--user", "daemon-reload"], check=False)
    # Workspace cleanup — only for non-shared modes (shared mode = project folder, NEVER delete)
    if ws_mode == "shared":
        info("workspace_mode=shared — project folder is the workspace; NOT touching it")
    elif ws_mode == "worktree":
        ws_path = compute_workspace_path(name, ws_mode)
        if ws_path.exists():
            if args.remove_workspace:
                info(f"Removing git worktree at {ws_path}")
                run(["git", "-C", str(PROJECT_ROOT), "worktree", "remove", "--force", str(ws_path)], check=False)
                ok(f"git worktree removed")
            else:
                info(f"worktree preserved at {ws_path} (use --remove-workspace to delete)")
    elif ws_mode == "own-workspace":
        ws_path = compute_workspace_path(name, ws_mode)
        if ws_path.exists():
            if args.remove_workspace:
                info(f"Removing own-workspace clone at {ws_path}")
                shutil.rmtree(ws_path)
                ok(f"clone removed")
            else:
                info(f"clone preserved at {ws_path} (use --remove-workspace to delete)")
    info("Profile YAML + vendor configs preserved at .assistant/ (not deleted)")
    return 0


def cmd_cron_install_global(args: argparse.Namespace) -> int:
    """Register global gateway cron jobs (no specific agent) — one-time setup.

    Per operator: profile cron has --agent <id>; global cron has NO --agent.

    Two paths depending on trigger.type:
      - trigger.type=shell    → systemd user timer (openclaw cron doesn't run shell natively)
      - trigger.type=agent    → openclaw cron add --cron <expr> --agent <id> --message ...
      - trigger.type=system-event → openclaw cron add --cron <expr> --system-event ... WITHOUT --agent
    """
    stage("Install global gateway cron jobs (from .assistant/_global/cron.yaml)")
    cron_path = GLOBAL_DIR / "cron.yaml"
    if not cron_path.exists():
        err(f"No global cron file at {cron_path}")
        return 1
    cron = load_yaml(cron_path)
    jobs = cron.get("jobs", [])
    ok(f"Found {len(jobs)} global cron job(s)")
    # Lists pulled once for idempotency
    gateway_cron_output = ""
    if have("openclaw"):
        proc = run(["openclaw", "cron", "list"], check=False)
        gateway_cron_output = proc.stdout if proc.returncode == 0 else ""
    timers_installed = 0
    gateway_jobs_registered = 0
    for j in jobs:
        job_name = j["name"]  # global jobs NOT prefixed (already in global scope)
        enabled = j.get("enabled", True)
        trigger = j.get("trigger", {})
        ttype = trigger.get("type", "shell")
        schedule = j.get("schedule", "")
        description = j.get("description", "")
        if ttype == "shell":
            # Systemd user timer path (openclaw cron does not run shell directly)
            cmd_str = trigger.get("command", "")
            cwd = trigger.get("cwd", "{{PROJECT_ROOT}}").replace("{{PROJECT_ROOT}}", str(PROJECT_ROOT))
            # Substitutions
            command = cmd_str.replace("{{PROJECT_ROOT}}", str(PROJECT_ROOT)).replace(
                "{{PROJECT}}", PROJECT_ROOT.name)
            svc_template = TEMPLATES_DIR / "assistant-cron.service.template"
            tmr_template = TEMPLATES_DIR / "assistant-cron.timer.template"
            if not (svc_template.exists() and tmr_template.exists()):
                err(f"systemd templates missing at {TEMPLATES_DIR}")
                return 1
            svc_content = svc_template.read_text() \
                .replace("{{PROFILE_NAME}}", "_global") \
                .replace("{{JOB_NAME}}", job_name) \
                .replace("{{PROJECT_ROOT}}", str(PROJECT_ROOT)) \
                .replace("{{TRIGGER_COMMAND}}", command)
            tmr_content = tmr_template.read_text() \
                .replace("{{PROFILE_NAME}}", "_global") \
                .replace("{{JOB_NAME}}", job_name) \
                .replace("{{PROJECT_ROOT}}", str(PROJECT_ROOT)) \
                .replace("{{SCHEDULE}}", schedule)
            svc_dest = SYSTEMD_USER_DIR / f"assistant-cron-_global-{job_name}.service"
            tmr_dest = SYSTEMD_USER_DIR / f"assistant-cron-_global-{job_name}.timer"
            info(f"  - {job_name} (shell): {schedule}  →  systemd timer  {'(enabled)' if enabled else '(disabled)'}")
            info(f"    command: {command}")
            if args.dry_run:
                info(f"    DRY RUN — would write {svc_dest.name} + {tmr_dest.name}")
                continue
            SYSTEMD_USER_DIR.mkdir(parents=True, exist_ok=True)
            svc_dest.write_text(svc_content)
            tmr_dest.write_text(tmr_content)
            run(["systemctl", "--user", "daemon-reload"], check=False)
            if enabled:
                proc = run(["systemctl", "--user", "enable", "--now", tmr_dest.name], check=False)
                if proc.returncode == 0:
                    ok(f"    installed + started: {tmr_dest.name}")
                else:
                    warn(f"    timer install failed: {proc.stderr.strip()[:200]}")
            else:
                run(["systemctl", "--user", "disable", tmr_dest.name], check=False)
                ok(f"    installed (DISABLED): {tmr_dest.name}")
            timers_installed += 1
        elif ttype in ("agent", "system-event"):
            # OpenClaw gateway cron path — no --agent for global, --system-event for system events
            if not have("openclaw"):
                warn(f"  - {job_name}: openclaw not on PATH; skipping")
                continue
            if job_name in gateway_cron_output:
                info(f"  - {job_name}: already registered in gateway — skipping (idempotent)")
                continue
            translated = translate_schedule(schedule)
            if not translated:
                warn(f"  - {job_name}: unrecognized schedule '{schedule}' — skipping")
                continue
            flag, value = translated
            payload_flag = "--system-event" if ttype == "system-event" else "--message"
            payload = trigger.get("event", trigger.get("message", job_name))
            cmd = [
                "openclaw", "cron", "add",
                "--name", job_name,
                flag, value,
                payload_flag, payload,
                "--description", description,
            ]
            if not enabled:
                cmd.append("--disabled")
            info(f"  - {job_name} ({ttype}): {schedule} → {flag} {value}  ({'enabled' if enabled else 'disabled'})  [no --agent: global]")
            if args.dry_run:
                info(f"    DRY RUN — would run: {' '.join(cmd)}")
                continue
            proc = run(cmd, check=False)
            if proc.returncode == 0:
                ok(f"    registered: {job_name}")
                gateway_jobs_registered += 1
            else:
                warn(f"    openclaw cron add failed: {proc.stderr.strip()[:200]}")
        else:
            warn(f"  - {job_name}: unknown trigger.type '{ttype}' — skipping")
    print()
    ok(f"Global cron install summary: {timers_installed} systemd timer(s), {gateway_jobs_registered} gateway cron job(s)")
    return 0


def cmd_modes(_args: argparse.Namespace) -> int:
    stage("Workspace modes (set in Profile YAML as `workspace_mode: <mode>`)")
    for mode, spec in WORKSPACE_MODES.items():
        print()
        print(f"  {BOLD}{mode}{RESET}")
        print(f"     {spec['description']}")
        print(f"     writes visible to operator immediately: {spec['writes_visible_immediately']}")
        print(f"     git isolation: {spec['git_isolation']}")
        print(f"     best for: {spec['best_for']}")
    print()
    info("Switch a Profile's mode by editing `workspace_mode:` in .assistant/<profile>.yaml,")
    info("then re-running `assistant install <profile>` to re-materialize the workspace.")
    return 0


# ───────────────────────────────────────────────────────────────────────
# Main
# ───────────────────────────────────────────────────────────────────────


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="assistant",
        description="Per-Project AI Assistant lifecycle management",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__.split("USAGE\n=====")[1] if "USAGE\n=====" in __doc__ else "",
    )
    sub = p.add_subparsers(dest="cmd", required=True)

    sp = sub.add_parser("profiles", help="List known profiles")
    sp.set_defaults(func=cmd_profiles)

    sp = sub.add_parser("install", help="Install (one-shot end-to-end)")
    sp.add_argument("profile")
    sp.add_argument("--dry-run", action="store_true")
    sp.add_argument("--no-openclaw", action="store_true", help="Skip OpenClaw agent registration")
    sp.add_argument("--no-mcp", action="store_true", help="Skip wiring this project's MCP server into OpenClaw gateway")
    sp.add_argument("--no-cron", action="store_true", help="Skip registering per-profile cron jobs into the gateway")
    sp.set_defaults(func=cmd_install)

    sp = sub.add_parser("up", help="Start the assistant")
    sp.add_argument("profile")
    sp.set_defaults(func=cmd_up)

    sp = sub.add_parser("down", help="Stop the assistant")
    sp.add_argument("profile")
    sp.set_defaults(func=cmd_down)

    sp = sub.add_parser("restart", help="Restart")
    sp.add_argument("profile")
    sp.set_defaults(func=cmd_restart)

    sp = sub.add_parser("status", help="Status across surfaces")
    sp.add_argument("profile", nargs="?")
    sp.set_defaults(func=cmd_status)

    sp = sub.add_parser("logs", help="Tail logs")
    sp.add_argument("profile")
    sp.set_defaults(func=cmd_logs)

    sp = sub.add_parser("config", help="Show/edit/sync configs")
    sp.add_argument("action", choices=["show", "edit", "sync"])
    sp.add_argument("profile")
    sp.add_argument("vendor", nargs="?", default="openclaw")
    sp.set_defaults(func=cmd_config)

    sp = sub.add_parser("cron", help="Manage CRON jobs (per-profile or global)")
    sp.add_argument("action", choices=["list", "enable", "disable", "status", "install"])
    sp.add_argument("profile_or_global", help="<profile-name> or --global")
    sp.add_argument("job", nargs="?")
    sp.set_defaults(func=cmd_cron)

    sp = sub.add_parser("surfaces", help="Manage surface integrations")
    sp.add_argument("action", choices=["list", "enable", "disable"])
    sp.add_argument("profile", nargs="?")
    sp.add_argument("surface", nargs="?")
    sp.set_defaults(func=cmd_surfaces)

    sp = sub.add_parser("uninstall", help="Remove assistant install (keeps Profile)")
    sp.add_argument("profile")
    sp.add_argument("--remove-workspace", action="store_true",
                    help="For worktree/own-workspace modes, also delete the workspace directory.")
    sp.set_defaults(func=cmd_uninstall)

    sp = sub.add_parser("modes", help="Show available workspace_mode values + tradeoffs")
    sp.set_defaults(func=cmd_modes)

    sp = sub.add_parser("install-global", help="Install global gateway cron jobs (one-time, no --agent)")
    sp.add_argument("--dry-run", action="store_true")
    sp.set_defaults(func=cmd_cron_install_global)

    return p


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
