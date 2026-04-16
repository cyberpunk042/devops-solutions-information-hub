"""Cross-platform setup for the DevOps Solutions Research Wiki.

Replaces bash scripts for environments where bash isn't available (Windows).
Works on Linux, macOS, and Windows.

Usage:
    python3 -m tools.setup                         # Full setup
    python3 -m tools.setup --deps                  # Install dependencies only
    python3 -m tools.setup --check                 # Check environment only
    python3 -m tools.setup --obsidian-config       # Configure Obsidian vault
    python3 -m tools.setup --services              # List available services
    python3 -m tools.setup --services wiki-sync    # Deploy sync daemon (auto-detect target)
    python3 -m tools.setup --services wiki-sync --target /mnt/c/Users/You/vault  # Custom target
    python3 -m tools.setup --services wiki-watcher # Deploy watcher daemon
"""

import argparse
import json
import os
import platform
import shutil
import subprocess
import sys
from pathlib import Path

from tools.common import get_project_root


def is_windows() -> bool:
    return platform.system() == "Windows"


def is_wsl() -> bool:
    try:
        return "microsoft" in Path("/proc/version").read_text().lower()
    except (FileNotFoundError, OSError):
        return False


def log_info(msg: str):
    print(f"\033[0;32m[INFO]\033[0m {msg}")


def log_warn(msg: str):
    print(f"\033[0;33m[WARN]\033[0m {msg}")


def log_error(msg: str):
    print(f"\033[0;31m[ERROR]\033[0m {msg}", file=sys.stderr)


def venv_python(project_root: Path) -> Path:
    """Get the venv Python path (cross-platform)."""
    if is_windows():
        return project_root / ".venv" / "Scripts" / "python.exe"
    return project_root / ".venv" / "bin" / "python"


def venv_bin(project_root: Path, name: str) -> Path:
    """Get a venv binary path (cross-platform)."""
    if is_windows():
        p = project_root / ".venv" / "Scripts" / f"{name}.exe"
        if p.exists():
            return p
        return project_root / ".venv" / "Scripts" / name
    return project_root / ".venv" / "bin" / name


# ---------------------------------------------------------------------------
# Check environment
# ---------------------------------------------------------------------------

def check_environment(project_root: Path) -> dict:
    """Check what's available in the environment."""
    report = {
        "platform": platform.system(),
        "python_version": platform.python_version(),
        "is_wsl": is_wsl(),
        "uv": shutil.which("uv") is not None,
        "git": shutil.which("git") is not None,
        "obsidian_cli": shutil.which("obsidian") is not None,
        "venv_exists": (project_root / ".venv").exists(),
        "venv_python": venv_python(project_root).exists(),
    }

    # Check notebooklm in venv
    nlm_path = venv_bin(project_root, "notebooklm")
    report["notebooklm"] = nlm_path.exists()

    return report


def print_check(project_root: Path):
    """Print environment check report."""
    report = check_environment(project_root)

    log_info(f"Platform:       {report['platform']}" +
             (" (WSL)" if report["is_wsl"] else ""))
    log_info(f"Python:         {report['python_version']}")

    for key in ["uv", "git", "obsidian_cli", "venv_exists", "venv_python", "notebooklm"]:
        status = "YES" if report[key] else "NO"
        color = "\033[0;32m" if report[key] else "\033[0;33m"
        print(f"  {color}{key:20s}{status}\033[0m")

    if not report["uv"]:
        log_warn("uv not found. Install: https://docs.astral.sh/uv/getting-started/installation/")
    if not report["venv_exists"]:
        log_warn("No .venv — run: python -m tools.setup --deps")


# ---------------------------------------------------------------------------
# Install dependencies
# ---------------------------------------------------------------------------

def install_deps(project_root: Path):
    """Install dependencies via uv into .venv."""
    uv = shutil.which("uv")
    if not uv:
        log_error("uv not found. Install: https://docs.astral.sh/uv/getting-started/installation/")
        sys.exit(1)

    venv_dir = project_root / ".venv"

    # Create venv if needed
    if not venv_dir.exists():
        log_info("Creating Python 3.11 venv...")
        subprocess.run([uv, "venv", "--python", "3.11", str(venv_dir)], check=True)
    else:
        log_info(f"Venv exists at {venv_dir}")

    # Install packages
    log_info("Installing Python packages...")
    req_file = project_root / "requirements.txt"
    subprocess.run([uv, "pip", "install", "-r", str(req_file)], check=True)

    # Install Playwright chromium
    playwright = venv_bin(project_root, "playwright")
    if playwright.exists():
        log_info("Installing Playwright chromium...")
        subprocess.run([str(playwright), "install", "chromium"],
                       capture_output=True)
    else:
        log_warn("Playwright not found in venv — notebooklm login may not work")

    # Verify
    log_info("Verifying installations...")
    py = venv_python(project_root)
    subprocess.run([str(py), "-c", "import yaml; print(f'  PyYAML {yaml.__version__}')"])
    subprocess.run([str(py), "-c", "import youtube_transcript_api; print('  youtube-transcript-api OK')"])

    nlm = venv_bin(project_root, "notebooklm")
    if nlm.exists():
        result = subprocess.run([str(nlm), "--version"], capture_output=True, text=True)
        if result.returncode == 0:
            log_info(f"notebooklm-py: {result.stdout.strip()}")
        else:
            log_warn("notebooklm-py installed but not responding")

    # Integration check
    log_info("Integration status:")
    subprocess.run([str(py), "-m", "tools.pipeline", "integrations"])

    log_info("Done.")


# ---------------------------------------------------------------------------
# Configure Obsidian vault
# ---------------------------------------------------------------------------

def configure_obsidian(project_root: Path):
    """Set up Obsidian vault configuration in wiki/.obsidian/."""
    obsidian_dir = project_root / "wiki" / ".obsidian"
    obsidian_dir.mkdir(parents=True, exist_ok=True)

    # app.json — basic settings
    app_config = {
        "livePreview": True,
        "readableLineLength": True,
        "showLineNumber": True,
        "strictLineBreaks": False,
    }
    (obsidian_dir / "app.json").write_text(json.dumps(app_config, indent=2))

    # core-plugins.json — enable graph, backlinks, search
    core_plugins = [
        "file-explorer", "global-search", "graph", "backlink",
        "tag-pane", "page-preview", "templates", "command-palette",
        "markdown-importer", "outline",
    ]
    (obsidian_dir / "core-plugins.json").write_text(json.dumps(core_plugins, indent=2))

    # graph.json — color groups per domain
    graph_config = {
        "collapse-filter": False,
        "search": "",
        "showTags": False,
        "showAttachments": False,
        "hideUnresolved": False,
        "showOrphans": True,
        "collapse-color-groups": False,
        "colorGroups": [
            {"query": "path:domains/ai-agents", "color": {"a": 1, "rgb": 14701138}},
            {"query": "path:domains/knowledge-systems", "color": {"a": 1, "rgb": 5431378}},
            {"query": "path:domains/automation", "color": {"a": 1, "rgb": 16098048}},
            {"query": "path:domains/tools-and-platforms", "color": {"a": 1, "rgb": 8564738}},
            {"query": "path:domains/devops", "color": {"a": 1, "rgb": 16750848}},
            {"query": "path:sources", "color": {"a": 1, "rgb": 11184810}},
            {"query": "path:comparisons", "color": {"a": 1, "rgb": 16777045}},
            {"query": "path:lessons", "color": {"a": 1, "rgb": 3394611}},
            {"query": "path:patterns", "color": {"a": 1, "rgb": 3381759}},
            {"query": "path:decisions", "color": {"a": 1, "rgb": 16753920}},
            {"query": "path:spine", "color": {"a": 1, "rgb": 16766720}},
        ],
        "collapse-display": False,
        "lineSizeMultiplier": 1,
        "nodeSizeMultiplier": 1,
        "textFadeMultiplier": 0,
        "collapse-forces": False,
        "centerStrength": 0.518713248970312,
        "repelStrength": 10,
        "linkStrength": 1,
        "linkDistance": 250,
    }
    (obsidian_dir / "graph.json").write_text(json.dumps(graph_config, indent=2))

    log_info(f"Obsidian vault configured at {obsidian_dir}")

    # Run manifest + obsidian wikilinks
    py = venv_python(project_root)
    if py.exists():
        log_info("Regenerating manifest and wikilinks...")
        subprocess.run([str(py), "-m", "tools.pipeline", "post"])
    else:
        log_warn("Venv not found — run tools.setup --deps first, then tools.pipeline post")


# ---------------------------------------------------------------------------
# Service deployment (systemd)
# ---------------------------------------------------------------------------

def list_services(project_root: Path):
    """List available service templates and their install status."""
    template_dir = project_root / "services"
    if not template_dir.exists():
        log_error("No service templates found in services/")
        return

    systemd_dir = Path.home() / ".config" / "systemd" / "user"

    log_info("Available services:")
    for template in sorted(template_dir.glob("*.service.template")):
        name = template.name.replace(".service.template", "")
        unit_path = systemd_dir / f"{name}.service"
        installed = unit_path.exists()

        running = False
        if installed:
            result = subprocess.run(
                ["systemctl", "--user", "is-active", name],
                capture_output=True, text=True,
            )
            running = result.stdout.strip() == "active"

        status_parts = []
        if installed:
            status_parts.append("installed")
        if running:
            status_parts.append("running")
        status = ", ".join(status_parts) if status_parts else "not installed"

        print(f"  {name:20s}  [{status}]")

    print()
    log_info("Deploy with: python -m tools.setup --services <name>")
    log_info("Manage with: systemctl --user start|stop|status <name>")
    log_info("View logs:   journalctl --user -u <name> -f")


def install_service(service_name: str, project_root: Path, target: str = None) -> bool:
    """Generate and enable a systemd user service from template."""
    if not is_wsl() and platform.system() != "Linux":
        log_error("systemd services only supported on Linux/WSL")
        return False

    template_dir = project_root / "services"
    template_path = template_dir / f"{service_name}.service.template"

    if not template_path.exists():
        log_error(f"No template for service: {service_name}")
        available = [
            f.name.replace(".service.template", "")
            for f in template_dir.glob("*.service.template")
        ]
        if available:
            log_info(f"Available: {', '.join(available)}")
        return False

    content = template_path.read_text(encoding="utf-8")
    content = content.replace("{{project_root}}", str(project_root))
    content = content.replace("{{venv_python}}", str(venv_python(project_root)))

    # Resolve sync target for wiki-sync service
    resolved_target = None
    if "{{sync_target}}" in content:
        if target:
            resolved_target = target
        else:
            from tools.sync import get_sync_config
            sync_config = get_sync_config(project_root)
            resolved_target = sync_config.get("target", "")
        if not resolved_target:
            log_error("No sync target. Use: setup.py --services wiki-sync --target /mnt/c/Users/You/path")
            return False
        log_info(f"Sync target: {resolved_target}")
        content = content.replace("{{sync_target}}", resolved_target)

    # Resolve sync mode (default: repo)
    if "{{sync_mode}}" in content:
        sync_mode = os.environ.get("WIKI_SYNC_MODE", "repo")
        content = content.replace("{{sync_mode}}", sync_mode)
        log_info(f"Sync mode: {sync_mode}")

    # Create sync target directory if needed
    if resolved_target:
        target_path = Path(resolved_target)
        if not target_path.exists():
            target_path.mkdir(parents=True, exist_ok=True)
            log_info(f"Created target directory: {resolved_target}")

    systemd_dir = Path.home() / ".config" / "systemd" / "user"
    systemd_dir.mkdir(parents=True, exist_ok=True)
    unit_path = systemd_dir / f"{service_name}.service"
    unit_path.write_text(content, encoding="utf-8")
    log_info(f"Unit file written: {unit_path}")

    subprocess.run(["systemctl", "--user", "daemon-reload"], check=True)
    subprocess.run(["systemctl", "--user", "enable", service_name], check=True)
    # restart (not start) in case service is already running with old config
    subprocess.run(["systemctl", "--user", "restart", service_name], check=True)

    log_info(f"Service '{service_name}' installed and started")
    log_info(f"  Status:  systemctl --user status {service_name}")
    log_info(f"  Logs:    journalctl --user -u {service_name} -f")
    log_info(f"  Stop:    systemctl --user stop {service_name}")
    log_info(f"  Disable: systemctl --user disable {service_name}")
    return True


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def find_second_brain() -> Path:
    """Auto-detect the second brain location.

    Searches common locations for the research wiki.
    Returns resolved path or None.
    """
    names = ["devops-solutions-information-hub", "devops-solutions-research-wiki"]
    search_dirs = [Path.cwd().parent, Path.home()]
    for d in search_dirs:
        for n in names:
            candidate = d / n
            if (candidate / "wiki" / "config" / "sister-projects.yaml").exists():
                return candidate.resolve()
    return None


def connect_second_brain(project_root: Path, brain_path: Path = None):
    """Connect a sister project to the second brain.

    Adds/updates the research-wiki MCP server entry in the project's .mcp.json.
    Also prints the gateway orient output for verification.

    Usage from any sister project:
        python3 <second-brain>/tools/setup.py --connect
        python3 <second-brain>/tools/setup.py --connect --brain /path/to/second-brain

    Or from the second brain itself targeting a sister:
        python3 -m tools.setup --connect-project ~/openarms
    """
    if brain_path is None:
        brain_path = find_second_brain()
    if brain_path is None:
        log_error("Cannot find the second brain. Pass --brain <path> or clone it next to this project.")
        return False

    brain_path = Path(brain_path).resolve()
    venv = brain_path / ".venv" / "bin" / "python"
    if not venv.exists():
        venv = brain_path / ".venv" / "Scripts" / "python.exe"  # Windows
    if not venv.exists():
        log_warn(f"Second brain venv not found at {brain_path}/.venv — using system python")
        venv = Path(shutil.which("python3") or "python3")

    # Build MCP server config
    mcp_entry = {
        "command": str(venv),
        "args": ["-m", "tools.mcp_server"],
        "cwd": str(brain_path),
    }

    # Read or create .mcp.json
    mcp_json_path = project_root / ".mcp.json"
    if mcp_json_path.exists():
        try:
            mcp_config = json.loads(mcp_json_path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            mcp_config = {}
    else:
        mcp_config = {}

    if "mcpServers" not in mcp_config:
        mcp_config["mcpServers"] = {}

    mcp_config["mcpServers"]["research-wiki"] = mcp_entry

    mcp_json_path.write_text(json.dumps(mcp_config, indent=2) + "\n", encoding="utf-8")

    # Create CLI forwarding scripts so gateway + view work from the sister
    _install_gateway_forwarder(project_root, brain_path, venv)
    _install_view_forwarder(project_root, brain_path, venv)

    # Add second-brain connection block to AGENTS.md (or CLAUDE.md) if not already present
    _inject_brain_pointer(project_root, brain_path)

    log_info(f"Connected to second brain: {brain_path}")
    log_info(f"  MCP entry:  {mcp_json_path}")
    log_info(f"  CLI:        python3 -m tools.gateway orient")
    log_info(f"              python3 -m tools.view spine")
    log_info(f"  MCP:        wiki_gateway_orient (from Claude Code)")
    return True


_BRAIN_POINTER_MARKER = "<!-- SECOND-BRAIN-CONNECTION -->"

_BRAIN_POINTER_BLOCK = """
{marker}
## Second Brain Connection

This project is connected to the **second brain** (research wiki) — a shared
knowledge system holding methodology, standards, validated lessons, patterns,
and decisions across the ecosystem.

**Your brain** (this CLAUDE.md/AGENTS.md + skills + hooks) is YOUR agent.
**The second brain** is a SEPARATE system. The goal is NOT runtime dependency —
it's to ADOPT what fits your identity and EVOLVE your own brain.

**Adoption tiers** — check where you are: `python3 -m tools.gateway compliance`
- Tier 1: Agent foundation (schema + templates)
- Tier 2: Stage-gate process (methodology + backlog + enforcement)
- Tier 3: Evolution pipeline (maturity lifecycle + scoring)
- Tier 4: Hub integration (bidirectional sync + export + contribute)

**First step for any fresh session:** `python3 -m tools.gateway orient`

**Browse the second brain's knowledge:**
```
python3 -m tools.view spine          # all 16 models, standards, sub-models
python3 -m tools.view standards      # what "good" looks like per artifact type
python3 -m tools.view model <name>   # one model in full
python3 -m tools.view lessons        # 44 validated operational lessons
python3 -m tools.view search <query> # search across all knowledge
```

**Contribute learnings back:** `python3 -m tools.gateway contribute --type lesson --title "..."`
{marker_end}
"""


def _inject_brain_pointer(project_root: Path, brain_path: Path):
    """Add or update the second-brain connection block in AGENTS.md or CLAUDE.md.

    If the marker block exists, REPLACES it (so re-connect updates the content).
    Prefers AGENTS.md (cross-tool); falls back to CLAUDE.md.
    """
    marker_end = _BRAIN_POINTER_MARKER.replace("-->", "-END -->")
    block = _BRAIN_POINTER_BLOCK.format(
        marker=_BRAIN_POINTER_MARKER,
        marker_end=marker_end,
    )

    for fname in ["AGENTS.md", "CLAUDE.md"]:
        target = project_root / fname
        if target.exists():
            content = target.read_text(encoding="utf-8")
            if _BRAIN_POINTER_MARKER in content and marker_end in content:
                # Replace existing block
                start = content.index(_BRAIN_POINTER_MARKER)
                end = content.index(marker_end) + len(marker_end)
                content = content[:start] + block.strip() + content[end:]
                target.write_text(content, encoding="utf-8")
                log_info(f"  Brain pointer updated in: {target}")
            elif _BRAIN_POINTER_MARKER not in content:
                # First injection
                target.write_text(content + block, encoding="utf-8")
                log_info(f"  Brain pointer added to: {target}")
            return
    log_warn("  No AGENTS.md or CLAUDE.md found — skipping brain pointer injection")


def _install_gateway_forwarder(project_root: Path, brain_path: Path, venv: Path):
    """Create a thin tools/gateway.py in the sister project that forwards to the second brain.

    This allows `python3 -m tools.gateway orient` to work from any connected project.
    The forwarder passes --wiki-root pointing to the sister's CWD so the gateway
    knows which project it's being called from.

    If tools/gateway.py already exists and was NOT generated by us, it's left untouched.
    """
    tools_dir = project_root / "tools"
    gateway_file = tools_dir / "gateway.py"

    # Don't overwrite a real gateway.py that belongs to the project
    _marker = "# AUTO-GENERATED by second-brain setup --connect"
    if gateway_file.exists():
        existing = gateway_file.read_text(encoding="utf-8")
        if _marker not in existing:
            log_warn(f"  {gateway_file} exists (not ours) — skipping forwarder")
            return

    tools_dir.mkdir(parents=True, exist_ok=True)

    # Ensure tools/__init__.py exists so `python3 -m tools.gateway` resolves
    init_file = tools_dir / "__init__.py"
    if not init_file.exists():
        init_file.write_text(f"{_marker}\n", encoding="utf-8")

    forwarder = f'''{_marker}
# Forwards `python3 -m tools.gateway <args>` to the second brain's gateway.
# The second brain runs the real gateway; --wiki-root tells it which project called.
# Regenerate with: python3 <second-brain>/tools/setup.py --connect
"""Gateway forwarder to the second brain ({brain_path.name})."""

import os, subprocess, sys

_SECOND_BRAIN = {str(brain_path)!r}
_VENV_PYTHON = {str(venv)!r}

sys.exit(subprocess.call(
    [_VENV_PYTHON, "-m", "tools.gateway",
     "--wiki-root", os.getcwd()] + sys.argv[1:],
    cwd=_SECOND_BRAIN,
))
'''
    gateway_file.write_text(forwarder, encoding="utf-8")


def connect_all_sisters(brain_root: Path):
    """Connect all sister projects from sister-projects.yaml to the second brain.

    Reads the registry, resolves paths, connects each project that exists locally.
    """
    registry_path = brain_root / "wiki" / "config" / "sister-projects.yaml"
    if not registry_path.exists():
        log_error(f"sister-projects.yaml not found at {registry_path}")
        return False

    import yaml
    data = yaml.safe_load(registry_path.read_text(encoding="utf-8"))
    projects = data.get("projects", {})

    connected = 0
    skipped = 0
    for name, info in projects.items():
        raw_path = info.get("path", "")
        project_path = Path(os.path.expanduser(raw_path))
        if project_path.exists():
            success = connect_second_brain(project_path, brain_root)
            if success:
                connected += 1
            else:
                skipped += 1
        else:
            log_warn(f"  {name}: path {raw_path} not found locally — skipped")
            skipped += 1

    log_info(f"\nConnected: {connected} | Skipped: {skipped} | Total: {len(projects)}")
    return connected > 0


def _install_view_forwarder(project_root: Path, brain_path: Path, venv: Path):
    """Create a thin tools/view.py in the sister project that forwards to the second brain.

    Allows `python3 -m tools.view spine`, `python3 -m tools.view model llm`, etc.
    from any connected project.
    """
    tools_dir = project_root / "tools"
    view_file = tools_dir / "view.py"

    _marker = "# AUTO-GENERATED by second-brain setup --connect"
    if view_file.exists():
        existing = view_file.read_text(encoding="utf-8")
        if _marker not in existing:
            log_warn(f"  {view_file} exists (not ours) — skipping view forwarder")
            return

    tools_dir.mkdir(parents=True, exist_ok=True)

    forwarder = f'''{_marker}
# Forwards `python3 -m tools.view <args>` to the second brain's view tool.
# Regenerate with: python3 <second-brain>/tools/setup.py --connect
"""Wiki view forwarder to the second brain ({brain_path.name})."""

import os, subprocess, sys

_SECOND_BRAIN = {str(brain_path)!r}
_VENV_PYTHON = {str(venv)!r}

env = os.environ.copy()
env["WIKI_VIEW_CALLER_DIR"] = os.getcwd()

sys.exit(subprocess.call(
    [_VENV_PYTHON, "-m", "tools.view"] + sys.argv[1:],
    cwd=_SECOND_BRAIN,
    env=env,
))
'''
    view_file.write_text(forwarder, encoding="utf-8")


def disconnect_second_brain(project_root: Path):
    """Remove the second brain MCP server entry from a project's .mcp.json."""
    mcp_json_path = project_root / ".mcp.json"
    if not mcp_json_path.exists():
        log_info("No .mcp.json found — nothing to disconnect.")
        return

    try:
        mcp_config = json.loads(mcp_json_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return

    servers = mcp_config.get("mcpServers", {})
    if "research-wiki" in servers:
        del servers["research-wiki"]
        mcp_json_path.write_text(json.dumps(mcp_config, indent=2) + "\n", encoding="utf-8")
        log_info("Disconnected from second brain (removed research-wiki MCP entry).")
    else:
        log_info("No research-wiki MCP entry found — already disconnected.")


def main():
    parser = argparse.ArgumentParser(description="Cross-platform setup for the research wiki")
    parser.add_argument("--deps", action="store_true", help="Install dependencies only")
    parser.add_argument("--check", action="store_true", help="Check environment only")
    parser.add_argument("--obsidian-config", action="store_true", help="Configure Obsidian vault")
    parser.add_argument("--services", nargs="?", const="__list__", default=None,
                        metavar="NAME", help="Deploy a systemd service (or list available)")
    parser.add_argument("--target", help="Sync target path (for wiki-sync service)")
    parser.add_argument("--connect", action="store_true",
                        help="Connect THIS project to the second brain (adds MCP server to .mcp.json)")
    parser.add_argument("--connect-project", metavar="PATH",
                        help="Connect a SISTER project to the second brain")
    parser.add_argument("--connect-all", action="store_true",
                        help="Connect ALL sister projects from sister-projects.yaml")
    parser.add_argument("--disconnect", action="store_true",
                        help="Remove second brain MCP connection from THIS project")
    parser.add_argument("--brain", metavar="PATH",
                        help="Path to the second brain (auto-detected if not specified)")
    args = parser.parse_args()

    root = get_project_root()

    if args.connect:
        brain = Path(args.brain).resolve() if args.brain else None
        success = connect_second_brain(root, brain)
        sys.exit(0 if success else 1)
    elif args.connect_project:
        target = Path(args.connect_project).resolve()
        brain = Path(args.brain).resolve() if args.brain else root
        if not target.exists():
            log_error(f"Project path not found: {target}")
            sys.exit(1)
        success = connect_second_brain(target, brain)
        sys.exit(0 if success else 1)
    elif args.connect_all:
        brain = Path(args.brain).resolve() if args.brain else root
        connect_all_sisters(brain)
    elif args.disconnect:
        disconnect_second_brain(root)
    elif args.check:
        print_check(root)
    elif args.deps:
        install_deps(root)
    elif args.obsidian_config:
        configure_obsidian(root)
    elif args.services is not None:
        if args.services == "__list__":
            list_services(root)
        else:
            success = install_service(args.services, root, target=args.target)
            sys.exit(0 if success else 1)
    else:
        # Full setup
        log_info("=== Research Wiki Setup ===")
        print_check(root)
        print()
        install_deps(root)
        print()
        configure_obsidian(root)
        log_info("=== Setup complete ===")


if __name__ == "__main__":
    main()
