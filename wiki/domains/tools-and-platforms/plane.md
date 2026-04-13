---
title: Plane
aliases:
  - "Plane"
type: concept
layer: 2
maturity: growing
domain: tools-and-platforms
status: synthesized
confidence: high
created: 2026-04-08
updated: 2026-04-10
sources:
  - id: src-plane-docs
    type: documentation
    url: https://plane.so
    title: Plane — Open-Source Project Management
    ingested: 2026-04-08
  - id: src-dspd-local
    type: documentation
    file: ../devops-solution-product-development/CLAUDE.md
    title: DSPD — Plane Fleet Integration
    ingested: 2026-04-08
tags: [plane, project-management, sprints, kanban, rest-api, webhooks, self-hosted, docker, fleet-integration, pm-agent]
---

# Plane

## Summary

Plane is the #1 open-source project management platform (AGPL-3.0, 47.4k+ stars, 1M+ Docker pulls) positioned as an alternative to Jira, Linear, and ClickUp. It provides work items, cycles (sprints), modules (epics), 5 view layouts (Kanban, List, Gantt, Calendar, Spreadsheet), pages/wiki, intake/triage, analytics dashboards, and AI capabilities (semantic search, duplicate detection). Self-hosted via Docker Compose (12 services) or Kubernetes with Helm charts. In the ecosystem, Plane serves as the PM surface for the OpenClaw Fleet via DSPD (devops-solution-product-development), where the PM agent bridges human planning in Plane with agent execution in Mission Control. 4 projects tracked: AICP, Fleet, DSPD, NNRT.

## Key Insights

- **Full REST API**: Base URL `/api/v1/workspaces/{slug}/`, X-API-Key auth, 60 req/min rate limit, cursor-based pagination. Full CRUD on projects, work items, cycles, modules, pages, states, labels, comments, attachments, estimates, time tracking, epics.

- **Webhook system**: Events for project, issue, cycle, module, comment. Triggers HTTP POST on create/update/delete. DSPD uses HMAC-SHA256 signed webhooks for fleet integration.

- **Three-surface model in DSPD**: Plane (planning: sprints, epics, analytics, wiki) → OCMC (execution: task dispatch, heartbeat, board memory) → GitHub (code: PRs, CI, releases). PM agent bridges the first two.

> [!warning] PM agent as sole writer
> Non-negotiable architecture rule — the PM agent is the only entity that writes to Plane. Other fleet agents route through PM. This prevents race conditions and maintains audit trail coherence.

- **Bidirectional sync**: Plane → OCMC (PM reads Plane, dispatches to MC), OCMC → Plane (PM detects completion, updates Plane + adds PR link). plane_sync.py handles the logic, plane_client.py is the sole API caller.

- **Self-hosted with operational independence**: Separate Docker Compose from OCMC, separate PostgreSQL instance (plane-db on port 5433), own nginx proxy on port 8080. No shared infrastructure with Mission Control.

- **5 Fibonacci estimate scale**: 1/2/3/5/8/13 story points. Labels: `agent:<name>`, `project:<name>`, `blocked`, `spec-required`. Custom states per project (backlog → todo → dispatched → in-review → done).

- **AI capabilities**: Natural language chat, duplicate detection, semantic search across items/pages/projects. Requires OpenSearch 2.19+ and LLM provider API key.

- **Community vs Commercial**: Free tier has unlimited projects/items/cycles/users. Commercial ($7/seat/month) adds SSO, RBAC, audit logs, workflows, epics/initiatives, GitHub/GitLab/Slack integrations.

## Deep Analysis

### Fleet Integration Architecture (DSPD)

The data flow in 5 steps:
1. **PLAN**: Humans create work items in Plane (sprints, epics, stories)
2. **DISPATCH**: PM agent reads Plane via MCP tools, creates OCMC tasks
3. **EXECUTE**: Fleet agents work in OCMC
4. **CLOSE**: PM detects OCMC completion, updates Plane + adds PR link
5. **REVIEW**: Humans see burn-down in Plane, merge PRs

PM agent MCP tools: `plane_list_projects`, `plane_list_cycles`, `plane_list_issues`, `plane_create_issue`, `plane_update_issue`, `plane_add_to_cycle`, `plane_create_comment`.

DSPD development phases: Phase 0 (architecture docs) ✅, Phase 1 (Plane deployed) IaC built, Phase 2 (fleet CLI) code done, Phase 3 (MCP + webhooks) code done, Phase 4 (analytics) not started.

### Why Plane Over Alternatives

For the ecosystem, Plane's advantages:
- Self-hosted (data sovereignty, no SaaS dependency)
- Open-source (customizable, forkable)
- REST API (programmatic access for agents)
- Webhooks (real-time event integration)
- Docker Compose deployment (consistent with OCMC, LightRAG, LocalAI)
- Free unlimited tier (cost control for multi-project fleet)

## Open Questions

- What is the performance profile under heavy API usage from automated fleet sync (60 req/min limit)? (Requires: empirical load testing of the Plane REST API at the DSPD sync frequency; the plane_client.py is the sole API caller but its call rate under active sprint conditions is not documented in existing wiki pages)

### Answered Open Questions

**Q: Can Plane's AI capabilities (semantic search) be integrated with the research wiki for cross-system queries?**

Cross-referencing `Four-Project Ecosystem` and `OpenFleet`: Plane's AI capabilities (semantic search, duplicate detection) require OpenSearch 2.19+ and an LLM provider API key. The research wiki runs its own knowledge graph via LightRAG (port 9621) and exposes 15 MCP tools via its own MCP server. These are two separate search systems. The `Four-Project Ecosystem` page documents the integration architecture: "the wiki's knowledge graph (via LightRAG and kb_sync.py) feeds back into OpenFleet's navigator intelligence" — but Plane is positioned as the PM surface, not the knowledge surface. The `OpenFleet` page documents that `kb_sync.py` parses wiki Relationships into the LightRAG graph (1,545 entities, 2,295 relationships from 219 KB entries) and that the LightRAG graph informs agent decision-making. Plane's semantic search operates over work items, pages, and projects within Plane — not over the wiki knowledge graph. Cross-system queries (e.g., "find all wiki pages related to the current sprint's work items") would require a bridge between Plane's API and the wiki MCP server, not an integration of Plane's AI capabilities into the wiki. The wiki MCP server's `wiki_search` tool is the correct entry point for knowledge queries. The practical answer: Plane's semantic search and the research wiki's LightRAG graph serve different query surfaces and are not directly integrable without a custom bridge agent — which could be implemented as a PM agent skill using both plane_list_issues and wiki_search MCP tools in sequence.

**Q: Can Plane's pages/wiki feature replace or complement the research wiki for operational documentation?**

Cross-referencing `Four-Project Ecosystem` and `OpenFleet`: the two systems have distinct purposes that make replacement inappropriate but complementarity natural. The `Four-Project Ecosystem` page defines the research wiki's role as "knowledge synthesis, second brain, central intelligence spine" with LightRAG export feeding agent navigators — a knowledge graph function. Plane's pages/wiki is sprint-scoped operational documentation (spec pages, decision logs, meeting notes) tied to work items and cycles. The `Four-Project Ecosystem` page documents the three-surface model: "Plane (planning: sprints, epics, analytics, wiki) → OCMC (execution) → GitHub (code)." Plane's wiki is explicitly one of three surfaces in a PM workflow, not a knowledge synthesis system. The `OpenFleet` page confirms the separation: `docs/knowledge-map/kb/` is the fleet's operational KB (219+ entries), while Plane holds project-management documentation. Replacing the research wiki with Plane's pages would lose: typed relationship graph (BUILDS ON, ENABLES, etc.), LightRAG integration, multi-domain synthesis, MCP tool exposure, and the evolution pipeline. The complementary use case: Plane's pages are appropriate for sprint-specific operational docs (architecture decision records tied to a work item, spec pages for features in-flight); the research wiki is appropriate for permanent synthesized knowledge that outlives any sprint.

**Q: How does Plane handle sprint-level analytics when tasks are dispatched to agents (velocity tracking per agent)?**

Cross-referencing `OpenFleet` and the DSPD fleet integration documented in this page: Plane tracks velocity at the work item level via story points (1/2/3/5/8/13 Fibonacci scale) and burns down against cycles (sprints). The `OpenFleet` page documents the bidirectional sync: "PM agent reads Plane via MCP tools, creates OCMC tasks" (dispatch) and "PM detects OCMC completion, updates Plane + adds PR link" (close). The labels system (`agent:<name>`, `project:<name>`) enables per-agent work item tagging, meaning Plane can show analytics filtered by `agent:software-engineer` or `agent:qa-engineer` by querying the labels dimension. The `OpenFleet` page documents 10 specialized agents each with defined roles — each agent's dispatched work is labeled with its identifier. Plane's analytics dashboards can therefore show per-agent velocity (story points completed per sprint per agent label) and burn-down, provided the PM agent consistently applies `agent:<name>` labels when creating or updating work items. The DSPD integration's `plane_sync.py` is the component responsible for ensuring this labeling consistency. The one gap: Plane's native analytics treat work items equally regardless of whether they were executed by a human or an agent — the "agent as contributor" model requires the label convention to distinguish agent-executed from human-executed work in the analytics view.

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **What principle applies?** | [[right-process-for-right-context-the-goldilocks-imperative|Principle — Right Process for Right Context — The Goldilocks Imperative]] |
> | **What is my identity?** | [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]] |
> | **System map** | [[methodology-system-map|Methodology System Map]] |

## Relationships

- USED BY: [[openfleet|OpenFleet]]
- RELATES TO: [[aicp|AICP]]
- RELATES TO: [[openclaw|OpenClaw]]
- RELATES TO: [[devops-control-plane]]
- ENABLES: [[claude-code-scheduling|Claude Code Scheduling]]

## Backlinks

[[openfleet|OpenFleet]]
[[aicp|AICP]]
[[openclaw|OpenClaw]]
[[devops-control-plane|devops-control-plane]]
[[claude-code-scheduling|Claude Code Scheduling]]
