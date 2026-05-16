---
title: "Synthesis — Claude Code Hooks Reference — 26 Lifecycle Events, 4 Handler Types"
aliases:
  - "Synthesis — Claude Code Hooks Reference"
  - "Claude Code Hooks — Lifecycle Events"
type: source-synthesis
domain: claude-code
status: synthesized
confidence: high
maturity: seed
created: 2026-05-15
updated: 2026-05-15
sources:
  - id: claude-code-hooks-reference
    type: documentation
    url: "https://code.claude.com/docs/en/hooks"
    file: raw/articles/claude-code-hooks-reference.md
    ingested: 2026-04-09
tags:
  - claude-code
  - hooks
  - lifecycle
  - automation
  - agent-control
  - mcp
  - harness-engineering
  - permissions
---

# Synthesis — Claude Code Hooks Reference — 26 Lifecycle Events, 4 Handler Types

> [!info] Reference Card
> **Source:** https://code.claude.com/docs/en/hooks
> **Ingest date:** 2026-04-09
> **Raw file:** `raw/articles/claude-code-hooks-reference.md` (39 lines)

## Summary

Claude Code's hooks system provides 26 lifecycle events that allow external handlers to observe, intercept, modify, and control agent behavior throughout a session. Four handler types (command, http, prompt, agent) support diverse integration patterns. A key capability is the "reverse hook" pattern—Stop and TeammateIdle hooks that fire on completion and can *prevent* the agent from stopping, enabling continuous autonomous operation. Hooks are composable via matchers, `if` filters, and scope hierarchy (user → project → local → plugins → policies), making them the primary extensibility surface for Claude Code harness engineering.

## Key Insights

### 26 Lifecycle Events — Three Categories

**Initiation Gates** (can block/modify):
- `SessionStart`, `UserPromptSubmit`, `InstructionsLoaded`, `ConfigChange`, `CwdChanged`, `FileChanged`
- `TaskCreated`, `TaskCompleted` — task-lifecycle control points
- `PreToolUse`, `PermissionRequest` — pre-execution gates; support `updatedInput` to rewrite tool calls
- `PostToolUse`, `PostToolUseFailure`, `PermissionDenied` — post-execution observers

**Subagent Events**:
- `SubagentStart`, `SubagentStop` — coordination points for multi-agent hierarchies

**Termination/Completion** (the "reverse" hooks):
- `Stop`, `StopFailure` — fire when Claude finishes. Exiting 2 or returning `decision:block` *prevents* the agent from stopping and forces it to continue
- `TeammateIdle` — fires when a teammate agent is idle; can prevent idling, keeping it working
- `PreCompact`, `PostCompact` — compact lifecycle control
- `Elicitation`, `ElicitationResult` — MCP elicitation control
- `Notification`, `SessionEnd` — passive observation

### 4 Handler Types

| Type | Description | Key Use Case |
|------|-------------|--------------|
| `command` | Shell script, receives JSON on stdin | Side effects, blocking (async supported) |
| `http` | POST to endpoint | Remote integrations, webhooks |
| `prompt` | Single-turn LLM evaluation | Policy enforcement via model judgment |
| `agent` | Subagent with tool access | Complex decisions, multi-step reactions |

### Blocking and Modification Capabilities

- **Block actions**: `PreToolUse`, `PermissionRequest`, `UserPromptSubmit`, `Stop`, `TaskCreated`, `TaskCompleted`, `ConfigChange` — exit code 2 or JSON `decision:block`
- **Modify tool input**: `PreToolUse`, `PermissionRequest` — return `updatedInput` to rewrite before execution
- **Inject context**: `SessionStart`, `UserPromptSubmit`, `PreToolUse`, `PostToolUse`, `SubagentStart` — `additionalContext` field
- **Set env vars**: `SessionStart`, `CwdChanged`, `FileChanged` — via `CLAUDE_ENV_FILE`

### Composition System

- **Matchers**: exact string, pipe-separated list, JavaScript regex — applied to tool names, event types
- **MCP tool matching**: `mcp__server__tool` pattern for fine-grained MCP control
- **`if` filters**: permission rule syntax (`Bash(rm *)`, `Edit(*.ts)`) for conditional hook application
- **Deduplication**: identical handlers execute only once per event
- **Scope hierarchy**: user settings → project settings → local settings → plugins → policies

### The Reverse Hook Pattern

The Stop and TeammateIdle events represent an inversion of typical hook semantics: rather than gating initiation, they gate *completion*. A Stop hook that blocks exit forces the agent into continuous operation — a critical primitive for autonomous harness construction. This pattern is not available in any earlier CLI tool or IDE integration.

## Relationships

BUILDS ON [[wiki/sources/claude-code/src-harness-engineering.md]] — hooks are the extensibility layer that harness engineering patterns depend on; the Stop-block pattern directly enables long-running harness loops.

COMPLEMENTS [[wiki/sources/src-claude-agent-sdk-and-managed-agents.md]] — the Agent SDK manages sessions programmatically; hooks provide the within-session event interception layer; together they cover the full harness surface.

RELATES TO [[wiki/sources/tools-integration/src-cloudflare-agent-memory-rrf-retrieval-context-rot-solution-2026-04-17.md]] — the PostCompact hook (`PostCompact`) signals when context was compressed, which is the trigger point for memory-retrieval injection patterns.

FEEDS INTO [[wiki/domains/ai-agents/agent-control-surfaces.md]] — hooks are one of three major control surfaces for AI agents (hooks / MCP / system prompt); this reference defines the full hook surface.
