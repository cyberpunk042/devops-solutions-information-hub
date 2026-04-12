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
- [Super-Model: Research Wiki as Ecosystem Intelligence Hub](super-model.md) — This is the super-model — the packaging of all 15 models, 7 standards pages, and the full knowledge architecture into...

## Tags

`spine`, `model`, `standards`, `quality`, `gold-standard`, `methodology`, `anti-patterns`, `ecosystem`, `concept`, `skills`, `hooks`, `adoption`, `context-management`, `integration`, `second-brain`, `transferable`, `guide`, `navigation`, `framework`, `claude-code`
