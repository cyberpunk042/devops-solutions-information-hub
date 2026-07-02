---
title: "Post-Anthropic 3-Layer Stack M002 — Harness-Level Integration Details (MCP Wiring · OpenCode Config · claude-code-router Wrapper Option)"
aliases:
  - "M002 — Harness-Level Integration Details"
  - "Multica MCP + OpenCode + Wrapper Wiring"
type: module
domain: backlog
status: active
priority: P0
task_type: module
parent_epic: "post-anthropic-stack-3-layer-assembly-multica-aicp-3090"
current_stage: implement
readiness: 85
progress: 60
stages_completed:
  - "document"
  - "design"
  - "scaffold"
artifacts:
  - "wiki/sources/tools-integration/src-multica-managed-agents-platform.md"
  - "wiki/sources/tools-integration/src-opencode-harness-features.md"
  - "tools/mcp_server.py (research-wiki MCP — 28 tools)"
  - ".mcp.json (research-wiki MCP config)"
confidence: high
created: 2026-04-28
updated: 2026-04-28
last_reviewed: 2026-04-28
sources:
  - id: parent-epic
    type: wiki
    file: wiki/backlog/epics/pre-milestone/post-anthropic-stack-3-layer-assembly-multica-aicp-3090.md
    description: "Parent epic — this module fills the harness-level integration gap that M001 (custom_env mechanism) and M003 (smoke-test runbook) don't fully cover"
  - id: m001
    type: wiki
    file: wiki/backlog/modules/post-anthropic-3-layer-m001-multica-per-agent-provider-config.md
    description: "Predecessor — `custom_env` mechanism. M002 builds on M001 by adding harness-specific concerns (MCP, wrapper, OpenCode config)"
  - id: opencode-synth
    type: wiki
    file: wiki/sources/tools-integration/src-opencode-harness-features.md
    description: "OpenCode's 75-provider config detail — the harness-level config mechanism for OpenCode agents in Multica"
  - id: multica-synth
    type: wiki
    file: wiki/sources/tools-integration/src-multica-managed-agents-platform.md
    description: "Multica's mcp_config field documentation (currently only Claude Code consumes it per docs line 7043)"
tags: [module, p0, multica, mcp-integration, research-wiki-mcp, opencode-config, claude-code-router, harness-level, post-anthropic, mission-2026-04-28, m002]
---

# M002 — Harness-Level Integration Details (Beyond `custom_env`)

## Summary

Builds on [M001](post-anthropic-3-layer-m001-multica-per-agent-provider-config.md)'s `custom_env` mechanism by addressing harness-specific integration concerns that don't fit M001's per-agent provider scope: **MCP integration** (Multica's `mcp_config` field is currently only consumed by Claude Code per docs line 7043 — relevant for plugging the research-wiki MCP server into Multica-orchestrated Claude Code agents); **OpenCode's harness-level provider config** (OpenCode's 75-provider list per [its synthesis](../../sources/tools-integration/src-opencode-harness-features.md) is configured via OpenCode's own config file, NOT via Multica's `custom_env` — different mechanism); **claude-code-router wrapper option** (a provider-proxy alternative for Claude Code agents that need dynamic per-request routing without AICP). Each harness has its own integration peculiarities; this module documents them so the operator knows which mechanism applies when.

## Per-Harness Provider-Config Mechanisms (Comparison Matrix)

> [!abstract] How each Multica-supported harness gets its provider config
>
> | Harness | Primary mechanism | Multica `custom_env` | Multica `mcp_config` | Notes |
> |---|---|---|---|---|
> | **Claude Code** | `ANTHROPIC_BASE_URL` + `ANTHROPIC_API_KEY` env vars | ✅ Use it | ✅ **Consumed by Claude Code today** (per docs line 7043) | Most flexible — supports both env routing AND MCP |
> | **OpenCode** | OpenCode config file at `~/.config/opencode/config.json` (or similar) — provider list with API keys | ⚠ Override-via-env where supported (some env vars per OpenCode's config), but config file is canonical | ❌ Receives but doesn't consume MCP config (per docs line 7043) | OpenCode has its own provider abstraction; Multica `custom_env` overrides specific vars but doesn't replace the config file |
> | **Codex** | OpenAI / OpenRouter via env vars + Codex's own config | ✅ Use for `OPENAI_API_KEY`, etc. | ❌ Not consumed | Standard OpenAI-compat config |
> | **Cursor Agent** | Cursor Inc.'s proprietary auth + config | ⚠ Limited — Cursor's auth model is opaque | ❌ Not consumed | Multica orchestrates the binary but Cursor's account-bound auth limits provider switching |
> | **Gemini CLI** | Google API key + project ID | ✅ `GOOGLE_API_KEY`, etc. | ❌ Not consumed | |
> | **Hermes / Pi / Kimi CLI / Kiro CLI / OpenClaw** | Each harness's own config conventions | ✅ Use where the harness reads env | ❌ Not consumed (per general Multica behavior) | Operator's per-harness expertise applies |

**Key insight**: Multica's UI exposes `mcp_config` as a generic field, but **only Claude Code's CLI consumes it** today. For the operator's wiki MCP integration scenario specifically, Claude Code is the path forward.

## Wiring the research-wiki MCP into Multica-orchestrated Claude Code agents

> [!success] Recipe — Multica Claude Code agent + research-wiki MCP (28 wiki tools available to the agent)

Per the wiki's own [`tools/mcp_server.py`](../../../tools/mcp_server.py) and [`.mcp.json`](../../../.mcp.json), the research-wiki MCP server exposes **28 tools** to Claude Code:

- Gateway (9): `wiki_gateway_query`, `wiki_gateway_orient`, `wiki_gateway_flow`, `wiki_gateway_health`, `wiki_gateway_compliance`, `wiki_gateway_template`, `wiki_gateway_timeline`, `wiki_gateway_contribute`, `wiki_gateway_docs`
- Ingestion (4): `wiki_fetch`, `wiki_fetch_topic`, `wiki_post`, `wiki_crossref`
- Knowledge (7): `wiki_search`, `wiki_read_page`, `wiki_list_pages`, `wiki_backlog`, `wiki_gaps`, `wiki_log`, `wiki_continue`
- Maintenance (6): `wiki_evolve`, `wiki_scan_project`, `wiki_sister_project`, `wiki_mirror_to_notebooklm`, `wiki_integrations`, `wiki_sync`
- Status / meta (2): `wiki_status`, `wiki_methodology_guide`

To make these available to a Multica Claude Code agent:

> [!tip] Multica UI: New Agent (or Edit existing)
>
> | Field | Value |
> |---|---|
> | Provider | `Claude Code` |
> | Custom Env | (per agent's provider routing — AICP / Ollama Cloud / etc. per M001 recipes) |
> | **MCP Config** | The research-wiki MCP server entry from this wiki's `.mcp.json` (operator copies the config block) |
> | Custom Args | (none specific to MCP) |
> | Skills | (optional Multica-skills — separate from MCP tools) |
>
> Once the agent runs under Multica's daemon, Claude Code consumes the `mcp_config` and exposes the 28 wiki tools to the agent's reasoning loop. **Agents can now call `wiki_search`, `wiki_read_page`, `wiki_contribute` directly from inside Multica.**

### What this enables operationally

| Use case | Multica agent invocation pattern |
|---|---|
| Agent reads wiki context before answering | `wiki_search` → `wiki_read_page` chain inside agent's tool-calling |
| Agent contributes findings back to wiki | `wiki_gateway_contribute` to land a lesson / remark / correction |
| Agent ingests new sources | `wiki_fetch` then `wiki_post` to validate |
| Agent queries methodology before recommending | `wiki_methodology_guide` or `wiki_gateway_query` |
| Agent generates a session log | `wiki_log` to write to `wiki/log/` with proper frontmatter |

This is the wiki's own MCP server **operating from inside Multica's orchestration layer** — agents in Multica's board can directly perform wiki operations as part of their task lifecycle.

## OpenCode Harness Config (Different Mechanism)

> [!info] OpenCode's provider config is in its own config file, not just Multica `custom_env`

Per [src-opencode-harness-features](../../sources/tools-integration/src-opencode-harness-features.md), OpenCode supports 75+ providers via its config file (typically `~/.config/opencode/config.json` or `~/.opencode/config.toml`). When Multica orchestrates an OpenCode agent:

1. **OpenCode's config file is the primary provider abstraction** — operator configures providers there
2. **Multica's `custom_env` for OpenCode** can override specific env vars OpenCode reads (e.g., `OPENROUTER_API_KEY`) but doesn't replace the config file
3. **Multica's `mcp_config` for OpenCode** is RECEIVED but NOT CONSUMED by OpenCode's CLI — research-wiki MCP integration via Multica works only for Claude Code today

> [!warning] OpenCode + research-wiki MCP gotcha
>
> If the operator wants OpenCode agents to access the research-wiki MCP, the wiring is OpenCode-side, not Multica-side. OpenCode has its own MCP support per its features synth — configure it in OpenCode's config file, NOT via Multica's `mcp_config` (which OpenCode ignores). Multica orchestrates the OpenCode binary; whatever MCP servers OpenCode is configured for are available to the agent.

## claude-code-router as a Wrapper Option

> [!tip] When `custom_env` isn't expressive enough — use claude-code-router as a wrapper

[musistudio/claude-code-router](https://github.com/musistudio/claude-code-router) is an open-source wrapper that intercepts Claude Code's API calls and routes them across providers (OpenRouter, DeepSeek, Ollama, Gemini, Volcengine, SiliconFlow). Use cases:

| Scenario | Wrapper option |
|---|---|
| Operator wants per-request dynamic routing INSIDE Claude Code (not just per-agent) | Install claude-code-router; configure its routing rules; Multica's agent's `provider: Claude Code` orchestrates `claude` (which is now actually claude-code-router) |
| Operator wants Claude Code to talk to providers without AICP in the loop | claude-code-router as the provider proxy |
| Operator wants to test multiple providers from a single Multica agent | claude-code-router can route by request semantics |

> [!warning] When to use AICP vs claude-code-router
>
> - **AICP**: complexity-scored routing, mission-aligned with operator's existing tier-map work, broader backend support (`local`, `k2_6_local`, `k2_6_openrouter`, `ollama_cloud`)
> - **claude-code-router**: simpler, focused on Claude Code's API surface, provider-list expansion
>
> They are alternatives, not complements at the same layer. Choose based on whether the operator's routing needs are AICP-style (complexity-scored across mission tiers) or claude-code-router-style (provider expansion under Anthropic API compat).

## Tasks

| Task | Description | Status |
|---|---|---|
| T-M002-1 | Document per-harness provider-config mechanism comparison | ✅ Done in this module |
| T-M002-2 | Document research-wiki MCP integration recipe for Claude Code agents in Multica | ✅ Done in this module |
| T-M002-3 | Document OpenCode-specific config file mechanism (different from `custom_env`) | ✅ Done in this module |
| T-M002-4 | Document claude-code-router as wrapper option (alternative to AICP at the harness-provider boundary) | ✅ Done in this module |
| T-M002-5 | Operator validates: create a Multica Claude Code agent with research-wiki MCP config; smoke-test by calling `wiki_search` from the agent | ⊙ Pending operator |
| T-M002-6 | Operator validates: create a Multica OpenCode agent; verify OpenCode's config-file mechanism works (separate from Multica's `custom_env`) | ⊙ Pending operator |
| T-M002-7 | (Optional) Operator evaluates claude-code-router as alternative to AICP for specific Claude Code agents | ⊙ Pending operator decision |

## Done When

- [x] Per-harness provider-config mechanism documented (matrix of which harnesses consume `custom_env` / `mcp_config` / their own config files)
- [x] Research-wiki MCP integration recipe documented (Claude Code only)
- [x] OpenCode harness-level config mechanism documented (separate from Multica `custom_env`)
- [x] claude-code-router wrapper option documented (alternative to AICP)
- [ ] Operator validates research-wiki MCP works inside a Multica Claude Code agent (call `wiki_search` from agent reasoning, observe output)
- [ ] Operator validates OpenCode agent in Multica works with OpenCode's config-file provider abstraction
- [ ] M002 → `current_stage: test` once operator validates above

## Dependencies

- **Predecessor**: [M001](post-anthropic-3-layer-m001-multica-per-agent-provider-config.md) (`custom_env` foundation)
- **Wiki**: [Multica synthesis](../../sources/tools-integration/src-multica-managed-agents-platform.md) for `mcp_config` documentation
- **Wiki**: [OpenCode synthesis](../../sources/tools-integration/src-opencode-harness-features.md) for OpenCode-specific config mechanism
- **External**: research-wiki MCP server at `tools/mcp_server.py` (already running in operator's environment per `.mcp.json`)
- **External**: claude-code-router (operator-optional install if Recipe 4 is needed)
- **Hardware**: NOT blocked by RTX 4090 — testable on existing hardware

## Open Questions

> [!question] Does Multica's `mcp_config` field translate to OpenCode's MCP integration eventually?
> Currently per docs line 7043, `mcp_config` is received but only consumed by Claude Code. If Multica adds OpenCode MCP consumption, this module's matrix changes. Track Multica releases.

> [!question] Should the operator prefer Multica `mcp_config` OR OpenCode's own MCP config for OpenCode agents?
> Today: must use OpenCode's own config (Multica's `mcp_config` is no-op for OpenCode). Future: Multica may add support; revisit then.

> [!question] What's the correct `mcp_config` JSON structure for the research-wiki MCP entry?
> Operator extracts from this wiki's existing `.mcp.json`. Documenting the exact JSON snippet would close this — but it's operator-side once the recipe lands.

## Why This Matters

This module closes the **harness-level integration gap** that M001's `custom_env` mechanism alone doesn't cover. The operator now knows: (a) which harness consumes which Multica field; (b) how to make the wiki's 28 MCP tools available to a Multica-orchestrated Claude Code agent; (c) why OpenCode's mechanism is different; (d) when claude-code-router is an option vs when AICP is the right path. Without this module, the operator would discover these gotchas one-by-one through trial-and-error during M003 smoke testing.

## Relationships

- PART OF: [[post-anthropic-stack-3-layer-assembly-multica-aicp-3090|Epic — Post-Anthropic 3-Layer Stack Assembly]]
- BUILDS ON: [[post-anthropic-3-layer-m001-multica-per-agent-provider-config|M001 — `custom_env` Mechanism]]
- BUILDS ON: [[src-multica-managed-agents-platform|Multica Synthesis]]
- BUILDS ON: [[src-opencode-harness-features|OpenCode Synthesis]]
- ENABLES: [[post-anthropic-3-layer-m003-multica-aicp-ollama-cloud-smoke-test-runbook|M003 — Smoke-Test Runbook]] (smoke-test agents can now use wiki MCP tools)
- DEMONSTRATES: [[infrastructure-over-instructions-for-process-enforcement|Principle 1]] — MCP integration is infrastructure (config-level), not instructions
- RELATES TO: [[mcp-vs-cli-for-tool-integration|Decision — MCP vs CLI]] (per-harness MCP support state informs that decision's applicability)

## Backlinks

[[Epic — Post-Anthropic 3-Layer Stack Assembly]]
[[M001 — `custom_env` Mechanism]]
[[src-multica-managed-agents-platform|Multica Synthesis]]
[[src-opencode-harness-features|OpenCode Synthesis]]
[[M003 — Smoke-Test Runbook]]
[[infrastructure-over-instructions-for-process-enforcement|Principle 1]]
[[Decision — MCP vs CLI]]
