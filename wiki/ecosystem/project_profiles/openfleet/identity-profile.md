---
title: "OpenFleet — Identity Profile"
aliases:
  - "OpenFleet — Identity Profile"
type: reference
domain: cross-domain
status: synthesized
confidence: high
maturity: growing
created: 2026-04-13
updated: 2026-04-13
sources:
  - id: openfleet-fleet-architecture
    type: wiki
    file: wiki/sources/ecosystem-projects/src-openfleet-fleet-architecture.md
  - id: openfleet-concept
    type: wiki
    file: wiki/domains/ai-agents/orchestration/openfleet.md
  - id: openfleet-immune-system
    type: file
    file: raw/articles/openfleet-immune-system.md
  - id: openfleet-methodology-scan
    type: file
    file: raw/articles/openfleet-methodology-scan.md
tags: [ecosystem, project-profile, openfleet, identity, goldilocks]
---

# OpenFleet — Identity Profile

## Summary

The second brain's understanding of OpenFleet as an ecosystem member. OpenFleet is a fleet orchestration framework (TypeScript/Node.js + Python orchestrator) that manages 10 specialized AI agents through deterministic dispatch, an immune system with 3 lines of defense, tier-based trust progression, contribution gating, and standing orders. It is the most architecturally complex project in the ecosystem and the primary source of multi-agent coordination patterns. Its orchestrator makes zero LLM calls — pure Python on a 30-second cycle.

## Identity (Goldilocks)

> [!info] OpenFleet Identity Profile
>
> Per [[execution-mode-is-consumer-property-not-project-property|Consumer-Property Doctrine]] (2026-04-15), rows marked **Stable** / **State** are project fields; rows marked **Consumer/Task** are defaults that apply to OpenFleet's own orchestrator-managed runtime. OpenFleet is a *fleet engineering project* — it BUILDS the orchestrator; its orchestrator is how OpenFleet's own work typically runs.
>
> | Dimension | Layer | Value | Evidence |
> |-----------|-------|-------|----------|
> | **Type** | Stable | system (fleet orchestrator) | Orchestrator + 10 agents + Mission Control + gateway + IRC + knowledge graph |
> | **Domain** | Stable | AI Agent Orchestration (TypeScript/Node + Python) | Agent code in TS, orchestrator in Python, IaC scripts in Bash |
> | **Phase** | State | production | Running fleet with sprints, dispatches, and immune system active |
> | **Scale** | State | large (~3,815 .md files, 2,246-line orchestrator) | 10 live agent workspaces, 219+ KB entries, 42+ IaC scripts |
> | Execution Mode | Consumer/Task (typical) | full system (orchestrator + 10 agents) | Deterministic brain dispatches; agents don't self-direct. Harness-owned loop. Solo still valid for direct operator work in the repo. |
> | SDLC Profile | Consumer/Task (typical) | full | 6 stages (conversation→analysis→investigation→reasoning→work→review), MCP tool blocking per stage |
> | PM Level | Consumer/Task (typical) | L3 (orchestrator-owned) | Deterministic brain decides dispatch, priority, gating; PO sets direction through boards |
> | Trust Tier | Consumer/Task (earned, per-agent per-task-type) | tier-progressive (Trainee→Standard→Expert) | Rolling 20-record approval windows, PO confirms tier changes |

## Execution Mode Detail

> [!abstract] Harness-Owned Loop Architecture
>
> | Component | Role |
> |-----------|------|
> | Deterministic Brain | 12-step cycle, 30s interval, zero LLM calls, pure Python |
> | Orchestrator | Dispatch, gating, budget sync, storm graduation |
> | Agents (10) | Specialized LLM-powered workers with SOUL.md + HEARTBEAT.md |
> | Doctor (immune system) | 30s detection cycle, hidden from agents, 5 named diseases |
> | Mission Control | FastAPI + Next.js UI, task/agent state visualization |
> | Open Gateway | WebSocket sessions for agent heartbeats |
>
> The orchestrator controls ALL dispatch. Agents execute assigned work but never self-direct, choose tasks, or modify their own role/tier. This is the harness-owned-loop pattern at its most evolved form.

## What the Brain Learned FROM OpenFleet

These are cross-referenced to the wiki's lesson and pattern pages — the second brain's distilled understanding, not OpenFleet documentation.

> [!tip] Key Lessons Contributed
>
> | Lesson | What OpenFleet Proved |
> |--------|---------------------|
> | [[harness-ownership-converges-independently-across-projects|Harness Ownership Converges Independently]] | OpenFleet and OpenArms independently evolved harness-owns-loop — convergent evolution confirms the pattern |
> | [[infrastructure-enforcement-proves-instructions-fail|Infrastructure Enforcement Proves Instructions Fail]] | MCP tool blocking at server level is stronger than hooks — tool call refused before reaching any handler |
> | [[never-skip-stages-even-when-told-to-continue|Never Skip Stages Even When Told to Continue]] | 6-stage model with per-stage tool blocking enforces this structurally |
> | [[context-management-is-primary-productivity-lever|Context Management Is the Primary LLM Productivity Lever]] | 10x cost difference between expert (full context) and lightweight (title+stage only) |
> | [[structured-context-is-proto-programming-for-ai-agents|Structured Context Is Proto-Programming for AI Agents]] | Validation matrix: 29 scenarios, same structural skeleton, content varies — shape constant |

> [!tip] Key Patterns Observed
>
> | Pattern | How OpenFleet Implements It |
> |---------|--------------------------|
> | [[three-lines-of-defense-immune-system-for-agent-quality|Three Lines of Defense]] | Prevention (tool blocking + contribution gates) → Detection (30s doctor: 5 diseases) → Correction (TEACH→COMPACT→PRUNE→ESCALATE) |
> | [[harness-owned-loop-deterministic-agent-execution|Harness-Owned Loop]] | Orchestrator dispatches, agents execute. Zero LLM calls in control loop. Storm graduation limits dispatch. |
> | [[contribution-gating-cross-agent-inputs-before-work|Contribution Gating]] | Synergy matrix (115 lines YAML): required/recommended/conditional per role pair. Task blocked until all required contributions received. |
> | [[tier-based-context-depth-trust-earned-through-approval-rates|Tier-Based Context Depth]] | Trainee→Standard (85%+)→Expert. Per-task-type overrides. Rolling 20-record windows. PO confirms, data recommends. |
> | [[validation-matrix-test-suite-for-context-injection|Validation Matrix]] | 29 scenarios (TK-*, HB-*, FL-*) testing context injection. Each: exact expected context + expected behavior. |
> | [[deterministic-shell-llm-core|Deterministic Shell, LLM Core]] | Brain is pure Python; LLM calls happen only inside agent execution, never in orchestration |
> | [[enforcement-hook-patterns|Enforcement Hook Patterns]] | MCP tool blocking per stage in methodology.yaml — stronger than hooks, refused at server level |

## Unique Discoveries

Patterns that the second brain learned ONLY from OpenFleet — not observed in other ecosystem projects:

- **5 named diseases with detection functions**: Deviation, Laziness, Protocol violation, Confident-but-wrong (3+ corrections), Scope creep. Each has a specific detection function in doctor.py.
- **Storm graduation**: CRITICAL→full stop, STORM→no dispatch, WARNING→limit to 1. Orchestrator responds proportionally to severity.
- **Standing orders**: Per-role autonomous authority levels (conservative/standard/autonomous). Escalation: 2 autonomous actions without feedback → PO alert.
- **Readiness vs progress as two fields**: `task_readiness` (0-99, pre-dispatch, PO sets) vs `task_progress` (0-100, post-dispatch, agent reports). Readiness gates at 99. See [[readiness-vs-progress|Readiness vs Progress — Two-Dimensional Work Tracking]].
- **5 cognitive contexts**: OpenArms discovered this (5 contexts reading one CLAUDE.md), but OpenFleet's agent diversity (10 agents, each with different SOUL.md) makes the problem structural. Each agent needs context shaped for its role.

## Artifact Chain (Project-Specific)

OpenFleet uses a TypeScript/Node domain chain for agent code and a Python chain for the orchestrator. The fleet's 6-stage model (conversation→analysis→investigation→reasoning→work→review) is a valid alternate instance of the methodology framework — different stage names from the wiki's 5-stage model, same structural concept.

> [!abstract] OpenFleet Artifact Summary
>
> | Domain | Key Artifacts | Gate |
> |--------|---------------|------|
> | Agent code (TS) | SOUL.md (identity), HEARTBEAT.md (checklist), role-specific hooks, skill files | Agent config validated by orchestrator |
> | Orchestrator (Python) | 12-step cycle, doctor.py, navigator.py, dispatcher.py | Zero LLM calls in control loop |
> | Infrastructure (IaC) | 42+ scripts, setup.sh (zero-to-fleet), service configs | `setup.sh` runs clean |
> | Knowledge base | 219+ KB entries, synergy matrix, tier profiles, standing orders (all YAML) | kb_sync parses into LightRAG graph |
> | Methodology | methodology.yaml, stage definitions, tool blocking per stage | MCP server enforces |

**Toolchain:** pnpm, TypeScript, OpenClaw + Mission Control, FastAPI, Next.js, LightRAG, LocalAI, PostgreSQL, Redis, IRC

See [[domain-chain-typescript|Artifact Chain — TypeScript-Node Domain]] for the generic TS chain and [[artifact-chains-by-model|Artifact Chains by Methodology Model]] for the framework.

## Methodology Adaptations

> [!info] How OpenFleet Customizes the Methodology
>
> | Aspect | Standard (Wiki) | OpenFleet Override |
> |--------|-----------------|-------------------|
> | Stage names | document→design→scaffold→implement→test | conversation→analysis→investigation→reasoning→work→review |
> | Stage count | 5 | 6 (adds review as explicit stage) |
> | Enforcement level | Advisory (default profile) | Enforced (MCP tool blocking per stage) |
> | PM level | L1 or L2 | L3 (orchestrator makes dispatch decisions, PO sets strategy through boards) |
> | Trust model | Static or per-session | Dynamic per-agent per-task-type, data-driven with PO confirmation |
> | Immune system | N/A at methodology level | 3 lines of defense, hidden from agents, 30s doctor cycle |
> | Budget integration | Not in methodology | Budget mode changes propagate to heartbeat intervals, CRON tempo |

## Integration with Second Brain

> [!abstract] Adoption Status
>
> | Component | Status |
> |-----------|--------|
> | CLAUDE.md as routing table | Adopted (per-agent SOUL.md + global CLAUDE.md) |
> | Three-layer root docs (AGENTS.md + CLAUDE.md + per-agent personas) | Partial — SOUL.md already acts as per-agent Layer 2; AGENTS.md as Layer 1 is a candidate upgrade. See [[root-documentation-map|Root Documentation Map]] |
> | methodology.yaml | Adopted (6-stage model, tool blocking) |
> | Stage enforcement | Adopted (MCP tool blocking — strongest in ecosystem) |
> | Wiki knowledge base | Active (219+ KB entries synced via kb_sync → LightRAG) |
> | Export from second brain | Pending (E002 defines the integration interface) |
> | Feed-back TO second brain | Active (fleet architecture synthesis + 5 patterns extracted) |

### How This Connects — Navigate From Here

> [!abstract] From This Profile → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **Ecosystem overview** | [[four-project-ecosystem|Four-Project Ecosystem]] |
> | **Enforcement comparison** | [[openarms-vs-openfleet-enforcement|OpenArms vs OpenFleet Enforcement Architecture]] |
> | **Full synthesis source** | [[src-openfleet-fleet-architecture|Synthesis — OpenFleet Fleet Architecture — Immune System, Dispatch, and Tiers]] |
> | **Immune system rules** | [[immune-system-rules|Immune System Rules]] |
> | **Generic artifact framework** | [[artifact-chains-by-model|Artifact Chains by Methodology Model]] |
> | **OpenArms comparison** | [[identity-profile|OpenArms — Identity Profile]] |
> | **Methodology model** | [[model-methodology|Model — Methodology]] |
> | **Ecosystem model** | [[model-ecosystem|Model — Ecosystem Architecture]] |

## Relationships

- PART OF: [[four-project-ecosystem|Four-Project Ecosystem]]
- DERIVED FROM: [[src-openfleet-fleet-architecture|Synthesis — OpenFleet Fleet Architecture — Immune System, Dispatch, and Tiers]]
- RELATES TO: [[openarms-vs-openfleet-enforcement|OpenArms vs OpenFleet Enforcement Architecture]]
- RELATES TO: [[model-methodology|Model — Methodology]]
- RELATES TO: [[model-ecosystem|Model — Ecosystem Architecture]]
- RELATES TO: [[immune-system-rules|Immune System Rules]]
- FEEDS INTO: [[artifact-chains-by-model|Artifact Chains by Methodology Model]]
- FEEDS INTO: [[three-lines-of-defense-immune-system-for-agent-quality|Three Lines of Defense — Immune System for Agent Quality]]
- FEEDS INTO: [[harness-owned-loop-deterministic-agent-execution|Harness-Owned Loop — Deterministic Agent Execution]]
- FEEDS INTO: [[contribution-gating-cross-agent-inputs-before-work|Contribution Gating — Cross-Agent Inputs Before Work]]
- FEEDS INTO: [[tier-based-context-depth-trust-earned-through-approval-rates|Tier-Based Context Depth — Trust Earned Through Approval Rates]]
- FEEDS INTO: [[validation-matrix-test-suite-for-context-injection|Validation Matrix — Test Suite for Context Injection]]

## Backlinks

[[four-project-ecosystem|Four-Project Ecosystem]]
[[src-openfleet-fleet-architecture|Synthesis — OpenFleet Fleet Architecture — Immune System, Dispatch, and Tiers]]
[[openarms-vs-openfleet-enforcement|OpenArms vs OpenFleet Enforcement Architecture]]
[[model-methodology|Model — Methodology]]
[[model-ecosystem|Model — Ecosystem Architecture]]
[[immune-system-rules|Immune System Rules]]
[[artifact-chains-by-model|Artifact Chains by Methodology Model]]
[[three-lines-of-defense-immune-system-for-agent-quality|Three Lines of Defense — Immune System for Agent Quality]]
[[harness-owned-loop-deterministic-agent-execution|Harness-Owned Loop — Deterministic Agent Execution]]
[[contribution-gating-cross-agent-inputs-before-work|Contribution Gating — Cross-Agent Inputs Before Work]]
[[tier-based-context-depth-trust-earned-through-approval-rates|Tier-Based Context Depth — Trust Earned Through Approval Rates]]
[[validation-matrix-test-suite-for-context-injection|Validation Matrix — Test Suite for Context Injection]]
