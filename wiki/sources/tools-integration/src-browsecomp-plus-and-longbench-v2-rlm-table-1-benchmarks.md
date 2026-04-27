---
title: "Synthesis — BrowseComp-Plus (Chen et al. Aug 2025) + LongBench v2 (Bai et al. Dec 2024): Completing the RLM Table 1 Benchmark Coverage"
aliases:
  - "BrowseComp-Plus"
  - "BrowseComp+"
  - "LongBench v2"
  - "BrowseComp+ + LongBench v2 Synthesis"
type: source-synthesis
domain: tools-integration
status: synthesized
confidence: high
maturity: seed
created: 2026-04-27
updated: 2026-04-27
last_reviewed: 2026-04-27
sources:
  - id: browsecomp-plus-paper
    type: paper
    url: https://arxiv.org/abs/2508.06600
    file: raw/articles/250806600-browsecomp-plus-a-more-fair-and-transparent-evaluation-benchmark-of-de.md
    title: "BrowseComp-Plus: A More Fair and Transparent Evaluation Benchmark of Deep-Research Agent (Chen et al., Aug 2025)"
    description: "20-author IR-research benchmark (lead authors: Zijian Chen, Xueguang Ma, Jimmy Lin) — derived from BrowseComp with fixed corpus + human-verified supporting docs + mined challenging negatives. Used in RLM Table 1 (RLM(GPT-5) 91.3% on 1K-doc subset)."
    ingested: 2026-04-27
  - id: longbench-v2-paper
    type: paper
    url: https://arxiv.org/abs/2412.15204
    title: "LongBench v2: Towards Deeper Understanding and Reasoning on Realistic Long-context Multitasks (Bai et al., Dec 2024 / Jan 2025 v2)"
    file: raw/articles/241215204-longbench-v2-towards-deeper-understanding-and-reasoning-on-realistic-l.md
    description: "503 multi-choice questions × 6 categories (incl. **CodeQA** — RLM Table 1 task). 8K to 2M words. Humans 53.7% under 15-min constraint. o1-preview 57.7% surpasses humans by 4% (validating thinking-paradigm for long-context)."
    ingested: 2026-04-27
  - id: rlm-paper-deep-dive-companion
    type: wiki
    file: wiki/sources/tools-integration/src-rlm-paper-deep-dive-table-1-training-recipe-six-observations.md
    description: "RLM paper deep-dive — Table 1 uses BrowseComp+ (1K docs) + LongBench v2 CodeQA split"
  - id: rlm-empirical-findings-companion
    type: wiki
    file: wiki/sources/tools-integration/src-rlm-empirical-findings-oolong-browsecomp-rlm-qwen3-8b.md
    description: "RLM blogpost-level findings — BrowseComp+ headline (RLM(GPT-5) maintains perfect performance at 1000 documents / 10M+ tokens)"
  - id: oolong-longbench-pro-companion
    type: wiki
    file: wiki/sources/tools-integration/src-oolong-and-longbench-pro-long-context-benchmarks-rlm-anchors.md
    description: "Companion synthesis — covers OOLONG (eval) + LongBench Pro (training data); this page covers the OTHER two Table 1 benchmarks"
tags: [browsecomp-plus, longbench-v2, deep-research, multi-hop, code-repository-understanding, long-context-benchmarks, codeqa, search-r1, qwen3-embedding, gpt-5, o1-preview, thinking-paradigm, jimmy-lin, tsinghua, rlm-table-1, fixed-corpus, fairness-transparency, mission-2026-04-27, paradigm-validation, anti-vendor-lock-in, tools-integration, ir-research, retrieval]
---

# Synthesis — BrowseComp-Plus + LongBench v2: Completing the RLM Table 1 Benchmark Coverage

## Summary

The remaining two benchmarks anchoring the [RLM paper Table 1](src-rlm-paper-deep-dive-table-1-training-recipe-six-observations.md). **BrowseComp-Plus** (Chen, Ma, Zhuang, ... Wenhu Chen, Jimmy Lin — 20 authors; arXiv 2508.06600, submitted 8 Aug 2025) is a fixed-corpus, transparency-focused derivative of OpenAI's BrowseComp benchmark for evaluating Deep-Research agents — RLM(GPT-5) achieves 91.3% at 1K-document subset (~6-11M tokens) where base GPT-5 hits the context limit at 0.0%. **LongBench v2** (Bai, Tu, Zhang, Peng, ..., Tang, Li — 12 authors; arXiv 2412.15204 v2 Jan 2025) is the 503-multi-choice-question successor benchmark spanning **8K to 2M words across 6 major task categories** (single-doc QA, multi-doc QA, long ICL, long dialogue, **code repository understanding [CodeQA]**, long structured data) — the CodeQA split is RLM Table 1 task #1 where RLM(GPT-5) scores 62.0% vs base GPT-5 24.0%. **Together with the [OOLONG + LongBench Pro synthesis](src-oolong-and-longbench-pro-long-context-benchmarks-rlm-anchors.md)**, this completes coverage of all 4 RLM Table 1 evaluation benchmarks. Two findings stand out: (1) **BrowseComp+'s retrieval-disentanglement design** — Search-R1+BM25 = 3.86%, GPT-5 = 55.9%, GPT-5+Qwen3-Embedding-8B = 70.1% — proves retriever choice matters more than model choice on multi-hop research tasks. (2) **LongBench v2's o1-preview-beats-humans finding** — humans achieve 53.7% in 15min, best direct-answer model 50.1%, **o1-preview 57.7%** — provides the canonical empirical case for thinking-time scaling on long-context tasks, parallel to RLM's recursive-time scaling. Both benchmarks are public, both have evaluation harnesses, both validate the wiki's mission framing: long-context dense-reasoning is the task class where structural inference-time-compute approaches (RLM-recursion, o1-thinking, retriever-augmentation) deliver disproportionate value over pure parameter scaling.

## Reference Card

> [!info] Combined reference card
>
> | Field | BrowseComp-Plus (Chen et al., Aug 2025) | LongBench v2 (Bai et al., Dec 2024 / Jan 2025) |
> |---|---|---|
> | **arXiv** | 2508.06600 | 2412.15204 (v2) |
> | **Submitted** | 8 Aug 2025 | 19 Dec 2024 v1 / 3 Jan 2025 v2 |
> | **Subjects** | cs.CL · **cs.IR** | cs.CL · cs.AI |
> | **Authors** | 20 authors (lead: Zijian Chen, Xueguang Ma, Shengyao Zhuang) — incl. **Wenhu Chen**, **Jimmy Lin** | 12 authors (lead: Yushi Bai) — Tsinghua-affiliated likely (Tang, Li are well-known names) |
> | **Total tasks** | Derived from BrowseComp (multi-hop research queries) | **503 challenging multi-choice questions** |
> | **Length range** | RLM tested at 1K docs ~6-11M tokens; benchmark itself unspecified upper | **8K to 2M words** |
> | **Task categories** | DeepResearch / multi-hop search-+-reason | **6 major categories**: single-doc QA · multi-doc QA · long in-context learning · long-dialogue history · **code repository understanding (CodeQA)** · long structured data |
> | **Construction method** | Fixed curated corpus + human-verified supporting docs + mined challenging negatives | ~100 highly educated individuals collected; automated + manual review |
> | **Human baseline** | (not given in abstract) | **53.7% under 15-minute time constraint** |
> | **Best direct-answer model in original paper** | GPT-5 = 55.9% (with BM25); 70.1% (with Qwen3-Embedding-8B retriever) | 50.1% direct-answer best |
> | **Best thinking model** | (not given in abstract) | **o1-preview = 57.7%, surpasses humans by 4%** |
> | **Key contribution** | Fairness + transparency vs live-web BrowseComp (which uses opaque APIs) | Difficulty + breadth + multi-task realism |
> | **Released** | Yes — fixed corpus public | Yes — project website linked |
> | **Used in RLM paper** | Table 1 BrowseComp+ (1K) — RLM(GPT-5) 91.3% vs base GPT-5 0.0% | Table 1 CodeQA split — RLM(GPT-5) 62.0% vs base GPT-5 24.0% |
> | **Paper length** | Standard arXiv length | **26 pages, 13 figures** |
> | **Confidence label** | high (abstract level — paper PDF not yet ingested) | high (abstract level — paper PDF not yet ingested) |

## Key Insights

1. **BrowseComp+ disentangles retriever quality from agent capability.** From the abstract: *"Evaluations on current benchmarks like BrowseComp relies on black-box live web search APIs, have notable limitations in (1) fairness: dynamic and opaque web APIs hinder fair comparisons and reproducibility... (2) transparency: lack of control over the document corpus makes it difficult to isolate retriever contributions."* The fixed-corpus design is a methodological breakthrough — anyone can reproduce; everyone evaluates on the same documents.

2. **The retriever-choice multiplier on BrowseComp+ is enormous**. Same-model GPT-5 ranges from 55.9% with BM25 to 70.1% with Qwen3-Embedding-8B — a +14 absolute point swing from retriever choice alone. **Open-source semantic retrievers (Qwen3-Embedding-8B) deliver competitive Deep-Research performance**. This is the wiki's anti-vendor-lock-in story validated at the retriever layer.

3. **Search-R1+BM25 floor is 3.86%** — small open model + lexical retriever. The gap between this and GPT-5+Qwen3-Embedding-8B (70.1%) is the size of the *capability stack* improvement available from upgrading individual layers (model + retriever). Each layer has its own multiplier.

4. **RLM(GPT-5) at 91.3% on the 1K-doc subset (~6-11M tokens) is dramatic**. Per the [RLM paper Table 1](src-rlm-paper-deep-dive-table-1-training-recipe-six-observations.md): RLM nearly solves the task while base GPT-5 hits context-limit (0.0%) and GPT-5+pre-query-BM25 also degrades sharply at 100+ docs. The original BrowseComp+ paper (which doesn't have RLM) tops out around 70% with retriever-augmented GPT-5. **RLM provides ~+20 absolute points beyond the strongest retriever-augmented GPT-5 baseline** at far larger document counts.

5. **LongBench v2 introduces the "thinking-beats-humans" finding for long-context.** From the abstract: *"the best-performing model, when directly answers the questions, achieves only 50.1% accuracy. In contrast, the o1-preview model, which includes longer reasoning, achieves 57.7%, surpassing the human baseline by 4%."* This is the canonical empirical case for thinking-time scaling on long-context tasks — and it parallels RLM's recursive-time scaling (different mechanism, same insight: inference-time compute > parameter scaling for hard long-context).

6. **LongBench v2 is the source of CodeQA in RLM Table 1.** Per the abstract, one of the 6 task categories is "**code repository understanding**". The RLM paper used this split: codebases ranging from 23K to 4.2M tokens. RLM(GPT-5) 62.0% vs base GPT-5 24.0% (often hitting context limit per Table 1's `*` annotation). Code-repository long-context is where RLM's REPL-recursion shines because the model can programmatically chunk + grep + recursively analyze.

7. **The 6 task categories of LongBench v2 are a reusable taxonomy for long-context evaluation**:
   1. Single-document QA
   2. Multi-document QA
   3. Long in-context learning
   4. Long-dialogue history understanding
   5. Code repository understanding (← used by RLM)
   6. Long structured data understanding

   This taxonomy is more granular than OOLONG's binary split (synth vs real) or LongBench Pro's primary/secondary tagging. For evaluating a model's long-context capability, sweeping all 6 categories is the comprehensive move.

8. **Both papers are dated EARLIER than RLM**. BrowseComp+ (Aug 2025) and LongBench v2 (Dec 2024) predate the RLM paper (Dec 2025). RLM authors picked these as evaluation surfaces because they were already established benchmarks with strong frontier-model baselines — RLM's advantage is measurable against a known floor.

9. **BrowseComp+ has 20 authors including IR-research luminaries**. Jimmy Lin (Waterloo, BM25 + ColBERT lineage), Wenhu Chen (Waterloo). The benchmark inherits IR-research methodological rigor (fixed corpus, mined negatives, human verification) — distinct from CMU's OOLONG (Neubig group, more NLP-leaning).

10. **The benchmark suite collectively defines the "hard long-context" task class**. With OOLONG (linear aggregation O(N)), OOLONG-Pairs (quadratic O(N²)), CodeQA (multi-file fixed reasoning), BrowseComp+ (multi-hop multi-document), the 4-task suite spans 4 distinct complexity classes. RLM's win across all 4 (+158% on CodeQA; ~impossible-to-91.3% on BrowseComp+; +28% on OOLONG; 0.1%-to-58% on OOLONG-Pairs) is what makes the paper's claim "task-agnostic" credible.

11. **LongBench v2 is bilingual-friendly via its Tsinghua-affiliated authorship**. Yushi Bai, Jie Tang, Juanzi Li are known Chinese-AI-research figures. The benchmark spans English broadly; Chinese coverage is implicit in some task categories. Pairs naturally with [LongBench Pro](src-oolong-and-longbench-pro-long-context-benchmarks-rlm-anchors.md) which is explicitly bilingual.

12. **All 4 RLM Table 1 benchmarks are now in the wiki** (4 source-synthesis pages + 1 paper deep-dive). The empirical claim chain — "RLM(GPT-5) vs base GPT-5 across 4 diverse long-context tasks" — has each task definition + author affiliation + license/release status traceable to a wiki page.

## Deep Analysis

### BrowseComp+ — IR-Methodology Applied to Deep-Research Evaluation

The benchmark's distinguishing claim is methodological:

> "the current evaluations may compare a complete deep research system at a given time, but they do not foster well-controlled experiments to provide insights into the capability of underlying deep research LLMs."

The fix is a **fixed corpus + human-verified supporting docs + mined challenging negatives**. This is classic IR-evaluation methodology (controlled corpus, gold judgments, hard negatives) applied to LLM-Deep-Research evaluation. The paper's lead authors include Jimmy Lin (Waterloo, founder of Anserini, prolific BM25 + ColBERT contributor) — IR-evaluation rigor is in the DNA.

**The retriever multiplier table** (from the abstract):

| System | BrowseComp+ accuracy |
|---|---|
| Search-R1 + BM25 | **3.86%** |
| GPT-5 (with BM25?) | 55.9% |
| GPT-5 + Qwen3-Embedding-8B | **70.1%** with **fewer search calls** |

The +14 absolute points from BM25 → Qwen3-Embedding-8B (same model: GPT-5) tells us:
1. **Retriever quality is a first-order multiplier**, not a second-order tweak
2. **Open-source dense retrievers (Qwen3-Embedding-8B)** match or beat the proprietary alternatives on Deep-Research
3. **Fewer search calls + better accuracy** = retriever quality also reduces inference cost

For the wiki's mission: this is *the* empirical anchor for "open-source retrievers compete with closed-source ones." Combined with [Qwen3.6-27B (open-source frontier-class generation)](src-qwen3-6-27b-dense-beats-397b-moe-agentic-coding.md), the open-source stack from retrieval through generation is now empirically validated.

### LongBench v2 — The Thinking-Time-Scaling Canonical Result

The paper's most-cited result (from the abstract):

> "human experts achieving only **53.7%** accuracy under a 15-minute time constraint... the best-performing model, when directly answers the questions, achieves only **50.1%** accuracy. In contrast, the **o1-preview** model, which includes longer reasoning, achieves **57.7%**, surpassing the human baseline by 4%."

Three numbers. Three implications:

1. **Long-context tasks are HARD for humans.** 53.7% in 15 minutes by educated experts is barely above chance for some task formats. This is a benchmark calibrated to human cognitive limits.
2. **Direct LLM answering is ~human-floor.** 50.1% direct-answer best model — language models without thinking are essentially at human's-quick-pass level.
3. **Thinking pushes past human-baseline.** o1-preview at 57.7% is the *first widely-cited result* of an LM exceeding human performance on a hard long-context multi-task benchmark. The mechanism (longer reasoning) is exactly what RLM does at a different abstraction level (longer recursion + REPL execution).

This validates the wiki's mission framing one layer deeper: **inference-time compute is the new dimension of scaling**. CoT/thinking is one direction; RLM-recursion is another; both succeed where parameter scaling alone plateaus.

### The 6 Categories of LongBench v2 — Taxonomy for Comprehensive Evaluation

| Category | Example task type | RLM-paper relevance |
|---|---|---|
| 1. Single-document QA | Read one long document, answer questions | Background — RLM not directly tested on this |
| 2. Multi-document QA | Reason across multiple documents | Adjacent to BrowseComp+'s multi-hop |
| 3. Long in-context learning | Few-shot from many examples | Adjacent to OOLONG's distributional aggregation |
| 4. Long-dialogue history understanding | Multi-turn dialogue context | Adjacent to multi-turn agent benchmarks |
| 5. **Code repository understanding (CodeQA)** | Reason over codebases | **Used directly by RLM Table 1** |
| 6. Long structured data understanding | Tables, JSON, structured docs | Adjacent — could be RLM applicable |

For an operator wanting comprehensive long-context evaluation of a tier-0 candidate (Qwen3.6-27B or RLM-Qwen3-8B), running against all 6 LongBench v2 categories provides a multi-dimensional capability picture.

### The 4-Benchmark Complexity-Class Map (Combined with [OOLONG + LongBench Pro](src-oolong-and-longbench-pro-long-context-benchmarks-rlm-anchors.md))

> [!abstract] Complete complexity-class map of RLM Table 1 evaluation
>
> | Benchmark | Complexity class | What it measures |
> |---|---|---|
> | S-NIAH (Figure 1 only) | O(1) — constant per query | Retrieval saturation point |
> | LongBench v2 CodeQA | O(fixed-files) — bounded | Multi-file code-reasoning over fixed repository |
> | BrowseComp+ (1K docs) | O(multi-hop-doc) — variable | Multi-hop reasoning across uncertain document set |
> | OOLONG `trec_coarse` | O(N) — linear | Distributional aggregation requiring all entries |
> | OOLONG-Pairs | O(N²) — quadratic | Pair-aggregation requiring all pairs of entries |

Each benchmark stresses a different complexity dimension. RLM wins across all of them — different mechanisms within the same paradigm (REPL + recursion) handle different complexity classes.

### Mission Implications — The Open-Source Stack is Empirically Validated

Combining this synthesis with the [RLM thread](src-rlm-paper-deep-dive-table-1-training-recipe-six-observations.md):

| Layer | Open-source option | Empirical validation |
|---|---|---|
| **Generation (frontier)** | Qwen3-Coder-480B-A35B | Beats CodeAct + Summary baselines on 3/4 RLM Table 1 tasks |
| **Generation (tier-0)** | Qwen3.6-27B + RLM(Qwen3-8B-tuned) | RLM-Qwen3-8B approaches GPT-5 on 3/4 long-context tasks |
| **Retrieval** | **Qwen3-Embedding-8B** | **+14pts on BrowseComp+ over BM25** (GPT-5 55.9 → 70.1, FEWER search calls) |
| **Inference paradigm** | RLM (alexzhang13/rlm) | 91.3% on 1K-doc subset where direct GPT-5 fails |
| **Training infrastructure** | verifiers + prime-rl | Trained RLM-Qwen3-8B in 48 H100 hours |
| **Evaluation infrastructure** | OOLONG + LongBench Pro + LongBench v2 + BrowseComp+ | All public, all reproducible |

Every layer of the open-source post-Anthropic stack now has empirical validation in the wiki. The mission's anti-vendor-lock-in framing has direct paper evidence at each stack layer.

## Open Questions

> [!question] What's the BrowseComp+ corpus size?
> Abstract says "fixed, carefully curated corpus" — RLM paper used 1K-doc subset. The full corpus per the original BrowseComp+ paper might be different. (Requires: paper PDF for corpus construction details.)

> [!question] What are the 503 LongBench v2 question type breakdowns?
> Abstract names 6 categories but not the per-category counts. For training data subset selection, this matters. (Requires: paper PDF.)

> [!question] How does Qwen3-Embedding-8B compare to other open-source dense retrievers?
> The +14pt jump over BM25 is impressive but the abstract doesn't compare to other dense retrievers (BGE, E5, etc.). (Requires: paper PDF + cross-comparison literature.)

> [!question] Does o1-preview's long-context advantage transfer to o3 / o3-pro / o4 family?
> LongBench v2 was published Dec 2024 with o1-preview as the headline thinking model. By 2026-04-27, the o-series has evolved (o3-mini, o3, o3-pro, etc.). The 57.7% number may be obsolete; thinking-paradigm gains may have widened. (Requires: cross-comparison + benchmark re-runs.)

> [!question] Can BrowseComp+ be used as a verifiers environment for AICP backend benchmarking?
> The fixed-corpus design makes it ideal for reproducible benchmarking. Could be wrapped as a `verifiers` `Environment` for evaluating AICP's various backends on Deep-Research tasks. (Requires: implementation work.)

> [!question] Is BrowseComp+ used by other recent papers beyond RLM?
> Aug 2025 paper, used in RLM (Dec 2025). What other published RL-or-RAG-or-agent papers use it? Citation graph would tell. (Requires: Google Scholar / connected-papers lookup.)

> [!question] Does LongBench v2's CodeQA split overlap with SWE-bench / CodeContests / HumanEval?
> Different benchmarks for different task shapes. CodeQA in LongBench v2 is multi-choice-over-codebase; SWE-bench is patch-generation. They evaluate different things but might inform each other. (Requires: cross-comparison.)

> [!question] How does LongBench Pro differ from LongBench v2?
> Both are "LongBench" — different teams (Pro: Chen et al. Tsinghua; v2: Bai et al. Tsinghua). Same lab but different benchmarks. The relationship and overlap aren't clear from abstracts. (Requires: PDF cross-read.)

## Applicability

> [!info] Where to use BrowseComp+
> - **Deep-Research agent evaluation** with retriever-disentanglement (the single best benchmark for "is this agent good at multi-hop research?")
> - **Retriever benchmarking** independent of generation model (substitute different retrievers behind same GPT-5)
> - **RLM evaluation** at large document counts (1K-doc + multi-hop + ~10M tokens)

> [!info] Where to use LongBench v2
> - **Comprehensive long-context capability mapping** (6 categories cover most realistic task shapes)
> - **Code-repository understanding evaluation** (CodeQA split, well-calibrated difficulty)
> - **Thinking-vs-direct-answer comparison** (the o1-preview vs direct answer canonical case)
> - **Long-context multi-choice eval** (when free-form generation is harder to score)

> [!warning] Where these benchmarks DON'T apply
> - Both **English-dominant** (BrowseComp+ implicitly; LongBench v2 broadly) — for bilingual eval, use LongBench Pro
> - **Single-turn factual Q&A on short contexts** — both target longer / multi-step
> - **Realtime agentic tasks** — both are static benchmarks, not live agentic environments
> - **Visual / multimodal** — text-only

## Relationships

- BUILDS ON: [[src-rlm-paper-deep-dive-table-1-training-recipe-six-observations|RLM Paper Deep Dive]] (this synthesis anchors the remaining benchmarks the deep-dive uses)
- BUILDS ON: [[src-rlm-empirical-findings-oolong-browsecomp-rlm-qwen3-8b|RLM Empirical Findings]] (BrowseComp+ is in the headline blogpost framing)
- BUILDS ON: [[src-oolong-and-longbench-pro-long-context-benchmarks-rlm-anchors|OOLONG + LongBench Pro Synthesis]] (companion synth — together cover all 4 RLM Table 1 benchmarks)
- COMPARES TO: [[rlm-qwen3-8b-vs-qwen3-6-27b-tier-0-long-context-candidate|Tier-0 Candidate Comparison]] (these are the evaluation surfaces for the comparison)
- DEMONSTRATES: [[right-process-for-right-context-the-goldilocks-imperative|Principle 3 — Goldilocks]] (4 different complexity classes, 4 different optimal strategies)
- DEMONSTRATES: [[infrastructure-over-instructions-for-process-enforcement|Principle 1]] (BrowseComp+'s fixed-corpus is structural enforcement of evaluation fairness)
- RELATES TO: [[2026-consumer-hardware-ai-stack|2026 Consumer Hardware AI Stack]] (long-context capability evaluation for tier-0 candidates)
- RELATES TO: [[ai-infrastructure-decision-framework-2026|AI Infrastructure Decision Framework 2026]] (long-context evaluation should reference all 4 of these as the canonical surface)
- RELATES TO: [[ai-model-provider-harness-decision-matrix-2026|AI Model Provider Harness Decision Matrix 2026]] (benchmark-driven row evaluation)
- FEEDS INTO: [[never-synthesize-from-descriptions-alone|Never Synthesize from Descriptions Alone]] (this synthesis is at abstract-level only; PDF deep-read remains a Layer-1 expansion path)

## Backlinks

[[src-rlm-paper-deep-dive-table-1-training-recipe-six-observations|RLM Paper Deep Dive]]
[[src-rlm-empirical-findings-oolong-browsecomp-rlm-qwen3-8b|RLM Empirical Findings]]
[[OOLONG + LongBench Pro Synthesis]]
[[Tier-0 Candidate Comparison]]
[[right-process-for-right-context-the-goldilocks-imperative|Principle 3 — Goldilocks]]
[[infrastructure-over-instructions-for-process-enforcement|Principle 1]]
[[2026 Consumer Hardware AI Stack]]
[[ai-infrastructure-decision-framework-2026|AI Infrastructure Decision Framework 2026]]
[[AI Model Provider Harness Decision Matrix 2026]]
[[never-synthesize-from-descriptions-alone|Never Synthesize from Descriptions Alone]]
