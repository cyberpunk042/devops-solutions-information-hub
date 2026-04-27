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

Curated reading order for the 11 wiki artifacts produced during the 2026-04-27 session arc, which built the complete open-source post-Anthropic AI stack evidence chain around Recursive Language Models (RLMs). Designed for a reader who wants to internalize the thread efficiently — whether arriving fresh tomorrow, picking up the operator's mission-execution work, or auditing the wiki's coverage of a specific layer (theory · SDK · training · benchmarks · decision). The path begins with the SHORTEST high-leverage read (the session handoff) and progressively drills into specific layers based on the reader's goal. **Three goals are supported**: (Goal A) understand the paradigm in 30 minutes; (Goal B) make the tier-0 candidate decision; (Goal C) reproduce the RLM-Qwen3-8B training recipe on operator's hardware. Each goal has a specific subsequence. Total reading time for the full path: ~3-4 hours of focused reading; minimum-viable path is ~30 minutes.

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

### Goal C — Reproduce the RLM-Qwen3-8B Training Recipe (3+ hours)

For an engineer who wants to actually train an RLM-native model on operator hardware or cloud GPU.

> [!abstract] Path C: Training-Reproducer Sequence
>
> | # | Read | Focus on |
> |---|---|---|
> | 1 | [RLM paper deep-dive](../../sources/tools-integration/src-rlm-paper-deep-dive-table-1-training-recipe-six-observations.md) Section "RLM-Qwen3-8B — The Training Recipe in Detail" | The 6-step recipe (sampling → filtering → SFT decomposition → programmatic correction → fine-tune → evaluate) |
> | 2 | [src-prime-intellect-prime-rl](../../sources/tools-integration/src-prime-intellect-prime-rl-async-rl-training-at-scale.md) | The training framework — async RL, FSDP2 + vLLM, hardware support, 5 basic + 5 advanced examples |
> | 3 | [src-prime-intellect-verifiers](../../sources/tools-integration/src-prime-intellect-verifiers-llm-rl-environments.md) | The environment library — RLMEnv, ToolEnv, the prime CLI lifecycle |
> | 4 | [src-rlm-recursive-language-models-mit-oasys](../../sources/tools-integration/src-rlm-recursive-language-models-mit-oasys.md) | The runtime SDK — pip install rlms, REPL semantics, 5 backends, 6 environments, broker pattern for cloud sandboxes |
> | 5 | [src-oolong-and-longbench-pro](../../sources/tools-integration/src-oolong-and-longbench-pro-long-context-benchmarks-rlm-anchors.md) | Training-data source (LongBench Pro) + evaluation surface (OOLONG) anchored to original papers |
> | 6 | [src-browsecomp-plus-and-longbench-v2](../../sources/tools-integration/src-browsecomp-plus-and-longbench-v2-rlm-table-1-benchmarks.md) | Two more evaluation surfaces (CodeQA + BrowseComp+) — completes Table 1 coverage |
> | 7 | [Tier-0 candidate comparison](../../comparisons/rlm-qwen3-8b-vs-qwen3-6-27b-tier-0-long-context-candidate.md) Hypothetical RLM-Qwen3.6-27B section | The composition path — apply the recipe to 27B base, ~$300-500 USD cloud rental estimate |
>
> **Outcome**: you can specify the data source, the training framework, the runtime SDK, the evaluation suite, and the budget for replicating (or scaling) the RLM-Qwen3-8B training.

### Full Path — All 11 Artifacts in Origin Order (3-4 hours)

For thorough internalization of the entire session arc.

> [!info] Path D: Complete Sequence (origin order)
>
> | # | Read | Type |
> |---|---|---|
> | 1 | [2026-04-25 regather log](../../log/2026-04-25-regather-systemic-bug-investigation-and-second-p4-instance.md) | Session investigation — the regather + 2nd P4 instance found in spine |
> | 2 | [src-rlm-recursive-language-models-mit-oasys](../../sources/tools-integration/src-rlm-recursive-language-models-mit-oasys.md) | Source-synthesis (implementation) |
> | 3 | [src-rlm-empirical-findings](../../sources/tools-integration/src-rlm-empirical-findings-oolong-browsecomp-rlm-qwen3-8b.md) | Source-synthesis (blogpost-level findings) |
> | 4 | [src-rlm-paper-deep-dive](../../sources/tools-integration/src-rlm-paper-deep-dive-table-1-training-recipe-six-observations.md) | Source-synthesis (paper-level deep-dive) |
> | 5 | [src-prime-intellect-verifiers](../../sources/tools-integration/src-prime-intellect-verifiers-llm-rl-environments.md) | Source-synthesis (environment library) |
> | 6 | [src-prime-intellect-prime-rl](../../sources/tools-integration/src-prime-intellect-prime-rl-async-rl-training-at-scale.md) | Source-synthesis (training framework) |
> | 7 | [Tier-0 candidate comparison](../../comparisons/rlm-qwen3-8b-vs-qwen3-6-27b-tier-0-long-context-candidate.md) | Comparison (decision matrix) |
> | 8 | [src-oolong-and-longbench-pro](../../sources/tools-integration/src-oolong-and-longbench-pro-long-context-benchmarks-rlm-anchors.md) | Source-synthesis (eval + training-data benchmarks) |
> | 9 | [src-browsecomp-plus-and-longbench-v2](../../sources/tools-integration/src-browsecomp-plus-and-longbench-v2-rlm-table-1-benchmarks.md) | Source-synthesis (remaining Table 1 benchmarks) |
> | 10 | [2026-04-27 session handoff](../../log/2026-04-27-session-handoff-rlm-thread-complete-evidence-chain-t-0-mission.md) | Session handoff (complete state capture) |
> | 11 | [self-reference-drift lesson](../../lessons/03_validated/methodology-process/self-reference-drift-wiki-must-practice-its-own-teachings.md) Evidence 6 | Lesson edit — positive evidence the brain refactor's enforcement works |

## Outcomes

> [!success] By the end of this path you will know
>
> 1. **What RLM is**: a paradigm replacing `llm.completion(prompt)` with `rlm.completion(prompt)` where the LM operates on its input as a Python REPL variable, with recursive sub-LM calls — extending effective context by 2 orders of magnitude
> 2. **The empirical evidence chain**: from the 4 RLM Table 1 benchmarks (CodeQA · BrowseComp+ · OOLONG · OOLONG-Pairs) to the headline numbers (RLM(GPT-5) beats base GPT-5 on 4/4 tasks; RLM-Qwen3-8B at 8B params approaches GPT-5 on 3/4 long-context tasks)
> 3. **The open-source training stack**: alexzhang13/rlm SDK (Apache 2.0) + PrimeIntellect/verifiers (RLMEnv) + PrimeIntellect/prime-rl (Apache 2.0, 48 H100 hours for RLM-Qwen3-8B) + Qwen3-Embedding-8B (retriever) + 4 public benchmarks
> 4. **The tier-0 decision**: Qwen3.6-27B (available now, dense, agentic-coding-strong) vs RLM-Qwen3-8B (8B + recursion, long-context-strong, may need self-training) vs both routed by context length vs hypothetical RLM-Qwen3.6-27B fine-tune
> 5. **The mission alignment**: every layer of the post-Anthropic stack has direct paper evidence in the wiki — anti-vendor-lock-in is empirically traceable end-to-end
> 6. **The brain refactor's enforcement state**: empirically validated for tool-call discipline this very session (pre-bash hook caught reflexive truncation); reasoning-layer compliance remains the open frontier

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

- BUILDS ON: [[2026-04-27-session-handoff-rlm-thread-complete-evidence-chain-t-0-mission|2026-04-27 Session Handoff]]
- BUILDS ON: [[rlm-qwen3-8b-vs-qwen3-6-27b-tier-0-long-context-candidate|Tier-0 Candidate Comparison]]
- BUILDS ON: [[src-rlm-paper-deep-dive-table-1-training-recipe-six-observations|RLM Paper Deep Dive]]
- RELATES TO: [[methodology-fundamentals|Methodology Fundamentals Learning Path]]
- RELATES TO: [[self-reference-drift-wiki-must-practice-its-own-teachings|Self-Reference Drift]]
- RELATES TO: [[super-model|Super-Model — Research Wiki as Ecosystem Intelligence Hub]]
- FEEDS INTO: [[2026-consumer-hardware-ai-stack|2026 Consumer Hardware AI Stack]]
- FEEDS INTO: [[ai-infrastructure-decision-framework-2026|AI Infrastructure Decision Framework 2026]]

## Backlinks

[[2026-04-27 Session Handoff]]
[[Tier-0 Candidate Comparison]]
[[src-rlm-paper-deep-dive-table-1-training-recipe-six-observations|RLM Paper Deep Dive]]
[[Methodology Fundamentals Learning Path]]
[[self-reference-drift-wiki-must-practice-its-own-teachings|Self-Reference Drift]]
[[super-model|Super-Model — Research Wiki as Ecosystem Intelligence Hub]]
[[2026 Consumer Hardware AI Stack]]
[[ai-infrastructure-decision-framework-2026|AI Infrastructure Decision Framework 2026]]
