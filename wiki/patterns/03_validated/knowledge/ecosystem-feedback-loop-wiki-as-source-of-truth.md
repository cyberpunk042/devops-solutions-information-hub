---
title: Ecosystem Feedback Loop — Wiki as Source of Truth
aliases:
  - "Ecosystem Feedback Loop — Wiki as Source of Truth"
type: pattern
domain: cross-domain
layer: 5
status: synthesized
confidence: high
maturity: growing
derived_from:
  - "Four-Project Ecosystem"
  - "Model: Ecosystem Architecture"
  - "Super-Model: Research Wiki as Ecosystem Intelligence Hub"
instances:
  - {'page': 'Model: Methodology', 'context': 'Methodology models defined in wiki, exported to OpenArms/OpenFleet via domain profiles, bug findings feed back as lessons'}
  - {'page': 'Model: LLM Wiki', 'context': 'Wiki architecture is the reference implementation — other projects adopt schema, templates, quality gates'}
  - {'page': 'Methodology Adoption Guide', 'context': '4-tier adoption enables any project to consume from the wiki at appropriate depth'}
  - {'page': 'Model: Claude Code', 'context': 'Claude Code best practices synthesized from multiple projects, fed back as a single model consumed by all'}
created: 2026-04-12
updated: 2026-04-12
sources:
  - id: operator-vision
    type: directive
    file: raw/notes/2026-04-12-context-regather-directive.md
    description: "Operator directive: 'the brain will become the source of truth from which they feedback and will take the pieces and adapt them to each individual project'"
  - id: openarms-evidence
    type: observation
    file: raw/articles/openarms-methodology-scan.md
    description: OpenArms methodology.yaml derived from wiki's generic base + TypeScript domain profile — first consumer
  - id: greater-model-principle
    type: directive
    file: docs/SESSION-2026-04-12-handoff.md
    description: "Operator: 'never blinding ourself by their limiting models but always thinking of a greater model and a CONSTANT EVOLUTION'"
tags: [ecosystem, feedback-loop, source-of-truth, second-brain, constant-evolution, architecture-pattern]
---

# Ecosystem Feedback Loop — Wiki as Source of Truth

## Summary

A central knowledge wiki serves as the source of truth for methodology, standards, and operational knowledge across a multi-project ecosystem. Each project consumes what it needs (configs, templates, standards, directives) and feeds operational learnings back (bug findings, methodology evolution, tool discoveries). The wiki is always AHEAD of any individual project — it defines what's possible, not just what's currently implemented. Projects are instances; the wiki is the framework.

> [!info] Pattern Reference Card
>
> | Component | Role | Flow Direction |
> |-----------|------|---------------|
> | **Central Wiki** | Source of truth — defines methodology, standards, knowledge | Produces → all projects |
> | **Consumer Projects** | Adopt pieces, adapt to their domain, run production | Consumes ← wiki |
> | **Feedback Channel** | Operational learnings from production use | Produces → wiki |
> | **Evolution Engine** | Pipeline that integrates feedback into wiki knowledge | Internal to wiki |
> | **Export Profiles** | Domain-specific bundles for each consumer project | Wiki → project (filtered) |

## Pattern Description

> [!abstract] The Architecture
>
> ```
> Research Wiki (source of truth)
>   ├── exports: methodology configs, knowledge pages, templates, standards
>   ├── → OpenArms (TypeScript, autonomous agents)
>   │     └── feeds back: operational lessons, methodology bugs, compliance data
>   ├── → OpenFleet (fleet orchestration, MCP blocking)
>   │     └── feeds back: multi-agent patterns, coordination failures
>   ├── → AICP (Python, AI routing, complexity scoring)
>   │     └── feeds back: routing patterns, cost optimization lessons
>   ├── → devops-control-plane (TUI/CLI/Web, infrastructure)
>   │     └── feeds back: infrastructure patterns, operational failures
>   └── ingests: NEW sources (articles, papers, tools, frameworks)
>         └── each: ingest → learn → integrate → update layers → conclusions
> ```

The pattern has three properties that distinguish it from simple documentation:

**1. Bidirectional flow.** The wiki is not a read-only reference. Projects actively feed learnings BACK. When OpenArms discovers that agents skip stages 75% of the time during overnight runs, that evidence becomes a wiki lesson, which updates the methodology model, which updates the methodology.yaml, which ALL projects then consume.

**2. Framework over instance.** The wiki defines HOW TO DEFINE models, stages, artifact chains — not just the current set. When a project needs something the wiki doesn't have, the wiki's framework is extended (not the project's fork). The greater model principle: "never blinding ourselves by their limiting models but always thinking of a greater model."

**3. Constant evolution.** Every new source ingested (10-15 per session), every production incident, every operator directive drives learning that flows through ALL affected layers. The wiki is never "done" — it is a living system where each session leaves it better (more interconnected, more insightful, more useful), not just bigger.

> [!warning] The Anti-Pattern: Project Forks
>
> Without the feedback loop, each project independently invents its own methodology, standards, and patterns. Knowledge silos form. When one project discovers a critical failure mode, others don't learn from it. This is the state BEFORE the pattern — and it's what the operator is solving.

## Instances

> [!example]- OpenArms: First Full Consumer (Tier 4)
>
> **What it consumes:** methodology.yaml (9 models), artifact-types.yaml (17 types), TypeScript domain profile (pnpm gates, src/ paths, test patterns), CLAUDE.md structural patterns (8 patterns)
>
> **What it feeds back:** 24-artifact chain (the most evolved instance), 93 completed tasks (execution evidence), 14 enforcement scripts (what infrastructure works), 75% overnight violation rate (what doesn't work without full enforcement)
>
> **Adaptation:** methodology.yaml gains TypeScript-specific gate commands. Domain profile resolves generic artifact categories to concrete .ts/.tsx paths.

> [!example]- OpenFleet: Fleet Orchestration Consumer
>
> **What it consumes:** methodology models, MCP tool architecture, Claude Code configuration patterns
>
> **What it feeds back:** Multi-agent coordination patterns, MCP blocking for stage enforcement, 10-agent fleet operational lessons, 24 immune system rules from 16 post-mortems
>
> **Adaptation:** Fleet-specific methodology models, agent persona definitions, deterministic orchestrator patterns.

> [!example]- Research Wiki: Reference Implementation (Tier 4, self-hosting)
>
> **The wiki consumes from ITSELF:** methodology.yaml governs how wiki work is done. artifact-types.yaml defines the wiki's own page types. The wiki is simultaneously the framework AND an instance.
>
> **What it produces for others:** The complete config stack, templates, standards, lessons, patterns, decisions — everything.
>
> **Why self-hosting matters:** The wiki must follow its own methodology to have credibility. If it preaches stage-gated work but produces content in a single chaotic sprint, the methodology has no evidence base.

## When To Apply

> [!tip] Conditions for the Ecosystem Feedback Loop
>
> - **2+ projects** share enough domain overlap that knowledge transfers meaningfully
> - **One team or operator** owns the central knowledge base and can enforce quality
> - **Projects are active** — feedback requires ongoing production use, not abandoned repos
> - **The wiki has tooling** — ingest, validate, lint, evolve pipelines make the loop mechanical, not manual
> - **Evolution is valued** — the team sees the wiki as a growing asset, not a one-time deliverable

## When Not To

> [!warning] When This Pattern Fails
>
> - **Single project, no ecosystem** — the overhead of maintaining a central wiki exceeds the value. Just use CLAUDE.md + good practices.
> - **No feedback discipline** — if projects consume but never feed back, the wiki becomes stale documentation, not a living system. The loop breaks.
> - **Wiki quality is low** — if the wiki contains bad methodology, the feedback loop AMPLIFIES the bad methodology across all projects. Quality gates are mandatory.
> - **No operator** — the pattern requires someone who enforces quality, resolves contradictions between projects, and makes evolution decisions. Without an operator, the wiki drifts.

### How This Connects — Navigate From Here

> [!abstract] From This Pattern → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **What is the source of truth?** | [[super-model|Super-Model — Research Wiki as Ecosystem Intelligence Hub]] — v1.3 state, 264 pages, all models |
> | **How do projects adopt from the wiki?** | [[methodology-adoption-guide|Methodology Adoption Guide]] — 4 tiers, per-domain quick starts, SDLC chain selection |
> | **What does the feedback look like?** | This session: OpenArms fed back 22 distilled lessons → wiki captured 7+ new mechanisms. OpenFleet fed back immune system + tiers + contributions. |
> | **What PM level enables feedback?** | [[three-pm-levels|Three PM Levels — Wiki to Fleet to Full Tool]] — L1 (manual feedback), L2 (structured via fleet tools), L3 (automated via Plane sync) |
> | **How do gateway tools enable this?** | [[wiki-gateway-tools-unified-knowledge-interface|Wiki Gateway Tools — Unified Knowledge Interface]] — agents write back remarks, lessons, corrections via structured gateway |
> | **What is the Goldilocks for feedback?** | [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]] — POC projects read only. Production projects feed back actively. |

## Relationships

- DERIVED FROM: [[four-project-ecosystem|Four-Project Ecosystem]]
- DERIVED FROM: [[model-ecosystem|Model — Ecosystem Architecture]]
- BUILDS ON: [[super-model|Super-Model — Research Wiki as Ecosystem Intelligence Hub]]
- RELATES TO: [[methodology-adoption-guide|Methodology Adoption Guide]]
- RELATES TO: [[model-methodology|Model — Methodology]]
- RELATES TO: [[model-llm-wiki|Model — LLM Wiki]]
- RELATES TO: [[hardcoded-instances-fail-build-frameworks-not-solutions|Hardcoded Instances Fail — Build Frameworks Not Solutions]]
- FEEDS INTO: [[ai-methodology-consumption-guide|How AI Agents Consume the Methodology Wiki]]

## Backlinks

[[four-project-ecosystem|Four-Project Ecosystem]]
[[model-ecosystem|Model — Ecosystem Architecture]]
[[super-model|Super-Model — Research Wiki as Ecosystem Intelligence Hub]]
[[methodology-adoption-guide|Methodology Adoption Guide]]
[[model-methodology|Model — Methodology]]
[[model-llm-wiki|Model — LLM Wiki]]
[[hardcoded-instances-fail-build-frameworks-not-solutions|Hardcoded Instances Fail — Build Frameworks Not Solutions]]
[[ai-methodology-consumption-guide|How AI Agents Consume the Methodology Wiki]]
[[agent-failure-taxonomy-seven-classes-of-behavioral-failure|Agent Failure Taxonomy — Seven Classes of Behavioral Failure]]
[[contribution-gating-cross-agent-inputs-before-work|Contribution Gating — Cross-Agent Inputs Before Work]]
[[infrastructure-enforcement-proves-instructions-fail|Infrastructure Enforcement Proves Instructions Fail]]
[[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]]
[[identity-profile|Research Wiki — Identity Profile]]
[[sdlc-customization-framework|SDLC Customization Framework — Phases, Scale, and Chain Selection]]
[[src-openfleet-fleet-architecture|Synthesis — OpenFleet Fleet Architecture — Immune System, Dispatch, and Tiers]]
[[the-wiki-is-a-hub-not-a-silo|The Wiki Is a Hub, Not a Silo]]
[[three-lines-of-defense-immune-system-for-agent-quality|Three Lines of Defense — Immune System for Agent Quality]]
[[three-pm-levels|Three PM Levels — Wiki to Fleet to Full Tool]]
[[wiki-gateway-tools-unified-knowledge-interface|Wiki Gateway Tools — Unified Knowledge Interface]]
