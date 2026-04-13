---
title: E003 Artifact Type System — Requirements Spec
aliases:
  - "E003 Artifact Type System — Requirements Spec"
type: concept
domain: cross-domain
status: synthesized
confidence: high
maturity: growing
created: 2026-04-11
updated: 2026-04-11
sources:
  - id: infrastructure-analysis
    type: file
    file: wiki/domains/cross-domain/methodology-standards-initiative-infrastructure.md
  - id: gap-analysis
    type: file
    file: wiki/domains/cross-domain/methodology-standards-initiative-gaps.md
  - id: openarms-methodology
    type: file
    file: /home/jfortin/openarms/wiki/config/methodology.yaml
  - id: openarms-artifact-spec
    type: file
    file: /home/jfortin/openarms/wiki/domains/architecture/methodology-artifact-spec.md
  - id: wiki-schema
    type: file
    file: wiki/config/wiki-schema.yaml
tags: [methodology, requirements, artifact-types, e003, type-system, templates]
---

# E003 Artifact Type System — Requirements Spec

## Summary

Formal requirements for the Artifact Type System — the foundation epic of the Methodology Standards Initiative. Defines what the system must do (functional requirements), how it must behave (non-functional requirements), and how we'll know it's done (acceptance criteria). The artifact type system answers the question: "for any given methodology model, stage, and domain — what documents must be produced, what must they contain, and how do we verify they're correct?"

## Key Insights

1. **The type system has three layers: taxonomy, templates, and chains** — the taxonomy defines WHAT types exist, templates define HOW each type is structured, and chains define WHEN and WHERE types appear in the methodology workflow. All three layers must be defined for the system to be complete.

2. **Two axes of variation: page type and domain context** — a "scaffold" stage produces TypeScript type stubs in a code project, template files in the wiki, and Terraform stubs in infrastructure. The type system must handle both the generic structure and the domain-specific instantiation.

3. **Operations plan and design plan are the critical missing types** — the distinction between a deterministic checklist (operations plan) and a complex analysis document (design plan) is the single most impactful type definition. It directly addresses agent confusion about what "plan" means.

4. **Artifact chains are directed acyclic graphs, not lists** — each artifact depends on specific artifacts from prior stages. An Interface Spec depends on the Requirements Spec. Test Stubs depend on the Test Plan. The chain captures these dependencies explicitly.

## Deep Analysis

### Functional Requirements

#### FR-1: Artifact Type Taxonomy

> [!info] Defines the complete vocabulary of document/artifact types in the methodology

**FR-1.1** The system SHALL define a taxonomy of artifact types organized into categories:
- **Knowledge pages** — wiki pages that contain synthesized understanding (concept, source-synthesis, comparison, reference, deep-dive, domain-overview, evolution, learning-path)
- **Evolved pages** — wiki pages distilled from other pages (lesson, pattern, decision)
- **Backlog pages** — wiki pages tracking planned work (epic, module, task, note)
- **Methodology documents** — documents produced during stage-gated work (requirements spec, infrastructure analysis, gap analysis, design document, ADR, tech spec, operations plan, test plan)
- **Stage artifacts** — non-wiki deliverables produced at specific stages (type definitions, test stubs, implementation code, integration wiring, test results, compliance reports)

**FR-1.2** Each artifact type definition SHALL include:
- **Name** — unique identifier (kebab-case)
- **Category** — which category above
- **Description** — what this type is and when it's produced
- **Required sections** — ordered list of section headings that must exist
- **Required frontmatter** — fields and default values
- **Minimum content thresholds** — word counts, relationship counts, etc.
- **Styling directives** — which callout types to use where
- **Verification method** — how to check this artifact exists and is complete (file existence, section scanning, word counting, etc.)

**FR-1.3** The taxonomy SHALL be defined in a machine-readable config file (YAML) in addition to being documented as a wiki page.

**FR-1.4** The taxonomy SHALL be extensible — new types can be added without modifying core tooling. The validator reads the taxonomy config; it doesn't hardcode type lists.

#### FR-2: Templates for All Page Types

> [!info] Every page type agents create has a template defining structure, defaults, and styling guidance

**FR-2.1** Templates SHALL exist for ALL page types that agents create. Currently missing:
- concept
- source-synthesis
- comparison
- reference
- deep-dive
- epic (backlog)
- module (backlog)
- task (backlog)
- note (backlog/log)

**FR-2.2** Each template SHALL include:
- Complete frontmatter with placeholder variables ({{title}}, {{domain}}, {{date}})
- Sensible defaults for type-specific fields (e.g., layer for evolved types, maturity: seed for new pages)
- All required sections per wiki-schema.yaml in correct order
- Inline styling comments (<!-- STYLING: ... -->) directing which callout types to use
- Inline content guidance (<!-- MIN 50 words. State the core insight plainly. -->)

**FR-2.3** Templates SHALL be consumable by the scaffold command:
```
python3 -m tools.pipeline scaffold <type> <title>
```
The scaffolder SHALL read templates from wiki/config/templates/ and fill in variables.

**FR-2.4** Templates for methodology documents (requirements spec, ADR, operations plan, etc.) SHALL be separate from wiki page templates, stored in wiki/config/templates/methodology/ or similar.

#### FR-3: Operations Plan vs Design Plan

> [!warning] Critical distinction — the single highest-impact type definition

**FR-3.1** The system SHALL formally define two distinct plan types:

**Operations Plan:**
- Sequential list of steps with validation criteria per step
- Deterministic — given the same input, any agent produces the same output
- Delegatable to a mechanical agent (no judgment required)
- Each step specifies: action, expected output, validation check, rollback on failure
- Used for: deployment checklists, migration steps, ingestion sequences, build processes

**Design Plan:**
- Analysis of a problem space with alternatives and trade-offs
- Non-deterministic — requires judgment, creativity, domain expertise
- NOT delegatable to a mechanical agent
- Includes: problem statement, constraints, options analysis, recommendation, decision rationale, risks
- Used for: architecture decisions, feature design, system redesign, methodology changes

**FR-3.2** Each plan type SHALL have its own template with clearly different structures.

**FR-3.3** The methodology model definitions SHALL specify which plan type is required at which stage:
- Design plan → design stage (Feature Development, Research models)
- Operations plan → implement stage (as a work breakdown), test stage (as a verification plan)

#### FR-4: Artifact Chains per Methodology Model

> [!info] For every model: complete stage → artifact mapping with dependencies

**FR-4.1** The system SHALL document the artifact chain for every methodology model:
- Feature Development (5 stages)
- Research (2 stages)
- Knowledge Evolution (2 stages)
- Documentation (1 stage)
- Bug Fix (3 stages)
- Refactor (4 stages)
- Hotfix (2 stages)
- Integration (3 stages)
- Project Lifecycle / SFIF (4 stages)

**FR-4.2** Each artifact chain SHALL specify per stage:
- **Required artifacts** — must exist for the stage gate to pass
- **Optional artifacts** — may exist if conditions apply (with conditions stated)
- **Forbidden artifacts** — must NOT exist (stage boundary enforcement)
- **Dependencies** — which prior-stage artifacts this artifact depends on

**FR-4.3** Artifact chains SHALL be documented both as:
- Wiki pages (human-readable, with examples and rationale)
- Machine-readable config (YAML, for tooling consumption)

**FR-4.4** The artifact chain for Feature Development (the most complex model) SHALL be documented at full depth with at least one concrete example showing all 5 stages producing all required artifacts.

#### FR-5: Domain-Specific Artifact Variations

> [!abstract] Same stage, different deliverables depending on context

**FR-5.1** The system SHALL define domain profiles for at least 3 domains:
- **TypeScript/Node project** (e.g., OpenArms) — src/ files, .test.ts, Zod schemas, pnpm gates
- **Python/wiki project** (e.g., research wiki) — wiki pages, Python tools, pipeline post gates
- **Infrastructure/IaC project** (e.g., devops-control-plane) — Terraform/YAML, deploy scripts, plan/apply gates

**FR-5.2** Domain profiles SHALL specify per-artifact-type:
- File path patterns (where artifacts live)
- Gate commands (what passes validation)
- Domain-specific required content (TypeScript exports vs Python functions vs Terraform resources)
- Domain-specific forbidden patterns (no src/ writes in document stage for code projects; no wiki/ modifications for infrastructure planning stage)

**FR-5.3** Domain profiles SHALL layer over the generic artifact definitions:
```
Generic artifact (from taxonomy) + Domain profile overrides = Resolved artifact spec
```

**FR-5.4** A project SHALL be able to declare its domain profile in its configuration (CLAUDE.md, methodology.yaml, or project config) and have the methodology engine resolve the correct artifact specs.

#### FR-6: Schema and Validation Extensions

**FR-6.1** The existing wiki-schema.yaml SHALL be extended (not replaced) to incorporate:
- required_sections for the `module` type (currently undefined)
- New page types if any are added (operations-plan, design-plan, or subtypes)
- Artifact type references (linking page types to artifact type definitions)

**FR-6.2** The validate tool SHALL be extended to check:
- Template compliance — does a page contain all sections defined in its template?
- Content thresholds per type — section-level word count minimums (not just summary-level)
- Styling compliance — do evolved pages have callouts as directed by their template?

**FR-6.3** The scaffold command SHALL be extended to:
- Support all new templates
- Accept domain profile as parameter (for methodology document templates)
- Generate proper frontmatter defaults from template + domain profile

### Non-Functional Requirements

**NFR-1: Backwards Compatibility** — All existing wiki pages SHALL remain valid after the type system is introduced. The system extends, never breaks, existing schema.

**NFR-2: Human-Readable First** — Every machine-readable config SHALL have a corresponding human-readable wiki page explaining the same content with context and rationale. Config is for tools; wiki pages are for understanding.

**NFR-3: Incremental Adoption** — Projects SHALL be able to adopt the type system incrementally. A project using only 2 methodology models should not need to configure all 9.

**NFR-4: Single Source of Truth** — Artifact type definitions SHALL live in one place (config/) and be consumed by tools, templates, and documentation. No duplication between config and wiki prose.

**NFR-5: Validation Speed** — Extended validation SHALL complete in <10 seconds for the full wiki (~200 pages). No per-page network calls or heavy computation.

**NFR-6: Portability** — Artifact type definitions SHALL not reference any specific technology stack in their core definitions. Domain-specific details live ONLY in domain profiles.

### Acceptance Criteria

> [!success] How We Know E003 Is Done
>
> | ID | Criterion | Verification |
> |----|-----------|-------------|
> | AC-1 | Artifact type taxonomy config exists in config/ with all types defined | File exists, YAML parses, all types from FR-1.1 present |
> | AC-2 | Templates exist for all 9 missing page types | `ls wiki/config/templates/` shows all types; scaffolder can generate from each |
> | AC-3 | Operations plan template is structurally distinct from design plan template | Templates differ in required sections; reviewer can distinguish at a glance |
> | AC-4 | Artifact chains documented for all 9 models | Wiki pages exist; each chain shows required/optional/forbidden/dependencies per stage |
> | AC-5 | Artifact chains available as machine-readable config | YAML config exists; matches wiki page content |
> | AC-6 | Domain profiles exist for ≥3 domains | Config files exist; each overrides ≥1 artifact type with domain-specific details |
> | AC-7 | Validation catches missing required sections per template | Test: create page with missing section → validate → error reported |
> | AC-8 | Existing pages still pass validation after changes | `pipeline post` → 0 errors on full wiki |
> | AC-9 | Scaffold command supports all new templates | `pipeline scaffold <type> <title>` succeeds for every type |
> | AC-10 | Feature Development artifact chain has complete worked example | Wiki page with 5-stage walkthrough, all artifacts shown |

### Out of Scope

> [!warning] Explicitly NOT in E003
>
> - **Portable methodology.yaml** — that's E004. E003 defines the type system; E004 packages it for export.
> - **Enforcement hooks or scripts** — that's E005. E003 defines what to validate; E005 defines how to enforce it.
> - **Annotated exemplars** — that's E006. E003 creates templates; E006 creates gold-standard instances.
> - **Tooling for methodology compliance reporting** — that's E005.
> - **Domain profiles beyond 3** — future work. Initial 3 prove the pattern.
> - **Runtime enforcement** — E003 is a definition system, not an execution engine.

### Module Breakdown (Preliminary)

> [!abstract] Proposed Module Structure
>
> | Module | Scope | Estimate | Key Deliverables |
> |--------|-------|----------|-----------------|
> | M1: Taxonomy | Define all artifact types in YAML + wiki page | L | wiki/config/artifact-types.yaml, wiki page |
> | M2: Knowledge Templates | Templates for concept, source-synthesis, comparison, reference, deep-dive | M | 5 template files |
> | M3: Backlog Templates | Templates for epic, module, task, note | S | 4 template files |
> | M4: Plan Types | Operations plan vs design plan definitions + templates | M | 2 template files, schema update |
> | M5: Artifact Chains | Full chains for all 9 models in wiki + config | XL | 9 wiki pages, config YAML |
> | M6: Domain Profiles | TypeScript, Python/wiki, Infrastructure profiles | L | 3 profile configs |
> | M7: Validation Extension | Extend validate.py + scaffold command | M | Tool updates, tests |

## Open Questions

> [!question] Should methodology document types (requirements spec, ADR, operations plan) be new wiki page types or a new category outside the wiki schema? (Requires: design decision — are these wiki-managed or project-local?)

> [!question] How granular should domain profile overrides be? Per-artifact-type? Per-stage? Per-model? (Requires: design — balance expressiveness vs complexity)

> [!question] Should the artifact chain config be inside methodology.yaml or a separate artifact-chains.yaml? (Requires: design — single file vs modular config)

> [!question] How do we handle artifact chains for composed models (SFIF nesting Feature Development)? Flatten or preserve nesting? (Requires: design with examples)

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **What principle applies?** | [[right-process-for-right-context-the-goldilocks-imperative|Principle — Right Process for Right Context — The Goldilocks Imperative]] |
> | **What is my identity?** | [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]] |
> | **System map** | [[methodology-system-map|Methodology System Map]] |

## Relationships

- IMPLEMENTS: [[E003-artifact-type-system|Artifact Type System]] (E003)
- BUILDS ON: [[methodology-standards-initiative-infrastructure|Methodology Standards Initiative — Infrastructure Analysis]]
- BUILDS ON: [[methodology-standards-initiative-gaps|Methodology Standards Initiative — Gap Analysis]]
- RELATES TO: [[methodology-framework|Methodology Framework]]
- RELATES TO: [[task-type-artifact-matrix|Task Type Artifact Matrix]]
- RELATES TO: [[stage-gate-methodology|Stage-Gate Methodology]]
- FEEDS INTO: [[model-methodology|Model — Methodology]]
- FEEDS INTO: [[model-llm-wiki-standards|LLM Wiki Standards — What Good Looks Like]]

## Backlinks

[[E003-artifact-type-system|Artifact Type System]]
[[methodology-standards-initiative-infrastructure|Methodology Standards Initiative — Infrastructure Analysis]]
[[methodology-standards-initiative-gaps|Methodology Standards Initiative — Gap Analysis]]
[[methodology-framework|Methodology Framework]]
[[task-type-artifact-matrix|Task Type Artifact Matrix]]
[[stage-gate-methodology|Stage-Gate Methodology]]
[[model-methodology|Model — Methodology]]
[[model-llm-wiki-standards|LLM Wiki Standards — What Good Looks Like]]
[[e003-artifact-type-system-design|E003 Artifact Type System — Design Document]]
