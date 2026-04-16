---
title: "Right-size the methodology model to the actual work, not the structural category"
type: lesson
domain: learnings
status: active
confidence: medium
maturity: seed
created: 2026-04-14
updated: 2026-04-14
tags:
  [methodology, model-selection, cost-optimization, task-type, feature-development, bug-fix, t116]
related:
  - wiki/backlog/tasks/T116-extend-cost-accumulator-cycle-week-windows.md
  - wiki/config/methodology.yaml
  - wiki/domains/learnings/lesson-epic-readiness-sparse-children.md
---

# Right-Size the Methodology Model to the Actual Work

## Summary

The methodology selector picks a model based on `task_type` (`task`, `bug`, `spike`, `docs`, `refactor`, etc.). For `task_type: task`, it picks `feature-development` — the full 5-stage model (document → design → scaffold → implement → test) with its full artifact requirements. **This is the right default for genuinely new feature work, but it's overkill for narrow mechanical extensions of existing infrastructure.** The selector should consider the SCOPE of the work, not just its structural category.

T116 (extend `CostAccumulator` with 2 new sliding windows) is the canonical example. The actual code work was: 2 new enum members, 2 new constants, 2 new class state fields, 2 new method calls per existing method, 2 new env var parses, 19 new unit tests. ~246 lines spread across 4 files. Mechanical, well-defined, low-novelty.

The 5-stage feature-development model produced 8 design documents (requirements / infrastructure / gaps / ADR / tech-spec / interface-spec / config-spec / test-plan) BEFORE writing a single line of code. Each was substantive, well-formed, and reusable. The agent did exactly what the methodology asked. **And it cost $9.07 over 35 minutes for a change that a competent engineer could write in 30 minutes for free.**

The methodology trades cost for rigor. That trade is correct for novel architectural work where the cost of getting it wrong is high. It is wrong for mechanical extensions where the right answer is already obvious from the existing pattern.

## Evidence — T116 cost analysis

| Stage     | Time spent  | Output                                                                    |
| --------- | ----------- | ------------------------------------------------------------------------- |
| Document  | ~6 min      | 3 wiki files (requirements + infrastructure map + gap analysis)           |
| Design    | ~12 min     | 5 wiki files (ADR + tech-spec + interface-spec + config-spec + test-plan) |
| Scaffold  | ~5 min      | 5 file modifications (types extended, test stubs added)                   |
| Implement | ~7 min      | 3 file modifications (real logic in cost-accumulator + env reader)        |
| Test      | ~5 min      | 1 file modification (real assertions filled in)                           |
| **Total** | **~35 min** | **8 wiki files + 4 src files modified**                                   |
| **Cost**  | **$9.07**   |                                                                           |

The cost-per-stage breakdown is roughly even ($1-2 per stage). The document and design stages alone cost ~$3-4 and produced 8 wiki files for a task whose actual code change is "add 2 things to an existing pattern." The artifacts are not wasted — they're reusable and they correctly anchor the implementation in operator intent — but the cost-to-novelty ratio is way off.

For comparison:

- T088 (cowork E2E test, 5-stage feature-development, genuine novel work): $14.83 / 50 min for ~135 lines in 12 files. **Cost per line ~$0.11**.
- T116 (cost accumulator extension, 5-stage feature-development, narrow mechanical work): $9.07 / 35 min for ~246 lines in 4 files. **Cost per line ~$0.037** (cheaper per line because the work was simpler) but cost per _unit-of-novelty_ much higher (the work was mechanically derivable from the existing pattern, so the design overhead delivered less value).

## What "right-sized" looks like

The methodology has 9 named models (`wiki/config/methodology.yaml`):

| Model                 | Stages                    | When to use                                                      |
| --------------------- | ------------------------- | ---------------------------------------------------------------- |
| `feature-development` | 5 (doc/des/scaf/imp/test) | Genuinely new feature work, novel architecture, unknown solution |
| `research`            | 2 (doc/des)               | Investigation without implementation                             |
| `knowledge-evolution` | 2 (doc/imp)               | Distilling higher-layer wiki pages                               |
| `documentation`       | 1 (doc)                   | Pure docs work                                                   |
| `bug-fix`             | 3 (doc/imp/test)          | Restore correct behavior — no new architecture                   |
| `refactor`            | 4 (doc/scaf/imp/test)     | Restructure without changing behavior                            |
| `hotfix`              | 2 (imp/test)              | Emergency fix when problem + solution already known              |
| `integration`         | 3 (scaf/imp/test)         | Wire existing modules into runtime                               |
| `project-lifecycle`   | 4 (sfif)                  | Macro-level, contains other models                               |

T116's actual work shape was closer to **`integration`** (scaffold + implement + test) or **`hotfix`** (implement + test) than to `feature-development`. Either would have skipped the document and design stages — saving $3-4 and ~15 minutes — and still produced the same code.

Why? Because:

- **Document stage value**: low. The existing pattern was already understood. The 3 document-stage wiki files re-explain things that `cost-accumulator.ts:67` (`WINDOW_DURATIONS`) and `cost-accumulator.ts:22` (`BudgetWindow`) already make obvious to anyone reading the code.
- **Design stage value**: low. The 5 design-stage wiki files document a design where the answer was "do exactly what the existing windows do, but with two new constants." The ADR has no real alternatives to compare. The interface spec is a copy of the existing interface with 2 fields added.
- **Scaffold stage value**: medium. Real value — types added before logic.
- **Implement stage value**: high. The actual mechanical extension.
- **Test stage value**: high. 19 new tests covering the new windows.

The first two stages are where the cost-to-value ratio collapsed. **For mechanical extensions of existing infrastructure, document and design stages are ceremonial.**

## How to fix this in the spec, not the methodology

The methodology selector currently keys on `task_type` only. The right model for a given task depends on TWO things:

1. **Structural category** (`task` vs `bug` vs `spike` vs `docs`) — what the methodology calls `task_type`
2. **Novelty level** — is the work genuinely new (need design), or a mechanical extension of existing patterns (skip design)?

The methodology has no representation of "novelty." Adding one would be invasive (schema change, new selector logic, agent has to detect novelty correctly). A simpler fix: **specify the model explicitly in the task frontmatter** and let it override the selector default.

### Proposed frontmatter extension

Add an optional `methodology_model` field to task frontmatter:

```yaml
---
title: "Extend CostAccumulator..."
type: task
task_type: task # structural category
methodology_model: integration # NEW: explicit override of the default for task_type
...
---
```

When `methodology_model` is set, the selector uses that model instead of looking up `task_type` in `model_selection`. When unset, behavior is unchanged (current default).

This is additive, backwards compatible, and lets the operator (or a smart agent) right-size individual tasks without changing the selector logic.

### When to override

Use `methodology_model: integration` (3 stages) when:

- You're wiring existing standalone code into a runtime consumer
- The bridge pattern applies (existing module + adapter + consumer edit)

Use `methodology_model: bug-fix` (3 stages) when:

- The work fixes broken behavior with a known root cause
- No new architecture, no design alternatives

Use `methodology_model: hotfix` (2 stages) when:

- Both problem AND solution are already understood
- You're skipping documentation because the urgency justifies it

Use `methodology_model: refactor` (4 stages) when:

- Restructuring without behavior change
- Type-system changes that don't add features

Use the default `feature-development` (5 stages) when:

- Genuinely new functionality
- Solution unknown at task creation time
- Multiple design alternatives need consideration

### What T116 should have looked like

T116's frontmatter, in retrospect:

```yaml
---
title: "Extend CostAccumulator with 5-hour cycle and 7-day rolling windows"
type: task
task_type: task
methodology_model: integration # NEW: 3-stage model instead of 5-stage default
priority: P1
epic: E013
...
---
```

The agent would have run scaffold → implement → test, skipping document and design. Estimated savings: ~$3-4, ~15 minutes. Same code output.

## Cost as an operator-facing concern

This lesson connects to the operator directive: "A way to make the AI assistant more economic." Right-sizing model selection is one of the cheapest economic optimizations available — no infrastructure changes required, just better task spec'ing.

Other related cost optimizations to consider in future lessons:

- Per-task `effort` levels (`low/medium/high/max`) currently default to `auto` which scales thinking depth. For mechanical work, `--effort low` is sufficient and cheaper.
- Model selection (`opus` vs `sonnet`): mechanical work can use sonnet, complex design work needs opus. The harness currently doesn't switch per stage.
- Skipping sub-agent delegation when not needed: the `Agent` tool spawns sub-agents at extra cost. For narrow tasks, the main agent's direct tool use is cheaper.

## Validation evidence — T117 (2026-04-14 evening)

This lesson was written post-T116 as a prediction: "if T116 had used `task_type: integration` instead of `task_type: task`, it would have saved ~$3-4 and ~15 minutes for the same code output." T117 was the first task to apply the prediction — same shape of work (mechanical extension of existing patterns, no novel architecture), same epic (E013 Track A), same operator, different `task_type`.

**Empirical result — the prediction was correct and the savings were larger than predicted:**

| Metric         | T116 (feature-development) | T117 (integration)                           | Delta                     |
| -------------- | -------------------------- | -------------------------------------------- | ------------------------- |
| Cost           | $9.07                      | **$1.20**                                    | **-86.8% (7.5× cheaper)** |
| Duration       | 35.2 min                   | **18.0 min**                                 | **-49%**                  |
| Turns          | 139                        | **36**                                       | **-74%**                  |
| Stages run     | 5 (doc/des/scaf/imp/test)  | **3 (scaf/imp/test)**                        | skip doc+des              |
| Artifacts      | 8 wiki + 4 src             | **2 src (new file + test)**                  | —                         |
| Lines added    | 246                        | **252**                                      | comparable                |
| Tests added    | 19                         | **10**                                       | scaled to surface         |
| Tests passing  | 35/35                      | **10/10**                                    | both clean                |
| `pnpm check`   | 0/0                        | **0/0**                                      | both clean                |
| Stage retries  | 0                          | **0**                                        | both clean                |
| Concerns filed | 0                          | **1 (template conflict — correct behavior)** | —                         |

**Key takeaways from the comparison:**

1. **The savings came from skipping two stages, not from writing sloppier code.** Both runs produced comparable lines-per-task and both were lint/test-clean. T117 skipped the document and design stages entirely and went straight to scaffold/implement/test.

2. **The document and design stages for mechanical work are where the cost-to-value ratio collapsed.** T116 spent ~$3-4 on those two stages producing 8 wiki files that documented a design where the answer was already obvious from the existing pattern. T117 skipped them and lost nothing.

3. **Code quality was not affected.** T117's `UsageSnapshot` type definition is arguably cleaner than T116's `CostAccumulator` extension — JSDoc on every field, proper null-semantics, pure builder function, separate input/output types. The scaffold-stage artifacts (types + test stubs) gave the agent enough structure to build on without needing a separate design stage.

4. **The agent's concern-filing discipline was better in T117.** T116 had 0 concerns (nothing surprising to flag). T117 had 1 concern — and it was a GOOD one: the implement-stage template generically says "wire into an existing file" but T117's Done When explicitly forbade modifying existing files (wiring was deferred to T118). The agent caught the conflict, followed task-spec over generic-template, AND filed a concern so the inconsistency is visible. That's exactly the methodology-vs-task-spec precedence behavior you want.

5. **Duration was slightly over the predicted 10-15 min range** (actual: 18 min), but cost was dramatically under the predicted $3-4 range. The asymmetry suggests fixed per-stage harness overhead dominates for small tasks — skipping stages saves dollars faster than it saves wall-clock time.

### The lesson upgrade this justifies

The lesson was written with `confidence: medium` pending real-world validation. T117 is one data point — not enough to upgrade to `confidence: high` (that needs multiple independent applications). But the evidence is strong enough to say:

- **For narrow mechanical extensions of existing patterns**, use `task_type: integration` or `task_type: bug-fix` instead of `task_type: task`. Expected cost savings: **5-10×** based on T116 vs T117.
- **For wiring tasks** (connecting new modules to existing consumers), `task_type: integration` is the correct default.
- **The `methodology_model` frontmatter override field is a nice-to-have, not a blocker.** T117 used the existing `task_type: integration` selector path and it worked correctly. The override field is useful for cases where the structural category and the work shape genuinely diverge (e.g. a `task_type: task` that's actually a refactor), but most cases can be handled by picking the right `task_type` from the start.

### Track A projected savings

E013 Track A has 8 tasks (A1-A8). T116 did A1 at $9.07 (overspent). T117 did A2 at $1.20 (right-sized). If A3-A8 all use `task_type: integration` at ~$1.20 each: **total Track A cost ~$8** instead of ~$54 if all used feature-development. **$46 savings across the track** if the pattern holds.

## When this lesson does NOT apply

Do NOT skip the document/design stages when:

- The work is genuinely novel (no existing pattern to extend)
- Multiple design alternatives need to be compared
- Backwards compatibility constraints are non-obvious
- Cross-cutting concerns (security, concurrency, data integrity) need explicit reasoning
- The operator wants the design artifact for handoff or review purposes
- The task is the FIRST in its area — even if mechanical, the design doc establishes the pattern that future tasks will extend

The lesson is "right-size, not undersize." Default to `feature-development` when in doubt. Switch to a narrower model only when the work is clearly a mechanical extension of an established pattern.

## Open question — should the agent be allowed to right-size?

The agent currently can't change its own methodology model mid-run. The selector is deterministic from frontmatter. But an agent that detects "this work is a mechanical extension, no design needed" could in principle propose a model downgrade to the operator before starting.

Two ways this could work:

1. **Pre-spawn check**: a new methodology hook that runs before stage 0 and asks the agent "given the task description, does the spec'd model fit?" If the agent says no, the harness exits with a recommendation for the operator to re-spec.
2. **Post-document check**: after the document stage produces requirements, a check fires that asks "given the requirements, is the rest of the spec'd model still appropriate?" This would let the agent detect "the design stage will produce nothing novel" and propose stopping after document.

Both are speculative. Worth filing as a future research spike if the cost-per-task pattern becomes a recurring pain point.

## Connection to other lessons

- **`lesson-specific-done-when.md`** — both lessons argue that the methodology only knows what is structurally encoded. Right-sizing is the model-selection version of "specific done-when items produce better work."
- **`lesson-methodology-battle-tested.md`** — adds another data point about methodology limitations under real use.
- **`lesson-epic-readiness-sparse-children.md`** — both lessons surfaced from T115/T116 runs and point at structural fixes the methodology needs.

## Relationships

- PRODUCED_BY: T116 cost analysis, 2026-04-14
- EVIDENCE: `wiki/backlog/tasks/T116-extend-cost-accumulator-cycle-week-windows.md` + commit chain `28d4d1ed` through `6af293e3`
- INFORMS: future task spec'ing for E013 Track A (A2-A8) and Track B (B1-B6) — most should use `methodology_model: integration` or `bug-fix` rather than the default `feature-development`
- INFORMS: future structural fix to add `methodology_model` frontmatter field to task schema
- RELATES_TO: `wiki/domains/learnings/lesson-specific-done-when.md`
- RELATES_TO: `wiki/domains/learnings/lesson-epic-readiness-sparse-children.md`
- RELATES_TO: operator directive "A way to make the AI assistant more economic"
