---
title: Domain Overview Page Standards
aliases:
  - "Domain Overview Page Standards"
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

> [!success] [[cross-domain-domain-overview|Cross-Domain — Domain Overview]] — 126 lines
>
> - State of Knowledge with 3 tiers (Authoritative, Good, Thin)
> - Maturity Map showing 29 lessons, 6 patterns, 13 decisions
> - Specific gap analysis with actionable priorities
> - Key Pages in recommended reading order

### Annotated Exemplar: Check any domain overview in wiki/spine/domain-overviews/

> [!example]- What makes a good domain overview
>
> **Maturity Map:** Groups pages by maturity (seed/growing/mature/canonical) — shows domain health at a glance.
> **Coverage Assessment:** What's covered, what's thin, what's missing — specific named gaps.
> **Key Pages:** Curated reading order, not alphabetical dump. Each page annotated with why it's key.
> **Priorities:** Named next actions with estimated effort.

### Template

`wiki/config/templates/domain-overview.md` — scaffold via `python3 -m tools.pipeline scaffold domain-overview "Title"`

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **Model these standards serve** | [[model-llm-wiki|Model — LLM Wiki]] |
> | **Global wiki standards** | [[model-llm-wiki-standards|LLM Wiki Standards — What Good Looks Like]] |
> | **Template for this type** | `wiki/config/templates/domain-overview.md` |
> | **System map** | [[methodology-system-map|Methodology System Map]] |
> | **Learning path** | [[methodology-fundamentals|Learning Path — Methodology Fundamentals]] |

## Relationships

- BUILDS ON: [[model-llm-wiki-standards|LLM Wiki Standards — What Good Looks Like]]
- FEEDS INTO: [[model-methodology-standards|Methodology Standards — What Good Execution Looks Like]]

## Backlinks

[[model-llm-wiki-standards|LLM Wiki Standards — What Good Looks Like]]
[[model-methodology-standards|Methodology Standards — What Good Execution Looks Like]]
