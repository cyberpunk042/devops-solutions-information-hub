---
title: OpenFleet
aliases:
  - "OpenFleet"
type: concept
layer: 2
maturity: growing
domain: ai-agents
status: synthesized
confidence: authoritative
created: 2026-04-08
updated: 2026-04-10
sources:
  - id: src-openfleet-local
    type: documentation
    file: ../openfleet/CLAUDE.md
    title: OpenFleet — Local Project Documentation
    ingested: 2026-04-08
tags: [openfleet, ai-agents, fleet-management, orchestration, deterministic-brain, vibe-managing, mission-control, openclaw, lightrag, multi-agent]
---

# OpenFleet

## Summary

OpenFleet is an AI-native project lifecycle orchestration framework implementing "Vibe Managing" — the shift from directing individual AI models via prompts to governing a fleet of 10 intelligent agents through declarative systems and deterministic orchestration. The human user (Product Owner) sets direction through structured management boards (tempo, phase, risk posture, budget). A deterministic orchestrator (zero LLM calls, pure Python) handles all operational mechanics on a 30-second cycle. AI agents are first-class assignable contributors — persistent, accountable, with roles, permissions, and earned trust. The system runs on OpenClaw + Mission Control with LightRAG for knowledge graph intelligence, LocalAI for routine inference, and Claude for complex reasoning.

## Key Insights

- **Deterministic brain, not LLM-driven**: The orchestrator runs every 30 seconds with zero LLM calls. Pure Python logic handles state diffing, budget gating, heartbeat scheduling, task dispatch, security scanning, and anomaly detection. This makes orchestration predictable, auditable, and cheap.

> [!info] Fleet architecture reference card
>
> | Layer | Component | Role |
> |-------|-----------|------|
> | L0 | Persistent state graph | Substrate — task, agent, board state |
> | L1 | Deterministic Brain | 12-step cycle, zero LLM calls, 30-second interval |
> | L2 | Orchestration | Dispatch, gating, budget, security scan |
> | L3 | Agent Execution | 10 specialized agents (LLM-powered) |
> | L4 | Capability & Extension | Skills, 13 MCP tools |
> | L5 | Interaction | Prompts, @mentions, Mission Control UI, API |
> | L6 | Observability & Governance | doctor.py immune system, audit ledger |

- **10 specialized agents**: fleet-ops, project-manager, devsecops, architect, software-engineer, qa-engineer, devops, technical-writer, ux-designer, accountability-generator. Each has SOUL.md (identity) + HEARTBEAT.md (periodic checklist).

> [!abstract] Multi-dimensional state replaces single "status" field
> 6 orthogonal axes: lifecycle, execution, progress, readiness, validation, context. Enables nuanced decisions like "ready for review but blocked by dependency."

**kb_sync.py replaces LLM-based extraction.** LightRAG's hermes 7B produced inconsistent results. kb_sync extracts from `## Relationships` directly — zero randomness, zero model dependency. 1,545 entities, 2,295 relationships from 219 KB entries.

**Dual-board sync.** Plane (PM, human-driven: sprints, epics, velocity) ↔ Mission Control (ops, agent-driven: tasks, dispatches, heartbeats). 5 sync mechanisms: structural, state, semantic, event-driven, intent.

**IaC-only operations.** No manual commands. 42+ scripts in `scripts/`. Zero to running fleet via `setup.sh`.

## Deep Analysis

### Orchestrator 12-Step Cycle

Every 30 seconds (configurable: turbo=5s, standard=30s, economic=60s):
1. Storm monitor evaluation
2. Gateway duplication check
3. Fleet mode gate
4. Refresh agent contexts (pre-embed full per-agent data to disk)
5. Security scan (behavioral security on new/changed tasks)
6. Doctor run (immune system: detect + respond to anomalies)
7. Ensure review approvals
8. Wake drivers (alert fleet-ops and PM about pending work)
9. Dispatch ready tasks (unblocked inbox tasks, max 2/cycle)
10. Process directives (parse PO directives from board memory)
11. Evaluate parents (when all children done, parent moves to review)
12. Health check (detect stuck tasks, offline agents)

### Service Infrastructure

| Service | Port | Purpose |
|---------|------|---------|
| Mission Control API | 8000 | FastAPI backend |
| Mission Control UI | 3000 | Next.js frontend |
| Open Gateway | ws://18789 | Agent sessions, heartbeats |
| IRC (miniircd) | 6667 | 10 channels: #fleet, #alerts, #reviews, etc. |
| The Lounge | 9000 | Web IRC client |
| LocalAI | 8090 | 9 models loaded |
| LightRAG | 9621 | Knowledge graph + API |
| PostgreSQL | 5432 | Mission Control DB |
| Redis | 6379 | Caching, RQ queue |

### Knowledge Base

219+ KB entries in `docs/knowledge-map/kb/` organized by branches (systems, tools, hooks, commands, skills, plugins, infrastructure). kb_sync parses these into LightRAG graph. Also indexes AICP SKILL.md files (78 skills from devops-expert-local-ai).

### Four-Project Ecosystem

| Project | Repo | Purpose |
|---------|------|---------|
| Fleet | openfleet | Agent operations, orchestrator, infrastructure |
| AICP | devops-expert-local-ai | AI Control Platform, LocalAI independence |
| DSPD | devops-solution-product-development | Project management via Plane |
| Research Wiki | devops-solutions-research-wiki | Knowledge synthesis, central intelligence spine |

## Open Questions

- How does fleet performance scale beyond 10 agents (20, 50)? (Requires: external research or empirical testing; the Agent Orchestration Patterns page notes this is an open scale question without documented answers in existing wiki pages)

### Answered Open Questions

**Q: What is the optimal heartbeat frequency per agent role for cost vs responsiveness?**

Cross-referencing `Agent Orchestration Patterns` and `Four-Project Ecosystem`: the answer varies by role and is already partially resolved by the silent heartbeat strategy. The `Four-Project Ecosystem` page documents: "silent heartbeats for idle agents save 70% cost." The `Agent Orchestration Patterns` page confirms the three cycle speed modes — turbo=5s (high responsiveness, high cost), standard=30s (balanced), economic=60s (low cost, reduced responsiveness). The optimal frequency per role is: fleet-ops (30m heartbeat, as documented) operates at a much lower frequency than the orchestrator cycle because its role is strategic coordination, not real-time dispatch. The `Immune System Rules` page documents that the 3-strike window is tuned for the standard 30s cycle — turbo mode risks false positive escalation. The practical answer: active task-executing agents (software-engineer, qa-engineer) benefit from standard=30s; idle agents should be silenced; fleet-ops operates at its own 30m cadence independent of the orchestrator cycle. The economic=60s mode is appropriate for non-critical background agents (technical-writer, ux-designer) when no active sprint is running.

**Q: Can the deterministic brain's 12-step cycle be extended with plugin hooks?**

Cross-referencing `Harness Engineering` and `Immune System Rules`: yes, and the mechanism is already designed for it. The `Harness Engineering` page documents that the harness pattern hierarchy includes "Level 3: Runtime guardrails via hooks, TypeScript engine" — the deterministic orchestrator is Level 4, and hooks can be added at the execution boundaries. The `Immune System Rules` page documents that doctor.py runs at step 6 of the 12-step cycle — a pre-existing plugin point. The `Harness Engineering` page also notes: "PreToolUse hooks for measuring skill usage, PostToolUse hooks for auto-formatting, Stop hooks to nudge Claude to verify." Applied to the orchestrator: each numbered step is a natural plugin point where a Python callable could be registered and invoked. The `Agent Orchestration Patterns` page's answered question on "minimal orchestration overhead" confirms the pipeline chains (`python3 -m tools.pipeline chain ingest`) already implement a hook-based extension model at Level 2. Extending the 12-step cycle with registered Python callables per step is architecturally consistent with the ecosystem's IaC-only philosophy.

**Q: What is the failure mode when LightRAG and LocalAI are both down?**

Cross-referencing `Immune System Rules` and `Four-Project Ecosystem`: the orchestrator is designed to degrade gracefully because LLM calls are excluded from the control loop by design. The `Immune System Rules` page lists "LLM backend circuit breaker open (AICP pattern applied at fleet level)" as a Resource Rule in the immune system — this means the doctor detects backend failure and quarantines tasks that would require LLM inference before they are dispatched. The `Four-Project Ecosystem` page documents: "AICP implements a circuit breaker (CLOSED → OPEN → HALF_OPEN) per backend" — when LocalAI is down, the circuit opens and AICP falls back to Claude for critical tasks. When LightRAG is down, the Navigator (fleet/core/navigator.py) loses graph-based context assembly but the orchestrator's 12 deterministic steps continue unaffected because they make zero LLM calls. The failure mode is degraded-but-functional: tasks are dispatched with reduced context quality (no LightRAG graph traversal for agent context), and any task requiring LLM inference for execution is queued until LocalAI or Claude becomes available. The fleet does not halt.

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **What principle applies?** | [[right-process-for-right-context-the-goldilocks-imperative|Principle — Right Process for Right Context — The Goldilocks Imperative]] |
> | **What is my identity?** | [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]] |
> | **System map** | [[methodology-system-map|Methodology System Map]] |

## Relationships

- IMPLEMENTS: [[openclaw|OpenClaw]]
- USED BY: [[ai-driven-content-pipeline|AI-Driven Content Pipeline]]
- BUILDS ON: [[lightrag|LightRAG]]
- BUILDS ON: [[aicp|AICP]]
- RELATES TO: [[plane|Plane]]
- RELATES TO: [[devops-control-plane]]
- ENABLES: [[claude-code-skills|Claude Code Skills]]
- RELATES TO: [[llm-wiki-pattern|LLM Wiki Pattern]]
- FEEDS INTO: [[wiki-knowledge-graph|Wiki Knowledge Graph]]

## Backlinks

[[openclaw|OpenClaw]]
[[ai-driven-content-pipeline|AI-Driven Content Pipeline]]
[[lightrag|LightRAG]]
[[aicp|AICP]]
[[plane|Plane]]
[[devops-control-plane|devops-control-plane]]
[[claude-code-skills|Claude Code Skills]]
[[llm-wiki-pattern|LLM Wiki Pattern]]
[[wiki-knowledge-graph|Wiki Knowledge Graph]]
[[agent-orchestration-patterns|Agent Orchestration Patterns]]
[[always-plan-before-executing|Always Plan Before Executing]]
[[claude-code|Claude Code]]
[[claude-code-scheduling|Claude Code Scheduling]]
[[context-management-is-primary-productivity-lever|Context Management Is the Primary LLM Productivity Lever]]
[[local-model-vs-cloud-api-for-routine-operations|Decision — Local Model vs Cloud API for Routine Operations]]
[[deterministic-shell-llm-core|Deterministic Shell, LLM Core]]
[[E002-ecosystem-integration|Ecosystem Integration Interfaces]]
[[four-project-ecosystem|Four-Project Ecosystem]]
[[gateway-centric-routing|Gateway-Centric Routing]]
[[graph-enhanced-retrieval-bridges-wiki-and-vector-search|Graph-Enhanced Retrieval Bridges Wiki Navigation and Vector Search]]
[[harness-engineering|Harness Engineering]]
[[immune-system-rules|Immune System Rules]]
[[infrastructure-as-code-patterns|Infrastructure as Code Patterns]]
[[llm-maintained-wikis-outperform-static-documentation|LLM-Maintained Wikis Outperform Static Documentation]]
[[local-llm-quantization|Local LLM Quantization]]
[[mcp-integration-architecture|MCP Integration Architecture]]
[[model-ecosystem|Model — Ecosystem Architecture]]
[[multi-channel-ai-agent-access|Multi-Channel AI Agent Access]]
[[multi-stage-ingestion-beats-single-pass|Multi-Stage Ingestion Beats Single-Pass Processing]]
[[openarms|OpenArms]]
[[plan-execute-review-cycle|Plan Execute Review Cycle]]
[[rework-prevention|Rework Prevention]]
[[scaffold-foundation-infrastructure-features|Scaffold → Foundation → Infrastructure → Features]]
[[skills-architecture-is-dominant-extension-pattern|Skills Architecture Is the Dominant LLM Extension Pattern]]
[[src-openclaw-billing-proxy|Source — openclaw-billing-proxy: Billing Proxy for OpenClaw via Claude Subscription]]
[[src-vercel-opensrc-toolkit|Source — vercel-labs/opensrc: Source Code Access Toolkit for AI Agents]]
[[spec-driven-development|Spec-Driven Development]]
[[src-harness-engineering|Synthesis — Claude Code Harness Engineering]]
[[src-gemma4-searxng-openclaw|Synthesis — Gemma 4 + SearXNG for Free Private OpenClaw]]
[[task-lifecycle-stage-gating|Task Lifecycle Stage-Gating]]
[[wiki-backlog-pattern|Wiki Backlog Pattern]]
