---
title: "Model: Ecosystem Architecture"
type: concept
domain: cross-domain
layer: spine
status: synthesized
confidence: high
maturity: growing
created: 2026-04-09
updated: 2026-04-09
sources: []
tags: [ecosystem, model, openfleet, aicp, openarms, devops-control-plane, multi-project, integration, spine, architecture]
---

# Model: Ecosystem Architecture

## Summary

The Ecosystem Architecture model describes how five projects — OpenFleet, AICP, devops-control-plane, the research wiki, and OpenArms — form a self-sustaining system where each project has a single primary role and defined integration points. OpenFleet runs the agents. AICP routes inference cheaply. devops-control-plane holds operational wisdom. The wiki synthesizes knowledge and feeds the agent intelligence graph. OpenArms provides multi-channel personal access. Projects integrate via files and shared protocols, not tightly coupled APIs — enabling independent evolution while maintaining system coherence. This model is the map of the entire ecosystem: understand it to understand why every other spine model exists.

## Key Insights

- **Minimal overlap is a design constraint, not an accident**: each project does one thing and hands off at a clean boundary. When a project starts doing what another project is responsible for, the integration contract breaks. The single-responsibility discipline is what makes the ecosystem evolvable rather than monolithic.

- **The wiki is active infrastructure, not passive docs**: the wiki's `## Relationships` sections are parsed by `kb_sync.py` into a LightRAG knowledge graph that feeds OpenFleet's navigator intelligence. 2,295 explicit relationships currently inform agent decision-making. Every wiki page added is a node added to the fleet's intelligence graph — this is why knowledge synthesis matters operationally.

- **devops-control-plane is the operational DNA donor**: 24 rules extracted from 16 post-mortems became OpenFleet's immune system (`doctor.py`). The control-plane is where operational failure becomes codified law. Knowledge flows in one direction: failure → post-mortem → rule → governance enforcement. The control-plane is a living rulebook, not a monitoring dashboard.

- **AICP is the economic enabler**: without local inference routing, running 10 agents continuously at Claude API rates would be unsustainable. AICP's 5-stage LocalAI independence roadmap targets 80%+ Claude token reduction. LocalAI handles routine tasks; Claude handles complex reasoning. The cost reduction unlocks the scale; the scale creates the ecosystem's value.

- **File-based integration is the coherence mechanism**: projects communicate via files and shared protocols (markdown exports, LightRAG graph, JSON manifests), not tightly coupled APIs. This means any project can be replaced or rewritten without taking down the ecosystem. The interfaces are durable even when the implementations change.

## Deep Analysis

### The Five Projects and Their Roles

**OpenFleet — The Agent Workforce**

OpenFleet implements "Vibe Managing" — governing a fleet of 10 specialized AI agents through declarative systems rather than directing individual models via prompts. The human Product Owner sets direction through structured management boards (tempo, phase, risk posture, budget). A deterministic orchestrator (zero LLM calls, pure Python, 30-second cycle) handles all operational mechanics: state diffing, budget gating, heartbeat scheduling, task dispatch, security scanning, anomaly detection.

10 specialized agents: fleet-ops, project-manager, devsecops-expert, architect, software-engineer, qa-engineer, devops, technical-writer, ux-designer, accountability-generator. Each has a `SOUL.md` (identity file) and `HEARTBEAT.md` (periodic checklist). Agents connect through OpenClaw (WebSocket gateway) and are managed via Mission Control UI.

See [[OpenFleet]] for architecture depth, the seven-layer stack, and LightRAG integration details.

**AICP — The AI Control Platform**

AICP (AI Control Platform) is the inference routing layer: it scores incoming tasks by complexity and routes them to LocalAI (free, local inference) or Claude (cloud, billed) accordingly. The complexity scorer assigns a 0-10 score; tasks below the threshold go local; tasks above route to Claude. This makes the fleet's inference costs scale with task complexity rather than request volume.

The 5-stage roadmap targets progressive LocalAI independence: LocalAI for routine tasks → complex reasoning → 78 skills migrated → voice pipeline → full local-first operation. At full roadmap completion, Claude API costs reduce by 80%+.

AICP also exports skills to fleet agent tooling — the inference profiles and guardrail configurations become available to OpenFleet agents as loadable tools.

See [[AICP]] for routing logic, circuit breaker behavior, and the 5-stage independence roadmap.

**devops-control-plane — The Operational Governance Origin**

The devops-control-plane is the project management platform built before the rest of the ecosystem existed. Its primary operational contribution: 16 post-mortems over its operational lifetime produced 24 rules that became OpenFleet's `doctor.py` immune system.

The control-plane is not a monitoring system — it is a governance codification system. When something goes wrong, the lesson gets extracted, formalized as a rule, and committed to the shared ruleset. OpenFleet's `doctor.py` enforces these rules on every agent action: budget checks, security scans, anomaly flags. The control-plane is the ecosystem's institutional memory made executable.

See [[devops-control-plane]] and [[Immune System Rules]] for the 24 rules and their operational origins.

**Research Wiki — The Central Intelligence Spine**

The wiki synthesizes knowledge from all projects, external sources, and operational experience into a structured, interlinked knowledge graph. Its role in the ecosystem is dual:

1. **Knowledge synthesis**: raw sources (articles, transcripts, project docs, post-mortems) become structured pages (concepts, lessons, patterns, decisions) through the ingestion and evolution pipeline.
2. **Agent intelligence**: the wiki's `## Relationships` sections are parsed by `kb_sync.py` into the LightRAG graph that OpenFleet's navigator uses for knowledge-grounded decision-making.

The wiki is not a documentation repository. It is infrastructure that feeds agent intelligence. Every new page added, every relationship created, and every pattern promoted strengthens the fleet's decision-making capability. See [[Model: Knowledge Evolution]] for how the wiki continuously improves itself.

**OpenArms — The Personal AI Assistant Layer**

OpenArms provides multi-channel access to the fleet's agent runtime from any device. It routes messages from 20+ messaging channels (Telegram, Discord, Slack, iMessage, and others) to the same underlying agent runtime via OpenClaw. From the human's perspective, the channel is irrelevant — the same agent intelligence responds regardless of whether the message arrives via phone, desktop client, or web interface.

OpenArms completes the human interface layer. The fleet operates autonomously on shared infrastructure, but the human can inspect, direct, and query it from any messaging channel without dedicated tooling. See `wiki/domains/devops/openarms.md` for channel routing architecture.

### The Integration Map

| From | To | Mechanism | What Transfers |
|------|----|-----------|----------------|
| Wiki | OpenFleet | `kb_sync.py` reads `## Relationships` | Knowledge graph edges → LightRAG navigation |
| devops-control-plane | OpenFleet | `doctor.py` rule import | 24 governance rules from 16 post-mortems |
| AICP | Fleet agents | Skills export | Inference profiles + tooling configurations |
| OpenFleet | AICP | Task dispatch | Tasks routed by complexity score to LocalAI vs Claude |
| OpenArms | Fleet via OpenClaw | WebSocket | User messages from 20+ channels → agent runtime |
| Wiki | AICP | File export | docs/kb/ via export profile for agent knowledge base |

### OpenClaw — The Connection Layer

OpenClaw is the WebSocket gateway that all Claude Code fleet agents connect through. It is the single connection point between Mission Control (the human-facing management interface) and individual agents. Every agent message, task assignment, and status update flows through OpenClaw.

The gateway-centric architecture (see [[Gateway-Centric Routing]]) means fleet governance is enforced at one point: OpenClaw can implement rate limiting, authentication, anomaly detection, and budget enforcement for all agents without modifying any individual agent. This is the fleet equivalent of a load balancer — routing is centralized, agents are stateless clients.

Mission Control, the human-facing UI, communicates with agents exclusively through OpenClaw. The human has a single pane of glass; the fleet has a single integration surface.

### The Knowledge Feedback Loop

The ecosystem has a self-reinforcing knowledge loop that is the source of compounding value over time:

1. **Operations generate events**: agents execute tasks, encounter failures, hit edge cases
2. **Events generate lessons**: post-mortems extract principles from failures; successful patterns get documented
3. **Lessons enter the wiki**: structured pages with relationships, scored for evolution
4. **Wiki feeds the fleet**: `kb_sync.py` parses relationships into LightRAG; evolved pages become high-value graph nodes
5. **Fleet makes better decisions**: navigator intelligence improves as the graph densifies

This loop is why the wiki's health directly affects fleet quality. A sparse, poorly linked wiki produces a sparse knowledge graph. A dense, well-linked wiki with mature patterns and decisions produces a rich graph that enables contextually grounded agent decisions.

### The Deterministic Shell + LLM Core Pattern

The [[Deterministic Shell, LLM Core]] pattern is the architectural principle that makes the fleet reliable at scale. It appears throughout the ecosystem:

**OpenFleet orchestrator**: pure Python, zero LLM calls. Handles state diffing, budget gating, heartbeat scheduling, task dispatch, security scanning, anomaly detection — all deterministic. LLM calls only happen inside individual agent executions, where reasoning is genuinely needed.

**AICP complexity scorer**: deterministic scoring assigns a 0-10 complexity value. Routing to LocalAI vs Claude is a threshold comparison — no LLM inference in the routing decision itself.

**Wiki evolution scorer**: six deterministic signals produce rankings with no LLM inference. The LLM is invoked only for generation after a candidate is deterministically selected.

**doctor.py governance rules**: 24 static rules enforced deterministically on every agent action. No LLM decides whether a rule applies — the check is a pure conditional.

The pattern's value: deterministic shells are predictable, auditable, cheap, and immune to hallucination. LLM cores are contextually intelligent, expensive, and probabilistic. Separating the two gives the system the best properties of both — reliability and intelligence — without the failure modes of either. A fully LLM-driven orchestrator hallucinates state. A fully deterministic orchestrator cannot handle novel situations. The boundary between them is the design's most important seam.

### The File-Based Coupling Model

Projects communicate via files and shared protocols rather than tight API contracts. Specific mechanisms:

- **Wiki → OpenFleet**: `kb_sync.py` reads `wiki/` directory for `## Relationships` sections; no API, no service dependency
- **devops-control-plane → OpenFleet**: rules are static files that `doctor.py` imports at runtime; updated by committing to the rules file
- **Wiki → AICP**: `tools/export.py` with the `aicp` profile writes to `docs/kb/` which AICP reads at its own cadence
- **OpenFleet → OpenClaw**: WebSocket protocol; agents connect as clients, OpenClaw is a lightweight gateway, not a service mesh

This decoupling means any component can be taken offline, rewritten, or replaced without cascading failures. The interfaces are durable even when implementations change.

### WSL2 as the Deployment Reality

All five projects run on a single machine: WSL2 on Windows. This is not a production constraint — it is an intentional architecture choice for a single-engineer ecosystem. The practical implications:

- **Filesystem constraints**: WSL2's inotify support means tools like `tools/watcher.py` can watch for file changes reliably. The wiki watcher daemon triggers the full post-chain automatically on any wiki edit, maintaining index freshness without manual pipeline runs.
- **Sync boundary**: `tools/sync.py` maintains the wiki in both the WSL2 filesystem (for tooling) and the Windows filesystem (for Obsidian's graph view). The two-way sync is automated but requires coordination — changes from Obsidian on Windows and from Claude Code in WSL2 must be reconciled.
- **Single-machine cost model**: running five projects on one machine (local inference via LocalAI, fleet agents via WebSocket, wiki via file operations) makes the economics feasible for a single engineer. Cloud costs would make the same ecosystem architecture prohibitive at this scope.
- **Service management**: `python -m tools.setup --services` deploys systemd user services for the watcher and sync daemons. The services are defined in reproducible tooling (not manual systemd configs), consistent with the IaC pattern documented in [[Model: Design.md and IaC]].

This is the context in which "ecosystem architecture" means something operational, not theoretical — the five projects actively run and interact on this machine, and the integration patterns are load-tested daily.

## Open Questions

- As the wiki grows beyond 200 pages, will `kb_sync.py`'s full-graph parse remain performant, or does the LightRAG integration need to shift to incremental updates?
- OpenArms currently routes to a single agent runtime. If OpenFleet scales to specialized agent pools per domain, how does OpenArms routing need to evolve?
- The current integration between AICP and OpenFleet is informal (skills export + task dispatch patterns). Is there a case for a more explicit integration contract as both systems mature?

## Relationships

- BUILDS ON: [[Four-Project Ecosystem]]
- BUILDS ON: [[OpenFleet]]
- BUILDS ON: [[AICP]]
- BUILDS ON: [[Gateway-Centric Routing]]
- BUILDS ON: [[Deterministic Shell, LLM Core]]
- RELATES TO: [[Model: MCP and CLI Integration]]
- RELATES TO: [[Model: Knowledge Evolution]]
- RELATES TO: [[Model: Skills, Commands, and Hooks]]
- FEEDS INTO: [[Model: Claude Code]]
- FEEDS INTO: [[Model: LLM Wiki]]

## Backlinks

[[Four-Project Ecosystem]]
[[OpenFleet]]
[[AICP]]
[[Gateway-Centric Routing]]
[[[[Deterministic Shell]]
[[LLM Core]]]]
[[Model: MCP and CLI Integration]]
[[Model: Knowledge Evolution]]
[[[[Model: Skills]]
[[Commands]]
[[and Hooks]]]]
[[Model: Claude Code]]
[[Model: LLM Wiki]]
[[Model: Methodology]]
