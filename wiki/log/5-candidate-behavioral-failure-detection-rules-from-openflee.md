---
title: "5 candidate behavioral-failure detection rules from OpenFleet doctor.py (2026-04-18)"
type: note
domain: log
note_type: session
status: synthesized
confidence: medium
created: 2026-04-18
updated: 2026-04-18
sources: []
tags: [contributed, remark]
contributed_by: "openfleet-solo-session-2026-04-18"
contribution_source: "/home/jfortin/openfleet"
contribution_date: 2026-04-18
contribution_status: accepted
contribution_reason: "5 candidate behavioral-detection rules found novel vs current brain taxonomy after mapping OpenFleet doctor.py to agent-failure-taxonomy + three-lines-of-defense. Filing as remark (not lesson) because ≥3 evidence threshold not yet met per brain's lesson-page-standards. Serves as signal for future lesson promotion if brain or operator finds additional evidence."
resolution_date: 2026-04-18
resolution_notes: |
  5 candidate detection rules incorporated as "Candidate Extensions" section in
  wiki/lessons/03_validated/enforcement-compliance/agent-failure-taxonomy-seven-classes-of-behavioral-failure.md.
  Preserved remark-not-lesson framing per ≥3-evidence threshold. Watch-signal documented:
  promotion trigger is (a) operator sees Class-9 behavior in OpenArms/Research Wiki, OR
  (b) OpenFleet's intervention-log audit produces ≥3 evidence per rule.
---

# 5 candidate behavioral-failure detection rules from OpenFleet doctor.py (2026-04-18)

## Summary

OpenFleet's fleet/core/doctor.py (679 lines) implements 10 Line-2 detection functions as the immune system's detection layer. After mapping against brain's agent-failure-taxonomy (8 classes) and three-lines-of-defense pattern (5 named diseases), 5 of our rules appear to be NOVEL detection categories not represented in either brain page.

Verified via gateway view search — no brain results for: 'code without reading', 'not listening', 'detect_abstraction', 'correction threshold' (except as mention in three-lines-of-defense + OpenFleet synthesis, no standalone treatment), 'cascading fix' (one loose mention, no detection rule).

FIVE CANDIDATE DETECTION RULES — novel vs current brain taxonomy:

1. detect_correction_threshold (fleet/core/doctor.py)
   Signal: agent corrected too many times on the same task.
   Distinct from brain's 'confident-but-wrong' (which is 'same mistake repeated 3+ times') in that correction_threshold tracks CORRECTIONS RECEIVED (operator/reviewer feedback count) rather than mistake-repetition-by-agent. Measures multi-iteration rework without root-cause fix. Fleet-scale signal: solo agents don't have enough interaction surface.

2. detect_code_without_reading
   Signal: agent produced code without reading existing code first.
   Overlaps brain's 'Never Synthesize from Descriptions Alone' lesson at a different operational layer — that lesson is about ingestion depth (Layer 0 vs Layer 1). This rule is about WRITE discipline. Fleet-scale: specialist agents inherit large codebase context; writing without reading produces drift and stale-pattern replication.

3. detect_cascading_fix (general form)
   Signal: fix-on-fix chain — each fix succeeds, reveals next failure, agent keeps going.
   Overlaps brain's Class 3 environment patching (polyfill chains, 2-15 overhead per occurrence) but cascading_fix is DOMAIN-GENERAL — any fix-on-fix, not just environment-specific. Could be promoted as a generalization of Class 3 or as a sibling class.

4. detect_abstraction
   Signal: agent replaced literal requirements with abstractions prematurely.
   Mirror of brain's 'Hardcoded Instances Fail — Build Frameworks Not Solutions' lesson, inverted: that lesson warns against FAILING TO ABSTRACT; this rule warns against ABSTRACTING TOO EARLY. The failure mode is that specialist agents (architect, senior engineer role) prefer their own abstractions and retrofit them onto concrete PO requirements. Cost: vision drift disguised as generalization.

5. detect_not_listening
   Signal: agent produces output instead of processing PO input.
   Fleet-scale: agents interact asynchronously with the operator (via Plane, IRC, notifications, board memory). The interaction cadence allows 'batch-output-then-check-for-input' patterns that solo tight-feedback-loop agents don't exhibit. Detection heuristic: unprocessed mentions in mentions queue + continued output generation. May not generalize to solo agents.

PROMOTION PATH (per brain's lesson-page-standards):
Each rule needs ≥3 independent evidence items to promote from 'candidate detection rule' to 'behavioral failure lesson.' OpenFleet has operational data in fleet/core/intervention logs and agent-session runs; would need a dedicated audit to extract evidence per rule. Filing as REMARK rather than lesson to respect the 3-evidence threshold.

FULL OPENFLEET MAPPING:
See OpenFleet wiki page 'OpenFleet doctor.py Rules Mapped to Agent Failure Taxonomy' (wiki/domains/architecture/doctor-rules-vs-agent-failure-taxonomy.md) for:
- Full 10-rule vs 8-class coverage map
- Alternative lens: 10 rules vs brain's 5 named diseases (Deviation/Laziness/Protocol/Confident-but-wrong/Scope creep) — we cover 4/5
- Line-1/2/3 breakdown of which gaps need prevention vs detection vs correction
- Hidden-from-agents alignment audit (passed — 0 detect_* references in agents/_template/)

RELATED BRAIN PAGES:
- agent-failure-taxonomy-seven-classes-of-behavioral-failure (the 8-class reference)
- three-lines-of-defense-immune-system-for-agent-quality (the 5-disease reference)
- OpenFleet is listed as the 'Full 3-Line Implementation' instance (746 lines) in the three-lines-of-defense pattern

Filed from openfleet-solo-session-2026-04-18 following the verify-before-contributing discipline: each claim of novelty verified via brain's own search tools before filing.

## Relationships

- RELATES TO: [[model-registry|Model Registry]]

## Backlinks

[[model-registry|Model Registry]]
