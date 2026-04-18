---
title: "Synthesis — AirLLM: Layer-Wise Inference with NVMe SSD Offload"
aliases:
  - "Synthesis — AirLLM: Layer-Wise Inference with NVMe SSD Offload"
  - "Synthesis: AirLLM"
  - "AirLLM Source Synthesis"
type: source-synthesis
layer: 1
maturity: growing
domain: ai-models
status: synthesized
confidence: high
created: 2026-04-17
updated: 2026-04-17
sources:
  - id: src-airllm-github
    type: repository
    url: https://github.com/lyogavin/airllm
    file: raw/articles/lyogavinairllm.md
    title: "AirLLM — GitHub Repository (lyogavin/airllm)"
    ingested: 2026-04-17
  - id: src-airllm-datasharepro-review
    type: article
    url: https://datasharepro.in/airllm/
    file: raw/articles/airllm-review-democratizing-access-vs-the-unavoidable-physics-of-latency-datasha.md
    title: "AirLLM Review: Democratizing Access vs. The Unavoidable Physics of Latency"
    ingested: 2026-04-17
tags: [airllm, local-llm, layer-wise-inference, ssd-offload, nvme, quantization, batch-inference, cost-optimization, aicp]
---

# Synthesis — AirLLM: Layer-Wise Inference with NVMe SSD Offload

## Summary

AirLLM is a Python library (Apache-2.0, HuggingFace-compatible) that runs 70B-parameter language models on a 4GB GPU, and Llama 3.1 405B on 8GB VRAM, by streaming one transformer layer at a time from disk to GPU instead of loading the whole model into VRAM. The mechanism is structurally elegant and immediately accessible — `pip install airllm`, four lines of Python, exact same API as Hugging Face Transformers. The operational reality is harsher: the latency bottleneck migrates from VRAM capacity to disk throughput. On a Gen4 NVMe SSD (~7 GB/s), a 4-bit-quantized 70B model (~40 GB) takes ~5.7 seconds per generated token. A 405B model on 8GB slows to 0.02–0.05 tok/s — a 2000-token response can literally take hours. AirLLM therefore is NOT a drop-in replacement for interactive inference; it is a new routing tier for the $0-target model: batch processing, offline pipelines, privacy-preserving on-premise work, prototyping decisions about whether a larger model is worth the cloud cost before paying for it.

## Key Insights

> [!info] AirLLM shifts the bottleneck, it does not remove it
> VRAM stops being the limit. Disk throughput becomes the limit. For a 4-bit-quantized 70B model on Gen4 NVMe: 40 GB ÷ 7 GB/s ≈ **5.7 seconds per token**. This is not a marginal slowdown — it is a paradigm shift in *where* the cost lives.

> [!tip] The NVMe SSD is now the load-bearing component
> Whatever VRAM you have, the effective model size is limited by **NVMe capacity and read bandwidth**, not VRAM. Operator's 19 GB VRAM upgrade matters — but with AirLLM, the *next* upgrade that matters is a fast NVMe drive with enough free space to hold decomposed layer shards plus the Hugging Face cache.

- **Layer-wise inference is the core mechanism.** Instead of holding the whole model in VRAM, AirLLM loads one layer (or a small group) at a time: stream from SSD → compute on GPU → free VRAM → load next layer → repeat for every layer, for every token. The GPU never holds more than a fraction of the model. This is conceptually simple but mechanically complex — it requires decomposing Hugging Face models into per-layer shards and managing the streaming lifecycle.

- **The API is frictionless.** `AutoModel.from_pretrained(...)` is the same call shape as Hugging Face Transformers. A 70B model loads with the same idiom as a 7B model. This is a deliberate design choice — the library does not ask the user to learn a new API surface. The user gets to write standard Transformers code and *never thinks about layer streaming* — that happens transparently inside `generate()`.

- **"No quantization required" is rebranded marketing.** AirLLM supports a `compression='4bit'` / `'8bit'` flag that applies block-wise quantization via `bitsandbytes` — this *is* quantization. The marketing line ("70B on 4GB *without quantization*") refers to running full-precision weights layer-by-layer; the 4bit flag is an *optional* 3× speedup. So the honest framing is: you *can* run without quantization if you can tolerate the latency; you will almost always want the 4bit compression in practice, which is standard quantization under a different name.

- **Model decomposition is one-time but disk-heavy.** The first inference call decomposes the Hugging Face model into layer-wise shards and caches them. This process is disk-intensive. The library has a `delete_original` flag that removes the original HF download after decomposition to save ~50% disk space. Running AirLLM without sufficient SSD free space causes `MetadataIncompleteBuffer` errors — the library's own FAQ lists this as #1.

- **Prefetching overlaps load and compute for ~10% speedup.** v2.5+ supports prefetching (loading the next layer while the current layer computes). This is on by default for AirLLMLlama2. It is a mechanical optimization that partially masks the disk I/O cost — but it cannot close the gap with in-memory inference. It narrows the latency hit, not closes it.

- **MacOS/Apple Silicon is supported via MLX.** The same library runs on Apple Silicon via `mlx` — this connects AirLLM to the same solution space as [[src-turboquant-122b-macbook|TurboQuant]] (122B on MacBook M4 Max). MacOS unified memory changes the math: Apple Silicon has no discrete VRAM, so layer streaming is from unified memory, which is materially faster than disk streaming — latency between TurboQuant and AirLLM on MacOS may converge for appropriately-sized models.

- **Supported models cover the top of the open LLM leaderboard.** Llama (through 3.1), Mixtral, ChatGLM, QWen (through 2.5), Baichuan, Mistral, InternLM — the major open-weight families. CPU inference was added in v2.10.1 (2024-08), extending the reach to machines without any discrete GPU at all.

- **The last release was 2024-08 (v2.11.0, Qwen2.5 support).** This matters: the library has not been updated since. Llama 3.3, Llama 4, newer Qwen/Mistral families are not officially in-scope. For operator's use case this is borderline — the library still works with in-support models, but betting infrastructure on an unmaintained library is a risk.

## Deep Analysis

### The Math — Why Disk Bandwidth is the Ceiling

The core equation for per-token latency under layer-wise inference:

> [!abstract] Per-Token Latency = Model Size / Effective Read Bandwidth + Compute Time
>
> | Model | 4-bit Size | Gen4 NVMe (7 GB/s) | Sata SSD (0.5 GB/s) | HDD (0.2 GB/s) |
> |-------|------------|---------------------|----------------------|-----------------|
> | Llama 3 8B | ~4.5 GB | 0.6 s/tok | 9 s/tok | 23 s/tok |
> | Llama 3 70B | ~40 GB | 5.7 s/tok | 80 s/tok | 200 s/tok |
> | Llama 3.1 405B | ~230 GB | 33 s/tok | ~460 s/tok | hours/tok |
>
> Compute time on the GPU is small relative to transfer time for the models that motivate AirLLM. The dominant term is the sequential disk read per token. This is why the datasharepro.in review calls AirLLM "waiting for 70B on 4GB" — the GPU spends most of its wall-clock time IDLE, waiting for the next layer to arrive.

The practical implication for operator: **the planned work involves running a 70B-class model on 19 GB VRAM**. Without AirLLM, a 70B-Q4 (~40 GB) does not fit in 19 GB VRAM — it can't run at all. With AirLLM and a Gen4 NVMe SSD, it runs at ~5.7 s/tok. A 500-token response = ~47 minutes. A 2000-token batch output = ~3 hours. This is the concrete trade-off.

### MoE Changes the Math — gpt-oss Correction (NEW)

> [!warning] The batch-only framing above assumes DENSE models. For MoE models with low active-parameter ratios, the math is different and the conclusion inverts.

The per-token latency derivation — "40 GB ÷ 7 GB/s = 5.7 s/tok" — assumes every weight participates in every token. That is true for Llama 3 70B (dense). It is **NOT true for Mixture-of-Experts models**. MoE routing activates only a subset of parameters per token; layer-offload engines that are MoE-aware stream only the ACTIVE experts, not the full weight set.

Concrete contrast using [[src-gpt-oss-openai-open-weight-moe|gpt-oss-120b]] (117B total, 5.1B active, MXFP4 native):

| Model class | Per-token read | Gen4 NVMe latency | Usable for |
|-------------|---------------|--------------------|------------|
| Llama 3 70B dense Q4 | ~40 GB | 5.7 s/tok | Batch only |
| **gpt-oss-120b MoE MXFP4** | **~2.5-3 GB (active experts + shared)** | **0.35-0.5 s/tok = 2-3 tok/s** | **Agent-viable, tool-augmented workflows** |
| DeepSeek V3 MoE (671B / 37B active) | ~18 GB MXFP4-equivalent | 2.5 s/tok | Substantive reasoning, slow but usable |
| Mixtral 8x22B MoE | ~12 GB at Q4 | 1.7 s/tok | Interactive-adjacent, good for agents |

**The correction**: AirLLM is not a strictly batch-tier tool. It is a **layer-offload mechanism**, and its usable latency depends on the *active* bandwidth per token, which for MoE models is a small fraction of the total. With gpt-oss-120b as the driving example, disk-offload moves from "overnight batch only" into "tool-augmented agent loops where a 1-5 second step latency is acceptable."

**Caveat — MoE-aware streaming is an engine-level feature, not automatic.** AirLLM v2.7+ added `AirLLMMixtral` (explicit MoE support for Mixtral). Whether gpt-oss works out-of-the-box on AirLLM is NOT confirmed as of the library's 2024-08 v2.11.0 (gpt-oss released 2025-08 — a year later). For near-term gpt-oss-120b-on-NVMe deployment, more current targets are:
- **llama.cpp with `-ngl N`** — explicit partial-GPU-offload, MoE-aware, actively maintained
- **vLLM with offload** — production-grade, day-0 gpt-oss support, MoE routing built in
- **transformers `device_map='auto'` + `offload_folder`** — simplest Python path, works with HuggingFace checkpoints

AirLLM's conceptual contribution (layer streaming) remains; the specific library may not be the execution path for gpt-oss. Budget for tool-integration effort, not library substitution.

### Production Reality — Where AirLLM Fits and Where It Breaks

> [!success] AirLLM is an excellent fit for:
> - **Prototyping decisions before paying cloud cost.** Want to know if a 70B is worth Vertex/Anthropic cost for your task? Validate with AirLLM on your NVMe first.
> - **Offline batch processing.** Document extraction from a large corpus. Summarization of thousands of long-form articles. Synthetic data generation. Overnight runs.
> - **Privacy-preserving on-premise inference.** Legal, medical, internal-sensitive contexts where data must never leave the host. AirLLM runs fully offline post-download.
> - **Education and architecture exploration.** Inspect layer-by-layer what a 70B model does, without cloud access. For research into model internals, the serial loading is actually a feature — you can hook each layer.
> - **Validation phase of AICP complexity-scoring research.** Can a 70B local pass what cloud does on specific task classes? AirLLM lets the question be asked without paying first.

> [!warning] AirLLM is the wrong tool for:
> - **Interactive chat or agent loops.** Time-to-first-token is seconds to minutes. Breaks flow state. Unusable for conversational work.
> - **Multi-user serving.** Layer-wise inference is fundamentally sequential; cannot batch across requests. One request monopolizes the pipeline.
> - **Fine-tuning or training.** AirLLM is strictly an inference engine. No backward pass, no gradient updates.
> - **Low-latency requirements.** Any SLA tighter than "overnight" rules it out for in-scope tasks.
> - **Machines without fast storage.** On a laptop HDD or slow SATA SSD, the latency moves from "slow" to "unusable." Gen4 NVMe or better is a practical floor.

### Answering the Operator's NVMe SSD Question

> [!question] "I wonder if the best solution is not to use my NVMe SSD space!?"
>
> **Answer: Yes — that is precisely what AirLLM does, and your NVMe SSD IS the load-bearing component.** The question has a real answer with real numbers:

AirLLM's entire value proposition is: **move the model weights to disk, load one layer at a time from disk to GPU, run it, discard, load the next layer**. The disk is not merely cold storage — it is the *active* memory hierarchy for every token generated. Every NVMe GB you can dedicate is an extra GB of model parameters you can run.

For the operator's specific situation (19 GB VRAM + presumed Gen4 NVMe SSD):

| Strategy | VRAM fit | NVMe capacity demand | Latency | Use case |
|----------|----------|----------------------|---------|----------|
| All-in-VRAM 13B Q4 | 7 GB | 7 GB | 20-60 tok/s | Interactive chat, agent loops, code assistance |
| All-in-VRAM 27B Q4 distilled (Qwopus) | 16 GB | 16 GB | 10-30 tok/s | Reasoning with tool-calling (verified by [[src-qwopus-claude-opus-reasoning-distilled-qwen-27b\|Qwopus]]) |
| AirLLM 70B Q4 with 19 GB VRAM | 4-8 GB at a time | ~45 GB free | 5-6 s/tok (maybe 2-3 s/tok with prefetch) | Offline batch, overnight synthesis, prototyping |
| AirLLM 405B Q4 with 19 GB VRAM | 4-8 GB at a time | ~230 GB free | 10-30 s/tok | Research-grade validation, experimental |

The useful mental model: **VRAM sets the latency floor; NVMe capacity sets the capability ceiling.** With 19 GB VRAM, you can run 27B-class models interactively without AirLLM — that's [[src-qwopus-claude-opus-reasoning-distilled-qwen-27b|Qwopus]]'s tier. With AirLLM + enough NVMe, you can *also* run 70B-405B-class models for offline/batch work. These are NOT competing strategies — they are **complementary routing tiers**.

### Strategic Placement in the AICP Routing Model

[[model-local-ai|Model — Local AI]] currently defines a 4-tier routing stack: simple → local · moderate → cloud-light · complex → cloud-standard · novel → cloud-heavy. AirLLM adds a **new tier between local and cloud-light**:

> [!info] Extended routing stack with AirLLM "local-batch" tier
>
> | Tier | Target backend | Latency | Use when |
> |------|---------------|---------|----------|
> | **local-interactive** | Qwen3/Gemma4 in-VRAM | 10-60 tok/s | Short-context, deterministic, real-time |
> | **local-reasoning** | Qwopus 27B in-VRAM (needs 19GB+) | 10-30 tok/s | Complex reasoning with tool-calling, still real-time |
> | **local-batch (NEW via AirLLM)** | 70B-405B streamed from NVMe | 0.05-2 tok/s | Offline synthesis, batch extraction, privacy-locked work, capability validation |
> | **cloud-light** | Opus 4.6 + medium | seconds | Context-heavy, inference-reliant, backward-compat |
> | **cloud-standard** | Opus 4.7 + high | seconds | Standard implementation, multi-turn |
> | **cloud-heavy** | Opus 4.7 + xhigh | seconds | Architecture, novel synthesis, deep review |

The key operational distinction: **local-batch is latency-agnostic by design**. It is the tier where a job runs overnight against a corpus and costs $0. A wiki-wide semantic re-ranking, a full-repo architectural review, a 200-document synthesis — these become *locally* viable at $0 with AirLLM, where previously they would have been routed to the cloud ($$) or abandoned for cost.

This tier is NOT replacing the interactive tiers. It is a net addition, aimed at a task class that was either ignored or cloud-routed.

### Connection to the Aspirational-Declaration Principle

> [!abstract] AirLLM's marketing is a classroom case of Principle 4
>
> The claim **"70B on 4GB VRAM without quantization"** is, as a declaration, true *structurally* (the model does run on that hardware) and false *operationally* (it runs at 0.1 tok/s, which for most use cases means "it does not run"). This is a textbook instance of [[declarations-are-aspirational-until-infrastructure-verifies-them|Declarations Are Aspirational Until Infrastructure Verifies Them]] — specifically the same layer as [[structural-compliance-is-not-operational-compliance|Structural Compliance Is Not Operational Compliance]].
>
> **The gate that would make the declaration honest: a latency SLO.** "Runs 70B on 4GB *at ≥N tok/s*" is either true or false — verifiable. "Runs 70B on 4GB" is aspirational until the latency context is added.
>
> For wiki readers evaluating AirLLM: **the claim is true, the implication is aspirational.** The library does exactly what it says on paper; the paper does not say what most readers assume it says. This is why the datasharepro.in review is valuable — it is the operational verifier for the structural claim.

### The Unmaintained-Library Risk

Last release: v2.11.0 on 2024-08-20 (Qwen2.5 support). That is ~20 months before today's date (2026-04-17). Implications:

- Llama 3.3, Llama 4, DeepSeek V3, Qwen 3, Mistral Large 3, and the 2025-2026 wave of models are not officially supported. Compatibility is a gamble — some work because the library is generic enough, some do not.
- No bug fixes for issues discovered in the last two years.
- The author (Gavin Li) has moved focus to Aiwrite Technology / content-creator tools per the repository README footer.

**The pragmatic read:** AirLLM is a *stable, understood mechanism* — the mechanism itself (layer streaming) is sound and will not bit-rot in the way that LLM frameworks often do. But if operator bets infrastructure on it, plan for the possibility of forking or rewriting the layer-streaming logic against newer model families. Alternative mechanisms with similar patterns: [accelerate](https://huggingface.co/docs/accelerate) with `device_map='auto'` + offloading, [llama.cpp](https://github.com/ggerganov/llama.cpp) with `-ngl N` (partial GPU offload), [DeepSpeed ZeRO-Inference](https://www.deepspeed.ai/tutorials/zero/). These are more actively maintained; the mechanism is the same.

### Hardware Shopping List the Operator May Want

Given the operator now has 19 GB VRAM and the question is whether to lean on NVMe, the relevant hardware reads:

| Component | Minimum for AirLLM | Recommended | Notes |
|-----------|---------------------|-------------|-------|
| NVMe SSD | Gen3 (3.5 GB/s) | Gen4 (7 GB/s) or Gen5 (13 GB/s) | Read bandwidth = per-token latency floor |
| NVMe free space | 50 GB | 250+ GB | Decomposed 70B ≈ 40 GB; 405B Q4 ≈ 230 GB; plus HF cache if not deleted |
| RAM | 16 GB | 32+ GB | Layer loading goes through system RAM; OS cache boosts repeat reads |
| GPU | 4 GB VRAM (Turing+) | 8-24 GB | More VRAM = fewer layer-swaps per token (multi-layer batching possible) |

The operator's 19 GB VRAM is comfortably above the AirLLM floor. The binding constraint becomes whichever is smaller: NVMe free space OR NVMe read bandwidth. A Gen5 NVMe with 500 GB free is the dream; a Gen4 with 250 GB free is more than enough for practical work.

## Key Pages

| Page | Role |
|------|------|
| [[model-local-ai\|Model — Local AI ($0 Target)]] | The routing model this extends with a new tier |
| [[src-qwopus-claude-opus-reasoning-distilled-qwen-27b\|Qwopus]] | Complementary strategy: distillation into smaller in-VRAM model |
| [[src-turboquant-122b-macbook\|TurboQuant]] | Parallel strategy on Apple Silicon unified memory |
| [[local-llm-quantization\|Local LLM Quantization]] | The quantization layer AirLLM's 4bit/8bit flags implement |
| [[local-model-vs-cloud-api-for-routine-operations\|Decision — Local Model vs Cloud API for Routine Operations]] | Routing decision framework that AirLLM adds a tier to |
| [[aicp\|AICP]] | The orchestrator that would integrate AirLLM as a batch-tier backend |
| [[declarations-are-aspirational-until-infrastructure-verifies-them\|Principle — Declarations Aspirational Until Verified]] | The principle AirLLM's marketing classically illustrates |
| [[structural-compliance-is-not-operational-compliance\|Structural Compliance Is Not Operational Compliance]] | The specific layer-instance — "runs" vs "runs at usable speed" |

## How This Connects — Navigate From Here

> [!abstract] From This Source → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **The routing model this extends** | [[model-local-ai\|Model — Local AI ($0 Target)]] |
> | **The complementary in-VRAM strategy** | [[src-qwopus-claude-opus-reasoning-distilled-qwen-27b\|Qwopus]] |
> | **The Apple Silicon parallel** | [[src-turboquant-122b-macbook\|TurboQuant]] |
> | **The principle this demonstrates** | [[declarations-are-aspirational-until-infrastructure-verifies-them\|Declarations Aspirational Until Verified]] |
> | **The orchestrator that would integrate it** | [[aicp\|AICP]] |

## Open Questions

> [!question] What is the measured latency on operator's specific hardware?
> The 5.7 s/tok figure assumes Gen4 NVMe at 7 GB/s. Operator's actual NVMe generation, free space, OS-cache behavior, and GPU transfer pipeline all shift the number. The honest answer needs a measurement — a 10-prompt benchmark run with a 70B Q4 model on the target hardware. Until measured, every routing-threshold choice is aspirational in the Principle-4 sense.

> [!question] Does AirLLM support the models in the current AICP inventory?
> Qwen3 (8B, 4B, 30B MoE, fast): likely YES (Qwen2.5 was the last officially added family; Qwen3 shares architecture). Gemma4 (E2B, E4B, 26B MoE): UNCLEAR — Gemma family not in the official compatibility list. This is a blocker for operator's current stack. A test-drive on one or two Qwen3 models is the cheapest way to answer.

> [!question] Is it worth a MacBook-side companion track?
> AirLLM-on-MacOS uses MLX with unified memory. If operator has access to Apple Silicon alongside the 19 GB VRAM WSL box, the two platforms may cover different parts of the routing space — larger models at lower latency on unified memory, medium models at higher throughput on dGPU.

## Relationships

- DERIVED FROM: [[src-qwopus-claude-opus-reasoning-distilled-qwen-27b|Synthesis — Qwopus — Claude Opus 4.6 Reasoning Distilled into Local Qwen 27B]]
- DERIVED FROM: [[src-turboquant-122b-macbook|Synthesis — TurboQuant 122B LLM on MacBook]]
- EXTENDED BY: [[src-gpt-oss-openai-open-weight-moe|Synthesis — gpt-oss]] (MoE-aware latency correction; invalidates batch-only framing for MoE models)
- FEEDS INTO: [[model-local-ai|Model — Local AI ($0 Target)]]
- FEEDS INTO: [[aicp|AICP]]
- RELATES TO: [[local-llm-quantization|Local LLM Quantization]]
- RELATES TO: [[local-model-vs-cloud-api-for-routine-operations|Decision — Local Model vs Cloud API for Routine Operations]]
- DEMONSTRATES: [[structural-compliance-is-not-operational-compliance|Structural Compliance Is Not Operational Compliance]]
- DEMONSTRATES: [[declarations-are-aspirational-until-infrastructure-verifies-them|Principle — Declarations Are Aspirational Until Infrastructure Verifies Them]]

## Backlinks

[[src-qwopus-claude-opus-reasoning-distilled-qwen-27b|Synthesis — Qwopus — Claude Opus 4.6 Reasoning Distilled into Local Qwen 27B]]
[[src-turboquant-122b-macbook|Synthesis — TurboQuant 122B LLM on MacBook]]
[[Synthesis — gpt-oss]]
[[model-local-ai|Model — Local AI ($0 Target)]]
[[aicp|AICP]]
[[local-llm-quantization|Local LLM Quantization]]
[[local-model-vs-cloud-api-for-routine-operations|Decision — Local Model vs Cloud API for Routine Operations]]
[[structural-compliance-is-not-operational-compliance|Structural Compliance Is Not Operational Compliance]]
[[declarations-are-aspirational-until-infrastructure-verifies-them|Principle — Declarations Are Aspirational Until Infrastructure Verifies Them]]
