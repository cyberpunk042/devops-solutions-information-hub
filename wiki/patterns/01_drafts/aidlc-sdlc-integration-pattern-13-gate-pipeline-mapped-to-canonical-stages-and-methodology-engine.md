---
title: "AIDLC/SDLC Integration Pattern — 13-Gate Pipeline Mapped to Canonical Stages + the second-brain Methodology Engine"
type: pattern
domain: agent-config
status: synthesized
confidence: high
maturity: seed
authorship: agent-authored
created: 2026-05-08
updated: 2026-05-08
sources:
  - id: comprehensive-13-gate-pattern
    type: wiki
    file: wiki/patterns/01_drafts/comprehensive-agent-action-emission-pipeline-13-gate-composition-architecture.md
    description: "PRIMARY parent — 13-gate central pattern; this integration maps gates to SDLC stages"
  - id: stage-class-implementation-spec
    type: wiki
    file: wiki/patterns/01_drafts/stage-class-gate-implementation-spec-methodology-edit-land-enforcement.md
    description: "Source — impl-spec #7 stage-class; gate #7 IS the SDLC-stage-discipline gate"
  - id: composability-map
    type: wiki
    file: wiki/patterns/01_drafts/13-gate-pipeline-composability-with-second-brain-5-tier-maturity-and-mcp-tool-layer.md
    description: "Sibling — composability map; SDLC integration is composability with the second-brain methodology engine"
  - id: implementation-roadmap-pattern
    type: wiki
    file: wiki/patterns/01_drafts/implementation-roadmap-pattern-sequenced-milestones-from-confirmation-to-tier-3.md
    description: "Source — implementation-roadmap M1-M7; aligns with SDLC implement+test+deploy stages"
  - id: substitution-pattern-meta-frame
    type: wiki
    file: wiki/lessons/01_drafts/documentation-as-substitute-for-discipline-the-meta-pattern.md
    description: "Meta-frame — SDLC-integration without paired-stage-class enforcement IS substitution at SDLC layer"
tags: [aidlc-sdlc-integration, methodology-engine, 13-gate-mapping, day-arc-2026-05-08, multi-day-pain-point-resolution]
---

# AIDLC/SDLC Integration Pattern — 13-Gate Pipeline Mapped to Canonical Stages + the second-brain Methodology Engine

## Summary

Per the second-brain second-brain `wiki/config/methodology.yaml`: 9 named methodology models with 5 universal stages (document → design → scaffold → implement → test). The 13-gate pipeline composes with this methodology engine but no prior piece explicitly maps each gate to canonical AIDLC/SDLC stage discipline. This pattern bridges 13-gate pipeline + the second-brain methodology engine + industry-standard AIDLC/SDLC + operator's pivotal directive on respecting workflow ("sdlc and methodology and workflow respect is utmost important"). Per substitution-pattern Insight 5b: gate documentation alone partial — must map to SDLC convention for cross-project + cross-team adoption. This piece closes the AIDLC/SDLC-integration gap.

## Pattern Description

### The 5 universal stages (per the second-brain methodology engine)

```
DOCUMENT (0-25% readiness):
  ALLOWED: wiki page, raw notes
  FORBIDDEN: code-file, test-file
  Gate: page exists with Summary + gaps identified

DESIGN (25-50%):
  ALLOWED: design-document, ADR, tech-spec, type sketches IN DOCS
  FORBIDDEN: code-file, test-file
  Gate: spec reviewed; trade-offs documented; no code yet

SCAFFOLD (50-80%):
  ALLOWED: type-defs, schema, test-stubs, config-files
  FORBIDDEN: implementation, real test assertions
  Gate: types compile; no business logic

IMPLEMENT (80-95%):
  ALLOWED: implementation, integration-wiring, config
  FORBIDDEN: new test files
  Gate: code compiles; lint passes; ≥1 existing file imports new code

TEST (95-100%):
  ALLOWED: test-implementation, test-results
  FORBIDDEN: new features, scope changes
  Gate: 0 test failures; health check clean
```

### 13-gate pipeline mapped to SDLC stages

For each of 12 axes (axis #12 self-referential excluded), per-stage applicability:

| Axis | document | design | scaffold | implement | test |
|---|---|---|---|---|---|
| #1 input-discipline | ✓ check pre-author | ✓ check pre-design | ✓ check pre-scaffold | ✓ check pre-impl | ✓ check pre-test |
| #2 decision-territory | ✓ /root edits limited | ✓ ADR is operator-territory | ✓ schema is design-territory | ✓ code is agent-territory | ✓ test code agent-territory |
| #3 regression-test | TEST-EXEMPT (.md) | TEST-EXEMPT | partial (test-stubs) | ✓ MANDATORY | ✓ MANDATORY |
| #4 severity | T4 typically | T4 (proposal-tier ADRs) | T3 (schema-tier) | T2-T3 (implementation-tier) | T2-T3 (test-tier) |
| #5 correction-shape | applies (operator may correct doc-direction) | applies (operator may correct design) | applies | applies | applies |
| #6 drift-detection | ✓ active-task scope | ✓ stays-in-design-stage | ✓ scope-anchor | ✓ scope-anchor | ✓ scope-anchor |
| #7 stage-class | (this gate IS the stage-discipline gate) | (this gate IS) | (this gate IS) | (this gate IS) | (this gate IS) |
| #8 authorship | applies (auto-tag agent-authored) | applies (auto-tag) | applies | applies | applies |
| #9 semantic-conflation | applies (operator-prompt detection) | applies | applies | applies | applies |
| #10 post-compact | applies (lifecycle-event; cross-stage) | applies | applies | applies | applies |
| #11 pattern-recurrence | applies (cycle aggregation cross-stage) | applies | applies | applies | applies |

**Pattern**: All 12 axes apply across all 5 stages BUT gate-#7 (stage-class) is the meta-gate validating which axis-actions are stage-allowed. Gate #3 (regression-test) is most relevant at implement+test stages; less so document/design.

### Composability with the second-brain methodology engine

```
Methodology engine (per the second-brain wiki/config/methodology.yaml):
  - 9 named models (feature-development / bug-fix / research / documentation / refactor / hotfix / integration / knowledge-evolution / project-lifecycle SFIF)
  - 5 universal stages
  - Per-stage ALLOWED/FORBIDDEN

13-gate pipeline composes with methodology engine via:
  - Gate #7 stage-class IS the runtime enforcement of methodology engine's per-stage discipline
  - Gate #6 drift-detection IS the active-task-anchor referenced by methodology engine's task scope
  - Gate #1 input-discipline CHECK 3 reads the second-brain methodology config before authoring (knowledge-reuse)
  - Gate #3 regression-test maps to methodology engine's "test stage" gate command

Per impl-spec #7 SOURCE 3 query: gate #7 reads methodology.yaml directly for per-stage rules.
```

### AIDLC/SDLC industry-standard mapping

The 5 universal stages map to industry-standard AIDLC/SDLC vocabulary:

| the second-brain 5-stage | AIDLC/SDLC equivalent | Standard description |
|---|---|---|
| document | Requirements / Discovery | Capture what + why; scoping |
| design | Architecture / Design | How (architectural); trade-offs |
| scaffold | Detailed-design / Module-skeleton | Type-defs + schemas + test-stubs |
| implement | Implementation / Coding | Real implementation; unit tests follow |
| test | Verification / Validation / QA | Test execution; release-readiness |

(Industry SDLC includes additional Deploy + Operate stages NOT in the second-brain 5-stage; those are post-test discipline at the second-brain's project-lifecycle SFIF model.)

### 13-gate pipeline within full AIDLC/SDLC + Deploy/Operate

```
Full SDLC = Requirements + Architecture + Detailed-design + Implement + Test + Deploy + Operate

the second-brain 5-stage covers: Requirements (document) → Architecture (design) → Detailed-design (scaffold) → Implement (implement) → Test (test)

Post-test stages (Deploy + Operate) handled via the second-brain project-lifecycle SFIF model:
  - SFIF Scaffold = Deploy-prep
  - SFIF Foundation = Initial-deploy
  - SFIF Infrastructure = Production-operate
  - SFIF Features = Feature-rollout

13-gate pipeline applies across ALL stages including Deploy + Operate:
  - Gate #4 severity matters HEAVILY at Deploy (T1 production mutations)
  - Gate #2 decision-territory matters at Deploy (production change-management)
  - Gate #11 pattern-recurrence matters at Operate (production-incident pattern detection)
```

### Per-stage gate-priority mapping

For implementation phase (M1-M7 per implementation-roadmap), different stages emphasize different gates:

| Stage | Highest-priority gates |
|---|---|
| Document | #1 input-discipline (knowledge-reuse) + #2 decision-territory (operator-territory respect) |
| Design | #2 decision-territory (architectural choices = operator-territory) + #5 correction-shape (operator may correct design direction) |
| Scaffold | #6 drift-detection (active-task scope) + #7 stage-class (scaffold-tier ALLOWED matrix) |
| Implement | #3 regression-test (Hard Rule 14 verified-edit) + #7 stage-class + #4 severity (production-class actions) |
| Test | #3 regression-test (test-execution discipline) + #11 pattern-recurrence (test-failure pattern aggregation) |

### Operator's pivotal directive linkage

Per operator's repeated /loop directive: *"sdlc and methodology and workflow respect is utmost important"*.

The 13-gate pipeline operationalizes this respect via:
- Gate #7 stage-class: methodology engine respect at edit-land time
- Standardize proposal #3: methodology rule extension codifies stage-class enforcement
- Implementation-roadmap M1-M7: roadmap traces SDLC discipline through phase
- Composability map: methodology engine IS layer of composability

Result: operator's "SDLC respect" directive structurally implemented across body.

## When To Apply

Apply this AIDLC/SDLC integration when:
- Project has methodology engine + 5-stage discipline (or analogous)
- 13-gate pipeline implementation underway (M1-M7)
- Cross-project propagation considers SDLC-vocabulary alignment
- Operator-empirical "sdlc + workflow respect" directive in force
- Sister-projects use industry-standard SDLC vocabulary

## Instances

**Instance 1: methodology-yaml gate consultation at edit-land**:
- Gate #7 fires on Edit at /root/wiki/lessons/01_drafts/foo.md
- Looks up active-task current_stage = "design"
- Reads methodology.yaml: design-stage ALLOWED includes wiki/, design/, ADR/
- Match: target /root/wiki/lessons/01_drafts/foo.md = wiki/* matches ALLOWED
- Gate allows; SDLC discipline respected.

**Instance 2: cross-stage operator request**:
- Operator: "this is a hotfix; bypass scaffold + go straight to implement"
- Methodology engine model selection: hotfix model (per the second-brain wiki/config/methodology.yaml)
- Hotfix model stages: implement → test only (skip document/design/scaffold)
- Gate #7 reads methodology engine + per-model stage discipline
- Allows direct implement-stage edits

**Instance 3: SDLC-vocabulary alignment for sister-project**:
- OpenArms agent reads canonical the second-brain 13-gate pipeline + SDLC mapping
- Maps the second-brain 5-stage to OpenArms internal "phase" vocabulary
- Adapts gate #7 stage-class per OpenArms's 5-stage equivalent
- 13-gate pipeline propagates with SDLC-aware adaptation

**Instance 4: production deploy-gate composition**:
- Gate #4 severity classifies `terraform apply` as T1
- Per-stage mapping: T1 actions at Deploy stage require operator-grant
- Composability with operator-territory gate #2: operator-grant required
- Banner-stack: severity T1 BLOCK + decision-territory operator-territory BLOCK
- Operator confirms; gate allows with audit log.

## When Not To

- Project lacks methodology engine (no 5-stage discipline established)
- Single-project work without SDLC-vocabulary cross-team adoption
- Cold-start scaffolding before any methodology config exists
- Operator-explicit "skip SDLC discipline" (rare; usually emergency hotfix)
- Sister-projects with fundamentally-different lifecycle model

## Empirical Evidence

Per operator's repeated /loop directive: SDLC + methodology + workflow respect is foundational. The 13-gate pipeline's gate #7 (stage-class) operationalizes this respect at runtime. Without explicit SDLC mapping (this piece), the connection between operator's directive + 13-gate pipeline is implicit. With this piece: operator-empirical clarity + sister-project propagation + cross-team vocabulary alignment all addressed.

## Required Gates (per hook-architecture proposal #2 4th component)

```yaml
required_gates:
  empirically_passed:
    - synthetic_5_stage_to_13_gate_mapping: passed 2026-05-08 via mock per-stage scenarios
  pending:
    - real_session_methodology_engine_consultation: pending — gate #7 reads methodology.yaml in real session
    - real_session_per_stage_gate_priority_validation: pending — empirical priority observed across 5 stages
    - real_session_sdlc_vocabulary_alignment: pending — cross-team adoption verified
    - real_session_post_test_deploy_gate_composition: pending — gate #4 + #2 stack on Deploy actions
    - operator_empirical_sdlc_respect_calibration: pending — operator confirms 13-gate pipeline operationalizes "SDLC respect" directive
  composite_compliance: aidlc-sdlc-integration-axis stress-test 0% (depends on M3+ implementation)
```

## Relationships


## Tags

[aidlc-sdlc-integration, methodology-engine, 13-gate-mapping, day-arc-2026-05-08, multi-day-pain-point-resolution]
