---
title: E106 — Pulse Vector Runtime
aliases:
  - "E106 — Pulse Vector Runtime"
  - "E106 — Pulse: bitnet.cpp + AVX-512 + AOT Wasm"
type: epic
domain: backlog
status: draft
priority: P0
task_type: epic
current_stage: document
readiness: 35
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
  - id: src-bitnet-b158-ternary-llm
    type: wiki
    file: "wiki/sources/src-bitnet-b158-ternary-llm.md"
  - id: src-zen5-avx512-single-cycle
    type: wiki
    file: "wiki/sources/src-zen5-avx512-single-cycle.md"
  - id: concept-1bit-ternary-weights
    type: wiki
    file: "wiki/domains/ai-models/concept-1bit-ternary-weights.md"
  - id: concept-dual-ccd-cache-partitioning-9900x
    type: wiki
    file: "wiki/domains/devops/concept-dual-ccd-cache-partitioning-9900x.md"
tags: [epic, sain-01, pulse, conductor, bitnet, ternary, 1bit, avx512, vnni, ccd-pinning, wasm, aot, cranelift, wasmtime]
---

# E106 — Pulse Vector Runtime

## Summary

Deploy the **Pulse** module — the first in the [[concept-srp-trinity-pulse-weaver-auditor|SRP Trinity]] — as a CPU-pinned ternary inference runtime + AOT-Wasm vector pipeline. The substrate is the [[concept-dual-ccd-cache-partitioning-9900x|9900X CCD 0]] (cores 0-5, thread mask `0xfff`). The primary runtime is **`bitnet.cpp`** running an official Microsoft b1.58 model (`microsoft/bitnet-b1.58-2B-4T` recommended for production; `microsoft/bitnet_b1_58-3B` matches the L0 dump's "3B" reference). Secondary: AOT-compiled WebAssembly via **Cranelift + Wasmtime** for custom bit-plane operations, with the `-C target-cpu=znver5` setting in Cranelift to emit single-cycle 512-bit AVX-512 (NOT via the L0 dump's wrong `WASMTIME_COMPARE_OPTIONS` env var — that's hallucinated). The Pulse handles: state routing, intent classification, sub-millisecond branching for the [[concept-srp-trinity-pulse-weaver-auditor|Conductor Agent]] responsibility. Target throughput: ≥5 tokens/sec sustained on operator-representative workload, with energy consumption ~5W average draw (estimate; verify on actual hardware). The L1/L2 grounding ([[concept-1bit-ternary-weights|1-bit Ternary Weights]] + [[src-bitnet-b158-ternary-llm|BitNet b1.58 synthesis]]) covers the ternary-math elimination of multiplication + the VNNI VPDPBUSD acceleration path.

## Operator Directive

> "1-bit notion and 512bit advantages"

> "the conductor agent"

> "BitNet-b1.58-3B" — L1 correction: the canonical 3B model is `microsoft/bitnet_b1_58-3B`; the L0 dump's `BitNet-b1.58-13B` is hallucinated and must NOT be substituted

## Goals

See Done When — verifiable CPU-inference throughput + pinning correctness checkpoints.

## Done When

- [ ] **`bitnet.cpp` cloned + built** from `github.com/microsoft/BitNet` with Python ≥3.9, CMake ≥3.22, Clang ≥18
- [ ] **Build flags** confirmed: `-march=znver5 -mavx512f -mavx512dq -mavx512bw -mavx512vl -mavx512bf16 -mavx512fp16` (per [[src-zen5-avx512-single-cycle|Zen 5 synthesis]])
- [ ] **Production-ready model selected + downloaded** to `tank/models`: `microsoft/bitnet-b1.58-2B-4T` (or `microsoft/bitnet_b1_58-3B` if operator picks 3B per L0 dump reference)
- [ ] **L1-corrected from L0**: confirm that `BitNet-b1.58-13B` is NOT what was deployed (no such Microsoft release; the dump's reference was hallucinated)
- [ ] **Kernel I2_S or TL2** selected based on Zen 5 benchmark: deploy + test both `i2_s` and `tl2` formats; pick the higher-throughput option on operator workload
- [ ] **CCD pinning correct**: `taskset -c 0-5 bitnet-cli -m ./models/bitnet-b1.58-2B-4T/ggml-model-i2.gguf -p "Evaluate state transition" --threads 6` executes pinned to cores 0-5 (CCD 0); confirmed via `taskset -p <pid>`
- [ ] **Throughput verified**: ≥5 tokens/sec sustained on operator workload (target depends on model size; 2.4B should hit higher, 8B Llama3-1.58 lower); recorded in epic artifacts
- [ ] **AVX-512 path engaged**: `perf stat -e avx512_inst -- bitnet-cli ...` shows non-trivial AVX-512 instruction count; VPDPBUSD specifically engaged for VNNI matmul
- [ ] **CCD locality preserved**: no thread migration off CCD 0 during sustained inference (verify via `perf sched record + perf sched timehist`)
- [ ] **AOT Wasm runtime built**: `wasmtime` installed; sample bit-plane Wasm module compiled with `wasmtime compile --target x86_64-unknown-linux-gnu -O speed <path>.wasm` (**L1 correction**: `--target` takes a triple, NOT `znver5` as the L0 dump implied; CPU tuning is via Cranelift inner settings, e.g., via Wasmtime's API for cranelift config)
- [ ] **Energy measurement**: `powerstat` or RAPL reading shows Pulse-only inference draws within reasonable range (target ~5W; verify and update if measured differently)
- [ ] **Idle test**: when no inference is running, Pulse cores 0-5 stay in low-power state; verified via `cpupower monitor`
- [ ] **Conductor wiring**: Pulse output routes into the [[e107-weaver-state-fabric|Weaver]]'s state-fabric API (gRPC or equivalent — exact protocol decided in E107)

## Scale and Model

> [!info] Epic Parameters
>
> | Parameter | Value |
> |---|---|
> | **Model** | feature-development |
> | **Quality tier** | Skyscraper |
> | **Estimated tasks** | 8-10 |
> | **Dependencies** | E101 (AVX-512 kernel), E102 (model weights storage on `tank/models`), E100 (CCD layout verified) |
> | **Feeds into** | E107 (Pulse is a producer of state input to the Weaver), E108 (Profile 1 = Pulse-only inference path) |
> | **Substrate** | CCD 0 (cores 0-5, thread mask `0xfff`); 32MB L3 local to CCD 0 |

## Handoff Context

> [!info] For a fresh context picking up this epic:
>
> - Milestone: [[sain-01-sovereign-node|Milestone — SAIN-01 Sovereign AI Node]]
> - L1 spec sections: [[src-sain-01-sovereign-node-spec|§§ 15-16 (1-bit paradigm + 512-bit fusion) + § 17.1 (Conductor Agent) + § 20 (Wasm-to-AVX-512 AOT)]]
> - L1 BitNet grounding: [[src-bitnet-b158-ternary-llm|Synthesis — BitNet b1.58]]
> - L2 ternary concept: [[concept-1bit-ternary-weights|1-bit Ternary Weights]]
> - L2 dual-CCD substrate: [[concept-dual-ccd-cache-partitioning-9900x|Dual-CCD Cache Partitioning]]
> - **Critical L0 corrections**: `BitNet-b1.58-13B` does not exist (use 2B or 3B); `WASMTIME_COMPARE_OPTIONS` is not a real env var; `wasmtime compile --target znver5` is wrong syntax (use a triple)
> - The 5-7 tok/sec figure from Microsoft is for a 100B-class CPU-only model; on 2.4B / 3B the throughput on Zen 5 should be significantly higher — record actual measurement

## Relationships

- PART OF: [[sain-01-sovereign-node|Milestone — SAIN-01 Sovereign AI Node]]
- DEPENDS ON: [[e101-sovereign-os-build|E101 — Sovereign OS Build]]
- DEPENDS ON: [[e102-zfs-storage-layout|E102 — ZFS Storage Layout]] (model weights on `tank/models`)
- DEPENDS ON: [[e100-hardware-foundation|E100 — Hardware Foundation]] (CCD layout)
- ENABLES: [[e107-weaver-state-fabric|E107 — Weaver State Fabric]] (Pulse feeds state input)
- ENABLES: [[e108-load-balancing-profiles|E108 — Load-Balancing Profiles]] (Profile 1 = Pulse + GPUs asleep)
- IMPLEMENTS: [[concept-srp-trinity-pulse-weaver-auditor|Concept — SRP Trinity (Pulse module)]]
- IMPLEMENTS: [[concept-1bit-ternary-weights|Concept — 1-bit Ternary Weights]]
- IMPLEMENTS: [[concept-dual-ccd-cache-partitioning-9900x|Concept — Dual-CCD Cache Partitioning]] (Pulse occupies CCD 0)
- IMPLEMENTS: [[src-sain-01-sovereign-node-spec|SAIN-01 Sovereign Node Spec]] §§ 15-16, 17.1, 19, 20

## Backlinks

[[sain-01-sovereign-node|Milestone — SAIN-01 Sovereign AI Node]]
[[e101-sovereign-os-build|E101 — Sovereign OS Build]]
[[e102-zfs-storage-layout|E102 — ZFS Storage Layout]]
[[e100-hardware-foundation|E100 — Hardware Foundation]]
[[e107-weaver-state-fabric|E107 — Weaver State Fabric]]
[[e108-load-balancing-profiles|E108 — Load-Balancing Profiles]]
[[Concept — SRP Trinity (Pulse module)]]
[[Concept — 1-bit Ternary Weights]]
[[Concept — Dual-CCD Cache Partitioning]]
[[SAIN-01 Sovereign Node Spec]]
[[17.1]]
[[19]]
[[20]]
[[e109-dflash-integration|E109 — DFlash Integration]]
