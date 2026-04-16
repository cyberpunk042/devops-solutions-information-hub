---
title: E022-M002 — Gateway Orient Subcommand (Module Design)
aliases:
  - "E022-M002 — Gateway Orient Subcommand"
  - "M002 — Gateway Orient Subcommand"
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
tags: [module, gateway, orient, context-detection, session-state, design, e022]
---

# E022-M002 — Gateway Orient Subcommand (Module Design)

## Summary

Design for the new `gateway orient` subcommand. Its job: answer "who are you, where, are you fresh, what must you internalize before doing anything" — with context-aware output branching on location (second-brain / sister / external) × freshness (fresh / task-bound / returning). This design spec covers context detection function, session-state file format, output mode dispatch, and declared-over-detected ordering. Gate: spec reviewed and approved before scaffold stage.

## Goals

- A single `gateway orient` subcommand that produces the correct output for every (location, freshness) pair without operator needing to specify them
- Declared-over-detected ordering preserved: explicit flags > env vars > CLAUDE.md declarations > filesystem heuristics
- Sanity-check warnings emitted on stderr when heuristics disagree with declarations (so disagreements are visible, not silent)
- Output in every mode passes all 5 rules of the [[gateway-output-contract|Gateway Output Contract]]
- Session-state file makes freshness inspectable post-compaction (the primary use case)

## Design Decisions

### Decision 1 — Context Detection Algorithm

> [!info] Detection order (highest authority first)
>
> | Priority | Signal | Type |
> |----------|--------|------|
> | 1 | `--orient-as <mode>` CLI flag | Fully declared, trumps all |
> | 2 | `MCP_CLIENT_RUNTIME` env var | Consumer-declared (existing convention) |
> | 3 | `--wiki-root <path>` flag | Stable identity signal (explicit) |
> | 4 | CLAUDE.md declarations in resolved repo | Stable identity (project-declared) |
> | 5 | Filesystem heuristics (CWD resolution) | Sanity-check only, warns on disagreement |

**Location classification:**

```
if MCP_CLIENT_RUNTIME set AND indicates external:
    location = external
elif --wiki-root resolves to second-brain repo (or CWD is second-brain repo):
    location = second-brain
elif --wiki-root resolves to registered sister (from sister-projects.yaml):
    location = sister
else:
    location = external
```

**Freshness classification:**

```
if --fresh flag:
    freshness = fresh
elif session-state file absent:
    freshness = fresh
elif session-state.current_task_type set AND last_update < 30 min ago:
    freshness = task-bound
elif session-state present AND last_update < 30 min ago:
    freshness = returning
else:
    freshness = fresh
```

### Decision 2 — Session-State File

> [!info] Location and format
>
> | Aspect | Value |
> |--------|-------|
> | **Location** | `~/.cache/research-wiki/session-state.json` (XDG cache dir, not in repo) |
> | **Why outside repo** | Session state is per-user-per-machine, not shared. Never committed. Survives compaction because it's file-based. |
> | **Lifecycle** | Created on first gateway invocation; updated on every subsequent invocation; stale after 30 minutes |
> | **Updated by** | Any gateway subcommand (orient included) writes `last_invocation` + context fields |

**Schema:**

```json
{
  "last_invocation": "2026-04-15T20:30:00Z",
  "last_subcommand": "orient",
  "location": "second-brain",
  "freshness": "fresh",
  "current_task_type": null,
  "consumer_runtime": "solo",
  "wiki_root_resolved": "/home/jfortin/devops-solutions-research-wiki",
  "session_id": "<uuid, rotated on detected compaction>"
}
```

`current_task_type` is `null` until set by `what-do-i-need --task <type>`. Its presence is the main task-bound signal.

`session_id` rotation handles the compaction case: if the agent loses context, a new session ID means the agent is effectively fresh even though the file exists. Detection: if `session_id` in the environment differs from the file (e.g., via a harness setting it), treat as fresh.

### Decision 3 — Output Mode Dispatch

Six (location, freshness) cells, three require full orient output, three redirect:

> [!abstract] Dispatch matrix
>
> | Location | Freshness | Output |
> |----------|-----------|--------|
> | second-brain | fresh | Full orient — brain reading path + standing rules |
> | second-brain | task-bound | Redirect: `NEXT: gateway what-do-i-need` (you know the base) |
> | second-brain | returning | Redirect: `NEXT: gateway what-do-i-need` |
> | sister | fresh | Full orient — how to consume second brain + contribute pattern |
> | sister | task-bound | Redirect: `NEXT: gateway query --task <type> --brain` |
> | sister | returning | Redirect: `NEXT: gateway <last_subcommand>` or `what-do-i-need` |
> | external | any | Full orient — MCP tool list + one-shot docs (freshness irrelevant without session file) |

**Rationale for redirects on task-bound / returning:** orient teaches the base. If you already know the base (task-bound means you're mid-work; returning means you invoked gateway recently), you don't need re-teaching. A one-line redirect preserves the SRP rule (orient ≠ route) while acknowledging the invocation was wrong-shape for the context.

### Decision 4 — Declared-Over-Detected Warning Protocol

When a heuristic signal disagrees with a declared value, emit a warning on **stderr** (not stdout — stdout is the contract-shaped output; stderr is metadata).

Warning format:

```
⚠ heuristic detected location=second-brain (CWD=<path>) but MCP_CLIENT_RUNTIME
  declared location=external. Honoring declaration (external).
  To override declaration, pass --wiki-root explicitly or unset the env var.
```

Rationale: silencing the heuristic entirely would hide bugs (wrong env var, typo in declaration). Warning on stderr surfaces the disagreement without corrupting the output contract.

### Decision 5 — Subcommand Signature

```
gateway orient
    [--orient-as second-brain|sister|external]         # explicit override
    [--fresh]                                         # force fresh freshness
    [--wiki-root PATH]                                # existing flag, reused
    [--brain PATH]                                    # existing flag, reused
    [--format text|json]                              # default text
```

`--format json` returns the context + next-move as structured data (for harness / MCP integration). `--format text` is the contract-shaped human/agent output.

### Decision 6 — MCP Tool Exposure

`wiki_gateway_orient(orient_as, fresh, wiki_root, brain, output_format)` — same surface as CLI. Description in the MCP tool registration must include:

- When to invoke (fresh session, post-compaction, entering the second brain for the first time)
- What it returns (context + reading path + standing rules + next move)
- When NOT to invoke (during an active task — use what-do-i-need instead)

## Tasks

| Task | What | Stage |
|------|------|-------|
| T-E022-04 | Design context detection function (second-brain / sister / external × fresh / task-bound / returning) with declared > detected priority | design (DONE — Decision 1 of this doc) |
| T-E022-05 | Design session-state file format for freshness detection | design (DONE — Decision 2 of this doc) |
| T-E022-06 | Scaffold `orient` subcommand in `tools/gateway.py` with argparse entry + context detector stub + empty mode handlers | scaffold |
| T-E022-07 | Implement the six output modes (3 full orient outputs + 3 redirects per dispatch matrix) | implement |
| T-E022-08 | Verify each output mode passes all 5 contract rules via manual audit + integration test | test |

## Done When

- [ ] Design reviewed and approved by operator (gate for exiting design stage)
- [ ] T-E022-04 complete: context detection function designed (this doc, Decision 1 — DONE)
- [ ] T-E022-05 complete: session-state file format specified (this doc, Decision 2 — DONE)
- [ ] All 6 dispatch cells have defined output (full or redirect) — DONE in Decision 3
- [ ] Declared-over-detected warning protocol specified — DONE in Decision 4
- [ ] MCP tool signature specified — DONE in Decision 6
- [ ] Scaffold stage picked up (T-E022-06, -07, -08) after operator approval

## Open Questions

> [!question] Should `session-state.json` include a hash of CLAUDE.md / CONTEXT.md to detect second-brain repo changes?
> Useful for invalidating session-state when the second brain's declarations change (e.g., phase moves from production to staging). Adds complexity; may be overkill for a cache file. Lean: NO for v1; add later if drift becomes a real problem.

> [!question] Should the 30-minute staleness threshold be configurable?
> Different sessions have different cadences. A cron-driven agent may invoke every few hours; an interactive session every few minutes. Lean: YES, but not for v1. Hard-code 30 min initially; make configurable if the value proves wrong.

> [!question] Should `--orient-as` accept a freshness hint too?
> Currently freshness is `--fresh` (force fresh) or heuristic. Could add `--task-bound` + `--returning` for full control. Lean: NO for v1. Explicit `--fresh` covers the main need (post-compaction). Task-bound / returning are detected reliably from session-state.

> [!question] Does the external mode need session-state at all?
> External callers (MCP clients without a repo) have no stable identity. Session-state may not make sense. Lean: still write session-state even for external mode — enables detecting repeated invocations and avoiding repeated full-orient dumps.

## Dependencies

- [[e022-context-aware-gateway-orientation-and-routing|E022]] — parent epic
- [[gateway-output-contract|Gateway Output Contract]] — every mode's output is audited against its 5 rules
- `sister-projects.yaml` registry — used to classify `sister` location (must be readable from the second brain)
- Existing `tools/gateway.py` — adds new subparser, reuses `--wiki-root` / `--brain` resolution
- Existing `MCP_CLIENT_RUNTIME` env var convention ([[consumer-runtime-signaling-via-mcp-config|Consumer Runtime Signaling via MCP Config]])

## Scaffold Readiness

Once operator approves this design, M002 enters scaffold stage with the following ALLOWED artifacts:

- New argparse subparser for `orient` in `tools/gateway.py` (stub only — no output logic yet)
- Empty context detection function with signature matching Decision 1 (returns stub values)
- Empty session-state read/write helpers (return hardcoded values)
- Empty output-mode dispatch (prints placeholders per cell)
- MCP tool stub in `tools/mcp_server.py`

FORBIDDEN in scaffold: real output formatting, real heuristic logic, real warning emission. Those are implement-stage work.

## Relationships

- PART OF: [[e022-context-aware-gateway-orientation-and-routing|E022 — Context-Aware Gateway Orientation and Task Routing]]
- BUILDS ON: [[gateway-output-contract|Gateway Output Contract — What Good Tool Output Looks Like]]
- RELATES TO: [[consumer-runtime-signaling-via-mcp-config|Decision — Consumer Runtime Signaling via MCP Config]]
- RELATES TO: [[execution-mode-is-consumer-property-not-project-property|Execution Mode Is a Consumer Property, Not a Project Property]]
- RELATES TO: [[model-mcp-cli-integration|Model — MCP and CLI Integration]]

## Backlinks

[[e022-context-aware-gateway-orientation-and-routing|E022 — Context-Aware Gateway Orientation and Task Routing]]
[[gateway-output-contract|Gateway Output Contract — What Good Tool Output Looks Like]]
[[consumer-runtime-signaling-via-mcp-config|Decision — Consumer Runtime Signaling via MCP Config]]
[[execution-mode-is-consumer-property-not-project-property|Execution Mode Is a Consumer Property, Not a Project Property]]
[[model-mcp-cli-integration|Model — MCP and CLI Integration]]
