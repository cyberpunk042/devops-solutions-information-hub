---
title: "Synthesis — Anthropic — Building Effective AI Agents — 5 Canonical Workflow Patterns"
aliases:
  - "Synthesis — Anthropic — Building Effective AI Agents — 5 Canonical Workflow Patterns"
  - "Synthesis — Anthropic Building Effective AI Agents"
  - "Building Effective AI Agents"
type: source-synthesis
domain: ai-agents
layer: 1
status: synthesized
confidence: authoritative
maturity: growing
created: 2026-04-15
updated: 2026-04-15
sources:
  - id: anthropic-building-effective-agents
    type: article
    url: https://www.anthropic.com/engineering/building-effective-agents
    file: raw/articles/building-effective-ai-agents-anthropic.md
    title: "Building Effective AI Agents"
    authors: "Erik Schluntz, Barry Zhang"
    published: 2024-12-19
    ingested: 2026-04-15
tags: [anthropic, agentic-systems, workflows, agents, prompt-chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer, aci, agent-computer-interface, harness-patterns]
---

# Synthesis — Anthropic — Building Effective AI Agents — 5 Canonical Workflow Patterns

## Summary

Anthropic's Dec 2024 engineering post draws a hard line between **workflows** (LLMs orchestrated through PREDEFINED code paths) and **agents** (LLMs that DYNAMICALLY direct their own processes). Both are agentic systems; the distinction is who controls the path. The post then documents five canonical workflow patterns observed across "dozens of teams building LLM agents across industries": prompt chaining, routing, parallelization, orchestrator-workers, and evaluator-optimizer. The most successful implementations consistently used these simple composable patterns rather than complex frameworks. Three core principles for agent design: (1) maintain simplicity, (2) prioritize transparency by explicitly showing planning steps, (3) carefully craft the agent-computer interface (ACI) through tool documentation and testing. The ACI principle deserves the same engineering investment as HCI. This synthesis captures the patterns, principles, and the workflow-vs-agent distinction — feeds directly into the [[harness-engineering-is-the-dominant-performance-lever|Harness Engineering Is the Dominant Performance Lever]] lesson and updates [[model-claude-code|Model — Claude Code]] with formal workflow taxonomy.

## Source Reference

> [!info] Source card
>
> | Field | Value |
> |-------|-------|
> | Authors | Erik Schluntz, Barry Zhang (Anthropic) |
> | Published | 2024-12-19 |
> | URL | [anthropic.com/engineering/building-effective-agents](https://www.anthropic.com/engineering/building-effective-agents) |
> | Length | ~20KB raw |
> | Type | Engineering blog post |
> | Cited by | Multiple sources in this cluster (NLAH, Meta-Harness, Rethinking AI Agents transcript) all reference these 5 patterns as canonical |

## Key Insights

### 1. Workflows vs Agents — the Architectural Cleavage

The post draws a precise distinction:
- **Workflows:** LLMs and tools orchestrated through PREDEFINED code paths. The path is in the code; the LLM fills in steps.
- **Agents:** LLMs that DYNAMICALLY direct their own processes and tool usage, maintaining control over how they accomplish tasks. The path is in the model; the code provides the tool surface.

Both are agentic systems. The cleavage is *who decides the path*. This maps directly to this wiki's [[methodology-is-a-framework-not-a-fixed-pipeline|Methodology Is a Framework, Not a Fixed Pipeline]] lesson — workflows are the stage-gate side, agents are the dynamic-composition side. Same distinction, different domain.

### 2. Start Simple — Frameworks Are an Optimization, Not a Default

> "We suggest that developers start by using LLM APIs directly: many patterns can be implemented in a few lines of code. If you do use a framework, ensure you understand the underlying code."

Frameworks (Claude Agent SDK, AWS Strands, Rivet, Vellum) help get started but "create extra layers of abstraction that can obscure the underlying prompts and responses, making them harder to debug." This is the **Goldilocks principle applied to agentic infrastructure** — right-sized to the problem, not maximally framework-ized. Aligns with [[right-process-for-right-context-the-goldilocks-imperative|Goldilocks Imperative]].

### 3. The 5 Canonical Workflow Patterns

The taxonomy that the rest of this cluster keeps citing:

| Pattern | Mechanism | When To Use |
|---------|-----------|-------------|
| **Prompt chaining** | Decompose into sequential steps; each LLM call processes prior output. Add programmatic "gates" between steps for on-track checks. | Task cleanly decomposes into fixed subtasks. Trade latency for accuracy. |
| **Routing** | Classify input → direct to specialized followup. Separation of concerns. | Distinct categories handled by different prompts/tools/models. E.g., simple→Haiku, complex→Sonnet. |
| **Parallelization** | (a) **Sectioning** — independent subtasks in parallel; (b) **Voting** — same task multiple times for confidence. | Speed (sectioning) or confidence/diversity (voting). |
| **Orchestrator-workers** | Central LLM dynamically breaks down task, delegates to worker LLMs, synthesizes. | Subtasks NOT predictable in advance (vs parallelization where they are). E.g., coding tasks where N files change. |
| **Evaluator-optimizer** | One LLM generates; another evaluates and provides feedback in a loop. | Clear evaluation criteria + iterative refinement provides measurable value. |

These compose. Real production agents combine multiple patterns. The Anthropic SWE-bench coding agent uses orchestrator-workers internally with evaluator-optimizer loops on test results.

### 4. Agent = Augmented LLM in a Tool-Use Loop

The basic building block underlying all five workflows: an LLM enhanced with augmentations (retrieval, tools, memory). Models actively use these — generating their own search queries, selecting tools, determining what to retain. Two implementation focuses: (a) tailor capabilities to the use case, (b) ensure they provide an easy, well-documented interface for the LLM. MCP is one approach to standardize this.

Agents proper (the dynamic kind) are "typically just LLMs using tools based on environmental feedback in a loop." Crucial design considerations:
- **Ground truth at every step** — tool call results, code execution, etc. — to assess progress
- **Pause for human feedback** at checkpoints or blockers
- **Stopping conditions** (max iterations) to maintain control
- **Higher costs** + **compounding error potential** mean extensive testing in sandboxed environments

### 5. ACI — Agent-Computer Interface as a Discipline

> "One rule of thumb is to think about how much effort goes into human-computer interfaces (HCI), and plan to invest just as much effort in creating good agent-computer interfaces (ACI)."

This is the post's most quotable framing. It elevates tool-design from "documentation chore" to "discipline parallel to HCI." Five principles:

1. **Put yourself in the model's shoes** — is it obvious how to use this tool from description + parameters alone?
2. **Change parameter names/descriptions** to make things obvious
3. **Write great docstrings** as if for a junior developer
4. **Test how the model uses tools** — run examples, see mistakes, iterate
5. **Poka-yoke your tools** — change arguments so mistakes are harder

Concrete example: in the SWE-bench agent, the team spent more time optimizing TOOLS than the overall prompt. They found relative filepaths caused mistakes after the agent moved out of root directory; switched to absolute filepaths and "the model used this method flawlessly."

### 6. Three Core Principles

The post's closing summary distills three principles for any agent implementation:

1. **Maintain simplicity** in agent design
2. **Prioritize transparency** by explicitly showing planning steps
3. **Carefully craft the ACI** through tool documentation and testing

These map directly to this wiki's [[infrastructure-over-instructions-for-process-enforcement|Infrastructure Over Instructions]] principle (transparency = visible planning = enforceability) and [[structured-context-governs-agent-behavior-more-than-content|Structured Context]] principle (ACI = structure of tool descriptions governs tool-use accuracy).

### 7. When NOT to Use Agents

> "When building applications with LLMs, we recommend finding the simplest solution possible, and only increasing complexity when needed. This might mean not building agentic systems at all."

The honest counterweight to all the workflow patterns: many tasks need only **a single LLM call with retrieval and in-context examples**. Workflows offer predictability for well-defined tasks; agents offer flexibility but with cost/latency/error trade-offs. This aligns with the Goldilocks principle and the "minimum viable methodology" answer (Q26 → CLAUDE.md + pipeline post is the minimum, not orchestrator-workers).

### 8. Two Production Domains Where Agents Shine

| Domain | Why Agents Work |
|--------|----------------|
| Customer support | Conversation flow + tool integration + clear success criteria + measurable resolution. Several companies use usage-based pricing — only pay for successful resolutions. |
| Coding agents | Verifiable through automated tests + iterate using test results as feedback + well-defined problem space + objectively measurable output. SWE-bench Verified results. |

The pattern: agents work where the loop has GROUND TRUTH (tests, resolutions). Aligns with [[if-you-can-verify-you-converge|If You Can Verify, You Converge]] — verification turns model differences into retry-count differences, not quality differences.

## Cross-Reference Integration

### Convergent Evidence (strengthens existing pages)

| Existing Page | How This Reinforces It |
|---------------|------------------------|
| [[harness-engineering-is-the-dominant-performance-lever\|Harness Engineering Lesson]] (new draft) | Provides the 5-pattern taxonomy that defines what a harness DOES. Agent = model + harness; this post enumerates the harness side. |
| [[model-claude-code\|Model — Claude Code]] | Anthropic's own framing of agent architecture should be the canonical reference. Adding "5 Canonical Workflow Patterns" section. |
| [[methodology-is-a-framework-not-a-fixed-pipeline\|Methodology Framework]] | Workflows-vs-agents = predefined-vs-dynamic; same distinction the methodology framework draws between stage-gate and dynamic composition. |
| [[if-you-can-verify-you-converge\|If You Can Verify, You Converge]] (draft) | The "ground truth at every step" requirement is the verification mechanism that makes agentic systems converge. |
| [[infrastructure-over-instructions-for-process-enforcement\|Infrastructure Over Instructions]] | ACI as discipline = structured tool design = infrastructure governs agent behavior. |

### Tensions / Notes

- **Frameworks reservation** — Anthropic explicitly warns against frameworks. Our wiki documents Skills/Hooks/MCP as patterns to ADOPT. No contradiction: skills/hooks/MCP are primitives, not frameworks. A "framework" in Anthropic's sense is something like Rivet/Vellum that abstracts the tool-call loop entirely.
- **"Workflow" terminology overload** — Anthropic uses "workflow" for predefined-path patterns. Other sources (LangChain, OpenFleet) use "workflow" for any multi-step agent process. Note in adoption.

## Deep Analysis

### Why the 5-Pattern Taxonomy Endures

The patterns are **structural primitives**, not implementations. Every production agent reduces to compositions of these five. The taxonomy succeeds because:

1. **Mutually exclusive** at the base level — a single LLM call is either chained, routed, parallelized, orchestrated, or evaluated. Composition layers them.
2. **Mechanism-distinguishable** — each pattern has a different "what governs the next call" answer (output-of-prior, classifier-decision, all-at-once, dynamic-orchestrator-decision, evaluator-feedback).
3. **Evidence-grounded** — drawn from "dozens of teams" building production agents, not a theoretical framework.

When Anthropic says "we identified five canonical patterns," NLAH and Meta-Harness papers cite this as the taxonomy. It has become the de-facto vocabulary for harness design.

### The ACI Principle Generalizes

ACI ≠ tool-only. The principle "structure of the interface governs the consumer's behavior" applies to:
- **Frontmatter fields** — agent-readable structure of wiki pages governs ingestion behavior
- **CLAUDE.md / AGENTS.md** — the structure of the context file governs session behavior
- **Skill descriptions** — the ACI for skill triggering
- **Hook configurations** — the ACI for enforcement
- **MCP tool schemas** — the canonical example of ACI

The Three Core Principles + ACI together amount to: **agents are programmed by the interfaces you give them**. This is the same insight as [[structured-context-is-proto-programming-for-ai-agents|Structured Context Is Proto-Programming for AI Agents]].

### Gap — No Quantification

The post is qualitative throughout. "Most successful implementations" — how many? "Higher accuracy" — by how much? The October 2025 follow-up (effective harnesses) and the March 2026 papers (NLAH, Meta-Harness) provide the quantification: 7.7-point improvements, 6× performance variation, etc. This synthesis pairs naturally with [[src-anthropic-effective-harnesses-long-running-agents|the Effective Harnesses synthesis]] and the two arxiv papers.

## Relationships

- RELATES TO: [[model-claude-code|Model — Claude Code]]
- RELATES TO: [[model-skills-commands-hooks|Model — Skills, Commands, and Hooks]]
- FEEDS INTO: [[harness-engineering-is-the-dominant-performance-lever|Lesson — Harness Engineering Is the Dominant Performance Lever]]
- RELATES TO: [[src-anthropic-effective-harnesses-long-running-agents|Synthesis — Effective Harnesses for Long-Running Agents]]
- RELATES TO: [[src-arxiv-natural-language-agent-harnesses|Synthesis — NLAH]]
- RELATES TO: [[src-arxiv-meta-harness-outer-loop-search|Synthesis — Meta-Harness]]
- RELATES TO: [[src-rethinking-ai-agents-harness-engineering-rise|Synthesis — Rethinking AI Agents (YouTube)]]
- BUILDS ON: [[methodology-is-a-framework-not-a-fixed-pipeline|Methodology Is a Framework, Not a Fixed Pipeline]]
- RELATES TO: [[structured-context-is-proto-programming-for-ai-agents|Structured Context Is Proto-Programming]]

## Backlinks

[[model-claude-code|Model — Claude Code]]
[[model-skills-commands-hooks|Model — Skills, Commands, and Hooks]]
[[Lesson — Harness Engineering Is the Dominant Performance Lever]]
[[src-anthropic-effective-harnesses-long-running-agents|Synthesis — Effective Harnesses for Long-Running Agents]]
[[src-arxiv-natural-language-agent-harnesses|Synthesis — NLAH]]
[[src-arxiv-meta-harness-outer-loop-search|Synthesis — Meta-Harness]]
[[Synthesis — Rethinking AI Agents (YouTube)]]
[[methodology-is-a-framework-not-a-fixed-pipeline|Methodology Is a Framework, Not a Fixed Pipeline]]
[[structured-context-is-proto-programming-for-ai-agents|Structured Context Is Proto-Programming]]
[[src-claude-agent-sdk-and-managed-agents|Synthesis — Claude Agent SDK and Managed Agents]]
