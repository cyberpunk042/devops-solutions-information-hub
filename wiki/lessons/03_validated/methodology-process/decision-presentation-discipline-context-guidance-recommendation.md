---
title: "Lesson — Decision-presentation discipline: every operator-pending decision needs CONTEXT + GUIDANCE + RECOMMENDATION (not a wall of vague questions)"
type: lesson
domain: cross-domain
status: synthesized
confidence: high
maturity: mature
layer: 2
created: 2026-05-05
updated: 2026-05-05
sources:
  - id: operator-directive-2026-05-05-decision-presentation
    type: directive
    project: root-ghostproxy
    path: /root/wiki/log/2026-05-05-decision-presentation-discipline-context-guidance-recommendation.md
    description: "Operator: 'this kind of situation we need a new feature /function / command and/or tools and way to do so that i am not just face to a wall of vague information and with lack of context and guidance'"
  - id: companion-blocker-filter-discipline
    type: wiki
    file: wiki/lessons/03_validated/methodology-quality/anti-minimizing-systemic-bug-counts-and-blocker-filter-discipline.md
    description: "Composes with blocker-filter discipline — both are PM-lens signal-to-noise patterns. Filter says 'only surface what's genuinely pending'; this says 'and when you do surface it, package it properly.'"
tags: [lesson, decision-presentation, context-guidance-recommendation, anti-question-wall, signal-to-noise, pm-lens, sister-project-applicable, layer-2, communication-discipline]
---

# Lesson — Decision-presentation discipline: CONTEXT + GUIDANCE + RECOMMENDATION

## Summary

Every operator-pending decision the agent surfaces must be a **self-contained decision package** with:
- **DECISION**: one-line title (what's being decided)
- **CONTEXT**: 2-3 lines of relevant background (what this decides for, why it's blocking, what's at stake)
- **GUIDANCE**: key trade-offs the operator should weigh
- **RECOMMENDATION**: agent's suggested answer + brief rationale (operator can override, but starts with a position to react to)
- **ALTERNATIVES**: other viable paths if multiple exist, briefly
- **TO ANSWER**: minimal operator response shape (single word / phrase / yes-no)

This makes the decision **decidable on-the-spot** without operator re-loading state. The anti-pattern: surfacing a "wall of vague questions" without context, guidance, or recommendation — operator must re-load state per question + derive answers from scratch + can't see what the answer would unblock.

## Context

This lesson applies when:
- The agent is surfacing a list of operator-pending decisions (cycle status block, blocker register, end-of-turn ask)
- Multiple decisions are surfaced simultaneously (3+ asks)
- The reflex is to write each ask as a question, leaving operator to load context for each
- The operator's attention is the constrained resource — wall-of-questions wastes it

Does NOT apply to: single-question moments where context is fresh in conversation; clarification questions about something the operator just said (those are conversational, not decision-package-shape).

## Insight

> [!success] **A decision package is a self-contained unit; a wall of questions is incomplete units**
>
> A decision package is a **self-contained unit** — operator reads it once and can decide. A wall of questions is **incomplete units** — operator has to do the work of completing each.

> [!tip] **PM-lens signal-to-noise applied to surfacing format**
>
> This is the **PM-lens signal-to-noise discipline** applied to the surfacing format. The blocker-filter discipline (don't over-surface) handles WHICH decisions reach the operator; the decision-presentation discipline handles HOW each one is shaped. Both are facets of *"operator attention is precious; respect it."*
>
> The agent has more context than the operator does at the moment of surfacing — agent has just been working on the issue; operator may have stepped away. The package format transfers that context, plus an opinionated recommendation. The operator either accepts the recommendation (fast path) or overrides with their own answer (slower path, but informed by the package's GUIDANCE). Either way, faster than wall-of-questions.

## Evidence

Empirical, 2026-05-05 root-ghostproxy session, Cycle 16.5:

- Agent emitted 7 "direction asks" with sub-questions
- Operator reaction (verbatim): *"this kind of situation we need a new feature /function / command and/or tools and way to do so that i am not just face to a wall of vague information and with lack of context and guidance"*
- Operator's diagnosis: each ask was a QUESTION (or set of questions) without context or agent-recommendation
- Operator must load context PER question + derive answers from scratch — cumulative attention cost is high
- Vague questions don't expose what the answer would unblock — operator can't prioritize across the 7

The structural fix landed as the package format above. /root registered it as SB-071 in the systemic-bugs tracker; modes' /cycle steps were updated to require this format when surfacing decisions.

## Applicability

| Domain | How This Lesson Applies |
|--------|----------------------|
| **PM-mode cycle reports** | When surfacing pending decisions, format each as a package |
| **Blocker register output** | `tools.blockers --filter --decision-package` (forward-compat) emits packages |
| **End-of-turn operator-pending asks** | Always package format, never raw questions |
| **Backlog grooming surfacing** | Each blocker-shaped item gets the package |
| **Cycle-end status blocks** | Pending-decisions section uses the package format |
| **Sister-project agent setups** | Universal pattern for any operator-supervised solo + AI configuration |
| **NOT applicable** | Mid-conversation clarification questions; already-fresh-context single-asks |

## Composition with other PM-lens disciplines

- **Blocker-filter** (`fake-blockers-vs-real-blockers`): determines WHETHER to surface (filter first; only genuinely-pending items reach the package step)
- **Anti-minimizing**: determines COUNT honesty (cumulative tracking; don't undercount)
- **This lesson**: determines SHAPE per surfaced item (package format)
- **Multi-branch parallel** ([[multi-branch-parallel-driving-options-mean-evaluate-not-freeze]]): determines what NOT to package (option-multiplicity is parallel-advance, not a decision package)

Together these form the PM-lens output discipline. Each handles a different surface; conflating them produces the dumping-ground / question-wall / minimizing-count anti-patterns.

## The package template (load-bearing format)

```markdown
**DECISION:** <one-line title>
**CONTEXT:** <2-3 lines: what this decides for, why blocking, what's at stake>
**GUIDANCE:** <key trade-offs operator should weigh>
**RECOMMENDATION:** <agent's suggested answer + brief rationale>
**ALTERNATIVES:** <if multiple paths, the others briefly>
**TO ANSWER:** <minimal operator response shape — single word / phrase / yes-no>
```

Adherence to the format matters — not just the content. Operator can scan the bold tokens (DECISION / CONTEXT / GUIDANCE / RECOMMENDATION / ALTERNATIVES / TO ANSWER) to extract structure quickly. Skipping a token (e.g., "no recommendation, agent has no view") should still leave the token visible: `**RECOMMENDATION:** None — operator's call without agent input`.

## Anti-patterns

| Anti-pattern | Why bad |
|---|---|
| Wall of vague questions | Operator loads context per question; no recommendation to react to |
| Single question with no context | Forces operator to recall state from scratch |
| Recommendation without rationale | Operator can't evaluate; might accept blindly or reject blindly |
| Context-only (no recommendation) | Operator does all the synthesis work the agent should have done |
| Hiding agent-uncertainty by omitting recommendation | If agent has no view, say so explicitly — don't pretend the operator has more context |
| Burying the TO ANSWER | Operator should know exactly what response shape unblocks |

## Tooling implications (forward-compat)

A `tools.decisions --emit-package` or `tools.blockers --decision-package` subcommand could auto-format pending decisions in the package shape from the underlying register data. The package fields map cleanly to register fields:
- DECISION ← title
- CONTEXT ← description + dependencies
- GUIDANCE ← related-decisions + trade-offs
- RECOMMENDATION ← agent-can-recommend logic (per blocker-filter discipline)
- ALTERNATIVES ← other_options field
- TO ANSWER ← expected_response_shape

Building such a tool is appropriate when the format has been used manually for several cycles + the structure has stabilized. Premature tooling encodes wrong assumptions.

## Sister-project applicability

Universal. Every project where an agent surfaces operator-pending decisions has this discipline. The package format is content-agnostic — works for /root's M-numbered modules + decisions, the second-brain's methodology-engine + ingestion-pending decisions, OpenArms harness decisions, etc.

## Relationships

