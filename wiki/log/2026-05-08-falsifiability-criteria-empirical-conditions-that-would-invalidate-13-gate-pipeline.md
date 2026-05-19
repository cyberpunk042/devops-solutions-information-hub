---
title: "Falsifiability Criteria — Empirical Conditions That Would Invalidate the 13-Gate Pipeline"
type: note
note_type: session
domain: log
status: synthesized
confidence: high
created: 2026-05-08
updated: 2026-05-08
sources:
  - id: comprehensive-13-gate-pattern
    type: wiki
    file: wiki/patterns/01_drafts/comprehensive-agent-action-emission-pipeline-13-gate-composition-architecture.md
    description: "PRIMARY parent — 13-gate central pattern; this log articulates falsifiability criteria for each gate"
  - id: stress-testing-as-validation-lesson
    type: wiki
    file: wiki/lessons/01_drafts/stress-testing-as-validation-the-only-way-to-surface-aspirational-vs-operational-gaps.md
    description: "Source — promotion-mechanism per piece #18; falsifiability criteria are the inverse (demotion-mechanism)"
  - id: composite-compliance-implementation-spec
    type: wiki
    file: wiki/patterns/01_drafts/composite-operational-compliance-metric-implementation-spec-measurement-layer-aggregator.md
    description: "Source — composite-metric formula; falsifiability operationalizes via metric-thresholds"
  - id: body-of-work-composite-metric-self-application
    type: wiki
    file: wiki/log/2026-05-08-body-of-work-composite-metric-self-application-meta-validation.md
    description: "Sibling — meta-validation showed 99.51% baseline; falsifiability criteria identify when body would be invalidated"
  - id: substitution-pattern-meta-frame
    type: wiki
    file: wiki/lessons/01_drafts/documentation-as-substitute-for-discipline-the-meta-pattern.md
    description: "Meta-frame — body without falsifiability criteria IS aspirational at scientific-discipline layer"
tags: [falsifiability, empirical-conditions, popper-style, demotion-mechanism, day-arc-2026-05-08, multi-day-pain-point-resolution]
---

# Falsifiability Criteria — Empirical Conditions That Would Invalidate the 13-Gate Pipeline

## Summary

Per scientific-discipline tradition (Popper-style falsifiability) + piece #18 stress-testing-as-validation: a body of work claiming empirical value MUST specify what operational conditions would FALSIFY it. The 13-gate pipeline body claims to address 180 pain-points across 15 clusters with empirical compliance ≥85% target. This log specifies the inverse: what empirical conditions would invalidate those claims. Per substitution-pattern Insight 5b: declaring empirical claims without falsifiability criteria is aspirational at scientific-discipline layer (claim-without-falsifiability IS substitution). This piece closes the falsifiability-criteria gap.

## Why falsifiability matters

A body of work that cannot be falsified cannot be validated. Per Popper:
- "All non-trivial claims must be falsifiable"
- "Failure to specify what would disprove a claim makes the claim non-empirical"

The 13-gate pipeline currently claims:
- 100% pain-point traceability (per piece #61 + #79)
- 100% paired-enforcement coverage (per piece #65)
- 100% Phase 10 internal coherence (per piece #74)
- 99.51% body-of-work composite-compliance self-application (per piece #85)
- ≥85% target post-implementation (per impl-spec #12)

Without falsifiability criteria, these claims are unfalsifiable assertions. With falsifiability criteria, they become empirically-disprovable predictions.

## Per-axis falsifiability criteria

For each of the 12 axes (excluding self-referential axis #12):

### Axis #1 — input-discipline: falsified IF...

**Falsification condition**: 30-day rolling axis-compliance < 70%

**Specific empirical evidence that would falsify**:
- Agent invokes Edit/Write WITHOUT prior Read on relevant the second-brain pieces in ≥30% of cycles for 30+ days
- CHECK 3 (opt-pieces) bypass with "weak_bypass_*" flag in ≥10 cycles per 30-day window
- Operator-empirical complaint: "agent re-authored content existing in the second-brain" (Insight 5b violation) ≥3 times per 30-day window

**Mitigation if falsified**: revise impl-spec #1 (e.g., enrich CHECK 3 gateway query taxonomy; tighter pattern-matching for relevance).

### Axis #2 — decision-territory: falsified IF...

**Falsification condition**: ≥1 unauthorized /root rule edit OR ≥3 unauthorized operator-canonical demotions per 30-day window

**Specific empirical evidence**:
- Agent edits /root/.claude/rules/*.md WITHOUT REASON= operator-grant citation
- Agent demotes operator-canonical content in cross-project context without authorization
- Operator-empirical complaint: "you edited /root without my permission"

**Mitigation if falsified**: tighten RULE 1 path patterns in impl-spec #2 + emit HARD BLOCK (currently SOFT-BLOCK in some scenarios).

### Axis #3 — regression-test: falsified IF...

**Falsification condition**: Verified-edit claims (Hard Rule 14) without inline test-runner output in ≥30% of edits per 30-day window

**Specific empirical evidence**:
- Agent claims "edit complete" without `pipeline post` 0-error inline output
- Agent ships regression that passes pre-edit baseline but fails post-edit (caught only by operator)
- Operator-empirical complaint: "tests are broken now"

**Mitigation if falsified**: enforce regression-test gate as MANDATORY for TEST-REQUIRING paths (currently allows broken-baseline graceful-degradation).

### Axis #4 — severity (T1-T4): falsified IF...

**Falsification condition**: ≥1 T1 catastrophic action executed without operator-explicit grant per 30-day window

**Specific empirical evidence**:
- Agent runs `git push --force origin main` without REASON= operator-grant-citation
- Agent edits /etc/, /boot/, /usr/, /lib/ without bypass
- Agent runs `rm -rf` on production paths

**Mitigation if falsified**: HARD-FAIL gate (currently allows weak-bypass with warning); audit-log every T1 attempt + deny without grant-citation + auto-escalate to operator-pending-decision.

### Axis #5 — correction-shape: falsified IF...

**Falsification condition**: extreme-swing pattern (suppress↔render or equivalent) repeats ≥3 times within 5-cycle window per 30-day window

**Specific empirical evidence**:
- Operator: "you went to the other extreme AGAIN" pattern recurs ≥3 cycles per month
- consecutive_corrections_count exceeds 3 in ≥2 distinct dimensions per 30-day window
- Circuit-breaker auto-escalation triggered ≥3 times per 30-day window

**Mitigation if falsified**: tighten extreme-swing detection in impl-spec #5 (currently uses opposite-extreme heuristic; may need calibrated threshold).

### Axis #6 — drift-detection: falsified IF...

**Falsification condition**: Hard-drift edits per cycle ≥5 per 30-day window OR cycle-history shows ≥30% cycles with drift_event_count > 5

**Specific empirical evidence**:
- Active-task scope violated repeatedly without /task set re-anchor
- Operator-empirical complaint: "you're doing X but I asked for Y"

**Mitigation if falsified**: tighten paths_in_scope/paths_explicitly_out per task scope-pattern + auto-/task set prose-detection refinement.

### Axis #7 — stage-class: falsified IF...

**Falsification condition**: Stage-class violations (FORBIDDEN edits) per 30-day window > 10 instances

**Specific empirical evidence**:
- Implementation edits in document-stage tasks
- New tests in implement-stage tasks (not test-stage)
- Operator-empirical complaint: "you wrote code in a document-stage task"

**Mitigation if falsified**: methodology engine consultation tightened (impl-spec #7 SOURCE 3 query becomes mandatory pre-edit) + standardize proposal #3 application accelerated.

### Axis #8 — authorship: falsified IF...

**Falsification condition**: ≥1 piece tagged operator-canonical without operator-promotion ceremony OR ≥3 demotion attempts without grant per 30-day window

**Specific empirical evidence**:
- Agent-authored piece appears at the second-brain with `authorship: operator-canonical` without /promote ceremony audit-log entry
- Operator-empirical complaint: "you tagged your own draft as canonical"

**Mitigation if falsified**: HARD-DENY frontmatter-modification on `authorship: operator-canonical` field without operator-grant.

### Axis #9 — semantic-conflation: falsified IF...

**Falsification condition**: ≥3 paraphrase-without-citation events OR ≥3 conditional-clause-as-current-imperative events per 30-day window

**Specific empirical evidence**:
- Agent text claims "operator rejected X" without verbatim citation
- Agent acts on "after we will" conditional clause as current
- Agent invokes /checkin on prose "continue"

**Mitigation if falsified**: tighten Detector 1-4 patterns in impl-spec #9 + emit BLOCK (not just banner) for paraphrase-without-citation.

### Axis #10 — post-compact: falsified IF...

**Falsification condition**: ≥1 first-action-after-compact bypass without /orient invocation per 30-day window

**Specific empirical evidence**:
- post-compact-pending-orient.flag bypassed via REASON= without legitimate emergency
- Cycle resumes post-compaction without state-file re-load

**Mitigation if falsified**: HARD-FAIL gate; bypass-without-emergency-grant denied.

### Axis #11 — pattern-recurrence: falsified IF...

**Falsification condition**: same-axis recurrence ≥5 in single cycle without auto-escalation per 30-day window

**Specific empirical evidence**:
- Same gate fires ≥5x in cycle without circuit-breaker triggering
- cross-cycle pattern detected ≥5 cycles without surfacing to operator

**Mitigation if falsified**: lower auto-escalation threshold (currently ≥3); add intermediate-warning at ≥3.

### Axis #12 — composite-compliance: falsified IF...

**Falsification condition**: 30-day rolling composite < 70% sustained for 14+ days

**Specific empirical evidence**:
- Composite drops from baseline + stays low for 2+ weeks
- Operator-empirical complaint: "the pipeline is just noise; nothing's getting through"

**Mitigation if falsified**: re-evaluate weights (impl-spec #12 operator-revision); per-axis investigation for axes pulling composite down; potentially tier-2-demote pieces.

## Aggregate falsifiability matrix

| Falsification scenario | Severity | Mitigation tier |
|---|---|---|
| Single-axis < 70% for 30 days | per-axis revision | Tier-2-revision (axis impl-spec) |
| Composite < 70% sustained 14+ days | systemic concern | Tier-1-demotion path activated |
| ≥3 axes < 70% concurrently | severe systemic | Tier-1-demotion + body re-evaluation |
| Operator-empirical override (e.g., "this whole thing isn't working") | trumps all | Demotion ceremony + agent-revise |

## Body-of-work falsifiability self-application

Per piece #85 composite-metric self-application: body achieves 99.51% on 11 axes. Falsification of body would require:

| Body-falsification condition | Empirical evidence required |
|---|---|
| Composite drops below 85% | impl-spec failures sustained 30 days |
| Operator-empirical "this body of work doesn't help" | operator review reveals ≥30% pieces don't address actual operator concerns |
| Cross-project propagation FAILS | sister-projects sustain <70% per-axis after /install-agent-brain adoption |
| Tier-4 candidate (P5+) FAILS to converge | <3 sister-projects sustain ≥85% per axis post-30-day |

## Demotion path (if falsification occurs)

Per piece #2 always-flexible + piece #58 implementation-roadmap reverse-promotion preview:

```
TIER-DEMOTION CASCADE:

Tier-3 → Tier-2 demotion (if 30-day metric drops):
  - Operator-confirms via /demote ceremony
  - Files move 03_validated/ → 02_synthesized/
  - Sister-projects notified
  - Pattern-recurrence aggregator captures demotion pattern

Tier-2 → Tier-1 demotion (if operator-empirical reveals fundamental flaw):
  - Operator-confirms via /demote
  - Files move 02_synthesized/ → 01_drafts/seed
  - Re-author candidates surface

Tier-1 → archived (if operator concludes piece deprecated):
  - Operator-confirms via /archive
  - Files move 01_drafts/ → archived/
  - Cross-references annotated as DEPRECATED

Falsification-driven demotion is RARE. Most falsifications trigger per-axis IMPL-SPEC revision (Tier-2-revision), not body-wide demotion.
```

## Falsifiability vs aspirational claims

| Type of claim | Falsifiable? |
|---|---|
| "13-gate pipeline addresses 180 pain-points" | YES — specifically; failure < 80% of pain-points addressed at empirical-test-time falsifies |
| "Per-axis empirical compliance ≥85% sustained 30 days" | YES — composite-metric trends < 70% for 14+ days falsifies |
| "Cross-project propagation enables tier-4" | YES — sister-projects fail to adopt OR fail to sustain ≥85% per axis falsifies |
| "Substitution-pattern recursive-applicability solved" | YES — body itself fails ≥85% self-applied composite falsifies |
| "Operator-empirical respect maintained" | YES — operator complaints "you violated my territory" ≥3 times falsifies |

ALL major claims are falsifiable per specific empirical conditions.

## Operator-empirical preview

When operator asks "how would I know this body of work is wrong?":

Ready-answer: 6 falsification scenarios surfaced + per-axis empirical-evidence requirements + demotion-path reversibility. The body is empirically-falsifiable; sustained empirical evidence (M5-M7) determines validation OR falsification.

## Composability with prior pieces

| Prior piece | Falsifiability complement |
|---|---|
| Piece #18 stress-testing-as-validation | Validation criteria; this log's falsification criteria are the inverse |
| Piece #58 implementation-roadmap | Forward-anchored M1-M7 success path; this log specifies failure path |
| Piece #65 recursive-applicability audit | 100% paired-enforcement validation; this log specifies under what conditions paired-enforcement would be insufficient |
| Piece #85 composite-metric self-application | 99.51% baseline; this log specifies what would drop the baseline materially |
| Piece #86 tier-4 candidate analysis | P5+ promotion path; this log specifies what would PREVENT tier-4 promotion |

## Sources

- 13-gate central pattern: `wiki/patterns/01_drafts/comprehensive-agent-action-emission-pipeline-13-gate-composition-architecture.md`
- Stress-testing-as-validation lesson: `wiki/lessons/01_drafts/stress-testing-as-validation-the-only-way-to-surface-aspirational-vs-operational-gaps.md`
- Composite-compliance impl-spec #12: `wiki/patterns/01_drafts/composite-operational-compliance-metric-implementation-spec-measurement-layer-aggregator.md`
- Body-of-work self-application (Fire 85): `wiki/log/2026-05-08-body-of-work-composite-metric-self-application-meta-validation.md`
- Substitution-pattern meta-frame: `wiki/lessons/01_drafts/documentation-as-substitute-for-discipline-the-meta-pattern.md`

## Tags

[falsifiability, empirical-conditions, popper-style, demotion-mechanism, day-arc-2026-05-08, multi-day-pain-point-resolution]
