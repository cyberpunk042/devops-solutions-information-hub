---
title: "The harness 'turnCount' variable counts streaming events, not conversational turns"
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

# The harness 'turnCount' variable counts streaming events, not conversational turns

## Summary

`src/commands/agent-run-harness.ts:373` declares `let turnCount = 0` and uses it for session-lifecycle decisions: - `turn count > 150` → compact the session - `turn count >= 200` (`maxTurns`) → start a fresh session The variable is meant to track conversational turns. **It actually counts streaming `message_start` events** — which fire dozens of times per assistant turn during stream-json output. The metric is inflated by ~20-50× compared to what its name suggests. Session lifecycle decis

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
