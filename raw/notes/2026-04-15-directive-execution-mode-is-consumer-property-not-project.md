---
title: "Operator directive — execution mode is a consumer property, not a project property; conflation slid back in"
type: note
domain: log
status: active
note_type: directive
created: 2026-04-15
updated: 2026-04-15
tags: [operator-directive, verbatim, execution-mode, consumer-property, conflation, drift, mcp-config, goldilocks, identity]
---

# Operator Directive — Execution Mode Is a Consumer Property, Not a Project Property

## Context

Near end of long 2026-04-15 session. I had run `python3 -m tools.gateway what-do-i-need` during the entrypoint-exercise iteration (iteration 6) and reported the tool's output, marking `execution mode: solo — no harness code found → solo is certain` as "correct." Operator pushed back on the earlier "identity detection" framing in general and then specifically on the execution-mode claim.

## Verbatim Operator Messages (this directive)

> "what do you mean identify detection ? what identity detection ? we had a conlation on that in the past where the AI would think a project is frozen to a model...."

> "I am just saying you cannot know if the project is being use by a harness or a full system if you are not in the full system or the harness.... a project is always solo by default...."

> "yes. its probably a conflation that was slidded back in..... it would require development in back and forth with openarms and openfleet to allow them to use the tool and it detect automatically or simply maybe just inside the mcp config ? to explore."

## The Directives Distilled

### 1. Execution mode is a property of the CONSUMER, not the project

- A project is always **solo by default.** Solo is the zero state.
- A harness (OpenArms v10 runtime) or fleet (OpenFleet orchestrator) WRAPS a project from outside. The harness's runtime is what knows "I'm running this project in harness mode."
- From INSIDE the project directory, you cannot see whether a harness elsewhere is consuming your artifacts. Local absence of harness code ≠ project is not being used in harness mode.
- Therefore: "no harness code found → solo is certain" is a tautology dressed as detection. The wiki cannot detect the non-default cases from its own vantage point.

### 2. This is the same class of conflation as "project frozen to a model"

- Prior conflation (caught in an earlier session): AI treated a project as bound to ONE methodology model forever. Correction: methodology model is per TASK (bug → bug-fix model, feature → feature-development model, docs → documentation model).
- Current conflation (slid back in): `gateway what-do-i-need` picks ONE SDLC profile for the whole project based on auto-"detected" identity, collapsing layers that should remain orthogonal:
  - **Stable identity** (type, second-brain) → declared, never detected
  - **Phase/scale** → declared, heuristic at best a sanity signal
  - **SDLC profile** → per task, not per project
  - **Methodology model** → per task, not per project
  - **Execution mode** → **property of the consumer's runtime**, not the project

### 3. Guard against conflations sliding back in

- The phrase "probably a conflation that was slidded back in" is the core observation: corrections decay. A rule written once in prose erodes unless encoded structurally.
- Fix must be structural (tool behavior changes, lint or schema enforces the distinction), not prose ("remember that execution mode is not detectable").

### 4. Real detection requires cross-project signaling — to EXPLORE, not implement

- Genuine "execution mode" awareness requires the CONSUMER (harness/fleet) to signal its identity to the wiki when connecting.
- Operator's proposal to explore: **the MCP config** of the consuming client could carry this declaration — when OpenArms/OpenFleet connect to `research-wiki` MCP, their `.mcp.json` entry could declare `runtime: harness-openarms-v10` or `runtime: fleet-openfleet-v1` vs default `runtime: solo-claude`.
- Status: "to explore" — do not implement; record as an open design question for future back-and-forth with the OpenArms and OpenFleet teams.

## Fix Scope (this session)

1. **Log this directive verbatim** (this file) per verbatim-always methodology.
2. **Fix `tools/gateway.py what-do-i-need`** to stop claiming to "detect" things it cannot:
   - Remove "no harness code found → solo is certain" — replace with: "solo is the default; consumers (harnesses/fleets) declare non-default"
   - Treat declared values in CLAUDE.md/CONTEXT.md as **authoritative**, heuristics as **sanity signals only**
   - Stop picking ONE SDLC profile for the project — surface the menu of profiles with selection criteria tied to the TASK at hand
3. **Create wiki lesson** documenting the class of conflation, with structural prevention: consumer-property vs project-property distinction, per-task-not-per-project for methodology model, declared-over-detected for all identity dimensions.
4. **Record Open Question** about MCP-config-based consumer-runtime signaling as future exploration.

## Standing Rules Going Forward

1. **Solo is the default.** Any tool that "detects" a non-default execution mode from inside the project is lying.
2. **Execution mode, methodology model, stage, and SDLC profile are consumer/task properties, not project properties.** Project properties = stable identity (type, second-brain, domain).
3. **Declared > detected** for ALL identity dimensions. Heuristics are sanity signals, not sources of truth.
4. **When a conflation is named + corrected, encode the correction structurally** (schema, lint, tool behavior) — prose alone erodes.
5. **Consumer-runtime signaling (if implemented) belongs in the MCP config** of the consuming client, not in heuristic detection from the hosted project.

## Cross-Reference

Reinforces and deepens:
- Earlier 2026-04-15 directives: no-caps, no-lowering, openarms-is-dumb, project-based-source-mechanism
- Foundational Goldilocks principle ([[right-process-for-right-context-the-goldilocks-imperative]]) — right process for right context, not one process for the whole project
- Agent Failure Taxonomy (Class 7: Memory/Wiki conflation) — this is a structural variant of the same class

## Why This Was Logged Verbatim

Per `feedback_verbatim_always.md` — operator directives logged verbatim in `raw/notes/` BEFORE acting, proactively. Logging this one was triggered by the operator's explicit confirmation to act ("yes") on the two-part fix (tool + lesson) plus the future-exploration note on MCP-config-based consumer signaling.
