---
title: "Synthesis — gpt-oss: OpenAI's Apache-2.0 Open-Weight MoE Models (20b + 120b)"
aliases:
  - "Synthesis — gpt-oss: OpenAI's Apache-2.0 Open-Weight MoE Models (20b + 120b)"
  - "Synthesis: gpt-oss"
  - "gpt-oss Source Synthesis"
type: source-synthesis
layer: 1
maturity: growing
domain: ai-models
status: synthesized
confidence: high
created: 2026-04-17
updated: 2026-04-17
sources:
  - id: src-gpt-oss-github
    type: repository
    url: https://github.com/openai/gpt-oss
    file: raw/articles/openaigpt-oss.md
    title: "openai/gpt-oss — GitHub Repository"
    ingested: 2026-04-17
  - id: src-gpt-oss-model-card
    type: paper
    url: https://arxiv.org/abs/2508.10925
    title: "gpt-oss-120b & gpt-oss-20b Model Card (OpenAI 2025)"
    ingested: 2026-04-17
tags: [gpt-oss, openai, open-weight, apache-2-0, moe, mxfp4, agentic, local-llm, harmony-format, reasoning, cost-optimization, aicp]
---

# Synthesis — gpt-oss: OpenAI's Apache-2.0 Open-Weight MoE Models (20b + 120b)

## Summary

In August 2025 OpenAI released **gpt-oss-20b** (21B total params, 3.6B active) and **gpt-oss-120b** (117B total params, 5.1B active) — their first open-weight reasoning models under a permissive Apache 2.0 license. Both use Mixture-of-Experts (MoE) architecture with native MXFP4 quantization, which is what makes gpt-oss-120b fit on a single 80GB GPU and gpt-oss-20b fit within 16GB of memory. Both support configurable reasoning effort (low / medium / high), full chain-of-thought visibility, native function calling, browser and Python code-execution tools, structured outputs, and parameter fine-tuning. Deployment stack is deliberately broad: Ollama, LM Studio, vLLM, transformers, llama.cpp, TensorRT-LLM, Metal for Apple Silicon, and day-0 cloud support (Groq, Cloudflare Workers AI, AWS, NVIDIA NIM). For the operator's 19 GB VRAM machine, **gpt-oss-20b is a direct in-VRAM Claude/OpenAI-API replacement candidate** — it fits, it does agent work, it exposes reasoning at adjustable depth, and it costs $0 beyond electricity. For larger workloads, **gpt-oss-120b's 5.1B active-per-token profile fundamentally changes the AirLLM disk-offload latency math** — streaming only the active experts, not the full 60GB MXFP4 weights, brings per-token latency from "batch-only" into "tool-augmented-agent-viable" territory. OpenAI joining the open-weight race is not a competitive curiosity; it is the point where the closed-vs-open gap narrows to *months* instead of *years*, and it forces the $0-target routing model to expand beyond "local for mechanical tasks only."

## Key Insights

> [!info] gpt-oss is OpenAI's declaration that open-weight has caught up
> The release date is August 2025. The architecture choices (MoE + MXFP4 + harmony format + full CoT access + agentic tool calling) mirror closed-frontier design decisions point-for-point. Apache 2.0 removes legal friction. This is not a "toy" or "research" release — it is a direct-deployment model with production tooling across NVIDIA, AMD, Groq, Cloudflare, AWS.

> [!tip] The MoE + MXFP4 combination is the cost-reduction engine
> A 117B model running on 80GB VRAM is only possible because (a) MXFP4 compresses linear MoE weights 4× relative to BF16, and (b) MoE routing keeps only 5.1B params active per token. Together: you pay total-parameter storage (NVMe) but per-token compute (VRAM + bandwidth). This is the structural insight that reshapes local-inference strategy for 2026.

- **gpt-oss-20b is the 19 GB VRAM sweet spot.** "Runs within 16GB of memory" per the README is a hard claim with MXFP4 on. On the operator's 19 GB VRAM machine, gpt-oss-20b fits natively with headroom for context (8K default, extendable). That means: full agentic tool calling (function calling, browser, Python exec, structured outputs), three reasoning effort tiers, CoT visibility, fine-tunability — all at $0 per token, latency bounded by compute (not disk, not network). This is the model the AICP routing tree was waiting for.

- **gpt-oss-120b changes what "too big for VRAM" means.** Total size in MXFP4 ≈ 60 GB. That does not fit in 19 GB VRAM as a dense load. But the model is MoE with 5.1B active parameters per token — so layer-offload engines that are MoE-aware only stream the SELECTED experts per token, not all weights. Effective per-token read ≈ 2.5-3 GB (active experts + shared layers). On Gen4 NVMe (7 GB/s), that is **~0.4 s/token = 2-3 tok/s**, which is *agent-viable* (tool-call latency is fine at a few seconds/step), not just batch-viable.

- **Configurable reasoning effort is the same mechanism as Opus 4.7 adaptive thinking.** Low/medium/high reasoning-effort dials at inference time. This turns a single deployed model into three tiers in the routing table — a gpt-oss-120b at `reasoning=low` is a different cost/latency point than `reasoning=high`. Combined with in-VRAM gpt-oss-20b, one local stack covers: fast deterministic → reasoning-light → reasoning-heavy without switching models.

- **Harmony response format is mandatory and load-bearing.** Both models REQUIRE the harmony format to function correctly. "If you use `model.generate` directly, you need to apply the harmony format manually." This is not optional formatting — it encodes conversation role separation, tool recipient routing, CoT separation, stop tokens. Integrations (Transformers chat template, vLLM offline, Ollama, LM Studio) handle this transparently; direct integrations do not. A custom AICP backend implementation must build harmony support or route through vLLM/Ollama.

- **Apache 2.0 means commercial deployment has zero legal friction.** No copyleft, no patent risk, no attribution burden beyond standard. For the ecosystem (Research Wiki second brain + OpenArms + OpenFleet + AICP + devops-control-plane), gpt-oss is deployable as a *product component*, not just a research tool. Distinguishes gpt-oss from Llama (community license restrictions) and from hermes/distilled models (derivative-license questions).

- **MXFP4 native quantization is the architecture, not a post-hoc compression.** Models were POST-TRAINED with MXFP4 on the MoE weights. This is different from Qwopus (LoRA on BF16 base) or AirLLM's compression flag (block-wise quantization at load time). Native MXFP4 means: no accuracy degradation from external quantization, no runtime decompression overhead, guaranteed compatibility with MXFP4-aware kernels (Triton, TensorRT-LLM, vLLM).

- **Deployment ecosystem is day-0 broad.** Launch-day support across Ollama (consumer hardware), LM Studio (desktop GUI), vLLM (production serving), transformers (Python), llama.cpp (portable), TensorRT-LLM (NVIDIA optimized), Metal (Apple Silicon), plus Groq / Cloudflare Workers AI / AWS Bedrock / NVIDIA NIM cloud hosting. This is closed-frontier-scale deployment breadth for an open-weight model, delivered on release day. Implies coordinated cross-vendor engagement before release — a different motion than previous open-weight releases.

- **Training transparency vs deployment transparency are different.** OpenAI released weights + inference code + model card (arXiv 2508.10925) but NOT training code, training data, or reinforcement-learning-from-feedback recipe. So: you can run, fine-tune, deploy, and commercialize; you cannot reproduce training or audit the data pipeline. This is the same trade-off Meta made with Llama — "open weights, closed training." For the wiki's principle-4 framing, the declaration "open-weight" is verified (weights are downloadable); the implicit claim "reproducible" is NOT — that remains aspirational without training code.

## Deep Analysis

### Architecture — MoE + MXFP4 + Harmony

> [!abstract] gpt-oss architecture at a glance
>
> | Dimension | gpt-oss-20b | gpt-oss-120b |
> |-----------|-------------|--------------|
> | Total params | 21 B | 117 B |
> | Active params/token | 3.6 B | 5.1 B |
> | Sparsity ratio | 17% | 4.4% |
> | Precision (MoE weights) | MXFP4 native | MXFP4 native |
> | Precision (other) | BF16 | BF16 |
> | Approx. MXFP4 total size | ~11 GB | ~60 GB |
> | Required VRAM/memory | 16 GB | 80 GB |
> | Context window (default chat CLI) | 8192 | 8192 |
> | License | Apache 2.0 | Apache 2.0 |
> | Release date | 2025-08 | 2025-08 |
> | Model card | arXiv 2508.10925 | arXiv 2508.10925 |

The **4.4% sparsity of the 120b** is the critical number. Of every forward pass through 117B weights, only ~5.1B participate in any given token. This is what distinguishes MoE inference from dense inference at the bandwidth layer, and it is what makes AirLLM-style disk-offload practical for gpt-oss-120b in a way it is not for dense 70B Llama.

### Reasoning Effort — Three Latency Tiers from One Model

`-r low` / `-r medium` / `-r high` on the chat CLI. This is the same structural idea as Claude Opus 4.7's adaptive thinking levels — internally, more reasoning = more CoT tokens consumed before the final answer. The implication for routing:

> [!info] Extended routing stack INCLUDING gpt-oss reasoning tiers
>
> | Tier | Model | Effort | Latency | Covers |
> |------|-------|--------|---------|--------|
> | local-fast | gpt-oss-20b | reasoning=low | 10-40 tok/s | Fast deterministic, tool-call dispatch |
> | local-reason | gpt-oss-20b | reasoning=high | 5-15 tok/s (more CoT) | Reasoning with reflection, short chains |
> | local-batch-reason | gpt-oss-120b via AirLLM | reasoning=medium | 2-3 tok/s | Agent loops, tool-augmented tasks, substantive analysis |
> | local-batch-deep | gpt-oss-120b via AirLLM | reasoning=high | 1-2 tok/s | Overnight synthesis, deep multi-step reasoning |
> | cloud-light | Opus 4.6 medium | seconds | Context-heavy, large-window tasks |
> | cloud-standard | Opus 4.7 high | seconds | Novel synthesis, high-stakes decisions |
> | cloud-heavy | Opus 4.7 xhigh | seconds | Architecture, security review, final judgment |

One deployed gpt-oss-20b + one NVMe-hosted gpt-oss-120b covers 4 of the 7 routing tiers. The wiki's prior local-only coverage was 1-2 tiers. This is a step-change in the $0-target trajectory.

### Agentic Capabilities — Parity Check with Closed Frontier

| Capability | Closed frontier (Opus 4.7 / GPT-5) | gpt-oss | Delta |
|-----------|------------------------------------|---------|-------|
| Function / tool calling | Yes | Yes (native, trained-in) | Match |
| Structured outputs | Yes | Yes (harmony format) | Match |
| Chain-of-thought | Hidden (4.7 adaptive) | EXPOSED (full CoT access) | gpt-oss wins on transparency |
| Web browsing | Yes (agent SDK) | Yes (reference browser tool) | Match |
| Python code execution | Yes (analysis tool) | Yes (reference python tool, Docker) | Match |
| Fine-tunability | Cloud-side only | Full (user-owned weights) | gpt-oss wins |
| Reasoning effort dial | 4.7: adaptive thinking | Explicit low/med/high | Match in mechanism |
| Commercial deployment | API only | Self-hosted + cloud | gpt-oss wins on sovereignty |

**The remaining closed-frontier advantage**: absolute benchmark leadership (MMLU, GPQA, coding evals), maximum context window (>200K), larger effective parameter budget for novel synthesis, less verbose CoT (efficient reasoning), access to proprietary training data. These gaps are real but **narrowed from years to months**.

### Answering "Is AirLLM Limited?" — The Corrected Framing

The prior AirLLM synthesis positioned disk-offload as a **batch-only tier** because the latency math assumed dense 70B models. That framing is accurate for dense models and WRONG for MoE. With gpt-oss-120b's 5.1B active params and MXFP4 weights:

> [!abstract] Corrected MoE-aware latency math (Gen4 NVMe 7 GB/s)
>
> | Model class | Strategy | Per-token read | Latency | Viable for |
> |-------------|----------|----------------|---------|------------|
> | Dense 70B Q4 (e.g. Llama 3 70B) | AirLLM layer streaming | ~40 GB | 5.7 s/tok | **Batch only** |
> | MoE 120B MXFP4 (gpt-oss-120b) | AirLLM MoE-aware streaming | ~2.5-3 GB (active experts) | 0.35-0.5 s/tok = 2-3 tok/s | **Agent-viable**, **tool-augmented interactive**, **not-great-for-chat** |
> | MoE 120B MXFP4 (gpt-oss-120b) | In-VRAM on 80 GB H100 | Full in VRAM | 30+ tok/s | Production interactive (cloud) |
> | Dense 20B (e.g. gpt-oss-20b MXFP4) | In-VRAM on 19 GB | Full in VRAM | 10-40 tok/s | **Local interactive + agents** |

**Correction**: AirLLM + MoE models is a new operating regime. AirLLM is NOT strictly batch-tier — it covers batch for dense, and agent-viable for MoE. The critical dependency is whether the layer-offload engine (AirLLM, accelerate, llama.cpp with `-ngl`) supports MoE-aware expert streaming. AirLLM has `AirLLMMixtral` (v2.7+, Dec 2023) — precedent for MoE support exists. Native gpt-oss support in AirLLM is not confirmed as of 2024-08 (last release); alternatives (vLLM, llama.cpp, transformers with `device_map='auto'` + offload) already support gpt-oss MoE.

**Practical recommendation**: Use **llama.cpp with partial GPU offload** (`-ngl N`) or **vLLM with offload** for gpt-oss-120b on 19 GB VRAM, not AirLLM specifically. The mechanism is the same (NVMe-backed disk-offload); the tooling is more current.

### Routing Architecture Implication for AICP

AICP's complexity scorer routes local/cloud based on task signals. With gpt-oss-20b + gpt-oss-120b-offload + cloud as three local/hybrid tiers above cloud-light, the routing table expands:

```
Request → Complexity Scorer
  ├── simple       → gpt-oss-20b reasoning=low         (in-VRAM, ~30 tok/s)
  ├── moderate     → gpt-oss-20b reasoning=high        (in-VRAM, ~10 tok/s)
  ├── substantive  → gpt-oss-120b MoE offload (llama.cpp / vLLM offload)
  │                                               (NVMe-backed, ~2-3 tok/s)
  ├── complex      → Opus 4.6 medium               (cloud, ~$)
  ├── novel        → Opus 4.7 high                 (cloud, $$)
  └── architectural → Opus 4.7 xhigh                (cloud, $$$)
```

**Before gpt-oss**: local tier capped at ~27B (Qwopus) for reasoning; everything above routed to cloud.
**With gpt-oss**: local tiers cover simple → substantive; only novel/architectural routes to cloud.
**Routing split shift**: estimated 40% local (pre-gpt-oss, Qwopus-only) → **70-80% local** (gpt-oss + AirLLM/llama.cpp offload). The AICP Stage 5 target ("80%+ Claude token reduction") is no longer hardware-blocked on 26B Gemma — it is *tool-integration-blocked* on deploying gpt-oss into the routing stack.

### Sovereign Deployment — Why Apache 2.0 Matters for the Ecosystem

The ecosystem (second brain + OpenArms + OpenFleet + AICP + devops-control-plane) is built on a teaching-system-for-adoption premise. Apache 2.0 means:

- **OpenFleet can ship gpt-oss-20b bundled with agent deployments** — no distribution license to worry about, no per-invocation fees, no external API dependency
- **AICP can include gpt-oss weights in its deployment artifacts** — no side-channel licensing
- **Research Wiki's $0-target claim becomes structurally verifiable** — not "$0 for routine tasks" but "$0 for everything the scorer routes below cloud-light"
- **Consumers adopting the wiki methodology can deploy gpt-oss alongside their CLAUDE.md / AGENTS.md** — the methodology gains a default-inference-backend answer

The license is load-bearing infrastructure for the ecosystem's sovereignty claims.

### The 2025-2026 Open-Weight Landscape Context

gpt-oss did not appear in isolation. The landscape it joins (as of April 2026):

| Model family | Release | Parameters | License | Competitive with |
|--------------|---------|-----------|---------|------------------|
| DeepSeek V3 / R1 | 2024-12 / 2025-01 | 671B MoE (37B active) | MIT / DeepSeek License | Claude 3.5 Sonnet, GPT-4o |
| Qwen 3 family | 2025 H1 | 30B MoE, 72B dense, etc. | Apache 2.0 | GPT-4 class on benchmarks |
| Llama 3.3 / 4 | 2024-12 / 2025 | 70B, 405B, 4x MoE | Meta community | GPT-4o class |
| Mistral Large 3 | 2025 H1 | ~120B MoE | Mistral Research / commercial | Claude 3.5 |
| **gpt-oss** | **2025-08** | **20B, 117B MoE** | **Apache 2.0** | **GPT-5 reasoning-light, Claude 4 tool-use** |
| Qwopus distilled | 2025 H2 | 27B distilled from Opus 4.6 | Apache 2.0 | Opus 4.6 on reasoning tasks |
| Hermes 4 | 2025 H2 | 70B fine-tuned | Llama derivative | Agentic tool use |

The pattern: **multiple credible open-weight reasoning models at every capability tier, released within ~12 months**. The question "can I do this locally at $0?" went from "maybe on batch" in 2024 to "yes at interactive latency on consumer hardware" in 2026. The Local AI model's 2026-04-14 section "Small Models Can Win" was a sign of this shift; gpt-oss is the shift becoming OpenAI-endorsed mainstream.

## Key Pages

| Page | Role |
|------|------|
| [[model-local-ai\|Model — Local AI ($0 Target)]] | The routing model gpt-oss extends with in-VRAM and offload tiers |
| [[src-airllm-layer-wise-inference-nvme-ssd-offload\|AirLLM synthesis]] | The offload mechanism; correction applied here for MoE |
| [[src-qwopus-claude-opus-reasoning-distilled-qwen-27b\|Qwopus]] | Prior local-reasoning candidate, now one of several tiers |
| [[src-turboquant-122b-macbook\|TurboQuant]] | Apple Silicon parallel approach |
| [[local-model-vs-cloud-api-for-routine-operations\|Decision — Local Model vs Cloud API]] | Routing framework gpt-oss re-tiers |
| [[aicp\|AICP]] | The orchestrator that must integrate gpt-oss into the router |
| [[declarations-are-aspirational-until-infrastructure-verifies-them\|Principle — Declarations Aspirational Until Verified]] | Applies to "open-weight" claim: weights yes, training no |

## How This Connects — Navigate From Here

> [!abstract] From This Source → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **The routing model this extends** | [[model-local-ai\|Model — Local AI ($0 Target)]] |
> | **The offload mechanism corrected for MoE** | [[src-airllm-layer-wise-inference-nvme-ssd-offload\|AirLLM synthesis]] |
> | **Complementary distilled-reasoning strategy** | [[src-qwopus-claude-opus-reasoning-distilled-qwen-27b\|Qwopus]] |
> | **The orchestrator that must integrate** | [[aicp\|AICP]] |
> | **Principle applicable to "open-weight" claim** | [[declarations-are-aspirational-until-infrastructure-verifies-them\|Declarations Aspirational]] |

## Open Questions

> [!question] Does AirLLM natively support gpt-oss MoE-aware expert streaming?
> AirLLM's last release (2024-08 v2.11.0) supports AirLLMMixtral for MoE. gpt-oss-specific support is not confirmed. For near-term deployment, **llama.cpp with `-ngl N`** and **vLLM with offload** are more current targets. Test needed to validate AirLLM + gpt-oss-120b path.

> [!question] What is the measured per-token latency for gpt-oss-20b on 19 GB VRAM?
> MXFP4 native, 16 GB memory claim, 8K context default. On the operator's hardware: a 10-prompt benchmark (matched prompt complexity, various reasoning efforts) will give real numbers. The projected 10-40 tok/s range is an estimate; ground truth is measurement.

> [!question] How does gpt-oss-20b compare to Qwopus 27B on reasoning tasks?
> Both targeted at the ~20-30B in-VRAM reasoning tier. gpt-oss-20b has native tool-calling training + harmony format + MXFP4. Qwopus has Opus-distilled CoT + LoRA + GGUF. Head-to-head evaluation on AICP's task classes would determine whether they complement or which dominates.

> [!question] Is gpt-oss-120b MXFP4 offload worth the complexity vs just running gpt-oss-20b reasoning=high?
> For ~same latency (2-3 tok/s offload vs 5-15 tok/s reasoning-high), gpt-oss-120b probably produces higher-quality output. But 20b-reasoning=high is simpler to deploy (no offload engine), stays in VRAM, and fine-tunes more easily. The question is task-specific; needs measurement.

> [!question] Can gpt-oss-20b replace Claude for routine AICP routing decisions?
> The structural match is close (tool calling, reasoning effort, CoT). The gap is likely on novel cross-domain synthesis and nuanced judgment. Empirical test: run the same wiki-evolution tasks on gpt-oss-20b and Claude; compare quality. If parity is within 10-15%, routing split moves aggressively to local.

## Relationships

- BUILDS ON: [[src-airllm-layer-wise-inference-nvme-ssd-offload|Synthesis — AirLLM]]
- FEEDS INTO: [[model-local-ai|Model — Local AI ($0 Target)]]
- FEEDS INTO: [[aicp|AICP]]
- RELATES TO: [[src-qwopus-claude-opus-reasoning-distilled-qwen-27b|Synthesis — Qwopus]]
- RELATES TO: [[src-turboquant-122b-macbook|Synthesis — TurboQuant]]
- RELATES TO: [[local-llm-quantization|Local LLM Quantization]]
- RELATES TO: [[local-model-vs-cloud-api-for-routine-operations|Decision — Local Model vs Cloud API for Routine Operations]]
- DEMONSTRATES: [[declarations-are-aspirational-until-infrastructure-verifies-them|Principle — Declarations Aspirational Until Verified]]

## Backlinks

[[Synthesis — AirLLM]]
[[model-local-ai|Model — Local AI ($0 Target)]]
[[aicp|AICP]]
[[Synthesis — Qwopus]]
[[Synthesis — TurboQuant]]
[[local-llm-quantization|Local LLM Quantization]]
[[local-model-vs-cloud-api-for-routine-operations|Decision — Local Model vs Cloud API for Routine Operations]]
[[Principle — Declarations Aspirational Until Verified]]
