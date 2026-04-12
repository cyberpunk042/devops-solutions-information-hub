---
title: "{{epic_id}} {{title}} — Design Document"
type: concept
domain: {{domain}}
status: synthesized
confidence: high
maturity: seed
created: {{date}}
updated: {{date}}
sources:
  - id: requirements-spec
    type: file
    file: "{{requirements_spec_path}}"
tags: [methodology, design, {{epic_tag}}]
---

# {{epic_id}} {{title}} — Design Document

## Summary

<!-- 2-3 sentences: design decisions and architecture for this epic/module.
     Resolves open questions from the requirements spec. Every decision
     includes rationale and reversibility. Produced during the DESIGN stage. -->

## Key Insights

<!-- Top design insights that shaped the decisions. -->

## Deep Analysis

<!-- Each major design decision gets its own subsection.
     Structure per decision:

### Decision N: {{decision_title}}

     STYLING: > [!success] Decision: {{statement}}
     > | Scenario | Action |
     > |----------|--------|

     Then: rationale, evidence, rejected alternatives.
     STYLING: > [!warning] Rejected Alternative: {{name}}
     > Why rejected: {{specific reason}}

     Reversibility assessment for each decision. -->

### Module Plan

<!-- Refined module/task breakdown with implementation order.
     STYLING: > [!abstract] with table: Order | Module | Scope | Estimate | Depends On -->

## Open Questions

<!-- Design-level questions remaining. Should be few — design stage resolves
     most questions from requirements. Any remaining questions are implementation
     details, not design choices. -->

## Relationships

- IMPLEMENTS: [[{{epic_title}}]]
- BUILDS ON: {{requirements_spec_title}}
