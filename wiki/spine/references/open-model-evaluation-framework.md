---
title: "Open-Model Evaluation Framework — How to Look at a New Model Announcement"
aliases:
  - "Open-Model Evaluation Framework"
  - "How to Evaluate a New Open-Weight Model"
  - "Open-Model Evaluation Framework — How to Look at a New Model Announcement"
type: reference
domain: cross-domain
layer: spine
status: synthesized
confidence: high
maturity: growing
created: 2026-04-17
updated: 2026-04-17
sources:
  - id: src-gpt-oss-openai-open-weight-moe
    type: wiki
    file: wiki/sources/tools-integration/src-gpt-oss-openai-open-weight-moe.md
    title: "Synthesis — gpt-oss"
  - id: src-airllm-layer-wise-inference-nvme-ssd-offload
    type: wiki
    file: wiki/sources/tools-integration/src-airllm-layer-wise-inference-nvme-ssd-offload.md
    title: "Synthesis — AirLLM"
  - id: src-qwopus-claude-opus-reasoning-distilled-qwen-27b
    type: wiki
    file: wiki/sources/src-qwopus-claude-opus-reasoning-distilled-qwen-27b.md
    title: "Synthesis — Qwopus"
tags: [reference, evaluation, local-llm, open-weight, framework, checklist, routing, cost-optimization]
---

# Open-Model Evaluation Framework — How to Look at a New Model Announcement

## Summary

Between late 2024 and early 2026, the open-weight reasoning-model landscape went from "years behind closed frontier" to "months behind, at interactive latency on consumer hardware." Announcements arrive weekly — DeepSeek, Qwen, Llama, Mistral, gpt-oss, Qwopus variants, Hermes, Gemma, distilled/merged/quantized spins on every base. It is easy to feel lost. This page is the stable framework for processing a new model announcement: **where to look**, **what to extract in what order**, **how to decide if it matters for you**, and **when to ignore versus integrate**. It is designed so a single pass takes ~20 minutes and produces a defensible decision, not a rabbit hole. The 2026 AirLLM / gpt-oss / Qwopus v3 ingestions are worked examples inline.

## The Evaluation Flow (5 Stages)

> [!info] Each stage either keeps or drops the candidate. Move to the next stage only if the current one keeps the model in scope.
>
> | Stage | Question | Time | Source |
> |-------|----------|------|--------|
> | **1. Identify** | Who made this, when, under what license? | 5 min | Repo README + HF model card |
> | **2. Size & fit** | Does it physically run on my hardware? | 5 min | Quantization table + VRAM math |
> | **3. Capability** | Can it do what I need (reasoning, tools, context)? | 5 min | Architecture + benchmark claims |
> | **4. Deployment** | What runtime do I use to actually deploy it? | 3 min | Ollama / LM Studio / vLLM / llama.cpp support |
> | **5. Slot** | Where does it fit in the routing table? | 2 min | Model — Local AI tiers |

## Stage 1 — Identify: Who, When, License

> [!abstract] Minimum facts to extract BEFORE reading further
>
> | Field | Where to look | Red flag |
> |-------|---------------|----------|
> | Creator / org | Repo README, HF user, model card | Anonymous-only user with no prior models |
> | Release date | Model card, GitHub commit history | >12 months stale (library may be unmaintained) |
> | License | LICENSE file, model card header | Custom "community" license (Llama-style), "research use only" |
> | Base model (if derivative) | Model card "base_model" field, README | Undisclosed base — raises attribution / training questions |
> | Training source | Model card description | No source disclosed or conflicting claims |

**Authoritative order** (descending trust):
1. **arXiv paper / model card PDF** — most formal, highest vetting
2. **GitHub repository README** — maintained by creators
3. **HuggingFace model card** — often same content as README, sometimes more
4. **Official announcement blog** (OpenAI, Meta, Mistral, Anthropic)
5. **Tech journalism** (decrypt.co, Ars Technica, The Register) — useful for narrative context, always verify numbers against primary source
6. **Twitter / Reddit / Discord** — lead indicator of release; do NOT trust specific numbers from these

**License classes that matter for the ecosystem:**
- **Apache 2.0 / MIT** — fully deployable commercially, no copyleft, no patent risk. gpt-oss, Qwen 3, Qwopus, Mistral-research-derivatives-that-allow-commercial.
- **Meta community license** (Llama) — commercial OK below 700M MAU, attribution required, some restricted uses.
- **Proprietary "source-available" / research-only** — NOT deployable in sister projects or customer-facing ecosystems. Treat as research-only.
- **Derivative uncertainty** — a LoRA on a base with different license (e.g., Qwopus = Apache on Qwen Apache, so OK; but a LoRA on Llama is Llama-derivative).

## Stage 2 — Size & Fit: Can I Run This HERE?

> [!tip] Start from hardware facts, not model claims
> "Runs on a potato PC" / "70B on 4GB VRAM" / "fits in 16GB memory" are all **aspirational declarations until you verify them with the quantization table and your hardware**. See [[declarations-are-aspirational-until-infrastructure-verifies-them|Principle — Declarations Aspirational Until Verified]].

### The VRAM/RAM math

For a quantized model, **memory footprint ≈ file size on disk + context overhead**. The file size is the load-bearing number and is usually stated clearly per quantization variant in the model card GGUF table. Typical overhead: **+1-3 GB for context** (8K-32K), more for longer contexts.

> [!abstract] Worked example — Qwopus3.5-27B-v3-GGUF (from the model card)
>
> | Quantization | File size | Effective VRAM need | Fits 8 GB? | Fits 19 GB? | Fits 24 GB? |
> |--------------|-----------|---------------------|------------|-------------|-------------|
> | Q2_K | 10.7 GB | ~11 GB | No | Yes (headroom) | Yes |
> | Q3_K_M | 13.3 GB | ~14 GB | No | Yes | Yes |
> | Q4_K_M | 16.5 GB | ~17-18 GB | No | Yes (tight) | Yes |
> | Q5_K_M | 19.2 GB | ~20-21 GB | No | **No** (exceeds) | Yes |
> | Q6_K | 22.1 GB | ~23-24 GB | No | No | Yes (tight) |
> | Q8_0 | 28.6 GB | ~29-30 GB | No | No | No (needs CPU offload) |
> | BF16 (full) | 53.8 GB | ~54-55 GB | No | No | No |
>
> **For a 19 GB VRAM machine**: Q4_K_M is the sweet spot. Q3_K_M is the safe default. Q5_K_M is OUT despite being only 19.2 GB — because context overhead pushes it over 19 GB VRAM.

### The "does it actually fit" checklist

1. **File size for chosen quantization** — look at the GGUF file listing or the quantization table.
2. **Context overhead** — add 1-3 GB for typical agent contexts.
3. **Competing processes** — Obsidian, browsers, system memory also claim VRAM on unified-memory systems (Apple Silicon).
4. **Disk offload possible?** — If VRAM too small, can the runtime offload some layers to CPU/NVMe? (llama.cpp `-ngl N`, vLLM offload, AirLLM layer streaming.) Latency cost comes with this.
5. **Validation target** — actually download and try the smallest quantization first; measure tokens/second with your prompt; scale up from there.

### For MoE models — the math is different

For Mixture-of-Experts (MoE) models, the **in-VRAM footprint is still the full model size** — weights must be loaded to VRAM to run. What MoE changes is **per-token compute and disk-offload bandwidth**:
- In-VRAM MoE inference speed depends on ACTIVE params, not total params
- Disk-offload MoE inference (AirLLM-style) streams only ACTIVE experts per token, not all weights

Example: gpt-oss-120b at MXFP4 ≈ 60 GB total. Does NOT fit in 24 GB VRAM in-memory, but can be offloaded with ~2.5-3 GB/token streaming (5.1B active params) → ~2-3 tok/s on Gen4 NVMe. See [[src-airllm-layer-wise-inference-nvme-ssd-offload|AirLLM synthesis]] and [[src-gpt-oss-openai-open-weight-moe|gpt-oss synthesis]] for full derivation.

## Stage 3 — Capability: Can It Do What I Need?

> [!abstract] Architecture / capability matrix to extract
>
> | Dimension | What to look for | Why it matters for routing |
> |-----------|------------------|----------------------------|
> | Dense vs MoE | Architecture type | MoE: lower per-token compute, disk-offload-friendly |
> | Total / active params | Headline figures | Both matter; active is per-token, total is storage |
> | Precision / quantization | Native MXFP4? BF16? Q4? | Native quantization = no accuracy loss; post-hoc may degrade |
> | Context window | In tokens, from base model | Long context = suits synthesis; short = suits tool calls |
> | Reasoning mode | Single / adaptive / effort dial | Adaptive = better routing granularity |
> | Chain-of-thought | Hidden / exposed / optional | Exposed = transparent debugging; hidden = cleaner output |
> | Tool calling | Native trained / post-hoc / none | Native = reliable for agents; post-hoc = fragile |
> | Structured outputs | Schema-constrained support | Required for any agent pipeline producing JSON / YAML |
> | Fine-tunable | Full / LoRA-only / none | Full ownership = you can evolve it |
> | Multimodal | Vision / audio / text-only | For most wiki-and-agent work, text-only is fine |

### Benchmark literacy — what to believe and what to probe

**Useful benchmarks for routing decisions:**
- **HumanEval** (code) — strict benchmark; report BOTH base-pass and plus-pass; e.g. Qwopus v3 = 97.56% base / 95.73% plus
- **MMLU / MMLU-Pro** (general knowledge + reasoning) — saturated at the top; differences <3 points are noise
- **ARC-AGI** (reasoning) — harder, less gamed; 7-27M models beat GPT-5 here per [[src-hrm-trm-tiny-recursion-models|HRM/TRM]]
- **BFCL / ToolBench** (tool calling) — emerging agentic benchmarks

**Red flags in benchmark claims:**
- Single benchmark reported — cherry-picking
- Pass@10 or Pass@N reported as headline with small N — inflates numbers
- "Beats GPT-X" without disclosing which specific eval
- No methodology disclosed (temperature, sampling, eval harness)
- Claims of parity with Opus / GPT-5 without specific task classes

**Safe interpretation**: treat a single benchmark number as a +/- 3-5 point range of actual capability on your real tasks. Treat multi-benchmark reports as more trustworthy. **The only definitive benchmark is your workload**; use public benchmarks to decide whether a model is worth testing.

## Stage 4 — Deployment: What Runtime?

> [!info] Runtime maturity matters more than library fanciness
> A month-old tool with vLLM + llama.cpp + Ollama day-0 support is more integration-ready than a polished 2024 library that has not been updated for the current model family. See [[src-airllm-layer-wise-inference-nvme-ssd-offload|AirLLM]] for the negative case.

### Runtime tier preferences (for this ecosystem)

| Runtime | Strengths | When to choose |
|---------|-----------|----------------|
| **Ollama** | Simplest setup, single-command install, broad model support | First deployment, testing, consumer hardware |
| **LM Studio** | GUI, quantization variants visible, tight HF integration | Manual evaluation, benchmark measurement |
| **llama.cpp** | Maximum quantization support, partial GPU offload (`-ngl`), CPU fallback, most current | Production local deployment, MoE + offload, low-VRAM |
| **vLLM** | Production serving, batching, best throughput, MoE-aware, day-0 for major releases | Multi-user, high-throughput, fleet deployment |
| **Transformers** | Pythonic, standard API, `device_map='auto'` + offload_folder | Research, custom integrations, fine-tuning |
| **TensorRT-LLM / Triton** | NVIDIA-optimized | H100-class hardware, last-mile latency optimization |
| **MLX** | Apple Silicon unified memory | MacOS exclusive, competitive with dGPU stacks |

**Rule**: if the model has day-0 Ollama + llama.cpp + vLLM support, deployment is 1-hour effort. If only custom-library support exists, plan 1-2 days of integration work AND evaluate whether an alternative runtime with the same model will emerge quickly.

### GGUF / MLX / MXFP4 — quantization format literacy

- **GGUF** — the dominant consumer format (llama.cpp, Ollama, LM Studio). Every mainstream model has a GGUF release within days of launch (community ports if not official).
- **MLX** — Apple Silicon native format; unified memory performance.
- **MXFP4 / FP8** — emerging precision formats for H100+ class hardware with native kernel support. gpt-oss is MXFP4-native.
- **AWQ / GPTQ** — older quantization formats; still useful but less common than GGUF for new releases.

## Stage 5 — Slot: Where Does It Fit in the Routing Table?

> [!abstract] Current routing tiers (see [[model-local-ai|Model — Local AI]] for the canonical list)
>
> | Tier | Latency | Capability | Example models |
> |------|---------|-----------|----------------|
> | local-fast | 10-40 tok/s | Deterministic, short context | Qwen3-8B, Gemma4-E4B, gpt-oss-20b reasoning=low |
> | local-reasoning | 5-30 tok/s | Multi-step reasoning + tools | Qwopus v3 Q4_K_M, gpt-oss-20b reasoning=high |
> | local-batch (MoE offload) | 0.5-3 tok/s | Substantive reasoning overnight or in agents | gpt-oss-120b via llama.cpp `-ngl`, Mixtral offload |
> | local-batch (dense offload) | 0.1-0.5 tok/s | Capability validation, overnight only | Llama 3 70B via AirLLM / layer-offload |
> | cloud-light | seconds | Context-heavy, inference-reliant | Opus 4.6 medium |
> | cloud-standard | seconds | Novel synthesis, implementation work | Opus 4.7 high |
> | cloud-heavy | seconds | Architecture, security, final judgment | Opus 4.7 xhigh |

### Decision tree for any new candidate

```
Does the new model fit in my VRAM at a reasonable quantization?
├── YES → which tier does its capability profile match?
│   ├── Better than current occupant of that tier?
│   │   └── YES → schedule migration (test against real workload)
│   │   └── NO → ignore OR keep as backup
│   └── Fills a GAP in the current routing table?
│       └── YES → integrate soon
│       └── NO → watch for v-next
└── NO → can it be offloaded (MoE-aware runtime)?
    ├── YES → is the new-tier latency acceptable for any workload I have?
    │   └── YES → test on real workload, measure tok/s
    │   └── NO → ignore
    └── NO → ignore for this hardware generation
```

### Signals to INTEGRATE soon

1. **License unlock** — Apache 2.0 on a tier where previously only restrictive licenses existed (e.g., gpt-oss in a tier previously held by Llama).
2. **Tier fill** — closes a gap that forced cloud routing previously (e.g., Qwopus gave us local-reasoning that didn't exist).
3. **Quality jump** — beats current tier occupant by >10% on your actual workload.
4. **Deployment simplification** — same tier but easier deployment (Ollama day-0 vs custom library).

### Signals to WATCH (not integrate)

1. Same tier, same license, marginal capability gain.
2. New runtime with no model support yet (wait for coverage).
3. Benchmark-only claims with no downstream community validation.
4. Requires hardware you don't have.

### Signals to IGNORE

1. Single-benchmark cherry-pick with no replication.
2. Closed training + unclear attribution + dubious license.
3. Stale base model (pre-2024 models released as "new" fine-tunes) with no capability justification.
4. Single individual's model with no HF downloads and no runtime integration (watch; do not integrate).

## Red Flags and Counter-Readings

> [!warning] Common marketing frames that need Principle-4 interpretation
>
> | Marketing claim | Operational reality | Check |
> |-----------------|--------------------|-------|
> | "70B on 4GB VRAM" | 0.1 tok/s via disk-offload | Latency math on your NVMe |
> | "Runs on potato PC" | Runs slowly; may need 32GB RAM + competent CPU | Full model card + quantization table |
> | "Open-weight" | Weights yes; training data usually NO | LICENSE + model card "training data" section |
> | "Beats GPT-5 / Opus" | On which eval? With what methodology? | Look for eval harness name + multiple benchmarks |
> | "No quantization required" | Usually refers to a specific-precision default; quantization is optional | Read the quantization section carefully |
> | "Drop-in replacement" | Usually means "same API shape"; behavior and quality differ | Test on your real workload before replacing |

## Worked Examples (2026-04 Cohort)

### AirLLM (mechanism, not model)

- **Identify**: lyogavin/airllm, Apache 2.0, last release 2024-08 (stale). → **Flag: library maintenance risk**.
- **Size & fit**: mechanism, not a model — runs other models layer-wise from SSD.
- **Capability**: layer-offload from NVMe → GPU → discard → next layer.
- **Deployment**: library is stale; current production path is llama.cpp `-ngl N` or vLLM offload instead.
- **Slot**: local-batch tier (dense) or local-batch-MoE tier. Not a model itself.
- **Decision**: **use the mechanism, not the library** — llama.cpp / vLLM are the current integration targets.

### gpt-oss-20b (OpenAI, 2025-08)

- **Identify**: OpenAI, 2025-08, Apache 2.0. → **Strong signal: OpenAI-endorsed mainstream.**
- **Size & fit**: 21B total / 3.6B active, MXFP4 native, "fits in 16 GB of memory." → 19 GB VRAM machine: native fit with context headroom.
- **Capability**: function calling + browser + python + structured outputs + low/med/high reasoning + fully exposed CoT. Parity with closed frontier except absolute benchmark leaders.
- **Deployment**: Day-0 Ollama, LM Studio, vLLM, transformers, llama.cpp, TensorRT-LLM, Metal.
- **Slot**: local-fast (reasoning=low), local-reasoning (reasoning=high).
- **Decision**: **integrate first** — most mature option for the local-fast + local-reasoning tiers.

### gpt-oss-120b (OpenAI, 2025-08)

- Same release as above. 117B / 5.1B active, MXFP4 native, needs 80 GB VRAM for native in-VRAM.
- **For 19 GB VRAM**: needs offload. MoE-aware → ~2-3 tok/s via llama.cpp `-ngl N` or vLLM offload.
- **Slot**: local-batch (MoE) tier — agent-viable, not chat-viable.
- **Decision**: **integrate second**, after gpt-oss-20b is live and measured.

### Qwopus3.5-27B-v3 (Jackrong, 2026)

- **Identify**: Jackrong (individual developer), 2026, Apache 2.0, base Qwen3.5-27B (Apache 2.0). 1M+ downloads across family — **strong community validation**.
- **Size & fit**: GGUF quantization table available. Q4_K_M = 16.5 GB, **fits 19 GB VRAM with ~2 GB context headroom**. Q3_K_M = 13.3 GB safer default.
- **Capability**: 95.73% HumanEval+, structural-alignment fine-tune (not just distillation), native tool-calling, long CoT. Creative-writing capability matches Claude Sonnet 4.5 per independent review (decrypt.co 2026-04-12).
- **Deployment**: llama.cpp, LM Studio, Ollama, GPT4All — full consumer ecosystem.
- **Slot**: local-reasoning tier (competitive with gpt-oss-20b at reasoning=high).
- **Decision**: **test head-to-head with gpt-oss-20b** on AICP workload. Both occupy the local-reasoning tier; empirical comparison decides which dominates (or whether they complement — Qwopus for creative/long-form, gpt-oss for tool-augmented agents).

## Answering "I Don't Know Where to Look"

> [!tip] Your authoritative reading order for any new model announcement
>
> 1. **HuggingFace model card** (5 min) — architecture table, quantization variants, license, sometimes benchmarks
> 2. **GitHub README** if present (5 min) — training methodology, deployment examples, community
> 3. **arXiv paper / model card PDF** if formal release (skim 10-15 min) — full benchmarks, methodology rigor
> 4. **One tech-journalism piece** (5 min) — narrative context, head-to-head with alternatives, community sentiment
> 5. **Run this framework** (Stages 1-5, 20 min) — decide
> 6. **If decided to integrate**: deploy smallest quantization first, measure tok/s on your hardware, scale up

This produces a defensible decision in ~1 hour for any new model. It does NOT produce a production deployment decision — that requires real workload measurement, which takes days. But it gets you from "new announcement" to "worth my time yes/no" quickly and repeatably.

## Connection to Principles

- **Principle 4** ([[declarations-are-aspirational-until-infrastructure-verifies-them|Declarations Aspirational Until Verified]]) — every marketing claim ("runs on 4GB", "beats Opus", "open-weight") is aspirational until verified against specific hardware and specific workload. Stage 2 and Stage 3 are the verification gates.
- **Principle 3** (Goldilocks) — the "does it fit HERE" check is Goldilocks applied at the model-selection layer. A POC tolerates a bigger quantization-quality trade-off than production.
- **Principle 2** (Structured Context > Content) — the tables in this framework ARE the structured context that make this guide actionable versus narrative prose. An agent parsing this page can follow the decision tree without reinterpretation.
- **Principle 1** (Infrastructure > Instructions) — the ultimate version of this framework is INFRASTRUCTURE: a gateway command `python3 -m tools.gateway evaluate-model <url>` that fetches, extracts, scores, and returns a routing-table decision. That is future work; this page is the current instruction-layer equivalent.

## Open Questions

> [!question] Should this be a gateway command / script?
> Right now the framework is manual checklist. A `tools.gateway evaluate-model` command could fetch the model card, parse quantization variants vs the operator's hardware profile, check runtime support, and return a routing-slot recommendation. Principle-1 says: if it can be automated, it should be. Candidate for future epic.

> [!question] How should this framework evolve as MoE becomes universal?
> As 2026+ models are majority-MoE (gpt-oss, DeepSeek, Qwen 3 MoE, Llama 4 MoE), the VRAM math becomes "total size for in-VRAM, active-param bandwidth for offload." Framework should probably restructure Stage 2 to branch on dense vs MoE.

> [!question] What is the pass-fail threshold for "worth testing"?
> Currently implicit in the decision tree. Should be explicit: "if model matches tier AND license OK AND deployment 1-day-or-less, always test" vs "if benchmark gap > 10% and tier-filling, test even if deployment expensive."

## Key Pages

| Page | Role |
|------|------|
| [[model-local-ai\|Model — Local AI ($0 Target)]] | The routing model this framework feeds into |
| [[src-gpt-oss-openai-open-weight-moe\|gpt-oss synthesis]] | Primary worked example, 2025-08 |
| [[src-airllm-layer-wise-inference-nvme-ssd-offload\|AirLLM synthesis]] | Mechanism analysis, library-vs-mechanism distinction |
| [[src-qwopus-claude-opus-reasoning-distilled-qwen-27b\|Qwopus synthesis]] | Distillation-based local-reasoning model |
| [[src-turboquant-122b-macbook\|TurboQuant synthesis]] | Apple Silicon parallel approach |
| [[declarations-are-aspirational-until-infrastructure-verifies-them\|Principle — Declarations Aspirational]] | Applies to every marketing claim in model announcements |
| [[local-llm-quantization\|Local LLM Quantization]] | Deep dive on quantization mechanics |
| [[local-model-vs-cloud-api-for-routine-operations\|Decision — Local vs Cloud Routing]] | The routing-decision framework |

## How This Connects — Navigate From Here

> [!abstract] From This Framework → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **The routing model** | [[model-local-ai\|Model — Local AI ($0 Target)]] |
> | **Applied worked examples** | [[src-gpt-oss-openai-open-weight-moe\|gpt-oss]], [[src-airllm-layer-wise-inference-nvme-ssd-offload\|AirLLM]], [[src-qwopus-claude-opus-reasoning-distilled-qwen-27b\|Qwopus]] |
> | **Principle this operationalizes** | [[declarations-are-aspirational-until-infrastructure-verifies-them\|Principle 4]] |
> | **The super-model** | [[super-model\|Super-Model]] |

## Relationships

- BUILDS ON: [[model-local-ai|Model — Local AI ($0 Target)]]
- BUILDS ON: [[declarations-are-aspirational-until-infrastructure-verifies-them|Principle — Declarations Aspirational Until Verified]]
- FEEDS INTO: [[model-local-ai|Model — Local AI ($0 Target)]]
- FEEDS INTO: [[local-model-vs-cloud-api-for-routine-operations|Decision — Local vs Cloud Routing]]
- RELATES TO: [[src-gpt-oss-openai-open-weight-moe|Synthesis — gpt-oss]]
- RELATES TO: [[src-airllm-layer-wise-inference-nvme-ssd-offload|Synthesis — AirLLM]]
- RELATES TO: [[src-qwopus-claude-opus-reasoning-distilled-qwen-27b|Synthesis — Qwopus]]
- RELATES TO: [[local-llm-quantization|Local LLM Quantization]]

## Backlinks

[[model-local-ai|Model — Local AI ($0 Target)]]
[[Principle — Declarations Aspirational Until Verified]]
[[Decision — Local vs Cloud Routing]]
[[Synthesis — gpt-oss]]
[[Synthesis — AirLLM]]
[[Synthesis — Qwopus]]
[[local-llm-quantization|Local LLM Quantization]]
