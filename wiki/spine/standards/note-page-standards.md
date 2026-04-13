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
updated: 2026-04-13
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

### Annotated Exemplar: [[2026-04-09-directive-models-are-not-documents|Models Are Not Documents — They Must Be Usable Systems]]

> [!example]- Full Walkthrough — Why Each Section Works
>
> **1. Frontmatter** — `type: note`, `domain: log`. Notes live in the log domain, not a content domain. ← Notes are temporal artifacts (when something was said), not knowledge artifacts (what we know). The domain placement reflects this — notes are process evidence, not synthesized understanding.
>
> **2. Operator Directive (verbatim)** — Block quotes with EXACT words: `> "the models are not finished. they should be usable systems not just collections of pages."` Not paraphrased. Not interpreted. ← The verbatim section IS the authority. When a future session needs to understand operator intent, the exact words prevent drift. Paraphrasing is lossy.
>
> **3. Interpretation** — After the verbatim quotes, clearly marked: "What the operator is saying: models need entry points, standards, adoption paths, and key pages — not just a list of concepts." ← Keeps observation (what was said) separate from analysis (what it means). This separation lets a reader agree with the words but disagree with the interpretation.
>
> **4. Requirements extracted** — Numbered list of concrete requirements derived from the directive. "1. Every model must have a Key Pages table. 2. Every model must link to its companion standards page." ← Each requirement is specific and actionable. An agent reading this note can turn each requirement into a task without further clarification.
>
> **5. Action items** — What was done as a result: "Created model-registry.md. Updated 8 models with Key Pages tables." ← Closes the loop — the note is not just a record of what was said but a record of what HAPPENED as a result. Traceability from directive to action.
>
> **What could still improve:** Linking action items to specific commits (git provenance), tagging which epics/tasks the directive influenced, noting which requirements were DEFERRED vs addressed.

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
