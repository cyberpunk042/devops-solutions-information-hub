---
title: "{{title}} — Test Plan"
type: reference
domain: {{domain}}
status: synthesized
confidence: high
maturity: seed
created: {{date}}
updated: {{date}}
sources:
  - id: tech-spec
    type: file
    file: "{{tech_spec_path}}"
tags: [methodology, test-plan, {{epic_tag}}]
---

# {{title}} — Test Plan

## Summary

<!-- 2-3 sentences: what this test plan covers and verification strategy.
     Produced during the DESIGN stage. Drives test stub creation in SCAFFOLD
     and test implementation in TEST stage. -->

## Reference Content

### Unit Tests

<!-- Per-function test cases.
     > [!info] Unit Tests
     > | Test ID | Component | Input | Expected Output |
     > |---------|-----------|-------|----------------|
-->

### Integration Tests

<!-- Cross-component test cases.
     > | Test ID | Setup | Steps | Expected Result |
     > |---------|-------|-------|----------------|
-->

### Validation Tests

<!-- For wiki/config projects: pipeline validation tests.
     > | Test ID | Input | Command | Expected Result |
     > |---------|-------|---------|----------------|
-->

### Regression Tests

<!-- Bugs that must not recur. Reference bug number or incident.
     > | Test ID | Bug | Scenario | Must Not Happen |
     > |---------|-----|----------|----------------|
-->

### Test Data

<!-- Mock files, temp directories, fake inputs, fixtures needed. -->

## Relationships

- IMPLEMENTS: {{tech_spec_title}}
- PART OF: [[{{epic_title}}]]
