---
title: "Three Classes of Methodology Output"
type: lesson
domain: cross-domain
layer: 4
status: synthesized
confidence: high
maturity: seed
derived_from:
  - "Methodology Artifact Taxonomy"
  - "Synthesis: Methodology Artifact Taxonomy — Full Spectrum Research"
  - "Construction and Testing Artifacts — Standards and Guide"
created: 2026-04-12
updated: 2026-04-12
sources: []
tags: [methodology, artifacts, documents, documentation, taxonomy, lesson]
---

# Three Classes of Methodology Output

## Summary

Methodology execution produces three fundamentally different classes of output — artifacts, documents, and documentation — each with different quality standards, audiences, lifecycles, and purposes. Conflating them (treating everything as "a wiki page" or "a file") produces the wrong quality bars and the wrong validation rules. This lesson was learned when an entire methodology standards initiative produced 37 files that were all called "crap" — because documents that should have been constraining specifications were treated as knowledge pages, and artifacts that should have been validated against gate commands were treated as prose.

## Context

This lesson applies when:
- Designing a methodology artifact system for any project
- Defining quality standards for different output types
- Building validation tooling that checks the right things for the right types
- An agent is producing methodology outputs and needs to know WHICH class it's creating
- A team is confused about why their "documentation" doesn't prevent implementation mistakes (it's not a DOCUMENT — it's documentation)

## Insight

> [!warning] Three Classes, Three Different Quality Rules
>
> | Class | What It Is | Purpose | Quality Rule | Lifecycle |
> |-------|-----------|---------|-------------|-----------|
> | **Artifact** | Tangible by-product of work | Produced as SIDE EFFECT | Must exist, must be valid | Created → used → replaced |
> | **Document** | Written specification with formal structure | Created to CONSTRAIN future work | Must be binding, complete, verifiable | Draft → active → approved → superseded |
> | **Documentation** | Explanatory material | Created to EXPLAIN what exists | Must be accurate, findable, maintainable | Created → updated → retired |
>
> A Test Plan (document) constrains how tests are written. A Test Result (artifact) is produced by running tests. A Testing Guide (documentation) explains how to test. Applying document-quality rules to an artifact is overhead. Applying artifact-quality rules to a document is insufficient. Applying documentation-quality rules to either misses the point entirely.

> [!abstract] The Misclassification Failure Pattern
>
> | What Happened | The Mistake | What Should Have Happened |
> |---------------|-----------|--------------------------|
> | Requirements spec written as a wiki concept page | Treated as documentation (explain) instead of document (constrain) | Requirements spec is a DOCUMENT — it must have FR/NFR/AC that agents read as binding constraints |
> | Config files produced without explanation pages | Treated as artifacts (produce) without documentation (explain) | Config files need companion wiki pages explaining WHY the config is shaped that way |
> | Per-type standards written as table rows in one page | Treated as one document instead of 15 separate documents | Each type needs its OWN standards document with section-by-section quality bars |

## Evidence

> [!bug]- Failure: 37 Files Called "Crap"
> The methodology standards initiative produced 37 files in one sprint — templates, config files, wiki pages, pattern pages. The operator's feedback: "HARDCODED, LOW MD QUALITY, DISCONNECTED, WRONGLY NAMED, WRONGLY CLASSIFIED, WRONGLY ANNOTATED, WRONG ON ALMOST EVERY POINT." Root cause: everything was treated as the same class of output (wiki pages to produce), when the operator was asking for three different things: specifications that CONSTRAIN (documents), config files that WORK (artifacts), and wiki pages that EXPLAIN (documentation).

> [!success] Recovery: Research-First Approach
> After the restart, online research revealed the real-world SDLC has 78+ artifact types across 11 categories. The three-class distinction emerged from industry taxonomy (Wikipedia, sdlcforms.com, GeeksforGeeks all distinguish artifacts from documents from documentation). Applying this distinction to the wiki's needs clarified: config files ARE artifacts (validate them with gate commands), methodology specs ARE documents (enforce them as binding constraints), wiki knowledge pages ARE documentation (make them accurate and findable).

> [!success] Evidence from OpenArms
> OpenArms's methodology-document-chain.md (846 lines) implicitly follows the three-class distinction: wiki pages in wiki/domains/ are documents (constraining), source files in src/ are artifacts (validated by pnpm tsgo), and the agent-directive.md is documentation (explaining how to follow the methodology). The chain works BECAUSE each class is validated differently.

## Applicability

| Domain | How This Lesson Applies |
|--------|----------------------|
| **Any methodology system** | Must classify every output as artifact, document, or documentation — then apply the right quality rules per class |
| **Wiki/knowledge projects** | Wiki pages can be any of the three classes — a concept page explaining something is documentation, a requirements spec is a document, a manifest.json is an artifact. Same medium, different classes. |
| **AI agent workflows** | Agents must know which class they're producing to apply the right quality standard. An agent writing a requirements spec should follow document standards (binding, complete, verifiable), not documentation standards (accurate, findable). |
| **Validation tooling** | Different validation per class: artifacts → gate commands (does it compile?), documents → structural checks (are all required sections present?), documentation → accuracy checks (does it match the code?) |

> [!tip] When This Lesson Does NOT Apply
>
> Small projects where one person does everything may not need formal class distinction — the same person writes the spec, builds the code, and writes the docs. The distinction matters when: (a) agents follow specs as binding constraints, (b) validation tooling checks different things for different types, (c) multiple people/agents produce different types and need to know what quality bar applies.

## Relationships

- DERIVED FROM: [[Methodology Artifact Taxonomy]]
- DERIVED FROM: [[Synthesis: Methodology Artifact Taxonomy — Full Spectrum Research]]
- DERIVED FROM: [[Construction and Testing Artifacts — Standards and Guide]]
- RELATES TO: [[Model: Methodology]]
- RELATES TO: [[Stage-Gate Methodology]]
- FEEDS INTO: [[Model: Methodology Standards — What Good Execution Looks Like]]

## Backlinks

[[Methodology Artifact Taxonomy]]
[[Synthesis: Methodology Artifact Taxonomy — Full Spectrum Research]]
[[Construction and Testing Artifacts — Standards and Guide]]
[[Model: Methodology]]
[[Stage-Gate Methodology]]
[[Model: Methodology Standards — What Good Execution Looks Like]]
