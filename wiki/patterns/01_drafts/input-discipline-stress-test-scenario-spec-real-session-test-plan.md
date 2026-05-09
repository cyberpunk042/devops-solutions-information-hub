---
title: "Input-Discipline Stress-Test Scenario Spec — Real-Session Test Plan"
type: pattern
domain: agent-config
status: synthesized
confidence: high
maturity: seed
authorship: agent-authored
created: 2026-05-08
updated: 2026-05-08
sources:
  - id: input-discipline-implementation-spec
    type: wiki
    file: wiki/patterns/01_drafts/input-discipline-gate-implementation-spec-pre-action-context-load-verification.md
    description: "PRIMARY parent — implementation-spec #1; this stress-test scenario spec expands its REQUIRED-gates pending list into full test plans"
  - id: stress-testing-as-validation-lesson
    type: wiki
    file: wiki/lessons/01_drafts/stress-testing-as-validation-the-only-way-to-surface-aspirational-vs-operational-gaps.md
    description: "Source lesson — stress-testing-as-validation discipline; this scenario spec is the canonical structure"
  - id: c04-input-discipline-lesson
    type: wiki
    file: wiki/lessons/01_drafts/agent-context-discipline-is-aspirational-without-enforcement-gates-not-reading-what-exists.md
    description: "Cluster lesson C04 — defines the empirical gap this stress-test set measures"
  - id: comprehensive-13-gate-pattern
    type: wiki
    file: wiki/patterns/01_drafts/comprehensive-agent-action-emission-pipeline-13-gate-composition-architecture.md
    description: "Integration pattern — input-discipline IS gate #1; stress-test feeds composite-compliance metric"
  - id: composite-compliance-implementation-spec
    type: wiki
    file: wiki/patterns/01_drafts/composite-operational-compliance-metric-implementation-spec-measurement-layer-aggregator.md
    description: "Sibling — composite-compliance metric; this stress-test data is the input"
tags: [stress-test-scenario-spec, input-discipline, gate-1, test-plan, day-arc-2026-05-08, multi-day-pain-point-resolution]
---

# Input-Discipline Stress-Test Scenario Spec — Real-Session Test Plan

## Summary

Per piece #18 (stress-testing-as-validation lesson) + impl-spec #1 (input-discipline gate) REQUIRED-gates pending list, the input-discipline gate operational-compliance is bridged from synthetic-passed to real-session-passed via concrete stress-test scenarios. This piece defines the test plan: 5 named scenarios with input setup + expected gate behavior + pass criteria + edge cases. Per substitution-pattern lesson Insight 5b: implementation-spec describes WHAT to build; stress-test scenario spec describes HOW to verify it operationally. Without stress-test scenarios, the gate is structurally-fixed but behaviorally aspirational. This spec closes the test-plan substitution at axis #1.

## Pattern Description

**Stress-test layer**: real-session evidence (per piece #18 evidence-priority-hierarchy tier 2) + operator-empirical confirmation (tier 1) for highest-confidence promotion.

**Test scenario format**:

```
SCENARIO_NAME:
  setup:
    - state-file initial conditions
    - operator prompt sequence
    - active-mode/active-task pre-conditions
  trigger:
    - the action that should fire the gate
  expected:
    - gate decision (allow / soft-warn / banner / block)
    - state-file mutation post-action
    - audit-log entry
  pass_criteria:
    - observable behaviors (banner emits / decision matches / log appended)
  edge_cases:
    - boundary scenarios that test gate robustness
```

### Scenario 1 — recent-messages-not-loaded violation

```yaml
scenario_1_recent_messages_not_loaded:
  setup:
    - ~/.claude/last-context-load.json: { recent_messages_loaded_at: "<2 hours ago>", cycle_id: "<current>" }
    - active-mode: dual-expert
    - operator prompt arrived: "<just now> work on the statusline edit"
    - cycle_start: "<now - 5 sec>"
  trigger:
    - PreToolUse on Edit `~/.claude/hooks/statusline.sh`
  expected:
    - CHECK 1 fails: recent_messages_loaded_at (2h ago) < cycle_start (5s ago)
    - banner emits via additionalContext
    - banner content: "FAILED: recent-messages — operator's recent messages not loaded this cycle. LOAD: re-read last 3-5 operator messages."
    - state-file: no mutation (banner is informational)
    - audit log: append entry to ~/.claude/hooks/input-discipline-bypass.log if REASON= used
  pass_criteria:
    - banner text matches expected format
    - banner emits BEFORE Edit tool executes
    - PostToolUse on Read of operator messages updates recent_messages_loaded_at
  edge_cases:
    - cycle just started (loaded_at exactly equals cycle_start): pass (boundary inclusive)
    - state-file missing entirely: emit "first cycle of session — load required" banner
    - cycle_id mismatch (state from prior session): treat as not-loaded
```

### Scenario 2 — mode-pieces-not-loaded violation

```yaml
scenario_2_mode_pieces_not_loaded:
  setup:
    - active-mode: dual-expert (per ~/.claude/active-mode)
    - dual-expert mode primary brain pieces: [ARCHITECTURE.md, DESIGN.md, methodology.yaml, blockers.md, progress.md]
    - ~/.claude/last-context-load.json mode_pieces_loaded: ["ARCHITECTURE.md"] (only 1 of 5)
  trigger:
    - PreToolUse on Bash `python3 -m tools.cycle`
  expected:
    - CHECK 2 fails: 4 of 5 dual-expert primary pieces unloaded
    - banner: "FAILED: mode-pieces — DESIGN.md, methodology.yaml, blockers.md, progress.md not loaded for dual-expert mode."
    - banner suggests Read commands for each missing piece
  pass_criteria:
    - all missing pieces listed in banner
    - banner emits BEFORE cycle invocation
    - PostToolUse on Read of each missing piece updates state-file
  edge_cases:
    - no active-mode set (file empty or absent): no banner; mode-pieces-check undefined
    - mode-file lists pieces that don't exist: emit warning + degrade gracefully
    - operator override via REASON=: banner suppressed; bypass logged
```

### Scenario 3 — opt-pieces-not-loaded violation (Insight 5b enforcement)

```yaml
scenario_3_opt_pieces_not_loaded:
  setup:
    - operator prompt: "let's work on lesson about agent-context-discipline"
    - gateway query for "agent-context-discipline" returns: ["wiki/lessons/01_drafts/agent-context-discipline-is-aspirational-without-enforcement-gates-not-reading-what-exists.md"]
    - ~/.claude/last-context-load.json opt_pieces_loaded: [] (none loaded)
  trigger:
    - PreToolUse on Write to `/opt/.../wiki/lessons/01_drafts/<new-related-lesson>.md`
  expected:
    - CHECK 3 fails: gateway-identified relevant pieces not in opt_pieces_loaded
    - banner: "FAILED: opt-pieces — related existing pieces not consulted before authoring. CHECK: <gateway-results>. RECOMMEND: extend existing or cite, don't duplicate."
    - banner cites Insight 5b knowledge-reuse discipline
  pass_criteria:
    - gateway query runs as part of CHECK 3
    - banner lists specific related-piece paths
    - subsequent Read of related pieces updates state; gate passes on retry
  edge_cases:
    - gateway query returns 0 matches: silent allow (no related pieces to consult)
    - gateway query returns 50+ matches: cap at top 5 by relevance score
    - operator explicit "I know about <piece>; bypass": REASON= bypass with citation
```

### Scenario 4 — bypass with logged audit (legitimate exception path)

```yaml
scenario_4_bypass_audit:
  setup:
    - any input-discipline check would fail (e.g., scenario 1)
    - operator just said "skip the orient; emergency edit needed"
  trigger:
    - PreToolUse on Edit with REASON="emergency-operator-grant-2026-05-08-13:34"
  expected:
    - REASON= bypass detected; banner suppressed
    - audit log: ~/.claude/hooks/input-discipline-bypass.log appends entry:
      {"timestamp": "<ISO>", "check_failed": "recent_messages", "bypass_reason": "emergency-operator-grant-2026-05-08-13:34"}
  pass_criteria:
    - bypass works without banner
    - audit log entry written deterministically
    - audit log entry includes original-check-name + reason verbatim
  edge_cases:
    - REASON= empty: not a bypass; original banner still emits
    - REASON= without operator-grant-citation: emits "weak bypass" warning + still allows
    - audit log file not writable: hook errors fail-safe (banner emits even with REASON=)
```

### Scenario 5 — cycle-boundary state-file freshness

```yaml
scenario_5_cycle_boundary_freshness:
  setup:
    - operator prompt arrives: starts new cycle
    - prior cycle ended 30 sec ago
    - state-file ~/.claude/last-context-load.json from prior cycle still present
  trigger:
    - UserPromptSubmit hook
  expected:
    - cycle_id rotates (new uuid generated)
    - cycle_start = now
    - mode_pieces_loaded array reset OR retained per state-file convention
    - opt_pieces_loaded array reset OR retained per state-file convention
    - recent_messages_loaded_at: updated to current operator-message timestamp
  pass_criteria:
    - subsequent PreToolUse uses fresh cycle_id
    - prior cycle's state doesn't bleed into new cycle's checks
    - cycle-history persists prior cycle to ~/.claude/cycle-history/<prior-uuid>.json
  edge_cases:
    - rapid back-to-back prompts (<5s apart): treat as same cycle (no rotate)
    - prompt with no edit-action follows (read-only cycle): cycle_id rotates; no audit logs
    - operator-explicit cycle reset via slash command: forced rotate
```

## When To Apply

Apply this stress-test scenario spec when:
- Implementation-spec #1 (input-discipline gate) is being implemented
- Hook scripts are being authored against the spec
- Real-session execution is operationally available (operator + agent collaborating)
- Composite-compliance metric is being computed (this stress-test data feeds it)
- Pain-point cluster C04 axis warrants empirical operational-compliance measurement

## Instances

**Instance 1: stress-test execution session — operator runs all 5 scenarios in real session**:
- Each scenario takes ~3-5 minutes (setup + trigger + verify expected + edge cases)
- Total session time: ~25-30 minutes for full input-discipline axis stress-test
- Output: per-scenario pass/fail + axis-level compliance %
- Updates impl-spec #1 REQUIRED-gates: pending → empirically_passed for each scenario passed

**Instance 2: stress-test partial execution — only critical-path scenarios**:
- Run scenarios 1-3 only (CHECK 1-3 paths); skip 4-5 (bypass + cycle-boundary)
- Output: 60% axis-coverage; operator decides whether to schedule full coverage later
- Caveats: incomplete coverage = lower confidence; promotion gated on full coverage

**Instance 3: stress-test fails on scenario 3 (opt-pieces gateway integration)**:
- Gateway query returns unexpected results (or fails to run)
- Scenario 3 marked FAILED; impl-spec #1 retains "real_session_opt_pieces_check: pending"
- Surface root cause: gateway integration bug OR query taxonomy gap
- Iterate on impl-spec OR gateway tools, not on scenario spec

**Instance 4: scenario passes empirically but operator-empirical disagrees**:
- Per evidence-priority-hierarchy (principle #5 extension): operator-empirical > diag log > subagent > inference
- Operator's "this banner is annoying noise" overrides synthetic + real-session pass
- Surface as impl-spec calibration issue (banner wording / threshold tuning)

## When Not To

- Implementation-spec #1 not yet authored (chicken-and-egg)
- Hook scripts not yet authored against the spec (nothing to test)
- Cold-start sessions before any state-files exist
- Operator-explicit deferral (REASON= bypass on entire stress-test execution)
- Axes other than input-discipline (this spec is per-axis-#1)

## Empirical Evidence

Per pain-point cluster C04 in master inventory: 15+ pain-point instances of input-discipline violations. The 5 scenarios above are derived empirically from those instances — each scenario is the test-plan version of a specific pain-point pattern observed. The implementation-spec above closes the test-plan substitution at axis #1 — without these named scenarios, "operationally meaningful" is undefined; with them, axis-level compliance is measurable per piece #18.

## Required Gates (per hook-architecture proposal #2 4th component)

```yaml
required_gates:
  empirically_passed:
    - synthetic_scenario_definition: passed 2026-05-08 via mock state-file scenarios per scenario (5/5)
  pending:
    - real_session_scenario_1_recent_messages: pending — needs real session execution
    - real_session_scenario_2_mode_pieces: pending — needs real session execution
    - real_session_scenario_3_opt_pieces: pending — needs real session execution + gateway integration
    - real_session_scenario_4_bypass_audit: pending — needs real session bypass invocation
    - real_session_scenario_5_cycle_boundary: pending — needs real session cycle-rotation observation
    - operator_empirical_confirmation: pending — operator confirms each scenario's banner wording is operationally useful (not noise)
  composite_compliance: input-discipline-axis stress-test 0% (no real-session executions yet) — target 5/5 scenarios pass for ≥85% axis compliance
```

## Relationships

- IMPLEMENTS test plan for: implementation-spec #1 (input-discipline-gate-implementation-spec)

## Tags

[stress-test-scenario-spec, input-discipline, gate-1, test-plan, day-arc-2026-05-08, multi-day-pain-point-resolution]
