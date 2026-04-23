---
title: "Principle — Declarations Are Aspirational Until Infrastructure Verifies Them"
aliases:
  - "Principle — Declarations Are Aspirational Until Infrastructure Verifies Them"
  - "Principle: Declarations Are Aspirational Until Infrastructure Verifies Them"
  - "Declaration-Verification Principle"
type: principle
domain: cross-domain
layer: 5
status: synthesized
confidence: high
maturity: growing
derived_from:
  - "Aspirational Naming in Lifecycle Code"
  - "Schema aspirationalism — defining required sections you never validate produces false confidence"
  - "Mandatory Without Verification Is Not Enforced"
  - "Machine-Specific Config in VCS Is Aspirational Portability"
  - "Structural Compliance Is Not Operational Compliance"
  - "Aspirational Declaration Produces False Confidence at Every Layer"
created: 2026-04-16
updated: 2026-04-16
last_reviewed: 2026-04-22
sources:
  - id: aspirational-declaration-meta-pattern
    type: wiki
    file: wiki/patterns/01_drafts/aspirational-declaration-without-enforcement.md
    description: "The L5 meta-pattern with 5 validated cross-layer instances that promoted to this principle"
  - id: infrastructure-principle
    type: wiki
    file: wiki/lessons/04_principles/hypothesis/infrastructure-over-instructions-for-process-enforcement.md
    description: "The sibling principle this one generalizes from the process-enforcement layer to every declaration layer"
tags: [principle, declaration, verification, infrastructure, aspirational, cross-layer, validated, convergent]
---

# Principle — Declarations Are Aspirational Until Infrastructure Verifies Them

## Summary

Any declaration — a variable name, a schema field, a skill attribute, a config value, a README promise, a compliance tier — is ASPIRATIONAL until infrastructure exists at the gate that verifies the declaration holds. Without verification, consumers trust the declaration, the gap between declared meaning and actual behavior compounds silently, and the divergence surfaces catastrophically under stress. Five validated instances across five independent layers (variable, schema, skill-attribute, version-control config, compliance-measurement) demonstrate this is a structural law, not a coincidence. The principle generalizes [[infrastructure-over-instructions-for-process-enforcement|Infrastructure > Instructions]] from one layer (process-rule enforcement) to every layer where declaration meets consumer.

## Statement

> [!tip] The Principle
>
> **For every declaration element (name, field, attribute, config, claim, tier-measurement) that downstream code or humans will TRUST as enforced, infrastructure MUST exist at the gate that verifies the declaration holds.** Without the verification gate, the declaration is ASPIRATIONAL — it expresses intent but does not produce reality. The mechanism: consumers extend trust based on the declaration's semantic meaning; the gap between trust and reality is invisible until stress-tested; the failure mode is gradual then catastrophic. The fix is structural per instance (add the gate) and systemic per codebase (audit every declaration layer for unverified claims).

## Derived From

> [!abstract] Evidence Chain — 5 Cross-Layer Validated Instances
>
> | Layer | Instance | Declaration | Missing Gate | Manifestation |
> |---|---|---|---|---|
> | **Variable** | [[aspirational-naming-in-lifecycle-code\|Aspirational Naming in Lifecycle Code]] | `turnCount` variable name implies conversational turns | No validation that increment trigger matches the name's semantics | 3352 "turns" in a 10-turn session; thresholds fire 20-50× too early |
> | **Schema** | [[schema-aspirationalism-defining-required-sections-you-neve\|Schema Aspirationalism]] | `required_sections` in wiki-schema.yaml | No validator enforces section presence | 333 validation failures against the project's own schema, silent for months |
> | **Skill attribute** | [[mandatory-without-verification-is-not-enforced\|Mandatory Without Verification Is Not Enforced]] | `mandatory: true` on skills per Extension Standards | No gate reads `invoked-skills.log` before `/stage-complete` | ~60% skill-invocation compliance vs ~100% with gate |
> | **Version-control config** | [[machine-specific-config-in-vcs-is-aspirational-portability\|Machine-Specific Config in VCS Is Aspirational Portability]] | README says "clone on any machine" | No linter forbids absolute paths in tracked files | `.mcp.json` with `/home/jfortin/...` breaks on first machine transfer |
> | **Compliance measurement** | [[structural-compliance-is-not-operational-compliance\|Structural Compliance Is Not Operational Compliance]] | `gateway compliance` reports Tier 4 | Check verifies file presence, not implementation depth | OpenArms Tier 4 structural achieved in one session with Tier 2 operational depth |
>
> The meta-pattern: [[aspirational-declaration-without-enforcement|Aspirational Declaration Produces False Confidence at Every Layer]] — documents all five instances with the shared mechanism.

## Application

> [!abstract] Application by Context (Goldilocks)
>
> | Identity Profile | How to Apply This Principle |
> |-----------------|---------------------------|
> | **Solo agent, POC, L1** | Before committing a new declaration, ask: "what enforces this?" If nothing — either name it correctly (recommended, not required; advisory, not mandatory) OR drop it. Don't carry aspirational declarations into the POC. |
> | **Solo agent, MVP+, L2** | Systematic audit during restructuring: grep for terms that imply enforcement (`required`, `must`, `mandatory`, `required_sections`, `enforce`). For each, locate the gate. If missing, add or demote. Pair every declaration with its gate in one commit. |
> | **Harness, L2-L3** | Harness-owned gates verify schema declarations, skill invocations, artifact presence, stage boundaries, AND declaration-consistency itself. Meta-gate: "no declaration without a verification path." |
> | **Fleet, L3** | Full three-layer defense with declaration-verification coverage. Detection cycle (Line 2) explicitly checks that declarations hold; Correction (Line 3) actions include "restore declaration consistency." MCP-level blocks enforce at the protocol boundary. |
> | **Consumer integrating with a standard** | When adopting a standard, AUDIT the standard's declarations. Look for `required`, `mandatory`, `must`. Ask: "does the standard's tooling verify these, or am I expected to?" If unclear, the declaration is aspirational from the adopter's POV. |
> | **Any system that claims "X is verified/required/enforced" in docs** | The claim is an aspirational declaration. README promises, comment examples, standards pages — all are subject to this principle. Portability/compliance claims especially. |

> [!abstract] Adherence to Global Standards
>
> | Standard | How This Principle Aligns |
> |----------|-------------------------|
> | **Design by Contract (Meyer)** | DbC separates preconditions, postconditions, invariants. A declaration is a postcondition the consumer assumes. Without runtime assertion, DbC collapses to aspirational contracts. This principle extends DbC to every declaration layer, not just function preconditions. |
> | **Fail-fast / Defensive programming** | Both depend on checks at boundaries. A declaration without a check is NOT defensive — it is an invitation to trust a lie. This principle is the failure mode fail-fast was designed to prevent. |
> | **Consumer-driven contracts (CDC, Pact)** | Contracts between services fail silently if no pact test verifies them. Same pattern at service boundaries as this principle names at variable/config boundaries. |
> | **Semantic versioning** | SemVer declares compatibility in version numbers. Without automated compatibility testing, the declaration is aspirational. Pypi's "works with Python 3.8+" means nothing if no CI verifies 3.8. |
> | **SRP** | A declaration's job is to DECLARE. A gate's job is to VERIFY. Splitting declaration from verification is SRP; coupling them structurally is what this principle requires. |

## Boundaries

> [!warning] Where This Principle Does NOT Apply
>
> - **Pure documentation for human readers** — A README that describes what the project does (without implying enforcement) is descriptive, not aspirational. "This project is a knowledge wiki" is a description, not a declaration that needs a gate.
> - **Hypotheses under active exploration** — During research/POC, declarations are conjectural. The principle applies when the declaration becomes TRUSTED by consumers — not before.
> - **Over-verification costs exceed gap costs** — Not every declaration deserves a gate. A log-only variable named aspirationally costs nothing if thresholds aren't set on it. Judgment required.
> - **Declarations pointing at external verification** — "This passes the W3C validator" is not aspirational if the W3C validator IS the gate. The principle asks: is the gate real and in the path? Not: is the gate co-located.
> - **Compliance-checker design trade-offs** — A cheap structural check is better than no check. The fix is LABELING: name a check `structural-compliance` to prevent the structural check from being interpreted as operational guarantee. See the Compliance-Measurement instance.

## Governing Relationship to Infrastructure > Instructions

This principle generalizes [[infrastructure-over-instructions-for-process-enforcement|Infrastructure > Instructions]] from one layer to all layers. The original principle stated: "tool-call-level rules expressed as instructions get ~25% compliance; expressed as infrastructure gates, 100%." This principle extends: "ANY declaration that downstream code trusts as enforced, at any layer, is aspirational without an infrastructure gate."

The sibling relationship:

| Original | Generalized (this principle) |
|---|---|
| Layer: process rules (stage boundaries, tool restrictions) | Layer: every declaration layer |
| Trust source: instructions in CLAUDE.md | Trust source: any declaration element |
| Verification source: hooks, immune system | Verification source: any gate paired with the declaration |
| Quantified: 25% → 100% | Quantified (from instances): schema 0% validation of 333 pages; turnCount 20-50× inflation; compliance Tier 4 structural ≠ operational |

The two principles form a family: Infrastructure > Instructions is the SEED; this is the generalization with five validated layer instances.

## How This Connects — Navigate From Here

> [!abstract] From This Principle → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **The meta-pattern this promotes from** | [[aspirational-declaration-without-enforcement\|Aspirational Declaration Produces False Confidence at Every Layer]] (L5 meta-pattern with all 5 instances) |
> | **The sibling principle it generalizes** | [[infrastructure-over-instructions-for-process-enforcement\|Infrastructure Over Instructions]] |
> | **Variable-layer instance** | [[aspirational-naming-in-lifecycle-code\|Aspirational Naming]] |
> | **Schema-layer instance** | [[schema-aspirationalism-defining-required-sections-you-neve\|Schema Aspirationalism]] |
> | **Skill-attribute-layer instance** | [[mandatory-without-verification-is-not-enforced\|Mandatory Without Verification]] |
> | **VCS-layer instance** | [[machine-specific-config-in-vcs-is-aspirational-portability\|Machine-Specific Config in VCS]] |
> | **Compliance-measurement-layer instance** | [[structural-compliance-is-not-operational-compliance\|Structural Compliance Is Not Operational Compliance]] |
> | **How to apply by profile** | [[project-self-identification-protocol\|Project Self-Identification Protocol]] |
> | **The adoption guide** | [[methodology-adoption-guide\|Methodology Adoption Guide]] |

## Relationships

- DERIVED FROM: [[aspirational-naming-in-lifecycle-code|Aspirational Naming in Lifecycle Code]]
- DERIVED FROM: [[schema-aspirationalism-defining-required-sections-you-neve|Schema Aspirationalism]]
- DERIVED FROM: [[mandatory-without-verification-is-not-enforced|Mandatory Without Verification Is Not Enforced]]
- DERIVED FROM: [[machine-specific-config-in-vcs-is-aspirational-portability|Machine-Specific Config in VCS Is Aspirational Portability]]
- DERIVED FROM: [[structural-compliance-is-not-operational-compliance|Structural Compliance Is Not Operational Compliance]]
- BUILDS ON: [[aspirational-declaration-without-enforcement|Aspirational Declaration Produces False Confidence at Every Layer]]
- GENERALIZES: [[infrastructure-over-instructions-for-process-enforcement|Principle — Infrastructure Over Instructions for Process Enforcement]]
- RELATES TO: [[structured-context-governs-agent-behavior-more-than-content|Principle — Structured Context Governs Agent Behavior More Than Content]]
- RELATES TO: [[right-process-for-right-context-the-goldilocks-imperative|Principle — Right Process for Right Context]]
- FEEDS INTO: [[super-model|Super-Model — Research Wiki as Ecosystem Intelligence Hub]]
- FEEDS INTO: [[methodology-adoption-guide|Methodology Adoption Guide]]

## Backlinks

[[aspirational-naming-in-lifecycle-code|Aspirational Naming in Lifecycle Code]]
[[Schema Aspirationalism]]
[[mandatory-without-verification-is-not-enforced|Mandatory Without Verification Is Not Enforced]]
[[Machine-Specific Config in VCS Is Aspirational Portability]]
[[structural-compliance-is-not-operational-compliance|Structural Compliance Is Not Operational Compliance]]
[[aspirational-declaration-without-enforcement|Aspirational Declaration Produces False Confidence at Every Layer]]
[[infrastructure-over-instructions-for-process-enforcement|Principle — Infrastructure Over Instructions for Process Enforcement]]
[[structured-context-governs-agent-behavior-more-than-content|Principle — Structured Context Governs Agent Behavior More Than Content]]
[[Principle — Right Process for Right Context]]
[[super-model|Super-Model — Research Wiki as Ecosystem Intelligence Hub]]
[[methodology-adoption-guide|Methodology Adoption Guide]]
[[src-airllm-layer-wise-inference-nvme-ssd-offload|Synthesis — AirLLM: Layer-Wise Inference with NVMe SSD Offload]]
[[2026-04-22-last-reviewed-frontmatter-field-evolve-mark-reviewed-cli|last_reviewed frontmatter field + evolve mark-reviewed CLI]]
