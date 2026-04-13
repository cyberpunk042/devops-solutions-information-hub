---
title: Reference Page Standards
aliases:
  - "Reference Page Standards"
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

> [!success] [[methodology-adoption-guide|Methodology Adoption Guide]] — 259 lines, 8 relationships
>
> - 4 adoption tiers with progressive detail per tier
> - Concrete YAML/bash/markdown examples throughout
> - Per-domain quick starts in separate callouts
> - Invariants section for universal rules

### Annotated Exemplar: [[frontmatter-field-reference|Frontmatter Field Reference — Complete Parameter Documentation]]

> [!example]- Full Walkthrough — Why Each Section Works
>
> **AI Quick Start annotation:**
> 5 numbered action items at the top — "Creating a page? → Check Required Fields." "Need advanced tracking? → Check Optional Fields." A reader finds their use case in seconds and jumps to the right section. This is LOOKUP optimization — the antithesis of linear reading.
>
> **Reference Content structure annotation:**
> 6 reference tables, each in an `> [!info]` callout:
> - Required Fields (9 fields × 4 columns: field, type, purpose, what it enables)
> - Knowledge Page Fields (10 fields with "Used By" column showing which types need them)
> - Backlog Fields (12 fields with TWO tracking dimensions: readiness + progress)
> - Milestone Fields (3 fields specific to milestones)
> - Impediment Fields (5 fields with VALUES column showing valid enum values)
> - Enum Values Reference (complete lookup table — 13 enums with all valid values)
>
> **"What It Enables" column annotation:**
> Every field has a "What It Enables" column that says WHAT AUTOMATION reads this field. This is the bridge between metadata and behavior — a reader knows not just "what to put" but "what HAPPENS when I put it." Example: `readiness` → "Dispatch gating (can't start work until threshold), honest progress reporting."
>
> **How Fields Connect to Automation annotation:**
> Final table maps 8 automation tools to the fields they read. `validate.py` reads type, status, confidence. `lint.py` reads maturity, updated, relationships. `evolve --score` reads maturity, derived_from. This table answers: "if I change field X, what breaks?"
>
> **Why this exemplar works:** You can open this page, Ctrl+F for any field name, and get: what it means, what values are valid, whether it's required, and what automation uses it — in one table row. No reading required. Pure LOOKUP.

### Common Failures

| Failure | What It Looks Like | The Fix |
|---------|-------------------|---------|
| **Prose reference** | Paragraphs explaining how to configure | Tables and code blocks. Show, don't tell. |
| **No examples** | "Configure your project" without showing HOW | Include the exact config/command/output |
| **Linear required** | Must read everything to find one answer | Progressive disclosure — overview first, detail in subsections |

### Template

`wiki/config/templates/reference.md` — scaffold via `python3 -m tools.pipeline scaffold reference "Title"`

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **Model these standards serve** | [[model-llm-wiki|Model — LLM Wiki]] |
> | **Global wiki standards** | [[model-llm-wiki-standards|LLM Wiki Standards — What Good Looks Like]] |
> | **Template for this type** | `wiki/config/templates/reference.md` |
> | **System map** | [[methodology-system-map|Methodology System Map]] |
> | **Learning path** | [[methodology-fundamentals|Learning Path — Methodology Fundamentals]] |

## Relationships

- BUILDS ON: [[model-llm-wiki-standards|LLM Wiki Standards — What Good Looks Like]]
- FEEDS INTO: [[model-methodology-standards|Methodology Standards — What Good Execution Looks Like]]

## Backlinks

[[model-llm-wiki-standards|LLM Wiki Standards — What Good Looks Like]]
[[model-methodology-standards|Methodology Standards — What Good Execution Looks Like]]
[[requirements-and-design-artifacts|Requirements and Design Artifacts — Standards and Guide]]
