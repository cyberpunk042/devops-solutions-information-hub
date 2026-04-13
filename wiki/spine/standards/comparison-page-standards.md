---
title: Comparison Page Standards
aliases:
  - "Comparison Page Standards"
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
  - id: exemplar
    type: wiki
    file: wiki/comparisons/cross-domain-patterns.md
tags: [standards, comparison, page-type, quality, exemplar]
---

# Comparison Page Standards

## Summary

Standards for comparison pages — structured evaluations of alternatives across multiple criteria. A comparison page MUST have a matrix table as its core structure. If you can't express the comparison as a table with ≥3 rows and ≥3 columns, it's not ready to be a comparison — keep it as a concept with prose analysis until the structure crystallizes.

## Key Insights

1. **The Comparison Matrix IS the page.** Everything else supports the matrix. The matrix is what the reader looks up. If the matrix doesn't tell the story, the page failed.

2. **Comparisons should DISCOVER something.** Don't just list differences — find the underlying pattern. Six patterns might reduce to three constraints. Four tools might separate into two fundamental approaches. The insight is in the synthesis.

3. **Include a Recommendation section.** A comparison without a recommendation is homework left for the reader. State what you'd choose and for what context. Use `> [!success]` for the recommendation.

## Deep Analysis

### Required Sections

| Section | Purpose | Minimum |
|---------|---------|---------|
| **Summary** | What's compared, headline conclusion | 30 words, state the recommendation upfront |
| **Comparison Matrix** | The core table | ≥3 rows × ≥3 columns in `> [!abstract]` |
| **Key Insights** | What the matrix reveals — interpretation, not restatement | Patterns discovered across the matrix |
| **Deep Analysis** | Per-alternative analysis with `###` subsections | Strengths, weaknesses, ideal use case per option |
| **Relationships** | COMPARES TO targets | ≥2 (must reference what's being compared) |

### Section-by-Section Quality Bar

#### Comparison Matrix

- Wrap in `> [!abstract] Comparison Matrix`
- Consistent scoring: ✓/✗, High/Med/Low, or specific data points
- Columns = alternatives. Rows = evaluation criteria.
- Every cell should be filled — no blanks without explanation

#### Deep Analysis

- One `###` subsection per alternative
- Use `> [!tip]` for "when to choose this"
- Use `> [!warning]` for "when this fails"
- Include a Recommendation subsection with `> [!success]`

### The Gold-Standard Exemplar

> [!success] [[cross-domain-patterns|Cross-Domain Patterns]] — 195 lines, 10 relationships
>
> - Pattern inventory table as core matrix (8 rows × 4 columns)
> - Each matrix row expanded into a Deep Analysis subsection with instance-level comparison tables
> - The comparison DISCOVERS: 6 patterns reduce to 3 underlying constraints (bounded context, probabilistic LLM, deployment drift)
> - Rich callout usage: warning, example, abstract

### Annotated Exemplar: [[openarms-vs-openfleet-enforcement|OpenArms vs OpenFleet Enforcement Architecture]]

> [!example]- Full Walkthrough — Why Each Section Works
>
> **Comparison Matrix annotation:**
> 14-row table comparing OpenArms vs OpenFleet across: agent count, stage enforcement, validation engine, loop ownership, git control, behavioral detection, correction, context compaction, cross-agent coordination, trust management, readiness gating, clean completion rate, implementation effort, configuration model. Each row has a "Winner" column — the matrix DECIDES, not just lists.
>
> **Key Insights annotation:**
> `> [!warning]` callout: "The Scale Transition Creates 6 New Requirements" — with table showing what's needed at solo vs fleet scale. This is the DISCOVERY the comparison produces — not just "they're different" but "HERE are the 6 specific things that change."
>
> **Per-Alternative Deep Analysis annotation:**
> Each alternative gets its own subsection with: `> [!tip]` for "when to choose" and `> [!warning]` for "when this option fails." Strengths AND weaknesses listed. Ideal use case named.
>
> **Recommendation annotation:**
> `> [!success]` callout with scenario → recommendation table. "Solo agent, interactive → OpenArms hooks." "4+ agents, autonomous → OpenFleet architecture." Clear, actionable, context-dependent.

### Common Failures

| Failure | What It Looks Like | The Fix |
|---------|-------------------|---------|
| **Prose comparison** | "X is good at A, Y is good at B" | Must be a table. If you can't make a table, it's not a comparison. |
| **No recommendation** | Matrix exists but no conclusion drawn | Add Recommendation section with `> [!success]` |
| **Restatement** | Key Insights just repeats the matrix in prose | Interpret — what patterns emerge? What's the underlying trade-off? |
| **Missing criteria** | Comparing on 1-2 dimensions only | ≥3 criteria. Include cost, complexity, reversibility. |

### Content Thresholds

| Threshold | Value |
|-----------|-------|
| summary_min_words | 30 |
| deep_analysis_min_words | 100 |
| min_relationships | 2 |
| callouts_required | Yes |

### Template

`wiki/config/templates/comparison.md` — scaffold via `python3 -m tools.pipeline scaffold comparison "Title"`

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **Model these standards serve** | [[model-llm-wiki|Model — LLM Wiki]] |
> | **Global wiki standards** | [[model-llm-wiki-standards|LLM Wiki Standards — What Good Looks Like]] |
> | **Template for this type** | `wiki/config/templates/comparison.md` |
> | **System map** | [[methodology-system-map|Methodology System Map]] |
> | **Learning path** | [[methodology-fundamentals|Learning Path — Methodology Fundamentals]] |

## Relationships

- BUILDS ON: [[model-llm-wiki-standards|LLM Wiki Standards — What Good Looks Like]]
- RELATES TO: [[model-wiki-design|Model — Wiki Design]]
- FEEDS INTO: [[model-methodology-standards|Methodology Standards — What Good Execution Looks Like]]

## Backlinks

[[model-llm-wiki-standards|LLM Wiki Standards — What Good Looks Like]]
[[model-wiki-design|Model — Wiki Design]]
[[model-methodology-standards|Methodology Standards — What Good Execution Looks Like]]
