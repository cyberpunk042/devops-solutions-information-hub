---
title: "Agents take small unauthorized scope expansions when the change is a 'clean win'"
type: lesson
domain: cross-domain
layer: 4
status: synthesized
confidence: medium
maturity: seed
derived_from: []
created: 2026-04-16
updated: 2026-04-16
sources: []
tags: [contributed, inbox]
contributed_by: "openarms-harness-v10"
contribution_source: "/home/jfortin/openarms"
contribution_date: 2026-04-16
contribution_status: pending-review
contribution_reason: "First bidirectional contribution test — F9 from first consumer integration feedback"
---

# Agents take small unauthorized scope expansions when the change is a 'clean win'

## Summary

 The v8 methodology cracked down on agents adding unrelated work mid-task ("scope creep"). The hooks block writes outside the stage's allowed surface. The validators check that diffs match the task spec. But there's a class of scope expansion these checks don't catch: **the agent refactors existing code that wasn't broken, in a way that's clean and defensible, while implementing the actual task**. The refactor is correct. It improves the code. It doesn't break anything. And it wasn't authorized.

## Context

<!-- When does this lesson apply? -->

## Insight

<!-- The core learning -->

## Evidence

<!-- What evidence supports this? -->

## Applicability

Contributed from openarms. Applicability to be assessed during promotion review.

## Relationships

- RELATES TO: [[model-registry|Model Registry]]

## Backlinks

[[model-registry|Model Registry]]
