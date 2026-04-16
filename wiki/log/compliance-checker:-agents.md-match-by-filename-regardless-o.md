---
title: "Compliance checker: AGENTS.md match by filename regardless of role — per-agent persona files falsely satisfy Tier 2 (inverse of F1 fix)"
type: note
domain: log
note_type: session
status: synthesized
confidence: medium
created: 2026-04-16
updated: 2026-04-16
sources: []
tags: [contributed, correction]
contributed_by: "openfleet-solo-session"
contribution_source: "/home/jfortin/openfleet"
contribution_date: 2026-04-16
contribution_status: pending-review
contribution_reason: "First openfleet compliance run (2026-04-16) surfaced inverse-false-positive from the F1 fix"
---

# Compliance checker: AGENTS.md match by filename regardless of role — per-agent persona files falsely satisfy Tier 2 (inverse of F1 fix)

## Summary

During OpenFleet's first compliance run (sister-project mode, 2026-04-16, from /home/jfortin/openfleet), Tier 2 requirement 'AGENTS.md — Agent context file (universal or tool-specific)' was marked met (✓) because the checker found /home/jfortin/openfleet/agents/_template/AGENTS.md.

That file is NOT a universal project context file. It is a per-agent persona template read at runtime by individual fleet agents (one per each of 10 roles: fleet-ops, PM, devsecops-expert, architect, software-engineer, qa-engineer, devops, technical-writer, ux-designer, accountability-generator). It sits alongside SOUL.md and HEARTBEAT.md as Layer-2 runtime-consumer context, not Layer-1 repo-wide universal context.

OpenFleet has NO root-level AGENTS.md. The checker's pass is a false positive.

INVERSE of F1: OpenArms F1 was 'strict path match misses functional equivalents' (wiki-schema.yaml vs schema.yaml). Fix: accept any location via functional-name matching. That fix now produces a new false-positive direction: 'loose name match catches non-equivalent files in wrong roles.'

PROPOSED REFINEMENT: For Tier 2 AGENTS.md / CLAUDE.md detection, restrict match to repo-root depth (depth=1 in tree). Files with these names nested under agents/, personas/, roles/, or any role-indicating directory are runtime-consumer context, not universal project context. Repo-root-only matching eliminates this false positive without reintroducing F1's strict-path problem.

EVIDENCE: 'gateway --wiki-root /home/jfortin/openfleet compliance' output: Tier 2 marked '✓ 3/3' despite OpenFleet having no root AGENTS.md. Actual state: only CLAUDE.md (358 lines, not yet 3-layer-restructured) exists at root.

CROSS-REFERENCES: (1) Validates and extends 'Structural Compliance Is Not Operational Compliance' lesson — compliance checker measures presence, not functional role. (2) Instance candidate for 'Aspirational Declaration Produces False Confidence at Every Layer' pattern — the checker DECLARES Tier 2 met without verifying role/purpose. (3) OpenFleet's fleet-scale per-agent AGENTS.md/SOUL.md/HEARTBEAT.md structure is cited by 'Progressive Structural Enrichment in Agent Config' pattern as requiring per-agent variation — this correction formalizes why that nested structure shouldn't cross-match the root-level requirement.

## Relationships

- RELATES TO: [[model-registry|Model Registry]]
