---
title: Readiness vs Progress — Two-Dimensional Work Tracking
aliases:
  - "Readiness vs Progress — Two-Dimensional Work Tracking"
type: concept
domain: cross-domain
status: synthesized
confidence: high
maturity: seed
created: 2026-04-12
updated: 2026-04-12
sources:
  - id: operator-directive
    type: directive
    file: raw/notes/2026-04-12-readiness-progress-pm-levels-directive.md
    description: "Operator: readiness is one side of the SDLC (definition), progress is the other (execution)"
  - id: openfleet-model
    type: observation
    file: raw/articles/openfleet-methodology-scan.md
    description: "OpenFleet models.py: task_readiness (0-99, pre-dispatch) vs task_progress (0-100, post-dispatch)"
tags: [readiness, progress, tracking, sdlc, two-dimensional, methodology, work-management]
---

# Readiness vs Progress — Two-Dimensional Work Tracking

## Summary

Work tracking requires TWO independent dimensions: READINESS (is this defined well enough to start?) and PROGRESS (how far along is the execution?). Readiness measures the left side of the SDLC — requirements, design, planning. Progress measures the right side — implementation, testing, delivery. They advance in parallel, converge toward the end, and have different ownership rules. Collapsing both into a single "percent complete" hides whether the work is ill-defined (low readiness) or unstarted (low progress) — two fundamentally different problems requiring different responses.

## Key Insights

1. **Readiness and progress are independent dimensions.** An epic at 80% readiness but 10% progress is well-defined but barely started — assign resources. An epic at 20% readiness and 50% progress is half-built on a shaky foundation — stop and define before continuing. A single percentage hides which failure mode you're in.

2. **Readiness gates progress.** Work cannot begin (or should not) until readiness crosses a threshold. OpenFleet gates dispatch at readiness 99 — the task is fully defined, contributions collected, plan confirmed before ANY implementation starts. This prevents the most expensive failure: building the wrong thing.

3. **99→100 is human-only.** No automated system marks work as complete. The final percentage requires adversarial review by a human. Systems and harnesses must know when to delegate upward. This is not a preference — it's a quality gate that prevents the "green dashboard, broken product" failure.

4. **They converge toward the end.** Early phases: readiness advances fast (defining is faster than building), progress stays low. Middle phases: both advance in parallel. Final phases: tightly coupled — the last percentages of readiness (edge cases, acceptance criteria details) and progress (final tests, integration) must converge together.

5. **Different hierarchy levels have different readiness/progress meanings.**

> [!abstract] Readiness and Progress by Hierarchy Level
>
> | Level | Readiness Means | Progress Means | Who Owns Readiness | Who Owns Progress |
> |-------|----------------|---------------|-------------------|-------------------|
> | **Milestone** | All epics defined, scope clear, target date set | All epics progressing, acceptance criteria met | Operator/PO | Derived from epics |
> | **Epic** | Requirements spec done, modules broken down, acceptance criteria specific | Modules completing, integration working | Operator/PO + agent (document stage) | Derived from modules/tasks |
> | **Module** | Design done, tasks broken down, dependencies clear | Tasks completing within module scope | Agent (design stage) + operator review | Derived from tasks |
> | **Task** | Done When items specific, stage sequence known, contributions received | Stages completing, artifacts produced, gates passing | Harness + contributions | Agent execution |

## Deep Analysis

### The Two Fields — Exact Definition

> [!info] OpenFleet Implementation
>
> ```python
> task_readiness: int = 0  # Pre-dispatch authorization (0-99). Gate at 99. PO confirms.
> task_progress: int = 0   # Post-dispatch work progression (0-100). 
>                          # 70=done, 80=challenged, 90=reviewed, 100=complete.
> ```
>
> | Field | Range | Owner | Gate | Purpose |
> |-------|-------|-------|------|---------|
> | `task_readiness` | 0-99 | PO/orchestrator | Dispatch blocked until 99 | Is this READY to be worked on? |
> | `task_progress` | 0-100 | Agent/harness | 100 requires human review | How far along is the WORK? |

**Readiness stages** map to the SDLC left side:

> [!abstract] Readiness Progression (OpenFleet methodology)
>
> | Readiness Range | Stage | What's Being Defined |
> |----------------|-------|---------------------|
> | 0-20 | conversation | Requirements clarified with PO |
> | 20-50 | analysis | Codebase examined, analysis document produced |
> | 50-80 | investigation | Root causes discovered, technical findings |
> | 80-99 | reasoning | Solution planned, contributions collected, design validated |
> | 99 | gate | PO confirms: this is ready to build |

**Progress stages** map to the SDLC right side:

> [!abstract] Progress Progression
>
> | Progress | Meaning | Who Sets It |
> |----------|---------|-------------|
> | 0 | Not started | System (initial) |
> | 10-60 | Implementation in progress | Agent (via fleet_task_progress) |
> | 70 | Agent claims done | Agent (via fleet_task_complete) |
> | 80 | Challenged / rework needed | Fleet-ops review |
> | 90 | Reviewed and approved | Fleet-ops / PO |
> | 99 | Ready for delivery | System |
> | 100 | Delivered | Human confirmation only |

### Parallel Evolution Pattern

```
READINESS  ████████████████████████████░░░░░░░░░  80%  (well-defined)
PROGRESS   ██████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  15%  (barely started)
           ^ Definition phase (readiness leads)

READINESS  ██████████████████████████████████░░░░  90%
PROGRESS   ██████████████████████░░░░░░░░░░░░░░░  55%
           ^ Parallel phase (both advancing)

READINESS  ████████████████████████████████████░░  95%
PROGRESS   █████████████████████████████████░░░░░  85%
           ^ Convergence phase (tightly coupled)

READINESS  █████████████████████████████████████░  99%  (gate: human confirms)
PROGRESS   ████████████████████████████████████░░  95%  (almost done)
           ^ Final gate (99→100 = human only, both sides)
```

### Three Levels of Project Management

The readiness/progress model operates differently at each PM level:

> [!abstract] PM Levels and Their Capabilities
>
> | Level | System | Readiness Enforcement | Progress Tracking | Human Gate |
> |-------|--------|----------------------|-------------------|-----------|
> | **L1: Wiki LLM** | In-repo backlog, CLAUDE.md, methodology.yaml | Soft — directives only, agent may ignore | Frontmatter fields, pipeline status | Operator reviews manually |
> | **L2: Fleet System** | OpenFleet orchestrator, Mission Control, Kanban | Hard — dispatch blocked until readiness gate | Real-time via fleet_task_progress, immune system | Fleet-ops agent + PO |
> | **L3: Full PM Tool** | DSPD / Plane, full SCRUM/agile | Hard — sprint planning, story point estimation | Burndown charts, velocity, time tracking | Multi-stakeholder review |

> [!warning] Each Level Wraps the Previous
>
> L2 wraps L1 — the fleet system reads the Wiki LLM's methodology and backlog. L3 wraps L2 — Plane syncs with the fleet's task state. Each level adds capabilities but DEPENDS on the lower level's data.
>
> A solo agent with only L1 can still track readiness and progress via frontmatter fields — but enforcement is voluntary. Adding L2 (harness) makes enforcement structural. Adding L3 (Plane) makes tracking organizational.

### Harness Version Progression

> [!info] Harness Versions and SDLC Integration
>
> | Version | What It Controls | SDLC Integration | When to Use |
> |---------|-----------------|-------------------|-------------|
> | **v1** (standalone) | Agent + Wiki LLM only. CLAUDE.md enforcement. | None — methodology is advisory | Solo agent, simple projects, POC |
> | **v2** (with fleet) | Agent + Wiki LLM + harness enforcement | Proper SDLC adherence. Methodology + wiki enforced. | Semi-autonomous, methodology-aware |
> | **v3** (full integration) | Agent + Wiki LLM + harness + Plane/DSPD | Full SDLC. Time tracking, sprint planning, traceability. | Production, multi-project, fleet |

### Frontmatter Field Reference — Complete

Every field in the backlog hierarchy should be documented: what it means, when it's required, and what it enables.

> [!info] Complete Frontmatter Fields for Work Items
>
> | Field | Required For | Values | What It Enables |
> |-------|-------------|--------|----------------|
> | `type` | All | milestone, epic, module, task | Page classification, template selection |
> | `status` | All | draft→active→in-progress→review→done→archived→blocked | Status propagation, board state |
> | `priority` | All | P0, P1, P2, P3 | Dispatch ordering, sprint planning |
> | `readiness` | Epic, Module, Task | 0-100 (derived for containers, computed for tasks) | Dispatch gating, honest progress reporting |
> | `task_type` | Task | epic/module/task/research/evolve/docs/bug/refactor | Methodology model selection |
> | `current_stage` | Task | document/design/scaffold/implement/test | Stage-gate enforcement |
> | `stages_completed` | Task | List of completed stages | Readiness computation, artifact verification |
> | `artifacts` | Task | List of file paths produced per stage | Traceability, artifact verification |
> | `estimate` | Task, Module | XS/S/M/L/XL | Sprint planning, velocity tracking |
> | `epic` | Module, Task | Epic ID | Hierarchy linkage, readiness roll-up |
> | `module` | Task | Module ID | Hierarchy linkage |
> | `depends_on` | Any | List of IDs | Dependency tracking, dispatch ordering |
> | `target_date` | Milestone | YYYY-MM-DD | Deadline tracking, milestone gating |
> | `epics` | Milestone | List of epic IDs | Milestone composition |
> | `acceptance_criteria` | Milestone, Epic | List of verifiable statements | Human review gate |
> | `impediment_type` | Any (when blocked) | technical/dependency/decision/environment/clarification/scope/external/quality | Blocker categorization, pattern detection |
> | `blocked_by` | Any (when blocked) | Task/issue ID | Dependency tracking |
> | `blocked_since` | Any (when blocked) | YYYY-MM-DD | Duration tracking, escalation |
> | `escalated` | Any (when blocked) | true/false | Has the blocker been raised to human? |

### How This Connects — Navigate From Here

> [!abstract] From Readiness/Progress → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **How do these track in the hierarchy?** | [[backlog-hierarchy-rules|Backlog Hierarchy Rules]] — Rule 4: both fields flow upward. [[frontmatter-field-reference|Frontmatter Field Reference — Complete Parameter Documentation]] — field definitions |
> | **What gates on readiness?** | [[contribution-gating-cross-agent-inputs-before-work|Contribution Gating — Cross-Agent Inputs Before Work]] — dispatch blocked until readiness threshold. OpenFleet gates at 99. |
> | **Where is the real implementation?** | [[src-openfleet-fleet-architecture|Synthesis — OpenFleet Fleet Architecture — Immune System, Dispatch, and Tiers]] — task_readiness (0-99) + task_progress (0-100) as two fields |
> | **How does this connect to stages?** | Readiness advances through document/design (left SDLC). Progress advances through scaffold/implement/test (right SDLC). |
> | **What PM level tracks both?** | [[three-pm-levels|Three PM Levels — Wiki to Fleet to Full Tool]] — L1: frontmatter only. L2: real-time via fleet tools. L3: burndown+velocity |
> | **Goldilocks connection** | [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]] — readiness gate threshold adapts per identity (POC: low gate, Production: 99) |

## Open Questions

> [!question] Should readiness and progress use the same 0-100 scale or different scales? **RESOLVED**
> **Two separate fields, both 0-100.** OpenFleet evidence: `task_readiness` (0-99, gate at 99) + `task_progress` (0-100, 70=done claim, 90=reviewed, 100=delivered). The 99 gate on readiness is a HUMAN CONFIRMATION gate, not a numeric threshold — the PO confirms "this is ready" at 99. A single collapsed field hides whether the problem is definition (low readiness) or execution (low progress) — two fundamentally different problems requiring different responses. The wiki recommends: both fields on all work items (milestone, epic, module, task). See [[frontmatter-field-reference|Frontmatter Field Reference — Complete Parameter Documentation]].

> [!question] How does readiness propagate for milestones? **PARTIALLY RESOLVED**
> Milestone readiness = AVERAGE of child epic readiness (same rule as epic→task). Simple average, not weighted. The Goldilocks principle applies: for a Simplified chain milestone, all epics crossing 50% readiness may be sufficient to start work. For a Full chain milestone, all epics must cross 99%. The THRESHOLD adapts per chain, but the PROPAGATION is always average. Remaining: should any epic at 0% block the milestone regardless of average?

> [!question] What is the minimum readiness threshold for dispatch?
> OpenFleet gates at 99. Is that too high for simplified chain projects? Should the gate be configurable per SDLC chain? (Requires: data from different project types.)

## Relationships

- BUILDS ON: [[backlog-hierarchy-rules|Backlog Hierarchy Rules]]
- BUILDS ON: [[stage-gate-methodology|Stage-Gate Methodology]]
- RELATES TO: [[sdlc-customization-framework|SDLC Customization Framework — Phases, Scale, and Chain Selection]]
- RELATES TO: [[harness-owned-loop-deterministic-agent-execution|Harness-Owned Loop — Deterministic Agent Execution]]
- RELATES TO: [[contribution-gating-cross-agent-inputs-before-work|Contribution Gating — Cross-Agent Inputs Before Work]]
- RELATES TO: [[infrastructure-enforcement-proves-instructions-fail|Infrastructure Enforcement Proves Instructions Fail]]
- FEEDS INTO: [[methodology-adoption-guide|Methodology Adoption Guide]]
- FEEDS INTO: [[model-methodology|Model — Methodology]]

## Backlinks

[[backlog-hierarchy-rules|Backlog Hierarchy Rules]]
[[stage-gate-methodology|Stage-Gate Methodology]]
[[sdlc-customization-framework|SDLC Customization Framework — Phases, Scale, and Chain Selection]]
[[harness-owned-loop-deterministic-agent-execution|Harness-Owned Loop — Deterministic Agent Execution]]
[[contribution-gating-cross-agent-inputs-before-work|Contribution Gating — Cross-Agent Inputs Before Work]]
[[infrastructure-enforcement-proves-instructions-fail|Infrastructure Enforcement Proves Instructions Fail]]
[[methodology-adoption-guide|Methodology Adoption Guide]]
[[model-methodology|Model — Methodology]]
[[when-to-use-milestone-vs-epic-vs-module-vs-task|Decision — When to Use Milestone vs Epic vs Module vs Task]]
[[frontmatter-field-reference|Frontmatter Field Reference — Complete Parameter Documentation]]
[[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]]
[[sdlc-rules-and-structure-customizable-project-lifecycle|SDLC Rules and Structure — Customizable Project Lifecycle]]
[[src-openfleet-fleet-architecture|Synthesis — OpenFleet Fleet Architecture — Immune System, Dispatch, and Tiers]]
[[src-sdlc-frameworks-research|Synthesis — SDLC Frameworks Research — CMMI, Lean Startup, and Agentic SDLC]]
[[three-pm-levels|Three PM Levels — Wiki to Fleet to Full Tool]]
