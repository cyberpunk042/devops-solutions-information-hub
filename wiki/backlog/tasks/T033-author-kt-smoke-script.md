---
title: "T033 — Author scripts/kt-smoke.sh (benchmark harness)"
type: task
domain: backlog
status: draft
priority: P1
task_type: task
current_stage: design
readiness: 90
progress: 0
stages_completed: [document, design]
artifacts:
  - scripts/kt-smoke.sh
estimate: XS
epic: "E008"
module: "E008-m003"
depends_on: []
confidence: high
created: 2026-04-22
updated: 2026-04-22
sources:
  - id: e008-m003-first-light-benchmark
    type: wiki
    file: wiki/backlog/modules/e008-m003-first-light-benchmark.md
tags: [task, p1, e008, script, benchmark, scaffold, kt-smoke]
---

# T033 — Author kt-smoke.sh

## Summary

Scaffold the benchmark harness script at `scripts/kt-smoke.sh` (in the wiki repo, since that's where methodology + tools live). Times a single prompt and reports {load_time, first_token_time, completion_tokens, total_time, tok_per_s}. Can be written today; validated against real inference once E008 M001 + M002 land.

## Done When

- [ ] `scripts/kt-smoke.sh` exists and is executable (chmod +x)
- [ ] Positional args: `$1` = prompt (default: test prompt), `$2` = max tokens (default: 200), `$3` = optimization YAML path (default: optimizations/kimi-k2.6.yaml)
- [ ] Env vars: `KT_MODEL_PATH` (default: `/mnt/models/kimi-k2-6-q2/UD-Q2_K_XL`), `KT_VENV` (default: `/home/jfortin/ktransformers-env`)
- [ ] Script activates the venv, invokes `python -m ktransformers.local_chat` with appropriate flags, tees output to a timestamped log in `/tmp/kt-smoke-<ts>.log`
- [ ] Script parses the output to print a one-line stats summary at the end
- [ ] Script exits non-zero on invocation failure
- [ ] `shellcheck scripts/kt-smoke.sh` passes with no errors (style warnings acceptable)
- [ ] Committed with message: `feat(scripts): scaffold kt-smoke.sh for E008 M003 benchmark`

## Procedure

```bash
cd /home/jfortin/devops-solutions-research-wiki
mkdir -p scripts
$EDITOR scripts/kt-smoke.sh
chmod +x scripts/kt-smoke.sh
shellcheck scripts/kt-smoke.sh || true

# Smoke the script logic (won't actually run inference until weights present)
./scripts/kt-smoke.sh --help 2>&1 || true
```

Canonical content: see `e008-m003-first-light-benchmark.md` Step 1.

## Rollback

```bash
rm scripts/kt-smoke.sh
```

## Relationships

- PART OF: [[e008-m003-first-light-benchmark|e008-m003-first-light-benchmark]]
- PART OF: [[E008-local-k2-6-offline-frontier-tier|E008-local-k2-6-offline-frontier-tier]]

## Backlinks

[[e008-m003-first-light-benchmark|e008-m003-first-light-benchmark]]
[[E008-local-k2-6-offline-frontier-tier|E008-local-k2-6-offline-frontier-tier]]
