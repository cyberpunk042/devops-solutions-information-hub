---
title: "Decision: Hooks Design Decisions"
type: decision
domain: ai-agents
layer: 6
status: synthesized
confidence: medium
maturity: growing
derived_from:
  - "Hooks Lifecycle Architecture"
  - "Per-Role Command Architecture"
  - "Harness Engineering"
reversibility: easy
created: 2026-04-10
updated: 2026-04-10
sources: []
tags: [hooks, pretooluse, stage-gate, latency, recursive-hooks, plan-generation, design-decisions]
---

# Decision: Hooks Design Decisions

## Summary

Five open questions from the Hooks Lifecycle Architecture page resolved by cross-referencing harness engineering guardrails, the stage-gate methodology, and Context Mode's implementation. The answers establish: PreToolUse command handlers CAN read filesystem state for dynamic stage-gating, hook latency budget is ~50ms per handler for hot-path hooks, recursive hook chains should be depth-limited to 1, and plan generation hooks are achieved via UserPromptSubmit with a `prompt` handler — not a dedicated event.

> [!success] Resolved decisions
>
> | Question | Decision | Confidence |
> |----------|----------|------------|
> | Dynamic stage-gating via filesystem read | Yes — command handlers have full FS access, read task frontmatter | High — Context Mode validates this exact pattern |
> | `--dangerously-skip-permissions` vs policy hooks | Policy hooks SHOULD survive the flag; if they don't, treat as a bug to report | Medium — not explicitly documented |
> | Latency budget for hot-path hooks | Target ≤50ms per handler; use async:true for logging/audit hooks | Medium — derived from UX expectations |
> | Recursive hook chains (agent handler triggering hooks) | Limit to depth 1 — agent handlers should NOT trigger further hooks | High — prevents unbounded execution |
> | Plan generation hook | UserPromptSubmit + prompt handler; no dedicated PlanGenerated event | High — Plannotator confirms this pattern |

## Decision

**PreToolUse CAN read task frontmatter for dynamic stage-gating.** A command handler is a shell script with full filesystem access. Reading `wiki/backlog/tasks/T001.md` frontmatter to check `current_stage` and blocking writes to `src/` during `document` stage is within the documented pattern. Context Mode does exactly this — its PreToolUse handler reads SQLite state to make routing decisions. The handler script: parse the active task's YAML, check stage, return `{"decision": "block"}` if the tool call violates the stage boundary.

**Latency budget: ≤50ms per handler on hot-path hooks.** PreToolUse fires on every tool call. In a fast session with 500 tool calls, 50ms per handler = 25 seconds total overhead. This is the upper bound of acceptable UX impact. For handlers that exceed this (database lookups, network calls), use `async: true` to fire-and-forget. Harness Engineering's TypeScript guardrail rules (R01-R13) validate this — they're local pattern matches and file reads, not network calls.

**No recursive hook chains.** If an `agent`-type handler makes tool calls that trigger further PreToolUse hooks on those calls, the chain can grow unbounded. Decision: agent handlers should execute in a context where hooks are suspended, or the runtime should enforce depth limit of 1. This matches the principle from Agent Orchestration Patterns: sub-agent scope must be bounded.

**Plan generation via UserPromptSubmit, not a dedicated event.** Plannotator demonstrates: the command sets up the planning context, UserPromptSubmit fires when the user submits the planning prompt, a `prompt` handler evaluates the plan quality and returns structured feedback via `additionalContext`. There is no PlanGenerated event because plan generation is an LLM response — it happens AFTER the user prompt, not as a distinct lifecycle event. PostToolUse or Stop hooks can intercept the plan output if needed.

## Alternatives

### Alternative: Dedicated PlanGenerated lifecycle event

> [!warning] Rejected — unnecessary extension to the event model
> Adding a 27th event for plan generation would require Claude Code platform changes. The existing UserPromptSubmit + prompt handler achieves the same result. Plannotator has validated this approach in production. Adding events has ecosystem-wide cost; using existing events correctly has zero cost.

### Alternative: Unlimited recursive hook depth

> [!warning] Rejected — unbounded execution risk
> An agent handler that triggers hooks which trigger agent handlers which trigger hooks is the hook equivalent of an infinite loop. The deterministic shell principle requires bounded execution — the hook system should not be a source of unbounded computation.

## Rationale

Each decision follows the pattern: **use existing mechanisms before requesting new ones.** Filesystem reads for stage-gating use command handlers' existing FS access. Plan generation uses existing UserPromptSubmit. Latency management uses existing `async: true`. Only the recursive depth limit is a new constraint — and it follows the bounded-execution principle documented in Agent Orchestration Patterns.

## Reversibility

All decisions are easy to reverse. They're design guidelines, not infrastructure commitments. If Claude Code adds a PlanGenerated event, adopt it. If hook latency proves not to be an issue, relax the budget. If recursive chains are needed, increase the depth limit with explicit justification.

## Dependencies

- [[Hooks Lifecycle Architecture]] — these decisions complete the open questions
- [[Harness Engineering]] — guardrail rule patterns validate the latency budget
- [[Plannotator — Interactive Plan & Code Review for AI Agents]] — validates plan generation pattern
- [[Stage-Gate Methodology]] — dynamic stage-gating is the primary use case

## Relationships

- DERIVED FROM: [[Hooks Lifecycle Architecture]]
- BUILDS ON: [[Harness Engineering]]
- BUILDS ON: [[Agent Orchestration Patterns]]
- RELATES TO: [[Stage-Gate Methodology]]
- RELATES TO: [[Plannotator — Interactive Plan & Code Review for AI Agents]]

## Backlinks

[[Hooks Lifecycle Architecture]]
[[Harness Engineering]]
[[Agent Orchestration Patterns]]
[[Stage-Gate Methodology]]
[[Plannotator — Interactive Plan & Code Review for AI Agents]]
[[Decision: Extension System Operational Decisions]]
