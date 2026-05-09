---
title: "Pattern-Recurrence-Quantification Stress-Test Scenario Spec — Real-Session Test Plan"
type: pattern
domain: agent-config
status: synthesized
confidence: high
maturity: seed
authorship: agent-authored
created: 2026-05-08
updated: 2026-05-08
sources:
  - id: pattern-recurrence-implementation-spec
    type: wiki
    file: wiki/patterns/01_drafts/pattern-recurrence-quantification-gate-implementation-spec-measurement-layer-cycle-aggregation.md
    description: "PRIMARY parent — implementation-spec #11; this stress-test spec expands its REQUIRED-gates pending list"
  - id: stress-testing-as-validation-lesson
    type: wiki
    file: wiki/lessons/01_drafts/stress-testing-as-validation-the-only-way-to-surface-aspirational-vs-operational-gaps.md
    description: "Source lesson — stress-testing-as-validation discipline"
  - id: c15-pattern-recurrence-pattern
    type: wiki
    file: wiki/patterns/01_drafts/pattern-recurrence-quantification-and-operator-frustration-as-signal.md
    description: "Cluster pattern C15 — defines the empirical gap this stress-test set measures"
  - id: post-compact-stress-test-spec
    type: wiki
    file: wiki/patterns/01_drafts/post-compact-stress-test-scenario-spec-real-session-test-plan.md
    description: "Sibling stress-test spec #10 — pattern parallels (5-scenario format)"
  - id: composite-compliance-implementation-spec
    type: wiki
    file: wiki/patterns/01_drafts/composite-operational-compliance-metric-implementation-spec-measurement-layer-aggregator.md
    description: "Sibling — composite-compliance metric (impl-spec #12); pattern-recurrence FEEDS composite"
tags: [stress-test-scenario-spec, pattern-recurrence, measurement-layer-1, test-plan, day-arc-2026-05-08, multi-day-pain-point-resolution]
---

# Pattern-Recurrence-Quantification Stress-Test Scenario Spec — Real-Session Test Plan

## Summary

Per piece #18 (stress-testing-as-validation lesson) + impl-spec #11 (pattern-recurrence-quantification, measurement layer #1) REQUIRED-gates pending list, the measurement-layer #1 operational-compliance is bridged from synthetic to real-session via concrete stress-test scenarios. This piece defines 5 named scenarios — covering Stop-hook cycle aggregation + same-axis recurrence detection + cross-cycle pattern detection + frustration-recurrence + correction-recurrence auto-escalation. Per substitution-pattern Insight 5b: declaring "iteration circuit-breaker after 2 corrections" is aspirational without runtime aggregator. This spec closes the test-plan substitution at measurement layer #1.

## Pattern Description

**Stress-test layer**: real-session evidence + operator-empirical confirmation. Scenarios derived empirically from cluster C15 pain-point instances. Gate #11 fires Stop-hook (cycle-end) + cross-session aggregator (slash command). Each scenario covers a recurrence-classification rule.

### Scenario 1 — cycle-end aggregation (Stop hook reads 9 PreToolUse audit logs)

```yaml
scenario_1_cycle_end_aggregation:
  setup:
    - cycle in progress with mixed gate activity:
        - 3 PreToolUse fires on input-discipline (1 banner, 2 silent)
        - 2 fires on severity-T2 (warns)
        - 1 fire on stage-class violation (block)
        - 0 fires on regression-test (no code edits)
        - 5 fires on drift-detection (3 soft, 2 hard)
        - 1 active-correction (resolved-one-notch this cycle)
    - all audit logs populated this cycle
  trigger:
    - Stop hook (end of cycle)
  expected:
    - LOAD all 9 PreToolUse audit logs + lifecycle event-log + correction-history
    - AGGREGATE per-cycle:
        - input_discipline: {fires: 3, banners: 1, bypasses: 0}
        - severity_t2: {warns: 2}
        - stage_class: {violations_blocked: 1}
        - regression_test: {no fires}
        - drift_detection: {soft: 3, hard: 2}
        - correction_shape: {resolved_one_notch: 1}
    - WRITE ~/.claude/cycle-history/<cycle_id>.json with aggregate
    - EMIT systemMessage in cycle stamp: "GATE-METRICS: ..."
  pass_criteria:
    - cycle-history JSON deterministically written
    - all 11 axes counted in aggregate
    - cycle stamp shows compact metrics summary
    - no duplicate counts (each fire counted once)
  edge_cases:
    - cycle had ZERO gate fires (read-only operations only): aggregate is all-zeros; stamp shows clean state
    - audit log file missing for one axis: aggregate uses zeros; warn about missing log
    - cycle ID rotation mid-cycle (rare): aggregate spans both IDs; flag inconsistency
```

### Scenario 2 — same-axis recurrence detection (≥3 fires in single cycle)

```yaml
scenario_2_same_axis_recurrence:
  setup:
    - this cycle: stage-class gate fires 4 times (4 separate violations across 4 edits)
    - cycle-history aggregator reads stage_class metrics: 4 violations
  trigger:
    - Stop hook
  expected:
    - DETECT: same-axis recurrence (≥3 fires in one cycle)
    - EMIT in cycle stamp:
        "RECURRING-PATTERN: stage-class fired 4 times this cycle.
         Consider escalation per piece #13 circuit-breaker."
    - record in recurrence_flags.same_axis_recurrence array: ["stage-class"]
  pass_criteria:
    - threshold detection (≥3) deterministic
    - recommendation banner cites piece #13 circuit-breaker
    - subsequent cycles can read this recurrence flag
  edge_cases:
    - exactly 2 fires (below threshold): silent; not flagged
    - exactly 3 fires: flagged (boundary inclusive)
    - mixed: 3 stage-class + 5 drift-detection: BOTH axes flagged in array
```

### Scenario 3 — cross-cycle recurrence detection (same axis fires across N consecutive cycles)

```yaml
scenario_3_cross_cycle_recurrence:
  setup:
    - last 3 cycles have stage-class violations (1+ per cycle)
    - cross-cycle aggregator reads ~/.claude/cycle-history/*.json
  trigger:
    - `/recurrence-report` slash command OR auto-emit at end of 3rd cycle
  expected:
    - DETECT: stage-class fires in 3 of last 3 cycles → ≥3 cross-cycle threshold
    - EMIT:
        "CROSS-CYCLE PATTERN: stage-class fires every cycle for 3 cycles.
         Pattern is systemic; surface to operator."
    - surface as TOP-3 IMPROVEMENT CANDIDATE (per impl-spec #12 dashboard)
  pass_criteria:
    - cross-cycle algorithm correctly counts axis-fires per cycle
    - threshold (≥3 of 10 cycles) detection deterministic
    - recommendation surfaces systemic-pattern-of-violations
  edge_cases:
    - axis fires 3 times in cycle 1, 0 times in cycles 2-3: NOT cross-cycle (same-cycle pattern only)
    - axis fires 1 time per cycle for 5+ cycles: flagged at 3rd cycle
    - cycle-history shorter than 3 cycles (cold-start): cross-cycle aggregator emits "insufficient data; need 3+ cycles"
```

### Scenario 4 — frustration-recurrence detection (≥2 negative-affect markers in single cycle)

```yaml
scenario_4_frustration_recurrence:
  setup:
    - operator's prompts this cycle:
        1. "WTF this is wrong"
        2. "fucking trash"
    - both prompts capture by UserPromptSubmit detector layer (negative-affect markers)
  trigger:
    - Stop hook
  expected:
    - DETECT: frustration-recurrence ≥2 (boundary)
    - set recurrence_flags.frustration_signal = true
    - EMIT in cycle stamp:
        "FRUSTRATION SIGNAL: operator-frustration markers accumulated this cycle.
         Per piece C15 + #13: stop iterating; ask explicitly."
  pass_criteria:
    - threshold deterministic (≥2)
    - frustration markers counted accurately
    - recommendation surfaces circuit-breaker action
    - subsequent cycle's banner emits "frustration-recurrence carryover" if not resolved
  edge_cases:
    - 1 frustration marker (below threshold): silent; not flagged
    - 5+ frustration markers (high-severity): emit "URGENT: surface to operator NOW"
    - operator's frustration is about a DIFFERENT system (not agent): markers still match; banner emits cautious wording
```

### Scenario 5 — correction-recurrence auto-escalate (consecutive_corrections ≥3)

```yaml
scenario_5_correction_recurrence_escalate:
  setup:
    - active-correction.json from correction-shape gate (sibling #5):
        consecutive_corrections_count: 3 (this is 3rd correction on dimension D)
    - prior 2 corrections did NOT lead to convergence
  trigger:
    - Stop hook (or correction-shape detector at UserPromptSubmit at the moment count=3)
  expected:
    - DETECT: correction-recurrence ≥3 → AUTO-ESCALATE
    - WRITE ~/.claude/circuit-breaker-pending.flag for dimension D
    - EMIT:
        "CIRCUIT-BREAKER triggered per piece #13 — 3 consecutive corrections on dimension D.
         BLOCK next iteration of same correction-target until operator clarifies.
         RECOMMEND: ask operator explicitly what they want this to be."
    - subsequent PreToolUse on same dimension D: BLOCK + emit "CIRCUIT-BREAKER active"
  pass_criteria:
    - escalation triggers at exactly 3rd correction (not before)
    - flag deterministic write
    - subsequent edits on same dimension blocked
    - operator-clarification (e.g., explicit dimension-naming) clears flag
  edge_cases:
    - count=2 (below threshold): silent; not escalated
    - count=4+ (above threshold): flag persists; warn about overrun
    - operator clears flag explicitly via /circuit-break clear D: flag cleared; iteration resumes
    - dimension naming changes mid-escalation: counter doesn't carry; new dimension has fresh count
```

## When To Apply

Apply this stress-test scenario spec when:
- Implementation-spec #11 (pattern-recurrence) is being implemented
- All 9 PreToolUse implementation-specs (axes 1-9) operational + writing audit logs
- Lifecycle-event implementation-spec (axis 10) operational + writing event log
- Stop hook event available
- Cycle-history persistence supported
- Pain-point cluster C15 axis warrants empirical compliance measurement
- 13-gate pipeline is being implemented (this is measurement layer #1 of 12 stress-test specs)

## Instances

**Instance 1: full stress-test session — operator runs all 5 scenarios**:
- Total time: ~30-45 minutes (multi-cycle scenarios require multiple Stop-hook fires)
- Output: per-scenario pass/fail + measurement-layer-1 compliance %
- Updates impl-spec #11 REQUIRED-gates: pending → empirically_passed per scenario

**Instance 2: cross-axis composability (pattern-recurrence + composite-compliance)**:
- Trigger: cycle aggregate feeds into composite-compliance computation (impl-spec #12)
- Expected: pattern-recurrence cycle-history → composite metric uses these aggregates
- Verifies measurement layer composability + dashboard surface

**Instance 3: scenario fails on cycle-history JSON serialization**:
- Synthetic test passed; real-session: special characters in operator-verbatim quotes break JSON
- Surface root cause: JSON serialization not handling unicode/control-chars cleanly
- Iterate on impl-spec #11 — JSON serializer with proper escaping

**Instance 4: scenario passes but operator finds GATE-METRICS line cluttered**:
- Per evidence-priority hierarchy: operator-empirical override
- Surface as cycle-stamp format calibration (collapse to compact summary OR expand on demand)
- Iterate on impl-spec #11 — banner format calibration

## When Not To

- Implementation-spec #11 not yet authored
- 9 PreToolUse audit logs not yet authored (substrate dependency)
- Cold-start cycles before any audit data exists
- Cycle-history persistence not desired (privacy / log-rotation concerns)
- Operator explicitly disabled measurement (`/recurrence-report off`)

## Empirical Evidence

Per pain-point cluster C15 in master inventory: 16+ pain-point instances of "agent didn't recognize recurring pattern", "agent kept iterating same approach", "operator-frustration grew without quantitative-awareness signal". The 5 scenarios derive empirically from those instances + threshold-tuning per piece C15.

## Required Gates (per hook-architecture proposal #2 4th component)

```yaml
required_gates:
  empirically_passed:
    - synthetic_audit_log_aggregation: passed 2026-05-08 via mock 9-axis logs (10/10)
    - synthetic_recurrence_classification: passed 2026-05-08 via mock pattern scenarios (8/8)
    - synthetic_circuit_breaker_threshold: passed 2026-05-08 via consecutive_corrections=3 (5/5)
  pending:
    - real_session_scenario_1_cycle_aggregation: pending — needs 5+ real-session cycles with mixed gate activity
    - real_session_scenario_2_same_axis_recurrence: pending
    - real_session_scenario_3_cross_cycle_recurrence: pending — needs 10+ consecutive cycles
    - real_session_scenario_4_frustration_recurrence: pending
    - real_session_scenario_5_correction_auto_escalate: pending
    - composability_with_composite_compliance: pending — depends on impl-spec #12 operational
    - cycle_history_persistence_format: pending — JSON schema validated against consumer
    - operator_empirical_format_calibration: pending
  composite_compliance: pattern-recurrence-axis stress-test 0% (depends on 9-axis substrate) — target ≥85%
```

## Relationships

- IMPLEMENTS test plan for: implementation-spec #11 (pattern-recurrence-quantification-gate)

## Tags

[stress-test-scenario-spec, pattern-recurrence, measurement-layer-1, test-plan, day-arc-2026-05-08, multi-day-pain-point-resolution]
