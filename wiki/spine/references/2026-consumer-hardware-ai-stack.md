---
title: "The 2026 Consumer-Hardware AI Stack — Strategic Synthesis"
aliases:
  - "The 2026 Consumer-Hardware AI Stack — Strategic Synthesis"
  - "2026 Consumer AI Stack"
  - "Four-Layer Consumer-Hardware AI Stack"
type: reference
domain: cross-domain
layer: spine
status: synthesized
confidence: high
maturity: growing
created: 2026-04-17
updated: 2026-04-17
sources:
  - id: src-unsloth-fast-lora-consumer-hardware
    type: wiki
    file: wiki/sources/tools-integration/src-unsloth-fast-lora-consumer-hardware.md
    title: "Synthesis — Unsloth"
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
  - id: open-model-evaluation-framework
    type: wiki
    file: wiki/spine/references/open-model-evaluation-framework.md
    title: "Open-Model Evaluation Framework"
tags: [strategic-synthesis, consumer-hardware, local-ai, open-weight, ecosystem, cost-optimization, 2026-landscape, aicp, spine]
---

# The 2026 Consumer-Hardware AI Stack — Strategic Synthesis

## Summary

Between late 2024 and mid-2026, four independent layers of the AI stack crossed the consumer-hardware feasibility threshold simultaneously: **training** (Unsloth reduces LoRA VRAM by 70% and trains gpt-oss-20B on Colab's free T4 tier), **base models** (gpt-oss under Apache 2.0, Qwen 3, Llama 4, DeepSeek V3 all competitive with closed frontier), **capability-beyond-VRAM** (AirLLM + llama.cpp + vLLM enable MoE disk-offload at 2-3 tok/s), and **routing** (the second brain's 7-tier routing model now has concrete fills for every tier). This page synthesizes today's 2026-04-17 ingestion wave (AirLLM, gpt-oss, Qwopus v3, Unsloth) into one cohesive picture of the four-layer consumer-hardware AI stack, its implications for AICP's 80% Claude-reduction target, and the operator's next concrete moves. The headline: **the barrier to running, fine-tuning, and deploying frontier-adjacent AI on a 19 GB VRAM machine is no longer technical — it is integration effort measured in days, not infrastructure measured in dollars.**

## The Four-Layer Stack — One Day, Four Ingestions, One Picture

> [!info] **The four layers that crossed the consumer-hardware threshold**
>
> | Layer | What it provides | 2026 example | Hardware floor | Matured |
> |-------|------------------|--------------|----------------|---------|
> | **1. Training** | LoRA / QLoRA / RL fine-tuning | [[src-unsloth-fast-lora-consumer-hardware\|Unsloth]] | 16 GB VRAM (Colab T4 free tier) | 2024-2025 |
> | **2. Base models** | Competitive open-weight models | [[src-gpt-oss-openai-open-weight-moe\|gpt-oss-20b]], [[src-qwopus-claude-opus-reasoning-distilled-qwen-27b\|Qwopus v3]] | 16-20 GB for 20-27B Q4 | 2025-2026 |
> | **3. Capability-beyond-VRAM** | Disk-offload / MoE-aware inference | [[src-airllm-layer-wise-inference-nvme-ssd-offload\|AirLLM]], llama.cpp `-ngl`, vLLM offload | 19 GB VRAM + Gen4 NVMe | 2024-2026 |
> | **4. Routing** | Task-to-tier mapping, hybrid local/cloud | [[model-local-ai\|Model — Local AI]] + [[open-model-evaluation-framework\|Evaluation Framework]] | N/A (software) | 2026 (today) |

Before 2024: each layer had a gap. Training needed an A100. Competitive bases were closed-weight. Offload was slow-and-dumb. Routing was ad-hoc. **The gap in any one layer forced cloud dependency.** In 2026 the gap closed on all four layers concurrently — and that concurrency is what enables something qualitatively different from any layer's improvement in isolation.

## What This Enables That Didn't Exist Before

> [!abstract] **Capabilities that are now feasible and weren't in early 2024**
>
> | Capability | 2024 reality | 2026 reality |
> |------------|---------------|---------------|
> | Deploy a frontier-adjacent reasoning agent locally | Not feasible below H100 | gpt-oss-20b on 16 GB VRAM with full agentic capabilities |
> | Fine-tune a specialized model on your corpus | A100/H100 + research budget | Colab free T4, 2-6 hours, ~$0 (Unsloth) |
> | Run a 120B MoE model locally | Needed 80 GB VRAM minimum | 19 GB VRAM + NVMe via llama.cpp offload at 2-3 tok/s |
> | Ship a local agent with tool calling + structured outputs | Unreliable with open models | gpt-oss and Qwopus both native |
> | Legal-friction-free commercial deployment | Meta community license or closed API | Apache 2.0 on gpt-oss, Qwen 3, Qwopus, Unsloth |
> | Domain-specific model in one day | Required a team + research cycle | Unsloth Data Recipe → LoRA → GGUF → deploy |

The operational consequence: **every capability the second brain previously routed to cloud for cost reasons can now be re-examined**. Not "is this hard to route" but "which tier of the local stack does this match against."

## How This Reshapes AICP's Roadmap

AICP's 5-stage independence roadmap was designed in 2024 under the assumption that Stage 5 ("80%+ Claude reduction") would be hardware-blocked on 19 GB VRAM. The 2026 landscape inverts this:

> [!info] **AICP Stage-Status — Before and After 2026-04-17 Evidence**
>
> | Stage | Goal | Pre-2026-04 status | Post-2026-04-17 status |
> |-------|------|---------------------|--------------------------|
> | 1 | LocalAI functional — models loaded, GPU, health | Complete | Complete |
> | 2 | Route simple ops to LocalAI | Complete | Complete |
> | 3 | Progressive offload — heartbeats, reviews, status | **Blocked on 19 GB VRAM** | **Unblocked — 19 GB is actual + gpt-oss-20b fills the reasoning tier** |
> | 4 | Reliability + failover — circuit breakers tuned | Planned | Planned (unchanged) |
> | 5 | Near-independent — 80%+ Claude reduction | Aspirational / distant | **Reachable via integration, not hardware** |

**The blocker moved.** AICP's next real work is wiring:
1. gpt-oss-20b into the routing as the local-reasoning tier
2. gpt-oss-120b via llama.cpp offload as the local-batch-reasoning tier
3. Unsloth-trained wiki-corpus fine-tune (Qwen3.5-4B base) as the methodology-maintenance tier
4. Circuit-breaker and DLQ implementation (Stage 4, already planned)

Four wiring tasks. None are research; all are integration. The Stage 5 target becomes a Q2-Q3 2026 objective rather than a multi-year horizon.

## Implications for the $0 Target

The [[model-local-ai|Model — Local AI]] page declared the $0 target "achievable for routine operations, not all operations." That framing was correct in 2024. In 2026 the scope expands:

> [!success] **What is now $0-feasible vs what still routes to cloud**
>
> | Task class | 2024 routing | 2026 routing |
> |------------|---------------|---------------|
> | Heartbeats, status checks, lint | Local ✓ | Local ✓ |
> | Manifest regen, scaffolding | Local ✓ | Local ✓ |
> | **Post-chain validation** | Cloud (validation complexity) | Local ✓ (gpt-oss-20b) |
> | **Multi-step agent workflows with tool calls** | Cloud (reliability) | Local ✓ (gpt-oss-20b / Qwopus v3) |
> | **Code review of small PRs** | Cloud (quality) | Local ✓ (Qwopus v3 coding advantage) |
> | **Wiki-page validation, relationship suggestions** | Cloud (novel synthesis) | Local ✓ (wiki-corpus fine-tune, via Unsloth) |
> | **Substantive reasoning on corpus-wide analysis** | Cloud | Local ✓ batch tier (gpt-oss-120b via offload) |
> | Novel cross-domain synthesis | Cloud | **Cloud** (genuine novelty at stake) |
> | Architecture decisions, security review | Cloud | **Cloud** (high stakes, judgment required) |
> | Final methodology evolution judgment | Cloud | **Cloud** (operator-supervised boundary) |

**The new equilibrium**: ~90% local / ~10% cloud for a mature deployment, up from the original 80/20 target. The 10% that stays cloud is **high-stakes novel judgment** — everything else has a local tier that meets the quality bar.

## Implications for the Ecosystem (Sister Projects)

### OpenArms
Consumer-hardware training + LoRA adapters = OpenArms can ship **agent-specific fine-tunes** alongside its deployment artifacts. The harness v2 can distribute a base + task-specific LoRAs per agent role. Previously this required per-agent prompts squeezed into context; now it's model-level specialization.

### OpenFleet
Fleet agents that currently require Claude for complex work can route to gpt-oss-20b + tool calls at $0 per invocation. Apache 2.0 licensing means gpt-oss can ship *bundled* with OpenFleet deployments — no per-invocation API dependency, no rate-limit exposure, full sovereignty. OpenFleet's first-consumer session (2026-04-16, documented in [[verify-before-contributing-to-external-knowledge-systems|the inbox lesson]]) becomes re-runnable with a local-first routing.

### AICP
As above — the primary beneficiary of today's evidence. Integration-blocked on four concrete tasks, not hardware-blocked.

### devops-control-plane
The Apache 2.0 licensing matters here specifically: DCP handles infrastructure governance where policy and audit trails matter. Running gpt-oss / Qwopus locally means the reasoning traces NEVER leave the machine — a structural win for sensitive infrastructure decisions.

### Research Wiki (this project)
The wiki IS the highest-value fine-tuning corpus in the ecosystem: 368 curated pages, 2461 relationships, 16 models, 22+ standards, all consistent-schema Markdown. A Qwen3.5-4B LoRA fine-tune on the wiki corpus produces a methodology-fluent local assistant in 1-3 hours. This enables the wiki to *itself* become distributed intelligence (fine-tune ships with the wiki export) rather than only a reading surface.

## The Operator's Concrete Next Moves (Ranked by Impact × Ease)

> [!tip] **Actions the operator can take NOW, from easiest to highest-value**
>
> | Action | Hours | Output | Dependency |
> |--------|-------|--------|------------|
> | 1. Install Ollama + pull gpt-oss-20b | 0.5 h | Baseline measurement of local-reasoning tier on 19 GB | None |
> | 2. Install Ollama + pull Qwopus3.5-27B Q4_K_M | 0.5 h | Head-to-head comparison with gpt-oss-20b | #1 |
> | 3. Install Unsloth Studio (`curl -fsSL https://unsloth.ai/install.sh \| sh`) | 0.5 h | Local fine-tuning capability; Colab-free-tier feature parity | None |
> | 4. Run Qwen3.5-4B LoRA notebook end-to-end (any dataset) | 2-3 h | Toolchain familiarity; deployable adapter; confidence baseline | #3 |
> | 5. Run Unsloth Data Recipe on `wiki/` folder | 1 h | SFT dataset of ~300 training pairs from wiki corpus | #3 |
> | 6. Fine-tune Qwen3.5-4B on wiki corpus | 1-3 h | Methodology-fluent local model (GGUF) | #4, #5 |
> | 7. Wire gpt-oss-20b into AICP complexity scorer | 4-8 h | Stage 3 unblocked; ~50% local routing achievable | #1 + AICP integration |
> | 8. Wire gpt-oss-120b via llama.cpp `-ngl` into AICP batch tier | 4-8 h | Local-batch tier for substantive-reasoning tasks | #7 |
> | 9. Replace OpenFleet / AICP cloud routes with local tier per task class | 8-20 h | Actual $0-target achievement (>80% local) | #7, #8 |
> | 10. Replicate Qwopus pipeline with own teacher (Opus 4.6 traces) | 8-24 h + ~$5-20 Colab A100 | Custom reasoning-distilled 27B for the wiki's domain | #4 |

**Actions 1-6 produce a defensible local-AI capability in a single weekend**. Actions 7-10 are integration projects that transform the ecosystem's cost structure. None require new hardware beyond what operator has.

## What's Still Missing (Watch For)

> [!question] Gaps in the 2026-04-17 picture worth tracking
>
> | Gap | Why it matters | Signal to watch |
> |------|----------------|------------------|
> | **MLX training on Apple Silicon** | Unified-memory inference alternative to dGPU+NVMe | Unsloth's "MLX training coming very soon" ships |
> | **Multi-GPU Unsloth stability** | Fleet-scale training (agent-specific LoRAs at scale) | Unsloth's "major upgrade on the way" |
> | **vLLM production support maturity for gpt-oss offload on consumer hardware** | Moves gpt-oss-120b from batch tier to near-interactive | vLLM + gpt-oss + offload tutorials appearing |
> | **DeepSeek V3 / R1 local deployment** | 671B MoE, potential quality ceiling on consumer hardware | llama.cpp + offload tested on 19 GB VRAM |
> | **Llama 4 MoE integration** | Meta's response to gpt-oss; license details matter | Meta community license v3 terms |
> | **AirLLM gpt-oss native support** | If it ever ships, simplest offload path | AirLLM v2.12+ release with gpt-oss mentions |
> | **Reasoning-distilled models from Qwopus successors** | Training pipelines become easier → more domain-specialized distills | Jackrong's next model + community replicators |

None of these gaps block current AICP work. They are second-wave improvements that, as they land, further compress the cloud-routing fraction.

## 2026-04-22 Addendum — Kimi K2.6 Rewrites the Premium Tier

Five days after the original 2026-04-17 synthesis, **Moonshot AI released [[src-kimi-k2-6-moonshot-agent-swarm|Kimi K2.6]]** (2026-04-20) — a **1T-total / 32B-active MoE** that **leads Claude Opus 4.6 and GPT-5.4 on agentic reasoning (HLE-Full 54.0) and real-world coding (SWE-Bench Pro 58.6)**, under a modified MIT license, at OpenRouter pricing of **$0.80 / $3.50 per M tokens (~1/20th Opus)**. It adds a fifth layer to the stack:

> [!info] **Fifth layer — Premium/Routing at 1/20th Cost**
>
> | Layer | What it provides | 2026 example | Hardware floor | Matured |
> |-------|------------------|--------------|----------------|---------|
> | **5. Premium online (NEW)** | Frontier agentic capability at open-model prices | [[src-kimi-k2-6-moonshot-agent-swarm\|Kimi K2.6 via OpenRouter]] | N/A (online) | 2026-04-20 |
>
> And as a **local-batch-frontier** option: K2.6 Q2 GGUF (340 GB) via **KTransformers** on 19 GB VRAM + 64 GB RAM (incoming) + RAID 0 NVMe swap — realistic ~3-10 tok/s.

> [!info] **Layer 5 has three sub-paths (added 2026-04-23)**
>
> | Sub-path | Cost model | Best for | Privacy |
> |---|---|---|---|
> | **5a. OpenRouter → K2.6** | $0.80 / $3.50 per M tokens | Daily default; per-request cost visibility; client-adjacent tasks | Medium (routed) |
> | **5b. Ollama Cloud → K2.6** | $20/month flat (Pro plan, all cloud models) | Heavy prototyping, volume-unbounded experimentation (>5M output tokens/month breakeven) | Low — prototyping only; author of [[src-kimi-k2-6-ollama-cloud-njenga\|Njenga walkthrough]] explicitly warns off client/monetizable work |
> | **5c. Local K2.6 Q2** | $0/token (Tier 2) | Offline, confidential, $0-target | High |
>
> See [[src-kimi-k2-6-moonshot-agent-swarm|Kimi K2.6 synthesis]] § Three access paths for the full matrix, cost-math breakeven, and revised tier-stack rule. Not mutually exclusive — configure all three; route per session.

## 2026-04-24 Addendum — Local K2.6 Postmortem Supersedes Parts of the 2026-04-22 Framing

AICP's 2026-04-22 through 2026-04-24 analysis (8 docs, 3,300+ lines) produced an empirical postmortem on local K2.6 as a primary tier — now captured in [[ai-infrastructure-decision-framework-2026|AI Infrastructure Decision Framework 2026]]. Four concrete updates to the Layer-5 framing above:

> [!warning] The "local-batch-frontier at ~3-10 tok/s" estimate was wrong in practice
> Measured reality on operator's Tier-0 hardware (RTX 2080 Ti + RTX 2080, 64 GB DDR4, NVMe swap) via llama.cpp `-ngl 0`: **~0.3 tok/s**. That is technically-working, not practically-usable. Local K2.6 Q2 is a **sovereignty-insurance fallback** for batch-tolerant work only, not a daily inference tier. The "realistic ~3-10 tok/s" estimate assumed KTransformers MoE-aware offload optimizations that did not materialize on consumer hardware in a usable form.

> [!warning] Hardware break-even does not pay back for operator's projected volume
> AICP's HARDWARE-BUILD-SCENARIOS (CAD pricing, 2026-04-24 quotes) + SCALING-PROJECTION-5YR shows that **no hardware tier pays back** at operator's realistic 5-year workload (2-3 personal sessions + 1-2 fleets of 10 agents). Tier 1 ~$15-19k CAD, Tier 2 ~$32k CAD, Tier 3 ~$65-80k CAD; smart-routed cloud totals ~$11,460 CAD over 5 years. Hardware is **capability insurance priced on non-economic grounds**, never "cheaper long-term."

> [!success] The personal-daily default should be Ollama Cloud Pro, not OpenRouter
> Prior framing (2026-04-22) named OpenRouter as the daily default. AICP's 2026-04-24 cost math flips this for personal work: Ollama Cloud Pro at **$27 CAD/mo flat** is mission-aligned (open-weight models only) and covers unlimited iteration up to ~20-30M tokens/mo soft-cap. **OpenRouter remains the client-work default** — per-request cost visibility and pinnable provider. Do not route employer/client work through Ollama's shared pool.

> [!info] Subscription framework: phase-gated, not volume-permissive
> The 4-phase framework ([[ai-infrastructure-decision-framework-2026|framework doc]]) gates tier upgrades on **sustained** volume — 2+ consecutive months above the next-phase threshold, not single-month spikes. Operator's prior $540 CAD/mo baseline (2× Anthropic + other) is replaced in Phase 1 by **$40-70 CAD/mo** smart-routed — ~1/10 the cost, with mission alignment.

### Revised routing table (post-2026-04-24)

> [!success] **$0-target and mission-aligned routing** (post-postmortem)
>
> | Task class | 2026-04-22 routing | 2026-04-24+ routing |
> |------------|---------------------|---------------------|
> | Multi-step agent workflows with tool calls | K2.6 cheap-cloud OR local | **K2.6 via Ollama Cloud Pro** (personal) / **OpenRouter** (client) |
> | Code review, refactors on public code | K2.6 cheap-cloud | **K2.6 via Ollama Cloud Pro** — or **GPT-5.1-codex-mini via OpenRouter** ($0.25/$2) as closed-weight cost-minimum option |
> | Substantive reasoning on corpus-wide analysis | K2.6 cheap-cloud OR local-batch | **K2.6 via Ollama Cloud Pro** — local-batch only if privacy-required and batch-tolerant |
> | Client / employer / private-repo work | K2.6 cheap-cloud (unspecified) | **K2.6 via OpenRouter with pinned provider** — never Ollama shared pool |
> | Offline / regulatory / sovereignty-hard | Local | **Local llama.cpp** (accept 0.3 tok/s batch) |
> | Pure-math reasoning (rare) | Opus fallback | **GPT-5.x** ($2.50/$15 tier); mission-exception logged |

**What this changes in the summary table** (updated 2026-04-22):

> [!success] **$0 target and premium-cheap routing** (post-K2.6 update)
>
> | Task class | 2024 routing | 2026-04-17 routing | 2026-04-22 routing |
> |------------|---------------|---------------------|---------------------|
> | Multi-step agent workflows with tool calls | Cloud | Local (gpt-oss / Qwopus) | **K2.6 cheap-cloud OR local** |
> | Code review, refactors | Cloud | Local (Qwopus) | **K2.6 cheap-cloud (58.6 SWE-Pro) OR local** |
> | Substantive reasoning on corpus-wide analysis | Cloud | Local batch (gpt-oss-120b offload) | **K2.6 cheap-cloud OR K2.6 local-batch** |
> | Novel cross-domain synthesis | Cloud (Opus) | Cloud (Opus) | **K2.6 cheap-cloud (agentic SOTA) — falls back to Opus only for pure-math / vision corners** |
> | Architecture decisions, security review | Cloud (Opus) | Cloud (Opus) | **K2.6 cheap-cloud primary, Opus 4.7 xhigh as deliberate fallback** |

**The new equilibrium**: ~90% local + ~8% K2.6-on-OpenRouter + ~2% Opus (or direct Moonshot) for the remaining pure-math / maximum-stakes / very-long-context corners. The cloud-spend budget effectively collapses by an order of magnitude for the same quality ceiling.

**Operator's 5-day self-autonomous workstation plan gains one critical path**: validate Claude Code CLI → OpenRouter → K2.6 (via `ANTHROPIC_BASE_URL` env var) on day 1. If it works, the Claude Code subscription transition (2026-04-27) becomes a non-event — the harness stays, the backend changes, the cost falls ~95%. Add to the operator's concrete next-moves table:

> [!tip] **Post-K2.6 next moves**
>
> | Action | Hours | Output | Dependency |
> |--------|-------|--------|------------|
> | 11. OpenRouter account + K2.6 API key | 0.5 h | Primary premium-cheap route available | None |
> | 12. Test Claude Code CLI → OpenRouter → K2.6 via env vars on wiki workload | 1-2 h | Subscription deadline de-risked | #11 |
> | 13. Download K2.6 Q2 GGUF (340 GB) to RAID 0 NVMe | 2-4 h (network-bound) | Offline frontier capability staged | 1 TB NVMe free |
> | 14. KTransformers setup + K2.6 Q2 local benchmark | 3-6 h | Real tok/s measured; Tier 2 viability confirmed | #13 + 64 GB RAM installed |
> | 15. Wire K2.6 as AICP premium-cheap tier (OpenRouter first, local fallback) | 4-8 h | ~90% local + ~8% K2.6 routing-split reached | #7, #12 |

## 2026-04-25 Addendum — Qwen3.6-27B Resets the Layer-2 Dense Tier

Three days after the 2026-04-22 K2.6 update and one day after the 2026-04-24 local-K2.6 postmortem, **Alibaba Qwen released [[src-qwen3-6-27b-dense-beats-397b-moe-agentic-coding|Qwen3.6-27B]]** (2026-04-22) — the first **dense** open-weight model in the Qwen3.6 family, **Apache 2.0**, **natively multimodal**, with a **hybrid Gated DeltaNet + Gated Attention architecture** (75% linear attention / 25% standard) that beats both Qwen3.6-35B-A3B (sparse MoE) and the much-larger **Qwen3.5-397B-A17B MoE** on agentic coding benchmarks. Day-of operational evidence from the [[src-qwen3-6-27b-2-bit-26-tool-calls-unsloth-discussion|Unsloth GGUF discussion]] confirms the **2-bit UD-IQ2 quantization** retains agentic capability — Daniel/Unsloth showcased the 2-bit model making **26 sequential tool calls**. This redraws the Layer-2 (Base models) row in the four-layer stack.

> [!success] **The headline finding — 27B dense beats 397B MoE on agentic coding**
>
> | Benchmark | Qwen3.5-27B | Qwen3.6-27B | Qwen3.5-397B-A17B (MoE) | Claude 4.5 Opus | Kimi K2.6 |
> |---|---|---|---|---|---|
> | SWE-bench Verified | 75.0 | **77.2** | — | 80.9 | — |
> | **SWE-bench Pro** | 51.2 | **53.5** | **50.9** ← lower | — | **58.6** |
> | Terminal-Bench 2.0 (3h, 32 CPU, 48GB RAM) | — | **59.3** | — | **59.3** ← match | — |
> | QwenWebBench (front-end coding) | 1068 | **1487** | — | — | — |
> | NL2Repo | 27.3 | **36.2** | — | — | — |
> | SkillsBench Avg5 | 27.2 | **48.2** (77% relative) | — | — | — |
>
> A **14.7× smaller dense model** beating a 397B MoE on the agentic-coding benchmark that matters most. This is empirical validation that **dense-and-trained-well outperforms parameter-count-as-proxy at the consumer-hardware tier**.

### Architectural innovations relevant to consumer-hardware deployment

> [!info] Why the architecture matters for tier-0 (19-32 GB VRAM)
>
> | Mechanism | Effect on consumer-hardware feasibility |
> |---|---|
> | **75% Gated DeltaNet (linear attention)** | O(n) attention dominates — long-context cost stays manageable on consumer GPUs even at 262K native context |
> | **25% Gated Attention with 4 KV heads** | Dramatically reduces KV cache memory (4 KV heads vs typical 8-16) — drives down inference VRAM |
> | **Multi-Token Prediction (MTP) trained multi-step** | Enables speculative decoding at inference — multi-token-per-step throughput without quality compromise |
> | **Thinking Preservation** (`chat_template_kwargs.preserve_thinking: True`) | Retains historical CoT across conversation turns — **stateful reasoning at the architecture level**; reduces redundant token generation in agentic loops; complements [[src-anthropic-effective-harnesses-long-running-agents\|Anthropic's harness state-file pattern]] |
> | **Native multimodal** (text + image + video, Causal LM with Vision Encoder) | Single model handles all modalities — no separate vision pipeline; mmproj GGUF files (BF16/F16/F32) ship alongside main quants |
> | **YaRN context extension** | 262K native → 1M tokens (recommended ≥128K to preserve thinking capability) |

### Updated Layer-2 row

> [!info] **Layer 2 (Base models) — post-2026-04-25**
>
> | Layer | What it provides | 2026 example | Hardware floor | Matured |
> |-------|------------------|--------------|----------------|---------|
> | **2. Base models** | Competitive open-weight models | [[src-qwen3-6-27b-dense-beats-397b-moe-agentic-coding\|**Qwen3.6-27B (DENSE — new tier leader)**]], [[src-gpt-oss-openai-open-weight-moe\|gpt-oss-20b]], [[src-qwopus-claude-opus-reasoning-distilled-qwen-27b\|Qwopus v3]] | 16-20 GB for 20-27B Q4 · 5-7 GB for Qwen3.6-27B UD-IQ2 (2-bit) | 2025-2026 |
>
> **Operator framing (verbatim, 2026-04-25):** *"this is our best bet for this tier 0 machine / system."* The 2-bit UD-IQ2 quant fits comfortably in the operator's RTX 2080 Ti VRAM budget while the 26-tool-call demonstration confirms agentic capability is preserved at that quantization level.

### Mission-relevant signal — the Opus-distillation hint

> [!warning] **Worth tracking, not yet authoritative**
>
> An Unsloth-discussion commenter (`owao`) asked why "Here is a reasoning process\n\n" residue from Claude Opus traces wasn't stripped from training data — implying **Qwen3.6-27B's reasoning may be partially distilled from Opus traces** (similar to the [[src-qwopus-claude-opus-reasoning-distilled-qwen-27b\|Qwopus pattern]] but at the official-Alibaba-channel scale). If true, this has **two contradictory mission implications**:
>
> | Frame | Implication |
> |---|---|
> | **Pro post-Anthropic stack** | The Qwen3.6-27B reasoning quality compounds Opus's existing strengths — choosing it for the local tier captures Opus reasoning provenance without per-token Anthropic cost. The post-Anthropic stack effectively inherits Opus's reasoning DNA at $0/token. |
> | **Caveat for the stack's "anti-vendor-lock-in" mission** | Per the operator's saved memory: *"specialty routing across providers is mission-aligned; default-tier lock-in is the violation."* If Qwen3.6-27B's reasoning provenance traces back to Opus training data, the operator's stack still has indirect Anthropic dependency at the **training-data level** — not a runtime dependency, but a quality-provenance one. |
>
> Confidence: **medium → low** until corroborated. Verification candidates:
> 1. Independent residue analysis across N outputs
> 2. Official Qwen team statement on training-data composition
> 3. Cross-reference with known Qwopus distillation traces
>
> **Operator stance (consistent with the 2026-04-24 mission framing):** the distillation provenance is a *signal worth knowing* but does not change the candidacy decision — the model is open-weight Apache 2.0, no Anthropic API runtime dependency, the reasoning quality is empirically there. The mission's actual constraint is "anti-vendor-lock-in," and Qwen3.6-27B satisfies that whether or not its training data included Opus traces.

### Three Qwen tier-0 deployment paths (added to the existing Layer 2 framing)

> [!abstract] How to actually deploy Qwen3.6-27B on tier-0 hardware
>
> | Path | Hardware | Toolchain | Speed estimate | Best for |
> |---|---|---|---|---|
> | **2a. Qwen3.6-27B BF16 (full precision)** | 16+ GB VRAM (e.g., RTX 4080/4090/A6000) | SGLang ≥0.5.10 / vLLM ≥0.19.0 / KTransformers / HF Transformers | Native | Reference-quality inference; baseline measurement |
> | **2b. Qwen3.6-27B FP8 (block size 128)** | 12-16 GB VRAM | Same toolchains | ~Native (near-identical quality) | Production-grade inference at half VRAM |
> | **2c. Qwen3.6-27B UD-IQ2 (2-bit Unsloth Dynamic)** | **5-7 GB VRAM (operator's tier-0 path)** | llama.cpp / Unsloth Studio | Slower per-token but fits where BF16/FP8 don't | The operator's "best bet for tier 0" — agentic capability proven via the 26-tool-call demo |
> | **2d. Qwen3.6-27B + multimodal (mmproj-BF16/F16/F32)** | +1-3 GB on top of any of the above | Same + mmproj loaded | Same | Image/video input — single-model multimodal vs separate vision pipeline |
>
> The **2c path is what the operator named** — "tier 0 machine / system." Path 2a-2b are higher-fidelity options if the operator's hardware is upgraded (the 64 GB RAM milestone from E010 + storage tiering would also enable path 2a on lower-VRAM cards via offload).

### Updated routing table (post-2026-04-25)

> [!success] **$0-target and mission-aligned routing** (post-Qwen3.6-27B)
>
> | Task class | 2026-04-24 routing | 2026-04-25+ routing |
> |------------|---------------------|---------------------|
> | Daily personal coding & multi-step agent workflows | K2.6 via Ollama Cloud Pro / OpenRouter | **Qwen3.6-27B local (UD-IQ2 or FP8 if VRAM allows)** — primary candidate · K2.6 via Ollama Cloud Pro as cloud fallback for context-heavy tasks (>262K tokens or quality-critical) |
> | Code review, refactors on public code | K2.6 cheap-cloud or GPT-5.1-codex-mini | **Qwen3.6-27B local** (SWE-bench Pro 53.5; matches Claude 4.5 Opus on Terminal-Bench 2.0) · K2.6 cheap-cloud only if cross-repo coordination needed |
> | Substantive reasoning on corpus-wide analysis | K2.6 via Ollama Cloud Pro | **Qwen3.6-27B local with Thinking Preservation enabled** — the multi-turn reasoning carry-forward gives this a structural advantage for corpus-wide work · K2.6 cheap-cloud as fallback |
> | Multimodal (image / video understanding) | Cloud (Opus 4.7 / Claude vision) | **Qwen3.6-27B local + mmproj** (native multimodal — VideoMME 87.7, AndroidWorld 70.3, VlmsAreBlind 97.0) |
> | Client / employer / private-repo work | K2.6 OpenRouter (pinned provider) | **Qwen3.6-27B local** (sovereignty) · K2.6 OpenRouter as cloud fallback |
> | Pure-math / max-stakes reasoning | GPT-5.x | **GPT-5.x or Opus 4.7** (no change — high-stakes still cloud, mission-exception logged) |
> | Offline / regulatory / sovereignty-hard | Local llama.cpp | **Qwen3.6-27B local** (Apache 2.0; no per-token cost; full sovereignty) |
>
> **The new equilibrium — post-Qwen3.6-27B:** ~95% local (Qwen3.6-27B) + ~3% cheap-cloud (K2.6 via Ollama Cloud Pro / OpenRouter) + ~2% premium-cloud (Opus 4.7 / GPT-5.x) for the remaining max-stakes corners. The cloud-spend budget shrinks again — and unlike the 2026-04-22 K2.6 framing where the cheap-cloud share was ~8%, Qwen3.6-27B's local-reasoning quality drops it to ~3%.

### Updated operator's concrete next-moves (post-Qwen3.6-27B)

> [!tip] **2026-04-25+ next moves**
>
> | Action | Hours | Output | Dependency |
> |--------|-------|--------|------------|
> | 16. Pull Qwen3.6-27B UD-IQ2 GGUF from Unsloth HF org | 0.5-1 h (network-bound) | Tier-0 model staged | None |
> | 17. Pull mmproj GGUF (BF16 or F16) for multimodal | 0.5 h | Vision capability staged | #16 |
> | 18. Test Qwen3.6-27B UD-IQ2 via llama.cpp on operator's RTX 2080 Ti | 1-2 h | Real tok/s + tool-call success rate measured on operator's hardware | #16 |
> | 19. Wire Qwen3.6-27B as AICP local-reasoning tier (replace gpt-oss-20b OR add as parallel option) | 4-8 h | Stage 3 routing updated; ~95% local achievable | #18 + AICP integration |
> | 20. Validate Thinking Preservation in agentic loops (vs without) | 2-4 h | Per-turn token-cost reduction quantified | #18 |
> | 21. Test Qwen3.6-27B's 26-tool-call capability on the wiki's `pipeline` toolset | 1-2 h | Confirm the model handles the wiki's internal tool surface | #18 |
> | 22. Independent residue analysis to confirm/refute Opus-distillation hint | 2-4 h | Mission-provenance question resolved | #18 |
> | 23. Replace gpt-oss-20b references in routing-related decisions with Qwen3.6-27B (if #18 confirms parity or better) | 1-2 h | Wiki routing decisions updated to reflect tier-0 candidate | #19 |
>
> **Action 18 is the load-bearing one for the 2026-04-27 mission deadline (T-2 days):** measured tok/s + tool-call success rate on the operator's actual hardware confirms or refutes the tier-0 candidacy at the empirical level. Without that measurement, "best bet for tier 0" is still aspirational — with it, the post-Anthropic stack's local-reasoning tier is committed.

### Connection to AICP's E008-E012 milestones

| Epic | What Qwen3.6-27B changes |
|---|---|
| **E008 — Local K2.6 offline frontier tier** | K2.6 local was deprioritized in 2026-04-24 postmortem (~0.3 tok/s on operator's hardware). Qwen3.6-27B replaces K2.6 local as the practical sovereignty tier — **at usable tok/s** because it's 27B dense (not 1T MoE). |
| **E009 — Harness Neutrality + OpenCode Parity** | Unchanged — harness-level work, not model-specific |
| **E010 — Storage and Hardware Enablement** | Lower priority for VRAM expansion if Qwen3.6-27B UD-IQ2 fits in current 5-7 GB. Higher priority if operator wants path 2a (BF16) for reference-quality. |
| **E011 — Routing Integration AICP Tiers** | **Significantly impacted.** Rewire from "K2.6 cloud / gpt-oss local" tiers to "Qwen3.6-27B local primary / K2.6 cloud fallback / Opus exception" tiers. Mission-load-bearing for 2026-04-27. |
| **E012 — Custom Model Library / Unsloth LoRAs** | **Boosted.** Qwen3.6-27B is the natural new base for wiki-corpus fine-tunes (replacing the originally-named Qwen3.5-4B). Larger base = more headroom for methodology fluency without losing tier-0 fit. |

## Connection to the Four Principles

> [!abstract] **How today's synthesis validates (or extends) the four principles**
>
> | Principle | Connection |
> |-----------|------------|
> | **1. Infrastructure > Instructions** | The evaluation framework ([[open-model-evaluation-framework\|5-stage flow]]) is the instruction-layer version. A future `tools.gateway evaluate-model <url>` that parses model cards, checks hardware fit, and returns routing decisions is the infrastructure-layer version — candidate future epic. |
> | **2. Structured Context > Content** | All four ingestion pages use tables (quantization variants, latency math, capability matrices, decision trees) rather than prose. Each page is readable as a table first, narrative second — structured context is load-bearing. |
> | **3. Goldilocks** | The 7-tier routing stack IS Goldilocks applied at the inference layer. POC → local-fast. Production reasoning → local-reasoning. Architecture review → cloud-heavy. Not "one tier for all," explicitly context-adapted. |
> | **4. Declarations Aspirational Until Verified** | Applied to every ingestion: AirLLM marketing ("70B on 4GB"), Unsloth marketing ("no accuracy loss"), gpt-oss claim ("fits 16 GB"), Qwopus benchmark ("95.73% HumanEval") — all checked against concrete verification (latency math, task-specific measurement, hardware fit, base-vs-plus-pass distinction). The framework embeds this check as a red-flag stage. |

The four principles held across a day of intensive ingestion with no gaps or exceptions. They **describe how this project evaluates external artifacts, not just how it produces internal ones**.

## Key Pages

| Page | Role |
|------|------|
| [[model-local-ai\|Model — Local AI ($0 Target)]] | The routing model this synthesis feeds strategic direction into |
| [[open-model-evaluation-framework\|Open-Model Evaluation Framework]] | The tactical process for evaluating any new model announcement |
| [[src-unsloth-fast-lora-consumer-hardware\|Unsloth synthesis]] | Training layer |
| [[src-gpt-oss-openai-open-weight-moe\|gpt-oss synthesis]] | Base-model layer (OpenAI Apache 2.0) |
| [[src-qwopus-claude-opus-reasoning-distilled-qwen-27b\|Qwopus synthesis]] | Base-model layer (distilled reasoning) |
| [[src-airllm-layer-wise-inference-nvme-ssd-offload\|AirLLM synthesis]] | Offload-mechanism layer |
| [[aicp\|AICP]] | The orchestration layer that integrates all of the above |
| [[declarations-are-aspirational-until-infrastructure-verifies-them\|Principle 4]] | Applied throughout this synthesis |

## How This Connects — Navigate From Here

> [!abstract] From This Synthesis → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **The tactical evaluation process** | [[open-model-evaluation-framework\|Open-Model Evaluation Framework]] |
> | **The routing model** | [[model-local-ai\|Model — Local AI]] |
> | **AICP integration context** | [[aicp\|AICP]] |
> | **Individual ingestions** | See sources table above |
> | **Principle framework** | [[declarations-are-aspirational-until-infrastructure-verifies-them\|Principle 4]], [[super-model\|Super-Model]] |

## Open Questions

> [!question] Should "Consumer-Hardware AI Stack Convergence" be promoted to a validated pattern?
> Four independent layers crossing the consumer-hardware threshold simultaneously is a pattern-level observation. Its structural form: "when N independent technology tracks reach a compatibility threshold concurrently, the combined capability is qualitatively greater than any single track's improvement." Candidate for [[wiki/patterns/01_drafts/]] with this ecosystem's instance + other compounding-technology-threshold examples (e.g. smartphones: capacitive touch + mobile internet + App Store, ~2008).

> [!question] What is the right epic to spawn from this synthesis?
> Candidate: **E024 — Local-First Routing Integration (Stage 3-5)**. Four concrete tasks (gpt-oss-20b wiring, gpt-oss-120b offload wiring, wiki-corpus fine-tune, circuit-breaker completion). Measurable outcome: routing-split metric moves from ~40% local to >80% local. Operator-supervised.

> [!question] Should the synthesis-of-syntheses pattern become a standard wiki type?
> Today's page synthesizes 4 ingestions + 1 framework into one strategic picture. That pattern (N source syntheses + framework → strategic synthesis) may recur whenever an ecosystem inflection point happens. Worth a page-type standard if it does (e.g. `type: strategic-synthesis`).

## Relationships

- BUILDS ON: [[src-unsloth-fast-lora-consumer-hardware|Synthesis — Unsloth]]
- BUILDS ON: [[src-gpt-oss-openai-open-weight-moe|Synthesis — gpt-oss]]
- BUILDS ON: [[src-airllm-layer-wise-inference-nvme-ssd-offload|Synthesis — AirLLM]]
- BUILDS ON: [[src-qwopus-claude-opus-reasoning-distilled-qwen-27b|Synthesis — Qwopus]]
- BUILDS ON: [[src-kimi-k2-6-moonshot-agent-swarm|Synthesis — Kimi K2.6]]
- BUILDS ON: [[open-model-evaluation-framework|Open-Model Evaluation Framework]]
- FEEDS INTO: [[model-local-ai|Model — Local AI ($0 Target)]]
- FEEDS INTO: [[aicp|AICP]]
- RELATES TO: [[super-model|Super-Model — Research Wiki as Ecosystem Intelligence Hub]]
- DEMONSTRATES: [[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4 — Declarations Aspirational Until Verified]]

## Backlinks

[[Synthesis — Unsloth]]
[[Synthesis — gpt-oss]]
[[Synthesis — AirLLM]]
[[Synthesis — Qwopus]]
[[Synthesis — Kimi K2.6]]
[[open-model-evaluation-framework|Open-Model Evaluation Framework]]
[[model-local-ai|Model — Local AI ($0 Target)]]
[[aicp|AICP]]
[[super-model|Super-Model — Research Wiki as Ecosystem Intelligence Hub]]
[[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4 — Declarations Aspirational Until Verified]]
[[2026-04-25-session-handoff-qwen3-6-27b-ingestion-batch|2026-04-25 Session Handoff — Qwen3.6-27B Ingestion Batch + Mission-Critical Spine Update]]
[[src-qwen3-6-27b-dense-beats-397b-moe-agentic-coding|Synthesis — Qwen3.6-27B: Dense 27B Beats 397B MoE on Agentic Coding]]
[[src-qwen3-6-27b-2-bit-26-tool-calls-unsloth-discussion|Synthesis — Unsloth GGUF: 2-bit Qwen3.6-27B Made 26 Tool Calls]]
