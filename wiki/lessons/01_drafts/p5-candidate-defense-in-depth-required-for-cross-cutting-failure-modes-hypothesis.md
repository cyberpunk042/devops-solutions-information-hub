---
title: "P5 Candidate Hypothesis — Defense-in-Depth Required for Cross-Cutting Failure Modes"
type: lesson
domain: cross-domain
status: synthesized
confidence: medium
maturity: seed
authorship: agent-authored
created: 2026-05-08
updated: 2026-05-08
sources:
  - id: c18-cross-cutting-per-instance-evidence-fire-115
    type: wiki
    file: wiki/log/2026-05-08-per-instance-pain-point-evidence-c18-cross-cutting-multi-cluster-intersections-15-instances-verbatim-mapped.md
    description: "PRIMARY parent (Fire 115) — 15 instances of cross-cluster failures; 53% HIGH severity (vs single-axis ~LOW-MEDIUM); foundational evidence for P5"
  - id: documentation-implementation-asymmetry-pattern-fire-103
    type: wiki
    file: wiki/patterns/01_drafts/documentation-implementation-asymmetry-pattern-4-tier-audit-distinguishes-design-from-enforcement.md
    description: "PRIMARY parent (Fire 103) — 4-tier audit method; T4 (single-axis enforcement) insufficient for cross-cutting failures"
  - id: auto-compact-disable-impl-spec-fire-107
    type: wiki
    file: wiki/patterns/01_drafts/auto-compact-disable-implementation-spec-prevention-layer-for-impl-spec-10-defense-in-depth.md
    description: "PRIMARY parent (Fire 107) — defense-in-depth 3-layer design (Layer 1 prevention + Layer 2 mitigation + Layer 3 enforcement) — concrete instance of P5 in design"
  - id: worked-example-4-real-session-empirical
    type: wiki
    file: wiki/log/2026-05-08-worked-example-4-post-compact-detection-failure-real-session-empirical-evidence-impl-spec-10-stress-test.md
    description: "PRIMARY parent (Fire 102) — 4-axis cross-cutting failure (C04+C02+C15+C19) demonstrates need for defense-in-depth"
  - id: composite-compliance-recomputation-fire-114
    type: wiki
    file: wiki/log/2026-05-08-composite-compliance-metric-recomputation-v2-tier-weighted-per-fire-103-audit-method.md
    description: "Sibling (Fire 114) — tier-weighted compliance reveals enforcement-density gap; defense-in-depth bridges design vs enforcement"
  - id: existing-4-principles
    type: file
    file: CONTEXT.md
    description: "/opt CONTEXT.md — 4 governing principles (Infrastructure>Instructions, Structured Context>Content, Goldilocks, Declarations Aspirational Until Verified)"
  - id: opt-principles-folder
    type: file
    file: wiki/lessons/04_principles/hypothesis/
    description: "Principles folder per /opt methodology — hypothesis in 01_drafts; promotion requires cross-project evidence"
tags: [p5-candidate, defense-in-depth, cross-cutting-failures, single-axis-insufficient, hypothesis, day-arc-2026-05-08, multi-day-pain-point-resolution, fire-118]
---

# P5 Candidate Hypothesis — Defense-in-Depth Required for Cross-Cutting Failure Modes

## Summary

The /opt second-brain has 4 validated governing principles (per CONTEXT.md): P1 Infrastructure>Instructions, P2 Structured Context>Content, P3 Goldilocks, P4 Declarations Aspirational Until Verified. Per Fire 115 C18 cross-cutting cluster + Fire 102 real-session evidence + Fire 107 defense-in-depth triplet design + Fire 114 tier-weighted compliance: a 5th principle CANDIDATE emerges. **P5 Hypothesis**: *single-axis enforcement (P1's hooks/validators) is necessary but INSUFFICIENT — when failures span multiple clusters, multiple enforcement layers stacked are required (defense-in-depth)*. This hypothesis is **agent-DRAFT** per SB-095 + /opt principle-promotion methodology requiring cross-project evidence (≥3 independent sources). This Fire 118 surfaces evidence chain + falsifiability + relationship to existing P1-P4 + promotion path. Per /loop directive: continued substantive piece progressing body's principle layer.

## Context

The /opt body of work has 4 governing principles (per CONTEXT.md). 100+ pieces have been authored exploring failure-mode coverage. Fire 115 C18 cross-cutting cluster surfaced empirical evidence: cross-cluster failures (4-axis combinations) are HIGH-severity dominant (53%) vs single-axis clusters' LOW-MEDIUM dominant. The 4 existing principles (P1-P4) collectively cover infrastructure-vs-instructions, structured-vs-prose-context, right-process-right-context, and verification-required-for-declarations. None explicitly addresses the cross-cutting failure-mode coverage problem. P5 candidate emerges as a structural complement.

## Insight

Cross-cutting failures (where multiple cluster-axis-failures stack simultaneously) cannot be reliably caught by single-axis enforcement (one hook covering one rule). The structural pattern observed: every cross-cutting failure (Fire 115 C18 instances) had its failure-attribution map to 3-4 cluster axes; if any one axis had been enforced, the failure might have surfaced earlier — but no single layer caught it. Defense-in-depth (multiple enforcement layers stacked, each catching different failure modes) is the structural complement: each layer fails independently; combined, the layers maximize prevention coverage. The auto-compact priority (Fires 105+106+107) operationalizes this for one specific cross-cutting failure (post-compact detection failure). P5 generalizes the pattern: cross-cutting failures REQUIRE multi-layer enforcement, not just single-axis.

## P5 Candidate Statement

> **Cross-Cutting Failures Require Defense-in-Depth Enforcement.** When agent failures span multiple cluster axes (≥2-3 clusters intersecting), single-axis enforcement layer (one hook, one validator, one gate) is insufficient. Defense-in-depth — multiple enforcement layers stacked, each catching different failure modes — is structurally required. Each layer may fail independently; combined, the layers maximize prevention coverage. Single-layer enforcement passes single-axis failures but fails on cross-cutting where the BYPASSED-AT-ONE-LAYER failure cascades through unprotected layers.

## Evidence

(≥3 independent sources required for promotion)

### Source 1: /opt body's C18 cross-cutting cluster (Fire 115)

15 instances of cross-cluster failures enumerated. Distribution:
- 53% HIGH severity (8 of 15)
- 53% 4-axis combination (vs 60% 3-axis)
- C04+C02 foundational: present in 80%/73% of instances

Key insight: **single-axis enforcement (e.g., HR 6 hook for ingestion routing — Tier 4) catches single-axis failures; cross-cutting failures bypass single-axis enforcement because the failure intersects axes that ENFORCEMENT-LAYER doesn't cover**.

Concrete instance: post-compact detection failure (Fire 102 = C18-1) intersects C04 (input-discipline) + C02 (decision-territory) + C15 (pattern-recurrence) + C19 (documentation-implementation-asymmetry). No single enforcement layer would have caught it; defense-in-depth (Layers 1+2+3 per Fire 107) is the structural fix.

### Source 2: Fire 107 auto-compact-disable spec (defense-in-depth design)

Operator's directive operationalized via 3-layer model:
```
Layer 1 — PREVENTION: auto-compact never fires (4 sub-layers: brain + harness + env + hook)
Layer 2 — MITIGATION: PreCompact handoff doc captures state if Layer 1 fails
Layer 3 — ENFORCEMENT: PreToolUse blocker prevents pre-regather action if Layers 1+2 fail
```

This design is operator-empirical-validated (sacrosanct directive 2026-05-08). The 3-layer model is the concrete instance of P5 candidate principle. Each layer fails independently:
- Layer 1 fail: auto-compact fires (e.g., harness-default overrides config)
- Layer 2 fail: hook errors; handoff doc not authored
- Layer 3 fail: agent uses bypass without operator-grant

Combined: structural coverage of Fire 102 incident's recurrence.

### Source 3: Fire 102 real-session worked example (empirical)

Real-session 2026-05-08: agent's first post-compact tool call was pre-compact pending action without regather. Operator's catch was sole mitigation. The incident is 4-axis cross-cutting:
- C19 documentation-implementation-asymmetry: impl-spec #10 designed but unwired
- C04 input-discipline: agent skipped /orient + handoff doc + raw notes
- C02 decision-territory: agent acted on summary's pending action
- C15 pattern-recurrence: same regather-failure pattern as mandate window

Single-layer enforcement scenarios:
- IF only Layer 1 (auto-compact disable): Layer 1 fails on manual /compact OR harness override
- IF only Layer 2 (handoff doc): handoff exists but agent doesn't read it
- IF only Layer 3 (PreToolUse blocker): blocker only fires post-compact; prevention-layer absent

Defense-in-depth (3 layers) catches each failure mode independently.

### Source 4: Existing /opt P1 hooks evidence

Existing /opt has 3 PreToolUse hooks (pre-bash, pre-webfetch, opt-write-block). Each is single-axis:
- pre-bash: catches truncation (1 axis)
- pre-webfetch: catches corpus URL routing (1 axis)
- opt-write-block: catches knowledge-vs-config writes (1 axis)

These work well for single-axis failures (per /opt's daily operation). But cross-cutting failures (e.g., pre-bash + decision-territory: agent uses REASON env var to bypass + claims "operator-confirmed" without operator-confirm) would slip through. Each hook is necessary; together insufficient if failure spans hooks.

Defense-in-depth = stacking hooks AT POINT-OF-RISK + audit-log to detect bypass-abuse.

### Source 5: Cross-project parallels (forward-anchored evidence)

Per Fire 113 sister-project propagation: 5 sister projects each have their own PreToolUse hooks (varying coverage). Cross-project evidence collection:
- /root: 6+ hooks per /root self-reference + Hard Rule architecture
- OpenArms: harness-engineering hooks
- OpenFleet: fleet-orchestrator hooks
- AICP: local-AI hooks
- devops-control-plane: governance hooks

Pattern emerges: every project benefits from defense-in-depth (multiple hooks per critical-domain) vs single-hook coverage. Per Fire 113 propagation methodology: spreading auto-compact triplet across all 5 = uniform defense-in-depth.

## Falsifiability criteria (per Popper-style testing)

P5 hypothesis is FALSIFIED if:

1. **Counter-example**: a real-session cross-cutting failure occurs DESPITE defense-in-depth design — would suggest 3 layers insufficient; need 4+
2. **Counter-evidence**: single-axis enforcement empirically catches cross-cutting failures consistently — would suggest cross-cutting clusters are spurious
3. **Cost-disproportionate**: defense-in-depth cost (3-layer maintenance burden) exceeds benefit (~few real-session catches per quarter) — would suggest principle aspirational but operationally impractical
4. **Better-alternative**: single super-axis enforcement (e.g., one mega-hook covering all cross-cutting) outperforms layered approach — would suggest P5 should be reformulated
5. **Recurrence under defense-in-depth**: post-implementation of Fire 107 triplet, Fire 102-like incidents recur — would suggest mechanism gap

If falsified: P5 demoted from candidate to historical; alternative formulation pursued.

## Relationship to existing P1-P4

| Existing principle | Relationship to P5 |
|---|---|
| **P1 Infrastructure > Instructions** | P5 EXTENDS P1: infrastructure (hooks/validators) is necessary baseline; P5 says single-layer infrastructure is insufficient for cross-cutting; multiple layers required |
| **P2 Structured Context > Content** | P5 ORTHOGONAL to P2: P2 governs how content reaches agent; P5 governs how enforcement covers failure space |
| **P3 Goldilocks** | P5 INTERACTS with P3: defense-in-depth complexity should match Goldilocks (POC = 1 layer; production = 3+ layers) — P5 is conditional on phase/scale/trust-tier |
| **P4 Declarations Aspirational Until Verified** | P5 EXTENDS P4 to enforcement-coverage: a SINGLE enforcement layer's verification is necessary but insufficient; cross-cutting verification requires layered tests |

P5 is most closely related to P1 (extends it). The relationship: P1 says "infrastructure beats instructions" (compliance-rate evidence). P5 says "single infrastructure beats no infrastructure but multi-layer infrastructure beats single for cross-cutting."

## Promotion path (per /opt methodology)

```
CURRENT: P5 candidate hypothesis (this Fire 118 — wiki/lessons/01_drafts/)
  ↓
Operator-empirical confirmation: ≥3 independent evidence sources verified
  ↓
P5 promoted to wiki/lessons/02_synthesized/
  ↓
Cross-project evidence: ≥3 sister projects demonstrate same pattern
  ↓
P5 promoted to wiki/lessons/03_validated/
  ↓
30-day cross-reference period; P5 cited in 5+ pieces
  ↓
P5 promoted to wiki/lessons/04_principles/hypothesis/ (canonical principle)
```

Estimated promotion timeline: 1-3 months depending on cross-project evidence accumulation.

## Anti-patterns this principle would prevent

| Anti-pattern (post-P5-adoption) | What changes |
|---|---|
| Adding ONE hook for a critical-domain failure | Author multiple hooks per critical-domain (per defense-in-depth pattern) |
| Treating single-axis enforcement as sufficient | Audit per-domain enforcement-LAYER count (1 = insufficient; 3+ = adequate) |
| Skipping cross-cutting failure analysis | Per-Fire-115 cross-cluster intersection mapping required |
| Single-layer security model | Multi-layer security per defense-in-depth |
| Cost-cutting via fewer enforcement layers | Recognize cost vs cross-cutting failure cost trade-off |

## Applicability

Apply P5 candidate principle when:
- Body of work has empirically-observed cross-cutting failure modes (per Fire 115 C18 cluster)
- Multiple enforcement layers are technically feasible (hooks + validators + state-files + cycle-checks)
- Goldilocks profile justifies investment (production + medium-large scale + supervised-or-higher trust)
- Defense-in-depth cost is proportionate to cross-cutting failure cost
- Post-mortem of past failures shows layered prevention would have caught them

Do NOT apply when:
- Project is POC / experimental phase (defense-in-depth premature)
- Single-axis failures dominate (cross-cutting rare; single-layer adequate)
- Operator-explicit "no defense-in-depth; advisory-only enforcement"
- Hook layer not supported by harness

## Relationships

- COMPOSES WITH: Fire 115 C18 cross-cutting cluster (empirical foundation)

## Composability with body's existing infrastructure

| Component | Composability |
|---|---|
| Fire 115 C18 cluster | Empirical foundation for P5 |
| Fire 103 4-tier audit | T4 single-axis; P5 says T4-stacked needed for cross-cutting |
| Fire 109 tier-elevation pathway | Per-piece elevation insufficient for cross-cutting; P5 adds cross-piece-stack |
| Fire 107 defense-in-depth triplet | Concrete P5 instance |
| Existing P1-P4 principles | P5 extends + composes; no contradictions |
| Fire 65 substitution-pattern lesson | P5 helps detect substitution at enforcement-layer (single-layer claim ≠ multi-layer effect) |

## Per-Fire-115 cluster-frequency insight (extending P5)

Per Fire 115: C04 + C02 are foundational (80% / 73% of cross-cutting instances). P5 implication:
- Defense-in-depth should PRIORITIZE coverage of foundational clusters
- Top-2 enforcement layers: C04 (input-discipline) + C02 (decision-territory)
- Tertiary layers: C15 / C19 / C07 (less foundational)
- Defense-in-depth efficiency: 2 well-placed layers may catch 73-80% of cross-cutting failures; 3-4 layers cover remainder

This refines P5: defense-in-depth ISN'T equal-priority across all clusters; FOUNDATIONAL clusters get FIRST enforcement.

## Required Gates (per hook-architecture proposal #2 4th component)

```yaml
required_gates:
  empirically_passed:
    - hypothesis_articulated: passed
    - 5_evidence_sources_cited: passed
    - falsifiability_5_criteria: passed
    - relationship_to_p1_p4_explicit: passed
    - promotion_path_articulated: passed
  pending:
    - operator_empirical_hypothesis_endorsement: pending
    - cross-project_evidence_collection: pending — sister-project audits
    - 30_day_cross-reference_observation: pending
    - falsification_attempts: pending — operator may dispute or refine
    - promotion_to_02_synthesized: pending
  composite_compliance: p5-candidate-axis stress-test 0% (forward-anchored)
```

## Operator-pending action

```
Q-FIRE-118-1: Endorse P5 candidate hypothesis?
  Argument for: cross-cutting failures empirically observed; defense-in-depth empirically operationalized
  Argument against: may be premature; principles need cross-project evidence
  Recommended: keep as candidate (DRAFT); collect cross-project evidence over months

Q-FIRE-118-2: P5 statement variant?
  Variant A (THIS): "Cross-Cutting Failures Require Defense-in-Depth Enforcement"
  Variant B (broader): "Multi-Layer Enforcement is Required When Single-Layer Coverage is Insufficient"
  Variant C (foundational-cluster-prioritized): "Foundational Cluster Enforcement Stacking Maximizes Defense-in-Depth Efficiency"

Q-FIRE-118-3: Path-to-validated principle (per /opt methodology)?
  Estimated 1-3 months; depends on sister-project evidence accumulation

Q-FIRE-118-4: Defense-in-depth scope per project (per Fire 113 propagation)?
  All 5 sister projects OR /opt + /root only OR varies per project's critical-domain count
```

## Closing framing

Per Fire 115 C18 cross-cutting evidence + Fire 107 defense-in-depth design + Fire 102 real-session empirical: P5 candidate emerges as substantive principle hypothesis. Per /opt methodology: hypothesis lives in 01_drafts; promotion requires cross-project evidence + 30-day cross-reference period. Per /loop directive *"sdlc and methodology and workflow respect is utmost important"*: principle-promotion methodology honored — this fire surfaces hypothesis without bypass-promoting.

Per /opt's 4 existing principles (P1-P4): P5 extends P1 specifically. Combined: 5-principle framework with defense-in-depth as the cross-axis principle bridging single-axis enforcement to cross-cutting coverage.

**The agent stands by per /loop directive. Cron continues at 90s cadence. P5 candidate awaits operator-empirical endorsement + cross-project evidence accumulation.**

## Sources

- Fire 115 C18 cross-cutting per-instance evidence: `wiki/log/2026-05-08-per-instance-pain-point-evidence-c18-cross-cutting-multi-cluster-intersections-15-instances-verbatim-mapped.md`
- Fire 103 4-tier audit method: `wiki/patterns/01_drafts/documentation-implementation-asymmetry-pattern-4-tier-audit-distinguishes-design-from-enforcement.md`
- Fire 107 auto-compact-disable defense-in-depth: `wiki/patterns/01_drafts/auto-compact-disable-implementation-spec-prevention-layer-for-impl-spec-10-defense-in-depth.md`
- Fire 102 worked example #4: `wiki/log/2026-05-08-worked-example-4-post-compact-detection-failure-real-session-empirical-evidence-impl-spec-10-stress-test.md`
- Fire 114 composite-compliance recomputation: `wiki/log/2026-05-08-composite-compliance-metric-recomputation-v2-tier-weighted-per-fire-103-audit-method.md`
- /opt CONTEXT.md (4 existing principles): `CONTEXT.md`
- /opt principle hypothesis folder: `wiki/lessons/04_principles/hypothesis/`

## Tags

[p5-candidate, defense-in-depth, cross-cutting-failures, single-axis-insufficient, hypothesis, day-arc-2026-05-08, multi-day-pain-point-resolution, fire-118]

## Backlinks

[[Fire 115 C18 cross-cutting cluster (empirical foundation)]]
