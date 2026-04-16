---
title: "Right-size the methodology model to the actual work, not the structural category"
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

# Right-size the methodology model to the actual work, not the structural category

## Summary

The methodology selector picks a model based on `task_type` alone. For `task_type: task`, it always selects the full 5-stage `feature-development` model (document, design, scaffold, implement, test). This is correct for genuinely novel feature work but massively overkill for narrow mechanical extensions of existing infrastructure. T116 (adding 2 sliding windows to `CostAccumulator`) cost $9.07 and 35 minutes using the 5-stage model, while T117 (comparable mechanical extension) cost $1.20 and 18 minutes using the 3-stage `integration` model -- a 7.5x cost reduction for the same quality of output.

The fix is straightforward: consider the scope and novelty of the work when selecting the model, not just its structural category. For mechanical extensions, use `integration` (scaffold/implement/test) or `bug-fix` (document/implement/test). Reserve `feature-development` for genuinely novel architecture where the design stage delivers real value.

## Context

This lesson applies when speccing tasks for agent execution under a methodology that offers multiple stage models. The methodology has 9 named models ranging from 1-stage (`documentation`) to 5-stage (`feature-development`). The selector maps `task_type` to a model, but `task_type` describes structural category (task, bug, spike, docs, refactor) while the right model depends on work novelty -- a dimension the methodology does not currently represent.

The cost-to-value collapse happens specifically in the document and design stages when applied to mechanical work. Those stages produce substantive, well-formed artifacts that re-explain things already obvious from the existing code. For T116, 8 design documents were generated for a change whose answer was "do exactly what the existing windows do, but with two new constants."

## Insight

**The methodology trades cost for rigor. That trade is correct when the cost of getting it wrong is high (novel architecture). It is wrong when the right answer is already obvious from the existing pattern (mechanical extension).** The document and design stages for mechanical work are ceremonial -- they produce artifacts but deliver no decision-making value.

The right model depends on two factors, not one:
1. **Structural category** (`task_type`) -- what kind of work it is
2. **Novelty level** -- whether the solution is known or needs discovery

The 9 available models and when to use them:

| Model | Stages | Use when |
|---|---|---|
| `feature-development` | 5 (doc/des/scaf/imp/test) | Genuinely novel work, unknown solution, multiple design alternatives |
| `integration` | 3 (scaf/imp/test) | Wiring existing modules, mechanical extensions of established patterns |
| `bug-fix` | 3 (doc/imp/test) | Restoring correct behavior, known root cause, no new architecture |
| `hotfix` | 2 (imp/test) | Emergency fix where both problem and solution are already understood |
| `refactor` | 4 (doc/scaf/imp/test) | Restructure without behavior change |
| `research` | 2 (doc/des) | Investigation without implementation |
| `documentation` | 1 (doc) | Pure docs work |

## Evidence

**T116 vs T117 comparison** (same epic E013 Track A, same operator, comparable mechanical work):

| Metric | T116 (feature-development) | T117 (integration) | Delta |
|---|---|---|---|
| Cost | $9.07 | $1.20 | -86.8% (7.5x cheaper) |
| Duration | 35.2 min | 18.0 min | -49% |
| Turns | 139 | 36 | -74% |
| Stages run | 5 (doc/des/scaf/imp/test) | 3 (scaf/imp/test) | skipped doc+des |
| Lines added | 246 | 252 | comparable |
| Tests passing | 35/35 | 10/10 | both clean |
| `pnpm check` | 0/0 | 0/0 | both clean |
| Stage retries | 0 | 0 | both clean |

**Key findings**: Code quality was not affected by skipping doc/design. T117's type definitions are arguably cleaner (JSDoc on every field, proper null-semantics, separate input/output types). The scaffold stage provided sufficient structure for the agent to build on without a separate design stage.

**T116 cost-per-stage breakdown**: Roughly $1-2 per stage. The document and design stages alone cost ~$3-4 and produced 8 wiki files for work whose design was mechanically derivable from the existing pattern. The cost-per-unit-of-novelty was extremely high.

**Track A projected savings**: If tasks A3-A8 all use `integration` at ~$1.20 each, total Track A cost would be ~$8 instead of ~$54 if all used `feature-development`. Potential savings of ~$46 across the track if the pattern holds.

## Applicability

This lesson applies to three concrete actions:

1. **Task spec'ing.** When creating a new task for mechanical extension work (adding fields, extending patterns, wiring modules), set `task_type: integration` or `task_type: bug-fix` instead of `task_type: task`. Expected cost savings: 5-10x based on the T116 vs T117 comparison. A proposed `methodology_model` frontmatter field could allow explicit model override independent of `task_type`, but using the correct `task_type` from the start handles most cases.

2. **Budget planning.** Factor model selection into cost estimates. A 5-stage run costs 3-5x more than a 3-stage run for the same scope of mechanical work. Combined with the multi-task cost growth lesson, the full optimization stack is: right-size the model (5-10x savings) then prefer single-task runs when possible (~2x additional savings).

3. **Knowing when NOT to apply this.** Do not skip document/design stages when the work is genuinely novel, when multiple design alternatives need comparison, when cross-cutting concerns need explicit reasoning, or when the task is the first in its area (even if mechanical, the design doc establishes the pattern for future tasks).

**Agent self-right-sizing (future)**: The agent currently cannot change its own methodology model mid-run. A future pre-spawn check that asks "does the spec'd model fit the actual work?" could propose downgrades to the operator before starting. This is speculative but worth tracking as a research spike if cost-per-task remains a recurring pain point.

## Self-Check

> [!warning] Before spec'ing a task, ask:
>
> 1. Is the solution KNOWN from an existing pattern, or does it need DISCOVERY?
> 2. If known: use `integration` (3 stages) or `bug-fix` (3 stages), NOT `feature-development` (5 stages)
> 3. Would the document + design stages produce anything the scaffold stage doesn't already give you?
> 4. Check: 5-stage runs cost 3-5x more than 3-stage for mechanical work
> 5. When in doubt: start with `integration`, escalate only if scaffold reveals unexpected complexity

## Relationships

- RELATES TO: [[follow-the-method-of-work-not-the-methodology-label|Method of Work]] -- matching the process to the work, not the label
- RELATES TO: [[methodology-is-a-framework-not-a-fixed-pipeline|Methodology as Framework]] -- the methodology should flex, not rigidly apply one model
- RELATES TO: [[model-methodology|Model: Methodology]] -- the methodology model definitions and selection logic
- RELATES TO: [[[[per-task-cost-grows-monotonically-across-multi-task-runs-(co|Per-Task Cost Growth]] -- second-order cost optimization layered on top of this first-order savings]]
- RELATES TO: [[epic-readiness-math-is-wrong-when-an-epic-has-implicit-goals|Epic Readiness Math]] -- both surfaced from T115/T116 runs
- RELATES TO: [[universal-stages-domain-specific-artifacts|Universal Stages]] -- the stage model that right-sizing selects from
- PRODUCED BY: T116 cost analysis (2026-04-14), validated by T117

## Backlinks

[[Method of Work]]
[[not the label]]
[[Methodology as Framework]]
[[not rigidly apply one model]]
[[model-methodology|Model: Methodology]]
[[Per-Task Cost Growth]]
[[Epic Readiness Math]]
[[Universal Stages]]
[[T116 cost analysis (2026-04-14)]]
[[validated by T117]]
