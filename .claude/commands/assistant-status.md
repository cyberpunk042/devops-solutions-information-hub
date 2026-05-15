---
description: Status of Per-Project AI Assistants across surfaces
allowed-tools: Bash
---

# /assistant-status — Status across surfaces

Reports for each Profile:
- Profile YAML present?
- Vendor configs present?
- Installed in `~/.openclaw/openclaw.json`?
- systemd unit installed / active / reboot-enabled?
- CRON jobs defined / enabled?

## Usage

```
/assistant-status [profile-name]
```

If no profile name → reports on all Profiles.

## Run

!`bin/assistant status $ARGUMENTS`
