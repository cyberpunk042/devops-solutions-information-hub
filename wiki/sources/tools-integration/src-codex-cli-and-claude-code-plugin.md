---
title: "Synthesis — OpenAI Codex CLI and the Codex Plugin for Claude Code"
aliases:
  - "Synthesis — OpenAI Codex CLI and the Codex Plugin for Claude Code"
  - "Codex CLI Synthesis"
  - "Codex Plugin for Claude Code"
  - "codex-plugin-cc"
type: source-synthesis
layer: 1
maturity: growing
domain: tools-and-platforms
status: synthesized
confidence: high
created: 2026-04-23
updated: 2026-04-23
sources:
  - id: codex-cli-features
    type: documentation
    url: https://developers.openai.com/codex/cli/features
    title: "Features — Codex CLI | OpenAI Developers"
    ingested: 2026-04-23
  - id: codex-cli-slash-commands
    type: documentation
    url: https://developers.openai.com/codex/cli/slash-commands
    title: "Slash commands in Codex CLI | OpenAI Developers"
    ingested: 2026-04-23
  - id: codex-plugin-cc-repo
    type: repository
    url: https://github.com/openai/codex-plugin-cc
    title: "openai/codex-plugin-cc — Use Codex from Claude Code to review code or delegate tasks"
    ingested: 2026-04-23
  - id: codex-cli-home
    type: documentation
    url: https://developers.openai.com/codex/cli
    title: "CLI — Codex | OpenAI Developers"
    ingested: 2026-04-23
  - id: codex-plugin-cc-community
    type: article
    url: https://community.openai.com/t/introducing-codex-plugin-for-claude-code/1378186
    title: "Introducing Codex Plugin for Claude Code — OpenAI Developer Community"
    ingested: 2026-04-23
tags: [codex, codex-cli, openai, claude-code, adversarial-review, plugin, slash-commands, mcp, agent-skills, gpt-5-5, code-review, tools-integration]
---

# Synthesis — OpenAI Codex CLI and the Codex Plugin for Claude Code

## Summary

**Codex CLI** is OpenAI's coding-workflow CLI product (not the Codex model family — the product shares the name). It is a full-screen terminal UI with its own command grammar, slash commands, approval modes, MCP support, agent skills, and session management. Recommended model: **gpt-5.5**. On **2026-03-30**, OpenAI released **Codex Plugin for Claude Code** (`openai/codex-plugin-cc`) — a plugin that exposes Codex's review and delegation workflows as `/codex:*` slash commands INSIDE Claude Code, making Codex a first-class specialist callable from Anthropic's harness. The most distinctive feature for mission-aligned use is **`/codex:adversarial-review`** — a steerable review that assumes code is broken and hunts assumption failures, with structured JSON output (severity, line numbers, impact, suggested fixes). This synthesis captures Codex's actual feature surface accurately — not as an abstract "adversarial review pattern," but as concrete product commands with their real flags, behaviors, and integration points.

## Key Insights

> [!info] Codex CLI is a product, adversarial-review is a command
> Adversarial review is not a generic multi-model pattern to reinvent — it is a specific slash command (`/codex:adversarial-review`) in the Codex Plugin for Claude Code, with documented flags (`--base`, `--background`, `--wait`, `--resume`, `--fresh`), a specific behavior (read-only critique), and a structured JSON output format (severity ratings + file paths + line numbers + impact analysis + suggested fixes). Use the command; don't rebuild it.

> [!tip] Codex + Claude Code is the "use both harnesses" path
> The plugin bridges OpenAI's and Anthropic's coding products. Inside Claude Code you can now invoke `/codex:review`, `/codex:adversarial-review`, `/codex:rescue` (delegation), `/codex:status`, `/codex:result`, `/codex:cancel`, `/codex:setup`. This is specialty-routing at the harness layer: Claude Code for daily authoring, Codex commands for specialist review + rescue delegation, without leaving Claude Code.

> [!abstract] The seven attack surfaces the adversarial-review tests
> Per the plugin docs, `/codex:adversarial-review` explicitly assumes the code is broken and hunts on these surfaces: **authentication · data loss · rollbacks · race conditions · dependencies · version skew · observability**. These are the class of failure modes that routine single-model review typically misses because the model that wrote the code is confident about the code. Steerable via free-text focus after flags (e.g. "look for race conditions").

- **Codex CLI is not just a model wrapper.** It's a TUI (full-screen terminal app), a session manager (`exec`, `fork`, `resume`), an approval model (auto/read-only/full-access), a slash-command surface, a plugin system, an MCP client, and a configuration layer (`~/.codex/config.toml`). Treating it as "just another way to call GPT-5.5" misses the product.

- **Slash command grammar.** Codex CLI's native slashes are organized by category: model/performance (`/model`, `/fast`, `/personality`), session (`/clear`, `/new`, `/fork`, `/resume`, `/plan`), permissions (`/permissions`, `/sandbox-add-read-dir`), navigation (`/status`, `/agent`, `/diff`, `/mention`), utilities (`/compact`, `/copy`, `/mcp`, `/apps`, `/plugins`, `/ps`, `/stop`), configuration (`/init`, `/statusline`, `/title`, `/debug-config`, `/experimental`, `/feedback`, `/logout`, `/quit`). Parallels Claude Code's slash surface but with different specializations.

- **Approval modes are structural, not prompt-level.** Auto (default — read/edit/run in cwd), Read-only (browse, approve every change), Full Access (cross-machine + network). Matches Claude Code's permission mode system but with different naming and defaults.

- **MCP support is first-class.** `codex mcp` subcommand to list/add/remove/authenticate servers. `/mcp` slash to inspect. Codex can also run AS an MCP server — meaning Claude Code could call Codex that way, or vice versa.

- **Agent Skills.** Codex has its own "Agent Skills" system, documented separately. Not identical to Claude Code's `.claude/skills/` but analogous — reusable domain instructions tied to trigger phrases.

- **Plugin marketplaces.** `codex plugin` subcommand manages plugin marketplaces from Git or local sources. The `codex-plugin-cc` repo is one such marketplace item, published to Claude Code's plugin system rather than Codex's own.

- **Background execution.** Every plugin command supports `--background` + `/codex:status` polling + `/codex:cancel`. Important for adversarial-review: you can kick off the review async, continue working, pick up results later. Different from Claude Code's mostly-synchronous flow.

- **Session resumption.** `codex resume` reopens earlier threads with same repository state. `codex resume --last` jumps to most recent. `fork` branches from any transcript point. This is richer than Claude Code's session model and useful for long-horizon review workflows.

- **Model default is gpt-5.5.** Not the cheapest; OpenAI's recommended model for "complex coding, computer use, knowledge work, and research workflows." Other models available via `/model`. Mission implication: **Codex CLI is GPT-tier by default**; running it assumes you're paying OpenAI API rates per call.

## Deep Analysis

### The Codex Plugin for Claude Code — command-by-command

| Command | What it does | Flags |
|---|---|---|
| **`/codex:review`** | Standard code review on uncommitted changes or branch comparisons | `--background`, `--wait`, free-text focus |
| **`/codex:adversarial-review`** | Steerable review challenging design choices and assumptions | `--base <ref>`, `--background`, `--wait`, `--resume`, `--fresh`, free-text focus |
| **`/codex:rescue`** | Delegate tasks to Codex (investigate bugs, attempt fixes, continue work) | `--background`, `--wait` |
| **`/codex:status`** | Check progress on running/recent Codex jobs | — |
| **`/codex:result`** | Display final output from completed jobs with session IDs | `<session-id>` |
| **`/codex:cancel`** | Stop active background tasks | `<session-id>` |
| **`/codex:setup`** | Verify installation, authentication, and configure review gates | — |

Typical adversarial-review invocation:
```
/codex:adversarial-review --base main challenge whether this was the right caching design
/codex:adversarial-review --background look for race conditions
```

Output: **read-only** — the command does not modify code. Returns structured JSON (severity: critical/high/medium/low, file paths, line numbers, impact analysis, suggested fixes). The operator/author model reconciles.

### Codex CLI core commands (native, not plugin)

| Command | Purpose |
|---|---|
| `codex` | Launch interactive TUI |
| `codex "prompt"` | Launch TUI with initial prompt |
| `codex exec "task"` | Non-interactive run, streams to stdout / JSONL |
| `codex resume` | Reopen earlier thread |
| `codex resume --last` | Jump to most recent session |
| `codex fork` | Branch a previous session |
| `codex app-server` | Run workspace on remote machine (WebSocket access) |
| `codex cloud` | Triage and launch cloud tasks from terminal |
| `codex features` | Inspect/persist feature flags |
| `codex completion` | Generate shell completion scripts |
| `codex mcp` | Manage MCP servers |
| `codex plugin` | Manage plugin marketplaces |

Key flags for scripting: `--model gpt-5.5`, `--json`, `-i screenshot.png` (image input), `--remote ws://host:port`, `--cd <path>`, `--add-dir`.

### The approval model

- **Auto** (default) — read files, edit, run commands in cwd without prompting
- **Read-only** — browse files, approve every change/command
- **Full Access** — cross-machine + network unrestricted

Switch mid-session via `/permissions`. Windows sandbox gets per-directory grants via `/sandbox-add-read-dir`.

### Integration with AICP / wiki routing

For the operator's stack, Codex CLI sits naturally as a **specialty backend that a session flips to** when the job fits Codex's surface:

- `codex:adversarial-review` for irreversible / high-stakes code decisions
- `codex:rescue` when stuck on a bug — delegate to Codex rather than burning more author-model cycles
- `codex:review` as a cheaper-than-adversarial-review sanity check on uncommitted changes

The plugin lives inside Claude Code, so the session context switch is minimal — you stay in Claude Code, invoke `/codex:*`, get Codex output in the same transcript. AICP's `tier_map` can surface this as "when task is a code review and the operator has Codex configured, suggest `/codex:review` instead of routing through a general model."

### Comparison surface — Codex CLI vs Claude Code

| Dimension | Codex CLI | Claude Code |
|---|---|---|
| Model family | gpt-5.x (default gpt-5.5) | Claude Opus/Sonnet (default varies) |
| TUI | ✅ Full-screen | ✅ Full-screen |
| Slash commands | Extensive (`/model`, `/fast`, `/personality`, etc.) | Extensive (different names) |
| Plugin system | `codex plugin` subcommand | Plugin marketplace via `.claude/plugins/` |
| MCP support | ✅ (`codex mcp`, `/mcp`) | ✅ (`.mcp.json`) |
| Agent Skills | ✅ (separate Agent Skills system) | ✅ (`.claude/skills/`) |
| Approval modes | Auto / Read-only / Full Access | Permission modes (similar shape, different names) |
| Session resume | ✅ `codex resume`, `fork` | ✅ `--resume` |
| Background tasks | ✅ via `--background` + `/codex:status` | ✅ via `run_in_background` tool |
| Cloud tasks | ✅ `codex cloud` subcommand | Via Claude agent cloud features |
| Review commands | ✅ `/review` native + `/codex:*` via plugin | Via skills / MCP tools |
| MCP server export | ✅ Can run as MCP server | ✅ (Claude Agent SDK) |

Neither strictly dominates the other on feature surface; the distinctive Codex features are **the adversarial-review specialty and the rescue-delegation workflow**.

### What this means for the AI Infrastructure framework

The [[ai-infrastructure-decision-framework-2026|framework's]] "Specialty Routing" section correctly identified Codex CLI as a specialist tool. The correction to make: adversarial-review is not an abstract routing pattern to build in AICP — it is a Codex plugin command to **invoke** from Claude Code via `/codex:adversarial-review`. The framework now routes that session-scenario directly to the command, not to a reinvented pipeline.

## Cross-References

- [[ai-infrastructure-decision-framework-2026|AI Infrastructure Decision Framework 2026]] — Codex is one of the specialists in the routing table
- [[src-kimi-k2-6-moonshot-agent-swarm|Kimi K2.6]] — K2.6 is the mission-aligned default author model; `/codex:adversarial-review` is the natural pair for high-stakes K2.6 output
- [[mcp-vs-cli-decision-vs-lesson|MCP vs CLI — Decision vs Lesson]] — Codex CLI + plugin is a CLI-first product with MCP as a secondary surface, consistent with the operator's stack
- [[src-claude-code|Claude Code]] (wiki page — may exist) — Codex Plugin for Claude Code bridges both harnesses

## State of Knowledge

| Claim | Verified? | Evidence |
|---|---|---|
| Codex Plugin for Claude Code released 2026-03-30 | ✅ | OpenAI Developer Community announcement + search results dated correctly |
| `/codex:adversarial-review` is a real slash command | ✅ | `openai/codex-plugin-cc` repo + plugin docs |
| Seven attack surfaces (auth, data loss, rollbacks, race conditions, dependencies, version skew, observability) | ✅ | Plugin docs directly list these |
| Flags: `--base`, `--background`, `--wait`, `--resume`, `--fresh` | ✅ | Plugin docs |
| Output is read-only + structured JSON | ✅ | Plugin docs |
| Full plugin command list (7 commands: review/adversarial-review/rescue/status/result/cancel/setup) | ✅ | Plugin repo docs |
| Codex CLI default model is gpt-5.5 | ✅ | Codex CLI docs |
| Codex CLI slash commands (categorized list) | ✅ | Codex CLI slash-commands docs |
| `codex mcp`, `codex plugin`, `codex exec`, `codex fork`, `codex resume` subcommands | ✅ | Codex CLI reference |
| Three approval modes (auto / read-only / full access) | ✅ | Codex CLI features docs |

## Next Steps for the Operator

1. **Install the plugin** (when ready): follow `openai/codex-plugin-cc` README to install into Claude Code; requires Codex CLI auth set up separately.
2. **Run `/codex:setup`** once post-install to verify auth + configure any review gates.
3. **First real use: run `/codex:adversarial-review --base main` on the current session's branch** to see the output format and decide if the structured critique is usefully actionable for the operator's workflow.
4. **Budget** — Codex CLI defaults to gpt-5.5 (OpenAI frontier pricing). Adversarial-review runs on a subset of diff, not the whole repo — typical cost per review is small, but log it as a specialty-routing OpenAI spend in the AI Infrastructure framework's mission-exception tracking.
5. **Decide whether to wire into AICP**: initially keep Codex as an operator-invoked specialty (via Claude Code slashes). Only consider AICP-automated routing if the plugin's command becomes a frequent manual invocation.

## Relationships

- BUILDS ON: [[ai-infrastructure-decision-framework-2026|AI Infrastructure Decision Framework 2026]] — Codex is one of the framework's specialty-routing providers; this synthesis documents it accurately instead of abstracting
- RELATES TO: [[src-kimi-k2-6-moonshot-agent-swarm|Synthesis — Kimi K2.6]] — K2.6 (author) + Codex (critic via `/codex:adversarial-review`) is a concrete specialty pair
- RELATES TO: [[mcp-vs-cli-decision-vs-lesson|MCP vs CLI — Decision vs Lesson]] — Codex CLI is a CLI-first product; fits the MCP-vs-CLI tradeoff analysis
- FEEDS INTO: [[aicp|AICP]] — when AICP surfaces task classes that match Codex commands, it can prompt the operator
- DEMONSTRATES: [[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4]] — the prior version of this material in the wiki was an **abstracted pattern**; this synthesis replaces it with the **verified product feature**, which is the correct level of abstraction

## Backlinks

[[ai-infrastructure-decision-framework-2026|AI Infrastructure Decision Framework 2026]]
[[Synthesis — Kimi K2.6]]
[[MCP vs CLI — Decision vs Lesson]]
[[aicp|AICP]]
[[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4]]
