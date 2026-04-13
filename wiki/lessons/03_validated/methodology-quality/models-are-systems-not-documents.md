---
title: Models Are Systems, Not Documents
aliases:
  - "Models Are Systems, Not Documents"
type: lesson
domain: cross-domain
layer: 4
status: synthesized
confidence: authoritative
maturity: growing
derived_from:
  - "Model Registry"
  - "Models Are Built in Layers, Not All at Once"
created: 2026-04-10
updated: 2026-04-12
sources:
  - id: directive-models-not-documents
    type: log
    file: wiki/log/2026-04-09-directive-models-are-not-documents.md
    title: Models Are Not Documents — They Must Be Usable Systems
    ingested: 2026-04-09
tags: [models, quality, depth, systems-thinking, usability, standards, failure-lesson]
---
# Models Are Systems, Not Documents

## Summary

The first attempt at building wiki models produced 14 "entry points" that were reading lists — pages listing other page paths without wikilinks, without articulating what the model IS, without standards, and without actionable guidance. A model is not a bibliography. A model is a usable system with clear boundaries, standards, schemas, and adoption guidance. The fix required rebuilding every model with the model-builder skill's full workflow: Key Pages, Lessons Learned, State of Knowledge, How to Adopt.

## Context

This lesson applies whenever building or reviewing a named model in the wiki — or any knowledge artifact that claims to be a "system" or "framework" rather than a page. The triggering signal: if you can strip the content down to a bullet list of links and lose nothing, it's a document, not a model.

## Insight

> [!warning] The document-vs-system test
> A model that can be reduced to "read these pages in this order" is a reading list, not a system. A real model has:
>
> | Property | Document | System |
> |----------|----------|--------|
> | Structure | List of links | Named components with boundaries |
> | Standards | None | What GOOD looks like (companion standards page) |
> | Guidance | "Read this" | "When you encounter X, do Y" |
> | Instances | None | Real examples from practice |
> | Connection | Isolated | Linked to super-model, feeds sister models |
> | Navigation | File paths | `[[Wikilinks]]` for graph connectivity |

The first 14 model pages failed every row of this table. They used file paths instead of wikilinks (zero Obsidian graph connectivity). They listed related pages without explaining the model's principles. They contained no trace of the operator's directives — the specific things asked for (methodology flexibility, composable sub-models, per-case artifact chains) were absent.

> [!tip] The fix: the model-builder skill workflow
> Document → Design → Scaffold → Implement → Test, applied to each model. Every model must have: Key Pages table (member pages with roles), Lessons Learned table (validated experience), State of Knowledge (verified vs thin), How to Adopt (invariant rules + per-project adaptations + what goes wrong). This is what transforms a reading list into a usable system.

## Evidence

**Date:** 2026-04-09

**The failure:** 14 model "entry points" created as `learning-path` type pages — 80-110 lines each, just ordered lists of wikilinks with brief annotations. No model content, no standards, no adoption guidance.

**The operator's response:** "There is also no trace of what I asked in the model.. it look like mindless document.... do you not know what a model is?"

**The fix:** All 15 models rebuilt with the model-builder skill over two sessions. Model pages grew from 80-110 lines to 200-500+ lines with full standard sections. 7 companion standards pages created. The Model Registry created as the entry point.

**Source:** `wiki/log/2026-04-09-directive-models-are-not-documents.md`

## Applicability

- **Wiki model building**: every model page must pass the document-vs-system test
- **API documentation**: an API reference is a document; an API guide with patterns, anti-patterns, and migration paths is a system
- **Architecture docs**: a diagram is a document; an architecture decision record with rationale, alternatives, and reversibility is a system
- **Runbooks**: a checklist is a document; an incident response playbook with decision trees and escalation paths is a system

> [!abstract] The general principle
> Any knowledge artifact that claims to be more than reference material must include: what it IS (boundaries), what GOOD looks like (standards), how to USE it (guidance), and proof it WORKS (instances). Without all four, it's a document wearing a system's label.

### How This Connects — Navigate From Here

> [!abstract] From This Lesson → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **What principle governs this?** | [[right-process-for-right-context-the-goldilocks-imperative|Principle — Right Process for Right Context — The Goldilocks Imperative]] |
> | **How does enforcement apply?** | [[infrastructure-over-instructions-for-process-enforcement|Principle — Infrastructure Over Instructions for Process Enforcement]] |
> | **How does structure help?** | [[structured-context-governs-agent-behavior-more-than-content|Principle — Structured Context Governs Agent Behavior More Than Content]] |
> | **What is my identity profile?** | [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]] |
> | **Where does this fit in the system?** | [[methodology-system-map|Methodology System Map]] — find any component |

## Self-Check — Am I About to Make This Mistake?

> [!warning] Ask yourself when creating or reviewing a model page:
>
> 1. **Is this a SYSTEM or a reading list?** A system defines components, interactions, failure modes, adoption paths. A reading list just links to other pages.
> 2. **Could someone IMPLEMENT from this page?** If they'd need to read 5 other pages to understand how it works, it's a reading list, not a system definition.
> 3. **Does it have concrete examples?** Not "this is used in many projects" — WHICH projects, showing WHAT, with what RESULT?
> 4. **Would the operator say "there is no trace of what I asked"?** The original 14 model pages were 80-110 line reading lists. The operator's response: "mindless document." Systems are 200+ lines with structure.

## Relationships

- DERIVED FROM: [[model-registry|Model Registry]]
- RELATES TO: [[models-are-built-in-layers-not-all-at-once|Models Are Built in Layers, Not All at Once]]
- RELATES TO: [[the-agent-must-practice-what-it-documents|The Agent Must Practice What It Documents]]
- FEEDS INTO: [[model-llm-wiki|Model — LLM Wiki]]

## Backlinks

[[model-registry|Model Registry]]
[[models-are-built-in-layers-not-all-at-once|Models Are Built in Layers, Not All at Once]]
[[the-agent-must-practice-what-it-documents|The Agent Must Practice What It Documents]]
[[model-llm-wiki|Model — LLM Wiki]]
[[2026-04-09-directive-bottom-up-model-completion|Bottom-Up Model Completion — 10+ Named Models Required]]
[[methodology-is-a-framework-not-a-fixed-pipeline|Methodology Is a Framework, Not a Fixed Pipeline]]
[[methodology-standards-initiative-gaps|Methodology Standards Initiative — Gap Analysis]]
[[methodology-standards-initiative-honest-assessment|Methodology Standards Initiative — Honest Assessment]]
[[2026-04-09-directive-models-are-not-documents|Models Are Not Documents — They Must Be Usable Systems]]
[[E006-standards-by-example|Standards-by-Example]]
[[systemic-incompleteness-is-invisible-to-validation|Systemic Incompleteness Is Invisible to Validation]]
