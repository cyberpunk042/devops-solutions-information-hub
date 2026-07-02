---
title: E110 — Model Catalog
aliases:
  - "E110 — Model Catalog"
  - "E110 — Model Catalog: Ling + Nemotron + Resident Selection"
type: epic
domain: backlog
status: draft
priority: P1
task_type: epic
current_stage: document
readiness: 30
progress: 0
stages_completed: []
artifacts: []
confidence: high
created: 2026-05-16
updated: 2026-05-16
sources:
  - id: milestone
    type: file
    file: "wiki/backlog/milestones/sain-01-sovereign-node.md"
  - id: cmp-ling-vs-nemotron
    type: wiki
    file: "wiki/comparisons/cmp-ling-26-flash-vs-nemotron-3-nano-omni.md"
  - id: ling-hf
    type: documentation
    url: "https://hf.co/inclusionAI/Ling-2.6-flash"
  - id: nemotron-hf
    type: documentation
    url: "https://hf.co/nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16"
  - id: operator-model-candidate-directive
    type: directive
    file: "raw/notes/2026-05-15-user-directive-sain01-info-hub-ingestion.md"
tags: [epic, sain-01, model-catalog, ling-2-6-flash, nemotron-3-nano-omni, blackwell-resident, oracle-core, vllm, moe, quantization]
---

# E110 — Model Catalog

## Summary

Resident-deploy the **Oracle Core's primary model(s)** on the 96 GB RTX PRO 6000 Blackwell — at least one of the operator-named candidates: **`inclusionAI/Ling-2.6-flash`** (107 B params, MoE, MIT, text-only, requires Q4 or MoE-active-only to fit) OR **`nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16`** (33 B, hybrid Mamba-Transformer MoE, multimodal, BF16 native fit with 30 GB headroom). The [[cmp-ling-26-flash-vs-nemotron-3-nano-omni|L3 comparison]] establishes that the two are complementary, not substitutes — both can resident-deploy at different times via runtime profile selection, or simultaneously in quantized form (Ling Q4 ~54 GB + Nemotron Q4 ~17 GB = ~71 GB, ~25 GB headroom for KV cache). Model weights live on `tank/models` (1M recordsize, lz4); vLLM serves via the Weaver's routing. Per-model quantization + format choice documented. Ling needs license sensitivity unchanged (MIT — clean); Nemotron requires license review for any commercial path ("other" — NVIDIA custom). DFlash integration (E109) applies to whichever target has a pre-trained DFlash draft on Hugging Face.

## Operator Directive

> "There is also those I think will be good candidate in general for the rtx pro 6000 96gb amongs other we will add to the list:
> https://huggingface.co/inclusionAI/Ling-2.6-flash
> https://huggingface.co/nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16"

## Goals

See Done When — verifiable resident-model deployment checkpoints.

## Done When

- [ ] **Operator picks the primary resident model**: Ling (text-heavy reasoning, MIT licensing) OR Nemotron-Omni (multimodal, lower-friction BF16 fit, NVIDIA backing) OR both (quantized + simultaneously resident)
- [ ] **License review documented** if Nemotron is picked: NVIDIA "other" license terms reviewed against the operator's intended use (personal sovereign workstation = almost certainly fine; commercial productization = requires legal review)
- [ ] **Model weights downloaded** to `tank/models/<model-name>/` (via Marvell 10GbE per [[e105-network-segregation|E105]]); recordsize 1M + lz4 verified
- [ ] **Quantization variant selected** per model + deployment goal:
  - Ling-2.6-flash: Q4 (~54 GB on disk + VRAM) OR MoE-active-only (full BF16; active params ~20-26 GB at any time)
  - Nemotron-3-Nano-Omni: BF16 native (~66 GB on Blackwell with 30 GB headroom) OR FP8 (~33 GB, 63 GB headroom) OR FP4 (~17 GB, 79 GB headroom)
- [ ] **vLLM serves the model** via Podman: `podman run --device nvidia.com/gpu=0 -v /mnt/vault/models:/models:ro vllm/vllm-openai:latest --model /models/<name>` (`device=0` = Blackwell since RTX 4090 is VFIO-bound — verify the dev ID corresponds to the Blackwell)
- [ ] **First inference test**: simple prompt → response succeeds end-to-end; throughput recorded
- [ ] **Long-context test** (Nemotron only): prompt with ~100 K tokens of input → response; verify Mamba-Transformer scaling holds; record memory + latency
- [ ] **Multimodal test** (Nemotron only): text + image input → response; verify all-to-any capability works
- [ ] **Weaver routing wired**: Weaver's gRPC layer routes queries to the resident model; integration with [[e108-load-balancing-profiles|Profile 2/3]] verified
- [ ] **DFlash compatibility check**: if the chosen target has a pre-trained DFlash draft, integrate per [[e109-dflash-integration|E109]]; if not, document the fallback (EAGLE-3 if available, or no speculative decoding)
- [ ] **Both-models-coexist test** (if operator picks the quantized-simultaneous path): both Ling Q4 + Nemotron Q4 resident at the same time; switching via runtime profile mechanism; verified ~25 GB headroom for KV cache + activations
- [ ] **Performance baseline recorded**: tokens/sec, time-to-first-token, memory consumption, energy draw — for each deployed model; documented in epic artifacts
- [ ] **Auditor compatibility**: the chosen models' inference processes match the Tetragon allowlist (vllm, podman); no false-positive kills during inference

## Scale and Model

> [!info] Epic Parameters
>
> | Parameter | Value |
> |---|---|
> | **Model** | integration |
> | **Quality tier** | Skyscraper |
> | **Estimated tasks** | 8-10 (model pick + download + quantization + serving + benchmark) |
> | **Dependencies** | E102 (tank/models), E103 (Blackwell ready), E105 (10GbE for weight downloads), E107 (Weaver routes queries), E108 (profiles call the model), E109 (DFlash integration if applicable) |
> | **Feeds into** | The milestone's final acceptance gate ("at least one of {Nemotron, Ling} resident on Blackwell") |
> | **Operator gate** | Model selection is operator decision; downstream automation can't pick |

## Handoff Context

> [!info] For a fresh context picking up this epic:
>
> - Milestone: [[sain-01-sovereign-node|Milestone — SAIN-01 Sovereign AI Node]]
> - L3 model comparison (the load-bearing decision support): [[cmp-ling-26-flash-vs-nemotron-3-nano-omni|Ling vs Nemotron comparison]]
> - L1 SAIN-01 spec: [[src-sain-01-sovereign-node-spec|§ 17.1 Oracle Core role]]
> - Live HF data (verified at L1 ingest time):
>   - Ling-2.6-flash: 107,494 M params, `bailing_hybrid` MoE, MIT license, May 3 2026 update
>   - Nemotron-3-Nano-Omni: 33,015 M params, `NemotronH_Nano_Omni_Reasoning_V3` (hybrid Mamba-Transformer), multimodal, "other" license, May 8 2026 update
> - **The "both can coexist" framing is the architectural insight**: they're not substitutes; pick per workload. The operator originally added both as "good candidate in general for the rtx pro 6000 96gb amongs other we will add to the list" — implying additional candidates may join over time.
> - **Ling cannot fit at BF16** on the Blackwell (~214 GB raw). Plan for Q4 or MoE-active-only up front.

## Relationships

- PART OF: [[sain-01-sovereign-node|Milestone — SAIN-01 Sovereign AI Node]]
- DEPENDS ON: [[e102-zfs-storage-layout|E102 — ZFS Storage Layout]]
- DEPENDS ON: [[e103-vfio-isolation|E103 — VFIO Isolation]]
- DEPENDS ON: [[e105-network-segregation|E105 — Network Segregation]]
- DEPENDS ON: [[e107-weaver-state-fabric|E107 — Weaver State Fabric]]
- DEPENDS ON: [[e108-load-balancing-profiles|E108 — Load-Balancing Profiles]]
- DEPENDS ON: [[e109-dflash-integration|E109 — DFlash Integration]] (if pre-trained draft available for the chosen target)
- IMPLEMENTS: [[cmp-ling-26-flash-vs-nemotron-3-nano-omni|Comparison — Ling vs Nemotron]] (operationalizes the per-workload decision)
- RELATES TO: [[local-llm-quantization|Local LLM Quantization]] (Q4/FP8/FP4 + MoE-active-only choices)

## Backlinks

[[sain-01-sovereign-node|Milestone — SAIN-01 Sovereign AI Node]]
[[e102-zfs-storage-layout|E102 — ZFS Storage Layout]]
[[e103-vfio-isolation|E103 — VFIO Isolation]]
[[e105-network-segregation|E105 — Network Segregation]]
[[e107-weaver-state-fabric|E107 — Weaver State Fabric]]
[[e108-load-balancing-profiles|E108 — Load-Balancing Profiles]]
[[e109-dflash-integration|E109 — DFlash Integration]]
[[Comparison — Ling vs Nemotron]]
[[local-llm-quantization|Local LLM Quantization]]
