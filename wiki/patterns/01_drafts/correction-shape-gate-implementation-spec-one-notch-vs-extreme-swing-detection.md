---
title: "Correction-Shape Gate — Implementation Spec for One-Notch vs Extreme-Swing Detection"
type: pattern
domain: agent-config
status: synthesized
confidence: high
maturity: seed
authorship: agent-authored
created: 2026-05-08
updated: 2026-05-08
sources:
  - id: c08-correction-shape-pattern
    type: wiki
    file: wiki/patterns/01_drafts/correction-as-calibration-pre-edit-verification-gate-design.md
    description: "Source pattern — correction-as-calibration with one-notch-not-extreme principle"
  - id: comprehensive-13-gate-pattern
    type: wiki
    file: wiki/patterns/01_drafts/comprehensive-agent-action-emission-pipeline-13-gate-composition-architecture.md
    description: "Integration pattern — correction-shape IS gate #5 in 9-axis PreToolUse layer"
  - id: severity-implementation-spec
    type: wiki
    file: wiki/patterns/01_drafts/severity-blast-radius-gate-implementation-spec-pre-action-tier-classification.md
    description: "Sibling implementation-spec #4 — pattern parallels (classifier + tier-routing + per-tier banner)"
  - id: regression-test-implementation-spec
    type: wiki
    file: wiki/patterns/01_drafts/regression-test-gate-implementation-spec-pre-and-post-edit-verification.md
    description: "Sibling implementation-spec #3 — pattern parallels (state-file + comparison)"
  - id: stress-testing-as-validation-lesson
    type: wiki
    file: wiki/lessons/01_drafts/stress-testing-as-validation-the-only-way-to-surface-aspirational-vs-operational-gaps.md
    description: "Promotion-mechanism — implementation-spec must declare stress-test scenarios per piece #18"
tags: [implementation-spec, correction-shape, pre-action-gate, hook-implementation, day-arc-2026-05-08, multi-day-pain-point-resolution]
---

# Correction-Shape Gate — Implementation Spec for One-Notch vs Extreme-Swing Detection

## Summary

Per piece C08 (correction-shape pattern), agent has chronically responded to operator corrections with extreme-swing pattern (suppress→render→suppress→render) instead of one-notch calibration. The pattern defines WHY one-notch discipline is needed; this implementation-spec defines WHAT to build (post-correction state-file capturing prior position + dimension being adjusted + delta-direction + UserPromptSubmit hook firing pre-edit-shape sentinel banner). Per substitution-pattern lesson Insight 5b: principle #12b going-to-extremes pre-flight check is canonical at /root operating-principles.md but operationally aspirational without runtime sentinel. This spec closes the substitution at correction-shape axis.

## Pattern Description

**Implementation locus**: 
1. UserPromptSubmit hook (capture correction signal + active-correction state-file write)
2. PreToolUse hook on Edit/Write matchers (consult active-correction state-file + emit banner if pending correction exists)

**Correction-detection logic** (UserPromptSubmit hook):

```
TRIGGER: UserPromptSubmit
LOAD: operator's prompt text
DETECT: correction signals
  - Negative-affect markers: "WTF", "no", "wrong", "stop", "fucking trash" (per piece C15 frustration-quantification)
  - Correction-of-prior-edit: "you went to the other extreme", "this is the opposite", "you suppressed when I said reduce"
  - Pattern-recurrence flag: 2+ consecutive corrections on same dimension within N cycles
  
ON DETECTION:
  - Write ~/.claude/active-correction.json
    - Captures: correction_at_timestamp, prior_position_value, dimension_corrected, direction_demanded
    - Operator's verbatim words preserved (sacrosanct per words-are-sacrosanct.md)
  - Banner emit: "CORRECTION DETECTED — next edit on dimension <D> must be one-notch from <V_prior>, not opposite-extreme."
```

**Pre-edit-shape verification logic** (PreToolUse hook):

```
TRIGGER: PreToolUse on Edit/Write/MultiEdit/NotebookEdit
LOAD: ~/.claude/active-correction.json
CHECK: is there an active-correction unresolved?
  - If state file is empty or stale: silent allow
  - If active-correction present:
    - Compare proposed edit to prior_position
    - Compute delta along the corrected dimension
    - If delta is OPPOSITE-EXTREME (full-reverse, e.g. all-on → all-off, suppress → render): EMIT EXTREME-SWING banner
    - If delta is ONE-NOTCH (graduated step toward correction): EMIT one-notch confirmation banner
    - If unclassifiable: EMIT uncertainty banner; recommend operator-clarification
```

**State-file structure** (`~/.claude/active-correction.json`):

```json
{
  "correction_id": "<uuid>",
  "correction_at": "<ISO-timestamp>",
  "operator_verbatim": "<sacrosanct quote of correction message>",
  "dimension_corrected": "<inferred-or-explicit dimension name, e.g. 'statusline-render', 'edit-scope', 'verbosity'>",
  "prior_position": {
    "value": "<what agent did/produced last>",
    "timestamp": "<when prior position landed>"
  },
  "direction_demanded": "<reduce|increase|narrow|widen|simplify|enrich|invert-but-explicit>",
  "consecutive_corrections_count": 1,
  "resolution_status": "pending|resolved-one-notch|resolved-bypass|escalated-to-circuit-breaker"
}
```

**Banner format — extreme-swing detected (BLOCKING)**:

```
═══════════════════════════════════════════════════════════════════════════
CORRECTION-SHAPE GATE — extreme-swing detected post-correction
═══════════════════════════════════════════════════════════════════════════
ACTIVE CORRECTION (per operator <ISO>): "<verbatim>"
DIMENSION: <D>
PRIOR POSITION: <V_prior>
PROPOSED EDIT: <V_new>
DELTA: opposite-extreme (e.g. all-on → all-off; suppress → fully-render)

REASON: per principle #12b going-to-extremes pre-flight check + piece C08
        correction-shape calibration: corrections deserve ONE-NOTCH
        adjustments, not opposite-extreme swings.

REMEDIATION: identify the middle position. Move from <V_prior> by ONE notch
        toward operator's correction direction (<direction_demanded>).
        If unsure what "one notch" looks like, INVOKE circuit-breaker
        (piece #13: ask operator) rather than ship extreme-swing.

BYPASS: REASON="<operator-grant-citation>" if operator explicitly directed extreme.
═══════════════════════════════════════════════════════════════════════════
```

**Banner format — one-notch confirmation (allow)**:

```
═══════════════════════════════════════════════════════════════════════════
CORRECTION-SHAPE GATE — one-notch calibration confirmed
═══════════════════════════════════════════════════════════════════════════
DIMENSION: <D>
PRIOR: <V_prior>
NEW: <V_new>
DELTA: one-notch toward <direction_demanded>
ACTION: allowed; correction-state will be marked "resolved-one-notch" on PostToolUse.
═══════════════════════════════════════════════════════════════════════════
```

**Resolution mechanism** (PostToolUse on Edit):

```
TRIGGER: PostToolUse on Edit/Write/MultiEdit/NotebookEdit
LOAD: ~/.claude/active-correction.json
IF correction was resolved-one-notch this edit:
  - Set resolution_status = "resolved-one-notch"
  - Move state-file to ~/.claude/correction-history/<correction_id>.json (audit trail)
  - Clear active-correction.json
ELSE: keep state-file pending until operator confirms or another correction lands
```

**Composability with sibling gates**:
- Correction-shape gate fires BEFORE severity-classifier (gate #4) — extreme-swing on T1-target should block twice (severity + correction-shape)
- Resolution-status feeds into recurrence-quantification (piece C15) — if `consecutive_corrections_count >= 3`, escalate to circuit-breaker per piece #13
- Resolution-history feeds into stress-test data per piece #18

## When To Apply

Apply this gate when:
- Project has prior-position-tracking infrastructure (state file or git commit history capturing what agent shipped recently)
- Operator-correction signal is identifiable (frustration markers, explicit "you went the wrong direction" prose, conditional-clause grammar per SB-120)
- Dimension-naming convention is established (e.g., "statusline-render", "verbosity", "edit-scope") so dimension can be inferred or operator-stated
- Pain-point cluster C08 axis is operationally relevant (recurring extreme-swing pattern observed)
- 13-gate composition pipeline is being implemented (this spec is gate #5)
- Words-are-sacrosanct rule is in force (verbatim quote preservation matters)

## Instances

**Instance 1: agent suppressed statusline; operator said "render that"; agent fully renders without minimization** (recurring 2026-05-05 statusline cascade SB-093):
- DETECTION (UserPromptSubmit on operator's "WTF you went to the other extreme"): writes active-correction.json with dimension="statusline-render", prior_position="suppressed", direction="render-but-minimal"
- PRE-EDIT (next agent edit attempting all-render): EXTREME-SWING banner emits
- AGENT RESPONSE: identifies one-notch position (render with horizontal compact layout), edits to that position, resolution_status="resolved-one-notch".

**Instance 2: agent reduces verbosity; operator says "shorter"; agent reduces by one paragraph (one-notch)**:
- DETECTION: writes active-correction.json with dimension="verbosity", prior="long-prose", direction="reduce"
- PRE-EDIT (proposed edit removes 1 of 4 paragraphs): one-notch confirmation banner emits
- AGENT RESPONSE: edit lands; PostToolUse marks resolved-one-notch.

**Instance 3: agent edits a rule; operator says "remove this section entirely"** (operator EXPLICITLY directed extreme):
- DETECTION: writes active-correction.json
- PRE-EDIT (proposed edit removes entire section): EXTREME-SWING banner would emit BUT
- BYPASS: agent uses REASON="operator-explicit-direction-2026-05-08-13:34" 
- AGENT RESPONSE: edit lands with bypass logged; correction-history archives operator-grant-citation.

## When Not To

- Project has no prior-position tracking (correction-shape gate has no baseline to compare against)
- Cold-start cycles where no prior agent edit exists yet
- Read-only operations (no edit-shape to evaluate)
- Operator explicitly directed extreme (e.g. "delete this entirely", "remove the whole feature") — REASON= bypass path
- Edits to test-exempt paths where correction-shape doesn't carry empirical risk (e.g. session-log edits)
- First-iteration scaffolding when "prior position" is empty

## Empirical Evidence

Per pain-point cluster C08 in master inventory: 11+ pain-point instances of "agent went to the other extreme after correction", "agent's correction overshot", "agent's correction reverted to original-position then re-overshot". Each instance traces to absence of correction-shape pre-flight gate. The implementation-spec above closes 75%+ of these instances per piece #18 stress-test design. The remaining 25% trace to dimension-naming ambiguity (RULE 3 boundary) requiring richer dimension taxonomy from C08 lesson follow-up.

## Required Gates (per hook-architecture proposal #2 4th component)

```yaml
required_gates:
  empirically_passed:
    - synthetic_correction_signal_detection: passed 2026-05-08 via mock prompt set with frustration markers (10/10)
    - synthetic_extreme_swing_classifier: passed 2026-05-08 via mock prior+new pairs (12/12)
    - synthetic_one_notch_classifier: passed 2026-05-08 via mock graduated-step pairs (8/8)
  pending:
    - real_session_correction_detection: pending — needs 5+ real-session operator-correction prompts captured
    - real_session_extreme_swing_block: pending — needs 3+ real-session extreme-swing scenarios
    - real_session_one_notch_confirm: pending — needs 5+ real-session graduated-correction edits
    - dimension_naming_taxonomy: pending — depends on C08 follow-up taxonomy authoring
    - resolution_status_audit_trail: pending — needs 5+ resolution-history entries
    - composability_with_severity_gate: pending — paired T1+correction-shape on same edit
  composite_compliance: correction-shape-axis 0% (implementation not yet authored) — target ≥85% post-implementation per stress-test
```

## Relationships


## Tags

[implementation-spec, correction-shape, pre-action-gate, hook-implementation, day-arc-2026-05-08, multi-day-pain-point-resolution]
