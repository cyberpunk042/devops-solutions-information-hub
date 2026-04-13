---
title: Lesson Page Standards
aliases:
  - "Lesson Page Standards"
type: concept
domain: cross-domain
layer: spine
status: synthesized
confidence: high
maturity: growing
created: 2026-04-11
updated: 2026-04-13
sources:
  - id: wiki-schema
    type: file
    file: wiki/config/wiki-schema.yaml
  - id: artifact-types
    type: file
    file: wiki/config/artifact-types.yaml
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

> [!success] [[cli-tools-beat-mcp-for-token-efficiency|CLI Tools Beat MCP for Token Efficiency]] — 122 lines, 9 relationships
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

### Annotated Exemplar: [[infrastructure-enforcement-proves-instructions-fail|Infrastructure Enforcement Proves Instructions Fail]]

> [!example]- Full Walkthrough — Why Each Section Works
>
> **Frontmatter annotations:**
> ```yaml
> type: lesson              # ← correct evolved type
> domain: ai-agents         # ← specific domain, not cross-domain (lesson is about agent enforcement)
> confidence: authoritative  # ← justified: quantified data from 5 production runs
> maturity: growing          # ← not seed: multiple evidence sources, not just one observation
> derived_from:              # ← REQUIRED: traces to source pages
>   - "CLAUDE.md Structural Patterns for Agent Compliance"
>   - "Enforcement Hook Patterns"
>   - "Model: Quality and Failure Prevention"
> sources:                   # ← each source has file: reference (not just description)
>   - id: openarms-v8-overnight
>     file: raw/articles/openarms-methodology-scan.md
> ```
>
> **Summary annotation:**
> "Instruction-based agent enforcement achieves 25% compliance for stage boundaries. Infrastructure enforcement achieves 100% compliance for the same rules."
> ← ONE actionable sentence. Contains the specific numbers. After reading ONLY this line, you know what to do (switch from instructions to infrastructure).
>
> **Context annotation:**
> 4 specific trigger conditions — each is a concrete scenario, not a vague category:
> - "You are configuring an AI agent to follow a process" ← specific
> - "You are writing rules in CLAUDE.md and expecting compliance" ← specific
> - "You are running agents autonomously" ← specific
> - "You have experienced agents ignoring directives" ← specific trigger
>
> **Insight annotation:**
> Uses `> [!tip]` callout (success-oriented lesson). Contains a 5-row TABLE inside `> [!abstract]` showing the enforcement hierarchy with measured compliance per level. This is the MECHANISM — not "hooks work" but "hooks work because they operate at the tool-call level where the agent physically cannot bypass them."
>
> **Evidence annotation:**
> 3 evidence items from independent instances:
> - `> [!bug]-` foldable: OpenArms v8 overnight (quantified: 75% violations)
> - `> [!bug]-` foldable: Fatigue cliff pattern (different failure mode, same root cause)
> - `> [!success]`: OpenArms v10 hooks (quantified: 0% violations, 215 lines)
> - `> [!success]`: OpenFleet MCP tool blocking (independent instance, different mechanism)
>
> Each evidence item has: bold label, specific claim with DATA, source reference.
>
> **Applicability annotation:**
> Uses `> [!abstract]` table mapping 4 enforcement tiers to when/what. Includes "When to upgrade" guidance. Self-Check section with 4 numbered questions — each question is testable and specific.
>
> **Relationships annotation:**
> 7 relationships using 4 different verbs (DERIVED FROM, BUILDS ON, RELATES TO, FEEDS INTO). Not all RELATES TO — verb choice carries meaning.

### Second Exemplar Reference: [[agent-failure-taxonomy-seven-classes-of-behavioral-failure|Agent Failure Taxonomy — Seven Classes of Behavioral Failure]]

> [!success] Why this exemplar works
>
> - **Taxonomy in the insight:** 6-row table with columns: class name, what happens, root cause, infrastructure fix? ← each class is a complete unit
> - **Evidence per class:** Separate `> [!bug]-` foldable for each failure class with file:line-level specifics
> - **Quantified assertion:** "Clean completion rate: 20%" — not "sometimes fails" but a measured percentage
> - **Connects to prior art:** BUILDS ON [[infrastructure-enforcement-proves-instructions-fail|Infrastructure Enforcement Proves Instructions Fail]] — explicitly says "even with 0% stage violations, these 6 classes persist"
> - **Mitigation table in applicability:** Each class → how to detect + how to mitigate

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

`wiki/config/templates/lesson.md` — scaffold via `python3 -m tools.pipeline scaffold lesson "Title"`

## Open Questions

> [!question] ~~Should lessons with <3 evidence items be automatically flagged for demotion to "observation" status?~~
> **RESOLVED:** No automatic demotion. Flag for review. 2 strong evidence items > 3 weak ones. Threshold is a guideline, not a gate. (Requires: design decision on observation vs lesson threshold)

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **Model these standards serve** | [[model-knowledge-evolution|Model — Knowledge Evolution]] |
> | **Global wiki standards** | [[model-llm-wiki-standards|LLM Wiki Standards — What Good Looks Like]] |
> | **Template for this type** | `wiki/config/templates/lesson.md` |
> | **System map** | [[methodology-system-map|Methodology System Map]] |
> | **Learning path** | [[methodology-fundamentals|Learning Path — Methodology Fundamentals]] |

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
[[deployment-closure-monitoring-artifacts|Deployment, Closure, and Monitoring Artifacts — Standards and Guide]]
