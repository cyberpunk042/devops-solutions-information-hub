---
title: "Source — openclaw-billing-proxy: Billing Proxy for OpenClaw via Claude Subscription"
type: source-synthesis
domain: cross-domain
status: synthesized
confidence: high
maturity: seed
created: 2026-04-14
updated: 2026-04-14
sources:
  - id: openclaw-billing-proxy-github
    type: repository
    url: "https://github.com/zacdcook/openclaw-billing-proxy"
tags:
  - openclaw
  - billing
  - proxy
  - anthropic
  - oauth
  - claude-max
  - fingerprint-detection
  - reverse-proxy
  - openfleet
  - billing-architecture
  - http-middleware
---

# Source — openclaw-billing-proxy: Billing Proxy for OpenClaw via Claude Subscription

## Summary

`openclaw-billing-proxy` is a Node.js HTTP proxy that routes OpenClaw API requests through a Claude Max/Pro subscription instead of Anthropic's Extra Usage billing tier. It uses 7-layer bidirectional request/response processing to make OpenClaw traffic appear to Anthropic as originating from Claude Code — injecting billing headers, swapping OAuth tokens, sanitizing trigger phrases, renaming tool names to Claude Code conventions, stripping system template fingerprints, and applying full reverse mapping on responses. This is a real-world adversarial engineering case study: a detailed technical account of how Anthropic's multi-layer detection evolved from April 2026 and how the proxy responded.

## Key Insights

### 1. The Billing Context: Anthropic's April 2026 Policy Change

On April 4, 2026, Anthropic revoked subscription billing for third-party tools. OpenClaw requests shifted to "Extra Usage" (pay-per-token) billing rather than the flat Claude Max/Pro subscription. This proxy was created as a workaround: it sits between OpenClaw and the Anthropic API, transforming requests to look like they originate from Claude Code (which retains subscription billing rights).

This event is a significant inflection point for our ecosystem: it means any agent platform that is not Claude Code faces ongoing billing adversity unless it uses a proxy or restructures its billing relationship with Anthropic.

### 2. Detection Architecture — Four Layers Anthropic Uses

Anthropic's detection system as documented in this proxy (updated April 8, 2026) uses four independently scored layers:

**Layer 1: Billing Header** — string match for an 84-character Claude Code billing identifier in the system prompt. Without it, OAuth requests route to Extra Usage.

**Layer 2: String Triggers** — keyword scan of the full request body for ~30 known phrases: `OpenClaw`, `sessions_spawn`, `sessions_list`, `sessions_history`, `sessions_send`, `sessions_yield`, `HEARTBEAT_OK`, `running inside`, `clawhub`, `clawd`, etc. The classifier checks these in ALL content — system prompt, tool definitions, and message history.

**Layer 3: Tool Name Fingerprinting** (added April 8, 2026) — The API identifies OpenClaw by the combination of tool names in the request. The threshold is ~25 tools; when enough OpenClaw-specific tool names appear together, the request is flagged. This was proved experimentally: identical empty schemas with original names = FAIL; same schemas with PascalCase Claude Code names = PASS.

**Layer 4: System Prompt Template Matching** (added April 8, 2026) — The structured config sections (`## Tooling`, `## Workspace`, `## Messaging`, `## Reply Tags`) match a known OpenClaw template fingerprint at ~26K characters. String replacement does not defeat this because structure is preserved when words change. The fix strips ~28K of config and replaces it with ~0.5K natural prose paraphrase.

**Critical insight**: Detection is cumulative. The classifier scores the entire request body (system + tools + messages). Each layer contributes to a total score. All four layers must be addressed simultaneously for large conversation bodies.

### 3. The 7-Layer Proxy Processing Pipeline (v2.0+)

**Outbound (request to Anthropic API):**
1. **Billing Header** — Injects 84-character Claude Code billing identifier into system prompt
2. **Token Swap** — Replaces OpenClaw auth token with Claude Code OAuth token (from `~/.claude/.credentials.json` or macOS Keychain)
3. **String Sanitization** — Replaces 30 trigger phrases via split/join (not regex, to avoid partial-match bugs)
4. **Tool Name Bypass** — Renames all 29 OpenClaw tool names to PascalCase Claude Code convention throughout the entire body (tools array, messages, system prompt): `exec` → `Bash`, `message` → `SendMessage`, `lcm_grep` → `ContextGrep`, `gateway` → `SystemCtl`, `cron` → `Scheduler`, `memory_search` → `KnowledgeSearch`, etc.
5. **System Template Bypass** — Strips ~28K of structured config, replaces with ~0.5K prose paraphrase
6. **Tool Description Stripping** — Removes tool descriptions to reduce fingerprint signal
7. **Property Renaming** — Renames OC-specific schema properties: `session_id` → `thread_id`, `conversation_id` → `dialogue_id`, etc.

**Inbound (response to OpenClaw):**
8. **Full Reverse Mapping** — Restores ALL original tool names, property names, file paths, and identifiers in both SSE streaming chunks and JSON responses

### 4. Reverse Mapping Is Non-Trivial at the SSE Level

SSE (Server-Sent Events) streaming chunks are TCP-fragmented — a single pattern like `ocplatform` can be split across two `data` events as `ocp` and `latform`. The v2.1.3 fix introduced a 64-byte tail buffer between chunks before applying `reverseMap()`, flushing the remaining tail on stream `end`. The tail size (64 bytes) is 2.5x the longest current pattern (24 chars), providing headroom for future longer patterns.

Additionally, SSE `input_json_delta` events embed tool arguments inside a `partial_json` field where inner quotes are escaped (`\"Name\"` rather than `"Name"`). The reverse mapping must handle both plain and escaped forms.

### 5. CC Signature Emulation for Authentication Fidelity

Beyond billing headers, v2.1.0 added Claude Code identity emulation:
- Dynamic billing fingerprint: SHA256-based 3-char hash matching Claude Code's `utils/fingerprint.ts`, computed per-request from first user message
- CC version header set to `2.1.97`, entrypoint `cli`
- Stainless SDK headers: `x-stainless-arch/lang/os/package-version/runtime`
- CC identity headers: `user-agent`, `x-app`, `x-claude-code-session-id`
- Request metadata: `device_id` + `session_id` in CC format
- Beta flags: `advanced-tool-use-2025-11-20`, `fast-mode-2026-02-01`

This transforms OpenClaw sessions into what looks like authentic Claude Code sessions from Anthropic's perspective.

### 6. OAuth Token Lifecycle and Refresh

Claude Code's OAuth token expires every ~24 hours. The proxy reads the token fresh from disk on each request (no caching). Refresh is triggered by opening Claude Code CLI (which auto-refreshes on startup), or via automated cron: `claude -p "ping" --max-turns 1 --no-session-persistence`.

macOS adds complexity: newer Claude Code versions store tokens in macOS Keychain instead of a file. The proxy checks four Keychain service names: `Claude Code-credentials`, `claude-code`, `claude`, `com.anthropic.claude-code`. The `setup.js` script auto-extracts from Keychain to `~/.claude/.credentials.json`.

### 7. Configuration Architecture — Merge Semantics

The v2.2.2 release fixed a critical configuration bug: `setup.js` previously wrote a frozen snapshot of pattern arrays to `config.json` at install time. After `git pull`, 20+ new critical patterns were silently skipped because `config.replacements || DEFAULT_REPLACEMENTS` used the stale config.

The fix: **merge semantics**. `config.json` patterns now merge with `proxy.js` defaults rather than replacing them. Defaults are applied first; config entries override (same key) or add (new key). This prevents stale config snapshots from masking new default patterns. Users can opt out via `"mergeDefaults": false` for full manual control.

### 8. Opus 4.6 Compatibility Fix

OpenClaw sometimes pre-fills the trailing assistant message to resume interrupted responses. Opus 4.6 disabled assistant message prefill — Anthropic returns: "This model does not support assistant message prefill." The prefill stays in conversation history, making every retry fail permanently.

Layer 8 (v2.1.1) strips trailing assistant prefill before forwarding. Implementation uses raw string manipulation (not JSON.parse/stringify) to avoid re-serialization risks on large bodies.

### 9. Deployment Patterns

The proxy supports four deployment modes:
- **Direct**: `node proxy.js` (simplest, requires Node.js 18+)
- **Docker Compose**: `docker compose up -d` with credential volume mount, health check, localhost-only port binding, log rotation
- **systemd**: standard `[Service]` unit with `Restart=always`
- **PM2**: `pm2 start proxy.js --name openclaw-proxy`

Docker adds complexity for macOS because Keychain credential extraction does not work inside Docker containers — requires `OAUTH_TOKEN` env var or the `~/.claude` volume mount.

### 10. Diagnostic Infrastructure

`troubleshoot.js` tests 8 layers independently: credentials, token, API connectivity, billing header, trigger detection, proxy health, and end-to-end. This is the right pattern for complex proxy systems — a dedicated diagnostic script that reports exactly what is broken, not just that something is broken.

`/health` endpoint returns: token status, request count, uptime, subscription type, version, pattern counts, and per-layer status.

## Deep Analysis

### Adversarial Engineering Pattern

This proxy is a case study in adversarial system engineering — a system designed to defeat an opponent's detection mechanisms. The changelog documents the entire arms race:

| Date | Anthropic Adds | Proxy Responds |
|------|----------------|----------------|
| Apr 4, 2026 | Revokes subscription billing for third-party tools | v1.0: billing header injection + OAuth swap |
| Apr 5, 2026 | — | v1.1: reduce to 7 verified triggers (removes unnecessary patterns) |
| Apr 5–6 | — | v1.2–1.4: reverse mapping, HEARTBEAT_OK, macOS Keychain |
| Apr 8, 2026 | Tool name fingerprinting + system template matching | v2.0: full 7-layer processing |
| Apr 8–9 | — | v2.1–v2.2: Opus 4.6 prefill, SSE tail buffer, CC emulation, Docker, config merge |

The proxy's debugging methodology is notable: binary search on a 103K system prompt to identify HEARTBEAT_OK as a trigger; controlled experiments with empty tool schemas to isolate tool name fingerprinting vs. other signals.

### Billing Architecture Implications for Our Ecosystem

This is directly relevant to [[openfleet|OpenFleet]] and any agent platform in our ecosystem that uses Anthropic's API:

1. **Third-party tool billing risk**: Any tool that identifies itself as non-Claude-Code faces the same Extra Usage redirect. The proxy documents exactly what signals Anthropic uses — this is intelligence about the billing boundary we need to understand.

2. **OAuth vs API key**: The proxy uses Claude Code OAuth tokens (subscription-billed) rather than API keys (pay-per-token). This is a cost architecture decision: subscription billing is cheaper at high volume. Our fleet infrastructure should understand this tradeoff.

3. **Header injection as billing control plane**: The 84-character billing identifier in the system prompt is the primary billing gate. This is a fragile pattern — any tool that can modify the system prompt can influence billing routing. Our own tooling should be aware of this.

4. **Fingerprinting as platform lock-in**: Anthropic's detection is a form of platform lock-in enforcement — it ensures subscription benefits accrue only to the officially authorized client (Claude Code). Understanding these mechanisms helps us architect our ecosystem tools to avoid unintentional detection.

### System Prompt Engineering Under Adversarial Conditions

The proxy's Layer 5 (system template bypass) reveals something important about large system prompts: Anthropic's classifier can fingerprint structured templates by their structure, not just their content. Replacing 28K of structured config with 0.5K of natural prose paraphrase (while preserving semantic meaning via AGENTS.md and workspace docs) is an extreme form of system prompt distillation.

This suggests that well-structured, long system prompts are more fingerprintable than short natural language prompts — a consideration for how we design agent system prompts in our ecosystem.

### Tool Name Conventions as Identity Signals

The proxy's tool rename map (29 tools) reveals the naming conventions that Claude Code uses:
- Bash, Read, Write, Edit, Glob, Grep, Agent (core tools)
- Scheduler, SystemCtl, KnowledgeSearch, ContextGrep, ContextExpand (domain tools)
- SendMessage, AgentList, TaskList (coordination tools)

The fact that PascalCase naming is specifically associated with Claude Code's billing identity is an interesting standardization signal — tool names are not just UX, they can be billing-significant.

### Node.js Implementation Choices

The proxy is implemented in Node.js (zero external dependencies by design). Key implementation decisions:
- Raw string manipulation for body processing rather than JSON.parse/stringify — avoids re-serialization of 235K+ bodies and preserves exact byte representation
- StringDecoder for correct UTF-8 chunk handling in SSE streams
- 64-byte tail buffer for SSE chunk boundary handling
- BOM stripping on credentials file before JSON.parse (v1.4.1 fix for PowerShell file rewrites)

### Relationship to Our OpenFleet Architecture

If OpenFleet agents use Anthropic's API directly, they may face the same billing classification issues. The proxy's documentation gives us:
1. The exact signals Anthropic uses for detection (can inform how we structure our tools)
2. A reference implementation for billing-aware proxy infrastructure
3. The OAuth token lifecycle pattern (auto-refresh via Claude Code CLI)
4. The health check + diagnostic pattern (8-layer independent test)

More broadly: the existence of this proxy signals that the OpenClaw ecosystem (a Claude Code competitor) is large enough to warrant anti-circumvention measures from Anthropic. This is ecosystem intelligence about the competitive landscape.

## Open Questions

- Is OpenClaw the same system as OpenFleet, or a related but distinct agent platform? The tool names (`sessions_spawn`, `sessions_list`, `sessions_send`) suggest a session-management architecture — what does this tell us about how OpenFleet sessions are structured?
- The billing identifier is an 84-character string injected into the system prompt — what happens to agents in our ecosystem that aren't Claude Code? Do they face Extra Usage billing?
- The proxy documents the complete list of trigger phrases Anthropic uses. Should our own agent system prompts audit against these to avoid unintentional billing misrouting?
- Layer 8 (Opus 4.6 prefill stripping) suggests Anthropic made a breaking change in Opus 4.6 regarding assistant prefill. How does this affect our own agents that may use prefill?

## Relationships

- RELATES TO: [[openfleet|OpenFleet]] (billing architecture, OAuth token patterns, and agent session management are directly relevant to OpenFleet infrastructure)
- RELATES TO: [[model-ecosystem|Model — Ecosystem Architecture]] (Anthropic billing policy changes affect the entire agent ecosystem; proxy patterns inform how we architect cross-platform billing)

## Backlinks

[[openfleet|OpenFleet]]
[[model-ecosystem|Model — Ecosystem Architecture]]
