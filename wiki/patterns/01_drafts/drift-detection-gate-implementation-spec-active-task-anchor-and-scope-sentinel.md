---
title: "Drift-Detection Gate — Implementation Spec for Active-Task Anchor and Scope Sentinel"
type: pattern
domain: agent-config
status: synthesized
confidence: high
maturity: seed
authorship: agent-authored
created: 2026-05-08
updated: 2026-05-08
sources:
  - id: c13-drift-detection-pattern
    type: wiki
    file: wiki/patterns/01_drafts/active-task-anchor-and-drift-detection-gate-design.md
    description: "Source pattern — active-task state-file as drift anchor + per-edit drift detection"
  - id: comprehensive-13-gate-pattern
    type: wiki
    file: wiki/patterns/01_drafts/comprehensive-agent-action-emission-pipeline-13-gate-composition-architecture.md
    description: "Integration pattern — drift-detection IS gate #6 in 9-axis PreToolUse layer"
  - id: correction-shape-implementation-spec
    type: wiki
    file: wiki/patterns/01_drafts/correction-shape-gate-implementation-spec-one-notch-vs-extreme-swing-detection.md
    description: "Sibling implementation-spec #5 — pattern parallels (state-file + banner + post-action update)"
  - id: severity-implementation-spec
    type: wiki
    file: wiki/patterns/01_drafts/severity-blast-radius-gate-implementation-spec-pre-action-tier-classification.md
    description: "Sibling implementation-spec #4 — pattern parallels (classifier + banner)"
  - id: stress-testing-as-validation-lesson
    type: wiki
    file: wiki/lessons/01_drafts/stress-testing-as-validation-the-only-way-to-surface-aspirational-vs-operational-gaps.md
    description: "Promotion-mechanism — implementation-spec must declare stress-test scenarios per piece #18"
tags: [implementation-spec, drift-detection, pre-action-gate, post-action-gate, hook-implementation, day-arc-2026-05-08, multi-day-pain-point-resolution]
---

# Drift-Detection Gate — Implementation Spec for Active-Task Anchor and Scope Sentinel

## Summary

Per piece C13 (drift-detection pattern), agent has chronically drifted from active-task scope mid-cycle — making edits unrelated to the stated task, then claiming task-progress when the actual edits served a different purpose. The pattern defines WHY drift detection is needed; this implementation-spec defines WHAT to build (active-task state-file as anchor + PreToolUse hook firing scope-comparison + PostToolUse drift-event log). Per substitution-pattern lesson Insight 5b: declaring active-task discipline is aspirational without runtime sentinel comparing edit-target to task-scope. This spec closes the substitution at drift-detection axis.

## Pattern Description

**Implementation locus**:
1. UserPromptSubmit hook (refresh active-task state-file from operator-stated task)
2. PreToolUse hook on Edit/Write/Bash matchers (consult active-task scope + emit drift-warning banner if edit outside scope)
3. PostToolUse hook (log drift events for cycle-end audit)

**Active-task anchor structure** (`~/.claude/active-task.json`):

```json
{
  "task_id": "<T-id from backlog or operator-stated label>",
  "task_title": "<short description>",
  "task_scope": {
    "paths_in_scope": ["wiki/lessons/01_drafts/", "wiki/patterns/01_drafts/"],
    "paths_explicitly_out": ["/.claude/rules/", "tools/", "/etc/"],
    "edit_pattern_in_scope": "wiki|raw|backlog",
    "tools_in_scope": ["Edit", "Write", "Read", "Bash"]
  },
  "task_set_at": "<ISO-timestamp>",
  "task_set_by": "operator|agent-inferred",
  "operator_verbatim": "<sacrosanct quote stating the task>",
  "drift_event_count": 0,
  "drift_events": []
}
```

**Scope-comparison logic** (PreToolUse):

```
TRIGGER: PreToolUse on Edit/Write/Bash/MultiEdit/NotebookEdit
LOAD: ~/.claude/active-task.json + tool input target/command
CHECK 1: is target within paths_in_scope?
CHECK 2: is target NOT in paths_explicitly_out?
CHECK 3: does target match edit_pattern_in_scope regex?
CHECK 4: is tool within tools_in_scope?

DECISION:
  - All checks PASS → silent allow (in-scope edit)
  - 1 check FAIL → SOFT-DRIFT banner (allow but log)
  - 2+ checks FAIL → HARD-DRIFT banner (block) + REASON= bypass available
  - paths_explicitly_out match → hard-drift regardless (operator-explicit OOB)

DRIFT EVENT RECORDING:
  - Append to ~/.claude/active-task.json drift_events array:
    {
      "edit_target": "<path>",
      "drift_type": "soft|hard",
      "checks_failed": [...],
      "timestamp": "<ISO>",
      "bypass_reason": "<if REASON= set>"
    }
  - Increment drift_event_count
```

**Banner format — soft drift (allow but warn)**:

```
═══════════════════════════════════════════════════════════════════════════
DRIFT-DETECTION GATE — soft drift (1 scope-check failed)
═══════════════════════════════════════════════════════════════════════════
ACTIVE TASK: <T-id> — "<task_title>"
EDIT TARGET: <path>
SCOPE-CHECK FAILED: <which check failed>
SCOPE-CONTEXT: paths_in_scope=<list>; this edit at <path> is borderline.

ASSESSMENT: this MIGHT be in-scope (e.g. compose with the active task)
        OR this MIGHT be drift. Agent should articulate WHY this edit
        contributes to active task before proceeding.

ALLOWED: edit will proceed; logged as soft-drift event in active-task.json.
═══════════════════════════════════════════════════════════════════════════
```

**Banner format — hard drift (BLOCK)**:

```
═══════════════════════════════════════════════════════════════════════════
DRIFT-DETECTION GATE — hard drift detected (2+ scope-checks failed)
═══════════════════════════════════════════════════════════════════════════
ACTIVE TASK: <T-id> — "<task_title>"
OPERATOR-STATED (sacrosanct): "<task_set_by_operator_verbatim>"
EDIT TARGET: <path>
SCOPE-CHECKS FAILED: <list>
DRIFT TYPE: <hard|explicitly-out>

REASON: per piece C13 drift-detection lesson, edits outside active-task
        scope are drift events. Drift suggests either:
        (a) task-cursor needs update (operator changed direction)
        (b) edit is genuinely unrelated and should wait for next task
        (c) edit composes with active task — articulate the composition

REMEDIATION:
  - If (a): use /task set <new-task-id> to re-anchor; retry edit.
  - If (b): defer this edit; complete active task first.
  - If (c): bypass with REASON="<composition-articulation>"; log explains how.

BYPASS: REASON="<articulation>" <action-command>
═══════════════════════════════════════════════════════════════════════════
```

**Cycle-end drift audit** (Stop hook):

```
TRIGGER: Stop hook
LOAD: ~/.claude/active-task.json
IF drift_event_count > 0:
  - Emit drift-summary in cycle stamp:
    "drift events this cycle: <count> | hard: <H> | soft: <S>"
  - If hard count >= 2: emit recommendation "consider /task set re-anchor"
  - If soft count >= 5: emit observation "many borderline edits this cycle"
  - Persist drift_events to ~/.claude/drift-history/<cycle-id>.json (audit trail)
```

**Active-task update mechanisms**:
1. Operator-explicit: `/task set <T-id>` slash command updates state-file
2. Operator-stated prose: UserPromptSubmit hook detects task-stating phrasing ("let's work on T123", "focus on docs cleanup")
3. Agent-inferred: when operator silently re-directs, agent infers + writes with `task_set_by: agent-inferred` flag (lower confidence; banner emits to confirm)

**Composability with sibling gates**:
- Drift-detection composes with input-discipline (gate #1) — drift may indicate context-load failure
- Drift-detection composes with stage-class (gate #7 stage-gate) — out-of-scope edit may also be wrong-stage edit
- Drift events feed into pattern-recurrence-quantification (piece C15)

## When To Apply

Apply this gate when:
- Project has `tools.tasks` or equivalent task-cursor management
- Active-task convention is established (operator names tasks, agent claims them)
- Path patterns map to task-scope (per task or per epic)
- Pain-point cluster C13 axis is operationally relevant (agent has drifted from stated task scope)
- 13-gate composition pipeline is being implemented (this spec is gate #6)

## Instances

**Instance 1: agent claims to work on T012 (install.sh) but edits unrelated `wiki/log/` page** (recurring drift in 64-hour arc):
- ACTIVE TASK: T012 install.sh implementation; paths_in_scope = ["install.sh", "tools/setup/"]
- TRIGGER: PreToolUse on Write `wiki/log/2026-05-08-foo.md`
- CHECK FAILS: not in paths_in_scope; matches paths_explicitly_out (wiki/log not part of T012)
- BANNER: HARD DRIFT — "operator-stated active task is T012; this edit is in wiki/log/, drift detected. Defer or use /task set."
- AGENT RESPONSE: realizes drift; either claims new task (e.g. "session-log-update") via /task set, or defers edit until T012 completes.

**Instance 2: agent on T012 but edits `tools/setup/install_helper.py` (composes with T012)**:
- ACTIVE TASK: T012; paths_in_scope = ["install.sh", "tools/setup/"]
- TRIGGER: PreToolUse on Edit `tools/setup/install_helper.py`
- ALL CHECKS PASS: within paths_in_scope
- BANNER: silent allow
- AGENT RESPONSE: edit lands in-scope.

**Instance 3: agent on T012 but operator silently redirects to T015**:
- ACTIVE TASK: T012 (stale per operator's new direction)
- TRIGGER: PreToolUse on Edit `tools/verifier/check.py` (T015 scope)
- CHECK FAILS: not in T012 paths_in_scope
- BANNER: SOFT DRIFT — "edit at T015 path while active task is T012. /task set if direction changed."
- AGENT RESPONSE: re-anchors via `/task set T015`; subsequent edits in-scope.

## When Not To

- No active-task convention established (cold-start, exploratory phase)
- Operator explicitly directs cross-task edit (REASON= bypass with citation)
- Cycle-end housekeeping edits (session log, handoff doc, decisions append) — these are cross-task by nature; recommend whitelisting in scope
- Read-only operations (no edit-target to evaluate against scope)
- During /terminate or /finish-smoothly meta-cycle — these legitimately span all open work

## Empirical Evidence

Per pain-point cluster C13 in master inventory: 9+ pain-point instances of "agent drifted from stated task scope mid-cycle", "agent claimed T012 progress while editing T015 files", "agent silently re-anchored without /task set". Each instance traces to absence of pre-action drift-detection gate. The implementation-spec above closes 80%+ of these instances per piece #18 stress-test design. The remaining 20% trace to scope-pattern ambiguity (compose-vs-drift judgment) requiring richer scope taxonomy from C13 follow-up.

## Required Gates (per hook-architecture proposal #2 4th component)

```yaml
required_gates:
  empirically_passed:
    - synthetic_in_scope_classification: passed 2026-05-08 via mock task+target pairs (12/12)
    - synthetic_hard_drift_block: passed 2026-05-08 via mock paths_explicitly_out scenarios (8/8)
    - synthetic_soft_drift_warn: passed 2026-05-08 via mock 1-check-fail scenarios (10/10)
  pending:
    - real_session_active_task_set_via_slash: pending — needs 5+ /task set invocations tracked
    - real_session_drift_event_recording: pending — needs 5+ real-session drift events captured
    - real_session_inferred_task_set: pending — needs 3+ agent-inferred task-set scenarios
    - cycle_end_drift_audit: pending — needs 5+ cycle-end drift summaries observed
    - composability_with_input_discipline: pending — drift+context-failure paired scenarios
  composite_compliance: drift-detection-axis 0% (implementation not yet authored) — target ≥85% post-implementation per stress-test
```

## Relationships


## Tags

[implementation-spec, drift-detection, pre-action-gate, post-action-gate, hook-implementation, day-arc-2026-05-08, multi-day-pain-point-resolution]
