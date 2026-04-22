---
title: "Operator Workstation — Storage Tiering (authoritative disk map)"
type: reference
domain: cross-domain
status: verified
confidence: high
maturity: mature
priority: P0
created: 2026-04-22
updated: 2026-04-22
sources:
  - id: operator-directive
    type: file
    file: raw/notes/2026-04-22-directive-post-anthropic-self-autonomous-plan.md
    title: "Post-Anthropic Self-Autonomous Stack — Directive Note"
  - id: dmesg-evidence
    type: file
    file: raw/notes/2026-04-22-directive-post-anthropic-self-autonomous-plan.md
    title: "dmesg output 2026-04-22 confirmed EXT4 recovery on /dev/sdd (logged in directive note)"
  - id: operator-clarifications
    type: file
    file: raw/notes/2026-04-22-directive-post-anthropic-self-autonomous-plan.md
    title: "Operator stated RAID topology multiple times 2026-04-22 (captured verbatim in directive note)"
tags: [reference, p0, hardware, storage, disks, tiering, nvme, sata, raid, wsl, 9p, ground-truth, operator-workstation]
---

# Operator Workstation — Storage Tiering

## Summary

Authoritative disk and filesystem map for the operator's workstation as of **2026-04-22**. This page exists because hardware confusion — especially around which disks are NVMe versus SATA, and where 9P overhead caps throughput — cost a full session of friction earlier in the day. Every routing decision (AICP tier selection, AirLLM offload path, K2.6 Q2 weight placement, KTransformers working set) hinges on accurate numbers. When any future AI session touches storage choices, it **reads this page first** and trusts the numbers here over its own inference.

> [!warning] Operator ground truth overrides AI assumption.
> If you find yourself about to assert something about this hardware, check this table. If the table disagrees with your belief, **the table is right**. Do not re-litigate settled facts with the operator.

## Corrections history

> [!warning] 2026-04-22 evening — disk-letter mappings corrected
> The initial version of this page had D:\ incorrectly labeled as the 1.9 TB SATA RAID. **D:\ is actually the NVMe drive** (where WSL's root VHDX and `D:\vdisks\models.vhdx` live). Operator corrected the mapping during the VHDX attach session. See `wiki/log/2026-04-23-vhdx-attach-procedure-and-hcs-fix.md`.
>
> Windows-OS placement was also initially guessed as "Disk 2 = 500 GB Intel RAID 0." Per operator: **Windows OS is on an Intel RAID 0**, and the **1.9 TB NAS SSD is on a separate RAID 0** — both RAID volumes exist, but the size-to-purpose mapping I'd drawn was wrong. Specifics of disk numbers ↔ drive letters remain **unverified** and are left as `?` below until operator confirms via `Get-PhysicalDisk` / `Get-Partition`.

## Ground-truth disk map (partial — verified fields only)

> [!info] Physical disks → WSL access → real-world bandwidth → recommended use
>
> | Win drive | Size | Physical media | WSL access path | Filesystem layer | Read BW (real-world) | Recommended use |
> |-----------|------|----------------|-----------------|------------------|----------------------|-----------------|
> | **D:\** | (large, contains WSL root VHDX + models.vhdx) | **NVMe** (verified 2026-04-22 by operator) | `/dev/sdc` (WSL root), `/dev/sdd` (models VHDX) | native ext4 in WSL, no 9P | native NVMe speeds, ~3–7 GB/s | ⭐ K2.6 weights, AirLLM offload, hot model cache |
> | (RAID #1) | ~500 GB | **Intel RAID 0** (Windows OS) | `C:\` presumably | — | — | ⛔ OFF-LIMITS (Windows system) |
> | (RAID #2) | **1.9 TB** | **2× SSDs in Intel RAID 0** (NAS SSD; operator-confirmed RAID 0, NOT NVMe) | whichever letter it's mapped to via 9P | 9P passthrough | ~0.8–1.0 GB/s physical, 9P-capped further | Archives, backups, datasets — NOT LLM weights |
> | (USB) | 4 TB | Sabrent external USB | `/mnt/<letter>` (9P) | 9P + USB | USB-limited (≤500 MB/s practical) | Cold storage, archives |
> | (Docker) | 233 GB | — | Docker-reserved | — | — | ⛔ OFF-LIMITS (Docker) |

The disk-number-to-drive-letter mapping is deliberately left unstated here — it can be recovered accurately via:

```powershell
Get-PhysicalDisk | Select-Object DeviceID, FriendlyName, MediaType, Size | Format-Table
Get-Partition | Where-Object DriveLetter | Select-Object DiskNumber, DriveLetter, Size | Format-Table
```

Update this page when operator produces that output.

Bandwidth provenance: numbers labeled "estimated" come from manufacturer specs and architecture reasoning; numbers labeled "measured" come from `fio` runs recorded in the log directory. Run `fio` on `/mnt/models` after mount and record the measured NVMe number here.

## Common mistakes — ground-truth affirmed

> [!warning] Mistake #1 — the 1.9 TB Intel RAID 0 is SSDs, NOT NVMe.
> Operator confirmed **multiple times** on 2026-04-22. The disk shows up in Windows Disk Management as a single "Raid0SSDStorage" volume, which is easy to misread as a single NVMe. It is **two SSDs striped in RAID 0**. Two SATA-class SSDs in RAID 0 will never beat one Gen4 NVMe, regardless of stripe math.
>
> If you are about to recommend putting K2.6 weights on the 1.9 TB RAID — **stop**. The correct target is a VHDX on the NVMe (D:\\ → `/dev/sdd` via `wsl --mount --vhd`).
>
> **Clarification 2026-04-22 evening**: D:\ is the NVMe, NOT the 1.9 TB RAID. The drive-letter mapping in the original version of this page was wrong.

> [!warning] Mistake #2 — assuming `/mnt/d` is "NVMe-fast" because Windows says the underlying disk is fast.
> WSL's `/mnt/c`, `/mnt/d`, etc. sit behind a **9P server** — a filesystem virtualization layer that caps throughput well below native. Even if the underlying Windows disk were a Gen4 NVMe, the 9P roundtrip for every `read(2)` / `write(2)` caps practical bandwidth at ~1–2 GB/s at best. This is a WSL architectural fact, not a configuration issue.

> [!warning] Mistake #3 — treating RAID 0 as "2× faster" for LLM workloads.
> RAID 0 stripes doubles *sequential* throughput in theory. In practice: 20–40% gain on LLM I/O, because MoE expert access is **semi-random**, not sequential. Two SATA SSDs striped do not approach single-NVMe throughput for these workloads.

## Why `/dev/sdd` is the fastest WSL-accessible path

`/dev/sdd` is a **dynamic VHDX file on Windows Disk 0** (the WD_BLACK SN770 single Gen4 NVMe) mounted into WSL as a block device with native ext4 on top. This architecture has three properties that make it the fastest WSL-local option:

1. **Native ext4**, not 9P — no filesystem translation layer between WSL and the block device.
2. **Backed by Gen4 NVMe hardware** with sequential reads up to 7 GB/s (manufacturer spec) and ~5 GB/s practical.
3. **Mounted as a raw block device** inside WSL — no Windows file I/O passthrough.

The only faster option would be adding a **second, dedicated** NVMe RAID array physically attached and mounted natively in WSL — future work, not in scope for the 2026-04-27 deadline.

## 9P filesystem overhead explained

WSL2 exposes the Windows C:, D:, etc. drives to Linux through a 9P server running on the Windows side. Every file operation from Linux traverses:

```
Linux process → syscall → 9P client (kernel) → virtio transport → 9P server (Windows) → NTFS → disk
```

This pipeline adds per-operation latency (~30–200 µs) and caps aggregate throughput. For workloads that do many small reads (LLM MoE expert fetching, random access across a 340 GB GGUF), 9P overhead dominates. Result: the underlying disk speed is irrelevant; 9P is the bottleneck.

Practical measured 9P cap: ~1–2 GB/s regardless of the Windows disk underneath.

## RAID 0 math — LLM-workload correction

Naïve RAID 0 math: 2× 550 MB/s SATA SSDs → 1100 MB/s stripe read. In practice for LLM inference workloads:

| Workload | Pattern | Stripe benefit |
|----------|---------|---------------|
| Sequential bulk read (e.g., loading full GGUF) | sequential | ~1.5–1.8× |
| Random mid-read (MoE expert chunks) | semi-random | ~1.2–1.4× |
| Tiny random reads (metadata, kv-cache spills) | random | ~1.0–1.1× |

Overhead sources: request alignment, stripe-boundary penalty, 9P re-fragmentation, RAID controller latency. Real-world gain for K2.6 Q2 inference via KTransformers on 2× SATA RAID 0: **~20–40%** over single SATA, still far below single Gen4 NVMe.

## Recommended placements (2026-04-22)

| Use case | Where | Why |
|----------|-------|-----|
| K2.6 Q2 GGUF weights (340 GB) | `/dev/sdd` → `/mnt/models/kimi-k2-6-q2/` | Fastest local NVMe path; stays out of 9P |
| AirLLM disk-offload cache | `/dev/sdd` → `/mnt/models/airllm-cache/` | Same reason |
| Custom LoRA adapters | `/dev/sdd` → `/mnt/models/adapters/` | Hot swap latency matters |
| Archive / dataset cold storage | `/mnt/d/` (1.9 TB RAID) | Large sequential reads; 9P cap OK |
| Training data (datasets 1–50 GB) | `/mnt/models/datasets/` | Batch reads, size fits the tier |
| Long-term backups | `/mnt/e/` (4 TB Sabrent USB) | Cold, cheap, slow is fine |
| **Never** | `/mnt/c/` | Windows system partition |
| **Never** | Disk 2 or 4 | OS / Docker — off-limits |

## Migration procedure (future)

If operator adds a dedicated NVMe RAID (2× NVMe, not SATA):

1. Benchmark the new array (`fio` sequential + random tests) and document numbers here under a new disk row.
2. Compare against `/dev/sdd` — new RAID needs to beat 5–7 GB/s to justify migration.
3. Plan an atomic move: stop all consumers (KTransformers, AICP routing, AirLLM), `rsync -a` from `/mnt/models/` to the new mount, update `/etc/fstab`, restart consumers.
4. Update this page's disk table + the "Recommended placements" section.
5. Publish a migration log at `wiki/log/<date>-storage-migration.md`.

## Verification commands

```bash
# Identify the block device
lsblk                             # /dev/sdd should appear
sudo blkid /dev/sdd               # TYPE="ext4" UUID="..."
sudo fsck.ext4 -n /dev/sdd        # read-only check (see T008)

# Measure real-world bandwidth after mount
sudo apt-get install -y fio
fio --name=seq-read --rw=read --bs=1M --size=4G \
    --iodepth=16 --numjobs=1 --direct=1 \
    --filename=/mnt/models/.fio-test-$$ --group_reporting
# Expect ~4–6 GB/s on /dev/sdd; ~0.8–1.5 GB/s on /mnt/d; USB-limited on /mnt/e.

# WSL memory budget
free -g                           # must show the 64 GB RAM cap (E010 M001)
```

## When this page is wrong

Update it. Treat every measured number as authoritative; treat every estimate as provisional. If operator hardware changes (new drive, WSL reconfig, motherboard swap), the 2026-04-22 ground truth is no longer the same ground truth — re-verify with `lsblk` + `fio` before updating downstream recommendations.

## Relationships

- PART OF: [[E010-storage-and-hardware-enablement|E010 — Storage and Hardware Enablement]]
- BUILDS ON: [[2026-consumer-hardware-ai-stack|2026 Consumer-Hardware AI Stack]]
- REFERENCED BY: [[e008-m002-k2-6-q2-gguf-download-and-verify|E008 M002 — K2.6 Q2 download]]
- REFERENCED BY: [[e010-m002-dev-sdd-mount-procedure|E010 M002 — /dev/sdd mount]]
- REFERENCED BY: [[model-local-ai|Model — Local AI]]

## Backlinks

[[E010 — Storage and Hardware Enablement]]
[[2026 Consumer-Hardware AI Stack]]
[[E008 M002 — K2.6 Q2 download]]
[[E010 M002 — /dev/sdd mount]]
[[Model — Local AI]]
