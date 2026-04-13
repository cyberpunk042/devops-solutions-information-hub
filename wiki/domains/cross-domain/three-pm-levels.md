---
title: "Three PM Levels — Wiki to Fleet to Full Tool"
type: concept
domain: cross-domain
status: synthesized
confidence: high
maturity: seed
created: 2026-04-12
updated: 2026-04-12
sources:
  - id: operator-directive
    type: directive
    file: raw/notes/2026-04-12-readiness-progress-pm-levels-directive.md
    description: "Operator: three levels of PM that interconnect with different degrees of capabilities"
  - id: openfleet-orchestrator
    type: observation
    file: raw/articles/openfleet-methodology-scan.md
    description: "OpenFleet orchestrator as L2 implementation — Mission Control, dispatch, immune system"
  - id: openarms-harness
    type: observation
    file: raw/articles/openarms-agent-behavior-failures.md
    description: "OpenArms harness as L1→L2 transition — standalone to enforced methodology"
tags: [project-management, pm-levels, wiki-llm, fleet, plane, harness, sdlc, scalability, traceability]
---

# Three PM Levels — Wiki to Fleet to Full Tool

## Summary

Project management for AI-agent-driven work operates at three levels, each wrapping the previous: L1 (Wiki LLM — in-repo backlog with CLAUDE.md directives), L2 (Fleet System — orchestrator with immune system, MCP enforcement, and real-time dispatch), and L3 (Full PM Tool — DSPD/Plane with SCRUM/agile, multi-project visibility, and organizational traceability). Each level adds enforcement, observability, and scalability capabilities. Projects start at L1 and graduate upward as their needs grow. The levels are not alternatives — they STACK. L2 reads L1's data. L3 syncs with L2's state.

## Key Insights

1. **Each level wraps the previous — they don't replace.** L2 (fleet) reads the Wiki LLM's methodology.yaml and backlog. L3 (Plane) syncs with the fleet's task state. Remove L1 and both L2 and L3 lose their data source. The foundation is always the wiki.

2. **Enforcement strength increases per level.** L1 = advisory (CLAUDE.md rules, agent may ignore, ~25% compliance). L2 = structural (hooks block actions, harness owns git, ~100% stage compliance). L3 = organizational (sprint commitments, stakeholder gates, full audit trail).

3. **The harness version determines the PM level ceiling.**

> [!abstract] Execution Modes and Their PM Levels
>
> | Mode | What It Is | PM Level | SDLC Integration |
> |------|-----------|---------|-------------------|
> | **Solo mode** | Human talks to Claude in a project folder. Normal conversation. No loop, no dispatch. Operator IS the enforcement. | L1 only | Advisory — CLAUDE.md directives, wiki methodology referenced |
> | **Harness v1** | Program wraps the agent (`openarms agent run`). Spawns sessions, dispatches tasks, basic loop. | L1→L2 | Methodology referenced, basic task dispatch |
> | **Harness v2** | Enhanced harness — hooks, commands, stage validation, model-aware pipeline. Enforcement baked in. | L2 | Methodology ENFORCED. Hooks block wrong actions. Commands own git. |
> | **Harness v3** | Future — full SDLC integration. Plane/DSPD sync, sprint planning, traceability. | L2→L3 | Full SDLC. Sprint planning. Traceability. |
> | **Full system** | Provisioned fleet. Orchestrator, immune system, multiple agents, Mission Control. NOT a harness version — different layer. | L3 | Multi-agent coordination. Contribution gating. Tier progression. |
>
> **Solo mode vs harness vs system are DIFFERENT THINGS:**
> - A **harness** wraps ONE agent in a controlled loop (v1 basic → v2 enforced → v3 full SDLC)
> - A **system** orchestrates MANY agents with immune system, dispatch, and coordination
> - **Solo mode** has NEITHER — just a human and Claude in conversation
>
> The research wiki operates in **solo mode**. OpenArms uses a **harness (v2)**. OpenFleet is a **full system**.

4. **99→100 is always human-only, at every level.** L1: operator reviews manually. L2: fleet-ops agent reviews + PO confirms. L3: multi-stakeholder review with sign-off. The mechanism differs but the principle is invariant: no automated system declares work complete.

5. **Traceability compounds across levels.** L1: git commits + frontmatter. L2: git + frontmatter + orchestrator logs + immune system reports + contribution trails. L3: all of L2 + sprint history + burndown + velocity + stakeholder decisions + time records.

## Deep Analysis

### Level 1: Wiki LLM (In-Repo)

> [!info] L1 Architecture
>
> | Component | Purpose | Enforcement |
> |-----------|---------|-------------|
> | `CLAUDE.md` | Agent behavioral configuration | Advisory — agent processes probabilistically |
> | `wiki/config/methodology.yaml` | Model definitions, stage gates | Read by skills, not enforced by infrastructure |
> | `wiki/backlog/` | Epic/module/task hierarchy | File-based, agent updates frontmatter |
> | `wiki/config/artifact-types.yaml` | Per-type quality thresholds | Checked by pipeline post, not per-action |
> | Second brain (this wiki) | Knowledge base, standards, lessons | Referenced by agent, not enforced |

**What L1 can do:** Track work in markdown files. Define methodology models. Validate page quality via pipeline post. Provide standards and lessons for agents to read.

**What L1 cannot do:** Prevent the agent from ignoring rules. Block wrong-stage actions. Enforce contribution requirements. Detect behavioral failures in real-time. Gate dispatch on readiness.

**When L1 is enough:** Solo human-supervised agent, simple projects, POC phase, projects where the human IS the enforcement layer.

---

### Level 2: Fleet System (Orchestrated)

> [!info] L2 Architecture (wraps L1)
>
> | Component | Purpose | Enforcement |
> |-----------|---------|-------------|
> | Orchestrator | 6-step deterministic cycle: security → doctor → contributions → approvals → dispatch → health | Structural — pure Python, no LLM in loop |
> | Hooks | Pre/Post ToolUse shell scripts | Structural — blocks actions at tool level |
> | Commands | /stage-complete, /task-done, /concern | Structural — harness validates before committing |
> | Immune system | 3-line defense: prevent → detect → correct | Active — 30s doctor cycle |
> | Contribution gating | Cross-agent inputs required before work | Structural — dispatch blocked without contributions |
> | Tier system | Context depth based on trust | Data-driven — approval rates control tiers |
> | Mission Control | Kanban board, agent lifecycle, real-time state | Observability — full visibility into fleet state |

**What L2 adds over L1:** Real-time enforcement (hooks, commands), behavioral detection (immune system), multi-agent coordination (contributions, dispatch), trust management (tiers), readiness gating (dispatch blocked until 99).

**What L2 cannot do:** Sprint planning across sprints, velocity tracking, multi-project portfolio view, stakeholder communication, time-based reporting, organizational audit trails.

**When to upgrade from L1 to L2:** When agents violate rules despite CLAUDE.md instructions. When autonomous overnight runs produce broken output. When multiple agents need coordination.

---

### Level 3: Full PM Tool (DSPD / Plane)

> [!info] L3 Architecture (wraps L2)
>
> | Component | Purpose | Enforcement |
> |-----------|---------|-------------|
> | Plane (project management) | Full SCRUM/agile: sprints, story points, burndown, velocity | Organizational — commitment tracking |
> | DSPD (devops-control-plane) | Multi-project dashboard, cross-project visibility | Portfolio — all projects, all levels |
> | Sprint planning | Time-boxed delivery commitments | Process — team commits to sprint scope |
> | Stakeholder gates | Multi-person review, sign-off | Organizational — not just PO, full team |
> | Time tracking | Actual vs estimated effort | Metrics — enables velocity and cost analysis |
> | Advanced integrations | CI/CD, notifications, group calls, tool chains | Automation — complete tool chain orchestration |

**What L3 adds over L2:** Multi-project portfolio view, time-based planning (sprints, velocity), organizational audit trails, stakeholder communication surfaces, advanced integrations that complete tool chains.

**When to upgrade from L2 to L3:** When the project has paying customers, SLAs, or compliance requirements. When multiple projects share resources. When stakeholders beyond the PO need visibility. When you need to answer "how long did this take?" not just "is this done?"

---

### How They Interconnect

```
┌─────────────────────────────────────────────────────┐
│  L3: DSPD / Plane                                   │
│  Sprint planning, multi-project, stakeholder gates   │
│  ┌─────────────────────────────────────────────────┐ │
│  │  L2: Fleet System / Harness                     │ │
│  │  Orchestrator, hooks, immune system, dispatch    │ │
│  │  ┌─────────────────────────────────────────────┐ │ │
│  │  │  L1: Wiki LLM                               │ │ │
│  │  │  CLAUDE.md, methodology.yaml, backlog/      │ │ │
│  │  │  The FOUNDATION. Data lives here.           │ │ │
│  │  └─────────────────────────────────────────────┘ │ │
│  │  L2 READS from L1. Enforcement lives here.      │ │
│  └─────────────────────────────────────────────────┘ │
│  L3 SYNCS with L2. Organizational tracking here.     │
└─────────────────────────────────────────────────────┘
```

**Data flow:** L1 → L2 (orchestrator reads wiki backlog) → L3 (Plane syncs with fleet state)
**Enforcement flow:** L3 → L2 (sprint scope constrains dispatch) → L1 (methodology gates constrain stages)
**Escalation flow:** L1 (agent files concern) → L2 (immune system escalates) → L3 (PO/stakeholder decides)

### How This Connects — Navigate From Here

> [!abstract] From PM Levels → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **What enforcement exists at each level?** | L1: [[CLAUDE.md Structural Patterns for Agent Compliance]]. L2: [[Enforcement Hook Patterns]] + [[Harness-Owned Loop — Deterministic Agent Execution]]. L3: + [[Three Lines of Defense — Immune System for Agent Quality]] |
> | **What SDLC chain matches each level?** | [[SDLC Customization Framework — Phases, Scale, and Chain Selection]] — L1=simplified, L2=default, L3=full |
> | **How does the wiki serve all levels?** | L1: agent reads wiki pages. L2: harness queries wiki config. L3: Plane syncs with wiki state. All read from [[Super-Model: Research Wiki as Ecosystem Intelligence Hub]] |
> | **What tools serve each level?** | [[Wiki Gateway Tools — Unified Knowledge Interface]] — same gateway, adapted per PM level |
> | **What harness version maps here?** | v1→L1, v2→L2, v3→L3. See harness version table in this page. |
> | **Goldilocks question** | [[Project Self-Identification Protocol — The Goldilocks Framework]] — PM level is one of 7 identity dimensions |

## Open Questions

> [!question] Can a project use L3 without L2?
> Skip the fleet system and connect Plane directly to the Wiki LLM? This loses real-time enforcement but gains organizational tracking. Useful for human-only teams that don't use AI agents.

> [!question] How does the second brain relate to PM levels?
> The research wiki (this project) is the second brain. L1 projects reference it for methodology and standards. L2 projects consume it via MCP tools. L3 projects may integrate it into sprint planning. Is the second brain a cross-level service or an L1 component?

> [!question] What determines when to upgrade harness versions?
> v1→v2: "when agents violate rules" is clear. v2→v3: "when you need organizational tracking" is vague. Can we define specific triggers (team size, compliance requirements, multi-project threshold)?

## Relationships

- BUILDS ON: [[Backlog Hierarchy Rules]]
- BUILDS ON: [[Readiness vs Progress — Two-Dimensional Work Tracking]]
- RELATES TO: [[SDLC Customization Framework — Phases, Scale, and Chain Selection]]
- RELATES TO: [[Harness-Owned Loop — Deterministic Agent Execution]]
- RELATES TO: [[Infrastructure Enforcement Proves Instructions Fail]]
- RELATES TO: [[Three Lines of Defense — Immune System for Agent Quality]]
- RELATES TO: [[Ecosystem Feedback Loop — Wiki as Source of Truth]]
- FEEDS INTO: [[Methodology Adoption Guide]]
- FEEDS INTO: [[Model: Ecosystem Architecture]]

## Backlinks

[[Backlog Hierarchy Rules]]
[[Readiness vs Progress — Two-Dimensional Work Tracking]]
[[SDLC Customization Framework — Phases, Scale, and Chain Selection]]
[[Harness-Owned Loop — Deterministic Agent Execution]]
[[Infrastructure Enforcement Proves Instructions Fail]]
[[Three Lines of Defense — Immune System for Agent Quality]]
[[Ecosystem Feedback Loop — Wiki as Source of Truth]]
[[Methodology Adoption Guide]]
[[Model: Ecosystem Architecture]]
[[Decision: When to Use Milestone vs Epic vs Module vs Task]]
[[Frontmatter Field Reference — Complete Parameter Documentation]]
[[OpenArms vs OpenFleet Enforcement Architecture]]
[[Principle: Right Process for Right Context — The Goldilocks Imperative]]
[[Project Self-Identification Protocol — The Goldilocks Framework]]
[[SDLC Rules and Structure — Customizable Project Lifecycle]]
[[Synthesis: SDLC Frameworks Research — CMMI, Lean Startup, and Agentic SDLC]]
