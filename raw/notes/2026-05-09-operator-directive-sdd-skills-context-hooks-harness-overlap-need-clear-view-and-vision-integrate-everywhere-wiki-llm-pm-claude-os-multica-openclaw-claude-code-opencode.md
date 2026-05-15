---
title: "2026-05-09 — Operator directive (turn 3): SDD ↔ Skills ↔ Context/Context-Injection ↔ Hooks ↔ Harness overlap heavily; need clear view + vision + integration across Wiki LLM, PM tools, Claude OS, Multica, OpenClaw, Claude Code, OpenCode"
type: note
note_type: directive
domain: cross-domain
status: raw
confidence: high
created: 2026-05-09
updated: "2026-05-09"
sources:
  - id: operator-directive-2026-05-09-turn-3
    type: directive
    description: "Operator directive 2026-05-09 (turn 3 of E024 arc) — synthesis directive: the 5 abstractions (SDD, Skills, Context/Context-Injection, Hooks, Harness Engineering) overlap heavily and need unification; the unified view must enable integration across tools (Claude OS, Multica, OpenClaw, Claude Code, OpenCode) and across destinations (Wiki LLM, PM tools)"
tags: [operator-directive, sacrosanct, verbatim, "2026-05-09", sdd-skills-context-hooks-harness, unification-synthesis, integration-everywhere, multi-tool-portability, wiki-llm, pm-tools, claude-os, multica, openclaw, claude-code, opencode, ai-agents, raw-note]
---

# Operator directive — 2026-05-09 (turn 3): SDD ↔ Skills ↔ Context/Context-Injection ↔ Hooks ↔ Harness overlap need clear view + integration everywhere

## Verbatim (operator, sacrosanct)

> "In the end SDD and Skills workflow overlap a lot, then context and context-injection / hooks and harnesss engineering too but, what I mean is we need a clear view and vision on and about all this. continue
> Both need to be possible to use / integrate properly everywhere, Wiki LLM, PM management tools, etc.... Through whatever tool Claude OS, Multica, OpenClaw, Claude Code, OpenCode... continue"

## Decomposition

### A — The 5 overlapping abstractions
- **SDD (Spec-Driven Development)** — operator-doctrinal 2026-05-05 (see [[spec-driven-agentic-build-is-the-2026-convergent-pattern-prompts-are-first-class-artifacts|Lesson — Spec-Driven Convergence]]); 11-impact-area denotation. The SPEC programs the AI's behavior.
- **Skills workflow** — per [[skill-systems-orchestrator-plus-modular-child-skills-the-architecture-pattern-anthropic-wont-solve-for-you|Pattern — Skill Systems]] (just authored). Orchestrator + child skills wired by skill.md.
- **Context engineering / context-injection** — per [[model-context-engineering|Model — Context Engineering]] + the recent [[claude-code-hook-additionalcontext-is-event-specific-not-all-events-accept-it|hook output-channel validity lesson]]. WHAT the AI sees + WHEN it's injected.
- **Hooks** — per existing [[model-skills-commands-hooks|Model — Skills, Commands, Hooks]] + [[hook-architecture rules]]. Lifecycle-event-driven behavior modification.
- **Harness engineering** — root-ghostproxy work + OpenArms + OpenClaw + Multica runtime layer. The substrate that hosts the AI.

### B — Operator's observation: they overlap A LOT
- "SDD and Skills workflow overlap a lot" — both encode workflows declaratively
- "context and context-injection / hooks and harnesss engineering too" — context, hooks, harness all program substrate behavior
- The implication: distinct categories, but FOR THE PURPOSE OF a clear view, the operator needs ONE unified framing

### C — The directive
- "we need a clear view and vision on and about all this"
- "continue" — operator-authorized to keep going (strong-loop)
- Output expected: a UNIFICATION + INTEGRATION synthesis

### D — Integration scope: everywhere
- "Both need to be possible to use / integrate properly everywhere"
  - "Both" likely refers to: (1) the SDD/Skills/etc. abstractions; (2) the per-project Assistant Profile architecture from E024
- Destinations:
  - **Wiki LLM** (this project = the second-brain wiki)
  - **PM management tools** (Obsidian PM, Multica board, etc.)
  - "etc." (extensible — could include git platforms, dashboards, terminals, etc.)

### E — Tool spectrum
- "Through whatever tool"
- Named:
  - **Claude OS** (brobertsaz — the memory layer in T1 of comparison)
  - **Multica** (operator-adopted runtime in T3 of comparison)
  - **OpenClaw** (operator's own ecosystem project — runtime)
  - **Claude Code** (Anthropic — the CLI we run inside)
  - **OpenCode** (already in operator's stack memory 2026-04-23)
- "..." (extensible — Hermes, Codex, Gemini, Pi, Cursor Agent, Kimi, Kiro CLI per Multica's daemon list)

## The unification gap to fill

The wiki has SEPARATE models/patterns for each layer:
- SDD: [[spec-driven-agentic-build-is-the-2026-convergent-pattern-prompts-are-first-class-artifacts]]
- Skills: [[model-skills-commands-hooks]] + [[skill-systems-orchestrator-plus-modular-child-skills-the-architecture-pattern-anthropic-wont-solve-for-you]]
- Context: [[model-context-engineering]]
- Hooks: [[hook-architecture rules]] + [[claude-code-hook-additionalcontext-is-event-specific-not-all-events-accept-it]]
- Harness: scattered across openarms/openclaw/multica work

What's MISSING: a single synthesis page that shows
- HOW these 5 layers relate (Venn diagram + dimensions where they overlap)
- WHAT each provides uniquely
- HOW each is realized in each tool (5 layers × 5 tools matrix)
- WHICH layer to use when (decision tree / heuristic)
- HOW the E024 Per-Project Assistant Profile pattern bridges all 5
- HOW destinations (Wiki LLM, PM tools) consume the integrated view

## Action plan

| # | Action | Status |
|---|---|---|
| 1 | Log verbatim BEFORE acting (this file) | ✅ done |
| 2 | Author the unification concept page — "Declarative Agent Programming Spectrum" with 5-layer × 5-tool integration matrix + destination integration | pending |
| 3 | Cross-reference into existing models (model-context-engineering, model-skills-commands-hooks, spec-driven lesson) | pending |
| 4 | Update E024 Epic to reference the new spectrum page as the foundational synthesis | pending |
| 5 | Pipeline post + report | pending |

## No-conflate guard

- **"SDD and Skills overlap"** — overlap doesn't mean SAME. Both are declarative-spec-of-workflow but at different granularities: SDD is project/feature-level spec; Skills are atomic-action-level spec.
- **"context and context-injection / hooks and harness"** — three distinct overlapping things grouped. Context = what AI sees; injection = how it gets there; hooks = lifecycle-event mechanism for injection; harness = runtime that hosts the agent.
- **"need a clear view and vision"** — synthesis directive, not "build something new". The unification is a NEW KNOWLEDGE artifact that maps existing territory.
- **"integrate properly everywhere"** — the unified view must be USABLE across tools and destinations. The synthesis must be tool-agnostic (per the anti-vendor-lock-in mission).
- **"continue × 2"** — strong-loop authorization. Don't pause, don't over-survey, execute.
