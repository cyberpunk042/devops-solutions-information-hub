---
title: "Evolution Page Standards"
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

> [!success] [[Evolution: Methodology System]] — 92 lines
>
> - 9 dated timeline entries, each with significance explanation
> - 5 Key Shifts identifying real turning points (instructions→infrastructure, project→portable, etc.)
> - Current State names achievements AND next frontiers

### Template

`config/templates/evolution.md` — scaffold via `python3 -m tools.pipeline scaffold evolution "Title"`

## Relationships

- BUILDS ON: [[LLM Wiki Standards — What Good Looks Like]]
- FEEDS INTO: [[Methodology Standards — What Good Execution Looks Like]]

## Backlinks

[[LLM Wiki Standards — What Good Looks Like]]
[[Methodology Standards — What Good Execution Looks Like]]
