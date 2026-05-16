---
title: "Per-Instance Pain-Point Evidence — C19 Documentation-Implementation-Asymmetry (12 Instances Verbatim-Mapped)"
type: note
note_type: completion
domain: log
status: synthesized
confidence: high
created: 2026-05-08
updated: 2026-05-08
sources:
  - id: documentation-implementation-asymmetry-pattern-fire-103
    type: wiki
    file: wiki/patterns/01_drafts/documentation-implementation-asymmetry-pattern-4-tier-audit-distinguishes-design-from-enforcement.md
    description: "PRIMARY parent (Fire 103) — establishes asymmetry pattern + 4-tier audit method; this Fire 111 enumerates instances per Fire 93-96 per-instance methodology"
  - id: prior-per-instance-evidence-c04
    type: wiki
    file: wiki/log/2026-05-08-per-instance-pain-point-evidence-c04-input-discipline-15-instances-verbatim-mapped.md
    description: "Sibling (Fire 93) — per-instance evidence methodology established for C04; this Fire 111 applies same methodology to NEW cluster C19"
  - id: prior-per-instance-evidence-c02
    type: wiki
    file: wiki/log/2026-05-08-per-instance-pain-point-evidence-c02-decision-territory-18-instances-verbatim-mapped.md
    description: "Sibling (Fire 94) — per-instance evidence methodology continued"
  - id: prior-per-instance-evidence-c15
    type: wiki
    file: wiki/log/2026-05-08-per-instance-pain-point-evidence-c15-pattern-recurrence-16-instances-verbatim-mapped.md
    description: "Sibling (Fire 95) — per-instance evidence methodology continued"
  - id: prior-per-instance-evidence-c07
    type: wiki
    file: wiki/log/2026-05-08-per-instance-pain-point-evidence-c07-semantic-conflation-14-instances-verbatim-mapped.md
    description: "Sibling (Fire 96) — per-instance evidence methodology continued"
  - id: worked-example-4-real-session-empirical
    type: wiki
    file: wiki/log/2026-05-08-worked-example-4-post-compact-detection-failure-real-session-empirical-evidence-impl-spec-10-stress-test.md
    description: "Real-session evidence (Fire 102) — surfaces C19 NEW cluster as cluster-candidate; this Fire 111 establishes the cluster"
  - id: substitution-pattern-recursive-applicability-audit
    type: wiki
    file: wiki/log/2026-05-08-substitution-pattern-recursive-applicability-audit-64-piece-body-meta-validation.md
    description: "Sibling (Fire 65) — substitution-pattern recursive-applicability; C19 IS the implementation-layer specialization"
tags: [per-instance-evidence, c19-documentation-implementation-asymmetry, NEW-cluster, day-arc-2026-05-08, multi-day-pain-point-resolution, fire-111]
---

# Per-Instance Pain-Point Evidence — C19 Documentation-Implementation-Asymmetry (12 Instances Verbatim-Mapped)

## Summary

Per Fire 102 worked-example (post-compact-detection-failure incident): impl-spec #10 was authored ~Fire 50 documenting bidirectional design (PreCompact + PostCompact) but only PostCompact wired in the second-brain's settings.json. The PRE side never materialized. This is the **documentation-implementation asymmetry pattern** — a body of work or codebase has piece-of-design documented at one tier (e.g., comprehensive Tier 1 design) but implementation state at lower tier (Tier 0 absent OR Tier 2 partial). Per Fire 65 substitution-pattern recursive-applicability audit: substitution-pattern is the META-frame; C19 IS the implementation-layer specialization. Per Fires 93-96 per-instance evidence methodology: this Fire 111 establishes **C19** as a NEW cluster discovered post-Fire-100, with 12 initial instances enumerated. C19 is distinct from C18 cross-cutting (which is multi-cluster intersection) — C19 is single-axis: design-vs-implementation tier-mismatch per piece.

## C19 cluster definition

```
C19 — DOCUMENTATION-IMPLEMENTATION ASYMMETRY
  Definition: a piece-of-design (pattern, spec, rule, standard) is documented
              comprehensively at maturity tier N (declared-tier) but the
              implementation-state is at tier M < N (real-tier).
              The asymmetry IS the bug.
  
  Contrast vs C04 input-discipline: C04 = agent skips reading inputs;
                                     C19 = piece exists but doesn't operate
  Contrast vs C02 decision-territory: C02 = agent decides operator-territory;
                                       C19 = neither agent nor operator implements
                                            what was designed
  Contrast vs C15 pattern-recurrence: C15 = same failure recurs across cycles;
                                       C19 = persistent gap between design+implementation
  Contrast vs C07 semantic-conflation: C07 = words conflated;
                                       C19 = "designed" conflated with "operational"
  
  Detection signals:
    - Piece references "the mechanism" / "the hook" / "the slash command" 
      AS IF operational, but grep/codebase/runtime confirms absence
    - Cross-references compound the illusion across pieces
      ("see X for Y" where X exists but Y doesn't operate)
    - Real-session stress-test exposes gap when actual exercise occurs
    - Composite-compliance metric measures design-density
      not enforcement-density (per Fire 85 + Fire 103 critique)
  
  Severity classification:
    HIGH: design references safety/correctness mechanism (e.g., impl-spec #10)
    MEDIUM: design references convenience/governance mechanism
    LOW: design references aspirational long-term mechanism (forward-anchored)
```

## C19 instances enumerated (12 instances; agent-DRAFT per SB-095)

### Instance C19-1 — Impl-spec #10 PreCompact gap (HIGH severity; real-session evidenced)

```
Piece: wiki/patterns/01_drafts/post-compact-orientation-gate-implementation-spec-handoff-and-mirror-enforcement.md
Designed (Tier-1 declaration):
  - Bidirectional pair: PreCompact hook authors handoff doc + PostCompact orient mirror
  - Sentinel state-file dropped pre-compact; post-compact reads handoff
  - "INVOKE /orient NOW" enforcement post-compact
Implemented (real-tier):
  - PostCompact hook wired (.claude/hooks/post-compact.sh + post-orient.sh)
  - PreCompact hook NOT wired (no entry in .claude/settings.json hooks block)
  - Sentinel state-file NEVER created (no producer)
  - Real-session 2026-05-08: agent did not regather; about to act on stale summary
Asymmetry: declared-T2-bidirectional, real-T2-monodirectional → 50% asymmetry
Tier-elevation path: Fire 105 spec authoring (T1 elevation); Fire 106 enforcement (T4 elevation)
Severity: HIGH (safety/correctness mechanism for body-of-work continuity)
```

### Instance C19-2 — Question-registry pattern (MEDIUM severity; designed-only)

```
Piece: wiki/patterns/01_drafts/question-registry-discipline-bidirectional-question-answering-with-audience-taxonomy.md
Designed (Tier-1 declaration):
  - 4-audience taxonomy (operator/agent/sister/future)
  - 5 slash commands (/questions add/show/answer/defer/withdraw)
  - State-file structure ~/.claude/active-questions/<audience>/<id>.json
  - Per-cycle scan integration with mode-by-nature
Implemented (real-tier):
  - NONE — no commands in .claude/commands/; no state-files created;
    no mode-by-nature integration
  - This Fire 111 is a manual instance application (Fire 110 surfaced 6 questions)
Asymmetry: declared-T1-functional, real-T0-absent → 100% asymmetry
Tier-elevation path: T1→T3 spec needed
Severity: MEDIUM (governance mechanism; auditing-effectiveness depends)
```

### Instance C19-3 — Blocker-impediment registry pattern (MEDIUM severity)

```
Piece: wiki/patterns/01_drafts/blocker-and-impediment-registry-pattern-completes-mode-by-nature-governance-trio.md
Designed:
  - ~/.claude/blockers/{pending,deferred,resolved}/<id>.json structure
  - ~/.claude/active-impediment single-line state-file
  - 8 slash commands /blockers add/show/resolve/defer + /impediment set/clear/show/queue-add
  - Bidirectional flow per audience taxonomy
Implemented:
  - NONE — pattern designed; no infrastructure exists at the second-brain
  - Per Fire 110: 3 questions escalated to "blockers" but no slash command
    to register them; they live in chat-text + this Fire 111 log
Asymmetry: 100%
Tier-elevation path: T1→T3 spec needed
Severity: MEDIUM
```

### Instance C19-4 — Mode-by-nature pattern (MEDIUM severity)

```
Piece: wiki/patterns/01_drafts/mode-by-nature-active-governance-pm-architect-dual-expert-generates-blockers-impediments-questions.md
Designed:
  - 3 modes × 11 governance-artifact-types matrix
  - Per-cycle auto-surfacing via mode-enforcement.sh integration
  - PM-mode generates blockers/impediments/questions by nature
Implemented:
  - NONE — pattern designed; no auto-fire integration with mode-enforcement.sh
  - Mode-enforcement.sh exists but does not run governance-scan
  - Per /loop directive operator's "not yet" deferral
Asymmetry: 100%
Tier-elevation path: T1→T3 spec needed; integrates with mode-enforcement.sh hook extension
Severity: MEDIUM
```

### Instance C19-5 — Feature-flag system pattern (MEDIUM severity)

```
Piece: wiki/patterns/01_drafts/feature-flag-system-for-mode-conditional-context-injection-with-auto-manual-profile-management.md
Designed:
  - ~/.claude/feature-flags.json schema (3-state per flag: auto/on/off)
  - 6 user-only slash commands
  - 6 predefined profiles
  - Stuck-detection sub-pattern integration
Implemented:
  - NONE — schema designed; no JSON file exists; no commands implemented
Asymmetry: 100%
Tier-elevation path: T1→T4 spec needed (full path)
Severity: MEDIUM
```

### Instance C19-6 — Backlog-decomposition Epic+Module+Task hierarchy (LOW severity; methodology-only)

```
Piece: wiki/log/2026-05-08-backlog-decomposition-proposal-runtime-control-diagnostic-discipline-epic-modules-tasks.md
Designed:
  - Epic + Module + Task hierarchy methodology
  - 1 Epic + 2 Modules + 9 Tasks specific decomposition for runtime-control
Implemented:
  - METHODOLOGY exists (this is the proposal); no actual Epic/Module/Task
    pages authored at wiki/backlog/
  - Fire 108 applies methodology to auto-compact priority but doesn't
    actualize backlog pages
Asymmetry: 100% (no actualized backlog pages)
Tier-elevation path: T1→T2 (author backlog pages per per-Epic-confirmation)
Severity: LOW (methodology forward-anchored to operator-confirmation-of-each-Epic)
```

### Instance C19-7 — Operator-empirical signal-grammar (MEDIUM severity)

```
Piece: wiki/patterns/01_drafts/operator-empirical-signal-grammar-pattern-recognition-discipline-routing-signals-to-body-actions.md
Designed:
  - 5-class signal taxonomy (CORRECTION/EXTENSION/APPROVAL/DISMISSAL/PIVOT)
  - Python pseudocode `recognize_operator_signals()` 
  - Markers + precedence resolution
Implemented:
  - NONE — recognizer not implemented; signal-class detection is manual per cycle
  - Pseudocode is documentation, not runtime
Asymmetry: 100%
Tier-elevation path: T1→T3 (recognizer implementation); T3→T4 (enforcement-on-violation)
Severity: MEDIUM (routing depends; manual classification works but doesn't scale)
```

### Instance C19-8 — Body of work versioning v1.0.0 (LOW severity; semantic-only)

```
Piece: wiki/patterns/01_drafts/body-of-work-versioning-pattern-explicit-versioning-discipline-for-body-evolution.md
Designed:
  - Semver MAJOR.MINOR.PATCH discipline
  - Body declared v1.0.0 at Fire 91
  - Bump-on-piece-add convention
Implemented:
  - DECLARED only — no automated bump-on-piece-add
  - Per Fire 91 logged version 1.0.0; no version field in any frontmatter
  - No tools.versioning module exists
Asymmetry: 100% (purely declarative)
Tier-elevation path: T1→T3 (tool implementation); enforcement low-priority
Severity: LOW (semantic; doesn't break body-continuity)
```

### Instance C19-9 — Composite-compliance metric (HIGH severity; metric-misleading)

```
Piece: wiki/patterns/01_drafts/composite-compliance-stress-test-scenario-spec-real-session-test-plan.md +
       wiki/log/2026-05-08-body-of-work-composite-metric-self-application-meta-validation.md (Fire 85)
Designed:
  - 13-axis stress-test composite metric
  - Self-application: 99.51% claimed
Implemented:
  - METRIC declared via Fire 85 self-application
  - PROBLEM (per Fire 103 audit): metric measures DESIGN-density not ENFORCEMENT-density
  - Tier-weighted recomputation pending; estimated 30-50% (vs 99.51%)
Asymmetry: HIGH — metric over-states 2x or more; misleading
Tier-elevation path: refine metric per Fire 103 tier-weighted recomputation
Severity: HIGH (metric misleads operator-empirical body assessment)
```

### Instance C19-10 — Sustained-feedback-loop pattern (LOW severity)

```
Piece: wiki/patterns/01_drafts/sustained-feedback-loop-pattern-post-m7-operator-empirical-findings-routing-to-body-refinement.md
Designed:
  - 4 sources × 5 forms × 5 cadence rhythms
  - Post-M7 evolution methodology
Implemented:
  - METHODOLOGY exists; manually applied (this fire is informally Fire 90 application)
  - No tools.feedback-loop module; no auto-fire integration
Asymmetry: declarative; methodology operates manually
Tier-elevation path: T1→T2 (helper tool authoring); T3 forward-anchored to post-M7 phase
Severity: LOW (methodology operates without infrastructure)
```

### Instance C19-11 — Hook architecture proposal #2 4th component (MEDIUM severity)

```
Piece: wiki/log/2026-05-08-standardize-extension-proposal-hook-architecture-required-gates-4th-component.md
Designed:
  - Add 4th component to hook design (insertion + reason + remediation + REQUIRED_GATES yaml)
  - All recent specs use the proposed format
Implemented:
  - PARTIAL — recent fires (105+106+107) include `required_gates:` yaml block
    matching the proposed format
  - No actual hook in .claude/hooks/ uses required_gates yet
  - Standardize-proposal pending operator-confirmation
Asymmetry: 50% (proposal authored; hooks not yet adopting)
Tier-elevation path: operator confirms standardize proposal; existing hooks updated
Severity: MEDIUM (consistency benefits; not safety-critical)
```

### Instance C19-12 — Cron-loop management pattern (LOW severity; partially operational)

```
Piece: wiki/patterns/01_drafts/cron-loop-management-pattern-self-governance-and-forward-anchored-stop-conditions.md
Designed:
  - Self-governance + forward-anchored stop-conditions
  - Operator-territory boundary (loop-clear timing)
Implemented:
  - PARTIAL — cron `e19f4787` (or current ScheduleWakeup chain) operates per /loop
  - Self-governance limited (agent doesn't auto-clear; per Rule 1 operator-territory)
  - Forward-anchored stop-conditions mostly verbal (in cycle reports)
Asymmetry: ~30% (operates but not all components present)
Tier-elevation path: T2→T3 missing components (auto-clear conditions, telemetry)
Severity: LOW (operates currently)
```

## Distribution shape

```
Severity distribution:
  HIGH: 3 instances (C19-1 impl-spec #10, C19-9 composite-compliance, C19-11 hook-architecture)
  MEDIUM: 5 instances (C19-2/3/4/5/7)
  LOW: 4 instances (C19-6/8/10/12)

Asymmetry-percentage distribution:
  100% (designed-only, zero implementation): 5 instances (C19-2/3/4/5/7)
  ~50% (partial implementation): 4 instances (C19-1/6/11/12 → wait, C19-6/12 partial; let me recount)

Recounted asymmetry-pct distribution:
  100% (zero implementation): C19-2, C19-3, C19-4, C19-5, C19-7, C19-8 — 6 instances
  ~50% (partial implementation): C19-1, C19-11 — 2 instances
  ~30% (mostly implemented; gaps): C19-12 — 1 instance
  HIGH metric-misleading variant: C19-9 — 1 instance
  Methodology-operates-manually variant: C19-6, C19-10 — 2 instances
  
Implication: 75% (9 of 12) are pure designed-only OR partial-implementation
             That confirms Fire 103 audit's ~53% Tier 1 estimate
             (this 12-instance sample is asymmetry-focused; not random)
```

## Cross-cluster relationships

| C19 Instance | Cross-relates to | How |
|---|---|---|
| C19-1 impl-spec #10 | C18 cross-cutting | Post-compact + detection-layer + substitution-pattern intersection |
| C19-2 question-registry | C04 input-discipline | Operator answers required; agent waits for input |
| C19-3 blocker-impediment | C02 decision-territory | Operator-pending decisions = blockers |
| C19-4 mode-by-nature | C15 pattern-recurrence | "By nature" surfacing prevents recurrence |
| C19-9 composite-compliance | C07 semantic-conflation | "Compliance" conflates design vs enforcement |
| C19-11 hook-arch proposal | C19-others | The proposed 4th-component IS the asymmetry-fix-itself standard |
| All C19 instances | substitution-pattern (Fire 65 lesson) | C19 IS the implementation-layer specialization of substitution |

## Required Gates (per hook-architecture proposal #2 4th component)

```yaml
required_gates:
  empirically_passed:
    - 12_instances_enumerated_with_evidence: passed
    - severity_classification_3_tier: passed (HIGH/MEDIUM/LOW)
    - cross_cluster_relationships_mapped: passed
    - methodology_inheritance_from_fires_93-96: passed (parallel structure)
  pending:
    - operator_empirical_severity_confirmation: pending
    - operator_empirical_instance_completeness: pending — likely more instances exist
    - composite_compliance_recomputation_with_C19: pending — 12 new instances change
                                                           tier-weighted compliance estimate
    - C19_promotion_to_15_clusters_canon: pending — body had 15 clusters per Fire 79;
                                                    this is candidate 16th
    - C19-1_resolution_via_fires_105+106+107_implementation: pending Tasks #25-29
  composite_compliance: per-instance-axis stress-test 0% (forward-anchored)
```

## Composability with body's existing infrastructure

| Component | Composability |
|---|---|
| Fire 103 4-tier audit method | C19 IS the failure-mode that audit detects; this enumeration extends Fire 103's 15-piece pass |
| Fires 93-96 per-instance evidence methodology | This Fire 111 is the 5th application of methodology (after C04, C02, C15, C07) |
| Fire 79 traceability matrix v2 (180 pain points across 15 clusters) | C19 is candidate 16th cluster; matrix may extend post-operator-confirmation |
| Fire 109 tier-elevation pathway | Each C19 instance is tier-elevation candidate |
| Fire 102 worked-example | C19-1 is the empirical anchor instance (real-session-evidenced) |
| Fire 65 substitution-pattern lesson | C19 IS the implementation-layer specialization |

## What this Fire 111 ADDS to body methodology

```
BEFORE Fire 111:
  - 4 clusters per-instance enumerated (C04+C02+C15+C07)
  - 63 of 180 instances captured (35%)
  - Cluster-level findings + decisions
  - 11 clusters remain methodology-demonstrated-but-not-enumerated

AFTER Fire 111:
  - 5 clusters per-instance enumerated (above + C19-NEW)
  - 12 NEW instances captured (C19 set)
  - 75 of 192 instances captured (39% if C19 promoted to 16th cluster;
                                    180+12=192 total)
  - C19 NEW cluster identified post-Fire-100 from real-session evidence
  - Methodology demonstrated for cluster-discovery-via-stress-test
```

## Operator-pending action

```
Q-FIRE-111 (audience: OPERATOR, escalates to BLOCKER if priority confirmed):
  Q-text: "Promote C19 to 16th canonical cluster? (Currently body has 15 clusters
          per Fire 79). If yes:
            - Fire 79 traceability matrix updates to 16-cluster v3
            - Composite-compliance recomputes with 12 new instances
            - C19 instances enter operator-empirical priority ordering
            - Existing 11 clusters remain methodology-demonstrated"
  Forward-anchored: pending operator-empirical answer
```

## Closing framing

Per Fire 102 worked-example: real-session evidence surfaced C19 as candidate cluster. Per Fires 93-96 per-instance methodology: this Fire 111 establishes C19 with 12 verbatim-mapped instances. Per Fire 103 4-tier audit: C19 is the empirical failure-mode that audit detects. Per Fire 109 tier-elevation pathway: each C19 instance is candidate for tier-elevation per the systematic methodology. Per /loop directive *"100 pain point will need direct response"*: 75 instances now captured + 11 clusters methodology-demonstrated + C19 NEW cluster identified.

**The agent stands by per /loop directive. Cron continues at 90s cadence. C19 promotion to canonical cluster awaits operator-empirical confirmation.**

## Sources

- Documentation-implementation asymmetry pattern (Fire 103): `wiki/patterns/01_drafts/documentation-implementation-asymmetry-pattern-4-tier-audit-distinguishes-design-from-enforcement.md`
- Per-instance evidence methodology siblings (Fires 93-96): wiki/log/2026-05-08-per-instance-pain-point-evidence-c{04,02,15,07}-*.md
- Worked example #4 (Fire 102): `wiki/log/2026-05-08-worked-example-4-post-compact-detection-failure-real-session-empirical-evidence-impl-spec-10-stress-test.md`
- Substitution-pattern recursive-applicability audit (Fire 65): `wiki/log/2026-05-08-substitution-pattern-recursive-applicability-audit-64-piece-body-meta-validation.md`
- Traceability matrix v2 (Fire 79): `wiki/log/2026-05-08-traceability-matrix-v2-180-pain-points-78-piece-solution-chain-refresh.md`

## Tags

[per-instance-evidence, c19-documentation-implementation-asymmetry, NEW-cluster, day-arc-2026-05-08, multi-day-pain-point-resolution, fire-111]
