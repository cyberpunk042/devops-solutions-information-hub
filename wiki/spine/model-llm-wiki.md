---
title: "Model Guide: LLM Wiki"
type: learning-path
domain: cross-domain
layer: spine
status: synthesized
confidence: high
maturity: growing
created: 2026-04-09
updated: 2026-04-09
sources: []
tags: [llm-wiki, model-guide, learning-path, knowledge-systems, ingestion-pipeline, knowledge-graph, maintenance, spine]
---

# Model Guide: LLM Wiki

## Summary

The LLM Wiki model describes how a markdown-file wiki maintained by an LLM outperforms static documentation on every axis that matters: it stays current, self-cross-references, surfaces contradictions, and compounds knowledge rather than letting it decay. The model covers the structural pattern (raw/ + wiki/ + index), the ingestion pipeline that turns any source into structured pages, the knowledge graph layer that makes relationships explicit, and the schema that acts as the real operational product. This is the model that this wiki itself instantiates — the knowledge here is both the documentation of the pattern and a live demonstration of it.

## Prerequisites

- Familiarity with markdown files and folder-based knowledge organization
- Some exposure to the idea of LLMs as agents (not just chatbots) helps but is not required
- No prior wiki-building experience needed — the model addresses the maintenance problem that kills every previous attempt

## Sequence

### L1 — Primary Sources

- [[Synthesis: Karpathy's LLM Wiki Idea File]] — Karpathy's original design doc; defines the three operations (Ingest, Query, Lint) and the compounding-knowledge thesis
- `wiki/sources/src-karpathy-claude-code-10x.md` — Video walkthrough; covers index-driven navigation and the "LLM as librarian" division of labor
- `wiki/sources/src-llm-wiki-v2-agentmemory.md` — The v2 extension; adds memory lifecycle, typed knowledge graph, event-driven automation, and the "schema is the real product" framing

### L2 — Core Concepts

Read in this order:

1. **LLM Wiki Pattern** ([[LLM Wiki Pattern]]) — The pattern itself: folder structure, index-driven navigation, compounding knowledge, three core operations, and the maintenance economics insight. Start here.
2. **Wiki Ingestion Pipeline** ([[Wiki Ingestion Pipeline]]) — How raw source material becomes structured wiki pages; the multi-phase workflow; source type handling; the post-chain (index → manifest → validate → lint).
3. **Wiki Knowledge Graph** ([[Wiki Knowledge Graph]]) — How relationships are extracted from `## Relationships` sections; the LightRAG integration; kb_sync.py compatibility; graph traversal vs text search.
4. **LLM Knowledge Linting** ([[LLM Knowledge Linting]]) — The lint operation; orphan detection, stale claim surfacing, contradiction flagging; how automated quality checks keep the wiki healthy without human micromanagement.
5. **Knowledge Evolution Pipeline** ([[Knowledge Evolution Pipeline]]) — The maturity ladder (seed → growing → mature → canonical); deterministic scoring; the evolution loop; human review gate at the mature → canonical transition.
6. **Memory Lifecycle Management** ([[Memory Lifecycle Management]]) — Confidence scoring, supersession, forgetting curves, and the four-tier memory model from LLM Wiki v2.

### L3 — Comparisons

- **LLM Wiki vs RAG** ([[LLM Wiki vs RAG]]) — When index-driven navigation outperforms vector search; the ~200 page boundary; hybrid approaches for larger corpora.

### L4 — Lessons (Validated Insights)

- **LLM-Maintained Wikis Outperform Static Documentation** ([[LLM-Maintained Wikis Outperform Static Documentation]]) — The core convergence lesson: maintenance economics, not intelligence, is the key differentiator.
- **Schema Is the Real Product** (`wiki/lessons/lesson-hub-—-knowledge-systems.md`) — The schema encodes domain operational knowledge; it is more durable and transferable than any individual wiki page.
- **Multi-Stage Ingestion Beats Single-Pass Processing** ([[Multi-Stage Ingestion Beats Single-Pass Processing]]) — Why a single ingest-then-done pass misses cross-references, gaps, and relationship opportunities that multi-pass catches.
- **Wiki Maintenance Problem Solved by Automation** ([[The Agent Must Practice What It Documents]]) — The historical failure mode of wikis (human abandonment) is structurally eliminated when the LLM handles all bookkeeping.

### L5 — Patterns (Structural Templates)

- **Progressive Distillation** ([[Progressive Distillation]]) — How raw source material moves through density layers (raw → seed → growing → mature → canonical); the maturity ladder as a structural template.
- **Wiki Backlog Pattern** ([[Wiki Backlog Pattern]]) — How open questions, gap analysis, and evolution candidates form a continuously prioritized work queue.

### L6 — Decisions (Resolved Choices)

- **Wiki-First with LightRAG Upgrade Path** ([[Decision: Wiki-First with LightRAG Upgrade Path]]) — Commit to markdown wiki as the operational base; add LightRAG graph traversal as scale demands it, not before.

## Outcomes

After completing this learning path you will understand:

- Why the LLM Wiki Pattern solves the specific failure mode (maintenance abandonment) that kills all previous personal wiki attempts
- The three-operation model (Ingest → Query → Lint) and how each operation compounds knowledge differently
- How the ingestion pipeline works end-to-end: source fetch → page generation → index update → validation → lint
- Why the schema document (CLAUDE.md) is the real product: it encodes all operational knowledge and is more transferable than any page
- The maturity ladder and how the evolution pipeline promotes pages from seed to canonical without premature promotion
- When to use index-driven navigation vs vector RAG, and where the practical scale boundary sits
- How this wiki itself is a live instance of everything documented here

## Relationships

- FEEDS INTO: [[Model Guide: Second Brain]]
- FEEDS INTO: [[Model Guide: Ecosystem Architecture]]
- ENABLES: [[Model Guide: Claude Code]]
- BUILDS ON: [[LLM Wiki Pattern]]
- BUILDS ON: [[Wiki Ingestion Pipeline]]
- BUILDS ON: [[Knowledge Evolution Pipeline]]
- RELATES TO: [[Model Guide: Methodology]]

## Backlinks

[[[[Model Guide: Second Brain]]]]
[[[[Model Guide: Ecosystem Architecture]]]]
[[[[Model Guide: Claude Code]]]]
[[[[LLM Wiki Pattern]]]]
[[[[Wiki Ingestion Pipeline]]]]
[[[[Knowledge Evolution Pipeline]]]]
[[[[Model Guide: Methodology]]]]
