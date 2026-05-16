---
title: "Inference Backend Stack — LocalAI vs vLLM vs llama.cpp vs SGLang vs Ollama vs Custom Direct Stack for SAIN-01"
aliases:
  - "Inference Backend Comparison"
  - "Q-017 Inference Stack Comparison"
  - "Direct Stack vs LocalAI Abstraction"
  - "Per-Tier Hardware Exploitation vs Unifying Abstraction"
type: comparison
layer: 3
maturity: growing
domain: ai-models
status: synthesized
confidence: high
created: 2026-05-16
updated: 2026-05-16
sources:
  - id: localai-docs
    type: documentation
    url: "https://localai.io/"
    title: "LocalAI documentation"
  - id: vllm-docs
    type: documentation
    url: "https://docs.vllm.ai/en/latest/"
    title: "vLLM documentation"
  - id: llama-cpp
    type: documentation
    url: "https://github.com/ggerganov/llama.cpp"
    title: "llama.cpp on GitHub"
  - id: bitnet-cpp
    type: documentation
    url: "https://github.com/microsoft/BitNet"
    title: "microsoft/BitNet bitnet.cpp"
  - id: sglang-docs
    type: documentation
    url: "https://github.com/sgl-project/sglang"
    title: "SGLang on GitHub"
  - id: ollama
    type: documentation
    url: "https://ollama.ai/"
    title: "Ollama"
  - id: src-bitnet
    type: wiki
    file: "wiki/sources/src-bitnet-b158-ternary-llm.md"
  - id: src-dflash
    type: wiki
    file: "wiki/sources/src-dflash-block-diffusion-spec-dec.md"
  - id: src-zen5
    type: wiki
    file: "wiki/sources/src-zen5-avx512-single-cycle.md"
  - id: src-sain01
    type: wiki
    file: "wiki/sources/src-sain-01-sovereign-node-spec.md"
  - id: cmp-ling-nemotron
    type: wiki
    file: "wiki/comparisons/cmp-ling-26-flash-vs-nemotron-3-nano-omni.md"
  - id: sovereign-os-sdd-011
    type: project
    project: cyberpunk042/sovereign-os
    path: docs/sdd/011-inference-backend-stack.md
  - id: operator-q017-directive
    type: directive
    file: "raw/notes/2026-05-16-user-directive-sovereign-os-arc-opening-limit-continuation.md"
tags:
  - comparison
  - inference-backend
  - localai
  - vllm
  - llama-cpp
  - bitnet-cpp
  - sglang
  - ollama
  - direct-stack
  - q-017
  - sovereign-os-arc
  - sain-01
  - srp-trinity
  - per-tier-hardware
  - layer-3
---

# Inference Backend Stack — LocalAI vs vLLM vs llama.cpp vs SGLang vs Ollama vs Custom Direct Stack for SAIN-01

## Summary

The operator's 2026-05-16 directive ("I dont even know if we can stick with LocalAI I think would limite us") opened Q-017. This page compares six candidate inference stacks against ten SAIN-01-specific criteria and presents the rationale for sovereign-os's chosen **direct-stack architecture** (no unifying abstraction by default; per-tier hardware exploitation).

**Headline result**: For SAIN-01's [[concept-srp-trinity-pulse-weaver-auditor|SRP Trinity]] (Pulse / Logic Engine / Oracle Core) where each tier maps to specific hardware ([[concept-dual-ccd-cache-partitioning-9900x|Zen 5 CCD 0]] / [[concept-vfio-gpu-isolation-amd-iommu|3090 VFIO]] / Blackwell host-resident), **a unifying abstraction (LocalAI) actively erases the architectural value the hardware provides**. The optimal stack is per-tier-native: `bitnet.cpp` on Pulse, `vLLM` on Logic + Oracle (with [[src-dflash-block-diffusion-spec-dec|DFlash drafts]] on Oracle), plus a thin OpenAI-compatible router for clients that need a single endpoint.

For the operator's `old-workstation` profile (constrained 11 GB RAM + 8 GB GPU), LocalAI or `llama.cpp`-via-Ollama is appropriate — the hardware doesn't reward per-tier specialization.

## Comparison Matrix

> [!abstract] Six candidates × ten SAIN-01-specific criteria

| Dimension | LocalAI | vLLM | llama.cpp | bitnet.cpp | SGLang | Ollama |
|---|---|---|---|---|---|---|
| **AVX-512 VNNI ternary inference** ([[concept-1bit-ternary-weights]]) | ✗ (abstracted; kernel choice hidden) | ✗ (GPU-only) | ★★ (CPU support but no TL2 packed kernels) | ★★★★★ (TL2 + I2_S kernels; first-class) | ✗ (GPU-only) | ✗ (wraps llama.cpp) |
| **DFlash block-diffusion spec-dec** ([[src-dflash-block-diffusion-spec-dec]]) | ★ (uncertain backend support) | ★★★★★ (v0.20.1+ native via `--speculative-config`) | ✗ | ✗ | ★★★ (Z-Lab supports SGLang backend) | ✗ |
| **Tensor-parallel Blackwell + 3090** | ★★★ (delegates to vLLM under hood) | ★★★★★ (`--tensor-parallel-size` first-class) | ★★★ (cuda_layers split possible) | ✗ (CPU-only) | ★★★★ (RadixAttention + TP) | ★★ (single-GPU primary) |
| **Constrained / structured output (JSON-mode / grammar)** | ★★★ (depends on backend) | ★★★ (guided_json supported) | ★★ (GBNF grammar) | ✗ | ★★★★★ (RadixAttention + per-rule generation; SGLang's strength) | ★★ |
| **[[concept-vfio-gpu-isolation-amd-iommu\|VFIO sandbox]] compatibility (3090 isolated)** | ★★★★ (runs in container; sandbox-compatible) | ★★★★★ (podman + CUDA_VISIBLE_DEVICES) | ★★★★ (same) | n/a (CPU-only) | ★★★★ (same) | ★★★★ (containerized) |
| **Pulse-tier sub-ms branching latency** | ✗ (abstraction-layer overhead) | ✗ (GPU dispatch latency dominates) | ★★★ (CPU but no packed kernels) | ★★★★★ (purpose-built for low-latency on CPU) | ✗ | ✗ |
| **Operator-direct observability** | ★ (single endpoint hides per-tier behavior) | ★★★★ (per-process metrics + logs) | ★★★★ (CLI flags expose everything) | ★★★★ (CLI flags + per-batch logging) | ★★★★ (logs + Prometheus) | ★★★ (CLI shows status) |
| **Sovereignty (no phone-home; operator-pulled)** | ★★★ (Go binary; some optional telemetry) | ★★★★ (Python + CUDA; no phone-home by default) | ★★★★★ (C++ binary; no telemetry; static link possible) | ★★★★★ (same as llama.cpp; MS-research-origin but no phone-home) | ★★★★ (no phone-home) | ★★★★ (Ollama Cloud is separate product; local Ollama is sovereign) |
| **Per-tier hardware exploitation** (Q-017 core question) | ✗ (abstraction erases per-tier choice) | ★★★★★ (each instance pinned to hardware) | ★★★★ (per-instance config) | ★★★★★ (CPU-CCD-pinned by design) | ★★★★ (per-instance) | ★★★ (single backend primary) |
| **Boot/install footprint** | ★★ (Go binary + many backends bundled) | ★★ (Python + CUDA runtime; large) | ★★★★★ (single C++ binary; minimal) | ★★★★ (small binary; minimal deps) | ★★ (Python + CUDA) | ★★★★ (Go binary; bundles llama.cpp) |

> [!success] Per-tier-native stack dominates SAIN-01's specific dimensions
>
> The dimensions where SAIN-01's architecture creates value — AVX-512 VNNI ternary, DFlash spec-dec, tensor-parallel, sub-ms branching, per-tier hardware exploitation — are exactly where the unifying abstraction (LocalAI) scores ★ or ✗. The dimension where LocalAI was supposed to win (operational uniformity) is replaced for SAIN-01 by a thin OpenAI-compatible router that preserves per-tier hardware exploitation underneath.

## Key Insights

> [!abstract] Six insights driving Q-017 resolution

> [!warning] An abstraction layer's price is paid in the dimension it abstracts
>
> LocalAI's value proposition is "one API, many backends." For a developer workstation running mixed workloads with no architectural commitments, that's compelling. For SAIN-01 — where the hardware exists *because* a specific software architecture (the [[concept-srp-trinity-pulse-weaver-auditor|SRP Trinity]]) demanded it — the abstraction layer erases the per-tier specialization that justified the hardware purchase. "Stick with LocalAI" means architecturally not using the [[concept-dual-ccd-cache-partitioning-9900x|Zen 5 CCD 0]]'s [[src-zen5-avx512-single-cycle|single-cycle 512-bit AVX-512]] for what makes it valuable.

> [!tip] The router-not-abstraction pattern preserves OpenAI-compatible UX without per-tier loss
>
> sovereign-os's `scripts/inference/router.py` (per [[sovereign-os-sdd-011|SDD-011]]) classifies each request by shape (model id; code/math markers; long context; JSON-mode; tools) and routes deterministically to one of Pulse / Logic Engine / Oracle Core. The router speaks OpenAI on the client side but **does not hide backend selection** — operators read the classify() function and know exactly where each request goes. This is the "have-both-cake-and-eat-it" pattern: client uniformity without operational opacity.

> [!info] DFlash availability locks vLLM as Oracle Core
>
> Per [[src-dflash-block-diffusion-spec-dec|DFlash synthesis]], Z-Lab's pre-trained DFlash draft checkpoints integrate via vLLM's `--speculative-config` flag (vLLM v0.20.1+). LocalAI doesn't expose this. llama.cpp doesn't support DFlash. SGLang has growing support but isn't the operator's first surface for production. For SAIN-01 Oracle Core, vLLM is uncontroversial.

> [!tip] Pulse's ternary CPU path locks bitnet.cpp
>
> Per [[src-bitnet-b158-ternary-llm|BitNet synthesis]], the only inference framework targeting AVX-512 VNNI VPDPBUSD packed ternary kernels (TL2 on x86) is `bitnet.cpp`. Pulse runs `microsoft/bitnet-b1.58-2B-4T` at 5-7 tok/sec on CPU CCD 0 — non-negotiable for the SRP Trinity's vector-core role. Any other backend gives up the AVX-512 win.

> [!info] llama.cpp is the right fallback (not the primary)
>
> When the operator's profile is `old-workstation` (constrained-resource: 11 GB RAM + 8 GB GPU), there's no Trinity to honor. A single-backend stack is correct. llama.cpp's portability + minimal install footprint + wide model support makes it the right choice there. For SAIN-01 it serves as a non-DFlash fallback when vLLM isn't suitable.

> [!info] Operational uniformity ≠ unifying abstraction
>
> The operator's expressed need ("one endpoint") is satisfied by a thin router (sovereign-os ships ~200 LOC of pure Python). The operator's expressed concern ("LocalAI will limit us") is about per-tier hardware exploitation, which an abstraction layer erases. These are reconcilable by **routing without abstracting**.

## Deep Analysis

### Why LocalAI scores poorly on SAIN-01 (not poorly in general)

LocalAI is a strong general-purpose backend gateway. The criteria where it loses on SAIN-01 are SAIN-01-specific:

| Criterion | Why LocalAI loses |
|---|---|
| AVX-512 VNNI ternary | LocalAI's backend matrix exposes bitnet.cpp as one option among many; per-tier-pin to CCD 0 + TL2 kernel selection + cores-0-5 affinity sit outside its abstraction shape |
| DFlash spec-dec | DFlash's vLLM `--speculative-config` flag isn't surfaced through LocalAI's OpenAI shim cleanly |
| Per-tier hardware exploitation | LocalAI's "one endpoint, dispatch by model_id" hides whether a request goes to CPU or GPU, which CCD, which IOMMU group |
| Pulse latency | The dispatcher adds milliseconds; Pulse needs sub-millisecond branching for state-routing decisions |

For a workstation running a single mid-size GPU and a casually-mixed workload, none of these matter and LocalAI's operational uniformity wins. For SAIN-01, all four are load-bearing.

### Why the operator's instinct ("LocalAI will limit us") is correct

The operator articulated the concern verbatim in `raw/notes/2026-05-16-user-directive-sovereign-os-arc-opening-limit-continuation.md`:

> "we aim another level and I dont even know if we can stick with LocalAI I think would limite us, but you will find the answers and the solutions."

The "another level" matters. SAIN-01's hardware was procured because the architectural design demanded **direct exploitation** of specific properties: [[src-zen5-avx512-single-cycle|Zen 5's single-cycle AVX-512 + VNNI]], the [[concept-dual-ccd-cache-partitioning-9900x|dual-CCD partition for SRP isolation]], the [[concept-vfio-gpu-isolation-amd-iommu|VFIO sandbox boundary]], and [[concept-zfs-tiered-storage-llm-inference|ZFS sync=always atomic state-handoffs]]. An abstraction that says "any backend can serve any tier" undoes the design — the hardware purchase no longer matches the software architecture.

The "find the answers" matters. The answer isn't "drop LocalAI"; it's "**route, don't abstract**." A thin router preserves the operator's stated client-side uniformity goal without compromising per-tier exploitation.

### The direct-stack architecture (sovereign-os SDD-011)

Per [[sovereign-os-sdd-011|sovereign-os SDD-011]], the recommended stack is:

```
                            sovereign-os router (~200 LOC Python)
                            scripts/inference/router.py
                            (OpenAI-compatible client surface)
                                       │
              ┌────────────────────────┼────────────────────────┐
              ▼                        ▼                        ▼
     ┌──────────────────┐  ┌──────────────────┐    ┌──────────────────┐
     │  Pulse (CCD 0)   │  │ Logic Engine     │    │  Oracle Core     │
     │  bitnet.cpp      │  │  vLLM on 3090    │    │  vLLM on Blackwell│
     │  cores 0-5 pin   │  │  (VFIO sandbox)  │    │  (BF16 full)     │
     │  TL2 kernels     │  │  + llama.cpp     │    │  + DFlash drafts │
     │                  │  │   fallback (Q4) │    │  for code/math   │
     └──────────────────┘  └──────────────────┘    └──────────────────┘
            CPU                   3090 VFIO              Blackwell host
            sub-ms                3-6× DFlash             1M ctx Nemotron
            branching             on code/math            (or Ling MoE)
```

Each tier's backend choice is locked by the tier's hardware constraint:

- **Pulse → bitnet.cpp** because only `bitnet.cpp` exploits AVX-512 VNNI VPDPBUSD for packed-2-bit ternary matmul.
- **Logic Engine → vLLM (primary) or llama.cpp (fallback)** because the 3090 needs GPU-native inference; vLLM gets DFlash drafts when available, llama.cpp fallback for Q4 quantized when DFlash isn't.
- **Oracle Core → vLLM + DFlash** because the Blackwell needs full-precision BF16, long context (1M tokens for Nemotron Mamba-Transformer hybrid), and DFlash's 3-6× speedup on code/math workloads.

The router's classify() rules are deterministic, operator-readable, and unit-tested (per sovereign-os `tests/unit/test_router_classify.py` — 19 cases).

### When LocalAI re-enters the picture

LocalAI is acceptable when:

1. **`old-workstation` profile**: Single 8 GB GPU; no Trinity; uniformity > specialization.
2. **As a translation layer for non-sovereign-os clients**: Some operator tools (Cursor / Continue.dev / etc.) speak OpenAI but expect specific model IDs LocalAI normalizes. Running LocalAI in *proxy mode* in front of the direct stack gives those clients a polished single endpoint while preserving per-tier exploitation underneath. Trade-off: extra hop.
3. **Multi-profile uniformity** where the operator wants ALL profiles' inference accessible via one URL: LocalAI-on-router. Adds complexity; only when warranted.

These are post-Stage-2 considerations. The default Stage-2+ build doesn't ship LocalAI.

### Profile-conditional backend matrix

| Profile | Pulse | Logic Engine | Oracle Core | Router |
|---|---|---|---|---|
| `sain-01` (default) | bitnet.cpp | vLLM (primary; 3090 VFIO) + llama.cpp (fallback) | vLLM + DFlash (Blackwell) | yes |
| `old-workstation` | n/a (no AVX-512) | llama.cpp (8 GB GPU) | n/a | optional |
| `minimal` / `headless` (reserved) | n/a | n/a | n/a | n/a |
| `developer` (reserved) | optional | llama.cpp or Ollama | n/a | optional |

## Recommendation

> [!success] Direct stack for sain-01; profile-specific backends for others
>
> | Use case | Pick |
> |---|---|
> | sain-01 default (SAIN-01 hardware) | **Direct stack** (router + bitnet.cpp + vLLM + DFlash) per [[sovereign-os-sdd-011]] |
> | old-workstation (constrained) | **llama.cpp** primary (or LocalAI for uniformity) |
> | minimal / headless | inference disabled by default |
> | developer | llama.cpp or Ollama (operator preference) |
> | mixed-fleet uniform endpoint | LocalAI-as-translation-layer over the direct stack (Stage-2+ enhancement) |

> [!warning] Anti-patterns to avoid
>
> - **Don't deploy LocalAI as the only entrypoint on sain-01** — erases the per-tier hardware exploitation that justified the Zen 5 + dual-GPU purchase.
> - **Don't use llama.cpp as the Oracle Core on sain-01** — misses DFlash's 3-6× speedup on code/math workloads.
> - **Don't run Pulse on GPU** — defeats the Trinity's CPU-CCD partition; wastes Blackwell VRAM budget.
> - **Don't pin vLLM to a model_id that lacks a DFlash draft checkpoint** — falls back to non-spec-dec generation; check Z-Lab's HF org for the target model before enabling `oracle-triage` channel (per selfdef SDD-016).
> - **Don't ignore the router's classify() rules** — they encode the operator's intent; modifying them silently changes per-request behavior.

## Open Questions

- For Z-Lab's DFlash drafts on Nemotron-3-Nano-Omni specifically, is a draft checkpoint published yet? (Per [[cmp-ling-26-flash-vs-nemotron-3-nano-omni|Ling vs Nemotron comparison]], roughly 20 target models ship pre-trained drafts as of Q2 2026.)
- For Pulse's bitnet.cpp throughput on Zen 5 single-cycle 512-bit AVX-512 specifically, what's the measured tok/sec on a real SAIN-01 (vs the published ~5-7 tok/sec on prior CPU classes)? Operator-side benchmark once hardware is procured.
- Should sovereign-os ship a LocalAI proxy mode out-of-box (one config flag enables it) or defer to operator-installed Stage-3? Stage-2+ design decision; currently the direct stack ships without LocalAI.

## Relationships

- DERIVED FROM: operator Q-017 directive (info-hub `raw/notes/2026-05-16-user-directive-sovereign-os-arc-opening-limit-continuation.md`)
- BUILDS ON: [[src-bitnet-b158-ternary-llm|BitNet b1.58 ternary LLM family]] — Pulse-tier requirement
- BUILDS ON: [[src-dflash-block-diffusion-spec-dec|DFlash speculative decoding]] — Oracle-tier code/math speedup
- BUILDS ON: [[src-zen5-avx512-single-cycle|Zen 5 AVX-512 single-cycle]] — Pulse-tier hardware substrate
- BUILDS ON: [[src-sain-01-sovereign-node-spec|SAIN-01 Sovereign Node Spec]] — hardware target
- BUILDS ON: [[concept-srp-trinity-pulse-weaver-auditor|SRP Trinity]] — software architecture
- COMPLEMENTS: [[cmp-ling-26-flash-vs-nemotron-3-nano-omni|Ling vs Nemotron]] — Oracle Core model picks
- RELATES TO: [[concept-1bit-ternary-weights|1-bit Ternary Weights]] — Pulse-tier algorithm
- RELATES TO: [[concept-vfio-gpu-isolation-amd-iommu|VFIO GPU Isolation]] — Logic Engine sandbox
- RELATES TO: [[concept-zfs-tiered-storage-llm-inference|ZFS Tiered Storage]] — model weights on tank/models
- IMPLEMENTS: sovereign-os SDD-011 (the architecture this comparison justifies)
- ENABLED BY: sovereign-os `scripts/inference/router.py` (the deterministic classify() that makes the stack work)
- CONSTRAINS: selfdef SDD-016 (`oracle-triage` channel targets this stack's router)

## Backlinks

(will be populated by `tools/obsidian.py backlinks` after pipeline post)
