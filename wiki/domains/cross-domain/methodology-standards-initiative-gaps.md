---
title: "Methodology Standards Initiative — Gap Analysis"
type: concept
domain: cross-domain
status: synthesized
confidence: high
maturity: seed
created: 2026-04-11
updated: 2026-04-11
sources:
  - id: infrastructure-analysis
    type: wiki
    file: wiki/domains/cross-domain/methodology-standards-initiative-infrastructure.md
  - id: operator-directive
    type: file
    file: raw/notes/2026-04-11-methodology-standards-directive.md
tags: [methodology, gap-analysis, artifact-system, agent-compliance, epic-planning]
---

# Methodology Standards Initiative — Gap Analysis

## Summary

Systematic identification of gaps between what the methodology standards initiative requires and what currently exists. Organized by the four confirmed epics (Artifact Type System, Portable Methodology Engine, Agent Compliance Framework, Standards-by-Example). Each gap includes: current state, required state, impact of the gap, affected scope, and complexity assessment. This analysis directly feeds the epic specifications and module breakdowns.

## Key Insights

1. **The largest gap is the artifact type system** — 8 of 14 page types have no template, 9 have no exemplar, and the full artifact chain (model → stage → artifacts → dependencies → domain variations) has never been formally mapped. This is the foundation everything else depends on.

2. **Operations plan vs design plan is a missing concept, not a missing document** — the methodology doesn't distinguish these two fundamentally different kinds of "plan." Without this distinction, agents produce todo lists when design thinking is needed, or overthink what should be a mechanical checklist.

3. **Enforcement infrastructure exists only in OpenArms** — the research wiki documents methodology theory but can't enforce it. No hooks, no stage validation, no artifact checking, no compliance reporting. Every other consumer project would need to build this from scratch.

4. **The CLAUDE.md structural patterns problem is the highest-leverage gap** — how you format and structure agent instructions determines whether agents follow them. This is the "magic tricks" dimension: dividers, nesting, ALLOWED/FORBIDDEN lists, hard vs soft rule separation, command checkpoints. These patterns are discovered empirically but never documented.

5. **Exemplars must be annotated, not just pointed at** — the current gold standards in model-llm-wiki-standards.md say "this page is good" and describe why in prose. But agents need annotated exemplars that show WHY each structural choice was made, inline, so the exemplar teaches by demonstration.

## Deep Analysis

### Gap Inventory by Epic

---

### Epic A: Artifact Type System

> [!warning] Foundation Gap — Everything Else Depends On This
>
> The artifact type system defines WHAT documents exist in the methodology. Without it, standards can't be written (standards for what?), enforcement can't be built (enforcing what?), and exemplars can't be created (exemplars of what?).

#### Gap A1: Incomplete Template Coverage

| Aspect | Details |
|--------|---------|
| **Current state** | 6 templates exist (lesson, pattern, decision, domain-overview, evolution, learning-path). 8 page types have no template. |
| **Required state** | Every page type that agents create has a template defining: required sections, section ordering, minimum content guidance, styling directives, frontmatter defaults. |
| **Impact** | Agents creating concept, source-synthesis, comparison, reference, deep-dive pages operate without structural guidance. Output quality varies wildly. |
| **Affected scope** | wiki/config/templates/, skills/wiki-agent/, tools/pipeline.py (scaffold command) |
| **Complexity** | M — templates for knowledge types are straightforward; backlog types (epic, task, module) need domain-specific guidance |

#### Gap A2: No Formal Artifact Type Definitions

| Aspect | Details |
|--------|---------|
| **Current state** | wiki-schema.yaml defines page types with required frontmatter and required sections. OpenArms methodology-artifact-spec.md defines typed artifacts with verifiable properties, but only for TypeScript code artifacts. |
| **Required state** | A generic artifact type system that defines: artifact categories (wiki page, design document, operations checklist, analysis report, configuration, test evidence), per-category properties (path pattern, required content, verification method), and mapping to stages. |
| **Impact** | Without typed artifacts, validation can only check "does a file exist?" not "does it have the required properties?" Stage gates remain vague. |
| **Affected scope** | config/ (new artifact-types.yaml or extension to wiki-schema.yaml), tools/validate.py |
| **Complexity** | L — requires defining the generic type system AND domain-specific instances |

#### Gap A3: Artifact Chain Not Mapped

| Aspect | Details |
|--------|---------|
| **Current state** | OpenArms methodology.yaml maps artifacts per stage for feature-development model. Other models have partial or no artifact mapping. The wiki's methodology pages describe stages but don't specify exact artifact requirements per model. |
| **Required state** | For every methodology model: complete artifact chain showing stage → required artifacts → dependencies on prior artifacts → domain-specific variations. Documented as wiki pages AND as machine-readable config. |
| **Impact** | Agents don't know what artifacts to produce at each stage. They guess, producing whatever seems right, often wrong. |
| **Affected scope** | Wiki methodology pages, config/ (methodology engine), skills/ |
| **Complexity** | XL — 9 models × 2-5 stages × multiple artifacts × domain variations = large combinatorial space |

#### Gap A4: Operations Plan vs Design Plan Not Distinguished

| Aspect | Details |
|--------|---------|
| **Current state** | "Plan" appears in multiple contexts: design-only mode, plan chain alias, superpowers writing-plans skill. No formal distinction between operations plan (deterministic checklist) and design plan (analysis, alternatives, trade-offs). |
| **Required state** | Two distinct document types with different templates: Operations Plan (sequential steps, validation criteria, delegatable to mechanical agent) and Design Plan (problem analysis, alternatives, decisions, rationale, not delegatable). |
| **Impact** | Agents produce shallow todo lists when design thinking is required. Or they overthink simple mechanical sequences. The operator can't specify "give me an operations plan, not a design" because the vocabulary doesn't exist. |
| **Affected scope** | wiki/config/wiki-schema.yaml (new types or subtypes), wiki/config/templates/ (new templates), methodology model definitions |
| **Complexity** | M — defining the types is clear; the complexity is in making the distinction legible to agents |

#### Gap A5: Domain-Adaptive Artifact Variations

| Aspect | Details |
|--------|---------|
| **Current state** | Templates and schemas are domain-agnostic. A "scaffold" stage means TypeScript type stubs in OpenArms, template files in the wiki, Terraform stubs in infrastructure. But nothing formally defines these variations. |
| **Required state** | Artifact type definitions include domain-specific overrides: "for domain X, scaffold produces Y with properties Z." Projects declare their domain profile, and the methodology engine resolves the right artifact spec. |
| **Impact** | Projects must manually translate generic methodology guidance into their stack. This translation is error-prone and inconsistent. |
| **Affected scope** | config/ (domain profiles), methodology engine, artifact type definitions |
| **Complexity** | L — the pattern is clear (generic + override), but populating overrides for multiple domains is labor-intensive |

---

### Epic B: Portable Methodology Engine

> [!warning] Integration Gap — How Projects Consume the Wiki's Methodology
>
> The methodology engine is the machine-readable, configurable system that projects use to adopt the wiki's methodology. Without it, each project builds its own from scratch (like OpenArms did).

#### Gap B1: No Generic methodology.yaml

| Aspect | Details |
|--------|---------|
| **Current state** | OpenArms has a 753-line methodology.yaml hardcoded to TypeScript/pnpm. The wiki has methodology described in prose across 7 concept pages. No portable, parameterizable methodology config exists. |
| **Required state** | A generic methodology.yaml with: model definitions (stages, artifacts, gates), domain profiles (overrides per stack/context), execution modes, end conditions. Projects import this and layer project-specific overrides. |
| **Impact** | Every new project rebuilds the methodology from scratch. No consistency across the ecosystem. No way to push methodology improvements to all consumers. |
| **Affected scope** | config/ (new methodology-engine.yaml or similar), wiki methodology pages (as authoritative source), export tooling |
| **Complexity** | XL — must generalize from OpenArms-specific to universal while keeping it actionable |

#### Gap B2: No Adoption Guide for Consumers

| Aspect | Details |
|--------|---------|
| **Current state** | wiki/spine/adoption-guide.md exists but covers wiki adoption, not methodology adoption. No guide for "how to configure your project to use this methodology." |
| **Required state** | Step-by-step guide: (1) declare your domain profile, (2) select applicable models, (3) configure stage gates for your stack, (4) install enforcement hooks, (5) set execution mode. With examples for TypeScript, Python, infrastructure, wiki projects. |
| **Impact** | Projects can't adopt the methodology without deep familiarity with both the wiki AND OpenArms internals. Adoption barrier is too high. |
| **Affected scope** | wiki/spine/ (new or updated adoption guide), example configurations per project type |
| **Complexity** | L — depends on methodology engine existing first |

#### Gap B3: No Model Composition Rules

| Aspect | Details |
|--------|---------|
| **Current state** | methodology-framework.md describes 4 composition modes (sequential, nested, conditional, parallel) in prose. No machine-readable composition rules. OpenArms project-lifecycle model references other models but doesn't formally compose them. |
| **Required state** | Formal composition rules: how models nest (SFIF → Feature Development at features stage), how parallel tracks coexist (execution + PM + knowledge), how to resolve conflicts between composed models. |
| **Impact** | Agents can't handle multi-model situations. They either ignore composition or invent ad-hoc rules. |
| **Affected scope** | Methodology engine, model definitions, agent directives |
| **Complexity** | L — the theory exists in wiki pages, needs formalization |

---

### Epic C: Agent Compliance Framework

> [!warning] Enforcement Gap — How to Make Agents Actually Follow This
>
> The entire initiative is pointless if agents continue to ignore the methodology. This epic turns theory into enforcement.

#### Gap C1: No CLAUDE.md Structural Patterns

| Aspect | Details |
|--------|---------|
| **Current state** | The wiki's CLAUDE.md is ~200 lines of flat prose with minimal structure. OpenArms AGENTS.md is ~400 lines with better structure (sacrosanct section, learnings, boundaries) but discovered empirically, never formalized. |
| **Required state** | A documented catalog of CLAUDE.md structural patterns that improve agent compliance: progressive disclosure (most important rules first), hard vs soft rule separation, ALLOWED/FORBIDDEN lists, command checkpoints, section dividers, nesting techniques, anchor patterns. WITH evidence of what works and what doesn't. |
| **Impact** | This is the highest-leverage gap. How instructions are STRUCTURED determines whether agents follow them. Currently each project discovers these patterns independently. |
| **Affected scope** | Wiki methodology pages (patterns), CLAUDE.md files across all projects |
| **Complexity** | L — requires empirical research + pattern extraction from OpenArms experience |

#### Gap C2: No Enforcement Hook Patterns

| Aspect | Details |
|--------|---------|
| **Current state** | OpenArms has 4 hooks (pre-bash, pre-write, post-write, post-compact). These are project-specific shell scripts. No reusable patterns or generic implementations. |
| **Required state** | A catalog of enforcement hook patterns: what each hook type prevents, when to use it, generic implementation templates, configuration for different stacks. Projects can adopt hooks from the catalog instead of building from scratch. |
| **Impact** | Without reusable hooks, infrastructure enforcement stays an OpenArms-only capability. Other projects fall back to instruction-based enforcement (75% failure rate). |
| **Affected scope** | Wiki patterns/lessons pages, example hook implementations, CLAUDE.md configuration guidance |
| **Complexity** | M — extracting patterns from OpenArms hooks is straightforward; making them generic requires abstraction |

#### Gap C3: No Methodology Compliance Validation

| Aspect | Details |
|--------|---------|
| **Current state** | `pipeline post` validates page quality (frontmatter, sections, relationships). No validation of methodology compliance (did the agent follow the right model? did it produce required artifacts per stage? did it skip stages?). |
| **Required state** | Validation tooling that checks: model was selected correctly for task type, each stage produced required artifacts, no forbidden artifacts exist, dependencies were respected, stage sequence was followed. |
| **Impact** | No way to detect methodology violations after the fact. Compliance is invisible. |
| **Affected scope** | tools/ (new or extended validation), config/ (validation rules per model) |
| **Complexity** | L — depends on artifact type system and methodology engine existing first |

#### Gap C4: No Skill Injection Patterns

| Aspect | Details |
|--------|---------|
| **Current state** | OpenArms has skill-stage-mapping.yaml (3 layers, restrictions). The wiki has skills loaded globally with no stage-awareness. |
| **Required state** | A generic skill injection pattern: which skills are recommended/mandatory/blocked per stage, per role, per domain. Portable across projects. |
| **Impact** | Without stage-aware skill injection, agents use wrong skills at wrong times (brainstorming during test stage, TDD during document stage). |
| **Affected scope** | Skills architecture, methodology engine, CLAUDE.md patterns |
| **Complexity** | M — the pattern exists in OpenArms, needs generalization |

#### Gap C5: No Agent Compliance Reporting

| Aspect | Details |
|--------|---------|
| **Current state** | OpenArms has completion logs (write-completion-log.cjs) and concern logging (record-concern.cjs). The wiki has session logs in wiki/log/ but no compliance analysis. |
| **Required state** | Post-session compliance report: which methodology model was used, which stages were executed, which artifacts were produced, which violations occurred, compliance score. Feeds back into methodology evolution. |
| **Impact** | Without compliance reporting, methodology improvements are based on anecdotes, not data. The evolution protocol described in methodology.yaml can't function without evidence. |
| **Affected scope** | tools/ (new reporting), wiki/log/ (structured compliance logs) |
| **Complexity** | M — depends on methodology engine and validation existing first |

---

### Epic D: Standards-by-Example

> [!warning] Credibility Gap — Standards That Don't Demonstrate Themselves Are Ignored
>
> Per the lesson "Standards Must Preach by Example" — every standard must ship with an annotated exemplar that passes its own rules. Currently most standards describe but don't demonstrate.

#### Gap D1: Missing Exemplars for 9 Page Types

| Aspect | Details |
|--------|---------|
| **Current state** | Gold-standard exemplars exist for 5 types (concept, source-synthesis, lesson, pattern, decision) in model-llm-wiki-standards.md. No exemplars for: comparison, reference, deep-dive, domain-overview, evolution, learning-path, epic, task, note. |
| **Required state** | Every page type that agents create has a gold-standard exemplar page in the wiki, referenced from the standards page. |
| **Impact** | Agents creating comparison or deep-dive pages have no model to follow. Quality is inconsistent. |
| **Affected scope** | Wiki pages (new exemplars), model-llm-wiki-standards.md (references to new exemplars) |
| **Complexity** | L — some exemplars already exist in the wiki but aren't designated as gold standard |

#### Gap D2: Exemplars Are Not Annotated

| Aspect | Details |
|--------|---------|
| **Current state** | model-llm-wiki-standards.md points to exemplar pages and describes what makes them good in separate prose. The exemplar pages themselves don't contain annotations explaining their structural choices. |
| **Required state** | Annotated exemplars: each exemplar includes inline annotations (comments or a companion guide) explaining WHY each section is structured the way it is, WHY specific callout types were chosen, WHY the evidence depth is what it is. The exemplar TEACHES, not just demonstrates. |
| **Impact** | Agents can copy exemplar structure but don't understand the reasoning. When they encounter novel situations, they can't adapt. |
| **Affected scope** | Exemplar pages (annotations), standards pages (annotation methodology) |
| **Complexity** | M — annotating existing strong pages is moderate; creating annotation methodology is harder |

#### Gap D3: Methodology Standards Page Is Thin

| Aspect | Details |
|--------|---------|
| **Current state** | model-methodology-standards.md is at "seed" maturity — the weakest of all standards pages. It has execution examples and checklists but lacks: recovery procedures, failure rate data, compliance metrics, annotated methodology.yaml example. |
| **Required state** | Mature standards page with: gold-standard execution examples for every model (not just feature-development), recovery procedures when gates fail, per-model compliance checklist, annotated methodology.yaml showing what good configuration looks like. |
| **Impact** | The methodology model's own standards page doesn't meet the quality bar of other standards pages. This undermines credibility. |
| **Affected scope** | wiki/spine/model-methodology-standards.md |
| **Complexity** | M — content exists across wiki pages and OpenArms learnings, needs consolidation |

#### Gap D4: No Self-Validation Loop

| Aspect | Details |
|--------|---------|
| **Current state** | The lesson "Standards Must Preach by Example" exists but there's no automated check that standards pages pass their own rules. |
| **Required state** | Validation rule: for every standards page, check that referenced exemplars exist and meet the quality criteria defined in the standards page itself. A standards page that references a non-existent exemplar or an exemplar that fails its own rules should fail validation. |
| **Impact** | Standards can drift from their own exemplars. The self-referential integrity test from the lesson is manual, not automated. |
| **Affected scope** | tools/validate.py or tools/lint.py (new check) |
| **Complexity** | S — straightforward validation rule once the exemplar system is defined |

---

### Epic Dependency Graph

> [!abstract] Epic Ordering and Dependencies
>
> ```
> Epic A: Artifact Type System (FOUNDATION)
>   ├── Epic B: Portable Methodology Engine (DEPENDS ON A)
>   │     └── needs artifact type definitions to specify per-model chains
>   ├── Epic C: Agent Compliance Framework (DEPENDS ON A, partially on B)
>   │     └── needs artifact types for validation, engine for model selection
>   └── Epic D: Standards-by-Example (DEPENDS ON A, partially on B and C)
>         └── needs artifact types to know what needs exemplars, engine for config examples
> ```
>
> **Critical path:** A → B → C → D (though B, C, D have independent modules that can parallel)

### Complexity and Effort Assessment

> [!info] Effort Summary
>
> | Epic | Gaps | Max Complexity | Estimate | Dependencies |
> |------|------|---------------|----------|-------------|
> | A: Artifact Type System | 5 gaps (A1-A5) | XL (artifact chain mapping) | XL | None — foundation |
> | B: Portable Methodology Engine | 3 gaps (B1-B3) | XL (generic methodology.yaml) | XL | Depends on A |
> | C: Agent Compliance Framework | 5 gaps (C1-C5) | L (CLAUDE.md patterns) | L | Depends on A, partially B |
> | D: Standards-by-Example | 4 gaps (D1-D4) | M (annotation methodology) | L | Depends on A, partially B+C |
>
> **Total initiative: XL — multiple epics, each with multiple modules, spanning the entire ecosystem.**

## Open Questions

> [!question] Should domain profiles be defined in the wiki (authoritative) or in each consumer project (local)? (Requires: design decision during Epic B)

> [!question] What is the minimum enforcement infrastructure for a project that doesn't have a harness like OpenArms? (Requires: analysis during Epic C — hooks + CLAUDE.md may be sufficient without scripts)

> [!question] Should annotated exemplars be inline in the exemplar page or in a separate companion document? (Requires: design decision during Epic D)

> [!question] How do we handle methodology evolution — when the wiki updates its methodology, how do consumer projects get notified and updated? (Requires: design decision during Epic B — relates to export/sync)

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **What principle applies?** | [[Principle: Right Process for Right Context — The Goldilocks Imperative]] |
> | **What is my identity?** | [[Project Self-Identification Protocol — The Goldilocks Framework]] |
> | **System map** | [[Methodology System Map]] |

## Relationships

- BUILDS ON: [[Methodology Standards Initiative — Infrastructure Analysis]]
- FEEDS INTO: [[Methodology Framework]]
- FEEDS INTO: [[Model: Methodology]]
- FEEDS INTO: [[Methodology Standards — What Good Execution Looks Like]]
- RELATES TO: [[Standards Must Preach by Example]]
- RELATES TO: [[Models Are Systems, Not Documents]]
- RELATES TO: [[Plan Execute Review Cycle]]
- ENABLES: [[Model: Quality and Failure Prevention]]
- ENABLES: [[Model: Skills, Commands, and Hooks]]

## Backlinks

[[Methodology Standards Initiative — Infrastructure Analysis]]
[[Methodology Framework]]
[[Model: Methodology]]
[[Methodology Standards — What Good Execution Looks Like]]
[[Standards Must Preach by Example]]
[[Models Are Systems, Not Documents]]
[[Plan Execute Review Cycle]]
[[Model: Quality and Failure Prevention]]
[[Model: Skills, Commands, and Hooks]]
[[Agent Compliance Framework]]
[[Artifact Type System]]
[[E003 Artifact Type System — Requirements Spec]]
[[Methodology Standards Initiative — Honest Assessment]]
[[Portable Methodology Engine]]
