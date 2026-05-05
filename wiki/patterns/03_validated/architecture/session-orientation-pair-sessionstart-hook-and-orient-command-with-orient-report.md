---
title: "Pattern — Session-orientation pair: SessionStart hook + /orient command + ORIENT REPORT (status I/O for cold-start intelligence)"
type: pattern
domain: cross-domain
status: synthesized
confidence: high
maturity: mature
layer: 2
created: 2026-05-05
updated: 2026-05-05
sources:
  - id: root-ghostproxy-orient-implementation
    type: project
    project: root-ghostproxy
    path: /root/.claude/commands/orient.md
    description: "First implementation: deterministic 21-step intel-gathering chain"
  - id: root-ghostproxy-session-orient-hook
    type: project
    project: root-ghostproxy
    path: /root/.claude/hooks/session-orient.sh
    description: "Session-orient hook (Python, additionalContext JSON) directing the agent to invoke /orient"
  - id: companion-lesson-broken-and-idle
    type: wiki
    file: wiki/lessons/03_validated/context-engineering/broken-and-idle-fresh-sessions-need-active-orientation-not-passive-context-loading.md
    description: "The lesson capturing WHY this pattern exists; this pattern is the HOW + Adoption"
tags: [pattern, session-orientation, sessionstart-hook, orient-command, status-io, cold-start, orient-report, additionalcontext, sister-project-applicable, layer-2, transcendable]
---

# Pattern — Session-orientation pair (SessionStart hook + /orient command + ORIENT REPORT)

## Summary

A two-component coordinated pattern that solves the "broken-and-idle fresh session" failure mode: a SessionStart hook that fires automatically + a deterministic `/orient` slash command + a structured ORIENT REPORT output. Together, these convert a cold-start session from passive context-loading into active project-aware behavior on the first turn.

The pattern is the **Status I/O bundle for cold-start**: hook injects the imperative (input side), agent responds by invoking the command (deterministic chain), command emits a structured report (output side, visible to operator). All three pieces are required — pairs of just two produce gaps (hook alone is ~85% reliable; command alone requires operator typing every session).

## Pattern Description

The pattern composes three deterministic-ladder mechanisms (per `model-skills-commands-hooks`):

1. **SessionStart hook** (`<project>/.claude/hooks/session-orient.sh`) fires on every session start. Outputs structured imperative via `additionalContext` JSON (~85% reliable behavioral influence vs ~70% for plain stdout). The imperative directs the agent: "INVOKE /orient NOW. THIS IS YOUR FIRST ACTION."

2. **Slash command** (`<project>/.claude/commands/orient.md`) executes a deterministic intel-gathering chain when invoked (100% deterministic per invocation). The chain reads brain files, governance docs, recent logs, methodology engine state, sister-project registry, mode state, etc.

3. **ORIENT REPORT** (the command's structured output) emits a fixed-format report: SFIF stage, active modules, pending operator decisions, active mode, next-best-actions. The operator sees the report on their first turn — no "what would you like to work on?" generic greeter.

The pattern realizes the **active orientation** principle: behavior requires direction; auto-loaded text alone is not enough.

## Instances

| Project | Status | Files | Validation |
|---|---|---|---|
| **root-ghostproxy** | First implementation, validated 2026-05-05 | `/root/.claude/hooks/session-orient.sh`, `/root/.claude/commands/orient.md` (21-step chain), structured ORIENT REPORT format | Empirical: pre-fix session "Hi"→"What would you like to work on?" (broken-and-idle); post-fix session "Hi"→agent cites SessionStart hook + references BOOTSTRAP.md + waits for work directive |
| devops-solutions-information-hub (/opt second-brain) | Adoption candidate (not yet adopted) | Has `session-start.sh` (security envelope) but no `/orient` command and no ORIENT REPORT format | Operator-stated desire 2026-05-05 ("such as now") |
| OpenArms | Adoption candidate | — | — |
| OpenFleet | Adoption candidate | — | — |
| AICP | Adoption candidate | — | — |

## When To Apply

- Project has comprehensive brain files (CLAUDE.md / AGENTS.md / BOOTSTRAP.md / rules / governance) that benefit from active orientation
- Operator wants intelligence on first turn (not "what would you like to do?" generic greeter)
- Cold-start sessions are a meaningful fraction of usage (vs always-resumed sessions)
- The project has a coherent ORIENT target (current state worth surfacing on first turn)
- Compaction events occur (PostCompact mirror of the same pattern restores behavioral state)

## When Not To

- Don't apply on projects where the agent is intentionally generic (scratch workspaces)
- Don't apply when load itself is the cost (very short sessions where ORIENT overhead exceeds value)
- Don't apply without a coherent ORIENT target — if the project lacks brain files / governance / state worth surfacing, the report has nothing to report
- Don't try to make the hook DO the command's work directly — hook injects directive; command does work; conflation produces brittle hooks
- Don't auto-execute /orient in the hook — Claude Code hooks output context, not commands; separation of concerns is structural

## Architecture (Status I/O flow)

```
session start
     │
     ▼
┌──────────────────────────────────────┐
│ SessionStart hook fires              │  STATUS INPUT
│ → outputs additionalContext JSON     │  (~85% reliability)
│   "INVOKE /orient NOW"               │
└────────────────┬─────────────────────┘
                 │ injects directive into agent's first-turn context
                 ▼
┌──────────────────────────────────────┐
│ Agent invokes /orient                │  COMMAND DISPATCH
│ → deterministic 21-step chain        │  (100% per invocation)
│   reads brain, gov, logs, state      │
└────────────────┬─────────────────────┘
                 │ chain completes
                 ▼
┌──────────────────────────────────────┐
│ Agent emits ORIENT REPORT            │  STATUS OUTPUT
│ → structured format:                 │  (operator-visible)
│   • SFIF stage                       │
│   • Active modules                   │
│   • Pending operator decisions       │
│   • Active mode                      │
│   • Next-best-actions                │
└──────────────────────────────────────┘
```

The PostCompact mirror: `post-compact.sh` hook fires after context compaction → directs agent to re-invoke /orient → agent re-loads brain + emits a fresh report. This restores behavioral state lost during compaction.

The SessionEnd companion: `session-summary.sh` hook fires at session end → emits a summary status. Closes the I/O loop for the session.

Together these three hooks (SessionStart + PostCompact + SessionEnd) form the **Status I/O bundle** the operator named.

## Why this pattern (vs alternatives)

| Approach | Reliability | Why it falls short |
|---|---|---|
| Auto-loaded brain text alone (CLAUDE.md, AGENTS.md) | ~25% behavioral influence | Text in context ≠ behavioral state; agent defaults to generic greeter |
| SessionStart hook stdout alone | ~70% | Plain text loses against structured imperatives |
| SessionStart hook with `additionalContext` JSON | ~85% | Better but still probabilistic; may miss in some sessions |
| Slash command alone (no hook) | 100% per invoke, ~0% on first turn | Operator must type `/orient` every cold start |
| **Pair: hook + command** | **~85% × 100% = effective ~85%** | Hook directs reliably; command executes deterministically — multiplied reliability |

The pair is the structural answer. Each layer compensates for the other's weakness.

## Adoption Guide (opt-in transcension to other projects)

Per operator directive 2026-05-05: this pattern is part of the **agent-behavior-infrastructure bundle** (modes + commands + /loop + hooks with Status I/O) that transcends from /root to individual projects on opt-in.

### Prerequisites

- [ ] Target project has `.claude/` directory
- [ ] Target project has comprehensive brain files (CLAUDE.md, AGENTS.md, ideally BOOTSTRAP.md or equivalent)
- [ ] Target project has SOMETHING worth surfacing on cold-start (active state, blockers, pending decisions, current stage, etc.) — if there's nothing to report, the pattern is hollow
- [ ] Operator confirms desire to adopt (this is opt-in, not auto-applied)

### Files to author

1. **`<TARGET>/.claude/hooks/session-orient.sh`** — Python script that emits `additionalContext` JSON imperative. Adapt root-ghostproxy's:
   ```python
   #!/usr/bin/env python3
   import json
   directive = """
   <PROJECT-NAME> — NEW SESSION DETECTED. INVOKE /orient NOW.
   ...detailed intel gathering directive customized per project...
   """
   print(json.dumps({"hookSpecificOutput": {"hookEventName": "SessionStart", "additionalContext": directive}}))
   ```

2. **`<TARGET>/.claude/commands/orient.md`** — slash command markdown defining the deterministic intel-gathering chain. The chain steps are project-specific:
   - Read brain files (CLAUDE.md, AGENTS.md, rules, methodology engine state)
   - Read governance docs (blockers, decisions, progress, etc. — if adopted)
   - Read recent logs / raw notes (last N entries from project's log layer)
   - Verify state (sister-projects.yaml registration, methodology engine reachable, git state, etc.)
   - Detect active mode (if modes adopted)
   - Emit structured ORIENT REPORT

3. **`<TARGET>/.claude/hooks/post-compact.sh`** (recommended companion) — fires after context compaction; same imperative pattern, directs re-invoke of /orient.

4. **`<TARGET>/.claude/hooks/session-summary.sh`** (optional companion) — SessionEnd hook emitting a summary status; closes the I/O loop.

### Settings.json wiring

Add to `<TARGET>/.claude/settings.json`:

```json
{
  "hooks": {
    "SessionStart": [
      {"matcher": "", "hooks": [
        {"type": "command", "command": "<TARGET>/.claude/hooks/session-orient.sh", "timeout": 10}
      ]}
    ],
    "PostCompact": [
      {"matcher": "", "hooks": [
        {"type": "command", "command": "<TARGET>/.claude/hooks/post-compact.sh", "timeout": 10}
      ]}
    ]
  }
}
```

### Project-specific customization

The /orient chain content is NOT one-size-fits-all. Each target project must adapt:

| Customization point | What to define |
|---|---|
| Intel-gathering steps (the N steps in /orient) | Project-specific files to read; project-specific verifications to run |
| ORIENT REPORT format | Headings + bullets reflecting the project's primary state surfaces |
| Brain pieces to load | Per-project list (e.g., /opt would load super-model + 4 principles + methodology vs /root loading SFIF stage + modules + governance) |
| Mode awareness | If modes adopted, /orient detects active mode + loads mode brain piece |
| Session-orient directive content | Per-project banner text (project name, type, group, doctrine) |

### Verification (after adoption)

1. Open a fresh session in the target project. Hook should fire automatically.
2. Send "Hi". Agent should reference the SessionStart hook + invoke /orient (~85% reliability).
3. /orient runs the chain. Should complete without errors.
4. Agent emits ORIENT REPORT. Should be structured (sections / bullets / tables, not prose).
5. Trigger a compaction event. PostCompact hook should fire + re-invoke /orient.
6. End session. SessionEnd hook should fire + emit summary.

### Currently desired by

- [x] root-ghostproxy — canonical first implementation (validated)
- [x] devops-solutions-information-hub (/opt second-brain) — adopted 2026-05-05; behavioral verification pending next session. See `wiki/log/2026-05-05-orient-pair-adoption-decision.md`
- [ ] OpenArms — adoption candidate
- [ ] OpenFleet — adoption candidate
- [ ] AICP — adoption candidate
- [ ] devops-control-plane — adoption candidate

## Composition with other transcendable patterns

- **Three-mode pattern** ([[agent-modes-three-mode-pattern-with-mode-aware-loop-cycles]]): /orient detects active mode and loads mode-specific brain pieces. The pair is a prerequisite for modes (modes need orient to load their brain pieces deterministically on cold start).
- **Mode-aware /cycle**: `/cycle` is the autopilot dispatcher; `/orient` is the cold-start equivalent. Different lifecycle events; same determinism-ladder approach.
- **Bug-fix flow** ([[agent-bug-fix-flow-must-be-mechanical-log-analyze-identify-fix-verify-confirm]]): /orient reads recent log layer; the verbatim-log + bug-fix-flow integrates with the orient chain.

## Trade-offs

| Choice | Trade-off |
|---|---|
| Hook uses additionalContext JSON | Higher reliability (~85%) but requires hook to output JSON, not plain text |
| /orient chain is deterministic (markdown defining steps) | Steps are inflexible per session — to handle dynamic state, the steps query state at execution time (not hardcode) |
| ORIENT REPORT is structured | Operator gets clean output; agent has to format consistently — minor cognitive load |
| Pair vs single layer | Two files to maintain; reliability multiplier worth it |

## Anti-patterns

| Anti-pattern | Why bad |
|---|---|
| Hook tries to execute /orient directly | Claude Code hooks output context, not commands; conflates layers |
| /orient lives only as a brain-file rule (no slash command) | Operator can't invoke deterministically; reduces to advisory |
| ORIENT REPORT is prose | Loses signal-to-noise; structured tables/bullets are the discipline |
| Skipping PostCompact mirror | Behavioral state degrades after compaction; report goes stale |
| Auto-loaded brain text alone (no hook + no command) | The "broken-and-idle" failure mode (per the lesson) |

## Relationships

