# CLAUDE.md — Claude Code Specific Overrides

> **Read [AGENTS.md](AGENTS.md) first.** That file has the universal rules, stage gates, page schema, and methodology that apply to every AI tool working on this project. This file adds ONLY Claude Code-specific concerns: skills, MCP, Claude-native commands, and anything that differs from the cross-tool default.

## Identity Profile (Goldilocks)

| Dimension | Value |
|-----------|-------|
| **Type** | system (framework + instance + second brain) |
| **Execution Mode** | solo — human + Claude in conversation, no harness, no loop |
| **Domain** | knowledge (Python/wiki tools) |
| **Phase** | production (used daily, 316+ pages) |
| **Scale** | medium (316 pages, growing) |
| **PM Level** | L1 (wiki backlog, CLAUDE.md directives, pipeline tools) |
| **Trust Tier** | operator-supervised |
| **SDLC Chain** | Default (stage-gated with selected artifacts) |
| **Second Brain** | IS the second brain (self-referential) |

See [CONTEXT.md](CONTEXT.md) for the full identity profile with current milestone status.

## Claude-Specific Behaviors

**Superpowers skills are active** — use them proactively. If a skill matches the task, invoke it. Skill priority: process first (brainstorming, debugging) → implementation second.

**MCP server exposes 21 tools.** Registered in `.mcp.json`. Start with `wiki_status` to orient, then `wiki_search`, `wiki_read_page`, `wiki_list_pages` for navigation. Gateway tools (`wiki_gateway_query`, `wiki_gateway_template`, `wiki_gateway_contribute`, `wiki_gateway_flow`) for unified operations.

**TodoWrite tool for multi-step work.** Track progress on anything ≥3 steps.

**Claude-native plan mode (`ExitPlanMode`)** is preferred over ad-hoc scaffolding when work has a clear plan. Matches our Document→Design stage gate philosophy.

**Sub-agents inherit AGENTS.md context** but NOT CLAUDE.md. When dispatching, include relevant rules in the spawn prompt. See the Agent Failure Taxonomy: sub-agent non-compliance is Class 5 (~33% base compliance).

## Skills Directory

Skills live in `.claude/skills/`. Primary project skills:
- `wiki-agent` — ingest sources, query knowledge, maintain quality, export
- `evolve` — score, scaffold, generate, review maturity, detect staleness
- `continue` — resume mission: diagnostics → state → options
- `model-builder` — build, review, or evolve a wiki model
- `log` — add log entry to `wiki/log/`
- `ingest` — ingest sources into the research wiki
- `status`, `backlog`, `gaps`, `review` — operational queries

See [SKILLS.md](SKILLS.md) for the full directory and conventions.

## Essential Commands (Claude Code Native)

| Action | Command |
|--------|---------|
| Full post-ingestion chain | `python3 -m tools.pipeline post` |
| Fetch URL(s) | `python3 -m tools.pipeline fetch URL [URL...]` |
| Fetch topic (web search) | `python3 -m tools.pipeline fetch --topic "query"` |
| Scan a local project | `python3 -m tools.pipeline scan ../project/` |
| Score evolution candidates | `python3 -m tools.pipeline evolve --score` |
| Scaffold a new page | `python3 -m tools.pipeline scaffold <type> "<title>"` |
| Show identity + recommendations | `python3 -m tools.gateway what-do-i-need` |
| Goldilocks flow walkthrough | `python3 -m tools.gateway flow [--step N]` |
| Query the wiki | `python3 -m tools.gateway query --<dimension>` |
| Dashboard view | `python3 -m tools.view` |

Full reference: [TOOLS.md](TOOLS.md).

## Ingestion Modes (Claude-Specific Defaults)

Three modes. Default is `smart`:
- **auto** — process without stopping, report after
- **guided** — show extraction plan, wait for approval, review each page
- **smart** (default) — auto when confident; escalate when: new domain, contradictions, ambiguity, expert-level complexity, low-quality source

## Claude-Specific Hard Rules (Extend AGENTS.md)

In addition to AGENTS.md hard rules:

8. **When denied a tool call, DO NOT retry the exact same call.** Think about why. Ask if unclear (AskUserQuestion). Adjust approach.
9. **For multi-step work, use TodoWrite.** Track in real-time. Mark completed immediately, not batched.
10. **For brainstorming/creative work, use the `brainstorming` skill FIRST.** Then implementation skills. Process > implementation.
11. **Never delegate understanding to sub-agents.** Prompts that say "based on your findings, fix the bug" push synthesis onto the agent. Write prompts that prove you understood: include file paths, line numbers, specific changes.
12. **Sub-agent prompts must be self-contained.** They don't see this conversation. Include context, paths, expected output format.

## Flow Per Mode

| Mode | How Claude Loads Context |
|------|------------------------|
| **Solo session** (primary, current) | Auto-loads this CLAUDE.md + AGENTS.md. Operator interactive. Skills invoked on-demand. |
| **Harness mode** (not yet) | Harness injects stage-specific skill. CLAUDE.md de-emphasized. Stage skill is primary context. |
| **Sub-agent dispatch** | Sub-agent gets ONLY the spawn prompt + AGENTS.md inheritance (uncertain). Include critical rules in prompt. |
| **MCP client from other project** | Reads AGENTS.md, not CLAUDE.md. Uses gateway MCP tools. |

## Adoption Direction

This wiki sits at **Level 4-5** of the [7 Levels of Claude Code + RAG](wiki/sources/src-7-levels-claude-code-rag.md) progression:
- Level 4 (Obsidian vault) — complete
- Level 5 (Naive RAG) — partial via pipeline + gateway
- Level 6 (Graph RAG / LightRAG) — target; we have the graph, need LightRAG integration
- Level 7 (Agentic multimodal RAG) — future

**Current CLAUDE.md size**: ~95 lines (target: <100 lines per ETH Zurich research — context files ≥300 lines reduce task success by ~3%).

## Where to Go Next

- **New to this project?** → [README.md](README.md)
- **Any AI tool?** → [AGENTS.md](AGENTS.md) (universal)
- **Tools / CLI?** → [TOOLS.md](TOOLS.md)
- **Architecture / data flow?** → [ARCHITECTURE.md](ARCHITECTURE.md)
- **Page design / styling?** → [DESIGN.md](DESIGN.md)
- **Skills / commands?** → [SKILLS.md](SKILLS.md)
- **Identity / scope?** → [CONTEXT.md](CONTEXT.md)
