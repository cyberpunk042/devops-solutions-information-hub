---
title: Deep-Dive Page Standards
aliases:
  - "Deep-Dive Page Standards"
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
tags: [standards, deep-dive, page-type, quality, exemplar]
---

# Deep-Dive Page Standards

## Summary

Standards for deep-dive pages — extended analysis that goes significantly deeper than a concept page. The Deep Analysis section IS the page — ≥200 words with ≥3 subsections. Callouts are REQUIRED, not optional. If the analysis fits in one section, it's a concept, not a deep-dive.

## Key Insights

1. **A deep-dive earns its name through exhaustive analysis.** The minimum 200-word Deep Analysis is a floor, not a target. Strong deep-dives are 300-500+ words of structured analysis.

2. **Callouts are required because deep-dives must be scannable.** A 400-word block of prose is an essay. A 400-word analysis with `> [!info]`, `> [!warning]`, `> [!example]-` foldable sections is a reference.

3. **Use for topics that outgrow concept pages.** If a concept page's Deep Analysis exceeds 300 words, consider splitting: the concept page keeps the overview, a deep-dive gets the extended analysis.

## Deep Analysis

### Required Sections

| Section | Purpose | Minimum |
|---------|---------|---------|
| **Summary** | What this deep-dive explores | 30 words |
| **Key Insights** | High-level takeaways for non-readers | 3-8 items |
| **Deep Analysis** | The primary content | 200 words, ≥3 subsections |
| **Relationships** | Connections | ≥2 |

### Quality Bar

- Deep Analysis ≥200 words, ≥3 `###` subsections
- Callouts REQUIRED: `> [!info]`, `> [!abstract]`, `> [!warning]`, `> [!example]-`
- Conclusions section recommended — synthesize findings
- Open Questions encouraged — surface subproblems for future work

### The Gold-Standard Exemplar

> [!success] [[adoption-guide|Adoption Guide — How to Use This Wiki's Standards]] — 325 lines
>
> - 5 core principles in Key Insights
> - Multi-subsection Deep Analysis with step-by-step walkthrough
> - Multiple callout types creating visual structure
> - Recursive framework explanation

### Common Failures

| Failure | What It Looks Like | The Fix |
|---------|-------------------|---------|
| **Shallow deep-dive** | <200 words in Deep Analysis | Go deeper or keep as concept page |
| **Single-block analysis** | No subsections, one long essay | ≥3 `###` subsections, one mechanism per section |
| **No callouts** | Prose-only at 300+ lines | Required: use callouts for structure |

### Annotated Exemplar: [[methodology-adoption-guide|Methodology Adoption Guide]]

> [!example]- Full Walkthrough — Why Each Section Works
>
> **1. Frontmatter** — `type: deep-dive`, `deep_analysis_min_words: 200` (from artifact-types.yaml — higher bar than concept). Deep-dives justify their length through DEPTH, not breadth. ← A concept page at 300+ lines should be a deep-dive. The type distinction tells the reader "this goes significantly deeper than a concept page on the same topic."
>
> **2. Summary** — "This guide explains how any project in the ecosystem picks up the methodology, stage-gate system, backlog hierarchy, and quality standards." States the scope AND the audience. ← Deep-dive summaries must set expectations for LENGTH and DEPTH. The reader commits to a longer read and needs to know it's worth it.
>
> **3. Progressive disclosure** — 4 adoption tiers presented in increasing complexity. Reader doesn't need to read all 4 — they pick their tier and read that section. Each tier has: what you get, effort, prerequisites. ← This is WHY deep-dives exist: they can structure information for multiple reader levels. A concept page serves one level; a deep-dive adapts to the reader.
>
> **4. Concrete code examples** — YAML, bash, and markdown examples throughout. Not "configure your project" but the ACTUAL config to paste. ← Deep-dives earn their length through specificity. Every abstraction is grounded in a real command or config block. Without concrete examples, a deep-dive is just a long concept page.
>
> **5. Per-domain quick starts** — 3 domain-specific callouts (TypeScript, Python/Wiki, Infrastructure). Reader picks their stack. ← Callouts are REQUIRED for deep-dives (per artifact-types.yaml). They break up the length, provide navigation handles, and let readers skip irrelevant sections.
>
> **6. Invariants section** — 7 rules that apply at EVERY tier. Clear boundary between what adapts (per-tier, per-domain) and what never changes (invariants). ← This structural separation is what makes the deep-dive a SYSTEM, not a list. The reader knows which rules to follow always vs which to adapt.
>
> **What could still improve:** Table of contents at the top (for pages >200 lines), estimated reading time per section, "If you only read one section" guidance.

### Template

`wiki/config/templates/deep-dive.md` — scaffold via `python3 -m tools.pipeline scaffold deep-dive "Title"`

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **Model these standards serve** | [[model-llm-wiki|Model — LLM Wiki]] |
> | **Global wiki standards** | [[model-llm-wiki-standards|LLM Wiki Standards — What Good Looks Like]] |
> | **Template for this type** | `wiki/config/templates/deep-dive.md` |
> | **System map** | [[methodology-system-map|Methodology System Map]] |
> | **Learning path** | [[methodology-fundamentals|Learning Path — Methodology Fundamentals]] |

## Relationships

- BUILDS ON: [[model-llm-wiki-standards|LLM Wiki Standards — What Good Looks Like]]
- FEEDS INTO: [[model-methodology-standards|Methodology Standards — What Good Execution Looks Like]]

## Backlinks

[[model-llm-wiki-standards|LLM Wiki Standards — What Good Looks Like]]
[[model-methodology-standards|Methodology Standards — What Good Execution Looks Like]]
