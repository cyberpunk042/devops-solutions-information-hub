---
title: "Milestone: {{title}}"
type: milestone
domain: backlog
status: draft
priority: {{priority}}
target_date: {{YYYY-MM-DD}}
readiness: 0               # 0-100: derived from child epics. Is the milestone DEFINED enough?
progress: 0                 # 0-100: derived from child epics. How far is the WORK?
epics:
  - "{{epic_id_1}}"
  - "{{epic_id_2}}"
acceptance_criteria:
  - "{{measurable_criterion_1}}"
  - "{{measurable_criterion_2}}"
confidence: high
created: {{date}}
updated: {{date}}
sources:
  - id: operator-directive
    type: file
    file: "{{directive_file}}"
tags: [milestone]
---

# Milestone: {{title}}

<!-- A milestone groups multiple epics into a delivery target — what ships TOGETHER.
     Use milestones for: version releases, phase transitions (POC→MVP), quarterly boundaries.
     Don't use milestones for single-epic deliveries — just use the epic directly. -->

## Summary

<!-- 2-3 sentences: what this milestone delivers and WHY these epics must coordinate.
     The summary defines the scope boundary — what's IN vs OUT of this milestone. -->

## Operator Directive

<!-- Verbatim quote(s) that define this milestone target.
     STYLING: > blockquote for each directive. -->

> "{{verbatim operator directive}}"

## Delivery Target

<!-- When and what.
     STYLING: > [!info] with target table. -->

> [!info] Milestone Parameters
>
> | Parameter | Value |
> |-----------|-------|
> | **Target date** | {{YYYY-MM-DD}} |
> | **Phase** | {{POC / MVP / Staging / Production}} |
> | **Chain** | {{Simplified / Middle Ground / Full}} |
> | **Total epics** | {{N}} |
> | **Estimated total tasks** | {{N}} |

## Epic Composition

<!-- Which epics are in this milestone, what each contributes, and their current state.
     STYLING: Table with readiness column updated from derived values. -->

| Epic | Contributes | Current Readiness | Status |
|------|------------|-------------------|--------|
| [[{{epic_1}}]] | {{what it delivers to this milestone}} | {{N}}% | {{status}} |
| [[{{epic_2}}]] | {{what it delivers to this milestone}} | {{N}}% | {{status}} |

## Acceptance Criteria

<!-- Measurable criteria that define "this milestone is DONE."
     Each criterion is verifiable — names a command, metric, or observable behavior.
     GOOD: "Agent stage violations < 5% across 10 autonomous runs"
     BAD: "System works well" -->

- [ ] {{measurable_criterion_1}}
- [ ] {{measurable_criterion_2}}
- [ ] All child epics at status: done (operator confirmed)

## Dependencies

<!-- External factors or cross-milestone dependencies.
     Format: what → impact if not ready → mitigation -->

## Impediments

<!-- Active blockers against this milestone. Each has a type.
     Types: technical, dependency, decision, environment, clarification, scope, external, quality
     Remove when resolved (move to Resolved Impediments section). -->

| Impediment | Type | Blocked Since | Escalated? | Resolution |
|-----------|------|---------------|-----------|------------|
| {{description}} | {{type}} | {{date}} | {{yes/no}} | {{pending / resolved: how}} |

## Relationships

- CONTAINS: [[{{epic_1}}]]
- CONTAINS: [[{{epic_2}}]]
- IMPLEMENTS: {{what_directive_or_vision}}
