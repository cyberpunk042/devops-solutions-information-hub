---
title: "Stage-Class Stress-Test Scenario Spec — Real-Session Test Plan"
type: pattern
domain: agent-config
status: synthesized
confidence: high
maturity: seed
authorship: agent-authored
created: 2026-05-08
updated: 2026-05-08
sources:
  - id: stage-class-implementation-spec
    type: wiki
    file: wiki/patterns/01_drafts/stage-class-gate-implementation-spec-methodology-edit-land-enforcement.md
    description: "PRIMARY parent — implementation-spec #7; this stress-test spec expands its REQUIRED-gates pending list"
  - id: stress-testing-as-validation-lesson
    type: wiki
    file: wiki/lessons/01_drafts/stress-testing-as-validation-the-only-way-to-surface-aspirational-vs-operational-gaps.md
    description: "Source lesson — stress-testing-as-validation discipline"
  - id: c10-stage-class-pattern
    type: wiki
    file: wiki/patterns/01_drafts/methodology-stage-gate-edit-land-enforcement-design.md
    description: "Cluster pattern C10 — defines the empirical gap this stress-test set measures"
  - id: methodology-standardize-proposal
    type: wiki
    file: wiki/log/2026-05-08-standardize-extension-proposal-methodology-stage-class-enforcement-extension.md
    description: "Sibling standardize proposal #3 — methodology rule extension; this stress-test spec validates the paired enforcement"
  - id: drift-detection-stress-test-spec
    type: wiki
    file: wiki/patterns/01_drafts/drift-detection-stress-test-scenario-spec-real-session-test-plan.md
    description: "Sibling stress-test spec #6 — pattern parallels (5-scenario format)"
tags: [stress-test-scenario-spec, stage-class, gate-7, test-plan, day-arc-2026-05-08, multi-day-pain-point-resolution]
---

# Stage-Class Stress-Test Scenario Spec — Real-Session Test Plan

## Summary

Per piece #18 (stress-testing-as-validation lesson) + impl-spec #7 (stage-class gate) REQUIRED-gates pending list, the stage-class gate operational-compliance is bridged from synthetic to real-session via concrete stress-test scenarios. This piece defines 5 named scenarios — covering document-stage forbidden-block + scaffold-stage allowed + implement-stage test-block + boundary-warn + cross-stage bypass. Per substitution-pattern Insight 5b: methodology stage-gates documented in /root/.claude/rules/methodology.md without paired hook enforcement IS substitution at methodology layer. This spec closes the test-plan substitution at axis #7.

## Pattern Description

**Stress-test layer**: real-session evidence (per piece #18 evidence-priority tier 2) + operator-empirical confirmation (tier 1). Scenarios derived empirically from cluster C10 pain-point instances (13+ stage-class violations during 64-hour /root failed-conversation arc).

### Scenario 1 — document-stage forbidden block (implementation forbidden)

```yaml
scenario_1_document_stage_implementation_block:
  setup:
    - active-task.json: { task_id: "T-foo", task_stage: "document" }
    - methodology.yaml document-stage FORBIDDEN: ["tests/", "src/", "**/*.py implementation", "install.sh"]
  trigger:
    - PreToolUse on Write `src/feature.py` (implementation file in document-stage task)
  expected:
    - LOOKUP current_stage = "document" (SOURCE 1: active-task.json)
    - MATCH src/feature.py against document-stage FORBIDDEN
    - BLOCK + emit stage-violation banner:
        "ACTIVE TASK: T-foo
         CURRENT STAGE: document (0-25% readiness)
         EDIT TARGET: src/feature.py
         VIOLATION: target matches FORBIDDEN pattern for document stage
         REMEDIATION:
           - Wrong stage? Verify current_stage; advance via gate command
           - Wrong target? Defer until stage advances
           - Composition unclear? REASON= bypass with articulation"
    - audit log appended to ~/.claude/hooks/stage-class-violation.log
  pass_criteria:
    - action does NOT execute (stage-class deny is structural per CLAUDE.md Hard Rule 6)
    - banner emits BEFORE Write
    - audit log entry deterministic
    - agent-natural response: defer + author new task at appropriate stage
  edge_cases:
    - target is .py.bak (backup): not in FORBIDDEN; allow
    - target is doc/example.py (documentation Python example, not src): not in FORBIDDEN; allow
    - operator says "skip stage-class for now": REASON= bypass with citation; logged
```

### Scenario 2 — scaffold-stage allowed (type-defs, schema, test-stubs)

```yaml
scenario_2_scaffold_stage_allowed:
  setup:
    - active-task.json: { task_id: "T-bar", task_stage: "scaffold" }
    - methodology.yaml scaffold-stage ALLOWED: ["type-defs", "schema", "test-stubs", "config-files"]
  trigger:
    - PreToolUse on Write `tools/types.py` (TypedDict definitions)
  expected:
    - LOOKUP current_stage = "scaffold"
    - MATCH tools/types.py: type-defs allowed
    - silent allow
    - no banner
  pass_criteria:
    - allow with no friction
    - subsequent test-stub Write (test_*.py with pytest.skip): also allowed
    - subsequent implementation Write (real assertions): would be FORBIDDEN
  edge_cases:
    - test-stub WITHOUT pytest.skip marker: ambiguous (boundary); SOFT-WARN
    - target is yaml schema: matches schema ALLOWED pattern
    - target is .ts file (TypeScript): same scaffold semantics; allow if matches type-def pattern
```

### Scenario 3 — implement-stage forbidden (new test files)

```yaml
scenario_3_implement_stage_test_block:
  setup:
    - active-task.json: { task_id: "T-baz", task_stage: "implement" }
    - methodology.yaml implement-stage FORBIDDEN: ["new test files"]
  trigger:
    - PreToolUse on Write `tests/test_baz.py` (new test file during implement stage)
  expected:
    - LOOKUP current_stage = "implement"
    - MATCH tests/test_baz.py: new test files FORBIDDEN
    - BLOCK + emit stage-violation banner:
        "implement stage forbids new test files; tests authored at test stage."
  pass_criteria:
    - block fires
    - banner suggests test stage advancement
    - cycle stamp action-type: NOT verified-edit; flagged as stage-violation
  edge_cases:
    - editing EXISTING test file (not creating new): not FORBIDDEN; allow
    - new test file with pytest.skip during implement (transitional): SOFT-WARN
    - test-stage gate already passed (test stage entered): allow new test files
```

### Scenario 4 — boundary stage-uncertainty (SOFT-WARN)

```yaml
scenario_4_stage_boundary_softwarn:
  setup:
    - active-task.json: { task_id: "T-qux", task_stage: "design" }
    - design-stage ALLOWED: ["wiki/", "design/", "ADR-*.md", "tech-spec-*.md"]
    - design-stage FORBIDDEN: ["tests/", "src/", "**/*.py implementation"]
  trigger:
    - PreToolUse on Edit `tools/utils.py` (neither in ALLOWED nor explicit FORBIDDEN for design)
  expected:
    - LOOKUP current_stage = "design"
    - MATCH tools/utils.py: not in ALLOWED, not in explicit FORBIDDEN
    - SOFT-WARN banner:
        "ACTIVE TASK: T-qux | CURRENT STAGE: design
         EDIT TARGET: tools/utils.py
         ASSESSMENT: target neither in ALLOWED nor FORBIDDEN — boundary case.
         May indicate stage-taxonomy gap OR legitimate cross-stage edit."
    - allow proceed; log boundary event
  pass_criteria:
    - SOFT-WARN does not block
    - banner suggests taxonomy review
    - boundary event logged for offline review
  edge_cases:
    - boundary count >= 5 in cycle: ESCALATE to recommendation "stage taxonomy needs revision"
    - operator clarifies via /task set with stage-update: state-file refresh; gate behavior shifts
```

### Scenario 5 — cross-stage bypass with articulation

```yaml
scenario_5_cross_stage_bypass:
  setup:
    - active-task.json: { task_id: "T-foo", task_stage: "document" }
    - operator just said: "compose this doc with the impl helper for clarity; cross-stage but justified"
    - REASON="cross-stage-doc-impl-clarity-2026-05-08-14:14"
  trigger:
    - PreToolUse on Edit `src/feature.py` with REASON= set (would normally be document-stage FORBIDDEN)
  expected:
    - REASON= bypass detected
    - banner suppressed
    - audit log captures BOTH stage-violation pattern AND bypass reason:
        {"timestamp": "<ISO>", "stage": "document", "target": "src/feature.py",
         "violation_type": "forbidden", "matched_pattern": "src/", "bypass_reason": "cross-stage-doc-impl-clarity..."}
    - allow action
  pass_criteria:
    - bypass works without banner
    - audit log entry deterministic + complete (BOTH violation AND bypass captured)
    - agent's response notes bypass + cites operator-grant in cycle stamp
  edge_cases:
    - REASON= without justification text: emit "weak bypass" warning + still allow
    - bypass repeated 3+ in cycle: pattern-recurrence aggregator (impl-spec #11) flags
    - bypass for stage UPGRADE (operator says "advance to implement"): use /task set --stage implement instead
```

## When To Apply

Apply this stress-test scenario spec when:
- Implementation-spec #7 (stage-class gate) is being implemented
- Methodology engine (methodology.yaml) provides authoritative stage definitions
- Active-task convention with current_stage field is operational
- Pain-point cluster C10 axis warrants empirical compliance measurement
- 13-gate pipeline is being implemented (this is axis #7 of 12 stress-test specs)

## Instances

**Instance 1: full stress-test session — operator runs all 5 scenarios**:
- Total time: ~30-40 minutes (5 stages + boundary + bypass coverage)
- Output: per-scenario pass/fail + axis-level compliance %
- Updates impl-spec #7 REQUIRED-gates: pending → empirically_passed per scenario

**Instance 2: cross-axis composability (stage-class + drift-detection)**:
- Trigger: out-of-stage + out-of-scope edit (e.g., tests/test_x.py during T-foo document-stage)
- Expected: BOTH stage-class (FORBIDDEN BLOCK) + drift-detection (hard-drift) banners stack
- Verifies banner-stacking + per-axis state-file independence

**Instance 3: scenario fails on stage-pattern false-positive**:
- doc/example.py classified as src/*.py FORBIDDEN (wrong)
- Surface root cause: pattern matching too broad (`*.py` matched dir-agnostically)
- Iterate on impl-spec #7 — tighten path glob

**Instance 4: scenario passes but operator wants softer enforcement (SOFT-WARN instead of BLOCK)**:
- Per evidence-priority hierarchy: operator-empirical override
- Surface as enforcement-tier calibration (per principle #3 strictness graduation)
- Iterate on stage-class enforcement strictness (Strict → Enforced softer)

## When Not To

- Implementation-spec #7 not yet authored
- Project lacks methodology engine (early-scaffold; no yaml)
- Tasks without `current_stage` frontmatter (chicken-and-egg)
- Hotfix or emergency mode (stage gate temporarily relaxed)
- Project using non-stage-gated methodology profile (e.g., simplified)

## Empirical Evidence

Per pain-point cluster C10 in master inventory: 13+ pain-point instances of "agent edited tests in implement stage, agent wrote implementation in document stage". The 5 scenarios derive empirically from those instances. The composability test verifies clean stacking with drift-detection (sibling axis #6).

## Required Gates (per hook-architecture proposal #2 4th component)

```yaml
required_gates:
  empirically_passed:
    - synthetic_per_stage_classifier: passed 2026-05-08 via mock task+target+stage scenarios (15/15)
  pending:
    - real_session_scenario_1_document_block: pending
    - real_session_scenario_2_scaffold_allow: pending
    - real_session_scenario_3_implement_test_block: pending
    - real_session_scenario_4_boundary_softwarn: pending
    - real_session_scenario_5_cross_stage_bypass: pending
    - composability_with_drift_detection: pending
    - composability_with_regression_test: pending
    - methodology_yaml_integration: pending — depends on engine config availability
    - operator_empirical_strictness_calibration: pending
  composite_compliance: stage-class-axis stress-test 0% (no real-session executions yet) — target ≥90%
```

## Relationships

- IMPLEMENTS test plan for: implementation-spec #7 + standardize proposal #3 (methodology rule extension) — pair-validation

## Tags

[stress-test-scenario-spec, stage-class, gate-7, test-plan, day-arc-2026-05-08, multi-day-pain-point-resolution]
