---
title: "Synthesis — BrowseComp-Plus Paper Deep Dive: Fixed 100K Corpus, Tables 1-8 Across 11 LLMs × 5 Retrievers, Oracle 93.49%, Citation Quality, API Cost (arXiv 2508.06600 v1, Aug 2025)"
aliases:
  - "BrowseComp-Plus Paper Deep Dive"
  - "BrowseComp+ Deep Dive"
  - "BrowseComp+ Tables 1-8"
  - "BrowseComp+ Oracle 93.49%"
type: source-synthesis
domain: tools-integration
status: synthesized
confidence: high
maturity: seed
created: 2026-04-27
updated: 2026-04-27
last_reviewed: 2026-04-27
sources:
  - id: browsecomp-plus-paper-pdf
    type: paper
    url: https://arxiv.org/pdf/2508.06600
    file: raw/papers/browsecomp-plus-a-more-fair-and-transparent-evaluation-benchmark-of-deep-researc.md
    title: "BrowseComp-Plus arXiv 2508.06600 v1 (8 Aug 2025) — Full PDF"
    description: "26 pages with appendix; 1334-line raw scrape. Authors: 20 (lead Zijian Chen, Xueguang Ma — University of Waterloo); affiliations span U Waterloo + CSIRO + CMU + U Queensland; senior authors Wenhu Chen, Jimmy Lin (UW IR-research group)."
    ingested: 2026-04-27
  - id: browsecomp-plus-abstract-companion
    type: wiki
    file: wiki/sources/tools-integration/src-browsecomp-plus-and-longbench-v2-rlm-table-1-benchmarks.md
    description: "Abstract-level companion synthesis covering BrowseComp+ AND LongBench v2 together at Layer 0/1; this page is the dedicated Layer-1 deep-dive on BrowseComp+ alone, sourced from the full PDF rather than the abstract page"
  - id: browsecomp-original
    type: paper
    url: https://arxiv.org/abs/2504.12516
    title: "BrowseComp (Wei et al., OpenAI, Apr 2025)"
    description: "Original BrowseComp benchmark — 1,266 fact-seeking questions; BrowseComp-Plus derives from this by adding fixed corpus + human-verified evidence + mined negatives"
  - id: rlm-paper-deep-dive
    type: wiki
    file: wiki/sources/tools-integration/src-rlm-paper-deep-dive-table-1-training-recipe-six-observations.md
    description: "RLM paper deep-dive — used BrowseComp+ at 1K-doc subset (~6-11M tokens) as Table 1 task; RLM(GPT-5) achieved 91.3% where base GPT-5 hit context limit at 0.0%"
  - id: anti-vendor-lock-in-lesson
    type: wiki
    file: wiki/lessons/01_drafts/anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence.md
    description: "Mission framing — Evidence 2 cites the +14pt retriever swap finding (BM25 → Qwen3-Embedding-8B on GPT-5) as the open-source-retrieval-layer empirical anchor; this synth grounds that finding in full-paper detail"
  - id: qwen3-embedding-paper
    type: paper
    url: https://arxiv.org/abs/2506.05176
    title: "Qwen3 Embedding (Zhang et al., Jun 2025)"
    description: "The retrieval model that produces the +14pt swing — referenced from BrowseComp+ paper as ref [26]"
  - id: search-r1-paper
    type: paper
    url: https://arxiv.org/abs/2503.09516
    title: "Search-R1 (Jin et al., Mar 2025)"
    description: "Open-source RL-trained search agent — represents the lower bound (3.86% with BM25) in the BrowseComp+ matrix"
  - id: reasonir-paper
    type: paper
    url: https://arxiv.org/abs/2504.20595
    title: "ReasonIR (Shao et al., Apr 2025)"
    description: "Reasoning-tuned dense retriever; nDCG@10 = 16.8 (between Qwen3-Embed-4B at 14.0 and 8B at 20.3)"
tags: [browsecomp-plus, deep-research-agents, fixed-corpus-evaluation, ir-research, retriever-disentanglement, qwen3-embedding-8b, search-r1, gpt-oss, gpt-5, oracle-retrieval, citation-quality, reasoning-effort-ablation, api-cost, jimmy-lin, wenhu-chen, university-of-waterloo, csiro, mit-csail-connection-via-rlm-table-1, mission-2026-04-27, anti-vendor-lock-in, paper-deep-dive, paper-pdf-layer-1]
---

# Synthesis — BrowseComp-Plus Paper Deep Dive

## Summary

The arXiv 2508.06600 v1 paper PDF (8 Aug 2025; 26 pages with Appendix; 1334-line raw scrape) supplies the full empirical detail the [combined abstract-level synthesis](src-browsecomp-plus-and-longbench-v2-rlm-table-1-benchmarks.md) compressed into a single section. **Twenty authors led by Xueguang Ma (University of Waterloo, correspondence) with senior authors Wenhu Chen + Jimmy Lin and collaborators across CSIRO + CMU + University of Queensland** — IR-research-rigor lineage from Lin's BM25/ColBERT/Pyserini group. The benchmark's distinguishing claim from the abstract — fairness + transparency via fixed corpus + retriever-disentanglement — is grounded in this paper by **Tables 1-8 across 11 LLMs × 5 retrievers (30+ result rows)**, a **3-stage corpus-construction pipeline** (o3 evidence-gathering → 14-annotator × 400+-hour human verification with cross-validation showing >80% agreement → GPT-4o sub-query decomposition for hard-negative mining via SerpAPI), **5 ablation studies** (reasoning effort × 6 modes; document reading strategy with get-doc tool; corpus size at 9.77M docs; oracle retrieval at 93.49%; alternative retrievers including ReasonIR-8B), and **API-cost analysis (Table 8) showing Opus 4 = $1,842 vs GPT-5 = $361 vs Gemini 2.5 Flash = $41 per full benchmark run**. This synthesis covers what the paper adds beyond what the abstract or RLM-paper Table 1 row could establish: the precise corpus statistics (100,195 documents · 830 queries · 6.1 evidence + 76.28 negatives + 2.9 gold per query · doc averages 5,179 words / 32,296 chars), the precise model-retriever matrix that the +14-point Qwen3-Embedding-8B claim emerges from, the **oracle-retrieval finding (gpt-4.1 hits 93.49% with all positive docs vs 14.58% with BM25)** that proves the bottleneck is retrieval not reasoning, and the **citation-quality table** that documents how often each model cites correct supporting documents (GPT-5 + Qwen3-Embed-8B: 98% coverage, 83.4% precision, 4.28 avg citations).

## Reference Card

> [!info] Paper deep-dive reference card

| Field | Value |
|---|---|
| **Paper** | arXiv 2508.06600 v1, dated 8 Aug 2025 (cs.CL) |
| **Length** | 26 pages with Appendix · 1334-line raw scrape |
| **Authors** | 20 — lead authors Zijian Chen, Xueguang Ma (correspondence: x93ma@uwaterloo.ca), Shengyao Zhuang; senior authors **Wenhu Chen**, **Jimmy Lin** |
| **Affiliations** | University of Waterloo (1, lead) · CSIRO (2) · Independent (3) · Carnegie Mellon (4) · University of Queensland (5) |
| **Project page** | https://texttron.github.io/BrowseComp-Plus/ |
| **Final corpus** | **100,195 documents**, **830 queries** |
| **Per-query averages** | 6.1 evidence docs · 76.28 negatives · 2.9 gold docs |
| **Per-doc averages** | 5,179.2 words · 32,296.2 chars |
| **Source coverage rate (truncation)** | 86.5% of queries have ground-truth answer in at least one of their gold docs within first 512 tokens |
| **Annotator effort** | 14 university student annotators · **400+ hours of manual verification** · cross-validation on >80% of labels |
| **LLMs evaluated** | 11 (gpt-4.1, o3, gpt-5, Sonnet 4, Opus 4, Gemini 2.5 Flash, Gemini 2.5 Pro, gpt-oss-20B/120B × low/medium/high reasoning modes, Qwen3-32B, SearchR1-32B) |
| **Retrievers evaluated** | 5 (BM25, Qwen3-Embedding-0.6B/4B/8B, ReasonIR-8B) |
| **Top accuracy in matrix** | **GPT-5 + Qwen3-Embedding-8B = 70.12%** (3.51 search calls, 9.11% calibration error) |
| **Bottom accuracy in matrix** | **SearchR1-32B + BM25 = 3.86%** |
| **Oracle accuracy (all positive docs given)** | **gpt-4.1 = 93.49%** · Qwen3-32B = 83.25% |
| **Top citation precision** | GPT-5 + Qwen3-Embed-8B: 83.4% precision, 4.28 avg citations |
| **Most expensive run (Table 8)** | **Opus 4 + Qwen3-Embed-8B = $1,842.48** for 830 queries |
| **Cheapest run (Table 8)** | **Gemini 2.5 Flash + Qwen3-Embed-8B = $41.29** |
| **Released** | Yes — benchmark data + evaluation scripts + baselines all public |
| **Confidence** | high — full paper PDF read (lines 1-1334) including all 8 tables, 5 ablation studies, all 7 appendices (prompts, labelling UI, problematic cases, hard-negative-mining prompts, evaluation prompts, API cost table); raw is the actual paper, not the abstract page |
| **Mission relevance** | Critical — Evidence 2 in the [anti-vendor-lock-in lesson](../../lessons/01_drafts/anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence.md) (the retrieval-layer empirical anchor) traces specifically to this paper's Table 1 |

## Key Insights

1. **The full LLM × retriever matrix is much richer than the headline numbers**. Beyond GPT-5 = 70.12% (top) and SearchR1+BM25 = 3.86% (bottom), the paper documents intermediate clustering:
   - **Proprietary tier with Qwen3-Embedding-8B**: GPT-5 = 70.12% > o3 = 63.49% > gpt-oss-120B-high = 42.89% > gpt-4.1 = 35.42% > Sonnet 4 = 36.75% ≈ Opus 4 = 36.14% > Gemini 2.5 Flash = 33.01% > Gemini 2.5 Pro = 28.67%
   - **gpt-oss-120B-high beats Sonnet 4 AND Opus 4** at this benchmark — the strongest open-source result in the matrix and a load-bearing data point for the wiki's open-source-stack-viability case
   - **Open-source 32B class** (Qwen3-32B, SearchR1-32B) plateaus at ~10% even with the best retriever — open-source weakness is **iterative tool-use / search-call discipline**, not factual reasoning (proven by oracle retrieval below)

2. **Stronger retrievers improve accuracy AND reduce search calls**. From Table 1, comparing BM25 → Qwen3-Embedding-8B with the SAME LLM: GPT-5 search calls drop from 23.23 → 21.74 (with +14pt accuracy gain); o3 drops 25.93 → 23.97; Sonnet 4 drops 9.95 → 9.03. Better retrieval = first-search-result more useful = fewer follow-up queries needed. **API cost falls accordingly** (Table 8): GPT-5 + BM25 = $400.36 → GPT-5 + Qwen3-Embed-8B = $360.71 (-$40 per benchmark run).

3. **Oracle retrieval reveals the actual bottleneck**. When gpt-4.1 is given ALL labeled positive documents directly (no retrieval phase), it achieves **93.49% accuracy** on BrowseComp-Plus — vs 14.58% with BM25 retrieval. **The gap (78.91 absolute points) is retrieval-attributable**, not reasoning-attributable. Even Qwen3-32B (open-source) hits 83.25% in the oracle setting; its weak end-to-end performance (~10% with embedding retriever) is mostly a **tool-use-iteration deficit**, not a reasoning deficit. *"open-source models do not substantially lag behind proprietary models in their ability to answer questions when provided with sufficient evidence. Instead, their primary limitation lies in performing interleaved reasoning with the search tool"* (paper §4.8.1).

4. **Citation quality matrix (Table 3) is a separate competence dimension**. GPT-5 + Qwen3-Embed-8B leads with **98% citation coverage, 4.28 avg citations, 83.4% precision, 62.3% recall**. o3 + Qwen3-Embed-8B is best on precision (91.8%) but lower coverage (78%). Open-source Qwen3-32B has 90% coverage but 8.9-20% precision — it cites *something* but rarely cites the right thing. **Citation precision and answer accuracy are correlated but distinct**: a model can answer correctly while citing wrong docs (unfaithful) or fail to answer while citing right docs (correctly-grounded but reasoning-failed).

5. **Reasoning effort scales monotonically (Table 4)**. gpt-oss-20B with Qwen3-Embed-8B: low = 13.37%, medium = 29.88%, high = 34.58% — accuracy more than 2.5× from low → high. Search-call counts scale similarly: low ≈ 2 calls, medium ≈ 14, high ≈ 24. **Calibration error decreases with reasoning** (better confidence-correctness alignment): low = 36.34% → high = 27.81%. **gpt-oss-120B-high is the strongest open-source data point** at 42.89% — surpasses Opus 4 — providing direct evidence that *open-source can match-or-beat closed-source on agentic search when reasoning effort is high*.

6. **The "open-source doesn't iterate enough" finding is structural**. Qwen3-32B and SearchR1-32B make **<2 search calls per query** despite being explicitly prompted to use the tool, while GPT-5 and o3 make 20+ calls. This isn't a reasoning gap — it's a tool-use behavior gap. Per the paper: *"This reflects a test-time scaling effect: more exhaustive search correlates with better outcomes and aligns with prior findings that reasoning-intensive queries benefit from multi-turn, exploratory retrieval."* RL-trained agents (Search-R1) do iterate more than base Qwen3-32B (1.78 vs 0.92 calls) but still fall far short of proprietary search-agent behavior.

7. **The 100K corpus is empirically validated as sufficient** (Section 4.8.4). The authors expanded the corpus 10× (adding Fineweb-edu 10BT, total 9,771,311 docs). BM25 effectiveness *improved* (better IDF estimation in larger corpus). Neural retrievers' measured effectiveness *decreased* (because added docs are unjudged → false negatives in TREC-style evaluation). End-to-end accuracy showed **minimal differences** between 100K and 9.77M corpora — validating that the 100K corpus's evaluation conclusions don't depend on corpus size. This is structurally important for **reproducibility**: researchers can reproduce on the smaller corpus without losing benchmark validity.

8. **Document-reading strategy matters (Section 4.8.3, Table 5)**. Extending the agent with a `get-document` tool (full-document reading vs 512-token preview only) gives **gpt-4.1 +8 absolute points** (35.42% → 43.61%) with 1.85 avg get-doc calls per query. Qwen3-32B gets only +1.3 points (limited by its ability to recognize when to use the tool). **This validates the wiki's [structured-context-as-IaC](../../spine/models/agent-config/model-markdown-as-iac.md) pattern**: how retrieved content is *presented* to the agent (truncated preview vs full doc) is itself a context-engineering decision worth optimizing.

9. **Within-Qwen3-Embedding model-size scaling is empirically clean**. Table 2: nDCG@10 for evidence retrieval: 0.6B = 8.0 → 4B = 14.0 → 8B = 20.3. **8B beats ReasonIR-8B (16.8)** despite ReasonIR being explicitly trained for reasoning-intensive retrieval — suggesting general-purpose embedding scale dominates reasoning-specific tuning at the same parameter count. **Mission relevance**: the open-source retriever competitive with the most expensive closed-source alternatives is a $0/inference Apache-2.0 8B model. This is the structural argument for the anti-vendor-lock-in stack at the retrieval layer.

10. **Calibration error reveals confidence reliability gaps**. From Table 1: GPT-5 + Qwen3-Embed-8B has 9.11% calibration error (well-calibrated). gpt-4.1 with the same retriever has 54.67% calibration error (badly miscalibrated despite 35.42% accuracy). **Models with high accuracy AND low calibration error are deployable**; models with mid-tier accuracy and high calibration error mislead downstream consumers. This is a deployment-relevant signal beyond accuracy alone.

11. **API costs span >40× across LLM choices (Table 8)**. For the same 830-query benchmark with Qwen3-Embed-8B retriever:
    - **Opus 4 = $1,842.48** (most expensive)
    - **o3 = $740.79**
    - **GPT-5 = $360.71**
    - **Sonnet 4 = $325.75**
    - **Gemini 2.5 Pro = $99.92**
    - **gpt-4.1 = $89.81**
    - **Gemini 2.5 Flash = $41.29** (cheapest premium tier)
    
    **Opus 4 costs 5× GPT-5 yet scores LOWER** (36.14% vs 70.12% accuracy). For this task class, **Opus 4 is mispriced relative to capability**. This is empirical anchoring for AICP's smart-routing logic — context-length / task-type routing should *not* default to Opus 4 for agentic search.

12. **Three failure modes excluded from the corpus** (Appendix C). 175 of 1,005 verified queries were dropped. Failure modes:
    - **BrowseComp inherent errors**: ground-truth answers based on confused identities (e.g., "the book author" and "the actor" being two different people sharing a name)
    - **Google Maps-dependent queries** (42): require live distance APIs, not retrievable from a static document corpus
    - **Ambiguous / non-unique answers** (13): multiple valid answers; ground-truth picks one arbitrarily
    
    The fact that these are explicitly documented (rather than silently dropped) is methodological rigor — a future researcher knows exactly what BrowseComp+ does and doesn't cover.

13. **The hard-negative mining pipeline is empirically validated**. GPT-4o decomposes each question into ~7 sub-queries; SerpAPI returns up to 100 results per sub-query; these are scraped and deduped against positives. Result: ~76 negatives per query. The authors verify: in the augmented Fineweb-corpus experiment, the ranking of retrievers and LLMs **does not change** — meaning the 100K corpus's hard negatives are competitive with web-scale alternatives at the evaluation level.

## Deep Analysis

### Paper Structure (26 pages, 7 main sections + appendices A-H)

| Section | Pages | Content |
|---|---|---|
| 1. Introduction | 1-3 | Three motivating problems: fairness (live-API black-box), transparency (no corpus control), accessibility (commercial-API cost) |
| 2. Related Works | 3-4 | Deep-Research agents (BrowseComp / Gemini / Opus / o3 / gpt-oss) · Neural retrieval (DPR / FAISS / continuous-pretraining / LLM-distillation) · Deep retrieval benchmarks (NQ / TriviaQA / HotpotQA / BrowseComp / ZH-BrowseComp / MedBrowseComp) |
| 3. BrowseComp-Plus | 4-7 | Construction: 1,266 BC questions → 1,142 with o3-evidence → 1,005 with scrapeable URLs → 830 verified · 100,195 final corpus docs |
| 4. Experiments | 7-13 | Tables 1-7 + Section 4.8 ablations |
| 5. Future Work | 13-14 | 5 named directions including federated-search breakdown + retriever-agent co-optimization |
| 6. Conclusion | 14 | Reproducibility + transparency framing reinforced |
| Appendices A-H | 14-26 | Prompts (4 different) · Labeling UI · Problematic cases · API costs |

### Corpus Construction — 3-Stage Pipeline

> [!info] Stage 1 — Evidence Document Gathering (paper §3.2.1)
>
> - Take 1,266 BrowseComp question-answer pairs
> - Prompt OpenAI o3 (with web search enabled) to find evidence URLs
> - Output structured 3-column table: clue / URL / evidence text
> - 124 pairs failed (o3 abstained or formatting errors)
> - 1,142 remaining
> - Scrape URLs via Selenium, parse with Trafilatura
> - 137 pairs excluded (≥1 unscrapeable URL)
> - **1,005 queries advance to Stage 2**

> [!info] Stage 2 — Evidence Document Verification (paper §3.2.2)
>
> - 14 university student annotators
> - >400 hours total manual effort
> - Each annotator: confirm clue-document support + label justifying text spans + confirm overall question is answerable
> - Annotators ALSO label **gold documents** (those directly containing the final answer)
> - Cross-validation: sample of each annotator's work checked by other annotators → **>80% agreement** average
> - **830 of 1,005 pairs pass verification**
> - 175 fail per Appendix C exclusion criteria (3 categories: BC errors / Google-Maps-dependent / ambiguous answers)

> [!info] Stage 3 — Hard Negative Mining (paper §3.3)
>
> - GPT-4o decomposes each question → **~7 self-contained sub-queries** on average
> - Each sub-query → SerpAPI → up to 100 search results
> - Scrape via Selenium + Trafilatura
> - Deduplicate against positives + cross-query
> - Final: **100,195 unique documents** (830 queries × 6.1 evidence + 830 × 76.28 negatives + 830 × 2.9 gold, deduplicated)

### Experimental Setup — Models, Retrievers, Tools

> [!abstract] LLM search agents (paper §4.1)
>
> | Category | Model | Reasoning effort variants |
> |---|---|---|
> | OpenAI commercial | gpt-4.1, o3, gpt-5 | gpt-5 default high reasoning |
> | Anthropic | Claude Opus 4, Claude Sonnet 4 | — |
> | Google | Gemini 2.5 Pro, Gemini 2.5 Flash | — |
> | OpenAI open-weight | gpt-oss-20B, gpt-oss-120B | × 3 reasoning modes (low/medium/high) |
> | Open-source agents | Qwen3-32B (base reasoning LLM), Search-R1-32B (RL-fine-tuned for search) | — |

> [!abstract] Retrievers (paper §4.2)
>
> | Retriever | Type | Backbone |
> |---|---|---|
> | BM25 [Robertson 1994] | Lexical sparse | Pyserini toolkit |
> | Qwen3-Embedding-0.6B [Zhang 2025] | Dense neural | Qwen3 family, Tevatron toolkit |
> | Qwen3-Embedding-4B | Dense neural | Qwen3 family |
> | Qwen3-Embedding-8B | Dense neural | Qwen3 family — paper's best-performing |
> | ReasonIR [Shao 2025] | Dense neural | Reasoning-tuned via synthetic data |

> [!info] Tool configuration
>
> - Retriever returns **top-5 results** per call
> - Each result truncated to **first 512 tokens** (token-budget constraint)
> - 86.5% of queries still have ground-truth answer in ≥1 gold doc within first 512 tokens (validates the truncation choice)
> - Get-document tool (Section 4.8.3) optionally enables full-document reading

### Table 1 — End-to-End Agent Accuracy (paper, Section 4.5)

> [!info] Complete LLM × Retriever matrix
>
> | LLM | Retriever | Accuracy | Recall | Search Calls | Calibration Error |
> |---|---|---|---|---|---|
> | gpt-4.1 | BM25 | 14.58% | 16.42% | 10.35 | 68.96% |
> | gpt-4.1 | Qwen3-Embed-8B | 35.42% | 36.89% | 8.67 | 54.67% |
> | o3 | BM25 | 49.28% | 56.64% | 25.93 | 12.58% |
> | o3 | Qwen3-Embed-8B | 63.49% | 73.24% | 23.97 | 16.77% |
> | **gpt-5** | BM25 | 55.90% | 61.70% | 23.23 | 13.50% |
> | **gpt-5** | **Qwen3-Embed-8B** | **70.12%** | **78.98%** | **21.74** | **9.11%** |
> | Sonnet 4 | BM25 | 14.34% | 21.31% | 9.95 | 29.79% |
> | Sonnet 4 | Qwen3-Embed-8B | 36.75% | 47.33% | 9.03 | 24.51% |
> | Opus 4 | BM25 | 15.54% | 22.96% | 11.22 | 22.00% |
> | Opus 4 | Qwen3-Embed-8B | 36.14% | 50.84% | 10.24 | 12.79% |
> | Gemini 2.5 Flash | BM25 | 15.54% | 21.45% | 10.56 | 29.28% |
> | Gemini 2.5 Flash | Qwen3-Embed-8B | 33.01% | 40.19% | 9.77 | 21.63% |
> | Gemini 2.5 Pro | BM25 | 19.04% | 22.81% | 7.44 | 51.58% |
> | Gemini 2.5 Pro | Qwen3-Embed-8B | 28.67% | 35.31% | 6.04 | 44.08% |
> | gpt-oss-120B-high | BM25 | 28.67% | 35.50% | 19.45 | 46.48% |
> | **gpt-oss-120B-high** | **Qwen3-Embed-8B** | **42.89%** | **52.63%** | **18.35** | **40.34%** |
> | Qwen3-32B | BM25 | 3.49% | 3.12% | 0.92 | 57.41% |
> | Qwen3-32B | Qwen3-Embed-0.6B | 4.10% | 3.45% | 0.91 | 60.71% |
> | Qwen3-32B | Qwen3-Embed-4B | 7.83% | 6.20% | 0.89 | 61.06% |
> | Qwen3-32B | Qwen3-Embed-8B | 10.36% | 7.80% | 0.94 | 59.84% |
> | Qwen3-32B | ReasonIR | 9.16% | 7.59% | 0.91 | 55.15% |
> | SearchR1-32B | BM25 | **3.86%** | 2.61% | 1.78 | N/A |
> | SearchR1-32B | Qwen3-Embed-0.6B | 5.66% | 5.30% | 1.73 | N/A |
> | SearchR1-32B | Qwen3-Embed-4B | 9.40% | 7.90% | 1.68 | N/A |
> | SearchR1-32B | Qwen3-Embed-8B | 10.36% | 10.17% | 1.69 | N/A |
> | SearchR1-32B | ReasonIR | 9.43% | 8.37% | 1.74 | N/A |

The 30+ rows reveal patterns the abstract's headline numbers don't:
- **The matrix is bimodal**: closed-source clusters around 30-70%; open-source clusters around 4-15% with the exception of gpt-oss-120B-high (42.89%).
- **Within-LLM retriever swap effect**: BM25 → Qwen3-Embed-8B yields **+14 to +25 absolute points** for proprietary LLMs (gpt-5: +14.22; o3: +14.21; gpt-4.1: +20.84; Opus 4: +20.60).
- **Within-retriever LLM swap effect**: With Qwen3-Embed-8B, swapping LLM produces **0-70 absolute points** of variance.
- **Search-call disparity is structural**: closed-source ~20+ calls, open-source <2 calls per query. Same explicit prompt to use the tool; behavior diverges.

### Table 2 — Retriever Effectiveness in Isolation (paper §4.6)

> [!info] Retriever-only evaluation, using complete BrowseComp questions as queries (no LLM in the loop)
>
> | Retriever | Recall@5 | Recall@100 | Recall@1000 | nDCG@10 |
> |---|---|---|---|---|
> | **Evidence Document Retrieval** |
> | BM25 | 1.2% | 4.7% | 13.7% | 1.6 |
> | Qwen3-Embed-0.6B | 6.2% | 26.5% | 59.7% | 8.0 |
> | Qwen3-Embed-4B | 9.8% | 40.2% | 71.8% | 14.0 |
> | **Qwen3-Embed-8B** | **14.5%** | **47.7%** | **76.7%** | **20.3** |
> | ReasonIR-8B | 12.2% | 43.6% | 73.9% | 16.8 |
> | **Gold Document Retrieval** |
> | BM25 | 1.4% | 6.1% | 17.3% | 1.7 |
> | Qwen3-Embed-0.6B | 8.5% | 30.5% | 66.2% | 7.4 |
> | Qwen3-Embed-4B | 13.0% | 47.3% | 77.0% | 13.6 |
> | **Qwen3-Embed-8B** | **18.5%** | **55.8%** | **83.5%** | **19.5** |
> | ReasonIR-8B | 15.3% | 49.7% | 78.9% | 15.5 |

Two findings:
1. **Within Qwen3-Embedding family, scale dominates**: 0.6B → 8B improves nDCG@10 by 2.5× across both evidence and gold retrieval.
2. **Qwen3-Embedding-8B beats ReasonIR-8B at the same parameter count** despite ReasonIR being explicitly reasoning-tuned. Suggests that for fact-seeking research queries, *general-purpose retrieval scale* is more valuable than reasoning-specific tuning at this size class.

### Table 3 — Citation Quality (paper §4.7)

> [!info] Per-query citation coverage / count / precision / recall
>
> | LLM | Retriever | Coverage | Avg Citations | Precision | Recall |
> |---|---|---|---|---|---|
> | gpt-4.1 | BM25 | 57.0% | 1.92 | 37.0% | 16.1% |
> | gpt-4.1 | Qwen3-Embed-8B | 79.2% | 2.54 | 58.5% | 28.2% |
> | o3 | BM25 | 63.5% | 3.27 | 86.7% | 51.0% |
> | o3 | Qwen3-Embed-8B | 78.0% | 3.51 | **91.8%** | 56.2% |
> | **gpt-5** | BM25 | 94.9% | 3.89 | 71.8% | 51.3% |
> | **gpt-5** | **Qwen3-Embed-8B** | **98.0%** | 4.28 | 83.4% | **62.3%** |
> | Sonnet 4 | BM25 | 76.1% | 3.19 | 31.9% | 21.3% |
> | Sonnet 4 | Qwen3-Embed-8B | 90.7% | 4.19 | 52.4% | 39.9% |
> | Opus 4 | BM25 | 74.9% | 3.03 | 35.1% | 22.3% |
> | Opus 4 | Qwen3-Embed-8B | 86.1% | 3.82 | 58.9% | 42.6% |
> | Gemini 2.5 Flash | BM25 | 74.2% | 4.89 | 34.2% | 21.7% |
> | Gemini 2.5 Flash | Qwen3-Embed-8B | 89.2% | 4.75 | 51.5% | 35.1% |
> | Gemini 2.5 Pro | BM25 | 53.9% | 3.03 | 52.1% | 31.4% |
> | Gemini 2.5 Pro | Qwen3-Embed-8B | 59.4% | 3.49 | 64.9% | 41.5% |
> | gpt-oss-120B-high | BM25 | 62.5% | 3.55 | 50.8% | 31.5% |
> | gpt-oss-120B-high | Qwen3-Embed-8B | 76.9% | 3.88 | 60.8% | 38.2% |
> | Qwen3-32B | (any) | 87-95% | ~1.8 | **8.9-20%** | 2.6-6.6% |

**The pattern**: GPT-5 dominates citation completeness (98% coverage) but o3 dominates citation correctness (91.8% precision). Qwen3-32B cites *something* nearly always (90%+) but rarely cites *the right thing* (8-20% precision) — accuracy is decoupled from citation faithfulness in open-source models.

### Reasoning-Effort Ablation (paper §4.8.2, Table 4)

> [!info] gpt-oss family, 3 reasoning modes × 2 model sizes × 2 retrievers
>
> | LLM | Retriever | Accuracy | Recall | Search Calls | Calibration Error |
> |---|---|---|---|---|---|
> | oss-20B-low | BM25 | 4.11% | 5.36% | 1.89 | 40.89% |
> | oss-20B-low | Qwen3-Embed-8B | 13.37% | 17.37% | 1.87 | 36.34% |
> | oss-20B-medium | BM25 | 16.39% | 21.96% | 13.72 | 41.78% |
> | oss-20B-medium | Qwen3-Embed-8B | 29.88% | 41.31% | 13.64 | 35.99% |
> | oss-20B-high | BM25 | 21.08% | 31.98% | 26.87 | 33.42% |
> | oss-20B-high | Qwen3-Embed-8B | 34.58% | 49.29% | 23.87 | 27.81% |
> | oss-120B-low | BM25 | 9.52% | 8.54% | 2.06 | 43.59% |
> | oss-120B-low | Qwen3-Embed-8B | 24.94% | 22.50% | 2.21 | 40.96% |
> | oss-120B-medium | BM25 | 23.73% | 27.02% | 9.73 | 45.78% |
> | oss-120B-medium | Qwen3-Embed-8B | 37.59% | 43.45% | 9.64 | 41.77% |
> | oss-120B-high | BM25 | 28.67% | 35.50% | 19.45 | 46.48% |
> | **oss-120B-high** | **Qwen3-Embed-8B** | **42.89%** | **52.63%** | 18.35 | 40.34% |

Patterns:
- **20B → 120B at high reasoning + best retriever: 34.58% → 42.89%** (+8.3 abs points from 6× model size)
- **low → high at 120B + best retriever: 24.94% → 42.89%** (+17.95 abs points from reasoning-effort-only)
- **Reasoning effort dominates model size at this scale class** — a smaller model with more reasoning beats a bigger model with less.

### Document-Reading Ablation (paper §4.8.3, Table 5)

> [!info] Effect of get-document tool (full-doc reading vs 512-token preview only)
>
> | Model | Accuracy | Search Calls | Get Document Calls | Calibration Error |
> |---|---|---|---|---|
> | gpt-4.1 | 35.42% | 8.67 | N/A | 54.67% |
> | gpt-4.1 + get-doc | **43.61%** | 10.03 | 1.85 | 54.28% |
> | Qwen3-32B | 10.36% | 0.94 | N/A | 59.84% |
> | Qwen3-32B + get-doc | 11.69% | 1.01 | 0.27 | 56.47% |

**+8.19 absolute points for gpt-4.1 from full-doc reading** with only 1.85 extra calls per query. Qwen3-32B gets only +1.33 — limited by ability to recognize *when* to use the get-doc tool. This validates context-engineering as a first-class concern, not a polish layer.

### Corpus-Size Sensitivity (paper §4.8.4, Tables 6-7)

> [!info] Adding 9.7M Fineweb-edu docs to the 100K corpus (10× expansion)
>
> | Retriever | Corpus | Recall@5 | Recall@100 | Recall@1000 | nDCG@10 |
> |---|---|---|---|---|---|
> | BM25 | Original | 1.2% | 4.7% | 13.6% | 1.6 |
> | BM25 | Original + Fineweb | 2.2% | 8.0% | 19.4% | 3.1 |
> | Qwen3-Embed-8B | Original | 14.5% | 47.7% | 76.7% | 20.3 |
> | Qwen3-Embed-8B | Original + Fineweb | 11.6% | 37.6% | 64.2% | 16.4 |
> | ReasonIR-8B | Original | 12.2% | 43.6% | 73.9% | 16.8 |
> | ReasonIR-8B | Original + Fineweb | 8.6% | 30.7% | 56.3% | 11.8 |

**Counterintuitive but expected**: BM25 *improves* with more docs (better IDF estimation); neural retrievers *appear* worse (TREC-style eval treats unjudged Fineweb docs as non-relevant). End-to-end agent accuracy (Table 7): minimal differences. **Conclusion**: 100K corpus is sufficient for evaluation conclusions.

### API Cost Matrix (paper Appendix H, Table 8)

> [!info] Total cost per benchmark run (830 queries) by LLM + retriever
>
> | LLM | Retriever | Accuracy | Cost (USD) |
> |---|---|---|---|
> | gpt-4.1 | BM25 | 14.58% | $106.96 |
> | gpt-4.1 | Qwen3-Embed-8B | 35.42% | $89.81 |
> | o3 | BM25 | 49.28% | $836.35 |
> | o3 | Qwen3-Embed-8B | 63.49% | $740.79 |
> | **gpt-5** | BM25 | 55.9% | $400.36 |
> | **gpt-5** | Qwen3-Embed-8B | 70.12% | **$360.71** |
> | Sonnet 4 | BM25 | 14.34% | $352.04 |
> | Sonnet 4 | Qwen3-Embed-8B | 36.75% | $325.75 |
> | **Opus 4** | BM25 | 15.54% | $2,043.95 |
> | **Opus 4** | Qwen3-Embed-8B | 36.14% | **$1,842.48** |
> | Gemini 2.5 Flash | BM25 | 15.54% | $47.32 |
> | **Gemini 2.5 Flash** | Qwen3-Embed-8B | 33.01% | **$41.29** |
> | Gemini 2.5 Pro | BM25 | 19.04% | $138.64 |
> | Gemini 2.5 Pro | Qwen3-Embed-8B | 28.67% | $99.92 |

**Three implications**:
1. **Better retrievers reduce cost** consistently (8-15% savings across all LLMs from BM25 → Qwen3-Embed-8B).
2. **Opus 4 is mispriced for this task class** — costs 5.1× GPT-5 yet scores ~half. Smart routing should NOT default to Opus 4 for agentic search.
3. **Gemini 2.5 Flash + Qwen3-Embed-8B** at $41.29 / 33.01% accuracy = $1.25 per accurate answer. **GPT-5 + Qwen3-Embed-8B** at $360.71 / 70.12% = $5.14 per accurate answer. Cost-per-accurate-answer crossover requires considering downstream usage.

### Why This Matters for the Wiki's Mission

> [!success] **The retriever-layer empirical anchor for the [anti-vendor-lock-in lesson](../../lessons/01_drafts/anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence.md)** is now grounded at full Layer-1 PDF depth
>
> The lesson's Evidence 2 cites **+14 absolute points on BrowseComp+** from BM25 → Qwen3-Embedding-8B with the same generation model (GPT-5). This synth shows that finding is structurally robust:
> - It holds for **every proprietary LLM tested** (+14 to +21 points for gpt-5/o3/gpt-4.1/Sonnet/Opus/Gemini Pro+Flash)
> - It holds for **gpt-oss-120B-high** (+14 abs from 28.67% → 42.89%)
> - It holds at the **retriever-isolation level** (Table 2: 12-13× nDCG@10 improvement)
> - It holds at the **citation-quality level** (Table 3: better retriever → higher precision + recall + coverage)
> - It holds at the **search-efficiency level** (Table 1: fewer search calls AND better answers)
> - It holds at the **API-cost level** (Table 8: cheaper API calls AND better answers)
>
> **The open-source retriever (Qwen3-Embedding-8B, Apache 2.0, 8B parameters) is empirically competitive with closed-source-only stacks at the retrieval layer.** This is mission-load-bearing.

> [!success] **Open-source LLM ceiling at this benchmark = gpt-oss-120B-high at 42.89%**
>
> Surpasses Sonnet 4 (36.75%) and Opus 4 (36.14%) at this task class. The wiki's [tier-0 candidate comparison](../../comparisons/rlm-qwen3-8b-vs-qwen3-6-27b-tier-0-long-context-candidate.md) tracks Qwen3.6-27B-Dense as the dense generation tier; gpt-oss-120B at 42.89% is a separate route (MoE, OpenAI Apache 2.0). For Deep-Research-style multi-hop tasks, gpt-oss-120B-high is the strongest open-source option this benchmark reveals.

> [!warning] **The reasoning-iteration gap is the open-source weakness**
>
> Oracle retrieval shows Qwen3-32B = 83.25% when given all positive docs — only ~10 points behind gpt-4.1's 93.49%. End-to-end gap (10% vs 35%) is **mostly tool-use behavior**, not reasoning. **Implication for the [RLM-Qwen3.6-27B fine-tune operations-plan](../../domains/cross-domain/rlm-qwen3-6-27b-fine-tune-operations-plan.md)**: post-training for *iterative tool use* may be more leverage than post-training for *reasoning depth*. The RLM paradigm's recursive sub-calls map naturally onto this gap — RLM-trained models would iterate more aggressively because they're trained to do so within the REPL substrate.

### Future Work (paper §5)

The authors name 5 directions:
1. **Retriever-during-optimization** — does BM25 vs embedding affect agent learning dynamics?
2. **Out-of-distribution tool generalization** — train with BM25, test with embedding tool: does it generalize?
3. **Federated search breakdown** — can an LLM orchestrate tiered/composed/multi-facet search like commercial search engines?
4. **Retriever-agent co-optimization** — retrievers tuned for LLM consumers, not human consumers
5. **Oracle retriever development** — high-precision systems for reasoning-intensive queries

These are research directions the wiki should track — particularly #2 (which is directly testable via AICP backend swaps) and #5 (which is the practical extension of the +14pt finding).

## Open Questions

> [!question] Does the +14pt retriever finding hold at smaller LLM scales?
> The paper's pattern is +14-21pt absolute for proprietary LLMs (GPT-5/o3/gpt-4.1/Sonnet/Opus/Gemini). It holds at +14 abs for gpt-oss-120B-high (28.67% → 42.89%). For Qwen3-32B (open-source 32B), the swing is much smaller: 3.49% → 10.36% (+6.87 abs). Why? Likely because Qwen3-32B's tool-use limitations (<1 search call/query) prevent it from fully exploiting better retrieval. Open question: does fine-tuning Qwen3.6-27B for iterative tool-use close this gap?

> [!question] Can RLM substrate replicate the BrowseComp+ retriever effect?
> The [RLM paper](src-rlm-paper-deep-dive-table-1-training-recipe-six-observations.md) Table 1 shows RLM(GPT-5) at **91.3%** on BrowseComp+ 1K-doc subset — far above GPT-5+Qwen3-Embed-8B (70.12% on full corpus). RLM's REPL-recursion is a *different* retrieval mechanism (programmatic context manipulation vs dense retrieval). Is RLM's gain additive with retriever choice, or does the REPL substitute for retrieval? The RLM paper doesn't ablate retriever × RLM combination. Worth a small experiment.

> [!question] What's the BrowseComp+ accessibility for AICP integration?
> The benchmark + evaluation scripts are public (https://texttron.github.io/BrowseComp-Plus/). Could AICP wire BrowseComp+ as a routing-decision benchmark suite? Step 6 of the [RLM-Qwen3.6-27B operations-plan](../../domains/cross-domain/rlm-qwen3-6-27b-fine-tune-operations-plan.md) targets this — `prime eval run browsecomp-plus-1k` if a verifiers RLMEnv exists.

> [!question] Why is Opus 4 mispriced for this task class?
> Opus 4 + Qwen3-Embed-8B = 36.14% accuracy at $1,842.48 per benchmark run. GPT-5 + Qwen3-Embed-8B = 70.12% at $360.71. Opus 4 costs 5.1× more for ~half the accuracy. Possible explanations: (a) Anthropic's pricing reflects context-length / system-prompt strengths not exercised here; (b) Opus 4's reasoning is optimized for different task classes (creative reasoning vs agentic search); (c) the API-cost methodology differs from per-token comparison. Worth empirical verification on a different benchmark.

> [!question] Does the 86.5%-truncation finding generalize?
> 86.5% of queries have ground-truth answer in ≥1 gold doc within first 512 tokens. This is BrowseComp-specific (fact-seeking, often-short-answer queries). For longer-form synthesis tasks (e.g., wiki-style source-synthesis production), the "first 512 tokens contain the answer" assumption likely doesn't hold. **Implication**: tools like the wiki's `pipeline fetch` should NOT default to 512-token previews; they should retrieve full documents.

> [!question] Why does ReasonIR-8B underperform Qwen3-Embedding-8B at the same parameter count?
> Both are 8B dense neural retrievers; ReasonIR is reasoning-tuned via synthetic data. At same params, Qwen3-Embedding-8B beats ReasonIR-8B on every metric in Table 2 (nDCG@10: 20.3 vs 16.8, Recall@5: 14.5 vs 12.2). Possibilities: (a) Qwen3-Embedding's general-purpose training data covers a broader skill surface; (b) ReasonIR's reasoning-tuning trades off general retrieval for narrow benefits not exercised on BrowseComp+; (c) Qwen3-Embedding is newer (Jun 2025 vs Apr 2025) and benefits from later training-data improvements. The within-family scaling (0.6B → 4B → 8B) for Qwen3-Embedding is empirically clean — suggesting general-purpose retrieval scale is a strong baseline.

> [!question] Could the wiki's own ingestion pipeline benefit from BrowseComp+-style fixed-corpus benchmarking?
> The wiki's `tools/pipeline.py post` validates page structure but doesn't measure synthesis quality. A BrowseComp+-style benchmark — fixed corpus of raws + verified target syntheses + hard negatives — could become the wiki's quality regression suite. (Requires: corpus + annotation effort.)

## Applicability

> [!info] Where to use BrowseComp+ findings directly
>
> - **Deep-Research agent benchmarking** with retriever disentanglement (the canonical benchmark for this)
> - **Retriever benchmarking** independent of generation model (substitute different retrievers behind same LLM)
> - **Cost-per-accurate-answer analysis** when evaluating LLM choices for production agentic search
> - **Citation-faithfulness validation** (Table 3 framework: coverage / count / precision / recall)
> - **Reasoning-effort tradeoff analysis** for any LLM family with explicit reasoning-mode toggles

> [!warning] Where these findings DON'T apply
>
> - **Non-fact-seeking tasks** (creative writing, code synthesis, open-ended dialog) — BrowseComp+ is fact-seeking-multi-hop
> - **Tasks where retrieval is unbounded by corpus** — BrowseComp+ has a fixed 100K corpus; live web is fundamentally different
> - **Single-turn factual Q&A** — most BrowseComp+ queries require multi-step reasoning + iterative retrieval
> - **Visual / multimodal queries** — text-only benchmark
> - **Streaming or real-time tasks** — BrowseComp+ is offline batch evaluation

## Relationships

- BUILDS ON: [[src-browsecomp-plus-and-longbench-v2-rlm-table-1-benchmarks|BrowseComp+ + LongBench v2 Combined Synthesis]] (this is the dedicated Layer-1 deep-dive expanding on BrowseComp+ specifics that the combined synth covered at abstract level)
- COMPARES TO: [[src-rlm-paper-deep-dive-table-1-training-recipe-six-observations|RLM Paper Deep Dive]] (RLM paper used BrowseComp+ at 1K-doc subset as its Table 1 task; RLM(GPT-5) achieved 91.3% — beyond the 70.12% ceiling here)
- DEMONSTRATES: [[infrastructure-over-instructions-for-process-enforcement|Principle 1]] (BrowseComp+'s fixed-corpus design IS structural enforcement of evaluation fairness; live-web benchmarks are instructions-only)
- DEMONSTRATES: [[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4]] (the +14pt retriever finding was aspirational until measured against fixed corpus with mined negatives + human-verified gold)
- DEMONSTRATES: [[anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence|Anti-Vendor-Lock-In Lesson]] § Evidence 2 (the open-source retriever +14pt finding is grounded at full Layer-1 PDF depth here)
- DEMONSTRATES: [[right-process-for-right-context-the-goldilocks-imperative|Principle 3 — Goldilocks]] (different reasoning-effort modes for different cost-accuracy tradeoffs; smart routing must adapt)
- RELATES TO: [[2026-consumer-hardware-ai-stack|2026 Consumer Hardware AI Stack]] (the cost-routing finding extends the existing $540→$100 framing — Opus 4 mispriced for agentic search, smart routing should de-prioritize it for this task class)
- RELATES TO: [[ai-infrastructure-decision-framework-2026|AI Infrastructure Decision Framework 2026]] (Table 8's API-cost matrix anchors the cost-per-task-class dimension)
- RELATES TO: [[ai-model-provider-harness-decision-matrix-2026|AI Model Provider Harness Decision Matrix 2026]] (concrete evidence for routing decisions per task class)
- FEEDS INTO: [[rlm-qwen3-6-27b-fine-tune-operations-plan|RLM-Qwen3.6-27B Operations Plan]] § Step 6 evaluation (BrowseComp+ 1K-doc subset is one of the 4 RLM Table 1 benchmarks the trained model would be evaluated against)
- FEEDS INTO: [[rlm-thread-evidence-chain-2026-04-27|Learning Path — RLM Thread Evidence Chain]] (Path C: Reproduce Training — this synth is the deep-dive reference for the BrowseComp+ evaluation surface)

## Backlinks

[[BrowseComp+ + LongBench v2 Combined Synthesis]]
[[src-rlm-paper-deep-dive-table-1-training-recipe-six-observations|RLM Paper Deep Dive]]
[[infrastructure-over-instructions-for-process-enforcement|Principle 1]]
[[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4]]
[[Anti-Vendor-Lock-In Lesson]]
[[right-process-for-right-context-the-goldilocks-imperative|Principle 3 — Goldilocks]]
[[2026 Consumer Hardware AI Stack]]
[[ai-infrastructure-decision-framework-2026|AI Infrastructure Decision Framework 2026]]
[[AI Model Provider Harness Decision Matrix 2026]]
[[rlm-qwen3-6-27b-fine-tune-operations-plan|RLM-Qwen3.6-27B Operations Plan]]
[[Learning Path — RLM Thread Evidence Chain]]
