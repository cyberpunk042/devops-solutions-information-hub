---
title: Decision — When to Use Milestone vs Epic vs Module vs Task
aliases:
  - "Decision — When to Use Milestone vs Epic vs Module vs Task"
  - "Decision: When to Use Milestone vs Epic vs Module vs Task"
type: decision
domain: cross-domain
layer: 6
status: synthesized
confidence: high
maturity: growing
derived_from:
  - "Backlog Hierarchy Rules"
  - "Readiness vs Progress — Two-Dimensional Work Tracking"
  - "SDLC Customization Framework — Phases, Scale, and Chain Selection"
reversibility: easy
created: 2026-04-12
updated: 2026-04-12
sources:
  - id: operator-directive
    type: directive
    file: raw/notes/2026-04-12-milestones-impediments-directive.md
    description: "Operator: 'its important to know when to chose what and when to chose what and in what order and for what reasons'"
  - id: openfleet-hierarchy
    type: observation
    file: raw/articles/openfleet-methodology-scan.md
    description: "OpenFleet Plane integration: cycles as milestones, modules as modules, issues as tasks"
  - id: openarms-backlog
    type: observation
    file: raw/articles/openarms-methodology-scan.md
    description: "OpenArms wiki backlog: epics/E00X.md, tasks/T00X.md, file-based hierarchy"
tags: [decision, hierarchy, milestone, epic, module, task, work-management, decomposition]
---

# Decision — When to Use Milestone vs Epic vs Module vs Task
## Summary

Use milestones for delivery coordination across epics, epics for strategic capabilities, modules for coherent subsystems, and tasks for atomic execution. The decision is based on three questions: how long will this take (duration), can it be independently reviewed (reviewability), and does it need its own design (design complexity). Wrong decomposition level causes either over-process (task treated as epic) or under-process (epic treated as task).

## Decision

> [!success] Hierarchy Level Selection
>
> | You have... | Duration | Design needed? | Review scope | → Use |
> |-------------|----------|---------------|-------------|-------|
> | Multiple epics that must ship together | Weeks-months | N/A (epics have their own) | Cross-epic coordination | **Milestone** |
> | A strategic capability requiring design + implementation | Weeks | Yes — full requirements + design | End-to-end acceptance criteria | **Epic** |
> | A coherent subsystem within an epic | Days | Yes — module-level design decisions | Independent subsystem review | **Module** |
> | A single-session piece of work | Hours | No — design decided at module/epic level | Self-contained verification | **Task** |
> | A known bug with a clear fix | Hours | No | Fix + test | **Task** (bug-fix model) |
> | An investigation with no implementation | Hours-days | No | Findings document | **Task** (research model) |
> | An emergency with a known solution | Minutes-hours | No | Fix + test only | **Task** (hotfix model) |

> [!warning] The Critical Decomposition Test
>
> **If a "task" needs both a design document AND implementation code, it's a MODULE.** Tasks inherit their design from the module level. A task that requires its own design stage means the decomposition was too coarse.
>
> **If an "epic" has no modules, it's either:** (a) a small epic where tasks report directly (OK for 3-5 tasks), or (b) the decomposition was too coarse and modules are implicit (refactor into explicit modules when task count exceeds 5).

## Alternatives

### Alternative 1: Flat task list (no hierarchy)

All work items at the same level — just a list of tasks.

> [!warning] Rejected: loses coordination and context
> Without epics, there's no acceptance criteria to verify end-to-end. Without modules, there's no design scope. Without milestones, there's no delivery coordination. Flat lists work for personal todo apps but not for multi-stage, multi-agent work.

### Alternative 2: Deep hierarchy (milestone → program → epic → feature → module → task → subtask)

7+ levels like enterprise PMOs use.

> [!warning] Rejected: over-process for current scale
> The current ecosystem (1 operator, 2-10 agents, 5 projects) doesn't need program/feature/subtask levels. 4 levels (milestone → epic → module → task) cover the full range from delivery targets to atomic work. Adding levels can happen when organizational complexity demands it.

### Alternative 3: Single-dimension tracking (readiness only, no separate progress)

OpenArms current model — single `readiness` field tracking both definition and execution.

> [!warning] Rejected: hides the failure mode
> A single field can't distinguish "not defined" from "defined but not built." Both show as "50%" but require completely different responses. OpenFleet's two-field model (`task_readiness` + `task_progress`) enables correct diagnosis. See [[readiness-vs-progress|Readiness vs Progress — Two-Dimensional Work Tracking]].

## Rationale

The 4-level hierarchy maps to natural work decomposition boundaries:

1. **Milestone = delivery event.** Multiple epics ship together. The milestone exists because epics A and B are independently valuable but must coordinate for a release. Without the milestone, coordination is implicit and fragile.

2. **Epic = strategic container.** It has its own acceptance criteria that ONLY make sense when ALL children complete. An epic that's 80% done is not 80% useful — it's 0% useful until the remaining 20% delivers the capability.

3. **Module = design boundary.** A module has its own design decisions. Tasks within the module inherit those decisions. This is the key distinction: modules have their OWN design stage, tasks do NOT.

4. **Task = execution boundary.** A task goes through stages (based on its methodology model), produces artifacts, and has a deterministic done state. Tasks are what agents actually execute.

**The impediment type system** adds a cross-cutting dimension: any level can be blocked, and the block has a TYPE (technical, dependency, decision, environment, clarification, scope, external, quality) that determines the correct response.

## Reversibility

Easy to reverse. Promoting a task to a module or demoting an epic to a task is a frontmatter change + decomposition/consolidation. The hierarchy is organizational, not structural — changing levels doesn't require code changes, only backlog reorganization.

## Dependencies

- [[backlog-hierarchy-rules|Backlog Hierarchy Rules]] — defines the 4-level hierarchy and 8 rules governing propagation
- [[readiness-vs-progress|Readiness vs Progress — Two-Dimensional Work Tracking]] — both fields tracked at every level
- [[three-pm-levels|Three PM Levels — Wiki to Fleet to Full Tool]] — PM level determines how hierarchy is enforced
- [[sdlc-customization-framework|SDLC Customization Framework — Phases, Scale, and Chain Selection]] — SDLC chain affects how many artifacts per level

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **What principle governs this?** | [[right-process-for-right-context-the-goldilocks-imperative|Principle — Right Process for Right Context — The Goldilocks Imperative]] |
> | **How does enforcement apply?** | [[infrastructure-over-instructions-for-process-enforcement|Principle — Infrastructure Over Instructions for Process Enforcement]] |
> | **What is my identity profile?** | [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]] |
> | **Where does this fit?** | [[methodology-system-map|Methodology System Map]] |

## Relationships

- DERIVED FROM: [[backlog-hierarchy-rules|Backlog Hierarchy Rules]]
- DERIVED FROM: [[readiness-vs-progress|Readiness vs Progress — Two-Dimensional Work Tracking]]
- DERIVED FROM: [[sdlc-customization-framework|SDLC Customization Framework — Phases, Scale, and Chain Selection]]
- RELATES TO: [[three-pm-levels|Three PM Levels — Wiki to Fleet to Full Tool]]
- RELATES TO: [[methodology-adoption-guide|Methodology Adoption Guide]]
- FEEDS INTO: [[model-methodology|Model — Methodology]]

## Backlinks

[[backlog-hierarchy-rules|Backlog Hierarchy Rules]]
[[readiness-vs-progress|Readiness vs Progress — Two-Dimensional Work Tracking]]
[[sdlc-customization-framework|SDLC Customization Framework — Phases, Scale, and Chain Selection]]
[[three-pm-levels|Three PM Levels — Wiki to Fleet to Full Tool]]
[[methodology-adoption-guide|Methodology Adoption Guide]]
[[model-methodology|Model — Methodology]]
