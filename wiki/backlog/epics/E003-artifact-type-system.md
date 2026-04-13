---
title: "Artifact Type System"
type: epic
domain: backlog
status: active
priority: P0
task_type: epic
current_stage: document
readiness: 55
progress: 40
stages_completed: [document, design, scaffold]
artifacts:
  - wiki/domains/cross-domain/methodology-standards-initiative-infrastructure.md
  - wiki/domains/cross-domain/methodology-standards-initiative-gaps.md
  - wiki/domains/cross-domain/e003-artifact-type-system-requirements.md
  - wiki/domains/cross-domain/e003-artifact-type-system-design.md
  - wiki/config/artifact-types.yaml
  - wiki/config/templates/concept.md
  - wiki/config/templates/source-synthesis.md
  - wiki/config/templates/comparison.md
  - wiki/config/templates/reference.md
  - wiki/config/templates/deep-dive.md
  - wiki/config/templates/epic.md
  - wiki/config/templates/module.md
  - wiki/config/templates/task.md
  - wiki/config/templates/note.md
  - wiki/config/templates/operations-plan.md
  - wiki/config/templates/methodology/requirements-spec.md
  - wiki/config/templates/methodology/infrastructure-analysis.md
  - wiki/config/templates/methodology/gap-analysis.md
  - wiki/config/templates/methodology/design-plan.md
  - wiki/config/templates/methodology/tech-spec.md
  - wiki/config/templates/methodology/test-plan.md
  - wiki/config/methodology.yaml
  - wiki/config/domain-profiles/typescript.yaml
  - wiki/config/domain-profiles/python-wiki.yaml
  - wiki/config/domain-profiles/infrastructure.yaml
  - wiki/domains/cross-domain/artifact-chains-by-model.md
  - wiki/config/templates/milestone.md
  - wiki/config/templates/evolution.md
  - wiki/config/templates/learning-path.md
  - wiki/spine/frontmatter-field-reference.md
  - wiki/domains/cross-domain/sdlc-customization-framework.md
  - wiki/domains/cross-domain/readiness-vs-progress.md
  - wiki/domains/cross-domain/three-pm-levels.md
  - wiki/decisions/when-to-use-milestone-vs-epic-vs-module-vs-task.md
  - raw/notes/2026-04-11-methodology-standards-directive.md
confidence: high
created: 2026-04-11
updated: 2026-04-12
sources:
  - id: operator-directive
    type: file
    file: raw/notes/2026-04-11-methodology-standards-directive.md
tags: [methodology, artifact-types, templates, exemplars, type-system, foundation]
---

# Artifact Type System

## Summary

Define every document and artifact type in the methodology with: formal type definition, template, validation rules, and domain-specific variations. Map the complete artifact chain for every methodology model — from model selection through stage sequence to per-stage artifacts with dependencies. This is the FOUNDATION epic — everything in Epics B, C, and D depends on having a complete, formal artifact type system.

## Goals

- Define a generic artifact type taxonomy: wiki page subtypes, design documents, operations checklists, analysis reports, configurations, test evidence, compliance reports
- Create templates for all 8 page types currently missing templates (concept, source-synthesis, comparison, reference, deep-dive, epic, task, note)
- Formalize the operations plan vs design plan distinction as separate document types with separate templates
- Map the complete artifact chain for every methodology model (9 models × stages × artifacts × dependencies)
- Define domain-specific artifact variations (TypeScript project, Python project, wiki/knowledge, infrastructure)
- Create a machine-readable artifact type definition schema (wiki/config/artifact-types.yaml or extension to wiki-schema.yaml)
- Document the artifact chain as both wiki pages (human-readable) and config (machine-readable)

## Done When

- [ ] Artifact type taxonomy wiki page exists with formal definitions for every type
- [ ] Templates exist for all page types agents create (currently 8 missing)
- [ ] Operations plan and design plan are formally distinguished with separate templates
- [ ] Complete artifact chain documented for all 9 methodology models
- [ ] Domain-specific variations defined for at least 3 domains (TypeScript, Python/wiki, infrastructure)
- [ ] Machine-readable artifact type config exists in config/
- [ ] Existing wiki-schema.yaml extended or replaced to incorporate artifact types
- [ ] `pipeline post` validation updated to check artifact type compliance
- [ ] All new pages pass validation with 0 errors

## Dependencies

None — this is the foundation epic.

## Blocked By

Nothing. Can start immediately.

### How This Connects — Navigate From Here

> [!abstract] From This Epic → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **Goldilocks** | [[Project Self-Identification Protocol — The Goldilocks Framework]] |
> | **System map** | [[Methodology System Map]] |

## Relationships

- ENABLES: [[Portable Methodology Engine]] (E004)
- ENABLES: [[Agent Compliance Framework]] (E005)
- ENABLES: [[Standards-by-Example]] (E006)
- BUILDS ON: [[Methodology Standards Initiative — Infrastructure Analysis]]
- BUILDS ON: [[Methodology Standards Initiative — Gap Analysis]]
- IMPLEMENTS: [[Methodology Framework]]
- FEEDS INTO: [[Model: Methodology]]
- FEEDS INTO: [[LLM Wiki Standards — What Good Looks Like]]

## Backlinks

[[Portable Methodology Engine]]
[[Agent Compliance Framework]]
[[Standards-by-Example]]
[[Methodology Standards Initiative — Infrastructure Analysis]]
[[Methodology Standards Initiative — Gap Analysis]]
[[Methodology Framework]]
[[Model: Methodology]]
[[LLM Wiki Standards — What Good Looks Like]]
[[E003 Artifact Type System — Design Document]]
[[E003 Artifact Type System — Requirements Spec]]
[[Methodology Standards Initiative — Honest Assessment]]
[[SDLC Rules and Structure — Customizable Project Lifecycle]]
[[Wiki Gateway Tools — Unified Knowledge Interface]]
