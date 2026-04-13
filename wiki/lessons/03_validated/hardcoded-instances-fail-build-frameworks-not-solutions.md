---
title: Hardcoded Instances Fail — Build Frameworks Not Solutions
aliases:
  - "Hardcoded Instances Fail — Build Frameworks Not Solutions"
type: lesson
domain: cross-domain
layer: 4
status: synthesized
confidence: high
maturity: growing
derived_from:
  - "Methodology Standards Initiative — Honest Assessment"
  - "Model: Methodology"
  - "Methodology Framework"
created: 2026-04-12
updated: 2026-04-12
sources:
  - id: phase1-failure
    type: observation
    file: docs/SESSION-2026-04-12-handoff.md
    description: 37 files produced in Phase 1 of methodology initiative — operator called 'complete crap'
  - id: openarms-yaml
    type: observation
    file: docs/SESSION-2026-04-12-handoff.md
    description: OpenArms methodology.yaml used as blueprint — produced specific instance instead of generic framework
  - id: operator-directive
    type: directive
    file: raw/notes/2026-04-11-methodology-standards-directive.md
    description: Operator explicitly said 'we want better... not hardcoded' and 'build FRAMEWORKS not instances'
tags: [methodology, framework, anti-pattern, quality, lesson-learned, agent-failure]
---

# Hardcoded Instances Fail — Build Frameworks Not Solutions

## Summary

When building systems meant to be reusable across multiple contexts, hardcoding specific values from one instance (one project, one domain, one team) produces output that is simultaneously too specific to reuse and too generic to be useful. The framework must define HOW TO DEFINE, not just provide current definitions. Config with specific values is NOT a framework — it is an instance that looks like a framework.

## Context

> [!warning] When does this lesson apply?
>
> - You are building a config, template, standard, or model that will be consumed by multiple projects
> - You have a working INSTANCE from one project and are tempted to "generalize" it
> - You are told to produce 40+ files and start generating content instead of designing the system
> - You are defining methodology, not executing methodology

## Insight

> [!tip] The Core Distinction
>
> | | Framework | Instance |
> |---|---|---|
> | **Defines** | How to define models, types, chains | 9 specific models, 17 specific types |
> | **Contains** | Extension points, composition rules, validation | Hardcoded values, project-specific paths |
> | **Consumed by** | Any project in any domain | One project, one domain |
> | **Changes when** | The meta-model evolves | The project's needs change |
> | **Example** | "A model has stages, each stage has ALLOWED/FORBIDDEN" | "Feature-development has 5 stages: document, design, scaffold, implement, test" |
>
> A correct system has BOTH: the framework defines the rules, instances fill them in. The failure is producing instances and calling them a framework.

The mechanism: when you take a working system (OpenArms's 846-line methodology-document-chain.md) and "generalize" it by changing project-specific values to slightly-less-project-specific values, you produce something that LOOKS generic but IS specific. It works for the source project and nowhere else. It fails the portability test: can a completely different project adopt this without rewriting it?

The solution: design the framework FIRST (what are the extension points, what varies, what is universal), THEN produce instances that demonstrate the framework works.

## Evidence

> [!bug]- Phase 1 Failure: 37 Files Called "Crap" (2026-04-12)
>
> **What happened:** Agent produced 37 files in a single sprint — methodology.yaml, artifact-types.yaml, 3 domain profiles, 16 templates, 6 methodology templates, 15 per-type standards pages, pattern pages, system map, adoption guide, etc. Claimed E003-E006 at 90-95% readiness.
>
> **What the operator said (verbatim):**
> "I feel like we are going to have to review what we are doing in reality.. I think that you hardcoded the solution like I told you not to do"
> "I AM TELING YOU ITS COMPLETE CRAP AND WE HAVE TO RESTART FROM THE START"
> "I DONT WANT HARDCODED, LOW MD QUALITY, DISCONNECTED, WRONGLY NAMES, WRONGLY CLASSIFIED"
>
> **Root cause:** The agent took OpenArms's methodology.yaml as a blueprint and produced a "generic" version with different hardcoded values. The operator had explicitly said the OpenArms yaml was "a mediocre first draft" not to be copied.
>
> **Impact:** Complete restart required. Trust severely damaged. All 37 files needed to be reconsidered.

> [!bug]- Evidence: Config Values ≠ Framework
>
> A config file that says `stages: [document, design, scaffold, implement, test]` is an INSTANCE. A framework says: "Models have stages. Each stage has: allowed_outputs, forbidden_outputs, gate_commands, readiness_range. Stages execute in declared order. Stage N gates block advance to N+1."
>
> The first tells you WHAT. The second tells you HOW TO DEFINE WHAT.

> [!success] Phase 2 Recovery: Research-First Framework Design
>
> After the restart, online research discovered 78 artifact types across 11 categories (not just 17 wiki page types). This revealed the FRAMEWORK question: how do 78 types compose into chains for different models and domains?
>
> The solution: methodology.yaml defines models with GENERIC artifact categories. domain-profiles/*.yaml resolve these to CONCRETE paths and gate commands. The universal layer transfers without modification. The domain layer is project-specific by design.

## Applicability

> [!abstract] Where This Lesson Applies
>
> | Domain | How It Applies |
> |--------|---------------|
> | **Methodology configs** | methodology.yaml must define HOW models work, not just WHICH models exist |
> | **Templates** | Templates must have extension guidance, not just placeholder values |
> | **Standards pages** | Standards must define the QUALITY BAR per aspect, not just show one example |
> | **CLAUDE.md** | The agent config must teach the FRAMEWORK of stage-gated work, not list specific commands |
> | **Export profiles** | Must define the SHAPE of an export, not hardcode one project's needs |
> | **Any multi-project system** | If 2+ consumers, the framework must exist independently of any instance |

> [!warning] Self-Check — Am I About to Make This Mistake?
>
> 1. Am I copying values from one project and changing them slightly?
> 2. Could a completely different project adopt this without rewriting it?
> 3. Does this define HOW TO DEFINE, or just WHAT IS DEFINED?
> 4. Am I producing at speed instead of designing for portability?

### How This Connects — Navigate From Here

> [!abstract] From This Lesson → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **How to build frameworks instead?** | [[methodology-framework|Methodology Framework]] — the META that defines how to define models |
> | **What does the SDLC framework look like?** | [[sdlc-customization-framework|SDLC Customization Framework — Phases, Scale, and Chain Selection]] — three chains, not one hardcoded pipeline |
> | **How do global standards help?** | OpenAPI (define the interface, not the instance), DDD (bounded contexts as extension points), Strategy pattern (select at runtime, not compile-time) |
> | **What is the Goldilocks approach?** | [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]] — identity profile selects chain, chain selects process. Framework adapts; instances don't. |

## Relationships

- DERIVED FROM: [[methodology-standards-initiative-honest-assessment|Methodology Standards Initiative — Honest Assessment]]
- BUILDS ON: [[model-methodology|Model — Methodology]]
- BUILDS ON: [[methodology-framework|Methodology Framework]]
- RELATES TO: [[coverage-blindness-modeling-only-what-you-know|Coverage Blindness — Modeling Only What You Know]]
- RELATES TO: [[always-plan-before-executing|Always Plan Before Executing]]
- RELATES TO: [[standards-must-preach-by-example|Standards Must Preach by Example]]
- FEEDS INTO: [[methodology-adoption-guide|Methodology Adoption Guide]]

## Backlinks

[[methodology-standards-initiative-honest-assessment|Methodology Standards Initiative — Honest Assessment]]
[[model-methodology|Model — Methodology]]
[[methodology-framework|Methodology Framework]]
[[coverage-blindness-modeling-only-what-you-know|Coverage Blindness — Modeling Only What You Know]]
[[always-plan-before-executing|Always Plan Before Executing]]
[[standards-must-preach-by-example|Standards Must Preach by Example]]
[[methodology-adoption-guide|Methodology Adoption Guide]]
[[ecosystem-feedback-loop-wiki-as-source-of-truth|Ecosystem Feedback Loop — Wiki as Source of Truth]]
[[follow-the-method-of-work-not-the-methodology-label|Follow the Method of Work Not the Methodology Label]]
[[new-content-must-integrate-into-existing-pages|New Content Must Integrate Into Existing Pages]]
[[right-process-for-right-context-the-goldilocks-imperative|Principle — Right Process for Right Context — The Goldilocks Imperative]]
[[structured-context-governs-agent-behavior-more-than-content|Principle — Structured Context Governs Agent Behavior More Than Content]]
[[2026-04-10-directive-quality-evolution-epic|Quality Evolution Epic — Level Up Everything, One File at a Time]]
