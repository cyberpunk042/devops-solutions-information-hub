---
title: Operator Decision Queue
aliases:
  - "Operator Decision Queue"
type: reference
domain: backlog
status: active
confidence: high
maturity: growing
created: 2026-04-13
updated: 2026-04-13
sources: []
tags: [backlog, decisions, operator, review, queue]
---

# Operator Decision Queue

## Summary

73 open questions across the wiki that need operator input, organized into 5 priority tiers for batch review. P1 architecture decisions unblock the most downstream work. Each question links to its source page where the full context and any existing recommendations live.

## Priority 1 — Architecture Decisions (affects multiple epics)

These shape how the system works. Deciding these unblocks downstream work.

| # | Question | Source Page | Impact |
|---|----------|------------|--------|
| ~~1~~ | ~~Should SDLC profiles be YAML configs or wiki pages?~~ **RESOLVED 2026-04-14:** YAML authoritative, wiki explains. Same pattern as methodology.yaml + model-methodology page. Renamed "SDLC chain" → "SDLC profile" (chain was a category error; chains belong to methodology layer). | [[sdlc-rules-and-structure-customizable-project-lifecycle|SDLC Rules Epic]] | Determines where profile definitions live |
| ~~2~~ | ~~Should the gateway be a separate Python module or extend pipeline.py?~~ **RESOLVED 2026-04-14:** Separate modules with audience-based separation. Pipeline = internal WRITE ops (ingest, validate, maintain). Gateway = external-facing knowledge interface (queries, flow, contribute) — also used by operator. `pipeline backlog` deprecated → `gateway query --backlog`. `status` kept in both with different audiences documented. | [[wiki-gateway-tools-unified-knowledge-interface|Gateway Epic]] | Tool architecture |
| ~~3~~ | ~~Should artifact chain config be inside methodology.yaml or separate?~~ **RESOLVED 2026-04-14:** Inside methodology.yaml — that's where chains belong (each of 9 models has its own `chain:`). Domain profiles layer CONCRETE RESOLUTION on top (paths, gate commands). Created `wiki/config/methodology-profiles/` (≥3 profiles: stage-gated, spec-driven, agile-ai, test-driven) for methodology STYLE overrides. External standards (BMAD/SDD/spec-kit/TDD) are methodology profiles, not SDLC. Added `knowledge.yaml` domain profile. Created `wiki/config/README.md` documenting all configs + 4-layer architecture. Archived `agent-directive.md` → `wiki/log/archived/` (superseded by AGENTS.md + CLAUDE.md). | [[e003-artifact-type-system-requirements|E003 Requirements]] | Config architecture |
| ~~4~~ | ~~Should domain profiles be in the wiki (authoritative) or per-project (local)?~~ **RESOLVED 2026-04-14:** Both. Everything is flexible. Wiki provides authoritative REFERENCE definitions (domain profiles, SDLC profiles, methodology profiles). Projects choose: take as-is, take and adapt, take part of it, or ignore entirely. Only mandatory layer is project-local CLAUDE.md/AGENTS.md — wiki configs are defaults to compose from, not rules to obey. This is Goldilocks applied to configuration. Documented as "The Flexibility Principle" in wiki/config/README.md. | [[methodology-standards-initiative-gaps|Standards Initiative Gaps]] | Ownership model |
| 5 | Should CLAUDE.md be split per cognitive context? | [[src-openarms-v10-enforcement|OpenArms v10 Synthesis]] | Agent config architecture |
| 6 | Should composition rules be machine-readable in methodology.yaml? | [[model-composition-rules|Model Composition Rules]] | Engine scope |
| 7 | Should methodology document types be new wiki page types? | [[e003-artifact-type-system-requirements|E003 Requirements]] | Schema scope |
| 8 | Should write-back (agent contributions) require approval or auto-merge? | [[wiki-gateway-tools-unified-knowledge-interface|Gateway Epic]] | Trust model |

## Priority 2 — Standards & Format Decisions

These define what "good" looks like. Affect all future content.

| # | Question | Source Page |
|---|----------|------------|
| 9 | Should exemplars be the BEST page or a TYPICAL good page? | [[e011-standards-exemplification-all-15-per-type-standards-with-inline-annotated-e|E011]] |
| 10 | Should the annotation format be standardized? | [[e011-standards-exemplification-all-15-per-type-standards-with-inline-annotated-e|E011]] |
| 11 | Should templates have TWO sections — structure + example? | [[e012-template-enrichment-rich-proto-programming-examples|E012]] |
| 12 | Should key methodology pages have "AI Quick Start" callout blocks? | [[ai-methodology-consumption-guide|How AI Agents Consume]] |
| 13 | Should lessons with <3 evidence items be flagged for demotion? | [[lesson-page-standards|Lesson Page Standards]] |
| 14 | Should concept pages above 300 lines be split into concept + deep-dive? | [[concept-page-standards|Concept Page Standards]] |
| 15 | Should there be a formal "styling review" gate? | [[model-wiki-design-standards|Wiki Design Standards]] |
| 16 | Should before/after examples include Obsidian screenshots? | [[model-wiki-design-standards|Wiki Design Standards]] |
| 17 | Should annotated exemplars be inline or in companion documents? | [[methodology-standards-initiative-gaps|Standards Initiative Gaps]] |

## Priority 3 — Tooling & Enforcement

How the system enforces itself.

| # | Question | Source Page |
|---|----------|------------|
| 18 | Should the gateway produce an actual OpenAPI spec? | [[global-standards-adherence|Global Standards]] |
| 19 | Should hook responses follow CloudEvents format? | [[global-standards-adherence|Global Standards]] |
| 20 | Should the MCP server expose a "methodology guide" tool? | [[ai-methodology-consumption-guide|How AI Agents Consume]] |
| 21 | Should MCP tools be 1:1 with CLI commands or aggregated? | [[e015-gateway-tools-completion-all-requirements-implemented-with-mcp-integration|E015]] |
| 22 | Should skills have a validation/quality schema? | [[model-claude-code-standards|Claude Code Standards]] |
| 23 | Should there be a "methodology health" score per project? | [[model-methodology-standards|Methodology Standards]] |
| 24 | Should there be a "quality health score" per project? | [[model-quality-failure-prevention-standards|Quality Standards]] |
| 25 | Should there be a super-model compliance checker? | [[super-model|Super-Model]] |
| 26 | What is the minimum viable enforcement for a project without a harness? | [[methodology-standards-initiative-infrastructure|Standards Initiative Infra]] |
| 27 | Should `factory-reset` be dangerous or safe? | [[e015-gateway-tools-completion-all-requirements-implemented-with-mcp-integration|E015]] |

## Priority 4 — Agent & Ecosystem

Multi-agent behavior and ecosystem integration.

| # | Question | Source Page |
|---|----------|------------|
| 28 | How do multi-agent handoff artifacts work? | [[ai-agent-artifacts|AI Agent Artifacts]] |
| 29 | Should agent persona templates be wiki page types or external config? | [[ai-agent-artifacts|AI Agent Artifacts]] |
| 30 | Should the operator's .agent/ rule system be studied as a model? | [[ai-agent-artifacts|AI Agent Artifacts]] |
| 31 | What are the "magic tricks" the operator referenced? | [[methodology-standards-initiative-honest-assessment|Honest Assessment]] |
| 32 | How should sub-agent behavioral rules be enforced? | [[src-openarms-v10-enforcement|OpenArms v10 Synthesis]] |
| 33 | Should AICP and OpenFleet have a formal integration contract? | [[model-ecosystem|Model — Ecosystem Architecture]] |
| 34 | Should wiki offer OpenFleet stage names as alternative config? | [[src-openfleet-fleet-architecture|OpenFleet Synthesis]] |
| 35 | Should we adopt Lean Startup terminology alongside our own? | [[src-sdlc-frameworks-research|SDLC Research]] |

## Priority 5 — Methodology Engine Details

Granular methodology decisions. Can be batched.

| # | Question | Source Page |
|---|----------|------------|
| 36 | How granular should domain profile overrides be? | [[e003-artifact-type-system-requirements|E003 Requirements]] |
| 37 | How do artifact chains handle composition (SFIF nesting)? | [[e003-artifact-type-system-requirements|E003 Requirements]] |
| 38 | Should artifact_class be added to artifact-types.yaml? | [[methodology-config-architecture|Config Architecture]] |
| 39 | Should methodology.yaml chain entries include template_hint? | [[methodology-config-architecture|Config Architecture]] |
| 40 | Should operations plans be a new page type or subtype? | [[methodology-standards-initiative-infrastructure|Standards Initiative Infra]] |
| 41 | Should the `module` type get required_sections in schema? | [[e003-artifact-type-system-design|E003 Design]] |
| 42 | Should methodology templates be accessible via the scaffolder? | [[e003-artifact-type-system-design|E003 Design]] |
| 43 | How many of 78 artifact types should be wiki page types? | [[methodology-artifact-taxonomy-research|Taxonomy Research]] |
| 44 | Should the taxonomy distinguish mandatory vs optional per model? | [[methodology-artifact-taxonomy-research|Taxonomy Research]] |
| 45 | Should ADR variants be separate templates or one with guidance? | [[methodology-artifact-taxonomy-research|Taxonomy Research]] |
| 46 | How many of 17 artifact types need their own standards doc? | [[methodology-standards-initiative-honest-assessment|Honest Assessment]] |
| 47 | Should existing configs be kept as-is or rewritten as framework instances? | [[methodology-standards-initiative-honest-assessment|Honest Assessment]] |
| 48 | How does methodology evolution notify consumer projects? | [[methodology-standards-initiative-gaps|Standards Initiative Gaps]] |
| 49 | Should the simplified profile have ANY stage gates? | [[sdlc-rules-and-structure-customizable-project-lifecycle|SDLC Rules Epic]] |
| 50 | Should model selection be declarative or dynamic? | [[model-methodology|Model — Methodology]] |
| 51 | Should SDLC profile selection be per-project or per-task? | [[sdlc-customization-framework|SDLC Customization]] |

## Deferred — Research Required (not operator decisions, need investigation)

These need external research or empirical data, not operator judgment.

| # | Question | Source Page | What's Needed |
|---|----------|------------|---------------|
| 52 | Can we formalize the structural grammar for context? | [[model-context-engineering|Model — Context Engineering]] | Research into markdown-as-grammar |
| 53 | Optimal context budget per tier? | [[model-context-engineering|Model — Context Engineering]] | Empirical measurement |
| 54 | When does LightRAG become necessary? | [[model-llm-wiki|Model — LLM Wiki]] | Scale testing |
| 55 | Does CMMI Level 5 map to anything we've built? | [[src-sdlc-frameworks-research|SDLC Research]] | CMMI deep dive |
| 56 | SFIF × SDLC Profile formal upgrade path? | [[model-sfif-architecture|Model — SFIF]] | Design work |
| 57 | Empirical rework rate across ingestion modes? | [[model-quality-failure-prevention|Model — Quality]] | Measurement |
| 58 | Can post-chain steps be parallelized? | [[model-automation-pipelines|Model — Automation]] | Technical analysis |
| 59 | What quality score triggers auto-filing from session hooks? | [[model-automation-pipelines|Model — Automation]] | Threshold design |
| 60-73 | (14 more research/speculative questions) | Various | Various |

## How to Use This Queue

1. **Scan by priority** — P1 decisions unblock the most downstream work
2. **Batch by theme** — several questions in the same area can be decided together
3. **Quick decisions** — many have recommendations already noted in their source pages
4. **Mark resolved** — when you decide, the source page's `[!question]` gets `~~struck~~` + `**RESOLVED:**`

## Relationships

- RELATES TO: [[second-brain-complete-system-v2-0|Milestone — Second Brain Complete System — v2.0]]
- RELATES TO: [[model-methodology|Model — Methodology]]

## Backlinks

[[second-brain-complete-system-v2-0|Milestone — Second Brain Complete System — v2.0]]
[[model-methodology|Model — Methodology]]
[[research-gaps|Research Gaps — Empirical Questions Requiring Data]]
