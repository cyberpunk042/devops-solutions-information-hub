---
description: Install a Per-Project AI Assistant Profile (one-shot end-to-end)
allowed-tools: Bash
---

# /assistant-install — One-shot install

Runs the full install chain for the named Profile:
1. Validate Profile YAML (`.assistant/<profile>.yaml`)
2. Validate OpenClaw vendor config (`.assistant/<profile>.openclaw.json5`)
3. Merge agent entry into `~/.openclaw/openclaw.json` agents.list[]
4. Register per-profile CRON jobs (`.assistant/<profile>.cron.yaml`)
5. Install systemd user unit (reboot-persistent)
6. Wire detected surfaces (multica/wiki/docs/claude-os/...)

After this completes:
- `systemctl --user enable assistant-<profile>` → reboot-persistent
- `/assistant up <profile>` → start the assistant

## Usage

```
/assistant-install <profile-name>
```

## Run

!`bin/assistant install $ARGUMENTS`
