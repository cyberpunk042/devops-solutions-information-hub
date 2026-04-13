---
title: Super-Model — Research Wiki as Ecosystem Intelligence Hub
aliases:
  - "Super-Model — Research Wiki as Ecosystem Intelligence Hub"
  - "Super-Model: Research Wiki as Ecosystem Intelligence Hub"
type: reference
domain: cross-domain
layer: spine
status: synthesized
confidence: authoritative
maturity: growing
created: 2026-04-10
updated: 2026-04-12
sources: []
tags: [super-model, second-brain, hub, ecosystem, adoption, models, standards, integration, quality]
---

# Super-Model — Research Wiki as Ecosystem Intelligence Hub
## Summary

This is the super-model — the packaging of all 15 models, 7 standards pages, and the full knowledge architecture into a consumable system that any project in the ecosystem can adopt. The research wiki is not just a documentation project. It is the central intelligence hub that defines HOW work is done (methodology), WHAT knowledge looks like (LLM Wiki), HOW quality is maintained (failure prevention), and HOW projects integrate with each other (ecosystem architecture). This page is the entry point for any project that wants to consume, adhere to, or contribute back to the hub.

> [!info] What the hub offers — v1.0
>
> | Layer | What It Provides | Key Models |
> |-------|-----------------|------------|
> | **Knowledge Architecture** | How to build and maintain a structured wiki | [[model-llm-wiki|Model — LLM Wiki]], [[model-second-brain|Model — Second Brain]], [[model-knowledge-evolution|Model — Knowledge Evolution]] |
> | **Work Process** | How to execute tasks with stage gates and quality gates | [[model-methodology|Model — Methodology]], [[model-sfif-architecture|Model — SFIF and Architecture]] |
> | **Agent Configuration** | How to configure Claude Code with skills, hooks, MCP | [[model-claude-code|Model — Claude Code]], [[model-skills-commands-hooks|Model — Skills, Commands, and Hooks]], [[model-markdown-as-iac|Model — Markdown as IaC — Design.md and Agent Configuration]] |
> | **Quality Systems** | How to prevent failures and maintain standards | [[model-quality-failure-prevention|Model — Quality and Failure Prevention]], [[model-wiki-design|Model — Wiki Design]] |
> | **Ecosystem Integration** | How projects connect and share knowledge | [[model-ecosystem|Model — Ecosystem Architecture]], [[model-mcp-cli-integration|Model — MCP and CLI Integration]] |
> | **Research Tooling** | How to use NotebookLM, Obsidian, local AI as complements | [[model-notebooklm|Model — NotebookLM]], [[model-local-ai|Model — Local AI ($0 Target)]], [[model-automation-pipelines|Model — Automation and Pipelines]] |

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
> 1. [[model-llm-wiki|Model — LLM Wiki]] — WHAT a wiki IS (schema, operations, quality gates)
> 2. [[model-methodology|Model — Methodology]] — HOW work proceeds (stage gates, task types, composability)
> 3. [[model-wiki-design|Model — Wiki Design]] — HOW pages LOOK (callout vocabulary, styling standards)
>
> **Execution (read after foundation):**
> 4. [[model-claude-code|Model — Claude Code]] — the agent runtime and extension system
> 5. [[model-skills-commands-hooks|Model — Skills, Commands, and Hooks]] — how to extend the agent
> 6. [[model-quality-failure-prevention|Model — Quality and Failure Prevention]] — three-layer defense, failure lessons
> 7. [[model-sfif-architecture|Model — SFIF and Architecture]] — the build lifecycle at every scale
>
> **Depth (read when ready):**
> 8. [[model-knowledge-evolution|Model — Knowledge Evolution]] — maturity lifecycle, scorer, promotion
> 9. [[model-mcp-cli-integration|Model — MCP and CLI Integration]] — tool integration decisions
> 10. [[model-markdown-as-iac|Model — Markdown as IaC — Design.md and Agent Configuration]] — markdown as AI configuration
> 11. [[model-second-brain|Model — Second Brain]] — PKM theory (PARA + Zettelkasten)
>
> **Ecosystem (read when integrating):**
> 12. [[model-ecosystem|Model — Ecosystem Architecture]] — the 5-project topology
> 13. [[model-automation-pipelines|Model — Automation and Pipelines]] — pipeline chains, event-driven automation
> 14. [[model-notebooklm|Model — NotebookLM]] — grounded research complement
> 15. [[model-local-ai|Model — Local AI ($0 Target)]] — cost reduction via local inference

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

## What "v2.0" Means

Updated to reflect deep sister project scan, work management framework, and SDLC customization (2026-04-12):

> [!abstract] v2.0 state assessment
>
> | Aspect | State | Evidence |
> |--------|-------|---------|
> | **Pages** | 258 total | +21 from continuation session (was 237 at start) |
> | **Models** | 15 defined + 9 methodology models | [[model-registry|Model Registry]] + [[model-methodology|Model — Methodology]] |
> | **Standards** | 7 model standards + 15 per-type standards + 3 annotated exemplars | wiki/spine/standards/ — lesson, pattern, decision standards now have inline annotated walkthroughs |
> | **Artifact taxonomy** | 78 types across 11 categories + milestone type | [[methodology-artifact-taxonomy|Methodology Artifact Taxonomy]] + milestone added to schema |
> | **Domain chains** | 4 domains | TypeScript, Python/Wiki, Infrastructure, Knowledge |
> | **Decisions** | 17 resolved | +1: When to Use Milestone vs Epic vs Module vs Task |
> | **Lessons** | 43 codified | +6 from sister projects: Infrastructure Enforcement, Agent Failure Taxonomy (6 classes), Context Compaction, Structured Context, Mindful Enforcement, Models Built in Layers (refreshed) |
> | **Patterns** | 17 documented | +6: Three Lines of Defense, Harness-Owned Loop, Contribution Gating, Tier-Based Context, Validation Matrix, Ecosystem Feedback Loop |
> | **Concepts** | 3 new | SDLC Customization Framework, Readiness vs Progress, Three PM Levels |
> | **Work management** | Complete framework | 4-level hierarchy (Milestone→Epic→Module→Task), 8 impediment types, readiness vs progress (two-dimensional), 3 PM levels, harness v1→v2→v3 |
> | **Templates** | 5 created/upgraded + milestone new | note, epic, learning-path, evolution upgraded; milestone created |
> | **Config** | Extended | milestone type, progress field, impediment_type enum, 6 new optional fields |
> | **Relationships** | 1,698 | +139 from session |
> | **Validation** | 0 errors | All pages pass pipeline post |
> | **External research** | SDLC frameworks | CMMI maturity levels, Lean Startup BML, EPAM ADLC, PwC Agentic SDLC |
> | **Sister project scan** | Deep | OpenArms v10 (1033-line validator, 4 hooks, 6 failure classes), OpenFleet (immune system, tiers, contributions, dispatch) |
> | **Frontmatter reference** | Complete | Every field documented with meaning, requirements, valid values, automation enablement |
> | **Epics scaffolded** | 2 | Gateway Tools (6 modules, 25-35 tasks), SDLC Rules (5 modules, 20-30 tasks) |
>
> **What v2.0 added over v1.3:**
> - 5 sub-super-models: Goldilocks, Enforcement, Knowledge, Work Management, Integration — each a navigation hub
> - Root super-model slimmed to dashboard + routing table
>
> **What v1.3 added (the 2026-04-12 session):**
> - Deep OpenArms/OpenFleet scan: real enforcement data (25%→100% compliance), 6 behavioral failure classes, immune system architecture, contribution gating, tier progression, validation matrix
> - Work management framework: milestones, 8 impediment types, readiness vs progress as independent dimensions, 3 PM levels (L1:Wiki → L2:Fleet → L3:Full PM), harness version progression
> - SDLC customization: phase (POC→Production) × scale (10k→15M) × chain (simplified/default/full), backed by CMMI, Lean Startup, and Agentic SDLC research
> - Annotated exemplars: lesson, pattern, and decision standards now have full inline walkthroughs showing WHY each part of the exemplar is good
> - Frontmatter field reference: complete parameter documentation with automation enablement column
> - 6 model pages updated with quantified enforcement evidence
> - Learning path expanded to 24 pages in 6 parts (was 17 in 5 parts)
>
> **What v2.0 does NOT have (remaining in Milestone v2.0):**
> - Canonical maturity on any model (all growing — promotions gated by operator)
> - Gateway tools implemented (epic scaffolded, needs design+build)
> - SDLC chain configs (simplified/default/full YAML profiles — epic scaffolded)
> - Automated compliance checking tooling (evidence-backed now, not yet built)
> - "Magic tricks" formalized (structured context principle captured, grammar not yet defined)
> - Multi-agent handoff artifact format (contribution gating documented but handoff format TBD)
> - 10-15 new source ingestions (operator has material ready)

## How to Use This Page

### How to Use This Page — Start Here, Go Anywhere

**First question to answer: WHO ARE YOU?** → [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]]

> [!abstract] Entry Points by Identity
>
> | If You Are... | Start With | Then |
> |---------------|-----------|------|
> | **The operator** | This page (dashboard) → v1.3 assessment | Decide maturity promotions, identify gaps, plan next session |
> | **A solo agent on a project** | [[methodology-adoption-guide|Methodology Adoption Guide]] → pick your tier | Read the model for your task type → follow stage sequence |
> | **A harness-managed agent** | Your stage skill (injected by harness) | The skill points to the right methodology model and artifacts |
> | **An agent from another project connecting to the second brain** | [[ai-methodology-consumption-guide|How AI Agents Consume the Methodology Wiki]] → 4 entry paths | Query methodology, get standards, adapt to your domain |
> | **A system designer** | [[model-methodology|Model — Methodology]] → [[three-pm-levels|Three PM Levels — Wiki to Fleet to Full Tool]] | Design the right PM infrastructure for your scale |
> | **A human learning the system** | [[methodology-fundamentals|Learning Path — Methodology Fundamentals]] → 24 pages in 6 parts | Progressive learning from concepts to execution to enforcement |

> [!tip] The Weave — How Everything Connects
>
> ```
> IDENTITY (who am I?) ←→ GOLDILOCKS (what's "just right"?)
>     ↓                          ↓
> SDLC CHAIN (simplified/default/full) ←→ PROJECT PHASE (POC→Production)
>     ↓                                        ↓
> METHODOLOGY MODEL (which stages?) ←→ DOMAIN PROFILE (which artifacts?)
>     ↓                                    ↓
> ENFORCEMENT (hooks/harness/immune) ←→ PM LEVEL (L1/L2/L3)
>     ↓                                    ↓
> EXECUTION (stages, gates, artifacts) ←→ TRACKING (readiness + progress)
>     ↓                                    ↓
> LEARNING (lessons, patterns, decisions) → feeds back to IDENTITY + METHODOLOGY
> ```
>
> Every node connects to every other node. Enter from ANY point and navigate to what you need. The system is not linear — it's a web with the super-model at the center.

## Sub-Super-Models — Navigate by Domain

> [!abstract] The Root Routes to 5 Domain Hubs
>
> | Sub-Model | Domain | Enter When You Need |
> |-----------|--------|-------------------|
> | [[goldilocks-protocol|Sub-Model — Goldilocks Protocol — Identity and Adaptation]] | Identity, chains, adaptation | "What am I? What process is right for me?" |
> | [[enforcement-hierarchy|Sub-Model — Enforcement Hierarchy — From Instructions to Immune System]] | Enforcement, hooks, harness, compliance | "How do I make agents follow methodology?" |
> | [[knowledge-architecture|Sub-Model — Knowledge Architecture — Layers, Maturity, and Evolution]] | Layers, types, evolution, standards | "How does knowledge grow? What quality bar applies?" |
> | [[work-management|Sub-Model — Work Management — Hierarchy, Tracking, and PM Levels]] | Backlog, readiness/progress, PM levels | "How do I organize and track work?" |
> | [[integration-ecosystem|Sub-Model — Integration and Ecosystem — Dual-Perspective and Feedback]] | Ecosystem, gateway, dual-scope, feedback | "How do I connect to the second brain?" |

Each sub-model is a NAVIGATION HUB for its domain — it lists member pages, entry points (CLI + Obsidian + MCP), and how to navigate from there. Start at the sub-model that matches your question, then drill into specifics.

## Key Pages

| Page | Role |
|------|------|
| [[model-registry|Model Registry]] | All 15 models with status and standards links |
| [[methodology-system-map|Methodology System Map]] | Complete lookup for every methodology component |
| [[methodology-adoption-guide|Methodology Adoption Guide]] | 4-tier adoption with per-domain quick starts |
| [[second-brain-integration-chain|Operations Plan — Second Brain Integration Chain — Complete Walkthrough]] | 17-step integration chain end-to-end |
| [[methodology-fundamentals|Learning Path — Methodology Fundamentals]] | 30-page learning path in 8 parts |
| [[frontmatter-field-reference|Frontmatter Field Reference — Complete Parameter Documentation]] | Every frontmatter field documented |
| [[four-project-ecosystem|Four-Project Ecosystem]] | The 5-project topology and knowledge flow |

## Open Questions

> [!question] What is the minimum viable super-model for a project that only needs knowledge architecture (no methodology)?
> A project that wants structured wiki pages but not stage gates. Tier 1 covers this — but the current Tier 1 bundles schema + methodology. Should there be a Tier 0: "just the wiki, no process"?

> [!question] ~~How should the super-model version when models evolve independently?~~
> **RESOLVED:** Super-model version reflects system-level changes (new sub-models, structural reorganization). Individual model updates don't bump super-model version.
> Model: LLM Wiki might reach mature while Model: Claude Code is still growing. Does the super-model version reflect the lowest common denominator, or the overall system state?

> [!question] ~~Should there be a super-model compliance checker?~~
> **RESOLVED:** Yes — a gateway command that reads CLAUDE.md + methodology.yaml and reports adoption tier + gaps. Future work.
> A tool that reads a project's CLAUDE.md and methodology.yaml and reports which models are adopted, at what tier, and what's missing. This would make adoption measurable.

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **All 15 models listed** | [[model-registry|Model Registry]] |
> | **Foundation model: wiki** | [[model-llm-wiki|Model — LLM Wiki]] |
> | **Foundation model: methodology** | [[model-methodology|Model — Methodology]] |
> | **System map (find anything)** | [[methodology-system-map|Methodology System Map]] |
> | **Learning path (read in order)** | [[methodology-fundamentals|Learning Path — Methodology Fundamentals]] |
> | **Adoption guide (get started)** | [[methodology-adoption-guide|Methodology Adoption Guide]] |
> | **Identity protocol** | [[project-self-identification-protocol|Project Self-Identification Protocol]] |

## Relationships

- CONTAINS: [[model-registry|Model Registry]]
- CONTAINS: [[adoption-guide|Adoption Guide — How to Use This Wiki's Standards]]
- BUILDS ON: [[methodology-framework|Methodology Framework]]
- BUILDS ON: [[model-llm-wiki|Model — LLM Wiki]]
- ENABLES: [[four-project-ecosystem|Four-Project Ecosystem]]
- FEEDS INTO: [[model-ecosystem|Model — Ecosystem Architecture]]

## Backlinks

[[model-registry|Model Registry]]
[[adoption-guide|Adoption Guide — How to Use This Wiki's Standards]]
[[methodology-framework|Methodology Framework]]
[[model-llm-wiki|Model — LLM Wiki]]
[[four-project-ecosystem|Four-Project Ecosystem]]
[[model-ecosystem|Model — Ecosystem Architecture]]
[[e010-model-updates-all-15-models-reflect-current-knowledge|E010 — Model Updates — All 15 Models Reflect Current Knowledge]]
[[e013-super-model-evolution-v2-0-with-sub-super-models|E013 — Super-Model Evolution — v2.0 with Sub-Super-Models]]
[[ecosystem-feedback-loop-wiki-as-source-of-truth|Ecosystem Feedback Loop — Wiki as Source of Truth]]
[[methodology-evolution-history|Evolution — Methodology System]]
[[methodology-fundamentals|Learning Path — Methodology Fundamentals]]
[[methodology-adoption-guide|Methodology Adoption Guide]]
[[second-brain-complete-system-v2-0|Milestone — Second Brain Complete System — v2.0]]
[[right-process-for-right-context-the-goldilocks-imperative|Principle — Right Process for Right Context — The Goldilocks Imperative]]
[[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]]
[[identity-profile|Research Wiki — Identity Profile]]
[[sdlc-customization-framework|SDLC Customization Framework — Phases, Scale, and Chain Selection]]
[[second-brain-integration-requirements|Second Brain Integration System — Full Chain Requirements]]
[[enforcement-hierarchy|Sub-Model — Enforcement Hierarchy — From Instructions to Immune System]]
[[goldilocks-protocol|Sub-Model — Goldilocks Protocol — Identity and Adaptation]]
[[integration-ecosystem|Sub-Model — Integration and Ecosystem — Dual-Perspective and Feedback]]
[[knowledge-architecture|Sub-Model — Knowledge Architecture — Layers, Maturity, and Evolution]]
[[work-management|Sub-Model — Work Management — Hierarchy, Tracking, and PM Levels]]
[[the-wiki-is-a-hub-not-a-silo|The Wiki Is a Hub, Not a Silo]]
