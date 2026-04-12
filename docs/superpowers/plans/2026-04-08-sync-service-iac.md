# Sync Service IaC Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make wiki sync and watcher deployable as persistent systemd user services via `setup.py --services`, with version-controlled templates and opt-in activation.

**Architecture:** Service unit templates in `config/services/` with `{{placeholder}}` variables. `setup.py` gains `--services [name]` subcommand that fills templates, writes to `~/.config/systemd/user/`, and runs `systemctl --user enable/start`. Two independent services: wiki-sync (file sync) and wiki-watcher (change detection + post-chain).

**Tech Stack:** Python 3.11, systemd user units, existing tools/setup.py

---

### Task 1: Create Service Templates

**Files:**
- Create: `services/wiki-sync.service.template`
- Create: `services/wiki-watcher.service.template`

- [ ] **Step 1: Create the services directory**

```bash
mkdir -p services
```

- [ ] **Step 2: Create wiki-sync.service.template**

Create `services/wiki-sync.service.template`:

```ini
[Unit]
Description=Research Wiki Sync (WSL → Windows)

[Service]
Type=simple
WorkingDirectory={{project_root}}
ExecStart={{venv_python}} -m tools.sync --watch
Restart=on-failure
RestartSec=10
Environment=PYTHONPATH={{project_root}}

[Install]
WantedBy=default.target
```

- [ ] **Step 3: Create wiki-watcher.service.template**

Create `services/wiki-watcher.service.template`:

```ini
[Unit]
Description=Research Wiki Watcher (change detection + post-chain)

[Service]
Type=simple
WorkingDirectory={{project_root}}
ExecStart={{venv_python}} -m tools.watcher --watch
Restart=on-failure
RestartSec=10
Environment=PYTHONPATH={{project_root}}

[Install]
WantedBy=default.target
```

- [ ] **Step 4: Commit**

```bash
git add services/
git commit -m "feat: service unit templates for wiki-sync and wiki-watcher"
```

---

### Task 2: Add list_services() and install_service() to setup.py

**Files:**
- Modify: `tools/setup.py`

- [ ] **Step 1: Add list_services() function**

Add after the `configure_obsidian()` function (after line 231), before the CLI section:

```python
# ---------------------------------------------------------------------------
# Service deployment (systemd)
# ---------------------------------------------------------------------------

def list_services(project_root: Path):
    """List available service templates and their install status."""
    template_dir = project_root / "services"
    if not template_dir.exists():
        log_error("No service templates found in config/services/")
        return

    systemd_dir = Path.home() / ".config" / "systemd" / "user"

    log_info("Available services:")
    for template in sorted(template_dir.glob("*.service.template")):
        name = template.name.replace(".service.template", "")
        unit_path = systemd_dir / f"{name}.service"
        installed = unit_path.exists()

        # Check running status if installed
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


def install_service(service_name: str, project_root: Path) -> bool:
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

    # Fill placeholders
    content = template_path.read_text(encoding="utf-8")
    content = content.replace("{{project_root}}", str(project_root))
    content = content.replace("{{venv_python}}", str(venv_python(project_root)))

    # Write to systemd user dir
    systemd_dir = Path.home() / ".config" / "systemd" / "user"
    systemd_dir.mkdir(parents=True, exist_ok=True)
    unit_path = systemd_dir / f"{service_name}.service"
    unit_path.write_text(content, encoding="utf-8")
    log_info(f"Unit file written: {unit_path}")

    # Reload, enable, start
    subprocess.run(["systemctl", "--user", "daemon-reload"], check=True)
    subprocess.run(["systemctl", "--user", "enable", service_name], check=True)
    subprocess.run(["systemctl", "--user", "start", service_name], check=True)

    log_info(f"Service '{service_name}' installed and started")
    log_info(f"  Status:  systemctl --user status {service_name}")
    log_info(f"  Logs:    journalctl --user -u {service_name} -f")
    log_info(f"  Stop:    systemctl --user stop {service_name}")
    log_info(f"  Disable: systemctl --user disable {service_name}")
    return True
```

- [ ] **Step 2: Verify functions are importable**

Run: `python3 -c "from tools.setup import list_services, install_service; print('OK')"`

Expected: `OK`

- [ ] **Step 3: Commit**

```bash
git add tools/setup.py
git commit -m "feat: list_services() and install_service() in setup.py"
```

---

### Task 3: Add --services CLI Subcommand

**Files:**
- Modify: `tools/setup.py`

- [ ] **Step 1: Update argparse and main()**

Replace the CLI section of `tools/setup.py` (the `main()` function starting at line 238) with:

```python
def main():
    parser = argparse.ArgumentParser(description="Cross-platform setup for the research wiki")
    parser.add_argument("--deps", action="store_true", help="Install dependencies only")
    parser.add_argument("--check", action="store_true", help="Check environment only")
    parser.add_argument("--obsidian-config", action="store_true", help="Configure Obsidian vault")
    parser.add_argument("--services", nargs="?", const="__list__", default=None,
                        metavar="NAME", help="Deploy a systemd service (or list available)")
    args = parser.parse_args()

    root = get_project_root()

    if args.check:
        print_check(root)
    elif args.deps:
        install_deps(root)
    elif args.obsidian_config:
        configure_obsidian(root)
    elif args.services is not None:
        if args.services == "__list__":
            list_services(root)
        else:
            success = install_service(args.services, root)
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
```

- [ ] **Step 2: Update module docstring**

Replace lines 1-11 of `tools/setup.py`:

```python
"""Cross-platform setup for the DevOps Solutions Research Wiki.

Replaces bash scripts for environments where bash isn't available (Windows).
Works on Linux, macOS, and Windows.

Usage:
    python3 -m tools.setup                         # Full setup
    python3 -m tools.setup --deps                  # Install dependencies only
    python3 -m tools.setup --check                 # Check environment only
    python3 -m tools.setup --obsidian-config       # Configure Obsidian vault
    python3 -m tools.setup --services              # List available services
    python3 -m tools.setup --services wiki-sync    # Deploy sync daemon
    python3 -m tools.setup --services wiki-watcher # Deploy watcher daemon
"""
```

- [ ] **Step 3: Test list mode**

Run: `python3 -m tools.setup --services 2>&1`

Expected: Lists wiki-sync and wiki-watcher with `[not installed]` status.

- [ ] **Step 4: Commit**

```bash
git add tools/setup.py
git commit -m "feat: setup.py --services CLI subcommand"
```

---

### Task 4: Update CLAUDE.md and Verify

**Files:**
- Modify: `CLAUDE.md`

- [ ] **Step 1: Update CLAUDE.md Setup section**

Find the Setup section in `CLAUDE.md` (the block with `python -m tools.setup` commands) and replace it with:

```markdown
## Setup

Cross-platform (Linux, macOS, Windows):

    python -m tools.setup              # Full setup (check + deps + obsidian config)
    python -m tools.setup --check      # Check environment
    python -m tools.setup --deps       # Install dependencies via uv + Python 3.11 venv
    python -m tools.setup --obsidian-config  # Configure Obsidian vault
    python -m tools.setup --services              # List available services
    python -m tools.setup --services wiki-sync    # Deploy sync daemon (WSL→Windows)
    python -m tools.setup --services wiki-watcher # Deploy watcher daemon (auto post-chain)

Requires uv (https://docs.astral.sh/uv/). All tools run via `.venv/bin/python -m tools.<name>`.
```

- [ ] **Step 2: Test full flow — list services**

Run: `python3 -m tools.setup --services 2>&1`

Expected output:
```
[INFO] Available services:
  wiki-sync               [not installed]
  wiki-watcher            [not installed]

[INFO] Deploy with: python -m tools.setup --services <name>
[INFO] Manage with: systemctl --user start|stop|status <name>
[INFO] View logs:   journalctl --user -u <name> -f
```

- [ ] **Step 3: Test install — deploy wiki-sync**

Run: `python3 -m tools.setup --services wiki-sync 2>&1`

Expected output:
```
[INFO] Unit file written: /home/jfortin/.config/systemd/user/wiki-sync.service
[INFO] Service 'wiki-sync' installed and started
[INFO]   Status:  systemctl --user status wiki-sync
[INFO]   Logs:    journalctl --user -u wiki-sync -f
```

Verify: `systemctl --user status wiki-sync 2>&1 | head -5`

Expected: Shows `active (running)`.

- [ ] **Step 4: Verify list shows installed status**

Run: `python3 -m tools.setup --services 2>&1`

Expected: wiki-sync shows `[installed, running]`, wiki-watcher shows `[not installed]`.

- [ ] **Step 5: Commit**

```bash
git add CLAUDE.md
git commit -m "docs: setup --services commands in CLAUDE.md"
```

---

## Self-Review

**Spec coverage:**
- Service templates → Task 1
- install_service() with placeholder filling → Task 2
- list_services() with status checking → Task 2
- --services CLI subcommand → Task 3
- Platform gate (WSL/Linux only) → Task 2 (in install_service)
- CLAUDE.md update → Task 4
- Runtime management via systemctl → documented in list_services output (Task 2)

**Placeholder scan:** No TBDs, TODOs, or vague steps. All code complete.

**Type consistency:** `list_services(project_root)` and `install_service(service_name, project_root)` signatures match across Tasks 2 and 3.
