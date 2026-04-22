---
title: "E008 — Local K2.6 Offline Frontier Tier (KTransformers on /dev/sdd)"
type: epic
domain: backlog
status: draft
priority: P1
task_type: epic
current_stage: document
readiness: 20
progress: 0
stages_completed: []
artifacts: []
confidence: high
created: 2026-04-22
updated: 2026-04-22
sources:
  - id: operator-directive
    type: file
    file: raw/notes/2026-04-22-directive-post-anthropic-self-autonomous-plan.md
  - id: src-kimi-k2-6-synthesis
    type: wiki
    file: wiki/sources/tools-integration/src-kimi-k2-6-moonshot-agent-swarm.md
    title: "Synthesis — Kimi K2.6"
  - id: src-airllm-synthesis
    type: wiki
    file: wiki/sources/tools-integration/src-airllm-layer-wise-inference-nvme-ssd-offload.md
    title: "Synthesis — AirLLM"
tags: [epic, p1, kimi-k2-6, ktransformers, offline, local-inference, gguf, moe, disk-offload, post-anthropic]
---

# E008 — Local K2.6 Offline Frontier Tier (KTransformers on /dev/sdd)

## Summary

Stand up Kimi K2.6 Q2 (340 GB GGUF from Unsloth HF) as a local **offline frontier-capability tier** using KTransformers on operator's 19 GB VRAM + 64 GB RAM (incoming 2026-04-23) + /dev/sdd (WD_BLACK SN770 Gen4 NVMe, 5-7 GB/s). Delivers $0-per-invocation, fully-offline, privacy-preserving frontier reasoning for tasks where network access is unacceptable or undesirable. Complements E007's cloud path (OpenRouter K2.6) — same model, different trade-offs: cloud is faster + costlier, local is free + slower but capability-equivalent.

## Operator Directive

> "Soon I will be at 64RAM (1 day) and we can have at least the same amount as swap on my RAID 0 NVME ssds."

> "In 5 days everything will most likely be happening on this computer with the 19GB VRAM and the 1TB NVME SSD for AirLLM and so on... we will make this workstation self-autonomous."

> "I want the plan to be thorough... I don't want to have to deal with Anthropic and Claude and Opus in the future."

## Goals

- K2.6 Q2 GGUF (340 GB) downloaded from `huggingface.co/unsloth/Kimi-K2.6-GGUF` to `/mnt/models` on /dev/sdd (WD_BLACK NVMe).
- KTransformers installed, configured for MoE disk-offload on operator's hardware.
- First-light inference test: cold-start time measured, sustained tok/s measured, 256K context behavior verified.
- Routing-adapter for K2.6 local ready for E011 M011.3 integration into AICP.
- Documentation: what works, what's slow, when to prefer local over OpenRouter.

## Done When

- [ ] `/mnt/models` exists as an ext4 mount of /dev/sdd (resolved via E010 M010.3)
- [ ] `unsloth/Kimi-K2.6-GGUF` Q2 variant (~340 GB) downloaded and checksum-verified to `/mnt/models/kimi-k2-6-q2/`
- [ ] KTransformers installed (Python package, CUDA build) and importable
- [ ] `python -c "import ktransformers; print(ktransformers.__version__)"` succeeds
- [ ] First inference: `./scripts/kt-smoke.sh` (to be authored) completes a 50-token generation successfully
- [ ] Cold-start time measured and recorded in `wiki/log/2026-04-24-k2-6-local-first-light.md`
- [ ] Sustained tok/s measured at 3 context sizes (1K, 32K, 256K) — results in same wiki log
- [ ] Context behavior at 256K: full context load, no OOM, tok/s degradation measured
- [ ] Quality comparison: same 3 wiki-typical workloads run via local K2.6 and via OpenRouter K2.6 — identical outputs expected, differences documented
- [ ] Routing-adapter stub ready for AICP: Python module (e.g., `aicp/backends/kimi_k2_6_local.py`) that exposes K2.6-local as an OpenAI-compatible endpoint
- [ ] `wiki/log/2026-04-24-k2-6-local-first-light.md` published with tok/s tables, setup commands, gotchas
- [ ] `python3 -m tools.pipeline post` returns 0 validation errors after all E008 work commits

## Scale and Model

> [!info] Epic Parameters
>
> | Parameter | Value |
> |-----------|-------|
> | **Model** | feature-development |
> | **Quality tier** | Pyramid (second-priority — E007 handles the deadline; E008 is offline bonus) |
> | **Estimated modules** | 4 |
> | **Estimated tasks** | 10-12 |
> | **Dependencies** | E010 M010.1 (64 GB RAM), E010 M010.3 (/dev/sdd mount), ~1 TB NVMe free (confirmed) |

## Stage Artifacts (per methodology model)

> [!abstract] Stage → Artifact Map
>
> | Stage | Required Artifacts | Location |
> |-------|--------------------|----------|
> | Document | K2.6 synthesis (DONE), KTransformers research note | `wiki/sources/tools-integration/` |
> | Design | Disk layout doc, KTransformers config choices, benchmark plan | `wiki/log/` |
> | Scaffold | Download script, kt-smoke.sh, routing-adapter stub | `scripts/`, `aicp/backends/` (if AICP repo accessible) |
> | Implement | Install KTransformers, download GGUF, run smoke, benchmark | Shell commands |
> | Test | Benchmark log, quality A/B vs OpenRouter K2.6 | `wiki/log/2026-04-24-k2-6-local-first-light.md` |

## Module Breakdown

| Module | Delivers | Est. Tasks |
|--------|----------|-----------|
| [[e008-m001-ktransformers-install-and-config]] | KTransformers installed, CUDA-compatible, configured for MoE offload | 3 |
| [[e008-m002-k2-6-q2-gguf-download-and-verify]] | Q2 GGUF at `/mnt/models/kimi-k2-6-q2/`, checksum verified | 2 |
| [[e008-m003-first-light-benchmark]] | Cold-start, sustained tok/s at 1K/32K/256K context, documented | 3 |
| [[e008-m004-local-backend-adapter]] | K2.6-local exposed as an OpenAI-compatible endpoint for AICP consumption | 2-3 |

## Dependencies

- [[E010-storage-and-hardware-enablement]] M010.1 (64 GB RAM installed) — page cache benefits from more RAM; hot-expert cache hit rate rises with RAM.
- [[E010-storage-and-hardware-enablement]] M010.3 (/dev/sdd mounted at /mnt/models) — required as the GGUF storage location; KTransformers needs a filesystem path.
- Network bandwidth — 340 GB download. At 100 Mbps: ~8h. At 1 Gbps: ~45 min. Operator's actual bandwidth TBD.
- Python environment with CUDA toolkit + bitsandbytes or equivalent; KTransformers has specific CUDA version requirements — verified during M008.1.

## Open Questions

> [!question] Realistic tok/s for K2.6 Q2 on 19 GB VRAM + 64 GB RAM + single Gen4 NVMe via KTransformers?
> Published benchmarks span 2-15 tok/s depending on hardware. Operator's hardware combination is new — M008.3 benchmark produces the authoritative number.

> [!question] Does the 256K context work in practice, or does memory pressure limit us to a smaller effective context?
> M008.3 explicitly tests 256K. Fallback: operate at 32K-64K if 256K causes OOM.

> [!question] Does K2.6 Q2 quality match K2.6-via-OpenRouter on operator's workloads?
> QAT-trained for INT4 — Moonshot claims minimal quality loss. M008.3 A/B test confirms empirically.

> [!question] Should Q4 also be downloaded for quality-vs-speed comparison, or skip to save 584 GB?
> Default: skip Q4. Revisit only if Q2 shows unacceptable quality gap. Storage consideration: Q2 (340 GB) + Q4 (584 GB) = 924 GB — fits on /dev/sdd 1 TB but leaves little headroom.

## Relationships

- PART OF: [[post-anthropic-self-autonomous-stack|Milestone: Post-Anthropic Self-Autonomous AI Stack]]
- DEPENDS ON: [[E010-storage-and-hardware-enablement|E010-storage-and-hardware-enablement]]
- BUILDS ON: [[src-kimi-k2-6-moonshot-agent-swarm|Synthesis — Kimi K2.6]]
- BUILDS ON: [[src-airllm-layer-wise-inference-nvme-ssd-offload|Synthesis — AirLLM]] (disk-offload paradigm)

## Backlinks

[[post-anthropic-self-autonomous-stack|Milestone: Post-Anthropic Self-Autonomous AI Stack]]
[[E010-storage-and-hardware-enablement|E010-storage-and-hardware-enablement]]
[[Synthesis — Kimi K2.6]]
[[Synthesis — AirLLM]]
