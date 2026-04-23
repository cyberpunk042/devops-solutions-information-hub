---
title: Principle — Right Process for Right Context — The Goldilocks Imperative
aliases:
  - "Principle — Right Process for Right Context — The Goldilocks Imperative"
  - "Principle: Right Process for Right Context — The Goldilocks Imperative"
type: principle
domain: cross-domain
layer: 5
status: synthesized
confidence: high
maturity: growing
derived_from:
  - "Enforcement Must Be Mindful — Hard Blocks Need Justified Bypass"
  - "Hardcoded Instances Fail — Build Frameworks Not Solutions"
  - "Follow the Method of Work Not the Methodology Label"
  - "New Content Must Integrate Into Existing Pages"
  - "Models Are Built in Layers, Not All at Once"
created: 2026-04-12
updated: 2026-04-13
last_reviewed: 2026-04-22
sources:
  - id: operator-goldilocks
    type: directive
    file: raw/notes/2026-04-12-goldilocks-higher-ground-directive.md
    description: "Operator: Goldilocks = optimal, not extreme. AM I a system? A harness? A solo session?"
  - id: cmmi-levels
    type: article
    url: https://en.wikipedia.org/wiki/Capability_Maturity_Model_Integration
    description: "CMMI: 5 maturity levels — each level is appropriate for its context, not universally better"
  - id: lean-startup
    type: article
    url: https://theleanstartup.com/principles
    description: "Lean Startup: limit scope of change as product matures — process rigor follows maturity"
tags: [principle, goldilocks, adaptation, context-aware, right-process, scalability]
---

# Principle — Right Process for Right Context — The Goldilocks Imperative
## Summary

Process must adapt to context. Too much process kills POC velocity. Too little process kills production quality. The "right" amount is a FUNCTION of identity (what am I?), phase (POC→Production), scale (10k→15M), PM level (L1→L3), and trust tier (trainee→expert). Hardcoding one process level for all situations is the same failure as hardcoding one artifact chain for all domains — it produces instances that don't transfer.

## Statement

> [!tip] The Principle
>
> **Every process decision (SDLC profile, enforcement level, methodology model, artifact depth, tracking granularity) MUST be parameterized by the consumer's identity profile, not fixed to one configuration.** The mechanism: process that is too heavy for the context creates friction that agents and humans route around (defeating the process). Process that is too light creates gaps that compound into failures (defeating quality). The Goldilocks point shifts as the project matures — what was right for POC is wrong for Production, and vice versa. The framework must ADAPT, and adaptation requires the consumer to DECLARE its context.

## Derived From

> [!abstract] Evidence Chain — 5 Converging Lessons
>
> | Lesson | What It Contributes |
> |--------|-------------------|
> | [[enforcement-must-be-mindful-hard-blocks-need-justified-bypass|Enforcement Must Be Mindful — Hard Blocks Need Justified Bypass]] | **Over-process creates its own failures.** OpenArms T086: correct work blocked by enforcement. T085: polyfilled 4 layers because no escalation mechanism. Both are process-context mismatches — the process assumed one context but the actual context was different. |
> | [[hardcoded-instances-fail-build-frameworks-not-solutions|Hardcoded Instances Fail — Build Frameworks Not Solutions]] | **Hardcoded process = hardcoded instance.** A methodology.yaml with fixed values for one project doesn't transfer. A FRAMEWORK that selects values based on identity profile does. Phase 1 failure (37 files of "crap") was hardcoded process applied to a framework problem. |
> | [[follow-the-method-of-work-not-the-methodology-label|Follow the Method of Work Not the Methodology Label]] | **"Follow the methodology" means different things to different contexts.** Operator meant "work systematically." Agent meant "enter Document stage." The label is the same; the appropriate METHOD differs by context. An explicit method of work per context prevents the loop. |
> | [[new-content-must-integrate-into-existing-pages|New Content Must Integrate Into Existing Pages]] | **Integration requires context awareness.** 37 pages created in isolation because the process didn't account for the context (existing high-traffic pages that needed updating). The right process for NEW pages is: update entry points first, create standalone pages second. |
> | [[models-are-built-in-layers-not-all-at-once|Models Are Built in Layers, Not All at Once]] | **Process depth follows maturity.** SFIF at the methodology level: scaffold (CLAUDE.md rules) → foundation (hooks) → infrastructure (harness) → features (immune system). Attempting full process at scaffold stage produces false readiness claims. |

## Application

> [!abstract] The Goldilocks Selection
>
> | Context | Too Little | Just Right | Too Much |
> |---------|-----------|-----------|----------|
> | **POC, micro, solo** | No rules at all | Simplified chain, CLAUDE.md advisory, 2-3 stages | Full chain + hooks + harness = kills exploration |
> | **MVP, small-medium, solo** | CLAUDE.md only (25% compliance) | Default chain, hooks + commands, 3-5 stages | Immune system + fleet = overkill for 1 agent |
> | **Staging, medium, L2** | Default chain without validation | Default→Full chain, hooks + harness + validation | Full fleet with 10-agent orchestrator |
> | **Production, large+, L3** | Default chain (insufficient traceability) | Full chain, immune system, contributions, sprints | N/A — at this scale, full IS just right |
> | **Sub-agents, any** | No rules (33% compliance) | Trustless verification (accept, then check output) | Hook injection (high cost, low ROI) |
> | **Research/spike, any** | No stages | 2-stage model (document→design), 50% readiness cap | Full 5-stage feature-dev = over-process |

> [!abstract] How CMMI and Lean Startup Validate This
>
> | External Framework | What It Says | How It Maps |
> |-------------------|-------------|------------|
> | **CMMI Level 1→5** | Each level is appropriate for its organizational maturity. Level 3 isn't "better" than Level 2 — it's appropriate for organizations that NEED it. | Our chains (simplified/default/full) map to CMMI Levels 2/3/4. Adopting Level 4 process at Level 1 maturity = chaos. |
> | **Lean Startup BML** | "Limit the scope of change as the product matures." POC allows drastic changes; Production requires stability. | Phase progression (POC→Production) naturally tightens process. The framework doesn't force it — it FOLLOWS maturity. |
> | **Agentic SDLC (2026)** | Traditional SDLC assumes behavior specified at build time. Agents violate that. | Our framework adds enforcement infrastructure (hooks, harness, immune system) that traditional SDLC doesn't need — because traditional SDLC doesn't have agents. |

## Boundaries

> [!warning] Where This Principle Does NOT Apply
>
> - **Invariants are NOT Goldilocks.** Stage boundaries are hard. 99→100 is human-only. Readiness is computed, never manual. These rules apply at EVERY identity profile. The Goldilocks principle applies to DEGREE of process, not EXISTENCE of process.
> - **Compliance requirements are non-negotiable.** If a project has regulatory compliance (SOC2, HIPAA, ISO), the chain must be Full regardless of scale or phase. External requirements override Goldilocks.
> - **Trust must be earned, not declared.** A project claiming "expert tier" to get less process oversight is gaming the framework. OpenFleet solves this with data-driven tiers. The second brain should verify claims against evidence.
> - **Downward adaptation requires justification.** Moving from Full to Default chain (simplifying) is a DECISION page, not a silent change. Document why, what risks are accepted, who approved.

## How This Connects — Navigate From Here

> [!abstract] From This Principle → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **The identity protocol that makes this work** | [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]] — 7 questions → profile selection |
> | **The SDLC profiles to choose from** | [[sdlc-customization-framework|SDLC Customization Framework — Phases, Scale, and Profile Selection]] — simplified/default/full with CMMI mapping |
> | **The PM infrastructure levels** | [[three-pm-levels|Three PM Levels — Wiki to Fleet to Full Tool]] — L1→L2→L3, harness v1→v3 |
> | **The tracking that adapts per context** | [[readiness-vs-progress|Readiness vs Progress — Two-Dimensional Work Tracking]] — gate threshold adapts per identity |
> | **The enforcement that adapts** | [[infrastructure-over-instructions-for-process-enforcement|Principle — Infrastructure Over Instructions for Process Enforcement]] — enforcement level follows PM level |
> | **The structure that adapts** | [[structured-context-governs-agent-behavior-more-than-content|Principle — Structured Context Governs Agent Behavior More Than Content]] — same structure, different depth per tier |
> | **The methodology that provides the models** | [[model-methodology|Model — Methodology]] — 9 models, each appropriate for different task types |
> | **The adoption guide that walks you through** | [[methodology-adoption-guide|Methodology Adoption Guide]] — progressive adoption from Tier 1 to Tier 4 |

## Relationships

- DERIVED FROM: [[enforcement-must-be-mindful-hard-blocks-need-justified-bypass|Enforcement Must Be Mindful — Hard Blocks Need Justified Bypass]]
- DERIVED FROM: [[hardcoded-instances-fail-build-frameworks-not-solutions|Hardcoded Instances Fail — Build Frameworks Not Solutions]]
- DERIVED FROM: [[follow-the-method-of-work-not-the-methodology-label|Follow the Method of Work Not the Methodology Label]]
- DERIVED FROM: [[new-content-must-integrate-into-existing-pages|New Content Must Integrate Into Existing Pages]]
- DERIVED FROM: [[models-are-built-in-layers-not-all-at-once|Models Are Built in Layers, Not All at Once]]
- BUILDS ON: [[sdlc-customization-framework|SDLC Customization Framework — Phases, Scale, and Profile Selection]]
- BUILDS ON: [[three-pm-levels|Three PM Levels — Wiki to Fleet to Full Tool]]
- RELATES TO: [[infrastructure-over-instructions-for-process-enforcement|Principle — Infrastructure Over Instructions for Process Enforcement]]
- RELATES TO: [[structured-context-governs-agent-behavior-more-than-content|Principle — Structured Context Governs Agent Behavior More Than Content]]
- FEEDS INTO: [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]]
- FEEDS INTO: [[methodology-adoption-guide|Methodology Adoption Guide]]
- FEEDS INTO: [[super-model|Super-Model — Research Wiki as Ecosystem Intelligence Hub]]

## Backlinks

[[enforcement-must-be-mindful-hard-blocks-need-justified-bypass|Enforcement Must Be Mindful — Hard Blocks Need Justified Bypass]]
[[hardcoded-instances-fail-build-frameworks-not-solutions|Hardcoded Instances Fail — Build Frameworks Not Solutions]]
[[follow-the-method-of-work-not-the-methodology-label|Follow the Method of Work Not the Methodology Label]]
[[new-content-must-integrate-into-existing-pages|New Content Must Integrate Into Existing Pages]]
[[models-are-built-in-layers-not-all-at-once|Models Are Built in Layers, Not All at Once]]
[[sdlc-customization-framework|SDLC Customization Framework — Phases, Scale, and Profile Selection]]
[[three-pm-levels|Three PM Levels — Wiki to Fleet to Full Tool]]
[[infrastructure-over-instructions-for-process-enforcement|Principle — Infrastructure Over Instructions for Process Enforcement]]
[[structured-context-governs-agent-behavior-more-than-content|Principle — Structured Context Governs Agent Behavior More Than Content]]
[[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]]
[[methodology-adoption-guide|Methodology Adoption Guide]]
[[super-model|Super-Model — Research Wiki as Ecosystem Intelligence Hub]]
[[e014-goldilocks-navigable-system-identity-to-action-in-continuous-flow|E014 — Goldilocks Navigable System — Identity to Action in Continuous Flow]]
[[e022-context-aware-gateway-orientation-and-routing|E022 — Context-Aware Gateway Orientation and Task Routing]]
[[execution-mode-is-consumer-property-not-project-property|Execution Mode Is a Consumer Property, Not a Project Property — Guard Against Conflation Drift]]
[[src-bmad-method-agile-ai-development-framework|Synthesis: BMAD-METHOD — Agile AI-Driven Development Framework]]
