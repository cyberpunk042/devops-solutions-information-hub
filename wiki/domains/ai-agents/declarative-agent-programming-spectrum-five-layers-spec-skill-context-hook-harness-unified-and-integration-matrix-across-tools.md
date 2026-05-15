---
title: "Concept — The Declarative Agent Programming Spectrum: 5 layers (SDD · Skills · Context/Context-Injection · Hooks · Harness) unified, with integration matrix across tools (Claude OS · Multica · OpenClaw · Claude Code · OpenCode · Hermes · Codex · Gemini) and destinations (Wiki LLM · PM tools)"
type: concept
domain: ai-agents
status: synthesized
confidence: high
maturity: seed
created: 2026-05-09
updated: "2026-05-09"
sources:
  - id: operator-directive-2026-05-09-turn-3
    type: directive
    file: raw/notes/2026-05-09-operator-directive-sdd-skills-context-hooks-harness-overlap-need-clear-view-and-vision-integrate-everywhere-wiki-llm-pm-claude-os-multica-openclaw-claude-code-opencode.md
    description: "Operator directive 2026-05-09 turn 3 — synthesis call: SDD/Skills/Context/Hooks/Harness overlap heavily; need a clear view + vision; must integrate everywhere (Wiki LLM, PM tools) across all tools"
  - id: src-sdd-convergence-lesson
    type: wiki
    file: wiki/lessons/02_synthesized/spec-driven-agentic-build-is-the-2026-convergent-pattern-prompts-are-first-class-artifacts.md
    description: "Lesson — Spec-Driven Convergence: 9 instances + 11-impact-area denotation. SDD layer of the spectrum."
  - id: src-skills-systems-pattern
    type: wiki
    file: wiki/patterns/01_drafts/skill-systems-orchestrator-plus-modular-child-skills-the-architecture-pattern-anthropic-wont-solve-for-you.md
    description: "Pattern — Skill Systems: orchestrator + child skills. Skills layer of the spectrum."
  - id: src-context-engineering-model
    type: wiki
    file: wiki/spine/models/depth/model-context-engineering.md
    description: "Existing model — Context Engineering. Context/Context-Injection layer of the spectrum."
  - id: src-skills-commands-hooks-model
    type: wiki
    file: wiki/spine/models/agent-config/model-skills-commands-hooks.md
    description: "Existing model — Skills, Commands, Hooks. Hooks layer of the spectrum + the existing mechanism-determinism framing."
  - id: src-hook-output-channel-validity
    type: wiki
    file: wiki/lessons/01_drafts/claude-code-hook-additionalcontext-is-event-specific-not-all-events-accept-it.md
    description: "Lesson — Hook output-channel validity. Hooks-layer constraint that the spectrum surfaces."
  - id: src-comparison-frontier
    type: wiki
    file: wiki/comparisons/assistant-platforms-and-frameworks-frontier-comparison-claude-os-obsidian-pm-multica-openclaw-command-center-2026-05-09.md
    description: "Frontier comparison — Claude OS · Obsidian PM · Multica · OCMC. Provides the tool-axis for the integration matrix."
  - id: src-per-project-profile-pattern
    type: wiki
    file: wiki/patterns/01_drafts/per-project-assistant-profile-pattern-tailored-config-to-spawn-ecosystem-runtimes.md
    description: "Pattern — Per-Project Assistant Profile. Bridges all 5 layers via its 6 schema sections + runtime targets."
  - id: epic-e024
    type: wiki
    file: wiki/backlog/epics/milestone-v2/e024-per-project-assistant-configurations-to-capture-programmatic-credit-and-enable-ecosystem-spawn.md
    description: "Parent Epic E024 — the operationalization of this spectrum via per-project Profiles."
tags: [concept, declarative-agent-programming, spectrum-of-abstractions, sdd, skills, context-engineering, context-injection, hooks, harness-engineering, unification, integration-matrix, claude-os, multica, openclaw, claude-code, opencode, hermes, ai-agents, "2026-05-09", synthesized]
---

# Concept — The Declarative Agent Programming Spectrum

> [!warning] **2026-05-09 refactor**: This concept was originally written with 5 layers (SDD · Skills · Context · Hooks · Harness). Operator correction 2026-05-09 turn 4: *"we see more, commands, hooks, agents brain files, etc..."* — the spectrum is wider. Now 7 layers (L0 Agents Brain Files · L1 SDD · L2 Skills · L3 Commands · L4 Context/Injection · L5 Hooks · L6 Harness). "etc." remains open — additional layers may surface (e.g., MCP server design as its own layer, telemetry config, governance gates).

## Summary

A unification concept that resolves the operator's 2026-05-09 observation — *"SDD and Skills workflow overlap a lot, then context and context-injection / hooks and harnesss engineering too"* + *"but we see more, commands, hooks, agents brain files, etc..."* — into **7 distinct-but-overlapping layers** of a single underlying activity: **declaratively programming an AI agent's behavior**. The 7 layers, ordered from **most foundational / always-loaded** to **most operational / runtime-bound**, are: **(L0) Agents Brain Files** — CLAUDE.md / AGENTS.md / RULES — the always-loaded foundational config that programs agent identity + ambient context · **(L1) SDD (Spec-Driven Development)** — the project/feature-level spec documents that program what the agent will build · **(L2) Skills (Skill Systems)** — the atomic-action-level spec that programs what the agent can do · **(L3) Commands** — slash-invoked operator-typed deterministic workflows (`.claude/commands/`) · **(L4) Context / Context-Injection** — what the agent SEES at inference time and how that information is delivered · **(L5) Hooks** — lifecycle-event-driven behavior modification · **(L6) Harness Engineering** — the runtime substrate that hosts the agent. All 7 layers are **declarative** (text/yaml/markdown files, not imperative code) and all 7 program agent behavior — they differ in WHEN they fire, WHAT they program, and WHERE they live. The layers compose; per-project Profiles span across them but DO NOT collapse them into one tool's config (operator-doctrinal 2026-05-09: *"A PROFILE IS WAY MORE THAN JUST SETTING FOR ONE TOOL"*). The pattern is **tool-agnostic by design**: each tool (Claude Code · Claude OS · Multica · OpenClaw · OpenCode · Hermes Agent · Codex · Gemini · etc.) supports each layer through different native mechanisms. Destinations (Wiki LLM, PM tools, public Obsidian — *every surface*) consume the integrated output flexibly + compatibly.

## The 7 Layers — Defined

### Layer 0: Agents Brain Files

> [!info] **Layer 0 — Agents Brain Files: the always-loaded foundational config that programs agent identity + ambient context**
>
> Examples: CLAUDE.md (Claude Code), AGENTS.md (universal cross-tool), RULES files, CONTEXT.md (this project), per-project conventions docs.

**Granularity**: foundational / ambient (always-loaded)
**Lifecycle**: persists across every invocation; agent's "identity layer"
**File form**: markdown at well-known paths (CLAUDE.md / AGENTS.md / RULES / etc.)
**Programs**: WHO the agent IS, HOW it works, WHAT it must never forget
**When it fires**: ambient — every reasoning step has these loaded
**Mechanism**: harness auto-loads at session start; remains in context throughout
**Operator-named**: *"agents brain files"* (2026-05-09 turn 3)
**Distinction from L4 Context**: brain files are constitutive (define identity); context is informational (what's accessible at inference)

### Layer 1: SDD (Spec-Driven Development)

> [!info] **Layer 1 — SDD: the project/feature-level spec that programs what the agent will build**
>
> See: [[spec-driven-agentic-build-is-the-2026-convergent-pattern-prompts-are-first-class-artifacts|Lesson — Spec-Driven Convergence]]

**Granularity**: project/feature scope (large)
**Lifecycle**: persists across many invocations
**File form**: markdown spec documents (requirements-spec, ADR, design-plan, etc.)
**Programs**: WHAT to build, in what order, with what acceptance criteria
**When it fires**: at every agent action during the feature work
**Mechanism**: agent reads the spec; spec is a binding artifact (per methodology — requirements-spec is class=document, must-be-binding)
**Operator-doctrinal**: *"we prone spec driven development and a strong methodology and standards"* (2026-05-05); 11-impact-area denotation captured in lesson

### Layer 2: Skills (Skill Systems)

> [!info] **Layer 2 — Skills: the atomic-action-level spec that programs what the agent can do**
>
> See: [[skill-systems-orchestrator-plus-modular-child-skills-the-architecture-pattern-anthropic-wont-solve-for-you|Pattern — Skill Systems]]; [[model-skills-commands-hooks|Model — Skills, Commands, Hooks]]

**Granularity**: workflow / repeatable-task (medium)
**Lifecycle**: persists across many invocations, composable
**File form**: `skill.md` per skill (orchestrator + children); skill library on disk
**Programs**: HOW the agent executes specific actions; reusable building blocks
**When it fires**: when agent invokes the skill via name match (description-triggered) or explicit `/skill-name`
**Mechanism**: skill description triggers loading; orchestrator chains child skills; progressive disclosure of context
**Determinism**: ~70% per operator-stated determinism ladder (skills auto-trigger but not 100% reliable)

### Layer 3: Commands

> [!info] **Layer 3 — Commands: slash-invoked deterministic operator-typed workflows**
>
> See: [[model-skills-commands-hooks|Model — Skills, Commands, Hooks]] for the mechanism-determinism positioning (Commands = 100% deterministic per operator 2026-04-24).

**Granularity**: workflow (medium — same as skills, but operator-explicit)
**Lifecycle**: persists; invoked when operator types `/<name>`
**File form**: `.claude/commands/<name>.md` (or equivalent per tool)
**Programs**: WHAT happens when operator deliberately invokes the named workflow
**When it fires**: 100% on operator slash-invocation; never auto-triggered
**Mechanism**: harness reads the command file when slash invoked; executes the workflow
**Determinism**: **100%** — strongest of any layer per operator's determinism ladder
**Distinction from L2 Skills**: skills auto-trigger by description-match (~70%); commands are operator-explicit slash-invocation (100%)

### Layer 4: Context / Context-Injection

> [!info] **Layer 3 — Context: what the agent SEES at inference time; Context-Injection: how it gets there**
>
> See: [[model-context-engineering|Model — Context Engineering]]; [[claude-code-hook-additionalcontext-is-event-specific-not-all-events-accept-it|Lesson — Hook output channel is event-specific]]

**Granularity**: prompt-token level (small — fits in context window)
**Lifecycle**: per-inference (one model call)
**File form**: system prompt, CLAUDE.md, AGENTS.md, MCP context, embedded knowledge, RAG retrievals
**Programs**: WHAT information the agent has access to during reasoning
**When it fires**: at every inference call (continuous)
**Mechanism**: ambient (always-loaded files), on-demand (MCP/RAG retrieval), injection (hooks adding text mid-flow)
**Channel constraints**: per the hook validity lesson — `hookSpecificOutput.additionalContext` valid ONLY for 6 events (SessionStart, UserPromptSubmit, PreToolUse, PostToolUse, PostToolBatch, SubagentStart); other events use `systemMessage` or plain stdout

### Layer 5: Hooks

> [!info] **Layer 4 — Hooks: lifecycle-event-driven behavior modification**
>
> See: [[model-skills-commands-hooks|Model — Skills, Commands, Hooks]]; `.claude/rules/hook-architecture.md`

**Granularity**: event-trigger (deterministic)
**Lifecycle**: per-event (e.g., PreToolUse, PostCompact)
**File form**: shell/Python scripts under `.claude/hooks/`; settings.json wiring
**Programs**: BLOCK / MODIFY / INJECT at specific lifecycle moments
**When it fires**: at the configured lifecycle event (insertion point)
**Mechanism**: Claude Code runs the hook script; script returns JSON with channel-event-specific shape; exit code 2 blocks
**Determinism**: 100% on the lifecycle event firing; logical (block + reason + remediation) per hook design pattern
**Schema constraint**: output channels are event-specific (Layer 3 lesson)

### Layer 6: Harness Engineering

> [!info] **Layer 5 — Harness: the runtime substrate that hosts the agent**
>
> See: root-ghostproxy SFIF rollout · OpenArms v10 enforcement · Multica daemon · OpenClaw runtime · Claude Code itself

**Granularity**: runtime / OS-substrate (broad)
**Lifecycle**: continuous (the harness runs the agent)
**File form**: harness binaries, config files, env vars, system-level wiring (root-ghostproxy: `$HOME/.claude/`, IPS modules; Multica: daemon + workspace; etc.)
**Programs**: WHERE the agent runs, WHICH model provider, WITH WHAT environment, GATED BY WHAT enforcement
**When it fires**: at every agent invocation (everything passes through the harness)
**Mechanism**: harness intercepts CLI calls / routes provider requests / enforces policies / streams telemetry
**Examples per tool**:
- **Claude Code** = Anthropic-shipped harness (terminal CLI + IDE extension + desktop app)
- **Multica** = open-source managed-agents platform (Go+Postgres+pgvector daemon) wrapping 10+ CLIs
- **OpenClaw** = harness for autonomous agentic workflows
- **OpenCode** = alternative CLI harness
- **root-ghostproxy** = OS-root harness propagating to all projects (per memory 2026-05-06)

## Key Insights

1. **All 5 abstractions are declarative agent-behavior programming** — just at different granularities (project → action → token → event → runtime). The operator's overlap-observation is correct because they all share that root activity.

2. **The 5 layers compose, not replace** — a real per-project Assistant needs all 5. Stopping at 3 produces a partial Profile.

3. **Tool mechanism differs, abstraction holds** — Claude OS's memory MCP and Multica's workspace context are different L3 mechanisms for the same L3 layer. Design at the abstraction; compile per tool.

4. **Multica is a meta-harness** — uniquely spans L5 across multiple harnesses (10+ CLIs). This makes it the integration point.

5. **MCP is the L3 convergence standard** — every tool supports MCP. Per-project MCP servers (research-wiki, code-forge, memory) are reusable across all tools.

6. **L4 Hooks have the lowest cross-tool portability** — Claude Code's hook architecture is most documented; other tools are less formal. Cross-tool hook portability requires the schema-validity discipline (per the recent lesson).

7. **E024 Per-Project Profile is the unification artifact** — its 6 schema sections map 1-to-1 onto the 5 layers, providing the runtime-agnostic spec.

## Deep Analysis

### Why "overlap a lot" is the right intuition

The operator's observation reflects an underlying truth: declarative agent programming has multiple legitimate granularities, and a workflow can be expressed at any of them. **A copywriting workflow** could be:
- A Skill (`copywriting.md`) — Layer 2
- A Context-injected style guide (`/CONTEXT.md` lines on brand voice) — Layer 3
- A Hook (PreToolUse hook intercepting tool calls to inject brand-voice prompt) — Layer 4
- An SDD spec for a copywriting feature (`copywriting-feature.requirements-spec.md`) — Layer 1
- A Harness-level config (Multica agent profile for copywriting) — Layer 5

The same workflow expressed at any layer can produce similar agent outputs. THIS is the overlap. The differentiator is: **at what granularity should the workflow live?** The decision heuristic above answers that.

### Why the integration matrix matters

The matrix shows that **no single tool implements all 5 layers equally well**. Claude Code has the strongest L4 Hooks. Claude OS has the strongest L3 Memory MCP. Multica has the strongest L5 (10-CLI meta-harness). Obsidian PM (T2 from comparison) has the strongest L1 SDD persistence (plain Markdown in vault).

The implication: **a maximally-functional per-project Assistant uses each tool's strongest layer**. The Profile pattern enables this by being runtime-agnostic — the same Profile compiles to Multica for L5, optionally Claude OS for L3 memory enhancement, and so on.

### Why tool-agnostic design is mission-aligned

The [[anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence|anti-vendor-lock-in mission claim]] requires every stack layer to have paper evidence of alternatives. The spectrum's tool-agnostic abstraction layer IS that evidence — by designing at the 5-layer abstraction, any tool can be swapped without re-authoring the Profile.

This is the operator's *"Pull the level from the frontier and remain independant"* doctrine applied to agent-behavior programming.

## The Overlap (Why the Operator's Observation Is Correct)

```
                  ┌─────────────────────────────────────┐
                  │     DECLARATIVE AGENT BEHAVIOR       │
                  │   (5 layers, one underlying activity)│
                  └─────────────────────────────────────┘
                                     │
        ┌────────────────────────────┼────────────────────────────┐
        ▼                            ▼                            ▼
   ┌─────────┐                ┌──────────────┐              ┌─────────────┐
   │   SDD   │ ◄─ overlap ─► │   Skills    │ ◄─ overlap ─►│   Context   │
   │ (spec)  │               │ (skill.md)  │              │ (sys prompt)│
   └─────────┘                └──────────────┘              └─────────────┘
        │                            │                            │
        │      ┌────────────────────┘                            │
        ▼      ▼                                                  ▼
   ┌─────────────┐                                          ┌─────────────┐
   │   Hooks     │ ◄────────── overlap (hooks inject     ──►│  Harness    │
   │ (lifecycle) │              context via Layer 3)      │ (runtime)   │
   └─────────────┘                                          └─────────────┘
```

**Where they overlap:**

| Pair | Overlap mechanism |
|---|---|
| **SDD ↔ Skills** | Both are declarative workflow specs. SDD = project/feature; Skills = atomic action. A skill can be an SDD implementation step; an SDD spec can drive skill selection. |
| **Skills ↔ Context** | Skills inject specific context when triggered (progressive disclosure). The skill IS context-shaping at trigger-time. |
| **Context ↔ Hooks** | Hooks are the mechanism for injecting context at lifecycle events. Per Layer 4 schema, the `additionalContext` channel only works for 6 events. |
| **Hooks ↔ Harness** | Harness defines which lifecycle events exist + how hooks register. Different harnesses (Claude Code, Multica, OpenClaw) expose different hook event names. |
| **Harness ↔ SDD** | Harness reads the SDD spec at boot and propagates context. CLAUDE.md / AGENTS.md / rules files all live in the harness layer but are SDD artifacts. |

**Where they're distinct:**

| Aspect | SDD | Skills | Context | Hooks | Harness |
|---|---|---|---|---|---|
| **Granularity** | feature | action | token | event | runtime |
| **Persistence** | long-lived | reusable | per-inference | per-event | continuous |
| **File form** | markdown spec | skill.md | sys prompt + RAG | shell/python script | binary + config |
| **Author** | engineer | engineer | engineer + agent | engineer | platform |
| **Programs** | what to build | what agent can do | what agent sees | block/modify | where it runs |

## The 5-Layer × N-Tool Integration Matrix

> [!success] **Same 5 layers; each tool provides its own mechanism for each. Pick the mechanism that fits the tool; the Profile pattern (E024) is the runtime-agnostic spec that compiles to any of them.**

| Layer | **Claude Code** | **Claude OS** (brobertsaz) | **Multica** | **OpenClaw** | **OpenCode** | **Hermes** | **Codex / Cursor / Gemini / Kimi / Kiro** |
|---|---|---|---|---|---|---|---|
| **L1 SDD** | CLAUDE.md + AGENTS.md + `.claude/rules/` + spec docs in repo | Knowledge Base (RAG) entries + memory MCP tracked decisions | Issues + Skills + workspace docs | Skills + agent config | Similar to Claude Code (CLAUDE.md / AGENTS.md adoption) | Inherits from Multica integration (TBD specifics) | Each adopts its own conventions; all use markdown/yaml |
| **L2 Skills** | `.claude/skills/<name>/SKILL.md` per skill (Anthropic native) | Smithery skills library (36+ community); skill.md | Multica skills system (workspace-scoped, agent-invocable) | OpenClaw skills | OpenCode skills | Hermes skills (via Multica) | Per-tool skill mechanism; converging on skill.md format |
| **L3 Context / Injection** | system prompt + CLAUDE.md preload + MCP tool results + hook `additionalContext` injection | Real-Time Learning (Redis pub/sub) + Memory MCP + Semantic KB | Workspace docs + agent system prompt + custom_env + MCP wiring | OpenClaw context injection | OpenCode context | Hermes context | All use system prompt + RAG + MCP retrieval |
| **L4 Hooks** | `.claude/settings.json` `hooks` block (8 events: PreToolUse, PostToolUse, SessionStart, PostCompact, PreCompact, UserPromptSubmit, Stop, etc.) | Limited (Real-Time Learning IS hook-like — Redis pub/sub captures conversation events) | Daemon-level events; per-agent hooks (TBD specifics) | OpenClaw hook system | OpenCode hooks (similar shape to Claude Code) | Hermes hooks (via Multica) | Varies; Claude Code's model is reference |
| **L5 Harness** | The `claude` CLI itself (+ desktop app + IDE extensions) | Runs ON TOP of Claude Code (not a harness — it's a memory layer) | Multica daemon = the harness (auto-detects 10+ CLIs, schedules, monitors) | OpenClaw daemon | OpenCode CLI | Hermes CLI | Each tool IS its own harness |

**Key cross-cutting observations from the matrix:**

1. **Claude Code is the harness; the others sit either ON TOP (Claude OS extends memory) or BESIDE (Multica wraps multiple CLIs)** — operator's harness landscape is layered, not flat.

2. **Multica is unique in spanning Layer 5 across multiple harnesses** — Multica's daemon auto-detects Claude Code + OpenClaw + OpenCode + Hermes + Codex + Cursor + Gemini + Kimi + Kiro CLI. It's a meta-harness.

3. **SKILL.md format is converging across tools** — Anthropic ships `.claude/skills/<name>/SKILL.md`; Claude OS uses skill.md; Multica's skills system uses similar shape. The format is becoming a de-facto standard.

4. **L4 Hooks vary most across tools** — Claude Code's hook architecture (8 events × output-channel-validity) is the most documented; other tools have hooks but less formalized. Cross-tool hook portability is LOW.

5. **L3 Context/Injection converges via MCP** — MCP is the cross-tool standard for context retrieval and tool invocation. Every tool supports MCP; the per-project MCP servers (research-wiki, code-forge, memory) are reusable across tools.

## Destination Integration (Wiki LLM · PM Tools · etc.)

> [!info] **The 5 layers produce artifacts that flow into destinations. Different destinations consume different layer outputs.**

| Destination | Consumes | Mechanism |
|---|---|---|
| **Wiki LLM** (this /opt second-brain) | L1 SDD specs (as `concept` / `decision` pages); L2 Skills patterns (as `pattern` pages); L3 Context (as `source-synthesis` pages); L4 Hook lessons (as `lesson` pages); L5 Harness comparisons (as `comparison` pages) | All layers contribute knowledge artifacts; wiki indexes via methodology + 9 page types |
| **PM Tools** (Obsidian PM, Multica board) | L1 SDD (epics/modules/tasks); L2 Skills (in PM tool task descriptions); L5 Harness (Multica = both PM tool AND harness) | PM tools display the SDD work breakdown + skill invocation tracking; Multica's board IS the L5/L1 unified view |
| **Public Obsidian** | All layers as published markdown | `wiki_sync` MCP / `tools.sync` → operator's public Obsidian vault |
| **D10 — Pre-public-Obsidian surface** | Same artifacts, surfaced earlier in the lifecycle | Multica's WebSocket streaming (real-time) + `multica issue list --watch` + agent skills metrics |
| **Git / GitHub** | L1 SDD + L4 Hooks (in `.claude/`) + L5 Harness (in repo config) | git commit history is the persistent record |
| **Memory (per-Claude-Code-session)** | L3 Context state + L1 directives | `$HOME/.claude/projects/<dir>/memory/` MEMORY.md + per-topic files |

## Where E024 (Per-Project Assistant Profile) Fits

> [!success] **The Per-Project Assistant Profile is the bridge that compiles all 5 layers into ONE runtime-agnostic spec.**

The Profile pattern's 6 schema sections map onto the 5 layers as follows:

| Profile section | Spectrum layer | What it captures |
|---|---|---|
| **Identity** | L5 Harness | Runtime targets + project + owner |
| **Knowledge Scope** | L3 Context | Wiki paths, raw paths, MCP servers, sister-project links |
| **Action Surface** | L2 Skills | Allowed/forbidden tools; skill systems; orchestrator + children |
| **Model Routing** | L3 Context + L5 Harness | Primary model + fallback chain + cost ceiling |
| **Prompt Templates** | L1 SDD + L3 Context | System prompt encodes SDD doctrine + ambient context |
| **Success Criteria** | L1 SDD + L4 Hooks | Observable outcomes + telemetry hooks |

So a Profile IS a 5-layer-unified spec. The spawn protocol (e.g., [[spawn-protocol-multica-the-runtime-agnostic-bridge-from-per-project-profile-to-multicas-10-cli-daemon|spawn-protocol-multica]]) compiles the Profile into the specific tool's mechanisms.

## Decision Heuristic — Which Layer To Use When

> [!tip] **When you have an agent-behavior-programming decision to make, ask: at what granularity does this need to fire?**

| Need | Use this layer |
|---|---|
| Encode WHAT we're building over weeks/months (multiple agent invocations) | **L1 SDD** — author requirements-spec / ADR / design-plan |
| Make an action reusable across workflows | **L2 Skills** — author orchestrator + child skills (skill.md) |
| Make information available to the agent at every inference | **L3 Context** — add to CLAUDE.md / AGENTS.md / MCP server |
| Block / modify behavior at a specific lifecycle event (deterministic) | **L4 Hooks** — author hook script + wire in settings.json |
| Change WHERE / HOW the agent runs (model provider, env, gating) | **L5 Harness** — config Multica agent / OpenClaw config / etc. |
| ALL of the above for a specific project | **E024 Per-Project Profile** — encode all 5 in one Profile.yaml |

## Anti-Patterns

| Anti-pattern | Why bad |
|---|---|
| Treating SDD and Skills as the same thing | Both are declarative but at different granularities; mixing loses precision |
| Encoding context-injection directly in skill.md instead of system prompt | Loses the per-inference reusability; skill should focus on actions |
| Building tool-specific hooks before identifying which lifecycle event matters | Hooks are L4 — most tool-specific layer; doing this before identifying the event leads to schema-validity bugs (the recently-discovered `additionalContext` bug class) |
| Inventing harness-level features when Multica already provides them | Multica = the operator's adopted meta-harness; reinventing its features = wasted engineering |
| Treating each tool as a silo | The 5 layers exist in ALL tools; the mechanisms differ but the abstractions don't — pick the mechanism per tool but design at the abstraction level |
| Stopping at one layer | The Profile pattern requires all 5; a "Profile" that only fills 3 sections is partial |

## How To Apply

1. **For a new agent behavior need**, identify which of the 5 layers is the natural fit using the decision heuristic above
2. **For per-project assistant work** (E024 scope), populate ALL 5 layers in the Profile (Identity, Knowledge Scope, Action Surface, Model Routing, Prompt Templates, Success Criteria)
3. **For cross-tool portability**, design at the **abstraction level** (e.g., "the agent needs a copywriting skill") and let the per-tool spawn protocol compile to the specific mechanism (skill.md in Claude Code, Multica skill in Multica, etc.)
4. **For destination integration**, identify which layer's output flows to which destination (e.g., L1 SDD → epics in Multica board; L3 Context → MCP server consumed by all tools)
5. **For tool selection**, evaluate which tool's mechanism for the relevant layer is the strongest (per the [[assistant-platforms-and-frameworks-frontier-comparison-claude-os-obsidian-pm-multica-openclaw-command-center-2026-05-09|Frontier comparison]])

## Open Operator-Decisions Surfaced

> [!question] **D11 — Should this spectrum become a spine-level model (model-declarative-agent-programming-spectrum)?** Currently a `concept` at draft maturity. Promotion to spine adds it to the 16-model registry; would replace ad-hoc reading order with named foundational reference.

> [!question] **D12 — Tool-specific spawn protocols beyond Multica + generic-Agent-SDK** — Should E024-M004 author spawn-protocol-openclaw, spawn-protocol-claude-code-cli-p, spawn-protocol-hermes as priority? Recommendation: Multica covers most CLIs (it's a meta-harness); direct spawn protocols only needed when bypassing Multica.

> [!question] **D13 — Cross-tool skill.md portability** — Anthropic / Claude OS / Multica skill formats are converging but not identical. Should /opt produce a canonical skill.md schema (extending the Skill Systems pattern) or wait for the de-facto standard to crystallize?

> [!question] **D14 — Per-tool L4 hook portability** — Hooks vary most across tools (Layer 4). Should /opt produce a hook-portability lesson (or pattern) documenting per-tool event mappings? Useful when migrating workflows between tools.

> [!question] **D15 — Profile-as-source-of-truth vs distributed-config** — Currently the Profile pattern envisions one YAML as the unified spec. Operator-decision: should we go full Profile-canonical (regenerate tool-specific configs FROM the Profile each time) OR allow tool-specific configs to drift (Profile as documentation only)?

## Sister-Project Applicability

| Project | Spectrum applicability |
|---|---|
| **/opt second-brain** | This spectrum lives here; provides the unified vocabulary |
| **OpenArms / OpenFleet / AICP / dcp / root-ghostproxy / Hermes** | Each project's Profile uses all 5 layers; spawn protocols compile to each project's harness |
| **All Claude Code users** | The spectrum applies — pick the layer per need; same vocabulary across the ecosystem |

## Relationships

- IMPLEMENTS: [[2026-05-09-operator-directive-sdd-skills-context-hooks-harness-overlap-need-clear-view-and-vision-integrate-everywhere-wiki-llm-pm-claude-os-multica-openclaw-claude-code-opencode|Operator directive 2026-05-09 turn 3]]
- BUILDS ON: [[spec-driven-agentic-build-is-the-2026-convergent-pattern-prompts-are-first-class-artifacts|Lesson — Spec-Driven Convergence]] (L1 source)
- BUILDS ON: [[model-skills-commands-hooks|Model — Skills, Commands, Hooks]] (L2 + L4 source)
- BUILDS ON: [[model-context-engineering|Model — Context Engineering]] (L3 source)
- BUILDS ON: [[claude-code-hook-additionalcontext-is-event-specific-not-all-events-accept-it|Lesson — Hook output channel is event-specific]] (L3 + L4 constraint)
- BUILDS ON: [[skill-systems-orchestrator-plus-modular-child-skills-the-architecture-pattern-anthropic-wont-solve-for-you|Pattern — Skill Systems]] (L2)
- BUILDS ON: [[assistant-platforms-and-frameworks-frontier-comparison-claude-os-obsidian-pm-multica-openclaw-command-center-2026-05-09|Comparison — Assistant Platforms Frontier]] (tool axis)
- COMPLEMENTS: [[per-project-assistant-profile-pattern-tailored-config-to-spawn-ecosystem-runtimes|Pattern — Per-Project Assistant Profile]] — Profile compiles all 5 layers; this spectrum is the conceptual foundation
- COMPLEMENTS: [[spawn-protocol-multica-the-runtime-agnostic-bridge-from-per-project-profile-to-multicas-10-cli-daemon|Pattern — spawn-protocol-multica]] — first concrete L5 compilation
- DEMONSTRATES: [[anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence|Lesson — Anti-Vendor-Lock-In]] — the spectrum is tool-agnostic by design
- DEMONSTRATES: [[infrastructure-over-instructions-for-process-enforcement|Principle 1 — Infrastructure Over Instructions]] — all 5 layers are structural enforcement, not prose
- DEMONSTRATES: [[structured-context-governs-agent-behavior-more-than-content|Principle 2 — Structured Context]] — the spectrum unifies what structural context looks like at each layer

## Cross-references

- All 5 layer source pages linked in Relationships
- Profile pattern: `wiki/patterns/01_drafts/per-project-assistant-profile-pattern-tailored-config-to-spawn-ecosystem-runtimes.md`
- Frontier comparison: `wiki/comparisons/assistant-platforms-and-frameworks-frontier-comparison-claude-os-obsidian-pm-multica-openclaw-command-center-2026-05-09.md`
- Epic E024: `wiki/backlog/epics/milestone-v2/e024-per-project-assistant-configurations-to-capture-programmatic-credit-and-enable-ecosystem-spawn.md`
- Operator directive log: `raw/notes/2026-05-09-operator-directive-sdd-skills-context-hooks-harness-overlap-need-clear-view-and-vision-integrate-everywhere-wiki-llm-pm-claude-os-multica-openclaw-claude-code-opencode.md`

## Backlinks

[[Operator directive 2026-05-09 turn 3]]
[[Lesson — Spec-Driven Convergence]]
[[Model — Skills, Commands, Hooks]]
[[model-context-engineering|Model — Context Engineering]]
[[Lesson — Hook output channel is event-specific]]
[[Pattern — Skill Systems]]
[[Comparison — Assistant Platforms Frontier]]
[[Pattern — Per-Project Assistant Profile]]
[[Pattern — spawn-protocol-multica]]
[[Lesson — Anti-Vendor-Lock-In]]
[[infrastructure-over-instructions-for-process-enforcement|Principle 1 — Infrastructure Over Instructions]]
[[structured-context-governs-agent-behavior-more-than-content|Principle 2 — Structured Context]]
