---
title: "E008 M001 — KTransformers Install and CUDA Config"
type: module
domain: backlog
status: draft
priority: P1
task_type: module
current_stage: design
readiness: 75
progress: 0
stages_completed: [document]
artifacts: []
epic: "E008"
depends_on: []
confidence: medium
created: 2026-04-22
updated: 2026-04-22
sources:
  - id: e008-local-k2-6-offline-frontier-tier
    type: wiki
    file: wiki/backlog/epics/pre-milestone/E008-local-k2-6-offline-frontier-tier.md
  - id: ktransformers-repo
    type: repository
    url: https://github.com/kvcache-ai/ktransformers
    title: "KTransformers — kvcache.ai"
tags: [module, p1, e008, ktransformers, install, cuda, moe, disk-offload]
---

# E008 M001 — KTransformers Install and CUDA Config

## Summary

Install KTransformers (kvcache.ai's MoE-optimized inference engine) into a clean Python 3.11 virtualenv. KTransformers has strict CUDA requirements (>= 12.1) and needs a C++/CUDA build toolchain available because parts of the codebase compile at install time. This module verifies the toolchain, installs the package (from source if wheels unavailable for operator's CUDA version), and confirms `import ktransformers` works. Does NOT download weights (E008 M002) or start the server (E008 M004).

## Tasks

| Task | Title | Readiness | Progress | Status |
|------|-------|-----------|----------|--------|
| T030 | Verify CUDA toolchain + GPU driver compatibility | 100% | 0% | draft |
| T031 | Create dedicated venv at /home/jfortin/ktransformers-env/ | 100% | 0% | draft |
| T032 | Install ktransformers (pip or from-source) and smoke-import | 75% | 0% | draft |

## Dependencies

- **E010 M001** — 64 GB RAM recommended (install itself works on 32 GB, but downstream benchmarks will fail at 32 GB for K2.6 Q2).
- CUDA 12.1+ toolkit on the Linux side of WSL2. Check via `nvcc --version` and `nvidia-smi`.
- Python 3.11 (KTransformers as of 2026-04 supports 3.10/3.11; 3.12 compatibility unconfirmed).
- ~5 GB free space for venv + compile artifacts (separate from model weights).

## Done When

- [ ] `nvcc --version` reports CUDA >= 12.1
- [ ] `nvidia-smi` shows the GPU and driver compatible with the CUDA toolkit
- [ ] Dedicated venv at `/home/jfortin/ktransformers-env/` exists and is activatable
- [ ] `pip show ktransformers` inside the venv returns a version
- [ ] `python -c "import ktransformers; print(ktransformers.__version__)"` succeeds
- [ ] If a from-source install was necessary, the build log is archived at `/home/jfortin/ktransformers-env/build.log`
- [ ] Install procedure captured in `wiki/log/2026-04-23-ktransformers-install.md` with exact commands + resolved version numbers
- [ ] All child tasks at status: done

## Procedure (reference)

### Step 1 — Verify CUDA toolchain

```bash
nvcc --version          # expect: release 12.1 or higher
nvidia-smi              # expect: driver version compatible with nvcc
which nvcc              # /usr/local/cuda-12.x/bin/nvcc (or similar)
echo $CUDA_HOME         # should point to /usr/local/cuda or similar; set if missing
```

If toolkit is absent, install from NVIDIA's WSL CUDA guide BEFORE proceeding.

### Step 2 — Create venv

```bash
python3.11 -m venv /home/jfortin/ktransformers-env
source /home/jfortin/ktransformers-env/bin/activate
pip install --upgrade pip wheel setuptools
```

### Step 3 — Install KTransformers

```bash
# Preferred: pre-built wheel
pip install ktransformers

# If wheel missing for operator's CUDA version, build from source:
git clone https://github.com/kvcache-ai/ktransformers /home/jfortin/ktransformers-src
cd /home/jfortin/ktransformers-src
git submodule update --init --recursive
pip install -r requirements-local_chat.txt
USE_BALANCE_SERVE=1 bash install.sh 2>&1 | tee /home/jfortin/ktransformers-env/build.log
```

### Step 4 — Smoke import

```bash
python -c "
import ktransformers
print('ktransformers version:', ktransformers.__version__)
import torch
print('torch CUDA available:', torch.cuda.is_available())
print('torch CUDA version:', torch.version.cuda)
"
```

### Step 5 — Archive install log

```bash
$EDITOR /home/jfortin/devops-solutions-research-wiki/wiki/log/2026-04-23-ktransformers-install.md
# Fields: CUDA version, Python version, ktransformers version, from-source vs wheel,
#         gotchas encountered, verification commands
```

## Rollback

```bash
deactivate
rm -rf /home/jfortin/ktransformers-env
rm -rf /home/jfortin/ktransformers-src    # if built from source
```

No system-level changes; venv is self-contained.

## Impediments

| Impediment | Type | Blocked Since | Escalated? | Resolution |
|-----------|------|---------------|-----------|------------|
| WSL2 CUDA passthrough can be finicky | environment | 2026-04-22 | no | Follow NVIDIA's WSL CUDA guide; `nvidia-smi` must work inside WSL before attempting install |
| From-source build can take 30-60 min | time | 2026-04-22 | no | Run overnight; archive log for debugging |
| ktransformers requires specific torch build | dependency | 2026-04-22 | no | Let install.sh manage torch version; don't pre-install an incompatible torch |

## Relationships

- PART OF: [[E008-local-k2-6-offline-frontier-tier|E008-local-k2-6-offline-frontier-tier]]
- FEEDS INTO: [[e008-m003-first-light-benchmark|e008-m003-first-light-benchmark]]
- FEEDS INTO: [[e008-m004-local-backend-adapter|e008-m004-local-backend-adapter]]

## Backlinks

[[E008-local-k2-6-offline-frontier-tier|E008-local-k2-6-offline-frontier-tier]]
[[e008-m003-first-light-benchmark|e008-m003-first-light-benchmark]]
[[e008-m004-local-backend-adapter|e008-m004-local-backend-adapter]]
