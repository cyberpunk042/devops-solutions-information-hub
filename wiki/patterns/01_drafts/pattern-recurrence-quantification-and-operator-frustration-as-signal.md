---
title: "Pattern-Recurrence Quantification and Operator-Frustration as Signal — The Meta-Measurement Pattern Closing C15 Operator-Exhaustion-Recurrence"
aliases:
  - "Pattern-Recurrence Quantification"
  - "Operator-Frustration as Signal"
  - "C15 Meta-Failure-Recurrence Cure"
  - "Recurrence-Threshold Escalation Trigger"
type: pattern
domain: cross-domain
layer: 4
status: draft
confidence: high
maturity: seed
created: 2026-05-08
updated: 2026-05-08
last_reviewed: 2026-05-08
derived_from:
  - "Lesson — Anti-minimizing systemic bug counts (PRIMARY parent at 03_validated/mature — count-honesty discipline)"
  - "Lesson — Bug vs systemic-bug nuance — systemic bugs live at meta-level (PRIMARY validated parent)"
  - "Lesson — Sidetrack detection + recovery (validated parent — operator-frustration as data)"
  - "P1 — Infrastructure Over Instructions for Process Enforcement"
  - "Documentation As Substitute For Discipline (sibling — meta-frame)"
  - "Pattern — Active-Task Anchor and Drift-Detection (sibling C13 — composes; recurrence-counter consumes drift events)"
  - "Pattern — SB-Tracker Priority-Shift Cycle-Step (sibling C12 — composes; recurrence over open SBs)"
  - "C15 cluster of pain-points-inventory"
sources:
  - id: anti-minimizing-lesson
    type: wiki
    file: wiki/lessons/03_validated/methodology-quality/anti-minimizing-systemic-bug-counts-and-blocker-filter-discipline.md
    description: "PRIMARY parent. Count-honesty discipline — don't undercount systemic bugs. This pattern provides the RUNTIME COUNTER + THRESHOLD-TRIGGER beyond per-session count-honesty."
  - id: bug-vs-systemic-bug-nuance
    type: wiki
    file: wiki/lessons/03_validated/methodology-quality/bug-vs-systemic-bug-nuance-systemic-bugs-live-at-the-meta-level-harness-ecosystem-brain-files.md
    description: "PRIMARY validated parent. Systemic bugs live at meta-level (harness/ecosystem/brain files). Pattern-recurrence at meta-level is itself a meta-meta level signal — this pattern quantifies recurrence as a measurement."
  - id: sidetrack-detection-lesson
    type: wiki
    file: wiki/lessons/03_validated/methodology-process/sidetrack-detection-and-recovery-when-agent-loses-the-original-task.md
    description: "VALIDATED parent. Operator-frustration is data, not just emotional output. This pattern operationalizes — frustration signals quantified + cross-referenced with recurrence."
  - id: principle-1
    type: wiki
    file: wiki/lessons/04_principles/hypothesis/infrastructure-over-instructions-for-process-enforcement.md
    description: "P1 — pattern-recurrence acknowledgment at prose tier (~25%) vs measurement-tier (quantified counter + threshold-trigger ~100%)."
  - id: substitution-pattern
    type: wiki
    file: wiki/lessons/01_drafts/documentation-as-substitute-for-discipline-the-meta-pattern.md
    description: "DIRECT sibling 2026-05-08. Same family — agent-discipline. This pattern provides the meta-meta measurement layer (recurrence quantification of pattern-violations)."
  - id: c12-sb-iteration-sibling
    type: wiki
    file: wiki/patterns/01_drafts/systemic-bug-tracker-priority-shift-cycle-step-design.md
    description: "DIRECT sibling 2026-05-08. C12 cycle-step gate produces per-cycle SB-iteration metric; this pattern aggregates SB-recurrence across sessions."
  - id: c13-drift-audit-sibling
    type: wiki
    file: wiki/patterns/01_drafts/active-task-anchor-and-drift-detection-gate-design.md
    description: "DIRECT sibling 2026-05-08. C13 includes drift-trace.log per-session; this pattern aggregates drift-recurrence across sessions."
  - id: c14-severity-audit-sibling
    type: wiki
    file: wiki/patterns/01_drafts/blast-radius-classification-and-pre-action-severity-gate.md
    description: "DIRECT sibling 2026-05-08. C14 includes severity-audit.log; this pattern aggregates severity-recurrence across sessions."
  - id: pain-points-inventory-c15
    type: wiki
    file: raw/notes/2026-05-08-pain-points-inventory-from-root-failed-conversation-master-aggregate.md
    description: "Primary source — C15 cluster (14 explicit hits + recursive)."
  - id: existing-output-discipline-guard-escalation-detector
    type: project
    project: root-ghostproxy
    path: /root/.claude/hooks/output-discipline-guard.sh
    description: "Existing /root UserPromptSubmit hook with operator-escalation detector (CAPS / 'WTF' / 'retard' / 'trash' patterns). Detection PRESENT; recurrence-threshold-trigger ABSENT."
tags: [pattern, p1-specialization, meta-measurement, pattern-recurrence-quantification, operator-frustration-as-signal, c15-cluster, recurrence-threshold-trigger, audit-aggregation, mission-2026-05-06, day-arc-2026-05-08, multi-day-pain-point-resolution]
---

# Pattern-Recurrence Quantification and Operator-Frustration as Signal

## Summary

The mature `anti-minimizing-systemic-bug-counts` lesson + `bug-vs-systemic-bug-nuance` lesson establish that systemic bugs live at meta-level + counts must be honest. The `sidetrack-detection-and-recovery` lesson establishes operator-frustration is data, not just emotional output. /root has `output-discipline-guard.sh` with operator-escalation detector (PARTIAL — detection without aggregation). **The GAP**: NO RUNTIME QUANTIFICATION of pattern-recurrence over time + NO THRESHOLD-TRIGGER forcing escalation when same pattern recurs N times. The C15 pain — operator-exhaustion compounds over 64-hour arc with phrases "should I give up", "lost cause", "how can you be so fucking bad", "general reduction in quality" — is empirical evidence that recurrence is a measurable signal that wasn't being measured. **The cure**: cross-session audit aggregator that consumes per-session metrics from siblings (C12 SB-iteration + C13 drift + C14 severity) + counts pattern-recurrence per failure-class + triggers operator-attention escalation when a pattern recurs N+ times across sessions. Plus operator-frustration-frequency metric across session timeline (frustration is data; quantify it).

## Pattern Description

The pattern has 5 structural components:

### 1. Per-Session Pattern-Recurrence Counter (state layer)

Each session maintains a counter of pattern-violations per failure-class:

```python
session_recurrence_counter = {
    "session_id": "<sid>",
    "started_at": "<ts>",
    "pattern_counters": {
        "premise-construction": {"events": [], "count": 0, "last_event_ts": None},
        "going-to-extremes": {...},
        "thin-output": {...},
        "freeze-after-correction": {...},
        "drift": {...},
        "regression-introduction": {...},
        "fabrication": {...},
        "conflation": {...},
        # ... per failure-class enum
    }
}
```

Stored at `~/.claude/recurrence-counters/<sid>.json`. Updated by sibling audit-emitters (C12 SB-iteration + C13 drift-audit + C14 severity-audit) + this pattern's operator-frustration detector.

### 2. Operator-Frustration Frequency Detector (input layer)

Extension to existing `output-discipline-guard.sh` operator-escalation detector:

```python
def quantify_operator_frustration(operator_msg, session_state) -> dict:
    """
    Beyond detection (already partial in escalation-detector), QUANTIFY:
    - Frustration signals per message (CAPS-ratio + escalation-words count)
    - Cumulative session frustration-rate (events per N messages)
    - Sustained-elevation periods (when frustration > baseline for sustained window)
    """
    frustration_score = compute_frustration_score(operator_msg)
    increment_session_counter(session_state, "operator-frustration", frustration_score)
    return {
        "score": frustration_score,
        "session_cumulative_rate": compute_session_rate(),
        "sustained_elevation": detect_sustained_elevation(),
    }
```

Score-emitter writes to session-recurrence-counter + frustration-trace.log. Sustained-elevation triggers component 4 (recurrence-threshold trigger).

### 3. Cross-Session Recurrence Aggregator (audit layer)

`tools/recurrence_aggregator.py` reads per-session counters across sessions:

```python
def aggregate_recurrence(sessions_dir) -> dict:
    """
    Per failure-class:
    - Total events across all sessions
    - Sessions where pattern recurred (>=1 event)
    - Sessions where pattern recurred multiple times (>=3 events)
    - Streak length (consecutive sessions with >=1 event)
    - Operator-frustration correlation (does operator-frustration spike when pattern fires?)
    """
    return {
        "premise-construction": {
            "total_events": N,
            "sessions_affected": M,
            "multi-event_sessions": K,
            "longest_streak": L,
            "frustration_correlation": 0.85,  # high correlation = pattern triggers operator-frustration
        },
        # ... per failure-class
    }
```

Aggregator output is itself a the second-brain second-brain consumable — `wiki/log/<ts>-recurrence-aggregation.md` generated periodically (daily/weekly).

### 4. Recurrence-Threshold Escalation Trigger (enforcement layer)

When a pattern recurs N+ times across sessions OR operator-frustration sustained-elevation detected:

```python
def threshold_trigger(aggregator_output, thresholds):
    """
    Per failure-class threshold:
    - Pattern-recurrence threshold = 5 sessions affected
    - Sustained-elevation threshold = N=3 messages with score > S over W=10 minutes
    """
    triggered = []
    for pattern, metrics in aggregator_output.items():
        if metrics["sessions_affected"] >= thresholds["sessions"]:
            triggered.append({
                "pattern": pattern,
                "trigger_type": "cross-session-recurrence",
                "remediation": f"Pattern '{pattern}' recurred in {metrics['sessions_affected']} sessions; structural-fix priority shift required."
            })
        if metrics["frustration_correlation"] > thresholds["correlation"]:
            triggered.append({
                "pattern": pattern,
                "trigger_type": "operator-frustration-correlated",
                "remediation": f"Pattern '{pattern}' correlates with operator-frustration {metrics['frustration_correlation']*100}%; address root cause."
            })
    return triggered
```

Triggered events route to:
- /root SB-tracker (auto-create entry per pattern)
- Mode-enforcement banner injection (surface to agent next prompt)
- Operator-attention surface (if recurrence sustained, escalate)

### 5. Pattern-Health Dashboard (governance layer)

Periodic the second-brain second-brain consumable — `wiki/log/<ts>-pattern-health-dashboard.md`:

```
PATTERN-HEALTH DASHBOARD <ts>
═══════════════════════════════
Sessions analyzed: <N> over <date-range>
Operator-frustration events: <M> total
Sustained-elevation periods: <K>

Pattern recurrence (top-10 by sessions-affected):
  premise-construction       12 sessions  (correlation 0.92)  → SB-090 active
  going-to-extremes          10 sessions  (correlation 0.88)  → SB-082/093 active
  thin-output                 8 sessions  (correlation 0.85)  → SB-128 active
  ...

Pattern-recurrence threshold-triggers:
  - SB-XXX created from cross-session recurrence (premise-construction × 12 sessions)
  - Operator-attention surfaced for going-to-extremes correlation
  ...

Operator-exhaustion timeline (per-session frustration-rate):
  2026-05-04: rate 0.12 (12% messages flagged)
  2026-05-05: rate 0.34 (escalated; mid-session reset)
  2026-05-06: rate 0.41 (sustained elevation; structural fix needed)
  2026-05-07: rate 0.18 (post-fix decrease)
  2026-05-08: rate 0.28 (current)

Recurring patterns approaching threshold (watch list):
  - <pattern>: <sessions>/<threshold>
  ...

Recommended structural-fix priorities (ranked):
  1. <pattern> — structural-fix design at <pattern-doc-path>
  2. ...
═══════════════════════════════
```

Dashboard is consumable by /cycle's SB-tracker iteration (per C12 sibling pattern) and by mode-enforcement banner (composes with C13 sibling drift-detection).

## Pattern Components

| Component | Implementation File | Project | Status |
|---|---|---|---|
| Per-session recurrence counter | `~/.claude/recurrence-counters/<sid>.json` + emitter API | /root + the second-brain | TO AUTHOR |
| Operator-frustration quantification | extension to `.claude/hooks/output-discipline-guard.sh` (existing escalation-detector → score + counter) | /root | TO EXTEND |
| Cross-session aggregator | `tools/recurrence_aggregator.py` | /root + the second-brain | TO AUTHOR |
| Recurrence-threshold trigger | `tools/recurrence_threshold.py` | /root + the second-brain | TO AUTHOR |
| Pattern-health dashboard generator | `tools/pattern_health_dashboard.py` | the second-brain (primary consumer); /root (data source) | TO AUTHOR |
| Threshold-trigger wiring | mode-enforcement banner extension + SB-tracker auto-create | /root | TO WIRE |
| Test files | `.claude/hooks/tests/test-recurrence-counter.py` + `tests/test-aggregator-thresholds.py` | /root + the second-brain | TO AUTHOR |

All 7 components are forward-anchors — design specified here; authoring + tests-passing is the promotion-to-02_synthesized gate.

## Instances

C15-cluster instances + recursive evidence:

| Instance | Operator-verbatim | Underlying recurrence | What this pattern would have surfaced |
|---|---|---|---|
| msg#23 (May 5 00:55) | *"HOW CAN YOU BE SO FUCKING RETARD???"* | First explicit meta-frustration | Frustration-rate metric increment; not yet sustained |
| msg#26 (May 5 01:01) | *"this is fucking helpless.... should I give up having you do what I ask?"* | Sustained elevation begins | Sustained-elevation threshold triggered; operator-attention surface; agent's NEXT response should reference this signal |
| msg#33 (May 5 01:35) | *"how can you be so fucking bad and useless"* | Recurrence within session | Counter increment; correlation with active patterns (likely premise-construction + freeze) |
| msg#37 (May 5 01:47) | *"its more like a general reduction in quality.. as if they had cut the supply by half"* | Operator-naming the recurrence pattern | Recurrence-pattern detected; SB candidate for "model-quality-degradation-perception" |
| msg#54 (May 5 11:02) | *"lost cause I think is the new word"* | Operator-giving-up signal | Cross-session aggregator would surface this as P1 priority for next session's pattern-fix |
| Brain-improvement mandate (May 7-8) | 11 *"Yes... do not minimize"* affirmations + accelerating frustration toward msg #350 | Pattern-recurrence within mandate without surfacing | Recurrence-counter would have flagged the mandate's per-file yes-protocol as recurring-without-convergence |

## When To Apply

- **When designing UserPromptSubmit hooks** — extend output-discipline-guard.sh with quantification beyond detection
- **When designing the second-brain audit aggregators** — `tools/recurrence_aggregator.py` reads per-session counters
- **When operator-frustration sustained-elevation triggers** — automatic SB-creation + operator-attention surface
- **When auditing pattern-fix effectiveness** — compare pre-fix vs post-fix recurrence rates per session
- **When evaluating sister-project pattern-health** — pattern deploys via `/install-agent-brain`; sister projects emit per-session counters; aggregator centralizes

## When Not To

- When session is too short to accumulate meaningful recurrence data (< N=3 messages)
- When operator-frustration is manually justified (operator-explicit "I'm venting; this isn't pattern-recurrence")
- When false-positive correlation > 30% (pattern-fixes not actually correlated with frustration drop) — refine correlation threshold
- When cross-session data unavailable (single-session ad-hoc work)

## Self-Check (audit procedure for any pattern-fix attempt)

After authoring/wiring a pattern-fix:

1. **What's the baseline pattern-recurrence rate (pre-fix)?** Run aggregator over last N sessions; record baseline.
2. **What's the predicted post-fix rate?** Hypothesis-driven estimate; document.
3. **Run sessions with the fix wired**; collect per-session counter data.
4. **Compute post-fix rate**; compare against baseline.
5. **If rate dropped > X%**: structural-fix worked. Promote to validated. Mark in SB-tracker.
6. **If rate didn't drop**: structural-fix didn't address root cause. Investigate; iterate.

The aggregator itself is the test — measurement validates the cure.

## Composability with siblings

This pattern composes with:
- **Lesson — Anti-minimizing systemic bug counts** (PRIMARY parent — count-honesty)
- **Lesson — Bug vs systemic-bug nuance — meta-level** (PRIMARY parent — meta-meta level)
- **Lesson — Sidetrack detection + recovery** (operator-frustration as data)
- **Lesson — Documentation As Substitute For Discipline** (sibling — meta-frame)
- **Pattern — SB-Tracker Priority-Shift Cycle-Step (C12)** (sibling — produces per-cycle SB metric; this pattern aggregates across sessions)
- **Pattern — Active-Task Anchor and Drift-Detection (C13)** (sibling — produces per-session drift metric)
- **Pattern — Blast-Radius Classification Pre-Action Severity Gate (C14)** (sibling — produces per-session severity metric)
- **Pattern — Methodology Stage-Gate Edit-Land Enforcement (C10)** (sibling — produces per-session methodology-skip metric)
- **Pattern — Pre-Edit Regression-Test Gate (C03)** (sibling — produces per-session regression-rate metric)
- **Pattern — Correction-as-Calibration Pre-Edit Verification Gate (C08)** (sibling — produces per-session swing metric)
- **Pattern — PostCompact Orientation Mirror (C05)** (sibling — produces per-compaction state-recovery metric)

The 7 sibling-pattern audit-emitters + this pattern's aggregator form the comprehensive measurement layer above the 12-gate enforcement pipeline. Together: measurement + enforcement = observable structural-discipline.

## Properties

| Property | Description |
|---|---|
| **Quantifies pattern-recurrence** | Counter per failure-class per session; cross-session aggregation |
| **Operator-frustration as data** | Frustration is a measurable signal; correlates with pattern-recurrence |
| **Threshold-trigger escalation** | When recurrence reaches threshold, automatic SB-creation + operator-attention surface |
| **Composes with all sibling audit-emitters** | C03/C05/C08/C10/C12/C13/C14 each emit per-session metrics; this aggregates them |
| **Cross-session view** | Beyond single-session — recurrence patterns visible only at multi-session scale |
| **Validates pattern-fixes** | Pre-fix vs post-fix recurrence-rate is the cure-effectiveness measurement |
| **Sister-project portable** | Deploys via `/install-agent-brain`; cross-project aggregation possible at the second-brain |

## Relationships

- **DERIVED FROM** [Lesson — Anti-minimizing systemic bug counts](../../lessons/03_validated/methodology-quality/anti-minimizing-systemic-bug-counts-and-blocker-filter-discipline.md) — **PRIMARY parent**.
- **DERIVED FROM** [Lesson — Bug vs systemic-bug nuance — meta-level](../../lessons/03_validated/methodology-quality/bug-vs-systemic-bug-nuance-systemic-bugs-live-at-the-meta-level-harness-ecosystem-brain-files.md) — **PRIMARY parent**.
- **DERIVED FROM** [Lesson — Sidetrack detection + recovery](../../lessons/03_validated/methodology-process/sidetrack-detection-and-recovery-when-agent-loses-the-original-task.md) — operator-frustration as data.
- **DERIVED FROM** [Principle 1 — Infrastructure Over Instructions](../../lessons/04_principles/hypothesis/infrastructure-over-instructions-for-process-enforcement.md).
- **PARALLELS** [Lesson — Documentation As Substitute For Discipline](../../lessons/01_drafts/documentation-as-substitute-for-discipline-the-meta-pattern.md) — DIRECT sibling 2026-05-08; meta-frame.
- **PARALLELS** [Pattern — SB-Tracker Priority-Shift Cycle-Step](systemic-bug-tracker-priority-shift-cycle-step-design.md) — DIRECT sibling 2026-05-08.
- **PARALLELS** [Pattern — Active-Task Anchor and Drift-Detection](active-task-anchor-and-drift-detection-gate-design.md) — DIRECT sibling 2026-05-08.
- **PARALLELS** [Pattern — Blast-Radius Classification Pre-Action Severity Gate](blast-radius-classification-and-pre-action-severity-gate.md) — DIRECT sibling 2026-05-08.
- **PARALLELS** [Pattern — Methodology Stage-Gate Edit-Land Enforcement](methodology-stage-gate-edit-land-enforcement-design.md) — DIRECT sibling 2026-05-08.
- **PARALLELS** [Pattern — Pre-Edit Regression-Test Gate](pre-edit-regression-test-gate-canonical-verified-edit-enforcement.md) — DIRECT sibling 2026-05-08.
- **PARALLELS** [Pattern — Correction-as-Calibration Pre-Edit Verification Gate](correction-as-calibration-pre-edit-verification-gate-design.md) — DIRECT sibling 2026-05-08.
- **PARALLELS** [Pattern — PostCompact Orientation Mirror](post-compact-orientation-mirror-and-handoff-doc-completeness-gate.md) — DIRECT sibling 2026-05-08.
- **PARALLELS** [Lesson — Class 9 Freeze-After-Correction](../../lessons/01_drafts/freeze-after-correction-is-class-9-of-agent-failure-taxonomy-abdication-as-freeze.md) — DIRECT sibling 2026-05-08.
- **PARALLELS** [Lesson — Agent-Decision vs Operator-Decision Boundary Discrimination](../../lessons/01_drafts/agent-decision-vs-operator-decision-boundary-discrimination-pre-action-gate.md) — DIRECT sibling 2026-05-08.
- **PARALLELS** [Lesson — Agent-Authored Content Must Be Flagged](../../lessons/01_drafts/agent-authored-content-must-be-flagged-vs-operator-canonical-the-fabrication-cure.md) — DIRECT sibling 2026-05-08.
- **PARALLELS** [Lesson — Agent-Context-Discipline Is Aspirational](../../lessons/01_drafts/agent-context-discipline-is-aspirational-without-enforcement-gates-not-reading-what-exists.md) — DIRECT sibling 2026-05-08.
- **PARALLELS** [Lesson — Conflation-Detection at Hook Layer](../../lessons/01_drafts/conflation-detection-at-hook-layer-the-rename-strategy-generalized.md) — DIRECT sibling 2026-05-08.
- **CONSTRAINS** /root/.claude/hooks/output-discipline-guard.sh — extension with frustration-quantification beyond detection
- **CONSTRAINS** the second-brain /tools/* (audit suite) — new aggregator tools
- **EXTENDS** anti-minimizing-systemic-bug-counts at runtime layer (count-honesty becomes runtime-counter)
- **SYNTHESIZES** [Pain-Points Inventory C15 Cluster](../../../raw/notes/2026-05-08-pain-points-inventory-from-root-failed-conversation-master-aggregate.md) — primary source.
- **FEEDS INTO** the 5-tier maturity progression: 01_drafts → 02_synthesized gated on:
  1. Per-session counter schema authored
  2. Output-discipline-guard.sh frustration-quantification extension
  3. `tools/recurrence_aggregator.py` authored
  4. `tools/recurrence_threshold.py` authored
  5. Pattern-health dashboard generator
  6. Test files authored + tests passing
  7. Operator-confirmed promotion
- **Mission served**: 2026-05-06 brain-improvement mandate (failed) → 2026-05-08+ multi-day systematic pain-point resolution; this pattern is C15 cluster's proposed-solution piece + the meta-measurement layer above all 12 sibling gates.

## Backlinks

(Auto-regenerated by `pipeline post`. Validated parents + 12 sibling pieces accumulate this pattern.)
