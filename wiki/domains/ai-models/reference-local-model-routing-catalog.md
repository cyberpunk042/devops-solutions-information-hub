---
title: Local Model Routing Catalog (task × hardware tier)
aliases:
  - "Local Model Routing Catalog"
  - "Complexity-Routed Model Selection Matrix"
type: reference
layer: 2
maturity: seed
domain: ai-models
status: processing
confidence: medium
created: 2026-07-02
updated: 2026-07-02
sources:
  - id: note-operator-model-routing-catalog-2026-07-02
    type: note
    file: raw/notes/2026-07-02-operator-model-routing-catalog-handwritten-verbatim.md
    title: Operator handwritten model-routing catalog (verbatim)
    ingested: 2026-07-02
tags: [ai-models, model-routing, complexity-routing, ternary, bitnet, 1bit, local-inference, aicp, hardware-tier, model-selection, cpu-inference, rtx-4090, rtx-pro, evolving]
---

# Local Model Routing Catalog (task × hardware tier)

> [!warning] Evolving catalog — not canonical
> This is an **operator-authored, tentative** routing catalog captured
> 2026-07-02 (*"new stuff are being added and we need to adapt and stay
> flexible on this side too"*). Entries carry alternatives (`ou` = "or"),
> hardware-tier splits, and uncertain readings (`[?]`). It is a **living
> selection matrix**, not a fixed spec — models are added/swapped as the
> local-inference landscape moves. Verbatim source:
> `raw/notes/2026-07-02-operator-model-routing-catalog-handwritten-verbatim.md`.

> [!note] Machine-readable source of truth
> This page is the human narrative. The **structured, extensible registry** that
> holds the fleet — **models**, **group models** (MoE / merged / replicated),
> and **routing profiles** — lives as config in
> [`wiki/config/model-catalog/`](../../config/model-catalog/README.md). Adding a
> model is a one-line data edit there; `tools/validate_model_catalog.py` checks
> every group member and profile selection resolves. Current fleet: **55 models
> (38 ternary/BitNet), 3 group models, 10 profiles.** Reality-check status
> (HF-verified 2026-07-02): **11 real · 18 aspirational · 26 unverified**, of
> which **14 are base-backed** (real upstream confirmed, ternary quant is the
> only open step). Notable real find: `prism-ml/Ternary-Bonsai` is a genuine
> HF line (1.7B/4B/8B — no 70B). See `wiki/config/model-catalog/VERIFICATION-LOG.md`.

## Summary

A complexity-routed **model selection matrix** for $0 local inference: which
local model to run for a given **task type** (coding, chat, analysis, agents,
orchestration, plus scientific and specialist workloads) on a given **hardware
tier** (CPU · RTX 4090 · RTX Pro). The catalog is weighted heavily toward
**ternary / BitNet-1.58-bit** quantized weights, which is what makes 70B–120B
models tractable on consumer/prosumer GPUs and even CPU. It is the concrete
routing table AICP (the complexity-routed local-inference project) implements;
the wiki holds it as evolving knowledge so the structure flexes as models change.

## Routing by task × hardware tier (Image 1)

| Task | CPU | RTX 4090 | RTX Pro |
|---|---|---|---|
| **Default / coding** | — | Qwen-Coder Ternary — 1.5B inline completion + 14B chat & refactoring; RLM-Code-Reasoner-8B; Thinking-Machines-Interaction-1B | BitNet-70B (1.58b) [Instruct / 120B]; Llama3-8B-Ternary; Mistral-2B-Ternary [?]; Prism-ML-Ternary-Bonsai-70B; Deepseek-V3-Ternary (PT²-LLM) |
| **General CPU** | TernLM-3-8B-Instruct-1.58b; BGE-M3 (embedding); Phi-3-Mini-Ternary | — | — |
| **Orchestrator** | Gemma-4-LiteRt-2B; Spectra-TriLM-3.9B; TernaLM3-15B-Instruct | — | — |
| **Analysis** | — | — | BitNet-70B-132k-context |
| **Agents** | TernaryLM-132M *ou* TRM-Recursive-Reasoner | Llama-3-Tiny-3B + Mistral-Tiny-3B; Nexus-Spec-1.1B; Deepseek-R1-Ternary-8B | Mistral-Ternary-3×70B |

## Scientific workloads (Image 2)

| Domain | RTX 4090 | RTX Pro |
|---|---|---|
| **DNA / genomics** | Evo (Arc Institute) *ou* HyenaDNA | RoseTTAFold All-Atom (RFAA) |
| **Protein folding** | AlphaFold3 (*ou* ESMFold *ou* OpenFold) | AlphaFold3 |
| **Particle / physics sim** | Warp-Lang (NVIDIA) | Warp-Lang (NVIDIA) |

## Reasoning / validation cluster (boxed group, Image 2)

- Document-Ternary-3B
- Recursive-Ref-Validator-2B
- Llama-3-thought-8B
- OpenThinking-7B

## Mergekit — mass model-merging pool (Image 2)

Candidate bases for `mergekit`-style ternary/1.58-bit merges:

- Ent/it[?] Qwen2.5-32B-trit-uniform
- PrismML: Ternary Bonsai
- 1bitLLM/bitnet-b1.58-large
- Xinyuan/T-MoE-8×7B
- tiiuae/Falcon3-10B-1.58bit-prequantized-6f16 (*ou* Falcon-E-3B)
- Zihan Wang 314/coe [?]
- Qwen2.5-Coder-72B (1.58b)
- Bash-Tiny-Coder-1B · Flex-Prompt-Tiny-1B · Security-Phi-3-Mini · StarCoder2-3B

## Specialist models (right column, Image 2)

| Specialty | Model |
|---|---|
| Kernel / low-level | Linux-Kernel-Tiny-1.5B |
| Math | BitNet-Math-Expert-30B |
| UI | Tiny-Ternary-UI-3B |
| Coordination | Hive-Gate-7B |
| Logic validation | TRM-Logic-Validator-2B; Logic-Loop-8B |
| Security | OWASP-Ternary-3B; HackerLM-tiny-3B |
| Long context | LLaMA-Ternary-Context-1B |
| Code | CodeLlama-Ternary-34B |
| Large general | Mistral-Large-Ternary-80B |

## Key Insights

- **Two routing axes, not one.** Selection is `task_type × hardware_tier` — the
  same task maps to a different model on CPU vs 4090 vs RTX Pro. This is the
  local-inference analogue of complexity-routing: match the smallest sufficient
  model for the task to the tier that can hold it.
- **Ternary / 1.58-bit is the enabler.** Nearly every large entry (70B, 80B,
  120B, 132k-context) is ternary/BitNet-quantized — that is what puts 70B+ on a
  single prosumer GPU and 8B on CPU. Ties directly to
  [[concept-1bit-ternary-weights]] and [[local-llm-quantization]].
- **Tiny models for hot paths.** Inline completion (1.5B), agents (3B tiny),
  embedding (BGE-M3), and 132M/recursive-reasoner fallbacks keep latency-
  sensitive and CPU-only paths cheap.
- **The catalog is a moving target.** `ou`-alternatives and scribbled sizes are
  intentional — treat it as a live selection surface to re-baseline, not a fixed
  registry. Staying flexible on the structure IS the requirement.

## Relationships

- BUILDS ON [[concept-1bit-ternary-weights]] — ternary/BitNet weights are what make the 70B–120B tiers here runnable locally.
- RELATES TO [[local-llm-quantization]] — the quantization techniques (MLX, GGUF, prequantized 1.58-bit) behind these model entries.
- FEEDS INTO AICP (complexity-routed local inference) — this is the routing table AICP implements to hit the $0 local-inference target.
