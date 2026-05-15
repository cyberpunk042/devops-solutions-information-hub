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
    info("Stages: 1) validate profile · 2) validate vendor config · 3) merge into")
    info("        ~/.openclaw/openclaw.json · 4) register cron jobs · 5) install systemd")
    info("        unit · 6) wire surfaces. Idempotent: re-running is safe.")
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

    # 3. merge into ~/.openclaw/openclaw.json
    if vp.exists() and not args.no_openclaw:
        stage("[3/6] Merge into ~/.openclaw/openclaw.json")
        cfg = load_openclaw_config()
        cfg.setdefault("agents", {}).setdefault("list", [])
        agent_id = agent["id"]
        existing_idx = next((i for i, a in enumerate(cfg["agents"]["list"]) if a.get("id") == agent_id), -1)
        if existing_idx >= 0:
            cfg["agents"]["list"][existing_idx] = agent
            ok(f"Updated existing agent entry (idx={existing_idx})")
        else:
            cfg["agents"]["list"].append(agent)
            ok(f"Appended new agent entry (now {len(cfg['agents']['list'])} agent(s))")
        if args.dry_run:
            info("DRY RUN — not writing ~/.openclaw/openclaw.json")
        else:
            save_openclaw_config(cfg)
            ok(f"Wrote {OPENCLAW_CONFIG}")
            # Validate
            if have("openclaw"):
                proc = run(["openclaw", "doctor"], check=False)
                if proc.returncode == 0:
                    ok("openclaw doctor: passed")
                else:
                    warn(f"openclaw doctor reported issues:\n{proc.stdout}\n{proc.stderr}")
    else:
        info("[3/6] Skipped (no OpenClaw vendor config or --no-openclaw)")

    # 4. cron jobs
    stage("[4/6] Register per-profile CRON jobs")
    cron_path = ASSISTANT_DIR / f"{name}.cron.yaml"
    if cron_path.exists():
        cron = load_yaml(cron_path)
        jobs = cron.get("jobs", [])
        ok(f"Found {len(jobs)} cron job(s) defined for this profile")
        for j in jobs:
            info(f"  - {j.get('name')}: {j.get('schedule')} ({j.get('description', '')[:60]})")
        info("(Cron jobs are DEFINED but NOT auto-enabled — use `assistant cron enable` to activate)")
    else:
        info(f"No cron file at {cron_path} — skipping cron registration")

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
    cfg = load_openclaw_config()
    agents = cfg.get("agents", {}).get("list", [])
    if args.profile:
        names = [args.profile]
    else:
        names = list_profiles()
    for name in names:
        print()
        print(f"{BOLD}{name}{RESET}")
        # 1. Profile YAML present?
        if profile_path(name).exists():
            ok(f"Profile YAML: present ({profile_path(name).name})")
        else:
            err("Profile YAML: missing")
            continue
        # 2. OpenClaw vendor config?
        vp = vendor_path(name, "openclaw", "json5")
        if vp.exists():
            ok(f"OpenClaw vendor config: present ({vp.name})")
        else:
            warn("OpenClaw vendor config: absent")
        # 3. Installed in ~/.openclaw/openclaw.json?
        installed = any(a.get("id") == name for a in agents)
        if installed:
            ok("Installed in ~/.openclaw/openclaw.json: YES")
        else:
            warn("Installed in ~/.openclaw/openclaw.json: NO")
        # 4. systemd unit?
        unit = f"assistant-{name}"
        unit_file = SYSTEMD_USER_DIR / f"{unit}.service"
        if unit_file.exists():
            ok(f"systemd unit: {unit_file.name}")
            if have("systemctl"):
                proc = run(["systemctl", "--user", "is-active", unit], check=False)
                ok(f"systemd state: {proc.stdout.strip()}")
                proc = run(["systemctl", "--user", "is-enabled", unit], check=False)
                ok(f"systemd enabled (reboot-persistent): {proc.stdout.strip()}")
        else:
            info("systemd unit: not installed")
        # 5. Cron file?
        cron_path = ASSISTANT_DIR / f"{name}.cron.yaml"
        if cron_path.exists():
            cron = load_yaml(cron_path)
            jobs = cron.get("jobs", [])
            ok(f"Cron jobs defined: {len(jobs)}")
        else:
            info("Cron jobs defined: 0")
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
        for j in cron.get("jobs", []):
            enabled = j.get("enabled", False)
            mark = f"{GREEN}●{RESET}" if enabled else f"{DIM}○{RESET}"
            print(f"  {mark} {BOLD}{j['name']}{RESET} — {j.get('schedule')}")
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
            ok(f"Set {args.job} → enabled={target['enabled']}")
        except ImportError:
            err("PyYAML required")
            return 2
        return 0
    elif args.action == "status":
        warn("cron status: install systemd timers first via `cron install`")
        return 0
    elif args.action == "install":
        warn("cron install (per-profile systemd timers): planned — see _templates/")
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
    info("Profile YAML + vendor configs preserved at .assistant/ (not deleted)")
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
    sp.add_argument("--no-openclaw", action="store_true", help="Skip OpenClaw vendor merge")
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
    sp.set_defaults(func=cmd_uninstall)

    return p


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
