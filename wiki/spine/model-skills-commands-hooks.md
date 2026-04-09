---
title: "Model Guide: Skills + Commands + Hooks"
type: learning-path
domain: cross-domain
layer: spine
status: synthesized
confidence: high
maturity: growing
created: 2026-04-09
updated: 2026-04-09
sources: []
tags: [skills, commands, hooks, model-guide, learning-path, ai-agent-extension, per-role, plannotator, design-md, spine]
---

# Model Guide: Skills + Commands + Hooks

## Summary

The Skills + Commands + Hooks model describes the three-tier system for extending and controlling AI agents. Skills are markdown instruction sets that teach agents how to operate specific tools or workflows, loaded on demand from context. Commands are lightweight slash-command triggers that invoke skills or inject prompts into the current context. Hooks are shell commands or agents that fire at lifecycle events, providing runtime enforcement that no instruction set alone can match. Together they form a coordinated extension system: Commands orchestrate, Skills provide knowledge, Hooks enforce. This model governs how every agent in this ecosystem is configured, extended, and controlled.

## Prerequisites

- Basic understanding of Claude Code as an agent runtime (see Model Guide: Claude Code)
- Familiarity with the concept of CLAUDE.md as the project brain loaded into every conversation
- No prior experience with hooks, slash commands, or skill files required

## Sequence

### L1 — Primary Sources

- [[Synthesis: Claude Code Best Practice (shanraisshan)]] — Origin of the Command-Agent-Skill hierarchy; progressive disclosure folder structure; on-demand hooks in skills
- `wiki/sources/src-claude-code-hooks-reference.md` — Full reference for all 26 hook events, 4 handler types, blocking pattern, and composition rules
- [[Claude Code Slash Commands (artemgetmann)]] — Per-role command architecture; two-scope install model; commands as workflow entry points
- [[Plannotator — Interactive Plan & Code Review for AI Agents]] — The command + hook pair pattern; interactive annotation workflow; how commands activate hook-intercepted pipelines

### L2 — Core Concepts

Read in this order:

1. **Claude Code Skills** ([[Claude Code Skills]]) — Skills as plain markdown instruction sets; two-phase operation (setup then use); progressive disclosure folder structure (SKILL.md + references/ + scripts/ + examples/); context forking for isolation; on-demand hooks embedded in skills. Start here.
2. **Hooks Lifecycle Architecture** ([[Hooks Lifecycle Architecture]]) — 26 events across 7 categories; the blocking pattern on PreToolUse; the reverse-hook pattern on Stop/TeammateIdle; context injection via additionalContext; 4 handler types (command, http, prompt, agent); composition via matchers and scope hierarchy.
3. **Per-Role Command Architecture** ([[Per-Role Command Architecture]]) — Commands as lightweight triggers vs skills as full context; role-segmented command palettes; the Plannotator pattern (command activates hook-intercepted workflow); execution mode to command set mapping.
4. **Design.md Pattern** ([[Design.md Pattern]]) — How the design document functions as a persistent shared context artifact between human and agent; why the Design stage produces a design.md before implementation begins.
5. **Obsidian Skills Ecosystem** ([[Skill Specification Is the Key to Ecosystem Interoperability]]) — Real-world complex skills: the kepano Obsidian skills as a reference implementation; multi-step workflow skills; skill composition patterns.
6. **NotebookLM Skills** ([[NotebookLM as Grounded Research Engine Not Just Note Storage]]) — The NotebookLM skill as the canonical example of a tool-wrapper skill: dependency management + authentication + operation + design guidance in one file.

### L3 — Comparisons

- **Pattern: Skills + Claude-Code** (`wiki/patterns/pattern-skills-+-claude-code.md`) — How skills compose with native Claude Code capabilities.
- **Pattern: Skills + CLI** (`wiki/patterns/pattern-skills-+-cli.md`) — Skills that wrap CLI tools; the preferred integration pattern for project-internal tooling.
- **Pattern: Skills + MCP** (`wiki/patterns/pattern-skills-+-mcp.md`) — When skills and MCP servers operate together; the hybrid integration model.
- **Pattern: Skills + Obsidian** (`wiki/patterns/pattern-skills-+-obsidian.md`) — Obsidian-specific skill composition patterns.
- **Pattern: Skills + NotebookLM** (`wiki/patterns/pattern-skills-+-notebooklm.md`) — NotebookLM skill architecture and composition.

### L4 — Lessons (Validated Insights)

- **Skill Specification Is Key to Interoperability** (`wiki/lessons/lesson-hub-—-agent-orchestration-patterns.md`) — Why a well-specified skill is interoperable across agent runtimes; the agentskills.io ecosystem standardization direction.
- **Skills Architecture Is the Dominant Pattern** ([[Skills Architecture Is the Dominant LLM Extension Pattern]]) — Skills are the primary extension mechanism; hooks and MCP serve narrower, complementary roles.

### L5 — Patterns (Structural Templates)

- **Context-Aware Tool Loading** ([[Context-Aware Tool Loading]]) — Defer skill loading until needed; never pre-load all skills at session start; how `context: fork` isolates skill execution.

## Outcomes

After completing this learning path you will understand:

- The three-tier hierarchy (Commands → Skills → Hooks) and the precise role of each tier
- How to build a skill: the folder structure, SKILL.md trigger description, references/ subdirectory, on-demand hooks, and context forking
- Which of the 26 hook events to use for each enforcement scenario: PreToolUse for gating, Stop for anti-premature-exit, PostToolUse for side effects
- How to structure a per-role command palette: personal scope for universal utilities, project scope for team workflows
- The Plannotator pattern: how commands activate hook-intercepted pipelines for interactive review workflows
- How skills, commands, and hooks compose into a coordinated harness — not independent features but a designed system
- Why skill specification determines whether a skill is portable across agent runtimes

## Relationships

- FEEDS INTO: [[Model Guide: Claude Code]]
- FEEDS INTO: [[Model Guide: MCP + CLI Integration]]
- BUILDS ON: [[Claude Code Skills]]
- BUILDS ON: [[Hooks Lifecycle Architecture]]
- BUILDS ON: [[Per-Role Command Architecture]]
- RELATES TO: [[Model Guide: Methodology]]
- RELATES TO: [[Model Guide: LLM Wiki]]

## Backlinks

[[Model Guide: Claude Code]]
[[Model Guide: MCP + CLI Integration]]
[[Claude Code Skills]]
[[Hooks Lifecycle Architecture]]
[[Per-Role Command Architecture]]
[[Model Guide: Methodology]]
[[Model Guide: LLM Wiki]]
[[Model Guide: Ecosystem Architecture]]
