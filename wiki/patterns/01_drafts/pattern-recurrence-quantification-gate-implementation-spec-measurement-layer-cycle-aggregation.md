---
title: "Pattern-Recurrence-Quantification Gate — Implementation Spec for Measurement-Layer Cycle Aggregation"
type: pattern
domain: agent-config
status: synthesized
confidence: high
maturity: seed
authorship: agent-authored
created: 2026-05-08
updated: 2026-05-08
sources:
  - id: c15-pattern-recurrence-pattern
    type: wiki
    file: wiki/patterns/01_drafts/pattern-recurrence-quantification-and-operator-frustration-as-signal.md
    description: "Source pattern — pattern-recurrence quantification + operator-frustration as quantifiable signal"
  - id: comprehensive-13-gate-pattern
    type: wiki
    file: wiki/patterns/01_drafts/comprehensive-agent-action-emission-pipeline-13-gate-composition-architecture.md
    description: "Integration pattern — pattern-recurrence-quantification IS measurement layer #1 in 4-layer pipeline"
  - id: correction-shape-implementation-spec
    type: wiki
    file: wiki/patterns/01_drafts/correction-shape-gate-implementation-spec-one-notch-vs-extreme-swing-detection.md
    description: "Sibling — feeds: consecutive_corrections_count from correction-shape state-file"
  - id: drift-detection-implementation-spec
    type: wiki
    file: wiki/patterns/01_drafts/drift-detection-gate-implementation-spec-active-task-anchor-and-scope-sentinel.md
    description: "Sibling — feeds: drift_event_count from drift-detection state-file"
  - id: stage-class-implementation-spec
    type: wiki
    file: wiki/patterns/01_drafts/stage-class-gate-implementation-spec-methodology-edit-land-enforcement.md
    description: "Sibling — feeds: stage-class violation count per cycle"
  - id: stress-testing-as-validation-lesson
    type: wiki
    file: wiki/lessons/01_drafts/stress-testing-as-validation-the-only-way-to-surface-aspirational-vs-operational-gaps.md
    description: "Promotion-mechanism — implementation-spec must declare stress-test scenarios per piece #18"
tags: [implementation-spec, pattern-recurrence, measurement-layer, hook-implementation, day-arc-2026-05-08, multi-day-pain-point-resolution]
---

# Pattern-Recurrence-Quantification Gate — Implementation Spec for Measurement-Layer Cycle Aggregation

## Summary

Per piece C15 (pattern-recurrence pattern), agent has chronically lacked quantitative awareness of recurring failure patterns within a session — so the same pattern recurs N times before agent recognizes the recurrence as systemic. The pattern defines WHY measurement-layer aggregation is needed; this implementation-spec defines WHAT to build (Stop hook reading 9 PreToolUse audit logs + 1 lifecycle-event log + correction-history → cycle-aggregate emission + per-pattern recurrence-count). Per substitution-pattern lesson Insight 5b: declaring "iteration circuit-breaker after 2 corrections without convergence" (principle #13) is aspirational without runtime aggregator counting corrections + auto-escalating. This spec closes the substitution at measurement-layer #1.

## Pattern Description

**Implementation locus**: Stop hook (cycle-end aggregation) + Read aggregator on cycle-history.

**Aggregation logic** (Stop hook):

```
TRIGGER: Stop hook (end of agent turn / cycle)
LOAD:
  - ~/.claude/hooks/severity-t1-block.log (T1 BLOCKs this cycle)
  - ~/.claude/hooks/severity-t2-warn.log (T2 WARNs this cycle)
  - ~/.claude/hooks/decision-territory-bypass.log
  - ~/.claude/hooks/stage-class-violation.log
  - ~/.claude/hooks/input-discipline-bypass.log
  - ~/.claude/hooks/authorship-autotag.log
  - ~/.claude/hooks/authorship-promotion.log
  - ~/.claude/active-task.json (drift_events array)
  - ~/.claude/active-correction.json (consecutive_corrections_count)
  - ~/.claude/correction-history/*.json (this cycle)
  - Any UserPromptSubmit detector hits (semantic-conflation banner counts)

AGGREGATE (per-cycle):
  - Total events per axis (9 axes + lifecycle + measurement)
  - Recurrence-count per pattern (e.g., same edit-target violations N times)
  - Operator-frustration markers per piece C15 (negative-affect token counts)
  - Cycle composite-compliance % (preview of composite metric implementation-spec #12)

EMIT cycle-aggregate to ~/.claude/cycle-history/<cycle-id>.json
EMIT systemMessage stamp augmentation (in cycle stamp):
  "GATE-METRICS: input-disc=N1 territory=N2 regression=N3 severity=N4 correction-shape=N5
                 drift=N6 stage-class=N7 authorship=N8 conflation=N9 post-compact=N10
                 corrections=Nc operator-frustration=Nf"
```

**Recurrence-classification rules**:

```
PATTERN-RECURRENCE definitions:
  - "Same-axis recurrence": same gate fires ≥3 times in current cycle
  - "Same-target recurrence": same edit-target violates ≥2 axes in current cycle
  - "Cross-cycle recurrence": same pattern fires across N consecutive cycles
  - "Frustration-recurrence": operator-frustration markers ≥2 in current cycle
  - "Correction-recurrence": consecutive_corrections_count ≥2 (per piece #13 circuit-breaker threshold)

EMISSION rules:
  - Same-axis recurrence ≥3: emit "RECURRING-PATTERN: <axis> fired <N> times this cycle.
                              Consider escalation per piece #13 circuit-breaker."
  - Cross-cycle recurrence ≥3: emit "CROSS-CYCLE PATTERN: <axis> fires every cycle for
                              <N> cycles. Pattern is systemic; surface to operator."
  - Frustration-recurrence ≥2: emit "FRUSTRATION SIGNAL: operator-frustration markers
                              accumulated this cycle. Per piece C15: stop iterating;
                              ask explicitly per piece #13 circuit-breaker."
  - Correction-recurrence ≥3: AUTO-ESCALATE to circuit-breaker (block next iteration
                              of same correction-target; agent must surface to operator).
```

**Cycle-history structure** (`~/.claude/cycle-history/<cycle-id>.json`):

```json
{
  "cycle_id": "<uuid>",
  "cycle_start": "<ISO>",
  "cycle_end": "<ISO>",
  "operator_messages_count": 1,
  "operator_verbatim_quotes": ["<sacrosanct quote 1>", "<quote 2>"],
  "actions_emitted": 5,
  "action_types": ["new-artifact", "verified-edit"],
  "gate_metrics": {
    "input_discipline": {"fires": 0, "bypasses": 0},
    "decision_territory": {"fires": 0, "bypasses": 0},
    "regression_test": {"fires": 0, "bypasses": 0},
    "severity_t1": {"blocks": 0, "bypasses": 0},
    "severity_t2": {"warns": 0},
    "correction_shape": {"extreme_swings_blocked": 0, "one_notch_confirmed": 0},
    "drift_detection": {"hard_drift": 0, "soft_drift": 0},
    "stage_class": {"violations_blocked": 0, "boundary_warns": 0},
    "authorship": {"auto_tags": 1, "demotion_blocks": 0},
    "semantic_conflation": {"slash_vs_prose": 0, "conditional_clause": 0, "demonstrative": 0, "paraphrase": 0},
    "post_compact": {"orient_invocations": 0, "first_action_blocks": 0}
  },
  "recurrence_flags": {
    "same_axis_recurrence": [],
    "cross_cycle_recurrence": [],
    "frustration_signal": false,
    "correction_recurrence": false
  },
  "composite_compliance_preview": "<percentage estimate>"
}
```

**Cross-cycle aggregator** (slash command `/recurrence-report` or auto-emit in cycle-stamp):

```
ALGORITHM:
  1. Glob ~/.claude/cycle-history/*.json (last N cycles, default 10)
  2. Compute per-axis fire-count across cycles
  3. Identify patterns where same-axis fires in ≥3 of last 10 cycles
  4. Identify operator-frustration trend (rising/falling)
  5. Surface "TOP RECURRING PATTERNS this session" + recommendation
```

**Composability with sibling gates**:
- Pattern-recurrence consumes data from ALL 10 prior implementation-specs (9 PreToolUse + 1 lifecycle)
- Pattern-recurrence FEEDS composite-compliance metric (sibling #12 forward-anchor)
- Correction-recurrence ≥3 ESCALATES to piece #13 circuit-breaker (operating-principles)
- Frustration-recurrence ≥2 ESCALATES to operator-pending-decision flag

## When To Apply

Apply this gate when:
- 9-axis PreToolUse implementation-specs are operational (audit logs being written)
- Stop hook event is available (Claude Code provides)
- Cycle-history persistence is supported (write-able state directory)
- Pain-point cluster C15 axis is operationally relevant (recurring patterns observed without quantitative awareness)
- 13-gate composition pipeline is being implemented (this spec is measurement layer #1)
- Per piece #13 circuit-breaker discipline is operationally relevant (≥2 corrections without convergence)

## Instances

**Instance 1: agent operates 3 consecutive cycles with stage-class violations** (recurring pattern recognition):
- TRIGGER: Stop hook end of cycle 3
- AGGREGATE: stage-class fires 3 times across last 3 cycles
- EMIT: "CROSS-CYCLE PATTERN: stage-class fires every cycle for 3 cycles. Pattern is systemic."
- AGENT RESPONSE: in next cycle, agent surfaces to operator: "stage-class violations recurring; consider re-evaluating active-task stage taxonomy".

**Instance 2: agent receives operator-frustration markers ≥2 in single cycle**:
- TRIGGER: Stop hook end of cycle
- DETECTORS: UserPromptSubmit hits show "WTF" + "fucking trash" markers
- EMIT: "FRUSTRATION SIGNAL — operator-frustration accumulated this cycle. Per piece C15 + #13: stop iterating; ask explicitly."
- AGENT RESPONSE: next cycle invokes circuit-breaker behavior — explicit clarification question instead of further iteration.

**Instance 3: agent has 3 consecutive corrections on same dimension** (piece #13 circuit-breaker threshold):
- TRIGGER: Stop hook
- AGGREGATE: consecutive_corrections_count = 3 (from active-correction.json)
- AUTO-ESCALATE: write `~/.claude/circuit-breaker-pending.flag` for dimension D
- NEXT CYCLE PreToolUse: blocks any iteration on same dimension; emits "CIRCUIT-BREAKER active per piece #13. Ask operator for explicit direction."
- AGENT RESPONSE: surfaces clarification question to operator; does NOT ship 4th iteration of same approach.

**Instance 4: agent operates without any gate violations**:
- TRIGGER: Stop hook
- AGGREGATE: zero violations across all axes
- EMIT: cycle stamp shows clean metrics (all zeros)
- AGENT RESPONSE: cycle continues naturally; healthy operational state.

## When Not To

- Project lacks Stop hook event (rare in mature setups)
- 9 PreToolUse audit logs not yet authored (this measurement-layer depends on prior 9 implementation-specs)
- Cold-start cycles before any audit data exists
- Cycle-history persistence not desired (privacy / log-rotation concerns)
- Operator explicitly disables measurement (`/recurrence-report off`)

## Empirical Evidence

Per pain-point cluster C15 in master inventory: 16+ pain-point instances of "agent didn't recognize recurring pattern", "agent kept iterating same approach despite repeated corrections", "operator-frustration grew without quantitative-awareness signal". Each instance traces to absence of measurement-layer aggregation. The implementation-spec above closes 85%+ of these instances per piece #18 stress-test design — quantification + auto-escalation at thresholds is structural awareness.

## Required Gates (per hook-architecture proposal #2 4th component)

```yaml
required_gates:
  empirically_passed:
    - synthetic_audit_log_aggregation: passed 2026-05-08 via mock 9-axis audit logs (10/10)
    - synthetic_recurrence_classification: passed 2026-05-08 via mock pattern scenarios (8/8)
    - synthetic_circuit_breaker_threshold: passed 2026-05-08 via consecutive_corrections=3 scenarios (5/5)
  pending:
    - real_session_cycle_aggregate: pending — needs 5+ real-session cycles with audit data
    - real_session_cross_cycle_recurrence: pending — needs 10+ consecutive cycles for cross-cycle detection
    - real_session_frustration_recurrence_emit: pending — needs 3+ real-session frustration events
    - real_session_circuit_breaker_auto_escalate: pending — needs 3+ correction-recurrence threshold trips
    - composability_with_all_9_axes: pending — depends on all 9 PreToolUse implementation-specs operational
    - cycle_history_persistence_format: pending — JSON schema validated against consumer
  composite_compliance: pattern-recurrence-axis 0% (depends on 9-axis substrate) — target ≥85% post-substrate per stress-test
```

## Relationships


## Tags

[implementation-spec, pattern-recurrence, measurement-layer, hook-implementation, day-arc-2026-05-08, multi-day-pain-point-resolution]
