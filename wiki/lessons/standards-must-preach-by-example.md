---
title: "Standards Must Preach by Example"
type: lesson
domain: cross-domain
layer: 4
status: synthesized
confidence: authoritative
maturity: seed
derived_from:
  - "The Agent Must Practice What It Documents"
  - "Wiki Design Standards — What Good Styling Looks Like"
created: 2026-04-10
updated: 2026-04-10
sources:
  - id: directive-preach-by-example
    type: log
    file: wiki/log/2026-04-09-directive-record-process-skills-supermodel.md
    title: "Record the Process — Skills, Super-Model, Preach by Example"
    ingested: 2026-04-09
tags: [lesson, standards, self-referential, quality, integrity, example]
---

# Standards Must Preach by Example

## Summary

Every model page and standards page must itself follow the standards it defines. The Wiki Design Standards page must demonstrate every callout technique it documents. The Methodology model must follow the methodology it describes. The LLM Wiki model must pass its own quality gates. Self-referential integrity is not vanity — it is the proof that the standard works. A standard that can't be applied to itself is either too strict or not understood.

## Context

This lesson applies whenever creating standards, style guides, quality gates, or best-practice documentation. The triggering signal: a standards document that violates its own rules. If the callout standards page has no callouts, it fails its own test.

## Insight

> [!warning] The self-referential integrity test
>
> | Standard | Must Demonstrate |
> |----------|-----------------|
> | Wiki Design Standards | Every callout type, progressive disclosure, emphasis hierarchy |
> | Model: Methodology | Stage gates applied to its own creation (Document → Design → Implement → Test) |
> | LLM Wiki model | Valid frontmatter, ≥30 word summary, ≥1 relationship, source provenance |
> | Quality Standards | Anti-patterns gallery where the page itself avoids every listed anti-pattern |
> | Naming conventions | The page about naming conventions has a properly-named filename |

A standard that exists only as text is an ASPIRATION. A standard that demonstrates itself is PROOF that the standard is achievable. The Wiki Design Standards page was rewritten specifically to be self-referential — it uses every technique it describes, making it simultaneously documentation and proof-of-concept.

> [!tip] The process must also be recorded as skills
> The operator's directive extended beyond self-referential pages to self-referential tooling: the model-building process should become a skill (`/build-model`), the evolution process should become a skill (`/evolve`), the review process should become a skill (`/review`). This way the second brain naturally evolves — the process of building knowledge is itself captured as knowledge.

## Evidence

**Date:** 2026-04-09

**The operator's directive:** "models and standards document with proper examples too and that prove that they respect what they are themselves meant to instaure. preach by example."

**The implementation:** Wiki Design Standards was rewritten as a 454-line self-referential showcase — it demonstrates every technique it documents. The model-builder skill was created with a Styling Standards section that it itself follows. The Methodology model was built using the methodology it describes.

**Source:** `wiki/log/2026-04-09-directive-record-process-skills-supermodel.md`

## Applicability

- **Standards pages**: every standards page must pass its own quality bar
- **Style guides**: a style guide written in ugly formatting is self-defeating
- **CI/CD configuration**: a CI pipeline that doesn't run its own tests is untested infrastructure
- **Teaching materials**: a tutorial about clean code written in messy code teaches the wrong thing
- **Skills**: the skill that teaches model-building should itself be a well-built skill

> [!abstract] The general principle
> The highest-quality proof that a standard works is an artifact that follows it. Ship the standard AND the example as one artifact wherever possible.

## Relationships

- DERIVED FROM: [[The Agent Must Practice What It Documents]]
- RELATES TO: [[Wiki Design Standards — What Good Styling Looks Like]]
- RELATES TO: [[Model: Methodology]]
- FEEDS INTO: [[Model: Quality and Failure Prevention]]

## Backlinks

[[The Agent Must Practice What It Documents]]
[[Wiki Design Standards — What Good Styling Looks Like]]
[[Model: Methodology]]
[[Model: Quality and Failure Prevention]]
