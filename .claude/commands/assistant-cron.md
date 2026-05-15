---
description: Manage CRON jobs for Per-Project AI Assistants (per-profile or global)
allowed-tools: Bash
---

# /assistant-cron — Manage scheduled tasks

Per operator 2026-05-09: "list of CRON jobs that can be enabled or disabled and configured by AI assistant profile to enable other per-profile specific or even other global CRON jobs".

## Usage

```
/assistant-cron list <profile>           # list per-profile jobs
/assistant-cron list --global            # list global cross-profile jobs
/assistant-cron enable <profile> <job>   # toggle ON
/assistant-cron disable <profile> <job>  # toggle OFF
/assistant-cron status <profile>         # last/next fire times
/assistant-cron install <profile>        # install systemd timers
```

## Example jobs (continuous-research Profile)

- `frontier-delta-check` — hourly novelty scan
- `morning-scan` — daily 08:00 overnight delta synthesis
- `evening-report` — daily 20:00 cumulative summary
- `start-of-week-deep-dive` — Mon 09:00 pattern extraction
- `end-of-week-summary` — Fri 17:00 weekly digest
- `monthly-budget-audit` — 1st of month value-output audit

## Run

!`bin/assistant cron $ARGUMENTS`
