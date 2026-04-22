---
title: "E008 M002 — K2.6 Q2 GGUF Download and Verify"
type: module
domain: backlog
status: done
priority: P1
task_type: module
current_stage: test
readiness: 100
progress: 100
stages_completed: [document, design, scaffold, implement, test]
artifacts: []
epic: "E008"
depends_on:
  - "E010-m002"
confidence: high
created: 2026-04-22
updated: 2026-04-22
sources:
  - id: e008-local-k2-6-offline-frontier-tier
    type: wiki
    file: wiki/backlog/epics/pre-milestone/E008-local-k2-6-offline-frontier-tier.md
  - id: unsloth-k2-6-gguf
    type: repository
    url: https://huggingface.co/unsloth/Kimi-K2.6-GGUF
    title: "unsloth/Kimi-K2.6-GGUF — Hugging Face"
tags: [module, p1, e008, gguf, kimi-k2-6, download, hf, unsloth, storage]
---

# E008 M002 — K2.6 Q2 GGUF Download and Verify

## Summary

Download the Unsloth Q2 dynamic quantization of Kimi K2.6 (~340 GB, UD-Q2_K_XL variant) from Hugging Face to `/mnt/models/kimi-k2-6-q2/`, verify checksums, and catalog the files in the storage inventory. Q2 is the recommended starting point because it balances size (fits in 1 TB /dev/sdd with headroom) and quality (QAT-trained INT4 quality is preserved even at aggressive quant). Q4 (584 GB) is optional upgrade for A/B quality comparison.

## Tasks

| Task | Title | Readiness | Progress | Status |
|------|-------|-----------|----------|--------|
| T011 | Install huggingface_hub CLI if missing | 100% | 0% | draft |
| T012 | Download UD-Q2_K_XL GGUF to /mnt/models/kimi-k2-6-q2/ | 100% | 0% | draft |
| T013 | Verify SHA256 checksums against HF repo | 100% | 0% | draft |

## Dependencies

- [[e010-m002-dev-sdd-mount-procedure]] — `/mnt/models` must be mounted and writable
- Network bandwidth — 340 GB. Plan for overnight download unless on high-bandwidth connection.
- `huggingface_hub` Python package with CLI (`hf` command in recent versions).

## Done When

- [ ] `/mnt/models/kimi-k2-6-q2/` exists with all Q2 variant files (multi-part GGUF)
- [ ] Total size ≈ 340 GB
- [ ] `sha256sum -c` against Unsloth's provided checksums reports OK for every file
- [ ] `df -h /mnt/models` shows ≥500 GB still free (for Q4 later or other models)
- [ ] `tools/inventory_models.sh` run on /mnt/models lists K2.6 Q2 with URL + size + checksum date
- [ ] All child tasks at status: done

## Procedure (reference)

```bash
# Step 1: Install huggingface CLI if not present
pip install --user "huggingface_hub[cli]"

# Step 2: Download (resumable)
cd /mnt/models
hf download unsloth/Kimi-K2.6-GGUF \
  --include "UD-Q2_K_XL/*" \
  --local-dir ./kimi-k2-6-q2 \
  --local-dir-use-symlinks False

# Step 3: Verify
cd kimi-k2-6-q2
# HF repository may provide a checksum manifest — hf download writes original sha256 for each file
# Option A: use hf's built-in verify
hf download --revision <revision> unsloth/Kimi-K2.6-GGUF --include "UD-Q2_K_XL/*" --local-dir . --resume-download

# Option B: manual sha256 if a separate manifest is published
# curl -sSLO https://huggingface.co/unsloth/Kimi-K2.6-GGUF/resolve/main/UD-Q2_K_XL/SHA256SUMS
# sha256sum -c SHA256SUMS

# Step 4: Report size and catalog
du -sh /mnt/models/kimi-k2-6-q2
/home/jfortin/devops-solutions-research-wiki/tools/inventory_models.sh
```

## Rollback

- If checksum verification fails: re-download only the failing file(s) with `--force-download`.
- If disk fills during download: `rm -rf /mnt/models/kimi-k2-6-q2/` and free space elsewhere before retry.

## Impediments

| Impediment | Type | Blocked Since | Escalated? | Resolution |
|-----------|------|---------------|-----------|------------|
| /mnt/models not yet mounted | dependency | 2026-04-22 | no | Resolves via E010 M002 |
| Bandwidth / wall-clock (340 GB) | external | 2026-04-22 | no | Start as background download; operator continues daily work |

## Relationships

- PART OF: [[E008-local-k2-6-offline-frontier-tier|E008-local-k2-6-offline-frontier-tier]]
- DEPENDS ON: [[e010-m002-dev-sdd-mount-procedure|e010-m002-dev-sdd-mount-procedure]]

## Backlinks

[[E008-local-k2-6-offline-frontier-tier|E008-local-k2-6-offline-frontier-tier]]
[[e010-m002-dev-sdd-mount-procedure|e010-m002-dev-sdd-mount-procedure]]
