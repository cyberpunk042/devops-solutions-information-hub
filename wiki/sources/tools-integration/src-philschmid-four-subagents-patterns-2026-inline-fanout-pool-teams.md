---
title: "Synthesis — Phil Schmid (May 5 2026): Four Subagents Patterns in 2026 — Inline Tool · Fan-Out · Agent Pool · Teams (Ordered by Main-Agent Control over Subagent Lifecycle)"
aliases:
  - "Four Subagents Patterns 2026"
  - "Phil Schmid Subagent Patterns Synthesis"
  - "Inline Fan-Out Pool Teams Pattern Quartet"
  - "Subagent Lifecycle Patterns"
type: source-synthesis
domain: tools-integration
status: synthesized
confidence: high
maturity: seed
layer: 1
created: 2026-05-08
updated: 2026-05-08
last_reviewed: 2026-05-08
sources:
  - id: philschmid-blog-2026-05-05
    type: article
    url: https://www.philschmid.de/subagent-patterns-2026
    file: raw/articles/how-agents-manage-other-agents-four-subagents-patterns-in-2026.md
    description: "Phil Schmid's 2026-05-05 follow-up to his prior subagents post — four patterns ordered by main-agent control over subagent lifecycle: (1) Inline Tool (call_agent), (2) Fan-Out (spawn_agent + wait_agent), (3) Agent Pool (spawn + send_message + wait + list + kill), (4) Teams (cross-agent send_message; agents talk to each other). Each step up requires a more capable model."
  - id: custom-model-concept
    type: wiki
    file: wiki/domains/cross-domain/custom-tailored-senior-engineer-tier-model-group-with-recreated-intelligence-layer-research-synthesis.md
    description: "Custom-Tailored Model Group Concept — M003 Recreated Intelligence Layer at I/O Boundaries explicitly named subagent dispatch + inter-agent latent transfer as substantive practices; Phil Schmid's quartet maps onto M003's operator-substitutable orchestration choices"
  - id: recursivemas-synth
    type: wiki
    file: wiki/sources/tools-integration/src-recursivemas-recursive-multi-agent-systems-stanford-2026.md
    description: "RecursiveMAS Synthesis — paper-grade evidence for Pattern 4 (Teams) substitutable; cross-agent latent transfer is RecursiveMAS's contribution; Phil Schmid's pattern names are the practitioner-ready vocabulary"
  - id: agent-modes-pattern
    type: wiki
    file: wiki/patterns/03_validated/architecture/agent-modes-three-mode-pattern-with-mode-aware-loop-cycles.md
    description: "Agent Modes Pattern — agent modes are PERSONA overlay on the SAME agent; subagent patterns are SEPARATE agents. Sister structurally; modes pick lens, subagents fan-out work"
  - id: anti-vendor-lock-in-lesson
    type: wiki
    file: wiki/lessons/01_drafts/anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence.md
    description: "Anti-Vendor-Lock-In Lesson — orchestrator-layer substitutability now has 4 named patterns within a single vendor's surface; pattern choice is operator-controllable per workload"
  - id: multi-layer-compression-lesson
    type: wiki
    file: wiki/lessons/01_drafts/end-to-end-compression-across-the-ai-stack-composes-multiplicatively-6-plus-independent-mechanisms-at-6-distinct-layers.md
    description: "Multi-Layer Compression Lesson — Pattern 1 (Inline Tool with isolated context) and Pattern 4 (Teams with main-agent context staying clean) are Layer 4 (Inter-agent) compression mechanisms; subagent isolation reduces main-agent context pressure"
  - id: claude-code-skill-chaining-synth
    type: wiki
    file: wiki/sources/tools-integration/src-claude-code-skill-chaining-fork-files-commands-85-percent-less-context.md
    description: "Claude Code Skill Chaining Synthesis — operationally implements Pattern 1 (Inline Tool — context fork) + file-handoff between sub-skills; concrete instantiation of Phil Schmid's Pattern 1 with empirical 85% context reduction"
tags: [synthesis, philschmid, subagents, agent-orchestration, inline-tool, fan-out, agent-pool, teams, multi-agent-systems, mission-2026-05-08, m003-recreated-intelligence-layer, model-capability-tiered, layer-1]
---

# Synthesis — Phil Schmid (May 5 2026): Four Subagents Patterns in 2026

## Summary

Phil Schmid's 2026-05-05 follow-up to his earlier subagents post catalogues **four orchestration patterns ordered by main-agent control over subagent lifecycle**. (1) **Inline Tool** — `call_agent` is identical to any other tool call; subagent runs in its own context with its own tools/instructions; main agent never manages lifecycle. Sync (blocks) or async (returns ID, result delivered as injected notification). Works with any tool-capable model. (2) **Fan-Out** — `spawn_agent` returns immediately; `wait_agent` blocks for results; the model decides interleaving (call wait immediately = Pattern 1; do its own work first = real fan-out). Requires reasoning about when-to-wait; otherwise no benefit. (3) **Agent Pool** — long-lived stateful subagents addressed by ID via `send_message`; main agent coordinates between specialists; multi-turn conversations per agent; richer surface (`spawn` + `send` + `wait` + `list` + `kill`). Frontier models handle 2-4 agents okayish. (4) **Teams** — agents message each other directly via cross-agent `send_message`; main agent sets up team + steps back. Hierarchical paths or shared mailboxes for addressing. Requires frontier-class capability for EVERY team agent; coordination logic exceeds single-agent scope; debugging is hard (cycles, conflicts, cascade failures). **Each step up requires a more capable model**: P1 → any tool-capable model; P2 → models that reason about when-to-wait; P3 → tracks multi-agent state across turns; P4 → frontier for every agent. Result-collection mechanism varies: P1 inline tool response; P2 batched via `wait_agent`; P3 incremental per-message; P4 only what agents explicitly report (everything else stays inside inter-agent conversations). **Mission relevance**: (1) **directly applies to operator's [Custom-Tailored Senior-Engineer-Tier Model Group](../../domains/cross-domain/custom-tailored-senior-engineer-tier-model-group-with-recreated-intelligence-layer-research-synthesis.md) M003 Recreated Intelligence Layer at I/O Boundaries** — input-boundary intelligence includes orchestration-pattern selection per workload class (lookup → P1; parallel research → P2; coordinated specialists → P3; build-feature → P4); (2) **adds substitutable axis to [[anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence|Anti-Vendor-Lock-In Lesson]]** at the orchestration-pattern dimension — operator-substitutable per workload; (3) **complements [Agent Modes Pattern](../../patterns/03_validated/architecture/agent-modes-three-mode-pattern-with-mode-aware-loop-cycles.md)** structurally — modes are persona OVERLAY on the same agent (`/mode-pm` flips lens); subagents are SEPARATE agents with their own contexts (`call_agent`); sister concepts that compose (a subagent can ITSELF be in a mode); (4) **Pattern 4 (Teams) lines up with [RecursiveMAS Synthesis](src-recursivemas-recursive-multi-agent-systems-stanford-2026.md)** — RecursiveMAS provides paper-grade evidence (34.6-75.6% token reduction, 8.3% accuracy improvement, 1.2-2.4× speedup); Phil Schmid's vocabulary is the practitioner naming layer; (5) **Pattern 1 (Inline Tool with isolated context) is empirically realized by [Claude Code Skill Chaining](src-claude-code-skill-chaining-fork-files-commands-85-percent-less-context.md)** — context fork in YAML frontmatter is the implementation; 85% context reduction is the empirical anchor.

## Reference

> [!info] Source identity
>
> | Field | Value |
> |---|---|
> | **Author** | Philipp Schmid |
> | **Date** | 2026-05-05 (11-minute read) |
> | **Type** | Pattern catalogue / practitioner essay |
> | **Predecessor** | Schmid's earlier post on the rise of subagents (referenced as prior work) |
> | **Pattern ordering principle** | By level of control the main agent has over the subagent lifecycle |
> | **Tools surface across patterns** | call_agent → spawn_agent + wait_agent → spawn + send_message + wait + list + kill → all-of-above + cross-agent send_message |

## The Four Patterns (Pattern × Tools × Role × Lifetime × Model-tier)

> [!success] **Each step up the pattern ladder requires a more capable model.**
>
> | Pattern | Tools | Main agent role | Agent lifetime | Min model tier | Result delivery |
> |---|---|---|---|---|---|
> | **1. Inline Tool** | `call_agent` | Caller | Single task | Any tool-capable | Inline tool response (sync) OR injected notification (async) |
> | **2. Fan-Out** | `spawn_agent` · `wait_agent` | Dispatcher | Single task | Reasons about when-to-wait | Batched via `wait_agent` |
> | **3. Agent Pool** | `spawn` · `send_message` · `wait` · `list` · `kill` | Coordinator | Multi-turn (stateful) | Tracks multi-agent state across turns | Per-message incremental via `wait_agent` |
> | **4. Teams** | All Pattern 3 + cross-agent `send_message` | Supervisor | Persistent | Frontier-class for EVERY agent in the team | Only what agents explicitly report back; rest stays inside inter-agent conversations |
>
> Schmid's recommendation: **Start with Pattern 1.** Most tasks that feel like they need multi-agent work fine with a well-prompted inline tool call. Move to Pattern 2 for genuinely independent parallel work. Move to Pattern 3 when agents collaborate across multiple steps. Pattern 4 is for when coordination logic exceeds what a single agent can manage.

## Key Insights

> [!success] **The framework provides the tools; the model controls the orchestration.**
>
> Schmid's structural insight: across patterns 2-4, `spawn_agent` always returns immediately and `wait_agent` collects results when the model decides to call it. The orchestration intelligence — when to spawn vs wait, who to message vs kill, sequential vs parallel coordination — comes from the model's reasoning, not from infrastructure-encoded business logic.
>
> **Operator-mission application**: this is exactly the [3-tier programming hyperstructure](../../domains/cross-domain/custom-tailored-senior-engineer-tier-model-group-with-recreated-intelligence-layer-research-synthesis.md) (proto / proto-proto / literal) frame applied to subagent orchestration. The tool surface (P1-P4) is Tier 1+2 (declarative + hyperstructure). The model's runtime decision-making across that surface is Tier 3 (literal programming).

> [!success] **Pattern 1 (Inline Tool) is the new "tool call" — most useful for most tasks.**
>
> *"Most subagent use cases start and stay here."* Self-contained work — research lookups, code reviews, file analysis, test generation — fits Pattern 1. Sync if the tool blocks; async if results arrive as injected notifications. **Operator-mission application**: most M003 (Recreated Intelligence Layer) input-boundary work fits Pattern 1 (e.g., "verify this claim against the wiki" → call a `wiki_search` subagent → result inline).

> [!success] **Pattern 2 (Fan-Out) is conditional on model reasoning about when-to-wait.**
>
> *"A model that calls wait_agent immediately after every spawn gets no benefit over Pattern 1. The value depends on the model's ability to interleave its own work between spawn and wait."* This is a **P4 (Declarations Aspirational Until Verified)** instance: declaring "we use Fan-Out" is aspirational until you verify the model actually interleaves work between spawn and wait.

> [!success] **Pattern 3 (Agent Pool) is where multi-step workflows belong.**
>
> Stateful agents retain conversation history across messages. Main agent routes information between specialists (researcher → writer → fact-check). **Operator-mission application**: the [Custom-Tailored Model Group](../../domains/cross-domain/custom-tailored-senior-engineer-tier-model-group-with-recreated-intelligence-layer-research-synthesis.md) M002 specialist LoRA group naturally instantiates Pattern 3 — each specialist (senior-engineer-coding · methodology-reasoning · spec-authoring · validation-checking · debug-analysis · refactor-planning) is a long-lived stateful agent the main orchestrator routes work to.

> [!success] **Pattern 4 (Teams) requires frontier-class for EVERY agent — economic + capability gate.**
>
> *"Every agent in the team needs frontier-class model capabilities, not just the main agent."* This is the highest-cost pattern. Schmid lists infrastructure challenges: cycle detection (A waits B, B waits A), conflict resolution (two agents edit same file), shutdown coordination, debugging difficulty. **Operator-mission application**: **defer Pattern 4 until model + infrastructure mature**. The operator's M002 (specialist LoRA) approach gives Pattern 3 capability with smaller models; Pattern 4 is post-RTX-4090 + post-frontier-model territory.

> [!success] **Pattern choice maps onto workload-class — not aspirational sophistication.**
>
> Schmid's decision matrix is operator-substitutable per workload, not "always use the most sophisticated":
>
> | Workload class | Recommended pattern |
> |---|---|
> | Self-contained lookup / review / analysis | **Pattern 1** (Inline Tool) |
> | Independent parallel tasks (no intermediate routing needed) | **Pattern 2** (Fan-Out) |
> | Multi-step collaboration with mid-task coordination | **Pattern 3** (Agent Pool) |
> | Coordination logic exceeds single-agent scope | **Pattern 4** (Teams) — only when frontier-models available for all team members |
> | Smaller / cheaper model | **Stay with Pattern 1 or 2** (3-4 lose track of multi-agent state) |

> [!info] **Result-collection mechanism is THE distinguishing axis.**
>
> | Pattern | How results return |
> |---|---|
> | **1. Inline Tool** | Single tool response (sync) OR injected notification message (async) |
> | **2. Fan-Out** | Batched via `wait_agent`; returns all completed agents since last call |
> | **3. Agent Pool** | Per-message incremental; main agent processes one response at a time and adjusts next message |
> | **4. Teams** | Only what agents explicitly report back; everything else (inter-agent message chains) stays invisible to main agent |
>
> **Key implication**: Pattern 4's invisibility is its feature (clean main-agent context) AND its drawback (debugging hard, cascade failures). Operator-decision per visibility-vs-scale tradeoff.

## Deep Analysis

### Connection to Operator's Custom-Tailored Senior-Engineer-Tier Model Group (M001-M006)

| M-module | Subagent pattern that fits naturally | Why |
|---|---|---|
| M001 — Toolchain + Data + Constitution v0.1 | (Not orchestration-relevant) | Foundation work; no subagent orchestration yet |
| M002 — First Specialist LoRA + Group Expansion | **Pattern 3 (Agent Pool)** | Specialists are long-lived stateful; main router (M003) routes work to specialist by task class |
| M003 — Recreated Intelligence Layer at I/O Boundaries | **Pattern 1 (Inline Tool) + Pattern 2 (Fan-Out)** | Input-boundary intelligence needs subagent dispatch (P1) + parallel pre-processing (P2) |
| M004 — Behavioral Preference Fine-Tune | (Not orchestration-relevant) | Training-time work; no orchestration |
| M005 — Trust + Compression Composition | **Pattern 1** | Cypher/decypher subagent operates as inline tool over compressed inputs |
| M006 — Multi-Version + Ecosystem Propagation | **Pattern 4 (Teams) — future** | Cross-project agent coordination across the 5-project ecosystem; defer until frontier-capability + infrastructure mature |

### Connection to Anti-Vendor-Lock-In Lesson — Orchestration-Pattern Substitutability

The pattern quartet adds a substitutability dimension WITHIN the orchestrator layer (per [[anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence|Evidence 10 — Multica]]). Substitutable axes within the orchestration-pattern dimension:

| Axis | Operator-substitutable options |
|---|---|
| Pattern selection | P1 (Inline Tool) · P2 (Fan-Out) · P3 (Agent Pool) · P4 (Teams) — chosen per workload |
| Implementation surface | Anthropic Agents SDK · operator-built · Claude Code skill chaining (P1+context fork) · Multica per-agent custom_env routing (P3-like) · OpenAI Assistants API (P3-like) |
| Determinism boundary | Pattern surface is 100% deterministic (tool calls fire); model's orchestration decisions are ~70-90% (model-tier-dependent) |
| Visibility-vs-scale tradeoff | P1-3 main-agent-visible; P4 invisible-by-design |

### Connection to Agent Modes Pattern (Sibling Structurally)

[Agent Modes Pattern](../../patterns/03_validated/architecture/agent-modes-three-mode-pattern-with-mode-aware-loop-cycles.md) and Phil Schmid's subagent patterns are **structurally complementary, not competing**:

| Aspect | Agent Modes | Subagent Patterns |
|---|---|---|
| **What it does** | Persona OVERLAY on the SAME agent (PM lens vs Architect lens) | SEPARATE agents with their own contexts |
| **State** | Per-project `active-mode` file | Per-pattern (P1 stateless; P3-4 stateful per agent ID) |
| **Composition** | A subagent can ITSELF be in a mode (e.g., `call_agent` → that subagent reads its own `active-mode`) | Modes can dispatch to subagents (`/cycle` step calls `call_agent`) |

**Operator-mission alignment**: modes give per-project lens-switching; subagent patterns give cross-context fan-out. Both compose with M003.

### Connection to RecursiveMAS (Stanford 2026) — Paper-Grade Evidence for Pattern 4

[RecursiveMAS](src-recursivemas-recursive-multi-agent-systems-stanford-2026.md) provides paper-grade evidence for Pattern 4 (Teams):
- 19 specialist HuggingFace models
- 34.6-75.6% token reduction via cross-agent latent transfer
- 8.3% average accuracy improvement
- 1.2-2.4× end-to-end speedup (Pareto improvement)

Phil Schmid's "Teams" is the practitioner-vocabulary for what RecursiveMAS demonstrates academically. Together: **Pattern 4 has both paper evidence (RecursiveMAS) and practitioner pattern (Schmid)** — the operator-mission can adopt with confidence when frontier-tier capability is available.

### Connection to Claude Code Skill Chaining Synthesis (Same-Day Ingestion)

[Claude Code Skill Chaining Synthesis](src-claude-code-skill-chaining-fork-files-commands-85-percent-less-context.md) (also ingested 2026-05-08) **operationally implements Pattern 1 (Inline Tool with isolated context)**:
- Context fork in YAML frontmatter = subagent runs in its own isolated fork
- File handoff between sub-skills = `call_agent` returning ONLY the relevant payload, not the full conversation
- 85% context reduction = empirical anchor for Pattern 1's promise

Pattern 1 is no longer aspirational — it has a concrete implementation pathway (Claude Code skill chaining v2 from 2026-05-08).

## Quotes (verbatim)

> *"Most subagent use cases start and stay here."* (Pattern 1)

> *"A model that calls wait_agent immediately after every spawn gets no benefit over Pattern 1."* (Pattern 2)

> *"Smaller models lose track of which agent has which context, or forget to call kill_agent when done. Frontier models might handle 2-4 agents okayish."* (Pattern 3)

> *"Every agent in the team needs frontier-class model capabilities, not just the main agent."* (Pattern 4)

> *"Each step up requires a more capable model."* (the structural lesson)

> *"The framework provides the tools. The model controls the orchestration."* (the central thesis)

> *"A task that takes 4 coordinated agents today may be solvable by a single agent with a better model tomorrow."* (capability evolution)

## Open Questions

> [!question] Should the operator's Custom-Tailored Model Group adopt Pattern 3 (Agent Pool) for M002 specialist routing?
> Current AICP routing (per [project_activated_stack_2026_04_23](memory)) is closer to Pattern 2 (fan-out per request, no stateful per-task continuity). Migrating to Pattern 3 would let specialist LoRAs retain conversation context across multi-step workflows. Engineering cost: ~50-100 LOC AICP backend extension. Operator-decision per workload class (single-shot inference fits P2; multi-turn workflows benefit from P3).

> [!question] Is Pattern 4 (Teams) worth pursuing pre-frontier-model-availability OR is it post-RTX-4090 + post-Phase-7 territory?
> Schmid: every agent needs frontier-tier capability. Operator's RTX 4090 (mid-May 2026 ETA) + Custom-Model Phase-2 specialist LoRA give Pattern 3 capability; Pattern 4 likely post-Phase-7 (multi-version ecosystem propagation). Default proposal: register Pattern 4 as future-state; do not pursue at MVP scope.

> [!question] Does Phil Schmid's pattern quartet apply to non-Anthropic ecosystems (OpenAI Assistants API, LangGraph, Multica)?
> Schmid's vocabulary is implementation-neutral. The pattern surface (call vs spawn vs send vs cross-agent send) is general; specific implementations vary. Adoption posture: track per-ecosystem implementation maturity; the pattern names ARE the cross-ecosystem vocabulary.

> [!question] How does Pattern 4 (Teams) compose with the operator's L0-L4 trust opt-ins?
> Each team agent operates in its own context with its own tools. Trust composition: each agent can have its own L-tier (operator-mixed). Inter-agent communication channels need their own trust treatment (encrypted IPC vs plaintext). Operator-design call when Pattern 4 is pursued.

## Relationships

- BUILDS ON: [[custom-tailored-senior-engineer-tier-model-group-with-recreated-intelligence-layer-research-synthesis|Custom-Tailored Model Group Concept]] — pattern quartet maps onto M001-M006 operator-substitutable orchestration choices
- BUILDS ON: [[anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence|Anti-Vendor-Lock-In Lesson]] — orchestration-pattern substitutability dimension
- BUILDS ON: [[end-to-end-compression-across-the-ai-stack-composes-multiplicatively-6-plus-independent-mechanisms-at-6-distinct-layers|Multi-Layer Compression Lesson]] — Pattern 1 (isolated context) + Pattern 4 (clean main-agent context) are Layer 4 compression mechanisms
- RELATES TO: [[src-recursivemas-recursive-multi-agent-systems-stanford-2026|RecursiveMAS Synthesis]] — paper-grade evidence for Pattern 4 (Teams)
- RELATES TO: [[agent-modes-three-mode-pattern-with-mode-aware-loop-cycles|Agent Modes Pattern]] — sibling structurally; modes overlay persona on same agent vs subagents are separate agents
- RELATES TO: [[src-claude-code-skill-chaining-fork-files-commands-85-percent-less-context|Claude Code Skill Chaining Synthesis]] — concrete implementation of Pattern 1 with empirical 85% context reduction
- RELATES TO: [[src-strands-agents-aws-intent-based-tool-design-96-percent-token-reduction|Strands Agents Synthesis]] — tool-design discipline (intent-based) within Pattern 1's `call_agent` definition
- DEMONSTRATES: [[goldilocks-protocol|Goldilocks Protocol]] — pick pattern per workload-class + model-tier, not aspirational sophistication
- DEMONSTRATES: [[infrastructure-over-instructions-for-process-enforcement|Principle 1 — Infrastructure Over Instructions]] — pattern surface is infrastructure (tool calls); model's orchestration is reasoning
- DEMONSTRATES: [[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4 — Declarations Aspirational Until Verified]] — declaring "we use Fan-Out" is aspirational until you verify the model interleaves work between spawn and wait

## Backlinks

[[custom-tailored-senior-engineer-tier-model-group-with-recreated-intelligence-layer-research-synthesis|Custom-Tailored Model Group Concept]]
[[Anti-Vendor-Lock-In Lesson]]
[[Multi-Layer Compression Lesson]]
[[src-recursivemas-recursive-multi-agent-systems-stanford-2026|RecursiveMAS Synthesis]]
[[Agent Modes Pattern]]
[[src-claude-code-skill-chaining-fork-files-commands-85-percent-less-context|Claude Code Skill Chaining Synthesis]]
[[src-strands-agents-aws-intent-based-tool-design-96-percent-token-reduction|Strands Agents Synthesis]]
[[Goldilocks Protocol]]
[[infrastructure-over-instructions-for-process-enforcement|Principle 1 — Infrastructure Over Instructions]]
[[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4 — Declarations Aspirational Until Verified]]
