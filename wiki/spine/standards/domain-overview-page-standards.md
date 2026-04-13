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

### Annotated Exemplar: [[cross-domain-domain-overview|Cross-Domain — Domain Overview]]

> [!example]- Full Walkthrough — Why Each Section Works
>
> **1. Frontmatter** — `type: domain-overview`, `domain: cross-domain`, `maturity: growing`. The `maturity` field on a domain overview reflects the domain's AGGREGATE health, not just this page. ← This is WHY domain overviews are curator pages, not content pages.
>
> **2. Summary** — "The cross-domain area is not a subject-matter domain but a structural layer." Immediately tells the reader what this domain IS and how it differs from content domains. ← Orientation in seconds — the reader knows whether this is the right domain before scrolling.
>
> **3. Maturity Map** — Groups 29 lessons by maturity (seed/growing/mature/canonical) as a table with counts. ← Shows domain health at a glance. A reader sees "3 canonical, 12 growing, 14 seed" and knows WHERE the domain is strong vs thin.
>
> **4. Coverage Assessment** — "What's covered: methodology framework, artifact taxonomy, agent compliance. What's thin: SDLC customization, formal context grammar." Named gaps with specificity. ← Not "some areas need work" — exact named gaps that become backlog candidates.
>
> **5. Key Pages** — Curated reading order, not alphabetical dump. Each page annotated with WHY it's key: "Methodology Framework — entry point, defines the 9 models." ← A new reader follows this order and builds understanding progressively.
>
> **6. Priorities** — "P1: Deepen SDLC chain configs (3 YAMLs are drafts). P2: Add context engineering standards page." Named next actions with estimated effort. ← Actionable, not aspirational. An agent or human can pick up work directly from these priorities.
>
> **What could still improve:** Backlink density analysis per page (which pages are referenced most but have the thinnest content?), automated maturity scoring from pipeline metrics.

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
