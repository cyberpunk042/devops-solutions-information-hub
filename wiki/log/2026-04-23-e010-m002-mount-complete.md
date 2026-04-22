---
title: "E010 M002 Complete — /mnt/models Live on 1 TB NVMe VHDX"
type: note
domain: cross-domain
note_type: completion
status: synthesized
confidence: high
created: 2026-04-22
updated: 2026-04-22
sources:
  - id: e010-m002-dev-sdd-mount-procedure
    type: wiki
    file: wiki/backlog/modules/e010-m002-dev-sdd-mount-procedure.md
  - id: vhdx-attach-fix
    type: wiki
    file: wiki/log/2026-04-23-vhdx-attach-procedure-and-hcs-fix.md
tags: [note, completion, e010, mount, ext4, dev-sdd, mnt-models, milestone-gate]
---

# E010 M002 Complete

## Summary

`/mnt/models` is live — 1 TB dedicated ext4 filesystem on an NVMe-backed WSL VHDX. E010 M002 closes out; E008 M002 (K2.6 Q2 340 GB download) is now unblocked. Only gotcha worth recording for next time: fresh ext4 root is owned by root; a `sudo chown` is required before non-root processes can write (hf CLI, KTransformers, etc.).

## What Was Done

1. Attached `D:\vdisks\models.vhdx` via `wsl --mount --vhd ... --bare` (see `2026-04-23-vhdx-attach-procedure-and-hcs-fix`).
2. Formatted `/dev/sdd` as ext4 with label `models`.
3. Mounted at `/mnt/models` (~1 TB).
4. Persisted via `/etc/fstab` using UUID.
5. Chowned `/mnt/models` to operator user so downstream tools can write without sudo.

## Commands run

```bash
sudo mkfs.ext4 -L models /dev/sdd
sudo mkdir -p /mnt/models
sudo mount /dev/sdd /mnt/models
df -h /mnt/models

SDD_UUID=$(sudo blkid -s UUID -o value /dev/sdd)
echo "UUID=$SDD_UUID /mnt/models ext4 defaults,nofail,x-systemd.device-timeout=10s 0 2" | sudo tee -a /etc/fstab
sudo umount /mnt/models
sudo mount -a
df -h /mnt/models

sudo chown $(id -u):$(id -g) /mnt/models
touch /mnt/models/.mount-ok   # confirms user-writable
```

## Validation

> [!success] /mnt/models is live, persistent, and user-writable
> - `df -h /mnt/models` reports ~1 TB available
> - `mount | grep /mnt/models` shows ext4 with rw
> - `sudo mount -a` after unmount re-attaches from fstab
> - `touch /mnt/models/.mount-ok` succeeds without sudo

## Gotcha recorded

Fresh ext4 root is owned `root:root` with mode 755 — non-root users cannot write to the mount until you `chown` the top level to your user. This is independent of the mount itself but needs to be part of the standard procedure.

## Next Steps

1. **T011** — install `huggingface_hub[cli]` (`pip install --user 'huggingface_hub[cli]'`).
2. **T012** — start `hf download unsloth/Kimi-K2.6-GGUF --include "UD-Q2_K_XL/*" --local-dir /mnt/models/kimi-k2-6-q2`. ~340 GB, resumable, safe to run overnight.
3. **T013** — SHA256 verify against Unsloth's manifest.

## Relationships

- COMPLETES: [[e010-m002-dev-sdd-mount-procedure|e010-m002-dev-sdd-mount-procedure]]
- UNBLOCKS: [[e008-m002-k2-6-q2-gguf-download-and-verify|e008-m002-k2-6-q2-gguf-download-and-verify]]
- RELATES TO: [[2026-04-23-vhdx-attach-procedure-and-hcs-fix|2026-04-23-vhdx-attach-procedure-and-hcs-fix]]
- RELATES TO: [[operator-workstation-storage-tiering|operator-workstation-storage-tiering]]

## Backlinks

[[e010-m002-dev-sdd-mount-procedure|e010-m002-dev-sdd-mount-procedure]]
[[e008-m002-k2-6-q2-gguf-download-and-verify|e008-m002-k2-6-q2-gguf-download-and-verify]]
[[2026-04-23-vhdx-attach-procedure-and-hcs-fix|2026-04-23-vhdx-attach-procedure-and-hcs-fix]]
[[operator-workstation-storage-tiering|operator-workstation-storage-tiering]]
