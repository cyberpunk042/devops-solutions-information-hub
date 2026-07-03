---
title: "Synthesis — Quantization (YouTube, 2026): How a 280GB Model Runs on Your Laptop — Outliers as Central Villain · 5 Algorithms · Bell-Curve Per-Group Scaling · NF4 Smart Grid"
aliases:
  - "Quantization Outliers Central Villain"
  - "5 Quantization Algorithms Synthesis"
  - "NF4 Smart Grid"
  - "Q4KM Format Decoded"
  - "GGUF K-Quants Per-Group"
type: source-synthesis
domain: tools-integration
status: synthesized
confidence: high
maturity: seed
layer: 1
created: 2026-05-08
updated: 2026-05-08
last_reviewed: 2026-05-08
sources:
  - id: youtube-quantization-280gb
    type: video
    url: https://www.youtube.com/watch?v=Quj3M5gqxT8
    file: raw/transcripts/how-your-laptop-can-run-a-280-gb-ai-model-quantization.txt
    description: "YouTube video — pedagogical synthesis of LLM quantization: Tim Dettmers' 6.7B-param outlier-emergence threshold; bell-curve weight distributions; per-group scaling; NF4 quantile-based grid; 5 production algorithms (LLM.int8 / SmoothQuant / GPTQ / AWQ / GGUF K-quants) all addressing outliers; concrete Llama-3 8B benchmarks; Q4KM format decoded character-by-character"
  - id: dettmers-llm-int8-paper
    type: documentation
    url: https://arxiv.org/abs/2208.07339
    description: "Tim Dettmers et al — LLM.int8() — 8-bit matrix multiplication for transformers at scale (the paper that surfaced outlier emergence at 6.7B parameters)"
  - id: nf4-qlora-paper
    type: documentation
    url: https://arxiv.org/abs/2305.14314
    description: "Dettmers et al — QLoRA — NF4 (NormalFloat4) quantization with quantile-based grid placement for normal-distribution weights"
  - id: smoothquant-paper
    type: documentation
    url: https://arxiv.org/abs/2211.10438
    description: "Xiao et al — SmoothQuant — algebraic identity to migrate outliers from activations to weights (X·W = (X/s)·(s·W))"
  - id: gptq-paper
    type: documentation
    url: https://arxiv.org/abs/2210.17323
    description: "Frantar et al — GPTQ — column-wise quantization with rounding-error redistribution"
  - id: awq-paper
    type: documentation
    url: https://arxiv.org/abs/2306.00978
    description: "Lin et al — AWQ — activation-weighted quantization; identifies salient weight channels (1%) and scales them up before rounding"
  - id: ggml-gguf-spec
    type: documentation
    url: https://github.com/ggerganov/llama.cpp
    description: "GGUF / llama.cpp — K-quants format; per-group scaling with two-level block structure"
  - id: unsloth-synth
    type: wiki
    file: wiki/sources/tools-integration/src-unsloth-fast-lora-consumer-hardware.md
    description: "Unsloth Synthesis — production deployment of UD-IQ2 / Q2_K weight quantization on consumer hardware (RTX 4090 24GB); this synthesis documents the algorithmic foundation Unsloth implements"
  - id: multi-layer-compression-lesson
    type: wiki
    file: wiki/lessons/01_drafts/end-to-end-compression-across-the-ai-stack-composes-multiplicatively-6-plus-independent-mechanisms-at-6-distinct-layers.md
    description: "Multi-Layer Compression Lesson — quantization is Layer 5 (Model weights); this synthesis enriches Layer 5 with 5-algorithm-convergence evidence (all addressing the same outlier root-cause through different mechanisms)"
  - id: anti-vendor-lock-in-lesson
    type: wiki
    file: wiki/lessons/01_drafts/anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence.md
    description: "Anti-Vendor-Lock-In Lesson — Layer 5 weight-quantization substitutability axis: 5 production algorithms + multiple format families (BF16 / FP8 / INT8 / GGUF Q4 / GPTQ / AWQ / NF4 / Q2_K / UD-IQ2 / FP4 microscaling / Bitnet ternary)"
  - id: custom-model-concept
    type: wiki
    file: wiki/domains/cross-domain/custom-tailored-senior-engineer-tier-model-group-with-recreated-intelligence-layer-research-synthesis.md
    description: "Custom-Tailored Model Group Concept — M002 specialist LoRA on RTX 4090 needs Q4KM-class quantization to fit 27B-class bases; this synthesis documents the substrate"
tags: [synthesis, quantization, outliers, llm-int8, smoothquant, gptq, awq, gguf, k-quants, nf4, q4km, q2k, ud-iq2, weight-compression, layer-5-compression, mission-2026-05-08, layer-1, paper-grade, dettmers, consumer-hardware, rtx-4090-substrate, anti-vendor-lock-in-evidence]
---

# Synthesis — Quantization: 280GB Model on a Laptop, Outliers as Central Villain

## Summary

Pedagogical YouTube synthesis of LLM quantization that traces the 5-algorithm convergence in the field to a single root-cause: **outliers**. **The trigger event** (Tim Dettmers 2022): naive 8-bit quantization works for small models but degrades catastrophically at **6.7B parameters** when "outliers emerge" — a tiny handful of weight magnitudes ~100× the average dominate the dynamic range, forcing a global scale that wastes precision on the bulk. **The bell-curve insight**: weight distributions in modern LLMs are reliably bell-shaped (most weights tiny, clustered near zero); precision belongs where the action is, not at the edges. **The fix at the algorithmic core**: per-group scaling — slice tensor into groups (e.g., 64 weights per group); each group gets its own absmax + scale; outliers contained to one group; bulk regains precision. Cost: ~0.25 bit/weight metadata. **NF4 (NormalFloat4)**: instead of 16 evenly-spaced grid points, place 16 grid points at the **quantiles of a normal distribution** — non-uniform grid crowded near zero, sparse at edges, where weights actually live. **Five production algorithms each addressing outliers differently**: (1) **LLM.int8 (2022)** — splits computation; outlier dimensions go through separate 16-bit path; bulk stays at 8 bits; (2) **SmoothQuant** — algebraic identity X·W = (X/s)·(s·W) migrates outlier difficulty from activations to weights; (3) **GPTQ** — quantizes column-wise + pushes leftover rounding error into not-yet-touched columns (errors cancel instead of accumulating); (4) **AWQ** — identifies the 1% of weight channels that multiply against the largest activations; scales those channels up before rounding (salient channels hit more accurate grid points); storage stays uniform at 4 bits; (5) **GGUF K-quants** — per-group scales + double-quantization (two-level block structure). **Concrete benchmarks** on Llama-3 8B: 16-bit perplexity 6.23 / 15GB · 8-bit perplexity 6.23 / 8GB · Q5KM perplexity 6.29 / 5.3GB · Q4KM perplexity 6.38 / 4.58GB. **Q4KM 70B fits 42GB** — runs on a single 48GB consumer GPU vs the 16-bit version requiring 2× A100 (>$10,000 each). **Q4KM format decoded**: Q=Quantized, 4=4 bits per weight, K=K-quants per-group two-level block structure, M=Medium variant (bulk 4-bit, sensitive tensors bumped to 5/6-bit). **Two myths refuted**: (a) "quantization halves quality" — reality: hockey-stick curve flat 16→5, small dip at 4, cliff below 3; (b) "AWQ keeps salient weights at 16-bit" — reality: storage uniform 4-bit; salience is a numerical pre-rounding trick, not a storage tier. **Mission relevance**: (1) **enriches the [[end-to-end-compression-across-the-ai-stack-composes-multiplicatively-6-plus-independent-mechanisms-at-6-distinct-layers|Multi-Layer Compression Lesson]] Layer 5 (Model weights)** with 5-algorithm-convergence evidence — all addressing the same outlier root-cause through structurally distinct mechanisms; this is **convergent-pattern within a single layer** (mirrors the cross-layer convergence the parent lesson documents); (2) **adds Layer-5 substitutability axes to [[anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence|Anti-Vendor-Lock-In Lesson]]** — substitution within Layer 5: BF16 / FP8 / INT8 / Q4_K_M / GPTQ / AWQ / NF4 / Q2_K / UD-IQ2 / FP4 microscaling / Bitnet ternary; (3) **production substrate for [Custom-Tailored Model Group](../../domains/cross-domain/custom-tailored-senior-engineer-tier-model-group-with-recreated-intelligence-layer-research-synthesis.md) M002** specialist LoRA on RTX 4090 — Q4KM is the realistic format for 27B-class bases at 24GB VRAM; (4) **operator-mission-aligned doctrine**: *"5 algorithms, 1 root cause"* — the **central-villain framing** mirrors the operator's mission discipline (root-cause-first, not symptom-treatment); applies to both code-level bugs (operator's *"fix it at the root"*) and inference-level outlier handling.

## Reference

> [!info] Source identity
>
> | Field | Value |
> |---|---|
> | **Type** | Pedagogical YouTube video |
> | **Date** | 2026 (Q1 or Q2; specific not in transcript) |
> | **Domain** | LLM quantization theory + production formats |
> | **Tone** | Educational; algorithm-comparison-driven |
> | **Confidence** | High — content is paper-grounded (cites Dettmers 2022; consistent with QLoRA + LLM.int8 + GPTQ + AWQ + SmoothQuant published results) |
> | **Outlier-emergence threshold** | 6.7B parameters (Dettmers' chart) |
> | **Outlier magnitude** | ~100× the average bulk weight |
> | **NF4 grid points** | 16 (4 bits) at normal-distribution quantiles |
> | **Llama-3 8B Q4KM perplexity** | 6.38 (vs 6.23 at 16-bit) — 2.4% increase, 3.3× compression |
> | **Llama-3 70B Q4KM size** | ~42GB (single 48GB consumer GPU) |

## Key Insights

> [!success] **The central villain across 5 algorithms is OUTLIERS — and the field's 4 years of progress is 5 different ways to handle the same root cause.**
>
> | Algorithm | Year | Mechanism | What it does to outliers |
> |---|---|---|---|
> | **LLM.int8** | 2022 | Split-precision math | Outlier dims → 16-bit path; bulk → 8-bit |
> | **SmoothQuant** | 2022-23 | Algebraic identity | Migrates outlier difficulty from activations to weights via X·W = (X/s)·(s·W) |
> | **GPTQ** | 2022-23 | Column-wise + error redistribution | Pushes leftover rounding error into not-yet-touched columns; errors cancel instead of accumulating |
> | **AWQ** | 2023 | Pre-rounding scaling of salient channels | 1% of weight channels (largest-activation multipliers) scaled up before rounding to hit better grid points |
> | **GGUF K-quants** | 2023+ | Per-group + double-quantization | Two-level block structure; per-group scales prevent global outlier dominance |
>
> **The structural insight (operator-mission-aligned)**: *"5 algorithms, 5 looks. What problem are they all solving? Outliers, every single one."* — same root cause, different mechanisms, all converge on the same anti-pattern. This **convergent-pattern within Layer 5** mirrors the cross-layer convergence in the [[end-to-end-compression-across-the-ai-stack-composes-multiplicatively-6-plus-independent-mechanisms-at-6-distinct-layers|Multi-Layer Compression Lesson]].

> [!success] **Per-group scaling is THE structural fix; metadata cost is small (~0.25 bit/weight).**
>
> Slice the tensor into groups (e.g., 64 weights per group). Each group gets its own absmax + scale. The outlier sits in just ONE of those groups (with a coarse scale). The other groups have ~10× finer scales — bulk regains natural precision. Cost: one extra scale per 64 weights ≈ 0.25 bit/weight metadata. **Every modern 4-bit format does this.**

> [!success] **NF4: smart grid placement matters as much as bit count.**
>
> With only 16 grid points (4 bits), where you place them across a bell curve determines effective resolution. Naive: 16 evenly-spaced. NF4: 16 at the **normal-distribution quantiles** — crowded near zero (where most weights live), sparse near the edges. Same bit count, dramatically better effective precision for normally-distributed weights.
>
> **Operator-mission generalization**: this is structurally identical to the K-Flat insight from [DFlash TPU Synthesis](src-google-tpu-dflash-diffusion-style-speculative-decoding-3x-speedup-2026-05-04.md) — quality-per-position compounds, quantity-per-position diminishes. **Convergent pattern across compression mechanisms**: smarter encoding > more bits.

> [!success] **The accuracy-vs-bits curve is HOCKEY-STICK shaped.**
>
> Empirical Llama-3 8B benchmarks:
>
> | Bits | Perplexity | Size | Compression | Quality cost |
> |---|---|---|---|---|
> | 16 (BF16) | 6.23 | 15.0 GB | 1× | baseline |
> | 8 (INT8) | 6.23 | 8.0 GB | 1.9× | 0% |
> | 5 (Q5_K_M) | 6.29 | 5.3 GB | 2.8× | 1.0% |
> | **4 (Q4_K_M)** | **6.38** | **4.58 GB** | **3.3×** | **2.4%** |
> | <3 | (cliff drops) | (smaller) | (>4×) | (catastrophic) |
>
> **Stay above the cliff (4-bit minimum for typical models) and the cost is small. Below 3-bit, the cliff is real.** This is the basis for the operator's M002 specialist LoRA target (Q4_K_M on RTX 4090).

> [!success] **Q4KM format decoded character-by-character: a precise recipe.**
>
> | Character | Meaning |
> |---|---|
> | **Q** | Quantized |
> | **4** | 4 bits per weight |
> | **K** | K-quants — per-group scales in a two-level block structure |
> | **M** | Medium variant — bulk weights at 4-bit; sensitive tensors bumped to 5 or 6-bit |
>
> Four characters, one precise recipe. Sister formats: Q5_K_M, Q3_K_M, Q2_K, IQ2_XS, etc. Each character is informative.

> [!success] **Llama-3 70B at Q4KM = 42GB = single 48GB consumer GPU. The 16-bit version needs 2× A100 (>$20,000).**
>
> Same model, same architecture, same weights. **The only thing that changed is how they are stored.** This is what makes consumer-hardware AI possible at the 70B-class.
>
> **Operator-mission directly aligned**: M002 specialist LoRA on Qwen3.6-27B (per [Custom-Model Concept](../../domains/cross-domain/custom-tailored-senior-engineer-tier-model-group-with-recreated-intelligence-layer-research-synthesis.md) Phase 2) at Q4KM fits comfortably in RTX 4090's 24GB VRAM with substantial headroom for KV cache + LoRA adapters.

> [!info] **Two myths refuted (operator-mission-relevant clarity).**
>
> | Myth | Reality |
> |---|---|
> | "Quantization halves quality" | False. Hockey-stick curve: 16→5 flat, dip at 4, cliff below 3. Q4KM costs ~2.4% perplexity for 3.3× compression. |
> | "AWQ keeps salient weights at 16-bit" | False. ALL weights stored at 4-bit uniformly. Salience is a numerical PRE-ROUNDING trick: salient channels multiplied by per-channel factor before rounding (so they hit a more accurate grid point); activations divided by same factor after matmul. Output unchanged; storage uniform. |
>
> **Operator-mission application**: per `feedback_research_not_abstract.md` — when operator names a specific format (Q4KM, NF4, AWQ), my role is to describe the SPECIFIC mechanism, not abstract patterns. This synthesis preserves that specificity.

## Deep Analysis

### Connection to Multi-Layer Compression Lesson — Layer 5 Convergence

[[end-to-end-compression-across-the-ai-stack-composes-multiplicatively-6-plus-independent-mechanisms-at-6-distinct-layers|Multi-Layer Compression Lesson]] lists Layer 5 (Model weights) substitutable mechanisms: BF16 baseline · FP8 · GGUF Q4_K_M · MXFP4 (gpt-oss-style) · Unsloth UD-IQ2 / Q2_K · Cloudflare Unweight (22% lossless).

**This synthesis adds the algorithmic genealogy** behind the format names:
- Q4_K_M / Q5_K_M / etc. = GGUF K-quants
- UD-IQ2 / Q2_K = sub-4-bit K-quants variants (Unsloth + Dettmers extensions)
- AWQ / GPTQ = checkpoint formats with their own loaders
- LLM.int8 / SmoothQuant = inference-time mechanisms (less common in checkpoint formats; more common in serving stacks)

**Convergent-pattern observation**: 5 algorithms × 1 root cause (outliers) is itself a convergent-pattern instance, parallel to the cross-layer convergence the parent lesson documents.

### Connection to Anti-Vendor-Lock-In Lesson — Layer 5 Substitutability

[[anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence|Anti-Vendor-Lock-In Lesson Evidence 11 (Trust-Layer)]] lists "Compression substrate" with Caveman + Unsloth + KV-cache. This synthesis enriches the operator's substitutability menu at Layer 5 (Model weights):

| Substitution axis | Options |
|---|---|
| Quantization format | BF16 · FP8 · INT8 · Q5_K_M · Q4_K_M · Q3_K_M · Q2_K · UD-IQ2 · IQ2_XS · NF4 · GPTQ · AWQ · MXFP4 · Bitnet ternary · FP4 microscaling |
| Algorithm choice | LLM.int8 · SmoothQuant · GPTQ · AWQ · K-quants |
| Tooling | llama.cpp · Unsloth · ExLlamaV2 · GPTQ-for-LLaMa · vLLM · transformers |
| Quality target | Lossless (BF16, Cloudflare Unweight) · 0%-cost (INT8) · ~1%-cost (Q5_K_M) · ~2.4%-cost (Q4_K_M) · sub-4-bit (Q2_K, UD-IQ2 — quality varies per base model) |

**No single vendor controls multiple Layer-5 axes simultaneously.**

### Connection to Custom-Tailored Model Group M002 — Specialist LoRA Substrate

[Custom-Tailored Model Group](../../domains/cross-domain/custom-tailored-senior-engineer-tier-model-group-with-recreated-intelligence-layer-research-synthesis.md) Phase 2 (First Specialist LoRA) targets:
- Qwen3.6-27B at UD-IQ2 (Unsloth) OR
- RLM-Qwen3-8B (recursive paradigm-aware base)

**This synthesis provides the algorithmic context for "UD-IQ2"**: sub-4-bit K-quants extension via Unsloth, depending on per-group scaling + smart-grid placement (NF4-style for normally-distributed sub-tensors). The operator's M002 plan is grounded in the production-validated 5-algorithm field.

### Connection to Operator's "Root-Cause-First" Mission Discipline

Operator-stated *"fix it at the root instead.. its not hard"* (CLAUDE.md sacrosanct directive). **This synthesis embodies the same discipline structurally**: 4 years of quantization research converged because 5 different teams identified ONE root cause (outliers) and addressed it 5 different ways. The field's progress IS root-cause-first work. **The operator's mission discipline is empirically validated by the field's own structural pattern.**

## Quotes (verbatim, from the transcript)

> *"70 billion numbers, each one four bytes wide, 280 GB bigger than any laptop, bigger than four data center GPUs combined. And yet, this exact model runs on your laptop, and it barely loses any quality."*

> *"At 6.7 billion parameters, something breaks. The orange line drops off a cliff. The dashed red line marks the moment when in Dettmers' words, the outliers emerge."*

> *"If most weights are tiny, we don't need precision out at the edges. We need it where the weights actually are."*

> *"Outliers are not a rare bug. They are the central villain that every modern algorithm exists to handle."*

> *"5 algorithms, 5 looks. What problem are they all solving? Outliers, every single one."*

> *"Once you see this, the field of LLM quantization stops looking like a zoo of disconnected tricks. It becomes one technique with several flavors."*

> *"Same model, same architecture, same weights. The only thing that changed is how they are stored."*

> *"Stay above the cliff and the cost is small."*

> *"The bell curve of weights stays the same."* (the doctrine endures across 4 years of algorithmic evolution)

## Open Questions

> [!question] Should the operator's M002 specialist LoRA target Q4_K_M or UD-IQ2 by default?
> Q4_K_M: 2.4% perplexity cost, 3.3× compression, well-validated. UD-IQ2: more aggressive (sub-4-bit), depends on base model's outlier characteristics. **Default proposal**: start with Q4_K_M for first specialist LoRA on Qwen3.6-27B; explore UD-IQ2 if VRAM headroom is needed for context budget. Operator-decision per workload.

> [!question] Does the 6.7B-param outlier-emergence threshold still hold for 2026 frontier models?
> The Dettmers chart was 2022. Newer models (Qwen3, Llama-3, DeepSeek V3/V4) likely follow the same pattern at scale (outliers emerge somewhere). Threshold may shift slightly with architecture changes (MoE vs dense, attention variants). **Tracking question**: revalidate when authoring M001 toolchain reproduction.

> [!question] Are there 6th-or-7th algorithms emerging beyond the 5 documented here?
> Operator-relevant emerging mechanisms: Bitnet (ternary weights), FP4 microscaling, Cloudflare Unweight (22% lossless). Each addresses outliers differently OR avoids them by structural design. **Track for additions to the 5-algorithm convergence**.

> [!question] Could the synthesis's 5-algorithm-1-root-cause framing become a doctrinal lesson?
> The structural pattern (multiple algorithms, one root cause, convergent-pattern within a layer) parallels the [[end-to-end-compression-across-the-ai-stack-composes-multiplicatively-6-plus-independent-mechanisms-at-6-distinct-layers|Multi-Layer Compression Lesson]]'s cross-layer convergence. **Default proposal**: capture as Layer-2 lesson "Convergent-pattern within a single layer reveals the root cause"; promote candidate.

> [!question] How does Q4_K_M compose with operator's L0-L4 trust opt-ins?
> At L2 (compressed-encrypted weights + on-GPU decypher via Triton): the encrypted form contains the Q4_K_M-encoded weights; decypher kernel decompresses + decrypts. Composition is operator-design-call when Trust-Layer Epic M001 reaches reference pipeline.

## Relationships

- BUILDS ON: [[end-to-end-compression-across-the-ai-stack-composes-multiplicatively-6-plus-independent-mechanisms-at-6-distinct-layers|Multi-Layer Compression Lesson]] — enriches Layer 5 with 5-algorithm convergence; reveals within-layer convergent-pattern parallel to cross-layer
- BUILDS ON: [[anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence|Anti-Vendor-Lock-In Lesson]] — Layer 5 substitutability axes documented per algorithm + format
- BUILDS ON: [[custom-tailored-senior-engineer-tier-model-group-with-recreated-intelligence-layer-research-synthesis|Custom-Tailored Model Group Concept]] — M002 specialist LoRA substrate documentation (Q4_K_M / UD-IQ2 algorithmic foundation)
- BUILDS ON: [[src-unsloth-fast-lora-consumer-hardware|Unsloth Synthesis]] — Unsloth's UD-IQ2 + Q2_K are sub-4-bit K-quants variants documented here
- RELATES TO: [[src-google-tpu-dflash-diffusion-style-speculative-decoding-3x-speedup-2026-05-04|DFlash TPU Synthesis]] — sister "smart-encoding-over-more-bits" insight; quality-per-position compounds, quantity-per-position diminishes
- RELATES TO: [[src-deepseek-v4-token-wise-compression-dsa-sparse-attention-1m-context-default-2026-04|DeepSeek V4 DSA Synthesis]] — DSA attention compression at Layer 6; this synthesis covers Layer 5 weight quantization; together they cover the full server-runtime compression surface
- DEMONSTRATES: [[infrastructure-over-instructions-for-process-enforcement|Principle 1 — Infrastructure Over Instructions]] — quantization is infrastructure (loss functions + bit-packing schemes + grid placements); not "remember to compress" prose
- DEMONSTRATES: [[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4 — Declarations Aspirational Until Verified]] — claims about quantization quality verified empirically (Llama-3 8B Q4_K_M = 6.38 perplexity); not aspirational
- DEMONSTRATES: [[goldilocks-protocol|Goldilocks Protocol]] — pick quantization format per workload (BF16 for training; Q5_K_M for high-quality serving; Q4_K_M for consumer-hardware deployment; Q2_K only when VRAM-constrained)

## Backlinks

[[Multi-Layer Compression Lesson]]
[[Anti-Vendor-Lock-In Lesson]]
[[custom-tailored-senior-engineer-tier-model-group-with-recreated-intelligence-layer-research-synthesis|Custom-Tailored Model Group Concept]]
[[Unsloth Synthesis]]
[[src-google-tpu-dflash-diffusion-style-speculative-decoding-3x-speedup-2026-05-04|DFlash TPU Synthesis]]
[[DeepSeek V4 DSA Synthesis]]
[[infrastructure-over-instructions-for-process-enforcement|Principle 1 — Infrastructure Over Instructions]]
[[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4 — Declarations Aspirational Until Verified]]
[[Goldilocks Protocol]]
