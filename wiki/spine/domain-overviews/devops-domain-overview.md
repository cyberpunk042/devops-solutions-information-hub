---
title: "Devops — Domain Overview"
type: domain-overview
domain: devops
layer: spine
status: synthesized
confidence: high
maturity: growing
created: 2026-04-08
updated: 2026-04-10
sources: []
tags: [domain-overview, devops]
---

# Devops — Domain Overview

## Summary

The devops domain covers stage-gate methodology, ecosystem topology, backlog management, task governance, infrastructure patterns, and the control plane vision — the operational backbone of the four-project ecosystem. With 9 concept pages, the domain has grown significantly from its original single page to become a well-developed methodology hub. Coverage now spans Stage-Gate Methodology (the 5-stage sequential system), Four-Project Ecosystem (topology), Immune System Rules (24 post-mortem-derived governance rules), Infrastructure as Code Patterns, WSL2 Development Patterns, Backlog Hierarchy Rules, Task Type Artifact Matrix, Execution Modes and End Conditions, and devops-control-plane. The domain defines how work proceeds across all projects — methodology, not just infrastructure.

> [!info] Domain at a glance
>
> | Metric | Value |
> |--------|-------|
> | Concept pages | 9 |
> | Related model pages | [[Model: Methodology]], [[Model: Ecosystem Architecture]], [[Model: SFIF Architecture]] |
> | Decision pages | [[Decision: Stage-Gate Operational Decisions]], [[Decision: Task Type Edge Cases]], [[Decision: Execution Mode Edge Cases]] |
> | Related lessons | 5+ (Never Skip Stages Even When Told to Continue, Infrastructure Must Be Reproducible Not Manual, Methodology Is a Framework Not a Fixed Pipeline, etc.) |

## State of Knowledge

> [!tip] From Sparse to Methodology Hub
> The devops domain has evolved from a single concept page to a 9-page methodology hub. It now defines how work proceeds across all projects — stage gates, task governance, ecosystem topology, and infrastructure patterns.

**Authoritative coverage:**
- Stage-Gate Methodology — the 5-stage sequential system (Document → Design → Scaffold → Implement → Test) governing all work. Multiple sources, heavily cross-referenced.
- Immune System Rules — 24 governance rules from 16 post-mortems. The operational guardrail system, now distilled with callout styling.
- Four-Project Ecosystem — the personal devops infrastructure topology across openfleet, AICP, DSPD, devops-control-plane.
- devops-control-plane — sourced from the live README. Architecture (layered: interfaces → core → policy → adapters → infrastructure), 20 stack definitions, dual vault system, audit ledger.

**Good coverage:**
- Task Type Artifact Matrix — 7 task types (epic, module, task, bug, hotfix, spike, chore) with required artifacts per type.
- Backlog Hierarchy Rules — EPIC → MODULE → TASK three-level structure, status propagation, upward aggregation.
- Execution Modes and End Conditions — operational envelope for autonomous agent execution.
- Infrastructure as Code Patterns — IaC beyond Terraform: config-as-code patterns in the ecosystem.
- WSL2 Development Patterns — Linux dev ecosystem alongside Windows tools, inotify limits, service management.

**Thin coverage:**
- CI/CD pipelines — the ecosystem projects use GitHub Actions but no wiki page covers their pipeline designs, testing strategies, or deployment workflows.
- Docker Compose and Kubernetes — both used (OpenFleet services, Plane self-hosting, AICP LocalAI) but no devops-domain synthesis of the container orchestration approach.
- Monitoring and observability — OpenFleet's 9-service architecture requires monitoring but no coverage exists.

## Maturity Map

| Maturity | Pages |
|----------|-------|
| **growing** (all 9) | Stage-Gate Methodology, Four-Project Ecosystem, Task Type Artifact Matrix, Backlog Hierarchy Rules, Execution Modes and End Conditions, Immune System Rules, devops-control-plane, Infrastructure as Code Patterns, WSL2 Development Patterns |

All pages assigned maturity. All styled with callout vocabulary. All have standard sections.

## Gaps

- **CI/CD architecture**: GitHub Actions pipelines across the four projects — what they test, how they deploy, what quality gates they enforce — are completely undocumented in the wiki.
- **Service dependency map**: The production service topology (PostgreSQL → Mission Control, Redis → RQ queue, LocalAI → fleet agents, LightRAG → navigator) is described in OpenFleet but not consolidated as a devops architectural view.
- **Secrets management**: The devops-control-plane vault (AES-256-GCM) is described but its role as a potential centralized credential store for all ecosystem projects hasn't been evaluated.
- **Container orchestration synthesis**: Docker Compose and Kubernetes are both used across projects but no dedicated page synthesizes the container orchestration approach.
- **Monitoring and observability**: No coverage of how the ecosystem monitors services, tracks health, or alerts on anomalies.

## Priorities

1. **CI/CD architecture** — Survey and document the GitHub Actions workflows across the four projects
2. **Service dependency map** — Consolidate the production service topology across the ecosystem
3. **Container orchestration synthesis** — Document the Docker Compose / Kubernetes approach across projects
4. **Monitoring and observability** — Design the observability strategy for the multi-service ecosystem
5. **Secrets management evaluation** — Assess devops-control-plane vault as centralized credential store

## Key Pages

1. **[Stage-Gate Methodology](../../domains/devops/stage-gate-methodology.md)** — The 5-stage sequential system (Document → Design → Scaffold → Implement → Test) governing all work across the ecosystem.
2. **[Four-Project Ecosystem](../../domains/devops/four-project-ecosystem.md)** — The personal devops infrastructure topology: openfleet, AICP, DSPD, devops-control-plane.
3. **[Immune System Rules](../../domains/devops/immune-system-rules.md)** — 24 operational governance rules derived from 16 post-mortems. The guardrail system adopted by OpenFleet's doctor.py.
4. **[Task Type Artifact Matrix](../../domains/devops/task-type-artifact-matrix.md)** — The 7 task types and their required artifacts: epic, module, task, bug, hotfix, spike, chore.
5. **[Infrastructure as Code Patterns](../../domains/devops/infrastructure-as-code-patterns.md)** — IaC beyond Terraform: config-as-code, scripts/, setup.sh patterns across the ecosystem.
6. **[devops-control-plane](../../domains/devops/devops-control-plane.md)** — Unified solution management platform: 20 stack auto-detection, encrypted vaults, audit ledger.

## FAQ

### Q: What is the Stage-Gate Methodology and why is it mandatory?
Stage-Gate is the 5-stage sequential system — Document → Design → Scaffold → Implement → Test — that governs all work across the ecosystem. Skipping stages is a violation. The methodology ensures that understanding precedes design, design precedes implementation, and verification follows all work. See [[Stage-Gate Methodology]].

### Q: What are the 24 Immune System Rules and where should I apply them?
The 24 rules originated from 16 real post-mortems across projects. They cover failure modes like runaway loops, permission drift, stale state reads, and cost spikes. They are implemented in OpenFleet's doctor.py and are transferable to any agent harness as a checklist. See [[Immune System Rules]].

### Q: How do the four ecosystem projects relate to each other?
openfleet (agent fleet), AICP (AI Control Platform), DSPD (the research wiki), and devops-control-plane (infrastructure management) form a single personal devops infrastructure. The wiki documents all four and acts as the shared knowledge backbone. See [[Four-Project Ecosystem]].

### Q: What WSL2-specific devops constraints should I know about?
WSL2 affects service startup (no systemd by default), networking (bridged vs NAT), inotify watch limits (relevant for the wiki watcher daemon), and daemon lifecycle management. Standard Linux devops documentation often does not account for these constraints. See [[WSL2 Development Patterns]].

## Relationships

- ENABLES: AI Agents — Domain Overview
- ENABLES: Tools And Platforms — Domain Overview
- ENABLES: Automation — Domain Overview
- RELATES TO: Knowledge Systems — Domain Overview
- UNDERPINS: AI Models — Domain Overview

## Backlinks

[[AI Agents — Domain Overview]]
[[Tools And Platforms — Domain Overview]]
[[Automation — Domain Overview]]
[[Knowledge Systems — Domain Overview]]
[[AI Models — Domain Overview]]
[[Cross-Domain — Domain Overview]]
