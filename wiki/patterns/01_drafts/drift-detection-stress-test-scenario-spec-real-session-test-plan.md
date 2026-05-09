---
title: "Drift-Detection Stress-Test Scenario Spec — Real-Session Test Plan"
type: pattern
domain: agent-config
status: synthesized
confidence: high
maturity: seed
authorship: agent-authored
created: 2026-05-08
updated: 2026-05-08
sources:
  - id: drift-detection-implementation-spec
    type: wiki
    file: wiki/patterns/01_drafts/drift-detection-gate-implementation-spec-active-task-anchor-and-scope-sentinel.md
    description: "PRIMARY parent — implementation-spec #6; this stress-test spec expands its REQUIRED-gates pending list"
  - id: stress-testing-as-validation-lesson
    type: wiki
    file: wiki/lessons/01_drafts/stress-testing-as-validation-the-only-way-to-surface-aspirational-vs-operational-gaps.md
    description: "Source lesson — stress-testing-as-validation discipline"
  - id: c13-drift-detection-pattern
    type: wiki
    file: wiki/patterns/01_drafts/active-task-anchor-and-drift-detection-gate-design.md
    description: "Cluster pattern C13 — defines the empirical gap this stress-test set measures"
  - id: correction-shape-stress-test-spec
    type: wiki
    file: wiki/patterns/01_drafts/correction-shape-stress-test-scenario-spec-real-session-test-plan.md
    description: "Sibling stress-test spec #5 — pattern parallels (5-scenario format)"
  - id: composite-compliance-implementation-spec
    type: wiki
    file: wiki/patterns/01_drafts/composite-operational-compliance-metric-implementation-spec-measurement-layer-aggregator.md
    description: "Sibling — composite-compliance metric; this stress-test data is the input"
tags: [stress-test-scenario-spec, drift-detection, gate-6, test-plan, day-arc-2026-05-08, multi-day-pain-point-resolution]
---

# Drift-Detection Stress-Test Scenario Spec — Real-Session Test Plan

## Summary

Per piece #18 (stress-testing-as-validation lesson) + impl-spec #6 (drift-detection gate) REQUIRED-gates pending list, the drift-detection gate operational-compliance is bridged from synthetic to real-session via concrete stress-test scenarios. This piece defines 5 named scenarios — covering active-task-set ceremony + in-scope silent allow + soft-drift warn + hard-drift block + cycle-end audit. Per substitution-pattern Insight 5b: declaring active-task discipline is aspirational without runtime sentinel. This spec closes the test-plan substitution at axis #6.

## Pattern Description

**Stress-test layer**: real-session evidence (per piece #18 evidence-priority tier 2) + operator-empirical confirmation (tier 1). Scenarios derived empirically from cluster C13 pain-point instances. Gate #6 spans 3 hooks: UserPromptSubmit (active-task refresh), PreToolUse (scope-comparison), Stop (cycle-end audit).

### Scenario 1 — active-task-set via slash command

```yaml
scenario_1_active_task_set_via_slash:
  setup:
    - ~/.claude/active-task.json: empty (fresh cycle)
    - operator just typed: "/task set T012"
    - backlog has T012 with paths_in_scope=["install.sh", "tools/setup/"]
  trigger:
    - UserPromptSubmit hook (slash command processed by harness)
  expected:
    - active-task.json populated:
        {
          "task_id": "T012",
          "task_title": "install.sh implementation",
          "task_scope": {
            "paths_in_scope": ["install.sh", "tools/setup/"],
            "paths_explicitly_out": [],
            "edit_pattern_in_scope": "install.sh|tools/setup/.*",
            "tools_in_scope": ["Edit", "Write", "Read", "Bash"]
          },
          "task_set_at": "<ISO>",
          "task_set_by": "operator",
          "operator_verbatim": "/task set T012",
          "drift_event_count": 0,
          "drift_events": []
        }
    - banner: "ACTIVE TASK set to T012 — install.sh implementation. Scope: install.sh, tools/setup/."
  pass_criteria:
    - state-file deterministically written
    - paths_in_scope read from backlog frontmatter
    - banner confirms task-set
    - subsequent edits validated against scope
  edge_cases:
    - T012 doesn't exist in backlog: emit error; do not write state-file
    - operator-stated prose ("let's work on T012"): UserPromptSubmit hook detects task-stating prose; writes state-file with task_set_by="agent-inferred"
    - T012 already done in backlog: warn "task is done; consider new task" + write state-file anyway
```

### Scenario 2 — in-scope silent allow

```yaml
scenario_2_in_scope_silent:
  setup:
    - active-task.json: T012 (paths_in_scope=["install.sh", "tools/setup/"])
  trigger:
    - PreToolUse on Edit `tools/setup/install_helper.py`
  expected:
    - all 4 scope-checks pass
    - silent allow
    - no banner
  pass_criteria:
    - no friction
    - no state-file mutation
  edge_cases:
    - target is install.sh exactly: matches; in-scope
    - target is install.sh.bak (backup file): NOT in paths_in_scope; soft-drift
    - target is tools/setup/ (directory): cannot edit a directory directly; not applicable
```

### Scenario 3 — soft drift (1 scope-check fails)

```yaml
scenario_3_soft_drift_warn:
  setup:
    - active-task.json: T012 (paths_in_scope=["install.sh", "tools/setup/"])
  trigger:
    - PreToolUse on Edit `tools/cycle.py` (NOT in T012 scope but composes with general project)
  expected:
    - CHECK 1 fails: tools/cycle.py not in paths_in_scope
    - CHECKS 2-4 pass (not in explicitly_out, no pattern conflict, tool in_scope)
    - SOFT-DRIFT banner emits:
        "ACTIVE TASK: T012 — install.sh implementation
         EDIT TARGET: tools/cycle.py
         SCOPE-CHECK FAILED: not in paths_in_scope (only 1/4 checks failed = soft drift)
         ASSESSMENT: this MIGHT be in-scope (e.g. compose with active task) OR drift.
         ALLOWED: edit will proceed; logged as soft-drift event."
    - drift_event_count incremented; drift_events appended
  pass_criteria:
    - allow proceeds
    - banner emits
    - drift event recorded in state-file
  edge_cases:
    - operator-explicit cross-task edit ("compose with T015 too"): REASON= bypass with citation; soft-drift suppressed
    - file just outside paths_in_scope by namespace (e.g., tools/lib/util.py): same soft-drift treatment
```

### Scenario 4 — hard drift (2+ scope-checks fail)

```yaml
scenario_4_hard_drift_block:
  setup:
    - active-task.json: T012 (paths_in_scope=["install.sh", "tools/setup/"], paths_explicitly_out=["wiki/log/"])
  trigger:
    - PreToolUse on Write `wiki/log/2026-05-08-foo.md`
  expected:
    - CHECK 1 fails: not in paths_in_scope
    - CHECK 2 fails: matches paths_explicitly_out
    - 2/4 checks fail → HARD-DRIFT banner emits:
        "ACTIVE TASK: T012 — install.sh implementation
         OPERATOR-STATED (sacrosanct): '/task set T012'
         EDIT TARGET: wiki/log/2026-05-08-foo.md
         SCOPE-CHECKS FAILED: paths_in_scope, paths_explicitly_out
         REMEDIATION:
           (a) /task set <new-task-id> if direction changed
           (b) defer this edit; complete T012 first
           (c) compose with T012 — articulate via REASON= bypass."
    - DO NOT execute edit (hard-drift = block by default)
  pass_criteria:
    - hard drift detected without false-positive
    - banner cites operator-verbatim task-statement (sacrosanct)
    - 3 remediation paths explicit
    - bypass mechanism documented
  edge_cases:
    - cycle-end housekeeping (session log, handoff doc, decisions append): whitelisted; hard-drift suppressed
    - emergency edit during /terminate ceremony: REASON= bypass for cross-task spread
    - operator silently re-directs without /task set: detector + soft-drift on first edit; hard-drift on persistence
```

### Scenario 5 — cycle-end drift audit

```yaml
scenario_5_cycle_end_drift_audit:
  setup:
    - active-task.json: T012 with drift_event_count=3 (1 soft + 2 hard accumulated this cycle)
  trigger:
    - Stop hook (end of cycle)
  expected:
    - drift-summary in cycle stamp:
        "drift events this cycle: 3 (hard: 2, soft: 1)"
    - if hard count >= 2: emit recommendation:
        "consider /task set re-anchor — significant cross-task work this cycle"
    - persist drift_events to ~/.claude/drift-history/<cycle-id>.json (audit trail)
  pass_criteria:
    - audit trail JSON deterministic
    - cycle stamp surfaces drift summary
    - recommendation context-aware (hard vs soft thresholds)
  edge_cases:
    - drift_event_count=0: silent (healthy cycle)
    - hard count >= 5 in one cycle: ESCALATE — pattern-recurrence aggregator (impl-spec #11) flags drift-recurrence
    - drift events span dimensions outside active-task: surface as "task-cursor stale"
```

## When To Apply

Apply this stress-test scenario spec when:
- Implementation-spec #6 (drift-detection gate) is being implemented
- /task set slash command + active-task convention operational
- Backlog tasks have paths_in_scope frontmatter or equivalent
- Pain-point cluster C13 axis warrants empirical compliance measurement
- 13-gate pipeline is being implemented (this is axis #6 of 12 stress-test specs)

## Instances

**Instance 1: full stress-test session — operator runs all 5 scenarios**:
- Total time: ~25-35 minutes
- Output: per-scenario pass/fail + axis-level compliance %
- Updates impl-spec #6 REQUIRED-gates: pending → empirically_passed per scenario

**Instance 2: cross-axis composability (drift-detection + stage-class)**:
- Trigger: out-of-scope + wrong-stage edit (e.g., tests/test_x.py during T012 scaffold-stage)
- Expected: BOTH drift-detection (hard-drift) + stage-class (FORBIDDEN) banners stack
- Verifies banner-stacking + per-axis state-file independence

**Instance 3: scenario fails on agent-inferred task-set false-positive**:
- Operator's prompt mentions "T012 reminder" but doesn't intend to set as active-task
- Synthetic test passed; real-session: detector incorrectly writes active-task.json
- Surface root cause: detector pattern matching too broad
- Iterate on impl-spec #6; tune detector

**Instance 4: scenario passes but operator rejects T-id-based scope (prefers semantic)**:
- Per evidence-priority hierarchy: operator-empirical override
- Surface as scope-naming taxonomy revision (per piece C13 follow-up)
- Iterate on dimensional naming convention

## When Not To

- Implementation-spec #6 not yet authored
- Project lacks active-task convention or task-cursor management
- Cold-start sessions before any backlog tasks exist
- /terminate or /finish-smoothly meta-cycles (legitimately span all open work)
- Operator-explicit deferral via REASON= bypass on entire stress-test execution

## Empirical Evidence

Per pain-point cluster C13 in master inventory: 9+ pain-point instances of "agent drifted from stated task scope". The 5 scenarios derive empirically from those instances. The composability test verifies clean stacking with stage-class (sibling axis #7).

## Required Gates (per hook-architecture proposal #2 4th component)

```yaml
required_gates:
  empirically_passed:
    - synthetic_scope_classification: passed 2026-05-08 via mock task+target pairs (12/12)
    - synthetic_drift_classification: passed 2026-05-08 via mock soft+hard scenarios (10/10)
  pending:
    - real_session_scenario_1_active_task_set: pending
    - real_session_scenario_2_in_scope_silent: pending
    - real_session_scenario_3_soft_drift_warn: pending
    - real_session_scenario_4_hard_drift_block: pending
    - real_session_scenario_5_cycle_end_audit: pending
    - composability_with_stage_class: pending
    - operator_empirical_scope_naming_calibration: pending
  composite_compliance: drift-detection-axis stress-test 0% (no real-session executions yet) — target ≥85%
```

## Relationships

- IMPLEMENTS test plan for: implementation-spec #6 (drift-detection-gate-implementation-spec)

## Tags

[stress-test-scenario-spec, drift-detection, gate-6, test-plan, day-arc-2026-05-08, multi-day-pain-point-resolution]
