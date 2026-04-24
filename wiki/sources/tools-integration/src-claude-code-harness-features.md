---
title: "Synthesis — Claude Code Harness: Skills, Hooks, Plugins, Subagents, MCP (2026)"
aliases:
  - "Synthesis — Claude Code Harness: Skills, Hooks, Plugins, Subagents, MCP (2026)"
  - "Claude Code Harness Features"
  - "Claude Code 2026 Feature Reference"
type: source-synthesis
layer: 1
maturity: growing
domain: tools-and-platforms
status: synthesized
confidence: high
created: 2026-04-23
updated: 2026-04-23
sources:
  - id: cc-skills-docs
    type: documentation
    url: https://code.claude.com/docs/en/skills
    title: "Extend Claude with skills — Claude Code Docs"
    ingested: 2026-04-23
  - id: cc-hooks-guide
    type: documentation
    url: https://code.claude.com/docs/en/hooks-guide
    title: "Automate workflows with hooks — Claude Code Docs"
    ingested: 2026-04-23
  - id: cc-subagents
    type: documentation
    url: https://code.claude.com/docs/en/sub-agents
    title: "Create custom subagents — Claude Code Docs"
    ingested: 2026-04-23
  - id: cc-agent-sdk
    type: documentation
    url: https://platform.claude.com/docs/en/agent-sdk/overview
    title: "Agent SDK overview — Claude API Docs"
    ingested: 2026-04-23
  - id: cc-plugins
    type: documentation
    url: https://code.claude.com/docs/en/plugins
    title: "Plugins — Claude Code Docs"
    ingested: 2026-04-23
  - id: agentskills-standard
    type: documentation
    url: https://agentskills.io
    title: "Agent Skills open standard"
    ingested: 2026-04-23
tags: [claude-code, anthropic, harness, skills, hooks, plugins, subagents, mcp, agent-sdk, agent-skills-standard, opus-4-7, 1m-context, slash-commands]
---

# Synthesis — Claude Code Harness: Skills, Hooks, Plugins, Subagents, MCP (2026)

## Summary

Claude Code is Anthropic's agentic coding CLI — a TUI harness with a structured extension system comprising **skills** (SKILL.md + YAML frontmatter, invokable by slash OR by model decision), **hooks** (8 lifecycle events including PreToolUse, PostToolUse, SessionStart, Stop), **plugins** (git-repo bundles of skills+hooks+commands+agents via marketplace), **subagents** (isolated-context parallel tasks via Claude Agent SDK), and **MCP** (.mcp.json for server wiring). As of **April 2026**, Claude Code ships Opus 4.7 support and a 1M-token context window. Skills follow the **Agent Skills open standard** at agentskills.io, making them portable across AI tools. This synthesis captures the actual feature surface — what each system is, where it lives on disk, how it's invoked, what fields the YAML frontmatter accepts — so the wiki's framework references the product accurately instead of abstracting it.

## Key Insights

> [!info] Skills are the primary extension mechanism in 2026
> Custom commands have been **merged into skills**. A file at `.claude/commands/deploy.md` and a skill at `.claude/skills/deploy/SKILL.md` both create `/deploy` and work identically. Skills add optional features: supporting files directory, frontmatter to control invocation, and automatic loading by Claude when relevant. The transition signal: use skills for new work; existing `.claude/commands/` files keep working.

> [!tip] Skills invocation is dual-mode by default
> Both you AND Claude can invoke any skill. You type `/skill-name`; Claude decides based on the `description` frontmatter field. Two knobs control this:
> - `disable-model-invocation: true` — only you can invoke (good for `/commit`, `/deploy`, anything with side effects)
> - `user-invocable: false` — only Claude can invoke (good for background reference material not actionable as a command)

> [!abstract] The 4 skill-storage locations (priority order)
>
> | Location | Path | Applies to |
> |---|---|---|
> | Enterprise | Managed settings | Org-wide |
> | Personal | `~/.claude/skills/<name>/SKILL.md` | All your projects |
> | Project | `.claude/skills/<name>/SKILL.md` | This project only |
> | Plugin | `<plugin>/skills/<name>/SKILL.md` + `plugin-name:skill-name` namespace | Where plugin is enabled |
>
> Conflicts resolve by priority: enterprise > personal > project. Plugin skills use namespacing so they don't conflict.

> [!warning] Skills content lifecycle matters for budget
> When invoked, the rendered SKILL.md enters the conversation once and stays. Claude Code does NOT re-read on later turns. Auto-compaction carries skills forward at ≤5,000 tokens each within a combined 25,000-token budget, older skills dropped first. Write standing instructions, not one-time steps. Re-invoke after compaction if content seems lost.

## Deep Analysis

### Skills — Full Frontmatter Reference

Verified from Claude Code Skills docs (2026-04-23):

| Field | Required | Purpose |
|---|---|---|
| `name` | No | Display name / slash command name; defaults to directory name; lowercase alphanumeric + hyphens, max 64 chars |
| `description` | Recommended | What the skill does; Claude uses this to decide auto-invocation; capped with `when_to_use` at 1,536 chars combined |
| `when_to_use` | No | Trigger phrases / example requests appended to `description` |
| `argument-hint` | No | Autocomplete hint like `[issue-number]` |
| `arguments` | No | Named positional args for `$name` substitution |
| `disable-model-invocation` | No | If `true`, only you can invoke |
| `user-invocable` | No | If `false`, only Claude can invoke; hidden from `/` menu |
| `allowed-tools` | No | Tools usable without per-request approval when skill is active |
| `model` | No | Override session model for the turn (accepts `/model` values or `inherit`) |
| `effort` | No | `low` / `medium` / `high` / `xhigh` / `max` — thinking budget per turn |
| `context` | No | Set `fork` to run in a subagent context |
| `agent` | No | Which subagent type (`Explore`, `Plan`, `general-purpose`, or custom) |
| `hooks` | No | Hooks scoped to this skill's lifecycle |
| `paths` | No | Glob patterns limiting auto-invocation to specific files |
| `shell` | No | `bash` (default) or `powershell` for inline `!`...` commands |

Available string substitutions in skill content: `$ARGUMENTS`, `$ARGUMENTS[N]`, `$N` (shorthand), `$name` (if `arguments` declared), `${CLAUDE_SESSION_ID}`, `${CLAUDE_SKILL_DIR}`.

Inline shell injection: `` !`command` `` syntax runs shell before Claude sees the skill content — the output replaces the placeholder. Multi-line via fenced ` ```! ` blocks. Disable via `"disableSkillShellExecution": true` in settings.

### Hooks — 8 Lifecycle Events

| Hook | Fires when | Can modify / block? |
|---|---|---|
| `SessionStart` | Session begins (incl. after compaction with `compact` matcher) | Writes stdout → injected into Claude's context |
| `UserPromptSubmit` | User submits a prompt | Stdout injected into context |
| `UserPromptExpansion` | Prompt is being expanded | Stdout injected into context |
| `PreToolUse` | Before a tool call | **Can deny** tool call + tell Claude why; **can escalate** to user; as of v2.0.10, can **modify tool inputs** |
| `PostToolUse` | After tool call completes | Cannot undo (tool already ran); runs cleanup |
| `PermissionRequest` | When permission dialog shown | — |
| `Stop` | Claude finishes responding (not on user interrupt) | — |
| `(+ 1 additional — full list in hooks-guide)` | | |

**Configuration locations** (priority order, lowest wins unless overridden):
- `.claude/settings.json` — project-level, shareable
- `~/.claude/settings.json` — user-level, personal
- `.claude/settings.local.json` — local-project, uncommitted

Disable all hooks with `"disableAllHooks": true`.

### Plugins — Bundling + Marketplace

A plugin is a git repository bundling: skills + hooks + slash commands + subagent definitions. Marketplaces are ALSO git repositories — a marketplace is a repo that lists plugins. Both plugins and marketplaces are "just public git repositories hosted on GitHub."

Plugin skills namespace: `plugin-name:skill-name`. No conflicts with personal/project/enterprise skills.

Relevant example for this operator's stack: the **Codex Plugin for Claude Code** (`openai/codex-plugin-cc`) — bundles `/codex:review`, `/codex:adversarial-review`, `/codex:rescue`, `/codex:status`, `/codex:result`, `/codex:cancel`, `/codex:setup` as plugin-namespaced slash commands. See [[src-codex-cli-and-claude-code-plugin|Codex CLI + Plugin synthesis]].

### Subagents (via Claude Agent SDK)

Purpose: isolate context, run tasks in parallel, apply specialized instructions. Each subagent runs in its own **fresh conversation** — intermediate tool calls and results stay inside the subagent; only the final message returns to the parent.

**Execution modes:**
- **Foreground** — blocks the main conversation until complete
- **Background** — runs concurrently while you continue working

**Permission model:** Before launching, Claude Code prompts for any tool permissions the subagent will need. Once running, subagent inherits those permissions and **auto-denies anything not pre-approved**.

**Subagent definition:** `.claude/agents/<name>.md` with its own markdown body (system prompt) + YAML frontmatter (tools, model, effort). Claude auto-dispatches based on the subagent's `description` field.

**Preload skills into subagent:** use the `skills` field in a subagent definition — loads full skill content at startup (vs regular session where descriptions are in context but full skills only load on invocation).

**Parallelization pattern:** main agent can spin up multiple subagents concurrently for disjoint work (e.g., explore 3 directories in parallel, each returning a digest).

### MCP — Model Context Protocol

Configured via `.mcp.json` at project root. Each entry: `command` + `args` + `cwd` (all absolute paths, no tilde expansion). MCP servers expose tools that become callable from Claude Code with the `mcp__<server>__<tool>` prefix.

This wiki's own MCP server (`tools/mcp_server.py`) is an example — 26+ tools prefixed `mcp__research-wiki__*`.

### Slash commands — built-in bundled skills

Claude Code ships **bundled skills** available in every session — prompt-based, not fixed logic. Examples: `/simplify`, `/batch`, `/debug`, `/loop`, `/claude-api`, `/init`, `/review`, `/security-review`, `/compact`, `/help`.

Typing `/` shows the full list (expands with plugin + project + personal + enterprise skills).

### Memory — CLAUDE.md files

Persistent context loaded per session:
- Project: `./CLAUDE.md` at repo root
- Personal: `~/.claude/CLAUDE.md` (global across projects)
- Memory system: `~/.claude/projects/<slug>/memory/MEMORY.md` (index) + individual memory files

Load CLAUDE.md from `--add-dir` directories via `CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1`.

### Permissions + Approval

Permission rules govern tool access. Syntax examples:
- `Skill` — blanket deny all skills via Skill tool
- `Skill(commit)` — exact skill match
- `Skill(review-pr *)` — prefix match with any args
- `Bash(git add *)` — tool + pattern

`allowed-tools` in a skill's frontmatter grants pre-approval for the listed tools while that skill is active.

### 2026 Update — Opus 4.7 + 1M context

As of April 2026: Claude Code ships weekly. Opus 4.7 is current; 1M-token context window is supported on Opus.

## Cross-References to wiki

- [[src-codex-cli-and-claude-code-plugin|Codex CLI + Codex Plugin for Claude Code]] — paired synthesis; the `openai/codex-plugin-cc` plugin is the concrete example of a Claude Code plugin bridging another provider's product
- [[ai-infrastructure-decision-framework-2026|AI Infrastructure Decision Framework 2026]] — Claude Code harness is separable from the Claude model; run via `ANTHROPIC_BASE_URL` against any compatible endpoint
- [[mcp-vs-cli-decision-vs-lesson|MCP vs CLI — Decision vs Lesson]] — this synthesis documents Claude Code's MCP support but the operator's default is CLI-first
- [[model-skills-commands-hooks|Model — Skills, Commands, and Hooks]] — the wiki's existing model-level abstraction; this synthesis provides the concrete 2026 product detail

## State of Knowledge

| Claim | Verified? | Evidence |
|---|---|---|
| Skills have YAML frontmatter with 16 documented fields | ✅ | code.claude.com/docs/en/skills |
| Skills follow Agent Skills open standard (agentskills.io) | ✅ | Skills docs |
| 4 skill locations: enterprise / personal / project / plugin | ✅ | Skills docs |
| Custom commands merged into skills | ✅ | Skills docs note |
| 8 hook events incl. PreToolUse, PostToolUse, SessionStart, Stop | ✅ | Hooks guide |
| PreToolUse can deny/modify tool calls (v2.0.10+) | ✅ | Hooks guide |
| Plugins = git repos bundling skills/hooks/commands/agents | ✅ | Plugins docs |
| Marketplaces = git repos that list plugins | ✅ | Plugins docs |
| Plugin skills use `plugin-name:skill-name` namespace | ✅ | Skills docs |
| Subagents run in fresh conversation, only final msg returns | ✅ | Subagents docs |
| Subagents support foreground + background execution | ✅ | Agent SDK overview |
| MCP configured via `.mcp.json` with absolute paths | ✅ | Operator-confirmed + Anthropic MCP docs |
| Opus 4.7 + 1M context window shipping April 2026 | ✅ | Claude Code changelog / search results |
| Bundled skills include /simplify, /batch, /debug, /loop, /claude-api | ✅ | Commands reference |

## Relationships

- BUILDS ON: [[ai-infrastructure-decision-framework-2026|AI Infrastructure Decision Framework 2026]] — the harness is one of the framework's specialties, valuable independently of which model runs inside
- BUILDS ON: [[src-codex-cli-and-claude-code-plugin|Codex CLI + Codex Plugin for Claude Code]] — sister synthesis; the Codex plugin is a concrete demonstration of the plugin system documented here
- RELATES TO: [[model-skills-commands-hooks|Model — Skills, Commands, and Hooks]]
- RELATES TO: [[model-claude-code|Model — Claude Code]]
- FEEDS INTO: [[aicp|AICP]] — AICP routes through `ANTHROPIC_BASE_URL`, so Claude Code harness features are usable with non-Claude backends
- DEMONSTRATES: [[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4]] — this synthesis is the verified-product-doc replacement for prior abstractions about "what Claude Code offers"

## Backlinks

[[ai-infrastructure-decision-framework-2026|AI Infrastructure Decision Framework 2026]]
[[Codex CLI + Codex Plugin for Claude Code]]
[[model-skills-commands-hooks|Model — Skills, Commands, and Hooks]]
[[model-claude-code|Model — Claude Code]]
[[aicp|AICP]]
[[Principle 4]]
