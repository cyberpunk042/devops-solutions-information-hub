---
title: "Synthesis — How To Train Your GPT (Raiyan Yahya): 12-Chapter Pedagogical Guide to Building a LLaMA-3-Style 124M GPT From Scratch"
aliases:
  - "How to Train Your GPT Synthesis"
  - "Raiyan Yahya GPT Training Guide"
  - "LLaMA-3-Style GPT Pedagogy"
  - "GPT Training Tutorial Repo"
type: source-synthesis
domain: wiki-methodology
status: synthesized
confidence: high
maturity: seed
layer: 1
created: 2026-05-04
updated: 2026-05-04
last_reviewed: 2026-05-04
sources:
  - id: github-repo
    type: documentation
    url: https://github.com/raiyanyahya/how-to-train-your-gpt
    file: raw/articles/raiyanyahyahow-to-train-your-gpt.md
    description: "Open-source 12-chapter, 3,671-line interactive textbook teaching how to build, train, and run a modern decoder-only Transformer (LLaMA-3 style) from absolute scratch — annotated to Python-developer-with-zero-ML-experience level"
tags: [synthesis, pedagogy, gpt-training, llama3, transformer-architecture, rope, rmsnorm, swiglu, pre-norm, adamw, bpe, weight-tying, mixed-precision, kv-cache, education, tutorial, mission-2026-05-04, custom-model-prerequisite]
---

# Synthesis — How To Train Your GPT (Raiyan Yahya): Pedagogical Substrate for the Custom-Model Mission

## Summary

Raiyan Yahya's open-source repository **"How To Train Your GPT"** is a **12-chapter, 3,671-line interactive textbook** that teaches how to build, train, and run a modern decoder-only Transformer (the same family as ChatGPT, Claude, LLaMA, Mistral) **from absolute scratch with zero ML prerequisites**. The pedagogy is explicit: every line annotated with WHAT and WHY; LLaMA-3-class architecture (RoPE + RMSNorm + SwiGLU + pre-norm); production training techniques (AdamW + cosine warmup + mixed precision + gradient accumulation); production inference techniques (KV cache + temperature + top-k/p + beam search). The 12 chapters: 0-Overview · 1-Setup · 2-Tokenization (BPE) · 3-Embeddings · 4-Positional Encoding (RoPE) · 5-Attention (THE CORE) · 6-Transformer Block · 7-Complete GPT Model (124M) · 8-Training Pipeline · 9-Inference · 10-Full Script · 11-Glossary. Each chapter includes the 4-step structure: analogy (5-year-old level) + worked example with real numbers + annotated code (every line: what + why) + diagram. **Mission relevance**: this is the **pedagogical substrate** that operator referenced via *"Its not as if I was mastering AI model creation yet... nor will I maybe but possibly my own customizations and possibly even more useful and flexible. like we teach."* — the wiki's spec-driven convergence applied to model-creation by an outside practitioner. The repo is also a candidate **constitution input** for the [Custom-Tailored Model Group's M001](../../backlog/epics/pre-milestone/custom-tailored-senior-engineer-tier-model-group-with-recreated-intelligence-layer-2026-05.md) data-discipline phase: the operator's senior-engineer-tier instruction data + preference data needs to teach the agent *how to reason about model architecture properly* at the same level Yahya teaches humans. **Operator caveat acknowledged**: full training of a 124M GPT from scratch (~2 hours on RTX 4090 per the repo) is NOT operator's mission path — operator's path is fine-tuning open-weight bases via LoRA + DPO/IPO. But this repo is the **understanding substrate** for choosing fine-tune vs full-training, picking a base, designing the training data, and authoring the constitution.

## Reference

> [!info] Source identity
>
> | Field | Value |
> |---|---|
> | **Repo** | github.com/raiyanyahya/how-to-train-your-gpt |
> | **Author** | Raiyan Yahya |
> | **Author posture** | *"I made this with the goal of learning something I didn't understand completely. Specifically the attention part. I use AI a lot to understand key concepts and verifying them."* |
> | **Scope** | 12 chapters · 3,671 lines · 100% commented |
> | **Architecture** | LLaMA-3-style (RoPE + RMSNorm + SwiGLU + pre-norm) |
> | **Target model size** | 124M parameters; ~2 hours on RTX 4090 per repo's stated expected output |
> | **Prerequisites** | Python basics only — no ML, no calculus, no linear algebra required |

## Key Insights

> [!success] **LLaMA-3-style architecture is the candidate baseline for operator's customizations.**
>
> The repo implements the **publicly-documented** modern decoder-only Transformer:
>
> | Technique | Source family | Why it matters for operator's customizations |
> |---|---|---|
> | **RoPE** (rotary position embedding) | LLaMA, Mistral, Qwen | Relative position without learned parameters; works for any context length without re-training the position layer |
> | **RMSNorm** (root mean square layer norm) | LLaMA, Mistral, Gemma | 15% faster than LayerNorm, equally effective; trivial replacement for stability and speed |
> | **SwiGLU** (swish-gated linear unit) | PaLM, LLaMA, Gemini | Learns which information to pass or block; gating mechanism beats ReLU/GeLU on most tasks |
> | **Pre-Norm** | GPT-3 onward | Stable training at 100+ layers; mandatory for modern depth |
> | **AdamW** | GPT-3+ | Better generalization than vanilla Adam; modern standard |
> | **BPE** (Byte Pair Encoding) | GPT-2/3/4 | Handles any text including unseen words and emoji; tokenization-drift concern (per [[src-tokenization-drift-and-automated-prompt-optimization-marktechpost\|Tokenization Drift Synthesis]]) applies |
> | **Weight Tying** | GPT-2/3 | Saves 30% parameters and improves training signal |
> | **Mixed Precision** (bf16/fp16) | All production LLMs | 2× speed, half memory, same quality |
>
> **Operator's path**: do NOT re-implement these; pick an open-weight base (Qwen3.6-27B / RLM-Qwen3-8B / Qwen3-Coder / Llama 3 / Mistral) that already implements them, fine-tune via LoRA over operator-curated preference data + behavioral constitution. The repo is the **understanding substrate** for that base-choice decision, not the implementation path.

> [!success] **The pedagogy IS the spec-driven convergence applied to model authoring.**
>
> Per [[spec-driven-agentic-build-is-the-2026-convergent-pattern-prompts-are-first-class-artifacts|Spec-Driven Agentic Build Convergence Lesson]]: structured artifacts authored before any code; verification checklist per chapter; progress tracking per chapter; closed-loop sync ("if you find a bug, a typo, or something unclear in the code or the chapters" → fix the chapter first, then the code). Yahya's repo IS this pattern applied to a model-training tutorial:
>
> | Spec-driven element | How Yahya's repo instantiates it |
> |---|---|
> | Specs as version-controlled artifacts | 12 chapters in `chapters/`; each is a Markdown spec with embedded code |
> | Verification checklist per spec | Each chapter's "What You'll Build" + "Skills You'll Gain" sections |
> | Closed-loop sync | Contributing guide explicitly says fix chapter first, then code |
> | Three core skills (abstraction-first / alignment / iterative review) | "4-step structure: analogy → worked example → annotated code → diagram" — abstraction-first explicitly |
> | Wiki self-application | Yahya names the antithesis: ML tutorials that are "Too Shallow" or "Too Academic" — the convergent pattern's value proposition is the same |
>
> **Implication**: the convergence lesson's 9th instance (the wiki itself + the model-creation workflow) gains a 10th: an outside practitioner instantiating the same pattern for ML pedagogy. The convergence is robust.

> [!success] **Operator-tier instruction data should target this depth — Yahya's "5-year-old analogies → full working code" is the gold standard for senior-engineer-tier explanations.**
>
> Operator's [Custom-Tailored Model Group Concept](../../domains/cross-domain/custom-tailored-senior-engineer-tier-model-group-with-recreated-intelligence-layer-research-synthesis.md): *"adapted to a real senior software engineer instead of a newbe."* But the operator's senior-engineer-tier model SHOULD be able to TEACH like a senior — meaning explain concepts at any level on demand. Yahya's pattern (5-year-old analogy → variance argument behind `1/√d_k` → annotated code) is the depth-of-understanding signal an operator-tier model should match. **Direct application to M001 instruction data**: include teaching-progression examples (analogy → worked numbers → code → why-each-decision-was-made) in the instruction-data corpus. Yahya's chapter format is a candidate template.

> [!info] **Not a full-training path for operator — fine-tune is the realistic path.**
>
> Honest reading of repo: full training of a 124M GPT from scratch on RTX 4090 takes ~2 hours but consumes 50,000 training steps with ~45,000 tokens/sec. **Operator's mission is fine-tuning open-weight 8B-27B+ bases via LoRA**, not training from scratch. The repo's value to operator is conceptual (understand what's happening at each layer) and architectural (recognize when a base model is well-built), not directly executable.

> [!info] **The repo's "Next Steps After Finishing" table doubles as a roadmap for operator's M002 → M005 phases.**
>
> | Yahya's "Next Step" | Operator-Mission mapping |
> |---|---|
> | Bigger model (`num_layers` 12 → 24) | M002 — pick a 27B+ base for the senior-engineer-tier specialist |
> | More data (BookCorpus, C4, The Pile) | M001 — operator-curated wiki + sister-projects + raw/notes corpus |
> | Flash Attention | Already shipped in Qwen3.6-27B + RLM-Qwen3-8B + LFM 2; sparse-attention candidate per [[src-subquadratic-subq-12m-context-sparse-attention-and-anythingllm-breakthrough-leads\|SubQuadratic synthesis]] |
> | Grouped Query Attention | Already shipped in modern bases including LFM 2 |
> | **LoRA fine-tuning** | **M002 — the operator's actual training mechanism** |
> | **RLHF / DPO** | **M004 — behavioral preference fine-tune; the highest-leverage module** |
> | KV Cache | Already shipped; relevant for trust-layer L2 (compressed KV cache per [Trust-Layer Concept](../../domains/cross-domain/secure-tamper-proof-model-on-shared-gpu-research-synthesis.md)) |
> | Mixture of Experts | M002/M003 — Mixture-of-LoRAs over MoE base per [RecursiveMAS Synthesis](../tools-integration/src-recursivemas-recursive-multi-agent-systems-stanford-2026.md) |

## Deep Analysis

### Connection to Custom-Tailored Model Group Mission (operator-relevant)

Operator's *"Its not as if I was mastering AI model creation yet."* — Yahya's repo is **the literal substrate that closes the model-creation knowledge gap** at the depth the operator needs without becoming a foundation-model researcher. The repo's positioning is: "Python developer with zero ML experience." Operator-fit: senior-engineer-tier Python developer with deep DevOps + integration experience but emerging-ML — exactly the audience.

**Reading-order recommendation for the operator's pre-4090 study window**:

1. **Chapter 0-1** (Overview + Setup) — orient + verify GPU + venv
2. **Chapter 5** (Attention — THE CORE, 713 lines) — the center of gravity for understanding what fine-tuning actually changes
3. **Chapter 8** (Training Pipeline) — read this BEFORE picking DPO/IPO; understand the loss/gradient mechanism so the preference-fine-tune choices in M004 are informed
4. **Chapter 9** (Inference) — KV cache + temperature + top-k/p; matters for the recreated intelligence layer at I/O boundaries (M003)
5. **Chapter 11** (Glossary) — architecture provenance table; operator-decision input for picking the base in M002

This is ~50% of the repo (~1,800 lines) and covers the operator's mission-critical knowledge. Chapters 2/3/4/6/7/10 can be deferred or skimmed.

### Connection to Spec-Driven Convergence (10th instance proposal)

The 8-instance Convergence Lesson lists Fowler SPDD · Six-File · BMAD · OpenSpec · Spec-Kit · AI-DLC · Karpathy · Cavekit. The wiki self-application = 9th instance (recursive). **Yahya's repo proposal as 10th instance**: ML pedagogy as spec-driven artifact authoring. Each chapter is a structured Markdown spec; each chapter has a verification checklist (skills gained); each chapter follows closed-loop sync (fix chapter first, then code per CONTRIBUTING.md). The convergence holds at one more independent practitioner, in one more domain (ML pedagogy), at one more scale (solo educator). **Operator-decision**: add to convergence lesson as Evidence 10 OR keep as related-but-not-counted (the convergence lesson focuses on production-build patterns; Yahya's repo is teaching-focused). Default proposal: register as related-but-not-counted in the lesson; capture in this synthesis only.

### Connection to Trust + Compression Layers

The repo doesn't address compression or trust directly — that's outside its 12-chapter scope. **Operator's compose forward path**: take Yahya's understanding of the architecture (especially attention + KV cache from chapters 5 + 9), apply [Trust-Layer Concept](../../domains/cross-domain/secure-tamper-proof-model-on-shared-gpu-research-synthesis.md) compression+cypher to the trained weights at L2, run inference via [RLM substrate](../tools-integration/src-rlm-recursive-language-models-mit-oasys.md). The repo is the *first link* of the chain (architectural understanding); the trust-layer + RLM are *later links* (deployment).

## Open Questions

> [!question] Should the operator allocate a study window to this repo before RTX 4090 arrives?
> Operator-decision. ~50% of the repo (Chapters 0/1/5/8/9/11) covers the mission-critical knowledge for picking M002 base, designing M004 preference fine-tune, and architecting M003 intelligence layer. Estimated reading time: 6–10 hours. High-leverage if operator wants to author the constitution and preference data with strong understanding of the substrate.

> [!question] Is the LLaMA-3-style architecture the right baseline for operator's specialist LoRA?
> Yes for most candidate bases (Qwen3.6-27B is LLaMA-3-style; Llama 3 is by definition; Mistral is similar). LFM 2 is HYBRID (gated short-conv + GQA, NOT pure attention) — different architecture, may need separate study.

> [!question] Does Yahya's repo become a sister-project or stay as a wiki-source-synthesis?
> Operator-decision. Sister-project framing would mean adding to `sister-projects.yaml`; that's heavier. Source-synthesis framing (this artifact) keeps it as referenceable knowledge without integration overhead. Default: source-synthesis; revisit if operator forks the repo for own training experiments.

> [!question] Should the operator's M001 data discipline include Yahya-style teaching examples?
> Yes — operator-tier model that can TEACH at the depth Yahya does is structurally a stronger model than one that can only DO. Add 5-10% teaching-progression examples to instruction data per M001.

## Relationships

- BUILDS ON: [[custom-tailored-senior-engineer-tier-model-group-with-recreated-intelligence-layer-research-synthesis|Custom-Tailored Model Group Concept]] — pedagogical substrate for operator's pre-4090 knowledge prep; informs M001/M002/M004 design
- BUILDS ON: [[spec-driven-agentic-build-is-the-2026-convergent-pattern-prompts-are-first-class-artifacts|Spec-Driven Convergence Lesson]] — 10th-instance candidate (operator-decision); structurally instantiates the convergent pattern for ML pedagogy
- RELATES TO: [[src-tokenization-drift-and-automated-prompt-optimization-marktechpost|Tokenization Drift Synthesis]] — Chapter 2 (Tokenization) is the architectural prerequisite for understanding tokenization drift
- RELATES TO: [[src-unsloth-fast-lora-consumer-hardware|Unsloth Synthesis]] — operator's actual training mechanism; understanding LoRA is downstream of understanding the architecture Yahya teaches
- RELATES TO: [[src-rlm-recursive-language-models-mit-oasys|RLM Synthesis]] — RLM extends the standard `llm.completion` substrate; understanding the standard via Yahya is prerequisite to understanding the recursive extension
- RELATES TO: [[secure-tamper-proof-model-on-shared-gpu-research-synthesis|Trust-Layer Concept]] — compression + cypher composes with the architecture Yahya teaches; first-link / later-link relationship
- RELATES TO: [[src-prime-intellect-prime-rl-async-rl-training-at-scale|prime-rl Synthesis]] — Chapter 8 (Training Pipeline) is prerequisite for understanding RL training framework
- DEMONSTRATES: [[structured-context-governs-agent-behavior-more-than-content|Principle 2 — Structured Context Governs Agent Behavior]] — annotated-code-with-WHY-comments programs reader behavior more reliably than prose explanations
- DEMONSTRATES: [[the-agent-must-practice-what-it-documents|The Agent Must Practice What It Documents]] — Yahya practices what he documents (his own learning journey produced the artifact)

## Backlinks

[[custom-tailored-senior-engineer-tier-model-group-with-recreated-intelligence-layer-research-synthesis|Custom-Tailored Model Group Concept]]
[[Spec-Driven Convergence Lesson]]
[[src-tokenization-drift-and-automated-prompt-optimization-marktechpost|Tokenization Drift Synthesis]]
[[Unsloth Synthesis]]
[[RLM Synthesis]]
[[Trust-Layer Concept]]
[[prime-rl Synthesis]]
[[structured-context-governs-agent-behavior-more-than-content|Principle 2 — Structured Context Governs Agent Behavior]]
[[the-agent-must-practice-what-it-documents|The Agent Must Practice What It Documents]]
