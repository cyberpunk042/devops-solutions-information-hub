---
title: Standards-by-Example
aliases:
  - "Standards-by-Example"
type: epic
domain: backlog
status: in-progress
priority: P1
task_type: epic
current_stage: implement
readiness: 70
progress: 50
stages_completed:
  - "document"
  - "implement"
artifacts:
  - "wiki/spine/standards/model-standards/model-llm-wiki-standards.md"
  - "wiki/spine/standards/model-standards/model-methodology-standards.md"
  - "wiki/spine/standards/concept-page-standards.md"
  - "wiki/spine/standards/lesson-page-standards.md"
  - "wiki/spine/standards/pattern-page-standards.md"
  - "wiki/spine/standards/decision-page-standards.md"
  - "wiki/spine/standards/comparison-page-standards.md"
  - "wiki/spine/standards/source-synthesis-page-standards.md"
  - "wiki/spine/standards/reference-page-standards.md"
  - "wiki/spine/standards/deep-dive-page-standards.md"
  - "wiki/spine/standards/domain-overview-page-standards.md"
  - "wiki/spine/standards/operations-plan-page-standards.md"
  - "wiki/spine/standards/epic-page-standards.md"
  - "wiki/spine/standards/task-page-standards.md"
  - "wiki/spine/standards/note-page-standards.md"
  - "wiki/spine/standards/evolution-page-standards.md"
  - "wiki/spine/standards/learning-path-page-standards.md"
  - "wiki/spine/learning-paths/methodology-fundamentals.md"
  - "wiki/spine/evolution-log/methodology-evolution-history.md"
  - "wiki/domains/cross-domain/wiki-post-ingestion-operations-plan.md"
  - "tools/lint.py"
  - "tools/validate.py"
confidence: high
created: 2026-04-11
updated: 2026-04-11
depends_on:
  - "E003"
sources:
  - id: operator-directive
    type: file
    file: raw/notes/2026-04-11-methodology-standards-directive.md
tags: [methodology, standards, exemplars, annotations, quality, self-validation]
---

# Standards-by-Example

## Summary

Every standard the wiki defines must ship with a gold-standard exemplar that passes its own rules. The wiki eats its own cooking. This epic creates annotated exemplars for all page types, elevates the methodology standards page from seed to mature, and builds a self-validation loop that ensures standards pages never drift from their own exemplars. Per the lesson "Standards Must Preach by Example" — a standard that can't demonstrate itself is dead text.

## Goals

- Create or designate gold-standard exemplar pages for all 9 page types currently missing exemplars
- Annotate exemplars: inline or companion annotations explaining WHY each structural choice was made
- Elevate model-methodology-standards.md from seed to mature maturity
- Create annotated methodology.yaml exemplar showing what good configuration looks like
- Build self-validation: automated check that every standards page references existing exemplars that pass quality gates
- Create an annotation methodology: how to annotate an exemplar so it teaches, not just demonstrates
- Update model-llm-wiki-standards.md to reference all new exemplars
- Ensure every standard in the wiki passes its own self-referential integrity test

## Done When

- [ ] Gold-standard exemplar designated or created for every page type agents create
- [ ] Exemplars are annotated (inline or companion) with structural reasoning
- [ ] model-methodology-standards.md elevated to mature maturity with recovery procedures, per-model examples
- [ ] Annotated methodology.yaml exemplar exists (generic base with comments)
- [ ] Self-validation rule added to tools/lint.py or tools/validate.py
- [ ] Annotation methodology documented as wiki page
- [ ] model-llm-wiki-standards.md updated with all exemplar references
- [ ] Every standards page passes self-referential integrity test
- [ ] All new pages pass validation with 0 errors

## Dependencies

- E003 (Artifact Type System) — needs complete type definitions to know what needs exemplars
- Partially E004 (Methodology Engine) — methodology.yaml exemplar requires the engine design
- Partially E005 (Compliance Framework) — enforcement patterns can serve as exemplars

### How This Connects — Navigate From Here

> [!abstract] From This Epic → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **Goldilocks** | [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]] |
> | **System map** | [[methodology-system-map|Methodology System Map]] |

## Relationships

- DEPENDS ON: [[[[E003-artifact-type-system|Artifact Type System]] (E003)]]
- BUILDS ON: [[standards-must-preach-by-example|Standards Must Preach by Example]]
- BUILDS ON: [[models-are-systems-not-documents|Models Are Systems, Not Documents]]
- IMPLEMENTS: [[model-llm-wiki-standards|LLM Wiki Standards — What Good Looks Like]]
- IMPLEMENTS: [[model-quality-failure-prevention|Model — Quality and Failure Prevention]]
- FEEDS INTO: [[model-methodology-standards|Methodology Standards — What Good Execution Looks Like]]
- RELATES TO: [[model-wiki-design|Model — Wiki Design]]

## Backlinks

[[E003-artifact-type-system|Artifact Type System]]
[[standards-must-preach-by-example|Standards Must Preach by Example]]
[[models-are-systems-not-documents|Models Are Systems, Not Documents]]
[[model-llm-wiki-standards|LLM Wiki Standards — What Good Looks Like]]
[[model-quality-failure-prevention|Model — Quality and Failure Prevention]]
[[model-methodology-standards|Methodology Standards — What Good Execution Looks Like]]
[[model-wiki-design|Model — Wiki Design]]
[[methodology-standards-initiative-honest-assessment|Methodology Standards Initiative — Honest Assessment]]
