---
title: E108 — Load-Balancing Profiles
aliases:
  - "E108 — Load-Balancing Profiles"
  - "E108 — Profiles: Ultra-Sovereign + Asymmetric-Burst + Deep-Context"
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
  - id: src-sain-01-sovereign-node-spec
    type: wiki
    file: "wiki/sources/src-sain-01-sovereign-node-spec.md"
tags: [epic, sain-01, profiles, load-balancing, runtime-profiles, orchestration, ultra-sovereign, asymmetric-burst, deep-context-synthesis]
---

# E108 — Load-Balancing Profiles

## Summary

Operationalize the three runtime profiles from [[src-sain-01-sovereign-node-spec|§ 18]] as the [[e107-weaver-state-fabric|Weaver]]'s top-level workload-routing primitive. **Profile 1 — Ultra-Sovereign Efficiency** (CPU-pinned BitNet on cores 0-7, GPUs in `nvidia-smi -pm 1` sleep — for continuous background state monitoring at near-zero power). **Profile 2 — Asymmetric Burst** (CPU coordinates state, sub-agents fan out across CPU + cuda:0 + cuda:1 with per-agent VRAM limits and engine selection — for multi-specialist code/repo analysis bursts). **Profile 3 — Deep Context Synthesis** (CPU runs streaming tokenizer, dual-GPU tensor-parallel with `--kv-cache-dtype fp8` — for whole-system telemetry parsing). **L1 corrections required**: Profile 2's JSON in the L0 dump references `vllm-vulkan` (not a real backend; use vLLM-CUDA or llama.cpp-Vulkan), `BitNet-b1.58-13B` (hallucinated; substitute a real model from [[src-bitnet-b158-ternary-llm|the canon]]), `Qwen-32B-Ternary-Quant` (not a real model ID; pick a real Qwen quantization), and `DeepSeek-R1-Distill-Llama-70B-FP16` (the distill is BF16, not FP16). Authored as YAML config files the Weaver's orchestration switches on.

## Operator Directive

> "loadbalancing / SRP and potentials profiles to try"

## Goals

See Done When — verifiable per-profile resource allocation + runtime switching.

## Done When

- [ ] **Profile 1 YAML** authored at `/etc/sovereign/profiles/ultra-sovereign-efficiency.yaml` — pins `bitnet-cli` to cores 0-7 + sets `nvidia-smi -pm 1` on both GPUs; verifies low-power state
- [ ] **Profile 2 JSON/YAML** authored at `/etc/sovereign/profiles/asymmetric-burst.yaml` with **L1 corrections** baked in: replace `vllm-vulkan` with `vllm` (CUDA backend; if Vulkan path actually needed, use llama.cpp); replace `BitNet-b1.58-13B` with `microsoft/bitnet-b1.58-2B-4T` or `Llama3-8B-1.58`; replace `Qwen-32B-Ternary-Quant` with a real Qwen quantization (e.g., Qwen2.5-32B-Instruct-AWQ-INT4 from a verified source); replace `DeepSeek-R1-Distill-Llama-70B-FP16` with `DeepSeek-R1-Distill-Llama-70B` (BF16 packaging is default)
- [ ] **Profile 3 YAML** authored at `/etc/sovereign/profiles/deep-context-synthesis.yaml` — uses `vllm/vllm-openai:latest` Podman image with `--tensor-parallel-size 2`, `--pipeline-parallel-size 1`, `--gpu-memory-utilization 0.95`, `--kv-cache-dtype fp8`; verify all flags are real vLLM options
- [ ] **Weaver routing switch implemented**: Weaver reads `/etc/sovereign/active-profile` and routes accordingly; profile switching documented (manual operator action + automated triggers for future)
- [ ] **Profile 1 throughput test**: Pulse-only inference at 5+ tok/sec sustained for 1 hour; GPUs verified in low-power state; total power draw < 80W
- [ ] **Profile 2 multi-agent test**: launch 3 sub-agents simultaneously per the corrected JSON; each routes to the right hardware tier; the Auditor's Tetragon policy does not flag any
- [ ] **Profile 3 tensor-parallel test**: vLLM serves a model across both GPUs (Blackwell + 3090); throughput at fp8 KV cache exceeds single-GPU baseline by 1.5×+
- [ ] **Profile switch test**: switch Profile 1 → Profile 2 → Profile 3 → Profile 1; each transition completes cleanly without orphaned processes
- [ ] **Auditor compatibility**: each profile's spawned processes match the Tetragon allowlist; no false-positive kills during profile switching
- [ ] **Documentation per profile**: operator runbook (when to pick which) ships at `docs/operator/sain01-profiles.md` (or equivalent in the wiki)

## Scale and Model

> [!info] Epic Parameters
>
> | Parameter | Value |
> |---|---|
> | **Model** | feature-development |
> | **Quality tier** | Skyscraper |
> | **Estimated tasks** | 8-10 |
> | **Dependencies** | E103 (VFIO 3090 for Profile 2/3), E104 (Tetragon allowlist must permit profile-spawned binaries), E106 (Pulse runtime for Profile 1), E107 (Weaver routes per profile), E109 (DFlash applies in Profile 2/3 for code/math) |
> | **Feeds into** | E110 (model catalog selection happens within a profile context) |
> | **Operator gate** | Operator picks which profile is the default; switching policy (manual vs auto-triggered) is operator decision |

## Handoff Context

> [!info] For a fresh context picking up this epic:
>
> - Milestone: [[sain-01-sovereign-node|Milestone — SAIN-01 Sovereign AI Node]]
> - L1 spec section: [[src-sain-01-sovereign-node-spec|§ 18 Load Balancing & Runtime Profiles to Try]]
> - **L1 corrections must be applied**: 4 hallucinated model IDs + 1 hallucinated backend (vllm-vulkan) in Profile 2's JSON. See the SAIN-01 synthesis page's "What's verified vs hallucinated" table for the full list.
> - Profile 2's JSON is illustrative — operator should adapt VRAM limits + model picks to their workload mix; the exact JSON in the L0 dump is a template, not a deployment spec
> - vLLM flag set in Profile 3 (`--tensor-parallel-size 2`, `--kv-cache-dtype fp8`, etc.) is real and tested; safe to deploy as-is

## Relationships

- PART OF: [[sain-01-sovereign-node|Milestone — SAIN-01 Sovereign AI Node]]
- DEPENDS ON: [[e103-vfio-isolation|E103 — VFIO Isolation]]
- DEPENDS ON: [[e104-tetragon-guardian-perimeter|E104 — Tetragon + Guardian Perimeter]]
- DEPENDS ON: [[e106-pulse-vector-runtime|E106 — Pulse Vector Runtime]]
- DEPENDS ON: [[e107-weaver-state-fabric|E107 — Weaver State Fabric]]
- DEPENDS ON: [[e109-dflash-integration|E109 — DFlash Integration]] (Profile 2/3 code/math workloads use DFlash)
- ENABLES: [[e110-model-catalog|E110 — Model Catalog]]
- IMPLEMENTS: [[src-sain-01-sovereign-node-spec|SAIN-01 Sovereign Node Spec]] § 18

## Backlinks

(will be populated by `tools/obsidian.py backlinks` after pipeline post)
