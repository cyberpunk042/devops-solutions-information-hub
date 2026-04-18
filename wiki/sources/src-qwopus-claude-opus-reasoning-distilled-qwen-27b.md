---
title: "Synthesis — Qwopus — Claude Opus 4.6 Reasoning Distilled into Local Qwen 27B"
aliases:
  - "Synthesis — Qwopus — Claude Opus 4.6 Reasoning Distilled into Local Qwen 27B"
type: source-synthesis
domain: ai-models
layer: 1
status: synthesized
confidence: high
maturity: growing
created: 2026-04-15
updated: 2026-04-15
sources:
  - id: decrypt-article
    type: article
    url: https://decrypt.co/364047/want-claude-opus-ai-potato-pc-next-best-bet
    file: raw/articles/want-claude-opus-ai-on-your-potato-pc-this-is-your-next-best-bet-decrypt.md
    title: "Want Claude Opus AI on Your Potato PC? This Is Your Next-Best Bet"
    ingested: 2026-04-15
  - id: huggingface-model-card
    type: article
    url: https://huggingface.co/Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled
    file: raw/articles/jackrongqwen35-27b-claude-46-opus-reasoning-distilled-hugging-face.md
    title: "Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled · Hugging Face"
    ingested: 2026-04-15
  - id: huggingface-qwopus-v3-gguf
    type: article
    url: https://huggingface.co/Jackrong/Qwopus3.5-27B-v3-GGUF
    file: raw/articles/jackrongqwopus35-27b-v3-gguf-hugging-face.md
    title: "Jackrong/Qwopus3.5-27B-v3-GGUF · Hugging Face"
    ingested: 2026-04-17
tags: [distillation, local-ai, qwen, claude-opus, reasoning, gguf, consumer-hardware, aicp, zero-cost, structural-alignment]
---

# Synthesis — Qwopus — Claude Opus 4.6 Reasoning Distilled into Local Qwen 27B

## Summary

Developer **Jackrong** took the Qwen3.5-27B open-source model from Alibaba and fine-tuned it on Claude Opus 4.6 chain-of-thought reasoning traces, producing a family of models (Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled → Qwopus3.5-27B-v3) that run on a single consumer GPU and approximate Opus-style step-by-step reasoning. The v3 release uses "structural alignment" (training the model to reason faithfully step-by-step rather than imitate surface patterns) plus explicit tool-calling reinforcement for agent workflows. The model family has crossed one million downloads. Reported: 95.73% on HumanEval under strict evaluation; coding output beat Google's Gemma 4 (41B params) despite being 27B. This is directly relevant to the wiki's $0-inference goal ([[model-local-ai|Model — Local AI]]), AICP Stage 3 routing strategy, and reinforces the [[if-you-can-verify-you-converge|If You Can Verify, You Converge]] lesson already in `01_drafts/`: when reasoning style transfers with structure preserved, parameter count matters less than training methodology.

## Source Reference

> [!info] Source cards
>
> | Source | Type | Key Focus |
> |--------|------|-----------|
> | [Decrypt article (2026-04-12)](https://decrypt.co/364047/want-claude-opus-ai-potato-pc-next-best-bet) | News + hands-on testing | Narrative + empirical tests (creative writing, coding, sensitive topics) |
> | [Hugging Face model card](https://huggingface.co/Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled) | Official release | Model weights, chat template, training notebook reference |

## Key Insights

### 1. Distillation as Reasoning Transfer, Not Output Mimicry

The v1 release (Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled) learned to match Opus's *output patterns*. The v3 release (Qwopus3.5-27B-v3) shifted approach to **structural alignment** — training the model to reproduce the step-by-step reasoning structure rather than the surface text. This is a different training objective: teach the student to *think like* the teacher, not just *write like* the teacher. Practical consequence: v3 can run autonomously for minutes without stalling, supports native tool-calling, and preserves "full thinking mode" that agentic frameworks (Claude Code, OpenCode) expect.

This distinction maps directly to the wiki's **framework-vs-instance** principle. Surface imitation = copying an instance. Structural alignment = learning the framework. The same error mode the wiki documents for agents ("overfitting to one concrete implementation") has a direct analog in model distillation.

### 2. Consumer Hardware Budget Is Real, Not Aspirational

Reported runtime: 27B-parameter model on Apple MacBook with 32GB unified memory. GGUF format via LM Studio or llama.cpp. Smaller variants down to 4B for weaker hardware. Separate Vision multimodal variant. The path to $0 inference is no longer theoretical — it's a 1M-download reality for this model family alone. For [[model-local-ai|Model — Local AI]], this changes the Stage 3 timeline: routing (local-for-simple, cloud-for-complex) has a concrete ≥27B reasoning-capable local model that plugs into LM Studio today.

### 3. The Training Pipeline Is Fully Reproducible

Jackrong published the full training notebook, codebase, and a PDF guide on GitHub. The pipeline: Qwen base → Unsloth framework → LoRA adapters → response-only fine-tuning → export to GGUF. "Anyone with a Colab account can reproduce the whole pipeline from scratch." This is a critical shift in the local-AI ecosystem — reasoning distillation is no longer gated behind FAANG-scale compute.

Implication for this wiki: when the operator's hardware upgrade lands (8GB → 19GB VRAM per memory `project_hardware_upgrade.md`), training distilled models on this wiki's own content becomes possible. The 320 curated pages + 2,095 relationships is a potential LoRA training corpus.

### 4. Benchmark Results Tied to Agent Workflows

Reported: 95.73% on HumanEval under strict evaluation. Hands-on tests from the Decrypt article:

| Test | Qwopus3.5-27B-v3 Result | Comparison |
|------|------------------------|-------------|
| Creative writing (dark sci-fi, 8K+ tokens) | Philosophical, coherent, strong imagery | On par with Claude Sonnet 4.5; below Opus 4.6 |
| Coding (build a game from scratch, 1 iteration + refine) | Working game, visual logic, collision, random levels | Beat Gemma 4 (41B params); beat Codestral, quantized Qwen3-Coder-Next |
| Sensitive topic (addiction counseling) | Declined cover story; provided FMLA/ADA/SAMHSA resources | Nuanced reasoning, not flat refusal |

The coding result is the key data point: **27B beat 41B when the 27B was reasoning-distilled**. Same pattern as HRM/TRM (27M model beating GPT-5 on ARC-AGI, in [[src-hrm-trm-tiny-recursion-models|src-hrm-trm]]) and AutoBE (Qwen 25× cheaper than GPT-4 with equivalent output when verification loops exist, in [[src-autobe-compiler-verified-backend-generation|src-autobe]]). Three independent data points now converge on: **training methodology dominates parameter count for structured reasoning tasks**.

### 5. Censorship and Alignment Preserved From Base Model

Qwopus maintains Qwen's original alignment constraints by default. The Decrypt article notes this can be bypassed via jailbreak or abliteration for users who need it — standard open-source behavior. The interesting observation: distillation *added* reasoning capability without *removing* alignment. The teacher (Opus 4.6) is more permissive on nuance than the student (Qwen base), yet the student retained its base alignment. This tells us: reasoning structure transfers; refusal behavior doesn't necessarily follow the teacher.

### 6. Long Reasoning Window Is the Trade-off

The Decrypt tester ran the creative writing test on M1 Mac: **6 minutes reasoning before writing a single word, then 6 more minutes writing**. For coding tasks this is acceptable (correctness > latency). For interactive chat it's friction. Qwopus is a *thinking* model, not a *responsive* model. Right use case: long coding sessions, complex analytical tasks, multi-turn agent workflows with tool-call waits. Not quick Q&A.

Matches the wiki's **Goldilocks principle**: right tool for right context. Qwopus at Tier 2-3 agent tasks where reasoning visibility matters. For Tier 1 (simple Q&A, formatting), a faster/smaller model is right. This is evidence for **routed local inference** (AICP's Stage 3 strategy) — not a single model but a routed portfolio.

### 7. Ecosystem Integration Points

The Decrypt article explicitly names **Claude Code and OpenCode** as tested agentic frameworks Qwopus plugs into without patches. This matters for our ecosystem:

- **AICP** (sister project, local inference routing) — Qwopus is a candidate Tier 2-3 local model for complex reasoning tasks. Stage 3 roadmap gains a concrete model.
- **OpenFleet** (sister project, agent workforce) — fleet agents that currently route to Claude for complex work could route to Qwopus for sensitive/offline tasks.
- **Claude Code / this wiki** — Qwopus preserves full thinking mode and developer role that Claude Code skills + tool calls expect. Drop-in tier candidate.
- **OpenClaw** (5th-project AI assistant layer) — Decrypt explicitly mentions "good model for OpenClaw enthusiasts."

### 8. Quantified Adoption

**1M+ downloads** across Jackrong's model family. This is not a research curiosity — it's ecosystem reality. When a reasoning-distilled 27B model hits seven-figure downloads, any project considering "should we plan for local inference?" finds the answer has already arrived.

## Cross-Reference Integration

### Convergent Evidence (strengthens existing pages)

| Existing Page | How Qwopus Reinforces It |
|---------------|--------------------------|
| [[if-you-can-verify-you-converge\|Lesson — If You Can Verify, You Converge]] (in `01_drafts/`) | Adds a fourth independent data point (AutoBE + HRM/TRM + our pipeline + Qwopus). Structural alignment = verification applied to reasoning structure, not output. Strengthens promotion case. |
| [[model-local-ai\|Model — Local AI ($0 Target)]] | Concrete 27B model on consumer GPU with tool-call + thinking mode intact. Changes Stage 3 from "future" to "available now." |
| [[src-hrm-trm-tiny-recursion-models\|Synthesis — HRM/TRM]] | Same pattern (small beat big via training methodology). Two order-of-magnitude different scales (27M vs 27B) converging on the same principle is striking. |
| [[src-autobe-compiler-verified-backend-generation\|Synthesis — AutoBE]] | Qwen 25× cheaper equivalent output; Qwopus 27B beats Gemma 4 41B. Both built on Qwen base. Both validate training-matters-more-than-size. |
| [[four-project-ecosystem\|Four-Project Ecosystem]] | AICP Stage 3 roadmap gets a concrete Tier 2-3 model candidate. |

### Contradictions / Tensions

None observed. Qwopus is consistent with every convergent insight the wiki has previously captured about local inference and distillation.

## v3 GGUF Quantization Detail (NEW 2026-04-17)

The Qwopus3.5-27B-v3-GGUF repository provides a full quantization spectrum — this is the operationally-useful data for deployment decisions.

> [!abstract] Quantization variants and VRAM fit on common hardware
>
> | Quantization | File size | Effective VRAM need | Quality vs BF16 | Fits 8 GB? | Fits 19 GB? | Fits 24 GB? |
> |--------------|-----------|---------------------|-----------------|-------------|-------------|-------------|
> | Q2_K | 10.7 GB | ~11 GB | Limited | No | **Yes (headroom)** | Yes |
> | Q3_K_S | 12.1 GB | ~13 GB | Mobile-grade | No | **Yes** | Yes |
> | Q3_K_M | 13.3 GB | ~14 GB | Balanced compression | No | **Yes (recommended safer default)** | Yes |
> | Q3_K_L | 14.3 GB | ~15 GB | Better than Q3_K | No | **Yes** | Yes |
> | Q4_K_S | 15.6 GB | ~17 GB | Good balance | No | **Yes (tight)** | Yes |
> | **Q4_K_M** | **16.5 GB** | **~17-18 GB** | **High quality (popular choice)** | No | **Yes (sweet spot — ~1-2 GB context headroom)** | Yes |
> | Q5_K_M | 19.2 GB | ~20-21 GB | High quality, minimal loss | No | **No (exceeds with context)** | Yes |
> | Q6_K | 22.1 GB | ~23-24 GB | Near-original | No | No | Yes (tight) |
> | Q8_0 | 28.6 GB | ~29-30 GB | Minimal quantization | No | No | No (needs CPU offload) |
> | BF16 (full) | 53.8 GB | ~54-55 GB | Original precision | No | No | No |

**For a 19 GB VRAM machine: Q4_K_M is the sweet spot; Q3_K_M is the safe default with extra context room. Q5_K_M does NOT fit despite nominally being 19.2 GB — context overhead (1-3 GB) pushes it over the ceiling.**

### v2 → v3: Training Methodology Delta

The HF v3 model card makes the v2-vs-v3 distinction explicit:

| Aspect | v2 (Distillation) | v3 (Structural Alignment) |
|--------|-------------------|---------------------------|
| CoT source | Third-party distilled traces | Curated, verifiable reasoning chains |
| Learning target | Imitate teacher outputs | Learn process-level reasoning |
| Reasoning style | Compressed, potentially fabricated | Explicit, step-by-step, faithful |
| Robustness | Lower on unseen tasks | **Higher generalization** |
| CoT length | Shorter | **Slightly longer (more explicit steps)** |

v3 transitions from "answer imitation" to "process-level reasoning learning" with improved faithfulness and interpretability. This is the **structural alignment** mechanism that makes the model more reliable in autonomous agent loops.

### Clarified Benchmark — HumanEval 164-Task Full Benchmark

The earlier "95.73% HumanEval" number is the **plus-pass** score on strict evaluation — the harder version. The base-pass number is higher:

| Model | HumanEval base pass | HumanEval plus pass | Delta vs Qwen3.5 |
|-------|---------------------|---------------------|-------------------|
| **Qwopus3.5-27B-v3** | **97.56% (160/164)** | **95.73% (157/164)** | **+1.22 pp** over base |
| Qwen3.5-27B (base) | 95.73% (157/164) | 94.51% (155/164) | Baseline |
| Claude-Distilled-v2 | 95.12% (156/164) | 92.68% (152/164) | -1.83 pp vs base |

v3 also beats base Qwen3.5-27B on MMLU-Pro by ~4 points, and achieves comparable results with **fewer output tokens** (reasoning efficiency gain).

### Deployment Path Confirmed

Model card explicitly lists supported inference backends: **llama.cpp ✅ · LM Studio ✅ · Ollama ✅ · GPT4All ✅**. No proprietary inference provider. This is the full open consumer stack — zero-friction deployment on any machine with llama.cpp or a wrapper.

### Evaluation Framework Connection

This model is a **worked example** in [[open-model-evaluation-framework|Open-Model Evaluation Framework]] — all 5 evaluation stages (identify, size-and-fit, capability, deployment, routing-slot) are demonstrated against Qwopus v3 in that page. For future model announcements in the same tier (local-reasoning, 20-30B), apply the same framework.

## Deep Analysis

### What "Structural Alignment" Actually Means

Surface-pattern distillation teaches the student to reproduce the teacher's output style — sentence structure, punctuation, step headers. The student learns *how the teacher writes*. Structural alignment teaches the student to reproduce the teacher's reasoning DAG — the decision points, the rejected alternatives, the backtracking. The student learns *how the teacher thinks*.

The Decrypt article captured Qwopus's inner monologue on the creative writing task:

> "Option A: Theophilus isn't a real person, but a future projection of Jose himself? No, too cliché. Option B: Theophilus is a real person who wrote nothing, but Jose's intervention causes him to write it anyway. Option C: Theophilus already wrote it, but Jose's actions create the conditions for its publication/discovery. Best: Theophilus is a quiet monk who doesn't want to write anything..."

This is not imitating Opus's output — it's structural reasoning: enumerate options, evaluate each against criteria, reject candidates, arrive at the chosen path. The explicit tool-calling reinforcement in v3 extends this: tool calls become structural decision points ("evaluate: do I have enough information to proceed, or should I call a tool?") rather than string patterns.

### The 1M-Download Signal

Before Qwopus, distillation at scale was a lab activity. After 1M downloads, it's a consumer product category. Implications for any project choosing an AI strategy:

1. **Local inference is not a "future upgrade"** — it's a present alternative for reasoning-heavy workloads
2. **Training methodology is the new moat** — parameter count is less of a differentiator when anyone can distill
3. **Routing strategies matter more than model selection** — the right question is no longer "which model" but "which model for which task tier"
4. **Open-source models will converge on proprietary capabilities via distillation** — not via scale, but via trained reasoning structure

### Gap — Formal Evaluation Beyond Self-Reported Benchmarks

The Decrypt article is qualitative and the HF model card is marketing-adjacent. 95.73% HumanEval is self-reported. For wiki-level confidence, independent benchmarks across diverse task types would be needed. Research gap — candidate for future investigation, not a blocker for adopting Qwopus as a Stage 3 candidate.

## Relationships

- RELATES TO: [[model-local-ai|Model — Local AI ($0 Target)]]
- RELATES TO: [[src-hrm-trm-tiny-recursion-models|Synthesis — HRM/TRM — Tiny Recursion Models]]
- RELATES TO: [[src-autobe-compiler-verified-backend-generation|Synthesis — AutoBE — Compiler-Verified Backend Generation]]
- RELATES TO: [[src-gpt-oss-openai-open-weight-moe|Synthesis — gpt-oss]] (competing / complementary local-reasoning tier candidate)
- FEEDS INTO: [[if-you-can-verify-you-converge|Lesson — If You Can Verify, You Converge]]
- FEEDS INTO: [[open-model-evaluation-framework|Open-Model Evaluation Framework]] (worked example)
- RELATES TO: [[four-project-ecosystem|Four-Project Ecosystem]]
- RELATES TO: [[model-ecosystem|Model — Ecosystem Architecture]]

## Backlinks

[[model-local-ai|Model — Local AI ($0 Target)]]
[[src-hrm-trm-tiny-recursion-models|Synthesis — HRM/TRM — Tiny Recursion Models]]
[[src-autobe-compiler-verified-backend-generation|Synthesis — AutoBE — Compiler-Verified Backend Generation]]
[[Synthesis — gpt-oss]]
[[if-you-can-verify-you-converge|Lesson — If You Can Verify, You Converge]]
[[open-model-evaluation-framework|Open-Model Evaluation Framework]]
[[four-project-ecosystem|Four-Project Ecosystem]]
[[model-ecosystem|Model — Ecosystem Architecture]]
[[src-airllm-layer-wise-inference-nvme-ssd-offload|Synthesis — AirLLM: Layer-Wise Inference with NVMe SSD Offload]]
