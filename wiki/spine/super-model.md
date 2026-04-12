---
title: "Super-Model: Research Wiki as Ecosystem Intelligence Hub"
type: reference
domain: cross-domain
layer: spine
status: synthesized
confidence: authoritative
maturity: seed
created: 2026-04-10
updated: 2026-04-10
sources: []
tags: [super-model, second-brain, hub, ecosystem, adoption, models, standards, integration, quality]
---

# Super-Model: Research Wiki as Ecosystem Intelligence Hub

## Summary

This is the super-model — the packaging of all 15 models, 7 standards pages, and the full knowledge architecture into a consumable system that any project in the ecosystem can adopt. The research wiki is not just a documentation project. It is the central intelligence hub that defines HOW work is done (methodology), WHAT knowledge looks like (LLM Wiki), HOW quality is maintained (failure prevention), and HOW projects integrate with each other (ecosystem architecture). This page is the entry point for any project that wants to consume, adhere to, or contribute back to the hub.

> [!info] What the hub offers — v1.0
>
> | Layer | What It Provides | Key Models |
> |-------|-----------------|------------|
> | **Knowledge Architecture** | How to build and maintain a structured wiki | [[Model: LLM Wiki]], [[Model: Second Brain]], [[Model: Knowledge Evolution]] |
> | **Work Process** | How to execute tasks with stage gates and quality gates | [[Model: Methodology]], [[Model: SFIF and Architecture]] |
> | **Agent Configuration** | How to configure Claude Code with skills, hooks, MCP | [[Model: Claude Code]], [[Model: Skills, Commands, and Hooks]], [[Model: Design.md and IaC]] |
> | **Quality Systems** | How to prevent failures and maintain standards | [[Model: Quality and Failure Prevention]], [[Model: Wiki Design]] |
> | **Ecosystem Integration** | How projects connect and share knowledge | [[Model: Ecosystem Architecture]], [[Model: MCP and CLI Integration]] |
> | **Research Tooling** | How to use NotebookLM, Obsidian, local AI as complements | [[Model: NotebookLM]], [[Model: Local AI ($0 Target)]], [[Model: Automation and Pipelines]] |

## Adoption Tiers

Not every project needs everything. Adopt in tiers — each tier builds on the previous:

> [!abstract] Four adoption tiers
>
> | Tier | What You Adopt | Effort | What You Get |
> |------|---------------|--------|-------------|
> | **1. Agent Foundation** | CLAUDE.md as routing table, wiki-schema.yaml, page templates | 1 hour | Structured knowledge base, quality gates on every page |
> | **2. Stage-Gate Process** | methodology.yaml, agent-directive.md, backlog structure | Half day | Stage-gated execution, task tracking, audit trail |
> | **3. Evolution Pipeline** | evolve pipeline, maturity lifecycle, cross-referencing | 1 day | Self-improving wiki, seed→canonical promotion, gap analysis |
> | **4. Hub Integration** | Export profiles, LightRAG sync, MCP tools, bidirectional sync | 2-3 days | Full ecosystem participation, knowledge flows in and out |

**Tier 1 is mandatory. Tiers 2-4 are progressive.** A project at Tier 1 has a structured wiki. At Tier 2 it has disciplined execution. At Tier 3 it generates its own lessons and patterns. At Tier 4 it participates as a full hub member feeding knowledge back to the ecosystem.

## The 15 Models — Dependency Graph

Models are not independent — they build on each other. Here is the adoption order:

> [!tip] Read and adopt in this order
>
> **Foundation (read first):**
> 1. [[Model: LLM Wiki]] — WHAT a wiki IS (schema, operations, quality gates)
> 2. [[Model: Methodology]] — HOW work proceeds (stage gates, task types, composability)
> 3. [[Model: Wiki Design]] — HOW pages LOOK (callout vocabulary, styling standards)
>
> **Execution (read after foundation):**
> 4. [[Model: Claude Code]] — the agent runtime and extension system
> 5. [[Model: Skills, Commands, and Hooks]] — how to extend the agent
> 6. [[Model: Quality and Failure Prevention]] — three-layer defense, failure lessons
> 7. [[Model: SFIF and Architecture]] — the build lifecycle at every scale
>
> **Depth (read when ready):**
> 8. [[Model: Knowledge Evolution]] — maturity lifecycle, scorer, promotion
> 9. [[Model: MCP and CLI Integration]] — tool integration decisions
> 10. [[Model: Design.md and IaC]] — markdown as AI configuration
> 11. [[Model: Second Brain]] — PKM theory (PARA + Zettelkasten)
>
> **Ecosystem (read when integrating):**
> 12. [[Model: Ecosystem Architecture]] — the 5-project topology
> 13. [[Model: Automation and Pipelines]] — pipeline chains, event-driven automation
> 14. [[Model: NotebookLM]] — grounded research complement
> 15. [[Model: Local AI ($0 Target)]] — cost reduction via local inference

## Per-Project Adaptation

Each project adapts the super-model to its context:

> [!info] How ecosystem projects instantiate the super-model
>
> | Project | Tier | Key Adaptations |
> |---------|------|----------------|
> | **OpenArms** | 4 (full) | TypeScript stack, methodology.yaml with 7 task types, 8 execution modes, OpenClaw gateway integration |
> | **OpenFleet** | 4 (full) | MCP tool blocking for stage enforcement, 10-agent fleet, deterministic orchestrator, LightRAG integration |
> | **AICP** | 2 (process) | Python stack, backend routing profiles, circuit breaker patterns, 78 skills |
> | **devops-control-plane** | 1 (foundation) | TUI/CLI/Web interfaces, tech auto-detection, vault security, 24 immune system rules |
> | **Research Wiki** | 4 (full, reference) | The reference implementation — all models, all standards, all tooling |

## Quality Contract

> [!warning] What the hub guarantees vs what projects must maintain
>
> **The hub guarantees:**
> - Every model page passes validation (frontmatter, required sections, relationships)
> - Every standards page demonstrates what it defines (self-referential integrity)
> - Knowledge flows wiki → projects via export profiles and LightRAG sync
> - The evolution pipeline continuously improves models through cross-referencing
> - All operator directives are preserved verbatim in wiki/log/
>
> **Each project must:**
> - Maintain its own CLAUDE.md as a routing table (not an encyclopedia)
> - Run quality gates appropriate to its stack (the GATE is universal; the COMMAND is per-project)
> - Feed operational learnings back to the wiki (incidents, methodology evolution, tool discoveries)
> - Adopt at least Tier 1 (schema + templates + quality gates)

## What "v1.0" Means

This is the first version of the super-model. It is honest about its maturity:

> [!abstract] v1.0 state assessment
>
> | Aspect | State | Evidence |
> |--------|-------|---------|
> | **Models** | 15 defined, all at growing maturity | [[Model Registry]] — 200-500 lines each, standard sections |
> | **Standards** | 7 companion pages | Quality bars defined for methodology, wiki, design, claude code, skills, evolution, quality |
> | **Decisions** | 13 resolved | 51 open questions answered via cross-referencing |
> | **Lessons** | 31 codified | 6 from operator directives, 11 convergence, 8 core failure/practice |
> | **Lint** | 1 issue (expected) | 0 dead relationships, 0 orphans, 0 thin pages |
> | **Styling** | 86% (159/184) | All content pages styled with Obsidian callout vocabulary |
> | **Adoption proof** | 3 projects | OpenArms (full), OpenFleet (full), AICP (partial) |
>
> **What v1.0 does NOT have:**
> - Canonical maturity on any model (all are growing — promotions gated by operator)
> - Automated adoption validation (no tool that checks a project's compliance with the super-model)
> - Complete open question resolution (86 remain, mostly needing external research)
> - New source ingestion this session (evolution has been internal cross-referencing)

## How to Use This Page

**If you're the operator:** This is your dashboard for the wiki's state as a consumable system. Review the v1.0 assessment. Decide which models are ready for the next maturity promotion. Identify gaps that need fresh research.

**If you're an agent from another project:** Start with the Adoption Tiers table. Determine your project's current tier. Follow the model dependency graph in order. Read each model + its standards page. Adapt per the Per-Project Adaptation table.

**If you're building this wiki further:** The quality contract defines what must be maintained. The v1.0 assessment shows where the gaps are. The evolution pipeline (`pipeline evolve --score`) identifies the next improvement candidates.

## Key Pages

| Page | Role |
|------|------|
| [[Model Registry]] | All 15 models with status and standards links |
| [[Adoption Guide — How to Use This Wiki's Standards]] | Detailed adoption walkthrough |
| [[Methodology Framework]] | The meta-methodology that governs all models |
| [[Four-Project Ecosystem]] | The 5-project topology and knowledge flow |

## Open Questions

> [!question] What is the minimum viable super-model for a project that only needs knowledge architecture (no methodology)?
> A project that wants structured wiki pages but not stage gates. Tier 1 covers this — but the current Tier 1 bundles schema + methodology. Should there be a Tier 0: "just the wiki, no process"?

> [!question] How should the super-model version when models evolve independently?
> Model: LLM Wiki might reach mature while Model: Claude Code is still growing. Does the super-model version reflect the lowest common denominator, or the overall system state?

> [!question] Should there be a super-model compliance checker?
> A tool that reads a project's CLAUDE.md and methodology.yaml and reports which models are adopted, at what tier, and what's missing. This would make adoption measurable.

## Relationships

- CONTAINS: [[Model Registry]]
- CONTAINS: [[Adoption Guide — How to Use This Wiki's Standards]]
- BUILDS ON: [[Methodology Framework]]
- BUILDS ON: [[Model: LLM Wiki]]
- ENABLES: [[Four-Project Ecosystem]]
- FEEDS INTO: [[Model: Ecosystem Architecture]]

## Backlinks

[[Model Registry]]
[[Adoption Guide — How to Use This Wiki's Standards]]
[[Methodology Framework]]
[[Model: LLM Wiki]]
[[Four-Project Ecosystem]]
[[Model: Ecosystem Architecture]]
[[Evolution: Methodology System]]
[[Learning Path: Methodology Fundamentals]]
[[Methodology Adoption Guide]]
