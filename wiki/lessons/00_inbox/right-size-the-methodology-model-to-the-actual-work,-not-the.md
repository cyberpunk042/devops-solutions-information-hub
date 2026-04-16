---
title: "Right-size the methodology model to the actual work, not the structural category"
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

# Right-size the methodology model to the actual work, not the structural category

## Summary

The methodology selector picks a model based on `task_type` (`task`, `bug`, `spike`, `docs`, `refactor`, etc.). For `task_type: task`, it picks `feature-development` — the full 5-stage model (document → design → scaffold → implement → test) with its full artifact requirements. **This is the right default for genuinely new feature work, but it's overkill for narrow mechanical extensions of existing infrastructure.** The selector should consider the SCOPE of the work, not just its struct

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
