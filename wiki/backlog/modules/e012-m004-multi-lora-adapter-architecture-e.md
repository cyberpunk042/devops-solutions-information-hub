---
title: "E012 M004 — Multi-LoRA Adapter Architecture (Candidate E, base + N adapters)"
type: module
domain: backlog
status: draft
priority: P2
task_type: module
current_stage: design
readiness: 60
progress: 0
stages_completed: [document]
artifacts: []
epic: "E012"
depends_on:
  - "E012-m001"
  - "E012-m002"
confidence: medium
created: 2026-04-22
updated: 2026-04-22
sources:
  - id: e012-custom-model-library-unsloth-loras
    type: wiki
    file: wiki/backlog/epics/pre-milestone/E012-custom-model-library-unsloth-loras.md
  - id: second-brain-custom-model-strategy
    type: wiki
    file: wiki/spine/references/second-brain-custom-model-strategy.md
tags: [module, p2, e012, multi-lora, candidate-e, adapter-swap, peft, specialization]
---

# E012 M004 — Multi-LoRA Adapter Architecture

## Summary

Establish the "one base model + many small adapters" pattern: a shared Qwen3.5-4B base, plus 3 specialized LoRA adapters swapped in at inference time per task — **methodology-assistant** (wiki standards + verbs + principles), **compliance-checker** (lint + page-schema validator), **relationship-suggester** (cross-link recommender). Drastically reduces storage per skill (~50 MB per adapter vs 2.5 GB per full model). Mechanism: PEFT / Unsloth's adapter-loading API, measured swap latency, documented accuracy per adapter.

## Tasks

| Task | Title | Readiness | Progress | Status |
|------|-------|-----------|----------|--------|
| T070 | Design 3 adapter training datasets (methodology, compliance, relationship) | 70% | 0% | draft |
| T071 | Train methodology-assistant adapter on Qwen3.5-4B base | 65% | 0% | draft |
| T072 | Train compliance-checker adapter (schema errors + fixes from pipeline logs) | 65% | 0% | draft |
| T073 | Train relationship-suggester adapter (existing cross-refs as labels) | 65% | 0% | draft |
| T074 | Benchmark adapter-swap latency (cold vs warm) | 80% | 0% | draft |
| T075 | Per-adapter holdout evaluation + accuracy documentation | 70% | 0% | draft |
| T076 | Serve adapter selection via AICP tier sub-router | 60% | 0% | draft |
| T077 | Publish adapter library page + usage guide | 80% | 0% | draft |

## Dependencies

- **E012 M001** — Unsloth + PEFT.
- **E012 M002** — Wiki-Assistant trained (shares the Qwen3.5-4B base; M004 can start from the same base weights or from M002's methodology-fine-tuned base).
- Three targeted datasets (one per adapter).

## Done When

- [ ] 3 datasets, each ≥100 labeled examples, stored under `/mnt/models/datasets/`
- [ ] 3 LoRA adapters trained, each ≤100 MB on disk, stored under `/mnt/models/adapters/`
- [ ] Per-adapter holdout accuracy ≥ chosen baseline (baselines TBD per task)
- [ ] Adapter-swap latency measured: cold load (new process) and warm swap (same process)
- [ ] Warm swap <500 ms (target — PEFT's adapter switch is typically fast)
- [ ] AICP router sub-tier logic: `local-wiki-maintenance` → pick adapter based on prompt hint or complexity-scorer signal
- [ ] `wiki/spine/references/custom-adapter-library.md` published with per-adapter description, training data, accuracy, use cases
- [ ] All child tasks at status: done

## Procedure (reference)

### Step 1 — Dataset design

For each adapter, design the SFT template:

- **methodology-assistant**: Q&A over standards/models/verbs/principles. Positive examples: correct invocation of verbs; correct standard citation.
- **compliance-checker**: input = draft page with lint issues, output = list of fixes with line refs. Bootstrap from pipeline lint output logs.
- **relationship-suggester**: input = draft page summary, output = suggested BUILDS ON / FEEDS INTO relationships to existing pages. Bootstrap from cross-ref graph mined from manifest.

### Step 2 — Train each adapter

Use the same base (Qwen3.5-4B), vary LoRA config:

```bash
source /home/jfortin/unsloth-env/bin/activate

for task in methodology-assistant compliance-checker relationship-suggester; do
  python tools/train_adapter.py \
    --base unsloth/Qwen3.5-4B-bnb-4bit \
    --dataset /mnt/models/datasets/$task-v1.jsonl \
    --lora-rank 16 \
    --epochs 3 \
    --out /mnt/models/adapters/$task-v1
done
```

### Step 3 — Swap benchmark

```python
# tools/bench_adapter_swap.py
from unsloth import FastLanguageModel
from peft import PeftModel
import time

base, tok = FastLanguageModel.from_pretrained("unsloth/Qwen3.5-4B-bnb-4bit")

# Cold load
t0 = time.time()
m1 = PeftModel.from_pretrained(base, "/mnt/models/adapters/methodology-assistant-v1")
print(f"cold load: {time.time() - t0:.3f}s")

# Warm swap (same process)
t0 = time.time()
m1.load_adapter("/mnt/models/adapters/compliance-checker-v1", "compliance")
m1.set_adapter("compliance")
print(f"warm swap: {time.time() - t0:.3f}s")
```

### Step 4 — Per-adapter eval

Each adapter has a task-specific holdout set. Report accuracy + sample outputs in the adapter library doc.

### Step 5 — AICP integration

Extend `k2_6_local` / `local_wiki_maintenance` adapter dispatching: based on a tag in the AICP request (or the classifier from M003), pick the right adapter, swap, run inference.

## Rollback

```bash
rm -rf /mnt/models/adapters
```

## Impediments

| Impediment | Type | Blocked Since | Escalated? | Resolution |
|-----------|------|---------------|-----------|------------|
| Small datasets (≥100 pairs) may be too few for adapter specialization | data | 2026-04-22 | no | Start with 100; grow to 300 if accuracy is low |
| Warm-swap latency regression if adapter rank high | perf | 2026-04-22 | no | Keep rank 16 per adapter; measure; raise only if accuracy demands |
| Deciding when the router picks adapter vs K2.6 | design | 2026-04-22 | no | Default: K2.6 for anything outside the adapter's training distribution |

## Relationships

- PART OF: [[E012-custom-model-library-unsloth-loras|E012-custom-model-library-unsloth-loras]]
- DEPENDS ON: [[e012-m001-unsloth-toolchain-install|e012-m001-unsloth-toolchain-install]]
- DEPENDS ON: [[e012-m002-wiki-assistant-candidate-a|e012-m002-wiki-assistant-candidate-a]]
- RELATES TO: [[e011-m001-tier-definitions-update|e011-m001-tier-definitions-update]]

## Backlinks

[[E012-custom-model-library-unsloth-loras|E012-custom-model-library-unsloth-loras]]
[[e012-m001-unsloth-toolchain-install|e012-m001-unsloth-toolchain-install]]
[[e012-m002-wiki-assistant-candidate-a|e012-m002-wiki-assistant-candidate-a]]
[[e011-m001-tier-definitions-update|e011-m001-tier-definitions-update]]
