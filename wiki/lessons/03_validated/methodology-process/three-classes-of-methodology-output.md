---
title: Three Classes of Methodology Output
aliases:
  - "Three Classes of Methodology Output"
type: lesson
domain: cross-domain
layer: 4
status: synthesized
confidence: high
maturity: growing
derived_from:
  - "Methodology Artifact Taxonomy"
  - "Synthesis: Methodology Artifact Taxonomy — Full Spectrum Research"
  - "Construction and Testing Artifacts — Standards and Guide"
created: 2026-04-12
updated: 2026-04-12
last_reviewed: 2026-04-22
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

## Self-Check — Am I About to Make This Mistake?

> [!warning] Ask yourself BEFORE producing any artifact:
>
> 1. **What CLASS am I producing?** Document (constraining spec), Artifact (by-product), or Documentation (explaining)?
> 2. **Am I applying the RIGHT quality rules for this class?** A requirements spec needs binding FR/NFR/AC — not a nice summary.
> 3. **Am I treating a DOCUMENT as if it were documentation?** If I'm writing a "nice explanation" when I should be writing "binding constraints that agents must follow" — I'm misclassifying.
> 4. **Am I treating 15 different things as one thing?** If I'm putting 15 entries in one page instead of giving each its own proper treatment — I'm compressing different classes into one.

### How This Connects — Navigate From Here

> [!abstract] From This Lesson → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **What principle governs this?** | [[right-process-for-right-context-the-goldilocks-imperative|Principle — Right Process for Right Context — The Goldilocks Imperative]] |
> | **How does enforcement apply?** | [[infrastructure-over-instructions-for-process-enforcement|Principle — Infrastructure Over Instructions for Process Enforcement]] |
> | **How does structure help?** | [[structured-context-governs-agent-behavior-more-than-content|Principle — Structured Context Governs Agent Behavior More Than Content]] |
> | **What is my identity profile?** | [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]] |
> | **Where does this fit in the system?** | [[methodology-system-map|Methodology System Map]] — find any component |

## Relationships

- DERIVED FROM: [[methodology-artifact-taxonomy|Methodology Artifact Taxonomy]]
- DERIVED FROM: [[methodology-artifact-taxonomy-research|Synthesis — Methodology Artifact Taxonomy — Full Spectrum Research]]
- DERIVED FROM: [[construction-and-testing-artifacts|Construction and Testing Artifacts — Standards and Guide]]
- RELATES TO: [[model-methodology|Model — Methodology]]
- RELATES TO: [[stage-gate-methodology|Stage-Gate Methodology]]
- FEEDS INTO: [[model-methodology-standards|Methodology Standards — What Good Execution Looks Like]]

## Backlinks

[[methodology-artifact-taxonomy|Methodology Artifact Taxonomy]]
[[methodology-artifact-taxonomy-research|Synthesis — Methodology Artifact Taxonomy — Full Spectrum Research]]
[[construction-and-testing-artifacts|Construction and Testing Artifacts — Standards and Guide]]
[[model-methodology|Model — Methodology]]
[[stage-gate-methodology|Stage-Gate Methodology]]
[[model-methodology-standards|Methodology Standards — What Good Execution Looks Like]]
[[methodology-config-architecture|Methodology Config Architecture — How the Pieces Fit Together]]
