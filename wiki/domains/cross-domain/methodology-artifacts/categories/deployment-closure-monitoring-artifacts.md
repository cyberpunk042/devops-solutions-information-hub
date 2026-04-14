---
title: Deployment, Closure, and Monitoring Artifacts — Standards and Guide
aliases:
  - "Deployment, Closure, and Monitoring Artifacts — Standards and Guide"
type: concept
domain: cross-domain
status: synthesized
confidence: high
maturity: growing
created: 2026-04-12
updated: 2026-04-13
sources:
  - id: taxonomy
    type: wiki
    file: wiki/domains/cross-domain/methodology-artifact-taxonomy.md
  - id: sdlcforms
    type: article
    url: https://www.sdlcforms.com/UnderstandingSDLC.html
tags: [methodology, deployment, closure, monitoring, artifacts, operations, lessons-learned, standards]
---

# Deployment, Closure, and Monitoring Artifacts — Standards and Guide

> [!tip] AI Quick Start — AFTER Implementation Is Done
>
> 1. **Need deployment docs?** Use the operations-plan template — sequential steps with Action/Expected/Validation/Rollback
> 2. **Completing an epic?** Write a Lessons Learned page (type: lesson) — what worked, what didn't, what to do differently
> 3. **Completing a task?** Write a completion log in wiki/log/ — stages done, artifacts produced, concerns raised
> 4. **Closure artifacts feed the knowledge evolution pipeline** — lessons → patterns → decisions
> 5. **Compliance reports are the biggest gap** — no automated methodology adherence checking exists yet

## Summary

Guide to the artifacts produced AFTER implementation — deployment (how to ship), closure (what was learned), and monitoring (ongoing tracking). These are the most commonly SKIPPED artifact categories in agile and AI agent workflows. Teams build features, verify they work, and move on — without writing the operations guide, capturing lessons, or tracking compliance. This gap is why production incidents happen, knowledge is lost, and methodology violations go undetected.

## Key Insights

1. **Deployment artifacts are the operations-plan type we created.** The operations-plan template (sequential steps with Action/Expected/Validation/Rollback) maps directly to Installation Guides, Production Implementation Plans, and Runbooks. These are the "dumb agent" documents — any operator can follow them mechanically.

2. **Closure artifacts feed the knowledge evolution pipeline.** Lessons Learned → wiki lesson pages. Post-Project Reviews → wiki decision/pattern pages. Knowledge Transfer → wiki domain overviews. Completion Logs → wiki notes. The closure phase IS the knowledge-evolution methodology model running on completed work.

3. **Monitoring artifacts are the missing category.** We have zero monitoring artifact types. No Change Management Log, no Risk Register, no Compliance Report, no Status Report format. The backlog system tracks task status but doesn't track methodology COMPLIANCE (did the agent follow the right model? did it produce required artifacts? did it skip stages?).

4. **These three categories complete the lifecycle.** Without deployment artifacts: "it works on my machine." Without closure artifacts: "we learned nothing." Without monitoring artifacts: "we have no idea if the methodology is working."

## Deep Analysis

### Deployment Artifacts (7 types)

> [!abstract] How to SHIP and OPERATE — produced after test stage passes
>
> | Type | Purpose | Audience | Our Equivalent |
> |------|---------|----------|---------------|
> | **Installation Guide** | Step-by-step installation for target environment | Operators | operations-plan template |
> | **User Guide** | How end users use the system | End users | wiki concept/reference pages |
> | **Admin Guide** | System administration, config, maintenance | Admins | wiki reference pages |
> | **Operations Guide** | Day-to-day operational procedures, monitoring | Operators | wiki reference + operations-plan |
> | **Production Implementation Plan** | Deployment steps with rollback | Deploy team | operations-plan template |
> | **Runbook** | Step-by-step for common operational tasks | On-call engineers | operations-plan template |
> | **Release Notes** | What changed, new, fixed, known issues | All users | wiki note (completion type) |
>
> **Key insight:** Three of these (Installation Guide, Production Plan, Runbook) are all operations-plan type documents. The operations-plan template we created is the right structure for all three — sequential steps with Action/Expected/Validation/Rollback.

#### When Deployment Artifacts Are Required

| Scale | Required | Optional |
|-------|----------|----------|
| **Project/Epic** | Operations Guide, Release Notes | User Guide, Admin Guide (if user-facing) |
| **Module** | — (inherits from epic) | Runbook for module-specific operations |
| **Task** | — | — |
| **Infrastructure changes** | ALWAYS: Runbook + Rollback Plan | Installation Guide if new system |

### SDLC Profile Level — What Applies Where

> [!abstract] Not all chains require all artifacts
>
> | Chain Level | What's Required | What's Optional | What's Skipped |
> |-------------|----------------|-----------------|----------------|
> | **Simplified** (POC, 2-3 stages) | Git commit + informal notes | — | Operations guide, runbook, lessons learned, compliance report |
> | **Default** (MVP-Prod, 5 stages) | Completion log + session summary | Lessons learned (epic-level), release notes | Formal operations guide, compliance report, retirement plan |
> | **Full** (Production fleet, all stages) | Operations guide + runbook + lessons learned + monitoring config | Compliance report, knowledge transfer report | — |
>
> See [[sdlc-customization-framework|SDLC Customization Framework — Phases, Scale, and Profile Selection]] for profile details.

### Closure Artifacts (5 types)

> [!abstract] What was LEARNED — produced when work completes
>
> | Type | Purpose | When | Our Equivalent |
> |------|---------|------|---------------|
> | **Lessons Learned** | What worked, what didn't, what to do differently | Epic/project completion | wiki lesson pages (type: lesson) |
> | **Post-Project Review** | Assessment against original objectives | Project completion | wiki decision pages (what we'd decide differently) |
> | **Knowledge Transfer Report** | What the next team/person needs to know | Handoffs, team changes | wiki domain overviews + learning paths |
> | **Completion Log** | What was done, what passed, concerns raised | Task/stage completion | wiki notes (type: note, note_type: completion) |
> | **Retirement Plan** | How to decommission, migrate, archive | End of life | operations-plan for decommission |

#### The Knowledge Evolution Connection

> [!tip] Closure artifacts feed DIRECTLY into the knowledge evolution pipeline
>
> ```
> Completion Log (per task) ──→ Accumulated evidence
>                                    ↓
> Lessons Learned (per epic) ──→ Wiki lesson pages (type: lesson)
>                                    ↓
> Post-Project Review ──→ Wiki pattern/decision pages
>                                    ↓
> Knowledge Transfer ──→ Wiki domain overviews + learning paths
> ```
>
> This is the knowledge-evolution methodology model (document → implement) applied to completed work. The "implement" stage for knowledge-evolution IS the writing of the evolved page. The raw material comes from closure artifacts.

#### Completion Log Standard

> [!info] Required after EVERY task — the minimum closure artifact
>
> | Section | Content |
> |---------|---------|
> | Task ID + title | What was completed |
> | Stages executed | Which stages, in what order |
> | Artifacts produced | File paths of everything created/modified |
> | Gate results | What commands were run, what passed |
> | Decisions made | Any choices that diverged from the plan |
> | Issues encountered | Problems and how they were resolved |
> | Concerns | Anything that felt wrong or uncertain |
> | Commit hashes | One per stage |
>
> **In our methodology:** OpenArms generates these automatically via write-completion-log.cjs. The wiki records them manually in wiki/log/. They should be REQUIRED, not optional.

### Monitoring Artifacts (5 types)

> [!warning] The Missing Category — We Have ZERO of These
>
> | Type | Purpose | What It Would Track |
> |------|---------|-------------------|
> | **Change Management Log** | All scope changes with approval status | Epic scope changes, requirement additions, deferred items |
> | **Risk Register** | Live risk tracking with mitigation status | Technical risks, dependency risks, timeline risks |
> | **Status Report** | Progress against plan, blockers, decisions needed | Epic readiness trends, stage completion rates, blocker list |
> | **Issue Log** | Problems encountered, resolution, owner | Bugs found during implementation, technical debt identified |
> | **Compliance Report** | Methodology adherence metrics | Stage boundary violations, missing artifacts, readiness inflation |
>
> **The compliance gap is the most critical.** Without Compliance Reports, we can't answer: "Are agents following the methodology?" OpenArms's overnight run (75% violation rate) was only detected because someone analyzed the git log manually. A Compliance Report artifact would detect this automatically.

#### What a Compliance Report Would Contain

> [!info] Post-session methodology adherence analysis
>
> | Metric | How to Measure |
> |--------|---------------|
> | Stage boundary compliance | Git diff per stage — any FORBIDDEN artifacts in the diff? |
> | Artifact chain completeness | Do all required artifacts exist for the completed stages? |
> | Readiness accuracy | Does computed readiness match claimed readiness? |
> | One-commit-per-stage | Git log — one commit per stage transition? |
> | Done When verification | Are Done When items verified against real artifacts? |
> | Model selection correctness | Was the right model selected for the task type? |
>
> This is a future tooling target — building automated compliance checking into the pipeline.

### Per-Domain Deployment Variations

> [!abstract] Deployment looks very different per domain
>
> | Domain | Key Deployment Artifacts | Gate |
> |--------|------------------------|------|
> | **TypeScript** | npm publish, Docker build, CI/CD pipeline config | Build passes, tests pass, publish succeeds |
> | **Python/Wiki** | pipeline post, sync to Obsidian, export to consumers | 0 validation errors, sync confirmed |
> | **Infrastructure** | terraform apply, DNS updates, monitoring setup | Apply succeeds, health checks pass |
> | **Knowledge** | Evolution pipeline run, domain overview update | New pages validated, relationships wired |

## Open Questions

> [!question] ~~Should Compliance Reports be generated automatically by the pipeline?~~
> **RESOLVED:** Yes — extend pipeline with basic compliance checking. See [[artifact-system-design-decisions|Decision — Artifact System Design Decisions]].

> [!question] ~~Should the wiki have a formal Status Report template?~~
> **RESOLVED:** Yes — lightweight template as note type, not new page type. See [[methodology-stage-extension-decisions|Decision — Methodology Stage Extension Decisions]].

> [!question] ~~Should Completion Logs be REQUIRED or RECOMMENDED?~~
> **RESOLVED:** Required for epic/module, advisory for tasks. See [[artifact-system-design-decisions|Decision — Artifact System Design Decisions]].

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **What principle applies?** | [[right-process-for-right-context-the-goldilocks-imperative|Principle — Right Process for Right Context — The Goldilocks Imperative]] |
> | **What is my identity?** | [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]] |
> | **System map** | [[methodology-system-map|Methodology System Map]] |
> | **Operations plan standards** | [[operations-plan-page-standards|Operations Plan Page Standards]] — quality bar for runbooks and deployment docs |
> | **Lesson standards** | [[lesson-page-standards|Lesson Page Standards]] — how to write closure lessons |
> | **Knowledge evolution** | [[model-knowledge-evolution|Model — Knowledge Evolution]] — how closure feeds back into the wiki |

## Relationships

- BUILDS ON: [[methodology-artifact-taxonomy|Methodology Artifact Taxonomy]]
- BUILDS ON: [[operations-plan-page-standards|Operations Plan Page Standards]]
- RELATES TO: [[model-methodology|Model — Methodology]]
- RELATES TO: [[model-knowledge-evolution|Model — Knowledge Evolution]]
- RELATES TO: [[note-page-standards|Note Page Standards]]
- RELATES TO: [[lesson-page-standards|Lesson Page Standards]]
- FEEDS INTO: [[artifact-chains-by-model|Artifact Chains by Methodology Model]]
- FEEDS INTO: [[methodology-evolution-protocol|Methodology Evolution Protocol]]

## Backlinks

[[methodology-artifact-taxonomy|Methodology Artifact Taxonomy]]
[[operations-plan-page-standards|Operations Plan Page Standards]]
[[model-methodology|Model — Methodology]]
[[model-knowledge-evolution|Model — Knowledge Evolution]]
[[note-page-standards|Note Page Standards]]
[[lesson-page-standards|Lesson Page Standards]]
[[artifact-chains-by-model|Artifact Chains by Methodology Model]]
[[methodology-evolution-protocol|Methodology Evolution Protocol]]
[[artifact-system-design-decisions|Decision — Artifact System Design Decisions]]
[[methodology-stage-extension-decisions|Decision — Methodology Stage Extension Decisions]]
