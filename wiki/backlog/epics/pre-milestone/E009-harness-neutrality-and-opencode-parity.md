---
title: "E009 — Harness Neutrality (OpenCode as Second Consumer)"
type: epic
domain: backlog
status: draft
priority: P1
task_type: epic
current_stage: document
readiness: 15
progress: 0
stages_completed: []
artifacts: []
confidence: high
created: 2026-04-22
updated: 2026-04-22
sources:
  - id: operator-directive
    type: file
    file: raw/notes/2026-04-22-directive-post-anthropic-self-autonomous-plan.md
tags: [epic, p1, harness, opencode, harness-neutral, consumer-property-doctrine, skills-portability, mcp, post-anthropic]
---

# E009 — Harness Neutrality (OpenCode as Second Consumer)

## Summary

Prove the project is **harness-neutral** by installing [OpenCode (sst/opencode)](https://github.com/sst/opencode) as a second consumer alongside Claude Code CLI, validate parity on the operator's top-N skills, confirm MCP servers (research-wiki, claude-mem, plannotator) work under both harnesses, and publish a **Harness Contract** document that captures the invariants any future harness must provide. This epic makes the "every `.agents/` / `.gemini/` / `.claude/` / `.opencode/` is equivalent" principle operational — the wiki, pipeline, MCP, and skills are the load-bearing artifacts; the harness is interchangeable.

## Operator Directive

> "We will personally stay on Claude Code for now but evolve our reasoning to be compatible with OpenCode or other real community service that won't lower quality or service with time."

> "Every .agents or .gemini or .claude can be treated as equivalent to us. Every ecosystem needs one and to us it's the same thing."

> "We don't need to lower ourselves to lower standards — even if we need to inject our sauce to elevate it we will."

## Goals

- OpenCode installed and configured against the same wiki working directory.
- OpenCode reaches parity with Claude Code on at least **3 of operator's top skills** (candidate set: `continue`, `ingest`, `log`, `evolve`).
- MCP servers (research-wiki, claude-mem, plannotator) callable from OpenCode.
- **Harness Contract** published at `wiki/spine/standards/harness-contract.md` — the invariants any harness must provide (tool names, hook model, skill invocation convention, memory persistence contract, MCP integration, cost tracking).
- Side-by-side session run documented — same wiki-typical task executed via Claude Code and via OpenCode, artifacts compared.

## Done When

- [ ] OpenCode binary installed; `opencode --version` returns a version number
- [ ] `~/.opencode/` directory contains baseline config pointing at the research wiki working dir
- [ ] OpenCode's API key configuration set to use OpenRouter (or direct provider) — same K2.6 route as Claude Code
- [ ] MCP config: `research-wiki` MCP server reachable from OpenCode; sample query succeeds
- [ ] MCP config: `claude-mem` MCP server reachable from OpenCode (or its equivalent memory tool configured)
- [ ] MCP config: `plannotator` MCP server reachable from OpenCode
- [ ] 3 portable-skill equivalents: translate `continue`, `ingest`, `log` from `.claude/skills/` to OpenCode's skill or agent format; invoke each and confirm equivalent behavior
- [ ] Side-by-side POC: the same wiki task (e.g., "scaffold a pattern page and validate with pipeline post") run via Claude Code and via OpenCode; both produce validating wiki pages
- [ ] `wiki/spine/standards/harness-contract.md` authored: tool names/semantics, hook event model + adapter expectations, skill invocation convention, memory/persistence contract, MCP integration, cost-tracking contract
- [ ] `wiki/log/2026-04-25-*-harness-neutrality-proof.md` documents the side-by-side session with evidence (files produced, pipeline results, any divergence)
- [ ] `python3 -m tools.pipeline post` returns 0 validation errors after all E009 work commits

## Scale and Model

> [!info] Epic Parameters
>
> | Parameter | Value |
> |-----------|-------|
> | **Model** | feature-development |
> | **Quality tier** | Pyramid (not on deadline critical path; strategic insurance) |
> | **Estimated modules** | 4 |
> | **Estimated tasks** | 12-15 |
> | **Dependencies** | E007 (proves OpenRouter route works — OpenCode uses same route) |

## Module Breakdown

| Module | Delivers | Est. Tasks |
|--------|----------|-----------|
| [[e009-m001-opencode-install-and-base-config]] | OpenCode installed, baseline config, OpenRouter K2.6 wired | 3 |
| [[e009-m002-mcp-server-continuity]] | All 3 MCP servers callable from OpenCode | 3 |
| [[e009-m003-skill-portability]] | 3 top skills ported/equivalenced in OpenCode's format | 3-4 |
| [[e009-m004-harness-contract-document]] | `wiki/spine/standards/harness-contract.md` published + side-by-side POC log | 2-3 |

## Dependencies

- [[E007-openrouter-deadline-de-risk]] M007.1 (OpenRouter access) — OpenCode uses same inference backend.
- Operator decision: stays on Claude Code primary for now (per directive). OpenCode proves the portability, doesn't replace primary.
- OpenCode's current feature set (as of 2026-04) — skills/agents concept, hook system, MCP support. Verified during M009.1.

## Open Questions

> [!question] Does OpenCode's skill/agent concept map cleanly to Claude Code's `.claude/skills/` markdown+frontmatter format?
> Research during M009.1. If format divergence is large, M009.3 may need an adapter/translator layer.

> [!question] Does OpenCode honor the same MCP server manifest (`.mcp.json`) as Claude Code?
> MCP is a standard — should work. Verified in M009.2.

> [!question] Which skills to port first? The full `.claude/skills/` set is large.
> Default: top 3 by recent usage (`continue`, `ingest`, `log`). Can grow from there.

> [!question] How do hooks translate? Claude Code's settings.json hooks are CC-specific schema.
> Harness Contract document (M009.4) formalizes a harness-neutral hook model; each harness implements an adapter.

## Relationships

- PART OF: [[post-anthropic-self-autonomous-stack|Milestone: Post-Anthropic Self-Autonomous AI Stack]]
- DEPENDS ON: [[E007-openrouter-deadline-de-risk|E007-openrouter-deadline-de-risk]]

## Backlinks

[[post-anthropic-self-autonomous-stack|Milestone: Post-Anthropic Self-Autonomous AI Stack]]
[[E007-openrouter-deadline-de-risk|E007-openrouter-deadline-de-risk]]
