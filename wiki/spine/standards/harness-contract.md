---
title: "Harness Contract — Invariants for a Harness-Neutral Ecosystem"
aliases:
  - "Harness Contract"
  - "Harness-Neutral Invariants"
type: concept
domain: cross-domain
layer: spine
status: draft
confidence: high
maturity: seed
created: 2026-04-22
updated: 2026-04-22
sources:
  - id: operator-directive
    type: directive
    file: raw/notes/2026-04-22-directive-post-anthropic-self-autonomous-plan.md
  - id: e009-harness-neutrality-and-opencode-parity
    type: wiki
    file: wiki/backlog/epics/pre-milestone/E009-harness-neutrality-and-opencode-parity.md
  - id: claude-code-docs
    type: reference
    url: https://docs.anthropic.com/en/docs/claude-code
    title: "Claude Code documentation"
  - id: opencode-repo
    type: repository
    url: https://github.com/sst/opencode
    title: "sst/opencode"
tags: [concept, spine, harness, contract, standard, consumer-property-doctrine, methodology, mcp, skills, tool-semantics, cost-tracking]
---

# Harness Contract — Invariants for a Harness-Neutral Ecosystem

## Summary

This document defines the invariants any AI-coding harness (Claude Code, OpenCode, Gemini CLI, a custom wrapper) must provide for the research wiki + pipeline + skills + MCP ecosystem to function without modification. It turns "harness-neutral" from an aspiration into a measurable contract: each section states a *requirement*, maps how current harnesses implement it, and names the minimum compliance test a candidate harness runs to prove it meets the bar.

The contract exists because operator directive **2026-04-22** makes harness interchangeability load-bearing:

> "Every `.agents` or `.gemini` or `.claude` can be treated as equivalent to us. Every ecosystem needs one and to us it's the same thing."

> "We will personally stay on Claude Code for now but evolve our reasoning to be compatible with OpenCode or other real community service that won't lower quality or service with time."

The wiki, the pipeline, the skills, and the MCP servers are the load-bearing artifacts; the harness that drives them is interchangeable. This document codifies the interface.

> [!info] Document status
> Skeleton drafted 2026-04-22 as part of [[E009-harness-neutrality-and-opencode-parity|E009 M004]]. Sections fill in as E009 M002 (MCP continuity) and M003 (skill portability) produce empirical data from OpenCode. Status will advance from `draft` → `growing` → `mature` as gaps close.

## Key Insights

1. **The load-bearing artifacts are not in the harness.** The wiki, the pipeline, the MCP servers, and the skills are durable across harness change; the harness is a thin driver. Any time a feature feels "Claude-Code-specific", ask whether it could live in an MCP server or a skill instead — the answer is usually yes, and that move preserves portability.

2. **MCP is the universal widening point.** Tool sets that live inside the harness binary are brittle; tool sets that live in MCP servers are portable by construction. If the harness supports MCP, new capabilities added to the ecosystem inherit that portability for free.

3. **Skills are portable via convention, not via format.** Markdown + YAML frontmatter is a low-commitment shared format. As long as both harnesses can read `/<name> <args>` and pass the args through, the skill content itself is already portable — no translator layer needed for most cases.

4. **Compliance is measurable, not aspirational.** The 12-test compliance suite (§ Compliance test suite) turns "is this harness usable?" from debate into evidence. A 9/12 score with named gaps is actionable — you know exactly what's missing and can either adapt or contribute upstream.

5. **The contract exists to *preserve* operator choice, not to constrain it.** If Claude Code's subscription model changes or OpenCode introduces a compelling UX, the switch cost for the operator is the delta between the two harnesses' compliance scores — typically small, and with named fixes.

## Deep Analysis

### Why this contract, not a new standard?

Existing MCP is a *protocol* standard: it tells servers how to expose tools and harnesses how to call them. It does not constrain hook event models, skill file formats, memory scopes, or cost-attribution fields. The Harness Contract fills that gap with the minimum necessary invariants — enough to guarantee ecosystem portability without dictating implementation. It layers *on top of* MCP, not in competition with it.

### Design axes the contract deliberately leaves open

- **TUI vs headless** — OpenCode is TUI-first, Claude Code supports TUI + headless, a future harness could be pure API. The contract requires none; all tool/hook/skill/MCP semantics work headless.
- **Streaming vs non-streaming** — both are acceptable. Cost-tracking §6 specifies tokens in+out; it does not require per-chunk emission.
- **Local vs remote inference** — the contract is agnostic. A harness that only routes to a local KTransformers server satisfies the contract as long as it meets §1–§6.
- **Language/runtime of the harness binary** — Claude Code ships a Node/binary mix; OpenCode is Bun-based; a custom wrapper could be Python. Contract compliance is observable at the interface; the binary's implementation is free to choose.

### Failure modes the contract is designed to prevent

| Failure mode | Prevented by |
|--------------|--------------|
| Skills become Claude-Code-specific, trapping operator | §3 requires portable format + invocation |
| Memory lives only in-harness, vanishes when switching | §4 requires durable per-user scope |
| MCP servers accidentally depend on Claude-specific tool shapes | §1 stable tool names across harnesses |
| Cost attribution only works in one harness's UI | §6 requires durable log with the five fields |
| A harness ships without lifecycle hooks, breaking pipeline integrations | §2 names the four minimum events |

### Contract evolution (versioning)

Semantic versioning: breaking changes to the minimum-compliance set bump major; new optional sections bump minor. Operator will be on v1.x of the contract at milestone close 2026-05-10; v2 requires explicit operator approval and a migration-cost estimate from each affected harness.

## 1. Tool semantics

### Requirement

A harness MUST expose a core set of file + shell tools with stable names and predictable contracts. At minimum:

- **Read** — read a file at an absolute path; accept optional offset/limit for large files.
- **Write** — write (or overwrite) a file at an absolute path; create parent dirs as needed.
- **Edit** — apply string replacements or structural edits to an existing file without full rewrite.
- **Glob** — find files by pattern; return paths, typically sorted by mtime.
- **Grep** — regex search across files with include/exclude globs.
- **Bash** (or equivalent shell executor) — run shell commands with a working directory and timeout.

### Current harness mapping

| Harness | Read | Write | Edit | Glob | Grep | Shell |
|---------|------|-------|------|------|------|-------|
| Claude Code | `Read` | `Write` | `Edit` | `Glob` | `Grep` | `Bash` |
| OpenCode | (TBD — audit in E009 M001) | (TBD) | (TBD) | (TBD) | (TBD) | (TBD) |
| Gemini CLI (hypothetical) | `read_file` | `write_file` | `replace_in_file` | `glob` | `grep` | `run_shell_command` |

### Minimum compliance test

A candidate harness reads an existing 10-line file, appends 3 lines via Edit (not Write), globs the directory, greps for a token, runs `ls` via shell — all five calls succeed and return expected results.

## 2. Hook event model

### Requirement

A harness SHOULD expose lifecycle hook points so external processes can observe and optionally veto agent actions. The minimal event set:

- **SessionStart** — fires when a new session begins; payload includes working dir, session ID, harness identity.
- **UserPromptSubmit** — fires when the user sends input; can inject additional context.
- **PreToolUse** — fires before any tool call; can block or modify.
- **PostToolUse** — fires after any tool call; observes result.

Harnesses MAY add more events (Stop, PreCompact, SubagentStop, etc.), but the four above are the contract minimum.

### Current harness mapping

| Harness | SessionStart | UserPromptSubmit | PreToolUse | PostToolUse |
|---------|--------------|------------------|-----------|-------------|
| Claude Code | ✓ (settings.json hooks) | ✓ | ✓ | ✓ |
| OpenCode | (TBD) | (TBD) | (TBD) | (TBD) |
| Gemini CLI | (TBD) | (TBD) | (TBD) | (TBD) |

### Minimum compliance test

A candidate harness fires all four events, and at least one of them (PreToolUse) accepts a veto decision that prevents the tool from running.

## 3. Skill invocation convention

### Requirement

A harness MUST allow user-defined "skills" (or "agents" / "commands" / "prompts") loaded from a directory of markdown files with YAML frontmatter. Each skill is:

- **Named** — invocable as `/<name>` or equivalent.
- **Free-text argument passthrough** — anything after the name is passed to the skill body.
- **Portable** — the same file, copied into a different harness's skill dir, produces equivalent behavior.

### Current harness mapping

| Harness | Skill dir | File format | Invocation | Arg passthrough |
|---------|-----------|-------------|-----------|------------------|
| Claude Code | `.claude/skills/` + `~/.claude/skills/` | markdown + frontmatter | `/<name> <args>` | yes |
| OpenCode | (TBD — audit in E009 M003 / T051) | (TBD) | (TBD) | (TBD) |
| Gemini CLI | (TBD) | (TBD) | (TBD) | (TBD) |

### Minimum compliance test

Drop a 10-line skill markdown file into the harness's skill dir; the skill is invocable by name; invocation with args passes them through; behavior matches the reference implementation in Claude Code.

## 4. Memory / persistence contract

### Requirement

A harness MUST distinguish between:

- **Ephemeral session state** — in-context, cleared on session end.
- **Durable per-project state** — survives sessions, scoped to a working directory (e.g., `.claude/`, `.opencode/`).
- **Durable per-user state** — survives sessions, shared across projects (e.g., `~/.claude/`, `~/.opencode/`).

Auto-memory (remembered facts about the user, feedback, project context) is durable, scoped to the user. Session transcripts and scratch notes are ephemeral unless explicitly persisted via a skill or tool.

### Current harness mapping

| Harness | Ephemeral state | Per-project | Per-user (memory) |
|---------|----------------|-------------|-------------------|
| Claude Code | in-context | `.claude/` | `~/.claude/projects/<slug>/memory/` |
| OpenCode | (TBD) | (TBD) | (TBD) |
| Gemini CLI | (TBD) | (TBD) | (TBD) |

### Minimum compliance test

Session 1: save a fact via the harness's memory mechanism. End the session. Start session 2: the fact is recalled.

## 5. MCP integration

### Requirement

A harness MUST support the **Model Context Protocol** (MCP) for tool/resource extension:

- Reads a server manifest (typically `.mcp.json` at project root, or equivalent per-harness config).
- Supports `stdio` and `http` transports at minimum.
- Discovers tools from each server via MCP `tools/list`.
- Calls tools via MCP `tools/call`.
- Passes through any auth config the server declares.

### Current harness mapping

| Harness | Manifest | Transports | Auth passthrough |
|---------|----------|-----------|------------------|
| Claude Code | `.mcp.json` (project) + client config (user) | stdio, http | env vars |
| OpenCode | (TBD — audit in E009 M002) | (TBD) | (TBD) |
| Gemini CLI | (TBD) | (TBD) | (TBD) |

### Minimum compliance test

Configure the `research-wiki` MCP server. The candidate harness lists ≥20 tools from it. `wiki_status` returns the same response as Claude Code.

## 6. Cost tracking contract

### Requirement

A harness MUST expose, per tool call or per LLM call, at minimum:

- **Provider** (e.g., `openrouter`, `anthropic`, `local-ktransformers`).
- **Model id** (e.g., `moonshotai/kimi-k2.6`).
- **Prompt tokens + completion tokens**.
- **Estimated cost in USD** (may be 0.0 for local inference).

These fields SHOULD be available both in-session (for display) and in a durable log (for post-hoc rollup by tools like `aicp routing-report`).

### Current harness mapping

| Harness | Per-call cost | Durable log | Rollup API |
|---------|---------------|-------------|-----------|
| Claude Code | yes (status line) | yes (conversation JSONL) | via `/cost` |
| OpenCode | (TBD) | (TBD) | (TBD) |
| Gemini CLI | (TBD) | (TBD) | (TBD) |

### Minimum compliance test

Run a 100-token completion. Read the harness's log. Find an entry with all five fields. Compare the cost to the provider's dashboard for the same request.

## Compliance summary (to be filled by T056)

| Section | Claude Code | OpenCode | Gemini CLI |
|---------|-------------|----------|-----------|
| 1. Tool semantics | ✓ full | TBD | TBD |
| 2. Hook event model | ✓ full | TBD | TBD |
| 3. Skill invocation | ✓ full | TBD | TBD |
| 4. Memory/persistence | ✓ full | TBD | TBD |
| 5. MCP integration | ✓ full | TBD | TBD |
| 6. Cost tracking | ✓ full | TBD | TBD |

## Compliance test suite (stub — fills in T056)

12 tests total, 2 per section. Each test produces a pass/fail artifact; aggregate to a one-line compliance score (e.g., "9/12 compliant — gaps in §3 skill arg passthrough, §6 durable log"). Candidate harness that scores 12/12 is **contract-compliant**; anything less is usable with noted gaps.

## Open questions

> [!question] Should the contract name specific tool schemas (JSON schema for Read, Edit, etc.), or stay at the "stable names + predictable contract" level?
> Leaning toward the latter for portability; the former creates a hard dependency on one harness's exact schema.

> [!question] How does the contract handle harness-specific capabilities (e.g., Claude Code's sub-agent dispatch, OpenCode's TUI rendering)?
> Out-of-scope extensions are fine; they don't affect contract compliance.

> [!question] What's the versioning story for the contract itself?
> Semantic versioning. Breaking changes to the minimum-compliance set bump major; new optional sections bump minor.

## Relationships

- PART OF: [[E009-harness-neutrality-and-opencode-parity|E009 — Harness Neutrality + OpenCode Parity]]
- BUILDS ON: [[2026-04-22-directive-post-anthropic-self-autonomous-plan|Post-Anthropic Directive]]
- REFERENCED BY: [[e009-m001-opencode-install-and-base-config|E009 M001 — OpenCode install]]
- REFERENCED BY: [[e009-m002-mcp-server-continuity|E009 M002 — MCP continuity]]
- REFERENCED BY: [[e009-m003-skill-portability|E009 M003 — Skill portability]]

## Backlinks

[[E009 — Harness Neutrality + OpenCode Parity]]
[[Post-Anthropic Directive]]
[[E009 M001 — OpenCode install]]
[[E009 M002 — MCP continuity]]
[[E009 M003 — Skill portability]]
