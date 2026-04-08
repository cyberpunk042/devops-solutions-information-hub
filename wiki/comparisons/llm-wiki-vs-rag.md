---
title: "LLM Wiki vs RAG"
type: comparison
domain: cross-domain
status: synthesized
confidence: high
created: 2026-04-08
updated: 2026-04-08
sources:
  - id: src-karpathy-claude-code-10x
    type: youtube-transcript
    file: wiki/sources/src-karpathy-claude-code-10x.md
    title: "Andrej Karpathy Just 10x'd Everyone's Claude Code"
  - id: src-karpathy-llm-wiki-idea-file
    type: documentation
    url: "https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f"
    file: raw/articles/karpathy-llm-wiki-idea-file.md
    title: "Karpathy LLM Wiki Idea File"
  - id: src-llm-wiki-v2-agentmemory
    type: documentation
    url: "https://gist.github.com/rohitg00/2067ab416f7bbe447c1977edaaa681e2"
    file: raw/articles/llm-wiki-v2-extending-karpathys-llm-wiki-pattern-with-lessons-from-building-agen.md
    title: "LLM Wiki v2 -- Extending Karpathy's LLM Wiki Pattern with Lessons from Building Agentmemory"
tags: [llm-wiki, rag, comparison, knowledge-retrieval, hybrid-search, vector-search, knowledge-management, cross-domain]
---

# LLM Wiki vs RAG

## Summary

A direct comparison of Karpathy's LLM Wiki Pattern against traditional Retrieval-Augmented Generation (RAG). The wiki approach uses structured markdown with explicit interlinks that the LLM navigates by reading indexes and following links. Traditional RAG uses embedding models and vector similarity to retrieve chunks on every query. The wiki accumulates and compounds knowledge over time; RAG rediscovers from scratch on each query. At small to medium scale (< 200 pages), the wiki wins on simplicity, cost, and relationship quality. At enterprise scale, RAG remains necessary. LLM Wiki v2 proposes hybrid search as the bridge.

## Comparison Matrix

| Criteria | LLM Wiki Pattern | Traditional RAG | Hybrid Search (LLM Wiki v2) |
|----------|-----------------|----------------|----------------------------|
| Retrieval mechanism | Index navigation + link following | Cosine similarity over vector embeddings | BM25 + vector + graph traversal (reciprocal rank fusion) |
| Infrastructure required | None (markdown files only) | Embedding model + vector database + chunking pipeline | Full stack: files + vector DB + graph store |
| Setup time | 5 minutes (paste Karpathy's prompt) | Hours to days | Days to weeks |
| Ongoing compute cost | Tokens per query only | Embedding re-compute on content change + query inference | Both token cost and embedding maintenance |
| Scale ceiling | ~200 pages / ~500K words | Millions of documents | Designed for scaling past 200 pages |
| Knowledge accumulation | Yes — compounds over time, curated incrementally | No — retrieves and forgets on every query | Yes — wiki layer accumulates; vector layer retrieves |
| Multi-hop reasoning | Excellent — explicit typed relationship links | Poor — chunks are decontextualized | Good — graph traversal stream captures relationships |
| Maintenance model | Periodic linting + LLM-driven updates | Re-embed on change; schema migrations | Both linting and re-indexing required |
| Hallucination risk | Low (reads synthesized, curated pages) | Medium (chunk assembly may lose context) | Low (cross-stream validation reduces errors) |
| Content change tolerance | High — edit markdown, no pipeline | Low — re-embedding required on every change | Medium — markdown edits cheap; vector re-index periodic |
| Best for | Personal KB, team wikis, < 200 curated pages | Large document archives, enterprise search | Mature wikis scaling beyond 200 pages |

## Key Insights

- The LLM Wiki pattern requires zero infrastructure beyond markdown files; RAG requires an embedding model, vector store, and chunking pipeline
- Karpathy explicitly names NotebookLM, ChatGPT file uploads, and "most RAG systems" as the "retrieve-and-forget" anti-pattern — the wiki compiles knowledge once and keeps it current rather than re-deriving on every query
- The wiki's explicit typed relationships (## Relationships section) enable multi-hop reasoning that RAG cannot replicate — RAG returns isolated chunks, the wiki lets the LLM trace a path across connected concepts
- The scale boundary is approximately 200 pages / 500K words: below this, wiki navigation is cheaper and more accurate; above this, vector search is necessary
- LLM Wiki v2 dissolves the binary choice: embed RAG as one stream in a three-stream hybrid (BM25 + vector + graph) with reciprocal rank fusion

## Deep Analysis

### Decision Criteria

Choose the **LLM Wiki Pattern** when:
- Your knowledge base is < 200 pages and actively curated
- You need multi-hop reasoning across related concepts
- Infrastructure budget is zero (personal project, small team)
- Content changes frequently (wiki maintenance is just editing files; no re-indexing)

Choose **Traditional RAG** when:
- You have millions of documents that cannot be curated manually
- Your query patterns are primarily single-hop factual retrieval
- You have existing infrastructure for embedding model serving
- Users are non-technical and cannot maintain a structured wiki

Choose **Hybrid Search** when:
- Your wiki is approaching or exceeding 200 pages
- You need both structural reasoning (wiki nav) and broad recall (vector search)
- You have the infrastructure budget for a vector store alongside the wiki
- Long-term scaling is a requirement

### Can the wiki index be used as a first-pass vector search target?

Cross-referencing the Wiki Ingestion Pipeline page: the ingestion pipeline already produces a structured index of all pages with titles, types, domains, and relationship summaries. This index is exactly the kind of compact, semantically dense document that embeds well. The LLM Wiki v2 architecture proposes hybrid search as "BM25 + vector + graph traversal with reciprocal rank fusion" — which means the wiki index (BM25/vector pass) plus link-following (graph traversal pass) is precisely the described architecture. The index file is small enough to embed cheaply and would serve as a first-pass filter before the LLM follows specific page links. This is technically feasible with existing wiki structure today.

### Karpathy's NotebookLM critique vs. NotebookLM's per-query accuracy

Cross-referencing the Second Brain Architecture page and the Claude Code Accuracy Tips source: these are not in conflict — they target different goals. Karpathy's critique is about **knowledge compounding**: NotebookLM, like most RAG systems, retrieves answers per-query without accumulating a persistent, structured knowledge graph. The wiki accumulates; NotebookLM re-derives. The NotebookLM accuracy advantage is about **per-query grounding quality**: for a single factual question, NotebookLM's grounding in 250-300 source documents produces fewer hallucinations than a local RAG system with a smaller or lower-quality index. The distinction maps directly onto the comparison matrix: "knowledge accumulation = Yes (wiki) vs No (RAG/NotebookLM)" and "hallucination risk = Low (wiki) vs Medium (RAG)." The Claude Code Accuracy Tips source actually recommends using NotebookLM as an *external knowledge base complement* to the wiki — storing research sources in NotebookLM for per-query accuracy while the wiki accumulates synthesized patterns. These are complementary layers, not competing approaches.

### At what scale does wiki navigation token cost exceed RAG infrastructure cost?

Cross-referencing the LLM Wiki Pattern and Knowledge Evolution Pipeline pages: the boundary is not purely about page count — it is about query frequency and context window size. The LLM Wiki Pattern page documents the scale ceiling as ~200 pages / ~500K words for index-only navigation. Beyond that, the index itself becomes too large to fit in a context window in a single pass, requiring either hierarchical sub-indexes or vector search as a pre-filter. The Knowledge Evolution Pipeline adds a relevant data point: as a wiki matures, each evolved canonical page is denser and more interlinked, meaning 200 mature pages may have higher effective information density than 200 seed pages. The practical answer from existing wiki knowledge: the token cost of navigation scales with O(pages read per query × turns per session), while RAG infrastructure cost is roughly fixed (embedding model hosting + vector DB). For a personal wiki queried a few times per day, wiki navigation remains cheaper well past 200 pages. For high-frequency automated querying (e.g., an agent reading the wiki on every task), RAG amortizes faster.

## Open Questions

- Has hybrid search been empirically benchmarked against pure wiki navigation at the 200-500 page transition zone? (Requires: empirical testing or external research; the wiki only documents the theoretical boundary at ~200 pages)
- Can the wiki index itself be embedded and searched via vectors as a first pass, with link-following as a second pass? (Partially answered above from existing knowledge; implementation details require external research on embedding pipeline setup)
- At what scale does the token cost of wiki navigation exceed the infrastructure cost of a RAG pipeline? (Partially answered above; precise crossover point requires empirical measurement with real query frequency data)

## Relationships

- COMPARES TO: LLM Wiki Pattern
- EXTENDS: Agentic Search vs Vector Search
- RELATES TO: Wiki Knowledge Graph
- RELATES TO: Wiki Ingestion Pipeline
- RELATES TO: LightRAG
- RELATES TO: Memory Lifecycle Management
- RELATES TO: NotebookLM

## Backlinks

[[LLM Wiki Pattern]]
[[Agentic Search vs Vector Search]]
[[Wiki Knowledge Graph]]
[[Wiki Ingestion Pipeline]]
[[LightRAG]]
[[Memory Lifecycle Management]]
[[NotebookLM]]
[[Claude Code Best Practices]]
[[Knowledge Evolution Pipeline]]
[[LLM-Maintained Wikis Outperform Static Documentation]]
[[Second Brain Architecture]]
[[Synthesis: Karpathy LLM Wiki Method via Claude Code]]
[[Synthesis: Karpathy's LLM Wiki Idea File]]
[[Synthesis: LLM Wiki v2 -- Extending Karpathy's Pattern with Agentmemory Lessons]]
[[Synthesis: NotebookLM + Claude Code Workflow via notebooklm-py]]
