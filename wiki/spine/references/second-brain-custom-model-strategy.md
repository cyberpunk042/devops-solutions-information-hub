---
title: "Second-Brain Custom Model — Training Strategy and Roadmap"
aliases:
  - "Second-Brain Custom Model — Training Strategy and Roadmap"
  - "Second-Brain Custom Model Strategy"
  - "Custom Model for the Second Brain"
type: reference
domain: cross-domain
layer: spine
status: synthesized
confidence: high
maturity: seed
created: 2026-04-18
updated: 2026-04-18
sources:
  - id: src-unsloth-fast-lora-consumer-hardware
    type: wiki
    file: wiki/sources/tools-integration/src-unsloth-fast-lora-consumer-hardware.md
    title: "Synthesis — Unsloth"
  - id: src-qwopus-claude-opus-reasoning-distilled-qwen-27b
    type: wiki
    file: wiki/sources/src-qwopus-claude-opus-reasoning-distilled-qwen-27b.md
    title: "Synthesis — Qwopus"
  - id: src-gpt-oss-openai-open-weight-moe
    type: wiki
    file: wiki/sources/tools-integration/src-gpt-oss-openai-open-weight-moe.md
    title: "Synthesis — gpt-oss"
  - id: 2026-consumer-hardware-ai-stack
    type: wiki
    file: wiki/spine/references/2026-consumer-hardware-ai-stack.md
    title: "2026 Consumer-Hardware AI Stack"
tags: [strategy, custom-model, fine-tuning, lora, second-brain, wiki-corpus, aicp, localai, cost-optimization]
---

# Second-Brain Custom Model — Training Strategy and Roadmap

## Summary

With the 2026 consumer-hardware AI stack in place (Unsloth training · gpt-oss / Qwen / Qwopus bases · llama.cpp offload · AICP routing), **fine-tuning a model on the second brain's own corpus is a 1-hour-to-weekend-sized experiment, not a research-lab project**. This page is the exploration and design layer: what the custom second-brain model should do, which base models are candidates, how to prepare the wiki as training data, how to evaluate the result, and how to integrate it into the ecosystem (AICP routing, MCP server, gateway operations). It presents **5 candidate model approaches** with trade-offs rather than prescribing one — the operator picks based on priorities. All 5 are achievable with the operator's current 19 GB VRAM dual-GPU setup; only the 27B-distilled variant needs rented compute (~$5-20 Colab A100 one-time). The phased rollout starts with a 2-hour proof-of-concept (Qwen3.5-4B + 200-pair Data Recipe) and escalates to multi-adapter production deployment. The strategic frame: **each successful fine-tune extends the $0-target footprint by routing another task class locally**, and the wiki's own 377-page / 2500-relationship / 16-model / 22-standards corpus is the highest-density domain-specific training substrate in the ecosystem.

## Why a Custom Second-Brain Model

Generic open-weight models (gpt-oss-20b, Qwopus 27B, Qwen3.5) are competent at *general* methodology reasoning. They are NOT fluent in the second brain's specific vocabulary, principles, and patterns:

- "Structural Compliance Is Not Operational Compliance" (a named lesson in this wiki)
- The 4 principles with their exact framings
- The Gateway Output Contract's 5 rules
- The 10 knowledge-project verbs (aggregate → process → evaluate → learn → integrate → modelize → validate → standardize → teach → offer)
- Readiness-vs-progress distinction
- Goldilocks protocol (identity → profile)
- Consumer-Property Doctrine (stable / state / consumer-task orthogonality)

A generic model can be PROMPTED into using these frames via CLAUDE.md + structured context, but it does so inconsistently and expensively (many tokens per invocation). **A fine-tuned model internalizes the frames — fewer tokens per request, higher consistency, lower cost, $0 per invocation post-training.**

The operational implications are four:

1. **AICP routing expands** — a methodology-fluent local model becomes a new tier ("local-wiki-maintenance") that handles compliance checks, lesson scaffolding, relationship suggestions without cloud routing
2. **MCP tools get smarter** — `gateway query`, `gateway compliance`, `gateway evaluate-model` can invoke the custom model for local reasoning
3. **Sister projects get a shipping default** — OpenFleet / AICP / devops-control-plane consuming the wiki's methodology can bundle the fine-tune as their "methodology agent"
4. **The operator gets a second-brain sidekick** — a local model that knows this corpus fluently, for daily drafting / review / synthesis

## Candidate Matrix

Five approaches, from smallest/fastest to largest/most-capable. All are compatible with 19 GB VRAM except Candidate C (needs rented compute).

> [!info] **5 candidates × 6 dimensions**
>
> | # | Candidate | Base | Data | Training time (19GB VRAM) | Deployment | Best for |
> |---|-----------|------|------|---------------------------|------------|----------|
> | A | **Wiki-Assistant** | Qwen3.5-4B | Wiki Q&A pairs (Data Recipes) | 30-60 min | Ollama | First experiment, toolchain familiarity, routine queries |
> | B | **Wiki-Reasoner** | gpt-oss-20b | Wiki + ecosystem learnings | 3-6 hours | Ollama / llama.cpp | Substantive reasoning about methodology evolution |
> | C | **Wiki-Opus-Distilled** | Qwen3.5-27B | Opus 4.6 traces on methodology tasks | 8-24 hours (Colab A100 ~$5-20) | llama.cpp GGUF | Closest to Opus-grade methodology reasoning at $0 runtime |
> | D | **Wiki-Router** | Qwen3.5-0.5B or 1.5B | Task → routing-tier classification pairs | 15-30 min | Embedded in AICP | Fast local classification for AICP's complexity scorer |
> | E | **Base + Multi-LoRA** | Qwen3.5-4B or gpt-oss-20b | Multiple domain-specific LoRAs | 30-60 min per adapter | Ollama + adapter-swap | Long-term: task-specific adapters swapped per request |

### Candidate A — Wiki-Assistant (recommended starting point)

- **Base**: Qwen3.5-4B (fits with room to spare; free Colab T4 proven)
- **Purpose**: conversational assistant fluent in the 4 principles, 16 models, 22 standards. Answers "what does Principle 4 say?", drafts initial lesson scaffolds, suggests relationship links.
- **Data**: ~200-500 SFT pairs generated by Unsloth Data Recipe from the wiki corpus:
  - Question "What is Principle 4?" → full principle page summary as answer
  - "Given this evidence, which lesson does it strengthen?" → wiki lesson content
  - "Name the 10 knowledge-project verbs" → enumeration
- **Training**: LoRA rank=32, 3 epochs, Unsloth Studio
- **Output**: Ollama-deployable GGUF, ~2.5 GB on disk
- **Latency**: 30-60 tok/s on 19 GB VRAM
- **Integration**: AICP `local-wiki-maintenance` tier
- **Risk**: fine-tuning on declarative facts may not generalize beyond exact Q&A shape. Evaluation on held-out questions catches this.

### Candidate B — Wiki-Reasoner

- **Base**: gpt-oss-20b (fits in 19 GB with MXFP4 + headroom)
- **Purpose**: Substantive reasoning about methodology evolution, not just retrieval. Can propose "this pattern is a candidate for Principle 5 because..." with structured argument.
- **Data**: wiki corpus + ecosystem contributions (OpenArms corrections, OpenFleet lessons, AICP decisions, raw/notes directives) + CoT traces of methodology reasoning
- **Training**: LoRA rank=64, 2-3 epochs, reasoning-preservation via structural alignment (Qwopus v3 method)
- **Output**: gpt-oss-20b + adapter, ~12-14 GB on disk
- **Latency**: 15-30 tok/s at reasoning=high on 19 GB VRAM
- **Integration**: AICP `local-reasoning` tier
- **Risk**: harmony format compliance; reasoning-effort dial behavior may drift under heavy fine-tuning — monitor via held-out reasoning tasks

### Candidate C — Wiki-Opus-Distilled

- **Base**: Qwen3.5-27B
- **Purpose**: Opus-grade methodology reasoning running at $0 per invocation post-training. The Qwopus recipe applied to the wiki's specific domain.
- **Data**: Opus 4.6 traces on ~500-1000 methodology reasoning tasks (task: "Given this new lesson, which principle does it strengthen? Explain your reasoning with references"). Collected via API (~$5-10).
- **Training**: LoRA rank=64, structural alignment, 3-5 epochs. Needs Colab A100 (~$1/hour × 8-24h = $5-20).
- **Output**: Qwen3.5-27B + adapter, ~16 GB GGUF after merge + quantize
- **Latency**: 10-25 tok/s at Q4_K_M on 19 GB VRAM
- **Integration**: AICP `local-reasoning` tier as premium option
- **Risk**: highest cost/complexity; most capable outcome. Probably the "destination" if the POC succeeds and the intermediate candidates don't quite hit quality.

### Candidate D — Wiki-Router

- **Base**: Qwen3.5-0.5B or Qwen3.5-1.5B (whichever has better task-classification accuracy)
- **Purpose**: AICP's complexity scorer becomes a local model call instead of rule-based heuristics. Classifies incoming request → {simple, moderate, substantive, novel, architectural}.
- **Data**: 500-2000 labeled examples — synthetic (operator labels) + historical (replay past AICP routing decisions with manual review)
- **Training**: LoRA or full fine-tune (tiny models fine-tune quickly), 15-30 min
- **Output**: ~300 MB GGUF
- **Latency**: 100+ tok/s on 19 GB (barely uses the card)
- **Integration**: embedded in AICP complexity scorer, replaces rule-based thresholds
- **Risk**: labeled-data gap — needs operator time to curate the router training set. Could start small (100 examples) and grow.

### Candidate E — Base + Multi-LoRA

- **Base**: Qwen3.5-4B (most practical) OR gpt-oss-20b (more headroom)
- **Architecture**: one base model, several LoRA adapters swapped at inference time per task:
  - `methodology-assistant` — Candidate A's target
  - `router-classifier` — Candidate D's target
  - `lesson-scaffolder` — trained on "given X evidence, produce a lesson shape"
  - `relationship-suggester` — trained on "given this new page, suggest RELATES TO / BUILDS ON / FEEDS INTO"
  - `compliance-checker` — trained on "given this page, list violations of the 4 principles"
- **Data**: task-specific per adapter (100-500 pairs each)
- **Training**: 30-60 min per adapter (additive, can start with one and grow)
- **Output**: base model (2.5 GB) + N adapters (10-100 MB each)
- **Latency**: same as base; adapter swap is near-free
- **Integration**: AICP dispatches based on task class, loading the right adapter
- **Risk**: requires adapter-management infrastructure (inference-time swap); multiple evaluation sets (one per adapter). But long-term this is the architecture that scales with task diversity.

## 2026-04-22 Addendum — K2.6 Rewrites the Capability Budget for B and C

When this strategy was written (Stage 1 of consumer-hardware synthesis), the target for Candidates **B (Wiki-Reasoner)** and **C (Wiki-Opus-Distilled)** was *raw methodology-reasoning capability*. The path: train on Opus traces, arrive at something like Opus-grade reasoning, run it on 19 GB VRAM at $0 per invocation. Candidate C's cost (Colab A100 ~$5-20) and time (8-24 h) reflected that capability goal.

Five days later (2026-04-22), **[[src-kimi-k2-6-moonshot-agent-swarm|Kimi K2.6]] on OpenRouter gives you Opus-4.6-class agentic and coding capability for $0.80 / $3.50 per million tokens** — ~1/20th Anthropic pricing, MIT-licensed, with 256K context and native agentic-swarm orchestration. At operator's expected volume, *using* K2.6 via OpenRouter is effectively cheaper than *training* a custom distilled model — and arrives at strictly higher raw capability than any 27B distill can reach.

**2026-04-23 addendum:** K2.6 is also available via **Ollama Cloud Pro** at $20/month flat for all cloud models (`ollama launch claude --model kimi-k2.6:cloud`). Cost-effective for heavy prototyping (>5M output tokens/month breakeven vs OpenRouter) — but the privacy posture is explicitly "prototyping only" per the source article's own framing. The strategic argument below ("K2.6 obsoletes training-a-distill for raw capability") holds under either cloud path. See [[src-kimi-k2-6-moonshot-agent-swarm|K2.6 synthesis]] § Three access paths for which path to pick per workload.

**Reassessment of each candidate under the K2.6 reality:**

> [!info] **Candidate × K2.6 impact table**
>
> | Candidate | 2026-04-17 framing | 2026-04-22 reassessment |
> |---|---|---|
> | **A — Wiki-Assistant** | First experiment, toolchain fluency | **Still recommended — K2.6 does NOT replace this.** A local 4B methodology-fluent model is about *privacy, speed on tiny queries, offline capability*, not raw capability. |
> | **B — Wiki-Reasoner** | Substantive methodology reasoning at $0 runtime | **Deprioritize or reframe.** If the goal is raw reasoning quality, K2.6 via OpenRouter dominates strictly. Rescoped goal: "privacy-locked methodology reasoning" — narrow, defensible. Otherwise skip. |
> | **C — Wiki-Opus-Distilled** | Opus-grade reasoning at $0 per invocation | **Mostly obsoleted.** Training a 27B distill to approach Opus 4.6 quality when K2.6 surpasses Opus 4.6 on the relevant benchmarks for ~5% of Opus cost is a reversal of the economics. Keep only if the pressure is *fully offline* or *absolute data sovereignty for methodology decisions*. |
> | **D — Wiki-Router** | Fast local task classifier for AICP | **Strengthened.** K2.6 makes more routes valuable, which makes smart routing more valuable. Router quality now decides which queries get K2.6 premium-cheap vs truly-local vs Opus-fallback. Higher-leverage than before. |
> | **E — Base + Multi-LoRA** | Long-term scalable adapter library | **Strengthened.** Each adapter (scaffolder, relationship-suggester, compliance-checker) targets a *specific domain operation on the wiki corpus*, which K2.6 does NOT inherently know. Capability comes from K2.6; domain-knowledge shaping comes from the LoRAs. They compose rather than compete. |

**Strategic reshape of the phased rollout:**

- **Phase 0**: Unchanged — Ollama + Unsloth toolchain setup, Qwen3.5-4B download.
- **Phase 1 (Candidate A)**: Unchanged — still the first deployable artifact.
- **Phase 2 (Candidate D, promoted from Phase 3)**: Router becomes higher priority — it is the glue between tiers, and K2.6 makes the tiers more differentiated.
- **Phase 3 (Candidate E, promoted from Phase 4-5)**: Multi-LoRA domain adapters layered on top of K2.6 or a small base. This is the real long-term architecture.
- **Phase 4 (Candidate B — narrowed)**: Only if privacy/offline pressure demands it. Keep scoped to "methodology reasoning, offline only."
- **Phase 5 (Candidate C — deferred)**: Deferred or deprecated. Revisit only if K2.6 becomes unavailable or quality-regresses at a scale that matters.

**The deeper principle.** The custom-model strategy exists to *fill gaps in the commercial landscape*. When the commercial landscape shifts — as it did on 2026-04-20 with K2.6 — the gaps move. The strategy must follow. The candidates are *tools*, not *destinations*; their justification is the shape of the gap on the day we pick them up.

## Data Preparation Strategy

The wiki corpus as of 2026-04-18: 377 pages, 2500 relationships, 16 models, 22 standards, 44+ validated lessons, 19+ validated patterns, 17 decisions, 48+ source syntheses, 4 principles. All under consistent YAML frontmatter + Markdown structure.

### Stage 1 — Automated extraction (Unsloth Data Recipes)

Unsloth Studio's Data Recipe workflow converts folder-of-Markdown into SFT jsonl. Input: `wiki/` directory. Output: structured training pairs.

Expected yields by page type:
- **Principles** (4 pages) → Q/A on principle definition, application, boundaries — ~10 pairs each = ~40
- **Models** (16 pages, ~300 lines each) → Q/A on model structure, components, adoption — ~15 each = ~240
- **Standards** (22 pages) → Q/A on "what does good look like for X" — ~10 each = ~220
- **Lessons** (44 validated) → Q/A on lesson triggers and applicability — ~5 each = ~220
- **Patterns** (19 validated) → Q/A on when to apply / when not to — ~5 each = ~95
- **Source syntheses** (48+) → Q/A on key insights per source — ~3 each = ~144

**Rough total: ~960 automated pairs.** More than enough for Candidate A; usable as the base for B/C/E.

### Stage 2 — Manual curation (operator + Claude)

Automated pairs are shallow (what-is-X). Deep methodology reasoning requires hand-curated pairs:

- **Synthesis pairs** — given an external source, synthesize a key insight that fits the wiki's voice
- **Relationship pairs** — given a new page, identify which existing pages it BUILDS ON / RELATES TO / FEEDS INTO
- **Compliance pairs** — given a page, identify violations of the 4 principles + the consumer-property doctrine
- **Evolution pairs** — given evidence, propose whether a lesson should bump seed → growing → mature
- **Gap pairs** — given the current wiki state + a question, identify what the wiki DOESN'T yet cover

Target: 100-300 hand-curated pairs added to automated yield.

### Stage 3 — Cross-project signal

OpenFleet + AICP contributions have a specific shape (verify-before-contributing, confidence markers, evidence tables). Train the model to RECOGNIZE and GENERATE that shape:

- "Given this draft contribution, what's missing per the verify-before-contributing self-check?"
- "Is this claim schema-valid but factually unverified?"

This uses recent contributions (the 6 accepted + 3 inbox) as training evidence.

### Stage 4 — Evaluation holdout

Hold out ~50 pairs as test set. Never train on them. Use for:
- Accuracy on factual questions (principle names, standards, model components)
- Quality on reasoning tasks (judged by operator + Claude review)
- Tone/voice (does the output sound like wiki prose?)

## Evaluation Framework

Quality has three dimensions that need separate measurement:

| Dimension | What "good" looks like | Measurement |
|-----------|------------------------|-------------|
| **Factual accuracy** | Given "What is Principle 4?", answer matches the principle page's summary | Automated: string similarity + fact extraction; target >85% |
| **Reasoning quality** | Given "Does X strengthen lesson Y?", answer reasons through applicability + evidence with wiki-appropriate structure | Manual: operator scores 1-5 on sample of 20; target mean >3.5 |
| **Voice / structure** | Output uses callouts, tables, RELATES TO format, proper terminology | Manual + lint: does the output PASS `pipeline post` if saved as a wiki page? Target: >70% of generated scaffolds pass schema on first try |

Baseline comparisons:
- **gpt-oss-20b unprompted** vs **fine-tuned** on same test set
- **Claude Opus 4.6 with wiki as context** vs **fine-tuned** — does the fine-tune close the quality gap at $0?

If the fine-tune matches gpt-oss-20b-with-wiki-in-context at <30% the token cost per query, the experiment is a success. If it beats Opus-with-wiki-as-context on even a subset of tasks, it's a major win.

## Integration Points

Once a candidate is trained and deployed via Ollama:

### AICP routing
Register the model as a new backend. Complexity scorer adds a "wiki-maintenance" signal:
- Task involves wiki-methodology terms (principle, standard, pattern, lesson, structural, operational, goldilocks) → route to wiki-assistant
- Task is Q&A about the wiki → wiki-assistant
- Task is methodology synthesis → wiki-reasoner (Candidate B)
- Task is wiki compliance check → wiki-compliance-checker (Candidate E adapter)

### MCP server
Wrap the model as a new `wiki_local_reasoning` MCP tool. Sister projects calling the brain's MCP server can now get methodology reasoning without cloud routing.

### Gateway operations
- `gateway query` could fall back to local model when pattern-based queries miss
- `gateway compliance` could augment its structural checks with model-based semantic checks (does this page's Evidence section actually cite evidence?)
- `gateway evaluate-model` could run the framework using the local model's judgment

### MCP client from sister projects
OpenFleet / AICP / devops-control-plane — via their forwarders — could call the brain's local model for methodology consultation. No cloud dependency, no rate limit.

## Phased Rollout

> [!abstract] From first experiment to production deployment
>
> | Phase | Goal | Timeline | Deliverable |
> |-------|------|----------|-------------|
> | **0. Toolchain POC** | Install Unsloth, run one free Colab notebook end-to-end on any dataset | 2-3 hours | Confidence that the training tooling works on operator's hardware |
> | **1. Candidate A (Wiki-Assistant)** | Fine-tune Qwen3.5-4B on 200-pair Data Recipe output | 1 afternoon | First Ollama-deployable model that answers wiki questions |
> | **2. Evaluation loop** | Build 50-pair held-out test set; measure accuracy + reasoning + voice | 1-2 evenings | Quality baseline; decision point for whether to escalate |
> | **3a. Iterate A** | Add hand-curated pairs, retrain, remeasure | Days | Improved wiki-assistant |
> | **3b. OR escalate to B** | Fine-tune gpt-oss-20b on expanded dataset | 1 weekend | Wiki-reasoner for substantive tasks |
> | **4. AICP integration** | Register model as AICP backend; update complexity scorer thresholds | 1 weekend | Routing-operational local-wiki-maintenance tier |
> | **5. Multi-adapter (Candidate E)** | Train adapter #2 (router-classifier OR compliance-checker) | Per-adapter: 1 afternoon | Growing adapter library |
> | **6. Optional: Candidate C distillation** | Rent Colab A100, distill Opus traces onto Qwen3.5-27B | 1 weekend + $5-20 | Premium methodology reasoner for the expert tier |

**Suggested first step**: Phase 0 + Phase 1 back-to-back (one weekend = a working wiki-assistant). If the result is good, continue. If not, the fine-tune toolchain investment is reusable for whatever comes next.

## Risks and Mitigations

| Risk | Likelihood | Mitigation |
|------|------------|------------|
| Fine-tune overfits to Q&A shape; fails on real free-form questions | Medium | Hand-curated pairs with varied phrasing; hold-out test set with novel question forms |
| Training data too shallow (wiki is dense but answers-in-wiki are not all Q&A-shaped) | Medium | Stage-2 manual curation; Opus-traces in Candidate C |
| Model hallucinates wiki content (invents page names, patterns that don't exist) | High | Evaluation includes "does this wikilink resolve?" check. Train explicitly on "I don't know" responses for out-of-wiki questions |
| AICP routing integration turns out to be more complex than expected | Medium | Start with a separate Ollama endpoint + manual invocation before hard-wiring into AICP scorer |
| Model drifts when wiki evolves (new principles, new standards) | Guaranteed | Plan for quarterly retraining; automate the Data Recipe run + LoRA training + deployment |
| Principle 4 applied to this model itself — "it works" is a declaration until evaluation verifies | Certain | Evaluation framework above IS the verification gate. Don't declare "works" without it. |

## Cost Summary

| Approach | Training cost | Ongoing cost | Break-even vs cloud |
|----------|---------------|--------------|---------------------|
| A (Wiki-Assistant) | 1-3 hours electricity on 19 GB VRAM + ~0 $ | $0 per query | ~10 Opus queries |
| B (Wiki-Reasoner) | 3-6 hours electricity + ~0 $ | $0 per query | ~50 Opus queries |
| C (Opus-Distilled) | $5-20 one-time + 8-24 hours | $0 per query | ~200 Opus queries |
| D (Router) | 15-30 min + ~0 $ | $0 per query | <10 Opus queries |
| E (Multi-LoRA) | 30-60 min per adapter × N adapters | $0 per query | ~10 Opus queries per adapter |

Every candidate pays back within the first few dozen real queries. **Fine-tuning is an investment that immediately reduces cloud spend.**

## Connection to Four Principles

> [!abstract] How this strategy maps to the governing principles
>
> | Principle | Connection |
> |-----------|------------|
> | **1. Infrastructure > Instructions** | A fine-tune is infrastructure-level internalization. CLAUDE.md instructions are 25% compliance; a fine-tune baked into the weights is closer to the "100% compliance" end |
> | **2. Structured Context > Content** | Training pairs use structured format (question → answer with wiki structure); the fine-tune learns to PRODUCE structured output, not just consume it |
> | **3. Goldilocks** | Each candidate is right-sized for a different task class. Candidate A for routine queries, C for substantive reasoning. Don't fine-tune one model for all tasks |
> | **4. Declarations Aspirational Until Verified** | The whole evaluation framework is the "verify the declaration" layer. "The model works" isn't true until the eval set says so |

## Open Questions

> [!question] How much of the wiki's VOICE is learnable via LoRA vs how much needs full fine-tuning?
> Qwopus demonstrated reasoning-structure transfer via LoRA. Wiki voice includes specific terminology, callout conventions, Principle-4-style framing. LoRA rank=32-64 should capture this; empirical test needed.

> [!question] Should the second-brain model also CONTRIBUTE BACK to the wiki?
> A fine-tuned model could generate lesson scaffolds via `gateway contribute --target local --contributor "wiki-assistant-v1"`. The consumer-property doctrine already supports this — the model becomes a consumer with its own declared identity. Could extend the feedback loop dramatically.

> [!question] At what maturity threshold does a wiki-specific fine-tune become canonical?
> Current: seed (this page). Growing: first successful training run with meaningful eval gains. Mature: fine-tune is actively used by AICP routing. Canonical: fine-tune is part of wiki distribution (like CLAUDE.md — exported to sister projects).

> [!question] Could the fine-tune be deployed ALONGSIDE the wiki as a distribution artifact?
> When a consumer `setup --connect`s to the brain, could they also pull a pre-trained methodology-assistant GGUF? This would make the brain a two-part artifact: knowledge (pages) + reasoning layer (model) co-distributed.

## Key Pages

| Page | Role |
|------|------|
| [[src-unsloth-fast-lora-consumer-hardware\|Unsloth synthesis]] | The training mechanism |
| [[src-qwopus-claude-opus-reasoning-distilled-qwen-27b\|Qwopus]] | Precedent for reasoning-distillation on consumer hardware |
| [[src-gpt-oss-openai-open-weight-moe\|gpt-oss]] | Best candidate for Candidate B base |
| [[open-model-evaluation-framework\|Open-Model Evaluation Framework]] | How to evaluate which base model to pick |
| [[2026-consumer-hardware-ai-stack\|2026 Consumer-Hardware AI Stack]] | The strategic context this initiative sits in |
| [[model-local-ai\|Model — Local AI ($0 Target)]] | Where the fine-tune plugs into routing |
| [[aicp\|AICP]] | The orchestrator that will integrate the fine-tune |
| [[declarations-are-aspirational-until-infrastructure-verifies-them\|Principle 4]] | The evaluation framework IS the verification gate |

## How This Connects — Navigate From Here

> [!abstract] From This Strategy → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **Training mechanism** | [[src-unsloth-fast-lora-consumer-hardware\|Unsloth]] |
> | **Base model choices** | [[open-model-evaluation-framework\|Open-Model Evaluation Framework]] · [[src-gpt-oss-openai-open-weight-moe\|gpt-oss]] · [[src-qwopus-claude-opus-reasoning-distilled-qwen-27b\|Qwopus]] |
> | **Integration context** | [[model-local-ai\|Model — Local AI]] · [[aicp\|AICP]] |
> | **Governing principles** | [[declarations-are-aspirational-until-infrastructure-verifies-them\|Principle 4]] · [[super-model\|Super-Model]] |

## Relationships

- BUILDS ON: [[src-unsloth-fast-lora-consumer-hardware|Synthesis — Unsloth]]
- BUILDS ON: [[src-qwopus-claude-opus-reasoning-distilled-qwen-27b|Synthesis — Qwopus]]
- BUILDS ON: [[src-gpt-oss-openai-open-weight-moe|Synthesis — gpt-oss]]
- BUILDS ON: [[2026-consumer-hardware-ai-stack|2026 Consumer-Hardware AI Stack]]
- FEEDS INTO: [[model-local-ai|Model — Local AI ($0 Target)]]
- FEEDS INTO: [[aicp|AICP]]
- RELATES TO: [[open-model-evaluation-framework|Open-Model Evaluation Framework]]
- DEMONSTRATES: [[declarations-are-aspirational-until-infrastructure-verifies-them|Principle — Declarations Aspirational Until Verified]]

## Backlinks

[[Synthesis — Unsloth]]
[[Synthesis — Qwopus]]
[[Synthesis — gpt-oss]]
[[2026 Consumer-Hardware AI Stack]]
[[model-local-ai|Model — Local AI ($0 Target)]]
[[aicp|AICP]]
[[open-model-evaluation-framework|Open-Model Evaluation Framework]]
[[Principle — Declarations Aspirational Until Verified]]
