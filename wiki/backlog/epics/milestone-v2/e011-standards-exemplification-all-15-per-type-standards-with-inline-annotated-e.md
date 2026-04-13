---
title: E011 — Standards Exemplification — All 15 Per-Type Standards with Inline Annotated Exemplars
aliases:
  - "E011 — Standards Exemplification — All 15 Per-Type Standards with Inline Annotated Exemplars"
  - "E011 — Standards Exemplification: All 15 Per-Type Standards with Inline Annotated Exemplars"
type: epic
domain: backlog
status: draft
priority: P0
task_type: epic
current_stage: document
readiness: 75
progress: 80
stages_completed:
artifacts:
  - "raw/notes/2026-04-12-documentation-standards-directive.md"
  - "wiki/domains/cross-domain/second-brain-integration-requirements.md"
confidence: high
created: 2026-04-12
updated: 2026-04-13
sources:
  - id: milestone
    type: file
    file: wiki/backlog/milestones/second-brain-complete-system-v2-0.md
  - id: documentation-standards
    type: directive
    file: raw/notes/2026-04-12-documentation-standards-directive.md
  - id: requirements
    type: file
    file: wiki/domains/cross-domain/second-brain-integration-requirements.md
tags: [epic, standards, exemplars, quality, v2, milestone-v2]
---

# E011 — Standards Exemplification — All 15 Per-Type Standards with Inline Annotated Exemplars
## Summary

Transform every per-type standards page from "rules with a reference to an exemplar" into "rules DEMONSTRATED with an inline annotated walkthrough." Currently 3 of 15 standards have inline annotations (lesson, pattern, decision). The remaining 12 reference exemplars but don't show WHY each part of the exemplar is good. The distinction matters: a standard that says "Evidence section must have ≥3 items" is a rule. A standard that shows a REAL Evidence section with annotations ("← this works because each item has bold source + specific data + source reference") teaches by example. Preach by example means the standard page itself IS the example.

## Operator Directive

> "we need to establish standards for everything with example of document on top of the standards documents for each artifact type"

> "We will also need proper example of artifacts not just unfinished standards with no examples and no real strong templates."

> "do not confuse everything. the words are important. goldilock is not model and model is not standard and standard is not example and example is not template and none of this is knowledge but knowledge is at all their layers."

> "Preach by example."

## Goals

- Every per-type standards page has at least ONE inline annotated exemplar walkthrough
- Each annotation explains WHY the exemplar element is good — not just WHAT it is
- Annotations reference the specific quality bar from the standards page (closes the loop)
- Where possible, use exemplars from the 2026-04-12 session's new pages (they demonstrate current best practices)
- Each standards page's "Common Failures" table is updated with failures observed the 2026-04-12 session
- Standards pages are self-validating: the page itself passes the quality bar it defines

## Done When

- [ ] `wiki/spine/standards/concept-page-standards.md` — has inline annotated exemplar
- [ ] `wiki/spine/standards/source-synthesis-page-standards.md` — has inline annotated exemplar
- [ ] `wiki/spine/standards/comparison-page-standards.md` — has inline annotated exemplar
- [ ] `wiki/spine/standards/reference-page-standards.md` — has inline annotated exemplar
- [ ] `wiki/spine/standards/deep-dive-page-standards.md` — has inline annotated exemplar
- [ ] `wiki/spine/standards/lesson-page-standards.md` — ALREADY HAS (verify still current)
- [ ] `wiki/spine/standards/pattern-page-standards.md` — ALREADY HAS (verify still current)
- [ ] `wiki/spine/standards/decision-page-standards.md` — ALREADY HAS (verify still current)
- [ ] `wiki/spine/standards/domain-overview-page-standards.md` — has inline annotated exemplar
- [ ] `wiki/spine/standards/evolution-page-standards.md` — has inline annotated exemplar
- [ ] `wiki/spine/standards/learning-path-page-standards.md` — has inline annotated exemplar
- [ ] `wiki/spine/standards/operations-plan-page-standards.md` — has inline annotated exemplar
- [ ] `wiki/spine/standards/epic-page-standards.md` — has inline annotated exemplar (use E010 as exemplar — it demonstrates the standard)
- [ ] `wiki/spine/standards/task-page-standards.md` — has inline annotated exemplar
- [ ] `wiki/spine/standards/note-page-standards.md` — has inline annotated exemplar
- [ ] Each annotation has ≥5 annotation points (frontmatter, summary, key sections, evidence, relationships)
- [ ] `pipeline post` returns 0 errors, 0 lint issues
- [ ] Operator confirms: each standards page teaches through its exemplar, not just lists rules

## Scale and Model

> [!info] Epic Parameters
>
> | Parameter | Value |
> |-----------|-------|
> | **Model** | knowledge-evolution (document → implement) |
> | **Quality tier** | Skyscraper — each standard gets FULL attention |
> | **Estimated modules** | 2 (existing 3 to verify + 12 new annotations) |
> | **Estimated tasks** | 15-18 |
> | **Dependencies** | E010 (Models must be current — standards reference models) |

## Stage Artifacts

> [!abstract] Stage → Artifact Map
>
> | Stage | Required Artifacts |
> |-------|-------------------|
> | Document | THIS epic page (done). Gap analysis: which standards have exemplars, which don't, which exemplars to use per standard. |
> | Implement | Updated standards pages (15). Each update adds the annotated exemplar section. |
> | Validation | `pipeline post` passes. Operator reviews each annotation for teaching quality. |

## Module Breakdown

### M1: Verify Existing Annotations (3 tasks)

The 3 standards with existing inline annotations need verification — are they still current after the 2026-04-12 session changes?

| Task | Standards Page | Current Exemplar | Check |
|------|--------------|-----------------|-------|
| T-E011-01 | Lesson Page Standards | Infrastructure Enforcement + Agent Failure Taxonomy | Verify annotations reference current content (we deepened both pages) |
| T-E011-02 | Pattern Page Standards | Three Lines of Defense | Verify annotations match current page structure |
| T-E011-03 | Decision Page Standards | When to Use Milestone vs Epic vs Module vs Task | Verify annotations match current page content |

### M2: Create New Annotations (12 tasks)

Each task: read the exemplar page FULLY, write the annotated walkthrough section, verify annotations reference the specific quality bars from the standards page.

| Task | Standards Page | Recommended Exemplar | Why This Exemplar |
|------|--------------|---------------------|-------------------|
| T-E011-04 | Concept Page Standards | [[sdlc-customization-framework|SDLC Customization Framework — Phases, Scale, and Chain Selection]] or [[readiness-vs-progress|Readiness vs Progress — Two-Dimensional Work Tracking]] | Both are session products demonstrating current best practices |
| T-E011-05 | Source-Synthesis Standards | [[src-openarms-v10-enforcement|Synthesis — OpenArms v10 — Infrastructure Enforcement and Agent Behavior]] | Real source synthesis with 11 key insights, deep analysis, specific data |
| T-E011-06 | Comparison Standards | [[openarms-vs-openfleet-enforcement|OpenArms vs OpenFleet Enforcement Architecture]] | Session product with comparison matrix, per-alternative analysis, recommendation |
| T-E011-07 | Reference Standards | [[frontmatter-field-reference|Frontmatter Field Reference — Complete Parameter Documentation]] | Complete reference with lookup tables, automation enablement column |
| T-E011-08 | Deep-Dive Standards | [[methodology-adoption-guide|Methodology Adoption Guide]] | 325+ lines, multiple callout types, progressive disclosure |
| T-E011-09 | Domain Overview Standards | One of the 7 domain overviews (pick the most complete) | Coverage assessment, maturity map, specific gaps |
| T-E011-10 | Evolution Standards | [[methodology-evolution-history|Evolution — Methodology System]] | Timeline with significance, key shifts, current state |
| T-E011-11 | Learning Path Standards | [[methodology-fundamentals|Learning Path — Methodology Fundamentals]] | 30 pages in 8 parts, testable outcomes |
| T-E011-12 | Operations Plan Standards | [[second-brain-integration-chain|Operations Plan — Second Brain Integration Chain — Complete Walkthrough]] | 17 steps, each with action/expected/validation |
| T-E011-13 | Epic Standards | [[e010-model-updates-all-15-models-reflect-current-knowledge|E010 — Model Updates — All 15 Models Reflect Current Knowledge]] | the 2026-04-12 session product — demonstrates strong scaffold with handoff context |
| T-E011-14 | Task Standards | Pick a well-defined task from backlog | Short, focused, verifiable Done When |
| T-E011-15 | Note Standards | Pick a directive note from the 2026-04-12 session | Verbatim quotes, interpretation, action items |

### M3: Integration (2 tasks)

| Task | What |
|------|------|
| T-E011-16 | Update LLM Wiki Standards page with count: "15/15 standards have inline annotated exemplars" |
| T-E011-17 | Run `pipeline post` + lint — resolve all issues |

## Dependencies

- **E010 (Model Updates):** Standards reference models for "what good looks like." If a model is outdated, the standard's exemplar might demonstrate something the model no longer defines. E010 should complete first, or at minimum M1 (core models) should be done.
- **Current exemplar pages must be stable.** If E010 changes a model page significantly, the annotation in E011 may need updating. Coordinate timing.

## Open Questions

> [!question] ~~Should the annotation format be standardized?~~
> **RESOLVED:** Yes. Format: > [!example] callout with numbered quality aspects + improvement note. Already consistent across 22 pages.
> Current format: `> [!example]- Full Walkthrough — Why Each Section Works` with nested annotation points. Should all 15 use this exact format, or adapt per type? Recommendation: same structural format, content adapts per type.

> [!question] ~~Should exemplars be the BEST page of that type, or a TYPICAL good page?~~
> **RESOLVED:** Best available page. The exemplar demonstrates the standard at its highest, with honest "What could still improve" notes.
> Best = aspirational ("this is the gold standard"). Typical = achievable ("this is what good normally looks like"). Recommendation: best — standards should RAISE the bar, not describe the average.

> [!question] ~~What about the new `principle` and `milestone` types?~~
> **RESOLVED:** Need standards pages. Principle and milestone exist in schema but lack dedicated page-type standards docs. Add to standards backlog.
> These were added the 2026-04-12 session. They don't have standards pages yet. Should E011 create them? Recommendation: yes — add 2 more standards pages (principle-page-standards.md, milestone-page-standards.md) as tasks T-E011-18 and T-E011-19.

## Handoff Context

> [!info] For anyone picking this up in a fresh context:
>
> **What this epic does:** Takes 15 per-type standards pages and adds inline annotated exemplar walkthroughs to each. The walkthrough shows a REAL page of that type with annotations explaining WHY each part is good.
>
> **What's already done:** 3 of 15 have annotations (lesson, pattern, decision). These were created during the 2026-04-12 session using pages from the 2026-04-12 session as exemplars.
>
> **What the annotations look like:** See `wiki/spine/standards/lesson-page-standards.md` → "### Annotated Exemplar: [[infrastructure-enforcement-proves-instructions-fail|Infrastructure Enforcement Proves Instructions Fail]]" section. It walks through frontmatter, summary, context, insight, evidence, applicability, and relationships — annotating WHY each works.
>
> **Quality bar for annotations:**
> - ≥5 annotation points per exemplar (frontmatter, summary, key sections, evidence, relationships)
> - Each point explains WHY, not just WHAT
> - Points reference the specific quality bar from the same standards page (closes the loop)
> - The annotation is in a `> [!example]-` foldable callout
>
> **Key files to read first:**
> - Any of the 3 existing annotated standards (lesson, pattern, decision) for the format
> - `wiki/spine/model-llm-wiki-standards.md` — the meta-standard that defines what ALL standards should have
> - `raw/notes/2026-04-12-documentation-standards-directive.md` — operator quality expectations

## Relationships

- PART OF: [[second-brain-complete-system-v2-0|Milestone — Second Brain Complete System — v2.0]]
- IMPLEMENTS: [[second-brain-integration-requirements|Second Brain Integration System — Full Chain Requirements]] (FR-D3, FR-D5)
- DEPENDS ON: [[e010-model-updates-all-15-models-reflect-current-knowledge|E010 — Model Updates — All 15 Models Reflect Current Knowledge]]
- BUILDS ON: [[model-llm-wiki-standards|LLM Wiki Standards — What Good Looks Like]]
- FEEDS INTO: [[e012-template-enrichment-rich-proto-programming-examples|E012 — Template Enrichment — Rich Proto-Programming Examples]] (E012)
- FEEDS INTO: [[e020-knowledge-sweep-global-quality-confirmation-by-human-review|E020 — Knowledge Sweep — Global Quality Confirmation by Human Review]] (E020)

## Backlinks

[[second-brain-complete-system-v2-0|Milestone — Second Brain Complete System — v2.0]]
[[second-brain-integration-requirements|Second Brain Integration System — Full Chain Requirements]]
[[e010-model-updates-all-15-models-reflect-current-knowledge|E010 — Model Updates — All 15 Models Reflect Current Knowledge]]
[[model-llm-wiki-standards|LLM Wiki Standards — What Good Looks Like]]
[[e012-template-enrichment-rich-proto-programming-examples|E012 — Template Enrichment — Rich Proto-Programming Examples]]
[[e020-knowledge-sweep-global-quality-confirmation-by-human-review|E020 — Knowledge Sweep — Global Quality Confirmation by Human Review]]
