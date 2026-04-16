---
title: "The harness 'turnCount' variable counts streaming events, not conversational turns"
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
contribution_status: pending-review
contribution_reason: "First bidirectional contribution test — F9 from first consumer integration feedback"
---

# The harness 'turnCount' variable counts streaming events, not conversational turns

## Summary

In the OpenArms harness (`agent-run-harness.ts:373`), the `turnCount` variable drives session-lifecycle decisions: compacting at >150 and starting fresh sessions at >=200. The variable is meant to represent conversational turns but actually increments on every `message_start` streaming event, which fires dozens of times per assistant turn. This inflates the count by 20-50x, causing sessions to restart far earlier than intended -- after roughly 10 real conversational turns instead of 200. The bug was invisible during single-task runs because `decideSessionLifecycle` never reached the `turnCount` check on the first dispatch.

## Context

This lesson applies whenever an agent harness uses streaming event counts as proxies for higher-level conversational metrics. The pattern generalizes beyond OpenArms: any system that counts protocol-level events (stream chunks, SSE frames, message blocks) and uses those counts for lifecycle decisions will hit the same inflation problem if the metric name suggests a different semantic level than what is actually measured.

The bug specifically surfaces in multi-task runs (`--tasks N` where N >= 2). Single-task runs always take the "no existing session" branch of `decideSessionLifecycle`, bypassing the `turnCount` check entirely. This is why the bug went undetected through all of the pre-Phase-2/3 development -- only single-task runs had been exercised.

## Insight

**Naming a variable after its intended semantic meaning rather than its actual measurement source creates invisible bugs in lifecycle-critical code.** The `turnCount` name led every reader (including the original author) to assume the thresholds (150/200) referred to conversational turns. In reality, they referred to streaming events, making the compact threshold dead code (it fires at ~7 real turns, but the fresh threshold at ~10 real turns fires almost simultaneously) and the fresh threshold wildly premature.

The deeper pattern: when a metric drives automated decisions, the metric's name must precisely describe what it measures, not what the designer wished it measured. Aspirational naming in lifecycle code is a class of bug that compiles, passes unit tests, and only manifests at integration boundaries.

## Evidence

**2026-04-14 multi-task run** (`pnpm openarms agent run --tasks 3 --filter E013`): T118, T119, T120 in sequence.

- T118 dispatched to a fresh session (no prior session -- expected)
- T119 continued the session (turn count at 0 after fresh -- expected)
- T120 forced a fresh session with log message: `SESSION fresh -- turn limit: 3352 >= 200`

The 3352 figure is absurd for conversational turns. The total run cost $9.29 across 158 user-facing turns across 4 result events. At ~20 `message_start` events per conversational turn, 158 turns yields ~3160 stream events -- close to the observed 3352.

**Code path** (from `agent-run-harness.ts`):
- `let turnCount = 0` (line 373) increments inside `stdoutLineHandler` on every `message_start` stream event
- `decideSessionLifecycle` receives the inflated value and compares against `maxTurns = 200`
- The compact branch (`turnCount > 150`) is effectively dead code -- it would fire at ~7 real turns, but the fresh branch (`>= 200`) fires at ~10 real turns, nearly simultaneously

**Cost impact**: Each fresh session reloads codebase context from scratch (~$0.50-$1.00 per spawn). The bug forces more fresh spawns than intended, inflating multi-task run costs.

## Applicability

This lesson applies directly to the OpenArms harness and to any agent orchestration system that:

1. **Counts streaming protocol events as a proxy for conversational turns.** The fix is to either rename the variable and adjust thresholds to match what is actually measured (Fix A: cheap, ~5 lines), or count actual conversational turns by incrementing on `type: "result"` events instead (Fix B: correct but changes runtime behavior).

2. **Uses lifecycle metrics for automated session management.** The recommended approach: track both `streamMessageCount` (for diagnostics) and `conversationalTurnCount` (for lifecycle decisions) as separate metrics. Compact at ~30-50 real turns, fresh at ~80-100 real turns.

3. **Has code paths only exercised in multi-task scenarios.** The bug was invisible because the multi-task path through `decideSessionLifecycle` was never end-to-end tested. This is the same "untested code path" risk pattern where unit tests of the function in isolation passed but integration under real conditions exposed the mismatch.

Beyond OpenArms, any system where a diagnostic log message reports an inflated metric and a human reads it at face value risks chasing the wrong root cause during debugging. The `SESSION fresh -- turn limit: 3352 >= 200` message actively misleads operators into thinking the agent performed 3352 turns of work.

## Relationships

- RELATES TO: [[agent-failure-taxonomy-seven-classes-of-behavioral-failure|Agent Failure Taxonomy]] -- untested code path failure
- RELATES TO: [[enforcement-hook-patterns|Enforcement Hook Patterns]] -- lifecycle hooks and session management
- RELATES TO: [[model-methodology|Model: Methodology]] -- methodology infrastructure bugs
- RELATES TO: [[harness-owned-loop-deterministic-agent-execution|Harness-Owned Loop]] -- the harness dispatch and session lifecycle system
- RELATES TO: [[[[per-task-cost-grows-monotonically-across-multi-task-runs-(co|Per-Task Cost Growth]] -- cost implications of premature fresh sessions]]
- RELATES TO: [[epic-readiness-math-is-wrong-when-an-epic-has-implicit-goals|Epic Readiness Math]] -- both surfaced from multi-task run observations

## Backlinks

[[Agent Failure Taxonomy]]
[[enforcement-hook-patterns|Enforcement Hook Patterns]]
[[model-methodology|Model: Methodology]]
[[harness-owned-loop-deterministic-agent-execution|Harness-Owned Loop]]
[[Per-Task Cost Growth]]
[[Epic Readiness Math]]
