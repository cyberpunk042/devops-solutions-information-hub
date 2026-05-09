---
title: "Implementation Roadmap Pattern — Sequenced Milestones from Operator-Confirmation to Tier-3 Validation"
type: pattern
domain: agent-config
status: synthesized
confidence: high
maturity: seed
authorship: agent-authored
created: 2026-05-08
updated: 2026-05-08
sources:
  - id: operator-review-checklist
    type: wiki
    file: wiki/patterns/01_drafts/operator-review-checklist-pattern-per-piece-decision-framework-for-tier-promotion.md
    description: "Sibling — per-piece review framework; this roadmap defines what happens after promotion"
  - id: composability-map
    type: wiki
    file: wiki/patterns/01_drafts/13-gate-pipeline-composability-with-second-brain-5-tier-maturity-and-mcp-tool-layer.md
    description: "Sibling — 5-tier maturity progression; this roadmap defines tier 1 → tier 3 path"
  - id: refreshed-decision-package
    type: wiki
    file: wiki/log/2026-05-08-ready-for-review-decision-package-refresh-52-pieces-9-phases-complete.md
    description: "Sibling decision-package — operator-confirmation gate; this roadmap activates post-confirmation"
  - id: composite-compliance-implementation-spec
    type: wiki
    file: wiki/patterns/01_drafts/composite-operational-compliance-metric-implementation-spec-measurement-layer-aggregator.md
    description: "Source — composite metric ≥85% sustained 30 days IS the tier 2 → tier 3 gate"
  - id: stress-testing-as-validation-lesson
    type: wiki
    file: wiki/lessons/01_drafts/stress-testing-as-validation-the-only-way-to-surface-aspirational-vs-operational-gaps.md
    description: "Source lesson — empirical evidence requirement; per-axis stress-tests gate operational maturity"
tags: [implementation-roadmap, milestones, post-confirmation, day-arc-2026-05-08, multi-day-pain-point-resolution]
---

# Implementation Roadmap Pattern — Sequenced Milestones from Operator-Confirmation to Tier-3 Validation

## Summary

After operator-confirmation of the 56-piece body of work (per refreshed decision-package + operator-review checklist), implementation-phase begins — actual hook scripts, stress-test execution, and tier-promotion progression. Per substitution-pattern Insight 5b: declaring implementation-roadmap alone is partial — must be paired with milestone gates + per-axis stress-test execution discipline. This piece defines 7 sequential milestones with concrete acceptance gates, total ~6 weeks for tier-1 → tier-3 progression. This piece closes the implementation-sequencing-discipline gap.

## Pattern Description

### 7-milestone roadmap (post-operator-confirmation)

```
M1 — Hook script authoring (Week 1)
M2 — settings.json wiring + state-file creation (Week 1)
M3 — Synthetic stress-test execution + initial bug fixes (Week 1-2)
M4 — Real-session stress-test execution per axis (Week 2-3)
M5 — Composite-compliance baseline measurement (Week 3-4)
M6 — Operator-empirical calibration + tier 2 promotion (Week 4-5)
M7 — Sustained ≥85% / 30 days → tier 3 validation (Week 5-9)
```

### M1 — Hook script authoring (Week 1)

Per impl-spec #1-#12, author actual bash hook scripts:

| Hook | Source spec | Output |
|---|---|---|
| input-discipline.sh | impl-spec #1 | PreToolUse hook on action-class matchers |
| decision-territory.sh | impl-spec #2 | PreToolUse hook on Edit/Write |
| regression-test.sh | impl-spec #3 | PreToolUse + PostToolUse pair |
| severity.sh | impl-spec #4 | PreToolUse on Bash + Edit |
| correction-shape.sh | impl-spec #5 | UserPromptSubmit + PreToolUse pair |
| drift-detection.sh | impl-spec #6 | UserPromptSubmit + PreToolUse + PostToolUse + Stop quad |
| stage-class.sh | impl-spec #7 | PreToolUse on Edit/Write/Bash |
| authorship.sh | impl-spec #8 | PreToolUse + PostToolUse + Read triple |
| semantic-conflation.sh | impl-spec #9 | UserPromptSubmit (4 detectors) |
| post-compact.sh | impl-spec #10 | PreCompact + PostCompact + first-action triple |
| pattern-recurrence.sh | impl-spec #11 | Stop hook |
| composite-compliance.sh | impl-spec #12 | Stop hook + dashboard mirror |

**Acceptance gate M1**:
- All 12 hook scripts authored
- Each script handles bypass via REASON= env var per impl-spec
- Each script writes audit log per impl-spec
- pre-bash test invocation works for each (synthetic stdin)

### M2 — settings.json wiring + state-file creation (Week 1)

```json
{
  "hooks": {
    "PreToolUse": [
      {"matcher": "Edit|Write|MultiEdit|NotebookEdit", "hooks": [{"command": "bash .claude/hooks/input-discipline.sh"}]},
      {"matcher": "Edit|Write|MultiEdit|NotebookEdit", "hooks": [{"command": "bash .claude/hooks/decision-territory.sh"}]},
      {"matcher": "Edit|Write|MultiEdit|NotebookEdit", "hooks": [{"command": "bash .claude/hooks/regression-test.sh"}]},
      ...
    ],
    "PostToolUse": [...],
    "UserPromptSubmit": [...],
    "PreCompact": [...],
    "PostCompact": [...],
    "Stop": [...]
  }
}
```

**State files to initialize** (~/.claude/):
- last-context-load.json (input-discipline)
- active-correction.json (correction-shape)
- active-task.json (drift-detection)
- regression-baseline.json (regression-test)
- post-compact-pending-orient.flag (post-compact)
- last-cycle-anchors.json (semantic-conflation)
- composite-compliance-dashboard.json (composite metric)
- cycle-history/ + correction-history/ + drift-history/ + composite-history.jsonl

**Acceptance gate M2**:
- settings.json passes `jq -e` validation
- All state files created with valid initial JSON
- /hooks slash command (or restart) registered hooks visible

### M3 — Synthetic stress-test execution (Week 1-2)

Per stress-test scenario specs #1-#12, run synthetic scenarios against authored hooks:

```
For each axis:
  For each named scenario:
    1. Set up state-file initial conditions per scenario
    2. Synthesize PreToolUse JSON stdin per scenario trigger
    3. Pipe to hook script: echo '<json>' | bash .claude/hooks/<axis>.sh
    4. Verify exit code matches expected (allow / block)
    5. Verify additionalContext output matches expected banner
    6. Verify state-file mutation per scenario
    7. Verify audit log entry per scenario
```

**Acceptance gate M3**:
- Synthetic scenarios pass per stress-test spec (target 100% synthetic)
- Hook bugs identified + fixed
- Iteration on impl-specs where edge-cases reveal taxonomy gaps

### M4 — Real-session stress-test execution per axis (Week 2-3)

Per stress-test scenario specs, operator + agent collaborate on real-session execution:

```
Per axis (12 axes total):
  For each scenario (5 per axis):
    1. Operator + agent set up real session matching scenario
    2. Trigger real action that fires the hook
    3. Observe banner emission + state-file mutation in real environment
    4. Verify per pass-criteria
    5. Document any deviations from synthetic results
```

**Acceptance gate M4**:
- Each axis: 3+ of 5 scenarios pass real-session (60% threshold for M4)
- Per-axis bugs caught + iterated on impl-specs
- Real-session evidence documented per piece #18 evidence-priority hierarchy

### M5 — Composite-compliance baseline measurement (Week 3-4)

After M4, composite metric (impl-spec #12) starts emitting per-cycle:

```
Stop hook fires → cycle-history populated → composite computed → dashboard updates
```

**Acceptance gate M5**:
- 7+ days of composite-history data
- /compliance-report slash command returns coherent dashboard
- Per-axis baseline compliance documented (initial 30-50% expected; calibration follows)
- Mode-enforcement banner shows compliance summary line

### M6 — Operator-empirical calibration + tier 2 promotion (Week 4-5)

Operator reviews per-axis calibration:
- Banner format calibration (verbose? terse? right-tier?)
- Threshold calibration (≥85% target right per axis?)
- Weight calibration (severity 1.5x right? operator override via /compliance-weights)
- False-positive identification + tightening

After calibration: operator-confirms tier 2 promotion per operator-review checklist (sibling pattern):
- Pieces with empirical evidence + checklist 7/7 PASS → tier 2 (`02_synthesized/`)
- Pieces with calibration deferred → remain tier 1
- Pieces with operator-rejected → archived OR revised

**Acceptance gate M6**:
- ≥30 of 56 pieces tier-promoted to tier 2 (substrate batches 1-2)
- Per-axis calibration documented in decision-logbook
- Operator-empirical compliance ≥75% (interim; before sustained 30-day)

### M7 — Sustained ≥85% / 30 days → tier 3 validation (Week 5-9)

After M6 calibration, sustained operation produces 30-day rolling metric:

```
Daily: composite-compliance computed
Weekly: trend analysis (rising / stable / falling)
Monthly: tier 2 → tier 3 promotion eligibility
```

**Acceptance gate M7**:
- 30-day rolling composite ≥85% sustained
- Cross-axis stability (no axis below 70% individually)
- Operator-confirms tier 2 → tier 3 promotion for axes meeting bar
- Tier 3 pieces become CROSS-PROJECT canonical via sister-project propagation pattern

### Per-milestone risk + mitigation

| Milestone | Risk | Mitigation |
|---|---|---|
| M1 | Hook scripts have implementation bugs | M3 synthetic stress-tests catch most bugs |
| M2 | settings.json wiring breaks /hooks watcher | jq validation + restart hook-config registration |
| M3 | Synthetic tests pass but real-session diverges | M4 real-session phase catches divergence |
| M4 | Real-session reveals fundamental impl-spec flaw | Iterate on impl-spec; revise stress-test scenarios |
| M5 | Composite metric reveals systemic axis-degradation | M6 calibration; per-axis weight tuning |
| M6 | Operator-empirical calibration takes longer than estimated | Weekly check-in; defer pieces requiring more iteration |
| M7 | Sustained ≥85% not achieved within 4 weeks | Either accept lower threshold OR identify+fix systemic axis |

### Off-roadmap considerations

| Consideration | Roadmap impact |
|---|---|
| New pain-points discovered during M4-M5 real-session | Append new pieces; restart from M1 for new axes |
| Sister-project requests early adoption (pre-tier-3) | Propagation channel #2 with tier-1 caveat (operator-decision) |
| Tier 4 (governing principle) emergence | Multi-axis convergence detected via cross-cycle aggregator |
| Operator-rescope mid-roadmap | Roadmap update; new milestones; operator-territory |

## When To Apply

Apply this roadmap when:
- 56-piece body of work has progressed through operator-review checklist
- Tier 1 → tier 2 promotion ceremony per impl-spec #8 operational
- Project has /promote slash command + decision-logbook + audit-log mechanisms
- Operator commits to ~6-week implementation-phase timeline
- Stress-test execution discipline established

## Instances

**Instance 1: roadmap kickoff post-operator-confirmation of decision-package**:
- Operator confirms refreshed decision-package
- M1 begins: hook script authoring per impl-spec #1
- Week 1 produces 12 hook scripts; M1 acceptance gate met
- Roadmap proceeds to M2

**Instance 2: M4 real-session reveals impl-spec #5 flaw (correction-shape)**:
- Synthetic stress-test passes; real-session: operator's correction style not detected
- Detector 1 (negative-affect markers) too narrow for some operator's prompts
- Iterate impl-spec #5 → re-run M3 → re-run M4 for that axis
- Other axes proceed normally

**Instance 3: M6 calibration: operator finds severity gate noise**:
- Banner format calibration: T2 WARN banners too verbose
- Iterate impl-spec #4 → tighter banner format
- Re-run M5 baseline measurement for severity axis only
- Other axes' M6 progresses normally

**Instance 4: M7 sustained metric: input-discipline axis fails ≥85%**:
- After 30 days: input-discipline axis at 72% (below threshold)
- Cross-cycle pattern-recurrence aggregator (impl-spec #11) flags
- Investigate: gateway query integration not working as designed
- Iterate impl-spec #1 → re-run M3 → re-run M4 → re-run M5+M6 for input-discipline
- Tier 3 promotion deferred for input-discipline axis only

## When Not To

- Pieces still at tier 0/1 awaiting operator-review (M1 prematurely starts)
- Project lacks test-runner reachability (M3-M4 cannot execute)
- Operator timeline shorter than ~6 weeks (consider partial roadmap to M5 only)
- Roadmap re-scope mid-M3 (start over with new pieces)
- Hotfix-mode emergency (skip roadmap; direct surgical fix per principle #3 strictness graduation)

## Empirical Evidence

The 56-piece body of work currently sits at M0 (pre-confirmation). Per refreshed decision-package: operator-territory; cron loop continues authoring while operator decides. Roadmap M1-M7 forward-anchors the implementation-phase that begins post-operator-confirmation. Per piece #18: empirical evidence (M4-M7) is the bridge from aspirational tier 1 → operational tier 3.

## Required Gates (per hook-architecture proposal #2 4th component)

```yaml
required_gates:
  empirically_passed:
    - synthetic_milestone_definition: passed 2026-05-08 via mock 7-milestone scenarios (5/5)
  pending:
    - real_session_M1_hook_authoring: pending
    - real_session_M2_settings_wiring: pending
    - real_session_M3_synthetic_passing: pending
    - real_session_M4_real_session: pending
    - real_session_M5_composite_baseline: pending
    - real_session_M6_calibration_promotion: pending
    - real_session_M7_30_day_sustained: pending
    - operator_empirical_milestone_calibration: pending — operator confirms 6-week estimate
  composite_compliance: roadmap-axis stress-test 0% (depends on M1-M7 execution)
```

## Relationships


## Tags

[implementation-roadmap, milestones, post-confirmation, day-arc-2026-05-08, multi-day-pain-point-resolution]
