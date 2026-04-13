---
title: Claude Code Skills
aliases:
  - "Claude Code Skills"
type: concept
layer: 2
maturity: growing
domain: ai-agents
status: synthesized
confidence: high
created: 2026-04-08
updated: 2026-04-10
sources:
  - id: src-claude-notebooklm-content-team
    type: youtube-transcript
    file: raw/transcripts/claude-notebooklm-content-team.txt
    title: Claude + NotebookLM = Your 24/7 Content Team
    ingested: 2026-04-08
  - id: src-obsidian-claude-code-second-brain
    type: youtube-transcript
    url: https://www.youtube.com/watch?v=Y2rpFa43jTo
    file: raw/transcripts/obsidian-claude-code-the-second-brain-setup-that-actually-works.txt
    title: "Obsidian + Claude Code: The Second Brain Setup That Actually Works"
    ingested: 2026-04-08
  - id: src-shanraisshan-claude-code-best-practice
    type: documentation
    url: https://github.com/shanraisshan/claude-code-best-practice
    file: raw/articles/shanraisshanclaude-code-best-practice.md
    title: shanraisshan/claude-code-best-practice
    ingested: 2026-04-08
  - id: src-token-hacks-claude-code
    type: youtube-transcript
    url: https://www.youtube.com/watch?v=49V-5Ock8LU
    file: raw/transcripts/18-claude-code-token-hacks-in-18-minutes.txt
    title: 18 Claude Code Token Hacks in 18 Minutes
    ingested: 2026-04-08
tags: [claude-code, skills, markdown, agent-configuration, extensibility, obsidian-cli, multi-step-workflows, gmail-integration, progressive-disclosure, context-forking, hooks]
---

# Claude Code Skills

## Summary

Skills are Claude Code's primary extension mechanism — markdown-based instruction sets that teach the agent new capabilities, design systems, and multi-step workflows. Unlike MCP servers (which load tool schemas into context on every message regardless of use), skills load on demand: they enter the context window only when invoked, making them the most context-efficient way to extend agent capability. A skill can bundle dependency management, authentication flows, operational instructions, and design guidance into a single artifact. Skills exist on a complexity spectrum from simple tool wrappers through design-guided generators to multi-source workflow automations — and the upper bound of that spectrum is further out than initially assumed.

> [!info] Skill Architecture Reference Card
>
> | Property | Value |
> |----------|-------|
> | Format | Markdown folder: SKILL.md + references/ + scripts/ + examples/ |
> | Loading | On-demand (invoked by user or auto-detected by model) |
> | Context cost | Zero at rest; full instructions loaded only during execution |
> | Isolation | `context: fork` runs skill in sub-agent; parent sees only result |
> | Description field | Written for the model ("when should I fire?"), not for humans |
> | Gotchas section | Known failure points — prevents repeat debugging |
> | Scripts | Bundled code artifacts for composition (not reconstruction) |
> | Hooks | On-demand safety: /careful (block destructive), /freeze (scope lock) |
> | Complexity ceiling | ~100 lines unfork'd; effectively unlimited with `context: fork` |

## Key Insights

### Architecture — Why Markdown Wins

> [!tip] Skills are compressed knowledge, not detailed instructions
> Claude expands skill instructions into detailed operational prompts at execution time. A skill encoding "use blackboard style with orange accents" produces a fully-specified 7-slide deck with color codes, font choices, and layout parameters — without the user ever writing or seeing those detailed prompts. Skills act as high-level intent that the model decompresses on demand.

**Progressive disclosure through folder structure.** Per Anthropic's Thariq: skills should be folders with subdirectories, not monolithic files. SKILL.md is the entry point; references/ holds detailed option files loaded only when that specific option is selected; scripts/ contains code artifacts for the model to compose rather than reconstruct. This mirrors the deferred loading principle from Context-Aware Tool Loading — applied at the intra-skill level.

**Self-editing as meta-capability.** Users can modify skills through natural language conversation. Claude reads the skill, edits relevant sections, writes the updated file. This creates a feedback loop: the agent improves its own instruction set based on user input. Combined with the clarifying question pattern ("ask me clarifying questions so the intention is clear"), skills evolve iteratively through use rather than requiring manual markdown editing.

### Behavior — How Skills Operate

> [!abstract] Two-phase lifecycle: setup then use
> When Claude receives a skill, it performs one-time setup (install dependencies, authenticate) then makes the capability available for repeated invocation. The NotebookLM skill: (1) installs `notebooklm-py`, (2) prompts Google authentication. After setup, the skill is callable on demand across sessions — enabling scheduled automation of tasks that were set up once interactively.

**Design guidance encoded as rules, not suggestions.** Skills can embed aesthetic and brand standards alongside functional behavior. The NotebookLM skill includes color schemes, font choices, title formatting, and layout parameters. Outputs are consistent across runs because the design system is codified, not improvised.

**Multiple presets within one skill.** A skill can offer named options (e.g., "blackboard" vs. "corporate navy") selectable at runtime. This keeps related capabilities grouped while allowing variation — though as presets multiply, progressive disclosure (separate reference files per preset) prevents context bloat.

### Composition and Complexity

> [!info] The skill complexity spectrum
>
> | Tier | Example | What It Does |
> |------|---------|-------------|
> | **Simple** — tool wrapper | NotebookLM skill | Install package, authenticate, expose API |
> | **Medium** — tool + design | NotebookLM + slide styling | Tool operations + aesthetic/brand standards |
> | **Complex** — workflow automation | Onboard Projects skill | Multi-source data collection (Gmail API, filesystem, pasted content), conditional processing, structured output, dashboard maintenance |

**Skills compose with each other.** Higher-level workflow skills can orchestrate lower-level capability skills. The Obsidian ecosystem demonstrates this: markdown skill, database skill, and Canvas skill are independent capabilities; workflow skills like "onboard projects" coordinate across them. This is an emergent composition pattern — not formally specified, but observed in practice.

**Complex skills include custom scripts.** The onboard projects skill bundles Gmail integration scripts (fetching labels, messages, threads, downloading attachments) alongside its markdown instructions. Skills coordinate between multiple code artifacts, not just a single instruction file.

### Context Economics

> [!warning] Skills load on invocation — MCP loads on every message
> This is the fundamental economic advantage. A skill's instructions occupy zero context at rest and full context only during execution. MCP servers load their entire JSON schema on every message regardless of whether those tools are used. For project-internal tooling where you control the invocation pattern, skills are the default winner on context cost. Reserve MCP for tools needing cross-conversation discoverability.

**Context forking prevents pollution.** `context: fork` runs a skill in an isolated sub-agent where the parent context only sees the final result, not intermediate tool calls. For complex skills, this is essential — a 5-phase workflow automation would consume massive context in the parent session without forking. The practical threshold: fork any skill that exceeds ~100 lines of instructions.

## Deep Analysis

The skill system prioritizes simplicity and accessibility over formal plugin architectures. Any user who can write a markdown file can extend Claude Code's capabilities. This low barrier is a deliberate design choice — it means the ecosystem can grow from user contributions rather than requiring developer toolchains.

The deeper architectural insight is that **skills are the context-aware counterpart to MCP's always-on model.** MCP provides universal discoverability at the cost of per-message overhead. Skills provide targeted capability at the cost of requiring explicit invocation. Neither is strictly better — the optimal choice depends on invocation frequency and context budget. But for the typical project where 80% of tools are used in <20% of conversations, the skills model is dramatically more efficient.

The self-editing meta-capability has implications beyond convenience. When an agent can modify its own instruction set through conversation, the skill evolves through use — accumulating the user's preferences, edge cases, and style choices as codified knowledge. Over time, a well-maintained skill becomes a compressed record of how a team actually works, not just how they planned to work. This is the same principle behind the wiki's own model-builder skill: it encodes not just "how to build models" but "what we learned about building models."

The composition pattern (higher-level skills orchestrating lower-level skills) suggests an emerging architecture where skills form a capability graph — similar to how this wiki's models reference building block concepts. Formal skill-to-skill composition remains unsolved in the ecosystem, but the practical pattern of "skill A invokes CLI operations that skill B also uses" achieves de facto composition through shared tooling rather than direct references.

> [!example]- This wiki's skill instances
>
> | Skill | Tier | What It Does |
> |-------|------|-------------|
> | wiki-agent | Complex | Ingest, query, validate, export — full wiki operations |
> | model-builder | Complex | Document → Design → Implement → Test for model pages |
> | evolve | Medium | Score candidates, scaffold, generate, review maturity |
> | continue | Simple | Resume mission: diagnostics → state → options |
>
> All four use the progressive disclosure pattern: SKILL.md routes to tool documentation that Claude reads on demand rather than loading everything upfront.

## Open Questions

(All resolved — see Answered Open Questions below.)

## Answered Open Questions

> [!example]- Is there a versioning or update mechanism for skills?
> Resolved in [[extension-system-operational-decisions|Decision — Extension System Operational Decisions]]. CHANGELOG section in SKILL.md tracks breaking changes; wait for agentskills.io for ecosystem-wide versioning.

> [!example]- Can skills formally compose other skills?
> Resolved in [[extension-system-operational-decisions|Decision — Extension System Operational Decisions]]. Formal skill-to-skill composition is not supported; de facto composition happens through shared CLIs and bundled scripts.

> [!example]- Maximum practical complexity before unreliability?
> The ceiling is not a fixed line count but a function of session context pressure. Any skill consuming a substantial fraction of the context window triggers degradation. Resolution: `context: fork` for extensive skills — this isolates execution in a sub-agent. The practical upper bound: ~100 lines unfork'd before degradation risk becomes significant; with `context: fork`, the ceiling is effectively the sub-agent's full context budget.

> [!example]- How are conflicts between contradictory skills resolved?
> Conflict resolution is governed by invocation order and CLAUDE.md routing, not a registry-level priority system. CLAUDE.md project instructions override community defaults. Skills loaded later with explicit instructions take precedence. `<important if="...">` tags provide the highest-priority override. For direct contradictions: `context: fork` for each skill isolates their instructions in separate sub-agents.

> [!example]- How does performance degrade as skill files grow?
> Degradation follows the context saturation curve directly. Each additional preset/option/example increases token load every time the skill is active. Resolution: instead of growing a single skill file, refactor into separate named skills (each loaded on demand) or use progressive disclosure — SKILL.md references detailed option files in references/ subdirectories loaded only when selected.

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **What principle applies?** | [[right-process-for-right-context-the-goldilocks-imperative|Principle — Right Process for Right Context — The Goldilocks Imperative]] |
> | **What is my identity?** | [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]] |
> | **System map** | [[methodology-system-map|Methodology System Map]] |

## Relationships

- DERIVED FROM: [[src-claude-notebooklm-content-team|Synthesis — Claude + NotebookLM Content Automation]]
- DERIVED FROM: [[src-obsidian-claude-code-second-brain|Synthesis — Obsidian + Claude Code Second Brain Setup]]
- DERIVED FROM: [[src-shanraisshan-claude-code-best-practice|Synthesis — Claude Code Best Practice (shanraisshan)]]
- DERIVED FROM: [[src-token-hacks-claude-code|Synthesis — 18 Claude Code Token Hacks in 18 Minutes]]
- ENABLES: [[ai-driven-content-pipeline|AI-Driven Content Pipeline]]
- ENABLES: [[claude-code-scheduling|Claude Code Scheduling]]
- ENABLES: [[claude-code-best-practices|Claude Code Best Practices]]
- ENABLES: [[claude-code-context-management|Claude Code Context Management]]
- ENABLES: [[wiki-event-driven-automation|Wiki Event-Driven Automation]]
- BUILDS ON: [[notebooklm|NotebookLM]]
- RELATES TO: [[obsidian-knowledge-vault|Obsidian Knowledge Vault]]
- RELATES TO: [[skills-architecture-patterns|Skills Architecture Patterns]]
- USED BY: [[openfleet|OpenFleet]]
- USED BY: [[aicp|AICP]]
- BUILDS ON: [[openclaw|OpenClaw]]
- BUILDS ON: [[claude-code|Claude Code]]

## Backlinks

[[src-claude-notebooklm-content-team|Synthesis — Claude + NotebookLM Content Automation]]
[[src-obsidian-claude-code-second-brain|Synthesis — Obsidian + Claude Code Second Brain Setup]]
[[src-shanraisshan-claude-code-best-practice|Synthesis — Claude Code Best Practice (shanraisshan)]]
[[src-token-hacks-claude-code|Synthesis — 18 Claude Code Token Hacks in 18 Minutes]]
[[ai-driven-content-pipeline|AI-Driven Content Pipeline]]
[[claude-code-scheduling|Claude Code Scheduling]]
[[claude-code-best-practices|Claude Code Best Practices]]
[[claude-code-context-management|Claude Code Context Management]]
[[wiki-event-driven-automation|Wiki Event-Driven Automation]]
[[notebooklm|NotebookLM]]
[[obsidian-knowledge-vault|Obsidian Knowledge Vault]]
[[skills-architecture-patterns|Skills Architecture Patterns]]
[[openfleet|OpenFleet]]
[[aicp|AICP]]
[[openclaw|OpenClaw]]
[[claude-code|Claude Code]]
[[always-plan-before-executing|Always Plan Before Executing]]
[[cli-tools-beat-mcp-for-token-efficiency|CLI Tools Beat MCP for Token Efficiency]]
[[src-claude-slash-commands|Claude Code Slash Commands (artemgetmann)]]
[[model-claude-code-standards|Claude Code Standards — What Good Agent Configuration Looks Like]]
[[context-management-is-primary-productivity-lever|Context Management Is the Primary LLM Productivity Lever]]
[[context-aware-tool-loading|Context-Aware Tool Loading]]
[[extension-system-operational-decisions|Decision — Extension System Operational Decisions]]
[[mcp-vs-cli-for-tool-integration|Decision — MCP vs CLI for Tool Integration]]
[[per-role-command-design-decisions|Decision — Per-Role Command Design Decisions]]
[[harness-engineering|Harness Engineering]]
[[model-claude-code|Model — Claude Code]]
[[model-skills-commands-hooks|Model — Skills, Commands, and Hooks]]
[[multi-channel-ai-agent-access|Multi-Channel AI Agent Access]]
[[notebooklm-skills|NotebookLM Skills]]
[[obsidian-cli|Obsidian CLI]]
[[obsidian-skills-ecosystem|Obsidian Skills Ecosystem]]
[[obsidian-as-knowledge-infrastructure|Obsidian as Knowledge Infrastructure Not Just Note-Taking]]
[[openarms|OpenArms]]
[[per-role-command-architecture|Per-Role Command Architecture]]
[[plan-execute-review-cycle|Plan Execute Review Cycle]]
[[src-plannotator|Plannotator — Interactive Plan & Code Review for AI Agents]]
[[skill-specification-is-key-to-interoperability|Skill Specification Is the Key to Ecosystem Interoperability]]
[[skills-architecture-is-dominant-extension-pattern|Skills Architecture Is the Dominant LLM Extension Pattern]]
[[src-claude-code-accuracy-tips|Synthesis — Claude Code Accuracy Tips]]
[[src-harness-engineering|Synthesis — Claude Code Harness Engineering]]
[[src-context-mode|Synthesis — Context Mode — MCP Sandbox for Context Saving]]
[[src-notebooklm-claude-code-workflow|Synthesis — NotebookLM + Claude Code Workflow via notebooklm-py]]
[[src-playwright-cli-vs-mcp|Synthesis — Playwright CLI vs MCP — Automate QA with Less Tokens]]
[[src-playwright-mcp-visual-testing|Synthesis — Playwright MCP for Visual Development Testing]]
[[src-pleaseprompto-notebooklm-skill|Synthesis — PleasePrompto-notebooklm-skill]]
[[src-superpowers-end-of-vibe-coding|Synthesis — Superpowers Plugin — End of Vibe Coding (Full Tutorial)]]
[[src-axton-obsidian-visual-skills|Synthesis — axtonliu-axton-obsidian-visual-skills]]
[[src-claude-world-notebooklm-skill|Synthesis — claude-world-notebooklm-skill]]
[[src-kepano-obsidian-skills|Synthesis — kepano-obsidian-skills]]
[[src-pablo-mano-obsidian-cli-skill|Synthesis — pablo-mano-Obsidian-CLI-skill]]
[[notebooklm-py-cli|notebooklm-py CLI]]
