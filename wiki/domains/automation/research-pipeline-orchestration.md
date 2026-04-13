---
title: Research Pipeline Orchestration
aliases:
  - "Research Pipeline Orchestration"
type: concept
layer: 2
maturity: growing
domain: automation
status: synthesized
confidence: medium
created: 2026-04-08
updated: 2026-04-10
sources:
  - id: src-user-directive-ecosystem
    type: notes
    file: raw/notes/2026-04-08-user-directive-ecosystem-connections.md
    title: User Directive — Ecosystem Connections & Automation Vision
    ingested: 2026-04-08
  - id: src-user-directive-integration
    type: notes
    file: raw/notes/2026-04-08-user-directive-integration-vision.md
    title: User Directive — Integration Vision & Service Architecture
    ingested: 2026-04-08
tags: [pipeline, orchestration, automation, chain-operations, group-operations, tree-operations, research-automation, ingestion, multi-pass]
---

# Research Pipeline Orchestration

## Summary

Research Pipeline Orchestration is the architectural vision for automating the research wiki's knowledge acquisition process from manual ingestion to autonomous chain/group/tree operations. The user directive states: "I should be able to add a list of things to research online and/or local in order to automate my needs, however many pipelines or pipelines options we need. And we need to automate what can be automated and group them and make sequence / chain and group call / trees operations in order to always move toward the targets and offload as much as possible the repetitive task." This vision transforms the wiki from a manually-fed knowledge base into a self-extending research engine with multiple pipeline types, parallel execution, and iterative deepening.

## Key Insights

> [!info] Three operation modes that compose
>
> | Mode | How It Works | When to Use |
> |------|-------------|-------------|
> | **Chain/Sequence** | A → B → C, each step feeds the next | Dependent steps (extract before analyze) |
> | **Group/Parallel** | A + B + C simultaneously, results merged | Independent inputs (12 URLs at once) |
> | **Tree** | Branch into parallel paths, merge at synthesis | Topic → 3 sources → merge into synthesis |

> [!abstract] Five pipeline types
>
> | Pipeline | Stages |
> |----------|--------|
> | **Online Research** | web_search → fetch → save_raw → extract → synthesize → integrate |
> | **Local Ingestion** | scan_project → extract_docs → classify → create_pages → integrate |
> | **Cross-Reference** | load_manifest → gap_analysis → relationship_discovery → integrate |
> | **Deepening** | lint_report → identify_thin → research_gaps → enrich → integrate |
> | **Ecosystem Sync** | detect_changes → diff → update_or_create → cross_reference → integrate |

**Multi-pass ingestion is fundamental.** The user directive: "ingestion is multi-pass, not one-shot" — extract → cross-reference → identify gaps → deepen. The current 2-pass implementation is the beginning, not the end.

**Research lists as input.** Submit URLs, topics, or local paths. The system classifies (URL → online research, path → local ingestion, topic → web search + ingest) and routes to the right chain automatically.

**Offload repetitive work.** "Offload as much as possible the repetitive task." Auto-validate, auto-index, auto-manifest, auto-stale-check — all currently manual post-ingestion steps become pipeline stages.

## Deep Analysis

### Pipeline Architecture Vision

```
Input Layer:
  URL list, topic list, local paths, Obsidian web clips, NotebookLM exports

Routing:
  classify_input() → select_pipeline() → configure_chain()

Pipeline Types:
  1. ONLINE RESEARCH:     web_search → fetch → save_raw → extract → analyze → synthesize → write → integrate
  2. LOCAL INGESTION:     scan_project → extract_docs → classify → create_pages → cross_reference → integrate
  3. CROSS-REFERENCE:     load_manifest → gap_analysis → relationship_discovery → update_pages → integrate
  4. DEEPENING:           lint_report → identify_thin → research_gaps → enrich → validate → integrate
  5. ECOSYSTEM SYNC:      detect_changes → diff → update_or_create → cross_reference → integrate

Execution Modes:
  - Sequential:  for dependent steps (extract must finish before analyze)
  - Parallel:    for independent inputs (ingest 12 URLs simultaneously)
  - Tree:        for branching research (topic → 3 sources → merge into synthesis)

Post-Pipeline (always):
  update_indexes → regenerate_manifest → validate → regenerate_wikilinks → report
```

### Integration with Existing Tools

| Pipeline Stage | Current Tool | Enhancement Needed |
|---------------|-------------|-------------------|
| Fetch URLs | tools/ingest.py | Already automated |
| Fetch topics | WebSearch + WebFetch | Needs pipeline wrapper |
| Scan local projects | Agent (Explore) | Needs automated trigger |
| Extract pages | Claude Code (manual) | Needs skill-driven automation |
| Validate | tools/validate.py | Already automated |
| Manifest | tools/manifest.py | Already automated |
| Wikilinks | tools/obsidian.py | Already automated |
| Lint/gaps | tools/lint.py | Already automated |
| Export | tools/export.py | Already automated |
| Cross-reference | Claude Code (manual) | Needs Pass N automation |

### From CLI Tools to Pipeline Engine

The gap between current state and the vision:
1. **Current**: Each tool is a standalone CLI command. The wiki-agent skill describes the workflow. Claude Code executes it manually.
2. **Target**: A pipeline engine that chains tools automatically: `pipeline run online-research --input urls.txt` → fetch all → ingest all → cross-reference → validate → report.
3. **Implementation path**: Python orchestrator (tools/pipeline.py) that composes existing tools into chains, with parallel execution via asyncio and progress tracking.

## Open Questions

- How to handle pipeline failures mid-chain (e.g., one URL fails to fetch — skip or retry)? (Requires: external research on asyncio error handling patterns and retry strategies; not directly covered in existing wiki pages)
- How does the pipeline interact with NotebookLM's research agent (notebooklm source add-research)? (Requires: external research on notebooklm-py API specifics; not covered in existing wiki pages)

### Answered Open Questions

> [!example]- Python CLI or MCP server for the pipeline engine?
> CLI Python script (tools/pipeline.py) is correct. MCP schema overhead is paid on every message even in conversations not involving the pipeline; CLI invokes zero overhead when not called. An MCP wrapper can be added later for cross-conversation discoverability without changing the CLI-primary model.

> [!example]- Right granularity for parallelism?
> **Parallel per-URL** during fetch+extract (each source is independent). **Sequential** within cross-reference and integration phases (dependencies between pages). Not per-page (cross-referencing introduces dependencies). Not per-domain (requires knowledge of all domain pages). OpenFleet caps parallel dispatch at 2 per cycle; similar cap recommended.

> [!example]- Can subagents do parallel page synthesis?
> Yes, with explicit scope boundaries. Each subagent receives one raw source file, produces one wiki page — well-bounded. Parent validates each page via `tools/validate.py` before integration. Use CLI tools (not MCP) in subagents — fresh context windows don't need MCP schema overhead.

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **What principle applies?** | [[right-process-for-right-context-the-goldilocks-imperative|Principle — Right Process for Right Context — The Goldilocks Imperative]] |
> | **What is my identity?** | [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]] |
> | **System map** | [[methodology-system-map|Methodology System Map]] |

## Relationships

- BUILDS ON: [[wiki-ingestion-pipeline|Wiki Ingestion Pipeline]]
- BUILDS ON: [[wiki-event-driven-automation|Wiki Event-Driven Automation]]
- ENABLES: [[llm-wiki-pattern|LLM Wiki Pattern]]
- RELATES TO: [[ai-driven-content-pipeline|AI-Driven Content Pipeline]]
- RELATES TO: [[claude-code-scheduling|Claude Code Scheduling]]
- RELATES TO: [[mcp-integration-architecture|MCP Integration Architecture]]
- RELATES TO: [[obsidian-cli|Obsidian CLI]]
- RELATES TO: [[notebooklm-py-cli|notebooklm-py CLI]]

## Backlinks

[[wiki-ingestion-pipeline|Wiki Ingestion Pipeline]]
[[wiki-event-driven-automation|Wiki Event-Driven Automation]]
[[llm-wiki-pattern|LLM Wiki Pattern]]
[[ai-driven-content-pipeline|AI-Driven Content Pipeline]]
[[claude-code-scheduling|Claude Code Scheduling]]
[[mcp-integration-architecture|MCP Integration Architecture]]
[[obsidian-cli|Obsidian CLI]]
[[notebooklm-py-cli|notebooklm-py CLI]]
[[agent-orchestration-patterns|Agent Orchestration Patterns]]
[[always-plan-before-executing|Always Plan Before Executing]]
[[automated-knowledge-validation-prevents-wiki-decay|Automated Knowledge Validation Prevents Silent Wiki Decay]]
[[context-aware-tool-loading|Context-Aware Tool Loading]]
[[cross-domain-patterns|Cross-Domain Patterns]]
[[local-model-vs-cloud-api-for-routine-operations|Decision — Local Model vs Cloud API for Routine Operations]]
[[mcp-vs-cli-for-tool-integration|Decision — MCP vs CLI for Tool Integration]]
[[polling-vs-event-driven-change-detection|Decision — Polling vs Event-Driven Change Detection]]
[[wiki-first-with-lightrag-upgrade-path|Decision — Wiki-First with LightRAG Upgrade Path]]
[[deterministic-shell-llm-core|Deterministic Shell, LLM Core]]
[[gateway-centric-routing|Gateway-Centric Routing]]
[[harness-engineering|Harness Engineering]]
[[knowledge-evolution-pipeline|Knowledge Evolution Pipeline]]
[[agent-orchestration-is-highest-connected-concept|Lesson — Agent Orchestration Is the Highest-Connected Concept in the Wiki]]
[[automation-is-bridge-between-knowledge-and-action|Lesson — Automation Is the Bridge Between Knowledge and Action]]
[[knowledge-systems-is-foundational-domain|Lesson — Knowledge Systems Is the Foundational Domain for the Entire Wiki]]
[[model-automation-pipelines|Model — Automation and Pipelines]]
[[multi-channel-ai-agent-access|Multi-Channel AI Agent Access]]
[[multi-stage-ingestion-beats-single-pass|Multi-Stage Ingestion Beats Single-Pass Processing]]
[[openarms|OpenArms]]
[[para-methodology|PARA Methodology]]
[[plan-execute-review-cycle|Plan Execute Review Cycle]]
[[rework-prevention|Rework Prevention]]
[[second-brain-architecture|Second Brain Architecture]]
[[src-context-mode|Synthesis — Context Mode — MCP Sandbox for Context Saving]]
[[src-notebooklm-claude-code-workflow|Synthesis — NotebookLM + Claude Code Workflow via notebooklm-py]]
[[src-playwright-cli-vs-mcp|Synthesis — Playwright CLI vs MCP — Automate QA with Less Tokens]]
[[src-superpowers-end-of-vibe-coding|Synthesis — Superpowers Plugin — End of Vibe Coding (Full Tutorial)]]
[[the-wiki-is-a-hub-not-a-silo|The Wiki Is a Hub, Not a Silo]]
[[wsl2-development-patterns|WSL2 Development Patterns]]
[[wiki-backlog-pattern|Wiki Backlog Pattern]]
