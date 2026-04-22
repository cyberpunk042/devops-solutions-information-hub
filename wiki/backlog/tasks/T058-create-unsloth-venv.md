---
title: "T058 — Create /home/jfortin/unsloth-env/ venv + Install unsloth"
type: task
domain: backlog
status: draft
priority: P2
task_type: task
current_stage: design
readiness: 100
progress: 0
stages_completed: [document, design]
artifacts: []
estimate: S
epic: "E012"
module: "E012-m001"
depends_on: []
confidence: high
created: 2026-04-22
updated: 2026-04-22
sources:
  - id: e012-m001-unsloth-toolchain-install
    type: wiki
    file: wiki/backlog/modules/e012-m001-unsloth-toolchain-install.md
tags: [task, p2, e012, unsloth, venv, install, preparation]
---

# T058 — Create unsloth-env venv + Install

## Summary

Create a dedicated Python 3.11 virtualenv at `/home/jfortin/unsloth-env/` and install `unsloth` + companion deps (trl, peft, datasets, accelerate, bitsandbytes). Runnable today — no RAM dependency. Smoke import proves the install; actual training waits for E012 M002 onwards.

## Done When

- [ ] `/home/jfortin/unsloth-env/` is a valid Python 3.11 venv
- [ ] `pip show unsloth` inside venv returns a version
- [ ] `python -c "import unsloth; from unsloth import FastLanguageModel; print(unsloth.__version__)"` succeeds
- [ ] `python -c "import torch; print(torch.cuda.is_available(), torch.version.cuda)"` prints True + 12.x
- [ ] `python -c "import bitsandbytes, peft, trl, datasets; print('deps ok')"` succeeds
- [ ] Version + install notes recorded in a local scratch file (feeds into the install log at M001 close)

## Procedure

```bash
# Sanity check Python 3.11 available
python3.11 --version

# Create venv
python3.11 -m venv /home/jfortin/unsloth-env
source /home/jfortin/unsloth-env/bin/activate
pip install --upgrade pip wheel setuptools

# Install unsloth + deps (let unsloth pin torch version)
pip install unsloth
pip install xformers trl datasets peft accelerate bitsandbytes

# Smoke
python -c "
import unsloth, torch, peft, trl, datasets, bitsandbytes
print('unsloth:', unsloth.__version__)
print('torch CUDA:', torch.cuda.is_available(), torch.version.cuda)
print('deps ok')
"
```

## Rollback

```bash
deactivate
rm -rf /home/jfortin/unsloth-env
```

## Relationships

- PART OF: [[e012-m001-unsloth-toolchain-install|e012-m001-unsloth-toolchain-install]]
- PART OF: [[E012-custom-model-library-unsloth-loras|E012-custom-model-library-unsloth-loras]]

## Backlinks

[[e012-m001-unsloth-toolchain-install|e012-m001-unsloth-toolchain-install]]
[[E012-custom-model-library-unsloth-loras|E012-custom-model-library-unsloth-loras]]
