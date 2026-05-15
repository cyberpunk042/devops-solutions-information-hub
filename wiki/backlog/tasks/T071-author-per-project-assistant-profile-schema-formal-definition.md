---
title: "T071 — Author Per-Project Assistant Profile schema formal definition (YAML schema for the 6 sections)"
type: task
domain: backlog
status: draft
priority: P1
task_type: task
current_stage: document
readiness: 40
progress: 0
stages_completed: []
artifacts: []
estimate: M
epic: "E024"
module: "E024-M002"
depends_on: []
confidence: high
created: 2026-05-09
updated: "2026-05-09"
sources:
  - id: parent-module
    type: wiki
    file: wiki/backlog/modules/e024-m002-per-project-assistant-profile-pattern-and-schema.md
    description: "Parent module E024-M002 — this task delivers the schema definition that the module's other tasks build on"
  - id: pattern-page
    type: wiki
    file: wiki/patterns/01_drafts/per-project-assistant-profile-pattern-tailored-config-to-spawn-ecosystem-runtimes.md
    description: "Pattern page with the 6-section structure this task formalizes"
tags: [task, "T071", schema-design, yaml, per-project-assistant, "2026-05-09", "draft"]
---

# T071 — Author Per-Project Assistant Profile schema formal definition

## Summary

Formalize the 6-section Per-Project Assistant Profile schema (Identity · Knowledge Scope · Action Surface · Model Routing · Prompt Templates · Success Criteria) as a YAML schema definition at `wiki/config/assistant-profile-schema.yaml`. The schema must enumerate required fields, allowed types, validation rules, and versioning policy. Other tasks (T072 template, T073 validator) consume this schema.

## Done When

- [ ] `wiki/config/assistant-profile-schema.yaml` exists with formal field definitions for all 6 sections
- [ ] Schema explicitly lists required fields, optional fields, allowed enum values, type constraints
- [ ] Schema includes `profile_version` field for migration policy
- [ ] Schema supports runtime-agnostic `runtime_targets:` list (at minimum: openclaw, openarms, generic-agent-sdk, claude-code-cli-p)
- [ ] Schema is reviewable by `.venv/bin/python -c "import yaml; yaml.safe_load(open('wiki/config/assistant-profile-schema.yaml'))"` without error
- [ ] One example Profile (the /opt profile from T075) validates against this schema

## Relationships

- PART OF: [[e024-m002-per-project-assistant-profile-pattern-and-schema|E024-M002 — Profile Pattern + Schema]]
- IMPLEMENTS: [[per-project-assistant-profile-pattern-tailored-config-to-spawn-ecosystem-runtimes|Pattern — Per-Project Assistant Profile]]
- ENABLES: T072 (template), T073 (validator), T075 (/opt profile)

## Backlinks

[[E024-M002 — Profile Pattern + Schema]]
[[Pattern — Per-Project Assistant Profile]]
[[T072 (template)]]
[[T073 (validator)]]
[[T075 (/opt profile)]]
