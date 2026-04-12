---
title: "Initiation and Planning Artifacts — Standards and Guide"
type: concept
domain: cross-domain
status: synthesized
confidence: high
maturity: seed
created: 2026-04-12
updated: 2026-04-12
sources:
  - id: taxonomy
    type: wiki
    file: wiki/domains/cross-domain/methodology-artifact-taxonomy.md
  - id: sdlcforms
    type: article
    url: "https://www.sdlcforms.com/UnderstandingSDLC.html"
  - id: openarms-chain
    type: file
    file: /home/jfortin/openarms/wiki/domains/architecture/methodology-document-chain.md
tags: [methodology, initiation, planning, artifacts, project-charter, wbs, risk, standards]
---

# Initiation and Planning Artifacts — Standards and Guide

> [!tip] AI Quick Start — BEFORE Methodology Stages Begin
>
> 1. **Working on an epic?** Check: does the epic have an operator directive in raw/notes/? That's your initiation artifact.
> 2. **Need to break down work?** The WBS = Epic → Module → Task hierarchy. See [[Backlog Hierarchy Rules]] for the 8 rules.
> 3. **Need risk assessment?** That's the Gap Analysis — produced during Document stage, not separately.
> 4. **Task or module level?** You INHERIT these from the parent epic — don't produce them again.
> 5. **These artifacts are domain-agnostic** — same structure whether TypeScript, Python, or Infrastructure.

## Summary

Complete guide to the artifacts produced BEFORE methodology execution begins — the initiation and planning phases that set up an epic or project for success. These artifacts answer: WHY are we doing this (initiation), and HOW will we organize the work (planning). Most task-level work inherits these from the parent epic. Module-level work may produce lightweight versions. Only epic and project-scale work requires the full set. In our methodology, these map to the pre-Document stage or the early Document stage at epic scale.

## Key Insights

1. **Initiation artifacts exist BEFORE the methodology stage gates begin.** The stage gate system starts at Document (0-25% readiness). But before Document, someone decided THIS work is worth doing. That decision — the Project Charter, Business Case, operator directive — is the initiation artifact. In our ecosystem, the operator's verbatim directives in raw/notes/ serve this function.

2. **Planning artifacts map to the Epic → Module → Task breakdown.** The WBS (Work Breakdown Structure) IS the epic-to-task decomposition. The Project Plan IS the backlog with readiness tracking. The Risk Analysis IS the gap analysis. We already do planning — we just don't name it using standard terminology.

3. **Scale determines which artifacts are required.** A task inherits its parent's initiation and planning. A module may need a lightweight plan. An epic needs the full set. A project needs everything.

4. **These artifacts are mostly DOMAIN-AGNOSTIC.** A Project Charter looks the same whether the project is TypeScript, Python, infrastructure, or knowledge work. The content changes but the structure doesn't.

## Deep Analysis

### When to Produce Initiation Artifacts

> [!abstract] Scale → Required Initiation Artifacts
>
> | Scale | Required | Optional | Not Needed |
> |-------|----------|----------|-----------|
> | **Project** | Project Charter, Business Case, Stakeholder List, Resource Plan | Feasibility Study, CONOPS, Cost-Benefit Analysis | — |
> | **Epic** | Operator Directive (our equivalent of Project Charter), Goals, Done When | Business Case (if investment decision), Risk Assessment | Feasibility Study, CONOPS |
> | **Module** | — (inherits from epic) | Scope clarification if module boundaries are unclear | All initiation artifacts |
> | **Task** | — (inherits from epic/module) | — | All initiation artifacts |

### Initiation Artifact Standards

#### Project Charter / Operator Directive

> [!info] The document that says "this work exists and here's why"
>
> | Aspect | Standard |
> |--------|---------|
> | **What it contains** | Scope, objectives, stakeholders, success criteria, constraints, verbatim operator intent |
> | **Quality bar** | Operator's EXACT words quoted. Scope boundaries explicit. Success criteria testable. |
> | **Anti-pattern** | Paraphrased intent ("the user wants to improve quality") — must be verbatim quotes |
> | **In our wiki** | raw/notes/ directive logs + epic Summary + Goals sections |
> | **Template** | wiki/config/templates/epic.md (the Summary section IS the charter) |
>
> **Example from this wiki:**
> "we need to establish a strong method of work with the Wiki LLM structure and Methodology structure and execution and we need to establish standards for everything with example of document on top of the standards documents for each artifact type." — This is the initiation artifact for E003-E006.

#### Business Case

> [!info] WHY this work is worth the investment — cost vs benefit
>
> | Aspect | Standard |
> |--------|---------|
> | **What it contains** | Problem statement, proposed solution, cost estimate, benefit estimate, ROI, risks, alternatives |
> | **Quality bar** | Costs and benefits quantified (hours, dollars, or comparable metric). At least one alternative considered. |
> | **When needed** | When the work requires significant investment (days+) and the justification isn't obvious |
> | **When NOT needed** | When the operator has already decided (directive = implicit business case approved) |
> | **Anti-pattern** | Vague benefits ("will improve efficiency") without quantification |

#### Stakeholder List

> [!info] WHO has interest in this work — for communication and review planning
>
> | Aspect | Standard |
> |--------|---------|
> | **What it contains** | Name/role, interest level, authority level, communication needs |
> | **When needed** | Multi-team or cross-project work (ecosystem integration, shared infra) |
> | **In our ecosystem** | The 5-project ecosystem (OpenFleet, AICP, OpenArms, control-plane, research wiki) — each project is a stakeholder for shared methodology |

### When to Produce Planning Artifacts

> [!abstract] Scale → Required Planning Artifacts
>
> | Scale | Required | Optional | Not Needed |
> |-------|----------|----------|-----------|
> | **Project** | Project Plan, WBS, Risk Analysis, Roles Matrix, Config Management Plan | Procurement Plan, Approvals Matrix | — |
> | **Epic** | WBS (= module/task breakdown), Risk/Gap Analysis | Roles Matrix (if multi-agent) | Procurement, Approvals |
> | **Module** | Task breakdown (= lightweight WBS) | — | All other planning artifacts |
> | **Task** | — (inherits from module/epic) | — | All planning artifacts |

### Planning Artifact Standards

#### Work Breakdown Structure (WBS) / Epic Breakdown

> [!info] Hierarchical decomposition: Epic → Modules → Tasks
>
> | Aspect | Standard |
> |--------|---------|
> | **What it contains** | Hierarchical tree: each node is a deliverable (not an activity). Leaf nodes are tasks with estimates. |
> | **Quality bar** | Every leaf task is atomic (one deliverable), estimable (XS/S/M/L/XL), and has a Done When. No task larger than L. |
> | **Anti-pattern** | Tasks that are actually epics ("Build the authentication system" as a single task) |
> | **In our methodology** | The epic's module/task breakdown in the backlog. Epic → Module → Task hierarchy per [[Backlog Hierarchy Rules]]. |
> | **OpenArms example** | E014 broke into 14 tasks (T089-T102), each with task_type, estimate, depends_on. Readiness computed from children. |
>
> **The 8 rules from Backlog Hierarchy Rules apply here:**
> 1. Work on TASKS, not epics
> 2. Epics are NEVER done by themselves
> 3. Readiness flows UP (computed from children)
> 4. Dependencies are gates
> 5. Gaps spawn tasks
> 6. Slow is normal

#### Risk Analysis / Gap Analysis

> [!info] What could go wrong, what's missing, what's the impact
>
> | Aspect | Standard |
> |--------|---------|
> | **What it contains** | Per-risk/gap: current state (with evidence), required state, impact if unaddressed, affected scope, mitigation, complexity estimate |
> | **Quality bar** | Every gap references existing files/components. Impact is specific ("blocks scaffold stage") not vague ("could cause problems"). |
> | **Anti-pattern** | "More research needed" as a gap — that's not a gap, it's a task. Name WHAT needs researching. |
> | **Template** | wiki/config/templates/methodology/gap-analysis.md |
> | **OpenArms example** | Document #3 in the chain — "Per-gap: current state with file refs, required state, impact, affected files, complexity" |

#### Project Plan / Backlog

> [!info] Timeline, milestones, dependencies — what gets done when
>
> | Aspect | Standard |
> |--------|---------|
> | **What it contains** | Prioritized task list, dependency graph, milestone targets, readiness tracking |
> | **Quality bar** | Every task has priority (P0-P3), estimate, depends_on. Critical path identifiable. |
> | **In our methodology** | wiki/backlog/ with epic readiness computed from children. The backlog IS the project plan. |

### Per-Domain Variations

> [!abstract] Initiation/Planning artifacts are 95% domain-agnostic
>
> | Artifact | TypeScript | Python/Wiki | Infrastructure | Knowledge |
> |----------|-----------|-------------|---------------|-----------|
> | Project Charter | Same | Same | Same | Same |
> | WBS | Epic→Module→Task | Epic→Module→Task | Epic→Module→Task | Epic→Module→Task |
> | Risk Analysis | Code-specific risks (type safety, bundle size) | Wiki-specific risks (orphans, staleness) | Infra-specific risks (state drift, outage) | Knowledge-specific risks (inaccuracy, gaps) |
> | Gap Analysis | File:line references to code | Page references to wiki | Resource references to infra | Topic references to knowledge |
>
> The STRUCTURE is the same everywhere. The CONTENT varies by domain. This is why initiation and planning artifacts don't need domain profiles — they work with the same templates.

## Open Questions

> [!question] ~~Should there be an explicit "Initiation" stage before Document for epic-scale work?~~
> **RESOLVED:** No — fold initiation into Document stage at epic scale. See [[Decision: Methodology Stage Extension Decisions]].

> [!question] Should the wiki have a formal Business Case template for investment decisions?
> **DEFERRED:** Needs operator input — relevant when fleet agents propose work autonomously.

## Relationships

- BUILDS ON: [[Methodology Artifact Taxonomy]]
- BUILDS ON: [[Backlog Hierarchy Rules]]
- RELATES TO: [[Stage-Gate Methodology]]
- RELATES TO: [[Model: Methodology]]
- FEEDS INTO: [[Artifact Chains by Methodology Model]]
- FEEDS INTO: [[Epic Page Standards]]

## Backlinks

[[Methodology Artifact Taxonomy]]
[[Backlog Hierarchy Rules]]
[[Stage-Gate Methodology]]
[[Model: Methodology]]
[[Artifact Chains by Methodology Model]]
[[Epic Page Standards]]
[[Decision: Methodology Stage Extension Decisions]]
