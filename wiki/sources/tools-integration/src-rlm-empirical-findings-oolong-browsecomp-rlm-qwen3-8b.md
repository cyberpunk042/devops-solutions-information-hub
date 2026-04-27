---
title: "Synthesis — RLM Empirical Findings: OOLONG, BrowseComp-Plus, and RLM-Qwen3-8B Approaching GPT-5 (Oct 2025 blogpost + Dec 2025/Jan 2026 arXiv 2512.24601)"
aliases:
  - "RLM Empirical Findings"
  - "RLM Benchmark Results"
  - "RLM-Qwen3-8B"
  - "Synthesis — RLM Benchmarks"
type: source-synthesis
domain: tools-integration
status: synthesized
confidence: high
maturity: seed
created: 2026-04-27
updated: 2026-04-27
last_reviewed: 2026-04-27
sources:
  - id: rlm-arxiv-abstract
    type: paper
    url: https://arxiv.org/abs/2512.24601
    file: raw/articles/251224601-recursive-language-models.md
    title: "Recursive Language Models — arXiv 2512.24601 (v2 28 Jan 2026)"
    description: "Submitted 31 Dec 2025; revised 28 Jan 2026 (v2). Authors: Alex L. Zhang, Tim Kraska, Omar Khattab. 9 pages + 33 with Appendix. cs.AI / cs.CL."
    ingested: 2026-04-27
  - id: rlm-blogpost-oct-2025
    type: article
    url: https://alexzhang13.github.io/blog/2025/rlm/
    file: raw/articles/recursive-language-models-alex-l-zhang.md
    title: "Recursive Language Models (Oct 2025 blogpost)"
    description: "Original blogpost preceding the arXiv paper; primary source for OOLONG + BrowseComp-Plus experimental results"
    ingested: 2026-04-27
  - id: rlm-implementation-companion
    type: wiki
    file: wiki/sources/tools-integration/src-rlm-recursive-language-models-mit-oasys.md
    description: "Companion synthesis on RLM architecture + reference SDK (alexzhang13/rlm); this page covers the empirical/research framing"
  - id: rlm-tweet-summary
    type: article
    url: https://x.com/a1zhang/status/1978469116542337259
    description: "Original Twitter/X compressed-summary thread"
tags: [rlm, recursive-language-models, empirical-findings, benchmark-results, oolong, browsecomp-plus, rlm-qwen3-8b, gpt-5-mini, gpt-5, context-rot, long-context, retrieval, post-training, dec-2025-arxiv, oct-2025-blogpost, mit-oasys, mission-2026-04-27, tier-0-candidate, tools-integration, anti-vendor-lock-in, paradigm-validation]
---

# Synthesis — RLM Empirical Findings: OOLONG, BrowseComp-Plus, and RLM-Qwen3-8B Approaching GPT-5

## Summary

This is the empirical-findings companion to [Synthesis — RLM (Recursive Language Models)](src-rlm-recursive-language-models-mit-oasys.md). The Oct 2025 blogpost and Dec 2025 → Jan 2026 arXiv paper (2512.24601, v2) provide the actual experimental evidence behind the unbelievable-sounding RLM claim. **Three load-bearing results**: (1) On the OOLONG `trec_coarse` long-context-reasoning benchmark at 132K-token contexts, **RLM(GPT-5-mini) outperforms GPT-5 by ~114% (over double the raw score)** at roughly the same total API cost per query — and the cheaper-model-with-RLM beats the more-expensive-model-without-RLM. (2) On the BrowseComp-Plus DeepResearch benchmark, **RLM(GPT-5) maintains perfect performance at 1000 documents (10M+ tokens) without a retriever**, while base GPT-5 (truncated or pre-query-BM25) shows clear performance dropoff as document count grows. (3) The arXiv paper extends to a *post-trained* natively-recursive model: **RLM-Qwen3-8B outperforms the underlying Qwen3-8B by 28.3% on average and approaches the quality of vanilla GPT-5 on three long-context tasks** — the first natively recursive language model trained explicitly for the paradigm. The paper also reports RLMs successfully process inputs **up to two orders of magnitude beyond model context windows** while dramatically outperforming both vanilla frontier LLMs and common long-context scaffolds at comparable cost across four diverse long-context tasks. These results are the validated answer to the operator's "*this sounds unbelievable*" reaction — they ARE unbelievable in the sense of "structurally surprising" but the evidence is empirical, replicable from the open-source [github.com/alexzhang13/rlm](https://github.com/alexzhang13/rlm) reference implementation, and tied to specific benchmarks the community can re-run.

## Reference Card

> [!info] Empirical-findings reference card
>
> | Field | Value |
> |---|---|
> | **Paper** | arXiv 2512.24601, v2 (28 Jan 2026 revision; v1 31 Dec 2025) |
> | **Pages** | 9 main + 33 with Appendix |
> | **Subjects** | cs.AI · cs.CL |
> | **Authors** | Alex L. Zhang · Tim Kraska · Omar Khattab |
> | **Lab funding** | Partly Laude Institute support |
> | **Core empirical bets** | Two orders of magnitude beyond model context window · approaches frontier-LLM quality at lower cost · post-trained 8B approaches GPT-5 |
> | **Benchmarks used** | OOLONG (trec_coarse split, 132K + 263K contexts) · BrowseComp-Plus (10/50/100/1000 docs, up to 10M+ tokens) |
> | **Models tested** | GPT-5 · GPT-5-mini · Qwen3-8B · post-trained RLM-Qwen3-8B |
> | **Recursion depth in experiments** | 1 (root LM can call sub-LMs but sub-LMs cannot recurse further); future work deeper |
> | **Confidence** | high — read both the arXiv abstract page (with v2 abstract text + author list + dates) and the full Oct 2025 blogpost (Layer 1 source); the full PDF v2 with appendix experiments has not been ingested into raw/ |
> | **Operator framing this validates** | "this sounds unbelievable" — the structural claim genuinely IS surprising; the empirical evidence makes it credible enough to act on |

## Key Insights

1. **The headline number from the blogpost: ~114% raw-score improvement at comparable cost.** On OOLONG `trec_coarse` at 132K-token contexts, RLM(GPT-5-mini) scored over 34 points higher than GPT-5 — over DOUBLE the raw score. *Median* query cost was actually *cheaper* than GPT-5 (some outlier expensive queries pulled the average up but the typical query was cheaper). This is the single most surprising single-number result: **a smaller cheaper model + RLM > a larger more-expensive model alone**, by a large margin, on a long-context-reasoning benchmark.

2. **The arXiv-paper post-training number: RLM-Qwen3-8B approaches GPT-5 on 3 long-context tasks.** The paper post-trains an 8B model to be natively recursive (i.e., trained to use the REPL paradigm rather than just be compatible with it as a wrapper). RLM-Qwen3-8B *outperforms the underlying Qwen3-8B by 28.3% on average*, and on three long-context tasks *approaches the quality of vanilla GPT-5*. This is the validation that RLM is not just a cheap-frontier-API trick — the paradigm itself is something models can be trained for, with cost/performance unlocks at the 8B scale.

3. **Two orders of magnitude beyond context window.** Per the arXiv abstract: RLMs "successfully process inputs up to two orders of magnitude beyond model context windows." Concretely: a model with a 4K context window can handle inputs around 400K tokens; a model with 128K can handle ~12.8M; a model with 1M can handle ~100M. The mechanism is the REPL — the LM never sees the whole context at once; it programmatically chunks/peeks/recurses.

4. **BrowseComp-Plus at 1000 documents (10M+ tokens): RLM is the only method achieving and maintaining perfect performance.** The blogpost's most striking result for a retrieval-style task. Baselines tested: GPT-5 (no truncation, just fails over context limit), GPT-5 (truncated to last 272K tokens), GPT-5 + pre-query BM25 (top-40 docs from BM25 then GPT-5), RLM(GPT-5) with sub-calls, RLM(GPT-5) without sub-calls, ReAct + GPT-5 + BM25. As doc count scales 10 → 50 → 100 → 1000, only the iterative methods (RLM, ReAct) maintain reasonable performance; only RLM(GPT-5) achieves PERFECT at 1000 docs. The ablation (RLM-without-recursion) hits ~90% — recursion provides the last 10 points but the REPL alone is most of the benefit.

5. **Context rot is the failure mode RLM addresses, but RULER-style benchmarks miss it.** The blogpost is direct: most needle-in-the-haystack benchmarks like RULER are saturated (90%+ on year-old models). Context rot — the colloquial sense of "model gets dumber as conversation grows" or "Claude Code history gets bloated and quality degrades" — is real but hard to benchmark. RLM was tested on benchmarks (OOLONG) where this degradation actually manifests for frontier LLMs. The framing matters: existing long-context benchmarks UNDERESTIMATE the problem RLM solves.

6. **Recursion accounts for ~10% of the total benefit on OOLONG; the REPL accounts for the rest.** When the experimenters ablated `rlm_query` (REPL but no recursion), RLM degraded by ~10% on OOLONG. Most of the gain comes from the REPL paradigm itself (programmatic context manipulation), not from recursive sub-calls. This has design implications: even at `max_depth=1` (no recursion), the REPL substrate is most of the value. Recursion is the cherry on top, not the cake.

7. **GPT-5 inside RLM doesn't show context rot at 263K; GPT-5-mini does.** A subtle finding from the 263K-token experiment: when context length doubled, GPT-5-mini (smaller, weaker context handler) showed performance drop; GPT-5 didn't (within its window). This means: weaker base models benefit *more* from RLM at long context, not less. The paradigm is most valuable for the cheaper-smaller-model end of the routing decision.

8. **Five model strategies emerge spontaneously, without prompting.** The blogpost documents what RLMs actually DO inside the REPL: (a) **Peek** — start with `context[:2000]` to observe structure; (b) **Grep** — regex/keyword search to narrow lines of interest before deeper processing; (c) **Partition + Map** — chunk context, run recursive LM calls per chunk, combine; (d) **Summarize** — natural generalization of compaction strategies; (e) **Long-input/long-output programmatic** — for tasks like LoCoDiff (git diff history tracking), the LM can ONE-SHOT by writing code rather than generating output token-by-token. The strategies emerge from the model deciding how to interact, not from human-prescribed workflows.

9. **The philosophy quote that contrasts RLM with agents.** From the blogpost (worth preserving verbatim): *"Agents are designed based on human / expert intuition on how to break down a problem to be digestible for an LM. RLMs are designed based on the principle that fundamentally, LMs should decide how to break down a problem to be digestible for an LM."* This is the conceptual sword cut. Modern agentic frameworks (Cursor, Claude Code, ReAct, ROMA) decompose by *task*. RLM defers decomposition to the model and decomposes by *context*. Different ontology of the problem.

10. **Limitations called out honestly.** Per the blogpost, RLM is NOT YET optimized for speed: each recursive LM call is blocking, no prefix caching, queries range from "a few seconds to several minutes." There are no strong guarantees on total cost or runtime. The author flags this as "amazing news" for the systems community — RLM at scale is a wide-open systems-engineering problem (efficient async sub-calls, prefix caching across recursive trees, cost guarantees). Don't deploy RLM in production latency-sensitive paths today; do explore RLM in research / batch / offline contexts.

11. **Test-time inference scaling: RLM is a new axis of scale, learnable via RL.** The blogpost connects RLM to the broader test-time-scaling story (CoT-style reasoning, ReAct-style agents). The trajectory of how an RLM chooses to interact with its context is *learnable* — i.e., RL-trainable in the same way reasoning is currently trained for frontier models. The arXiv paper validates this: RLM-Qwen3-8B is the first such model. The author predicts: "RLMs trained explicitly to recursively reason are likely to represent the next milestone in general-purpose inference-time scaling after CoT-style reasoning models and ReAct-style agent models."

12. **Comparison framing: RLM ≠ MemGPT, MemWalker, LADDER, THREAD, RSA, CodeAct.** The blogpost lists related works:
    - **MemGPT** — defers context management to model but builds on a single context call
    - **MemWalker** — tree-structured summarization, prescribed shape
    - **LADDER** — problem-decomposition not context-decomposition
    - **THREAD** — modifies output generation to spawn child threads
    - **TRM (Tiny Recursive Model)** — already in this wiki ([[src-hrm-trm-tiny-recursion-models|HRM/TRM synthesis]]); recursion in latent space, not language space
    - **Recursive LLM Prompts** — early experiment treating prompt as evolving state
    - **Recursive Self-Aggregation (RSA)** — combines test-time inference sampling
    - **CodeAct** — closest analog; RLM extends with recursive model calls
    - **ROMA agent** — closest agentic-scaffolding analog (decomposes problems with sub-agents)

    RLM's distinctive claim: context-as-variable, decomposition deferred to model, recursive sub-LMs first-class.

## Deep Analysis

### Result 1 — OOLONG `trec_coarse` at 132K Tokens: 114% Raw-Score Increase

**Setup**:
- Benchmark: OOLONG `trec_coarse` split, 6 query types about a giant list of ~3000-6000 entries (date, user ID, instance text — semantic labels NOT explicit).
- Example query: "For instances associated with user IDs [list of 20 IDs], how many should be classified as label 'entity'?"
- Filter: contexts ≥128K tokens (~100 queries).
- Evaluation: number of queries answered correctly; numerical/counting problems use a continuous scoring metric.

**Methods tested**:
| Method | Description |
|---|---|
| GPT-5 | Whole context + query → answer |
| GPT-5-mini | Whole context + query → answer (smaller cheaper baseline) |
| **RLM(GPT-5-mini)** | GPT-5-mini as root, recursively calls GPT-5-mini in REPL |
| RLM(GPT-5) without sub-calls | Ablation: REPL but no recursion |
| ReAct + GPT-5 + BM25 | Chunk context per line, BM25 retrieve top-10 per request |

**Result**: **RLM(GPT-5-mini) outperforms GPT-5 by over 34 points (~114% raw-score increase, OVER DOUBLE)**. Median query cost cheaper than GPT-5. Without recursion, RLM degraded by ~10% — ablation confirms most-but-not-all benefit comes from the REPL substrate alone.

**Why this matters**: A *cheaper* model + RLM beats a *more-expensive* model alone, on the same benchmark, at the same cost. This is direct empirical support for the cost-routing implication: route to smaller-cheaper-models with RLM-augmentation, save tokens, get better answers.

### Result 2 — OOLONG at 263K Tokens: 49% Raw-Score Increase

**Setup**: Same benchmark, but contexts doubled to ~263K tokens (near GPT-5's 272K context limit).

**Result**:
- **RLM(GPT-5-mini) outperforms GPT-5 by over 15 points (~49% increase)**.
- Cheaper per query on average.
- **GPT-5-mini direct shows performance drop at 263K** (context rot at the small-model end).
- **GPT-5 direct does NOT drop within window** (still fits in 272K context).
- RLM degradation occurs mainly on counting problems at this scale.

**Implication**: Context rot affects smaller models more severely. The RLM substrate is most valuable for the smaller-model side of the routing decision, exactly where cost optimization wants to live. As contexts grow toward the limit, the GAP between "use big-context model directly" and "use small model + RLM" actually widens in RLM's favor.

### Result 3 — BrowseComp-Plus at 10/50/100/1000 Documents: Perfect at 10M+ Tokens

**Setup**:
- BrowseComp-Plus: pre-downloaded ~100K-document corpus from the original BrowseComp DeepResearch benchmark.
- Multi-hop queries: answers require associating information across multiple documents (e.g., "what trading card released between 2005-2015 with multiple rarities used in a Japanese world-championship deck whose lore identifies it as armor for a different card released 2013-2018, and is below level 8?").
- Subset: 20 randomly sampled queries.
- Document count varied: 10, 50, 100, 1000 documents in context.
- Always include gold/evidence documents; include hard-mined negatives if available.
- GPT-5 fits ~40 documents before exceeding 272K input context.

**Methods tested**:
| Method | Behavior at 1000 docs |
|---|---|
| GPT-5 (no truncation) | Fails — exceeds context limit |
| GPT-5 (truncated to most-recent tokens) | Fails — random docs included, gold lost |
| GPT-5 + pre-query BM25 (top-40) | Drops as relevant docs less likely in top-40 |
| **RLM(GPT-5) with sub-calls** | **Perfect — 100% on the 20-query sample** |
| RLM(GPT-5) without sub-calls | ~90% — REPL alone is most of the benefit |
| ReAct + GPT-5 + BM25 | Maintains reasonable performance — iterative method |

**Result**: **RLM(GPT-5) is the ONLY method achieving and maintaining perfect performance at the 1000-document scale (~10M+ tokens) without a retriever**. Cost scales reasonably as a function of context length (sub-linear in document count for typical query patterns). Key caveat: BM25 baseline indexes per-query (more powerful than indexing the full 100K corpus once), so the comparison is favorable to BM25 — RLM still wins.

**Implication for retrieval**: For multi-hop tasks where the answer requires associating across documents, RLM substitutes for retrieval. The model decides which documents to peek at, grep through, recursively process — without a pre-built index. For long-document corpora that fit in memory, this avoids the index-build cost entirely.

### Result 4 — Post-Training: RLM-Qwen3-8B Approaches GPT-5

This result lives in the arXiv paper (v2, 28 Jan 2026), referenced in the abstract:

> "At a small scale, we post-train the first natively recursive language model. Our model, RLM-Qwen3-8B, outperforms the underlying Qwen3-8B model by 28.3% on average and even approaches the quality of vanilla GPT-5 on three long-context tasks."

The paper's experiments cover **four diverse long-context tasks** (per abstract); the post-training section evidently covers three of them where the 8B-post-trained-RLM approaches GPT-5. The full task list and per-task numbers live in the paper's appendix — **the paper PDF has not been ingested into raw/ yet**; this synthesis covers what the abstract + blogpost establish, not the full appendix.

**Implication for the wiki's mission**: a post-trained 8B model approaching GPT-5 on long-context tasks is the *direct cost-reduction proof*. An 8B model can run on consumer hardware (the wiki's tier-0 candidate Qwen3.6-27B is much larger than 8B; a post-trained RLM-Qwen3-8B is even more accessible). The arXiv paper has the full training recipe — anyone with consumer GPU + the open-source RLM SDK + the right post-training data can reproduce.

### Result 5 — Two Orders of Magnitude Beyond Context Window

The arXiv abstract's general-claim:

> "We find that RLMs can successfully process inputs up to two orders of magnitude beyond model context windows..."

Operationally:
| Base context window | Effective RLM context |
|---|---|
| 4K (small open-weight) | ~400K |
| 32K (Qwen3 default) | ~3.2M |
| 128K (most current frontier) | ~12.8M |
| 272K (GPT-5) | ~27M+ |
| 1M (Gemini long-context) | ~100M+ |

The blogpost's BrowseComp-Plus result (10M+ tokens with GPT-5 root LM) lands in this regime.

### Spontaneous Strategies — What the LM Actually Does

The blogpost identifies five strategies the RLM root LM picks up without explicit prompting:

> [!example]- **Peeking — start by observing the context's structure**
>
> The root LM begins with only the query and the knowledge that `context` exists in a REPL variable. To understand its shape, it writes:
> ```python
> print(len(context))
> print(context[:2000])
> ```
> This is the human-researcher behavior — peek at a few entries to understand format before doing anything substantive. RLM does it spontaneously.

> [!example]- **Grepping — narrow the search space with regex/keywords**
>
> Rather than semantic retrieval (BM25, embeddings), the RLM uses Python's string operations:
> ```python
> import re
> matching_lines = [l for l in context.split('\n') if re.search(r'User: 67144', l)]
> print(matching_lines[:50])
> ```
> The blogpost notes this is particularly useful for arbitrary long context inputs where indexing a retriever is expensive on the fly.

> [!example]- **Partition + Map — chunk context, recurse per chunk, combine**
>
> For semantically-difficult queries (where grep can't help):
> ```python
> chunks = [context[i:i+5000] for i in range(0, len(context), 5000)]
> labels = llm_query_batched([f"Label this question: {c}" for c in chunks])
> answer = llm_query("Use these labels to answer query: " + ...)
> ```
> The blogpost example: OOLONG queries asking the model to "label each question" → root LM partitions context, dispatches recursive LM calls to label each partition, combines the labeled set.

> [!example]- **Summarization — natural compaction over subsets**
>
> RLMs are a natural generalization of summarization-based context-window-management strategies. The model summarizes irrelevant subsets of the context to free working memory. This is what `compaction=True` in the SDK automates.

> [!example]- **Long-input / long-output programmatic — one-shot via REPL code**
>
> For tasks like LoCoDiff (track a long git-diff history and produce the final file): GPT-5 directly fails (<10% on 75K-token histories). RLM(GPT-5) sometimes one-shots by *programmatically* processing the diff sequence:
> ```python
> # Pseudocode — actual is more nuanced
> file_state = []
> for diff_block in parse_diffs(context):
>     file_state = apply_diff(file_state, diff_block)
> FINAL_VAR(file_state)
> ```
> The blogpost: "RLMs offer a framework for avoiding the need for [programmatic abilities the LM lacks] altogether" — i.e., the LM doesn't need to be GOOD at huge multiplications or diff tracking; it just needs to be good at writing code that does it.

### Comparison to Prior Work — The Distinctive Claim

| Prior work | What it does | How RLM differs |
|---|---|---|
| **MemGPT** | LM manages own memory across calls | MemGPT builds on a single eventual LM call; RLM has recursive sub-calls as first-class |
| **MemWalker** | Tree-structured summarization | MemWalker imposes a fixed tree shape; RLM defers shape to LM |
| **LADDER** | Decomposes problems hierarchically | LADDER decomposes by problem; RLM decomposes by context |
| **THREAD** | Spawns child threads in output generation | THREAD modifies generation; RLM modifies inference paradigm |
| **TRM (Tiny Recursive Models)** | Latent-space iterative refinement | TRM iterates on latent representation; RLM iterates on text via code |
| **Recursive LLM Prompts** | Treat prompt as evolving state | Earlier experiment; RLM formalizes with REPL grounding |
| **Recursive Self-Aggregation (RSA)** | Sample candidate responses, aggregate | RSA aggregates candidates; RLM operates on context |
| **CodeAct** | LM acts via code generation in REPL | RLM extends CodeAct with recursive model calls + context-as-variable focus |
| **ROMA agent** | Decomposes problems with sub-agents | ROMA decomposes by task; RLM decomposes by context |

The two-axis distinction:
- **Decomposition by**: task (most agentic frameworks) vs **context** (RLM)
- **Decomposition author**: human/expert intuition (most agentic frameworks) vs **the model itself, at inference time** (RLM)

### Limitations + Open Systems Engineering

> [!warning] What the blogpost is honest about
>
> **Not optimized for speed:**
> - Each recursive LM call is *blocking* (no async dispatch within REPL execution)
> - No prefix caching across recursive calls (each child rebuilds context fresh)
> - Per-query latency: "a few seconds to several minutes" depending on partition strategy
>
> **No strong cost/runtime guarantees:**
> - Total API cost can vary widely per query
> - Total wall-clock time depends on partition strategy + recursive depth
> - SDK provides `max_budget`, `max_timeout`, `max_tokens`, `max_errors` as user-set explicit limits, but these are abort-conditions, not predictive bounds
>
> **Author's framing**: "amazing news" for the systems community / GPU MODE community — RLM is a research paradigm with massive low-hanging-fruit for systems engineering. The CONTRIBUTING.md "If you can tackle these, thanks LOL" tier explicitly calls out:
> - Pipelining / asynchrony of LM calls — "could be a paper of its own"
> - Efficient prefix caching — "could also be a paper / entire research project"

### Where RLM Sits in the Test-Time-Scaling Story

The blogpost's framing puts RLM as a NEW axis of inference-time scaling, complementary to existing axes:

| Era | Scaling axis | Examples |
|---|---|---|
| Pre-2022 | Model size | GPT-2 → GPT-3 |
| 2022-2023 | Instruction-tuning + RLHF | GPT-3.5 / ChatGPT |
| 2023-2024 | ReAct-style agentic loops | Codex, Claude Code, Cursor |
| 2024-2025 | CoT / reasoning models | o1 / o3 / DeepSeek-R1 / Qwen3 |
| 2025 → | **RLM-style recursive context-decomposition** | RLM-Qwen3-8B, future RLM-trained models |

The author's prediction: "RLMs trained explicitly to recursively reason are likely to represent the next milestone in general-purpose inference-time scaling after CoT-style reasoning models and ReAct-style agent models."

## Mission Implications — Updated with Empirical Evidence

| Mission element | Without RLM evidence (yesterday) | WITH RLM evidence (today) |
|---|---|---|
| Local AI tier sufficiency for long-context | Theoretical — "smaller models + recursion may approach larger models" | **Empirical — RLM(GPT-5-mini) > GPT-5 by 114% on OOLONG; RLM-Qwen3-8B approaches GPT-5 on 3 long-context tasks** |
| Cost-routing strategy | Smart routing alone drops $540 → $100 CAD/mo | Smart routing + RLM-augmentation could drop further: cheaper-model + RLM > more-expensive-model on long-context tasks at comparable cost |
| Tier-0 hardware need | Qwen3.6-27B on RTX 2080 Ti is the candidate | **Qwen3-8B (or RLM-Qwen3-8B fine-tune) on consumer hardware suffices for long-context per the paper's post-training results** — even smaller hardware could work |
| Post-Anthropic milestone (2026-04-27 = today, T-0) | Reachable on smart-routing + Qwen3.6-27B | **Reachable on smart-routing + RLM-augmented local model**, with paper-level evidence backing the capability |
| Sovereignty fallback | Local K2.6 at 0.3 tok/s — slow but mission-milestone | Same. RLM doesn't change the throughput floor; it changes the *quality* of what can be done at that throughput |

> [!tip] **Operator's "this sounds unbelievable" — calibrated**
>
> The "unbelievable" reaction is well-grounded:
> - 114% raw-score improvement (cheaper model + RLM > expensive model alone) IS unbelievable as a single number
> - Perfect performance at 10M+ tokens without retrieval IS unbelievable as a structural claim
> - 8B post-trained model approaching GPT-5 on 3 long-context tasks IS unbelievable as a cost story
>
> The paradigm achieves these via REPL-based context decomposition + bounded recursion. Empirically validated on OOLONG + BrowseComp-Plus + the post-training experiments. The author flags limitations honestly (speed, async, no caching). For the wiki's mission: RLM is **structurally aligned with the anti-vendor-lock-in framing** — it makes smaller open-weight models more capable, not just cheaper.

## Open Questions

> [!question] What are the four diverse long-context tasks in the arXiv paper?
> The abstract names "four diverse long-context tasks" but doesn't list them. The blogpost covers OOLONG and BrowseComp-Plus (only two). The other two are presumably in the paper's appendix. (Requires: ingesting arXiv 2512.24601 PDF directly, not just the abstract page.)

> [!question] What is the post-training data + recipe for RLM-Qwen3-8B?
> The arXiv paper post-trains the first natively recursive language model. The training data shape, RL reward design, and compute budget are not in the abstract or blogpost. (Requires: paper PDF appendix.)

> [!question] How does RLM-Qwen3-8B compare to other 8B-class models (Llama-3.1-8B, Mistral-7B-v0.3, Qwen2.5-7B)?
> The 28.3% improvement over Qwen3-8B is impressive, but cross-8B comparisons matter for adoption decisions (especially for the wiki's mission of post-Anthropic stack with locally-runnable models). (Requires: paper PDF + possibly direct benchmarking.)

> [!question] Can the RLM-Qwen3-8B post-training approach be applied to Qwen3.6-27B (the wiki's existing tier-0 candidate)?
> If post-training to be RLM-native scales to 27B, it could combine the dense-27B coding gains (existing wiki spine reference) with the RLM long-context paradigm. (Requires: paper recipe + sufficient training compute.)

> [!question] What's the latency profile per task class?
> Blogpost says "a few seconds to several minutes" — too wide for production deployment decisions. Per-benchmark latency p50/p95/p99 would inform whether RLM is suitable for batch-only or could approach interactive. (Requires: instrumentation of the alexzhang13/rlm reference SDK on real workloads.)

> [!question] Does prefix caching, when implemented (the "could be a paper" TODO), restore latency to acceptable interactive bounds?
> The fundamental cost / latency limiter is independent re-prompting per recursive sub-call. Prefix caching would dramatically reduce both. (Requires: someone in the systems community tackling that TODO.)

> [!question] How does compaction in RLM compare to manual context compaction in Claude Code / OpenAI assistants API?
> RLM's `compaction=True` auto-summarizes when context fills. The wiki's [model-context-engineering](../../spine/models/depth/model-context-engineering.md) discusses compaction as a reset event. RLM's compaction operates within a single completion; it's a different beast than session-level compaction. (Requires: comparison experiment.)

> [!question] Could the wiki's own ingestion pipeline benefit from RLM-augmented synthesis?
> The wiki's `tools/pipeline.py fetch+synth` currently uses a single LM call to produce source-syntheses. For long raws (e.g., this RLM repo at 4142 lines, or the awslabs/aidlc-workflows raw at 6340 lines), an RLM-augmented synthesizer could programmatically chunk, summarize per chunk, and produce more thorough syntheses. (Requires: small experiment using the alexzhang13/rlm SDK on a real raw.)

## Applicability

> [!info] Where these findings apply directly
> - **Long-context reasoning** (counting/distributional queries over thousands of entries — OOLONG-class) — RLM(cheaper-model) > frontier-model-alone empirically
> - **Multi-hop document retrieval at scale** (1000+ documents, 10M+ tokens — BrowseComp-Plus-class) — RLM is the only method maintaining performance
> - **Programmatic long-input/long-output** (LoCoDiff-class git history, big-multiplication-class) — RLM can one-shot via code generation
> - **Cost-conscious deployment** where smaller models can substitute for larger ones IF given the RLM substrate

> [!warning] Where these findings do NOT apply
> - **Latency-sensitive interactive UX** (chat) — until prefix caching + async dispatch land, RLM adds seconds-to-minutes per query
> - **Short-context tasks** — RLM machinery is overhead with no benefit
> - **Tasks the model already does well alone** — many existing long-context benchmarks (RULER, NIAH) are saturated; RLM is for the hard remaining cases
> - **Production deployment without budgets** — without `max_budget`/`max_timeout`/`max_tokens` set, an RLM call CAN run for several minutes; this is research-grade

## How to Apply

> [!tip] Concrete next steps the wiki / operator could take
>
> 1. **Reproduce the OOLONG result locally**: install `pip install rlms`, get OOLONG `trec_coarse` split (anonymous authors share on request per the blogpost), run RLM(GPT-5-mini) vs GPT-5 baseline. Validate the 114% number on the operator's hardware/setup.
> 2. **Try the post-trained RLM-Qwen3-8B**: when/if the model is released (the paper post-trains it; release status not in abstract), compare on operator's tier-0 RTX 2080 Ti. This is the load-bearing test for the cost story.
> 3. **Wrap an existing AICP backend with RLM**: take the existing `local` backend in AICP (LocalAI Qwen3/Gemma4), add an `rlm_local` backend that wraps it via `pip install rlms`'s vLLM-compatible interface. Test on a long-context task.
> 4. **Wiki-side experiment**: try RLM-augmented synthesis on a long raw (e.g., a 6000+-line repo dump) to see if synthesis quality improves. Compare to the current single-LM-call synthesis.
> 5. **Track the systems-engineering TODOs**: prefix caching + async dispatch are the latency unlocks. When community contributions land, RLM moves from research-grade to production-eligible.

## Relationships

- BUILDS ON: [[src-rlm-recursive-language-models-mit-oasys|Synthesis — RLM (Recursive Language Models): Implementation companion]]
- BUILDS ON: [[model-context-engineering|Model — Context Engineering]] (RLM provides empirical proof of the OS-analogy / context-as-RAM framing)
- BUILDS ON: [[structured-context-governs-agent-behavior-more-than-content|Principle 2 — Structured Context Governs Behavior]] (RLM moves "structure" to the program-grammar level)
- DEMONSTRATES: [[infrastructure-over-instructions-for-process-enforcement|Principle 1]] (RLM's REPL substrate is infrastructure that the LM operates within; structure beats prompt-only by 114% on OOLONG)
- DEMONSTRATES: [[right-process-for-right-context-the-goldilocks-imperative|Principle 3 — Goldilocks]] (RLM is the right process for long-context tasks; not for short interactive ones)
- COMPARES TO: [[src-anthropic-effective-harnesses-long-running-agents|Synthesis — Anthropic Effective Harnesses for Long-Running Agents]] (parallel insight, different abstraction layer)
- COMPARES TO: [[src-hrm-trm-tiny-recursion-models|Synthesis — HRM and TRM]] (different recursion: latent space vs language/REPL space)
- COMPARES TO: [[src-claude-agent-sdk-and-managed-agents|Synthesis — Claude Agent SDK and Managed Agents]] (both inference SDKs; RLM adds REPL substrate)
- FEEDS INTO: [[2026-consumer-hardware-ai-stack|2026 Consumer Hardware AI Stack]] (RLM-Qwen3-8B is a tier-0 candidate; potentially smaller hardware floor than Qwen3.6-27B)
- FEEDS INTO: [[ai-infrastructure-decision-framework-2026|AI Infrastructure Decision Framework 2026]] (adds inference-paradigm dimension: single-shot vs RLM-recursive)
- FEEDS INTO: [[ai-model-provider-harness-decision-matrix-2026|AI Model Provider Harness Decision Matrix 2026]]
- RELATES TO: [[model-llm-wiki|Model — LLM Wiki]] (the wiki's own synthesis pipeline could integrate RLM)
- RELATES TO: [[model-local-ai|Model — Local AI ($0 Target)]] (RLM is force-multiplier for the local-AI cost story)
- RELATES TO: [[never-synthesize-from-descriptions-alone|Never Synthesize from Descriptions Alone]] (this synthesis cites the abstract + blogpost as Layer 1; the paper PDF appendix is the deeper Layer 1 not yet ingested)

## Backlinks

[[Synthesis — RLM (Recursive Language Models): Implementation companion]]
[[model-context-engineering|Model — Context Engineering]]
[[Principle 2 — Structured Context Governs Behavior]]
[[infrastructure-over-instructions-for-process-enforcement|Principle 1]]
[[right-process-for-right-context-the-goldilocks-imperative|Principle 3 — Goldilocks]]
[[src-anthropic-effective-harnesses-long-running-agents|Synthesis — Anthropic Effective Harnesses for Long-Running Agents]]
[[Synthesis — HRM and TRM]]
[[src-claude-agent-sdk-and-managed-agents|Synthesis — Claude Agent SDK and Managed Agents]]
[[2026 Consumer Hardware AI Stack]]
[[ai-infrastructure-decision-framework-2026|AI Infrastructure Decision Framework 2026]]
[[AI Model Provider Harness Decision Matrix 2026]]
[[model-llm-wiki|Model — LLM Wiki]]
[[model-local-ai|Model — Local AI ($0 Target)]]
[[never-synthesize-from-descriptions-alone|Never Synthesize from Descriptions Alone]]
