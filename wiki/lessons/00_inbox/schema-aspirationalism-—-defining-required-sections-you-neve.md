---
title: "Schema aspirationalism — defining required sections you never validate produces false confidence"
type: lesson
domain: cross-domain
layer: 4
status: synthesized
confidence: medium
maturity: seed
derived_from:
  - "Systemic Incompleteness Is Invisible to Validation"
created: 2026-04-16
updated: 2026-04-16
sources:
  - id: openarms-schema
    type: observation
    project: openarms
    path: wiki/config/schema.yaml
    description: "Schema defines required_sections per type; no validator enforces them. 333 violations discovered via health check."
  - id: openarms-integration-feedback
    type: wiki
    file: raw/notes/2026-04-16-openarms-first-consumer-integration-feedback.md
tags: [contributed, inbox, schema, validation, aspirational, false-confidence]
contributed_by: "openarms-operator-claude"
contribution_source: "/home/jfortin/openarms"
contribution_date: 2026-04-16
contribution_status: accepted
---

# Schema aspirationalism — defining required sections you never validate produces false confidence

## Summary

A schema that defines `required_sections` per page type without any validator checking section structure creates false confidence. The schema LOOKS comprehensive — it passes code review, gets committed, references best practices. But no pipeline step enforces it. When the second brain's health check ran OpenArms's own schema against their own pages, 333 "blocking" violations appeared. These weren't quality failures — they were aspirational standards nobody validates. The schema was written when the wiki was scaffolded; the pages evolved differently. The gap was invisible until an external tool measured it.

## Context

This lesson applies when a project defines structural validation rules (required sections, minimum content thresholds, format specifications) without wiring them into the validation pipeline. The pattern is especially common during project scaffolding: the schema is written ambitiously at setup time, pages accumulate organically, and nobody notices the divergence because no automation checks it.

The lesson generalizes beyond wiki schemas to any configuration-as-specification pattern: API specs that don't generate validators, type definitions that don't generate runtime checks, test plans that don't generate test cases.

## Insight

**An aspirational schema is WORSE than no schema.** No schema = everyone knows there's no standard. Aspirational schema = everyone believes there IS a standard, but the standard is fiction. The false confidence prevents the gap from being noticed and addressed.

The deeper pattern: **validation coverage must match specification coverage.** Every field in the spec that says "required" must have a corresponding check in the pipeline that verifies it. If the pipeline only checks frontmatter fields but the schema defines required_sections, the pipeline validates 60% of the spec and silently ignores 40%. That 40% diverges.

This is the same structural gap as [[systemic-incompleteness-is-invisible-to-validation|Systemic Incompleteness Is Invisible to Validation]] applied to the schema itself: the schema is systemically incomplete (it defines rules the tooling can't check), and that incompleteness is invisible until an external measurement reveals it.

## Evidence

**OpenArms 2026-04-16:** `wiki/config/schema.yaml` defines `required_sections` for each page type:
- `lesson` requires: Summary, Context, Insight, Application, Relationships
- Actual OpenArms lessons use: Summary, Evidence, Root Cause, Relationships
- 333 pages fail their own required_sections rules

**OpenArms validation pipeline:** `scripts/methodology/validate-stage.cjs` checks:
- Frontmatter field presence and types ✓
- Stage validity and progression ✓
- Section structure — NOT CHECKED ✗

**The health check that revealed it:** `gateway health` using OpenArms's own schema (after the F2 fix) scored 0/100 on validation dimension — 333 blocking issues. Before the F2 fix, these looked like schema-mismatch artifacts. After the fix (using project's own schema), they're revealed as real violations of the project's own aspirational standards.

**Cost of the gap:** Zero immediate operational impact (pages work fine without matching the schema). But: every future integration attempt (schema convergence, lesson format bridge, standards adoption) must reconcile the aspirational schema with operational reality before proceeding. The schema is technical debt disguised as specification.

## Applicability

This lesson applies to three decisions:

1. **Schema authoring.** When defining a schema, only include rules you will validate. Every `required` field needs a corresponding pipeline check. If the check doesn't exist yet, mark the field as `recommended` not `required`.

2. **Integration planning.** When connecting to the second brain (or any external standard), check your OWN schema compliance first. Run `gateway health --verbose` against your own schema. The violations reveal where your operational reality diverges from your aspirational specification.

3. **Validation pipeline design.** Coverage of the validation pipeline must match coverage of the schema. If the schema has 20 rules and the validator checks 12, the remaining 8 are aspirational. Either build the missing 8 checks or remove the 8 unvalidated rules.

## Self-Check

> [!warning] Before committing any schema change, ask:
>
> 1. Does a validator CHECK every rule this schema DEFINES?
> 2. If I run the validator against existing pages, do they pass?
> 3. If they don't pass, is the schema wrong or are the pages wrong?
> 4. Am I adding a "required" rule that no automation enforces?

## Relationships

- EXTENDS: [[systemic-incompleteness-is-invisible-to-validation|Systemic Incompleteness Is Invisible to Validation]] — same gap at the schema level
- RELATES TO: [[model-llm-wiki|Model — LLM Wiki]] — wiki schema as the real product
- RELATES TO: [[infrastructure-over-instructions-for-process-enforcement|Principle — Infrastructure Over Instructions]] — an unenforced schema IS instruction, not infrastructure
- RELATES TO: [[model-quality-failure-prevention|Model — Quality and Failure Prevention]] — the three-layer defense requires all three layers
- RELATES TO: [[schema-is-the-real-product|Schema Is the Real Product]] — yes, but only if the schema is OPERATIONAL not aspirational

## Backlinks

[[systemic-incompleteness-is-invisible-to-validation|Systemic Incompleteness Is Invisible to Validation]]
[[model-llm-wiki|Model — LLM Wiki]]
[[Principle — Infrastructure Over Instructions]]
[[model-quality-failure-prevention|Model — Quality and Failure Prevention]]
[[Schema Is the Real Product]]
