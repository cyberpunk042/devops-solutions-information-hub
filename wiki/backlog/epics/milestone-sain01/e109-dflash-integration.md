---
title: E109 — DFlash Integration
aliases:
  - "E109 — DFlash Integration"
  - "E109 — DFlash: Block-Diffusion Speculative Decoding"
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
  - id: src-dflash-block-diffusion-spec-dec
    type: wiki
    file: "wiki/sources/src-dflash-block-diffusion-spec-dec.md"
  - id: concept-speculative-decoding-block-diffusion
    type: wiki
    file: "wiki/domains/ai-models/concept-speculative-decoding-block-diffusion.md"
  - id: cmp-dflash-vs-eagle3-vs-medusa
    type: wiki
    file: "wiki/comparisons/cmp-dflash-vs-eagle3-vs-medusa.md"
tags: [epic, sain-01, dflash, speculative-decoding, block-diffusion, code-math-acceleration, vllm, qwen3, blackwell, rtx-3090]
---

# E109 — DFlash Integration

## Summary

Deploy **DFlash block-diffusion speculative decoding** for code/math workloads on the Blackwell + RTX 3090 GPU tiers. DFlash (Z-Lab, arXiv:2602.06036) replaces autoregressive drafting with a block-diffusion draft model using bidirectional attention, generating K tokens per forward pass. Reported speedups: **up to 6× lossless** (2.5× over EAGLE-3); **4.7× on Math500, 5.2× on HumanEval** at concurrency 1 on Qwen3-8B/B200. The operator's first-hand framing — "3× faster on code tasks, doesn't work on creative" — matches the paper's reported math/code-vs-conversational entropy gradient. Deploy via vLLM v0.20.1+ (mandatory minimum) with pre-trained DFlash drafts from `z-lab/<Model>-DFlash` on Hugging Face. The technique is workload-conditioned: turn ON for code/math/structured-output paths in [[e108-load-balancing-profiles|Profile 2/3]]; turn OFF for free-form conversational generation (creative writing has high per-token entropy → draft acceptance degrades → speedup approaches 1×). Composes orthogonally with [[concept-1bit-ternary-weights|ternary inference on CPU]] (Pulse on CCD 0) — the two techniques stack on different tiers.

## Operator Directive

> "Dflash I recently learned about that somehow with code task on model that fit in memory like any functional model in general it can work 3 times faster, does not work on creative tasks in general but interesting topic and place of introspection and knowledge"

## Goals

See Done When — verifiable per-workload speedup checkpoints.

## Done When

- [ ] **vLLM upgraded** to v0.20.1+ (mandatory for DFlash support); older deployments rejected by the integration
- [ ] **DFlash draft model selected** from `https://huggingface.co/z-lab` for the target Oracle Core or Logic Engine model (e.g., `z-lab/Qwen3-8B-DFlash-b16` for an 8B target; `z-lab/Qwen3.6-35B-A3B-DFlash` for the MoE 35B-A3B target; `z-lab/Qwen3.5-27B-DFlash` for 27B)
- [ ] **Draft + target downloaded** to `tank/models` (separate subdirectories)
- [ ] **vLLM serves with DFlash draft**: `podman run --device nvidia.com/gpu=all vllm/vllm-openai:latest --model /models/<target> --speculative-model /models/<draft-DFlash> --speculative-tokens K` (where K = block size; tune per workload)
- [ ] **Math benchmark verification**: HumanEval and MATH-500 evals produce ≥3× speedup vs vLLM-no-speculation baseline; recorded in epic artifacts
- [ ] **Code benchmark verification**: MBPP / LiveCodeBench show ≥3× speedup at concurrency 1
- [ ] **Conversational baseline verification**: MT-Bench shows ≤2× speedup (expected to degrade per the entropy-gradient pattern); not a failure — the technique is workload-conditioned
- [ ] **Acceptance rate logged**: vLLM exposes draft acceptance rate metrics; record for each benchmark
- [ ] **Composes with `--kv-cache-dtype fp8`** (from [[e108-load-balancing-profiles|Profile 3]]): verify the combination works; if not, document the conflict
- [ ] **Single-GPU fallback verified**: DFlash on RTX 3090 alone (no tensor-parallel) for ~2× on a 27B target — matches Luce DFlash community writeup
- [ ] **Profile integration**: profile YAML (Profile 2 + Profile 3) documents "with DFlash" vs "without DFlash" variants; operator selects per workload type
- [ ] **Operator runbook**: workload-selection guidance documented — turn ON for math/code/structured-output; turn OFF for free-form

## Scale and Model

> [!info] Epic Parameters
>
> | Parameter | Value |
> |---|---|
> | **Model** | feature-development |
> | **Quality tier** | Skyscraper |
> | **Estimated tasks** | 6-8 |
> | **Dependencies** | E103 (GPUs ready), E108 (profiles operationalized — DFlash slots into Profile 2/3), E102 (model + draft weights on `tank/models`) |
> | **Feeds into** | E110 (model catalog — DFlash applies to the chosen resident model if supported) |
> | **External dependency** | vLLM v0.20.1+ availability; Z-Lab maintains pre-trained drafts for the chosen target (or operator accepts EAGLE-3 fallback) |

## Handoff Context

> [!info] For a fresh context picking up this epic:
>
> - Milestone: [[sain-01-sovereign-node|Milestone — SAIN-01 Sovereign AI Node]]
> - L1 DFlash synthesis: [[src-dflash-block-diffusion-spec-dec|DFlash block-diffusion synthesis]]
> - L2 concept: [[concept-speculative-decoding-block-diffusion|Speculative Decoding via Block Diffusion]]
> - L3 family comparison: [[cmp-dflash-vs-eagle3-vs-medusa|DFlash vs EAGLE-3 vs MEDUSA]] — picks DFlash for math/code; EAGLE-3 maturity-fallback; MEDUSA for custom-target community drafts
> - **vLLM v0.20.1+ is the gating dependency**. Older vLLM cannot deploy DFlash — must upgrade.
> - **Workload-conditioning is the operative pattern**. DFlash doesn't break on creative workloads; the speedup just collapses. Operator picks per workload, not per model.
> - Z-Lab's training recipe was "open-sourced soon" as of Q2 2026 — custom-target draft training may not be possible yet; depend on the ~20 pre-trained drafts that ship.

## Relationships

- PART OF: [[sain-01-sovereign-node|Milestone — SAIN-01 Sovereign AI Node]]
- DEPENDS ON: [[e102-zfs-storage-layout|E102 — ZFS Storage Layout]] (draft + target weights on `tank/models`)
- DEPENDS ON: [[e103-vfio-isolation|E103 — VFIO Isolation]] (GPUs ready)
- DEPENDS ON: [[e108-load-balancing-profiles|E108 — Load-Balancing Profiles]] (DFlash slots into Profile 2/3)
- ENABLES: [[e110-model-catalog|E110 — Model Catalog]] (operator picks DFlash-supported targets)
- IMPLEMENTS: [[src-dflash-block-diffusion-spec-dec|Synthesis — DFlash block-diffusion]]
- IMPLEMENTS: [[concept-speculative-decoding-block-diffusion|Concept — Speculative Decoding via Block Diffusion]]
- RELATES TO: [[cmp-dflash-vs-eagle3-vs-medusa|Comparison — DFlash vs EAGLE-3 vs MEDUSA]]
- COMPLEMENTS: [[e106-pulse-vector-runtime|E106 — Pulse Vector Runtime]] (CPU ternary; orthogonal acceleration on different tier)

## Backlinks

(will be populated by `tools/obsidian.py backlinks` after pipeline post)
