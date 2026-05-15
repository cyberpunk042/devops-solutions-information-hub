---
description: List or configure surface integrations (multica · wiki · docs · claude-os · ...)
allowed-tools: Bash
---

# /assistant-surfaces — Manage multi-surface integrations

Per operator 2026-05-09: "I can interact with, with or without multica or the wiki LLM folder and/or docs folder and/or Claude OS and/or any other relevant surface".

## Usage

```
/assistant-surfaces list                              # available surfaces (with detect status)
/assistant-surfaces enable <profile> <surface>        # wire a surface to a profile
/assistant-surfaces disable <profile> <surface>       # unwire
```

## Known surfaces (see .assistant/_global/surfaces.yaml)

- `openclaw-native` — primary OpenClaw channels (Slack/Discord/Telegram/CLI)
- `multica` — Multica board + WebSocket
- `wiki-llm-folder` — research-wiki MCP access
- `docs-folder` — project docs ambient context
- `claude-os` — Memory MCP + Real-Time Learning
- `claude-code` — interactive Claude Code session
- `opencode` — OpenCode CLI consumer
- `hermes` — Hermes Agent CLI
- `huggingface` — Hugging Face MCP tools
- `github` — gh CLI auth-bearing surface
- `public-obsidian` — downstream Obsidian vault sync

## Run

!`bin/assistant surfaces $ARGUMENTS`
