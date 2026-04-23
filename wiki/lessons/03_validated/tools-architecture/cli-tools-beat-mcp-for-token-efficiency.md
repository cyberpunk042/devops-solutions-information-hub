---
title: CLI Tools Beat MCP for Token Efficiency
aliases:
  - "CLI Tools Beat MCP for Token Efficiency"
type: lesson
domain: ai-agents
layer: 4
status: synthesized
confidence: high
maturity: growing
derived_from:
  - "Synthesis: Claude Code Accuracy Tips"
  - "Synthesis: Claude Code Harness Engineering"
  - "Claude Code"
  - "MCP Integration Architecture"
created: 2026-04-08
updated: 2026-04-10
last_reviewed: 2026-04-22
sources:
  - id: src-claude-code-accuracy-tips
    type: youtube-transcript
    url: https://www.youtube.com/watch?v=D5bRTv6GhXk
    title: Claude Code Works Better When You Do This
  - id: src-harness-engineering-article
    type: article
    url: https://levelup.gitconnected.com/building-claude-code-with-harness-engineering-d2e8c0da85f0
    title: Building Claude Code with Harness Engineering
  - id: src-playwright-cli-vs-mcp
    type: youtube-transcript
    url: https://www.youtube.com/watch?v=nN5R9DFYsXY
    title: "Claude Code + Playwright CLI: Automate QA with Less Tokens"
tags: [cli, mcp, token-efficiency, skills, context-management, accuracy, tool-integration, agent-design]
---

# CLI Tools Beat MCP for Token Efficiency

## Summary

When integrating external tools into LLM-powered workflows, CLI tools paired with skill files consistently outperform MCP server integrations on token cost and output accuracy. MCP loads all registered tool schemas into the context window at session startup regardless of whether those tools will be used, while skill-based CLI tools inject instructions only when the relevant skill is invoked. The practical result is lower token consumption, fewer hallucinations from schema noise, and better accuracy — a tradeoff confirmed by independent practitioners and converging across multiple sources.

## Context

This lesson applies whenever you are deciding how to expose a capability to a Claude Code agent or any LLM-powered workflow:

- Choosing between building an MCP server vs. a CLI tool + SKILL.md to give Claude access to an external system (databases, APIs, wiki operations, Obsidian, NotebookLM)
- Designing agent architectures where multiple tools compete for context budget
- Debugging unexplained hallucinations or tool-call errors and looking for root causes beyond prompt quality
- Evaluating whether an existing MCP integration is worth its overhead for the frequency it is actually invoked
- Planning the MCP Integration Architecture evolution for the research wiki itself — where the tradeoff between discoverability and context cost is a live architectural decision

The tradeoff is most consequential in long-running sessions, multi-tool setups, and subagent pipelines where context pressure compounds across turns.

## Insight

> [!warning] MCP loads on every message; Skills load on invocation
> MCP registers a server once → all tool schemas appear on every turn. In a multi-server setup, the cumulative schema payload consumes meaningful context budget before any tool is called. Skills contain no schema overhead at rest — they enter context only when invoked, delivering prose-form instructions optimized for the model.

> [!abstract] The loading profile comparison
>
> | Property | MCP Server | CLI + Skill |
> |----------|-----------|-------------|
> | Context cost at rest | Full JSON schema on every message | Zero |
> | Loading trigger | Session start (always) | Invocation (on demand) |
> | Instruction format | JSON-RPC schema (for parser) | Prose markdown (for model) |
> | Best for | Cross-context discoverability | Project-internal tooling |

The accuracy implication compounds: schema tokens from unused tools occupy space that could hold relevant conversation turns or file content. This is context pollution — high-entropy JSON boilerplate displacing higher-signal task context. The Playwright CLI vs. MCP comparison produced a measurable result: CLI was both cheaper AND more accurate.

**2026 practitioner consensus:** Use MCP when tools need cross-context discoverability without setup. Use CLI+Skills when you control the environment and want minimal overhead. For project-internal tooling — CLI+Skills is the default winner.

## Evidence

**Playwright CLI vs. MCP direct comparison (src-claude-code-accuracy-tips):** A former Amazon/Microsoft senior AI engineer building BookZero.AI entirely with Claude Code ran a direct comparison between Playwright's MCP server and its CLI+Skills equivalent. The CLI was cheaper and more accurate. This is the most concrete single data point: same task, two integration modes, measurable difference in both cost and output quality.

**Playwright CLI vs. MCP mechanism video (src-playwright-cli-vs-mcp):** A dedicated comparison video provides the underlying mechanism with precise detail. MCP dumps the full accessibility tree into context after every single navigation step. CLI saves page state to a YAML file on disk and only loads it when Claude explicitly needs to find an element. In a 10-step QA test, MCP injects 10 full accessibility trees into the context window; CLI loads 2-3 targeted YAML snapshots on demand. The referenced "12x cost differential" in the accuracy tips source is substantiated by this mechanism: MCP's per-step context injection compounds across every action, while CLI's lazy-loading eliminates most of that overhead. The video also shows the accuracy trade-off clearly: CLI is more accurate for known-page tests (you know what fields and flows to expect), MCP retains an advantage for exploratory testing or unknown-page bug verification (where forced full-page visibility catches unexpected error states). This is the most mechanistically detailed evidence available.

**Microsoft officially recommends CLI over MCP for Playwright (src-playwright-cli-vs-mcp):** Playwright's creator (Microsoft) now recommends the CLI for AI agent integrations. The CLI also has 3x more features than the Playwright MCP server. This makes the CLI-over-MCP finding asymmetric — CLI wins on cost, accuracy for known tests, AND feature breadth. The tool's creator endorsing CLI over their own MCP server is a strong external validation signal.

**Google Trends signal (src-claude-code-accuracy-tips):** The accuracy tips source notes that Google Trends shows "CLI overtaking MCP" as a search trend in 2026. This is a weak signal individually but meaningful as confirmation that the practitioner community is converging on the same conclusion independently.

**Context loading mechanics (src-claude-code-accuracy-tips):** The source states explicitly: "CLI+Skills loads tool instructions only when relevant (skill loading is contextual), while MCP loads all tool schemas into context at startup." This is the mechanism, not just the observation.

**Harness engineering convergence (src-harness-engineering-article):** The harness engineering synthesis independently identifies the same pattern: "CLI over MCP is emerging consensus: Multiple sources now converge on CLI+Skills being more token-efficient and accurate than MCP for tool integration." The note explicitly flags a design implication: "consider a CLI+Skills alternative" for the research wiki's own MCP server.

**Claude Code extension comparison table (claude-code.md):** The Claude Code concept page documents the loading behavior of each extension type. MCP is listed as "Always available" — meaning always loaded — while Skills are "Invoked by user or auto" — meaning contextual. The table makes the tradeoff structural, not incidental.

**Context degradation curve (src-claude-code-accuracy-tips):** The same source documents that Claude Code context management matters at higher utilization (one practitioner reported increased error rates around 40-60% — but this is probabilistic and session-dependent). Any mechanism that loads tokens into context at startup — before the task begins — consumes context budget that compounds this degradation curve sooner. MCP schema loading is a direct contributor to earlier context exhaustion in multi-tool setups.

## Applicability

**Domains where this lesson applies directly:**

- **AI agent design**: Any Claude Code project deciding how to expose tools. Default to CLI+Skills for project-internal tooling; reserve MCP for tools that need cross-project discoverability.
- **Research wiki architecture**: The three planned MCP servers (wiki, NotebookLM, Obsidian) are the right long-term target for discoverability and "Claude becomes replaceable" goals — but the cost is per-session schema overhead. The current CLI tool + SKILL.md approach (pipeline commands + wiki-agent skill) should be validated against the MCP target before migrating.
- **OpenFleet agent design**: Each fleet agent is a Claude Code instance. MCP servers registered fleet-wide would load their schemas into every agent's context, including agents that never use those tools. Skills distributed to specific agents are more targeted.
- **AICP and devops-control-plane**: Any future agent in the ecosystem faces the same tradeoff. Establish the CLI-first default now before MCP proliferates as the default integration pattern.

**When MCP is still the right choice:**

- Tools that need to be callable from many different, unrelated conversations without per-conversation setup (e.g., a company-wide database access tool)
- Tools used so frequently in a project that the skill-loading overhead (an extra invocation step) outweighs the schema overhead
- External tool ecosystems where MCP servers already exist and the integration cost of a CLI+Skills alternative is not justified
- Discoverability requirements — when the agent needs to autonomously discover what tools are available without being explicitly told

> [!warning] Self-Check — Am I About to Make This Mistake?
>
> 1. Am I applying this lesson to my current context?
> 2. Do I have evidence that this applies HERE, or am I assuming?
> 3. What would change if this lesson didn't apply to my situation?
> 4. Have I checked the boundaries — where does this lesson NOT apply?

### How This Connects — Navigate From Here

> [!abstract] From This Lesson → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **What pattern generalizes this?** | [[context-aware-tool-loading|Context-Aware Tool Loading]] — eager vs deferred vs external loading. CLI = deferred. MCP = eager. 12x measured differential. |
> | **How does this connect to structured context?** | [[structured-context-governs-agent-behavior-more-than-content|Principle — Structured Context Governs Agent Behavior More Than Content]] — MCP schemas are UNSTRUCTURED context pollution. CLI+Skills load STRUCTURED context on demand. |
> | **How does tier-based depth apply?** | [[tier-based-context-depth-trust-earned-through-approval-rates|Tier-Based Context Depth — Trust Earned Through Approval Rates]] — same principle: lightweight tier = less context loaded = less pollution |
> | **What is the decision record?** | [[mcp-vs-cli-for-tool-integration|Decision — MCP vs CLI for Tool Integration]] — CLI for operational tasks, MCP for external service bridges and tool discovery |
> | **How does this connect to the wiki's own tools?** | The wiki has 26 MCP tools (as of 2026-04-15, grown from 17) AND CLI pipeline. MCP for discoverability. CLI for operational efficiency. Both exist because the tradeoff is real. |

## Relationships

- DERIVED FROM: [[src-claude-code-accuracy-tips|Synthesis — Claude Code Accuracy Tips]]
- DERIVED FROM: [[src-harness-engineering|Synthesis — Claude Code Harness Engineering]]
- DERIVED FROM: [[src-playwright-cli-vs-mcp|Synthesis — Playwright CLI vs MCP — Automate QA with Less Tokens]]
- RELATES TO: [[claude-code|Claude Code]]
- RELATES TO: [[mcp-integration-architecture|MCP Integration Architecture]]
- RELATES TO: [[claude-code-context-management|Claude Code Context Management]]
- RELATES TO: [[claude-code-skills|Claude Code Skills]]
- FEEDS INTO: [[mcp-integration-architecture|MCP Integration Architecture]]

## Backlinks

[[src-claude-code-accuracy-tips|Synthesis — Claude Code Accuracy Tips]]
[[src-harness-engineering|Synthesis — Claude Code Harness Engineering]]
[[src-playwright-cli-vs-mcp|Synthesis — Playwright CLI vs MCP — Automate QA with Less Tokens]]
[[claude-code|Claude Code]]
[[mcp-integration-architecture|MCP Integration Architecture]]
[[claude-code-context-management|Claude Code Context Management]]
[[claude-code-skills|Claude Code Skills]]
[[context-management-is-primary-productivity-lever|Context Management Is the Primary LLM Productivity Lever]]
[[context-aware-tool-loading|Context-Aware Tool Loading]]
[[skills-as-primary-extension-pattern|Decision — Skills as the Primary Extension Pattern (over MCP-everywhere or hooks-only)]]
[[model-knowledge-evolution-standards|Evolution Standards — What Good Knowledge Promotion Looks Like]]
[[mcp-vs-cli-decision-vs-lesson|MCP vs CLI — Decision Artifact vs Lesson Artifact]]
[[model-claude-code|Model — Claude Code]]
[[model-mcp-cli-integration|Model — MCP and CLI Integration]]
[[skills-architecture-is-dominant-extension-pattern|Skills Architecture Is the Dominant LLM Extension Pattern]]
[[src-7-levels-claude-code-rag|Source — The 7 Levels of Claude Code & RAG]]
[[src-context-mode|Synthesis — Context Mode — MCP Sandbox for Context Saving]]
[[model-wiki-design-standards|Wiki Design Standards — What Good Styling Looks Like]]
