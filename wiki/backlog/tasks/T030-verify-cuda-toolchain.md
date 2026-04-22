---
title: "T030 — Verify CUDA Toolchain + GPU Driver Compatibility"
type: task
domain: backlog
status: draft
priority: P1
task_type: task
current_stage: design
readiness: 100
progress: 0
stages_completed: [document, design]
artifacts: []
estimate: XS
epic: "E008"
module: "E008-m001"
depends_on: []
confidence: high
created: 2026-04-22
updated: 2026-04-22
sources:
  - id: e008-m001-ktransformers-install-and-config
    type: wiki
    file: wiki/backlog/modules/e008-m001-ktransformers-install-and-config.md
tags: [task, p1, e008, cuda, nvcc, nvidia-smi, wsl2, verification]
---

# T030 — Verify CUDA Toolchain

## Summary

Confirm CUDA >= 12.1 toolkit + compatible NVIDIA driver are installed and usable inside WSL2 BEFORE attempting any KTransformers install. This is a read-only check that takes ~30 seconds. Can be run today. If it fails, the fix (install NVIDIA WSL CUDA) is a separate preparation step that must happen before T031.

## Done When

- [ ] `nvcc --version` reports CUDA release 12.1 or higher
- [ ] `nvidia-smi` prints GPU details + driver version
- [ ] `nvidia-smi` and `nvcc --version` report compatible versions (driver supports the CUDA runtime version)
- [ ] `echo $CUDA_HOME` returns a valid path (fix `~/.bashrc` if empty)
- [ ] Results captured in `wiki/log/2026-04-23-ktransformers-install.md` (even if M001 isn't started yet — start the log stub)

## Procedure

```bash
nvcc --version
nvidia-smi
which nvcc
echo "CUDA_HOME=$CUDA_HOME"
ls /usr/local/ | grep -i cuda    # confirm toolkit install root
```

Expected pass criteria:

| Signal | Pass |
|--------|------|
| `nvcc --version` | `release 12.1` or higher |
| `nvidia-smi` | GPU detected, driver reported |
| `which nvcc` | non-empty path |
| `ls /usr/local/` | contains `cuda-12.x/` or `cuda/` symlink |

If any FAIL: follow NVIDIA's WSL CUDA install guide before T031.

## Rollback

Read-only check — nothing to roll back.

## Relationships

- PART OF: [[e008-m001-ktransformers-install-and-config|e008-m001-ktransformers-install-and-config]]
- PART OF: [[E008-local-k2-6-offline-frontier-tier|E008-local-k2-6-offline-frontier-tier]]

## Backlinks

[[e008-m001-ktransformers-install-and-config|e008-m001-ktransformers-install-and-config]]
[[E008-local-k2-6-offline-frontier-tier|E008-local-k2-6-offline-frontier-tier]]
