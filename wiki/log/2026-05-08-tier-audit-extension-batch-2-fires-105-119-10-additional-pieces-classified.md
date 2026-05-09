---
title: "Tier-Audit Extension Batch 2 — Fires 105-119 (10 Additional Pieces Classified)"
type: note
note_type: completion
domain: log
status: synthesized
confidence: high
created: 2026-05-08
updated: 2026-05-08
sources:
  - id: documentation-implementation-asymmetry-pattern-fire-103
    type: wiki
    file: wiki/patterns/01_drafts/documentation-implementation-asymmetry-pattern-4-tier-audit-distinguishes-design-from-enforcement.md
    description: "PRIMARY parent (Fire 103) — 4-tier audit method; this fire extends initial 15-piece audit to next batch"
  - id: composite-compliance-recomputation-fire-114
    type: wiki
    file: wiki/log/2026-05-08-composite-compliance-metric-recomputation-v2-tier-weighted-per-fire-103-audit-method.md
    description: "Sibling (Fire 114) — composite-compliance baseline"
tags: [tier-audit-extension, batch-2, fires-105-119, day-arc-2026-05-08, fire-142]
---

# Tier-Audit Extension Batch 2 — Fires 105-119 (10 Additional Pieces Classified)

## Summary

Per Fire 103: initial 15-piece audit. Per Fire 110 Q4 (body-audit batch ordering): batch-by-piece-cluster recommended. This Fire 142 extends audit to 10 ADDITIONAL pieces (Fires 105-119 era — auto-compact triplet + tier-framework). Total audited: 25 of 140 pieces.

## Tier classification per piece (agent-DRAFT)

```
Fire 105 PreCompact handoff hook impl-spec:    T1 (designed; not wired at /opt)
Fire 106 PreToolUse-blocker impl-spec:          T1 (designed; not wired)
Fire 107 Auto-compact-disable impl-spec:        T1 (designed; not wired)
Fire 108 Auto-compact backlog decomposition:    T1 (designed; not in /opt/wiki/backlog/)
Fire 109 Tier-elevation pathway pattern:        T1 (designed; methodology-only)
Fire 113 Sister-project propagation spec:       T1 (designed; not implemented)
Fire 114 Composite-compliance recomputation:    T2 (computed; auto-recompute pending)
Fire 116 Wiki-schema implementation_tier field: T1 (proposed; not yet in schema)
Fire 118 P5 candidate principle:                T1 (hypothesis; pending promotion)
Fire 119 Foundational-cluster prioritization:   T1 (designed; layers not wired)
```

10 of 10 pieces at Tier 1 (designed-only).

## Distribution at Batch 2 sub-level

```
Tier 1: 9 of 10 (90%)
Tier 2: 1 of 10 (10% — Fire 114 composite-compliance partially-computed)
Tier 3: 0
Tier 4: 0
```

This batch is HEAVILY Tier 1 — confirms post-Fire-100 era is design-substantive (matches body's growth pattern post-compact).

## Cumulative tier-distribution (initial 15 + this batch 10 = 25 audited)

```
Initial 15-piece (Fire 103):
  T1: 8 (~53%)
  T2: 2 (~13%)
  T3: 4 (~27%)
  T4: 1 (~7%)

Batch 2 (this fire — 10 pieces):
  T1: 9 (90%)
  T2: 1 (10%)
  T3: 0
  T4: 0

Combined 25 pieces:
  T1: 17 (68%)
  T2: 3 (12%)
  T3: 4 (16%)
  T4: 1 (4%)
```

Tier 1 percentage rises (53% → 68%) post-batch-2 inclusion. This reflects auto-compact + tier-framework era's design-density.

## Tier-weighted compliance refresh (per Fire 114 method)

```
Per-piece contribution:
  T0: 0% / T1: 25% / T2: 50% / T3: 75% / T4: 100%

25-piece tier-weighted contribution:
  17 T1 × 25 = 425
  3 T2 × 50 = 150
  4 T3 × 75 = 300
  1 T4 × 100 = 100
  Total: 975 of 2500 max = 39%

Compared to:
  Fire 103 initial 15-piece: 58.3%
  Fire 114 estimate: ~58%
  
This batch update: tier-weighted compliance LOWER than initial estimate
                   (39% with 25 pieces vs 58% with 15 pieces)
                   reflects post-Fire-100 era's Tier-1-dominant addition
```

Body-wide tier-weighted compliance estimate (extrapolated to 140 pieces):
- If batch-2 distribution typical: ~35-40%
- If foundational pieces (P1-P4) included: ~45-55%
- If all 4 governing principles (T4-grade) included: rises to baseline

Implication: composite-compliance recomputation (Fire 114) should now estimate ~35-45% body-wide (initial estimate ~58% needs DOWNWARD revision per this batch evidence).

## Path-to-elevation status per batch-2 piece

| Piece | Current | Path to T2 | Path to T3 | Path to T4 |
|---|---|---|---|---|
| 105 PreCompact spec | T1 | impl Python hook | wire settings.json | + post-compact PreToolUse hook (Fire 106) |
| 106 PreToolUse-blocker | T1 | impl Python hook | wire settings.json | sentinel-removal automation |
| 107 Auto-compact-disable | T1 | impl Layer 1A brain rule | impl Layer 1B+1C harness | impl Layer 1D PreCompact-block hook |
| 108 Backlog decomposition | T1 | author Epic backlog page | author Module pages | author Task pages |
| 109 Tier-elevation pathway | T1 | implement audit tool | implement elevation tool | enforcement-on-skip |
| 113 Sister-project propagation | T1 | per-project investigation | per-project adaptation | cross-project sync |
| 114 Compliance recomputation | T2 | auto-recompute tool | per-cycle integration | enforcement-on-decline |
| 116 Wiki-schema field | T1 | edit wiki-schema.yaml | populate per-piece field | lint validation |
| 118 P5 candidate | T1 | promote to 02_synthesized | cross-project evidence | promote to 04_principles |
| 119 Foundational-cluster prio | T1 | implement C04 hook | implement C04+C02 | implement triplet (Fire 137) |

Per Fire 109 5-step elevation: each piece requires 6-26h elevation work.

## Composability with existing fires

| Component | Composability |
|---|---|
| Fire 103 audit method | This fire EXTENDS Fire 103 audit to 25 pieces |
| Fire 114 composite-compliance | Tier-weighted estimate refined per batch |
| Fire 109 tier-elevation pathway | Path per piece to higher tier |
| Fire 137 foundational-triplet | Phase 1 elevation for C04+C02+C09 layers |

## Forward-anchored: remaining body audit

```
Audited: 25 of 140 pieces (18%)
Remaining: 115 pieces
Estimated effort: 3-5h additional batch-audits (10-30 pieces per batch)
Output: full-body tier-distribution + refined composite-compliance baseline
```

## Closing

Batch 2 audit: 9 T1 + 1 T2 of 10 pieces (Fires 105-119 era). Cumulative 25-piece audit shows Tier-1 dominance (68%) post-Fire-100 era. Tier-weighted composite-compliance estimate REVISED DOWNWARD: ~35-45% body-wide (vs Fire 114 initial ~58%).

**Standing by per /loop directive. Audit progressing; 115 pieces remain for full body coverage.**

## Tags

[tier-audit-extension, batch-2, fires-105-119, day-arc-2026-05-08, fire-142]
