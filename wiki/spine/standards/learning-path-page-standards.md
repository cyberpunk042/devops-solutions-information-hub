---
title: Learning Path Page Standards
aliases:
  - "Learning Path Page Standards"
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
tags: [standards, learning-path, page-type, quality, exemplar]
---

# Learning Path Page Standards

## Summary

Standards for learning path pages — curated sequences that guide a reader through a topic in a specific order. Learning paths are spine-layer navigation — they don't contain original content, they organize existing content into a pedagogical flow. Each page in the sequence gets a 1-sentence annotation explaining WHY it's at that position.

## Key Insights

1. **Sequence order is the value.** The wiki has 200+ pages. A learning path says "read THESE 8, in THIS order, for THIS reason." The curation IS the content.

2. **Every page gets an annotation.** Not just a list of links — each entry explains what the reader will learn from that page and why it comes at that position in the sequence.

3. **Outcomes must be testable capabilities.** "You should understand methodology" is not testable. "You should be able to select the correct methodology model for any task type" IS testable.

## Deep Analysis

### Required Sections

| Section | Purpose | Minimum |
|---------|---------|---------|
| **Summary** | What you'll learn and why it matters | 30 words |
| **Prerequisites** | What to read/know before starting | Specific pages or skills |
| **Sequence** | Ordered pages with annotations | ≥3 pages, each with 1-sentence annotation |
| **Outcomes** | Testable capabilities after completion | ≥2 testable outcomes |
| **Relationships** | Connections | ≥1 |

### The Gold-Standard Exemplar

> [!success] [[methodology-fundamentals|Learning Path — Methodology Fundamentals]] — 68 lines
>
> - 8 ordered pages, each with `[[wikilink]]` + annotation
> - Prerequisites name specific starting pages
> - Outcomes are testable: "select the correct model," "identify ALLOWED/FORBIDDEN actions"

### Annotated Exemplar: [[methodology-fundamentals|Learning Path — Methodology Fundamentals]]

> [!example]- What makes a good learning path
>
> **30 pages in 8 parts:** Organized by learning mode (LEARN → DECIDE → EXECUTE → ENFORCE → LESSONS → PRINCIPLES → GOLDILOCKS). Each part has a PURPOSE, not just a topic.
> **Per-page annotations:** "Start here. Defines what a methodology model IS" — not just a title link but WHY to read it NOW and what it enables for the NEXT page.
> **Testable outcomes:** "After completing this path you should be able to: select the correct SDLC chain based on phase and scale" — verifiable, not vague.

### Template

`wiki/config/templates/learning-path.md` — scaffold via `python3 -m tools.pipeline scaffold learning-path "Title"`

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **Model these standards serve** | [[model-llm-wiki|Model — LLM Wiki]] |
> | **Global wiki standards** | [[model-llm-wiki-standards|LLM Wiki Standards — What Good Looks Like]] |
> | **Template for this type** | `wiki/config/templates/learning-path.md` |
> | **System map** | [[methodology-system-map|Methodology System Map]] |
> | **Learning path** | [[methodology-fundamentals|Learning Path — Methodology Fundamentals]] |

## Relationships

- BUILDS ON: [[model-llm-wiki-standards|LLM Wiki Standards — What Good Looks Like]]
- FEEDS INTO: [[model-methodology-standards|Methodology Standards — What Good Execution Looks Like]]

## Backlinks

[[model-llm-wiki-standards|LLM Wiki Standards — What Good Looks Like]]
[[model-methodology-standards|Methodology Standards — What Good Execution Looks Like]]
