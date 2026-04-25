---
title: "Local Training Playbook 2026 — Wiki Alignment, Tool Calls, Semantic Enhancement"
aliases:
  - "Local Training Playbook 2026"
  - "Training Playbook — LoRA + Embeddings on Operator Hardware"
type: operations-plan
domain: cross-domain
layer: spine
status: synthesized
confidence: high
maturity: growing
priority: P1
created: 2026-04-23
updated: 2026-04-23
sources:
  - id: second-brain-custom-model-strategy
    type: wiki
    file: wiki/spine/references/second-brain-custom-model-strategy.md
    description: "Parent strategy doc — 5 candidate approaches A/B/C/D/E. This playbook operationalizes the subset actually worth doing in 2026 Q2."
  - id: ai-infrastructure-decision-framework-2026
    type: wiki
    file: wiki/spine/references/ai-infrastructure-decision-framework-2026.md
    description: "Framework doc — the specialty-routing + training-vs-rental section sets the economic context this playbook operates in."
  - id: src-unsloth-fast-lora-consumer-hardware
    type: wiki
    file: wiki/sources/tools-integration/src-unsloth-fast-lora-consumer-hardware.md
    description: "Unsloth training mechanism — the toolchain this playbook assumes."
tags: [operations-plan, training, lora, unsloth, wiki-alignment, tool-calls, semantic-enhancement, embeddings, local, qwen3, bge-m3, p1]
---

# Local Training Playbook 2026

## Summary

**Direct answers to operator's three training questions (2026-04-23):**

1. **"Can I still do Unsloth training locally for some uses?"** → **YES.** All three projects you named (Wiki alignment, tool calls, semantic enhancement) fit on your 19 GB VRAM Tier-0 hardware with Unsloth. Total runtime for all three: ~6-10 hours across one weekend. Zero cloud spend required.
2. **"Would renting cloud resources be preferable?"** → **NO for these three projects. YES only for 27B+ bases or experimentation sweeps.** The break-even is model-size-gated, not cost-gated.
3. **"LoRA, Wiki alignment, tool calls, semantic enhancement — how?"** → Three tracks below. Each has a specific base model, data preparation approach, training command, runtime estimate, and evaluation gate.

**Budget for all three tracks combined**: 1 weekend of operator time + ~$0 cloud + electricity. Expected outcome: three deployable artifacts integrating into AICP routing and MCP tooling.

## Prerequisites

> [!info] Hardware and environment
>
> | Requirement | Status on operator Tier-0 | Action if missing |
> |---|---|---|
> | 19+ GB VRAM total | ✅ RTX 2080 Ti (11 GB) + RTX 2080 (8 GB) | — |
> | 64 GB RAM | ✅ Confirmed 2026-04-22 | — |
> | CUDA 12.6 | ✅ Verified | — |
> | Unsloth installed | ⚠️ Install via `pip install unsloth` in AICP venv or standalone | `uv pip install unsloth transformers peft datasets accelerate bitsandbytes` |
> | Sentence-Transformers installed (Track 3) | ⚠️ `pip install sentence-transformers` | — |
> | Ollama for deployment | ⚠️ Install Ollama CLI | `curl -fsSL https://ollama.com/install.sh \| sh` |
> | Wiki corpus exportable to jsonl | ✅ 468 pages, parseable via `tools.manifest` | — |
> | Evaluation holdout set reserved | ❌ Needs building (step 1 of each track) | See per-track Data sections |

## The Decision Grid (before starting)

> [!tip] Local vs cloud rental — the actual rule
>
> | Training job | Decision | Reason |
> |---|---|---|
> | LoRA on ≤8B base | **Local** | Fits comfortably in 11 GB VRAM with Unsloth 4-bit base; 2-4h/run |
> | LoRA on 13B base | **Local, if patient** | Tight fit; gradient checkpointing; 6-12h/run |
> | LoRA on 27B base | **Cloud H100** | $15-40/run, ~1h; local is multi-day |
> | Full fine-tune, any size ≥7B | **Cloud** | Gradient state alone exceeds 19 GB VRAM |
> | Embedding fine-tune (≤500M params) | **Local trivially** | Sentence-transformers with MNR loss; <1h |
> | Experimental sweeps (5+ configs) | **Cloud parallel** | Time-value of wall-clock hours |
> | Off-the-shelf embedding (no training) | **No training needed** | BGE-M3 and nomic-embed-text-v2 already excellent; start here |
>
> **For operator's three projects** (Wiki alignment LoRA on 4B, tool-call LoRA on 4-8B, semantic enhancement embedding-fine-tune): **all three are local**. Cloud rental has zero ROI on these specific tasks.

## Steps

Three parallel training tracks below. Each self-contained — execute in any order; recommended order is Track 3 evaluation first (to decide if Track 3 training is needed) then Tracks 1 and 2 in training order.

### Track 1 — Wiki Alignment LoRA

> [!success] Goal: Qwen3-4B fine-tuned on wiki corpus → methodology-fluent local model
> Operationalizes Candidate A from [[second-brain-custom-model-strategy|Second-Brain Custom Model Strategy]]. First shippable artifact of the training investment.

### Specifics

| Parameter | Value |
|---|---|
| **Base model** | Qwen3-4B (Unsloth 4-bit variant) |
| **LoRA rank** | 32 |
| **LoRA alpha** | 64 |
| **Target modules** | q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj |
| **Training data** | Auto-extracted (Unsloth Data Recipe on `wiki/`) + manual curation |
| **Dataset size** | ~960 auto pairs + ~100-300 manual = ~1,100-1,300 pairs |
| **Epochs** | 3 |
| **Batch size** | 2 (effective 16 via gradient accumulation) |
| **Learning rate** | 2e-4 |
| **Expected runtime** | **2-3 hours** on RTX 2080 Ti (primary) + RTX 2080 (secondary) |
| **Output size** | ~50 MB adapter + merged GGUF ~2.5 GB |
| **Deployment** | Ollama `ollama create wiki-assistant-v1 -f Modelfile` |
| **Inference throughput** | 30-60 tok/s on operator hardware |
| **Cloud rental alternative** | Not recommended — $10-15 H100 rental saves ~1h wall-clock; not worth the setup overhead for a first run |

### Data preparation

1. **Run Unsloth Data Recipe** on `wiki/`:
   ```bash
   python -m unsloth.data_recipe --source wiki/ --output data/wiki-sft.jsonl \
     --page-types concept,lesson,pattern,decision,principle,reference
   ```
   Yields ~960 automated (question → wiki content) pairs.
2. **Manual curation pass** (~2-3 hours operator time): add ~100-300 deep-reasoning pairs — "given X evidence, which lesson does it strengthen?", "given this new page, suggest relationships", "given this page, does it comply with Principle 4?"
3. **Hold out 50 pairs** as evaluation set in `data/wiki-eval.jsonl`. Never train on them.

### Training command

```bash
unsloth train \
  --base Qwen3-4B-Instruct-bnb-4bit \
  --data data/wiki-sft.jsonl \
  --lora-rank 32 --lora-alpha 64 \
  --epochs 3 --batch-size 2 --grad-accum 8 \
  --lr 2e-4 \
  --output-dir models/wiki-assistant-v1
```

### Completion criteria (gates, in order)

1. **Training converges** — loss curve flattens before epoch 3 (not overfitting, not under-trained)
2. **Factual accuracy ≥85%** on 50-pair holdout (automated string similarity)
3. **Reasoning quality ≥3.5/5** on 20-pair operator review
4. **Voice/structure ≥70%** — outputs pass `pipeline post` lint when saved as wiki scaffolds
5. **Integrated into AICP** as `wiki-assistant-v1` backend; routes on methodology-term detection

Pass 1-2 → declare v1 complete. Fail → iterate on data curation, not hyperparameters.

### Track 2 — Tool-Call LoRA

> [!success] Goal: Qwen3-4B or 8B fine-tuned to emit valid JSON tool calls consistently
> **This adapter is NEW in this playbook** — existed implicitly in Candidate E's adapter library but not developed. It addresses a real pain point: small local models tend to garble tool-call JSON under context pressure; a targeted LoRA fixes this dramatically.

### Specifics

| Parameter | Value |
|---|---|
| **Base model** | Qwen3-4B (reuse Track 1 base for adapter-swap compatibility) OR Qwen3-8B if capability ceiling matters |
| **LoRA rank** | 16 (smaller — tool-call patterns are narrow) |
| **LoRA alpha** | 32 |
| **Target modules** | q_proj, k_proj, v_proj, o_proj (attention-only sufficient for format learning) |
| **Training data** | Tool-use dataset — MCP tool schemas (26 wiki MCP tools) + positive/negative examples |
| **Dataset size** | ~500-1,000 tool-call pairs |
| **Epochs** | 3 |
| **Expected runtime** | **1-2 hours** on RTX 2080 Ti |
| **Output size** | ~20 MB adapter |
| **Deployment** | Adapter-swap at inference time — load base once, swap adapters per request |
| **Cloud rental alternative** | Not recommended — smaller LoRA, faster training, trivially local |

### Data preparation

1. **Extract MCP tool schemas** from the wiki's own MCP server:
   ```bash
   python -m tools.mcp_server --list-tools --json > data/mcp-schemas.json
   ```
   (26 tools at current count.)
2. **Generate positive examples** (correct tool calls) — 15-30 per tool covering happy-path invocations:
   ```
   User: "Search the wiki for 'harness-owned loop'"
   Assistant: {"tool": "wiki_search", "arguments": {"query": "harness-owned loop"}}
   ```
3. **Generate negative examples** (malformed calls model should NOT produce) and pair with correct forms — teaches the model to avoid common errors (missing required args, wrong types, hallucinated tool names).
4. **Include tool-not-applicable cases** — "tell the user what tool to run manually" responses when no tool fits. Prevents over-eager tool invocation.
5. **Hold out 50 tool-call scenarios** for evaluation.

### Training command

```bash
unsloth train \
  --base Qwen3-4B-Instruct-bnb-4bit \
  --data data/tool-calls-sft.jsonl \
  --lora-rank 16 --lora-alpha 32 \
  --target-modules "q_proj,k_proj,v_proj,o_proj" \
  --epochs 3 --batch-size 4 --grad-accum 4 \
  --lr 1e-4 \
  --output-dir models/tool-calls-v1
```

### Completion criteria

1. **JSON validity rate ≥98%** on 50-scenario holdout (parses cleanly as JSON)
2. **Correct tool selection ≥90%** (right tool for the scenario)
3. **Argument completeness 100%** for required args; 0 hallucinated args
4. **Refusal on tool-not-applicable cases ≥85%** (doesn't over-invoke)
5. **Integrated into AICP** — when routing to a local model for tool-heavy workflows, auto-load the tool-calls adapter on top of the base

### Track 3 — Semantic Enhancement (Embeddings)

> [!warning] Different beast: embeddings ≠ LLM LoRA
> The first two tracks fine-tune LLMs. Semantic enhancement is about **embedding quality** — how well vectors cluster semantically-related wiki content. Different base models, different training approach (contrastive loss), different deployment (usually vector-DB side, not LLM side).

### Decision: off-the-shelf vs fine-tune

> [!info] Start with off-the-shelf. Fine-tune only if measurement justifies.
>
> | Option | What it is | Cost | When to choose |
> |---|---|---|---|
> | **A — BGE-M3 off-the-shelf** | 568M-param multilingual embedding from BAAI; SOTA on many retrieval benchmarks | $0, 5-min deploy | **Default starting point** for a 468-page wiki. Almost certainly sufficient |
> | **B — nomic-embed-text-v2** | 305M-param; strong English; smaller/faster | $0, 5-min deploy | If BGE-M3 throughput is an issue at query time |
> | **C — Fine-tune BGE-M3 on wiki triplets** | Domain-aligned embeddings | ~1h local + ~1000 manual triplets | Only if A's retrieval @5 on held-out queries is <75% |
> | **D — Custom small reranker** | Cross-encoder on top of retrieval | ~2h local | Only if retrieval is strong but top-k ordering is wrong |

### For your 468-page wiki: use Option A first

Rationale: embedding fine-tunes pay off when the domain vocabulary is so specialized that general-purpose embeddings fail. Your wiki's vocabulary — "Principle 4," "Goldilocks protocol," "consumer-property doctrine" — is specialized but **sparse relative to corpus size**. BGE-M3 off-the-shelf will handle it. Verify before investing in fine-tuning.

### Evaluation gate (measure before training)

Build a 30-query evaluation set from your actual wiki-query patterns:
```
# data/wiki-retrieval-eval.jsonl — one line per query
{"query": "what does Principle 4 say?", "relevant": ["declarations-are-aspirational-until-infrastructure-verifies-them"]}
{"query": "how to promote a seed to growing?", "relevant": ["second-brain-custom-model-strategy", "evolution-standards"]}
{"query": "fleet contribution gating", "relevant": ["contribution-gating-cross-agent-inputs-before-work"]}
# ...
```

Run BGE-M3 retrieval @5 on this set. If recall@5 ≥ 85% across all queries, stop here — you're done. Ship BGE-M3 as your wiki embedding layer, integrate with LightRAG.

### If fine-tuning needed (Option C)

Only if the evaluation above flunks:

| Parameter | Value |
|---|---|
| **Base model** | BAAI/bge-m3 |
| **Training objective** | Multiple Negatives Ranking (MNR) contrastive loss |
| **Training data** | ~1,000 triplets: `(query, relevant_page, irrelevant_page)` |
| **Epochs** | 2 |
| **Batch size** | 16 |
| **Expected runtime** | **~1 hour** on RTX 2080 Ti |
| **Output size** | Same as base (568M params) |
| **Deployment** | Replace base in LightRAG config |

Training command (sentence-transformers, not Unsloth — different toolchain for embeddings):
```bash
python -m sentence_transformers.train \
  --base BAAI/bge-m3 \
  --data data/wiki-triplets.jsonl \
  --loss MultipleNegativesRankingLoss \
  --epochs 2 --batch-size 16 \
  --output-dir models/wiki-embedder-v1
```

### Completion criteria

1. **Off-the-shelf BGE-M3 recall@5 ≥ 85%** on wiki-retrieval-eval → DONE, no training needed
2. If below: **fine-tuned BGE-M3 recall@5 ≥ 90%** on same eval set
3. **Deployed as LightRAG embedding backend** — replaces prior choice
4. **Query latency < 100ms** for single-query retrieval on operator hardware

## Track execution order and total budget

> [!tip] Recommended sequencing — one weekend
>
> | Slot | Track | Duration | Gate |
> |---|---|---|---|
> | **Saturday AM** | Prerequisites (Unsloth install, data prep) | 2-3h | Unsloth runs end-to-end on a toy example |
> | **Saturday PM** | Track 3 evaluation (BGE-M3 off-the-shelf) | 1h | Decision: skip Track 3 training or proceed |
> | **Saturday night** | Track 1 training (Wiki alignment) | 2-3h (can run overnight) | Training completes without OOM |
> | **Sunday AM** | Track 1 evaluation + integration | 2h | Gates 1-2 of Track 1 pass |
> | **Sunday PM** | Track 2 training (Tool calls) | 1-2h | Training completes |
> | **Sunday evening** | Track 2 evaluation + integration | 1h | Gate 1-2 of Track 2 pass |
>
> **Total operator time**: ~10-12 hours across a weekend. **Total cost**: $0 cloud + electricity. **Delivered artifacts**: 3 production-deployable capabilities.

## Completion Criteria

Each track has its own gates (listed in the track sections above). The playbook as a whole is considered delivered when:

1. **Track 1 complete**: Wiki-assistant v1 passes its gates 1-2 (convergence + factual accuracy ≥85%) and is registered as an AICP backend.
2. **Track 2 complete**: Tool-call adapter passes JSON validity ≥98% and correct-tool-selection ≥90%; wired into AICP's tool-heavy routing.
3. **Track 3 complete**: BGE-M3 retrieval @5 ≥85% on the wiki-retrieval-eval set (whether off-the-shelf or fine-tuned). LightRAG configured to use it.
4. **Documentation updated**: `## Relationships` of [[second-brain-custom-model-strategy|Second-Brain Custom Model Strategy]] marks Candidates A, D-subset, E-tool-adapter as "shipped v1"; training data + eval sets committed under `data/`.
5. **No cloud spend incurred** for any of the three tracks (the whole point — this validates the "local viable" claim).

Partial delivery is acceptable — shipping any single track unlocks value independent of the others. Track 3's off-the-shelf option can complete in one afternoon; Tracks 1 and 2 take a weekend.

## Rollback

Each track is independently reversible:

| Track | Rollback procedure |
|---|---|
| Track 1 (Wiki alignment) | Unregister `wiki-assistant-v1` from AICP `tier_map`; retain adapter on disk for later iteration |
| Track 2 (Tool calls) | Remove adapter from AICP's tool-heavy routing; base model unchanged |
| Track 3 (Embeddings) | Revert LightRAG config to prior embedding; no data loss |

Training data is retained regardless — it's valuable for future retraining or evaluation.

## When to escalate to cloud rental

> [!info] The specific triggers that invalidate "local only"
>
> - **Base model requirement climbs to 27B+** (e.g., if Candidate B or C from the parent strategy gets activated) → H100 on RunPod at ~$2/hr is cheaper than days-long local runs
> - **You want to compare 5+ hyperparameter configs in a single session** — parallelize across rented A100s; Colab Pro+ is sufficient
> - **Full fine-tuning (not LoRA)** on any base ≥7B — local VRAM headroom insufficient for gradient state
> - **Training data grows 10× beyond current plan** (e.g., 10K+ pairs on 8B base with 5 epochs) — wall-clock time becomes operator-time-expensive
> - **Embedding model training on >1M page corpus** — unlikely for this wiki, but possible for sister projects

For any of these, the [[ai-infrastructure-decision-framework-2026|framework doc]]'s cloud-rental economics table applies: Lambda Labs / RunPod H100 at $1.90-3.50/hr; typical LoRA job $15-40; typical embedding fine-tune $5-20.

## How This Connects — Navigate From Here

> [!abstract] From this playbook → related knowledge
>
> | Direction | Go To |
> |---|---|
> | Full strategy with 5 candidates | [[second-brain-custom-model-strategy\|Second-Brain Custom Model Strategy]] |
> | Economic context (local training vs rental) | [[ai-infrastructure-decision-framework-2026\|AI Infrastructure Decision Framework 2026]] § Training |
> | Unsloth toolchain details | [[src-unsloth-fast-lora-consumer-hardware\|Unsloth Synthesis]] |
> | Evaluation framework for custom models | [[open-model-evaluation-framework\|Open-Model Evaluation Framework]] |
> | Principle governing "don't declare success before eval" | [[declarations-are-aspirational-until-infrastructure-verifies-them\|Principle 4]] |

## Relationships

- IMPLEMENTS: [[second-brain-custom-model-strategy|Second-Brain Custom Model Strategy]]
- BUILDS ON: [[ai-infrastructure-decision-framework-2026|AI Infrastructure Decision Framework 2026]]
- BUILDS ON: [[src-unsloth-fast-lora-consumer-hardware|Synthesis — Unsloth]]
- FEEDS INTO: [[aicp|AICP]]
- FEEDS INTO: [[model-local-ai|Model — Local AI]]
- RELATES TO: [[open-model-evaluation-framework|Open-Model Evaluation Framework]]
- DEMONSTRATES: [[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4 — Declarations Aspirational Until Verified]] — every track has explicit completion-criteria gates; no declaration of success without measurement

## Backlinks

[[second-brain-custom-model-strategy|Second-Brain Custom Model Strategy]]
[[ai-infrastructure-decision-framework-2026|AI Infrastructure Decision Framework 2026]]
[[Synthesis — Unsloth]]
[[aicp|AICP]]
[[Model — Local AI]]
[[open-model-evaluation-framework|Open-Model Evaluation Framework]]
[[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4 — Declarations Aspirational Until Verified]]
