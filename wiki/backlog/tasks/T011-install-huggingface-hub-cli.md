---
title: "T011 — Install huggingface_hub CLI (prerequisite for K2.6 download)"
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
module: "E008-m002"
depends_on: []
confidence: high
created: 2026-04-22
updated: 2026-04-22
sources:
  - id: e008-m002-k2-6-q2-gguf-download-and-verify
    type: wiki
    file: wiki/backlog/modules/e008-m002-k2-6-q2-gguf-download-and-verify.md
tags: [task, p1, e008, huggingface, cli, install, preparation]
---

# T011 — Install huggingface_hub CLI

## Summary

Install the `huggingface_hub[cli]` Python package so the `hf` command is available for the K2.6 Q2 download (T012). This is operator-runnable today — no hardware prereqs.

## Done When

- [ ] `pip install --user 'huggingface_hub[cli]'` completes without error
- [ ] `hf --help` prints usage (OR `huggingface-cli --help` on older versions)
- [ ] `hf auth whoami` returns a valid username (after `hf auth login`, if needed)
- [ ] Package version captured in wiki log or install notes

## Procedure

```bash
# Outside any venv (user-site install) — simplest for the download stage
pip install --user 'huggingface_hub[cli]'
hf --help || huggingface-cli --help

# If gated models are ever needed (not expected for unsloth/Kimi-K2.6-GGUF which is public)
hf auth login
hf auth whoami
```

## Rollback

```bash
pip uninstall -y huggingface_hub
```

## Relationships

- PART OF: [[e008-m002-k2-6-q2-gguf-download-and-verify|e008-m002-k2-6-q2-gguf-download-and-verify]]
- PART OF: [[E008-local-k2-6-offline-frontier-tier|E008-local-k2-6-offline-frontier-tier]]

## Backlinks

[[e008-m002-k2-6-q2-gguf-download-and-verify|e008-m002-k2-6-q2-gguf-download-and-verify]]
[[E008-local-k2-6-offline-frontier-tier|E008-local-k2-6-offline-frontier-tier]]
