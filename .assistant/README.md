# `.assistant/` — Per-Project AI Assistant Lifecycle

> Operator-facing guide. Per operator 2026-05-09 turn 7 (sacrosanct, verbatim): *"you are not done, till I cannot just call a script and be ready to interact with my live running AI assistant"* + *"I have to do nothing manually and everything must be explained to me at each stage properly"*.

## TL;DR — Go-live in one command

```bash
bin/assistant install continuous-research    # one-shot end-to-end install
bin/assistant up continuous-research          # start the assistant; LIVE
```

Then interact via whichever surfaces you have wired (OpenClaw native channels · Multica board · Claude Code · Claude OS · etc.). Reboot-persistent via `systemctl --user enable assistant-continuous-research`.

---

## What lives here

```
.assistant/
├── README.md                                    ← this file (operator guide)
│
├── <profile-name>.yaml                          ← Per-Project Assistant Profile
│                                                  (abstract · tool-agnostic ·
│                                                   ONE focused assistant job)
│
├── <profile-name>.openclaw.json5                ← OpenClaw vendor config
├── <profile-name>.openclaw.json                 ← stripped-to-JSON deploy form
├── <profile-name>.<vendor>.<ext>                ← other vendor configs as needed
│                                                  (multica yaml · hermes toml · etc.)
│
├── <profile-name>.cron.yaml                     ← per-profile CRON jobs
│
├── _global/
│   ├── cron.yaml                                ← cross-profile CRON jobs
│   └── surfaces.yaml                            ← surface integrations
│
├── _templates/
│   ├── assistant.service.template               ← systemd user unit
│   ├── assistant-cron.service.template          ← per-cron-job oneshot
│   └── assistant-cron.timer.template            ← per-cron-job timer
│
└── _state/                                      ← runtime state (gitignored)
```

---

## The two-file pair per assistant Profile

Every assistant Profile is **two files** (minimum):

1. **`<name>.yaml`** — the **abstract Profile**. Tool-agnostic. Defines what the assistant IS for this project: identity · knowledge scope · action surface · model routing preferences · prompt templates · success criteria. Same Profile is consumed by 0, 1, or MULTIPLE tools.
2. **`<name>.<vendor>.<ext>`** — the **vendor configuration file** that consumes the Profile. One per consuming tool (OpenClaw · Multica · Hermes · etc.). Concrete; uses the vendor's native schema.

Operator-doctrinal 2026-05-09 (sacrosanct): *"A PROFILE IS WAY MORE THAN JUST SETTING FOR ONE TOOL"* — the Profile is upstream of all vendor configs.

---

## Workspace modes (`workspace_mode:` in the Profile YAML)

Every Profile declares a `workspace_mode:` that determines where the running assistant operates relative to the project tree. Set in `.assistant/<name>.yaml`; `assistant install` materializes the workspace + overrides the vendor config's `workspace:` path to match.

| Mode | Where the assistant works | Operator sees writes live? | Git isolation | Best for |
|---|---|---|---|---|
| **`shared`** | The project folder itself (`~/devops-solutions-information-hub`) — same files, same `.git`, same branch as operator | YES — files appear as the assistant writes them | NONE — assistant commits to the operator's current branch | Live observable work — synthesis, research surfacing, ingestion — where operator wants to see + correct in real time |
| **`worktree`** | `git worktree add ~/.openclaw/agents/<name>/worktree` on its own branch `assistant/<name>` (shared `.git`, separate working tree) | NO — writes land in the worktree, invisible until merged back | YES — assistant branch separate from operator's | Longer autonomous runs without interleaving operator's work; `git merge assistant/<name>` when ready |
| **`own-workspace`** | A fully separate clone at `~/.openclaw/agents/<name>/workspace` | NO — separate repo entirely | FULL — sync via `git push` / `git pull` | Remote / sandboxed / untrusted contexts where full isolation is required |

**Listing modes**: `bin/assistant modes` prints all 3 with tradeoffs.

**Switching mode for an existing Profile**: edit `workspace_mode:` in `.assistant/<name>.yaml`, then re-run `bin/assistant install <name>` (idempotent; re-materializes workspace + overrides agent entry). For non-shared → other transitions, optionally `bin/assistant uninstall <name> --remove-workspace` first to clean up the prior worktree/clone.

**Current Profiles** (this project):

| Profile | `workspace_mode` | Workspace path |
|---|---|---|
| `continuous-research` | `shared` | `~/devops-solutions-information-hub/` |
| `pipeline-synthesis` | `shared` | `~/devops-solutions-information-hub/` |

---

## Complete lifecycle commands

All commands have THREE invocation paths (operator preference):

| What | Shell shim | Direct Python | Slash command (Claude Code) |
|---|---|---|---|
| Install | `bin/assistant install <name>` | `.venv/bin/python -m tools.assistant install <name>` | `/assistant-install <name>` |
| Up (start) | `bin/assistant up <name>` | `... up <name>` | `/assistant-up <name>` |
| Down (stop) | `bin/assistant down <name>` | `... down <name>` | `/assistant down <name>` |
| Restart | `bin/assistant restart <name>` | `... restart <name>` | `/assistant restart <name>` |
| Status | `bin/assistant status [name]` | `... status [name]` | `/assistant-status [name]` |
| Logs (tail) | `bin/assistant logs <name>` | `... logs <name>` | `/assistant logs <name>` |
| Config show | `bin/assistant config show <name>` | `... config show <name>` | `/assistant config show <name>` |
| Config edit | `bin/assistant config edit <name> <vendor>` | `... config edit <name> <vendor>` | `/assistant config edit <name> <vendor>` |
| Cron list (profile) | `bin/assistant cron list <name>` | `... cron list <name>` | `/assistant-cron list <name>` |
| Cron list (global) | `bin/assistant cron list --global` | `... cron list --global` | `/assistant-cron list --global` |
| Cron enable | `bin/assistant cron enable <name> <job>` | `... cron enable <name> <job>` | `/assistant-cron enable <name> <job>` |
| Cron disable | `bin/assistant cron disable <name> <job>` | `... cron disable <name> <job>` | `/assistant-cron disable <name> <job>` |
| Surfaces list | `bin/assistant surfaces list` | `... surfaces list` | `/assistant-surfaces list` |
| Surfaces enable | `bin/assistant surfaces enable <name> <surface>` | `... surfaces enable <name> <surface>` | `/assistant-surfaces enable <name> <surface>` |
| Uninstall | `bin/assistant uninstall <name>` | `... uninstall <name>` | `/assistant uninstall <name>` |
| Profiles list | `bin/assistant profiles` | `... profiles` | `/assistant profiles` |

**OpenCode users**: same shell shim + direct Python paths work. OpenCode equivalents of the slash commands can be added under `.opencode/commands/` (planned — same content, OpenCode's directive syntax).

---

## What `install` actually does (6 stages, explained at each)

`bin/assistant install <name>` runs 6 stages. Each stage prints what it's doing.

| Stage | What | Mutates | Skips if... |
|---|---|---|---|
| **[1/6]** | Validate Profile YAML + resolve `workspace_mode` + materialize workspace (`git worktree add` for `worktree` / `git clone` for `own-workspace`; no-op for `shared`) | `~/.openclaw/agents/<name>/worktree` or `/workspace` (only if non-shared) | profile file missing → error; workspace already exists → idempotent skip |
| **[2/6]** | Validate vendor config (OpenClaw default) | (read-only) | no vendor file → warn + `--no-openclaw` proceeds |
| **[3/6]** | Merge agent entry into `~/.openclaw/openclaw.json` agents.list[] — **agent's `workspace` field is overridden with the workspace_mode-resolved path**, and `_workspace_mode` is stamped on the entry for status reporting | `~/.openclaw/openclaw.json` (writes JSON) | `--dry-run` to preview |
| **[4/6]** | Register per-profile CRON jobs | (reads `.assistant/<name>.cron.yaml`) | no cron file → skipped |
| **[5/6]** | Install systemd user unit (reboot persistence) | `~/.config/systemd/user/assistant-<name>.service` | systemctl absent → skipped |
| **[6/6]** | Wire detected surfaces | (reads `.assistant/_global/surfaces.yaml`) | no surfaces file → skipped |

Idempotent. Re-running install is safe — it updates the agent entry in place.

After install: `bin/assistant up <name>` to start. Or `systemctl --user enable assistant-<name>` for reboot-persistent + `systemctl --user start assistant-<name>` to start now.

---

## CRON jobs (per-profile and global)

Per operator 2026-05-09: per-profile CRON jobs (specific) AND global CRON jobs (cross-project). Each is configurable, enable/disable-able, status-able.

### Per-profile (example: continuous-research)

Defined in `.assistant/continuous-research.cron.yaml`. Current job catalog:

| Job | Schedule | What it does |
|---|---|---|
| `frontier-delta-check` | hourly | Lightweight novelty scan across fast-moving frontier surfaces |
| `morning-scan` | daily 08:00 | Overnight delta synthesis + operator-decision-queue triage |
| `evening-report` | daily 20:00 | Cumulative day's frontier findings + urgent operator-review items |
| `start-of-week-deep-dive` | Mon 09:00 | Pattern extraction from last week's daily findings |
| `end-of-week-summary` | Fri 17:00 | Research output metrics + anti-signal surfacing |
| `monthly-budget-audit` | 1st of month 12:00 | Cost/value audit per Profile.success_criteria |

All start `enabled: false`. Operator opts in:

```bash
bin/assistant cron enable continuous-research morning-scan
bin/assistant cron enable continuous-research evening-report
```

Status:

```bash
bin/assistant cron list continuous-research
# ● morning-scan  — *-*-* 08:00:00
#   Daily morning brief — overnight delta synthesis + operator-decision-queue triage
# ○ evening-report — *-*-* 20:00:00
#   Daily evening summary ...
```

### Global cross-profile

Defined in `.assistant/_global/cron.yaml`. Current catalog:

| Job | Schedule | What it does |
|---|---|---|
| `hourly-pipeline-post` | hourly | Validate wiki structure, manifest, schema |
| `daily-gateway-health` | daily 09:30 | Composite methodology+quality score |
| `weekly-maturity-flow` | Sun 18:00 | Maturity-tier velocity report |
| `monday-backlog-surface` | Mon 07:00 | Epics/modules/tasks state into wiki/log/ |
| `weekly-provider-pricing-health` | Wed 11:00 | Detect provider rate-card changes |
| `morning-git-status` | daily 07:30 | Uncommitted state snapshot |

```bash
bin/assistant cron list --global
bin/assistant cron enable --global hourly-pipeline-post  # planned syntax
```

### Implementation

Each enabled CRON job becomes a **systemd timer** (`assistant-cron-<profile>-<job>.timer`) + **oneshot service** (`assistant-cron-<profile>-<job>.service`). Templates at `.assistant/_templates/`. Run `bin/assistant cron install <name>` to materialize them into `~/.config/systemd/user/`.

Persistent across reboots: `Persistent=true` in the timer ensures missed runs (e.g., laptop closed) fire on next boot.

---

## Surfaces (multi-tool interaction)

Per operator 2026-05-09: *"I can interact with, with or without multica or the wiki LLM folder and/or docs folder and/or Claude OS and/or any other relevant surface that we usually use to interact with OpenClaw"*.

The assistant is the same Profile; the surfaces just change WHERE you interact with it. None are required (except the runtime — OpenClaw for OpenClaw-spawned assistants).

```bash
bin/assistant surfaces list
#  ● openclaw-native       (detected)
#  ● multica               (detected)  ← operator self-hosted at /home/jfortin/.multica/server
#  ● wiki-llm-folder       (detected)
#  ● docs-folder           (detected)
#  ○ claude-os             (absent — Redis not installed)
#  ● claude-code           (detected)
#  ● opencode              (detected)
#  ○ hermes                (absent — Nous Research hermes CLI not installed)
#  ● huggingface           (always-available via MCP)
#  ● github                (detected — gh CLI)
#  ○ public-obsidian       (downstream of wiki/ sync)
```

Wire a surface to a profile:

```bash
bin/assistant surfaces enable continuous-research multica
bin/assistant surfaces enable continuous-research wiki-llm-folder
```

Result: when the assistant runs, it can be accessed via the wired surfaces. The Profile's `knowledge_scope` declares which paths/MCPs are accessible (always-on); surfaces add WHERE the operator can interact (chat / board / terminal / etc.).

---

## Reboot persistence

After `install`, two paths to reboot-persistent:

### Linux / WSL2 (systemd)

```bash
systemctl --user enable assistant-continuous-research      # persist across reboots
systemctl --user start  assistant-continuous-research      # start now
systemctl --user status assistant-continuous-research      # check
journalctl --user -u assistant-continuous-research -f      # tail logs
```

**WSL2 note**: requires `/etc/wsl.conf` to have `[boot]\nsystemd=true` for `systemctl --user` to work. If not enabled, fallback: Windows Task Scheduler with `wsl --exec` action.

### Windows side (alternative)

If running OpenClaw daemon from Windows: use Task Scheduler with action `wsl --exec bin/assistant up continuous-research`. Trigger: at logon or at startup. Reboot-persistent.

---

## Multiple assistants per project (the plural per-project doctrine)

Operator 2026-05-09 turn 6 (sacrosanct): *"I CAN RUN MULTIPLE OPENCLAW ASSISTANT AT THE SAME TIME FOR ONE PROJECT... I COULD HAVE TWO 24/7 for just the second-brain"*.

Each Profile is ONE focused assistant job. Multiple Profiles per project. Multiple can run concurrently:

```bash
bin/assistant install continuous-research        # Profile #1: research-focused
bin/assistant install pipeline-synthesis         # Profile #2: synthesis-focused (when authored)
bin/assistant up continuous-research              # start #1
bin/assistant up pipeline-synthesis               # start #2
# Both run concurrently; both are agents in ~/.openclaw/openclaw.json agents.list[]
```

The OpenClaw daemon is shared (one process serving all agents). Each agent runs independently with its own Profile.

---

## Adding a new vendor (Multica · Hermes · etc.)

To consume a Profile via Multica (already operator-adopted):
1. Author `.assistant/<name>.multica.yaml` mapping Profile sections → Multica agent fields
2. Add Multica to the surface wiring: `bin/assistant surfaces enable <name> multica`
3. Use Multica's setup: `multica setup` and the agent appears under Multica Settings (per `https://github.com/multica-ai/multica` README)

To consume via Hermes Agent (Nous Research):
1. Author `.assistant/<name>.hermes.toml` (or similar — Hermes-specific shape)
2. Install Hermes Agent CLI: see `github.com/nousresearch/hermes-agent`
3. Configure Hermes to load this Profile via its skill+memory subsystem

The Profile YAML never changes when you add a vendor. Only the vendor file is new.

---

## Troubleshooting

```bash
bin/assistant status                           # high-level health
bin/assistant logs <name>                      # journal logs (last 200 lines, then tail)
openclaw doctor                                # validate ~/.openclaw/openclaw.json
systemctl --user status assistant-<name>       # systemd state
systemctl --user list-timers                   # CRON timer state
```

Common issues:

| Symptom | Likely cause | Fix |
|---|---|---|
| `Installed in ~/.openclaw/openclaw.json: NO` after install | install failed at stage [3/6] | Re-run install; check JSON5 validity (`npx json5 <file>`) |
| systemd unit fails to start | OpenClaw not in PATH for systemd | Add `Environment=PATH=...` to the unit |
| CRON jobs not firing | timers not installed | `bin/assistant cron install <name>` |
| Surfaces all "absent" | tools not on PATH | Install the surface tools or use without them |

---

## Documentation cross-references

- Profile concept (knowledge): [wiki/spine/models/agent-config/model-per-project-assistant-profile.md](../wiki/spine/models/agent-config/model-per-project-assistant-profile.md)
- Profile standards: [wiki/spine/standards/per-project-assistant-profile-standards.md](../wiki/spine/standards/per-project-assistant-profile-standards.md)
- Profile pattern: [wiki/patterns/01_drafts/per-project-assistant-profile-pattern-tailored-config-to-spawn-ecosystem-runtimes.md](../wiki/patterns/01_drafts/per-project-assistant-profile-pattern-tailored-config-to-spawn-ecosystem-runtimes.md)
- this project's current Profiles (knowledge layer): `wiki/domains/cross-domain/profile-*.md`
- Knowledge integration topology: [wiki/domains/cross-domain/profile-integration-into-the-knowledge-cross-reference-topology-with-existing-wiki-layers.md](../wiki/domains/cross-domain/profile-integration-into-the-knowledge-cross-reference-topology-with-existing-wiki-layers.md)
- OpenClaw configuration reference: [docs.openclaw.ai/gateway/config-agents](https://docs.openclaw.ai/gateway/config-agents)
- Multica self-hosting: `/home/jfortin/.multica/server/SELF_HOSTING.md`
