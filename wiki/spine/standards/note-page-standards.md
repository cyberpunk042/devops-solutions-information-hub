---
title: Note Page Standards
aliases:
  - "Note Page Standards"
type: concept
domain: cross-domain
layer: spine
status: synthesized
confidence: high
maturity: growing
created: 2026-04-11
updated: 2026-04-11
sources:
  - id: artifact-types
    type: file
    file: wiki/config/artifact-types.yaml
tags: [standards, note, page-type, quality, exemplar, log]
---

# Note Page Standards

## Summary

Standards for note pages — log entries recording directives, session summaries, or completion reports. The critical rule: operator words are VERBATIM. Never paraphrase. The `note_type` field (directive, session, completion) determines the structure.

## Key Insights

1. **Directive notes preserve operator intent exactly.** Quotes are verbatim. Interpretation is clearly separated. The operator's exact words are sacrosanct.

2. **Session notes record what happened.** Key decisions, artifacts produced, state changes. Not a conversation transcript — a structured summary.

3. **Completion notes record what was done.** Stages completed, artifacts produced, concerns raised, verification results.

## Deep Analysis

### Required Sections

| Section | Purpose | Minimum |
|---------|---------|---------|
| **Summary** | What happened or was directed | 10 words |

### Per note_type structure

| Type | Additional Content |
|------|-------------------|
| **directive** | Verbatim quotes in blockquotes, then interpretation section |
| **session** | Decisions list, artifacts list, state changes |
| **completion** | Stages done, artifacts, gate results, concerns |

### The Gold-Standard Exemplar

> [!success] [[2026-04-09-directive-models-are-not-documents|Models Are Not Documents — They Must Be Usable Systems]] — 49 lines
>
> - Operator words quoted VERBATIM
> - Interpretation clearly separated from quotes
> - Summary is actionable: states what needs to change

### Annotated Exemplar: See directive notes in raw/notes/

> [!example]- What makes a good note (directive type)
>
> **Operator words verbatim:** Block quotes with EXACT words. Not paraphrased. Not interpreted. The verbatim section IS the authority.
> **Interpretation separated:** After the verbatim quotes, clearly marked interpretation: "What the operator is actually saying." Keeps observation separate from analysis.
> **Requirements extracted:** Numbered list of concrete requirements derived from the directive. Each is specific and actionable.

### Template

`wiki/config/templates/note.md` — scaffold via `python3 -m tools.pipeline scaffold note "Title"`

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **Model these standards serve** | [[model-methodology|Model — Methodology]] |
> | **Methodology standards** | [[model-methodology-standards|Methodology Standards — What Good Execution Looks Like]] |
> | **Template for this type** | `wiki/config/templates/note.md` |
> | **System map** | [[methodology-system-map|Methodology System Map]] |
> | **Learning path** | [[methodology-fundamentals|Learning Path — Methodology Fundamentals]] |

## Relationships

- RELATES TO: [[model-methodology|Model — Methodology]]
- FEEDS INTO: [[model-methodology-standards|Methodology Standards — What Good Execution Looks Like]]

## Backlinks

[[model-methodology|Model — Methodology]]
[[model-methodology-standards|Methodology Standards — What Good Execution Looks Like]]
[[deployment-closure-monitoring-artifacts|Deployment, Closure, and Monitoring Artifacts — Standards and Guide]]
