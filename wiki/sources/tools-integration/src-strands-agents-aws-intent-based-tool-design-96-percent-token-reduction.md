---
title: "Synthesis — Strands Agents (AWS): Intent-Based Tool Design Cuts Token Usage 96% (52K → 2K) via Narrow Scope + Semantic-Search MCP Gateway"
aliases:
  - "Strands Agents Synthesis"
  - "AWS Strands Intent-Based Tools"
  - "Strands 96% Token Reduction"
type: source-synthesis
domain: tools-integration
status: synthesized
confidence: high
maturity: seed
layer: 1
created: 2026-05-04
updated: 2026-05-04
last_reviewed: 2026-05-04
sources:
  - id: thenewstack-article
    type: article
    url: https://thenewstack.io/strands-agents-tool-design/
    file: raw/articles/cut-ai-token-usage-by-96-here039s-how-aws-strands-agents-does-it-the-new-stack.md
    description: "The New Stack 2026-04-29 — AWS dev advocate Morgan Willis demonstrates 3 iterations of accounting-API tool design: API-endpoint tools (52K tokens) → intent-based tools (2K) → remote MCP server + semantic-search gateway (~1K). 14M+ Strands downloads in <1 year."
  - id: strands-framework
    type: documentation
    url: https://strandsagents.com/
    description: "Strands Agents — open-source agentic framework from AWS"
tags: [synthesis, strands, aws, agentic-framework, intent-based-tools, mcp, semantic-search, token-efficiency, tool-design, narrow-scope, agent-cardinality, mission-2026-05-04]
---

# Synthesis — Strands Agents (AWS): Intent-Based Tool Design Cuts Token Usage 96% (52K → 2K)

## Summary

The New Stack interview 2026-04-29 with AWS developer advocate Morgan Willis demonstrates a three-iteration optimization on the same accounting-API task ("look up the latest invoice for a customer"): (1) **API-endpoint-mapped tools** — 5 chained API calls × 52,000 tokens (default mapping every endpoint to a tool); (2) **intent-based tools** — 1 tool call × 2,000 tokens (tools that wrap multi-API outcomes into a single intent); (3) **remote MCP server + semantic-search tool catalog** — agent receives only relevant tools per query, cutting token usage roughly in half again. **Net: 96% token reduction by intent-design + selective tool exposure**. The principle Willis names: *"the fewer tools that you expose to your agent, the less likely it is to call the wrong one"* and *"agents that are more narrowly defined tend to perform better than general use case agents"*. Strands Agents has 14M+ downloads in under a year. The architectural pattern — many narrowly-scoped agents, each with a small intent-aligned tool set, served via MCP gateways with semantic search — is the **input-boundary intelligence-layer pattern** the operator's [Custom-Tailored Senior-Engineer-Tier Model Group Concept](../../domains/cross-domain/custom-tailored-senior-engineer-tier-model-group-with-recreated-intelligence-layer-research-synthesis.md) M003 names directly.

## Reference

> [!info] Source identity
>
> | Field | Value |
> |---|---|
> | **Article** | "Cut AI token usage by 96%? Here's how AWS Strands Agents does it." (The New Stack, 2026-04-29) |
> | **Authors** | Frederic Lardinois (interviewer) · Morgan Willis (AWS developer advocate, demo) |
> | **Framework** | [Strands Agents](https://strandsagents.com/) — open-source agentic framework |
> | **Maturity** | 14M+ downloads in <1 year (released ~2025-05) |
> | **License** | Open source (Apache 2.0 per AWS pattern) |
> | **Sponsor disclosure** | AWS-sponsored post on The New Stack |

## Key Insights

> [!success] **Token efficiency is fundamentally a tool-design problem, not a model-size problem.**
>
> The same task with the same Strands framework on the same model varies from **52,000 tokens → 2,000 tokens (96% reduction) by changing how tools are designed.** Iteration 1 (API-endpoint mapping): the agent must reason through 5 chained API calls (find customer → list invoices → filter latest → fetch details → format). Iteration 2 (intent-based): one `get_latest_invoice(customer)` tool internally calls the 5 endpoints; the agent makes one call. The 26× reduction comes from removing the agent's reasoning burden over data-shape composition. This validates the operator's *"recreated intelligence layer at I/O boundaries"* framing: tool design IS the intelligence layer at the input boundary; offloading data-composition work from the agent into well-named intent tools is structurally equivalent to operator's *"intelligence at the layers needed. in and out"*.

> [!success] **Selective tool exposure (semantic search over tool catalog) cuts another ~50%.**
>
> Iteration 3 moves tools to a remote MCP server via [AWS Agent Core Gateway](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-core.html) with semantic search. Instead of loading the full 16-tool catalog, the agent receives only the tools relevant to each query. This cuts token usage roughly in half compared to loading everything. **The principle**: *"As MCP servers proliferate and tool catalogs grow, the question of which tools an agent actually sees on a given run is going to matter as much as the tools themselves."* This is the input-boundary routing layer — operator's M003 (Recreated Intelligence Layer) names it directly.

> [!success] **Narrow agents > general agents (Willis's stated principle).**
>
> *"I think agents that are more narrowly defined tend to perform better than general use case agents. If you're looking for context efficiency, speed, and accuracy, I would also look at your agent design as well."* This is the agent-cardinality principle: many narrow agents > one general agent. The operator's [Custom-Tailored Model Group Concept](../../domains/cross-domain/custom-tailored-senior-engineer-tier-model-group-with-recreated-intelligence-layer-research-synthesis.md) Mixture-of-LoRAs across senior-engineer task surfaces (coding · methodology-reasoning · validation-checking · refactor-planning · debug-analysis) is the same architectural insight applied to the model layer rather than the agent layer.

> [!info] **The 96% reduction is paper-evidence-grade for the input-boundary intelligence layer.**
>
> Operator's *"recreate intelligence at the layers needed. in and out"* now has measured grounding: 52K → 2K tokens via intent-based tool design + ~1K via semantic-search gateway = ~98% from end-to-end. This is comparable in scale to the trust-layer's 80–90% space-saved composition math (Caveman + UD-IQ2 + KV-cache + cypher overlay). The intelligence-layer compression and the trust-layer compression compose.

## Deep Analysis

### The Three Iterations (concrete numbers)

| Iteration | Tool design | API calls | Tokens | Token reduction |
|---|---|---|---|---|
| 1 | API-endpoint mapping (1:1 with each endpoint) | 5 chained | ~52,000 | baseline |
| 2 | Intent-based tools (`get_latest_invoice(customer)` wraps all 5) | 1 | ~2,000 | **96.2%** |
| 3 | Remote MCP server with semantic search across 16-tool catalog (only relevant tools sent per query) | 1 | ~1,000 | **~98%** |

The key insight is that the model is NOT the variable — same model, same task, different tool design produces 50× difference. This is the input-boundary intelligence layer governing model behavior more than the model itself.

### Connection to Spec-Driven Convergence

Per [[spec-driven-agentic-build-is-the-2026-convergent-pattern-prompts-are-first-class-artifacts|Spec-Driven Agentic Build Convergence Lesson]]: structured artifacts authored before any code make AI output predictable. Strands Agents extends this insight from *spec artifacts* to *tool artifacts*: tools are first-class artifacts the agent reads at every invocation, and their design (intent-named vs endpoint-mapped) is the difference between predictable execution and combinatorial reasoning explosion.

### Connection to Custom-Model Mission (operator-relevant)

The operator's [Custom-Tailored Senior-Engineer-Tier Model Group](../../domains/cross-domain/custom-tailored-senior-engineer-tier-model-group-with-recreated-intelligence-layer-research-synthesis.md) M003 (Recreated Intelligence Layer at I/O Boundaries) names exactly this pattern. Strands provides a paper-evidence anchor for the *input boundary* slice: routing + selective tool exposure + intent-based tool wrapping. Mixture-of-LoRAs at the model level + Strands-style intent-based tool design at the I/O boundary = compounding compression across both axes.

### MCP Gateway as the Substitutable Substrate

The semantic-search gateway pattern is **vendor-neutral**: the same pattern works with [AWS Agent Core Gateway](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-core.html), [Strands](https://strandsagents.com/), [LangGraph](https://langchain-ai.github.io/langgraph/), [LlamaIndex](https://docs.llamaindex.ai/), or operator-built. Per the Anti-Vendor-Lock-In mission, this is one more substitutable component within the (candidate) model-customization layer's intelligence-layer dimension.

## Quotes (verbatim from Willis interview)

> *"It's calling multiple API's, but rolling them up into one intent-based tool for the agent that it's going to have a better time using — and understanding when exactly to use it."*

> *"The fewer tools that you expose to your agent, the less likely it is to call the wrong one."*

> *"Your agent is going to have a better time reasoning around what tool to use and when, because these tools are more aligned to a task and less aligned to data."*

> *"I think agents that are more narrowly defined tend to perform better than general use case agents. If you're looking for context efficiency, speed, and accuracy, I would also look at your agent design as well."*

> *"As MCP servers proliferate and tool catalogs grow, the question of which tools an agent actually sees on a given run is going to matter as much as the tools themselves."*

## Open Questions

> [!question] What's the empirical limit on intent-based-tool composition for a senior-engineer-tier model group?
> Strands' worked example is a 5-endpoint accounting API. Senior-engineer-tier workloads (coding · methodology-reasoning · refactor-planning) involve much larger tool catalogs (LSP · Git · package managers · test runners · CI · static analyzers). Empirical scaling test is the next step.

> [!question] Can semantic-search-over-tool-catalog be operator-authored without AWS Agent Core Gateway?
> Likely yes — the pattern is vendor-neutral. Operator-authored Python middleware on top of an MCP server with embeddings-based tool selection achieves the same architecture. Substitutability holds.

> [!question] Does the 96% token reduction hold at higher complexity (multi-step reasoning over many domains)?
> Strands' example is a single intent. For multi-step workflows (debug-analyze → propose-fix → verify-test → commit-and-push), the saving may be lower per step but compounds across steps. Empirical validation would close this gap.

## Relationships

- BUILDS ON: [[custom-tailored-senior-engineer-tier-model-group-with-recreated-intelligence-layer-research-synthesis|Custom-Tailored Senior-Engineer-Tier Model Group Concept]] — provides paper evidence for the input-boundary intelligence layer (M003)
- BUILDS ON: [[spec-driven-agentic-build-is-the-2026-convergent-pattern-prompts-are-first-class-artifacts|Spec-Driven Convergence Lesson]] — extends the structured-artifacts insight from specs to tools
- RELATES TO: [[anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence|Anti-Vendor-Lock-In Lesson]] — Strands is one of multiple agentic-framework substitutes (LangGraph · LlamaIndex · operator-built); substitutability holds
- RELATES TO: [[secure-tamper-proof-model-on-shared-gpu-research-synthesis|Trust-Layer Concept]] — input-boundary compression composes with trust-layer compression
- DEMONSTRATES: [[infrastructure-over-instructions-for-process-enforcement|Principle 1 — Infrastructure Over Instructions]] — intent-based tools are infrastructure (the tool wraps the multi-step composition); endpoint-mapped tools are instructions to the agent
- DEMONSTRATES: [[structured-context-governs-agent-behavior-more-than-content|Principle 2 — Structured Context Governs Agent Behavior]] — well-named intent tools program agent behavior more reliably than ad-hoc reasoning over endpoint maps

## Backlinks

[[Custom-Tailored Senior-Engineer-Tier Model Group Concept]]
[[Spec-Driven Convergence Lesson]]
[[Anti-Vendor-Lock-In Lesson]]
[[Trust-Layer Concept]]
[[infrastructure-over-instructions-for-process-enforcement|Principle 1 — Infrastructure Over Instructions]]
[[structured-context-governs-agent-behavior-more-than-content|Principle 2 — Structured Context Governs Agent Behavior]]
