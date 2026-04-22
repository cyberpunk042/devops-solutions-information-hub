---
title: "E010 — Storage and Hardware Enablement (64 GB RAM + /dev/sdd + tiering)"
type: epic
domain: backlog
status: draft
priority: P0
task_type: epic
current_stage: document
readiness: 25
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
tags: [epic, p0, hardware, storage, ram, nvme, wsl, ext4, dev-sdd, vhdx, disk-tiering, post-anthropic]
---

# E010 — Storage and Hardware Enablement

## Summary

Prepare operator's workstation hardware and storage for the local K2.6 tier and the overall self-autonomous stack: install 64 GB RAM (arrives 2026-04-23), mount /dev/sdd (dynamic WSL VHDX on WD_BLACK SN770 Gen4 NVMe) as ext4 at `/mnt/models`, document the full disk tiering with accurate speed numbers so future AIs don't repeat the NVMe-vs-SATA confusion, and establish a backup strategy for model weights. This epic is a **prerequisite for E008** (local K2.6) and a **performance multiplier for E011** (routing) — accurate hardware information is load-bearing for every downstream decision.

## Operator Directive

> "Soon I will be at 64RAM (1 day)."

> "I will buy more storage if needed but already we should have a lot here and there and we can even consider that I can do cleanup if we lack space."

> "In 5 days everything will most likely be happening on this computer with the 19GB VRAM and the 1TB NVME SSD for AirLLM and so on."

## Goals

- 64 GB RAM installed and detected by WSL.
- `/dev/sdd` filesystem verified (ext4 recovery-mountable per dmesg evidence) and mounted at `/mnt/models`.
- Mount persisted via `/etc/fstab`.
- Storage tiering document published — authoritative, avoids the NVMe-vs-SATA mistake — mapping every Windows disk → Linux access path → real-world speed → recommended use.
- Backup strategy for `/mnt/models` contents (model weights can be re-downloaded, so strategy is light: inventory only, no full backup).

## Done When

- [ ] `free -g` in WSL reports ~62 GiB total memory (64 GB installed minus kernel reserves)
- [ ] `dmesg` shows no memory errors on boot after RAM install
- [ ] `/dev/sdd` identified: WSL dynamic VHDX on Disk 0 (WD_BLACK SN770 single Gen4 NVMe), 1 TB capacity
- [ ] `sudo blkid /dev/sdd` reports `TYPE="ext4"` (filesystem recoverable per dmesg 2026-04-22)
- [ ] `sudo mkdir -p /mnt/models && sudo mount /dev/sdd /mnt/models` succeeds; `/mnt/models` is writable
- [ ] `/etc/fstab` entry added; `sudo mount -a` after reboot shows `/mnt/models` persisted
- [ ] `df -h /mnt/models` reports ~1 TB capacity, mostly free
- [ ] `wiki/spine/references/operator-workstation-storage-tiering.md` published with the authoritative disk map (verified, not assumed): Windows disk # → size → physical drive type (NVMe/SATA/USB) → WSL access path → real-world read bandwidth → recommended use
- [ ] Storage tiering doc includes: why /mnt/d (9P) is slow, why Intel RAID 0 SATA SSDs are slower than single NVMe, why /dev/sdd is the fastest WSL-accessible path today, which disks are off-limits (Windows OS, Docker)
- [ ] Model weights inventory script at `tools/inventory_models.sh` — lists what's at `/mnt/models`, sizes, source URLs for re-download
- [ ] `python3 -m tools.pipeline post` returns 0 validation errors after all E010 work commits

## Scale and Model

> [!info] Epic Parameters
>
> | Parameter | Value |
> |-----------|-------|
> | **Model** | feature-development |
> | **Quality tier** | Pyramid (infrastructure — unblocks other epics) |
> | **Estimated modules** | 4 |
> | **Estimated tasks** | 8-10 |
> | **Dependencies** | RAM hardware arrival 2026-04-23 |

## Module Breakdown

| Module | Delivers | Est. Tasks |
|--------|----------|-----------|
| [[e010-m001-64gb-ram-install-and-verify]] | RAM installed, detected, no errors | 2 |
| [[e010-m002-dev-sdd-mount-procedure]] | /dev/sdd mounted ext4 at /mnt/models, persisted in /etc/fstab | 3 |
| [[e010-m003-storage-tiering-documentation]] | Authoritative disk-tiering doc at wiki/spine/references/ | 2 |
| [[e010-m004-model-weights-inventory]] | `tools/inventory_models.sh` + initial model manifest | 2 |

## Dependencies

- RAM hardware arrival (2026-04-23) — external, not in project control.
- Operator sudo access — required for mount, fstab edit, filesystem check.
- `/dev/sdd` ext4 filesystem integrity — dmesg indicated recovery completed on prior mount; `fsck.ext4 -n` should verify cleanly before mount.

## Open Questions

> [!question] Does /dev/sdd's existing ext4 data matter, or should we reformat?
> Default: try mounting first (non-destructive). If existing data is unwanted, backup/clean/reformat as a separate task.

> [!question] Operator mentioned "RAID 0 NVMe SSDs" separately from the existing Intel RAID 0 (which is SATA). Is a new NVMe RAID being added?
> Possibly future hardware. Not in scope for the 5-day plan — track as a follow-up if operator confirms the purchase/install.

> [!question] Should `/mnt/models` be moved to a different drive if operator adds a dedicated NVMe RAID later?
> Yes — storage tiering doc includes migration procedure. Handled in a future follow-up, not M010 scope.

## Relationships

- PART OF: [[post-anthropic-self-autonomous-stack|Milestone: Post-Anthropic Self-Autonomous AI Stack]]

## Backlinks

[[post-anthropic-self-autonomous-stack|Milestone: Post-Anthropic Self-Autonomous AI Stack]]
