---
title: Model — MCP and CLI Integration
aliases:
  - "Model — MCP and CLI Integration"
  - "Model: MCP and CLI Integration"
type: concept
domain: cross-domain
layer: spine
status: synthesized
confidence: high
maturity: growing
created: 2026-04-09
updated: 2026-04-13
sources:
  - id: src-playwright-cli-vs-mcp
    type: youtube-transcript
    url: https://www.youtube.com/watch?v=nN5R9DFYsXY
    title: "Claude Code + Playwright CLI: Automate QA with Less Tokens"
tags: [mcp, cli, integration, model, token-efficiency, tool-integration, playwright, sandbox, spine, context-management]
---

# Model — MCP and CLI Integration
## Summary

The MCP and CLI Integration model resolves one of the most consequential architectural decisions in LLM agent design: how to expose external tools to an agent without degrading its context window. MCP servers load all tool schemas at session startup (eager). CLI tools paired with skills load on demand (deferred). A third approach — the context-mode sandbox — isolates heavy operations in a subagent with a clean context window. ==Empirically, CLI produces a 12x token cost differential for operational tooling. The decision is resolved: CLI+Skills default, MCP for external bridges, sandbox for heavy operations.==

## Key Insights

- **MCP's always-available property has a per-turn cost.** Every MCP server adds schema overhead to every message — not just when tools are invoked. Five MCP servers compound that overhead on every turn.

- **CLI+Skills defers all schema loading.** SKILL.md files sit on disk between invocations. Zero overhead until needed. Strictly superior to MCP for tools used in specific workflows.

- **The 12x differential is measured, not estimated.** Playwright MCP: 10 full accessibility tree dumps. Playwright CLI: 2-3 targeted YAML reads. Same task, same result, 12x cost difference. Microsoft now recommends CLI over MCP for AI agent use.

- **The context-mode sandbox handles the extreme case.** Operations requiring full codebase analysis run in an isolated subagent. Parent session receives a compact result. 98% fewer tokens in the parent session.

- **MCP genuinely wins for external service bridges.** Cross-conversation discoverability, OAuth state persistence, interactive workflows with rapid iteration — these justify MCP's overhead.

## Deep Analysis

### The Three Integration Strategies

> [!info] **Three strategies with different cost profiles**
> | Strategy | When it loads | Context cost | Best for |
> |----------|-------------|-------------|----------|
> | **MCP (eager)** | Session startup — all schemas always present | Permanent, every message | External services, cross-conversation discovery |
> | **CLI+Skills (deferred)** | On invocation only | Zero until needed | Operational tooling, project-internal workflows |
> | **Sandbox (isolated)** | Fresh subagent, clean context | Zero in parent session | Heavy operations (>30% of remaining context) |

**MCP — Eager Load:** Registers tool schemas at session startup. The model can invoke any registered tool at any point without setup. Cost: schema tokens for ALL tools persist for the entire session, regardless of use.

**CLI+Skills — Deferred Load:** Instruction files on disk. Load when invoked via `/command` or agent decision. Between invocations: zero overhead. For tools used occasionally, this preserves thousands of tokens MCP would have consumed.

**Context-Mode Sandbox:** Spawns a fresh Claude Code subprocess with a clean context window. The subagent runs the heavy operation in isolation and writes results to disk. The parent session reads the compact output. A fresh session starts with ~190K usable tokens; a main session at turn 50 may have 40-60% consumed. The sandbox runs cleanly where the main session would degrade.

---

### The Playwright Case Study

The clearest empirical validation of the CLI-over-MCP decision.

> [!example]- **10-step QA test: MCP vs CLI head-to-head**
> **Same task:** Automated QA testing of a web application, 10 navigation steps.
>
> **MCP approach:** After every navigation, Playwright MCP dumps the FULL accessibility tree into context. 10 steps = 10 full dumps. The model has full page data at all times.
>
> **CLI approach:** Playwright CLI writes the accessibility tree to a YAML file on disk. Claude reads the file ONLY when it needs to locate a specific element — typically 2-3 reads per 10-step test.
>
> **Result:** 12x fewer tokens with CLI. Accuracy equivalent or better — the model wasn't operating in a degraded context state.
>
> **Counter-case:** In interactive visual development (designer iterating on component appearance), MCP's always-available property makes tight feedback loops faster. The 12x differential is the default for QA automation; MCP is correct for interactive visual iteration. See [[src-playwright-mcp-visual-testing|Synthesis — Playwright MCP for Visual Development Testing]].

---

### The Decision Framework

> [!info] **4-step sequence for choosing MCP vs CLI for a new tool**

**Step 1 — Usage pattern:**

> [!tip] **MCP candidate signals**
> - Tool used in every session regardless of task
> - Requires authentication state preserved across sessions
> - Needs autonomous agent discovery (no explicit user invocation)

> [!tip] **CLI+Skills candidate signals**
> - Tool used in specific workflows only
> - Invoked 0-3 times per session on average
> - User or explicit agent step triggers it at the right time

**Step 2 — Schema cost assessment:**
- How many tools does this server expose? Each adds tokens per turn.
- How many OTHER MCP servers are already registered? Each multiplies overhead.
- Is this a long analytical session (sensitive to overhead) or a short task session?

**Step 3 — Discoverability need:**
- Does the agent need to invoke this tool WITHOUT explicit user instruction? → MCP
- Can a user invoke the skill at the right time? → CLI+Skills

**Step 4 — Sandwich case:**
- Is the operation estimated to consume >30% of remaining context? → Sandbox

> [!abstract] **Defaults in the absence of specific requirements**
> CLI+Skills for project-internal tools. MCP for external services needing cross-session availability. Context-mode sandbox for operations >30% of remaining context.

---

### The [[context-aware-tool-loading|Context-Aware Tool Loading]] Pattern

The MCP vs CLI decision generalizes to any information entering an agent's context:

> [!info] **Three loader types**
> | Type | Mechanism | Cost | Example |
> |------|-----------|------|---------|
> | **Eager** | Always loaded, always available | Permanent overhead | MCP servers, CLAUDE.md |
> | **Deferred** | On-disk until invoked | Zero until needed | Skills, CLI tools |
> | **External** | Outside context entirely, queried on demand | Per-query only | NotebookLM, Context7, LightRAG |

This applies uniformly to: browser automation (MCP vs CLI), documentation (pre-loaded vs Context7), knowledge bases (inline vs LightRAG graph), and skill libraries (always-loaded vs SKILL.md).

---

### MCP Server Design Principles

When MCP IS the right choice, server design minimizes the schema overhead:

> [!tip] **Design principles for MCP servers**
> - **Minimize tool count** — each tool adds schema tokens on every turn. Expose only tools that legitimately need always-discoverable. Tools for specific workflows → CLI skills.
> - **Narrow tool signatures** — fewer optional parameters = smaller schema. Composition (two sequential calls) beats one tool with eight parameters.
> - **Semantic tool naming** — `wiki_search`, `wiki_post`, `wiki_status` — self-describing for autonomous invocation. Opaque names (`do_operation_7`) defeat discoverability.
> - **Document preconditions in tool descriptions** — autonomous agents have only the schema to guide them. Put preconditions, side effects, expected output format in the description.

> [!example]- **Real instance: this wiki's 26-tool MCP server (updated 2026-04-15)**
> Tool names follow `wiki_<verb>` format (semantically clear). Each tool has a single primary function. Descriptions include what the tool returns. The server follows all four design principles. **The tool count has grown from 17 to 26 as of 2026-04-15 — now past the "~17-20 upper limit" this model originally stated.** Full enumeration: wiki_backlog, wiki_continue, wiki_crossref, wiki_evolve, wiki_fetch, wiki_fetch_topic, wiki_gaps, wiki_gateway_compliance, wiki_gateway_contribute, wiki_gateway_docs, wiki_gateway_flow, wiki_gateway_health, wiki_gateway_query, wiki_gateway_template, wiki_integrations, wiki_list_pages, wiki_log, wiki_methodology_guide, wiki_mirror_to_notebooklm, wiki_post, wiki_read_page, wiki_scan_project, wiki_search, wiki_sister_project, wiki_status, wiki_sync. Selective tool exposure (loading only context-relevant tools per conversation) is now the recommended next step — currently tools are all eagerly loaded per MCP defaults.

---

### Ecosystem Integration Bindings

> [!info] **Resolved pattern for this ecosystem**
> | Strategy | What uses it | Why |
> |----------|-------------|-----|
> | **CLI+Skills** | Wiki pipeline, Playwright QA, NotebookLM queries, Context7, all project-internal tooling | Deferred loading, zero idle overhead |
> | **MCP** | Wiki MCP server (17 tools), AICP inference bridge, external services | Cross-conversation discoverability, service bridging |
> | **Sandbox** | Full codebase analysis, large document processing, parallel ingestion | >30% context cost isolation |

---

### Context Fill and Degradation

> [!warning] **Degradation thresholds — one practitioner's observations, not hard limits**
> One former Amazon/Microsoft engineer reported: increased error rates at ~40% fill, unreliable outputs at ~60%, active bugs at ~80%. These are PROBABILISTIC observations from one person's workflow — not Anthropic documentation or measured benchmarks. Well-managed sessions can work effectively at high utilization.
>
> **What IS structural:** MCP schema overhead advances the fill rate before any task-relevant work begins. CLI+Skills starts at zero. This is the mechanism, regardless of where the specific thresholds fall.

---

### Key Pages

| Page | Layer | Role in the model |
|------|-------|-------------------|
| [[mcp-vs-cli-for-tool-integration|Decision — MCP vs CLI for Tool Integration]] | L6 | The resolved decision — CLI default, MCP for external bridges |
| [[cli-tools-beat-mcp-for-token-efficiency|CLI Tools Beat MCP for Token Efficiency]] | L4 | The lesson — 12x measured differential, structural mechanism |
| [[context-aware-tool-loading|Context-Aware Tool Loading]] | L5 | The generalized pattern — eager/deferred/external |
| [[mcp-integration-architecture|MCP Integration Architecture]] | L2 | MCP server design, tool registration, schema management |
| [[claude-code-context-management|Claude Code Context Management]] | L2 | Context discipline — the constraint MCP/CLI choices optimize for |
| [[harness-engineering|Harness Engineering]] | L2 | Context-mode sandbox pattern for isolated heavy operations |
| [[src-playwright-cli-vs-mcp|Synthesis — Playwright CLI vs MCP — Automate QA with Less Tokens]] | L1 | The primary evidence — 10-step QA test comparison |
| [[src-playwright-mcp-visual-testing|Synthesis — Playwright MCP for Visual Development Testing]] | L1 | The counter-evidence — when MCP wins for interactive visual iteration |
| [[src-context-mode|Synthesis — Context Mode — MCP Sandbox for Context Saving]] | L1 | The sandbox evidence — 98% context saving |
| [[gateway-output-contract\|Gateway Output Contract]] | Standards | The 5-rule output contract for gateway subcommands — proto-programming applied to tool outputs. Added 2026-04-15. |

---

### Lessons Learned

| Lesson | What was learned |
|--------|-----------------|
| [[cli-tools-beat-mcp-for-token-efficiency|CLI Tools Beat MCP for Token Efficiency]] | 12x cost differential is structural (eager vs deferred loading). Default to CLI for operational tasks. |
| [[skills-architecture-is-dominant-extension-pattern|Skills Architecture Is the Dominant LLM Extension Pattern]] | Skills' zero-baseline-cost property is what makes CLI+Skills viable — the skill teaching the CLI tool costs nothing until invoked. |
| [[context-management-is-primary-productivity-lever|Context Management Is the Primary LLM Productivity Lever]] | The MCP vs CLI decision IS a context management decision. Every MCP server connection is a context budget choice. |

---

### State of Knowledge

> [!success] **Well-covered (measured evidence)**
> - 12x cost differential on Playwright (measured, reproduced in dedicated comparison video)
> - Microsoft recommends CLI over MCP for Playwright AI agent use
> - CLI has 3x more features than MCP version of Playwright
> - Context-mode sandbox achieves 98% context saving (measured)
> - Decision framework with 4-step evaluation sequence
> - MCP server design principles (from operating a 26-tool wiki server as of 2026-04-15 — grown from 17)
> - Ecosystem bindings resolved (CLI for internal, MCP for external, sandbox for heavy)

> [!warning] **Thin or unverified**
> - The 12x figure is task-specific (Playwright QA) — no general benchmark across task types
> - Degradation thresholds (40%/60%/80%) — one practitioner's observations, not Anthropic data
> - MCP selective tool exposure — upcoming feature that could reduce eager-load cost
> - Sandbox composition with MCP — can subagents inherit parent MCP registrations?
> - The wiki's own MCP server at 17 tools — is this too many? No measured overhead comparison
> - As context windows reach 1M+, MCP overhead (~2K tokens) becomes 0.2% — does the decision flip?

---

### How to Adopt

> [!info] **Choosing the integration strategy for a new tool**
> 1. Apply the 4-step decision framework (usage pattern → schema cost → discoverability → sandwich case)
> 2. Default to CLI+Skills unless MCP is specifically justified
> 3. If MCP, follow the server design principles (minimize tools, narrow signatures, semantic naming)
> 4. For heavy operations, consider the context-mode sandbox

> [!warning] **INVARIANT — never change these**
> - CLI+Skills is the default for project-internal tooling (the 12x differential is structural)
> - MCP schema overhead is real and compounds per connected server
> - Never connect MCP servers "just in case" — each connection is a per-message context cost
> - The sandwich case (>30% remaining context) always justifies sandbox isolation

> [!tip] **PER-PROJECT — always adapt these**
> - Which tools are MCP vs CLI (depends on usage patterns and discoverability needs)
> - How many MCP servers are acceptable (depends on session length and context sensitivity)
> - Whether to use the context-mode sandbox (depends on whether heavy operations exist)
> - MCP server tool count (the wiki has 17 — a project with 5 tools may expose all via MCP affordably)

### Gateway Tools as Unified Interface (NEW)

The gateway (`tools/gateway.py`) unifies CLI + MCP into one engine. It demonstrates the dual-scope principle: `--wiki-root` targets a project, `--brain` targets the second brain, auto-detection finds both. MCP server extension (E015) will expose gateway operations as MCP tools. See [[wiki-gateway-tools-unified-knowledge-interface|Wiki Gateway Tools — Unified Knowledge Interface]].

## Open Questions

> [!question] ~~****At what MCP server count does schema overhead measurably degrade accuracy?****~~
> **RESOLVED:** ~17-20 tools. Wiki's 17-tool MCP server is "at the upper limit." Beyond 20, selective tool exposure becomes necessary.
> The 12x figure is task-specific. A general benchmark — 1 server, 3 servers, 5 servers × short/medium/long sessions × simple/complex tasks — would make the decision framework empirical. (Requires: controlled testing)

> [!question] ~~****Does MCP selective tool exposure change the equation?****~~
> **RESOLVED:** Yes — selective exposure reduces schema overhead proportionally. Goldilocks applied to tool loading. Not yet widely implemented.
> If MCP servers can expose only tools relevant to a conversation (not all registered tools), the eager-load cost drops. Does this make MCP-first viable? (Requires: testing selective exposure when available)

> [!question] ~~****Does the decision flip at 1M context?****~~
> **RESOLVED:** Shifts from CLI-always to CLI-for-automation + MCP-for-exploration. MCP overhead matters less at 1M but CLI latency/determinism advantages remain.
> At 1M tokens, MCP overhead (~2K) is 0.2% — negligible. But does the degradation curve also flatten? Or does it remain proportional, just shifted? (Requires: testing MCP performance at 1M utilization)

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **Claude Code runtime** | [[model-claude-code|Model — Claude Code]] |
> | **Automation pipelines** | [[model-automation-pipelines|Model — Automation and Pipelines]] |
> | **Gateway tools** | [[gateway-tools-reference|Gateway Tools Reference]] |
> | **Extension system** | [[model-skills-commands-hooks|Model — Skills, Commands, and Hooks]] |

## Relationships

- BUILDS ON: [[cli-tools-beat-mcp-for-token-efficiency|CLI Tools Beat MCP for Token Efficiency]]
- BUILDS ON: [[context-aware-tool-loading|Context-Aware Tool Loading]]
- BUILDS ON: [[mcp-vs-cli-for-tool-integration|Decision — MCP vs CLI for Tool Integration]]
- BUILDS ON: [[mcp-integration-architecture|MCP Integration Architecture]]
- RELATES TO: [[model-skills-commands-hooks|Model — Skills, Commands, and Hooks]]
- RELATES TO: [[model-claude-code|Model — Claude Code]]
- RELATES TO: [[harness-engineering|Harness Engineering]]
- RELATES TO: [[claude-code-context-management|Claude Code Context Management]]
- FEEDS INTO: [[model-ecosystem|Model — Ecosystem Architecture]]

## Backlinks

[[cli-tools-beat-mcp-for-token-efficiency|CLI Tools Beat MCP for Token Efficiency]]
[[context-aware-tool-loading|Context-Aware Tool Loading]]
[[mcp-vs-cli-for-tool-integration|Decision — MCP vs CLI for Tool Integration]]
[[mcp-integration-architecture|MCP Integration Architecture]]
[[model-skills-commands-hooks|Model — Skills, Commands, and Hooks]]
[[model-claude-code|Model — Claude Code]]
[[harness-engineering|Harness Engineering]]
[[claude-code-context-management|Claude Code Context Management]]
[[model-ecosystem|Model — Ecosystem Architecture]]
[[consumer-runtime-signaling-via-mcp-config|Decision — Consumer Runtime Signaling via MCP Config]]
[[e022-context-aware-gateway-orientation-and-routing|E022 — Context-Aware Gateway Orientation and Task Routing]]
[[e022-m002-gateway-orient-subcommand|E022-M002 — Gateway Orient Subcommand (Module Design)]]
[[e022-m003-what-do-i-need-upgrade|E022-M003 — Gateway What-Do-I-Need Upgrade (Module Design)]]
[[e023-gateway-wide-output-contract-audit|E023 — Gateway-Wide Output Contract Audit]]
[[execution-mode-is-consumer-property-not-project-property|Execution Mode Is a Consumer Property, Not a Project Property — Guard Against Conflation Drift]]
[[first-consumer-integration-reveals-systematic-gaps-between-k|First consumer integration reveals systematic gaps between knowledge and tooling]]
[[gateway-output-contract|Gateway Output Contract — What Good Tool Output Looks Like]]
[[mcp-runtime-signaling|MCP Runtime Signaling — Integration Guide for Consumers]]
[[src-7-levels-claude-code-rag|Source — The 7 Levels of Claude Code & RAG]]
[[src-cline-agentic-coding-ide-extension|Synthesis — Cline — Agentic Coding IDE Extension with Plan/Act, Skills, Hooks, MCP]]
