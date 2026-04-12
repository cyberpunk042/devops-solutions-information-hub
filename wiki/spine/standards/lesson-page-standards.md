---
title: "Lesson Page Standards"
type: concept
domain: cross-domain
layer: spine
status: synthesized
confidence: high
maturity: seed
created: 2026-04-11
updated: 2026-04-11
sources:
  - id: wiki-schema
    type: file
    file: config/wiki-schema.yaml
  - id: artifact-types
    type: file
    file: config/artifact-types.yaml
  - id: exemplar
    type: wiki
    file: wiki/lessons/cli-tools-beat-mcp-for-token-efficiency.md
tags: [standards, lesson, page-type, quality, exemplar, evolved-page]
---

# Lesson Page Standards

## Summary

Standards for lesson pages — actionable learnings distilled from convergent evidence across multiple sources. A lesson is NOT an opinion or an observation. It is a pattern of failure or success that has been seen ≥3 times, explains WHY it happens (mechanism), and tells the reader WHEN it applies and when it doesn't. Lesson pages are Layer 4 evolved pages — they MUST have `derived_from` linking to the source pages they distill from.

## Key Insights

1. **A lesson explains the MECHANISM, not just the observation.** "CLI beats MCP" is an observation. "CLI beats MCP because unused MCP tool schemas consume context tokens that displace task-relevant content" is a lesson. The mechanism is what makes it transferable to new situations.

2. **Evidence must be convergent — ≥3 independent data points.** A lesson with one source is an anecdote. A lesson with two sources is a coincidence. Three or more independent sources showing the same pattern is evidence. The Evidence section must show this convergence explicitly.

3. **Applicability must have boundaries.** A lesson that "applies everywhere" is useless. The Applicability section must name specific domains WHERE it applies AND situations where it DOESN'T. The "When Not To" is as important as the "When To."

4. **Styling is required for lessons.** Insight gets `> [!warning]` or `> [!tip]`. Evidence failures get `> [!bug]-` (foldable). Validated approaches get `> [!success]`. This isn't decoration — it's semantic: the callout type tells the reader what KIND of evidence this is.

## Deep Analysis

### Required Sections (from wiki-schema.yaml)

| Section | Purpose | Minimum |
|---------|---------|---------|
| **Summary** | The lesson in 1-2 sentences, immediately actionable | 30 words |
| **Context** | When and where this lesson applies. Trigger conditions. | ≥3 specific trigger conditions |
| **Insight** | The core learning — the MECHANISM (why), not just the observation (what) | 50 words, in a `> [!warning]` or `> [!tip]` callout |
| **Evidence** | Convergent data from derived_from pages. Each item: source + specific claim + data | ≥3 independent evidence items |
| **Applicability** | Which domains benefit AND where this lesson doesn't apply | Table or bulleted list with both positive and negative cases |
| **Relationships** | At least DERIVED FROM links to source pages | ≥2 (DERIVED FROM + at least one other verb) |

### Required Frontmatter

| Field | Value | Why |
|-------|-------|-----|
| `type` | lesson | — |
| `layer` | 4 | Lessons are Layer 4 in the knowledge evolution hierarchy |
| `derived_from` | list of source page titles | Provenance — where was this distilled from? |
| `maturity` | seed (initially) | Grows via evidence accumulation |

### Section-by-Section Quality Bar

#### Summary

- ONE sentence stating the lesson as an actionable rule
- A reader should know WHAT TO DO after reading only the summary

**Good:** "CLI tools paired with skill files consistently outperform MCP server integrations on token cost and output accuracy."

**Bad:** "There are trade-offs between CLI and MCP approaches." (vague, not actionable)

#### Context

- List ≥3 specific trigger conditions — when does this lesson activate?
- Each trigger is a concrete scenario, not a vague category

**Good:** "Debugging unexplained hallucinations in agent output and looking for root causes beyond prompt quality"

**Bad:** "When working with agents" (too broad, not a trigger)

#### Insight

- MUST be wrapped in `> [!warning]` (for lessons about failures/risks) or `> [!tip]` (for lessons about successes/approaches)
- Explain the MECHANISM — WHY this happens
- If there's a comparison or taxonomy, add a table inside `> [!abstract]`

**Good:**
```markdown
> [!warning] Context Pollution
> Unused MCP tool schemas occupy context tokens that could hold task-relevant content.
> This is "context pollution" — high-entropy JSON boilerplate displacing high-signal task context.
```

**Bad:** "MCP has higher costs than CLI." (observation without mechanism)

#### Evidence

- ≥3 independent evidence items from different sources
- Each item has: **bold source label** + specific claim with data + `(source parenthetical)`
- Use `> [!bug]-` foldable for failure incidents with verbatim operator quotes
- Use `> [!success]` for validated approaches

**Good:**
```markdown
- **Harness Engineering comparison**: CLI was both cheaper and more accurate
  for the same filesystem operations. 12x cost differential. (src-harness-engineering)
```

**Bad:** "Several sources confirm this." (no specifics, no data, no sourcing)

#### Applicability

- Name specific domains where the lesson applies
- Include a "When this lesson does NOT apply" section or counterexamples
- If multiple domains, use a table: `| Domain | How It Applies |`

### The Gold-Standard Exemplar

> [!success] [[CLI Tools Beat MCP for Token Efficiency]] — 122 lines, 9 relationships
>
> **Why it's the standard:**
> - Summary: ONE actionable sentence
> - Context: 5 specific trigger conditions
> - Insight: explains the MECHANISM (context pollution) in `> [!warning]` callout
> - Evidence: 8 items from 4 independent sources, each with bold label + data + sourcing
> - Applicability: 4 domains named + "When MCP is still right" with 4 counterexamples
> - Uses CONTRADICTS relationship — explicitly challenges the default assumption
>
> **The test:** After reading this lesson, could you decide between CLI and MCP for your next tool integration? If yes, the lesson succeeded. If you'd need to read the sources yourself, it failed.

### Common Failures

| Failure | What It Looks Like | The Fix |
|---------|-------------------|---------|
| **Observation not lesson** | "We noticed X happens" | Explain WHY X happens (the mechanism) |
| **Single-source** | One anecdote presented as universal truth | Need ≥3 independent sources showing same pattern |
| **No boundaries** | "This applies everywhere" | Name where it DOESN'T apply — counterexamples |
| **Missing styling** | Plain prose Insight section | Wrap in `> [!warning]` or `> [!tip]` — semantic callouts are required |
| **Vague evidence** | "Sources confirm this" | Name each source, state the specific claim, include data |
| **No derived_from** | Lesson appears from nowhere | Must link to source pages in frontmatter |

### Content Thresholds (from artifact-types.yaml)

| Threshold | Value |
|-----------|-------|
| summary_min_words | 30 |
| insight_min_words | 50 |
| min_relationships | 2 |
| min_evidence_items | 3 |
| callouts_required | Yes |

### Template

`config/templates/lesson.md` — scaffold via `python3 -m tools.pipeline scaffold lesson "Title"`

## Open Questions

> [!question] Should lessons with <3 evidence items be automatically flagged for demotion to "observation" status? (Requires: design decision on observation vs lesson threshold)

## Relationships

- BUILDS ON: [[Model: LLM Wiki Standards — What Good Looks Like]]
- RELATES TO: [[Model: Knowledge Evolution]]
- RELATES TO: [[Model: Wiki Design]]
- FEEDS INTO: [[Model: Methodology Standards — What Good Execution Looks Like]]

## Backlinks

[[Model: LLM Wiki Standards — What Good Looks Like]]
[[Model: Knowledge Evolution]]
[[Model: Wiki Design]]
[[Model: Methodology Standards — What Good Execution Looks Like]]
