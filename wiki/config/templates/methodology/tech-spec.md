---
title: "{{title}} — Tech Spec"
type: reference
domain: {{domain}}
status: synthesized
confidence: high
maturity: seed
created: {{date}}
updated: {{date}}
sources:
  - id: design-doc
    type: file
    file: "{{design_doc_path}}"
tags: [methodology, tech-spec, {{epic_tag}}]
---

# {{title}} — Tech Spec

## Summary

<!-- 2-3 sentences: what this spec defines and for whom.
     A tech spec is LOOKUP material — API tables, interface definitions,
     algorithm pseudocode. Produced during the DESIGN stage. -->

## Reference Content

### Component Specifications

<!-- Per component: responsibility, location, dependencies, consumers.
     STYLING: > [!info] per component with table:
     > | Attribute | Value |
     > |-----------|-------|
     > | Responsibility | ... |
     > | Location | ... |
     > | Dependencies | ... |
     > | Consumers | ... |
-->

### API

<!-- Function/method reference table.
     > [!info] API Reference
     > | Function | Input | Output | Side Effects |
     > |----------|-------|--------|-------------|
-->

### Data Contracts

<!-- File formats, JSON/YAML structures, state file formats.
     Use code blocks with concrete examples, not placeholders. -->

### Algorithm

<!-- Pseudocode or step-by-step for key logic.
     Code blocks for pseudocode. Numbered steps for process. -->

### Error Handling

<!-- Error case → response mapping.
     > | Error Case | Response | Recovery |
     > |-----------|----------|----------|
-->

## Relationships

- IMPLEMENTS: {{design_doc_title}}
- PART OF: [[{{epic_title}}]]
