---
title: "Post-Compact Orientation Stress-Test Scenario Spec — Real-Session Test Plan"
type: pattern
domain: agent-config
status: synthesized
confidence: high
maturity: seed
authorship: agent-authored
created: 2026-05-08
updated: 2026-05-08
sources:
  - id: post-compact-implementation-spec
    type: wiki
    file: wiki/patterns/01_drafts/post-compact-orientation-gate-implementation-spec-handoff-and-mirror-enforcement.md
    description: "PRIMARY parent — implementation-spec #10; this stress-test spec expands its REQUIRED-gates pending list"
  - id: stress-testing-as-validation-lesson
    type: wiki
    file: wiki/lessons/01_drafts/stress-testing-as-validation-the-only-way-to-surface-aspirational-vs-operational-gaps.md
    description: "Source lesson — stress-testing-as-validation discipline"
  - id: c05-postcompact-pattern
    type: wiki
    file: wiki/patterns/01_drafts/post-compact-orientation-mirror-and-handoff-doc-completeness-gate.md
    description: "Cluster pattern C05 — defines the empirical gap this stress-test set measures"
  - id: semantic-conflation-stress-test-spec
    type: wiki
    file: wiki/patterns/01_drafts/semantic-conflation-stress-test-scenario-spec-real-session-test-plan.md
    description: "Sibling stress-test spec #9 — pattern parallels (5-scenario format)"
  - id: composite-compliance-implementation-spec
    type: wiki
    file: wiki/patterns/01_drafts/composite-operational-compliance-metric-implementation-spec-measurement-layer-aggregator.md
    description: "Sibling — composite-compliance metric; this stress-test data is the input"
tags: [stress-test-scenario-spec, post-compact, lifecycle-event-gate, test-plan, day-arc-2026-05-08, multi-day-pain-point-resolution]
---

# Post-Compact Orientation Stress-Test Scenario Spec — Real-Session Test Plan

## Summary

Per piece #18 (stress-testing-as-validation lesson) + impl-spec #10 (post-compact orientation gate) REQUIRED-gates pending list, the post-compact lifecycle-event gate operational-compliance is bridged from synthetic to real-session via concrete stress-test scenarios. This piece defines 5 named scenarios — covering PreCompact handoff auto-write + PostCompact orientation banner + first-action-must-be-orient enforcement + handoff completeness validation + bypass paths. Per substitution-pattern Insight 5b: declaring "compaction is a reset event" is aspirational without runtime hooks executing the pre+post-compact ceremonies. This spec closes the test-plan substitution at the lifecycle-event layer.

## Pattern Description

**Stress-test layer**: real-session evidence + operator-empirical confirmation. Scenarios derived empirically from cluster C05 pain-point instances (state-loss across compactions). Gate #10 spans 3 hooks: PreCompact (handoff validation/auto-write) + PostCompact (orientation banner + flag write) + PreToolUse (first-action enforcement).

### Scenario 1 — PreCompact handoff auto-write (no prior handoff this cycle)

```yaml
scenario_1_precompact_auto_handoff:
  setup:
    - cycle in progress; substantial work this cycle (multiple edits)
    - no /handoff slash command invoked this cycle
    - context budget approaching auto-compaction threshold
    - state files populated:
        active-mission, active-focus, active-impediment, active-task,
        active-priorities (no active-correction pending)
  trigger:
    - PreCompact event (auto-triggered by harness)
  expected:
    - VALIDATION: handoff doc not written this cycle
    - AUTO-WRITE: deterministic state snapshot to wiki/log/<ISO>-pre-compact-handoff.md
    - REQUIRED FIELDS populated:
        - active-mission (from state-file)
        - active-focus
        - active-impediment
        - active-task
        - active-priorities
        - operator-pending-decisions (from blockers tracker)
        - recent-operator-verbatim (last 3-5 sacrosanct quotes)
        - in-flight work-items
        - cycle-context-summary
    - additionalContext emit: "PRE-COMPACT — handoff doc <path> contains state snapshot."
  pass_criteria:
    - handoff doc deterministically written
    - all REQUIRED FIELDS present (no missing data)
    - state-files preserved (compaction destroys conversation, not state-files)
    - subsequent PostCompact discovers this handoff doc
  edge_cases:
    - handoff doc auto-write fails (disk full, perm error): emit error; allow compaction with warning
    - state-files missing some fields (cold-start): handoff captures what exists; flags missing
    - handoff doc already written same minute (rapid re-compact): append rather than overwrite
```

### Scenario 2 — PostCompact orientation banner + flag write

```yaml
scenario_2_postcompact_orientation:
  setup:
    - PreCompact already handled (Scenario 1 completed)
    - compaction collapsed conversation prose
    - latest handoff doc: wiki/log/2026-05-08T14:22-pre-compact-handoff.md
  trigger:
    - PostCompact event (auto-triggered by harness)
  expected:
    - DISCOVER latest handoff doc via Glob algorithm
    - emit additionalContext (compulsory):
        "POST-COMPACT — context reset; orientation required.
         REQUIRED ACTIONS:
           1. Invoke /orient
           2. Read handoff doc: wiki/log/2026-05-08T14:22-pre-compact-handoff.md
           3. Re-read state files
           4. Verify cycle continues from prior trajectory
           5. Acknowledge to operator"
    - ALSO write ~/.claude/post-compact-pending-orient.flag with timestamp
  pass_criteria:
    - banner emits in PostCompact additionalContext
    - flag deterministically written
    - subsequent PreToolUse hook can detect flag
  edge_cases:
    - no handoff doc exists (cold-start compaction): banner says "no prior handoff; orient from cold-start"
    - handoff doc auto-discovery returns multiple candidates: pick most-recent ISO timestamp
    - handoff doc disk path inaccessible: banner emits warning + recommends manual /orient
```

### Scenario 3 — first-action-after-compact enforcement (block non-orient action)

```yaml
scenario_3_first_action_block:
  setup:
    - ~/.claude/post-compact-pending-orient.flag exists (Scenario 2 completed)
    - agent attempts: PreToolUse on Edit `tools/cycle.py` (non-orient action)
  trigger:
    - PreToolUse on Edit
  expected:
    - CHECK: flag exists
    - tool is NOT /orient slash AND NOT Read on handoff doc AND NOT Read on state-files
    - BLOCK + emit:
        "FIRST-ACTION-AFTER-COMPACT must be /orient or handoff-doc Read.
         Agent attempting Edit instead. Re-orient first."
  pass_criteria:
    - block fires deterministically
    - banner specifies allowed actions (orient / Read handoff / Read state-files)
    - subsequent /orient invocation OR Read on handoff clears flag
  edge_cases:
    - agent invokes /orient: flag cleared; subsequent edits silent
    - agent reads handoff doc: flag cleared; subsequent edits silent
    - agent reads ALL 6 state-files individually: flag cleared
    - agent emergency-bypass via REASON="emergency-skip-orient": allow + log; flag persists
```

### Scenario 4 — handoff completeness validation (existing handoff lacks required fields)

```yaml
scenario_4_handoff_completeness_validation:
  setup:
    - operator pre-wrote partial handoff doc this cycle via /handoff command
    - handoff missing field: operator-pending-decisions (forgotten)
  trigger:
    - PreCompact event
  expected:
    - VALIDATION: handoff doc found, parse required fields
    - DETECT: operator-pending-decisions field missing
    - emit warning banner:
        "PRE-COMPACT — existing handoff doc missing fields: operator-pending-decisions.
         RECOMMEND: append missing fields before compaction OR allow auto-supplement."
    - if auto-supplement enabled: append missing fields from state-files/tracker
    - if auto-supplement disabled: emit error; allow compaction with degraded handoff
  pass_criteria:
    - validation parses YAML/markdown handoff structure
    - missing fields detected by required-field schema
    - banner is informational, not blocking
    - auto-supplement preserves operator's existing fields
  edge_cases:
    - handoff doc has fields but values empty: treat as "field present"; no warning
    - handoff doc has extra fields (not in required schema): preserve; no warning
    - handoff doc malformed YAML: emit error; auto-write replacement deterministic snapshot
```

### Scenario 5 — bypass with operator-grant for skip-orient

```yaml
scenario_5_skip_orient_bypass:
  setup:
    - post-compact-pending-orient.flag exists
    - operator just said: "skip orient, urgent fix needed"
    - REASON="operator-explicit-skip-orient-2026-05-08-14:22"
  trigger:
    - PreToolUse on Edit with REASON= set
  expected:
    - REASON= bypass detected; first-action-block suppressed
    - flag NOT cleared (orient still expected; operator just deferred)
    - audit log appended to ~/.claude/hooks/post-compact-bypass.log:
        {"timestamp": "<ISO>", "tool": "Edit", "target": "<path>", "bypass_reason": "operator-explicit-skip-orient..."}
    - subsequent edits without REASON= will re-trigger block
  pass_criteria:
    - bypass works without banner suppression for the warning that orient is recommended
    - audit log captures both flag-presence AND bypass-reason
    - subsequent action without REASON= re-triggers block (flag persists)
  edge_cases:
    - bypass repeated 3+ times in cycle: pattern-recurrence aggregator (impl-spec #11) flags
    - operator clears flag explicitly via /orient invocation: flag-clear takes precedence over bypass
    - operator provides REASON= for ALL subsequent actions: warns about persistent skip-orient pattern
```

## When To Apply

Apply this stress-test scenario spec when:
- Implementation-spec #10 (post-compact orientation gate) is being implemented
- Project uses Claude Code or equivalent with PreCompact + PostCompact hook events
- /orient + /handoff slash commands operational
- State-file convention established (~/.claude/active-*)
- Pain-point cluster C05 axis warrants empirical compliance measurement
- 13-gate pipeline is being implemented (this is lifecycle-event of 12 stress-test specs)

## Instances

**Instance 1: full stress-test session — operator runs all 5 scenarios**:
- Total time: ~30-40 minutes (compaction simulation requires care)
- Output: per-scenario pass/fail + lifecycle-event compliance %
- Updates impl-spec #10 REQUIRED-gates: pending → empirically_passed per scenario

**Instance 2: cross-axis composability (post-compact + input-discipline)**:
- Trigger: PostCompact orient invocation triggers input-discipline state-file refresh
- Expected: BOTH gates' state-files updated; orient ceremony is canonical context-load
- Verifies orient-as-input-discipline pattern composability

**Instance 3: scenario fails on handoff doc auto-discovery (multiple candidates)**:
- Glob returns 3 handoff docs from different cycles; timestamp-sort works correctly
- Synthetic test passed; real-session: latest handoff doc has timestamp typo; sorted incorrectly
- Surface root cause: auto-discovery should fallback on file-mtime if timestamp parse fails
- Iterate on impl-spec #10 — robustify discovery algorithm

**Instance 4: scenario passes but operator finds first-action-block intrusive**:
- Per evidence-priority hierarchy: operator-empirical override
- Surface as enforcement-tier calibration (Strict → Enforced softer warn-not-block)
- Iterate on impl-spec #10 — add config option for enforcement tier

## When Not To

- Implementation-spec #10 not yet authored
- Project lacks PreCompact/PostCompact hook events
- No state-file convention established (cold-start)
- Cold-start sessions before any cycle has run
- Test/sandbox sessions where compaction is intentional reset
- Operator-explicit deferral via REASON= bypass on entire stress-test execution

## Empirical Evidence

Per pain-point cluster C05 in master inventory: 11+ pain-point instances of "agent forgot operator-correction post-compaction", "agent re-built premise from scratch", "agent ignored handoff doc". The 5 scenarios derive empirically from those instances.

## Required Gates (per hook-architecture proposal #2 4th component)

```yaml
required_gates:
  empirically_passed:
    - synthetic_pre_compact_handoff: passed 2026-05-08 via mock state-file scenarios (10/10)
    - synthetic_post_compact_banner: passed 2026-05-08 via mock PostCompact events (8/8)
    - synthetic_first_action_block: passed 2026-05-08 via mock pending-orient scenarios (12/12)
  pending:
    - real_session_scenario_1_precompact_auto_handoff: pending — needs real auto-compaction
    - real_session_scenario_2_postcompact_orientation: pending
    - real_session_scenario_3_first_action_block: pending
    - real_session_scenario_4_handoff_completeness: pending
    - real_session_scenario_5_skip_orient_bypass: pending
    - composability_with_input_discipline: pending — orient + input-discipline state-file refresh paired
    - state_file_re_load_correctness: pending — all 6 active-* re-loaded post-compact
    - operator_empirical_first_action_block_calibration: pending
  composite_compliance: post-compact-axis stress-test 0% (no real-session executions yet) — target ≥90%
```

## Relationships

- IMPLEMENTS test plan for: implementation-spec #10 (post-compact-orientation-gate-implementation-spec)

## Tags

[stress-test-scenario-spec, post-compact, lifecycle-event-gate, test-plan, day-arc-2026-05-08, multi-day-pain-point-resolution]
