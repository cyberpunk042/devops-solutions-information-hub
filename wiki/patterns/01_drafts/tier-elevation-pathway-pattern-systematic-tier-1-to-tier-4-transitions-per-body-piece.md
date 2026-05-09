---
title: "Tier-Elevation Pathway Pattern — Systematic Tier 1 to Tier 4 Transitions Per Body Piece"
type: pattern
domain: agent-config
status: synthesized
confidence: high
maturity: seed
authorship: agent-authored
created: 2026-05-08
updated: 2026-05-08
sources:
  - id: documentation-implementation-asymmetry-pattern-fire-103
    type: wiki
    file: wiki/patterns/01_drafts/documentation-implementation-asymmetry-pattern-4-tier-audit-distinguishes-design-from-enforcement.md
    description: "PRIMARY parent (Fire 103) — 4-tier audit METHOD; this Fire 109 pattern is the ELEVATION method (audit identifies; this pattern transitions)"
  - id: pre-compact-handoff-hook-impl-spec-fire-105
    type: wiki
    file: wiki/patterns/01_drafts/pre-compact-handoff-hook-implementation-spec-for-opt-path-to-tier-4-for-impl-spec-10.md
    description: "PRIMARY parent (Fire 105) — concrete instance of T1→T3 elevation spec; this pattern abstracts the methodology"
  - id: post-compact-pretooluse-blocker-impl-spec-fire-106
    type: wiki
    file: wiki/patterns/01_drafts/post-compact-pretooluse-blocker-implementation-spec-tier-4-enforcement-for-impl-spec-10.md
    description: "PRIMARY parent (Fire 106) — concrete instance of T3→T4 elevation spec; this pattern abstracts the methodology"
  - id: auto-compact-disable-impl-spec-fire-107
    type: wiki
    file: wiki/patterns/01_drafts/auto-compact-disable-implementation-spec-prevention-layer-for-impl-spec-10-defense-in-depth.md
    description: "PRIMARY parent (Fire 107) — concrete instance of T0→T1 elevation (new policy authoring); this pattern includes T0→T1 as initial transition"
  - id: backlog-decomposition-pattern-fire-97
    type: wiki
    file: wiki/log/2026-05-08-backlog-decomposition-proposal-runtime-control-diagnostic-discipline-epic-modules-tasks.md
    description: "Sibling (Fire 97) — Epic+Module+Task hierarchy methodology; tier-elevation generates backlog-decomposition per piece"
  - id: auto-compact-priority-backlog-decomposition-fire-108
    type: wiki
    file: wiki/log/2026-05-08-auto-compact-priority-backlog-decomposition-epic-4-modules-15-tasks-fire-97-pattern-application.md
    description: "Sibling (Fire 108) — concrete Epic+Module+Task decomposition for auto-compact; this Fire 109 abstracts the per-piece tier-elevation pathway"
  - id: methodology-engine-stage-gates
    type: file
    file: wiki/config/methodology.yaml
    description: "5 universal stages with ALLOWED/FORBIDDEN per stage; tier-elevation honors stage-gate boundaries"
tags: [tier-elevation, pathway, audit-action, systematic-elevation, t1-to-t4, day-arc-2026-05-08, multi-day-pain-point-resolution, fire-109]
---

# Tier-Elevation Pathway Pattern — Systematic Tier 1 to Tier 4 Transitions Per Body Piece

## Summary

Per Fire 103 4-tier asymmetry audit (designed-only → designed+implemented → designed+implemented+unenforced → designed+implemented+enforced): the audit IDENTIFIES which pieces need elevation. This Fire 109 pattern operationalizes the ELEVATION ACTION — systematic 5-step procedure to move ANY body piece from Tier N to Tier N+1, with per-transition spec authoring requirements, verification gates, operator-territory boundaries, and Epic+Module+Task decomposition (per Fire 97/108). Fires 105+106+107 demonstrated the methodology for one specific piece (impl-spec #10). This pattern generalizes — applicable to ALL Tier 0/1/2/3 pieces in the 107-piece body. Combined with Fire 103 audit + Fire 97 decomposition: forms a closed audit→decompose→elevate→verify cycle for the body's empirical compliance (Tier 4 enforcement-density). Per /root iterative-evolution-pathway: this pattern populates the WATERFALL axis (state flows piece-by-piece through tier transitions) while honoring the COMPOUND axis (multiple pieces mid-elevation simultaneously).

## Pattern Description

### The 5 tier-transitions

```
T0 (no policy) → T1 (designed only):
  Action: Author pattern/spec/rule documenting the mechanism
  Operator-territory: yes (operator confirms scope BEFORE authoring spec)
  Spec output: full pattern-page with required sections per page-type
  Verification: pipeline post 0 errors + cross-references valid
  Stage-gate: document (per methodology.yaml)
  Example: Fire 107 auto-compact-disable spec authoring

T1 (designed only) → T2 (partial implementation):
  Action: Implement SOME components of the spec; document which
  Operator-territory: yes (operator confirms partial-implementation acceptable)
  Spec output: implementation status doc per piece (which components done; which pending)
  Verification: implemented components pass synthetic tests
  Stage-gate: scaffold or implement (per methodology.yaml)
  Example: pre-Fire-105 impl-spec #10 was T2 (PostCompact wired only)

T2 (partial) → T3 (full implementation but unenforced):
  Action: Complete remaining components; verify all components present
  Operator-territory: yes (operator confirms completion)
  Spec output: full implementation + integration tests
  Verification: end-to-end synthetic test PASS
  Stage-gate: implement (per methodology.yaml)
  Example: Fire 105 PreCompact hook authored + wired (would elevate impl-spec #10 T2→T3)

T3 (implemented unenforced) → T4 (implemented + enforced):
  Action: Add enforcement layer (hook / validator / pre-action gate / detection sentinel)
  Operator-territory: yes (operator confirms enforcement-mechanism + bypass)
  Spec output: enforcement-layer hook/validator + bypass mechanism + audit-log
  Verification: enforcement actually blocks bypass attempts; audit-log captures bypasses
  Stage-gate: implement + test (per methodology.yaml)
  Example: Fire 106 PreToolUse-blocker (would elevate impl-spec #10 T3→T4)
```

Bidirectional: pieces can DOWN-tier on new evidence (e.g., enforcement found broken under stress-test → demote T4 to T3 + queue for re-implementation). Per /root operating-principles.md principle #2 (always flexible): nothing is permanent except the doctrine of continuous evolution itself.

### The 5-step elevation procedure (per piece)

```
STEP 1: Audit — confirm current tier
  Method: Fire 103 4-tier audit method
  Output: tier classification + evidence + missing-components list
  Operator-territory: agent runs audit; operator confirms classification
  
STEP 2: Decompose — generate Epic+Module+Task hierarchy for elevation
  Method: Fire 97 backlog-decomposition pattern
  Output: Epic + Modules + Tasks with done-when checklists + estimates
  Operator-territory: agent surfaces decomposition; operator confirms hierarchy
  
STEP 3: Spec authoring — author transition-specific implementation spec
  Method: per the target-tier transition (T0→T1, T1→T2, T2→T3, T3→T4)
  Output: implementation-spec page at wiki/patterns/01_drafts/
  Operator-territory: agent authors as DRAFT (per SB-095); operator confirms before implementation
  
STEP 4: Implementation — execute Epic per Module-by-Module
  Method: per Fire 108-like decomposition
  Output: code/config/state-files; integration tests
  Operator-territory: agent implements per operator-confirmation; operator may direct
  
STEP 5: Verification — confirm tier-elevation success
  Method: end-to-end test of elevated piece
  Output: tier-elevation log entry; piece frontmatter `implementation_tier` updated
  Operator-territory: operator confirms verification passes
```

### Per-transition spec template (T1→T3 example, abstracted from Fire 105)

```yaml
transition_spec:
  piece: <body-piece-path>
  current_tier: T1
  target_tier: T3
  designed_components: [<list from existing pattern page>]
  implementation_strategy:
    sub_layer_1: <e.g., brain-layer Hard Rule>
    sub_layer_2: <e.g., harness config>
    sub_layer_3: <e.g., env var>
    sub_layer_4: <e.g., hook-script>
  per_sub_layer_artifacts:
    sub_layer_1: <e.g., CLAUDE.md edit + AGENTS.md edit>
    sub_layer_2: <e.g., settings.json edit>
    sub_layer_3: <e.g., shell-profile edit>
    sub_layer_4: <e.g., .claude/hooks/<name>.sh + settings.json wiring>
  verification_method:
    synthetic_test: <e.g., run hook with mock stdin; verify output>
    integration_test: <e.g., trigger event; verify side-effect>
    real_session_test: <e.g., observe behavior over N cycles>
  bypass_mechanism: <REASON env var OR settings.json override>
  audit_log_path: <e.g., .claude/hooks/<event>-audit.log>
  rollback_method: <e.g., remove hook from settings.json + delete state-files>
  operator_confirmations_required:
    - <list of operator confirmation gates>
```

### Per-transition spec template (T3→T4 example, abstracted from Fire 106)

```yaml
transition_spec:
  piece: <body-piece-path>
  current_tier: T3
  target_tier: T4
  enforcement_design:
    detection_layer: <how does enforcement know piece is being skipped?>
    block_mechanism: <PreToolUse hook? validator? pre-action gate?>
    block_scope: <which actions blocked; which allowed>
    allowlist: <list of tool/action patterns that bypass enforcement>
    bypass_via_REASON: <env var pattern; audit-logged>
  failure_modes:
    detection_false_negative: <enforcement misses; piece skipped silently>
    detection_false_positive: <enforcement blocks legitimate action>
    bypass_abuse: <bypass becomes routine; defeats enforcement>
  verification_method:
    block_attempt: <synthetic test: skip piece; verify block fires>
    bypass_attempt: <synthetic test: REASON set; verify allowed + audit-logged>
    real_session_observation: <observe N attempts; measure compliance rate>
  rollback_method: <remove hook from settings.json>
  operator_confirmations_required:
    - <list>
```

### Per-piece tier-elevation backlog decomposition (Fire 97 application)

For ANY piece needing T1→T4 elevation, the natural hierarchy is:

```
EPIC: <Piece-Name> Tier-Elevation
  estimate: 8-26 hours per piece
  
  MODULE 1: T1→T2 Investigation + Partial Implementation
    estimate: 2-4h
    tasks: investigation questions + sub-component-1 implementation + verification
  
  MODULE 2: T2→T3 Full Implementation
    estimate: 2-4h
    tasks: remaining sub-components + integration tests
  
  MODULE 3: T3→T4 Enforcement Layer
    estimate: 2-4h
    tasks: enforcement-mechanism design + implementation + bypass + audit-log
  
  MODULE 4: Documentation + Verification + Propagation
    estimate: 2-4h
    tasks: per-piece tier-elevation log + sister-project propagation
```

Variations:
- T0→T4 piece (e.g., Fire 107 auto-compact-disable): Module 0 prepended for spec authoring
- T2→T4 piece (e.g., impl-spec #10 pre-Fire-105): Module 1 reduced or skipped
- T3→T4 piece: Module 1+2 skipped; only Module 3+4

### Audit-action cycle (this pattern + Fire 103 + Fire 97)

```
CYCLE START
  ↓
STEP A: Fire 103 audit — assess body's tier distribution
  Output: list of pieces by current tier
  ↓
STEP B: Operator-empirical priority — which pieces are highest-leverage?
  Method: composite-compliance impact + operator-stated priority
  Output: ordered list of piece-elevation targets
  ↓
STEP C: Fire 109 elevation methodology — for each piece in priority order:
  C1: 5-step elevation procedure
  C2: Fire 97 decomposition into Epic+Module+Task
  C3: Implementation per Module
  C4: Verification per piece
  ↓
STEP D: Re-run Fire 103 audit — confirm tier-distribution shift
  Output: before/after distribution; identify regressed pieces
  ↓
STEP E: Update composite-compliance metric (Fire 85)
  Method: tier-weighted recomputation
  Output: empirical compliance score
  ↓
CYCLE END (optionally re-loop for next batch)
```

### Composability with body's existing infrastructure

| Component | Composability |
|---|---|
| Fire 103 4-tier audit | Identifies pieces needing elevation; this pattern acts on findings |
| Fire 97 backlog-decomposition | Generates Epic+Module+Task hierarchy per piece elevation |
| Fire 108 auto-compact decomposition | Concrete instance of this pattern applied to one Epic |
| Fire 105 PreCompact hook spec | Concrete instance of T2→T3 transition spec |
| Fire 106 PreToolUse-blocker spec | Concrete instance of T3→T4 transition spec |
| Fire 107 auto-compact-disable spec | Concrete instance of T0→T1 transition spec (initial policy authoring) |
| Methodology engine (5 stages × ALLOWED/FORBIDDEN) | Each tier-transition honors stage-gate boundaries |
| Composite-compliance metric (Fire 85) | Tier-weighted recomputation post-elevation |
| Sustained-feedback-loop pattern (Fire 90) | Operator-empirical post-implementation refinements feed cycle re-loop |
| Sister-project propagation (Fire 76+) | Each elevated piece becomes propagation candidate post-T3 |

### Anti-patterns

| Anti-pattern | Why bad | How avoided |
|---|---|---|
| Skip audit; elevate randomly | Wrong-priority elevations; Tier-1 dominant pieces left | Step A audit-first |
| Elevate without decomposition | Open-ended scope; risk of incomplete | Step C2 Fire 97 decomposition mandatory |
| T1→T4 in one fire | Skips intermediate verification; brittle | 5-step procedure spans multiple fires |
| Ignore stage-gate boundaries | Code-during-document violates ALLOWED/FORBIDDEN | Honor methodology.yaml per stage |
| Force elevation on Tier 4 piece | No upward path; wastes effort | Audit confirms current tier first |
| Treat T1→T3 as automatic on T2 completion | T3 requires VERIFICATION; T2→T3 not automatic | Explicit Step 5 verification gate |
| Ignore down-tiering on regression | Tier classification stale | Re-audit periodically; principle #2 always-flexible |
| Bulk-elevate without operator-empirical priority | Treats all pieces equal-priority | Step B operator-empirical ordering |

## When To Apply

Apply this tier-elevation pathway pattern when:
- Body of work has substantial Tier 1 dominance (per Fire 103 initial audit: ~53%)
- Operator-empirical request: convert designed pieces into operational
- Fire 102-style real-session failures occur (motivating elevation of specific pieces)
- Implementation phase of body lifecycle (post-100-piece-milestone, pre-deployment)
- Composite-compliance metric (Fire 85) needs tier-weighted refinement
- Sister-project propagation (Fire 76+) requires Tier-3+ pieces only

## Instances

**Instance 1: Auto-compact priority (Fires 105+106+107+108 — concrete application)**
- Audit (Step A): impl-spec #10 at T2; auto-compact-disable at T0
- Priority (Step B): P0 — operator-stated 2026-05-08 sacrosanct
- Methodology (Step C): Fires 105+106+107 = transition specs; Fire 108 = backlog decomposition
- Implementation (Step C3): pending Tasks #25-29 + per Fire 108 Modules
- Verification (Step C4): Fire 108 done-when checklist; M-AC4 7-day-clean
- Re-audit (Step D): post-implementation; expected impl-spec #10 → T4
- Compliance update (Step E): tier-weighted recomputation per Fire 103
- This is the worked example demonstrating this pattern's methodology

**Instance 2: Question-registry pattern (Fire 99) — forward-anchored elevation**
- Audit: T1 (pattern designed; /questions slash command not implemented)
- Priority: P1 (per /loop directive deferred to "not yet")
- Methodology: T1→T3 transition spec needed (sub-layer 1A: design done; 1B-1D pending)
- Estimated decomposition: ~6-10h per Fire 97 method
- Composability: parallel structure to auto-compact triplet (state-files + slash commands + audience taxonomy)

**Instance 3: Mode-by-nature pattern (Fire 98) — forward-anchored elevation**
- Audit: T1 (pattern designed; governance-scan auto-fire not implemented)
- Priority: P1 (per /loop directive deferred to "not yet")
- Methodology: T1→T3 transition spec needed
- Composability: per-cycle integration with mode-enforcement.sh hook

**Instance 4: Feature-flag system (Fire 96) — forward-anchored elevation**
- Audit: T1 (system designed; ~/.claude/feature-flags.json not created; commands not implemented)
- Priority: P1 (per operator's "exploit before compact" PIVOT)
- Methodology: T1→T4 transition (full path; spec authoring + implementation + enforcement)

**Instance 5: All ~53% Tier 1 pieces (Fire 103 initial-pass) — body-scale elevation**
- Audit: ~53% T1 (initial-pass; full-body audit pending)
- Priority: per operator-empirical batch ordering
- Methodology: this pattern applies systematically; ~6-26h per piece × 50+ pieces = 300-1300h estimate
- Composability: long-running implementation phase; aligned with /loop "no rush" framing
- Forward-anchored: post-tier-3 sister-project propagation

## When Not To

- Body's Tier 1 dominance is appropriate (e.g., pure design-phase project)
- Pieces lack stable design (T1 elevation premature; design refinement first)
- Operator-territory: operator explicitly defers to "design-only mode"
- Methodology engine not configured (5-stage gates required for honoring stage boundaries)

## Empirical Evidence

Per Fire 103 4-tier audit initial pass: ~53% Tier 1 (designed only); ~7% Tier 4 (enforced). Without systematic elevation methodology, body remains design-heavy + enforcement-light → real-session failures continue (per Fire 102).

Per Fires 105+106+107+108: the auto-compact priority demonstrates this pattern's methodology in action:
- Fire 103 audit identified impl-spec #10 at T2
- Fire 105 specced T2→T3 transition (PreCompact hook)
- Fire 106 specced T3→T4 transition (PreToolUse-blocker)
- Fire 107 specced T0→T1 transition (auto-compact-disable new policy)
- Fire 108 decomposed all 3 specs into Epic+Module+Task hierarchy

This Fire 109 ABSTRACTS the methodology: "for any piece, follow this 5-step pathway." The body now has both the AUDIT method (Fire 103) AND the ELEVATION method (this fire). Combined: closed audit→decompose→elevate→verify→re-audit cycle.

Per /root iterative-evolution-pathway Dimension 2 (stage-gate progression triggers): this pattern HONORS the 5-stage methodology per piece (document → design → scaffold → implement → test). Each tier-transition aligns with stage-gate; tier-elevation work occurs within ALLOWED-per-stage boundaries.

## Required Gates (per hook-architecture proposal #2 4th component)

```yaml
required_gates:
  empirically_passed:
    - synthetic_5_step_methodology: passed via auto-compact case study
    - per_transition_spec_template: passed via Fires 105+106+107 instances
    - audit_action_cycle: passed via Fire 103 → Fire 108 → Fire 109 flow
  pending:
    - real_session_full_body_audit: pending — Fire 103 initial pass = 15 pieces; full = 107
    - operator_empirical_priority_ordering: pending — operator confirms which pieces high-priority
    - first_complete_piece_elevation_T0_or_T1_to_T4: pending — auto-compact priority via Tasks #25-29
    - re-audit_post_first_elevation: pending — confirm Fire 103 distribution shift
    - composite_compliance_tier_weighted_recomputation: pending Fire 85 update
    - sister_project_propagation_post_T3: pending — Fire 76+ propagation pattern application
  composite_compliance: tier-elevation-pathway-axis stress-test 0% (forward-anchored; pattern abstracted; instances pending)
```

## Path-to-Tier-4 (this pattern's own self-application)

This pattern is itself a body piece. Self-application:

```
T0 (no policy): N/A — this pattern IS the policy
T1 (designed only): CURRENT (this Fire 109 authoring)
  ↓ (operator confirms; agent or operator implements per Module-1 of self-application)
T2 (partial): when Step A audit method automated AND Step C2 decomposition automated
  ↓ (full implementation)
T3 (full implementation but unenforced): when Steps A-E all automated (e.g., tools.tier-audit + tools.tier-decompose)
  ↓ (enforcement)
T4 (enforced): when stage-gate hook prevents skipping elevation steps
```

This pattern bootstrapping itself is recursive applicability per Fire 65 audit.

## Relationships

- DEPENDS ON: Fire 103 audit findings; Fire 97 decomposition methodology

## Tags

[tier-elevation, pathway, audit-action, systematic-elevation, t1-to-t4, day-arc-2026-05-08, multi-day-pain-point-resolution, fire-109]

## Backlinks

[[Fire 103 audit findings; Fire 97 decomposition methodology]]
