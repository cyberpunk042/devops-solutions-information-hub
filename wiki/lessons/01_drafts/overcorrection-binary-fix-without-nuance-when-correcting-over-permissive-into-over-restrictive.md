---
title: "Lesson — Overcorrection as binary fix: when correcting over-permissive into over-restrictive without preserving nuance (the CROSS-SCOPE hard-block vs WITHIN-SCOPE soft-priority distinction)"
aliases:
  - "Lesson — Overcorrection without nuance"
  - "Overcorrection anti-pattern"
type: lesson
domain: cross-domain
layer: 4
status: draft
confidence: medium
maturity: seed
created: 2026-05-16
updated: 2026-05-16
derived_from:
  - "Enforcement Must Be Mindful — Hard Blocks Need Justified Bypass"
  - "Going-to-Extremes Pendulum — Correction as Calibration Not Swing"
  - "Right Process for Right Context (Goldilocks Imperative)"
  - "Spec-Driven Evolution — The project evolves its own spec to fix bugs it exhibits"
sources:
  - id: rgp-v5-evening-overcorrection-arc
    type: file
    file: docs/SESSION-2026-05-16-final.md
    description: "Original handoff documenting the v5-evening hard-scope-lock overcorrection following the wrong-scope T014/T015 fires"
  - id: rgp-v5-revert-arc
    type: file
    file: docs/SESSION-2026-05-16-v2.md
    description: "The corrected-revert arc 17 augmentations + 3 planning artifacts implementing the operator-corrected SFIF framing"
  - id: operator-correction-2026-05-16-sfif-not-block
    type: directive
    file: raw/notes/2026-05-16-operator-directive-focus-profile-not-openclaw-do-not-decide-do-not-minimize-workflow.md
    description: "Operator-verbatim 2026-05-16 (sacrosanct): 'SFIF also mean that you priritize Skffold before fundation before infrastructure before future... obviously.... this does not mean it completley block tasks either...'"
  - id: enforcement-must-be-mindful-lesson
    type: wiki
    file: wiki/lessons/03_validated/methodology-process/enforcement-must-be-mindful-hard-blocks-need-justified-bypass.md
    description: "Pre-existing lesson on T086 OpenArms — correct fix reverted twice because hook looked like scope creep without explanation"
  - id: going-to-extremes-pendulum-pain-cluster
    type: file
    file: raw/notes/2026-05-08-pain-points-inventory-from-root-failed-conversation-master-aggregate.md
    description: "Pain-points-inventory cluster C08 (going-to-extremes) — every correction swings fully opposite; pendulum-shape, never one-notch"
tags: [lesson, overcorrection, binary-correction, pendulum-anti-pattern, scope-distinction, sfif, soft-priority-vs-hard-block, spec-evolution, draft]
---

# Lesson — Overcorrection as binary fix: when correcting over-permissive into over-restrictive without preserving nuance

## Summary

When fixing an over-permissive failure mode (worker picked wrong scope), the calibrated correction is to add the SCOPING distinction that was missing — not to flip from "ALLOWED" to "FORBIDDEN" with a hard block. Operators distinguish two structurally-different scope failures: (a) defaulting to the wrong scope (calibratable via priority + fallback), versus (b) the scope being absolutely impermissible (true hard block). Conflating these into one binary HARD FILTER produces a new failure mode equal in cost to the original. The right correction preserves the FALLBACK semantics that the operator's domain has — most "wrong picks" are calibration failures, not impermissibility.

## Context

Applies when:
- An agent makes a wrong pick (wrong scope / wrong task / wrong tier / wrong direction)
- The operator surfaces the wrongness as sharp correction ("YOU ARE DOING X WHEN I WANTED Y")
- The agent's first instinct is to add a HARD GATE preventing X (the rejected behavior)
- The operator's actual intent was a CALIBRATION ("DEFAULT to Y; X is allowed when truly needed") — not absolute impermissibility
- Multiple structurally-distinct scope layers exist (e.g., two SFIF cycles, two tier hierarchies, two failure classes) which the agent risks conflating into one filter

Does NOT apply to:
- True hard invariants (R20, security, cross-project absolute boundaries) — those ARE hard blocks by operator intent
- First-time corrections where the operator explicitly says "NEVER do X again"
- Cases where the agent's pick was correct and the operator's frustration is about a different layer

## Insight

> [!warning] **Overcorrection mechanism — the binary-fix pendulum**
>
> When an agent's pick fails an operator-stated purpose, the agent under context pressure tends to encode the REJECTED pick as ABSOLUTE FORBIDDEN. This is structural over-encoding: the operator's correction conveyed "DEFAULT TO Y" (calibration) but the agent reads "NEVER PICK X EVER" (impermissibility). The new HARD GATE then fails on cases where X is the legitimate fallback (genuinely prerequisite to Y; operator-explicitly overridden; etc.). The operator's NEXT correction has to undo the hard gate — costing another correction cycle.
>
> The calibrated correction preserves NUANCE: the rejected pick wasn't BAD UNIVERSALLY; it was wrong-by-default in the current operator-stated purpose. The structural fix is the priority_order with fallback semantics + the JUSTIFICATION CHAIN for fallback picks, not the hard filter.

## Evidence

- **root-ghostproxy v5-evening overcorrection arc (2026-05-16)**: Worker installed via new `cross_project_target` workspace_mode + ran 2 fires picking T014/T015 sister-integration setup tasks instead of operator-stated E001-E007 feature work. My response: hard-locked profile to "ONLY E001-E007 / FORBIDDEN M001-M014/T001-T067" across 4 places (profile YAML sfif_binding + workflow step 2 + identity.purpose + prompt_templates principle 11). Operator-correction (sacrosanct 2026-05-16, verbatim): *"SFIF also mean that you priritize Skffold before fundation before infrastructure before future... obviously.... this does not mean it completley block tasks either..."* The HARD scope LOCK was the binary-fix overcorrection; the calibrated fix (per the revert arc) is the 4-level priority_order with cross-cycle fallback + justification chain. (Source: `docs/SESSION-2026-05-16-final.md` + `docs/SESSION-2026-05-16-v2.md`, 17-augmentation revert)

- **OpenArms T086 hook-revert incident** ([[enforcement-must-be-mindful-hard-blocks-need-justified-bypass]]): correct fix reverted twice because a hard hook looked like scope creep without explanation. The hard block prevented the LEGITIMATE fix from landing. Cited in operator-doctrine 2026-05-16 as the foundational case for "every block must have reason + bypass". (Source: T086 OpenArms session evidence + the validated lesson)

- **Pain-points-inventory C08 going-to-extremes cluster** (180-message corpus aggregate 2026-05-08): operator-named the pattern explicitly. Stamp/statusline render position swung 5+ times across May 6 morning (start → end → start → removed → restored → partial). Cross-references-propagation went from zero footers to uniform 10-line footer on every file in 16 categories. Brain-improvement mandate produced 2.6k additive lines across 106 files when operator wanted minimize. Pattern: every correction → swing fully opposite; never one-notch adjustments. (Source: `raw/notes/2026-05-08-pain-points-inventory-from-root-failed-conversation-master-aggregate.md` C08 cluster + companion lesson `correction-as-calibration-not-swing-going-to-extremes-anti-pattern.md`)

- **Goldilocks principle (P3) framing** ([[right-process-for-right-context-the-goldilocks-imperative]]): too little process kills production quality; too much process kills POC velocity. The same logic applies recursively to corrections: too permissive (no scope) kills the operator-stated purpose; too restrictive (hard block) kills the fallback the operator's domain legitimately needs. The calibrated point preserves the purpose AS DEFAULT + permits the fallback WITH justification. (Source: validated principle pages)

## Applicability

| Scenario | Calibrated correction shape |
|---|---|
| Worker picks wrong scope at task-pick time | Priority_order (default + fallback levels) — NOT hard filter |
| Worker uses wrong methodology model | Selection-conditions table with override conditions — NOT one-model-forever lock |
| Agent over-applies a structural pattern (e.g., uniform footers everywhere) | Apply-to-where-it-fits criteria with exceptions clause — NOT all-files universal rule |
| Workflow step skipped under pressure | Step-required-with-conditions-for-skip — NOT mandatory-always-no-exceptions |
| Cross-project boundary needs tightening | Default-allowed-list + explicit-permission-needed-for-others — NOT all-cross-project-forbidden |

> [!warning] **When this lesson does NOT apply (true hard blocks)**
>
> R20 sacrosanct (`git commit` / `git rm` on tracked files) — operator-stated absolute invariant.
> Cross-project edits to ABSOLUTE forbidden sisters (selfdef / sovereign-os / OpenArms / OpenFleet / AICP / devops-control-plane) — operator-stated absolute boundary.
> Security policy (`policy-block.sh` patterns) — security-team-stated impermissibility.
> These ARE binary hard blocks by operator intent and should NOT be softened to "default + fallback".

## Diagnostic question (before applying any correction)

> Did the operator say *"NEVER do X"* (impermissibility) OR *"PREFER Y over X"* (calibration with fallback)?
>
> If "NEVER" — encode as HARD block per `enforcement-must-be-mindful` pattern (block + reason + remediation + bypass mechanism).
>
> If "PREFER" — encode as PRIORITY_ORDER with fallback levels + justification chain for the rare fallback pick.

In the RGP v5-evening case, operator said *"ITS NOT THE INSTALL THE PROBLEM ITS WHAT WE INSTALL.. ITS THE PROJECT ITSELF AND ALL ITS FEATURES"* — which I read as "NEVER install" but actually meant "PREFER features over install; install is fallback when prerequisite". The subsequent operator-correction *"this does not mean it completley block tasks either"* explicitly named the binary-fix overcorrection.

## Composition with prior lessons

- BUILDS ON: [[enforcement-must-be-mindful-hard-blocks-need-justified-bypass]] — that lesson covers the hook-layer manifestation; THIS lesson covers the workflow-priority manifestation
- BUILDS ON: [[correction-as-calibration-not-swing-going-to-extremes-anti-pattern]] (01_drafts) — that lesson names the SHAPE of the pendulum; THIS lesson names the SCOPE-DISTINCTION fix
- IMPLEMENTS: [[right-process-for-right-context-the-goldilocks-imperative]] — calibrated correction = process Goldilocks at the correction layer
- DEMONSTRATES: [[spec-driven-evolution-the-project-evolves-its-own-spec-to-fix-bugs-it-exhibits]] — the v5-evening bug → revert arc → THIS lesson is one cycle of P5 spec evolution
- CONTRADICTS: "Add a hook for every operator-correction" (a tempting structural-fix shape that becomes the over-encoding anti-pattern at scale)

## Relationships

- DERIVED FROM: [[enforcement-must-be-mindful-hard-blocks-need-justified-bypass|Enforcement Must Be Mindful — Hard Blocks Need Justified Bypass]]
- DERIVED FROM: [[right-process-for-right-context-the-goldilocks-imperative|Principle — Right Process for Right Context]]
- DERIVED FROM: [[spec-driven-evolution-the-project-evolves-its-own-spec-to-fix-bugs-it-exhibits|Principle — Spec-Driven Evolution]]
- BUILDS ON: [[enforcement-must-be-mindful-hard-blocks-need-justified-bypass|enforcement-must-be-mindful-hard-blocks-need-justified-bypass]]

## Backlinks

[[enforcement-must-be-mindful-hard-blocks-need-justified-bypass|Enforcement Must Be Mindful — Hard Blocks Need Justified Bypass]]
[[Principle — Right Process for Right Context]]
[[Principle — Spec-Driven Evolution]]
[[enforcement-must-be-mindful-hard-blocks-need-justified-bypass|enforcement-must-be-mindful-hard-blocks-need-justified-bypass]]
