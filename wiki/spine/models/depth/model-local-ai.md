---
title: Model — Local AI ($0 Target)
aliases:
  - "Model — Local AI ($0 Target)"
  - "Model: Local AI ($0 Target)"
type: concept
domain: cross-domain
layer: spine
status: synthesized
confidence: high
maturity: growing
created: 2026-04-09
updated: 2026-04-13
sources:
  - id: src-aicp-identity-profile
    type: wiki
    file: wiki/ecosystem/project_profiles/aicp/identity-profile.md
  - id: src-turboquant-122b-macbook
    type: wiki
    file: wiki/sources/tools-integration/src-turboquant-122b-macbook.md
    title: Synthesis — TurboQuant 122B on MacBook
tags: [model, concept, spine, local-ai, aicp, zero-cost, backend-routing, complexity-scoring, vram]
---

# Model — Local AI ($0 Target)
## Summary

The Local AI model describes how to reduce AI costs through local inference, model routing, and intelligent fallback — the principles apply regardless of which local inference stack you use. The core pattern is universal: score task complexity, route simple tasks to free local models, reserve expensive cloud APIs for complex reasoning. AICP is one implementation of these patterns; the framework transfers to any multi-model setup.

## Key Insights

- **The $0 target is achievable for routine operations, not all operations.** The routing split is not 100% local — it is local for mechanical tasks and cloud for reasoning tasks. The 80% Claude token reduction target means ~80% of invocations are free; the remaining ~20% (synthesis, evolution, architecture) still use Claude. This is the sustainable equilibrium, not a transitional phase.

- **AICP's complexity scorer is the production routing mechanism.** Every request is scored on task signals: deterministic output? validatable by downstream tools? short context window sufficient? If yes → LocalAI. If no → Claude. The thresholds are profile-configurable, not hardcoded. Profiles like `fleet-light` and `offline` push more to local; `thorough` and `code-review` push more to cloud.

- **Circuit breakers provide reliability without compromising the model.** Each backend (LocalAI, Claude) runs an independent circuit breaker in three states: CLOSED (healthy, route freely), OPEN (failed, route away), HALF_OPEN (recovering, probe cautiously). This means a LocalAI crash does not take down the ecosystem — requests fail over to Claude automatically and circuit closes again when LocalAI recovers.

- **9 loaded models cover distinct capability tiers.** The Qwen3 family (8B, 4B, 30B MoE, fast variant) covers most text tasks. The Gemma4 family (e2b, e4b, 26B MoE) adds multimodal and stronger agentic tool-calling — particularly Gemma 4 E4B's breakthrough reliable multi-step tool execution on 9.6GB. Legacy models (hermes, codellama) cover specialized domains. Embedding models (nomic-embed, bge-reranker) enable semantic search without cloud calls.

- **VRAM is the primary physical constraint.** The Gemma 4 26B model requires 18GB VRAM minimum. The current 8GB baseline makes it unrunnable. The planned upgrade to 19GB unlocks Stage 3: running complex agent reasoning locally, which is the step that moves the routing split from ~40% local to ~80% local.

- **Gemma 4 E4B's tool-calling reliability is the key capability breakthrough.** Prior local models failed unpredictably on multi-step agentic operations (tool calls, structured output, sequential reasoning). Gemma 4 E4B at 9.6GB changed this. It reliably executes multi-step tool sequences — meaning it can run the post-chain, invoke lint, scaffold pages, and update manifests without a human in the loop.

## Deep Analysis

### Generic Local Inference Patterns

The core question is: how do you split work between free local models and paid cloud APIs? Four patterns, from simplest to most sophisticated:

| Pattern | What It Does | When To Use |
|---------|-------------|-------------|
| Single local model | One model handles everything | Solo developer, simple tasks, cost = $0 |
| Router + fallback | Local for routine, cloud for complex | Medium scale, cost optimization |
| Tiered routing | Multiple local models by capability + cloud fallback | Fleet/production, quality-sensitive |
| Cloud-only with caching | No local models, cache frequent prompts | When hardware is limited |

### Local Inference Stack Options

| Stack | Strengths | Requirements |
|-------|-----------|-------------|
| Ollama | Simple setup, broad model support | 8GB+ VRAM |
| llama.cpp / MLX | Maximum performance, fine-tuning | Technical expertise |
| LocalAI | OpenAI-compatible API, drop-in replacement | Docker or bare metal |
| vLLM | Production-grade serving, batching | Varies by model, optimized for multi-GPU |
| LM Studio | GUI, easy model management | Desktop, not server |

### Universal Routing Invariants

These hold regardless of which stack or pattern you choose:

- **Complex reasoning, security review, and novel synthesis always route to cloud** — local models are not reliable enough for high-stakes judgment
- **Circuit breakers must be active on every backend** — no routing without health checks
- **The complexity scorer threshold is the routing mechanism** — not manual human selection
- **The $0 target applies to maintenance, not creation** — knowledge creation remains cloud; routine operations become free

---

### Instance — AICP Routing

> [!info] The following sections describe AICP's specific implementation of the routing patterns above. Your stack may use different models, different thresholds, and different infrastructure.

The [[aicp|AICP]] (AI Control Platform) is this ecosystem's orchestration layer: it scores task complexity, checks circuit breaker states, and routes deterministically-validatable tasks (status checks, index rebuilds, manifest regeneration, lint) to LocalAI, while reserving Claude for complex reasoning (architecture decisions, deep synthesis, security review).

### The 5-Stage LocalAI Independence Roadmap

[[aicp|AICP]] defines a concrete roadmap with current status:

> [!info] Roadmap status
>
> | Stage | Goal | Status |
> |-------|------|--------|
> | 1 | Make LocalAI functional — models loaded, GPU acceleration, health endpoint | Complete |
> | 2 | Route simple operations to LocalAI — complexity scorer implemented | Complete |
> | 3 | Progressive offload — heartbeats, reviews, status checks, index rebuilds | **Blocked: needs 19GB VRAM** |
> | 4 | Reliability and failover — circuit breakers tuned, DLQ implemented | Planned |
> | 5 | Near-independent operation — 80%+ Claude token reduction achieved | Target state |

Stage 1 and 2 are done. Stage 3 is the hardware-blocked inflection point. Until then, the system routes ~40% of operations locally; after the VRAM upgrade, target is ~80%.

### The Routing Decision Framework

The [[local-model-vs-cloud-api-for-routine-operations|Decision — Local Model vs Cloud API for Routine Operations]] formalizes the routing logic:

> [!tip] Route to LocalAI when:
> - Output is deterministically validatable (e.g., `tools.validate` will catch errors)
> - Task fits in a short context window (4K-8K tokens)
> - Task is mechanical and repeatable (manifest regeneration, lint, scaffold generation)
> - Latency matters more than quality (heartbeats, status polling)
> - Cost matters (batch operations over many wiki pages)

> [!warning] Route to Claude when:
> - Task requires novel cross-domain synthesis
> - Output is not externally validatable (architectural decisions, security review)
> - Context window is large (full codebase analysis, deep-dive evolution)
> - The task is a one-off judgment call rather than a routine operation
> - Stakes are high and failure is expensive

**The quality threshold is per-profile, not global.** The `fleet-light` profile aggressively pushes to local (threshold 0.3); `code-review` pulls toward cloud (threshold 0.8). A wiki post-chain run uses `fleet-light`; an evolution synthesis session uses `thorough`.

### The Backend Architecture

AICP's routing stack:

```
Request → Complexity Scorer → Profile Threshold Check
    ↓ below threshold           ↓ above threshold
  LocalAI Circuit Breaker     Claude Circuit Breaker
    ↓ CLOSED                    ↓ CLOSED
  LocalAI (free, fast)         Claude (paid, powerful)
    ↓ OPEN (circuit tripped)
  Fallback to Claude
```

The circuit breaker prevents cascading failures. If LocalAI becomes unavailable (model loading, GPU OOM, network issue on the OpenAI-compatible endpoint), the circuit trips, and all traffic flows to Claude until LocalAI recovers. This keeps the ecosystem operational even when the local backend is unhealthy.

### The 9 Loaded Models and Their Roles

The current model inventory reflects deliberate capability coverage:

- **Qwen3-8B** — General text tasks, fast inference, default routing target
- **Qwen3-4B** — Ultra-fast, for simple status checks and heartbeats
- **Qwen3-30B MoE** — Higher-quality reasoning locally, for tasks just below the cloud threshold
- **Qwen3-fast** — Optimized for latency-sensitive operations
- **Gemma4-E2B** — Lightweight multimodal
- **Gemma4-E4B** — Reliable multi-step tool calling (the Stage 3 unlock)
- **Gemma4-26B MoE** — Complex agent reasoning locally (blocked on 19GB VRAM)
- **Hermes-3B / CodeLlama** — Specialized legacy models
- **nomic-embed + bge-reranker** — Semantic search and reranking without cloud

### What Remains Cloud-Only

After Stage 5, these operations will still route to Claude:
- First-pass synthesis of novel concepts with no existing wiki coverage
- Cross-domain pattern recognition requiring >100K token context
- Security review of system architecture changes
- Evolution of seed pages to canonical status (judgment-heavy)
- Resolving contradictions between existing pages

The $0 target is for routine wiki maintenance and fleet operations, not for knowledge creation. Knowledge creation remains Claude's domain; maintenance becomes local's domain.

### Hardware Dependency and the Upgrade Path

> [!note] Personal context — this ecosystem's specific hardware situation
> The current baseline is 8GB VRAM with a planned upgrade to 19GB. AICP Stages 1-2 were built on 8GB intentionally to validate the routing model before investing in hardware. The 19GB upgrade enables Gemma4-26B MoE, simultaneous model loading, and Stage 3-4 progressive offload.

The general principle: build the routing infrastructure first, scale the hardware second. VRAM is the primary physical constraint for any local inference setup — it determines which models you can run and how many simultaneously. The routing architecture should be validated on minimal hardware before scaling up.

### Key Pages

| Page | Layer | Role in the model |
|------|-------|-------------------|
| [[aicp|AICP]] | concept | The orchestration and routing platform |
| [[local-llm-quantization|Local LLM Quantization]] | concept | How large models run on consumer hardware |
| [[local-model-vs-cloud-api-for-routine-operations|Decision — Local Model vs Cloud API for Routine Operations]] | decision | The formal routing decision framework |
| [[gateway-centric-routing|Gateway-Centric Routing]] | pattern | Architectural pattern for traffic routing |
| [[deterministic-shell-llm-core|Deterministic Shell, LLM Core]] | pattern | Wrapper pattern keeping LLM inside deterministic orchestration |

### Lessons Learned

| Lesson | What was learned |
|--------|-----------------|
| [[cli-tools-beat-mcp-for-token-efficiency|CLI Tools Beat MCP for Token Efficiency]] | Build routing infrastructure before scaling hardware. AICP Stages 1-2 were built on 8GB VRAM intentionally — validate the routing model before investing in hardware. |
| [[hardcoded-instances-fail-build-frameworks-not-solutions|Hardcoded Instances Fail — Build Frameworks Not Solutions]] | The $0 target applies to maintenance, not creation. The routing framework (complexity scoring → threshold → local/cloud) is the reusable pattern; AICP is one instance. |
| [[infrastructure-must-be-reproducible-not-manual|Infrastructure Must Be Reproducible, Not Manual]] | Circuit breakers, fallback chains, and health checks must be automated — manual intervention for local inference failures defeats the $0 target. |

### State of Knowledge

> [!success] Well-covered
> - The 5-stage roadmap with clear status per stage
> - Routing decision framework (when local vs cloud)
> - Circuit breaker reliability model (CLOSED/OPEN/HALF_OPEN)
> - The 9 loaded models and their distinct capability tiers

> [!warning] Thin or missing
> - Empirical routing split data (Stage 3 not yet operational)
> - Context window overflow handling strategy
> - Profile auto-selection logic (manual vs automatic per operation)

### How to Adopt

> [!info] What you need
> - LocalAI or compatible OpenAI-endpoint server running locally
> - AICP installed with complexity scorer and circuit breaker modules
> - At minimum 8GB VRAM for Stages 1-2; 19GB for Stage 3+
> - Routing profiles configured per operation type

> [!warning] Invariants (do not change per project)
> - Complex reasoning, security review, and novel synthesis always route to cloud
> - Circuit breakers must be active on every backend — no routing without health checks
> - The complexity scorer threshold is the routing mechanism, not manual selection

> [!tip] Per-project adaptations
> - Profile thresholds vary by risk tolerance (`fleet-light` at 0.3 vs `code-review` at 0.8)
> - Model selection depends on available VRAM and task mix
> - The "what remains cloud-only" list may shrink as local models improve

### Context Depth and Routing Tier Connection (NEW)

AICP's complexity scoring tiers (simple → moderate → complex → cloud-only) parallel the context engineering tier system (lightweight → capable → expert). The connection: a task routed to a local model should also receive LESS context (lightweight tier) because local models have smaller context windows and lower comprehension. A task routed to Claude (cloud) can receive full expert-tier context. This means routing decisions inform context injection depth — the two tier systems are complementary, not independent. See [[model-context-engineering|Model — Context Engineering]] for the tier definitions and [[tier-based-context-depth-trust-earned-through-approval-rates|Tier-Based Context Depth]] for trust-earned depth.

## Open Questions

> [!question] Empirical routing split after Stage 3
> The 80% target is an estimate. Actual measurement requires Stage 3 to be operational.

> [!question] ~~Can the post-chain run entirely on local models?~~
> **RESOLVED:** Post-chain is already pure Python — no LLM needed, already $0. Evolution pipeline can route to local models via AICP.
> Stage 3 targets this, but validation of complex relationship synthesis may still require Claude.

> [!question] Context window as a hidden routing constraint
> Qwen3-8B has a 32K context limit; tasks involving full wiki analysis exceed this. How should the router handle context overflow — split the task, or escalate to cloud?

> [!question] Profile auto-selection
> Should the pipeline auto-select the AICP profile based on the operation being run, or should profiles be set manually per session?

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **MCP and CLI integration** | [[model-mcp-cli-integration|Model — MCP and CLI Integration]] |
> | **Ecosystem architecture** | [[model-ecosystem|Model — Ecosystem Architecture]] |
> | **AICP project profile** | [[aicp|AICP]] |
> | **Automation pipelines** | [[model-automation-pipelines|Model — Automation and Pipelines]] |

## Relationships

- BUILDS ON: [[aicp|AICP]]
- BUILDS ON: [[local-llm-quantization|Local LLM Quantization]]
- FEEDS INTO: [[model-automation-pipelines|Model — Automation and Pipelines]]
- FEEDS INTO: [[model-quality-failure-prevention|Model — Quality and Failure Prevention]]
- RELATES TO: [[model-sfif-architecture|Model — SFIF and Architecture]]
- IMPLEMENTS: [[local-model-vs-cloud-api-for-routine-operations|Decision — Local Model vs Cloud API for Routine Operations]]
- COMPARES TO: [[gateway-centric-routing|Gateway-Centric Routing]]

## Backlinks

[[aicp|AICP]]
[[local-llm-quantization|Local LLM Quantization]]
[[model-automation-pipelines|Model — Automation and Pipelines]]
[[model-quality-failure-prevention|Model — Quality and Failure Prevention]]
[[model-sfif-architecture|Model — SFIF and Architecture]]
[[local-model-vs-cloud-api-for-routine-operations|Decision — Local Model vs Cloud API for Routine Operations]]
[[gateway-centric-routing|Gateway-Centric Routing]]
[[identity-profile|AICP — Identity Profile]]
[[model-notebooklm|Model — NotebookLM]]
