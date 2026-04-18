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

| # | Model | Standards Page | Maturity | Domain |
|---|-------|---------------|----------|--------|
| 1 | [[model-llm-wiki|Model — LLM Wiki]] | [[model-llm-wiki-standards|LLM Wiki Standards]] | growing | Content structure |
| 2 | [[model-methodology|Model — Methodology]] | [[model-methodology-standards|Methodology Standards]] | growing | Work processes |
| 3 | [[model-wiki-design|Model — Wiki Design]] | [[model-wiki-design-standards|Wiki Design Standards]] | growing | Visual design |
| 4 | [[model-claude-code|Model — Claude Code]] | [[model-claude-code-standards|Claude Code Standards]] | growing | Agent runtime |
| 5 | [[model-skills-commands-hooks|Model — Skills, Commands, and Hooks]] | [[model-skills-commands-hooks-standards|Extension Standards]] | growing | Extension system |
| 6 | [[model-quality-failure-prevention|Model — Quality and Failure Prevention]] | [[model-quality-failure-prevention-standards|Quality Standards]] | growing | Operational quality |
| 7 | [[model-sfif-architecture|Model — SFIF and Architecture]] | — | growing | Build lifecycle |
| 8 | [[model-knowledge-evolution|Model — Knowledge Evolution]] | [[model-knowledge-evolution-standards|Evolution Standards]] | growing | Evolution pipeline |
| 9 | [[model-mcp-cli-integration|Model — MCP and CLI Integration]] | — | growing | Tool integration |
| 10 | [[model-markdown-as-iac|Model — Markdown as IaC — Design.md and Agent Configuration]] | — | growing | Agent config patterns |
| 11 | [[model-second-brain|Model — Second Brain]] | — | growing | PKM theory |
| 12 | [[model-context-engineering|Model — Context Engineering]] | [[model-context-engineering-standards|Context Engineering Standards]] | growing | Structured context |
| 13 | [[model-ecosystem|Model — Ecosystem Architecture]] | — | growing | Project topology |
| 14 | [[model-automation-pipelines|Model — Automation and Pipelines]] | — | growing | Pipeline orchestration |
| 15 | [[model-notebooklm|Model — NotebookLM]] | — | growing | Research tooling |
| 16 | [[model-local-ai|Model — Local AI ($0 Target)]] | — | growing | Cost reduction |

**Status:** All 16 models have standard sections (Key Pages, Lessons Learned, State of Knowledge, How to Adopt). 8 have companion standards pages with annotated exemplars. All at growing maturity — promotions gated by operator.

## The Super-Model

The [[super-model|Super-Model — Research Wiki as Ecosystem Intelligence Hub]] packages all 16 models into a consumable system with 5 sub-super-models for navigation. [[model-methodology|Model — Methodology]] governs how work proceeds. [[model-llm-wiki|Model — LLM Wiki]] defines what the wiki IS. Start with either based on your need.

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
[[aicp-stage-3-hardware-unlocked-2026-04-17-—-19gb-vram-dual-g|AICP Stage 3 hardware unlocked 2026-04-17 — 19GB VRAM dual-GPU]]
[[aicp-identity-profile.md-needs-reconciliation-per-consumer-p|AICP identity-profile.md needs reconciliation per consumer-property doctrine + outdated facts]]
[[amendment-to-prior-compliance-checker-correction:-root-depth|Amendment to prior compliance-checker correction: root-depth heuristic insufficient — OpenFleet's root AGENTS.md IS at depth 0 but functions as agent-workspace template]]
[[boilerplate-skill-anti-pattern-at-scale:-47%-of-aicps-78-ski|Boilerplate skill anti-pattern at scale: 47% of AICP's 78 skills are identical instruction dumps]]
[[2026-04-09-directive-bottom-up-model-completion|Bottom-Up Model Completion — 10+ Named Models Required]]
[[compliance-checker:-agents.md-match-by-filename-regardless-o|Compliance checker: AGENTS.md match by filename regardless of role — per-agent persona files falsely satisfy Tier 2 (inverse of F1 fix)]]
[[2026-04-09-directive-docs-layers-old-models|Documentation Layers + Old Model Tolerance]]
[[e010-model-updates-all-15-models-reflect-current-knowledge|E010 — Model Updates — All 16 Models Reflect Current Knowledge]]
[[gateway-identity-parser-fragility-+-forwarder-contribute-tar|Gateway identity parser fragility + forwarder contribute-target bug (2026-04-17)]]
[[2026-04-09-ingest-awesome-design-md|Ingest awesome-design-md repository]]
[[2026-04-09-directive-model-quality-links-schema|Model Quality + Links + Schema Naming Issues]]
[[models-are-systems-not-documents|Models Are Systems, Not Documents]]
[[profile-as-coordination-bundle|Profile as Coordination Bundle]]
[[2026-04-09-directive-quality-models-hub-mindset|Quality Models — Hub Mindset — OpenArms Methodology Learnings]]
[[2026-04-09-directive-record-process-skills-supermodel|Record the Process — Skills, Super-Model, Preach by Example]]
[[2026-04-09-directive-stop-guessing-false-claims|Stop Guessing — False Claims in Models]]
[[2026-04-09-directive-styling-obsidian|Styling — Make It Look Good in Obsidian]]
[[super-model|Super-Model — Research Wiki as Ecosystem Intelligence Hub]]
[[systemic-incompleteness-is-invisible-to-validation|Systemic Incompleteness Is Invisible to Validation]]
[[three-layer-autocomplete-chain-validated-in-production-fleet|Three-layer autocomplete chain validated in production fleet operation]]
[[2026-04-09-directive-validate-second-brain-readiness|Validate Second Brain Readiness]]
[[verify-before-contributing-to-external-knowledge-systems|Verify Before Contributing to External Knowledge Systems]]
[[walkthrough-c-(openfleet)-ground-truth-verification-2026-04-|Walkthrough C (OpenFleet) ground-truth verification 2026-04-17]]
[[2026-04-09-directive-wiki-design-model-emerging|Wiki Design Model Emerging — Obsidian Styling as Standard]]
[[2026-04-09-directive-wiki-design-model-research|Wiki Design Model — Research Sources]]
