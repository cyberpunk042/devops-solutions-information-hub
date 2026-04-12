---
title: "Coverage Blindness — Modeling Only What You Know"
type: lesson
domain: cross-domain
layer: 4
status: synthesized
confidence: high
maturity: growing
derived_from:
  - "Methodology Artifact Taxonomy"
  - "Synthesis: Methodology Artifact Taxonomy — Full Spectrum Research"
  - "Methodology Standards Initiative — Honest Assessment"
created: 2026-04-12
updated: 2026-04-12
sources: []
tags: [methodology, coverage, blindness, taxonomy, lesson, gap]
---

# Coverage Blindness — Modeling Only What You Know

## Summary

Systems that model their own artifacts tend to cover only the artifacts they already produce — creating a self-reinforcing blind spot where the system appears complete because it validates 100% of what it measures, while measuring only 20% of what exists. The research wiki defined 17 page types and validated all of them, achieving "0 validation errors" — while the real-world SDLC has 78+ artifact types across 11 categories. The wiki was 100% compliant with 20% of the problem space.

## Context

This lesson applies when:
- Building a methodology or quality system from scratch without external research
- A system reports "0 errors" or "100% compliance" — check what it's NOT measuring
- Defining artifact types based on what a project currently produces rather than what it SHOULD produce
- An agent claims the type system is "complete" without comparing to external taxonomies

## Insight

> [!warning] 100% of 20% = Invisible Incompleteness
>
> The coverage blindness pattern:
> 1. Build a system to validate your artifacts
> 2. Define the artifact types based on what you currently produce
> 3. Validate all your artifacts → 100% pass rate
> 4. Conclude the system is complete
> 5. Never discover the 80% of artifact types you don't produce
>
> The system can't detect what it doesn't define. A wiki that defines 17 page types and validates all 17 reports "0 errors" — but it has no requirements spec type, no infrastructure analysis type, no ADR type, no test plan type, no operations guide type, no compliance report type. These artifacts either don't exist (gap) or exist misclassified as generic "concept" pages (wrong quality bar).

> [!abstract] The Coverage Gap by Category
>
> | Category | Real-World Types | Our Coverage | What We Missed |
> |----------|-----------------|-------------|---------------|
> | Initiation | 7 | 0% | Project charters, business cases, feasibility studies |
> | Planning | 8 | 12% | WBS, risk analysis, procurement, roles matrix |
> | Requirements | 7 | 14% | BRD, FRD, SRS, use cases, RTM |
> | Design | 10 | 20% | Tech specs, interface specs, config specs, HLD/LLD |
> | Construction | 7 | N/A | Code artifacts — not wiki pages |
> | Testing | 8 | N/A | Test artifacts — not wiki pages |
> | Deployment | 7 | 14% | Operations guides, runbooks, release notes |
> | Closure | 5 | 40% | Post-project reviews, knowledge transfer reports |
> | Monitoring | 5 | 0% | Change logs, risk registers, compliance reports |
> | Knowledge | 8 | 100% | (fully covered) |
> | AI Agent | 6 | 0% | Personas, skills, hooks, compliance |

## Evidence

> [!bug]- Failure: "Complete" Type System at 20% Coverage
> The wiki's artifact-types.yaml defined 17 page types with content thresholds, styling directives, and verification methods. Pipeline post validated all of them. The system reported "0 validation errors" across 220 pages. The operator looked at the result and said: "I see nothing about everything I told you... just flim traces... clearly there is a massive gap." The 0-error report was accurate — AND the system was only covering 20% of the artifact space.

> [!success] Recovery: Online Research Revealed the Full Spectrum
> A single online research session (sdlcforms.com, nxcode.io agentic engineering, ADR GitHub, Wikipedia artifacts, Zettelkasten) revealed 78+ artifact types across 11 categories. The knowledge layer (our strength) was 100% covered. EVERYTHING ELSE was 0-40%. This could only be discovered by looking OUTSIDE the system at what the real world produces.

> [!success] Evidence from OpenArms
> OpenArms's methodology-document-chain.md defines 24 artifacts for Feature Development alone — and the operator called it "a first draft, a 20% subset." Even the most evolved instance in the ecosystem acknowledges its own incompleteness. The cure is external research, not internal analysis.

## Applicability

| Domain | How This Lesson Applies |
|--------|----------------------|
| **Any validation system** | Check what you're NOT measuring. "0 errors" means nothing if your error definitions cover 20% of reality. |
| **Methodology design** | Compare your artifact types against industry taxonomies (SDLC, Agile, DevOps, AI Agent) before declaring completeness. |
| **Quality gates** | Gates can only check what they're configured to check. If the gate doesn't know about infrastructure analysis documents, it can't verify they exist. |
| **AI agent systems** | Agents optimize for what's measured. If compliance only checks stage boundary violations, agents comply on boundaries but skip artifact production entirely. |

> [!tip] When This Lesson Does NOT Apply
>
> Small projects or spikes that intentionally use a subset of artifacts (Pyramid tier). The lesson is about UNINTENTIONAL incompleteness — not knowing what you're missing. Intentional compression with documented reasoning (Pyramid) is a valid choice. The problem is when the system BELIEVES it's complete because it can't see what it doesn't define.

## Self-Check — Am I About to Make This Mistake?

> [!warning] Ask yourself BEFORE declaring a type system, taxonomy, or coverage report "complete":
>
> 1. **Did I research OUTSIDE my own system?** If my artifact types are based only on what I currently produce, I'm blind to what I don't produce.
> 2. **Am I reporting "0 errors" on a narrow scope?** What am I NOT checking? What types am I NOT validating?
> 3. **Would an external taxonomy (SDLC, Agile, IEEE) have types I don't?** If yes, my system is incomplete — even if it passes its own tests.
> 4. **Am I at 100% of 20%?** Full validation of a partial scope creates false confidence. Check the denominator.

## Relationships

- DERIVED FROM: [[Methodology Artifact Taxonomy]]
- DERIVED FROM: [[Synthesis: Methodology Artifact Taxonomy — Full Spectrum Research]]
- DERIVED FROM: [[Methodology Standards Initiative — Honest Assessment]]
- RELATES TO: [[Systemic Incompleteness Is Invisible to Validation]]
- RELATES TO: [[Model: Quality and Failure Prevention]]
- FEEDS INTO: [[Methodology Standards — What Good Execution Looks Like]]

## Backlinks

[[Methodology Artifact Taxonomy]]
[[Synthesis: Methodology Artifact Taxonomy — Full Spectrum Research]]
[[Methodology Standards Initiative — Honest Assessment]]
[[Systemic Incompleteness Is Invisible to Validation]]
[[Model: Quality and Failure Prevention]]
[[Methodology Standards — What Good Execution Looks Like]]
[[Methodology Config Architecture — How the Pieces Fit Together]]
