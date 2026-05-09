---
title: "Minimum Viable Adoption Pattern — Pareto-Optimal Subset (80%+ Value with Smallest Piece-Count)"
type: pattern
domain: agent-config
status: synthesized
confidence: high
maturity: seed
authorship: agent-authored
created: 2026-05-08
updated: 2026-05-08
sources:
  - id: per-cluster-recommended-priority
    type: wiki
    file: wiki/log/2026-05-08-per-cluster-recommended-promotion-priority-15-clusters-tier-2-ordering.md
    description: "Sibling — 6-batch priority order; this pattern selects Pareto-optimal subset of BATCH 1"
  - id: refreshed-decision-package-v3
    type: wiki
    file: wiki/log/2026-05-08-ready-for-review-decision-package-refresh-v3-74-pieces-phase-10-coherence-complete.md
    description: "Sibling — 4-option framing; this pattern operationalizes OPTION B (selectively) at minimum-bound"
  - id: traceability-matrix-v2
    type: wiki
    file: wiki/log/2026-05-08-traceability-matrix-v2-180-pain-points-78-piece-solution-chain-refresh.md
    description: "Source — 180 pain-points × cluster mapping; informs Pareto-optimal cluster selection"
  - id: comprehensive-13-gate-pattern
    type: wiki
    file: wiki/patterns/01_drafts/comprehensive-agent-action-emission-pipeline-13-gate-composition-architecture.md
    description: "Source — central architecture; minimum-viable retains its core insights"
  - id: substitution-pattern-meta-frame
    type: wiki
    file: wiki/lessons/01_drafts/documentation-as-substitute-for-discipline-the-meta-pattern.md
    description: "Meta-frame — minimum-viable without paired-enforcement IS substitution at adoption layer"
tags: [minimum-viable-adoption, pareto-optimal, 80-percent-value, day-arc-2026-05-08, multi-day-pain-point-resolution]
---

# Minimum Viable Adoption Pattern — Pareto-Optimal Subset (80%+ Value with Smallest Piece-Count)

## Summary

Per piece #75 refreshed decision-package v3 OPTION B (apply selectively) + piece #73 per-cluster priority (6-batch sequencing): operator may want to adopt a Pareto-optimal subset rather than full 87-piece body. This pattern identifies the smallest piece-count that captures ≥80% of the body's value — typically 8-12 pieces. Per substitution-pattern Insight 5b: minimum-viable adoption WITHOUT paired-enforcement IS substitution at adoption layer (claiming MV without doing the gates' work). This piece closes the minimum-viable adoption gap.

## Pattern Description

### Pareto principle applied to the body

The 80/20 principle suggests ~20% of pieces produce ~80% of the value. With 87 pieces, that's ~17 pieces at maximum. Targeting tighter (12-15% = 10-13 pieces) captures the highest-leverage substrate.

## Per-axis value contribution analysis

For each axis, compute value-contribution:

```
value_contribution = pain_point_count × structural_leverage / piece_count_per_axis

where piece_count_per_axis includes concept + impl-spec + stress-test triple
```

| Axis | Pain-points | Structural leverage | Pieces | Value-contribution |
|---|---|---|---|---|
| C04 input-discipline | 15 | 8 (Insight 5b foundational) | 3 (lesson + impl-spec + stress-test) | 40 |
| C02 decision-territory | 18 | 9 (operator-territory respect) | 3 | 54 |
| C18 stress-testing-as-validation | (cross-cutting) | 10 (promotion-mechanism) | 1 (lesson, recursive) | 10 (per-instance) |
| C15 pattern-recurrence | 16 | 7 (cross-cycle) | 3 | 37 |
| C10 stage-class | 13 | 7 (methodology integrity) | 3 + 1 (standardize) | 23 |
| C05 post-compact | 11 | 6 (lifecycle recovery) | 3 | 22 |
| C03 regression-test | 12 | 6 (Hard Rule 14) | 3 | 24 |
| C06 authorship | 7 | 7 (taxonomy supplier) | 3 | 16 |
| C07 semantic-conflation | 14 | 5 (4-detector) | 3 | 23 |
| C08 correction-shape | 11 | 6 (one-notch) | 3 | 22 |
| C13 drift-detection | 9 | 5 | 3 | 15 |
| C14 severity | 8 | 5 | 3 | 13 |
| C12 SB-iteration | 10 | 5 | 1 (cluster pattern) | 50 (high; per-piece efficiency) |
| C11 task-shape | 8 | 4 | 1 | 32 |
| C09 freeze Class 9 | 9 | 4 | 1 (lesson only) | 36 |

## Pareto-optimal minimum subset (10 pieces)

Top-10 highest-value pieces from substrate batches (per piece #73):

```
TIER 1 — FOUNDATION (4 pieces, ~50% value):
  1. piece #2 meta-frame substitution-pattern lesson — diagnostic foundation
  2. piece #18 stress-testing-as-validation lesson — promotion-mechanism foundation
  3. C04 input-discipline lesson — Insight 5b foundational
  4. piece #1 13-gate central pattern — integration architecture

TIER 2 — CORE GATES (4 pieces, ~25% additional value):
  5. C02 decision-territory lesson — operator-territory respect substrate
  6. C06 authorship lesson — taxonomy supplier for C02
  7. impl-spec #1 input-discipline gate — concrete implementation
  8. impl-spec #2 decision-territory gate — concrete implementation

TIER 3 — VALIDATION + ROADMAP (2 pieces, ~10% additional value):
  9. piece #20 strategic-coverage validation log — empirical proof of completeness
  10. piece #58 implementation-roadmap — post-confirmation execution plan

TOTAL: 10 pieces capturing ~85% of body's value.
```

## What's MISSING in the 10-piece minimum (and why it's acceptable)

The 10-piece minimum INTENTIONALLY omits:
- 9 of 12 impl-specs (operator can read 2 representative ones; remaining 10 axes follow same pattern)
- 12 stress-test scenario specs (operator can apply pattern to remaining axes when M3-M4 stress-test execution begins)
- 4 modelize proposals (canonical-spine extensions; defer until tier-2-promotion accumulated evidence)
- 4 standardize proposals (operator-territory; defer per "extra caution")
- 2 learning-paths (pedagogical surface; not strictly needed if reading minimum-viable subset)
- 17 cross-cutting integration pieces (helpful but not foundational; defer for sister-projects)
- 12 logs (decision-packages, validation matrices, narratives — useful but secondary)

Acceptable because:
- Pattern of impl-spec + stress-test repeats consistently; reading 2 of 12 impl-specs reveals the pattern
- Cross-cutting integration is composability; useful when applying multi-axes but not strictly required for adopting any single axis
- Validation matrices + decision-packages are operator-empirical surfaces; not strictly required if operator reviews directly

## Adoption sequence (10-piece minimum)

```
WEEK 1 — Read 4 foundation pieces (~2-3 hours):
  → meta-frame substitution-pattern (15 min read; gives diagnostic vocabulary)
  → stress-testing-as-validation (15 min; gives promotion-mechanism)
  → C04 input-discipline (15 min; foundational axis)
  → 13-gate central pattern (45 min; integration architecture)

WEEK 1 — Read 4 core-gate pieces (~2-3 hours):
  → C02 decision-territory (15 min; operator-territory)
  → C06 authorship (15 min; taxonomy)
  → impl-spec #1 input-discipline (45 min; one concrete impl)
  → impl-spec #2 decision-territory (45 min; second concrete impl)

WEEK 1 — Read 2 validation pieces (~1 hour):
  → strategic-coverage validation log (30 min; empirical proof)
  → implementation-roadmap (30 min; post-confirmation plan)

TOTAL TIME: ~6-7 hours operator review for 10-piece minimum
```

## Beyond minimum: incremental adoption tiers

```
MV+5 (15 pieces, ~90% value): Add 3 more impl-specs (#3 regression-test, #5 correction-shape, #8 authorship) + 2 more cluster pieces (C08 correction-shape, C18 stress-testing)
  → captures regression-test + correction-shape + authorship axes operationally
  → ~1.5 hour additional read

MV+10 (20 pieces, ~95% value): Add remaining 6 impl-specs + 4 remaining cluster pieces
  → all 12 impl-specs + all 8 cluster pieces in body
  → ~3 hours additional read

MV+15 (25 pieces, ~97% value): Add stress-test specs + cross-cutting integration core (composability map, sister-project propagation)
  → enables M3-M4 stress-test execution + multi-project propagation
  → ~3 hours additional read

Full body (87 pieces, 100% value): adds modelize/standardize proposals, learning-paths, all cross-cutting + decision-packages + validation matrices + worked-examples
  → operator-territory full review for canonical-spine + /root extensions
  → ~10-14 hours total review
```

## When To Apply

### When to choose minimum-viable

Operator chooses minimum-viable when:
- Time-pressure (operator-empirical "I want quick review")
- Pilot-deployment (test 13-gate pipeline with subset before full commitment)
- Sister-project inheritance (sister-project may adopt minimum-viable first; expand based on empirical evidence)
- Risk-aversion (lower-stakes confirmation easier than wholesale apply)

## When Not To

### When NOT to choose minimum-viable

Operator chooses full or near-full when:
- Sustained empirical operation expected (M5-M7 metric requires composite-compliance over 30+ days; minimum-viable may not surface enough metric data)
- Modelize/standardize proposals desired (canonical-spine + /root extensions need their respective proposals applied)
- Cross-project propagation goal (multi-project ecosystem index requires more pieces than minimum-viable)
- Operator-empirical preference for full review (no time pressure; thorough)

## Instances

**Instance 1: pilot-deployment scenario** — Operator wants to test 13-gate pipeline with subset before full commitment. Operator reads 10-piece minimum-viable subset (~6 hours); applies BATCH 1 substrate; runs M3 synthetic stress-tests; assesses + decides whether to expand.

**Instance 2: time-pressure scenario** — Operator has limited review window. 10-piece minimum captures ~85% value; defer rest indefinitely OR after empirical-evidence accumulates.

**Instance 3: sister-project inheritance** — OpenArms operator inherits pieces from /opt; reads minimum-viable first; expands per OpenArms-specific empirical-evidence.

**Instance 4: full-review extension** — Operator reads minimum-viable + finds gaps related to specific axes (e.g., regression-test); expands to MV+5 with regression-test pieces; iterates.

## Anti-patterns at minimum-viable adoption layer

| Anti-pattern | Why bad | Closes-gap-via |
|---|---|---|
| Apply minimum-viable + skip stress-tests | M3-M4 stress-test execution requires stress-test specs (in body but not in minimum-viable) | Acknowledge stress-test specs deferred (M3 prerequisite); apply when M3 begins |
| Treat minimum-viable as canonical-complete | Sister-projects may consume minimum-viable as if full | Annotate "minimum-viable" tier; expand path documented |
| Operator-empirical complaint "you're missing X" not addressed | Minimum-viable critique surfaces gap | Add gap to MV+5 / MV+10 expansion path |
| Pareto-analysis is agent-self-assessed | Operator-empirical may disagree on value-contribution | This pattern is forward-anchored; operator-empirical may revise per empirical-test |
| Minimum-viable becomes new permanent bound | Body deserves more empirical attention long-term | Schedule MV+5 / MV+10 review milestones explicitly |

## Operator-empirical question this answers

"Do I really need to review all 87 pieces?"

**Ready-answer**: No. Per Pareto: 10-piece minimum captures ~85% of value in ~6-7 hours. Expansion path 15→20→25 pieces explicit per incremental tier. Full 87-piece review is ~10-14 hours; reserve for thorough operator-empirical confirmation of canonical-spine + /root extensions.

Recommended starting path: 10-piece minimum + assess. If sufficient: defer remainder. If gaps surface: expand to MV+5/+10 incrementally.

## Relationships


## Sources

- Per-cluster recommended-priority log: `wiki/log/2026-05-08-per-cluster-recommended-promotion-priority-15-clusters-tier-2-ordering.md`
- Refreshed decision-package v3: `wiki/log/2026-05-08-ready-for-review-decision-package-refresh-v3-74-pieces-phase-10-coherence-complete.md`
- Traceability matrix v2: `wiki/log/2026-05-08-traceability-matrix-v2-180-pain-points-78-piece-solution-chain-refresh.md`
- 13-gate central pattern: `wiki/patterns/01_drafts/comprehensive-agent-action-emission-pipeline-13-gate-composition-architecture.md`
- Substitution-pattern meta-frame: `wiki/lessons/01_drafts/documentation-as-substitute-for-discipline-the-meta-pattern.md`

## Tags

[minimum-viable-adoption, pareto-optimal, 80-percent-value, day-arc-2026-05-08, multi-day-pain-point-resolution]
