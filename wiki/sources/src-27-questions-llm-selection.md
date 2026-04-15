---
title: "Source — 27 Questions to Ask Before Choosing an LLM"
type: source-synthesis
domain: ai-models
status: synthesized
confidence: high
maturity: seed
created: 2026-04-14
updated: 2026-04-14
sources:
  - id: infoworld-27-questions-llm-2024
    type: article
    url: https://www.infoworld.com/article/4152738/27-questions-to-ask-before-choosing-an-llm.html
    author: Peter Wayner
    outlet: InfoWorld
tags:
  - llm-selection
  - evaluation-framework
  - ai-models
  - decision-criteria
  - local-ai
  - compliance
  - cost-optimization
  - performance
---

# Source — 27 Questions to Ask Before Choosing an LLM

## Summary

A structured, 27-question evaluation framework across six categories for selecting language models: performance and technical specs, capabilities and features, licensing and availability, cost and environment, legal and compliance, and implementation considerations. Directly applicable to the Local AI model selection decisions and any LLM procurement in the devops ecosystem.

The framework's core thesis is that "not every application requires the same support" — comprehensive evaluation prevents mismatches between model selection and operational requirements. The questions force explicit tradeoffs rather than defaulting to the most prominent or cheapest option.

## Key Insights

1. **The framework is structured in decision order.** Performance and capability questions come first because they are disqualifying — a model that does not fit the hardware or lacks required media types can be eliminated before evaluating cost or compliance.

2. **Legal questions are often skipped and carry existential risk.** Training data provenance, copyright in the training set, indemnification guarantees, and third-party audit availability are overlooked in most informal evaluations but represent real organizational liability. At minimum, Q20–Q24 should be checked for any production deployment.

3. **The cost/environment category bundles sustainability with TCO.** Pricing model evaluation (Q17) cannot be decoupled from environmental impact (Q18) and renewable energy sourcing (Q19) for organizations with sustainability commitments. This linkage is underappreciated.

4. **Agentic feature evaluation (Q13) is a first-class concern now.** Multi-model coordination and reasoning capabilities were minor considerations two years ago; in an agent-first architecture like the devops ecosystem, they are primary selection criteria alongside raw performance.

5. **Knowledge cutoff date (Q8) is a latent failure mode for local models.** When running quantized models locally, the cutoff governs what facts are embedded. Without RAG or retrieval augmentation, a model with a 2023 cutoff running in 2026 gives silent stale answers with no confidence signal.

6. **Human-in-the-loop support (Q26) is an architectural prerequisite.** For any operation touching production systems, confirming the model supports oversight callbacks and interrupts is non-negotiable. Models optimized for batch autonomy may not support graceful interrupt patterns.

7. **Model quirks (Q27) cannot be evaluated from benchmarks.** Distinctive behavioral patterns — hallucination tendencies, refusal patterns, verbosity biases, format preferences — only surface through direct testing on representative prompts. This is the single question that requires empirical validation rather than documentation review.

## Deep Analysis

### Framework Structure and Decision Logic

The 27 questions are organized so that early answers constrain or eliminate later questions. If a model fails hardware compatibility (Q2), questions 6–27 are moot. If the model is not open source (Q14) and the use case requires weight access for fine-tuning (Q9), that is a two-question disqualification. This implicit dependency structure makes the framework more efficient than its length suggests.

The flow mirrors a standard procurement gate:
1. Technical feasibility (Q1–Q5) — "Can we run this?"
2. Capability fit (Q6–Q13) — "Does it do what we need?"
3. Supply chain (Q14–Q16) — "Is it available long-term?"
4. Total cost of ownership (Q17–Q19) — "Can we afford the full bill?"
5. Legal standing (Q20–Q25) — "Can we deploy without liability?"
6. Operational characteristics (Q26–Q27) — "Does it behave well in production?"

### Category 1 — Performance and Technical Specs

**Model Size (Q1):** Parameter count is a rough proxy for encoded knowledge capacity. It does not directly predict performance on any specific task; a 7B model fine-tuned on domain data often outperforms a 70B general model on narrow tasks. In the local AI context, parameter count also determines minimum VRAM — a hard constraint before any other evaluation.

**Hardware Compatibility (Q2):** Beyond raw VRAM, quantization format compatibility, CUDA compute level, and inference runtime support all factor in. A model that requires BF16 precision cannot run on consumer NVIDIA cards that lack BF16 hardware support.

**Time to First Token (Q3):** Critical for interactive use cases. Agentic pipelines where the model runs as a background process can tolerate high TTFT; human-facing tools cannot. The wiki's Local AI routing framework uses this as a tiebreaker between otherwise equivalent models.

**Rate Limits (Q4):** Cloud provider rate limits constrain agentic pipelines that fan out to parallel model calls. Local models have no external rate limits but are bounded by hardware throughput. This is the question that determines whether local inference is viable for a given workload.

**Context Window Size (Q5):** The hard constraint for codebase analysis, long-document synthesis, and multi-turn agent tasks. 128K context is now common; 1M context (Gemini 1.5 Pro) is available. For the wiki pipeline, context window size determines whether full files can be processed in a single call or must be chunked.

### Category 2 — Capabilities and Features

**Reasoning vs. Speed Balance (Q6):** Extended thinking / chain-of-thought models (Claude Sonnet 3.7, o3) trade latency for quality on complex reasoning tasks. Routing decisions in the Local AI model must account for whether a task requires iterative reasoning or fast pattern matching — and price accordingly.

**Model Stability (Q7):** Quantified as the tendency to produce coherent, non-divergent outputs over long contexts. Heavily quantized models (2-bit, 3-bit) exhibit higher instability on long completions. This is task-type dependent; Q7 pairs with Q27 (model quirks) to form a complete behavioral assessment.

**Knowledge Cutoff (Q8):** Training data recency. For local models without internet access, this is fixed and decays over time. The wiki itself partially compensates for cutoff limitations by exporting synthesized knowledge to CLAUDE.md and structured references — converting embedded model knowledge into retrieval-available knowledge.

**Fine-tuning Support (Q9):** The ability to perform domain-specific training on model weights. Open source models (Llama, Mistral, Gemma) support this natively; most closed API models do not or charge significant premiums. The AICP local inference pipeline must account for whether a model can be adapted to ecosystem-specific terminology.

**Supported Media Types (Q10):** Text is table stakes. For code analysis tasks: structured data (JSON, XML), images (screenshots, diagrams), and PDFs. Multi-modal models add cost and latency; they should only be selected when the use case genuinely requires non-text inputs.

**Prompting Structure (Q11):** Different models respond distinctly to instruction placement, system prompt formats, and few-shot examples. A model that performs well with one prompting style may degrade significantly with another. This is particularly important when migrating prompts between models.

**Tool Use (Q12):** Function calling / tool integration quality varies significantly. For the devops ecosystem's agent chains, reliable, low-hallucination tool use is a hard requirement. Models that frequently confabulate tool calls or ignore tool results are disqualifying for agentic use.

**Agentic Features (Q13):** Multi-model coordination, persistent memory, task decomposition, and reasoning loop support. In a Claude Code + local inference hybrid architecture, the local model need not have full agentic capabilities — it serves as a leaf node executor. But for models designated as orchestrators, Q13 is primary.

### Category 3 — Licensing and Availability

**Open Source Status (Q14):** Governs weight access, modification rights, and deployment freedom. The local AI model explicitly favors open weight models (Llama family, Mistral, Qwen) for local deployment because they carry no per-call cost and support quantization. Licensing varies among open weight models — some prohibit commercial use above a user count threshold.

**Guaranteed Lifespan (Q15):** API-served models deprecate. Cloud providers have deprecated models with as little as 90 days notice, breaking production pipelines. This is the hidden TCO item — migration cost when a model is discontinued. Local models with persistent weights have infinite lifespan as long as the inference runtime remains viable.

**Batch Architecture Support (Q16):** Asynchronous batch APIs (Claude Batch, OpenAI Batch) offer 50% cost reduction for workloads that tolerate latency. The wiki's evolve pipeline — which runs non-interactively — is a natural candidate for batch routing.

### Category 4 — Cost and Environment

**Pricing Model (Q17):** Input tokens, output tokens, and cached tokens are priced differently. For the wiki pipeline's heavy context-reuse pattern, providers with prompt caching discounts (Anthropic: cache writes at 1.25x, cache reads at 0.1x) dramatically outperform flat-rate pricing at scale.

**Environmental Impact (Q18):** Water and electricity consumption per inference call. Frontier models running on non-renewable infrastructure have measurable environmental cost per query. For organizations with sustainability reporting, this is a compliance question, not just an ethical preference.

**Renewable Energy Use (Q19):** Whether the inference infrastructure is powered by renewable sources. Certain cloud regions have significantly higher renewable percentages than others. This is selectable in some providers' routing configurations.

### Category 5 — Legal and Compliance

**Training Data Provenance (Q20):** Whether the training corpus includes synthetic data, permissively licensed data, or potentially unlicensed content. Synthetic data reduces copyright risk but may introduce distributional biases. Providers vary widely in transparency here.

**Copyright in Training Set (Q21):** The live litigation risk area. Multiple ongoing lawsuits (NYT v. OpenAI, Getty v. Stability AI) concern training data copyright. Using a model whose training corpus included pirated or unlicensed content transfers legal exposure to the operator in some jurisdictions.

**Third-Party Audits (Q22):** Independent verification of training data composition and model behavior claims. Rare in the industry but increasingly required for enterprise procurement. SOC2 certification does not cover training data; it only covers infrastructure security.

**Indemnification (Q23):** Whether the provider contractually protects the operator against copyright infringement claims arising from model outputs. Google (Vertex AI) and Microsoft (Azure OpenAI) offer limited indemnification; most providers do not.

**Compliance Requirements (Q24):** SOC2 Type II, HIPAA Business Associate Agreement, GDPR Data Processing Agreement, FedRAMP. Required if the workload processes regulated data. Local models on self-hosted infrastructure bypass most cloud compliance requirements but create a self-certification obligation.

**Geographic Location (Q25):** Physical server location determines applicable data residency regulation (GDPR Art. 44 cross-border transfer restrictions, China's PIPL, Canadian PIPEDA). API calls to US servers from EU origin may require additional legal basis.

### Category 6 — Implementation Considerations

**Human-in-the-Loop (Q26):** Whether the model runtime supports pausing for human confirmation, returning partial results, or graceful interrupt on escalation. Fully autonomous pipelines eliminate this; systems touching production require it. Claude Code implements HITL natively through its approval workflow.

**Model Quirks (Q27):** The behavioral fingerprint that benchmarks do not capture. Examples from production experience: Llama models tend to verbose preambles; GPT-4o tends to affirmative restating; Claude models are reluctant to produce certain output types without explicit prompting; Mistral models are more literal in instruction following. These quirks require direct observation on representative tasks, not documentation review.

### Application to the Devops Ecosystem

The 27 questions map directly to three decision points in the ecosystem:

| Decision | Primary Questions | Notes |
|---|---|---|
| Local vs. cloud routing (AICP) | Q1, Q2, Q4, Q6, Q17 | Hardware fit, latency, cost |
| Model selection for wiki evolution | Q5, Q8, Q9, Q13, Q27 | Context size, recency, tool use, behavior |
| Production agent deployment | Q12, Q13, Q20–Q25, Q26 | Legal, tool use, HITL |

The framework also highlights a gap: the wiki has no systematic evaluation record for models currently in use. Q7 (stability), Q11 (prompting structure), and Q27 (quirks) should be empirically documented for each model in the Local AI model page.

## Open Questions

- Does the ecosystem's AICP deployment currently track model versions against Q15 (guaranteed lifespan) to detect upcoming deprecations?
- Which of Q20–Q25 have been formally evaluated for the current cloud model usage? The wiki has no compliance page covering LLM legal risk.
- For local model candidates (Llama 3, Qwen2.5, Mistral), has Q7 (stability) been benchmarked at production context lengths?
- Should this 27-question framework be formalized as a reusable evaluation template in `wiki/config/templates/`?

## Relationships

- FEEDS INTO: [[model-local-ai|Model — Local AI ($0 Target)]]
- FEEDS INTO: [[local-model-vs-cloud-api-for-routine-operations|Decision — Local Model vs Cloud API for Routine Operations]]
- RELATES TO: [[ai-models-domain-overview|AI Models — Domain Overview]]
- RELATES TO: [[aicp|AICP]]
- RELATES TO: [[local-llm-quantization|Local LLM Quantization]]

## Backlinks

[[model-local-ai|Model — Local AI ($0 Target)]]
[[local-model-vs-cloud-api-for-routine-operations|Decision — Local Model vs Cloud API for Routine Operations]]
[[ai-models-domain-overview|AI Models — Domain Overview]]
[[aicp|AICP]]
[[local-llm-quantization|Local LLM Quantization]]
