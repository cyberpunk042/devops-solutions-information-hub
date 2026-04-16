---
title: "Per-task cost grows monotonically across multi-task runs (context accumulation)"
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

# Per-task cost grows monotonically across multi-task runs (context accumulation)

## Summary

## Summary When `pnpm openarms agent run --tasks N` runs multiple tasks in sequence within a single harness invocation, each successive task pays MORE than the previous task — even when the tasks are similar in scope. The cost growth comes from accumulating codebase context: each task adds new files and modifies existing ones, and the next task's "read the codebase" startup cost is higher because there's more state to absorb. The pattern is monotonic across `--tasks N` runs and predictable: ex

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
