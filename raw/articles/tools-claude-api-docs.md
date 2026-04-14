# Managed Agents — Tools Reference

Source: https://platform.claude.com/docs/en/managed-agents/tools
Ingested: 2026-04-14
Type: documentation

---

## Overview

Claude Managed Agents provides built-in tools that Claude can use autonomously within a session. Custom tools are also supported — your application executes them and sends results back.

Requires `managed-agents-2026-04-01` beta header.

## Available Built-in Tools

| Tool | Name | Description |
|------|------|-------------|
| Bash | `bash` | Execute bash commands in a shell session |
| Read | `read` | Read a file from the local filesystem |
| Write | `write` | Write a file to the local filesystem |
| Edit | `edit` | Perform string replacement in a file |
| Glob | `glob` | Fast file pattern matching using glob patterns |
| Grep | `grep` | Text search using regex patterns |
| Web fetch | `web_fetch` | Fetch content from a URL |
| Web search | `web_search` | Search the web for information |

All enabled by default when toolset is included.

## Configuring the Toolset

Enable with `agent_toolset_20260401`:

```python
agent = client.beta.agents.create(
    name="Coding Assistant",
    model="claude-sonnet-4-6",
    tools=[{
        "type": "agent_toolset_20260401",
        "configs": [
            {"name": "web_fetch", "enabled": False},
        ],
    }],
)
```

### Disable specific tools
Set `enabled: false` in config entry.

### Enable only specific tools
Set `default_config.enabled` to false, then enable specific ones:

```json
{
  "type": "agent_toolset_20260401",
  "default_config": { "enabled": false },
  "configs": [
    { "name": "bash", "enabled": true },
    { "name": "read", "enabled": true }
  ]
}
```

## Custom Tools

Extend Claude's capabilities with user-defined tools. Claude emits structured requests; your code runs the operation; results flow back.

```python
agent = client.beta.agents.create(
    name="Weather Agent",
    model="claude-sonnet-4-6",
    tools=[
        {"type": "agent_toolset_20260401"},
        {
            "type": "custom",
            "name": "get_weather",
            "description": "Get current weather for a location",
            "input_schema": {
                "type": "object",
                "properties": {
                    "location": {"type": "string", "description": "City name"},
                },
                "required": ["location"],
            },
        },
    ],
)
```

## Best Practices for Custom Tools

1. **Provide extremely detailed descriptions** — 3-4+ sentences per tool. More context = better tool selection.
2. **Consolidate related operations** — Group actions into fewer tools with action parameters instead of many separate tools.
3. **Use meaningful namespacing** — Prefix names with resource (e.g., `db_query`, `storage_read`).
4. **Return only high-signal information** — Semantic identifiers, only fields Claude needs for next step.

## Supported Languages

Examples provided in: curl, CLI, Python, TypeScript, C#, Go, Java, PHP, Ruby
