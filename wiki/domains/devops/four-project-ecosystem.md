---
title: Four-Project Ecosystem
aliases:
  - "Four-Project Ecosystem"
type: concept
layer: 2
maturity: growing
domain: devops
status: synthesized
confidence: authoritative
created: 2026-04-08
updated: 2026-04-13
sources:
  - id: src-openfleet-local
    type: documentation
    file: ../openfleet/CLAUDE.md
    title: OpenFleet — Local Project Documentation
    ingested: 2026-04-08
  - id: src-aicp-local
    type: documentation
    file: ../devops-expert-local-ai/CLAUDE.md
    title: AICP — Local Project Documentation
    ingested: 2026-04-08
  - id: src-openarms-local
    type: documentation
    file: raw/articles/openarms-readme.md
    title: OpenArms — Project Documentation
    ingested: 2026-04-08
  - id: src-devops-control-plane-local
    type: documentation
    file: ../devops-control-plane/README.md
    title: devops-control-plane — Local Project Documentation
    ingested: 2026-04-08
  - id: aicp-live-openarms-architecture-analysis
    type: observation
    file: /home/jfortin/devops-expert-local-ai/docs/kb/research/openarms-architecture-analysis.md
    description: "Live AICP research doc — AICP's concrete integration architecture for OpenArms. Captures protocol details (WebSocket ws://localhost:18789, JSON RequestFrame/ResponseFrame/EventFrame), session-key format (acp:uuid, agent:main:wa:peer), 11-row architecture-parallels table (Gateway ↔ Agent daemon, TaskRecord ↔ TaskState, ACP ↔ Fleet agent, etc.), and a 4-phase integration roadmap (MCP → Provider Plugin → ACP Runtime → Full Multimodal). Unique cross-sister-perspective source: AICP analyzing OpenArms as integration target. Verified 2026-04-15."
  - id: devops-control-plane-live-adapters
    type: observation
    file: /home/jfortin/devops-control-plane/docs/ADAPTERS.md
    description: "Live devops-control-plane adapter spec — concretely defines the plugin/adapter protocol (Action → AdapterRegistry → Receipt) that other ecosystem projects follow. Invariant: 'Adapters never raise exceptions.' Feeds the Adapters Never Raise pattern. Verified 2026-04-15."
  - id: devops-control-plane-live-design
    type: observation
    file: /home/jfortin/devops-control-plane/docs/DESIGN.md
    description: "Live devops-control-plane DESIGN.md — product-vision and core pillars. Frames the control plane as a meta-tool: 'Not an application. A structured way to discover what a solution is, what it needs, and how to act on it — through any interface (CLI, Web, TUI), backed by pluggable tool bindings.' Six pillars (Visibility, Integrations, Vaults, Stacks, Automation, Lifecycle). Gives the ecosystem's 'infrastructure governance' project a first-principles description. Verified 2026-04-15."
tags: [devops, ecosystem, openfleet, aicp, devops-control-plane, openarms, research-wiki, architecture, multi-project, integration]
---

# Four-Project Ecosystem

## Summary

The four-project ecosystem is a personal devops infrastructure built by a single engineer running a fleet of AI agents at minimal cost. The core four: OpenFleet (agent workforce and orchestration), AICP (AI control platform and local inference routing), devops-control-plane (project management platform and operational rule origin), and the research wiki (knowledge synthesis spine). OpenArms functions as a fifth project — the personal AI assistant layer providing multi-channel access. Each project has a distinct role with defined integration points; together they form a self-sustaining system where agents do operational work, local inference reduces cloud cost, the control plane enforces governance, and the wiki accumulates knowledge from all activity.

> [!info] Ecosystem Quick Reference
>
> | Project | Primary Role | Integration Point |
> |---------|-------------|-------------------|
> | **OpenFleet** | Agent workforce + orchestration | kb_sync.py ← wiki; doctor.py ← control-plane |
> | **AICP** | Local inference routing + cost reduction | Circuit breaker → fleet agents; docs/kb/ ← wiki |
> | **devops-control-plane** | Project management + operational rules | 24 rules → doctor.py (immune system) |
> | **Research Wiki** | Knowledge synthesis spine | LightRAG export; MCP server (17 tools) |
> | **OpenArms** | Personal AI, 20+ channels | mcporter → wiki MCP; OpenClaw gateway → fleet |

## Key Insights

> [!tip] The wiki is active infrastructure, not passive documentation
> The wiki's knowledge graph (via LightRAG and kb_sync.py) feeds back into OpenFleet's navigator intelligence. The `## Relationships` sections are parsed into explicit relationships that inform agent decision-making. The wiki closes the feedback loop — it is the synthesis layer, not the end of the pipeline.

> [!abstract] File-based integration, not API coupling
> Projects integrate via files and shared protocols, not tightly coupled APIs. The wiki exports to LightRAG (kb_sync.py reads `## Relationships`). AICP exports skills to fleet tooling. devops-control-plane's rules are imported as doctor.py. Loose coupling means projects evolve independently.

**Each project has a single primary role.** OpenFleet runs agents. AICP routes inference. devops-control-plane holds operational wisdom. The wiki synthesizes knowledge. OpenArms provides human access. Overlap is minimal by design.

**devops-control-plane is the operational DNA donor.** Its 24 rules from 16 post-mortems became OpenFleet's immune system (doctor.py). Knowledge flows: operational failure → post-mortem → rule codification → fleet governance. The control-plane is where lessons become law.

**AICP's cost reduction enables scale.** Without routing (LocalAI for simple tasks, Claude for complex ones), running 10 agents continuously would be financially unsustainable. The 5-stage roadmap targets 80%+ Claude token reduction. AICP is the economic enabler.

**All projects run in WSL2 on a single machine.** Not distributed — single-machine ecosystem designed to scale to dual-machine (Alpha + Bravo) when hardware allows.

## Deep Analysis

### Project-by-Project Breakdown

#### OpenFleet — Agent Workforce

| Attribute | Value |
|-----------|-------|
| Repo | openfleet |
| Role | AI agent orchestration, fleet management, project execution |
| Core component | Deterministic orchestrator (30s cycle, zero LLM calls) |
| Agents | 10 specialized agents with SOUL.md identity + HEARTBEAT.md checklist |
| Interfaces | Mission Control (FastAPI + Next.js), Open Gateway (WebSocket), IRC channels |
| Knowledge integration | kb_sync.py parses wiki Relationships into LightRAG graph |
| Cost control | AICP routing, silent heartbeats for idle agents (70% cost reduction) |
| Governance | doctor.py immune system (24 rules, 3-strike), Plane board sync |

#### AICP — AI Control Platform

| Attribute | Value |
|-----------|-------|
| Repo | devops-expert-local-ai |
| Role | Local inference routing, Claude cost reduction, agent capability management |
| Core component | Backend router (LocalAI vs Claude, complexity scoring) |
| Models | 9 loaded: Qwen3 family, Gemma4 family, legacy, specialized |
| Skills | 78 skills in .claude/skills/, 18 referenced in fleet agent-tooling.yaml |
| Integration | Fleet agents use AICP circuit breaker; wiki exports to docs/kb/ |
| Stage | Stage 2 of 5 (routing implemented); targeting 80%+ Claude token reduction |

#### devops-control-plane — Project Management Platform

| Attribute | Value |
|-----------|-------|
| Repo | devops-control-plane |
| Role | Unified project management for any software project |
| Core component | Tech auto-detection engine (20 stacks), AES-256-GCM vault, audit ledger |
| Interfaces | TUI (manage.sh), CLI (Click), Web (Flask SPA) |
| Key export | 24 immune system rules → OpenFleet doctor.py |
| Vault | Potential centralized credential store for all ecosystem projects |

#### Research Wiki — Knowledge Spine

| Attribute | Value |
|-----------|-------|
| Repo | devops-solutions-research-wiki |
| Role | Knowledge synthesis, second brain, central intelligence spine |
| Core component | Ingestion pipeline (5-stage), post-chain (6-step), LightRAG export |
| MCP server | 17 tools exposed to Claude Code and other agents |
| Knowledge export | wiki/domains/ → LightRAG (OpenFleet), docs/kb/ (AICP) |
| Post-mortem record | Captures operational lessons for all ecosystem projects |

#### OpenArms — Personal AI Assistant

| Attribute | Value |
|-----------|-------|
| Repo | openarms (or related) |
| Role | Multi-channel personal AI assistant, human interface layer |
| Channels | 20+ (Telegram, Discord, Slack, Signal, iMessage, WhatsApp, Matrix, IRC...) |
| Architecture | Local Gateway daemon (WebSocket, ws://127.0.0.1:18789) |
| Skills | ClawHub registry; can include Claude Code skills from research wiki |
| MCP | mcporter bridge exposes wiki MCP tools to OpenArms agents |
| Sandbox | Per-session Docker isolation for non-main sessions |

### Integration Map

```
                    ┌─────────────────────────────┐
                    │     Research Wiki            │
                    │  (knowledge synthesis)       │
                    │  wiki/ → LightRAG (kb_sync)  │
                    │  wiki/ → docs/kb/ (export)   │
                    └──────┬──────────┬────────────┘
                           │          │
                    feeds  │          │ feeds
                           ▼          ▼
┌─────────────────┐   ┌────────────────────┐   ┌─────────────────┐
│ devops-control- │   │    OpenFleet       │   │     AICP        │
│    plane        │   │  (agent workforce) │   │  (inference     │
│  (project mgmt) │──►│  doctor.py from   │   │   routing)      │
│  rules → doctor │   │  24 rules          │◄──│  circuit breaker│
│  vault → creds  │   │  AICP routing      │   │  78 skills      │
└─────────────────┘   └────────┬───────────┘   └─────────────────┘
                               │
                               │ OpenClaw gateway
                               ▼
                    ┌──────────────────────┐
                    │     OpenArms         │
                    │  (personal assistant)│
                    │  20+ channels        │
                    │  mcporter → wiki MCP │
                    └──────────────────────┘
```

### Knowledge Flow Direction

> [!tip] The ecosystem is a closed feedback loop
>
> 1. **Operational work** — OpenFleet agents execute tasks, generating incidents and lessons
> 2. **Post-mortem analysis** — devops-control-plane extracts rules from incidents
> 3. **Rules codification** — doctor.py enforces lessons as immune system governance
> 4. **Wiki ingestion** — research wiki synthesizes both lessons and rules
> 5. **LightRAG graph** — kb_sync.py feeds synthesized knowledge back to agent navigators
> 6. **Agents execute better** (informed by graph) → back to step 1
>
> The wiki is not the end of the loop — it is the synthesis layer that closes the feedback cycle.

### The $0 Target

> [!warning] The ecosystem is designed to survive losing any single AI provider
> AICP's 5-stage roadmap targets near-zero Claude API cost by routing 80%+ to local models. OpenFleet's deterministic orchestrator eliminates LLM calls from operational mechanics. The wiki stores all output locally. The long-term design assumes Claude is replaceable: every interface has a local fallback, every skill can execute against a local model, every orchestration step is deterministic.

## Open Questions

- How does the dual-machine target architecture (Alpha + Bravo) change the integration map? (Requires: external research on distributed WSL2/multi-machine fleet architecture; not covered in detail in existing wiki pages beyond the machine table in AICP)
- What is the right cadence for syncing wiki knowledge back to LightRAG — on every post-chain, or on a schedule? (Requires: external research on LightRAG ingestion performance and incremental update semantics; not covered in existing wiki pages)

### Answered Open Questions

> [!example]- Should devops-control-plane's vault be the centralized credential store?
> The vault uses AES-256-GCM with PBKDF2-SHA256 (100K KDF iterations) — robust characteristics. AICP currently uses per-project `.env` files with path protection. The vault's technical characteristics make it suitable as centralized store, but migration requires all five projects to read credentials via the vault API instead of `.env`. The decision is not yet made — both devops-control-plane and AICP flag it as open.

> [!example]- What is the OpenArms → OpenFleet integration story?
> The technical bridge exists: OpenArms agents can reach OpenFleet via its Open Gateway WebSocket (ws://127.0.0.1:18789), and `mcporter` enables MCP tool calls to the fleet's exposed tools. OpenFleet uses IRC channels for agent-to-agent coordination. The integration path is clear; the skill definition for bridging OpenArms ↔ OpenFleet coordination is pending.

> [!example]- Can the wiki's MCP server serve as knowledge layer for OpenArms via mcporter?
> Yes — both OpenArms and MCP Integration Architecture confirm this as an intended path. The wiki MCP server (17 tools) is the natural knowledge query layer. "mcporter enables MCP tool exposure, including the research-wiki MCP server, to OpenArms agents." Integration is technically straightforward via mcporter — the implementation work is connecting `.mcp.json` to the mcporter bridge registration.

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **What principle applies?** | [[right-process-for-right-context-the-goldilocks-imperative|Principle — Right Process for Right Context — The Goldilocks Imperative]] |
> | **What is my identity?** | [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]] |
> | **System map** | [[methodology-system-map|Methodology System Map]] |

## Relationships

- ENABLES: [[openfleet|OpenFleet]]
- ENABLES: [[aicp|AICP]]
- ENABLES: [[openarms|OpenArms]]
- RELATES TO: [[devops-control-plane]]
- FEEDS INTO: [[wiki-knowledge-graph|Wiki Knowledge Graph]]
- RELATES TO: [[mcp-integration-architecture|MCP Integration Architecture]]
- RELATES TO: [[four-project-ecosystem|Four-Project Ecosystem]]
- RELATES TO: [[wsl2-development-patterns|WSL2 Development Patterns]]
- RELATES TO: [[immune-system-rules|Immune System Rules]]
- RELATES TO: [[infrastructure-as-code-patterns|Infrastructure as Code Patterns]]

## Backlinks

[[openfleet|OpenFleet]]
[[aicp|AICP]]
[[openarms|OpenArms]]
[[devops-control-plane|devops-control-plane]]
[[wiki-knowledge-graph|Wiki Knowledge Graph]]
[[mcp-integration-architecture|MCP Integration Architecture]]
[[four-project-ecosystem|Four-Project Ecosystem]]
[[wsl2-development-patterns|WSL2 Development Patterns]]
[[immune-system-rules|Immune System Rules]]
[[infrastructure-as-code-patterns|Infrastructure as Code Patterns]]
[[identity-profile|AICP — Identity Profile]]
[[adapters-never-raise-failure-as-data-at-integration-boundaries|Adapters Never Raise — Failure As Data at Integration Boundaries]]
[[adoption-guide|Adoption Guide — How to Use This Wiki's Standards]]
[[backlog-hierarchy-rules|Backlog Hierarchy Rules]]
[[ecosystem-feedback-loop-wiki-as-source-of-truth|Ecosystem Feedback Loop — Wiki as Source of Truth]]
[[E002-ecosystem-integration|Ecosystem Integration Interfaces]]
[[execution-modes-and-end-conditions|Execution Modes and End Conditions]]
[[methodology-adoption-guide|Methodology Adoption Guide]]
[[methodology-framework|Methodology Framework]]
[[model-ecosystem|Model — Ecosystem Architecture]]
[[model-sfif-architecture|Model — SFIF and Architecture]]
[[identity-profile|OpenArms — Identity Profile]]
[[identity-profile|OpenFleet — Identity Profile]]
[[E004-portable-methodology-engine|Portable Methodology Engine]]
[[identity-profile|Research Wiki — Identity Profile]]
[[scaffold-foundation-infrastructure-features|Scaffold → Foundation → Infrastructure → Features]]
[[skyscraper-pyramid-mountain|Skyscraper, Pyramid, Mountain]]
[[stage-gate-methodology|Stage-Gate Methodology]]
[[super-model|Super-Model — Research Wiki as Ecosystem Intelligence Hub]]
[[src-qwopus-claude-opus-reasoning-distilled-qwen-27b|Synthesis — Qwopus — Claude Opus 4.6 Reasoning Distilled into Local Qwen 27B]]
[[task-type-artifact-matrix|Task Type Artifact Matrix]]
[[the-wiki-is-a-hub-not-a-silo|The Wiki Is a Hub, Not a Silo]]
[[identity-profile|devops-control-plane — Identity Profile]]
