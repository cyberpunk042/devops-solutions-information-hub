---
title: "Domain Overview Page Standards"
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
tags: [standards, domain-overview, page-type, quality, exemplar]
---

# Domain Overview Page Standards

## Summary

Standards for domain overview pages — curator pages that assess a domain's knowledge state, classify pages by maturity, identify gaps, and set research priorities. Domain overviews live on the spine layer. They're NAVIGATION, not content — they help readers find what exists and understand what's missing.

## Key Insights

1. **State of Knowledge must be honest.** Three tiers: Authoritative (we know this well), Good (decent coverage), Thin (gaps). Don't inflate — a domain with 3 seed pages is Thin, not Good.

2. **Maturity Map reflects ACTUAL page distribution.** Group pages by their maturity field (seed, growing, mature, canonical). This is a live snapshot, not a wishful assessment.

3. **Gaps section names SPECIFIC missing topics.** Not "more research needed" — "missing: comparison of X vs Y, deep-dive on Z mechanism, lesson about W failure."

4. **Key Pages list is CURATED reading order.** Not alphabetical. Not all pages. The 5-8 most important, in the order a newcomer should read them.

## Deep Analysis

### Required Sections

| Section | Purpose | Minimum |
|---------|---------|---------|
| **Summary** | Domain scope and current state | 30 words |
| **State of Knowledge** | Authoritative / Good / Thin assessment | Honest tier-based assessment |
| **Maturity Map** | Pages grouped by maturity | Reflects actual frontmatter values |
| **Gaps** | Specific missing topics | Named topics, not vague |
| **Priorities** | Ordered research targets | Numbered, actionable |
| **Key Pages** | Curated reading order | 5-8 pages, ordered for newcomers |
| **Relationships** | Connections | ≥3 |

### The Gold-Standard Exemplar

> [!success] [[Cross-Domain — Domain Overview]] — 126 lines
>
> - State of Knowledge with 3 tiers (Authoritative, Good, Thin)
> - Maturity Map showing 29 lessons, 6 patterns, 13 decisions
> - Specific gap analysis with actionable priorities
> - Key Pages in recommended reading order

### Template

`wiki/config/templates/domain-overview.md` — scaffold via `python3 -m tools.pipeline scaffold domain-overview "Title"`

## Relationships

- BUILDS ON: [[LLM Wiki Standards — What Good Looks Like]]
- FEEDS INTO: [[Methodology Standards — What Good Execution Looks Like]]

## Backlinks

[[LLM Wiki Standards — What Good Looks Like]]
[[Methodology Standards — What Good Execution Looks Like]]
