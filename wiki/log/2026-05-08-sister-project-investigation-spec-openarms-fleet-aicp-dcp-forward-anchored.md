---
title: "Sister-Project Investigation Spec — OpenArms / OpenFleet / AICP / DCP (Forward-Anchored)"
type: note
note_type: completion
domain: log
status: synthesized
confidence: medium
created: 2026-05-08
updated: 2026-05-08
sources:
  - id: fire-189-root-investigation
    type: wiki
    file: wiki/log/2026-05-08-sister-project-investigation-kickoff-spec-root-ghostproxy-foundational-triplet-adaptation.md
    description: "Sibling (Fire 189) — /root spec; parallel structure"
  - id: fire-113-propagation-spec
    type: wiki
    file: wiki/patterns/01_drafts/sister-project-propagation-spec-for-auto-compact-triplet-5-projects-adaptation-matrix.md
    description: "PRIMARY parent (Fire 113)"
tags: [sister-project-investigation, openarms-fleet-aicp-dcp, forward-anchored, day-arc-2026-05-08, fire-190]
---

# Sister-Project Investigation Spec — OpenArms / OpenFleet / AICP / DCP (Forward-Anchored)

## Summary

Per Fire 113: 4 sister projects beyond /root (OpenArms / OpenFleet / AICP / devops-control-plane). Per Fire 189: /root spec'd. This Fire 190 specs investigation for remaining 4 (forward-anchored).

## Per-project investigation outline

```
OPENARMS (~/openarms/):
  Type: harness / agent-runtime
  Phase: production
  Per Fire 113 estimate: 8-15h
  Adaptation focus: harness-engineering specifics; agent-runtime entrypoints
  REGATHER_ALLOWLIST: harness-specific tools

OPENFLEET (~/openfleet/):
  Type: fleet-orchestrator
  Phase: production
  Per Fire 113 estimate: 10-18h
  Adaptation focus: fleet-multi-agent state-capture
  PreCompact handoff: extends to fleet-state per project

AICP (path TBD):
  Type: local-AI-inference
  Phase: development
  Per Fire 113 estimate: 2-4h
  Adaptation focus: possibly Layer 1 only; reduced triplet
  AICP may not have compaction events (different agent model)

DEVOPS-CONTROL-PLANE (path TBD):
  Type: infrastructure-governance
  Phase: unknown
  Per Fire 113 estimate: TBD
  Adaptation focus: governance-decision-flow; investigation prerequisite
```

## Combined effort

```
4 sister projects: ~20-37h investigation + adaptation
Plus /root (Fire 189): ~14-25h
Combined cross-project Phase 6: ~34-62h calendar 2-4 weeks at 50% engagement
```

## Sequencing

```
Per Fire 165 + Fire 113 + Fire 189: post-/opt-Phase-1 + post-/root
  Week 5+: /opt Phase 1 complete
  Week 6: /root adaptation
  Weeks 6-8: 4 sister projects (parallel after first investigation)
  Week 9+: Phase 7 cross-project synchronization
```

## Operator-pending

```
Q-FIRE-190-1: Endorse forward-anchored 4-project investigation post-Phase-1?
  Recommended: yes; scheduled per Fire 165 sequencing

Q-FIRE-190-2: AICP scope — Layer 1 only OR full triplet?
  Per Fire 113 Q-FIRE-113-2: pending operator-empirical
```

## Closing

4 sister projects investigation specs forward-anchored. Combined ~20-37h. Sequence post-/opt + /root.

**Standing by per /loop directive.**

## Tags

[sister-project-investigation, openarms-fleet-aicp-dcp, forward-anchored, day-arc-2026-05-08, fire-190]
