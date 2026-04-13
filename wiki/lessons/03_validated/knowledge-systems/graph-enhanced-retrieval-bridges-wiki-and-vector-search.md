---
title: Graph-Enhanced Retrieval Bridges Wiki Navigation and Vector Search
aliases:
  - "Graph-Enhanced Retrieval Bridges Wiki Navigation and Vector Search"
type: lesson
domain: knowledge-systems
layer: 4
status: synthesized
confidence: high
maturity: growing
created: 2026-04-08
updated: 2026-04-10
derived_from:
  - "LightRAG"
  - "LLM Wiki vs RAG"
  - "Wiki Knowledge Graph"
sources:
  - id: src-lightrag-docs
    type: documentation
    url: https://github.com/HKUDS/LightRAG
    title: LightRAG — Graph-Based RAG Framework
tags: [lightrag, graph-retrieval, hybrid-search, wiki-graph, knowledge-graph, rag, vector-search, bm25]
---

# Graph-Enhanced Retrieval Bridges Wiki Navigation and Vector Search

## Summary

The choice between wiki-style navigation and vector RAG is a false binary. LightRAG's three-stream hybrid retrieval (BM25 keyword matching, vector semantic search, and graph traversal) dissolves the either-or framing by treating the wiki's typed relationships as first-class graph edges. The wiki becomes the knowledge graph source; LightRAG becomes the query engine. What appeared to be competing paradigms are revealed as complementary layers in a single retrieval architecture.

## Context

This lesson emerges from the scale boundary of the LLM Wiki Pattern. At under 200 pages, wiki index navigation is cheaper and more accurate than vector RAG. Above 200 pages, the index no longer fits in a context window, and sequential link-following becomes slow relative to vector search. The naive response is to abandon the wiki structure for a traditional RAG pipeline — losing all the typed relationships and compounding value that made the wiki worth building. LightRAG provides a third path: retain the wiki as the authoring and structuring layer, add LightRAG as the query layer.

The context in which this lesson became concrete is OpenFleet's implementation. OpenFleet's KB (219 entries, 1,545 entities, 2,295 relationships) hit the scale boundary where flat index navigation was impractical. The solution was not to replace the KB with a vector database — it was to feed the KB's explicit `## Relationships` sections into LightRAG via `kb_sync.py`, enabling natural language queries against the same knowledge graph without changing the authoring format.

## Insight

> [!abstract] Wiki Navigation vs RAG Is a False Binary
> LightRAG's three-stream hybrid (BM25 + vector + graph traversal) dissolves the either-or framing. The wiki becomes the knowledge graph source; LightRAG becomes the query engine. Start with the wiki, add the graph query engine at the scale boundary.

The wiki's `## Relationships` sections (typed edges in ALL_CAPS verb format) are not just documentation — they are a serialized knowledge graph waiting for a query engine. Every line like `- BUILDS ON: LLM Wiki Pattern` or `- CONTRADICTS: RAG-Only Architecture` is a typed edge that carries semantic meaning beyond a plain hyperlink. This is precisely the data model that graph-enhanced retrieval systems need.

LightRAG's insight — extracted from EMNLP 2025 research — is that graph traversal catches structural connections that both keyword search and vector similarity miss. When asked "What does this system depend on?", vector search retrieves semantically similar chunks about dependencies in general; graph traversal follows `DEPENDS ON` edges from the specific entity and returns its actual dependency graph. The wiki's carefully authored relationships become high-value graph edges the moment a traversal engine can query them.

The performance difference is not marginal. The LightRAG page documents: "Agriculture domain: LightRAG 62.4% vs GraphRAG 43.6%. Legal domain: 54.3% vs 45.7%. Cost: <100 tokens + 1 API call per query vs GraphRAG's 610,000 tokens + hundreds of API calls." The graph traversal approach wins on both quality and cost compared to LLM-heavy alternatives.

The practical lesson for wiki maintainers: the way you structure wiki relationships today directly determines the quality of graph queries tomorrow. A relationship like `- RELATES TO: Something` provides minimal graph signal. A relationship like `- CONTRADICTS: RAG-Only Architecture` or `- ENABLES: [[Wiki Knowledge Graph]]` provides typed traversal paths that enable queries like "what contradicts this?" or "what does this enable?" to return precise, structured answers.

## Evidence

The LightRAG page documents OpenFleet's `kb_sync.py` bypass as the production implementation proof: "kb_sync extracts relationships from the KB's explicit `## Relationships` sections and inserts directly via REST API — zero randomness, deterministic." The bypass of LightRAG's own LLM-based entity extraction (which "produced inconsistent results: 32/0, 15/7, 21/21 entities/relations across runs") confirms that human-authored typed relationships are higher quality than LLM-extracted ones — the wiki's curation provides a quality floor that automated extraction cannot match.

The LLM Wiki vs RAG comparison matrix documents the multi-hop reasoning advantage: "Multi-hop reasoning: Excellent (wiki) — explicit typed relationship links" vs "Poor (RAG) — chunks are decontextualized." The answered question in LLM Wiki vs RAG confirms: "Typed relationship format in the wiki's ## Relationships section gives multi-hop reasoning capabilities that vector RAG cannot replicate. RAG chunks are decontextualized — they carry no edge-type semantics. The wiki's explicit typed edges let the LLM trace paths like 'what does X enable?' by following ENABLES edges."

The Wiki Knowledge Graph page documents the current state: "The wiki IS the knowledge graph source; LightRAG is the query engine." The research wiki's relationship format is directly compatible with `kb_sync.py`'s regex parser: `^([A-Z][A-Z /\-]+?):\s*(.+)$`. No format change is required to activate the LightRAG integration path.

The LLM Wiki vs RAG page articulates the migration path: "The trigger for activating the migration is when the domain sub-indexes become too large to navigate in a single context pass — estimated at 200+ pages per domain or 500+ total pages." This is an additive migration: the wiki's markdown files remain unchanged; LightRAG is added as a query layer pointing at the same relationship data.

## Applicability

This lesson applies to:

- **This wiki at scale**: When the research wiki approaches 200 pages, activate LightRAG integration using the existing `kb_sync.py` pattern from OpenFleet. The relationship format is already compatible. No wiki content changes are needed.
- **Relationship authoring practice**: Write relationships with specific typed verbs (CONTRADICTS, ENABLES, SUPERSEDES, BUILDS ON) rather than generic RELATES TO. Each specific relationship type becomes a queryable graph traversal path in LightRAG.
- **OpenFleet and AICP integration**: Both sister projects can query this wiki's knowledge via LightRAG once `kb_sync.py` is configured to point at the research wiki's manifest. The same query engine that serves OpenFleet's agent fleet can serve AICP's context assembly.
- **Any knowledge system design**: When choosing between wiki navigation and RAG, the answer is "start with the wiki, add the graph query engine at the scale boundary." The wiki gives you curation and compounding; the graph query engine gives you scale.

## Self-Check — Am I About to Make This Mistake?

> [!warning] Ask yourself:
>
> 1. **Am I using only keyword or vector search when relationship-based navigation exists?** — If the wiki has typed relationships (BUILDS ON, ENABLES, CONTRADICTS) and you are searching by keyword instead of following edges, you are ignoring the highest-quality retrieval path available.
> 2. **Am I writing generic RELATES TO relationships when a specific verb would carry more signal?** — Every `RELATES TO` is a missed opportunity for graph traversal. Could it be CONTRADICTS, ENABLES, SUPERSEDES, or BUILDS ON? Specific verbs become queryable graph edges.
> 3. **Am I treating wiki navigation and RAG as an either-or choice?** — The wiki is the authoring layer; a graph query engine is the retrieval layer. They are complementary, not competing. If you are choosing one over the other, you are accepting an unnecessary tradeoff.
> 4. **Am I at the scale boundary where index navigation breaks down?** — Under 200 pages, index navigation is cheaper and more accurate. Above 200, you need a query engine. Know which side of the boundary you are on before choosing your retrieval strategy.

### How This Connects — Navigate From Here

> [!abstract] From This Lesson → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **What principle governs this?** | [[right-process-for-right-context-the-goldilocks-imperative|Principle — Right Process for Right Context — The Goldilocks Imperative]] |
> | **How does enforcement apply?** | [[infrastructure-over-instructions-for-process-enforcement|Principle — Infrastructure Over Instructions for Process Enforcement]] |
> | **How does structure help?** | [[structured-context-governs-agent-behavior-more-than-content|Principle — Structured Context Governs Agent Behavior More Than Content]] |
> | **What is my identity profile?** | [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]] |
> | **Where does this fit in the system?** | [[methodology-system-map|Methodology System Map]] — find any component |

## Relationships

- DERIVED FROM: [[lightrag|LightRAG]]
- DERIVED FROM: [[llm-wiki-vs-rag|LLM Wiki vs RAG]]
- DERIVED FROM: [[wiki-knowledge-graph|Wiki Knowledge Graph]]
- EXTENDS: [[llm-wiki-pattern|LLM Wiki Pattern]]
- BUILDS ON: [[lightrag|LightRAG]]
- COMPARES TO: [[llm-wiki-vs-rag|LLM Wiki vs RAG]]
- FEEDS INTO: [[openfleet|OpenFleet]]
- ENABLES: Wiki Knowledge Graph

## Backlinks

[[lightrag|LightRAG]]
[[llm-wiki-vs-rag|LLM Wiki vs RAG]]
[[wiki-knowledge-graph|Wiki Knowledge Graph]]
[[llm-wiki-pattern|LLM Wiki Pattern]]
[[openfleet|OpenFleet]]
