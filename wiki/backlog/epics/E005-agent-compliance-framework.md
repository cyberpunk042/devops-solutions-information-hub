---
title: "Agent Compliance Framework"
type: epic
domain: backlog
status: in-progress
priority: P0
task_type: epic
current_stage: document
readiness: 30
stages_completed: [document]
artifacts:
  - wiki/patterns/claude-md-structural-patterns.md
  - wiki/patterns/enforcement-hook-patterns.md
  - wiki/patterns/stage-aware-skill-injection.md
  - CLAUDE.md
confidence: high
created: 2026-04-11
updated: 2026-04-11
depends_on: [E003, E004]
sources:
  - id: operator-directive
    type: file
    file: raw/notes/2026-04-11-methodology-standards-directive.md
tags: [methodology, agent-compliance, enforcement, hooks, claude-md, skills, validation]
---

# Agent Compliance Framework

## Summary

Turn methodology theory into agent enforcement. Document and productize the structural patterns that make agents actually follow methodology: CLAUDE.md structural patterns, enforcement hooks, stage-aware skill injection, methodology compliance validation, and compliance reporting. The research wiki becomes the laboratory where enforcement patterns are proven, then exported to consumer projects. This epic addresses the core operator problem: "the AI keep ignoring in certain cases even completely the directives given from the methodology."

## Goals

- Document CLAUDE.md structural patterns that improve compliance: progressive disclosure, hard vs soft rule separation, ALLOWED/FORBIDDEN lists, command checkpoints, section dividers, nesting, anchor patterns
- Extract reusable enforcement hook patterns from OpenArms (pre-bash, pre-write, post-write, post-compact)
- Define stage-aware skill injection patterns: which skills recommended/mandatory/blocked per stage, per role, per domain
- Build methodology compliance validation: check that agents followed the right model, produced required artifacts, respected stage boundaries
- Create compliance reporting: post-session analysis showing model used, stages executed, artifacts produced, violations detected
- Test enforcement patterns in the research wiki itself (eat our own cooking)
- Publish enforcement pattern catalog for consumer projects

## Done When

- [ ] CLAUDE.md structural patterns documented as wiki pages (patterns, with evidence)
- [ ] Enforcement hook patterns extracted, generalized, and documented
- [ ] Skill injection pattern formalized and documented
- [ ] Methodology compliance validation exists in tools/ (extends or complements pipeline post)
- [ ] Compliance reporting generates structured output after sessions
- [ ] Research wiki's own CLAUDE.md restructured using discovered patterns
- [ ] At least one consumer project (OpenArms) validates patterns work in practice
- [ ] Enforcement pattern catalog wiki page exists for consumer adoption
- [ ] All new pages pass validation with 0 errors

## Dependencies

- E003 (Artifact Type System) — needs artifact type definitions for validation
- E004 (Portable Methodology Engine) — needs methodology engine for model selection validation

## Relationships

- DEPENDS ON: [[Epic: Artifact Type System]] (E003)
- DEPENDS ON: [[Epic: Portable Methodology Engine]] (E004)
- BUILDS ON: [[Methodology Standards Initiative — Infrastructure Analysis]]
- BUILDS ON: [[Methodology Standards Initiative — Gap Analysis]]
- IMPLEMENTS: [[Model: Quality and Failure Prevention]]
- IMPLEMENTS: [[Model: Skills, Commands, and Hooks]]
- FEEDS INTO: [[Model: Claude Code]]
- RELATES TO: [[Never Skip Stages Even When Told to Continue]]
- RELATES TO: [[Always Plan Before Executing]]
- RELATES TO: [[Plan-Execute-Review Cycle]]

## Backlinks

[[Epic: Artifact Type System]]
[[Epic: Portable Methodology Engine]]
[[Methodology Standards Initiative — Infrastructure Analysis]]
[[Methodology Standards Initiative — Gap Analysis]]
[[Model: Quality and Failure Prevention]]
[[Model: Skills, Commands, and Hooks]]
[[Model: Claude Code]]
[[Never Skip Stages Even When Told to Continue]]
[[Always Plan Before Executing]]
[[Plan-Execute-Review Cycle]]
