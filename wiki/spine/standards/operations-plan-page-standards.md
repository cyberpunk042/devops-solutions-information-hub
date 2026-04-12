---
title: "Operations Plan Page Standards"
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
tags: [standards, operations-plan, page-type, quality, exemplar]
---

# Operations Plan Page Standards

## Summary

Standards for operations plan pages — sequential deterministic checklists that any agent can follow mechanically. An operations plan is NOT a design plan. It requires ZERO judgment — every step has Action, Expected output, Validation, and Rollback. If judgment is required at any step, it should be a design plan (concept type with methodology/design-plan template) instead.

## Key Insights

1. **The delegation test:** Give this plan to a different agent with no context. Can they execute it and get the same result? If yes, it's a valid operations plan. If no, it needs more detail or is actually a design plan.

2. **Every step has 4 components.** Action (what to do), Expected output (what success looks like), Validation (how to verify), Rollback (what to do if it fails). Missing any component makes the step unreliable.

3. **Prerequisites are checkboxes.** Verifiable BEFORE step 1. Not "make sure you're ready" — specific checks with specific commands.

## Deep Analysis

### Required Sections

| Section | Purpose | Minimum |
|---------|---------|---------|
| **Summary** | What this plan executes and the end state | 30 words |
| **Prerequisites** | Checkboxes — verifiable before step 1 | ≥1 prerequisite |
| **Steps** | Sequential, each with Action/Expected/Validation/Rollback | ≥3 steps |
| **Rollback** | Global rollback for partial failure | How to restore pre-plan state |
| **Completion Criteria** | Checkboxes — verifiable after all steps | ≥1 criterion |
| **Relationships** | What this plan implements | ≥1 |

### The Gold-Standard Exemplar

> [!success] [[Operations Plan: Wiki Post-Ingestion Validation]] — 90 lines
>
> - 6 sequential steps, each with all 4 components
> - Prerequisites as checkboxes with verification commands
> - Global rollback section covering partial failure
> - Completion criteria with specific commands to run

### The Critical Distinction

> [!warning] Operations Plan ≠ Design Plan
>
> | Dimension | Operations Plan | Design Plan |
> |-----------|----------------|-------------|
> | Judgment | None | High |
> | Delegatable | Yes, to any agent | No, requires expertise |
> | Structure | Steps with Action/Validation | Decisions with Rationale |
> | Template | `operations-plan.md` | `methodology/design-plan.md` |
> | Wiki type | `operations-plan` | `concept` |

### Template

`config/templates/operations-plan.md` — scaffold via `python3 -m tools.pipeline scaffold operations-plan "Title"`

## Relationships

- BUILDS ON: [[Model: LLM Wiki Standards — What Good Looks Like]]
- RELATES TO: [[Stage-Gate Methodology]]
- FEEDS INTO: [[Model: Methodology Standards — What Good Execution Looks Like]]

## Backlinks

[[Model: LLM Wiki Standards — What Good Looks Like]]
[[Stage-Gate Methodology]]
[[Model: Methodology Standards — What Good Execution Looks Like]]
[[Deployment, Closure, and Monitoring Artifacts — Standards and Guide]]
