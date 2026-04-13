---
title: Operations Plan Page Standards
aliases:
  - "Operations Plan Page Standards"
type: concept
domain: cross-domain
layer: spine
status: synthesized
confidence: high
maturity: growing
created: 2026-04-11
updated: 2026-04-13
sources:
  - id: artifact-types
    type: file
    file: wiki/config/artifact-types.yaml
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

> [!success] [[wiki-post-ingestion-operations-plan|Operations Plan — Wiki Post-Ingestion Validation]] — 90 lines
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

### Annotated Exemplar: [[second-brain-integration-chain|Operations Plan — Second Brain Integration Chain — Complete Walkthrough]]

> [!example]- Full Walkthrough — Why Each Section Works
>
> **1. Frontmatter** — `type: operations-plan`, `artifact_class: document` (from artifact-types.yaml). Operations plans are BINDING — they constrain execution, not suggest it. ← The document class means an agent treats this as instructions, not reference. This is WHY operations plans exist as a separate type from concept pages.
>
> **2. Summary** — "Complete step-by-step chain for integrating ANY project with the second brain." States the scope (any project) and the format (step-by-step). ← The summary tells the reader immediately: this is a SEQUENTIAL checklist, not a discussion. If you're looking for reasoning, read the design doc instead.
>
> **3. Prerequisites as checklist** — `- [ ] Second brain accessible` `- [ ] Python available` — verifiable BEFORE starting. ← Without prerequisites, step 1 may fail due to missing setup. Checkboxes make this verifiable — an agent can programmatically check each condition before beginning.
>
> **4. Steps with 4-field structure** — Each of 17 steps has: Action (what to do), Command (exact CLI), Expected output (what success looks like), Validation (how to verify). ← A "dumb agent" can follow these mechanically. The 4-field structure prevents the common failure where steps say WHAT but not HOW TO VERIFY. The validation field is what makes this deterministic rather than suggestive.
>
> **5. Phases group related steps** — Discovery → Identity → Methodology → Standards → Work Loop → Feedback → Mode Selection. Reader can enter at their current phase. ← Phases create entry points for partially-completed integrations. A project that already has an identity profile starts at Phase 3.
>
> **6. Completion criteria** — Observable behaviors: "identity profile declared," "at least one contribution back." Not "plan followed." ← Outcome-based, not process-based. The plan succeeds when the behaviors exist, not when every step was executed in order.
>
> **What could still improve:** Error handling guidance per step (what to do when a step fails), estimated time per phase, dependency markers between steps.

### Template

`wiki/config/templates/operations-plan.md` — scaffold via `python3 -m tools.pipeline scaffold operations-plan "Title"`

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **Model these standards serve** | [[model-methodology|Model — Methodology]] |
> | **Global wiki standards** | [[model-llm-wiki-standards|LLM Wiki Standards — What Good Looks Like]] |
> | **Template for this type** | `wiki/config/templates/operations-plan.md` |
> | **System map** | [[methodology-system-map|Methodology System Map]] |
> | **Learning path** | [[methodology-fundamentals|Learning Path — Methodology Fundamentals]] |

## Relationships

- BUILDS ON: [[model-llm-wiki-standards|LLM Wiki Standards — What Good Looks Like]]
- RELATES TO: [[stage-gate-methodology|Stage-Gate Methodology]]
- FEEDS INTO: [[model-methodology-standards|Methodology Standards — What Good Execution Looks Like]]

## Backlinks

[[model-llm-wiki-standards|LLM Wiki Standards — What Good Looks Like]]
[[stage-gate-methodology|Stage-Gate Methodology]]
[[model-methodology-standards|Methodology Standards — What Good Execution Looks Like]]
[[deployment-closure-monitoring-artifacts|Deployment, Closure, and Monitoring Artifacts — Standards and Guide]]
