---
title: "VHDX Attach Procedure + HCS E_ACCESSDENIED Fix (authoritative)"
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
  - id: microsoft-qna-hcs-access-denied
    type: reference
    url: https://learn.microsoft.com/en-us/answers/questions/1697336/error-code-wsl-service-createinstance-mountvhd-hcs
    title: "Microsoft Q&A — HCS/E_ACCESSDENIED fix via ownership change"
  - id: wsl-issue-12493
    type: reference
    url: https://github.com/microsoft/WSL/issues/12493
    title: "WSL #12493 — Windows Security Entities on --mount"
  - id: wsl-issue-11323
    type: reference
    url: https://github.com/microsoft/WSL/issues/11323
    title: "WSL #11323 — 2.1.5.0 HCS/E_ACCESSDENIED regression"
tags: [note, completion, e010, vhdx, wsl, mount, hcs, access-denied, icacls, takeown, troubleshooting, gotcha]
---

# VHDX Attach Procedure + HCS E_ACCESSDENIED Fix

## Summary

Attaching a fresh VHDX to WSL2 via `wsl --mount --vhd ... --bare` fails with `Wsl/Service/AttachDisk/MountVhd/HCS/E_ACCESSDENIED` even when PowerShell is elevated and the file exists in a writable location. HCS (Host Compute Service) does NTFS ACL checks that include **file ownership**, not just the DACL — it requires the current user / Administrators as owner plus explicit grants to the virtual-machine identities. This note captures the working attach procedure for future reference.

## What Was Done

- Created a 1 TB dynamic VHDX at `D:\vdisks\models.vhdx` via `New-VHD`.
- Attempted `wsl --mount --vhd ... --bare` → failed with HCS/E_ACCESSDENIED.
- Granting only `NT VIRTUAL MACHINE\Virtual Machines:(F)` via `icacls` was **insufficient** — still denied.
- Applied full `takeown` + `icacls /reset` + multi-identity grant sequence → attach succeeded.
- `/dev/sdd` now visible in WSL at 1 TB (1099511627776 bytes), unformatted.

## Working procedure (future VHDX attaches)

In an **elevated** PowerShell window:

```powershell
# Step 1 — Create the VHDX (dynamic; sparse on disk, grows as used)
New-VHD -Path "D:\vdisks\models.vhdx" -SizeBytes 1TB -Dynamic

# Step 2 — Fix ownership + ACL (THE STEP EVERYONE MISSES)
takeown /F "D:\vdisks\models.vhdx"
icacls "D:\vdisks\models.vhdx" /reset
icacls "D:\vdisks\models.vhdx" /grant "$(whoami):(F)"
icacls "D:\vdisks\models.vhdx" /grant "NT VIRTUAL MACHINE\Virtual Machines:(F)"
icacls "D:\vdisks\models.vhdx" /grant "SYSTEM:(F)"
icacls "D:\vdisks\models.vhdx" /grant "Administrators:(F)"

# Step 3 — Attach to WSL as a bare block device
wsl --mount --vhd "D:\vdisks\models.vhdx" --bare
```

Inside WSL, the new block device appears as the next available `sdX` (here: `/dev/sdd`):

```bash
lsblk -b
# Expected row: sdd  8:48  0  1099511627776  0 disk  (no mountpoint yet)
```

## Why the error happens

HCS runs under its own identity and performs an NTFS access check that includes **file ownership**, not just the DACL. A freshly-created VHDX can have:

- An owner that doesn't include the VM service identity.
- A DACL that doesn't grant `NT VIRTUAL MACHINE\Virtual Machines` (the SID WSL2 mounts under).
- Stale ACLs inherited from a parent directory with restrictive permissions.

`takeown` resets the owner. `icacls /reset` clears stale inherited entries. The subsequent `/grant` calls add every identity HCS might touch the file under.

## Other root causes to rule out (not hit here, but recorded for future triage)

- **WSL version 2.1.5.0** has a documented regression for this exact error — `wsl --version`; update if on that build.
- **Controlled Folder Access** (Windows Security → Ransomware protection) can block `vmcompute.exe` from modifying VHDX files. Whitelist `vmcompute.exe` or toggle CFA off to isolate.

## Hardware correction (affects storage tiering reference doc)

- **D:\ is the NVMe drive** — where WSL lives and where this VHDX now sits. The earlier storage tiering doc incorrectly labeled D:\ as the 1.9 TB SATA RAID 0. That labeling was wrong.
- Per operator: Windows OS is on an Intel RAID 0; the 1.9 TB is a NAS SSD on its own RAID 0 (separate volume from Windows OS).
- **Action**: correct `wiki/spine/references/operator-workstation-storage-tiering.md` — the disk-letter and disk-number columns are misaligned with actual topology.

## Validation

> [!success] VHDX attached successfully
> - `lsblk -b` shows `sdd  8:48   0  1099511627776  0 disk` (1 TB, no mount)
> - Block device accessible inside WSL
> - Next gate: format + mount (T009 → T010)

## Next Steps

- Format `/dev/sdd` as ext4 and mount at `/mnt/models`:
  ```bash
  sudo mkfs.ext4 -L models /dev/sdd
  sudo mkdir -p /mnt/models
  sudo mount /dev/sdd /mnt/models
  ```
- Persist via `/etc/fstab` (T010).
- Then E008 M002 — download K2.6 Q2 GGUF (340 GB).
- Correct the storage tiering reference doc with real disk mapping.

## Relationships

- RELATES TO: [[e010-m002-dev-sdd-mount-procedure|e010-m002-dev-sdd-mount-procedure]]
- RELATES TO: [[operator-workstation-storage-tiering|operator-workstation-storage-tiering]]
- RELATES TO: [[2026-04-23-ram-upgrade-48gb-wsl|2026-04-23-ram-upgrade-48gb-wsl]]
- UNBLOCKS: [[E008-local-k2-6-offline-frontier-tier|E008-local-k2-6-offline-frontier-tier]]

## Backlinks

[[e010-m002-dev-sdd-mount-procedure|e010-m002-dev-sdd-mount-procedure]]
[[operator-workstation-storage-tiering|operator-workstation-storage-tiering]]
[[2026-04-23-ram-upgrade-48gb-wsl|2026-04-23-ram-upgrade-48gb-wsl]]
[[E008-local-k2-6-offline-frontier-tier|E008-local-k2-6-offline-frontier-tier]]
