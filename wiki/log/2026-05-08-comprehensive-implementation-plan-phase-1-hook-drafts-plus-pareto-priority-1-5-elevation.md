---
title: "Comprehensive Implementation Plan — Phase-1 Hook Drafts + Pareto-Priority 1-5 Elevation"
type: note
note_type: completion
domain: log
status: synthesized
confidence: high
created: 2026-05-08
updated: 2026-05-08
sources:
  - id: phase-1-hook-drafts-summary-fire-159
    type: wiki
    file: wiki/log/2026-05-08-phase-1-hook-drafts-complete-5-concrete-implementations-summary-fires-154-158.md
    description: "Sibling (Fire 159)"
  - id: pareto-priority-1-fire-161
    type: wiki
    file: wiki/log/2026-05-08-fire-65-substitution-pattern-lesson-tier-elevation-candidate-pareto-priority-1-of-5.md
    description: "Sibling (Fire 161) — Priority 1"
  - id: pareto-priority-4-5-fire-164
    type: wiki
    file: wiki/log/2026-05-08-fires-93-94-c04-c02-per-instance-tier-elevation-candidates-pareto-priority-4-5-of-5.md
    description: "Sibling (Fire 164) — Priority 4+5"
tags: [comprehensive-plan, phase-1-plus-pareto, day-arc-2026-05-08, fire-165]
---

# Comprehensive Implementation Plan — Phase-1 Hook Drafts + Pareto-Priority 1-5 Elevation

## Summary

Per Fires 154-159 (Phase 1 hook drafts) + Fires 161-164 (Pareto Priority 1-5 elevation specs): comprehensive forward-anchor for tier-2/3/4 transitions. This Fire 165 consolidates plan.

## Combined plan summary

```
PHASE 1 HOOK DRAFTS (Fires 154-158): 5 hooks
  Fire 154 C09 (~80 LOC): 12-20h
  Fire 155 C04 (~70 LOC): 16-24h
  Fire 156 C02 (~90 LOC): 16-24h
  Fire 157 PreCompact (~120 LOC): 4-6h
  Fire 158 PreToolUse-blocker (~100 LOC): 6-8h
  Subtotal: 54-82h

PARETO PRIORITY 1-3 ELEVATIONS (Fires 161-163):
  Fire 65 elevation (Priority 1): 8-15h
  Fire 103 elevation (Priority 2): 30-50h
  Fire 109 elevation (Priority 3): 26-45h
  Subtotal: 64-110h (50-90h with synergy via integrated tools.tier-* suite)

PARETO PRIORITY 4-5 ELEVATIONS (Fire 164):
  Fires 93+94 (Priority 4+5) = SAME AS Phase 1 C04+C02 hooks
  Already counted in Phase 1; no double-counting

COMBINED TOTAL: 104-172h
  WITH SYNERGY: ~95-150h (10-15% savings via integrated tools)
  Calendar at 50% engagement: 5-12 weeks
  Calendar at 75% engagement: 3-7 weeks
```

## Recommended sequenced wiring

```
WEEK 1 (operator-confirmation phase):
  - Resolve 5 BLOCKERS (~30 min)
  - Approve Phase 1 hook drafts review (~30-60 min)
  - Approve Pareto 1-3 elevation specs (~30 min)
  - Bundle HR 16 + wiki-schema field (~15-30 min)
  Total operator-empirical input: ~2-3 hours

WEEK 1-2: Phase 1 Layer 2 + Layer 3 (auto-compact protection)
  - Wire Fire 157 PreCompact handoff hook (4-6h)
  - Wire Fire 158 PreToolUse-blocker (6-8h)
  - Test via manual /compact + observe sentinel cycle
  Subtotal: 10-14h

WEEK 2-3: Phase 1 Foundational Triplet (parallel)
  - Wire Fire 155 C04 hook (16-24h)
  - Wire Fire 156 C02 hook (16-24h)
  - Wire Fire 154 C09 hook (12-20h)
  - Per-hook tuning per real-session evidence
  Subtotal: 44-68h

WEEK 3-5: Pareto Priority 1-3 elevation
  - Author tools.tier-audit module (Fire 103 elevation; 12-20h)
  - Author tools.tier-elevation module (Fire 109 elevation; 8-15h)
  - Author Fire 65 substitution-pattern detection lint extension (8-15h)
  - Wire wiki-schema implementation_tier field (per Fire 116; ~5h)
  - Re-audit body per Fire 103 (Fire 137 M-VERIFY)
  Subtotal: ~33-55h

WEEK 5-7: Verification + 30-day observation
  - Full body audit per Fire 103 + Fire 116 field
  - Composite-compliance recomputation per Fire 114
  - Fire 65 promotion candidate (post-30-day)
  - Documentation updates per /opt promotion methodology
  Subtotal: 8-15h
```

## Total effort + calendar

```
Operator-empirical input: ~2-3h
Implementation effort: 95-150h (with synergy)
Calendar (50% engagement): 5-12 weeks
Calendar (75% engagement): 3-7 weeks
Calendar (full-time): 2-4 weeks
```

## Body-wide impact projection (post-implementation)

```
Pre-implementation:
  Tier-weighted compliance: ~44%
  Cross-cutting catch rate: ~50-60%
  Auto-compact risk: HIGH (no Layer 2/3 wired)
  Substitution detection: NONE
  Tier-audit automation: NONE

Post-implementation (Week 7):
  Tier-weighted compliance: ~80-85% (estimated)
  Cross-cutting catch rate: ~80-90% (3 foundational hooks)
  Auto-compact risk: LOW (Layers 1+2+3 + structural prevention)
  Substitution detection: enforced (lint validation)
  Tier-audit automation: per-piece operational
  
  Body's empirical compliance: structurally elevated to production-grade
```

## Forward-anchored: post-Phase-1+Pareto state

```
Per Fire 137 v2 roadmap M2-M7:
  M1 operator-confirmation: per-piece reviews (variable; rolls)
  M2 Tier-1 → Tier-2 promotion: 50+ pieces × 6-15h = 300-750h forward
  M3 Tier-2 → Tier-3 deployment: 30-day cross-reference per piece
  M4-M5 standardize/modelize-extension applications: 64-120h
  M6 sister-project propagation: 40-75h
  M7 cross-project sync: ongoing
  
Body matures to TIER-3 deployment phase post-M3 (~2-3 months calendar)
```

## Operator-pending action

```
Q-FIRE-165-1: Endorse comprehensive plan?
  Bundle authorization for all 5 hook drafts + 5 Pareto elevations
  Estimated total operator-input: 2-3h coordinated

Q-FIRE-165-2: Implementation cadence preference?
  Sequential vs parallel (per Week 1-7 schedule)

Q-FIRE-165-3: Verification + promotion timing?
  Per Fire 137 M-VERIFY phase
```

## Closing

Comprehensive plan combines 5 Phase 1 hook drafts (Fires 154-158) + 5 Pareto Priority elevation specs (Fires 161-164) into single 95-150h implementation forward-anchor. Calendar 5-12 weeks at 50% engagement. Body-wide tier-weighted compliance projection: ~44% → ~80-85%.

**Standing by per /loop directive. Comprehensive Phase 1 + Pareto plan established for operator-empirical authorization.**

## Tags

[comprehensive-plan, phase-1-plus-pareto, day-arc-2026-05-08, fire-165]
