---
title: "Comprehensive Agent-Action-Emission Pipeline — 13-Gate Composition Architecture Across 4 Lifecycle Layers"
aliases:
  - "13-Gate Pipeline Architecture"
  - "Agent-Action Comprehensive Enforcement Composition"
  - "Cross-Cluster Integration Pattern"
  - "Multi-Axis Gate Composition"
type: pattern
domain: cross-domain
layer: 5
status: draft
confidence: high
maturity: seed
created: 2026-05-08
updated: 2026-05-08
last_reviewed: 2026-05-08
derived_from:
  - "13 sibling gate-design-spec pieces from 2026-05-08 multi-day work (each is a component this pattern composes)"
  - "P1 — Infrastructure Over Instructions for Process Enforcement"
  - "Documentation As Substitute For Discipline (sibling — meta-frame)"
  - "Strategic Coverage Validation log (sibling — provides architecture diagram)"
  - "Stress-Testing as Validation (sibling — promotion path)"
sources:
  - id: substitution-pattern
    type: wiki
    file: wiki/lessons/01_drafts/documentation-as-substitute-for-discipline-the-meta-pattern.md
    description: "META-FRAME parent. Establishes that all 13 gate-design-specs are aspirational without enforcement; this pattern shows how they compose into unified pipeline architecture."
  - id: strategic-coverage-validation-log
    type: wiki
    file: wiki/log/2026-05-08-strategic-coverage-validation-180-pain-points-to-17-solution-pieces.md
    description: "DIRECT sibling 2026-05-08. Provides the architecture diagram + composition map; this pattern formalizes that diagram into a canonical pattern."
  - id: stress-testing-validation-lesson
    type: wiki
    file: wiki/lessons/01_drafts/stress-testing-as-validation-the-only-way-to-surface-aspirational-vs-operational-gaps.md
    description: "DIRECT sibling 2026-05-08. Specifies promotion-path validation mechanism that applies to ALL 13 gates this pattern composes."
  - id: agent-context-discipline-c04
    type: wiki
    file: wiki/lessons/01_drafts/agent-context-discipline-is-aspirational-without-enforcement-gates-not-reading-what-exists.md
    description: "C04 — input-side gate component"
  - id: agent-decision-territory-c02
    type: wiki
    file: wiki/lessons/01_drafts/agent-decision-vs-operator-decision-boundary-discrimination-pre-action-gate.md
    description: "C02 — territory-axis gate component"
  - id: agent-authorship-c06
    type: wiki
    file: wiki/lessons/01_drafts/agent-authored-content-must-be-flagged-vs-operator-canonical-the-fabrication-cure.md
    description: "C06 — authorship-axis gate component"
  - id: conflation-detection-c07
    type: wiki
    file: wiki/lessons/01_drafts/conflation-detection-at-hook-layer-the-rename-strategy-generalized.md
    description: "C07 — semantic-axis gate component"
  - id: correction-calibration-c08
    type: wiki
    file: wiki/patterns/01_drafts/correction-as-calibration-pre-edit-verification-gate-design.md
    description: "C08 — correction-shape-axis gate component"
  - id: blast-radius-c14
    type: wiki
    file: wiki/patterns/01_drafts/blast-radius-classification-and-pre-action-severity-gate.md
    description: "C14 — severity-axis gate component"
  - id: regression-test-c03
    type: wiki
    file: wiki/patterns/01_drafts/pre-edit-regression-test-gate-canonical-verified-edit-enforcement.md
    description: "C03 — regression-prevention-axis gate component"
  - id: drift-detection-c13
    type: wiki
    file: wiki/patterns/01_drafts/active-task-anchor-and-drift-detection-gate-design.md
    description: "C13 — drift-axis gate component"
  - id: methodology-stage-c10
    type: wiki
    file: wiki/patterns/01_drafts/methodology-stage-gate-edit-land-enforcement-design.md
    description: "C10 — stage-class-axis gate component"
  - id: class-9-freeze-c09
    type: wiki
    file: wiki/lessons/01_drafts/freeze-after-correction-is-class-9-of-agent-failure-taxonomy-abdication-as-freeze.md
    description: "C09 — output-substance Stop-hook gate component"
  - id: sb-iteration-c12
    type: wiki
    file: wiki/patterns/01_drafts/systemic-bug-tracker-priority-shift-cycle-step-design.md
    description: "C12 — SB-iteration cycle-step gate component"
  - id: postcompact-mirror-c05
    type: wiki
    file: wiki/patterns/01_drafts/post-compact-orientation-mirror-and-handoff-doc-completeness-gate.md
    description: "C05 — PostCompact lifecycle gate component"
  - id: task-shape-calibration-c11
    type: wiki
    file: wiki/lessons/01_drafts/task-shape-vs-response-shape-calibration-the-thin-output-cure.md
    description: "C11 — per-response measurement layer component"
  - id: recurrence-quantification-c15
    type: wiki
    file: wiki/patterns/01_drafts/pattern-recurrence-quantification-and-operator-frustration-as-signal.md
    description: "C15 — cross-session measurement layer component"
  - id: principle-1
    type: wiki
    file: wiki/lessons/04_principles/hypothesis/infrastructure-over-instructions-for-process-enforcement.md
    description: "P1 governing principle"
tags: [pattern, p1-specialization, comprehensive-enforcement-architecture, 13-gate-composition, cross-cluster-integration, multi-axis-pipeline, mission-2026-05-06, day-arc-2026-05-08, multi-day-pain-point-resolution]
---

# Comprehensive Agent-Action-Emission Pipeline — 13-Gate Composition Architecture

## Summary

The 2026-05-08 multi-day work authored 13 distinct gate-design-spec pieces (C02, C03, C04, C05, C06, C07, C08, C09, C10, C11, C12, C13, C14, C15) — each a structural-enforcement specification for a specific axis of agent-action-emission discipline. Individually they address one cluster of pain-points; composed they form a comprehensive pipeline architecture spanning 4 lifecycle layers (cold-start lifecycle · pre-action gates · post-action gates · measurement). The substitution-pattern lesson is the cross-cutting meta-frame establishing that all 13 are aspirational without enforcement. **The GAP this pattern fills**: the strategic-coverage-validation log provides the architecture diagram inline; this pattern formalizes the composition into a canonical pattern doc with explicit precedence rules + cross-gate communication contracts + unified bypass protocol + composite operational-compliance metric. The architecture is THE deliverable the operator's multi-day work has been building toward — 13 gates composed into unified discipline-enforcement pipeline.

## Pattern Description

The pattern composes 13 gate-design-specs across 4 lifecycle layers + 1 cross-cutting frame:

### Layer 1 — Cold-Start Lifecycle (2 gates)

Fire when session begins or after compaction destroys conversational context.

| Gate | Source piece | Event | Purpose |
|---|---|---|---|
| **SessionStart orientation** | Existing 03_validated `session-orientation-pair` pattern | SessionStart | Force /orient invocation; load brain pieces; emit ORIENT REPORT |
| **PostCompact orientation mirror** | C05 — `post-compact-orientation-mirror-and-handoff-doc-completeness-gate` | PostCompact | Mirror SessionStart for compaction events; pre-compact completeness gate + post-compact behavior gate; STATE-RECOVERY REPORT |

### Layer 2 — Pre-Action Gates (PreToolUse, 9 orthogonal axes)

Fire BEFORE Edit / Write / NotebookEdit / Bash / WebFetch / WebSearch land. Each axis is independent; same action can fire multiple gates.

| Axis | Gate | Source piece | Block trigger |
|---|---|---|---|
| **Input-discipline** | re-read-before-edit + look-on-explicit-directive + query-existing-before-author | C04 | File mtime > last-Read; operator-said "look at X"; wiki/lessons-write without prior gateway query |
| **Decision-territory** | premise-confirmation + agent-vs-operator-territory + user-only-discovery | C02 | Operator-territory action without grant; agent-construction premise without verification; `authority: user-only` command auto-invoked |
| **Authorship-canonical** | maturity-tier promotion + citation-tier annotation | C06 | Agent-authored content auto-promoted above seed; agent-authored citation without authorship parenthetical |
| **Semantic-conflation** | 4-sub-axis discriminator (slash-vs-prose · conditional-clause · demonstrative-pronoun · paraphrase-without-citation) | C07 | Bare prose word matches command; conditional + immediate co-occur; this/that without referent; agent paraphrases without verbatim cite |
| **Correction-shape** | calibrate-vs-swing detector | C08 | Edit reverses last edit-direction with magnitude ≥80%; oscillation across 2+ corrections |
| **Severity** | 4-tier blast-radius (T1 catastrophic / T2 high / T3 medium / T4 low) | C14 | T1 without operator-grant-this-turn; T2 without REASON env var |
| **Regression-prevention** | tests-pass-before-edit-lands + cascading-fix detector | C03 | Target file has tests + tests not run pre-edit OR new failures introduced |
| **Drift** | active-task-anchor + drift-audit + cascading-drift detector | C13 | Action target ∉ active-task scope; 3+ consecutive different-task actions |
| **Stage-class** | ALLOWED/FORBIDDEN per-stage + quickfix-pattern detector | C10 | Edit's output-class ∈ FORBIDDEN list for current_stage; workaround-naming or condition-add patterns |

### Layer 3 — Post-Action Gates (Stop hook, 2 gates)

Fire on Stop event after agent completes a turn.

| Gate | Source piece | Block trigger |
|---|---|---|
| **Output-substance** | bare-standby + iteration-circuit-breaker | C09 (Class 9 freeze) | Cycle output ends with bare-standby (no concrete blocker); iter N+3 of same approach without convergence |
| **SB-iteration substance** | auto-pick + claim-shape + tracker-auto-update | C12 | Cycle without SB-action-claim OR claim-shape doesn't match 4 valid forms (structural-fix / verification / recurring-flag / explicit-standby) |

### Layer 4 — Measurement (2 layers)

Aggregate per-event metrics; surface trends over time.

| Layer | Source piece | Output |
|---|---|---|
| **Per-response** | C11 task-shape-vs-response-shape calibration | Composite score 0.7-1.3 = calibrated; <0.7 thin-output; >1.3 scope-expansion |
| **Cross-session** | C15 pattern-recurrence quantification + operator-frustration as signal | Recurrence-rate per failure-class · operator-frustration correlation · threshold-trigger escalation |

### Cross-Cutting — Meta-Frame (1 lesson)

| Frame | Source piece | Purpose |
|---|---|---|
| **substitution-pattern** | Documentation As Substitute For Discipline | Establishes that all 13 gates are aspirational without enforcement; provides recursive applicability principle |

## Gate-Precedence Ordering

When same action triggers multiple gates, ordering matters for performance + diagnostic clarity:

```
1. PreCompact completeness gate (if compaction event)
2. PostCompact orientation gate (if just-after-compact)
   ↓
3. Input-discipline gate (C04) — read-before-edit
4. Decision-territory gate (C02) — verify-territory
5. Authorship-canonical gate (C06) — verify-authorship-tag (for wiki-write actions)
6. Semantic-conflation detector (C07) — flag ambiguity warnings (advisory; doesn't block)
   ↓
7. Correction-shape gate (C08) — calibrate-vs-swing
8. Severity gate (C14) — blast-radius classification
9. Regression-prevention gate (C03) — tests-pass + cascading-fix detector
10. Drift gate (C13) — active-task-anchor + audit
11. Stage-class gate (C10) — ALLOWED/FORBIDDEN per-stage
   ↓
[ACTION EXECUTES if all gates pass]
   ↓
12. Output-substance gate (C09) — bare-standby check
13. SB-iteration substance gate (C12) — claim-shape verification
14. Per-response measurement (C11) — task-shape composite score
   ↓
[End of turn]
   ↓
15. Cross-session measurement (C15) — aggregator runs periodically (not per-turn)
```

Ordering rationale:
- Lifecycle gates first (cold-start framing)
- Input-discipline before decision (must read before deciding)
- Cheap detectors before expensive (semantic-conflation cheap; regression-tests expensive)
- Action-time gates execute immediately before action lands
- Post-action gates verify substance after
- Measurement aggregation is asynchronous

## Cross-Gate Communication

Gates share state via filesystem files (avoid in-memory state that doesn't survive turn boundaries):

| Shared state file | Producers | Consumers |
|---|---|---|
| `~/.claude/active-task` | /task command | C13 drift-audit · C12 SB-iteration · C10 stage-class |
| `~/.claude/active-mission` + `active-focus` + `active-impediment` | /mission /focus /impediment commands | C13 drift-audit · all gates banner |
| `~/.claude/active-priorities` | /priorities command | mode-enforcement banner · all gates |
| `~/.claude/operator-grants/<tier>-<topic>.txt` | operator-grant ceremony | C14 severity-gate · C02 territory-gate |
| `~/.claude/test-coverage-map.json` | `tools/test_coverage_generate.py` | C03 regression-test-gate |
| `~/.claude/correction-tracker.json` | C08 calibration-gate | C08 calibration-gate (next turn) |
| `~/.claude/drift-trace.log` | C13 drift-audit | C15 cross-session aggregator |
| `~/.claude/severity-trace.log` | C14 severity-gate | C15 cross-session aggregator |
| `~/.claude/severity-audit.log` | C14 severity-gate | C15 cross-session aggregator · operator-review |
| `~/.claude/recurrence-counters/<sid>.json` | all sibling audit-emitters | C15 aggregator |
| `~/.claude/frustration-trace.log` | C15 frustration-quantification (extension to existing output-discipline-guard.sh) | C15 aggregator |
| `wiki/governance/systemic-bugs.md` | C12 tracker-auto-update | C12 next-cycle SB-pick |
| `wiki/governance/blockers.md` | /blockers command | C12 SB-iteration cycle-step |
| `wiki/log/<ts>-pre-compact-handoff.md` | C05 PreCompact gate | C05 PostCompact gate (next turn after compact) |

The state-file communication is INTENTIONAL — survives turn boundaries + compaction + session restart. In-memory only state would lose visibility post-compact.

## Unified Bypass Protocol

All 13 gates respect REASON env var bypass (per parent enforcement-mindful lesson):

```bash
REASON="<concrete justification>" <command-or-edit>
```

Bypass behavior:
- Block-tier gates (T1 catastrophic, FORBIDDEN-stage, premise-construction): require REASON; logged to per-gate audit trail
- Warning-tier gates (T2 high, calibrate-warning, drift-warning): warn but allow; track bypass-rate
- Advisory-tier gates (T3 medium, semantic-conflation): no bypass needed; warn-only

Bypass-rate aggregation: if a gate's bypass-rate >10% sustained, refine the gate's pattern per parent lesson SCOPE property (calibration loop). High bypass-rate = false-positive issue, not gate-effectiveness.

## Composite Operational-Compliance Metric

Per the strategic-coverage-validation log + Stress-Testing as Validation (C18):

```python
def compute_pipeline_compliance(per_session_logs) -> dict:
    """
    Composite metric across 13 gates:
    - Per-gate compliance rate (events blocked / events that should-have-been-blocked)
    - Per-gate false-positive rate (legitimate actions blocked)
    - Per-gate bypass rate (REASON-bypass events / total)
    - Composite operational compliance: weighted average
    """
    return {
        "C04_compliance": 0.96,  # per stress-test
        "C02_compliance": 0.92,
        # ... per gate
        "composite": 0.94,  # weighted average
        "false_positive_rate": 0.04,
        "operator_perceived_coverage": 0.85,  # operator-empirical signal
    }
```

The composite metric IS the operational-vs-aspirational gap measurement per P4. Below threshold (e.g., <85%) → gates need refinement OR new gates needed for uncovered patterns.

## Pattern Components

| Component | Implementation File | Project | Status |
|---|---|---|---|
| 13 gate-design-spec pieces | This pattern's source-list | the second-brain | Authored 2026-05-08 (this multi-day work); all at 01_drafts |
| 13 gate-implementation hooks | `.claude/hooks/<gate-name>.sh` (Python) | /root | TO AUTHOR per piece (post-Ready-for-Review) |
| Cross-gate state files | `~/.claude/<file>` per table | /root + the second-brain | Some exist (active-task per SB-124d, active-mission/focus/impediment per SB-118); rest TO AUTHOR |
| Pipeline orchestrator | `tools/pipeline_orchestrator.py` (gate-precedence + skip-on-bypass) | /root | TO AUTHOR (post-implementation) |
| Composite metric aggregator | `tools/pipeline_compliance_audit.py` | /root + the second-brain | TO AUTHOR |
| Cross-project deployment | `/install-agent-brain` extension to deploy 13-gate pipeline | /root | TO EXTEND |
| Test files | per-gate test files + integration test for full pipeline | /root | TO AUTHOR |

## Instances

This pattern's instances ARE the 13 sibling gate-design-spec pieces from 2026-05-08 work. Each piece IS an instance contribution to the unified architecture. The empirical evidence:

| Empirical surface | Measurement | Source |
|---|---|---|
| Pain-point clusters covered | 15 of 15 (100%) | Strategic-coverage validation log |
| Pain-point instances mapped | 180 of 180 (100%) — each has at least one solution piece | Same |
| Underlying-failure categories covered | 5 of 5 (100%) | Master pain-points inventory |
| Operator-named structural-fix candidates forward-anchored | 7 of 7 (100%) | Strategic-coverage validation log |
| 13 gates pipeline-post validated | 0 errors across all 13 | Each fire's pipeline post |
| Gate-axes with orthogonal coverage | 9 PreToolUse + 2 Stop-hook + 2 lifecycle = 13 | This pattern |
| Composite operational compliance pre-implementation | 0% (gates are SPECIFICATIONS, not implementations) | Tautological |
| Composite operational compliance post-implementation (target) | ≥85% (per P1 quantified-evidence ~100% target with calibration tolerance) | Target per P1 |

## When To Apply

- **When designing comprehensive agent-action enforcement** — use this pattern's 13-gate architecture as reference; per-axis pieces provide details
- **When auditing existing /root hooks for gap analysis** — compare against 13-axis coverage; identify uncovered axes
- **When evaluating sister-project enforcement adoption** — pattern deploys via `/install-agent-brain`; per-axis or full-pipeline adoption
- **When operator stress-tests new structural-enforcement** — per piece #18 stress-test methodology; metrics aggregate per this pattern's composite
- **When operator promotes 01_drafts pieces to 02_synthesized** — per-piece promotion path requires implementation + stress-test data per piece #18; this pattern provides the integration view

## When Not To

- When project has no autopilot loops (gates designed for /loop /cycle autonomous-agent contexts)
- When project has no methodology-stage discipline (C10 stage-class gate inapplicable)
- When project has no tests (C03 regression-test gate inapplicable)
- When project doesn't experience compactions (C05 PostCompact gate skippable)
- When operator explicitly suspends pipeline for ad-hoc debugging — bypass via REASON

## Self-Check (audit procedure for gate-implementation work)

When implementing any of the 13 gates from specification → working hook:

1. **Has this gate been authored as 01_drafts spec?** Verify at piece's path; check cross-references.
2. **Are the gate's state files defined?** Check ~/.claude/ for input/output files this gate uses.
3. **Are sibling gates' state files writable?** Verify cross-gate communication contracts.
4. **Has stress-test methodology been authored?** Per piece #18 — real-session conditions, not synthetic.
5. **Is bypass protocol implemented?** REASON env var support per unified bypass.
6. **Is per-gate audit-log writable?** For C15 cross-session aggregation.
7. **Are tests authored?** Per piece's listed test file specifications.
8. **Does pipeline post pass?** Schema validation of any wiki content the gate produces.

If 1-4 skipped: gate-implementation is aspirational. Per piece #18: stress-test required for promotion.

## Composability with siblings

This pattern composes with ALL 17 sibling pieces from 2026-05-08 work:
- 13 gate-design-spec pieces are the COMPONENTS this pattern composes
- 1 substitution-pattern lesson is the META-FRAME
- 1 strategic-coverage-validation log is the COVERAGE EVIDENCE
- 1 stress-testing-as-validation lesson is the PROMOTION PATH
- 1 master pain-points inventory is the SCAFFOLDING

The 18 pieces (counting this integration pattern) form a coherent body of work covering the operator's multi-day workflow directive.

## Properties

| Property | Description |
|---|---|
| **9 PreToolUse axes orthogonal** | Same action can fire 5+ gates independently |
| **2 Stop-hook gates** | Substance + SB-iteration enforcement |
| **2 lifecycle-event gates** | Cold-start + compaction-recovery |
| **2 measurement layers** | Per-response + cross-session |
| **State-file communication** | All gates communicate via ~/.claude/ files (no in-memory state) |
| **Unified bypass** | All 13 respect REASON env var per parent enforcement-mindful lesson |
| **Operator-extensible** | Each gate's classifier/data is operator-curated |
| **Audit-friendly** | Composite metric measures operational compliance |
| **Sister-project portable** | Deploys via `/install-agent-brain` per brain-inheritance pattern |

## Relationships

- **DERIVED FROM** all 13 gate-design-spec sibling pieces from 2026-05-08 (each cited in source list)
- **DERIVED FROM** [Lesson — Documentation As Substitute For Discipline](../../lessons/01_drafts/documentation-as-substitute-for-discipline-the-meta-pattern.md) — META-FRAME parent
- **DERIVED FROM** [Strategic Coverage Validation log](../../log/2026-05-08-strategic-coverage-validation-180-pain-points-to-17-solution-pieces.md) — provides coverage evidence + architecture diagram
- **DERIVED FROM** [Lesson — Stress-Testing as Validation](../../lessons/01_drafts/stress-testing-as-validation-the-only-way-to-surface-aspirational-vs-operational-gaps.md) — promotion-path validation mechanism
- **DERIVED FROM** [Principle 1 — Infrastructure Over Instructions](../../lessons/04_principles/hypothesis/infrastructure-over-instructions-for-process-enforcement.md)
- **CONSTRAINS** all 13 gate implementations — each must respect this pattern's precedence + state-file contracts + unified bypass + audit-aggregation
- **EXTENDS** P1 quantified-evidence approach to multi-axis-pipeline composite measurement
- **FEEDS INTO** the 5-tier maturity progression: 01_drafts → 02_synthesized gated on:
  1. All 13 gates implemented (post-piece-#18 stress-test)
  2. Pipeline orchestrator authored
  3. Composite metric aggregator authored
  4. Cross-project deployment via `/install-agent-brain` tested
  5. Operational compliance ≥85% measured empirically
  6. Operator-confirmed promotion
- **Mission served**: 2026-05-06 brain-improvement mandate (failed) → 2026-05-08+ multi-day systematic pain-point resolution; this pattern is the cross-cluster integration architecture deliverable + Ready-for-Review evidence.

## Backlinks

(Auto-regenerated by `pipeline post`. All 17 sibling pieces accumulate this pattern as a backlink.)
