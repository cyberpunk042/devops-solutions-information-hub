---
title: Backlog Hierarchy Rules
aliases:
  - "Backlog Hierarchy Rules"
type: concept
layer: 2
domain: devops
status: synthesized
confidence: authoritative
created: 2026-04-09
updated: 2026-04-12
maturity: growing
derived_from:
  - "Stage-Gate Methodology"
  - "Wiki Backlog Pattern"
sources:
  - id: src-openarms-methodology-yaml-full
    type: documentation
    file: raw/articles/openarms-methodology-yaml-full.md
    title: OpenArms Methodology YAML + Agent Directive — Full Reference
    ingested: 2026-04-09
  - id: src-openfleet-methodology-scan
    type: documentation
    file: raw/articles/openfleet-methodology-scan.md
    title: OpenFleet Methodology Scan — Deep Research Findings
    ingested: 2026-04-09
tags: [backlog, epic, module, task, hierarchy, readiness, status-propagation, wiki-backlog, openarms, openfleet, task-management, decomposition, upward-aggregation]
---

# Backlog Hierarchy Rules

## Summary

The Backlog Hierarchy Rules define the four-level MILESTONE → EPIC → MODULE → TASK structure used by the OpenArms project and mirrored in OpenFleet's Plane board. Eight rules govern how work is organized, how readiness propagates upward, how status flows upward, and when containers are considered done. The key operational principle: you work on TASKS, not epics or modules. To advance an epic, pick a task and complete its next stage. Epics are never manually marked done — they can reach a maximum of `review` status, requiring human confirmation before closure.

> [!info] Four-level hierarchy
>
> | Level | Role | Readiness | Status Ceiling |
> |-------|------|-----------|---------------|
> | **Milestone** | Delivery target — groups epics that ship together | AVERAGE of child epics (derived) | `review` (human confirmation) |
> | **Epic** | Strategic container — acceptance criteria, scope boundary | AVERAGE of all descendant tasks (derived, never manual) | `review` (human confirmation for `done`) |
> | **Module** | Scoped subsystem within an epic | AVERAGE of child tasks | `review` (human confirmation for `done`) |
> | **Task** | Atomic execution unit — stages, frontmatter, commits | Derived from stages_completed | `done` (automatic when all stages pass) |

## Key Insights

> [!warning] Work happens at tasks, not epics
> You never "work on an epic." You work on a task → child of module → child of epic. Epic = coordination artifact (acceptance criteria, scope). Task = execution artifact (stages, commits). To advance an epic, pick a task and complete its next stage.

> [!tip] Readiness propagation eliminates false completion signals
> Epic readiness = AVERAGE of children's readiness. Cannot be overridden manually. 9 tasks at 100% + 1 task at 0% = 90%, not 100%. An agent setting `readiness: 75` because "it feels done" is corrupting the signal.

**Status flows upward automatically.** Any child in-progress → parent in-progress. ALL children done → parent moves to `review` (never `done` — human confirmation required). No manual monitoring needed.

**"No tasks but not 100%" = create new tasks.** The correct response to incomplete readiness with no remaining tasks is decomposition was incomplete — create tasks to cover the gap. This is signal, not a bug.

**Epics staying in-progress for weeks is normal.** Consistent task completion = healthy. No task activity = stuck (watcher should surface it).

## Deep Analysis

### The Three Levels

#### Level 1: EPIC

An epic is a strategic container. It defines:
- A meaningful capability or deliverable at the product/system level
- Acceptance criteria that can only be verified when ALL children complete
- The scope boundary — everything that logically belongs to this delivery

**Epic characteristics:**
- Contains modules (and sometimes tasks directly, for small epics)
- Never worked on directly — only via its children
- Readiness = AVERAGE of all descendant task readiness (weighted or simple, depending on implementation)
- Status ceiling = `review` (never automatically moved to `done`)
- May contain its own YAML frontmatter with `epic_id`, `acceptance_criteria`, `dependencies`
- Example: E001 — Authentication System, E007 — Agent Fleet Elevation

**Epic lifecycle:**
```
created → draft → active → in-progress → review → done
```
The `in-progress` state is triggered by ANY child task becoming in-progress.
The `review` state is triggered by ALL child tasks reaching `done` or `archived`.
The `done` state requires human review confirming all acceptance criteria.

---

#### Level 2: MODULE

A module is a scoped deliverable within an epic. It defines:
- A coherent subsystem or component
- Its own acceptance criteria (more specific than the parent epic's)
- A bounded set of tasks that can be executed in roughly priority order

**Module characteristics:**
- Parent: always an epic
- Children: tasks (and sometimes sub-modules for very large modules)
- Readiness = AVERAGE of child task readiness
- Status ceiling = `review` (same rule as epics)
- Independently reviewable — a module can be reviewed and accepted before the parent epic is complete
- Example: M-SP01 (storm prevention subsystem), M-BM03 (budget mode implementation)

**When to create a module vs. a task:**
Create a module when:
1. The work requires full 5-stage execution (document → design → scaffold → implement → test)
2. The deliverable is independently reviewable and has its own acceptance criteria
3. The scope is too large to fit in a single sprint

Create a task when:
1. The work can be fully described in a scaffold (type definitions + empty tests)
2. The design decisions were made at the module level
3. The work can be completed within one session

---

#### Level 3: TASK

The task is the atomic unit of work. Tasks have:
- A specific `task_type` (epic/module/task/bug/spike/docs/refactor)
- A sequence of stages to complete based on type
- A `current_stage`, `stages_completed`, `readiness`, and `artifacts` in frontmatter
- One git commit per stage
- A definitive `done` state (readiness = 100, all required stages complete, all Done When items verified)

Tasks are what agents actually execute. The work loop (see Execution Modes and End Conditions) operates at the task level. Every agent action is: find the highest-priority undone task, determine its next required stage, execute that stage, update frontmatter, commit.

---

### The 8 Rules — Complete Reference

**Rule 1: An EPIC is a container. NEVER done by itself.**

An epic reaches `done` ONLY when ALL children are done AND acceptance criteria are met AND human review confirms. No amount of automated stage completion can close an epic. This rule prevents premature closure of strategic deliverables that appear complete on metrics but fail acceptance testing.

**Rule 2: A MODULE is a scoped deliverable within an epic. Same rule.**

Modules follow the same closure rule as epics. A module is never automatically moved to `done` — only to `review`. This is the correct behavior because modules often have cross-system impact that automated tests cannot verify. Human review is the gate.

**Rule 3: A TASK is the atomic work unit. Tasks go through stages. Done when all required stages complete.**

Tasks are the only items that can be automatically closed (status = `done`). When all required stages are in `stages_completed`, all Done When items are verified, and readiness = 100, the task can be marked `done` without human review. This is appropriate because tasks are scoped to be independently verifiable.

**Rule 4: READINESS and PROGRESS are TWO independent fields. Both flow UPWARD. Neither is set manually on containers.**

Readiness = definition completeness (is it DEFINED enough?). Progress = execution completeness (how far is the WORK?). They are independent dimensions that advance in parallel and converge toward the end. See [[readiness-vs-progress|Readiness vs Progress — Two-Dimensional Work Tracking]] for the full model.

```
epic_readiness = mean(all_task_readiness_in_epic)     # Is the epic DEFINED?
epic_progress  = mean(all_task_progress_in_epic)      # Is the epic BUILT?
```

Example: Epic E007 has 8 tasks:

| Task | Readiness | Progress |
|------|-----------|----------|
| T001 | 100 | 100 |
| T002 | 100 | 100 |
| T003 | 80 | 50 |
| T004 | 60 | 0 |
| T005-T008 | 0 | 0 |

- Epic readiness = 42% (some tasks well-defined, some not started)
- Epic progress = 31% (only 2 tasks fully built)

This tells you TWO things: the epic is moderately defined (42%) but barely built (31%). A single "41% complete" hides whether the problem is definition or execution.

**Rule 5: STATUS flows UPWARD — any child in-progress → parent in-progress. ALL children done → parent moves to review (not done).**

Status propagation means the board state is always accurate without manual updates:
- Task moves to `in-progress` → its parent module becomes `in-progress` → its parent epic becomes `in-progress`
- All tasks in a module become `done` → module moves to `review`
- All modules in an epic become `done` or `review` → epic moves to `review`
- Human confirms review → epic moves to `done`

This propagation is implemented by the orchestrator's `_evaluate_parents()` step (in OpenFleet) or by the agent's post-task update (in OpenArms). The agent is responsible for updating _index.md when a task completes.

**Rule 6: You WORK ON TASKS, not epics. To advance an epic, pick a task and complete the next stage.**

This rule is the operational imperative. When an agent is given an epic to "work on," the correct behavior is:
1. Find the epic's undone tasks in priority order
2. Pick the highest priority undone task
3. Determine that task's next required stage
4. Execute that stage
5. Repeat

An agent that attempts to directly "work on an epic" without identifying a specific task has no clear artifact to produce and no stage to follow. The rule forces decomposition to the executable level before action begins.

**Rule 7: An epic may stay in-progress for weeks. Normal.**

This rule prevents false urgency. Long-running epics are not a problem to be resolved — they are the nature of complex work. The appropriate response to an epic that has been in-progress for 3 weeks is to check whether tasks are being completed consistently (healthy) or whether no tasks have been completed (stuck). The in-progress duration is not a quality signal by itself.

**Rule 8: When an epic has no tasks left but isn't at 100%, CREATE NEW TASKS to cover the gap.**

This rule addresses incomplete decomposition. If an epic's readiness is 80% and all tasks are `done`, the 20% gap must be covered by new tasks. The methodology does not allow "rounding up" — an epic cannot be closed if readiness is below 100%. The correct response to a gap is to identify what specific work fills it and create the task.

Examples of gaps that require new tasks:
- Integration testing between newly completed modules
- Documentation that was omitted from the original decomposition
- Performance testing that wasn't planned
- Edge cases discovered during implementation

---

### Readiness Calculation Example

Epic E007 has 2 modules, each with tasks:

**Module M-01 (5 tasks):**
- T001: readiness 100 (done)
- T002: readiness 100 (done)
- T003: readiness 80 (in scaffold stage)
- T004: readiness 0 (not started)
- T005: readiness 0 (not started)

Module M-01 readiness = (100 + 100 + 80 + 0 + 0) / 5 = 56%

**Module M-02 (3 tasks):**
- T006: readiness 100 (done)
- T007: readiness 50 (in design stage)
- T008: readiness 0 (not started)

Module M-02 readiness = (100 + 50 + 0) / 3 = 50%

**Epic E007 readiness:**
Option 1 (average of modules): (56 + 50) / 2 = 53%
Option 2 (average of all tasks): (100 + 100 + 80 + 0 + 0 + 100 + 50 + 0) / 8 = 53.75% ≈ 54%

The epic is approximately 53-54% done. An agent that claimed "the epic is mostly done" because 3 of 8 tasks are complete would be wrong — the quantitative measure provides precision that subjective assessment cannot.

---

### Connection to the Wiki Backlog Pattern

In the OpenArms project, the backlog lives in `wiki/backlog/`. Each level of the hierarchy corresponds to file types:

- `wiki/backlog/_index.md` — master view of all epics, with readiness rolled up
- `wiki/backlog/epics/E00X-name.md` — individual epic files with YAML frontmatter and module list
- `wiki/backlog/tasks/T00X-name.md` — individual task files with full task frontmatter (current_stage, stages_completed, readiness, artifacts)

The work loop reads `wiki/backlog/tasks/_index.md` to find the highest-priority undone task. After task completion, the agent updates:
1. The task file (status = done, readiness = 100)
2. The parent module/epic _index.md (move task to Completed table)
3. The master backlog _index.md (readiness aggregated upward)
4. A completion note in `wiki/log/`

This file-based hierarchy is the OpenArms adaptation of OpenFleet's Plane board + OCMC task system. The pattern is the same; the infrastructure differs.

---

### OpenFleet's Implementation

In OpenFleet, the hierarchy maps to Plane's issue structure:
- Epics = Plane Cycles or Groups
- Modules = Plane Modules
- Tasks = Plane Issues with task_type field

The orchestrator's `_evaluate_parents()` step runs on every 30-second cycle and checks whether all children of any parent are in done state. When triggered, the parent's status is updated to `review`. The fleet-ops agent handles the `review` state — it is the human-equivalent review gate in the fleet.

OpenFleet's `project-manager` agent is responsible for task assignment and sprint planning. It reads the backlog, identifies unassigned tasks, creates sprint plans, and assigns tasks to worker agents. This is the equivalent of a developer picking the next task in a solo context.

---

### Anti-Patterns and What They Signal

**Anti-pattern: Setting epic readiness manually**
Signal: The agent is trying to hide that many tasks are incomplete. Or the agent does not understand that readiness is derived. Either way, the readiness field has been corrupted and the dashboard is no longer reliable.

**Anti-pattern: Marking an epic `done` when modules are in `review`**
Signal: A review step was skipped. Either the human reviewer was bypassed or the status flow logic is broken. The maximum automated status for epics and modules is `review` — any `done` that appears without a review log entry is suspect.

**Anti-pattern: Creating tasks that are too large (should be modules)**
Signal: A "task" that requires both a design document and implementation code is actually a module. Breaking this pattern results in the Document and Design stages being skipped (tasks don't require them), producing implementation without design understanding.

**Anti-pattern: Leaving epic stale when readiness is 100% but status hasn't updated**
Signal: The status propagation logic failed to fire, or the agent forgot to update the parent after the last task completed. The agent should check parent status after every task completion.

**Anti-pattern: Closing an epic because all tasks are done, without checking acceptance criteria**
Signal: The acceptance criteria (documented in the epic's design stage) were never verified. Stage completion is necessary but not sufficient — the acceptance criteria are the final gate.

### Level 0: MILESTONE — Delivery Target Above Epics

A milestone is a delivery target that groups multiple epics into a meaningful release or checkpoint.

> [!info] Milestone Characteristics
>
> | Property | Value |
> |----------|-------|
> | **Contains** | Epics (and their full hierarchies) |
> | **Purpose** | Time-boxed or feature-boxed delivery target — "what ships together" |
> | **Readiness** | AVERAGE of child epic readiness (derived, never manual) |
> | **Status ceiling** | `review` (same as epics — human confirms the milestone is met) |
> | **When to use** | When multiple epics must coordinate toward a single delivery event |

**When to use milestones vs just epics:**

> [!abstract] Milestone vs Epic Decision
>
> | Situation | Use |
> |-----------|-----|
> | Single deliverable, one team, one sprint | Epic (no milestone needed) |
> | Multiple epics that ship independently | Epics (no milestone — they're independent) |
> | Multiple epics that MUST ship together | Milestone grouping the coordinated epics |
> | Version release (v1.0, v2.0) | Milestone = the release, epics = the features |
> | Phase transition (POC→MVP, MVP→Staging) | Milestone = the phase gate, epics = the work |
> | Quarterly/sprint planning boundary | Milestone = the timebox, epics = what's committed |

**Milestone frontmatter:**

```yaml
---
title: "Milestone: v1.2 — Agent Compliance Framework"
type: milestone
domain: backlog
status: active
priority: P0
target_date: 2026-05-01
readiness: 0           # derived from child epics
epics:
  - E003               # Artifact Type System
  - E005               # Agent Compliance Framework
  - E007               # Gateway Tools (partial — M1 + M3 only)
acceptance_criteria:
  - "Agent stage violations < 5% across 10 autonomous runs"
  - "All 15 per-type standards have annotated exemplars"
  - "Gateway query API returns correct artifacts for any stage/domain combo"
created: 2026-04-12
updated: 2026-04-12
tags: [milestone, release, delivery-target]
---
```

**Examples:**
- **Milestone: v1.0 — Wiki Foundation** → grouped the original wiki structure epics
- **Milestone: v1.2 — Agent Compliance** → groups E003 + E005 + gateway tools
- **Milestone: Fleet Elevation Batch 2** → groups OpenFleet's second wave of improvements

---

### Impediment Types — Structured Categories for What Blocks Work

Not all blockers are the same. An impediment has a TYPE that determines the correct response:

> [!abstract] Impediment Type Taxonomy
>
> | Type | What It Means | Response | Example |
> |------|--------------|----------|---------|
> | **technical** | Code/infrastructure problem prevents progress | Fix the technical issue (tooling, not manual) | Node 18 incompatibility blocking test gate |
> | **dependency** | Waiting on another task, module, or epic to complete first | Sequence work correctly, or parallelize if possible | E005 needs E003's artifact definitions |
> | **decision** | A design question must be resolved before proceeding | Create a decision page, brainstorm with operator | Should templates be self-contained or reference-based? |
> | **environment** | Infrastructure, access, or setup issue | Fix with tooling (setup scripts, IaC) — never manual | Missing API key, broken CI, wrong Node version |
> | **clarification** | Requirements are ambiguous, operator input needed | File a concern/question, pause until answered | "Does 'simplified chain' mean 2 stages or 3?" |
> | **scope** | Work is larger than estimated, needs re-decomposition | Create new tasks/modules to cover the gap | Module estimated at 3 tasks actually needs 8 |
> | **external** | Waiting on something outside the project | Track and check periodically, work on other items | Hardware upgrade (19GB VRAM), third-party API availability |
> | **quality** | Prior work doesn't meet the quality bar, needs rework | Rework task using rework methodology model | Standards page is "crap" — needs restart |

**Impediment frontmatter fields:**

```yaml
impediment_type: technical | dependency | decision | environment | clarification | scope | external | quality
blocked_by: "T045"           # specific task/issue that blocks
blocked_since: 2026-04-12
escalated: false              # has this been raised to operator?
resolution: ""                # how it was resolved (filled when unblocked)
```

**Why typed impediments matter:**
- **Agents can self-diagnose:** "I'm blocked by a `technical` impediment → I should try to fix it with tooling, not hand it to the operator." vs "I'm blocked by a `decision` impediment → I need to file a concern and wait."
- **Patterns emerge:** If 60% of impediments are `environment` type, the setup tooling needs work. If 40% are `decision` type, requirements need to be clearer upfront.
- **Immune system can detect:** "Agent has been blocked by the same `technical` impediment for 3 retries → ESCALATE." Different types have different escalation thresholds.

---

### Complete Hierarchy with Milestones

```
MILESTONE (delivery target)
  ├── EPIC (strategic container)
  │     ├── MODULE (scoped deliverable)
  │     │     ├── TASK (atomic execution)
  │     │     ├── TASK
  │     │     └── TASK
  │     └── MODULE
  │           ├── TASK
  │           └── TASK
  └── EPIC
        └── TASK (small epics can have tasks directly)
```

> [!info] When to Choose What
>
> | You Have... | Create... | Because... |
> |-------------|-----------|-----------|
> | A release date or delivery event | **Milestone** | Groups epics that must coordinate |
> | A strategic capability (weeks of work) | **Epic** | Container with acceptance criteria, not directly executable |
> | A coherent subsystem (days of work) | **Module** | Independently reviewable, has its own design |
> | A single-session piece of work | **Task** | Atomic, has stages, produces artifacts |
> | A bug report | **Task** (bug-fix model) | 3 stages: document → implement → test |
> | A research question | **Task** (research model) | 2 stages: document → design, caps at 50% |
> | A known fix | **Task** (hotfix model) | 2 stages: implement → test |
> | A blocker that stops work | **Impediment** (on the blocked task) | Typed, tracked, escalatable |

## Open Questions

(All resolved — see Answered Open Questions below.)

## Answered Open Questions

> [!example]- Sub-module readiness calculation?
> Resolved in [[stage-gate-operational-decisions|Decision — Stage-Gate Operational Decisions]]. Use simple average of all descendant tasks. No intermediate sub-module averaging — flatten to leaf tasks.

> [!example]- Review trigger in solo-agent context?
> Resolved in [[stage-gate-operational-decisions|Decision — Stage-Gate Operational Decisions]]. The agent sets the epic/module to `review` status, logs the transition, and stops. The human discovers pending reviews via `pipeline status` or backlog commands.

> [!example]- Should higher-complexity tasks be weighted in readiness?
> Resolved in [[stage-gate-operational-decisions|Decision — Stage-Gate Operational Decisions]]. No weighting. If a task is too large relative to siblings, decompose it into smaller tasks instead of adding weight to the formula.

> [!example]- New gap task reduces parent readiness?
> Resolved in [[stage-gate-operational-decisions|Decision — Stage-Gate Operational Decisions]]. Yes, this is correct behavior. Adding a task with readiness 0 honestly lowers the parent's readiness. Honesty over inflation — the gap was always there, the readiness was previously overstated.

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **What principle applies?** | [[right-process-for-right-context-the-goldilocks-imperative|Principle — Right Process for Right Context — The Goldilocks Imperative]] |
> | **What is my identity?** | [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]] |
> | **System map** | [[methodology-system-map|Methodology System Map]] |

## Relationships

- DERIVED FROM: [[stage-gate-methodology|Stage-Gate Methodology]] (the hierarchy enforces stage-gating at the container level)
- BUILDS ON: [[wiki-backlog-pattern|Wiki Backlog Pattern]] (the file-based hierarchy IS the wiki backlog)
- IMPLEMENTS: [[plan-execute-review-cycle|Plan Execute Review Cycle]] (the review ceiling for epics/modules IS the review phase)
- USED BY: [[task-type-artifact-matrix|Task Type Artifact Matrix]] (epic and module types follow all 5 stages; the hierarchy rules define how they relate)
- USED BY: [[execution-modes-and-end-conditions|Execution Modes and End Conditions]] (the work loop picks tasks from the hierarchy; end conditions reference backlog-empty)
- RELATES TO: [[four-project-ecosystem|Four-Project Ecosystem]] (all four projects organize work in this hierarchy — Plane issues in OpenFleet, wiki backlog in OpenArms)
- RELATES TO: [[spec-driven-development|Spec-Driven Development]] (epics/modules always have design docs; their stage requirements enforce spec-first)
- FEEDS INTO: [[immune-system-rules|Immune System Rules]] (hierarchy violations — manual readiness, premature done status — are detectable anti-patterns)

## Backlinks

[[stage-gate-methodology|Stage-Gate Methodology]]
[[wiki-backlog-pattern|Wiki Backlog Pattern]]
[[plan-execute-review-cycle|Plan Execute Review Cycle]]
[[task-type-artifact-matrix|Task Type Artifact Matrix]]
[[execution-modes-and-end-conditions|Execution Modes and End Conditions]]
[[four-project-ecosystem|Four-Project Ecosystem]]
[[spec-driven-development|Spec-Driven Development]]
[[immune-system-rules|Immune System Rules]]
[[artifact-chains-by-model|Artifact Chains by Methodology Model]]
[[execution-mode-edge-cases|Decision — Execution Mode Edge Cases]]
[[stage-gate-operational-decisions|Decision — Stage-Gate Operational Decisions]]
[[when-to-use-milestone-vs-epic-vs-module-vs-task|Decision — When to Use Milestone vs Epic vs Module vs Task]]
[[epic-page-standards|Epic Page Standards]]
[[frontmatter-field-reference|Frontmatter Field Reference — Complete Parameter Documentation]]
[[initiation-and-planning-artifacts|Initiation and Planning Artifacts — Standards and Guide]]
[[methodology-framework|Methodology Framework]]
[[methodology-standards-initiative-infrastructure|Methodology Standards Initiative — Infrastructure Analysis]]
[[model-composition-rules|Model Composition Rules]]
[[model-methodology|Model — Methodology]]
[[readiness-vs-progress|Readiness vs Progress — Two-Dimensional Work Tracking]]
[[sdlc-rules-and-structure-customizable-project-lifecycle|SDLC Rules and Structure — Customizable Project Lifecycle]]
[[task-page-standards|Task Page Standards]]
[[three-pm-levels|Three PM Levels — Wiki to Fleet to Full Tool]]
