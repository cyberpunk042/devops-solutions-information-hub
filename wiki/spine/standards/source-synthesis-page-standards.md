---
title: "Source-Synthesis Page Standards"
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
    file: wiki/config/artifact-types.yaml
tags: [standards, source-synthesis, page-type, quality, exemplar]
---

# Source-Synthesis Page Standards

## Summary

Standards for source-synthesis pages — processed versions of raw sources (articles, videos, papers, repos). The synthesis must capture the MECHANISM, not just the surface. A reader should be able to DECIDE whether to use the tool/pattern/technique described without reading the raw source. If they need the original, the synthesis failed. Page length must be ≥25% of raw source length.

## Key Insights

1. **The 0.25 ratio rule is structural.** A 60-line synthesis from a 1,000-line source missed 94% of the content. The 25% minimum ensures depth, not just coverage.

2. **Depth verification is mandatory.** If the source DESCRIBES a tool or format, you MUST read a real INSTANCE of that thing. A README about design.md files ≠ understanding design.md — download and read an actual one.

3. **Start with a reference card.** Every source-synthesis should open with a `> [!info] Source Reference` card: source title, type, author, date, key claim. This is the lookup header for the page.

4. **Concrete data points, not adjectives.** "315 KB → 5.4 KB. 98% reduction." Not "significant reduction." Specificity is what makes a synthesis useful.

## Deep Analysis

### Required Sections

| Section | Purpose | Minimum |
|---------|---------|---------|
| **Summary** | What this source teaches and the decision it enables | 30 words |
| **Key Insights** | 5-12 numbered insights, each a distinct aspect | Concrete data points, not vague claims |
| **Relationships** | Connection to existing wiki knowledge | ≥1 |

### Section-by-Section Quality Bar

#### Summary + Reference Card

- After Summary text, add:
  ```markdown
  > [!info] Source Reference
  > | Attribute | Value |
  > |-----------|-------|
  > | Source    | Title |
  > | Type      | article/video/paper/repo |
  > | Author    | Name |
  > | Key claim | One sentence |
  ```

#### Key Insights

- 5-12 numbered items, each covering a DISTINCT aspect of the source
- Use specific data: percentages, line counts, costs, timings
- If insights contain comparative data, use tables
- Mark constraints/gotchas with `> [!warning]`

### The Gold-Standard Exemplar

> [!success] [[Synthesis: Context Mode — MCP Sandbox for Context Saving]] — 254 lines from 1,057-line source
>
> - 11 Key Insight subsections, each a distinct aspect
> - Concrete data: "315 KB → 5.4 KB. 98% reduction."
> - 12-platform comparison table (structured data, not prose)
> - Actual instance examined — synthesis REWRITTEN after first version caught being surface-level
> - Ratio: 254/1057 = 0.24 (borderline — deeper is better)

### Common Failures

| Failure | What It Looks Like | The Fix |
|---------|-------------------|---------|
| **Surface synthesis** | 60 lines from 1,000-line source | Read the FULL source. Multiple offset reads. ≥0.25 ratio. |
| **Description not understanding** | Synthesized the README, not the code | Depth verification: read a real INSTANCE of the thing |
| **Vague data** | "Significant improvement" | Specific numbers: "12x cost reduction," "98% compression" |
| **No reference card** | Jumps straight into insights | Add `> [!info]` source reference card after Summary |

### Content Thresholds

| Threshold | Value |
|-----------|-------|
| summary_min_words | 30 |
| min_relationships | 1 |
| source_ratio | 0.25 (page length ≥ 25% of raw source) |
| callouts_recommended | Yes (reference card + data tables) |

### Template

`wiki/config/templates/source-synthesis.md` — scaffold via `python3 -m tools.pipeline scaffold source-synthesis "Title"`

## Relationships

- BUILDS ON: [[LLM Wiki Standards — What Good Looks Like]]
- RELATES TO: [[Model: Wiki Design]]
- FEEDS INTO: [[Methodology Standards — What Good Execution Looks Like]]

## Backlinks

[[LLM Wiki Standards — What Good Looks Like]]
[[Model: Wiki Design]]
[[Methodology Standards — What Good Execution Looks Like]]
