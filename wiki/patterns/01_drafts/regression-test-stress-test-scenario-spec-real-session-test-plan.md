---
title: "Regression-Test Stress-Test Scenario Spec — Real-Session Test Plan"
type: pattern
domain: agent-config
status: synthesized
confidence: high
maturity: seed
authorship: agent-authored
created: 2026-05-08
updated: 2026-05-08
sources:
  - id: regression-test-implementation-spec
    type: wiki
    file: wiki/patterns/01_drafts/regression-test-gate-implementation-spec-pre-and-post-edit-verification.md
    description: "PRIMARY parent — implementation-spec #3; this stress-test spec expands its REQUIRED-gates pending list"
  - id: stress-testing-as-validation-lesson
    type: wiki
    file: wiki/lessons/01_drafts/stress-testing-as-validation-the-only-way-to-surface-aspirational-vs-operational-gaps.md
    description: "Source lesson — stress-testing-as-validation discipline"
  - id: c03-regression-test-pattern
    type: wiki
    file: wiki/patterns/01_drafts/pre-edit-regression-test-gate-canonical-verified-edit-enforcement.md
    description: "Cluster pattern C03 — defines the empirical gap this stress-test set measures"
  - id: decision-territory-stress-test-spec
    type: wiki
    file: wiki/patterns/01_drafts/decision-territory-stress-test-scenario-spec-real-session-test-plan.md
    description: "Sibling stress-test spec #2 — pattern parallels (5-scenario format)"
  - id: composite-compliance-implementation-spec
    type: wiki
    file: wiki/patterns/01_drafts/composite-operational-compliance-metric-implementation-spec-measurement-layer-aggregator.md
    description: "Sibling — composite-compliance metric; this stress-test data is the input"
tags: [stress-test-scenario-spec, regression-test, gate-3, test-plan, day-arc-2026-05-08, multi-day-pain-point-resolution]
---

# Regression-Test Stress-Test Scenario Spec — Real-Session Test Plan

## Summary

Per piece #18 (stress-testing-as-validation lesson) + impl-spec #3 (regression-test gate) REQUIRED-gates pending list, the regression-test gate operational-compliance is bridged from synthetic to real-session via concrete stress-test scenarios. This piece defines 5 named scenarios with setup + trigger + expected gate behavior + pass criteria + edge cases. Per substitution-pattern Insight 5b: implementation-spec describes WHAT to build (PreToolUse baseline + PostToolUse verification); stress-test scenario spec describes HOW to verify operationally. Without these scenarios, baseline-capture timing + post-edit comparison + delta-emission remains aspirational. This spec closes the test-plan substitution at axis #3.

## Pattern Description

**Stress-test layer**: real-session evidence (per piece #18 evidence-priority tier 2) + operator-empirical confirmation (tier 1). Scenarios derived empirically from cluster C03 pain-point instances. Gate #3 is unique: BOTH PreToolUse (baseline) AND PostToolUse (verify) phases — scenarios cover both phases per scenario.

### Scenario 1 — verified-edit confirmation (no regression path)

```yaml
scenario_1_verified_edit_confirm:
  setup:
    - test-runner reachable: `python3 -m tools.run-tests` returns 322/322 baseline
    - target file: tools/cycle.py (matches TEST-REQUIRING)
    - cycle just started; no prior baseline captured
    - edit will not break anything (cosmetic comment edit)
  trigger_pre:
    - PreToolUse on Edit tools/cycle.py
  expected_pre:
    - baseline check: state-file empty for current cycle
    - test-runner executes: 322/322 captured
    - state-file ~/.claude/regression-baseline.json populated
    - allow edit silently (baseline pass)
  trigger_post:
    - PostToolUse on Edit tools/cycle.py
  expected_post:
    - test-runner re-executes: 322/322 still passing
    - banner emits: "REGRESSION-TEST GATE — verified-edit confirmed. 322/322 → 322/322"
    - cycle stamp action-type: "verified-edit per Hard Rule 14"
  pass_criteria:
    - baseline captured BEFORE edit
    - post-run executes deterministically
    - confirmation banner emits
    - state-file post_edit_runs array appended
  edge_cases:
    - test-runner fails at baseline (network/env): emit "baseline broken" warning, allow edit
    - test runtime exceeds 30s: surface "long test runtime" notice; consider deferred verification
    - cycle was already running with stale baseline from prior cycle: rotate baseline (cycle_id mismatch)
```

### Scenario 2 — regression detected (BLOCK on pattern; banner emits)

```yaml
scenario_2_regression_detected:
  setup:
    - baseline 322/322 captured this cycle
    - target file: .claude/hooks/output-discipline-guard.sh
    - edit will break 3 unit tests (e.g., agent removes a function the tests depend on)
  trigger_pre:
    - PreToolUse on Edit
  expected_pre:
    - baseline already captured this cycle: skip re-run
    - allow edit silently
  trigger_post:
    - PostToolUse on Edit
  expected_post:
    - test-runner: 319/322 (3 failed)
    - banner emits regression-detected variant:
        "REGRESSION-TEST GATE — regression detected post-edit.
         BASELINE: 322 passed
         POST-EDIT: 319 passed (3 failed)
         DELTA: test_a, test_b, test_c failed.
         RECOMMEND: revert OR fix the failing tests."
    - DO NOT auto-revert
  pass_criteria:
    - regression detected without false-positive
    - delta lists specific test names
    - banner does NOT auto-revert (agent decides)
    - cycle stamp action-type: NOT verified-edit; flagged as regression-pending
  edge_cases:
    - new tests added in same edit (322 → 325 passed): NOT regression; verified-edit per superset
    - tests skipped due to missing dep: emit "test-skipped" warning; not regression
    - test-runner crashes: emit "test-runner-failed" warning; gate cannot verify
```

### Scenario 3 — TEST-EXEMPT path (silent, no test-run)

```yaml
scenario_3_test_exempt_silent:
  setup:
    - target file: wiki/log/2026-05-08-foo.md (TEST-EXEMPT: *.md)
  trigger_pre:
    - PreToolUse on Write
  expected_pre:
    - classify TEST-EXEMPT: no baseline capture
    - silent allow
  trigger_post:
    - PostToolUse on Write
  expected_post:
    - classify TEST-EXEMPT: no verification
    - silent allow
  pass_criteria:
    - no banner emits
    - no test-runner execution
    - no state-file mutation
    - cycle stamp action-type: new-artifact (not verified-edit; doesn't apply)
  edge_cases:
    - file is .yaml (TEST-EXEMPT but config): same silent allow; config-validation handled separately
    - file is .py but in /docs/ (documentation Python examples): TEST-REQUIRING by extension; baseline still captures
    - file path matches multiple patterns: most-specific match wins (TEST-EXEMPT explicit > extension default)
```

### Scenario 4 — baseline-broken-at-cycle-start (graceful degradation)

```yaml
scenario_4_baseline_already_broken:
  setup:
    - cycle starts with test suite already broken (e.g., 320/322; 2 pre-existing failures)
    - target file: tools/cycle.py
  trigger_pre:
    - PreToolUse on Edit
  expected_pre:
    - test-runner executes: 320/322 (2 pre-existing failures)
    - banner emits "baseline already broken" warning:
        "BASELINE: 320/322 (2 pre-existing failures: test_x, test_y)
         WARNING: cycle starts with broken baseline; gate emits warnings, does not block."
    - allow edit
  trigger_post:
    - PostToolUse on Edit
  expected_post:
    - test-runner: must verify failures don't WORSEN (320 → 320 OK; 320 → 318 regression)
    - banner: "POST-EDIT: 320/322. No new regressions; pre-existing failures persist."
  pass_criteria:
    - broken baseline doesn't block edits
    - banner explicitly states pre-existing failures
    - post-edit comparison: regression = ANY worsening (not just zero failures expected)
  edge_cases:
    - baseline 0/322 (test suite completely broken): warning + allow; cycle is in test-fix mode
    - operator explicitly working on test fixes (intent: 320→322): verified-edit confirmed if numbers IMPROVE
    - baseline has FLAKY tests: emit "flaky-test detected" advisory; recommend re-run
```

### Scenario 5 — bypass with operator-grant for legitimate behavior change

```yaml
scenario_5_bypass_legitimate_behavior_change:
  setup:
    - baseline 322/322
    - operator just said: "we're refactoring; tests will be rewritten — proceed despite expected regressions"
    - REASON="operator-explicit-refactor-2026-05-08-14:04"
  trigger_pre:
    - PreToolUse on Edit (or batch of edits)
  expected_pre:
    - REASON= bypass detected; baseline still captured for audit
    - silent allow
  trigger_post:
    - PostToolUse on Edit
  expected_post:
    - test-runner: <regression>
    - banner emits but with bypass-acknowledged variant:
        "REGRESSION-TEST GATE — regression detected; bypass active per REASON=
         BYPASS_REASON: operator-explicit-refactor-2026-05-08-14:04
         Audit logged to ~/.claude/hooks/regression-test-bypass.log"
    - cycle stamp action-type: "verified-edit-with-operator-bypass"
  pass_criteria:
    - bypass logs but doesn't suppress audit completely
    - operator-grant citation captured in audit log
    - subsequent cycles see baseline-rotation (broken baseline expected per refactor)
  edge_cases:
    - REASON= without grant citation: emit "weak bypass" warning + still allow
    - bypass repeated across many cycles: aggregator (impl-spec #11) flags pattern-recurrence
    - operator removes bypass mid-refactor: gate resumes blocking on next regression
```

## When To Apply

Apply this stress-test scenario spec when:
- Implementation-spec #3 (regression-test gate) is being implemented
- Test-runner is reachable + reasonable runtime (≤30s)
- Project has TEST-REQUIRING + TEST-EXEMPT path conventions
- Pain-point cluster C03 axis warrants empirical compliance measurement
- 13-gate pipeline is being implemented (this is axis #3 of 12 stress-test specs)

## Instances

**Instance 1: full stress-test session — operator runs all 5 scenarios**:
- Total time: ~30-40 minutes (test-runner runs are the bulk of time per scenario)
- Output: per-scenario pass/fail + axis-level compliance %
- Updates impl-spec #3 REQUIRED-gates: pending → empirically_passed per scenario

**Instance 2: cross-axis composability (regression-test + stage-class)**:
- Trigger: implement-stage edit on tools/cycle.py
- Expected: BOTH stage-class (allowed) + regression-test (verify) emit + cooperate
- Verifies banner-stacking + per-axis state-file independence

**Instance 3: scenario fails on test-runner reachability**:
- `python3 -m tools.run-tests` requires .venv/bin/python (per CLAUDE.md Hard Rule 5)
- Synthetic test passed; real-session fails because system python lacks deps
- Surface root cause: hook command needs `.venv/bin/python` not `python3`
- Iterate on impl-spec #3 — fix command in spec; re-run scenarios

**Instance 4: scenario passes but operator finds banner content too long**:
- Per evidence-priority hierarchy: operator-empirical override
- Surface as banner-format calibration issue (one-notch tightening)
- Iterate on impl-spec banner format; re-run scenario

## When Not To

- Implementation-spec #3 not yet authored
- Project lacks reachable test-runner (early-scaffold; no tests yet)
- Test runtime exceeds operator-tolerance (long integration tests; defer to async path)
- Cold-start scaffolding when test suite itself is being authored (chicken-and-egg)
- Operator-explicit deferral via REASON= bypass on entire stress-test execution

## Empirical Evidence

Per pain-point cluster C03 in master inventory: 12+ pain-point instances of "agent claimed verified-edit without running tests". The 5 scenarios derive empirically from those instances. The composability test (Instance 2) verifies this gate composes cleanly with stage-class (sibling axis #7).

## Required Gates (per hook-architecture proposal #2 4th component)

```yaml
required_gates:
  empirically_passed:
    - synthetic_scenario_definition: passed 2026-05-08 via mock baseline+post pairs (5/5)
  pending:
    - real_session_scenario_1_verified_edit_confirm: pending
    - real_session_scenario_2_regression_detected: pending
    - real_session_scenario_3_test_exempt_silent: pending
    - real_session_scenario_4_baseline_broken_graceful: pending
    - real_session_scenario_5_bypass_legitimate_refactor: pending
    - composability_with_stage_class: pending
    - operator_empirical_banner_calibration: pending
  composite_compliance: regression-test-axis stress-test 0% (no real-session executions yet) — target ≥90% (highest among gates)
```

## Relationships

- IMPLEMENTS test plan for: implementation-spec #3 (regression-test-gate-implementation-spec)

## Tags

[stress-test-scenario-spec, regression-test, gate-3, test-plan, day-arc-2026-05-08, multi-day-pain-point-resolution]
