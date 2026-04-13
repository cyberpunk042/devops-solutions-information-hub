---
title: Evolution Page Standards
aliases:
  - "Evolution Page Standards"
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
tags: [standards, evolution, page-type, quality, exemplar]
---

# Evolution Page Standards

## Summary

Standards for evolution pages — historical narratives tracking how a concept, system, or domain changed over time. Evolution pages are spine-layer navigation — they're meta-analysis, not original content. Timeline entries must have dates AND significance. Key Shifts identify turning points, not restate the timeline.

## Key Insights

1. **Timeline entries need significance, not just dates.** "2026-04-10 — something happened" is a log entry. "2026-04-10 — Overnight run proved instruction-based enforcement fails at 75%. Triggered shift to infrastructure enforcement." is an evolution entry.

2. **Key Shifts are interpretive.** They answer "what CHANGED direction?" not "what happened?" The shift from instructions to infrastructure enforcement is a Key Shift. Each individual bug fix is not.

3. **Current State must be honest about what's next.** Not a victory lap. Name what's done AND what remains.

## Deep Analysis

### Required Sections

| Section | Purpose | Minimum |
|---------|---------|---------|
| **Summary** | What evolved and where it stands now | 30 words |
| **Timeline** | Dated entries with significance | ≥5 entries |
| **Key Shifts** | Turning points that changed direction | ≥2 shifts |
| **Current State** | What's done, what's next | Honest: both achievements and gaps |
| **Relationships** | Connections | ≥1 |

### The Gold-Standard Exemplar

> [!success] [[methodology-evolution-history|Evolution — Methodology System]] — 92 lines
>
> - 9 dated timeline entries, each with significance explanation
> - 5 Key Shifts identifying real turning points (instructions→infrastructure, project→portable, etc.)
> - Current State names achievements AND next frontiers

### Annotated Exemplar: [[methodology-evolution-history|Evolution — Methodology System]]

> [!example]- What makes a good evolution page
>
> **Timeline with significance:** Every entry has a date AND why it mattered. "2026-04-08 — Infrastructure enforcement deployed (violations: 75%→0%)" — not just "hooks added."
> **Key Shifts:** ≥2 turning points with Before/Evidence/After structure. Shows the DIRECTION change, not just events.
> **Current State:** Honest table with aspect/state/evidence. Numbers where possible.

### Template

`wiki/config/templates/evolution.md` — scaffold via `python3 -m tools.pipeline scaffold evolution "Title"`

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **Model these standards serve** | [[model-llm-wiki|Model — LLM Wiki]] |
> | **Global wiki standards** | [[model-llm-wiki-standards|LLM Wiki Standards — What Good Looks Like]] |
> | **Template for this type** | `wiki/config/templates/evolution.md` |
> | **System map** | [[methodology-system-map|Methodology System Map]] |
> | **Learning path** | [[methodology-fundamentals|Learning Path — Methodology Fundamentals]] |

## Relationships

- BUILDS ON: [[model-llm-wiki-standards|LLM Wiki Standards — What Good Looks Like]]
- FEEDS INTO: [[model-methodology-standards|Methodology Standards — What Good Execution Looks Like]]

## Backlinks

[[model-llm-wiki-standards|LLM Wiki Standards — What Good Looks Like]]
[[model-methodology-standards|Methodology Standards — What Good Execution Looks Like]]
