---
title: "Ecosystem Integration Interfaces"
type: epic
domain: backlog
status: draft
priority: P2
task_type: epic
current_stage: document
readiness: 15
stages_completed: [document]
artifacts:
  - wiki/domains/devops/four-project-ecosystem.md
  - [[Adoption Guide — How to Use This Wiki's Standards]]
confidence: high
created: 2026-04-09
updated: 2026-04-09
sources: []
tags: [ecosystem, integration, openfleet, openarms, aicp, export]
---

# Ecosystem Integration Interfaces

## Summary

Make the wiki's knowledge and methodology consumable by each sister project through their preferred interface. OpenFleet needs LightRAG-compatible exports. AICP needs routing profiles. OpenArms needs the methodology.yaml model. devops-control-plane needs the immune system rules in a shareable format.

## Goals

- Export profiles for each project (openfleet, AICP, OpenArms, devops-control-plane)
- OpenArms methodology transfer (validated — they already adopted it)
- OpenFleet immune system rules as a shared YAML module
- Wiki MCP tools accessible from sister projects via mcporter
- LightRAG activation path when wiki reaches 200 pages

## Done When

- [ ] `tools/export.py openfleet` produces LightRAG-compatible output
- [ ] `tools/export.py openarms` produces methodology.yaml + agent-directive
- [ ] OpenFleet immune system rules extracted as standalone module
- [ ] At least 1 sister project consuming wiki knowledge via MCP or export
- [ ] Integration documented as wiki pages

### How This Connects — Navigate From Here

> [!abstract] From This Epic → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **Goldilocks** | [[Project Self-Identification Protocol — The Goldilocks Framework]] |
> | **System map** | [[Methodology System Map]] |

## Relationships

- BUILDS ON: [[Four-Project Ecosystem]]
- ENABLES: OpenFleet, AICP, OpenArms, devops-control-plane
- RELATES TO: [[Adoption Guide — How to Use This Wiki's Standards]]
- RELATES TO: [[Decision: Wiki-First with LightRAG Upgrade Path]]

## Backlinks

[[Four-Project Ecosystem]]
[[OpenFleet]]
[[AICP]]
[[OpenArms]]
[[devops-control-plane]]
[[Adoption Guide — How to Use This Wiki's Standards]]
[[Decision: Wiki-First with LightRAG Upgrade Path]]
