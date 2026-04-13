---
title: Decision — Task Type Edge Cases
aliases:
  - "Decision — Task Type Edge Cases"
  - "Decision: Task Type Edge Cases"
type: decision
domain: devops
layer: 6
status: synthesized
confidence: medium
maturity: growing
derived_from:
  - "Task Type Artifact Matrix"
  - "Stage-Gate Methodology"
  - "Methodology Framework"
reversibility: easy
created: 2026-04-10
updated: 2026-04-10
sources: []
tags: [task-types, spike, type-evolution, mid-execution, design-decisions]
---

# Decision — Task Type Edge Cases
## Summary

Four open questions from the Task Type Artifact Matrix and Wiki Backlog Pattern pages — what happens when tasks change type mid-execution, whether spike+implement should exist, how to migrate from external boards, and how to handle async human gating.

> [!success] Resolved decisions
>
> | Question | Decision | Confidence |
> |----------|----------|------------|
> | Task type evolution mid-execution | Spike completes, then new task/module created. Never merge phases. | High — follows stage-gate separation |
> | spike+implement compound type | No. Spike produces knowledge; implementation is a separate deliverable. | High — commingling is the failure mode |
> | Board migration (Plane → wiki backlog) | Keep both. Plane for human PM; wiki for agent context. | High — OpenFleet validates this |
> | Async human gating | Semi-autonomous mode + session artifacts (not MCP tools). | Medium — pragmatic given current tooling |

## Decision

> [!tip] Spikes complete, then spawn implementation work
> A spike that reveals an obvious answer does NOT become an implementation task. The spike completes (Document + Design stages, both with artifacts). The spike's Design artifact — the recommendation document — becomes the input for a NEW `task` or `module` that implements the answer. Two clean deliverables are better than one muddled one. The spike's purpose is knowledge; the task's purpose is code.

**No spike+implement compound type.** The entire value of spikes is that they cannot produce code. This constraint is what prevents "quick research" from sliding into unplanned implementation. If the overhead of creating a separate task after a spike feels excessive, the overhead IS the safety mechanism — it forces a conscious decision to implement, not an accidental slide from research into coding. Cross-referencing Rework Prevention: "prevention is orders of magnitude cheaper than correction."

**Keep Plane and wiki backlog in parallel.** OpenFleet validates this architecture: Plane provides human-facing PM (burndown charts, sprint views, velocity tracking) while the wiki backlog provides agent-facing context (frontmatter state machine, stage gates, artifact provenance). The duality is not drift — it is separation of concerns. Plane answers "what is the project's health?" The wiki answers "what should the agent do next?" Drift is managed by the 5 sync mechanisms documented in OpenFleet (structural, state, semantic, event-driven, intent).

**Async human gating via semi-autonomous mode + session artifacts.** When a task needs human input mid-execution, the agent uses `semi-autonomous` mode (pause after each task). The agent writes its question to `wiki/log/` as a session note, sets the task to `blocked` with a `blocked_by` note describing what input is needed, and stops. The human reviews the log, provides input (as a new log entry or direct edit to the task), and the next session picks up the unblocked task. This is lower-tech than a `fleet_request_input` MCP tool but works TODAY without new infrastructure.

## Alternatives

### Alternative: Mutable task types (spike → module in-place)

> [!warning] Rejected — violates stage-gate audit trail
> Changing a task's type mid-execution means `stages_completed` no longer matches the type's required stages. A spike with `stages_completed: [document, design, scaffold]` is incoherent — spikes don't have a scaffold stage. The git history shows commit messages referencing stages that shouldn't exist for the type. The audit trail breaks.

### Alternative: MCP tool for async human gating

> [!warning] Deferred — not rejected, but not needed yet
> A `fleet_request_input` MCP tool would be cleaner: the agent sends a structured query, the tool queues it for human review, the response arrives when the human answers. This is the right long-term architecture. But it requires building an MCP tool, a notification system, and a response queue. Session artifacts + blocked status achieve the same result with zero new infrastructure.

## Rationale

Every decision preserves stage-gate integrity and avoids premature infrastructure. Spike completion before implementation keeps phases clean. Parallel boards keep concerns separated. Session artifacts for async gating use existing wiki infrastructure. These are Pyramid-tier decisions — pragmatic, correct, and upgradeable when scale demands it.

## Reversibility

All easy. Adding a spike+implement type later is additive. Migrating from parallel boards to wiki-only is a policy change. Upgrading from session artifacts to MCP-based gating adds infrastructure without changing the workflow.

## Dependencies

- [[task-type-artifact-matrix|Task Type Artifact Matrix]] — resolves 2 of its open questions
- [[wiki-backlog-pattern|Wiki Backlog Pattern]] — resolves 2 of its open questions
- [[stage-gate-methodology|Stage-Gate Methodology]] — stage-gate integrity drives the spike decision
- [[methodology-framework-design-decisions|Decision — Methodology Framework Design Decisions]] — mid-execution type change already resolved there

> [!info] SDLC Chain Context
> This decision was calibrated for a solo operator managing spikes and tasks via wiki backlog. At different chain levels:
> - **Simplified chain:** Task type evolution is rare — most work is tasks or hotfixes, and spikes are informal conversations rather than tracked work items with stage artifacts.
> - **Full chain:** Spike-to-module promotion becomes a harness-managed workflow with automated task creation. Board sync between Plane and wiki backlog is enforced by integration tooling, not manual discipline. Async gating uses a dedicated MCP request-input tool instead of session logs.
> See [[sdlc-customization-framework|SDLC Customization Framework]] for chain details.

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **What defines the task type matrix?** | [[task-type-artifact-matrix|Task Type Artifact Matrix]] |
> | **What backlog pattern does this reference?** | [[wiki-backlog-pattern|Wiki Backlog Pattern]] |
> | **Related decision: framework design** | [[methodology-framework-design-decisions|Decision — Methodology Framework Design Decisions]] |
> | **What prevents rework from type confusion?** | [[rework-prevention|Rework Prevention]] |
> | **Where does this fit?** | [[methodology-system-map|Methodology System Map]] |

## Relationships

- DERIVED FROM: [[task-type-artifact-matrix|Task Type Artifact Matrix]]
- DERIVED FROM: [[wiki-backlog-pattern|Wiki Backlog Pattern]]
- BUILDS ON: [[stage-gate-methodology|Stage-Gate Methodology]]
- RELATES TO: [[methodology-framework-design-decisions|Decision — Methodology Framework Design Decisions]]
- RELATES TO: [[rework-prevention|Rework Prevention]]

## Backlinks

[[task-type-artifact-matrix|Task Type Artifact Matrix]]
[[wiki-backlog-pattern|Wiki Backlog Pattern]]
[[stage-gate-methodology|Stage-Gate Methodology]]
[[methodology-framework-design-decisions|Decision — Methodology Framework Design Decisions]]
[[rework-prevention|Rework Prevention]]
