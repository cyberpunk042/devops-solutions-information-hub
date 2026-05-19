---
description: Manage Per-Project AI Assistants — interactive view when blank, drill-down with params (pace, fire, enable/disable, schedule edit, history, sessions).
---

# /ai-assistants — AI Assistant management surface

Unified management entry for the Per-Project AI Assistants registered in OpenClaw + the global systemd timers. Operator-facing surface for: see the pace · fire a task NOW · enable/disable a recurring task · re-schedule a task · inspect last runs · view sessions · re-install.

## Invocation patterns

| Form | Behavior |
|---|---|
| `/ai-assistants` | Blank — runs `bin/assistant manage` (full pace + status + numbered action menu) |
| `/ai-assistants pace` | Just the schedule timeline (gateway cron + systemd timers + heartbeats) |
| `/ai-assistants status` | Per-profile state (profile YAML / vendor config / agent registered / cron count) |
| `/ai-assistants activity` | What the assistants ACTUALLY did — files authored, run history with auditor verdicts, inboxes, pending operator actions |
| `/ai-assistants raw list` | Lifecycle inventory of `raw/` — every file with its retention status (ephemeral/permanent/conditional/pinned/forbidden) + synthesis-presence |
| `/ai-assistants raw pin <path> "<reason>"` | Protect a raw from purge by adding `lifecycle: keep` frontmatter |
| `/ai-assistants raw unpin <path>` | Remove the pin |
| `/ai-assistants raw purge-dry-run` | Preview what would be purged (ephemeral + has-synthesis + not pinned) |
| `/ai-assistants raw purge-execute` | Actually delete the purge-eligible raws (operator-triggered; the agent does this autonomously per cron tick) |
| `/ai-assistants promotions list` | Show entries from `wiki/backlog/operator-decision-queue.md` (filter by `--kind`) |
| `/ai-assistants promotions show <N>` | Full content of entry N |
| `/ai-assistants fire <profile> <job>` | Fire a cron job NOW (wakes the agent immediately) |
| `/ai-assistants enable <profile> <job>` | Enable a cron job (yaml + gateway) |
| `/ai-assistants disable <profile> <job>` | Disable a cron job (yaml + gateway) |
| `/ai-assistants edit <profile> <job> "<new-schedule>"` | Change a cron's schedule (yaml + gateway re-register) |
| `/ai-assistants history <profile> <job>` | Show last N runs of a cron job |
| `/ai-assistants reinstall <profile>` | Re-materialize workspace markdown + re-register cron + re-wake |

## What runs underneath

This slash command just shells out to `bin/assistant` with the appropriate args:

```bash
$ARGUMENTS="$ARGUMENTS"

# Map subcommand → bin/assistant invocation
case "$1" in
  "")
    bin/assistant manage
    ;;
  pace)
    bin/assistant pace
    ;;
  status)
    bin/assistant status "${2:-}"
    ;;
  fire)
    bin/assistant manage --action fire --profile "$2" --job "$3"
    ;;
  enable|disable)
    bin/assistant manage --action "$1" --profile "$2" --job "$3"
    ;;
  edit)
    bin/assistant manage --action edit --profile "$2" --job "$3" --schedule "$4"
    ;;
  history)
    bin/assistant manage --action history --profile "$2" --job "$3"
    ;;
  reinstall)
    bin/assistant install "$2"
    ;;
  *)
    echo "Unknown subcommand: $1"
    echo "Try: /ai-assistants (blank), /ai-assistants pace, /ai-assistants fire <profile> <job>, etc."
    ;;
esac
```

## The interactive menu (when run blank)

`bin/assistant` with no subcommand opens a progressive view:

1. **Full pace timeline** — every cron job + every systemd timer + every heartbeat, with next-fire and last-fire timestamps
2. **Installed profiles** — listed with their focus
3. **Numbered action menu**:
   - `1` — full status report
   - `2` — fire a cron job NOW
   - `3` — enable/disable a cron
   - `4` — change a cron's schedule
   - `5` — show last runs of a cron
   - `6` — open sessions list for an assistant
   - `7` — show workspace modes
   - `8` — list surface integrations
   - `9` — display the agent's IDENTITY.md / AGENTS.md / TOOLS.md (what the assistant IS)
   - `0` — reinstall a profile

Pick a number, drill into the operation, get an outcome.

## Examples

```
# Just look at what's running
/ai-assistants pace

# Fire the hourly delta-check now (don't wait an hour)
/ai-assistants fire continuous-research frontier-delta-check

# Stop the monthly budget audit (don't need it yet)
/ai-assistants disable continuous-research monthly-budget-audit

# Change the morning scan from 08:00 to 07:00
/ai-assistants edit continuous-research morning-scan "*-*-* 07:00:00"

# See last 10 runs of evening-report
/ai-assistants history continuous-research evening-report

# Full interactive flow
/ai-assistants
```

## Related

- `wiki/spine/standards/per-project-assistant-profile-standards.md` — Profile authoring standards
- `wiki/domains/cross-domain/profile-continuous-research-...md` — Continuous Research Profile (concept page)
- `.assistant/README.md` — full lifecycle docs (install · up · down · cron · surfaces · uninstall)
- `.assistant/<profile>.yaml` — abstract Profile YAML (source of truth)
- `.assistant/<profile>.cron.yaml` — per-profile cron jobs
- `.assistant/_global/cron.yaml` — global gateway cron / systemd timers
