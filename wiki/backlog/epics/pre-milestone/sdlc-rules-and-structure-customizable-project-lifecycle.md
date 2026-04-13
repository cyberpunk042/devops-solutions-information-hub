---
title: SDLC Rules and Structure — Customizable Project Lifecycle
aliases:
  - "SDLC Rules and Structure — Customizable Project Lifecycle"
type: epic
domain: backlog
status: draft
priority: P0
task_type: epic
current_stage: document
readiness: 10
progress: 0
stages_completed:
artifacts:
  - "wiki/domains/cross-domain/sdlc-customization-framework.md"
  - "wiki/domains/cross-domain/readiness-vs-progress.md"
  - "wiki/domains/cross-domain/three-pm-levels.md"
confidence: high
created: 2026-04-12
updated: 2026-04-13
sources:
  - id: operator-sdlc-directive
    type: file
    file: raw/notes/2026-04-12-mega-vision-directive.md
  - id: operator-readiness-directive
    type: file
    file: raw/notes/2026-04-12-readiness-progress-pm-levels-directive.md
tags: [sdlc, customization, lifecycle, phases, scale, harness, pm-levels, readiness, progress]
---

# SDLC Rules and Structure — Customizable Project Lifecycle

## Summary

Build a customizable SDLC framework that adapts to project phase (POC→MVP→Staging→Production), codebase scale (10k→15M lines), and organizational needs (solo→team→fleet). Projects configure their entire lifecycle — not just methodology models but the full SDLC chain, PM infrastructure level, harness version, readiness/progress gates, and traceability requirements. The wiki provides three pre-built chains (simplified, default, full) plus the framework for defining custom chains. This enables companies, teams, and individual developers to adopt at their own pace and scale.

## Operator Directive

> "we are also going to offer an sdlc rules and structure that will allow project to customize not only their methodologies but the whole sdlc (not that they can't just copy the our wiki example but other company might need their own or I might realize myself we need a few type to be able to adapt to Type and Size of projects and repository and complexity and phases (POC TO MVP TO STAGING TO PRODUCTION which impact changes and how we work."

> "Imagine dealing with a 10k code base vs 100k vs 1m vs 5m vs 15m..... the scale and the need for tidiness and respect of full SDLC become more and more needed as it grow"

> "So its would be logical to have a middle ground and at least one simplified and one full chain and the default is the middle ground."

> "Like readiness is one side of the sdlc and the progress is the other where after the information and definitions was ready to start working on / from."

> "Lets remember they are also at least three level of PM."

## Goals

- Three pre-built SDLC chains (simplified, middle ground, full) defined as config profiles
- Phase-aware methodology adaptation (POC gets short loops, Production gets full traceability)
- Scale-aware process selection (10k = minimal process, 1M+ = full governance)
- Readiness vs progress as two independent tracked dimensions at every hierarchy level
- Three PM levels (L1: Wiki, L2: Fleet, L3: Full PM) formally defined with capabilities per level
- Harness version progression (v1→v2→v3) mapped to PM levels and SDLC integration
- Frontmatter field reference documenting every field, what it means, when required, what it enables
- SDLC chain selection wizard or decision tree for new projects
- Migration guide between chains (simplified→default→full) as projects grow

## Done When

- [ ] `wiki/config/sdlc-chains/simplified.yaml` defines the simplified chain with stages, artifacts, gates
- [ ] `wiki/config/sdlc-chains/default.yaml` defines the middle-ground chain
- [ ] `wiki/config/sdlc-chains/full.yaml` defines the full chain
- [ ] Decision page: When to use which chain (with worked examples per phase × scale)
- [ ] Frontmatter field reference page: every field documented with meaning, requirement level, and what it enables
- [ ] PM level reference page: L1→L2→L3 capabilities, prerequisites, migration triggers
- [ ] Harness version guide: v1→v2→v3 what changes, when to upgrade, what it unblocks
- [ ] Readiness vs progress model validated against OpenFleet implementation
- [ ] At least one external project can adopt the simplified chain from the wiki's documentation alone
- [ ] Pipeline post returns 0 errors
- [ ] Operator confirms: "I can pick the right chain for any project in under 2 minutes"

## Scale and Model

> [!info] Epic Parameters
>
> | Parameter | Value |
> |-----------|-------|
> | **Model** | feature-development |
> | **Quality tier** | Skyscraper |
> | **Estimated modules** | 5 |
> | **Estimated tasks** | 20-30 |
> | **Dependencies** | E003 (Artifact Type System), Gateway Tools epic (for config queries) |

## Stage Artifacts (per methodology model)

> [!abstract] Stage → Artifact Map
>
> | Stage | Required Artifacts | Template |
> |-------|--------------------|----------|
> | Document | Online research (SDLC frameworks, maturity models), gap analysis vs current system | wiki/config/templates/methodology/gap-analysis.md |
> | Design | SDLC chain specifications, field reference design, PM level architecture | wiki/config/templates/methodology/requirements-spec.md |
> | Scaffold | YAML chain profiles, field definitions in wiki-schema.yaml | N/A |
> | Implement | Chain configs, wiki reference pages, selection wizard, migration guide | N/A |
> | Test | External project adoption test, pipeline validation | N/A |

## Module Breakdown

| Module | Delivers | Est. Tasks |
|--------|----------|-----------|
| M1: Three SDLC Chains | simplified.yaml, default.yaml, full.yaml config profiles | 4-5 |
| M2: Phase and Scale Model | Decision trees, worked examples, phase transition triggers | 4-5 |
| M3: Frontmatter Field Reference | Complete field documentation with requirement levels and automation enablement | 3-4 |
| M4: PM Level and Harness Guide | L1→L2→L3 capabilities, v1→v2→v3 migration, prerequisites | 4-5 |
| M5: Selection and Migration | Chain selection wizard, migration paths, external adoption guide | 4-5 |

## Dependencies

- **E003 (Artifact Type System):** Chain configs reference artifact types. Current state: 40%.
- **Gateway Tools epic:** Selection wizard ideally uses gateway query API. Can work without it (static wiki pages).
- **OpenFleet scan data:** Readiness vs progress model validated against real OpenFleet data (in raw/).

## Open Questions

> [!question] ~~Should SDLC chains be YAML configs or wiki pages?~~
> **RESOLVED:** Both. Already implemented. YAML for policy config, wiki page for explanation.
> YAML = machine-readable, composable, validatable. Wiki pages = human-readable, discoverable. Both? Config for machines, wiki page explaining the config for humans?

> [!question] ~~How do phase transitions trigger chain upgrades?~~
> **RESOLVED:** SDLC chain upgrade_triggers are signals. When triggers are met, operator decides. Not automatic.
> POC→MVP: manual operator decision? Metric-based (first paying user, first SLA)? Should the wiki recommend triggers or just document options?

> [!question] ~~Should the simplified chain have ANY stage gates?~~
> **RESOLVED:** Advisory only. The operator IS the gate at simplified level. No infrastructure enforcement.
> Or is simplified = "just build it, no gates"? Tension: gates slow POCs but prevent the "untraceable mess" that makes MVP→Production painful.

> [!question] ~~How does this relate to OpenFleet's delivery phases?~~
> **RESOLVED:** OpenFleet phases (conversation→analysis→investigation→building→verification→delivery) are an INSTANCE of the generic stage sequence (document→design→scaffold→implement→test). Different names, same structure.
> OpenFleet has delivery_phase: mvp | staging | production which controls test depth, docs requirements, security checks. Is this the same concept or a parallel dimension?

### How This Connects — Navigate From Here

> [!abstract] From This Epic → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **Goldilocks** | [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]] |
> | **System map** | [[methodology-system-map|Methodology System Map]] |

## Relationships

- IMPLEMENTS: [[sdlc-customization-framework|SDLC Customization Framework — Phases, Scale, and Chain Selection]]
- BUILDS ON: [[model-methodology|Model — Methodology]]
- BUILDS ON: [[readiness-vs-progress|Readiness vs Progress — Two-Dimensional Work Tracking]]
- BUILDS ON: [[three-pm-levels|Three PM Levels — Wiki to Fleet to Full Tool]]
- RELATES TO: [[backlog-hierarchy-rules|Backlog Hierarchy Rules]]
- RELATES TO: [[methodology-adoption-guide|Methodology Adoption Guide]]
- DEPENDS ON: [[E003-artifact-type-system|Artifact Type System]]

## Backlinks

[[sdlc-customization-framework|SDLC Customization Framework — Phases, Scale, and Chain Selection]]
[[model-methodology|Model — Methodology]]
[[readiness-vs-progress|Readiness vs Progress — Two-Dimensional Work Tracking]]
[[three-pm-levels|Three PM Levels — Wiki to Fleet to Full Tool]]
[[backlog-hierarchy-rules|Backlog Hierarchy Rules]]
[[methodology-adoption-guide|Methodology Adoption Guide]]
[[E003-artifact-type-system|Artifact Type System]]
[[second-brain-integration-requirements|Second Brain Integration System — Full Chain Requirements]]
