---
title: "Synthesis — OOLONG Paper Deep Dive: 2-Split Aggregation Benchmark, 9-Model Leaderboard, Frontier Models Fail Below 50% at 128K, DeepSeek-R1 Pathology, Reasoning-Effort Counter-Intuition (CMU; arXiv 2511.02817 v1, Nov 2025)"
aliases:
  - "OOLONG Paper Deep Dive"
  - "OOLONG Tables 1-4"
  - "OOLONG-synth + OOLONG-real Deep Dive"
  - "OOLONG R1 Pathology"
type: source-synthesis
domain: tools-integration
status: synthesized
confidence: high
maturity: seed
created: 2026-04-27
updated: 2026-04-27
last_reviewed: 2026-04-27
sources:
  - id: oolong-paper-pdf
    type: paper
    url: https://arxiv.org/pdf/2511.02817
    file: raw/papers/oolong-evaluating-long-context-reasoning-and-aggregation-capabilities.md
    title: "OOLONG arXiv 2511.02817 v1 (4 Nov 2025) — Full PDF"
    description: "28 pages with Appendix; 1250-line raw scrape. Authors: Amanda Bertsch, Adithya Pratapa, Teruko Mitamura, Graham Neubig, Matthew R. Gormley — all CMU Language Technologies Institute (@cs.cmu.edu). Lead author Bertsch supported by NSF GRFP DGE2140739. Code at github.com/abertsch72/oolong; data at huggingface.co/oolongbench/oolong-[synth, real]."
    ingested: 2026-04-27
  - id: oolong-abstract-companion
    type: wiki
    file: wiki/sources/tools-integration/src-oolong-and-longbench-pro-long-context-benchmarks-rlm-anchors.md
    description: "Abstract-level companion synthesis covering OOLONG AND LongBench Pro together at Layer 0/1; this page is the dedicated Layer-1 deep-dive on OOLONG alone, sourced from the full PDF rather than the abstract page. Combined synth speculated 'CMU (Neubig at CMU)' — confirmed accurate by full PDF."
  - id: rlm-paper-deep-dive
    type: wiki
    file: wiki/sources/tools-integration/src-rlm-paper-deep-dive-table-1-training-recipe-six-observations.md
    description: "RLM paper deep-dive — uses OOLONG `trec_coarse` split (synth, 132K) as Table 1 task; also introduces OOLONG-Pairs as their own modification (20 new pair-aggregation queries). RLM(GPT-5) achieves 56.5% on OOLONG vs base GPT-5's 44.0%; on OOLONG-Pairs, RLM(GPT-5) 58.0% vs base 0.1%."
  - id: rlm-empirical-findings
    type: wiki
    file: wiki/sources/tools-integration/src-rlm-empirical-findings-oolong-browsecomp-rlm-qwen3-8b.md
    description: "RLM blogpost-level findings — sources the 114% relative improvement headline (RLM(GPT-5-mini) > GPT-5 by 34 points on OOLONG `trec_coarse` 132K)"
  - id: anti-vendor-lock-in-lesson
    type: wiki
    file: wiki/lessons/01_drafts/anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence.md
    description: "Mission framing — Evidence 6 (Evaluation layer: 4 public benchmarks define the task class) is grounded by this Layer 1 reading on the OOLONG side"
  - id: rlm-qwen3-6-27b-operations-plan
    type: wiki
    file: wiki/domains/cross-domain/rlm-qwen3-6-27b-fine-tune-operations-plan.md
    description: "Operations plan — Step 6 evaluation uses OOLONG and OOLONG-Pairs as 2 of the 4 evaluation surfaces. This synth grounds the benchmark structure and reference target numbers."
  - id: oolong-github
    type: documentation
    url: https://github.com/abertsch72/oolong
    title: "abertsch72/oolong (GitHub)"
    description: "Public eval harness; ensures reproducibility per the wiki's anti-vendor-lock-in mission"
  - id: oolong-huggingface-synth
    type: documentation
    url: https://huggingface.co/oolongbench/oolong-synth
    title: "OOLONG-synth dataset (Hugging Face)"
  - id: oolong-huggingface-real
    type: documentation
    url: https://huggingface.co/oolongbench/oolong-real
    title: "OOLONG-real dataset (Hugging Face)"
  - id: critical-role-crd3
    type: paper
    url: https://aclanthology.org/2020.acl-main.459/
    title: "Critical Role Dungeons and Dragons Dataset (Rameshkumar & Bailey, ACL 2020)"
    description: "Source of the OOLONG-real transcripts — first 115 episodes of Critical Role campaign 1"
  - id: critrolestats
    type: documentation
    url: https://www.critrolestats.com/
    title: "CritRoleStats fan project"
    description: "Source of OOLONG-real gold answers (per-episode dice rolls + spells cast statistics, fan-annotated)"
tags: [oolong, oolong-synth, oolong-real, long-context-aggregation, cmu, neubig, bertsch, gormley, mitamura, pratapa, dnd-evaluation, critical-role, crd3, critrolestats, frontier-models-fail-50pct, deepseek-r1-pathology, gemini-recitation-filter, gpt-5, claude-sonnet-4, gemini-2-5-pro, reasoning-effort-counterintuition, label-aggregation-not-bottleneck, identification-aggregation-bottleneck, temporal-reasoning-hardest, in-context-learning-datasets, exponential-partial-credit-scoring, prompt-caching, mission-2026-04-27, anti-vendor-lock-in, rlm-eval-source, paper-deep-dive, paper-pdf-layer-1]
---

# Synthesis — OOLONG Paper Deep Dive

## Summary

The arXiv 2511.02817 v1 paper PDF (4 Nov 2025; 28 pages with Appendix; 1250-line raw scrape) supplies the full empirical detail that the [combined OOLONG + LongBench Pro abstract-level synthesis](src-oolong-and-longbench-pro-long-context-benchmarks-rlm-anchors.md) compressed into a single column. **5 authors at Carnegie Mellon University Language Technologies Institute** — Amanda Bertsch (lead, NSF GRFP-supported), Adithya Pratapa, Teruko Mitamura, Graham Neubig, Matthew R. Gormley — all `@cs.cmu.edu`. The benchmark's distinguishing claim from the abstract — frontier models <50% at 128K on aggregation tasks — is grounded by a **2-split design**: **OOLONG-synth** built from 10 in-context learning datasets (Spam, TREC-QC, AGNews, App Reviews, Pavlick Formality, IMDB, HiTZ Negation, Yahoo Topics, MultiNLI, Metaphors) with date+user-ID metadata enabling temporal/distributional/user-aggregation question types; and **OOLONG-real** from Critical Role D&D campaign 1 (115 episodes, [Rameshkumar & Bailey CRD3 dataset](https://aclanthology.org/2020.acl-main.459/)) with gold answers from the [CritRoleStats fan project](https://www.critrolestats.com/) — first benchmark to use fan-annotated game-state statistics as evaluation gold. **Table 4 — full 9-model leaderboard with per-context-length stratification** (8K-128K for synth, 55K-175K for real) ranks GPT-5 first on average (synth 70.75, real 47.00) but reveals **Gemini-2.5-Pro is best on real (52.95)** while dropping below-random at 256K synth (Gemini API returns 0 on max-token overrun + "recitation" filter triggers on IMDB-content reciting). **DeepSeek-R1 exhibits a striking pathology**: strong on OOLONG-real (32.00) but BELOW RANDOM on OOLONG-synth (13.11) — 60% of R1's traces don't provide an answer, 64% end mid-sentence, 17% debate task tractability, 4% refuse. **Reasoning-effort ablation is counter-intuitive**: high reasoning effort helps at SHORT contexts only; at 256K on synth, high reasoning slightly UNDERPERFORMS low. **Label-providing ablation isolates the bottleneck**: providing gold labels in-context yields only 0.79-10.9 abs points improvement — the bottleneck is aggregation/identification, NOT labeling. **No model exceeds 85% at any context length, even at 1K-4K tokens**. **Mission-relevant**: this synth grounds the OOLONG side of the [anti-vendor-lock-in lesson Evidence 6](../../lessons/01_drafts/anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence.md), the 2-of-4 evaluation surfaces in [RLM-Qwen3.6-27B operations plan Step 6](../../domains/cross-domain/rlm-qwen3-6-27b-fine-tune-operations-plan.md), and the load-bearing 114% improvement headline from the [RLM blogpost-level findings](src-rlm-empirical-findings-oolong-browsecomp-rlm-qwen3-8b.md).

## Reference Card

> [!info] Paper deep-dive reference card

| Field | Value |
|---|---|
| **Paper** | arXiv 2511.02817 v1, dated 4 Nov 2025 (cs.CL) |
| **Length** | 28 pages with Appendix · 1250-line raw scrape |
| **Authors (5, all CMU LTI)** | Amanda Bertsch (lead) · Adithya Pratapa · Teruko Mitamura · Graham Neubig · Matthew R. Gormley — `{abertsch, vpratapa, teruko, gneubig, mgormley}@cs.cmu.edu` |
| **Funding** | Lead author Bertsch supported by **NSF Graduate Research Fellowship Program Grant DGE2140739** |
| **Affiliations confirmed** | Carnegie Mellon University, Language Technologies Institute (LTI) — abstract-level synth's "(Neubig at CMU)" inference confirmed accurate |
| **GitHub** | github.com/abertsch72/oolong (eval harness, public) |
| **HuggingFace** | huggingface.co/oolongbench/oolong-synth + huggingface.co/oolongbench/oolong-real (data, public) |
| **Sub-benchmarks** | **OOLONG-synth** (8 test datasets + 2 validation, naturalistic synthetic) + **OOLONG-real** (Critical Role D&D campaign 1, fan-annotated gold) |
| **OOLONG-synth source datasets** | 10 ICL datasets: Spam · TREC-QC-coarse · AGNews · App Reviews · Pavlick Formality · IMDB · HiTZ Negation · Yahoo Topics · MultiNLI · Metaphors |
| **OOLONG-synth question types** | **Counting** (label distribution properties) · **User** (cross-reference user IDs, Pareto-distributed 80/20) · **Timeline** (date-based queries — most challenging) |
| **OOLONG-synth context lengths** | Powers of 2 from **1K to 4M tokens** |
| **OOLONG-synth scale** | 400 questions per context length × multiple context lengths · 2 context windows × 25 questions × 8 test datasets · sample with replacement to fill distribution |
| **OOLONG-real source** | [CRD3 dataset](https://aclanthology.org/2020.acl-main.459/) — Critical Role TV series Campaign 1, **115 episodes**, average 55K tokens/episode |
| **OOLONG-real gold source** | [CritRoleStats](https://www.critrolestats.com/) fan project — per-episode dice rolls + spells cast statistics |
| **OOLONG-real question categories** | **Rolls** (16 templates) + **Spells** (15 templates) for single-episode; expanded for multi-episode (1-24 episodes, **55K-1.3M tokens**) |
| **Numerical scoring formula** | **`score(ŷ) = 0.75^\|y-ŷ\|`** — exponential partial credit decreasing with absolute error |
| **Models in main leaderboard** | 9: GPT-5 · GPT-5-mini · GPT-5-nano · o3 · o4-mini · Claude-Sonnet-4 · Gemini-2.5-Pro · DeepSeek-R1 · Llama-4-Maverick |
| **Top average (synth + real)** | **GPT-5: 70.75 / 47.00** = 58.88 avg |
| **Top OOLONG-synth** | **GPT-5: 70.75** (avg over 8K-128K) |
| **Top OOLONG-real** | **Gemini-2.5-Pro: 52.95** (avg over 55K-175K) |
| **Below-random on synth** | **DeepSeek-R1: 13.11** (random baseline = ~23 by paper construction) |
| **Frontier ceiling at 128K synth** | <50% across all models — **GPT-5 = 46.36**, Claude-Sonnet-4 = 48.02, all others lower |
| **Performance ceiling at any length** | **No model exceeds 85% at any context length** — even at 1K-4K (paper §4.5 short-context regime) |
| **Released** | Yes — data + evaluation harness public on HuggingFace + GitHub |
| **Confidence** | high — full paper PDF read (lines 1-1250) including: §1 introduction · §2 OOLONG-synth construction with all 10 datasets and question types · §3 OOLONG-real construction with CRD3 lineage · §4 leaderboard (Table 4) + 4 ablations (reasoning effort, question type, label-providing, short-context, R1 pathology) · §5 related works positioning · Appendix A example failed/passed validation per dataset (Tables 5-14) · Appendix B full question templates (Tables 15-19) · Appendix C R1 trace examples (Figures 6-7) |
| **Mission relevance** | Critical — grounds the headline 114% improvement number from RLM blogpost; Step 6 of [RLM-Qwen3.6-27B operations plan](../../domains/cross-domain/rlm-qwen3-6-27b-fine-tune-operations-plan.md) targets OOLONG and OOLONG-Pairs as 2 of 4 evaluation surfaces |

## Key Insights

1. **The benchmark's framing is explicit anti-NIAH/RULER** (paper §1): *"existing long-context evaluations... tend to rely on retrieval from one or more sections of the context, which allows nearly all of the context tokens to be disregarded as noise. This represents only one type of task that might be performed with long context."* OOLONG positions itself as testing **information aggregation across the FULL context**, where all tokens contribute to the answer — making it complementary, not redundant, to RULER/HELMET/MRCR.

2. **OOLONG-synth's 10 source datasets** are old, well-vetted, simple ICL benchmarks. The choice is methodological: each individual classification task is **easy for both humans and models** — the difficulty is in **aggregating** results, not in the underlying task. By construction, the benchmark measures aggregation capability cleanly. **Filtering**: the authors run zero-shot ICL with GPT-4.1-nano + Llama-4-Maverick and exclude examples both fail (% removed: 0.000% to 0.635% per dataset — Table 2). This screens out mislabeled or unusually hard examples that would propagate as noise across many questions.

3. **The Pareto-distributed user IDs are a deliberate design choice**: per paper §2.2, *"User IDs are drawn such that 80% of instances have an ID in the 20% of IDs that are most common."* This forces models to identify dominant users (User questions like "which user is represented most often?") in a realistic skew distribution, not a uniform one. The 80/20 ratio matches typical real-world frequency distributions.

4. **The 25-questions-per-context-window design enables prompt caching** (paper §2.2). This is critical for reproducibility cost: each context (large) is reused for 25 questions (small), so API costs scale with question count rather than context-tokens × questions. The wiki's [pipeline.py provider-check](../../spine/references/provider-pricing-monitoring-operations-plan.md) tracks API costs at this granularity — a similar architectural choice (cache the expensive part) applies to RLM evaluations.

5. **OOLONG-real's choice of D&D transcripts is clever in 3 ways**:
   - **Naturalistic**: real conversational data, not synthetic
   - **Hard to memorize**: D&D play is improvised live, not in pretraining data
   - **Fan-curated gold answers**: CritRoleStats fans annotate per-episode dice rolls + spells cast — gold labels exist without authors having to construct them
   - **Cannot be trivially decomposed**: unlike OOLONG-synth where the task COULD be solved by labeling each example then aggregating, OOLONG-real has cross-turn coreference and conversational ambiguity that resists simple decomposition

6. **The numerical scoring formula `score(ŷ) = 0.75^|y-ŷ|`** is structurally interesting. It gives:
   - Score 1.0 for exact match (`|y-ŷ| = 0`)
   - Score 0.75 for off-by-1
   - Score 0.5625 for off-by-2
   - Score 0.42 for off-by-3
   - Score ~0 for off-by-15+
   
   This is **exponential partial credit** — much more forgiving than exact-match alone, but penalizes wrong-by-orders-of-magnitude harshly. **The wiki's source-synthesis ratio gate (≥0.25 line ratio to raw)** is a different example of structural-credit-design — both papers and this wiki use partial-credit formulas to enable graceful degradation rather than binary pass/fail.

7. **Table 4's leaderboard reveals 3 distinct model failure modes**:
   - **Llama-4-Maverick fails both splits** (synth 16.37, real 2.07) — across-the-board incapability for this task class
   - **DeepSeek-R1 fails ONLY on synth** (13.11 vs real 32.00) — task-class-specific failure
   - **Gemini-2.5-Pro is best on real but drops on long synth** — API/filter-specific failure mode (max-token cutoff + recitation filter)
   
   These are diagnostically distinct — different failure modes have different fixes. Llama needs better long-context training; R1 needs better reasoning-budget management; Gemini needs API/filter handling.

8. **The R1 pathology is the most striking finding** (paper §4.4). Authors prompt GPT-5-nano to label 2,400 R1 traces:
   - **60% don't provide an answer at all**
   - **64% end in incomplete sentence** (run out of output tokens)
   - **17% spend at least some time debating whether the task is impossible/intractable**
   - **4% refuse to respond completely**
   
   Hypothesis: R1's strategy of "label every example before deciding which are relevant" is fatal at long contexts — it consumes all output token budget on labeling and never gets to the aggregation step. **Figure 6 shows a real example**: R1 starts classifying NLI pairs 1-by-1, the trace cuts off at item 20 with "this could be neutral. However, note that the first lists shopping areas..." mid-sentence. The model never reaches the actual aggregation question.
   
   **Mission relevance**: this is exactly the pathology RLM-Qwen3-8B is trained to avoid (per [RLM paper Observation 5](src-rlm-paper-deep-dive-table-1-training-recipe-six-observations.md): per-model prompt tuning is required, especially for context-window awareness). RLM's REPL substrate would let R1 chunk + recurse rather than enumerate.

9. **The reasoning-effort ablation is counter-intuitive** (paper §4.2, Figure 3). For GPT-5-nano:
   - Short context (8K-32K): high reasoning effort helps substantially
   - Medium context (64K): little discernible difference
   - **Long context (256K on synth)**: high reasoning slightly UNDERPERFORMS low
   
   Authors hypothesize: at lengths where there's "sufficient remaining room in the context window to enumerate labels for each example", high reasoning encourages an enumeration strategy that exhausts context — same pathology as DeepSeek-R1 in degraded form. **Operational implication**: high-reasoning modes are NOT free — at long contexts they can hurt. This contradicts the assumption "more thinking is always better."

10. **Question-type difficulty stratification** (paper §4.3, Figure 4):
    - **Counting questions**: easiest across all models
    - **User questions**: middle difficulty
    - **Timeline questions**: hardest — temporal reasoning is the bottleneck
    - **Date/month-year answer types** show greater spread + lower performance
    - Gap between GPT-5 and GPT-5-nano is **>4× larger** for date-output questions vs label-output questions
    
    **Operational implication for AICP routing**: temporal reasoning tasks should route to the strongest available model OR to RLM-augmented inference; the GPT-5-vs-GPT-5-nano accuracy gap is much wider on this question class.

11. **Aggregation-without-classification ablation isolates the bottleneck** (paper §4.5, Figure 5). Provide gold labels for each ICL example in-context — task reduces to "identify relevant + sum":
    - Improvement: 0.79 to 10.9 absolute points for GPT-5
    - **Improvement NOT consistently larger at longer inputs** → performance degradation at long context is NOT primarily mislabeling accumulation
    - **Improvement NOT larger for GPT-5-nano vs GPT-5** → performance gap is NOT classification-ability difference
    
    **Conclusion** (paper): *"the lower performance at longer context lengths is not primarily due to an accumulation of mislabeling errors... the ability to aggregate information is the main capability we aim to measure."* The bottleneck is **identification + aggregation**, not labeling. This matters for the wiki's anti-vendor-lock-in mission: pure model-quality improvements won't close the gap on long-context aggregation; **paradigm changes (like RLM's REPL recursion) are needed**.

12. **Short-context ceiling exists** (paper §4.5, Figure 5b). At 1K-4K tokens:
    - Top models converge to similar performance (~85% ceiling)
    - **No model exceeds 85% at any context length** including the shortest
    
    **Operational implication**: even at trivial context lengths, ~15% of OOLONG-synth questions are inherently hard for current models. This is NOT a long-context-only problem — it's an aggregation-capability problem that gets worse with length.

13. **Gemini 2.5 Pro pathology has 2 distinct mechanisms** (paper §4.4):
    - **Max-token-cutoff during reasoning**: Gemini API returns 0 tokens (NOT a partial output) when max-token-count exceeded during reasoning → automatic 0 score on long synth
    - **Recitation filter**: Gemini's safety filter triggers on IMDB-style content (which is in pretraining data), returning empty output
    - Neither triggers on OOLONG-real (D&D transcripts not heavily memorized) — Gemini stays strong there
    
    **Operational implication**: model-vs-API distinction matters. Gemini-2.5-Pro the LM is capable; Gemini-2.5-Pro the API has guardrails that hurt benchmark scores. Real deployments may experience these guardrails too. **Mission-load-bearing for AICP routing**: when scoring providers, distinguish "model failed" from "API filtered."

14. **OpenAI long-context prompting guide compliance is built-in** (paper §2.2). Instructions provided at start AND end of input (per OpenAI guidance), question only at end (enables prompt caching). This is a structured-context-design choice the wiki's [model-context-engineering](../../spine/models/depth/model-context-engineering.md) page tracks — placement of instructions within long inputs is itself a P2-relevant decision.

15. **OOLONG complements rather than duplicates RULER/HELMET/ZeroSCROLLS/etc.** Per §5 related works positioning:
    - **RULER**: synthetic retrieval with multi-hop tracing — different complexity class (retrieval vs aggregation)
    - **HELMET**: extends RULER to downstream tasks — complementary
    - **MRCR**: multi-round coreference resolution — different task
    - **ZeroSCROLLS Amazon-review-percentage task**: closest conceptual ancestor of OOLONG-synth aggregation
    - **GSM-infinite**: math-reasoning at scale — orthogonal to OOLONG's naturalistic-text aggregation
    - **MoNaCo**: agentic retrieval — disjoint
    
    **The benchmark is designed to fill a gap, not duplicate existing efforts.** This matters for the [anti-vendor-lock-in lesson Evidence 6](../../lessons/01_drafts/anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence.md): the 4 RLM Table 1 benchmarks are NOT redundant — they span 4 distinct complexity classes.

16. **The Goldman et al. 2024 dispersion+scope taxonomy** (cited paper §5):
    - **Dispersion**: HIGH for OOLONG (relevant info distributed over full context length)
    - **Scope**: HIGH for OOLONG (most input necessary, particularly for OOLONG-synth)
    
    Per the taxonomy, OOLONG occupies the hardest quadrant (high-dispersion + high-scope). This is structurally different from NIAH-style benchmarks (low-dispersion + low-scope) and explains why frontier models struggle here while saturating elsewhere.

17. **DataCit chain — the 10 source ICL datasets** are themselves canonical NLP benchmarks with their own citation lineages:
    - Spam (Almeida et al. 2011)
    - TREC-QC-coarse (Li & Roth 2002, Hovy et al. 2001)
    - AGNews (Zhang et al. 2015)
    - App Reviews (2017)
    - Pavlick Formality (Lahiri 2015, Pavlick & Tetreault 2016)
    - IMDB reviews (Maas et al. 2011)
    - HiTZ Negation (García-Ferrero et al. 2023)
    - Yahoo Topics (Zhang et al. 2015)
    - MultiNLI (Williams et al. 2018)
    - Metaphors (Bizzoni & Lappin 2018)
    
    By choosing well-vetted ICL datasets, the authors ensure underlying-task quality is not the variable being measured. **Methodological rigor**: this is the same pattern as BrowseComp+'s 14-annotator × 400-hour verification effort — both papers spend significant care on baseline-task quality so the long-context-aggregation difficulty is the actual variable under test.

## Deep Analysis

### Paper Structure (28 pages, 6 main sections + Appendices A-C)

| Section | Pages | Content |
|---|---|---|
| 1. Introduction | 1-2 | Anti-NIAH framing; multi-step aggregation as the missing capability |
| 2. OOLONG-synth | 2-5 | Dataset selection (Table 1), filtering (Table 2), context construction, 3 question types, evaluation methodology with random baseline + scoring + iterative-solution discussion |
| 3. OOLONG-real | 4-5 | CRD3 + CritRoleStats lineage; 31 question templates split single-episode + multi-episode; evaluation parsing + scoring |
| 4. Results and Analysis | 5-9 | Table 4 leaderboard + Figures 2-5; 5 sub-analyses (reasoning effort, question type, real-vs-synth differences, R1 pathology, simpler settings) |
| 5. Related Work | 9-10 | Long-context benchmarks (RULER/HELMET/MRCR/ZeroSCROLLS/etc.) · D&D in NLP · aggregation-as-NLP-concept |
| 6. Conclusion | 10 | Substantial headroom remaining; open weights vs API gap |
| Appendix A | 14-22 | ICL label validation — 10 datasets, examples that failed/passed validation (Tables 5-14) |
| Appendix B | 22-26 | Full question template tables (15-19) for synth + real |
| Appendix C | 27-28 | DeepSeek R1 trace examples (Figures 6-7) |

### Table 4 — Main Leaderboard (Section 4.1)

> [!info] Full per-context-length stratification
>
> | Model | Synth Avg | 8K | 16K | 32K | 64K | 128K | Real Avg | 55K | 118K | 175K |
> |---|---|---|---|---|---|---|---|---|---|---|
> | **GPT-5** | **70.75** | 85.56 | 84.45 | 76.12 | 61.24 | 46.36 | 47.00 | 58.74 | 45.72 | 36.53 |
> | **Gemini-2.5-Pro** | 55.29 | **88.13** | 69.84 | 56.83 | 36.56 | 25.06 | **52.95** | **60.12** | **50.81** | **47.93** |
> | **o3** | 62.37 | 86.80 | 79.52 | 63.23 | 44.86 | 37.45 | 36.71 | 50.57 | 33.57 | 25.99 |
> | GPT-5-mini | 63.68 | 85.13 | 77.65 | 64.64 | 50.14 | 40.85 | 34.55 | 49.86 | 29.90 | 23.89 |
> | **Claude-Sonnet-4** | 58.18 | 74.43 | 62.75 | 55.67 | 50.04 | **48.02** ← beats GPT-5 here | 36.75 | 50.58 | 32.98 | 26.70 |
> | o4-mini | 56.74 | 83.07 | 65.10 | 51.86 | 44.15 | 39.53 | 27.13 | 41.69 | 21.77 | 17.93 |
> | GPT-5-nano | 50.73 | 70.96 | 54.53 | 47.81 | 41.02 | 39.31 | 31.05 | 43.09 | 26.82 | 23.23 |
> | **DeepSeek-R1** | **13.11** ← below random! | 13.94 | 13.65 | 12.91 | 13.20 | 11.87 | 32.00 | 47.85 | 27.35 | 20.81 |
> | Llama-4-Maverick | 16.37 | 15.00 | 16.29 | 15.42 | 16.35 | 18.80 | 2.07 | 2.48 | 2.11 | 1.62 |

**Three patterns visible**:
1. **GPT-5 best on synth average** (70.75) but **Claude-Sonnet-4 beats GPT-5 at 128K specifically** (48.02 vs 46.36) — only frontier model that doesn't degrade as steeply
2. **Gemini-2.5-Pro best on real overall** (52.95, robust at 175K = 47.93) but tank below 25% at 256K synth (not in this table — discussed in §4.4)
3. **DeepSeek-R1's synth performance is essentially flat at ~13%** across all context lengths — pathological (random baseline ≈ 23%, so R1 underperforms random by 10 absolute points)

### OOLONG-synth Construction (Section 2)

> [!info] Stage 1 — Dataset selection (Table 1)
>
> 10 datasets, 8 test + 2 validation. **Label-space reduction** for sentiment/formality datasets (>2 labels collapsed to 2) reduces task difficulty. Per-instance length 39-376 Llama-2 tokens including added date+user metadata.

> [!info] Stage 2 — Validation filtering (Table 2)
>
> Models used for filter: **GPT-4.1-nano + Llama-4-Maverick** (chosen for being NOT substantially stronger than evaluation models). Zero-shot ICL with minimal label-space-and-task-type instruction. Examples both models get wrong → excluded.
>
> Removal rates: 0.000% (Metaphors) to 0.635% (Spam). Datasets with web-scraped labels (Yahoo Topics, AGNews, IMDB, App Reviews) generally have higher rates — likely genuine mislabels from user-error.

> [!info] Stage 3 — Context construction
>
> - **500K tokens** average context per estimate (using Llama-2 tokenizer)
> - Determine number of examples by 95% target context fill
> - **Sample distribution over labels** so model can't guess from prior knowledge of typical balance
> - Sample with replacement if needed
> - **User IDs**: 80% of instances have IDs in 20% most-common (Pareto distribution)
> - **Dates**: uniform with replacement over ~40-month range, MM/DD/YYYY format
> - **25 questions per context window** for prompt-caching efficiency
> - **2 context windows × 50 questions × 8 datasets = 400 questions per context length**
> - **Powers of 2 from 1K to 4M** evaluated

### OOLONG-real Construction (Section 3)

> [!info] Source pipeline
>
> 1. **CRD3 dataset** (Rameshkumar & Bailey 2020) provides Critical Role campaign 1 transcripts (115 episodes, full episode transcripts with player-name labels)
> 2. **CritRoleStats fan project** provides per-episode statistics on dice rolls + spells cast
> 3. Authors construct question templates that aggregate over those statistics
> 4. Single-episode questions: 16 roll templates + 15 spell templates (Tables 18, 19)
> 5. Multi-episode questions: extended for 1-24 episodes with delimiters between transcripts
> 6. Context: **55K-1.3M tokens** (single episode = 55K average)
>
> **First benchmark to use fan-annotated game-state stats as gold labels** for capability evaluation (per §5).

### Question Types — Increasing Complexity

> [!abstract] OOLONG-synth question difficulty hierarchy
>
> | Type | What it tests | Tables |
> |---|---|---|
> | **Counting** | Label distribution properties — most/least common, frequency comparison, label count | Table 15 (4 templates) |
> | **User** | Cross-reference user IDs with labels — most-frequent user, subset queries, user-with-most-of-label | Table 16 (8 templates) |
> | **Timeline** | Temporal reasoning — frequency by date/month/year, before-vs-after-date comparisons, label-frequency-shift over time | Table 17 (12 templates, **most complex**) |
>
> Difficulty grows because temporal queries require **reasoning about temporal relationships** rather than just matching identifiers. Per Figure 4: across all models, timeline questions show lowest accuracy.

### Random Baseline Algorithm (§2.3)

> [!info] Non-trivial random baseline because output spaces vary
>
> | Question type | Random strategy |
> |---|---|
> | n-way label choice | Uniform random from valid label set |
> | Numerical answer | Return N/\|L\| (data points / label space size) |
> | Date / user ID | Uniform random from in-context list |
>
> Computed as expected value over the dataset. **Estimated ~23%** (paper doesn't give exact number; DeepSeek-R1's 13.11 is below this).

### Reasoning-Effort Ablation (§4.2, Figure 3)

> [!warning] **Counter-intuitive finding**: more reasoning ≠ always better
>
> For GPT-5-nano with 3 reasoning levels (low / default / high):
> - **8K-32K**: high reasoning effort > default > low (expected pattern)
> - **64K**: little discernible difference
> - **128K**: little discernible difference
> - **256K (synth)**: **high reasoning slightly UNDERPERFORMS low** (pathology zone)
>
> **Hypothesis** (paper): at lengths where there's "sufficient remaining room in the context window to enumerate labels for each example", adding more reasoning effort encourages the enumeration strategy — which exhausts context. Low-reasoning effort skips this and just goes to aggregation directly.
>
> **Operational implication**: the wiki should NOT default to high-reasoning modes for long-context tasks. AICP routing logic should consider reasoning-effort × context-length interaction.

### DeepSeek-R1 Pathology Deep-Dive (§4.4)

> [!bug]- **The R1 trace analysis is the paper's most striking sub-finding**
>
> Authors prompt GPT-5-nano to label 2,400 randomly sampled R1 traces from OOLONG-synth (the failure regime, 13.11 score):
>
> | Pathology | Frequency |
> |---|---|
> | No answer at all | **60%** |
> | Trace ends in incomplete sentence | **64%** |
> | Spends time debating task tractability | 17% |
> | Refuses to respond completely | 4% |
>
> **Figure 6 shows a real R1 trace** on an MNLI aggregation task with 21 NLI pairs. R1 starts: *"\<think\> We are given 21 pairs. We need to classify each pair as one of 'neutral', 'contradiction', or 'entailment'. Then, we will count the frequency..."* It then classifies pairs 1-2-3-...-19-20 in detail, runs out of tokens at item 20 with the trace cut off mid-sentence: *"...However, note that the first lists shopping areas, which might include shoe stores, but it doesn't specify. The second is too..."*. The aggregation step never happens.
>
> **In contrast, on OOLONG-real**, the same model handles the task because real questions don't require enumerating 21+ items — they require focused identification (e.g., "What is the second spell cast?") which fits in budget.
>
> **Mission relevance**: R1's enumeration strategy is exactly the failure mode RLM-paradigm post-training avoids (per [RLM paper Observation 5](src-rlm-paper-deep-dive-table-1-training-recipe-six-observations.md): per-model prompt tuning required, especially context-window awareness). RLM-Qwen3-8B's training recipe explicitly programs FINAL/FINAL_VAR contracts so the root LM doesn't lose itself in enumeration.

### Aggregation-Without-Classification Ablation (§4.5, Figure 5a)

> [!info] **Provide gold labels in-context — does it help?**
>
> Method: include each ICL example's ground-truth label inline. Task reduces to: "identify relevant examples + sum the occurrences of each label."
>
> Results for GPT-5 + GPT-5-nano:
> - Improvement: **0.79 to 10.9 absolute points** (highly variable)
> - **NOT consistently larger at longer inputs** → degradation isn't from mislabel accumulation
> - **NOT larger for GPT-5-nano than GPT-5** → gap isn't from classification ability differences
>
> **Conclusion**: aggregation/identification IS the bottleneck, not labeling. **Implication for the wiki's anti-vendor-lock-in mission**: if labels can't fix the gap, neither will training models to be better classifiers. Paradigm changes (RLM's REPL substrate) ARE needed.

### Short-Context Regime (§4.5, Figure 5b)

> [!info] **Even at 1K-4K tokens, the task is hard**
>
> - Top models converge to similar performance (~85% ceiling)
> - **NO model exceeds 85% at any context length, including the shortest**
> - Differences between top models become difficult to distinguish
>
> **Implication**: OOLONG-synth has structural difficulty independent of context length. The benchmark measures aggregation capability, not just long-context capability. This is methodologically important — the benchmark isolates the right variable.

### Gemini 2.5 Pro Pathology Mechanisms (§4.4)

> [!bug]- **Two distinct API/safety failure modes**
>
> 1. **Max-token-cutoff during reasoning**: Gemini API returns ZERO TOKENS (not partial output) when max-token-count exceeded during reasoning. Other APIs return whatever was generated so far. This causes automatic 0 scores on long-context inputs where Gemini's reasoning trace overflows.
>
> 2. **Recitation filter**: Gemini's safety filter triggers on substantial regurgitation of pretraining data. Some OOLONG-synth source datasets (especially IMDB movie reviews) are widely-distributed on the web and present in pretraining. Filter triggers occasionally on long synth contexts → empty output → 0 score.
>
> **Neither mechanism triggers on OOLONG-real** (D&D transcripts not heavily memorized) — Gemini stays strong there (52.95 average, best on real).
>
> **Operational implication for AICP**: model capability vs API behavior are distinguishable concerns. A "Gemini-2.5-Pro failed" report might actually be "Gemini API truncated" or "Gemini filter triggered." Smart routing should distinguish.

### Differences Between Synth and Real Splits (§4.4)

> [!info] **Why Gemini and DeepSeek-R1 behave differently across splits**
>
> | Pattern | Synth | Real |
> |---|---|---|
> | Iterative-decomposable | Yes (label each ICL example then aggregate) | No (cross-turn coreference, conversational) |
> | API filter trigger likelihood | High (IMDB/YahooAnswers content) | Low (D&D play not heavily memorized) |
> | R1 enumeration pathology | Severe (60% no-answer) | Mild (real questions are focused, not enumeration-heavy) |
> | Gemini API behavior | Triggers max-token + recitation | Cleaner |
>
> **The two splits stress models differently** — they're complementary, not redundant. Authors recommend evaluating on both for a full picture.

### Why This Matters for the Wiki's Mission

> [!success] **Evidence 6 of [anti-vendor-lock-in lesson](../../lessons/01_drafts/anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence.md) is now Layer 1 on the OOLONG side**
>
> The lesson's Evidence 6 cites the 4 RLM Table 1 benchmarks as "public, released with evaluation harnesses, reproducible." This synth grounds the OOLONG side at full PDF depth: 2 splits, 10 ICL source datasets, full question template tables (15-19), 9-model leaderboard with per-context-length breakdown, public GitHub + HuggingFace.
>
> **The empirical evidence chain at the evaluation-layer is auditable end-to-end** at full Layer 1 for OOLONG.

> [!success] **The 114% improvement headline (RLM blogpost) is grounded against this benchmark's empirical baselines**
>
> The blogpost's load-bearing claim: RLM(GPT-5-mini) outperforms base GPT-5 by 34 points on OOLONG `trec_coarse` 132K. **From this paper**: GPT-5 = 46.36 at 128K. **From RLM Table 1**: RLM(GPT-5) = 56.5% on OOLONG (full average). Both numbers are now traceable to specific paper rows. The headline isn't aspirational anymore — it's anchored to specific Tables on specific benchmarks.

> [!success] **Step 6 of [RLM-Qwen3.6-27B operations plan](../../domains/cross-domain/rlm-qwen3-6-27b-fine-tune-operations-plan.md) target numbers are grounded**
>
> The plan's Step 6 evaluation table cites OOLONG and OOLONG-Pairs as 2 of 4 RLM Table 1 benchmarks. **Reference targets** (from RLM paper Table 1): RLM(GPT-5) on OOLONG = 56.5%, RLM(Qwen3-Coder-480B) = 48.0%, RLM-Qwen3-8B = 32.0%. Plan's hypothetical RLM-Qwen3.6-27B target: ≥45% (between 8B and 480B). **This synth grounds the benchmark structure**: 8 test ICL datasets, 25 questions × 2 windows × 8 datasets = 400 questions per context length, evaluation harness on GitHub.

> [!warning] **The R1 pathology informs RLM-Qwen3.6-27B fine-tune design choices**
>
> R1's enumeration strategy fails at long context — the model labels every example before deciding which are relevant, exhausting tokens. **Operations plan Step 4** (programmatic FINAL/FINAL_VAR fix) directly addresses this: the RLM training recipe filters out trajectories where the model fails to signal completion. Qwen3-Coder-480B as teacher had 16% bad-FINAL + 13% bad-FINAL_VAR rates per [RLM paper](src-rlm-paper-deep-dive-table-1-training-recipe-six-observations.md). RLM-Qwen3.6-27B fine-tune must do the same filtering — **the R1 pathology is the failure mode the recipe is designed to avoid**.

> [!info] **The reasoning-effort × context-length counter-intuition has direct AICP-routing implications**
>
> Per Finding 9: high reasoning effort is NOT free — at long contexts, it can hurt by encouraging enumeration strategies. **AICP smart-routing should NOT default to high-reasoning modes for long-context inputs**. The wiki's [tier-0 candidate comparison](../../comparisons/rlm-qwen3-8b-vs-qwen3-6-27b-tier-0-long-context-candidate.md) routing logic might benefit from a context-length-vs-reasoning-effort decision dimension.

> [!info] **Gemini-2.5-Pro distinction (model vs API) is operationally important**
>
> Per Finding 13: Gemini-2.5-Pro the LM is capable; Gemini-2.5-Pro the API has 2 distinct failure modes (max-token zero-return + recitation filter). **AICP backend integration should account for API-specific behaviors** — not all "Gemini failed" outcomes are model-capability failures. This applies broadly: Anthropic's Claude APIs, OpenAI's o-series APIs, and Google's Gemini APIs all have distinct failure modes that smart-routing should distinguish.

## Open Questions

> [!question] What's the relationship between OOLONG `trec_coarse` and OOLONG-Pairs?
> The RLM paper Table 1 uses both. `trec_coarse` is one of the 8 test datasets in OOLONG-synth (TREC-QC-coarse, 6 labels). OOLONG-Pairs is RLM authors' own derivative — 20 new pair-aggregation queries built on top of OOLONG-synth's `trec_coarse` data. **Implication**: OOLONG-Pairs is RLM-paper-specific, NOT in the original OOLONG benchmark. When deploying OOLONG eval for AICP/wiki use, the RLM paper's Appendix D.1 has the 20 OOLONG-Pairs queries; the GitHub eval harness may or may not include them. (Requires: harness inspection.)

> [!question] How does OOLONG-real handle multi-episode delimiter design?
> Paper §3.1 says concatenated transcripts use "delimiters to highlight the start and end of each transcript." The exact delimiter format isn't shown in the paper. (Requires: GitHub eval harness inspection.)

> [!question] Is the 0.75^|y-ŷ| scoring formula's exponential base optimal?
> Paper presents the formula without theoretical justification. Other reasonable choices: 0.5^|y-ŷ| (harsher), 0.9^|y-ŷ| (more lenient), or absolute-error-based. (Requires: ablation experiment if benchmark adoption is wide enough to motivate.)

> [!question] How does R1 perform on OOLONG with longer max-output tokens?
> The 60% no-answer rate is hypothesized to come from output-token budget exhaustion. If the budget were doubled (or 10×), would R1's strategy succeed? (Requires: re-running the benchmark with extended budgets.)

> [!question] Could the wiki's `pipeline post` synthesis quality use OOLONG-style aggregation evaluation?
> The wiki has source-syntheses with hundreds of references and multiple-document content. Aggregation tasks (summarize all references citing X; count entities) over wiki source content could become a wiki-internal regression suite. (Requires: synthesis + corpus design.)

> [!question] Why doesn't GPT-5-mini outperform GPT-5 at long contexts on OOLONG-synth, given the RLM blogpost's headline?
> RLM blogpost: RLM(GPT-5-mini) > GPT-5 by 34 points on `trec_coarse` 132K — that's at +28% RELATIVE. **This paper's Table 4**: GPT-5-mini base = 40.85 at 128K, GPT-5 base = 46.36 at 128K. **The +34-point gain is from RLM-wrapping, not from GPT-5-mini being intrinsically better than GPT-5.** This synth confirms the headline mechanism: RLM provides a paradigm shift; the cheaper model isn't intrinsically better, it's better-wrapped.

> [!question] Could OOLONG be extended to non-English ICL datasets?
> Currently English-only. The Pavlick Formality + IMDB datasets are English-only. Extending to LongBench Pro's bilingual coverage (English + Chinese) would require Chinese ICL datasets + re-running validation. (Requires: corpus design + annotator effort.)

## Applicability

> [!info] Where to use OOLONG findings directly
>
> - **Long-context reasoning + aggregation evaluation** for any LLM
> - **Reasoning-effort × context-length interaction analysis** when picking inference parameters
> - **Model-vs-API distinction validation** when scoring providers (Gemini case study)
> - **Pathological failure mode diagnosis** for reasoning-trained models (R1 case study)
> - **Iterative-vs-aggregation task class taxonomy** when designing evaluation suites
> - **D&D-domain capability evaluation** for naturalistic long-conversation tasks

> [!warning] Where these findings DON'T apply
>
> - **NIAH-style retrieval tasks** — OOLONG explicitly contrasts with retrieval-only benchmarks
> - **Multilingual tasks** — English-only
> - **Code-specific evaluation** — none of the 10 source datasets are code; LongBench v2 CodeQA covers code
> - **Real-time / streaming** — offline batch benchmark
> - **Visual / multimodal** — text-only
> - **Tasks where iterative-decomposition is acceptable/desirable** — OOLONG-synth is decomposable but the benchmark is designed for single-pass evaluation

## Relationships

- BUILDS ON: [[src-oolong-and-longbench-pro-long-context-benchmarks-rlm-anchors|OOLONG + LongBench Pro Combined Synthesis]] (this is the dedicated Layer-1 deep-dive expanding on OOLONG specifics that the combined synth covered at abstract level; CMU affiliation confirmed accurate)
- COMPARES TO: [[src-rlm-paper-deep-dive-table-1-training-recipe-six-observations|RLM Paper Deep Dive]] (RLM paper used OOLONG `trec_coarse` split as primary evaluation surface AND introduced OOLONG-Pairs as their own derivative)
- COMPARES TO: [[src-rlm-empirical-findings-oolong-browsecomp-rlm-qwen3-8b|RLM Empirical Findings]] (sources the 114% improvement headline; this synth grounds the underlying numbers in OOLONG paper Tables)
- COMPARES TO: [[src-browsecomp-plus-paper-deep-dive-fixed-corpus-table-1-oracle-citation-quality|BrowseComp+ Paper Deep Dive]] (parallel Layer-1 deep-dive on a different RLM Table 1 benchmark; both use rigorous methodology — BrowseComp+ via 14 annotators × 400 hours, OOLONG via filtering with weak ICL models)
- COMPARES TO: [[src-longbench-pro-paper-deep-dive-1500-samples-46-models-three-findings|LongBench Pro Paper Deep Dive]] (parallel Layer-1 deep-dive; LongBench Pro's "long-context optimization > parameter scaling" finding aligns with OOLONG's "label-providing doesn't fix gap" finding — both point to paradigm-level changes being needed, not just better models)
- DEMONSTRATES: [[infrastructure-over-instructions-for-process-enforcement|Principle 1]] (OOLONG's filtering pipeline + 25-questions-per-window + non-trivial random baseline are structural enforcement of evaluation rigor)
- DEMONSTRATES: [[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4]] (the "frontier models effectively use long context" claim was aspirational until OOLONG measured it; result: <50% at 128K)
- DEMONSTRATES: [[anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence|Anti-Vendor-Lock-In Lesson]] § Evidence 6 (the evaluation-layer empirical anchor on the OOLONG side; the lesson's claim "all 4 RLM Table 1 benchmarks public + reproducible" is grounded by this Layer 1 reading)
- DEMONSTRATES: [[right-process-for-right-context-the-goldilocks-imperative|Principle 3 — Goldilocks]] (different reasoning-effort modes for different context lengths — the counter-intuitive finding that high reasoning underperforms at long contexts is exactly Goldilocks-applicable: process must adapt to context size)
- RELATES TO: [[2026-consumer-hardware-ai-stack|2026 Consumer Hardware AI Stack]] (frontier-model failure at 128K aggregation tasks is part of the empirical case for paradigm-level alternatives like RLM at the tier-0 candidate level)
- RELATES TO: [[ai-infrastructure-decision-framework-2026|AI Infrastructure Decision Framework 2026]] (the model-vs-API distinction informs routing decisions; reasoning-effort × context-length interaction informs inference-parameter routing)
- FEEDS INTO: [[rlm-qwen3-6-27b-fine-tune-operations-plan|RLM-Qwen3.6-27B Operations Plan]] § Step 6 (OOLONG and OOLONG-Pairs are 2 of 4 evaluation surfaces; this synth grounds the reference targets and benchmark structure)
- FEEDS INTO: [[rlm-thread-evidence-chain-2026-04-27|Learning Path — RLM Thread Evidence Chain]] (Path C: Reproduce Training — this synth is the deep-dive reference for the OOLONG evaluation surface)

## Backlinks

[[OOLONG + LongBench Pro Combined Synthesis]]
[[src-rlm-paper-deep-dive-table-1-training-recipe-six-observations|RLM Paper Deep Dive]]
[[src-rlm-empirical-findings-oolong-browsecomp-rlm-qwen3-8b|RLM Empirical Findings]]
[[BrowseComp+ Paper Deep Dive]]
[[src-longbench-pro-paper-deep-dive-1500-samples-46-models-three-findings|LongBench Pro Paper Deep Dive]]
[[infrastructure-over-instructions-for-process-enforcement|Principle 1]]
[[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4]]
[[Anti-Vendor-Lock-In Lesson]]
[[right-process-for-right-context-the-goldilocks-imperative|Principle 3 — Goldilocks]]
[[2026 Consumer Hardware AI Stack]]
[[ai-infrastructure-decision-framework-2026|AI Infrastructure Decision Framework 2026]]
[[rlm-qwen3-6-27b-fine-tune-operations-plan|RLM-Qwen3.6-27B Operations Plan]]
[[Learning Path — RLM Thread Evidence Chain]]
