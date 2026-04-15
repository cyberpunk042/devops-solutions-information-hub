---
title: "Synthesis — Cline — Agentic Coding IDE Extension with Plan/Act, Skills, Hooks, MCP"
aliases:
  - "Synthesis — Cline — Agentic Coding IDE Extension with Plan/Act, Skills, Hooks, MCP"
type: source-synthesis
domain: ai-agents
layer: 1
status: synthesized
confidence: high
maturity: growing
created: 2026-04-15
updated: 2026-04-15
sources:
  - id: cline-github
    type: documentation
    url: https://github.com/cline/cline
    file: raw/articles/clinecline.md
    title: "cline/cline — VS Code extension for agentic coding"
    ingested: 2026-04-15
tags: [cline, claude-code, vs-code-extension, agentic-coding, mcp, skills, hooks, plan-mode, checkpoints, agents-md, multi-provider, ecosystem-comparison]
---

# Synthesis — Cline — Agentic Coding IDE Extension with Plan/Act, Skills, Hooks, MCP

## Summary

Cline is a VS Code extension (formerly "Claude Dev") providing agentic coding capabilities inside the editor. It is the closest peer to Claude Code — same architectural primitives (skills, hooks, MCP, plan mode, checkpoints, agentic tool loop) but a different UX surface (IDE panel with diff-approval GUI vs terminal CLI). Cline supports 10+ model providers (OpenRouter, Anthropic, OpenAI, Gemini, Bedrock, Azure, Vertex, Cerebras, Groq) plus local via LM Studio/Ollama. As of v3.55 it added AGENTS.md support, first-class skills, hooks, multi-root workspaces, and parallel tool calling. Cline's CLAUDE.md is literally `@.clinerules/general.md` + 2 imports — a distinct composition pattern from this wiki's three-layer AGENTS.md + CLAUDE.md pattern. Cline validates the three-layer agent context architecture as an ecosystem-wide convergence and adds a new "imports/include" composition pattern to the [[context-file-taxonomy|Context File Taxonomy]].

## Source Reference

> [!info] Source card
>
> | Source | Type | Content |
> |--------|------|---------|
> | [cline/cline GitHub repo](https://github.com/cline/cline) | Monorepo | README, changelog (80+ versions), SKILL.md exemplars, CLAUDE.md, hooks docs, MCP integration |
> | Fetch depth | Deep (via enhanced pipeline ingest) | 22,000+ lines of raw content including README + SKILL examples + full CHANGELOG |

## Key Insights

### 1. Architectural Twin of Claude Code

Cline and Claude Code have converged on the same primitive set despite being developed independently:

| Primitive | Claude Code | Cline |
|-----------|-------------|-------|
| **Skills** | `.claude/skills/*.md` with SKILL.md format | `.agents/skills/create-pull-request/SKILL.md` (same pattern — folder per skill with SKILL.md anchor) |
| **MCP** | Native client; registers external tools | Native client; can create new MCP servers on demand ("add a tool that…") |
| **Hooks** | User-defined shell scripts | User-defined shell scripts running from workspace repo root (v3.55) |
| **Plan mode** | `ExitPlanMode` tool | Plan/Act modes (strict plan mode disabled by default since v3.55) |
| **Checkpoints** | Git-backed branch state | Workspace snapshots per step with Compare/Restore diff UI |
| **Context management** | Progressive disclosure, explicit CLAUDE.md | AST analysis, regex search, relevant-file reading for "large projects without overwhelming the context window" |
| **Human-in-the-loop** | Permission mode for tool calls | Per-change diff approval GUI (file edits) + per-command terminal approval |

This convergence is not coincidence. It's evidence that agentic coding as a domain has **solved architecture** — the problem space naturally produces these abstractions. Any new entrant will rediscover them.

### 2. AGENTS.md Support Is Ecosystem-Wide

Cline added AGENTS.md support (per changelog). This is direct evidence that [[three-layer-agent-context-architecture|Three-Layer Agent Context Architecture]] — currently in `01_drafts/` — is a cross-ecosystem convergence, not a Claude-Code-specific pattern. Combined with Claude Code's native AGENTS.md support, Codex's adoption, Copilot CLI, Gemini CLI, Cursor, and OpenCode, AGENTS.md is emerging as the *de facto* universal agent context standard. The three-layer pattern (AGENTS.md universal + tool-specific-delta + Skills conditional) is stronger for promotion.

### 3. Cline's CLAUDE.md Is Pure Imports — New Composition Pattern

Cline's own `CLAUDE.md` file is three lines:

```markdown
@.clinerules/general.md
@.clinerules/network.md
@.clinerules/cli.md
```

This is a completely different composition pattern from this wiki's approach. Ours: CLAUDE.md is a slim overrides file (107 lines) that references AGENTS.md and companion `.md` files. Cline's: CLAUDE.md is a pure aggregator that `@`-imports sibling files. This adds a new expansion variant to Dimension 8 of the [[context-file-taxonomy|Context File Taxonomy]]: **"folder with imports/includes"** (distinct from the taxonomy's existing "flat file", "file + companion folder", "folder-indexed", "runtime-generated tree"). Worth adding as a fifth expansion pattern.

### 4. Strict Plan Mode Disabled by Default — Mindful Enforcement at Scale

Cline v3.55 note: *"disabled strict plan mode by default."* Plan mode (their `ExitPlanMode` equivalent) became opt-in after being mandatory. Why? Almost certainly because strict plan mode created friction for simple tasks — the same observation captured in [[enforcement-must-be-mindful-hard-blocks-need-justified-bypass|Enforcement Must Be Mindful]]. Cline is a large-scale real-world validation (millions of users) of the mindful-enforcement principle: rigid gates that don't match the user's context get disabled; flexibility with explicit opt-in survives.

### 5. Multi-Provider Strategy Validates Local-AI Target

Cline supports: OpenRouter, Anthropic, OpenAI, Google Gemini, AWS Bedrock, Azure, GCP Vertex, Cerebras, Groq — plus local via LM Studio/Ollama. Users can combine providers across tasks. This is the [[model-local-ai|Model — Local AI]] strategy in practice: not a single model, not a single provider, but a routed portfolio where simple tasks go to local or cheap models and complex reasoning goes to Opus/Sonnet/similar. Cline's approach informs AICP's Stage 3 design — the routing decision logic and provider abstraction layer are already solved problems in production.

### 6. Skills Are First-Class via `.agents/skills/` Directory

The cline repo contains `.agents/skills/create-pull-request/SKILL.md` — a concrete skill instance with the same folder-per-skill structure this wiki uses in `.claude/skills/`. Changelog note: "Move PR skill to .agents/skills". The migration from `.claude/` → `.agents/` signals Cline is aligning with the cross-tool `.agents/` convention that AGENTS.md implies. This is the same dimension-8 "file + companion folder" pattern the Context File Taxonomy documents.

### 7. Autonomous + Human-in-Loop Hybrid

Cline runs autonomously by default but gates every file change and terminal command behind human approval (via the diff UI or approve/deny buttons). This is a concrete instance of the three-lines-of-defense pattern from [[three-lines-of-defense-immune-system-for-agent-quality|Three Lines of Defense]]: the agent is Line 1 (prevention via good prompting), the diff UI is Line 2 (detection via human review), and the restore/rollback via checkpoints is Line 3 (correction). Cline's UX materializes the pattern in a consumer product.

### 8. Checkpoints: Agent-Aware Version Control

Every step the agent takes produces a workspace snapshot. The user can diff the snapshot vs current state and restore to any prior step. This is more granular than git (which captures only commits, not intermediate states) and makes the agent's trial-and-error visible. For comparison, Claude Code relies on git for this and doesn't have step-level snapshots.

This is a gap this wiki's ecosystem might want to close — OpenFleet's agents operate autonomously and the lack of step-level snapshots makes debugging their decisions harder. Cline's checkpoint design is a reference implementation worth studying.

### 9. CLI Mode Exists

Recent changelog: CLI mode with `/q`, `--thinking` token budget, `--max-consecutive-mistakes` for "yolo runs". Cline is not just a VS Code extension — it's evolving a terminal CLI too, blurring the line with Claude Code's native terminal interface. The UX convergence completes: both tools span editor + terminal, both expose agentic primitives, both speak AGENTS.md.

### 10. MCP Server Creation on Demand

Cline explicitly supports "add a tool that fetches Jira tickets" — where Cline itself creates and installs a new MCP server for the task. This is meta: the agent extends its own capabilities by writing the MCP code, testing it, and registering it. Claude Code does not have this at the same level of friction-free UX (though the primitives exist). This is a differentiator worth tracking.

## Cross-Reference Integration

### Convergent Evidence (strengthens existing pages)

| Existing Page | How Cline Reinforces It |
|---------------|--------------------------|
| [[three-layer-agent-context-architecture\|Three-Layer Agent Context Architecture]] (in `01_drafts/`) | Cline's AGENTS.md support + `.agents/skills/` pattern + CLAUDE.md as aggregator = direct cross-ecosystem evidence. Strengthens promotion case from `01_drafts` to `02_synthesized`. |
| [[context-file-taxonomy\|Context File Taxonomy]] | Adds a fifth expansion pattern — "folder with imports/includes" (`@file.md` syntax). Currently documents: flat file, file+folder, folder-indexed, runtime-generated tree. Cline extends. |
| [[enforcement-must-be-mindful-hard-blocks-need-justified-bypass\|Enforcement Must Be Mindful]] | Cline disabled strict plan mode by default in v3.55 — large-scale validation that rigid gates get routed around. |
| [[model-claude-code\|Model — Claude Code]] | Direct comparative peer. Cline = same primitives, different UX surface. Model page should note this for architecture discussions. |
| [[model-skills-commands-hooks\|Model — Skills, Commands, and Hooks]] | Cline implements identical skill/hook/MCP patterns independently. The pattern set is ecosystem-wide. |
| [[model-local-ai\|Model — Local AI ($0 Target)]] | Cline's multi-provider portfolio (10+ cloud + local) is the routing strategy in production. Reference implementation for AICP Stage 3. |
| [[model-mcp-cli-integration\|Model — MCP and CLI Integration]] | Cline's "add a tool" MCP-creation-on-demand is a differentiating pattern worth documenting. |
| [[four-project-ecosystem\|Four-Project Ecosystem]] | OpenFleet agent debugging could benefit from Cline-style step snapshots. Gap worth noting. |

### Tensions / Divergences

| Cline Design Choice | Our Current Approach | Reconciliation |
|---------------------|---------------------|----------------|
| CLAUDE.md = pure imports (`@file.md`) | CLAUDE.md = slim overrides, references AGENTS.md | Both are valid Dimension-8 expansion patterns — different trade-offs (Cline: composition; ours: delta). Document both in taxonomy. |
| Strict plan mode opt-in | We haven't made ours opt-in yet | Consider: does our stage-gate enforcement need a similar "opt-out for simple tasks" escape valve? Aligns with Mindful Enforcement principle. |
| Workspace snapshots per step | Git commits only | Feature gap. Worth evaluating for OpenFleet. |

## Deep Analysis

### The Ecosystem Has Converged on Architecture

Claude Code, Cline, Codex, Copilot CLI, Gemini CLI, Cursor, OpenCode — all independently rediscovering skills + hooks + MCP + plan mode + checkpoints. When independent implementations converge on the same abstractions, the abstractions are load-bearing. Architectures that diverge (e.g., agents-as-services, agents-as-prompts, agents-as-RAG-endpoints) have not proven out; agents-as-editor/terminal-companions with typed tool access has.

Implication for this wiki: the patterns already documented (skills-commands-hooks, three-layer context, enforcement hierarchy, checkpoints via git) are not idiosyncratic — they reflect ecosystem-level consensus. This raises confidence in the existing models from "growing" toward "mature/authoritative."

### Why Cline's Imports Pattern Matters

The `@.clinerules/general.md` include syntax treats CLAUDE.md as a *manifest*, not as content. The real context lives in `.clinerules/` — one file per concern (general / network / CLI). This has trade-offs vs our slim-overrides approach:

| Approach | Pros | Cons |
|----------|------|------|
| **Cline imports (manifest + folder)** | Each concern in its own file; easy to swap/disable; version-control-friendly per concern | Requires tooling to resolve imports; CLAUDE.md alone is meaningless |
| **Our slim overrides (AGENTS.md + delta)** | CLAUDE.md is self-contained and readable without tooling; delta is explicit | CLAUDE.md can drift from AGENTS.md if edits skip the cross-reference |

Neither dominates. Both are valid. The taxonomy should document both as legitimate Dimension-8 patterns. This is direct input for updating [[context-file-taxonomy|Context File Taxonomy]] — a fifth expansion variant.

### What the Millions of Users Tell Us

Cline has crossed enough users to be a de-facto standard. Its design choices — especially the ones that REVERSED (strict plan mode → opt-in) — are empirical validations against fixed design assumptions. When a feature gets opt-out defaults, it's because real-world friction exceeded the benefit for the default user. This is the [[right-process-for-right-context-the-goldilocks-imperative|Goldilocks Principle]] at ecosystem scale: too-much-process gets routed around, too-little creates gaps, the right amount shifts with context.

### Gap — No Formal Comparison Vs Claude Code

A dedicated comparison page ([[model-claude-code|Model — Claude Code]] vs Cline vs Copilot CLI vs Cursor) would be high-value. The primitives are converged but the UX choices differ materially. Would affect "which agent tool should I recommend" decisions for sister projects. Noted as a gap, not built here.

## Relationships

- RELATES TO: [[model-claude-code|Model — Claude Code]]
- RELATES TO: [[model-skills-commands-hooks|Model — Skills, Commands, and Hooks]]
- RELATES TO: [[model-mcp-cli-integration|Model — MCP and CLI Integration]]
- RELATES TO: [[context-file-taxonomy|Context File Taxonomy]]
- FEEDS INTO: [[three-layer-agent-context-architecture|Three-Layer Agent Context Architecture]]
- RELATES TO: [[enforcement-must-be-mindful-hard-blocks-need-justified-bypass|Enforcement Must Be Mindful — Hard Blocks Need Justified Bypass]]
- RELATES TO: [[model-local-ai|Model — Local AI ($0 Target)]]
- COMPARES TO: [[model-claude-code|Model — Claude Code]]

## Backlinks

[[model-claude-code|Model — Claude Code]]
[[model-skills-commands-hooks|Model — Skills, Commands, and Hooks]]
[[model-mcp-cli-integration|Model — MCP and CLI Integration]]
[[context-file-taxonomy|Context File Taxonomy]]
[[three-layer-agent-context-architecture|Three-Layer Agent Context Architecture]]
[[enforcement-must-be-mindful-hard-blocks-need-justified-bypass|Enforcement Must Be Mindful — Hard Blocks Need Justified Bypass]]
[[model-local-ai|Model — Local AI ($0 Target)]]
