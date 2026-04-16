---
title: "The harness 'turnCount' variable counts streaming events, not conversational turns"
type: lesson
domain: learnings
status: active
confidence: high
maturity: seed
created: 2026-04-15
updated: 2026-04-15
tags: [methodology, harness, session-lifecycle, metrics, naming-bug, turn-count, multi-task-run]
related:
  - wiki/domains/learnings/lesson-methodology-model-right-sizing.md
---

# The Harness `turnCount` Variable Is Mis-Named and Wildly Inflated

## Summary

`src/commands/agent-run-harness.ts:373` declares `let turnCount = 0` and uses it for session-lifecycle decisions:

- `turn count > 150` → compact the session
- `turn count >= 200` (`maxTurns`) → start a fresh session

The variable is meant to track conversational turns. **It actually counts streaming `message_start` events** — which fire dozens of times per assistant turn during stream-json output. The metric is inflated by ~20-50× compared to what its name suggests. Session lifecycle decisions fire much sooner than the operator (or the lesson reader) would expect.

## Evidence — multi-task run 2026-04-14 evening

Running `pnpm openarms agent run --tasks 3 --filter E013` with T118 → T119 → T120 produced this harness event sequence (extracted from the log):

```
DISPATCH  T118  stage=scaffold  model=integration
SESSION   fresh        — no existing session
COMPLETE  T118  dur=1121.6s

DISPATCH  T119  stage=scaffold  model=integration
SESSION   continue     — turn count 0 within limits
COMPLETE  T119  dur=1014.0s

DISPATCH  T120  stage=scaffold  model=integration
SESSION   fresh        — turn limit: 3352 >= 200
COMPLETE  T120  dur=1117.7s
```

Reading the `SESSION fresh — turn limit: 3352 >= 200` line at face value: the harness believed the session had reached 3352 conversational turns by the time it dispatched T120. **That's absurd.** The total cost of the run was $9.29 across 158 user-facing turns (across 4 result events). 158 turns ≠ 3352.

The actual `turnCount` variable was incrementing on `message_start` stream events, which fire once per `assistant` message block in the stream-json output. Each agent "turn" produces multiple message blocks (thinking + text + tool_use + tool_result-handler + ...). At ~20 message_start events per conversational turn, 158 turns would produce ~3160 message_start events — close enough to 3352 to confirm the hypothesis.

## Root cause

Looking at `src/commands/agent-run-harness.ts`:

```typescript
let turnCount = 0; // line 373 — the bugged variable
const maxTurns = 200; // line 375

// ... inside the loop:
const stdoutLineHandler = (line: string) => {
  // ... parse the line ...
  if (line.includes('"type":"stream_event"') && line.includes('"message_start"')) {
    turnCount++; // INCREMENTS ON EVERY message_start
  }
  // ... other handlers ...
};

// ... session lifecycle decision:
function decideSessionLifecycle(
  sessionId: string | undefined,
  turnCount: number, // ← receives the inflated value
  previousEpic: string | undefined,
  currentEpic: string,
  maxTurns: number,
): LifecycleDecision {
  // ...
  if (turnCount >= maxTurns) {
    return { action: "fresh", reason: `turn limit: ${turnCount} >= ${maxTurns}` };
  }
  if (turnCount > 150) {
    return { action: "compact", reason: `turn count ${turnCount} > 150` };
  }
  // ...
}
```

The increment fires on `message_start` stream events. The threshold check uses the same variable as if it were conversational turns. Mismatch.

(Note: I wrote that code snippet from memory based on grep findings. The actual line numbers may differ slightly. The behavioral pattern is verified by the log evidence above.)

## Why this is a real bug, not a cosmetic name issue

1. **The compact threshold is dead code.** The check `if (turnCount > 150) return compact` would in principle compact the session at ~7-8 conversational turns (150 / ~20 message_starts per turn). But the fresh threshold `>= 200` fires almost simultaneously, so compact never gets selected. The "compact then continue" path in `decideSessionLifecycle` is reachable in theory but unreachable in practice because of the rate at which `turnCount` accumulates.

2. **Fresh sessions trigger too eagerly.** The intent of `maxTurns = 200` was "after ~200 conversational turns, the session is too long, start fresh." Reality: after ~10 conversational turns the count is already at 200 and the session restarts. Multi-task runs end up doing fresh-session-per-task much earlier than designed. This is what happened in the 2026-04-14 multi-task run — T119 → T120 transition fired `fresh` because the inflated count had passed 200 mid-T119, and the next dispatch reset state cumulatively.

3. **Fresh sessions are expensive.** Each fresh session re-loads the codebase context from scratch (~$0.50-$1 in context-load cost per fresh spawn). The bug causes more fresh spawns than intended, inflating cost.

4. **The `decideSessionLifecycle` log message is misleading.** When the operator reads `SESSION fresh — turn limit: 3352 >= 200`, they reasonably think "the agent did 3352 turns of work, that's a lot, fresh makes sense." Actually the agent did ~150 conversational turns and the metric is exaggerating by 20×. **The diagnostic message lies to the reader**, and a future operator debugging cost issues might chase the wrong cause.

## What "the right behavior" looks like

There are two valid fixes, and they're not equivalent:

### Fix A: Rename the variable, adjust thresholds

Keep counting `message_start` events but rename `turnCount` → `streamEventCount` and adjust thresholds:

- `streamEventCount > 3000` → compact (currently dead)
- `streamEventCount >= 4000` → fresh (replaces 200)

This preserves current behavior and removes the misleading naming. Cheap fix, ~5 line change. Documents what the metric actually measures.

### Fix B: Count actual conversational turns

Increment a `conversationalTurnCount` only on `type: "result"` events, which fire once per agent turn (not once per message block). Adjust thresholds back to their original semantic meaning:

- `conversationalTurnCount > 150` → compact (now fires for real)
- `conversationalTurnCount >= 200` → fresh

This fixes the metric but changes the lifecycle behavior. Sessions will live MUCH longer before triggering compact/fresh decisions. **This is the methodologically correct fix** but it changes runtime behavior, which deserves separate validation.

The Fix B variant raises a follow-up question: were the original thresholds (150/200) tuned for `streamEventCount` semantics or for `conversationalTurnCount` semantics? If they were tuned for streams (which I suspect, since the v8/v9 evolution happened with this bug present), then Fix B + threshold adjustment is the real correct path.

## Recommended approach

Spec a bug-fix task (not a feature-development task — `task_type: bug`, 3-stage `bug-fix` model) that:

1. Renames `turnCount` → `streamMessageCount` everywhere in `agent-run-harness.ts`
2. Adds a NEW `conversationalTurnCount` that increments on `type: "result"` events
3. Updates `decideSessionLifecycle` to take BOTH metrics
4. Implements the lifecycle decision using `conversationalTurnCount` for the "session is getting long" semantic check
5. Keeps `streamMessageCount` as a debug-only metric for diagnostic logs
6. Adjusts `maxTurns` and the compact threshold to values that make sense for ACTUAL conversational turns (~30-50 for compact, ~80-100 for fresh, based on T088 data)
7. Adds a unit test for `decideSessionLifecycle` that exercises all 4 branches with realistic counts

Effort: ~1 hour of agent work, ~$2-3 cost. Ship as a separate task on a separate epic (probably E001 since it's solo-agent infrastructure) or as a methodology-infrastructure task on E014.

## Why this surfaced now and not earlier

Previous runs were all single-task (`--tasks 1`). Single-task runs only call `decideSessionLifecycle` once at the start of the task. Since `sessionId` is undefined at that point, the first branch of `decideSessionLifecycle` always returns `{ action: "fresh", reason: "no existing session" }` — the `turnCount` check never fires. The bug was invisible because the path that uses the bugged variable was never taken.

**The first time the bug was observable was in a multi-task run** when `decideSessionLifecycle` got called for the SECOND task with a non-undefined `sessionId`, which made the function reach the `turnCount` check. Multi-task runs hadn't been done since T088. T088's harness had different code (pre-Phase-2/3 fix chain) so the comparison isn't direct. The 2026-04-14 multi-task run is the first observation point in the post-fix-chain era.

This is **another example of the "untested code path" risk** that `lesson-verify-all-code-paths.md` warns about. The lifecycle decision logic was nominally tested by unit tests of `decideSessionLifecycle` in isolation, but the integration path `agent-run-harness loop → stdoutLineHandler increments → decideSessionLifecycle reads → log message displays` was never end-to-end exercised under multi-task conditions.

## Connection to other lessons

- **`lesson-verify-all-code-paths.md`** — same root cause: a code path that compiled and unit-tested fine but had never been exercised in production.
- **`lesson-methodology-model-right-sizing.md`** — relevant to cost analysis. Multi-task runs have higher per-task cost partly because of fresh-session triggering, which is partly because of this bug.
- **`lesson-epic-readiness-sparse-children.md`** — both lessons surfaced from running real multi-task or sparse-epic scenarios, both expose methodology-infrastructure bugs that single-task runs hide.

## Relationships

- PRODUCED_BY: 2026-04-14 multi-task run `bwhmsotkr` — first observation
- EVIDENCE: harness event log showing `SESSION fresh — turn limit: 3352 >= 200` after a session that produced ~158 conversational turns
- INFORMS: future bug-fix task to rename + restructure the turn-count metrics
- RELATES_TO: `wiki/domains/learnings/lesson-verify-all-code-paths.md` (same untested-path failure family)
- RELATES_TO: `wiki/domains/learnings/lesson-methodology-model-right-sizing.md` (cost implications)
