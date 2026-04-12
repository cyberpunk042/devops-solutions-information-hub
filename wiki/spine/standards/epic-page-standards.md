---
title: "Epic Page Standards"
type: concept
domain: cross-domain
layer: spine
status: synthesized
confidence: high
maturity: seed
created: 2026-04-11
updated: 2026-04-11
sources:
  - id: artifact-types
    type: file
    file: config/artifact-types.yaml
tags: [standards, epic, page-type, quality, exemplar, backlog]
---

# Epic Page Standards

## Summary

Standards for epic pages — strategic containers that break into modules and tasks. An epic is NEVER done by itself. Its readiness is COMPUTED from children, never manually claimed. Every epic must trace to a verbatim operator directive. Goals must be concrete and measurable. Done When items must be verifiable with specific commands or checks.

## Key Insights

1. **Epics trace to operator directives.** Every epic exists because the operator said something. The `sources` field links to the raw/notes/ directive log. No invented epics.

2. **Done When items are VERIFIABLE.** "Improve quality" is not verifiable. "Templates exist for all page types" is verifiable with `ls config/templates/`. Each item should have an implicit or explicit verification command.

3. **Artifacts list grows across stages.** As the epic progresses through stages, the artifacts list accumulates all deliverables. This is the audit trail — what was actually produced.

4. **Readiness is computed, never claimed.** Epic readiness = average of child readiness. 95% means all stages complete but pending operator review. Claiming 95% when children are at 40% is a methodology violation.

## Deep Analysis

### Required Sections

| Section | Purpose | Minimum |
|---------|---------|---------|
| **Summary** | What this epic delivers and WHY | 30 words, reference operator directive |
| **Goals** | Concrete, measurable deliverables | Bulleted, specific |
| **Done When** | Verifiable completion criteria | Checkboxes with testable statements |
| **Relationships** | What it implements, what it depends on | ≥1 |

### Required Frontmatter

| Field | Value | Why |
|-------|-------|-----|
| `type` | epic | — |
| `priority` | P0-P3 | Scheduling |
| `task_type` | epic | Methodology model selection |
| `current_stage` | document/design/scaffold/implement/test | Where work is now |
| `readiness` | 0-100 | Computed from children |
| `stages_completed` | list | Audit trail |
| `artifacts` | list of file paths | What was produced |

### The Gold-Standard Exemplar

> [!success] [[Artifact Type System]] — 105 lines, all 5 stages complete
>
> - Goals are concrete: "Create templates for all 8 page types currently missing"
> - Done When checkboxes verifiable with specific commands
> - 22 artifacts listed across all stages
> - Dependencies explicit: "None — this is the foundation epic"
> - Traces to operator directive in sources field

### Template

`config/templates/epic.md` — scaffold via `python3 -m tools.pipeline scaffold epic "Title"`

## Relationships

- BUILDS ON: [[Backlog Hierarchy Rules]]
- RELATES TO: [[Model: Methodology]]
- FEEDS INTO: [[Methodology Standards — What Good Execution Looks Like]]

## Backlinks

[[Backlog Hierarchy Rules]]
[[Model: Methodology]]
[[Methodology Standards — What Good Execution Looks Like]]
[[Initiation and Planning Artifacts — Standards and Guide]]
