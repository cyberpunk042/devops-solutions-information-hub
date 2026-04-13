---
title: E014 — Goldilocks Navigable System — Identity to Action in Continuous Flow
aliases:
  - "E014 — Goldilocks Navigable System — Identity to Action in Continuous Flow"
  - "E014 — Goldilocks Navigable System: Identity to Action in Continuous Flow"
type: epic
domain: backlog
status: draft
priority: P0
task_type: epic
current_stage: document
readiness: 65
progress: 60
stages_completed:
artifacts:
  - "wiki/domains/cross-domain/project-self-identification-protocol.md"
confidence: high
created: 2026-04-12
updated: 2026-04-13
sources:
  - id: milestone
    type: file
    file: wiki/backlog/milestones/second-brain-complete-system-v2-0.md
  - id: goldilocks-directive
    type: directive
    file: raw/notes/2026-04-12-goldilocks-higher-ground-directive.md
tags: [epic, goldilocks, navigation, identity, routing, flow, v2, milestone-v2]
---

# E014 — Goldilocks Navigable System — Identity to Action in Continuous Flow
## Summary

Transform the Goldilocks Protocol from a concept page into a NAVIGABLE SYSTEM — a continuous flow from identity declaration through chain selection, model selection, stage routing, artifact production, and feedback. Currently you READ the protocol. After this epic, you FOLLOW it — from any entry point (Obsidian browse, CLI gateway, MCP tool) the flow guides you to the right action for your context. At every decision point: what was selected, why, what alternatives exist, how to override, how to adapt. The flow IS the Goldilocks principle in action.

## Operator Directive

> "AM I a system? Am I a harness? V2? V3? Am I just a solo agent session? What is my domain and my type of project? What make this works? Where is all the magic? What is the intelligence, the structure and the way? What are the ways and level of adhering / using it as needed?"

> "a proper way to lead to the right place in order and move from the top of the tree to any layer downward or from the bottom and upward or anyway along the middle in any direction and always on any direction horizontally on any layer."

> "auto-set on the most logical config from perspective of call by default unless specify and always warned about when auto-detected."

## Goals

- Goldilocks flow navigable as a continuous sequence: identity → chain → model → stage → artifacts → templates → gates → feedback
- Every decision point shows: criteria, default recommendation, alternatives, override mechanism, flexibility explanation
- Auto-detection for what CAN be detected (domain, scale) with explicit WARNINGS ("Auto-detected: typescript. Override with --domain if wrong.")
- Honest "declare this" for what CANNOT be detected (execution mode — the harness decides its own version at runtime)
- Three worked example walkthroughs: solo/wiki, harness-v2/TypeScript, full-system/fleet
- Flow works from Obsidian browse (wikilinks), CLI (gateway commands), AND MCP (tool calls)
- From any point: navigate UP (what selected me?), DOWN (what do I select?), HORIZONTAL (peers at this level)
- Flexibility demonstrated at every step with real per-profile adaptations

## Done When

- [ ] Goldilocks flow page in spine — complete decision sequence with internal anchors per decision point
- [ ] Each decision point has: criteria table, default, alternatives, override, flexibility note
- [ ] Gateway `what-do-i-need` shows auto-detect WARNINGS ("detected: X. override with --Y")
- [ ] Gateway `navigate` incorporates the Goldilocks flow (not just knowledge tree)
- [ ] New gateway `flow` command — walks step-by-step through Goldilocks routing interactively
- [ ] In Obsidian: Goldilocks → any specific stage/model/standard in ≤3 wikilink clicks
- [ ] 3 worked example walkthroughs: solo (this wiki), harness-v2 (OpenArms), full system (OpenFleet)
- [ ] Flexibility shown at every decision point: "For POC, simplify by..." / "For Production, add..."
- [ ] `pipeline post` 0 errors
- [ ] Operator browses Goldilocks from Obsidian and confirms: "I can follow this"

## Scale and Model

> [!info] Epic Parameters
>
> | Parameter | Value |
> |-----------|-------|
> | **Model** | feature-development |
> | **Quality tier** | Skyscraper |
> | **Estimated modules** | 3 (flow design, wiki pages, gateway code) |
> | **Estimated tasks** | 8-12 |
> | **Dependencies** | E010 (models current), E013 (sub-super-models to route into) |

## Module Breakdown

### M1: Flow Design

| Task | What | Est. |
|------|------|------|
| T-E014-01 | Map complete Goldilocks flow: every decision point, branch, default, override | L |
| T-E014-02 | Define per-decision criteria + 3-profile examples (solo, harness, fleet) | M |
| T-E014-03 | Design Obsidian-browsable structure (anchors, wikilinks, callouts per decision) | M |

### M2: Wiki Implementation

| Task | What | Est. |
|------|------|------|
| T-E014-04 | Create Goldilocks flow page in spine (navigable sequence, anchored decision points) | L |
| T-E014-05 | Update Goldilocks concept page → link to flow (concept = WHY, flow = HOW) | M |
| T-E014-06 | Wire flow into sub-super-model (E013) as its navigation guide | M |
| T-E014-07 | Create 3 worked walkthroughs as foldable sections (solo/harness/fleet) | M |

### M3: Gateway Implementation

| Task | What | Est. |
|------|------|------|
| T-E014-08 | Add auto-detect warnings to `what-do-i-need` ("detected: X, override with --Y") | S |
| T-E014-09 | Enhance `navigate` with Goldilocks flow tree (not just knowledge tree) | M |
| T-E014-10 | New `gateway flow` command — interactive step-by-step Goldilocks routing | L |
| T-E014-11 | Test all 3 profiles end-to-end through both gateway and Obsidian browse | M |

## Dependencies

- **E010 (Model Updates):** Flow routes TO models. Models must be current or routing is misleading.
- **E013 (Sub-Super-Models):** Flow routes INTO sub-super-models. They must exist as destinations.
- **Gateway (tools/gateway.py):** Already built the 2026-04-12 session (649+ lines). This epic ENHANCES it, doesn't rebuild it.

## Open Questions

> [!question] ~~Single flow page or sequence of pages?~~
> **RESOLVED:** A single flow page was created (`goldilocks-flow.md`). See [[goldilocks-flow|Goldilocks Flow — From Identity to Action]].

> [!question] ~~How to handle "I don't know my execution mode"?~~
> **RESOLVED:** Gateway what-do-i-need. Auto-detects what it can (domain, scale), says "unknown — declare in CLAUDE.md" for what it can't.
> Can't auto-detect (harness decides at runtime). Recommendation: show capabilities detected, ask user to choose. "We detected harness code. Are you running in harness mode?"

> [!question] ~~How to handle chain upgrades mid-project?~~
> **RESOLVED:** Decision page documenting why. Apply new chain to new tasks. In-progress tasks finish under old chain. No retroactive rework.
> POC→MVP transitions change the recommended chain. The flow should advisory: "Your tests + CI suggest MVP. Consider upgrading to default chain."

## Handoff Context

> [!info] For anyone picking this up in a fresh context:
>
> **What this epic does:** Makes the Goldilocks Protocol navigable — a continuous flow from "who am I?" to "what do I do next?" that works in Obsidian, CLI, and MCP.
>
> **Current state:** Goldilocks concept page exists (~200 lines, 7 dimensions, YAML profiles, auto-detection). Gateway has `what-do-i-need` and `navigate` commands. But the protocol is READ, not FOLLOWED. No flow page exists. Auto-detection doesn't warn. No interactive routing.
>
> **What needs to happen:**
> 1. Design the complete decision flow with every branch and default
> 2. Build as navigable wiki page (anchored decision points, wikilinks, callouts)
> 3. Implement in gateway (warnings, enhanced navigate, new `flow` command)
> 4. Test with 3 real identity profiles end-to-end
>
> **Critical design principle:** The harness decides its own version at runtime. The project can detect capabilities (harness code exists) but NOT the current mode. The flow must handle this honestly — detect what's detectable, declare what isn't, warn on auto-detection.
>
> **Key files:**
> - `wiki/domains/cross-domain/project-self-identification-protocol.md` — current concept page
> - `tools/gateway.py` — current gateway with auto_detect_identity function
> - `wiki/config/sdlc-chains/` — 3 chain configs
> - `wiki/spine/second-brain-integration-chain.md` — 17-step chain (flow should enhance or replace)

## Relationships

- PART OF: [[second-brain-complete-system-v2-0|Milestone — Second Brain Complete System — v2.0]]
- IMPLEMENTS: [[second-brain-integration-requirements|Second Brain Integration System — Full Chain Requirements]] (FR-C1 through FR-C4, FR-B8)
- DEPENDS ON: [[e010-model-updates-all-15-models-reflect-current-knowledge|E010 — Model Updates — All 15 Models Reflect Current Knowledge]]
- DEPENDS ON: [[e013-super-model-evolution-v2-0-with-sub-super-models|E013 — Super-Model Evolution — v2.0 with Sub-Super-Models]]
- BUILDS ON: [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]]
- BUILDS ON: [[right-process-for-right-context-the-goldilocks-imperative|Principle — Right Process for Right Context — The Goldilocks Imperative]]
- FEEDS INTO: [[wiki-gateway-tools-unified-knowledge-interface|Wiki Gateway Tools — Unified Knowledge Interface]] (E015)
- FEEDS INTO: [[e016-integration-chain-proof-end-to-end-with-openarms|E016 — Integration Chain Proof — End to End with OpenArms]] (E016)

## Backlinks

[[second-brain-complete-system-v2-0|Milestone — Second Brain Complete System — v2.0]]
[[second-brain-integration-requirements|Second Brain Integration System — Full Chain Requirements]]
[[e010-model-updates-all-15-models-reflect-current-knowledge|E010 — Model Updates — All 15 Models Reflect Current Knowledge]]
[[e013-super-model-evolution-v2-0-with-sub-super-models|E013 — Super-Model Evolution — v2.0 with Sub-Super-Models]]
[[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]]
[[right-process-for-right-context-the-goldilocks-imperative|Principle — Right Process for Right Context — The Goldilocks Imperative]]
[[wiki-gateway-tools-unified-knowledge-interface|Wiki Gateway Tools — Unified Knowledge Interface]]
[[e016-integration-chain-proof-end-to-end-with-openarms|E016 — Integration Chain Proof — End to End with OpenArms]]
[[e015-gateway-tools-completion-all-requirements-implemented-with-mcp-integration|E015 — Gateway Tools Completion — All Requirements Implemented with MCP Integration]]
