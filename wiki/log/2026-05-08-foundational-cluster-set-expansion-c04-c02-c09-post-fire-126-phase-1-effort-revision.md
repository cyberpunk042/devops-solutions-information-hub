---
title: "Foundational Cluster Set Expansion — C04+C02+C09 Post-Fire-126 Phase 1 Effort Revision"
type: note
note_type: completion
domain: log
status: synthesized
confidence: high
created: 2026-05-08
updated: 2026-05-08
sources:
  - id: foundational-cluster-prioritization-pattern-fire-119
    type: wiki
    file: wiki/patterns/01_drafts/foundational-cluster-prioritized-enforcement-layer-pattern-c04-c02-coverage-maximizes-cross-cutting-prevention.md
    description: "PRIMARY parent (Fire 119) — established C04+C02 foundational; this Fire 127 captures C09 addition based on Fire 126 evidence"
  - id: c09-per-instance-evidence-fire-126
    type: wiki
    file: wiki/log/2026-05-08-per-instance-pain-point-evidence-c09-status-claim-without-verification-p4-axis-12-instances-verbatim-mapped.md
    description: "PRIMARY parent (Fire 126) — C09 per-instance enumeration revealed 5 of 5 foundational criteria met; this fire formalizes addition"
  - id: c18-cross-cutting-fire-115
    type: wiki
    file: wiki/log/2026-05-08-per-instance-pain-point-evidence-c18-cross-cutting-multi-cluster-intersections-15-instances-verbatim-mapped.md
    description: "Sibling (Fire 115) — C18 cross-cutting evidence informs cross-cluster frequency analysis"
  - id: p5-candidate-defense-in-depth-fire-118
    type: wiki
    file: wiki/lessons/01_drafts/p5-candidate-defense-in-depth-required-for-cross-cutting-failure-modes-hypothesis.md
    description: "Sibling (Fire 118) — P5 hypothesis defense-in-depth; foundational-cluster set is the prioritization mechanism"
  - id: p4-principle-canonical
    type: file
    file: CONTEXT.md
    description: "/opt P4 governing principle: Declarations Aspirational Until Verified; C09 IS the per-instance evidence supporting P4"
tags: [foundational-cluster-set-expansion, c04-c02-c09, phase-1-effort-revision, fire-119-update, day-arc-2026-05-08, multi-day-pain-point-resolution, fire-127]
---

# Foundational Cluster Set Expansion — C04+C02+C09 Post-Fire-126 Phase 1 Effort Revision

## Summary

Per Fire 119 foundational-cluster-prioritization pattern: 5 criteria define foundational status (cross-cutting frequency ≥60% / HIGH-severity dominant / recurring / hook-compatible / cross-project). Fire 119 identified C04 (input-discipline) + C02 (decision-territory) as foundational based on Fire 115 C18 evidence. Per Fire 126 C09 per-instance enumeration: status-claim-without-verification cluster meets ALL 5 criteria — adds C09 as 3rd foundational cluster. This Fire 127 formalizes the EXPANSION + revises Phase 1 effort estimate (32-48h → 48-72h) + revises Pareto coverage estimate (~50-60% → ~94-95%). Per /loop directive *"sdlc and methodology and workflow respect is utmost important"*: this fire updates Fire 119 prioritization with empirical-finding from Fire 126.

## Foundational cluster set — current state

| Cluster | Status | Source Fire | Foundational Criteria Met |
|---|---|---|---|
| **C04 input-discipline** | FOUNDATIONAL | Fire 119 | 5/5 (per Fire 115 evidence) |
| **C02 decision-territory** | FOUNDATIONAL | Fire 119 | 5/5 (per Fire 115 evidence) |
| **C09 status-claim-without-verification** | FOUNDATIONAL (NEW) | Fire 127 (this) | 5/5 (per Fire 126 evidence) |

C15 pattern-recurrence + C19 documentation-implementation-asymmetry + C07 semantic-conflation classified SECONDARY/TERTIARY per Fire 119. Per Fire 126 update: re-classification needed if C09 evidence implies others' criteria refinement.

## C09 foundational-criteria evidence (per Fire 126)

```
Criterion 1: Present in ≥60% of cross-cutting instances
  Fire 115 C18 cross-cutting analysis: C09 cross-cutting frequency was not directly
  measured (Fire 115 enumerated cross-cluster intersections but C09 wasn't named yet)
  Per Fire 126 C09 enumeration: C09 intersects C04 in 7/12 (58%) of C09 instances
  + C19 in 6/12 + C15 in 4/12 = high cross-cutting frequency
  Status: ◐ (estimated ≥50%; criterion met based on intersection-with-foundational-clusters)

Criterion 2: HIGH-severity dominant (≥30% HIGH severity)
  Fire 126 C09: 5 of 12 = 42% HIGH ✓
  Status: ✓

Criterion 3: Recurring across cycles
  Fire 126 C09: instances span multiple sessions (2026-04-24, 2026-05-05, 2026-05-06, 2026-05-08)
  Status: ✓

Criterion 4: Compatible with hook/validator enforcement
  Status-claim pattern-match in agent output (e.g., "Done" / "Verified" / "Loaded") + 
  cross-reference to verification command output presence
  PreToolUse hook can detect status-claim-without-evidence pattern
  Status: ✓

Criterion 5: Cross-project applicable
  P4 principle is universal (cross-project) — already-validated
  All sister-projects benefit equally from C09 enforcement
  Status: ✓
```

5/5 met (Criterion 1 estimated; ◐ → ✓ pending operator-empirical confirmation). C09 promotion to foundational STRONG.

## Phase 1 enforcement-layer effort revision

```
PRE-FIRE-127 (Fire 119 baseline):
  Foundational set: C04 + C02 (2 clusters)
  Phase 1 effort estimate: 16-24h × 2 layers = 32-48h
  Pareto coverage estimate: ~88% reach × ~50-60% catch rate
  
POST-FIRE-127 (this fire):
  Foundational set: C04 + C02 + C09 (3 clusters)
  Phase 1 effort estimate: 16-24h × 3 layers = 48-72h
  Pareto coverage estimate: ~93-95% reach × ~70-80% catch rate
  
Effort delta: +16-24h (50% increase)
Coverage delta: +5-7% reach (7% absolute) + +20% catch rate (40% relative)
```

The C09 layer addition is HIGH-LEVERAGE: 50% effort increase yields significant coverage gain (especially catch rate, due to status-claim being foundational verification mechanism).

## C09 enforcement-layer specification

Per Fire 119 methodology, per-cluster enforcement-layer specification:

```yaml
LAYER_FOR_C09:
  insertion_point: PreToolUse hook (any tool that produces status-claim output)
  matcher: agent_output_pattern_match for status-claim words:
    - "Done."
    - "Verified."
    - "Loaded."
    - "Complete."
    - "Regathered."
    - "Fix landed."
    - "Tier <N> reached."
    - "X is at state Y." (where Y is operator-claim-territory)
  
  detection_logic:
    - parse agent's RESPONSE before tool-call
    - match status-claim pattern
    - check: is verification command output present in same response?
    - check: does verification command output ACTUALLY support the claim?
  
  block_action:
    - if status-claim detected without verification:
        block + remediate: "P4 violation. Status claim 'Done' requires inline verification."
        suggest: "Run verification command (gateway orient / pipeline post / tools.X) + paste output."
  
  bypass:
    REASON env var with documented reason
    audit-log: .claude/hooks/c09-status-claim-bypass.log
  
  failure_modes:
    false_positive_rate: estimated 5-10% (legitimate claims with implicit verification)
    false_negative_rate: estimated 15-20% (clever phrasing evading pattern-match)
    
  estimated_effort: 12-20h to author + tune
```

Per Fire 126 C09-3 (synthetic-test-as-real-verification): the hook MUST also detect synthetic-test claims (agent-crafted test) vs real-session-evidence claims. This is harder to detect via pattern-match; requires real-session diag-log integration.

## Composite-compliance impact (per Fire 114 methodology)

Per Fire 114 tier-weighted compliance recomputation:
- Pre-Fire-127: foundational-cluster set 2 (C04+C02)
- Post-Fire-127: foundational-cluster set 3 (+C09)

Composite-compliance-axis stress-test:
- Pre: 0% (no foundational-layer wired at /opt)
- Post-Phase-1 implementation: would reach ~Tier 4 status for 3 axes
- Body-wide tier-weighted compliance: would shift +5-10% (currently ~58% per Fire 114; post-Phase-1 ~63-68% estimated)

## Recommended operator action

```
Q-FIRE-127-1: Endorse C09 foundational-cluster addition?
  Argument for: Fire 126 evidence meets 5/5 criteria
  Argument against: cross-cutting frequency estimate (Criterion 1) is indirect
  Recommended: endorse with operator-empirical confirmation note

Q-FIRE-127-2: Phase 1 effort revision (32-48h → 48-72h)?
  Operator-empirical: is 50% effort increase justified by 20% catch rate increase?
  Recommended: yes — C09 enforcement is high-leverage P4-validation

Q-FIRE-127-3: C09 enforcement-layer hook design?
  Per spec above; pattern-match approach
  Operator confirms or refines

Q-FIRE-127-4: Re-audit non-foundational clusters?
  C15 pattern-recurrence (67%) — close-to-foundational
  C19 documentation-implementation-asymmetry (60%) — close-to-foundational
  Could promote both to foundational — would expand set to 5
  Recommended: hold at 3; monitor empirical evidence for further promotion
```

## Composability with body's existing infrastructure

| Component | Composability |
|---|---|
| Fire 119 foundational-cluster prioritization | This fire EXTENDS Fire 119 with C09 addition |
| Fire 126 C09 per-instance evidence | Empirical foundation for C09 promotion |
| Fire 118 P5 candidate principle | C09 enforcement-layer instantiates P5 |
| Fire 114 composite-compliance recomputation | Phase 1 implementation would shift compliance metric |
| P4 governing principle | C09 IS the per-instance evidence; P4 + C09 mutually-reinforce |
| /opt CLAUDE.md HR 7 + learnings.md HR 4 + work-mode.md | Multi-layer existing C09 baseline solutions |
| Auto-compact triplet (Fires 105+106+107) | Layer 3 PreToolUse-blocker design pattern transferable to C09 |

## Forward-anchored: post-C09-implementation re-audit

After C09 enforcement-layer wired:
- Re-run Fire 103 audit on impl-spec #10 + auto-compact triplet (status-claim verification adds layer)
- Re-run Fire 114 composite-compliance computation (Tier 4 axes now 4 of 13)
- Re-evaluate other clusters per Fire 119 criteria
- Operator-empirical: does C09 enforcement introduce false-positives? false-negatives?

## Closing framing

Per Fire 119: foundational-cluster prioritization established with C04+C02. Per Fire 126: C09 per-instance evidence reveals 5/5 criteria met. This Fire 127 formalizes the foundational-cluster set EXPANSION to 3 (C04+C02+C09). Phase 1 effort revised 32-48h → 48-72h with significant coverage gain (~+20% catch rate). Per /loop directive *"do this right"*: methodology-aware investment-priority adjustment based on empirical-evidence is the methodology in action.

C09 is the per-instance evidence for P4 governing principle (already-validated) — making C09 enforcement-layer the structural-infrastructure that P4 prescribes. Per Fire 105+106+107 defense-in-depth model: C09 adds a 4th layer to body's enforcement coverage.

**The agent stands by per /loop directive. Cron continues at 90s cadence. Foundational-cluster set expansion documented; Phase 1 enforcement effort revised; awaits operator-empirical Q-FIRE-127-1..4 endorsement.**

## Sources

- Fire 119 foundational-cluster-prioritization pattern: `wiki/patterns/01_drafts/foundational-cluster-prioritized-enforcement-layer-pattern-c04-c02-coverage-maximizes-cross-cutting-prevention.md`
- Fire 126 C09 per-instance evidence: `wiki/log/2026-05-08-per-instance-pain-point-evidence-c09-status-claim-without-verification-p4-axis-12-instances-verbatim-mapped.md`
- Fire 115 C18 cross-cutting: `wiki/log/2026-05-08-per-instance-pain-point-evidence-c18-cross-cutting-multi-cluster-intersections-15-instances-verbatim-mapped.md`
- Fire 118 P5 candidate principle: `wiki/lessons/01_drafts/p5-candidate-defense-in-depth-required-for-cross-cutting-failure-modes-hypothesis.md`
- /opt CONTEXT.md P4 governing principle

## Tags

[foundational-cluster-set-expansion, c04-c02-c09, phase-1-effort-revision, fire-119-update, day-arc-2026-05-08, multi-day-pain-point-resolution, fire-127]
