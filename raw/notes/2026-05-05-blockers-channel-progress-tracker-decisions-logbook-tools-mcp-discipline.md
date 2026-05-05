---
title: "2026-05-05 — Operator directive: governance layer (blockers channel + progress tracker + decisions logbook with SRP) + tools-vs-commands-vs-MCP discipline"
type: note
domain: cross-domain
status: raw
confidence: high
created: 2026-05-05
updated: 2026-05-05
sources:
  - id: operator-directive-2026-05-05-governance-and-tools-discipline
    type: directive
tags: [note, operator-directive, sacrosanct, verbatim, governance, blockers, progress-tracker, decisions-logbook, srp, tools, commands, mcp-discipline, observability, planning-perspective]
---

# Operator directive — 2026-05-05 governance layer + tools/MCP discipline

## Verbatim

> "there should be a clear channel of the blockers that cummulate that require my inputs and the tracking of the progress and the view of journey and current position and planning.. we need to solve the lack of perspective / view of the planning the that act seem to have even regress arround. so yeah like I said I really need a way to have the blockers surfacing and with enough context and explanation so I can answer and so I dont receive dumb questions too. There can also be a tracking of the decisions like a logbook that I can look at, similar to a kind of progress trackin but with its own SRP... like we aspire to have in general. important note. (when needed a bit like with in the second-brain we can do tool for the things that have no need to be done by a model but mostly empower or interact or exploit it.) a bit like commands but obviously thats the deeper level and yes a command can make use a tools or MCP depending on the case / needs. those been complimentary but MCP we must not overflow especially with things that are useless or confusing or useless or we dont even refer to anywhere so will never be used..."

## Decomposition

### A — Blockers channel
- "clear channel of the blockers that cummulate that require my inputs"
- Blockers cumulate over time; need a centralized surfaced channel
- "with enough context and explanation so I can answer" — operator-facing, not agent-internal
- "so I dont receive dumb questions too" — context must be sufficient that operator doesn't need clarification

### B — Progress tracker / journey view
- "the tracking of the progress and the view of journey and current position and planning"
- "we need to solve the lack of perspective / view of the planning the that act seem to have even regress arround"
- The agent regresses when it lacks the planning view — current gap to fix
- View = where we are + where we're going + how we got here

### C — Decisions logbook
- "tracking of the decisions like a logbook that I can look at"
- "similar to a kind of progress trackin but with its own SRP"
- Single Responsibility Principle: decisions logbook is its OWN artifact, distinct from progress tracking and blockers
- Audit trail for decisions made

### D — Tools layer (deeper than commands)
- "(when needed a bit like with in the second-brain we can do tool for the things that have no need to be done by a model but mostly empower or interact or exploit it.)"
- Tools = deterministic non-model invocations
- Empower / interact with / exploit the system without needing LLM
- "a bit like commands but obviously thats the deeper level"
- Commands COMPOSE tools + MCPs
- "(when needed)" — qualifier; build tools when complexity warrants, not pre-emptively

### E — MCP discipline
- "MCP we must not overflow especially with things that are useless or confusing or useless or we dont even refer to anywhere so will never be used"
- Don't add MCPs for the sake of having them
- Only register MCPs that are referenced and actually used
- Useless / unreferenced MCPs eat context budget + confuse

## Action plan

1. Log this directive verbatim — done.
2. Create `/root/wiki/governance/` with three SRP-separated docs:
   - `blockers.md` — operator-facing blockers register (with context + explanation per blocker)
   - `progress.md` — journey view (where + headed + how)
   - `decisions.md` — decisions logbook (chronological, with rationale)
3. Author 3 slash commands: `/blockers`, `/progress`, `/decisions` — read + present each doc.
4. Update mode `/cycle` sequences to invoke these as appropriate per mode.
5. Update CONTEXT.md to point at the governance layer.
6. Capture tools discipline as principle (no implementation — "when needed"). MCP discipline same.

## SRP for the three governance docs

| Doc | Single Responsibility |
|---|---|
| `blockers.md` | What requires operator input; cumulative; current state of pending decisions with full context |
| `progress.md` | Where the project IS (current position) + where it's HEADED (planning) + journey traveled |
| `decisions.md` | Audit trail of decisions made; rationale; downstream effects; chronological |

Don't conflate. Blockers ≠ decisions made; progress ≠ blockers; progress ≠ decisions log.

## No-conflate guard

- "(when needed)" about tools = not a directive to build tools now; future option.
- "MCP we must not overflow" = principle/discipline, not a directive to refactor existing MCPs.
- "the agent seems to have even regress around" = operator-observed behavior; the governance layer addresses the perspective gap that drives regression.
