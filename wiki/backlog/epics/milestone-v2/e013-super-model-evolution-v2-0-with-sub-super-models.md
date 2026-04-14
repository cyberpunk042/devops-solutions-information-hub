---
title: E013 — Super-Model Evolution — v2.0 with Sub-Super-Models
aliases:
  - "E013 — Super-Model Evolution — v2.0 with Sub-Super-Models"
  - "E013 — Super-Model Evolution: v2.0 with Sub-Super-Models"
type: epic
domain: backlog
status: draft
priority: P0
task_type: epic
current_stage: document
readiness: 70
progress: 75
stages_completed:
artifacts:
  - "wiki/spine/super-model.md"
confidence: high
created: 2026-04-12
updated: 2026-04-13
sources:
  - id: milestone
    type: file
    file: wiki/backlog/milestones/second-brain-complete-system-v2-0.md
  - id: operator-directive
    type: directive
    file: raw/notes/2026-04-12-full-chain-requirement-directive.md
tags: [epic, super-model, evolution, sub-models, goldilocks, v2, milestone-v2]
---

# E013 — Super-Model Evolution — v2.0 with Sub-Super-Models
## Summary

Evolve the super-model from a single dashboard page (currently v1.3) into a system of interconnected super-models — each governing a DOMAIN of the framework. The current super-model tries to be everything: adoption tiers, model dependency graph, quality contract, per-project adaptation, version assessment. That's too much in one page. v2.0 splits into a ROOT super-model (the entry point and dashboard) plus SUB-SUPER-MODELS that each govern one concern. The Goldilocks Protocol becomes its own sub-super-model. The Enforcement Hierarchy becomes its own. The Knowledge Architecture becomes its own. Each is navigable, each has its own standards, each connects to the root.

## Operator Directive

> "updating the models and the standards and the examples and the super-model and creating the new super-models"

> "do not confuse everything. the words are important. goldilock is not model and model is not standard and standard is not example and example is not template and none of this is knowledge but knowledge is at all their layers."

> "lets not forget how all the knowledge of the information hub / research wiki / second brain must all come together"

> "it allow to browse and navigate properly at each layer with always the right level and right structure of information and format and directives"

## Goals

- Root super-model (v2.0) is a clean DASHBOARD — shows the system, links to sub-super-models, provides adoption tiers. Not a 200-line monolith.
- Each sub-super-model GOVERNS its domain: defines what's in it, what the standards are, how to navigate within it, what models compose it.
- The Goldilocks Protocol is a sub-super-model (not just a concept page) — it governs identity, SDLC profile selection, and adaptation.
- The Enforcement Hierarchy is a sub-super-model — governs infrastructure, hooks, harness, immune system, compliance.
- The Knowledge Architecture is a sub-super-model — governs layers (L0-L6), maturity folders, evolution pipeline, principles.
- The Work Management system is a sub-super-model — governs hierarchy (milestone→task), readiness/progress, PM levels, impediments.
- The SDLC Framework is a sub-super-model — governs profiles, phases, scale, global standards.
- Each sub-super-model has its own: member models, member standards, member lessons/patterns, navigation guide.
- The root super-model links to ALL sub-super-models with a "start here" routing table.

## Done When

- [ ] Root super-model v2.0 — clean dashboard, routes to sub-super-models, substantial depth (≥150 lines)
- [ ] Sub-Super-Model: Goldilocks Protocol — identity, SDLC profile selection, adaptation, flexibility
- [ ] Sub-Super-Model: Enforcement Hierarchy — hooks, harness, immune system, compliance, principles
- [ ] Sub-Super-Model: Knowledge Architecture — layers, maturity, evolution, principles, lessons→patterns→decisions flow
- [ ] Sub-Super-Model: Work Management — hierarchy, readiness/progress, PM levels, impediments, SDLC profiles
- [ ] Sub-Super-Model: Integration & Ecosystem — dual-perspective, feedback loop, sister projects, gateway
- [ ] Each sub-super-model has: member models table, member standards, navigation to related knowledge
- [ ] Root super-model routing table: "I want to..." → go to sub-super-model X
- [ ] All sub-super-models pass `pipeline post` with 0 errors
- [ ] Operator can navigate from root to any specific piece of knowledge in ≤3 clicks

## Scale and Model

> [!info] Epic Parameters
>
> | Parameter | Value |
> |-----------|-------|
> | **Model** | knowledge-evolution (document → implement) |
> | **Quality tier** | Skyscraper |
> | **Estimated modules** | 2 (root evolution + sub-super-models creation) |
> | **Estimated tasks** | 5-8 |
> | **Dependencies** | E010 (Models must be current before super-model aggregates them) |

## Stage Artifacts

> [!abstract] Stage → Artifact Map
>
> | Stage | Required Artifacts |
> |-------|-------------------|
> | Document | THIS epic page. Design decision: which sub-super-models? What goes in each? |
> | Implement | Root super-model v2.0. 5 sub-super-model pages. |
> | Validation | Navigation test: can operator reach any knowledge in ≤3 clicks from root? |

## Module Breakdown

### M1: Design the Sub-Super-Model Architecture

| Task | What | Est. |
|------|------|------|
| T-E013-01 | Design decision: which sub-super-models, what each contains, how they interconnect | M |

**Proposed sub-super-model structure:**

```
Root Super-Model (v2.0) — dashboard + routing
├── Sub-SM: Goldilocks Protocol
│   ├── Members: Self-Identification Protocol, SDLC Framework, Three PM Levels, Readiness/Progress
│   ├── Principles: Goldilocks Imperative
│   └── Standards: Goldilocks adherence guide
│
├── Sub-SM: Enforcement Hierarchy
│   ├── Members: Model: Quality, Model: Skills/Commands/Hooks, Enforcement Hook Patterns, Three Lines of Defense
│   ├── Principles: Infrastructure Over Instructions
│   ├── Lessons: 7 Failure Classes, Harness Convergence, Mindful Enforcement, Context Compaction
│   └── Standards: Enforcement adherence guide
│
├── Sub-SM: Knowledge Architecture
│   ├── Members: Model: LLM Wiki, Model: Knowledge Evolution, Model: Wiki Design
│   ├── Principles: Structured Context
│   ├── Layers: L0 raw → L1 sources → L2 concepts → L3 comparisons → L4 lessons → L5 patterns+principles → L6 decisions
│   ├── Maturity: 00_inbox → 04_principles
│   └── Standards: LLM Wiki Standards, per-type standards (15)
│
├── Sub-SM: Work Management
│   ├── Members: Backlog Hierarchy, Readiness/Progress, PM Levels, Impediments
│   ├── Hierarchy: Milestone → Epic → Module → Task
│   ├── SDLC Profiles: simplified / default / full
│   └── Standards: Frontmatter Field Reference
│
└── Sub-SM: Integration & Ecosystem
    ├── Members: Model: Ecosystem Architecture, Feedback Loop, Dual-Perspective
    ├── Sister Projects: OpenArms (harness-v2), OpenFleet (full system), AICP, devops-control-plane
    ├── Gateway Tools: query, template, config, contribute, navigate
    └── Standards: Global Standards Adherence
```

### M2: Build Sub-Super-Models + Evolve Root

| Task | What | Est. |
|------|------|------|
| T-E013-02 | Evolve root super-model → v2.0 dashboard (slim down, add routing table) | L |
| T-E013-03 | Create Sub-SM: Goldilocks Protocol | M |
| T-E013-04 | Create Sub-SM: Enforcement Hierarchy | M |
| T-E013-05 | Create Sub-SM: Knowledge Architecture | M |
| T-E013-06 | Create Sub-SM: Work Management | M |
| T-E013-07 | Create Sub-SM: Integration & Ecosystem | M |
| T-E013-08 | Wire all sub-super-models to root + to each other + to member pages | S |

## Dependencies

- **E010 (Model Updates):** Super-model aggregates models. If models are outdated, the super-model misrepresents the system. E010 M1 (core models) should complete first.
- **E011 (Standards):** Sub-super-models reference standards. Standards should be exemplified before sub-SMs reference them.
- **No hard block:** The design (M1) can start immediately. Implementation (M2) should wait for E010 completion.

## Open Questions

> [!question] ~~Is 5 sub-super-models the right number?~~
> **RESOLVED:** Follows domain count. Currently 5 (Goldilocks, Enforcement, Knowledge, Work Management, Integration). Grows with domains.
> Could be fewer (merge Goldilocks + Work Management since they both deal with "how much process"). Could be more (split Knowledge Architecture into "wiki structure" + "evolution pipeline"). The design task (T-E013-01) must resolve this.

> [!question] ~~Should sub-super-models be spine pages or domain pages?~~
> **RESOLVED:** Created as spine pages under `spine/super-model/`. They are navigation hubs, not knowledge content. See [[super-model|Super-Model — Research Wiki as Ecosystem Intelligence Hub]] for the root and siblings in `wiki/spine/super-model/`.

> [!question] ~~What happens to the current super-model v1.3 content?~~
> **RESOLVED:** Evolved to v2.0 with a routing table. The v1.3 content was decomposed into sub-super-model pages (goldilocks-protocol, enforcement-hierarchy, knowledge-architecture, work-management, integration-ecosystem). See [[super-model|Super-Model — Research Wiki as Ecosystem Intelligence Hub]].

## Handoff Context

> [!info] For anyone picking this up in a fresh context:
>
> **What this epic does:** Splits the monolithic super-model (currently 200+ lines, v1.3) into a root dashboard + 5 sub-super-models, each governing one domain of the framework.
>
> **Why:** The operator said "goldilock is not model and model is not standard" — each concept needs its own navigable home. A single super-model page can't serve as the entry point for Goldilocks AND enforcement AND knowledge architecture AND work management. Sub-super-models give each domain its own hub.
>
> **Current state:** The super-model (v1.3) has: adoption tiers table, model dependency graph (15 models in reading order), per-project adaptation table, quality contract, version assessment (v1.3), key pages table, open questions. The v1.3 assessment was updated multiple times the 2026-04-12 session.
>
> **What needs to happen:**
> 1. Design which sub-super-models (proposed: 5 — Goldilocks, Enforcement, Knowledge, Work Management, Integration)
> 2. For each: determine member models, member standards, member lessons/patterns, navigation structure
> 3. Build each sub-super-model page with: summary, member table, "start here" routing, navigation weave
> 4. Slim down root super-model to dashboard + routing + version assessment
> 5. Wire everything: root → sub-SMs → members → back to root
>
> **Key files to read first:**
> - `wiki/spine/super-model.md` — current v1.3 (the source material to decompose)
> - `wiki/spine/references/model-registry.md` — all 16 models with status
> - `wiki/spine/references/methodology-system-map.md` — complete lookup for every component
> - `wiki/domains/cross-domain/project-self-identification-protocol.md` — the Goldilocks protocol that becomes a sub-SM
> - This milestone page: `wiki/backlog/milestones/second-brain-complete-system-v2-0.md`

## Relationships

- PART OF: [[second-brain-complete-system-v2-0|Milestone — Second Brain Complete System — v2.0]]
- IMPLEMENTS: [[second-brain-integration-requirements|Second Brain Integration System — Full Chain Requirements]] (FR-D4, FR-G5)
- DEPENDS ON: [[e010-model-updates-all-15-models-reflect-current-knowledge|E010 — Model Updates — All 16 Models Reflect Current Knowledge]]
- BUILDS ON: [[super-model|Super-Model — Research Wiki as Ecosystem Intelligence Hub]]
- BUILDS ON: [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]]
- FEEDS INTO: [[e014-goldilocks-navigable-system-identity-to-action-in-continuous-flow|E014 — Goldilocks Navigable System — Identity to Action in Continuous Flow]] (E014)
- FEEDS INTO: [[e019-obsidian-navigation-complete-browse-experience-with-folder-cleanup|E019 — Obsidian Navigation — Complete Browse Experience with Folder Cleanup]] (E019)

## Backlinks

[[second-brain-complete-system-v2-0|Milestone — Second Brain Complete System — v2.0]]
[[second-brain-integration-requirements|Second Brain Integration System — Full Chain Requirements]]
[[e010-model-updates-all-15-models-reflect-current-knowledge|E010 — Model Updates — All 16 Models Reflect Current Knowledge]]
[[super-model|Super-Model — Research Wiki as Ecosystem Intelligence Hub]]
[[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]]
[[e014-goldilocks-navigable-system-identity-to-action-in-continuous-flow|E014 — Goldilocks Navigable System — Identity to Action in Continuous Flow]]
[[e019-obsidian-navigation-complete-browse-experience-with-folder-cleanup|E019 — Obsidian Navigation — Complete Browse Experience with Folder Cleanup]]
