---
title: "T031 — Create Dedicated venv at /home/jfortin/ktransformers-env/"
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
depends_on:
  - "T030"
confidence: high
created: 2026-04-22
updated: 2026-04-22
sources:
  - id: e008-m001-ktransformers-install-and-config
    type: wiki
    file: wiki/backlog/modules/e008-m001-ktransformers-install-and-config.md
tags: [task, p1, e008, python, venv, preparation, isolation]
---

# T031 — Create ktransformers venv

## Summary

Create a dedicated Python 3.11 virtualenv at `/home/jfortin/ktransformers-env/` to isolate KTransformers + torch from the system Python and from AICP's own venv. Can run today, no hardware/RAM dependency.

## Done When

- [ ] `python3.11 --version` reports 3.11.x (install if missing)
- [ ] `/home/jfortin/ktransformers-env/` exists and is a valid venv
- [ ] Activating the venv (`source /home/jfortin/ktransformers-env/bin/activate`) works
- [ ] Inside the venv: `pip --version`, `python --version` report expected values
- [ ] `pip install --upgrade pip wheel setuptools` completes in the venv
- [ ] A stub `requirements.lock.txt` file initialized (will fill in T032)

## Procedure

```bash
# Python 3.11 check
python3.11 --version || { echo "install python3.11 first"; exit 1; }

# Create venv
python3.11 -m venv /home/jfortin/ktransformers-env
source /home/jfortin/ktransformers-env/bin/activate

# Baseline tooling
pip install --upgrade pip wheel setuptools

# Sanity
python --version
pip --version
which python pip

# Stub lockfile
touch /home/jfortin/ktransformers-env/requirements.lock.txt

deactivate
```

## Rollback

```bash
rm -rf /home/jfortin/ktransformers-env
```

Fully self-contained; no system changes.

## Relationships

- PART OF: [[e008-m001-ktransformers-install-and-config|e008-m001-ktransformers-install-and-config]]
- PART OF: [[E008-local-k2-6-offline-frontier-tier|E008-local-k2-6-offline-frontier-tier]]
- DEPENDS ON: [[T030-verify-cuda-toolchain|T030-verify-cuda-toolchain]]

## Backlinks

[[e008-m001-ktransformers-install-and-config|e008-m001-ktransformers-install-and-config]]
[[E008-local-k2-6-offline-frontier-tier|E008-local-k2-6-offline-frontier-tier]]
[[T030-verify-cuda-toolchain|T030-verify-cuda-toolchain]]
