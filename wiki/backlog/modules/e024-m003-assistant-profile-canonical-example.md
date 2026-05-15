---
title: "E024-M003 — this project Second-Brain Assistant Profile (the canonical tailored example)"
type: module
domain: backlog
status: draft
priority: P1
task_type: module
current_stage: document
readiness: 25
progress: 0
stages_completed: []
artifacts: []
epic: "E024"
depends_on:
  - E024-M002                            # needs the schema before authoring the instance
confidence: high
created: 2026-05-09
updated: "2026-05-09"
sources:
  - id: epic-e024
    type: wiki
    file: wiki/backlog/epics/milestone-v2/e024-per-project-assistant-configurations-to-capture-programmatic-credit-and-enable-ecosystem-spawn.md
    description: "Parent Epic E024"
  - id: operator-directive-2026-05-09
    type: directive
    file: raw/notes/2026-05-09-operator-directive-per-project-assistant-configs-spawn-openclaw-openarms-hermess-and-anthropic-programmatic-budget-policy-research.md
    description: "Operator: 'in the knowledge/information-hub we will have one taillored to the needs'"
tags: [module, "E024-M003", per-project-assistant, opt-second-brain, canonical-example, tailored-profile, "2026-05-09", "draft"]
---

# E024-M003 — this project Second-Brain Assistant Profile (the canonical tailored example)

## Summary

Author the this project (the research wiki) Assistant Profile — the tailored profile for THIS project — as the canonical example that demonstrates the Profile pattern by exemplary instance. Operator-stated 2026-05-09: *"in the knowledge/information-hub we will have one taillored to the needs"*. The profile captures this project's specific assistance needs: knowledge curation, methodology stewardship, source ingestion, lesson distillation, gateway-driven orientation, P4-compliant verification, sacrosanct-verbatim quoting. Once authored, the profile serves as the reference for sister-project profiles in M006 — each project's profile mirrors this project's structure, adapted to that project's needs.

## Tasks

| Task | Title | Readiness | Progress | Status |
|------|-------|-----------|----------|--------|
| T075 | Author this project (the research wiki) assistant profile per M002 schema | 30% | 0% | draft |
| T076 | Document this project profile success criteria + telemetry hooks | 20% | 0% | draft |
| T077 | Operator-review the profile for "high quality" bar adherence | 10% | 0% | draft |

## Dependencies

- [[e024-m002-per-project-assistant-profile-pattern-and-schema]] — schema must be locked before authoring this instance

## Done When

- [ ] All 3 child tasks at status: done
- [ ] `.assistant/profile.yaml` (or equivalent — TBD in M002) exists at this project repo root
- [ ] `.venv/bin/python -m tools.pipeline post` validates this project profile
- [ ] Profile contains all 6 sections (Identity · Knowledge Scope · Action Surface · Model Routing · Prompt Templates · Success Criteria)
- [ ] Operator confirms profile reflects this project's actual needs and the "high quality definitions and features" bar
- [ ] Profile is sufficient to spawn an instance via at least one spawn protocol from M004

## Impediments

- (none active until M002 completes)

## Relationships

- PART OF: [[e024-per-project-assistant-configurations-to-capture-programmatic-credit-and-enable-ecosystem-spawn|E024 — Per-Project Assistant Configurations]]
- DEPENDS ON: [[e024-m002-per-project-assistant-profile-pattern-and-schema|E024-M002 — Profile Pattern + Schema]]
- DEMONSTRATES: [[per-project-assistant-profile-pattern-tailored-config-to-spawn-ecosystem-runtimes|Pattern — Per-Project Assistant Profile]] by exemplary instance

## Backlinks

[[E024 — Per-Project Assistant Configurations]]
[[E024-M002 — Profile Pattern + Schema]]
[[Pattern — Per-Project Assistant Profile]]
