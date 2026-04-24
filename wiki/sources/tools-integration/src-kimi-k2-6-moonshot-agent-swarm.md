---
title: "Synthesis — Kimi K2.6: Moonshot's 1T/32B-Active Open-Weight Agentic Frontier Model"
aliases:
  - "Synthesis — Kimi K2.6: Moonshot's 1T/32B-Active Open-Weight Agentic Frontier Model"
  - "Synthesis: Kimi K2.6"
  - "Kimi K2.6 Source Synthesis"
  - "K2.6"
type: source-synthesis
layer: 1
maturity: growing
domain: ai-models
status: synthesized
confidence: high
created: 2026-04-22
updated: 2026-04-23
sources:
  - id: src-kimi-k2-6-blog
    type: blog-post
    url: https://www.kimi.com/blog/kimi-k2-6
    title: "Kimi K2.6 Tech Blog — Advancing Open-Source Coding (Moonshot AI)"
    ingested: 2026-04-22
  - id: src-kimi-k2-6-the-decoder
    type: article
    url: https://the-decoder.com/open-weight-kimi-k2-6-takes-on-gpt-5-4-and-claude-opus-4-6-with-agent-swarms/
    title: "Open-weight Kimi K2.6 takes on GPT-5.4 and Claude Opus 4.6 with agent swarms"
    ingested: 2026-04-22
  - id: src-kimi-k2-6-siliconangle
    type: article
    url: https://siliconangle.com/2026/04/20/moonshot-ai-releases-kimi-k2-6-model-1t-parameters-attention-optimizations/
    title: "Moonshot AI releases Kimi-K2.6 model with 1T parameters, attention optimizations"
    ingested: 2026-04-22
  - id: src-kimi-k2-6-marktechpost
    type: article
    url: https://www.marktechpost.com/2026/04/20/moonshot-ai-releases-kimi-k2-6-with-long-horizon-coding-agent-swarm-scaling-to-300-sub-agents-and-4000-coordinated-steps/
    title: "Moonshot AI Releases Kimi K2.6 with Long-Horizon Coding, Agent Swarm Scaling to 300 Sub-Agents"
    ingested: 2026-04-22
  - id: src-kimi-k2-6-unsloth-gguf
    type: repository
    url: https://huggingface.co/unsloth/Kimi-K2.6-GGUF
    title: "unsloth/Kimi-K2.6-GGUF — Hugging Face"
    ingested: 2026-04-22
  - id: src-kimi-k2-6-openrouter
    type: api-documentation
    url: https://openrouter.ai/moonshotai/kimi-k2.6
    title: "Kimi K2.6 — API Pricing & Providers | OpenRouter"
    ingested: 2026-04-22
  - id: src-kimi-benchmarks-buildfast
    type: article
    url: https://www.buildfastwithai.com/blogs/kimi-k2-6-vs-gpt-claude-benchmarks
    title: "Kimi K2.6 vs GPT-5.4 vs Claude Opus: Who Wins? (2026)"
    ingested: 2026-04-22
  - id: src-kimi-latent-space-ainews
    type: article
    url: https://www.latent.space/p/ainews-moonshot-kimi-k26-the-worlds
    title: "AINews — Moonshot Kimi K2.6: the world's leading Open Model refreshes to catch up to Opus 4.6"
    ingested: 2026-04-22
  - id: src-kimi-k2-6-ollama-cloud-njenga
    type: article
    url: https://medium.com/@joe.njenga/i-tried-kimi-k2-6-on-claude-code-and-forgot-opus-4-6-exists-5d9ba4c01911
    file: raw/articles/kimi-k2-6-claude-code-ollama-cloud-joe-njenga-medium.md
    title: "I Tried Kimi k2.6 on Claude Code (And Forgot Opus 4.6 Exists) — Joe Njenga"
    ingested: 2026-04-23
    description: "Hands-on walkthrough of `ollama launch claude --model kimi-k2.6:cloud` — a THIRD access path for K2.6 (alongside OpenRouter cloud and local KTransformers). Ollama Cloud Pro is $20/month flat for all cloud models (vs OpenRouter's per-token pricing). Setup is one command; Anthropic-compatible endpoint at localhost:11434. Cost-math breakeven vs OpenRouter: ~5-6M output tokens/month."
tags: [kimi, k2-6, moonshot, open-weight, mit-license, moe, mla, agentic, agent-swarm, long-horizon-coding, 256k-context, multimodal, gguf, openrouter, ollama-cloud, ktransformers, cost-optimization, aicp, access-paths]
---

# Synthesis — Kimi K2.6: Moonshot's 1T/32B-Active Open-Weight Agentic Frontier Model

## Summary

On **2026-04-20**, Moonshot AI released **Kimi K2.6** — a Mixture-of-Experts (MoE) model with **1 trillion total parameters and 32 billion activated per token**, 384 experts (8 + 1 shared selected), 61 layers, 64 attention heads using **Multi-head Latent Attention (MLA)** and SwiGLU activation, a **256K (262,144 token) context window**, a **400M-parameter MoonViT vision encoder** for native image and video input, and **Quantization-Aware Training (QAT)** producing native INT4 inference at ~2× speed. The license is a **modified MIT** — attribution requirement applies only to products exceeding 100M MAU or $20M monthly revenue. On elite benchmarks, K2.6 **leads the frontier on agentic tasks and real-world coding**: 54.0 on HLE-Full with Tools (vs 53.0 Claude Opus 4.6, 52.1 GPT-5.4), 58.6 on SWE-Bench Pro (vs 57.7 GPT-5.4, top rank), 66.7 on Terminal-Bench 2.0, 89.6 on LiveCodeBench, 83.2 on BrowseComp. It trails GPT-5.4 on pure math (AIME 2026: 96.4 vs 99.2) and Gemini 3.1 Pro on multimodal (MMMU-Pro: 79.4 vs 83.0). The signature capability is **Agent Swarm**: K2.6 dynamically decomposes a task into heterogeneous subtasks executed concurrently by **up to 300 self-created domain-specialized sub-agents across 4,000 coordinated steps**, with 12+h autonomous runs and 4,000+ tool-call chains demonstrated in Rust, Go, and Python. On OpenRouter, K2.6 is priced at **$0.80 per million input tokens and $3.50 per million output tokens** — roughly **1/20th of Claude Opus 4.6's pricing** — with 262K context and a `reasoning` parameter for step-by-step thinking exposure. For the operator's stack (19 GB VRAM + 64 GB RAM incoming + RAID 0 NVMe with large swap), K2.6 slots in **two places simultaneously**: Tier 3 premium/routing via OpenRouter (primary path, same-day), and Tier 2 disk-offload via KTransformers or llama.cpp on Q2 (340 GB GGUF) or Q4 (584 GB GGUF) quants for $0-target offline capability. K2.6 is the point where **open-weight has structurally caught the closed frontier on agentic workloads**, and where **the economics of "route everything premium through Claude" break down** for anyone not bound to Anthropic by subscription.

## Key Insights

> [!info] K2.6 is the current agentic frontier, not just a catch-up
> On HLE-Full with tools (agentic reasoning) K2.6 *beats* Opus 4.6 and GPT-5.4. On SWE-Bench Pro (real-world coding) it beats GPT-5.4. This is not "approaching parity" — it is the first time an open-weight model tops closed frontier on the benchmarks that actually matter for agent workloads.

> [!tip] 300-agent swarms × 4,000 steps × 12+h autonomy redefines long-horizon
> K2.6 is not sold as "a better chatbot." It is sold as a coordination substrate. The agent-swarm capability (300 sub-agents, 4,000 steps, 12h autonomous execution) is an entire class of workload the second brain's research pipelines can now offload — at OpenRouter prices this becomes strategically cheap.

> [!warning] Local inference is feasible but non-trivial on consumer hardware
> Q8 (lossless): 595 GB · Q4: 584 GB · Q2: 340 GB. On 19 GB VRAM + 64 GB RAM + RAID 0 NVMe swap, **Q2 via KTransformers is realistic at ~3-10 tok/s; Q4 is at the edge; Q8 is aspirational**. Not the Qwen3-8B "drop in and go" tier — needs setup effort and quality/speed trade-off measurement.

- **Architecture: MoE + MLA is the cost-per-capability engine.** 1T total parameters gives the model its capacity ceiling; 32B activated per token keeps compute tractable. MLA (Multi-head Latent Attention) compresses the KV cache aggressively vs standard MHA, which is what makes 256K context tractable in production. 384 experts (8 + 1 shared selected per token) is a deeper MoE than gpt-oss-120b (8 experts) or Mixtral (8) — more specialization per token at the cost of sharper routing requirements.

- **Agent Swarm is the key architectural differentiator.** Competing frontier models expose agent loops as application-layer patterns (ReAct, tool-calling, planner+executor). K2.6 exposes swarm orchestration as a **model-native capability**: the model itself decomposes, spawns, and coordinates. "Claw Groups" is a preview feature extending this to heterogeneous agent collaboration (human + model + specialized agents). For the wiki's multi-pass ingestion methodology (extract → cross-ref → gaps → deepen), this maps directly — one K2.6 invocation could orchestrate the full pipeline in parallel across 300 sub-agents.

- **QAT → native INT4 changes the "quantization tax" calculus.** Unlike post-hoc GGUF quantization (where Q4 is a compression of a BF16 model), K2.6 was trained with quantization-aware methods producing **native INT4 inference**. Combined with Unsloth's Dynamic 2.0 GGUFs (the operator's same Q2 or Q4 download), the quality loss at aggressive quantization is materially smaller than typical post-hoc quants. Practical consequence: on the operator's hardware, running Q2 locally is not "crippled model" — it is "model designed with this path in mind."

- **License is permissive where it matters, attributed where it scales.** Modified MIT: free commercial use, redistribution, derivative models, fine-tuning — all unrestricted below the 100M MAU / $20M revenue line. For the operator's ecosystem (research-wiki, AICP, OpenArms, OpenFleet, devops-control-plane) this is zero-friction. The attribution clause only binds at a scale this ecosystem is years away from. Practical equivalent of fully-open for the operator's purposes.

- **OpenRouter at $0.80 / $3.50 per M tokens is a strategic break from Anthropic-tier pricing.** Empirically verified 2026-04-22 via smoke test: Opus 4.6 through OpenRouter (Amazon Bedrock provider) runs at approximately **$5 per M input / $25 per M output**. K2.6 at $0.80/$3.50 is therefore **~6× cheaper on input, ~7× cheaper on output** (NOT the "~20×" that earlier estimates based on list-price Anthropic API suggested — OpenRouter's Opus pricing is already below Anthropic-direct). Still a ~6-7× compound reduction for an agentic workload dominated by output tokens — from "metered and tracked" down toward "background noise at operator's expected volume."

- **OpenRouter + CC-compatible env var turns K2.6 into a drop-in replacement right now.** Claude Code CLI honors `ANTHROPIC_BASE_URL` + `ANTHROPIC_API_KEY` env vars to route requests through OpenAI-compatible endpoints. OpenRouter exposes an OpenAI-compatible API. The operator can — before the subscription deadline — test K2.6 as the primary inference backend **with the same Claude Code harness**. Validates the "harness-neutral consumer contract" principle empirically.

- **256K context with MLA handles the wiki-scale workloads this second brain produces.** The wiki has 391 pages, hundreds of relationships, deep cross-refs. A 256K window can load the entire super-model + 50-100 page sub-selection + conversation history + tool outputs without chunking. For gap analysis, coherence review, or cross-layer synthesis (all operator-critical workloads), this removes the "stitch multiple calls together" tax.

- **Multimodal MoonViT is native, not a bolt-on.** 400M parameter vision encoder trained jointly, supports images + video. For the wiki's page structure (which is mostly text), this is currently a latent capability. For future extensions — screenshotting dashboards, ingesting diagrams from PDFs, reviewing UI mockups produced by agent workflows — the capability exists without reaching for a separate vision model.

- **Benchmark weaknesses are known and bounded.** K2.6 trails GPT-5.4 on pure-math reasoning (AIME 2026: 96.4 vs 99.2) and Gemini 3.1 Pro on multimodal understanding (MMMU-Pro: 79.4 vs 83.0) and Claude Opus 4.6 on some creative/writing tasks anecdotally. For operator's workloads (agentic coding, DevOps orchestration, wiki synthesis, decision reasoning), these weaknesses do not hit the critical path. For a researcher running physics/math-heavy workloads, they might.

- **Inference engines: vLLM, SGLang, KTransformers are the recommended stack.** KTransformers is the one that maps cleanly to operator's hardware — it's purpose-built for MoE models on hybrid CPU+GPU+disk setups. vLLM is production-serving scale (multi-GPU). SGLang is agent-workflow-optimized. For a single-node 19 GB VRAM + 64 GB RAM + RAID 0 NVMe, **KTransformers is the local deployment target**.

- **Deployment velocity matters: K2.6 is 2 days old at ingestion time.** The ecosystem (Unsloth GGUFs on HF, OpenRouter listing, llama.cpp support, community quantizations by ubergarm) is already present. Moonshot coordinates releases with the open-source inference stack. For the operator, this means "I want to try it today" is actually "I can try it today" — not "in 3-6 months."

## Deep Analysis

### How K2.6 compares to the other tiers in operator's 2026 stack

| Model | Params / Active | Local fit (19 GB VRAM + 64 GB RAM) | OpenRouter / API cost | Agentic capability |
|---|---|---|---|---|
| **Qwen3-8B (4-bit)** | 8B dense | ✅ VRAM native, fast | Free (local) | B — solid small-model |
| **gpt-oss-20b** | 21B / 3.6B active | ✅ VRAM native, 8K ctx | Free (local) | B+ — configurable reasoning |
| **gpt-oss-120b** | 117B / 5.1B active | ⚠️ disk-offload (MoE-aware) 2-3 tok/s | Free (local) / Groq-hosted | A — MoE-aware disk-offload tier |
| **Qwopus-27B v3** | 27B dense | ✅ VRAM tight (Q4) | Free (local) | A — Opus-4.6-distilled reasoning |
| **AirLLM + 70B** | 70B dense | ⚠️ disk-offload 0.18 tok/s batch | Free (local) | A — batch/offline only |
| **Kimi K2.6 Q2** | 1T / 32B active MoE | ⚠️ disk-offload 3-10 tok/s realistic | — | **S — agentic frontier** |
| **Kimi K2.6 (OpenRouter)** | 1T / 32B active MoE | — | $0.80/$3.50 per M | **S — agentic frontier, cheap** |
| **Claude Opus 4.6** | closed | — | $15/$75 per M (approx) | **S — but 20× cost** |

K2.6 on OpenRouter is **dominant on the Pareto frontier** (capability × cost) for operator's current agentic workloads. Locally, K2.6 Q2 is a *candidate for Tier 2* (disk-offload offline), alongside AirLLM+70B and gpt-oss-120b.

### Three access paths: OpenRouter vs Ollama Cloud vs Local KTransformers

Added 2026-04-23 after the Njenga Medium walkthrough surfaced **Ollama Cloud** as a third access path with a fundamentally different cost model (flat-rate, not per-token). Each of the three paths suits a different workload shape, privacy posture, and cost curve.

> [!abstract] K2.6 access paths — side by side
>
> | Dimension | OpenRouter | Ollama Cloud | Local KTransformers |
> |---|---|---|---|
> | **Model location** | Moonshot / provider-routed cloud | Ollama-hosted cloud | On-device (340 GB Q2 GGUF on `/mnt/models`) |
> | **Inference cost model** | Per-token: $0.80 / $3.50 per M in/out | Flat: $20/month (Pro) for all cloud models | $0/token (hardware + electricity) |
> | **Setup command** | `aicp --backend k2_6_openrouter ...` (already wired, E011 M002 done) | `ollama launch claude --model kimi-k2.6:cloud` | `python -m ktransformers.local_chat --model-path /mnt/models/kimi-k2-6-q2/...` (blocked on E008 M003 — dual-GPU optimization YAML) |
> | **Endpoint protocol** | OpenRouter → OpenAI-compatible (Anthropic-translated) | Anthropic-compatible at `localhost:11434` | KTransformers OpenAI-compatible server (planned) |
> | **Throughput / latency** | Depends on OpenRouter-routed provider (variance) | Ollama-managed (shared pool) | 3-10 tok/s realistic on 19 GB VRAM + 64 GB RAM |
> | **Provider transparency** | Per-request cost visibility; pick high-quality providers | Opaque — which Ollama host serves, what quantization | Full control; known quant (Q2 Unsloth) |
> | **Tool-use / agent-swarm API surface** | Whatever OpenRouter exposes from Moonshot — generally OK | Ollama's compatibility layer — unknown for 300-sub-agent swarm invocation | Full model capability (can configure directly) |
> | **Privacy posture** | Medium — routed through OpenRouter + provider | **Low** — author of the Medium article explicitly flags "prototyping only, not client work" | **High** — never leaves the machine |
> | **Best for** | Per-request billing, client work, quality-critical | Heavy prototyping, experimental, volume-unbounded | Offline, confidential, $0-target, long-horizon jobs where 3-10 tok/s is acceptable |

> [!tip] Cost-math: when does Ollama Cloud beat OpenRouter?
> OpenRouter is pay-as-you-go; Ollama Cloud Pro is $20/month flat. At K2.6's OpenRouter rates:
> - $20 ÷ $3.50/M output = **~5.7M output tokens/month** is the breakeven for output-heavy workloads
> - Mixed (30/70 in/out) workload: around the same range (input is much cheaper)
>
> A single heavy Claude-Code session produces ~200-500K output tokens. Monthly use across 20-30 sessions puts you at 5-15M output tokens — **Ollama Cloud is cheaper for heavy daily use**, OpenRouter is cheaper for light / per-project use.

> [!warning] Privacy asymmetry is NOT a cost question
> The Medium article's author explicitly divides work into "prototyping" vs "serious client/monetization" and places Ollama Cloud firmly in the prototyping bucket. For the operator's stack:
>
> - **Research wiki sessions** (public knowledge synthesis): Ollama Cloud safe
> - **AICP development** (AICP repo, operator's code, no client data): Ollama Cloud mostly safe
> - **OpenArms / client-connected work**: OpenRouter (with vetted provider) or Local only
> - **Any session touching `.env` / credentials / private infra**: Local only
>
> The `ollama launch` command makes it trivially easy to flip a project to cloud inference — which is ALSO what makes it easy to accidentally route sensitive context through a shared pool. An operator rule of thumb: default to OpenRouter for daily use, explicitly opt into Ollama Cloud per-session for prototyping workloads.

> [!info] Recommendation — revised tier stack with three K2.6 paths
>
> | Tier | Path | When to pick |
> |---|---|---|
> | 3a (cheap, online, quality) | OpenRouter → K2.6 | Default for daily agentic work; per-request cost visibility; client-adjacent tasks |
> | 3b (cheap, online, heavy volume) | Ollama Cloud → K2.6 | Experimental prototypes, volume-heavy iterations where >5M output tokens/month is likely |
> | 2 (free, offline, slow) | Local KTransformers → K2.6 Q2 | Confidential work, offline sessions, $0-target, willing to accept 3-10 tok/s |
>
> Not mutually exclusive — configure all three; route per session based on workload shape. The `ollama launch claude --model X` mechanism makes 3b a single-command flip without disturbing the other paths.

### How K2.6 reshapes the second-brain custom-model strategy

The wiki page [[second-brain-custom-model-strategy]] previously considered 5 candidates:
1. **Wiki-Assistant** (embedding+routing)
2. **Wiki-Reasoner** (LoRA on mid-model for structured reasoning)
3. **Wiki-Opus-Distilled** (distilled from Opus for style)
4. **Wiki-Router** (small routing layer)
5. **Base + Multi-LoRA** (modular adapters on a single base)

**K2.6 via OpenRouter largely obsoletes candidates 2 and 3** — training a Wiki-Reasoner or Wiki-Opus-Distilled to match K2.6's agentic/coding capability is a multi-month project that would deliver strictly worse results than the $0.80/$3.50 API call. **Candidates 1, 4, 5 remain valid** — they are about *routing and adaptation to the wiki's domain*, not raw capability. The custom-model strategy should refocus on: *use K2.6 for capability, use local custom-trained small models for privacy, routing, and personalization.*

### How K2.6 reshapes the 5-day self-autonomous workstation plan

Revised tier stack (post-K2.6):

```
Tier 1 (free, offline, fast)      : Qwen3-8B (VRAM) + gpt-oss-20b (VRAM)
Tier 2 (free, offline, slow-ish)  : K2.6 Q2 via KTransformers on NVMe+swap
                                     OR gpt-oss-120b (MoE-aware disk-offload)
                                     OR AirLLM+70B (batch only)
Tier 3 (cheap, online, frontier)  : OpenRouter → K2.6 PRIMARY
                                     + Claude/GPT/Gemini as fallback
Tier 4 (premium, rare)            : Direct Anthropic/OpenAI/Moonshot APIs
```

5-day plan impact:
- **Day 1-2**: OpenRouter account + key; test K2.6 via `ANTHROPIC_BASE_URL` env var from Claude Code CLI. De-risks the subscription deadline before day 5.
- **Day 2-3**: 64 GB RAM install; KTransformers setup; download K2.6 Q2 GGUF (~340 GB — fits on 1 TB NVMe easily). Benchmark local tok/s.
- **Day 3-4**: Harness port (whatever replacement or continue CC via OpenRouter); wire skills/hooks; MCP continuity check.
- **Day 5**: Hardening, session POC, harness-contract doc updated with K2.6 as primary.

## Risks and Open Questions

- [ ] **Provider quality variance on OpenRouter.** OpenRouter routes across multiple providers. Some providers may throttle, quantize aggressively, or have lower uptime than Moonshot-direct. Need to observe behavior at operator workload scale; may want to pin to a specific high-quality provider via OpenRouter's provider-routing options.
- [ ] **Tool-use format compatibility with Claude Code.** CC's tool-call schema is Anthropic-style (XML/JSON hybrid). OpenRouter exposes OpenAI-style function calling. Translation layer behavior TBD — likely works out-of-the-box via OpenRouter's cross-provider translation, but an integration test on day 1 is essential.
- [ ] **KTransformers MoE disk-offload real tok/s on 64 GB RAM.** Published benchmarks assume specific hardware (often datacenter NVMe or dual-CPU). Operator's RAID 0 NVMe will likely exceed published numbers for sequential reads but the realistic tok/s needs measurement, not guessing.
- [ ] **Agent swarm API access pattern.** K2.6's 300-sub-agent orchestration is a model-native capability — how is it invoked? Is it a special parameter (`num_agents`) or does the model self-orchestrate given a task? OpenRouter documentation is incomplete on this; direct Moonshot API + Agent Platform may be required to access the full swarm capability.
- [ ] **License attribution at scale.** Not an operator-scale concern today, but if K2.6 ends up powering a product that scales above 100M MAU or $20M monthly revenue, the attribution requirement is a UX design consideration — flag it early.

## Cross-References

- [[src-airllm-layer-wise-inference-nvme-ssd-offload|AirLLM]] — same disk-offload paradigm, model-agnostic wrapper; K2.6 fits the tier AirLLM established
- [[src-gpt-oss-openai-open-weight-moe|gpt-oss]] — same MoE + open-weight family; K2.6 is larger (1T vs 117B) and newer (2026-04 vs 2025-08)
- [[src-turboquant-122b-macbook|TurboQuant]] — Apple Silicon parallel, different hardware target
- [[src-unsloth-fast-lora-consumer-hardware|Unsloth]] — same Unsloth team publishing K2.6 GGUFs; fine-tuning path available
- [[src-qwopus-claude-opus-reasoning-distilled-qwen-27b|Qwopus]] — smaller distilled alternative for Opus-style reasoning
- [[open-model-evaluation-framework|Open-Model Evaluation Framework]] — the 5-stage decision process applied here
- [[2026-consumer-hardware-ai-stack|2026 Consumer-Hardware AI Stack]] — updated Tier 3 with K2.6 primary
- [[second-brain-custom-model-strategy|Second-Brain Custom Model Strategy]] — capability candidates refocused given K2.6
- [[model-local-ai|Model — Local AI]] — routing tiers updated with K2.6 in premium/routing tier

## State of Knowledge

| Claim | Verified? | Evidence |
|---|---|---|
| K2.6 released 2026-04-20 | ✅ | MarkTechPost, SiliconANGLE dated 2026-04-20 |
| 1T total / 32B active MoE, 384 experts, 61 layers, MLA | ✅ | SiliconANGLE primary; K2.6 shares K2 architecture |
| 256K context | ✅ | OpenRouter lists 262,144; blog references 256K |
| Modified MIT license | ✅ | The Decoder + MarkTechPost primary |
| 54.0 HLE-Full w/ tools (LEADS) | ✅ | BuildFastWithAI primary; The Decoder confirms |
| 58.6 SWE-Bench Pro (LEADS GPT-5.4) | ✅ | BuildFastWithAI primary; Moonshot blog confirms |
| OpenRouter $0.80 / $3.50 per M tokens | ✅ | OpenRouter page direct fetch |
| Q2 GGUF 340 GB, Q4 584 GB, Q8 595 GB | ✅ | Unsloth HF primary |
| Agent Swarm 300 sub-agents, 4,000 steps | ✅ | Moonshot blog + MarkTechPost primary |
| Native INT4 via QAT | ✅ | Unsloth + community quantization pages |
| Claude Code CLI routes via ANTHROPIC_BASE_URL | ⚠️ Untested | Known CC env-var; **needs operator-workload verification before trusted** |
| K2.6 via OpenRouter tool-use compatibility with CC | ⚠️ Untested | **Needs day-1 integration test** |
| KTransformers K2.6 Q2 tok/s on 19 GB VRAM + 64 GB RAM | ⚠️ Untested | **Needs local benchmark once 64 GB RAM lands** |
| K2.6 quality parity on operator's actual workloads vs Opus 4.6 | ⚠️ Benchmark-only | **Needs production-workload A/B test** |

## Next Steps

1. **Update dependent pages**: [[model-local-ai]] (Tier 3 addition), [[2026-consumer-hardware-ai-stack]] (K2.6 primary at premium tier), [[second-brain-custom-model-strategy]] (candidates 2+3 reassessed).
2. **Day-1 POC**: Configure Claude Code CLI → OpenRouter → K2.6 route via env vars; run a wiki-typical workload (cross-ref check, scaffold a page, validate lint); compare latency, quality, and tool-use fidelity vs current Claude route.
3. **Day-2/3 local setup**: Once 64 GB RAM installed, download K2.6 Q2 GGUF via Unsloth HF; stand up KTransformers; measure real tok/s; document.
4. **Update 5-day self-autonomous workstation plan** to reflect K2.6 as Tier-3 primary and Tier-2 local candidate; revise task sequencing.
5. **Follow-up research directive (pending)**: Moonshot Agent Platform — how is the 300-sub-agent swarm invoked programmatically? Is it OpenRouter-accessible or Moonshot-direct only?

## Relationships

- BUILDS ON: [[src-airllm-layer-wise-inference-nvme-ssd-offload|Synthesis — AirLLM]] — same disk-offload paradigm; K2.6 is a new candidate for the local-batch-frontier tier AirLLM established
- BUILDS ON: [[src-gpt-oss-openai-open-weight-moe|Synthesis — gpt-oss]] — same open-weight MoE family; K2.6 is larger and agentically stronger
- BUILDS ON: [[open-model-evaluation-framework|Open-Model Evaluation Framework]] — the 5-stage process applied here, worked-example form
- FEEDS INTO: [[model-local-ai|Model — Local AI ($0 Target)]] — adds premium-cheap-online and local-batch-frontier tiers
- FEEDS INTO: [[2026-consumer-hardware-ai-stack|2026 Consumer-Hardware AI Stack]] — adds a fifth layer (premium/routing) to the four-layer picture
- FEEDS INTO: [[second-brain-custom-model-strategy|Second-Brain Custom Model Strategy]] — reshapes candidates B and C capability budget
- RELATES TO: [[src-qwopus-claude-opus-reasoning-distilled-qwen-27b|Synthesis — Qwopus]] — smaller Opus-distilled alternative for Opus-style reasoning at a different scale
- RELATES TO: [[src-unsloth-fast-lora-consumer-hardware|Synthesis — Unsloth]] — same Unsloth team publishes K2.6 GGUFs; fine-tuning path available
- RELATES TO: [[src-turboquant-122b-macbook|Synthesis — TurboQuant]] — Apple Silicon parallel deployment strategy
- DEMONSTRATES: [[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4 — Declarations Aspirational Until Verified]] — benchmark claims verified via primary sources; operator-workload validation flagged as pending

## Backlinks

[[Synthesis — AirLLM]]
[[Synthesis — gpt-oss]]
[[open-model-evaluation-framework|Open-Model Evaluation Framework]]
[[model-local-ai|Model — Local AI ($0 Target)]]
[[2026 Consumer-Hardware AI Stack]]
[[second-brain-custom-model-strategy|Second-Brain Custom Model Strategy]]
[[Synthesis — Qwopus]]
[[Synthesis — Unsloth]]
[[Synthesis — TurboQuant]]
[[Principle 4 — Declarations Aspirational Until Verified]]
[[kimi-k2-6-access-paths-openrouter-ollama-cloud-local|Kimi K2.6 Access Paths — OpenRouter vs Ollama Cloud vs Local KTransformers]]
