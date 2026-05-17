---
title: Dual-CCD Cache Partitioning (Zen 5 9900X)
aliases:
  - "Dual-CCD Cache Partitioning (Zen 5 9900X)"
  - "Dual-CCD Topology"
  - "Infinity Fabric Crossing"
  - "CCD-Aware Scheduling"
type: concept
layer: 2
maturity: growing
domain: devops
status: synthesized
confidence: high
created: 2026-05-15
updated: 2026-05-15
sources:
  - id: src-zen5-avx512-single-cycle
    type: wiki
    file: "wiki/sources/src-zen5-avx512-single-cycle.md"
    title: "Synthesis — AMD Zen 5 Single-Cycle 512-bit AVX-512 and Dual-CCD Topology"
  - id: src-sain-01-sovereign-node-spec
    type: wiki
    file: "wiki/sources/src-sain-01-sovereign-node-spec.md"
    title: "Synthesis — SAIN-01 Sovereign AI Node Master Specification"
tags:
  - devops
  - cpu
  - amd
  - zen5
  - ryzen-9-9900x
  - ccd
  - dual-ccd
  - infinity-fabric
  - l3-cache
  - core-pinning
  - taskset
  - numa
  - sain-01
  - cache-locality
  - srp
---

# Dual-CCD Cache Partitioning (Zen 5 9900X)

## Summary

The **AMD Ryzen 9 9900X** uses a dual-CCD (Core Complex Die) layout: 12 cores split as 2 × 6-core CCDs, each with **its own isolated 32MB L3 cache**, connected by AMD Infinity Fabric. **Dual-CCD cache partitioning** is the technique of pinning workloads to a single CCD so their hot data stays in that CCD's local L3 cache — avoiding the cross-CCD Infinity Fabric crossing penalty (~8-10× slower than local L3 access). On the [[src-sain-01-sovereign-node-spec|SAIN-01 Sovereign Node]], this technique maps the [[concept-srp-trinity-pulse-weaver-auditor|SRP Trinity]] to physical hardware: **The Pulse pinned to CCD 0 cores 0-5** (thread mask `0xfff`) for AVX-512 ternary inference; **The Weaver + Auditor pinned to CCD 1 cores 6-9** (mask `0xff000`) for state-engine + Tetragon stream parsing; **kernel/IRQ/ZFS-compression** on cores 10-11 (mask `0xf00000`). The technique matters because the [[concept-1bit-ternary-weights|Pulse module's ternary-LUT matmul]] working set fits comfortably in CCD 0's 32MB L3 — but spilling cache traffic across the fabric would erase the [[src-zen5-avx512-single-cycle|single-cycle 512-bit AVX-512]] performance win. The dual-CCD partition is not a tuning optimization; it's the difference between cache-hot inference and cache-thrash inference for the SAIN-01 workload profile.

## Key Insights

- **9900X is 2× CCDs of 6 cores each, with 2× 32MB L3 (one per CCD, NOT shared).** This is the structural topology. Each CCD has its own complete cache hierarchy (L1d + L1i + L2 + L3) and its own connection to the Infinity Fabric. Cores within the same CCD share L3 transparently; cores in different CCDs do not. ([[src-zen5-avx512-single-cycle|Zen 5 synthesis]])

- **Cross-CCD memory access goes through Infinity Fabric.** When a thread on CCD 0 accesses data resident in CCD 1's L3 (or vice versa), the request traverses the IF, hits the remote CCD's cache controller, and returns. Independent third-party measurements (Phoronix, Chipsandcheese, AnandTech-style reviews) show this round-trip at **~80-120 nanoseconds** — vs **~10-15 ns** for a local L3 hit. The latency multiplier is **~8-10×**. ([[src-zen5-avx512-single-cycle|Zen 5 synthesis]])

- **Cache-resident workloads see massive degradation under cross-CCD scheduling.** A workload whose working set fits in one CCD's 32MB L3 (the typical inference path for a ternary 2-3B model with its activations) runs near-peak when pinned to that CCD. The same workload, when scheduled across both CCDs, suffers continuous L3 misses + IF crossings — measurably worse than even a single-CCD topology would have been. This is the core motivation for explicit CCD pinning. ([[src-zen5-avx512-single-cycle|Zen 5 synthesis]], [[src-sain-01-sovereign-node-spec|SAIN-01 synthesis]])

- **The SRP Trinity maps cleanly to the dual-CCD partition.** Three responsibilities, three core-mask regions: **The Pulse** on cores 0-5 (CCD 0 entirely — vector pipeline gets the full 6 cores + 32MB local L3); **The Weaver + Auditor** on cores 6-9 (4 cores of CCD 1 — state engine + Tetragon parsing); **System host / kernel / IRQ / ZFS-compression** on cores 10-11 (2 cores of CCD 1 — isolated from Trinity work). The mask values: Pulse `0xfff`, Weaver `0xff000`, Host `0xf00000`. ([[src-sain-01-sovereign-node-spec|SAIN-01 synthesis]])

- **Pinning is enforced via `taskset` (process-level) or systemd `CPUAffinity=` (service-level).** `taskset -c 0-5 bitnet-cli ...` launches the Pulse runtime pinned to CCD 0. Systemd unit files can use `CPUAffinity=0-5` to enforce the same at the service level. The kernel scheduler respects these constraints; a properly-pinned process never migrates off its assigned CCD. ([[src-sain-01-sovereign-node-spec|SAIN-01 synthesis]])

- **The 9900X's choice over the 9950X is microarchitecture-driven, not core-count-driven.** The 9950X (16C/32T) has 2× CCDs of 8 cores each, same L3 layout. For the SAIN-01 SRP partition (Pulse needs 6 cores, Weaver+Auditor need ~4, host needs ~2), the 9900X's 12 cores are sufficient. The 9950X's extra cores don't reshape the partition; the microarchitectural properties (single-cycle 512-bit AVX-512, dual-CCD, AVX-VNNI) are identical. Picking the 9900X saves cost without compromising the architectural choice. ([[src-zen5-avx512-single-cycle|Zen 5 synthesis]])

- **The 9900X is the minimum dual-CCD Zen 5 part for this SRP topology.** The 9700X (8C, single CCD) cannot deliver the spatial separation between Pulse and Weaver+Auditor. The 9600X (6C, single CCD) is also off the table. Anything below 9900X loses the dual-CCD property — the SRP partition becomes purely logical (core groups), not physical (separate cache hierarchies). Loses most of the win. ([[src-zen5-avx512-single-cycle|Zen 5 synthesis]])

- **Single-thread peak boost is asymmetric across CCDs.** Independent reviews of the 9900X show one CCD boost-clocks slightly higher than the other (the "preferred CCD" or "CPPC2 favored CCD"). Linux exposes this via the `cppc` cpufreq driver — single-thread workloads are preferentially scheduled on the faster CCD. For the SAIN-01 layout this is consequential: if CCD 0 happens to be the faster CCD, the Pulse gets the higher clocks; if CCD 1, the Weaver does. The operator may want to verify via `cat /sys/devices/system/cpu/cpufreq/policy*/cpuinfo_max_freq` post-deployment which CCD got the favored die. ([[src-zen5-avx512-single-cycle|Zen 5 synthesis]])

> [!success] Cache-Hot vs Cache-Thrash — A Categorical Difference
> A workload pinned to a single CCD whose working set fits in its 32MB L3 runs at cache-hot speed (~10-15 ns per L3 hit). The same workload scheduled across both CCDs runs at cache-thrash speed (~80-120 ns per cross-CCD access). For a tight inference loop hitting L3 thousands of times per token, this is the difference between sub-millisecond and multi-millisecond per-token latency. The dual-CCD partition is the architectural choice that puts the SAIN-01 in the cache-hot regime by design.

## Deep Analysis

### Why dual-CCD exists (and what it costs)

AMD's Zen 5 desktop parts use chiplet design — multiple silicon dies packaged together. The Ryzen 9 9900X comprises:

- 2× CCD (Core Complex Die) — each contains 6 cores + their full cache hierarchy (L1d 48KB/core, L1i 32KB/core, L2 1MB/core, L3 32MB shared by the 6 cores in that CCD)
- 1× I/O Die — memory controllers, PCIe controllers, integrated graphics, Infinity Fabric hub

The chiplet design has real benefits — better yields, cheaper manufacturing, easier core-count scaling. The cost is that **the two CCDs cannot share L3 cache directly**. They each have their own. Cross-CCD memory coherency goes through the IO die's Infinity Fabric, which is fast but not free.

The 9950X (16C/32T) uses the same dual-CCD pattern with 8-core CCDs. The 9700X (8C/16T) and 9600X (6C/16T) use single-CCD designs — no cross-CCD penalty because there's no cross. The 9900X sits in the sweet spot for the SAIN-01 architecture: dual-CCD (for SRP partition) but with the smallest cost.

### Measured cross-CCD latency

Independent reviewer measurements (Chipsandcheese, AnandTech, ServeTheHome, in the Zen 4 / Zen 5 era — the IF latencies are similar):

| Operation | Typical latency on 9900X |
|---|---|
| L1d hit (same core) | ~4 cycles (~0.9 ns at 4.7 GHz base) |
| L2 hit (same core) | ~14 cycles (~3 ns) |
| L3 hit (same CCD, different core) | ~50-60 cycles (~10-13 ns) |
| L3 miss → memory (same CCD) | ~250+ cycles (~55 ns) |
| **Cross-CCD L3 access** | **~360-560 cycles (~80-120 ns)** |
| Cross-CCD memory miss | ~600+ cycles (~130+ ns) |

The cross-CCD L3 access is roughly 7-10× the same-CCD L3 access. For workloads that hit L3 thousands of times per token (inference loops with their activation working sets), the difference dominates the latency budget.

### Working sets and cache footprints — does it fit?

The crucial question for the SAIN-01 architecture: **does the Pulse module's working set fit in CCD 0's 32MB L3?**

A back-of-the-envelope estimate for a 3B-parameter ternary BitNet model running via `bitnet.cpp`:

| Component | Approximate size |
|---|---|
| Layer weights (active layer, 2-bit packed ternary) | ~5-30 MB per layer (depends on layer width) |
| Activation buffer (one layer's outputs, INT8) | ~1-3 MB |
| KV cache (one layer's K + V, INT8 or fp8) | ~1-5 MB per layer per sequence |
| Lookup tables for LUT-matmul | ~256 KB |
| Code + working buffers | ~few MB |
| **Per-layer hot working set** | **~10-40 MB** |

For most layers of a 3B model, the per-layer working set fits in 32MB L3 with margin. The bitnet.cpp execution pattern is layer-by-layer: only one layer's weights are hot at a time. The cache locality story is favorable.

For larger models (Llama3-8B-1.58, 8B parameters), individual layer sizes grow; some layers may spill out of 32MB and have to refetch from RAM. This is a graceful degradation — memory bandwidth becomes the bottleneck, but no cross-CCD penalty is introduced. The Pulse stays on CCD 0.

For very large models (a hypothetical 30B+ ternary, not yet released), the per-layer working set might routinely exceed 32MB. At that point, the Pulse-on-CCD-0 pinning still wins (avoids the cross-CCD penalty on top of the memory penalty), but the absolute throughput is bottlenecked by RAM bandwidth rather than L3.

### The Weaver's cache footprint is smaller

The [[concept-srp-trinity-pulse-weaver-auditor|Weaver + Auditor]] on CCD 1 cores 6-9 has a different access pattern:

- State files (`CLAUDE.md`, `SOUL.md`, etc.) — ~10-100 KB each; fits in L1d
- Tetragon event stream parsing — small JSON parsing, sub-MB working set
- gRPC routing — small payloads, sub-MB
- ZFS metadata access — handled by kernel threads on CCD 1 cores 10-11

The Weaver doesn't stress L3. The benefit of CCD 1 placement is **isolation from the Pulse's L3 traffic** — by keeping the Weaver on its own CCD, the Pulse's 32MB working set doesn't get evicted by Weaver activity (or vice versa).

### Why kernel+ZFS on cores 10-11 of CCD 1, not CCD 0

The choice to place kernel + IRQ + ZFS-compression on cores 10-11 (CCD 1) rather than CCD 0 is deliberate:

- **CCD 0 stays exclusive to the Pulse** — the highest-latency-sensitive Trinity module gets uncontended L3 access. No kernel interrupts evicting bitnet.cpp's working set.
- **CCD 1's last 2 cores absorb everything else** — kernel work, Marvell 10GbE driver, ZFS compression threads. These can tolerate occasional L3 eviction; their workloads are throughput-oriented (network bandwidth, compression), not latency-oriented.
- **The Weaver on cores 6-9 of CCD 1** is somewhat exposed to kernel-induced L3 pressure, but its working set is small enough (sub-MB) that this is acceptable.

The partition trades fully-uncontested CCD 0 (Pulse benefits) for slightly-contested CCD 1 (Weaver tolerates) — net win.

### Verifying the partition at boot

Operator verification commands:

```bash
# Identify CCD topology
lscpu --extended=CPU,CORE,SOCKET,NODE,L1d,L1i,L2,L3
# Look for CPUs sharing the same L3 ID → those are in the same CCD.

# Verify cache sizes
cat /sys/devices/system/cpu/cpu0/cache/index3/size   # Expect ~32M
cat /sys/devices/system/cpu/cpu6/cache/index3/size   # Expect ~32M

# Check CPPC2 favored CCD
for i in 0 6; do
  echo -n "core ${i}: "
  cat /sys/devices/system/cpu/cpufreq/policy${i}/cpuinfo_max_freq
done
# Higher freq = favored CCD = should host the most latency-sensitive workload.

# Inspect IF (Infinity Fabric) clock
cat /sys/class/hwmon/hwmon*/freq*_input  # Approx; depends on hardware
```

The `friction-audit` script in the SAIN-01 spec is the equivalent boot-time check — verifies that the topology is what it should be before any Trinity service starts.

### Composition with other SAIN-01 design elements

| Component | Interaction with dual-CCD partition |
|---|---|
| [[concept-1bit-ternary-weights|1-bit Ternary Weights]] | Pulse runs ternary inference on CCD 0; working set fits in 32MB L3 for 3B-8B models |
| [[concept-srp-trinity-pulse-weaver-auditor|SRP Trinity]] | Each module pinned to its own CCD region; SRP boundary = CCD boundary |
| [[concept-zfs-tiered-storage-llm-inference|ZFS Tiered Storage]] | ZFS compression threads on cores 10-11 (CCD 1) to avoid Pulse contention |
| [[concept-vfio-gpu-isolation-amd-iommu|VFIO GPU Isolation]] | GPUs are PCIe-attached, not CCD-attached; partition is orthogonal |
| Network split | Marvell 10GbE driver IRQs typically pinned to CCD 1 cores 10-11 |
| Tetragon eBPF | Tetragon's kernel-space work happens wherever the syscall originates; user-space `guardian-core` daemon stays on CCD 1 |

## Open Questions

- Does the 9900X's preferred-CCD assignment (which die boosts higher) consistently align with the SAIN-01 spec's choice of CCD 0 for the Pulse? If CCD 1 happens to be the favored die, does the operator want to swap the partition (Pulse → cores 6-11, Weaver → cores 0-3, host → cores 4-5)? (Requires: per-deployment verification post-boot.)
- For workloads where the Pulse's working set exceeds 32MB (larger ternary models), is there benefit to spilling controlled cross-CCD prefetch? Hard to do without sophisticated thread scheduling. (Requires: research on cross-CCD prefetch hint patterns.)
- How does the dual-CCD partition interact with hyperthreading (SMT)? The 9900X has SMT enabled by default (12C/24T). If the Pulse should NOT share its physical cores with other work, SMT may need to be disabled — at the cost of halving the effective Pulse thread count. (Requires: empirical SMT-on-vs-off benchmark on the Pulse workload.)
- Power management — does `cpupower frequency-set -g performance` keep both CCDs at full boost simultaneously, or does it asymmetrically downclock the unused CCD? Relevant for the Weaver's responsiveness when the Pulse is mid-workload. (Requires: power-governor tuning + measurement.)
- The SAIN-01 spec's thread masks (`0xfff` / `0xff000` / `0xf00000`) count SMT threads, not physical cores. The 9900X has 12 cores × 2 threads = 24 logical threads, hence the 24-bit masks. If SMT is disabled, the masks need recomputation (`0x3f` / `0x3c0` / `0xc00`). (Requires: spec clarification on SMT policy.)
- Cross-CCD coherency under heavy NUMA-style access patterns — does the Weaver's frequent reads of `tank/context` state from disk-side caches incur cross-CCD penalties when ZFS compression on cores 10-11 was the last to touch them? (Requires: cache-line ping-pong analysis.)

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **What runs on CCD 0** | [[concept-1bit-ternary-weights\|1-bit Ternary Weights]] (Pulse's ternary inference) |
> | **What runs on CCD 1** | [[concept-srp-trinity-pulse-weaver-auditor\|SRP Trinity (Weaver + Auditor)]] |
> | **Why this microarchitecture** | [[src-zen5-avx512-single-cycle\|Zen 5 single-cycle 512-bit AVX-512]] |
> | **What lives outside CCDs** | [[concept-vfio-gpu-isolation-amd-iommu\|VFIO GPU Isolation]] (GPUs are PCIe-attached) |
> | **ZFS compression threads on CCD 1** | [[concept-zfs-tiered-storage-llm-inference\|ZFS Tiered Storage]] |

## Relationships

- DERIVED FROM: [[src-zen5-avx512-single-cycle|Zen 5 AVX-512 single-cycle datapath]] (CCD topology details)
- DERIVED FROM: [[src-sain-01-sovereign-node-spec|SAIN-01 Sovereign Node Spec]] (§ 19 partition strategy)
- IMPLEMENTS: CCD-aware thread pinning for cache-locality preservation
- ENABLES: [[concept-srp-trinity-pulse-weaver-auditor|SRP Trinity]] (physical realization of the software SRP boundary)
- ENABLES: [[concept-1bit-ternary-weights|1-bit Ternary Weights]] (Pulse's L3-resident inference path)
- CONSTRAINED BY: SMT policy (thread masks change if SMT is disabled)
- RELATES TO: [[concept-zfs-tiered-storage-llm-inference|ZFS Tiered Storage]] (compression threads sit on the partition's host cores)

## Backlinks

[[Zen 5 AVX-512 single-cycle datapath]]
[[SAIN-01 Sovereign Node Spec]]
[[CCD-aware thread pinning for cache-locality preservation]]
[[SRP Trinity]]
[[concept-1bit-ternary-weights|1-bit Ternary Weights]]
[[SMT policy (thread masks change if SMT is disabled)]]
[[ZFS Tiered Storage]]
