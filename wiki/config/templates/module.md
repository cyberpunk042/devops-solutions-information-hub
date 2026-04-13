---
title: "{{title}}"
type: module
domain: backlog
status: draft
priority: {{priority}}
task_type: module
current_stage: document
readiness: 0               # 0-100: derived from child tasks. Is this module DEFINED enough?
progress: 0                 # 0-100: derived from child tasks. How far is the WORK?
stages_completed: []
artifacts: []
epic: "{{epic_id}}"
depends_on: []
confidence: high
created: {{date}}
updated: {{date}}
sources: []
tags: []
---

# {{title}}

<!-- READINESS vs PROGRESS for modules:
     - readiness = AVERAGE of child task readiness (derived, never manual)
     - progress = AVERAGE of child task progress (derived, never manual)
     - Module readiness gates its children: if module design isn't done (readiness < 50),
       child tasks shouldn't start implementation
     See: wiki/domains/cross-domain/readiness-vs-progress.md -->

## Summary

<!-- 2-3 sentences: what this module delivers within its parent epic.
     A module is a scoped subsystem — independently reviewable with its own design. -->

## Goals

<!-- Bulleted list of module-scoped deliverables. Subset of epic goals.
     Each goal is specific and verifiable. -->

## Done When

<!-- Checklist. Module is done when ALL child tasks are done AND these criteria met.
     Format: - [ ] Specific verifiable statement
     99→100: requires human review (status ceiling = review, not done). -->

- [ ] All child tasks at status: done
- [ ] {{module_specific_criterion}}

## Tasks

<!-- List of child tasks (created separately in wiki/backlog/tasks/).
     Format: | Task ID | Title | Readiness | Progress | Status |
     Track both dimensions for each child. -->

| Task | Title | Readiness | Progress | Status |
|------|-------|-----------|----------|--------|
| {{task_id}} | {{task_title}} | 0% | 0% | draft |

## Impediments

<!-- Active blockers. Remove when resolved.
     Types: technical, dependency, decision, environment, clarification, scope, external, quality -->

## Relationships

- PART OF: [[{{epic_title}}]]
