---
title: ZFS Tiered Storage for LLM Inference
aliases:
  - "ZFS Tiered Storage for LLM Inference"
  - "ZFS Dataset Stratification"
  - "Tiered NVMe Storage for AI Workloads"
type: concept
layer: 2
maturity: growing
domain: devops
status: synthesized
confidence: high
created: 2026-05-15
updated: 2026-05-15
sources:
  - id: src-sain-01-sovereign-node-spec
    type: wiki
    file: "wiki/sources/src-sain-01-sovereign-node-spec.md"
    title: "Synthesis — SAIN-01 Sovereign AI Node Master Specification"
  - id: openzfs-direct-io-2-2
    type: documentation
    url: "https://openzfs.org/wiki/Documentation"
    title: "OpenZFS documentation (O_DIRECT support landed in 2.2)"
tags:
  - devops
  - zfs
  - storage
  - nvme
  - llm-inference
  - dataset-stratification
  - recordsize
  - compression
  - sync-always
  - atomic-state
  - copies-2
  - sain-01
  - tank-models
  - tank-context
  - tank-agents
---

# ZFS Tiered Storage for LLM Inference

## Summary

**ZFS tiered storage for LLM inference** is the pattern of partitioning a single physical NVMe pool into multiple ZFS datasets, each tuned to a distinct access pattern — large sequential reads (model weights), small synchronous writes (state files), and balanced runtime cache (agent ephemeral data). On the [[src-sain-01-sovereign-node-spec|SAIN-01 Sovereign Node]], this manifests as three datasets on the `tank` pool: **`tank/models`** with 1M recordsize + lz4 compression + redundant metadata for 100GB+ weight files; **`tank/context`** with 16k recordsize + zstd-9 + `copies=2` + critically `sync=always` for the [[concept-srp-trinity-pulse-weaver-auditor|Trinity's state-fabric]] files; **`tank/agents`** with 128k + zstd-3 for the agents' runtime working set. The pattern matters because LLM inference workloads have **bimodal storage characteristics**: weights are streaming-sequential and benefit from big-recordsize + light compression to maximize bandwidth, while state files are small + synchronous + cannot tolerate race conditions and require completely different tuning. A naive "one dataset, default settings" approach hurts both ends — undersized recordsize on weights wastes bandwidth on FS metadata overhead; oversized recordsize on state files inflates write amplification. The tiered approach also enables differentiated durability (`copies=2` on state, single copies on weights — operators can re-download weights, can't reconstruct lost state) and differentiated compression aggressiveness (zstd-9 on small text-heavy state files, lz4 on huge binary weight files).

## Key Insights

- **LLM inference is bimodal in its storage profile.** Model weights are **streaming-sequential reads of large files** (100GB+) — bandwidth-bound, low FS-metadata overhead tolerance. State files (`CLAUDE.md`, `SOUL.md`, `IDENTITY.md`, `AGENTS.md`) are **small, frequent, synchronous writes** — durability-bound, race-condition-intolerant. Agent runtime cache is in between. One dataset can't optimize all three; tuning per-pattern unlocks all three. ([[src-sain-01-sovereign-node-spec|SAIN-01 synthesis]])

- **`tank/models` is tuned for sequential bandwidth.** 1M recordsize + lz4 compression + `atime=off` + `redundant_metadata=most`. The 1M recordsize matches the streaming access pattern of large weight files — each ZFS read reads a full 1MB block, minimizing FS-metadata trips per byte fetched. lz4 is lightweight enough that the CPU overhead is negligible vs the bandwidth saved. `atime=off` removes the per-read metadata update that would otherwise inflate writes on a read-mostly dataset. `redundant_metadata=most` keeps two copies of metadata blocks (for resilience) without doubling actual data writes. ([[src-sain-01-sovereign-node-spec|SAIN-01 synthesis]])

- **`tank/context` is tuned for atomic state durability.** 16k recordsize + zstd-9 + `copies=2` + **`sync=always`**. The 16k recordsize matches the small-file profile of the state markdown files (10-100KB each). zstd-9 is aggressive compression — these are text files where the CPU cost is worth the storage savings. `copies=2` stores two physical copies of every block on the pool (durability for irreplaceable state). **`sync=always`** is the load-bearing knob: every write is forced to physical NVMe before the syscall returns, guaranteeing that when [[concept-srp-trinity-pulse-weaver-auditor|the Weaver]] writes a state mutation, the next reader (the Pulse, another agent) sees the new state immediately — no race window. ([[src-sain-01-sovereign-node-spec|SAIN-01 synthesis]])

- **`tank/agents` is balanced runtime cache.** 128k recordsize + zstd-3 + standard durability. The 128k recordsize is a compromise — agents do mixed-size I/O (sometimes small RPC payloads, sometimes larger cached results). zstd-3 is moderately aggressive compression with low CPU cost. No `copies=2` because agent runtime state is recoverable (re-derive from the source data); the durability isn't worth doubling storage. ([[src-sain-01-sovereign-node-spec|SAIN-01 synthesis]])

- **`sync=always` is what makes inter-agent state handoffs race-free.** Standard Linux filesystems and default ZFS settings use **lazy write page-caching** — a write returns to user space when the data is in the OS page cache, not when it's on physical NVMe. If the [[concept-srp-trinity-pulse-weaver-auditor|Weaver]] writes a state update to `CLAUDE.md` and immediately transfers control to a downstream agent, the downstream agent could query the underlying block file *before* the OS kernel physically flushes the dirty cache pages. This is a real race condition — agents see stale state. Forcing `sync=always` on `tank/context` enforces synchronous write paths: each write doesn't return until the data is durably on NVMe. The downstream agent's read can't beat the write. ([[src-sain-01-sovereign-node-spec|SAIN-01 synthesis]])

- **ZFS's `O_DIRECT` semantics changed in OpenZFS 2.2.** The atomic-state-writer pattern in the SAIN-01 spec's §21 uses `O_DIRECT | O_SYNC` to bypass volatile OS page caches. Prior to OpenZFS 2.2 (released Oct 2023), the OpenZFS `O_DIRECT` implementation **silently fell back to buffered I/O** — the flag was honored syntactically but the semantic guarantee was absent. From OpenZFS 2.2+, `O_DIRECT` is properly supported with the documented semantics. The pattern's correctness depends on the OpenZFS version. ⚠️ Pin OpenZFS ≥2.2 in any SAIN-01 deployment. ([[src-sain-01-sovereign-node-spec|SAIN-01 synthesis]], openzfs-direct-io-2-2)

- **Compression aggressiveness is tuned per dataset, not globally.** lz4 (`tank/models`) is fast + light — appropriate for 100GB+ weight files where CPU overhead matters and the data is already weakly compressible (FP16/INT8 weights have low entropy in some ranges). zstd-9 (`tank/context`) is slow + aggressive — appropriate for ~10KB markdown text where storage savings matter (~2-3× on natural-language text) and the CPU cost amortizes over rare writes. zstd-3 (`tank/agents`) is balanced. A single dataset with one compression algorithm would either under-compress text (waste) or over-compress weights (slow). ([[src-sain-01-sovereign-node-spec|SAIN-01 synthesis]])

- **The ZFS RAID 0 + dataset-stratification combination is a *throughput-first*, not durability-first design.** RAID 0 striped across 2× PCIe 5.0 NVMe maximizes sequential read bandwidth (target ~31.5 GB/s per the L0 dump) at the cost of zero redundancy — single NVMe failure loses everything in the pool. `copies=2` on `tank/context` partially compensates *for the irreplaceable subset* (state files) by writing two physical copies, but it doesn't restore device-failure resilience. Operators choosing this pattern must accept that backup + off-host replication is mandatory; ZFS send/receive to a separate device is the standard remediation. ([[src-sain-01-sovereign-node-spec|SAIN-01 synthesis]])

> [!warning] No Redundancy by Default
> RAID 0 + `copies=2` on `tank/context` is NOT a replacement for backups. `copies=2` writes two block copies on the same pool — a single NVMe failure still loses both copies. Operators deploying this pattern must layer external backup (ZFS send/receive to a separate device, or off-host replication) on top. The SAIN-01 spec's choice prioritizes throughput; durability is an operator responsibility, not a ZFS feature.

## Deep Analysis

### Why one dataset can't optimize for both weights and state

ZFS recordsize tuning is one of the most consequential single-knob choices in the system. Recordsize is the unit of block allocation for a dataset; ZFS reads, writes, compresses, checksums, and cache-manages at recordsize granularity.

| Workload | Effect of small recordsize (16k) | Effect of large recordsize (1M) |
|---|---|---|
| Sequential reads of 100GB weight file | Excessive FS metadata trips; lower bandwidth; cache thrash | Minimal metadata overhead; full bandwidth; cache-coherent streaming |
| Small synchronous writes to 50KB state file | Whole-record write = 16KB; matches actual data size; ~zero waste | Whole-record write = 1MB to update 50KB → 20× write amplification; storage churn |
| Random-access lookups in mid-size files | Acceptable | Bandwidth waste — reading 1MB to access 64KB of relevant data |
| Compression efficiency | Smaller blocks → less context for compressor; worse ratios | Larger blocks → better compression ratios |

The tradeoffs invert across workloads. A single dataset must pick one operating point and accept the inefficiency on the other workload. **Two datasets pick two operating points simultaneously.**

### The state-fabric atomicity contract

The [[concept-srp-trinity-pulse-weaver-auditor|Weaver]] writes state to `tank/context` and the [[concept-srp-trinity-pulse-weaver-auditor|Pulse]] reads it from the same dataset. The atomicity contract is:

> When the Weaver completes a write to `CLAUDE.md`, any subsequent read by the Pulse MUST see the new content. Never partial. Never stale.

ZFS delivers this via the combination of:

1. **`sync=always`** at the dataset level — writes don't return until durably on NVMe.
2. **Atomic rename** at the application level — write to `CLAUDE.md.tmp`, then `rename()` it to `CLAUDE.md`. POSIX guarantees `rename()` is atomic on the same filesystem; readers either see the old file or the new file, never a half-written file.
3. **`O_DIRECT | O_SYNC`** flags on the write — bypass the OS page cache + ensure synchronous semantics at the syscall level.

The three combine. Without `sync=always`, the OS page cache can hold the write briefly. Without atomic rename, partial writes can be visible. Without `O_DIRECT | O_SYNC`, the user-space buffer flush isn't synchronized.

⚠️ The `O_DIRECT` flag is meaningless on OpenZFS <2.2 — falls back to buffered. The `sync=always` + atomic rename combination still works without `O_DIRECT`, but the cleanest version requires OpenZFS 2.2+.

### Cost accounting per dataset

A back-of-the-envelope cost breakdown for the SAIN-01 deployment:

| Dataset | Typical contents | Typical size | Compression | Effective stored size |
|---|---|---|---|---|
| `tank/models` | 5-10 quantized models, each 1-50GB | ~200-500GB raw | lz4 ~1.5× | ~130-330GB |
| `tank/context` | 4 state files + audit logs + escalations SQLite | ~50-500MB raw | zstd-9 ~3× + copies=2 | ~33-330MB (with redundancy) |
| `tank/agents` | Ephemeral agent runtime cache | varies, ~50-200GB | zstd-3 ~2× | ~25-100GB |
| **Total pool consumption** | | ~300-700GB raw | mixed | ~200-450GB on disk |

On a 2× 2TB or 2× 4TB PCIe 5.0 NVMe RAID 0 pool, this consumes 5-20% of capacity, leaving substantial headroom for growth + ZFS internal overhead (ARC + L2ARC + ZIL + snapshots).

### How this pattern composes with other SAIN-01 design choices

The dataset stratification interacts with several other SAIN-01 components:

| Component | Interaction |
|---|---|
| [[concept-srp-trinity-pulse-weaver-auditor|Trinity (Weaver)]] | The Weaver is the only writer to `tank/context`; uses the atomic-rename + sync=always pattern for every state mutation |
| [[concept-srp-trinity-pulse-weaver-auditor|Trinity (Auditor)]] | The Auditor's `security_audit.log` is on `tank/context` (append-only, written atomically) |
| [[concept-1bit-ternary-weights|Pulse + bitnet.cpp]] | Reads ternary model weights from `tank/models`; the 1M recordsize maximizes streaming throughput for the lookup-table matmul |
| [[concept-vfio-gpu-isolation-amd-iommu|VFIO RTX 3090]] | Sandboxed sub-agents on the 3090 use `tank/agents` for their runtime cache; isolated from the host's state on `tank/context` |
| [[concept-dual-ccd-cache-partitioning-9900x|Dual-CCD partition]] | The Weaver's writes happen on CCD 1 cores 6-9; ZFS compression threads run on cores 10-11 to avoid cross-CCD contention |
| Network split | Marvell 10GbE pulls weights from local NAS into `tank/models`; Intel 2.5GbE handles management traffic (no weight transit) |

The stratification is a system-level design choice, not just a storage tuning. Changing the dataset properties without considering these interactions can silently break a Trinity contract.

### Failure modes + remediation

| Failure | Mechanism | Mitigation |
|---|---|---|
| Single NVMe device failure | RAID 0 = zero redundancy | External ZFS send/receive snapshots; off-host replication |
| `tank/context` corruption | Bit rot or controller error | `copies=2` provides on-pool redundancy; scrubs catch corruption early |
| Stale-state race on agent handoff | Default `sync=standard` allows page-cache hold | `sync=always` (as specified); verify in deployment |
| `O_DIRECT` silently buffered | OpenZFS <2.2 | Pin OpenZFS ≥2.2; verify with `zfs --version` |
| Write amplification on `tank/context` | Recordsize too large for small files | 16k recordsize (as specified) — matches actual file sizes |
| Bandwidth ceiling on weights | Recordsize too small / metadata overhead | 1M recordsize + lz4 + `atime=off` (as specified) |
| `tank/agents` cache spill | Ephemeral data fills the dataset | Operator monitors via `zfs list`; sets quota if needed; cleans periodically |

## Open Questions

- The L0 dump targets RAID 0 for throughput, but doesn't specify any backup posture. ZFS send/receive to a second device, off-host replication, or both — what's the operator's chosen durability strategy for irreplaceable `tank/context` state? (Requires: operator decision; would land as an L6 decision page on backup posture.)
- ARC tuning is mentioned (`zfs_arc_max=137438953472` = 128GB of the 256GB total system memory) — does this leave enough RAM for the Trinity's actual workloads (model weights, agent runtimes, KV caches)? The 128GB allocation is aggressive. (Requires: empirical sizing on the production workload.)
- L2ARC + ZIL placement — does the dump's 2-NVMe RAID 0 leave room for L2ARC (read cache) or ZIL (write log) on a separate device? The current spec doesn't address either. (Requires: L2ARC/ZIL design decision.)
- Snapshots cadence — for `tank/context` specifically, what's the snapshot frequency? Hourly? Per-state-mutation? Each option has cost/benefit trade-offs. (Requires: snapshot policy decision.)
- ZFS encryption — for off-host backup, native ZFS encryption is the cleanest path. The SAIN-01 spec doesn't address whether the pool is encrypted. (Requires: encryption decision; security-relevant.)
- Does the dataset stratification compose cleanly with Podman's storage drivers? The dump mentions Podman's graph driver mapping to a `tank/containers` dataset (not in the three-dataset plan) — needs explicit ZFS-driver configuration to align block sizes. (Requires: Podman + ZFS integration verification.)

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **What writes here?** | [[concept-srp-trinity-pulse-weaver-auditor\|SRP Trinity (Weaver writes state, Auditor writes audit log)]] |
> | **What reads weights from here?** | [[concept-1bit-ternary-weights\|1-bit Ternary Weights]] (Pulse reads bitnet.cpp models from `tank/models`) |
> | **CPU pinning for I/O threads** | [[concept-dual-ccd-cache-partitioning-9900x\|Dual-CCD Cache Partitioning]] (ZFS compression on cores 10-11) |
> | **Container storage on `tank/agents`** | [[concept-vfio-gpu-isolation-amd-iommu\|VFIO GPU Isolation]] (sandboxed agent fleet's runtime cache lives here) |
> | **Source synthesis** | [[src-sain-01-sovereign-node-spec\|SAIN-01 Sovereign Node Spec]] (§§ 3, 4.1, 7.2, 21) |

## Relationships

- DERIVED FROM: [[src-sain-01-sovereign-node-spec|SAIN-01 Sovereign Node Spec]] (§§ 3, 4.1, 7.2, 21)
- IMPLEMENTS: ZFS dataset stratification by workload access pattern
- ENABLES: [[concept-srp-trinity-pulse-weaver-auditor|SRP Trinity]] (the Weaver's atomic state-handoff contract; the Auditor's append-only audit log)
- USED BY: [[concept-1bit-ternary-weights|1-bit Ternary Weights]] (model weights stored on `tank/models`)
- USED BY: [[concept-vfio-gpu-isolation-amd-iommu|VFIO GPU Isolation]] (sandboxed agents' runtime cache on `tank/agents`)
- CONSTRAINED BY: OpenZFS version (`O_DIRECT` semantics; ≥2.2 required for the atomic-state pattern's clean implementation)
- CONSTRAINS: Backup posture (RAID 0 = no native redundancy; external backup mandatory)
- RELATES TO: [[infrastructure-as-code-patterns|Infrastructure as Code Patterns]] (ZFS dataset properties as declarative state)

## Backlinks

(will be populated by `tools/obsidian.py backlinks` after pipeline post)
