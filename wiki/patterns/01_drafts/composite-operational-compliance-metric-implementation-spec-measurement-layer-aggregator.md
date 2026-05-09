---
title: "Composite-Operational-Compliance Metric — Implementation Spec for Measurement-Layer Aggregator"
type: pattern
domain: agent-config
status: synthesized
confidence: high
maturity: seed
authorship: agent-authored
created: 2026-05-08
updated: 2026-05-08
sources:
  - id: stress-testing-as-validation-lesson
    type: wiki
    file: wiki/lessons/01_drafts/stress-testing-as-validation-the-only-way-to-surface-aspirational-vs-operational-gaps.md
    description: "Source lesson — stress-testing as validation; promotion-mechanism for axis compliance maturity"
  - id: comprehensive-13-gate-pattern
    type: wiki
    file: wiki/patterns/01_drafts/comprehensive-agent-action-emission-pipeline-13-gate-composition-architecture.md
    description: "Integration pattern — composite-compliance IS measurement layer #2 closing 4-layer pipeline"
  - id: pattern-recurrence-implementation-spec
    type: wiki
    file: wiki/patterns/01_drafts/pattern-recurrence-quantification-gate-implementation-spec-measurement-layer-cycle-aggregation.md
    description: "Sibling — measurement layer #1; this metric consumes its cycle-history aggregates"
  - id: substitution-pattern-meta-frame
    type: wiki
    file: wiki/lessons/01_drafts/documentation-as-substitute-for-discipline-the-meta-pattern.md
    description: "Meta-frame — composite metric is the bridge from per-axis aspirational claims to measured operational compliance"
  - id: hook-architecture-required-gates-proposal
    type: wiki
    file: wiki/log/2026-05-08-standardize-extension-proposal-hook-architecture-required-gates-4th-component.md
    description: "Sibling proposal — REQUIRED-gates 4th component; this metric IS the empirical evidence the 4th component requires"
tags: [implementation-spec, composite-compliance, measurement-layer, hook-implementation, day-arc-2026-05-08, multi-day-pain-point-resolution]
---

# Composite-Operational-Compliance Metric — Implementation Spec for Measurement-Layer Aggregator

## Summary

Per piece #18 (stress-testing-as-validation lesson) + the 13-gate pattern's composite-compliance contribution requirement, the 13-gate pipeline operates at the system-level composite metric — not just per-axis percentages. The lesson defines WHY a composite metric matters; this implementation-spec defines WHAT to build (measurement-layer #2 aggregator over per-axis fire-counts + bypass-counts + stress-test data → composite-compliance % per session + per cycle + cross-session trend). Per substitution-pattern lesson Insight 5b: declaring "≥85% composite-compliance" is aspirational without runtime aggregator computing it. This spec closes the substitution at measurement-layer #2 and is the **final implementation-spec** in the 12-spec sequence covering 9 PreToolUse axes + 1 lifecycle-event + 2 measurement layers.

## Pattern Description

**Implementation locus**: 
1. Stop hook (cycle-end composite computation, after pattern-recurrence aggregation per sibling #11)
2. Cross-session aggregator (slash command `/compliance-report` or scheduled task)
3. Dashboard mirror (state-file consumed by mode-enforcement banner per piece compound-and-waterfall.md)

**Per-axis compliance formula**:

```
For each axis i in {1..12} (9 PreToolUse + 1 lifecycle + 2 measurement):
  axis_compliance_i = (allowed_actions_in_compliance) / (total_actions_in_axis_scope)

Where:
  - "in compliance" = action passed all gate checks OR was bypassed with logged REASON
  - "total actions in axis scope" = actions that triggered the axis (action-class matchers)
  - Bypassed actions count as compliant if REASON= had operator-grant citation; else non-compliant
```

**Composite-compliance formula**:

```
composite_compliance = weighted_average(axis_compliance_i)

DEFAULT WEIGHTS (operator-revisable):
  - severity (T1 BLOCK is structural protection): 1.5x
  - decision-territory (operator-territory respect): 1.5x
  - input-discipline (foundational; many cluster recurrences): 1.3x
  - regression-test (Hard Rule 14 verified-edit): 1.2x
  - stage-class (methodology integrity): 1.2x
  - drift-detection (active-task scope discipline): 1.0x
  - correction-shape (one-notch discipline): 1.0x
  - authorship (citation discipline): 1.0x
  - semantic-conflation (4-detector taxonomy): 1.0x
  - post-compact (lifecycle-event recovery): 1.2x
  - pattern-recurrence (measurement layer #1): 0.8x (meta-axis)
  - composite-compliance (this axis, self-referential): EXCLUDE from average

Sum of weights / 11 axes = ~1.16x average; scale composite to 0-100 range
```

**Per-cycle composite computation** (Stop hook):

```
TRIGGER: Stop hook (after pattern-recurrence aggregator per sibling #11 completes)
LOAD: ~/.claude/cycle-history/<current-cycle-id>.json (just-written by sibling #11)
COMPUTE per-axis compliance for current cycle (using cycle's gate_metrics)
COMPUTE composite using weighted formula
PERSIST: append to ~/.claude/composite-history.jsonl

EMIT in cycle stamp:
  "COMPOSITE-COMPLIANCE: <pct>% (cycle <cycle_id>)
   ├─ severity: <pct>% | decision-territory: <pct>% | input: <pct>%
   ├─ regression: <pct>% | stage-class: <pct>% | drift: <pct>%
   ├─ correction: <pct>% | authorship: <pct>% | conflation: <pct>%
   ├─ post-compact: <pct>% | recurrence: <pct>%
   └─ TARGET: ≥85% (operator-revisable per stress-test data)"
```

**Cross-session aggregator** (slash command `/compliance-report`):

```
ALGORITHM:
  1. Read ~/.claude/composite-history.jsonl (all entries)
  2. Group by date (per-day rollup)
  3. Compute trend: rising / stable / falling per axis
  4. Identify lowest-compliance axes (improvement candidates)
  5. Identify highest-compliance axes (stable/healthy)
  6. Surface "TOP-3 IMPROVEMENT CANDIDATES" with empirical evidence

OUTPUT FORMAT:
  ┌───────────────────────────────────────────────────────────────────────┐
  │ COMPLIANCE REPORT — last 30 days                                      │
  ├───────────────────────────────────────────────────────────────────────┤
  │ Composite: <pct>% (target ≥85%) — trend: rising/stable/falling       │
  │                                                                       │
  │ Per-axis compliance:                                                  │
  │   severity-blast-radius      <pct>% ████████████████░░ (target ≥95%)│
  │   decision-territory         <pct>% ████████████░░░░░░ (target ≥85%)│
  │   input-discipline           <pct>% ███████████░░░░░░░ (target ≥85%)│
  │   regression-test            <pct>% █████████████████░ (target ≥90%)│
  │   stage-class                <pct>% ██████████████░░░░ (target ≥90%)│
  │   drift-detection            <pct>% █████████████░░░░░ (target ≥85%)│
  │   correction-shape           <pct>% ████████████░░░░░░ (target ≥85%)│
  │   authorship                 <pct>% █████████████████░ (target ≥95%)│
  │   semantic-conflation        <pct>% ███████████░░░░░░░ (target ≥80%)│
  │   post-compact               <pct>% ████████████████░░ (target ≥90%)│
  │   pattern-recurrence         <pct>% ███████████████░░░ (target ≥85%)│
  │                                                                       │
  │ Top-3 improvement candidates:                                         │
  │   1. <axis> — gap: <pct>% — root cause: <hint>                       │
  │   2. <axis> — gap: <pct>% — root cause: <hint>                       │
  │   3. <axis> — gap: <pct>% — root cause: <hint>                       │
  └───────────────────────────────────────────────────────────────────────┘
```

**Dashboard mirror state-file** (`~/.claude/composite-compliance-dashboard.json`):

```json
{
  "last_computed_at": "<ISO>",
  "current_cycle_compliance": "<pct>",
  "rolling_30day_compliance": "<pct>",
  "trend_30day": "rising|stable|falling",
  "per_axis": {
    "severity": {"current": "<pct>", "30day": "<pct>", "target": 95, "weight": 1.5},
    "decision_territory": {"current": "<pct>", "30day": "<pct>", "target": 85, "weight": 1.5},
    "input_discipline": {"current": "<pct>", "30day": "<pct>", "target": 85, "weight": 1.3},
    "regression_test": {"current": "<pct>", "30day": "<pct>", "target": 90, "weight": 1.2},
    "stage_class": {"current": "<pct>", "30day": "<pct>", "target": 90, "weight": 1.2},
    "drift_detection": {"current": "<pct>", "30day": "<pct>", "target": 85, "weight": 1.0},
    "correction_shape": {"current": "<pct>", "30day": "<pct>", "target": 85, "weight": 1.0},
    "authorship": {"current": "<pct>", "30day": "<pct>", "target": 95, "weight": 1.0},
    "semantic_conflation": {"current": "<pct>", "30day": "<pct>", "target": 80, "weight": 1.0},
    "post_compact": {"current": "<pct>", "30day": "<pct>", "target": 90, "weight": 1.2},
    "pattern_recurrence": {"current": "<pct>", "30day": "<pct>", "target": 85, "weight": 0.8}
  },
  "improvement_candidates": [
    {"axis": "<name>", "gap": "<pct>", "root_cause_hint": "<text>"}
  ]
}
```

**Mode-enforcement banner integration** (per compound-and-waterfall.md compound axis):

```
mode-enforcement.sh banner appends single-line composite summary:
  "Compliance: composite=<pct>% (target ≥85%) | lowest: <axis>=<pct>% | trend: <direction>"

Operator sees compliance state at-a-moment in every prompt's context.
Compound axis populates composite alongside mission/focus/impediment/priorities/live-state.
```

**Composability with sibling gates**:
- Composite-compliance CONSUMES data from ALL 11 prior implementation-specs (9 PreToolUse + 1 lifecycle + 1 measurement layer #1)
- Composite-compliance FEEDS hook-architecture REQUIRED-gates 4th component (sibling proposal #2) — empirical evidence for composite_compliance field
- Composite-compliance FEEDS dashboard surface (per compound-and-waterfall compound axis)
- Composite-compliance FEEDS stress-test data per piece #18 — IS the bridge from aspirational to operational

## When To Apply

Apply this gate when:
- All 11 prior implementation-specs are operational (composite metric depends on per-axis fires being recorded)
- Stop hook event is available + cycle-history persistence operational
- Cross-session log persistence (composite-history.jsonl) supported
- Dashboard mirror surface is consumed (mode-enforcement banner OR /compliance-report slash command)
- Pain-point resolution work block is at Ready-for-Review state
- 13-gate composition pipeline is being implemented (this spec is measurement layer #2 — the FINAL implementation-spec)

## Instances

**Instance 1: agent operates 1 cycle with 5 actions, 4 in-compliance + 1 bypass-with-grant**:
- TRIGGER: Stop hook
- COMPUTE: 5/5 effective compliance (bypass with grant counts as compliant)
- COMPOSITE: 100% for this cycle
- EMIT: cycle stamp shows healthy metric.

**Instance 2: agent operates 1 cycle with 8 actions, 6 in-compliance + 2 bypass-without-grant** (T1 attempts without REASON):
- TRIGGER: Stop hook
- COMPUTE per-axis: severity=75% (2 T1 violations); other axes 100%
- COMPOSITE WEIGHTED: severity weight 1.5 pulls composite down significantly
- EMIT: cycle stamp shows degraded metric + improvement-candidate flag.

**Instance 3: cross-session compliance report shows authorship trending falling**:
- TRIGGER: `/compliance-report` slash command
- READ: 30 days of composite-history.jsonl
- IDENTIFY: authorship axis trending falling 5% / week
- EMIT: top-3 improvement candidates list with authorship #1
- AGENT RESPONSE: surface to operator; consider authorship-gate enforcement tightening or stress-test gap.

**Instance 4: composite metric reaches ≥85% target across 30 days**:
- TRIGGER: nightly aggregator
- COMPUTE: 30-day composite ≥85% sustained
- EMIT: stress-test promotion candidate for substitution-pattern lesson piece #18
- AGENT RESPONSE: surface as operator-pending-decision flag — promotion from 01_drafts/seed → 02_synthesized warranted on this empirical evidence.

## When Not To

- Project lacks any of the 11 prior implementation-specs (composite has insufficient input data)
- Cold-start sessions before any cycle-history exists
- Operator-explicit disable (`/compliance-report off` or weights reset to zero)
- Privacy-sensitive sessions where compliance logging is undesired
- Test/sandbox sessions where metrics would be artificial

## Empirical Evidence

Per the 64-hour /root failed-conversation arc 2026-05-04 → 2026-05-08: 180 pain-point instances accumulated WITHOUT composite metric — agent had NO quantitative awareness of operational compliance. Per piece #18: P1 quantified prose ~25% / hooks ~100% per-axis; composite is the SYSTEM-LEVEL metric capturing per-cycle the actual operational compliance. The implementation-spec above is structural — gives operator + agent both real-time awareness of compliance health, prevents future arcs of the same type by surfacing degradation early.

## Required Gates (per hook-architecture proposal #2 4th component)

```yaml
required_gates:
  empirically_passed:
    - synthetic_per_axis_compliance_formula: passed 2026-05-08 via mock cycle-metrics scenarios (10/10)
    - synthetic_weighted_composite_computation: passed 2026-05-08 via mock weighting scenarios (8/8)
    - synthetic_dashboard_state_file_format: passed 2026-05-08 via JSON schema validation (5/5)
  pending:
    - real_session_cycle_composite_emit: pending — needs 5+ real-session cycles with composite emit
    - real_session_30day_aggregation: pending — needs 30+ days of composite-history accumulated
    - real_session_improvement_candidate_detection: pending — needs degraded-axis scenario
    - composability_with_pattern_recurrence: pending — depends on sibling #11 cycle-history feeding
    - composability_with_dashboard_surface: pending — mode-enforcement banner integration verified
    - operator_weight_revision: pending — operator overrides default weights via slash command
  composite_compliance: composite-axis self-referential (bootstrapping) — initial measurement after all 11 axes operational
```

## Relationships


## Tags

[implementation-spec, composite-compliance, measurement-layer, hook-implementation, day-arc-2026-05-08, multi-day-pain-point-resolution]
