---
title: DFlash vs EAGLE-3 vs MEDUSA — Speculative Decoding Family
aliases:
  - "DFlash vs EAGLE-3 vs MEDUSA — Speculative Decoding Family"
  - "DFlash vs EAGLE-3"
  - "Speculative Decoding Comparison"
type: comparison
layer: 3
maturity: growing
domain: ai-models
status: synthesized
confidence: high
created: 2026-05-15
updated: 2026-05-15
sources:
  - id: src-dflash-block-diffusion-spec-dec
    type: wiki
    file: "wiki/sources/src-dflash-block-diffusion-spec-dec.md"
    title: "Synthesis — DFlash: Block-Diffusion Flash Speculative Decoding"
  - id: concept-speculative-decoding-block-diffusion
    type: wiki
    file: "wiki/domains/ai-models/concept-speculative-decoding-block-diffusion.md"
    title: "Concept — Speculative Decoding via Block Diffusion"
  - id: eagle3-paper
    type: paper
    url: "https://arxiv.org/abs/2503.01840"
    title: "EAGLE-3: Scaling up Inference Acceleration of Large Language Models via Training-Time Test"
  - id: medusa-paper
    type: paper
    url: "https://arxiv.org/abs/2401.10774"
    title: "MEDUSA: Simple LLM Inference Acceleration Framework with Multiple Decoding Heads"
tags:
  - comparison
  - ai-models
  - speculative-decoding
  - inference-acceleration
  - dflash
  - eagle-3
  - medusa
  - block-diffusion
  - autoregressive-drafting
  - parallel-drafting
  - acceptance-rate
  - sain-01
---

# DFlash vs EAGLE-3 vs MEDUSA — Speculative Decoding Family

## Summary

Three approaches to **lossless speculative-decoding acceleration** of LLM inference, ordered by recency + capability: **MEDUSA** (Jan 2024, simple multi-decoding-head approach), **EAGLE-3** (Feb 2025, autoregressive draft with training-time test, state-of-the-art before DFlash), **DFlash** (Feb 2026, block-diffusion draft with bidirectional attention, current state-of-the-art at ~2.5× over EAGLE-3 on math/code workloads). All three preserve target-model output identity (lossless); they differ in *how* the draft generates candidate tokens and consequently in *acceptance rate* + *end-to-end speedup*. The choice for the [[src-sain-01-sovereign-node-spec|SAIN-01]] Oracle Core / Logic Engine tier comes down to: workload entropy (math/code wins more with DFlash; conversational/creative narrows the gap), target-model availability (DFlash ships pre-trained drafts for ~20 targets; EAGLE-3 has narrower native support; MEDUSA is broadly available), and deployment maturity (EAGLE-3 is more battle-tested in production; DFlash is newer with strong Z-Lab + Baseten + Spheron writeups). **Headline result**: for math + code workloads on the SAIN-01 Blackwell, DFlash is the right pick — 4.7-5.2× speedup on Math500/HumanEval at concurrency 1, vs ~2× from EAGLE-3, vs ~1.5-1.8× from MEDUSA. For free-form conversational workloads, all three degrade toward target-only latency; pick by deployment maturity, not headline speedup.

## Comparison Matrix

> [!abstract] Three Speculative-Decoding Approaches
>
> | Dimension | MEDUSA | EAGLE-3 | DFlash |
> |---|---|---|---|
> | **Date introduced** | Jan 2024 | Feb 2025 | Feb 2026 |
> | **Origin** | Princeton + Together AI | Tsinghua + Microsoft Research | Z-Lab |
> | **Paper** | arXiv:2401.10774 | arXiv:2503.01840 | arXiv:2602.06036 |
> | **License** | Apache 2.0 | Apache 2.0 | MIT |
> | **Draft architecture** | **Multiple decoding heads** on target model, each predicting Nth-next token | Small autoregressive draft model, trained via training-time test | **Block diffusion draft** with bidirectional attention |
> | **K-token draft generation** | Heads predict K tokens in parallel (~1 forward pass) | K sequential forward passes | **1 forward pass for full K-token block** |
> | **Attention direction in draft** | n/a (multi-head, no separate draft) | Causal (left-to-right) | **Bidirectional** |
> | **Draft model depth** | Fixed (tied to target architecture) | Constrained by K-step serialization cost | **Decoupled from K — can be deep without per-step cost** |
> | **Target-model integration** | Heads grafted onto target; same parameters | Separate small AR draft trained against target | Separate block-diffusion draft trained against target |
> | **Headline speedup vs no-speculation** | 1.5-2.3× | 2-3× | **up to 6×** (lossless) |
> | **Speedup ratio over MEDUSA** | baseline 1× | ~1.5× over MEDUSA | ~3× over MEDUSA |
> | **Speedup ratio over EAGLE-3** | (worse) | baseline 1× | **up to 2.5× over EAGLE-3** |
> | **Best workloads (entropy-low)** | math, code | math, code | **math (highest) + code (high)** |
> | **Worst workloads (entropy-high)** | conversational, creative | conversational, creative | conversational, creative (still real, but moderate) |
> | **Lossless?** | Yes | Yes | Yes |
> | **Multi-batch / high-concurrency** | Designed for low-batch | Improved over MEDUSA | Designed for concurrency 1-32 simultaneously |
> | **GPU memory overhead vs target alone** | Small (heads are part of target) | Moderate (draft model VRAM) | Moderate (draft model VRAM; deeper draft) |
> | **Pre-trained drafts available** | Per-target (community-trained) | Per-target (some shipped) | **~20 pre-trained drafts on HF (Gemma 4, Qwen 3.x, MiniMax, Kimi, GPT-OSS, Llama 3.1)** |
> | **Backend compatibility** | vLLM, llama.cpp, transformers | vLLM, transformers | **vLLM v0.20.1+, SGLang, Transformers, MLX** |
> | **Production maturity** | Mature (2 years in production) | Mature-emerging (1 year in production) | **Newer (months); strong Z-Lab + Baseten + Spheron writeups; production-grade** |
> | **Training recipe public?** | Yes | Partial | "Open-sourced soon" (per repo); inference checkpoints public |

## Key Insights

> [!abstract] The architectural progression: simpler → autoregressive → block-diffusion
>
> The three approaches form a generational sequence. MEDUSA: simplest — graft extra heads onto the target, predict K tokens in parallel. EAGLE-3: introduce a separate draft model that's still autoregressive (causal attention) but smaller + trained against target's hidden states. DFlash: replace the autoregressive draft with a block-diffusion draft using bidirectional attention. Each step trades implementation complexity for higher acceptance rate. ([[concept-speculative-decoding-block-diffusion|block-diffusion concept]])

> [!tip] DFlash's win is structural, not just tuning
>
> EAGLE-3's draft must respect causal attention — generating K tokens serializes K forward passes. DFlash's bidirectional draft produces all K in one pass. This isn't a clever optimization; it's a categorical change in draft latency vs depth. A deeper DFlash draft = better predictions = higher acceptance = larger end-to-end speedup, without the K× draft-time penalty EAGLE-3 pays. ([[src-dflash-block-diffusion-spec-dec|DFlash synthesis]])

> [!success] The math-code-vs-creative gradient is the operative signal
>
> All three approaches share the entropy-based pattern: low-entropy outputs (math, code) get high speedups; high-entropy outputs (creative, conversational) get moderate speedups. DFlash amplifies the gradient (deeper drafts predict structured output better; flatter distributions still rejected). **Operator's first-hand DFlash framing — "3× on code, doesn't work on creative" — matches the published pattern.** ([[src-dflash-block-diffusion-spec-dec|DFlash synthesis]])

> [!warning] Speedup ≠ universally applicable
>
> Headline speedups (DFlash up to 6×, EAGLE-3 ~3×, MEDUSA ~2×) assume the workload sits in the speculative-decoding sweet spot (low-entropy targets, sufficient draft acceptance). Free-form chat, creative writing, exploratory dialogue: all three approaches degrade — the speedup approaches 1× as the target's next-token distribution flattens. **Don't size capacity for the headline number; size for the expected workload distribution.**

> [!info] Production maturity differs from research novelty
>
> MEDUSA is the most battle-tested (~2 years in production). EAGLE-3 is mature-emerging (~1 year). DFlash is newer (months) but shipped MIT-licensed with pre-trained drafts for ~20 target models on HuggingFace, plus production deployments documented at Baseten + Spheron. **For risk-averse deployment, the DFlash-vs-EAGLE-3 choice is a maturity vs speed-headroom trade-off.**

## Deep Analysis

### MEDUSA — multi-head decoding on the target

> [!tip] Read this when
> You need a low-overhead, well-understood speculative path and the target model is one MEDUSA already supports.

**Approach.** MEDUSA modifies the target model architecture by adding multiple decoding heads — each head predicts a token at a specific position (N+1, N+2, N+3, ...) given the current hidden states. The K heads run in parallel against the same forward pass; the target verifies as a K-token candidate sequence. Effectively a "fat target" approach: no separate draft model, just additional output heads.

**Strengths:**
- No separate draft model to load — VRAM overhead is small
- Tight integration with target — no synchronization issues
- Mature: 2+ years of production deployment
- Available across vLLM, llama.cpp, transformers ecosystems

**Weaknesses:**
- Requires modifying the target model — each head must be trained
- Acceptance rate bounded by what the target's own hidden states encode about future tokens (limited foresight)
- Doesn't generalize cleanly to massively-parallel drafts at deep depths

**Headline speedup:** 1.5-2.3× on the original paper's benchmarks (Vicuna-13B and similar).

**Ideal use:** older target models where MEDUSA heads are already trained + available; deployment environments where simplicity matters more than headline speedup; pre-DFlash maturity baseline.

### EAGLE-3 — autoregressive draft with training-time test

> [!tip] Read this when
> The target is well-supported, you want a proven speedup beyond MEDUSA, and DFlash drafts for your target haven't shipped yet.

**Approach.** EAGLE-3 trains a separate small autoregressive draft model against the target. The draft generates K candidate tokens one at a time (K forward passes), conditioned on the target's hidden states. The target verifies the K-token sequence in one parallel pass. The "training-time test" technique improves acceptance rate by exposing the draft to target-distribution outputs during training, not just teacher-forced tokens.

**Strengths:**
- Significant speedup over MEDUSA (~1.5× more)
- Lossless guarantee
- Well-integrated with vLLM + Transformers
- Wide target-model coverage in the EAGLE community

**Weaknesses:**
- Draft model is autoregressive — K-step drafting time is K × draft-fwd-pass
- Draft must be small or its serialization cost dominates per-step latency
- Deeper drafts = higher quality = K× slower drafting; the depth-vs-K trade-off is constraining
- EAGLE-3 specifically is research-grade; some production deployments still use EAGLE-2

**Headline speedup:** 2-3× on the original paper's benchmarks (Llama-2-7B-Chat, Vicuna-13B, similar).

**Ideal use:** production deployment as of Q1 2026 — proven, well-tooled, predictable. The default speculative-decoding choice until DFlash matures further.

### DFlash — block-diffusion draft with bidirectional attention

> [!tip] Read this when
> Math + code workloads dominate, you can deploy vLLM v0.20.1+, and pre-trained DFlash drafts ship for your target model.

**Approach.** Replace the autoregressive draft with a **block-diffusion model** using **bidirectional attention** across the K-token window. The draft produces K candidate tokens **in one forward pass**, conditioned on context features extracted from the target model. The target verifies the K-token block in one parallel pass. Bidirectional attention is the load-bearing architectural choice: it lets the draft be much deeper without paying a K-step serialization cost.

**Strengths:**
- **Up to 6× lossless acceleration** (head-and-shoulders above EAGLE-3)
- Deeper, more accurate drafts at constant per-step latency
- Especially strong on math (4.7× Math500) + code (5.2× HumanEval) at concurrency 1 on Qwen3-8B / B200
- Scales to concurrency 1-32 simultaneously
- Pre-trained drafts ship for ~20 target models on HuggingFace
- Backend coverage: vLLM v0.20.1+, SGLang, Transformers, MLX
- MIT license

**Weaknesses:**
- Newer; smaller production-deployment footprint (months vs years)
- Training recipe roadmapped as "open-sourced soon" but not yet public — custom fine-tunes can't get their own DFlash draft until then
- Deeper draft = more VRAM overhead than MEDUSA-on-target
- Multi-tenant draft-cache management is less battle-tested
- vLLM v0.20.1+ requirement (older deployments need upgrade)

**Headline speedup:** up to 6× lossless on Qwen3-8B / B200 with FlashAttention-4; 4.7× Math500; 5.2× HumanEval; ~5.1× across concurrency 1-32.

**Ideal use:** SAIN-01 Logic Engine + Oracle Core code/math workloads on the Blackwell or 3090, especially when the operator's first-hand experience confirms the technique's gradient on the target workload.

### How they map onto the SAIN-01 tier architecture

| SAIN-01 tier | Hardware | Suitable workloads | Best speculative-decoding pick |
|---|---|---|---|
| **Conductor (Pulse)** | CPU CCD 0 | State routing, intent classification | **None** — CPU runs ternary (not speculative-decoding territory) |
| **Logic Engine** | RTX 3090 (24GB) | Parsing, JSON, regex, code completion | **DFlash** (community writeup confirms ~2× on Qwen3.6-27B on 24GB) |
| **Oracle Core (code/math)** | Blackwell PRO 6000 (96GB) | Code generation, mathematical reasoning, structured output | **DFlash** (5× headline speedups apply) |
| **Oracle Core (conversational)** | Blackwell PRO 6000 (96GB) | Free-form generation, dialogue, creative writing | **EAGLE-3** or none — all three degrade; pick maturity over speedup headroom |
| **Audit / Logging** | host CPU | Tetragon stream parsing, audit-log append | n/a |

The map matters: speculative decoding is not a universal acceleration — it's a workload-conditioned trade-off. Deploying DFlash on the Conductor wouldn't make sense (no GPU); deploying DFlash on creative-writing workloads wouldn't deliver headline speedups. Deploy the right technique at the right tier on the right workload.

### Where to read further

- The [[src-dflash-block-diffusion-spec-dec|DFlash synthesis]] grounds the block-diffusion approach in primary sources (arXiv:2602.06036 + Z-Lab + Baseten + Spheron).
- The [[concept-speculative-decoding-block-diffusion|speculative-decoding concept page]] formalizes the entropy-based mechanism.
- EAGLE-3 paper: arXiv:2503.01840 — "Scaling up Inference Acceleration of Large Language Models via Training-Time Test."
- MEDUSA paper: arXiv:2401.10774 — "Simple LLM Inference Acceleration Framework with Multiple Decoding Heads."

## Recommendation

> [!success] Pick by workload entropy + target availability
>
> | Your workload | Pick | Why |
> |---|---|---|
> | Math reasoning (GSM8K, MATH-500, AIME) on a target DFlash supports | **DFlash** | 4.7× Math500 at concurrency 1; structural advantage |
> | Code generation (HumanEval, MBPP, LiveCodeBench) on a target DFlash supports | **DFlash** | 5.2× HumanEval; matches operator's first-hand framing |
> | Structured output (JSON compilation, schema-constrained generation) | **DFlash** if target supports; else **EAGLE-3** | Low-entropy output wins with speculative decoding; DFlash amplifies |
> | Free-form conversational (MT-Bench class) | **EAGLE-3** or **none** | DFlash gradient flattens; EAGLE-3 maturity wins; or skip speculation entirely |
> | Creative writing, long-form narrative | **None** (pure target inference) | All three degrade toward 1×; overhead not worth it |
> | Risk-averse production deployment, target model EAGLE-3 supports | **EAGLE-3** | Production-mature; well-understood failure modes |
> | Target model is custom fine-tune | **MEDUSA** (community-trained heads) or **EAGLE-3** (if training pipeline accessible) | DFlash training recipe not yet public; can't ship a custom draft |
> | Apple Silicon deployment (MLX) | **DFlash** | Native MLX backend support; the others require custom porting |
> | Multi-tenant / high-concurrency (concurrency 16-32) | **DFlash** | Designed for the concurrency-1-32 range explicitly |
> | Pre-Q1 2026 deployments | **EAGLE-3** or **MEDUSA** | DFlash didn't exist yet; this is a historical / migration question |

> [!warning] Anti-patterns to avoid
>
> - **Don't enable speculative decoding indiscriminately.** Speculative decoding adds draft-model compute + memory overhead. On workloads where the entropy is high, the overhead exceeds the gain. Match the technique to the workload, not the model.
> - **Don't compare headline speedups across approaches without controlling for target + workload.** A "6× DFlash" claim on Math500 doesn't translate to "6×" on creative-writing. The published numbers are workload-specific.
> - **Don't switch from EAGLE-3 to DFlash on production at the headline speedup alone.** The production-maturity gap is real; rollout carefully + verify acceptance rates on the specific workload distribution.
> - **Don't ignore vLLM version requirements.** DFlash needs v0.20.1+; older vLLM deployments can't deploy it without upgrade. Plan the upgrade as part of the rollout.

## Relationships

- BUILDS ON: [[src-dflash-block-diffusion-spec-dec|DFlash synthesis]]
- BUILDS ON: [[concept-speculative-decoding-block-diffusion|Concept — Speculative Decoding via Block Diffusion]]
- COMPLEMENTS: [[cmp-bitnet-vs-fp16-execution-cost|BitNet vs FP16 comparison]] (orthogonal acceleration on CPU vs GPU; the two stack on different tiers)
- USED BY: [[src-sain-01-sovereign-node-spec|SAIN-01 Sovereign Node Spec]] (Logic Engine + Oracle Core tier deployment decisions)
- RELATES TO: [[concept-vfio-gpu-isolation-amd-iommu|VFIO GPU Isolation]] (GPU substrate that hosts the speculative-decoding pipeline)

## Backlinks

[[DFlash synthesis]]
[[Concept — Speculative Decoding via Block Diffusion]]
[[BitNet vs FP16 comparison]]
[[SAIN-01 Sovereign Node Spec]]
[[VFIO GPU Isolation]]
