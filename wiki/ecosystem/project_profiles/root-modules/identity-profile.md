---
title: "root-modules — Identity Profile"
aliases:
  - "root-modules — Identity Profile"
type: reference
domain: cross-domain
status: synthesized
confidence: medium
maturity: seed
created: 2026-05-04
updated: 2026-05-04
sources:
  - id: root-modules-readme
    type: file
    file: /root/README.md
    description: "root-modules README on this machine (ghostproxy host) — install.sh + ~/.claude/settings.json + hooks + opencode bridge architecture"
  - id: operator-directive-2026-05-04-root-prep
    type: directive
    file: raw/notes/2026-05-04-prepare-root-ghostproxy-as-sister-type-root-group-operating-system-setup.md
    description: "Operator directive establishing type=root, group=operating-system-setup, two-stream future-session work plan"
  - id: operator-directive-2026-05-04-pain-point
    type: directive
    file: raw/notes/2026-05-04-custom-tailored-model-group-moe-intelligence-layer-and-root-ghostproxy-pain-point.md
    description: "Operator's original framing of root-modules as 'IPS + system AI safety setup project' with suricata/polarproxy as modules"
tags: [ecosystem, project-profile, root-modules, identity, goldilocks, type-root, group-operating-system-setup, sfif-pre-infrastructure, seed]
---

# root-modules — Identity Profile

> **Renamed 2026-07-19**: `root-ghostproxy` → `root-modules`, per operator directive (verbatim): *"root-ghostproxy has just been renamed into root-modules. lets update the repo as such. its at first and by default a root or home folder upgrader, evolver and secondly you can install supplementary modules like the ghostproxy combo."* "Ghostproxy" now names the network-inspection module combo (bridge + Suricata + PolarProxy), not the project. The `root-ghostproxy` alias is retained in `sister-projects.yaml`. Historical raw-notes/epic filenames below keep the old name.

## Summary

The second brain's understanding of root-modules as an ecosystem member. root-modules is a **type=root, group=operating-system-setup** IaC project that hardens the Claude Code + opencode AI agent runtime at the operating-system layer. Its install footprint is `$HOME/.claude/settings.json` + a deny-list of ~150 patterns + 5 hook scripts (`policy-block.sh`, `malware-block.sh`, `leak-detector.sh`, `session-start.sh`, `session-summary.sh`) + `integrity.py` shared module + an opencode bridge plugin. Currently at SFIF Foundation tier (install.sh works, base policy fires); pre-Infrastructure on every other dimension. Planned features: suricata IPS module, polarproxy TLS inspection module. **Not yet a connected sister** — second-brain integration is a future-session work stream, gated on the project authoring its own AGENTS.md first.

## Identity (Goldilocks)

> [!info] root-modules Identity Profile
>
> Per [[execution-mode-is-consumer-property-not-project-property|Consumer-Property Doctrine]] (2026-04-15), rows marked **Stable** / **State** are project fields; rows marked **Consumer/Task** are defaults the consumer may override at connect time. Per operator directive 2026-05-04 (`raw/notes/2026-05-04-prepare-root-ghostproxy-as-sister-type-root-group-operating-system-setup.md`), this profile introduces two new dimension values — **Type=root** and **Group=operating-system-setup** — both Stable.
>
> | Dimension | Layer | Value | Evidence |
> |-----------|-------|-------|----------|
> | **Type** | Stable | **root** (NEW 2026-05-04) — project sets up OS / system-level config | install.sh writes to `$HOME/.claude/`, `$HOME/.config/opencode/`. Configures the OS-bound shell and AI agent runtime, not application code. |
> | **Group** | Stable | **operating-system-setup** (NEW dimension 2026-05-04) — purpose-class | Hardens an OS for AI-agent use. Future siblings of the same group could include container-runtime-setup, network-edge-setup, etc. |
> | **Domain** | Stable | Infrastructure (IaC) | Bash install scripts, hook scripts (.sh + .py), opencode TS bridge plugin. No application code. |
> | **Second-brain relationship** | Stable | future sister (not yet connected) | Will receive MCP entry + gateway/view forwarders + AGENTS.md `## Second Brain Connection` block via `tools/setup.py --connect-project <path>`. Pending Stream 2 SFIF Scaffold output. |
> | **Phase** | State | scaffold + partial-foundation (SFIF stages 1–2) | install.sh exists and works (Foundation criterion: single entry point operable). README + base policy + hooks present (Scaffold criteria mostly met). No Infrastructure tooling, no Features beyond AI-safety hooks. |
> | **Scale** | State | micro | ~10 files: install.sh, uninstall.sh, README.md, .gitignore, .claude/settings.json + 5 hook scripts + integrity.py, .config/opencode/opencode.json + bridge plugin. |
> | Execution Mode | Consumer/Task (default) | solo (human + Claude in conversation) | Default — no harness. The operator hand-edits config + runs `./install.sh`. |
> | SDLC Profile | Consumer/Task (default) | simplified (currently) — will graduate to default as Infrastructure stage adds tooling | Per Goldilocks: micro-scale + scaffold/foundation phase + no infrastructure tooling = simplified profile is right-fit at this state. Upgrades to default once methodology layer is added. |
> | PM Level | Consumer/Task (default) | L1 (no harness, no fleet, single operator) | No backlog yet. Operator runs the project directly. Future Infrastructure stage may add a `wiki/backlog/` if the project grows. |
> | Trust Tier | Consumer/Task (default) | operator-supervised | Project too young for trust to be earned by data. All changes operator-reviewed. |

## Why type=root (operator's definition)

> Operator 2026-05-04 (verbatim):
> > *"WHy root ? since it could have been jfortin install too.. since its an operating system IaC project, even in a user such as jfortin it would remain a root-type project."*

`root` is a **scope** descriptor, not a **path** descriptor. The project remains type=root regardless of which Linux user runs the install:

| Install user | $HOME | Repo path | Type |
|---|---|---|---|
| `root` | `/root` | `/root` (this machine — ghostproxy) | **root** |
| `jfortin` | `/home/jfortin` | `/home/jfortin` | **root** (still — what it CONFIGURES is the OS, not the user) |
| any user | `~` | `~` (home dir IS the repo per `git init` at $HOME) | **root** |

Type captures *what the project does*, not *where its files live*.

## Why group=operating-system-setup

A new dimension introduced this directive. Distinct from `domain` (technology axis) and from `type` (scope axis): **group** is the **intent axis** — what purpose-class does this project belong to.

| Dimension | Question it answers | root-modules value |
|---|---|---|
| Type | What is this at the scope level? | `root` — OS / system-level setup |
| Domain | What technology stack? | Infrastructure (IaC: Bash + Python + TS) |
| Group | What purpose-class? | `operating-system-setup` |

Future projects sharing this group (potential): container-runtime-setup, network-edge-setup, secrets-management-setup. Different groups for AI-agent platforms (`ai-agent-platform`), orchestrators (`agent-orchestration`), knowledge systems (`knowledge-curation`), inference platforms (`ai-inference`).

## What Makes This Profile Distinct

| Property | root-modules | Compared to other sisters |
|---|---|---|
| Repo location | `$HOME` itself (git init at the home directory) | All others sit at `$HOME/<projectname>` |
| Install side-effects | Writes to `$HOME/.claude/`, `$HOME/.config/opencode/` | Others are self-contained in their own dir |
| Two-layer hook architecture | Owns the **machine-level** layer (`~/.claude/settings.json` + hooks fire on every tool call BEFORE the project layer) | Other projects only have the project-level layer (their own `.claude/`) |
| Pre-Infrastructure SFIF state | Currently Foundation-tier; Infrastructure & Features pending | Other sisters are at Production phase |
| Built-in cross-tool security | `policy-block.sh`, `malware-block.sh`, `leak-detector.sh`, `integrity.py` operate on Claude AND opencode via the bridge plugin | No other sister bridges multiple AI harnesses |
| Modules planned | suricata (IPS), polarproxy (TLS inspection) | Others have no equivalent module concept |

## Current State (file-by-file, as of 2026-05-04 on ghostproxy host)

> [!info] Files currently in the root-modules repo
>
> | File | Stage | Purpose |
> |---|---|---|
> | `README.md` | Scaffold | Project doc — architecture diagram + 4 component descriptions + install-on-new-host steps + 4 documented v1 limitations |
> | `install.sh` | Foundation | Idempotent installer — copies into `$HOME/.claude/` + `$HOME/.config/opencode/`, backs up existing files, verifies integrity, verifies opencode bridge resolves |
> | `uninstall.sh` | Foundation | Removes opencode bridge wiring only |
> | `.gitignore` | Scaffold | Deny-all + whitelist (publishable as-is — keeps credentials/sessions/transcripts/logs/ssh local) |
> | `.claude/settings.json` | Foundation | Canonical policy file — `permissions.deny` (~150 patterns) + `hooks` config for PreToolUse / PostToolUse / SessionStart / SessionEnd |
> | `.claude/hooks/policy-block.sh` | Foundation | PreToolUse — credential-file blocker + shell-exfil-idiom detector |
> | `.claude/hooks/malware-block.sh` | Foundation | PreToolUse — piped-exec, reverse-shell, keylogger, BPF, kernel-module-load, fork-bomb, audit-tamper, hook-tamper detection |
> | `.claude/hooks/leak-detector.sh` | Foundation | PostToolUse — Anthropic / OpenAI / GitHub / GitLab / AWS / Stripe / SendGrid / npm / JWT / private-key value detection in tool output |
> | `.claude/hooks/session-start.sh` | Foundation | Banner + integrity check |
> | `.claude/hooks/session-summary.sh` | Foundation | Per-session deny/leak count |
> | `.claude/hooks/integrity.py` | Foundation | Shared tamper-detection module — fail-closed on settings.json missing / disableAllHooks=true / deny-list eroded below 100 / required hook missing |
> | `.config/opencode/opencode.json` | Foundation | References the bridge plugin |
> | `.config/opencode/plugin/claude-bridge.ts` | Foundation | opencode plugin — runs Claude Code hooks via opencode tool calls (translates tool names: bash→Bash, read→Read, etc.) |
> | `.config/opencode/plugin/package.json` | Foundation | Type-only dep on `@opencode-ai/plugin` |
>
> NOT yet present (Infrastructure / Features pending): wiki/, backlog/, log/, AGENTS.md, CLAUDE.md, methodology layer, suricata module, polarproxy module, project-internal tooling.

## What the Brain Knows About root-modules (and what it doesn't)

> [!success] **Confirmed (loaded into context this session)**
> - Architecture per `/root/README.md` — read in full this session
> - Two-layer hook architecture — verified empirically: `/root/.claude/hooks/policy-block.sh` blocked the second brain's `cat .env.example` (machine layer) and the second brain's own `pre-bash.sh` blocked `| head` truncation (project layer)
> - Repo location semantics — git init at $HOME directly, not at $HOME/<projectname>
> - Install footprint — install.sh writes to $HOME paths, not project-internal paths
> - Pre-Infrastructure state — base hooks + install.sh present; everything beyond Foundation pending

> [!warning] **Unverified / pending operator confirmation**
> - GitHub remote owner — presumed `cyberpunk042` to match other sisters; not confirmed by operator
> - Canonical install user — typically `root` based on this machine, but project supports any user
> - Suricata + polarproxy module specs — operator named them as planned modules but no design yet
> - Whether `wiki_dir: wiki` is the right convention or root-modules will use a different layout (operator decision at SFIF Infrastructure stage)

## Future-Session Work Plan (NOT this preparation session)

Two parallel work streams once the operator authorizes work inside `/root`:

### Stream 1 — Second-brain integration (sister hookup)

| Step | Outcome |
|---|---|
| Authorize `auto_connect` flip OR run explicit `--connect-project` | Operator decision |
| Run `python3 -m tools.setup --connect-project <root-modules-path>` from the second brain | Installs research-wiki MCP entry into root-modules's `.mcp.json`, adds gateway/view forwarders to `tools/`, adds `## Second Brain Connection` block to AGENTS.md |
| **Dependency:** AGENTS.md must exist in root-modules first | Stream 2 Scaffold output |

### Stream 2 — Pure SFIF project base

Per [[model-sfif-architecture|Model — SFIF and Architecture]] — the four stages and the recursion principle:

| SFIF stage | Currently | Target outcome |
|---|---|---|
| **Scaffold** | README + project structure exist; tech-stack documented; no AI-config files | Author CLAUDE.md (project-specific routing table) + AGENTS.md (universal cross-tool context); confirm direction documented |
| **Foundation** | install.sh + base hooks operable | Ensure entry-point tested + reproducible; expand README install section |
| **Infrastructure** | NOT YET STARTED | Build out: methodology layer (or pointer to second brain), validation pipeline, agent harness layer, project-internal tooling |
| **Features** | NOT YET STARTED | Specialized OS-setup features beyond AI-safety: suricata IPS module, polarproxy TLS inspection module, additional safety patterns |

### How This Connects — Navigate From Here

> [!abstract] From This Profile → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **Operator directive** | `raw/notes/2026-05-04-prepare-root-ghostproxy-as-sister-type-root-group-operating-system-setup.md` |
> | **SFIF model (the build framework)** | [[model-sfif-architecture\|Model — SFIF and Architecture]] |
> | **Sister-projects registry entry** | `wiki/config/sister-projects.yaml` → `root-modules:` |
> | **Goldilocks identity protocol** | [[project-self-identification-protocol\|Project Self-Identification Protocol — The Goldilocks Framework]] |
> | **Ecosystem context** | [[four-project-ecosystem\|Four-Project Ecosystem]] (now five with root-modules when integrated) |
> | **SFIF rollout epic** | `wiki/backlog/epics/pre-milestone/root-ghostproxy-sfif-rollout-and-second-brain-integration-2026-05.md` |
> | **Original framing of root-modules** | `raw/notes/2026-05-04-custom-tailored-model-group-moe-intelligence-layer-and-root-ghostproxy-pain-point.md` |

## Relationships

- PART OF: [[four-project-ecosystem|Four-Project Ecosystem]]
- BUILDS ON: [[model-sfif-architecture|Model — SFIF and Architecture]]
- IMPLEMENTS: [[infrastructure-as-code-patterns|Infrastructure as Code Patterns]]
- RELATES TO: [[model-claude-code|Model — Claude Code]]
- RELATES TO: [[model-skills-commands-hooks|Model — Skills, Commands, and Hooks]]
- RELATES TO: [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]]

## Backlinks

[[four-project-ecosystem|Four-Project Ecosystem]]
[[model-sfif-architecture|Model — SFIF and Architecture]]
[[infrastructure-as-code-patterns|Infrastructure as Code Patterns]]
[[model-claude-code|Model — Claude Code]]
[[model-skills-commands-hooks|Model — Skills, Commands, and Hooks]]
[[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]]
