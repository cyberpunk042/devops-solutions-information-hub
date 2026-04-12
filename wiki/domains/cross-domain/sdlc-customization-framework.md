---
title: "SDLC Customization Framework — Phases, Scale, and Chain Selection"
type: concept
domain: cross-domain
status: synthesized
confidence: medium
maturity: seed
created: 2026-04-12
updated: 2026-04-12
sources:
  - id: operator-sdlc-vision
    type: directive
    file: raw/notes/2026-04-12-mega-vision-directive.md
    description: "Operator vision for SDLC customization — project phases, scale tiers, three chain types"
  - id: methodology-model
    type: file
    file: wiki/config/methodology.yaml
    description: "Current 9-model methodology system — foundation for SDLC customization"
tags: [sdlc, customization, framework, phases, scale, chain-selection, methodology, project-lifecycle]
---

# SDLC Customization Framework — Phases, Scale, and Chain Selection

## Summary

Projects don't all need the same SDLC rigor. A POC exploring an idea needs different process than a production system with 15M lines of code. The SDLC Customization Framework defines three dimensions of variation — project PHASE (POC→MVP→Staging→Production), codebase SCALE (10k→100k→1M→5M→15M), and methodology CHAIN (simplified, default, full) — that together determine how much process a project needs. The wiki's methodology system becomes customizable per these dimensions, with the middle-ground chain as default and explicit reasoning for when to simplify or expand.

## Key Insights

- **Project phase determines flexibility.** A project still in initial development (POC/MVP) has door wide open for refactors, major changes, short loops. A production system with paying users requires traceability, approval gates, rollback plans. The same methodology model applied at both phases produces either over-process (kills POC velocity) or under-process (production incidents).

- **Codebase scale determines rigor needs.** 10k lines: one person can hold it in their head. 100k: team needs conventions. 1M: needs automation. 5M: needs full SDLC with traceability. 15M: needs governance layers. The inflection points are not arbitrary — they correspond to cognitive and organizational capacity limits.

- **Three chains cover the spectrum.** Simplified (short loops, minimal documents, fast iteration), Middle Ground (stage-gated with selected artifacts, the default), Full (complete artifact chain, all stages, formal reviews, compliance documentation). Each chain is a complete methodology profile — not a degraded version of Full but a purpose-designed configuration.

- **Phase and scale are independent dimensions.** A POC at 10k lines and a production system at 10k lines need different process despite same scale. A 1M-line POC (rare but exists) needs scale rigor but phase flexibility. Both dimensions contribute independently.

## Deep Analysis

### Dimension 1: Project Phase

> [!abstract] Phase Progression and Process Impact
>
> | Phase | Characteristics | Loop Length | Documents Required | Flexibility |
> |-------|----------------|-----------|-------------------|-------------|
> | **POC** | Exploring feasibility. May be thrown away. | Hours-days | Near zero — notes only | Maximum — refactor anything, change architecture daily |
> | **MVP** | Proving value. First real users possible. | Days-weeks | Requirements + basic design | High — major changes OK but need lightweight rationale |
> | **Staging** | Preparing for production. Real integrations. | Weeks | Full requirements, design, test plan | Moderate — changes need approval, breaking changes need migration |
> | **Production** | Live users, SLAs, compliance. | Weeks-sprints | Full SDLC artifacts + compliance + operational runbooks | Low — changes gated, rollback plans required, traceability mandatory |

Phase transitions are one-directional in practice. A production system doesn't regress to POC flexibility (though sections of it might be isolated for experimentation).

### Dimension 2: Codebase Scale

> [!abstract] Scale Tiers and Process Needs
>
> | Scale | Lines | Team | What Breaks Without Process |
> |-------|-------|------|---------------------------|
> | **Micro** | <10k | 1 person | Nothing — one person holds full context |
> | **Small** | 10k-100k | 1-3 | Naming conventions, file organization, test habits |
> | **Medium** | 100k-1M | 3-10 | Ownership boundaries, CI/CD, code review, documentation |
> | **Large** | 1M-5M | 10-30 | Architecture governance, API contracts, dependency management, compliance |
> | **Massive** | 5M-15M+ | 30+ | Full SDLC governance, change management, multi-team orchestration, security layers |

Scale transitions happen gradually. The 100k→1M transition is typically where agent-driven development starts needing full methodology enforcement — this is where the wiki's current system is most valuable.

### Dimension 3: Three Methodology Chains

> [!info] Chain Comparison
>
> | Aspect | Simplified | Middle Ground (Default) | Full |
> |--------|-----------|----------------------|------|
> | **Stages** | 2-3 (document, implement, test) | 3-5 (depends on model) | 5 (all stages mandatory) |
> | **Artifacts per stage** | 1-2 (just the essentials) | 3-5 (core + important) | 5-10+ (every artifact type) |
> | **Review gates** | Self-review or peer | Stage-complete validation | Formal review + approval + compliance |
> | **Documentation** | Inline comments + README | Wiki pages + design docs | Full artifact chain + compliance docs + runbooks |
> | **Automation** | Manual + lint | Pipeline post + hooks | Full harness + immune system + orchestrator |
> | **When to use** | POC + micro/small scale | MVP→Staging + small→medium | Production + medium→massive |

> [!warning] The Middle Ground Is the Default — Not the Full Chain
>
> Most projects should start at the middle ground. Full chain is for production systems that have earned it through scale and complexity. Simplified is for exploration that accepts throwaway risk. Choosing Full for a POC is as wrong as choosing Simplified for production. The default exists because most work lives in the middle.

### How This Relates to Existing Methodology Models

The current methodology.yaml has 9 models (feature-development, research, bug-fix, etc.). These models define WHAT stages a task goes through. The SDLC chains define HOW MUCH process wraps around those stages.

A feature-development task in Simplified chain: document (brief) → implement → test (basic).
The same task in Full chain: document (requirements spec + infrastructure analysis + gap analysis) → design (design plan + decisions + tech spec) → scaffold (types + stubs) → implement (logic, wired into runtime) → test (full assertions + pipeline + review).

The models and chains are ORTHOGONAL dimensions. Every model × chain combination is valid.

### Interaction: Phase × Scale × Chain Selection

> [!abstract] Recommended Chain by Phase × Scale
>
> | | Micro (<10k) | Small (10k-100k) | Medium (100k-1M) | Large (1M-5M) | Massive (5M+) |
> |---|---|---|---|---|---|
> | **POC** | Simplified | Simplified | Simplified→Middle | Middle | Middle |
> | **MVP** | Simplified | Middle | Middle | Middle→Full | Full |
> | **Staging** | Middle | Middle | Middle→Full | Full | Full |
> | **Production** | Middle | Middle | Full | Full | Full |
>
> Transitions: use Simplified until it hurts, upgrade to Middle when agent violations or manual fixes become frequent, upgrade to Full when compliance, traceability, or team scale demand it.

## Open Questions

> [!question] Should chain selection be per-project or per-task?
> A production project doing a hotfix might use Simplified chain for that specific task while the project overall is Full chain. Can chains be task-scoped within a project-level default?

> [!question] How do chains map to the wiki's 4-tier adoption guide?
> Tier 1 (Read) ≈ awareness of chains. Tier 2 (Configure) ≈ select chain in methodology.yaml. Tier 3 (Validate) ≈ enforce chain rules. Tier 4 (Enforce) ≈ full harness with chain-aware validation. Are these the same dimension or orthogonal?

> [!question] What triggers a phase transition?
> Going from MVP to Staging: first paying customer? First SLA? First compliance requirement? The trigger should be explicit and measurable, not a feeling.

> [!question] How does the research wiki itself select its chain?
> The wiki is a knowledge system, not a product. It's "in production" (used daily) but at medium scale (~250 pages). Does it use Middle or Full?

## Relationships

- BUILDS ON: [[Model: Methodology]]
- BUILDS ON: [[Methodology Framework]]
- RELATES TO: [[Skyscraper, Pyramid, Mountain]]
- RELATES TO: [[Methodology Adoption Guide]]
- RELATES TO: [[Ecosystem Feedback Loop — Wiki as Source of Truth]]
- FEEDS INTO: [[Super-Model: Research Wiki as Ecosystem Intelligence Hub]]

## Backlinks

[[Model: Methodology]]
[[Methodology Framework]]
[[Skyscraper, Pyramid, Mountain]]
[[Methodology Adoption Guide]]
[[Ecosystem Feedback Loop — Wiki as Source of Truth]]
[[Super-Model: Research Wiki as Ecosystem Intelligence Hub]]
