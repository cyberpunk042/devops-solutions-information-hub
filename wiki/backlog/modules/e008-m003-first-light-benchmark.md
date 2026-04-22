---
title: "E008 M003 — K2.6 First-Light Benchmark (cold start + tok/s at 3 contexts)"
type: module
domain: backlog
status: draft
priority: P1
task_type: module
current_stage: design
readiness: 70
progress: 0
stages_completed: [document]
artifacts:
  - wiki/log/2026-04-24-k2-6-local-first-light.md
epic: "E008"
depends_on:
  - "E008-m001"
  - "E008-m002"
confidence: medium
created: 2026-04-22
updated: 2026-04-22
sources:
  - id: e008-local-k2-6-offline-frontier-tier
    type: wiki
    file: wiki/backlog/epics/pre-milestone/E008-local-k2-6-offline-frontier-tier.md
tags: [module, p1, e008, ktransformers, benchmark, k2-6, tok-per-s, first-light]
---

# E008 M003 — K2.6 First-Light Benchmark

## Summary

Run the first real inference on K2.6 Q2 locally and measure three axes: cold-start time (load + first token), sustained tokens/sec at steady state, and behavior at three context sizes (1K / 32K / 256K). The benchmark produces the authoritative number for "is local K2.6 usable on operator's hardware?". Also runs a quality A/B against K2.6-via-OpenRouter on 3 identical wiki-typical prompts to confirm QAT-INT4 parity.

## Tasks

| Task | Title | Readiness | Progress | Status |
|------|-------|-----------|----------|--------|
| T033 | Author kt-smoke.sh script (single-prompt, times the run) | 100% | 0% | draft |
| T034 | Run benchmark suite at 1K / 32K / 256K context, record results | 70% | 0% | draft |
| T035 | Quality A/B vs OpenRouter K2.6 on 3 wiki-typical prompts | 80% | 0% | draft |

## Dependencies

- **E008 M001** — KTransformers importable and configured.
- **E008 M002** — K2.6 Q2 weights present at `/mnt/models/kimi-k2-6-q2/`.
- **E010 M001** — 64 GB RAM strongly recommended for 32K+ context runs.

## Done When

- [ ] `scripts/kt-smoke.sh` exists and prints {load_time, first_token_time, completion_tokens, total_time, tok_per_s}
- [ ] Cold-start time recorded (separate from warm generation)
- [ ] Sustained tok/s measured at 1K context — recorded
- [ ] Sustained tok/s measured at 32K context — recorded
- [ ] 256K context: either records tok/s OR documents OOM / memory-pressure observation
- [ ] Quality A/B: 3 prompts run via local + via OpenRouter; outputs compared; diff documented
- [ ] `wiki/log/2026-04-24-k2-6-local-first-light.md` published with: setup commands, results tables, gotchas, recommended operating context size
- [ ] Decision recorded: "local K2.6 is usable / limited / not viable on this hardware — because ..."

## Procedure (reference)

### Step 1 — Author kt-smoke.sh

```bash
cd /home/jfortin/devops-solutions-research-wiki
$EDITOR scripts/kt-smoke.sh
chmod +x scripts/kt-smoke.sh
```

Minimum content (tentative — adapt to actual KTransformers CLI):

```bash
#!/usr/bin/env bash
set -euo pipefail

MODEL=/mnt/models/kimi-k2-6-q2/UD-Q2_K_XL
PROMPT="${1:-"Write a short poem about disk I/O in free verse."}"
MAX_TOK="${2:-200}"
OPT_CONFIG="${3:-optimizations/kimi-k2.6.yaml}"

source /home/jfortin/ktransformers-env/bin/activate

python -m ktransformers.local_chat \
  --model-path "$MODEL" \
  --gguf-path "$MODEL" \
  --optimize-config-path "$OPT_CONFIG" \
  --prompt "$PROMPT" \
  --max-new-tokens "$MAX_TOK" \
  --report-stats 2>&1 | tee /tmp/kt-smoke-$(date +%s).log
```

### Step 2 — Benchmark suite

```bash
# Cold start (no warmup)
time ./scripts/kt-smoke.sh "Hello, introduce yourself." 50

# Warm 1K context
./scripts/kt-smoke.sh "$(python -c 'print("foo " * 250)') End of prefix. Now summarize." 200

# Warm 32K context
./scripts/kt-smoke.sh "$(python -c 'print("foo " * 8000)') End of prefix. Now summarize." 200

# Warm 256K context (may OOM — capture either way)
./scripts/kt-smoke.sh "$(python -c 'print("foo " * 64000)') End of prefix. Now summarize." 200
```

### Step 3 — Quality A/B

Run 3 wiki-typical prompts through both backends and diff the outputs:

```bash
cd /home/jfortin/devops-expert-local-ai
source .env

PROMPTS=(
  "Explain the difference between mmap and swap for LLM inference in 3 bullet points."
  "Refactor this Python function to use type hints: def add(a, b): return a + b"
  "Summarize a 500-word essay about AI autonomy in 2 sentences: <insert any 500-word text>"
)

for i in "${!PROMPTS[@]}"; do
  p="${PROMPTS[$i]}"
  /home/jfortin/devops-solutions-research-wiki/scripts/kt-smoke.sh "$p" 400 > "/tmp/ab-local-$i.txt"
  python3 -m aicp.cli.main run --backend k2_6_openrouter "$p" > "/tmp/ab-cloud-$i.txt"
  diff "/tmp/ab-local-$i.txt" "/tmp/ab-cloud-$i.txt" > "/tmp/ab-diff-$i.txt" || true
done
```

### Step 4 — Publish results

```bash
cd /home/jfortin/devops-solutions-research-wiki
python3 -m tools.pipeline scaffold note "2026-04-24-k2-6-local-first-light"
$EDITOR wiki/log/2026-04-24-k2-6-local-first-light.md
python3 -m tools.pipeline post
```

## Rollback

Benchmark is read-only on model weights; rollback is just removing generated logs.

```bash
rm /tmp/kt-smoke-*.log /tmp/ab-*.txt
# Log page can stay (historical record)
```

## Impediments

| Impediment | Type | Blocked Since | Escalated? | Resolution |
|-----------|------|---------------|-----------|------------|
| 256K context may OOM on 64 GB RAM | hardware | 2026-04-22 | no | Document the ceiling; falls back to 32K-64K operational range |
| Optimization YAML for K2.6 may not ship with KTransformers | external | 2026-04-22 | no | Check `optimizations/` in ktransformers-src; may need to author one based on DeepSeek-V3 template |
| First run slow due to cold file system cache | expected | 2026-04-22 | no | Report cold + warm numbers separately |

## Relationships

- PART OF: [[E008-local-k2-6-offline-frontier-tier|E008-local-k2-6-offline-frontier-tier]]
- DEPENDS ON: [[e008-m001-ktransformers-install-and-config|e008-m001-ktransformers-install-and-config]]
- DEPENDS ON: [[e008-m002-k2-6-q2-gguf-download-and-verify|e008-m002-k2-6-q2-gguf-download-and-verify]]
- FEEDS INTO: [[e008-m004-local-backend-adapter|e008-m004-local-backend-adapter]]

## Backlinks

[[E008-local-k2-6-offline-frontier-tier|E008-local-k2-6-offline-frontier-tier]]
[[e008-m001-ktransformers-install-and-config|e008-m001-ktransformers-install-and-config]]
[[e008-m002-k2-6-q2-gguf-download-and-verify|e008-m002-k2-6-q2-gguf-download-and-verify]]
[[e008-m004-local-backend-adapter|e008-m004-local-backend-adapter]]
