---
title: Portable Methodology Engine
aliases:
  - "Portable Methodology Engine"
type: epic
domain: backlog
status: in-progress
priority: P0
task_type: epic
current_stage: document
readiness: 15
stages_completed:
  - "document"
artifacts:
  - "wiki/config/methodology.yaml"
  - "wiki/config/domain-profiles/typescript.yaml"
  - "wiki/config/domain-profiles/python-wiki.yaml"
  - "wiki/config/domain-profiles/infrastructure.yaml"
  - "wiki/config/artifact-types.yaml"
  - "wiki/config/export-profiles.yaml"
  - "wiki/domains/cross-domain/model-composition-rules.md"
  - "wiki/spine/references/methodology-adoption-guide.md"
  - "wiki/domains/cross-domain/methodology-evolution-protocol.md"
confidence: high
created: 2026-04-11
updated: 2026-04-11
depends_on:
  - "E003"
sources:
  - id: operator-directive
    type: file
    file: raw/notes/2026-04-11-methodology-standards-directive.md
tags: [methodology, methodology-engine, portable, ecosystem, configuration]
---

# Portable Methodology Engine

## Summary

Create a generic, parameterizable methodology configuration system that the wiki produces and consumer projects adopt. Not hardcoded to any technology stack. Includes model definitions, stage specifications, artifact chains, execution modes, end conditions, and domain profiles. Projects import the base methodology and layer project-specific overrides. This replaces the current state where every project builds its own methodology from scratch (as OpenArms did with its 753-line hardcoded methodology.yaml).

## Goals

- Design a generic methodology.yaml schema: models, stages, artifacts, gates, protocols, domain profiles — all parameterizable
- Create the canonical methodology.yaml as the wiki's authoritative export
- Define domain profiles for major project types (TypeScript/Node, Python, infrastructure/IaC, knowledge/wiki)
- Define model composition rules: how models nest, how parallel tracks coexist, how conflicts resolve
- Create an adoption guide: step-by-step for projects to import and configure the methodology
- Define the methodology evolution protocol: how wiki updates propagate to consumers
- Create export tooling to publish methodology config alongside wiki content exports
- Ensure OpenArms's methodology.yaml can be derived from the generic base + OpenArms-specific overrides

## Done When

- [ ] Generic methodology schema defined and documented as wiki page + config
- [ ] Canonical methodology.yaml exists in config/ with all 9+ models defined generically
- [ ] Domain profiles exist for at least 3 domains (TypeScript, Python/wiki, infrastructure)
- [ ] OpenArms methodology.yaml can be expressed as: generic base + overrides (validated)
- [ ] Model composition rules formalized and documented
- [ ] Adoption guide wiki page exists with per-domain examples
- [ ] Methodology evolution protocol defined (how updates propagate)
- [ ] Export tooling updated to include methodology config
- [ ] All new pages pass validation with 0 errors

## Dependencies

- E003 (Artifact Type System) — needs artifact type definitions to specify per-model artifact chains

### How This Connects — Navigate From Here

> [!abstract] From This Epic → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **Goldilocks** | [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]] |
> | **System map** | [[methodology-system-map|Methodology System Map]] |

## Relationships

- DEPENDS ON: [[[[E003-artifact-type-system|Artifact Type System]] (E003)]]
- ENABLES: [[[[E005-agent-compliance-framework|Agent Compliance Framework]] (E005)]]
- BUILDS ON: [[methodology-standards-initiative-infrastructure|Methodology Standards Initiative — Infrastructure Analysis]]
- BUILDS ON: [[methodology-standards-initiative-gaps|Methodology Standards Initiative — Gap Analysis]]
- IMPLEMENTS: [[methodology-framework|Methodology Framework]]
- FEEDS INTO: [[model-methodology|Model — Methodology]]
- FEEDS INTO: [[model-ecosystem|Model — Ecosystem Architecture]]
- RELATES TO: [[four-project-ecosystem|Four-Project Ecosystem]]

## Backlinks

[[E003-artifact-type-system|Artifact Type System]]
[[E005-agent-compliance-framework|Agent Compliance Framework]]
[[methodology-standards-initiative-infrastructure|Methodology Standards Initiative — Infrastructure Analysis]]
[[methodology-standards-initiative-gaps|Methodology Standards Initiative — Gap Analysis]]
[[methodology-framework|Methodology Framework]]
[[model-methodology|Model — Methodology]]
[[model-ecosystem|Model — Ecosystem Architecture]]
[[four-project-ecosystem|Four-Project Ecosystem]]
[[e003-artifact-type-system-design|E003 Artifact Type System — Design Document]]
