---
title: "Source — The 7 Levels of Claude Code & RAG"
type: source-synthesis
domain: ai-agents
status: synthesized
confidence: high
maturity: seed
created: 2026-04-14
updated: 2026-04-14
sources:
  - id: 7-levels-claude-code-rag-youtube
    type: youtube-transcript
    url: https://www.youtube.com/watch?v=kQu5pWKS8GA
tags:
  - claude-code
  - rag
  - memory
  - context-management
  - obsidian
  - graph-rag
  - vector-database
  - embeddings
  - context-engineering
  - knowledge-base
  - token-efficiency
---

# Source — The 7 Levels of Claude Code & RAG

## Summary

A structured road map deconstructing the memory and retrieval problem in Claude Code across seven levels — from native automemory through CLAUDE.md, state-file architectures, Obsidian vaults, naive RAG, graph RAG, and agentic multimodal RAG. The video frames each level with what to expect, skills to master, traps to avoid, and when to move on. The central thesis is that most people stay at level one and never need level seven — the right level depends on scale, use case, and willingness to experiment.

## Key Insights

1. **Context rot is the root problem.** As a session accumulates tokens toward the 1M context ceiling, output quality degrades measurably (from ~92% to ~78% performance in the video's example). Every memory strategy is ultimately a defense against context rot and the ballooning token cost that comes with it.

2. **CLAUDE.md is a double-edged sword.** Studies show that instruction files injected into every prompt can reduce LLM effectiveness when they contain low-signal content. Less is more — CLAUDE.md should be a high-signal routing index, not a bloated rulebook.

3. **Obsidian is the 80/20 solution for most solo operators.** A well-structured vault with a master index and hierarchical article folders gives Claude Code a clear retrieval path without any RAG infrastructure. The video's benchmark puts naive RAG at ~1,200x cheaper/faster than full context LLM, but Obsidian closes most of that gap for typical solo workloads at zero cost.

4. **Naive RAG is often just a complicated search engine.** Isolated vector chunks with no relationship awareness produce ~25% accuracy in practice. Chunking strategy, document structure, and cross-chunk context dependencies make naive RAG fragile. It is foundational to understand but inadequate to ship.

5. **Graph RAG (e.g., LightRAG) doubles accuracy on relational queries.** LightRAG benchmarks show 31.6 → 68.4%, 24 → 76%, 24 → 75% improvements over naive RAG across multiple categories. Relationship extraction between entities is the key differentiator.

6. **The real work at level seven is data ingestion, not retrieval.** Agentic RAG systems spend the majority of their infrastructure on data pipelines — deduplication, versioning, multi-source sync, access control — not on the query side. The retrieval part is a small fraction of total architecture.

7. **Experiment in ascending order, stop when it's good enough.** Start with CLAUDE.md → state files → Obsidian → LightRAG → agentic multimodal. Avoid skipping to graph RAG before validating simpler options. The cost of over-engineering a RAG system that isn't needed is significant.

## Deep Analysis

### The Memory Problem in Claude Code

The video opens by reframing the RAG conversation as fundamentally a memory problem. AI systems lack persistent memory across sessions, and users compensate by keeping sessions alive indefinitely — which directly causes context rot. The 1M token context window made this worse, not better, because it removed the forcing function that made users clear sessions.

The core tension throughout all seven levels: adding more context to help the model remember things also degrades output quality and increases token cost. Every level is an attempt to resolve this tension more elegantly.

---

### Level 1 — Automemory (Baseline)

**What it is:** Claude Code's built-in memory system, which autonomously creates markdown files in `~/.claude/projects/<project>/memory/` based on inferred user preferences during conversations.

**What to expect:** Post-it note quality. The system records things like "user wants X subscribers by 2026" and surface them in future turns. Similar to ChatGPT's memory interjection behavior — occasionally useful, often irrelevant.

**The trap:** Most users never progress past this level. Because sessions can run arbitrarily long with a 1M context window, users compensate for weak memory by never closing sessions. Context rot accumulates silently.

**To move on:** Understand that automemory is not enough, and take active control of what Claude Code considers. The escape is explicit, curated context.

---

### Level 2 — CLAUDE.md

**What it is:** A single markdown file at the project root (or user home) that Claude Code reads before every prompt. Contains conventions, permanent rules, and structural guidance for a project.

**Techniques:**
- Use `CLAUDE.md` for high-signal, always-relevant information only
- Structure it as an index pointing to other files rather than as an exhaustive rulebook
- Treat it as a conventions file, not a memory dump

**The trap (validated by study):** The same property that makes CLAUDE.md powerful — injection into every prompt — makes it harmful when content is low-signal. The study referenced in the video found that instruction files reduce LLM effectiveness when they contain noise. Context pollution is a real phenomenon.

**What good looks like:**
- Concise about-me section
- Filesystem/project structure overview
- Pointer index to domain-specific files
- Conventions that apply to literally every task

**To move on:** Recognize that a single file cannot hold all project state, and that state should be distributed into purpose-specific files with CLAUDE.md as the routing layer.

---

### Level 3 — State File Architecture (Multi-Markdown)

**What it is:** Replacing the single CLAUDE.md monolith with a structured hierarchy of markdown files. Each file serves a specific memory function. The video cites GSD (Get Stuff Done) as an example implementation.

**Example structure:**
- `project.md` — North star, high-level overview
- `requirements.md` — What is being built
- `roadmap.md` — Past, present, and future work
- `state.md` — Current session state

**Why this is better than a single file:** Files are loaded selectively. When Claude Code follows the index to find a specific piece of information, it is not injecting all state into every prompt — it retrieves what is needed. This is a primitive analog of the chunking principle in RAG.

**The GSD/Superpowers connection:** Orchestration tools like GSD and Superpowers implement this multi-markdown architecture automatically. Using them means getting level-3 structure without building it manually.

**The trap:** Each project has its own isolated markdown structure. Files do not transfer cleanly across projects. The system does not scale to hundreds or thousands of documents. There is no tooling for index maintenance.

**To move on:** The project-specific nature of markdown architectures demands an external tool that manages the vault abstraction across projects. That tool is Obsidian.

---

### Level 4 — Obsidian Vault (Recommended Floor for Most Users)

**What it is:** An Obsidian vault used as a structured knowledge base that Claude Code queries. André Carpathy's public LLM knowledge base (20M views) is the canonical reference implementation.

**Architecture (Carpathy pattern):**
- `raw/` — Staging area for unstructured ingested content (competitive analyses, research dumps, documents)
- `wiki/` — Structured articles generated from raw content. Each topic gets its own subfolder with an `index.md`
- `vault/_index.md` — Master index: the routing layer Claude Code always reads first
- `CLAUDE.md` — Describes vault structure and access conventions

**How Claude Code retrieves information:**
1. Check vault master index
2. Master index points to wiki section index
3. Section index lists articles
4. Navigate to specific article

**Why this works at scale:** The hierarchy is explicit and navigable. Claude Code does not need semantic similarity search to find relevant content — it follows a deterministic index path. With a clean hierarchy, thousands of documents become tractable without RAG infrastructure.

**Token efficiency comparison:** Textual RAG is ~1,200x cheaper/faster than full-context LLM in 2025 benchmarks (noted as likely outdated but the magnitude of the gap remains relevant). Obsidian sits between these extremes — near-RAG efficiency for well-structured content, at zero infrastructure cost.

**When Obsidian breaks down:**
- When the document count drives index lookup cost too high
- When speed and token efficiency gaps become measurable at production scale
- When relational queries span documents that don't directly reference each other

**The trap:** Obsidian connections are manual and somewhat arbitrary (bracket-linked). This is fundamentally different from semantic embedding-based relationships. The visual graph looks similar to LightRAG's knowledge graph but is far more rudimentary under the hood.

**Recommendation from the video:** Start here. Always. If you haven't tried Obsidian, do not attempt graph RAG. It is the correct entry point for solo operators and most small teams.

---

### Level 5 — Naive RAG (Foundation to Understand, Not to Ship)

**What it is:** The classical three-stage RAG pipeline: embedding → vector database → retrieval. Understanding this level is mandatory for making good decisions at levels 6 and 7.

**The pipeline:**
1. **Chunking:** Documents are split into overlapping fragments (by token count, paragraph boundary, or semantic unit)
2. **Embedding:** Each chunk passes through an embedding model (e.g., text-embedding-3-small, Gemini Embedding) and is converted to a high-dimensional vector
3. **Vector database:** Vectors are stored with positional semantics — semantically similar content clusters together (e.g., fruits cluster near fruits, ships near ships) in hundreds or thousands of dimensions
4. **Query time:** User query is embedded into the same vector space → nearest-neighbor search retrieves top-k matching chunks → chunks are injected into the LLM prompt alongside the query → LLM generates a retrieval-augmented answer

**Why naive RAG fails in practice:**
- Chunk 3 may reference context that only exists in chunk 1 — without both chunks, chunk 3 is meaningless
- Documents are rarely structured to chunk cleanly along semantic boundaries
- Inter-document relationships (how document A relates to document B) are invisible in a purely vectorized, siloed system
- Practical accuracy: ~25% correct answers in unsophisticated implementations

**Rerankers as a partial fix:** A second-pass LLM evaluates the retrieved chunks for relevance and reranks them before injecting into the final prompt. This improves accuracy but adds latency and cost.

**The trap:** Pine cone, Supabase, and other naive vector RAG offerings marketed without graph awareness or reranking produce poor results. Recognizing them on sight protects against being "hoodwinked into buying rag systems that do not make sense."

**To move on:** Understand chunking, embeddings, and vector similarity at a conceptual level. Then evaluate whether relational queries are needed — if yes, graph RAG is required.

---

### Level 6 — Graph RAG (Minimum Viable Production RAG)

**What it is:** A knowledge graph that augments vector similarity with explicit entity-relationship extraction. The video focuses on LightRAG as the recommended open-source implementation.

**How it differs from naive RAG:**
- Documents are processed to extract entities and relationships between them, not just text chunks
- The graph database stores both vectors AND edges (relationships)
- Queries can traverse the graph — "how does X relate to Y across multiple documents?" becomes answerable
- LightRAG uses a hybrid vector + graph query mode

**LightRAG benchmarks (from LightRAG's own GitHub, ~6-8 months old):**
- Naive RAG vs. LightRAG: 31.6% → 68.4%
- 24% → 76%
- 24% → 75%
- LightRAG claims to outperform Microsoft's GraphRAG on several benchmarks (with the caveat that these are self-reported)

**When to use graph RAG over Obsidian:**
- Document count makes index traversal expensive
- Query patterns require relationship traversal across documents that don't directly reference each other
- Production team environment with multiple contributors

**The key distinction from Obsidian:** Obsidian links are manually set or generated by Claude Code based on surface heuristics. LightRAG relationships are extracted by analyzing actual content semantics and encoded into the graph with entity types, relationship types, and source attribution. These are architecturally different.

**Remaining limitations at level 6:**
- Text-only: no support for scanned PDFs, images, tables, or video
- No data ingestion pipeline: documents go directly into LightRAG without version control, deduplication, or access management

**To move on:** Need multimodal ingestion or production-grade data pipeline management.

---

### Level 7 — Agentic Multimodal RAG (Bleeding Edge, April 2026)

**What it is:** The integration of multimodal embedding, production data pipelines, and agentic routing into a unified retrieval architecture.

**Multimodal additions:**
- **RAG Anything:** Extends LightRAG-style graph RAG to support scannable PDFs, images, and tables via specialized document parsers
- **Gemini Embedding 2 (March 2026):** Embeds video natively into vector databases — not just transcripts but the video content itself

**Agentic routing pattern:**
At level 7, a top-of-funnel AI agent decides the retrieval strategy per query:
- Graph RAG database (for knowledge queries)
- SQL/Postgres queries (for structured data)
- Direct context injection (for small, known documents)
- Web search (for current events beyond training cutoff)

**The data pipeline problem (the real work at level 7):**
The video references a NAND agentic RAG diagram where the vast majority of infrastructure is data ingestion and sync, not retrieval. Real production concerns:
- Document versioning: when v2 supersedes v1, old embeddings must be cleaned
- Deduplication: same content ingested from multiple sources
- Access control: who can add/remove documents
- Source pipeline: documents staged in Google Drive → ingested → logged, rather than direct upload
- Freshness: how stale are embeddings when source documents change

**The trap at level 7:** Forcing complexity that isn't needed. After building through all seven levels conceptually, the video concludes that most people are still best served by Obsidian. Level 7 is justified only when multimodal ingestion is required AND relational queries across thousands of documents are needed AND team-scale data governance is required.

---

### Token Efficiency Perspective

The video provides a framing for token efficiency across the levels:

| Approach | Relative Cost | Accuracy (relational queries) |
|----------|--------------|-------------------------------|
| Bloated context (never clear) | Highest | Degrades with rot |
| CLAUDE.md only | High if noisy | Limited |
| State file architecture | Moderate | Project-scoped |
| Obsidian vault | Low (with good index) | Good for solo scale |
| Naive RAG | ~1,200x cheaper than LLM | ~25% on relational |
| Graph RAG (LightRAG) | Comparable to naive RAG | ~70% on relational |
| Agentic multimodal RAG | Route-dependent | Context-dependent |

The 1,200x benchmark is from 2025 on older models and is noted as likely overestimated today, but the directional gap between context-stuffing and RAG remains large.

---

### Skills Architecture Implications

The video's level 2 treatment of CLAUDE.md has direct implications for how Claude Code skills are structured:

- CLAUDE.md as index → skills as leaf documents: the CLAUDE.md file points to skill definitions rather than containing them. This is the architecture this wiki uses.
- State files per concern: context about a project should live in purpose-specific files, not aggregated in CLAUDE.md
- Deferred loading: Claude Code should fetch context on demand (follow the index) rather than receive all context on every prompt

This maps directly to the [[model-context-engineering|Model — Context Engineering]] principle of structured, depth-appropriate context delivery.

---

### Graph RAG vs. Obsidian — The Structural Difference

A nuance the video makes explicit: Obsidian and LightRAG look visually similar (nodes and connections) but are architecturally different.

**Obsidian connections:**
- Set by Claude Code based on surface content review
- Implemented as `[[wiki-links]]` in markdown
- Manual, arbitrary, low-semantic-fidelity

**LightRAG connections:**
- Extracted by embedding model analyzing document content
- Encoded with entity types (person, concept, technology), relationship types (builds-on, contradicts, enables), and source attribution
- Semantically grounded, high-fidelity

At low document counts and solo-operator scale, this difference may not manifest as measurable accuracy gaps. At thousands of documents with complex relational queries, the gap is the entire point.

## Open Questions

- ~~At what document count does Obsidian's index traversal cost begin to exceed a graph RAG query cost?~~ **PARTIALLY RESOLVED (2026-04-15):** This wiki's [[llm-wiki-vs-rag|LLM Wiki vs RAG]] comparison sets the ceiling for **index-only navigation** at **~200 pages**. Beyond that, `index.md` itself becomes too long for the LLM to read in one pass — matching the [[src-llm-wiki-v2-agentmemory|LLM Wiki v2]] finding (~100-200 pages is where flat-file search breaks down). The crossover with graph-RAG query cost depends on the specific query type (single-hop vs multi-hop), but structural index breakdown is well-bounded. Exact graph-RAG cost comparison at varying sizes remains empirical.
- Does LightRAG's claimed superiority over Microsoft's GraphRAG hold on code-heavy technical corpora (vs. general text)? (Requires: benchmark comparison on code corpora — external empirical data.)
- What is the practical accuracy of Gemini Embedding 2 for video content retrieval vs. transcript-only embedding? (Requires: empirical measurement — external.)
- ~~Can the Obsidian vault architecture in this wiki be extended with LightRAG as a complementary system for cross-document relational queries?~~ **RESOLVED (2026-04-15):** **Yes — this is a documented upgrade path.** See [[wiki-first-with-lightrag-upgrade-path|Decision — Wiki-First with LightRAG Upgrade Path]]: the wiki's Obsidian vault provides structural navigation at current scale (334 pages, avg 6.6 relationships/page), with LightRAG available as a graph-RAG layer when query complexity or scale demands it. Additionally, OpenFleet's `kb_sync.py` already parses the wiki's `## Relationships` sections into a LightRAG graph (2,295 explicit relationships from 219 KB entries per [[four-project-ecosystem|Four-Project Ecosystem]]). The extension is not theoretical — it is partially operational in the ecosystem.
- What is the real accuracy gap in 2026 between naive RAG and graph RAG on modern models (given the benchmarks cited are 6-8 months old)? (Requires: recent benchmark data — external empirical.)

### Answered Open Questions

**Resolved by wiki cross-reference** (2026-04-15):

- **Obsidian index ceiling at ~200 pages** — partial answer from [[llm-wiki-vs-rag|LLM Wiki vs RAG]] and LLM Wiki v2 finding; graph-RAG crossover cost remains empirical.
- **Obsidian + LightRAG extension** — documented upgrade path ([[wiki-first-with-lightrag-upgrade-path|Decision]]) + partially operational (OpenFleet's kb_sync.py integration).

**Genuinely deferred** (require external empirical benchmarks):

- LightRAG vs GraphRAG on code corpora
- Gemini Embedding 2 video retrieval accuracy
- 2026 RAG-vs-graph-RAG accuracy gap

## Relationships

- BUILDS ON: [[model-context-engineering|Model — Context Engineering]] (context rot, signal/noise, deferred loading)
- BUILDS ON: [[model-claude-code|Model — Claude Code]] (CLAUDE.md architecture, skills, session management)
- RELATES TO: [[model-mcp-cli-integration|Model — MCP and CLI Integration]] (tool integration patterns that affect context cost)
- RELATES TO: [[model-llm-wiki|Model — LLM Wiki]] (the wiki-as-RAG-system parallel; vault architecture mirrors wiki architecture)
- VALIDATES: [[cli-tools-beat-mcp-for-token-efficiency|CLI Tools Beat MCP for Token Efficiency]] (same token efficiency principle applies to RAG vs. context stuffing)

## Backlinks

[[model-context-engineering|Model — Context Engineering]]
[[model-claude-code|Model — Claude Code]]
[[model-mcp-cli-integration|Model — MCP and CLI Integration]]
[[model-llm-wiki|Model — LLM Wiki]]
[[cli-tools-beat-mcp-for-token-efficiency|CLI Tools Beat MCP for Token Efficiency]]
