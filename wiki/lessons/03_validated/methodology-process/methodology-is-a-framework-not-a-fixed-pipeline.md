---
title: "Methodology Is a Framework, Not a Fixed Pipeline"
aliases:
  - "Methodology Is a Framework, Not a Fixed Pipeline"
type: lesson
domain: cross-domain
layer: 4
status: synthesized
confidence: authoritative
maturity: growing
derived_from:
  - "Methodology Framework"
  - "Stage-Gate Methodology"
created: 2026-04-10
updated: 2026-04-13
sources:
  - id: directive-methodology-flexible
    type: log
    file: wiki/log/2026-04-09-directive-methodology-is-flexible-not-fixed.md
    title: "Methodology Is Flexible — Multiple Chains, Not One Fixed Pipeline"
    ingested: 2026-04-09
tags: [failure-lesson, methodology, flexibility, framework, composability, overfitting]
---

# Methodology Is a Framework, Not a Fixed Pipeline

## Summary

The Methodology model page collapsed the entire methodology framework into a single 5-stage pipeline (Document → Design → Scaffold → Implement → Test) — treating one specific sequence as THE methodology. But the operator had explicitly described a FLEXIBLE framework with multiple chains, conditional selection, and composable sequences. The agent got lost in a specific case instead of presenting the framework. This is the same failure pattern as the first LLM Wiki model — overfitting to one instance instead of capturing the system.

## Context

This lesson applies whenever documenting a system that has multiple modes of operation, configurable behavior, or contextual adaptation. The triggering signal: if the documentation describes ONE way to use the system, and the system actually supports MANY ways, the documentation is overfitting.

## Insight

> [!warning] Overfitting to one instance of a framework
>
> | What the Operator Described | What the Agent Documented |
> |---------------------------|--------------------------|
> | Multiple named sequences (research, feature-dev, hotfix, evolution) | ONE 5-stage sequence |
> | Conditions selecting which sequence applies | Task type as the ONLY condition |
> | Composable sequences (sequential, nested, conditional, parallel) | No composition model |
> | The 5-stage sequence as ONE INSTANCE | The 5-stage sequence as THE WHOLE THING |

The failure is conceptual, not technical. The agent understood the 5-stage sequence perfectly. But understanding one instance of a framework is not understanding the framework. The framework is: what IS a methodology model, how are models SELECTED, how do they COMPOSE, and how are they ADAPTED per-instance.

> [!tip] The fix: document the framework, then the instances
> The Methodology Framework page (wiki/domains/cross-domain/) now covers: model definition (named entity with stages, gates, protocols), selection (5 condition dimensions), composition (4 patterns), adaptation (overrides per instance), recursion (same vocabulary at every scale), and multi-track coexistence. The 5-stage sequence is documented as one model within the framework — important, but not the whole story.

## Evidence

**Date:** 2026-04-09

**The operator's response:** "your methodology doesn't work... I told you it was flexible and it was possible to have multiple chains / group of stage for various cases and there was conditions possible..."

**The pattern:** Same failure as the first LLM Wiki model. In both cases, the agent latched onto one concrete implementation and documented it as the entire system. For LLM Wiki: documented THIS wiki's structure instead of the universal LLM Wiki pattern. For Methodology: documented the 5-stage sequence instead of the flexible framework.

**Source:** `wiki/log/2026-04-09-directive-methodology-is-flexible-not-fixed.md`

## Applicability

- **API documentation**: documenting one endpoint's behavior as "how the API works" instead of the API's design patterns
- **Framework documentation**: documenting one configuration as "the setup" instead of the configuration model
- **Architecture docs**: documenting one deployment topology as "the architecture" instead of the deployment framework
- **Knowledge systems**: documenting one wiki's schema as "the schema" instead of the schema design principles

> [!abstract] The general principle
> When a system is CONFIGURABLE, document the configuration model (what can vary, what selects between options, how options compose). When a system is FIXED, document the behavior. Treating a configurable system as fixed produces documentation that's correct for one case and wrong for all others.

## Self-Check — Am I About to Make This Mistake?

> [!warning] Ask yourself:
>
> 1. **Am I treating the methodology as one fixed 5-stage pipeline?** — The methodology has multiple named models (research, feature-dev, hotfix, evolution, etc.) with different stage sequences. Am I applying the right model for this task, or defaulting to Document-Design-Scaffold-Implement-Test for everything?
> 2. **Am I documenting one instance of a configurable system as if it were the entire system?** — If the system supports multiple modes, conditional selection, and composable sequences, documenting only one path produces documentation that is correct for one case and wrong for all others.
> 3. **Have I described what can VARY, not just what IS?** — For any configurable system: what selects between options? How do options compose? What are the adaptation points? If I only described the default configuration, I have documented an instance, not a framework.
> 4. **Am I overfitting to the concrete case I know best?** — This is the same failure as documenting one wiki's schema as "the schema" instead of the schema design principles. Check: does my documentation cover the space of possibilities, or just the one I have seen?

### How This Connects — Navigate From Here

> [!abstract] From This Lesson → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **What principle governs this?** | [[right-process-for-right-context-the-goldilocks-imperative|Principle — Right Process for Right Context — The Goldilocks Imperative]] |
> | **How does enforcement apply?** | [[infrastructure-over-instructions-for-process-enforcement|Principle — Infrastructure Over Instructions for Process Enforcement]] |
> | **How does structure help?** | [[structured-context-governs-agent-behavior-more-than-content|Principle — Structured Context Governs Agent Behavior More Than Content]] |
> | **What is my identity profile?** | [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]] |
> | **Where does this fit in the system?** | [[methodology-system-map|Methodology System Map]] — find any component |

## Relationships

- DERIVED FROM: [[methodology-framework|Methodology Framework]]
- RELATES TO: [[stage-gate-methodology|Stage-Gate Methodology]]
- RELATES TO: [[models-are-systems-not-documents|Models Are Systems, Not Documents]]
- RELATES TO: [[methodology-framework-design-decisions|Decision — Methodology Framework Design Decisions]]

## Backlinks

[[methodology-framework|Methodology Framework]]
[[stage-gate-methodology|Stage-Gate Methodology]]
[[models-are-systems-not-documents|Models Are Systems, Not Documents]]
[[methodology-framework-design-decisions|Decision — Methodology Framework Design Decisions]]
[[2026-04-09-directive-methodology-is-flexible-not-fixed|Methodology Is Flexible — Multiple Chains, Not One Fixed Pipeline]]
[[src-anthropic-building-effective-ai-agents|Synthesis — Anthropic — Building Effective AI Agents — 5 Canonical Workflow Patterns]]
