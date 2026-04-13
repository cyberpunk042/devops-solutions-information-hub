---
title: "Synthesis: SDLC Frameworks Research — CMMI, Lean Startup, and Agentic SDLC"
type: source-synthesis
domain: cross-domain
status: synthesized
confidence: high
maturity: seed
created: 2026-04-12
updated: 2026-04-12
sources:
  - id: cmmi-wikipedia
    type: article
    url: "https://en.wikipedia.org/wiki/Capability_Maturity_Model_Integration"
    description: "CMMI 5 maturity levels — from ad hoc to optimizing"
  - id: epam-adlc
    type: article
    url: "https://www.epam.com/insights/ai/blogs/agentic-development-lifecycle-explained"
    description: "EPAM: Agentic Development Lifecycle (ADLC) as new model beyond SDLC"
  - id: lean-startup-principles
    type: article
    url: "https://theleanstartup.com/principles"
    description: "Lean Startup Build-Measure-Learn cycle"
  - id: pwc-agentic-sdlc
    type: article
    url: "https://www.pwc.com/m1/en/publications/2026/docs/future-of-solutions-dev-and-delivery-in-the-rise-of-gen-ai.pdf"
    description: "PwC 2026: Agentic SDLC in practice — autonomous delivery"
  - id: cio-agentic-2026
    type: article
    url: "https://www.cio.com/article/4134741/how-agentic-ai-will-reshape-engineering-workflows-in-2026.html"
    description: "CIO: How agentic AI reshapes engineering workflows in 2026"
  - id: geeksforgeeks-sdlc
    type: article
    url: "https://www.geeksforgeeks.org/software-engineering/sdlc-models-types-phases-use/"
    description: "GeeksforGeeks: Complete guide to SDLC models — when to use each"
  - id: neoteric-sdlc
    type: article
    url: "https://neoteric.eu/blog/software-development-life-cycle-sdlc"
    description: "Neoteric: SDLC stages with Lean POC→Prototype→MVP→Product progression"
  - id: lean-poc-mvp
    type: article
    url: "https://medium.com/@klappy/lean-expectations-poc-prototype-mvp-140749383fd4"
    description: "Chris Klapp: Lean Expectations — PoC, Prototype, MVP distinctions"
tags: [sdlc, cmmi, lean-startup, agentic-sdlc, research, maturity-model, project-phases, source-synthesis]
---

# Synthesis: SDLC Frameworks Research — CMMI, Lean Startup, and Agentic SDLC

## Summary

Online research across 8 sources reveals three converging perspectives that validate and extend the wiki's SDLC Customization Framework: CMMI's 5 maturity levels map to our 3 chains (simplified≈Level 2, default≈Level 3, full≈Level 4), the Lean Startup's Build-Measure-Learn cycle maps to our phase progression (POC=Build, MVP=Measure, Production=Learn+Scale), and the emerging Agentic SDLC (A-SDLC) validates that AI agents require different lifecycle models than traditional development — specifically infrastructure enforcement and stage-gated processes.

> [!info] Source Reference
>
> | Attribute | Value |
> |-----------|-------|
> | Source | 8 articles: CMMI (Wikipedia, TutorialsPoint), EPAM ADLC, PwC Agentic SDLC, Lean Startup, CIO, GfG, Neoteric, Medium |
> | Type | Online research synthesis |
> | Date | 2026-04-12 |
> | Key claim | Industry frameworks validate 3-chain model AND agentic AI requires process beyond traditional SDLC |

## Key Insights

1. **CMMI 5 levels map to our 3 chains.** Level 1 (Initial/ad hoc) = no chain. Level 2 (Managed/project-level) ≈ simplified chain. Level 3 (Defined/rigorous processes) ≈ middle-ground chain. Level 4 (Quantitatively Managed/statistical control) ≈ full chain. Level 5 (Optimizing/continuous improvement) = full + automation (the wiki's aspiration).

2. **CMMI maturity progression takes 12-18 months per level.** A first-time Level 3 appraisal requires documenting 18 process areas. This validates that chain upgrades are significant efforts — you don't jump from simplified to full in a sprint.

3. **Lean Startup's BML cycle IS our phase model.** POC = Build (simplest version to test assumptions). MVP = Measure (real users, real feedback). Production = Learn (refine based on data, then scale). The Lean principle "limit scope of change as product matures" IS the wiki's phase progression.

4. **POC is internal, MVP is external.** Critical distinction: POC tests feasibility (not customer-facing). MVP tests market demand (real users). Production commits to SLAs. Each transition changes what process is appropriate — this maps directly to our chain selection.

5. **Traditional SDLC assumes behavior is specified at build time.** EPAM's ADLC paper: "Agentic systems violate that assumption because they reason, adapt, and act across environments engineers do not fully control." This validates our infrastructure enforcement approach — you can't just specify agent behavior in a spec, you must enforce it at runtime.

6. **The engineer of 2026 orchestrates agents, not code.** CIO: Engineers will "spend less time writing foundational code and more time orchestrating a dynamic portfolio of AI agents." This validates our Three PM Levels — the human's role shifts from coding to orchestration, requiring different PM infrastructure.

7. **GitHub Spec Kit (2025) centers specifications.** Spec-driven development places specs at the center of engineering. This aligns with our readiness model — readiness = specification completeness, and it gates progress (you don't build until the spec is ready).

8. **AI code review quality jumped to 81%.** Qodo 2025 report: AI code reviews increased quality improvements to 81% (from 55%). This provides evidence for our immune system pattern — automated detection (Line 2) catches more issues with AI agents than without.

9. **SDLC model selection depends on 4 factors.** GeeksforGeeks: project size, complexity, budget, team structure. Our framework uses 3 of these (size=scale, complexity=phase, team=PM level) plus a 4th dimension (chain type) that subsumes budget considerations.

## Deep Analysis

### CMMI → Our Framework Mapping

> [!abstract] Detailed Level Mapping
>
> | CMMI Level | Process State | Our Chain | Our PM Level | What Changes |
> |-----------|---------------|-----------|-------------|-------------|
> | 1 Initial | Ad hoc, heroics | No chain | L0 (no wiki) | Nothing structured |
> | 2 Managed | Project-level planning | Simplified | L1 (Wiki LLM) | CLAUDE.md + backlog + basic methodology |
> | 3 Defined | Rigorous, proactive | Middle Ground | L1-L2 | Stage gates + hooks + validation |
> | 4 Quantitative | Statistical control | Full | L2-L3 | Immune system + metrics + fleet |
> | 5 Optimizing | Continuous improvement | Full + evolution | L3 | Automated evolution + constant learning |

### Lean Startup Phase Transition Triggers

> [!abstract] When to Transition
>
> | Transition | Lean Signal | Our Signal |
> |-----------|------------|-----------|
> | POC → MVP | Hypothesis validated, feasibility proven | Readiness ≥ threshold for core features, operator confirms |
> | MVP → Staging | Product-market fit signals, retention data | First paying user OR first SLA commitment |
> | Staging → Production | Stable metrics, operational readiness | Compliance requirements met, rollback plan tested |

### Agentic SDLC Implications

The Agentic SDLC literature validates two of our patterns:

1. **Infrastructure enforcement is necessary, not optional.** If agents "reason, adapt, and act across environments engineers do not fully control" (EPAM), then instructions are insufficient and infrastructure enforcement is the minimum viable quality architecture. Our [[Infrastructure Enforcement Proves Instructions Fail]] is independently validated.

2. **Agent orchestration is the new engineering.** If the engineer orchestrates agents rather than writing code, the PM infrastructure becomes the primary tool — not the IDE. Our Three PM Levels model (L1→L2→L3) maps to the transition from manual coding → agent-assisted → agent-orchestrated.

## Open Questions

> [!question] Does CMMI Level 5 map to anything we've built?
> Level 5 (Optimizing) = continuous improvement built into the process. Our evolution pipeline (evolve --score → scaffold → generate → validate) is the closest, but it's manual. Full Level 5 would require automated detection of improvement opportunities and automatic application.

> [!question] Should we adopt Lean Startup terminology alongside our own?
> Using "Build-Measure-Learn" as synonyms for our phases could help adoption by teams familiar with Lean. Risk: terminology overload. Benefit: instant recognition.

### How This Connects — Navigate From Here

> [!abstract] From This Source → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **What principles derive from this?** | Check FEEDS INTO relationships above |
> | **What is the Goldilocks framework?** | [[Project Self-Identification Protocol — The Goldilocks Framework]] |
> | **Where does this fit?** | [[Methodology System Map]] |

## Relationships

- FEEDS INTO: [[SDLC Customization Framework — Phases, Scale, and Chain Selection]]
- FEEDS INTO: [[Three PM Levels — Wiki to Fleet to Full Tool]]
- FEEDS INTO: [[Readiness vs Progress — Two-Dimensional Work Tracking]]
- RELATES TO: [[Model: Methodology]]
- RELATES TO: [[Methodology Adoption Guide]]
- RELATES TO: [[Infrastructure Enforcement Proves Instructions Fail]]

## Backlinks

[[SDLC Customization Framework — Phases, Scale, and Chain Selection]]
[[Three PM Levels — Wiki to Fleet to Full Tool]]
[[Readiness vs Progress — Two-Dimensional Work Tracking]]
[[Model: Methodology]]
[[Methodology Adoption Guide]]
[[Infrastructure Enforcement Proves Instructions Fail]]
