---
title: "Body-of-Work Versioning Pattern — Explicit Versioning Discipline for Body Evolution"
type: pattern
domain: agent-config
status: synthesized
confidence: high
maturity: seed
authorship: agent-authored
created: 2026-05-08
updated: 2026-05-08
sources:
  - id: sustained-feedback-loop-pattern
    type: wiki
    file: wiki/patterns/01_drafts/sustained-feedback-loop-pattern-post-m7-operator-empirical-findings-routing-to-body-refinement.md
    description: "Sibling — post-M7 sustained evolution; this pattern adds versioning discipline to that evolution"
  - id: composability-map
    type: wiki
    file: wiki/patterns/01_drafts/13-gate-pipeline-composability-with-second-brain-5-tier-maturity-and-mcp-tool-layer.md
    description: "Sibling — 5-tier maturity progression; versioning happens within + across tiers"
  - id: implementation-roadmap-pattern
    type: wiki
    file: wiki/patterns/01_drafts/implementation-roadmap-pattern-sequenced-milestones-from-confirmation-to-tier-3.md
    description: "Source — M1-M7 milestones; each milestone could trigger version increment"
  - id: refreshed-decision-package-v3
    type: wiki
    file: wiki/log/2026-05-08-ready-for-review-decision-package-refresh-v3-74-pieces-phase-10-coherence-complete.md
    description: "Sibling — decision-package v3; iterative refresh history per body version"
  - id: substitution-pattern-meta-frame
    type: wiki
    file: wiki/lessons/01_drafts/documentation-as-substitute-for-discipline-the-meta-pattern.md
    description: "Meta-frame — body-without-versioning ages opaquely; versioning makes evolution legible"
tags: [body-versioning, evolution-tracking, semver-style, meta-discipline, day-arc-2026-05-08, multi-day-pain-point-resolution]
---

# Body-of-Work Versioning Pattern — Explicit Versioning Discipline for Body Evolution

## Summary

Per piece #90 sustained-feedback-loop pattern: post-M7 the body continues evolving via 5 refinement-output forms. Per piece #55 composability map: 5-tier maturity progression. The body needs explicit versioning discipline analogous to semantic-versioning (semver) so evolution is legible to operator + sister-projects + future agents. This pattern specifies: when version increments; what counts as breaking change; how versions interact with tier-promotion; cross-version compatibility. Per substitution-pattern Insight 5b: body without versioning is illegible at evolution layer (illegibility-as-substitute-for-versioning). This piece closes the versioning-discipline gap.

## Pattern Description

### Semver-style versioning for body of work

Adopt MAJOR.MINOR.PATCH versioning:

```
MAJOR — fundamental architecture change
  - 13-gate count changes (e.g., 14-gate or 12-gate)
  - Tier-promotion ceremony fundamentally redesigned
  - Substitution-pattern meta-frame challenged + replaced

MINOR — body extension or new piece-types
  - New cluster axis added (axis #14)
  - New piece-type introduced (e.g., implementation cookbook)
  - Significant cross-cutting integration added (e.g., new lifecycle event)

PATCH — refinements within existing structure
  - Impl-spec revision (per Fire 90 Form 1)
  - Stress-test extension (Form 2)
  - Schema corrections / cross-reference updates
```

### Current body version assignment

Per this work block (88 substantive pieces + 4 decision-packages + Fire 90 sustained-feedback-loop pattern + Fire 91 this versioning pattern):

```
Body of Work v1.0.0 (initial release)
  - 90+ pieces; 10 phases
  - Tier-1 across all pieces (`01_drafts/seed`)
  - 13-gate pipeline central architecture
  - 5 governing-principle candidates forward-anchored (P5-P8)
```

### Forward-anchored version increments

```
v1.0.0 (current; this work block) — pre-M0 authoring complete
v1.0.1 (post-M3) — synthetic stress-tests pass; PATCH refinements
v1.0.2 (post-M4) — real-session stress-tests pass; PATCH refinements
v1.0.3 (post-M5) — composite baseline emitting; PATCH calibrations

v1.1.0 (post-M6) — tier-2 promotion of subset; MINOR (some pieces become canonical)
v1.2.0 (post-M7) — tier-3 sustained ≥85%; MINOR (full body validated)

v1.3.0 (post-tier-3 + sister-project propagation) — multi-project deployment; MINOR
v1.4.0 (cross-project gateway-contribute findings) — body extends per Channel #1; MINOR

v2.0.0 (post-tier-4 governing-principle promotion) — P5+ promoted; MAJOR (canonical-spine restructured)
v2.1.0 (additional tier-4 candidates emerge) — MINOR

v3.0.0 (fundamental architecture revision; e.g., 13-gate becomes 14-gate or simplified to fewer) — MAJOR (rare; only on falsification)
```

### Per-piece versioning (within-body)

Each piece may have its own version increment:

```
Piece-level frontmatter: version: <semver>
  - v0.1 — initial agent-authored draft
  - v0.2-0.9 — pre-promotion revisions
  - v1.0 — operator-promoted to tier-2
  - v1.1+ — post-promotion refinements (PATCH)
  - v2.0+ — substantive revision (MINOR within tier; MAJOR if structural)

Body version aggregates from per-piece versions:
  - Body PATCH increments: ≥3 PATCH-level per-piece revisions in 30 days
  - Body MINOR increments: ≥1 new piece OR per-piece MINOR revision
  - Body MAJOR increments: structural change (rare)
```

### Version-bump triggers (per Fire 90 sustained-feedback-loop)

Each Fire 90 refinement-output form maps to version-bump:

| Form | Bump |
|---|---|
| Form 1 (impl-spec revision) | PATCH (refines without restructuring) |
| Form 2 (stress-test extension) | PATCH (extends without restructuring) |
| Form 3 (new piece authoring) | MINOR (extends body) |
| Form 4 (tier-demotion) | PATCH (reverses without restructuring) |
| Form 5 (sister-project contribution) | MINOR (extends body via Channel #1) |

### Cross-version compatibility

For sister-projects + future agents adopting body across versions:

```
v1.x.y — backward-compatible across PATCH/MINOR
  - Sister-projects on v1.0 can upgrade to v1.5 with minor adaptations
  - Adaptation 5-layer manifest stable across v1.x

v1.x → v2.0 — breaking change (MAJOR)
  - Sister-projects must re-evaluate adaptation per v2.0 architecture
  - Migration guide authored as separate piece per major-version

v2.x → v3.0 — breaking (architectural revision)
  - Rare; only on substitution-pattern falsification
  - Migration guide mandatory
```

### Versioning aligned with the second-brain 5-tier maturity

| Body version | Typical tier-state |
|---|---|
| v1.0.x | Tier-1 (all pieces) — initial release; pre-promotion |
| v1.1.x | Mixed Tier-1+Tier-2 — partial promotion |
| v1.2.x | Tier-2 majority — most pieces operator-confirmed |
| v1.3.x | Tier-3 emerging — empirical-evidence accumulating |
| v2.0.x | Tier-4 candidates promoted — governing principles canonical |

### Operator-empirical version-decision points

Operator decides version-bump at:
- M6 milestone: tier-2 promotion of pieces → v1.1.0 increment
- M7 milestone: tier-3 sustained ≥85% → v1.2.0 increment
- Post-M7 ongoing: per-piece refinements → PATCH increments
- Tier-4 governing-principle convergence → v2.0.0 increment (operator-confirmed)

### Anti-patterns at versioning layer

| Anti-pattern | Why bad | Closes-gap-via |
|---|---|---|
| Body has no version → operator + sister-projects can't track | Illegibility | Adopt semver per this pattern |
| MAJOR-bump for routine PATCH | Inflates version churn | Strict semver discipline; PATCH for refinements only |
| MINOR-bump for breaking change | Sister-projects break unexpectedly | Reserve MAJOR for breaking changes |
| Per-piece + body versions diverge unmanageably | Complexity overhead | Body version aggregates from per-piece bumps |
| No migration guide on MAJOR | Sister-projects can't upgrade | MAJOR-version mandates migration guide piece |

## When To Apply

Apply this versioning when:
- Body of work has substantial substrate (≥30 pieces; this body 90+ qualifies)
- Sister-projects expected to consume body
- Long-horizon evolution anticipated (post-M7 sustained discipline)
- Operator-empirical legibility matters (vs implicit-evolution opacity)

## Instances

**Instance 1: current body assignment**:
- This work block: v1.0.0 (90+ pieces; tier-1; pre-M0)
- Frontmatter convention adopted retroactively or forward
- Decision-package v3 (Fire 75) becomes the v1.0.0 release surface

**Instance 2: post-M3 PATCH increment**:
- M3 synthetic stress-tests reveal 3 impl-spec bugs
- Per Fire 90 Form 1: 3 impl-spec revisions
- Body bumps v1.0.0 → v1.0.1 (PATCH)
- Decision-logbook entry; sister-projects unaffected

**Instance 3: post-M6 MINOR increment**:
- 30 of 90 pieces tier-2-promoted
- Body bumps v1.0.x → v1.1.0 (MINOR)
- Sister-projects can now consume canonical pieces (vs DRAFTs)
- Cross-reference annotations updated

**Instance 4: tier-4 governing-principle MAJOR increment**:
- P5 + P6 + P7 promoted to tier-4 over 6+ months
- Body bumps v1.x → v2.0.0 (MAJOR)
- Migration guide authored as new piece
- Sister-projects re-evaluate adaptation manifest

**Instance 5: body-aging detected (Form 4 demotion cascade)**:
- 14-day sustained composite < 70% surfaces multiple impl-specs failing
- Body in transition: v1.x → demotion-cascade → v1.x.y revision
- Per Fire 87 falsifiability: demotion path activated
- Body version may regress to lower-tier-equivalent

## When Not To

- Single-version single-project (no propagation; versioning overhead)
- Cold-start initial body (versioning emerges with maturity)
- Body actively in flux (frequent revisions; versioning churn)
- Operator-explicit "no versioning needed" (operator may prefer informal)

## Empirical Evidence

This pattern is forward-anchored — actual versioning happens post-M3 onward as body refinements accumulate. Without versioning, body evolution is opaque; sister-projects struggle with cross-version compatibility; operator-empirical track-of-changes degrades. With versioning, body evolution is legible at semver granularity.

## Required Gates (per hook-architecture proposal #2 4th component)

```yaml
required_gates:
  empirically_passed:
    - synthetic_semver_assignment: passed 2026-05-08 via mock body-state scenarios
    - synthetic_form_to_bump_mapping: passed 2026-05-08 via mock refinement scenarios
  pending:
    - real_session_post_m3_patch_bump: pending — depends on M3 stress-test execution
    - real_session_post_m6_minor_bump: pending — depends on M6 tier-2 promotion
    - real_session_tier_4_major_bump: pending — depends on tier-4 governing-principle promotion
    - cross_version_sister_project_adaptation: pending — depends on sister-project propagation
    - operator_empirical_versioning_calibration: pending — operator confirms semver discipline
  composite_compliance: versioning-axis stress-test 0% (forward-anchored; M3+ dependency)
```

## Relationships


## Tags

[body-versioning, evolution-tracking, semver-style, meta-discipline, day-arc-2026-05-08, multi-day-pain-point-resolution]
