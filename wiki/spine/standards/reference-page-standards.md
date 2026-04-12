---
title: "Reference Page Standards"
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
tags: [standards, reference, page-type, quality, exemplar]
---

# Reference Page Standards

## Summary

Standards for reference pages — LOOKUP material that readers consult for specific answers, not read linearly. A reference page is structured for scanning: tables, code blocks, checklists. If the page must be read start-to-finish to be useful, it's a concept, not a reference.

## Key Insights

1. **Reference pages are optimized for LOOKUP, not reading.** The reader arrives with a specific question ("what are the gate commands for TypeScript?") and should find the answer without reading the whole page.

2. **Progressive disclosure is the structural principle.** Start with the overview table. Drill into subsections for detail. The reader stops when they have enough.

3. **Code examples are required, not optional.** A reference page about configuration without config examples is incomplete. Show the exact YAML, the exact command, the exact output.

## Deep Analysis

### Required Sections

| Section | Purpose | Minimum |
|---------|---------|---------|
| **Summary** | What this reference covers and who needs it | 30 words |
| **Reference Content** | The actual lookup material — tables, code blocks, checklists | Structured, not prose |
| **Relationships** | Connections | ≥1 |

### Section Quality Bar

- Main content in `> [!info]` tables for scanability
- `> [!tip]` for usage guidance
- `> [!warning]` for gotchas and common mistakes
- Code blocks for exact commands, configs, outputs

### The Gold-Standard Exemplar

> [!success] [[Methodology Adoption Guide]] — 259 lines, 8 relationships
>
> - 4 adoption tiers with progressive detail per tier
> - Concrete YAML/bash/markdown examples throughout
> - Per-domain quick starts in separate callouts
> - Invariants section for universal rules

### Common Failures

| Failure | What It Looks Like | The Fix |
|---------|-------------------|---------|
| **Prose reference** | Paragraphs explaining how to configure | Tables and code blocks. Show, don't tell. |
| **No examples** | "Configure your project" without showing HOW | Include the exact config/command/output |
| **Linear required** | Must read everything to find one answer | Progressive disclosure — overview first, detail in subsections |

### Template

`config/templates/reference.md` — scaffold via `python3 -m tools.pipeline scaffold reference "Title"`

## Relationships

- BUILDS ON: [[Model: LLM Wiki Standards — What Good Looks Like]]
- FEEDS INTO: [[Model: Methodology Standards — What Good Execution Looks Like]]

## Backlinks

[[Model: LLM Wiki Standards — What Good Looks Like]]
[[Model: Methodology Standards — What Good Execution Looks Like]]
