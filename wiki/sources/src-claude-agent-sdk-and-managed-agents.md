---
title: "Synthesis — Claude Agent SDK and Managed Agents"
type: source-synthesis
domain: ai-agents
status: synthesized
confidence: high
maturity: seed
created: 2026-04-14
updated: 2026-04-14
sources:
  - id: agent-sdk-python-reference
    type: documentation
    url: "https://code.claude.com/docs/en/agent-sdk/python"
  - id: managed-agents-tools-reference
    type: documentation
    url: "https://platform.claude.com/docs/en/managed-agents/tools"
tags:
  - ai-agents
  - claude-agent-sdk
  - managed-agents
  - orchestration
  - tool-use
  - permissions
  - hooks
  - mcp
  - agent-definition
  - harness-engineering
---

# Synthesis — Claude Agent SDK and Managed Agents

## Summary

The Claude Agent SDK (`claude-agent-sdk` Python package) and the Managed Agents API (`managed-agents-2026-04-01` beta) are two complementary interfaces for embedding Claude-powered agents into applications. The SDK exposes a local subprocess model with two interaction patterns — stateless `query()` and stateful `ClaudeSDKClient` — backed by a large configuration surface (`ClaudeAgentOptions`) governing tools, permissions, hooks, thinking, effort, and named sub-agents. Managed Agents is the API-side complement, providing a hosted tool execution layer with eight built-in tools and a contract for custom tool integration. Together they define the complete programmatic surface through which harness engineers interact with Claude at runtime.

> [!info] Source Reference
> | Attribute | Value |
> |-----------|-------|
> | Source 1  | Claude Agent SDK Python Reference (`https://code.claude.com/docs/en/agent-sdk/python`) |
> | Source 2  | Managed Agents Tools Reference (`https://platform.claude.com/docs/en/managed-agents/tools`) |
> | Type      | Official Anthropic documentation — SDK reference + API reference |
> | Date      | Ingested 2026-04-14 |
> | Key claim | Programmatic agent control requires choosing the right interaction pattern (stateless vs stateful) before any tool or permission wiring |

## Key Insights

**1. Two interaction patterns serve fundamentally different use cases.**

`query()` creates a new session per call and returns an `AsyncIterator[Message]`. It is appropriate for one-off agent tasks where state continuity is neither needed nor wanted. `ClaudeSDKClient` maintains a conversation session across multiple `.query()` calls, supports interrupts, file rewinding, and live MCP server management. Choosing between them is the first architectural decision in any harness — conflating them creates either resource leaks (sessions left open) or context loss (session closed too early). This mirrors the stateless-vs-stateful split that appears in every distributed system design.

**2. `ClaudeAgentOptions` is the entire programmatic configuration surface in one object.**

The options object has twelve distinct concern areas: `tools`, `allowed_tools`, `system_prompt`, `mcp_servers`, `permission_mode`, `model`, `max_turns`, `max_budget_usd`, `can_use_tool`, `hooks`, `agents`, `thinking`, `effort`, `setting_sources`, `sandbox`, and `plugins`. This single object is the complete contract between the harness and the agent runtime. Understanding each field and its interaction effects is the central competency of harness engineering — not prompt writing.

**3. The eight built-in Managed Agents tools are identical to what Claude Code uses internally.**

`bash`, `read`, `write`, `edit`, `glob`, `grep`, `web_fetch`, `web_search` — these are the same tools exposed to Claude Code's internal execution engine and to this wiki's pipeline tooling. This is not a coincidence: Anthropic has standardized the agent execution surface. When you configure a Managed Agents session, you are configuring the same action vocabulary Claude Code operates with. Disabling `web_fetch` and `web_search` creates a sandboxed file-only agent; disabling `write` and `edit` creates a read-only auditing agent.

**4. The permission system is a five-mode spectrum from fully supervised to fully autonomous.**

`default` — standard approval flow. `acceptEdits` — auto-approve file edits only. `plan` — plan before acting, no execution without review. `dontAsk` — auto-approve everything in `allowed_tools`. `bypassPermissions` — unrestricted. The `can_use_tool` callback is a sixth escape hatch: a Python function called before every tool execution, returning `PermissionResultAllow` (optionally with mutated input) or `PermissionResultDeny` (with interrupt signal). This enables context-aware dynamic permissions that no static mode can replicate — for example, allowing `bash` only when the working directory matches a whitelist.

**5. Ten hook event types map directly onto this wiki's hook lifecycle model.**

`PreToolUse`, `PostToolUse`, `PostToolUseFailure`, `UserPromptSubmit`, `Stop`, `SubagentStop`, `PreCompact`, `Notification`, `SubagentStart`, `PermissionRequest`. These are not generic lifecycle hooks — they are instrumentation points on the agent's complete execution cycle. `PreCompact` is particularly notable: it fires before the context is trimmed, allowing the harness to inject a summary or checkpoint before memory is lost. A harness that wires hooks at all ten points has complete observability over agent behavior.

**6. `AgentDefinition` enables named sub-agents with isolated capability profiles.**

The `agents` field in `ClaudeAgentOptions` accepts a dict of `AgentDefinition` objects, each specifying `description`, `prompt`, `tools`, `model` (sonnet/opus/haiku/inherit), `skills`, `memory` scope, and `mcpServers`. This enables multi-agent topologies entirely within a single SDK session — a coordinator agent can delegate to a specialized sub-agent with a smaller tool set and a cheaper model, implementing tier-based agent economics without external orchestration infrastructure.

**7. Custom tools follow a three-step contract: schema → request → result.**

The Managed Agents API pattern is: declare a `custom` type tool with `name`, `description`, and `input_schema` on agent creation; Claude emits a structured tool-use request during session execution; the application code runs the operation and sends the result back. The SDK side uses the `@tool` decorator and `create_sdk_mcp_server()` to create an in-process MCP server that Claude sees natively. Both patterns share the same underlying contract — JSON Schema input validation, structured result return — but differ in transport layer (in-process MCP vs API round-trip).

**8. `effort` and `thinking` are orthogonal quality knobs with cost implications.**

`effort` (`low`/`medium`/`high`/`max`) controls how hard the model tries within its token budget. `thinking` (`adaptive`/`enabled`/`disabled`) controls whether extended chain-of-thought reasoning is activated. Together they define the quality-cost operating point for a given agent invocation. Running a cost-capped batch task at `effort: low, thinking: disabled` is architecturally different from a production critic agent at `effort: high, thinking: adaptive`. These fields belong in harness configuration, not ad-hoc prompt modification.

## Deep Analysis

### Interaction Patterns — query() vs ClaudeSDKClient

The SDK presents two entry points with distinct operational semantics:

| Feature              | `query()`               | `ClaudeSDKClient`               |
|----------------------|-------------------------|---------------------------------|
| Session lifecycle    | New session per call    | Reuses same session             |
| Conversation memory  | Single exchange         | Accumulates across exchanges    |
| Interrupt support    | No                      | Yes — `.interrupt()`            |
| Continue a chat      | No                      | Yes — `.query()` again          |
| File rewind          | No                      | Yes — `.rewind_files()`         |
| MCP runtime control  | No                      | Yes — toggle/reconnect servers  |
| Async iterator       | Yes — via `async for`   | Yes — via `.receive_messages()` |
| Use case             | Pipelines, one-shot CI  | IDE integration, long sessions  |

`query()` accepts either a plain `str` prompt or an `AsyncIterable[dict]` for streaming multi-part prompts. This makes it suitable for pipeline stages where the prompt is constructed dynamically from earlier outputs.

`ClaudeSDKClient` is a context manager (`async with ClaudeSDKClient() as client:`) that maintains the subprocess connection. `.reconnect_mcp_server()` and `.toggle_mcp_server()` allow runtime-hot MCP reconfiguration without restarting the agent — critical for long-running harness scenarios where a tool server may restart independently.

### ClaudeAgentOptions — Full Configuration Surface

The options object is not merely a convenience wrapper — it is the full API between the harness and the SDK runtime. Every field represents an explicit policy decision:

**Tool surface:**
- `tools` — which tool preset or set of tools is active
- `allowed_tools` — list of tools that are auto-approved without permission prompts
- `mcp_servers` — list of `McpStdioServerConfig`, `McpSSEServerConfig`, or `McpHttpServerConfig` objects

**Execution control:**
- `model` — which Claude model to use
- `max_turns` — circuit breaker on runaway agent loops
- `max_budget_usd` — hard cost cap per session
- `effort` — `low`/`medium`/`high`/`max`
- `thinking` — `ThinkingConfig` (adaptive/enabled with budget_tokens/disabled)

**Permission and safety:**
- `permission_mode` — one of five modes (see Permission System section)
- `can_use_tool` — dynamic per-tool Python callback

**Observability and control:**
- `hooks` — list of `HookMatcher` objects (matcher + callback + timeout)

**Multi-agent topology:**
- `agents` — dict of named `AgentDefinition` objects

**Context and settings:**
- `system_prompt` — custom or preset system prompt
- `setting_sources` — which config files to load (`user`, `project`, `local`)
- `sandbox` — sandbox execution settings
- `plugins` — plugin configurations

The key insight is that `ClaudeAgentOptions` is instantiated once per session and passed to either `query()` or the `ClaudeSDKClient` constructor. There is no mid-session mutation of the options object — runtime changes require the `ClaudeSDKClient` methods (`.set_permission_mode()`, `.set_model()`) which are separate from the options schema.

### Built-in Toolset — The Eight Standard Tools

Managed Agents provides an `agent_toolset_20260401` bundle. All eight tools are enabled by default when the toolset is included:

| Tool name    | Operation                              |
|--------------|----------------------------------------|
| `bash`       | Execute bash commands in a shell session |
| `read`       | Read a file from the local filesystem  |
| `write`      | Write a file to the local filesystem   |
| `edit`       | Perform string replacement in a file   |
| `glob`       | Fast file pattern matching             |
| `grep`       | Text search using regex patterns       |
| `web_fetch`  | Fetch content from a URL               |
| `web_search` | Search the web for information         |

Selective configuration uses a `default_config.enabled: false` plus an explicit list pattern to create whitelisted-only toolsets. This is the pattern for locked-down agents (e.g., a read-only auditor only gets `read`, `glob`, `grep`).

These eight tools map exactly to the tools exposed in Claude Code's internal execution and to this wiki's own pipeline tooling. The SDK-level `@tool` decorator and `create_sdk_mcp_server()` function allow custom tools to appear in the same namespace, making the tool surface extensible to any Python function.

### Custom Tool Contract

The Managed Agents API custom tool pattern:

1. **Declaration at agent creation time** — `type: custom`, `name`, `description` (3-4+ sentences recommended), `input_schema` (JSON Schema object)
2. **Claude emits structured `ToolUseBlock`** — contains `tool_name` and `input` dict validated against the declared schema
3. **Application executes the operation** — any Python function, external API call, database query
4. **Application returns `ToolResultBlock`** — success or error, serialized content

Best practices from the Managed Agents documentation:
- **Extremely detailed descriptions** increase tool selection accuracy more than any other factor
- **Consolidate related operations** into one tool with an `action` parameter rather than creating parallel tools
- **Namespace by resource** (`db_query`, `storage_read`, `cache_invalidate`) to avoid name collisions
- **Return only high-signal data** — Claude's next decision depends on the result; irrelevant fields create noise

The SDK-side equivalent uses `@tool(name, description, input_schema)` decorator to register a Python function as an MCP tool, then `create_sdk_mcp_server()` to expose the collection as an in-process MCP server. This server is passed as a `McpStdioServerConfig` (pointing to the in-process binary) in `ClaudeAgentOptions.mcp_servers`.

### Permission System — Five Modes + Dynamic Callback

The five permission modes represent increasing levels of agent autonomy:

| Mode                | Behavior                                                         |
|---------------------|------------------------------------------------------------------|
| `default`           | Standard approval flow — prompts for each non-whitelisted tool  |
| `acceptEdits`       | Auto-approve file write/edit operations                          |
| `plan`              | Generate plan first; no execution without explicit review        |
| `dontAsk`           | Auto-approve all tools in `allowed_tools` list                  |
| `bypassPermissions` | Unrestricted — all tools, no approval prompts                   |

The `can_use_tool` callback is orthogonal to these modes — it fires regardless of the mode and can override the mode's default behavior. Signature:

```python
async def can_use_tool(tool_name: str, tool_input: dict) -> PermissionResultAllow | PermissionResultDeny
```

`PermissionResultAllow` can return an `updated_input` dict, enabling input sanitization (strip dangerous flags, normalize paths) before execution. `PermissionResultDeny` accepts a `message` string and an optional `interrupt` bool — when `interrupt=True`, the agent session halts rather than continuing with a permission error.

This is the mechanism by which harness engineers implement policy-as-code on agent tool use: whitelist directories, validate URLs, enforce naming conventions, log every tool call to audit infrastructure — all in a single Python callback function.

### Hook System — Ten Lifecycle Events

Hook events with their architectural significance:

| Event                | Fires when                                            | Harness use case                              |
|----------------------|-------------------------------------------------------|-----------------------------------------------|
| `PreToolUse`         | Before any tool is executed                           | Audit logging, dry-run mode, input validation |
| `PostToolUse`        | After successful tool execution                       | Result caching, metrics, follow-up actions    |
| `PostToolUseFailure` | After tool execution fails                            | Error escalation, retry logic, alerting       |
| `UserPromptSubmit`   | When user submits a prompt                            | Input sanitization, rate limiting             |
| `Stop`               | When agent session stops normally                     | Cleanup, result persistence, cost reporting   |
| `SubagentStart`      | When a named sub-agent is invoked                     | Sub-agent telemetry, capability audit         |
| `SubagentStop`       | When a named sub-agent completes                      | Sub-agent result aggregation                  |
| `PreCompact`         | Before context window is compacted                    | Checkpoint injection, summary generation      |
| `Notification`       | When agent emits a notification                       | User-facing alerting, monitoring integration  |
| `PermissionRequest`  | When agent requests a permission not yet decided      | Escalation routing, approval workflows        |

Hooks are defined via `HookMatcher` objects with three fields: `matcher` (pattern to match tool name or event type), `callback` (Python async function), and `timeout` (max execution time). Multiple matchers can fire on the same event. The order of execution follows list order in `ClaudeAgentOptions.hooks`.

`PreCompact` is architecturally the most significant hook for long-running agents. Context compaction discards older turns to make room for new ones — a `PreCompact` hook can inject a structured summary or a checkpoint payload that survives the compaction, preserving semantic continuity even when the full transcript is lost.

### AgentDefinition — Named Sub-Agents

```python
@dataclass
class AgentDefinition:
    description: str          # Human-readable purpose statement
    prompt: str               # System prompt for this sub-agent
    tools: list[str] | None   # Tool whitelist (subset of parent's tools)
    model: Literal["sonnet", "opus", "haiku", "inherit"] | None
    skills: list[str] | None  # Skill file references
    memory: Literal["user", "project", "local"] | None
    mcpServers: list[str | dict] | None  # MCP servers scoped to sub-agent
```

Named agents create a hierarchical capability model within a single SDK session:
- A coordinator (using `opus` or `sonnet`) dispatches to specialized workers
- Workers can be `haiku`-class with restricted tool sets, reducing cost per sub-task
- `memory` scope controls which CLAUDE.md/settings files the sub-agent reads
- Sub-agent `mcpServers` are independent of the parent's server list

This is the SDK's answer to multi-agent orchestration. Rather than spinning up separate processes or using an external orchestration framework, the parent agent maintains full visibility into sub-agent lifecycle via `SubagentStart` / `SubagentStop` hooks.

### Message Types and Result Handling

The SDK streams six message types:

`UserMessage | AssistantMessage | SystemMessage | ResultMessage | StreamEvent | RateLimitEvent`

`ResultMessage` is the terminal message of a session, containing:
- `subtype` — `"success"` or `"error"`
- `duration_ms` — wall-clock session time
- `is_error` — boolean flag
- `num_turns` — total turns consumed
- `session_id` — for post-hoc retrieval
- `total_cost_usd` — actual USD cost (for budget accounting)
- `result` — final text output
- `structured_output` — typed output if the agent was configured for structured responses

Harness engineers should always collect the `ResultMessage` and log `total_cost_usd` and `num_turns` — these are the primary observability signals for detecting runaway agents, cost anomalies, and task complexity drift over time.

Content blocks within messages are typed:
`TextBlock | ThinkingBlock | ToolUseBlock | ToolResultBlock`

`ThinkingBlock` is present only when `thinking` is `adaptive` or `enabled`. Harness code should filter these out in production telemetry (they contain internal reasoning, not user-facing content) while preserving them for debugging sessions.

### MCP Server Configuration Options

Three transport types for connecting external tool servers:

| Config Type           | Transport    | Use case                                      |
|-----------------------|--------------|-----------------------------------------------|
| `McpStdioServerConfig` | Local process | In-process tools, local binaries              |
| `McpSSEServerConfig`  | Server-Sent Events | Remote server, streaming required          |
| `McpHttpServerConfig` | HTTP          | Remote server, request-response sufficient    |

All three share `url` or `command`/`args` fields plus optional `headers` dict for auth. The `ClaudeSDKClient.reconnect_mcp_server()` and `toggle_mcp_server()` methods operate on server names defined in these configs, enabling runtime MCP topology changes.

### Ecosystem Integration — Relation to Our Harness

This SDK is the programmatic foundation that underlies every harness engineering pattern in this wiki. Specifically:

- The `hooks` system is the SDK realization of the hook lifecycle model (`PreToolUse` → `PostToolUse` → etc.) documented in our hooks architecture
- `AgentDefinition` sub-agents implement the subagent isolation pattern
- `permission_mode: plan` implements the "plan-first" harness posture
- `can_use_tool` implements policy-as-code at the tool level
- `max_turns` + `max_budget_usd` implement circuit breakers against runaway agents
- `effort` + `thinking` are the quality knobs that separate development vs production agent configurations
- The eight built-in tools map 1:1 to the tools Claude Code uses — knowing the toolset is knowing the agent's full action vocabulary

## Open Questions

- What is the versioning strategy for `agent_toolset_20260401`? Will a `20261001` toolset appear, and what migration path exists?
- How does `setting_sources: ["user", "project", "local"]` interact with `ClaudeAgentOptions` when both specify conflicting values for the same field?
- What is the maximum number of named `AgentDefinition` objects supported per session before context overhead becomes prohibitive?
- How does `PreCompact` interact with structured output requirements — can a compacted session still produce a valid `structured_output` in the final `ResultMessage`?
- Is `bypassPermissions` mode available in API-hosted Managed Agents sessions, or is it SDK-only?

## Relationships

- RELATES TO: [[model-claude-code|Model — Claude Code]]
- RELATES TO: [[model-skills-commands-hooks|Model — Skills, Commands, and Hooks]]
- RELATES TO: [[src-anthropic-building-effective-ai-agents|Synthesis — Anthropic — Building Effective AI Agents — 5 Canonical Workflow Patterns]]
- RELATES TO: [[src-anthropic-effective-harnesses-long-running-agents|Synthesis — Anthropic — Effective Harnesses for Long-Running Agents]]
- FEEDS INTO: [[harness-engineering-is-the-dominant-performance-lever|Harness Engineering Is the Dominant Performance Lever]]

## Backlinks

[[model-claude-code|Model — Claude Code]]
[[model-skills-commands-hooks|Model — Skills, Commands, and Hooks]]
[[src-anthropic-building-effective-ai-agents|Synthesis — Anthropic — Building Effective AI Agents — 5 Canonical Workflow Patterns]]
[[src-anthropic-effective-harnesses-long-running-agents|Synthesis — Anthropic — Effective Harnesses for Long-Running Agents]]
[[harness-engineering-is-the-dominant-performance-lever|Harness Engineering Is the Dominant Performance Lever]]
[[src-pydantic-ai-typed-agent-framework|Synthesis — Pydantic AI: Typed Agent Framework]]
