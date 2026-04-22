---
title: "E012 M001 — Unsloth Toolchain Install (GPU build, 19 GB VRAM)"
type: module
domain: backlog
status: draft
priority: P2
task_type: module
current_stage: design
readiness: 85
progress: 0
stages_completed: [document]
artifacts: []
epic: "E012"
depends_on: []
confidence: high
created: 2026-04-22
updated: 2026-04-22
sources:
  - id: e012-custom-model-library-unsloth-loras
    type: wiki
    file: wiki/backlog/epics/pre-milestone/E012-custom-model-library-unsloth-loras.md
  - id: src-unsloth-synthesis
    type: wiki
    file: wiki/sources/tools-integration/src-unsloth-fast-lora-consumer-hardware.md
  - id: unsloth-repo
    type: repository
    url: https://github.com/unslothai/unsloth
    title: "Unsloth AI — unslothai/unsloth"
tags: [module, p2, e012, unsloth, lora, install, cuda, gpu, training-toolchain]
---

# E012 M001 — Unsloth Toolchain Install

## Summary

Install Unsloth into a dedicated Python 3.11 venv separate from the KTransformers venv (E008 M001) and AICP's venv — LoRA fine-tuning needs a specific torch + xformers + bitsandbytes matrix, and mixing with inference envs creates version conflicts. After install, verify CUDA-aware import and run Unsloth's own smoke notebook to confirm the training path works end-to-end before committing to the full Wiki-Assistant training run (M002).

## Tasks

| Task | Title | Readiness | Progress | Status |
|------|-------|-----------|----------|--------|
| T058 | Create /home/jfortin/unsloth-env/ venv + install unsloth | 100% | 0% | draft |
| T059 | Smoke Unsloth with its canonical example (Qwen small model) | 80% | 0% | draft |

## Dependencies

- CUDA 12.1+ toolkit (same as E008 M001's T030).
- 19 GB VRAM (sufficient for Qwen3.5-4B + LoRA rank 32).
- 20-30 GB disk for torch + xformers wheels + example model cache.
- Python 3.11.

## Done When

- [ ] `/home/jfortin/unsloth-env/` venv exists and is activatable
- [ ] `pip show unsloth` reports a version inside the venv
- [ ] `python -c "import unsloth; print(unsloth.__version__)"` succeeds
- [ ] `python -c "from unsloth import FastLanguageModel; print('ok')"` succeeds
- [ ] Canonical Unsloth smoke notebook (or CLI equivalent) runs a 1-epoch training on a tiny model without OOM
- [ ] Install log at `wiki/log/2026-04-28-unsloth-install.md` with resolved versions + smoke result
- [ ] All child tasks at status: done

## Procedure (reference)

### Step 1 — Dedicated venv

```bash
python3.11 -m venv /home/jfortin/unsloth-env
source /home/jfortin/unsloth-env/bin/activate
pip install --upgrade pip wheel setuptools
```

### Step 2 — Install Unsloth

Unsloth's README has the canonical install command; matrix depends on CUDA version:

```bash
# For CUDA 12.1+
pip install "unsloth[colab-new] @ git+https://github.com/unslothai/unsloth.git"
# Or stable wheel:
pip install unsloth
```

Possible companion deps:

```bash
pip install xformers trl datasets peft accelerate bitsandbytes
```

### Step 3 — Smoke import

```bash
python -c "
import torch; print('torch CUDA:', torch.cuda.is_available(), torch.version.cuda)
import unsloth; print('unsloth:', unsloth.__version__)
from unsloth import FastLanguageModel
print('FastLanguageModel import ok')
"
```

### Step 4 — Canonical tiny-model smoke

Follow Unsloth's Qwen3.5-0.5B example (from their README / notebooks). Run for 1 epoch on a tiny dataset. Success means: no OOM, loss decreases, a few output tokens generate after training.

### Step 5 — Log

```bash
cd /home/jfortin/devops-solutions-research-wiki
python3 -m tools.pipeline scaffold note "2026-04-28-unsloth-install"
$EDITOR wiki/log/2026-04-28-unsloth-install.md
python3 -m tools.pipeline post
```

## Rollback

```bash
deactivate
rm -rf /home/jfortin/unsloth-env
```

Self-contained venv; no system changes.

## Impediments

| Impediment | Type | Blocked Since | Escalated? | Resolution |
|-----------|------|---------------|-----------|------------|
| xformers wheel may lag torch version | dependency | 2026-04-22 | no | Let Unsloth pin the matrix; don't pre-install torch |
| bitsandbytes WSL2 build | environment | 2026-04-22 | no | Unsloth's install.sh handles; fallback to from-source if needed |
| VRAM margin at 19 GB for Qwen3.5-4B + LoRA rank 32 | hardware | 2026-04-22 | no | Smoke with rank 16 first; up to 32 if headroom allows |

## Relationships

- PART OF: [[E012-custom-model-library-unsloth-loras|E012-custom-model-library-unsloth-loras]]
- FEEDS INTO: [[e012-m002-wiki-assistant-candidate-a|e012-m002-wiki-assistant-candidate-a]]
- FEEDS INTO: [[e012-m003-wiki-router-candidate-d|e012-m003-wiki-router-candidate-d]]
- FEEDS INTO: [[e012-m004-multi-lora-adapter-architecture-e|e012-m004-multi-lora-adapter-architecture-e]]

## Backlinks

[[E012-custom-model-library-unsloth-loras|E012-custom-model-library-unsloth-loras]]
[[e012-m002-wiki-assistant-candidate-a|e012-m002-wiki-assistant-candidate-a]]
[[e012-m003-wiki-router-candidate-d|e012-m003-wiki-router-candidate-d]]
[[e012-m004-multi-lora-adapter-architecture-e|e012-m004-multi-lora-adapter-architecture-e]]
