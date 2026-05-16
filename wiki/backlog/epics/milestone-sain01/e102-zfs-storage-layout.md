---
title: E102 — ZFS Storage Layout
aliases:
  - "E102 — ZFS Storage Layout"
  - "E102 — Tiered ZFS Datasets + ARC Tuning"
type: epic
domain: backlog
status: draft
priority: P0
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
  - id: concept-zfs-tiered-storage-llm-inference
    type: wiki
    file: "wiki/domains/devops/concept-zfs-tiered-storage-llm-inference.md"
tags: [epic, sain-01, zfs, storage, nvme, raid-0, recordsize, sync-always, arc, openzfs]
---

# E102 — ZFS Storage Layout

## Summary

Initialize the ZFS pool on the 2× PCIe 5.0 NVMe devices in **RAID 0** for throughput (target ~31.5 GB/s sequential read) and create three datasets tuned per access pattern: **`tank/models`** (1M recordsize + lz4 + `atime=off` + `redundant_metadata=most`) for 100GB+ weight files; **`tank/context`** (16k recordsize + zstd-9 + **`copies=2`** + **`sync=always`** + `primarycache=all` + `logbias=latency`) for the state-fabric files; **`tank/agents`** (128k recordsize + zstd-3) for sub-agent runtime cache. Clamp ARC to 128 GB via the `zfs-arc-tune.service` systemd unit (leaving 128 GB of the 256 GB total system memory free for inference workloads). **Critical version pin**: OpenZFS ≥2.2 — older versions silently fall back to buffered I/O when `O_DIRECT` is requested, breaking the atomic-state-writer pattern E107 depends on. The RAID 0 + `copies=2` combination is **throughput-first, not redundancy-first**; the operator must layer external backup (ZFS send/receive to a separate device, or off-host replication) as part of E102's completion criteria.

## Operator Directive

> "we do this right all the way"

## Goals

See Done When criteria — each is a verifiable storage-layer checkpoint.

## Done When

- [ ] **OpenZFS ≥2.2 installed + verified** via `zfs --version` — must be 2.2 or newer for proper `O_DIRECT` support
- [ ] **`zpool create` succeeds** with `ashift=12 -O compression=lz4 -m none tank /dev/nvme0n1 /dev/nvme1n1`
- [ ] **`tank/models` dataset created** with: `recordsize=1M`, `compression=lz4`, `atime=off`, `redundant_metadata=most`, `mountpoint=/mnt/vault/models`
- [ ] **`tank/context` dataset created** with: `recordsize=16k`, `compression=zstd-9`, `copies=2`, `sync=always`, `primarycache=all`, `logbias=latency`, `mountpoint=/mnt/vault/context`
- [ ] **`tank/agents` dataset created** with: `recordsize=128k`, `compression=zstd-3`, `mountpoint=/mnt/vault/agents`
- [ ] **ARC clamp configured** via `zfs-arc-tune.service` — `ExecStart=/sbin/modprobe zfs zfs_arc_max=137438953472`; service runs `Before=zfs-mount.service`
- [ ] **`zpool status tank`** shows healthy; both NVMe devices online; no errors
- [ ] **`zfs list`** confirms all three datasets present with correct mount points
- [ ] **`arcstat -s c`** shows ARC clamped to exactly 137438953472 bytes (128 GB)
- [ ] **Pool throughput baseline measured** — `dd if=/dev/zero of=/mnt/vault/models/test.bin bs=1M count=10000 oflag=direct` or `fio` benchmark; record observed peak sequential write/read; document as the throughput baseline for future regression testing
- [ ] **Backup posture decided + documented**: operator chooses one or both of (a) ZFS send/receive cron job to a second physical device, (b) off-host replication via `syncoid` or `znapzend`; configuration deployed
- [ ] **Snapshot policy decided + documented**: cadence for `tank/context` (hourly? per-mutation?); retention policy; cleanup script if needed
- [ ] **`friction-audit` extended** to include `zpool status -x` check (delivered by E101's script; this epic verifies it covers ZFS)
- [ ] **Empty-file atomic-rename test passes**: write to `tank/context/test.tmp`, `rename()` to `tank/context/test`, immediate read — content matches; no torn write observed across 1000 iterations

## Scale and Model

> [!info] Epic Parameters
>
> | Parameter | Value |
> |---|---|
> | **Model** | feature-development |
> | **Quality tier** | Skyscraper — storage corruption is unrecoverable; verify everything |
> | **Estimated tasks** | 6-8 (pool creation + 3 datasets + ARC + backup posture + benchmark + atomic-rename test) |
> | **Dependencies** | E101 (OS booted with ZFS-DKMS loaded) |
> | **Feeds into** | E104 (Auditor audit log on tank/context), E106 (Pulse reads model weights from tank/models), E107 (Weaver writes state to tank/context with sync=always), E108 (Profile YAML on tank/agents), E109/E110 (model weights for DFlash + catalog) |
> | **Critical caveat** | OpenZFS 2.2+ for `O_DIRECT`; RAID 0 has no native redundancy — backup layer mandatory |

## Handoff Context

> [!info] For a fresh context picking up this epic:
>
> - Read the milestone: [[sain-01-sovereign-node|Milestone — SAIN-01 Sovereign AI Node]]
> - Read the storage section: [[src-sain-01-sovereign-node-spec|§ 3 Storage Architecture]] + [[src-sain-01-sovereign-node-spec|§ 4.1 ZFS Storage Tuning Matrix]] + [[src-sain-01-sovereign-node-spec|§ 7.2 ZFS Transactional Optimizations]]
> - Read the concept: [[concept-zfs-tiered-storage-llm-inference|ZFS Tiered Storage for LLM Inference]] — explains why the three datasets exist
> - **Critical**: OpenZFS version must be ≥2.2 for the `O_DIRECT` semantics. Older versions silently buffer; E107's atomic-state-writer pattern depends on this.
> - **RAID 0 = zero device-failure tolerance.** `copies=2` writes two block copies on the same pool — still loses both copies on NVMe failure. External backup is mandatory, not optional.

## Relationships

- PART OF: [[sain-01-sovereign-node|Milestone — SAIN-01 Sovereign AI Node]]
- DEPENDS ON: [[e101-sovereign-os-build|E101 — Sovereign OS Build]]
- ENABLES: [[e104-tetragon-guardian-perimeter|E104 — Tetragon + Guardian Perimeter]] (audit log on tank/context)
- ENABLES: [[e106-pulse-vector-runtime|E106 — Pulse Vector Runtime]] (model weights on tank/models)
- ENABLES: [[e107-weaver-state-fabric|E107 — Weaver State Fabric]] (state files on tank/context sync=always)
- ENABLES: [[e108-load-balancing-profiles|E108 — Load-Balancing Profiles]] (profile YAML on tank/agents)
- ENABLES: [[e110-model-catalog|E110 — Model Catalog]] (model weights on tank/models)
- IMPLEMENTS: [[src-sain-01-sovereign-node-spec|SAIN-01 Sovereign Node Spec]] §§ 3, 4.1, 7.2
- BUILDS ON: [[concept-zfs-tiered-storage-llm-inference|Concept — ZFS Tiered Storage for LLM Inference]]

## Backlinks

(will be populated by `tools/obsidian.py backlinks` after pipeline post)
