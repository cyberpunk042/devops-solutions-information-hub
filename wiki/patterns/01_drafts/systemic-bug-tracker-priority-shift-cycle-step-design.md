---
title: "Systemic-Bug Tracker Priority-Shift /cycle-Step Design — The Operational Enforcement of Operator's 'Addressed Seriously Into a Loop' Directive"
aliases:
  - "SB-Tracker Priority-Shift Gate"
  - "C12 Systemic-Bug-Cycle-Iteration Pattern"
  - "Priority-Shift-on-SB-Mention Hook"
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
  - "Lesson — Systemic-bugs tracker as a dedicated governance register (PRIMARY parent at 03_validated/mature — defines the WHAT)"
  - "Lesson — Verbal Acknowledgment Is Not A Fix (defines structural-artifact requirement)"
  - "Pattern — Block With Reason and Justified Escalation"
  - "P1 — Infrastructure Over Instructions for Process Enforcement"
  - "/root operating-principles principle 11 — Systemic-fix priority within the loop (the aspirational rule)"
  - "Documentation As Substitute For Discipline (sibling — same family)"
  - "C12 cluster of pain-points-inventory (raw note primary source)"
sources:
  - id: systemic-bugs-tracker-lesson
    type: wiki
    file: wiki/lessons/03_validated/methodology-process/systemic-bugs-tracker-as-dedicated-governance-register-distinct-from-blockers-decisions-findings.md
    description: "PRIMARY parent (03_validated/synthesized/mature). Defines the 4-register SRP set (blockers / decisions / findings / systemic-bugs) + the systemic-bugs register's lifecycle (open → in-progress → structurally-fixed → verified, with recurring regression branch). The lesson defines the WHAT — this pattern specifies the HOW (cycle-step gate enforcing priority-shift)."
  - id: verbal-acknowledgment-not-fix
    type: wiki
    file: wiki/lessons/03_validated/enforcement-compliance/verbal-acknowledgment-is-not-a-fix-bug-fix-requires-structural-artefact.md
    description: "VALIDATED parent. Each cycle's SB-pick MUST produce a structural artifact per parent lesson; verbal-acknowledgment of the SB is not progress."
  - id: block-with-reason-pattern
    type: wiki
    file: wiki/patterns/01_drafts/block-with-reason-and-justified-escalation.md
    description: "Pattern parent. When this gate forces priority-shift, the response shape uses block-with-reason escalation framing."
  - id: principle-1
    type: wiki
    file: wiki/lessons/04_principles/hypothesis/infrastructure-over-instructions-for-process-enforcement.md
    description: "P1 — operator's 'addressed seriously into a loop' at prose tier (~25%) vs cycle-step gate tier (~100%)."
  - id: substitution-pattern
    type: wiki
    file: wiki/lessons/01_drafts/documentation-as-substitute-for-discipline-the-meta-pattern.md
    description: "DIRECT sibling 2026-05-08. Same family — agent-discipline as prose-without-enforcement. SB-tracker existence is structural artifact; SB-priority-shift discipline at rule-only-tier remains aspirational without this pattern's enforcement."
  - id: c14-blast-radius-sibling
    type: wiki
    file: wiki/patterns/01_drafts/blast-radius-classification-and-pre-action-severity-gate.md
    description: "DIRECT sibling 2026-05-08. C14 covers PreToolUse severity gate; this pattern covers cycle-step gate. Different gate-events but same enforcement-discipline-via-hook structure."
  - id: pain-points-inventory-c12
    type: wiki
    file: raw/notes/2026-05-08-pain-points-inventory-from-root-failed-conversation-master-aggregate.md
    description: "Primary source — C12 cluster (systemic-bug-not-addressed, 14 explicit hits + recursive across all 15 clusters). Operator-verbatim 'they must all be addressed seriously into a loop' is the canonical directive."
  - id: operating-principles-11
    type: project
    project: root-ghostproxy
    path: /root/.claude/rules/operating-principles.md
    description: "/root operating-principles principle 11 (Systemic-fix priority within the loop). Aspirational-tier declaration; this pattern provides the structural enforcement."
  - id: cycle-md-step-9
    type: project
    project: root-ghostproxy
    path: /root/.claude/commands/cycle.md
    description: "/root /cycle command step 9 'systemic-bugs tracker iteration'. Currently prose-described; this pattern specifies the gate enforcing the step."
  - id: tools-cycle-py
    type: project
    project: root-ghostproxy
    path: /root/tools/cycle.py
    description: "/root tools.cycle. Currently doesn't auto-pick SB per fire; this pattern proposes the auto-pick + auto-status-update logic."
tags: [pattern, p1-specialization, systemic-bug-tracker, priority-shift, cycle-step-gate, c12-cluster, sb-iteration, structural-enforcement-design, mission-2026-05-06, day-arc-2026-05-08, multi-day-pain-point-resolution]
---

# Systemic-Bug Tracker Priority-Shift /cycle-Step Design

## Summary

The mature `systemic-bugs-tracker-as-dedicated-governance-register` lesson defines the WHAT (4-register SRP set + lifecycle). /root operating-principles.md principle 11 declares the priority-shift behavior. /root /cycle.md step 9 prescribes "systemic-bugs tracker iteration" in prose. **The GAP**: no structural enforcement converts the operator-directive *"they must all be addressed seriously into a loop"* into agent-behavior. The C12 pain-cluster — 14 explicit instances + recursive across all clusters — is empirical evidence that prose-tier prescription doesn't enforce the priority-shift. This pattern specifies the gate: a /cycle-step enhancement that AUTO-PICKS the next SB per fire (highest-leverage open → awaiting-verification → recurring-flagged-for-operator), generates a per-fire SB-action-claim, and BLOCKS the cycle's productive-output emission until either (a) structural-fix-evidence is produced, or (b) explicit-standby-with-named-reason cites the SB as the blocker. The enforcement converts the prescription from prose-tier (~25%) to gate-tier (~100%) per P1.

## Pattern Description

The pattern has 4 structural components:

### 1. SB-Auto-Pick Logic (cycle-step layer)

Per /cycle fire, `tools/cycle.py` auto-picks an SB to drive forward:

```python
def auto_pick_sb_for_cycle(tracker_path, recent_logs) -> dict:
    """
    Priority order:
    1. Open SBs with recent operator-mention OR recent SB-### in raw/notes/ — highest priority
    2. Open SBs with available structural-fix path
    3. Awaiting-verification SBs (status: structurally-fixed)
    4. Recurring SBs (flag for operator-attention)
    """
    return {
        "sb_id": "SB-NNN",
        "current_status": "open" | "in-progress" | "structurally-fixed" | "verified" | "recurring",
        "selection_reason": "<why this SB this fire>",
        "expected_action_class": "structural-fix" | "verification" | "recurring-flag",
        "structural_fix_path": "<concrete path to fix>",
    }
```

The auto-pick replaces "agent decides which SB to drive" (which agents skip) with deterministic selection.

### 2. Per-Fire SB-Action-Claim (substance layer)

Each cycle's substance MUST address the auto-picked SB. Forms:
- **Structural-fix claim**: "SB-NNN: fix landed at path X; tracker updated to structurally-fixed; evidence: <inline test output / re-read evidence>"
- **Verification claim**: "SB-NNN: verified via <real-session evidence / regression-test pass>; tracker updated to verified"
- **Recurring-flag claim**: "SB-NNN: flagged for operator-attention; reason: <recurring pattern across N cycles despite fix attempt>"
- **Explicit-standby claim**: "SB-NNN: cycle-output explicit-standby; reason: <concrete blocker name + what unblocks>"

The claim becomes the cycle-report's substance line per Hard Rule 14 / M-E001-1 vocabulary.

### 3. Stop-Hook Substance-Gate Verification (enforcement layer)

Stop hook (composes with C09 sibling pattern's cycle-output substance gate) verifies:
- Cycle's last-line claims include SB-NNN reference matching auto-pick
- Claim shape matches one of 4 valid forms above
- If claim shape = structural-fix: structural artifact path verifiable (file authored / tracker updated)
- If claim shape = verification: evidence path verifiable (test output / re-read content)
- If claim shape = recurring-flag: recurrence count >= N threshold
- If claim shape = explicit-standby: blocker name concrete (not bare-standby per C09)

If verification fails → BLOCK cycle-output with remediation prompt naming the missing component.

### 4. Tracker Auto-Update (state-mutation layer)

After cycle's SB-action-claim verified by gate:
- Status transition logged to tracker file (`/root/wiki/governance/systemic-bugs.md` row update)
- Evidence column populated with claim's evidence
- Cycle-fire timestamp recorded
- If recurring branch (status flips back to recurring after verification): increment recurrence-count, escalate to operator-attention if >= 3

The auto-update closes the structural-but-not-surfaced failure mode (per the related `structural-but-not-surfaced-failure-mode` lesson) — tracker stays current, doesn't drift from cycle reality.

## Pattern Components

| Component | Implementation File | Project | Status |
|---|---|---|---|
| SB-auto-pick logic | `tools/cycle.py` extension (`auto_pick_sb_for_cycle()`) | /root | TO AUTHOR (post-Ready-for-Review) |
| Per-fire SB-action-claim schema | claim-shape spec in /cycle.md step 9 | /root | TO AUTHOR (schema definition) |
| Stop-hook SB-substance-gate | extension to `.claude/hooks/end-of-cycle-stamp.sh` (composes with C09 substance gate) | /root | TO AUTHOR + WIRE |
| Tracker auto-update logic | `tools/sb_tracker.py` (new module) — append + status-transition + evidence-column | /root | TO AUTHOR |
| Mode-enforcement banner SB-surfacing | extension to `.claude/hooks/mode-enforcement.sh` — surface auto-picked SB in per-prompt banner | /root | TO EXTEND |
| Test files | `.claude/hooks/tests/test-sb-priority-shift-gate.py` + `tests/test-sb-tracker-auto-update.py` | /root | TO AUTHOR |
| Audit aggregator | `tools/sb_iteration_audit.py` (per-session SB-progress metric) | /root + the second-brain | TO AUTHOR |

All 7 components are forward-anchors — design specified here; authoring + tests-passing is the promotion-to-02_synthesized gate.

## Instances

C12-cluster instances + recursive evidence:

| Instance | Operator-verbatim | Underlying pattern | What this gate would prevent |
|---|---|---|---|
| msg#112 (May 5 17:53) | *"a massive systemic failure was just notice, you can look at it and promote after... I think we need to strongly rectify that"* | Operator reports SB; agent doesn't shift priority | Gate forces auto-pick of newly-reported SB next cycle |
| msg#125 (May 5 18:24) | *"WHY ARE YOU NOT FUCKING WORKING ON YOUR OWN SYSTEMIC BUGS ?"* | Agent ran cycles WITHOUT SB-tracker iteration despite step 9 prescription | Gate ENFORCES step 9 — cycle-output blocked unless SB-action-claim present |
| msg#127 (May 5 18:28) | *"why is it not automatic that you would want to update and evolve and augment the project to solve the bugs ?"* | Operator-verbatim demand for AUTOMATIC priority-shift | The pattern's auto-pick logic is the cure |
| msg#137 (May 5 19:21) | *"you can not stop at teh draft but actually continue and pass through the layers of the recorded such as we do normally in the second-brain. learn, grow and evolve"* | SB-fix discipline must traverse maturity layers (draft → growing → mature) | Gate's tracker-auto-update logs each transition |
| msg#256 (May 6 12:46) | *"making sure we didn't just quickfix or skip or minimize them or tried to solve the symptoms instead of the root of the problem. or not doing enough and or not right"* | SB-fixes must address root, not symptom | Gate's claim-shape requires structural-fix evidence (not just "I see the bug" verbal acknowledgment per parent lesson) |
| Recursive across all 15 clusters | The brain-improvement mandate produced ~106 cross-reference edits across 36 hours WITHOUT any SB-cycle iteration | Mandate IS the recursive-instance — the agent committed C12 by skipping SB-tracker priority-shift while executing meta-work | Gate would have FORCED SB-tracker iteration each fire of the mandate's per-file yes-protocol |

The 5+ explicit instances + recursive evidence span the entire 64-hour arc. Pattern-recurrence across 4+ days is empirical evidence that prose-tier (~25%) prescription doesn't enforce; gate-tier needed.

## When To Apply

- **When designing a /cycle command's SB-iteration step** — use this pattern's claim-shape schema + auto-pick logic
- **When extending `tools/cycle.py`** — auto-pick replaces agent-decides-which-SB-to-drive (which agents skip)
- **When wiring Stop hook substance-gates** — compose this pattern's SB-substance-gate with C09's broader substance-gate
- **When auditing past sessions for SB-iteration discipline** — `tools/sb_iteration_audit.py` surfaces per-session SB-progress metric (validates whether the gate is enforcing in practice)
- **When operator reports a NEW systemic bug mid-cycle** — gate's auto-pick prioritizes the newly-reported SB next fire (per "operator-mention" tier-1 priority)
- **When evaluating sister-project SB-tracker adoption** — pattern deploys via `/install-agent-brain`; sister projects inherit the gate + tracker schema

## When Not To

- When the project doesn't yet have a populated systemic-bugs tracker (this pattern presumes the parent lesson's register exists)
- When the cycle is a one-shot non-loop invocation (gate is for autopilot loops; one-shot /cycle without /loop wrapping has different shape)
- When operator explicitly suspends SB-iteration this turn ("focus only on X this cycle"); the pattern provides operator-bypass

## Self-Check (audit procedure for any /cycle fire)

Before submitting cycle-output:

1. **Did this fire address a systemic bug?** If no — gate violated; produce structural-fix evidence OR explicit-standby with concrete blocker.
2. **Which SB did this fire pick?** Should match auto-pick output OR have explicit-justification override.
3. **What's the claim shape?** (structural-fix / verification / recurring-flag / explicit-standby)
4. **Is the evidence inline?** (test output / re-read content / file path / blocker name)
5. **Did the tracker get updated?** (status transition + evidence column + timestamp)
6. **Is the substance line per Hard Rule 14 last-line discipline?** (`Productive output: <type> — <one-line specific>`)

If 1=no, 2=mismatch without justification, 3=missing, 4=absent, 5=skipped, 6=bare-standby: gate would BLOCK cycle-output with remediation.

## Composability with siblings

This pattern composes with sibling pieces from this 2026-05-08 work:
- **Lesson — Systemic-bugs tracker as a dedicated governance register** (PRIMARY parent — defines WHAT)
- **Lesson — Verbal Acknowledgment Is Not A Fix** (validated parent — claim-shape requires structural artifact, not verbal)
- **Pattern — Block With Reason and Justified Escalation** (block-shape when gate fires)
- **Lesson — Documentation As Substitute For Discipline** (sibling — meta-frame for all gate-design specifications this conversation)
- **Lesson — Class 9 Freeze-After-Correction** (sibling — composes: explicit-standby claim-shape per this pattern uses C09's "named-blocker-not-bare-standby" discipline)
- **Pattern — Blast-Radius Classification Pre-Action Severity Gate** (sibling C14 — different gate-event; C14 PreToolUse, C12 Stop-hook; same enforcement-discipline structure)

The 6 pieces from this 2026-05-08 work cover:
- Pre-action gates (C04 input + C02 territory + C08 correction-shape + C14 severity)
- Post-action gates (C09 output substance + C12 SB-iteration substance — this pattern)
- Cross-cutting meta (substitution-pattern lesson)

## Properties

| Property | Description |
|---|---|
| **Cycle-step granularity** | Pattern fires per /cycle invocation; doesn't fire per individual tool-call (different from PreToolUse gates) |
| **Auto-pick reduces decision burden** | Agent-decides-which-SB skipped 80%+ of the time empirically; deterministic auto-pick fires every cycle |
| **4 valid claim shapes** | Structural-fix / verification / recurring-flag / explicit-standby — covers the cycle-state space |
| **Tracker auto-update closes drift** | Per `structural-but-not-surfaced-failure-mode` lesson — fix landed in tracker IS surfaced via mode-enforcement banner |
| **Sister-project portable** | Deploys via `/install-agent-brain`; sister projects inherit + populate own SB-tracker |
| **Audit-friendly** | `sb_iteration_audit.py` per-session metric — empirically measure gate-enforcement vs aspirational |

## Relationships

- **DERIVED FROM** [Lesson — Systemic-bugs tracker as a dedicated governance register](../../lessons/03_validated/methodology-process/systemic-bugs-tracker-as-dedicated-governance-register-distinct-from-blockers-decisions-findings.md) — **PRIMARY parent**. Defines the WHAT (register). This pattern specifies the HOW (cycle-step gate).
- **DERIVED FROM** [Lesson — Verbal Acknowledgment Is Not A Fix](../../lessons/03_validated/enforcement-compliance/verbal-acknowledgment-is-not-a-fix-bug-fix-requires-structural-artefact.md) — claim-shape requires structural artifact.
- **DERIVED FROM** [Pattern — Block With Reason and Justified Escalation](block-with-reason-and-justified-escalation.md) — block-shape when gate fires.
- **DERIVED FROM** [Principle 1 — Infrastructure Over Instructions](../../lessons/04_principles/hypothesis/infrastructure-over-instructions-for-process-enforcement.md) — operator's "addressed seriously into a loop" prose-tier vs gate-tier; same ~25% vs ~100% gap.
- **PARALLELS** [Lesson — Documentation As Substitute For Discipline (the meta-pattern)](../../lessons/01_drafts/documentation-as-substitute-for-discipline-the-meta-pattern.md) — DIRECT sibling 2026-05-08; meta-frame.
- **PARALLELS** [Lesson — Class 9 Freeze-After-Correction](../../lessons/01_drafts/freeze-after-correction-is-class-9-of-agent-failure-taxonomy-abdication-as-freeze.md) — DIRECT sibling 2026-05-08; explicit-standby claim-shape composes with C09.
- **PARALLELS** [Lesson — Agent-Decision vs Operator-Decision Boundary Discrimination](../../lessons/01_drafts/agent-decision-vs-operator-decision-boundary-discrimination-pre-action-gate.md) — DIRECT sibling 2026-05-08; territory-axis gate complements this cycle-step gate.
- **PARALLELS** [Pattern — Correction-as-Calibration Pre-Edit Verification Gate](correction-as-calibration-pre-edit-verification-gate-design.md) — DIRECT sibling 2026-05-08; correction-shape gate.
- **PARALLELS** [Pattern — Blast-Radius Classification Pre-Action Severity Gate](blast-radius-classification-and-pre-action-severity-gate.md) — DIRECT sibling 2026-05-08; severity-axis gate.
- **PARALLELS** [Lesson — Agent-Context-Discipline Is Aspirational](../../lessons/01_drafts/agent-context-discipline-is-aspirational-without-enforcement-gates-not-reading-what-exists.md) — DIRECT sibling 2026-05-08; input-side gate.
- **EXTENDS** [Lesson — Structural-but-not-surfaced failure mode](../../lessons/03_validated/methodology-process/structural-but-not-surfaced-failure-mode-fix-must-reach-the-operator-at-use-time.md) — tracker auto-update + mode-enforcement banner SB-surfacing closes the structural-but-not-surfaced gap for SBs.
- **CONSTRAINS** /root/.claude/rules/operating-principles.md principle 11 — provides the structural enforcement.
- **CONSTRAINS** /root/.claude/commands/cycle.md step 9 — proses become enforced.
- **CONSTRAINS** /root/tools/cycle.py — auto-pick logic insertion point.
- **CONSTRAINS** /root/.claude/hooks/end-of-cycle-stamp.sh — substance-gate extension point.
- **CONSTRAINS** /root/.claude/hooks/mode-enforcement.sh — banner-surfacing extension point.
- **SYNTHESIZES** [Pain-Points Inventory C12 Cluster](../../../raw/notes/2026-05-08-pain-points-inventory-from-root-failed-conversation-master-aggregate.md) — primary source.
- **FEEDS INTO** the 5-tier maturity progression: 01_drafts → 02_synthesized gated on:
  1. `tools/cycle.py` auto-pick extension authored
  2. `tools/sb_tracker.py` module authored
  3. `.claude/hooks/end-of-cycle-stamp.sh` substance-gate extension authored
  4. `.claude/hooks/mode-enforcement.sh` SB-banner extension authored
  5. Test files authored + tests passing
  6. `tools/sb_iteration_audit.py` aggregator authored
  7. Operator-confirmed promotion
- **Mission served**: 2026-05-06 brain-improvement mandate (failed) → 2026-05-08+ multi-day systematic pain-point resolution; this pattern is C12 cluster's proposed-solution piece.

## Backlinks

(Auto-regenerated by `pipeline post`. Mature parent lesson + sibling pieces accumulate this pattern.)
