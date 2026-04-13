---
title: "Decision Page Standards"
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
    file: wiki/decisions/execution-mode-edge-cases.md
tags: [standards, decision, page-type, quality, exemplar, evolved-page]
---

# Decision Page Standards

## Summary

Standards for decision pages — the highest-layer evolved page type (Layer 6). A decision resolves an open question with a concrete recommendation backed by evidence, rejected alternatives, and an honest reversibility assessment. Every decision must have ≥2 alternatives with specific rejection rationale. The `reversibility` frontmatter field is required — it forces cost-of-wrong assessment before committing.

## Key Insights

1. **A decision is ONE clear statement, not a discussion.** The Decision section should be readable in 10 seconds: "Do X. Use Y for Z." Everything else (alternatives, rationale, evidence) supports that statement.

2. **Alternatives must be REJECTED with reasons, not just listed.** "We considered Option B" is not an alternative analysis. "We rejected Option B because it requires N and we don't have N" IS. The rejection reason is the insight.

3. **Reversibility is a required field because it forces intellectual honesty.** Claiming `reversibility: easy` when reversal would require refactoring 5 files is dishonest. The reversibility assessment tells future readers the cost of changing course.

4. **Decisions resolve open questions — they should link back.** Every decision should trace to specific `> [!question]` entries on other pages. After the decision is made, those open questions get marked as resolved with a reference to the decision.

## Deep Analysis

### Required Sections (from wiki-schema.yaml)

| Section | Purpose | Minimum |
|---------|---------|---------|
| **Summary** | The decision + recommendation in 2-3 sentences | 30 words |
| **Decision** | The clear statement of what to do | `> [!success]` callout with scenario-action table |
| **Alternatives** | ≥2 rejected options with specific rejection reasons | 2 alternatives minimum |
| **Rationale** | Why this choice, backed by evidence | 100 words, references derived_from |
| **Reversibility** | How hard to undo, downstream impact | Honest assessment matching frontmatter field |
| **Dependencies** | What this decision affects | Other decisions, systems, pages impacted |
| **Relationships** | DERIVED FROM + connections | ≥2 relationships |

### Required Frontmatter

| Field | Value | Why |
|-------|-------|-----|
| `type` | decision | — |
| `layer` | 6 | Decisions are the highest evolved layer |
| `reversibility` | easy / moderate / hard / irreversible | Forces cost-of-wrong assessment |
| `derived_from` | list of source pages | What evidence was this decided from? |

### Section-by-Section Quality Bar

#### Decision

- Wrap in `> [!success]` callout
- Include a scenario-action table when multiple scenarios exist:
  ```
  > [!success] Decision
  > | Scenario | Action |
  > |----------|--------|
  > | Default case | Do X |
  > | Edge case | Do Y instead |
  ```
- ONE clear statement. Not "we should consider..." — "Do X."

#### Alternatives

- ≥2 alternatives, each as a `###` subsection
- Each alternative gets `> [!warning]` explaining why it was rejected
- The rejection must be SPECIFIC — not "we preferred the other option"

**Good:** "Rejected because hard-kill on cost limit would leave partial commits in the audit trail, corrupting stage-gate tracking."

**Bad:** "We didn't choose this option." (no reason)

#### Rationale

- ≥100 words of evidence-backed reasoning
- Reference specific data, pages, incidents
- The rationale should be compelling enough that a reader who disagreed would change their mind

#### Reversibility

- Must match the `reversibility:` frontmatter value
- Explain what reversal COSTS — not just "it's possible"
- Name downstream impacts: what other decisions, systems, or pages would need to change

### The Gold-Standard Exemplar

> [!success] [[Execution Mode Edge Cases]] — 113 lines, 9 relationships
>
> **Why it's the standard:**
> - Decision section uses `> [!success]` with clear scenario-action table
> - "Finish the stage, then stop" cost-limit decision shows excellent reasoning: partial commits corrupt audit trail
> - Log format decision (structured YAML + prose) solves both queryability and readability
> - N/A gates via frontmatter declaration is an elegant solution with clear rationale
> - Every decision has explicit cost-benefit reasoning
> - `> [!tip]` for positive guidance, `> [!warning]` for rejected alternatives
>
> Also strong: [[Methodology Framework Design Decisions]] — resolves 7 open questions with nuanced mid-execution model change reasoning.

### Annotated Exemplar: [[Decision: When to Use Milestone vs Epic vs Module vs Task]]

> [!example]- Full Walkthrough — Why Each Section Works
>
> **Decision section annotation:**
> `> [!success]` callout with a 7-row scenario-action table. Each row: "You have X" → duration → design needed? → review scope → "Use Y." The reader can find their situation in the table and get the answer WITHOUT reading the rest of the page. This is the hallmark of a good decision page — the decision is IMMEDIATELY actionable.
>
> **Critical decomposition test annotation:**
> `> [!warning]` callout with two specific tests: "If a task needs both design AND implementation, it's a MODULE" and "If an epic has no modules and >5 tasks, decompose." These are the FAILURE MODE detectors — not just "how to choose" but "how to know you chose wrong."
>
> **Alternatives annotation:**
> 3 alternatives, each with `> [!warning] Rejected:` explaining the specific reason. Not "we didn't like it" but "flat lists lose coordination," "7 levels is over-process for current scale," "single field hides the failure mode." Evidence-backed rejection.
>
> **Rationale annotation:**
> 4 numbered points, one per hierarchy level, each explaining the DESIGN BOUNDARY that justifies that level's existence. Milestones = delivery coordination. Epics = acceptance criteria. Modules = design decisions. Tasks = execution. The rationale explains the MECHANISM, not just the preference.
>
> **Reversibility annotation:**
> Honest — "easy to reverse" because it's organizational, not structural. Changing levels = frontmatter change + reorganization, not code changes. This honesty is critical — see the "dishonest reversibility" anti-pattern below.

### Common Failures

| Failure | What It Looks Like | The Fix |
|---------|-------------------|---------|
| **Discussion not decision** | "There are pros and cons to both approaches..." | State the decision. "Do X." Then explain why. |
| **No alternatives** | Decision presented without rejected options | ≥2 alternatives with specific rejection reasons |
| **Dishonest reversibility** | `reversibility: easy` for a decision affecting 5 systems | Be honest. If reversal is hard, say so. |
| **Vague rationale** | "This seemed like the best approach" | Reference specific evidence, data, incidents |
| **Orphaned decision** | Decision exists but open questions on source pages not updated | Mark resolved OQs on source pages with link to decision |

### Content Thresholds (from artifact-types.yaml)

| Threshold | Value |
|-----------|-------|
| summary_min_words | 30 |
| rationale_min_words | 100 |
| min_relationships | 2 |
| min_alternatives | 2 |
| callouts_required | Yes |

### Template

`wiki/config/templates/decision.md` — scaffold via `python3 -m tools.pipeline scaffold decision "Title"`

## Relationships

- BUILDS ON: [[LLM Wiki Standards — What Good Looks Like]]
- RELATES TO: [[Model: Knowledge Evolution]]
- RELATES TO: [[Model: Wiki Design]]
- FEEDS INTO: [[Methodology Standards — What Good Execution Looks Like]]

## Backlinks

[[LLM Wiki Standards — What Good Looks Like]]
[[Model: Knowledge Evolution]]
[[Model: Wiki Design]]
[[Methodology Standards — What Good Execution Looks Like]]
[[Requirements and Design Artifacts — Standards and Guide]]
