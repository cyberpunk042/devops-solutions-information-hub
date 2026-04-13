---
title: "{{title}}"
type: epic
domain: backlog
status: draft
priority: {{priority}}
task_type: epic
current_stage: document
readiness: 0               # 0-100: derived from children. Are the requirements, design, plan DEFINED?
progress: 0                 # 0-100: derived from children. How far is the WORK across all modules/tasks?
stages_completed: []
artifacts: []
confidence: high
created: {{date}}
updated: {{date}}
sources:
  - id: operator-directive
    type: file
    file: "{{directive_file}}"
tags: []
---

# {{title}}

## Summary

<!-- 2-3 sentences: what this epic delivers and WHY it matters.
     Every epic MUST trace to a verbatim operator directive.
     The summary IS the charter — it defines scope boundaries. -->

## Operator Directive

<!-- Verbatim quote(s) that originated this epic.
     STYLING: > blockquote for each directive.
     This section is the AUTHORITY — when in doubt, re-read the directive. -->

> "{{verbatim operator directive}}"

## Goals

<!-- Bulleted list of concrete goals. Each goal is a CAPABILITY or DELIVERABLE.
     Not vague aspirations — specific outcomes that can be demonstrated.
     GOOD: "Agent can query all artifacts required for a stage via MCP tool"
     BAD: "Improve agent experience" -->

- {{goal_1}}
- {{goal_2}}

## Done When

<!-- Checklist of verifiable completion criteria. Each item names specific FILES,
     COMMANDS, or OBSERVABLE BEHAVIORS — not abstractions.
     GOOD: "- [ ] `python3 -m tools.pipeline post` returns 0 errors"
     BAD: "- [ ] System works correctly"
     Include at least one validation step per major deliverable. -->

- [ ] {{specific_verifiable_criterion_1}}
- [ ] {{specific_verifiable_criterion_2}}
- [ ] Pipeline post returns 0 errors after all changes
- [ ] Operator confirms deliverables are findable (discoverability test)

## Scale and Model

<!-- Which methodology model governs this epic?
     What quality tier: Skyscraper (full process), Pyramid (deliberate compression)?
     How many modules/tasks expected? -->

> [!info] Epic Parameters
>
> | Parameter | Value |
> |-----------|-------|
> | **Model** | feature-development |
> | **Quality tier** | Skyscraper |
> | **Estimated modules** | {{N}} |
> | **Estimated tasks** | {{N}} |
> | **Dependencies** | {{list or "none"}} |

## Stage Artifacts (per methodology model)

<!-- What does each stage produce for THIS epic?
     Reference wiki/config/methodology.yaml for the model's artifact chain.
     Be specific — name the wiki pages, config files, tool changes. -->

> [!abstract] Stage → Artifact Map
>
> | Stage | Required Artifacts | Template |
> |-------|--------------------|----------|
> | Document | Directive log, research synthesis, gap analysis | wiki/config/templates/methodology/gap-analysis.md |
> | Design | Requirements spec, design plan, decisions | wiki/config/templates/methodology/requirements-spec.md |
> | Scaffold | Config changes, templates, schema updates | N/A — per deliverable |
> | Implement | Code, wiki pages, tool changes | N/A — per deliverable |
> | Test | Validation runs, pipeline post, operator review | N/A — per deliverable |

## Module Breakdown

<!-- Break the epic into modules. Each module becomes its own page.
     Format: Module name — what it delivers — estimated tasks. -->

| Module | Delivers | Est. Tasks |
|--------|----------|-----------|
| {{module_1}} | {{deliverable}} | {{N}} |
| {{module_2}} | {{deliverable}} | {{N}} |

## Dependencies

<!-- Other epics, external factors, or blockers.
     For each: what it depends on + what happens if it's not ready. -->

## Open Questions

<!-- What's not yet decided? Each question should block a specific module or task.
     Resolve questions during Document/Design stages — not during Implement. -->

> [!question] {{question}}
> {{context for the question}}

## Relationships

- IMPLEMENTS: {{what_directive_or_model}}
- DEPENDS ON: {{dependency_epic_or_page}}
