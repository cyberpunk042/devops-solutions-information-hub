---
title: Local LLM Quantization
aliases:
  - "Local LLM Quantization"
type: concept
layer: 2
maturity: growing
domain: ai-models
status: synthesized
confidence: medium
created: 2026-04-08
updated: 2026-04-10
sources:
  - id: src-turboquant-122b-macbook
    type: article
    url: https://medium.com/data-science-collective/how-i-run-122b-parameter-llms-on-a-macbook-outperforming-mxfp4-and-standard-quantization-on-apple-0552ee3da1f7
    file: raw/articles/turboquant-122b-llm-macbook-mlx.md
    title: How I Run 122B Parameter LLMs on a MacBook
    ingested: 2026-04-08
  - id: src-gemma4-searxng-openclaw
    type: youtube-transcript
    url: https://www.youtube.com/watch?v=T0CKsU0hQx4
    file: raw/transcripts/gemma-4-searxng-100-free-amp-private-openclaw-full-setup.txt
    title: Gemma 4 + SearXNG for OpenClaw
    ingested: 2026-04-08
tags: [quantization, local-llm, mlx, ollama, apple-silicon, moe, turboquant, gemma4, consumer-hardware, local-first]
---

# Local LLM Quantization

## Summary

Local LLM quantization enables running large language models (up to 122B parameters) on consumer hardware like MacBooks by reducing precision from full floating-point to lower bit-widths. Two approaches dominate: TurboQuant-MLX achieves 44 tok/s for 122B MoE models on M4 Max (64GB RAM), outperforming Apple's native MXFP4 format. Ollama provides a simpler path, packaging quantized models (GGUF format) for one-command download and native integration with AI agent frameworks like OpenClaw. The Gemma 4 family demonstrates that even 7GB models (E2B) can reliably handle multi-step agentic tool calling — a capability that previously required much larger models.

## Key Insights

- **Consumer hardware runs 122B models**: MacBook M4 Max (64GB) runs 122B MoE at 44 tok/s via TurboQuant-MLX. MacBook Pro (24GB) comfortably runs Gemma 4 26B (18GB model file). Even 16GB MacBooks can run Gemma 4 E2B (7GB).

- **MoE architecture enables local large models**: Mixture-of-Experts only activates a subset of parameters per token. A 122B MoE model might only use 13B active parameters per forward pass, making it memory-feasible on consumer hardware despite the large total size.

- **TurboQuant > MXFP4 > standard quantization**: Model-aware quantization (adapted per architecture) outperforms hardware-native formats (Apple's MXFP4) and generic affine quantization. This suggests quantization should be tailored to model structure, not just hardware.

- **Ollama as model distribution**: `ollama pull gemma4:e2b` downloads, quantizes, and serves models with a single command. `ollama list` manages local model inventory. Native integrations with OpenClaw, Open WebUI, and other frameworks eliminate configuration.

> [!success] Small Model Capability Breakthrough
> Gemma 4 E4B (9.6GB, designed for phones) reliably executes multi-step agentic tasks: web search, summarize, create report, send email. This was previously unreliable with small models, representing a fundamental shift in what consumer hardware can do.

- **Small models now do tool calling**: Gemma 4 E4B (9.6GB, designed for phones) reliably executes multi-step agentic tasks: web search → summarize → create report → send email. This was previously unreliable with small models, representing a capability breakthrough.

- **Two quantization paths**: (1) MLX/TurboQuant for maximum performance on Apple Silicon (research-grade, manual setup), (2) Ollama/GGUF for maximum convenience across platforms (one-command, auto-quantized). AICP's model evaluation pipeline tests both paths.

## Deep Analysis

### Implications for the Ecosystem

The local LLM quantization landscape directly affects three ecosystem projects:

**AICP (AI Control Platform):** The 5-stage LocalAI independence roadmap (target: 80% Claude token reduction) becomes more achievable as consumer hardware capabilities grow. AICP already evaluates Qwen3 and Gemma4 models — adding TurboQuant-MLX for MoE models could unlock 122B-class reasoning locally. The backend router can factor quantization performance into its complexity-based routing decisions.

**OpenFleet:** Fleet agents running on LocalAI currently use hermes-3b for queries and bge-m3 for embeddings. If Gemma 4 26B runs comfortably on 24GB hardware with reliable tool calling, it could replace hermes for agent inference — better reasoning at negligible cost. The silent heartbeat optimization (70% cost savings) becomes even more effective when the baseline cost is already zero (local inference).

**Research Wiki:** For the pipeline automation vision, local inference means research operations (web search, summarization, cross-referencing) can run without API calls. A local model could power automated gap analysis and relationship discovery in the pipeline.

## Open Questions

- What is the quality degradation of TurboQuant at 2-bit vs 4-bit vs 8-bit for reasoning tasks specifically? (Requires: empirical benchmarking of TurboQuant-MLX at each bit-width on reasoning tasks such as MMLU, HumanEval, or GSM8K; no existing wiki page documents bit-width-specific quality curves for TurboQuant)
- Can TurboQuant-MLX be integrated with Ollama for best-of-both-worlds (Ollama distribution + TurboQuant quantization)? (Requires: external research on whether TurboQuant-MLX outputs can be converted to GGUF format for Ollama distribution; not covered in existing wiki pages)

### Answered Open Questions

**Q: How does Gemma 4 26B's tool calling reliability compare to Claude Sonnet for OpenFleet agent tasks?**

Cross-referencing `AICP` and `OpenFleet`: the question can be partially answered from the ecosystem's current routing architecture and AICP's documented model evaluation strategy. The `AICP` page documents that 9 models are loaded — including the full Gemma4 family (e2b, e4b, 26B MoE) — and that the backend router assigns complex reasoning tasks to Claude while routing simple/fast tasks to LocalAI models. The routing decision is explicitly complexity-based: "simple/fast tasks to LocalAI (free) and complex tasks to Claude (paid)." This architecture implies that, as currently configured, Gemma 4 26B is not trusted for the class of reasoning tasks Claude handles in OpenFleet — it is used for simpler queries. The `OpenFleet` page documents the current local inference stack: "hermes-3b for queries, bge-m3 for embeddings, bge-reranker for reranking" — Gemma4 is available in AICP's loaded model set but the fleet's agents still use the older hermes stack. The `AICP` page's 5-stage roadmap (Stage 2: routing implemented, targeting 80%+ Claude token reduction) represents the framework within which Gemma 4 26B would be evaluated for escalating fleet task reliability. The practical answer from existing wiki knowledge: Gemma 4 26B has not yet replaced Claude for OpenFleet agent tasks in the current ecosystem configuration. AICP's complexity-scoring router is the mechanism that would govern any such substitution — when Gemma 4 26B's reliability on tool calling is empirically confirmed sufficient, the router's LocalAI threshold would be adjusted to route more agent tasks locally. Direct comparative benchmarking between Gemma 4 26B and Claude Sonnet for OpenFleet-specific task types (Requires: empirical evaluation; not yet documented in existing wiki pages).

**Q: What is the memory/performance profile of running multiple quantized models simultaneously (e.g., reasoning + embedding + reranking)?**

Cross-referencing `AICP` and `OpenFleet`: the AICP page documents that 9 models are currently loaded simultaneously on LocalAI v4.0.0 with GPU acceleration. The model roster is segmented by function: Qwen3 family (8B, 4B, 30B MoE, fast variant) for reasoning/chat; Gemma4 family (e2b, e4b, 26B MoE) for reasoning; legacy models (hermes, codellama); and specialized models (whisper for transcription, piper for TTS, nomic-embed and bge-m3 for embeddings, bge-reranker for reranking, stablediffusion for image generation). The `OpenFleet` page confirms the current fleet inference stack uses hermes-3b for queries, bge-m3 for embeddings, and bge-reranker for reranking simultaneously. The memory profile is implicit in the hardware context: all 9 models run on a GPU-accelerated LocalAI instance. The `Local LLM Quantization` page (this page) documents that a 26B model requires 18GB of GPU memory at standard quantization — which means simultaneous loading of multiple large models requires either sufficient VRAM, offloading to CPU RAM, or sequential loading with model swapping. AICP's 9-model configuration suggests model swapping is in use: specialized models (whisper, stablediffusion) are unlikely to be hot-loaded simultaneously with reasoning models. The ecosystem's hardware upgrade note (8GB→19GB VRAM) in the memory context confirms that VRAM growth directly unlocks simultaneous loading of larger model combinations. Full performance profiling of all 9 models loaded concurrently (Requires: empirical measurement on the specific GPU hardware; not documented in existing wiki pages).

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **What principle applies?** | [[right-process-for-right-context-the-goldilocks-imperative|Principle — Right Process for Right Context — The Goldilocks Imperative]] |
> | **What is my identity?** | [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]] |
> | **System map** | [[methodology-system-map|Methodology System Map]] |

## Relationships

- RELATES TO: [[aicp|AICP]]
- RELATES TO: [[openfleet|OpenFleet]]
- RELATES TO: [[openclaw|OpenClaw]]
- ENABLES: [[lightrag|LightRAG]]
- RELATES TO: [[claude-code|Claude Code]]

## Backlinks

[[aicp|AICP]]
[[openfleet|OpenFleet]]
[[openclaw|OpenClaw]]
[[lightrag|LightRAG]]
[[claude-code|Claude Code]]
[[local-model-vs-cloud-api-for-routine-operations|Decision — Local Model vs Cloud API for Routine Operations]]
[[E001-local-inference-engine|Local Inference Engine (Subsystem 3)]]
[[model-local-ai|Model — Local AI ($0 Target)]]
[[src-27-questions-llm-selection|Source — 27 Questions to Ask Before Choosing an LLM]]
[[src-hrm-trm-tiny-recursion-models|Synthesis — HRM and TRM: Tiny Recursive Models Beat LLMs on ARC-AGI]]
[[src-llm-architecture-gallery-raschka|Synthesis — LLM Architecture Gallery (Raschka)]]
