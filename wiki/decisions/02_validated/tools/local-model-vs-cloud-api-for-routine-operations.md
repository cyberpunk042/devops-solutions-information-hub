---
title: Decision — Local Model vs Cloud API for Routine Operations
aliases:
  - "Decision — Local Model vs Cloud API for Routine Operations"
  - "Decision: Local Model vs Cloud API for Routine Operations"
type: decision
domain: ai-agents
layer: 6
status: synthesized
confidence: high
maturity: growing
derived_from:
  - "AICP"
  - "Local LLM Quantization"
  - "Knowledge Evolution Pipeline"
reversibility: easy
created: 2026-04-08
updated: 2026-04-10
sources:
  - id: src-aicp-local
    type: documentation
    file: ../devops-expert-local-ai/CLAUDE.md
    title: AICP — Local Project Documentation
tags: [aicp, localai, claude, routing, local-first, cost-optimization, backend-selection, complexity-scoring, wiki-pipeline]
---

# Decision — Local Model vs Cloud API for Routine Operations
## Summary

For routine wiki and devops operations, use local models (LocalAI/AICP) for mechanical, deterministic, and output-validatable tasks; use Claude (cloud API) for reasoning-heavy synthesis, evolution, and cross-referencing tasks. AICP's complexity-scoring router is the production mechanism that operationalizes this split — it routes automatically based on task signals rather than requiring manual backend selection per invocation.

## Decision

> [!success] Route by task complexity, not by preference
> **Use local models for mechanical operations. Use Claude for reasoning operations. Let AICP route automatically via complexity scoring.**

Concretely:

- **Local model (LocalAI via AICP)**: manifest regeneration, lint checks, index rebuilds, scaffold generation, status checks, heartbeat processing, simple summarization, embedding generation. These tasks have deterministic validation downstream — if the output is wrong, `tools.validate` will catch it.

- **Claude (cloud API via AICP)**: page synthesis, cross-domain relationship discovery, evolution generation (seed → growing → mature), gap analysis requiring judgment, deep analysis sections, contradiction resolution, decision and pattern page generation. These tasks have no downstream validator — quality errors are silent.

- **Routing mechanism**: AICP's complexity scorer analyzes task keywords, history depth, and context size, then applies profile thresholds to select the backend. The "thorough" profile routes more to Claude; the "fleet-light" profile routes more to LocalAI. For the wiki pipeline specifically, `python3 -m tools.pipeline post` operations are local-model candidates; `pipeline evolve --auto --backend aicp` delegates backend selection to AICP's router.

## Alternatives

### Alternative 1: All-Cloud (Claude for Everything)

Use Claude for every wiki operation — manifest rebuilds, lint, scaffold generation, and synthesis alike. **Rejected** because it is unnecessary expensive for mechanical operations. The AICP page documents the 5-stage LocalAI independence roadmap targeting 80%+ Claude token reduction. Running `tools.manifest`, `tools.lint`, and `tools.validate` through Claude consumes paid API tokens for operations that a deterministic Python script or a 3B local model handles identically. At Stage 2 of AICP's roadmap (already implemented), 70–80% of routine operations route to LocalAI for free. All-cloud eliminates this cost optimization entirely.

### Alternative 2: All-Local (LocalAI for Everything)

Run every wiki operation through LocalAI — including synthesis, evolution, and cross-referencing. **Rejected** because local model quality is insufficient for high-stakes generation tasks where errors are silent. The AICP page's answered Open Question on quality thresholds is explicit: "LocalAI output requires Claude escalation when the task involves: architectural decisions, security analysis, novel cross-domain synthesis, or deep analysis where errors would be silent (no downstream validation gate)." Local LLM quantization quality degrades at lower bit-widths for reasoning tasks, and even Gemma4 26B has not yet replaced Claude for complex fleet tasks in the current ecosystem configuration. All-local produces plausible-looking but subtly incorrect synthesis that accumulates into wiki quality degradation.

### Alternative 3: Hybrid with Manual Backend Selection

Choose the backend manually per invocation — explicitly pass `--backend localai` or `--backend claude` to every pipeline command. **Rejected** because it is operationally tedious and degrades to inconsistency in practice. When the routing decision must be made explicitly for every `pipeline evolve` or `pipeline chain` invocation, operators will default to a single backend rather than reasoning about complexity per task. AICP's router was built precisely to remove this decision from the hot path: it evaluates complexity signals automatically and applies profile-based thresholds consistently. Manual selection is appropriate only for one-off overrides (e.g., `--backend claude` for a specific high-stakes evolution run), not as the default operating mode.

## Rationale

The core insight from the AICP page's Deep Analysis section is that the routing decision is a solved problem — AICP's complexity scorer classifies tasks reliably enough to support a 5-stage independence roadmap targeting 80% Claude token reduction. The task taxonomy is consistent across all ecosystem projects: mechanical/deterministic tasks (status checks, heartbeats, simple edits) are LocalAI-appropriate because their outputs are either validated downstream or inherently low-risk. Reasoning tasks (synthesis, architecture decisions, cross-domain analysis) require Claude because their quality cannot be verified by a downstream deterministic check.

This split is not unique to the wiki. The OpenFleet page documents the same principle at the fleet level: "LocalAI (hermes-3b for queries, bge-m3 for embeddings) handles routine work. Claude handles complex reasoning. Silent heartbeats for idle agents save 70% cost." The Local LLM Quantization page confirms that even Gemma4 E4B (9.6GB, phone-scale) reliably handles multi-step tool calling for simple agent tasks — the capability floor for local models on mechanical operations is now very low.

The quality threshold is the key discriminator. LocalAI output is "good enough" when either: (a) the task has a deterministic validator downstream (manifest, lint, validate — all return non-zero on errors), or (b) a human review gate exists upstream of any downstream consumers. LocalAI output requires Claude escalation when quality errors would be silent — no validator, no review gate, errors propagate directly into the wiki graph. Evolution pages, synthesis pages, and cross-reference updates fall into this category.

The Knowledge Evolution Pipeline confirms that the `--review` flag is the human-in-the-loop checkpoint placed at the growing→mature transition precisely because LLM-generated content may need curator validation before promotion. For local-model-generated content, this review gate is even more important as a quality backstop.

## Reversibility

**Easy to reverse.** The routing split is implemented as AICP profile configuration — changing the complexity thresholds in a profile YAML file adjusts the local/cloud boundary without modifying any pipeline code. If VRAM upgrades or new local model releases (Qwen3 30B MoE, future Gemma releases) improve local reasoning quality sufficiently, the "thorough" profile thresholds can be adjusted to route more synthesis tasks locally. The migration path is purely configuration: no wiki pages need updating, no pipeline code changes, no infrastructure teardown. The two backends (LocalAI and Claude) already run simultaneously in the AICP dual-backend setup.

The one risk: if local model quality issues produce a batch of subtly incorrect evolution pages before being caught, those pages must be regenerated with Claude. The review gate (`pipeline evolve --review`) is the mitigation — it surfaces generated content before maturity promotion, containing the blast radius of quality issues to the seed/growing tier rather than allowing them to reach canonical status.

## Dependencies

**Downstream effects of this decision:**

- **AICP profile configuration**: The "thorough" and "fleet-light" profiles control routing thresholds. Wiki pipeline invocations that use `--backend aicp` inherit the active profile's thresholds. Profile selection for wiki operations should be documented in the wiki's operational runbook.
- **Pipeline evolve commands**: `pipeline evolve --auto --backend aicp` delegates backend selection to AICP's router. `pipeline evolve --auto --backend claude-code` bypasses the router and always uses Claude. The default for high-stakes evolution (maturity promotion candidates) should be `--backend claude-code` until AICP's routing is empirically validated on wiki synthesis tasks.
- **Post-chain operations**: `python3 -m tools.pipeline post` (validate, manifest, lint, index rebuild) are all local-model or pure-Python candidates — no Claude API calls needed for routine post-ingestion maintenance.
- **Cost tracking**: AICP's telemetry tracks API costs per backend. Monitoring the actual token cost reduction at Stage 2 vs Stage 1 would validate whether the routing is functioning as designed (target: 80%+ reduction from pre-routing baseline).
- **Hardware dependency**: The local model routing assumes LocalAI is running with adequate VRAM. The hardware upgrade (8GB→19GB VRAM) documented in the project memory directly expands which models can be routed locally. This decision should be revisited as hardware changes.

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **What routing system operationalizes this?** | [[aicp|AICP]] |
> | **What model does this feed?** | [[model-local-ai|Model — Local AI ($0 Target)]] |
> | **What evolution pipeline depends on this?** | [[knowledge-evolution-pipeline|Knowledge Evolution Pipeline]] |
> | **What quantization research informs quality thresholds?** | [[local-llm-quantization|Local LLM Quantization]] |
> | **Where does this fit?** | [[methodology-system-map|Methodology System Map]] |

## Relationships

- DERIVED FROM: [[aicp|AICP]]
- DERIVED FROM: [[local-llm-quantization|Local LLM Quantization]]
- DERIVED FROM: [[knowledge-evolution-pipeline|Knowledge Evolution Pipeline]]
- RELATES TO: [[openfleet|OpenFleet]]
- RELATES TO: [[research-pipeline-orchestration|Research Pipeline Orchestration]]
- ENABLES: [[knowledge-evolution-pipeline|Knowledge Evolution Pipeline]]
- FEEDS INTO: [[wiki-knowledge-graph|Wiki Knowledge Graph]]
- RELATES TO: [[infrastructure-as-code-patterns|Infrastructure as Code Patterns]]

## Backlinks

[[aicp|AICP]]
[[local-llm-quantization|Local LLM Quantization]]
[[knowledge-evolution-pipeline|Knowledge Evolution Pipeline]]
[[openfleet|OpenFleet]]
[[research-pipeline-orchestration|Research Pipeline Orchestration]]
[[wiki-knowledge-graph|Wiki Knowledge Graph]]
[[infrastructure-as-code-patterns|Infrastructure as Code Patterns]]
[[E001-local-inference-engine|Local Inference Engine (Subsystem 3)]]
[[model-knowledge-evolution|Model — Knowledge Evolution]]
[[model-local-ai|Model — Local AI ($0 Target)]]
