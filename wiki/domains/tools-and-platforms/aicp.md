---
title: AICP
aliases:
  - "AICP"
type: concept
layer: 2
maturity: growing
domain: tools-and-platforms
status: synthesized
confidence: authoritative
created: 2026-04-08
updated: 2026-04-13
sources:
  - id: src-aicp-local
    type: documentation
    project: aicp
    path: CLAUDE.md
    title: AICP — Local Project Documentation
    ingested: 2026-04-08
tags: [aicp, localai, ai-control-platform, backend-routing, think-edit-act, guardrails, circuit-breaker, fleet-integration, local-first]
---

# AICP

## Summary

AICP (AI Control Platform) is a personal AI control workspace that orchestrates local and cloud AI backends under user control. The core thesis: "You → AICP → (LocalAI | Claude Code) → Your Project." It is NOT the open-source LocalAI project itself, but a management layer built around LocalAI as the local inference engine. AICP provides unified CLI interaction with both LocalAI (local, free, fast) and Claude Code (cloud, powerful, paid), graduated permission modes (think/edit/act), automatic backend routing based on task complexity, guardrails for safe operation, circuit breakers for reliability, and a 5-stage roadmap toward LocalAI independence (80%+ Claude token reduction). Currently at 60 Python modules, 1,631 tests, 78 skills, with Stage 1 (LocalAI functional) complete and Stage 2 (routing) implemented.

## Key Insights

> [!info] Backend routing with complexity scoring
>
> | Mode | What Gets Routed Where |
> |------|----------------------|
> | **Think** | Read-only — safest, cheapest local models |
> | **Edit** | Read + write allowed paths — local for simple, Claude for complex |
> | **Act** | Read + write + execute — full capabilities, Claude preferred |
>
> Auto mode: score complexity → check circuit breaker → apply profile thresholds → select backend → failover chain. 70-80% of routine operations run locally for free.

> [!tip] 5-stage LocalAI independence roadmap
> (1) Make LocalAI functional ✅ (2) Route simple operations to LocalAI ✅ (3) Progressive offload (heartbeats, reviews, status) (4) Reliability & failover (5) Near-independent: 80%+ Claude token reduction.

- **9 loaded models**: Qwen3 family (8B, 4B, 30B MoE, fast variant), Gemma4 family (e2b, e4b, 26B MoE), legacy (hermes, codellama), specialized (whisper, piper, nomic-embed, bge-reranker, stablediffusion). All running on LocalAI v4.0.0 with GPU acceleration.

- **Guardrails pipeline**: Path protection (forbids .env, *.key, .ssh/), response filtering (detects leaked AWS keys, JWTs, GitHub PATs, bearer tokens), pre/post execution checks. Safety is enforced at the framework level, not the model level.

- **11 MCP tools**: chat, vision, transcribe, speak, voice pipeline, route, deep health, profile, kb search, task status, DLQ status. Exposed as MCP server for IDE clients and fleet agents.

- **Profile system**: Config load order: default.yaml → profile.yaml → user config → project config → CLI flag. 9 operational presets (default, fast, offline, thorough, code-review, fleet-light, reliable, dual-gpu, benchmark). Profiles control backends, router thresholds, mode sampling, RAG, budget, cache, timeouts.

- **Fleet integration**: AICP works ON the fleet project (point at ../openfleet/). Skills produced become fleet project code. At runtime, fleet agents use AICP's circuit breaker and routing for backend selection. 78 skills in .claude/skills/, 18 referenced in fleet's agent-tooling.yaml.

- **Reliability patterns from Claude Code's architecture**: Circuit breaker, startup warmup, deep health endpoint, dead-letter queue (DLQ), persistent metrics, health reports, event emitter, tool safety metadata, task lifecycle tracking, memory relevance scoring, microcompaction, skill model override, auto-memory extraction, away summary.

## Deep Analysis

### The Backend Routing Decision

The router is the core value proposition. It decides for every request:
1. Score task complexity (keywords, history, context size)
2. Check circuit breaker state for each backend
3. Apply profile thresholds (e.g., fast profile routes more to LocalAI)
4. Select backend (local → LocalAI hermes-3b/qwen3-8b, complex → Claude)
5. Failover chain if selected backend is down

This means 70-80% of routine operations (status checks, simple edits, heartbeat processing) can run locally for free, while complex reasoning (architecture decisions, security reviews, deep analysis) escalates to Claude.

### The "Not LocalAI" Distinction

A critical clarification: AICP is not LocalAI. LocalAI is the open-source LLM inference server (OpenAI-compatible API, GGUF models, GPU acceleration). AICP is the orchestration layer that makes LocalAI (or Claude Code, or both) work seamlessly in a multi-agent context. AICP adds: permission enforcement, backend routing, guardrails, profiles, fleet integration, MCP exposure, metrics, and reliability patterns. LocalAI provides the raw inference capability.

### Dual-Machine Target Architecture

```
Machine 1 (Alpha)              Machine 2 (Bravo)
├── LocalAI Cluster + GPU      ├── LocalAI Cluster + GPU
├── OpenClaw Gateway + MC      ├── OpenClaw Gateway + MC
├── Fleet Daemons              ├── Fleet Daemons
└── 10 Alpha-prefixed agents   └── 10 Bravo-prefixed agents

P2P LocalAI peering between clusters
Shared: Plane, GitHub, ntfy
```

## Open Questions

- What is the actual token cost reduction at Stage 2 vs Stage 1? (Requires: empirical measurement from AICP telemetry comparing API costs before and after the routing implementation; not documented in existing wiki pages)
- How does the dual-machine architecture handle split-brain scenarios? (Requires: external research on distributed orchestration and P2P LocalAI peering failure modes; the Four-Project Ecosystem page notes the dual-machine Alpha+Bravo target but does not document split-brain handling)

### Answered Open Questions

**Q: Can AICP's router be exposed as an MCP tool so other projects (research wiki) can use backend routing?**

Cross-referencing `OpenFleet` and `Four-Project Ecosystem`: the answer is yes — and it is already partially implemented. The `AICP` page (this page) documents that AICP exposes 11 MCP tools, and one of them is explicitly named `route`. This means the backend routing decision (LocalAI vs Claude, complexity scoring, circuit breaker evaluation) is already an MCP-callable operation. The `Four-Project Ecosystem` page documents the integration architecture: the research wiki exports knowledge to docs/kb/ (AICP consumes it), and AICP's 11 MCP tools are "exposed as MCP server for IDE clients and fleet agents." The `OpenArms` page confirms the mcporter bridge as the mechanism for connecting MCP servers across projects — the same pattern applies to the research wiki. The research wiki's own CLAUDE.md registers its MCP server in `.mcp.json` and lists `wiki_post` as a tool that can trigger pipeline operations. The practical implementation path: the research wiki's ingestion pipeline can invoke AICP's `route` MCP tool to select whether a given synthesis task (complex deep analysis vs simple index update) should use a local model or Claude. This routing is the exact mechanism that supports the "evolution pipeline AICP backend" documented in the `Knowledge Evolution Pipeline` page: "Routes through the devops AI control platform, enabling integration with the OpenFleet agent fleet. An AICP agent can run evolution as part of a sprint task."

**Q: What quality threshold determines when LocalAI output is "good enough" vs needs Claude escalation?**

Cross-referencing `Knowledge Evolution Pipeline` and `Immune System Rules`: the threshold is not a single fixed value but a configurable profile-based decision governed by two mechanisms. First, AICP's router uses complexity scoring (keywords, history, context size) with configurable thresholds per profile — the 9 operational presets (default, fast, offline, thorough, code-review, fleet-light, reliable, dual-gpu, benchmark) each encode different routing biases. The "thorough" profile routes more to Claude; "fleet-light" routes more to LocalAI. Second, the `Knowledge Evolution Pipeline` page documents the human-in-the-loop checkpoint: the `--review` flag surfaces pages where "LLM-generated content may benefit from curator validation" — this is the quality gate for evolved pages, placed at the growing→mature transition. The implicit threshold from cross-referencing: LocalAI output is "good enough" for tasks where the output can be deterministically validated (index updates, manifest regeneration, lint checks, simple summarization) or where a human review gate exists downstream. LocalAI output requires Claude escalation when the task involves: architectural decisions, security analysis, novel cross-domain synthesis, or deep analysis where errors would be silent (no downstream validation gate). The `Immune System Rules` page confirms this principle: "A deterministic security scan cannot be social-engineered via a crafted task description. An LLM-based security layer can be prompted around" — quality-critical operations should not rely solely on LocalAI without either deterministic validation or human review.

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **What principle applies?** | [[right-process-for-right-context-the-goldilocks-imperative|Principle — Right Process for Right Context — The Goldilocks Imperative]] |
> | **What is my identity?** | [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]] |
> | **System map** | [[methodology-system-map|Methodology System Map]] |

## Relationships

- USED BY: [[openfleet|OpenFleet]]
- BUILDS ON: [[lightrag|LightRAG]]
- RELATES TO: [[claude-code|Claude Code]]
- RELATES TO: [[openclaw|OpenClaw]]
- ENABLES: [[claude-code-skills|Claude Code Skills]]
- FEEDS INTO: [[wiki-knowledge-graph|Wiki Knowledge Graph]]
- RELATES TO: [[devops-control-plane|devops-control-plane]]

## Backlinks

[[openfleet|OpenFleet]]
[[lightrag|LightRAG]]
[[claude-code|Claude Code]]
[[openclaw|OpenClaw]]
[[claude-code-skills|Claude Code Skills]]
[[wiki-knowledge-graph|Wiki Knowledge Graph]]
[[devops-control-plane|devops-control-plane]]
[[ai-model-provider-harness-decision-matrix-2026|AI Model × Provider × Harness Decision Matrix 2026]]
[[identity-profile|AICP — Identity Profile]]
[[context-management-is-primary-productivity-lever|Context Management Is the Primary LLM Productivity Lever]]
[[local-model-vs-cloud-api-for-routine-operations|Decision — Local Model vs Cloud API for Routine Operations]]
[[deterministic-shell-llm-core|Deterministic Shell, LLM Core]]
[[E002-ecosystem-integration|Ecosystem Integration Interfaces]]
[[four-project-ecosystem|Four-Project Ecosystem]]
[[gateway-centric-routing|Gateway-Centric Routing]]
[[immune-system-rules|Immune System Rules]]
[[knowledge-evolution-pipeline|Knowledge Evolution Pipeline]]
[[E001-local-inference-engine|Local Inference Engine (Subsystem 3)]]
[[local-llm-quantization|Local LLM Quantization]]
[[local-training-playbook-2026|Local Training Playbook 2026 — Wiki Alignment, Tool Calls, Semantic Enhancement]]
[[mcp-integration-architecture|MCP Integration Architecture]]
[[model-ecosystem|Model — Ecosystem Architecture]]
[[model-local-ai|Model — Local AI ($0 Target)]]
[[multi-channel-ai-agent-access|Multi-Channel AI Agent Access]]
[[openarms|OpenArms]]
[[plane|Plane]]
[[profile-as-coordination-bundle|Profile as Coordination Bundle]]
[[scaffold-foundation-infrastructure-features|Scaffold → Foundation → Infrastructure → Features]]
[[second-brain-custom-model-strategy|Second-Brain Custom Model — Training Strategy and Roadmap]]
[[2026-04-17-session-summary|Session 2026-04-17 Summary]]
[[skills-architecture-is-dominant-extension-pattern|Skills Architecture Is the Dominant LLM Extension Pattern]]
[[src-27-questions-llm-selection|Source — 27 Questions to Ask Before Choosing an LLM]]
[[src-airllm-layer-wise-inference-nvme-ssd-offload|Synthesis — AirLLM: Layer-Wise Inference with NVMe SSD Offload]]
[[src-claude-code-harness-features|Synthesis — Claude Code Harness: Skills, Hooks, Plugins, Subagents, MCP (2026)]]
[[src-gemma4-searxng-openclaw|Synthesis — Gemma 4 + SearXNG for Free Private OpenClaw]]
[[src-inference-provider-landscape-2026|Synthesis — Inference Provider Landscape 2026 (OpenRouter, Together, Groq, Cerebras, DeepInfra, Ollama Cloud, Direct APIs)]]
[[src-codex-cli-and-claude-code-plugin|Synthesis — OpenAI Codex CLI and the Codex Plugin for Claude Code]]
[[src-opencode-harness-features|Synthesis — OpenCode Harness: Build/Plan Modes, LSP, Multi-Session, AGENTS.md, 75+ Providers (2026)]]
[[src-turboquant-122b-macbook|Synthesis — TurboQuant 122B LLM on MacBook]]
[[src-gpt-oss-openai-open-weight-moe|Synthesis — gpt-oss: OpenAI's Apache-2.0 Open-Weight MoE Models (20b + 120b)]]
[[T001-test-openai-backend|Test OpenAI backend with LocalAI]]
[[2026-consumer-hardware-ai-stack|The 2026 Consumer-Hardware AI Stack — Strategic Synthesis]]
