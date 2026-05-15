---
title: "Pattern — Skill Systems: orchestrator skill + modular child skills wired by skill.md (the architecture that compounds — what Anthropic won't solve for you)"
type: pattern
domain: ai-agents
status: synthesized
confidence: high
maturity: seed
layer: 2
created: 2026-05-09
updated: "2026-05-09"
sources:
  - id: src-claude-os-skill-chaining-youtube
    type: video
    url: https://www.youtube.com/watch?v=RrMTtG1ZccI
    file: raw/transcripts/skill-chaining-in-claude-os-is-insane-dont-fall-behind.txt
    description: "YouTube — Skill Chaining in Claude OS is INSANE — primary empirical source for the Skill Systems pattern: orchestrator + modular child skills wired by skill.md, with the strategic frame that this is the ONE thing Anthropic won't solve for your business"
  - id: src-comparison-frontier
    type: wiki
    file: wiki/comparisons/assistant-platforms-and-frameworks-frontier-comparison-claude-os-obsidian-pm-multica-openclaw-command-center-2026-05-09.md
    description: "Frontier comparison surfacing this pattern as the recommended implementation pattern within the per-project Profile's Action Surface"
  - id: src-claude-os-repo
    type: file
    file: raw/articles/brobertsazclaude-os.md
    description: "Claude OS v2.5 skills library — 36+ community skills demonstrating the modular-skill-as-building-block discipline"
  - id: companion-profile-pattern
    type: wiki
    file: wiki/patterns/01_drafts/per-project-assistant-profile-pattern-tailored-config-to-spawn-ecosystem-runtimes.md
    description: "Companion pattern — Per-Project Assistant Profile. Skill Systems is one canonical implementation pattern within the Profile's Action Surface section"
  - id: existing-skills-commands-hooks-model
    type: wiki
    file: wiki/spine/models/agent-config/model-skills-commands-hooks.md
    description: "Existing model — Skills, Commands, Hooks. This pattern extends the skills layer with the orchestrator-plus-children composition pattern"
tags: [pattern, skill-systems, skills-architecture, orchestrator-pattern, modular-skills, anti-mega-skill, anti-isolated-skill, claude-os, claude-code, ai-agents, "2026-05-09", "draft", profile-action-surface]
---

# Pattern — Skill Systems: orchestrator + modular child skills

## Summary

A **Skill System** is the composition of one **orchestrator skill** with multiple **modular child skills**, wired together by the orchestrator's `skill.md` instruction set, to execute an end-to-end business workflow that no single skill could deliver alone. The orchestrator IS the brain (manages context flow, dispatches to child skills, aggregates results); the child skills ARE the reusable building blocks (small, focused, modular, progressive-disclosure-aware). This pattern is the architecture-of-choice for the part of an AI-coding workflow that **vendors won't solve for you**: the YouTube source (operator-shared 2026-05-09) argues persuasively that Anthropic will solve 8 of 9 limitations (memory, scheduled tasks, output separation, cross-channel access) themselves over the next few months, but the ONE thing they will not solve is **YOUR specific business workflows**. Skill Systems are how you turn a generalist model (Claude Opus 4.7 et al.) into a specialist indistinguishable from doing the work manually yourself. The pattern explicitly rejects two common failure modes — **isolated skills** (user is the intermediary between disconnected skills) and **mega skills** (one giant skill that loses modularity, maintainability, and progressive disclosure). Within the [[per-project-assistant-profile-pattern-tailored-config-to-spawn-ecosystem-runtimes|Per-Project Assistant Profile pattern]], Skill Systems is the canonical implementation pattern populating the Profile's **Action Surface** section.

## Pattern Description

A Skill System has three structural components that together form the "system":

| Component | Role | What lives here |
|---|---|---|
| **Orchestrator skill** | The brain — dispatches work, manages context flow, sequences child invocations, aggregates results | A `skill.md` with the orchestration logic, child-skill references, parameter passing, error-recovery prompts |
| **Child skills (multiple)** | The modular building blocks — each does ONE thing well | Per-child `skill.md` with focused logic, well-defined inputs/outputs, no embedded business logic from other concerns |
| **Shared context** | The substrate the system runs against | Brand voice, terminology, design system, learnings — accessible to ALL skills in the system without re-explaining |

The pattern enforces a parent-children relationship analogous to Claude Code's sub-agent pattern (operator has main instance, sub-agents handle context-sectioned work, return outputs).

## Instances

| Instance | Source | Notes |
|---|---|---|
| **Video → Short-form clips skill system** | Claude OS / Agentic Academy (per YouTube) | Orchestrator + child skills for transcription, clipping, captioning, format conversion |
| **Video → Long-form article skill system** | Claude OS / Agentic Academy | Orchestrator + shared transcription skill + content rewrite + humanizing + factcheck child skills |
| **Social carousel skill system** | Claude OS / Agentic Academy | Orchestrator + research + writing + factcheck + humanizing + slide-generation child skills |
| **HTML slide generation skill system** | Claude OS / Agentic Academy | Orchestrator + design-system + slide-renderer + export child skills |
| **Skill System Creator** (meta-skill) | Claude OS / Agentic Academy | A skill system that BUILDS skill systems from existing skills — single-line install per user |
| **this-project knowledge curation skill system** (planned) | E024 (this Epic) | Orchestrator + ingest + synthesize + cross-ref + maturity-promote child skills |
| **this-project session-checkin skill system** (planned) | E024 (this Epic) | Orchestrator + gateway-orient + recent-directives + pipeline-status + decisions-survey child skills |

## When To Apply

> [!success] **Apply Skill Systems when**
>
> 1. You have a multi-step business workflow that no single skill could deliver
> 2. The child skills are independently useful (would be reused across other workflows)
> 3. The workflow needs maintainability — copywriting style changes shouldn't require editing 5 different skills
> 4. You want **progressive disclosure** — Claude Code's context-loading optimization only kicks in when skills are scoped, not when one mega-skill loads all context
> 5. You're investing in the part Anthropic won't solve: your specific business workflows

## When Not To

> [!warning] **DO NOT apply Skill Systems when**
>
> 1. **Single-shot ad-hoc question** — direct `claude` interactive use, no orchestration needed
> 2. **One-time scripts** — use `claude -p` directly, no Profile/Skill abstraction
> 3. **Dashboard-only work** — the YouTube source's central warning: don't invest in dashboards because Anthropic will subsume them (see Claude desktop + new agents view + scheduled tasks + cross-channel access)
> 4. **Memory / context recall** — Anthropic is solving this (project context, memory features); Skill Systems are not the right layer
> 5. **Output formatting / asset routing** — Anthropic will change how outputs are displayed (already underway in desktop app); not skill-territory

## Anti-Patterns (from the YouTube source)

### Anti-Pattern 1: Isolated Skills (manual chaining)

```
User asks Claude (skill 1: copywriting): "write a LinkedIn post about X"
  → Claude writes draft
  → User copies draft
  → User asks Claude (skill 2: scheduling): "schedule this for tomorrow"
  → Claude schedules
```

> [!warning] **Why bad**: the USER is the intermediary between skill 1 and skill 2 — that's manual chaining, defeating orchestration entirely. The "skills" are not a system; they're isolated tools.

### Anti-Pattern 2: Mega Skills (over-correction)

```
ONE skill.md containing: research + writing + repurposing + scheduling + posting + factcheck + humanizing
```

> [!warning] **Why bad**:
> - **Loses modularity** — copywriting logic locked inside one giant flow; can't reuse for emails / newsletters / landing pages
> - **Loses maintainability** — to change copy style, you edit it in 5 different mega-skills (email-mega-skill, newsletter-mega-skill, social-mega-skill...)
> - **Loses progressive disclosure** — Anthropic designed skills to load only the context needed; mega-skills load everything, causing quality drop
> - **Feels faster the first time** — and is, but every subsequent reuse costs 10x more

### ✅ The fix: Skill Systems

> [!success] **Pattern**: orchestrator + modular child skills wired together
>
> ```
> Orchestrator (skill.md = instruction set)
>   ├── Child skill: research
>   ├── Child skill: copywriting          ← REUSABLE across LinkedIn / email / newsletter
>   ├── Child skill: scheduling
>   ├── Child skill: factchecking         ← REUSABLE across content types
>   └── Child skill: humanizing           ← REUSABLE — your brand voice
> ```
>
> The orchestrator's `skill.md` chains child skills together end-to-end. Information flows: orchestrator → child → orchestrator (aggregating) → next child → ...

## Architecture Diagram

```
┌────────────────────────────────────────────────────────────────┐
│  SHARED CONTEXT (brand voice, learnings, design system, etc.)  │
└─────────────────────┬──────────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────────┐
│  ORCHESTRATOR SKILL (skill.md = instruction set)                 │
│  - Knows the end-to-end workflow                                  │
│  - Dispatches to child skills in sequence/parallel                │
│  - Aggregates returns into final output                           │
│  - Handles error recovery                                         │
└────┬───────────────┬───────────────┬────────────────┬───────────┘
     ▼               ▼               ▼                ▼
 ┌────────┐    ┌─────────┐    ┌──────────┐    ┌──────────┐
 │ CHILD  │    │  CHILD  │    │  CHILD   │    │  CHILD   │
 │ SKILL  │    │  SKILL  │    │  SKILL   │    │  SKILL   │
 │  1     │    │   2     │    │    3     │    │    4     │
 └────────┘    └─────────┘    └──────────┘    └──────────┘
   (one     (one      (one         (one
    job)     job)      job)         job)
```

## The Compounding Effect

When you update a single child skill (say, **fact-checking**), **every system that uses it** automatically gets better. With 4 skill systems using factchecking:

| Update factchecking once → | Improvement |
|---|---|
| Video-to-short-form system | ↑ better (uses factcheck) |
| Video-to-article system | ↑ better (uses factcheck) |
| Social-carousel system | ↑ better (uses factcheck) |
| HTML-slide-generation system | ↑ better (uses factcheck) |

This is the architectural payoff. The 5th, 10th, 50th skill system you build benefits from skills you've already built.

## How To Apply

1. **Identify the end-to-end workflow** you need (e.g., "operator submits raw note → wiki gets validated synthesis page → cross-references propagated"). The orchestrator's job is this end-to-end.
2. **Decompose into single-purpose child skills** — each child does ONE thing. Use the question: "would this skill be reusable in OTHER workflows?" If yes, it's a child skill. If no, it might be orchestrator logic.
3. **Author each child skill** as its own `skill.md` with clear inputs, outputs, and scope. Resist embedding cross-skill business logic.
4. **Author the orchestrator skill** as its own `skill.md` with the workflow logic. The orchestrator references child skills by name, doesn't reimplement their logic.
5. **Define shared context** (brand voice, terminology, design system) as accessible substrate the orchestrator + child skills can both reach without re-explaining.
6. **Test the system end-to-end** — invoke the orchestrator with realistic input; verify the chain produces correct output.
7. **Iterate the child skills** as needs evolve — every system using the improved child benefits automatically.
8. **Build a Skill System Creator** (meta-skill) when you have several skill systems — to scaffold new ones in the same shape.

## Integration with E024 Per-Project Assistant Profiles

Within the [[per-project-assistant-profile-pattern-tailored-config-to-spawn-ecosystem-runtimes|Per-Project Assistant Profile pattern]] (E024), Skill Systems is the **canonical implementation pattern populating the Profile's Action Surface section**:

| Profile section | Skill-System mapping |
|---|---|
| **Identity** | Skill System name + version + project + owner |
| **Knowledge Scope** | Shared context substrate (brand voice, learnings, design system, wiki paths, MCP servers) |
| **Action Surface** | **The Skill Systems** — orchestrator + child skills the assistant can invoke |
| **Model Routing** | Orchestrator-level model preferences; child skills may have different model needs |
| **Prompt Templates** | System prompt for the orchestrator + per-child error-recovery prompts |
| **Success Criteria** | Each Skill System's end-to-end output; child skill telemetry |

This means: **Profile = identity + scope spec; Skill Systems = the Action Surface implementation**.

## Strategic Frame (the "Why Anthropic Won't Solve This For You")

> [!info] **The investment thesis from the YouTube source**
>
> Anthropic ships a model that's a good generalist (Claude Opus 4.7). Anthropic can't ship a model that's brilliant at YOUR specific copywriting style, YOUR client onboarding process, YOUR meta-ads composition — because the moment they specialize, they make the product worse for everyone else.
>
> **The wedge**: between a good-generalist output (driven by the model) and YOUR exact-output-needed (driven by your business). Skills + Skill Systems are how you close that wedge.
>
> **Where to invest engineering time**: in this wedge. Not in dashboards (Anthropic will absorb), not in memory (Anthropic will absorb), not in scheduling (Anthropic will absorb). In skills that turn the generalist into your specialist.

This aligns with the operator-stated doctrine: *"Pull the level from the frontier and remain independant"* (2026-05-09). The Skill System architecture is exactly that — pull the model from the frontier, encode YOUR specific workflows in skills, stay independent of the dashboard / harness / orchestration the vendor ships.

## Sister-Project Applicability

| Project | Skill Systems applicable? | Example |
|---|---|---|
| **this project (the research wiki)** | YES — knowledge curation, methodology stewardship, source ingestion as orchestrator + child skill systems | Ingest System: orchestrator + fetch + read-full + synthesize + cross-ref + pipeline-post child skills |
| **OpenArms** | YES — fleet-agent runtime, harness compliance, methodology enforcement | Methodology Enforcement System: orchestrator + stage-detect + boundary-check + violation-report child skills |
| **OpenFleet** | YES — fleet orchestration, task dispatch | Task Dispatch System: orchestrator + agent-select + context-package + handoff + heartbeat child skills |
| **AICP** | YES — local-AI complexity routing, $0 target | Routing System: orchestrator + complexity-detect + tier-select + backend-call + fallback child skills |
| **devops-control-plane** | YES — infrastructure governance, decision tracking | Decision System: orchestrator + state-detect + adr-render + approval-gate + audit child skills |
| **root-ghostproxy** | YES — harness/ecosystem maintenance, global config propagation | Propagation System: orchestrator + sister-detect + delta-compute + apply + verify child skills |
| **Hermes** | YES (once integrated) | Hermes-runtime-specific Skill Systems |

## Anti-Patterns

| Anti-pattern | Why bad |
|---|---|
| One mega-skill containing the entire workflow | Loses modularity, maintainability, progressive disclosure |
| Disconnected/isolated skills with user manually chaining | User is the intermediary — defeats the system |
| Orchestrator that re-implements child skill logic | Duplication; child skills become dead code |
| Child skill that depends on context from another child without going through orchestrator | Hidden coupling; breaks reusability |
| Building dashboards instead of skill systems | Investing where Anthropic will subsume (per video) — wasted engineering time |
| No shared context substrate | Every skill re-asks for brand voice / design system / learnings — repeated tax |
| No telemetry on child skill outputs | Can't optimize what isn't measured; Profile Success Criteria can't be validated |

## Relationships

- BUILDS ON: [[model-skills-commands-hooks|Model — Skills, Commands, Hooks]] — the foundational mechanism-determinism model; Skill Systems is the orchestrator-plus-children composition pattern on top of skills layer
- BUILDS ON: [[assistant-platforms-and-frameworks-frontier-comparison-claude-os-obsidian-pm-multica-openclaw-command-center-2026-05-09|Comparison — Assistant Platforms Frontier]] — Claude OS skills library + YouTube transcript = the empirical source for this pattern
- COMPLEMENTS: [[per-project-assistant-profile-pattern-tailored-config-to-spawn-ecosystem-runtimes|Pattern — Per-Project Assistant Profile]] — Skill Systems IS the canonical Action Surface implementation pattern within the Profile pattern
- DEMONSTRATES: [[anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence|Lesson — Anti-Vendor-Lock-In]] — Skill Systems are runtime-agnostic (work on any LLM); embodying the "pull from frontier, stay independent" doctrine
- DEMONSTRATES: [[infrastructure-over-instructions-for-process-enforcement|Principle 1 — Infrastructure Over Instructions]] — Skills + Systems are structural (file-based, validated, composable), not prose
- DEMONSTRATES: [[structured-context-governs-agent-behavior-more-than-content|Principle 2 — Structured Context Governs Agent Behavior]] — skill.md format + orchestrator dispatch = programmatic context-flow

## Cross-references

- YouTube primary source: `raw/transcripts/skill-chaining-in-claude-os-is-insane-dont-fall-behind.txt`
- Claude OS repo evidence: `raw/articles/brobertsazclaude-os.md`
- Frontier comparison: `wiki/comparisons/assistant-platforms-and-frameworks-frontier-comparison-claude-os-obsidian-pm-multica-openclaw-command-center-2026-05-09.md`
- Profile pattern (companion): `wiki/patterns/01_drafts/per-project-assistant-profile-pattern-tailored-config-to-spawn-ecosystem-runtimes.md`
- Skills mechanism model: `wiki/spine/models/agent-config/model-skills-commands-hooks.md`

## Backlinks

[[Model — Skills, Commands, Hooks]]
[[Comparison — Assistant Platforms Frontier]]
[[Pattern — Per-Project Assistant Profile]]
[[Lesson — Anti-Vendor-Lock-In]]
[[infrastructure-over-instructions-for-process-enforcement|Principle 1 — Infrastructure Over Instructions]]
[[structured-context-governs-agent-behavior-more-than-content|Principle 2 — Structured Context Governs Agent Behavior]]
