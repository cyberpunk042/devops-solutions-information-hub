---
title: SDLC Customization Framework — Phases, Scale, and Chain Selection
aliases:
  - "SDLC Customization Framework — Phases, Scale, and Chain Selection"
type: concept
domain: cross-domain
status: synthesized
confidence: high
maturity: growing
created: 2026-04-12
updated: 2026-04-13
sources:
  - id: operator-sdlc-vision
    type: directive
    file: raw/notes/2026-04-12-mega-vision-directive.md
    description: Operator vision for SDLC customization — project phases, scale tiers, three chain types
  - id: methodology-model
    type: file
    file: wiki/config/methodology.yaml
    description: Current 9-model methodology system — foundation for SDLC customization
  - id: epam-adlc
    type: article
    url: https://www.epam.com/insights/ai/blogs/agentic-development-lifecycle-explained
    description: "EPAM: Agentic Development Lifecycle (ADLC) — new model for AI systems beyond traditional SDLC"
  - id: cmmi-levels
    type: article
    url: https://en.wikipedia.org/wiki/Capability_Maturity_Model_Integration
    description: "CMMI: 5 maturity levels — Initial, Managed, Defined, Quantitatively Managed, Optimizing"
  - id: lean-startup-bml
    type: article
    url: https://theleanstartup.com/principles
    description: Lean Startup Build-Measure-Learn cycle — validated learning, POC→MVP→production progression
  - id: pwc-agentic-sdlc
    type: article
    url: https://www.pwc.com/m1/en/publications/2026/docs/future-of-solutions-dev-and-delivery-in-the-rise-of-gen-ai.pdf
    description: "PwC 2026: Agentic SDLC in practice — autonomous software delivery"
tags: [sdlc, customization, framework, phases, scale, chain-selection, methodology, project-lifecycle, cmmi, lean-startup, agentic-sdlc]
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

### External Research: How Industry Handles Scale and Phase

> [!abstract] CMMI Maturity Levels — Process Rigor Scaling
>
> | CMMI Level | Name | Process State | Analogous Chain |
> |-----------|------|---------------|----------------|
> | 1 | Initial | Ad hoc, chaotic. Success depends on heroics. | No chain (chaos) |
> | 2 | Managed | Projects planned, performed, measured at project level. | Simplified |
> | 3 | Defined | Processes described rigorously, managed proactively with detailed measures. | Middle Ground |
> | 4 | Quantitatively Managed | Statistical process control, quantitative quality objectives. | Full |
> | 5 | Optimizing | Continuous improvement, built to pivot and respond. | Full + automation |
>
> CMMI validates our 3-chain model: there IS a recognized industry progression from ad-hoc (Level 1) through managed (Level 2) to defined (Level 3) to quantitative (Level 4). Our simplified/default/full maps to Levels 2/3/4. Level 1 is what happens without ANY chain. Level 5 is what the research wiki's constant evolution aspires to.

> [!abstract] Lean Startup: Build-Measure-Learn as Phase Progression
>
> The Lean Startup's Build-Measure-Learn cycle maps to our phase model:
> - **POC phase** = Build (create simplest possible version to test assumptions)
> - **MVP phase** = Measure (release to real users, gather feedback, validate demand)
> - **Production phase** = Learn + Scale (refine based on data, then grow)
>
> Key Lean principle: "Limit the scope of change as the product matures." This IS our phase progression — POC allows drastic changes, Production requires stability. The SDLC chain naturally tightens as the product matures.
>
> Distinction matters: POC is internal (feasibility test, not customer-facing). MVP is external (real users, real feedback). Production is committed (SLAs, compliance). Each transition changes what process is appropriate.

> [!abstract] Agentic SDLC (A-SDLC) — The AI Agent Dimension
>
> The industry is recognizing that AI agents require a DIFFERENT lifecycle model:
> - **EPAM's ADLC:** "Traditional SDLCs assume behavior is fully specified at build time. Agentic systems violate that assumption because they reason, adapt, and act across environments engineers do not fully control."
> - **PwC 2026:** "Agentic SDLC in practice — the rise of autonomous software delivery"
> - **GitHub Spec Kit (2025):** Placing specifications at the center of the engineering process
>
> This validates our approach: methodology models (stage-gated, artifact-producing) PLUS enforcement infrastructure (hooks, harness, immune system) PLUS the SDLC chain selection (how much process wraps the models). Traditional SDLC doesn't account for agents. Our framework does.
>
> The engineer of 2026 "will spend less time writing foundational code and more time orchestrating a dynamic portfolio of AI agents" — which is exactly why the Three PM Levels and harness version progression matter.

### How This Connects — Navigate From Here

> [!abstract] From SDLC Framework → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **What identity determines my chain?** | [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]] — 7 questions → chain selection |
> | **What enforcement matches each chain?** | Simplified → L1 advisory. Default → L2 hooks+commands. Full → L3 immune system+fleet. See [[three-pm-levels|Three PM Levels — Wiki to Fleet to Full Tool]] |
> | **How does readiness/progress work per chain?** | [[readiness-vs-progress|Readiness vs Progress — Two-Dimensional Work Tracking]] — both dimensions at every level, gates tighter on full chain |
> | **What global standards validate this?** | CMMI Levels 1-5 map to our chains. Lean Startup BML maps to our phases. See [[src-sdlc-frameworks-research|Synthesis — SDLC Frameworks Research — CMMI, Lean Startup, and Agentic SDLC]] |
> | **How does SFIF relate?** | [[model-sfif-architecture|Model — SFIF and Architecture]] — Skyscraper≈Full, Pyramid≈Default, Mountain≈Simplified. SFIF at product level: POC=Scaffold, MVP=Foundation, Staging=Infrastructure, Production=Features |
> | **What methodology models work per chain?** | [[model-methodology|Model — Methodology]] — all 9 models work in all chains, but chain determines artifact depth per model |
> | **Where is the backlog hierarchy?** | [[backlog-hierarchy-rules|Backlog Hierarchy Rules]] — Milestone→Epic→Module→Task. Full chain uses all 4 levels. Simplified may skip milestones+modules. |

## Open Questions

> [!question] Should chain selection be per-project or per-task? **PARTIALLY RESOLVED**
> Yes — per-task within a project default. A production project (Full chain default) doing a hotfix uses Hotfix model (2 stages, minimal process) — this IS simplified chain applied to one task. The methodology model already handles this. The project chain sets the DEFAULT; the model can override downward (never upward). Remaining: formalize the override rules in methodology.yaml.

> [!question] ~~How do chains map to the wiki's 4-tier adoption guide?~~
> **RESOLVED:** Parallel dimensions. Tiers = enforcement depth (read→configure→validate→enforce). Chains = process weight (simplified→default→full). Pairings: Simplified+Tier1-2, Default+Tier2-3, Full+Tier3-4. See [[methodology-adoption-guide|Methodology Adoption Guide]].

> [!question] What triggers a phase transition? **PARTIALLY RESOLVED**
> POC→MVP: hypothesis validated, first external user. MVP→Staging: product-market fit, first SLA. Staging→Production: compliance met, rollback tested. See [[src-sdlc-frameworks-research|Synthesis — SDLC Frameworks Research — CMMI, Lean Startup, and Agentic SDLC]]. Remaining: define measurable triggers specific to this ecosystem.

> [!question] ~~How does the research wiki itself select its chain?~~
> **RESOLVED:** Identity: type=system, domain=knowledge, phase=production, scale=medium (297 pages), pm_level=L1 → Chain: Default. Not Full (no sprint planning needed). Not Simplified (297 pages need real quality standards). See [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]].

## Relationships

- BUILDS ON: [[model-methodology|Model — Methodology]]
- BUILDS ON: [[methodology-framework|Methodology Framework]]
- RELATES TO: [[skyscraper-pyramid-mountain|Skyscraper, Pyramid, Mountain]]
- RELATES TO: [[methodology-adoption-guide|Methodology Adoption Guide]]
- RELATES TO: [[ecosystem-feedback-loop-wiki-as-source-of-truth|Ecosystem Feedback Loop — Wiki as Source of Truth]]
- FEEDS INTO: [[super-model|Super-Model — Research Wiki as Ecosystem Intelligence Hub]]

## Backlinks

[[model-methodology|Model — Methodology]]
[[methodology-framework|Methodology Framework]]
[[skyscraper-pyramid-mountain|Skyscraper, Pyramid, Mountain]]
[[methodology-adoption-guide|Methodology Adoption Guide]]
[[ecosystem-feedback-loop-wiki-as-source-of-truth|Ecosystem Feedback Loop — Wiki as Source of Truth]]
[[super-model|Super-Model — Research Wiki as Ecosystem Intelligence Hub]]
[[domain-chain-infrastructure|Artifact Chain — Infrastructure-IaC Domain]]
[[domain-chain-python-wiki|Artifact Chain — Python-Wiki Domain]]
[[domain-chain-typescript|Artifact Chain — TypeScript-Node Domain]]
[[when-to-use-milestone-vs-epic-vs-module-vs-task|Decision — When to Use Milestone vs Epic vs Module vs Task]]
[[goldilocks-flow|Goldilocks Flow — From Identity to Action]]
[[second-brain-integration-chain|Operations Plan — Second Brain Integration Chain — Complete Walkthrough]]
[[right-process-for-right-context-the-goldilocks-imperative|Principle — Right Process for Right Context — The Goldilocks Imperative]]
[[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]]
[[readiness-vs-progress|Readiness vs Progress — Two-Dimensional Work Tracking]]
[[sdlc-rules-and-structure-customizable-project-lifecycle|SDLC Rules and Structure — Customizable Project Lifecycle]]
[[src-sdlc-frameworks-research|Synthesis — SDLC Frameworks Research — CMMI, Lean Startup, and Agentic SDLC]]
[[three-pm-levels|Three PM Levels — Wiki to Fleet to Full Tool]]
[[wiki-gateway-tools-unified-knowledge-interface|Wiki Gateway Tools — Unified Knowledge Interface]]
