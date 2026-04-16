---
title: E022-M003 — Gateway What-Do-I-Need Upgrade (Module Design)
aliases:
  - "E022-M003 — Gateway What-Do-I-Need Upgrade"
  - "M003 — What-Do-I-Need Upgrade"
type: module
domain: backlog
status: active
priority: P1
task_type: module
current_stage: design
readiness: 40
progress: 0
stages_completed: []
epic: E022
artifacts: []
confidence: high
created: 2026-04-15
updated: 2026-04-15
sources:
  - id: parent-epic
    type: wiki
    file: wiki/backlog/epics/milestone-v2/e022-context-aware-gateway-orientation-and-routing.md
  - id: output-contract
    type: wiki
    file: wiki/spine/standards/gateway-output-contract.md
  - id: m002-design
    type: wiki
    file: wiki/backlog/modules/e022-m002-gateway-orient-subcommand.md
tags: [module, gateway, what-do-i-need, context-aware, srp, upgrade, design, e022]
---

# E022-M003 — Gateway What-Do-I-Need Upgrade (Module Design)

## Summary

Design for upgrading the existing `gateway what-do-i-need` subcommand to be context-aware (second-brain / sister / external × fresh / task-bound) and SRP-compliant. This is NOT a new subcommand — it's a rework of an existing one. The current output mixes task routing + consumer-runtime signaling + default-profile advice (3 questions in 1 output, violating Rule 1 of the [[gateway-output-contract|Gateway Output Contract]]). This design separates concerns, adds context branches, and closes with an unambiguous next-move. Reuses M002's context detection (Decision 1), session-state (Decision 2), and warning protocol (Decision 4) — only the output modes are new.

## Goals

- SRP: what-do-i-need answers ONLY "given your context, what's the right work path?"
- Context-aware: second-brain returns knowledge-verb task types; sister returns sister routing; external returns MCP tool pointers
- Fresh agents get a redirect to orient, NOT an inline teaching (orient's job, not this command's)
- Output passes all 5 contract rules in every mode
- No regression for sister and external consumers who currently get useful output (just shaped better)

## Design Decisions

### Decision 1 — SRP Separation (What to Remove)

Current output mixes three concerns. The upgrade separates them:

> [!abstract] Current-to-target mapping
>
> | Current content block | SRP violation? | Where it goes |
> |----------------------|----------------|---------------|
> | **PROJECT IDENTITY** section (domain, phase, scale, second brain, all ✓-marked) | No — contextual header, relevant to routing | KEEP — trimmed to 2 lines: `location: second-brain` + `freshness: task-bound` |
> | **CONSUMER / TASK PROPERTIES** section (execution mode, methodology model, SDLC profile) | YES — separate concern from routing | REMOVE from main output. Consumer runtime → visible only in `orient` (which lists MCP_CLIENT_RUNTIME if declared). Methodology model / SDLC profile → shown per task-type row, not as project-wide declaration |
> | **SUGGESTED DEFAULT PROFILE** section | YES — conflates project-wide with per-task | REMOVE. Profile is per-task (embedded in task-type table), not project-wide advice |
> | **YOUR FIRST STEPS** section | Rule 5 violation — menu of 3, not a single next-move | REPLACE with `NEXT:` single line |
> | **EXPLORE MORE** footer | Rule 5 violation — menu of 4 commands | REMOVE entirely. Next move is sufficient. Gateway --help covers browse needs. |

**Net effect:** output goes from ~40 lines (currently) to ~35 lines (target), but coherent and SRP-clean.

### Decision 2 — Brain-Self Output Mode

Two branches within second-brain based on freshness:

**Brain-self + fresh:**

```
⚠ READ THIS OUTPUT IN FULL — you need orientation before routing.

WHAT DO YOU NEED? — You are inside the second brain, but FRESH.

You need orientation before task routing.

NEXT: gateway orient    (internalize the base first)
```

8 lines. Under ceiling. SRP: redirects to orient. Does NOT duplicate orient's teaching content.

**Brain-self + task-bound:**

```
⚠ READ THIS OUTPUT IN FULL — routing depends on the task-type table.

WHAT DO YOU NEED? — Inside the second brain (self = brain)

  location:   second-brain
  freshness:  task-bound

  Task type               | Verbs activated         | Entry
  ------------------------|-------------------------|------------------------
  Ingest source           | aggregate → process     | skill: wiki-agent
                            → integrate → validate |
  Evolve candidate        | evaluate → learn        | skill: evolve
                            → integrate → validate |
  Promote to principle    | evaluate → modelize     | gateway query --review
                            → validate             |
  Author standards        | modelize → standardize  | skill: model-builder
                            → teach → validate     |
  Aggregation sweep       | aggregate → integrate   | sister_project + timeline
                            → evaluate (no write)  |
  Cross-ecosystem retro   | aggregate → integrate   | timeline --scope all
                            (timeline) → evaluate  |
  Expose new tool         | offer → validate        | tools/gateway.py + mcp_server.py

NEXT: gateway query --task <type>    (loads verb chain for that task)
```

~30 lines. Under ceiling. SRP: routes to task types only. Knowledge-verb task types specific to the second brain — NOT the app-dev models (feature-development, bug-fix, etc. are for sister projects).

### Decision 3 — Sister Output Mode

Two branches:

**Sister + fresh:**

```
⚠ READ THIS OUTPUT IN FULL — you need orientation first.

WHAT DO YOU NEED? — You are a sister project connecting to the second brain.

You need orientation before consuming.

NEXT: gateway orient    (learn how to consume the second brain)
```

Same redirect pattern as second-brain + fresh. Keeps SRP.

**Sister + task-bound:**

```
WHAT DO YOU NEED? — Sister project (<project-name>), task-bound

  Your project methodology models:
    gateway query --models --wiki-root <your-path>

  Brain's methodology for your task type:
    gateway query --model <type> --brain

  Contribute back after work:
    gateway contribute --type lesson --brain

NEXT: gateway query --model <task-type> --brain
```

~15 lines. Routes to second-brain queries + contribution flow. Keeps SRP (routing only; no teaching).

### Decision 4 — External Output Mode

No freshness branching (external callers don't have session-state).

```
WHAT DO YOU NEED? — External MCP client

  Available MCP tools: 26
  Start with:
    wiki_status           → wiki health snapshot
    wiki_gateway_docs     → root documentation
    wiki_search           → keyword search

  One-shot orientation:
    wiki_read_page("super-model")

NEXT: wiki_status    (start with status)
```

~12 lines. Minimal, tool-focused. Keeps SRP.

### Decision 5 — Reuse from M002

| Reused decision | From | How reused |
|----------------|------|-----------|
| Context detection algorithm | M002 Decision 1 | Same function call; what-do-i-need invokes the same detector orient uses |
| Session-state file | M002 Decision 2 | what-do-i-need reads AND writes session-state (including setting `current_task_type` when routing) |
| Warning protocol | M002 Decision 4 | Same stderr warnings when heuristics disagree with declarations |

No duplication. The context detection function is shared code, not copied logic.

### Decision 6 — Session-State Write on Routing

When what-do-i-need completes routing (second-brain + task-bound mode), it writes `current_task_type` to session-state. This enables subsequent orient invocations to detect `task-bound` freshness — closing the loop:

```
orient (fresh) → what-do-i-need (routes, writes task_type) → orient (detects task-bound, redirects)
```

Without this write, orient can't distinguish "user finished task-routing" from "user is still fresh." The session-state file is the inter-subcommand state machine.

## Tasks

| Task | What | Stage |
|------|------|-------|
| T-E022-09 | Design context branching for what-do-i-need; identify SRP violations to fix | design (DONE — Decision 1 of this doc) |
| T-E022-10 | Scaffold context branches in what-do-i-need handler (stubs returning placeholder per mode) | scaffold |
| T-E022-11 | Implement second-brain branch: fresh redirect + task-bound knowledge-verb table | implement |
| T-E022-12 | Implement sister and external branches | implement |
| T-E022-13 | Honor declared > detected: remove heuristic overrides; heuristics become stderr warnings only | implement |
| T-E022-14 | Verify all modes pass 5 contract rules via manual audit | test |

## Done When

- [ ] T-E022-09 complete: SRP separation designed + context branches specified (this doc — DONE)
- [ ] Design reviewed and approved by operator
- [ ] Current output's consumer-runtime and default-profile blocks removed or relocated
- [ ] Brain-self output shows knowledge-verb task types (not app-dev models)
- [ ] Fresh agents get redirect to orient (not inline teaching)
- [ ] `NEXT:` line closes every output mode (no menus)
- [ ] session-state `current_task_type` written on routing
- [ ] Scaffold tasks (T-E022-10 through T-E022-14) can proceed

## Open Questions

> [!question] Should second-brain + task-bound include a "not finding your task type?" footer pointing to gateway orient?
> Covers the edge case where the knowledge-verb table doesn't match the agent's actual work. One extra line. Lean: YES — add a footer `Not listed? → gateway orient for full base context, or gateway flow for operational flow.` Keeps it to two choices (orient OR flow), not a menu.

> [!question] Should the task-type table reference E024 knowledge-verbs when that epic lands?
> Currently the table is inline (hardcoded in the what-do-i-need handler). Once E024 ships knowledge-verbs.yaml, the table could be computed FROM config. Lean: hardcode for v1; switch to config-driven when E024 ships. Avoids blocking M003 on E024.

> [!question] What happens to the "CONSUMER / TASK PROPERTIES" block currently in what-do-i-need?
> Per Decision 1: removed from main output. But should it move to orient (where it contextualizes the consumer's declarations) or to a new `gateway identity` subcommand? Lean: into orient's second-brain + task-bound redirect mode as a 1-line "Your declared runtime: <X>" — keeps orient's SRP (it contextualizes identity) without bloating it.

## Dependencies

- [[e022-m002-gateway-orient-subcommand|E022-M002 — Gateway Orient Subcommand]] — context detection, session-state, warning protocol all reused from M002
- [[gateway-output-contract|Gateway Output Contract]] — every mode audited against 5 rules
- Existing `tools/gateway.py` `query_what_do_i_need()` function — the code being upgraded
- E024 (Knowledge-Verbs, future) — task-type table becomes config-driven once E024 ships; not a blocker

## Scaffold Readiness

Once operator approves this design, M003 enters scaffold stage. ALLOWED:

- Context branches in existing `query_what_do_i_need()` handler (stubs returning placeholders)
- Shared context detection function call (from M002 shared code)
- Session-state write stub for `current_task_type`

FORBIDDEN in scaffold: real output formatting, real SRP extraction, real heuristic removal.

## Relationships

- PART OF: [[e022-context-aware-gateway-orientation-and-routing|E022 — Context-Aware Gateway Orientation and Task Routing]]
- DEPENDS ON: [[e022-m002-gateway-orient-subcommand|E022-M002 — Gateway Orient Subcommand]]
- BUILDS ON: [[gateway-output-contract|Gateway Output Contract — What Good Tool Output Looks Like]]
- RELATES TO: [[execution-mode-is-consumer-property-not-project-property|Execution Mode Is a Consumer Property, Not a Project Property]]
- RELATES TO: [[model-mcp-cli-integration|Model — MCP and CLI Integration]]

## Backlinks

[[e022-context-aware-gateway-orientation-and-routing|E022 — Context-Aware Gateway Orientation and Task Routing]]
[[e022-m002-gateway-orient-subcommand|E022-M002 — Gateway Orient Subcommand]]
[[gateway-output-contract|Gateway Output Contract — What Good Tool Output Looks Like]]
[[execution-mode-is-consumer-property-not-project-property|Execution Mode Is a Consumer Property, Not a Project Property]]
[[model-mcp-cli-integration|Model — MCP and CLI Integration]]
