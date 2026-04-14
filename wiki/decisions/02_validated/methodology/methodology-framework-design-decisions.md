---
title: Decision — Methodology Framework Design Decisions
aliases:
  - "Decision — Methodology Framework Design Decisions"
  - "Decision: Methodology Framework Design Decisions"
type: decision
domain: cross-domain
layer: 6
status: synthesized
confidence: medium
maturity: growing
derived_from:
  - "Methodology Framework"
  - "Stage-Gate Methodology"
  - "Task Type Artifact Matrix"
  - "Skyscraper, Pyramid, Mountain"
reversibility: moderate
created: 2026-04-10
updated: 2026-04-13
sources: []
tags: [methodology, framework, model-selection, composition, versioning, quality-tiers, meta-methodology, design-decisions]
---

# Decision — Methodology Framework Design Decisions
## Summary

Seven open questions from the Methodology Framework page resolved by cross-referencing the stage-gate methodology, task type artifact matrix, Skyscraper/Pyramid/Mountain quality tiers, and the wiki's own recursive application of SFIF. These are architectural questions about how the meta-methodology operates — selection engine design, composition strategy, mid-execution model changes, quality granularity, track synchronization, self-application, and versioning.

> [!success] Resolved decisions
>
> | Question | Decision | Confidence |
> |----------|----------|------------|
> | Selection engine formalization | Lookup table with fallback scoring. Simple first. | High — YAGNI until lookup fails |
> | Declarative vs imperative composition | Declarative config, imperative only for conditional branches | High — matches CLAUDE.md-as-config pattern |
> | Mid-execution model change | Promote the task, keep completed stages, restart from the new model's next required stage | High — follows backlog hierarchy rules |
> | Quality dimension granularity | Three tiers sufficient. No intermediate levels. | High — adding tiers adds decision cost without proportional value |
> | Track synchronization | Soft sync at SFIF phase boundaries, not hard gates | Medium — hard sync creates bottlenecks |
> | Framework as a model (meta-meta) | Yes — and this wiki already does it. The framework page IS the Document stage. | High — observable in practice |
> | Model versioning | Semver on methodology.yaml, no automated compatibility check | Medium — manual review sufficient at current scale |

## Decision

**Selection engine: lookup table with fallback.** Task type → model is a lookup (`methodology.yaml` already defines this). When the lookup doesn't cover a case (new task type, ambiguous scope), fall back to the "when uncertain, choose the type with MORE required stages" heuristic from the Task Type Artifact Matrix. A scoring/priority system is premature — the lookup table handles 95%+ of cases. Build the scoring system when the lookup demonstrably fails.

**Declarative composition, imperative for conditionals only.** Model sequences (SFIF → 5-stage → type-subset) are defined in `methodology.yaml` — this is declarative. Conditional branches (if spike → run 2 stages, if module → run 5) are evaluated at runtime — this is imperative. But the CONDITIONS are declared in config; only the EVALUATION is code. This matches the Deterministic Shell pattern: configuration defines what's possible, code evaluates which possibility applies.

> [!tip] Mid-execution model change: promote, don't restart
> If a `task` reveals module-level complexity during Document, promote it to `module` in frontmatter. Completed stages (`stages_completed: [document]`) are preserved — Document is required by both types, so it counts. The agent restarts from the next required stage the new type adds (Design). No work is lost. This follows the Backlog Hierarchy Rules: readiness derived from stages completed, not task type.

**Three quality tiers are sufficient.** Skyscraper / Pyramid / Mountain is a decision about rigor level, not a continuous scale. Adding "reinforced pyramid" or "lightweight skyscraper" makes the choice harder without making the outcome better. The value is in MAKING the choice explicitly — the specific tier is secondary. If a stage needs skyscraper rigor in an otherwise pyramid project, declare that stage as skyscraper in the frontmatter (`quality_override: {design: skyscraper}`), don't invent a new tier.

**Soft sync between tracks at SFIF boundaries.** When the project transitions from Foundation to Infrastructure phase (SFIF boundary), the three tracks (execution, PM, knowledge) should ALIGN — all three should acknowledge the phase change. But this is a soft sync (a checklist review), not a hard gate (blocking execution until all tracks confirm). Hard sync creates bottlenecks: the knowledge track might be mid-evolution when the execution track finishes Foundation. Let the tracks operate at their own cadence; align at boundaries via a review checkpoint.

**Yes, the framework IS a model.** The Methodology Framework page IS the Document stage of the framework's own lifecycle. The vocabulary design (models, stages, gates, tracks) IS the Design stage. `methodology.yaml` IS the Scaffold. The ecosystem projects' configurations ARE the Implement. And this wiki's `pipeline post` quality checks ARE the Test. The meta-meta level is already operational — it just wasn't explicitly labeled. This confirms the framework's recursive property: it applies to itself at every level.

**Semver on methodology.yaml, manual compatibility.** When `methodology.yaml` changes in a project, the version field bumps: minor for additive changes (new task type), major for breaking changes (stage renamed, gate removed). Cross-project compatibility is checked manually during the weekly `pipeline chain review` — not by automated tooling. At the current ecosystem scale (4 projects, 1 operator), manual review is sufficient and automated compatibility checking would be over-engineering.

## Alternatives

### Alternative: Scoring-based model selection engine

> [!warning] Deferred, not rejected
> A scoring system that evaluates task complexity, domain familiarity, and blast radius to select a model is theoretically better than a lookup table. But it requires training data (which model worked best for which conditions) that doesn't exist yet. When the lookup table produces demonstrably wrong selections 3+ times, revisit scoring.

### Alternative: Hard sync between tracks

> [!warning] Rejected — creates artificial bottlenecks
> Requiring all three tracks to complete their current phase before any track advances the SFIF phase means the slowest track blocks the others. The knowledge track (wiki evolution) operates at a different cadence than the execution track (sprint delivery). Hard sync penalizes the fast track to wait for the slow one.

## Rationale

Every decision follows: **simplest mechanism that works at current scale, with a clear trigger for upgrading.** Lookup table → upgrade to scoring when lookup fails 3+ times. Three tiers → add tiers when the choice becomes ambiguous. Soft sync → add hard sync when track drift causes integration failures. Manual version check → automate when the ecosystem exceeds 4 projects.

This is the Pyramid approach applied to the framework itself: pragmatic choices with documented triggers for skyscraper upgrades.

## Reversibility

Moderate. The selection engine, composition strategy, and versioning approach are all upgradeable without migration. Quality tiers and track sync are harder to change if projects have been calibrated to the current model — but the changes would be additive (adding tiers, adding gates), not breaking (removing options).

## Dependencies

- [[methodology-framework|Methodology Framework]] — these decisions complete the open questions
- [[stage-gate-methodology|Stage-Gate Methodology]] — stage mechanics drive the mid-execution change decision
- [[task-type-artifact-matrix|Task Type Artifact Matrix]] — type-to-model mapping is the selection engine's primary input
- [[skyscraper-pyramid-mountain|Skyscraper, Pyramid, Mountain]] — quality tier sufficiency assessment
- [[scaffold-foundation-infrastructure-features|Scaffold → Foundation → Infrastructure → Features]] — SFIF phase boundaries drive the sync decision

> [!info] SDLC Profile Context
> This decision was calibrated for a 4-project ecosystem with 1 operator and lookup-table model selection. At different profile levels:
> - **Simplified chain:** Selection engine is unnecessary — the operator picks the model directly. Three quality tiers collapse to one (Pyramid). Versioning is irrelevant with a single project.
> - **Full chain:** The lookup table should upgrade to a scoring engine with telemetry-trained thresholds. Hard sync between tracks replaces soft sync. Automated version compatibility checks become mandatory across 10+ projects.
> See [[sdlc-customization-framework|SDLC Customization Framework]] for profile details.

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **What framework does this configure?** | [[methodology-framework|Methodology Framework]] |
> | **What quality model does this reference?** | [[skyscraper-pyramid-mountain|Skyscraper, Pyramid, Mountain]] |
> | **Related decision: quality tiers** | [[quality-tier-operational-decisions|Decision — Quality Tier Operational Decisions]] |
> | **Related decision: task type edges** | [[task-type-edge-cases|Decision — Task Type Edge Cases]] |
> | **Where does this fit?** | [[methodology-system-map|Methodology System Map]] |

## Relationships

- DERIVED FROM: [[methodology-framework|Methodology Framework]]
- BUILDS ON: [[stage-gate-methodology|Stage-Gate Methodology]]
- BUILDS ON: [[task-type-artifact-matrix|Task Type Artifact Matrix]]
- RELATES TO: [[skyscraper-pyramid-mountain|Skyscraper, Pyramid, Mountain]]
- RELATES TO: [[scaffold-foundation-infrastructure-features|Scaffold → Foundation → Infrastructure → Features]]

## Backlinks

[[methodology-framework|Methodology Framework]]
[[stage-gate-methodology|Stage-Gate Methodology]]
[[task-type-artifact-matrix|Task Type Artifact Matrix]]
[[skyscraper-pyramid-mountain|Skyscraper, Pyramid, Mountain]]
[[scaffold-foundation-infrastructure-features|Scaffold → Foundation → Infrastructure → Features]]
[[quality-tier-operational-decisions|Decision — Quality Tier Operational Decisions]]
[[task-type-edge-cases|Decision — Task Type Edge Cases]]
[[methodology-is-a-framework-not-a-fixed-pipeline|Methodology Is a Framework, Not a Fixed Pipeline]]
