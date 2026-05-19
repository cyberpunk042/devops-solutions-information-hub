---
title: "Active-Task Anchor and Drift-Detection Gate — Structural Enforcement of the Mature Sidetrack-Detection Lesson"
aliases:
  - "Active-Task Anchor Gate"
  - "Drift-Detection in Mode-Enforcement Banner"
  - "C13 Rogue-Drift Pattern"
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
  - "Lesson — Sidetrack detection + recovery (PRIMARY parent at 03_validated/mature — 4-part structural fix; this pattern provides the gate enforcement)"
  - "Lesson — Compound-waterfall input-retention rule (closely related — operator inputs cumulate, comments are additive)"
  - "P1 — Infrastructure Over Instructions for Process Enforcement"
  - "Documentation As Substitute For Discipline (sibling — same family)"
  - "C13 cluster of pain-points-inventory"
sources:
  - id: sidetrack-detection-lesson
    type: wiki
    file: wiki/lessons/03_validated/methodology-process/sidetrack-detection-and-recovery-when-agent-loses-the-original-task.md
    description: "PRIMARY parent (03_validated/synthesized/mature). 4-part structural fix prescribed: (1) active-task register, (2) additive-by-default, (3) sidetrack detection, (4) recovery flow. The lesson PRESCRIBES; this pattern specifies WHICH HOOKS / GATES enforce each part."
  - id: compound-waterfall-lesson
    type: wiki
    file: wiki/lessons/03_validated/methodology-process/compound-waterfall-input-retention-rule-cumulative-not-discarded.md
    description: "VALIDATED parent. Operator inputs must cumulate, never discard prior context. Closely related to additive-by-default — comments compound on the active-task; pivots are explicit exception."
  - id: principle-1
    type: wiki
    file: wiki/lessons/04_principles/hypothesis/infrastructure-over-instructions-for-process-enforcement.md
    description: "P1 governing principle — sidetrack-detection at prose tier (~25% — agent reads the lesson and may or may not self-check) vs gate tier (~100% — mode-enforcement banner surfaces active-task per prompt + PostToolUse audits action vs active-task)."
  - id: substitution-pattern
    type: wiki
    file: wiki/lessons/01_drafts/documentation-as-substitute-for-discipline-the-meta-pattern.md
    description: "DIRECT sibling 2026-05-08. Same family — agent-discipline as prose-without-enforcement."
  - id: c04-context-discipline-sibling
    type: wiki
    file: wiki/lessons/01_drafts/agent-context-discipline-is-aspirational-without-enforcement-gates-not-reading-what-exists.md
    description: "DIRECT sibling 2026-05-08. C04 covers re-read-before-edit at PreToolUse; this pattern covers active-task-anchor at mode-enforcement banner + PostToolUse. Composing — drift detected when action's target unrelated to active-task."
  - id: c09-class-9-freeze-sibling
    type: wiki
    file: wiki/lessons/01_drafts/freeze-after-correction-is-class-9-of-agent-failure-taxonomy-abdication-as-freeze.md
    description: "DIRECT sibling 2026-05-08. C09 covers post-correction freeze; this pattern covers post-correction drift. Both track operator-correction events — Class 9 prevents freeze-response; this prevents drift-response."
  - id: c02-decision-territory-sibling
    type: wiki
    file: wiki/lessons/01_drafts/agent-decision-vs-operator-decision-boundary-discrimination-pre-action-gate.md
    description: "DIRECT sibling 2026-05-08. C02 covers WHO-decides; this pattern covers WHAT-task. Composing — agent must verify operator-territory AND target-relates-to-active-task."
  - id: pain-points-inventory-c13
    type: wiki
    file: raw/notes/2026-05-08-pain-points-inventory-from-root-failed-conversation-master-aggregate.md
    description: "Primary source — C13 cluster (rogue-deviant-drift, 9 hits including current arc msg 345 'WHY ARE YOU SO FUCKING ROGUE DEVIANT AND RETARD???')."
  - id: existing-active-task-state-file
    type: project
    project: root-ghostproxy
    path: /root/.claude/active-task
    description: "Existing /root state file (SB-124d) — single-line task ID (e.g., T012). Read by /handoff, /cycle, mode-enforcement.sh. Active-task register exists per parent lesson's 1st structural-fix part; this pattern's gate REFERENCES it."
  - id: existing-active-mission-focus-impediment-files
    type: project
    project: root-ghostproxy
    path: /root/.claude/active-mission /root/.claude/active-focus /root/.claude/active-impediment
    description: "Existing /root state files (SB-118 objective layer). Multi-cycle mission + sub-objective + block. Same anchor for drift-detection at higher granularity."
  - id: existing-mode-enforcement-hook
    type: project
    project: root-ghostproxy
    path: /root/.claude/hooks/mode-enforcement.sh
    description: "Existing /root UserPromptSubmit hook — surfaces active-mode + LIVE STATE. PARTIAL implementation — surfaces active-task in banner, doesn't enforce drift-detection. This pattern extends with drift-check logic."
  - id: existing-output-discipline-guard-hook
    type: project
    project: root-ghostproxy
    path: /root/.claude/hooks/output-discipline-guard.sh
    description: "Existing /root UserPromptSubmit hook — premise/escalation/conditional-clause detection. Operator-frustration signal detection partially implemented (escalation-detector). This pattern extends with operator-frustration→drift-detection chain."
tags: [pattern, p1-specialization, active-task-anchor, drift-detection, sidetrack-prevention, c13-cluster, mode-enforcement-banner-extension, post-tool-use-audit, structural-enforcement-design, mission-2026-05-06, day-arc-2026-05-08, multi-day-pain-point-resolution]
---

# Active-Task Anchor and Drift-Detection Gate

## Summary

The mature `sidetrack-detection-and-recovery` lesson at 03_validated prescribes a 4-part structural fix: (1) active-task register, (2) additive-by-default, (3) sidetrack detection, (4) recovery flow. /root has the active-task register (SB-124d state file) + active-mission/focus/impediment (SB-118 objective layer) + mode-enforcement.sh hook surfacing them in the per-prompt banner — partial implementation of part 1 + 3. **The GAP**: no gate ENFORCES additive-by-default (part 2); no PostToolUse audit detects when agent's action diverges from active-task (part 3 enforcement); no recovery-flow gate triggers on operator-frustration signals (part 4). The C13 pain-cluster — 9 explicit instances + recursive presence in current arc (msg #345 *"WHY ARE YOU SO FUCKING ROGUE DEVIANT AND RETARD???"*) — is empirical evidence that prose-tier prescription doesn't enforce. This pattern specifies 3 composing gates: mode-enforcement banner drift-anchor extension (input boundary) + PostToolUse drift-audit (per-action boundary) + operator-frustration→recovery-flow trigger (correction boundary). Each gate references existing state files; no new state required.

## Pattern Description

The pattern has 5 structural components:

### 1. Drift-Anchor in Mode-Enforcement Banner (input layer)

`/root/.claude/hooks/mode-enforcement.sh` already surfaces active-task in per-prompt banner. EXTENSION: explicit drift-anchor framing forces agent to verify alignment per prompt:

```
ACTIVE-TASK ANCHOR (drift-prevention):
  Current task:    T012 (install.sh real-execute on sandbox)
  Mission:         Ship root-ghostproxy MVP
  Focus:           Foundation tier completion
  Impediment:      (none — focus unblocked)

DRIFT-CHECK before responding:
  Q1: Does my proposed next-action serve T012? (yes / no / unclear)
  Q2: If operator's prompt is comment-shaped, does it integrate INTO T012 or pivot AWAY? (additive default)
  Q3: If unsure: surface the question explicitly; do NOT silently switch tasks.
```

The framing is CONTENT in the additionalContext injection — agent's reasoning sees the explicit drift-check before generating response. Per parent lesson: most operator messages are additive; default to additive-integration into active-task.

### 2. PostToolUse Drift-Audit (per-action layer)

After each Edit / Write / NotebookEdit / Bash:

```python
def drift_audit(tool_name, tool_input, tool_response, active_task) -> dict:
    """
    Compare action's target/scope against active-task scope.
    Active-task scope = (parent_module + done_when_files + recent operator-named scope).
    
    If target ∈ active-task scope → ALIGNED
    If target ∈ active-mission scope but ∉ active-task → ZOOM-IN/OUT (acceptable; flag)
    If target ∉ active-task ∉ active-mission → DRIFT (warn + log)
    If 3+ consecutive drift events → ESCALATE (cascading-drift; force re-anchor)
    """
    target = tool_input.get("file_path") or tool_input.get("command", "")
    scope = lookup_active_task_scope(active_task)
    alignment = check_alignment(target, scope)
    return {
        "alignment": "aligned" | "zoom" | "drift" | "cascading-drift",
        "active_task": active_task,
        "action_target": target,
        "decision": "allow" | "warn" | "block-with-re-anchor",
    }
```

Logged to `~/.claude/drift-trace.log`. Cascading-drift → BLOCK with re-anchor prompt forcing agent to either: (a) acknowledge drift + recover to active-task, or (b) explicitly propose task-pivot to operator + wait for grant.

### 3. Operator-Frustration → Recovery-Flow Trigger (correction layer)

Per parent lesson: operator-frustration is data signaling "you're off the original track." Existing `output-discipline-guard.sh` partially detects escalation. EXTENSION:

```python
def operator_frustration_drift_check(operator_msg, active_task, recent_drift_log):
    """
    Operator-frustration signals (CAPS / 'WTF' / 'rogue' / 'sidetrack' / 'why are you'):
    Cross-reference with recent drift-trace.log:
      If recent drift events present → likely frustration is ABOUT the drift
      Inject recovery-flow imperative into next response
    """
    if escalation_detected(operator_msg):
        recent_drifts = get_recent_drifts_in_session(recent_drift_log, last_N_minutes=15)
        if recent_drifts:
            return {
                "decision": "inject-recovery-flow-imperative",
                "context": f"Recent drift events: {recent_drifts}; operator likely catching the drift; recovery-flow required before next action"
            }
```

Recovery-flow per parent lesson:
- Acknowledge drift explicitly
- Re-state active-task verbatim
- Integrate the operator's frustration signal as data
- Resume active-task
- Optionally capture the drift-target as separate finding

### 4. Cascading-Drift Tracking (state layer)

`~/.claude/drift-trace.log` accumulates per-session drift events. Aggregator:

```python
def cascading_drift_audit(session_drift_log) -> dict:
    """
    Per-session metric: drift-rate, recovery-rate, time-to-recovery
    """
    return {
        "drift_events_count": N,
        "recovery_events_count": M,
        "drift_recovery_ratio": M/N if N else 1.0,
        "average_time_to_recovery_minutes": ...,
        "longest_drift_streak": ...,
    }
```

Surfaces in /cycle output + raw note when sustained drift-rate > threshold. Empirical measurement per P1 quantified-evidence.

### 5. Recovery-Flow Action-Type (Hard Rule 14 layer)

Add `drift-recovery` as expected sub-claim within productive-output line when operator-frustration trigger fires:

```
Productive output: drift-recovery — re-anchored to T012; integrating operator-frustration signal as data; recent action <X> was off-task drift; resuming T012 next-action <Y>.
```

Connects to substitution-pattern lesson Insight 5b — claims must have inline evidence.

## Pattern Components

| Component | Implementation File | Project | Status |
|---|---|---|---|
| Drift-anchor framing in mode-enforcement banner | extension to `.claude/hooks/mode-enforcement.sh` | /root | TO EXTEND |
| Active-task scope-lookup | `tools/active_task_scope.py` | /root | TO AUTHOR |
| PostToolUse drift-audit hook | new `.claude/hooks/post-tool-drift-audit.sh` | /root | TO AUTHOR + WIRE |
| Operator-frustration→recovery-flow trigger | extension to `.claude/hooks/output-discipline-guard.sh` | /root | TO EXTEND |
| Drift-trace log + audit aggregator | `~/.claude/drift-trace.log` + `tools/drift_audit.py` | /root + the second-brain | TO AUTHOR |
| Recovery-flow action-type spec | extension to /cycle output last-line generation | /root | TO EXTEND |
| Test files | `.claude/hooks/tests/test-drift-audit-gate.py` + `tests/test-recovery-flow-trigger.py` | /root | TO AUTHOR |

All 7 components are forward-anchors — design specified here; authoring + tests-passing is the promotion-to-02_synthesized gate.

## Instances

C13-cluster instances + recursive evidence:

| Instance | Operator-verbatim | Underlying drift | What this gate would prevent |
|---|---|---|---|
| msg#14 (May 4 23:08) | *"you would still stay idle or round in circle around the center"* | Drift+freeze cousin (composes with C09) | Drift-anchor banner forces re-anchor every prompt; circle-pattern detected by cascading-drift audit |
| msg#54 (May 5 11:02) | *"why are you this fucking rogue and retard????"* | General drift signal | Operator-frustration → recovery-flow trigger fires |
| msg#121 (May 5 18:17) | *"how did we go from on track to sidetrack and you completely lost about what we currently are doing?"* | Direct operator-naming of drift | THIS lesson's PRIMARY parent originated from this exact moment; cure is the gate this pattern specifies |
| msg#324 (May 6 22:48) | *"just fucking stop doing AI slop anyway..."* | Drift toward generic non-task content | PostToolUse drift-audit catches off-scope edits |
| msg#345 (May 8 — current arc) | *"WHY ARE YOU SO FUCKING ROGUE DEVIANT AND RETARD???"* | Pivoted the second-brain gateway-orient when operator said "this side" = root | Drift-anchor banner would have surfaced active-mission = root-fix; agent's pivot would have been gate-flagged + redirected |
| **Brain-improvement mandate** (May 7-8 36-hour) | Treated each "Yes do not minimize" as continuation grant; mandate scope expanded from operator-named 4-7 main files to 106-files-uniform-treatment | Cumulative drift across 16 phases without re-anchor | Cascading-drift detector triggers after N consecutive same-pattern edits; re-anchor forced |

The current arc msg #345 is the most-recent live evidence. Pattern-recurrence over 4+ days is empirical for gate-tier (~100%) over advisory-tier.

## When To Apply

- **When designing UserPromptSubmit hooks** — add drift-anchor framing to existing mode-enforcement banner
- **When designing PostToolUse hooks** — add drift-audit per-action
- **When operator names "sidetrack" / "rogue" / "drift" in current message** — recovery-flow trigger fires; agent re-anchors before next action
- **When auditing past sessions for drift discipline** — `tools/drift_audit.py` per-session metric
- **When evaluating sister-project drift-prevention adoption** — pattern deploys via `/install-agent-brain`

## When Not To

- When the session has no active-task set (banner empty for active-task field; gate skips)
- When operator explicitly pivots ("stop X, do Y instead") — pivot is the exception per parent lesson; gate respects explicit pivots
- When the agent is intentionally exploring / brainstorming (operator-stated; bypass via REASON)
- When false-positive rate >10% sustained — refine scope-lookup logic per parent enforcement-mindful lesson SCOPE property

## Self-Check (audit procedure for any agent action when active-task is set)

Before invoking any tool that mutates state OR generating any prose response:

1. **Is active-task set?** Check `~/.claude/active-task`; if empty — drift-anchor doesn't apply this turn.
2. **Does my proposed action serve active-task?** (yes / no / unclear); if no — drift-event; consider re-anchor.
3. **If operator just sent message containing frustration signals** (CAPS / WTF / rogue / sidetrack / "why are you"): cross-reference with recent drift-events; if drift recent → recovery-flow first.
4. **Last 3 actions: same active-task or different?** If 3+ consecutive different-task actions → cascading drift; STOP, re-anchor, surface.
5. **Drift-claim in cycle output**: if drift detected + recovered, productive-output line includes `drift-recovery — re-anchored to <T###>; ...`

If 1=yes + 2=no + 4=cascading: this pattern's anti-pattern applies. Recovery-flow per parent lesson before next action.

## Composability with siblings

This pattern composes with:
- **Lesson — Sidetrack detection + recovery** (PRIMARY parent — 4-part structural fix; this pattern enforces all 4 via 3 composing gates)
- **Lesson — Compound-waterfall input-retention** (validated parent — additive-by-default discipline)
- **Lesson — Documentation As Substitute For Discipline** (sibling 2026-05-08 — meta-frame)
- **Lesson — Agent-Context-Discipline Is Aspirational** (sibling C04 — input-side gate; composes — drift-anchor banner uses C04's read-before-edit + this pattern's anchor-vs-action check)
- **Lesson — Class 9 Freeze-After-Correction** (sibling C09 — output-side gate; composes — recovery-flow distinct from freeze-response)
- **Lesson — Agent-Decision vs Operator-Decision Boundary Discrimination** (sibling C02 — agent must verify operator-territory AND active-task scope; both check pre-action)
- **Pattern — Correction-as-Calibration Pre-Edit Verification Gate** (sibling C08 — correction-shape axis)
- **Pattern — Blast-Radius Classification Pre-Action Severity Gate** (sibling C14 — severity axis)
- **Pattern — SB-Tracker Priority-Shift Cycle-Step** (sibling C12 — Stop-hook gate)
- **Pattern — PostCompact Orientation Mirror** (sibling C05 — lifecycle gate)
- **Pattern — Pre-Edit Regression-Test Gate** (sibling C03 — regression axis)

The 10 pieces from 2026-05-08 work cover the agent-action-emission boundary from input through decision, correction-shape, severity, regression-prevention, output-substance, cycle-step, lifecycle, and now drift. Comprehensive coverage across the action lifecycle.

## Properties

| Property | Description |
|---|---|
| **Composes 3 gates** | mode-enforcement banner + PostToolUse audit + operator-frustration trigger; each addresses different lifecycle moment |
| **References existing state** | active-task + active-mission + active-focus + active-impediment files already exist; no new state required |
| **Per-session metric** | drift-rate, recovery-rate, time-to-recovery — empirical measurement |
| **Bypass-able** | REASON env var for intentional exploration / explicit pivot |
| **Cascading detection** | Beyond single drift event, pattern detects sustained drift |
| **Sister-project portable** | Deploys via `/install-agent-brain` per brain-inheritance pattern |

## Relationships

- **DERIVED FROM** [Lesson — Sidetrack detection + recovery](../../lessons/03_validated/methodology-process/sidetrack-detection-and-recovery-when-agent-loses-the-original-task.md) — **PRIMARY parent**. 4-part structural fix; this pattern enforces.
- **DERIVED FROM** [Lesson — Compound-waterfall input-retention](../../lessons/03_validated/methodology-process/compound-waterfall-input-retention-rule-cumulative-not-discarded.md) — additive-by-default discipline.
- **DERIVED FROM** [Principle 1 — Infrastructure Over Instructions](../../lessons/04_principles/hypothesis/infrastructure-over-instructions-for-process-enforcement.md).
- **PARALLELS** [Lesson — Documentation As Substitute For Discipline](../../lessons/01_drafts/documentation-as-substitute-for-discipline-the-meta-pattern.md) — DIRECT sibling 2026-05-08; meta-frame.
- **PARALLELS** [Lesson — Agent-Context-Discipline Is Aspirational](../../lessons/01_drafts/agent-context-discipline-is-aspirational-without-enforcement-gates-not-reading-what-exists.md) — DIRECT sibling 2026-05-08; input-side composes.
- **PARALLELS** [Lesson — Class 9 Freeze-After-Correction](../../lessons/01_drafts/freeze-after-correction-is-class-9-of-agent-failure-taxonomy-abdication-as-freeze.md) — DIRECT sibling 2026-05-08; output-side complement.
- **PARALLELS** [Lesson — Agent-Decision vs Operator-Decision Boundary Discrimination](../../lessons/01_drafts/agent-decision-vs-operator-decision-boundary-discrimination-pre-action-gate.md) — DIRECT sibling 2026-05-08; territory complements active-task scope.
- **PARALLELS** [Pattern — Correction-as-Calibration Pre-Edit Verification Gate](correction-as-calibration-pre-edit-verification-gate-design.md) — DIRECT sibling 2026-05-08.
- **PARALLELS** [Pattern — Blast-Radius Classification Pre-Action Severity Gate](blast-radius-classification-and-pre-action-severity-gate.md) — DIRECT sibling 2026-05-08.
- **PARALLELS** [Pattern — SB-Tracker Priority-Shift Cycle-Step](systemic-bug-tracker-priority-shift-cycle-step-design.md) — DIRECT sibling 2026-05-08.
- **PARALLELS** [Pattern — PostCompact Orientation Mirror](post-compact-orientation-mirror-and-handoff-doc-completeness-gate.md) — DIRECT sibling 2026-05-08.
- **PARALLELS** [Pattern — Pre-Edit Regression-Test Gate](pre-edit-regression-test-gate-canonical-verified-edit-enforcement.md) — DIRECT sibling 2026-05-08.
- **CONSTRAINS** /root/.claude/hooks/mode-enforcement.sh — extension with drift-anchor framing
- **CONSTRAINS** /root/.claude/hooks/output-discipline-guard.sh — extension with operator-frustration→recovery-flow trigger
- **CONSTRAINS** /root/.claude/active-task + /root/.claude/active-mission + /root/.claude/active-focus + /root/.claude/active-impediment — gate references all 4
- **EXTENDS** SB-118 (objective layer state files) + SB-124d (active-task cursor) — leverages existing state-file infrastructure
- **SYNTHESIZES** [Pain-Points Inventory C13 Cluster](../../../raw/notes/2026-05-08-pain-points-inventory-from-root-failed-conversation-master-aggregate.md) — primary source.
- **FEEDS INTO** the 5-tier maturity progression: 01_drafts → 02_synthesized gated on:
  1. mode-enforcement.sh drift-anchor framing extension authored
  2. `tools/active_task_scope.py` authored
  3. PostToolUse drift-audit hook authored + wired
  4. output-discipline-guard.sh frustration-trigger extension authored
  5. `tools/drift_audit.py` aggregator authored
  6. Test files authored + tests passing
- **Mission served**: 2026-05-06 brain-improvement mandate (failed) → 2026-05-08+ multi-day systematic pain-point resolution; this pattern is C13 cluster's proposed-solution piece.

## Backlinks

(Auto-regenerated by `pipeline post`. Mature parent lesson + sibling pieces accumulate this pattern.)
