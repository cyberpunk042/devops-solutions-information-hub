---
title: Decision — Methodology Stage Extension Decisions
aliases:
  - "Decision — Methodology Stage Extension Decisions"
  - "Decision: Methodology Stage Extension Decisions"
type: decision
domain: cross-domain
layer: 6
status: synthesized
confidence: medium
maturity: growing
reversibility: moderate
derived_from:
  - "Initiation and Planning Artifacts — Standards and Guide"
  - "Deployment, Closure, and Monitoring Artifacts — Standards and Guide"
  - "Artifact Chain: Infrastructure/IaC Domain"
created: 2026-04-12
updated: 2026-04-12
sources: []
tags: [methodology, decision, stages, initiation, deployment, drift, status-report]
---

# Decision — Methodology Stage Extension Decisions
## Summary

Resolves 4 questions about extending the methodology's stage system: whether to add an Initiation stage before Document, a Deploy stage after Test, a formal Status Report template, and how to handle infrastructure drift detection. Decision: fold initiation into Document at epic scale, add Deploy as a domain-specific optional stage for infrastructure, create a lightweight Status Report template, and model drift detection as a periodic monitoring task.

## Decision

> [!success] 4 Decisions
>
> | # | Question | Decision | Rationale |
> |---|---------|----------|-----------|
> | 1 | Initiation stage before Document? | NO — fold initiation into Document stage for epic-scale work. The operator directive IS the initiation artifact. | Adding a stage increases process overhead for all scales. Epic-level Document stage already includes charter-equivalent content (Summary, Goals, Done When). Separating them would split what is naturally one phase of understanding. |
> | 2 | Deploy stage for infrastructure? | YES — as an OPTIONAL domain-specific stage after Test, for Infrastructure domain only. Not added to the universal 5-stage model. | Infrastructure has a materially different deployment step (terraform apply to production) that code projects handle via CI/CD. The Deploy stage includes: production apply, health checks, monitoring setup, runbook verification. Other domains don't need this explicit stage. |
> | 3 | Formal Status Report template? | YES — lightweight template in wiki/config/templates/methodology/status-report.md. Not a new page type. Use note type with note_type: session. | Periodic epic health updates need structure: readiness trend, blockers, decisions needed, next actions. Currently implicit in backlog readiness numbers. A template makes the report consistent without adding a new page type. |
> | 4 | Drift detection in methodology? | Model as periodic monitoring task using bug-fix model. Not a new methodology model. Schedule via cron/manual triggers. | Drift is infrastructure-specific and intermittent. Creating a dedicated methodology model for it adds complexity. Using bug-fix (document: identify drift → implement: fix config → test: verify state matches) handles it within existing models. Periodic scheduling is a tooling concern, not a methodology concern. |

## Alternatives

### Alt 1: Add Initiation as Universal Stage

> [!warning] Rejected: Process overhead for non-epic work
>
> Adding a 6th stage (Initiation → Document → Design → Scaffold → Implement → Test) increases overhead for EVERY task, module, and epic. Most tasks don't need a Project Charter — they inherit scope from their parent epic. Only epic-scale work needs initiation artifacts, and the Document stage already accommodates them (the epic's Summary + Goals + operator directive reference IS the charter).

### Alt 2: Add Deploy as Universal Stage

> [!warning] Rejected: Only infrastructure needs it
>
> For TypeScript projects, deployment is handled by CI/CD (npm publish, Docker push) — it's automated and not a methodology concern. For Python/wiki projects, `pipeline post` + `sync` IS deployment. For knowledge projects, publishing means the page exists and passes validation. Only infrastructure projects have a distinct manual deployment step that needs its own stage with specific artifacts (production apply, health checks, rollback plan).

### Alt 3: Create Drift Detection Model

> [!warning] Rejected: Overcomplicating an intermittent concern
>
> A dedicated "drift-detection" methodology model with its own stages would add a 10th model to the system. Drift occurs intermittently and is functionally identical to bug-fix: something is wrong (drift) → document it (what drifted and why) → fix it (update config or resource) → verify (plan + apply confirms no more drift). The bug-fix model handles this without any new infrastructure.

## Rationale

All 4 decisions follow the "minimal change with documented upgrade path" principle. The methodology already has 9 models and 5 stages — adding more stages or models increases cognitive load for every agent and user. The evidence says: (1) Initiation content is already in epic Document stages — no users have asked for separation. (2) Only infrastructure has a distinct deployment step — code projects deploy via CI/CD. (3) Status reporting is needed but doesn't justify a new page type — the note template with consistent sections is sufficient. (4) Drift is intermittent and matches the bug-fix model's structure exactly. In each case, the simpler approach works TODAY and has an explicit trigger for when it won't.

## Reversibility

Moderate. All decisions are reversible:
- Initiation stage: can be added later if fleet agents need explicit project chartering
- Deploy stage: currently optional for infrastructure only — can be promoted to universal if other domains need it
- Status Report: can be upgraded from note template to full page type if structured reporting becomes critical
- Drift detection: can be promoted to its own model if drift frequency justifies dedicated tooling

## Dependencies

- Decision 2 (Deploy stage) requires updating the Infrastructure domain profile and chain page
- Decision 3 (Status Report) requires creating the template
- Decision 4 (Drift) requires no changes — uses existing bug-fix model

> [!info] SDLC Chain Context
> This decision was calibrated for a 5-stage model used across 4 projects with mixed domains. At different chain levels:
> - **Simplified chain:** Stage extensions are irrelevant — simplified chains use 2-3 stages maximum, so adding Initiation or Deploy is over-engineering. Status Reports are verbal, not templated.
> - **Full chain:** Initiation becomes a formal stage with project charter artifacts. Deploy becomes universal (not infrastructure-only) with automated rollback verification. Status Reports become mandatory per-sprint structured artifacts feeding a PM dashboard.
> See [[sdlc-customization-framework|SDLC Customization Framework]] for chain details.

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **What stage model does this extend?** | [[stage-gate-methodology|Stage-Gate Methodology]] |
> | **What infrastructure domain triggers Deploy?** | [[domain-chain-infrastructure|Artifact Chain — Infrastructure-IaC Domain]] |
> | **Related decision: artifact system** | [[artifact-system-design-decisions|Decision — Artifact System Design Decisions]] |
> | **What evolution protocol governs changes?** | [[methodology-evolution-protocol|Methodology Evolution Protocol]] |
> | **Where does this fit?** | [[methodology-system-map|Methodology System Map]] |

## Relationships

- DERIVED FROM: [[initiation-and-planning-artifacts|Initiation and Planning Artifacts — Standards and Guide]]
- DERIVED FROM: [[deployment-closure-monitoring-artifacts|Deployment, Closure, and Monitoring Artifacts — Standards and Guide]]
- DERIVED FROM: [[domain-chain-infrastructure|Artifact Chain — Infrastructure-IaC Domain]]
- RELATES TO: [[model-methodology|Model — Methodology]]
- RELATES TO: [[stage-gate-methodology|Stage-Gate Methodology]]
- FEEDS INTO: [[methodology-evolution-protocol|Methodology Evolution Protocol]]

## Backlinks

[[initiation-and-planning-artifacts|Initiation and Planning Artifacts — Standards and Guide]]
[[deployment-closure-monitoring-artifacts|Deployment, Closure, and Monitoring Artifacts — Standards and Guide]]
[[domain-chain-infrastructure|Artifact Chain — Infrastructure-IaC Domain]]
[[model-methodology|Model — Methodology]]
[[stage-gate-methodology|Stage-Gate Methodology]]
[[methodology-evolution-protocol|Methodology Evolution Protocol]]
