---
title: "Synthesis — OOLONG (Bertsch et al. Nov 2025) + LongBench Pro (Chen et al. Jan 2026): The Long-Context Benchmarks Anchoring the RLM Thread"
aliases:
  - "OOLONG Benchmark"
  - "LongBench Pro"
  - "OOLONG + LongBenchPro Synthesis"
type: source-synthesis
domain: tools-integration
status: synthesized
confidence: high
maturity: seed
created: 2026-04-27
updated: 2026-04-27
last_reviewed: 2026-04-27
sources:
  - id: oolong-paper
    type: paper
    url: https://arxiv.org/abs/2511.02817
    file: raw/articles/251102817-oolong-evaluating-long-context-reasoning-and-aggregation-capabilities.md
    title: "OOLONG: Evaluating Long Context Reasoning and Aggregation Capabilities (Bertsch et al., Nov 2025)"
    description: "CMU-affiliated benchmark used as the load-bearing eval in RLM paper Table 1; trec_coarse split scored 56.5% by RLM(GPT-5) vs 44.0% by base GPT-5"
    ingested: 2026-04-27
  - id: longbench-pro-paper
    type: paper
    url: https://arxiv.org/abs/2601.02872
    file: raw/articles/260102872-longbench-pro-a-more-realistic-and-comprehensive-bilingual-long-contex.md
    title: "LongBench Pro: A More Realistic and Comprehensive Bilingual Long-Context Evaluation Benchmark (Chen et al., Jan 2026)"
    description: "Source of 750 English tasks → 2250 candidate trajectories → 1072 filtered → SFT samples used to train RLM-Qwen3-8B"
    ingested: 2026-04-27
  - id: rlm-paper-deep-dive
    type: wiki
    file: wiki/sources/tools-integration/src-rlm-paper-deep-dive-table-1-training-recipe-six-observations.md
    description: "RLM paper deep-dive — uses OOLONG as eval (Table 1) and LongBenchPro as training data source"
  - id: rlm-empirical-findings
    type: wiki
    file: wiki/sources/tools-integration/src-rlm-empirical-findings-oolong-browsecomp-rlm-qwen3-8b.md
    description: "RLM empirical findings — OOLONG headline number (114% improvement at 132K)"
tags: [oolong, longbench-pro, long-context-benchmarks, evaluation, training-data, distributional-reasoning, aggregation, classification, counting, bilingual, english-chinese, cmu, real-world-data, synthetic-data, rlm-anchor, frontier-model-evaluation, mission-2026-04-27, paradigm-validation, anti-vendor-lock-in, tools-integration]
---

# Synthesis — OOLONG + LongBench Pro: Long-Context Benchmarks Anchoring the RLM Thread

## Summary

Two benchmarks load-bearing for the [RLM paper deep-dive](src-rlm-paper-deep-dive-table-1-training-recipe-six-observations.md): **OOLONG** (Bertsch, Pratapa, Mitamura, Neubig, Gormley — CMU; arXiv 2511.02817, submitted 4 Nov 2025) is the long-context reasoning + aggregation benchmark RLM uses as a primary evaluation surface; the `trec_coarse` split is where RLM(GPT-5-mini) outperformed base GPT-5 by ~114% raw-score increase per the RLM blogpost. **LongBench Pro** (Chen, Wu, Jia, Gao, Fu, Zhang, Hu; arXiv 2601.02872, submitted 6 Jan 2026) is the bilingual (English + Chinese) benchmark of 1,500 naturally-occurring long-context samples used as the *source domain* for RLM-Qwen3-8B's training trajectories — the paper sampled 750 English LongBenchPro tasks, generated 2,250 candidate trajectories with RLM(Qwen3-Coder-480B-A35B), filtered to 1,072, and decomposed per-turn for SFT. Together these two papers anchor RLM's *empirical claim chain*: trained on LongBenchPro, evaluated on OOLONG (and BrowseComp+, CodeQA, OOLONG-Pairs). Both benchmarks share the framing that **frontier LLMs struggle on long-context tasks once those tasks require dense access throughout the prompt** rather than retrieval-style pinpointing — OOLONG explicitly contrasts with NIAH-style benchmarks; LongBench Pro's first finding is that *"long-context optimization contributes more to long-context comprehension than parameter scaling"*. Both are public, both have evaluation harnesses released, both are mission-relevant: they define the *task class* where the wiki's anti-vendor-lock-in story has empirical traction (small-model-with-RLM > big-model-direct).

## Reference Card

> [!info] Combined reference card
>
> | Field | OOLONG (Bertsch et al., Nov 2025) | LongBench Pro (Chen et al., Jan 2026) |
> |---|---|---|
> | **arXiv** | 2511.02817 | 2601.02872 |
> | **Submitted** | 4 Nov 2025 | 6 Jan 2026 |
> | **Subjects** | cs.CL · cs.AI | cs.CL · cs.AI |
> | **Authors** | Amanda Bertsch · Adithya Pratapa · Teruko Mitamura · Graham Neubig · Matthew R. Gormley | Ziyang Chen · Xing Wu · Junlong Jia · Chaochen Gao · Qi Fu · Debing Zhang · Songlin Hu |
> | **Affiliation hint** | CMU (Neubig at CMU) | (per author list — likely Tsinghua / Chinese AI lab) |
> | **Languages** | English | **English + Chinese (bilingual)** |
> | **Total samples** | 50 tasks per `trec_coarse` split + 20 OOLONG-Pairs (per RLM paper) + 2 task sets (Oolong-synth + Oolong-real) | 1,500 naturally-occurring samples |
> | **Length range** | Tested at 132K + 263K (per RLM paper); paper goes up to 128K with all-frontier-models <50% | 8K–256K tokens |
> | **Length levels** | Continuous variable | 6 discrete levels (taxonomy dimension) |
> | **Difficulty levels** | Continuous (varies by query type) | 4 levels (calibrated by model performance) |
> | **Task types** | classification + counting + temporal reasoning + user-relation reasoning + distributional aggregation | 11 primary + 25 secondary task categories |
> | **Construction method** | Synthetic (`Oolong-synth`, ablatable) + Real (`Oolong-real`, real-world conversations) | **Human-Model Collaborative Construction** (frontier LLM drafts → expert validates) |
> | **Models evaluated in original paper** | GPT-5 · Claude-Sonnet-4 · Gemini-2.5-Pro (all <50% at 128K) | **46 widely-used long-context LLMs** |
> | **Released** | Yes — data + evaluation harness | Yes — bilingual; HTML version available |
> | **Used in RLM paper as** | Primary evaluation surface (Table 1: `trec_coarse` split + `OOLONG-Pairs` modification) | Training data source for RLM-Qwen3-8B (English split, 750 tasks) |
> | **Key finding** | Frontier models <50% at 128K when tasks require dense-access reasoning, not retrieval | Long-context optimization > parameter scaling; effective context << claimed context; thinking paradigm Pareto-trade-off |
> | **Confidence label** | high (abstract level only — Layer 1 PDF not yet ingested) | high (abstract level only — Layer 1 PDF not yet ingested) |

## Key Insights

1. **OOLONG is the benchmark where frontier models break.** From the abstract: *"Even frontier models struggle on Oolong, with GPT-5, Claude-Sonnet-4, and Gemini-2.5-Pro all achieving less than 50% accuracy on both splits at 128K."* This is the empirical ceiling RLM(GPT-5-mini) shattered at 56.5% on the `trec_coarse` 131K split (per RLM paper Table 1) — beating base GPT-5's 44.0% by 28% relative.

2. **OOLONG is explicitly NOT NIAH-style.** From the abstract: *"existing long-context evaluations... tend to rely on retrieval from one or more sections of the context, which allows nearly all of the context tokens to be disregarded as noise."* OOLONG instead requires *"analyzing individual chunks of text on an atomic level, and then aggregating these analyses to answer distributional questions."* This is exactly the complexity class the [RLM paper's Observation 3](src-rlm-paper-deep-dive-table-1-training-recipe-six-observations.md) identifies as where RLM gains the most.

3. **OOLONG has two splits: synth and real.** `Oolong-synth` is naturalistic synthetic (component-ablatable for clean experimentation); `Oolong-real` requires reasoning over real-world conversational data. The RLM paper used the `trec_coarse` split (which appears to be a subset of Oolong-synth based on the structured nature of the 50-task format).

4. **LongBench Pro is the natural training-data source.** From the abstract: 1,500 samples × 11 primary tasks × English + Chinese. The RLM paper sampled 750 English tasks (half the corpus) for trajectory generation. The Human-Model Collaborative Construction pipeline (frontier-LLM-drafts + expert-validates) ensures quality at scale — exactly the kind of training data shape that produces transferable RLM trajectories.

5. **LongBench Pro's first finding is foundational for the wiki's mission**: *"long-context optimization contributes more to long-context comprehension than parameter scaling."* Direct empirical support for: smaller models with the right post-training > bigger models without. This is the principle that makes RLM-Qwen3-8B (8B + RLM training) approach GPT-5 on long-context tasks.

6. **LongBench Pro's second finding documents the effective-context-length gap**: *"effective context length is typically shorter than the claimed context length, with pronounced cross-lingual misalignment."* This is the exact failure mode RLM addresses — the gap between *claimed* 128K window and *effective* useful window is filled by REPL-recursion. The bilingual angle adds another dimension: most long-context evals are English-only, so claims about cross-lingual (esp. Chinese) effective context are a separate research surface.

7. **LongBench Pro's third finding ties to thinking-mode tradeoffs**: *"the 'thinking' paradigm helps primarily models trained with native reasoning, while mixed-thinking designs offer a promising Pareto trade-off."* Two implications: (a) RLM's recursive paradigm parallels but extends thinking-paradigm reasoning — RLM-Qwen3-8B is post-trained to be RLM-native, the same way reasoning models are post-trained for thinking; (b) "mixed-thinking" designs could coexist with RLM (thinking on the root LM + recursive sub-calls without thinking).

8. **The bilingual dimension matters for sovereignty/anti-vendor-lock-in**. Most major closed-source LMs (GPT-5, Claude-Sonnet-4, Opus 4.7) are English-trained-dominant. Open-weight models like Qwen3 are explicitly bilingual (Mandarin+English by Qwen Team's design). LongBench Pro's bilingual evaluation is a competitive advantage for Qwen3-class models the wiki has been tracking. RLM-Qwen3-8B inherits Qwen3-8B's bilingual capability + adds the long-context recursive paradigm — directly relevant to operator's mission for international/multi-lingual workloads.

9. **OOLONG release status: "We release the data and evaluation harness."** Public. Anyone can reproduce the RLM-on-OOLONG numbers. This is structurally important for the wiki's mission: the *empirical evidence chain* for RLM is reproducible, not gated.

10. **LongBench Pro release status: PDF + HTML public on arXiv.** Public. The training data is reachable.

11. **Both benchmarks are recent (Nov 2025 / Jan 2026).** They postdate most of the wiki's existing benchmark coverage. The wiki should update its [AI Infrastructure Decision Framework 2026](../../spine/references/ai-infrastructure-decision-framework-2026.md) and [2026 Consumer Hardware AI Stack](../../spine/references/2026-consumer-hardware-ai-stack.md) to reference these as the canonical long-context evaluation surfaces.

## Deep Analysis

### OOLONG — The Long-Context-Reasoning Benchmark RLM Built On

OOLONG's distinguishing claim from the abstract:

> "While several carefully designed long-context evaluations have recently been released, these evaluations tend to rely on retrieval from one or more sections of the context, which allows nearly all of the context tokens to be disregarded as noise. This represents only one type of task that might be performed with long context."

The contrast with NIAH/RULER is structural: needle-in-haystack is O(1) in input — the answer is one chunk; retrieval suffices. OOLONG is O(N) — every chunk contributes; aggregation is required. Per the [RLM paper Figure 1](src-rlm-paper-deep-dive-table-1-training-recipe-six-observations.md), this complexity-class difference is exactly where frontier models degrade fastest and where RLM scales best.

> [!info] OOLONG capabilities tested
>
> 1. **Atomic-chunk analysis** — read each entry, classify or extract semantic content
> 2. **Distributional aggregation** — count, compare frequencies, find pairs satisfying joint conditions
> 3. **Classification in-context** — figure out labels from semantics, not provided
> 4. **Counting in-context** — aggregate exact counts over entries
> 5. **Temporal relations** — date-based filters and range queries
> 6. **User relations** — user-ID-based grouping and pair construction

The OOLONG-Pairs modification (introduced by the RLM authors as a derivative benchmark) explicitly forces O(N²) — pair-aggregation queries where the answer requires all pairs satisfying joint properties. This is the highest-complexity end of the OOLONG framing.

### LongBench Pro — The Bilingual Training-Data Source

LongBench Pro's distinguishing claims:

> "synthetic tasks underrepresent real-world complexity, while fully manual annotation is costly to scale to extreme lengths and diverse scenarios."

The paper's solution: **Human-Model Collaborative Construction**. Frontier LLMs draft challenging questions + reference answers + design rationales + solution processes; experts then validate correctness and refine problematic cases. This pipeline gets the cost-of-quality balance — scale via LLM drafting, quality via expert review. From the wiki's [structured-context principle](../../lessons/04_principles/hypothesis/structured-context-governs-agent-behavior-more-than-content.md) lens: this is structured-collaboration as a data-construction tool, the same pattern as the wiki's own ingestion → synthesis → validate flow.

> [!abstract] LongBench Pro's multi-dimensional taxonomy
>
> | Dimension | Levels | What it captures |
> |---|---|---|
> | **Context requirement** | Full vs partial dependency | Does the answer require ALL the context, or just SOME of it? (NIAH = partial; OOLONG = full) |
> | **Length** | 6 levels (8K-256K) | The same task can be presented at different lengths to measure scaling |
> | **Difficulty** | 4 levels (calibrated by model performance) | Empirical difficulty, not author-declared |

This is a more rigorous taxonomy than most benchmarks — the multi-dimensional structure means a researcher can pick a slice (e.g., "full-dependency tasks at 64K, difficulty 3") to evaluate specific capabilities.

### How RLM Used Both Benchmarks

| Use | Benchmark | Concrete details from RLM paper |
|---|---|---|
| **Evaluation** | OOLONG `trec_coarse` (50 tasks at 131K + 263K) | Table 1: RLM(GPT-5) 56.5%, RLM(Qwen3-Coder-480B) 48.0%, RLM-Qwen3-8B (fine-tuned) 32.0%. Base GPT-5: 44.0%. |
| **Evaluation** | OOLONG-Pairs (20 new pair-aggregation queries) | Table 1: RLM(GPT-5) 58.0%, base GPT-5 0.1%. RLM-Qwen3-8B 5.2%. |
| **Training** | LongBenchPro (English split, 750 tasks) | RLM(Qwen3-Coder-480B-A35B) generates 2,250 candidate trajectories → 1,072 after filtering → per-turn SFT samples → fine-tune Qwen3-8B with prime-rl in 48 H100 hours |

The training-evaluation domain gap matters: the model is trained on LongBenchPro tasks but evaluated on a different benchmark suite (OOLONG, OOLONG-Pairs, BrowseComp+, CodeQA). The 28.3% average improvement of RLM-Qwen3-8B over Qwen3-8B-as-RLM is a *generalization signal* — training in one domain transfers to evaluation in others. The paper frames this as Observation 6: *"Training RLMs on one domain can improve general downstream RLM performance."*

### Why This Matters for the Wiki's Mission

| Mission claim | Direct support from these benchmarks |
|---|---|
| "Long-context optimization beats parameter scaling" | LongBench Pro Finding 1 — empirically validated across 46 LLMs |
| "Effective context << claimed context" | LongBench Pro Finding 2 — direct measurement |
| "Frontier models break on long-context dense-access tasks" | OOLONG abstract — GPT-5 / Claude / Gemini all <50% at 128K |
| "Smaller-trained-right beats bigger-untrained" | RLM-Qwen3-8B's 32% on OOLONG approaches GPT-5's 44% — at 8B vs frontier scale |
| "Open public benchmarks anchor open evaluation" | Both released publicly; reproducible; not vendor-locked |

These benchmarks are the **measurement infrastructure** the wiki's mission depends on. Without them, the RLM paper's claims would be unfalsifiable; with them, anyone can verify the cost/quality tradeoff at the task class the operator's mission cares about.

## Open Questions

> [!question] What are the exact OOLONG synthetic task generators?
> The abstract names `Oolong-synth` as "naturalistic synthetic" with "components ablatable" — but the actual generation grammar / template format isn't in the abstract. (Requires: ingest paper PDF or evaluation harness code.)

> [!question] What are the 11 primary + 25 secondary LongBench Pro task categories?
> The abstract names the count but not the categories. For training-data quality assessment + selecting subsets relevant to operator's task mix, this matters. (Requires: ingest paper PDF.)

> [!question] What's LongBench Pro's Chinese-half coverage like?
> Mentioned as bilingual but the English/Chinese split ratios + cross-lingual difficulty parity aren't in the abstract. Operator's primary workload language is English; Chinese coverage is bonus. (Requires: ingest paper PDF.)

> [!question] How does RLM-Qwen3-8B perform on Oolong-real (vs Oolong-synth)?
> The RLM paper used `trec_coarse` (likely Oolong-synth subset). Performance on Oolong-real (real-world conversations) would tell whether RLM's gains hold on naturalistic data. (Requires: separate experiment.)

> [!question] Are there OOLONG / LongBench Pro extensions yet (v2, larger context, more tasks)?
> Both papers are <6 months old at synthesis time. Field is moving fast. Worth tracking. (Requires: arXiv watch / Hugging Face dataset list.)

> [!question] How does LongBench Pro compare to LongBench v2 (Bai et al. 2025)?
> The RLM paper Table 1 uses LongBench v2's CodeQA split (Bai et al.). LongBench Pro is a different benchmark by different authors. The relationship + overlap aren't clear from abstracts. (Requires: cross-reading both PDFs.)

> [!question] Could the wiki's own ingestion pipeline use LongBench Pro as a quality benchmark?
> The wiki's `tools/pipeline.py post` validates page structure but not synthesis quality. LongBench Pro's task taxonomy could provide a synthesis-quality eval surface. (Requires: design experiment.)

## Applicability

> [!info] Where to use OOLONG
> - As an **evaluation surface** for RLM-class systems on long-context reasoning + aggregation
> - As a **complexity-class probe** for any long-context model (does it scale with O(N) reasoning?)
> - As a **public alternative to RULER** when retrieval-style needles aren't representative

> [!info] Where to use LongBench Pro
> - As a **training-data source** for long-context post-training (the same way RLM-Qwen3-8B used it)
> - As an **evaluation surface** for bilingual long-context capability
> - As a **multi-dimensional eval** when the user wants to slice by length × difficulty × dependency

> [!warning] Where neither applies
> - **Short-context tasks** (≤8K tokens) — both benchmarks target longer ranges
> - **Single-turn factual Q&A** — both require multi-step reasoning
> - **Visual / multimodal** — text-only benchmarks
> - **Code-only** — LongBench v2 (Bai et al.) is more code-focused; CodeQA from there used by RLM

## Relationships

- BUILDS ON: [[src-rlm-paper-deep-dive-table-1-training-recipe-six-observations|RLM Paper Deep Dive]] (this synthesis anchors the benchmarks the deep-dive uses)
- BUILDS ON: [[src-rlm-empirical-findings-oolong-browsecomp-rlm-qwen3-8b|RLM Empirical Findings]] (OOLONG is the source of the headline 114% improvement)
- DEMONSTRATES: [[right-process-for-right-context-the-goldilocks-imperative|Principle 3 — Goldilocks]] (LongBench Pro's multi-dimensional taxonomy lets researchers slice tasks by appropriate complexity)
- RELATES TO: [[2026-consumer-hardware-ai-stack|2026 Consumer Hardware AI Stack]] (these benchmarks define the long-context capability surface for tier-0 candidates)
- RELATES TO: [[ai-infrastructure-decision-framework-2026|AI Infrastructure Decision Framework 2026]] (long-context evaluation should reference these as canonical surfaces)
- FEEDS INTO: [[rlm-qwen3-8b-vs-qwen3-6-27b-tier-0-long-context-candidate|Tier-0 Candidate Comparison]] (defines the evaluation surface for the comparison)

## Backlinks

[[src-rlm-paper-deep-dive-table-1-training-recipe-six-observations|RLM Paper Deep Dive]]
[[src-rlm-empirical-findings-oolong-browsecomp-rlm-qwen3-8b|RLM Empirical Findings]]
[[right-process-for-right-context-the-goldilocks-imperative|Principle 3 — Goldilocks]]
[[2026 Consumer Hardware AI Stack]]
[[ai-infrastructure-decision-framework-2026|AI Infrastructure Decision Framework 2026]]
[[Tier-0 Candidate Comparison]]
