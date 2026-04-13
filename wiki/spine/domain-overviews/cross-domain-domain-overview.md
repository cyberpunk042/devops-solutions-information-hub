---
title: Cross-Domain — Domain Overview
aliases:
  - "Cross-Domain — Domain Overview"
type: domain-overview
domain: cross-domain
layer: spine
status: synthesized
confidence: medium
maturity: growing
created: 2026-04-08
updated: 2026-04-13
sources: []
tags: [domain-overview, cross-domain]
---

# Cross-Domain — Domain Overview

## Summary

The cross-domain area is not a subject-matter domain but a structural layer — it holds concept pages, comparisons, patterns, decisions, and lessons that emerge from synthesizing across two or more subject domains. The domain folder contains 2 concept pages (Methodology Framework, Skyscraper Pyramid Mountain), while cross-domain content also lives in the wiki's evolved layers: 29 lesson pages (in lessons/), 6 pattern pages (in patterns/), 13 decision pages (in decisions/), and 5 comparison pages (in comparisons/ including 2 cross-domain ones). This is the domain where convergences, tradeoffs, and durable principles live — content no single-domain page can capture. Cross-domain synthesis is deliberately selective, representing only insights with multi-source validation.

> [!info] Domain at a glance
>
> | Metric | Value |
> |--------|-------|
> | Concept pages (in domain folder) | 2 |
> | Lesson pages (wiki-wide) | 29 |
> | Pattern pages (wiki-wide) | 6 |
> | Decision pages (wiki-wide) | 13 |
> | Comparison pages (wiki-wide) | 5 |

## State of Knowledge

> [!abstract] Cross-Domain Synthesis Is the Highest-Value Layer
> While the domain folder is small, the evolved layers (lessons, patterns, decisions) represent the highest synthesis quality in the wiki — convergences validated across multiple sources and domains.

**Authoritative coverage:**
- Methodology Framework — the meta-system for defining, selecting, and composing methodology models. Composable, recursive, transferable.
- Skills Architecture Patterns — synthesized from 8 sources across 3 ecosystems (Claude Code, Obsidian, NotebookLM). Convergent design principles (SKILL.md as universal format, three-layer stratification). Confidence: high.
- Plan Execute Review Cycle — pattern with 4 documented instances (OpenFleet orchestrator, Harness Engineering, Claude Code, Research Pipeline Orchestration). Confidence: high.
- Deterministic Shell LLM Core — pattern extracted from OpenFleet + devops-control-plane + harness engineering.

**Good coverage:**
- 29 lesson pages across all domains — covering convergences from multi-source validation (e.g., Never Skip Stages, CLI Beats MCP, Always Plan Before Executing, Models Are Systems Not Documents).
- 13 decision pages — concrete operational decisions with rationale and reversibility ratings.
- 6 pattern pages — including Progressive Distillation, Gateway-Centric Routing, Context-Aware Tool Loading, Scaffold-Foundation-Infrastructure-Features.
- Skyscraper Pyramid Mountain — architectural quality analogy for three structural states of a codebase.

**Thin coverage:**
- No principles page yet — the highest evolved layer (abstract, context-free principles derived from multiple patterns) has not been populated.
- The compounding knowledge principle (file answers back into the wiki) appears across multiple pages but has not been synthesized as a dedicated pattern.

## Maturity Map

| Maturity | Pages |
|----------|-------|
| **growing** (concept, 2) | Methodology Framework, Skyscraper Pyramid Mountain |

**Evolved layers (all growing maturity):**

| Layer | Count | Notable pages |
|-------|-------|---------------|
| Lessons | 29 | Never Skip Stages, CLI Beats MCP, Always Plan Before Executing, Models Are Systems Not Documents, Schema Is the Real Product, Never Synthesize from Descriptions Alone |
| Patterns | 6 | Plan Execute Review Cycle, Deterministic Shell LLM Core, Progressive Distillation, Gateway-Centric Routing, Context-Aware Tool Loading, Scaffold-Foundation-Infrastructure-Features |
| Decisions | 13 | MCP vs CLI, Obsidian vs NotebookLM, Stage-Gate Operational, Local Model vs Cloud API, Wiki-First with LightRAG Upgrade Path |
| Comparisons | 5 | Skills Architecture Patterns, Agentic Search vs Vector Search, Cross-Domain Patterns, LLM Wiki vs RAG |

All concept pages assigned maturity. All styled with callout vocabulary.

## Gaps

- **Principles layer (layer 7)**: The highest evolved layer is completely empty. Principles like "make intelligence persistent, not ephemeral" and "enforce at runtime, not by prompt" should be extractable from current content.
- **Local-first inference as ecosystem principle**: The "local inference when adequate, cloud inference when necessary" principle appears in AICP, OpenFleet, Local LLM Quantization, and Claude Code scheduling — a candidate for the first principles page.
- **The compounding knowledge principle**: Karpathy's insight that filing query answers back into the wiki compounds knowledge over time appears in LLM Wiki Pattern, Wiki Event-Driven Automation, and Memory Lifecycle Management. A cross-domain synthesis would make this actionable.
- **Pattern promotion pipeline**: 29 lessons exist but only 6 have been promoted to patterns. Systematic review of lessons for pattern candidates is overdue.

## Priorities

1. **First principles page** — Begin the principles layer with 2-3 abstract, durable insights extracted from the 6 existing patterns
2. **Local-first inference principle** — Synthesize from AICP + OpenFleet + Local LLM Quantization as a first principles page
3. **Compounding knowledge pattern** — Extract the file-answers-back pattern from LLM Wiki Pattern + Wiki Event-Driven Automation + Memory Lifecycle
4. **Pattern promotion review** — Systematically review 29 lessons for promotion to pattern candidates
5. **Promote agentic search comparison** — Sharpen decision criteria for Agentic Search vs Vector Search; promote to decision page

## Key Pages

1. **[Methodology Framework](../../domains/cross-domain/methodology-framework.md)** — The meta-system for defining, selecting, and composing methodology models across the ecosystem.
2. **[Skyscraper, Pyramid, Mountain](../../domains/cross-domain/skyscraper-pyramid-mountain.md)** — Architectural quality analogy: three structural states of a codebase (fragile, solid, organic).
3. **[Plan Execute Review Cycle](../../patterns/plan-execute-review-cycle.md)** — The most-validated pattern in the wiki. Four independent instances across OpenFleet, harness engineering, Claude Code, and the research pipeline.
4. **[Deterministic Shell LLM Core](../../patterns/deterministic-shell-llm-core.md)** — Use deterministic state machines for coordination, reserve LLM calls for reasoning.
5. **[Skills Architecture Patterns](../../comparisons/skills-architecture-patterns.md)** — Cross-ecosystem synthesis across Claude Code, Obsidian, and NotebookLM.
6. **[Decision: MCP vs CLI for Tool Integration](../../decisions/mcp-vs-cli-for-tool-integration.md)** — CLI + Skills beats MCP for token efficiency in interactive contexts.

## FAQ

### Q: Should I use MCP or CLI+Skills for tool integration?
Default to CLI+Skills for project-internal tooling — it is 12x cheaper in token cost and more accurate for known tasks. Use MCP for external service bridges and cross-conversation tool discovery. The decision is documented with full rationale. See [[mcp-vs-cli-for-tool-integration|Decision — MCP vs CLI for Tool Integration]].

### Q: What is the Plan-Execute-Review cycle and why does it appear across four independent projects?
It is the pattern where agents plan before acting, execute from the plan, then review the output against the original intent. It emerged independently in OpenFleet's orchestrator, harness engineering, Claude Code best practices, and the research pipeline — four independent instances of the same loop. This convergence is strong evidence it reflects a real constraint in LLM agent reliability. See [[plan-execute-review-cycle|Plan Execute Review Cycle]].

### Q: What is the Deterministic Shell LLM Core pattern?
Use a deterministic state machine (shell scripts, file reads, no LLM calls) for operational coordination — scheduling, routing, state tracking. Reserve LLM calls for actual reasoning work. This pattern appears in OpenFleet's 30s orchestrator, devops-control-plane's architecture, and harness engineering's enforcement hierarchy. See [[harness-owned-loop-deterministic-agent-execution|Harness-Owned Loop — Deterministic Agent Execution]].

### Q: What does "CLI tools beat MCP for token efficiency" mean in practice?
MCP servers add tool definitions to every message in the conversation, costing tokens continuously. CLI tools are called only when needed and cost tokens only at invocation. The empirical finding from harness engineering sources: CLI+Skills is approximately 12x more token-efficient than MCP for the same task. See [[cli-tools-beat-mcp-for-token-efficiency|CLI Tools Beat MCP for Token Efficiency]].

### Q: What is the "agentic search vs vector search" decision framework?
The choice depends on three variables: scale (< 200 pages favors agentic navigation), content change rate (high change rate favors agentic search because embeddings go stale), and structural organization (well-structured content favors navigation; unstructured content favors vectors). See [[agentic-search-vs-vector-search|Agentic Search vs Vector Search]].

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **Models covering this domain** | [[model-methodology|Model — Methodology]], [[model-knowledge-evolution|Model — Knowledge Evolution]] |
> | **Standards for this page type** | [[domain-overview-page-standards|Domain Overview Page Standards]] |
> | **Super-model (all models)** | [[super-model|Super-Model]] |
> | **System map** | [[methodology-system-map|Methodology System Map]] |
> | **Learning path** | [[methodology-fundamentals|Learning Path — Methodology Fundamentals]] |

## Relationships

- SYNTHESIZES FROM: AI Agents — Domain Overview
- SYNTHESIZES FROM: Knowledge Systems — Domain Overview
- SYNTHESIZES FROM: Tools And Platforms — Domain Overview
- SYNTHESIZES FROM: Automation — Domain Overview
- SYNTHESIZES FROM: Devops — Domain Overview
- SYNTHESIZES FROM: AI Models — Domain Overview

## Backlinks

[[ai-agents-domain-overview|AI Agents — Domain Overview]]
[[knowledge-systems-domain-overview|Knowledge Systems — Domain Overview]]
[[tools-and-platforms-domain-overview|Tools And Platforms — Domain Overview]]
[[automation-domain-overview|Automation — Domain Overview]]
[[devops-domain-overview|Devops — Domain Overview]]
[[ai-models-domain-overview|AI Models — Domain Overview]]
