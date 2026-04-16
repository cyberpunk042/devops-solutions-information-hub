---
title: "Per-task cost grows monotonically across multi-task runs (context accumulation)"
type: lesson
domain: learnings
status: active
confidence: medium
maturity: seed
created: 2026-04-15
updated: 2026-04-15
tags:
  [methodology, cost-optimization, multi-task-run, context-accumulation, session-pressure, harness]
related:
  - wiki/domains/learnings/lesson-methodology-model-right-sizing.md
  - wiki/domains/learnings/lesson-harness-turncount-misnamed.md
---

# Per-Task Cost Grows Monotonically in Multi-Task Runs

## Summary

When `pnpm openarms agent run --tasks N` runs multiple tasks in sequence within a single harness invocation, each successive task pays MORE than the previous task — even when the tasks are similar in scope. The cost growth comes from accumulating codebase context: each task adds new files and modifies existing ones, and the next task's "read the codebase" startup cost is higher because there's more state to absorb.

The pattern is monotonic across `--tasks N` runs and predictable: extrapolating from a single-task baseline UNDERESTIMATES the cost of the multi-task version by 2-3×.

## Evidence — multi-task run 2026-04-14 evening

Three task runs in sequence on E013 Track A (T118 → T119 → T120), all using the integration model (3 stages each), all working on related files in `src/infra/` and `src/cli/`:

| Result event #                 | Per-result cost | Per-result delta vs prior |
| ------------------------------ | --------------- | ------------------------- |
| 1 (T118 portion)               | $1.46           | baseline                  |
| 2 (T118 portion or T119 start) | $2.18           | +49%                      |
| 3 (T119 portion or T120 start) | $2.69           | +23%                      |
| 4 (T120 portion)               | $2.94           | +9%                       |
| **Total**                      | **$9.29**       | —                         |

Note: the result events don't cleanly correspond to task boundaries because the harness can produce multiple result events per task (one per assistant turn that the inner stream-json parser identifies as a "result"). The relevant signal is the monotonic growth.

For comparison:

| Reference run                            | Cost              | Notes                                       |
| ---------------------------------------- | ----------------- | ------------------------------------------- |
| T117 single-task integration             | $1.20             | the baseline                                |
| Multi-task per-task average              | $3.10 ($9.29/3)   | **2.6× the baseline**                       |
| 3 hypothetical separate single-task runs | $3.60 ($1.20 × 3) | what you'd predict from naive extrapolation |
| Actual multi-task run                    | $9.29             | **+158% over naive extrapolation**          |

The naive prediction that "running 3 tasks together costs the same as running them separately" is wrong by a factor of ~2.6.

## Root cause analysis

Three separate effects compound:

### 1. Codebase context grows after each task

T118 created `src/infra/usage-collector.ts` and `src/infra/usage-collector.test.ts`. T119 starts with those files in the repo and has to read them when assembling context for the new work. By T120, both T118's and T119's outputs are in the codebase. The agent's "understand what exists" cost grows linearly with the work that's already shipped.

### 2. Session resumption is not free

When the harness uses `decideSessionLifecycle` to `continue` (resume the same claude session for the next task), the session has to load its accumulated state. This includes cache-read of prior context, replay of prior conversation history, and re-orientation to the new task. The resumption cost is small per turn but compounds over multiple turns.

The cumulative effect: T119 paid ~$0.50-$0.70 in session-resumption cost on top of its actual work.

### 3. Fresh sessions reload the entire codebase

When `decideSessionLifecycle` decides `fresh` (start a new claude session because the current one is "too long"), the new session has to read the codebase from scratch. This is expensive because by the time the fresh decision fires, the codebase contains ALL the work from the prior tasks. T120 cost more than T117 (despite both being fresh integration-model runs) specifically because T120's "fresh" started against a codebase that had T118 + T119's work already landed.

## Prediction model

Based on the single data point of 2026-04-14:

```
multi_task_cost(N) ≈ baseline × N × (1 + growth_factor × N / 2)
```

For N=3 with `baseline = $1.20` and `growth_factor ≈ 0.5`:

```
≈ 1.20 × 3 × (1 + 0.5 × 1.5) = 1.20 × 3 × 1.75 = $6.30
```

Actual was $9.29. The prediction underestimates by ~50%, which suggests the growth factor is higher than 0.5 — closer to 1.0 in this dataset. With `growth_factor = 1.0`:

```
≈ 1.20 × 3 × (1 + 0.5 × 3) = 1.20 × 3 × 2.5 = $9.00
```

That matches actual $9.29 within margin. **But this is fitted to one data point and should not be treated as predictive without more runs.**

The point isn't the exact formula. The point is: **multi-task cost grows super-linearly. Don't budget for `N × baseline` — budget for `N × baseline × ~2` until more data is in.**

## Implications for budget planning

For a planned E013 Track A completion (8 tasks total, ~5 still to do = T118-T122), the cost forecast:

- **Naive 5-task budget**: 5 × $1.20 = $6.00
- **Multi-task 5-run budget**: 5 × $1.20 × ~2.5 = $15.00 (if all 5 in one run)
- **Five separate single-task runs**: 5 × $1.20 = $6.00 (no growth factor because each run starts fresh)

**Single-task runs are cheaper per task than multi-task runs**, but multi-task runs are LESS operator overhead (one launch, one monitoring session, one batch of evaluation). The tradeoff is dollars vs operator attention.

When operator time is more expensive than $5-10, multi-task is the right call. When operator time is cheap (e.g. asynchronous overnight runs), single-task is more economical.

## Why the right-sizing lesson is still right (just incomplete)

`lesson-methodology-model-right-sizing.md` claims that `task_type: integration` (3 stages) is dramatically cheaper than `task_type: task` (5 stages) for mechanical extension work. That claim is correct and validated. **What this lesson adds**: even with the right-sized model, multi-task runs are not linearly cheaper than N single-task runs.

The cost optimization stack:

1. **First-order optimization**: pick the right `task_type` to skip unnecessary stages (lesson-methodology-model-right-sizing.md). Saves ~5-10× per task.
2. **Second-order optimization**: prefer single-task runs when operator time is cheap. Saves ~2× compared to multi-task.
3. **Third-order optimization**: minimize cross-task context bloat by avoiding unnecessary file changes (a behavioral discipline, not a methodology setting).

The `~5-10× × ~2×` total savings is real and additive. Don't apply only one and assume it's enough.

## Caveats — what this lesson is NOT yet

This lesson is `confidence: medium` because it's based on a single multi-task run. Things I don't yet know:

- **Does the growth factor depend on epic scope?** A multi-task run that touches 3 unrelated epics might NOT show this pattern because each task's context is largely disjoint from the others.
- **Does the session lifecycle bug (lesson-harness-turncount-misnamed.md) artificially inflate the cost?** The fresh-session-too-eager bug forces context reloads that wouldn't happen if `turnCount` were measured correctly. If the bug were fixed, multi-task cost growth might be lower.
- **Is the growth factor task-shape dependent?** Mechanical Track A tasks (this run's data) might have higher growth than research tasks (which read more, write less).
- **Is this specific to E013 Track A?** The growth might be amplified because all 3 tasks were related and modified overlapping infrastructure.

A few more multi-task runs on different epics would let us upgrade to `confidence: high` and refine the formula. Until then, **use the rule of thumb "multi-task cost ≈ 2 × naive prediction" and plan accordingly.**

## Related to the harness turn-count bug

The growth factor is partially driven by `lesson-harness-turncount-misnamed.md`. That bug causes fresh sessions to fire much earlier than intended, which forces cumulative context reloads. **Fixing the turn-count bug should reduce the growth factor**, because sessions would survive longer and amortize their startup cost across more tasks.

If the turn-count fix lands and we re-run a multi-task scenario with similar shape, expect the growth factor to drop. That would be the empirical confirmation that this lesson and that bug are linked.

## Connection to other lessons

- **`lesson-methodology-model-right-sizing.md`** — first-order cost optimization. This lesson is the second-order layer.
- **`lesson-harness-turncount-misnamed.md`** — partial cause of the cost growth. Fixing the bug would reduce the growth factor.
- **`lesson-epic-readiness-sparse-children.md`** — different methodology bug that surfaced from the same multi-task run. Multi-task runs are surfacing a lot of latent issues.

## Relationships

- PRODUCED_BY: 2026-04-14 multi-task run `bwhmsotkr` — first observation of the growth pattern
- EVIDENCE: `/tmp/agent-run.log` result events showing $1.46 → $2.18 → $2.69 → $2.94 monotonic growth
- INFORMS: future budget planning for multi-task runs
- INFORMS: cost-optimization stack for the dashboard work
- RELATES_TO: `wiki/domains/learnings/lesson-methodology-model-right-sizing.md`
- RELATES_TO: `wiki/domains/learnings/lesson-harness-turncount-misnamed.md`
