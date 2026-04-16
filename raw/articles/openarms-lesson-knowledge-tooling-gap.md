---
title: "First consumer integration reveals systematic gaps between knowledge and tooling"
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
contributed_by: "openarms-operator-claude"
contribution_source: "/home/jfortin/openarms/wiki/log/2026-04-16-second-brain-integration-notes.md"
contribution_date: 2026-04-16
contribution_status: pending-review
contribution_reason: "Meta-lesson from the first real consumer integration — the integration experience itself is evidence"
---

# First consumer integration reveals systematic gaps between knowledge and tooling

## Summary

The first real consumer integration (OpenArms connecting to the second brain, 2026-04-16) revealed that knowledge in model pages (800+ lines of deep analysis per model) was not accessible via the gateway tooling. Artifact chains returned empty, SDLC profiles were not queryable, field definitions returned 'Unknown field', orient gave a one-liner to returning consumers, compliance checked file paths not functional equivalence, identity profile conflated project and consumer properties. Three OFV cycles in one session fixed 7 of 9 issues. The pattern: knowledge exists in prose, tooling doesn't surface it. Each gateway command needs to read its corresponding model/reference page and extract structured data. The gap between 'the knowledge exists' and 'an agent can query it' is the integration bottleneck, not the knowledge itself.

## Context

<!-- When does this lesson apply? -->

## Insight

<!-- The core learning -->

## Evidence

<!-- What evidence supports this? -->

## Applicability

Contributed from /home/jfortin/openarms/wiki/log/2026-04-16-second-brain-integration-notes.md. Applicability to be assessed during promotion review.

## Relationships

- RELATES TO: [[model-registry|Model Registry]]
