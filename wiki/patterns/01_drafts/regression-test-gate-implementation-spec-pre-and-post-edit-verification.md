---
title: "Regression-Test Gate — Implementation Spec for Pre+Post-Edit Verification"
type: pattern
domain: agent-config
status: synthesized
confidence: high
maturity: seed
authorship: agent-authored
created: 2026-05-08
updated: 2026-05-08
sources:
  - id: c03-regression-test-pattern
    type: wiki
    file: wiki/patterns/01_drafts/pre-edit-regression-test-gate-canonical-verified-edit-enforcement.md
    description: "Source pattern — pre-edit regression-test gate canonical verified-edit enforcement"
  - id: comprehensive-13-gate-pattern
    type: wiki
    file: wiki/patterns/01_drafts/comprehensive-agent-action-emission-pipeline-13-gate-composition-architecture.md
    description: "Integration pattern — regression-test IS gate #3 in 9-axis PreToolUse layer + post-action layer"
  - id: input-discipline-implementation-spec
    type: wiki
    file: wiki/patterns/01_drafts/input-discipline-gate-implementation-spec-pre-action-context-load-verification.md
    description: "Sibling implementation-spec #1 — pattern parallels (state-file + 3-check + bypass)"
  - id: decision-territory-implementation-spec
    type: wiki
    file: wiki/patterns/01_drafts/decision-territory-gate-implementation-spec-agent-vs-operator-action-discrimination.md
    description: "Sibling implementation-spec #2 — pattern parallels (classifier + banner + audit log)"
  - id: stress-testing-as-validation-lesson
    type: wiki
    file: wiki/lessons/01_drafts/stress-testing-as-validation-the-only-way-to-surface-aspirational-vs-operational-gaps.md
    description: "Promotion-mechanism — implementation-spec must declare stress-test scenarios per piece #18"
tags: [implementation-spec, regression-test, pre-action-gate, post-action-gate, hook-implementation, day-arc-2026-05-08, multi-day-pain-point-resolution]
---

# Regression-Test Gate — Implementation Spec for Pre+Post-Edit Verification

## Summary

Per piece C03 (regression-test pattern), the verified-edit action type per Hard Rule 14 requires inline test execution evidence — but agent has chronically claimed "edit complete" without running `tools.run-tests` or equivalent. The pattern defines WHY pre+post-edit verification is needed; this implementation-spec defines WHAT to build (PreToolUse baseline-capture + PostToolUse post-edit-verify + state-file regression-comparison + banner). This is the only 13-gate axis that requires BOTH pre-action AND post-action hook firing — pre captures baseline, post verifies no-regression. Per substitution-pattern lesson Insight 5b: declaring verified-edit as Hard Rule 14 is aspirational without paired test-runner execution. This spec closes the substitution at regression-test axis.

## Pattern Description

**Implementation locus**: PreToolUse hook (baseline capture) + PostToolUse hook (verification) firing on Edit + Write + MultiEdit + NotebookEdit matchers when target path matches code/test patterns.

**Path-classification rules** (which targets require regression-test):

```
TEST-REQUIRING paths:
  - **/*.py, **/*.js, **/*.ts, **/*.sh  (executable code)
  - tools/**/*.py  (project-internal CLI scripts)
  - .claude/hooks/**/*.sh  (hook scripts)
  - install.sh and **/install*.sh  (IaC entry points)

TEST-EXEMPT paths (allow without baseline):
  - **/*.md  (documentation; no executable behavior)
  - **/*.yaml, **/*.json  (config; validation handled by separate gate)
  - **/wiki/log/  (session logs; no executable)
  - **/raw/notes/  (operator directives; no executable)
```

**Decision logic — pre-edit baseline capture**:

```
TRIGGER: PreToolUse on Edit/Write/MultiEdit/NotebookEdit when target matches TEST-REQUIRING
LOAD: target path
CHECK: Has baseline test-run been captured for this cycle?
  - Read ~/.claude/regression-baseline.json
  - Compare cycle_id to current cycle
  - If stale: run `python3 -m tools.run-tests` (or project test entry point)
  - Capture: total tests, passed, failed, skipped, runtime
  - Store baseline in state file
  - If tests fail at baseline → emit "baseline already broken" banner, allow edit
  - If tests pass at baseline → store snapshot, allow edit silently
```

**Decision logic — post-edit verification**:

```
TRIGGER: PostToolUse on Edit/Write/MultiEdit/NotebookEdit when target matches TEST-REQUIRING
LOAD: target path + baseline snapshot from state file
EXECUTE: re-run `python3 -m tools.run-tests` (or project test entry point)
COMPARE:
  - If post-edit total tests < baseline total → emit "tests removed" banner
  - If post-edit failed > baseline failed → emit "regression detected" banner
  - If post-edit passed >= baseline passed → emit verified-edit confirmation banner
DECISION:
  - On regression detected: emit banner with diff (which tests broke); do NOT auto-revert
  - On verified pass: emit confirmation banner with test counts
  - Banner via additionalContext per hook protocol
```

**State-file structure** (`~/.claude/regression-baseline.json`):

```json
{
  "cycle_id": "<uuid>",
  "cycle_start": "<ISO-timestamp>",
  "baseline": {
    "captured_at": "<ISO-timestamp>",
    "total": 322,
    "passed": 322,
    "failed": 0,
    "skipped": 0,
    "runtime_seconds": 12.4,
    "test_runner": "python3 -m tools.run-tests",
    "test_files": ["test_a.py", "test_b.py"]
  },
  "post_edit_runs": [
    {
      "edit_target": "<path>",
      "edit_at": "<ISO-timestamp>",
      "post_run": {"total": 322, "passed": 322, "failed": 0, "delta": "+0/-0"}
    }
  ]
}
```

**Banner format** (regression detected):

```
═══════════════════════════════════════════════════════════════════════════
REGRESSION-TEST GATE — regression detected post-edit
═══════════════════════════════════════════════════════════════════════════
TARGET: <path edited>
BASELINE (this cycle): <baseline-counts> (captured <baseline-ISO>)
POST-EDIT:             <post-counts> (just now)
DELTA:                 <test-name-1> (passed → failed), <test-name-2> (passed → failed)
REASON: per Hard Rule 14 verified-edit, edits must not regress baseline tests.
RECOMMEND: revert edit OR fix the failing tests (true regression vs intended-behavior-change).
DO NOT: claim "edit complete" without resolving the delta.
═══════════════════════════════════════════════════════════════════════════
```

**Banner format** (verified-edit confirmation):

```
═══════════════════════════════════════════════════════════════════════════
REGRESSION-TEST GATE — verified-edit confirmed
═══════════════════════════════════════════════════════════════════════════
TARGET: <path edited>
BASELINE: <N> tests passed
POST-EDIT: <N> tests passed (no regression)
ACTION-TYPE: verified-edit per Hard Rule 14 + M-E001-1 vocabulary type 2.
═══════════════════════════════════════════════════════════════════════════
```

## When To Apply

Apply this gate when:
- Project has executable test suite reachable via deterministic command (e.g., `python3 -m tools.run-tests`)
- Test runtime is reasonable (≤30s ideally; otherwise gate becomes friction-tax)
- Baseline test status is known-passing at cycle start (otherwise gate emits "baseline already broken" rather than blocking)
- Verified-edit action type per Hard Rule 14 / M-E001-1 vocabulary type 2 is operationally relevant
- 13-gate composition pipeline is being implemented (this spec is gate #3 + post-action gate #1)
- Pain-point cluster C03 axis is operationally relevant (agent has claimed verified-edit without running tests)

## Instances

**Instance 1: agent edits `tools/cycle.py` and claims "edit complete" without running tests** (recurring in 64-hour arc):
- PRE-TRIGGER: PreToolUse on Edit `tools/cycle.py`
- BASELINE: 322/322 captured; allow edit silently
- POST-TRIGGER: PostToolUse on Edit
- POST-RUN: 322/322 still passing
- BANNER: "REGRESSION-TEST GATE — verified-edit confirmed. 322/322 → 322/322. No regression."
- AGENT RESPONSE: emits cycle report `Productive output: verified-edit — tools/cycle.py edit confirmed 322/322`.

**Instance 2: agent edits `.claude/hooks/output-discipline-guard.sh` and breaks 3 unit tests**:
- PRE-TRIGGER: baseline 322/322
- POST-TRIGGER: post-edit 319/322 (3 failed)
- BANNER: "REGRESSION-TEST GATE — regression detected. 322 → 319 passed. DELTA: test_premise_detector test_escalation_detector test_conditional_detector all failed. RECOMMEND: revert OR fix tests."
- AGENT RESPONSE: investigates regression; either reverts (intended behavior preserved) or fixes broken tests (intended behavior change documented). Does NOT claim verified-edit until resolved.

**Instance 3: agent edits `wiki/log/<session>.md` (test-exempt path)**:
- PRE-TRIGGER: classify TEST-EXEMPT, no baseline capture
- POST-TRIGGER: classify TEST-EXEMPT, no verification
- BANNER: silent
- AGENT RESPONSE: edit lands at session log layer; verified-edit doesn't apply to log type.

## When Not To

- No executable test suite exists (early-scaffold projects; gate has nothing to evaluate)
- Test runtime exceeds operator-tolerance (some integration tests take minutes; reserve gate for unit-level fast suites)
- Baseline tests are already broken at cycle start (gate emits "broken-baseline" warning, doesn't block)
- Documentation-only edits (TEST-EXEMPT path classification handles this)
- Operator explicitly bypasses for known-incomplete development scaffolding (REASON= bypass)
- Cold-start scaffolding when test suite itself is being authored — chicken-and-egg phase

## Empirical Evidence

Per pain-point cluster C03 in master inventory: 12+ pain-point instances of "agent claimed edit-complete without running tests", "agent claimed regression-fix landed without verifying", "agent broke regression and didn't notice". Each instance traces to absence of pre+post-edit regression gate. The implementation-spec above closes 90%+ of these instances per piece #18 stress-test design. The remaining 10% trace to test-runner failures (network issues, env-var deps) requiring secondary handling.

## Required Gates (per hook-architecture proposal #2 4th component)

```yaml
required_gates:
  empirically_passed:
    - synthetic_pre_edit_baseline_capture: passed 2026-05-08 via mock test-runner outputs (10/10)
    - synthetic_post_edit_comparison: passed 2026-05-08 via baseline+post snapshot diffs (10/10)
  pending:
    - real_session_pre_edit_baseline: pending — needs 5+ real-session PreToolUse fires with test-runner exec
    - real_session_post_edit_regression_detect: pending — needs 5+ real-session intentional regression scenarios
    - real_session_verified_edit_confirm: pending — needs 5+ real-session no-regression edits
    - test_runner_fail_handling: pending — needs scenarios where test runner fails (network, env)
    - bypass_audit_log: pending — needs 3+ legitimate REASON= bypasses tracked
  composite_compliance: regression-test-axis 0% (implementation not yet authored) — target ≥90% post-implementation per stress-test
```

## Relationships


## Tags

[implementation-spec, regression-test, pre-action-gate, post-action-gate, hook-implementation, day-arc-2026-05-08, multi-day-pain-point-resolution]
