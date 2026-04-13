---
title: Knowledge Systems — Domain Overview
aliases:
  - "Knowledge Systems — Domain Overview"
type: domain-overview
domain: knowledge-systems
layer: spine
status: synthesized
confidence: high
maturity: growing
created: 2026-04-08
updated: 2026-04-10
sources: []
tags: [domain-overview, knowledge-systems]
---

# Knowledge Systems — Domain Overview

## Summary

The knowledge-systems domain covers the theory and architecture of building LLM-powered knowledge bases, from Karpathy's original wiki pattern through graph-enhanced RAG, structured ingestion pipelines, PKM theory, and knowledge evolution. It is the intellectual foundation for this wiki's own design — the domain documents the patterns the wiki itself implements. With 11 concept pages, it is the second-largest domain. Coverage spans the LLM Wiki Pattern (the Karpathy origin), LightRAG (graph-based RAG framework used in OpenFleet), the Wiki Ingestion Pipeline (the operational workflow), Memory Lifecycle Management (knowledge validity over time), the Wiki Knowledge Graph (typed relationship extensions), the LLM Wiki vs RAG comparison, Second Brain Architecture (PKM design), PARA Methodology, Zettelkasten Methodology, Wiki Backlog Pattern, and Knowledge Evolution Pipeline. Confidence is high across the board, anchored by primary source documentation from Karpathy directly and the LightRAG EMNLP 2025 paper. This domain feeds every other domain: ai-agents use the wiki as their knowledge backbone, automation tools implement the ingestion pipeline, and tools-and-platforms provide the frontend layers (Obsidian, NotebookLM).

> [!info] Domain at a glance
>
> | Metric | Value |
> |--------|-------|
> | Concept pages | 11 |
> | Related model pages | [[model-llm-wiki|Model — LLM Wiki]], [[model-second-brain|Model — Second Brain]], [[model-knowledge-evolution|Model — Knowledge Evolution]] |
> | Decision pages | [[wiki-first-with-lightrag-upgrade-path|Decision — Wiki-First with LightRAG Upgrade Path]] |
> | Related lessons | 7+ (LLM-Maintained Wikis Outperform Static Documentation, Multi-Stage Ingestion Beats Single-Pass, Knowledge Systems Is Foundational Domain, etc.) |

## State of Knowledge

> [!abstract] The Intellectual Foundation
> This domain documents the patterns the wiki itself implements. It feeds every other domain: ai-agents use the wiki as their knowledge backbone, automation tools implement the ingestion pipeline, and tools-and-platforms provide the frontend layers (Obsidian, NotebookLM).

**Authoritative coverage:**
- LLM Wiki Pattern — primary source (Karpathy's idea file gist), two YouTube transcripts, LLM Wiki v2 extension document. The theoretical foundation is well-established. Confidence: high.
- LightRAG — sourced from the official GitHub documentation and OpenFleet's live integration. Four query modes, indexing pipeline, kb_sync bypass, OpenFleet's 1,545 entities / 2,295 relationships. Confidence: high.
- Wiki Ingestion Pipeline — three-phase workflow well documented from multiple Karpathy sources plus this project's own implementation. Confidence: high.
- Knowledge Evolution Pipeline — maturity promotion mechanics, scoring algorithm, evolution candidates, review workflow. Confidence: high.
- Second Brain Architecture — PKM theory synthesis from Forte, Karpathy, and Luhmann traditions. Confidence: high.

**Good coverage:**
- LLM Wiki vs RAG — dedicated comparison page synthesizing the two approaches with decision criteria.
- Wiki Knowledge Graph — architectural extension proposal from LLM Wiki v2. Medium confidence (proposed, not yet fully implemented in this wiki).
- PARA Methodology — Forte's four-category PKM framework with clear action orientation.
- Zettelkasten Methodology — Luhmann's atomic-note system, three core principles.
- Wiki Backlog Pattern — wiki as both knowledge base and project tracker.

**Thin coverage:**
- Memory Lifecycle Management — concept page exists but lacks implementation depth: how to implement staleness detection, which sources decay fastest, automation strategies.
- Agentic Search vs Vector Search — lives in the comparisons folder rather than here; only weakly cross-referenced.
- No coverage of vector database selection, embedding model tradeoffs, or BM25 implementation details for hybrid search.
- Obsidian graph integration with typed relationships — mentioned as a gap in Wiki Knowledge Graph but not investigated.

## Maturity Map

| Maturity | Pages |
|----------|-------|
| **growing** (all 11) | LLM Wiki Pattern, Wiki Ingestion Pipeline, LightRAG, Wiki Knowledge Graph, LLM Wiki vs RAG, Memory Lifecycle Management, Second Brain Architecture, PARA Methodology, Zettelkasten Methodology, Wiki Backlog Pattern, Knowledge Evolution Pipeline |

All pages assigned maturity. All styled with callout vocabulary. All have standard sections.

## Gaps

- **Hybrid search implementation**: BM25 + vector + graph fusion (reciprocal rank fusion) is described in Wiki Knowledge Graph but no implementation guidance exists. This is the scaling path for the wiki beyond ~200 pages.
- **Entity extraction quality**: The wiki pages describe entity extraction as a desirable ingestion step but there is no evaluation of how well Claude Code performs this task across different source types.
- **Memory lifecycle automation**: The Memory Lifecycle Management concept lacks a concrete mechanism — how should staleness be detected, what triggers a review, what does deprecation look like in practice?
- **LightRAG for this wiki**: The research wiki does not yet have its own LightRAG instance; the integration path is documented in the LightRAG page but not implemented.
- **Embedding model selection**: AICP runs bge-m3 for embeddings, LightRAG recommends bge-m3 or text-embedding-3-large, but there is no structured comparison of options with latency/quality tradeoffs.
- **Chunking strategies**: Wiki pages are already section-structured (Summary, Key Insights, Deep Analysis). How this maps to optimal chunk boundaries for RAG ingestion is unexplored.

## Priorities

1. **LightRAG integration for this wiki** — Deploy a local LightRAG instance, wire kb_sync-style export, enable natural language queries against the wiki graph
2. **Hybrid search design** — Specify BM25 + vector + graph fusion architecture as a concrete implementation plan
3. **Memory lifecycle automation** — Design the staleness detection mechanism and deprecation workflow
4. **Embedding model evaluation** — Structured comparison of bge-m3, nomic-embed, text-embedding-3-large for wiki-sized documents
5. **Entity extraction validation** — Evaluate Claude Code's entity extraction quality against structured test cases

## Key Pages

1. **[LLM Wiki Pattern](../../domains/knowledge-systems/llm-wiki-pattern.md)** — The origin. Karpathy's three-operation model (Ingest, Query, Lint) and the "Obsidian is the IDE, LLM is the programmer, wiki is the codebase" framing.
2. **[Wiki Ingestion Pipeline](../../domains/knowledge-systems/wiki-ingestion-pipeline.md)** — The operational implementation of the LLM Wiki Pattern. How raw sources become interlinked pages, including batch ingestion and entity extraction.
3. **[Knowledge Evolution Pipeline](../../domains/knowledge-systems/knowledge-evolution-pipeline.md)** — How pages promote from seed to canonical: scoring algorithm, evolution candidates, review workflow.
4. **[Second Brain Architecture](../../domains/knowledge-systems/second-brain-architecture.md)** — The PKM architecture this wiki implements: externalized thinking from Forte, Karpathy, and Luhmann.
5. **[LightRAG](../../domains/knowledge-systems/lightrag.md)** — The graph-based RAG layer that extends the wiki into a queryable knowledge graph. Production-deployed in OpenFleet.
6. **[Wiki Knowledge Graph](../../domains/knowledge-systems/wiki-knowledge-graph.md)** — The typed-relationship extension to flat wikilinks. Entity extraction, graph traversal, scaling path beyond 200 pages.

## FAQ

### Q: What is the LLM Wiki Pattern and how is it different from RAG?
The LLM Wiki Pattern (originated by Karpathy) stores synthesized knowledge in structured markdown with explicit interlinks; the LLM navigates by reading indexes and following links rather than doing similarity search. RAG embeds documents into a vector store and retrieves chunks by cosine similarity on every query. The wiki accumulates and compounds knowledge; RAG rediscovers from scratch each time. See [[llm-wiki-vs-rag|LLM Wiki vs RAG]].

### Q: At what scale should I switch from pure wiki navigation to hybrid search?
Karpathy's sources suggest pure index navigation works well up to ~200 pages (roughly 500K words). Beyond that, the index becomes too large for one-pass reading and a three-stream hybrid (BM25 + vector + graph traversal with reciprocal rank fusion) is recommended. See [[wiki-knowledge-graph|Wiki Knowledge Graph]] and [[llm-wiki-vs-rag|LLM Wiki vs RAG]].

### Q: What is LightRAG and how does it relate to the wiki?
LightRAG is a graph-based RAG framework that builds a knowledge graph from documents and uses graph traversal for multi-hop retrieval. OpenFleet uses it in production with 1,545 entities and 2,295 relationships. The wiki's ## Relationships sections are designed to be compatible with LightRAG's entity extraction. See [[lightrag|LightRAG]].

### Q: How does memory lifecycle management prevent the wiki from going stale?
Memory lifecycle uses confidence scoring and status fields (raw → synthesized → stale) to track page freshness. Periodic linting detects pages not updated recently or contradicted by newer sources. The goal is to promote durable insights to canonical status while deprecating outdated claims. See [[memory-lifecycle-management|Memory Lifecycle Management]].

### Q: What is the ingestion pipeline's three-phase model?
Phase 1 is extraction (source → summary + key insights), Phase 2 is cross-referencing (new page → existing pages → relationship mapping), Phase 3 is deepening (gap analysis → follow-up questions → next ingestion targets). The pipeline is multi-pass, not one-shot. See [[wiki-ingestion-pipeline|Wiki Ingestion Pipeline]].

## Relationships

- FEEDS INTO: AI Agents — Domain Overview
- FEEDS INTO: Automation — Domain Overview
- FEEDS INTO: Tools And Platforms — Domain Overview
- ENABLES: Cross-Domain — Domain Overview
- BUILDS ON: AI Models — Domain Overview
- RELATES TO: Devops — Domain Overview

## Backlinks

[[ai-agents-domain-overview|AI Agents — Domain Overview]]
[[automation-domain-overview|Automation — Domain Overview]]
[[tools-and-platforms-domain-overview|Tools And Platforms — Domain Overview]]
[[cross-domain-domain-overview|Cross-Domain — Domain Overview]]
[[ai-models-domain-overview|AI Models — Domain Overview]]
[[devops-domain-overview|Devops — Domain Overview]]
