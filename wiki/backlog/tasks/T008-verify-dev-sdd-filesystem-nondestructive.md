---
title: "T008 — Verify /dev/sdd Filesystem (blkid + fsck -n, non-destructive)"
type: task
domain: backlog
status: done
priority: P0
task_type: task
current_stage: test
readiness: 100
progress: 100
stages_completed: [document, design, scaffold, implement, test]
artifacts: []
estimate: XS
epic: "E010"
module: "E010-m002"
depends_on: []
confidence: high
created: 2026-04-22
updated: 2026-04-22
sources:
  - id: e010-m002-dev-sdd-mount-procedure
    type: wiki
    file: wiki/backlog/modules/e010-m002-dev-sdd-mount-procedure.md
tags: [task, p0, e010, dev-sdd, blkid, fsck, non-destructive, pre-mount]
---

# T008 — Verify /dev/sdd Filesystem (non-destructive)

## Summary

Before mounting `/dev/sdd` at `/mnt/models` (T009), confirm its filesystem is ext4 and healthy. dmesg on 2026-04-22 showed "EXT4-fs (sdd): recovery complete", suggesting an ext4 filesystem exists and was recovered. Use `blkid` + `fsck.ext4 -n` (READ-ONLY, `-n` means "no fix") to verify without mutation. This task is runnable TODAY without waiting for the mount or RAM install.

## Done When

- [ ] `sudo blkid /dev/sdd` reports `TYPE="ext4"` and a valid UUID
- [ ] `sudo fsck.ext4 -n /dev/sdd` completes without reporting filesystem corruption
- [ ] Output (UUID + fsck summary) captured in `wiki/log/2026-04-23-dev-sdd-verify.md` (create stub if needed)
- [ ] Decision recorded: mount non-destructively (existing data preserved) OR reformat before mount (only if fsck shows unrecoverable issues)

## Procedure

```bash
# Step 1: Confirm device exists
ls -l /dev/sdd
lsblk | grep sdd

# Step 2: Filesystem type + UUID
sudo blkid /dev/sdd
# Expected output form: /dev/sdd: UUID="xxxxxxxx-..." BLOCK_SIZE="4096" TYPE="ext4"

# Step 3: Read-only filesystem sanity check
sudo fsck.ext4 -n /dev/sdd
# Expected: "clean" or a report of minor issues; look for "errors detected".

# Step 4: Capture UUID for later /etc/fstab entry (see T009)
SDD_UUID=$(sudo blkid -s UUID -o value /dev/sdd)
echo "UUID captured: $SDD_UUID"

# Step 5: Log results
cd /home/jfortin/devops-solutions-research-wiki
python3 -m tools.pipeline scaffold note "2026-04-23-dev-sdd-verify" 2>/dev/null || true
$EDITOR wiki/log/2026-04-23-dev-sdd-verify.md
```

## Rollback

Read-only — nothing to roll back.

## Decision tree

| fsck result | Decision |
|-------------|----------|
| "clean" | Proceed to T009 (mount) as non-destructive — preserves existing ext4 filesystem |
| minor recoverable issues | Optional: `sudo fsck.ext4 -p /dev/sdd` to auto-fix, then T009 |
| unrecoverable corruption | Reformat: `sudo mkfs.ext4 -L models /dev/sdd` (DESTRUCTIVE — only if data is disposable); then T009 |

## Relationships

- PART OF: [[e010-m002-dev-sdd-mount-procedure|e010-m002-dev-sdd-mount-procedure]]
- PART OF: [[E010-storage-and-hardware-enablement|E010-storage-and-hardware-enablement]]
- FEEDS INTO: [[T009-mount-dev-sdd-at-mnt-models|T009-mount-dev-sdd-at-mnt-models]]

## Backlinks

[[e010-m002-dev-sdd-mount-procedure|e010-m002-dev-sdd-mount-procedure]]
[[E010-storage-and-hardware-enablement|E010-storage-and-hardware-enablement]]
[[T009-mount-dev-sdd-at-mnt-models]]
