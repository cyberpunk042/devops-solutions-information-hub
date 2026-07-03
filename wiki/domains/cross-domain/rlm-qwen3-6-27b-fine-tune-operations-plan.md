---
title: "Operations Plan — RLM-Qwen3.6-27B Fine-Tune (Hypothetical Composition Path for Tier-0 Long-Context)"
aliases:
  - "RLM-Qwen3.6-27B Operations Plan"
  - "Operations Plan — RLM-Qwen3.6-27B"
  - "Hypothetical RLM-Qwen3.6-27B Fine-Tune Plan"
  - "Composition Path Operations Plan"
type: operations-plan
domain: cross-domain
status: synthesized
confidence: medium
maturity: seed
priority: P1
created: 2026-04-27
updated: 2026-04-28
last_reviewed: 2026-04-28
sources:
  - id: rlm-paper-deep-dive
    type: wiki
    file: wiki/sources/tools-integration/src-rlm-paper-deep-dive-table-1-training-recipe-six-observations.md
    description: "The 8B training recipe this plan scales: 750 LongBenchPro tasks → 2,250 candidate trajectories → 1,072 filtered → per-turn SFT samples → programmatic FINAL/FINAL_VAR fix → prime-rl batch 64, 300 steps, 48 H100 hours."
  - id: prime-rl-synthesis
    type: wiki
    file: wiki/sources/tools-integration/src-prime-intellect-prime-rl-async-rl-training-at-scale.md
    description: "Training framework — Apache 2.0, FSDP2 + vLLM, FP8 + EP/CP, IPO + Kimi-K2.5 KL default loss, async k=2."
  - id: verifiers-synthesis
    type: wiki
    file: wiki/sources/tools-integration/src-prime-intellect-verifiers-llm-rl-environments.md
    description: "Environment library — v0.1.12 (2026-04-17) added RLMEnv (context dropping, prompt builder, hardened transport) + RLM tasksets."
  - id: rlm-implementation-synthesis
    type: wiki
    file: wiki/sources/tools-integration/src-rlm-recursive-language-models-mit-oasys.md
    description: "Deployment runtime — alexzhang13/rlm SDK, 5 backends (incl. vllm for local), 6 environments, REPL semantics."
  - id: tier-0-comparison
    type: wiki
    file: wiki/comparisons/rlm-qwen3-8b-vs-qwen3-6-27b-tier-0-long-context-candidate.md
    description: "The decision matrix this plan implements — specifically the third path (Composition: future RLM-Qwen3.6-27B fine-tune at ~$300-500 USD)."
  - id: qwen3-6-27b-marktechpost
    type: wiki
    file: wiki/sources/tools-integration/src-qwen3-6-27b-dense-beats-397b-moe-agentic-coding.md
    description: "Base model — Qwen3.6-27B-Dense (Apache 2.0); SWE-bench Pro 53.5; hybrid Gated-DeltaNet (75%) + Attention (25%); native multimodal."
  - id: qwen3-6-27b-unsloth
    type: wiki
    file: wiki/sources/tools-integration/src-qwen3-6-27b-2-bit-26-tool-calls-unsloth-discussion.md
    description: "Quantization detail — UD-IQ2 fits 5-7GB VRAM with retained 26-tool-call agentic capability; deployment target for the trained model on operator's tier-0 hardware."
  - id: oolong-longbench-pro-synthesis
    type: wiki
    file: wiki/sources/tools-integration/src-oolong-and-longbench-pro-long-context-benchmarks-rlm-anchors.md
    description: "LongBench Pro = training data source (English split, 750 tasks). OOLONG + OOLONG-Pairs = evaluation surface."
  - id: browsecomp-longbench-v2-synthesis
    type: wiki
    file: wiki/sources/tools-integration/src-browsecomp-plus-and-longbench-v2-rlm-table-1-benchmarks.md
    description: "Remaining 2 evaluation benchmarks — BrowseComp+ (1K-doc multi-hop research) + LongBench v2 CodeQA split (multi-file code repository understanding)."
  - id: anti-vendor-lock-in-lesson
    type: wiki
    file: wiki/lessons/01_drafts/anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence.md
    description: "Mission framing — this plan is a worked example of step 6 ('close gaps systematically') of the lesson's How-to-Apply."
  - id: aicp-handoff
    type: external
    file: ~/devops-expert-local-ai/docs/SESSION-2026-04-24-HANDOFF.md
    description: "Authoritative compute-side state — operator's tier-0 hardware (X299 + RTX 2080 Ti 11GB + RTX 2080 8GB + 64GB DDR4); AICP backend pattern (`local`/`k2_6_local`/`k2_6_openrouter`/`ollama_cloud`); $540→$100 routing finding the trained model would slot into."
tags: [operations-plan, rlm, recursive-language-models, qwen3-6-27b, fine-tune, composition-path, post-anthropic-mission, anti-vendor-lock-in, sovereignty-tier, hypothetical, post-t-0, prime-rl, verifiers, longbenchpro, oolong, browsecomp-plus, longbench-v2, deterministic-steps, tier-0-candidate, hardware-tier-0, mission-2026-04-27, p1]
---

# Operations Plan — RLM-Qwen3.6-27B Fine-Tune (Hypothetical Composition Path)

## Summary

Reproducible, deterministic operations plan for fine-tuning **Qwen3.6-27B-Dense** (Alibaba, Apache 2.0, 2026-04-22 release) into a **natively-recursive language model** by applying the [RLM paper's training recipe](../../sources/tools-integration/src-rlm-paper-deep-dive-table-1-training-recipe-six-observations.md) — scaled from the published 8B recipe (Qwen3-8B base, 48 H100 hours, ~$48-100 USD) to 27B (~150-200 H100 hours, **~$300-500 USD cloud GPU rental** at typical 2026 rates). End state: a checkpoint **RLM-Qwen3.6-27B** that combines (a) Qwen3.6-27B-Dense's agentic-coding gains (SWE-bench Pro 53.5, beats some 397B MoE), (b) the RLM paradigm's effective-context extension (32K native → ~3.2M+ effective via REPL-recursion), (c) Apache 2.0 throughout the stack, deployable as the operator's local tier-0 long-context primary via AICP. **This plan is hypothetical — it has not been executed.** It is authored as the actionable artifact named in the [tier-0 candidate comparison](../../comparisons/rlm-qwen3-8b-vs-qwen3-6-27b-tier-0-long-context-candidate.md) "Composition Path" and the [2026-04-27 session-end handoff](../../log/2026-04-27-session-end-handoff-13-artifacts-rlm-thread-saturation.md) P1 wiki-side list. Execution requires operator approval (compute budget commitment + cloud-GPU access) and AICP-side coordination for deployment wiring.

## Phase-1 vs Phase-2 framing (REVISED 2026-04-28)

> [!warning] **This plan is now Phase-2-conditional, not Phase-1-default**
>
> Two state changes since the original 2026-04-27 authoring:
>
> 1. **MIT released the RLM-Qwen3-8B checkpoint** at [`mit-oasys/rlm-qwen3-8b-v0.1`](https://huggingface.co/mit-oasys/rlm-qwen3-8b-v0.1) — the operations plan's previous "checkpoint release status unverified" caveat is now resolved. Pull-and-run available at $0.
> 2. **Operator ordered RTX 4090 (renewed)** on 2026-04-27, ETA 2-3 weeks. 24GB VRAM Ada — comfortably runs Qwen3.6-27B at UD-IQ2 quantization (~14-16GB) AND fits RLM-Qwen3-8B at full precision.
>
> **Together, these unblock a $0-cash routing path**: deploy `mit-oasys/rlm-qwen3-8b-v0.1` for long-context tasks + vanilla Qwen3.6-27B for short-context tasks, routed by context length via AICP. No cloud GPU rental required for Phase-1 capability.
>
> **This operations plan (the $300-500 cloud fine-tune producing RLM-Qwen3.6-27B) is now the Phase-2 path** — executed only IF the Phase-1 routing approach demonstrates a real workload ceiling that consolidation into one combined model would break. Empirical evidence required from the routed deployment before committing the spend.
>
> | Phase | What you do | Cash | Wall time | Capability |
> |---|---|---|---|---|
> | **Phase 1** (default) | Pull MIT 8B checkpoint + run vanilla 27B + AICP context-length routing | **$0** | hours (after 4090 delivery) | Long-context via RLM-8B + short-context via 27B |
> | **Phase 2** (conditional) | This operations plan — fine-tune 27B with RLM recipe via cloud GPUs | **~$300-500 one-time** | ~24h cloud + this plan's wall time | One combined RLM-Qwen3.6-27B (long + short consolidated) |
>
> **Phase 2 is justified IFF Phase 1 hits a concrete ceiling on operator's actual workload that the combined model would break through.** That's an empirical decision after running Phase 1, not an aspirational decision before.

## Prerequisites

> [!info] Compute and access
>
> | Requirement | Verification | Action if missing |
> |---|---|---|
> | Cloud GPU access (≥8× H100 single-node, or multi-node SLURM equivalent) | Prime Intellect / Lambda / RunPod / Together / direct cloud account | Operator-decision: select provider; Prime Intellect's hosted training natively integrates with prime-rl |
> | Compute budget approved | Operator-decision: ~$300-500 USD typical 2026 rates ($2-3/H100-hr × ~150-200 hrs) | Authorize before fetching weights |
> | `prime` CLI installed + authenticated | `prime --version` and `prime status` | `uv tool install prime && prime login` |
> | `prime-rl` cloned + setup script run | `uv run rl --help` returns RL trainer help | `curl -sSL https://raw.githubusercontent.com/PrimeIntellect-ai/prime-rl/main/scripts/install.sh \| bash` |
> | `verifiers` v0.1.12+ installed | `uv pip show verifiers` shows version ≥0.1.12 | `uv add verifiers` (the v0.1.12 release upstreamed RLM tasksets) |
> | Hugging Face account + access to `Qwen/Qwen3.6-27B` weights | `huggingface-cli whoami` + `huggingface-cli download Qwen/Qwen3.6-27B --dry-run` | Apache 2.0 license — public; only HF account needed |
> | LongBench Pro dataset accessible | English split 750 tasks reachable | Public via HF dataset card or arXiv supplementary; verify path |
> | Teacher RLM access (Qwen3-Coder-480B-A35B as RLM, OR alternative ≥30B coding-capable model) | API endpoint reachable; `pip install rlms` and test `rlm.completion` | Decision: use `vllm` backend for self-hosted teacher (cheapest) OR OpenRouter for managed access (simpler but per-token cost on top of training) |
> | RLMEnv harness for 4 evaluation benchmarks | `prime env install` of OOLONG, BrowseComp+, LongBench-v2-CodeQA, OOLONG-Pairs equivalents | Some may need authoring as new RLMEnv environments; some may exist on Environments Hub |

> [!warning] Hard prerequisites — non-negotiable
>
> 1. **Operator authorization in writing for compute budget** (any cloud GPU spend ≥$100 requires explicit per-action approval per AICP memory `feedback_never_unauthorized_large_disk_writes.md` and operator's 2026-04-24 disk-budget incident framing).
> 2. **No editing the wiki's authoritative spine references during execution** — RLM-Qwen3.6-27B's empirical results, when produced, flow back via [`gateway contribute`](../../../tools/gateway.py), not direct spine edits. The 2026-04-25 `~/aicp/` fabrication incident's [Hard Rule #9](../../../.claude/rules/learnings.md) carries forward.
> 3. **Bilingual signal acknowledged but optional** — Qwen3.6-27B is bilingual (English + Chinese); LongBench Pro is bilingual; this plan trains on the **English split** (750 tasks) per the original RLM paper. A separate plan can scope Chinese-split training if ever needed.

## Steps

### Step 1: Acquire base model and training data

- **Action:** Download Qwen3.6-27B base weights and LongBench Pro English-split tasks
  ```bash
  # Base model (≈54 GB BF16 weights; ≈14-16 GB UD-IQ2 quantized for tier-0 deploy later)
  huggingface-cli download Qwen/Qwen3.6-27B --local-dir ./models/qwen3-6-27b-base

  # Training data — LongBench Pro English split (750 tasks)
  # If on HF Datasets:
  huggingface-cli download <longbench-pro-org>/longbench-pro --repo-type dataset \
      --include "english/*" --local-dir ./data/longbench-pro-en
  ```
- **Expected output:** `./models/qwen3-6-27b-base/` contains `config.json`, `tokenizer*`, weight shards. `./data/longbench-pro-en/` contains 750 task definitions with input contexts + reference answers.
- **Validation:**
  ```bash
  ls -la ./models/qwen3-6-27b-base/ | wc -l       # ≥10 files
  jq '.architectures' ./models/qwen3-6-27b-base/config.json  # ["Qwen3MoEForCausalLM"] or dense equivalent
  find ./data/longbench-pro-en -type f -name "*.json*" | wc -l   # ≈750 task files (may be jsonl-batched)
  ```
- **Rollback:** `rm -rf ./models/qwen3-6-27b-base ./data/longbench-pro-en` — disk recovered, no other state changed

### Step 2: Stand up the training infrastructure

- **Action:** Configure prime-rl + verifiers for SFT on RLM trajectories. Create `configs/sft-rlm-qwen3-6-27b.toml` modeled on prime-rl's basic SFT examples (Reverse Text / Wordle / Hendrycks Sanity).
  ```toml
  [model]
  name = "Qwen/Qwen3.6-27B"
  impl = "auto"   # selects custom Qwen3.5-MoE stack if applicable

  [model.parallelism]
  fsdp = 8        # 8-way FSDP2 across 8× H100
  ep = 1          # no expert parallelism for dense
  cp = 1          # context parallelism if sequences exceed 128K tokens

  [data]
  type = "trajectory_sft"
  source = "./data/rlm-trajectories-filtered.jsonl"   # produced in Step 4

  [training]
  batch_size = 64
  steps = 600     # scaled from 8B's 300 steps; subject to monitoring + early-stop
  lr = 1e-5       # conservative for 27B; reduce if loss spikes
  max_seq_len = 32768  # Qwen3-8B used 32K context limit per RLM paper appendix; reduce if OOM

  [loss]
  type = "default"  # IPO (DPPO-Binary TV) + Kimi-K2.5 KL — prime-rl default since 2026-03-02

  [logging]
  wandb_project = "rlm-qwen3-6-27b-finetune"
  metrics_server = true
  ```
- **Expected output:** `uv run sft @ configs/sft-rlm-qwen3-6-27b.toml --validate-only` returns 0 errors and prints config hash.
- **Validation:**
  ```bash
  uv run sft @ configs/sft-rlm-qwen3-6-27b.toml --validate-only
  echo "Exit code: $?"     # must be 0
  ```
- **Rollback:** Delete `configs/sft-rlm-qwen3-6-27b.toml`; no infrastructure changed yet

### Step 3: Generate distillation trajectories with teacher RLM

- **Action:** Run `Qwen3-Coder-480B-A35B-Instruct` (or alternative ≥30B coding-capable teacher) AS an RLM on the 750 LongBenchPro English tasks, sampling 3 trajectories per task (matches paper's 2,250 total).
  ```python
  # scripts/generate-trajectories.py
  from rlm import RLM, RLMLogger
  import json

  teacher = RLM(
      backend="vllm",  # self-hosted; or "openrouter" for managed access
      backend_kwargs={"model_name": "Qwen/Qwen3-Coder-480B-A35B-Instruct",
                      "base_url": "http://teacher-vllm:8000/v1"},
      max_iterations=30,
      logger=RLMLogger(log_dir="./trajectories/raw/"),
  )

  with open("./data/longbench-pro-en/tasks.jsonl") as f:
      for line in f:
          task = json.loads(line)
          for sample in range(3):  # 3 candidate trajectories per task
              teacher.completion(task["input"], root_prompt=task["prompt"])
  ```
- **Expected output:** `./trajectories/raw/` contains ~2,250 JSONL trajectory files (`rlm_<TIMESTAMP>_<UUID>.jsonl`).
- **Validation:**
  ```bash
  ls ./trajectories/raw/*.jsonl | wc -l     # ≈2250 (allow ±5% for any errors)
  # Spot-check trajectory completeness
  jq '.[] | select(.type=="iteration") | .iteration' ./trajectories/raw/$(ls ./trajectories/raw/ | head -1) | tail -1
  # Last iteration index per file should usually be ≥2 (single-turn = trivial; will be filtered)
  ```
- **Rollback:** `rm -rf ./trajectories/raw/` — disk recovered. Note: regenerating costs significant compute; preserve trajectories across Step-3-→-Step-4 rollbacks.

### Step 4: Filter + decompose trajectories into per-turn SFT samples

- **Action:** Apply the paper's filtering (drop zero-score + single-turn trajectories) and decomposition (each ROOT RLM TURN becomes one SFT sample with full history input + root LM output).
  ```python
  # scripts/filter-and-decompose.py
  import json, glob

  raw = []
  for path in glob.glob("./trajectories/raw/*.jsonl"):
      with open(path) as f:
          traj = [json.loads(line) for line in f]
      score = next((e["score"] for e in traj if e.get("type") == "score"), 0.0)
      iterations = [e for e in traj if e["type"] == "iteration"]
      if score == 0.0 or len(iterations) <= 1:
          continue   # drop zero-score and single-turn
      raw.append((path, traj, iterations))

  # Decompose to per-turn SFT samples
  out = open("./data/rlm-trajectories-filtered.jsonl", "w")
  for path, traj, iterations in raw:
      for i, turn in enumerate(iterations):
          history = iterations[:i]
          if estimate_chars(history) > 100_000:  # Qwen3-8B paper used ~100K char filter; adjust for 27B context
              continue
          # Programmatic FINAL/FINAL_VAR fix per paper
          fixed = fix_final_template(turn["response"])
          out.write(json.dumps({"input": history, "output": fixed}) + "\n")
  out.close()
  ```
- **Expected output:** `./data/rlm-trajectories-filtered.jsonl` containing ~per-turn SFT samples (paper's 8B recipe yielded "1,072 trajectories" after filter then per-turn decomposition; 27B should produce comparable counts).
- **Validation:**
  ```bash
  wc -l ./data/rlm-trajectories-filtered.jsonl       # report line count for run record
  # Sanity-check sample structure
  head -1 ./data/rlm-trajectories-filtered.jsonl | jq 'keys'   # ["input", "output"]
  # Verify no zero-score trajectories made it through
  python3 -c "import json; [print('ZERO SCORE LEAKED') for l in open('./data/rlm-trajectories-filtered.jsonl') if json.loads(l).get('score') == 0]"
  ```
- **Rollback:** `rm ./data/rlm-trajectories-filtered.jsonl` — preserves Step 3 raw trajectories for re-filtering with different criteria

### Step 5: Fine-tune Qwen3.6-27B with prime-rl SFT

- **Action:** Launch the SFT training run.
  ```bash
  uv run sft @ configs/sft-rlm-qwen3-6-27b.toml \
      --output_dir ./checkpoints/rlm-qwen3-6-27b/ \
      --resume_from_checkpoint  # idempotent re-runs
  ```
- **Expected output:** Training completes 600 steps. W&B dashboard shows loss curve descending then plateauing. Checkpoint directory contains `adapter_model.safetensors` (if LoRA) or full weights, `config.json`, `tokenizer*`. Estimated runtime: **~150-200 H100 hours** (8× H100 single-node ≈ 19-25 wall-clock hours; multi-node faster). Estimated cost: **~$300-500 USD** at $2-3/H100-hour.
- **Validation:**
  ```bash
  # Final loss should be lower than initial; eval loss should be near training loss
  cat ./checkpoints/rlm-qwen3-6-27b/training_stats.json | jq '{final_loss, eval_loss}'

  # Checkpoint loads in vLLM
  vllm serve ./checkpoints/rlm-qwen3-6-27b/ --port 8001 --max-model-len 32768
  curl http://localhost:8001/v1/models   # should list rlm-qwen3-6-27b

  # Smoke-test as RLM root
  python3 -c "
  from rlm import RLM
  rlm = RLM(backend='vllm', backend_kwargs={'model_name': 'rlm-qwen3-6-27b', 'base_url': 'http://localhost:8001/v1'})
  result = rlm.completion('test_context', root_prompt='What is the length of context?')
  print(result.metadata)
  "
  ```
- **Rollback:** Training failures: `rm -rf ./checkpoints/rlm-qwen3-6-27b/` and re-launch with reduced batch size, lower LR, or fewer FSDP shards. Loss-divergence: check IPO `ipo_mask_low`/`ipo_mask_high` defaults (0.2 each); reduce LR by 10× before retrying. **Hard limit: if 3 consecutive runs diverge, stop and operator-review** (this is the indicator that the recipe doesn't directly transfer to 27B and needs research, not more training).

### Step 6: Evaluate on the 4 RLM Table 1 benchmarks

- **Action:** Run RLM-Qwen3.6-27B against the same 4 benchmarks the [RLM paper](../../sources/tools-integration/src-rlm-paper-deep-dive-table-1-training-recipe-six-observations.md) Table 1 uses, plus side-by-side baselines (vanilla Qwen3.6-27B, RLM-Qwen3-8B published, GPT-5 reference if accessible).
  ```bash
  # Each benchmark via prime CLI evaluation (verifiers env)
  prime eval run oolong-trec-coarse -m ./checkpoints/rlm-qwen3-6-27b/ --rlm-mode
  prime eval run oolong-pairs       -m ./checkpoints/rlm-qwen3-6-27b/ --rlm-mode
  prime eval run codeqa-longbench-v2 -m ./checkpoints/rlm-qwen3-6-27b/ --rlm-mode
  prime eval run browsecomp-plus-1k -m ./checkpoints/rlm-qwen3-6-27b/ --rlm-mode

  # Same with vanilla Qwen3.6-27B (no RLM, baseline) for comparison
  prime eval run oolong-trec-coarse -m Qwen/Qwen3.6-27B
  # ... etc
  ```
- **Expected output:** Per-benchmark score + cost (median + 95th percentile per RLM paper Figure 3 framing). Hypothesis to test: **RLM-Qwen3.6-27B should approach or exceed published RLM(GPT-5) numbers** on at least 2 of 4 tasks, given it composes RLM-paradigm gains with Qwen3.6-27B's stronger base reasoning vs Qwen3-8B.

  Reference targets from [RLM paper Table 1](../../sources/tools-integration/src-rlm-paper-deep-dive-table-1-training-recipe-six-observations.md):

  | Benchmark | RLM(GPT-5) | RLM(Qwen3-Coder-480B) | RLM-Qwen3-8B (8B fine-tuned) | **RLM-Qwen3.6-27B target** |
  |---|---|---|---|---|
  | CodeQA | 62.0% | 56.0% | 32.0% | ≥50% (between 8B and 480B) |
  | BrowseComp+ (1K) | 91.3% | 44.7% | 14.0% | ≥40% (closer to 480B) |
  | OOLONG | 56.5% | 48.0% | 32.0% | ≥45% |
  | OOLONG-Pairs | 58.0% | 23.1% | 5.2% | ≥20% |

- **Validation:**
  ```bash
  # All 4 evals report cleanly; aggregate via prime eval tui
  prime eval tui    # Browse evaluation results in terminal UI
  # Document the actual numbers in a results page (deferred to Step 7)
  ```
- **Rollback:** Eval failures don't affect the trained model. Re-running an eval is idempotent; per-eval failures isolate to that benchmark.

### Step 7: Document results + contribute back to the wiki

- **Action:** Author a results-comparison page that records actual numbers vs targets and updates the [tier-0 candidate comparison](../../comparisons/rlm-qwen3-8b-vs-qwen3-6-27b-tier-0-long-context-candidate.md) with a 4th column. Use `gateway contribute` (NOT direct edit) so the wiki's contribution audit trail is honored.
  ```bash
  python3 -m tools.gateway contribute \
      --type comparison \
      --title "RLM-Qwen3.6-27B Empirical Results vs RLM Table 1 Baselines" \
      --content "$(cat ./eval-results-summary.md)" \
      --contributor "operator-direct-or-aicp" \
      --source "/home/jfortin/devops-expert-local-ai" \
      --reason "Empirical validation of the RLM-Qwen3.6-27B composition path; updates the tier-0 comparison's hypothetical column with measured numbers."

  # Then run pipeline post (mandatory)
  .venv/bin/python -m tools.pipeline post     # 0 errors required
  ```
- **Expected output:** New page at `wiki/lessons/00_inbox/` with `contribution_status: pending-review`. Operator promotes via maturity lifecycle.
- **Validation:**
  ```bash
  ls wiki/lessons/00_inbox/ | grep -i rlm-qwen3-6-27b   # contributed page lands
  .venv/bin/python -m tools.pipeline status    # page count +1; 0 errors
  ```
- **Rollback:** `git checkout wiki/lessons/00_inbox/<contributed-page>.md && git checkout wiki/manifest.json` — un-lands the contribution

### Step 8: Deploy to AICP (optional — only if Step 6 hits target thresholds)

- **Action:** Quantize to UD-IQ2 (Unsloth 2-bit dynamic) for tier-0 hardware fit, then add an AICP backend.
  ```bash
  # Quantization (delegated to Unsloth's conversion path)
  # Result: ~14-16GB quantized weights from ~54GB BF16

  # AICP backend wiring follows the existing k2_6_local pattern at ~/devops-expert-local-ai/aicp/backends/k2_6_local.py
  # Add: aicp/backends/rlm_qwen3_6_27b_local.py
  # Update: config/default.yaml backends.rlm_qwen3_6_27b_local section
  # Test: aicp --check
  ```
- **Expected output:** AICP `--check` reports `[OK] rlm_qwen3_6_27b_local: OK` once the local server is running.
- **Validation:** Operator-side; outside this wiki repo. The AICP-side handoff at `~/devops-expert-local-ai/docs/SESSION-2026-04-24-HANDOFF.md` is the authoritative state-of-deployment.
- **Rollback:** Disable backend in AICP config; remove backend file. Existing `local`, `k2_6_local`, `k2_6_openrouter`, `ollama_cloud` backends untouched.

## Rollback

Global rollback if the plan fails irrecoverably partway through (per-step rollbacks above handle isolated failures):

1. Stop any running training jobs (`uv run rl --stop` or kill the SLURM job)
2. Preserve the last good checkpoint at `./checkpoints/rlm-qwen3-6-27b-LAST/` (rename, don't delete; a partial checkpoint may still be useful for diagnosis)
3. Document the failure mode at `wiki/log/YYYY-MM-DD-rlm-qwen3-6-27b-finetune-postmortem.md` (use the `note` template; include verbatim error logs, last-good config, hypothesis on root cause)
4. Operator-review before re-attempting; the plan may need recipe-level changes (e.g., different teacher, different filtering thresholds, different hyperparameters)

## Completion Criteria

- [ ] Trained checkpoint exists at `./checkpoints/rlm-qwen3-6-27b/` and loads in vLLM successfully (Step 5 validation)
- [ ] All 4 RLM Table 1 benchmarks evaluated and recorded (Step 6 validation)
- [ ] At least 2 of 4 benchmarks meet or exceed the **target column** in Step 6's table (composition path's empirical claim validated; specifically OOLONG and OOLONG-Pairs are most relevant since these are RLM's strongest gain regimes per paper Observation 2)
- [ ] Results contributed back to wiki via `gateway contribute` (Step 7) with `pipeline post` returning 0 errors
- [ ] (Optional) AICP backend deployed and `--check` reports OK (Step 8)
- [ ] Cost report delivered to operator: actual H100-hours × actual rate = USD spent vs budgeted ($300-500)

## Limitations and Known Risks

> [!warning] What this plan assumes that may not hold
>
> 1. **The 8B → 27B recipe-scaling assumption.** The paper's recipe is validated at 8B. Scaling to 27B may need different hyperparameters (LR, batch size, FSDP config, IPO masks). Step 5's hard-limit (3 consecutive divergent runs → stop + operator-review) protects against silent failure but does not guarantee success.
> 2. **Teacher model availability.** Qwen3-Coder-480B-A35B-Instruct as the teacher (per the paper) requires either (a) self-hosted vLLM at significant compute cost, or (b) OpenRouter access at per-token cost layered onto training. Alternative teachers (smaller, cheaper) may produce lower-quality trajectories — risking the 28.3% improvement claim from the paper.
> 3. **Filter thresholds may need tuning.** The paper's 16% bad-FINAL / 13% bad-FINAL_VAR rates were measured for Qwen3-Coder-480B as teacher. A different teacher will have different rates; the programmatic correction code in Step 4 needs validation against actual teacher behavior.
> 4. **Domain-transfer risk.** RLM-Qwen3-8B trained on LongBenchPro generalized to OOLONG / BrowseComp+ / CodeQA / OOLONG-Pairs (paper Observation 6). The same generalization may or may not hold at 27B scale — empirical question, answerable only by running Step 6.
> 5. **Hardware compatibility.** Operator ordered RTX 4090 (renewed) on 2026-04-27 (ETA 2-3 weeks); until delivery, current tier-0 is RTX 2080 Ti (Turing, pre-Ampere) which may not run prime-rl natively (the README's tested hardware list starts at RTX 3090). Once 4090 is in hand, **Step 8 deployment becomes comfortable** — Qwen3.6-27B at UD-IQ2 (~14-16GB) fits 24GB with headroom. **Training (Steps 3-5) still requires cloud GPU access regardless** — single 4090 is ~100-500x slower than 8× H100 cluster (months vs ~24 hours). If cloud GPU access is unavailable, this plan does not apply — fallback to deploying RLM-Qwen3-8B from [`mit-oasys/rlm-qwen3-8b-v0.1`](https://huggingface.co/mit-oasys/rlm-qwen3-8b-v0.1) (confirmed live 2026-04-27) or vanilla Qwen3.6-27B without RLM training.
> 6. **License compatibility.** Qwen3.6-27B is Apache 2.0; LongBench Pro license needs verification (likely permissive, but check). RLM SDK is open per repo. **No vendor lock-in introduced by execution.**

> [!info] Future extensions (not in scope for this plan)
>
> 1. **Chinese-split training** — LongBench Pro is bilingual; a follow-up plan could train on the Chinese split. Out of scope here.
> 2. **Multi-modal training** — Qwen3.6-27B is natively multimodal (Vision Encoder + mmproj). RLM paper is text-only. A multimodal RLM extension is a research direction.
> 3. **Async RL on top of SFT** — prime-rl supports both. The 8B recipe was SFT-only (per paper). RL post-training of the SFT'd model could yield additional gains; out of scope.
> 4. **Larger teacher model** — Qwen3.6-27B fine-tuned could itself become a teacher for a hypothetical RLM-Qwen3.5-MoE (35B-A3B) trainee. Recursion at the meta-level. Out of scope.

## Mission Framing

This plan is a worked example of step 6 ("close gaps systematically") of the [[anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence|anti-vendor-lock-in lesson]]'s How-to-Apply. The lesson's gap analysis identified open-source paper evidence at every stack layer; this plan converts the *generation (tier-0 recursive)* layer's hypothetical from "paper evidence at 8B" to "operator-validated evidence at 27B" — provided execution succeeds.

By [Principle 4](../../lessons/04_principles/hypothesis/declarations-are-aspirational-until-infrastructure-verifies-them.md), the tier-0 candidate comparison's "Composition Path" is **aspirational until infrastructure verifies it**. This operations plan IS that infrastructure (deterministic steps + validation gates + rollback paths). Executing the plan is what demotes the claim from aspirational to empirical. **Until executed, the plan itself is at `seed` maturity** — its very existence is the verification gate that the composition path is *concretely actionable*, not vaporware.

By [Principle 1](../../lessons/04_principles/hypothesis/infrastructure-over-instructions-for-process-enforcement.md), every step has a Validation field that uses tooling output, not narrative judgment. A "dumb" agent following this plan mechanically would not need to make trade-off decisions — those have been resolved (or marked as out-of-scope) here.

**Phase-2-conditional execution per [Saturation Lesson Hard Rule #11](../../lessons/01_drafts/saturation-declarations-are-p4-aspirational-test-by-attempting-forward-work.md)**: this plan's spend ($300-500 cloud rental, one-time) is justified IFF the Phase-1 routing approach (RLM-Qwen3-8B + vanilla Qwen3.6-27B + AICP context-length routing, $0 cash) demonstrates a real ceiling on operator's actual workload. The Phase-1 path is now available at $0 since the [MIT RLM-Qwen3-8B checkpoint](https://huggingface.co/mit-oasys/rlm-qwen3-8b-v0.1) is confirmed live (2026-04-27) and the operator's incoming RTX 4090 (ETA 2-3 weeks from 2026-04-27) comfortably runs both candidates locally. Empirical evidence from the Phase-1 deployment is the operator's gate for Phase-2 commitment.

## Cost-Math Cross-Check

| Item | Estimate | Source |
|---|---|---|
| H100-hours for 8B recipe (paper) | 48 H100 hours | [RLM paper §Training](../../sources/tools-integration/src-rlm-paper-deep-dive-table-1-training-recipe-six-observations.md) |
| Scaling factor 8B → 27B (parameters) | 3.375× | (27/8) |
| Scaling factor for compute (loose, with FSDP overhead + sequence parallelism) | ~3-4× compute | typical empirical range |
| Estimated H100-hours for 27B recipe | **~150-200 H100 hours** | scaled from 48 × 3-4 |
| Cloud rate (2026, typical) | $2-3 USD per H100-hour | provider-spread; Lambda / RunPod / Together |
| **Total estimated cost** | **$300-600 USD** | (150-200 × $2-3) |
| Operator's prior cloud baseline (per [AICP handoff](file:///home/jfortin/devops-expert-local-ai/docs/SESSION-2026-04-24-HANDOFF.md)) | $540 CAD/mo | one month of training cost ≈ one prior month of cloud bill |
| Operator's current smart-routed baseline | $100 CAD/mo | the $540 → $100 finding |
| **One-time training cost vs ongoing reduced cloud spend** | Pays back via post-Anthropic mission progression IF the model becomes a primary local tier | mission-critical conditional |

The cost math is operator-decision territory: a one-time ~$400 USD training run vs ongoing recurring cloud spend. **This plan does not make that decision; it scopes what execution looks like once the decision is made.**

## Relationships

- IMPLEMENTS: [[rlm-qwen3-8b-vs-qwen3-6-27b-tier-0-long-context-candidate|Tier-0 Candidate Comparison]] § Composition Path
- BUILDS ON: [[src-rlm-paper-deep-dive-table-1-training-recipe-six-observations|RLM Paper Deep Dive]] (the 8B recipe this plan scales)
- BUILDS ON: [[src-prime-intellect-prime-rl-async-rl-training-at-scale|Prime Intellect prime-rl]] (training framework used in Steps 2 + 5)
- BUILDS ON: [[src-prime-intellect-verifiers-llm-rl-environments|Prime Intellect Verifiers]] (RLMEnv used in Step 6)
- BUILDS ON: [[src-rlm-recursive-language-models-mit-oasys|RLM Implementation]] (deployment runtime in Step 8)
- BUILDS ON: [[src-qwen3-6-27b-dense-beats-397b-moe-agentic-coding|Qwen3.6-27B Base Model]] (the dense base trained from)
- BUILDS ON: [[src-qwen3-6-27b-2-bit-26-tool-calls-unsloth-discussion|Qwen3.6-27B at 2-bit Unsloth]] (quantization path for Step 8)
- BUILDS ON: [[src-oolong-and-longbench-pro-long-context-benchmarks-rlm-anchors|OOLONG + LongBench Pro Benchmarks]] (training data + 2 evaluation surfaces)
- BUILDS ON: [[src-browsecomp-plus-and-longbench-v2-rlm-table-1-benchmarks|BrowseComp+ + LongBench v2 Benchmarks]] (remaining 2 evaluation surfaces)
- DEMONSTRATES: [[anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence|Anti-Vendor-Lock-In Lesson]] § How-to-Apply step 6
- DEMONSTRATES: [[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4]] (this plan converts a hypothetical decision matrix entry into actionable infrastructure)
- DEMONSTRATES: [[infrastructure-over-instructions-for-process-enforcement|Principle 1]] (every step has a tooling-verified Validation field)
- FEEDS INTO: [[2026-consumer-hardware-ai-stack|2026 Consumer Hardware AI Stack]] (potential new tier-0 candidate path once executed)
- FEEDS INTO: [[ai-infrastructure-decision-framework-2026|AI Infrastructure Decision Framework 2026]]
- RELATES TO: [[2026-04-27-session-end-handoff-13-artifacts-rlm-thread-saturation|2026-04-27 Session-End Handoff]] § P1 wiki-side (this is item #5 of that list)
- RELATES TO: [[rlm-thread-evidence-chain-2026-04-27|Learning Path — RLM Thread Evidence Chain]] (Path C: Reproduce Training)

## Backlinks

[[Tier-0 Candidate Comparison]]
[[src-rlm-paper-deep-dive-table-1-training-recipe-six-observations|RLM Paper Deep Dive]]
[[src-prime-intellect-prime-rl-async-rl-training-at-scale|Prime Intellect prime-rl]]
[[src-prime-intellect-verifiers-llm-rl-environments|Prime Intellect Verifiers]]
[[RLM Implementation]]
[[Qwen3.6-27B Base Model]]
[[Qwen3.6-27B at 2-bit Unsloth]]
[[OOLONG + LongBench Pro Benchmarks]]
[[BrowseComp+ + LongBench v2 Benchmarks]]
[[Anti-Vendor-Lock-In Lesson]]
[[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4]]
[[infrastructure-over-instructions-for-process-enforcement|Principle 1]]
[[2026 Consumer Hardware AI Stack]]
[[ai-infrastructure-decision-framework-2026|AI Infrastructure Decision Framework 2026]]
[[2026-04-27 Session-End Handoff]]
[[Learning Path — RLM Thread Evidence Chain]]
