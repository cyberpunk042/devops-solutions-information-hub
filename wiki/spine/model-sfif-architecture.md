---
title: "Model: SFIF and Architecture"
type: concept
domain: cross-domain
layer: spine
status: synthesized
confidence: high
maturity: growing
created: 2026-04-09
updated: 2026-04-09
sources: []
tags: [model, spine, sfif, architecture, quality-tiers, build-lifecycle, skyscraper, pyramid, mountain, recursive, cross-domain]
---

# Model: SFIF and Architecture

## Summary

The SFIF and Architecture model describes the universal 4-stage build lifecycle (Scaffold → Foundation → Infrastructure → Features) and the 3-tier quality analogy (Skyscraper/Pyramid/Mountain) that together form a complete framework for building, auditing, and improving software systems. SFIF is recursive — it applies at the project level, the feature level, the sub-component level, and the design level simultaneously, with each layer advancing at its own pace. Skyscraper/Pyramid/Mountain describes the structural state of any system at any point in time: Skyscraper (all stages complete, clean), Pyramid (pragmatic compromise under real constraints), Mountain (accumulated mass, no structure). The four ecosystem projects — research wiki, OpenFleet, AICP, and layered front/middleware/backend systems — each have documented SFIF instances that make the abstract pattern concrete and verifiable.

## Key Insights

- **The pattern is recursive by design**: a project in Infrastructure stage has features within each subsystem that are themselves in Scaffold stage. A backend service may be Skyscraper-tier while the frontend it serves is Mountain-tier. Evaluating "where is this project?" always requires specifying the layer of granularity — system-level assessments are only valid when each layer is evaluated independently.

- **Stage boundary conditions are structural commitments, not completion percentages**: Foundation is complete when there is a single entry point that manages everything — not when 70% of the code is written. Infrastructure is complete when other things can reliably depend on it — not when the components exist. The exit criterion is about structural stability, not code volume.

- **Mountain is the natural entropy state**: systems do not accumulate to Mountain intentionally. Emergency hotfixes layer over each other. POC decisions never get revisited. Features get added without structural investment. Mountain is what systems become when SFIF stages get skipped, abbreviated, or rushed. The pattern is not prescriptive overhead — it is the thing that prevents the default entropy.

- **Pyramid is the practitioner's art**: building a Skyscraper from scratch is straightforward. The harder skill is improving a Mountain into a Pyramid without stopping delivery — making principled compromises around immovable constraints while still moving the structural quality forward. Most real engineering lives in Pyramid territory.

- **POC → Production without rewrite is the critical failure pattern**: POC code is Mountain-tier by design. It is exploratory, expedient, undocumented, untested. Deploying Mountain code as production, then scaling it as if it were Skyscraper, produces the systems that require emergency rewrites at 10x the original cost. The correct sequence is Mountain (POC) → Pyramid (rewrite for production) → Skyscraper (refactor when conditions allow).

- **SFIF alignment is the Skyscraper's distinguishing property**: a Skyscraper is not just clean code — it is a system where scaffold artifacts (CLAUDE.md, DESIGN.md, README) exist and are current, where there is a single entry point managing the system, where infrastructure is stable enough that features depend on it reliably. A Mountain can have clean code at the line level while being Mountain-tier at the structural level.

## Deep Analysis

### The Four SFIF Stages

**Stage 1 — Scaffold**

Core config files, project structure, tech stack choice, AI configuration (CLAUDE.md, DESIGN.md), READMEs. The scaffolding phase answers: "Where is this project headed?"

Exit criterion: direction is decided and documented. Anyone joining the project can understand the intent, the stack, and the conventions without reading code. The project is *joinable*.

What Scaffold is NOT: running code. The scaffold stage is about establishing shared understanding, not building anything functional. A project that skips Scaffold produces a codebase that is internally consistent but externally opaque — each team member has a different mental model of what the project is for.

**Stage 2 — Foundation**

Single entry point established, core data model defined, basic connectivity proven, error handling patterns set. The foundation phase answers: "Does this actually work at its simplest?"

Exit criterion: a single entry point manages everything. `main.py`, `pipeline.py`, `orchestrator.py` — one file is the system's center of gravity. All other components are loaded, configured, or invoked through it. The system is *operable*.

What Foundation is NOT: all functionality implemented. Foundation is about establishing the structural center, not building out the surface. A project with ten entry points is a project with no foundation — it has code, but not structure.

**Stage 3 — Infrastructure**

Common components present and reliable: authentication, logging, monitoring, retry logic, health checks, shared utilities. The infrastructure phase answers: "Can other things reliably depend on this?"

Exit criterion: other components (features, external systems, tests) can depend on the infrastructure without special-casing. The infrastructure absorbs the generic cross-cutting concerns so features do not have to. The system is *dependable*.

What Infrastructure is NOT: features. The infrastructure/feature boundary is the most commonly violated SFIF boundary. Infrastructure enables; features use what infrastructure enables. Hardcoded database queries in a feature controller, or authentication logic scattered across handlers, signals infrastructure skipped — features built before the enabling layer was stable.

**Stage 4 — Features**

Specialized value built on the stable base: domain-specific logic, user-facing functionality, advanced capabilities. The features phase has no terminal exit criterion — it is ongoing work that continues as long as the project exists.

What Features require: a stable Foundation and Infrastructure. Features built before Foundation produces hardcoded-path spaghetti. Features built before Infrastructure produces auth logic copied across five handlers, retry logic reimplemented in every API call.

See [[Scaffold → Foundation → Infrastructure → Features]] for stage descriptions, exit criteria, and the full treatment of the recursive property.

### The Three Quality Tiers

**Skyscraper**

All SFIF stages complete and clean. Scaffold artifacts exist and are current (CLAUDE.md reflects the actual codebase). A single entry point manages everything. Infrastructure is stable and well-tested. Features build clearly on infrastructure. The system can grow upward without structural compromise — adding the next floor does not require rebuilding the base.

Skyscraper requires conditions, not just intent: a greenfield project, a full authorized refactor, or a system that can be decomposed and rebuilt layer-by-layer. Attempting Skyscraper design against a Mountain codebase without the conditions for refactor produces architecture documents that describe the desired state but do not match the actual system.

**Pyramid**

Functional and livable. Built around real constraints — a legacy database that cannot be migrated, a team that cannot pause delivery for a refactor, a third-party integration that forces an architectural compromise. Pyramid decisions are principled (the tradeoff is understood and documented) rather than random (the tradeoff is unknown or unacknowledged).

Pyramid is not failure. It is the practitioner's art: improving a Mountain without stopping delivery, working around immovable constraints, making the best structural decisions available within real limits. Most production engineering is Pyramid work.

**Mountain**

Accumulated mass with no structure. Spaghetti code, deprecated patterns layered on ad-hoc fixes, no scaffold artifacts (or scaffold that no longer describes the system), multiple competing entry points, authentication logic everywhere, no consistent error handling. The system works, but only people who built it understand why, and they are not fully sure either.

Mountain is the natural entropy state. It is not incompetence — it is what happens when stages get skipped: a POC deployed as production, features built before Infrastructure was stable, a growing system that never got its Foundation refactored. Mountain is reversible, but the reversal is expensive.

See [[Skyscraper, Pyramid, Mountain]] for the full quality tier analysis, the per-layer evaluation model, and the Mountain → Pyramid → Skyscraper improvement path.

### The Four SFIF Instances in the Ecosystem

| Project | Scaffold | Foundation | Infrastructure | Features Stage |
|---------|---------|-----------|---------------|---------------|
| Research Wiki | `CLAUDE.md`, `wiki/` structure, `config/schema.yaml`, tech stack | `tools/common.py`, schema validation, `manifest.json` | `pipeline.py` post-chain, MCP server (15 tools), lint, obsidian | evolve pipeline, watcher daemon, sync service, export |
| OpenFleet | `SOUL.md` + `HEARTBEAT.md` templates, monorepo layout, agent identity model | Deterministic orchestrator, agent base model, single entry point | `doctor.py` (24 governance rules), IRC routing, OpenClaw gateway | 10 specialized agents, Mission Control UI, Open Gateway |
| AICP | Profile system, `CLAUDE.md`, venv, tech stack choices | Backend router, circuit breaker, complexity scorer | MCP tools, guardrails pipeline (path protection, response filter) | Voice pipeline, 5-stage LocalAI roadmap, 78 skills |
| Front-Middleware-Backend | Per-layer: design system decisions, stack choices | Per-layer: component library, routing foundation | Per-layer: auth, state management, API contracts | Per-layer: specialized screens, flows, business logic |

The Research Wiki is the most structurally complete example: all four stages are populated and documented. OpenFleet is Infrastructure-complete and Features-active. AICP is Infrastructure-complete with Features ongoing. Front-Middleware-Backend is the example that most clearly illustrates the recursive property — each of the three layers independently traverses all four stages at its own pace.

### Auditing a System Against SFIF

The SFIF framework provides a concrete audit procedure for any system. The goal is not to assign a single grade but to identify which components are in which stage and whether anything is in the wrong stage.

**Scaffold audit**: Does `CLAUDE.md` (or equivalent) exist and match the actual system? Is there a README that accurately describes what the project does? Are the tech stack decisions documented? If a new person joined today, could they understand the project's intent from the scaffold artifacts alone? If the answer is no, the scaffold is either absent (Mountain) or stale (Mountain disguised as Skyscraper).

**Foundation audit**: Is there a single entry point? In Python: is there one `__main__` or one `pipeline.py` that everything flows through? In a web app: is there one router registration point? If there are five ways to start the application, the foundation is incomplete. Foundation completion is binary — either there is a single authoritative entry point or there is not.

**Infrastructure audit**: Can you add a new feature without touching shared concerns? If adding a new API endpoint requires modifying the auth system, the retry logic, or the logging configuration in that endpoint's code — rather than in a shared infrastructure layer — infrastructure is incomplete. Infrastructure is complete when adding a feature is pure feature code, with cross-cutting concerns handled transparently by the infrastructure layer.

**Feature audit**: Are features using infrastructure, or re-implementing it? Copied authentication logic across handlers, bespoke retry patterns in individual services, hardcoded configuration values in business logic — these are features that were built before or without infrastructure, and they now ARE infrastructure masquerading as features. These are the structural debt items that SFIF audits surface.

**Mountain indicators**: no scaffold artifacts, multiple entry points, auth/retry/logging in feature code, no schema or validation layer, tests (if any) against implementation details rather than behavior contracts.

**Pyramid indicators**: scaffold artifacts exist but are partially outdated, foundation is clear but has one or two competing entry points for legacy reasons, infrastructure handles 80% of cross-cutting concerns but has documented exceptions, features are mostly clean but have some embedded infrastructure.

**Skyscraper indicators**: scaffold is accurate and current, single entry point, all cross-cutting concerns handled at infrastructure layer, features contain only feature logic, tests verify behavior contracts.

### The Recursive Property in Practice

The recursive property is SFIF's most important and least obvious characteristic. At any scale:

- A *project* traverses Scaffold → Foundation → Infrastructure → Features
- Each *feature* within the project traverses Scaffold → Foundation → Infrastructure → Features at the feature level
- Each *component* within a feature traverses the same four stages at the component level
- The *design system* within a frontend independently traverses: design decisions documented (Scaffold) → component library established (Foundation) → responsive grid and state management (Infrastructure) → specialized screens and flows (Features)

This means structural quality can exist at one level and not at another. The wiki project is Skyscraper-tier at the system level (all four stages complete, clean interfaces) but individual pages within it can be Mountain-tier (orphaned, untested, poorly linked). The recursive property requires per-level audit, not a single system-level verdict.

### Relationship to the Knowledge Layer

The SFIF pattern has a direct analog in the wiki's 6-layer knowledge architecture. [[Progressive Distillation]] describes the same density-increasing, layer-by-layer structure applied to knowledge:

- Raw notes (Scaffold): direction captured, not yet structured
- Source synthesis (Foundation): single-source grounded understanding
- Concepts (Infrastructure): multi-source synthesis that other pages can depend on
- Lessons/Patterns/Decisions (Features): specialized value built on the stable conceptual base

A wiki page that skips Foundation (jumping from raw notes to a pattern) produces the knowledge equivalent of a Mountain: pattern-typed content that is actually a restatement of a single source, with no cross-linking, that cannot be reliably referenced by other pages. The SFIF exit criteria for knowledge work are: concept reachable from domain `_index.md` (joinable), has 2+ sources (operable), has 3+ relationships (dependable), has been validated and reviewed (features-ready).

## Open Questions

- The SFIF pattern is articulated but not yet operationalized as a tooling check — could `python3 -m tools.validate` detect "Infrastructure masquerading as Features" (e.g., auth logic in feature controllers) through static analysis of page relationships?
- At what point does a well-structured Pyramid become a Skyscraper? Is the boundary a discrete architectural decision (e.g., a refactor sprint) or a continuous improvement process?
- The four ecosystem instances show SFIF applied to Python tooling and AI agent systems. How does the pattern apply to data pipeline systems or ML model deployment, where the Foundation/Infrastructure boundary is less obvious?

## Relationships

- BUILDS ON: [[Scaffold → Foundation → Infrastructure → Features]]
- BUILDS ON: [[Skyscraper, Pyramid, Mountain]]
- RELATES TO: [[Model: Design.md and IaC]]
- RELATES TO: [[Model: Quality and Failure Prevention]]
- RELATES TO: [[Model: Knowledge Evolution]]
- RELATES TO: [[Four-Project Ecosystem]]
- FEEDS INTO: [[Model: Local AI ($0 Target)]]

## Backlinks

[[Scaffold → Foundation → Infrastructure → Features]]
[[Skyscraper]]
[[Pyramid]]
[[Mountain]]]]
[[Model: Design.md and IaC]]
[[Model: Quality and Failure Prevention]]
[[Model: Knowledge Evolution]]
[[Four-Project Ecosystem]]
[[Model: Local AI ($0 Target)]]
