---
title: "Principle: {{title}}"
type: principle
domain: cross-domain
layer: 5
status: synthesized
confidence: medium
maturity: seed
derived_from:
  - "{{lesson_1}}"
  - "{{lesson_2}}"
  - "{{lesson_3}}"
created: {{date}}
updated: {{date}}
sources: []
tags: [principle]
---

# Principle: {{title}}

<!-- A PRINCIPLE is distilled from multiple VALIDATED LESSONS.
     A lesson says "we learned X from incident Y."
     A principle says "ALWAYS do X because the mechanism is Z, and here are N lessons that prove it."
     
     Promotion criteria: ≥3 validated lessons converge on the same mechanism.
     Principles are the highest knowledge layer — they govern behavior across all contexts. -->

## Summary

<!-- 1-2 sentences: the principle as an actionable rule.
     A reader should be able to FOLLOW this principle from the summary alone. -->

## Statement

<!-- The principle stated formally. One sentence. Unambiguous.
     STYLING: > [!tip] for the principle statement.
     
     GOOD: "Infrastructure enforcement achieves categorically higher compliance than instruction-based enforcement for any process rule that can be checked at the tool-call level."
     BAD: "Infrastructure is better than instructions." (no mechanism, no scope) -->

> [!tip] The Principle
>
> {{formal statement with mechanism and scope}}

## Derived From

<!-- The lessons that converge to prove this principle.
     MINIMUM 3 validated lessons, each providing independent evidence.
     STYLING: Table with lesson → what it contributes to the principle. -->

> [!abstract] Evidence Chain
>
> | Lesson | What It Contributes |
> |--------|-------------------|
> | [[{{lesson_1}}]] | {{specific evidence from this lesson}} |
> | [[{{lesson_2}}]] | {{specific evidence from this lesson}} |
> | [[{{lesson_3}}]] | {{specific evidence from this lesson}} |

## Application

<!-- How to apply this principle in practice.
     STYLING: Table mapping contexts to application.
     Include: which identity profiles benefit, which SDLC chains, which PM levels. -->

> [!abstract] Application by Context
>
> | Context | How to Apply |
> |---------|-------------|
> | {{context_1}} | {{how}} |
> | {{context_2}} | {{how}} |

## Boundaries

<!-- Where this principle does NOT apply. What breaks it.
     A principle without boundaries is a dogma.
     STYLING: > [!warning] for the boundary conditions. -->

> [!warning] Boundaries
>
> - {{condition where this principle doesn't apply}}
> - {{what would change the principle if discovered}}

## How This Connects — Navigate From Here

> [!abstract] From This Principle → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **Lessons that prove this** | See Derived From above |
> | **Patterns that implement this** | {{related patterns}} |
> | **Models that embed this** | {{which models use this principle}} |
> | **Goldilocks application** | [[Project Self-Identification Protocol — The Goldilocks Framework]] |

## Relationships

- DERIVED FROM: [[{{lesson_1}}]]
- DERIVED FROM: [[{{lesson_2}}]]
- DERIVED FROM: [[{{lesson_3}}]]
