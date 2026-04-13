---
title: Decision — Quality Tier Operational Decisions
aliases:
  - "Decision — Quality Tier Operational Decisions"
  - "Decision: Quality Tier Operational Decisions"
type: decision
domain: cross-domain
layer: 6
status: synthesized
confidence: medium
maturity: growing
derived_from:
  - "Skyscraper, Pyramid, Mountain"
  - "Methodology Framework"
reversibility: easy
created: 2026-04-10
updated: 2026-04-10
sources: []
tags: [quality-tiers, skyscraper, pyramid, mountain, leading-indicators, equilibrium, organizational, design-decisions]
---

# Decision — Quality Tier Operational Decisions
## Summary

Three open questions from Skyscraper, Pyramid, Mountain resolved by cross-referencing the Methodology Framework, Immune System Rules, and operational experience from the ecosystem. The questions are about detecting Pyramid→Mountain regression, whether Pyramid is a stable equilibrium, and applying the analogy to organizational architecture.

> [!success] Resolved decisions
>
> | Question | Decision | Confidence |
> |----------|----------|------------|
> | Leading indicators of Pyramid→Mountain regression | 4 measurable signals from the wiki's own tooling | High — observable today |
> | Is Pyramid a stable equilibrium? | Yes, IF maintenance investment is continuous. Neglect = decay. | High — matches maintenance economics |
> | Organizational architecture application | Yes — same 3 tiers apply to teams and processes | Medium — theoretical, needs instances |

## Decision

> [!warning] Four leading indicators that a Pyramid is sliding toward Mountain
>
> | Signal | How to Detect | Tool |
> |--------|--------------|------|
> | Increasing lint issues over time | Lint count trending up across `pipeline post` runs | `tools/lint.py` trend analysis |
> | Growing orphan pages | Pages created without relationships | `pipeline gaps` orphan count |
> | Stale pages accumulating | `updated` dates falling behind, no evolution activity | `pipeline evolve --review` |
> | Stage gates being skipped | Commits without stage names, tasks at 100% without all stages | Git log audit |
>
> These are observable TODAY using the wiki's own tooling. The lint-to-zero effort the 2026-04-12 session was itself a Mountain→Pyramid recovery operation — lint 103→1 is the metric.

**Pyramid IS a stable equilibrium — with continuous investment.** A Pyramid that receives regular maintenance (weekly `pipeline chain review`, periodic `evolve --score`, lint monitoring) remains Pyramid indefinitely. Decay happens when maintenance stops — not from some inherent instability. This matches the LLM Wiki Pattern's maintenance economics: "LLMs don't get bored." With automated maintenance (post-chain, watcher daemon, evolution pipeline), the cost of sustaining Pyramid is near-zero. Without automation, it requires human discipline — which historically fails.

**The analogy applies to organizations.** A Mountain organization has ad-hoc processes, undocumented decisions, tribal knowledge. A Pyramid organization has documented processes with known compromises. A Skyscraper organization has clean processes designed from principles. The same SFIF progression applies: scaffold the org structure, build the foundation (hiring, roles), add infrastructure (processes, tooling), then deliver features (products). The analogy extends naturally — but needs concrete organizational instances to validate beyond theory.

## Alternatives

### Alternative: Continuous quality scoring instead of discrete tiers

> [!warning] Rejected — tiers force a decision, scores enable avoidance
> A continuous quality score (0-100) lets teams say "we're at 67" without deciding what tier they're targeting. Three discrete tiers force a conscious choice: "we're building a Pyramid here, not a Skyscraper, and here's why." The value of the analogy is in the CHOICE, not the measurement.

## Rationale

The decisions make the quality tier analogy operational rather than theoretical. Leading indicators use existing tooling. Pyramid stability depends on automated maintenance (which this wiki has). Organizational application is a valid extension but needs validation.

## Reversibility

All easy. These are interpretive frameworks, not infrastructure commitments.

## Dependencies

- [[skyscraper-pyramid-mountain|Skyscraper, Pyramid, Mountain]] — resolves all 3 open questions
- [[methodology-framework|Methodology Framework]] — quality dimension is a framework parameter

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **What principle governs this?** | [[right-process-for-right-context-the-goldilocks-imperative|Principle — Right Process for Right Context — The Goldilocks Imperative]] |
> | **How does enforcement apply?** | [[infrastructure-over-instructions-for-process-enforcement|Principle — Infrastructure Over Instructions for Process Enforcement]] |
> | **What is my identity profile?** | [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]] |
> | **Where does this fit?** | [[methodology-system-map|Methodology System Map]] |

## Relationships

- DERIVED FROM: [[skyscraper-pyramid-mountain|Skyscraper, Pyramid, Mountain]]
- RELATES TO: [[methodology-framework|Methodology Framework]]
- RELATES TO: [[immune-system-rules|Immune System Rules]]
- RELATES TO: [[methodology-framework-design-decisions|Decision — Methodology Framework Design Decisions]]

## Backlinks

[[skyscraper-pyramid-mountain|Skyscraper, Pyramid, Mountain]]
[[methodology-framework|Methodology Framework]]
[[immune-system-rules|Immune System Rules]]
[[methodology-framework-design-decisions|Decision — Methodology Framework Design Decisions]]
