---
title: "Composite-Operational-Compliance Stress-Test Scenario Spec — Real-Session Test Plan"
type: pattern
domain: agent-config
status: synthesized
confidence: high
maturity: seed
authorship: agent-authored
created: 2026-05-08
updated: 2026-05-08
sources:
  - id: composite-compliance-implementation-spec
    type: wiki
    file: wiki/patterns/01_drafts/composite-operational-compliance-metric-implementation-spec-measurement-layer-aggregator.md
    description: "PRIMARY parent — implementation-spec #12; this stress-test spec expands its REQUIRED-gates pending list"
  - id: stress-testing-as-validation-lesson
    type: wiki
    file: wiki/lessons/01_drafts/stress-testing-as-validation-the-only-way-to-surface-aspirational-vs-operational-gaps.md
    description: "Source lesson — stress-testing-as-validation discipline; composite IS the bridge from aspirational to operational"
  - id: pattern-recurrence-stress-test-spec
    type: wiki
    file: wiki/patterns/01_drafts/pattern-recurrence-stress-test-scenario-spec-real-session-test-plan.md
    description: "Sibling stress-test spec #11 — measurement layer #1; this stress-test spec depends on its cycle-history aggregates"
  - id: comprehensive-13-gate-pattern
    type: wiki
    file: wiki/patterns/01_drafts/comprehensive-agent-action-emission-pipeline-13-gate-composition-architecture.md
    description: "Integration pattern — composite IS measurement layer #2 closing 4-layer pipeline"
  - id: hook-architecture-required-gates-proposal
    type: wiki
    file: wiki/log/2026-05-08-standardize-extension-proposal-hook-architecture-required-gates-4th-component.md
    description: "Sibling proposal — REQUIRED-gates 4th component; this metric IS the empirical evidence the 4th component requires"
tags: [stress-test-scenario-spec, composite-compliance, measurement-layer-2, test-plan, day-arc-2026-05-08, multi-day-pain-point-resolution]
---

# Composite-Operational-Compliance Stress-Test Scenario Spec — Real-Session Test Plan

## Summary

Per piece #18 (stress-testing-as-validation lesson) + impl-spec #12 (composite-compliance, measurement layer #2) REQUIRED-gates pending list, the composite-compliance metric operational-compliance is bridged from synthetic to real-session via concrete stress-test scenarios. This piece defines 5 named scenarios — covering per-cycle composite computation + cross-session 30-day rolling aggregation + improvement-candidate detection + dashboard mirror + operator weight-revision. Per substitution-pattern Insight 5b: declaring "≥85% composite-compliance" is aspirational without runtime aggregator computing it. This is the **FINAL** stress-test scenario spec in the 12-spec sequence — closes test-plan substitution at measurement layer #2 and the entire 13-gate pipeline.

## Pattern Description

**Stress-test layer**: real-session evidence + operator-empirical confirmation. Scenarios derived empirically from impl-spec #12 weighted-formula + dashboard requirements. Gate #12 is the integration metric — consumes ALL 11 prior axes' data via measurement layer #1 (sibling #11) and emits composite-compliance % at per-cycle + per-30-day granularity.

### Scenario 1 — per-cycle composite computation (Stop hook)

```yaml
scenario_1_per_cycle_composite:
  setup:
    - cycle just ended; pattern-recurrence aggregator (sibling #11) wrote ~/.claude/cycle-history/<cycle_id>.json
    - cycle had 5 actions: 4 in-compliance + 1 T1 BLOCK with operator-grant bypass
    - per-axis fire-counts:
        - severity: T1 attempt + grant bypass = 1 in-compliance (bypass with grant counts as compliant)
        - 0 fires on other axes (read-only intervening operations)
  trigger:
    - Stop hook (after pattern-recurrence aggregator completes)
  expected:
    - LOAD ~/.claude/cycle-history/<cycle_id>.json (cycle metrics)
    - COMPUTE per-axis compliance:
        severity: 1/1 = 100% (bypass with grant)
        decision-territory: no fires = N/A → 100% default
        ... (all axes)
    - APPLY weighted formula:
        composite = weighted_average(axis_compliance_i)
        WEIGHTS: severity 1.5x, decision-territory 1.5x, input-discipline 1.3x, ...
    - APPEND to ~/.claude/composite-history.jsonl:
        {"cycle_id": "<>", "timestamp": "<ISO>", "composite": 100.0, "per_axis": {...}}
    - EMIT in cycle stamp:
        "COMPOSITE-COMPLIANCE: 100% (cycle <id>)
         ├─ severity: 100% | decision-territory: 100% | input: 100%
         ...
         └─ TARGET: ≥85%"
  pass_criteria:
    - per-axis compliance correctly computed
    - weighted formula deterministic
    - composite rounded to integer percentage
    - composite-history.jsonl appends one entry per cycle
    - cycle stamp shows compact composite summary
  edge_cases:
    - cycle had ZERO actions (read-only): all axes N/A → composite = 100% (vacuous)
    - cycle had ALL actions non-compliant: composite low (e.g., 20%)
    - per-axis compliance = 0% on weighted axis: composite drops significantly
    - operator weight-override: re-compute composite with operator weights
```

### Scenario 2 — cross-session 30-day rolling aggregation (`/compliance-report`)

```yaml
scenario_2_cross_session_30day_rolling:
  setup:
    - composite-history.jsonl populated with 30 days of cycle entries
    - operator types: `/compliance-report`
  trigger:
    - UserPromptSubmit detects /compliance-report slash command
  expected:
    - READ ~/.claude/composite-history.jsonl (all entries)
    - GROUP by date (per-day rollup)
    - COMPUTE 30-day composite (rolling)
    - COMPUTE per-axis 30-day rolling
    - COMPUTE trends: rising / stable / falling per axis (slope of last 30 days)
    - IDENTIFY top-3 lowest-compliance axes
    - IDENTIFY top-3 highest-compliance axes
    - EMIT report:
        ┌──────────────────────────────────────────────────────────┐
        │ COMPLIANCE REPORT — last 30 days                        │
        │ Composite: 87% (target ≥85%) — trend: stable           │
        │                                                          │
        │ Per-axis: severity 95% / decision-territory 90% / ...  │
        │                                                          │
        │ Top-3 improvement candidates:                           │
        │   1. semantic-conflation 72% — gap: 8% — root: detector calibration │
        │   2. drift-detection 78% — gap: 7% — root: scope taxonomy │
        │   3. correction-shape 80% — gap: 5% — root: dimension naming │
        └──────────────────────────────────────────────────────────┘
  pass_criteria:
    - 30-day window correctly bounded
    - per-axis trends computed (slope > +1% = rising, etc)
    - top-3 candidates correctly ordered by gap
    - report formatted in ASCII bar-chart per impl-spec #12 dashboard
  edge_cases:
    - composite-history < 30 days: emit "insufficient data; <N>-day rolling"
    - all axes at 100%: emit "no improvement candidates; healthy"
    - all axes at 0%: emit "system-wide degradation; surface to operator"
```

### Scenario 3 — improvement-candidate detection + root-cause hint

```yaml
scenario_3_improvement_candidate_detection:
  setup:
    - 30-day composite shows axis "drift-detection" at 78% (target ≥85%, gap 7%)
    - cycle-history shows: drift_event_count averaging 3 per cycle (high)
  trigger:
    - `/compliance-report` slash command (or auto-emit at threshold)
  expected:
    - DETECT: drift-detection axis below target with sustained gap
    - HINT root cause: high drift_event_count indicates active-task scope taxonomy may be incomplete
    - SURFACE in report:
        "1. drift-detection 78% — gap: 7% — root: high drift_event_count;
            consider scope taxonomy revision (per piece C13 follow-up)"
  pass_criteria:
    - root-cause hint matches axis-specific data pattern
    - hint is actionable (cites which subsystem to iterate on)
    - operator can use hint to drive next sprint of improvements
  edge_cases:
    - root-cause hint not deterministic (multiple data patterns): emit best-guess + alternative
    - axis at gap but cycle-history empty (cold-start): hint: "insufficient data for root-cause"
    - operator overrides root-cause hint: log operator's revision; refine future hints
```

### Scenario 4 — dashboard mirror state-file consumption by mode-enforcement banner

```yaml
scenario_4_dashboard_mirror_in_banner:
  setup:
    - mode-enforcement banner (compound axis per piece compound-and-waterfall.md)
    - ~/.claude/composite-compliance-dashboard.json populated by Stop hook (sibling #12 implementation)
    - operator submits new prompt
  trigger:
    - UserPromptSubmit hook (mode-enforcement banner emission)
  expected:
    - LOAD ~/.claude/composite-compliance-dashboard.json
    - EXTRACT current_cycle_compliance + rolling_30day + lowest-axis
    - APPEND single-line composite summary to mode-enforcement banner:
        "Compliance: composite=87% (target ≥85%) | lowest: semantic-conflation=72% | trend: stable"
    - operator sees compliance state at-a-moment in every prompt's context
  pass_criteria:
    - banner appends compliance line without disrupting other layers
    - composite-compliance-dashboard.json is read-current (not stale)
    - line is compact (single-line; ≤200 chars)
    - operator can act on visibility (e.g., decide to focus on lowest-axis)
  edge_cases:
    - dashboard state-file missing (cold-start): banner emits "compliance: pending data"
    - dashboard state-file stale (>1 hour old): banner emits "compliance: stale; recompute via /compliance-report"
    - operator doesn't want compliance in banner: opt-out via /compliance-banner off
```

### Scenario 5 — operator weight revision via slash command

```yaml
scenario_5_operator_weight_revision:
  setup:
    - default weights: severity 1.5x, decision-territory 1.5x, ...
    - operator types: `/compliance-weights set semantic-conflation 2.0` (raising weight)
  trigger:
    - UserPromptSubmit detects /compliance-weights slash command
  expected:
    - parse arguments: axis="semantic-conflation", weight=2.0
    - validate: axis in known set; weight in reasonable range (0.1-3.0)
    - WRITE ~/.claude/composite-weights.json:
        {"semantic-conflation": 2.0, ... others default}
    - subsequent composite computation uses operator weights
    - audit log to ~/.claude/composite-weight-revisions.log
  pass_criteria:
    - weight revision deterministic
    - audit log captures both old and new weight + operator-grant timestamp
    - subsequent cycle's composite reflects new weight
    - operator can list current weights via /compliance-weights show
  edge_cases:
    - weight value invalid (negative, >10): emit error; weight unchanged
    - axis name unknown: emit error; recommend valid axis names
    - weight = 0 (excludes axis): allowed but warns "this disables axis from composite"
    - operator sets weight on excluded axis (composite-compliance itself): emit error; self-referential exclusion preserved
```

## When To Apply

Apply this stress-test scenario spec when:
- Implementation-spec #12 (composite-compliance) is being implemented
- All 11 prior implementation-specs (axes 1-9 + lifecycle + measurement-1) operational
- Stop hook event available + cycle-history persistence operational (per sibling #11)
- Cross-session log persistence (composite-history.jsonl) supported
- Dashboard mirror surface consumed (mode-enforcement banner OR /compliance-report)
- Pain-point resolution work block at Ready-for-Review state
- 13-gate pipeline is being implemented (this is the **FINAL** stress-test spec — measurement layer #2)

## Instances

**Instance 1: full stress-test session — operator runs all 5 scenarios**:
- Total time: ~30-45 minutes (multi-cycle scenarios + 30-day rolling requires accumulated data)
- Output: per-scenario pass/fail + measurement-layer-2 compliance %
- Updates impl-spec #12 REQUIRED-gates: pending → empirically_passed per scenario
- This stress-test session CLOSES the 12-spec sequence; entire 13-gate pipeline is empirically-stress-tested

**Instance 2: cross-axis composability — entire pipeline integration test**:
- Trigger: cycle with mixed gate activity → pattern-recurrence (#11) → composite-compliance (#12) → dashboard banner (compound axis)
- Expected: full data flow validated end-to-end
- Verifies entire 13-gate pipeline behaves coherently per piece #1 integration pattern

**Instance 3: scenario fails on weighted-formula precision**:
- Synthetic test passed; real-session: floating-point composite computation has small drift across many cycles
- Surface root cause: rounding strategy needs explicit policy (banker's rounding vs truncation)
- Iterate on impl-spec #12 — formalize rounding policy

**Instance 4: scenario passes but operator wants different per-axis targets**:
- Default targets: severity ≥95%, decision-territory ≥85%, etc
- Operator: "I want severity ≥99% as the standard"
- Per evidence-priority hierarchy: operator-empirical override
- Surface as target-revision flow (similar to weight-revision in Scenario 5)
- Iterate on impl-spec #12 — add /compliance-targets slash command

## When Not To

- Implementation-spec #12 not yet authored
- Any of the 11 prior implementation-specs not operational (substrate dependency)
- Cold-start sessions before any cycle-history exists
- Operator-explicit disable (`/compliance-report off` or all weights = 0)
- Privacy-sensitive sessions where compliance logging is undesired

## Empirical Evidence

Per the 64-hour /root failed-conversation arc 2026-05-04 → 2026-05-08: 180 pain-point instances accumulated WITHOUT composite metric — agent had NO quantitative awareness of operational compliance. The composite metric is the structural awareness instrument; without it, axis-level data is fragmented per-fire. The 5 scenarios derive empirically from impl-spec #12 weighted-formula + dashboard requirements + operator-revision needs.

## Required Gates (per hook-architecture proposal #2 4th component)

```yaml
required_gates:
  empirically_passed:
    - synthetic_per_axis_compliance_formula: passed 2026-05-08 via mock cycle scenarios (10/10)
    - synthetic_weighted_composite_computation: passed 2026-05-08 via mock weighting (8/8)
    - synthetic_dashboard_state_file_format: passed 2026-05-08 via JSON schema (5/5)
  pending:
    - real_session_scenario_1_per_cycle_composite: pending — needs 5+ real-session cycles with mixed activity
    - real_session_scenario_2_30day_rolling: pending — needs 30+ days of accumulated composite-history
    - real_session_scenario_3_improvement_candidate: pending — needs degraded-axis scenario
    - real_session_scenario_4_dashboard_in_banner: pending — needs mode-enforcement banner integration
    - real_session_scenario_5_operator_weight_revision: pending — depends on /compliance-weights slash command
    - composability_with_pattern_recurrence: pending — depends on sibling #11 cycle-history feeding
    - operator_empirical_target_calibration: pending — operator confirms per-axis targets are useful
    - end_to_end_pipeline_integration: pending — full 13-gate pipeline empirical validation
  composite_compliance: composite-axis self-referential (bootstrapping) — initial measurement after all 11 axes operational
```

## Relationships

- IMPLEMENTS test plan for: implementation-spec #12 (composite-operational-compliance-metric)

## Tags

[stress-test-scenario-spec, composite-compliance, measurement-layer-2, test-plan, day-arc-2026-05-08, multi-day-pain-point-resolution]
