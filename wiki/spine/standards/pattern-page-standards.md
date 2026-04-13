---
title: Pattern Page Standards
aliases:
  - "Pattern Page Standards"
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
  - id: exemplar
    type: wiki
    file: wiki/patterns/plan-execute-review-cycle.md
tags: [standards, pattern, page-type, quality, exemplar, evolved-page]
---

# Pattern Page Standards

## Summary

Standards for pattern pages — recurring structural phenomena observed across ≥2 independent instances. A pattern is NOT a best practice or a recommendation. It is something that RECURS — observed multiple times in different contexts — with identifiable conditions that make it appear and conditions where it fails. Pattern pages are Layer 5 evolved pages. They MUST have `instances` in frontmatter listing concrete occurrences with page references and context.

## Key Insights

1. **A pattern without instances is a hypothesis.** The `instances` frontmatter field is the structural proof. Each instance has `page` (where) and `context` (how). If you can't name ≥2 real instances, it's not a pattern yet — keep it as a concept until you find more occurrences.

2. **"When Not To" is as important as "When To Apply."** A pattern that supposedly works everywhere is not useful guidance. The quality of a pattern page is measured equally by its positive and negative boundary conditions.

3. **The pattern must be NAMED and RECOGNIZABLE.** The title is how people reference it in conversation: "we're doing SFIF," "this follows Plan-Execute-Review." If the title doesn't stick as a label, the pattern isn't crisp enough.

4. **Patterns are cross-domain by default.** A pattern observed in only one domain is a practice, not a pattern. The `domain` field should be `cross-domain` unless the pattern is genuinely domain-specific. Most real patterns cross boundaries.

## Deep Analysis

### Required Sections (from wiki-schema.yaml)

| Section | Purpose | Minimum |
|---------|---------|---------|
| **Summary** | What recurs and why it matters | 30 words |
| **Pattern Description** | What the pattern IS, how to recognize it | 100 words, mechanism explained |
| **Instances** | ≥2 concrete occurrences with wiki page references | 2 instances minimum, each with source + how |
| **When To Apply** | Conditions that make this pattern appropriate | Specific trigger conditions |
| **When Not To** | Conditions where it fails or is counterproductive | Equally thoughtful as When To Apply |
| **Relationships** | DERIVED FROM source pages + connections | ≥2 relationships |

### Required Frontmatter

| Field | Value | Why |
|-------|-------|-----|
| `type` | pattern | — |
| `layer` | 5 | Patterns are Layer 5 — above lessons, below decisions |
| `domain` | cross-domain (usually) | Patterns cross domain boundaries |
| `derived_from` | list of source pages | Where was convergence observed? |
| `instances` | list of `{page, context}` | Structural proof of recurrence |

### Section-by-Section Quality Bar

#### Summary

- State what RECURS (the structural phenomenon) and why it matters
- Include the pattern name as a recognizable label

**Good:** "Recurring structural pattern: Plan (deliberation) → Execute (action) → Review (verification) with mechanical enforcement at each boundary."

**Bad:** "A useful approach to organizing work." (not specific, no structural claim)

#### Pattern Description

- ≥100 words explaining the MECHANISM — why this pattern emerges
- If the pattern has stages/components, add a `> [!info]` reference card table
- If there's a core tradeoff, wrap in `> [!warning]`
- If there's a taxonomy (variants, modes), use `> [!abstract]` with a table

#### Instances

- ≥2 concrete instances, each referencing a wiki page
- Use `> [!example]-` foldable per instance for detailed breakdowns
- A summary table at the top is ideal: `| Instance | How It Implements |`
- Each instance must be independently verifiable — the reader can go read the source page

**Good:** "OpenFleet uses this pattern in its spec-to-code workflow. The Plan phase is CONVERSATION→ANALYSIS→INVESTIGATION. The Execute phase is REASONING→WORK. Review gates each transition."

**Bad:** "This appears in many projects." (WHICH projects?)

#### When To Apply / When Not To

- `> [!tip]` for positive conditions
- `> [!warning]` for negative conditions / anti-patterns
- Both sections should be equally detailed
- Name specific scenarios, not abstract categories

### The Gold-Standard Exemplar

> [!success] [[plan-execute-review-cycle|Plan Execute Review Cycle]] — 165 lines, 13 relationships
>
> **Why it's the standard:**
> - 4 detailed instances (OpenFleet, Harness Engineering, Claude Code, Research Pipeline) each showing the pattern differently
> - Enforcement strength insight: "weak = documented, strong = mechanically enforced" — a discovery, not just a description
> - "When Not To" is as detailed as "When To Apply": "rubber stamp review is worse than no review"
> - Pattern is self-demonstrating — the page's own structure follows Plan→Execute→Review
> - Nested granularity explained: the pattern applies at project, epic, task, and stage levels
>
> **The test:** After reading this page, could you recognize this pattern in a new system and decide whether to apply it? If yes, the pattern page succeeded.

### Annotated Exemplar: [[three-lines-of-defense-immune-system-for-agent-quality|Three Lines of Defense — Immune System for Agent Quality]]

> [!example]- Full Walkthrough — Why Each Section Works
>
> **Frontmatter annotations:**
> ```yaml
> instances:                           # ← REQUIRED for patterns — structural proof
>   - page: "Model: Quality and Failure Prevention"
>     context: "Three-layer defense model defined..."   # ← context explains HOW the instance shows the pattern
>   - page: "Infrastructure Enforcement Proves Instructions Fail"
>     context: "Structural prevention (Line 1) proven..." # ← each instance is a DIFFERENT manifestation
>   - page: "Agent Failure Taxonomy..."
>     context: "6 behavioral failure classes..."          # ← 3 instances > minimum 2
> ```
> 3 instances with specific context annotations. Each instance shows a DIFFERENT aspect of the pattern.
>
> **Summary annotation:**
> "AI agents are 'sick by default'..." — Contains the provocative frame (diseases), the 3-line structure (prevention/detection/correction), AND the key design principle (hidden from agents). All in 2 sentences.
>
> **Reference Card annotation:**
> `> [!info] Pattern Reference Card` — 5-column table mapping each component to its role, mechanism, and when it fires. A reader can USE the pattern from this table alone without reading further.
>
> **Pattern Description annotations:**
> - `> [!abstract] The Five Named Diseases` — TAXONOMY table. Each disease has: symptom + detection method. This is the MECHANISM — not "things go wrong" but "here are the 5 specific ways things go wrong and how you detect each."
> - Three Lines described with SPECIFIC mechanisms: Line 1 = tool blocking + contribution gates + verbatim anchoring. Line 2 = 4 detection functions every 30s. Line 3 = 4 graduated corrections (TEACH → COMPACT → PRUNE → ESCALATE).
> - `> [!warning]` for the correction ladder — communicates that this is a RISK AREA (corrections can be too aggressive).
>
> **Instance annotations:**
> - OpenFleet instance: `> [!example]-` foldable with FULL implementation details (746 lines, 3 files, doctor cycle, hidden from agents)
> - OpenArms instance: `> [!example]-` foldable showing a PARTIAL implementation (Line 1 only, no Lines 2-3) — contrasts with OpenFleet to show the SPECTRUM of pattern adoption
>
> **When To / When Not To annotations:**
> - When To: 5 specific conditions (not "when you need quality" but "multiple agents OR autonomous OR recurring failures")
> - When Not To: 4 specific conditions including "Solo human-supervised agent — the human IS the immune system" — shows the pattern has BOUNDARIES, not universal applicability

### Common Failures

| Failure | What It Looks Like | The Fix |
|---------|-------------------|---------|
| **Hypothesis not pattern** | 0-1 instances. "I think this recurs." | Find ≥2 real instances or keep as concept |
| **Lazy When Not To** | "Don't use when it doesn't apply" | Name specific failure conditions with evidence |
| **Single domain** | Pattern observed only in one project | Cross-reference other domains — or acknowledge it's a practice, not a pattern |
| **Description without mechanism** | "Things happen in this order" | Explain WHY they happen in this order |
| **Missing instances frontmatter** | `instances:` field absent or empty | Required field — the structural proof of the pattern |

### Content Thresholds (from artifact-types.yaml)

| Threshold | Value |
|-----------|-------|
| summary_min_words | 30 |
| pattern_description_min_words | 100 |
| min_relationships | 2 |
| min_instances | 2 |
| callouts_required | Yes |

### Template

`wiki/config/templates/pattern.md` — scaffold via `python3 -m tools.pipeline scaffold pattern "Title"`

## Relationships

- BUILDS ON: [[model-llm-wiki-standards|LLM Wiki Standards — What Good Looks Like]]
- RELATES TO: [[model-knowledge-evolution|Model — Knowledge Evolution]]
- RELATES TO: [[model-wiki-design|Model — Wiki Design]]
- FEEDS INTO: [[model-methodology-standards|Methodology Standards — What Good Execution Looks Like]]

## Backlinks

[[model-llm-wiki-standards|LLM Wiki Standards — What Good Looks Like]]
[[model-knowledge-evolution|Model — Knowledge Evolution]]
[[model-wiki-design|Model — Wiki Design]]
[[model-methodology-standards|Methodology Standards — What Good Execution Looks Like]]
