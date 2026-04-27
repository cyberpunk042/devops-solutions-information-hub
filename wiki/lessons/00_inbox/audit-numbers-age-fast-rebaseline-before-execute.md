---
title: "audit-numbers-age-fast-rebaseline-before-execute"
type: lesson
domain: cross-domain
layer: 4
status: synthesized
confidence: medium
maturity: seed
derived_from: []
created: 2026-04-27
updated: 2026-04-27
sources: []
tags: [contributed, inbox]
contributed_by: "jfortin@WORKSTATION-JFM"
contribution_source: "/home/jfortin/devops-expert-local-ai"
contribution_date: 2026-04-27
contribution_status: pending-review
---

# audit-numbers-age-fast-rebaseline-before-execute

## Summary

# Audit Numbers Age Fast — Rebaseline Before Executing Against an Old Audit

## Pattern

A brain audit (or any retrospective metric report) reports a percentage at a
specific time T: e.g., "47% of skills are boilerplate against the standard." That
number is true at T but ages quickly because:

1. Other workstreams may have been silently chipping at the underlying problem.
2. The audit's diagnostic criteria may have evolved.
3. The codebase itself may have moved (refactors, deletions, additions).

Six weeks later, the number can be wrong by a substantial margin while still
appearing in the decision document as a current fact.

## Why this matters

If the team picks up the audit-driven plan based on the OLD number:
- They may execute against a problem that no longer exists at that scale.
- They may miss the ACTUAL current gap, which has shifted to a different shape.
- Their commit messages and reports will reference a metric that doesn't reflect
  the work actually done.

Re-baselining at execution time is cheap (a single grep or count) and prevents
weeks of work being framed against stale data.

## Evidence: AICP skills audit, 2026-04-17 (audit) vs 2026-04-27 (execution)

- **2026-04-17 (audit time)**: brain decision doc reported "47% boilerplate against
  Extension Standards" across 78 AICP skills. The percentage was correct at that
  time.
- **Between 2026-04-17 and 2026-04-27**: in-flight work (driven by other concerns
  — feature additions, mid-session cleanup) silently eliminated boilerplate from
  many skills. Nobody re-counted.
- **2026-04-27 (execution time)**: when the operator picked up Phase 2 of the
  audit-driven plan, a re-count revealed:
  - 17 fleet-referenced skills already had Quality Bar coverage (tier-2).
  - 26 fleet-referenced skills still needed the gold-standard structure.
  - The original "47% of 78" frame was no longer the right unit.
- **What the work actually was**: rewrite 26 specific skills to gold-standard
  pattern. Not "fix 47% boilerplate". The framing matters because the SCOPE
  estimate, the EFFORT estimate, and the MEASURABLE goal all change.

The plan was directionally correct — boilerplate was real and the gold-standard
pattern was the right answer. The number was misleading by execution time.

## Detection

Before starting work driven by an audit/metric/baseline that's >2 weeks old:

1. Re-run the audit's measurement step (a count, a grep, a script).
2. Compare to the audit's reported figure.
3. If the figures differ substantially: the plan's scope and effort estimates
   should be revisited before execution.

## How to apply

In handoff documents and audit decisions:
- ALWAYS include the measurement command/query, not just the number.
- Mark numbers with the time they were taken: "47% as of 2026-04-17".
- When picking up the plan later, re-run the measurement and update the number
  before executing.

In retrospectives that reference audit numbers:
- Always cite "the figure at the time of the audit" vs "the figure at execution"
  if both are known.
- Treat divergence as data: it tells you something about the team's velocity on
  the underlying concern.

## What this is NOT

- Not "audits are useless". Audits are valuable for surfacing patterns; the
  pattern + the standards are the durable artifact, not the percentage.
- Not "always re-baseline". For audits <2 weeks old, the figure is probably still
  good enough. The pattern matters specifically for plans being executed against
  older numbers.
- Not specific to skills audits. Applies to any audit: code coverage, technical
  debt, dependency health, etc.

## Source

AICP Post-Anthropic mission retrospective (2026-04-27),
docs/retros/RETRO-post-anthropic-2026-04-27.md.
Original audit: wiki/decisions/00_inbox/skills-audit-2026-04-17.md.
Re-baseline discovery: HANDOFF-SKILLS-PHASE-2-2026-04-27.md section 4.

## Context

<!-- When does this lesson apply? -->

## Insight

<!-- The core learning -->

## Evidence

<!-- What evidence supports this? -->

## Applicability

Contributed from /home/jfortin/devops-expert-local-ai. Applicability to be assessed during promotion review.

## Relationships

- RELATES TO: [[model-registry|Model Registry]]

## Backlinks

[[model-registry|Model Registry]]
