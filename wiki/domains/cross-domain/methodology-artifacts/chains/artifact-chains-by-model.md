---
title: Artifact Chains by Methodology Model
aliases:
  - "Artifact Chains by Methodology Model"
type: reference
domain: cross-domain
status: synthesized
confidence: authoritative
maturity: growing
created: 2026-04-11
updated: 2026-04-11
sources:
  - id: methodology-config
    type: file
    file: wiki/config/methodology.yaml
  - id: artifact-types
    type: file
    file: wiki/config/artifact-types.yaml
  - id: design-doc
    type: file
    file: wiki/domains/cross-domain/e003-artifact-type-system-design.md
tags: [methodology, artifact-chains, models, reference, stage-gate]
---

# Artifact Chains by Methodology Model

## Summary

Complete artifact chain documentation for all 9 methodology models. For each model: the stage sequence, required artifacts per stage, dependencies between artifacts, and what domain profiles resolve. Machine-readable authority is `wiki/config/methodology.yaml`; this page provides human-readable context, rationale, and a full worked example for the Feature Development model.

## Reference Content

### Model Summary

> [!info] All 9 Models at a Glance
>
> | Model | Stages | Readiness Cap | When to Use |
> |-------|--------|--------------|-------------|
> | Feature Development | document → design → scaffold → implement → test | 100% | Complex work, solution unknown |
> | Research | document → design | 50% | Investigation without implementation |
> | Knowledge Evolution | document → implement | 100% | Distill lessons/patterns/decisions from wiki |
> | Documentation | document | 100% | Single-page wiki work |
> | Bug Fix | document → implement → test | 100% | Restore correct behavior |
> | Refactor | document → scaffold → implement → test | 100% | Restructure without behavior change |
> | Hotfix | implement → test | 100% | Emergency, solution already known |
> | Integration | scaffold → implement → test | 100% | Wire standalone modules into runtime |
> | Project Lifecycle (SFIF) | scaffold → foundation → infrastructure → features | N/A | Macro project planning (nests other models) |

### Feature Development — Full Chain

The most complex model. 5 stages, multiple artifacts per stage, rich dependency chain.

> [!abstract] Feature Development Artifact Chain
>
> | Stage | Required Artifacts | Depends On | Forbidden |
> |-------|--------------------|-----------|-----------|
> | **Document** | Requirements spec (1+), Infrastructure analysis, Gap analysis | — | Code files, test files |
> | **Design** | Design document (1+), ADR, Tech spec, Test plan | All Document artifacts | Code files, test files |
> | **Scaffold** | Type definitions (1+), Test stubs (1+) | Design documents | Implementation code, real tests |
> | **Implement** | Implementation (1+), Integration wiring (1+) | Scaffold types | Test modifications |
> | **Test** | Test implementations (1+), Test results (0 failures) | Test stubs + implementation | — |

> [!example]- Worked Example: Building a New Validation Feature
>
> **Task:** Add per-type content threshold validation to the wiki pipeline.
>
> **Document Stage (0→25%):**
> - Artifact 1: Infrastructure analysis — maps existing validate.py, wiki-schema.yaml, quality-standards.yaml
> - Artifact 2: Gap analysis — identifies 8 missing page type templates, no per-type thresholds
> - Artifact 3: Requirements spec — FR/NFR/AC for the artifact type system
> - Gate: Wiki pages exist, no code files created
>
> **Design Stage (25→50%):**
> - Artifact 1: Design document — 7 decisions (types stay as wiki pages, one new type operations-plan, etc.)
> - Depends on: All 3 document-stage artifacts
> - Gate: Design doc exists, no code files created
>
> **Scaffold Stage (50→80%):**
> - Artifact 1: wiki/config/artifact-types.yaml — type definitions with thresholds (zero behavior)
> - Artifact 2: 16 template files — empty structures with placeholders
> - Artifact 3: Schema update — new type added to enum and required_sections
> - Depends on: Design document
> - Gate: Pipeline post passes, no business logic in config
>
> **Implement Stage (80→95%):**
> - Artifact 1: validate.py extension — reads artifact-types.yaml, checks thresholds
> - Artifact 2: pipeline.py scaffolder update — handles new types and methodology/ prefix
> - Depends on: Scaffold config and templates
> - Gate: Pipeline post passes with 0 errors, validation catches missing sections
>
> **Test Stage (95→100%):**
> - Artifact 1: Verify all existing pages still pass validation (backwards compatibility)
> - Artifact 2: Verify new templates scaffold correctly for all types
> - Artifact 3: Verify per-type thresholds produce warnings on thin pages
> - Gate: 0 validation errors on full wiki

### Research — Chain

> [!info] 2-Stage Investigation Chain
>
> | Stage | Required Artifacts | Depends On | Forbidden |
> |-------|--------------------|-----------|-----------|
> | **Document** | Research wiki pages (1+) with sources and evidence | — | Code files, test files |
> | **Design** | Options analysis (1+) with recommendation | Document wiki pages | Code files, test files |
>
> Readiness cap: 50%. When document + design are complete, the research IS done. No implementation expected.

### Knowledge Evolution — Chain

> [!info] 2-Stage Distillation Chain
>
> | Stage | Required Artifacts | Depends On | Forbidden |
> |-------|--------------------|-----------|-----------|
> | **Document** | Source inventory — pages to distill from, convergence identified | — | — |
> | **Implement** | Evolved page (lesson, pattern, or decision) with evidence | Source inventory | — |
>
> The "implement" stage for knowledge evolution means writing the evolved page, not writing code. Gate: page passes pipeline post and has evidence from listed sources.

### Bug Fix — Chain

> [!info] 3-Stage Fix Chain
>
> | Stage | Required Artifacts | Depends On | Forbidden |
> |-------|--------------------|-----------|-----------|
> | **Document** | Bug analysis — description, reproduction, root cause with file refs | — | — |
> | **Implement** | Code fix addressing documented root cause | Bug analysis | New architecture |
> | **Test** | Regression test + 0 failures | Code fix | — |
>
> No design stage. Bug fixes don't introduce new architecture — if the fix requires design, it's a feature, not a bug.

### Refactor — Chain

> [!info] 4-Stage Restructure Chain
>
> | Stage | Required Artifacts | Depends On | Forbidden |
> |-------|--------------------|-----------|-----------|
> | **Document** | Current structure mapped, target structure defined, migration plan | — | — |
> | **Scaffold** | New type definitions for target structure | Document | — |
> | **Implement** | Code moved to new structure, consumers updated | Scaffold types | — |
> | **Test** | Tests proving behavior is UNCHANGED | Implementation | — |
>
> No design stage. If the refactor requires design decisions about new architecture, it's a feature, not a refactor.

### Hotfix — Chain

> [!info] 2-Stage Emergency Chain
>
> | Stage | Required Artifacts | Depends On | Forbidden |
> |-------|--------------------|-----------|-----------|
> | **Implement** | Direct code fix for known problem | — | — |
> | **Test** | Proof the fix works + 0 failures | Code fix | — |
>
> No document stage. Problem and solution are already known. Quality tier: Pyramid by definition (deliberate compression).

### Integration — Chain

> [!info] 3-Stage Wiring Chain
>
> | Stage | Required Artifacts | Depends On | Forbidden |
> |-------|--------------------|-----------|-----------|
> | **Scaffold** | Bridge adapter types (1+), test stubs (1+) | — | Business logic |
> | **Implement** | Bridge logic (<80 LOC) + existing file modified to import bridge | Scaffold types | — |
> | **Test** | Tests proving wiring works — import chain, data flow + 0 failures | Implementation | — |
>
> The bridge module pattern is recommended: thin adapter between new module and existing consumer.

### Documentation — Chain

> [!info] 1-Stage Documentation Chain
>
> | Stage | Required Artifacts | Depends On | Forbidden |
> |-------|--------------------|-----------|-----------|
> | **Document** | Complete wiki page meeting all quality gates | — | — |
>
> Readiness cap: 100%. Single stage — done when the page passes validation.

### Project Lifecycle (SFIF) — Chain

> [!info] 4-Stage Macro Chain with Composition
>
> | Stage | Required Artifacts | Inner Model | Notes |
> |-------|--------------------|------------|-------|
> | **Scaffold** | Project structure, directory layout, config skeleton | — | — |
> | **Foundation** | Core dependencies, base config, CI setup | documentation | Inner tasks use documentation model |
> | **Infrastructure** | Tooling, automation, deployment pipeline | feature-development | Inner tasks use full model |
> | **Features** | Feature deliverables | feature-development | Each feature runs its own full cycle |
>
> This is the only model that uses **composition** — inner stages invoke other methodology models for their work. The outer model defines SCOPE (what kind of work belongs here), the inner model defines PROCESS (how that work is executed).

### Domain Profile Resolution

> [!tip] How Domain Profiles Layer Over Chains
>
> The artifact chains above define WHAT artifacts are needed. Domain profiles define WHERE they live and HOW they're verified:
>
> | Artifact Category | TypeScript | Python/Wiki | Infrastructure |
> |-------------------|-----------|-------------|---------------|
> | Type definitions | `src/**/*.ts` | `config/**/*.yaml` | `**/*.tf` |
> | Test stubs | `src/**/*.test.ts` | `tests/**/*.py` | `tests/**/*.tf` |
> | Implementation | `src/**/*.ts` | `tools/**/*.py` | `**/*.tf` |
> | Gate (scaffold) | `pnpm tsgo` | `pipeline post` | `terraform validate` |
> | Gate (implement) | `pnpm tsgo` + `pnpm check` | `pipeline post` + `validate` | `terraform plan` |
> | Gate (test) | `pnpm test -- file` | `pipeline post` | `terraform apply (staging)` |
>
> A project declares its domain profile. The methodology engine resolves artifact specs: generic chain + domain overrides = concrete paths and gates.

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **What principle applies?** | [[right-process-for-right-context-the-goldilocks-imperative|Principle — Right Process for Right Context — The Goldilocks Imperative]] |
> | **What is my identity?** | [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]] |
> | **System map** | [[methodology-system-map|Methodology System Map]] |

## Relationships

- IMPLEMENTS: [[methodology-framework|Methodology Framework]]
- BUILDS ON: [[stage-gate-methodology|Stage-Gate Methodology]]
- BUILDS ON: [[task-type-artifact-matrix|Task Type Artifact Matrix]]
- BUILDS ON: [[model-methodology|Model — Methodology]]
- RELATES TO: [[execution-modes-and-end-conditions|Execution Modes and End Conditions]]
- RELATES TO: [[backlog-hierarchy-rules|Backlog Hierarchy Rules]]
- FEEDS INTO: [[model-methodology-standards|Methodology Standards — What Good Execution Looks Like]]

## Backlinks

[[methodology-framework|Methodology Framework]]
[[stage-gate-methodology|Stage-Gate Methodology]]
[[task-type-artifact-matrix|Task Type Artifact Matrix]]
[[model-methodology|Model — Methodology]]
[[execution-modes-and-end-conditions|Execution Modes and End Conditions]]
[[backlog-hierarchy-rules|Backlog Hierarchy Rules]]
[[model-methodology-standards|Methodology Standards — What Good Execution Looks Like]]
[[domain-chain-infrastructure|Artifact Chain — Infrastructure-IaC Domain]]
[[domain-chain-knowledge|Artifact Chain — Knowledge-Evolution Domain]]
[[domain-chain-python-wiki|Artifact Chain — Python-Wiki Domain]]
[[domain-chain-typescript|Artifact Chain — TypeScript-Node Domain]]
[[construction-and-testing-artifacts|Construction and Testing Artifacts — Standards and Guide]]
[[deployment-closure-monitoring-artifacts|Deployment, Closure, and Monitoring Artifacts — Standards and Guide]]
[[initiation-and-planning-artifacts|Initiation and Planning Artifacts — Standards and Guide]]
[[methodology-adoption-guide|Methodology Adoption Guide]]
[[methodology-artifact-taxonomy|Methodology Artifact Taxonomy]]
[[model-composition-rules|Model Composition Rules]]
[[identity-profile|OpenArms — Identity Profile]]
[[identity-profile|OpenFleet — Identity Profile]]
[[requirements-and-design-artifacts|Requirements and Design Artifacts — Standards and Guide]]
[[identity-profile|Research Wiki — Identity Profile]]
[[methodology-artifact-taxonomy-research|Synthesis — Methodology Artifact Taxonomy — Full Spectrum Research]]
