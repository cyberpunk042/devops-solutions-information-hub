---
title: "Decision — Asymmetric KV Cache Quantization (q4_0 Keys + q2_K Values) for Qwen3 Models"
aliases:
  - "Decision — Asymmetric KV Cache Quantization (q4_0 Keys + q2_K Values) for Qwen3 Models"
  - "Decision: Asymmetric KV Cache Quantization"
type: decision
domain: cross-domain
layer: 6
status: synthesized
confidence: high
maturity: growing
reversibility: easy
derived_from:
  - model-local-ai
  - qwen3-8b-as-main-reasoning-model
  - single-active-backend-with-lru-eviction
created: 2026-04-19
updated: 2026-04-22
sources:
  - id: qwen3-8b-config
    type: file
    file: config/models/qwen3-8b.yaml
    description: "Qwen3-8B — cache_type_k=q4_0, cache_type_v=q2_K, flash_attention=true, context_size=16384 (AICP project)"
  - id: qwen3-30b-config
    type: file
    file: config/models/qwen3-30b-a3b.yaml
    description: "Qwen3-30B-A3B MoE — same asymmetric KV pattern, 'critical for MoE — saves significant VRAM' (AICP project)"
  - id: gpu-helpers
    type: file
    file: aicp/core/gpu.py
    description: "estimate_kv_cache_mb() and calculate_optimal_config() — read cache_type_k from model YAML, assume q4_0 = 4x reduction vs f16 (AICP project)"
  - id: dual-gpu-profile
    type: file
    file: config/profiles/dual-gpu.yaml
    description: "Extends default; promotes qwen3-30b-a3b primary; CONTEXT_SIZE=32768 (AICP project)"
  - id: llamacpp-turboquant
    type: external
    url: https://github.com/ggml-org/llama.cpp/discussions/20969
    description: "Upstream tracking issue for TurboQuant 'turbo3' KV types — future asymmetric option"
  - id: aicp-contribution-staging
    type: wiki
    file: raw/articles/from-aicp/decisions/01_drafts/asymmetric-kv-cache-quantization-q4-keys-q2-values.md
    description: "AICP's original submission, 2026-04-19 staged in raw/ before ingestion here"
tags: [decision, kv-cache, quantization, qwen3, gpu, vram, dual-gpu, aicp, transferable, pattern]
contributed_by: "aicp"
contribution_source: "/home/jfortin/devops-expert-local-ai"
contribution_date: "2026-04-19"
contribution_status: accepted
---

# Decision — Asymmetric KV Cache Quantization (q4_0 Keys + q2_K Values) for Qwen3 Models

## Summary

AICP's Qwen3 model configs use **asymmetric KV cache quantization** — `cache_type_k: q4_0` paired with `cache_type_v: q2_K` — instead of symmetric defaults. Identical in both `config/models/qwen3-8b.yaml` and `config/models/qwen3-30b-a3b.yaml`, with `flash_attention: true` enabling the asymmetric path in llama.cpp. The trade-off exploits a known asymmetry in attention math: keys participate in dot-product similarity (softmax over scaled dot-products) where small perturbations cascade through the exponent; values participate only in a final weighted sum (linear projection) where larger perturbations dilute additively. Empirically validated by upstream llama.cpp work + AICP's own profile: keys at q4_0 (4-bit) preserve attention quality; values at q2_K (~2.5-bit K-quant) lose almost no quality on Qwen3 specifically while saving substantial VRAM.

Concrete outcomes: (a) Qwen3-8B runs at 16K context on the 8 GB single-GPU baseline (was 8K with symmetric q4_0); (b) Qwen3-30B-A3B MoE fits on the 19 GB dual-GPU baseline at 8K context (would not fit at all without aggressive KV compression); (c) `flash_attention` requires symmetric quant when both K and V use the same type, but llama.cpp accepts K=q4_0/V=q2_K as a known-good asymmetric pair.

## Decision

> [!success] Use `cache_type_k: q4_0` + `cache_type_v: q2_K` + `flash_attention: true` for all Qwen3 models.
>
> | Model | cache_type_k | cache_type_v | context_size unlocked | VRAM saved vs symmetric f16 |
> |-------|--------------|--------------|----------------------|------------------------------|
> | qwen3-8b | q4_0 | q2_K | 16K (was 8K) | ~6× reduction in KV cache footprint |
> | qwen3-8b-fast | q4_0 | q2_K | 16K | same |
> | qwen3-4b | q4_0 | q2_K | 16K (fits 4 GB easily) | ~6× reduction |
> | qwen3-30b-a3b | q4_0 | q2_K | 8K (only fit at all with this) | required for dual-GPU profile |
> | gemma4-* | Gemma-specific defaults under evaluation | — | — | tracked separately |

Pattern documented inline in each model YAML with a comment block. New Qwen-family model YAMLs should copy the canonical comment block from `config/models/qwen3-8b.yaml` lines 17-22.

## Alternatives

### Alternative 1 — Symmetric f16 KV cache (no quantization)

llama.cpp's default. Highest quality.

> [!warning] Rejected: VRAM cost prohibitive. At 16K on a 32-layer 8B model, cache ~32 MB; model weights at Q4_K_M ~5 GB; system reserve 800 MB → fine for small contexts on 8 GB, breaks at 16K. Dual-GPU qwen3-30b-a3b (48 layers) at 8K f16 ~4 GB cache + ~17 GB weights = exceeds 19 GB. f16 is correct only when VRAM is unconstrained (24 GB+).

### Alternative 2 — Symmetric q8_0 (mild quantization)

Halve f16 with minimal quality loss.

> [!warning] Rejected: still too expensive for 16K target on 8 GB. q8_0 saves ~2× vs f16, not 6×. Prior AICP config used q8_0 and was capped at 8K — operators noticed truncation. Asymmetric q4_0 K + q2_K V is what made 16K feasible on same hardware. q8_0 also doesn't enable dual-GPU MoE.

### Alternative 3 — Symmetric q4_0 (uniform 4-bit)

Uniform aggressive quantization.

> [!warning] Rejected: quality regressions visible in Qwen3's tool-calling output (dropped arguments, mis-parsed JSON). Values at q4_0 contribute observable noise to the final attention-weighted output projection; Qwen3's tool-calling head is sensitive to small magnitude shifts. Switching values to q2_K (K-quant superblock structure with per-block scales) preserved tool-calling fidelity better than uniform q4_0. Keys stay at q4_0 because softmax exponentiates dot products: any K compression below q4_0 amplifies through the exponent.

### Alternative 4 — Symmetric q2_K (aggressive uniform)

Maximum VRAM savings.

> [!warning] Rejected: keys at q2_K destroy attention quality. Chain-of-reasoning chains (Qwen3 thinking mode) collapse into repetitive loops; tool-calling JSON becomes inconsistent; multi-turn coherence degrades after ~3 turns. This is the failure mode motivating the asymmetry.

### Alternative 5 — Disable KV quantization + reduce context_size

Set cache_type_k/v to defaults (f16), lower context_size to whatever fits.

> [!warning] Rejected: trades context length for KV precision-above-q4_0, but context is more operationally valuable. AICP's workload (RAG + multi-file diff review + long agent transcripts) benefits from 16K. Cutting to 8K to preserve f16 KV would limit these workloads in exchange for quality improvements operators do not perceive.

### Alternative 6 — Experimental q5_0 / q5_1 KV types

5-bit precision between q4_0 and q8_0.

> [!warning] Rejected (deferred): llama.cpp's q5_x KV types exist but less mature than q4_0 + q2_K in production builds. AICP tracks TurboQuant turbo3 discussion for next-generation asymmetric types that may obsolete q4_0/q2_K. Until then, the current scheme is the operationally proven default.

## Rationale

> [!info] Evidence-backed reasons
>
> 1. **Attention math is asymmetric — quantize accordingly.** `softmax(QK^T / sqrt(d)) · V`. Errors in K propagate through softmax (exponential amplification). Errors in V propagate through a linear weighted sum (additive dilution). Treating K and V identically wastes precision on V or destroys quality on K.
>
> 2. **Operationally validated on AICP's hardware.** `config/models/qwen3-8b.yaml` line 35: "Context: 16384 enabled by asymmetric KV quant (q4_0 K + q2_K V)". Same model was capped at 8K with symmetric q4_0. After change: 16K fits on 8 GB GPU — encoded in shipped config, verified by successful LocalAI load.
>
> 3. **Required for the dual-GPU MoE profile.** `config/models/qwen3-30b-a3b.yaml` line 26: "KV cache quantization (critical for MoE — saves significant VRAM)". 48-layer model + uniform f16 KV at 8K would consume ~4 GB just for cache on top of ~17 GB weights — over 19 GB total. Without this decision, the `dual-gpu` profile (which the 2026-04-17 hardware upgrade unlocked) would still not run.
>
> 4. **flash_attention requires a known-good K/V combination.** `flash_attention: true` works with f16/f16, q8_0/q8_0, q4_0/q4_0, AND asymmetric q4_0/q2_K (empirically validated upstream). Other combos silently fall back to slower non-flash path or raise errors. The chosen pair is the only asymmetric option keeping flash_attention on.
>
> 5. **`aicp/core/gpu.py` already assumes q4_0 KV throughout.** `calculate_optimal_config()` reads `cache_type_k` and assumes 4× VRAM reduction vs f16 (line 137: `per_1k = 0.5 if kv_quantized else 2.0`). Switching defaults would invalidate the auto-tuner's math.
>
> 6. **Reversal cost concentrated in two YAML keys per model.** `cache_type_k` and `cache_type_v` are the only places this lives. Reverting means deleting `cache_type_v: q2_K` from each Qwen3 YAML and reducing `context_size`. Operationally: qwen3-8b loses 16K → 8K context; dual-gpu profile stops being runnable.

## Reversibility

**Easy** — per-model edit to `config/models/<name>.yaml`, two keys + optional `context_size` rollback. Reload via `docker compose restart localai`.

Cost scales with hardware:
- 8 GB single-GPU: reverting drops qwen3-8b 16K → 8K. Visible in long-RAG and long-transcript workloads.
- 19 GB dual-GPU: reverting makes qwen3-30b-a3b unloadable. Dual-GPU profile loses its primary; must fall back to qwen3-8b — defeating the profile.
- Future 24 GB+: reversal becomes nearly free.

## Dependencies

If reversed (drop asymmetric scheme):

- `config/models/qwen3-*.yaml` — remove `cache_type_v: q2_K`; set `cache_type_k: f16` or `q8_0`
- `config/models/qwen3-8b.yaml` — reduce `context_size` from 16384 to 8192 (otherwise OOM)
- `config/models/qwen3-30b-a3b.yaml` — model becomes unloadable on 19 GB; must drop from dual-gpu profile
- `config/profiles/dual-gpu.yaml` — primary `model: qwen3-30b-a3b` would need to revert to qwen3-8b
- `aicp/core/gpu.py` `estimate_kv_cache_mb()` — q4_0 = 0.5 MB/1K assumption becomes wrong for f16; auto-tuner over-allocates
- Skill expectations — skills with `model: qwen3-8b` expect 16K context; would need to stay under 8K
- Documentation — CLAUDE.md `## LocalAI Assessment` table claims 16K context; would need updating

If extended (apply to non-Qwen models):

- `config/models/gemma4-*.yaml` — Gemma 4's attention architecture differs from Qwen3 (different head dim, layer count, MoE structure for 26B-A4B); validate with benchmark before adopting
- `config/models/codellama.yaml`, `hermes.yaml` — older models; KV-quant interaction with their training is less studied; A/B test before changing
- New model YAMLs should adopt the same comment block as the canonical (`config/models/qwen3-8b.yaml` lines 17-22)

If migrated to TurboQuant turbo3 (when available):

- llama.cpp must support the new types (track [discussion #20969](https://github.com/ggml-org/llama.cpp/discussions/20969))
- `config/models/qwen3-*.yaml` — change `cache_type_k` value to `turbo3_*` variant
- Re-validate quality on Qwen3's tool-calling and thinking-mode outputs
- `aicp/core/gpu.py` — update `estimate_kv_cache_mb()` constants for the new compression ratio

## Relationships

- BUILDS ON: [[model-local-ai|Model — Local AI ($0 Target)]]
- RELATES TO: [[qwen3-8b-as-main-reasoning-model|Decision — Qwen3-8B as Main Reasoning Model]] (sibling — choice of model; this is choice of how to fit it)
- RELATES TO: [[localai-over-ollama-vllm-for-multi-model-orchestration|Decision — LocalAI over Ollama/vLLM]] (LocalAI passes YAML keys through to llama.cpp; Ollama abstracts them away)
- RELATES TO: [[single-active-backend-with-lru-eviction|Single-Active Backend with LRU Eviction]] (asymmetric KV reduces per-model VRAM; allows more concurrent backends within MAX_ACTIVE_BACKENDS)

## Backlinks

[[model-local-ai|Model — Local AI ($0 Target)]]
[[Decision — Qwen3-8B as Main Reasoning Model]]
[[Decision — LocalAI over Ollama/vLLM]]
[[single-active-backend-with-lru-eviction|Single-Active Backend with LRU Eviction]]
