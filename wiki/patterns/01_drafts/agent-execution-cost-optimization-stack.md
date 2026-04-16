---
title: "Agent Execution Cost Optimization Stack"
aliases:
  - "Agent Execution Cost Optimization Stack"
  - "Cost Optimization Stack"
type: pattern
domain: cross-domain
layer: 5
status: synthesized
confidence: medium
maturity: seed
instances:
  - page: "OpenArms T116 vs T117"
    context: "Right-sizing from feature-development to integration saved 86.8% ($9.07 → $1.20). First-order optimization."
  - page: "OpenArms multi-task run T118-T120"
    context: "Multi-task run cost 2.6x naive prediction ($9.29 vs $3.60 predicted). Single-task preference is second-order optimization."
derived_from:
  - "Right-size the methodology model to the actual work, not the structural category"
  - "Per-task cost grows monotonically across multi-task runs (context accumulation)"
created: 2026-04-16
updated: 2026-04-16
sources:
  - id: openarms-right-size
    type: wiki
    file: wiki/lessons/02_synthesized/contributed/right-size-the-methodology-model-to-the-actual-work,-not-the.md
  - id: openarms-cost-growth
    type: wiki
    file: wiki/lessons/01_drafts/contributed/per-task-cost-grows-monotonically-across-multi-task-runs-(co.md
tags: [pattern, cost, optimization, methodology, agent-execution, multi-task, contributed, synthesized]
---

# Agent Execution Cost Optimization Stack

## Summary

Agent execution cost is reducible through a five-layer optimization stack (3 original + 2 added with Opus 4.7), ordered by impact. Each layer is independent — you can apply any subset — but they compound multiplicatively. Combined, the stack can reduce a multi-task run from $54 to under $5 for the same deliverables.

## Pattern Description

The stack is ordered by ROI — highest-impact, lowest-effort optimizations first:

| Layer | Optimization | Mechanism | Measured savings | Effort |
|---|---|---|---|---|
| **1st order** | Right-size the methodology model | Use `integration` (3 stages) instead of `feature-development` (5 stages) for known-pattern work. Skip doc+design when the answer is obvious. | 86.8% per task ($9.07 → $1.20) | Zero — just pick the right `task_type` |
| **2nd order** | Right-size the effort level (NEW) | Use `high` for implementation, `medium` for maintenance, `xhigh` for architecture. Lower effort = less thinking = fewer tokens. | ~2-3x per effort level step (estimated from token reduction) | Zero — set effort per task |
| **3rd order** | Right-size the Claude model (NEW) | Use Opus 4.6 for extended-thinking tasks; 4.7 for literal/memory tasks. 4.7's tokenizer costs 35% more — use 4.6 when context is heavy. | Up to 35% savings on context-heavy tasks | Low — model selection per task |
| **4th order** | Prefer single-task runs | Each task in a multi-task run inherits prior context burden. Run tasks individually when operator time is cheap. | ~2.6x per run ($3.60 predicted → $9.29 actual for 3-task) | Low — launch N times instead of once |
| **5th order** | Minimize cross-task context bloat | Avoid unnecessary file changes that inflate codebase size for subsequent tasks. Small commit footprints. | Unquantified — behavioral | Medium — requires discipline |

**The multiplication:**
- 6-task track at feature-development, multi-task: ~$54 (6 × $9.07)
- Same track at integration, single-task: ~$7.20 (6 × $1.20)
- Savings: ~$47 (87% reduction)

**Why first-order dominates:** The cost of unnecessary stages (doc+design for mechanical work) is ~$3-4 per task regardless of other optimizations. Eliminating them is the largest single lever. Second-order (task isolation) addresses context accumulation but only saves ~2x. Third-order is behavioral noise compared to the structural savings of right-sizing.

## Instances

> [!example]- Instance 1: OpenArms E013 Track A (2026-04-14)
>
> **Before optimization:** T116 ran as `feature-development` (5 stages). Cost: $9.07, 35 min, 139 turns. Produced 8 design documents for work whose answer was "do exactly what the existing pattern does."
>
> **After first-order:** T117 ran as `integration` (3 stages). Cost: $1.20, 18 min, 36 turns. Same quality output. The doc+design stages were ceremonial.
>
> **After second-order observation:** T118-T120 multi-task run (3 tasks, integration model) cost $9.29. Naive prediction: 3 × $1.20 = $3.60. Actual: 2.6x over naive. Context accumulation inflated each successive task.
>
> **Projected full-stack savings for 6-task track:** $54 (all feature-dev, multi-task) → ~$8 (all integration, single-task). 85% reduction.

## When To Apply

- **Always apply first-order** when spec'ing tasks. Ask: "is the solution known from an existing pattern?" If yes → `integration` or `bug-fix`, not `feature-development`.
- **Apply second-order** when operator time is cheaper than agent cost. Overnight batch runs with async review → single-task. Synchronous monitoring where each launch costs operator attention → multi-task is worth the premium.
- **Apply third-order** as discipline, not as a primary lever. Don't optimize file change footprint at the expense of code quality.

## When Not To

- **Don't right-size away the design stage for genuinely novel work.** The 86.8% savings assumes the design stage produces nothing the scaffold can't derive. When there ARE multiple design alternatives, the design stage earns its cost.
- **Don't split single-task when context CONTINUITY matters.** Some multi-task runs benefit from shared context (task B reads task A's output). Splitting forces re-reading. Measure before splitting.

## Self-Check

> [!warning] Before planning any multi-task agent run, ask:
>
> 1. Can each task use `integration` instead of `feature-development`? (saves 5-10x per task)
> 2. Do the tasks need shared context, or can they run independently? (single-task saves ~2x)
> 3. What's the budget for N tasks? Use `N × baseline × 2` not `N × baseline` for multi-task
> 4. Is operator time cheaper than the 2.6x multi-task premium?

## Relationships

- DERIVED FROM: [[right-size-the-methodology-model-to-the-actual-work,-not-the|Right-Size Methodology Model — OpenArms Evidence]]
- DERIVED FROM: [[per-task-cost-grows-monotonically-across-multi-task-runs-(co|Per-Task Cost Growth — OpenArms Evidence]]
- RELATES TO: [[model-methodology|Model — Methodology]] — model selection and stage economics
- RELATES TO: [[model-local-ai|Model — Local AI ($0 Target)]] — the ultimate cost optimization: route to local inference
- RELATES TO: [[context-management-is-primary-productivity-lever|Context Management Is the Primary LLM Productivity Lever]]

## Backlinks

[[Right-Size Methodology Model — OpenArms Evidence]]
[[Per-Task Cost Growth — OpenArms Evidence]]
[[model-methodology|Model — Methodology]]
[[model-local-ai|Model — Local AI ($0 Target)]]
[[context-management-is-primary-productivity-lever|Context Management Is the Primary LLM Productivity Lever]]
[[context-depth-must-vary-per-task-type-not-per-project|Context Depth Must Vary Per Task Type, Not Per Project — Tier Selection Extends Beyond Identity]]
