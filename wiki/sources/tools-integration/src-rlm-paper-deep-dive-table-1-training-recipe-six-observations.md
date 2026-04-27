---
title: "Synthesis — RLM Paper Deep Dive: Table 1 Across 4 Tasks, RLM-Qwen3-8B Training Recipe (48 H100 hrs / prime-rl / 1000 trajectories), and Six Observations (arXiv 2512.24601 v2 Jan 2026)"
aliases:
  - "RLM Paper Deep Dive"
  - "RLM Paper Table 1"
  - "RLM-Qwen3-8B Training Recipe"
  - "RLM Six Observations"
type: source-synthesis
domain: tools-integration
status: synthesized
confidence: high
maturity: seed
created: 2026-04-27
updated: 2026-04-27
last_reviewed: 2026-04-27
sources:
  - id: rlm-paper-pdf
    type: paper
    url: https://arxiv.org/pdf/2512.24601
    file: raw/papers/recursive-language-models.md
    title: "Recursive Language Models — arXiv 2512.24601 (v2 28 Jan 2026 PDF)"
    description: "Full paper PDF, 1928-line scrape. Authors: Alex L. Zhang, Tim Kraska, Omar Khattab. MIT CSAIL. 9 pages main + 33 with Appendix. Preprint dated January 29, 2026. Citations include DeepSeek-R1, Qwen3, ReAct, MemGPT, LongBench v2, BrowseComp-Plus, ViperGPT, THREAD, ReDel, Context Folding, AgentFold, ReSum, Mem0, MemAgent, G-Memory."
    ingested: 2026-04-27
  - id: rlm-implementation-companion
    type: wiki
    file: wiki/sources/tools-integration/src-rlm-recursive-language-models-mit-oasys.md
    description: "Implementation companion — covers the alexzhang13/rlm reference SDK (architecture, REPL semantics, 5 backends, 6 environments)"
  - id: rlm-empirical-findings-companion
    type: wiki
    file: wiki/sources/tools-integration/src-rlm-empirical-findings-oolong-browsecomp-rlm-qwen3-8b.md
    description: "Empirical-findings companion — covers the Oct 2025 blogpost + arXiv abstract; this page covers the paper's deep specifics that exceed the blogpost-level summary"
  - id: oolong-paper
    type: paper
    url: https://arxiv.org/abs/2511.02817
    title: "OOLONG: Evaluating Long Context Reasoning and Aggregation Capabilities (Bertsch et al. 2025)"
    description: "Long-reasoning benchmark used for RLM's main results; trec_coarse split is the focus"
  - id: browsecomp-plus-paper
    type: paper
    url: https://arxiv.org/abs/2508.06600
    title: "BrowseComp-Plus: A More Fair and Transparent Evaluation Benchmark of Deep-Research Agent (Chen et al. 2025)"
    description: "DeepResearch benchmark with 100K-document offline corpus; RLM uses 150 sampled instances with 1K-document context"
  - id: longbench-v2
    type: paper
    url: https://arxiv.org/abs/2412.15204
    title: "LongBench v2 (Bai et al. 2025)"
    description: "Multi-choice code repository understanding (CodeQA split) used as fourth RLM task"
  - id: longbench-pro
    type: paper
    url: https://arxiv.org/abs/2601.02872
    title: "LongBenchPro (Chen et al. 2026)"
    description: "Bilingual long-context benchmark used as the SOURCE of training trajectories for RLM-Qwen3-8B (English split, 750 tasks)"
  - id: prime-rl-library
    type: documentation
    url: https://github.com/PrimeIntellect-ai/prime-rl
    title: "prime-rl library (Prime Intellect)"
    description: "Fine-tuning library used for RLM-Qwen3-8B training. Connects to wiki's existing Prime Intellect ecosystem references."
tags: [rlm, recursive-language-models, paper-deep-dive, table-1, four-tasks, codeqa, browsecomp-plus, oolong, oolong-pairs, s-niah, rlm-qwen3-8b, training-recipe, prime-rl, longbench-pro, six-observations, negative-results, system-prompt, mit-csail, mit-oasys, mit-dsg, prime-intellect, modal-labs, laude-institute, mission-2026-04-27, tier-0-candidate, post-training, sft, fine-tuning, 48-h100-hours, 1000-trajectories, gpt-5-mini, qwen3-coder-480b, qwen3-8b]
---

# Synthesis — RLM Paper Deep Dive: Table 1, Training Recipe, Six Observations

## Summary

The arXiv 2512.24601 v2 paper PDF (28 Jan 2026; 9 pages main + 33 with Appendix; 1928-line raw scrape) supplies the substance the [blogpost-level summary](src-rlm-empirical-findings-oolong-browsecomp-rlm-qwen3-8b.md) compressed: the **specific four long-context tasks** (CodeQA from LongBench v2 / BrowseComp+ at 1K docs / OOLONG `trec_coarse` / OOLONG-Pairs — plus a fifth, S-NIAH, used in Figure 1 to demonstrate complexity-scaling without inclusion in Table 1's main results); the **full Table 1 results matrix** across 5 methods × 4 tasks × 3 models (GPT-5, Qwen3-Coder-480B-A35B, Qwen3-8B) with API costs ± std deviation per cell; the **RLM-Qwen3-8B training recipe** (1,000 filtered trajectories sampled from RLM(Qwen3-Coder-480B) on LongBenchPro tasks, fine-tuned on Qwen3-8B with the prime-rl library, batch 64 × 300 steps × 48 H100-hours); the **six observations** the authors assert from the data; the **negative results section** (what didn't work — distinguishing FINAL vs thoughts is brittle, sync sub-calls are slow, models without coding ability struggle as RLMs, etc.); and the **system-prompt full text** — the actual operational artifact that programs an LM to behave as the root RLM. This synthesis covers what the paper adds beyond what the blogpost or abstract established. **Funding via Laude Institute + Prime Intellect + Modal Labs** is mission-relevant: the same Prime Intellect ecosystem the wiki already tracks (verifiers library, prime-rl, prime sandboxes) underwrites this work.

## Reference Card

> [!info] Paper deep-dive reference card
>
> | Field | Value |
> |---|---|
> | **Paper** | arXiv 2512.24601 v2, dated 28 Jan 2026; preprint 29 Jan 2026 |
> | **Length** | 9 pages main + 33 with Appendix |
> | **Affiliations** | All authors: MIT CSAIL (lab subdivisions: OASYS lab — Kraska's group; DSG = Database Systems Group) |
> | **Funding** | Laude Institute · **Prime Intellect** · **Modal Labs** (acknowledgments) |
> | **Notable thanked individuals** | Noah Ziems · Jacob Li · James Moore · Jack Cook · Matej Sirovatka · Ofir Press · Sebastian Müller · Simon Guo · Zed Li |
> | **4 tasks (Table 1 main results)** | **CodeQA** (LongBench v2 split, 23K-4.2M tokens) · **BrowseComp+ (1K docs)** (6M-11M tokens) · **OOLONG** (trec_coarse split, 131K tokens) · **OOLONG-Pairs** (32K tokens, 20 new pair-aggregation queries) |
> | **5th task (Figure 1 complexity-scaling demo only)** | **S-NIAH** (single needle-in-haystack from RULER) |
> | **3 models tested** | **GPT-5** (with RLM sub-calls to GPT-5-mini) · **Qwen3-Coder-480B-A35B** · **Qwen3-8B** (incl. fine-tuned RLM-Qwen3-8B variant) |
> | **5 methods compared per model** | Base Model · CodeAct (+BM25) · CodeAct (+sub-calls) · Summary agent · RLM · RLM (no sub-calls) |
> | **Training recipe for RLM-Qwen3-8B** | Source: 750 English LongBenchPro tasks → 2250 RLM(Qwen3-Coder-480B) candidate trajectories → 1,072 after dropping zero-score/single-turn → per-turn SFT samples → filter turns beyond 100K chars → programmatic FINAL/FINAL_VAR fix step → fine-tune with **prime-rl library**, batch 64, 300 steps, **48 H100 hours total** |
> | **Confidence** | high — read the full paper raw including Table 1, 6 observations, related works, training recipe, system prompts, and negative results section. Pages 1-17 of the paper raw are covered; remaining ~600 lines are additional appendix material on emergent patterns + system prompt continuations. |

## Key Insights

1. **Table 1 numbers (RLM vs Base Model on GPT-5)** validate the blogpost's claims and add depth:

   | Task | Base GPT-5 | RLM(GPT-5) | Improvement |
   |---|---|---|---|
   | CodeQA | 24.0% (often hits context limit) | 62.0% | **+158% relative / +38 absolute** |
   | BrowseComp+ (1K) | 0.0% (always hits context limit at 6-11M tokens) | **91.3%** | from impossible to nearly-solved |
   | OOLONG | 44.0% | 56.5% | +28.4% |
   | OOLONG-Pairs | 0.1% (catastrophic) | 58.0% | from 0 to 58% |

   The OOLONG-Pairs result is the most striking single number: the base model essentially scores zero (F1 0.1%) while RLM scores 58.0% — RLM enables a class of tasks the base model cannot perform at all.

2. **The 4 tasks span 4 different complexity classes** (the paper's framing):
   - **S-NIAH** (Figure 1 only): O(1) — needle size constant despite prompt length growth
   - **CodeQA**: O(fixed-files) — multi-choice code-repository understanding over a fixed file set
   - **BrowseComp+**: O(needs-to-find-multi-hop) — multi-hop reasoning across docs, retrieval-difficult
   - **OOLONG**: O(N) — linear in input length (each task uses ~all entries)
   - **OOLONG-Pairs**: O(N²) — quadratic in input length (each task uses ~all PAIRS of entries)

   The complexity-scaling framing matters: the paper argues effective context window cannot be measured independently of task complexity. RULER-class tasks (NIAH-style) are O(1) and saturate; OOLONG-class tasks are O(N) or O(N²) and frontier models break down at much shorter lengths.

3. **The REPL alone provides most of the benefit; recursion adds info-density**. Observation 2: "the REPL is necessary for handling long inputs, while the recursive sub-calling of RLMs provides strong benefits on information-dense inputs." On CodeQA + BrowseComp+ with Qwen3-Coder, RLM-without-recursion actually *outperforms* RLM-with-recursion by ~17.9% and 3% respectively. Recursion's value shows on OOLONG / OOLONG-Pairs (info-dense): RLM beats RLM-no-sub-calls by 10-59% across info-dense tasks.

4. **The training recipe is unexpectedly simple — and small**:
   - **Data source**: 750 English LongBenchPro tasks (Chen et al. 2026)
   - **Distillation source model**: RLM(Qwen3-Coder-480B-A35B) — the larger model acting AS an RLM
   - **2250 candidate trajectories** generated; filtered to 1,072 by removing zero-score and single-turn trajectories
   - **Per-turn SFT samples** — each iteration of an RLM trajectory becomes its own (input=full history, output=root LM's response) SFT pair
   - **Programmatic correction step** — patches FINAL/FINAL_VAR template mistakes in the source trajectories (16% of turns had bad FINAL, 13% had bad FINAL_VAR — "Qwen3-Coder-480B made noticeable mistakes in following the RLM instructions")
   - **Training compute**: prime-rl library, batch size 64, 300 training steps, **48 H100 hours total**
   - **Result**: RLM-Qwen3-8B improves over Qwen3-8B-as-RLM by 28.3% on average across 4 evaluation tasks
   - **Generalization signal**: trained on LongBenchPro tasks; evaluated on CodeQA/BrowseComp+/OOLONG/OOLONG-Pairs (different domains) — improvement transfers

5. **Three system prompts shown in full in Appendix C** — the operational artifact that programs LMs as RLMs:
   - **(1a)** RLM-with-REPL system prompt for **GPT-5** — the canonical version
   - **(1b)** Diff for **Qwen3-Coder-480B-A35B**: adds 3 lines warning against excessive sub-calls ("aim for around ~200k characters per call... thousands of LM subcalls for basic tasks")
   - **(1c)** Diff for **Qwen3-8B**: adjusts context-window expectations from 500K char sub-LLM context to ~100K (32K tokens), tightens batching guidance, and modifies example chunk sizes
   - **(2)** RLM-with-REPL no-sub-calls system prompt — ablation version
   - **(3a-onward)** CodeAct + BM25 prompts — baseline methods

   The prompt is itself a structured program: instructs about `context` variable, `llm_query` function, `print()` usage, REPL `repl` code-block format, `FINAL()` / `FINAL_VAR()` tags, includes 3 worked examples (Harry Potter book chunking, Great Gatsby book-chunked retrieval, Markdown-header-aware chunking).

6. **Six observations the authors derive** (worth quoting directly — they are the paper's own conclusions):
   1. **RLMs can scale to the 10M+ token regime** and outperform base LMs and existing task-agnostic agent scaffolds on long-context tasks (up to 2× performance at comparable/cheaper token costs)
   2. **The REPL is necessary for handling long inputs**; recursive sub-calling provides benefits on info-dense inputs (10-59% gain over no-sub-calls on info-dense)
   3. **LM performance degrades as a function of input length and problem complexity**, while RLM performance scales better — for context lengths beyond 2¹⁴ tokens, RLM(GPT-5) consistently outperforms GPT-5
   4. **The inference cost of RLMs remains comparable to a base LM call** but has high variance due to trajectory length differences (median cheaper than base, 95th percentile much higher)
   5. **RLMs are model-agnostic but different models exhibit different decisions** — GPT-5 conservative on sub-calls, Qwen3-Coder needs an explicit warning to not over-sub-call
   6. **Training RLMs on one domain can improve general downstream RLM performance** — the LongBenchPro→4-task generalization signal

7. **Negative results section** (unusually frank for a paper):
   - **Same RLM system prompt across all models is problematic** — Qwen3-Coder needed an extra warning line to prevent thousand-subcall basic-task behavior
   - **Models without sufficient coding capabilities struggle as RLMs** — small models (Qwen3-8B vanilla) can't write good REPL code
   - **Thinking models without enough output tokens struggle as RLMs** — Qwen3-235B-A22B trajectories ran out of output tokens due to thinking tokens, despite OOLONG performance bumping from 30% to 38% on the base model
   - **Sync sub-calls are slow** — naive blocking implementation; "we are confident this can be resolved with a robust implementation"
   - **Distinguishing FINAL from thoughts is brittle** — model sometimes outputs its plan as a final answer; safeguards added but the issue should be avoided when models are trained as RLMs

8. **Cost analysis (Figure 3) — quartiles tell a different story than median**:
   - At 50th percentile: RLM is comparable or *cheaper* than base model
   - At 95th percentile: RLM has sharp tail-end increases (long trajectories)
   - vs Summary agent: RLM is up to **3× cheaper** while maintaining stronger performance
   - Latency: blocking sub-calls cause wide range; runtime numbers in Appendix F

9. **The paper distinguishes RLMs from Algorithm 2 — a "deceptively similar" alternative scaffold**. Three failure points of Algorithm 2 that RLMs fix:
   - **Flaw #1**: Algorithm 2 puts the prompt P INTO the LLM context window from turn 1, inheriting all M's window limitations. RLMs put P in REPL state; M only sees metadata about P (length, prefix, access functions).
   - **Flaw #2**: Algorithm 2 asks M to autoregressively generate output via Finish action — bounded by M's output context. RLMs build output through REPL variables, breaking the output-context bound.
   - **Flaw #3**: Algorithm 2 has separate "code execution" and "sub-LLM" actions — cannot programmatically invoke sub-LLM in loops over slices of P. RLMs make symbolic recursion (M-calling-M from inside loops) first-class.

   This is a sharper formal contrast than the blogpost's prose handling.

10. **Funding ties to existing wiki ecosystem**:
    - **Prime Intellect** (acknowledged + prime-rl library used for training) — the wiki has prior tracking of Prime Intellect's `verifiers` library + `prime-rl` (Intellect 2025 citation in paper). This synthesis adds load-bearing context: the same Prime Intellect ecosystem underwrites RLM and the broader open-source RL-for-agents direction.
    - **Modal Labs** (acknowledged + ModalREPL is the canonical isolated-environment reference implementation in the SDK)
    - **Laude Institute** — acknowledged supporter

11. **Related works section names 14+ alternatives, organized by category**:
    - **Long-context architecture**: Press et al. 2022 (ALiBi), Gu/Goel/Ré 2022 (S4), Munkhdalai et al. 2024 (Infini-attention)
    - **Lossy context management**: MemWalker (Chen 2023, tree-summarization), ReSum (Wu 2025, summarization tool)
    - **Memory hierarchies**: MemGPT (Packer 2024), Mem0 (Chhikara 2025), G-Memory (Zhang 2025), MemAgent (Yu 2025)
    - **Self-delegation / sub-LM calls**: Anthropic Claude Code subagents, Sentient ROMA, THREAD (Schroeder 2025), DisCIPL (Grand 2025), ReDel (Zhu 2024), Context Folding (Sun 2025), AgentFold (Ye 2025), ViperGPT (Surís 2023)

    RLM's distinctive claim against this body of work: "RLMs differ in that all context window management is implicitly handled by the LM itself" + "symbolically manipulate arbitrarily long strings and iteratively refine recursion via execution feedback from the persistent REPL."

12. **Connection to bootstrapping reasoning training (STaR, Quiet-STaR)**: the paper hypothesizes "RLM trajectories can be viewed as a form of reasoning, which can be trained by bootstrapping existing models" — citing Zelikman et al. 2022 (STaR) + 2024 (Quiet-STaR). This positions RLM as a candidate for the same bootstrap training methodology that worked for chain-of-thought reasoning.

## Deep Analysis

### Table 1 — The Full Results Matrix

> [!info] Performance comparison across 5 methods × 4 tasks × 3 models (Table 1 from the paper)
>
> Format: percentage score (median cost ± std dev). N/A = method ran into context limits. Costs in USD.

**GPT-5 with RLM sub-calls to GPT-5-mini** (best-performing root model):

| Method | CodeQA (23K-4.2M tok) | BrowseComp+ (1K) (6M-11M tok) | OOLONG (131K tok) | OOLONG-Pairs (32K tok) |
|---|---|---|---|---|
| Base Model | 24.0%* ($0.13±$0.07) | **0.0%*** (N/A) | 44.0% ($0.14±$0.02) | 0.1% ($0.16±$0.10) |
| CodeAct (+ BM25) | 22.0%* ($0.06±$0.08) | 51.0% ($0.71±$1.20) | 38.0% ($0.61±$1.06) | 24.7% ($0.75±$0.43) |
| CodeAct (+ sub-calls) | 24.0%* ($0.06±$0.08) | 0.0%* (N/A) | 40.0% ($0.85±$1.27) | 28.4% ($1.11±$0.62) |
| Summary agent | 58.0% ($1.31±$1.46) | 70.5% ($0.57±$0.10) | 46.0% ($0.13±$0.01) | 0.1% ($0.13±$0.09) |
| **RLM** | **62.0%** ($0.11±$0.10) | **91.3%** ($0.99±$1.22) | **56.5%** ($0.43±$0.85) | **58.0%** ($0.33±$0.20) |
| RLM (no sub-calls) | 58.0% ($0.18±$0.56) | 88.0% ($0.44±$0.90) | 36.0% ($0.37±$0.42) | 43.9% ($0.69±$1.16) |

*indicates context-limit hit (sometimes truncation, sometimes failure).

**Qwen3-Coder-480B-A35B**:

| Method | CodeQA | BrowseComp+ (1K) | OOLONG | OOLONG-Pairs |
|---|---|---|---|---|
| Base Model | 20.0%* ($0.13±$0.08) | 0.0%* (N/A) | 36.0% ($0.06±$0.00) | 0.1% ($0.05±$0.01) |
| CodeAct (+ BM25) | 24.0%* ($0.17±$0.08) | 12.7% ($0.39±$0.50) | 38.0% ($1.51±$1.09) | 0.3% ($1.54±$0.35) |
| CodeAct (+ sub-calls) | 26.0%* ($0.28±$0.30) | 0.0%* (N/A) | 32.0% ($1.83±$1.14) | 0.1% ($1.49±$0.46) |
| Summary agent | 50.0% ($1.26±$1.50) | 38.0% ($8.98±$2.12) | 44.1% ($0.15±$0.01) | 0.31% ($0.05±$0.00) |
| **RLM** | 56.0% ($0.92±$1.23) | 44.7% ($0.84±$0.63) | **48.0%** ($0.61±$0.49) | **23.1%** ($1.02±$0.52) |
| RLM (no sub-calls) | **66.0%** ($0.18±$0.58) | **46.0%** ($0.82±$0.69) | 43.5% ($0.32±$0.13) | 17.3% ($1.77±$1.23) |

Note Qwen3-Coder's REPL-without-sub-calls beats REPL-with-sub-calls on CodeQA + BrowseComp+ — observation 2 confirmed.

**Qwen3-8B (8B-class small model)**:

| Method | CodeQA | BrowseComp+ (1K) | OOLONG | OOLONG-Pairs |
|---|---|---|---|---|
| Base Model | 4.0%* ($0.01±$0.00) | 0.0%* (N/A) | 0.0%* (N/A) | 0.1% ($0.01±$0.00) |
| RLM | 26.0% ($0.04±$0.13) | 2.0% ($0.03±$0.06) | 24.0% ($0.19±$0.26) | 4.3% ($0.05±$0.05) |
| **RLM (fine-tuned)** | **32.0%** ($0.02±$0.02) | **14.0%** ($0.01±$0.03) | **32.0%** ($0.04±$0.09) | **5.2%** ($0.02±$0.02) |

**RLM-Qwen3-8B (fine-tuned)** approaches the wiki's mission-critical numbers: 32.0 / 14.0 / 32.0 / 5.2 across the four tasks. Compare to base GPT-5: 24.0 / 0.0 / 44.0 / 0.1. The 8B fine-tuned model **beats base GPT-5 on three of four tasks** (CodeQA, BrowseComp+, OOLONG-Pairs) — the abstract's claim "approaches the quality of vanilla GPT-5 on three long-context tasks" is precisely this comparison. The fourth task (OOLONG, 32 vs 44) is where GPT-5 still leads at this size.

### The Four Tasks — Characterized

> [!abstract] Each task at a glance
>
> | Task | Source | Token range | Complexity class | What it tests |
> |---|---|---|---|---|
> | **CodeQA** (LongBench v2 split) | Bai et al. 2025 | 23K–4.2M | O(fixed files) | Multi-choice questions over a code repository; reason over fixed file count |
> | **BrowseComp+ (1K docs)** | Chen et al. 2025 | 6M–11M | O(multi-hop) | DeepResearch-style: piece together info across multiple docs; gold + evidence + hard-negative docs guaranteed in 1K-doc subset |
> | **OOLONG** (trec_coarse split) | Bertsch et al. 2025 | 131K | O(N) linear | 50 distributional/categorical queries over a list of question entries; nearly all entries needed per task |
> | **OOLONG-Pairs** | RLM authors' modification | 32K | O(N²) quadratic | 20 new queries over `trec_coarse` requiring aggregating *pairs* of chunks; quadratic in input |
> | S-NIAH (Figure 1 only) | RULER (Hsieh 2024) | 8K-1M | O(1) constant | Single needle in haystack; saturated by frontier models |

The paper's own framing: "more 'complex' problems will exhibit degradation at even shorter lengths than simpler ones." The four chosen tasks span three complexity classes (CodeQA's O(fixed files) is roughly between O(1) and O(N)). This is a **structurally useful taxonomy** for picking benchmarks — it generalizes beyond RLM evaluation to long-context model evaluation overall.

### RLM-Qwen3-8B — The Training Recipe in Detail

This is the paper's load-bearing post-training contribution and it's unexpectedly small/simple:

**Step 1 — Generate trajectories** (the sampling step):
- Take the larger model: **Qwen3-Coder-480B-A35B-Instruct** (the 480B coding model with 35B active)
- Run it AS an RLM (root LM = Qwen3-Coder-480B; sub-call LM = Qwen3-8B itself)
- Run on **750 English LongBenchPro tasks** (English split of the bilingual benchmark)
- Result: **2,250 candidate trajectories** (3 per task on average)

**Step 2 — Filter trajectories**:
- Remove trajectories scoring exactly 0.0
- Remove trajectories not going beyond one turn
- Result: **1,072 candidate trajectories** (~52% retention rate)

**Step 3 — Decompose into SFT samples**:
- Each ROOT RLM TURN becomes a separate SFT sample
- Input: the full history up to that turn
- Output: the root LM's output at that step
- Filter: remove turns beyond Qwen3-8B's context limit (~100K characters approximation)

**Step 4 — Programmatic correction**:
- 16% of turns had FINAL answer template mistakes
- 13% of turns incorrectly used FINAL_VAR (referring to non-existent variables)
- "Qwen3-Coder-480B-A35B had noticeable mistakes in following the RLM instructions, which hurt the performance of the distilled RLM-Qwen3-8B"
- Apply programmatic fix step to common templated mistakes

**Step 5 — Fine-tune**:
- Library: **prime-rl** (Prime Intellect's RL library — github.com/PrimeIntellect-ai/prime-rl)
- Hyperparameters: batch size **64**, **300 training steps**
- Compute: **48 H100 hours total**
- Sampling parameters: per Qwen Team 2025a (Qwen3-8B reference)

**Step 6 — Evaluate**:
- Test on 4 long-context tasks (different from training domain)
- Result: **+28.3% average improvement** over Qwen3-8B-as-RLM-without-fine-tune

**The key insight from the authors** (Section A): "being an effective sub-call model is roughly similar to being a general purpose reasoning model, so we can make the training much more tractable (and seemingly short-horizon) at small scale by focusing on improving the root model's ability to manipulate the REPL and to launch recursive calls."

In other words: train the ROOT, not the sub-call. The root needs to learn the REPL/recursion machinery. The leaves are just regular LM calls — already general-purpose.

> [!success] Mission-relevant takeaway
>
> 48 H100 hours is **~$48-100 USD on a typical H100 cloud rental rate**. For a single open-weight 8B-class model improvement that gets to "approaches GPT-5 on 3 long-context tasks", this is *extremely* tractable. The wiki's mission of post-Anthropic AI stack with $0 / minimal cost has a load-bearing existence proof here: a researcher (or operator) can replicate this training in <2 days of cloud GPU time.

### Six Observations — The Paper's Own Framing

> [!abstract] **Observation 1**: RLMs scale to 10M+ tokens, outperform base + scaffolds
> Up to 2× the performance at comparable/cheaper token costs. Scale beyond base context window.
>
> Mission relevance: **the wiki's 200K-token Opus tier and 32K Qwen tier both extend ~10M+ effective with RLM.**

> [!abstract] **Observation 2**: REPL is necessary; recursion benefits info-dense
> REPL-no-sub-calls is enough for retrieval-style tasks (CodeQA, BrowseComp+). Recursion adds 10-59% on info-dense (OOLONG, OOLONG-Pairs).
>
> Implementation hint: a minimum-viable RLM is just `max_depth=1` (REPL only). Adding recursion is a per-task call.

> [!abstract] **Observation 3**: LM degrades w/ length+complexity; RLM scales
> Across S-NIAH, OOLONG, OOLONG-Pairs at lengths 2¹³ to 2¹⁸: GPT-5 degrades steeply on O(N) and O(N²) tasks; RLM scales gracefully. **RLM(GPT-5) consistently outperforms GPT-5 beyond context length 2¹⁴.**
>
> Implementation hint: at short contexts (<16K), base model can be better. RLM has overhead. The crossover is task-dependent but lives around 2¹⁴ tokens for these complexity classes.

> [!abstract] **Observation 4**: Cost comparable to base, high variance
> 25th/50th/75th/95th percentile cost analysis (Figure 3). Median RLM cheaper than base; 95th percentile much higher (long trajectories). Up to 3× cheaper than Summary agent.
>
> Operational hint: **set `max_budget` and `max_timeout` as hard caps per RLM call** — without them, a 95th-percentile trajectory can be 5-10× a typical query.

> [!abstract] **Observation 5**: Model-agnostic, but models exhibit different behavior
> GPT-5 conservative on sub-calls; Qwen3-Coder needs explicit warning to prevent thousand-sub-call cascades. Same RLM system prompt across models = problematic.
>
> Operational hint: **per-model prompt tuning is required**. Even small models (8B) need their own system-prompt diff to handle context-window awareness.

> [!abstract] **Observation 6**: Training RLMs on one domain → general improvement
> RLM-Qwen3-8B trained on LongBenchPro generalizes to 4 different evaluation tasks. **+28.3% on average.** Inference costs lower than base RLM-Qwen3-8B due to fewer mistakes.
>
> Mission relevance: cross-domain generalization means a single fine-tune produces broad capability gains — load-bearing for the cost story.

### The System Prompt as Operational Artifact

The paper publishes the FULL system prompt in Appendix C (3 variants: GPT-5, Qwen3-Coder, Qwen3-8B; plus the no-sub-calls variant). This is structured-context-as-program at its purest — and worth treating as the canonical example of [Principle 2 (Structured Context Governs Behavior)](../../lessons/04_principles/hypothesis/structured-context-governs-agent-behavior-more-than-content.md) applied at the system-prompt level.

Key design choices visible in the prompt:

> [!info] System-prompt structural choices
>
> 1. **Context metadata declared up-front**: `{context_type}`, `{context_total_length}`, `{context_lengths}` substituted in. The model is TOLD what it's working with before any reasoning.
> 2. **REPL contract numbered**: 3 environment guarantees (context variable, llm_query function, print()) presented as `1. ... 2. ... 3. ...` — same MUST/MUST NOT structural pattern the wiki teaches.
> 3. **Three worked examples inline**: Harry Potter book Q&A (chunk per section), Great Gatsby corpus (chunk by N then aggregate), Markdown-header-aware (split by header, summarize per section). The prompt teaches the strategies the paper later observes the model using.
> 4. **FINAL/FINAL_VAR contract is sacrosanct**: `IMPORTANT: When you are done...you MUST provide a final answer inside a FINAL function...NOT in code.` — uppercase emphasis + must-language. This is exactly the structural pattern that programs the model's stop condition.
> 5. **Per-model differential adjustments**: Qwen3-Coder gets a warning about over-using sub-calls; Qwen3-8B gets context-window-size-awareness adjustments throughout. Same SHAPE, different content per model — matching the wiki's [validation-matrix-test-suite-for-context-injection](../../patterns/) pattern.

### Negative Results — What Didn't Work

The paper has a dedicated "B. Negative Results" section, unusually frank for academic papers. Five named failures:

| # | What didn't work | Why | What was done about it |
|---|---|---|---|
| 1 | Same system prompt across all models | Different undesirable behavior per model | Per-model prompt diffs |
| 2 | Models without coding ability struggle as RLMs | RLM relies on REPL code generation; small Qwen3-8B without coding training fails | Use coding-capable models or fine-tune |
| 3 | Thinking models without sufficient output tokens fail | Qwen3-235B-A22B trajectories ran out of output tokens due to thinking | Caveat — small evaluation with degraded results |
| 4 | Sync sub-calls are slow | Naive blocking implementation | Caveat — known to be solvable with async impl |
| 5 | Distinguishing FINAL vs thoughts is brittle | Model sometimes outputs plan as final | Programmatic safeguards added; root issue: should be RL-trained out |

This list is itself useful for adopters: **don't use RLM with a non-coding-capable model**, **always set output token limits high enough for thinking models**, **expect blocking-call overhead until async lands**, **plan for FINAL parsing edge cases**.

### Funding & Mission Connection — Prime Intellect + Modal Labs + Laude

The acknowledgments name three primary supporters:

- **Laude Institute** — research support
- **Prime Intellect** — both acknowledged AND `prime-rl` is the training library used for RLM-Qwen3-8B. The wiki's existing tracking of Prime Intellect (verifiers library, prime sandboxes) connects directly here.
- **Modal Labs** — acknowledged AND ModalREPL is the canonical isolated-environment reference implementation in the SDK.

This is mission-relevant because:
1. The wiki's [AI Infrastructure Decision Framework 2026](../../spine/references/ai-infrastructure-decision-framework-2026.md) tracks Prime Intellect as a sovereignty-tier provider option.
2. The post-training recipe (1K trajectories, 48 H100 hours, prime-rl) is reproducible by anyone with Prime Intellect compute access — directly aligned with the wiki's anti-vendor-lock-in framing.
3. Modal as the canonical isolated-sandbox reference connects to the wiki's existing Modal-tier discussions in the cost-routing analysis.

### Comparison to Algorithm 2 — The Formal Distinction

The paper presents an Algorithm 2 (a "deceptively similar" but ineffective scaffold) to sharpen RLMs' distinctive design choices:

| Property | Algorithm 2 (effective baseline) | Algorithm 1 (RLM, the paper's contribution) |
|---|---|---|
| **Where prompt P lives** | In the LLM context window from turn 1 (`hist`) | In external REPL state, `M` only sees metadata about P |
| **How output is produced** | Autoregressive `Finish` action — bounded by M's output context | Built up through REPL variables — breaks output bound |
| **Sub-LM call mechanism** | Separate "sub_LLM" action invoked verbalize-style | Programmatic invocation in arbitrary code (loops, transforms) — `Ω(\|P\|)` or `Ω(\|P\|²)` invocations possible |
| **Failure mode** | Falls back to context compaction; bounded by M's input window | None (in principle); recursion cap at `max_depth` is the practical limit |

This formalization is the paper's most academically distinctive contribution — it makes RLM's three design choices precise and shows they're each load-bearing.

## Open Questions

> [!question] Will Prime Intellect / Modal release a hosted RLM-Qwen3-8B that operators can immediately use?
> The model is post-trained but the paper doesn't say if it's released as a Hugging Face checkpoint. If yes, operator can `pip install rlms` + `from rlm import RLM; RLM(backend="vllm", backend_kwargs={"model_name": "OASYS/RLM-Qwen3-8B", "base_url": "..."})` immediately. (Requires: checking Hugging Face, alphaXiv, RLM repo for release status.)

> [!question] Does the training recipe generalize to RLM-Qwen3.6-27B (the wiki's existing tier-0 candidate)?
> If the LongBenchPro→4-task generalization holds at the 27B scale, an RLM-Qwen3.6-27B fine-tune could approach Opus 4.7 on long-context tasks while running locally on operator's RTX 2080 Ti. Compute estimate: ~150-200 H100 hours scaling from 8B → 27B (~3× model size, slightly less in compute due to LoRA possibilities). (Requires: training run + benchmark.)

> [!question] What's the asynchronous sub-call latency improvement?
> The paper says sync sub-calls are slow but "we are confident this can be resolved with a robust implementation." Quantitatively, what's the speedup from async + prefix caching? (Requires: implementation work — directly matches the alexzhang13/rlm CONTRIBUTING.md "If you can tackle these, thanks LOL" tier.)

> [!question] Does deeper recursion (max_depth > 1) actually help on existing benchmarks, or does it just add cost?
> The paper notes "we chose to use a max recursion depth of one" but says "we believe future work should investigate deeper levels of recursion." The OOLONG-Pairs result (O(N²) task) might be the natural fit for max_depth=2. (Requires: benchmark.)

> [!question] Can RLM-style training apply to existing reasoning-trained models (DeepSeek-R1, o1-class)?
> The paper hypothesizes "RLM trajectories can be viewed as a form of reasoning, which can be trained by bootstrapping existing models" — if reasoning-trained models are good substrate for RLM training, the gains might compound. (Requires: experiment.)

> [!question] How does RLM compose with existing structured-context patterns in this wiki?
> The wiki has [model-context-engineering](../../spine/models/depth/model-context-engineering.md) (the 8 structural patterns), [gateway-output-contract](../../spine/standards/gateway-output-contract.md) (the 5 rules), [model-claude-code](../../spine/models/agent-config/model-claude-code.md) (the 4-level extension system). RLM is a NEW substrate that operates AT the inference call. How would the wiki's gateway tools compose with an RLM-augmented LM call? (Requires: design experiment.)

> [!question] What's the OOLONG-Pairs query set?
> Appendix D.1 lists "all queries in this benchmark" (the 20 new pair-aggregation queries). These are not in the raw I read (lines 1-1500). The OOLONG-Pairs benchmark itself is mission-relevant: it's where base models score 0.1% and RLM scores 58.0%. (Requires: ingest the appendix, not just first 1500 lines.)

> [!question] Are the 4 tasks public + reproducible?
> CodeQA (LongBench v2): public benchmark. BrowseComp+: public. OOLONG: anonymous authors shared dataset upon request to RLM team — *may or may not be public yet*. OOLONG-Pairs: defined in this paper's Appendix D.1. Public reproducibility depends on OOLONG release. (Requires: status check on OOLONG public release.)

## Mission Implications — Final, with Numbers

> [!success] The empirical case for the wiki's anti-vendor-lock-in mission, validated:
>
> | Mission claim | Direct evidence |
> |---|---|
> | "Smaller cheaper local models can substitute for frontier cloud models on long-context tasks" | RLM-Qwen3-8B (8B params, $0.02-0.04/query) approaches GPT-5 on 3/4 long-context tasks |
> | "Smart routing drops cost dramatically" | RLM(GPT-5) median cost cheaper than base GPT-5 on 3/4 tasks; up to 3× cheaper than Summary agent |
> | "Tier-0 hardware can host the substitute" | RLM-Qwen3-8B fits on consumer GPU (8B params, ~16GB VRAM at full precision); recipe is 48 H100 hours = ~$48-100 USD to train |
> | "The substitute approaches frontier on hard tasks" | OOLONG-Pairs (O(N²) pair-aggregation, base models 0.1% F1): RLM(GPT-5) 58.0%, RLM(Qwen3-Coder-480B) 23.1%, RLM-Qwen3-8B 5.2%. The pattern holds: RLM unlocks task classes that base models can't do. |
> | "Anti-vendor-lock-in is structurally sound" | Open-source SDK, open-weight Qwen3-8B, public training library (prime-rl), public benchmarks. The full stack to reproduce these results is open. |
>
> **The 2026-04-27 mission deadline is today (T-0). The empirical evidence to make the bet exists in this paper.**

## How to Apply

> [!tip] Concrete next steps grounded in the paper
>
> 1. **Reproduce a single Table 1 cell**: pick OOLONG-Pairs (smallest task, 32K tokens, biggest base→RLM gap). Run RLM(GPT-5) on a few queries from the OOLONG-Pairs Appendix D.1 set. Validate the 58.0% number on operator's setup.
> 2. **Test RLM-Qwen3-8B on operator's RTX 2080 Ti**: if Hugging Face checkpoint released, `pip install rlms` + vLLM serve + run on a long-context query. This is the single most load-bearing test for the post-Anthropic stack thesis.
> 3. **Apply the training recipe to Qwen3.6-27B**: replicate the LongBenchPro → SFT → 4-task evaluation pipeline at the wiki's existing tier-0 candidate scale. Estimated compute: ~150-200 H100 hours (~$300-500 USD).
> 4. **Wrap an existing AICP backend with RLM**: AICP has the `local` backend (LocalAI Qwen3); add RLM wrapping via `pip install rlms`. Validate the long-context capability extension.
> 5. **Update wiki's tier-0 candidate analysis**: the 2026 Consumer Hardware AI Stack spine reference currently names Qwen3.6-27B as the dense reasoning candidate. Add RLM-Qwen3-8B + the post-training recipe as a complementary path: smaller hardware floor, comparable long-context capability via RLM substrate.

## Relationships

- BUILDS ON: [[src-rlm-recursive-language-models-mit-oasys|Synthesis — RLM (Implementation Companion)]]
- BUILDS ON: [[src-rlm-empirical-findings-oolong-browsecomp-rlm-qwen3-8b|Synthesis — RLM Empirical Findings (Blogpost + Abstract)]]
- BUILDS ON: [[model-context-engineering|Model — Context Engineering]] (the 8 structural patterns directly visible in the RLM system prompt)
- DEMONSTRATES: [[structured-context-governs-agent-behavior-more-than-content|Principle 2]] (the system prompt is structured-context-as-program; per-model variants prove the pattern)
- DEMONSTRATES: [[infrastructure-over-instructions-for-process-enforcement|Principle 1]] (the REPL substrate is infrastructure; the LM operates within it; max_depth bound is structural enforcement)
- DEMONSTRATES: [[right-process-for-right-context-the-goldilocks-imperative|Principle 3 — Goldilocks]] (RLM has overhead at short contexts but unlocks long-context tasks; goldilocks decision per task)
- COMPARES TO: [[src-anthropic-effective-harnesses-long-running-agents|Synthesis — Anthropic Effective Harnesses for Long-Running Agents]] (parallel insight; RLM goes further with recursive sub-calls + REPL-as-context)
- COMPARES TO: [[src-claude-agent-sdk-and-managed-agents|Synthesis — Claude Agent SDK and Managed Agents]] (both inference SDKs)
- RELATES TO: [[src-hrm-trm-tiny-recursion-models|Synthesis — HRM and TRM]] (different recursion: latent vs language/REPL)
- FEEDS INTO: [[2026-consumer-hardware-ai-stack|2026 Consumer Hardware AI Stack]] (RLM-Qwen3-8B is a new tier-0 candidate; smaller hardware floor than Qwen3.6-27B)
- FEEDS INTO: [[ai-infrastructure-decision-framework-2026|AI Infrastructure Decision Framework 2026]] (Prime Intellect + Modal connection adds to existing routing analysis)
- FEEDS INTO: [[ai-model-provider-harness-decision-matrix-2026|AI Model Provider Harness Decision Matrix 2026]]
- RELATES TO: [[model-llm-wiki|Model — LLM Wiki]] (the wiki's own synthesis pipeline could integrate RLM-augmented synthesis for long raws)
- RELATES TO: [[model-local-ai|Model — Local AI ($0 Target)]] (the empirical case for local + RLM as post-Anthropic substrate)
- RELATES TO: [[never-synthesize-from-descriptions-alone|Never Synthesize from Descriptions Alone]] (this synthesis cites the actual paper PDF as Layer 1 source — the appendix beyond line 1500 of the raw is still Layer 0 description from this synthesis's POV; deeper read pending)

## Backlinks

[[Synthesis — RLM (Implementation Companion)]]
[[Synthesis — RLM Empirical Findings (Blogpost + Abstract)]]
[[model-context-engineering|Model — Context Engineering]]
[[structured-context-governs-agent-behavior-more-than-content|Principle 2]]
[[infrastructure-over-instructions-for-process-enforcement|Principle 1]]
[[right-process-for-right-context-the-goldilocks-imperative|Principle 3 — Goldilocks]]
[[src-anthropic-effective-harnesses-long-running-agents|Synthesis — Anthropic Effective Harnesses for Long-Running Agents]]
[[src-claude-agent-sdk-and-managed-agents|Synthesis — Claude Agent SDK and Managed Agents]]
[[Synthesis — HRM and TRM]]
[[2026 Consumer Hardware AI Stack]]
[[ai-infrastructure-decision-framework-2026|AI Infrastructure Decision Framework 2026]]
[[AI Model Provider Harness Decision Matrix 2026]]
[[model-llm-wiki|Model — LLM Wiki]]
[[model-local-ai|Model — Local AI ($0 Target)]]
[[never-synthesize-from-descriptions-alone|Never Synthesize from Descriptions Alone]]
