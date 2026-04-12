---
title: "Concept Page Standards"
type: concept
domain: cross-domain
layer: spine
status: synthesized
confidence: high
maturity: seed
created: 2026-04-11
updated: 2026-04-11
sources:
  - id: wiki-schema
    type: file
    file: config/wiki-schema.yaml
  - id: artifact-types
    type: file
    file: config/artifact-types.yaml
  - id: exemplar
    type: wiki
    file: wiki/domains/cross-domain/methodology-framework.md
tags: [standards, concept, page-type, quality, exemplar]
---

# Concept Page Standards

## Summary

Standards for concept pages — the most common page type in the wiki (74 pages). A concept page defines WHAT something IS: its components, mechanisms, relationships, and boundaries. This document specifies the quality bar section by section, shows what good looks like via the gold-standard exemplar, and lists the common failures specific to this type.

## Key Insights

1. **A concept page defines a SYSTEM, not a list.** The worst concept pages are reading lists — "here are 5 things about X." The best define a system: components, how they interact, what happens when they fail, how to adopt them.

2. **Key Insights must stand alone.** If someone reads ONLY the Key Insights section, they should be able to explain the concept to a colleague. If they need Deep Analysis to understand the concept at all, the Key Insights failed.

3. **Deep Analysis must be subsectioned.** A single-block Deep Analysis is an essay. A subsectioned Deep Analysis is a reference. Each subsection covers one mechanism, one dimension, one facet. The reader can jump to the subsection they need.

4. **Callouts are recommended, not required.** Concept pages CAN be prose-only below 80 lines. Above 80 lines, callouts help the reader scan. Above 150 lines, callouts are expected.

## Deep Analysis

### Required Sections (from wiki-schema.yaml)

| Section | Purpose | Minimum |
|---------|---------|---------|
| **Summary** | What this concept IS and why it matters | 30 words, 2-3 sentences |
| **Key Insights** | Self-contained takeaways a colleague could repeat | 3-8 numbered items |
| **Deep Analysis** | Full mechanism, with ### subsections | 100 words, ≥2 subsections |
| **Relationships** | How this concept connects to others | ≥1 relationship |

### Optional But Encouraged

| Section | When to Include |
|---------|----------------|
| **Open Questions** | When gaps exist. Format: `> [!question]` with `(Requires: ...)` |
| **Reference Card** | When the concept has named components. `> [!info]` table after Summary |

### Section-by-Section Quality Bar

#### Summary

> [!tip] The 30-Second Test
>
> Read the Summary out loud. If the listener can't explain the concept to someone else, the Summary is too vague.

- State what the concept IS, not what the page covers
- Include the key mechanism or insight in the summary itself
- End with why it matters — what breaks without this concept?

**Good:** "The Methodology model defines a flexible FRAMEWORK for defining, selecting, composing, and adapting work processes. It is NOT one fixed pipeline — it is a system that CONTAINS multiple named methodology models..."

**Bad:** "This page discusses methodology and how it works in our projects."

#### Key Insights

- Each insight is a complete, self-contained statement
- Use bold for the key phrase, then explain
- If an insight contains a comparison or taxonomy, use a table
- If an insight is a critical constraint, wrap in `> [!warning]`
- 3-8 insights. Fewer than 3 means the concept is thin. More than 8 means the concept should be split.

**Good:** "**Multiple models, not one pipeline.** Feature Development has 5 stages. Research has 2. Knowledge Evolution has 4 with different stage names. These are INDEPENDENT models, not subsets of one sequence."

**Bad:** "The system supports multiple models." (no detail, not self-contained)

#### Deep Analysis

- MUST use `### subsection` headings — never one continuous block
- Each subsection defines ONE mechanism or dimension
- Use `> [!info]` for reference tables, `> [!abstract]` for taxonomies
- Use `> [!example]-` (foldable) for detailed worked examples
- Use `> [!warning]` for constraints and failure modes
- Include real instances from the wiki or ecosystem — not hypotheticals

**Good:** 8 subsections: "What Is a Methodology Model," "The Model Catalog," "Model Selection," "Model Composition," "Stage Boundaries," "What Goes Wrong," "Model Adaptation," "The Quality Dimension"

**Bad:** One long essay with no headings.

#### Relationships

- Use precise verbs: BUILDS ON, ENABLES, CONTAINS, IMPLEMENTS — not just RELATES TO
- ≥1 relationship required. Strong concept pages have 5-15.
- If the concept governs or contains other pages, use GOVERNS or CONTAINS

### The Gold-Standard Exemplar

> [!success] [[Methodology Framework]] — 383 lines, 17+ relationships
>
> **Why it's the standard:**
> - 7 components defined in a reference card table (Model, Selection, Composition, Adaptation, Recursion, Multi-Track, Quality Target)
> - 6 numbered Key Insights, each with embedded tables
> - 8 Deep Analysis subsections, each defining a concrete mechanism
> - Answered Open Questions section showing resolved questions with decision links
> - Model Registry table showing all 15 governed models
> - Transferability section explaining wiki → project propagation
> - Relationship section uses CONTAINS (not just RELATES TO) for owned sub-pages
>
> **The test:** After reading this page, could you CREATE a new methodology model from scratch? If yes, the concept page succeeded. If you'd need to read 5 other pages, it's a reference list, not a concept.

### Common Failures

| Failure | What It Looks Like | The Fix |
|---------|-------------------|---------|
| **Reading list** | "This concept involves X, Y, Z. See [[X]], [[Y]], [[Z]]." | Define the SYSTEM — how X, Y, Z interact, what breaks without one |
| **Vague insights** | "This is useful in many situations" | Name the situations. Be specific. Data points > adjectives. |
| **Essay analysis** | 500 words of unbroken prose | Add `###` subsections. One mechanism per subsection. |
| **Missing instances** | "This works well in practice" | WHICH practice? Name the wiki page, the project, the date. |
| **Over-claiming** | "This is authoritative" (maturity: seed) | Be honest about maturity. Seed means "first pass, needs evidence." |

### Content Thresholds (from artifact-types.yaml)

| Threshold | Value |
|-----------|-------|
| summary_min_words | 30 |
| deep_analysis_min_words | 100 |
| min_relationships | 1 |
| callouts_required | No (recommended above 80 lines) |

### Template

`config/templates/concept.md` — scaffold via `python3 -m tools.pipeline scaffold concept "Title"`

## Open Questions

> [!question] Should concept pages above 300 lines be split into a concept + deep-dive pair? (Requires: analysis of current long concept pages to see if splitting improves navigation)

## Relationships

- BUILDS ON: [[LLM Wiki Standards — What Good Looks Like]]
- BUILDS ON: [[Methodology Framework]]
- RELATES TO: [[Model: Wiki Design]]
- FEEDS INTO: [[Methodology Standards — What Good Execution Looks Like]]

## Backlinks

[[LLM Wiki Standards — What Good Looks Like]]
[[Methodology Framework]]
[[Model: Wiki Design]]
[[Methodology Standards — What Good Execution Looks Like]]
