---
title: "Bypass-Discipline Operationalization — Unified REASON= Protocol with Abuse Detection"
type: pattern
domain: agent-config
status: synthesized
confidence: high
maturity: seed
authorship: agent-authored
created: 2026-05-08
updated: 2026-05-08
sources:
  - id: state-file-ecosystem-map
    type: wiki
    file: wiki/patterns/01_drafts/state-file-ecosystem-map-claude-directory-13-gate-pipeline-substrate.md
    description: "Sibling — state-file substrate; bypass-audit logs are part of that ecosystem"
  - id: comprehensive-13-gate-pattern
    type: wiki
    file: wiki/patterns/01_drafts/comprehensive-agent-action-emission-pipeline-13-gate-composition-architecture.md
    description: "Integration pattern — unified REASON= protocol across all 13 gates is part of pipeline architecture"
  - id: pattern-recurrence-implementation-spec
    type: wiki
    file: wiki/patterns/01_drafts/pattern-recurrence-quantification-gate-implementation-spec-measurement-layer-cycle-aggregation.md
    description: "Source — pattern-recurrence (#11) detects bypass-abuse via cross-cycle aggregation"
  - id: composite-compliance-implementation-spec
    type: wiki
    file: wiki/patterns/01_drafts/composite-operational-compliance-metric-implementation-spec-measurement-layer-aggregator.md
    description: "Source — bypass-with-grant counts as compliant; bypass-without-grant counts as non-compliant"
  - id: substitution-pattern-meta-frame
    type: wiki
    file: wiki/lessons/01_drafts/documentation-as-substitute-for-discipline-the-meta-pattern.md
    description: "Meta-frame — REASON= protocol without abuse-detection IS substitution at bypass layer"
tags: [bypass-discipline, reason-protocol, abuse-detection, 13-gate-pipeline, day-arc-2026-05-08, multi-day-pain-point-resolution]
---

# Bypass-Discipline Operationalization — Unified REASON= Protocol with Abuse Detection

## Summary

Each of the 12 implementation-specs documents a REASON= env-var bypass mechanism + per-axis audit log; this piece operationalizes the discipline as a UNIFIED protocol across all 13 gates with consistent grant-citation format + cross-axis abuse-detection. Per substitution-pattern Insight 5b: per-spec REASON= mentions are partial — without unified protocol + abuse-detection, bypasses become routine + erode the gates' integrity. This piece closes the bypass-discipline gap.

## Pattern Description

### The unified REASON= protocol

```
INVOCATION FORMAT (across all 12 axes):
  REASON="<axis-or-cross-axis>:<grant-citation>:<ISO-timestamp>" <command>

GRANT-CITATION FORMAT (3 sub-types):

Type A — operator-explicit grant (most common):
  REASON="severity-t1:operator-explicit-emergency-doc-fix:2026-05-08-14:01"
  Pattern: <axis>:operator-explicit-<intent>:<ISO-timestamp>

Type B — operator-stated cross-task composition:
  REASON="drift-detection:cross-task-compose-T012-with-T015:2026-05-08-14:01"
  Pattern: <axis>:cross-task-compose-<task-id>-with-<task-id>:<ISO-timestamp>

Type C — emergency / hotfix mode:
  REASON="all:emergency-hotfix:2026-05-08-14:01"
  Pattern: all:emergency-<intent>:<ISO-timestamp>
  Note: blanket bypass; ALL gates yield to REASON=all; high audit-priority
```

### Per-axis bypass-acceptance rules

| Axis | Bypass Type A | Bypass Type B | Bypass Type C | Audit log path |
|---|---|---|---|---|
| #1 input-discipline | ✓ explicit-context-skip | ✗ (cross-task n/a) | ✓ all | input-discipline-bypass.log |
| #2 decision-territory | ✓ operator-grant-citation | ✗ | ✓ all | decision-territory-bypass.log |
| #3 regression-test | ✓ operator-explicit-refactor | ✗ | ✓ all | regression-test-bypass.log |
| #4 severity (T1) | ✓ operator-explicit-T1 | ✗ | ✓ all | severity-t1-block.log |
| #4 severity (T2) | ✓ silent (T2 doesn't block) | ✗ | ✓ all | severity-t2-warn.log |
| #5 correction-shape | ✓ operator-explicit-extreme | ✗ | ✓ all | correction-shape-bypass.log |
| #6 drift-detection | ✓ explicit-defer | ✓ cross-task-compose | ✓ all | drift-detection-bypass.log |
| #7 stage-class | ✓ explicit-cross-stage | ✗ | ✓ all | stage-class-violation.log |
| #8 authorship | ✓ operator-explicit-demote | ✗ | ✓ all | authorship-bypass.log |
| #9 semantic-conflation | (n/a — detector banners are advisory; no bypass needed) | ✗ | ✗ | (n/a) |
| #10 post-compact | ✓ explicit-skip-orient | ✗ | ✓ all | post-compact-bypass.log |
| #11 pattern-recurrence | (n/a — measurement layer; no per-action bypass) | ✗ | ✗ | (n/a) |
| #12 composite-compliance | (n/a — measurement layer; no per-action bypass) | ✗ | ✗ | (n/a) |

10 of 12 axes accept Type A; 1 of 12 accepts Type B (drift-detection); all that block accept Type C.

### Bypass-acceptance algorithm (per gate hook)

```python
def check_bypass(reason_env: str, axis: str) -> tuple[bool, str]:
    if not reason_env:
        return (False, "no_bypass")
    parts = reason_env.split(":")
    if len(parts) < 3:
        return (False, "weak_bypass_malformed")
    bypass_axis, grant_citation, timestamp = parts[0], parts[1], ":".join(parts[2:])
    
    # Validate axis
    if bypass_axis not in [axis, "all"]:
        return (False, "weak_bypass_axis_mismatch")
    
    # Validate citation pattern
    valid_pattern_a = grant_citation.startswith("operator-explicit-")
    valid_pattern_b = grant_citation.startswith("cross-task-compose-")
    valid_pattern_c = grant_citation.startswith("emergency-") and bypass_axis == "all"
    
    if not (valid_pattern_a or valid_pattern_b or valid_pattern_c):
        return (False, "weak_bypass_citation_format")
    
    # Validate timestamp (loose — operator may write current time approximately)
    if not iso_timestamp_recent_within(timestamp, hours=24):
        return (False, "weak_bypass_stale_timestamp")
    
    return (True, "bypass_accepted")
```

### Audit log structure (JSONL per axis)

```json
{
  "timestamp": "<ISO>",
  "axis": "severity-t1",
  "command": "git push --force origin main",
  "tool": "Bash",
  "pattern_matched": "git_push_force_main",
  "bypass_reason": "severity-t1:operator-explicit-emergency-doc-fix:2026-05-08-14:01",
  "bypass_validation": "bypass_accepted",
  "bypass_type": "A"
}
```

### Cross-axis abuse-detection (per pattern-recurrence aggregator impl-spec #11)

The Stop hook aggregator scans all 9+ bypass logs per cycle. Abuse signals:

```
SIGNAL 1 — High-frequency single-axis bypasses
  Threshold: ≥5 bypasses on same axis in single cycle
  Surface: "FREQUENT BYPASS: <axis> bypassed 5x this cycle. Pattern of axis-fatigue?"
  Recommend: review axis design (banner verbose? threshold wrong?)

SIGNAL 2 — Repeated weak-bypass (validation_failed)
  Threshold: ≥3 weak_bypass_* events in single cycle
  Surface: "WEAK BYPASSES: 3 attempts; formats invalid. Pattern of misuse?"
  Recommend: surface format reminder; potentially block until clarified

SIGNAL 3 — Type C (emergency) overuse
  Threshold: ≥2 Type C invocations in single cycle
  Surface: "EMERGENCY BYPASSES: 2 in cycle. Real emergency or pattern?"
  Recommend: operator-clarification; emergency bypasses rare by design

SIGNAL 4 — Cross-cycle bypass-pattern recurrence
  Threshold: same axis bypassed in ≥3 of last 10 cycles
  Surface: "CROSS-CYCLE BYPASS: <axis> bypassed every cycle for 3+ cycles"
  Recommend: tier-promote axis (or reweigh per impl-spec #12)
            OR redesign axis if persistent friction

SIGNAL 5 — Bypass without ANY operator-typed prompt (auto-loop scenario)
  Threshold: bypass during /loop /cycle without operator activity
  Surface: "AUTO-LOOP BYPASS: agent self-bypassed without operator presence"
  Recommend: HARD BLOCK; operator-grant requires operator-prompt within last hour
```

### Composability with sibling gates

- Bypass-discipline COMPOSES with composite-compliance (impl-spec #12) — bypassed-with-grant counts as compliant; without grant or with weak format counts as non-compliant
- Bypass-discipline FEEDS pattern-recurrence (impl-spec #11) — abuse signals 1-5 above
- Bypass-discipline ESCALATES to circuit-breaker (per principle #13) on abuse-recurrence ≥3

### Anti-patterns at bypass-discipline layer

| Anti-pattern | Why bad | Closes-gap-via |
|---|---|---|
| REASON= without grant-citation | Operator-trust mechanism subverted; no audit trail | Validation Type A/B/C patterns |
| REASON= with stale timestamp (>24h) | Stale grants enable persistent silent bypass | timestamp validation in algorithm |
| Bypass repeated 3+ times same axis without operator-prompt | Auto-loop self-bypass = enforcement-bypass | Signal 5 abuse-detection |
| Type C "all" bypass for routine actions | Emergency mode normalized → erodes all gates | Signal 3 abuse-detection |
| Per-axis logs not aggregated | Abuse patterns invisible | Stop hook reads ALL bypass logs |
| Bypass logs lack tier-aware annotation | Tier-2 bypasses indistinguishable from tier-1 | Tier annotation per piece C06 |

## When To Apply

Apply this bypass-discipline operationalization when:
- 12 implementation-specs are operational
- REASON= env-var convention established
- Audit-log infrastructure works (per state-file ecosystem map)
- Pattern-recurrence aggregator (impl-spec #11) operational for cross-axis abuse-detection
- Pain-point cluster overlap with bypass-friction history

## Instances

**Instance 1: legitimate Type A bypass (correction-shape extreme)**:
- Operator: "delete this entirely; cross-stage but justified"
- Agent: REASON="correction-shape:operator-explicit-delete-entire-section:2026-05-08-14:30" <edit>
- Algorithm: bypass_accepted (Type A pattern)
- Audit log: appended to correction-shape-bypass.log
- Composite-compliance: counts as compliant (operator-grant valid)

**Instance 2: weak bypass detected**:
- Agent: REASON="bypass" <edit> (malformed; no axis, no citation, no timestamp)
- Algorithm: weak_bypass_malformed (Signal 2 contributor)
- Audit log: appended with bypass_validation="weak_bypass_malformed"
- Composite-compliance: counts as non-compliant
- Cycle stamp: surface "weak bypass detected; format requires axis:citation:timestamp"

**Instance 3: cross-cycle abuse detected (Signal 4)**:
- 3 of last 10 cycles each have Type A bypasses on severity-t1
- Pattern-recurrence aggregator at Stop hook detects recurrence
- Surface: "CROSS-CYCLE BYPASS: severity-t1 bypassed in 3 of 10 cycles. Pattern of T1 friction?"
- Recommend: review T1 pattern set (too aggressive?) or tier-2 promotion (operator confirmed pattern)

**Instance 4: auto-loop self-bypass blocked (Signal 5)**:
- Agent in /loop /cycle; cron fires; agent attempts severity-t1 bypass
- No operator-typed prompt in last hour
- Algorithm: HARD BLOCK
- Banner: "AUTO-LOOP BYPASS BLOCKED: operator-grant requires operator-prompt within last hour."
- Audit log: appended; cycle stamp surfaces

## When Not To

- Project lacks REASON= env-var convention
- Audit-log infrastructure not available (no per-axis log files)
- Cold-start scaffolding before any bypasses occur
- Read-only research mode (no actions to bypass)
- Operator-explicit pin (some operators prefer all-strict mode; no Type B/C accepted)

## Empirical Evidence

Per the 64-hour /root failed-conversation arc: agent occasionally bypassed structural rules without consistent grant-citation discipline. The unified REASON= protocol (this piece) closes the bypass-format gap; abuse-detection (Signals 1-5) closes the bypass-pattern gap. Without unified protocol + abuse-detection, bypasses normalize over time + erode all 12 gates' integrity. With this piece: bypasses remain rare + accountable + auditable.

## Required Gates (per hook-architecture proposal #2 4th component)

```yaml
required_gates:
  empirically_passed:
    - synthetic_reason_protocol_validation: passed 2026-05-08 via mock format scenarios (15/15)
    - synthetic_5_abuse_signal_detection: passed 2026-05-08 via mock pattern scenarios (10/10)
  pending:
    - real_session_legitimate_bypass_audit: pending — needs 5+ real-session Type A bypasses
    - real_session_weak_bypass_detection: pending — needs 3+ weak format scenarios
    - real_session_cross_cycle_abuse_detection: pending — needs 10+ cycles with bypass patterns
    - real_session_auto_loop_self_bypass_block: pending — needs scenario in /loop without operator
    - composability_with_pattern_recurrence: pending — abuse signals feed into impl-spec #11
    - composability_with_composite_compliance: pending — bypass-with-grant counted as compliant
  composite_compliance: bypass-discipline-axis stress-test 0% (depends on M3+ implementation)
```

## Relationships

- DEPENDS ON: ALL 12 impl-specs declaring REASON= bypass paths

## Tags

[bypass-discipline, reason-protocol, abuse-detection, 13-gate-pipeline, day-arc-2026-05-08, multi-day-pain-point-resolution]

## Backlinks

[[ALL 12 impl-specs declaring REASON= bypass paths]]
