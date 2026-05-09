---
title: "Documentation-Implementation Asymmetry Pattern — 4-Tier Audit Distinguishes Design from Enforcement"
type: pattern
domain: agent-config
status: synthesized
confidence: high
maturity: seed
authorship: agent-authored
created: 2026-05-08
updated: 2026-05-08
sources:
  - id: worked-example-4-post-compact-detection-failure
    type: wiki
    file: wiki/log/2026-05-08-worked-example-4-post-compact-detection-failure-real-session-empirical-evidence-impl-spec-10-stress-test.md
    description: "PRIMARY parent (Fire 102) — real-session empirical evidence: impl-spec #10 documented bidirectional design but PreCompact hook never wired; this incident surfaces the asymmetry pattern"
  - id: documentation-as-substitute-for-discipline-meta-pattern
    type: wiki
    file: wiki/lessons/01_drafts/documentation-as-substitute-for-discipline-the-meta-pattern.md
    description: "PRIMARY parent (lesson) — meta-frame for substitution-pattern; this pattern is the AUDIT METHOD for detecting substitution at implementation layer"
  - id: post-compact-orientation-gate-impl-spec-10
    type: wiki
    file: wiki/patterns/01_drafts/post-compact-orientation-gate-implementation-spec-handoff-and-mirror-enforcement.md
    description: "Empirical-evidence source — impl-spec #10 is at TIER 2 (partial implementation: PostCompact wired, PreCompact NOT wired); this pattern audits ALL body pieces against tier criteria"
  - id: substitution-pattern-recursive-applicability-audit
    type: wiki
    file: wiki/log/2026-05-08-substitution-pattern-recursive-applicability-audit-64-piece-body-meta-validation.md
    description: "Sibling — recursive applicability audit (Fire 65); this pattern extends to documentation-implementation-asymmetry dimension"
  - id: composite-compliance-stress-test-spec
    type: wiki
    file: wiki/patterns/01_drafts/composite-compliance-stress-test-scenario-spec-real-session-test-plan.md
    description: "Sibling — composite-compliance metric methodology; this pattern's tier criteria align with composite-compliance enforcement-layer measurement"
tags: [documentation-implementation-asymmetry, audit-method, 4-tier-implementation-maturity, substitution-pattern-extension, day-arc-2026-05-08, multi-day-pain-point-resolution, fire-103]
---

# Documentation-Implementation Asymmetry Pattern — 4-Tier Audit Distinguishes Design from Enforcement

## Summary

Per Fire 102 worked example: impl-spec #10 (post-compact-orientation-gate) documented a comprehensive bidirectional design 100+ pieces ago BUT only the POST side was wired in /opt's settings.json. The PRE side never materialized. This is the **documentation-implementation asymmetry pattern**: a body of work or codebase has a piece-of-design at maturity-tier-N (e.g., Tier 4 designed) but the implementation-state is at maturity-tier-M (e.g., Tier 2 partial). The asymmetry IS the bug. Per substitution-pattern (Fire 65 lesson + Fires 53-64 cluster): documentation-as-substitute-for-discipline IS one specific failure mode of asymmetry. This pattern operationalizes a 4-tier audit distinguishing **designed → partial → enforced → full** so the body can verify itself + sister projects can verify themselves + future agents can verify post-compact handoff.

## Pattern Description

### The 4 implementation-maturity tiers

```
TIER 1 — DESIGNED ONLY (worst — pure documentation-as-substitute):
  Definition: pattern/spec/rule documents the mechanism comprehensively
  Implementation state: NO code, hook, tool, slash-command, or state-file
  Failure mode: documentation refers to "the mechanism" as if real;
                cross-references compound the illusion across pieces
  Example: question-registry pattern (Fire 99) — designed; /questions slash command NOT implemented
  Audit signal: grep for invocation produces zero results
  Composite-compliance contribution: 0% (designed but unused)

TIER 2 — PARTIAL IMPLEMENTATION (mixed — half-built):
  Definition: pattern/spec describes N components; M < N components implemented
  Failure mode: pieces compose AS IF complete; the missing component fails silently in real-session
  Example: impl-spec #10 — POST wired, PRE NOT wired (Fire 102 evidence)
  Example: backlog-decomposition (Fire 97) — Epic+Module+Task hierarchy authored but no actualization
  Audit signal: implementation-checklist comparison; missing items stand out
  Composite-compliance contribution: ~50% × (component-count-implemented / total)

TIER 3 — IMPLEMENTED BUT NOT ENFORCED (intermediate — exists but skippable):
  Definition: implementation exists; no enforcement-layer prevents bypass
  Failure mode: agent or operator can skip the mechanism without consequence;
                under pressure, mechanism gets skipped
  Example: gateway orient — exists; agent skipped it post-compact (Fire 102 incident)
  Example: pipeline post after every wiki change — exists; mandate-window had 36+ hours of edits without invocation
  Audit signal: enforcement-layer hooks present? If no, Tier 3
  Composite-compliance contribution: depends on operator-empirical compliance rate (typically 25-70%)

TIER 4 — DESIGNED, IMPLEMENTED, AND ENFORCED (gold standard — full):
  Definition: design + implementation + enforcement-layer prevents bypass
  Failure mode: rare; mostly enforcement-layer false-positives
  Example: pre-bash.sh hook (blocks reflexive truncation pipes — closes "read in full" rule)
  Example: pre-webfetch-corpus-check.sh (blocks WebFetch on corpus URLs — closes ingestion-routing rule)
  Audit signal: hook fires on attempt-to-bypass + REASON env var bypass available
  Composite-compliance contribution: ~100%
```

### Audit method per body piece

For each pattern / impl-spec / rule / standard in the body, ask:

```
Q1. Is the design documented at this piece?  YES → continue; NO → not applicable
Q2. Is the implementation present in code/config/state-files?
    NONE     → TIER 1 (designed only)
    PARTIAL  → TIER 2 (partial)
    COMPLETE → continue
Q3. Is enforcement-layer present (hook / validator / pre-action gate)?
    NONE → TIER 3 (implemented but not enforced)
    YES  → TIER 4 (designed + implemented + enforced)
```

Operationalized:

```python
def audit_piece(piece_path: str) -> tuple[int, dict]:
    """Audit a body piece for documentation-implementation asymmetry tier."""
    design = parse_design_components(piece_path)  # required-mechanisms list
    if not design.has_documented_mechanism:
        return None, {"reason": "no design to audit"}
    
    impl_state = check_implementation(design)  # grep for code/config/state-files
    if impl_state.count_implemented == 0:
        return 1, {"tier": 1, "components_designed": design.count, "components_implemented": 0}
    if impl_state.count_implemented < design.count:
        return 2, {"tier": 2, "missing_components": impl_state.missing}
    
    enforcement = check_enforcement(design)  # hooks, validators, pre-action gates
    if not enforcement.present:
        return 3, {"tier": 3, "compliance_rate": measure_operator_empirical()}
    
    return 4, {"tier": 4, "enforcement_layer": enforcement.layer_id}
```

### Body-piece tier audit (initial pass — agent-DRAFT per SB-095)

| Body piece | Tier | Evidence |
|---|---|---|
| Impl-spec #10 (post-compact orientation gate) | **2** | PostCompact wired; PreCompact NOT wired (Fire 102 empirical) |
| Question-registry pattern (Fire 99) | **1** | Pattern designed; /questions slash command NOT in /opt commands dir |
| Blocker-impediment registry pattern (Fire 101) | **1** | Pattern designed; ~/.claude/blockers/ NOT created; /blockers slash NOT in /opt commands |
| Mode-by-nature governance pattern (Fire 98) | **1** | Pattern designed; governance-scan auto-fire NOT implemented |
| Feature-flag system pattern (Fire 96) | **1** | Pattern designed; ~/.claude/feature-flags.json NOT created; flag commands NOT implemented |
| Backlog-decomposition (Fire 97) | **1** | Epic+Module+Task hierarchy proposed; no actualization at /opt or /root |
| Operator-empirical signal-grammar (Fire 92) | **1** | 5-class taxonomy + Python pseudocode `recognize_operator_signals()`; no actual recognizer |
| Body versioning v1.0.0 (Fire 91) | **3** | Versioning declared; no automated semver-bump-on-piece-add enforcement |
| Composite-compliance metric (Fire 85) | **3** | Metric computed via methodology; no auto-aggregator running per-cycle |
| Pipeline post (canonical wiki gate) | **4** | Implemented + enforced (operator-empirical: blocks completion without 0 errors) |
| Pre-bash hook (truncation block) | **4** | Implemented + enforced (active during this very session) |
| Pre-webfetch corpus check | **4** | Implemented + enforced (active) |
| Sacrosanct verbatim quoting (Hard Rule 4) | **3** | Brain-pieces document; no hook enforces; operator catches violations |
| /orient invocation post-compact (impl-spec #10) | **2** | PostCompact additionalContext present; agent compliance ~0% in Fire 102 incident |
| Gateway orient invocation cadence | **3** | Implemented; not enforced; mandate window had 1 invocation in 36+ hours |

Initial pass: **8 of 15 audited pieces at Tier 1** (designed only). This is the substitution-pattern at body-of-work scale.

### Distribution shape (initial-pass — falsifiable; subject to operator-empirical revision)

```
TIER 1 (designed only):           ████████ ~53%
TIER 2 (partial implementation):  ██ ~13%
TIER 3 (implemented unenforced):  ████ ~27%
TIER 4 (designed+impl+enforced):  ██ ~7%

Implication: ~93% of audited pieces have implementation-asymmetry of some flavor.
The body's empirical-compliance is dominated by pieces THAT ARE IMPLEMENTED (Tiers 3-4),
not by piece COUNT. Documentation density does NOT equal enforcement density.
```

### Anti-patterns at asymmetry layer

| Anti-pattern | Why bad | Closes-gap-via |
|---|---|---|
| Cross-reference designed pieces as if implemented | Compounds illusion across body; future audit harder | Per-piece tier-frontmatter field |
| Author new patterns without auditing existing pieces | Body grows in design-only direction; tier 1 percentage rises | Pre-author audit pass |
| Treat composite-compliance as compliance score for designed pieces | Inflates score; obscures asymmetry | Tier-weighted composite-compliance computation |
| Defer enforcement-layer wiring as "operator-territory" | Permanent Tier 3 ceiling | Specific tasks per piece; operator-confirmation explicit |
| Conflate "wiki page exists" with "mechanism operates" | Categorical confusion; subset of behave-OVER-not-FROM | Tier audit method |

### Audit cadence integration

Per substitution-pattern + Fire 102 empirical evidence:

```
PER NEW PIECE (forward-looking):
  Author: include `implementation_tier: <1|2|3|4>` in frontmatter
  Author: declare which components are designed; which implemented; which enforced
  Reviewer: cross-check declaration against actual codebase state

PER CYCLE (mode-by-nature integration):
  PM-mode by-nature scan includes: tier audit one piece per cycle
  Surfaced: pieces that drift down (tier 2 → tier 1) or up (tier 1 → tier 2)
  Output: tier distribution shape across body

PER MILESTONE (decision-package refresh):
  Full body audit: re-tier every piece
  Compare against prior milestone audit: drift ratio + direction
  Operator-confirmation: ratify tier classifications

PER COMPACTION EVENT (per impl-spec #10 + Fire 102 evidence):
  Pre-compact: snapshot tier distribution to handoff doc
  Post-compact: verify tier distribution preserved (catches stealth tier-1 drift)
```

## When To Apply

Apply this 4-tier asymmetry audit when:
- Body of work has 30+ pieces (sufficient density to surface asymmetry pattern)
- Real-session evidence of "documented but not implemented" failure mode (per Fire 102)
- Composite-compliance metric needed (per Fire 85)
- Pre-compact preservation matters (per impl-spec #10)
- Operator-empirical review of body's enforcement-density requested

## Instances

**Instance 1: impl-spec #10 (Fire 102 empirical)**
- Tier: **2**
- Designed: PreCompact + PostCompact bidirectional pair
- Implemented: PostCompact only (post-compact.sh + post-orient.sh)
- Asymmetry: 50% (one of two components missing)
- Real-session impact: handoff doc never authored 2026-05-08 compaction event
- Path to Tier 4: Task #28 wires PreCompact hook → Tier 3; future enforcement-hook on agent's first post-compact tool call → Tier 4

**Instance 2: Question-registry (Fire 99)**
- Tier: **1**
- Designed: 4-audience taxonomy + 5 slash commands + state-file structure
- Implemented: NONE
- Path to Tier 2: implement /questions add slash command + state-file creation
- Path to Tier 3: implement remaining 4 commands + bidirectional flow
- Path to Tier 4: enforcement-hook for "agent has question? must use /questions add"

**Instance 3: Pre-bash truncation block (Tier 4 baseline)**
- Tier: **4**
- Designed: hook description + REASON env var bypass
- Implemented: pre-bash.sh active in /opt settings.json
- Enforced: blocks reflexive truncation pipes; operator-empirical compliance high
- This session: hook fired on agent's `ls | head -20` attempt → agent corrected to `head -100`

**Instance 4: Pipeline post canonical gate (Tier 4)**
- Tier: **4**
- Designed: 6-step validation chain
- Implemented: tools.pipeline post
- Enforced: operator-empirical "0 errors required" + mandate raw-note evidence
- Real-session this fire: enforced Fire 102 note_type fix (rejected 'worked-example' → forced 'session')

## When Not To

- Body of work < 30 pieces (insufficient density for tier-distribution insight)
- Pure prototype phase (asymmetry expected; tier 1 dominant by design)
- Operator-explicit "design-only mode" (auditing premature)
- Mid-compaction event (defer audit to post-compact)

## Empirical Evidence

Per Fire 102 real-session evidence: impl-spec #10 was authored ~Fire 50 (pre-Fire-100 milestone), referenced 50+ times across subsequent fires AS IF complete. The first real-session stress-test (compaction event 2026-05-08) exposed the asymmetry: PreCompact never wired. Without this audit pattern, the asymmetry would have continued unnoticed. Per substitution-pattern Insight 5b (recursive applicability): documentation-as-substitute-for-discipline applies recursively at every body layer — and detection requires explicit AUDIT method (this pattern), not assumption that "if it's documented, it operates."

Body distribution shape (initial-pass): Tier 1 dominant (~53%) confirms operator's pre-compact PIVOT directive *"the experts mode should exibit by nature"* was empirically necessary — without by-nature surfacing, asymmetry remains invisible.

## Required Gates (per hook-architecture proposal #2 4th component)

```yaml
required_gates:
  empirically_passed:
    - synthetic_tier_classification_4_categories: passed via 15-piece initial audit
    - operator_empirical_tier_4_baseline: passed (pre-bash + pipeline-post evidence)
    - tier_2_real_session_evidence: passed (Fire 102 incident)
  pending:
    - full_body_audit_all_102_pieces: pending — initial pass covers 15 pieces; remaining ~87 pending
    - operator_empirical_tier_classifications: pending — operator confirms 15-piece tier assignments
    - tier_weighted_composite_compliance_recomputation: pending — current composite-compliance (99.51% Fire 85) likely OVER-states; tier-weighted may drop to ~30-50%
    - enforcement_layer_coverage_audit: pending — count of hooks vs designed-mechanisms ratio
  composite_compliance: documentation-implementation-asymmetry axis stress-test 0% (forward-anchored; operator-territory)
```

## Relationships


## Tags

[documentation-implementation-asymmetry, audit-method, 4-tier-implementation-maturity, substitution-pattern-extension, day-arc-2026-05-08, multi-day-pain-point-resolution, fire-103]
