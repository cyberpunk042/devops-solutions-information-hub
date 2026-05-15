---
description: Manage Per-Project AI Assistant lifecycle (install · up · down · status · cron · surfaces · logs)
allowed-tools: Bash
---

# /assistant — Per-Project AI Assistant Management

Wraps `bin/assistant` (which wraps `tools/assistant.py`) for in-Claude-Code invocation. Same subcommands. Operator-facing.

## Usage

```
/assistant <subcommand> [args]
```

## Subcommands

| Subcommand | What it does |
|---|---|
| `profiles` | List known Profiles in `.assistant/` |
| `install <profile>` | One-shot end-to-end install (profile + vendor merge + systemd + cron + surfaces) |
| `up <profile>` | Start the assistant (live + ready to interact) |
| `down <profile>` | Stop the assistant |
| `restart <profile>` | Restart |
| `status [profile]` | Status across surfaces (per profile or all) |
| `logs <profile>` | Tail logs (via journalctl) |
| `config show <profile>` | Show Profile YAML + vendor configs |
| `config edit <profile> <vendor>` | Open vendor config in $EDITOR |
| `cron list <profile\|--global>` | List CRON jobs |
| `cron enable <profile> <job>` | Enable a cron job |
| `cron disable <profile> <job>` | Disable a cron job |
| `cron status <profile\|--global>` | Status of timers (last/next run) |
| `surfaces list` | Show available surfaces (multica/wiki/docs/claude-os/...) |
| `surfaces enable <profile> <surface>` | Wire a surface to a Profile |
| `uninstall <profile>` | Remove install (preserves Profile YAML) |

## Run

!`bin/assistant $ARGUMENTS`
