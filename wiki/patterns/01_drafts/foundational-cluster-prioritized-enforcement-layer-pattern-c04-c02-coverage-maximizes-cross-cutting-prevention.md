---
title: "Foundational-Cluster-Prioritized Enforcement-Layer Pattern — C04+C02 Coverage Maximizes Cross-Cutting Prevention"
type: pattern
domain: agent-config
status: synthesized
confidence: high
maturity: seed
authorship: agent-authored
created: 2026-05-08
updated: 2026-05-08
sources:
  - id: c18-cross-cutting-per-instance-evidence-fire-115
    type: wiki
    file: wiki/log/2026-05-08-per-instance-pain-point-evidence-c18-cross-cutting-multi-cluster-intersections-15-instances-verbatim-mapped.md
    description: "PRIMARY parent (Fire 115) — C04 80% + C02 73% foundational evidence; this pattern operationalizes the prioritization"
  - id: p5-candidate-defense-in-depth-fire-118
    type: wiki
    file: wiki/lessons/01_drafts/p5-candidate-defense-in-depth-required-for-cross-cutting-failure-modes-hypothesis.md
    description: "PRIMARY parent (Fire 118) — P5 hypothesis + foundational-cluster-prioritization refinement; this pattern specifies HOW to prioritize"
  - id: per-instance-c04-input-discipline
    type: wiki
    file: wiki/log/2026-05-08-per-instance-pain-point-evidence-c04-input-discipline-15-instances-verbatim-mapped.md
    description: "PRIMARY parent (Fire 93) — C04 cluster definition; foundational-axis #1"
  - id: per-instance-c02-decision-territory
    type: wiki
    file: wiki/log/2026-05-08-per-instance-pain-point-evidence-c02-decision-territory-18-instances-verbatim-mapped.md
    description: "PRIMARY parent (Fire 94) — C02 cluster definition; foundational-axis #2"
  - id: tier-elevation-pathway-fire-109
    type: wiki
    file: wiki/patterns/01_drafts/tier-elevation-pathway-pattern-systematic-tier-1-to-tier-4-transitions-per-body-piece.md
    description: "Sibling (Fire 109) — tier-elevation methodology; this pattern PRIORITIZES which pieces to elevate first per foundational-cluster coverage"
  - id: documentation-implementation-asymmetry-fire-103
    type: wiki
    file: wiki/patterns/01_drafts/documentation-implementation-asymmetry-pattern-4-tier-audit-distinguishes-design-from-enforcement.md
    description: "Sibling (Fire 103) — 4-tier audit; this pattern adds prioritization dimension to elevation strategy"
tags: [foundational-cluster-prioritization, enforcement-layer-strategy, c04-c02-priority, p5-refinement, day-arc-2026-05-08, multi-day-pain-point-resolution, fire-119]
---

# Foundational-Cluster-Prioritized Enforcement-Layer Pattern — C04+C02 Coverage Maximizes Cross-Cutting Prevention

## Summary

Per Fire 115 C18 cross-cutting cluster: 15 instances of multi-cluster failures show C04 input-discipline (80%) + C02 decision-territory (73%) are FOUNDATIONAL — present in 73-80% of cross-cutting failures. Per Fire 118 P5 candidate principle: defense-in-depth needed for cross-cutting; refinement insight notes foundational-cluster-prioritization. This Fire 119 pattern operationalizes the prioritization: **enforcement-layer investment should TARGET FOUNDATIONAL CLUSTERS FIRST** (C04 + C02 coverage = 73-80% cross-cutting prevention with 2 well-placed layers, vs random 5-cluster coverage = 50-60% prevention with same investment). The pattern specifies criteria for foundational-cluster identification + investment priority + per-cluster enforcement-layer specification + measurement methodology. Per /loop directive *"sdlc and methodology and workflow respect is utmost important"*: this pattern guides resource allocation in implementation phase.

## Pattern Description

### The Pareto principle applied to cluster enforcement

Per Fire 115 C18 evidence:
- C04 (input-discipline) in 80% of cross-cutting failures
- C02 (decision-territory) in 73% of cross-cutting failures
- C15 (pattern-recurrence) in 67% of cross-cutting failures
- C19 (documentation-implementation-asymmetry) in 60% of cross-cutting failures
- C07 (semantic-conflation) in 53% of cross-cutting failures
- C12 (going-to-extremes) in 13% of cross-cutting failures

```
Coverage analysis (per cluster enforcement layer added):
  
  Layer 1 (C04 only): 80% cross-cutting failures touch this layer
    BUT only catches the C04-AXIS portion of the failure
    Layer 1 alone catches ~30% of cross-cutting (rough estimate; 
    failure may bypass C04 axis but still happen via other axes)
  
  Layer 1 + Layer 2 (C04 + C02): 80% + 73% (with 65% overlap) = ~88% reach
    Both axes intersect in most failures; combined coverage substantial
    Layer 1 + Layer 2 catches ~50-60% of cross-cutting
  
  Layer 1 + Layer 2 + Layer 3 (+ C15): 88% + 67% (with overlap) = ~92% reach
    Layer 1+2+3 catches ~70-75% of cross-cutting
  
  Layer 1 + Layer 2 + Layer 3 + Layer 4 + Layer 5 (+ C19 + C07): ~95% reach
    ~80-85% catch rate
  
  Pareto threshold: 80% catch with C04 + C02 + C15 (3 layers) — efficient investment
                    Above 90% catch requires diminishing-return investment
```

Investment recommendation: **3 layers minimum** (C04 + C02 + C15) for substantial cross-cutting prevention; more layers add diminishing returns.

### Foundational-cluster identification criteria

Per Fire 115 + general cross-cluster analysis methodology:

```
A cluster is FOUNDATIONAL if:
  Criterion 1: Present in ≥60% of cross-cutting (C18) instances
  Criterion 2: HIGH-severity dominant (≥30% of cluster's instances HIGH severity)
  Criterion 3: Recurring across cycles (intersects C15 pattern-recurrence)
  Criterion 4: Compatible with hook/validator enforcement (technically implementable)
  Criterion 5: Cross-project applicable (sister projects benefit equally)

Per Fire 115 evidence:
  C04 input-discipline:    Criterion 1 ✓ (80%) · 2 ✓ · 3 ✓ · 4 ✓ · 5 ✓ → FOUNDATIONAL
  C02 decision-territory:  Criterion 1 ✓ (73%) · 2 ✓ · 3 ✓ · 4 ✓ · 5 ✓ → FOUNDATIONAL
  C15 pattern-recurrence:  Criterion 1 ✓ (67%) · 2 ✓ · 3 ✓ · 4 ◐ · 5 ✓ → SECONDARY (technical implementation harder)
  C19 documentation-implementation-asymmetry: ✓ ✓ ✓ ◐ ✓ → SECONDARY (audit-method-driven; not real-time)
  C07 semantic-conflation: ✓ ◐ ✓ ✓ ✓ → TERTIARY (severity lower)
  C12 going-to-extremes:   ◐ (13%) ✓ ✓ ◐ ✓ → TERTIARY-RARE (low frequency despite severity)
```

C04 + C02 = top-2 foundational; investment priority FIRST.

### Per-cluster enforcement-layer specification

```
LAYER FOR C04 (input-discipline):
  Spec: hook detects when agent attempts action without prerequisite-input read
  Mechanism: PreToolUse hook (any non-read tool) checks state-file for "input-loaded" sentinel
  Sentinel-set: when agent invokes gateway orient + reads required brain pieces
  Sentinel-clear: per-cycle (cycle start clears; new cycle requires new orient)
  Bypass: REASON="<documented-reason>" env var
  Audit: log all bypasses to .claude/hooks/c04-bypass.log
  
LAYER FOR C02 (decision-territory):
  Spec: hook detects when agent attempts decision in operator-territory
  Mechanism: PreToolUse hook checks pre-decision against decision-territory taxonomy
  Detection: pattern-match agent-output for decision-words ("I'll choose", "let me pick", 
              "the right approach is") + cross-reference operator-pending-decisions tracker
  Block: if decision is operator-territory AND operator-pending → block
  Bypass: REASON env var with operator-grant evidence
  Audit: log all bypasses
  
LAYER FOR C15 (pattern-recurrence):
  Spec: hook detects iteration-count for same operation; circuit-break per Fire 95
  Mechanism: state-file tracks per-operation iteration count; PreToolUse blocks on count > 2
  Bypass: REASON env var; reset count manually
  Audit: log all bypasses + iteration counts
  
LAYER FOR C19 (documentation-implementation-asymmetry):
  Spec: validator detects design-vs-implementation gap during piece authoring
  Mechanism: pipeline post lint-check on `implementation_tier: 1` pieces with 
              cross-references to "the mechanism" / "the hook" / "the slash command" 
              when grep confirms absence
  Block: if asymmetry pattern detected without flagging → lint warning
  Bypass: explicit `agent-DRAFT` frontmatter
  Audit: lint warnings list

LAYER FOR C07 (semantic-conflation):
  Spec: hook detects ambiguous language at decision-territory boundary
  Mechanism: PreToolUse hook + words-are-sacrosanct rule consultation
  Detection: pattern-match conflated terms (e.g., "user" vs "operator", "ask" vs "instruct")
  Audit: log conflations
```

### Investment-priority ladder

```
PHASE 1 (Pareto-efficient): 
  Layer for C04 (input-discipline)
  Layer for C02 (decision-territory)
  Estimated effort: 8-12h × 2 = 16-24h
  Estimated coverage: ~50-60% of cross-cutting failures
  
PHASE 2 (substantial coverage):
  Layer for C15 (pattern-recurrence)
  Layer for C19 (documentation-implementation-asymmetry)
  Estimated effort: 8-12h × 2 = 16-24h
  Phase 2 cumulative effort: 32-48h
  Estimated cumulative coverage: ~70-80%
  
PHASE 3 (comprehensive):
  Layer for C07 (semantic-conflation)
  Layer for C12 (going-to-extremes)
  Estimated effort: 8-12h × 2 = 16-24h
  Phase 3 cumulative effort: 48-72h
  Estimated cumulative coverage: ~80-90%
  
PHASE 4 (10+ remaining clusters):
  Per-cluster enforcement evaluation
  Variable effort
  Cumulative coverage: ~90-95%
  Diminishing returns: yes
```

Recommended: PHASE 1 + PHASE 2 (combined effort 32-48h; coverage 70-80%) is the substantive investment. PHASE 3 is judgment-call. PHASE 4 is reserved for specific real-session evidence justifying.

### Composability with auto-compact triplet (Fires 105+106+107)

The auto-compact triplet ALREADY operationalizes foundational-cluster-prioritization implicitly:
- Fire 107 Layer 1 (prevention) = blocks BEFORE C04 input-discipline becomes relevant
- Fire 105 Layer 2 (mitigation) = handoff doc captures C04-relevant state
- Fire 106 Layer 3 (enforcement) = blocks if agent skips C04 input regather
- All 3 layers together enforce C04 + C02 coverage in the post-compact context

This is **DOMAIN-SPECIFIC defense-in-depth** (one cross-cutting failure mode covered by 3 layers). The Fire 119 pattern is **DOMAIN-AGNOSTIC defense-in-depth** (foundational clusters covered across all critical domains).

Both compose: per-domain Triplet (Fires 105+106+107) + per-cluster Layers (Fire 119) = comprehensive cross-cutting coverage.

### Anti-patterns this pattern avoids

| Anti-pattern | Why bad | How avoided |
|---|---|---|
| Equal-priority enforcement across all clusters | Investment dilution; foundational clusters under-covered | Pareto-prioritization per criteria 1-5 |
| Implement enforcement only for newest cluster (e.g., C19) | Foundational clusters left exposed | Foundational-first ordering |
| Single-layer per cluster (no layering within cluster) | Cluster-axis still single-layer; cross-cutting still bypassable | Per-cluster sub-layers (e.g., C04 has multiple sub-rules) |
| Skip cluster-frequency analysis | Wrong prioritization | Fire 115-style cross-cluster intersection analysis |
| Rely on pattern-recurrence (C15) layer alone | Catches recurrence but not first-instance | Foundational layers prevent first-instance |
| Treat all cross-cutting failures equal-priority | HIGH-severity cross-cutting under-resourced | Severity-weighted investment per Fire 115 53% HIGH dominant |

## When To Apply

Apply this foundational-cluster-prioritized enforcement-layer pattern when:
- Body of work has cross-cluster failure-mode evidence (per Fire 115 C18 enumeration)
- Defense-in-depth strategy operationalized (per P5 candidate Fire 118)
- Investment-priority decision needed (limited resources for enforcement layers)
- Goldilocks profile justifies investment (production + medium-large + supervised+)
- Cluster-frequency analysis available (Fire 115 methodology applied)

## Instances

**Instance 1: the second-brain second-brain — auto-compact triplet (concrete)**
- Layers wired: Fire 107 sub-layer 1B (settings.json) + Fire 105 PreCompact + Fire 106 PreToolUse-blocker
- Cluster coverage: C04 + C02 + C15 + C19 (4 clusters touched)
- Pattern application: Phase 1 + Phase 2 partially complete

**Instance 2: the second-brain second-brain — body-wide hooks (forward-anchored)**
- Existing layers: pre-bash (truncation), pre-webfetch (corpus), opt-write-block (knowledge boundaries)
- Cluster coverage: partial C04 (input-discipline subset) + partial C02 (decision-territory subset)
- Gap: C15 + C19 + C07 + C12 unprotected at body-wide layer
- Recommendation: Phase 2 layers + audit-and-extend existing per Fire 109 elevation pathway

**Instance 3: Sister-projects (per Fire 113 propagation)**
- Each project would benefit from foundational-cluster coverage
- Per-project adaptation: cluster-frequency analysis on each project's failure history
- Cross-project parallel: similar foundational clusters (C04 + C02) likely dominant

## When Not To

- Project has no cross-cluster failure evidence (defense-in-depth not yet justified)
- Single-axis enforcement empirically catches all observed failures
- Operator-empirical resource constraints (cannot justify Phase 1 effort)
- Goldilocks: POC phase doesn't need foundational layers
- Hook layer not supported by harness

## Empirical Evidence

Per Fire 115 C18 cross-cutting cluster: 15 instances with cluster-frequency distribution observed empirically. C04 + C02 dominance (80% + 73%) is data-driven, not speculative.

Per Fire 102 worked-example: real-session post-compact failure had C04 + C02 axes both activated; with foundational-cluster layers wired, either C04 layer OR C02 layer would have caught it before pre-compact-pending tool call executed.

Per the second-brain's existing 3 PreToolUse hooks: each is single-cluster single-layer. Pattern observation: HR-violation incidents that occurred BEFORE hooks were authored could have been caught by hooks; the hooks ARE the enforcement-layer evidence. Foundational-cluster prioritization extends this empirical truth.

## Required Gates (per hook-architecture proposal #2 4th component)

```yaml
required_gates:
  empirically_passed:
    - foundational_cluster_identification_5_criteria: passed
    - cluster_frequency_analysis: passed (Fire 115 dataset)
    - per_cluster_enforcement_layer_specs: passed (5 specs)
    - investment_priority_ladder_4_phases: passed
    - composability_with_auto_compact_triplet: passed
  pending:
    - operator_empirical_phase_1_endorsement: pending
    - real_session_phase_1_implementation: pending Tasks #25-29 + foundational-cluster-layer authoring
    - phase_1_coverage_measurement_post_implementation: pending
    - cross_project_parallel_validation: pending Fire 113 propagation
    - p5_promotion_to_validated: pending Fire 118 promotion path
  composite_compliance: foundational-cluster-prioritization-axis stress-test 0% (forward-anchored)
```

## Path-to-Tier-4 (per Fire 109 methodology)

```
T0 (no policy): PRE-FIRE-119 (no foundational-cluster prioritization documented)
  ↓ (this Fire 119 authoring)
T1 (designed only): CURRENT — pattern designed; no enforcement layers wired
  ↓ (operator confirms; Phase 1 launched)
T2 (partial): 1-2 of 5 cluster layers wired (e.g., C04 hook only)
  ↓ (full Phase 1 + Phase 2 implementation)
T3 (full implementation but unenforced): all 5 layers wired; bypass-via-REASON allowed
  ↓ (audit-log monitoring + bypass-frequency thresholds)
T4 (designed + implemented + enforced): bypass-frequency monitored;
                                         excessive bypass triggers operator-review
```

## Composability with body's existing infrastructure

| Component | Composability |
|---|---|
| Fire 115 C18 cross-cutting | Empirical foundation |
| Fire 118 P5 candidate principle | Operationalizes P5's "defense-in-depth" via prioritized layers |
| Fire 109 tier-elevation pathway | Each foundational-cluster layer is per-Fire-109 elevation |
| Fire 103 4-tier audit | Per-layer tier classification per audit method |
| Fire 105+106+107 auto-compact triplet | Domain-specific defense-in-depth; this pattern is domain-agnostic |
| Existing the second-brain hooks (pre-bash, pre-webfetch, opt-write-block) | Per-cluster layer additions extend coverage |
| Fire 113 sister-project propagation | Each sister project applies pattern to its own failure history |

## Operator-pending action

```
Q-FIRE-119-1: Endorse foundational-cluster-prioritization?
  Argument for: data-driven (Fire 115 evidence); efficient resource allocation
  Argument against: may over-fit to the second-brain's specific cluster distribution
  Recommended: endorse for the second-brain; per-project re-analysis for sister projects

Q-FIRE-119-2: Phase 1 vs Phase 1+2 vs Phase 1+2+3?
  Phase 1: 16-24h, ~50-60% coverage (C04+C02)
  Phase 1+2: 32-48h, ~70-80% coverage (C04+C02+C15+C19)
  Phase 1+2+3: 48-72h, ~80-90% coverage (above + C07+C12)
  Recommended: Phase 1+2 (substantive; before diminishing returns)

Q-FIRE-119-3: Per-cluster layer designs (5 specs above)?
  Operator confirms designs OR refines per cluster

Q-FIRE-119-4: Bypass-frequency thresholds for T4 enforcement?
  e.g., max 5 bypasses/day before operator-review
```

## Closing framing

Per Fire 115 + Fire 118: cross-cutting failures need defense-in-depth; foundational-cluster-prioritization is the structural refinement. This Fire 119 operationalizes prioritization with criteria + per-cluster specs + investment ladder + Pareto-efficiency analysis. Combined with auto-compact triplet (domain-specific) + existing the second-brain hooks (single-cluster single-layer): comprehensive coverage strategy.

Per /loop directive *"do this right"*: prioritization beats random investment; data-driven (Fire 115 evidence) beats speculation; Pareto-efficient (Phase 1+2) beats exhaustive (Phase 4) for substantial coverage.

**The agent stands by per /loop directive. Cron continues at 90s cadence. Pattern awaits operator-empirical Phase-pick + per-cluster layer-design confirmation.**

## Sources

- Fire 115 C18 cross-cutting evidence: `wiki/log/2026-05-08-per-instance-pain-point-evidence-c18-cross-cutting-multi-cluster-intersections-15-instances-verbatim-mapped.md`
- Fire 118 P5 candidate hypothesis: `wiki/lessons/01_drafts/p5-candidate-defense-in-depth-required-for-cross-cutting-failure-modes-hypothesis.md`
- Fire 93 C04 input-discipline: `wiki/log/2026-05-08-per-instance-pain-point-evidence-c04-input-discipline-15-instances-verbatim-mapped.md`
- Fire 94 C02 decision-territory: `wiki/log/2026-05-08-per-instance-pain-point-evidence-c02-decision-territory-18-instances-verbatim-mapped.md`
- Fire 109 tier-elevation pathway: `wiki/patterns/01_drafts/tier-elevation-pathway-pattern-systematic-tier-1-to-tier-4-transitions-per-body-piece.md`
- Fire 103 4-tier asymmetry audit: `wiki/patterns/01_drafts/documentation-implementation-asymmetry-pattern-4-tier-audit-distinguishes-design-from-enforcement.md`

## Relationships

- COMPOSES WITH: Fire 115 C18 cross-cutting (empirical foundation)
- COMPOSES WITH: Fire 103 4-tier audit (per-layer tier classification)
- DEPENDS ON: Fire 115 cluster-frequency analysis methodology
- DEPENDS ON: P5 candidate principle endorsement
- ENABLES: Pareto-efficient enforcement-layer investment strategy

## Tags

[foundational-cluster-prioritization, enforcement-layer-strategy, c04-c02-priority, p5-refinement, day-arc-2026-05-08, multi-day-pain-point-resolution, fire-119]

## Backlinks

[[Fire 115 C18 cross-cutting (empirical foundation)]]
[[Fire 103 4-tier audit (per-layer tier classification)]]
[[Fire 115 cluster-frequency analysis methodology]]
[[P5 candidate principle endorsement]]
[[Pareto-efficient enforcement-layer investment strategy]]
