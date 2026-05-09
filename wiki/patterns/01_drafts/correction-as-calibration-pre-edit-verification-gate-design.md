---
title: "Correction-as-Calibration Pre-Edit Verification Gate — Hook Design Pattern Codifying the Mature Going-to-Extremes Lesson"
aliases:
  - "Pre-Edit Calibration Verification Gate"
  - "C08 Going-to-Extremes Hook Design"
  - "Calibrate-vs-Swing Verification at Action Boundary"
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
  - "Lesson — Correction-as-calibration, not swing: the going-to-extremes anti-pattern (PRIMARY parent at 03_validated/mature)"
  - "P1 — Infrastructure Over Instructions for Process Enforcement"
  - "Documentation As Substitute For Discipline (sibling — same family of structural-enforcement-vs-prose discipline)"
  - "Agent-Context-Discipline Is Aspirational Without Enforcement Gates (sibling)"
  - "Class 9 — Freeze-After-Correction (sibling — same agent-action-discipline subspace)"
  - "C08 cluster of pain-points-inventory (raw note primary source)"
sources:
  - id: correction-as-calibration-mature-lesson
    type: wiki
    file: wiki/lessons/03_validated/enforcement-compliance/correction-as-calibration-not-swing-the-going-to-extremes-anti-pattern.md
    description: "PRIMARY parent — the mature 03_validated/synthesized lesson. Prescribes a 5-step verification (identify spectrum → identify current point → identify proposed-correction's point → calibrate-vs-swing test → if-swing-apply-calibrated-fix-instead). The lesson PRESCRIBES the verification but does NOT specify how to ENFORCE it structurally — that's this pattern's contribution."
  - id: principle-1
    type: wiki
    file: wiki/lessons/04_principles/hypothesis/infrastructure-over-instructions-for-process-enforcement.md
    description: "P1 — verification-step at prose tier ~25% compliance vs hook-tier ~100%. This pattern converts the mature lesson's verification step from prose to enforcement gate."
  - id: refine-triggers-companion
    type: wiki
    file: wiki/lessons/03_validated/enforcement-compliance/refine-triggers-not-revoke-permissions-when-fixing-overzealous-rules.md
    description: "COMPOSES with this pattern — the specific case (rule edits with permission semantics); this pattern's gate design covers ALL correction shapes including refine-triggers cases."
  - id: pain-points-inventory-c08
    type: wiki
    file: raw/notes/2026-05-08-pain-points-inventory-from-root-failed-conversation-master-aggregate.md
    description: "Primary source — C08 cluster (going-to-extremes; 0 explicit hits + many implicit sequence-patterns). The /root failed-conversation arc 2026-05-04 → 2026-05-08 contributed 4+ new sequence-instance evidence rows: stamp render position (start↔end pendulum), uniform Cross-references footers (zero↔every-file binary), premise-construction-then-opposite-extreme on 'this side' interpretation, mandate scope (minimize↔2.6k-line additive)."
  - id: documentation-as-substitute-sibling
    type: wiki
    file: wiki/lessons/01_drafts/documentation-as-substitute-for-discipline-the-meta-pattern.md
    description: "DIRECT sibling 2026-05-08 — same family of structural-enforcement-required for agent-discipline rules. This pattern is one of the structural-enforcement artifacts that lesson prescribes."
  - id: c09-class-9-freeze-sibling
    type: wiki
    file: wiki/lessons/01_drafts/freeze-after-correction-is-class-9-of-agent-failure-taxonomy-abdication-as-freeze.md
    description: "DIRECT sibling 2026-05-08 — Class 9 of taxonomy. C08 (this) and C09 (Class 9 freeze) are paired correction-shape failure modes: C08 is over-correction (swing); C09 is under-correction (freeze). Both fail at the action-boundary; both need gate enforcement."
  - id: agent-context-discipline-sibling
    type: wiki
    file: wiki/lessons/01_drafts/agent-context-discipline-is-aspirational-without-enforcement-gates-not-reading-what-exists.md
    description: "DIRECT sibling 2026-05-08 — agent-input-side discipline. This pattern covers correction-shape at action-output boundary. Together: input gates (read-before-edit) + correction-shape gates (calibrate-vs-swing) + output gates (forward-not-backward) = full agent-discipline subspace coverage."
tags: [pattern, p1-specialization, p4-specialization, going-to-extremes, correction-shape, calibrate-vs-swing, structural-enforcement-design, hook-design-spec, c08-cluster, mission-2026-05-06, day-arc-2026-05-08, multi-day-pain-point-resolution, behave-from-not-over]
---

# Correction-as-Calibration Pre-Edit Verification Gate — Hook Design Pattern

## Summary

The mature 03_validated lesson `correction-as-calibration-not-swing` PRESCRIBES a 5-step verification (identify spectrum → current point → proposed-correction's point → calibrate-vs-swing test → apply-calibrated-fix-instead) but does NOT specify how to ENFORCE it. Per P1 (Infrastructure Over Instructions): prose ~25% compliance, hooks ~100%. This pattern fills the gap with a concrete hook-design-specification — a PreToolUse hook on Edit/Write that performs spectrum-analysis on the proposed change against the file's recent-edit-direction history, blocks with calibration-prompt when the change is detected as a swing-to-opposite-extreme rather than a refinement-of-trigger. The pattern also provides sequence-pattern detection (cross-turn): if recent N edits oscillated direction without convergence (per Class 9 sibling lesson's iteration-circuit-breaker principle), upgrade the block to a circuit-breaker. **This is a structural-enforcement artifact** — the cure prescribed by the mature lesson made implementable.

## Pattern Description

The pattern has FOUR structural components — all required:

### 1. Spectrum Map (data layer)

A spectrum map records correction-dimensions for common rule/edit classes. Examples:

| Edit Class | Spectrum Dimension | Extremes |
|---|---|---|
| Rule strictness | enforcement | always-allow ↔ always-deny |
| Hook scope | match-pattern | match-everything ↔ match-nothing |
| Permission grant | scope | all-actions ↔ no-actions |
| Output verbosity | shape | walls-of-text ↔ silent |
| Loop cadence | trigger-eagerness | fire-every-tick ↔ never-fire |
| Operator-asking | check-frequency | ask-every-action ↔ never-ask |
| Stamp render | position | start-of-prompt ↔ end-of-prompt |
| Cross-references | footer-application | every-file ↔ no-files |

The spectrum map lives in `tools/correction_spectrum.py` (data structure) — operator-extensible. New edit-classes added per empirical observation.

### 2. Recent-Edit-Direction Tracker (state layer)

Per-file (or per-rule-name) tracker maintains last N edits' direction-vectors:

```python
edit_history = {
    "file_path:hook_match_pattern": [
        {"ts": ..., "direction": "broaden", "magnitude": 1},
        {"ts": ..., "direction": "broaden", "magnitude": 1},
        {"ts": ..., "direction": "narrow", "magnitude": 5},  # SWING — magnitude jumps from 1 to 5
        {"ts": ..., "direction": "broaden", "magnitude": 4},  # SWING again
    ]
}
```

Direction = encoded relative to the spectrum (broaden/narrow, eager/lazy, allow/deny). Magnitude = how far along the spectrum the edit moves. State persisted at `~/.claude/correction-tracker.json` (session-scoped or session-bridging per operator preference).

### 3. PreToolUse Gate (enforcement layer)

PreToolUse hook on Edit / Write / NotebookEdit fires before the edit lands:

```
1. Identify edit-class (regex/path-matching against spectrum map)
2. Compute proposed-edit's direction + magnitude on the spectrum
3. Compare against recent-edit-direction tracker:
   - If direction REVERSES last edit AND magnitude >= 80% of last edit's magnitude → SWING DETECTED
   - If last 2 edits already inverted direction without convergence → CIRCUIT-BREAKER per Class 9 sibling lesson
4. Decision:
   - SWING DETECTED + first occurrence → BLOCK with remediation prompt requiring agent to:
     (a) name the spectrum dimension explicitly,
     (b) name current point on spectrum,
     (c) name proposed point,
     (d) state whether this is calibration-step (one-notch) or swing (full-opposite),
     (e) if swing, propose a refined trigger/condition that distinguishes buggy vs legitimate cases
   - SWING DETECTED + second occurrence (oscillation) → BLOCK as circuit-breaker; require explicit operator clarification ASK; agent moves to NEXT issue in queue (per Class 9 sibling)
   - NOT a swing → ALLOW (calibration; matches expected refinement shape)
5. Bypass: REASON env var with operator-justified swing case (e.g., `REASON="operator explicitly requested opposite-extreme per msg X"`)
```

The hook follows the project's existing 3-component design pattern (insertion + reason + remediation per `/root/.claude/rules/hook-architecture.md`); it adds the REQUIRED-gates fourth component this work prescribes.

### 4. Cycle-Output Substance Marker (audit layer)

Each cycle that includes an Edit/Write surfaces in its productive-output line:
```
Productive output: <type> — <one-line specific> [calibration-step|operator-bypass-swing|N/A]
```

The bracket annotation tracks per-cycle whether corrections passed the gate as calibration vs operator-bypass. Audit aggregator scans cycle-reports to surface swing-rate per session/per agent — calibration discipline becomes a measured signal.

## Pattern Components

| Component | Implementation File | Project | Status |
|---|---|---|---|
| Spectrum map | `tools/correction_spectrum.py` | /root | TO AUTHOR (post-Ready-for-Review) |
| Recent-edit-direction tracker | `~/.claude/correction-tracker.json` + `tools/correction_tracker.py` | /root + /opt | TO AUTHOR |
| PreToolUse calibration-vs-swing gate | `.claude/hooks/correction-calibration-gate.sh` (Python) | /root canonical, sister-projects via `/install-agent-brain` | TO AUTHOR |
| Cycle-output substance marker | extension to `tools/cycle.py` last-line generation | /root | TO EXTEND |
| Test file | `.claude/hooks/tests/test-correction-calibration-gate.py` | /root | TO AUTHOR |
| Audit aggregator | `tools/correction_audit.py` (scans cycle-reports) | /root + /opt | TO AUTHOR |

All 6 components are forward-anchors — design specified here; authoring + tests-passing is the promotion-to-02_synthesized gate.

## Instances

The mature lesson's Evidence table has 5 swing-correction rows from earlier 2026-05-05 work. The /root failed-conversation arc 2026-05-06 → 2026-05-08 produced 4+ NEW evidence rows that should extend the mature lesson's Evidence section (additive — see "Application 1 below: extend the mature lesson"):

| Original bug | Operator-flagged | Agent's correction (SWING) | Correct calibration |
|---|---|---|---|
| Stamp at start of prompt (wrong) | "should be at the end" | Removed stamp entirely | Move trigger to Stop event; preserve config |
| No Cross-references on files | "do not minimize" | Uniform 10-line Cross-references footer on every file in 16 categories | Per-file judgment; selective addition where load-bearing |
| Brain-improvement scope = 4-7 main files | mandate text | Touched 106 files with 2.6k additive lines | Stay within named-file scope; surface scope-expansion proposal before executing |
| "this side" ambiguous between root vs /opt | operator-context | Pivoted /opt gateway-orient | Read operator's prior 5 messages; literal context = root project |
| /handoff /terminate /finish-smoothly listed as routine compose-with | "Are you telling the AI to use my personal commands?" | Removed all 3 from compose-with sections in 7 tools | Distinguish operator-authority from AI-routine; positive framing in Cross-references describing channel |

These 5 rows extend the mature lesson's Evidence to 10 cumulative empirical instances of the swing pattern — strong evidence that the gate design proposed here addresses observed real-world failures.

## When To Apply

- **When authoring or modifying a hook script** — the hook itself is at risk of swing-corrections (over-broad → over-narrow → broken)
- **When editing a rule file in `.claude/rules/`** — most rule edits have spectrum-shape; gate detects swings
- **When configuring permissions in `settings.json`** — permission grants/revokes are spectrum operations
- **When tuning a hook's matcher pattern** — match-everything vs match-nothing extremes
- **When operator flags an over-correction** — per the mature lesson's Section 6 verification step; this gate enforces it
- **When a cycle's last-line claims a correction-action** — substance marker tracks calibration vs swing per fire

## When Not To

- When the change has no spectrum (e.g., a regex syntax error fix has a single-correct-value)
- When operator EXPLICITLY requests opposite-extreme (REASON bypass justified)
- When the change is at design/scaffold stage and gate-overhead exceeds value
- When the "swing" is the FIRST edit on this dimension (no prior direction to compare against)

## Self-Check (audit procedure for any correction-edit)

Before applying any correction-shaped edit, the agent must answer:

1. **What spectrum dimension does this edit operate on?** (broaden↔narrow / eager↔lazy / allow↔deny / etc.)
2. **What was the file/rule's current point on that spectrum BEFORE this edit?**
3. **Where would the proposed edit place the file/rule on that spectrum?**
4. **Is the proposed point at the OPPOSITE end?** Or is it a refinement of the trigger/condition that distinguishes buggy from legitimate?
5. **If at the opposite end (swing): can I identify the precise condition that distinguishes the buggy case from legitimate cases?** That condition IS the calibrated fix.
6. **If at a calibration point (one-notch refinement): proceed.** If swing detected without legitimate justification: STOP, identify the specific trigger, refine THAT instead.

The gate this pattern designs would BLOCK at step 4 with the prompt forcing the agent to answer 5 + 6.

## Composability with sibling patterns and lessons

This pattern composes with:
- **Lesson — Correction-as-calibration, not swing** (PRIMARY parent — the prescription this pattern makes structural)
- **Lesson — Refine triggers, not revoke permissions** (specific subcase — permission-edit family)
- **Pattern — Aspirational Declaration Without Enforcement** (this pattern is the enforcement-side answer to the mature lesson's aspirational verification step)
- **Lesson — Documentation As Substitute For Discipline** (sibling 2026-05-08 — same family; this pattern is one of the structural-enforcement artifacts that lesson prescribes)
- **Lesson — Class 9 Freeze-After-Correction** (sibling 2026-05-08 — pairs with this; C08 is over-correction-swing, C09 is under-correction-freeze; both at action-emission gate)
- **Lesson — Agent-Context-Discipline Is Aspirational** (sibling 2026-05-08 — input-side gates; this pattern is correction-shape gate; together they cover the agent-action boundary)

## Properties

| Property | Description |
|---|---|
| **Cross-edit-class** | Applies to rule / hook / code / config / behavior edits — same gate, different spectrum-map entries |
| **Composable** | The 4 components compose; missing any one weakens the gate but doesn't invalidate it |
| **Operator-extensible** | Spectrum map is data; new edit-classes added without code change |
| **Bypass-able** | REASON env var allows operator-justified swings (e.g., explicit "go to opposite extreme on this case") |
| **Audit-friendly** | Cycle-output substance marker + audit aggregator surface swing-rate as a measured signal — meta-pattern instance of P1's "measured ~25% vs ~100%" approach |
| **Sister-project portable** | Deploys via `/install-agent-brain` — gate design is operational tooling that propagates per brain-inheritance pattern |

## Relationships

- **DERIVED FROM** [Lesson — Correction-as-calibration, not swing](../../lessons/03_validated/enforcement-compliance/correction-as-calibration-not-swing-the-going-to-extremes-anti-pattern.md) — **PRIMARY parent**. This pattern is the gate-design-specification that codifies the mature lesson's verification step into structural enforcement.
- **DERIVED FROM** [Principle 1 — Infrastructure Over Instructions](../../lessons/04_principles/hypothesis/infrastructure-over-instructions-for-process-enforcement.md) — verification-step at prose tier ~25% compliance vs hook-tier ~100%; this pattern moves the verification from prose to gate.
- **PARALLELS** [Lesson — Refine Triggers, Not Revoke Permissions](../../lessons/03_validated/enforcement-compliance/refine-triggers-not-revoke-permissions-when-fixing-overzealous-rules.md) — same family at the specific permission-revocation subcase.
- **PARALLELS** [Pattern — Aspirational Declaration Without Enforcement](aspirational-declaration-without-enforcement.md) — this pattern is the enforcement-side answer.
- **PARALLELS** [Lesson — Documentation As Substitute For Discipline (the meta-pattern)](../../lessons/01_drafts/documentation-as-substitute-for-discipline-the-meta-pattern.md) — DIRECT sibling 2026-05-08; this pattern is the structural-enforcement artifact that lesson prescribes for the correction-shape failure mode.
- **PARALLELS** [Lesson — Class 9 Freeze-After-Correction](../../lessons/01_drafts/freeze-after-correction-is-class-9-of-agent-failure-taxonomy-abdication-as-freeze.md) — DIRECT sibling 2026-05-08; pairs at action-emission boundary (C08 over-correction; C09 under-correction).
- **PARALLELS** [Lesson — Agent-Context-Discipline Is Aspirational](../../lessons/01_drafts/agent-context-discipline-is-aspirational-without-enforcement-gates-not-reading-what-exists.md) — DIRECT sibling 2026-05-08; input-side gates.
- **EXTENDS** the mature lesson's Evidence table with 5 new /root-arc rows (forward-anchor: extend mature lesson directly when operator-confirmed; meanwhile preserved here as evidence-extension).
- **CONSTRAINS** /root/.claude/hooks/* authoring discipline — when modifying a hook, this gate prevents over-broad → over-narrow → broken oscillation.
- **CONSTRAINS** /root/.claude/rules/* authoring discipline — same shape at the rule layer.
- **FEEDS INTO** the 5-tier maturity progression for this pattern: `01_drafts/`; promotion to `02_synthesized/` gated on:
  1. Spectrum map authored (`tools/correction_spectrum.py`)
  2. Tracker authored (`tools/correction_tracker.py` + state file schema)
  3. Hook authored (`.claude/hooks/correction-calibration-gate.sh`) + wired
  4. Test file authored + tests passing
  5. Audit aggregator authored (`tools/correction_audit.py`)
  6. Operator-confirmed promotion
- **Mission served**: 2026-05-06 brain-improvement mandate (failed) → 2026-05-08+ multi-day systematic pain-point resolution; this pattern is C08 cluster's proposed-solution piece (gate-design-spec form, not parallel-lesson form per knowledge-reuse > re-authoring).

## Backlinks

(Auto-regenerated by `pipeline post`. Mature parent lesson + sibling lessons + composing patterns accumulate this pattern as a backlink upon next post-chain run.)

## Application 1 — Extend the mature lesson's Evidence table additively (forward-anchor)

The mature lesson at 03_validated/synthesized/mature has 5 Evidence rows from 2026-05-05. The /root failed-conversation arc 2026-05-06 → 2026-05-08 contributed 5 new swing-instances (this pattern's "Instances" section). Extending the mature lesson with these new rows is workflow-respectful additive content (Hard Rule 11 — additive ≠ discarding) but should be operator-confirmed since the lesson is mature/synthesized status (PO approval boundary per work-mode.md).

The proposal: append a "## Evidence — 2026-05-06 → 2026-05-08 /root-arc extension (5 additional rows)" subsection to the mature lesson, OR retain the 5 new rows here in this pattern's "Instances" section as the canonical /root-arc record. Operator decides path on review.

## Application 2 — Cross-project deployment

When `/install-agent-brain` deploys to sister projects, this pattern's 6 components deploy together:
- /opt second-brain: gate fires on /opt's edits (substantial pattern density — wiki/lessons authoring is correction-shape work)
- OpenArms: harness layer instance — refines the correction-as-swing pattern at fleet harness-engineering level
- OpenFleet: per-agent gates + fleet-aggregator
- AICP: model-routing-edit gate (which complexity tier handles which task)
- devops-control-plane: IaC-edit gate
