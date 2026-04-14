---
title: "Synthesis — LLM Architecture Gallery (Raschka)"
type: source-synthesis
domain: ai-models
status: synthesized
confidence: high
maturity: seed
created: 2026-04-14
updated: 2026-04-14
sources:
  - id: raschka-llm-gallery
    type: article
    url: "https://sebastianraschka.com/llm-architecture-gallery/"
tags:
  - ai-models
  - llm-architecture
  - mixture-of-experts
  - attention-mechanisms
  - kv-cache
  - context-window
  - moe
  - mla
  - linear-attention
  - architecture-trends
  - model-selection
  - raschka
  - dense-transformer
  - hybrid-models
---

# Synthesis — LLM Architecture Gallery (Raschka)

## Summary

Sebastian Raschka's LLM Architecture Gallery is a curated, continuously updated catalog of 60+ large language model architectures released between 2019–2026, featuring structured fact sheets, visual diagrams, and side-by-side comparison tooling. The gallery documents the clear architectural evolution from GPT-2's simple dense multi-head attention (MHA) baseline through grouped-query attention (GQA), mixture-of-experts (MoE), multi-head latent attention (MLA), and hybrid linear/recurrent attention designs. Key dimensions tracked — KV cache cost per token, active parameter fraction, context window length, attention mechanism type — provide the quantitative grounding for model selection decisions. The gallery shows that by 2025–2026, architecture has converged around MLA+MoE templates, with the primary differentiation shifting to active parameter efficiency and KV cache minimization for edge/local deployment.

> [!info] Source Reference
> | Attribute | Value |
> |-----------|-------|
> | Source    | Sebastian Raschka — LLM Architecture Gallery (`https://sebastianraschka.com/llm-architecture-gallery/`) |
> | Type      | Curated reference gallery with 60+ architecture fact sheets and diff tooling |
> | Author    | Sebastian Raschka — ML researcher, author of "Build a Large Language Model (From Scratch)" |
> | Last Updated | April 10, 2026 |
> | Date Ingested | 2026-04-14 |
> | Key claim | Architecture has largely converged; the decision axis has shifted from "which paradigm" to "how few parameters need to be active per token" |

## Key Insights

**1. Architecture convergence: independent teams reached the same MLA+MoE blueprint.**

Mistral Large 3 (673B) and DeepSeek V3 (671B) share nearly identical architectural blueprints despite independent development on separate continents. Both use Multi-head Latent Attention (MLA) combined with sparse Mixture-of-Experts (MoE), dense prefix layers, and shared expert mechanisms. This is not imitation — it is convergence evidence. When two teams optimizing for the same objective (maximum quality at minimum active compute) independently arrive at the same solution, that solution is likely near-optimal for the current state of hardware and training dynamics. The architectural design space has narrowed to a small cluster around MLA+MoE.

**2. Active parameter fraction — the key efficiency metric for 2025–2026.**

The gallery reveals a consistent trend: top-tier models activate an ever-shrinking fraction of their total parameters per token:

| Model | Total Params | Active Params | Active % |
|-------|-------------|---------------|----------|
| DeepSeek V3 | 671B | 37B | 5.5% |
| Qwen3 (235B-A22B) | 235B | 22B | 9.4% |
| Mistral Large 3 | 673B | 41B | 6.1% |
| GLM-5 | 744B | 40B | 5.4% |
| Qwen3 Next | 80B | 3B | 3.8% |
| Kimi Linear | 48B | 3B | 6.3% |

The pattern: 500B+ parameter models operate at 5-10% activation density. A 671B model that activates only 37B parameters per forward pass has the inference cost profile of a 37B model while maintaining the knowledge capacity of a 671B model. This is the primary mechanism behind the cost reduction that makes frontier-class models increasingly deployable.

**3. KV cache cost per token — the practical deployment bottleneck.**

KV cache size per token (in bf16) determines how many tokens of context a model can maintain in GPU VRAM simultaneously. The gallery reveals a 100x spread across architectures:

| Tier | Range | Examples |
|------|-------|---------|
| Very low | 7.9–24 KiB | Kimi Linear (7.9 KiB), Qwen3 Next (24 KiB) |
| Low | 32–68.6 KiB | MLA-based MoE, efficient architectures |
| Moderate | 128–192 KiB | Standard GQA/MoE |
| High | 248–368 KiB | Full attention models |
| Very high | 496–840 KiB | Wide MHA with many KV heads |

For local deployment (our $0 target), KV cache cost is the binding constraint. A model with 7.9 KiB/token KV cache can serve 128K context on the same VRAM that a 248 KiB/token model can only serve 4K context. The architectural choice of attention mechanism — and specifically whether MLA or linear attention is used — has a direct, measurable impact on what's deployable on consumer hardware.

**4. MLA (Multi-head Latent Attention) — the KV compression breakthrough.**

Multi-head Latent Attention compresses the KV cache by projecting keys and values into a low-dimensional latent space before caching, then expanding back for attention computation. The result is dramatically smaller KV cache at marginal quality cost. MLA is now used by DeepSeek V3, Mistral Large 3, GLM-5, Mistral Small 4, Kimi K2.5, and Sarvam — the most capable models in the gallery. For local AI deployment, MLA-based models should be the default architecture preference because they make long-context operation feasible on constrained hardware.

**5. Context window explosion: 1K → 1M+ tokens in seven years.**

GPT-2 (2019): 1,024 tokens. Llama 3.2 1B (2024): 128,000 tokens. Nemotron 3 Super: 1,000,000+ tokens. The context window has grown by 1,000x in 7 years. This is not a smooth linear progression — it reflects architectural innovations (RoPE position embeddings with extended scaling, sliding-window + global attention, linear attention), hardware improvements (larger VRAM), and optimized KV cache strategies (MLA, sparse attention). For our wiki's use of long-context models, the practical implication is that 256K–1M context windows are now mainstream in top-tier models, enabling whole-codebase and whole-document reasoning without chunking.

**6. Hybrid linear/attention models — transformer alternatives reaching production.**

Several 2025–2026 models replace full attention in most layers with linear attention or state-space mechanisms:

- **Qwen3 Next** (80B-A3B): 3:1 Gated DeltaNet / Gated Attention hybrid — only 24 KiB KV cache per token
- **Kimi Linear** (48B-A3B): Linear attention in most layers — only 7.9 KiB KV cache per token
- **Ling 2.5** (1T): Lightning Attention + MLA at 7:1 linear/MLA ratio
- **Nemotron 3 Nano**: Mamba-2 / GQA / MoE hybrid — most extreme transformer/state-space hybrid

These models maintain competitive quality benchmarks while achieving KV cache costs 10–30x lower than full-attention equivalents. For local AI deployment, hybrid/linear architectures represent the frontier of what's feasible on consumer hardware.

**7. Normalization evolution — QK-Norm and post-norm for training stability.**

The gallery documents a clear normalization trend: moving from pre-norm LayerNorm (GPT-2 era) toward QK-Norm (per-head normalization of queries and keys before attention) and post-norm with inside-residual designs. QK-Norm stabilizes attention scores and prevents attention entropy collapse in deep models. OLMo 2 uses inside-residual post-norm specifically for transparency and reproducibility. Gemma 4 uses post-norm on global attention layers. This trend reflects accumulated training-time insights: models that were previously unstable to train now converge reliably with these normalization innovations.

**8. Edge models — frontier capabilities compressed to 2–5B effective compute.**

Gemma 4 E2B (2.3B effective compute) and E4B (4.5B effective compute) pack per-layer embeddings and multimodal audio support into a footprint that runs on mobile hardware. Qwen3 Next and Kimi Linear achieve 3B active parameters from 48–80B total parameter models via MoE sparsity. This compression to small effective compute enables deployment scenarios that were impossible in 2023: local inference on laptops, embedded inference on IoT devices, and air-gapped deployments with no cloud dependency.

## Deep Analysis

### The Architecture Decision Tree for Model Selection

The gallery enables a systematic decision framework for model selection in our ecosystem:

**Step 1: Determine deployment target**
- Cloud inference → any model, optimize for quality per dollar
- Local deployment → filter by KV cache per token and active parameters

**Step 2: Apply KV cache filter for local deployment**
- 8GB VRAM: need < 32 KiB/token for 256K context
- 16GB VRAM: < 64 KiB/token for 256K context
- 24GB VRAM: < 96 KiB/token for 256K context
- Target models: Qwen3 Next (24 KiB), Kimi Linear (7.9 KiB), MLA-based MoE (32–68 KiB)

**Step 3: Verify attention mechanism**
- Full attention (MHA/GQA): high quality, high KV cost, best for accuracy-critical tasks
- MLA: best quality/KV ratio, now the frontier standard
- Linear/hybrid: lowest KV cost, competitive quality, best for local long-context tasks

**Step 4: Validate against benchmark tier**
- AA Intelligence Index provides four-category scores: General, Scientific, Coding, Agents
- GLM-5.1 (744B total, 40B active): 51.4 total — frontier tier
- Target for local AI with reasonable hardware: models scoring 35–45 total with <3B active params

### Architectural Evolution Timeline

The gallery documents a clean progression from 2019 to 2026:

**2019–2021: Dense MHA era**
- GPT-2: Simple dense MHA, 1K context
- Models defined by parameter count (bigger = better)
- No KV cache optimization

**2022–2023: GQA + RoPE transition**
- Grouped Query Attention reduces KV heads (3-8x KV cache reduction vs MHA)
- Rotary Position Embeddings (RoPE) enable context extension
- Llama family established GQA as the standard for open models

**2024: MoE + long context scaling**
- Sparse MoE achieves frontier quality with dramatically fewer active params
- Context windows extend to 128K–256K
- Models begin targeting edge deployment

**2025–2026: MLA + hybrid convergence**
- MLA becomes standard in top-tier models (DeepSeek, Mistral, Kimi)
- Linear attention models hit production quality (Kimi Linear, Qwen3 Next)
- Active parameter fraction drops to 3–10% for top models
- KV cache per token minimized as first-class design constraint
- Edge models with multimodal capability emerge (Gemma 4 E2B/E4B)

### The Convergence Finding — Architecture as Commodity

The near-identical blueprints of Mistral Large 3 and DeepSeek V3 have a strategic implication for model selection: if independent optimization leads to convergence, then architectural differentiation is shrinking as a competitive moat. What differentiates models in 2026 is increasingly:

1. **Training data quality and composition** (not visible in architecture diagrams)
2. **RLHF / instruction tuning quality** (determines usable task performance)
3. **KV cache efficiency** (determines what's deployable locally)
4. **Active parameter fraction** (determines inference cost at scale)
5. **Context window** (determines task scope)

For our ecosystem's model selection decisions, this means: stop selecting models primarily on architecture and start selecting on KV cache profile, active parameter fraction, and task-specific benchmark scores. The architecture is converging to a template; the differentiation lies elsewhere.

### Implications for Local AI Model Architecture

The gallery provides the architectural grounding for the Local AI model's hardware target. With the documented 8GB → 19GB VRAM upgrade (from hardware upgrade notes), the feasibility analysis changes substantially:

**Pre-upgrade (8GB VRAM):**
- KV cache budget: ~8GB total minus model weights
- Practical constraint: small models (7B–13B) with short context
- Architecture preference: quantized GQA models

**Post-upgrade (19GB VRAM):**
- Can load models up to ~12B parameters in fp16, or ~24B in 4-bit quantization
- With MLA-based architecture (32–68 KiB/token): 128K–256K context becomes feasible
- With Qwen3 Next / Kimi Linear (7.9–24 KiB/token): 500K+ context on 19GB becomes feasible
- Architecture preference: MLA or linear attention models in 4-bit quantization

The gallery's KV cache figures are in bf16 (full precision). At 4-bit quantization, KV cache scales approximately 4x in the number of tokens that fit in the same VRAM. This means the Qwen3 Next at 24 KiB/token bf16 becomes effectively 6 KiB/token at 4-bit, enabling over 2 million tokens of context on 19GB VRAM — far beyond any practical need.

### Architecture Diff Tool — Operational Value

The gallery's architecture diff tool enables rapid side-by-side comparison across any two models in the catalog. For model selection decisions in our ecosystem, the workflow becomes:

1. Identify candidate models matching deployment constraints
2. Use diff tool to compare: KV cache/token, active params, context window, attention type
3. Check AA Intelligence Index scores for target task categories (General/Coding for most tasks)
4. Select the candidate with best quality-per-KV-cache-cost ratio

This operational workflow transforms model selection from qualitative reasoning into a data-driven comparison against quantified architectural constraints.

### Multimodal and Specialized Architecture Trends

The gallery documents emerging specialized architecture variants not present in 2022–2023 reviews:

- **Audio support**: Gemma 4 E2B/E4B include audio tokens as a native input type alongside text and images
- **Multilingual optimization**: Gemma 3 uses a 262K multilingual vocabulary (3x larger than typical); Sarvam models target Indian languages specifically
- **Reasoning-orientation**: Sarvam and Qwen3 include reasoning-oriented variants with extended chain-of-thought training
- **Per-layer embeddings**: Gemma 4 edge variants use per-layer embeddings to compress vocabulary lookup cost

These specializations signal that the 2026 frontier is not a single model type but an ecosystem of specialized architectures, each optimized for specific deployment scenarios. For our model selection framework: don't assume the same model serves all task types — consider whether task-specific specialization (coding, reasoning, multilingual) warrants a different model choice.

## Open Questions

- What is the quality cost of linear attention vs full attention on long-context reasoning tasks? The KV cache savings are documented; the quality degradation at 256K+ context needs empirical quantification.
- Does the MLA+MoE convergence mean that post-2026 models will primarily differentiate on training data rather than architecture? Is architectural innovation slowing?
- For the Qwen3-35B-A3B model (3B active parameters, approaching 100% AutoBE compilation rates) — what is the KV cache cost per token? This would determine whether it's viable for local deployment on 19GB VRAM.
- How do hybrid linear/attention models (Qwen3 Next, Kimi Linear) perform on tasks requiring long-range dependency tracking compared to full attention? Is the quality trade-off acceptable for code generation?
- The gallery tracks AA Intelligence Index scores but these are aggregate. What are the per-domain scores (especially Coding and Agents) for the most promising local deployment candidates?
- As active parameter fractions drop to 3–6%, what is the effect on in-context learning capability? Does MoE sparsity hurt few-shot performance relative to an equally compute-dense model?

## Relationships

- FEEDS INTO: [[model-local-ai|Model — Local AI ($0 Target)]] (KV cache per token figures + active parameter fractions determine what's deployable on local hardware; MLA and linear attention models are the primary candidates)
- RELATES TO: [[model-ecosystem|Model — Ecosystem Architecture]] (architecture convergence affects multi-model routing strategy; model selection framework grounded in gallery data)
- COMPARES TO: [[src-autobe-compiler-verified-backend-generation|Synthesis — AutoBE: Compiler-Verified Backend Generation]] (gallery documents Qwen3-35B-A3B as the 77x cost reduction candidate; Raschka's MoE data explains why 3B active params with 35B total is viable)
- RELATES TO: [[local-llm-quantization|Local LLM Quantization]] (gallery's bf16 KV cache figures scale predictably with quantization; architecture choice determines quantization ceiling)
- RELATES TO: [[model-quality-failure-prevention|Model — Quality and Failure Prevention]] (active parameter fraction + retry convergence: gallery data shows small active-param models are capable enough for verified tasks)
- BUILDS ON: [[model-claude-code|Model — Claude Code]] (architecture context for understanding why frontier model selection matters for agent reasoning tasks vs. structured generation tasks)

## Backlinks

[[model-local-ai|Model — Local AI ($0 Target)]]
[[model-ecosystem|Model — Ecosystem Architecture]]
[[src-autobe-compiler-verified-backend-generation|Synthesis — AutoBE: Compiler-Verified Backend Generation]]
[[local-llm-quantization|Local LLM Quantization]]
[[model-quality-failure-prevention|Model — Quality and Failure Prevention]]
[[model-claude-code|Model — Claude Code]]
