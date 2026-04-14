---
title: Epic Page Standards
aliases:
  - "Epic Page Standards"
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
tags: [standards, epic, page-type, quality, exemplar, backlog]
---

# Epic Page Standards

## Summary

Standards for epic pages — strategic containers that break into modules and tasks. An epic is NEVER done by itself. Its readiness is COMPUTED from children, never manually claimed. Every epic must trace to a verbatim operator directive. Goals must be concrete and measurable. Done When items must be verifiable with specific commands or checks.

## Key Insights

1. **Epics trace to operator directives.** Every epic exists because the operator said something. The `sources` field links to the raw/notes/ directive log. No invented epics.

2. **Done When items are VERIFIABLE.** "Improve quality" is not verifiable. "Templates exist for all page types" is verifiable with `ls wiki/config/templates/`. Each item should have an implicit or explicit verification command.

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

> [!success] [[E003-artifact-type-system|Artifact Type System]] — 105 lines, all 5 stages complete
>
> - Goals are concrete: "Create templates for all 8 page types currently missing"
> - Done When checkboxes verifiable with specific commands
> - 22 artifacts listed across all stages
> - Dependencies explicit: "None — this is the foundation epic"
> - Traces to operator directive in sources field

### Annotated Exemplar: [[e010-model-updates-all-15-models-reflect-current-knowledge|E010 — Model Updates — All 16 Models Reflect Current Knowledge]]

> [!example]- Full Walkthrough — Why Each Section Works
>
> **Operator Directives annotation:**
> 4 verbatim quotes traced to specific directive files. Each quote names what the operator ACTUALLY SAID — not paraphrased, not interpreted. The directives ARE the authority: "when in doubt, re-read the directive."
>
> **Goals annotation:**
> 8 specific goals, each a CAPABILITY: "Every model page reflects ALL knowledge," "Each model's Key Insights section is CURRENT." Not "improve models" — WHAT specifically improves and HOW you verify it.
>
> **Done When annotation:**
> 14 checkboxes — each names a SPECIFIC FILE or OBSERVABLE BEHAVIOR: "Model: Methodology — updated with SDLC profiles, Goldilocks, readiness/progress..." Not "models are updated" — WHICH models, WITH WHAT content. The last 2 items are validation steps (pipeline post + operator discoverability test).
>
> **Module Breakdown annotation:**
> 4 modules (M1-M4), 18 tasks total. Each task row has: task ID, which model, what's needed, effort estimate (XS to L). A person reading ONLY the module breakdown can understand the full scope and start working.
>
> **Handoff Context annotation:**
> `> [!info] For anyone picking this up in a fresh context:` — 5 paragraphs: what happened, what's partially done, what needs to happen, key files to read first. This is the CRITICAL section that makes the epic work across context boundaries. Anyone reading this in a fresh session can resume immediately.
>
> **Why this exemplar works:** It preaches what it teaches. The epic about updating models ITSELF demonstrates every standard it defines: specific goals, verifiable Done When, module breakdown with per-task details, dependencies both in and out, open questions, and a handoff context that serves PM/PO/any agent.

### Template

`wiki/config/templates/epic.md` — scaffold via `python3 -m tools.pipeline scaffold epic "Title"`

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **Model these standards serve** | [[model-methodology|Model — Methodology]] |
> | **Methodology standards** | [[model-methodology-standards|Methodology Standards — What Good Execution Looks Like]] |
> | **Template for this type** | `wiki/config/templates/epic.md` |
> | **System map** | [[methodology-system-map|Methodology System Map]] |
> | **Learning path** | [[methodology-fundamentals|Learning Path — Methodology Fundamentals]] |

## Relationships

- BUILDS ON: [[backlog-hierarchy-rules|Backlog Hierarchy Rules]]
- RELATES TO: [[model-methodology|Model — Methodology]]
- FEEDS INTO: [[model-methodology-standards|Methodology Standards — What Good Execution Looks Like]]

## Backlinks

[[backlog-hierarchy-rules|Backlog Hierarchy Rules]]
[[model-methodology|Model — Methodology]]
[[model-methodology-standards|Methodology Standards — What Good Execution Looks Like]]
[[initiation-and-planning-artifacts|Initiation and Planning Artifacts — Standards and Guide]]
