---
title: "Synthesis — OpenCode Harness: Build/Plan Modes, LSP, Multi-Session, AGENTS.md, 75+ Providers (2026)"
aliases:
  - "OpenCode Harness Features"
  - "OpenCode Synthesis"
  - "OpenCode 2026"
type: source-synthesis
layer: 1
maturity: growing
domain: tools-and-platforms
status: synthesized
confidence: high
created: 2026-04-23
updated: 2026-04-23
sources:
  - id: opencode-docs
    type: documentation
    url: https://opencode.ai/docs/
    title: "OpenCode Documentation (official)"
    ingested: 2026-04-23
  - id: opencode-lsp-docs
    type: documentation
    url: https://opencode.ai/docs/lsp/
    title: "LSP Servers — OpenCode"
    ingested: 2026-04-23
  - id: opencode-plugins-docs
    type: documentation
    url: https://opencode.ai/docs/plugins/
    title: "Plugins — OpenCode"
    ingested: 2026-04-23
  - id: opencode-tools-docs
    type: documentation
    url: https://opencode.ai/docs/tools/
    title: "Tools — OpenCode"
    ingested: 2026-04-23
  - id: opencode-github
    type: repository
    url: https://github.com/opencode-ai/opencode
    title: "opencode-ai/opencode — A powerful AI coding agent built for the terminal"
    ingested: 2026-04-23
  - id: awesome-opencode
    type: repository
    url: https://github.com/awesome-opencode/awesome-opencode
    title: "awesome-opencode — Curated plugins, themes, agents, resources"
    ingested: 2026-04-23
  - id: together-opencode-guide
    type: documentation
    url: https://docs.together.ai/docs/how-to-use-opencode
    title: "How to use OpenCode with Together AI"
    ingested: 2026-04-23
tags: [opencode, harness, tui, byom, agents-md, lsp, multi-session, session-sharing, mcp, plugins, build-plan-modes, go, open-source, 75-providers, 2026]
---

# Synthesis — OpenCode Harness (2026)

## Summary

OpenCode is an open-source terminal-first AI coding harness — Go binary, 95K+ GitHub stars, 75+ LLM provider support, **LSP-native** (Language Server Protocol with 20+ languages auto-configured), **multi-session** (parallel independent contexts per workspace), **Build/Plan mode toggle** (Tab key — different execution posture), **AGENTS.md** as the cross-tool Agent Skills standard companion, and a plugin system for custom hooks. OpenCode occupies the **"tool-harness" niche** in the 2026 agentic-coding landscape — provider-agnostic, config-driven, community cadence — and is the operator's activated immediate-substitute for Claude Code per the resilience playbook. This synthesis captures the actual feature surface from the official docs (opencode.ai/docs) so the operator's toying is grounded in verified capability rather than marketing claims.

## Key Insights

> [!info] Build vs Plan modes are a first-class UX primitive (Tab key toggle)
> OpenCode distinguishes two execution modes at the TUI level — not buried in a setting, but toggled by pressing **Tab**:
> - **Build Mode**: executes code changes directly (like Claude Code default behavior)
> - **Plan Mode**: generates implementation strategies WITHOUT modifying files
>
> This is **structurally different** from Claude Code's approach (where planning vs editing is context-signaled rather than mode-switched). For operator workflows requiring explicit "think first, edit second" — design docs, refactor proposals, architecture reviews — Plan Mode is a single keystroke. Closer in spirit to Cline's dual Plan/Act modes, but with tighter TUI integration.

> [!tip] Multi-session = parallel independent contexts
> One OpenCode instance can hold multiple concurrent sessions, each with its own context window, conversation history, and model configuration. Idiomatic use: **one "research" session exploring a library + one "implementation" session writing the code, same workspace, different mental models, different cached context**. This is closer to Cursor's parallel Agent Tabs than to Claude Code's single-thread-per-terminal.

> [!abstract] LSP integration is NATIVE (not bolted on)
> OpenCode auto-downloads and configures language servers for 20+ languages. Supported operations exposed to the LLM: **goToDefinition, findReferences, hover, documentSymbol, workspaceSymbol, goToImplementation, prepareCallHierarchy, incomingCalls, outgoingCalls**. Meaning: the agent can ask "where is this function used?" and get an accurate cross-file answer without grep-prompting. This is a distinct capability class — LSP gives the agent an IDE-grade view of the codebase that string-search-based harnesses approximate but don't match.

> [!warning] `AGENTS.md` is the cross-tool standard — NOT OpenCode-specific
> OpenCode generates an `AGENTS.md` via `/init` that documents project structure + coding patterns. This file is the same Agent Skills standard (agentskills.io) that Claude Code's skills follow. Meaning: **skills and agent context written for one harness port to the other** with minimal changes. Mission-resilience payoff: the operator's investment in `.claude/skills/` and CLAUDE.md is not harness-locked.

## Deep Analysis

### Installation and surface

**Install options** (any of these works):
```
npm install -g opencode-ai/opencode
brew install opencode
pacman -S opencode      # Arch AUR
choco install opencode  # Windows
scoop install opencode
docker run opencode-ai/opencode
```

Launch: `opencode` in a project directory. TUI opens full-screen.

**Minimum first-session flow:**
1. `/connect` — configure an LLM provider (OpenRouter, direct OpenAI, Anthropic, etc. — 75+ supported)
2. `/init` — OpenCode analyzes the project and generates `AGENTS.md`
3. Prompt the agent; press **Tab** to switch Build ↔ Plan
4. Use **`@`** to fuzzy-find files and reference them inline in prompts

### Slash commands (confirmed)

| Command | Function |
|---|---|
| `/connect` | Configure LLM provider API key |
| `/init` | Analyze project + generate `AGENTS.md` |
| `/undo` | Revert last change + restore previous prompt |
| `/redo` | Restore undone changes |
| `/share` | Generate shareable conversation link (for debugging or handoff) |

The public docs surface these five explicitly. The CLI likely has more (themes, keybinds, etc. are configurable which implies slash commands or config-edit paths) — worth exploring in the operator's toying session.

### Keyboard UX

| Key | Action |
|---|---|
| `Tab` | Toggle Build ↔ Plan mode |
| `@` | Fuzzy-find files in project to reference |
| `/` | Open slash-command menu |

### Provider support — 75+ LLMs

OpenCode's distinguishing resilience feature: it wraps **75+ LLM provider endpoints** in a uniform interface. Via `/connect` you can pick from:
- **OpenAI** (GPT-5.x, Codex variants)
- **Anthropic** (Claude Opus, Sonnet)
- **Google AI** (Gemini family)
- **OpenRouter** (aggregator — gets the whole 313-model catalog at once)
- **Together AI** (175 models, own GPUs)
- **Groq** (315 TPS Llama tier)
- **Cerebras** (1M tokens/day free)
- **Ollama** (local OR Ollama Cloud — crucial for operator's current setup)
- **DeepSeek**, **Moonshot**, **Z.ai**, **Mistral**, **Perplexity**
- … and ~60 more including local providers (LM Studio, llama.cpp, vLLM, SGLang)

**OpenCode Zen** — curated pre-tested model list recommended for newcomers; reduces the "pick from 75" paralysis. For operator who already has a decision matrix, configure the specific providers from the [[ai-model-provider-harness-decision-matrix-2026|matrix]] directly.

### `AGENTS.md` — the cross-tool context file

OpenCode's `/init` generates AGENTS.md following the Agent Skills open standard (agentskills.io). Contents typically:
- Project overview and structure
- Coding conventions
- Build/test/lint commands
- Key architectural decisions
- Per-directory guidance (when to modify which paths)

**Relationship to CLAUDE.md**: similar role, similar content, but AGENTS.md is the cross-tool standard. Claude Code reads CLAUDE.md natively; OpenCode reads AGENTS.md natively; and both tools increasingly read each other's files. **For mission-resilience, the operator's project root should have BOTH CLAUDE.md and AGENTS.md** — with AGENTS.md as the neutral canonical source and CLAUDE.md as a Claude-Code-specific extension that adds skill definitions.

### LSP — the quiet differentiator

OpenCode's LSP integration auto-downloads language servers on first use. Supported per the docs:
- TypeScript/JavaScript (tsserver)
- Python (pyright, ruff)
- Rust (rust-analyzer)
- Go (gopls)
- C/C++ (clangd)
- Java (jdtls)
- PHP, Ruby, Elixir, Swift, Kotlin, Scala, Haskell, Clojure, OCaml, Lua, etc.

**What this unlocks that string-search-based harnesses can't do as well:**
- Exact callsite enumeration ("where is `fetchUser` called?") — not a grep approximation
- Symbol-accurate rename across modules
- Type-aware reasoning (agent can ask "what's the inferred type of X at line 42?")
- Cross-file dependency mapping (call hierarchies)
- Accurate goto-definition even through re-exports, type aliases, overloads

Claude Code's approach is grep + AST-via-tools. Both work, but LSP gives higher-fidelity answers for large typed codebases.

### Multi-session architecture

Multiple independent sessions in one OpenCode instance. Each session:
- Own context window (separate token budget)
- Own conversation history
- Own model configuration (research session can use Opus, implementation can use K2.6)
- Shareable independently via `/share`

**Operator use case**: the wiki-synthesis arc + the AICP-implementation arc can run as two sessions in the same OpenCode window — context from each doesn't pollute the other. Claude Code's rough equivalent is spawning subagents, but subagents are ephemeral/task-scoped rather than persistent parallel conversations.

### Plugin system

Plugins hook into OpenCode's event lifecycle and customize behavior. The `awesome-opencode` curated list covers:
- Background agents
- Memory systems (persistent context across sessions)
- Notifications (desktop / Slack / IRC on certain events)
- Specialized workflows (e.g., PR review, test-first automation)

Plugins are the primary extension mechanism — analogous to Claude Code's combined skills + hooks system but with a different API surface.

### MCP integration

OpenCode supports MCP servers. Config format is similar to Claude Code's `.mcp.json` but named differently — see OpenCode's advanced-configuration docs. Meaning: **the operator's wiki MCP server (`tools/mcp_server.py` — 26+ tools) is callable from OpenCode with roughly the same wiring effort as from Claude Code**. Mission-resilience payoff: custom MCP servers port between harnesses.

### Customization surface

- **Themes** — syntax highlighting + TUI color schemes
- **Keybinds** — override default shortcuts
- **Code formatters** — configure per-language formatting hooks
- **Custom commands** — add your own `/commands` (like Claude Code skills)
- **Rules** — project-level agent instructions via AGENTS.md
- **Tools / permissions** — which built-in tools the agent can use, per project

## How OpenCode compares to Claude Code for operator's stack

> [!abstract] Claude Code vs OpenCode — operator's practical lens
>
> | Dimension | Claude Code | OpenCode |
> |---|---|---|
> | **Default model** | Claude Opus/Sonnet (Anthropic-controlled) | Whatever `/connect` configures (operator picks) |
> | **Mode switching** | Context-signaled (plan vs act blended) | Explicit Tab toggle (Build vs Plan) |
> | **Skill format** | `.claude/skills/*.md` (SKILL.md + 16-field frontmatter) | Custom commands + AGENTS.md + plugins |
> | **Context file** | CLAUDE.md (Claude-specific) | AGENTS.md (cross-tool standard) |
> | **Code intelligence** | Grep + AST-via-tools | **LSP-native** (20+ languages, 9 operations) |
> | **Concurrent sessions** | Subagents (ephemeral, task-scoped) | Multi-session (persistent parallel contexts) |
> | **Session sharing** | No native URL-share | `/share` → URL |
> | **Plugin model** | Plugins (git-repo bundles) | Plugin system (different API) |
> | **MCP support** | ✅ native | ✅ (similar shape) |
> | **Provider flexibility** | 1 primary + `ANTHROPIC_BASE_URL` override | **75+ providers first-class** |
> | **Pricing** | $20-$200/mo subscription | Free (BYOM — you pay the model) |
> | **Mission-aligned** | Product-tier lock | **Fully mission-aligned** (open-source, no vendor) |
> | **Benchmark** | SWE-Bench 80.8% leader | Strong across benchmarks |
> | **Best at** | Polished UX, skills ecosystem, Anthropic-tight | Multi-session work, LSP-heavy codebases, provider-switching |

### When to use OpenCode vs Claude Code

> [!tip] Pragmatic routing for operator's 2026 daily work
>
> **Reach for Claude Code when**:
> - Task benefits from the skills-plus-hooks-plus-subagents ecosystem the operator has already built in this wiki
> - Using Claude Opus 4.7 specifically (tone, long-form synthesis)
> - Codex plugin commands (`/codex:adversarial-review`, `/codex:rescue`) are needed
> - The operator wants the current most-polished harness UX
>
> **Reach for OpenCode when**:
> - Switching models mid-task (pay-per-token visibility; `/connect` mid-session)
> - LSP-heavy codebase (typed TypeScript, Rust, Java) where precise symbol reasoning pays off
> - Running parallel research + implementation sessions in one workspace
> - Pure BYOM against Ollama Cloud (direct `/connect ollama`), OpenRouter, Cerebras-free, Together
> - Testing a new model you haven't used before (75+ provider catalog makes experimentation cheap)
> - Building agent configurations that must be portable across harnesses (AGENTS.md is the right anchor)
>
> **Both are usable same-session-same-workspace** — AGENTS.md is readable by both. `ollama launch claude` would run Claude Code against Ollama models; `/connect ollama` in OpenCode does the same for OpenCode. No lock-in at either layer.

## Ollama Cloud catalog (verified 2026-04-23, operator has login)

Since the operator has Ollama login active, these cloud models are immediately callable via `/connect ollama` in OpenCode or `ollama launch claude --model <id>` for Claude Code:

| Model ID | Parameters | Features | Context |
|---|---|---|---|
| `kimi-k2.6` | — | vision + tools + thinking | 256K |
| `kimi-k2.5` | — | vision + tools + thinking + multimodal | — |
| `deepseek-v4-flash` | 284B / 13B active MoE | tools + thinking | **1M** |
| `glm-5.1` | — | tools + thinking + coding | — |
| `glm-5` | 744B / 40B active | tools + thinking + reasoning | — |
| `glm-4.7` | — | tools + thinking + coding | 203K |
| `gemma4` | 26-31B variants | vision + tools + thinking + audio | — |
| `qwen3.5` | 0.8B-122B variants | vision + tools + thinking + multimodal | — |
| `qwen3-coder-next` | — | tools + coding | — |
| `qwen3-next` | 80B | tools + thinking | — |
| `ministral-3` | 3B-14B | vision + tools + edge | — |
| `devstral-small-2` | 24B | vision + tools + software engineering | — |
| `devstral-2` | 123B | tools + software engineering | — |
| `nemotron-3-super` | 120B / 12B active MoE | tools + thinking | — |
| `nemotron-3-nano` | 4B-30B | tools + thinking | — |
| `minimax-m2.7` | — | tools + thinking | — |
| `minimax-m2.5` | — | tools + thinking | — |
| `rnj-1` | 8B | tools + code/STEM | — |
| **`gemini-3-flash-preview`** | — | vision + tools + thinking | — |
| `cogito-2.1` | 671B | MIT licensed | — |

**Notable findings:**
- **Ollama Cloud DOES carry Gemini 3 Flash Preview** — contradicts my earlier framework claim that Ollama Cloud had no GPT/Gemini/Claude proprietary models. Correction to propagate.
- **DeepSeek V4-Flash with 1M context** is available — same model OpenRouter serves, now accessible flat-rate under Pro plan
- **GLM 5 and GLM 5.1** are newer than GLM 4.7 — need to evaluate if they supersede 4.7 for operator's coding work
- **qwen3-coder-next** — coding-specialized Qwen variant; worth testing for AICP routing
- **cogito-2.1 (671B, MIT)** — large MIT-licensed model; noteworthy for mission-aligned deployment if Moonshot ever changes K2.6 license

## Cross-references

- [[src-agentic-coding-harness-landscape-2026|Harness Landscape 2026]] — OpenCode's place in the 11-harness ecosystem
- [[src-claude-code-harness-features|Claude Code Harness Features]] — sister synthesis; most-comparable harness
- [[src-codex-cli-and-claude-code-plugin|Codex CLI + Plugin]] — different bet; works alongside OpenCode via Claude Code
- [[ai-model-provider-harness-decision-matrix-2026|Decision Matrix 2026]] — OpenCode's 75+ providers + Ollama Cloud catalog feed the matrix
- [[ai-infrastructure-decision-framework-2026|AI Infrastructure Framework 2026]] — OpenCode is the activated substitute for Claude Code per the resilience playbook

## State of Knowledge

| Claim | Verified? | Evidence |
|---|---|---|
| OpenCode has Build / Plan modes toggled via Tab | ✅ | opencode.ai/docs |
| `/connect /init /undo /redo /share` are real slash commands | ✅ | opencode.ai/docs |
| 75+ LLM providers supported | ✅ | Multiple sources incl. Together AI guide |
| LSP native with 20+ languages + 9 operations | ✅ | opencode.ai/docs/lsp |
| Multi-session with independent contexts | ✅ | opencode.ai/docs |
| `/share` creates public URLs | ✅ | opencode.ai/docs |
| AGENTS.md generation via `/init` | ✅ | opencode.ai/docs |
| Install paths: npm/brew/pacman/choco/scoop/docker | ✅ | opencode.ai/docs |
| MCP support | ✅ | opencode.ai/docs (advanced configuration page) |
| Plugin system with event hooks | ✅ | opencode.ai/docs/plugins |
| 95K+ GitHub stars | ✅ | Prior research (harness landscape synthesis) |
| Ollama Cloud carries 20+ models incl. Gemini 3 Flash Preview | ✅ | ollama.com/search?c=cloud |

## Next steps for operator

1. **In a new OpenCode session**: run `/init` in the wiki repo to see what AGENTS.md OpenCode auto-generates — compare to existing AGENTS.md/CLAUDE.md
2. **Test multi-session**: open wiki session + AICP session in the same OpenCode instance; verify context isolation
3. **Try Build vs Plan mode** on a non-trivial task (e.g., designing a new AICP routing rule) — see if the explicit mode-switch helps vs. Claude Code's blended approach
4. **Configure Ollama Cloud provider** via `/connect ollama` — directly test kimi-k2.6, deepseek-v4-flash, glm-5.1 on a real task
5. **Port one skill from `.claude/skills/` to OpenCode** — verify cross-harness skill portability in practice
6. **Run pricing on OpenCode with K2.6 via OpenRouter** — compare actual cost per task against Claude Code+OpenRouter for the same work

## Relationships

- BUILDS ON: [[src-agentic-coding-harness-landscape-2026|Harness Landscape 2026]]
- BUILDS ON: [[ai-infrastructure-decision-framework-2026|AI Infrastructure Decision Framework 2026]]
- COMPARES TO: [[src-claude-code-harness-features|Claude Code Harness Features]]
- RELATES TO: [[src-codex-cli-and-claude-code-plugin|Codex CLI + Codex Plugin for Claude Code]]
- RELATES TO: [[src-inference-provider-landscape-2026|Inference Provider Landscape 2026]]
- FEEDS INTO: [[ai-model-provider-harness-decision-matrix-2026|Model × Provider × Harness Decision Matrix]]
- FEEDS INTO: [[aicp|AICP]] — OpenCode is now a second activated harness in the operator's stack
- DEMONSTRATES: [[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4]] — the "OpenCode is our Claude-Code-immediate-substitute" claim from the resilience playbook is now ACTIVATED and verifiable

## Backlinks

[[Harness Landscape 2026]]
[[ai-infrastructure-decision-framework-2026|AI Infrastructure Decision Framework 2026]]
[[src-claude-code-harness-features|Claude Code Harness Features]]
[[Codex CLI + Codex Plugin for Claude Code]]
[[src-inference-provider-landscape-2026|Inference Provider Landscape 2026]]
[[Model × Provider × Harness Decision Matrix]]
[[aicp|AICP]]
[[Principle 4]]
