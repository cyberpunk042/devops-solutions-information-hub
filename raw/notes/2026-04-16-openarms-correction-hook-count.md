---
title: "OpenArms hook count is 4 not 5 — enforcement-hook-patterns.md reference card"
type: note
domain: log
note_type: session
status: synthesized
confidence: medium
created: 2026-04-16
updated: 2026-04-16
sources: []
tags: [contributed, correction]
contributed_by: "openarms-operator-claude"
contribution_source: "/home/jfortin/openarms/scripts/methodology/hooks/pre-write.sh"
contribution_date: 2026-04-16
contribution_status: pending-review
contribution_reason: "Accuracy correction from the project that implements the pattern"
---

# OpenArms hook count is 4 not 5 — enforcement-hook-patterns.md reference card

## Summary

The Enforcement Hook Patterns page reference card lists 4 hook patterns (Scope Guard, Write Guard, Artifact Tracker, Context Rebuilder). The page instances section correctly describes 4 OpenArms hooks. But the newly added Pattern 5 (Race Prevention Guard) is a refinement of the Write Guard, not a separate hook — our pre-write.sh contains BOTH the stage-scope blocking AND the race prevention blocking in the same 106-line file. The reference card should note that Pattern 5 is typically implemented as an extension of Pattern 2 (Write Guard), not as a separate hook. OpenArms has 4 hook FILES (pre-bash, pre-write, post-write, post-compact) implementing 5 PATTERNS.

## Relationships

- RELATES TO: [[model-registry|Model Registry]]
