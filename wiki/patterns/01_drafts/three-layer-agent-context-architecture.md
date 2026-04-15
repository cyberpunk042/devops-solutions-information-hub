---
title: "Three-Layer Agent Context Architecture"
type: pattern
domain: cross-domain
layer: 5
status: synthesized
confidence: high
maturity: growing
derived_from:
  - "src-skillmd-claudemd-agentsmd-three-layer-context"
  - "src-bmad-method-agile-ai-development-framework"
  - "model-claude-code"
  - "model-skills-commands-hooks"
instances:
  - page: "src-skillmd-claudemd-agentsmd-three-layer-context"
    context: "Canonical three-layer architecture: AGENTS.md (universal, <100 lines) + CLAUDE.md (tool-specific delta, <20 lines) + skills (on-demand, <500 lines each)"
  - page: "src-bmad-method-agile-ai-development-framework"
    context: "project-context.md (cross-agent living constitution) + agent personas (tool-specific roles) + workflow skills (on-demand task scoping)"
  - page: "Research Wiki (this project, post 2026-04-14 refactor)"
    context: "AGENTS.md (159L) + CLAUDE.md (107L, slimmed from 315L) + .claude/skills/ + 5 thematic root files (CONTEXT/ARCHITECTURE/DESIGN/TOOLS/SKILLS) for separation of concerns. See [[root-documentation-map|Root Documentation Map]]."
created: 2026-04-14
updated: 2026-04-14
sources:
  - id: src-skillmd-claudemd-agentsmd-termdock
    type: article
    url: "https://www.termdock.com/blog/skill-md-vs-claude-md-vs-agents-md"
  - id: bmad-method-github
    type: repository
    url: "https://github.com/bmad-code-org/BMAD-METHOD"
tags:
  - context-engineering
  - agent-config
  - three-layer-architecture
  - agents-md
  - claude-md
  - skill-md
  - cross-tool-portability
  - context-efficiency
  - ai-agents
  - pattern
---

# Three-Layer Agent Context Architecture

## Summary

AI agent context configuration naturally separates into three distinct layers that differ in scope, loading model, and size constraints. Mixing them into a single monolithic file creates context pollution, tool lock-in, and performance degradation — ETH Zurich Feb 2026 research found AI-generated monolithic context files reduce task success by 3% compared to no file. The three-layer pattern resolves this: a universal always-on layer for cross-tool project context, a tool-specific thin delta layer for tool-unique overrides, and an on-demand task-scoped layer for rich workflow depth. This structure has emerged independently across multiple ecosystems with remarkably consistent layer semantics.

> [!info] Pattern Reference Card
>
> | Layer | Name(s) | Scope | Loading | Max Size | Script Execution |
> |-------|---------|-------|---------|----------|-----------------|
> | 1 — Universal | AGENTS.md | Cross-tool, always-on | Every session, all tools | <100 lines | No |
> | 2 — Tool-specific | CLAUDE.md, per-tool deltas | Single tool, always-on | Every session, this tool only | <20 lines | No |
> | 3 — Conditional | SKILL.md, workflows, personas | Per-task, on-demand | On trigger/invocation | <500 lines each | Yes (Layer 3 only) |

## Pattern Description

Agent context configuration solves the problem of giving an AI agent the right information at the right moment. Every piece of context injected into a session competes for the model's attention window. Information loaded unconditionally but only relevant to 10% of tasks wastes 90% of the cognitive load it creates. Information that is always relevant but loaded conditionally creates session-startup ambiguity ("did my project context load?"). The three-layer architecture resolves this tension by matching **loading behavior** to **relevance scope**.

**Layer 1 — Universal Always-On (AGENTS.md)**

This layer carries everything that is true about the project regardless of which AI tool is being used and regardless of which task is being performed. Project identity, core conventions, critical constraints, command references. It is intentionally cross-tool — the same file is read by Claude Code, Codex CLI, Copilot CLI, Gemini CLI, and any other tool implementing the AGENTS.md standard (60,000+ repos; Linux Foundation Agentic AI Foundation stewardship as of 2026).

The 100-line limit is not a suggestion but a performance boundary. ETH Zurich Feb 2026 research found that even carefully written context files improve task success by only ~4%, while AI-generated context files reduce success by ~3%. This narrow margin means every line must pay for its presence. Bloat actively costs performance.

**Layer 2 — Tool-Specific Delta (CLAUDE.md)**

This layer contains only what Layer 1 cannot express because it is specific to one tool's behavior model. For Claude Code, this is: skill invocation patterns, memory behavior, specific commands that use Claude-unique APIs, tool-specific overrides. In the three-layer model, this shrinks to under 20 lines — a pointer to AGENTS.md plus 2–3 Claude-specific items. Most projects that have a 300-line CLAUDE.md could express the same content with a 15-line CLAUDE.md pointing to a 90-line AGENTS.md with no loss of quality and significant gain in portability and session startup efficiency.

**Layer 3 — On-Demand Task-Scoped (SKILL.md / workflows / personas)**

This layer carries the rich, detailed, step-by-step workflow knowledge that would be prohibitively expensive to load unconditionally. Database migration workflows. Code review protocols. Deployment procedures. Brainstorming facilitation scripts. Agent personas with specialized knowledge. These load only when invoked — by trigger match in skill systems, by explicit agent selection in BMAD, by command invocation in Spec Kit.

The 500-line ceiling per skill file is a per-file limit, not an aggregate limit. A project can have 50 skill files, each up to 500 lines, without any of that content polluting baseline sessions. Script execution capability is unique to Layer 3: the always-on layers (1 and 2) are passive context injection; skills can execute bash scripts, call tools, and actively modify the session state.

> [!warning] The monolith failure mode
>
> The most common mistake is conflating all three layers into a single file — usually a 300–400 line CLAUDE.md that tries to be project context, tool overrides, and task workflows simultaneously. This creates three concurrent failures:
> 1. **Context pollution**: workflow steps load for every task, not just the tasks they apply to
> 2. **Tool lock-in**: the content is Claude-specific and can't be reused by other AI tools
> 3. **Performance degradation**: measured 3% success rate drop vs. no file at all (ETH Zurich)
>
> This wiki's CLAUDE.md was previously ~315 lines (a live example of this failure mode). On 2026-04-14, the fix was applied mechanically: extracted project-universal content to AGENTS.md, reduced CLAUDE.md to a 107-line delta, and added 5 thematic root files (CONTEXT/ARCHITECTURE/DESIGN/TOOLS/SKILLS) for separation of concerns. See [[root-documentation-map|Root Documentation Map]] for the full implementation.

## Instances

| Instance | Domain | Layer 1 | Layer 2 | Layer 3 |
|----------|--------|---------|---------|---------|
| Claude Code ecosystem | ai-agents | AGENTS.md (<100 lines, cross-tool) | CLAUDE.md (<20 lines, Claude delta) | `.claude/skills/*.md` (<500 lines each) |
| BMAD-METHOD | methodology | `project-context.md` (living constitution, auto-loaded by all agents) | Per-agent persona files (PM, Architect, Developer, etc.) | Task workflow skills (brainstorming, quick-dev, code-review, etc.) |
| This wiki (post-refactor 2026-04-14) | knowledge | AGENTS.md (159 lines) | CLAUDE.md (107 lines, slimmed from 315) | `.claude/skills/` + 5 thematic root docs |
| Cline (VS Code extension, v3.55+) | ai-agents | AGENTS.md (explicit support added) | CLAUDE.md as pure imports: `@.clinerules/general.md` + others | `.agents/skills/*/SKILL.md` (folder-per-skill pattern) |

> [!example]- Instance 1: Claude Code Ecosystem (canonical source)
>
> **Source:** [[src-skillmd-claudemd-agentsmd-three-layer-context|Synthesis — SKILL.md vs CLAUDE.md vs AGENTS.md]]
>
> **Layer 1 — AGENTS.md:** Cross-tool project context. Read simultaneously by Claude Code, Codex CLI, Copilot CLI, Gemini CLI, Cursor. 60,000+ repos have adopted this format. Under Linux Foundation (Agentic AI Foundation). Hard limit: <100 lines. AI-generated AGENTS.md files that blow past this limit measurably hurt performance.
>
> **Layer 2 — CLAUDE.md:** Claude Code–specific session identity. In the three-layer model, shrinks to under 20 lines: a pointer to AGENTS.md plus Claude-unique items (skill invocation syntax, memory instructions, tool permissions). Claude Code reads BOTH AGENTS.md and CLAUDE.md simultaneously — CLAUDE.md becomes the delta, AGENTS.md becomes canonical.
>
> **Layer 3 — SKILL.md files in `.claude/skills/`:** On-demand task depth. Up to 500 lines each. YAML frontmatter `description` field is the trigger surface — Claude Code matches the incoming task description against skill descriptions to determine which skills to inject. Script execution is possible here. The `agentskills.io` SKILL.md format is cross-tool compatible (Claude Code, Codex CLI, OpenCode, Cursor).
>
> **Key finding:** AI-generated context files reduce task success by ~3% vs. no file. Human-written files improve by ~4%. The net margin is razor-thin. Every line must justify its presence.

> [!example]- Instance 2: BMAD-METHOD (independent emergence of same pattern)
>
> **Source:** [[src-bmad-method-agile-ai-development-framework|Synthesis: BMAD-METHOD — Agile AI-Driven Development Framework]]
>
> **Layer 1 — `project-context.md`:** A living "constitution" auto-loaded by all implementation workflows regardless of which agent persona is active. Contains project identity, tech stack, architectural decisions, and cross-cutting constraints. Analogous to AGENTS.md in function: always-on, cross-agent, project-universal.
>
> **Layer 2 — Agent persona files:** PM, Analyst, Architect, Developer/Amelia, UX Designer, Tech Writer, etc. Each persona has a distinct communication style, skill menu, and area of authority. These are tool-specific in the sense that they are BMAD-specific; they don't port to Copilot. They are always-on for their specific agent type, analogous to CLAUDE.md's per-tool delta role.
>
> **Layer 3 — Task workflow skills:** `bmad-brainstorming` (60+ named techniques), `bmad-quick-dev` (compressed intent-to-implementation), `bmad-prfaq` (5-stage coached PRFAQ workflow), `bmad-party-mode` (multi-agent deliberation). Each is a rich, detailed workflow that loads only when invoked. Some include script execution. In v6.3.0, Party Mode was consolidated into a single SKILL.md using real subagent spawning via the Agent tool.
>
> **Structural confirmation:** BMAD didn't adopt the three-layer architecture by copying Claude Code — it evolved the same structure independently from first principles of AI-driven agile development. The convergent emergence across two independent ecosystems confirms the pattern reflects a genuine constraint in AI agent context architecture, not tool-specific convention.

> [!example]- Instance 3: This wiki (post-refactor implementation, 2026-04-14)
>
> **Pre-refactor state (problem):**
> - Layer 1: Absent. No AGENTS.md. All cross-tool context lived in CLAUDE.md.
> - Layer 2: CLAUDE.md at 315 lines — a monolith doing all three jobs.
> - Layer 3: `.claude/skills/` correctly implemented with evolve, ingest, continue, build-model.
>
> **Post-refactor state (applied):**
> - **Layer 1 — AGENTS.md (159 lines)**: Universal cross-tool context. Sacrosanct directives, hard rules, stage gates, methodology models, page schema, quality gates. Read by any AI tool (Claude Code, Codex CLI, Copilot, Gemini, Cursor).
> - **Layer 2 — CLAUDE.md (107 lines, down from 315)**: Claude Code-specific overrides only. Identity profile, Claude-specific behaviors (skills, MCP, TodoWrite, plan mode), essential commands, flow per mode, 5 Claude-specific hard rules that extend AGENTS.md.
> - **Layer 3 — `.claude/skills/`**: Unchanged. Skills load on-demand per task.
>
> **Plus 5 thematic root files for separation of concerns:**
> - **CONTEXT.md** (227L) — identity profile, current state, active epics, constraints
> - **ARCHITECTURE.md** (585L) — data flow, tool topology, page schema, integration points
> - **DESIGN.md** (355L) — visual design principles, callout vocabulary, page layouts
> - **TOOLS.md** (806L) — complete CLI reference (pipeline, gateway, view, sync, MCP)
> - **SKILLS.md** (275L) — skills directory guide, format, extension hierarchy
>
> **Result:** 2,714 lines across 8 files vs 315 lines crammed into one. Each file has ONE responsibility. AGENTS.md slightly over the 100-line target (pragmatic — this is a complex system with many sacrosanct rules), CLAUDE.md slightly over 100 (107) but well below the 300-line ETH Zurich harm threshold. See [[root-documentation-map|Root Documentation Map]] for the full implementation map.

> [!example]- Instance 4: Cline (independent implementation, VS Code extension, 2026-04-15 evidence)
>
> **Source:** [[src-cline-agentic-coding-ide-extension|Synthesis — Cline — Agentic Coding IDE Extension]]
>
> **Layer 1 — AGENTS.md:** Cline added explicit AGENTS.md support (per changelog). Cross-tool universal standard adopted independently by a VS Code extension reaching millions of users. Direct ecosystem validation that AGENTS.md is not Claude-Code-specific — it's the emerging universal agent context standard.
>
> **Layer 2 — CLAUDE.md as pure imports:** Cline's own `CLAUDE.md` is three lines: `@.clinerules/general.md` + `@.clinerules/network.md` + `@.clinerules/cli.md`. This is a distinct composition pattern from the delta-overrides approach. The manifest aggregates separate concern-files via `@`-include syntax. Two legitimate composition patterns for Layer 2: **delta overrides** (our approach) and **manifest + imports** (Cline). Both valid, different trade-offs.
>
> **Layer 3 — `.agents/skills/`:** Folder-per-skill pattern with SKILL.md anchor. Example in repo: `.agents/skills/create-pull-request/SKILL.md`. Migration noted in changelog: "Move PR skill to .agents/skills" — Cline is actively aligning with the cross-tool `.agents/` convention that AGENTS.md implies.
>
> **Structural confirmation:** Cline's convergence is particularly strong evidence because (a) it's independently developed, (b) it's at consumer scale (millions of users), (c) it REVERSED design choices (strict plan mode became opt-in in v3.55) which shows the architecture was refined against real friction rather than imposed. The three-layer pattern is now validated across FOUR independent implementations at different scales and domains.

## When To Apply

> [!tip] Apply the three-layer pattern when:
>
> - Any project that uses AI coding agents — this is the universal case
> - Multiple AI tools exist or may be added (Copilot, Gemini, Claude, Codex — each wants context)
> - CLAUDE.md has grown beyond 100 lines (strong signal that Layer 1 and 3 content is being compressed into Layer 2)
> - Task performance feels inconsistent (possible signal that wrong context is loading unconditionally)
> - Team members ask "where does this instruction go?" — the three-layer decision tree answers this question structurally
>
> **Decision tree for any new piece of context:**
> 1. Is it true regardless of which AI tool executes the task? → Layer 1 (AGENTS.md)
> 2. Is it Claude Code–specific and always relevant? → Layer 2 (CLAUDE.md, keep minimal)
> 3. Is it task-specific, detailed, or workflow-heavy? → Layer 3 (SKILL.md)

## When Not To

> [!warning] Do NOT apply when:
>
> - **Single-use scripts or prototypes**: a one-off script doesn't need three-layer context architecture; just use a system prompt
> - **Projects with a single AI tool and no plans to add more**: if AGENTS.md portability is irrelevant, the overhead of maintaining a Layer 1/Layer 2 split is not justified
> - **Very small projects (<5 conventions to communicate)**: a 15-line CLAUDE.md is already an appropriate Layer 2 without needing a Layer 1
>
> **The most common over-application mistake:** creating an empty AGENTS.md just to "have" Layer 1 when all the content already fits in a lean CLAUDE.md. The pattern solves a real problem (context pollution, tool lock-in, performance degradation) — if those problems don't exist at your current scale, don't introduce complexity for theoretical future benefit.
>
> **The ETH Zurich warning:** An AI-generated Layer 1 AGENTS.md is measurably worse than no Layer 1 at all. If you let an AI scaffold your AGENTS.md, it will likely bloat it beyond the 100-line limit and fill it with generic instructions that add noise without adding signal. Write Layer 1 by hand. Keep it tight.

## Relationships

- INSTANCES IN: [[src-skillmd-claudemd-agentsmd-three-layer-context|Synthesis — SKILL.md vs CLAUDE.md vs AGENTS.md]]
- INSTANCES IN: [[src-bmad-method-agile-ai-development-framework|Synthesis: BMAD-METHOD — Agile AI-Driven Development Framework]]
- BUILDS ON: [[model-claude-code|Model — Claude Code]]
- BUILDS ON: [[model-skills-commands-hooks|Model — Skills, Commands, and Hooks]]
- RELATES TO: [[model-context-engineering|Model — Context Engineering]]
- RELATES TO: [[context-file-taxonomy|Context File Taxonomy — The 8 Dimensions of Agent Context]]
- RELATES TO: [[model-markdown-as-iac|Model — Markdown as IaC — Design.md and Agent Configuration]]
- RELATES TO: [[src-github-spec-kit-specification-driven-development|Synthesis — GitHub Spec Kit: Specification-Driven Development]]

## Backlinks

[[Synthesis — SKILL.md vs CLAUDE.md vs AGENTS.md]]
[[src-bmad-method-agile-ai-development-framework|Synthesis: BMAD-METHOD — Agile AI-Driven Development Framework]]
[[model-claude-code|Model — Claude Code]]
[[model-skills-commands-hooks|Model — Skills, Commands, and Hooks]]
[[model-context-engineering|Model — Context Engineering]]
[[context-file-taxonomy|Context File Taxonomy — The 8 Dimensions of Agent Context]]
[[model-markdown-as-iac|Model — Markdown as IaC — Design.md and Agent Configuration]]
[[src-github-spec-kit-specification-driven-development|Synthesis — GitHub Spec Kit: Specification-Driven Development]]
[[root-documentation-map|Root Documentation Map — Repository-Level Files]]
[[src-cline-agentic-coding-ide-extension|Synthesis — Cline — Agentic Coding IDE Extension with Plan/Act, Skills, Hooks, MCP]]
