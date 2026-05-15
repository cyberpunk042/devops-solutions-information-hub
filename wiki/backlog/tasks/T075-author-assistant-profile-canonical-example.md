---
title: "T075 — Author this project Second-Brain Assistant Profile per M002 schema (canonical tailored example)"
type: task
domain: backlog
status: draft
priority: P1
task_type: task
current_stage: document
readiness: 30
progress: 0
stages_completed: []
artifacts: []
estimate: L
epic: "E024"
module: "E024-M003"
depends_on:
  - T071                                  # need the schema before authoring the instance
confidence: high
created: 2026-05-09
updated: "2026-05-09"
sources:
  - id: parent-module
    type: wiki
    file: wiki/backlog/modules/e024-m003-assistant-profile-canonical-example.md
    description: "Parent module E024-M003 — this project canonical example"
  - id: operator-directive-2026-05-09
    type: directive
    file: raw/notes/2026-05-09-operator-directive-per-project-assistant-configs-spawn-openclaw-openarms-hermess-and-anthropic-programmatic-budget-policy-research.md
    description: "Operator: 'in the knowledge/information-hub we will have one taillored to the needs'"
tags: [task, "T075", opt-second-brain, per-project-assistant-profile, canonical-example, "2026-05-09", "draft"]
---

# T075 — Author this project Second-Brain Assistant Profile

## Summary

Author the tailored profile for this project (the research wiki) (this project) at `.assistant/profile.yaml` (or path-TBD-by-T071) per the schema established in T071. The profile reflects this project's actual needs: knowledge curation, methodology stewardship, source ingestion, lesson distillation, gateway-driven orientation, P4 verification discipline, sacrosanct-verbatim quoting. Serves as the canonical reference for sister-project profiles (M006).

## Done When

- [ ] `.assistant/profile.yaml` exists at this project repo root (path per T071 outcome)
- [ ] Profile contains all 6 schema-required sections (Identity · Knowledge Scope · Action Surface · Model Routing · Prompt Templates · Success Criteria)
- [ ] Identity section: name=`assistant-profile`, project=`devops-solutions-information-hub`, owner=`operator`
- [ ] Knowledge Scope includes: `wiki/spine/`, `wiki/lessons/03_validated/`, `wiki/config/`, `raw/notes/`, MCP server `research-wiki`
- [ ] Action Surface allows: `wiki_search`, `wiki_read_page`, `wiki_log`, `wiki_gateway_orient`, `pipeline_post`; forbids `WebFetch` on corpus URLs, destructive git ops
- [ ] Prompt Templates honor sacrosanct verbatim quoting + behave-FROM-not-OVER doctrine
- [ ] Success Criteria includes: verbatim log entries per directive, monthly lesson promotions, 0 pipeline-post errors per session, target $30-50/month credit consumption
- [ ] `.venv/bin/python -m tools.pipeline post` returns 0 errors for the profile
- [ ] Operator confirms profile reflects this project's actual needs

## Relationships

- PART OF: [[e024-m003-assistant-profile-canonical-example|E024-M003 — this project Profile]]
- DEPENDS ON: [[T071-author-per-project-assistant-profile-schema-formal-definition|T071 — Profile Schema]]
- DEMONSTRATES: [[per-project-assistant-profile-pattern-tailored-config-to-spawn-ecosystem-runtimes|Pattern — Per-Project Assistant Profile]] by exemplary instance

## Backlinks

[[E024-M003 — this project Profile]]
[[T071 — Profile Schema]]
[[Pattern — Per-Project Assistant Profile]]
