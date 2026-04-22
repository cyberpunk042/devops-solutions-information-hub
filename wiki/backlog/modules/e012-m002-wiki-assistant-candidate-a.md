---
title: "E012 M002 — Wiki-Assistant (Candidate A, Qwen3.5-4B + LoRA rank 32)"
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
  - id: second-brain-custom-model-strategy
    type: wiki
    file: wiki/spine/references/second-brain-custom-model-strategy.md
tags: [module, p2, e012, wiki-assistant, candidate-a, qwen, lora, fine-tuning, sft, methodology]
---

# E012 M002 — Wiki-Assistant (Candidate A)

## Summary

Train a methodology-fluent small model that knows the wiki's 4 principles, 16 models, 22 standards, and 10 verbs deeply enough to act as a fast local assistant for routine wiki operations (scaffold pages, check compliance, suggest relationships) without requiring a frontier call. Base: Qwen3.5-4B. LoRA rank: 32. Training: 3 epochs on ~200-500 SFT pairs synthesized by Unsloth Data Recipe from the wiki corpus. Output: GGUF ~2.5 GB deployed to Ollama for local inference, integrated as AICP tier `local-wiki-maintenance`.

## Tasks

| Task | Title | Readiness | Progress | Status |
|------|-------|-----------|----------|--------|
| T060 | Audit wiki corpus maturity for training readiness (400+ pages, relationships density) | 100% | 0% | draft |
| T061 | Generate SFT dataset via Unsloth Data Recipe over wiki/ (200-500 pairs) | 70% | 0% | draft |
| T062 | Train Qwen3.5-4B + LoRA rank 32 for 3 epochs | 70% | 0% | draft |
| T063 | Hold-out evaluation: methodology Q&A accuracy | 70% | 0% | draft |
| T064 | Export GGUF + deploy to Ollama | 75% | 0% | draft |
| T065 | Integrate as AICP `local-wiki-maintenance` tier | 80% | 0% | draft |

## Dependencies

- **E012 M001** — Unsloth usable.
- **E010 M001** — RAM for bigger context during training.
- Wiki corpus at ≥400 pages with ≥2500 relationships (currently 446 / 2737 — sufficient).
- Ollama installed (separate prereq; `curl https://ollama.ai/install.sh | sh`).

## Done When

- [ ] Wiki corpus audit: ≥150 standards/models/patterns pages suitable for Q&A SFT pair generation
- [ ] SFT dataset: ~200-500 pairs in JSONL, stored at `/mnt/models/datasets/wiki-assistant-sft-v1.jsonl`
- [ ] Training run completes in ≤6 hours on operator's hardware (19 GB VRAM + 64 GB RAM); training loss curve captured
- [ ] Holdout evaluation: ≥70% accuracy on methodology Q&A (20-item benchmark hand-authored)
- [ ] GGUF export at `/mnt/models/wiki-assistant-v1.gguf` (~2.5 GB)
- [ ] Ollama `ollama run wiki-assistant` works and responds to a sample methodology question
- [ ] AICP `local-wiki-maintenance` backend registered (reuses LocalAIBackend pattern from E011 M003 with config_key="local_wiki_maintenance")
- [ ] Training run documented in `wiki/log/2026-05-*-wiki-assistant-v1-training.md`
- [ ] All child tasks at status: done

## Procedure (reference)

### Step 1 — Corpus audit

```bash
cd /home/jfortin/devops-solutions-research-wiki
python3 -m tools.pipeline status
# Check page counts by type: standard, model, pattern, principle, verb
python3 -c "
from tools.manifest import load_manifest
m = load_manifest()
from collections import Counter
c = Counter(p['type'] for p in m['pages'])
for t, n in c.most_common(): print(f'{t}: {n}')
"
```

### Step 2 — Generate SFT dataset

Unsloth's Data Recipe docs: feed the wiki corpus + a Q&A template to generate SFT pairs.

```bash
source /home/jfortin/unsloth-env/bin/activate
python tools/generate_sft_dataset.py \
  --corpus wiki/ \
  --template tools/sft_templates/wiki_qa.jinja \
  --target-pairs 300 \
  --out /mnt/models/datasets/wiki-assistant-sft-v1.jsonl
# Script tbd — part of T061 implementation
```

### Step 3 — Training

```bash
source /home/jfortin/unsloth-env/bin/activate
python tools/train_wiki_assistant.py \
  --base unsloth/Qwen3.5-4B-bnb-4bit \
  --dataset /mnt/models/datasets/wiki-assistant-sft-v1.jsonl \
  --lora-rank 32 \
  --epochs 3 \
  --output-dir /mnt/models/wiki-assistant-v1-lora
```

### Step 4 — Evaluate + export

```bash
python tools/eval_wiki_assistant.py \
  --lora /mnt/models/wiki-assistant-v1-lora \
  --holdout tools/eval_sets/wiki_methodology_qa.jsonl

# Export GGUF
python tools/export_gguf.py \
  --base Qwen3.5-4B --lora /mnt/models/wiki-assistant-v1-lora \
  --out /mnt/models/wiki-assistant-v1.gguf --quant Q4_K_M
```

### Step 5 — Ollama + AICP

```bash
ollama create wiki-assistant -f /home/jfortin/devops-solutions-research-wiki/ollama/wiki-assistant.Modelfile
ollama run wiki-assistant "What are the 4 principles?"

# AICP integration — add backend stanza (reuse LocalAIBackend pattern)
# See e011-m001-tier-definitions-update Step 2 canonical form
```

## Rollback

```bash
rm -rf /mnt/models/wiki-assistant-v1-lora /mnt/models/wiki-assistant-v1.gguf
rm -f /mnt/models/datasets/wiki-assistant-sft-v1.jsonl
ollama rm wiki-assistant
```

## Impediments

| Impediment | Type | Blocked Since | Escalated? | Resolution |
|-----------|------|---------------|-----------|------------|
| Wiki corpus may not have enough Q&A-shaped content for 300 SFT pairs | data | 2026-04-22 | no | Augment with hand-authored methodology questions; T060 audit confirms |
| Training loss plateau at low quality | model | 2026-04-22 | no | Increase dataset size; raise LoRA rank to 64; train more epochs |
| Qwen3.5-4B license restrictions for redistribution | legal | 2026-04-22 | no | Keep weights local; no redistribution planned |

## Relationships

- PART OF: [[E012-custom-model-library-unsloth-loras|E012-custom-model-library-unsloth-loras]]
- DEPENDS ON: [[e012-m001-unsloth-toolchain-install|e012-m001-unsloth-toolchain-install]]
- RELATES TO: [[e011-m001-tier-definitions-update|e011-m001-tier-definitions-update]]

## Backlinks

[[E012-custom-model-library-unsloth-loras|E012-custom-model-library-unsloth-loras]]
[[e012-m001-unsloth-toolchain-install|e012-m001-unsloth-toolchain-install]]
[[e011-m001-tier-definitions-update|e011-m001-tier-definitions-update]]
