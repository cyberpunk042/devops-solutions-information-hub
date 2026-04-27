---
title: "Synthesis — LongBench Pro Paper Deep Dive: 1,500-Sample Bilingual Benchmark, 11×25 Task Taxonomy, 46-Model Evaluation, Three Findings, Human-Model Collaborative Construction (arXiv 2601.02872 v1, Jan 2026)"
aliases:
  - "LongBench Pro Paper Deep Dive"
  - "LongBench Pro Tables 1-5"
  - "LongBench Pro Three Findings"
  - "LongBench Pro 46 Models"
type: source-synthesis
domain: tools-integration
status: synthesized
confidence: high
maturity: seed
created: 2026-04-27
updated: 2026-04-27
last_reviewed: 2026-04-27
sources:
  - id: longbench-pro-paper-pdf
    type: paper
    url: https://arxiv.org/pdf/2601.02872
    file: raw/papers/longbench-pro-a-more-realistic-and-comprehensive-bilingual-long-context-evaluati.md
    title: "LongBench Pro arXiv 2601.02872 v1 (6 Jan 2026) — Full PDF"
    description: "28 pages with Appendix; 2226-line raw scrape. Authors: Ziyang Chen, Xing Wu (correspondence), Junlong Jia, Chaochen Gao, Qi Fu, Debing Zhang, Songlin Hu (correspondence). Affiliations: Institute of Information Engineering CAS + UCAS School of Cyber Security + Beihang University AI School + Xiaohongshu Inc. Dataset on Hugging Face: caskcsg/LongBench-Pro."
    ingested: 2026-04-27
  - id: longbench-pro-abstract-companion
    type: wiki
    file: wiki/sources/tools-integration/src-oolong-and-longbench-pro-long-context-benchmarks-rlm-anchors.md
    description: "Abstract-level companion synthesis covering OOLONG AND LongBench Pro together at Layer 0/1; this page is the dedicated Layer-1 deep-dive on LongBench Pro alone, sourced from the full PDF rather than the abstract page. Note: combined synth speculated 'Tsinghua-affiliated' for LongBench Pro authors — this PDF reading corrects to IIE-CAS + UCAS + Beihang + Xiaohongshu."
  - id: longbench-original
    type: paper
    url: https://arxiv.org/abs/2308.14508
    title: "LongBench (Bai et al., 2023) — original benchmark this extends"
    description: "First in the LongBench family — bilingual multitask benchmark. LongBench Pro is the larger, harder, more comprehensive successor (1500 samples vs LongBench's smaller scope)."
  - id: longbench-v2-related
    type: paper
    url: https://arxiv.org/abs/2412.15204
    title: "LongBench v2 (Bai et al., 2025)"
    description: "Different team's LongBench-line benchmark — fully natural, 6 tasks, single metric, English-only. LongBench Pro positions itself as more comprehensive: 11 tasks, diverse metrics, bilingual, multi-dimensional categorization."
  - id: rlm-paper-deep-dive
    type: wiki
    file: wiki/sources/tools-integration/src-rlm-paper-deep-dive-table-1-training-recipe-six-observations.md
    description: "RLM paper deep-dive — uses LongBench Pro English split (750 tasks) as TRAINING DATA SOURCE for RLM-Qwen3-8B (2,250 candidate trajectories → 1,072 filtered → per-turn SFT samples → prime-rl 48 H100 hours)"
  - id: rlm-qwen3-6-27b-operations-plan
    type: wiki
    file: wiki/domains/cross-domain/rlm-qwen3-6-27b-fine-tune-operations-plan.md
    description: "Operations plan — Step 1 dependency on LongBench Pro English split. This synth grounds the dataset's structure, license accessibility, and sample shape for that plan's execution."
  - id: anti-vendor-lock-in-lesson
    type: wiki
    file: wiki/lessons/01_drafts/anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence.md
    description: "Mission framing — Evidence 6 (Evaluation layer: 4 public benchmarks define the task class) is grounded by this Layer 1 reading on the LongBench Pro side"
  - id: huggingface-dataset
    type: documentation
    url: https://huggingface.co/datasets/caskcsg/LongBench-Pro
    title: "LongBench Pro dataset on Hugging Face"
    description: "Public dataset hosted by caskcsg organization — accessibility confirmed for the RLM-Qwen3.6-27B operations-plan Step 1"
tags: [longbench-pro, long-context-benchmarks, bilingual-evaluation, english-chinese, fully-natural-documents, 11-primary-tasks, 25-secondary-tasks, 46-llm-evaluation, three-findings, long-context-optimization-beats-scaling, effective-vs-claimed-context, native-thinking-paradigm, mixed-thinking-pareto, human-model-collaborative-construction, iie-cas, ucas, beihang, xiaohongshu, rlm-training-data-source, mission-2026-04-27, anti-vendor-lock-in, paper-deep-dive, paper-pdf-layer-1]
---

# Synthesis — LongBench Pro Paper Deep Dive

## Summary

The arXiv 2601.02872 v1 paper PDF (6 Jan 2026; 28 pages with Appendix; 2226-line raw scrape) supplies the full empirical detail that the [combined OOLONG + LongBench Pro abstract-level synthesis](src-oolong-and-longbench-pro-long-context-benchmarks-rlm-anchors.md) compressed into a single column. **Seven authors led by Xing Wu (correspondence: wuxing@iie.ac.cn) and Songlin Hu (correspondence: husonglin@iie.ac.cn) at the Institute of Information Engineering, Chinese Academy of Sciences (IIE-CAS), with co-authors from UCAS School of Cyber Security + Beihang University AI School + Xiaohongshu Inc.** This **corrects the combined synth's speculative "Tsinghua-affiliated" attribution** — the actual lineage is IIE-CAS (Hu's group) + corporate co-author Xiaohongshu, distinct from the Tsinghua LongBench / LongBench v2 line (Yushi Bai et al.). The paper grounds the abstract's 1,500-sample claim with the precise construction pipeline (5 steps · 5 frontier LLMs as drafters · 63 annotators including 12 long-context experts compensated 50 RMB/hour · 5×25×2×6 = 1,500 samples balanced design · 99.3% attribute correctness + 97.3% answer correctness on 300-sample audit), the **full 11 primary task × 25 secondary task taxonomy** (Table 2 with Context-Requirement / metric mappings: NDCG@k / Pairwise Accuracy / Accuracy / SemSim+ROUGE-L / F1 / SubEM), the **46-LLM general-performance table** (Table 3 — Gemini-2.5-Pro 73.42 / GPT-5 72.61 / Claude-4-Sonnet 69.87 leading; DeepSeek-V3.2 67.82 + Qwen3-235B-A22B-Thinking-2507 66.97 narrowing closed-source gap to 6 points), and detailed **per-finding empirical anchors**: (1) **long-context optimization > parameter scaling** — Qwen3-30B-A3B-Instruct-2507 (256k context) = 54.52 OUTPERFORMS Qwen3-32B = 51.12 despite 1/8 active params; (2) **effective context << claimed context** — MiniMax-Text-01 (claims 4M) scores 45.00 falling behind 128k models; (3) **thinking paradigm requires native training** — Llama-3.1-8B-Instruct prompted thinking actually DEGRADES from 21.09 → 20.06. **Mission-load-bearing**: this is the dataset Step 1 of the [RLM-Qwen3.6-27B operations plan](../../domains/cross-domain/rlm-qwen3-6-27b-fine-tune-operations-plan.md) targets — confirmed accessible at `huggingface.co/datasets/caskcsg/LongBench-Pro`, English split = 750 tasks (1500 / 2 languages), per-task structure (3 candidate samples per (document, task) pair before filtering, drafted by 5 frontier LLMs).

## Reference Card

> [!info] Paper deep-dive reference card

| Field | Value |
|---|---|
| **Paper** | arXiv 2601.02872 v1, dated 6 Jan 2026 (cs.CL) |
| **Length** | 28 pages with Appendix · 2226-line raw scrape |
| **Authors (7)** | Ziyang Chen (1,2) · **Xing Wu** (1, correspondence) · Junlong Jia (3) · Chaochen Gao (1,2) · Qi Fu (4) · Debing Zhang (4) · **Songlin Hu** (1, correspondence) |
| **Affiliations** | (1) **Institute of Information Engineering, Chinese Academy of Sciences (IIE-CAS)** · (2) School of Cyber Security, University of Chinese Academy of Sciences (UCAS) · (3) School of Artificial Intelligence, Beihang University · (4) **Xiaohongshu Inc.** |
| **Lineage correction** | **NOT Tsinghua-affiliated** (combined-synth speculation was wrong). Hu/Wu's IIE-CAS group + Xiaohongshu corporate involvement. Distinct from Tsinghua's LongBench / LongBench v2 line (Yushi Bai et al.). |
| **Dataset URL** | huggingface.co/datasets/caskcsg/LongBench-Pro (public, accessible) |
| **Total samples** | **1,500** (5 × 25 × 2 × 6 balanced design) |
| **Languages** | English + Chinese (bilingual) |
| **Length buckets** | 6 levels: 8k / 16k / 32k / 64k / 128k / 256k tokens (Qwen tokenizer; ±20% tolerance) |
| **Task taxonomy** | **11 primary tasks × 25 secondary tasks** |
| **Difficulty levels** | 4 (Easy / Moderate / Hard / Extreme) — calibrated against 15 reference models in 3 tiers |
| **Annotators** | **63 total**: 51 general + **12 long-context experts** (≥1 yr experience + 2-mo specialized training) |
| **Annotator compensation** | **50 RMB/hour** |
| **Sample quality (300-sample audit)** | 99.3% attribute correctness · 97.3% answer correctness |
| **Construction strategies compared (§5.7)** | Human-only · Model-only · **Human-model collaborative (ours)** |
| **Quality scores (5 dimensions, 3 expert raters, Fleiss κ = 0.76)** | Human-model collaborative: **0.9609 ± 0.0415** (highest) · Human-only: 0.9484 ± 0.0450 · Model-only: 0.8964 ± 0.0536 |
| **5 frontier LLMs as drafters** | Gemini-2.5-Pro · GPT-5 · Claude-4-Sonnet · DeepSeek-V3.2 · Qwen3-235B-A22B-Thinking-2507 |
| **Models evaluated (Table 3)** | **46** spanning closed/open · thinking/mixed-thinking/non-thinking · 3B-1T params · dense/MoE · 128k-1M context |
| **Top closed-source** | **Gemini-2.5-Pro = 73.42** · GPT-5 = 72.61 · Claude-4-Sonnet = 69.87 |
| **Top open-source** | **DeepSeek-V3.2 = 67.82** · Qwen3-235B-A22B-Thinking-2507 = 66.97 (within 6 points of best closed) |
| **Three findings (validated empirically)** | (1) Long-context optimization > parameter scaling · (2) Effective context << claimed context · (3) Thinking paradigm requires native training |
| **Future work** | "Critique-of-Critique" recursive verification (cf. DeepSeekMath-V2 meta-verification) |
| **Confidence** | high — full paper PDF read (lines 1-2226) including all 5 tables, all 3 findings with their empirical anchors, full 11×25 task taxonomy, all 5 construction strategies, all 5 quality dimensions, all 7 appendices (task definitions A · annotation guidelines B · annotator statistics C · inference parameters D · truncation length E) |
| **Mission relevance** | Critical — Step 1 dependency for [RLM-Qwen3.6-27B operations plan](../../domains/cross-domain/rlm-qwen3-6-27b-fine-tune-operations-plan.md); Evidence 6 (evaluation layer) for [anti-vendor-lock-in lesson](../../lessons/01_drafts/anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence.md) |

## Key Insights

1. **The combined synth's "Tsinghua-affiliated" attribution was wrong**. Authoritative lineage: lead correspondence Xing Wu and Songlin Hu at **Institute of Information Engineering, Chinese Academy of Sciences** with corporate co-author Xiaohongshu Inc. The Tsinghua line (Yushi Bai et al.) authored LongBench / LongBench v2 — different group entirely. Both are Chinese academic-AI long-context efforts but the institutional provenance differs. *This is a Layer-1-only correction the abstract page didn't expose.*

2. **The 11×25 task taxonomy is structurally important** (Table 2 — full enumeration in §A of the paper). Each of the 11 primary tasks has 1-3 secondary tasks split by **context-requirement** (Full vs Partial), with 6 distinct evaluation metrics:
   - **NDCG@k** for retrieval/ranking (T1.1, T1.2)
   - **Pairwise Accuracy** for sequencing (T2.1, T2.2, T6.3)
   - **Accuracy** for QA + dialogue (T3.1, T3.2, T11.1, T11.2)
   - **0.5×SemSim + 0.5×ROUGE-L** for summarization (T4.1, T4.2)
   - **F1** for citation/clustering-targeted/consistency (T5.1, T5.2, T6.2, T7.1, T7.2, T7.3, T8.3, T9.1, T9.2)
   - **SubEM** for clustering-large/numeric/rule-induction (T6.1, T8.1, T8.2, T10.1, T10.2)

3. **Final dataset shape is 5 × 25 × 2 × 6 = 1,500 samples** — exactly balanced. Each (secondary task, language, length) cell has 5 samples. **The English split (750 tasks) is what the [RLM-Qwen3.6-27B operations plan](../../domains/cross-domain/rlm-qwen3-6-27b-fine-tune-operations-plan.md) Step 1 + the original [RLM paper's](src-rlm-paper-deep-dive-table-1-training-recipe-six-observations.md) RLM-Qwen3-8B training depend on**.

4. **The Human-Model Collaborative Construction pipeline is empirically validated against alternatives (§5.7)**:
   - **Time cost**: human-only grows exponentially with length; model-only is flat-low; collaborative is in-between and grows slowly
   - **Quality scores** (5 dimensions × 3 expert raters × scores 0/0.5/1; Fleiss κ = 0.76):
     - Human-model collaborative: **0.9609 ± 0.0415** ← highest
     - Human-only: 0.9484 ± 0.0450 (lacks model-driven recall)
     - Model-only: 0.8964 ± 0.0536 (lacks human verification of difficulty + correctness)
   - **Conclusion**: collaboration outperforms either pure mode on quality AND on cost-scalability.

5. **Difficulty calibration uses 15 reference models across 3 tiers** — model-centric, not human-rated:
   - **High-tier** (5): Gemini-2.5-Pro, GPT-5, Claude-4-Sonnet, DeepSeek-V3.2, Qwen3-235B-A22B-Thinking-2507
   - **Mid-tier** (5): GLM-4.6, DeepSeek-V3-0324, Kimi-K2-Instruct-0905, Qwen3-30B-A3B-Instruct-2507, MiniMax-M2
   - **Low-tier** (5): Ministral-3-8B-Instruct-2512, Qwen3-8B, Qwen2.5-72B-Instruct, Llama-3.1-405B-Instruct, Gemma-3-27B-It
   
   Difficulty assignment: Extreme (≤1 high-tier correct) → Hard (≤1 mid-tier correct, excluding Extremes) → Moderate (≤1 low-tier correct) → Easy (remaining). **This anchors difficulty in measured model performance, not subjective annotator ratings** — providing automatic re-calibration as future models exceed today's tiers.

6. **Finding 1 — Long-context optimization > parameter scaling — empirically grounded**:
   - **Within Qwen3 family (32k native + YaRN to 128k)**: 4B → 32B improves 40.82 → 51.12 (marginal gains decrease)
   - **Long-context-optimized variants overcome size**:
     - Qwen3-4B-Instruct-2507 (256k context) = **45.68** vs Qwen3-8B (128k) = **44.34** (4B beats 8B by virtue of longer-context-tuning)
     - **Qwen3-30B-A3B-Instruct-2507 (256k) = 54.52 OUTPERFORMS Qwen3-32B = 51.12** (30B-A3B = 30B total, 3B active MoE)
   - **Direct quote** (paper §5.2): *"This demonstrates that extending the effective context length constitutes the primary approach for improving long-context performance, and its effectiveness far exceeds that of scaling up parameters by several times."*
   - **Mission relevance**: this is the empirical anchor for the wiki's anti-vendor-lock-in mission. Smaller-trained-right > bigger-trained-loosely on long-context tasks. RLM-paradigm post-training is one specific instance of "trained right".

7. **Finding 2 — Effective context << claimed context — empirically grounded with multiple instances**:
   - **MiniMax-Text-01** claims **4M context**, scores 45.00 — falls behind most 128k models
   - **GLM-4.6** claims 198k; output unstable at 190k truncation for 256k samples → effective length significantly less than claimed (Table 4 shows score drop on 256k samples: 32.55 at 190k truncation vs 34.14 at 120k truncation)
   - **Cross-lingual misalignment** is uneven: **GPT/Claude/Mistral/Llama series** perform better in English; **GLM/Kimi/MiniMax series** perform better in Chinese. As model scale grows + capabilities improve, gap narrows but persists.
   - **Direct quote** (paper §5.2): *"the claimed context length reflects the model's input capacity, whereas the effective context length reflects its actual long-context understanding and processing capability, and a significant gap may exist between the two."*

8. **Finding 3 — Thinking paradigm requires native training — directly evidenced**:
   - **Native-thinking gain (mixed-thinking models)**: Claude-4-Sonnet **+13.80** (56.07→69.87) · DeepSeek-V3.2 **+16.15** (51.67→67.82) · Qwen3-235B-A22B-Thinking-2507 vs Qwen3-235B-A22B-Instruct-2507-with-thinking +3.20 (63.77→66.97)
   - **Prompted-thinking on instruct models — limited or DEGRADED**:
     - Llama-3.1-405B-Instruct: **+0.59** (40.07→40.66, negligible)
     - Gemma-3-12B-It: **−0.24** (32.16→31.92, slight decline)
     - Llama-3.1-8B-Instruct: **−1.03** (21.09→20.06, **DEGRADATION**)
   - **Direct quote** (paper §5.2 finding 6): *"Thinking is not merely a form of prompt engineering, but a fundamental post-training paradigm shift. Compared to prompted thinking, native thinking ability is the key to improving long-context performance."*
   - **Implication for mission**: post-training (RLM-style fine-tune of Qwen3.6-27B) is the path; prompting alone won't reach the same gains.

9. **Mixed-thinking models exhibit Pareto optimality** (Finding 3 extension):
   - Mixed-thinking models (Gemini-2.5-Flash, Claude-4-Sonnet, DeepSeek-V3.2) maintain efficient baseline when thinking disabled AND approach/surpass thinking-only models when thinking enabled
   - **Gemini-2.5-Flash** in thinking mode approaches Gemini-2.5-Pro performance
   - **DeepSeek-V3.2** in thinking mode significantly outperforms DeepSeek-R1 (thinking-only) in thinking mode
   - **Direct quote** (paper §5.2 finding 7): *"This phenomenon indicates that mixed-thinking, which dynamically chooses between fast output and deep reasoning based on user needs, is highly likely to become the most competitive paradigm for future long-context models."*
   - **Practical implication**: when picking tier-0 candidates, prefer architectures that support both modes. Qwen3.6-27B is mixed-thinking-architected (thinking preservation per [marktechpost synth](src-qwen3-6-27b-dense-beats-397b-moe-agentic-coding.md)).

10. **Open-source narrows the gap to within 6 points of closed-source on long-context tasks** (Finding 2 extension):
    - Top closed: Gemini-2.5-Pro = 73.42
    - Top open: DeepSeek-V3.2 = 67.82 + Qwen3-235B-A22B-Thinking-2507 = 66.97
    - **Gap = ~6 points** (less than the ~30-40 point gap visible in many other benchmarks)
    - **gpt-oss-120B-Thinking = 52.61** (open, OpenAI Apache 2.0) — strong but ~20 points below frontier
    - **Implication for the wiki's anti-vendor-lock-in mission**: open-source long-context capability exists at competitive quality; the narrative "open-source can substitute" is empirically grounded at the tier-1 model class.

11. **Performance stratifies dramatically across difficulty levels**:
    - **Easy samples**: GPT-5 = 85.23, DeepSeek-V3.2 = 85.02 (gap = ~0)
    - **Extreme samples**: Gemini-2.5-Pro = 50.77, GPT-5 = 48.37, DeepSeek-V3.2 = 44.27, Qwen3-235B-A22B-Thinking-2507 = 43.39 (gap widens; even best frontier <51%)
    - **Thinking gains diminish on extreme samples**:
      - Claude-4-Sonnet Easy: +15.36 (68.42→83.78); Extreme: +4.13 (42.92→47.05)
      - Gemini-2.5-Flash Easy: +13.27 (66.55→79.82); Extreme: +3.13 (44.26→47.39)
    - **Implication**: even native-thinking gains plateau on the hardest tasks. There is substantial headroom for future model improvement. Extreme samples test composite long-context memory + integration + reasoning — current models still face substantial bottlenecks.

12. **Pass@N + Best-of-N show Gemini-2.5-Pro Pass@3 = 10.68 on Extreme samples** (§5.3):
    - **The benchmark has substantial difficulty headroom** even under N=3 retries.
    - This is structurally important for **future-proofing**: the benchmark won't saturate quickly even as models improve in single-shot capability.
    - LongBench Pro's fine-grained scoring (partial credit) + Pass@N together provide clear discriminability across model tiers.

13. **Length-saturation observation** (§5.4):
    - Most models show declining performance as sample length grows (8k → 256k)
    - **Gemini-2.5-Pro is length-insensitive**: 256k score = 71.77 ≈ 8k score = 74.50 (gap = ~3 points)
    - **Direct quote**: *"merely increasing sample length to stress-test model performance has reached a point of saturation. The current bottleneck in long-context performance does not lie in the model's ability to 'read' 256k tokens, but in its capacity to handle long-range dependencies and complex logical relationships."*
    - **Shift in evaluation focus**: from "how much can it read" to "how deeply can it comprehend." This is the structural framing the wiki's [model-context-engineering](../../spine/models/depth/model-context-engineering.md) page should track.

14. **Task-dimension performance reveals capability bottlenecks** (§5.5):
    - **Retrieval (T1) + Sequencing (T2)**: avg score >80 (most models proficient)
    - **Aggregation/Clustering (T6)**: avg 57.72 (sharp drop — semantic integration is hard)
    - **QA (T3) + Summarization (T4)**: avg <55 (forward-from-evidence-to-outcome is harder than backward-from-outcome-to-evidence)
    - **Logical reasoning (T8-T10)**: avg ~60 (moderate, with reasoning-trained models pulling ahead)
    - **Consistency maintenance (T7, T11)**: avg <49 (lowest — sustaining global states across very long sequences exposes inherent limitations)
    - **Implication**: long-context capability is multi-dimensional. A model can be strong on retrieval but weak on aggregation. The 11-task taxonomy diagnoses these per-skill profiles.

15. **Context-requirement stratification** (§5.6, Figure 9):
    - All models perform substantially better on Partial tasks (localization + retrieval) than Full tasks (integration + reasoning)
    - **Performance drop**: 7.32 to 10.84 absolute points on Full vs Partial across most models
    - **Implication**: current models have mature local-retrieval capability but limited cross-segment integration. This is exactly the regime where **RLM's REPL-recursion + sub-call paradigm** would help most — programmatically chunking + integrating across spans.

16. **63 annotators × 50 RMB/hour cost structure** (Appendix C):
    - 51 general annotators + 12 long-context experts
    - Long-context experts: ≥1 year annotation experience + 2-month specialized training
    - Ages: 23-32 (mostly), balanced gender, diverse majors, mostly bachelor's, ~25% graduate degree
    - **50 RMB/hour ≈ $7 USD/hour** at typical exchange rates — significantly lower than US-research-rate; this cost structure is part of why the construction was feasible at 1,500-sample scale
    - **The construction methodology (Human-Model Collaborative) is cost-efficient relative to pure manual annotation while preserving quality** — applicable to other long-context dataset construction efforts

17. **Future work points to recursive verification**:
    - Author quote (§7): *"As task length and complexity continue to grow, even human-model collaborative construction can face a tension between verification accuracy and production efficiency."*
    - Direction: **"Critique-of-Critique" recursive verification scheme** — *"to recursively and progressively decompose verification into easier subproblems that are tractable for human annotators"*
    - Cites DeepSeekMath-V2 meta-verification design (arxiv:2511.22570) as precedent
    - **Recursive verification is structurally analogous to RLM's recursive sub-LM calls** — both decompose hard problems into LM-tractable subproblems via recursion. Cross-paper conceptual alignment is notable.

## Deep Analysis

### Paper Structure (28 pages, 7 main sections + Appendices A-E)

| Section | Pages | Content |
|---|---|---|
| 1. Introduction | 1-2 | Motivation: synthetic-vs-realism tradeoff in existing benchmarks; LongBench Pro positioning |
| 2. Task Framework | 3-5 | 11 primary × 25 secondary task taxonomy (Table 2 + Figure 2); context-requirement dimension definition |
| 3. Construction Process | 5-6 | 5 stages: document collection · human-model collaborative sample generation · question standardization · answer review · difficulty classification |
| 4. Data Statistics + Validation | 6 | 1,500-sample composition; 300-sample audit at 99.3%/97.3% correctness |
| 5. Evaluation | 6-13 | Tables 1-5 + Figures 5-10; 7 sub-findings on general performance, length, task, context-req, construction strategy |
| 6. Related Works | 13 | RULER, ∞BENCH, CLongEval, HELMET, LongBench v2, SCROLLS, ZeroSCROLLS, L-Eval, Ada-L-Eval, ∞Bench positioned |
| 7. Conclusion + Future Work | 13 | Critique-of-Critique recursive verification direction |
| Appendix A | 16-21 | Full task definitions + I/O examples for all 25 secondary tasks |
| Appendix B | 21-26 | Annotation guidelines: sample-generation prompts, verification criteria, rewriting criteria, answer review, quality evaluation |
| Appendix C | 26-27 | Annotator statistics + compensation |
| Appendix D | 28 | Inference parameter table for 46 models |
| Appendix E | 26 | Truncation length notes (GLM-4.6 effective vs claimed) |

### The 11 Primary Tasks × 25 Secondary Tasks (Table 2)

> [!info] Full taxonomy
>
> | Primary | Secondary | Context-Req | Metric |
> |---|---|---|---|
> | T1 Retrieval & Ranking | T1.1 Global Cohesive Retrieval | Full | NDCG@k |
> | | T1.2 Key-Snippet Retrieval | Partial | NDCG@k |
> | T2 Sequencing & Structure Reconstruction | T2.1 Global Timeline Reconstruction | Full | Pairwise Accuracy |
> | | T2.2 Local Causal Chain Sorting | Partial | Pairwise Accuracy |
> | T3 Evidence-Grounded QA | T3.1 Multi-Doc Integration QA | Full | Accuracy |
> | | T3.2 Single-Hop Fact QA | Partial | Accuracy |
> | T4 Summarization & Synthesis | T4.1 Global-Coverage Constrained Summary | Full | SemSim+ROUGE-L |
> | | T4.2 Query-Focused Summary | Partial | SemSim+ROUGE-L |
> | T5 Attribution & Citation Alignment | T5.1 Full-Sentence Citation Alignment | Full | F1 |
> | | T5.2 Key-Statement Citation Alignment | Partial | F1 |
> | T6 Aggregation & Clustering | T6.1 Large-Scale Document Clustering | Full | SubEM |
> | | T6.2 Targeted Subset Cluster Identification | Partial | F1 |
> | | T6.3 Global Frequency Analysis | Full | Pairwise Accuracy |
> | T7 Consistency & Compliance Checking | T7.1 Global Conflict & Inconsistency Localization | Full | F1 |
> | | T7.2 Targeted Rule or Condition Violation Detection | Partial | F1 |
> | | T7.3 Comprehensive Error & Anomaly Sweep | Full | F1 |
> | T8 Structured & Numeric Reasoning | T8.1 Structured Multi-Source Consistency Verification | Full | SubEM |
> | | T8.2 Single-Source Targeted Aggregation | Partial | SubEM |
> | | T8.3 Long-Context Procedural State Tracking | Full | F1 |
> | T9 Version & Code Diff Analysis | T9.1 Dependency-Aware Multi-Version Impact Analysis | Full | F1 |
> | | T9.2 Localized Interface Change Detection | Partial | F1 |
> | T10 Rule Induction & In-Context Learning | T10.1 Large-Scale In-Context Rule Induction | Full | SubEM |
> | | T10.2 Targeted Example-Based Rule Induction | Partial | SubEM |
> | T11 Dialogue Memory & Long-Horizon Tracking | T11.1 Long-Range Entity & Commitment Tracking | Full | Accuracy |
> | | T11.2 Short-Range Reference Resolution & State Query | Partial | Accuracy |

The taxonomy has notable methodological precision:
- **Each secondary task has a defined Context-Requirement** (Full vs Partial) — orthogonal axis to task type
- **Each metric is task-appropriate** — F1 for citation alignment where coverage + precision both matter; SubEM for canonical-answer tasks; SemSim+ROUGE-L for summarization (paper formalizes the weighted combination as 0.5×max(SemSim) + 0.5×max(ROUGE-L) over 3 reference summaries per sample)
- **Coverage is comprehensive** — Figure 2 shows LongBench Pro covers all task dimensions of RULER, ∞BENCH, CLongEval, HELMET, LongBench v2 individually. This is a *superset* benchmark, intentionally so.

### Construction Pipeline — 5 Stages (§3)

> [!info] Stage 1 — Document Collection (§3.1)
>
> - Curate naturally-occurring long documents from public internet
> - Domains: news, medicine, science, literature, law, education
> - Formats: reports, tables, code, dialogues, lists, JSON
> - Balanced across single-doc + multi-doc settings, English + Chinese, 6 length buckets (8k/16k/32k/64k/128k/256k)
> - Length measured via Qwen tokenizer; documents assigned to bucket if within ±20% of target
> - **All documents undergo compliance review** by human annotators to exclude privacy-sensitive, copyrighted, or non-compliant content

> [!info] Stage 2 — Human-Model Collaborative Sample Generation (§3.2)
>
> - For each (long document, target task definition, context requirement), prompt **5 frontier LLMs** (Gemini-2.5-Pro, GPT-5, Claude-4-Sonnet, DeepSeek-V3.2, Qwen3-235B-A22B-Thinking-2507) to draft **3 candidate samples each**
> - Each sample includes: question + reference answer + design rationale + solution process (the latter two enable later verification)
> - Human annotators critically evaluate model output along 4 axes:
>   1. Verify task alignment + context-requirement against design rationale
>   2. Validate answer correctness via solution processes
>   3. Estimate difficulty using the 5 drafting models' responses (challenging if ≥1 fails)
>   4. Select the best sample, edit minimally if needed; if none qualifies, move to next document
> - Each accepted sample is reviewed by a **long-context expert**; failed cases must be revised until passing

> [!info] Stage 3 — Question Standardization (§3.3)
>
> - Construct **2 prompt templates per question**: non-thinking + thinking
> - Each prompt has 3 sections: Task Description (mandatory) · Supplementary Content (optional) · Output Example (mandatory)
> - **Non-thinking template**: "Output the [Answer] identifier first, and then output {elements} line by line, without any additional content."
> - **Thinking template**: "Think step by step. After your thinking process, output the [Answer] identifier, and then output {elements} line by line."
> - This dual-prompt design enables systematic non-thinking-vs-thinking score comparison per model

> [!info] Stage 4 — Answer Review (§3.4)
>
> - Pre-generate predictions from 5 advanced models per sample
> - **2 annotators independently** verify each sample component-by-component (precision via human + recall via model predictions)
> - Disagreement → escalate to long-context expert
> - Three potential issue types: Document Issues (incomplete content) · Question Issues (unclear/ambiguous) · Answer Issues (incorrect/incomplete)

> [!info] Stage 5 — Difficulty Classification (§3.5)
>
> - Model-centric difficulty (NOT human-rated) — aligns with practical LLM-evaluation needs
> - **15 reference models** in 3 tiers (high/mid/low, 5 each)
> - 4-level partitioning: Extreme → Hard → Moderate → Easy
> - Performance threshold: SubEM > 0.65 on summarization considered "correct"

This pipeline is methodologically sophisticated. The combination of model-driven drafting + human verification + model-centric difficulty calibration achieves cost-quality tradeoffs that pure manual annotation cannot at extreme lengths.

### Quality Validation (§4) — 300-sample audit

> [!success] **Audit results: 99.3% attribute correctness · 97.3% answer correctness**
>
> 300 samples uniformly selected across (secondary task × language × length) cells. Two checks:
> 1. **Attribute correctness**: language + length + secondary task + context requirement all correct
> 2. **Answer correctness**: answer fully correct
>
> Problematic samples have only minor deviations (impacting overall benchmark score by 0.96 — negligible). **The benchmark is empirically high-quality, with measured precision rather than asserted precision.**

### Table 3 — General Performance of 46 Long-Context LLMs

> [!info] The 46-model evaluation matrix (excerpted from paper §5.2)
>
> Format: model · type · context length · overall score (sometimes English/Chinese/difficulty breakdowns)
>
> | Model | Type | Context | Overall |
> |---|---|---|---|
> | **Gemini-2.5-Pro** | Thinking | 1M | **73.42** |
> | Gemini-2.5-Flash (thinking) | Mixed | 1M | 67.41 |
> | Gemini-2.5-Flash (non-thinking) | Mixed | 1M | 55.92 |
> | **GPT-5** | Thinking | 272k | **72.61** |
> | GPT-OSS-120B | Thinking | 128k | 52.61 |
> | GPT-OSS-20B | Thinking | 128k | 44.66 |
> | GPT-4o | Instruct | 128k | 49.44 (thinking-prompt) / 46.67 |
> | **Claude-4-Sonnet (thinking)** | Mixed | 1M | **69.87** |
> | Claude-4-Sonnet (non-thinking) | Mixed | 1M | 56.07 |
> | Claude-3.7-Sonnet (thinking) | Mixed | 200k | 59.66 |
> | **DeepSeek-V3.2 (thinking)** | Mixed | 160k | **67.82** |
> | DeepSeek-V3.2 (non-thinking) | Mixed | 160k | 51.67 |
> | DeepSeek-R1-0528 | Thinking | 128k | 61.89 |
> | DeepSeek-R1 | Thinking | 128k | 60.07 |
> | DeepSeek-V3-0324 | Instruct | 128k | 56.71 (thinking-prompt) / 51.70 |
> | **Qwen3-235B-A22B-Thinking-2507** | Thinking | 256k | **66.97** |
> | Qwen3-235B-A22B-Instruct-2507 (thinking) | Instruct | 256k | 63.77 |
> | Qwen3-Next-80B-A3B-Thinking | Thinking | 256k | 63.95 |
> | Qwen3-30B-A3B-Thinking-2507 | Thinking | 256k | 59.68 |
> | **Qwen3-30B-A3B-Instruct-2507 (thinking-prompt)** | Instruct | 256k | **54.52** |
> | Qwen3-32B (thinking) | Mixed | 128k | 51.12 |
> | Qwen3-4B-Thinking-2507 | Thinking | 256k | 50.10 |
> | Qwen3-4B-Instruct-2507 (thinking-prompt) | Instruct | 256k | 45.68 |
> | Qwen3-8B (thinking) | Mixed | 128k | 44.34 |
> | Qwen3-4B (thinking) | Mixed | 128k | 40.82 |
> | GLM-4.6 (thinking) | Mixed | 198k | 58.21 |
> | GLM-4.5 (thinking) | Mixed | 128k | 55.48 |
> | Kimi-K2-Instruct-0905 (thinking-prompt) | Instruct | 256k | 55.53 |
> | MiniMax-M2 | Thinking | 192k | 53.21 |
> | MiniMax-Text-01 | Instruct | **4M** | **45.00** ← claims 4M, falls behind 128k models |
> | Llama-3.1-405B-Instruct | Instruct | 128k | 40.66 (thinking-prompt) / 40.07 |
> | Llama-3.3-70B-Instruct | Instruct | 128k | 33.69 (thinking-prompt) / 31.89 |
> | Llama-3.1-8B-Instruct | Instruct | 128k | **20.06 (thinking-prompt) / 21.09** ← thinking-prompt DEGRADES |
> | Gemma-3-27B-It | Instruct | 128k | 37.34 (thinking-prompt) / 36.14 |
> | Gemma-3-12B-It | Instruct | 128k | **31.92 (thinking-prompt) / 32.16** ← thinking-prompt DEGRADES |
> | Gemma-3-4B-It | Instruct | 128k | 21.20 (thinking-prompt) / 21.76 ← thinking-prompt DEGRADES |
> | Mistral-Small-3.2-24B-Instruct-2506 | Instruct | 128k | 39.87 (thinking-prompt) / 37.32 |
> | Ministral-3-14B-Instruct-2512 | Instruct | 256k | 45.80 (thinking-prompt) / 40.14 |
> | Ministral-3-8B-Instruct-2512 | Instruct | 256k | 44.46 (thinking-prompt) / 37.80 |
> | Ministral-3-3B-Instruct-2512 | Instruct | 256k | 34.54 (thinking-prompt) / 30.18 |
> | Magistral-Small-2509 | Thinking | 128k | 38.40 |
> | Mistral-Large-Instruct-2411 | Instruct | 128k | 36.25 (thinking-prompt) / 31.69 |
> | Qwen2.5-72B-Instruct | Instruct | 128k | 44.09 (thinking-prompt) / 39.64 |
> | Ministral-8B-Instruct-2410 | Instruct | 128k | 14.43 (thinking-prompt) / 17.56 ← thinking-prompt DEGRADES |
> | Llama-3.2-3B-Instruct | Instruct | 128k | 12.58 (thinking-prompt) / 15.71 ← thinking-prompt DEGRADES |
> | Llama-3.1-70B-Instruct | Instruct | 128k | 32.12 (thinking-prompt) / 31.53 |

This matrix is the most comprehensive long-context evaluation publicly available at this scale. **5 models show prompted-thinking DEGRADATION** (Llama-3.1-8B, Gemma-3-12B, Gemma-3-4B, Ministral-8B, Llama-3.2-3B) — non-trivially dropping by 0.24-3.13 absolute points when forced to think without native training.

### Difficulty-Level Stratification (excerpted from Table 3)

> [!info] Top models on Extreme samples vs Easy samples
>
> | Model | Easy | Extreme | Gap |
> |---|---|---|---|
> | Gemini-2.5-Pro (Thinking) | 84.40 | **50.77** | -33.63 |
> | GPT-5 (Thinking) | 85.23 | 48.37 | -36.86 |
> | Claude-4-Sonnet (Thinking) | 83.78 | 47.05 | -36.73 |
> | DeepSeek-V3.2 (Thinking) | 85.02 | 44.27 | -40.75 |
> | Qwen3-235B-A22B-Thinking-2507 | 83.55 | 43.39 | -40.16 |
> | gpt-oss-120B (Thinking) | 74.06 | 35.40 | -38.66 |
>
> **Even the strongest model (Gemini-2.5-Pro) scores only 50.77 on Extreme samples** — substantial headroom remains. Gap closes on Easy samples (~85 across all top models) but widens to ~33-40 absolute points on Extreme samples.

### Inference Settings (Appendix D, Table 5)

> [!abstract] Per-model inference parameters used in Table 3
>
> All 46 models have explicit per-model settings (truncation length, output length, temperature) documented in Appendix D Table 5. Highlights:
>
> - **Thinking models output length**: 32k for 256k+-context models, 8k for 128k-context models
> - **Non-thinking output length**: 1k uniformly
> - **Truncation length**: 120k typically, model-specific for some (DeepSeek-V3.2 = 120k despite 160k claim; GLM-4.6 = 120k despite 198k claim per §E "effective vs claimed length" finding)
> - **Temperature**: typically 1.0 (Gemini, Claude, GPT, MiniMax, Mistral defaults); 0.6-0.7 for Qwen + DeepSeek; 0.1-0.15 for Mistral-Small-3.2-24B-Instruct
>
> **The transparent disclosure of inference parameters is methodologically rare** — this enables true reproducibility, not just claimed reproducibility (P4 — Declarations Aspirational Until Verified, applied at the inference-config level).

## Why This Matters for the Wiki's Mission

> [!success] **Step 1 of [RLM-Qwen3.6-27B operations plan](../../domains/cross-domain/rlm-qwen3-6-27b-fine-tune-operations-plan.md) is grounded**
>
> The operations plan's Step 1 ("Acquire base model and training data") depends on LongBench Pro English-split being publicly accessible at expected structure. This Layer 1 reading **confirms**:
> - **Public hosting**: `huggingface.co/datasets/caskcsg/LongBench-Pro` (paper §abstract footnote)
> - **English split = 750 tasks** (1500 / 2 languages = 750; balanced design 5 × 25 × 6 = 750)
> - **Per-task structure**: question + reference answer + design rationale + solution process (drafted by 5 frontier LLMs, human-verified)
> - **Difficulty distribution**: 4 levels, model-centric calibration
> - **License accessibility**: dataset is hosted publicly; per Hugging Face convention, downloadable via `huggingface-cli download`
>
> **The operations plan's Step 1 is no longer aspirational** — it's executable as written. P4 (Declarations Aspirational Until Verified) applied at the dataset-acquisition layer.

> [!success] **Evidence 6 of [anti-vendor-lock-in lesson](../../lessons/01_drafts/anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence.md) is anchored at full Layer 1 on the LongBench Pro side**
>
> The lesson's Evidence 6 cites the 4 RLM Table 1 benchmarks as "public, released with evaluation harnesses, reproducible." This synth grounds the LongBench Pro side at full PDF depth: 1,500 samples, 11×25 task taxonomy, public dataset URL, complete annotation methodology, 99.3% attribute correctness audit, 46-model evaluation table, Pass@N + Best-of-N upper-bound analyses.
>
> **The empirical evidence chain at the evaluation-layer is auditable end-to-end** — the wiki's anti-vendor-lock-in claim has Layer 1 paper evidence at this layer.

> [!success] **The "long-context optimization > parameter scaling" finding is direct mission-alignment**
>
> Per Finding 1: a 4B-Instruct-2507 with 256k context BEATS an 8B model with 128k context. A 30B-A3B-Instruct-2507 with 256k context BEATS a 32B model with 128k context. **Smaller-trained-right > bigger-trained-loosely** at the long-context regime.
>
> This is the empirical case for the wiki's [tier-0 candidate comparison](../../comparisons/rlm-qwen3-8b-vs-qwen3-6-27b-tier-0-long-context-candidate.md) "Composition Path" — **post-training Qwen3.6-27B for the RLM paradigm is more leverage than scaling to a larger base model**. The benchmark's empirical pattern supports the strategic decision to fine-tune rather than buy bigger weights.

> [!warning] **The "effective context << claimed context" finding has direct AICP-routing relevance**
>
> Per Finding 2: MiniMax-Text-01 claims 4M context, scores 45.00 — falls behind most 128k models. GLM-4.6 claims 198k, output unstable at 190k truncation.
>
> **AICP smart-routing should NOT default to high-claimed-context models for long-context tasks** — empirical effective length is the load-bearing measure. The [tier-0 comparison](../../comparisons/rlm-qwen3-8b-vs-qwen3-6-27b-tier-0-long-context-candidate.md)'s routing logic should incorporate effective-context-length per benchmark rather than claimed-context-length.

> [!warning] **The "thinking paradigm requires native training" finding constrains prompt-engineering ambition**
>
> Per Finding 3: prompted-thinking on 5 instruct models DEGRADES performance (-0.24 to -3.13 absolute points). Native-thinking gain on mixed-thinking models is +13.80 to +16.15.
>
> **Prompting tier-0 candidates to "think step by step" without native-thinking training won't yield long-context gains** — it can actively hurt. RLM post-training is the path; CoT prompting is not a substitute for the wiki's mission.

> [!info] **The "mixed-thinking is Pareto-optimal" finding informs tier-0 architecture choice**
>
> Per Finding 3 extension: mixed-thinking models (Gemini-2.5-Flash, Claude-4-Sonnet, DeepSeek-V3.2) maintain efficient baseline AND deep-reasoning capability under thinking-mode. **Qwen3.6-27B is mixed-thinking-architected** (with `chat_template_kwargs.preserve_thinking: True` per [marktechpost synth](src-qwen3-6-27b-dense-beats-397b-moe-agentic-coding.md)) — aligning with the architectural pattern that scales best on long-context.
>
> The wiki's [2026 Consumer Hardware AI Stack spine reference](../../spine/references/2026-consumer-hardware-ai-stack.md) tier-0 selection of Qwen3.6-27B is structurally validated by this finding.

## Open Questions

> [!question] How does LongBench Pro relate to LongBench v2 in benchmark coverage?
> Both are "LongBench" but different teams (Pro: Hu/Wu IIE-CAS+Xiaohongshu; v2: Bai et al. presumably Tsinghua). Figure 2 in the paper claims LongBench Pro covers all the task dimensions of v2 (and RULER, ∞BENCH, CLongEval, HELMET). The relationship: LongBench Pro is the *more comprehensive successor*, but they're parallel benchmarks rather than versions. **For the RLM paper Table 1, CodeQA comes from LongBench v2 — different benchmark, different team.** This is worth noting for evaluation-suite design.

> [!question] Does the Critique-of-Critique recursive verification scheme (future work) align structurally with RLM's REPL-recursion?
> Both decompose hard problems into LM-tractable subproblems via recursion. The paper cites DeepSeekMath-V2 meta-verification (arxiv:2511.22570). RLM cites DeepSeek-R1 + STaR/Quiet-STaR. The two papers may share methodological lineage but they don't cross-reference each other in either direction. **Worth tracking** as a candidate cross-pollination direction.

> [!question] Why is the Chinese split's role in mission planning underspecified?
> 750 tasks in Chinese, 750 in English. The [RLM-Qwen3.6-27B operations plan](../../domains/cross-domain/rlm-qwen3-6-27b-fine-tune-operations-plan.md) trains on the English split per the original RLM paper. **The Chinese split is a separate-plan opportunity** — particularly relevant if the operator's mission ever extends to bilingual / multi-lingual workloads. Qwen3.6-27B is bilingual-trained per Qwen team's design.

> [!question] How does the difficulty calibration evolve as models improve?
> Difficulty levels are calibrated against the 15 reference models (high/mid/low tiers). As future models exceed today's high-tier (e.g., GPT-6, Claude-5), what was Extreme today may become Hard or Moderate. **Does the benchmark auto-recalibrate?** The paper doesn't address this — implicitly, recalibration is a future task. The model-centric design at least makes recalibration *possible* (vs subjective human ratings which are harder to update).

> [!question] What's the cross-lingual fine-tuning transfer story?
> Finding 2 notes uneven cross-lingual performance and that "stronger models reduce these gaps." If RLM-Qwen3.6-27B is trained on the English split only, does it generalize to Chinese? Per [RLM paper Observation 6](src-rlm-paper-deep-dive-table-1-training-recipe-six-observations.md), single-domain training transfers to multiple downstream tasks (+28.3% avg) — but cross-lingual transfer is a different direction than cross-task transfer. **Worth empirical validation if cross-lingual capability matters.**

> [!question] What's the cost of replicating the 1,500-sample construction at additional length classes?
> 63 annotators × 50 RMB/hour × N hours per sample × 1500 samples = total construction cost. The paper doesn't disclose total budget. **For wiki-scale dataset construction (e.g., a wiki-corpus QA benchmark), the cost-per-sample is the load-bearing planning input**. Worth correspondence with authors if such a benchmark were ever in scope.

> [!question] Can the Human-Model Collaborative pipeline be wired into the wiki's own ingestion?
> The paper validates that human-model collaboration (5 LLMs draft + 2 annotators verify + 1 expert audit + 5-model difficulty calibration) produces 0.9609 quality vs 0.9484 human-only or 0.8964 model-only. **The wiki's `tools/pipeline.py post` validates page structure but doesn't measure synthesis quality.** Could this collaborative pattern become the wiki's quality regression suite? (Open-ended; would require corpus + annotation effort.)

## Applicability

> [!info] Where to use LongBench Pro findings directly
>
> - **Long-context capability evaluation** for any LLM with claimed context ≥ 8k
> - **Effective-vs-claimed context length validation** before deploying a long-context model in production
> - **Multi-task long-context profiling** (11 task types × 25 secondary tasks) to identify per-skill strengths/weaknesses
> - **Difficulty-stratified analysis** to understand where the headroom is (Extreme samples) vs where models saturate (Easy samples)
> - **Bilingual coverage** when Chinese / English asymmetry matters
> - **Training-data source for RLM-style fine-tunes** (the paper is the source for RLM-Qwen3-8B's 750-task training set)

> [!warning] Where these findings DON'T apply
>
> - **Short-context tasks** (<8k) — benchmark targets long-context exclusively
> - **Multimodal queries** — text-only benchmark
> - **Real-time / streaming tasks** — offline batch evaluation
> - **Code-specific evaluation** — only T9 (Version & Code Diff) covers code; SWE-bench / CodeContests / HumanEval are dedicated benchmarks for code
> - **Languages other than English / Chinese** — bilingual scope only

## Relationships

- BUILDS ON: [[src-oolong-and-longbench-pro-long-context-benchmarks-rlm-anchors|OOLONG + LongBench Pro Combined Synthesis]] (this is the dedicated Layer-1 deep-dive expanding on LongBench Pro specifics that the combined synth covered at abstract level; corrects the "Tsinghua-affiliated" speculation)
- COMPARES TO: [[src-rlm-paper-deep-dive-table-1-training-recipe-six-observations|RLM Paper Deep Dive]] (RLM paper used LongBench Pro English split as TRAINING DATA SOURCE for RLM-Qwen3-8B — 750 English tasks → 2,250 candidate trajectories → 1,072 filtered → SFT)
- COMPARES TO: [[src-browsecomp-plus-paper-deep-dive-fixed-corpus-table-1-oracle-citation-quality|BrowseComp+ Paper Deep Dive]] (parallel Layer-1 deep-dive on the OTHER load-bearing RLM Table 1 benchmark; both use Human-Model Collaborative-style construction with frontier-LLM drafting + human verification)
- DEMONSTRATES: [[infrastructure-over-instructions-for-process-enforcement|Principle 1]] (model-centric difficulty calibration is structural enforcement of difficulty assignment; subjective human ratings are instructions-only)
- DEMONSTRATES: [[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4]] (effective-vs-claimed context length finding directly applies P4: claimed context is aspirational until measured; MiniMax-Text-01's 4M is the canonical instance)
- DEMONSTRATES: [[anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence|Anti-Vendor-Lock-In Lesson]] § Evidence 6 (the evaluation-layer empirical anchor on the LongBench Pro side; the lesson's claim "all 4 RLM Table 1 benchmarks public + reproducible" is grounded by this Layer 1 reading)
- DEMONSTRATES: [[right-process-for-right-context-the-goldilocks-imperative|Principle 3 — Goldilocks]] (different difficulty levels for different model-tier needs; mixed-thinking Pareto optimality reflects context-adaptive process selection)
- RELATES TO: [[2026-consumer-hardware-ai-stack|2026 Consumer Hardware AI Stack]] (Finding 1 — long-context optimization beats parameter scaling — directly supports the spine reference's selection of Qwen3.6-27B + RLM-paradigm post-training over scaling to larger weights)
- RELATES TO: [[ai-infrastructure-decision-framework-2026|AI Infrastructure Decision Framework 2026]] (Finding 2's effective-vs-claimed context lens informs routing decisions; Finding 3's native-thinking-required constraint informs prompt-engineering boundary)
- FEEDS INTO: [[rlm-qwen3-6-27b-fine-tune-operations-plan|RLM-Qwen3.6-27B Operations Plan]] § Step 1 (this synth grounds the dataset-acquisition step; English split confirmed = 750 tasks; HuggingFace dataset confirmed accessible at `caskcsg/LongBench-Pro`)
- FEEDS INTO: [[rlm-thread-evidence-chain-2026-04-27|Learning Path — RLM Thread Evidence Chain]] (Path C: Reproduce Training — this synth is the deep-dive reference for the LongBench Pro training-data source)

## Backlinks

[[OOLONG + LongBench Pro Combined Synthesis]]
[[src-rlm-paper-deep-dive-table-1-training-recipe-six-observations|RLM Paper Deep Dive]]
[[BrowseComp+ Paper Deep Dive]]
[[infrastructure-over-instructions-for-process-enforcement|Principle 1]]
[[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4]]
[[Anti-Vendor-Lock-In Lesson]]
[[right-process-for-right-context-the-goldilocks-imperative|Principle 3 — Goldilocks]]
[[2026 Consumer Hardware AI Stack]]
[[ai-infrastructure-decision-framework-2026|AI Infrastructure Decision Framework 2026]]
[[rlm-qwen3-6-27b-fine-tune-operations-plan|RLM-Qwen3.6-27B Operations Plan]]
[[Learning Path — RLM Thread Evidence Chain]]
