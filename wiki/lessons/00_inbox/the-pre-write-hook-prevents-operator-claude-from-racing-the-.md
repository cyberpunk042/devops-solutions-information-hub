---
title: "The pre-write hook prevents operator-Claude from racing the running agent on backlog files"
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

# The pre-write hook prevents operator-Claude from racing the running agent on backlog files

## Summary

While a `pnpm openarms agent run` is in flight, the `scripts/methodology/hooks/pre-bash.sh` and `scripts/methodology/hooks/pre-write.sh` hooks block writes to task files, epic files, and `_index.md` from ANY context — including operator-Claude (Context A in `lesson-five-claude-contexts.md`). The block message is: ``` BLOCKED: Task/epic frontmatter is managed by the harness. Use /stage-complete to advance stages and /task-done to complete tasks. ``` I'd been mentally treating operator-Claude as

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
