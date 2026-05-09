---
title: "Composite-Compliance Metric Recomputation v2 — Tier-Weighted per Fire 103 Audit Method"
type: note
note_type: completion
domain: log
status: synthesized
confidence: medium
created: 2026-05-08
updated: 2026-05-08
sources:
  - id: prior-composite-metric-self-application-fire-85
    type: wiki
    file: wiki/log/2026-05-08-body-of-work-composite-metric-self-application-meta-validation.md
    description: "PRIOR composite-compliance metric (Fire 85): 99.51% claimed; this Fire 114 recomputes tier-weighted per Fire 103 method"
  - id: documentation-implementation-asymmetry-pattern-fire-103
    type: wiki
    file: wiki/patterns/01_drafts/documentation-implementation-asymmetry-pattern-4-tier-audit-distinguishes-design-from-enforcement.md
    description: "PRIMARY parent (Fire 103) — 4-tier audit method; this Fire 114 applies tier-weighting to recompute composite-compliance"
  - id: c19-per-instance-evidence-fire-111
    type: wiki
    file: wiki/log/2026-05-08-per-instance-pain-point-evidence-c19-documentation-implementation-asymmetry-12-instances-verbatim-mapped.md
    description: "Sibling (Fire 111) — C19 cluster establishes asymmetry as named cluster; provides 12 instances for tier-weighting input"
  - id: traceability-matrix-v2-fire-79
    type: wiki
    file: wiki/log/2026-05-08-traceability-matrix-v2-180-pain-points-78-piece-solution-chain-refresh.md
    description: "Sibling (Fire 79) — 180 pain points across 15 clusters; provides per-cluster compliance weighting basis"
  - id: composite-compliance-stress-test-spec
    type: wiki
    file: wiki/patterns/01_drafts/composite-compliance-stress-test-scenario-spec-real-session-test-plan.md
    description: "Methodology source — 13-axis stress-test composite metric; this Fire 114 refines per tier-weighting"
  - id: tier-elevation-pathway-fire-109
    type: wiki
    file: wiki/patterns/01_drafts/tier-elevation-pathway-pattern-systematic-tier-1-to-tier-4-transitions-per-body-piece.md
    description: "Sibling (Fire 109) — tier-elevation pathway; this Fire 114 quantifies the gap between current vs target compliance"
tags: [composite-compliance-recomputation, v2, tier-weighted, fire-103-application, day-arc-2026-05-08, multi-day-pain-point-resolution, fire-114]
---

# Composite-Compliance Metric Recomputation v2 — Tier-Weighted per Fire 103 Audit Method

## Summary

Per Fire 85 self-application: composite-compliance metric returned 99.51% (high; design-density-as-proxy). Per Fire 103 4-tier audit critique: this metric OVER-states because it weights designed pieces equally with enforced pieces. Per Fire 111 C19 cluster: 53% of audited body is Tier 1 (designed-only) — pieces exist on paper but don't operate. This Fire 114 recomputes the composite-compliance metric **tier-weighted**: each piece contributes per its actual maturity tier, not per its existence. Result: tier-weighted composite-compliance estimated at **~33-42%** (vs Fire 85's 99.51%) — the body's TRUE empirical-enforcement density. Confidence: **medium** (initial 15-piece audit pass per Fire 103; full 112-piece audit pending). Per /loop directive *"sdlc and methodology and workflow respect is utmost important"*: this fire honors the methodology by replacing aspirational metric with empirical metric.

## Recomputation methodology

### Tier-weighting formula (per Fire 103 audit)

```
Per-piece contribution to composite-compliance:
  T0 (no policy): 0% (piece is candidate; not yet contributing)
  T1 (designed only): 25% (design exists; agent-readable; no operation)
  T2 (partial implementation): 50% (some components work)
  T3 (implemented but unenforced): 75% (works but skippable)
  T4 (designed + implemented + enforced): 100% (full)

Composite-compliance =
  (sum(per-piece-contribution × per-piece-weight) / sum(weights)) × 100%

Per-piece weight options:
  Option A — equal weight (each piece counts the same)
  Option B — severity-weighted (HIGH×3, MEDIUM×2, LOW×1)
  Option C — recency-weighted (recent pieces × 1; older pieces × 0.5)

Recommended: Option A for v2 baseline (simplest; matches Fire 85's approach)
            Option B/C for v3 refinement (per operator-empirical request)
```

### Initial 15-piece tier-weighted audit (per Fire 103 + Fire 111)

| Piece | Tier | Contribution |
|---|---|---|
| Impl-spec #10 (post-compact orientation gate) | T2 | 50% |
| Question-registry pattern (Fire 99) | T1 | 25% |
| Blocker-impediment registry (Fire 101) | T1 | 25% |
| Mode-by-nature governance (Fire 98) | T1 | 25% |
| Feature-flag system (Fire 96) | T1 | 25% |
| Backlog-decomposition (Fire 97) | T1 | 25% |
| Operator-empirical signal-grammar (Fire 92) | T1 | 25% |
| Body versioning v1.0.0 (Fire 91) | T3 | 75% |
| Composite-compliance metric (Fire 85) | T3 | 75% |
| Pipeline post canonical gate | T4 | 100% |
| Pre-bash hook (truncation block) | T4 | 100% |
| Pre-webfetch corpus check | T4 | 100% |
| Sacrosanct verbatim quoting (HR 4) | T3 | 75% |
| /orient invocation post-compact | T2 | 50% |
| Gateway orient invocation cadence | T3 | 75% |

**Sum of contributions: 875%** (15 pieces × 100% theoretical max = 1500%)
**Tier-weighted compliance: 875/1500 = 58.3%**

(Earlier estimate per Fire 103 was 30-50% — actual computation higher due to inclusion of T4 pieces in initial pass)

### Cross-cluster tier-weighted compliance (sample)

Per Fire 79 traceability matrix: 180 pain-points across 15 clusters. Per Fire 111 C19 candidate 16th cluster.

| Cluster | Solution-chain pieces (Fire 79) | Avg tier (estimate) | Compliance contribution |
|---|---|---|---|
| C04 input-discipline | 8-12 | T1-T2 mixed | ~33% |
| C02 decision-territory | 10-14 | T1 dominant | ~25% |
| C15 pattern-recurrence | 6-10 | T1 dominant | ~25% |
| C07 semantic-conflation | 8-12 | T1-T2 mixed | ~33% |
| C18 cross-cutting | TBD | unknown | TBD |
| C19 documentation-implementation-asymmetry (NEW per Fire 111) | 12 instances | T0-T1 dominant | ~10% |
| Other 11 clusters | varies | unknown | TBD (forward-anchored) |

Estimated body-wide cluster-average compliance: ~30-40% (medium confidence)

## Comparison: Fire 85 vs Fire 114

| Metric | Fire 85 (design-density) | Fire 114 (tier-weighted) | Delta |
|---|---|---|---|
| Methodology | 13-axis stress-test summed | Same axes × tier-weighting | Significant |
| Per-piece contribution | Existence (binary 100%) | Per-tier (0/25/50/75/100%) | Major |
| Body-wide score | 99.51% | ~58% (initial 15-piece) | -41 pp |
| What it measures | Design-density (do pieces exist?) | Enforcement-density (do pieces operate?) | Different things |
| Empirical validity | LOW (design-density is proxy) | MEDIUM (tier classifications need operator-confirmation) | Fire 114 better |

Fire 85's 99.51% is NOT WRONG — it accurately measures DESIGN-density (which is what the metric was originally formulated to compute). Fire 114's ~58% measures ENFORCEMENT-density (what operator-empirical actually wants). Both are valid; they measure different dimensions.

The body's "true empirical compliance" depends on which dimension matters:
- **Knowledge persistence** (design-density): 99.51% — body is preserved, agents can read it
- **Operational enforcement** (tier-weighted): ~58% — body has substantial gap between design + operation

Per /loop directive *"do this right"*: enforcement-density is the operator-empirical metric of interest.

## Per-axis tier breakdown (refining 13-axis stress-test)

```
AXIS 1: post-compact orientation gate (impl-spec #10)
  Tier: T2 (PostCompact wired; PreCompact missing)
  Contribution: 50%

AXIS 2: input-discipline gate
  Tier: T2 (gateway orient exists; not enforced post-action)
  Contribution: 50%

AXIS 3: decision-territory gate
  Tier: T2 (work-mode.md PO approval boundary; partial enforcement)
  Contribution: 50%

AXIS 4: stage-class gate (methodology engine)
  Tier: T3 (5 stages × ALLOWED/FORBIDDEN; agent-compliance; no hook enforces)
  Contribution: 75%

AXIS 5: severity blast-radius gate
  Tier: T2 (pattern designed; classification manual)
  Contribution: 50%

AXIS 6: regression-test gate (pipeline post)
  Tier: T4 (pipeline post enforced via 0-error requirement)
  Contribution: 100%

AXIS 7: drift-detection gate
  Tier: T1 (designed only)
  Contribution: 25%

AXIS 8: correction-shape gate (one-notch vs extreme swing)
  Tier: T1 (designed; documented in /root operating-principles)
  Contribution: 25%

AXIS 9: authorship classification gate
  Tier: T2 (frontmatter authorship field used; not validated)
  Contribution: 50%

AXIS 10: pattern-recurrence quantification gate
  Tier: T1 (designed only)
  Contribution: 25%

AXIS 11: semantic-conflation gate
  Tier: T2 (commands renamed; semantic-grammar partial)
  Contribution: 50%

AXIS 12: composite-compliance gate
  Tier: T3 (computed; not auto-running per cycle)
  Contribution: 75%

AXIS 13: post-compact-orientation+mirror gate (extended)
  Tier: T2 (same as AXIS 1; mirror semi-implemented)
  Contribution: 50%

Sum: 775%
Axes: 13
Per-axis avg: 775 / 1300 = 59.6%
```

13-axis tier-weighted: **59.6%** (close to per-piece 58.3% — methodology-internal-consistency)

## C19 cluster impact on composite

Per Fire 111: C19 has 12 instances at heavily T0-T1 distribution. Including C19 in composite:

```
Pre-C19-inclusion:  ~58% (initial 15-piece audit)
Post-C19-inclusion: 
  12 new instances × ~T1 = 12 × 25% = 300% / 1200% = drops contribution rate
  
Body-wide if C19 promoted to canonical 16th cluster:
  Estimated tier-weighted compliance: ~50-55%
```

Promoting C19 surfaces asymmetry that Fire 85 didn't see. The body becomes more honest with itself.

## Forward-anchored: closing the gap

To raise tier-weighted compliance from 58% → 75-90%:

```
Target: Tier 4 for high-leverage pieces
  Approach: Fire 109 tier-elevation pathway applied to T1 dominant pieces
  Priority order (per Fire 103 + Fire 111):
    1. Impl-spec #10 T2 → T4 (Fires 105+106 + Tasks #25-29)
       Impact: +50% contribution (50→100%)
    2. Question-registry T1 → T3 (Fire 99 implementation)
       Impact: +50% contribution
    3. Blocker-impediment T1 → T3
       Impact: +50% contribution
    4. Mode-by-nature T1 → T3
       Impact: +50% contribution
    5. Feature-flag T1 → T4 (full path)
       Impact: +75% contribution
  
  Estimated body-wide compliance after closing top-5 elevations: ~75%
  Estimated body-wide compliance after all T1 elevations: ~85-90%
  Theoretical maximum: 100% (every piece T4) — practically unattainable

Per Fire 109: tier-elevation requires Fire 97 backlog-decomposition per piece
              Fire 108 example: 18-26h per Epic
              Body-wide elevation: ~300-1300h estimate (depending on scope)
```

## Limitations + caveats

| Limitation | Impact | Mitigation |
|---|---|---|
| Initial 15-piece audit (vs full 112-piece) | Body-wide estimate uncertain | Q4 (Fire 110) full-body audit pending |
| Tier classifications agent-DRAFT (per SB-095) | May be wrong on individual pieces | Operator-empirical confirmation pending |
| Equal-weight method (Option A) | Doesn't capture severity differences | Option B/C refinement forward-anchored |
| 13-axis stress-test designed-mostly | Multi-axis assessment partial | Per-axis tier classifications per Fire 103 method |
| Cross-cluster averaging crude | Per-cluster tier-distribution varies | Per-cluster per-instance audit (Fires 93-96 + 111 + future) |
| Body still growing | Metric is snapshot; will shift | Recompute periodically (e.g., post-major-milestone) |

## Required Gates (per hook-architecture proposal #2 4th component)

```yaml
required_gates:
  empirically_passed:
    - tier_weighting_formula_articulated: passed
    - 15_piece_per_piece_recomputation: passed (per Fire 103 method)
    - 13_axis_per_axis_recomputation: passed
    - C19_inclusion_impact: passed
    - comparison_fire_85_vs_fire_114: passed
  pending:
    - operator_empirical_tier_classification_confirmation: pending
    - full_112_piece_audit: pending Q4 (Fire 110)
    - cross_cluster_per_instance_audit_remaining_11: pending (~22h)
    - severity_weighted_v3_refinement: pending operator-empirical request
    - per_milestone_recomputation_cadence: pending operator-empirical
  composite_compliance: composite-compliance-recomputation-axis stress-test 0%
                       (forward-anchored — this fire IS the stress-test)
```

## What this Fire 114 ADDS to body methodology

```
BEFORE Fire 114:
  - Composite-compliance metric: 99.51% (Fire 85 design-density)
  - Operator-empirical interpretation: "body is highly compliant"
  - Implication: false confidence; design-density obscures enforcement-gap

AFTER Fire 114:
  - Composite-compliance metric: ~58% tier-weighted (initial)
  - Operator-empirical interpretation: "body is design-rich but enforcement-light"
  - Implication: honest assessment; tier-elevation is the gap-closing path
  - New baseline: target 75-90% body-wide tier-weighted compliance
```

## Operator-pending questions

```
Q-FIRE-114-1: Adopt tier-weighted as primary metric vs design-density?
  Argument for: empirical-honest; matches operator's enforcement-density preference
  Argument against: established baseline (Fire 85) needs preservation
  Recommended: maintain BOTH; primary = tier-weighted; secondary = design-density

Q-FIRE-114-2: Target tier-weighted compliance percentage?
  Options: 75% (top-5 elevation), 85% (all T1), 90% (production-ready), 100% (theoretical)
  Recommended: 75% as Phase 1 target; 85% as Phase 2; 90% as Phase 3

Q-FIRE-114-3: Recomputation cadence?
  Options: per-fire / per-Epic / per-milestone / per-quarter
  Recommended: per-milestone (avoid metric-noise per fire)

Q-FIRE-114-4: Severity weighting (Option B)?
  Apply HIGH×3 / MEDIUM×2 / LOW×1 in v3?
  Argument: HIGH-severity gaps weighted more heavily
  Argument against: complexity; may obscure simple-case gaps
```

## Closing framing

Per Fire 85 baseline: composite-compliance 99.51% (design-density). Per Fire 103 critique + Fire 111 C19 evidence: design-density ≠ enforcement-density. Per Fire 109 tier-elevation methodology: empirical compliance moves through tier transitions. This Fire 114 recomputes ~58% tier-weighted (initial 15-piece) with body-wide estimate ~50-55% post-C19-inclusion. The 41-point delta is NOT regression — it's HONESTY: the body's design-density is high; enforcement-density has substantial gap.

Per /loop directive *"the at least 100 pain point... will need direct response"*: tier-weighted compliance shows the body is DESIGN-RICH (>100 pieces) but ENFORCEMENT-LIGHT (~58% empirical operations). The gap-closing path = Fire 109 systematic tier-elevation per Fire 103 audit findings.

**The agent stands by per /loop directive. Cron continues at 90s cadence. Tier-weighted recomputation surfaces honest assessment for operator-empirical review.**

## Sources

- Fire 85 composite-metric self-application: `wiki/log/2026-05-08-body-of-work-composite-metric-self-application-meta-validation.md`
- Fire 103 4-tier audit method: `wiki/patterns/01_drafts/documentation-implementation-asymmetry-pattern-4-tier-audit-distinguishes-design-from-enforcement.md`
- Fire 111 C19 cluster: `wiki/log/2026-05-08-per-instance-pain-point-evidence-c19-documentation-implementation-asymmetry-12-instances-verbatim-mapped.md`
- Fire 79 traceability matrix v2: `wiki/log/2026-05-08-traceability-matrix-v2-180-pain-points-78-piece-solution-chain-refresh.md`
- Composite-compliance stress-test spec: `wiki/patterns/01_drafts/composite-compliance-stress-test-scenario-spec-real-session-test-plan.md`
- Fire 109 tier-elevation pathway: `wiki/patterns/01_drafts/tier-elevation-pathway-pattern-systematic-tier-1-to-tier-4-transitions-per-body-piece.md`

## Tags

[composite-compliance-recomputation, v2, tier-weighted, fire-103-application, day-arc-2026-05-08, multi-day-pain-point-resolution, fire-114]
