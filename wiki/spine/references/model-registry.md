---
title: Model Registry
aliases:
  - "Model Registry"
type: reference
domain: cross-domain
layer: spine
status: synthesized
confidence: authoritative
maturity: growing
created: 2026-04-09
updated: 2026-04-13
sources: []
tags: [models, registry, index, navigation, spine, entry-point]
---

# Model Registry

## Summary

This is the entry point for all named models in the wiki. A model is a coherent system definition — not a reading list but a real specification with standards, schemas, adoption guidance, and real examples. Each model has a companion standards page that defines what GOOD looks like for that domain. Use this page to find any model and assess its maturity.

> [!info] The Three-Layer Pattern
>
> Every model follows the same three-layer structure:

| Layer | What it defines | Example |
|-------|----------------|---------|
| **System definition** (model page) | WHAT the system IS — architecture, components, member pages, adoption | [[model-methodology|Model — Methodology]] |
| **Execution standards** (standards page) | What GOOD looks like — gold standards, anti-patterns, checklists | [[model-methodology-standards|Methodology Standards — What Good Execution Looks Like]] |
| **Visual design** | How pages LOOK — callout vocabulary, layout patterns | Covered by [[model-wiki-design-standards|Wiki Design Standards — What Good Styling Looks Like]] for all models |

## Model Catalog

| Model | Lines | Standards Page | Maturity | Domain |
|-------|-------|---------------|----------|--------|
| [[model-llm-wiki|Model — LLM Wiki]] | 444 | [[model-llm-wiki-standards|LLM Wiki Standards — What Good Looks Like]] | growing | Content structure |
| [[model-methodology|Model — Methodology]] | 568 | [[model-methodology-standards|Methodology Standards — What Good Execution Looks Like]] | growing | Work processes |
| [[model-wiki-design|Model — Wiki Design]] | 368 | [[model-wiki-design-standards|Wiki Design Standards — What Good Styling Looks Like]] | seed | Visual design |
| [[model-claude-code|Model — Claude Code]] | 494 | [[model-claude-code-standards|Claude Code Standards — What Good Agent Configuration Looks Like]] | growing | Agent runtime |
| [[model-quality-failure-prevention|Model — Quality and Failure Prevention]] | 370 | [[model-quality-failure-prevention-standards|Quality Standards — What Good Failure Prevention Looks Like]] | growing | Operational quality |
| [[model-skills-commands-hooks|Model — Skills, Commands, and Hooks]] | 349 | [[model-skills-commands-hooks-standards|Extension Standards — What Good Skills, Commands, and Hooks Look Like]] | growing | Extension system |
| [[model-knowledge-evolution|Model — Knowledge Evolution]] | 279 | [[model-knowledge-evolution-standards|Evolution Standards — What Good Knowledge Promotion Looks Like]] | growing | Evolution pipeline |
| [[model-mcp-cli-integration|Model — MCP and CLI Integration]] | 283 | — | growing | Tool integration |
| [[model-ecosystem|Model — Ecosystem Architecture]] | 293 | — | growing | Project topology |
| [[model-markdown-as-iac|Model — Markdown as IaC — Design.md and Agent Configuration]] | 261 | — | growing | Agent config patterns |
| [[model-notebooklm|Model — NotebookLM]] | 229 | — | growing | Research tooling |
| [[model-sfif-architecture|Model — SFIF and Architecture]] | 217 | — | growing | Build lifecycle |
| [[model-second-brain|Model — Second Brain]] | 226 | — | growing | PKM theory |
| [[model-local-ai|Model — Local AI ($0 Target)]] | 204 | — | growing | Cost reduction |
| [[model-automation-pipelines|Model — Automation and Pipelines]] | 202 | — | growing | Pipeline orchestration |

**Status:** 13 of 15 models elevated with standard sections (Key Pages, Lessons Learned, State of Knowledge, How to Adopt, callout styling). 2 models (Methodology, Wiki Design) use their own structure as super-model and design model respectively.

## The Super-Model

The [[model-methodology|Model — Methodology]] is the super-model — it GOVERNS how all work proceeds. Every other model operates WITHIN its framework. When starting with this wiki, read Methodology first.

## How to Use This Registry

**If you're an agent from another project:**
1. Start here. Find the model relevant to your question.
2. Read the model page for the system definition.
3. Read the standards page (if it exists) for what good looks like.
4. Follow the adoption section to apply the model to your project.

**If you're building or reviewing a model:**
1. Use the `/build-model` command or invoke the `model-builder` skill.
2. Follow the model-builder skill's workflow: Document → Design → Scaffold → Implement → Test.
3. Every model needs: Key Pages table, Lessons Learned, State of Knowledge, How to Adopt (invariant vs per-project).
4. After the model is complete, create the companion standards page.

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **Principles** | [[infrastructure-over-instructions-for-process-enforcement|Principle — Infrastructure Over Instructions for Process Enforcement]] · [[structured-context-governs-agent-behavior-more-than-content|Principle — Structured Context Governs Agent Behavior More Than Content]] · [[right-process-for-right-context-the-goldilocks-imperative|Principle — Right Process for Right Context — The Goldilocks Imperative]] |
> | **Identity** | [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]] |
> | **System map** | [[methodology-system-map|Methodology System Map]] |

## Relationships

- RELATES TO: [[model-methodology|Model — Methodology]] (the super-model)
- RELATES TO: [[model-llm-wiki|Model — LLM Wiki]] (the content structure model)
- RELATES TO: [[model-wiki-design|Model — Wiki Design]] (the visual design model)

## Backlinks

[[model-methodology|Model — Methodology]]
[[model-llm-wiki|Model — LLM Wiki]]
[[model-wiki-design|Model — Wiki Design]]
[[2026-04-09-directive-bottom-up-model-completion|Bottom-Up Model Completion — 10+ Named Models Required]]
[[2026-04-09-directive-docs-layers-old-models|Documentation Layers + Old Model Tolerance]]
[[e010-model-updates-all-15-models-reflect-current-knowledge|E010 — Model Updates — All 15 Models Reflect Current Knowledge]]
[[2026-04-09-ingest-awesome-design-md|Ingest awesome-design-md repository]]
[[2026-04-09-directive-model-quality-links-schema|Model Quality + Links + Schema Naming Issues]]
[[models-are-systems-not-documents|Models Are Systems, Not Documents]]
[[2026-04-09-directive-quality-models-hub-mindset|Quality Models — Hub Mindset — OpenArms Methodology Learnings]]
[[2026-04-09-directive-record-process-skills-supermodel|Record the Process — Skills, Super-Model, Preach by Example]]
[[2026-04-09-directive-stop-guessing-false-claims|Stop Guessing — False Claims in Models]]
[[2026-04-09-directive-styling-obsidian|Styling — Make It Look Good in Obsidian]]
[[super-model|Super-Model — Research Wiki as Ecosystem Intelligence Hub]]
[[systemic-incompleteness-is-invisible-to-validation|Systemic Incompleteness Is Invisible to Validation]]
[[2026-04-09-directive-validate-second-brain-readiness|Validate Second Brain Readiness]]
[[2026-04-09-directive-wiki-design-model-emerging|Wiki Design Model Emerging — Obsidian Styling as Standard]]
[[2026-04-09-directive-wiki-design-model-research|Wiki Design Model — Research Sources]]
