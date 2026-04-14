---
title: "Synthesis — HRM and TRM: Tiny Recursive Models Beat LLMs on ARC-AGI"
type: source-synthesis
domain: ai-models
status: synthesized
confidence: high
maturity: seed
created: 2026-04-14
updated: 2026-04-14
sources:
  - id: hrm-trm-youtube-transcript
    type: youtube-transcript
    url: "https://www.youtube.com/watch?v=ZgwHaI2C-9s"
tags:
  - ai-models
  - small-models
  - recursive-reasoning
  - arc-agi
  - hrm
  - trm
  - hierarchical-reasoning
  - tiny-recursion
  - model-efficiency
  - overfitting
  - mlp-vs-attention
  - parameter-count
  - logical-reasoning
  - benchmark
  - scaling-hypothesis
---

# Synthesis — HRM and TRM: Tiny Recursive Models Beat LLMs on ARC-AGI

## Summary

HRM (Hierarchical Reasoning Model, 27M parameters) and TRM (Tiny Recursion Model, 7M parameters) are purpose-built recursive models that outperform multi-billion parameter LLMs on the ARC-AGI benchmark by replacing parameter count with iterative refinement. HRM scored 32% on ARC-AGI beating Claude 4 Opus and GPT-5 mini; TRM pushed to 40% on ARC-AGI-1 and 6.2% on ARC-AGI-2, ahead of Gemini 2.5 Pro and O3 Pro High. The core architectural insight is that recursion — repeatedly polishing an internal answer state — substitutes for scale when the problem domain is bounded and rule-based, and that **decreasing layers while increasing recursion depth improves performance**, the inverse of the LLM scaling hypothesis.

## Key Insights

1. **Recursion replaces parameter count for bounded logical tasks.** Both HRM and TRM solve ARC-AGI not by storing pattern-match knowledge in billions of weights, but by iteratively refining an internal state until a confidence threshold is met. This proves that hard logical problems are not exclusively an LLM domain.

2. **HRM: two-timescale networks (fast + slow) form a hierarchical loop.** A fast low-level network tweaks a hidden scratchpad on every microstep; a slow high-level network resets the scratchpad and makes a strategic correction after several fast passes. A halting head on the slow network decides when to stop. Training assumes the fast loop reaches equilibrium (steady state) before computing gradients — a shortcut that reduces memory but introduces potentially incorrect gradient estimates.

3. **HRM's biological justification was heuristic, not mechanistic.** The paper compared HRM's representational dimensionality to a mouse cortex and cited multi-timescale cortical processing to motivate the two-network design. Researchers found this similarity was purely observational (latent space organization looks similar) with no mechanistic or empirical proof. The hierarchical interpretation of what HRM does internally is also unproven — the model may be doing something with more than two levels of latent features.

4. **TRM: cleaner functional separation, no equilibrium assumption.** TRM (by researcher Alexia) strips HRM's biological framing and instead justifies two states on purely functional grounds: a scratchpad (working thinking space) and an answer placeholder. Collapsing them into one causes interference; adding more states destabilizes learning on small data. TRM trains on the loop it actually runs — it never pretends equilibrium exists; it unrolls a fixed number of steps and back-propagates through real outputs, not hypothetical stable states.

5. **DECREASING layers + INCREASING recursion improves performance — the inverse of LLM scaling.** On TRM's ablations: 4-layer TRM achieves 79.5% on their task set; 2-layer TRM achieves 87.4%. Adding depth causes overfitting when training data is scarce. Fewer parameters make memorization harder and generalization easier; recursion then handles the computational depth that extra layers would have provided in a single forward pass.

6. **Attention vs. MLP tradeoff depends on grid size / context length.** For small grids (9×9 Sudoku), MLP-only TRM outperforms attention-based TRM because MLP generalizes better when context is short. For large grids (30×30 ARC-AGI mazes), attention-based TRM wins because self-attention handles long-range spatial dependencies more efficiently. This is a direct tradeoff: MLP = flexibility and generalization at small context; attention = capacity at large context.

7. **Why small models can win on narrow, data-scarce tasks.** The ARC-AGI training set is deliberately small (to prevent LLMs from memorizing it). Large models overfit small datasets easily. A 7M model with a recursive loop has too few parameters to memorize patterns, so it must learn the underlying rule — exactly what ARC-AGI tests. Recursion turns a single-step inference into a sequence of reusable edits, each light-weight, with no need for a large feed-forward recall store.

8. **These models are not general-purpose LLMs.** HRM and TRM cannot generate text, reason about language, or perform tasks outside ARC-AGI-style visual pattern matching. They compete on the benchmark by working within its highly restrictive, clearly defined rule-based domain. Comparing them to GPT-5 or Claude on general tasks is a category error — the benchmark score is meaningful for narrow logical problem-solving capability only.

9. **TRM performance numbers.** 40% on ARC-AGI-1 (beats Gemini 2.5 Pro, O3 Pro High; slightly below GPT-5 Medium). 6.2% on ARC-AGI-2. HRM: 32% on ARC-AGI-1, 2% on ARC-AGI-2. Both scores achieved with no language understanding, no chain-of-thought prompt, no system prompt engineering — purely architectural recursion.

## Deep Analysis

### The Problem HRM and TRM Solve

Modern LLMs allocate equal compute to every output token regardless of difficulty. Predicting a space character and predicting the final digit of a multi-step arithmetic problem cost the same number of forward-pass FLOPs. This is architecturally wasteful for tasks where reasoning depth varies across positions. HRM and TRM address this by making compute allocation adaptive through recursion: easy positions converge fast, hard positions keep iterating.

### HRM Architecture — Two-Timescale Recurrence

HRM operates with a pair of networks running at different update frequencies:

- **Fast (low-level) network:** runs every microstep, takes the current input and the current provisional answer, and makes a small adjustment to a hidden latent state (the scratchpad).
- **Slow (high-level) network:** wakes up after several fast microsteps, resets the scratchpad, and makes a larger strategic steering correction. It also hosts a **halting head** that decides whether to stop iterating.

This alternation continues — fast refines details, slow sets direction — until the halting head fires. At that point the final answer is read from the provisional answer state.

**Training shortcut (and its cost):** Rather than back-propagating through every microstep (expensive), HRM waits for the fast loop to reach a "stable state" and then computes gradients as if stability already existed. This is computationally efficient and fits the two-timescale biological narrative, but the loop rarely actually settles in the finite number of steps used at runtime — meaning the training gradients may systematically misestimate the true gradient of the unrolled loop. Results proved robust in practice, but the theoretical guarantee is weak.

**Biological framing:** The paper draws a correspondence between HRM's multi-timescale design and multi-timescale cortical processing in the mouse brain, going so far as to include a brain correspondence section comparing representational dimensionality. Critics note this is purely observational — the latent space of HRM happens to look organized similarly to a mouse cortex, but there is no mechanistic evidence the two systems compute in the same way. The hierarchical label is also an interpretation: HRM may actually have more than two levels of latent abstraction operating internally.

### TRM Architecture — Scratchpad + Answer Placeholder

TRM simplifies HRM's design to a clear functional duality without any biological metaphor:

- **Scratchpad state:** the working memory for iterative thinking
- **Answer placeholder state:** a running draft of the output

These two states must stay separate because merging them causes the thinking process to corrupt the answer buffer, and adding more states degrades learning stability on small datasets (empirically confirmed in ablations). The update rule is: run several scratchpad updates (micro-iterations), then apply the result to the answer placeholder (macro-iteration), and repeat.

**No equilibrium assumption:** TRM back-propagates through the loop it actually ran. It runs a fixed number of update steps, reads the actual output from the last real pass, and computes exact gradients. This eliminates the theoretical weakness of HRM's training shortcut at the cost of slightly more memory — acceptable at 7M parameters.

### The Inverse Scaling Finding

The most counterintuitive empirical result from TRM: performance increases when you decrease depth and increase recursion:

| Model variant | Layers | Recursion | Task accuracy |
|---|---|---|---|
| TRM-deep | 4 | standard | 79.5% |
| TRM-shallow | 2 | increased | 87.4% |

This directly contradicts the LLM scaling hypothesis, which holds that more layers → more representational power → better generalization. The explanation: on small training sets (ARC-AGI has ~400 training tasks), more parameters = more opportunity to memorize rather than learn the rule. A two-layer model has so few parameters that it cannot overfit — it must generalize. Recursive depth then substitutes for the missing representational capacity, but in a compute-efficient way that does not increase the parameter count.

### Attention vs. MLP at Different Context Scales

TRM's ablations reveal a context-length-dependent tradeoff:

- **9×9 Sudoku (small context):** MLP-only TRM > attention TRM. MLP learns flexible, generalizable transformations that work well when all relevant information fits in a short context.
- **30×30 ARC-AGI grids or mazes (large context):** Attention TRM > MLP TRM. Self-attention efficiently routes information across long spatial sequences that MLP cannot index into globally.

This suggests an architectural design principle for recursive small models: choose the mixing mechanism based on the expected context length of the target task, not as a blanket choice.

### Implications for the AI Paradigm

HRM and TRM do not invalidate LLM scaling for general intelligence tasks. They do prove something specific and important:

1. **Hard logical problems in bounded domains are not exclusively solvable by scale.** For any task where the rules are well-defined, the search space is constrained, and training data is limited, recursive small models may outperform generalist giants.

2. **The recursion-vs-parameter tradeoff is real and task-dependent.** When data is plentiful and tasks diverse, more parameters generalize better. When data is scarce and the task is narrow, fewer parameters plus more recursion generalize better.

3. **Specialized models for specialized domains is a viable alternative to one-model-for-everything.** The ARC-AGI result suggests a future ecosystem where domain-specific recursive models handle bounded reasoning tasks at a fraction of the inference cost of LLMs.

4. **Training data scarcity as an architectural constraint.** HRM and TRM were designed for ARC-AGI, which is intentionally small to prevent memorization. This constraint shaped the entire architectural philosophy: resist overfitting through minimal parameters, achieve depth through recursion. Other domains with scarce rule-based training data may benefit from the same approach.

### Limitations and Open Questions

- Both models are task-specific: trained for ARC-AGI-style grid pattern matching, incapable of language understanding or cross-domain generalization.
- TRM's 6.2% on ARC-AGI-2 (the harder benchmark) vs. 40% on ARC-AGI-1 shows that increased problem complexity still exposes limits.
- The ceiling of recursive models on more complex logical domains (formal proofs, planning problems, constraint satisfaction at scale) is unknown.
- Combining recursive reasoning with language understanding (hybrid architectures) has not been demonstrated.
- The halting mechanism in HRM (when to stop iterating) needs robustness research — early stopping on hard problems could degrade performance silently.

## Open Questions

- Can recursive architectures be extended to language tasks without losing the overfitting resistance that makes them work on ARC-AGI?
- What is the theoretical ceiling of TRM-style recursion on ARC-AGI-2 and beyond?
- Does the MLP-vs-attention context length finding generalize to other grid-based or graph-based reasoning tasks?
- Is there a hybrid architecture that combines TRM-style recursion with an LLM's semantic understanding for tasks that require both?
- How does the performance scale as training data increases — does the small model advantage disappear when data is abundant?
- Can the halting mechanism be made more principled than a learned head (e.g., convergence criteria on the answer state delta)?

## Relationships

- RELATES TO: [[model-local-ai|Model — Local AI ($0 Target)]] — recursive small models are a candidate for local inference at near-zero cost; 7M parameters runs on any CPU
- RELATES TO: [[deterministic-shell-llm-core|Deterministic Shell, LLM Core]] — TRM embodies this pattern: the recursion loop is the deterministic shell, the tiny network is the core; bounded problem + small model architecture
- RELATES TO: [[src-llm-architecture-gallery-raschka|LLM Architecture Gallery]] — contrasting architecture direction: gallery covers scaling trends (MoE, MLA, hybrid) while TRM/HRM show anti-scaling for bounded tasks
- RELATES TO: [[src-autobe-compiler-verified-backend-generation|AutoBE]] — same theme: bounded problem domain + constrained model enables results that generalist LLMs miss; compiler verification ~ recursive convergence as correctness gate
- RELATES TO: [[model-quality-failure-prevention|Model — Quality and Failure Prevention]] — iterative refinement with a halting condition is a quality assurance mechanism; recursion as built-in review loop
- FEEDS INTO: [[local-llm-quantization|Local LLM Quantization]] — 7M-parameter models are trivially quantizable; recursive models offer a new dimension (recursion depth) beyond quantization for quality-vs-cost tradeoffs

## Source Notes

The primary source is a YouTube explainer video (transcript) covering both the original HRM paper and the follow-up TRM paper by researcher Alexia. The video explicitly distinguishes between empirical results (well-documented, numbers sourced from the papers) and theoretical justifications (the biological correspondence in HRM, the equilibrium assumption in training) where the research community has raised valid criticisms. Confidence is rated high for the architectural descriptions and benchmark numbers; medium for the forward-looking implications, which are the video author's interpretation rather than paper claims.

The ARC-AGI benchmark context matters: scores are not comparable to LLM general capability. A 40% ARC-AGI score from a 7M-parameter grid model and a 40% ARC-AGI score from a trillion-parameter LLM represent entirely different capability profiles — one is a specialist winning its home turf, the other is a generalist unexpectedly failing at a narrow task.

## Backlinks

[[model-local-ai|Model — Local AI ($0 Target)]]
[[deterministic-shell-llm-core|Deterministic Shell, LLM Core]]
[[LLM Architecture Gallery]]
[[AutoBE]]
[[model-quality-failure-prevention|Model — Quality and Failure Prevention]]
[[local-llm-quantization|Local LLM Quantization]]
