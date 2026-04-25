# .claude/rules/self-reference.md — This Project IS the Second Brain

> Loaded on demand when the agent needs to understand the project's self-referential nature. CLAUDE.md has the summary; this file has the full framing.

## What This Project IS

This wiki at `~/devops-solutions-information-hub` is the **central intelligence hub** for a 5-project ecosystem. It is not a documentation project. It is the **second brain** that the other 4 projects (OpenArms, OpenFleet, AICP, devops-control-plane) consume from and contribute back to.

When operating in this repo, the AI is **inside** the second brain — not consulting it from outside. This is the most important framing the operator needs the AI to hold.

## Brain vs Second Brain (don't conflate)

> Distinction borrowed from `~/openfleet/.claude/rules/second-brain-connection.md`:
>
> **The brain** = what CONSTITUTES the agent. CLAUDE.md + AGENTS.md + the rules files + the loaded models/principles/methodology + skills (when built) + commands + hooks. Per-project. Every project in the ecosystem has its own brain.
>
> **The second brain** = THIS wiki. The shared knowledge system holding methodology, standards, lessons, patterns, decisions, 16 models, 25 standards across 477+ pages. Projects consume from it; projects contribute to it. It validates itself with its own methodology.

In this project, **the brain and the second brain coincide**. The AI's brain (CLAUDE.md + AGENTS.md + .claude/rules/ + .claude/commands/ + the loaded super-model + 4 principles + methodology) IS what defines this project's agent. AND this same project IS the second brain that the ecosystem consumes from.

That's why P4 (Declarations Aspirational Until Verified) is so load-bearing here: when the wiki teaches P4 to other projects, its OWN config must demonstrate P4 — every declaration in CLAUDE.md / AGENTS.md / the rules files needs a verification gate, or the wiki is not preaching by example.

## Markdown-as-IaC (the brain's mechanism)

The brain is implemented as **layered Markdown configuration**. That's the model: Markdown-as-Infrastructure-as-Code. Reference: [model-markdown-as-iac](wiki/spine/models/agent-config/model-markdown-as-iac.md).

The Markdown layer is:
- **Always loaded** at session start (CLAUDE.md, AGENTS.md auto-load via Claude Code)
- **On-demand loaded** when work touches a topic (.claude/rules/{topic}.md per Claude Code convention; sister projects use this pattern)
- **Operator-invoked** via slash commands (.claude/commands/)
- **Auto-triggered** via skills (when built; description-match drives loading) — currently unbuilt in this project
- **Ambient** via the MCP server's available tools and the operator-loaded principles/super-model/methodology

This is the entire enforcement mechanism. There is no Python "agent runtime" forcing rules. The agent reads the Markdown and behaves from it. **The brain works only if the Markdown is structured as a program** (P2 — Structured Context Governs Agent Behavior).

## The Failure Mode This Layer Has (and how to mitigate)

Markdown-only enforcement achieves ~25% compliance for tool-call rules under context pressure (P1 quantified). That's why hooks exist — to bring tool-call rules to ~100% compliance. The hook layer in this project (`.claude/hooks/`) is being built precisely for the rules that **must** hold (corpus URL routing, output truncation, post-compaction state restoration). See [.claude/rules/hook-architecture.md](.claude/rules/hook-architecture.md).

## Behave FROM the Project, Not OVER It

> Operator directive 2026-04-24 (verbatim):
> "A PROJECT IS THE EXTENSION OF A BRAIN AND YOU NEED TO BEHAVE FROM IT NOT OVER IT... THE PROJECT IS INTELLIGENT... THE INTELLIGENCE COMES FROM USING THE PROJECT... THIS IS THE BASE OF WHAT THIS FUCKING PROJECT IS SUPPOSED TO TEACH AND ENFORCE"

What this means operationally:

| ❌ Behaving OVER the project | ✅ Behaving FROM the project |
|---|---|
| Read principles, then improvise | Read principles, then act per their application table |
| Cite the methodology in prose | Use methodology.yaml as the program — pick model by task_type, follow stages, hit gates |
| Generate a synthesis from base-model knowledge | Use `wiki_search` / `wiki_read_page` to ground claims in actual wiki content |
| Improvise URL fetch with WebFetch | Use `wiki_fetch` MCP / `pipeline fetch` per the routing table |
| Generate a status claim | Run the gate command, inline its output, then claim |
| Invent a bug to fix | `gateway query`, `pipeline status`, `lint`, `validate` to investigate before asserting |

The project's tools (gateway, pipeline, MCP, view, stats, validate, lint) ARE the agent's operating system. Use them as the first reach, not as citations.

## The 5-Project Ecosystem (where this fits)

| Project | Role | Relationship to this wiki |
|---|---|---|
| **Research Wiki** (this) | Central intelligence hub | IS the second brain |
| **OpenArms** | Harness engineering; advanced agent runtime | Feeds operational lessons back; uses wiki methodology |
| **OpenFleet** | Agent fleet orchestrator | Consumes wiki as LightRAG knowledge source |
| **AICP** | Local-AI complexity-routed inference ($0 target) | Implements patterns documented in wiki |
| **devops-control-plane** | Infrastructure governance | Uses wiki methodology for decision tracking |

When the agent asks "what should I do here," the answer is in the wiki the agent is INSIDE. Not external research. Not base-model improvisation. The wiki itself.

## Self-Reference Manifest (what loads automatically vs on-demand)

### Always loaded (every Claude Code session)
- [CLAUDE.md](CLAUDE.md)
- [AGENTS.md](AGENTS.md)
- [CONTEXT.md](CONTEXT.md) — referenced from CLAUDE.md but auto-loaded by convention

### Loaded on-demand when topic comes up
- [.claude/rules/routing.md](.claude/rules/routing.md) — when operator intent ambiguous
- [.claude/rules/methodology.md](.claude/rules/methodology.md) — when stage or model selection needed
- [.claude/rules/ingestion.md](.claude/rules/ingestion.md) — when URL ingestion happens
- [.claude/rules/learnings.md](.claude/rules/learnings.md) — when re-encountering a known failure mode
- [.claude/rules/work-mode.md](.claude/rules/work-mode.md) — for solo session pattern
- [.claude/rules/self-reference.md](.claude/rules/self-reference.md) — this file
- [.claude/rules/hook-architecture.md](.claude/rules/hook-architecture.md) — when designing/debugging hooks

### Loaded by gateway orient (recommended at session start)
- [wiki/spine/super-model/super-model.md](wiki/spine/super-model/super-model.md) — what this system IS
- [wiki/spine/references/model-registry.md](wiki/spine/references/model-registry.md) — the 16 named models
- [wiki/lessons/04_principles/hypothesis/](wiki/lessons/04_principles/hypothesis/) — the 4 principles in full
- [wiki/spine/models/foundation/model-methodology.md](wiki/spine/models/foundation/model-methodology.md) — methodology in depth

### Loaded on-demand via MCP / CLI
- Specific page reads via `wiki_read_page` MCP
- Search results via `wiki_search` MCP
- Backlog state via `wiki_backlog` MCP

## Cross-references

- Operator-directive corpus (all 2026-04-24 verbatim): `raw/notes/2026-04-24-operator-directives-session-verbatim.md`
- Markdown-as-IaC model: [wiki/spine/models/agent-config/model-markdown-as-iac.md](wiki/spine/models/agent-config/model-markdown-as-iac.md)
- Skills/commands/hooks model: [wiki/spine/models/agent-config/model-skills-commands-hooks.md](wiki/spine/models/agent-config/model-skills-commands-hooks.md)
- 4 Principles: [wiki/lessons/04_principles/hypothesis/](wiki/lessons/04_principles/hypothesis/)
- Sister project's parallel rules: `~/openfleet/.claude/rules/second-brain-connection.md`, `~/openarms/.claude/rules/`
