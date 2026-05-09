---
title: "Fire 101 Blocker-Impediment-Registry Tier-Elevation Candidate (Pareto Secondary)"
type: note
note_type: completion
domain: log
status: synthesized
confidence: high
created: 2026-05-08
updated: 2026-05-08
sources:
  - id: fire-101-pattern
    type: wiki
    file: wiki/patterns/01_drafts/blocker-and-impediment-registry-pattern-completes-mode-by-nature-governance-trio.md
    description: "PRIMARY parent (Fire 101)"
  - id: fire-99-elevation-fire-168
    type: wiki
    file: wiki/log/2026-05-08-fire-99-question-registry-tier-elevation-candidate-pareto-secondary.md
    description: "Sibling (Fire 168) — parallel structure"
tags: [fire-101-elevation, blocker-impediment-registry, pareto-secondary, day-arc-2026-05-08, fire-169]
---

# Fire 101 Blocker-Impediment-Registry Tier-Elevation Candidate (Pareto Secondary)

## Summary

Per Fire 125: Fire 101 blocker-impediment-registry pattern scored 13/18 (Pareto Secondary). Current tier T1 (designed; not implemented). Path parallels Fire 99 question-registry.

## Fire 101 current state

```
Title: blocker-and-impediment-registry-pattern-completes-mode-by-nature-governance-trio
Type: pattern
Current tier: T1 (designed; ~/.claude/blockers/ + ~/.claude/active-impediment + 8 slash commands not impl)
Pareto score: 13/18 (Secondary)
Cross-project applicability: HIGH
Empirical evidence: blockers surfaced this conversation (5 BLOCKERS per Fire 140)
```

## Path to T3

```
T1 → T2: state-file structure
  ~/.claude/blockers/{pending,deferred,resolved}/<id>.json
  ~/.claude/active-impediment (single line)
  ~/.claude/impediments-history/<id>.json
  ~/.claude/pending-impediments/<id>.json (FIFO queue)

T2 → T3: 8 slash commands
  /blockers add/show/resolve/defer (4)
  /impediment set/clear/show/queue-add (4)

Effort: 12-20h to T3
Composability: integrates with Fire 98 mode-by-nature + Fire 99 question-registry
```

## Composition

- Fire 99 question-registry (parallel structure; questions can become blockers)
- Fire 98 mode-by-nature (per-cycle surfacing integration)
- Decision-logbook integration (per /root tools.decisions)

## Operator-pending

```
Q-FIRE-169-1: Endorse Fire 101 elevation T1 → T3?
  Recommended: bundle with Fire 99 + Fire 98 (governance trio implementation)

Q-FIRE-169-2: Combined governance trio implementation effort?
  Fire 99 (~12-20h) + Fire 101 (~12-20h) + Fire 98 (~15-25h) = ~40-65h combined
  Calendar: 2-4 weeks at 50% engagement
```

## Closing

Fire 101 = Pareto Secondary. T1 → T3 path: state-files + 8 slash commands (~12-20h). Bundles with Fires 99 + 98 for governance trio (~40-65h combined).

**Standing by per /loop directive.**

## Tags

[fire-101-elevation, blocker-impediment-registry, pareto-secondary, day-arc-2026-05-08, fire-169]
