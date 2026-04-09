---
title: "Model Guide: Methodology"
type: learning-path
domain: cross-domain
layer: spine
status: synthesized
confidence: high
maturity: growing
created: 2026-04-09
updated: 2026-04-09
sources: []
tags: [methodology, model-guide, learning-path, stage-gate, task-types, backlog, execution-modes, spec-driven, spine]
---

# Model Guide: Methodology

## Summary

The Methodology model describes the stage-gate system, task type taxonomy, backlog hierarchy, and execution modes that govern all work in this ecosystem — whether that work is writing code, ingesting wiki sources, or planning infrastructure. It is not itself a process document; it is the meta-system that contains, selects, and composes methodology models. The core invariant: every task runs through a named, composable stage sequence with hard artifact gates, regardless of domain. This model is the governance layer that prevents the two most common AI-agent failure modes — skipping design stages and synthesizing from descriptions instead of sources.

## Prerequisites

- Familiarity with how work is actually done in this ecosystem (at least one project or wiki task completed)
- Understanding that "methodology" here means a formal configuration, not a vague process — models are defined in YAML and enforced by tooling
- No prior stage-gate or agile experience required, though it helps

## Sequence

### L1 — Primary Sources

- `wiki/sources/src-openarms-methodology.md` — OpenArms methodology YAML and agent directive; the canonical implementation of the 5-stage model
- `wiki/sources/src-openfleet-methodology-scan.md` — OpenFleet's implementation of the same framework; confirms transferability across projects

### L2 — Core Concepts

Read in this order:

1. **Methodology Framework** (`wiki/domains/cross-domain/methodology-framework.md`) — The meta-system: what a methodology model IS, how models are selected per-condition, how they compose (nested, sequential, conditional, parallel), and the fractal property (same vocabulary at every scale). Start here.
2. **Stage-Gate Methodology** (`wiki/domains/devops/stage-gate-methodology.md`) — The 5-stage sequence (Document → Design → Scaffold → Implement → Test); hard stage boundaries; readiness ranges; per-stage required artifacts; how stages enforce themselves via protocol and hooks.
3. **Task Type Artifact Matrix** (`wiki/domains/devops/task-type-artifact-matrix.md`) — How task types (feature, research, spike, hotfix, docs, refactor) map to stage subsets and artifact bindings; why not every task runs all 5 stages.
4. **Backlog Hierarchy Rules** (`wiki/domains/devops/backlog-hierarchy-rules.md`) — The 4-level hierarchy (Epic → Module → Task → Sub-task); promotion rules; why a flat backlog is an anti-pattern.
5. **Execution Modes and End Conditions** (`wiki/domains/devops/execution-modes-and-end-conditions.md`) — Autonomous, semi-autonomous, and document-only modes; end condition types; how the agent knows when to stop.
6. **Spec-Driven Development** (`wiki/domains/ai-agents/spec-driven-development.md`) — Why specs come before implementation; the spec-to-code pipeline; how spec quality determines execution quality.
7. **Task Lifecycle Stage-Gating** (`wiki/domains/ai-agents/task-lifecycle-stage-gating.md`) — How stage gates work at the task level; the readiness percentage system; gate conditions and what triggers advancement.

### L3 — Comparisons

- **Adoption Guide** (`wiki/spine/adoption-guide.md`) — How any project picks up the framework; what is invariant vs what is per-project variable; the four integration levels (CLI → Skills → MCP → Export).
- **Wiki Backlog Pattern** (`wiki/domains/knowledge-systems/wiki-backlog-pattern.md`) — The methodology applied to knowledge work specifically; how open questions, gap analysis, and evolution candidates form a prioritized queue.

### L4 — Lessons (Validated Insights)

- **Never Skip Stages** (`wiki/lessons/never-skip-stages-even-when-told-to-continue.md`) — The lesson with the most ecosystem-wide enforcement implications: skipping stages produces the wrong artifact category, which corrupts the stage system.
- **The Agent Must Practice What It Documents** (`wiki/lessons/the-agent-must-practice-what-it-documents.md`) — The wiki agent is subject to the same stage-gate rules it documents; this is not a contradiction, it is a consistency requirement.
- **Never Synthesize from Descriptions Alone** (`wiki/lessons/never-synthesize-from-descriptions-alone.md`) — Why synthesis requires primary sources, not summaries of summaries; how this connects to the Document stage's source-provenance requirement.

### L5 — Patterns (Structural Templates)

- **Plan Execute Review Cycle** (`wiki/patterns/plan-execute-review-cycle.md`) — The convergent pattern across all successful agent workflows; how it maps to the stage-gate sequence.
- **Scaffold Foundation Infrastructure Features** (`wiki/patterns/scaffold-foundation-infrastructure-features.md`) — The SFIF macro-lifecycle model; how it composes with the 5-stage micro-model.

### L6 — Decisions (Resolved Choices)

There are no standalone decisions in this model yet — the framework itself embeds the key resolved choices (stage ordering, artifact requirements, hierarchy rules). See the config files for the authoritative definitions.

## Config Reference

These files are the ground truth for the methodology — not narrative pages but executable configuration:

- `wiki/config/methodology.yaml` — Task types, stages, modes, artifact bindings, end conditions
- `wiki/config/agent-directive.md` — The 14-step work loop, enforcement rules, and the "never" list

## Outcomes

After completing this learning path you will understand:

- What a methodology model IS in this ecosystem: a named, YAML-defined stage sequence with hard artifact gates and composable structure
- The 5-stage sequence and why each stage boundary is hard (not soft guidance)
- How task type determines which stages run and what artifacts prove completion
- The backlog hierarchy and why 4 levels (Epic → Module → Task → Sub-task) is the right granularity
- The three execution modes and how the agent knows when to stop in each
- Why the two most common failure modes (stage-skipping, synthesizing from descriptions) are structural problems, not willpower problems
- How to read and adapt `methodology.yaml` for a new project in the ecosystem

## Relationships

- FEEDS INTO: Model Guide: Claude Code
- FEEDS INTO: Model Guide: LLM Wiki
- FEEDS INTO: Model Guide: Ecosystem Architecture
- BUILDS ON: Methodology Framework
- BUILDS ON: Stage-Gate Methodology
- BUILDS ON: Task Type Artifact Matrix
- RELATES TO: Model Guide: Skills + Commands + Hooks
- RELATES TO: Adoption Guide

## Backlinks

[[Model Guide: Claude Code]]
[[Model Guide: LLM Wiki]]
[[Model Guide: Ecosystem Architecture]]
[[Methodology Framework]]
[[Stage-Gate Methodology]]
[[Task Type Artifact Matrix]]
[[Model Guide: Skills + Commands + Hooks]]
[[Adoption Guide]]
[[Model Guide: Second Brain]]
