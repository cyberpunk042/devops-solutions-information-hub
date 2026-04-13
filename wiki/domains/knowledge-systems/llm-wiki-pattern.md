---
title: "LLM Wiki Pattern"
type: concept
layer: 2
maturity: growing
domain: knowledge-systems
status: synthesized
confidence: high
created: 2026-04-08
updated: 2026-04-10
sources:
  - id: src-karpathy-claude-code-10x
    type: youtube-transcript
    file: raw/transcripts/karpathy-claude-code-10x.txt
    title: "Andrej Karpathy Just 10x'd Everyone's Claude Code"
    ingested: 2026-04-08
  - id: src-karpathy-llm-wiki-idea-file
    type: documentation
    url: "https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f"
    file: raw/articles/karpathy-llm-wiki-idea-file.md
    title: "Karpathy LLM Wiki Idea File"
    ingested: 2026-04-08
  - id: src-llm-wiki-v2-agentmemory
    type: documentation
    url: "https://gist.github.com/rohitg00/2067ab416f7bbe447c1977edaaa681e2"
    file: raw/articles/llm-wiki-v2-extending-karpathys-llm-wiki-pattern-with-lessons-from-building-agen.md
    title: "LLM Wiki v2 -- Extending Karpathy's LLM Wiki Pattern with Lessons from Building Agentmemory"
    ingested: 2026-04-08
tags: [llm-wiki, knowledge-base, markdown, karpathy, second-brain, index-files, memex, schema, compounding-knowledge]
---

# LLM Wiki Pattern

## Summary

The LLM Wiki Pattern is Andrej Karpathy's approach to building personal knowledge bases using LLMs and plain markdown files. Rather than relying on vector databases and embedding pipelines, you maintain a structured folder of markdown files with indexes and interlinks that an LLM can read, navigate, and maintain. The LLM ingests raw source documents, autonomously creates wiki pages with summaries and relationship links, and maintains a master index. Knowledge compounds over time — unlike ephemeral chat conversations — while keeping infrastructure as simple as a folder of text files. The core philosophical insight: "Humans abandon wikis because the maintenance burden grows faster than the value. LLMs don't get bored. The wiki stays maintained because the cost of maintenance is near zero."

> [!info] Pattern Architecture Reference Card
>
> | Component | What It Is | Role |
> |-----------|-----------|------|
> | `raw/` | Source material (any format) | Input layer — provenance preserved permanently |
> | `wiki/` | LLM-generated structured pages | Knowledge layer — compounds over time |
> | `index.md` | Master navigation to all pages | Replaces vector search with structural navigation |
> | `_index.md` (per domain) | Domain-level navigation | Scalable sub-indexes for hierarchical browsing |
> | `CLAUDE.md` | Schema + instructions for the LLM | "The most important file" — co-evolved, not static |
> | `log.md` | Operation history | Audit trail for all wiki changes |
>
> **Three core operations:** Ingest (process source → 10-15 pages), Query (search → synthesize → file answer back as new page), Lint (health checks for contradictions, stale claims, orphans).

## Key Insights

### The Compounding Principle

> [!tip] Knowledge compounds — the wiki is a persistent artifact, not an ephemeral chat
> Normal AI conversations are ephemeral — context vanishes after the session. The wiki pattern makes knowledge persist and accumulate. Each new source enriches the existing graph of relationships. Critically, when a query produces a valuable comparison or connection, it gets filed back as a new wiki page: "Your explorations compound just like ingested sources do." This is the key feedback loop that distinguishes the pattern from a simple document store.

**Automatic relationship discovery.** When processing a source, the LLM doesn't create a single page — it may produce 5, 10, or 25 pages depending on content density, automatically discovering cross-links between them. The wiki grows denser and more interconnected with each ingestion without manual curation.

**Token efficiency through structure.** Converting scattered files into a structured wiki reduces token consumption dramatically. One user reported 95% token reduction after migrating 383 files into the wiki format. The structure IS the optimization — indexes eliminate the need to load everything into context.

### The Human-AI Division of Labor

> [!abstract] "The human curates sources and thinks about what it all means. The LLM does everything else."
> Karpathy's division: human as curator, LLM as librarian. "Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase." Three independent sources converge on the same boundary: (1) Karpathy's "librarian vs curator", (2) Harness Engineering's 5-verb workflow where humans approve Plan before Work, (3) the Knowledge Evolution Pipeline's `--review` flag as the explicit human gate at growing → mature.

### The Schema Is the Real Product

> [!warning] CLAUDE.md is "the most important file in the system"
> The schema document is not static configuration — it is something "you and the LLM co-evolve over time as you figure out what works for your domain." The LLM Wiki v2 extends this further: the schema encodes entity types, ingestion workflows, quality standards, and contradiction handling. It is transferable domain operational knowledge — more valuable than any individual page because it governs how ALL pages are created.

### Architecture and Scale

**Index-driven navigation replaces similarity search.** The LLM maintains index files with links to every concept, tool, and source. This replaces RAG's vector similarity search with explicit structural navigation. Karpathy confirms: "works surprisingly well at moderate scale (~100 sources, ~hundreds of pages)."

**Customizable and multi-vault.** Karpathy left the prompt intentionally vague for adaptation. Flat files or domain subfolders. Separate vaults for different purposes (research, personal) connected to different agents.

**Broad use cases.** Personal (goals, health), Research (papers with evolving thesis), Reading ("think fan wikis like Tolkien Gateway"), Business/team (Slack threads, meeting transcripts), and more (competitive analysis, due diligence, trip planning, course notes).

> [!abstract] Memex lineage
> Karpathy connects the pattern to Vannevar Bush's 1945 Memex — "private, actively curated, with the connections between documents as valuable as the documents themselves. The part he couldn't solve was who does the maintenance. The LLM handles that."

## Deep Analysis

The LLM Wiki Pattern represents a shift in how we think about AI knowledge management. Traditional approaches treat the knowledge retrieval problem as a search problem — embed everything into vectors, find nearest neighbors. Karpathy's insight: at small to medium scale (up to hundreds of pages, ~500K words), a well-organized set of markdown files with explicit indexes is both simpler and more effective.

The pattern works because modern LLMs with large context windows can read an index, identify relevant pages, follow links, and synthesize with full contextual understanding. This is fundamentally different from vector similarity search, which retrieves chunks based on surface semantics without understanding structural relationships between documents.

The architecture is self-improving: each ingestion updates indexes, creates cross-references, and may restructure existing pages. The wiki becomes denser and more interconnected without manual curation beyond feeding raw sources.

A practical advantage is radical simplicity. No databases, no embedding models, no infrastructure. Just files on disk — version-controlled with Git, synced with any tool, referenced from any Claude Code project via CLAUDE.md. "The wiki is just a git repo of markdown files. You get version history, branching, and collaboration for free."

> [!warning] Scale limitation
> At hundreds of pages the pattern works well. At millions of documents, indexes become too large for context and sequential link-following becomes slow compared to vector search. The v2 document identifies the boundary at ~100-200 pages for index-only navigation and proposes hybrid search (BM25 + vector + graph traversal). For enterprise-scale, traditional RAG or knowledge graph solutions may be necessary.

### Evolution: LLM Wiki v2 Extensions

> [!info] Maturation path from personal tool to production system
>
> | Extension | What It Adds | Impact |
> |-----------|-------------|--------|
> | Memory lifecycle | Confidence scoring, supersession, forgetting (Ebbinghaus), 4-tier consolidation | Flat store → probabilistic model |
> | Typed knowledge graph | Entity extraction, typed relationships ("uses", "contradicts") | Text search → graph traversal |
> | Event-driven automation | Hooks (on-new-source, on-session-end, on-query, on-schedule) | Manual operations → automated bookkeeping |
> | Self-healing lint | Auto-fix orphans, stale claims, broken cross-refs, contradiction resolution | Flagging → self-correcting |
> | Schema as product | Schema encodes transferable domain operational knowledge | Configuration → the real product |
>
> Implementation spectrum: start with minimal viable wiki (Karpathy's original), progressively add lifecycle, structure, automation, scale, and collaboration.

### This Wiki as Practitioner Instance

> [!example]- How this wiki implements the LLM Wiki Pattern
>
> | Pattern Component | This Wiki's Implementation |
> |-------------------|---------------------------|
> | Raw sources | `raw/` with articles, transcripts, notes, dumps (70 files) |
> | Structured pages | `wiki/` with 175 pages across 10 domains |
> | Index navigation | Hierarchical: `wiki/index.md` + per-domain `_index.md` |
> | Schema co-evolution | CLAUDE.md at ~230 lines, evolved from simple instructions to full routing table |
> | Three operations | `pipeline post` (ingest chain), MCP wiki_search (query), `tools/lint.py` (lint) |
> | Compounding queries | Answered Open Questions filed back as page content |
> | v2 extensions | Maturity lifecycle (seed→canonical), typed relationships (15 verbs), event-driven pipeline chains, self-healing obsidian.py |
> | Git as infrastructure | Full version history, ~95 commits, branching for features |
> | Scale approach | 175 pages (well within index-only range), LightRAG upgrade path documented |

## Open Questions

- At what exact scale does the wiki pattern start to degrade compared to vector-based RAG? Is the boundary sharp or gradual? (The v2 document suggests ~100-200 pages for index-only; the LLM Wiki vs RAG comparison page documents ~200 pages / ~500K words as the practical ceiling. Requires: empirical benchmarking to confirm whether degradation is sharp or gradual.)
- Can the wiki structure be automatically migrated to a graph database or RAG pipeline when scale demands it, preserving the relationships? (Requires: external research on graph DB migration tooling; the wiki documents the hybrid search destination but not the migration path.)
- Is there a recommended approach for merging multiple single-user wikis into a shared team wiki? (The v2 document proposes mesh sync with last-write-wins, but details are sparse. Requires: external research or implementation experience.)

## Answered Questions

> [!example]- How does the pattern handle conflicting sources?
> The Knowledge Evolution Pipeline implements a maturity ladder (seed → growing → mature → canonical) where each promotion requires multi-source synthesis. When sources conflict, the scorer favors higher source counts and cross-domain references — the more corroborated claim accumulates more relationships. The `--review` flag surfaces candidates for human inspection before mature → canonical promotion. The v2 document proposes automated contradiction resolution; this wiki handles it through promotion gates and human review.

> [!example]- Optimal index granularity — master or hierarchical?
> This wiki uses hierarchical sub-indexes: each domain folder has `_index.md`, and a master `wiki/index.md` serves as top-level navigation. The ingestion pipeline automatically maintains both levels as part of the `post` chain. Hierarchical is correct because the master index becomes too large for single-pass navigation beyond ~50 pages, while domain indexes remain scannable at all scales this wiki will reach.

> [!example]- How does CLAUDE.md evolve in practice?
> This wiki's schema has evolved from simple frontmatter fields to include: 12 explicit page types, status lifecycle (raw → processing → synthesized → verified → stale), confidence levels, maturity levels (seed → canonical), and ingestion modes (auto, guided, smart). This is the v2 document's "schema co-evolution" made concrete — compare early Karpathy prompts (minimal) with this project's current CLAUDE.md (comprehensive operational knowledge).

> [!example]- Are LLM Wiki Pattern and Skills Architecture structurally parallel?
> Yes. Both use markdown files as LLM-readable persistent artifacts that compound over time. Wiki pages accumulate synthesized knowledge; skill files accumulate operational knowledge. Both have index structures, both compound through iterative refinement, both solve the same maintenance problem (LLM does bookkeeping). This confirms the LLM Wiki Pattern is an instance of a more general "LLM-readable persistent artifact" pattern.

> [!example]- Is the human-AI boundary independently derived?
> Three sources converge: (1) Karpathy's "librarian vs curator", (2) Harness Engineering's Plan-before-Work approval, (3) Knowledge Evolution's `--review` flag at growing → mature. All independently place the human at the same point: direction-setting and critical transition validation. The LLM handles all maintenance and bookkeeping. Convergence across independent sources strengthens reliability.

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **What principle applies?** | [[Principle: Right Process for Right Context — The Goldilocks Imperative]] |
> | **What is my identity?** | [[Project Self-Identification Protocol — The Goldilocks Framework]] |
> | **System map** | [[Methodology System Map]] |

## Relationships

- DERIVED FROM: src-karpathy-claude-code-10x
- DERIVED FROM: src-karpathy-llm-wiki-idea-file
- DERIVED FROM: src-llm-wiki-v2-agentmemory
- COMPARES TO: [[LLM Wiki vs RAG]]
- ENABLES: [[Wiki Ingestion Pipeline]]
- ENABLES: [[Memory Lifecycle Management]]
- ENABLES: [[Wiki Knowledge Graph]]
- ENABLES: [[Wiki Event-Driven Automation]]
- USED BY: [[Obsidian Knowledge Vault]]
- FEEDS INTO: [[LLM Knowledge Linting]]
- RELATES TO: [[Claude Code Context Management]]
- RELATES TO: [[NotebookLM]]
- RELATES TO: [[Skills Architecture Patterns]]
- RELATES TO: [[Agentic Search vs Vector Search]]
- CONTRASTS WITH: [[LightRAG]]
- USED BY: [[OpenFleet]]
- ENABLED BY: [[Claude Code]]

## Backlinks

[[src-karpathy-claude-code-10x]]
[[src-karpathy-llm-wiki-idea-file]]
[[src-llm-wiki-v2-agentmemory]]
[[LLM Wiki vs RAG]]
[[Wiki Ingestion Pipeline]]
[[Memory Lifecycle Management]]
[[Wiki Knowledge Graph]]
[[Wiki Event-Driven Automation]]
[[Obsidian Knowledge Vault]]
[[LLM Knowledge Linting]]
[[Claude Code Context Management]]
[[NotebookLM]]
[[Skills Architecture Patterns]]
[[Agentic Search vs Vector Search]]
[[LightRAG]]
[[OpenFleet]]
[[Claude Code]]
[[Automated Knowledge Validation Prevents Silent Wiki Decay]]
[[Claude Code Best Practices]]
[[Context-Aware Tool Loading]]
[[Cross-Domain Patterns]]
[[Decision: Wiki-First with LightRAG Upgrade Path]]
[[Design.md Pattern]]
[[Graph-Enhanced Retrieval Bridges Wiki Navigation and Vector Search]]
[[Knowledge Evolution Pipeline]]
[[LLM-Maintained Wikis Outperform Static Documentation]]
[[Lesson: Automation Is the Bridge Between Knowledge and Action]]
[[Lesson: Knowledge Systems Is the Foundational Domain for the Entire Wiki]]
[[Lesson: Schema Is the Real Product — Not the Content]]
[[Methodology Framework]]
[[Model: LLM Wiki]]
[[Multi-Stage Ingestion Beats Single-Pass Processing]]
[[NotebookLM Skills]]
[[NotebookLM as Grounded Research Engine Not Just Note Storage]]
[[Obsidian CLI]]
[[Obsidian Skills Ecosystem]]
[[Obsidian as Knowledge Infrastructure Not Just Note-Taking]]
[[PARA Methodology]]
[[Progressive Distillation]]
[[Research Pipeline Orchestration]]
[[Second Brain Architecture]]
[[Skill Specification Is the Key to Ecosystem Interoperability]]
[[Synthesis: Claude Code Best Practice (shanraisshan)]]
[[Synthesis: Karpathy LLM Wiki Method via Claude Code]]
[[Synthesis: Karpathy's LLM Wiki Idea File]]
[[Synthesis: LLM Wiki v2 -- Extending Karpathy's Pattern with Agentmemory Lessons]]
[[Synthesis: NotebookLM + Claude Code Workflow via notebooklm-py]]
[[Synthesis: Obsidian + Claude Code Second Brain Setup]]
[[Synthesis: kepano/obsidian-skills]]
[[The Wiki Maintenance Problem Is Solved by LLM Automation]]
[[Wiki Backlog Pattern]]
[[Zettelkasten Methodology]]
[[notebooklm-py CLI]]
