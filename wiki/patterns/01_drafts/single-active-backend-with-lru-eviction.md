---
title: "Single-Active Backend with LRU Eviction"
aliases:
  - "Single-Active Backend with LRU Eviction"
type: pattern
domain: cross-domain
layer: 5
status: synthesized
confidence: high
maturity: seed
derived_from:
  - model-local-ai
  - localai-over-ollama-vllm-for-multi-model-orchestration
instances:
  - page: "AICP LocalAI runtime (baseline 8 GB single-GPU)"
    context: "MAX_ACTIVE_BACKENDS=3 with LRU eviction (GPU model + nomic-embed CPU + bge-reranker CPU). Switching from qwen3-8b to gemma4-e4b evicts the LRU model."
  - page: "AICP dual-GPU profile (19 GB total)"
    context: "`config/profiles/dual-gpu.yaml` keeps MAX=3 even with more VRAM. Constraint is application coherence, not raw VRAM — predictable warm cache + single cold-start cost per swap beats maximizing concurrent loads."
  - page: "LocalAI v4.x watchdog"
    context: "LOCALAI_WATCHDOG_IDLE=15m + LOCALAI_WATCHDOG_BUSY=10m. Health-based eviction complements LRU's usage-based eviction; stuck backends can't pin a slot indefinitely."
  - page: "AICP `default` profile parallelism"
    context: "LLAMACPP_PARALLEL=2 × CONTEXT_SIZE=16384 → 8192 per slot. Fast profile uses PARALLEL=4 + CONTEXT=8192 → 2048 per slot. The parallelism knob shapes the slot; MAX_ACTIVE_BACKENDS bounds how many slots coexist."
created: 2026-04-18
updated: 2026-04-18
sources:
  - id: aicp-compose
    type: file
    file: docker-compose.yaml
    description: "LocalAI container with LOCALAI_MAX_ACTIVE_BACKENDS=3 + watchdog config (AICP project)"
  - id: aicp-models-config
    type: directory
    file: config/models/
    description: "14 model YAMLs — only ONE chat-class GPU model can be active at a time even with MAX=3 (the other 2 slots are CPU embedding + reranker) (AICP project)"
  - id: aicp-contribution-staging
    type: wiki
    file: raw/articles/from-aicp/patterns/01_drafts/single-active-backend-with-lru-eviction.md
    description: "AICP's original submission, 2026-04-18 staged in raw/ before ingestion here"
tags: [pattern, gpu, vram, eviction, lru, backend, local-ai, aicp, transferable]
contributed_by: "aicp"
contribution_source: "/home/jfortin/devops-expert-local-ai"
contribution_date: "2026-04-18"
contribution_status: accepted
---

# Single-Active Backend with LRU Eviction

## Summary

When multi-model AI inference is constrained by a fixed resource (VRAM, RAM, file handles, license seats) that any one model consumes a SIGNIFICANT fraction of, the right runtime pattern is **single-active per resource class with LRU (least-recently-used) eviction**: only one model per resource class is loaded at a time; switching models forces an eviction; eviction is automatic per usage history. This is what makes a 9-model library viable on a single 8 GB GPU. The pattern composes with classes — AICP runs ONE chat-GPU-model + ONE CPU embedder + ONE CPU reranker simultaneously (`MAX_ACTIVE_BACKENDS=3`), each in its own resource class, LRU-evicted within its class. The pattern's correctness does NOT depend on resource size: 19 GB dual-GPU AICP still uses single-active because the relevant constraint is application coherence (predictable warm-paths), not just raw VRAM.

> [!info] Pattern Reference Card
>
> | Component | Role | Why it must be single-active |
> |-----------|------|-----------------------------|
> | GPU chat model (e.g., qwen3-8b) | The reasoning workhorse | One full GGUF load saturates the GPU; concurrent loads OOM |
> | CPU embedder (e.g., nomic-embed) | Vector search / RAG | Different resource class (CPU+RAM vs GPU); can run alongside |
> | CPU reranker (e.g., bge-reranker) | Result reranking | Different resource class again; alongside embedder + GPU model |
> | LRU eviction policy | When MAX_ACTIVE_BACKENDS reached, oldest is evicted | Predictable VRAM bound + predictable warm cache for recent models |
> | Watchdog (idle / busy) | Auto-evict stuck or long-idle backends | Complements LRU with crash recovery |

## Pattern Description

**Single-active per resource class** is a runtime constraint: at any moment, at most ONE backend per (resource-class, capability) tuple is loaded. When a new request needs a different backend in the same class, the old backend is evicted before the new one loads. **LRU eviction** is the policy: when a slot is needed, the least-recently-used backend in that class is the one to go.

> [!warning] Recognition signal — a system that "supports N models" but M < N can be loaded simultaneously
>
> Example: a 9-model library on 8 GB VRAM. Each model is 2-7 GB. Math: ~2 small models or 1 medium model per GPU. The system either rejects requests for models that don't fit (bad UX) or evicts a loaded model to make room (LRU). Single-active is the latter.

A correct implementation has 4 properties:

1. **Atomic switch** — eviction completes before the new backend starts loading. No two backends in the same class concurrently allocate the constrained resource.
2. **Predictable warm vs cold timing** — recently-used backends serve warm requests in milliseconds; freshly-loaded backends pay the full cold-start cost (10-80 s for GGUF + GPU upload, per AICP measurements). The pattern doesn't HIDE the cold start — it makes it predictable per usage history.
3. **Configurable concurrency per class** — `MAX_ACTIVE_BACKENDS=3` in AICP means one slot per class (chat + embed + rerank). A different deployment with fewer classes might use MAX=1; a richer deployment might use MAX=5.
4. **Watchdog complement** — LRU evicts based on USAGE; watchdog evicts based on HEALTH (stuck, idle too long, busy too long). Both are necessary; LRU alone leaks stuck-but-recently-used backends, watchdog alone permits unbounded growth.

> [!abstract] The constraint determines the resource class
>
> | Resource class | Constraint | Examples |
> |----------------|-----------|----------|
> | GPU VRAM | One large model saturates | LocalAI chat models (qwen3-8b, gemma4-e4b, llava) |
> | CPU + RAM | Often non-blocking; multiple can coexist | nomic-embed, bge-reranker, phi-2 (CPU fallback) |
> | License seats | API tokens with concurrent-call limits | Some cloud APIs; not yet relevant to AICP |
> | File handles / sockets | OS-level limits | Usually plentiful; not a typical class for inference |

The pattern PARTITIONS by class: same class → single-active; different classes → can coexist. AICP's 14 models partition as: 7 GPU-class chat models (one slot, LRU among them), nomic-embed (one CPU-embed slot), bge-reranker (one CPU-rerank slot), several CPU fallbacks sharing a slot via lazy load.

## Instances

### Instance 1 — AICP LocalAI baseline (8 GB single-GPU)

`docker-compose.yaml` sets `LOCALAI_MAX_ACTIVE_BACKENDS=3`. Active simultaneously: ONE GPU chat model + ONE CPU embedder + ONE CPU reranker. Switching from `qwen3-8b` to `gemma4-e4b` (for vision) evicts qwen3-8b (LRU within the GPU-chat class). Cold-start cost: ~10-80 s per swap; warm inference: 1-1.2 s. Keeps the 7-class library coherent on 8 GB.

### Instance 2 — LocalAI v4.x watchdog

`LOCALAI_WATCHDOG_IDLE=true LOCALAI_WATCHDOG_IDLE_TIMEOUT=15m` + `LOCALAI_WATCHDOG_BUSY=true LOCALAI_WATCHDOG_BUSY_TIMEOUT=10m`. Health-based eviction complements LRU's usage-based eviction. Without watchdog, a stuck backend pinning a slot would block all requests in that class until manual restart. With watchdog, eviction is automatic; next request triggers a fresh load.

### Instance 3 — `config/profiles/default.yaml` LLAMACPP_PARALLEL=2

Per-backend parallelism × per-slot context = effective per-request VRAM. AICP's `default` profile: PARALLEL=2 + CONTEXT_SIZE=16384 → 8192 tokens per slot. A `fast` profile might set PARALLEL=4 + CONTEXT=8192 → 2048 per slot. Both stay within MAX_ACTIVE_BACKENDS=3 — the parallelism knob tunes the slot SHAPE, not whether backends coexist.

### Instance 4 — `config/profiles/dual-gpu.yaml` (19 GB dual-GPU upgrade)

RTX 2080 8 GB + RTX 2080 Ti 11 GB. One could naively set MAX_ACTIVE_BACKENDS=6 to "use all the VRAM." The dual-gpu profile keeps MAX=3 because: (a) coherence — knowing which model is active matters for routing, (b) cold-start cost stays the same per swap, so preventing swap thrash is more valuable than maximizing concurrent loads, (c) the new resource (11 GB second GPU) is used to load LARGER models (qwen3-30b-a3b MoE needs 18 GB), not more concurrent ones. Pattern correctness is independent of resource size; what changes is which models fit.

## When To Apply

- Multi-model AI inference where any single model consumes a significant fraction of a fixed resource (typical: GPU VRAM, sometimes RAM)
- Library size > capacity (more models defined than can fit simultaneously)
- Workload mix: requests come for different models over time, but each request typically uses one model end-to-end (not pipelining 5 models per request)
- Cold-start cost is acceptable amortized over a session (warm hits dominate after first request to each model)
- Operator wants predictable VRAM bound — never OOM, even under load

## When Not To

- **Single-model deployment** — if only one model runs, single-active is trivially satisfied and the pattern adds no value
- **Small enough models that all fit** — 5 models × 1 GB + 16 GB VRAM → just load all of them; eviction adds latency for no benefit
- **Latency-critical workload that can't pay cold-start** — real-time voice with 50 ms budgets needs one-model-per-instance (vLLM-style), accept higher hardware cost
- **Pipelined multi-model requests** — embed → rerank → chat in parallel for ONE request needs all participating models always-loaded
- **Stateful sessions across many models** — if a user pings A, B, C, A, B, C... single-active will thrash. Pin those always-loaded OR redesign to batch by model

## Tradeoffs

> [!warning] The single-active cost
>
> | Cost | Mitigation |
> |------|-----------|
> | Cold-start latency on first request to a new model (10-80 s) | Warmup at deploy: pre-load expected models at startup. AICP's `reliable` profile uses `warmup.models: [qwen3-8b, nomic-embed]` |
> | Thrashing if request mix alternates between many GPU models | Routing policy keeps requests on the same model when possible (router's complexity-tier selection has hysteresis); operator picks profile matching workload |
> | Loss of warm cache when a model is evicted | LRU keeps RECENTLY-used models warm; cold ones go first. Profile choice tunes which models are recently-used |
> | Predictable cost upper bound but no SAVINGS from idle compute | If GPU sits idle 90% of the time with one model loaded, that VRAM is "wasted" relative to a system that could swap in another workload. AICP accepts this — predictability beats marginal utilization |

## Relationships

- BUILDS ON: [[model-local-ai|Model — Local AI ($0 Target)]] (VRAM as primary constraint)
- RELATES TO: [[localai-over-ollama-vllm-for-multi-model-orchestration|Decision — LocalAI over Ollama / vLLM]] (single-active is the runtime pattern that LocalAI's MAX_ACTIVE_BACKENDS implements; vLLM's "one model per instance" is the OPPOSITE pattern, valid in different contexts)
- RELATES TO: [[profile-as-coordination-bundle|Profile as Coordination Bundle]] (profiles tune CONTEXT_SIZE, LLAMACPP_PARALLEL, warmup model list per workload)
- COMPLEMENTS: [[per-backend-circuit-breaker-with-failover-chain|Per-Backend Circuit Breaker with Failover Chain]] (when a model swap times out, the breaker prevents repeated swap-attempt cascades)
- ENABLES: AICP's $0 target on consumer hardware

## Backlinks

[[model-local-ai|Model — Local AI ($0 Target)]]
[[Decision — LocalAI over Ollama / vLLM]]
[[profile-as-coordination-bundle|Profile as Coordination Bundle]]
[[per-backend-circuit-breaker-with-failover-chain|Per-Backend Circuit Breaker with Failover Chain]]
[[AICP's $0 target on consumer hardware]]
[[per-backend-circuit-breaker-with-failover-chain|Per-Backend Three-State Circuit Breaker with Failover-Chain Integration]]
