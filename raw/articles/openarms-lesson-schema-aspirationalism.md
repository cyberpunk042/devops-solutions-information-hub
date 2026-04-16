---
title: "Schema aspirationalism — defining required sections you never validate produces false confidence"
type: lesson
domain: cross-domain
layer: 4
status: synthesized
confidence: medium
maturity: seed
derived_from: []
created: 2026-04-16
updated: 2026-04-16
sources: []
tags: [contributed, inbox]
contributed_by: "openarms-operator-claude"
contribution_source: "/home/jfortin/openarms/wiki/config/schema.yaml"
contribution_date: 2026-04-16
contribution_status: pending-review
contribution_reason: "Discovered during health check integration — the second brain's systemic-incompleteness lesson applies to schema definitions too"
---

# Schema aspirationalism — defining required sections you never validate produces false confidence

## Summary

OpenArms wiki/config/schema.yaml defines required_sections per page type (e.g., lesson requires Summary, Context, Insight, Application, Relationships). But no validation pipeline checks section structure — only frontmatter fields are validated by validate-stage.cjs. The health check scoring against the project's own schema revealed 333 'blocking' violations. These aren't real violations of operational standards — they're violations of aspirational standards nobody enforces. The false confidence is dangerous: the schema looks comprehensive, passes code review, gets committed — but it's fiction. The fix: either align the schema to what pages actually look like (accept reality), or build validation that enforces required_sections (make the aspiration real). Don't do neither — an aspirational schema is worse than no schema because it creates confidence without substance.

## Context

<!-- When does this lesson apply? -->

## Insight

<!-- The core learning -->

## Evidence

<!-- What evidence supports this? -->

## Applicability

Contributed from /home/jfortin/openarms/wiki/config/schema.yaml. Applicability to be assessed during promotion review.

## Relationships

- RELATES TO: [[model-registry|Model Registry]]
