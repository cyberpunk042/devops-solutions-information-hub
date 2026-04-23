---
title: "Hierarchical Metrics Fail on Sparse Coverage"
aliases:
  - "Hierarchical Metrics Fail on Sparse Coverage"
type: pattern
domain: cross-domain
layer: 5
status: synthesized
confidence: medium
maturity: growing
instances:
  - page: "OpenArms epic readiness"
    context: "average(child.readiness) = 100% with 1 of 14 children done. 5/5 frontmatter fields fiction. Dangerous when 1-4 children, benign at 10+."
  - page: "Sprint velocity from incomplete stories"
    context: "Team velocity computed from completed stories only. Sprint with 3 of 10 stories done, all large, shows high velocity. Missing stories invisible."
derived_from:
  - "Epic readiness math is wrong when an epic has implicit goals beyond its current children"
created: 2026-04-16
updated: 2026-04-22
sources:
  - id: openarms-epic-readiness
    type: wiki
    file: wiki/lessons/02_synthesized/contributed/epic-readiness-math-is-wrong-when-an-epic-has-implicit-goals.md
tags: [pattern, metrics, hierarchy, coverage, anti-pattern, contributed]
---

# Hierarchical Metrics Fail on Sparse Coverage

## Summary

When a parent metric is derived from its children (average, sum, max) and the children don't cover the parent's full scope, the derived value is a mathematical artifact. It satisfies the formula but answers a different question than the one the consumer asks. "What percent of this epic is done?" becomes "What percent of the tasks we've created so far are done?" — which can be 100% when the real answer is 10%.

## Pattern Description

The pattern has three structural components:

1. **Parent metric derived from children.** `parent.readiness = average(child.readiness)`, `sprint.velocity = sum(completed_story.points)`, `project.health = weighted_average(module.health)`. The formula is mathematically correct.

2. **Children don't cover parent scope.** The parent has goals, deliverables, or dimensions not yet decomposed into children. The epic has 14 implicit tasks but only 1 is created. The sprint has 10 stories but only 3 are pointed.

3. **The gap between children and scope is invisible to the formula.** The derived metric has no way to know what's missing. It computes over what EXISTS, not what SHOULD exist. The formula is correct; the input is incomplete.

**The danger window scales with sparsity:**

| Child count | Coverage | Trust level |
|---|---|---|
| 1-4 children | Probably sparse | DO NOT trust derived metrics |
| 5-9 children | Mixed states reveal gaps | Approximately correct |
| 10+ children | Likely covers scope | Reliable |

## Instances

> [!example]- Instance 1: OpenArms E013 epic readiness (2026-04-14)
>
> One research spike (T115) completed. `average([100]) = 100`. Epic auto-flipped to `status: review, readiness: 100`. The epic body described 14+ implementation tasks across two tracks. The harness recomputed readiness 3 times (T115, T116, T117); each time it produced fiction. Compounding bugs: stage-name pollution (epics don't have stages), stale artifact lists (stuck on first child). 5 of 5 frontmatter fields wrong.

> [!example]- Instance 2: Sprint velocity from completed-only stories
>
> Sprint velocity = sum of completed story points. Sprint with 3 large stories (13, 8, 8 = 29 points) done out of 10 total stories (50 points total). Reported velocity: 29 points (high!). Actual throughput: 58% of committed work. The 7 incomplete stories are invisible to the velocity calculation, creating an inflated metric that feeds into future sprint planning.

## When To Apply

- **Recognize it** when a parent metric hits 100% unexpectedly early
- **Prevent it** by requiring minimum child count before trusting derived metrics, OR requiring parent-level done-when items independent of children
- **Diagnose it** by asking: "do the current children cover ALL of the parent's goals?" If not, the metric is an artifact
- **Fix it** (cheap): warn on 100% with <5 children. (Medium): parent done-when items as an independent gate. (Expensive): scope declaration with coverage tracking.

## Structural Fix — Backlog Rule 8

> [!tip] Backlog Hierarchy Rule 8 is the STRUCTURAL fix for this pattern
>
> The pattern names the failure mode; [[backlog-hierarchy-rules|Backlog Hierarchy Rule 8]] names the remediation: **create new tasks when an epic has no tasks left but readiness < 100%**. Rule 8 closes the gap by requiring the harness to detect "children done, parent not complete by acceptance criteria" and respond by generating missing children rather than flipping the parent to review.
>
> **The harness responsibilities Rule 8 implies:**
>
> | Responsibility | What the harness does |
> |---|---|
> | Detection | All children are `done` but parent's acceptance criteria name work that has no matching child |
> | Classification | Surface as `impediment_type: scope` on the parent epic |
> | Gate | Block status progression to `review` until new child tasks are created that cover the missing scope |
> | Evidence | OpenArms implemented Rule 8's warning layer as `recalculate-epic.cjs` enhancement on 2026-04-16 (commit `74e8a50d`). Full Rule 8 gap-detection (auto-generation of missing children) is not yet in code — only warning. |
>
> The pattern and Rule 8 are bidirectional: the pattern explains WHY a metric failed; Rule 8 prescribes HOW the harness should respond. Without Rule 8 in code, the pattern's remediation stays advisory.

## When Not To

- When children ARE the complete scope (leaf-level tasks in a fully decomposed work breakdown)
- When the parent has no implicit goals beyond its children (a module that IS its 3 tasks, nothing more)
- When the metric is informational, not decision-driving (showing progress on a dashboard vs auto-flipping status)

## Self-Check

> [!warning] Before trusting any parent-derived metric, ask:
>
> 1. How many children does this parent have?
> 2. Do those children FULLY cover the parent's scope?
> 3. Would the metric change if you added the implicit work as children?
> 4. Is this metric driving automated decisions (status flip, dispatch, reporting)?

## Relationships

- DERIVED FROM: [[epic-readiness-math-is-wrong-when-an-epic-has-implicit-goals|Epic Readiness Math — OpenArms Evidence]]
- RELATES TO: [[model-methodology|Model — Methodology]] — readiness computation and epic lifecycle
- RELATES TO: [[readiness-vs-progress|Readiness vs Progress]] — the two-dimensional tracking model this pattern challenges
- RELATES TO: [[backlog-hierarchy-rules|Backlog Hierarchy Rules]] — Rule 8 is the structural fix this pattern prescribes
- RELATES TO: [[coverage-blindness-modeling-only-what-you-know|Coverage Blindness]] — same structural gap at the metric level
- RELATES TO: [[systemic-incompleteness-is-invisible-to-validation|Systemic Incompleteness]] — implicit goals invisible to the formula

## Backlinks

[[Epic Readiness Math — OpenArms Evidence]]
[[model-methodology|Model — Methodology]]
[[Readiness vs Progress]]
[[backlog-hierarchy-rules|Backlog Hierarchy Rules]]
[[Coverage Blindness]]
[[Systemic Incompleteness]]
