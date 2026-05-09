---
title: "Per-Cluster Recommended Promotion Priority — 15 Clusters Tier-2 Ordering"
type: note
note_type: session
domain: log
status: synthesized
confidence: high
created: 2026-05-08
updated: 2026-05-08
sources:
  - id: traceability-matrix
    type: wiki
    file: wiki/log/2026-05-08-per-cluster-pain-point-traceability-matrix-180-instances-solution-chain.md
    description: "Source — 180 pain-points per cluster with traceability"
  - id: tier-1-promotion-readiness-snapshot
    type: wiki
    file: wiki/log/2026-05-08-tier-1-promotion-readiness-snapshot-64-pieces-7-criterion-self-review.md
    description: "Sibling — per-piece readiness self-assessment"
  - id: operator-review-checklist
    type: wiki
    file: wiki/patterns/01_drafts/operator-review-checklist-pattern-per-piece-decision-framework-for-tier-promotion.md
    description: "Source — 7-criterion checklist; this priority log informs operator-empirical batch ordering"
  - id: m0-current-status-snapshot
    type: wiki
    file: wiki/log/2026-05-08-m0-current-status-snapshot-pre-implementation-state-and-next-action-options.md
    description: "Sibling — M0 state-snapshot; this priority log feeds OPTION B selective batch decisions"
  - id: composability-map
    type: wiki
    file: wiki/patterns/01_drafts/13-gate-pipeline-composability-with-second-brain-5-tier-maturity-and-mcp-tool-layer.md
    description: "Source — composability dependencies inform priority ordering"
tags: [per-cluster-priority, tier-2-ordering, batch-promotion, day-arc-2026-05-08, multi-day-pain-point-resolution]
---

# Per-Cluster Recommended Promotion Priority — 15 Clusters Tier-2 Ordering

## Summary

Per piece #57 operator-review checklist + M0 snapshot (Fire 72) OPTION B (apply selectively): operator may batch-promote subsets. This log recommends tier-2 promotion priority order based on three weighted factors: (1) pain-point density (more instances = higher priority), (2) structural-leverage (axes that downstream pieces depend on = higher priority), (3) composability dependencies (pieces that supply taxonomies for other pieces = higher priority). Per substitution-pattern Insight 5b: priority recommendations alone are partial — operator-empirical confirms or revises per project-context.

## 3-factor priority scoring

For each cluster, compute weighted score:

```
priority_score = pain_point_density * 0.4
               + structural_leverage * 0.4
               + composability_dependency * 0.2

WHERE:
  pain_point_density = (cluster instances / 180) * 100  [normalized]
  structural_leverage = depth of downstream dependence (1-10 scale)
  composability_dependency = how many other pieces depend on this cluster (count)
```

## Per-cluster scoring

| # | Cluster | Pain-points (density) | Structural-leverage (1-10) | Composability dependency | Weighted score | Priority order |
|---|---|---|---|---|---|---|
| C04 input-discipline | 15 | 8 (Insight 5b foundational; CHECK 3 in many gates) | 5 (input-discipline state-file consumed by many) | (15/180)*40 + 8*40 + 5*20 = 3.3 + 320 + 100 = 423 | **1** |
| C02 decision-territory | 18 | 9 (operator-territory respect underpins all gate-decisions) | 4 (RULE 3 boundary depends on C06 authorship) | (18/180)*40 + 9*40 + 4*20 = 4 + 360 + 80 = 444 | **2** |
| C06 authorship | 7 | 7 (supplies taxonomy for C02 RULE 3) | 6 (taxonomy used by C02 + downstream) | (7/180)*40 + 7*40 + 6*20 = 1.6 + 280 + 120 = 402 | **3** |
| C18 stress-testing-as-validation | (cross-cutting) | 10 (promotion-mechanism for ALL 15 clusters) | 15 (all stress-test specs depend on it) | 0 + 400 + 300 = 700 | **4** (cross-cutting) |
| C15 pattern-recurrence | 16 | 7 (cross-cycle aggregator informs many) | 4 (composite-compliance depends on it) | 3.6 + 280 + 80 = 364 | **5** |
| C10 stage-class | 13 | 7 (methodology integrity foundational) | 3 (regression-test composability) | 2.9 + 280 + 60 = 343 | **6** |
| C03 regression-test | 12 | 6 (Hard Rule 14 verified-edit) | 2 (stage-class composability) | 2.7 + 240 + 40 = 283 | **7** |
| C07 semantic-conflation | 14 | 5 (4-detector taxonomy) | 2 (correction-shape composability) | 3.1 + 200 + 40 = 243 | **8** |
| C08 correction-shape | 11 | 6 (one-notch discipline; cited in many corrections) | 2 (pattern-recurrence dependency) | 2.4 + 240 + 40 = 282 | **9** (tied with C03 zone) |
| C13 drift-detection | 9 | 5 (active-task discipline) | 3 (stage-class composability) | 2 + 200 + 60 = 262 | **10** |
| C05 post-compact | 11 | 6 (lifecycle-event recovery) | 3 (input-discipline composability) | 2.4 + 240 + 60 = 302 | **11** (tied) |
| C14 severity | 8 | 5 (T1-T4 tier discipline) | 2 (decision-territory composability) | 1.8 + 200 + 40 = 242 | **12** |
| C12 SB-iteration | 10 | 5 (systemic-fix priority) | 1 (referenced via pattern-recurrence) | 2.2 + 200 + 20 = 222 | **13** |
| C11 task-shape calibration | 8 | 4 (task vs response calibration) | 1 (cross-cutting) | 1.8 + 160 + 20 = 182 | **14** |
| C09 freeze Class 9 | 9 | 4 (Class 9 taxonomy extension) | 1 (cited via correction-shape) | 2 + 160 + 20 = 182 | **15** (tied) |

**Score interpretation**:
- ≥400: HIGH priority (substrate)
- 250-399: MEDIUM priority
- <250: LOWER priority (still important, but downstream of substrate)

## Recommended batch-promotion sequence

### BATCH 1 — Substrate first (high priority, scores ≥400)

Pieces in clusters: C18 cross-cutting, C02, C04, C06.

| Order | Cluster | Score | Recommended |
|---|---|---|---|
| 1.1 | C18 stress-testing-as-validation | 700 | YES — promotion-mechanism foundational |
| 1.2 | C02 decision-territory | 444 | YES — operator-territory respect substrate |
| 1.3 | C04 input-discipline | 423 | YES — Insight 5b foundational + CHECK 3 in many gates |
| 1.4 | C06 authorship | 402 | YES — supplies C02 RULE 3 taxonomy |

**Batch 1 size**: 4 clusters × per-cluster pieces (concept + impl-spec + stress-test) ≈ 12-15 pieces.

### BATCH 2 — Major axes (medium priority, scores 300-399)

Pieces in clusters: C10, C05, C03.

| Order | Cluster | Score | Recommended |
|---|---|---|---|
| 2.1 | C10 stage-class | 343 | YES — methodology integrity + paired with standardize proposal #3 |
| 2.2 | C05 post-compact | 302 | YES — lifecycle-event substrate |
| 2.3 | C03 regression-test | 283 | YES — Hard Rule 14 verified-edit |

**Batch 2 size**: 3 clusters × per-cluster pieces ≈ 9-12 pieces.

### BATCH 3 — Calibration axes (medium priority, scores 250-299)

Pieces in clusters: C08, C13, C15.

| Order | Cluster | Score | Recommended |
|---|---|---|---|
| 3.1 | C15 pattern-recurrence | 364 | YES — measurement-layer foundational |
| 3.2 | C08 correction-shape | 282 | YES — one-notch discipline |
| 3.3 | C13 drift-detection | 262 | YES — active-task discipline |

**Batch 3 size**: 3 clusters × per-cluster pieces ≈ 9-12 pieces.

### BATCH 4 — Detail axes (lower priority, scores <250)

Pieces in clusters: C07, C14, C12, C11, C09.

| Order | Cluster | Score | Recommended |
|---|---|---|---|
| 4.1 | C07 semantic-conflation | 243 | YES — 4-detector taxonomy |
| 4.2 | C14 severity | 242 | YES — T1-T4 tier discipline |
| 4.3 | C12 SB-iteration | 222 | YES — systemic-fix priority |
| 4.4 | C11 task-shape calibration | 182 | YES — task vs response calibration |
| 4.5 | C09 freeze Class 9 | 182 | YES — Class 9 taxonomy extension |

**Batch 4 size**: 5 clusters × per-cluster pieces ≈ 5-15 pieces (some cross-cutting).

### BATCH 5 — Cross-cutting integration (operator's strategic priority)

Pieces NOT in cluster framework but in Phase 10 cross-cutting:
- 13-gate central pattern (already implicit in Batch 1-4)
- composability map
- sister-project propagation pattern
- operator-review checklist
- implementation-roadmap
- per-axis cross-reference validation matrix
- MCP-tool-catalog adoption pattern
- per-cluster traceability matrix
- state-file ecosystem map
- bypass-discipline operationalization
- cron-loop-management pattern
- multi-project ecosystem index pattern
- canonical-spine update preview
- /root standardize-application preview
- M0 current-status snapshot
- THIS LOG (per-cluster priority)

**Batch 5 size**: ~16-18 pieces.

### BATCH 6 — Modelize + Standardize proposals (operator-territory)

| Order | Type | Recommendation |
|---|---|---|
| 6.1 | Modelize #1 (skills-commands-hooks) | YES if Batch 1-2 promoted |
| 6.2 | Modelize #2 (quality-failure-prevention) | YES if Batch 1-3 promoted |
| 6.3 | Modelize #3 (claude-code) | YES if Batch 1-4 promoted |
| 6.4 | Modelize #4 (super-model) | YES if all prior promoted |
| 6.5 | Standardize #1 (operating-principles 16th) | OPERATOR-TERRITORY — discrete decision |
| 6.6 | Standardize #2 (hook-architecture 4th component) | OPERATOR-TERRITORY |
| 6.7 | Standardize #3 (methodology stage-class) | OPERATOR-TERRITORY (paired with C10) |
| 6.8 | Standardize #4 (context-engineering gate-mode tiers) | OPERATOR-TERRITORY |

**Batch 6 size**: 8 pieces (4 modelize + 4 standardize). Operator-territory standardize proposals deserve careful per-piece review.

## Total promotion sequence (6 batches)

```
BATCH 1 (substrate):           ~12-15 pieces
BATCH 2 (major axes):          ~9-12 pieces
BATCH 3 (calibration):         ~9-12 pieces
BATCH 4 (detail):              ~5-15 pieces
BATCH 5 (cross-cutting):       ~16-18 pieces
BATCH 6 (modelize+standardize): ~8 pieces
                              ─────────────
                              ~59-80 pieces total
```

**Result: roughly matches operator's stated "70-80 pieces" expectation. Substrate-first batching maintains coherence.**

## Operator-empirical override conditions

This priority recommendation is AGENT-AUTHORED self-assessment per piece C06. Operator-empirical may override:

| Override scenario | Action |
|---|---|
| Operator wants different priority order | Apply operator's order; this log informs but doesn't bind |
| Operator wants single-batch wholesale apply | OPTION A from M0 snapshot; bypass batches |
| Operator wants per-piece (not batch) | OPTION B per-piece; this log indicates score-derived order |
| Operator pins specific clusters at tier-1 | Per-cluster operator-decision; remove from batches |
| Operator wants batch-size differently sized | Adjust batch boundaries per operator-empirical chunking preference |

## Composability dependency graph (informs ordering)

```
                 C18 stress-testing (700)
                          │
           ┌──────────────┼──────────────┐
           ▼              ▼              ▼
      C02 territory  C04 input    C06 authorship
       (444)          (423)         (402)
           │              │              │
           ▼              ▼              ▼
       C13 drift    C05 post-compact  C02 RULE 3 supply
        (262)        (302)              │
                                         ▼
       C10 stage    C03 regression  C07 conflation
        (343)        (283)           (243)
                                         │
       C15 pattern  C08 correction       │
        (364)        (282)               │
                                         ▼
       C14 severity C12 SB-iter      Mode C09 / C11
        (242)        (222)              (182)
```

**Reading the graph**: top tier (700) is dependency-free; 423/444/402 depend on top + each other; mid-tier depends on top + 423 zone; lower tier depends on mid + top.

**Substrate-first batching honors this dependency graph**: BATCH 1 = top tier; BATCH 2-3 = mid; BATCH 4 = lower; BATCH 5-6 cross-cutting layered atop.

## Sources

- Pain-point traceability matrix: `wiki/log/2026-05-08-per-cluster-pain-point-traceability-matrix-180-instances-solution-chain.md`
- Tier-1 promotion-readiness snapshot: `wiki/log/2026-05-08-tier-1-promotion-readiness-snapshot-64-pieces-7-criterion-self-review.md`
- Operator-review checklist: `wiki/patterns/01_drafts/operator-review-checklist-pattern-per-piece-decision-framework-for-tier-promotion.md`
- M0 current-status snapshot: `wiki/log/2026-05-08-m0-current-status-snapshot-pre-implementation-state-and-next-action-options.md`
- Composability map: `wiki/patterns/01_drafts/13-gate-pipeline-composability-with-second-brain-5-tier-maturity-and-mcp-tool-layer.md`

## Tags

[per-cluster-priority, tier-2-ordering, batch-promotion, day-arc-2026-05-08, multi-day-pain-point-resolution]
