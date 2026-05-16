---
title: "Fire 99 Question-Registry Tier-Elevation Candidate (Pareto Secondary)"
type: note
note_type: completion
domain: log
status: synthesized
confidence: high
created: 2026-05-08
updated: 2026-05-08
sources:
  - id: fire-99-pattern
    type: wiki
    file: wiki/patterns/01_drafts/question-registry-discipline-bidirectional-question-answering-with-audience-taxonomy.md
    description: "PRIMARY parent (Fire 99)"
  - id: fire-110-instance
    type: wiki
    file: wiki/log/2026-05-08-question-registry-instance-6-questions-from-auto-compact-priority-sequence-fires-102-109-formal-surface.md
    description: "Sibling (Fire 110) — first instance application"
tags: [fire-99-elevation, question-registry, pareto-secondary, day-arc-2026-05-08, fire-168]
---

# Fire 99 Question-Registry Tier-Elevation Candidate (Pareto Secondary)

## Summary

Per Fire 125: Fire 99 question-registry pattern scored 14/18 (Pareto Secondary). Per Fire 110: first instance applied. Current tier T1 (designed; slash commands not implemented).

## Fire 99 current state

```
Title: question-registry-discipline-bidirectional-question-answering-with-audience-taxonomy
Type: pattern
Current tier: T1 (designed; 5 slash commands /questions add/show/answer/defer/withdraw not implemented)
Pareto score: 14/18 (Secondary)
Cross-project applicability: HIGH
Empirical evidence: Fire 110 first instance + Fires 113/118/119/121/137 each surface Q's
```

## Path to T3

```
T1 → T2: implement state-file structure
  ~/.claude/active-questions/<audience>/<id>.json schema

T2 → T3: implement /questions slash commands
  /questions add <text> [--audience operator|agent|sister|future]
  /questions show [--audience X] [--status pending|answered|deferred]
  /questions answer <id> "<text>"
  /questions defer <id>
  /questions withdraw <id>

Effort: 12-20h to T3
Composability: integrates with mode-by-nature (Fire 98) per-cycle scan
```

## Composition

- Fire 110 (instance application; provides 6 question test-cases)
- Fire 101 blocker-impediment-registry (parallel structure)
- Fire 98 mode-by-nature (per-cycle surfacing integration)

## Operator-pending

```
Q-FIRE-168-1: Endorse Fire 99 elevation T1 → T3?
  Recommended: bundle with Fire 101 blocker-impediment-registry parallel
  
Q-FIRE-168-2: Slash command implementation pattern?
  Per the second-brain commands/ existing patterns
```

## Closing

Fire 99 = Pareto Secondary. T1 → T3 path: state-files + 5 slash commands (~12-20h). Composes with Fires 101 + 98.

**Standing by per /loop directive.**

## Tags

[fire-99-elevation, question-registry, pareto-secondary, day-arc-2026-05-08, fire-168]
