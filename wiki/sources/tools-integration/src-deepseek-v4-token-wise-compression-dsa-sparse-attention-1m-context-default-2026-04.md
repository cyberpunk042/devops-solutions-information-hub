---
title: "Synthesis — DeepSeek V4 (Apr 2026): Token-Wise Compression + DSA (DeepSeek Sparse Attention) Delivers 1M Context as Default at 27% FLOPs / 10% KV Cache vs V3.2"
aliases:
  - "DeepSeek V4 Synthesis"
  - "DSA DeepSeek Sparse Attention"
  - "1M Context as Default"
  - "DeepSeek V4 Hybrid Attention"
type: source-synthesis
domain: tools-integration
status: synthesized
confidence: high
maturity: seed
layer: 1
created: 2026-05-06
updated: 2026-05-06
last_reviewed: 2026-05-06
sources:
  - id: deepseek-v4-announcement
    type: documentation
    url: https://api-docs.deepseek.com/news/news260424
    file: raw/articles/httpsapi-docsdeepseekcomnewsnews260424.md
    description: "DeepSeek's official 2026-04-24 announcement of V4 Preview — V4-Pro 1.6T total / 49B active + V4-Flash 284B total / 13B active; 1M context default; token-wise compression + DSA novel attention; integrated in Claude Code + OpenClaw + OpenCode"
  - id: deepseek-v4-tech-report
    type: documentation
    url: https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro/blob/main/DeepSeek_V4.pdf
    description: "DeepSeek-V4 full technical report — 'DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence' — comprehensive academic document covering architecture, training methodology, evaluation"
  - id: deepseek-v4-hf-collection
    type: documentation
    url: https://huggingface.co/collections/deepseek-ai/deepseek-v4
    description: "Open-weight DeepSeek V4 collection — V4-Pro and V4-Flash weights"
  - id: andrew-lukyanenko-review
    type: article
    url: https://artgor.medium.com/deepseek-v4-review-why-million-token-context-needs-efficient-attention-not-just-larger-windows-6dc8e74a00b1
    description: "Andrew Lukyanenko Medium review — explains DSA mechanism in detail; CSA (4:1 KV cache compression + top-512 sparse attention) + HCA (128:1 compression with dense attention over compressed sequence)"
  - id: byteiota-1m-context-coverage
    type: article
    url: https://byteiota.com/deepseek-v4-1m-token-context-at-90-less-memory/
    description: "byteiota industry coverage — 1M context at 90% less memory framing; 9.62 GiB KV cache per sequence at 1M context vs estimated 83.9 GiB V3.2-style stack"
  - id: trust-layer-concept
    type: wiki
    file: wiki/domains/cross-domain/secure-tamper-proof-model-on-shared-gpu-research-synthesis.md
    description: "Trust-Layer Concept — operator's compression-theme mission framing; DSA at the KV-cache + attention layer adds another 6th-layer mechanism"
  - id: compression-lesson
    type: wiki
    file: wiki/lessons/01_drafts/end-to-end-compression-across-the-ai-stack-composes-multiplicatively-6-plus-independent-mechanisms-at-6-distinct-layers.md
    description: "Multi-Layer Compression Lesson — DSA is the 7th independent mechanism convergence at the KV-cache+attention layer"
  - id: anti-vendor-lock-in-lesson
    type: wiki
    file: wiki/lessons/01_drafts/anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence.md
    description: "Anti-Vendor-Lock-In Lesson — DeepSeek V4 is one substitutable axis at the model-customization layer (alongside Qwen3.6-27B, RLM-Qwen3-8B, Llama 3 etc); 1M context as default extends operator's options"
tags: [synthesis, deepseek, deepseek-v4, dsa, deepseek-sparse-attention, csa, hca, compressed-sparse-attention, heavily-compressed-attention, 1m-context, kv-cache-compression, mhc, manifold-constrained-hyper-connections, muon-optimizer, agentic-coding, claude-code-integration, open-weight, open-source, mission-2026-05-06]
---

# Synthesis — DeepSeek V4 (Apr 2026)

## Summary

DeepSeek released **V4 Preview on 2026-04-24** with two open-weight variants: **V4-Pro (1.6T total / 49B active params)** rivaling top closed-source models on agentic coding benchmarks, and **V4-Flash (284B total / 13B active params)** as the fast/economical option. The structural innovation is **token-wise compression + DSA (DeepSeek Sparse Attention)** — a hybrid attention architecture combining **CSA (Compressed Sparse Attention, 4:1 KV cache compression + sparse attention over top-512 selected entries)** and **HCA (Heavily Compressed Attention, 128:1 compression with dense attention over the aggressively compressed sequence)**. **Empirical efficiency at 1M context: 27% of single-token inference FLOPs and 10% of KV cache vs DeepSeek-V3.2** — concretely, **9.62 GiB KV cache per sequence at 1M context** versus an estimated 83.9 GiB for a 61-layer V3.2-style stack. **1M context is now the default across all official DeepSeek services** — the model is purpose-built for million-token-class workloads. Additional architectural innovations: **mHC (Manifold-Constrained Hyper-Connections)** strengthens conventional residual connections for stable signal propagation across layers; the **Muon optimizer** delivers faster convergence and greater training stability. Already integrated in **Claude Code, OpenClaw, and OpenCode** per DeepSeek's own announcement. Both models support 1M context + dual modes (Thinking / Non-Thinking) via the same OpenAI ChatCompletions + Anthropic API surface (just change `model` parameter to `deepseek-v4-pro` or `deepseek-v4-flash`). **Mission relevance**: (1) DSA is the **7th independent mechanism** in the operator's [Multi-Layer Compression Convergence Lesson](../../lessons/01_drafts/end-to-end-compression-across-the-ai-stack-composes-multiplicatively-6-plus-independent-mechanisms-at-6-distinct-layers.md) at the **KV-cache + attention layer** — joins KV-cache asymmetric quantization + Qwen-Scope SAE + sliding-window attention as substitutable axes within Layer 6; (2) 1M-context-as-default extends the operator's [Custom-Tailored Senior-Engineer-Tier Model Group](../../domains/cross-domain/custom-tailored-senior-engineer-tier-model-group-with-recreated-intelligence-layer-research-synthesis.md) base-model choice set with a frontier-class open-weight long-context option; (3) integration with Claude Code + OpenClaw + OpenCode means the operator's existing harness layer can route to V4-Flash/Pro via API endpoint change with no other config; (4) [Karen's earlier video reference](src-subquadratic-subq-12m-context-sparse-attention-and-anythingllm-breakthrough-leads.md) to "DeepSeek v4 hybrid attention" is empirically anchored — the lead is paper-grade real (vs SubQ's claimed-but-unverified 12M context which lacks technical report).

## Reference

> [!info] Source identity
>
> | Field | Value |
> |---|---|
> | **Release** | DeepSeek V4 Preview (2026-04-24) |
> | **Variants** | V4-Pro (1.6T total / 49B active) · V4-Flash (284B total / 13B active) |
> | **Tech report** | huggingface.co/deepseek-ai/DeepSeek-V4-Pro/blob/main/DeepSeek_V4.pdf — *"DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence"* |
> | **Open weights** | Available on HuggingFace |
> | **Default context** | 1M tokens (across all official DeepSeek services) |
> | **API compatibility** | OpenAI ChatCompletions + Anthropic API |
> | **Integration in operator's stack** | Claude Code · OpenClaw · OpenCode (per DeepSeek's announcement) |
> | **Migration path** | Same `base_url`, just update `model` to `deepseek-v4-pro` or `deepseek-v4-flash` |
> | **Sunset** | `deepseek-chat` and `deepseek-reasoner` retire 2026-07-24 (currently route to V4-Flash) |

## Key Insights

> [!success] **DSA (DeepSeek Sparse Attention) is the 7th independent mechanism in the operator's compression-layer convergence — at the KV-cache + attention layer.**
>
> Per the [Multi-Layer Compression Convergence Lesson](../../lessons/01_drafts/end-to-end-compression-across-the-ai-stack-composes-multiplicatively-6-plus-independent-mechanisms-at-6-distinct-layers.md), Layer 6 (KV-cache + internal representation) substitutable axes were: KV-cache asymmetric quantization (50-87%) · Qwen-Scope SAE sparse-feature representation (top-k of 16×–64× hidden size) · attention sparsity · sliding-window attention. **DSA adds two more sub-mechanisms**:
>
> | Sub-mechanism | Mechanism detail | Compression |
> |---|---|---|
> | **CSA (Compressed Sparse Attention)** | 4:1 KV cache compression + sparse attention over top-512 selected entries | 4× KV cache reduction + sparsity savings |
> | **HCA (Heavily Compressed Attention)** | 128:1 KV cache compression + dense attention over the aggressively compressed sequence | KV cache reduced to <1% of original size |
>
> Combined effect at 1M context: **27% of V3.2's FLOPs and 10% of V3.2's KV cache** — concretely, 9.62 GiB KV cache per sequence at 1M (vs estimated 83.9 GiB V3.2-style). **The compression compounds with the operator's existing layers** (e.g., V4 + UD-IQ2 weight quantization + Caveman prompt compression + Cloudflare Markdown for Agents at the source).

> [!success] **1M context as the default — operator's [Custom-Tailored Model Group](../../domains/cross-domain/custom-tailored-senior-engineer-tier-model-group-with-recreated-intelligence-layer-research-synthesis.md) base-model choice set gains a frontier-class long-context open-weight option.**
>
> Per DeepSeek announcement: *"1M Standard: 1M context is now the default across all official DeepSeek services."* This is structural — not a premium tier or paid upgrade, but the **base offering**. Combined with V4's open-weight release, operator can self-host V4-Flash for 1M-context workloads on H100-class hardware. M002 of the operator's Custom-Model Epic (First Specialist LoRA + Group Expansion) gains DeepSeek V4-Flash as a candidate base alongside Qwen3.6-27B, RLM-Qwen3-8B, Qwen3-Coder, Llama 3, Mistral.

> [!success] **Open-source SOTA on Agentic Coding benchmarks — DeepSeek's own claim, paper-citable.**
>
> Per DeepSeek announcement V4-Pro: *"Enhanced Agentic Capabilities: Open-source SOTA in Agentic Coding benchmarks. Rich World Knowledge: Leads all current open models, trailing only Gemini-3.1-Pro. World-Class Reasoning: Beats all current open models in Math/STEM/Coding, rivaling top closed-source models."* This positions V4-Pro as a candidate substitute for Anthropic Opus-class workloads in the operator's anti-vendor-lock-in mission. V4-Flash performs *"on par with V4-Pro on simple Agent tasks"* with smaller param size + faster response + cost-effective API.

> [!success] **Already integrated in operator's harness layer (Claude Code + OpenClaw + OpenCode) — zero migration cost.**
>
> Per DeepSeek announcement: *"DeepSeek-V4 is seamlessly integrated with leading AI agents like Claude Code, OpenClaw & OpenCode."* The operator's existing harness setup (Claude Code default + OpenCode activated 2026-04-23) can route to V4 by changing the `model` parameter. **This is anti-vendor-lock-in operationalized at the harness × provider intersection** — same harness, same API, different provider, frontier-class capability.

> [!success] **mHC + Muon optimizer = stability innovations beyond DSA.**
>
> Per Andrew Lukyanenko's review: **mHC (Manifold-Constrained Hyper-Connections)** strengthens conventional residual connections for stable signal propagation across layers while preserving model expressivity. **Muon optimizer** delivers faster convergence and greater training stability than Adam-class optimizers. These are training-time innovations that affect inference-time quality. **Mission relevance**: operator's M004 (behavioral preference fine-tune) on V4-Flash base would inherit Muon's stability advantages.

> [!info] **The Karen-video reference is now empirically anchored — DeepSeek V4 is paper-grade real.**
>
> Per the operator's [SubQuadratic + AnythingLLM tracked-leads synthesis](src-subquadratic-subq-12m-context-sparse-attention-and-anythingllm-breakthrough-leads.md), Timothy Karen mentioned *"DeepS v4 came out with this hybrid attention mechanism"* on 2026-05-04. **This synthesis confirms that lead at HIGH confidence**: technical report, open weights, vendor-published benchmarks, multi-vendor harness integration. Substantively distinct from the SubQ low-confidence claim (which lacked any of those).

## Deep Analysis

### DSA Architecture (Compressed Sparse + Heavily Compressed)

```
                  ┌───── Token-wise compression ─────┐
                  │                                    │
                  ▼                                    ▼
       CSA (Compressed Sparse Attention)    HCA (Heavily Compressed Attention)
       ─────────────────────────────────    ──────────────────────────────────
       1. 4:1 KV cache compression          1. 128:1 KV cache compression
       2. Sparse attention over top-512        (KV cache → <1% of original)
          selected entries                  2. Dense attention over the
                                                aggressively compressed seq
       
       Use case: medium-context queries     Use case: extremely long context
       requiring keyword precision          where global semantic capture matters
```

The hybrid is the load-bearing innovation: CSA preserves precision for short-range contexts; HCA enables global reasoning over million-token sequences without runaway memory cost. **Combined at 1M context: 27% of V3.2's FLOPs + 10% of V3.2's KV cache.**

### Connection to Operator's Compression-Theme Mission

| Compression layer | Existing mechanisms | NEW from V4 |
|---|---|---|
| Layer 6 (KV-cache + internal representation) | KV-cache asymmetric quantization (50-87%) · Qwen-Scope SAE · attention sparsity · sliding-window attention | **DSA (CSA + HCA): 4:1 + 128:1 KV cache compression with hybrid sparse/dense attention** |
| Inference paradigm (cross-cutting) | RLM (recursive language models, 2-orders-of-magnitude effective context) | **1M-context-as-default — structural compression of the long-context decision** |

**End-to-end stack at 1M context with operator's full composition**:
- Cloudflare Markdown for Agents at source (80% reduction)
- Caveman Wenyan-Full prompt compression (80-90%)
- Strands intent-based tool design (96% on tool I/O)
- DeepSeek V4-Flash base via Multica → Claude Code (operator's harness)
- DSA at the attention layer (27% FLOPs, 10% KV cache vs V3.2)
- Operator's L2 trust opt-ins (compressed-encrypted weights via Triton)
- RecursiveMAS cross-agent latent transfer (34.6-75.6%)

**Multiplicative composition holds**: the 80-90% combined-envelope claim from the [Trust-Layer Concept](../../domains/cross-domain/secure-tamper-proof-model-on-shared-gpu-research-synthesis.md) is even more empirically defensible after V4. Each layer's compression compounds.

### Connection to Custom-Model Epic M002 (Base Model Choice)

| Candidate base | Strengths | Operator-relevance |
|---|---|---|
| Qwen3.6-27B | Senior-engineer-tier on agentic coding (per Anti-Vendor-Lock-In Evidence 1) | UD-IQ2 fits 24 GB VRAM |
| RLM-Qwen3-8B | RLM-paradigm-aware; 48 H100-hour post-train precedent | Smaller; recursive scaling-friendly |
| Qwen3-Coder family | Purpose-built for coding | Coding-tier specialist baseline |
| **DeepSeek V4-Flash (284B / 13B active)** | 1M context default; DSA hybrid attention; SOTA agentic coding | **Larger; needs H100-class hardware OR Q4_K_M for consumer; long-context-tier specialist** |
| **DeepSeek V4-Pro (1.6T / 49B active)** | Top-tier reasoning; rivals closed-source; 1M context | **Cloud-rental tier; RTX 3090 not sufficient; H100/H200 territory** |
| Llama 3 / Mistral | Mature ecosystem; many fine-tunes | Wide tooling support |

V4-Flash at 13B active params is operator-substantive (smaller than Qwen3-27B but with 1M-context superpower); V4-Pro at 49B active is cloud-rental tier. **Operator-decision in M002**: when 1M-context capability is mission-relevant for a specific specialist LoRA, V4-Flash becomes the candidate base.

### Connection to Anti-Vendor-Lock-In Lesson

Per [Anti-Vendor-Lock-In Lesson](../../lessons/01_drafts/anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence.md): every stack layer needs substitutable axes with paper evidence. DeepSeek V4 adds:

| Layer | New substitutability axis from V4 |
|---|---|
| Provider × Model | Open-weight V4-Flash / V4-Pro adds frontier-class long-context option to existing K2.6 / Qwen3.6-27B / RLM-Qwen3-8B set |
| Model-customization (candidate Layer 5) | DeepSeek V4 base + LoRA fine-tune is operator-feasible (V4-Flash) or cloud-rental (V4-Pro) |
| Compression (cross-cutting) | DSA hybrid attention adds another substitutable mechanism at Layer 6 (KV-cache + attention) |
| Inference paradigm | 1M-context-as-default reduces dependence on context-window-extending paradigms (RLM, retrieval) for many workloads |

## Quotes (verbatim from DeepSeek announcement)

> *"Welcome to the era of cost-effective 1M context length."*

> *"Novel Attention: Token-wise compression + DSA (DeepSeek Sparse Attention)."*

> *"Peak Efficiency: World-leading long context with drastically reduced compute & memory costs."*

> *"DeepSeek-V4 is seamlessly integrated with leading AI agents like Claude Code, OpenClaw & OpenCode."*

> *"Already driving our in-house agentic coding at DeepSeek."*

## Open Questions

> [!question] V4-Flash on RTX 3090 — feasible at Q4 quantization?
> 13B active params at Q4_K_M ≈ 7.3 GB; routing weights in MoE add overhead but should fit 24 GB VRAM. Empirical sizing needed. Operator-validation candidate post-3090 delivery.

> [!question] V4-Pro on cloud H100 rental for operator's M005 (L3 additive trust path)?
> 49B active params would benefit from H100-class hardware; cost ~$3-10/hour cloud rental per the [Trust-Layer Epic](../../backlog/epics/pre-milestone/secure-tamper-proof-inference-pipeline-cypher-decypher-compression-2026-04.md) framing. Operator-decision per workload class.

> [!question] DSA composition with operator's L2 trust + Triton on-GPU decypher kernels — interaction risks?
> DSA's CSA + HCA operate on KV cache; operator's L2 cypher operates on weights at rest + KV cache compressed-encrypted form. The two should compose (cypher applied to compressed-DSA form), but empirical validation post-3090 needed.

> [!question] Should V4-Flash become the default routing-tier for 1M-context workloads in operator's AICP setup?
> AICP routes by complexity tier; DeepSeek V4-Flash at 1M context is a candidate routing target for `long-context-heavy` workloads. Operator-decision per AICP routing config.

> [!question] DeepSeek V4 vs Kimi K2.6 (operator's existing primary) — which dominates which workload?
> [Kimi K2.6 synthesis](src-kimi-k2-6-moonshot-agent-swarm.md) dominates agentic coding at $0.80/$3.50 per million tokens. V4-Flash adds 1M-context specialty. Tier-0 candidate comparison with V4 is the empirical next step. Operator-decision pending workload-class routing strategy.

## Relationships

- BUILDS ON: [[end-to-end-compression-across-the-ai-stack-composes-multiplicatively-6-plus-independent-mechanisms-at-6-distinct-layers|Multi-Layer Compression Lesson]] — DSA is the 7th independent mechanism at Layer 6
- BUILDS ON: [[anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence|Anti-Vendor-Lock-In Lesson]] — adds substitutability axes at provider, model-customization, and compression layers
- BUILDS ON: [[custom-tailored-senior-engineer-tier-model-group-with-recreated-intelligence-layer-research-synthesis|Custom-Tailored Model Group Concept]] — V4-Flash candidate base for M002 long-context specialist
- BUILDS ON: [[secure-tamper-proof-model-on-shared-gpu-research-synthesis|Trust-Layer Concept]] — DSA composes with L2 cypher overlay; further empirical evidence for the 80-90% combined-envelope claim
- RELATES TO: [[src-rlm-recursive-language-models-mit-oasys|RLM Synthesis]] — RLM provides 2-orders-of-magnitude effective context expansion via recursion; V4 provides 1M-context-as-default via attention compression; complementary at the inference paradigm + attention layer
- RELATES TO: [[src-qwen-scope-sparse-autoencoders-llm-interpretability-suite|Qwen-Scope Synthesis]] — both compress at internal representation; SAE for interpretability + DSA for inference efficiency
- RELATES TO: [[src-subquadratic-subq-12m-context-sparse-attention-and-anythingllm-breakthrough-leads|SubQuadratic + AnythingLLM Synthesis]] — Karen's video reference to DeepSeek v4 hybrid attention is now paper-grade anchored
- RELATES TO: [[src-kimi-k2-6-moonshot-agent-swarm|Kimi K2.6 Synthesis]] — adjacent open-weight provider tier; comparison candidate for operator's routing
- RELATES TO: [[src-cloudflare-markdown-for-agents-content-negotiation-80-percent-token-reduction-2026-02|Cloudflare Markdown for Agents Synthesis]] — content-source compression composes with V4's DSA at inference
- DEMONSTRATES: [[infrastructure-over-instructions-for-process-enforcement|Principle 1 — Infrastructure Over Instructions]] — DSA is architecture-level infrastructure (built into the model); cannot be added as prompt instruction
- DEMONSTRATES: [[goldilocks-protocol|Goldilocks Protocol]] — V4-Pro for top-tier reasoning, V4-Flash for cost-effective; operator picks per workload class

## Backlinks

[[Multi-Layer Compression Lesson]]
[[Anti-Vendor-Lock-In Lesson]]
[[custom-tailored-senior-engineer-tier-model-group-with-recreated-intelligence-layer-research-synthesis|Custom-Tailored Model Group Concept]]
[[Trust-Layer Concept]]
[[RLM Synthesis]]
[[src-qwen-scope-sparse-autoencoders-llm-interpretability-suite|Qwen-Scope Synthesis]]
[[SubQuadratic + AnythingLLM Synthesis]]
[[Kimi K2.6 Synthesis]]
[[src-cloudflare-markdown-for-agents-content-negotiation-80-percent-token-reduction-2026-02|Cloudflare Markdown for Agents Synthesis]]
[[infrastructure-over-instructions-for-process-enforcement|Principle 1 — Infrastructure Over Instructions]]
[[Goldilocks Protocol]]
