---
title: "Synthesis — Prime Intellect PRIME-RL: Async RL Training at Scale (1000+ GPUs, FSDP2 + vLLM, Used to Train RLM-Qwen3-8B)"
aliases:
  - "Prime Intellect prime-rl"
  - "PRIME-RL"
  - "Async RL Training at Scale"
  - "Synthesis — prime-rl"
type: source-synthesis
domain: tools-integration
status: synthesized
confidence: high
maturity: seed
created: 2026-04-27
updated: 2026-04-27
last_reviewed: 2026-04-27
sources:
  - id: prime-rl-repo
    type: documentation
    url: https://github.com/PrimeIntellect-ai/prime-rl
    file: raw/articles/primeintellect-aiprime-rl.md
    title: "PrimeIntellect-ai/prime-rl — Async RL Training at Scale"
    ingested: 2026-04-27
  - id: verifiers-companion
    type: wiki
    file: wiki/sources/tools-integration/src-prime-intellect-verifiers-llm-rl-environments.md
    description: "Verifiers companion synthesis — prime-rl natively integrates with verifiers environments via the Environments Hub"
  - id: rlm-paper-trainer
    type: wiki
    file: wiki/sources/tools-integration/src-rlm-paper-deep-dive-table-1-training-recipe-six-observations.md
    description: "RLM paper deep-dive — prime-rl is the named training library for RLM-Qwen3-8B (48 H100 hours, batch 64, 300 steps)"
  - id: aipo-paper
    type: paper
    url: https://arxiv.org/abs/2505.24034
    title: "AIPO — Asynchronous Importance-Sampling Policy Optimization (Llama-RL)"
    description: "Loss objective prime-rl uses by default; introduced in Llama-RL"
  - id: ipo-paper
    type: paper
    url: https://arxiv.org/pdf/2602.04879
    title: "IPO — DPPO-Binary TV variant"
    description: "Default loss in prime-rl as of 2026-03-02 changelog entry"
  - id: kimi-k25-kl
    type: paper
    url: https://arxiv.org/pdf/2602.02276
    title: "Kimi-K2.5 KL"
    description: "KL term in prime-rl's default loss"
tags: [prime-rl, prime-intellect, async-rl, rl-training-at-scale, fsdp2, vllm, fp8-inference, pd-disaggregation, expert-parallelism, context-parallelism, moe-training, rlm-qwen3-8b-trainer, sft, multi-node-slurm, kubernetes, intellect-3, qwen3-moe, glm-5, minimax-m2, nemotron-h, gpt-oss, aipo, ipo, kimi-k25-kl, mit-csail-connection, mission-2026-04-27, sovereignty-tier, anti-vendor-lock-in, post-training-stack, tools-integration]
---

# Synthesis — Prime Intellect PRIME-RL

## Summary

PRIME-RL is Prime Intellect's open-source framework for **asynchronous reinforcement learning training at scale** — designed to be hackable yet capable of scaling to **1000+ GPUs**, with native integration to [`verifiers`](src-prime-intellect-verifiers-llm-rl-environments.md) environments and the Prime Intellect Environments Hub. It is the **named training library used for RLM-Qwen3-8B** in the [RLM paper](src-rlm-paper-deep-dive-table-1-training-recipe-six-observations.md) (batch 64, 300 steps, 48 H100 hours total). The framework's distinguishing claims: **fully asynchronous RL** (inference can generate rollouts from a stale policy up to `k` steps ahead of the trainer; default `k=2`), **performant at frontier scale** (FSDP2 for training + vLLM for inference, FP8 inference, PD disaggregation, EP/CP parallelism), **end-to-end post-training pipeline** (SFT + RL + evals as one cohesive product), **multi-node deployment** (SLURM + Kubernetes), and **deep multimodal support** for VLMs like Qwen3-VL. Custom-stack model implementations exist for **GLM-5, Qwen3 MoE, Qwen3.5 MoE, MiniMax M2, Nemotron H, Trinity, GLM-4/GLM-4.5, INTELLECT-3, GPT-OSS** — covering the major open-weight families. The repo includes 5 basic-tier (1-8 GPU) examples (Reverse Text on Qwen3-0.6B, Wordle, Alphabet Sort, Wiki Search, Hendrycks Sanity) + 5 advanced-tier (32-2048 GPU) examples (Qwen3 30B Math/SWE, INTELLECT-3.1, MiniMax-M2.5 SWE, GLM-5 PD-disaggregation). Apache 2.0 licensed. **Mission relevance**: this is the open-source training framework that — combined with verifiers' RLMEnv — would let the operator (or any community member) reproduce the RLM-Qwen3-8B post-training recipe on commodity GPUs.

## Reference Card

> [!info] PRIME-RL reference card
>
> | Field | Value |
> |---|---|
> | **Type** | Async RL training framework + post-training pipeline |
> | **License** | Apache 2.0 |
> | **Repo** | github.com/PrimeIntellect-ai/prime-rl |
> | **Setup** | `curl -sSL https://raw.githubusercontent.com/PrimeIntellect-ai/prime-rl/main/scripts/install.sh \| bash` (one-shot) |
> | **Hardware tested** | NVIDIA RTX 3090 / 4090 / 5090 / A100 / H100 / H200 / B200 |
> | **Hardware floor** | At least 1 NVIDIA GPU (consumer GPUs work for small examples) |
> | **Python** | 3.12 (validated in setup) |
> | **Package manager** | `uv` (mandated; `python` directly disallowed per AGENTS.md) |
> | **Default async level (`k`)** | 2 (inference is up to 2 steps ahead of trainer) |
> | **Default loss** | IPO (DPPO-Binary TV variant) + Kimi-K2.5 KL term (as of 2026-03-02 changelog) |
> | **Training: SFT** | `uv run sft @ configs/...toml` |
> | **Training: RL** | `uv run rl @ configs/...toml` |
> | **Inference** | `uv run inference @ configs/...toml` (vLLM-backed) |
> | **Orchestrator** | `uv run orchestrator @ configs/orch.toml` |
> | **Evaluation** | `uv run eval @ configs/eval.toml` |
> | **Multi-node** | SLURM templates + Kubernetes deployment |
> | **Multimodal** | Qwen3-VL, Qwen3.5-VL, Qwen3.5-MoE-VL |
> | **Confidence label** | high — read README + AGENTS.md + CHANGELOG (massive — covers 2025-12 to 2026-04 evolution) + start of docs/async.md and docs/benchmarking.md and docs/bring-your-own-algorithms.md as Layer 1 sources; ~3000 more lines of docs not exhaustively read but the architecture + extensibility patterns are visible. |
> | **Mission relevance** | Critical — the named training library used to produce RLM-Qwen3-8B; the open-source path to reproduce frontier-quality post-training |

## Key Insights

1. **Asynchronous RL is the central design choice**. Per README: "Fully asynchronous RL for high-throughput agentic training at scale." The async architecture lets inference run `k` steps ahead of the trainer (default `k=2`), eliminating idle time on either side. The math: at each step `n`, the trainer produces policy π_n with weights θ_n from rollouts (x_n, y_n); the inference produces rollouts (x_n, y_n) from policy π_{max(0, n-k)}. The two run concurrently, with bounded staleness — and the loss objective (AIPO variant) handles the natural distribution shift caused by off-policy training.

2. **The performance scale is frontier-grade**. README Item 2: "Performant: built to train 1T+ MoE models on 1000+ GPUs with FSDP2 for training and vLLM for inference, with FP8 inference, PD disaggregation, EP and CP parallelism, and more." This is not a research-toy — it's the production training framework Prime Intellect uses internally.

3. **The Models Support table is comprehensive for current open-weight families**:
   | Family | Custom impl | EP | CP |
   |---|---|---|---|
   | GLM-5 | yes | ✅ | ✅ |
   | Qwen3 MoE | yes | ✅ | ✅ |
   | Qwen3.5 MoE | yes | ✅ | ✅ |
   | Qwen3 / Qwen3.5 VLMs | MoE only | MoE only | ✅ |
   | MiniMax M2 | yes | ✅ | ✅ |
   | Nemotron H | yes | ✅ | ❌ |
   | Trinity (afmoe) | yes | ✅ | ✅ |
   | GLM-4 / GLM-4.5 / INTELLECT-3 | yes | ✅ | ✅ |
   | GPT-OSS (HF, MoE) | yes | ❌ | ✅ |
   | Other HF causal LMs | varies | ❌ | ✅ |
   The `[model] impl = "auto"` default automatically selects the optimized custom stack when available, falling back to HuggingFace.

4. **End-to-end post-training in one framework**: SFT + RL + evaluation. README Item 4: "End-to-end post-training: SFT, RL training, and evals." A user can take a base model through full post-training (SFT → RL → eval) without hopping between frameworks.

5. **The CHANGELOG documents major design evolution (2025-12 → 2026-04)**. The breaking-change history reveals deep refactoring across:
   - **Config consolidation** (2026-02-24) — all configs moved into `prime_rl.configs`; class renames; TOML structure stabilization
   - **Loss objective evolution** (2026-03-02) — IPO (DPPO-Binary TV) + Kimi-K2.5 KL became the default; removed many older loss-shape options; `ipo_mask_low`/`ipo_mask_high` introduced
   - **Async semantics finalization** — `max_async_level` k=2 default
   - **Deployment unification** (2026-02-23) — `[deployment]` section replaces scattered GPU-id configs; `single_node` / `multi_node` types; SLURM templates renamed and reorganized
   - **Per-env training architecture** (2026-04-09) — `[[orchestrator.train.env]]` replaces flat `[[orchestrator.env]]`; per-env sampling overrides; per-env eval sampling overrides
   - **Custom loss + custom advantage support** (2026-02-26) — `loss.type = "custom"` and `advantage.type = "custom"` for bring-your-own-algorithm extensibility
   - **MoE expert parallelism** (2026-01-15) — `model.ep > 1` properly parallelizes (was no-op before)

   Reading the CHANGELOG is reading the framework's mind: which abstractions stabilized, which were ripped out (`temp_scheduler`, `verification.enabled`, `skip_first`, etc.), which became defaults.

6. **The default loss is IPO + Kimi-K2.5 KL — non-trivial to swap**. Per the 2026-03-02 changelog: *"Made IPO (DPPO-Binary TV variant + Kimi-K2.5 KL) the default loss. Removed `ratio_type`, `token_mask_low`, `token_mask_high`, `sequence_clip_high`, `geo_mask_low`, `geo_mask_high`, `sequence_mask_low`, `sequence_mask_high`. Added `ipo_mask_low` (default: 0.2) and `ipo_mask_high` (default: 0.2) for token-level probability-difference masking. Changed `kl_tau` default from 0.0 to 1e-3."* This is structural opinion — prime-rl picks loss objectives, not just hyperparameters.

7. **Bring-your-own algorithms via `loss.type = "custom"` and `advantage.type = "custom"`**. The framework is opinionated about the default but extensible: users can register custom loss functions (per-sequence) and advantage functions (per-example) via `import_path = "my_module.my_loss"` config. This is the wiki's [structured-context](../../spine/models/depth/model-context-engineering.md) pattern at the algorithm level — a stable interface (LossInputs, LossOutputs dataclasses) lets researchers plug in alternatives without touching the trainer.

8. **AGENTS.md mandates `uv run`, never raw `python`**. Direct quote: *"Always use uv: run code with `uv run` or `uv run <command>`, never raw `python`."* This is the wiki's [`.venv/bin/python`](../../../CLAUDE.md) Hard Rule #5 in spirit — venv-only deps require venv-aware execution.

9. **The Skills folder is symlinked to `.claude/skills/`**. Per AGENTS.md: *"Skills live in `skills/` and are symlinked to `.claude/skills/`. They teach agents how to handle specific workflows... When you make changes to the codebase, check if any skills need to be updated to stay accurate. You are responsible for maintaining the skills folder."* This matches the [verifiers companion](src-prime-intellect-verifiers-llm-rl-environments.md) pattern. Both Prime Intellect repos enforce "skills must stay current with code" as agent contributor discipline.

10. **The `[orchestrator.train.env]` per-environment training architecture**. As of 2026-04-09, the trainer can mix multiple environments per training run with explicit per-env ratios (`[[orchestrator.train.env]]` `ratio = ...`), per-env sampling overrides (`[sampling]`), and per-env eval overrides. This is the production-RL-training equivalent of the wiki's [Goldilocks principle](../../lessons/04_principles/hypothesis/right-process-for-right-context-the-goldilocks-imperative.md) — different envs need different sampling configurations; enforce that explicitly rather than globally.

11. **W&B + Prometheus + JSON-structured logging out-of-the-box**. From the changelog: *"`trainer.metrics_server` (NEW)"* — Prometheus `/metrics` endpoint with step/loss/throughput/grad_norm/etc. *"`log.json_logging`"* — JSON structured logging for log aggregation systems (Loki, Grafana). *"`wandb.shared`"* — single W&B run for trainer + orchestrator (instead of two separate). Production observability is first-class.

12. **Conservative test discipline**. AGENTS.md: *"Don't add new tests unless the user explicitly asks for them or it's clearly necessary. Editing existing tests is fine, but adding new test files or test functions should be the exception, not the default. Test what matters: only test code with clear, isolated logic — pure functions, abstract base classes, data transformations, well-defined algorithms."* This matches the wiki's anti-aspirational-test-coverage philosophy.

13. **Branch prefixes + draft-PR discipline**. AGENTS.md: *"`feat/`, `fix/`, `chore/`"* prefixes for branches; *"always create PRs as drafts (`gh pr create --draft`)"* to avoid triggering CI unnecessarily. Production engineering hygiene baked into the contributor agent guidance.

## Deep Analysis

### Architecture: Three Cooperating Components

```
┌──────────────────────┐    ZMQ    ┌──────────────────────┐
│   Trainer (FSDP2)    │◄─────────►│   Orchestrator       │
│   (produces θ_n)     │           │   (coordinates)      │
└──────────────────────┘           └────────────┬─────────┘
                                                │
                                                ▼
                                   ┌──────────────────────┐
                                   │  Inference (vLLM)    │
                                   │  (rollouts from π_n) │
                                   └──────────────────────┘
                                                │
                                                ▼
                                   ┌──────────────────────┐
                                   │  Verifiers Env       │
                                   │  (rubric scores)     │
                                   └──────────────────────┘
```

**Trainer** runs FSDP2 (PyTorch's fully-sharded data-parallel v2) for memory-efficient training across many GPUs. **Orchestrator** is the coordinator — it manages the rollout buffer, applies the loss/advantage functions, and maintains the async pipeline. **Inference** runs vLLM as the LM-serving layer; rollouts produced by inference (via verifiers environments) feed back to the orchestrator → trainer.

### Asynchronous Training in Detail (from `docs/async.md`)

The async loss objective:

$$
\mathcal{J}_{\text{AIPO}}(\theta) = \frac{1}{\sum_j \sum_i |y_i^{(j)}|} \sum_j \sum_i \sum_t \min\left( \frac{\pi(y_{i,t}^{(j)}|x_j, y_{i,<t}^{(j)})}{\mu(y_{i,t}^{(j)}|x_j, y_{i,<t}^{(j)})}, \delta \right) \hat{A}_{i,t}^{(j)}
$$

where μ is the policy that generated the rollout, π is the current policy, Â is the token-level advantage, and δ is the importance-sampling clipping ratio. The min(ratio, δ) handles the natural distribution shift from off-policy generation — this is the AIPO variant that the docs cite from Llama-RL.

Default: `max_async_level = 2`. Allows trainer + inference to run concurrently with up to 2-step staleness. From the docs: "with `k=1` and trainer and inference step timings being equal, this allows to run without any idle time on either the trainer or inference. By default, we set `k=2` to allow overlap with a weight broadcast over the Internet, which is needed for decentralized training."

### Models Support Matrix

| Family | Example IDs | MoE | EP | CP |
|---|---|---|---|---|
| GLM-5 (`glm_moe_dsa`) | `zai-org/GLM-5`, `zai-org/GLM-5-FP8` | yes | ✅ | ✅ |
| Qwen3 MoE (`qwen3_moe`) | `Qwen/Qwen3-30B-A3B`, ... | yes | ✅ | ✅ |
| Qwen3.5 MoE (`qwen3_5_moe`) | `Qwen/Qwen3.5-35B-A3B`, ... | yes | ✅ | ✅ |
| Qwen3 / Qwen3.5 VLMs | (multimodal.md table) | MoE only on MoE VLMs | MoE only | ✅ |
| MiniMax M2 (`minimax_m2`) | `MiniMax/MiniMax-M2` | yes | ✅ | ✅ |
| Nemotron H (`nemotron_h`) | `nvidia/Nemotron-3-Nano-30B-A3B`, `nvidia/Nemotron-3-Super-120B-A12B` | yes | ✅ | ❌ |
| Trinity (`afmoe`) | `arcee-ai/Trinity-Mini` | yes | ✅ | ✅ |
| GLM-4/GLM-4.5/INTELLECT-3 (`glm4_moe`) | `THUDM/GLM-4-9B-0414`, `zai-org/GLM-4.5-Air`, `PrimeIntellect/INTELLECT-3` | yes | ✅ | ✅ |
| GPT-OSS (HF, MoE) | `openai/gpt-oss-20b`, `openai/gpt-oss-120b` | yes | ❌ | ✅ |
| Other HF causal LMs | Qwen3 dense, Mistral, ... (`impl = "hf"`) | varies | ❌ | ✅ |

**EP** = Expert Parallelism (split MoE experts across GPUs). **CP** = Context Parallelism (split long sequences across GPUs). Default `[model] impl = "auto"` selects custom stack when registered.

### Training Examples — Tier-by-Tier

**Basic Training (1-8 GPUs)** — for getting started:

| Example | Model | Hardware | Time | What it teaches |
|---|---|---|---|---|
| Reverse Text | Qwen3-0.6B | 1 consumer GPU | minutes | Tiny-scale single-turn SFT + RL |
| Wordle | Qwen3-1.7B | 2-4 H100 | hours | Multi-turn SFT + RL training |
| Alphabet Sort | Qwen3-4B-Instruct-2507 | 1 H100 | ~1 hour | LoRA-based multi-turn RL (no SFT warmup) |
| Wiki Search | Qwen3-4B-Instruct-2507 | (sized to env) | (varies) | Multi-turn web search tool use |
| Hendrycks Sanity | DeepSeek-R1-Distill-Qwen-1.5B | (sized to env) | (varies) | Algorithm ablations on a filtered MATH subset |

**Advanced Training (32-2048 GPUs)** — for frontier work:

| Example | Model | Domain |
|---|---|---|
| Qwen 3 30B-A3B Math | Qwen3-30B-A3B | Hard math |
| Qwen 3 30B-A3B SWE | Qwen3-30B-A3B | Hard SWE problems |
| INTELLECT-3.1 | (Prime Intellect's frontier model) | Reproduction recipe |
| MiniMax-M2.5 SWE | MiniMax-M2.5 | Agentic SWE tasks |
| High-throughput GLM-5 | GLM-5 | PD disaggregation + FP8 inference on SWE |

The Reverse Text example on a single consumer GPU in minutes is the operator's tier-0 entry point. The advanced tier requires SLURM-cluster access — Prime Intellect's compute platform is the natural path.

### Bring-Your-Own Algorithms

PRIME-RL is opinionated about the default but explicitly extensible:

**Custom Loss Function**:
```python
from prime_rl.trainer.rl.loss import LossInputs, LossOutputs

def my_custom_loss(inputs: LossInputs, **kwargs) -> LossOutputs:
    ratio = torch.exp(inputs.trainer_logprobs - inputs.inference_logprobs)
    clipped_ratio = torch.clamp(ratio, 1 - clip_eps, 1 + clip_eps)
    surr1 = ratio * inputs.advantages
    surr2 = clipped_ratio * inputs.advantages
    loss = -torch.min(surr1, surr2)[inputs.loss_mask].sum()
    return LossOutputs(loss=loss, metrics={"clip_frac": (...)})
```

Configured via:
```toml
[loss]
type = "custom"
import_path = "my_module.ppo_clip_loss"
kwargs = { clip_eps = 0.2 }
```

**Custom Advantage Function**:
```python
def normalized_advantage(inputs: AdvantageInputs, eps: float = 1e-8) -> AdvantageOutputs:
    mean = inputs.rewards.mean(dim=1, keepdim=True)
    std = inputs.rewards.std(dim=1, keepdim=True)
    advantages = (inputs.rewards - mean) / (std + eps)
    return AdvantageOutputs(advantages=advantages)
```

This extensibility pattern is critical for research applications: experiment with PPO vs IPO vs custom; experiment with different reward shaping; experiment with different baselines — all without touching the trainer's internals.

### CHANGELOG-Visible Refactoring Pattern

The CHANGELOG (which makes up a significant fraction of the README dump) is a transparent record of the framework's design evolution. Reading it sequentially reveals:

1. **Period 2025-12 → 2026-01**: foundational stabilization. Config schema introduced. LoRA moved from experimental. Resume-from-checkpoint behavior settled.
2. **Period 2026-01 → 2026-02**: scale features added. Async-level k semantics finalized. Multi-node SLURM templates. Expert parallelism became real (was no-op).
3. **Period 2026-02 → 2026-03**: deployment unification. `[deployment]` config section consolidates GPU/node assignments. Custom-loss + custom-advantage support. Comprehensive metrics overhaul (`{metric}/{scope}/{stat}` naming convention).
4. **Period 2026-03 → 2026-04**: opinion locking. IPO + Kimi-K2.5 KL became the default loss; many older loss-shape configs removed. Per-env training architecture replaces flat configs. Per-env sampling overrides.

This is mature production engineering — opinionated defaults that consolidate experience, with extensibility points for the cases where opinion isn't enough. The wiki's [Goldilocks principle](../../lessons/04_principles/hypothesis/right-process-for-right-context-the-goldilocks-imperative.md) at the framework-design level: pick a reasonable default; don't over-flag-ify; expose extension points where genuine variability exists.

### How RLM-Qwen3-8B Was Trained (cross-referenced with the RLM paper)

Per the [RLM paper deep-dive](src-rlm-paper-deep-dive-table-1-training-recipe-six-observations.md):
- Source data: 750 English LongBenchPro tasks
- Distillation source: RLM(Qwen3-Coder-480B-A35B) producing trajectories
- Filtering: 2250 → 1072 candidate trajectories
- Per-turn SFT decomposition
- Programmatic FINAL/FINAL_VAR correction (16% / 13% of turns had errors)
- **Training: prime-rl, batch 64, 300 steps, 48 H100 hours**
- Fine-tuning Qwen3-8B with the prime-rl SFT pipeline (`uv run sft @ configs/...toml`)

The 48-H100-hour number, combined with prime-rl's `single_node` deployment supporting consumer hardware down to RTX 3090 (per the Setup section), means: **a researcher with access to a multi-H100 cloud rental (~$48-100 USD on typical rates) can replicate the RLM-Qwen3-8B post-training run end-to-end**. This is the open-source path the wiki's mission cares about.

## Open Questions

> [!question] Does the prime-rl SFT trainer support the per-turn decomposition the RLM paper used?
> The RLM paper's training recipe decomposes RLM trajectories into per-turn SFT samples (each iteration = its own input/output pair). Does prime-rl's SFT entrypoint support this trajectory-decomposition input format natively, or does the dataset need pre-processing? (Requires: reading docs/configs.md or examples/ for trajectory-style SFT.)

> [!question] Can prime-rl run on the operator's RTX 2080 Ti (Tier-0 hardware)?
> README says hardware tested includes RTX 3090/4090/5090 (consumer). RTX 2080 Ti (Turing architecture) is not in the tested list — Turing predates Ampere/Ada/Hopper. May lack BF16 support. (Requires: actual test or compatibility analysis. Possibly LoRA training can fit, but full SFT/RL might need at least Ampere.)

> [!question] What's the minimum-viable single-GPU training session?
> The Reverse Text example runs on "a single consumer GPU in a few minutes". Validate this is the right entry point for operator hardware before scaling to anything else. (Requires: test run.)

> [!question] How does the elastic inference pool work?
> CHANGELOG 2026-01-19: *"orchestrator.client.elastic — elastic inference pool with DNS-based service discovery. Supports dynamic server scaling via any DNS hostname with multiple A records (Kubernetes headless services, Consul, Route53, etc.). Automatically syncs LoRA adapters on new servers and only exposes ready servers to workers."* This sounds production-grade — a Kubernetes-deployed prime-rl could elastically scale inference based on training throughput. Worth a deeper read for any future production deployment. (Requires: docs/deployment.md.)

> [!question] What's the ZMQ transport between orchestrator and trainer?
> CHANGELOG 2025-12-22: *"`{orchestrator,trainer}.transport.zmq` — Added ZMQ transport for training batches and micro batches"*. ZMQ-based message passing between orchestrator and trainer suggests a deliberate choice over gRPC or other RPC. Likely chosen for minimal overhead at frontier scale. (Requires: docs/transport or src/prime_rl/transport.)

> [!question] Can the AICP backend integrate with prime-rl as an inference provider?
> AICP currently routes between local (LocalAI), k2_6_local (llama.cpp), k2_6_openrouter, claude, ollama_cloud. Could prime-rl's `[client]` config point at AICP's local backend as the inference endpoint for evaluation runs? This would let the operator evaluate AICP backends in standardized ways. (Requires: AICP-side integration design.)

> [!question] What's INTELLECT-3 / INTELLECT-3.1?
> Prime Intellect's own frontier model — `PrimeIntellect/INTELLECT-3` is in the Models Support table; advanced training example "INTELLECT-3.1" reproduces a training run. The wiki should track this as Prime Intellect's own model entry in the [AI Model Provider Harness Decision Matrix](../../spine/references/ai-model-provider-harness-decision-matrix-2026.md). (Requires: pricing + capability info from Prime Intellect.)

## Applicability

> [!info] Where prime-rl applies for the wiki's mission
>
> - **Reproducing the RLM-Qwen3-8B training**: cited as the named training library in the RLM paper; recipe is 48 H100 hours
> - **Post-training open-weight models on local + cloud GPUs**: SFT + RL in one framework; consumer GPU floor (Reverse Text on RTX 3090)
> - **Anti-vendor-lock-in training pipeline**: Apache 2.0 + open weights + open-source SDKs throughout
> - **Multi-node enterprise training**: SLURM + Kubernetes deployment for fleet scale
> - **VLM training**: Qwen3-VL family supported with multi-modal docs

> [!warning] Where prime-rl does NOT apply
>
> - **No GPU available**: requires at least 1 NVIDIA GPU
> - **Pre-Ampere GPUs (RTX 2080 Ti, etc.)**: not in the tested hardware list; FP8 + Hopper-only kernels may not be available; LoRA might be the only path
> - **Inference-only deployments**: prime-rl is for training; inference uses vLLM separately (which prime-rl wraps but doesn't replace as a serving framework)
> - **Non-LM RL** (game agents, robotics): designed for LMs

## How to Apply

> [!tip] Concrete adoption paths
>
> 1. **Validate hardware compatibility on operator's RTX 2080 Ti** — try the Setup steps; check if BF16/flash-attn3 work on Turing architecture; if not, stick to LoRA-mode + small models.
> 2. **Run Reverse Text example as smoke test** — `uv run sft` on Qwen3-0.6B with the example config. Validates the install + training path. Cost: minutes of GPU time + electricity.
> 3. **Reproduce RLM-Qwen3-8B step 1 (SFT-only on LongBenchPro)** — trajectory generation requires Qwen3-Coder-480B (huge), but operator could try with a smaller distillation source as a sanity check before committing to the full recipe.
> 4. **Use prime-rl evals for AICP backend benchmarking** — the `eval` entrypoint supports any verifiers environment; define a benchmark suite, point at AICP's backends, get standardized comparison.
> 5. **Combined verifiers + prime-rl + RLMEnv recipe**: define an RLMEnv-compatible long-context task using verifiers, run prime-rl SFT on trajectories from that environment, evaluate. This is the full open-source RLM training pipeline.

## Relationships

- BUILDS ON: [[src-prime-intellect-verifiers-llm-rl-environments|Synthesis — Prime Intellect Verifiers]] (verifiers + prime-rl are the two halves of the same training stack)
- BUILDS ON: [[src-rlm-paper-deep-dive-table-1-training-recipe-six-observations|Synthesis — RLM Paper Deep Dive]] (prime-rl is the named training library for RLM-Qwen3-8B)
- DEMONSTRATES: [[infrastructure-over-instructions-for-process-enforcement|Principle 1]] (mandatory `uv run` enforces venv-only execution; pre-commit hooks enforce style)
- DEMONSTRATES: [[right-process-for-right-context-the-goldilocks-imperative|Principle 3 — Goldilocks]] (basic 1-8 GPU tier vs advanced 32-2048 GPU tier; per-env config overrides)
- FEEDS INTO: [[ai-infrastructure-decision-framework-2026|AI Infrastructure Decision Framework 2026]] (open-source Prime Intellect training tier)
- FEEDS INTO: [[2026-consumer-hardware-ai-stack|2026 Consumer Hardware AI Stack]] (consumer GPU support enables tier-0 training experiments)
- FEEDS INTO: [[ai-model-provider-harness-decision-matrix-2026|AI Model Provider Harness Decision Matrix 2026]] (INTELLECT-3 / INTELLECT-3.1 are Prime Intellect's own model entries)
- RELATES TO: [[model-local-ai|Model — Local AI ($0 Target)]] (the open-source training path for the local AI tier)

## Backlinks

[[Synthesis — Prime Intellect Verifiers]]
[[Synthesis — RLM Paper Deep Dive]]
[[infrastructure-over-instructions-for-process-enforcement|Principle 1]]
[[right-process-for-right-context-the-goldilocks-imperative|Principle 3 — Goldilocks]]
[[ai-infrastructure-decision-framework-2026|AI Infrastructure Decision Framework 2026]]
[[2026 Consumer Hardware AI Stack]]
[[AI Model Provider Harness Decision Matrix 2026]]
[[model-local-ai|Model — Local AI ($0 Target)]]
