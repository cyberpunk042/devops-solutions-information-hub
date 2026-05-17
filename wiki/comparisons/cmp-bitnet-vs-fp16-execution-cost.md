---
title: BitNet b1.58 Ternary vs FP16 Baseline — Execution Cost Comparison
aliases:
  - "BitNet b1.58 Ternary vs FP16 Baseline — Execution Cost Comparison"
  - "Ternary vs FP16"
  - "BitNet b1.58 vs FP16"
type: comparison
layer: 3
maturity: growing
domain: ai-models
status: synthesized
confidence: high
created: 2026-05-15
updated: 2026-05-15
sources:
  - id: src-bitnet-b158-ternary-llm
    type: wiki
    file: "wiki/sources/src-bitnet-b158-ternary-llm.md"
    title: "Synthesis — BitNet b1.58 Ternary LLM Family and bitnet.cpp Inference"
  - id: concept-1bit-ternary-weights
    type: wiki
    file: "wiki/domains/ai-models/concept-1bit-ternary-weights.md"
    title: "Concept — 1-bit Ternary Weights"
  - id: src-zen5-avx512-single-cycle
    type: wiki
    file: "wiki/sources/src-zen5-avx512-single-cycle.md"
    title: "Synthesis — AMD Zen 5 Single-Cycle 512-bit AVX-512"
tags:
  - comparison
  - ai-models
  - bitnet
  - ternary
  - fp16
  - quantization
  - cpu-inference
  - gpu-inference
  - execution-cost
  - memory-bandwidth
  - energy-efficiency
  - sain-01
---

# BitNet b1.58 Ternary vs FP16 Baseline — Execution Cost Comparison

## Summary

Two execution profiles for the same logical transformer architecture: **BitNet b1.58 ternary** (weights ∈ `{−1, 0, +1}`, 1.585 bits/param, matmul collapses to integer add/sub/skip) vs **FP16 baseline** (full-precision weights, traditional FPU multiply-accumulate). This page evaluates the trade-off head-to-head along the dimensions that matter for the [[src-sain-01-sovereign-node-spec|SAIN-01]] deployment: where each runs, what each costs in memory + bandwidth + energy, where each is fastest, and where each is the right pick. **Headline result**: at 3B+ parameters, ternary matches FP16 on accuracy + delivers 2.71× faster CPU inference + 3.55× less memory + 71-82% energy reduction on x86. Below 3B, FP16 wins on quality; above 100B, ternary unlocks CPU-only inference at human-reading speed (5-7 tok/s) — a regime FP16 cannot reach without a $20K+ GPU. The choice is workload-conditioned: ternary for orchestration / background / state-routing / energy-constrained deployments; FP16 for deep reasoning + creative generation + workloads below the 3B accuracy threshold.

## Comparison Matrix

> [!abstract] BitNet b1.58 Ternary vs FP16 Baseline
>
> | Dimension | BitNet b1.58 (ternary) | FP16 baseline |
> |---|---|---|
> | **Weight representation** | `{−1, 0, +1}` ternary, packed at 2 bits/param | 16-bit floating point per param |
> | **Storage per parameter** | 1.585 bits info, 2 bits packed | 16 bits |
> | **Matmul arithmetic** | Integer add / subtract / skip | FP fused multiply-accumulate |
> | **FPU usage during inference** | None (integer pipeline) | Primary (FP multiply-accumulate) |
> | **Where it runs best** | CPU (wide SIMD + VNNI) | GPU (Tensor Cores, FP16 native) |
> | **Memory footprint (3B model weights)** | ~0.75 GB (2-bit packed) | ~6 GB |
> | **Memory footprint (8B model weights)** | ~2 GB | ~16 GB |
> | **Throughput on consumer CPU (100B model)** | 5-7 tok/sec | not feasible without GPU |
> | **Throughput vs FP16 LLaMA at 3B (Microsoft bench)** | **2.71× faster** | baseline 1× |
> | **GPU memory (3B model)** | 3.55× less than FP16 baseline | baseline 1× |
> | **Energy on x86 CPU** | **71.9-82.2% reduction** | baseline 1× |
> | **Energy on ARM CPU** | 55.4-70.0% reduction | baseline 1× |
> | **Accuracy at 3B (perplexity + downstream)** | **matches FP16 LLaMA** | baseline 1× |
> | **Accuracy at 700M / 1.3B** | trails FP16 measurably | wins |
> | **Accuracy at 8B+** | matches or exceeds FP16 (per Llama3-8B-1.58 + Falcon3) | baseline |
> | **Training cost** | Comparable to FP (specialized quant-aware passes required) | Standard (well-tooled) |
> | **Production-ready model availability** | microsoft/bitnet-b1.58-2B-4T (Apr 2025), Llama3-8B-1.58, Falcon3 / Falcon-E b1.58 family | Universe of FP16 / BF16 models (millions of fine-tunes) |
> | **Inference framework** | `bitnet.cpp` (Microsoft official, CPU + GPU since May 2025) | vLLM, llama.cpp, transformers, TensorRT-LLM (mature ecosystem) |
> | **Hardware lock-in** | Wide CPU SIMD (Zen 5 single-cycle AVX-512 ideal; ARM via NEON; Apple Silicon) | GPU strongly preferred (CUDA Tensor Cores, ROCm) |
> | **PCIe bus pressure** | None (CPU-resident) | Constant (GPU prefill + KV cache transfers) |

## Key Insights

> [!abstract] The compute profile inverts
>
> FP16 inference is **FPU-bound** — the FPU is the bottleneck and Tensor Cores are the architectural response. Ternary inference is **memory-bandwidth-bound** + **integer-pipeline-bound** — wide SIMD + VNNI (CPU) is the architectural response. This isn't "quantization makes things faster"; it's a categorical shift in which silicon does the work. ([[concept-1bit-ternary-weights|1-bit Ternary Weights concept]])

> [!tip] The 3B threshold is where ternary becomes a free upgrade
>
> Below 3B parameters, ternary trails FP16 on accuracy benchmarks measurably — pick FP16 if quality matters more than throughput. **At 3B and above**, ternary matches FP16 in perplexity + downstream tasks while delivering 2.71× faster CPU inference + 3.55× less memory + 71-82% energy reduction. There's no accuracy cost; the only cost is training-side tooling (which Microsoft has now released open-source). ([[src-bitnet-b158-ternary-llm|BitNet b1.58 synthesis]])

> [!success] Ternary unlocks regimes FP16 cannot reach
>
> A 100B-parameter ternary model runs on a single consumer CPU at 5-7 tok/sec (above human reading speed). The FP16 equivalent would need ~200GB VRAM (= an H100 + a B100, or NVL36 / NVL72 server) at $20K-100K+ entry cost. Ternary is not just "FP16 but cheaper" — it's a regime FP16 cannot enter on consumer hardware. For sovereign / local-first deployments, this is decisive. ([[src-bitnet-b158-ternary-llm|BitNet b1.58 synthesis]])

> [!warning] The asymmetry isn't symmetric across model sizes
>
> Ternary's win narrows on GPU (where FP16 already runs efficiently on Tensor Cores) and widens on CPU. The technique was conceived around CPU bandwidth limits; on GPU, the FPU isn't the bottleneck for FP16 inference. The May 2025 GPU support for `bitnet.cpp` is closing this gap — but as of Q2 2026, **ternary is most differentiating on CPU**, FP16 remains dominant on GPU.

> [!info] Energy is the under-rated dimension
>
> 71-82% energy reduction on x86 sounds like a power-bill optimization, but for the SAIN-01 use case it has a load-bearing architectural consequence: a CPU-resident ternary model can run **continuously** as the [[concept-srp-trinity-pulse-weaver-auditor|Conductor Agent]] without thermal pressure on the GPUs. The Blackwell stays cool and ready for the heavier reasoning workloads. The Trinity's CPU/GPU asymmetry is partly an energy story.

## Deep Analysis

### Where each path runs best

**BitNet b1.58 ternary** — the FPU sits idle during inference; the work happens in the integer execution units + memory bandwidth path. The optimal substrate is a CPU with:

- Wide SIMD registers (512-bit on Zen 5 single-cycle, NEON 128-bit on ARM)
- VNNI / matrix-multiply integer instructions (VPDPBUSD on Intel/AMD, equivalent on ARM)
- Large L3 cache to hold the per-layer working set (32MB per CCD on [[concept-dual-ccd-cache-partitioning-9900x|Zen 5 9900X]])
- High memory bandwidth (DDR5-6000+ for desktop, HBM3 if available)

The [[src-zen5-avx512-single-cycle|Zen 5 9900X]] satisfies all of these properties and is essentially the ideal consumer CPU for ternary inference as of Q2 2026. Apple Silicon's M-series chips are competitive on ARM. Server-class chips (Sapphire Rapids, Zen 5 Epyc) deliver more throughput per box but at server cost.

**FP16 baseline** — the work happens primarily in FPU / Tensor Cores. The optimal substrate is a GPU with:

- Native FP16 / BF16 execution units (NVIDIA Tensor Cores, AMD CDNA matrix cores)
- High HBM bandwidth (HBM3 / HBM3e on H100 / H200 / B200; GDDR7 on Blackwell PRO 6000)
- Large VRAM (96GB on Blackwell, 80GB on H100)
- Mature CUDA / ROCm software stack

The Blackwell RTX PRO 6000 (the SAIN-01 Oracle Core's substrate) is the FP16-target hardware. The 24GB RTX 3090 is mid-tier; serves quantized + FP16 mid-scale.

### Where each path WINS on the SAIN-01 architecture

| Tier | Workload | Best fit | Reasoning |
|---|---|---|---|
| **Conductor (Pulse) on CPU** | State routing, intent classification, sub-millisecond branching | **Ternary** | Single-cycle 512-bit AVX-512 + VNNI; sub-MB working set fits L1d; energy-zero idle |
| **Logic Engine on 3090** | Parsing, JSON compilation, regex extraction, embedding generation | **FP16 mid-scale** (Llama-3-70B at Q4_K_M or Qwen3-30B at FP16) | GPU's parallel throughput; 24GB ceiling; needs Tensor Cores |
| **Oracle Core on Blackwell** | Deep reasoning, codebase analysis, long-context synthesis | **FP16 (or BF16) large-scale** | 96GB VRAM headroom; Tensor Cores; uncompromised precision |
| **Background autonomic loop** | Continuous state monitoring, log auditing | **Ternary** | CPU-resident, GPU stays asleep, energy-zero |
| **Burst reasoning under deadline** | Multi-turn complex analysis | **FP16 (Oracle Core)** | Higher quality per second matters more than energy |

The tier-by-tier mapping isn't an aesthetic choice — each tier picks the technique that's structurally fastest for its workload class.

### Per-dimension analysis

#### Storage + memory footprint

A 3B-parameter ternary model fits in **~0.75 GB** of weight storage (2-bit packed) vs **~6 GB** for FP16. The 8× savings is uniform across model sizes:

| Model size | Ternary weights | FP16 weights | Ratio |
|---|---|---|---|
| 700M | ~175 MB | ~1.4 GB | 8× |
| 1.3B | ~325 MB | ~2.6 GB | 8× |
| 3B | ~750 MB | ~6 GB | 8× |
| 8B | ~2 GB | ~16 GB | 8× |
| 70B | ~17.5 GB | ~140 GB | 8× |
| 100B | ~25 GB | ~200 GB | 8× |
| 290B (Ling-Plus, hypothetical b1.58) | ~72 GB | ~580 GB | 8× |

The 8× factor is approximate — packing overhead, scale factors, LayerNorm parameters, and per-block metadata add ~5-10% on top of the raw 2-bit weights, but the rough ratio holds.

**Implication for SAIN-01**: a 100B ternary model fits in 25 GB — comfortably in the 96 GB Blackwell's VRAM with 70+ GB headroom for KV cache + activations. The same model at FP16 wouldn't fit on the Blackwell at all. A 290B ternary model (e.g., a hypothetical Ling-Plus-b1.58) would fit on the Blackwell. A 290B FP16 model needs multi-GPU.

#### Matmul arithmetic

| Operation | Ternary path | FP16 path |
|---|---|---|
| Weight load | LUT decode of 2-bit packed weight | Direct FP16 load |
| Multiply | None (encoded in the lookup table) | FP multiply (16-bit × 16-bit → 32-bit) |
| Accumulate | INT32 add / subtract | FP add (16-bit → 32-bit) |
| Per-cycle SIMD throughput on Zen 5 ZMM | 64 INT8 lanes × VNNI VPDPBUSD = up to 256 ternary ops/cycle (LUT-accelerated) | 32 FP16 lanes × FMA = 32 multiply-add/cycle |
| Per-cycle SIMD throughput on Tensor Core | irrelevant (FPU bypassed for ternary path) | hundreds of FP16 ops/cycle |

The ternary path has higher per-cycle throughput on CPU because integer ALUs are wider and VNNI VPDPBUSD is exactly the kind of bandwidth-saturating instruction the wide SIMD path optimizes. The FP16 path has higher per-cycle throughput on GPU because Tensor Cores are purpose-built for FP16 matmul.

**Categorical statement**: ternary inference is bandwidth-bound; FP16 inference is FPU-bound. They live on different silicon for a reason.

#### Energy

Microsoft reports 71.9-82.2% energy reduction on x86 CPUs and 55.4-70.0% on ARM. This isn't just "fewer joules per inference"; it's "the CPU doesn't dissipate as much heat per token."

For the SAIN-01 deployment:

- A continuous Conductor Agent at ~5 W average draw (estimated) does not stress the cooling system.
- The same FP16 model on GPU would draw 200-400 W continuously — would require sustained cooling capacity, would heat the chassis enclosure, would generate audible fan noise during low-traffic periods.

The energy story is what makes "always-on" CPU-resident inference architecturally viable. FP16-on-GPU is a "fire-and-cool-down" pattern; ternary-on-CPU is a "always-warm-never-hot" pattern.

#### Accuracy

Below 3B, ternary trails FP16 by a measurable margin (3-10% on standard benchmarks per the original BitNet b1.58 paper). At 3B+, ternary matches FP16 in perplexity + downstream tasks. At 8B (Llama3-8B-1.58), ternary at-or-slightly-better than FP16 on reasoning + math benchmarks per Microsoft's reported numbers.

The accuracy story has a sharp threshold:

- 700M-1.3B: FP16 wins
- 2-3B: parity (BitNet b1.58 catches up)
- 3B+: ternary often equal-or-better

The SAIN-01 spec's choice of a 3B-class Conductor (or 2B official) sits at the parity threshold — picking ternary doesn't cost accuracy.

#### Training cost

Both paths cost roughly the same to train when amortized across model size. Ternary requires quantization-aware training (BitLinear-aware optimizer, calibration of absmean/absmax scales) which is non-trivial to implement but Microsoft has released the open-source tooling. FP16 training is standard and mature.

**For the SAIN-01 deployment**, this dimension is moot — both paths consume *pre-trained* released checkpoints. The operator doesn't train models from scratch. The choice is purely runtime.

## Recommendation

> [!success] Pick per workload tier, not per model
>
> | Your workload | Pick | Why |
> |---|---|---|
> | State routing, intent classification, branching decisions | **Ternary on CPU** (Conductor Pulse) | Sub-millisecond branching beats GPU scheduling; energy-zero |
> | Parsing, JSON compilation, regex extraction | **FP16 mid-scale on 3090** (Logic Engine) | 24GB ceiling fits 30-70B at Q4-Q8; structured output is GPU-friendly |
> | Deep reasoning, codebase analysis, multi-turn synthesis | **FP16 large on Blackwell** (Oracle Core) | Uncompromised quality matters; 96GB VRAM accommodates large models |
> | Continuous background monitoring | **Ternary on CPU** | Energy-zero; never wakes the GPU |
> | Code generation with low entropy (math, structured output) | **FP16 + DFlash speculative decoding** on Blackwell | Compounding accelerations on the right entropy profile |
> | Long-form creative generation | **FP16 (Blackwell)** | DFlash degrades; ternary's quality cost not worth it |
> | < 3B model size requirement | **FP16** | Below ternary's accuracy threshold |
> | Air-gapped / offline / sovereignty-critical | **Ternary on CPU** | Removes GPU + PCIe dependency entirely |

> [!warning] Anti-patterns to avoid
>
> - **Don't treat ternary as "cheap FP16."** It's a different execution profile. Workloads where FP16 wins on quality won't be served by ternary regardless of cost.
> - **Don't pick FP16 by default for orchestration tier.** The Conductor's job is sub-millisecond branching — FP16-on-GPU adds GPU-context-switch latency on every state read. Ternary-on-CPU is structurally faster for this workload class.
> - **Don't run ternary on GPU just because `bitnet.cpp` supports it.** The technique was conceived around CPU bandwidth limits; on GPU you're paying the GPU's overhead without claiming its FP-throughput advantage. The May 2025 GPU support is for cases where GPU is the only option, not for cases where CPU is.
> - **Don't deploy a custom ternary-trained model without verifying the Microsoft training recipe.** The technique requires quantization-aware training; off-the-shelf FP16 → b1.58 conversion produces lossy approximations, not lossless.

## Relationships

- BUILDS ON: [[src-bitnet-b158-ternary-llm|BitNet b1.58 synthesis]]
- BUILDS ON: [[concept-1bit-ternary-weights|1-bit Ternary Weights concept]]
- BUILDS ON: [[src-zen5-avx512-single-cycle|Zen 5 AVX-512 synthesis]]
- USED BY: [[src-sain-01-sovereign-node-spec|SAIN-01 Sovereign Node Spec]] (Conductor Pulse on CPU = ternary; Oracle Core on Blackwell = FP16)
- COMPLEMENTS: [[cmp-dflash-vs-eagle3-vs-medusa|DFlash vs EAGLE-3 vs MEDUSA comparison]] (orthogonal acceleration on the FP16 GPU side)
- RELATES TO: [[local-llm-quantization|Local LLM Quantization]] (broader landscape — 4-bit, 8-bit; ternary is the most aggressive end)
- RELATES TO: [[concept-dual-ccd-cache-partitioning-9900x|Dual-CCD Cache Partitioning]] (the substrate that makes ternary CPU inference fast)

## Backlinks

[[BitNet b1.58 synthesis]]
[[1-bit Ternary Weights concept]]
[[Zen 5 AVX-512 synthesis]]
[[SAIN-01 Sovereign Node Spec]]
[[DFlash vs EAGLE-3 vs MEDUSA comparison]]
[[local-llm-quantization|Local LLM Quantization]]
[[Dual-CCD Cache Partitioning]]
