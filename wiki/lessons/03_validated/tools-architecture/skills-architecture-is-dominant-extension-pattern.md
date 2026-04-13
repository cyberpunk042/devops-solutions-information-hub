---
title: Skills Architecture Is the Dominant LLM Extension Pattern
aliases:
  - "Skills Architecture Is the Dominant LLM Extension Pattern"
type: lesson
domain: ai-agents
layer: 4
status: synthesized
confidence: high
maturity: growing
created: 2026-04-08
updated: 2026-04-13
sources:
  - id: src-obsidian-claude-code-second-brain
    type: youtube-transcript
    url: https://www.youtube.com/watch?v=Y2rpFa43jTo
    title: "Obsidian + Claude Code: The Second Brain Setup That Actually Works"
tags: [skills, llm-extension, claude-code, markdown, extensibility, patterns, agent-configuration]
derived_from:
  - "Claude Code Skills"
  - "Claude Code Best Practices"
---

# Skills Architecture Is the Dominant LLM Extension Pattern

## Summary

Skills — bundled markdown packages that combine instructions, context, scripts, and design guidance — have emerged as the primary pattern for extending LLM agent capabilities. Observed independently across Claude Code, Obsidian, NotebookLM integrations, and custom frameworks, skills outcompete plugins, MCP servers, and fine-tuning for the majority of extension use cases because they are readable, composable, and require no infrastructure beyond a text file.

## Context

This lesson applies whenever you need to extend an LLM agent's capability to interact with a new tool, enforce a workflow, or embed domain-specific knowledge. It is especially relevant during agent harness design, when building operator tooling in ecosystems like openfleet or AICP, and when deciding whether to invest in MCP integration vs. a simpler skill-based approach.

The convergence was observed across at least four independent contexts: Claude Code's own extensibility model (skills folders), the Obsidian + Claude Code second brain setup (Obsidian CLI skills installed via npx), the NotebookLM integration (notebooklm-py skill bundled with design guidance), and the shanraisshan best practices repository documenting skills as a first-class architectural tier alongside commands and agents.

## Insight

> [!tip] Right Level of Abstraction
> Skills are plain markdown — no compiled code, no API registrations, no infrastructure. They bundle all concerns: dependency installation, authentication flow, operational instructions, design guidance, and known failure points. Before writing MCP tooling, ask whether a skill achieves 80% of the value at 10% of the cost.

Skills are winning because they solve the LLM extension problem at the right level of abstraction. They are plain markdown — no compiled code, no API registrations, no infrastructure. They bundle all concerns a Claude needs to use a tool: dependency installation, authentication flow, operational instructions, design guidance, and known failure points (Gotchas section). Skills can be iterated through natural language ("change the slide style"), shared as community packages, and composed hierarchically (higher-level workflow skills orchestrating lower-level capability skills).

The architecture has three levels: simple skills are single markdown files wrapping a single tool; medium skills combine tool instructions with format or design guidance; complex skills orchestrate multi-source data pipelines with conditional logic. The upper bound for skill complexity is further out than initially assumed — the "onboard projects" skill in the Obsidian second brain demo ingests data from Gmail API, local files, and pasted screenshots, processes with conditional logic, and maintains a structured Obsidian database, all from a single skill definition.

The key structural innovation is progressive disclosure via folders: `SKILL.md` (trigger description written for the model), `references/` (spec documents), `scripts/` (bundled code), `examples/` (sample outputs). Combined with `context: fork` to run in isolated subagents, this prevents skill execution from polluting the main conversation's context window — solving the composition problem cleanly.

## Evidence

From the Claude Code Skills source page: "Skills are folders with progressive disclosure... The SKILL.md description field is a trigger written for the model ('when should I fire?'), not a human summary. Skills should include a Gotchas section for known failure points and should contain scripts/libraries so Claude composes rather than reconstructs boilerplate."

From the Claude Code Best Practices source page: "Skills are configurable, preloadable knowledge bundles with progressive disclosure and context forking. The pattern is: Command orchestrates, Agent executes in isolation, Skill provides specialized knowledge."

From the Accuracy Tips synthesis: "CLI+Skills loads tool instructions only when relevant (skill loading is contextual), while MCP loads all tool schemas into context at startup. Result: CLI is more token-efficient, produces fewer hallucinations, costs less. Google Trends shows CLI overtaking MCP."

From the second brain demo (Claude Code Skills): "Complex multi-step workflow skills... goes well beyond simple tool wrappers. It includes multi-source data collection (Gmail API via OAuth2, local filesystem, user-pasted text/screenshots), conditional processing logic, structured output generation, and dashboard maintenance."

The skills-beat-MCP finding is independently confirmed in the harness engineering synthesis: "CLI over MCP is emerging consensus: Multiple sources now converge on CLI+Skills being more token-efficient and accurate than MCP for tool integration."

## Applicability

- **openfleet / AICP / devops-control-plane**: When integrating new tools into agent workflows, default to skill-first over MCP. Build skills for tools with stable APIs; reserve MCP for tools requiring bidirectional streaming or complex resource negotiation.
- **Any new agent capability**: Before writing MCP tooling, ask whether a skill (markdown + bundled script) achieves 80% of the value at 10% of the cost.
- **Operator tooling**: Skills are the natural unit of sharing in Claude Code communities. Build operator-specific skills for recurring workflows (infrastructure provisioning, incident response, deployment pipelines).
- **Context management**: Use `context: fork` in complex skills to keep intermediate steps out of the main orchestrator's context window.

## Self-Check — Am I About to Make This Mistake?

> [!warning] Ask yourself:
>
> 1. **Am I building custom MCP tooling when a skill (markdown + bundled script) would achieve 80% of the value at 10% of the cost?** — Skills are plain markdown with no compiled code, no API registration, no infrastructure. Before investing in MCP, verify that a skill does not already solve the problem more simply.
> 2. **Am I building a monolithic tool when a composable skill would be more portable?** — Skills can be shared as community packages, composed hierarchically, and iterated through natural language. A custom tool locks you into one implementation. Which do you need?
> 3. **Am I loading all tool schemas into context at startup (MCP pattern) when contextual skill loading would be more token-efficient?** — MCP loads everything upfront; skills load only when triggered. For token-sensitive workflows, this difference compounds across every interaction.
> 4. **Am I running a complex skill in the main conversation instead of using `context: fork`?** — Skill execution in the main thread pollutes the orchestrator's context with intermediate steps. Fork the skill so the main conversation sees only the final result.

### How This Connects — Navigate From Here

> [!abstract] From This Lesson → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **What principle governs this?** | [[right-process-for-right-context-the-goldilocks-imperative|Principle — Right Process for Right Context — The Goldilocks Imperative]] |
> | **How does enforcement apply?** | [[infrastructure-over-instructions-for-process-enforcement|Principle — Infrastructure Over Instructions for Process Enforcement]] |
> | **How does structure help?** | [[structured-context-governs-agent-behavior-more-than-content|Principle — Structured Context Governs Agent Behavior More Than Content]] |
> | **What is my identity profile?** | [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]] |
> | **Where does this fit in the system?** | [[methodology-system-map|Methodology System Map]] — find any component |

## Relationships

- DERIVED FROM: [[src-kepano-obsidian-skills|Synthesis — kepano-obsidian-skills]]

- DERIVED FROM: [[claude-code-skills|Claude Code Skills]]
- DERIVED FROM: [[claude-code-best-practices|Claude Code Best Practices]]
- BUILDS ON: [[claude-code|Claude Code]]
- COMPARES TO: [[mcp-integration-architecture|MCP Integration Architecture]]
- ENABLES: [[wiki-event-driven-automation|Wiki Event-Driven Automation]]
- RELATES TO: [[cli-tools-beat-mcp-for-token-efficiency|CLI Tools Beat MCP for Token Efficiency]]
- RELATES TO: [[harness-engineering|Harness Engineering]]
- FEEDS INTO: [[openfleet|OpenFleet]]
- FEEDS INTO: [[aicp|AICP]]

## Backlinks

[[src-kepano-obsidian-skills|Synthesis — kepano-obsidian-skills]]
[[claude-code-skills|Claude Code Skills]]
[[claude-code-best-practices|Claude Code Best Practices]]
[[claude-code|Claude Code]]
[[mcp-integration-architecture|MCP Integration Architecture]]
[[wiki-event-driven-automation|Wiki Event-Driven Automation]]
[[cli-tools-beat-mcp-for-token-efficiency|CLI Tools Beat MCP for Token Efficiency]]
[[harness-engineering|Harness Engineering]]
[[openfleet|OpenFleet]]
[[aicp|AICP]]
[[identity-profile|AICP — Identity Profile]]
[[model-claude-code|Model — Claude Code]]
[[per-role-command-architecture|Per-Role Command Architecture]]
