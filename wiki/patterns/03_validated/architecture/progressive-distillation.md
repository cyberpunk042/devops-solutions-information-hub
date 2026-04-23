---
title: Progressive Distillation
aliases:
  - "Progressive Distillation"
type: pattern
domain: knowledge-systems
layer: 5
status: synthesized
confidence: high
maturity: growing
derived_from:
  - "Second Brain Architecture"
  - "Knowledge Evolution Pipeline"
instances:
  - {'page': 'Knowledge Evolution Pipeline', 'context': 'Six-layer wiki architecture (raw → seed → growing → mature → canonical) with deterministic scoring engine that promotes pages through maturity layers.'}
  - {'page': 'Second Brain Architecture', 'context': 'PARA progressive summarization (raw → highlights → bold → summary) and Zettelkasten note lifecycle (fleeting → literature → permanent) both instantiate the pattern.'}
  - {'page': 'NotebookLM', 'context': 'Source → research → artifact pipeline: raw source files loaded into notebook, synthesized into grounded research, then generated as 10 artifact types.'}
  - {'page': 'Research Wiki', 'context': 'The wiki itself: raw/ → sources/ → domains/ → lessons/ → patterns/ → decisions/. Six layers, each qualitatively different from the previous.'}
created: 2026-04-08
updated: 2026-04-10
last_reviewed: 2026-04-22
sources:
  - id: src-second-brain-research
    type: article
    file: raw/articles/second-brain-pkm-research.md
    title: Second Brain / PKM Research
  - id: src-zettelkasten-basb
    type: article
    url: https://zettelkasten.de/posts/building-a-second-brain-and-zettelkasten/
    title: Combining Zettelkasten and Building a Second Brain
  - id: src-pipeline-tooling
    type: documentation
    file: tools/pipeline.py
    title: Wiki Pipeline Tool — evolve command
tags: [progressive-distillation, knowledge-systems, maturity, zettelkasten, para, synthesis, second-brain, evolution, density, distillation]
---

# Progressive Distillation

## Summary

Progressive Distillation is the pattern of processing raw material through successive layers of increasing density and actionability — each pass producing a smaller, more synthesized artifact that captures more value per unit than the layer below it. The pattern recurs across knowledge management, content pipelines, and AI agent systems wherever the challenge is converting high-volume input into durable, actionable knowledge. ==Its defining characteristic: each layer is qualitatively different from the previous, not merely shorter. Distillation is not compression — it is transformation.==

## Pattern Description

Progressive distillation is recognizable by three structural properties:

> [!abstract] **The three properties**
> 1. **Multiple distinct layers** with defined transitions between them
> 2. **Increasing density and actionability** at each layer — the top is smaller in volume but higher in value per unit
> 3. **Explicit promotion criteria** governing when material moves between layers — systems that simply accumulate are not distillation systems

### The Layer Model

> [!info] **Five distillation layers from raw to actionable**
> | Layer | Name | Volume | Density | What it contains | Wiki directory |
> |-------|------|--------|---------|-----------------|----------------|
> | 0 | **Raw** | High | Low | Unprocessed source material. Articles, transcripts, dumps. | `raw/` |
> | 1 | **Synthesis** | Medium | Medium | Structured summaries of individual sources. Key insights extracted, relationships identified. | `wiki/sources/` |
> | 2 | **Concepts** | Lower | Higher | Cross-source synthesis. Ideas abstracted from sources, domain-indexed, linked. | `wiki/domains/` |
> | 3-4 | **Lessons & Patterns** | Small | High | Cross-domain distillation. Recurring structures from multiple instances. | `wiki/lessons/`, `wiki/patterns/` |
> | 5 | **Decisions** | Minimal | Maximal | Actionable distillates. Choices with rationale, alternatives, reversibility. | `wiki/decisions/` |

The value compounds at each layer: a well-distilled decision page is denser in actionable knowledge than any number of raw sources covering the same territory. But upper layers depend on lower layers for validity — a pattern without documented instances is speculation, not distillation.

### The Promotion Mechanism

> [!tip] **What moves material between layers**
> Each transition requires specific evidence that the material has been TRANSFORMED, not just reformatted:
> - **Raw → Synthesis**: source has been read in full, key claims extracted with citations, relationships to existing pages identified
> - **Synthesis → Concept**: multiple sources converge on the same idea, cross-source integration produces understanding no single source contained
> - **Concept → Lesson/Pattern**: concrete instances identified across 2+ independent contexts, the principle is generalizable beyond its origin
> - **Lesson/Pattern → Decision**: the insight has been applied to a concrete choice context with alternatives evaluated and reversibility assessed

> [!warning] **Where distillation systems fail**
> The promotion transition is the bottleneck. PARA requires human re-reading at each pass. Zettelkasten requires deliberate writing in one's own voice. Traditional wikis degrade because distillation cost grows faster than available attention.
>
> The evolution pipeline's insight: **deterministic scoring automates candidate identification** — removing the human attention bottleneck from the promotion SIGNAL while preserving human judgment at the review GATE. The scorer finds what's ready; the human confirms it's worthy.

### Two Failure Modes

> [!bug]- **Premature distillation**
> Material promoted to a higher layer before it has enough instances, cross-references, or source diversity to support the generalization. A single-source pattern page encodes one example as a universal principle without the multi-instance evidence that makes it trustworthy.
>
> **How the scorer prevents this:** age, source count, and cross-domain reference signals require minimum thresholds before promotion eligibility. A page that's new, single-sourced, and domain-local won't score high enough to be considered.

> [!bug]- **Distillation arrest**
> Material accumulates at lower layers and is never promoted. The wiki grows in raw and synthesis pages but never develops patterns, lessons, or decisions. The value is there — the page is cited, cross-linked, multi-sourced — but locked in seed format.
>
> **How the tooling prevents this:** `pipeline evolve --review` surfaces pages in growing maturity with scores above the promotion threshold that haven't been acted on. Gap analysis identifies domains with concepts but no lessons. The weekly review cadence catches arrested pages.

### What Distillation Looks Like — Before and After

> [!example]- **Before: concept page (Layer 2) — thin, single-perspective**
> A page titled "CLI Tools and Token Efficiency" with a summary saying "CLI tools are more efficient than MCP for token usage" and a Key Insights section listing 3 bullet points from one source. No mechanism explanation. No measured data. No applicability boundaries.
>
> This is a concept page that DESCRIBES a claim. It is not distilled — it is restated.

> [!example]- **After: lesson page (Layer 4) — distilled, multi-source, actionable**
> [[cli-tools-beat-mcp-for-token-efficiency|CLI Tools Beat MCP for Token Efficiency]] (122 lines): Summary states the lesson in one actionable sentence. Context lists 5 specific trigger conditions. Insight explains the MECHANISM (schema tokens displacing task context — "context pollution"). Evidence has 8 discrete items from 4 independent sources with data ("12x cost differential", "98% reduction", "3x more features"). Applicability names 4 domains + 4 counterexamples. CONTRADICTS relationship challenges the default assumption.
>
> This is a lesson that TEACHES a principle. The transformation from concept to lesson added: mechanism explanation (WHY not just WHAT), convergent evidence (4 sources not 1), measured data (12x, not "more efficient"), honest boundaries (when MCP still wins), and actionability (the reader can DECIDE after reading).

> [!tip] **The distillation test**
> Remove the upper-layer page. Does the wiki lose insight that wasn't on the lower-layer pages? If yes — real distillation occurred. If the lesson page just restates the concept page in different words, the promotion was premature.

---

## Instances

### This Wiki's Six-Layer Architecture

The most complete instantiation. The evolution pipeline (`pipeline evolve`) is the mechanical promotion mechanism. The `--score` flag ranks pages by 6 deterministic signals. The `--review` flag surfaces ready-for-promotion pages. The compounding property: promoted pages link back to source concepts, increasing those concepts' scores in subsequent runs.

> [!info] **Six scoring signals that measure distillation readiness**
> | Signal | What it measures | Why it indicates readiness |
> |--------|-----------------|--------------------------|
> | Cross-source convergence | How many distinct sources back the page | Multi-source = ready for cross-source synthesis |
> | Relationship hub | How many pages reference or are referenced by it | High connectivity = junction point worth distilling |
> | Domain layer gap | Missing layers in the page's domain | Domains with concepts but no lessons = distillation arrested |
> | Open question density | How many unresolved questions | Questions = evolution directions |
> | Tag co-occurrence | Shared tags with existing evolved pages | Related evolution opportunity |
> | Orphaned references | Relationship targets that don't exist | Missing pages = distillation candidates |

### PARA's Progressive Summarization

Tiago Forte's method implements the same pattern manually. CODE workflow: Capture → Organize → Distill → Express. Progressive summarization is the distillation mechanism: first pass highlights, second pass bolds the critical highlights, third pass writes an executive summary. Each pass produces a denser artifact.

> [!warning] **PARA's weakness is distillation arrest**
> The method requires human attention for each pass. Material that's never revisited never gets distilled. The wiki's automated pipeline solves this by replacing human-initiated re-reads with scoring-triggered promotion.

The wiki maps PARA directly: `## Summary` (executive summary) → `## Key Insights` (bold highlights) → `## Deep Analysis` (full passage) — three density layers in one page schema.

### Zettelkasten's Permanent Notes

Luhmann's system implements distillation across three note types: fleeting (raw capture), literature (source summary in own words), permanent (one idea per note, linked to existing notes). The promotion criterion is explicit: does this idea warrant its own card, stated in my own voice, linked to the existing network?

> [!tip] **The Zettelkasten insight the wiki adopts**
> A note's value is its position in the network, not its content in isolation. The evolution scorer's relationship count signal implements this directly: pages with more relationships are better promotion candidates because they sit at network junctions where distillation produces high-value cross-domain synthesis.

### NotebookLM's Source → Research → Artifact Pipeline

Three-layer distillation in a content generation context: raw sources (uploaded docs) → grounded research (Q&A bounded to sources) → generated artifacts (slides, podcasts, reports). The source grounding property ensures the artifact layer doesn't drift from raw material — same principle as the wiki's `derived_from` frontmatter field.

---

## When To Apply

- **Volume exceeds direct processability** — distillation creates intermediate stopping points where high-value material gets extracted even if raw volume grows indefinitely
- **Knowledge must compound over time** — without distillation, each source is processed in isolation and insights are lost when the session closes
- **Actionability is the terminal goal** — the decision layer is what makes the chain produce operational value. Systems that stop at concepts produce intellectually interesting but operationally inert knowledge.
- **Quality must be validated at each transition** — promotion criteria are quality gates. Each filters out poorly-supported generalizations before they reach actionable status.
- **The process must be maintainable at scale** — automated promotion (scoring, pipeline) removes the human attention bottleneck that causes traditional wikis to stall

## When Not To

- **Speed over depth** — rapid content generation (same-day blog posts, quick docs) doesn't benefit from multi-layer promotion overhead
- **Small, stable source set** — <20 pages, single domain: a flat wiki with one synthesis layer is sufficient. Patterns emerge from observation, not formal mechanics.
- **Ephemeral sources** — news feeds, real-time alerts, transient data don't warrant promotion to permanent layers
- **Promotion criteria can't be defined** — if "what makes a concept worth promoting to a pattern" has no clear answer, layers will either stall (arrest) or produce premature promotions. Define criteria BEFORE building infrastructure.
- **Raw layer never cleaned** — systems that grow raw/ without processing develop "raw debt" — accumulated unprocessed material creating false scale with no distillation value

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **What principle governs this?** | [[right-process-for-right-context-the-goldilocks-imperative|Principle — Right Process for Right Context — The Goldilocks Imperative]] |
> | **How does enforcement apply?** | [[infrastructure-over-instructions-for-process-enforcement|Principle — Infrastructure Over Instructions for Process Enforcement]] |
> | **What is my identity profile?** | [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]] |
> | **Where does this fit?** | [[methodology-system-map|Methodology System Map]] |

## Relationships

- DERIVED FROM: [[second-brain-architecture|Second Brain Architecture]]
- DERIVED FROM: [[knowledge-evolution-pipeline|Knowledge Evolution Pipeline]]
- IMPLEMENTS: [[memory-lifecycle-management|Memory Lifecycle Management]]
- RELATES TO: [[para-methodology|PARA Methodology]]
- RELATES TO: [[zettelkasten-methodology|Zettelkasten Methodology]]
- ENABLES: [[knowledge-evolution-pipeline|Knowledge Evolution Pipeline]]
- RELATES TO: [[llm-wiki-pattern|LLM Wiki Pattern]]
- FEEDS INTO: [[wiki-knowledge-graph|Wiki Knowledge Graph]]
- RELATES TO: [[notebooklm|NotebookLM]]
- BUILDS ON: [[multi-stage-ingestion-beats-single-pass|Multi-Stage Ingestion Beats Single-Pass Processing]]

## Backlinks

[[second-brain-architecture|Second Brain Architecture]]
[[knowledge-evolution-pipeline|Knowledge Evolution Pipeline]]
[[memory-lifecycle-management|Memory Lifecycle Management]]
[[para-methodology|PARA Methodology]]
[[zettelkasten-methodology|Zettelkasten Methodology]]
[[llm-wiki-pattern|LLM Wiki Pattern]]
[[wiki-knowledge-graph|Wiki Knowledge Graph]]
[[notebooklm|NotebookLM]]
[[multi-stage-ingestion-beats-single-pass|Multi-Stage Ingestion Beats Single-Pass Processing]]
[[methodology-framework|Methodology Framework]]
[[model-knowledge-evolution|Model — Knowledge Evolution]]
[[model-sfif-architecture|Model — SFIF and Architecture]]
[[model-second-brain|Model — Second Brain]]
[[scaffold-foundation-infrastructure-features|Scaffold → Foundation → Infrastructure → Features]]
[[skyscraper-pyramid-mountain|Skyscraper, Pyramid, Mountain]]
[[wiki-backlog-pattern|Wiki Backlog Pattern]]
