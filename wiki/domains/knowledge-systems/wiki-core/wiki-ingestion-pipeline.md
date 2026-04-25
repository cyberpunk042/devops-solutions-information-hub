---
title: Wiki Ingestion Pipeline
aliases:
  - "Wiki Ingestion Pipeline"
type: concept
layer: 2
maturity: growing
domain: knowledge-systems
status: synthesized
confidence: high
created: 2026-04-08
updated: 2026-04-13
sources:
  - id: src-karpathy-claude-code-10x
    type: youtube-transcript
    file: raw/transcripts/karpathy-claude-code-10x.txt
    title: Andrej Karpathy Just 10x'd Everyone's Claude Code
    ingested: 2026-04-08
  - id: src-karpathy-llm-wiki-idea-file
    type: documentation
    url: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
    file: raw/articles/karpathy-llm-wiki-idea-file.md
    title: Karpathy LLM Wiki Idea File
    ingested: 2026-04-08
  - id: src-llm-wiki-v2-agentmemory
    type: documentation
    url: https://gist.github.com/rohitg00/2067ab416f7bbe447c1977edaaa681e2
    file: raw/articles/llm-wiki-v2-extending-karpathys-llm-wiki-pattern-with-lessons-from-building-agen.md
    title: LLM Wiki v2 -- Extending Karpathy's LLM Wiki Pattern with Lessons from Building Agentmemory
    ingested: 2026-04-08
tags: [ingestion, pipeline, claude-code, wiki, markdown, data-processing, workflow, entity-extraction, event-driven]
---

# Wiki Ingestion Pipeline

## Summary

The wiki ingestion pipeline is the workflow by which raw source documents are transformed into structured, interlinked wiki pages by Claude Code. The process has distinct phases: data ingest (placing raw documents into the `raw/` folder), processing (Claude Code reads the source, asks clarifying questions, then generates multiple wiki pages with relationships), and linking (the index is updated, cross-references are created, and the operation is logged). The pipeline handles diverse source types including PDFs, web articles, and transcript batches, and adapts its output granularity based on source complexity — a single article may produce anywhere from 5 to 25 wiki pages.

## Key Insights

> [!info] Three ingestion modes
>
> | Mode | Behavior | When to Use |
> |------|----------|-------------|
> | **guided** | Show extraction plan, wait for approval, review each page | New domains, complex sources, high-stakes content |
> | **smart** (default) | Auto when confident; escalate on: new domain, contradictions, ambiguity | Most ingestion |
> | **auto** | Process without stopping, report summary | High-confidence, low-complexity, batch URLs |

> [!tip] The pipeline comprehends, not chunks
> Unlike RAG (mechanical splitting at token boundaries), the LLM reads holistically and makes editorial decisions: how many pages, what entities, what relationships. A single article may produce 5–25 pages depending on content density. The human does no manual relationship building.

**Clarifying questions shape output.** After reading a source, Claude Code asks about emphasis, focus areas, granularity, and project purpose. This is what makes the same pipeline work for research vaults and personal second brains.

**Batch ingestion scales linearly.** 36 YouTube transcripts in 14 minutes (~23 seconds/transcript in batch). Individual articles ~10 minutes. `pipeline run URL [URL...]` for parallel fetch + post-chain.

**v2 extensions.** Entity extraction during ingestion (structured entities, not just prose). Event-driven auto-ingestion (hooks on new raw files). Privacy filtering (strip API keys, PII before wiki). All additive to the current pipeline.

## Deep Analysis

> [!info] Pipeline Commands for Ingestion
>
> | Command | What It Does |
> |---------|-------------|
> | `pipeline fetch URL` | Fetch a URL into raw/ |
> | `pipeline run URL` | Fetch + full post-chain |
> | `pipeline post` | 6-step validation chain (indexes → manifest → validate → wikilinks → lint → layer indexes) |
> | `pipeline scaffold <type> "Title"` | Create page from template |
> | `pipeline chain ingest` | Full ingestion chain |

The ingestion pipeline is the core engine of the LLM Wiki pattern. Its effectiveness comes from treating document processing not as a chunking problem (as in RAG) but as a comprehension and organization problem. Claude Code reads the full source, understands it holistically, and then makes editorial decisions about how to decompose it into wiki pages.

This is a fundamentally different approach from RAG chunking, where documents are mechanically split at fixed token boundaries or paragraph breaks. The LLM's chunking is semantic — it groups related information into coherent pages based on conceptual boundaries, creates pages for entities and concepts that deserve their own entries, and links everything together.

The clarifying questions phase is an underappreciated design element. By asking the user about their goals and focus, the pipeline customizes its output to the user's actual needs rather than producing generic summaries. This interactive step is what makes the same pipeline work for both a YouTube transcript archive and a personal second brain — the structure emerges from the conversation, not from a rigid template.

The batch ingestion capability demonstrates that the pipeline scales linearly with source count. 36 transcripts in 14 minutes suggests roughly 23 seconds per transcript for a batch operation, which is significantly faster than the 10-minute single-article ingestion — likely because batch mode reduces the per-source overhead of index updates and question-asking.

A key architectural decision is that the raw source is preserved in the `raw/` folder even after ingestion. This means you can re-ingest sources with different parameters, audit the wiki against its sources, or migrate to a different system later without losing original data.

## Open Questions

- How does ingestion quality vary across source types (structured PDF vs. rambling transcript vs. dense technical paper)? (Requires: empirical benchmarking across source types; the `Rework Prevention` page notes that smart mode escalates for "low-quality source" cases, but no quantitative quality data across source types is documented in existing wiki pages)

### Answered Open Questions

**Q: Can the pipeline be run in fully non-interactive mode for automated ingestion (skipping the clarifying questions)?**

Cross-referencing `Rework Prevention` and `Research Pipeline Orchestration`: yes — `auto` mode is the fully non-interactive ingestion mode. The `Rework Prevention` page documents all three ingestion modes: "auto mode: No gates. Appropriate only for high-confidence, low-complexity sources where rework risk is low and throughput is valued. The `post` chain's validation step (exit code 1 on errors) is the only hard gate in auto mode." The `Research Pipeline Orchestration` page confirms the vision: "Extract pages (Claude Code manual) → Needs skill-driven automation" and documents `pipeline run URL [URL...]` as the "Parallel fetch + post-chain in one command" — this is the closest current implementation of fully automated end-to-end ingestion. The three-mode system (auto/guided/smart) means non-interactive operation is already supported by design; the user selects `auto` or the pipeline defaults to `smart` which only asks questions when risk is high. For fully automated pipeline operation (e.g., scheduled overnight ingestion of a URL list), `auto` mode with `pipeline run --batch urls.txt` is the correct invocation.

**Q: How does the pipeline handle updates to a previously ingested source — does it diff and update, or re-create from scratch?**

Cross-referencing `Knowledge Evolution Pipeline` and `Rework Prevention`: the current model is re-create from scratch using the evolution pipeline's `derived_from` + `status: stale` mechanism, not diff-and-patch. The `Knowledge Evolution Pipeline` page documents the update mechanism: "The original page is preserved (or marked `status: stale`) and the promoted page carries a `derived_from` frontmatter field pointing back." The `Rework Prevention` page notes: "The raw source is preserved in the `raw/` folder even after ingestion. This means you can re-ingest sources with different parameters." The practical update workflow: re-ingest the updated source (or new version of a source) and the pipeline creates new pages; the curator then marks the old pages `status: stale` and adds `SUPERSEDES` relationships from new to old. A true diff-and-update mechanism (detecting changes between ingestion runs and patching only modified sections) is not implemented in existing wiki tooling — the `Knowledge Evolution Pipeline` page's `--review` flag is the closest human gate for deciding whether a re-ingested version should supersede an existing page.

**Q: Is there a way to prioritize which raw documents to ingest next based on the wiki's current gaps?**

Cross-referencing `Knowledge Evolution Pipeline` and `Research Pipeline Orchestration`: yes — `pipeline gaps` is the gap analysis tool that identifies what to ingest next. The `Knowledge Evolution Pipeline` page documents the outer loop: "3. Gaps: Run `pipeline gaps` to find orphans, thin pages, missing backlinks, and under-covered domains. 4. Research: Queue new sources to fill identified gaps." The `Research Pipeline Orchestration` page describes a `DEEPENING` pipeline type: "lint_report → identify_thin → research_gaps → enrich → validate → integrate" — this is the automated version of gap-driven ingestion prioritization. For raw files already in `raw/`, `tools/pipeline status` shows unprocessed raw files, and `pipeline gaps` identifies which domains are thin. Cross-referencing these two outputs gives a priority queue: ingest raw files that address the weakest domains first. The `pipeline chain continue` command (`status → review → score → gaps → crossref`) surfaces this priority information in one operation.

**Q: Could the pipeline be triggered automatically when a new file appears in the `raw/` folder?**

Cross-referencing `Knowledge Evolution Pipeline` and `WSL2 Development Patterns`: yes — this is explicitly described in the LLM Wiki v2 source as "event-driven auto-ingestion" and the infrastructure to implement it already exists. The `Wiki Ingestion Pipeline` Key Insights section (from v2) states: "Rather than requiring the user to manually trigger ingestion, a 'new source' event hook should auto-ingest, extract entities, update the graph, and update the index. The human remains in the loop for curation but is freed from remembering to trigger processing." The `WSL2 Development Patterns` page documents `tools/watcher.py` which already watches the `wiki/` folder for changes and triggers the post-chain. Extending `watcher.py` to also watch `raw/` for new files (which land on the Linux filesystem where inotify is reliable) and trigger `pipeline run` in `auto` or `smart` mode is a direct implementation of the v2 vision. The `Research Pipeline Orchestration` page calls this the `ONLINE RESEARCH` pipeline triggered by "new source" events. The technical components exist; the missing piece is extending the watcher's watched paths from `wiki/` to also include `raw/`.

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **What principle applies?** | [[right-process-for-right-context-the-goldilocks-imperative|Principle — Right Process for Right Context — The Goldilocks Imperative]] |
> | **What is my identity?** | [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]] |
> | **System map** | [[methodology-system-map|Methodology System Map]] |

## Relationships

- DERIVED FROM: [[src-karpathy-claude-code-10x|Synthesis — Karpathy LLM Wiki Method via Claude Code]]
- DERIVED FROM: [[src-karpathy-llm-wiki-idea-file|Synthesis — Karpathy's LLM Wiki Idea File]]
- DERIVED FROM: [[src-llm-wiki-v2-agentmemory|Synthesis — LLM Wiki v2 -- Extending Karpathy's Pattern with Agentmemory Lessons]]
- IMPLEMENTS: [[llm-wiki-pattern|LLM Wiki Pattern]]
- USED BY: [[obsidian-knowledge-vault|Obsidian Knowledge Vault]]
- FEEDS INTO: [[llm-knowledge-linting|LLM Knowledge Linting]]
- FEEDS INTO: [[wiki-knowledge-graph|Wiki Knowledge Graph]]
- EXTENDS: [[research-pipeline-orchestration|Research Pipeline Orchestration]]
- RELATES TO: [[notebooklm-py-cli|notebooklm-py CLI]]
- RELATES TO: [[obsidian-cli|Obsidian CLI]]
- RELATES TO: [[wiki-event-driven-automation|Wiki Event-Driven Automation]]
- PARALLELS: [[ai-driven-content-pipeline|AI-Driven Content Pipeline]]
- CONSTRAINED BY: [[claude-code-context-management|Claude Code Context Management]]

## Backlinks

[[src-karpathy-claude-code-10x|Synthesis — Karpathy LLM Wiki Method via Claude Code]]
[[src-karpathy-llm-wiki-idea-file|Synthesis — Karpathy's LLM Wiki Idea File]]
[[src-llm-wiki-v2-agentmemory|Synthesis — LLM Wiki v2 -- Extending Karpathy's Pattern with Agentmemory Lessons]]
[[llm-wiki-pattern|LLM Wiki Pattern]]
[[obsidian-knowledge-vault|Obsidian Knowledge Vault]]
[[llm-knowledge-linting|LLM Knowledge Linting]]
[[wiki-knowledge-graph|Wiki Knowledge Graph]]
[[research-pipeline-orchestration|Research Pipeline Orchestration]]
[[notebooklm-py-cli|notebooklm-py CLI]]
[[obsidian-cli|Obsidian CLI]]
[[wiki-event-driven-automation|Wiki Event-Driven Automation]]
[[ai-driven-content-pipeline|AI-Driven Content Pipeline]]
[[claude-code-context-management|Claude Code Context Management]]
[[claude-code|Claude Code]]
[[claude-code-best-practices|Claude Code Best Practices]]
[[context-aware-tool-loading|Context-Aware Tool Loading]]
[[mcp-vs-cli-for-tool-integration|Decision — MCP vs CLI for Tool Integration]]
[[obsidian-vs-notebooklm-as-knowledge-interface|Decision — Obsidian vs NotebookLM as Knowledge Interface]]
[[infrastructure-must-be-reproducible-not-manual|Infrastructure Must Be Reproducible, Not Manual]]
[[knowledge-evolution-pipeline|Knowledge Evolution Pipeline]]
[[llm-wiki-vs-rag|LLM Wiki vs RAG]]
[[llm-maintained-wikis-outperform-static-documentation|LLM-Maintained Wikis Outperform Static Documentation]]
[[schema-is-the-real-product|Lesson — Schema Is the Real Product — Not the Content]]
[[lightrag|LightRAG]]
[[mcp-integration-architecture|MCP Integration Architecture]]
[[memory-lifecycle-management|Memory Lifecycle Management]]
[[model-llm-wiki|Model — LLM Wiki]]
[[multi-stage-ingestion-beats-single-pass|Multi-Stage Ingestion Beats Single-Pass Processing]]
[[never-synthesize-from-descriptions-alone|Never Synthesize from Descriptions Alone]]
[[obsidian-as-knowledge-infrastructure|Obsidian as Knowledge Infrastructure Not Just Note-Taking]]
[[para-methodology|PARA Methodology]]
[[per-role-command-architecture|Per-Role Command Architecture]]
[[plan-execute-review-cycle|Plan Execute Review Cycle]]
[[rework-prevention|Rework Prevention]]
[[second-brain-architecture|Second Brain Architecture]]
[[shallow-ingestion-is-systemic-not-isolated|Shallow Ingestion Is Systemic, Not Isolated]]
[[src-context-mode|Synthesis — Context Mode — MCP Sandbox for Context Saving]]
[[src-firecrawl-web-scraper-for-ai-agents|Synthesis — Firecrawl: Web Scraper API for AI Agents (Search · Scrape · Agent · Change-Tracking)]]
[[src-notebooklm-claude-code-workflow|Synthesis — NotebookLM + Claude Code Workflow via notebooklm-py]]
[[src-obsidian-claude-code-second-brain|Synthesis — Obsidian + Claude Code Second Brain Setup]]
[[wsl2-development-patterns|WSL2 Development Patterns]]
[[zettelkasten-methodology|Zettelkasten Methodology]]
[[devops-control-plane|devops-control-plane]]
