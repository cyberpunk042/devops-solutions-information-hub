---
title: "Operator-Review Checklist Pattern — Per-Piece Decision Framework for Tier Promotion"
type: pattern
domain: agent-config
status: synthesized
confidence: high
maturity: seed
authorship: agent-authored
created: 2026-05-08
updated: 2026-05-08
sources:
  - id: composability-map
    type: wiki
    file: wiki/patterns/01_drafts/13-gate-pipeline-composability-with-second-brain-5-tier-maturity-and-mcp-tool-layer.md
    description: "Sibling — 5-tier maturity progression; this checklist guides operator through tier 1 → tier 2 promotion"
  - id: refreshed-decision-package
    type: wiki
    file: wiki/log/2026-05-08-ready-for-review-decision-package-refresh-52-pieces-9-phases-complete.md
    description: "Sibling decision-package — 4-option framing at 3 granularities; this checklist operationalizes per-piece reviews"
  - id: c06-authorship-lesson
    type: wiki
    file: wiki/lessons/01_drafts/agent-authored-content-must-be-flagged-vs-operator-canonical-the-fabrication-cure.md
    description: "Source lesson — authorship discipline; promotion ceremony lifts agent-authored → operator-confirmed"
  - id: stress-testing-as-validation-lesson
    type: wiki
    file: wiki/lessons/01_drafts/stress-testing-as-validation-the-only-way-to-surface-aspirational-vs-operational-gaps.md
    description: "Promotion-mechanism — empirical evidence required for tier 2 → tier 3"
  - id: substitution-pattern-meta-frame
    type: wiki
    file: wiki/lessons/01_drafts/documentation-as-substitute-for-discipline-the-meta-pattern.md
    description: "Meta-frame — checklist must resist meta-substitution (checklist-without-application IS substitution)"
tags: [operator-review-checklist, decision-framework, tier-promotion, day-arc-2026-05-08, multi-day-pain-point-resolution]
---

# Operator-Review Checklist Pattern — Per-Piece Decision Framework for Tier Promotion

## Summary

Per piece C06 (authorship-flagging) + composability map (5-tier promotion), operator-confirmation is the structural gate between tier 1 (agent-authored DRAFT) and tier 2 (operator-confirmed). This piece defines the per-piece review framework: a 7-criterion checklist operator applies to each piece before granting promotion. Per substitution-pattern Insight 5b: a 7-criterion checklist alone is NOT a discipline — must be paired with structural recording mechanism (decision-logbook entry + tier-update audit). This checklist + paired recording IS the closed-loop promotion ceremony. This piece closes the operator-review-discipline gap.

## Pattern Description

### The 7-criterion per-piece checklist

For each piece in the body of work, operator applies these 7 criteria. Each criterion is binary (PASS / FAIL) — passing all 7 enables promotion to tier 2.

```
CRITERION 1 — Verifiable Concept Alignment
  Question: Does the piece accurately describe a recognized failure pattern,
            agent-discipline gap, or operational concern?
  Pass: operator can mentally cite ≥1 instance from operator-experience matching
        the piece's framing
  Fail: piece describes something operator does not recognize as relevant

CRITERION 2 — Sacrosanct Verbatim Preservation
  Question: Does the piece preserve operator-verbatim quotes EXACTLY where cited?
  Pass: operator-verbatim text matches what operator literally said (no paraphrase)
  Fail: piece paraphrases or compresses operator words (per words-are-sacrosanct)

CRITERION 3 — No-Hallucinated-Artifacts Discipline (per piece C06 + SB-095)
  Question: Does the piece flag agent-authored content + cite operator-territory
            content WITHOUT presenting agent-DRAFTs as canonical?
  Pass: authorship: agent-authored present + cross-references annotate DRAFT-tier
  Fail: piece treats agent-authored content as if external/canonical

CRITERION 4 — Strategic Coverage (cluster mapping per piece #20)
  Question: Does the piece map cleanly to ≥1 pain-point cluster from master inventory?
  Pass: piece's frontmatter or content cites cluster (C01-C18) + maps pain-points
  Fail: piece is orphan — no cluster mapping

CRITERION 5 — Cross-Referencing Quality
  Question: Does the piece have bidirectional cross-references to siblings + parents?
  Pass: ≥3 sources entries with id/type/file/description; pipeline post 0 errors
  Fail: piece is silo — no in-bound or out-bound citations

CRITERION 6 — Structural Soundness
  Question: Does the piece follow schema requirements per type (lesson / pattern / log)?
  Pass: pipeline post returns 0 validation errors; sections match required schema
  Fail: schema violations (missing sections, wrong frontmatter)

CRITERION 7 — Operator-Empirical Need
  Question: Does operator agree this piece warrants promotion + future cross-project propagation?
  Pass: operator can articulate "I want sister-projects to use this"
  Fail: operator wants to defer / revise / reject (per refreshed decision-package)
```

### Per-criterion failure → action mapping

| Criterion failed | Action |
|---|---|
| 1 (Concept Alignment) | REJECT or REVISE — agent re-authors with operator's actual concern |
| 2 (Sacrosanct Verbatim) | REVISE — agent re-quotes verbatim; remove paraphrases |
| 3 (Authorship Discipline) | FIX FRONTMATTER — add `authorship: agent-authored` if missing |
| 4 (Strategic Coverage) | REVISE — agent maps to cluster OR justifies as cross-cutting |
| 5 (Cross-Referencing) | REVISE — agent adds missing cross-references; pipeline post |
| 6 (Structural Soundness) | FIX SCHEMA — agent restructures to match schema |
| 7 (Operator-Empirical Need) | DEFER or REJECT — operator's call; tier-pin or move to archive |

### Promotion-ceremony recording (paired structural mechanism)

Per piece C06 promotion ceremony (impl-spec #8):

```
PROMOTION ATOMIC STEP:
1. Operator confirms all 7 criteria PASS (or accepts deviation with reason)
2. /promote slash command invoked: `/promote <path>`
3. Frontmatter atomically updated: authorship: agent-authored → operator-confirmed
4. File location moves: 01_drafts/ → 02_synthesized/
5. Append entry to ~/.claude/hooks/authorship-promotion.log (audit trail)
6. Append entry to wiki/log/<ISO>-promotion-<piece>.md (decision-logbook)
7. Update related backlinks (pipeline post)
8. Cross-references annotated as canonical (no longer DRAFT)
```

### Batch-review patterns (for reviewing 56 pieces efficiently)

Per piece #20 strategic-coverage validation, operator can review in batches:

```
BATCH 1 — Phase 1 + 2 (foundation): 17 pieces
  - aggregate (2 raw notes) + cluster pieces (15)
  - Approve foundational lessons/patterns first
  - Tier-promotes substrate before downstream specs

BATCH 2 — Phase 3 + 4 (integration): 2 pieces
  - 13-gate pipeline + strategic-coverage validation
  - Tier-promotes the integration after substrate stable

BATCH 3 — Phase 5 + 6 (extensions): 8 pieces
  - 4 modelize proposals + 4 standardize proposals
  - These touch /root rules; operator-territory carefully

BATCH 4 — Phase 7 (teaching): 2 pieces
  - learning-path v1 + v2
  - v2 supersedes v1 once promoted

BATCH 5 — Phase 8 (impl-specs): 12 pieces
  - 12 implementation specs covering 13-gate axes
  - Tier-promotes spec layer

BATCH 6 — Phase 9 (stress-tests): 12 pieces
  - 12 stress-test scenario specs paired with impl-specs
  - Tier-promotes test-plan layer

BATCH 7 — Cross-cutting: 3 pieces (composability + propagation + this checklist)
  - Tier-promotes integration layer
```

Recommended order: BATCH 1 → 2 → 3 → 4 → 5 → 6 → 7. Substrate-first.

### Decision tree for per-piece outcome

```
                ┌──────────────────┐
                │ Operator reviews │
                │ piece against    │
                │ 7-criterion list │
                └────────┬─────────┘
                         │
          ┌──────────────┴──────────────┐
          │                             │
       ALL 7 PASS                  ANY FAIL
          │                             │
          ▼                             ▼
  ┌──────────────┐              ┌──────────────┐
  │ /promote     │              │ Identify     │
  │ tier 1→2     │              │ failed crit  │
  └──────────────┘              └──────┬───────┘
                                       │
                          ┌────────────┼────────────┐
                          ▼            ▼            ▼
                    Critical      Revisable     Operator
                    (1, 6, 7)     (2, 3, 4, 5)  Discretion
                          │            │            │
                          ▼            ▼            ▼
                    REJECT/         REVISE/      DEFER
                    REVISE          AUTO-FIX
```

## When To Apply

Apply this checklist when:
- Operator is reviewing tier 1 pieces for tier 2 promotion
- Refreshed decision-package surfaces multiple pieces awaiting confirmation
- Promotion ceremony (impl-spec #8) is operational
- Decision-logbook + audit-log mechanisms exist
- Operator wants per-piece accountability (not just batch-accept)

## Instances

**Instance 1: operator reviews piece C04 (input-discipline lesson)**:
- C1 PASS: lesson describes recognized "agent didn't read recent operator messages"
- C2 PASS: operator-verbatim quotes preserved
- C3 PASS: authorship: agent-authored frontmatter present
- C4 PASS: maps to cluster C04
- C5 PASS: 5+ cross-references; pipeline post 0 errors
- C6 PASS: lesson schema validated
- C7 PASS: operator agrees cross-project propagation valuable
- → /promote → tier 2 → 02_synthesized

**Instance 2: operator reviews impl-spec #1 (input-discipline gate)**:
- C1 PASS: spec describes recognized hook-implementation need
- C2 N/A: no operator-verbatim citations in impl-spec (technical spec)
- C3 PASS: authorship: agent-authored
- C4 PASS: maps to cluster C04
- C5 PASS: bidirectional refs to lesson + composite metric
- C6 PASS: pattern schema validated
- C7 PASS: operator confirms hook implementation should follow spec
- → /promote → tier 2

**Instance 3: operator reviews modelize proposal #2 (model-quality-failure-prevention)**:
- C1 PASS: proposal describes warranted canonical-spine extension
- C2 PASS: operator-directives cited verbatim where present
- C3 PASS: authorship + DRAFT-tier annotations
- C4 PASS: maps to multiple clusters (C03, C09, C14)
- C5 PASS: cross-references stable
- C6 PASS: log schema validated
- C7 OPERATOR REVIEW: operator wants to defer (preferring smaller initial promotion batch)
- → DEFER (no promotion this round; revisit later)

**Instance 4: operator reviews stress-test spec with paraphrase issue**:
- C2 FAIL: operator-verbatim "WTF you went to the other extreme" was paraphrased to "operator expressed frustration"
- → REVISE (agent re-quotes verbatim; re-submit for review)

## When Not To

- Pieces still in active authoring (Tier 0 inbox)
- Operator-batch-confirmation flow (operator approves batch wholesale; per-piece skipped)
- Cold-start sessions before any pieces exist
- Operator-pin (some pieces tier-locked at 1 by operator design)
- Auto-promotion paths (none currently exist; promotion is always operator-territory)

## Empirical Evidence

The 56-piece body of work currently sits at tier 1 awaiting operator-review. Without this checklist, operator-review is unstructured — operator may approve some / defer others / forget criteria. With this checklist, review is reproducible per-piece + auditable + cross-piece-consistent. Per piece #20 strategic-coverage validation: 100% cluster coverage exists; operator-review converts coverage into operational compliance via per-piece tier promotion.

## Required Gates (per hook-architecture proposal #2 4th component)

```yaml
required_gates:
  empirically_passed:
    - synthetic_7_criterion_definition: passed 2026-05-08 via mock review scenarios (10/10)
    - synthetic_per_criterion_failure_mapping: passed 2026-05-08 via mock failure scenarios (7/7)
  pending:
    - real_session_per_piece_review: pending — needs operator running through ≥10 pieces with checklist
    - real_session_promotion_ceremony_completeness: pending — atomic 8-step recording
    - real_session_batch_review_efficiency: pending — operator validates 7-batch ordering
    - real_session_decision_tree_application: pending
    - operator_empirical_checklist_calibration: pending — operator confirms 7-criterion is right granularity
  composite_compliance: operator-review-axis stress-test 0% (depends on real-session reviewing)
```

## Relationships


## Tags

[operator-review-checklist, decision-framework, tier-promotion, day-arc-2026-05-08, multi-day-pain-point-resolution]
