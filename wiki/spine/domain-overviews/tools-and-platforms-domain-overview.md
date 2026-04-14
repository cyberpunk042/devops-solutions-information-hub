---
title: Tools And Platforms — Domain Overview
aliases:
  - "Tools And Platforms — Domain Overview"
type: domain-overview
domain: tools-and-platforms
layer: spine
status: synthesized
confidence: high
maturity: growing
created: 2026-04-08
updated: 2026-04-13
sources: []
tags: [domain-overview, tools-and-platforms]
---

# Tools And Platforms — Domain Overview

## Summary

The tools-and-platforms domain covers the software tools, platforms, CLI utilities, and SaaS products used across the four-project ecosystem. With 10 concept pages, it is the most heterogeneous domain, spanning project management (Plane), knowledge visualization (Obsidian), research synthesis (NotebookLM), AI control infrastructure (AICP), local-first AI assistant (OpenArms), multi-channel access patterns, and CLI automation tools (notebooklm-py, Obsidian CLI, NotebookLM Skills, Obsidian Skills Ecosystem). The domain acts as the connector layer — each tool here bridges agent operations (ai-agents domain) with knowledge management (knowledge-systems domain) or project execution (devops domain). Coverage is strong for the tools actively integrated into the ecosystem: AICP, Plane, and OpenArms are documented from primary sources (live project CLAUDE.md files), while the Obsidian and NotebookLM tooling is sourced from multiple YouTube transcripts and GitHub repositories.

> [!info] Domain at a glance
>
> | Metric | Value |
> |--------|-------|
> | Concept pages | 10 |
> | Related model pages | [[model-mcp-cli-integration|Model — MCP and CLI Integration]], [[model-notebooklm|Model — NotebookLM]], [[model-wiki-design|Model — Wiki Design]] |
> | Decision pages | [[mcp-vs-cli-for-tool-integration|Decision — MCP vs CLI for Tool Integration]], [[obsidian-vs-notebooklm-as-knowledge-interface|Decision — Obsidian vs NotebookLM as Knowledge Interface]] |
> | Related lessons | 4+ (Obsidian as Knowledge Infrastructure, NotebookLM as Grounded Research Engine, Skills Architecture Is Dominant Extension Pattern, etc.) |

## State of Knowledge

> [!tip] The Connector Layer
> Each tool here bridges agent operations (ai-agents domain) with knowledge management (knowledge-systems domain) or project execution (devops domain). The domain acts as the connector layer across the entire ecosystem.

**Authoritative coverage:**
- AICP — sourced directly from the live project documentation. 60 Python modules, 1,631 tests, 78 skills, 9 loaded models, 5-stage LocalAI independence roadmap. The most architecturally rich page in this domain.
- Plane — sourced from official docs and DSPD project documentation. PM bridge between human planning and agent execution is well understood.
- OpenArms — sourced from the live project. Local-first personal AI assistant with Gateway daemon, multi-channel routing.

**Good coverage:**
- NotebookLM — multiple source transcripts cover features, notebook paradigm, and content output types.
- Obsidian Knowledge Vault — primary Karpathy sources plus dedicated YouTube transcript. Graph view, web clipper, git-sync.
- notebooklm-py CLI — well-documented Python package covering notebook management API.
- Obsidian Skills Ecosystem — synthesized comparison of three-layer architecture across kepano, Axton, and Pablo-mano skills.
- Multi-Channel AI Agent Access — architectural pattern of single agent runtime reachable through multiple interfaces.

**Thin coverage:**
- Obsidian CLI — the first-party command-line interface (shipped with Obsidian v1) is documented but MCP integration potential and programmatic sync patterns need deeper treatment.
- NotebookLM Skills — two independent open-source bridging projects are documented but their current maintenance status and reliability are unclear.
- The MCP layer for Obsidian and NotebookLM is architecturally planned (see MCP Integration Architecture in automation domain) but not yet implemented or documented at depth.

## Maturity Map

| Maturity | Pages |
|----------|-------|
| **growing** (all 10) | AICP, Plane, OpenArms, NotebookLM, Obsidian Knowledge Vault, notebooklm-py CLI, NotebookLM Skills, Obsidian CLI, Obsidian Skills Ecosystem, Multi-Channel AI Agent Access |

All pages assigned maturity. All styled with callout vocabulary. All have standard sections.

## Gaps

- **End-to-end Obsidian automation**: Obsidian CLI is documented but the complete workflow of Claude Code → Obsidian CLI → vault sync → graph refresh → wikilink update is not consolidated into a single operational pattern.
- **NotebookLM as research validator**: The concept of using NotebookLM as a second-opinion research tool (ingest wiki sources → query → compare against wiki conclusions) is mentioned but not developed.
- **AICP router as shared service**: Whether the backend routing logic in AICP can be exposed to other ecosystem projects (including this wiki) is an open question that hasn't been investigated.
- **Plane API depth**: The Plane REST API, webhook support, and bidirectional sync architecture with Mission Control are mentioned in the OpenFleet page but the Plane page doesn't go deep on the sync mechanisms.
- **Tool comparison matrix**: No formal comparison exists between NotebookLM and the LLM Wiki Pattern for the same use case. Both serve research synthesis but with different tradeoffs (cloud-only vs local, structured export vs conversation, etc.).
- **LocalAI model inventory**: AICP lists 9 models but there is no dedicated page on model selection rationale, benchmark comparisons, or the tradeoff between Qwen3 and Gemma4 for specific task types.

## Priorities

1. **Obsidian automation consolidation** — Single page or pattern documenting the complete Claude Code ↔ Obsidian CLI ↔ vault sync workflow
2. **NotebookLM as research cross-validator** — Design and document the pattern of using NotebookLM to cross-validate wiki conclusions
3. **AICP router exposure** — Investigate whether AICP's routing logic can be called by other projects; document findings
4. **Plane API and sync architecture** — Deep-dive on bidirectional sync mechanisms between Plane and Mission Control
5. **LocalAI model selection guide** — Structured comparison of Qwen3 vs Gemma4 vs Hermes for agent inference tasks

## Key Pages

1. **[AICP](../../domains/tools-and-platforms/aicp.md)** — The AI Control Platform orchestrating local and cloud backends. Central to the ecosystem's goal of 80%+ Claude token reduction through local inference.
2. **[OpenArms](../../domains/tools-and-platforms/openarms.md)** — Local-first personal AI assistant with Gateway daemon. Multi-channel routing across CLI, messaging, and browser.
3. **[Obsidian Knowledge Vault](../../domains/tools-and-platforms/obsidian-knowledge-vault.md)** — The visual frontend for the LLM Wiki Pattern. Graph view, web clipper, and the "Obsidian is the IDE" framing.
4. **[Plane](../../domains/tools-and-platforms/plane.md)** — Open-source project management. The human-facing PM surface that syncs bidirectionally with OpenFleet's Mission Control.
5. **[NotebookLM](../../domains/tools-and-platforms/notebooklm.md)** — Google's source-grounded research tool. Multi-format output (audio overviews, slides, quizzes) from user-supplied sources.
6. **[Obsidian Skills Ecosystem](../../domains/tools-and-platforms/obsidian-skills-ecosystem.md)** — Three-layer architecture for AI agent skills around Obsidian. Cross-project pattern synthesis.

## FAQ

### Q: What is AICP and why is it central to the ecosystem?
AICP (AI Control Platform) is the backend routing layer that dispatches LLM requests to the right model — local inference for simple tasks, Claude API for complex ones. Its complexity scoring targets 80%+ token reduction from Claude API by offloading to local Ollama/LocalAI models. It's the cost-reduction engine for the entire fleet. See [[aicp|AICP]].

### Q: Should I use Obsidian or NotebookLM as the wiki frontend?
They serve different purposes: Obsidian is the long-term structured knowledge vault (graph view, wikilinks, offline-first, git-backed). NotebookLM is the research validation layer (audio overviews, source-grounded Q&A, hallucination reduction). Use both: Obsidian for compounding knowledge, NotebookLM for cross-checking specific claims. See [[obsidian-knowledge-vault|Obsidian Knowledge Vault]] and [[notebooklm|NotebookLM]].

### Q: What is the Obsidian Skills Ecosystem and how do the three layers fit together?
Three independently developed skill sets compose into a complete Obsidian automation stack: kepano (format standards), axton (content generation in those formats), and pablo-mano (130+ CLI commands for programmatic vault control). Each layer builds on the one below. See [[obsidian-skills-ecosystem|Obsidian Skills Ecosystem]].

### Q: How does Plane connect to the AI agent ecosystem?
Plane is the human-facing PM surface that syncs bidirectionally with OpenFleet's Mission Control. Agents write task status to BOARD.md; the orchestrator syncs that to Plane issues; humans update Plane; changes flow back to BOARD.md. It's the human↔agent task handoff layer. See the [[plane|Plane]] page and [[openfleet|OpenFleet]].

### Q: What is MCP vs CLI+Skills for tool integration, and which should I choose?
CLI+Skills is 12x cheaper in token cost, more accurate for project-internal tooling, and simpler to debug. MCP is for external service bridges (cross-conversation tool discovery, ecosystem-wide integrations). Default to CLI+Skills; use MCP only when a tool needs to be available across unrelated conversations. See [[mcp-vs-cli-for-tool-integration|Decision — MCP vs CLI for Tool Integration]].

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **Models covering this domain** | [[model-mcp-cli-integration|Model — MCP and CLI Integration]], [[model-notebooklm|Model — NotebookLM]], [[model-wiki-design|Model — Wiki Design]] |
> | **Standards for this page type** | [[domain-overview-page-standards|Domain Overview Page Standards]] |
> | **Super-model (all models)** | [[super-model|Super-Model]] |
> | **System map** | [[methodology-system-map|Methodology System Map]] |
> | **Learning path** | [[methodology-fundamentals|Learning Path — Methodology Fundamentals]] |

## Relationships

- USED BY: [[ai-agents-domain-overview|AI Agents — Domain Overview]]
- IMPLEMENTS: [[knowledge-systems-domain-overview|Knowledge Systems — Domain Overview]]
- FEEDS INTO: [[automation-domain-overview|Automation — Domain Overview]]
- RELATES TO: [[devops-domain-overview|Devops — Domain Overview]]
- BUILDS ON: [[ai-models-domain-overview|AI Models — Domain Overview]]
- RELATES TO: [[cross-domain-domain-overview|Cross-Domain — Domain Overview]]

## Backlinks

[[ai-agents-domain-overview|AI Agents — Domain Overview]]
[[knowledge-systems-domain-overview|Knowledge Systems — Domain Overview]]
[[automation-domain-overview|Automation — Domain Overview]]
[[devops-domain-overview|Devops — Domain Overview]]
[[ai-models-domain-overview|AI Models — Domain Overview]]
[[cross-domain-domain-overview|Cross-Domain — Domain Overview]]
