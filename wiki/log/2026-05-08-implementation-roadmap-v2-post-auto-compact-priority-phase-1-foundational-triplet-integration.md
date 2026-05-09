---
title: "Implementation Roadmap v2 — Post-Auto-Compact Priority + Phase 1 Foundational-Triplet Integration"
type: note
note_type: completion
domain: log
status: synthesized
confidence: high
created: 2026-05-08
updated: 2026-05-08
sources:
  - id: implementation-roadmap-v1-fire-58
    type: wiki
    file: wiki/patterns/01_drafts/implementation-roadmap-pattern-sequenced-milestones-from-confirmation-to-tier-3.md
    description: "PRIOR roadmap (Fire 58) — sequenced milestones M1-M7; this v2 integrates auto-compact priority + Phase 1"
  - id: foundational-triplet-solution-fire-137
    type: wiki
    file: wiki/log/2026-05-08-foundational-triplet-solution-piece-chain-c04-c02-c09-phase-1-implementation-forward-anchor.md
    description: "PRIMARY parent (Fire 137) — Phase 1 forward-anchor; this v2 incorporates"
  - id: auto-compact-backlog-decomposition-fire-108
    type: wiki
    file: wiki/log/2026-05-08-auto-compact-priority-backlog-decomposition-epic-4-modules-15-tasks-fire-97-pattern-application.md
    description: "Sibling (Fire 108) — auto-compact decomposition; this v2 sequences with Phase 1"
  - id: tier-elevation-pathway-fire-109
    type: wiki
    file: wiki/patterns/01_drafts/tier-elevation-pathway-pattern-systematic-tier-1-to-tier-4-transitions-per-body-piece.md
    description: "PRIMARY parent (Fire 109) — methodology consumed by roadmap"
tags: [implementation-roadmap, v2, auto-compact-priority, phase-1-integration, day-arc-2026-05-08, fire-139]
---

# Implementation Roadmap v2 — Post-Auto-Compact Priority + Phase 1 Foundational-Triplet Integration

## Summary

Per Fire 58 v1 implementation-roadmap: sequenced milestones M1-M7 from operator-confirmation to tier-3 deployment. Per Fires 102-137 post-compact era: auto-compact priority + foundational-triplet emerge as PRE-M1 dependencies. This Fire 139 v2 roadmap integrates: pre-M1 phase (auto-compact + Phase 1) → M1-M7 (existing) → cross-project propagation. Estimated end-to-end: 6-12 months calendar time depending on operator-empirical engagement cadence.

## v1 baseline (Fire 58)

```
M1: Operator-confirmation phase (per-piece review)
M2: Tier-1 → Tier-2 promotion
M3: Tier-2 → Tier-3 deployment
M4: Standardize-extension applications
M5: Modelize-extension applications
M6: Sister-project propagation Phase 1
M7: Sister-project propagation Phase 2-N
```

## v2 (this fire) — sequenced post-Fire-137

```
PRE-M1: AUTO-COMPACT PRIORITY (Fires 102-108 + 137)
  Duration: 18-26h Phase 1 + investigation
  Tasks:
    - M-AC1 Investigation (4-6h) → Q1-Q4 resolution
    - M-AC2 Layer 1 Prevention (4-6h)
    - M-AC3 Layer 2+3 Mitigation+Enforcement (6-8h)
    - M-AC4 Documentation+Verification+Propagation (4-6h)
  Dependency: operator-empirical Q-FIRE-110 + Q-FIRE-128 + Q-FIRE-137 answers

PHASE-1: FOUNDATIONAL TRIPLET ENFORCEMENT (Fire 137)
  Duration: 48-74h
  Tasks:
    - M-C04 input-discipline hook (16-24h)
    - M-C02 decision-territory hook (16-24h)
    - M-C09 status-claim hook (12-20h)
    - M-VERIFY combined coverage measurement (4-6h)
  Dependency: operator-empirical Q-FIRE-137 endorsement + parallel/sequential pick
  Deliverable: composite-compliance ~58% → ~63-68%; cross-cutting catch ~70-80%

M1: OPERATOR-CONFIRMATION (per Fire 58 + this v2)
  Duration: variable (per-piece operator-review pace)
  Per Fire 121 7-criterion: ready-for-review state SUSTAINED
  Per Fire 125: Pareto-priority subset (5 pieces); secondary (14 pieces)
  Tasks:
    - PATH 1 Pareto-priority review (1-3h)
    - PATH 5 Decision-packages review (1-2h)
    - Pieces selected for tier-2 promotion based on review
  Dependency: operator schedules review session

M2: TIER-1 → TIER-2 PROMOTION (per Fire 58 + Fire 109)
  Duration: 6-26h per piece × N pieces
  Per Fire 109 5-step elevation procedure
  Per Fire 125 Pareto-priority: 5 pieces × 8-26h = 40-130h
  Per all T1 pieces: 50+ pieces × 6-15h = 300-750h (full body elevation)
  Dependency: M1 complete

M3: TIER-2 → TIER-3 DEPLOYMENT (per Fire 58)
  Duration: 30-day cross-reference period per piece
  Per /opt promotion methodology
  Dependency: M2 complete

M4: STANDARDIZE-EXTENSION APPLICATIONS
  Per existing standardize-extension proposals (Fires 30-35 era + Fires 112+116)
  Per HR 16 + wiki-schema field
  Duration: 8-15h per proposal × N proposals

M5: MODELIZE-EXTENSION APPLICATIONS  
  Per existing modelize-extension proposals
  Duration: 8-15h per proposal × N proposals

M6: SISTER-PROJECT PROPAGATION PHASE 1 (per Fires 76+ + 113)
  Duration: 8-15h per project × 5 projects = 40-75h
  Per /opt → /root → OpenArms → OpenFleet → AICP → devops-control-plane
  Dependency: M3 complete; tier-3 prerequisite per /opt methodology

M7: SISTER-PROJECT PROPAGATION PHASE 2-N (long-running)
  Cross-project synchronization
  Per Fire 113 Phase 7 sync mechanism
  Duration: ongoing

POST-M7: SUSTAINED-FEEDBACK-LOOP (per Fire 90)
  Operator-empirical findings → body-refinement
  Per Fire 124 empirically-validated pattern
  Duration: ongoing
```

## Total estimate

```
PRE-M1: 18-26h
PHASE-1: 48-74h
M1: variable (operator-paced)
M2: 40-130h (Pareto-priority) OR 300-750h (full body)
M3: 30-day calendar per piece
M4: 32-60h (4 proposals × 8-15h)
M5: 32-60h (4 proposals × 8-15h)
M6: 40-75h
M7+: ongoing

Subtotal Phase 1+M2-Pareto+M4+M5+M6: ~210-425h
Calendar estimate: 3-9 months at 25% operator engagement
                   1-3 months at 75% operator engagement
                   Variable at 0-100% mixed
```

## Critical-path identification

```
Critical-path nodes (sequential dependencies):
  Operator-empirical Q-answers (Q-FIRE-110/128/137) — gate-blocker
    ↓
  PRE-M1 implementation (Tasks #25-29 + Phase 1 design)
    ↓
  PHASE-1 hook implementation (3 layers parallel)
    ↓
  M1 review session (operator-paced)
    ↓
  M2 elevation
    ↓
  M3 30-day period
    ↓
  M4-M5-M6 (parallelizable post-M3)

Earliest-start blockers: operator-empirical Q-answers
Most-effort node: M2 Tier-1 → Tier-2 promotion (40-750h depending on scope)
Longest-duration node: M3 30-day per piece × N pieces = months
```

## Operator-pending decisions (consolidated)

Per all prior fires:
- Q-FIRE-110 Q1: auto-dream definition (BLOCKER)
- Q-FIRE-110 Q2: Epic placement v2.0 vs v2.1
- Q-FIRE-110 Q3: Investigation method
- Q-FIRE-128 Q1 reformulated: auto-dream
- Q-FIRE-137-1: foundational-triplet endorsement
- Q-FIRE-137-2: Phase 1 launch timing (A/B/C)
- Q-FIRE-137-3: parallel vs sequential
- Q-FIRE-117 v5 Options A-E: ready-for-review pivot
- Q-FIRE-122 milestone Options A-E: 120-piece pivot
- HR 16 variant + numbering (Fire 112)
- wiki-schema field (Fire 116)

12+ operator-pending decisions accumulated.

## Closing

v2 roadmap integrates auto-compact priority (PRE-M1) + Phase 1 foundational-triplet + existing M1-M7. Critical-path: operator-empirical Q-answers → PRE-M1 → PHASE-1 → M1 → M2 → M3 → M4-M6.

**Standing by per /loop directive. v2 roadmap forward-anchor established; awaits operator-empirical engagement.**

## Tags

[implementation-roadmap, v2, auto-compact-priority, phase-1-integration, day-arc-2026-05-08, fire-139]
