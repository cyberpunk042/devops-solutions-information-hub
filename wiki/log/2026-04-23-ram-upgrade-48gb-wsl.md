---
title: "RAM Upgrade — 48 GB WSL Cap Live (E010 M001 complete)"
type: note
domain: cross-domain
note_type: completion
status: synthesized
confidence: high
created: 2026-04-22
updated: 2026-04-22
sources:
  - id: e010-m001-64gb-ram-install-and-verify
    type: wiki
    file: wiki/backlog/modules/e010-m001-64gb-ram-install-and-verify.md
  - id: operator-workstation-storage-tiering
    type: wiki
    file: wiki/spine/references/operator-workstation-storage-tiering.md
tags: [note, completion, e010, ram, hardware, wsl, 48gb, 64gb, milestone-gate]
---

# RAM Upgrade — 48 GB WSL Cap Live

## Summary

64 GB host RAM installed and `.wslconfig` configured to cap WSL at 48 GB (leaving 16 GB for Windows host + browser + Docker Desktop). WSL restart confirmed the new cap. This unblocks E008 (K2.6 Q2 local inference — needs the expert-cache headroom) and E012 (LoRA training — needs context headroom for training data batches).

## What Was Done

- Host memory upgraded to 64 GB (operator-applied, 2026-04-22).
- `%USERPROFILE%\.wslconfig` updated with `memory=48GB` + `swap=16GB`.
- `wsl --shutdown` executed from PowerShell to re-apply the cap.
- `free -g` inside WSL reports ~47 GiB total (48 GB cap minus Linux kernel reserve).
- `dmesg | grep hv_balloon` confirms `Max. dynamic memory size: 49152 MB`.
- No memory errors in dmesg on fresh boot.

## Validation

> [!success] RAM upgrade verified
> - `free -g`: total 47, available 42
> - `dmesg`: `hv_balloon: Max. dynamic memory size: 49152 MB`
> - No `memory error | corrected | uncorrected` entries in dmesg
> - Windows host retains 16 GB headroom (64 − 48)

## State Changes

| Dimension | Before | After |
|-----------|--------|-------|
| Host RAM | 32 GB | 64 GB |
| WSL cap | 16 GB (default) | 48 GB (.wslconfig) |
| WSL swap | default | 16 GB |
| Windows headroom | ~16 GB | ~16 GB |
| K2.6 Q2 local inference | blocked (OOM risk) | **unblocked** |
| LoRA training batch size | constrained | workable |

## Concerns Raised

- 48 GB WSL cap may be too generous if operator runs video editing or VMs on Windows side; watch Task Manager pressure during first K2.6 Q2 inference. Tunable via `.wslconfig` + `wsl --shutdown`.
- Max dynamic memory = 49152 MB is very close to 48 GB — small headroom for WSL's own kernel + services. If `free -g` approaches total during inference, drop the cap to 44 GB to leave swap room.

## Next Steps

1. **T008** — verify /dev/sdd filesystem (blkid + fsck -n, read-only, needs sudo).
2. **T009** — mount /dev/sdd at /mnt/models (needs sudo).
3. **T010** — persist mount via /etc/fstab.
4. Then E008 M002 — download K2.6 Q2 GGUF (340 GB) to /mnt/models.

## Relationships

- COMPLETES: [[e010-m001-64gb-ram-install-and-verify|e010-m001-64gb-ram-install-and-verify]]
- UNBLOCKS: [[E008-local-k2-6-offline-frontier-tier|E008-local-k2-6-offline-frontier-tier]]
- UNBLOCKS: [[E012-custom-model-library-unsloth-loras|E012-custom-model-library-unsloth-loras]]
- RELATES TO: [[operator-workstation-storage-tiering|operator-workstation-storage-tiering]]

## Backlinks

[[e010-m001-64gb-ram-install-and-verify|e010-m001-64gb-ram-install-and-verify]]
[[E008-local-k2-6-offline-frontier-tier|E008-local-k2-6-offline-frontier-tier]]
[[E012-custom-model-library-unsloth-loras|E012-custom-model-library-unsloth-loras]]
[[operator-workstation-storage-tiering|operator-workstation-storage-tiering]]
