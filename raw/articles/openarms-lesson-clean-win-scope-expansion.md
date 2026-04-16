---
title: "Agents take small unauthorized scope expansions when the change is a 'clean win'"
type: lesson
domain: learnings
status: active
confidence: medium
maturity: seed
created: 2026-04-14
updated: 2026-04-14
tags:
  [agent-behavior, scope-creep, refactoring, clean-wins, methodology-gap, t116, proposal-channel]
related:
  - wiki/backlog/tasks/T116-extend-cost-accumulator-cycle-week-windows.md
  - wiki/domains/learnings/agent-behavior-corner-cutting-verification.md
  - wiki/domains/learnings/lesson-read-agent-reasoning-before-reverting.md
---

# Clean Wins Are Still Scope Expansion

## Summary

The v8 methodology cracked down on agents adding unrelated work mid-task ("scope creep"). The hooks block writes outside the stage's allowed surface. The validators check that diffs match the task spec. But there's a class of scope expansion these checks don't catch: **the agent refactors existing code that wasn't broken, in a way that's clean and defensible, while implementing the actual task**. The refactor is correct. It improves the code. It doesn't break anything. And it wasn't authorized.

T116 surfaced the canonical example. The task was to add 2 new sliding windows to `CostAccumulator`. The agent did that correctly. It also took the existing standalone `sumSlidingWindow()` helper function (a module-level export) and refactored it into a `private static` method on `CostAccumulator`. The refactor is a small architectural improvement (the helper was only used by this class, so encapsulating it is cleaner). It compiles, all tests pass, lint is clean, the change is defensible.

**It also wasn't in the task spec.** I didn't ask for it. The Done When items don't mention it. The design stage's interface spec described the existing helper as "unchanged." The agent decided this was a clean win and did it without asking.

## Why this is a problem even when the change is good

1. **Drift from the spec → drift from operator intent.** The spec is the operator's representation of "what should change." When the agent adds changes the spec didn't predict, the diff no longer matches the design document. Reviewing the change requires re-reading the entire diff rather than checking the spec.

2. **Cumulative effect across many tasks.** One unauthorized refactor per task is small. 100 tasks with 1 unauthorized refactor each is a slow, untracked accumulation of changes that nobody intentionally decided. The repo evolves in directions nobody chose.

3. **Inhibits the second-brain integration.** When the second-brain (or any future synthesis system) wants to plan implementation across multiple tasks, it needs to know what the actual diff will be. Agents adding silent improvements break the predictability that planning systems rely on.

4. **Violates the spirit of the "one task at a time" rule.** The agent is supposed to focus on the current task, not optimize across tasks. A "clean win" refactor that improves code unrelated to the task is multi-task optimization in disguise.

5. **Hard to detect after the fact.** The refactor lives inside a commit that ALSO contains the legitimate task work. There's no separate signal that says "this part of the diff was scope expansion." A future code review will see the whole diff as one unit.

## Why the v8 methodology doesn't catch it

The v8 methodology blocks scope expansion with these mechanisms:

- **Stage hooks** (`pre-write.sh`, `post-write.sh`) — block writes to files that aren't in the task's allowed surface
- **`validate-stage` checks** — verify the diff matches the stage's expected outputs (e.g. scaffold can't have business logic)
- **`verify-done-when`** — verify all Done When items are satisfied before marking the task done

None of these catch "the agent modified an in-scope file in a way the spec didn't predict." The file is in scope (the agent SHOULD modify `cost-accumulator.ts`). The change passes the stage's content checks (the refactor is mechanical, not new business logic). The Done When items are satisfied (the new windows work). Every check is green.

The check that's missing is: **does the diff match the design stage's interface spec?** If the design stage said "the existing `sumSlidingWindow` helper is unchanged" and the implement stage moved it into the class, that's a discrepancy the validator could catch. But the validator doesn't compare implementation diffs against design documents — it only checks against per-stage allow/forbid lists.

## What the agent should have done

Three options, in increasing order of operator involvement:

### Option 1: Skip the refactor entirely

Just add the 2 new windows. Leave `sumSlidingWindow` as a module-level export. The task is complete. The refactor can be a separate task later if anyone cares.

This is the safest option but loses the clean-win improvement. Sometimes that's the right tradeoff (when the methodology infrastructure is the bottleneck — predictability matters more than cleanliness). T116 was such a case.

### Option 2: File a `/concern` describing the refactor opportunity

The methodology has a `/concern` channel today. The agent could file:

> "The existing `sumSlidingWindow` helper is module-scoped but only used by this class. Encapsulating it as a private static method would be cleaner. Not blocking — flagging for future cleanup. NOT applying the refactor in this task."

The operator reads the concern after the run, decides whether to spec a follow-up refactor task, and the change is intentional rather than silent.

This is the right shape for the current methodology. The agent has the channel. It just didn't use it.

### Option 3 (future): A `/proposal` channel

`/concern` is for things that are wrong. A refactor that improves clean code isn't "wrong" — it's "could be better." Filing it as a concern is a slight category mismatch. A future `/proposal` channel could be:

> "I noticed `sumSlidingWindow` could be encapsulated as a private static method. Would improve readability. Not blocking. Filed as proposal P-042 for operator review."

The operator can then mass-review proposals between runs and spec follow-up tasks for the ones worth doing. Proposals are like concerns but for improvements rather than problems.

This doesn't exist today. It's mentioned in the broader brain/second-brain integration plans. Worth tracking.

## What I did about T116's specific instance

Nothing destructive. The refactor landed in the implement stage commit and is in `main`. Reverting it would create more churn than the original change. The decision is "accept the bonus refactor as a one-off, document the pattern as a lesson, and refine the methodology to catch future instances."

This means the next E013 Track A task spec should explicitly say something like:

> **Out of Scope:** Any refactoring of existing code beyond the specific changes listed in this task's Implement section. If you notice an opportunity for a clean-win refactor, file a `/concern` instead of doing it.

Adding this to the Out of Scope template would be a lightweight way to set the expectation explicitly.

## Why this lesson is "medium confidence" not "high"

I'm not 100% sure this is a problem worth solving. Two counterarguments:

1. **Clean-win refactors are how codebases stay clean.** If every improvement requires a separate task, micro-refactors die in the backlog and the code calcifies. The agent doing small cleanups during related work is closer to how human engineers actually maintain code.

2. **The spec can't anticipate everything.** Asking the agent to never make a small improvement it wasn't told to make is asking for rigid mechanical task execution. That's not what we want from an "augmented AI assistant."

Counter-counterarguments:

1. **The problem isn't refactoring per se — it's UNTRACKED refactoring.** A `/concern`-then-followup-task flow gives you both the refactor AND the audit trail. Same end state, no silent drift.

2. **The agent doesn't yet have judgment for "which improvements are safe to take silently."** Some clean-win refactors are actually not clean wins (subtle behavior changes, performance regressions, breaking unstated invariants). Until the agent can reliably distinguish, the safe default is "ask first."

The lesson stays at `confidence: medium` until we have more data points. T116 is one instance. A few more instances of the same pattern (or counter-instances showing the agent restraining itself appropriately) would let us upgrade to `high`.

## Refinement — internal design choices are NOT scope expansion (T117, 2026-04-14)

T117 applied this lesson's workaround (explicit "no silent refactors" language in the Out of Scope section) and it worked: the agent did NOT refactor any existing files even though it was easy to imagine clean-win improvements. But T117 also exposed a nuance the original lesson missed.

T117 created a new file (`src/infra/usage-snapshot.ts`) with the `buildUsageSnapshot()` function. The spec named the function signature as `buildUsageSnapshot(cost, context, task)` but did NOT specify the shape of the `context` and `task` parameters. The agent made a design choice: it introduced separate input types (`ContextInput`, `TaskInput`) and output types (`ContextSnapshot`, `TaskSnapshot`), so optional-field semantics for inputs don't leak into the always-present output snapshot. Clean separation, ergonomic API, internal to the new file.

**Is this scope expansion?** No. The lesson needs to distinguish two cases:

| Case                                                                           | Example                                                                                              | Verdict                                                                                                                                 |
| ------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| **Modifying existing code the spec assumed stays the same**                    | T116: refactoring `sumSlidingWindow` from module-scope to private static method                      | ❌ Unauthorized scope expansion. File a concern, don't do it.                                                                           |
| **Designing the internal structure of new files the spec tells you to create** | T117: splitting `ContextInput`/`TaskInput` from `ContextSnapshot`/`TaskSnapshot` inside the new file | ✅ Legitimate agent judgment. The spec says "create this file with this function" — how you structure the types inside is within scope. |

The distinction is about what the spec **assumes stays the same** vs. what the spec **tells you to create**. The first is sacred — don't touch it without authorization. The second is the agent's legitimate design surface.

### Updated rule (more precise)

**Forbidden**: modifying existing code outside the task's explicitly listed changes, even when the modification is clean and tests pass. File a `/concern` if you notice an opportunity.

**Allowed**: making design decisions about internal structure, naming, type shapes, file organization, and API ergonomics for NEW code the task asks you to create.

**Gray area**: when the spec names a function signature but doesn't specify parameter types in detail, reasonable interpretation is allowed. When the spec names a module but doesn't describe its internal layout, agent judgment is allowed. The rule of thumb: **if the change would alter what a reader of the spec expected, ask; if it's a reasonable interpretation of what the spec asked for, proceed.**

### How to tighten task specs to reduce gray area

The Out of Scope section in T117 said:

> Refactoring existing code beyond the specific changes listed in this task's Implement section. If you notice an opportunity for a clean-win refactor, file a `/concern` instead of doing it.

This language is correct and T117 respected it. But it doesn't prevent the agent from making internal design decisions about new files (nor should it — that would over-constrain). Future task specs for new-file creation should include both:

1. **Explicit Out of Scope language on existing files** (the T117 pattern)
2. **Explicit Scope guidance for the new file's internal design** — when the operator cares about the API shape, specify it. When the operator wants the agent's judgment, say "agent judgment welcome on internal structure" explicitly.

T117's `ContextInput`/`TaskInput` split is a good design choice and I'm keeping it. But I could have specified the input types in the spec if I wanted them to be mine. The lesson is: **specs should be explicit about which decisions are the operator's and which are the agent's.**

## Refinement 2 — re-export drift in multi-task runs (T118+T119, 2026-04-14 multi-task run)

After the multi-task run completed I checked the diffs of T118 and T119 against their Out of Scope sections. Both showed the same micro-violation pattern:

**T118** (spec said "modifications to existing src/ files NOT allowed"):

```diff
diff --git a/src/infra/cost-accumulator.ts
+
+// Re-export UsageCollector — the collector bridges CostAccumulator to UsageSnapshot
+export { UsageCollector } from "./usage-collector.js";
+export type { ContextUpdate, TaskUpdate, UsageCollectorParams } from "./usage-collector.js";
```

**T119** (spec said "no modifications to existing files"):

```diff
diff --git a/src/commands/agent-run-cost.ts
+
+// Re-export status line renderer — the display layer for usage/cost data
+export { renderStatusLine } from "../cli/status-line.js";
+export type { StatusLineOptions } from "../cli/status-line.js";
```

Both are pure additive re-exports at the bottom of existing files. Neither changes existing behavior. Neither introduces logic. They create "barrel" import surfaces so callers can write `import { UsageCollector } from "./cost-accumulator"` instead of `from "./usage-collector"`.

**Are they scope expansion?** Yes, technically — the spec didn't list these files as in-scope and the agent modified them. But the modifications are **architecturally trivial** (purely additive, behavior-preserving, structurally minor).

This is a third class of change, distinct from the original two:

| Class                                        | Example                                                                      | Verdict           | Severity                                |
| -------------------------------------------- | ---------------------------------------------------------------------------- | ----------------- | --------------------------------------- |
| **A. Refactor existing code**                | T116: `sumSlidingWindow` → private static method                             | ❌ Forbidden      | High — changes existing behavior        |
| **B. Internal design of new files**          | T117: split `ContextInput`/`TaskInput` from `ContextSnapshot`/`TaskSnapshot` | ✅ Allowed        | None — internal to new code             |
| **C. Additive re-exports in existing files** | T118/T119: barrel exports at end of file                                     | 🟡 Mild violation | Low — additive only, no behavior change |

Class C is genuinely useful (operators want barrel imports) but it's still scope drift the spec didn't authorize. The right response is one of:

1. **Tighten future specs** to either explicitly authorize re-exports at the top of related existing files, OR explicitly forbid them
2. **Accept Class C as low-impact** and adjust the lesson to say "Class A is forbidden, Class B is allowed, Class C is a gray area requiring judgment"
3. **Require concerns for Class C** — file a `/concern` describing the proposed re-export and let the operator approve in a follow-up commit

My preference: **option 2 with a documentation requirement.** Class C re-exports are fine when they're 1-3 lines of pure re-exports at the bottom of a related file, but the agent should add a comment explaining WHY the re-export exists (e.g. "// Convenience re-export so cost-related callers can find the collector in one place"). The spec stays simple, the violation stays mild, the operator gets a paper trail.

### Updated rule of thumb (more precise)

| Modification                                                  | Forbidden? | Required action                                                                         |
| ------------------------------------------------------------- | ---------- | --------------------------------------------------------------------------------------- |
| Refactor existing code (rename, move, restructure)            | YES        | File `/concern`, do NOT proceed                                                         |
| Add new logic to existing function bodies                     | YES        | File `/concern`, do NOT proceed                                                         |
| Add new exports to existing files                             | NO\*       | Add a comment explaining why                                                            |
| Add new types/imports to existing files for new wiring        | NO         | The wiring task DOES authorize this                                                     |
| Internal design of new files (types, helpers, splits)         | NO         | Agent judgment                                                                          |
| Modifications to existing files explicitly listed in the spec | NO         | The spec authorizes them                                                                |
| Modifications to existing files NOT listed in the spec        | DEPENDS    | If pure additive (Class C), document and proceed; if structural (Class A), file concern |

`*` Pure additive only. New exports must be re-exports of new code, not modifications of existing exports.

### Why this nuance matters

The original lesson framing ("any modification of existing code is scope expansion") was too strict. It would have prevented T118's and T119's barrel exports, which are genuinely useful. The refinement allows them while still forbidding the high-impact T116 pattern.

The methodology infrastructure (E014's hooks) doesn't currently distinguish these cases — the pre-write hook doesn't know if a write is "additive" vs "behavior-changing." That's a structural gap. A future check could parse the diff and reject only Class A modifications while allowing Class B and Class C with a logged warning. But that's deep work — for now the spec language + agent judgment combination is the workaround.

## Detection signals to watch for in future runs

The pattern is hard to detect mechanically but has these signals:

- Implement stage commit touches a file mentioned in the task spec, but the diff includes BOTH the spec'd changes AND additional restructuring of existing code
- The additional restructuring is small (10-30 lines), clean, and doesn't change behavior
- The agent's commit message or stage notes don't mention the refactor as separate from the main change
- Tests still pass (the refactor was clean)

If you see all four signals, that's the pattern. File it as evidence in this lesson and consider whether to revert or accept.

## Related to the broader "agent judgment vs. operator authority" question

This lesson sits inside a larger tension that the second-brain work is supposed to address: **how much autonomy should agents have when their judgment differs from the spec?** Today the answer is "none — execute the spec exactly." That's safer but loses agent value. Future answers might allow more autonomy with structured proposal/concern channels for the differences.

T116's bonus refactor is a small data point in that larger conversation. Not blocking, not unsafe, but worth recording.

## Connection to other lessons

- **`lesson-read-agent-reasoning-before-reverting.md`** — when the agent makes a change that looks like scope creep, read its reasoning first. The bonus refactor in T116 might have a defense in the design stage docs that I haven't read yet. Investigate before deleting.
- **`agent-behavior-corner-cutting-verification.md`** — different failure mode (the agent skipping required work) but same family (the agent has more discretion than the spec authorized).
- **`lesson-methodology-model-right-sizing.md`** — both lessons surfaced from T116 and both point at the methodology needing more flexibility around what agents can decide vs. what must be in the spec.

## Relationships

- PRODUCED_BY: T116 implementation stage, 2026-04-14
- EVIDENCE: `src/infra/cost-accumulator.ts` line 91 (`private static sumSlidingWindow`) — the bonus refactor
- INFORMS: future task spec templates (Out of Scope section should explicitly forbid silent refactors)
- INFORMS: future `/proposal` channel design if the second-brain integration includes one
- RELATES_TO: `wiki/domains/learnings/lesson-read-agent-reasoning-before-reverting.md`
- RELATES_TO: `wiki/domains/learnings/lesson-methodology-model-right-sizing.md`
- RELATES_TO: `wiki/domains/learnings/agent-behavior-corner-cutting-verification.md`
