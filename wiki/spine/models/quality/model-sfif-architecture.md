---
title: Model — SFIF and Architecture
aliases:
  - "Model — SFIF and Architecture"
  - "Model: SFIF and Architecture"
type: concept
domain: cross-domain
layer: spine
status: synthesized
confidence: high
maturity: growing
created: 2026-04-09
updated: 2026-04-13
sources: []
tags: [model, spine, sfif, architecture, quality-tiers, build-lifecycle, skyscraper, pyramid, mountain, recursive, cross-domain]
---

# Model — SFIF and Architecture
## Summary

The SFIF and Architecture model describes the universal 4-stage build lifecycle (Scaffold → Foundation → Infrastructure → Features) and the 3-tier quality analogy (Skyscraper/Pyramid/Mountain) that together form a complete framework for building, auditing, and improving software systems. ==SFIF is recursive — it applies at project, feature, component, and design levels simultaneously, each advancing at its own pace.== The four ecosystem projects each have documented SFIF instances making the abstract pattern concrete.

## Key Insights

- **The pattern is recursive by design.** A backend may be Skyscraper-tier while the frontend it serves is Mountain-tier. "Where is this project?" requires specifying the layer of granularity.

- **Stage boundaries are structural commitments, not completion percentages.** Foundation is complete when there's a single entry point — not when 70% of code is written. Exit criteria are about stability, not volume.

- **Mountain is the natural entropy state.** POC decisions never revisited. Hotfixes layered. Features added without structural investment. SFIF prevents the default entropy.

- **Pyramid is the practitioner's art.** Improving a Mountain into a Pyramid without stopping delivery — principled compromises around immovable constraints. Most real engineering lives here.

- **POC → Production without rewrite is the critical failure pattern.** Mountain code deployed as production, then scaled as if Skyscraper, produces emergency rewrites at 10x cost.

## Deep Analysis

### The Four SFIF Stages

> [!info] **Four stages with structural exit criteria**
> | Stage | Question it answers | Exit criterion | What it is NOT |
> |-------|-------------------|---------------|----------------|
> | **Scaffold** | "Where is this project headed?" | Direction decided, documented. Project is *joinable*. | Running code |
> | **Foundation** | "Does this work at its simplest?" | Single entry point manages everything. System is *operable*. | All functionality implemented |
> | **Infrastructure** | "Can other things depend on this?" | Cross-cutting concerns handled transparently. System is *dependable*. | Features |
> | **Features** | "What specialized value does this deliver?" | No terminal criterion — ongoing work on the stable base. | Infrastructure |

> [!warning] **The Infrastructure/Feature boundary is the most commonly violated**
> Infrastructure ENABLES. Features USE what infrastructure enables. Auth logic in a feature controller = infrastructure that was skipped. Retry logic in every API call = infrastructure that was never built.

See [[scaffold-foundation-infrastructure-features|Scaffold → Foundation → Infrastructure → Features]] for full stage descriptions, anti-patterns per stage, and the recursive property.

---

### The Three Quality Tiers

> [!success] **Skyscraper — all SFIF stages complete and clean**
> Scaffold artifacts exist and are current. Single entry point. Infrastructure is stable. Features build clearly on infrastructure. The system can grow upward without structural compromise. Requires conditions: greenfield, authorized refactor, or layer-by-layer rebuild.

> [!warning] **Pyramid — functional, built around real constraints**
> Legacy database that can't be migrated. Team that can't pause delivery. Third-party integration forcing compromise. ==Pyramid decisions are principled (tradeoff understood and documented), not random (tradeoff unknown).== Pyramid is not failure — it is the art of improving a Mountain without stopping delivery.

> [!bug]- **Mountain — accumulated mass, no structure**
> Spaghetti code, deprecated patterns on ad-hoc fixes, no scaffold or stale scaffold, multiple entry points, auth everywhere, no consistent error handling. Works, but only the builders understand why. Mountain is what happens when SFIF stages get skipped.
>
> **Mountain is reversible** — but the reversal is expensive. The correct path: Mountain → Pyramid (stabilize around constraints) → Skyscraper (when conditions allow full refactor).

See [[skyscraper-pyramid-mountain|Skyscraper, Pyramid, Mountain]] for the full tier analysis and the improvement path.

---

### The Four Ecosystem Instances

> [!info] **SFIF across the ecosystem**
> | Project | Scaffold | Foundation | Infrastructure | Features |
> |---------|----------|-----------|----------------|----------|
> | **Research Wiki** | CLAUDE.md, wiki/ structure, schema | tools/common.py, validation, manifest.json | pipeline.py post-chain, MCP server, lint, obsidian | Evolve pipeline, watcher, sync, export |
> | **OpenFleet** | SOUL.md + HEARTBEAT.md, monorepo layout | Deterministic orchestrator, agent base model | doctor.py (24 rules), IRC routing, OpenClaw gateway | 10 specialized agents, Mission Control UI |
> | **AICP** | Profile system, CLAUDE.md, venv | Backend router, circuit breaker, complexity scorer | MCP tools, guardrails pipeline | Voice pipeline, 5-stage LocalAI roadmap, 78 skills |
> | **Front↔Mid↔Back** | Per-layer design decisions | Per-layer component library, routing | Per-layer auth, state, API contracts | Per-layer screens, flows, logic |

---

### Auditing a System Against SFIF

> [!tip] **Audit checklist per stage**
> - **Scaffold**: Does CLAUDE.md match the actual system? Can a new person understand the project's intent from scaffold artifacts alone? If no → scaffold is absent or stale.
> - **Foundation**: Is there ONE entry point? If there are 5 ways to start the app → foundation is incomplete. Binary: single entry or not.
> - **Infrastructure**: Can you add a feature WITHOUT touching shared concerns (auth, retry, logging)? If adding an endpoint requires modifying infra → infrastructure is incomplete.
> - **Features**: Are features using infrastructure or re-implementing it? Copied auth, bespoke retry, hardcoded config = features built before infrastructure.

> [!info] **Tier indicators**
> | Tier | What you see |
> |------|-------------|
> | **Mountain** | No scaffold, multiple entry points, auth/retry in feature code, no schema, no tests or tests against implementation |
> | **Pyramid** | Scaffold exists but partially outdated, clear foundation with 1-2 legacy entry points, 80% infra coverage with documented exceptions |
> | **Skyscraper** | Scaffold current, single entry point, all cross-cutting at infra layer, features are pure feature logic, tests verify behavior contracts |

---

### The Recursive Property

> [!abstract] **SFIF applies at every granularity simultaneously**
> - A *project* traverses Scaffold → Foundation → Infrastructure → Features
> - Each *feature* within the project traverses the same four stages
> - Each *component* within a feature traverses them again
> - The *design system* independently traverses: decisions (S) → component library (F) → responsive grid (I) → specialized screens (F)
>
> Structural quality can exist at one level and not another. The wiki is Skyscraper at the system level but individual pages can be Mountain. Per-level audit is required, not a single verdict.

---

### Knowledge SFIF — The Wiki Analog

The SFIF stages map directly to wiki knowledge work:

> [!abstract] SFIF Applied to Knowledge Systems
>
> | SFIF Stage | Code Equivalent | Wiki Equivalent | Gate |
> |-----------|----------------|-----------------|------|
> | **Scaffold** | Empty types + stubs | Frontmatter + section headings (from template) | Page exists, schema valid |
> | **Foundation** | Core logic working | Summary + Key Insights filled with real content | ≥30 word summary, ≥1 insight |
> | **Infrastructure** | Integrated into system | Relationships wired, navigation weave, domain index | ≥1 relationship, reachable from index |
> | **Features** | Full functionality | Deep Analysis, State of Knowledge, Open Questions, examples | Per-type thresholds met |
>
> **The quality tiers also apply:**
> - **Pyramid** (POC knowledge): Quick capture, minimal structure. raw/notes/ files.
> - **Skyscraper** (Production knowledge): Full structure, validated content, evidence-backed. Validated lessons, patterns.
> - **Mountain** (Reference knowledge): Comprehensive, self-validating, exemplary. Model pages, standards with annotated exemplars.

A wiki page that skips Foundation (jumping from raw notes to a pattern) produces the knowledge equivalent of a Mountain: pattern-typed content that is a single-source restatement with no cross-linking. See [[progressive-distillation|Progressive Distillation]].

---

### Key Pages

| Page | Layer | Role in the model |
|------|-------|-------------------|
| [[scaffold-foundation-infrastructure-features|Scaffold → Foundation → Infrastructure → Features]] | L5 | The pattern definition — 4 stages, exit criteria, recursive property, 4 instances |
| [[skyscraper-pyramid-mountain|Skyscraper, Pyramid, Mountain]] | L2 | The quality tier framework — structural state assessment |
| [[progressive-distillation|Progressive Distillation]] | L5 | Knowledge analog — same density-increasing structure applied to knowledge |
| [[four-project-ecosystem|Four-Project Ecosystem]] | L2 | The projects that implement SFIF instances |
| [[models-are-built-in-layers-not-all-at-once|Models Are Built in Layers, Not All at Once]] | L4 | Lesson: model-building follows SFIF — scaffold ≠ substance |
| [[infrastructure-as-code-patterns|Infrastructure as Code Patterns]] | L2 | IaC as the scaffold layer's primary artifact class |

---

### Lessons Learned

| Lesson | What was learned |
|--------|-----------------|
| [[models-are-built-in-layers-not-all-at-once|Models Are Built in Layers, Not All at Once]] | Building this wiki's models followed SFIF: scaffold (entry points) → foundation (maturity assignment) → infrastructure (system definitions) → features (standards pages). Claiming "done" at scaffold level was a documented failure. |
| [[infrastructure-must-be-reproducible-not-manual|Infrastructure Must Be Reproducible, Not Manual]] | Infrastructure stage artifacts must be IaC. Manual infra = Mountain-tier infrastructure that drifts silently. |
| [[never-skip-stages-even-when-told-to-continue|Never Skip Stages Even When Told to Continue]] | "Continue" means advance within the current SFIF stage, not skip to Features. Stage skipping is how Mountains are built. |

---

### State of Knowledge

> [!success] **Well-covered**
> - Four SFIF stages with structural exit criteria (not completion percentages)
> - Three quality tiers with concrete indicators per tier
> - Four ecosystem instances with per-stage artifact examples
> - Audit procedure (scaffold/foundation/infrastructure/feature checks)
> - Recursive property demonstrated across 4 granularity levels
> - Knowledge layer analog via Progressive Distillation

> [!warning] **Thin or unverified**
> - SFIF as a tooling check — could validation detect "infrastructure masquerading as features"?
> - Pyramid → Skyscraper boundary — is it a discrete refactor or continuous improvement?
> - SFIF for data pipelines and ML deployment — where is the Foundation/Infrastructure boundary?
> - No automated SFIF audit tool exists — currently manual evaluation only

---

### How to Adopt

> [!info] **Applying SFIF to a new or existing project**
> 1. **Audit current state** — per stage, per layer (use the checklist above)
> 2. **Identify the weakest stage** — that's where structural debt lives
> 3. **Fix from the bottom up** — don't add features to fix foundation problems. Fix the foundation first.
> 4. **Choose your quality tier honestly** — Pyramid is fine if the constraints are real and documented. Mountain is the failure mode.

> [!warning] **INVARIANT — never change these**
> - Stage exit criteria are structural, not percentage-based
> - Infrastructure ≠ Features (the most violated boundary)
> - Mountain is the default without intervention (entropy applies)
> - Per-level audit, not single-verdict assessment
> - POC code is Mountain-tier by design and MUST be rewritten for production

> [!tip] **PER-PROJECT — always adapt these**
> - Which stages need emphasis (greenfield = Scaffold first; legacy = audit Foundation first)
> - Quality tier target (Skyscraper for new systems; Pyramid-improving for legacy)
> - Granularity of recursive application (project + feature level is usually sufficient)
> - The specific exit criteria per stage (domain-specific artifacts)

### Connection to SDLC Customization

SFIF and the SDLC Customization Framework are complementary:
- **SFIF** describes the BUILD lifecycle (what order to construct things)
- **SDLC profile** describes the PROCESS lifecycle (how much rigor wraps the build)
- **Quality tiers** (Skyscraper/Pyramid/Mountain) map to SDLC profiles (Full/Default/Simplified)

> [!info] SFIF × SDLC Profile
>
> | Quality Tier | SDLC Profile | CMMI Level | What It Means |
> |-------------|-----------|-----------|---------------|
> | Skyscraper | Full | 4 (Quantitative) | Every SFIF stage gets full artifacts + gates + review |
> | Pyramid | Middle Ground | 3 (Defined) | Deliberate compression — SFIF stages with selected artifacts |
> | Mountain | Simplified or None | 1-2 (Initial/Managed) | POC decisions never revisited. Acceptable for POC phase only. |
>
> See [[sdlc-customization-framework|SDLC Customization Framework — Phases, Scale, and Profile Selection]] for phase × scale decision matrix.

The phase progression (POC → MVP → Staging → Production) also maps to SFIF: POC is the Scaffold of the product lifecycle. MVP is Foundation. Staging is Infrastructure. Production is Features at scale. The pattern IS recursive — SFIF at the product level mirrors SFIF at the code level.

## Open Questions

> [!question] ~~****Can SFIF be detected automatically?****~~
> **RESOLVED:** Detection automatable (AST for scaffold, coverage for foundation, import graph for infrastructure). Advancement decision remains human.
> Could `tools/validate` or a static analysis tool detect "infrastructure in features" (auth in controllers, retry in handlers)? (Requires: defining detectable anti-patterns per stage)

> [!question] ~~****Where is the Pyramid → Skyscraper boundary?****~~
> **RESOLVED:** POC→MVP phase transition. Same trigger as simplified→default chain upgrade. When real users depend on the output.
> Is it a discrete architectural decision (refactor sprint) or continuous improvement? Can a system cross the boundary without anyone noticing? (Requires: observing the transition in a real project)

> [!question] ~~**Does SFIF × SDLC Profile produce a formal upgrade path?**~~
> **RESOLVED:** Conceptually yes — a project at Pyramid quality on simplified profile upgrades to Skyscraper/default when triggers hit. Not yet formalized.
> If a project is Mountain/Simplified (POC), is the upgrade path: Mountain→Pyramid (quality) THEN Simplified→Default (process)? Or do quality and process upgrade together? (Requires: empirical data from at least 2 project upgrades)

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **Quality model** | [[model-quality-failure-prevention|Model — Quality and Failure Prevention]] |
> | **Methodology model** | [[model-methodology|Model — Methodology]] |
> | **Quality tiers** | [[skyscraper-pyramid-mountain|Skyscraper, Pyramid, Mountain]] |
> | **Methodology standards** | [[model-methodology-standards|Methodology Standards — What Good Execution Looks Like]] |

## Relationships

- BUILDS ON: [[scaffold-foundation-infrastructure-features|Scaffold → Foundation → Infrastructure → Features]]
- BUILDS ON: [[skyscraper-pyramid-mountain|Skyscraper, Pyramid, Mountain]]
- BUILDS ON: [[progressive-distillation|Progressive Distillation]]
- RELATES TO: [[model-markdown-as-iac|Model — Markdown as IaC — Design.md and Agent Configuration]]
- RELATES TO: [[model-quality-failure-prevention|Model — Quality and Failure Prevention]]
- RELATES TO: [[model-knowledge-evolution|Model — Knowledge Evolution]]
- RELATES TO: [[model-methodology|Model — Methodology]]
- RELATES TO: [[four-project-ecosystem|Four-Project Ecosystem]]

## Backlinks

[[scaffold-foundation-infrastructure-features|Scaffold → Foundation → Infrastructure → Features]]
[[skyscraper-pyramid-mountain|Skyscraper, Pyramid, Mountain]]
[[progressive-distillation|Progressive Distillation]]
[[model-markdown-as-iac|Model — Markdown as IaC — Design.md and Agent Configuration]]
[[model-quality-failure-prevention|Model — Quality and Failure Prevention]]
[[model-knowledge-evolution|Model — Knowledge Evolution]]
[[model-methodology|Model — Methodology]]
[[four-project-ecosystem|Four-Project Ecosystem]]
[[global-standards-adherence|Global Standards Adherence — Engineering Principles the Wiki Follows]]
[[model-local-ai|Model — Local AI ($0 Target)]]
