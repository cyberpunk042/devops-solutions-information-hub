---
title: "{{title}} — Gap Analysis"
type: concept
domain: {{domain}}
status: synthesized
confidence: high
maturity: seed
created: {{date}}
updated: {{date}}
sources:
  - id: infrastructure-analysis
    type: file
    file: "{{infrastructure_analysis_path}}"
tags: [methodology, gap-analysis, {{epic_tag}}]
---

# {{title}} — Gap Analysis

## Summary

<!-- 2-3 sentences: what's missing between current state and target state.
     Built on top of the infrastructure analysis. -->

## Key Insights

<!-- Top gaps and their implications. What's the biggest risk? What's the
     highest-impact gap to close? -->

## Deep Analysis

### Gap Inventory

<!-- Numbered gaps. Each gap has:
     | Aspect | Details |
     |--------|---------|
     | Current state | What exists today |
     | Required state | What needs to exist |
     | Impact | What breaks or is blocked without this |
     | Affected scope | Files, components, systems affected |
     | Complexity | S/M/L/XL effort estimate |

     Group related gaps by module or epic.
     STYLING: > [!warning] for critical/blocking gaps. -->

### Dependency Graph

<!-- How gaps relate to each other. Which must be filled first?
     STYLING: > [!abstract] with ordering or dependency tree. -->

### Complexity and Effort Assessment

<!-- Summary table of all gaps with effort estimates.
     STYLING: > [!info] with table: Gap | Complexity | Dependencies -->

## Open Questions

<!-- Questions about gaps that need research or design decisions. -->

## Relationships

- BUILDS ON: {{infrastructure_analysis_title}}
- FEEDS INTO: {{requirements_spec_title}}
