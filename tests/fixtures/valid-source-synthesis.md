---
title: "Synthesis: Karpathy LLM Wiki Post"
type: source-synthesis
domain: knowledge-systems
status: synthesized
confidence: high
created: 2026-04-08
updated: 2026-04-08
sources:
  - id: src-karpathy-llm-wiki
    type: article
    url: "https://x.com/karpathy/status/example"
    title: "Karpathy on LLM Knowledge Bases"
    ingested: 2026-04-08
tags: [karpathy, llm, knowledge-base, markdown]
---

# Synthesis: Karpathy LLM Wiki Post

## Summary

Andrej Karpathy proposed using well-organized markdown files with indexes and
interlinks as knowledge bases for LLMs, instead of traditional RAG with vector
databases. The approach leverages the LLM's ability to read indexes and follow
links, producing deeper understanding than similarity-based chunk retrieval.

## Key Insights

- LLMs navigate markdown wikis by reading indexes and following links
- Explicit relationships via links produce deeper understanding than similarity search
- Scales well to hundreds of pages with good indexes
- The LLM can identify gaps and suggest new research directions
- Periodic linting keeps the wiki accurate and structured

## Relationships

- ENABLES: LLM Wiki Pattern, Agent Memory Systems
- DERIVED FROM: src-karpathy-llm-wiki
- RELATES TO: RAG Architecture, Knowledge Graph Approaches
