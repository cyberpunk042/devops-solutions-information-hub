---
title: Gateway Output Contract — What Good Tool Output Looks Like
aliases:
  - "Gateway Output Contract — What Good Tool Output Looks Like"
  - "Gateway Output Contract"
  - "Gateway Output Standards"
type: concept
domain: cross-domain
layer: spine
status: synthesized
confidence: high
maturity: growing
created: 2026-04-15
updated: 2026-04-15
sources:
  - id: operator-directive-rework
    type: directive
    file: raw/notes/2026-04-15-directive-knowledge-project-methodology-rework.md
  - id: principle-structured-context
    type: wiki
    file: wiki/lessons/04_principles/hypothesis/structured-context-governs-agent-behavior-more-than-content.md
  - id: principle-infrastructure
    type: wiki
    file: wiki/lessons/04_principles/hypothesis/infrastructure-over-instructions-for-process-enforcement.md
  - id: model-context-engineering
    type: wiki
    file: wiki/spine/models/depth/model-context-engineering.md
  - id: execution-mode-consumer-property
    type: wiki
    file: wiki/lessons/01_drafts/execution-mode-is-consumer-property-not-project-property.md
tags: [standards, gateway, tool-output, context-injection, contract, structured-context, proto-programming, srp]
---

# Gateway Output Contract — What Good Tool Output Looks Like

## Summary

Tool outputs from gateway subcommands are **context injections to the invoking agent, not data returns**. Every gateway subcommand must honor five structural rules: single responsibility, context-aware branches, size ceiling, read-whole marker, closing next-move. This contract extends [[structured-context-governs-agent-behavior-more-than-content|Principle 2 — Structured Context Governs Behavior]] from inputs (CLAUDE.md, skills, task context) to outputs (tool return shape). The same proto-programming principles that make structured INPUT programs agent behavior must apply to structured OUTPUT, because the output IS the next context injection the agent consumes.

## Key Insights

1. **Tool outputs ARE context injections, not data returns.** The moment a gateway subcommand produces text the agent reads, that text programs the agent's next move. Apply the same structural rules to outputs that Principle 2 applies to inputs: consistent shape, typed markers, sequential cues, decision tables.

2. **Single Responsibility Principle (SRP) per subcommand.** One subcommand answers ONE question. If an output mixes two questions (e.g., "what task should I do?" + "what's the runtime declaration?"), it violates SRP and fragments the agent's cognitive model.

3. **Declared > detected — always.** Context-aware branching must honor the three-layer authority ([[execution-mode-is-consumer-property-not-project-property|stable identity + phase/scale + consumer/task]]). Heuristic detection is a sanity-check signal, never an override of explicit declaration. Tools that claim to "detect" what the consumer must declare are lying.

4. **Size ceiling is a discipline, not a limit.** The brain teaches context hygiene (Model — Claude Code). Outputs that can flood context compound per invocation. Default ≤60 lines; past that, point to a reference page. Full-content opt-in via explicit operator flag, never default.

5. **Read-whole marker is proto-programming applied to output shape.** Agents skim under context pressure. An explicit structural marker at the top overrides skim heuristics. Use it when the output contains task-routing, decision-branching, or context-critical information buried past the first 20 lines.

6. **Closing next-move prevents invented actions.** Without explicit next move, agents improvise — observed directly on 2026-04-15 when a fresh agent (post-compaction) invented a 5-layer plan because no gateway output said "run gateway orient next." The closing line is infrastructure against improvisation.

## Deep Analysis

### Why This Contract Exists

On 2026-04-15, a fresh agent inside the brain (post-compaction) invoked `gateway flow` and `gateway what-do-i-need`. Both returned outputs shaped for app-project task routing. Neither recognized the agent was inside the second brain, fresh, and needed orientation before task routing. The operator's observation: the gateway is app-project-shaped, not knowledge-project-aware. Root cause: there is no output contract. Each subcommand was authored independently; the compounded drift produced context-blind outputs that violate the brain's own Principle 2.

This contract codifies the structural rules every gateway subcommand must inherit. It is framework-level enforcement: the gateway no longer depends on per-author discipline to produce agent-appropriate output. The shape is specified; the subcommand either matches or fails audit.

### The Five Rules

> [!info] **Rule 1 — Single Responsibility**
>
> | Aspect | Definition |
> |--------|------------|
> | **WHY** | Cognitive mixing forces consumers to parse which part applies. SRP = one subcommand, one question answered. |
> | **HOW** | Author states the ONE question in one sentence before coding. If the output mixes answers to two questions, split into two subcommands. |
> | **GATE** | Readable statement of the question. Output contains ONLY material answering that question. |
> | **ANTI-PATTERN** | `gateway what-do-i-need` today mixes: task routing + consumer-runtime signaling + default-profile advice in one block. Three questions, one output = skim confusion. |

> [!info] **Rule 2 — Context-Aware Branches**
>
> | Aspect | Definition |
> |--------|------------|
> | **WHY** | Three-layer orthogonality: stable identity (brain vs. sister) + phase/scale (declared) + consumer/task (per-invocation) each have different authority and invocation source. Same output for all contexts = wrong shape for most invocations. |
> | **HOW** | Branch on `(location: brain \| sister \| external) × (freshness: fresh \| returning \| task-bound)`. Declared flags override heuristics always. Heuristics are sanity-check signals, never overrides. |
> | **GATE** | Same invocation in different contexts produces meaningfully different output tailored to that context. |
> | **ANTI-PATTERN** | `gateway flow` today auto-detects `phase: mvp \| scale: micro \| mode: solo` even when CLAUDE.md explicitly declares `production \| medium \| solo`. Heuristic override of declaration is the exact conflation Principle 2 names. |

> [!info] **Rule 3 — Size Ceiling (~60 lines)**
>
> | Aspect | Definition |
> |--------|------------|
> | **WHY** | Context window is the primary constraint. Tool output compounds per invocation. Outputs that exceed one terminal screen invite skimming AND consume budget that later work needs. |
> | **HOW** | Default ≤60 lines. Content requiring more → point to a reference page (wiki link), not an inline dump. Exception: operator declares `--full-content` explicitly (opt-in, never default). |
> | **GATE** | Output at default flags fits one terminal screen. `--full-content` is the documented opt-in for exhaustive dumps. |
> | **ANTI-PATTERN** | `gateway navigate` without bounds can emit the entire knowledge tree. `gateway timeline --scope all` without ceiling can emit hundreds of events. Both flood context without operator opt-in. |

> [!info] **Rule 4 — Read-Whole Marker**
>
> | Aspect | Definition |
> |--------|------------|
> | **WHY** | Agents skim under context pressure. A structural marker at the top is proto-programming: it overrides skim heuristics by signaling "behavioral decision ahead, full read required." Applies Principle 2 to output shape. |
> | **HOW** | First line: `⚠ READ THIS OUTPUT IN FULL — <specific reason>`. Show only when the reason is real (task-routing embedded, decision-branching, context-critical info past line 20). Do NOT show on short informational outputs. |
> | **GATE** | Output either fits comfortably without marker (≤30 lines, single-point content) OR includes the marker with a specific stated reason. |
> | **ANTI-PATTERN** | Output without marker that buries critical branching in the middle. Agent skims first 10 lines, acts on incomplete context, produces wrong next move. |

> [!info] **Rule 5 — Closing Next-Move**
>
> | Aspect | Definition |
> |--------|------------|
> | **WHY** | Without explicit next move, the agent invents one. Observed 2026-04-15: fresh agent improvised a 5-layer onboarding plan because no gateway output declared the canonical next step. Explicit next move = infrastructure against improvisation. |
> | **HOW** | Last line: `NEXT: <command>` or `NEXT: <1-2 options with clear chooser>`. Never a menu of 5+ options — that is a browse list, not a next move. |
> | **GATE** | Reader can act on the output without additional reasoning. The next move is unambiguous OR the chooser between two options is stated. |
> | **ANTI-PATTERN** | `gateway what-do-i-need` today closes with "EXPLORE MORE:" listing 4 commands with no indication which to pick. That is a menu, not a close. |

### The Three Contexts to Branch On

Every context-aware subcommand branches on location × freshness. Output shape is tailored per cell.

> [!abstract] Context Detection Matrix
>
> | Location | Detection rule | Source of truth |
> |----------|---------------|----------------|
> | **brain-self** | `--wiki-root` resolves to research-wiki repo (or no flag + CWD is the brain) | Repo identity in CLAUDE.md + `--wiki-root` |
> | **sister** | `--wiki-root` resolves to a registered sister, OR `--brain` is explicit and CWD is different | `sister-projects.yaml` registry + explicit flags |
> | **external** | No `--wiki-root` or `--brain` resolution, typically an MCP-only caller | Absence of any repo-linked flag |
>
> **Freshness overlay** — each location branches further on freshness signal:
>
> | Freshness | Detection |
> |-----------|-----------|
> | **fresh** | Post-compaction detected (session-state absent) OR explicit `--fresh` flag OR first invocation of the session |
> | **task-bound** | Current stage declared (frontmatter, session-state) OR explicit `--task <type>` |
> | **returning** | Session-state present and recent (last invocation < N minutes ago) |
>
> Consumer declaration via `MCP_CLIENT_RUNTIME` env var ([[consumer-runtime-signaling-via-mcp-config|existing decision]]) overrides heuristic location detection. Declared > detected.

### Annotated Exemplar 1 — `gateway orient` (brain-mode, fresh agent)

> [!example]- Output block
>
> ```
> ⚠ READ THIS OUTPUT IN FULL — routing decisions depend on every section.
>
> ORIENT — You are inside the second brain
> ========================================
>
> YOU ARE:     a fresh agent inside research-wiki (the brain itself)
> FRESHNESS:   post-compaction / first session / no prior state found
> LOCATION:    brain-self (resolved via --wiki-root)
>
> BEFORE YOU DO ANY TASK, INTERNALIZE THE BASE.
>
> Recommended reading path (30-60 min, in order):
>
>   1. wiki/spine/super-model/super-model.md
>   2. 5 sub-super-models in wiki/spine/super-model/
>        goldilocks-protocol, enforcement-hierarchy,
>        knowledge-architecture, work-management,
>        integration-ecosystem
>   3. wiki/spine/references/model-registry.md    (16 models index)
>   4. Foundation models (dependency order):
>        model-llm-wiki → model-methodology → model-wiki-design
>   5. wiki/lessons/04_principles/hypothesis/      (3 principles)
>   6. wiki/spine/standards/                       (per-type standards)
>
> STANDING RULES (read in full, not summarized):
>   memory/feedback_verbatim_always.md
>   memory/feedback_no_caps_no_compact_read_full.md
>   memory/feedback_answer_before_asking.md
>   memory/feedback_pipeline_not_manual.md
>
> NEXT: gateway what-do-i-need    (after internalizing the base)
> ```

> [!abstract] Rule-by-rule audit of the exemplar
>
> | Rule | Applied in exemplar | Line reference |
> |------|-------------------|----------------|
> | **1 — SRP** | Answers only "who are you, where, what to internalize." Does NOT route to specific tasks — that is `what-do-i-need`'s job. | Whole block |
> | **2 — Context-aware** | `brain-self + fresh` branch. Different from sister-mode (which shows contribute flow) or external (tool list). | Header lines "LOCATION / FRESHNESS" |
> | **3 — Size ceiling** | 28 content lines. Under 60-line default. Reading path is a numbered list, not inline prose. | Whole block |
> | **4 — Read-whole marker** | `⚠` first line with specific reason: "routing decisions depend on every section." | Line 1 |
> | **5 — Closing next-move** | `NEXT: gateway what-do-i-need` — single, unambiguous next step. | Last line |

### Annotated Exemplar 2 — `gateway what-do-i-need` (brain-mode, task-bound)

> [!example]- Output block
>
> ```
> ⚠ READ THIS OUTPUT IN FULL — routing depends on the task-type table.
>
> WHAT DO YOU NEED? — Inside the second brain (self = brain)
>
> YOUR CONTEXT:
>   location:   research-wiki (brain-self)
>   freshness:  task-bound (session-state present)
>
> IF YOU ARE FRESH, run `gateway orient` first. Otherwise pick a task:
>
>   Task type               | Verbs activated         | Entry
>   ------------------------|-------------------------|------------------------
>   Ingest source           | aggregate → process     | skill: wiki-agent
>                             → integrate → validate |
>   Evolve candidate        | evaluate → learn        | skill: evolve
>                             → integrate → validate |
>   Promote to principle    | evaluate → modelize     | gateway query --review
>                             → validate             |
>   Author standards        | modelize → standardize  | skill: model-builder
>                             → teach → validate     |
>   Aggregation sweep       | aggregate → integrate   | sister_project + timeline
>                             → evaluate (no write)  |
>   Cross-ecosystem retro   | aggregate → integrate   | timeline --scope all
>                             (timeline) → evaluate  |
>
> NEXT: gateway query --task <type>    (loads the verb chain for that task)
> ```

> [!abstract] Rule-by-rule audit of the exemplar
>
> | Rule | Applied in exemplar | Line reference |
> |------|-------------------|----------------|
> | **1 — SRP** | Answers only "given task-bound in brain, what's the path?" Does NOT orient, does NOT execute — just routes. | Whole block |
> | **2 — Context-aware** | brain-self + task-bound branch. Different from app-task routing (which would show feature-dev stages) or sister branch. | Header + task-type table |
> | **3 — Size ceiling** | 32 content lines. Under 60-line default. | Whole block |
> | **4 — Read-whole marker** | `⚠` with specific reason pointing to the task-type table. | Line 1 |
> | **5 — Closing next-move** | `NEXT: gateway query --task <type>` — unambiguous, even with placeholder. | Last line |

### Anti-Pattern Gallery

> [!bug]- **Anti-Pattern 1: `gateway flow` today — Rule 2 violation**
>
> Current output (2026-04-15):
> ```
> YOUR CONTEXT (auto-detected):
>   domain: knowledge  |  phase: mvp  |  scale: micro  |  mode: solo
> ```
>
> But CLAUDE.md declares `phase: production` and `scale: medium`. The tool heuristically re-detected values that are explicitly declared — overriding the declaration with a heuristic guess. This is the exact conflation [[execution-mode-is-consumer-property-not-project-property|Principle 2]] warns against: declared > detected.
>
> **Fix:** Honor declared values. Heuristic detection is a sanity-check signal (warn if heuristic and declaration disagree), never an override. `gateway what-do-i-need` already does this correctly and shows the pattern to follow.

> [!bug]- **Anti-Pattern 2: `gateway what-do-i-need` today — Rules 1 + 5 violations**
>
> Current output mixes three distinct questions:
> - Task routing ("pick a model")
> - Consumer runtime signaling ("declare via MCP_CLIENT_RUNTIME")
> - Default profile advice ("SUGGESTED DEFAULT PROFILE")
>
> Rule 1 violation: three questions, one output. Rule 5 violation: closes with `EXPLORE MORE:` listing 4 optional commands — a menu, not a next move.
>
> **Fix:** Extract consumer-runtime content to a separate subcommand or a conditional section shown only on first invocation. Close with a specific `NEXT:` line. If routing is genuinely branched, say so: `NEXT: gateway query --task <type>` or `NEXT: gateway orient` for fresh agents.

> [!bug]- **Anti-Pattern 3: Hypothetical orient-plus-route mashup — Rule 1 violation**
>
> Imagine `gateway orient` also showed the task-type routing table. Seems efficient — "one command, everything a fresh agent needs." But violates SRP:
>
> - Orientation teaches the base. That's a learn-before-do message.
> - Routing picks a task. That's a do-now-that-you-know message.
>
> Mashing them forces the agent to parse "should I read the base or pick a task?" when the answer depends on freshness. Freshness is orient's job; routing is what-do-i-need's job. Chain them; don't mash.
>
> **Fix:** Keep subcommands focused. Closing next-move on orient points to what-do-i-need. Each subcommand's internal cohesion survives.

### State of Knowledge

> [!success] **Well-covered**
> - Five rules with WHY / HOW / GATE / ANTI-PATTERN for each
> - Three-context branching matrix aligned with three-layer orthogonality
> - Two annotated exemplars (orient brain-mode, what-do-i-need brain-mode)
> - Three anti-patterns grounded in observed 2026-04-15 behavior
> - Proto-programming extended from inputs to outputs (new application of Principle 2)

> [!warning] **Thin or unverified**
> - Exemplars for sister-mode and external-mode not yet drafted (deferred to E022 M002 document stage)
> - No validator yet — this contract is currently enforced by author discipline, not by `pipeline post` (future infrastructure gap)
> - Size ceiling (~60 lines) is an estimate grounded in one terminal screen; empirical measurement of degradation threshold not done
> - Read-whole marker adoption untested across real agent sessions — effect on skim behavior is theoretical

## How to Apply

> [!tip] Checklist authors run when building or auditing a gateway subcommand
>
> Before shipping, verify:
>
> - [ ] **Rule 1 — SRP:** I can state the ONE question this subcommand answers in one sentence. The output contains ONLY material answering that question.
> - [ ] **Rule 2 — Context-aware:** Output branches on (location × freshness). Same invocation in two contexts produces meaningfully different output. Declared flags override heuristics.
> - [ ] **Rule 3 — Size ceiling:** Default output ≤60 lines. Content exceeding points to a reference page. `--full-content` flag opt-in only.
> - [ ] **Rule 4 — Read-whole marker:** If output is >30 lines OR contains routing/decision branching, the first line is `⚠ READ THIS OUTPUT IN FULL — <specific reason>`.
> - [ ] **Rule 5 — Closing next-move:** Last line is `NEXT: <command>` or `NEXT: <1-2 options with clear chooser>`. Not a menu of 5+ options.
>
> Fails any check → the subcommand does not ship until fixed.

## Open Questions

> [!question] Should the contract include a hard validator in `pipeline post`?
> Per [[infrastructure-over-instructions-for-process-enforcement|Principle 1]], a contract enforced by author discipline is ~25% compliant. A validator that parses gateway output against the 5 rules would achieve ~100% on the checkable subset (Rules 3, 4, 5 are mechanically checkable; Rules 1 and 2 require judgment). This is a candidate for M001's follow-on work.

> [!question] What is the empirical right size ceiling?
> 60 lines is one terminal screen. But agent context windows are orders of magnitude larger. Is the real ceiling cognitive (skim threshold) rather than physical? Needs measurement across real sessions.

> [!question] Should `MCP_CLIENT_RUNTIME` env var extend to cover freshness declaration?
> Current var signals consumer runtime. Freshness (fresh / task-bound / returning) is similar — a per-session declaration the consumer knows. Worth a `MCP_CLIENT_FRESH=1` companion var? (Requires: design in E022 M002.)

### How This Connects — Navigate From Here

> [!abstract] From This Contract → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **The principle this implements** | [[structured-context-governs-agent-behavior-more-than-content\|Principle — Structured Context Governs Behavior More Than Content]] |
> | **The principle this enforces structurally** | [[infrastructure-over-instructions-for-process-enforcement\|Principle — Infrastructure Over Instructions]] |
> | **The three-layer orthogonality the branching honors** | [[execution-mode-is-consumer-property-not-project-property\|Execution Mode Is a Consumer Property]] |
> | **The gateway model this extends** | [[model-mcp-cli-integration\|Model — MCP and CLI Integration]] |
> | **The context-engineering model this applies to outputs** | [[model-context-engineering\|Model — Context Engineering]] |
> | **The epic implementing this contract** | [[e022-context-aware-gateway-orientation-and-routing\|E022 — Context-Aware Gateway Orientation and Routing]] |

## Relationships

- BUILDS ON: [[structured-context-governs-agent-behavior-more-than-content|Principle — Structured Context Governs Agent Behavior More Than Content]]
- BUILDS ON: [[infrastructure-over-instructions-for-process-enforcement|Principle — Infrastructure Over Instructions for Process Enforcement]]
- BUILDS ON: [[model-context-engineering|Model — Context Engineering]]
- BUILDS ON: [[model-mcp-cli-integration|Model — MCP and CLI Integration]]
- RELATES TO: [[execution-mode-is-consumer-property-not-project-property|Execution Mode Is a Consumer Property, Not a Project Property]]
- RELATES TO: [[consumer-runtime-signaling-via-mcp-config|Decision — Consumer Runtime Signaling via MCP Config]]
- FEEDS INTO: [[e022-context-aware-gateway-orientation-and-routing|E022 — Context-Aware Gateway Orientation and Routing]]
- ENABLES: [[model-claude-code|Model — Claude Code]]

## Backlinks

[[structured-context-governs-agent-behavior-more-than-content|Principle — Structured Context Governs Agent Behavior More Than Content]]
[[infrastructure-over-instructions-for-process-enforcement|Principle — Infrastructure Over Instructions for Process Enforcement]]
[[model-context-engineering|Model — Context Engineering]]
[[model-mcp-cli-integration|Model — MCP and CLI Integration]]
[[execution-mode-is-consumer-property-not-project-property|Execution Mode Is a Consumer Property, Not a Project Property]]
[[consumer-runtime-signaling-via-mcp-config|Decision — Consumer Runtime Signaling via MCP Config]]
[[e022-context-aware-gateway-orientation-and-routing|E022 — Context-Aware Gateway Orientation and Routing]]
[[model-claude-code|Model — Claude Code]]
[[e022-context-aware-gateway-orientation-and-routing|E022 — Context-Aware Gateway Orientation and Task Routing]]
[[e022-m002-gateway-orient-subcommand|E022-M002 — Gateway Orient Subcommand (Module Design)]]
[[e022-m003-what-do-i-need-upgrade|E022-M003 — Gateway What-Do-I-Need Upgrade (Module Design)]]
[[e023-gateway-wide-output-contract-audit|E023 — Gateway-Wide Output Contract Audit]]
