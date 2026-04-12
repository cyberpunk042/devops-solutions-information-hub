---
title: "Comparison Page Standards"
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

> [!success] [[Cross-Domain Patterns]] — 195 lines, 10 relationships
>
> - Pattern inventory table as core matrix (8 rows × 4 columns)
> - Each matrix row expanded into a Deep Analysis subsection with instance-level comparison tables
> - The comparison DISCOVERS: 6 patterns reduce to 3 underlying constraints (bounded context, probabilistic LLM, deployment drift)
> - Rich callout usage: warning, example, abstract

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

`config/templates/comparison.md` — scaffold via `python3 -m tools.pipeline scaffold comparison "Title"`

## Relationships

- BUILDS ON: [[Model: LLM Wiki Standards — What Good Looks Like]]
- RELATES TO: [[Model: Wiki Design]]
- FEEDS INTO: [[Model: Methodology Standards — What Good Execution Looks Like]]

## Backlinks

[[Model: LLM Wiki Standards — What Good Looks Like]]
[[Model: Wiki Design]]
[[Model: Methodology Standards — What Good Execution Looks Like]]
