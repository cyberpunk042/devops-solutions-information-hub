# Spine

Strategic architecture: models, standards, domain overviews, and the adoption guide.

**Entry point:** [[Model Registry]] — all 15 models with status and standards links.

## Methodology System

| Page | What It Covers |
|------|---------------|
| [[Methodology System Map]] | Complete system map — every component, where it lives, how to extend — LOOKUP |
| [[Model: Methodology]] | The 9 named models, stage gates, composition, quality tiers — UNDERSTAND |
| [[Methodology Standards — What Good Execution Looks Like]] | Gold standards for methodology execution with real examples |
| [[Methodology Adoption Guide]] | 4-tier adoption from read to enforce, per-domain quick starts |
| [[Artifact Chains by Methodology Model]] | Full artifact chains for all 9 models |
| [[Model Composition Rules]] | Sequential, nested, conditional, parallel composition |
| [[Methodology Evolution Protocol]] | Evidence-driven versioned improvement |
| [[CLAUDE.md Structural Patterns for Agent Compliance]] | 8 patterns that improve agent compliance |
| [[Enforcement Hook Patterns]] | 4 hook types for infrastructure enforcement |
| [[Stage-Aware Skill Injection]] | Per-stage skill recommendations and restrictions |

## Per-Type Page Standards

Every page type has its own standards doc with: section-by-section quality bar, gold-standard exemplar, common failures, content thresholds, and template reference.

| Type | Standards Page | Exemplar |
|------|--------------|----------|
| concept | [[Concept Page Standards]] | [[Methodology Framework]] |
| source-synthesis | [[Source-Synthesis Page Standards]] | [[Synthesis: Context Mode — MCP Sandbox for Context Saving]] |
| comparison | [[Comparison Page Standards]] | [[Cross-Domain Patterns]] |
| reference | [[Reference Page Standards]] | [[Methodology Adoption Guide]] |
| deep-dive | [[Deep-Dive Page Standards]] | [[Adoption Guide — How to Use This Wiki's Standards]] |
| lesson | [[Lesson Page Standards]] | [[CLI Tools Beat MCP for Token Efficiency]] |
| pattern | [[Pattern Page Standards]] | [[Plan-Execute-Review Cycle]] |
| decision | [[Decision Page Standards]] | [[Execution Mode Edge Cases]] |
| domain-overview | [[Domain Overview Page Standards]] | [[Cross-Domain — Domain Overview]] |
| evolution | [[Evolution Page Standards]] | [[Evolution: Methodology System]] |
| learning-path | [[Learning Path Page Standards]] | [[Learning Path: Methodology Fundamentals]] |
| operations-plan | [[Operations Plan Page Standards]] | [[Operations Plan: Wiki Post-Ingestion Validation]] |
| epic | [[Epic Page Standards]] | [[Artifact Type System]] |
| task | [[Task Page Standards]] | [[Test OpenAI backend with LocalAI]] |
| note | [[Note Page Standards]] | [[Models Are Not Documents — They Must Be Usable Systems]] |

## Domain Overviews

| Overview | Domain |
|----------|--------|
| [[AI Agents — Domain Overview]] | Agent orchestration, Claude Code, harness engineering |
| [[AI Models — Domain Overview]] | Local LLM quantization, model capabilities |
| [[Automation — Domain Overview]] | Pipelines, MCP integration, event-driven automation |
| [[Cross-Domain — Domain Overview]] | Methodology framework, quality tiers |
| [[Devops — Domain Overview]] | Stage gates, ecosystem, infrastructure patterns |
| [[Knowledge Systems — Domain Overview]] | LLM Wiki, PKM theory, evolution pipeline |
| [[Tools And Platforms — Domain Overview]] | Obsidian, NotebookLM, AICP, OpenArms |

## Pages

- [Adoption Guide — How to Use This Wiki's Standards](adoption-guide.md) — This guide explains how any project in the ecosystem (or outside it) picks up the methodology, stage-gate system, bac...
- [AI Agents — Domain Overview](domain-overviews/ai-agents-domain-overview.md) — The ai-agents domain covers the theory, patterns, and practice of building, operating, and orchestrating AI coding ag...
- [AI Models — Domain Overview](domain-overviews/ai-models-domain-overview.md) — The ai-models domain covers LLMs, embeddings, quantization, fine-tuning, and model evaluation — the foundational laye...
- [Automation — Domain Overview](domain-overviews/automation-domain-overview.md) — The automation domain covers scheduling, pipeline orchestration, workflow automation, event-driven patterns, and serv...
- [Cross-Domain — Domain Overview](domain-overviews/cross-domain-domain-overview.md) — The cross-domain area is not a subject-matter domain but a structural layer — it holds concept pages, comparisons, pa...
- [Devops — Domain Overview](domain-overviews/devops-domain-overview.md) — The devops domain covers stage-gate methodology, ecosystem topology, backlog management, task governance, infrastruct...
- [Knowledge Systems — Domain Overview](domain-overviews/knowledge-systems-domain-overview.md) — The knowledge-systems domain covers the theory and architecture of building LLM-powered knowledge bases, from Karpath...
- [Tools And Platforms — Domain Overview](domain-overviews/tools-and-platforms-domain-overview.md) — The tools-and-platforms domain covers the software tools, platforms, CLI utilities, and SaaS products used across the...
- [Evolution: Methodology System](evolution-log/methodology-evolution-history.md) — How the methodology system evolved from prose instructions to infrastructure-enforced stage gates
- [Frontmatter Field Reference — Complete Parameter Documentation](frontmatter-field-reference.md) — Complete reference for every YAML frontmatter field used in the wiki
- [Learning Path: Methodology Fundamentals](learning-paths/methodology-fundamentals.md) — Guided sequence for understanding the research wiki's methodology system — from what a methodology model IS, through ...
- [Methodology Adoption Guide](methodology-adoption-guide.md) — Step-by-step guide for any project to adopt the research wiki's methodology
- [Methodology System Map](methodology-system-map.md) — Complete map of the methodology system — every component, where it lives, what it does, and how they connect
- [Model: Automation and Pipelines](model-automation-pipelines.md) — The Automation and Pipelines model describes how this wiki transforms knowledge work from manual operations into auto...
- [Claude Code Standards — What Good Agent Configuration Looks Like](model-claude-code-standards.md) — This page defines the quality bar for CLAUDE CODE CONFIGURATION
- [Model: Claude Code](model-claude-code.md) — Claude Code is Anthropic's CLI coding agent — a tool-use loop that reads, writes, and reasons about codebases from th...
- [Model: Design.md and IaC](model-design-md.md) — The Design
- [Model: Ecosystem Architecture](model-ecosystem.md) — The Ecosystem Architecture model describes how five projects — OpenFleet, AICP, devops-control-plane, the research wi...
- [Evolution Standards — What Good Knowledge Promotion Looks Like](model-knowledge-evolution-standards.md) — This page defines the quality bar for KNOWLEDGE EVOLUTION
- [Model: Knowledge Evolution](model-knowledge-evolution.md) — The Knowledge Evolution model describes how raw sources become lessons, patterns, and decisions through a structured,...
- [LLM Wiki Standards — What Good Looks Like](model-llm-wiki-standards.md) — This page defines the quality bar for every page type in the LLM Wiki model
- [Model: LLM Wiki](model-llm-wiki.md) — The LLM Wiki model defines a knowledge system where an LLM agent maintains a structured markdown wiki — ingesting sou...
- [Model: Local AI ($0 Target)](model-local-ai.md) — The Local AI model describes the ecosystem's strategy for reducing Claude API costs toward zero by routing routine op...
- [Model: MCP and CLI Integration](model-mcp-cli-integration.md) — The MCP and CLI Integration model resolves one of the most consequential architectural decisions in LLM agent design:...
- [Methodology Standards — What Good Execution Looks Like](model-methodology-standards.md) — This page defines the quality bar for METHODOLOGY EXECUTION
- [Model: Methodology](model-methodology.md) — The Methodology model defines a flexible FRAMEWORK for defining, selecting, composing, and adapting work processes
- [Model: NotebookLM](model-notebooklm.md) — The NotebookLM model describes how Google's free, source-grounded AI research tool functions as a complementary resea...
- [Quality Standards — What Good Failure Prevention Looks Like](model-quality-failure-prevention-standards.md) — This page defines the quality bar for FAILURE PREVENTION
- [Model: Quality and Failure Prevention](model-quality-failure-prevention.md) — Quality and failure prevention for AI agents is not a set of best practices — it is a system with three enforcement l...
- [Model Registry](model-registry.md) — This is the entry point for all named models in the wiki
- [Model: Second Brain](model-second-brain.md) — The Second Brain model describes the personal knowledge management (PKM) theoretical foundation that underlies this w...
- [Model: SFIF and Architecture](model-sfif-architecture.md) — The SFIF and Architecture model describes the universal 4-stage build lifecycle (Scaffold → Foundation → Infrastructu...
- [Extension Standards — What Good Skills, Commands, and Hooks Look Like](model-skills-commands-hooks-standards.md) — This page defines the quality bar for the EXTENSION SYSTEM
- [Model: Skills, Commands, and Hooks](model-skills-commands-hooks.md) — The AI agent extension ecosystem is a four-level hierarchy: CLAUDE
- [Wiki Design Standards — What Good Styling Looks Like](model-wiki-design-standards.md) — This page defines the quality bar for VISUAL DESIGN in the wiki
- [Model: Wiki Design](model-wiki-design.md) — The Wiki Design model defines the VISUAL layer of the knowledge system — how pages look and feel, not just what they ...
- [Comparison Page Standards](standards/comparison-page-standards.md) — Standards for comparison pages — structured evaluations of alternatives across multiple criteria
- [Concept Page Standards](standards/concept-page-standards.md) — Standards for concept pages — the most common page type in the wiki (74 pages)
- [Decision Page Standards](standards/decision-page-standards.md) — Standards for decision pages — the highest-layer evolved page type (Layer 6)
- [Deep-Dive Page Standards](standards/deep-dive-page-standards.md) — Standards for deep-dive pages — extended analysis that goes significantly deeper than a concept page
- [Domain Overview Page Standards](standards/domain-overview-page-standards.md) — Standards for domain overview pages — curator pages that assess a domain's knowledge state, classify pages by maturit...
- [Epic Page Standards](standards/epic-page-standards.md) — Standards for epic pages — strategic containers that break into modules and tasks
- [Evolution Page Standards](standards/evolution-page-standards.md) — Standards for evolution pages — historical narratives tracking how a concept, system, or domain changed over time
- [Learning Path Page Standards](standards/learning-path-page-standards.md) — Standards for learning path pages — curated sequences that guide a reader through a topic in a specific order
- [Lesson Page Standards](standards/lesson-page-standards.md) — Standards for lesson pages — actionable learnings distilled from convergent evidence across multiple sources
- [Note Page Standards](standards/note-page-standards.md) — Standards for note pages — log entries recording directives, session summaries, or completion reports
- [Operations Plan Page Standards](standards/operations-plan-page-standards.md) — Standards for operations plan pages — sequential deterministic checklists that any agent can follow mechanically
- [Pattern Page Standards](standards/pattern-page-standards.md) — Standards for pattern pages — recurring structural phenomena observed across ≥2 independent instances
- [Reference Page Standards](standards/reference-page-standards.md) — Standards for reference pages — LOOKUP material that readers consult for specific answers, not read linearly
- [Source-Synthesis Page Standards](standards/source-synthesis-page-standards.md) — Standards for source-synthesis pages — processed versions of raw sources (articles, videos, papers, repos)
- [Task Page Standards](standards/task-page-standards.md) — Standards for task pages — the atomic work unit
- [Super-Model: Research Wiki as Ecosystem Intelligence Hub](super-model.md) — This is the super-model — the packaging of all 15 models, 7 standards pages, and the full knowledge architecture into...

## Tags

`standards`, `quality`, `page-type`, `exemplar`, `spine`, `model`, `methodology`, `domain-overview`, `gold-standard`, `anti-patterns`, `concept`, `ecosystem`, `skills`, `hooks`, `adoption`, `evolution`, `stage-gate`, `reference`, `context-management`, `integration`
