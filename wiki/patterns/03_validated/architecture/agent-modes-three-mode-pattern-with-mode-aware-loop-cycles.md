---
title: "Pattern — Agent Modes (Three-Mode: PM / Architect / Dual) with Mode-Aware /loop Cycles for Autopilot"
type: pattern
domain: cross-domain
status: synthesized
confidence: medium
maturity: mature
layer: 2
created: 2026-05-05
updated: 2026-05-05
sources:
  - id: root-ghostproxy-modes-implementation
    type: project
    project: root-ghostproxy
    path: /root/.claude/modes/
    description: "First implementation of the three-mode pattern in the ecosystem"
  - id: operator-directive-modes-architecture
    type: directive
    file: raw/notes/2026-05-05-claudeignore-purpose-and-modes-architecture-directive.md
  - id: skills-commands-hooks-model
    type: wiki
    file: wiki/spine/models/agent-config/model-skills-commands-hooks.md
tags: [pattern, agent-modes, pm-scrum-master, devops-architect, dual-expert, mode-aware-loop, autopilot, persona-overlay, claude-code, sister-project-applicable, layer-2]
---

# Pattern — Three-Mode Agent Architecture with Mode-Aware /loop Cycles

## Summary

A three-tier persona-overlay system for AI coding agents that distinguishes operator-supervised work into focused lenses: **PM Scrum Master** (backlog + decisions + status), **DevOps Architect** (design + implementation + hooks), and **Dual Expert** (both, lens-switching per question). Each mode pre-defines a `/cycle` sequence; combined with Claude Code's `/loop <interval>` skill, modes enable autonomous recurring autopilot in the chosen lens.

The pattern composes mechanism-determinism layers known from `model-skills-commands-hooks`: **state file** (durable mode persistence) → **slash commands** (100% deterministic mode switch) → **brain pieces** (per-mode persona + scope + cycle definitions) → **hook directives** (~85% surface the feature without auto-enabling).

## Pattern Description

A solo-operator + AI configuration historically conflates three distinct work types within the same agent context: PM coordination (backlog, decisions, blockers, status reports), engineering (architecture, implementation, hooks), and cross-cutting work (mixed). This conflation produces scope drift and lower output quality per role.

The three-mode pattern provides a **persona overlay** mechanism: the operator selects an active mode via slash command; the agent's behavior shifts (loaded brain pieces, cycle sequence, in/out-of-scope discipline) per the chosen mode. State persists in a file (`active-mode`); switching is 100% deterministic when the operator invokes the slash command; cycles fire per the mode's `/cycle` sequence definition.

**Five components**:
1. **State file** — `active-mode` single-line file holding the current mode name (or absent)
2. **Mode brain pieces** — `.claude/modes/<mode>.md` files defining persona + scope + cycle + when-to-switch-out per mode
3. **Mode switch commands** — `/mode-pm`, `/mode-architect`, `/mode-dual`, `/mode-clear`, `/mode-status` (100% deterministic)
4. **Cycle dispatch command** — `/cycle` reads state, loads mode brain piece, executes the mode's cycle sequence
5. **Surface mechanism** — SessionStart hook mentions mode feature when no mode active; never auto-enables (operator-choice rule)

When combined with Claude Code's `/loop <interval>` skill, the pattern produces **autonomous recurring autopilot** in the chosen lens — `/loop 30m /cycle` fires the active mode's cycle every 30 minutes.

## Instances

| Project | Status | Files | Notes |
|---|---|---|---|
| **root-ghostproxy** | First implementation, validated 2026-05-05 | `/root/.claude/modes/{pm-scrum-master,devops-architect,dual-expert}.md`, `/root/.claude/commands/{cycle,mode-pm,mode-architect,mode-dual,mode-clear,mode-status}.md`, `/root/.claude/active-mode`, SessionStart hook surface mention | Empirical validation: operator activated `/mode-dual` + auto-armed `/loop /cycle`; cycles surfaced 8 then 2+5-verified findings |
| OpenArms (potential) | Adoption candidate | — | Different domain (harness engineering); modes might be: harness-engineer / agent-author / dual |
| OpenFleet (potential) | Adoption candidate | — | Different domain (fleet orchestration); modes might be: fleet-coordinator / agent-debugger / dual |
| AICP (potential) | Adoption candidate | — | Different domain (local-AI inference); modes might be: model-curator / cost-optimizer / dual |

The pattern is operator-canonical: *"to drive the development properly and offer an easy and strong loop and adaptive and progress tracking capabilities."* Sister projects implementing it should evaluate their modes against the four named goals (drive development properly, easy + strong loop, adaptive, progress tracking).

## Operator's canonical purpose statement (added 2026-05-05 from empirical test session)

Per operator directive 2026-05-05 (verbatim), the goal of agent modes is:

> *"to drive the development properly and offer an easy and strong loop and adaptive and progress tracking capabilities"*

Four named goals:
1. **Drive the development PROPERLY** — modes shape WHAT gets done, not just how
2. **Offer an EASY and STRONG loop** — autopilot via `/loop /cycle` is the strong loop; ease comes from the mode hiding lens-switching complexity
3. **ADAPTIVE** — modes change behavior per project state (lifecycle scenarios per `loop-cron-lifecycle` rule)
4. **Progress tracking** — modes integrate with backlog readiness flow + governance docs

This is the operator's authoritative framing. Sister projects implementing this pattern should evaluate their modes against these four goals.

## Empirical validation (2026-05-05 test session)

The pattern was validated end-to-end in a fresh /root session:
- Operator typed `/mode-dual` with self-evaluation arguments
- Agent activated dual mode + logged directive verbatim + auto-armed `/loop /cycle`
- Cycle 1 surfaced 8 findings; Cycle 2 surfaced 2 more + 5 verified-clean checks
- Lifecycle signal `L1-near` correctly registered (6 blockers + 40 gated tasks) but didn't auto-cancel because dual-mode requires both lenses idle — Architect lens still had runway
- Findings accumulated in `/root/wiki/log/2026-05-05-mode-dual-self-improvement-iterations.md` as operator directed ("loop till blocked + accumulate + batch-process")

The pattern works as designed. Recommendation for sister-project adoption: copy the determinism ladder + state-file mechanism + per-mode `/cycle` chain. Customize the persona + scope per project domain.

## Why this pattern

Solo + AI scenarios common to small project teams (one operator, one agent) historically conflate roles: the agent is asked to coordinate, design, and implement in the same context, leading to scope drift and lower-quality output per role. Claude Code sub-agents address this via on-demand delegation, but they don't provide a *durable* persona overlay for the main agent.

Three modes give the operator explicit control:

- "I want to do PM work for the next hour" → `/mode-pm` → agent stays in PM lens
- "Now I want to design the install.sh" → `/mode-architect` → engineering lens
- "I'm in mixed work" → `/mode-dual` → switches per question
- "I want this autopilot every 30m" → `/loop 30m /cycle` → mode-cycle fires recurring

The pattern emerged from operator framing 2026-05-05 in root-ghostproxy: *"we will... invent modes... PM Scrum Master Mode and the DevOps Software Engineer & Architect expert mode and the Dual Expert mode and we will when those mode are enabled allow be to trigger with a /loop a desired sequence or group of sequence."*

## Architecture

### Layers

| Layer | What | Where | Determinism |
|---|---|---|---|
| **State** | Active-mode name | `/<project>/.claude/active-mode` (single-line file) | 100% (file-based) |
| **Brain pieces** | Per-mode persona + scope + cycle | `/<project>/.claude/modes/<mode>.md` | Documentation; agent reads and applies |
| **Switch commands** | `/mode-pm`, `/mode-architect`, `/mode-dual`, `/mode-clear`, `/mode-status` | `/<project>/.claude/commands/mode-*.md` | 100% when invoked (harness executes) |
| **Cycle dispatch** | `/cycle` reads state + executes mode-specific chain | `/<project>/.claude/commands/cycle.md` | 100% when invoked |
| **Surface mechanism** | SessionStart hook mentions mode feature when no mode is active | `/<project>/.claude/hooks/session-orient.sh` | ~85% (hook directive via `additionalContext` JSON) |

### Mode anatomy (each mode brain piece must define)

| Section | Purpose |
|---|---|
| Persona | Voice, role, language used |
| Primary brain pieces | Files this mode prioritizes loading |
| Scope discipline | In-scope / out-of-scope; what to defer to other modes |
| /cycle sequence | The chain of actions per `/loop /cycle` fire |
| When to switch out | Operator-facing prompts to move to a different mode |
| Autopilot mention | How this mode + /loop = autopilot for that workstream |

### The 3 modes

#### PM Scrum Master Mode
- **In-scope**: backlog, decisions, status reports, blocker / risk identification, methodology stage tracking, task page authoring (NOT writing the task IS).
- **Out-of-scope**: implementation, architecture design, hook refinement, vendor manifests.
- **/cycle**: orient → surface-decisions → backlog-status → risk-scan → wait.

#### DevOps Software Engineer & Architect Mode
- **In-scope**: install.sh authoring, architecture design, ADRs, vendor manifests, hook refinement, smoke tests, verifier scripts, design docs.
- **Out-of-scope**: backlog grooming as primary focus, decision-tracking, sprint coordination.
- **/cycle**: orient → architecture-review → implementation-progress → stage-gate-check → wait.

#### Dual Expert Mode
- **In-scope**: both. Switches lens per question/task.
- **/cycle**: orient → PM-lens → Architect-lens → cross-cutting → wait. Longer per fire.

### `/loop` integration (autopilot)

Operator runs `/loop 30m /cycle` (or any interval). Each fire:
1. Cron / loop scheduler triggers `/cycle`
2. `/cycle` reads `/<project>/.claude/active-mode` (fresh read each fire — mode change mid-loop takes effect on next fire)
3. Loads the corresponding mode brain piece
4. Executes the mode's `/cycle` sequence
5. Stands by for operator direction; does NOT make decisions or commit forward action unilaterally

This converts mode + /loop into a working autopilot for the project's PM (or Architect, or Dual) workstream.

## When To Apply

- Project has a **clear separation of work types** (PM-vs-engineering distinction is real, not artificial)
- Operator wants **durable mode** state across turns (not just per-task delegation)
- Combined with `/loop`, operator wants **recurring autopilot** that's **mode-aware**
- Project has substantial brain pieces (CLAUDE.md, AGENTS.md, .claude/rules/, methodology config) for modes to overlay on
- Solo + AI configuration where one agent must wear multiple hats over time

## When Not To

- Don't build modes BEFORE the project has substantial brain pieces (modes overlay on top of the brain; without depth, modes are hollow)
- Don't auto-enable a mode at session start (per operator directive: mode-entry is operator-choice; agent informs but doesn't pick)
- Don't skip the **scope discipline** section per mode — without explicit in/out, modes drift into "the agent does whatever"
- Don't apply when project work is uniformly one type (no PM-vs-Architect distinction to separate)
- Don't apply when main agent is short-lived (no benefit to durable persona overlay)
- Don't apply when all work is operator-in-the-loop synchronous (autopilot adds no value)

## Composition with other patterns

- **Sub-agents** are complementary, not replaced: in PM mode, an action like "implement install.sh" can dispatch to a `devops-architect` sub-agent for that specific work, then return to PM mode for the next interaction.
- **Hook → Command determinism ladder** (separate pattern): hooks surface the feature ~85%; commands operate it 100%. Modes use this ladder to balance auto-discoverability with deterministic execution.
- **Three-layer file-handling architecture** (separate pattern): `.gitignore` + `.claudeignore` + `permissions.deny` cover modes' supporting state files (active-mode is small + tracked; mode brain pieces are tracked) without leaking sensitive runtime state.

## Trade-offs

| Choice | Trade-off |
|---|---|
| Mode is persistent across turns (state file) | Cross-session leak: a session enabling /mode-pm leaves the next session in PM mode by default. Document this; let operator clear at session-start if needed. |
| Each mode's `/cycle` is defined inline in the mode file | Centralization: changing the cycle requires editing the mode file. Could be split into per-step commands at cost of more files. |
| `/cycle` reads state fresh each fire | Mode-mid-loop change takes effect next fire (could be confusing). Mitigate by mentioning in autopilot framing. |
| Hook surface is ~85%, not 100% | Some sessions won't see the mode feature mentioned. Mitigation: `/mode-status` always available; `/orient` always mentions modes in its report. |

## First implementation reference

`root-ghostproxy` (sister project at `/root`) — first implementation, 2026-05-05. Files:

- `/root/.claude/modes/pm-scrum-master.md`
- `/root/.claude/modes/devops-architect.md`
- `/root/.claude/modes/dual-expert.md`
- `/root/.claude/commands/mode-{pm,architect,dual,status,clear}.md`
- `/root/.claude/commands/cycle.md`
- `/root/.claude/active-mode` (state file; absent or single-line content)

## Adoption Guide (opt-in transcension to other projects)

Per operator directive 2026-05-05: *"we are also going to find a way to opt in into feature of the root project that start to be interesting that could transcend down into the individual project when desired such as now."*

This pattern is **opt-in**, not auto-applied. A target project (sister project, OR the second-brain itself) adopts it by following the steps below.

### Prerequisites

Before opting in, confirm the target project has:
- [ ] `.claude/` directory with at least CLAUDE.md and AGENTS.md
- [ ] A backlog or work-tracking surface (modes overlay on top of work)
- [ ] Brain pieces of substance (rules, methodology, hooks) — modes are persona OVERLAY, not standalone scaffolding
- [ ] At least one clearly-distinct work-type pair (PM-vs-engineering, or domain-equivalent)

If any prerequisite is missing, build that layer first — adopting modes onto a thin project produces hollow modes.

### Per-project adaptation (modes are NOT one-size-fits-all)

The three modes (PM Scrum Master / DevOps Architect / Dual) work for `root-ghostproxy` because that project has clear PM-vs-engineering distinction. Other projects must **adapt the lenses**:

| Project | Suggested lens A | Suggested lens B | Dual |
|---|---|---|---|
| root-ghostproxy (canonical) | PM Scrum Master | DevOps Architect | Dual |
| Second-brain (/opt) | Knowledge Curator (ingest, distill, mature) | Methodology Steward (engine, gate, schema) | Dual |
| OpenArms (potential) | Harness Engineer | Agent Author | Dual |
| OpenFleet (potential) | Fleet Coordinator | Agent Debugger | Dual |
| AICP (potential) | Model Curator | Cost Optimizer | Dual |

The operator picks the two distinct lenses per project. Don't blindly copy the /root names.

### Files to author in target project

For each target project at `<TARGET>/`:

1. `<TARGET>/.claude/modes/<lens-a>.md` — persona + scope + cycle for lens A
2. `<TARGET>/.claude/modes/<lens-b>.md` — persona + scope + cycle for lens B
3. `<TARGET>/.claude/modes/<dual>.md` — both lenses, cycle that switches per question
4. `<TARGET>/.claude/commands/mode-<a>.md` — slash command to enter lens A
5. `<TARGET>/.claude/commands/mode-<b>.md` — slash command to enter lens B
6. `<TARGET>/.claude/commands/mode-dual.md` — slash command to enter dual
7. `<TARGET>/.claude/commands/mode-clear.md` — slash command to clear mode
8. `<TARGET>/.claude/commands/mode-status.md` — slash command to report current mode
9. `<TARGET>/.claude/commands/cycle.md` — dispatches to the active mode's cycle
10. `<TARGET>/.claude/active-mode` — state file (initially absent or empty)

Each mode brain piece must define: Persona, Primary brain pieces, Scope discipline, /cycle sequence, When to switch out, Autopilot mention.

### Settings.json wiring (optional surface mention)

Add to `<TARGET>/.claude/settings.json` SessionStart hook a one-line mention of the modes feature when no mode is active. Do NOT auto-enable — operator-choice rule per the operator's 2026-05-05 directive.

### Verification

After adoption:
1. Run `/mode-status` — should report "no mode active"
2. Run `/mode-<a>` — should write to `active-mode` and confirm
3. Run `/cycle` — should execute lens A's cycle sequence
4. Run `/mode-clear` — should remove active-mode state
5. Verify lens A and lens B cycles produce different outputs (genuinely distinct lenses)
6. Combined with `/loop 30m /cycle`: verify each fire reads `active-mode` fresh

### Customization checklist

Per-project decisions (not all defaults are universal):

- [ ] Lens A name, persona, primary brain pieces, scope, cycle sequence
- [ ] Lens B name, persona, primary brain pieces, scope, cycle sequence
- [ ] Dual name (often "dual-expert" but project-specific names like "knowledge-and-methodology" also valid)
- [ ] Cycle's autopilot guard scenarios (per loop-cron-lifecycle if adopted; else inline)
- [ ] Whether to wire SessionStart surface mention (recommended)
- [ ] Whether to adopt mode-aware /loop /cycle autopilot (recommended for projects with substantial backlog)

### Currently desired by (project status)

- [x] root-ghostproxy — canonical first implementation (2026-05-05, validated)
- [ ] devops-solutions-information-hub (/opt second-brain) — operator-stated desire ("such as now"); prerequisites check pending
- [ ] OpenArms — adoption candidate (no operator-stated desire yet)
- [ ] OpenFleet — adoption candidate
- [ ] AICP — adoption candidate
- [ ] devops-control-plane — adoption candidate

Operator confirms adoption per project; agent does NOT unilaterally adopt.

## Relationships

