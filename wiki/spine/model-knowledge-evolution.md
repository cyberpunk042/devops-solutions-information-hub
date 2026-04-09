---
title: "Model: Knowledge Evolution"
type: learning-path
domain: cross-domain
layer: spine
status: synthesized
confidence: high
maturity: growing
created: 2026-04-09
updated: 2026-04-09
sources: []
tags: [model, learning-path, spine, knowledge-evolution, maturity, progressive-distillation, wiki-lifecycle]
---

# Model: Knowledge Evolution

## Summary

The Knowledge Evolution model describes how raw sources become lessons, patterns, and decisions through a structured, automated promotion pipeline. Raw files enter as seed-maturity pages; a deterministic scorer ranks them by relationship density, cross-domain references, source count, age, and type; the prompt builder assembles generation context from wiki relationships; an LLM backend generates evolved content (lesson, pattern, or decision type); and a human review gate validates promotion to mature and canonical tiers. The pipeline is self-compounding: promoted pages add relationship edges that improve neighbor scores in subsequent runs. The outer loop — ingest → evolve → gap-analyze → research → repeat — is the wiki's steady-state improvement mechanism.

## Prerequisites

- Understanding of the wiki's page types (concept, lesson, pattern, decision) and maturity levels (seed, growing, mature, canonical)
- Familiarity with the ingestion pipeline (how raw sources become wiki pages)
- Basic understanding of graph structures (why relationship density matters for scoring)

## Sequence

### Layer 2 — Core Concepts

1. **Knowledge Evolution Pipeline** ([[Knowledge Evolution Pipeline]])
   Entry point. Explains the six deterministic scoring signals, the 8-step generation loop (SCORE → SELECT → ASSEMBLE → GENERATE → WRITE → POST-CHAIN → REVIEW → LOOP), the four maturity levels and their promotion criteria, and the three LLM backends (claude-code for session execution, openai/LocalAI for direct API, AICP for fleet integration). Key insight: the scorer is deterministic (reproducible rankings, no hallucination) while the generator is LLM-based. The pipeline's compounding property: every promoted page increases neighbor scores.

2. **Progressive Distillation** ([[Progressive Distillation]])
   The structural pattern behind the evolution pipeline. Five density layers: Layer 0 raw → Layer 1 synthesis → Layer 2 concepts → Layer 3 patterns and lessons → Layer 6 decisions. Each layer is qualitatively different from the previous (transformation, not compression). The pattern's two failure modes: premature distillation (single-source pattern pages) and distillation arrest (seeds that never get promoted). Instances: this wiki's six-layer architecture, PARA's progressive summarization, Zettelkasten's permanent notes model, NotebookLM's source → research → artifact pipeline.

### Layer 4 — Lessons

3. **Multi-Stage Ingestion Beats Single-Pass Processing** ([[Multi-Stage Ingestion Beats Single-Pass Processing]])
   The lesson that motivates the pipeline: every source should go through extract → cross-reference → gap-identification → deepening. Single-pass ingestion produces thin seed pages that score too low to evolve. The pipeline's inputs depend on the quality of what was ingested.

4. **Shallow Ingestion Is Systemic, Not Isolated** ([[Shallow Ingestion Is Systemic, Not Isolated]])
   Why one skipped quality gate degrades the entire evolution pipeline downstream: thin pages have low relationship counts, low scores, and never get promoted. The lesson is about cumulative systemic effects, not isolated page quality.

5. **Schema Is the Real Product — Not the Content** ([[Lesson: Schema Is the Real Product — Not the Content]])
   The meta-lesson: the frontmatter schema (type, domain, layer, maturity, confidence, relationships) is what makes evolution possible. Without a consistent schema, the scorer has no signals to evaluate. Schema defines the scoring surface.

6. **Graph-Enhanced Retrieval Bridges Wiki Navigation and Vector Search** ([[Graph-Enhanced Retrieval Bridges Wiki Navigation and Vector Search]])
   How LightRAG's graph-aware retrieval complements the wiki's structured navigation. Evolution-promoted pages (patterns, decisions) become high-value graph nodes that improve retrieval quality for both keyword search and semantic queries.

### Layer 6 — Decisions

7. **Decision: Wiki-First with LightRAG Upgrade Path** ([[Decision: Wiki-First with LightRAG Upgrade Path]])
   The explicit architectural decision: operate in wiki-first mode (pure structured markdown + index navigation) until approaching 200 pages, then evaluate LightRAG integration. Evolution pipeline output (dense, cross-linked patterns and decisions) is exactly the content that makes LightRAG's graph-enhanced retrieval valuable.

8. **Decision: Local Model vs Cloud API for Routine Operations** ([[Decision: Local Model vs Cloud API for Routine Operations]])
   Directly governs the evolution pipeline's backend choice. The `--backend openai` flag with LocalAI routes lower-complexity evolution tasks (seed → growing) to free local inference; `--backend claude-code` is reserved for high-complexity canonical-tier evolution.

## The Evolution Loop in Practice

```
Weekly cadence (pipeline chain review):
  1. post         → validate, manifest, lint (catch any decay since last run)
  2. review       → surface pages ready for maturity promotion
  3. gaps         → orphans, thin pages, open questions, weak domains
  4. crossref     → missing backlinks, comparison candidates, domain bridges

Then if evolution is queued:
  5. evolve --score --top 10  → rank all candidates, review the list
  6. evolve --dry-run --top 3 → preview what would be generated
  7. Execute top candidates    → generate lessons/patterns/decisions
  8. post                      → validate new evolved pages, rebuild indexes
  9. gaps                      → re-run to see what the promotions unlocked
```

## Outcomes

After completing this path you understand:

- The six deterministic scoring signals and how to interpret high vs low evolution scores
- Why the scorer must be deterministic (auditable, schedulable, immune to hallucination)
- How the prompt builder assembles context from wiki relationships (the "intelligence" of the pipeline lives here)
- The three LLM backends and when to use each (cost vs capability vs fleet integration)
- The weekly evolution cadence and how it interleaves with gap analysis and research queuing
- Why evolved pages should coexist with their source pages (marked `status: stale`, linked via `derived_from`)
- The 200-page threshold for evaluating LightRAG integration

## Relationships

- BUILDS ON: [[Knowledge Evolution Pipeline]]
- BUILDS ON: [[Progressive Distillation]]
- FEEDS INTO: [[Model: Automation + Pipelines]]
- RELATES TO: Model: Local AI ($0 Target)
- RELATES TO: [[Model: SFIF + Architecture]]
- RELATES TO: [[Model: NotebookLM]]
- ENABLES: [[Decision: Wiki-First with LightRAG Upgrade Path]]

## Backlinks

[[Knowledge Evolution Pipeline]]
[[Progressive Distillation]]
[[Model: Automation + Pipelines]]
[[Model: Local AI ($0 Target)]]
[[Model: SFIF + Architecture]]
[[Model: NotebookLM]]
[[Decision: Wiki-First with LightRAG Upgrade Path]]
[[Model: LLM Wiki]]
