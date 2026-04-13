---
title: Model Composition Rules
aliases:
  - "Model Composition Rules"
type: concept
domain: cross-domain
status: synthesized
confidence: high
maturity: seed
created: 2026-04-11
updated: 2026-04-11
sources:
  - id: methodology-framework
    type: wiki
    file: wiki/domains/cross-domain/methodology-framework.md
  - id: methodology-config
    type: file
    file: wiki/config/methodology.yaml
  - id: openarms-methodology
    type: file
    file: /home/jfortin/openarms/wiki/config/methodology.yaml
tags: [methodology, composition, models, recursive, multi-track]
---

# Model Composition Rules

## Summary

Formal rules for how methodology models combine when work is multi-layered. Models compose in four patterns — sequential, nested, conditional, and parallel — with explicit rules for scope inheritance, artifact chain resolution, and conflict handling. Without composition rules, agents either ignore nesting (flatten everything to one model) or invent ad-hoc rules that conflict across sessions.

## Key Insights

1. **Composition is how real work actually happens** — a Feature Development epic contains documentation tasks, integration tasks, and research spikes. Each inner task uses a different model. The outer model defines SCOPE; the inner model defines PROCESS.

2. **Four composition patterns cover all cases** — sequential (one after another), nested (model inside a model's stage), conditional (switch model based on runtime condition), and parallel (multiple tracks coexist). Every real-world scenario maps to one of these.

3. **The outer model never loses authority** — when models nest, the outer model's stage boundaries still apply. A Feature Development task in the Infrastructure stage of SFIF still follows Feature Development's artifact chain, but the SFIF stage defines WHAT kind of features are in scope.

4. **Parallel tracks are independent — they don't compose** — the Execution track, PM track, and Knowledge track run simultaneously but don't share stages or artifacts. They coordinate through shared state (backlog, wiki, completion logs), not through model composition.

## Deep Analysis

### The Four Composition Patterns

> [!abstract] Composition Pattern Summary
>
> | Pattern | What Happens | When to Use | Example |
> |---------|-------------|-------------|---------|
> | Sequential | Model A completes, then Model B starts | Phased work with clear handoff | Research → Feature Development |
> | Nested | Model B runs inside Model A's stage | Complex stage requiring its own process | Feature Dev inside SFIF's features stage |
> | Conditional | Model selected at runtime based on conditions | Variable work where type isn't known upfront | Task starts as docs, promotes to feature-dev |
> | Parallel | Models A and B run simultaneously on different tracks | Independent concerns with shared state | Execution + PM + Knowledge tracks |

### Sequential Composition

Two or more models run in sequence, each completing fully before the next begins.

**Rules:**
- Model A must reach its readiness cap before Model B starts
- No artifact dependencies cross the model boundary — Model B reads Model A's outputs but doesn't depend on its internal artifacts
- The transition point is explicit: "when Research completes (50% readiness), begin Feature Development from document stage"

> [!example]- Example: Research → Feature Development
>
> A spike task runs the Research model (document → design, capped at 50%). The design stage produces a recommendation. If the recommendation is "build it," a new epic is created using Feature Development model, starting from document stage. The research artifacts become inputs to the new epic's document stage — but the Feature Development model starts fresh, not from 50%.

### Nested Composition

One model runs inside another model's stage. The outer model defines scope; the inner model defines process.

**Rules:**
- The outer model's stage defines WHAT kind of work belongs (e.g., SFIF's "infrastructure" stage = tooling and automation work)
- The inner model defines HOW that work is executed (e.g., Feature Development's 5-stage cycle)
- The inner model runs its FULL artifact chain — nesting doesn't skip inner stages
- Readiness propagation: inner task readiness feeds into outer stage readiness (weighted average of all inner tasks)
- The outer stage is complete when ALL inner tasks are complete
- Artifact scope: inner model artifacts live within the outer stage's scope directory/domain

> [!warning] Critical Rule: Inner Models Don't Skip Stages
>
> A Feature Development task nested inside SFIF's features stage still runs all 5 stages: document, design, scaffold, implement, test. The nesting defines WHAT the feature IS (it's a "features-stage" deliverable), not how many stages it goes through.

> [!example]- Example: SFIF → Feature Development
>
> ```
> Project Lifecycle (SFIF):
>   scaffold:     → project structure, directory layout
>   foundation:   → core deps, CI (inner: documentation model per task)
>   infrastructure: → tooling, automation (inner: feature-development per task)
>   features:     → user-facing features (inner: feature-development per task)
>     ├── Task A (feature-dev): document → design → scaffold → implement → test
>     ├── Task B (feature-dev): document → design → scaffold → implement → test
>     └── Task C (bug-fix): document → implement → test
> ```
>
> The SFIF features stage readiness = average of Task A + B + C readiness.

### Conditional Composition

Model is selected or changed based on runtime conditions. This handles cases where the work type isn't known upfront or changes during execution.

**Rules:**
- The initial model is selected via model_selection rules (task_type primary, overrides for scale/context)
- If conditions change mid-execution, the task can be PROMOTED to a different model
- Promotion preserves completed stages — if document stage is done under Documentation model and the task promotes to Feature Development, the document stage doesn't re-run
- Promotion ADDS stages — the new model's remaining stages are appended
- Demotion is not allowed — you can't go from Feature Development to Hotfix to skip stages

> [!tip] Mid-Execution Model Promotion
>
> | Scenario | Original Model | Promoted To | What Happens |
> |----------|---------------|-------------|-------------|
> | Docs task reveals a design need | documentation | research | Design stage added after document |
> | Research finds something to build | research | feature-development | Scaffold, implement, test added after design |
> | Bug fix requires refactoring | bug-fix | refactor | Scaffold stage inserted before implement |
> | Simple task grows complex | hotfix | feature-development | Document and design prepended (may re-run) |

### Parallel Composition

Multiple models run simultaneously on independent tracks. They don't share stages or compose artifact chains — they coordinate through shared state.

**Rules:**
- Each track has its own model, backlog, and cadence
- Tracks share: wiki (knowledge state), backlog (work state), completion logs (history)
- No artifact dependencies between parallel tracks — if Track A needs Track B's output, that's a dependency and should be modeled as sequential, not parallel
- Common parallel configuration: Execution track (feature-development model) + PM track (documentation model) + Knowledge track (knowledge-evolution model)

> [!abstract] The Three Standard Tracks
>
> | Track | Model | Material | Artifacts | Cadence |
> |-------|-------|----------|-----------|---------|
> | Execution | feature-development (or per-task) | Source code, config, infra | Code, tests, deploys | Continuous |
> | PM | documentation | Backlog, plans, reviews | Wiki pages, completion logs | Per-session |
> | Knowledge | knowledge-evolution | Wiki, logs, patterns | Lessons, patterns, decisions | Weekly or trigger-based |

### Conflict Resolution

> [!warning] What Happens When Models Disagree
>
> | Conflict | Resolution |
> |----------|-----------|
> | Inner model wants to skip a stage | Not allowed — inner model runs its full chain |
> | Outer stage scope doesn't match inner model | Outer wins — inner model produces artifacts scoped to the outer stage's domain |
> | Two parallel tracks both modify the same file | Not composition — this is a dependency that should be sequentialized |
> | Conditional promotion creates impossible state | Preserve completed stages, add remaining from new model, never subtract |
> | Nested model's readiness exceeds outer stage range | Inner readiness is used for task-level tracking; outer stage readiness is the aggregate |

## Open Questions

> [!question] Should composition rules be machine-readable in methodology.yaml (they currently are for nested only via `composition_model`), or is wiki documentation sufficient for sequential/conditional/parallel? (Recommendation: document first, formalize in config when enforcement needs it)

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **What principle applies?** | [[right-process-for-right-context-the-goldilocks-imperative|Principle — Right Process for Right Context — The Goldilocks Imperative]] |
> | **What is my identity?** | [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]] |
> | **System map** | [[methodology-system-map|Methodology System Map]] |

## Relationships

- BUILDS ON: [[methodology-framework|Methodology Framework]]
- BUILDS ON: [[model-methodology|Model — Methodology]]
- BUILDS ON: [[artifact-chains-by-model|Artifact Chains by Methodology Model]]
- RELATES TO: [[stage-gate-methodology|Stage-Gate Methodology]]
- RELATES TO: [[execution-modes-and-end-conditions|Execution Modes and End Conditions]]
- RELATES TO: [[backlog-hierarchy-rules|Backlog Hierarchy Rules]]
- FEEDS INTO: [[model-methodology-standards|Methodology Standards — What Good Execution Looks Like]]

## Backlinks

[[methodology-framework|Methodology Framework]]
[[model-methodology|Model — Methodology]]
[[artifact-chains-by-model|Artifact Chains by Methodology Model]]
[[stage-gate-methodology|Stage-Gate Methodology]]
[[execution-modes-and-end-conditions|Execution Modes and End Conditions]]
[[backlog-hierarchy-rules|Backlog Hierarchy Rules]]
[[model-methodology-standards|Methodology Standards — What Good Execution Looks Like]]
[[methodology-adoption-guide|Methodology Adoption Guide]]
