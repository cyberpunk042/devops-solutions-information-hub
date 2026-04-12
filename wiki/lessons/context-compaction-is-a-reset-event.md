---
title: "Context Compaction Is a Reset Event"
type: lesson
domain: ai-agents
layer: 4
status: synthesized
confidence: high
maturity: growing
derived_from:
  - "Infrastructure Enforcement Proves Instructions Fail"
  - "Agent Failure Taxonomy — Six Classes of Behavioral Failure"
created: 2026-04-12
updated: 2026-04-12
sources:
  - id: openarms-compaction
    type: observation
    file: raw/articles/openarms-agent-behavior-failures.md
    description: "OpenArms v10 — post-compact hook rebuilds task state; without it, all corrections lost"
  - id: openarms-v10-learnings
    type: observation
    file: raw/articles/openarms-methodology-v10-v11.md
    description: "OpenArms CLAUDE.md learning: 'After compaction, re-read ALL memories first — all old illnesses return'"
tags: [context-compaction, reset, agent-behavior, enforcement, memory-loss, openarms]
---

# Context Compaction Is a Reset Event

## Summary

When an LLM agent's context is compacted (summarized to reduce token count), all behavioral corrections accumulated during the session are lost. The agent reverts to base behavior — the same failures that were corrected earlier reappear immediately. Context compaction is not a "trim" — it is a RESET. Any enforcement that depends on accumulated context (corrections, lessons, task state) must be rebuilt after compaction via infrastructure, not re-learned.

## Context

> [!warning] When does this lesson apply?
>
> - Your agent runs long sessions (60+ minutes, 300+ tool calls)
> - Your agent has been corrected during the session and improved
> - Context pressure triggers automatic compaction
> - You rely on in-session corrections to maintain quality

## Insight

> [!tip] What Survives Compaction vs What Dies
>
> | Survives | Dies |
> |----------|------|
> | CLAUDE.md (loaded fresh) | In-session corrections |
> | Hook configurations | Behavioral adjustments from feedback |
> | Files on disk | Mental model of "what I learned this session" |
> | Memories (.claude/memory) | Accumulated context about task progress |
> | Infrastructure enforcement | Soft compliance improvements |
>
> **The mechanism:** Compaction summarizes the conversation into a shorter representation. Corrections like "don't use find, use Glob" or "you missed the strict checker — always run pnpm tsgo" exist as conversation turns. After compaction, those turns become a brief summary. The SPECIFICITY that made the correction effective is lost.

OpenArms solved this with a `post-compact.sh` hook (29 lines) that calls `build-reinstruction.cjs` to read the FULL task state from `.openarms/` files and re-inject it as additional context. The hook fires automatically after every compaction event. Without it, the agent loses: current stage, task requirements, prior stage artifacts, model config, and all accumulated corrections.

OpenFleet solves it differently — the immune system's PRUNE response kills the session entirely and regrows fresh. No attempt to preserve context across compaction. Clean restart with full state from orchestrator files.

## Evidence

> [!bug]- OpenArms: "All Old Illnesses Return" After Compaction
>
> CLAUDE.md learning (v10): "After compaction, re-read ALL memories first — all old illnesses return after context compaction."
>
> The agent was corrected 3 times on the same issue. Each correction worked for the remainder of that context window. After compaction, the correction was gone and the agent repeated the exact same mistake. The correction existed only as a conversation turn, not as infrastructure.

> [!success] Post-Compact Hook as Infrastructure Solution
>
> OpenArms `post-compact.sh` (29 lines):
> 1. Checks `.openarms/methodology-enforced` flag
> 2. Calls `build-reinstruction.cjs` which reads ALL state files from `.openarms/`
> 3. Returns the full task state as `additionalContext` in the hook response
>
> State rebuilt from files: current-stage, current-task-id, stage-files.log, required-stages.json, stages-completed.json, current-model-config.json.
>
> This converts ephemeral corrections into persistent state — the hook doesn't need to know WHAT was corrected, it rebuilds the ENTIRE context from authoritative files.

> [!success] OpenFleet: PRUNE as Clean Restart
>
> When the immune system detects 3+ corrections on the same issue, it doesn't try to preserve context. It PRUNEs: kills the session, regrows fresh. All in-session memory is lost — but the orchestrator's files contain the authoritative state.
>
> This is a more aggressive solution. The tradeoff: work in progress may be lost. The benefit: no accumulated state corruption.

## Applicability

> [!abstract] Compaction Defense Strategies
>
> | Strategy | Mechanism | When to Use |
> |----------|-----------|-------------|
> | **Post-compact hook** | Rebuild context from files after every compaction | Solo agent, long sessions, corrections are frequent |
> | **Persistent state files** | Task state on disk, not in context only | Any agent that runs more than 30 minutes |
> | **PRUNE and regrow** | Kill session on repeated failures, start fresh | Fleet with orchestrator that tracks state externally |
> | **Session pressure monitoring** | Detect high context usage, proactively compact or restart | Harness-managed agents with budget awareness |

> [!warning] Self-Check — Am I Vulnerable to Compaction Reset?
>
> 1. Does my agent store task state ONLY in conversation context, or also in files?
> 2. Do I have a post-compact hook that rebuilds state?
> 3. If the agent has been corrected 3 times this session, will those corrections survive compaction?
> 4. What is my compaction threshold, and do I know when it fires?

## Relationships

- DERIVED FROM: [[Infrastructure Enforcement Proves Instructions Fail]]
- DERIVED FROM: [[Agent Failure Taxonomy — Six Classes of Behavioral Failure]]
- RELATES TO: [[Three Lines of Defense — Immune System for Agent Quality]]
- RELATES TO: [[Enforcement Hook Patterns]]
- FEEDS INTO: [[Model: Claude Code]]

## Backlinks

[[Infrastructure Enforcement Proves Instructions Fail]]
[[Agent Failure Taxonomy — Six Classes of Behavioral Failure]]
[[Three Lines of Defense — Immune System for Agent Quality]]
[[Enforcement Hook Patterns]]
[[Model: Claude Code]]
[[Harness-Owned Loop — Deterministic Agent Execution]]
