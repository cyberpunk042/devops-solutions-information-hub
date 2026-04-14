# Claude Agent SDK — Python Reference

Source: https://code.claude.com/docs/en/agent-sdk/python
Ingested: 2026-04-14
Type: documentation

---

## Installation

```bash
pip install claude-agent-sdk
```

## Core Functions

### `query()`
Creates a new session for each interaction. Returns an `AsyncIterator[Message]` that yields messages as they arrive.

```python
async def query(
    *,
    prompt: str | AsyncIterable[dict[str, Any]],
    options: ClaudeAgentOptions | None = None,
    transport: Transport | None = None
) -> AsyncIterator[Message]
```

Use when: One-off questions, independent tasks, fresh starts each time.

### `tool()` Decorator
Defines MCP tools with type safety.

```python
def tool(
    name: str,
    description: str,
    input_schema: type | dict[str, Any],
    annotations: ToolAnnotations | None = None
) -> Callable
```

### `create_sdk_mcp_server()`
Creates an in-process MCP server for custom tools.

```python
def create_sdk_mcp_server(
    name: str,
    version: str = "1.0.0",
    tools: list[SdkMcpTool[Any]] | None = None
) -> McpSdkServerConfig
```

### `list_sessions()` / `get_session_messages()` / `get_session_info()`
Session management — list, retrieve messages, get metadata. Synchronous.

### `rename_session()` / `tag_session()`
Session metadata modification.

## ClaudeSDKClient Class

Maintains conversation session across multiple exchanges.

```python
class ClaudeSDKClient:
    async def connect(self, prompt=None) -> None
    async def query(self, prompt, session_id="default") -> None
    async def receive_messages(self) -> AsyncIterator[Message]
    async def receive_response(self) -> AsyncIterator[Message]
    async def interrupt(self) -> None
    async def set_permission_mode(self, mode: str) -> None
    async def set_model(self, model: str | None = None) -> None
    async def rewind_files(self, user_message_id: str) -> None
    async def get_mcp_status(self) -> McpStatusResponse
    async def reconnect_mcp_server(self, server_name: str) -> None
    async def toggle_mcp_server(self, server_name: str, enabled: bool) -> None
    async def stop_task(self, task_id: str) -> None
    async def disconnect(self) -> None
```

Context manager support: `async with ClaudeSDKClient() as client:`

### query() vs ClaudeSDKClient

| Feature | query() | ClaudeSDKClient |
|---------|---------|-----------------|
| Session | New each time | Reuses same |
| Conversation | Single exchange | Multiple exchanges |
| Interrupts | No | Yes |
| Continue Chat | No | Yes |
| Use Case | One-off tasks | Continuous conversations |

## ClaudeAgentOptions Configuration

Key fields:
- `tools`: Tool configuration or preset
- `allowed_tools`: Auto-approve list
- `system_prompt`: Custom or preset
- `mcp_servers`: MCP server configs
- `permission_mode`: "default", "acceptEdits", "plan", "dontAsk", "bypassPermissions"
- `model`: Claude model to use
- `max_turns`: Turn limit
- `max_budget_usd`: Cost cap
- `can_use_tool`: Custom permission callback
- `hooks`: Event hooks (PreToolUse, PostToolUse, Stop, etc.)
- `agents`: Named agent definitions
- `thinking`: Extended thinking config (adaptive/enabled/disabled)
- `effort`: "low", "medium", "high", "max"
- `setting_sources`: ["user", "project", "local"]
- `sandbox`: Sandbox settings
- `plugins`: Plugin configs

## Message Types

Message = UserMessage | AssistantMessage | SystemMessage | ResultMessage | StreamEvent | RateLimitEvent

### ResultMessage
```python
@dataclass
class ResultMessage:
    subtype: str           # "success", "error", etc.
    duration_ms: int
    is_error: bool
    num_turns: int
    session_id: str
    total_cost_usd: float | None
    result: str | None
    structured_output: Any = None
```

## Content Block Types

ContentBlock = TextBlock | ThinkingBlock | ToolUseBlock | ToolResultBlock

## Permission System

PermissionMode = "default" | "acceptEdits" | "plan" | "dontAsk" | "bypassPermissions"

Custom permission handler via `can_use_tool` callback:
- Returns PermissionResultAllow (optionally with updated_input)
- Returns PermissionResultDeny (with message, optional interrupt)

## Hook Events

HookEvent = PreToolUse | PostToolUse | PostToolUseFailure | UserPromptSubmit | Stop | SubagentStop | PreCompact | Notification | SubagentStart | PermissionRequest

Hooks defined via HookMatcher with matcher pattern + callback + timeout.

## AgentDefinition

```python
@dataclass
class AgentDefinition:
    description: str
    prompt: str
    tools: list[str] | None = None
    model: Literal["sonnet", "opus", "haiku", "inherit"] | None = None
    skills: list[str] | None = None
    memory: Literal["user", "project", "local"] | None = None
    mcpServers: list[str | dict] | None = None
```

## MCP Server Configs

- McpStdioServerConfig: command + args (local process)
- McpSSEServerConfig: url + headers (SSE transport)
- McpHttpServerConfig: url + headers (HTTP transport)

## ThinkingConfig

- adaptive: Model decides when to think
- enabled: Always think with budget_tokens
- disabled: No extended thinking

## Error Types

ClaudeSDKError (base), CLINotFoundError, CLIConnectionError, ProcessError, CLIJSONDecodeError
