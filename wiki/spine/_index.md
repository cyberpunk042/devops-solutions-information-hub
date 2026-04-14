# Spine

Strategic architecture: models, standards, domain overviews, and the adoption guide.

**Entry point:** [[model-registry|Model Registry]] — all 16 models with status and standards links.

## Methodology System

| Page | What It Covers |
|------|---------------|
| [[methodology-system-map|Methodology System Map]] | Complete system map — every component, where it lives, how to extend — LOOKUP |
| [[model-methodology|Model — Methodology]] | The 9 named models, stage gates, composition, quality tiers — UNDERSTAND |
| [[model-methodology-standards|Methodology Standards — What Good Execution Looks Like]] | Gold standards for methodology execution with real examples |
| [[methodology-adoption-guide|Methodology Adoption Guide]] | 4-tier adoption from read to enforce, per-domain quick starts |
| [[artifact-chains-by-model|Artifact Chains by Methodology Model]] | Full artifact chains for all 9 models |
| [[model-composition-rules|Model Composition Rules]] | Sequential, nested, conditional, parallel composition |
| [[methodology-evolution-protocol|Methodology Evolution Protocol]] | Evidence-driven versioned improvement |
| [[claude-md-structural-patterns|CLAUDE.md Structural Patterns for Agent Compliance]] | 8 patterns that improve agent compliance |
| [[enforcement-hook-patterns|Enforcement Hook Patterns]] | 4 hook types for infrastructure enforcement |
| [[stage-aware-skill-injection|Stage-Aware Skill Injection]] | Per-stage skill recommendations and restrictions |

## Per-Type Page Standards

Every page type has its own standards doc with: section-by-section quality bar, gold-standard exemplar, common failures, content thresholds, and template reference.

| Type | Standards Page | Exemplar |
|------|--------------|----------|
| concept | [[concept-page-standards|Concept Page Standards]] | [[methodology-framework|Methodology Framework]] |
| source-synthesis | [[source-synthesis-page-standards|Source-Synthesis Page Standards]] | [[src-context-mode|Synthesis — Context Mode — MCP Sandbox for Context Saving]] |
| comparison | [[comparison-page-standards|Comparison Page Standards]] | [[cross-domain-patterns|Cross-Domain Patterns]] |
| reference | [[reference-page-standards|Reference Page Standards]] | [[methodology-adoption-guide|Methodology Adoption Guide]] |
| deep-dive | [[deep-dive-page-standards|Deep-Dive Page Standards]] | [[adoption-guide|Adoption Guide — How to Use This Wiki's Standards]] |
| lesson | [[lesson-page-standards|Lesson Page Standards]] | [[cli-tools-beat-mcp-for-token-efficiency|CLI Tools Beat MCP for Token Efficiency]] |
| pattern | [[pattern-page-standards|Pattern Page Standards]] | [[plan-execute-review-cycle|Plan Execute Review Cycle]] |
| decision | [[decision-page-standards|Decision Page Standards]] | [[execution-mode-edge-cases|Decision — Execution Mode Edge Cases]] |
| domain-overview | [[domain-overview-page-standards|Domain Overview Page Standards]] | [[cross-domain-domain-overview|Cross-Domain — Domain Overview]] |
| evolution | [[evolution-page-standards|Evolution Page Standards]] | [[methodology-evolution-history|Evolution — Methodology System]] |
| learning-path | [[learning-path-page-standards|Learning Path Page Standards]] | [[methodology-fundamentals|Learning Path — Methodology Fundamentals]] |
| operations-plan | [[operations-plan-page-standards|Operations Plan Page Standards]] | [[wiki-post-ingestion-operations-plan|Operations Plan — Wiki Post-Ingestion Validation]] |
| epic | [[epic-page-standards|Epic Page Standards]] | [[E003-artifact-type-system|Artifact Type System]] |
| task | [[task-page-standards|Task Page Standards]] | [[T001-test-openai-backend|Test OpenAI backend with LocalAI]] |
| note | [[note-page-standards|Note Page Standards]] | [[2026-04-09-directive-models-are-not-documents|Models Are Not Documents — They Must Be Usable Systems]] |

## Domain Overviews

| Overview | Domain |
|----------|--------|
| [[ai-agents-domain-overview|AI Agents — Domain Overview]] | Agent orchestration, Claude Code, harness engineering |
| [[ai-models-domain-overview|AI Models — Domain Overview]] | Local LLM quantization, model capabilities |
| [[automation-domain-overview|Automation — Domain Overview]] | Pipelines, MCP integration, event-driven automation |
| [[cross-domain-domain-overview|Cross-Domain — Domain Overview]] | Methodology framework, quality tiers |
| [[devops-domain-overview|Devops — Domain Overview]] | Stage gates, ecosystem, infrastructure patterns |
| [[knowledge-systems-domain-overview|Knowledge Systems — Domain Overview]] | LLM Wiki, PKM theory, evolution pipeline |
| [[tools-and-platforms-domain-overview|Tools And Platforms — Domain Overview]] | Obsidian, NotebookLM, AICP, OpenArms |

## Pages

- [AI Agents — Domain Overview](domain-overviews/ai-agents-domain-overview.md) — The ai-agents domain covers the theory, patterns, and practice of building, operating, and orchestrating AI coding ag...
- [AI Models — Domain Overview](domain-overviews/ai-models-domain-overview.md) — The ai-models domain covers LLMs, embeddings, quantization, fine-tuning, and model evaluation — the foundational laye...
- [Automation — Domain Overview](domain-overviews/automation-domain-overview.md) — The automation domain covers scheduling, pipeline orchestration, workflow automation, event-driven patterns, and serv...
- [Cross-Domain — Domain Overview](domain-overviews/cross-domain-domain-overview.md) — The cross-domain area is not a subject-matter domain but a structural layer — it holds concept pages, comparisons, pa...
- [Devops — Domain Overview](domain-overviews/devops-domain-overview.md) — The devops domain covers stage-gate methodology, ecosystem topology, backlog management, task governance, infrastruct...
- [Knowledge Systems — Domain Overview](domain-overviews/knowledge-systems-domain-overview.md) — The knowledge-systems domain covers the theory and architecture of building LLM-powered knowledge bases, from Karpath...
- [Tools And Platforms — Domain Overview](domain-overviews/tools-and-platforms-domain-overview.md) — The tools-and-platforms domain covers the software tools, platforms, CLI utilities, and SaaS products used across the...
- [Evolution — Methodology System](evolution-log/methodology-evolution-history.md) — How the methodology system evolved from prose instructions to infrastructure-enforced stage gates
- [Goldilocks Flow — From Identity to Action](goldilocks-flow.md) — The complete decision flow from "who am I?" to "what do I do next?" — every decision point with criteria, defaults, a...
- [Learning Path — Methodology Fundamentals](learning-paths/methodology-fundamentals.md) — Guided sequence for understanding the research wiki's methodology system — from what a methodology model IS, through ...
- [Model — Claude Code](models/agent-config/model-claude-code.md) — Claude Code is Anthropic's CLI coding agent — a tool-use loop that reads, writes, and reasons about codebases from th...
- [Model — Markdown as IaC — Design.md and Agent Configuration](models/agent-config/model-markdown-as-iac.md) — The Design
- [Model — Skills, Commands, and Hooks](models/agent-config/model-skills-commands-hooks.md) — The AI agent extension ecosystem is a four-level hierarchy: CLAUDE
- [Model — Context Engineering](models/depth/model-context-engineering.md) — Context engineering is the discipline of designing WHAT information reaches an AI agent, in WHAT STRUCTURE, at WHAT D...
- [Model — Knowledge Evolution](models/depth/model-knowledge-evolution.md) — The Knowledge Evolution model describes how raw sources become lessons, patterns, and decisions through a structured,...
- [Model — Local AI ($0 Target)](models/depth/model-local-ai.md) — The Local AI model describes how to reduce AI costs through local inference, model routing, and intelligent fallback ...
- [Model — NotebookLM](models/depth/model-notebooklm.md) — This model addresses a fundamental question for any knowledge wiki: how external grounded research tools complement a...
- [Model — Second Brain](models/depth/model-second-brain.md) — The Second Brain model describes the personal knowledge management (PKM) theoretical foundation that underlies this w...
- [Model — Automation and Pipelines](models/ecosystem/model-automation-pipelines.md) — The Automation and Pipelines model describes how this wiki transforms knowledge work from manual operations into auto...
- [Model — Ecosystem Architecture](models/ecosystem/model-ecosystem.md) — The Ecosystem Architecture model describes how multiple projects form a self-sustaining system where each project has...
- [Model — MCP and CLI Integration](models/ecosystem/model-mcp-cli-integration.md) — The MCP and CLI Integration model resolves one of the most consequential architectural decisions in LLM agent design:...
- [Model — LLM Wiki](models/foundation/model-llm-wiki.md) — The LLM Wiki model defines a knowledge system where an LLM agent maintains a structured markdown wiki — ingesting sou...
- [Model — Methodology](models/foundation/model-methodology.md) — The Methodology model defines a flexible FRAMEWORK for defining, selecting, composing, and adapting work processes
- [Model — Wiki Design](models/foundation/model-wiki-design.md) — The Wiki Design model defines the VISUAL layer of the knowledge system — how pages look and feel, not just what they ...
- [Model — Quality and Failure Prevention](models/quality/model-quality-failure-prevention.md) — Quality and failure prevention for AI agents is not a set of best practices — it is a system with three enforcement l...
- [Model — SFIF and Architecture](models/quality/model-sfif-architecture.md) — The SFIF and Architecture model describes the universal 4-stage build lifecycle (Scaffold → Foundation → Infrastructu...
- [Adoption Guide — How to Use This Wiki's Standards](references/adoption-guide.md) — This guide explains how any project in the ecosystem (or outside it) picks up the methodology, stage-gate system, bac...
- [Context File Taxonomy — The 8 Dimensions of Agent Context](references/context-file-taxonomy.md) — The complexity of agent context is NOT captured by a fixed number of "cognitive contexts
- [Frontmatter Field Reference — Complete Parameter Documentation](references/frontmatter-field-reference.md) — Complete reference for every YAML frontmatter field used in the wiki
- [Gateway Tools Reference — Complete Command Documentation](references/gateway-tools-reference.md) — Complete reference for the wiki gateway — the unified Python interface serving humans (CLI), AI agents (programmatic)...
- [Methodology Adoption Guide](references/methodology-adoption-guide.md) — Step-by-step guide for any project to adopt the research wiki's methodology
- [Methodology System Map](references/methodology-system-map.md) — Complete map of the methodology system — every component, where it lives, what it does, and how they connect
- [Model Registry](references/model-registry.md) — This is the entry point for all named models in the wiki
- [Root Documentation Map — Repository-Level Files](references/root-documentation-map.md) — The repository root contains 8 documentation files (2,714 total lines) that serve as the entry point for humans, AI t...
- [Operations Plan — Second Brain Integration Chain — Complete Walkthrough](references/second-brain-integration-chain.md) — Complete step-by-step chain for integrating ANY project with the second brain
- [Comparison Page Standards](standards/comparison-page-standards.md) — Standards for comparison pages — structured evaluations of alternatives across multiple criteria
- [Concept Page Standards](standards/concept-page-standards.md) — Standards for concept pages — the most common page type in the wiki (74 pages)
- [Decision Page Standards](standards/decision-page-standards.md) — Standards for decision pages — the highest-layer evolved page type (Layer 6)
- [Deep-Dive Page Standards](standards/deep-dive-page-standards.md) — Standards for deep-dive pages — extended analysis that goes significantly deeper than a concept page
- [Domain Overview Page Standards](standards/domain-overview-page-standards.md) — Standards for domain overview pages — curator pages that assess a domain's knowledge state, classify pages by maturit...
- [Epic Page Standards](standards/epic-page-standards.md) — Standards for epic pages — strategic containers that break into modules and tasks
- [Evolution Page Standards](standards/evolution-page-standards.md) — Standards for evolution pages — historical narratives tracking how a concept, system, or domain changed over time
- [Learning Path Page Standards](standards/learning-path-page-standards.md) — Standards for learning path pages — curated sequences that guide a reader through a topic in a specific order
- [Lesson Page Standards](standards/lesson-page-standards.md) — Standards for lesson pages — actionable learnings distilled from convergent evidence across multiple sources
- [Claude Code Standards — What Good Agent Configuration Looks Like](standards/model-standards/model-claude-code-standards.md) — This page defines the quality bar for CLAUDE CODE CONFIGURATION
- [Context Engineering Standards — What Good Structured Context Looks Like](standards/model-standards/model-context-engineering-standards.md) — This page defines the quality bar for CONTEXT ENGINEERING — the discipline of designing what information reaches an A...
- [Evolution Standards — What Good Knowledge Promotion Looks Like](standards/model-standards/model-knowledge-evolution-standards.md) — This page defines the quality bar for KNOWLEDGE EVOLUTION
- [LLM Wiki Standards — What Good Looks Like](standards/model-standards/model-llm-wiki-standards.md) — This page defines the quality bar for every page type in the LLM Wiki model
- [Methodology Standards — What Good Execution Looks Like](standards/model-standards/model-methodology-standards.md) — This page defines the quality bar for METHODOLOGY EXECUTION
- [Quality Standards — What Good Failure Prevention Looks Like](standards/model-standards/model-quality-failure-prevention-standards.md) — This page defines the quality bar for FAILURE PREVENTION
- [Extension Standards — What Good Skills, Commands, and Hooks Look Like](standards/model-standards/model-skills-commands-hooks-standards.md) — This page defines the quality bar for the EXTENSION SYSTEM
- [Wiki Design Standards — What Good Styling Looks Like](standards/model-standards/model-wiki-design-standards.md) — This page defines the quality bar for VISUAL DESIGN in the wiki
- [Note Page Standards](standards/note-page-standards.md) — Standards for note pages — log entries recording directives, session summaries, or completion reports
- [Operations Plan Page Standards](standards/operations-plan-page-standards.md) — Standards for operations plan pages — sequential deterministic checklists that any agent can follow mechanically
- [Pattern Page Standards](standards/pattern-page-standards.md) — Standards for pattern pages — recurring structural phenomena observed across ≥2 independent instances
- [Reference Page Standards](standards/reference-page-standards.md) — Standards for reference pages — LOOKUP material that readers consult for specific answers, not read linearly
- [Source-Synthesis Page Standards](standards/source-synthesis-page-standards.md) — Standards for source-synthesis pages — processed versions of raw sources (articles, videos, papers, repos)
- [Task Page Standards](standards/task-page-standards.md) — Standards for task pages — the atomic work unit
- [Sub-Model — Enforcement Hierarchy — From Instructions to Immune System](super-model/enforcement-hierarchy.md) — Navigation hub for enforcement — how to make agents actually follow methodology
- [Sub-Model — Goldilocks Protocol — Identity and Adaptation](super-model/goldilocks-protocol.md) — Navigation hub for the Goldilocks system — identity declaration, SDLC profile selection, methodology adaptation, and ...
- [Sub-Model — Integration and Ecosystem — Dual-Perspective and Feedback](super-model/integration-ecosystem.md) — Navigation hub for ecosystem integration — how the second brain connects to projects, how feedback flows, and how too...
- [Sub-Model — Knowledge Architecture — Layers, Maturity, and Evolution](super-model/knowledge-architecture.md) — Navigation hub for the knowledge system — how knowledge flows from raw sources through progressive distillation to pr...
- [Super-Model — Research Wiki as Ecosystem Intelligence Hub](super-model/super-model.md) — This is the super-model — the packaging of all 16 models, 22 standards pages, and the full knowledge architecture int...
- [Sub-Model — Work Management — Hierarchy, Tracking, and PM Levels](super-model/work-management.md) — Navigation hub for work management — how work is organized, tracked, and enforced

## Tags

`standards`, `quality`, `spine`, `page-type`, `exemplar`, `model`, `domain-overview`, `methodology`, `gold-standard`, `reference`, `anti-patterns`, `skills`, `concept`, `sub-model`, `navigation-hub`, `hooks`, `second-brain`, `ecosystem`, `integration`, `evolution`
