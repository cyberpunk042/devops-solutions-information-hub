---
title: "E010 M002 — /dev/sdd Mount Procedure (ext4 at /mnt/models)"
type: module
domain: backlog
status: draft
priority: P1
task_type: module
current_stage: design
readiness: 50
progress: 0
stages_completed: [document]
artifacts: []
epic: "E010"
depends_on: []
confidence: high
created: 2026-04-22
updated: 2026-04-22
sources:
  - id: e010-storage-and-hardware-enablement
    type: wiki
    file: wiki/backlog/epics/pre-milestone/E010-storage-and-hardware-enablement.md
tags: [module, p1, e010, dev-sdd, ext4, mount, fstab, wsl, storage, sudo]
---

# E010 M002 — /dev/sdd Mount Procedure

## Summary

Mount the existing WSL dynamic VHDX (`/dev/sdd`, 1 TB capacity, on Windows Disk 0 WD_BLACK SN770 Gen4 NVMe) as `/mnt/models` with ext4, and persist the mount via `/etc/fstab`. Per dmesg evidence from 2026-04-22, /dev/sdd already contains an ext4 filesystem (`EXT4-fs (sdd): recovery complete`) — attempt non-destructive mount first; only reformat if the existing data is unwanted.

## Tasks

| Task | Title | Readiness | Progress | Status |
|------|-------|-----------|----------|--------|
| T008 | Verify /dev/sdd filesystem (blkid + fsck -n) | 100% | 0% | draft |
| T009 | Mount /dev/sdd at /mnt/models (non-destructive first) | 100% | 0% | draft |
| T010 | Persist mount via /etc/fstab | 100% | 0% | draft |

## Dependencies

- Operator sudo access — required for all three tasks.
- No RAM upgrade dependency (can happen before or after 2026-04-23).

## Done When

- [ ] `sudo blkid /dev/sdd` reports a valid ext4 filesystem with UUID
- [ ] `sudo mkdir -p /mnt/models` succeeds
- [ ] `sudo mount /dev/sdd /mnt/models` succeeds and `df -h /mnt/models` reports ~1 TB capacity
- [ ] `/etc/fstab` contains a line pinning the mount (by UUID, not by device path, for WSL stability): `UUID=<uuid> /mnt/models ext4 defaults,nofail,x-systemd.device-timeout=10s 0 2`
- [ ] After WSL restart (`wsl --shutdown` from PowerShell, then reopen), `/mnt/models` automatically mounted
- [ ] `touch /mnt/models/.mount-ok` succeeds (writable by operator user)
- [ ] All child tasks at status: done

## Procedure (reference — operator executes)

```bash
# Step 1: Verify existing filesystem (non-destructive)
sudo blkid /dev/sdd
# Expected: /dev/sdd: UUID="..." BLOCK_SIZE="4096" TYPE="ext4"

# Step 1b: Sanity-check filesystem integrity
sudo fsck.ext4 -n /dev/sdd

# Step 2: Create mount point and mount
sudo mkdir -p /mnt/models
sudo mount /dev/sdd /mnt/models
df -h /mnt/models
# Expected: ~1 TB available

# Step 3: Capture UUID, add to /etc/fstab
SDD_UUID=$(sudo blkid -s UUID -o value /dev/sdd)
echo "UUID=$SDD_UUID /mnt/models ext4 defaults,nofail,x-systemd.device-timeout=10s 0 2" | sudo tee -a /etc/fstab

# Step 4: Test persistence by unmounting and remounting via fstab
sudo umount /mnt/models
sudo mount -a
df -h /mnt/models
```

## Rollback

If the existing filesystem on /dev/sdd is corrupt or unwanted:

```bash
# DESTRUCTIVE — only if the existing data is truly unneeded
sudo umount /mnt/models 2>/dev/null
sudo mkfs.ext4 -L models /dev/sdd
sudo mount /dev/sdd /mnt/models
```

## Impediments

| Impediment | Type | Blocked Since | Escalated? | Resolution |
|-----------|------|---------------|-----------|------------|
| Operator sudo access required | environment | 2026-04-22 | no | Operator runs the procedure when ready |

## Relationships

- PART OF: [[E010-storage-and-hardware-enablement|E010-storage-and-hardware-enablement]]

## Backlinks

[[E010-storage-and-hardware-enablement|E010-storage-and-hardware-enablement]]
