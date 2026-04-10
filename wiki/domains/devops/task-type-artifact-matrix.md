---
title: "Task Type Artifact Matrix"
type: concept
layer: 2
domain: devops
status: synthesized
confidence: authoritative
created: 2026-04-09
updated: 2026-04-10
maturity: growing
derived_from:
  - "Stage-Gate Methodology"
  - "Task Lifecycle Stage-Gating"
sources:
  - id: src-openarms-methodology-yaml-full
    type: documentation
    file: raw/articles/openarms-methodology-yaml-full.md
    title: "OpenArms Methodology YAML + Agent Directive — Full Reference"
    ingested: 2026-04-09
  - id: src-openfleet-methodology-scan
    type: documentation
    file: raw/articles/openfleet-methodology-scan.md
    title: "OpenFleet Methodology Scan — Deep Research Findings"
    ingested: 2026-04-09
tags: [task-types, artifact-matrix, epic, module, task, bug, spike, docs, refactor, stage-requirements, exit-criteria, methodology, openarms, per-type, complexity-scaling]
---

# Task Type Artifact Matrix

## Summary

The Task Type Artifact Matrix defines the 7 distinct task types in the OpenArms methodology — epic, module, task, bug, spike, docs, refactor — and maps each to its required stages, artifact requirements, and exit criteria. This is the "per-case, per-size, per-type" flexibility layer on top of the 5-stage system: not every task requires all five stages. A `docs` task requires only Document; a `spike` requires Document + Design with no code; a `task` skips Design entirely. The matrix prevents over-process on simple work while enforcing full staging on complex work.

> [!info] Stage Requirement Matrix
>
> | Type | Document | Design | Scaffold | Implement | Test | Stages | Key Constraint |
> |------|----------|--------|----------|-----------|------|--------|---------------|
> | **epic** | REQUIRED | REQUIRED | REQUIRED | REQUIRED | REQUIRED | 5 | Max auto-status: `review` (human gate) |
> | **module** | REQUIRED | REQUIRED | REQUIRED | REQUIRED | REQUIRED | 5 | Max auto-status: `review` (human gate) |
> | **task** | — | — | REQUIRED | REQUIRED | REQUIRED | 3 | Inherits design from parent |
> | **bug** | REQUIRED | — | — | REQUIRED | REQUIRED | 3 | Surgical fix, no new architecture |
> | **spike** | REQUIRED | REQUIRED | — | — | — | 2 | Research only — zero code |
> | **docs** | REQUIRED | — | — | — | — | 1 | Document stage IS the deliverable |
> | **refactor** | REQUIRED | — | REQUIRED | REQUIRED | REQUIRED | 4 | Behavior must remain unchanged |

## Key Insights

> [!warning] Type selection shapes the entire execution path
> Choosing `task` instead of `module` is not labeling — it determines which stages the agent must complete. Choosing `spike` instead of `task` means the agent is FORBIDDEN from producing implementation code. Choosing wrong produces either over-process (wasted stages) or under-process (rework). **When uncertain, choose the type with MORE required stages.** Over-process on a small task wastes one stage; under-process on complex work produces rework.

> [!abstract] Design principle behind the matrix
>
> Required stages track with decision-making need and implementation risk:
> - **Epic/Module:** Highest risk → full 5-stage planning before execution
> - **Refactor:** Understand before transforming, no new decisions needed
> - **Task:** Inherits design from parent → skeleton + execution only
> - **Bug:** Understand the defect, no new architecture → surgical correction
> - **Spike:** Understand and decide, forbidden from producing code
> - **Docs:** Pure artifact production → Document stage IS the deliverable

**Spike formalizes "research without implementation."** Capped at Design — produces understanding and options only, never code. This prevents the pattern where a "quick research spike" slides into implementation. The type system enforces the boundary.

**Bug skips Design deliberately.** Adding a design document to a bug fix creates architectural pressure — the agent may be tempted to redesign the area rather than fix the defect. The Document stage is sufficient: what is broken, why, what the correct behavior is.

**Epic/Module are never auto-completed.** Maximum automated status is `review` — human confirmation required. Epic completion is a strategic decision, not a mechanical stage completion.

## Deep Analysis

### The 7 Types — Detailed Reference

> [!example]- Epic — strategic deliverable spanning modules
>
> **When to use:** Work too large for a single design document. Requires decomposition into independently-developable sub-deliverables.
>
> | Stage | Required Artifact |
> |-------|------------------|
> | Document | Wiki page with scope, affected systems map, gap analysis |
> | Design | Decision doc, config shape, high-level type sketches |
> | Scaffold | Top-level types, .env.example, empty acceptance test files |
> | Implement | Child module/task completion |
> | Test | Acceptance tests passing, cross-module integration verified |
>
> **Exit:** ALL children `done` or `archived`. Acceptance criteria met. Status = `review` (never `done` directly).

> [!example]- Module — scoped subsystem within an epic
>
> **When to use:** Feature scoped to one coherent subsystem (e.g., "authentication service", "routing layer"). Small enough for one sprint, too complex to skip design.
>
> | Stage | Required Artifact |
> |-------|------------------|
> | Document | Module scope, affected systems, gap analysis |
> | Design | Module-specific decisions (not broader epic), config shape |
> | Scaffold | Module types, .env entries, empty tests |
> | Implement | Module code filling scaffolded stubs |
> | Test | Module tests passing, no regressions |
>
> **Exit:** All child tasks `done` or `archived`. Status = `review` (human gate — module boundaries affect other systems).

> [!example]- Task — atomic work unit
>
> **When to use:** Work concrete enough to describe in a scaffold before implementation. If you can write the function signature and test case before writing the code, it is a task.
>
> **Skips Document + Design** — inherits design context from parent module/epic.
>
> | Stage | Required Artifact |
> |-------|------------------|
> | Scaffold | Type definitions, empty test files with describe blocks |
> | Implement | Code filling stubs, passing type checks, lint clean |
> | Test | Test implementations, passing suite, no regressions |
>
> **Exit:** Three stages in `stages_completed`. All Done When items verified. Readiness = 100.
>
> **If a task requires a design decision**, promote to `module` or precede with a `spike`. Sneaking design into implementation is a stage violation.

> [!example]- Bug — defect fix, no new architecture
>
> **When to use:** Behavior diverges from specification. The fix is restorative (returning to spec), not additive (adding behavior). If the fix requires a design decision, use `task` or `module`.
>
> **Skips Design + Scaffold** — surgical correction, not restructuring.
>
> | Stage | Required Artifact |
> |-------|------------------|
> | Document | Bug analysis: what is broken, why, correct behavior, affected files |
> | Implement | The fix, passing type checks, lint clean |
> | Test | Test proving fix, full regression suite passing |
>
> **Exit:** Bug behavior eliminated. Three stages complete. Existing tests pass.

> [!example]- Spike — research only, zero code
>
> **When to use:** A decision cannot be made without research. "Which library for X?" "Approach A or B?" "Performance at our scale?"
>
> **Capped at Design** — produces knowledge artifacts only.
>
> | Stage | Required Artifact |
> |-------|------------------|
> | Document | Research scope, existing state, the specific question |
> | Design | Findings with ≥3 options, tradeoffs, recommendation with rationale |
>
> **Exit:** Research question answered with enough specificity for a task/module to implement. The spike produces NO code — exploratory code during a spike is the entry point to unplanned scope.
>
> **Downstream:** Spike's Design artifact becomes input to the Document stage of whatever implements the recommendation. Spikes are NEVER final — always followed by implementation work.

> [!example]- Docs — documentation IS the work
>
> **When to use:** Deliverable is documentation only. Synthesizing wiki pages, writing architecture docs, creating guides.
>
> **Single stage** — Document IS the deliverable.
>
> | Stage | Required Artifact |
> |-------|------------------|
> | Document | Complete wiki page/doc meeting quality gates (≥30 word Summary, ≥1 relationship, reachable from _index.md) |
>
> **Exit:** Documentation exists and passes validation. The single stage does NOT lower the quality bar — a stub with no Summary is incomplete.

> [!example]- Refactor — behavior unchanged, structure improved
>
> **When to use:** Code needs restructuring (extract, split, rename, simplify) with external behavior held constant.
>
> **Skips Design** — the refactor's "design" is captured in Document: current state and target state.
>
> | Stage | Required Artifact |
> |-------|------------------|
> | Document | Current state + target state description, affected files |
> | Scaffold | New structure (new files, renamed stubs, empty modules) |
> | Implement | Transform code, maintaining all behavior |
> | Test | Existing tests pass, new structural contract tests added |
>
> **Exit:** Four stages complete. External behavior unchanged. If the refactor reveals behavior needs to change → separate `task` or `bug`. Combining is a scope violation.

### Mistype Diagnostic

> [!warning] Common type selection errors
>
> | Mistype | What Happens | Root Problem |
> |---------|-------------|-------------|
> | Epic → Task | Design decisions made during Scaffold/Implement | Architecture-without-understanding |
> | Task → Spike | Research document produced, no code | Incomplete deliverable if code was needed |
> | Bug → Task | Bug fix includes design document | Architectural pressure to expand beyond fix |
> | Module → Task | Document + Design skipped | Implementation without system impact awareness |
> | Spike → Task | Design stage (research output) skipped | No actionable output |
>
> **Decision rule:** When uncertain about scope, choose the type with MORE required stages.

### Readiness by Type

> [!tip] Readiness is always derived from stage completion evidence
>
> | Type | How Readiness Is Calculated |
> |------|---------------------------|
> | **task** | 0–49%: no stages. 50–79%: scaffold. 80–94%: +implement. 95–100%: +test |
> | **epic** | AVERAGE of children's readiness (never manual). 100% requires ALL children at 100 AND acceptance criteria verified |
> | **docs** | 0–99%: document incomplete. 100%: document complete + quality gates passed |
> | **All types** | Derived from `stages_completed`, never from subjective assessment |

## Open Questions

- How should the type system handle tasks that start as one type and evolve? A spike that reveals the answer is obvious and implementation should begin immediately — does this become a `module` or does the spike complete and a new `module` task get created?
- Is there a case for a `spike+implement` type that allows code production after the research phase is committed? The current system requires a separate task to avoid commingling research and implementation. Is this overhead justified in all cases?
- The `refactor` type lacks a Design stage, which means the "target state" is captured in the Document stage. Is a single Document artifact sufficient to capture both "current state" and "target state" analysis? Or should refactors use a two-document approach (current state in Document, target state in Design)?
- How does the matrix interact with the `full-autonomous` execution mode that skips Document on non-epic/module tasks? A `task` type with `full-autonomous` would skip Document (already not required) and run scaffold → implement → test directly. But a `bug` type with `full-autonomous` would skip Document — which IS required for bugs. Is this a mode interaction bug in the methodology design?

## Relationships

- DERIVED FROM: [[Stage-Gate Methodology]] (the type matrix selects stage subsets from the full 5-stage system)
- BUILDS ON: [[Task Lifecycle Stage-Gating]] (per-type stage selection is the flexibility layer of stage gating)
- USED BY: [[Backlog Hierarchy Rules]] (epics and modules follow the full 5-stage path; tasks use the 3-stage path)
- USED BY: [[Execution Modes and End Conditions]] (execution modes interact with type requirements — e.g., full-autonomous behavior differs by type)
- RELATES TO: [[Spec-Driven Development]] (spike type formalizes research-without-implementation; docs type formalizes documentation-as-work)
- RELATES TO: [[Wiki Backlog Pattern]] (all 7 types appear in wiki backlog; type determines which stages are tracked in frontmatter)
- RELATES TO: [[Four-Project Ecosystem]] (all four projects use task types — spike for research, docs for wiki, task/module/epic for features)
- FEEDS INTO: [[Immune System Rules]] (type violations — e.g., code produced during a spike — are detectable diseases)

## Backlinks

[[Stage-Gate Methodology]]
[[Task Lifecycle Stage-Gating]]
[[Backlog Hierarchy Rules]]
[[Execution Modes and End Conditions]]
[[Spec-Driven Development]]
[[Wiki Backlog Pattern]]
[[Four-Project Ecosystem]]
[[Immune System Rules]]
[[Adoption Guide — How to Use This Wiki's Standards]]
[[Methodology Framework]]
[[Model: Methodology]]
