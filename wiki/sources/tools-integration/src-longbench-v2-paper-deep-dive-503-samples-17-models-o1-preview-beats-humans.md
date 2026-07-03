---
title: "Synthesis — LongBench v2 Paper Deep Dive: 503-Sample Multi-Choice Benchmark, 6×20 Task Taxonomy, 17-Model Leaderboard, o1-Preview Beats Humans by 4%, RAG + Memorization + YaRN Ablations (Tsinghua + Zhipu.AI; arXiv 2412.15204 v2, Jan 2025)"
aliases:
  - "LongBench v2 Paper Deep Dive"
  - "LongBench v2 Tables 1-5"
  - "LongBench v2 17 Models"
  - "LongBench v2 o1-preview Beats Humans"
type: source-synthesis
domain: tools-integration
status: synthesized
confidence: high
maturity: seed
created: 2026-04-27
updated: 2026-04-27
last_reviewed: 2026-04-27
sources:
  - id: longbench-v2-paper-pdf
    type: paper
    url: https://arxiv.org/pdf/2412.15204
    file: raw/papers/longbench-v2-towards-deeper-understanding-and-reasoning-on-realistic-long-contex.md
    title: "LongBench v2 arXiv 2412.15204 v2 (3 Jan 2025) — Full PDF"
    description: "26 pages with Appendix; 1703-line raw scrape. Authors: Yushi Bai*, Shangqing Tu* (equal contribution), Jiajie Zhang, Hao Peng, Xiaozhi Wang, Xin Lv, Shulin Cao, Jiazheng Xu, Lei Hou, Yuxiao Dong, Jie Tang, Juanzi Li. Affiliations: Tsinghua University (1) + Zhipu.AI (2). Project page: longbench2.github.io. Code: github.com/THUDM/LongBench."
    ingested: 2026-04-27
  - id: longbench-v2-abstract-companion
    type: wiki
    file: wiki/sources/tools-integration/src-browsecomp-plus-and-longbench-v2-rlm-table-1-benchmarks.md
    description: "Abstract-level companion synthesis covering BrowseComp+ AND LongBench v2 together at Layer 0/1; this page is the dedicated Layer-1 deep-dive on LongBench v2 alone, sourced from the full PDF rather than the abstract page. Combined synth speculation 'Tsinghua-affiliated likely (Tang, Li are well-known names)' confirmed by full PDF."
  - id: longbench-original
    type: paper
    url: https://arxiv.org/abs/2308.14508
    title: "LongBench (Bai et al., 2023) — original benchmark this version 2 succeeds"
    description: "First in the LongBench family — bilingual multitask benchmark by the same Tsinghua THUDM group (lead author Yushi Bai)."
  - id: longbench-pro-related
    type: wiki
    file: wiki/sources/tools-integration/src-longbench-pro-paper-deep-dive-1500-samples-46-models-three-findings.md
    description: "LongBench Pro (Chen et al. Jan 2026, IIE-CAS + Beihang + Xiaohongshu) is a DIFFERENT team's parallel benchmark in the LongBench family — distinct from LongBench v2's Tsinghua/Zhipu provenance. Both share the LongBench naming convention but are independent research efforts."
  - id: rlm-paper-deep-dive
    type: wiki
    file: wiki/sources/tools-integration/src-rlm-paper-deep-dive-table-1-training-recipe-six-observations.md
    description: "RLM paper deep-dive — uses LongBench v2's CodeQA subtask (50 entries, 167k median, multi-file code repo understanding) as the CodeQA split in Table 1. RLM(GPT-5) achieves 62.0% on CodeQA vs base GPT-5's 24.0%."
  - id: anti-vendor-lock-in-lesson
    type: wiki
    file: wiki/lessons/01_drafts/anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence.md
    description: "Mission framing — Evidence 6 (Evaluation layer: 4 public benchmarks define the task class) is grounded by this Layer 1 reading on the LongBench v2 side"
  - id: rlm-qwen3-6-27b-operations-plan
    type: wiki
    file: wiki/domains/cross-domain/rlm-qwen3-6-27b-fine-tune-operations-plan.md
    description: "Operations plan — Step 6 evaluation uses LongBench v2 CodeQA split as 1 of 4 evaluation surfaces. This synth grounds the benchmark structure and reference target numbers."
  - id: longbench-v2-github
    type: documentation
    url: https://github.com/THUDM/LongBench
    title: "THUDM/LongBench GitHub repository"
    description: "Public eval code (THUDM = Tsinghua University Data Mining group); ensures reproducibility per the wiki's anti-vendor-lock-in mission. Same repo hosts both LongBench v1 and v2 evaluation code."
  - id: longbench-v2-projectpage
    type: documentation
    url: https://longbench2.github.io
    title: "LongBench v2 project page"
  - id: gpqa-google-proof
    type: paper
    url: https://arxiv.org/abs/2311.12022
    title: "GPQA: A Graduate-Level Google-Proof Q&A Benchmark (Rein et al., 2023)"
    description: "Source of the 'Google-proof' verification methodology — search for the answer on Google for 15 minutes; if not findable, the data is Google-proof. LongBench v2's 70-sample audit applies this methodology — 67/70 (96%) Google-proof"
tags: [longbench-v2, long-context-benchmark, multiple-choice, 6-task-categories, 20-subtasks, code-repo-qa, code-repository-understanding, long-icl, kalamang, zhuang, agent-history-qa, knowledge-graph-reasoning, table-qa, detective-novel-qa, event-ordering, tsinghua, zhipu-ai, jie-tang, juanzi-li, yushi-bai, o1-preview, gpt-4o, claude-sonnet-3-5, glm-4-plus, qwen2-5, llama-3, mistral-large, cohere-command-r, thinking-paradigm, cot-effect, rag-saturation-32k, memorization-check, yarn-ablation, google-proof-verification, rlm-codeqa-split, mission-2026-04-27, anti-vendor-lock-in, paper-deep-dive, paper-pdf-layer-1]
---

# Synthesis — LongBench v2 Paper Deep Dive

## Summary

The arXiv 2412.15204 v2 paper PDF (3 Jan 2025; 26 pages with Appendix; 1703-line raw scrape) supplies the full empirical detail that the [combined BrowseComp+ + LongBench v2 abstract-level synthesis](src-browsecomp-plus-and-longbench-v2-rlm-table-1-benchmarks.md) compressed into a single column. **12 authors at Tsinghua University + Zhipu.AI** — equal-contribution leads Yushi Bai + Shangqing Tu, senior authors Juanzi Li + Lei Hou + Jie Tang + Yuxiao Dong (Tsinghua THUDM/AI faculty). Combined synth speculation "Tsinghua-affiliated likely (Tang, Li are well-known names)" is **confirmed accurate** by full PDF — Tsinghua-led, Zhipu.AI-co-affiliated. Distinct provenance from [LongBench Pro](src-longbench-pro-paper-deep-dive-1500-samples-46-models-three-findings.md) (Chen et al., IIE-CAS + Beihang + Xiaohongshu) despite shared "LongBench" name. The benchmark's distinguishing claims from the abstract — 503 challenging multiple-choice questions, 8K-2M words context range, human experts 53.7% under 15 min, o1-preview 57.7% surpassing humans by 4% — are grounded by **Table 1's full taxonomy** (6 categories × 20 subtasks with per-subtask data count + median length + expert accuracy + solving time), **Table 2's 17-model leaderboard with per-difficulty + per-length stratification** (10 open-source + 7 proprietary, both zero-shot AND CoT), **5-stage construction pipeline** (Document Collection → Annotation → 3-LLM Automated Review → Human-Expert Manual Review → Data Revision with max 5 rewrites), **97-annotator + 24-expert workforce** at **100,000 CNY total cost over 2+ months** (~$14k USD for 503 samples). **Three load-bearing empirical findings**: (1) **scaling test-time compute beats parameter scaling** — o1-preview vs GPT-4o = +7.6%, o1-mini vs GPT-4o-mini = +8.5%, average CoT improvement on open-source = +3.4%; (2) **RAG saturates at 32K retrieval context** — Qwen2.5/GLM-4-Plus peak at 32K; only GPT-4o effectively uses 128K but still falls -0.6% below its non-RAG full-context score; (3) **memorization is minimal for tasks II/III/VI but measurable for tasks I/V** (Single-Doc QA + Code Repository) — likely from training-data overlap. **70-sample author audit confirms 97% correctness + 96% Google-proof** (using GPQA Rein et al. 2023 methodology). **Mission-relevant**: this synth grounds the LongBench v2 side of [[anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence|anti-vendor-lock-in lesson Evidence 6]], the Code Repo QA split that is RLM Table 1's CodeQA task ([RLM(GPT-5) = 62.0% vs base GPT-5 = 24.0%](src-rlm-paper-deep-dive-table-1-training-recipe-six-observations.md)), and the o1-preview-beats-humans-by-4-points headline that anchors the thinking-paradigm narrative throughout the wiki's [tier-0 candidate comparison](../../comparisons/rlm-qwen3-8b-vs-qwen3-6-27b-tier-0-long-context-candidate.md). **With this synthesis, all 4 RLM Table 1 benchmarks (BrowseComp+, OOLONG, LongBench Pro, LongBench v2 CodeQA) are now at Layer 1 / full PDF confidence in the wiki — the evaluation-layer evidence chain is complete.**

## Reference Card

> [!info] Paper deep-dive reference card

| Field | Value |
|---|---|
| **Paper** | arXiv 2412.15204 v2, dated 3 Jan 2025 (cs.CL); v1 19 Dec 2024 |
| **Length** | 26 pages with Appendix · 1703-line raw scrape |
| **Authors (12)** | **Yushi Bai\*** (lead) · **Shangqing Tu\*** (equal contribution) · Jiajie Zhang · Hao Peng · Xiaozhi Wang · Xin Lv · Shulin Cao · Jiazheng Xu · Lei Hou · Yuxiao Dong · **Jie Tang** · **Juanzi Li** |
| **Affiliations** | (1) **Tsinghua University** · (2) **Zhipu.AI** (Xin Lv + Shulin Cao at Zhipu.AI; rest at Tsinghua) |
| **Lineage confirmed** | Combined synth speculation "Tsinghua-affiliated likely" CORRECT. Distinct from [LongBench Pro](src-longbench-pro-paper-deep-dive-1500-samples-46-models-three-findings.md)'s IIE-CAS + Beihang + Xiaohongshu lineage despite shared name. |
| **Project page** | https://longbench2.github.io |
| **Code** | github.com/THUDM/LongBench (THUDM = Tsinghua University Data Mining; same repo hosts v1 + v2) |
| **Total samples** | **503** (192 Easy + 311 Hard) |
| **Languages** | English only (limitation explicitly acknowledged §6) |
| **Context length range** | **8K-2M words** (median 54k · average 104k) |
| **Length distribution** | 180 Short (<32k) · 215 Medium (32k-128k) · 108 Long (>128k) |
| **Task taxonomy** | **6 categories × 20 subtasks** |
| **6 categories** | I. Single-Doc QA (175) · II. Multi-Doc QA (125) · III. Long ICL (81) · IV. Long-dialogue History (39) · **V. Code Repo Understanding (50)** · VI. Long Structured Data (33) |
| **Construction pipeline** | 5 stages: Document Collection → Data Annotation → Automated Review (3 LLMs) → Manual Review (24 experts) → Data Revision (max 5 rewrites) |
| **Annotator workforce** | **97 annotators** (Bachelor 47% / Master 29% / PhD 24%; CS 29% / Law 24% / Economics 22%; ages 20-26 mostly) + **24 long-context experts** (subset) |
| **Reward structure** | Base 100 CNY/passed sample · length bonus +20/+40/+50 (32-64k/64-128k/>128k) · difficulty bonus +50 CNY · reviewer 25 CNY/sample |
| **Total cost** | **100,000 CNY (~$14,000 USD)** over **2+ months** |
| **Quality audit (70 samples)** | 68/70 (97%) correct · 67/70 (96%) Google-proof per [GPQA methodology](https://arxiv.org/abs/2311.12022) |
| **Reject rate during construction** | 4% illegal question · 7% insufficient difficulty · 4% wrong answer |
| **Models in main leaderboard (Table 2)** | **17** (10 open-source + 7 proprietary), all 128K+ context window (Claude-3.5-Sonnet 200K) |
| **Top thinking model** | **o1-preview-2024-09-12 = 57.7%** overall (CoT 56.2%) — surpasses 53.7% human baseline by **+4%** |
| **Top non-thinking model** | **GPT-4o-2024-08-06 = 50.1%** zero-shot · 51.2% CoT |
| **Top open-source** | **Qwen2.5-72B-Instruct = 39.4%** zero-shot · 38.8% CoT |
| **Top Chinese closed-source** | **GLM-4-Plus = 44.3%** zero-shot · 46.1% CoT |
| **CoT effect** | Open-source avg +3.4%; o1-preview vs GPT-4o = **+7.6%**; o1-mini vs GPT-4o-mini = **+8.5%** |
| **YaRN ablation** | Qwen2.5-7B 27.0→30.0% (+3.0); Qwen2.5-72B 39.4→42.1% (+2.7); larger benefit on >32k + CoT |
| **RAG saturation point** | 32K retrieval (Qwen2.5/GLM-4-Plus); only GPT-4o uses 128K effectively, but -0.6% vs no-RAG full-context |
| **Memorization without context** | Most models 25-30% (random); GPT-4o 33.1% (some training-data leakage); minimal on tasks II/III/VI; measurable on I/V |
| **Per-length-interval pattern** | Short (<32k): top models +15.4% above human · Medium (32k-128k): top model -5.6% below human · Long (>128k): top model +4% above human |
| **Per-task pattern** | Models par/above human on Single-Doc + Multi-Doc QA · LARGEST gap on Long Structured Data (V & VI) · o1-preview superior on Multi-Doc QA + Long ICL + Code Repo |
| **Question types EXCLUDED** | Counting (>10 items) · simple retrieval · overly professional · tricky/deliberate · visual-dependent |
| **Released** | Yes — eval code public on GitHub (THUDM/LongBench) |
| **Confidence** | high — full paper PDF read (lines 1-1703) including: §1 introduction · §2 related works (categorizes 18+ prior benchmarks) · §3 task framework + 5-stage construction · §4 evaluation with Tables 2-5 + Figures 3-4 · §5 conclusion · §6 limitations · Appendix A author contributions · Appendix B 20-subtask descriptions with example questions · Appendix C annotator statistics + screenshots of platform · Appendix D evaluation prompts (zero-shot + CoT) · Appendix E YaRN + compensated results |
| **Mission relevance** | Critical — Code Repo QA subtask = RLM Table 1's CodeQA split; o1-preview-beats-humans finding anchors thinking-paradigm narrative across wiki; Step 6 of [RLM-Qwen3.6-27B operations plan](../../domains/cross-domain/rlm-qwen3-6-27b-fine-tune-operations-plan.md) evaluates against this benchmark |

## Key Insights

1. **The combined synth's "Tsinghua-affiliated likely" speculation is confirmed accurate** by full PDF authorship: equal-contribution leads Yushi Bai (Tsinghua) + Shangqing Tu (Tsinghua), senior authors Jie Tang + Juanzi Li + Lei Hou + Yuxiao Dong all Tsinghua. Xin Lv + Shulin Cao at Zhipu.AI (Tsinghua-spinoff company that develops the GLM models). **Provenance distinct from [LongBench Pro](src-longbench-pro-paper-deep-dive-1500-samples-46-models-three-findings.md)** which is IIE-CAS + Beihang + Xiaohongshu — different team despite shared "LongBench" naming convention. Two parallel research efforts in the long-context-benchmark space, both Chinese-academic-led.

2. **The 6-task × 20-subtask taxonomy is more granular than the abstract revealed** (Table 1). Each of 6 categories has 1-7 subtasks with **per-subtask data count + median word length + expert accuracy + median solving time** — methodologically rigorous specification.

3. **Code Repository Understanding is one of the longest subtasks** (167k median tokens, only 1 subtask of 50 entries). Difficulty: 44% expert accuracy, 6.4 min median solving time. Question shape (per Appendix B): *"For the current Megatron-LM framework, if I want to use the THD data format while enabling Context Parallel, how should I modify the experiments for rotary_pos_embedding?"* — production-engineering depth, not toy code-comprehension. **This is the RLM Table 1 CodeQA split.** RLM(GPT-5) = 62.0% on this benchmark per [RLM paper](src-rlm-paper-deep-dive-table-1-training-recipe-six-observations.md).

4. **Long In-context Learning has a Kalamang/Zhuang translation subtask** (20 entries, 132K median — longest median of any subtask). Tests **learning to translate an unseen low-resource language from a vocabulary book** — citing [Tanzer et al. 2024](https://openreview.net/forum?id=tbVWug9f2h) (Kalamang) + Zhang et al. 2024a (Zhuang). This is a *generative* benchmark hidden inside a multiple-choice format — translate a sentence, multi-choice over candidate translations.

5. **Detective novel + Event ordering subtasks are notable** (within Single-Doc QA):
   - **Detective**: 22 entries, 70K median, **64% expert accuracy** — requires inferring killer/motive from novel context. Citing [Xu et al. 2024 DetectiveQA](https://arxiv.org/abs/2409.02465).
   - **Event ordering**: 20 entries, 96K median, **75% expert accuracy** — order 4 plot events from a novel by timeline. Highest expert accuracy of any Single-Doc subtask but lowest model accuracy gap (humans good at narrative timelines).

6. **The construction pipeline is methodologically robust**: 5 stages with explicit acceptance criteria + reject categories + max-5-revisions cycle. Per §3.4: 4% rejected as illegal question · 7% as insufficient difficulty · 4% as wrong answer. **Total reject rate ~15%** during construction — high enough to indicate rigorous filtering, low enough to indicate annotators understood the task.

7. **The 100,000 CNY (~$14,000 USD) total cost over 2+ months is methodologically transparent** — a feature, not a bug. Compared to [LongBench Pro's 1500 samples](src-longbench-pro-paper-deep-dive-1500-samples-46-models-three-findings.md) (no total cost disclosed but 63 annotators × 50 RMB/hr × hours × samples implies a similar magnitude), and [BrowseComp+'s 14 annotators × 400+ hours](src-browsecomp-plus-paper-deep-dive-fixed-corpus-table-1-oracle-citation-quality.md) (cost not disclosed), LongBench v2's transparency on cost provides a **reproducibility budget benchmark** for similar future construction efforts.

8. **The 70-sample author audit at 96-97% correctness** uses the [GPQA Rein et al. 2023](https://arxiv.org/abs/2311.12022) Google-proof methodology — search Google for 15 minutes; if answer not findable → Google-proof. **3% error rate** is acknowledged as the empirical floor; conclusions hold above this noise level.

9. **Table 2 — Full 17-model leaderboard with per-difficulty + per-length stratification**:
   - **Open-source clusters around 27-39%** with Qwen2.5-72B-Instruct = 39.4% best, GLM-4-9B-Chat = 30.2% lowest
   - **Proprietary non-thinking clusters around 41-50%** with GPT-4o = 50.1% best, GPT-4o-mini = 29.3% (smaller-tier)
   - **Proprietary thinking: o1-preview = 57.7%** (Outlier — surpasses humans), o1-mini = 37.8%
   - **Claude-3.5-Sonnet-2024-10-22 = 41.0%** (zero-shot), 46.7% CoT (+5.7% from CoT — substantial)
   - **GLM-4-Plus = 44.3%** zero-shot — best Chinese closed-source

10. **CoT effect quantified**:
   - Open-source models: average **+3.4%** improvement under CoT
   - Mistral-Large-Instruct-2407: **+7.0%** (26.6→33.6%)
   - Llama-3.1-70B-Instruct: **+4.6%** (31.6→36.2%)
   - **Strongest scaling-test-time-compute signal**: o1-preview vs GPT-4o = **+7.6%** (50.1→57.7%); o1-mini vs GPT-4o-mini = **+8.5%** (29.3→37.8%)
   - **CoT does NOT help all models equally** — e.g., Qwen2.5-72B drops from 39.4 zero-shot to 38.8 CoT (the only DECLINE)

11. **Per-length-interval performance is highly task-distribution-dependent** (paper §4.1 footnote): models do NOT show monotonic decline with length because tasks differ across length ranges. **Authors explicitly recommend per-interval comparisons** rather than aggregate length comparisons. **GPT-4o on Short (<32k): ~53.3%** vs **Long (>128k): 40.2%** — declines, but Short tasks include Single-Doc QA which is comparatively easier; Long tasks include Code Repo + Multi-Doc QA which are harder. **Methodological note**: per-interval comparison is the correct way to interpret length-stratified results in this benchmark.

12. **Per-task patterns reveal distinct capability profiles** (Figure 3, Table 3):
   - **Single-Doc QA + Multi-Doc QA**: Models par or surpass humans (these are document-extractive-style)
   - **Largest gap on Long Structured Data (Tables + KGs)**: Models trained more on document-data than structured-data
   - **o1-preview shows superior performance on Multi-Doc QA + Long ICL + Code Repo** with substantial leads — thinking-paradigm helps most on complex composite tasks
   - **GPT-4o w/o context = 33.1% on Code Repo (V)**: indicates **some training-data overlap** for code repositories (possibly seen during pretraining)

13. **RAG ablation reveals retrieval saturation at 32K**:
   - Method: chunk to 512 tokens (GLM-4-9B tokenizer), encode with Zhipu Embedding-3, retrieve top-N (N = 4, 8, 16, 32, 64, 128, 256), concatenate in original order
   - **Qwen2.5 + GLM-4-Plus**: peak at 32K retrieval, no benefit beyond
   - **Only GPT-4o effectively uses 128K retrieval** but still **-0.6% below its non-RAG full-context score**
   - **Conclusion (paper §4.2)**: questions cannot be solved by retrieval alone — they require deep understanding + reasoning. **Direct refutation of "RAG-can-replace-long-context" framing.**

14. **Memorization check (Table 3) reveals which tasks are training-data-leakage-vulnerable**:
   - Without context, most models 25-30% (≈ random for 4-option multi-choice)
   - **Tasks II (Multi-Doc QA), III (Long ICL), VI (Long Structured Data)**: minimal memorization
   - **Tasks I (Single-Doc QA), V (Code Repo)**: measurable memorization — likely from common documents/repos in pretraining
   - **GPT-4o w/o context overall = 33.1%**, indicating some training-data leakage exists but bounded
   - **Implication**: when comparing models, prefer tasks II/III/VI for cleanest capability measurement

15. **YaRN ablation confirms long-context fine-tuning helps Qwen2.5** (Table 4):
   - Qwen2.5-7B-Instruct: 27.0% → 30.0% (+3.0% absolute) with YaRN scaling factor 4.0
   - Qwen2.5-72B-Instruct: 39.4% → 42.1% (+2.7% absolute)
   - **YaRN benefit larger on >32k samples** (Medium + Long subsets)
   - **YaRN has larger impact under CoT setting** — paper notes "the underlying reasons for this remain unclear"
   - **Implication for the wiki's mission**: long-context fine-tuning IS a free lunch at the open-source side — Qwen2.5+YaRN closes ~3 absolute points to GLM-4-Plus closed-source levels

16. **Author contributions disclosed (Appendix A)** — methodologically transparent:
   - Project lead: Yushi Bai (also lead author on original LongBench, [LongAlign](https://arxiv.org/abs/2401.18058), [LongCite](https://arxiv.org/abs/2409.02897), [LongWriter](https://arxiv.org/abs/2408.07055))
   - Benchmark design: 7 contributors
   - Annotation platform built specifically for this benchmark by Tu + Bai
   - Supervision + fundraising: Juanzi Li, Lei Hou, Jie Tang, Yuxiao Dong (senior Tsinghua AI faculty)

17. **Limitations explicitly acknowledged (§6)** with specificity:
   - **Size**: 503 may be too small for stable evaluation against statistical noise; 100K CNY + 2 months precluded scaling further
   - **Language**: English-only acknowledged
   - **Length distribution per task**: tasks concentrated at specific lengths; per-interval comparisons recommended over aggregate

18. **Distinct from LongBench v1 (the family's first paper)**: v1 was bilingual (English + Chinese) and used metrics like F1 and ROUGE; v2 is English-only with multiple-choice format for evaluation reliability. The team's evolution: F1/ROUGE judged unreliable → multiple-choice with verifiable correctness. **This validates [Principle 1](../../lessons/04_principles/hypothesis/infrastructure-over-instructions-for-process-enforcement.md) at the metric design level**: evaluation metrics should be structurally verifiable (multi-choice with single correct answer), not subjective (F1/ROUGE/LLM-as-judge with biases per Bai et al. 2024c + Ye et al. 2024).

## Deep Analysis

### Paper Structure (26 pages, 6 main sections + Appendices A-E)

| Section | Pages | Content |
|---|---|---|
| 1. Introduction | 1-2 | Motivation: existing benchmarks fail to test deep understanding · 4 design goals (Length / Difficulty / Coverage / Reliability) · headline numbers (53.7% expert / 50.1% direct-answer / 57.7% o1-preview) |
| 2. Related Work | 2-3 | 18+ prior benchmarks categorized · existing-benchmark issues (lack-of-deep-reasoning · unreliable-metrics) · multiple-choice rationale |
| 3. Task and Construction | 3-7 | 6 task categories × 20 subtasks · 5-stage data collection · data verification · data statistics |
| 4. Evaluation | 7-9 | 17-model leaderboard (Table 2) · RAG ablation (Figure 4) · memorization check (Table 3) |
| 5. Conclusion | 9 | Brief summary |
| 6. Limitations | 9 | Size · language · length distribution per task |
| Appendix A | 14 | Author contributions disclosed |
| Appendix B | 14-21 | Full 20-subtask descriptions with example questions |
| Appendix C | 21-24 | Annotator statistics (97 annotators) + platform screenshots |
| Appendix D | 24-25 | Evaluation prompts (zero-shot + CoT) |
| Appendix E | 25-26 | YaRN results + compensated results |

### Table 1 — Full Task Taxonomy

> [!info] All 20 subtasks with per-subtask statistics (paper §3.1, Table 1)
>
> | Cat | Subtask | Source | #data | Length | Expert Acc | Expert Time |
> |---|---|---|---|---|---|---|
> | I.1 | Academic | Paper, textbook | 44 | 14k | 50% | 7.3 min |
> | I.2 | Literary | Novel | 30 | 72k | 47% | 8.5 min |
> | I.3 | Legal | Legal doc | 19 | 15k | 53% | 13.1 min |
> | I.4 | Financial | Financial report | 22 | 49k | 59% | 9.0 min |
> | I.5 | Governmental | Gov report | 18 | 20k | 50% | 9.5 min |
> | I.6 | Detective | Detective novel | 22 | 70k | 64% | 9.3 min |
> | I.7 | Event ordering | Novel | 20 | 96k | **75%** | 9.4 min |
> | **I total** | Single-Doc QA | | **175** | 51k | 55% | 8.9 min |
> | II.1 | Academic | Papers, textbooks | 50 | 27k | 22% | 6.1 min |
> | II.2 | Legal | Legal docs | 14 | 28k | 64% | 8.8 min |
> | II.3 | Financial | Financial reports | 15 | 129k | 40% | 7.0 min |
> | II.4 | Governmental | Gov reports | 23 | 89k | 22% | 6.0 min |
> | II.5 | Multi-news | News | 23 | 15k | 61% | 5.3 min |
> | **II total** | Multi-Doc QA | | **125** | 34k | **36%** | 6.1 min |
> | III.1 | User guide QA | Electronic device, software | 40 | 61k | 63% | 9.9 min |
> | III.2 | New language translation | Vocab book (Kalamang, Zhuang) | 20 | **132k** | **75%** | 5.4 min |
> | III.3 | Many-shot learning | Multi-class classification | 21 | 71k | 52% | 8.0 min |
> | **III total** | Long ICL | | **81** | 71k | 63% | 8.3 min |
> | IV.1 | Agent history QA | LLM agent conversations | 20 | 13k | 70% | 8.3 min |
> | IV.2 | Dialogue history QA | User-LLM conversation | 19 | 77k | **89%** | 6.5 min |
> | **IV total** | Long-dialogue History | | **39** | 25k | **79%** | 8.2 min |
> | **V.1** | **Code repo QA** | **Code repository** | **50** | **167k** | **44%** | **6.4 min** |
> | **V total** | **Code Repo Understanding** | | **50** | **167k** | **44%** | 6.4 min |
> | VI.1 | Table QA | Table | 18 | 42k | 61% | 7.4 min |
> | VI.2 | KG reasoning | KG subgraph | 15 | 52k | **87%** | 6.2 min |
> | **VI total** | Long Structured Data | | **33** | 49k | 73% | 6.4 min |

**Pattern observations**:
- **Hardest for humans**: Multi-Doc Academic (22% expert acc) + Multi-Doc Governmental (22%)
- **Easiest for humans**: Dialogue history QA (89%) · Knowledge graph reasoning (87%) · Event ordering (75%)
- **Longest median**: Code repo QA (167k) · New language translation (132k) · Multi-doc Financial (129k)
- **Multi-Doc QA average expert accuracy = 36%** is striking — humans struggle here, multi-document reasoning is genuinely hard

### 5-Stage Construction Pipeline

> [!info] Stage 1 — Document Collection (paper §3.2)
>
> - **Annotator-uploaded** rather than designer-defined documents — naturalistic
> - Tools: PyMuPDF for PDF→text conversion
> - **Auto-rejection criteria**: length <8,192 words OR high overlap with existing annotations
> - Document categories per task type: papers, textbooks, novels, legal docs, financial reports, government reports, code repos, KGs

> [!info] Stage 2 — Data Annotation (paper §3.2)
>
> - Multiple-choice question with 4 options + groundtruth + supporting evidence
> - **Forbidden question types** (per Appendix C.3 guideline):
>   1. Counting questions (>10 items)
>   2. Simple retrieval questions
>   3. Overly professional questions (require external/specialty knowledge)
>   4. Tricky questions (deliberately difficult)
>   5. Visual-dependent questions (require looking at pictures)
> - **Per-annotator cap**: 20 questions max — diversity constraint

> [!info] Stage 3 — Automated Review (paper §3.2)
>
> - **3 LLMs** answer the question: GPT-4o-mini + GLM-4-Air + GLM-4-Flash (all 128K context)
> - If all 3 correct → too easy → reject + revise
> - **Hard set definition**: ≥2/3 LLMs WRONG ⇒ counts as hard data → eligible for difficulty bonus

> [!info] Stage 4 — Manual Review (paper §3.2)
>
> - **24 long-context experts** (subset of 97 annotators, recruited based on major + year of study)
> - Reviewer downloads documents + attempts to answer with timer
> - **Too easy criterion**: human expert correct in <3 minutes → reject + revise
> - **Too hard criterion**: human expert can respond "I don't know" after 15 minutes (8% of total test data)
> - Reviewer also flags illegal questions (mismatched task type, requires external knowledge, etc.)

> [!info] Stage 5 — Data Revision (paper §3.2)
>
> - Annotator revises rejected data based on 3 reject categories:
>   1. Illegal question (rejected by reviewer for non-compliance)
>   2. Insufficient difficulty (failed automated OR <3-min human)
>   3. Wrong answer (reviewer disputes groundtruth)
> - **Maximum 5 revision cycles** — terminate if not passing after 5 attempts

### Reward Structure (paper §3.2 mechanism design)

> [!info] **Annotator economics — full disclosure**
>
> | Component | Amount |
> |---|---|
> | Base reward (passed data) | **100 CNY** |
> | Length bonus 8-32k | 0 CNY |
> | Length bonus 32-64k | +20 CNY |
> | Length bonus 64-128k | +40 CNY |
> | Length bonus >128k | +50 CNY |
> | Difficulty bonus (hard set) | +50 CNY |
> | Reviewer reward per data | 25 CNY |
> | **Total project cost** | **~100,000 CNY ($14,000 USD)** |
> | Project duration | **2+ months** |
>
> Quality control: random checks on reviews; reviewers whose checks repeatedly fail have ALL rewards revoked. **Methodological strength**: aligned incentives — annotators benefit from longer + harder data; reviewers benefit from accurate review.

### Table 2 — 17-Model Leaderboard (Section 4.1)

> [!info] Open-source models
>
> | Model | Zero-shot | CoT | Easy | Hard | Short | Medium | Long |
> |---|---|---|---|---|---|---|---|
> | GLM-4-9B-Chat | 30.2 | 30.8 | 30.7→34.4 | 29.9→28.6 | 33.9→35.0 | 29.8→30.2 | 25.0→25.0 |
> | Llama-3.1-8B-Instruct | 30.0 | 30.4 | 30.7→36.5 | 29.6→26.7 | 35.0→34.4 | 27.9→31.6 | 25.9→21.3 |
> | Llama-3.1-70B-Instruct | 31.6 | 36.2 | 32.3→35.9 | 31.2→36.3 | 41.1→45.0 | 27.4→34.0 | 24.1→25.9 |
> | Llama-3.3-70B-Instruct | 29.8 | 36.2 | 34.4→38.0 | 27.0→35.0 | 36.7→45.0 | 27.0→33.0 | 24.1→27.8 |
> | Llama-3.1-Nemotron-70B-Inst. | 31.0 | 35.2 | 32.8→37.0 | 29.9→34.1 | 38.3→46.7 | 27.9→29.8 | 25.0→26.9 |
> | Qwen2.5-7B-Instruct | 27.0 | 29.8 | 29.2→30.7 | 25.7→29.3 | 36.1→35.6 | 23.7→26.5 | 18.5→26.9 |
> | **Qwen2.5-72B-Instruct** | **39.4** | **38.8** ← only model where CoT DECREASES | 43.8→42.2 | 36.7→36.7 | 44.4→50.0 | 34.0→28.8 | 41.7→39.8 |
> | Mistral-Large-Inst-2407 | 26.6 | 33.6 | 29.7→34.4 | 24.8→33.1 | 37.8→41.1 | 19.5→31.2 | 22.2→25.9 |
> | Mistral-Large-Inst-2411 | 34.4 | 39.6 | 38.0→43.8 | 32.2→37.0 | 41.7→46.1 | 30.7→34.9 | 29.6→38.0 |
> | c4ai-command-r-plus-08-2024 | 27.8 | 31.6 | 30.2→34.4 | 26.4→29.9 | 36.7→39.4 | 23.7→24.2 | 21.3→33.3 |

> [!info] Proprietary models (with thinking models highlighted)
>
> | Model | Zero-shot | CoT | Easy | Hard | Short | Medium | Long |
> |---|---|---|---|---|---|---|---|
> | GLM-4-Plus | 44.3 | 46.1 | 47.4→52.1 | 42.4→42.4 | 50.0→53.3 | 46.5→44.7 | 30.6→37.0 |
> | GPT-4o-mini-2024-07-18 | 29.3 | 32.4 | 31.1→32.6 | 28.2→32.2 | 31.8→34.8 | 28.6→31.6 | 26.2→29.9 |
> | **GPT-4o-2024-08-06** | **50.1** | 51.2 | 57.4→57.9 | 45.6→47.1 | 53.3→53.9 | 52.4→50.7 | 40.2→47.7 |
> | GPT-4o-2024-11-20 | 46.0 | 51.4 | 50.8→54.2 | 43.0→49.7 | 47.5→59.6 | 47.9→48.6 | 39.8→43.5 |
> | **o1-mini-2024-09-12** | **37.8** ← thinking | 38.9 | 38.9→42.6 | 37.1→36.6 | 48.6→48.9 | 33.3→32.9 | 28.6→34.3 |
> | **o1-preview-2024-09-12** | **57.7** ← top thinking | 56.2 | 66.8→58.9 | 52.1→54.6 | 62.6→64.6 | 53.5→50.2 | **58.1→54.3** |
> | Claude-3.5-Sonnet-20241022 | 41.0 | 46.7 | 46.9→55.2 | 37.3→41.5 | 46.1→53.9 | 38.6→41.9 | 37.0→44.4 |
> | **Human** ∗ | **53.7** | — | 100 | 25.1 | 47.2 | 59.1 | 53.7 |

**Three patterns emerge**:
1. **CoT helps almost all models** (avg +3.4% open-source); **Qwen2.5-72B is the sole exception** (39.4→38.8, slight decline)
2. **o1-preview's thinking-paradigm advantage is concentrated**: +7.6% over GPT-4o, +12% over Claude-3.5-Sonnet
3. **Length-stratification reveals task-distribution effects**: GPT-4o on Long is 40.2→47.7 (CoT lifts it +7.5%); o1-preview on Long is 58.1→54.3 (CoT actually DROPS) — thinking-paradigm benefits saturate at certain lengths

### RAG Ablation (Section 4.2, Figure 4)

> [!info] RAG performance vs full-context baseline
>
> Method:
> - Chunk to 512 tokens (GLM-4-9B tokenizer)
> - Encode query (question + choices) and chunks via Zhipu Embedding-3
> - Sort chunks by embedding similarity
> - Retrieve top-N where N ∈ {4, 8, 16, 32, 64, 128, 256}
> - Concatenate retrieved chunks in **original order** (preserves text structure)
>
> Results:
> - **Qwen2.5-72B-Instruct**: peaks at N=32 (~32k retrieved tokens) with **+4.1% improvement** over no-RAG full-context (39.4 → 43.5%); declines beyond
> - **GLM-4-Plus**: similar pattern, peaks around N=32
> - **GPT-4o**: monotonic improvement up to N=128 (~64k retrieved tokens), but **best RAG = 49.5% < 50.1% no-RAG full context** (-0.6%)
>
> **Key conclusion** (paper §4.2): **questions in LongBench v2 cannot be solved through retrieval alone**. Even oracle-style large retrieval (256 chunks = ~128k tokens) doesn't outperform giving the model the full context. **This refutes the "RAG can replace long-context capability" framing for this benchmark's task class.**

### Memorization Check (Section 4.3, Table 3)

> [!info] With (w/) vs without (w/o) context performance
>
> | Model | Avg | I (Single) | II (Multi) | III (ICL) | IV (Dialog) | V (Code) | VI (Struct) |
> |---|---|---|---|---|---|---|---|
> | GLM-4-9B-Chat | 30.2 | 30.9 | 27.2 | 33.3 | 38.5 | 28.0 | 24.2 |
> | GLM-4-9B-Chat w/o context | 26.2 | 30.9 | 21.6 | 18.5 | 30.8 | 34.0 | 21.2 |
> | Llama-3.1-8B-Inst | 30.0 | 34.9 | 30.4 | 23.5 | 17.9 | 32.0 | 30.3 |
> | Llama-3.1-8B-Inst w/o | 25.8 | 31.4 | 26.4 | 24.7 | 23.1 | 22.0 | 6.1 |
> | Qwen2.5-72B-Inst | 39.4 | 40.6 | 35.2 | 42.0 | 25.6 | 50.0 | 42.4 |
> | Qwen2.5-72B-Inst w/o | 30.0 | 33.7 | 31.2 | 25.9 | 28.2 | 34.0 | 12.1 |
> | GLM-4-Plus | 44.3 | 41.7 | 42.4 | 46.9 | 51.3 | 46.0 | 48.5 |
> | GLM-4-Plus w/o | 27.6 | 33.7 | 27.2 | 25.9 | 10.3 | 38.0 | 6.1 |
> | **GPT-4o** | 50.1 | 48.6 | 44.0 | 58.0 | 46.2 | **56.0** | 51.5 |
> | **GPT-4o w/o** | **33.1** | 40.0 | 25.6 | 32.1 | 38.5 | **34.0** | 18.2 |

**Pattern observations**:
- **Most models w/o context: 25-30%** ≈ random (4-option multi-choice baseline)
- **GPT-4o w/o = 33.1%** indicates ~8 absolute points of training-data leakage at this model class
- **Highest w/o-context scores by task**: GPT-4o on I (Single-Doc) = 40.0% and V (Code Repo) = 34.0% — likely from training-data overlap
- **Lowest w/o-context scores**: tasks III, IV, VI cluster around 6-25% (no leakage detected)

**Implication for benchmark interpretation**: when comparing models on tasks I + V, account for memorization advantages of larger commercial models trained on more web data. Tasks II + III + VI offer cleaner capability measurement.

### YaRN Ablation (Appendix E, Table 4)

> [!info] **Long-context fine-tuning closes some open-source gap**
>
> | Model | Overall | CoT | Short | Medium | Long |
> |---|---|---|---|---|---|
> | Qwen2.5-7B-Instruct | 27.0 | 29.8 | 36.1 | 23.7 | 18.5 |
> | + YaRN | **30.0** | **35.6** | 40.6 | 24.2 | 24.1 |
> | Qwen2.5-72B-Instruct | 39.4 | 38.8 | 44.4 | 34.0 | 41.7 |
> | + YaRN | **42.1** | **43.5** | 45.6 | 38.1 | 44.4 |
>
> **YaRN** (Peng et al. 2024) = position-encoding extension for context length. Scaling factor 4.0.
>
> Patterns:
> - **+3.0% overall for Qwen2.5-7B**; **+2.7% for Qwen2.5-72B**
> - **YaRN benefit larger on Medium + Long subsets** (>32k tokens)
> - **YaRN benefit larger under CoT setting** — paper notes "the underlying reasons for this remain unclear"
>
> **Implication for the wiki's mission**: long-context fine-tuning IS a reachable capability gain at the open-source side. Qwen2.5-72B + YaRN = 42.1% closes ~2 absolute points to GLM-4-Plus (44.3%) closed-source levels.

### Compensated Results (Appendix E, Table 5)

> [!info] **Invalid output rates and compensated results**
>
> Some models occasionally fail to produce a parseable answer (refusal or format error). The paper reports both raw scores AND compensated scores (invalid outputs counted as random 25% accuracy).
>
> Notable invalid rates:
> - Mistral-Large-Inst-2407: **16.9%** invalid (highest — concerning for production use)
> - Claude-3.5-Sonnet: **13.9%** invalid zero-shot, 14.9% CoT
> - Most other models: <8% invalid
>
> Compensation mostly preserves rankings — high-invalid models gain a few absolute points but don't change conclusions.

### Why This Matters for the Wiki's Mission

> [!success] **Evidence 6 of [[anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence|anti-vendor-lock-in lesson]] is now Layer 1 across ALL 4 RLM Table 1 benchmarks**
>
> With this synthesis, the evaluation-layer evidence chain is complete at full PDF depth:
>
> | Benchmark | Layer 1 status |
> |---|---|
> | BrowseComp+ | ✓ [Layer 1 deep-dive](src-browsecomp-plus-paper-deep-dive-fixed-corpus-table-1-oracle-citation-quality.md) |
> | OOLONG | ✓ [Layer 1 deep-dive](src-oolong-paper-deep-dive-synth-real-leaderboard-cmu-frontier-fails-128k.md) |
> | LongBench Pro | ✓ [Layer 1 deep-dive](src-longbench-pro-paper-deep-dive-1500-samples-46-models-three-findings.md) |
> | **LongBench v2 / CodeQA** | ✓ **THIS SYNTH** |
>
> **The mission's anti-vendor-lock-in claim is now empirically traceable end-to-end at the evaluation layer.** All 4 benchmarks: public + reproducible + paper-citable + Layer 1 deep-dive in the wiki.

> [!success] **The o1-preview-beats-humans-by-4-points finding anchors the thinking-paradigm narrative**
>
> Per Finding 9: o1-preview = 57.7% > human 53.7% by **+4 absolute points**. **Empirical canonical case for thinking-time scaling on long-context tasks**. The finding parallels [LongBench Pro Finding 3](src-longbench-pro-paper-deep-dive-1500-samples-46-models-three-findings.md) (native thinking required) and [BrowseComp+ Section 4.8.2](src-browsecomp-plus-paper-deep-dive-fixed-corpus-table-1-oracle-citation-quality.md) (reasoning-effort scales accuracy + search calls).
>
> **Mission implication**: post-training models for native thinking (RLM, reasoning fine-tunes) is empirically validated as the path to long-context capability — NOT prompting-based shortcuts.

> [!success] **Step 6 of [RLM-Qwen3.6-27B operations plan](../../domains/cross-domain/rlm-qwen3-6-27b-fine-tune-operations-plan.md) target numbers are grounded for CodeQA**
>
> The plan's Step 6 evaluation table cites CodeQA (LongBench v2 split) as 1 of 4 benchmarks. **Reference targets** (from RLM paper Table 1 + this synth):
> - **Base GPT-5 on CodeQA**: 24.0% (per RLM Table 1; LongBench v2 paper has GPT-4o = 56.0% on Code Repo task; the discrepancy is due to "CodeQA" being a sub-task evaluation done by RLM authors with different prompting)
> - **RLM(GPT-5) on CodeQA**: 62.0%
> - **RLM-Qwen3-8B on CodeQA**: 32.0%
> - **Plan's hypothetical RLM-Qwen3.6-27B target on CodeQA**: ≥50% (between 8B and 480B)
>
> **This synth grounds the benchmark structure** for the operations plan: Code Repo QA = 50 entries × 167k median tokens × multi-file code reasoning. Step 6 has executable target numbers.

> [!warning] **The RAG-saturation-at-32K finding contradicts naive RAG-replaces-long-context framing**
>
> Per Finding 13: only GPT-4o effectively uses 128K retrieval, but **still -0.6% below its non-RAG full-context score**. **Implication**: AICP smart-routing should NOT default to RAG for long-context-reasoning tasks. The wiki's [tier-0 candidate comparison](../../comparisons/rlm-qwen3-8b-vs-qwen3-6-27b-tier-0-long-context-candidate.md) routing logic should use the model's effective long-context capability, not its retrieval window.

> [!info] **Memorization-check finding informs benchmark interpretation when comparing models**
>
> Per Finding 14: GPT-4o w/o context = 33.1% overall (some training-data leakage). For cleaner capability comparison, prefer tasks II (Multi-Doc QA) + III (Long ICL) + VI (Long Structured Data) where memorization is minimal. Tasks I (Single-Doc) + V (Code Repo) carry leakage risk for commercial models.
>
> **Mission implication**: when AICP benchmarks closed-source vs open-source models, control for memorization differences — closed-source has more pretraining data exposure.

### Future Work Implications

The paper's design choices and findings imply several directions worth tracking:
1. **Bilingual extension** (limitation §6) — current English-only constraint; team could extend to Chinese (their LongBench v1 was bilingual)
2. **Larger benchmark size** (limitation §6) — 503 may be statistically noisy; would require more funding (~100k CNY × N for N× scale)
3. **Native-thinking fine-tunes** — o1-preview's gain is the strongest signal; open-source post-training for thinking-paradigm is the natural follow-on
4. **RAG-aware models** — paper's finding that even oracle-large retrieval falls short suggests RAG architectures need redesign for long-context-reasoning

## Open Questions

> [!question] What's the relationship between LongBench v2's "Code Repo QA" subtask and the RLM paper's "CodeQA" Table 1 task?
> RLM paper Table 1 has CodeQA with token range 23K-4.2M and base GPT-5 = 24.0% — clearly NOT the same numbers as this synth's GPT-4o on Code Repo (V) = 56.0%. **Likely**: RLM paper's "CodeQA" uses LongBench v2 Code Repo QA *but* with RLM-paper-specific prompting + extended context lengths via re-sampling. The 50 entries in LongBench v2 Code Repo QA become evaluation seeds; the actual Table 1 numbers may use a derived test set rather than the original 503-question benchmark. (Requires: cross-reading RLM paper's Section 4.1 + LongBench v2 evaluation harness inspection.)

> [!question] How does LongBench v2 compare to LongBench v1 (the original Bai et al. 2023 benchmark)?
> Same lead authors (Yushi Bai et al., Tsinghua). v1 is bilingual (English + Chinese) with metrics like F1 + ROUGE; v2 is English-only with multiple-choice + 4-option format. **The methodological evolution** — F1/ROUGE → multi-choice — reflects the team's empirical conclusion that subjective metrics are unreliable. v2 supersedes v1 for evaluation but v1's broader methodology (more tasks, bilingual) may still be useful for capability profiling.

> [!question] Could the 503-sample size be statistically too small for reliable model comparisons?
> Per Limitations §6: "less stable results that are more vulnerable to randomness". For a 4-option multi-choice benchmark with ~95%-confidence intervals: 503 samples → margin of error ~±4.4 percentage points. **Implication**: differences <5 absolute points between models may not be statistically significant. Per-difficulty + per-length stratification further reduces effective sample sizes (e.g., Long subset = 108 samples → ~±9.6 pp margin). **Conclusion**: treat per-interval comparisons as directional, not definitive.

> [!question] Is the Tsinghua + Zhipu.AI co-affiliation relevant to which models perform best?
> Zhipu.AI is the company behind GLM models. **GLM-4-Plus = 44.3%** is best Chinese closed-source on this benchmark — possibly aided by Zhipu.AI's long-context training data overlapping with the benchmark's source documents. **Plausible bias**: benchmark co-affiliated with model-family-creator should be evaluated for indirect contamination. The paper's memorization check (Table 3) addresses this for individual tasks but not at the benchmark-construction-bias level.

> [!question] What does Long ICL's "New language translation" subtask actually test?
> Per Appendix B III.2: 20 entries on Kalamang (Tanzer et al. 2024) + Zhuang (Zhang et al. 2024a). Models given a vocabulary book (132k median) + a sentence to translate into multi-choice options. **This is the most novel ICL test in any long-context benchmark** — tests genuinely-out-of-distribution language acquisition rather than memorization. Worth tracking as a benchmark design pattern.

> [!question] Could the benchmark be wired into the wiki's [tools/pipeline.py](../../../tools/pipeline.py) as a quality-regression suite?
> The 503-sample structure + multi-choice format + per-task metrics + GitHub eval code make this technically feasible. AICP-side wiring would let routing decisions be benchmark-driven. (Requires: harness adoption + per-question cost analysis; the 503 samples × 17 models with CoT would be a non-trivial spend.)

## Applicability

> [!info] Where to use LongBench v2 findings directly
>
> - **Long-context capability evaluation** for any 128K+ model
> - **Thinking-paradigm vs direct-answer comparison** (the canonical o1-preview-beats-humans case)
> - **RAG saturation analysis** for retrieval-vs-context-window decisions
> - **Memorization audit** for closed-source vs open-source comparisons
> - **YaRN benefit estimation** for Qwen-family long-context fine-tunes
> - **Per-task capability profiling** (6 categories × 20 subtasks for fine-grained comparison)
> - **Code repository understanding** specifically — the V.1 subtask is one of the only public benchmarks for this task class

> [!warning] Where these findings DON'T apply
>
> - **Short-context tasks** (<8K) — benchmark targets ≥8K
> - **Bilingual / multilingual evaluation** — English-only
> - **Visual / multimodal queries** — text-only
> - **Generative-quality evaluation** — multi-choice format, no free-form generation
> - **Tasks where 503-sample size is statistically insufficient** — small differences may not be significant
> - **Production deployments where invalid-output handling matters** — Mistral-Large-2407's 16.9% invalid rate is concerning for non-research use

## Relationships

- BUILDS ON: [[src-browsecomp-plus-and-longbench-v2-rlm-table-1-benchmarks|BrowseComp+ + LongBench v2 Combined Synthesis]] (this is the dedicated Layer-1 deep-dive expanding on LongBench v2 specifics that the combined synth covered at abstract level; Tsinghua/Zhipu.AI affiliation confirmed)
- COMPARES TO: [[src-rlm-paper-deep-dive-table-1-training-recipe-six-observations|RLM Paper Deep Dive]] (RLM paper used LongBench v2 Code Repo QA subtask as Table 1's CodeQA split; RLM(GPT-5) = 62.0% vs base GPT-5 = 24.0%)
- COMPARES TO: [[src-longbench-pro-paper-deep-dive-1500-samples-46-models-three-findings|LongBench Pro Paper Deep Dive]] (DIFFERENT team's parallel benchmark in the LongBench family — this paper is Tsinghua/Zhipu.AI; LongBench Pro is IIE-CAS + Beihang + Xiaohongshu. Both share "LongBench" name but are independent research efforts.)
- COMPARES TO: [[src-browsecomp-plus-paper-deep-dive-fixed-corpus-table-1-oracle-citation-quality|BrowseComp+ Paper Deep Dive]] (parallel Layer-1 deep-dive; BrowseComp+ uses fixed corpus + retriever-disentanglement vs LongBench v2's multi-choice + 5-stage construction; both are RLM Table 1 benchmarks)
- COMPARES TO: [[src-oolong-paper-deep-dive-synth-real-leaderboard-cmu-frontier-fails-128k|OOLONG Paper Deep Dive]] (parallel Layer-1 deep-dive; OOLONG focuses on aggregation tasks specifically; LongBench v2 is broader 6×20 task taxonomy)
- DEMONSTRATES: [[infrastructure-over-instructions-for-process-enforcement|Principle 1]] (multi-choice format with single correct answer is structural enforcement of evaluation reliability vs F1/ROUGE/LLM-as-judge subjectivity)
- DEMONSTRATES: [[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4]] (the "long-context models truly comprehend" claim was aspirational until LongBench v2 measured it; result: 50.1% direct-answer best, 53.7% human, 57.7% o1-preview)
- DEMONSTRATES: [[anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence|Anti-Vendor-Lock-In Lesson]] § Evidence 6 (the evaluation-layer empirical anchor — completing the 4-of-4 RLM Table 1 benchmarks at Layer 1 confidence)
- DEMONSTRATES: [[right-process-for-right-context-the-goldilocks-imperative|Principle 3 — Goldilocks]] (per-difficulty + per-length-interval evaluation; thinking-paradigm vs direct-answer process selection per task class)
- RELATES TO: [[2026-consumer-hardware-ai-stack|2026 Consumer Hardware AI Stack]] (long-context capability evaluation for tier-0 candidates)
- RELATES TO: [[ai-infrastructure-decision-framework-2026|AI Infrastructure Decision Framework 2026]] (model-vs-API distinction; thinking-paradigm × context-length interaction; RAG-saturation findings inform routing decisions)
- FEEDS INTO: [[rlm-qwen3-6-27b-fine-tune-operations-plan|RLM-Qwen3.6-27B Operations Plan]] § Step 6 (CodeQA = LongBench v2 Code Repo QA; 1 of 4 evaluation surfaces)
- FEEDS INTO: [[rlm-thread-evidence-chain-2026-04-27|Learning Path — RLM Thread Evidence Chain]] (Path C: Reproduce Training — this synth is the deep-dive reference for the LongBench v2 evaluation surface)

## Backlinks

[[BrowseComp+ + LongBench v2 Combined Synthesis]]
[[src-rlm-paper-deep-dive-table-1-training-recipe-six-observations|RLM Paper Deep Dive]]
[[src-longbench-pro-paper-deep-dive-1500-samples-46-models-three-findings|LongBench Pro Paper Deep Dive]]
[[BrowseComp+ Paper Deep Dive]]
[[src-oolong-paper-deep-dive-synth-real-leaderboard-cmu-frontier-fails-128k|OOLONG Paper Deep Dive]]
[[infrastructure-over-instructions-for-process-enforcement|Principle 1]]
[[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4]]
[[Anti-Vendor-Lock-In Lesson]]
[[right-process-for-right-context-the-goldilocks-imperative|Principle 3 — Goldilocks]]
[[2026 Consumer Hardware AI Stack]]
[[ai-infrastructure-decision-framework-2026|AI Infrastructure Decision Framework 2026]]
[[rlm-qwen3-6-27b-fine-tune-operations-plan|RLM-Qwen3.6-27B Operations Plan]]
[[Learning Path — RLM Thread Evidence Chain]]
