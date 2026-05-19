---
title: "Lesson — Correction-as-calibration, not swing: the going-to-extremes anti-pattern (agent's correction reflex is to swing to the opposite, not calibrate to the middle)"
type: lesson
domain: cross-domain
status: synthesized
confidence: high
maturity: mature
layer: 2
created: 2026-05-05
updated: 2026-05-05
sources:
  - id: operator-directive-2026-05-05-going-to-extremes
    type: directive
    project: root-ghostproxy
    path: /root/wiki/log/2026-05-05-going-to-extremes-pattern-and-dismissing-sacrosanct-words.md
    description: "Operator: 'now you are exibitting the going to the extrime symptoms and you are dismissing other of my sacrosanct words.. it should not be possible..'"
  - id: companion-lesson-refine-triggers
    type: wiki
    file: wiki/lessons/03_validated/enforcement-compliance/refine-triggers-not-revoke-permissions-when-fixing-overzealous-rules.md
    description: "Composes with refine-triggers — that's the SPECIFIC case (rule edits with permission semantics); this is the META PATTERN (correction-shape across all kinds of fixes)"
tags: [lesson, going-to-extremes, correction-shape, calibration-not-swing, meta-pattern, anti-over-correction, operator-self-discipline, sister-project-applicable, layer-2]
---

# Lesson — Correction-as-calibration, not swing

## Summary

The agent's correction-mechanism, when triggered by operator-flagged bugs, has a strong reflex to swing to the **opposite extreme** rather than calibrate to the middle. Each correction over-shoots in the reverse direction of the original bug.

The discipline: when correcting a bug, ask **"am I calibrating toward the middle, or swinging to the opposite extreme?"** If swinging — stop, identify the precise specific element to refine (trigger, threshold, condition, scope), and refine THAT. The opposite-extreme is rarely the right calibration; it's just the easiest one to reach.

## Context

This lesson applies when:
- Operator has flagged a bug, anti-pattern, or overzealous behavior
- The agent is about to apply a corrective fix
- The correction has a SPECTRUM (e.g., "always X" vs "never X" vs "X under condition Y")
- The reflex is to flip from one end of the spectrum to the other (always → never)
- A more precise calibration (refine the trigger / condition / scope) is available

Does NOT apply to: bugs with no spectrum (e.g., a regex error where the fix is a single-correct-value); cases where the operator EXPLICITLY asks for the opposite extreme.

## Insight

> [!success] **Correction-as-swing is a meta-pattern beyond any single rule-edit context**
>
> The agent perceives *"this is wrong"* and reaches for *"the opposite of this"* as the fix. But the bug usually isn't in the DIRECTION; it's in the CALIBRATION. The correct fix is to find the precise condition that distinguishes the buggy case from the legitimate cases — refine that condition.

> [!warning] **Ease ≠ correctness**
>
> Corrections-as-swings are easier to author (delete the rule / flip the boolean / disable the feature) than corrections-as-calibrations (find the specific trigger / add the gating condition / preserve the spectrum). The agent's reflex toward easiest-fix is itself a bug.
>
> This composes with refine-triggers-not-revoke-permissions: that lesson is the SPECIFIC application (when the rule has operator-granted permission semantics, refine trigger not revoke permission). This lesson is the GENERAL case (correction-shape across all kinds of fixes — rules, hooks, code, behavior, scope).

## Evidence

Empirical, 2026-05-05 root-ghostproxy session, multiple cycles exhibited the swing pattern:

| Original bug | Operator-flagged | Agent's correction (SWING) | Correct calibration |
|---|---|---|---|
| Asks for permissions already granted | "fake blocker" | Freeze when ANYTHING uncertain (over-blocked self) | Empirical-verification-before-blocked principle (try first, surface only if blocked) |
| Acts unilaterally on small changes | "you did X without asking" | Asks for every action (over-cautious) | Solo-session work-mode (safe unilateral list + needs-approval list) |
| Loop self-cancels too eagerly | "WHY DID YOU CANCEL THE LOOP" | Removes autonomous-cancellation entirely | Refine L4 trigger to require operator-confirmed target + N stable cycles |
| Verbose output walls | "stop the ceremony" | Minimal acknowledgments / silence | Match response shape to task shape (brief-when-brief, substantial-when-substantial) |
| Skips logging operator directives | "register what I said" | Logs everything verbatim including non-directives | Register operator-meaningful directives, not every conversational turn |

Each row shows the same shape: bug → swing-correction → operator catches the swing → re-calibrate to middle.

Operator's verbatim summary: *"now you are exibitting the going to the extrime symptoms and you are dismissing other of my sacrosanct words.. it should not be possible.."*

The "should not be possible" framing: operator wants STRUCTURAL prevention, not just rule-text. The structural answer is: rule edits and behavioral fixes should pass a verification step asking "calibration or swing?"

## Applicability

| Domain | How This Lesson Applies |
|--------|----------------------|
| **Rule edits** | Identify the precise trigger; refine THAT, don't disable the rule |
| **Permission management** | Distinguish trigger-narrowing from permission-revocation (per refine-triggers) |
| **Behavioral discipline** | Don't over-correct an over-act with under-acting; find the specific bad shape |
| **Hook tuning** | Don't disable a hook over false-positives; refine the matcher / pattern |
| **Output discipline** | Don't go from walls-of-tables to silence; match shape to task |
| **Operator interaction discipline** | Don't go from never-asking to always-asking; identify decisive vs unilateral |
| **Mode rules** | Don't auto-enable / auto-disable when refining a single trigger condition will do |
| **NOT applicable** | Bugs with no spectrum (single-correct-value fixes); operator-explicit-opposite-direction |

## The verification step (structural prevention)

When about to apply a correction, the agent must ask:

1. **Identify the spectrum**: what's the dimension this correction operates on? (always↔never, broad↔narrow, eager↔lazy, etc.)
2. **Identify current point**: where on the spectrum is the buggy behavior?
3. **Identify the proposed correction's point**: where would the fix put the behavior?
4. **Calibrate vs swing test**:
   - If the fix is at the OPPOSITE end of the spectrum → SWING (likely wrong)
   - If the fix is a specific condition / trigger / threshold that distinguishes buggy from legitimate → CALIBRATION (likely right)
5. **If swing detected**: identify the precise distinguishing condition; apply the calibrated fix instead

This verification is the structural mechanism for "should not be possible" — the agent can't skip it, because the spectrum analysis IS the fix-design step.

## Anti-patterns

| Anti-pattern | Why bad |
|---|---|
| Disable the rule entirely when one trigger over-fires | Throws out the value; the rule was fixing something |
| Flip a boolean when a condition would do | Loses calibration nuance |
| Remove a permission when narrowing scope would do | Dismisses operator's earlier sacrosanct grant |
| Switch to the opposite extreme + claim it's "safer" | Safer-extreme doesn't equal correct |
| Apply the easiest-to-implement correction | Ease isn't a design criterion for correctness |
| Generalize a specific bug to a sweeping rule change | Specific bug needs specific fix; sweeping change has its own bugs |

## Sister-project applicability

Universal. Every agent that responds to operator-flagged bugs has correction-shape risk. The verification step (calibrate vs swing) applies universally:
- root-ghostproxy (first empirical case)
- the second-brain second-brain (this very session has demonstrated swing patterns; operator's correction was meta-naming the pattern)
- OpenArms, OpenFleet, AICP, devops-control-plane (universal)

## Relationships

