---
title: "Decision: Obsidian vs NotebookLM as Knowledge Interface"
type: decision
domain: tools-and-platforms
layer: 6
status: synthesized
confidence: high
maturity: seed
derived_from:
  - "Obsidian Knowledge Vault"
  - "NotebookLM"
  - "Second Brain Architecture"
reversibility: easy
created: 2026-04-08
updated: 2026-04-08
sources:
  - id: src-karpathy-claude-code-10x
    type: youtube-transcript
    file: raw/transcripts/karpathy-claude-code-10x.txt
    title: "Andrej Karpathy Just 10x'd Everyone's Claude Code"
  - id: src-claude-notebooklm-content-team
    type: youtube-transcript
    file: raw/transcripts/claude-notebooklm-content-team.txt
    title: "Claude + NotebookLM = Your 24/7 Content Team"
  - id: src-obsidian-claude-code-second-brain
    type: youtube-transcript
    url: "https://www.youtube.com/watch?v=Y2rpFa43jTo"
    title: "Obsidian + Claude Code: The Second Brain Setup That Actually Works"
tags: [obsidian, notebooklm, knowledge-interface, second-brain, graph-view, grounded-qa, complementary-tools, wiki-frontend, research-interface]
---

# Decision: Obsidian vs NotebookLM as Knowledge Interface

## Summary

Obsidian and NotebookLM serve complementary roles as knowledge interfaces and should both be maintained rather than choosing one exclusively. Obsidian is the structured graph browser and editor: it visualizes the wiki's relationship graph, supports direct page editing, and provides the human's canonical view of the wiki's organization. NotebookLM is the grounded Q&A and content generation engine: it answers questions against specific source sets and generates multi-format content artifacts. The wiki is the source of truth synced to both.

## Decision

**Use Obsidian as the graph browser and editor. Use NotebookLM as the grounded research and content generation engine. Maintain the wiki as the source of truth that feeds both.**

Concretely:

- **Obsidian**: Primary interface for navigating the wiki graph, reviewing page relationships, browsing domain indexes, and making direct edits via the Obsidian vault (synced from WSL2 via `tools/sync.py`). The graph view is the operational dashboard for understanding knowledge structure. The Web Clipper extension is the ingestion front door for browser-sourced articles.

- **NotebookLM**: Secondary interface for grounded Q&A against specific source sets, podcast generation, slide creation, and content artifacts. Fed by exporting wiki pages to the NotebookLM notebook via `wiki_mirror_to_notebooklm` (MCP tool) or `tools/export.py`. Appropriate when the question is "what do these specific sources say about X?" rather than "what does the whole wiki know about X?"

- **Wiki as source of truth**: All writes go to the wiki (WSL2 Linux filesystem) via Claude Code or direct file editing. Obsidian reads a sync copy. NotebookLM reads an exported copy. Neither Obsidian edits nor NotebookLM outputs are committed back to the wiki without going through the ingestion pipeline and post-chain validation.

- **Sync cadence**: Obsidian syncs continuously via `wiki-sync.service` daemon. NotebookLM sync is on-demand (`wiki_mirror_to_notebooklm`) when a research or content generation session is planned.

## Alternatives

### Alternative 1: Obsidian-Only (No NotebookLM)

Use only Obsidian for all knowledge interaction — browsing, editing, and Q&A. **Rejected** because Obsidian does not provide grounded Q&A against a curated source set. Obsidian's graph view excels at structure visualization, but answering "what does the research say about routing complexity in multi-agent systems?" requires either manually navigating to relevant pages or relying on Claude to read the wiki without source grounding. NotebookLM's notebook-based model provides something Obsidian cannot: a bounded, grounded answer from a specific set of pages, with citations traceable to specific sources. The combination enables a workflow Obsidian alone cannot: curate a set of wiki pages into a NotebookLM notebook, then ask it to generate a synthesis, a comparison, or a slide deck from exactly those sources.

### Alternative 2: NotebookLM-Only (No Obsidian)

Use only NotebookLM for all knowledge interaction — browsing, editing, and Q&A. **Rejected** because NotebookLM cannot serve as the wiki's editor or graph browser. NotebookLM is a consumption and generation tool: you load sources, ask questions, generate artifacts. It does not provide a graph view of relationships, does not support direct page editing, and does not expose the wiki's typed relationship structure (`BUILDS ON`, `DERIVES FROM`, etc.). Obsidian's backlink navigation and graph view are irreplaceable for understanding which pages are hubs, which domains are thin, and what structural gaps exist. NotebookLM also has a 300-source limit per notebook, making it unsuitable as the primary interface for a wiki that may grow to hundreds of pages.

### Alternative 3: Custom RAG (Replace Both)

Build a custom RAG system (vector store + retrieval + LLM) that serves as the single knowledge interface. **Rejected as premature.** The Second Brain Architecture page identifies this as "Subsystem 3 (local inference)" in the ecosystem's roadmap, unlocked by the hardware upgrade to 19GB VRAM. Custom RAG would provide the best of both worlds — graph-aware retrieval plus grounded generation — but requires significant infrastructure investment (embedding pipeline, vector store, retrieval tuning, hosted interface). Obsidian + NotebookLM provides complementary coverage today with zero infrastructure cost. The custom RAG path remains the long-term target but is not the right decision for the current ecosystem maturity level.

## Rationale

The Obsidian Knowledge Vault page identifies two distinct use modes for the Obsidian + Claude Code combination: "(1) the knowledge accumulation mode (Karpathy's wiki pattern, where the goal is research synthesis) and (2) the operational management mode (where the goal is actionable project intelligence)." Both modes require Obsidian's graph view and editing capability — NotebookLM cannot substitute for either.

The NotebookLM page establishes its core value proposition: "Source-grounded generation — NotebookLM generates all outputs from user-provided sources rather than from general training data, making it a grounded research and content tool rather than a general-purpose chatbot." This grounding is exactly what general-purpose LLMs lack when answering questions about the wiki: without source pinning, answers may blend wiki knowledge with training data. NotebookLM's notebook model enforces explicit source boundaries.

The LLM Wiki vs RAG comparison (referenced in the NotebookLM page's answered questions) frames the tradeoff clearly: the wiki pattern compiles and reconciles knowledge during ingestion; RAG (and NotebookLM) returns raw conflicting chunks per query. For questions that require synthesized, contradiction-resolved answers across many domains, the wiki's ingestion-time synthesis is more reliable than NotebookLM's per-query retrieval. But for questions that require grounded verification against specific source texts — "does source X actually say Y?" — NotebookLM's retrieval model is more trustworthy than the wiki's synthesized summaries, which may lose nuance during ingestion.

The wiki-as-source-of-truth architecture preserves clean data lineage. The NotebookLM page's answered question confirms: "Sources ingested via tools/ingest.py can be simultaneously pushed to NotebookLM notebooks via `notebooklm source add`" — the wiki ingestion pipeline and the NotebookLM pipeline can share the same raw sources without creating data duplication. The wiki synthesizes; NotebookLM retrieves against the originals.

## Reversibility

**Easy to reverse.** Both Obsidian and NotebookLM are consumption layers — they read from the wiki and from raw sources, respectively. Neither stores canonical data. Removing either from the workflow requires updating operational habits and the sync daemon configuration, but no data migration and no architectural changes. The wiki's markdown files remain usable with any other tool (VS Code, vim, any text editor) if both Obsidian and NotebookLM were abandoned.

The custom RAG alternative (Subsystem 3) is the likely long-term successor to both. When it becomes available, Obsidian would remain as the graph editor and NotebookLM would be replaced by the custom RAG interface for Q&A. This transition is incremental: add the RAG layer, validate quality, then reduce reliance on NotebookLM over time.

## Dependencies

**Downstream effects of this decision:**

- **wiki-sync.service daemon**: Must remain running for Obsidian to reflect wiki edits. The decision to use Obsidian as the graph browser requires the sync daemon to be reliable.
- **wiki_mirror_to_notebooklm MCP tool**: The on-demand NotebookLM sync tool (`mcp__research-wiki__wiki_mirror_to_notebooklm`) is the operationalization of the NotebookLM workflow. It should be invoked before any NotebookLM research session that requires current wiki state.
- **tools/obsidian.py**: The Obsidian wikilink regeneration step (part of the post-chain) must keep [[wikilinks]] current so Obsidian's graph view reflects actual relationships. If obsidian.py is skipped, the Obsidian graph degrades over time.
- **Obsidian edits are low-trust**: Direct Obsidian edits (made in the Windows-side vault) must be synced back via `tools/sync.py --reverse` and then run through the post-chain for validation. They should not bypass `tools.validate`. This means Obsidian is "almost read-only" for the wiki's canonical content — it is safe for adding notes and annotations, but structural edits (frontmatter, relationship sections) should go through Claude Code.
- **NotebookLM rate limits**: The NotebookLM page notes "heavy automated usage triggers Google's rate limits." On-demand sync (not continuous automated sync) avoids this issue. The `--retry` flag in notebooklm-py handles transient failures.
- **300-source limit**: NotebookLM notebooks support up to 300 sources. As the wiki grows past 300 pages, the mirror strategy may need to split into topic-scoped notebooks rather than a full-wiki notebook. This is a known scaling boundary, not a current blocker.

## Relationships

- DERIVED FROM: Obsidian Knowledge Vault
- DERIVED FROM: NotebookLM
- DERIVED FROM: Second Brain Architecture
- RELATES TO: WSL2 Development Patterns
- RELATES TO: Wiki Ingestion Pipeline
- RELATES TO: MCP Integration Architecture
- ENABLES: AI-Driven Content Pipeline
- FEEDS INTO: Wiki Knowledge Graph
- RELATES TO: LLM Wiki vs RAG

## Backlinks

[[Obsidian Knowledge Vault]]
[[NotebookLM]]
[[Second Brain Architecture]]
[[WSL2 Development Patterns]]
[[Wiki Ingestion Pipeline]]
[[MCP Integration Architecture]]
[[AI-Driven Content Pipeline]]
[[Wiki Knowledge Graph]]
[[LLM Wiki vs RAG]]
