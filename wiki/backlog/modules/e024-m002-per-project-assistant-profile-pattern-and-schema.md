---
title: "E024-M002 — Per-Project Assistant Profile Pattern + Schema (the foundational module)"
type: module
domain: backlog
status: draft
priority: P1
task_type: module
current_stage: document
readiness: 30
progress: 0
stages_completed: []
artifacts:
  - wiki/patterns/01_drafts/per-project-assistant-profile-pattern-tailored-config-to-spawn-ecosystem-runtimes.md
epic: "E024"
depends_on: []
confidence: high
created: 2026-05-09
updated: "2026-05-09"
sources:
  - id: epic-e024
    type: wiki
    file: wiki/backlog/epics/milestone-v2/e024-per-project-assistant-configurations-to-capture-programmatic-credit-and-enable-ecosystem-spawn.md
    description: "Parent Epic E024"
  - id: profile-pattern
    type: wiki
    file: wiki/patterns/01_drafts/per-project-assistant-profile-pattern-tailored-config-to-spawn-ecosystem-runtimes.md
    description: "Profile pattern page authored this turn — module finalizes its schema"
tags: [module, "E024-M002", per-project-assistant, profile-schema, pattern, foundation, "2026-05-09", "draft"]
---

# E024-M002 — Per-Project Assistant Profile Pattern + Schema

## Summary

Foundational module of E024 that finalizes the Per-Project Assistant Profile pattern + formal schema. Produces the pattern page (already drafted this turn), a YAML schema definition extending `wiki/config/wiki-schema.yaml` or living as `wiki/config/assistant-profile-schema.yaml`, a profile template at `wiki/config/templates/assistant-profile.md` (or equivalent), and validator integration via `pipeline post`. Other modules (M003-M006) consume the schema this module finalizes — schema design must be locked before profile authoring proceeds.

## Tasks

| Task | Title | Readiness | Progress | Status |
|------|-------|-----------|----------|--------|
| T071 | Author Profile schema formal definition (YAML schema for the 6 sections) | 40% | 0% | draft |
| T072 | Author profile template at `wiki/config/templates/assistant-profile.md` | 20% | 0% | draft |
| T073 | Extend `pipeline post` to validate Profile schema | 10% | 0% | draft |
| T074 | Document schema versioning policy + migration path | 10% | 0% | draft |

## Dependencies

- (none blocking)
- The pattern page [[per-project-assistant-profile-pattern-tailored-config-to-spawn-ecosystem-runtimes]] is the design artifact this module formalizes into schema

## Done When

- [ ] All 4 child tasks at status: done
- [ ] `wiki/config/assistant-profile-schema.yaml` (or equivalent) exists with formal field definitions
- [ ] Template at `wiki/config/templates/assistant-profile.md` exists
- [ ] `.venv/bin/python -m tools.pipeline post` validates an example Profile correctly
- [ ] Operator confirms schema covers the operator-stated "high quality definitions and features" bar

## Impediments

- (none active)

## Relationships

- PART OF: [[e024-per-project-assistant-configurations-to-capture-programmatic-credit-and-enable-ecosystem-spawn|E024 — Per-Project Assistant Configurations]]
- BUILDS ON: [[per-project-assistant-profile-pattern-tailored-config-to-spawn-ecosystem-runtimes|Pattern — Per-Project Assistant Profile]]

## Backlinks

[[E024 — Per-Project Assistant Configurations]]
[[Pattern — Per-Project Assistant Profile]]
