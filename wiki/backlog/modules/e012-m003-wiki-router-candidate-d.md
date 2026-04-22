---
title: "E012 M003 — Wiki-Router (Candidate D, Qwen3.5-0.5B complexity classifier)"
type: module
domain: backlog
status: draft
priority: P2
task_type: module
current_stage: design
readiness: 70
progress: 0
stages_completed: [document]
artifacts: []
epic: "E012"
depends_on:
  - "E012-m001"
confidence: medium
created: 2026-04-22
updated: 2026-04-22
sources:
  - id: e012-custom-model-library-unsloth-loras
    type: wiki
    file: wiki/backlog/epics/pre-milestone/E012-custom-model-library-unsloth-loras.md
  - id: aicp-router
    type: repository
    file: /home/jfortin/devops-expert-local-ai/aicp/core/router.py
tags: [module, p2, e012, wiki-router, candidate-d, qwen, complexity-classifier, lora, aicp]
---

# E012 M003 — Wiki-Router (Candidate D)

## Summary

Train a tiny fast classifier (Qwen3.5-0.5B or 1.5B + LoRA) that replaces or augments AICP's current heuristic complexity scorer (`analyze_complexity()` in `aicp/core/router.py`). Outputs a tier-class token — `local`, `k2_6_local`, `k2_6_openrouter`, `openrouter`, `claude` — with higher accuracy than keyword/length heuristics on operator's real task distribution. Small enough to run on CPU or a few hundred MB VRAM so routing latency stays <100 ms.

## Tasks

| Task | Title | Readiness | Progress | Status |
|------|-------|-----------|----------|--------|
| T066 | Collect 500+ labeled examples from AICP JSONL log (backfill labels from human override data) | 65% | 0% | draft |
| T067 | Fine-tune Qwen3.5-0.5B + LoRA for 5-class classification | 70% | 0% | draft |
| T068 | Evaluate vs current heuristic on held-out set; decide rule vs. ML vs. hybrid | 80% | 0% | draft |
| T069 | Integrate as classifier hook in aicp/core/router.py | 75% | 0% | draft |

## Dependencies

- **E012 M001** — Unsloth usable.
- **E011 M002** — AICP emitting metrics with per-request (prompt, chosen_backend, cost, latency) so we can backfill training data.
- A few weeks of real routing decisions to bootstrap labels (ideally after E011 goes live).

## Done When

- [ ] Labeled dataset: ≥500 examples with (prompt, mode, chosen_tier_label) tuples stored at `/mnt/models/datasets/wiki-router-v1.jsonl`
- [ ] Qwen3.5-0.5B + LoRA trained; inference latency <100 ms on CPU (or <20 ms on GPU)
- [ ] Holdout accuracy ≥ baseline heuristic accuracy + 10 pp OR documented as "not worth replacing"
- [ ] Decision recorded: replace heuristic, augment heuristic (hybrid), or abandon
- [ ] If chosen: classifier integrated as `router.ml_classifier` hook in `aicp/core/router.py` with config flag `router.use_ml_classifier: true`
- [ ] Latency added to classification path measured and documented
- [ ] All child tasks at status: done

## Procedure (reference)

### Step 1 — Collect + label data

```bash
# Bootstrap: AICP's JSONL log already contains (prompt, backend, cost, latency).
# Label = the backend that was chosen. Filter out failover events (those are noise).
python tools/build_wiki_router_dataset.py \
  --log "${AICP_LOG_FILE:-$HOME/.aicp/events.jsonl}" \
  --min-examples-per-class 50 \
  --out /mnt/models/datasets/wiki-router-v1.jsonl
```

Supplement with hand-labeled borderline cases if volume is low.

### Step 2 — Train

```bash
source /home/jfortin/unsloth-env/bin/activate
python tools/train_wiki_router.py \
  --base unsloth/Qwen3.5-0.5B-bnb-4bit \
  --dataset /mnt/models/datasets/wiki-router-v1.jsonl \
  --lora-rank 16 \
  --epochs 5 \
  --out /mnt/models/wiki-router-v1-lora
```

### Step 3 — Evaluate

```bash
python tools/eval_wiki_router.py \
  --lora /mnt/models/wiki-router-v1-lora \
  --heuristic-baseline aicp/core/router.py \
  --holdout /mnt/models/datasets/wiki-router-holdout.jsonl
# Outputs: accuracy, F1 per class, avg latency
```

### Step 4 — Integrate (if keep)

In `aicp/core/router.py`, add a hook that, when `router.use_ml_classifier: true`, invokes the classifier and uses its output alongside or instead of the heuristic. Preserve a fallback to the heuristic if classifier inference fails.

## Rollback

```bash
rm -rf /mnt/models/wiki-router-v1-lora
# Config rollback: set router.use_ml_classifier: false in ~/.aicp/config.yaml
```

## Impediments

| Impediment | Type | Blocked Since | Escalated? | Resolution |
|-----------|------|---------------|-----------|------------|
| Bootstrap labels come from current heuristic → classifier can't beat it | data | 2026-04-22 | no | Include operator-correction data once collected; hand-label 100 borderline cases |
| 5-class is coarse — some prompts genuinely span 2 tiers | design | 2026-04-22 | no | Emit top-2 with confidence; tier choice considers confidence |
| Classifier adds latency to every routing decision | perf | 2026-04-22 | no | Keep model tiny (0.5B); CPU inference OK; cache recent prompts |

## Relationships

- PART OF: [[E012-custom-model-library-unsloth-loras|E012-custom-model-library-unsloth-loras]]
- DEPENDS ON: [[e012-m001-unsloth-toolchain-install|e012-m001-unsloth-toolchain-install]]
- RELATES TO: [[e011-m002-k2-6-openrouter-backend-adapter|e011-m002-k2-6-openrouter-backend-adapter]]
- RELATES TO: [[e011-m005-routing-metric-and-review-ritual|e011-m005-routing-metric-and-review-ritual]]

## Backlinks

[[E012-custom-model-library-unsloth-loras|E012-custom-model-library-unsloth-loras]]
[[e012-m001-unsloth-toolchain-install|e012-m001-unsloth-toolchain-install]]
[[e011-m002-k2-6-openrouter-backend-adapter|e011-m002-k2-6-openrouter-backend-adapter]]
[[e011-m005-routing-metric-and-review-ritual|e011-m005-routing-metric-and-review-ritual]]
