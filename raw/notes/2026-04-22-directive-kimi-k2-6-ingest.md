---
title: "Directive — 2026-04-22 — Ingest Kimi K2.6 + Hardware Update (64GB RAM + RAID 0 NVMe Swap)"
date: 2026-04-22
type: directive
tags: [directive, kimi, moonshot, hardware, swap, raid-nvme, verbatim]
---

# Directive — 2026-04-22 — Ingest Kimi K2.6 + Hardware Update

## Verbatim (user) — 2026-04-22

> I also hear about this KIMI thing that would even highly beat Opus 4.7 and 5.4 now...
> Lets do our research properly

> Soon I will be at 64RAM (1 day) and we can have at least the same amount as swap on my RAID 0 NVME ssds
>
> but yea continue

## Context (operator intent, inferred)

- Research Kimi K2.x properly per established ingestion methodology (directive → fetch → synthesize → cross-ref → deepen).
- Hardware profile update: **64 GB RAM (in ~1 day)** + **RAID 0 NVMe SSDs** (1 TB previously confirmed) **with ≥ 64 GB swap usable on the RAID** — effective addressable memory rises dramatically for large MoE + disk-offload workloads.
- Strategic frame (from preceding turns): 5-day horizon to make workstation self-autonomous if Claude Code subscription becomes unavailable; harness-neutral consumer contract; no quality compromise. Kimi is a top-tier candidate for the premium/routing tier.

## Actions taken this session

1. WebSearch × 4 (benchmarks / architecture / GGUF / OpenRouter pricing).
2. WebFetch × 4 (Moonshot K2.6 blog, Unsloth GGUF page, OpenRouter K2.6 page, The Decoder article).
3. Synthesis: **Kimi K2.6 is real Opus-class agentic competitor at ~1/20th cost; MIT-licensed; open weights available via Unsloth/ubergarm GGUF quants (340 GB Q2 → 2.05 TB BF16).**
4. Realistic deployment: **primary via OpenRouter ($0.80/$3.50 per M tokens) today; local via KTransformers disk-offload on NVMe/swap once 64 GB RAM lands — now feasible, previously aspirational.**
5. Wiki capture: `wiki/sources/tools-integration/src-kimi-k2-6-moonshot-agent-swarm.md` + Model — Local AI + 2026 Consumer-Hardware Stack + Second-Brain Custom Model Strategy updates.

## Principles applied

- **Principle 1 — Infrastructure > Instructions**: Kimi is captured in the wiki as a source synthesis, not as a chat response — future sessions inherit it through the structured context.
- **Principle 4 — Declarations Aspirational Until Verified**: "K2.6 beats Opus 4.6" is a vendor claim sourced from Moonshot's own blog + cross-validated by The Decoder + BuildFastWithAI. Benchmarks referenced by source, but **independent production verification on operator workloads is PENDING**. Capture as growing-maturity synthesis with evidence trail, not validated.
- **Memory rule — verbatim logging**: User's exact words captured above before any action. Memory file added if not present.

## Cross-ref anchors

- [[src-airllm-layer-wise-inference-nvme-ssd-offload|AirLLM]] — same disk-offload paradigm, pre-dates K2.6, model-agnostic
- [[src-gpt-oss-openai-open-weight-moe|gpt-oss]] — same MoE + open-weight family, different scale
- [[src-turboquant-122b-macbook|TurboQuant]] — Apple Silicon parallel
- [[open-model-evaluation-framework|Open-Model Evaluation Framework]] — the 5-stage decision process applied here
- [[2026-consumer-hardware-ai-stack|2026 Consumer-Hardware AI Stack]] — updated with K2.6 in Tier 3 (premium/routing)
- [[second-brain-custom-model-strategy|Second-Brain Custom Model Strategy]] — K2.6 via OpenRouter potentially obsoletes most capability-focused custom training candidates
