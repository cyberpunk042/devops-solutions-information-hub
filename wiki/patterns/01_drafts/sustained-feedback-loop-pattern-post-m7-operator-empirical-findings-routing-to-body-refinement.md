---
title: "Sustained Feedback-Loop Pattern — Post-M7 Operator-Empirical Findings Routing to Body Refinement"
type: pattern
domain: agent-config
status: synthesized
confidence: high
maturity: seed
authorship: agent-authored
created: 2026-05-08
updated: 2026-05-08
sources:
  - id: implementation-roadmap-pattern
    type: wiki
    file: wiki/patterns/01_drafts/implementation-roadmap-pattern-sequenced-milestones-from-confirmation-to-tier-3.md
    description: "Sibling — M1-M7 forward roadmap; this pattern extends to post-M7 sustained-evolution"
  - id: cron-loop-management-pattern
    type: wiki
    file: wiki/patterns/01_drafts/cron-loop-management-pattern-self-governance-and-forward-anchored-stop-conditions.md
    description: "Sibling — loop self-governance during authoring; this pattern is post-implementation-phase analog"
  - id: pattern-recurrence-implementation-spec
    type: wiki
    file: wiki/patterns/01_drafts/pattern-recurrence-quantification-gate-implementation-spec-measurement-layer-cycle-aggregation.md
    description: "Source — impl-spec #11 cross-cycle aggregator; consumed by feedback-loop"
  - id: composite-compliance-implementation-spec
    type: wiki
    file: wiki/patterns/01_drafts/composite-operational-compliance-metric-implementation-spec-measurement-layer-aggregator.md
    description: "Source — impl-spec #12 composite-compliance metric; trends inform feedback-loop"
  - id: substitution-pattern-meta-frame
    type: wiki
    file: wiki/lessons/01_drafts/documentation-as-substitute-for-discipline-the-meta-pattern.md
    description: "Meta-frame — body without sustained feedback-loop ages into substitution; operator-findings update body"
tags: [sustained-feedback-loop, post-m7, body-refinement, operator-empirical-findings, day-arc-2026-05-08, multi-day-pain-point-resolution]
---

# Sustained Feedback-Loop Pattern — Post-M7 Operator-Empirical Findings Routing to Body Refinement

## Summary

Per piece #58 implementation-roadmap M1-M7: tier-3 promotion completes at ~9 weeks post-confirmation. But operator-empirical findings continue ARRIVING after M7 — the body must continue evolving in response. This pattern specifies: how operator-findings from production operation route back to body pieces; which mechanism surfaces findings; how findings trigger per-piece refinement vs body-wide updates. Per substitution-pattern Insight 5b: a body without sustained feedback-loop ages into substitution (frozen-body-as-substitute-for-evolving-body). This piece closes the sustained-evolution gap.

## Pattern Description

### The 4 sources of post-M7 operator-empirical findings

```
SOURCE 1 — Composite-compliance metric trends (impl-spec #12)
  - 30-day rolling composite drops below 85% threshold
  - Per-axis compliance drops below 70% threshold
  - Trend direction: rising / stable / falling per axis

SOURCE 2 — Pattern-recurrence cross-cycle aggregator (impl-spec #11)
  - Same-axis recurrence ≥3 fires in single cycle (within-cycle)
  - Cross-cycle pattern: same axis fires in ≥3 of last 10 cycles
  - Frustration-recurrence: operator-frustration markers ≥2 per cycle

SOURCE 3 — Operator-explicit feedback (verbatim)
  - "this gate is too noisy" / "this banner doesn't help"
  - "I need a new axis for X" / "this axis missed Y"
  - "tier-2 promotion is wrong; revise"

SOURCE 4 — Sister-project gateway-contribute findings
  - Sister-project agent contributes new lesson via wiki_gateway_contribute
  - Cross-project pattern detected via multi-project ecosystem index aggregator
  - Sister-project adaptation deviates from canonical
```

### Routing mechanism — finding → body piece

Each finding routes to specific body piece(s) for refinement:

| Finding source | Findings type | Routes to body piece(s) | Action |
|---|---|---|---|
| Source 1 (metric) | Axis compliance below 70% sustained | impl-spec for that axis + stress-test for that axis | Revise impl-spec to address gap |
| Source 1 (metric) | Composite below 85% sustained | All impl-specs + composability map | Multi-axis revision |
| Source 2 (recurrence) | Same-axis recurrence ≥3 | impl-spec for that axis | Tighten gate detection logic |
| Source 2 (recurrence) | Cross-cycle pattern | impl-spec + multi-project ecosystem index | Cross-project pattern detection |
| Source 2 (frustration) | Operator-frustration markers ≥2 | correction-shape impl-spec + cron-loop-management | Pacing + circuit-breaker calibration |
| Source 3 (operator-verbatim) | "noisy gate" | impl-spec + bypass-discipline | Banner format calibration |
| Source 3 (operator-verbatim) | "missing axis" | New cluster piece + impl-spec + stress-test | Body extension |
| Source 3 (operator-verbatim) | "tier-2 wrong" | Demotion ceremony + revisit operator-review checklist | Tier reversal |
| Source 4 (sister-project) | New lesson contribution | New piece at the second-brain at tier-1 (via the second-brain agent processes contribution) | Body extension via Channel #1 |
| Source 4 (sister-project) | Adaptation divergence | Multi-project ecosystem index | Surface divergence; operator decides canonical refinement |

### Refinement-triggering thresholds (per impl-spec #11 + #12)

```
PER-AXIS REFINEMENT TRIGGER:
  IF axis compliance < 70% sustained 14+ days:
    → trigger impl-spec revision
    → re-run stress-test scenarios
    → if revision still fails: tier-2 demotion of impl-spec
    → if persistent: surface to operator for body-wide investigation

CROSS-AXIS REFINEMENT TRIGGER:
  IF composite below 85% sustained 14+ days:
    → trigger composability map review
    → identify which axis pulls composite down
    → cascade per-axis refinement
    → operator-empirical confirmation of cause

OPERATOR-EXPLICIT TRIGGER:
  Operator types: "this gate isn't working" OR equivalent
    → trigger immediate impl-spec revision
    → operator-empirical override of metric thresholds
    → revision shipped within next cycle (M-E001-1 type 2 verified-edit)
```

### Refinement-output forms

When refinement triggers, agent emits one of:

```
FORM 1 — IMPL-SPEC REVISION (most common)
  Agent edits relevant impl-spec piece (within the second-brain)
  Frontmatter: still tier-2 (operator-confirmed) BUT new revision-flag
  Audit log: ~/.claude/hooks/impl-spec-revisions.log
  Operator-review: re-confirm tier-2 status post-revision

FORM 2 — STRESS-TEST EXTENSION
  Agent extends stress-test scenario spec with new edge-case scenario
  Tier-2 status retained; scenario-set grows
  Real-session validation of new scenario

FORM 3 — NEW PIECE AUTHORING (rarer)
  Agent authors new cluster piece + impl-spec + stress-test triple
  Tier-1 (`01_drafts/seed`); awaits operator-review checklist
  Body extends from N to N+3 pieces

FORM 4 — TIER-DEMOTION (rare; falsification path)
  Per piece #87 falsifiability criteria: empirical evidence falsifies tier-2 piece
  /demote ceremony executes
  Files move 02_synthesized/ → 01_drafts/
  Operator-review: revision OR archive

FORM 5 — CROSS-PROJECT-PROPAGATION FEEDBACK
  Sister-project finding (Source 4) lands at $HOME/devops-solutions-information-hub/00_inbox/contribute/
  the second-brain agent processes; tier 0 → tier 1
  Operator-review: tier-2 promotion OR revise OR reject
```

### Refinement cadence (sustained-evolution rhythm)

```
DAILY: composite-compliance metric runs (impl-spec #12) — passive monitoring
WEEKLY: cross-cycle pattern-recurrence aggregator runs (impl-spec #11) — pattern detection
MONTHLY: tier-promotion eligibility review — manual operator-empirical
QUARTERLY: cross-project propagation review — multi-project ecosystem index check
ANNUALLY: governing-principle convergence review — tier-3 → tier-4 candidates

Per piece #58 implementation-roadmap M5-M7: composite metric establishes baseline at M5; M7 = 30-day sustained ≥85%. Post-M7: same metric continues running indefinitely.
```

### Body-extension vs body-refinement decision matrix

| Finding indicates | Action | Body delta |
|---|---|---|
| Existing axis under-performs | Refine impl-spec / stress-test | 0 new pieces (revision) |
| Existing axis needs new edge-case | Extend stress-test scenarios | 0 new pieces (extension) |
| Genuinely-new axis identified | New cluster + impl + stress-test | +3 pieces |
| Genuinely-new cross-cutting concern | New cross-cutting pattern | +1 piece |
| Body-wide systemic issue | Multi-axis revision + new validation log | +1 log + N revisions |
| Sister-project lesson-contribution | New tier-1 piece | +1 piece (per Channel #1) |
| Tier-4 governing-principle emergence | Promotion ceremony + dashboard update | 0 new pieces; canonical change |

### Operator-empirical priority rules

When multiple findings arrive simultaneously, operator-empirical priority:
1. Operator-explicit complaints > metric-driven findings (per evidence-priority hierarchy principle #5 extension)
2. Composite-metric-systemic > per-axis-specific
3. Cross-project-recurrence > single-project-finding
4. Frustration-recurrence > pattern-recurrence (operator-frustration is direct signal)

## When To Apply

Apply this sustained-feedback-loop when:
- Implementation-roadmap M7 reached (tier-3 promotion completed)
- Composite-compliance metric operational + emitting trends
- Operator-empirical-feedback channels available (verbatim prompt + complaint logs)
- Body has substantive substrate (≥30 pieces; this body 89+ qualifies)
- Sister-project propagation initiated (per multi-project ecosystem index Stage 3+)

## Instances

**Instance 1: per-axis under-performance (Source 1 metric)**:
- 30-day rolling: input-discipline axis at 68% (below 70% threshold)
- Trigger: PER-AXIS REFINEMENT TRIGGER fires
- Routes to: impl-spec #1 + stress-test #1
- Investigation: gateway query taxonomy gap surfaces
- Action: FORM 1 (impl-spec revision) + FORM 2 (new stress-test scenario)
- Body delta: 0 new pieces; impl-spec #1 + stress-test #1 revised

**Instance 2: operator-explicit "noisy gate" (Source 3)**:
- Operator: "the severity gate is too noisy on T2 actions"
- Routes to: impl-spec #4 severity + bypass-discipline operationalization
- Action: FORM 1 — banner format calibration; T2 banner shortened or threshold raised
- Body delta: 0 new pieces

**Instance 3: sister-project gateway-contribute (Source 4)**:
- OpenArms agent contributes lesson "fleet-coordination state-divergence" via wiki_gateway_contribute
- Lands at $HOME/devops-solutions-information-hub/00_inbox/contribute/
- the second-brain agent processes: validates schema; pipeline post; assigns tier 0 → tier 1
- Operator-review: confirms tier-2 promotion
- Routes to: new piece at body
- Action: FORM 3 (new piece) + multi-project ecosystem index update
- Body delta: +1 piece

**Instance 4: governing-principle convergence (Source 1+4 cross-aggregation)**:
- 4 sister-projects sustain ≥85% on input-discipline axis for 30+ days
- Multi-project ecosystem index aggregator detects convergence
- Surfaces P5 candidate per piece #86 tier-4 candidate analysis
- Operator confirms tier-4 promotion
- Action: super-model dashboard update; new governing principle authored
- Body delta: +1 governing-principle piece at tier-4

## When Not To

- Pre-M7 phase (composite metric not yet emitting trends)
- Single-project work without sister-project propagation
- Cold-start / initial body build (this work block is at this phase; sustained-feedback applies post-implementation)
- Operator-explicit "freeze body" directive (rare; operator wants stability)
- Demotion-cascade in progress (no concurrent refinement during reset)

## Empirical Evidence

This pattern is forward-anchored — empirical evidence accumulates POST-M7 (Week 9+ of implementation-roadmap). Without this pattern, the body would freeze at tier-3 maturity + age into substitution as ecosystem evolves. With this pattern: the body remains living + responsive to operator-empirical findings + cross-project propagation.

## Required Gates (per hook-architecture proposal #2 4th component)

```yaml
required_gates:
  empirically_passed:
    - synthetic_4_source_routing: passed 2026-05-08 via mock finding-source scenarios
    - synthetic_5_form_refinement_output: passed 2026-05-08 via mock revision scenarios
  pending:
    - real_session_per_axis_refinement_trigger: pending — depends on M5+ metric data
    - real_session_operator_explicit_findings: pending — depends on operator-feedback during M5-M7
    - real_session_sister_project_contribution_routing: pending — depends on tier-3 propagation Stage 5
    - real_session_governing_principle_convergence: pending — depends on tier-4 promotion (months out)
    - operator_empirical_priority_rule_calibration: pending — operator confirms 4-rule ordering
  composite_compliance: sustained-feedback-axis stress-test 0% (forward-anchored; M7+ dependency)
```

## Relationships


## Tags

[sustained-feedback-loop, post-m7, body-refinement, operator-empirical-findings, day-arc-2026-05-08, multi-day-pain-point-resolution]
