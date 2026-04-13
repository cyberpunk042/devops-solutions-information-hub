---
title: Claude Code Best Practices
aliases:
  - "Claude Code Best Practices"
type: concept
layer: 2
maturity: growing
domain: ai-agents
status: synthesized
confidence: high
created: 2026-04-08
updated: 2026-04-10
sources:
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
tags: [claude-code, best-practices, orchestration, plan-mode, subagents, skills, commands, hooks, workflows, prompting, git, debugging, development-workflow]
---

# Claude Code Best Practices

## Summary

Claude Code best practices span the full development lifecycle: planning discipline (95% confidence before changes), memory architecture (lean CLAUDE.md as routing table), extensibility patterns (Command-Agent-Skill hierarchy), workflow automation (hooks for enforcement, skills for knowledge), context hygiene (deferred loading, subagent isolation, manual compaction), and git discipline (small PRs, frequent commits). The overarching pattern: 10 independent open-source frameworks converge on Research-Plan-Execute-Review-Ship. The convergence confirms this cycle is inherent to effective AI-assisted development, not one team's preference. Sources: Boris Cherny (Claude Code's creator), Anthropic team members, shanraisshan best practices repo, 18 Claude Code Token Hacks.

## Key Insights

### Planning and Execution

- **Plan before you build — the #1 practice.** Boris Cherny: "Do not make any changes until you have 95% confidence in what you need to build. Ask me follow-up questions until you reach that confidence level." The biggest source of token waste is not expensive models — it is Claude going down the wrong path and scrapping work.

- **Don't babysit, but do watch.** Let Claude work autonomously on bug fixes and exploration. But watch the initial direction — the first 2-3 tool calls reveal whether it's on the right path. The balance is temporal: control at planning, autonomy at execution.

- **Prototype over PRD (for exploratory features).** Boris's counterintuitive advice: build 20-30 prototype versions instead of detailed specs, because building is now cheap enough to take many shots. This does NOT contradict "plan before building" — it applies specifically to exploratory features where the requirements are unclear and iteration is the discovery method. For well-understood work, plan and spec first. For unknown territory, prototype.

### Extension Architecture

> [!info] **Command-Agent-Skill hierarchy**
> | Mechanism | Analog | When to use |
> |-----------|--------|-------------|
> | **Command** | Shell alias | Repeated prompt template in current context. No isolation needed. |
> | **Agent** | Microservice | Isolated context needed. Parallel execution. Different tool permissions. |
> | **Skill** | Library | Specialized knowledge loaded on demand. Progressive disclosure. Context forking. |
>
> The orchestration pattern: Command triggers → Agent executes in isolation → Skill provides knowledge. Mirrors the controller-service-library pattern in traditional architectures.

- **Skills are folders with progressive disclosure.** SKILL.md at root, references/, scripts/, examples/ subdirectories. The `description` field is a trigger written for the model ("when should I fire?"), not a human summary. Include a Gotchas section. Use `context: fork` when instructions exceed ~100 lines.

- **Hooks as enforcement glue.** PostToolUse for auto-formatting. PreToolUse for blocking dangerous operations. Stop hooks to force verification before completion. Permission-routing hooks that escalate to Opus for safety classification. On-demand hooks in skills (like /careful) add contextual safety.

### Memory Architecture

- **CLAUDE.md is an index, not an encyclopedia.** Under 200 lines. Routes to detailed files. Every message re-reads the entire CLAUDE.md — bloat compounds across every interaction. Use `.claude/rules/` for splitting large instruction sets. `<important if="...">` tags for rules that must not be forgotten.

### Context Hygiene

- **Deferred loading over eager loading.** Skills load on demand (zero baseline cost). MCP loads at startup (permanent overhead). CLI over MCP for operational tasks (12x measured differential). See [[context-aware-tool-loading|Context-Aware Tool Loading]].

- **Subagent isolation for heavy operations.** The Agent tool spawns workers with fresh context windows. Delegate research, bulk file operations, and exploratory analysis to subagents. The main conversation stays clean.

- **Compact at breakpoints, not under pressure.** Manual `/compact` at natural milestones (finished a task, completed an ingestion batch). Fresh sessions over infinite continuation when context feels heavy.

### Git and Development

- **Git discipline amplifies everything.** Small, focused PRs (p50 = 118 lines). Squash merges for clean history. Commit at least once per hour. Use /code-review for multi-agent PR analysis. Tag @claude on a colleague's PR to auto-generate lint rules from recurring feedback.

- **Agentic search beats RAG for code.** Claude Code tried and discarded vector databases internally — code drifts out of sync with embeddings. Glob + grep is more accurate for codebases. For stable curated knowledge bases, hybrid search (BM25 + vector + graph) wins. The split is domain-dependent: agentic search for code, hybrid for knowledge.

### The Universal Workflow

> [!abstract] **10 independent frameworks converge on one cycle**
> Everything Claude Code, Superpowers, Spec Kit, gstack, Get Shit Done, BMAD-METHOD, OpenSpec, oh-my-claudecode, Compound Engineering, HumanLayer — all arrived independently at Research → Plan → Execute → Review → Ship. Implementation varies (agents vs commands vs skills for planning, different spec formats, different verification). The fundamental cycle does not. This convergence is the strongest evidence that the pattern is inherent to the domain.

## Deep Analysis

### The Autonomy-Control Tension

The best practices landscape reveals a fundamental tension: "don't babysit" (let Claude work autonomously) coexists with "always plan first" (never let Claude start without a vetted plan). The resolution is temporal:

> [!tip] **Control at planning, autonomy at execution**
> Plan mode creates a contract — what to build, why, what approach. Execution mode fulfills it — the agent works autonomously within the contract's boundaries. The planning phase is HIGH control (95% confidence, clarifying questions, explicit approval). The execution phase is LOW control (watch the first few steps, then let it run). This matches the harness engineering pattern: enforce constraints at boundaries (plan → execute transition), allow freedom within stages.

This temporal split explains why Boris's "prototype over PRD" advice doesn't contradict planning discipline. Prototyping IS planning — each iteration narrows the solution space. The 95% confidence rule applies to the IMPLEMENTATION plan, not to the feature definition. You might build 20 prototypes to discover what to build, then plan carefully how to build the final version.

### The Compliance Problem

> [!warning] **Why does Claude sometimes ignore CLAUDE.md instructions?**
> An unsolved "billion-dollar question." CLAUDE.md instructions marked with MUST or ALWAYS are still sometimes ignored. The mechanism is likely context pressure — at higher utilization, the model's attention to earlier context degrades probabilistically. This is NOT a binary threshold ("above 60% = ignores rules") — it's a gradient where compliance becomes less reliable as context fills.
>
> **Practical mitigations (from current evidence):**
> - Keep CLAUDE.md under 200 lines (less to attend to = higher compliance per instruction)
> - Use `<important if="...">` tags for critical rules (attention anchoring)
> - Move enforcement to hooks where possible (~98% compliance vs ~60% for instructions)
> - Compact at natural breakpoints (reduce context pressure)
> - Fresh sessions for high-stakes work (start with clean context)

### Answered Deep Questions

> [!success] **Command vs Agent vs Skill — the decision tree**
> Use a **command** when: repeated prompt template in current context, no isolation needed. Use an **agent** when: isolated context needed, parallel execution, different tool permissions. Use a **skill** when: specialized knowledge needed on demand, progressive disclosure, `context: fork` for heavy instructions. Skills are for KNOWLEDGE, agents for ISOLATION, commands for SHORTCUTS. The hierarchy (Level 2 skills < Level 3 hooks) means skills sequence and teach; hooks enforce.

> [!success] **Skill complexity upper bound**
> The reliability boundary maps to the context degradation curve. A large skill (extensive SKILL.md + examples + scripts) compounds context pressure. The actionable rule: use `context: fork` for any skill exceeding ~100 lines. Forking gives the skill a fresh context window — the main conversation stays clean regardless of skill size.

> [!success] **Agentic search vs RAG — domain-dependent**
> Agentic search (glob + grep) wins for **code** — content drifts with every commit, embeddings go stale immediately. Hybrid search (BM25 + vector + graph) wins for **knowledge bases** — curated content is stable enough for semantic embeddings. The split mirrors CLI vs MCP: "CLI for project-internal" (code-like, frequent change) vs "MCP with indexing for cross-project" (knowledge-like, stable).

> [!success] **Skills: single file vs folder — maturity spectrum**
> Not conflicting approaches — different points on a spectrum. A seed skill is a single SKILL.md. A mature skill is a folder with SKILL.md + references/ + scripts/ + examples/. Start with a single file to validate the trigger, graduate to a folder when the skill accumulates scripts, reference docs, or known failure cases (Gotchas section).

## Open Questions

> [!question] **Can the Plan-Execute-Review cycle be further compressed?**
> Is the 5-verb cycle already at minimum viable complexity, or can it be optimized for specific task types? (Requires: comparative analysis of framework performance across task categories)

> [!question] **How do best practices change as models improve?**
> Does plan mode become less necessary as models improve at self-correction? Does the compliance problem diminish with larger context windows? (Requires: longitudinal tracking across model generations)

## Answered Open Questions

> [!example]- Is there a measurable CLAUDE.md compliance threshold?
> Resolved in [[extension-system-operational-decisions|Decision — Extension System Operational Decisions]]. Compliance is binary per rule, not a percentage threshold. Rules with consistently low compliance should graduate from CLAUDE.md instructions to hook-based enforcement.

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **What principle applies?** | [[right-process-for-right-context-the-goldilocks-imperative|Principle — Right Process for Right Context — The Goldilocks Imperative]] |
> | **What is my identity?** | [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]] |
> | **System map** | [[methodology-system-map|Methodology System Map]] |

## Relationships

- DERIVED FROM: [[src-shanraisshan-claude-code-best-practice|Synthesis — Claude Code Best Practice (shanraisshan)]]
- DERIVED FROM: [[src-token-hacks-claude-code|Synthesis — 18 Claude Code Token Hacks in 18 Minutes]]
- BUILDS ON: [[claude-code-skills|Claude Code Skills]]
- ENABLES: [[claude-code-context-management|Claude Code Context Management]]
- RELATES TO: [[llm-wiki-pattern|LLM Wiki Pattern]]
- RELATES TO: [[wiki-ingestion-pipeline|Wiki Ingestion Pipeline]]
- RELATES TO: [[harness-engineering|Harness Engineering]]
- RELATES TO: [[context-aware-tool-loading|Context-Aware Tool Loading]]
- RELATES TO: [[plan-execute-review-cycle|Plan Execute Review Cycle]]
- EXTENDS: [[claude-code|Claude Code]]

## Backlinks

[[src-shanraisshan-claude-code-best-practice|Synthesis — Claude Code Best Practice (shanraisshan)]]
[[src-token-hacks-claude-code|Synthesis — 18 Claude Code Token Hacks in 18 Minutes]]
[[claude-code-skills|Claude Code Skills]]
[[claude-code-context-management|Claude Code Context Management]]
[[llm-wiki-pattern|LLM Wiki Pattern]]
[[wiki-ingestion-pipeline|Wiki Ingestion Pipeline]]
[[harness-engineering|Harness Engineering]]
[[context-aware-tool-loading|Context-Aware Tool Loading]]
[[plan-execute-review-cycle|Plan Execute Review Cycle]]
[[claude-code|Claude Code]]
[[agent-orchestration-patterns|Agent Orchestration Patterns]]
[[agentic-search-vs-vector-search|Agentic Search vs Vector Search]]
[[always-plan-before-executing|Always Plan Before Executing]]
[[src-claude-slash-commands|Claude Code Slash Commands (artemgetmann)]]
[[model-claude-code-standards|Claude Code Standards — What Good Agent Configuration Looks Like]]
[[context-management-is-primary-productivity-lever|Context Management Is the Primary LLM Productivity Lever]]
[[extension-system-operational-decisions|Decision — Extension System Operational Decisions]]
[[per-role-command-design-decisions|Decision — Per-Role Command Design Decisions]]
[[design-md-pattern|Design.md Pattern]]
[[deterministic-shell-llm-core|Deterministic Shell, LLM Core]]
[[hooks-lifecycle-architecture|Hooks Lifecycle Architecture]]
[[infrastructure-as-code-patterns|Infrastructure as Code Patterns]]
[[model-claude-code|Model — Claude Code]]
[[model-markdown-as-iac|Model — Markdown as IaC — Design.md and Agent Configuration]]
[[model-skills-commands-hooks|Model — Skills, Commands, and Hooks]]
[[per-role-command-architecture|Per-Role Command Architecture]]
[[src-plannotator|Plannotator — Interactive Plan & Code Review for AI Agents]]
[[rework-prevention|Rework Prevention]]
[[skills-architecture-is-dominant-extension-pattern|Skills Architecture Is the Dominant LLM Extension Pattern]]
[[skills-architecture-patterns|Skills Architecture Patterns]]
[[src-claude-code-accuracy-tips|Synthesis — Claude Code Accuracy Tips]]
[[src-harness-engineering|Synthesis — Claude Code Harness Engineering]]
[[src-playwright-mcp-visual-testing|Synthesis — Playwright MCP for Visual Development Testing]]
[[src-superpowers-end-of-vibe-coding|Synthesis — Superpowers Plugin — End of Vibe Coding (Full Tutorial)]]
[[src-awesome-design-md|Synthesis — awesome-design-md — 58 Design Systems for AI Agents]]
[[wiki-event-driven-automation|Wiki Event-Driven Automation]]
