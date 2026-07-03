---
title: "Learning Path — RLM Thread Evidence Chain (Session Arc 2026-04-27)"
aliases:
  - "RLM Thread Learning Path"
  - "Learning Path — RLM"
  - "Learning Path — Recursive Language Models Thread"
type: learning-path
domain: cross-domain
layer: spine
status: synthesized
confidence: high
maturity: seed
created: 2026-04-27
updated: 2026-04-27
last_reviewed: 2026-04-27
sources:
  - id: session-handoff
    type: wiki
    file: wiki/log/2026-04-27-session-handoff-rlm-thread-complete-evidence-chain-t-0-mission.md
    description: "The 2026-04-27 session handoff that produced this thread"
  - id: rlm-paper-deep-dive
    type: wiki
    file: wiki/sources/tools-integration/src-rlm-paper-deep-dive-table-1-training-recipe-six-observations.md
    description: "Anchor artifact — the RLM paper PDF deep-dive"
  - id: tier-0-comparison
    type: wiki
    file: wiki/comparisons/rlm-qwen3-8b-vs-qwen3-6-27b-tier-0-long-context-candidate.md
    description: "Anchor artifact — the actionable mission comparison"
tags: [learning-path, spine, rlm, recursive-language-models, evidence-chain, session-arc, mission-2026-04-27, post-anthropic-stack, tier-0-candidate, anti-vendor-lock-in, navigation, curated-reading]
---

# Learning Path — RLM Thread Evidence Chain (Session Arc 2026-04-27)

## Summary

Curated reading order for the **16 wiki artifacts** produced during the 2026-04-27 session arc (initially 11 in Session 1; **expanded to 16 in Session 2 / continuation session** with the RLM-Qwen3.6-27B fine-tune operations plan + Layer-1 paper deep-dives for all 4 RLM Table 1 benchmarks per [continuation session-end handoff](../../log/2026-04-27-continuation-session-end-handoff-rlm-table-1-100pct-layer-1.md)), which built the complete open-source post-Anthropic AI stack evidence chain around Recursive Language Models (RLMs). Designed for a reader who wants to internalize the thread efficiently — whether arriving fresh tomorrow, picking up the operator's mission-execution work, or auditing the wiki's coverage of a specific layer (theory · SDK · training · benchmarks at full Layer 1 · decision · executable operations plan). The path begins with the SHORTEST high-leverage read (the session handoff) and progressively drills into specific layers based on the reader's goal. **Five goals are now supported**: (Goal A) understand the paradigm in 30 minutes; (Goal B) make the tier-0 candidate decision; (Goal C) reproduce the RLM-Qwen3-8B training recipe — or execute the RLM-Qwen3.6-27B fine-tune via the actionable operations plan; (Goal D) full path for thorough internalization; (Goal E NEW) audit the evaluation layer at full Layer 1 / paper-PDF depth across all 4 RLM Table 1 benchmarks. Each goal has a specific subsequence. Total reading time for the full path: **~5-6 hours of focused reading**; minimum-viable path is ~30 minutes.

## Prerequisites

> [!info] Before starting this path
>
> | Prerequisite | Why |
> |---|---|
> | Familiarity with the wiki's [4 governing principles](../../lessons/04_principles/hypothesis/) | The RLM thread maps directly to Principle 1 (Infrastructure>Instructions), Principle 2 (Structured Context), Principle 3 (Goldilocks), Principle 4 (Declarations Aspirational) at every layer |
> | Read [super-model.md](../super-model/super-model.md) | The system topology — situates the RLM thread within the wiki's broader 16-model architecture |
> | Optional: skim the [2026-04-24 brain refactor handoff](../../log/2026-04-24-session-handoff-brain-refactor-rules-and-hooks.md) | Provides context for the regather pattern + hook-layer enforcement that this session validated |
> | Optional: skim the AICP authoritative state at `~/devops-expert-local-ai/docs/SESSION-2026-04-24-HANDOFF.md` | Compute-side mission status; the wiki side documents the candidates, AICP-side deploys them |

## Sequence

### Goal A — Understand the Paradigm (30 minutes)

For a reader who wants the headline insight + structural framing without all the depth.

> [!abstract] Path A: Paradigm in 30 Minutes
>
> | # | Read | Why | Rough time |
> |---|---|---|---|
> | 1 | [Session handoff](../../log/2026-04-27-session-handoff-rlm-thread-complete-evidence-chain-t-0-mission.md) | One-page state-of-the-thread; verbatim operator directives; full artifact list | 5 min |
> | 2 | [RLM empirical findings](../../sources/tools-integration/src-rlm-empirical-findings-oolong-browsecomp-rlm-qwen3-8b.md) Summary + Key Insights only | The unbelievable headline numbers (114% improvement, 91.3% on 10M+ tokens, RLM-Qwen3-8B approaches GPT-5 at 8B params) | 10 min |
> | 3 | [Tier-0 candidate comparison](../../comparisons/rlm-qwen3-8b-vs-qwen3-6-27b-tier-0-long-context-candidate.md) Comparison Matrix only | The actionable side-by-side decision matrix | 10 min |
> | 4 | Skim 1 of: [RLM implementation](../../sources/tools-integration/src-rlm-recursive-language-models-mit-oasys.md) OR [paper deep-dive](../../sources/tools-integration/src-rlm-paper-deep-dive-table-1-training-recipe-six-observations.md) | Pick implementation if you want SDK/architecture, paper if you want benchmark numbers | 5 min skim |
>
> **Outcome**: you can articulate (a) what RLM is, (b) why the wiki cares, (c) what the operator's tier-0 decision looks like.

### Goal B — Make the Tier-0 Candidate Decision (1.5 hours)

For an operator (or fleet PM) deciding which tier-0 candidate to deploy for the post-Anthropic mission.

> [!abstract] Path B: Decision-Maker Sequence
>
> | # | Read | Focus on |
> |---|---|---|
> | 1 | [Session handoff](../../log/2026-04-27-session-handoff-rlm-thread-complete-evidence-chain-t-0-mission.md) | Mission state at T-0 EOD |
> | 2 | [Tier-0 candidate comparison](../../comparisons/rlm-qwen3-8b-vs-qwen3-6-27b-tier-0-long-context-candidate.md) | The full deep-analysis section, especially the 3 paths (Pragmatic / Maximalist / Composition) |
> | 3 | [src-qwen3-6-27b-dense-beats-397b-moe-agentic-coding](../../sources/tools-integration/src-qwen3-6-27b-dense-beats-397b-moe-agentic-coding.md) | Qwen3.6-27B's strengths on agentic coding |
> | 4 | [src-qwen3-6-27b-2-bit-26-tool-calls-unsloth-discussion](../../sources/tools-integration/src-qwen3-6-27b-2-bit-26-tool-calls-unsloth-discussion.md) | Quantization details for tier-0 hardware fit |
> | 5 | [RLM empirical findings](../../sources/tools-integration/src-rlm-empirical-findings-oolong-browsecomp-rlm-qwen3-8b.md) | RLM side empirical claims |
> | 6 | [RLM paper deep-dive](../../sources/tools-integration/src-rlm-paper-deep-dive-table-1-training-recipe-six-observations.md) Table 1 + Six Observations | Per-task numbers, hardware floor, training cost |
> | 7 | [2026 Consumer Hardware AI Stack](../references/2026-consumer-hardware-ai-stack.md) | Spine context — where these candidates fit in the broader hardware decision |
> | 8 | AICP-side `~/devops-expert-local-ai/docs/SESSION-2026-04-24-HANDOFF.md` | Authoritative current state of operator's hardware + smart-routing finding |
>
> **Outcome**: you can pick (a) Qwen3.6-27B alone, (b) RLM-Qwen3-8B alone, (c) both with context-length routing, or (d) future RLM-Qwen3.6-27B fine-tune — with empirical evidence for each.

### Goal C — Reproduce the RLM-Qwen3-8B Training Recipe / Execute the RLM-Qwen3.6-27B Fine-Tune (3-4 hours)

For an engineer who wants to actually train an RLM-native model on operator hardware or cloud GPU. **Updated 2026-04-27 continuation session**: Path C now has all 4 evaluation benchmarks at Layer-1 / full PDF depth + the actionable [RLM-Qwen3.6-27B operations plan](../../domains/cross-domain/rlm-qwen3-6-27b-fine-tune-operations-plan.md) as the actionable artifact (was hypothetical → now executable per Principle 4).

> [!abstract] Path C: Training-Reproducer Sequence (with executable operations plan)
>
> | # | Read | Focus on |
> |---|---|---|
> | 1 | [RLM paper deep-dive](../../sources/tools-integration/src-rlm-paper-deep-dive-table-1-training-recipe-six-observations.md) Section "RLM-Qwen3-8B — The Training Recipe in Detail" | The 6-step recipe (sampling → filtering → SFT decomposition → programmatic correction → fine-tune → evaluate) |
> | 2 | [src-prime-intellect-prime-rl](../../sources/tools-integration/src-prime-intellect-prime-rl-async-rl-training-at-scale.md) | The training framework — async RL, FSDP2 + vLLM, hardware support, 5 basic + 5 advanced examples |
> | 3 | [src-prime-intellect-verifiers](../../sources/tools-integration/src-prime-intellect-verifiers-llm-rl-environments.md) | The environment library — RLMEnv, ToolEnv, the prime CLI lifecycle |
> | 4 | [src-rlm-recursive-language-models-mit-oasys](../../sources/tools-integration/src-rlm-recursive-language-models-mit-oasys.md) | The runtime SDK — pip install rlms, REPL semantics, 5 backends, 6 environments, broker pattern for cloud sandboxes |
> | 5 | [src-longbench-pro-paper-deep-dive](../../sources/tools-integration/src-longbench-pro-paper-deep-dive-1500-samples-46-models-three-findings.md) **(NEW Layer 1 — replaces combined synth)** | Training data source — 1500 bilingual samples (English split = 750 tasks); IIE-CAS + Xiaohongshu lineage; Hugging Face dataset URL `caskcsg/LongBench-Pro` confirmed accessible |
> | 6 | [src-oolong-paper-deep-dive](../../sources/tools-integration/src-oolong-paper-deep-dive-synth-real-leaderboard-cmu-frontier-fails-128k.md) **(NEW Layer 1)** | Evaluation surface — CMU/LTI; 2-split design (synth + real); DeepSeek-R1 below-random pathology forensically explained; reasoning-effort × context-length counter-intuition |
> | 7 | [src-browsecomp-plus-paper-deep-dive](../../sources/tools-integration/src-browsecomp-plus-paper-deep-dive-fixed-corpus-table-1-oracle-citation-quality.md) **(NEW Layer 1)** | Evaluation surface — UWaterloo IR group; oracle 93.49% finding; +14 abs pts retriever-swap finding (Qwen3-Embedding-8B vs BM25); citation quality matrix; API cost analysis |
> | 8 | [src-longbench-v2-paper-deep-dive](../../sources/tools-integration/src-longbench-v2-paper-deep-dive-503-samples-17-models-o1-preview-beats-humans.md) **(NEW Layer 1)** | Evaluation surface — Tsinghua + Zhipu.AI; CodeQA = Code Repo QA subtask (50 entries × 167K median); o1-preview-beats-humans-by-4-pts canonical thinking-paradigm case; RAG saturates at 32K |
> | 9 | [Tier-0 candidate comparison](../../comparisons/rlm-qwen3-8b-vs-qwen3-6-27b-tier-0-long-context-candidate.md) Hypothetical RLM-Qwen3.6-27B section | The composition path — apply the recipe to 27B base, ~$300-500 USD cloud rental estimate |
> | 10 | **[RLM-Qwen3.6-27B Operations Plan](../../domains/cross-domain/rlm-qwen3-6-27b-fine-tune-operations-plan.md) (NEW — actionable artifact)** | The 8-step deterministic operations plan: Acquire base + data → Stand up infra → Generate trajectories → Filter + decompose → Fine-tune → Evaluate on 4 RLM Table 1 benchmarks → Contribute results back → (Optional) AICP deploy. Each step has Action / Expected output / Validation / Rollback. Cost-math: ~$300-500 USD cloud GPU rental. |
>
> **Outcome**: you can specify the data source, the training framework, the runtime SDK, the evaluation suite, the budget, AND have a deterministic operations plan to execute. **The plan is no longer aspirational — it's executable per Principle 4 (Declarations Aspirational Until Infrastructure Verifies Them)**.

### Goal E — Audit the Evaluation Layer at Full Layer 1 / Paper-PDF Depth (1-2 hours, NEW 2026-04-27 continuation)

For a reader auditing the wiki's anti-vendor-lock-in claim at the evaluation layer specifically (e.g., third-party reviewer, AICP routing benchmark designer, mission-claim auditor). All 4 RLM Table 1 benchmarks now grounded at Layer 1 / full PDF as of 2026-04-27 continuation session.

> [!abstract] Path E: Evaluation-Layer-Auditor Sequence (Layer 1 / full PDF across 4 benchmarks)
>
> | # | Read | Why |
> |---|---|---|
> | 1 | [[anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence\|Anti-vendor-lock-in lesson]] Evidence 6 | The mission claim being audited — 4 public benchmarks define the task class, all at Layer 1 |
> | 2 | [src-browsecomp-plus-paper-deep-dive](../../sources/tools-integration/src-browsecomp-plus-paper-deep-dive-fixed-corpus-table-1-oracle-citation-quality.md) | UWaterloo IR group; 100,195 docs / 830 queries; 14-annotator × 400+-hour construction; oracle 93.49%; +14 abs pts retriever finding |
> | 3 | [src-longbench-pro-paper-deep-dive](../../sources/tools-integration/src-longbench-pro-paper-deep-dive-1500-samples-46-models-three-findings.md) | IIE-CAS + UCAS + Beihang + Xiaohongshu; 1500 bilingual; 11×25 task taxonomy; 3 findings empirically grounded; 100K CNY construction cost |
> | 4 | [src-oolong-paper-deep-dive](../../sources/tools-integration/src-oolong-paper-deep-dive-synth-real-leaderboard-cmu-frontier-fails-128k.md) | CMU LTI; 2-split design (synth + real); 9-model leaderboard; DeepSeek-R1 below-random pathology |
> | 5 | [src-longbench-v2-paper-deep-dive](../../sources/tools-integration/src-longbench-v2-paper-deep-dive-503-samples-17-models-o1-preview-beats-humans.md) | Tsinghua + Zhipu.AI; 503 multi-choice × 6×20 taxonomy; 17-model leaderboard; o1-preview = 57.7% > 53.7% human; RAG saturates at 32K |
>
> **Outcome**: you can independently audit the wiki's anti-vendor-lock-in claim at the evaluation layer; verify reproducibility of each benchmark; identify per-benchmark methodology strengths + limitations; design benchmark-driven AICP routing decisions on Layer-1-grounded foundations. **Distinct authorial provenance across 4 independent academic groups (Tsinghua + Zhipu / IIE-CAS + Xiaohongshu / CMU LTI / UWaterloo + CSIRO + CMU + UQueensland)** validates that the evaluation infrastructure is itself anti-vendor-lock-in — not concentrated in any single research lab.

### Full Path — All 16 Artifacts in Origin Order (5-6 hours)

For thorough internalization of the entire session arc.

> [!info] Path D: Complete Sequence (origin order, 16 artifacts spanning Session 1 + Session 2 / continuation)
>
> | # | Read | Type | Session |
> |---|---|---|---|
> | 1 | [2026-04-25 regather log](../../log/2026-04-25-regather-systemic-bug-investigation-and-second-p4-instance.md) | Session investigation — the regather + 2nd P4 instance found in spine | S1 |
> | 2 | [src-rlm-recursive-language-models-mit-oasys](../../sources/tools-integration/src-rlm-recursive-language-models-mit-oasys.md) | Source-synthesis (implementation) | S1 |
> | 3 | [src-rlm-empirical-findings](../../sources/tools-integration/src-rlm-empirical-findings-oolong-browsecomp-rlm-qwen3-8b.md) | Source-synthesis (blogpost-level findings) | S1 |
> | 4 | [src-rlm-paper-deep-dive](../../sources/tools-integration/src-rlm-paper-deep-dive-table-1-training-recipe-six-observations.md) | Source-synthesis (paper-level deep-dive) | S1 |
> | 5 | [src-prime-intellect-verifiers](../../sources/tools-integration/src-prime-intellect-verifiers-llm-rl-environments.md) | Source-synthesis (environment library) | S1 |
> | 6 | [src-prime-intellect-prime-rl](../../sources/tools-integration/src-prime-intellect-prime-rl-async-rl-training-at-scale.md) | Source-synthesis (training framework) | S1 |
> | 7 | [Tier-0 candidate comparison](../../comparisons/rlm-qwen3-8b-vs-qwen3-6-27b-tier-0-long-context-candidate.md) | Comparison (decision matrix) | S1 |
> | 8 | [src-oolong-and-longbench-pro](../../sources/tools-integration/src-oolong-and-longbench-pro-long-context-benchmarks-rlm-anchors.md) | Source-synthesis (eval + training-data benchmarks, abstract level) | S1 |
> | 9 | [src-browsecomp-plus-and-longbench-v2](../../sources/tools-integration/src-browsecomp-plus-and-longbench-v2-rlm-table-1-benchmarks.md) | Source-synthesis (remaining Table 1 benchmarks, abstract level) | S1 |
> | 10 | [2026-04-27 mid-session handoff](../../log/2026-04-27-session-handoff-rlm-thread-complete-evidence-chain-t-0-mission.md) | Session handoff (mid-session state capture) | S1 |
> | 11 | [self-reference-drift lesson Evidence 6 edit](../../lessons/03_validated/methodology-process/self-reference-drift-wiki-must-practice-its-own-teachings.md) | Lesson edit — positive evidence the brain refactor's enforcement works | S1 |
> | 12 | [[anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence\|Anti-vendor-lock-in lesson]] | Layer-4 evolved-knowledge distillation — mission-claim verification specializes Principle 4 | S1 |
> | 13 | [2026-04-27 session-end handoff (#14)](../../log/2026-04-27-session-end-handoff-13-artifacts-rlm-thread-saturation.md) | Session 1 close — 13-artifact arc reaches natural saturation | S1 |
> | 14 | **[RLM-Qwen3.6-27B Operations Plan](../../domains/cross-domain/rlm-qwen3-6-27b-fine-tune-operations-plan.md)** | Operations plan (NEW S2) — 8-step deterministic plan; closes the composition-path-aspirational from Tier-0 comparison | S2 |
> | 15 | [src-browsecomp-plus-paper-deep-dive](../../sources/tools-integration/src-browsecomp-plus-paper-deep-dive-fixed-corpus-table-1-oracle-citation-quality.md) | Layer 1 deep-dive (NEW S2) — UWaterloo IR group; oracle 93.49%; +14 abs pts retriever finding | S2 |
> | 16 | [src-longbench-pro-paper-deep-dive](../../sources/tools-integration/src-longbench-pro-paper-deep-dive-1500-samples-46-models-three-findings.md) | Layer 1 deep-dive (NEW S2) — IIE-CAS + Xiaohongshu; 1500 bilingual; 3 findings | S2 |
> | 17 | [src-oolong-paper-deep-dive](../../sources/tools-integration/src-oolong-paper-deep-dive-synth-real-leaderboard-cmu-frontier-fails-128k.md) | Layer 1 deep-dive (NEW S2) — CMU LTI; 2-split design; DeepSeek-R1 below-random pathology | S2 |
> | 18 | [src-longbench-v2-paper-deep-dive](../../sources/tools-integration/src-longbench-v2-paper-deep-dive-503-samples-17-models-o1-preview-beats-humans.md) | Layer 1 deep-dive (NEW S2) — Tsinghua + Zhipu.AI; o1-preview-beats-humans-by-4-pts | S2 |
> | 19 | [[anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence\|Anti-vendor-lock-in lesson Evidence 6 enrichment]] | Lesson edit (NEW S2) — Evidence 6 enriched with 4-of-4 Layer-1 grounding | S2 |
> | 20 | [2026-04-27 continuation session-end handoff](../../log/2026-04-27-continuation-session-end-handoff-rlm-table-1-100pct-layer-1.md) | Session 2 close — 5-artifact continuation arc; RLM Table 1 100% at Layer 1 | S2 |
>
> **Note**: numbered 1-20 reflects all artifacts touched (created or edited) across S1 + S2; the headline count "16 artifacts" refers to NEW artifacts (excluding edits to existing artifacts which are #11, #19). S1 = Session 1 (early 2026-04-27); S2 = Session 2 / continuation (post-compact 2026-04-27).

## Outcomes

> [!success] By the end of this path you will know
>
> 1. **What RLM is**: a paradigm replacing `llm.completion(prompt)` with `rlm.completion(prompt)` where the LM operates on its input as a Python REPL variable, with recursive sub-LM calls — extending effective context by 2 orders of magnitude
> 2. **The empirical evidence chain at full Layer 1 depth**: from the 4 RLM Table 1 benchmarks (CodeQA · BrowseComp+ · OOLONG · OOLONG-Pairs) ALL grounded at full PDF / Layer 1 depth as of 2026-04-27 continuation session, to the headline numbers (RLM(GPT-5) beats base GPT-5 on 4/4 tasks; RLM-Qwen3-8B at 8B params approaches GPT-5 on 3/4 long-context tasks; o1-preview beats humans on LongBench v2 by +4 pts)
> 3. **The open-source training stack**: alexzhang13/rlm SDK (Apache 2.0) + PrimeIntellect/verifiers (RLMEnv) + PrimeIntellect/prime-rl (Apache 2.0, 48 H100 hours for RLM-Qwen3-8B) + Qwen3-Embedding-8B (retriever, +14 abs pts vs BM25 per BrowseComp+ deep-dive) + 4 public benchmarks at Layer 1
> 4. **The tier-0 decision**: Qwen3.6-27B (available now, dense, agentic-coding-strong) vs RLM-Qwen3-8B (8B + recursion, long-context-strong, may need self-training) vs both routed by context length vs **future RLM-Qwen3.6-27B fine-tune (now executable per the [operations plan](../../domains/cross-domain/rlm-qwen3-6-27b-fine-tune-operations-plan.md))**
> 5. **The mission alignment, fully grounded**: every layer of the post-Anthropic stack has direct paper evidence in the wiki — anti-vendor-lock-in is empirically traceable end-to-end at Layer 1 (per the [[anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence|anti-vendor-lock-in lesson Evidence 6]])
> 6. **The brain refactor's enforcement state across 3 cycles**: empirically validated for tool-call discipline cumulatively across S1 + S2 sessions — pre-bash hook caught 5+ reflexive truncations across the continuation session arc alone (Cycle 3 of Evidence 6 validation in the self-reference-drift lesson); reasoning-layer compliance remains the open frontier
> 7. **The evaluation-layer authorial diversity**: the 4 RLM Table 1 benchmarks come from **4 independent academic groups** (Tsinghua + Zhipu / IIE-CAS + UCAS + Beihang + Xiaohongshu / CMU LTI / UWaterloo + CSIRO + CMU + UQueensland) — anti-vendor-lock-in NOT just at the model layer; the evaluation infrastructure itself is provenance-distributed

## How to Apply This Path

> [!tip] Pick your goal first, then path:
>
> - **Decision-maker today** → Path A (30 min) → Path B if you need to decide
> - **Engineer planning a training run** → Path A first to ground, then Path C
> - **Wiki maintainer auditing coverage** → Path D for completeness
> - **Operator picking up tomorrow's mission-execution work** → Path A + the AICP-side handoff at `~/devops-expert-local-ai/docs/SESSION-2026-04-24-HANDOFF.md`

> [!warning] What this path does NOT teach
>
> - **Operational deployment** of the candidates — that's compute-side, AICP-repo work
> - **Specific Hugging Face checkpoint names** — RLM-Qwen3-8B release status was unverified at synthesis time
> - **Hardware compatibility on RTX 2080 Ti** — Turing architecture; flash-attn3 / BF16 may need fallback paths (LoRA + INT8 most likely viable)
> - **Production observability** — wiki-side documents the stack; production telemetry is operator-side

## Open Questions

> [!question] Should this path be the canonical entry point for new RLM-thread readers?
> The wiki's [methodology-fundamentals](methodology-fundamentals.md) is the canonical 30-page learning path for the wiki itself. This new path is much smaller (11 artifacts, ~3-4 hours) and topic-specific. Worth promoting as a featured navigational entry? (Requires: operator decision on spine-level promotion.)

> [!question] How will this path stay current as the RLM thread evolves?
> If the operator self-trains RLM-Qwen3-8B, runs benchmarks, deploys to AICP, etc. — there will be follow-on artifacts. Should this path auto-extend or be replaced by a successor? (Requires: convention decision; possibly an `evolution` page tracks updates.)

> [!question] Do other research threads in the wiki deserve similar curated paths?
> Existing threads include: brain refactor (2026-04-24), Qwen3.6-27B ingestion (2026-04-25 prior), AI infrastructure decision framework (2026-04-23). Each could have a learning-path. Or this could be a one-off for the most-recent thread. (Requires: judgment on path-page proliferation vs navigation utility.)

### How This Connects — Navigate From Here

> [!abstract] From This Learning Path → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **The session that produced this thread** | [[2026-04-27-session-handoff-rlm-thread-complete-evidence-chain-t-0-mission\|2026-04-27 Session Handoff]] |
> | **The actionable mission decision** | [[rlm-qwen3-8b-vs-qwen3-6-27b-tier-0-long-context-candidate\|Tier-0 Candidate Comparison]] |
> | **The empirical evidence anchor** | [[src-rlm-paper-deep-dive-table-1-training-recipe-six-observations\|RLM Paper Deep Dive]] |
> | **The wiki's broader learning path system** | [[methodology-fundamentals\|Methodology Fundamentals Learning Path]] |
> | **The 4 principles the thread validates** | [[infrastructure-over-instructions-for-process-enforcement\|P1]] · [[structured-context-governs-agent-behavior-more-than-content\|P2]] · [[right-process-for-right-context-the-goldilocks-imperative\|P3]] · [[declarations-are-aspirational-until-infrastructure-verifies-them\|P4]] |
> | **The lesson the thread validates** | [[self-reference-drift-wiki-must-practice-its-own-teachings\|Self-Reference Drift]] (Evidence 6) |
> | **The spine reference candidates feed into** | [[2026-consumer-hardware-ai-stack\|2026 Consumer Hardware AI Stack]] · [[ai-infrastructure-decision-framework-2026\|AI Infrastructure Decision Framework 2026]] · [[ai-model-provider-harness-decision-matrix-2026\|AI Model Provider Harness Decision Matrix 2026]] |

## Relationships

- BUILDS ON: [[2026-04-27-session-handoff-rlm-thread-complete-evidence-chain-t-0-mission|2026-04-27 Mid-Session Handoff (S1)]]
- BUILDS ON: [[2026-04-27-session-end-handoff-13-artifacts-rlm-thread-saturation|2026-04-27 Session-End Handoff #14 (S1 close)]]
- BUILDS ON: [[2026-04-27-continuation-session-end-handoff-rlm-table-1-100pct-layer-1|2026-04-27 Continuation Session-End Handoff (S2 close)]]
- BUILDS ON: [[rlm-qwen3-8b-vs-qwen3-6-27b-tier-0-long-context-candidate|Tier-0 Candidate Comparison]]
- BUILDS ON: [[src-rlm-paper-deep-dive-table-1-training-recipe-six-observations|RLM Paper Deep Dive]]
- BUILDS ON: [[rlm-qwen3-6-27b-fine-tune-operations-plan|RLM-Qwen3.6-27B Operations Plan]] (S2 — actionable artifact for Path C)
- BUILDS ON: [[src-browsecomp-plus-paper-deep-dive-fixed-corpus-table-1-oracle-citation-quality|BrowseComp+ Paper Deep Dive]] (S2 — Layer 1 evaluation surface)
- BUILDS ON: [[src-longbench-pro-paper-deep-dive-1500-samples-46-models-three-findings|LongBench Pro Paper Deep Dive]] (S2 — Layer 1 training-data source)
- BUILDS ON: [[src-oolong-paper-deep-dive-synth-real-leaderboard-cmu-frontier-fails-128k|OOLONG Paper Deep Dive]] (S2 — Layer 1 evaluation surface)
- BUILDS ON: [[src-longbench-v2-paper-deep-dive-503-samples-17-models-o1-preview-beats-humans|LongBench v2 Paper Deep Dive]] (S2 — Layer 1 evaluation surface)
- BUILDS ON: [[anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence|Anti-Vendor-Lock-In Lesson]] (the mission claim Path E audits)
- RELATES TO: [[methodology-fundamentals|Methodology Fundamentals Learning Path]]
- RELATES TO: [[self-reference-drift-wiki-must-practice-its-own-teachings|Self-Reference Drift]]
- RELATES TO: [[super-model|Super-Model — Research Wiki as Ecosystem Intelligence Hub]]
- FEEDS INTO: [[2026-consumer-hardware-ai-stack|2026 Consumer Hardware AI Stack]]
- FEEDS INTO: [[ai-infrastructure-decision-framework-2026|AI Infrastructure Decision Framework 2026]]

## Backlinks

[[2026-04-27 Mid-Session Handoff (S1)]]
[[2026-04-27 Session-End Handoff #14 (S1 close)]]
[[2026-04-27 Continuation Session-End Handoff (S2 close)]]
[[Tier-0 Candidate Comparison]]
[[src-rlm-paper-deep-dive-table-1-training-recipe-six-observations|RLM Paper Deep Dive]]
[[rlm-qwen3-6-27b-fine-tune-operations-plan|RLM-Qwen3.6-27B Operations Plan]]
[[BrowseComp+ Paper Deep Dive]]
[[src-longbench-pro-paper-deep-dive-1500-samples-46-models-three-findings|LongBench Pro Paper Deep Dive]]
[[src-oolong-paper-deep-dive-synth-real-leaderboard-cmu-frontier-fails-128k|OOLONG Paper Deep Dive]]
[[src-longbench-v2-paper-deep-dive-503-samples-17-models-o1-preview-beats-humans|LongBench v2 Paper Deep Dive]]
[[Anti-Vendor-Lock-In Lesson]]
[[Methodology Fundamentals Learning Path]]
[[self-reference-drift-wiki-must-practice-its-own-teachings|Self-Reference Drift]]
[[super-model|Super-Model — Research Wiki as Ecosystem Intelligence Hub]]
[[2026 Consumer Hardware AI Stack]]
[[ai-infrastructure-decision-framework-2026|AI Infrastructure Decision Framework 2026]]
