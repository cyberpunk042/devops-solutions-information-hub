---
title: "Epic readiness math is wrong when an epic has implicit goals beyond its current children"
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

# Epic readiness math is wrong when an epic has implicit goals beyond its current children

## Summary

 The harness computes epic readiness as the average of its child task readiness. This is only correct when the children fully cover the epic's goals. If an epic has implicit goals that have not yet been broken down into child tasks, the average is a mathematical artifact that does not reflect actual progress. **The first child task to complete will flip the epic to 100% even if the epic's real work is barely started.** This bit me on 2026-04-14 with E013 (Usage Dashboard and Status Line). I wrot

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
