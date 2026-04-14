---
title: Agent Compliance Framework
aliases:
  - "Agent Compliance Framework"
type: epic
domain: backlog
status: in-progress
priority: P0
task_type: epic
current_stage: document
readiness: 55
progress: 35
stages_completed:
  - "document"
  - "design"
artifacts:
  - "wiki/patterns/claude-md-structural-patterns.md"
  - "wiki/patterns/enforcement-hook-patterns.md"
  - "wiki/patterns/stage-aware-skill-injection.md"
  - "wiki/lessons/infrastructure-enforcement-proves-instructions-fail.md"
  - "wiki/lessons/agent-failure-taxonomy-six-classes-of-behavioral-failure.md"
  - "wiki/lessons/context-compaction-is-a-reset-event.md"
  - "wiki/lessons/enforcement-must-be-mindful-hard-blocks-need-justified-bypass.md"
  - "wiki/lessons/structured-context-is-proto-programming-for-ai-agents.md"
  - "wiki/lessons/harness-ownership-converges-independently-across-projects.md"
  - "wiki/patterns/three-lines-of-defense-immune-system-for-agent-quality.md"
  - "wiki/patterns/harness-owned-loop-deterministic-agent-execution.md"
  - "wiki/patterns/contribution-gating-cross-agent-inputs-before-work.md"
  - "wiki/patterns/tier-based-context-depth-trust-earned-through-approval-rates.md"
  - "wiki/patterns/validation-matrix-test-suite-for-context-injection.md"
  - "wiki/comparisons/openarms-vs-openfleet-enforcement.md"
  - "wiki/sources/src-openarms-v10-enforcement.md"
  - "wiki/sources/src-openfleet-fleet-architecture.md"
  - "CLAUDE.md"
confidence: high
created: 2026-04-11
updated: 2026-04-12
depends_on:
  - "E003"
  - "E004"
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

### How This Connects — Navigate From Here

> [!abstract] From This Epic → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **Goldilocks** | [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]] |
> | **System map** | [[methodology-system-map|Methodology System Map]] |

## Relationships

- DEPENDS ON: [[[[E003-artifact-type-system|Artifact Type System]] (E003)]]
- DEPENDS ON: [[[[E004-portable-methodology-engine|Portable Methodology Engine]] (E004)]]
- BUILDS ON: [[methodology-standards-initiative-infrastructure|Methodology Standards Initiative — Infrastructure Analysis]]
- BUILDS ON: [[methodology-standards-initiative-gaps|Methodology Standards Initiative — Gap Analysis]]
- IMPLEMENTS: [[model-quality-failure-prevention|Model — Quality and Failure Prevention]]
- IMPLEMENTS: [[model-skills-commands-hooks|Model — Skills, Commands, and Hooks]]
- FEEDS INTO: [[model-claude-code|Model — Claude Code]]
- RELATES TO: [[never-skip-stages-even-when-told-to-continue|Never Skip Stages Even When Told to Continue]]
- RELATES TO: [[always-plan-before-executing|Always Plan Before Executing]]
- RELATES TO: [[plan-execute-review-cycle|Plan Execute Review Cycle]]

## Backlinks

[[E003-artifact-type-system|Artifact Type System]]
[[E004-portable-methodology-engine|Portable Methodology Engine]]
[[methodology-standards-initiative-infrastructure|Methodology Standards Initiative — Infrastructure Analysis]]
[[methodology-standards-initiative-gaps|Methodology Standards Initiative — Gap Analysis]]
[[model-quality-failure-prevention|Model — Quality and Failure Prevention]]
[[model-skills-commands-hooks|Model — Skills, Commands, and Hooks]]
[[model-claude-code|Model — Claude Code]]
[[never-skip-stages-even-when-told-to-continue|Never Skip Stages Even When Told to Continue]]
[[always-plan-before-executing|Always Plan Before Executing]]
[[plan-execute-review-cycle|Plan Execute Review Cycle]]
[[e003-artifact-type-system-design|E003 Artifact Type System — Design Document]]
