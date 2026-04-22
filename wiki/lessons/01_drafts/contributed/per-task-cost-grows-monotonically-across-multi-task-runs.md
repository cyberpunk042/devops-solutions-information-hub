---
title: "Per-task cost grows monotonically across multi-task runs (context accumulation)"
type: lesson
domain: cross-domain
layer: 4
status: synthesized
confidence: medium
maturity: seed
derived_from: []
created: 2026-04-16
updated: 2026-04-16
sources: []
tags: [contributed, inbox]
contributed_by: "openarms-harness-v10"
contribution_source: "/home/jfortin/openarms"
contribution_date: 2026-04-16
contribution_status: accepted
contribution_reason: "First bidirectional contribution test — F9 from first consumer integration feedback"
---

# Per-task cost grows monotonically across multi-task runs (context accumulation)

## Summary

When running multiple tasks in sequence within a single harness invocation (`--tasks N`), each successive task costs more than the previous one, even when the tasks are similar in scope and complexity. The growth comes from three compounding effects: codebase context accumulates as each task adds files, session resumption carries replay overhead, and fresh sessions triggered mid-run must reload an increasingly large codebase. Naive budgeting (`N x single-task cost`) underestimates actual multi-task cost by roughly 2-3x. The rule of thumb until more data is available: budget `N x baseline x 2` for multi-task runs.

## Context

This lesson applies when planning and budgeting autonomous agent runs that execute multiple tasks sequentially in a single harness session. The pattern is specific to harness architectures where tasks share (or inherit) codebase context within a session, and where session lifecycle decisions (compact, fresh) are triggered by accumulated metrics.

The lesson sits as a second-order cost optimization layer on top of the first-order optimization from methodology model right-sizing. Even with the correct model selected (e.g., `integration` instead of `feature-development`), multi-task runs still exhibit super-linear cost growth.

## Insight

**Multi-task cost grows super-linearly because each task inherits the context burden of all prior tasks.** Three effects compound:

1. **Codebase context growth.** T118 creates new files; T119 has to read those files when orienting to its task. By T120, both T118 and T119 outputs are in the codebase. The agent's "understand what exists" startup cost grows linearly with shipped work.

2. **Session resumption overhead.** When the harness continues a session (rather than starting fresh), the session replays prior conversation history and re-orients to the new task. This cost is small per turn but compounds across tasks within a continued session.

3. **Fresh session codebase reload.** When `decideSessionLifecycle` forces a fresh session (due to the inflated `turnCount` -- see the turnCount bug lesson), the new session reads the entire codebase from scratch. By that point the codebase contains all prior tasks' outputs, making the reload more expensive than a clean single-task start.

The cost optimization stack, in priority order:
- **First-order**: Pick the right methodology model to skip unnecessary stages (saves 5-10x per task)
- **Second-order**: Prefer single-task runs when operator time is cheap (saves ~2x vs multi-task)
- **Third-order**: Minimize cross-task context bloat by avoiding unnecessary file changes (behavioral discipline)

## Evidence

**2026-04-14 multi-task run** on E013 Track A (T118, T119, T120), all using the `integration` model (3 stages each):

| Result event | Per-result cost | Delta vs prior |
|---|---|---|
| 1 (T118 portion) | $1.46 | baseline |
| 2 (T118/T119 boundary) | $2.18 | +49% |
| 3 (T119/T120 boundary) | $2.69 | +23% |
| 4 (T120 portion) | $2.94 | +9% |
| **Total** | **$9.29** | -- |

**Comparison to single-task baseline:**

| Scenario | Cost | Notes |
|---|---|---|
| T117 single-task integration | $1.20 | the baseline |
| Multi-task per-task average | $3.10 ($9.29/3) | 2.6x the baseline |
| 3 separate single-task runs (predicted) | $3.60 ($1.20 x 3) | naive extrapolation |
| Actual multi-task run | $9.29 | +158% over naive |

The naive prediction that "running 3 tasks together costs the same as running them separately" was wrong by a factor of ~2.6x.

**Fitted prediction model** (single data point, not yet validated across multiple runs):
```
multi_task_cost(N) ~ baseline x N x (1 + growth_factor x N/2)
```
With `growth_factor = 1.0` and `baseline = $1.20`: estimated $9.00 for N=3, actual $9.29 (within margin).

## Applicability

This lesson applies to three concrete planning scenarios:

1. **Budget planning for multi-task autonomous runs.** Do not use `N x single-task-cost` as the budget. Use `N x single-task-cost x 2` as a conservative estimate until the growth factor is calibrated with more data points.

2. **Choosing between multi-task and single-task execution modes.** Single-task runs are cheaper per task but require more operator overhead (one launch per task). When operator attention is expensive (e.g., synchronous monitoring), multi-task is worth the premium. When operator attention is cheap (e.g., overnight batch runs with async review), single-task is more economical.

3. **Evaluating the interaction with the turnCount bug.** The premature fresh-session triggering from the inflated `turnCount` metric forces unnecessary context reloads, amplifying the growth factor. Fixing the turnCount bug should reduce multi-task cost growth -- re-running a similar scenario post-fix would confirm this empirically.

**Confidence caveat**: This lesson is based on a single multi-task run. Open questions remain about whether the growth factor depends on epic scope (disjoint task contexts might not compound), task shape (research tasks read more and write less), or whether it is specific to E013 Track A's overlapping infrastructure changes.

## Relationships

- RELATES TO: [[[[right-size-the-methodology-model-to-the-actual-work-not-the|Right-Size Methodology Model]] -- first-order cost optimization that this lesson layers on top of]]
- RELATES TO: [[[[the-harness-turncount-variable-counts-streaming-events-not|Harness turnCount Bug]] -- partial cause of cost growth via premature fresh sessions]]
- RELATES TO: [[epic-readiness-math-is-wrong-when-an-epic-has-implicit-goals|Epic Readiness Math]] -- both lessons surfaced from the same multi-task run
- RELATES TO: [[model-methodology|Model: Methodology]] -- methodology infrastructure and cost analysis
- RELATES TO: [[harness-owned-loop-deterministic-agent-execution|Harness-Owned Loop]] -- session lifecycle and dispatch architecture
- RELATES TO: [[context-management-is-primary-productivity-lever|Context Management]] -- context accumulation as a cost driver

## Backlinks

[[Right-Size Methodology Model]]
[[Harness turnCount Bug]]
[[Epic Readiness Math]]
[[model-methodology|Model: Methodology]]
[[harness-owned-loop-deterministic-agent-execution|Harness-Owned Loop]]
[[Context Management]]
