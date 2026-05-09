---
title: "Correction-Shape Stress-Test Scenario Spec — Real-Session Test Plan"
type: pattern
domain: agent-config
status: synthesized
confidence: high
maturity: seed
authorship: agent-authored
created: 2026-05-08
updated: 2026-05-08
sources:
  - id: correction-shape-implementation-spec
    type: wiki
    file: wiki/patterns/01_drafts/correction-shape-gate-implementation-spec-one-notch-vs-extreme-swing-detection.md
    description: "PRIMARY parent — implementation-spec #5; this stress-test spec expands its REQUIRED-gates pending list"
  - id: stress-testing-as-validation-lesson
    type: wiki
    file: wiki/lessons/01_drafts/stress-testing-as-validation-the-only-way-to-surface-aspirational-vs-operational-gaps.md
    description: "Source lesson — stress-testing-as-validation discipline"
  - id: c08-correction-shape-pattern
    type: wiki
    file: wiki/patterns/01_drafts/correction-as-calibration-pre-edit-verification-gate-design.md
    description: "Cluster pattern C08 — defines the empirical gap this stress-test set measures"
  - id: severity-stress-test-spec
    type: wiki
    file: wiki/patterns/01_drafts/severity-blast-radius-stress-test-scenario-spec-real-session-test-plan.md
    description: "Sibling stress-test spec #4 — pattern parallels (5-scenario format)"
  - id: composite-compliance-implementation-spec
    type: wiki
    file: wiki/patterns/01_drafts/composite-operational-compliance-metric-implementation-spec-measurement-layer-aggregator.md
    description: "Sibling — composite-compliance metric; this stress-test data is the input"
tags: [stress-test-scenario-spec, correction-shape, gate-5, test-plan, day-arc-2026-05-08, multi-day-pain-point-resolution]
---

# Correction-Shape Stress-Test Scenario Spec — Real-Session Test Plan

## Summary

Per piece #18 (stress-testing-as-validation lesson) + impl-spec #5 (correction-shape gate) REQUIRED-gates pending list, the correction-shape gate operational-compliance is bridged from synthetic to real-session via concrete stress-test scenarios. This piece defines 5 named scenarios — covering UserPromptSubmit correction-detection + PreToolUse extreme-swing-block + one-notch confirmation + sacrosanct-verbatim preservation + bypass paths. Per substitution-pattern Insight 5b: principle #12b going-to-extremes pre-flight check is canonical at /root operating-principles.md but operationally aspirational without runtime sentinel. This spec closes the test-plan substitution at axis #5.

## Pattern Description

**Stress-test layer**: real-session evidence (per piece #18 evidence-priority tier 2) + operator-empirical confirmation (tier 1). Scenarios derived empirically from cluster C08 pain-point instances (statusline cascade SB-093 etc). Gate #5 is dual-hook: UserPromptSubmit captures correction signal, PreToolUse consults state-file at next edit attempt.

### Scenario 1 — correction signal detection + state-file write

```yaml
scenario_1_correction_detection:
  setup:
    - active-correction.json: empty (no pending correction)
    - prior agent action (this cycle): "suppressed the statusline render entirely"
    - operator just typed: "WTF you went to the other extreme — render that but minimize it"
  trigger:
    - UserPromptSubmit hook on operator's prompt
  expected:
    - DETECTOR matches: negative-affect markers ("WTF") + correction-of-prior-edit ("you went to the other extreme")
    - ~/.claude/active-correction.json written:
        {
          "correction_id": "<uuid>",
          "correction_at": "<ISO>",
          "operator_verbatim": "WTF you went to the other extreme — render that but minimize it",
          "dimension_corrected": "statusline-render",
          "prior_position": {"value": "suppressed", "timestamp": "<earlier-ISO>"},
          "direction_demanded": "render-but-minimize",
          "consecutive_corrections_count": 1,
          "resolution_status": "pending"
        }
    - banner emits via additionalContext:
        "CORRECTION DETECTED — next edit on dimension 'statusline-render' must be one-notch
         from 'suppressed' toward 'render-but-minimize', not opposite-extreme."
  pass_criteria:
    - operator_verbatim preserved sacrosanct (per words-are-sacrosanct rule)
    - dimension_corrected inferred correctly (or operator-stated explicitly)
    - state-file deterministically written
    - banner emits during current cycle (informational; gates next edit)
  edge_cases:
    - operator's correction has no negative-affect markers but explicit redirection: still detected (correction-of-prior-edit subdetector)
    - operator's correction is ambiguous: write state-file with `dimension_corrected: "<unclear>"`; banner suggests operator-clarification
    - prior_position unknown (state-file empty across cycle boundary): infer from cycle-history; mark as inferred
```

### Scenario 2 — extreme-swing detected (BLOCK on next edit attempt)

```yaml
scenario_2_extreme_swing_block:
  setup:
    - active-correction.json: as-written by Scenario 1 (dimension="statusline-render", direction="render-but-minimize")
    - agent's next edit attempts: full-render statusline (all rows, verbose; opposite of suppressed)
  trigger:
    - PreToolUse on Edit ~/.claude/hooks/end-of-cycle-stamp.sh
  expected:
    - LOAD active-correction.json
    - COMPARE proposed edit's effect to prior_position
    - DETECT: opposite-extreme (suppressed → all-rendered)
    - BLOCK: emit EXTREME-SWING banner via additionalContext:
        "ACTIVE CORRECTION (per operator <ISO>): 'WTF you went to the other extreme...'
         DIMENSION: statusline-render
         PRIOR POSITION: suppressed
         PROPOSED EDIT: all-render (opposite-extreme)
         REMEDIATION: identify the middle. Move ONE notch toward render-but-minimize.
         BYPASS: REASON= if operator-explicit-extreme."
  pass_criteria:
    - banner emits BEFORE Edit tool executes
    - banner cites operator's verbatim correction (sacrosanct)
    - banner suggests middle position
    - cycle stamp action-type: NOT verified-edit; flagged as correction-pending
  edge_cases:
    - extreme-swing detection ambiguous: emit "uncertainty banner" (not BLOCK); recommend operator-clarification
    - prior_position empty (no baseline): cannot detect extreme; allow with "no baseline" warning
    - bypass with REASON="operator-explicit-extreme-2026-05-08": allow + log to bypass-history
```

### Scenario 3 — one-notch confirmation (allow with positive feedback)

```yaml
scenario_3_one_notch_confirm:
  setup:
    - active-correction.json: as-written (direction="render-but-minimize")
    - agent's next edit: render statusline with horizontal compact layout (one notch toward render, NOT all-render)
  trigger:
    - PreToolUse on Edit
  expected:
    - LOAD active-correction.json
    - COMPARE: proposed edit is graduated step (suppressed → compact-render, NOT all-render)
    - DETECT: one-notch
    - emit one-notch confirmation banner:
        "DIMENSION: statusline-render
         PRIOR: suppressed
         NEW: compact-render
         DELTA: one-notch toward render-but-minimize
         ACTION: allowed; correction-state will be marked resolved-one-notch on PostToolUse."
    - allow edit
  trigger_post:
    - PostToolUse on Edit
  expected_post:
    - update active-correction.json: resolution_status="resolved-one-notch"
    - move state-file to ~/.claude/correction-history/<correction_id>.json (audit trail)
    - clear active-correction.json
  pass_criteria:
    - one-notch correctly classified vs extreme
    - allow-with-feedback banner emits (positive, not blocking)
    - resolution lifecycle: pending → resolved-one-notch → archived
  edge_cases:
    - subsequent edit on SAME dimension: cleared state-file means no further banner unless operator corrects again
    - subsequent edit on DIFFERENT dimension: separate active-correction lifecycle
    - operator's correction was actually about a DIFFERENT thing than what agent inferred: agent's resolution invalid; subsequent operator correction increments consecutive_corrections_count
```

### Scenario 4 — sacrosanct verbatim preservation (no paraphrase contamination)

```yaml
scenario_4_sacrosanct_verbatim:
  setup:
    - operator typed: "stop doing that fucking trash and just keep it minimal"
    - DETECTOR matches: negative-affect ("fucking trash") + correction signal
  trigger:
    - UserPromptSubmit hook
  expected:
    - operator_verbatim preserved EXACTLY: "stop doing that fucking trash and just keep it minimal"
    - NOT paraphrased to: "operator wants minimal" or "operator rejected the verbose approach"
    - dimension_corrected: inferred + flagged as inference (operator didn't name dimension)
    - direction_demanded: "minimal"
  pass_criteria:
    - state-file's operator_verbatim field exactly matches operator's input (no truncation, no rephrase)
    - subsequent banners cite this verbatim text directly
    - per words-are-sacrosanct rule: "operator words MUST quote verbatim, never paraphrase"
  edge_cases:
    - operator's prompt is very long (>2000 chars): preserve full text in state-file; cite first 200 chars in banner with "(see state-file for full)"
    - operator's prompt has special chars (unicode, control codes): preserve literally; escape only at JSON serialization boundary
    - operator types in non-ASCII (e.g., French accents, emoji): preserve unicode-cleanly
```

### Scenario 5 — circuit-breaker escalation (consecutive_corrections ≥ 3)

```yaml
scenario_5_circuit_breaker_escalation:
  setup:
    - active-correction.json: consecutive_corrections_count=2 (this is 3rd correction)
    - operator's 3rd correction: "STILL WRONG. JUST STOP."
  trigger:
    - UserPromptSubmit hook
  expected:
    - DETECTOR fires; consecutive_corrections_count → 3
    - AUTO-ESCALATE per piece #13 iteration-circuit-breaker:
        write ~/.claude/circuit-breaker-pending.flag for dimension D
    - banner emits ESCALATION variant:
        "CIRCUIT-BREAKER triggered per piece #13 — 3 consecutive corrections on dimension <D>.
         BLOCK next iteration of same correction-target until operator clarifies.
         RECOMMEND: ask operator explicitly what they want this to be."
  trigger_next_pretooluse:
    - any next PreToolUse on Edit on dimension D's target file
  expected_block:
    - circuit-breaker-pending.flag detected
    - BLOCK + emit "CIRCUIT-BREAKER active for dimension D. Surface to operator before iterating."
  pass_criteria:
    - escalation triggers at exactly the 3rd correction (not before)
    - flag deterministically written
    - subsequent edits on same dimension blocked until operator-clarification
    - operator-clarification clears flag (e.g., operator types: "OK, do it as <specific>; circuit-break clear")
  edge_cases:
    - dimension switches mid-cycle (operator corrects A, then corrects B): each dimension has separate counter
    - 3 corrections on different dimensions (A, B, C): no escalation; per-dimension counters
    - operator-explicit "I'm not correcting": state-file rolls back; consecutive_corrections decrements
```

## When To Apply

Apply this stress-test scenario spec when:
- Implementation-spec #5 (correction-shape gate) is being implemented
- UserPromptSubmit hook + PreToolUse hook events are operational
- Sacrosanct-verbatim preservation pattern is established (state-file convention)
- Pain-point cluster C08 axis warrants empirical compliance measurement
- 13-gate pipeline is being implemented (this is axis #5 of 12 stress-test specs)
- Words-are-sacrosanct rule is in force (verbatim preservation matters)

## Instances

**Instance 1: full stress-test session — operator runs all 5 scenarios**:
- Total time: ~30-40 minutes (correction-detection requires careful setup)
- Output: per-scenario pass/fail + axis-level compliance %
- Updates impl-spec #5 REQUIRED-gates: pending → empirically_passed per scenario

**Instance 2: cross-axis composability (correction-shape + severity)**:
- Trigger: extreme-swing on T1-target file (e.g., reversing settings.json deletion)
- Expected: BOTH severity (T2 WARN) + correction-shape (extreme-swing BLOCK) emit
- Verifies banner-stacking + per-axis state-file independence

**Instance 3: scenario fails on negative-affect false-positive**:
- Operator types: "this is so cool, I love what you did" (positive feedback)
- Synthetic test passed; real-session: detector incorrectly classifies as correction
- Surface root cause: detector pattern matching on "wow" or "what you did" too broadly
- Iterate on impl-spec #5; tune detector

**Instance 4: scenario passes but dimension-naming is unclear**:
- Operator's correction is ambiguous; agent infers wrong dimension
- One-notch banner emits but for wrong dimension; agent ships wrong edit
- Surface as dimension-taxonomy gap (per piece C08 follow-up); operator iterates on dimension naming

## When Not To

- Implementation-spec #5 not yet authored
- Project lacks UserPromptSubmit + PreToolUse hook events
- No prior-position tracking (cold-start; first cycle of session)
- Read-only operations (no edit-shape to evaluate)
- Operator explicitly directed extreme (REASON= bypass with citation)
- Sacrosanct-verbatim discipline not in force (rare; would undermine state-file integrity)

## Empirical Evidence

Per pain-point cluster C08 in master inventory: 11+ pain-point instances of "agent went to the other extreme after correction" (statusline cascade SB-093 etc). The 5 scenarios derive empirically from those instances. Without these scenarios, axis-level operational compliance is undefined; with them, axis #5 compliance is measurable per piece #18.

## Required Gates (per hook-architecture proposal #2 4th component)

```yaml
required_gates:
  empirically_passed:
    - synthetic_correction_signal_detection: passed 2026-05-08 via mock prompt set (10/10)
    - synthetic_extreme_swing_classifier: passed 2026-05-08 via mock pair scenarios (12/12)
  pending:
    - real_session_scenario_1_correction_detection: pending
    - real_session_scenario_2_extreme_swing_block: pending
    - real_session_scenario_3_one_notch_confirm: pending
    - real_session_scenario_4_sacrosanct_verbatim: pending
    - real_session_scenario_5_circuit_breaker_escalation: pending
    - composability_with_severity: pending
    - dimension_naming_taxonomy_calibration: pending — depends on operator-iteration of dimension naming
  composite_compliance: correction-shape-axis stress-test 0% (no real-session executions yet) — target ≥85%
```

## Relationships

- IMPLEMENTS test plan for: implementation-spec #5 (correction-shape-gate-implementation-spec)

## Tags

[stress-test-scenario-spec, correction-shape, gate-5, test-plan, day-arc-2026-05-08, multi-day-pain-point-resolution]
