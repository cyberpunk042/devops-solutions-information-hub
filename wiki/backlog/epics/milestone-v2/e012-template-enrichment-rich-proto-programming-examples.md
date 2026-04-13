---
title: E012 — Template Enrichment — Rich Proto-Programming Examples
aliases:
  - "E012 — Template Enrichment — Rich Proto-Programming Examples"
  - "E012 — Template Enrichment: Rich Proto-Programming Examples"
type: epic
domain: backlog
status: draft
priority: P0
task_type: epic
current_stage: document
readiness: 70
progress: 75
stages_completed:
artifacts:
  - "raw/notes/2026-04-12-documentation-standards-directive.md"
confidence: high
created: 2026-04-12
updated: 2026-04-12
sources:
  - id: milestone
    type: file
    file: wiki/backlog/milestones/second-brain-complete-system-v2-0.md
  - id: documentation-standards
    type: directive
    file: raw/notes/2026-04-12-documentation-standards-directive.md
  - id: proto-programming
    type: wiki
    file: wiki/lessons/03_validated/structured-context-is-proto-programming-for-ai-agents.md
tags: [epic, templates, proto-programming, enrichment, examples, v2, milestone-v2]
---

# E012 — Template Enrichment — Rich Proto-Programming Examples
## Summary

Transform every page template from a structural skeleton with placeholder comments into a RICH EXAMPLE that teaches through its own content. A template is proto-programming: the STRUCTURE of the template programs the agent's behavior when filling it. Currently most templates have `<!-- guidance comments -->` telling the agent what to do. After this epic, templates have INLINE EXAMPLE CONTENT showing what a good page looks like — the agent learns by SEEING, not by READING instructions. The template IS the example. The example IS the standard. Preach by example at the template level.

## Operator Directive

> "Then there is the template which should themselves be example of rich usage and strong structure and example of contents."

> "We will also need proper example of artifacts not just unfinished standards with no examples and no real strong templates."

> "Markdown offer proto-programming and proto-programming is what AI does best. just like Human building structure or giving proper structured information to AI."

> "Preach by example."

## Goals

- Every template contains INLINE EXAMPLE CONTENT that demonstrates the standard it scaffolds
- Templates teach through STRUCTURE (headers, callout types, table layouts, field values) not just comments
- The guidance comments remain but are supplemented with actual example content in `<!-- EXAMPLE: ... -->` blocks or as default pre-filled sections
- Templates are self-validating: scaffolding from the template and running `pipeline post` produces a page that PASSES validation with zero changes (all required sections present, frontmatter valid)
- Each template's frontmatter demonstrates proper field usage (not just `{{placeholder}}` but typed values with inline comments explaining each)
- The 6 methodology templates (`wiki/config/templates/methodology/`) are enriched with real document examples (requirements spec, design plan, etc.)

## Done When

- [ ] `wiki/config/templates/concept.md` — has example Key Insights + example Deep Analysis subsection inline
- [ ] `wiki/config/templates/source-synthesis.md` — has example Source Reference card + example Key Insight inline
- [ ] `wiki/config/templates/comparison.md` — has example Comparison Matrix inline
- [ ] `wiki/config/templates/reference.md` — has example Reference Content table inline
- [ ] `wiki/config/templates/deep-dive.md` — has example Deep Analysis with subsections inline
- [ ] `wiki/config/templates/lesson.md` — ALREADY RICH (verify + improve if needed)
- [ ] `wiki/config/templates/pattern.md` — ALREADY RICH (verify + improve if needed)
- [ ] `wiki/config/templates/decision.md` — ALREADY RICH (verify + improve if needed)
- [ ] `wiki/config/templates/domain-overview.md` — has example Maturity Map + Key Pages inline
- [ ] `wiki/config/templates/evolution.md` — has example Timeline entry + Key Shift inline
- [ ] `wiki/config/templates/learning-path.md` — has example Sequence entry with annotation inline
- [ ] `wiki/config/templates/epic.md` — ALREADY RICH (verify + improve if needed)
- [ ] `wiki/config/templates/module.md` — has example Tasks table with readiness/progress inline
- [ ] `wiki/config/templates/task.md` — has example Done When items naming files inline
- [ ] `wiki/config/templates/note.md` — has example per note_type (directive/session/completion) inline
- [ ] `wiki/config/templates/operations-plan.md` — ALREADY RICH (verify + improve if needed)
- [ ] `wiki/config/templates/milestone.md` — has example Epic Composition table inline
- [ ] `wiki/config/templates/principle.md` — has example Derived From table inline
- [ ] `wiki/config/templates/methodology/requirements-spec.md` — has example FR item inline
- [ ] `wiki/config/templates/methodology/design-plan.md` — has example decision table inline
- [ ] `wiki/config/templates/methodology/gap-analysis.md` — has example gap inventory row inline
- [ ] `wiki/config/templates/methodology/infrastructure-analysis.md` — has example inventory row inline
- [ ] `wiki/config/templates/methodology/tech-spec.md` — has example component/API section inline
- [ ] `wiki/config/templates/methodology/test-plan.md` — has example test matrix row inline
- [ ] Scaffolding any template with `pipeline scaffold <type> "Test"` produces a page passing `pipeline post` with 0 errors
- [ ] Operator confirms: templates TEACH through their content, not just provide structure

## Scale and Model

> [!info] Epic Parameters
>
> | Parameter | Value |
> |-----------|-------|
> | **Model** | knowledge-evolution (document → implement) |
> | **Quality tier** | Skyscraper |
> | **Estimated modules** | 3 (wiki page templates, methodology templates, validation) |
> | **Estimated tasks** | 10-15 (some templates are already rich, need verify only) |
> | **Dependencies** | E011 (Standards — templates must demonstrate what standards define) |

## Stage Artifacts

> [!abstract] Stage → Artifact Map
>
> | Stage | Required Artifacts |
> |-------|-------------------|
> | Document | THIS epic page (done). Audit of each template's current state vs desired state. |
> | Implement | Updated template files (24). Each update enriches with inline example content. |
> | Validation | `pipeline scaffold <type> "Test"` for each type → `pipeline post` → 0 errors. Operator review. |

## Module Breakdown

### M1: Wiki Page Templates (18 templates)

| Task | Template | Current State | What to Add |
|------|----------|--------------|-------------|
| T-E012-01 | concept.md | Guidance comments, 44L | Example Key Insight (1 self-contained), example Deep Analysis subsection |
| T-E012-02 | source-synthesis.md | Rich guidance, 56L | Example Source Reference card filled in, example Key Insight with specific data |
| T-E012-03 | comparison.md | Rich guidance, 55L | Example Comparison Matrix row (3 columns filled) |
| T-E012-04 | reference.md | Basic, 35L | Example Reference Content table with 3 rows |
| T-E012-05 | deep-dive.md | Basic, 48L | Example Deep Analysis with 2 subsections |
| T-E012-06 | lesson.md | Rich, 47L | VERIFY — already has callout guidance. Improve if needed. |
| T-E012-07 | pattern.md | Rich, 59L | VERIFY — already has instances table format. Improve if needed. |
| T-E012-08 | decision.md | Rich, 52L | VERIFY — already has scenario-action table. Improve if needed. |
| T-E012-09 | domain-overview.md | Moderate, 48L | Example Maturity Map row, example Key Pages with reading order |
| T-E012-10 | evolution.md | Upgraded the 2026-04-12 session, 75L | VERIFY — already has timeline format + key shift structure. |
| T-E012-11 | learning-path.md | Upgraded the 2026-04-12 session, 65L | VERIFY — already has part structure + annotations. |
| T-E012-12 | epic.md | Upgraded the 2026-04-12 session, 107L | VERIFY — already has Stage Artifacts + Module Breakdown + Handoff Context sections. |
| T-E012-13 | module.md | Upgraded the 2026-04-12 session, 60L | Example Tasks table with 2 rows filled (readiness/progress columns) |
| T-E012-14 | task.md | Upgraded the 2026-04-12 session, 44L | Example Done When with 2 specific items naming files |
| T-E012-15 | note.md | Upgraded the 2026-04-12 session, 75L | VERIFY — already has per-type structure (directive/session/completion). |
| T-E012-16 | operations-plan.md | Rich, 56L | VERIFY — already has Action/Expected/Validation/Rollback per step. |
| T-E012-17 | milestone.md | Created the 2026-04-12 session, 83L | Example Epic Composition table with 2 rows filled |
| T-E012-18 | principle.md | Created the 2026-04-12 session, 85L | Example Derived From table with 1 row filled |

### M2: Methodology Templates (6 templates)

| Task | Template | Current State | What to Add |
|------|----------|--------------|-------------|
| T-E012-19 | methodology/requirements-spec.md | Rich, 76L | Example FR item (FR-1 with SHALL statement + rationale) |
| T-E012-20 | methodology/design-plan.md | Rich, 60L | Example decision row in decision table |
| T-E012-21 | methodology/gap-analysis.md | Rich, 62L | Example gap inventory row (Current/Required/Impact/Complexity) |
| T-E012-22 | methodology/infrastructure-analysis.md | Rich, 59L | Example inventory row with file:line reference |
| T-E012-23 | methodology/tech-spec.md | Rich, 67L | Example component or API section with table |
| T-E012-24 | methodology/test-plan.md | Rich, 63L | Example test matrix row (Test ID, Description, Type, Required) |

### M3: Validation (1 task)

| Task | What |
|------|------|
| T-E012-25 | Scaffold EVERY type with `pipeline scaffold <type> "Template Test"`, run `pipeline post`, verify 0 errors. Delete test files after. |

## Dependencies

- **E011 (Standards):** Templates must demonstrate what standards define. If a standard says "Evidence section must have ≥3 items," the lesson template should show 3 example evidence items. E011 should complete (or at least M1 verify pass) before templates are enriched.
- **Current template upgrades:** 6 templates were upgraded the 2026-04-12 session (note, epic, learning-path, evolution, milestone, principle). These need VERIFY tasks, not full rewrites.

## Open Questions

> [!question] ~~Should example content use `<!-- EXAMPLE: ... -->` comments or actual pre-filled sections?~~
> **RESOLVED:** HTML comments. Pre-filled sections risk being left in final pages. Comments are clearly not-real-content.
> Comments: agent sees the example but knows to replace. Pre-filled: agent sees real content and adapts. Recommendation: pre-filled sections with `<!-- Replace this example with your content -->` marker. The pre-filled content IS the teaching.

> [!question] ~~Should templates have TWO sections — structure + example?~~
> **RESOLVED:** Yes. Already implemented — 24 templates enriched with inline examples. Structure + example is the standard.
> Or should the example BE the structure? Recommendation: the structure IS the example. One section, rich content. The `{{placeholder}}` markers indicate what to replace. Everything else is example content that teaches through format.

## Handoff Context

> [!info] For anyone picking this up in a fresh context:
>
> **What this epic does:** Takes 24 page templates and enriches each with inline example content so the template TEACHES by example, not just by comments.
>
> **What's already done:** 6 templates upgraded the 2026-04-12 session with richer guidance (note, epic, learning-path, evolution, milestone, principle). 6 templates were already rich before (lesson, pattern, decision, operations-plan, source-synthesis, comparison). The remaining 12 need enrichment.
>
> **The proto-programming principle:** The template's STRUCTURE programs agent behavior. An agent filling a template with example content will produce output that mimics the example's quality. An agent filling a template with empty placeholders will produce minimal output.
>
> **Key files to read first:**
> - Any of the "ALREADY RICH" templates (lesson.md, pattern.md, decision.md) for the target quality
> - `wiki/lessons/03_validated/structured-context-is-proto-programming-for-ai-agents.md` — the principle this epic implements
> - `wiki/spine/standards/lesson-page-standards.md` → annotated exemplar section — this is what "teaching by example" looks like in a standards page; templates should achieve the same at the template level

## Relationships

- PART OF: [[second-brain-complete-system-v2-0|Milestone — Second Brain Complete System — v2.0]]
- IMPLEMENTS: [[second-brain-integration-requirements|Second Brain Integration System — Full Chain Requirements]] (FR-D2: Template exemplars)
- IMPLEMENTS: [[structured-context-governs-agent-behavior-more-than-content|Principle — Structured Context Governs Agent Behavior More Than Content]]
- DEPENDS ON: [[e011-standards-exemplification-all-15-per-type-standards-with-inline-annotated-e|E011 — Standards Exemplification — All 15 Per-Type Standards with Inline Annotated Exemplars]]
- BUILDS ON: [[structured-context-is-proto-programming-for-ai-agents|Structured Context Is Proto-Programming for AI Agents]]
- FEEDS INTO: [[e017-context-engineering-framework-formalized-as-model-with-standards|E017 — Context Engineering Framework — Formalized as Model with Standards]] (E017)
- FEEDS INTO: [[e016-integration-chain-proof-end-to-end-with-openarms|E016 — Integration Chain Proof — End to End with OpenArms]] (E016)

## Backlinks

[[second-brain-complete-system-v2-0|Milestone — Second Brain Complete System — v2.0]]
[[second-brain-integration-requirements|Second Brain Integration System — Full Chain Requirements]]
[[structured-context-governs-agent-behavior-more-than-content|Principle — Structured Context Governs Agent Behavior More Than Content]]
[[e011-standards-exemplification-all-15-per-type-standards-with-inline-annotated-e|E011 — Standards Exemplification — All 15 Per-Type Standards with Inline Annotated Exemplars]]
[[structured-context-is-proto-programming-for-ai-agents|Structured Context Is Proto-Programming for AI Agents]]
[[e017-context-engineering-framework-formalized-as-model-with-standards|E017 — Context Engineering Framework — Formalized as Model with Standards]]
[[e016-integration-chain-proof-end-to-end-with-openarms|E016 — Integration Chain Proof — End to End with OpenArms]]
