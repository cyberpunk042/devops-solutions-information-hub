---
title: "E010 M003 — Storage Tiering Documentation (authoritative disk map)"
type: module
domain: backlog
status: draft
priority: P0
task_type: module
current_stage: design
readiness: 100
progress: 0
stages_completed: [document]
artifacts:
  - wiki/spine/references/operator-workstation-storage-tiering.md
epic: "E010"
depends_on: []
confidence: high
created: 2026-04-22
updated: 2026-04-22
sources:
  - id: e010-storage-and-hardware-enablement
    type: wiki
    file: wiki/backlog/epics/pre-milestone/E010-storage-and-hardware-enablement.md
  - id: operator-hardware-ground-truth
    type: file
    file: raw/notes/2026-04-22-directive-post-anthropic-self-autonomous-plan.md
tags: [module, p0, e010, storage, tiering, documentation, reference, hardware-ground-truth]
---

# E010 M003 — Storage Tiering Documentation

## Summary

Publish the authoritative disk-tiering reference page — `wiki/spine/references/operator-workstation-storage-tiering.md` — that maps every Windows physical disk to its Linux/WSL access path, real-world read bandwidth, filesystem-layer overhead (9P vs native VHDX), and recommended use. This page exists specifically to prevent future AI sessions from re-litigating settled hardware facts (e.g., the 1.9 TB Intel RAID 0 is SATA SSDs, NOT NVMe — operator clarified multiple times on 2026-04-22). Load-bearing for E008 weights placement, AirLLM offload decisions, and any future routing optimization.

## Tasks

| Task | Title | Readiness | Progress | Status |
|------|-------|-----------|----------|--------|
| T041 | Author operator-workstation-storage-tiering.md with verified disk map | 100% | 0% | draft |
| T042 | Cross-link the reference from model-local-ai + 2026-consumer-hardware-ai-stack | 100% | 0% | draft |

## Dependencies

- None — content is already known from 2026-04-22 research. Writing task only.

## Done When

- [ ] `wiki/spine/references/operator-workstation-storage-tiering.md` exists with full frontmatter (type: reference, domain: hardware, status: growing)
- [ ] Page length ≥150 lines
- [ ] Contains the 5-disk table: Windows Disk # → size → physical media → WSL access path → real-world bandwidth → recommended use
- [ ] Explicit "common mistakes" section naming the NVMe-vs-SATA trap with the corrected facts
- [ ] Bandwidth numbers labeled `verified`, `measured`, or `estimated` with date stamps
- [ ] Off-limits disks clearly marked (Windows OS, Docker)
- [ ] 9P filesystem overhead explanation (why /mnt/d is slower than /dev/sdd despite underlying NVMe)
- [ ] RAID 0 math explained (2× SATA SSD → ~0.8–1.0 GB/s theoretical, ~20–40% real-world gain, not 2×)
- [ ] Migration procedure stub for "when operator adds NVMe RAID later"
- [ ] Referenced from at least two other pages (model-local-ai, 2026-consumer-hardware-ai-stack)
- [ ] `python3 -m tools.pipeline post` passes after commit
- [ ] All child tasks at status: done

## Procedure (reference)

### Step 1 — Scaffold the reference page

```bash
cd /home/jfortin/devops-solutions-research-wiki
python3 -m tools.pipeline scaffold reference "operator-workstation-storage-tiering"
$EDITOR wiki/spine/references/operator-workstation-storage-tiering.md
```

### Step 2 — Canonical content outline

```markdown
# Operator Workstation — Storage Tiering Reference

## Summary (verified 2026-04-22)
One-paragraph statement of what this page is and why it exists.

## Ground-truth disk map
| Win Disk | Size | Physical | WSL path | Read BW | Filesystem | Use |
|----------|------|----------|----------|---------|------------|-----|
| 0 | 931 GB | WD_BLACK SN770 (single Gen4 NVMe) | /dev/sdd (dynamic VHDX, ext4) | 5–7 GB/s | native | K2.6 weights, AirLLM offload |
| 1 | 1.9 TB | 2× SATA SSDs in Intel RAID 0 | /mnt/d (NTFS via 9P) | 0.8–1.0 GB/s phys, ~1–2 GB/s via 9P cap | 9P-capped | archive, backups, NOT LLM weights |
| 2 | ~500 GB | Intel RAID 0 | Windows OS | — | — | OFF-LIMITS |
| 3 | 4 TB | Sabrent USB external | /mnt/e (NTFS via 9P) | USB-limited | 9P-capped | cold storage |
| 4 | 233 GB | — | Docker | — | — | OFF-LIMITS |

## Common mistakes (ground-truth affirmed)
- The 1.9 TB Intel RAID 0 is SATA SSDs, NOT NVMe. Operator-verified multiple times.
- `/mnt/d` is capped by 9P filesystem overhead, not by the underlying disk speed.
- `/dev/sdd` is faster than `/mnt/d` even though both ultimately touch NVMe, because `/dev/sdd` is a native ext4 VHDX, not a 9P passthrough.
- RAID 0 of 2× SATA SSDs is SLOWER than a single Gen4 NVMe. 2× 550 MB/s SATA ≠ 2× faster than 7 GB/s NVMe.

## 9P filesystem overhead explained
Paragraph covering why WSL's /mnt/c, /mnt/d, etc. sit behind a 9P server and why that caps throughput regardless of underlying disk speed.

## RAID 0 math
Paragraph: striping theory vs reality, LLM I/O patterns (semi-random MoE expert access ≠ large sequential reads).

## Migration procedure (future)
Stub for "when operator adds dedicated NVMe RAID": what to re-benchmark, what paths to update, how to move /mnt/models atomically.

## Relationships
```

### Step 3 — Cross-link from existing pages

```bash
# Add a "See also" link to these two pages pointing at the new reference
$EDITOR wiki/spine/models/depth/model-local-ai.md
$EDITOR wiki/spine/references/2026-consumer-hardware-ai-stack.md
```

### Step 4 — Validate

```bash
python3 -m tools.pipeline post
# Confirm: 0 validation errors, ≥2 backlinks to the new reference page
```

## Rollback

```bash
cd /home/jfortin/devops-solutions-research-wiki
rm wiki/spine/references/operator-workstation-storage-tiering.md
# Revert cross-link edits
git checkout -- wiki/spine/models/depth/model-local-ai.md wiki/spine/references/2026-consumer-hardware-ai-stack.md
python3 -m tools.pipeline post
```

## Impediments

| Impediment | Type | Blocked Since | Escalated? | Resolution |
|-----------|------|---------------|-----------|------------|
| Real-world NVMe bandwidth not yet measured directly on this hardware | data | 2026-04-22 | no | Mark as "estimated 5–7 GB/s"; run `fio` benchmark post-mount in a follow-up |

## Relationships

- PART OF: [[E010-storage-and-hardware-enablement|E010-storage-and-hardware-enablement]]
- FEEDS INTO: [[e008-m002-k2-6-q2-gguf-download-and-verify|e008-m002-k2-6-q2-gguf-download-and-verify]]
- FEEDS INTO: [[e010-m002-dev-sdd-mount-procedure|e010-m002-dev-sdd-mount-procedure]]
- PRODUCES: `wiki/spine/references/operator-workstation-storage-tiering.md`

## Backlinks

[[E010-storage-and-hardware-enablement|E010-storage-and-hardware-enablement]]
[[e008-m002-k2-6-q2-gguf-download-and-verify|e008-m002-k2-6-q2-gguf-download-and-verify]]
[[e010-m002-dev-sdd-mount-procedure|e010-m002-dev-sdd-mount-procedure]]
[[`wiki/spine/references/operator-workstation-storage-tiering.md`]]
