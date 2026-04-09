---
title: "Model Guide: Claude Code"
type: learning-path
domain: cross-domain
layer: spine
status: synthesized
confidence: high
maturity: growing
created: 2026-04-09
updated: 2026-04-09
sources: []
tags: [claude-code, model-guide, learning-path, ai-agent, skills, hooks, context-management, harness-engineering, spine]
---

# Model Guide: Claude Code

## Summary

The Claude Code model describes how Anthropic's CLI coding agent works as an extensible runtime, not just an interactive chat tool. It covers the agent's tool-use loop, its three-tier extension system (Skills, Hooks, MCP), and the context management discipline that determines whether it succeeds or fails on complex tasks. This model is the execution engine behind everything in this ecosystem: the wiki's ingestion pipeline, every OpenFleet agent, and the primary human-to-system interface. Mastering this model means knowing how to extend Claude Code correctly, how to constrain it safely, and how to keep its context window healthy across long sessions.

## Prerequisites

- Basic familiarity with terminal-based AI tools
- Understanding that Claude Code is an agent loop (decides → calls tools → evaluates → repeats), not a one-shot Q&A interface
- No prior knowledge of MCP, hooks, or skills required — this model covers all three

## Sequence

### L1 — Primary Sources

These sources establish the empirical baseline. Read them to understand where the insights originate.

- `wiki/sources/src-karpathy-claude-code-10x.md` — Andrej Karpathy's walkthrough of Claude Code patterns; origin of the skills-as-compounding-knowledge insight
- `wiki/sources/src-shanraisshan-claude-code-best-practice.md` — Anthropic's official best practices repo covering the Command-Agent-Skill hierarchy
- `wiki/sources/src-token-hacks-claude-code.md` — 18 token hacks; origin of the context degradation curve data (40%/60%/80% thresholds)
- `wiki/sources/src-harness-engineering-article.md` — The harness engineering model; origin of stage-gating via hooks

### L2 — Core Concepts

Read in this order. Each page builds on the previous.

1. **Claude Code** (`wiki/domains/ai-agents/claude-code.md`) — What the agent IS: tool-use loop, extension mechanisms, subagent parallelism, CLAUDE.md as project brain. Start here.
2. **Claude Code Best Practices** (`wiki/domains/ai-agents/claude-code-best-practices.md`) — The Command-Agent-Skill hierarchy; plan-first discipline; CLAUDE.md as index not encyclopedia; hooks as automation glue.
3. **Claude Code Context Management** (`wiki/domains/ai-agents/claude-code-context-management.md`) — The context window as the primary constraint; degradation curve; compaction, subagent isolation, and targeted reads as mitigations.
4. **Claude Code Skills** (`wiki/domains/ai-agents/claude-code-skills.md`) — Skills as plain markdown instruction sets; two-phase operation (setup then use); progressive disclosure folder structure; context forking.
5. **Hooks Lifecycle Architecture** (`wiki/domains/ai-agents/hooks-lifecycle-architecture.md`) — 26 events across 7 categories; blocking pattern (PreToolUse); reverse-hook pattern (Stop/TeammateIdle); context injection; stage-gate enforcement.
6. **Per-Role Command Architecture** (`wiki/domains/ai-agents/per-role-command-architecture.md`) — Commands as lightweight triggers that invoke skills; role-segmented palettes; the Plannotator pattern (command + hook pair).
7. **Harness Engineering** (`wiki/domains/ai-agents/harness-engineering.md`) — The full harness concept: CLAUDE.md + skills + hooks + commands + subagents working as a coordinated system.

### L3 — Comparisons

- **Claude Code Scheduling** (`wiki/domains/ai-agents/claude-code-context-management.md`) — How to structure autonomous sessions that run without human babysitting.
- **MCP Integration Architecture** (`wiki/domains/tools-and-platforms/mcp-integration-architecture.md`) — How MCP servers fit into the extension model; when MCP is the right choice vs CLI.

### L4 — Lessons (Validated Insights)

- **CLI Tools Beat MCP for Token Efficiency** (`wiki/lessons/cli-tools-beat-mcp-for-token-efficiency.md`) — 12x cost differential; schema noise vs targeted loading; when to prefer each.
- **Context Management Is the Primary Lever** (`wiki/lessons/lesson-convergence-on-src-karpathy-claude-code-10x.md`) — Context discipline is the single biggest lever on Claude Code output quality.
- **Skills Architecture Is Dominant** (`wiki/lessons/lesson-convergence-on-claude-code-skills.md`) — Skills are the dominant extension pattern; MCP and hooks serve specific narrow roles.
- **Always Plan Before Executing** (`wiki/lessons/always-plan-before-executing.md`) — The planning step is not optional; it is the primary lever for avoiding token-wasting wrong paths.

### L5 — Patterns (Structural Templates)

- **Context-Aware Tool Loading** (`wiki/patterns/context-aware-tool-loading.md`) — Defer all tool schema loading until actually needed; never pre-load at session start.
- **Plan Execute Review Cycle** (`wiki/patterns/plan-execute-review-cycle.md`) — The convergent workflow structure across all successful Claude Code frameworks.

### L6 — Decisions (Resolved Choices)

- **MCP vs CLI for Tool Integration** (`wiki/decisions/mcp-vs-cli-for-tool-integration.md`) — Default to CLI+Skills for operational tasks; MCP for external service bridges.

## Outcomes

After completing this learning path you will understand:

- How Claude Code's tool-use loop works and why it is fundamentally different from a chatbot
- The three-tier extension model (Skills → Hooks → MCP) and when to use each tier
- Why context management is the primary performance lever and what the 40%/60%/80% degradation thresholds mean in practice
- How to structure a Claude Code harness: CLAUDE.md as routing table, skills for task knowledge, hooks for runtime enforcement
- Why CLI+Skills beats MCP for project-internal tooling and when MCP genuinely wins
- How to enforce stage-gate constraints at the infrastructure level using PreToolUse hooks
- How commands, skills, and hooks compose into a coordinated per-role workflow system

## Relationships

- FEEDS INTO: Model Guide: Skills + Commands + Hooks
- FEEDS INTO: Model Guide: MCP + CLI Integration
- ENABLES: Model Guide: LLM Wiki
- ENABLES: Model Guide: Ecosystem Architecture
- RELATES TO: Model Guide: Methodology
- BUILDS ON: Claude Code
- BUILDS ON: Claude Code Skills
- BUILDS ON: Hooks Lifecycle Architecture

## Backlinks

[[Model Guide: Skills + Commands + Hooks]]
[[Model Guide: MCP + CLI Integration]]
[[Model Guide: LLM Wiki]]
[[Model Guide: Ecosystem Architecture]]
[[Model Guide: Methodology]]
[[Claude Code]]
[[Claude Code Skills]]
[[Hooks Lifecycle Architecture]]
[[Model Guide: Second Brain]]
