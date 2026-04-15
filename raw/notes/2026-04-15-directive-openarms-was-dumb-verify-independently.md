---
title: "Operator directive — OpenArms was dumb development, sister lessons must be verified independently"
type: note
domain: log
status: active
note_type: directive
created: 2026-04-15
updated: 2026-04-15
tags: [operator-directive, verbatim, higher-ground, verify-independently, openarms, epistemic-hygiene]
---

# Operator Directive — OpenArms Was Dumb Development; Sister Lessons Must Be Verified Independently

## Context

Mid-session 2026-04-15 — while implementing the consumption-diff tracker on the sister-project tool. Operator clarifies the epistemic status of sister-project content.

## Verbatim Operator Message

> "Lets not forget openarms was a dumb development,, it may have deduce things without diagnostic, without proof, without even knowing what it was sending to the Agent up to a certain point...."

## Distillation

OpenArms itself — the sister project — produced some of its knowledge by deduction without diagnostic, without proof, without full visibility into its own agent's input. Its lessons may themselves be assumption-derived, not evidence-verified. Therefore:

1. **Consumption ≠ validation.** Referencing a sister lesson does not make it true. The wiki's evidence standards apply independently to any claim, regardless of who sourced it.
2. **Verify before synthesizing.** If we absorb a sister insight, we verify it against other evidence (external research, our own observations, cross-source convergence) before treating it as canon.
3. **Sister lessons are weak signals, not ground truth.** They point at things worth investigating. They are not themselves investigations.
4. **Double-lowering is the failure mode.** Taking sister claims at face value AND mirroring them into our tree = worse than either alone. We'd be synthesizing on a foundation we haven't inspected.

## How This Shapes the Consumption-Diff Tool (in progress)

The tracker I'm building detects what sister-project paths are REFERENCED in our wiki. This is "touched" — not "validated." Unreferenced sister files are unconsumed — interesting to look at. Referenced sister files are already in our research loop — but that doesn't mean their claims are validated; only that we have them in view.

Tool semantics going forward:
- `--new` default → "what sister material have we not even looked at yet" (genuine delta for exploration)
- `--all` → "show everything, consumed or not"
- **Never add** a mode that claims "consumed = validated." That conflation would embed the failure mode the operator just named into the tool itself.

## Standing Rules Going Forward

1. **Assume sister claims are unverified until our wiki independently validates them.** OpenArms specifically is flagged as "dumb development" by the operator — its output is signal, not truth.
2. **Verification requires multi-source convergence.** One sister saying something is not evidence. Convergence across 2+ independent sources (sisters, external research, our observations) is the minimum bar for incorporating into validated content.
3. **Diagnose before distilling.** When we do synthesize from sister material, trace each claim to its supporting evidence. If the claim has no diagnostic basis in the sister, it doesn't get promoted.

## Cross-Reference

Reinforces and refines:
- 2026-04-15 directive: "Do not lower yourself to sister projects" (higher ground)
- 2026-04-15 directive: "no caps, no compacting, read full, log verbatim" (discipline applied to reading)
- Existing lesson: `never-synthesize-from-descriptions-alone.md` (layer-0 vs layer-1)
- Existing memory: `feedback_depth_verification.md`

The thread: **read real instances → verify independently → synthesize above sources, not alongside them.**
