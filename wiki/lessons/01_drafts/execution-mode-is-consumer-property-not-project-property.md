---
title: "Execution Mode Is a Consumer Property, Not a Project Property — Guard Against Conflation Drift"
aliases:
  - "Execution Mode Is a Consumer Property, Not a Project Property"
  - "Execution Mode Is a Consumer Property"
  - "Consumer Properties vs Project Properties"
  - "Consumer-Property Conflation"
type: lesson
domain: cross-domain
layer: 4
status: synthesized
confidence: high
maturity: seed
derived_from:
  - "Right Process for Right Context — The Goldilocks Imperative"
  - "Infrastructure Over Instructions for Process Enforcement"
  - "Agent Failure Taxonomy — Seven Classes of Behavioral Failure"
contribution_status: accepted
created: 2026-04-15
updated: 2026-04-15
sources:
  - id: operator-directive-2026-04-15
    type: directive
    file: raw/notes/2026-04-15-directive-execution-mode-is-consumer-property-not-project.md
    description: Operator directive establishing the rule, caught a prior conflation that had slid back into gateway's what-do-i-need tool.
  - id: research-wiki-gateway-bug
    type: file
    file: tools/gateway.py
    description: "The `query_what_do_i_need` function (lines 235-345) as it was BEFORE the fix — claimed 'no harness code found → solo is certain' and picked ONE SDLC profile for the whole project from heuristic auto-detection."
tags: [lesson, execution-mode, consumer-property, project-property, conflation, drift-prevention, goldilocks, orthogonality, detection-limits, declared-over-detected]
---

# Execution Mode Is a Consumer Property, Not a Project Property — Guard Against Conflation Drift

## Summary

Execution mode (solo vs harness vs fleet) is a property of the **CONSUMER'S runtime**, not a property of the project. A project is always solo by default. A harness (e.g., OpenArms v10) or a fleet (e.g., OpenFleet orchestrator) **WRAPS a project from outside** — the wrapper's runtime is what knows "I'm running this project in harness mode." From inside the project directory, this cannot be detected: local absence of harness code ≠ project is not being consumed by a harness elsewhere. The same rule extends to **SDLC profile**, **methodology model**, and **stage** — these are task-dependent choices the consumer makes per work unit, not static properties of the project. Conflating these with stable project properties (type, domain, second-brain declaration) is a recurring drift failure: corrections erode unless encoded **structurally** in tool behavior, not just documented in prose.

## Context

> [!warning] When does this lesson apply?
>
> - You are building a tool that introspects a project to "auto-detect" its identity, process, or state
> - Your tool picks ONE SDLC profile, methodology model, or execution mode for the whole project
> - You have documented a correction about "identity shouldn't be static" in the past and want to verify it still holds
> - A consumer (harness/fleet/MCP client) is about to integrate with this project and you need to know what they own vs what you declare

## Insight

> [!tip] The Three-Layer Orthogonality
>
> | Layer | Properties | Who decides | When it changes | Detectable from inside? |
> |---|---|---|---|---|
> | **Stable project identity** | type, domain, second-brain relationship | The project (declared in CLAUDE.md / CONTEXT.md) | Rarely — quarters/years | **Yes** — declared is authoritative |
> | **Phase / scale state** | phase (poc/mvp/staging/production), scale (micro/medium/large) | The project (declared, owner reviews periodically) | Slowly — quarters | **Partial** — heuristics can cross-check declarations, never overrule |
> | **Consumer / task properties** | execution mode, SDLC profile, methodology model, current stage | The CONSUMER (harness/fleet/solo human) per task | Per work unit | **No** — only the consumer knows |

> [!abstract] The Rule
>
> **Solo is the default for every project.** Non-default execution modes are declared BY THE CONSUMER at connection time (e.g., via MCP config `runtime:` field, or explicit CLI arg).
>
> **SDLC profile, methodology model, and stage are per-TASK, not per-project.** A production project can run a hotfix under simplified profile while simultaneously running a deep-architecture-review under full profile. Binding one profile to the project-as-a-whole is the "frozen to a model" conflation.
>
> **From inside a project, you can NEVER detect who is consuming it or how.** The best a project-local tool can do is declare defaults and invite the consumer to override.

### Why this matters — the conflation sliding back in

Corrections about orthogonality decay. An earlier session caught "project is frozen to a model" — the fix was to make methodology model per-task. A later session unknowingly introduced the same conflation in a different dimension (SDLC profile, execution mode). The tool claimed to "detect" execution mode via the tautology "no harness code found → solo is certain" — which is not detection, only a restatement of the default with false confidence. The operator's framing: *"a conflation that was slidded back in."*

Prose rules erode. Only **structural encoding** persists: the tool's output format, schema validation, lint checks.

## Evidence

> [!bug]- Research Wiki 2026-04-15: `gateway what-do-i-need` tautological detection
>
> Before the fix, the tool's output block:
>
> ```
> DETECTED IDENTITY:
>   domain:         knowledge       (auto-detected)
>   phase:          mvp             (auto-detected from CI/tests/Docker)
>   scale:          micro (28 files)(auto-detected from file count)
>   execution mode: solo
>                   (no harness code found → solo is certain)
>   second brain:   self
>   ✓ Identity also declared in CLAUDE.md — declared values take precedence.
>
> RECOMMENDED SDLC PROFILE: simplified
> ```
>
> Bugs present simultaneously:
> 1. **Tautology as detection** — "no harness code found → solo is certain" restates the default with false confidence instead of acknowledging the detection limit.
> 2. **Declared values ignored for the recommendation** — CLAUDE.md declared `phase: production, scale: medium, SDLC Profile: Default`, but the recommendation was `simplified`. The tool's own message "declared values take precedence" was contradicted by its own logic (declared strings carry parenthetical context like "production (used daily, 316+ pages)" that breaks equality comparison).
> 3. **One profile bound to the project** — the tool picked ONE SDLC profile for the whole project. A production project running a hotfix doesn't want `default` profile for that task; it wants `simplified`. Per-task selection is invisible in the current tool UX.
> 4. **All heuristic-detected fields flagged as "⚠ Auto-detected"** — even when declarations exist. The declaration should be authoritative and should suppress the warning.

> [!success]- OpenFleet model: consumer-declared runtime
>
> OpenFleet's dispatch orchestrator declares to each agent its context at invocation — the agent doesn't detect its mode, the orchestrator states it. The wiki consuming OpenFleet wouldn't need to "detect" fleet mode; the fleet runtime would pass its identity in its MCP config or initial connection message. This is the structural shape of consumer-declared properties done right.

> [!info]- Prior conflation: project frozen to a methodology model
>
> In an earlier session, an agent assumed that a project picks ONE methodology model for its lifetime. The correction: a bug-fix task uses `bug-fix` model (document → implement → test), a feature uses `feature-development` (document → design → scaffold → implement → test), research uses `research` (document → design), and all three may happen within the same project on the same day. The operator's current message names this directly: *"a project is always solo by default... AI would think a project is frozen to a model."* Same class of failure, different dimension.

## Applicability

> [!abstract] How to apply this rule when building project-introspection tools
>
> | Temptation | Correct Behavior |
> |---|---|
> | "Auto-detect execution mode from project files" | **Don't.** Declare solo as the default. Only the consumer's runtime (via its MCP config or CLI arg) can state non-default. |
> | "Pick the right SDLC profile based on phase and scale" | Recommend a **default** profile as a starting point. Make it clear the task owner overrides per work unit. Never claim the project IS a specific profile. |
> | "Bind methodology model to project-type" | **Don't.** Model is per-task. Publish the menu; task owner selects. |
> | "Heuristically infer declared fields" | Use declarations as authoritative. Heuristics are sanity signals at best ("you declared medium but I see 28 files — investigate"). Never overrule declarations. |
> | "Warn on declared fields with ⚠ Auto-detected" | Remove the warning when a declaration exists. Show ✓ declared instead. Warnings only appear for heuristic-only dimensions. |

> [!tip] Self-check — is your project-introspection tool honest?
>
> 1. Does it claim to "detect" anything that a consumer declares? (If yes: you are conflating.)
> 2. Does it pick ONE profile/model/mode for the whole project? (If yes: you are conflating.)
> 3. Does it treat declared values as authoritative, heuristics as sanity signals? (If no: you are conflating.)
> 4. Does it warn the user about declared fields as "auto-detected"? (If yes: the warning is false.)
> 5. Could the tool say "solo is the default; the harness/fleet declares non-default when it connects"? (If no: you don't yet honor the consumer-property orthogonality.)

### Structural prevention — how to guard against re-sliding

> [!warning] Prose rules erode. Encode the correction in STRUCTURE.
>
> 1. **Tool output format** — label fields as `✓ declared` vs `⚠ heuristic`; remove "is certain" language for things that can't be detected.
> 2. **Lint check** — a wiki or code lint that fails if a tool's identity-detection output says "certain" for any consumer-declared property.
> 3. **Schema distinction** — the identity profile in CLAUDE.md/CONTEXT.md should separate PROJECT fields (stable + phase/scale) from CONSUMER-PROPERTY notes (execution mode listed with the note "declared by the consumer at connection time, not a project field").
> 4. **Integration test** — when a project-introspection tool is built or touched, its output must be reviewed against the three-layer orthogonality table above.

### Future exploration — MCP-config-based consumer declaration

> [!question] How could consumers declare their runtime to the projects they connect to?
>
> The operator's proposal: **inside the MCP config of the consuming client**. When OpenArms v10 harness or OpenFleet orchestrator connects to this wiki's MCP server, their `.mcp.json` entry for `research-wiki` could carry:
>
> ```json
> {
>   "mcpServers": {
>     "research-wiki": {
>       "command": "python3",
>       "args": ["-m", "tools.mcp_server"],
>       "runtime": "harness-openarms-v10"
>     }
>   }
> }
> ```
>
> The wiki's MCP server could read this on connect and attach the runtime to its session context — now calls to `wiki_methodology_guide` or `wiki_gateway_flow` know which consumer is asking. Solo Claude Code conversations don't declare `runtime`; default remains solo. Harness and fleet declare explicitly.
>
> Status: **to explore** — requires back-and-forth with OpenArms and OpenFleet. Not implemented in this session.

## Relationships

- DERIVED FROM: [[right-process-for-right-context-the-goldilocks-imperative|Principle — Right Process for Right Context — The Goldilocks Imperative]]
- DERIVED FROM: [[infrastructure-over-instructions-for-process-enforcement|Principle — Infrastructure Over Instructions for Process Enforcement]]
- DERIVED FROM: [[agent-failure-taxonomy-seven-classes-of-behavioral-failure|Agent Failure Taxonomy — Seven Classes of Behavioral Failure]]
- RELATES TO: [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]]
- RELATES TO: [[model-methodology|Model — Methodology]]
- RELATES TO: [[four-project-ecosystem|Four-Project Ecosystem]]
- FEEDS INTO: [[model-mcp-cli-integration|Model — MCP and CLI Integration]]

## Backlinks

[[right-process-for-right-context-the-goldilocks-imperative|Principle — Right Process for Right Context — The Goldilocks Imperative]]
[[infrastructure-over-instructions-for-process-enforcement|Principle — Infrastructure Over Instructions for Process Enforcement]]
[[agent-failure-taxonomy-seven-classes-of-behavioral-failure|Agent Failure Taxonomy — Seven Classes of Behavioral Failure]]
[[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]]
[[model-methodology|Model — Methodology]]
[[four-project-ecosystem|Four-Project Ecosystem]]
[[model-mcp-cli-integration|Model — MCP and CLI Integration]]
