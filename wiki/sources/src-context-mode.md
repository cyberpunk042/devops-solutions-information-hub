---
title: "Synthesis: Context Mode — MCP Sandbox for Context Saving"
type: source-synthesis
domain: ai-agents
status: synthesized
confidence: high
created: 2026-04-09
updated: 2026-04-09
sources:
  - id: src-context-mode
    type: documentation
    url: "https://github.com/mksglu/context-mode"
    file: raw/articles/mksglucontext-mode.md
    title: "mksglu/context-mode"
    ingested: 2026-04-09
tags: [context-mode, mcp, context-management, sandbox, session-continuity, context-saving, fts5, sqlite, claude-code-plugin]
---

# Synthesis: Context Mode — MCP Sandbox for Context Saving

## Summary

Context Mode is an MCP server that attacks the context pollution problem from the opposite direction than CLI+Skills: instead of replacing MCP tools with CLI alternatives, it wraps MCP tool calls in a sandbox so raw data never enters the context window. A Playwright snapshot normally costs 56 KB per call; through context-mode's `ctx_execute` sandbox, only the console output reaches context — 299 bytes, a 99% reduction. Over a full 30-minute session, 315 KB of raw MCP output compresses to 5.4 KB, extending usable session length from ~30 minutes to ~3 hours. This is a complementary strategy to the CLI-over-MCP lesson: use CLI+Skills for tools you control, use context-mode for MCP tools you must use.

## Key Insights

### The three-sided problem context-mode solves

Context Mode frames the context window problem as having three distinct failure modes, each requiring a different mechanism:

1. **Raw data flooding** — Every unmediated MCP tool call dumps its full payload into context. Playwright snapshots: 56 KB each. Twenty GitHub issues: 59 KB. An access log of 500 requests: 45 KB. After 30 minutes of normal agent work, 40% of the context window is consumed by data the model already processed and no longer needs. Context-mode's sandbox tools (`ctx_execute`, `ctx_execute_file`, `ctx_batch_execute`) intercept these calls: data is processed in an isolated subprocess, and only `console.log()` output enters context.

2. **Compaction amnesia** — When context fills, the agent compacts the conversation, dropping older messages. Without state tracking, the model forgets which files it was editing, what tasks are pending, and what the user last asked. Context-mode captures every meaningful session event (file edits, git operations, task completions, user decisions, error states) in a per-project SQLite database. On compaction, a PreCompact hook builds a priority-tiered snapshot (≤2 KB), which SessionStart then re-injects as a structured Session Guide. The model resumes from the last user prompt with full working state intact.

3. **LLM-as-data-processor anti-pattern** — Reading 50 files into context to count functions is the wrong paradigm. Context-mode's "Think in Code" principle makes this explicit: the LLM should write a script that does the counting and `console.log()` only the result. One script replaces ten tool calls and avoids 100x the context cost. This is enforced as a mandatory paradigm across all 12 supported platforms.

### Sandbox mechanics

`ctx_execute` spawns an isolated subprocess per call with its own process boundary. Eleven language runtimes are available (JavaScript, TypeScript, Python, Shell, Ruby, Go, Rust, PHP, Perl, R, Elixir). Authenticated CLIs (`gh`, `aws`, `gcloud`, `kubectl`, `docker`) work via credential passthrough — environment variables and config paths are inherited without being exposed to the conversation. When output exceeds 5 KB and an `intent` parameter is provided, context-mode switches to intent-driven filtering: full output is indexed into FTS5, then searched for sections matching the intent, returning only relevant snippets.

### Knowledge base: SQLite FTS5 + BM25

The `ctx_index` and `ctx_search` tools build a per-project knowledge base using SQLite FTS5. Indexing chunks markdown by headings (preserving code blocks intact) and stores chunks with BM25 weighting — titles and headings are weighted 5x for navigational queries. Porter stemming is applied at index time so variant word forms match the same stem. Search runs two parallel strategies merged via Reciprocal Rank Fusion: Porter stemming FTS5 MATCH and trigram substring FTS5 for partial string matching. Multi-term queries get a proximity reranking pass (terms appearing close together rank higher). Levenshtein distance fuzzy correction catches typos before re-searching. The `ctx_fetch_and_index` tool extends this to URLs with a 24-hour TTL cache — repeat calls skip the network entirely.

### Session continuity requires four hooks

Full session continuity (capture + snapshot + restore) depends on four hooks working together: PreToolUse (sandbox routing enforcement), PostToolUse (event capture after each call), PreCompact (snapshot construction), and SessionStart (state restoration). Among the 12 supported platforms, Claude Code, Gemini CLI, and VS Code Copilot have full support for all four hooks. Cursor and Kiro have partial support (missing SessionStart). OpenCode and KiloCode use a TypeScript plugin paradigm that provides high continuity but lacks SessionStart. OpenClaw runs context-mode as a native gateway plugin with full hook support targeting Pi Agent sessions. Antigravity and Zed have no hook support — they rely on manually-copied routing files with ~60% compliance versus ~98% for hook-enforced routing.

### Benchmark data

| Scenario | Raw | In Context | Saved |
|---|---|---|---|
| Playwright snapshot | 56.2 KB | 299 B | 99% |
| GitHub Issues (20) | 58.9 KB | 1.1 KB | 98% |
| Access log (500 requests) | 45.1 KB | 155 B | 100% |
| Analytics CSV (500 rows) | 85.5 KB | 222 B | 100% |
| Git log (153 commits) | 11.6 KB | 107 B | 99% |
| Repo research (subagent) | 986 KB | 62 KB | 94% |
| Full session aggregate | 315 KB | 5.4 KB | 98% |

### The relationship to CLI-over-MCP

Context-mode does not contradict the CLI Tools Beat MCP lesson — it completes it. The CLI lesson answers the design-time question: when building new tooling from scratch, prefer CLI+Skills over MCP servers to avoid schema overhead at session startup. Context-mode answers the runtime question: given MCP tools you must use (Playwright, GitHub APIs, third-party integrations), how do you prevent their output from consuming your context window? The two strategies are orthogonal:

- **CLI+Skills**: eliminates MCP schema overhead at session initialization (tools that load into context whether used or not)
- **Context-mode sandbox**: eliminates MCP tool output overhead at execution time (data dumped into context after each call)

A well-optimized agent architecture could use both: CLI+Skills for internal tools where schema overhead matters, context-mode sandbox for external MCP tools where output volume matters. The pattern that unifies both is Context-Aware Tool Loading — load the minimum needed, when it is needed, for the immediate task.

### Installation on Claude Code

Context-mode integrates as a Claude Code plugin via the marketplace:

```bash
/plugin marketplace add mksglu/context-mode
/plugin install context-mode@context-mode
```

The plugin registers four hooks (PreToolUse, PostToolUse, PreCompact, SessionStart) and six sandbox tools automatically. No routing file is written to the project directory. Slash commands available: `/context-mode:ctx-stats`, `/context-mode:ctx-doctor`, `/context-mode:ctx-upgrade`, `/context-mode:ctx-purge`.

### Privacy and architecture

Context-mode operates at the MCP protocol layer. All processing happens in sandboxed subprocesses on the local machine. No telemetry, no cloud sync, no account required. Session SQLite databases live in `~/.context-mode/` and are deleted when the session ends (unless `--continue` is used). Licensed under Elastic License 2.0 — source-available but cannot be offered as a hosted/managed service.

## Open Questions

- How does context-mode interact with the research wiki's existing MCP server (`research-wiki`)? The wiki MCP exposes 15 tools at session startup (schema overhead). Context-mode addresses output overhead, not schema overhead — could both be relevant simultaneously?
- Does the `ctx_fetch_and_index` + `ctx_search` pattern supersede the wiki's own `wiki_fetch` + `wiki_search` workflow, or are they complementary (wiki for structured knowledge, context-mode for ad-hoc URL research)?
- The "Think in Code" paradigm (LLM writes scripts, only stdout enters context) maps well to the wiki's pipeline tool model. Could `ctx_execute` replace `Bash` calls in ingestion pipelines to reduce context noise during long processing sessions?
- At what session length does context-mode's overhead (hook invocations, SQLite writes, snapshot construction) become worthwhile versus the savings? The benchmarks show clear wins for 30-minute+ sessions; what is the break-even point for short sessions?
- The 98% savings figure assumes hooks are active. For Claude Code specifically, do the four registered hooks (PreToolUse, PostToolUse, PreCompact, SessionStart) add measurable latency per tool call that is visible to the user?

## Relationships

- EXTENDS: Context-Aware Tool Loading
- COMPLEMENTS: CLI Tools Beat MCP for Token Efficiency
- RELATES TO: MCP Integration Architecture
- RELATES TO: Claude Code Context Management
- RELATES TO: Claude Code Skills
- RELATES TO: Claude Code
- FEEDS INTO: Research Pipeline Orchestration

## Backlinks

[[Context-Aware Tool Loading]]
[[CLI Tools Beat MCP for Token Efficiency]]
[[MCP Integration Architecture]]
[[Claude Code Context Management]]
[[Claude Code Skills]]
[[Claude Code]]
[[Research Pipeline Orchestration]]
