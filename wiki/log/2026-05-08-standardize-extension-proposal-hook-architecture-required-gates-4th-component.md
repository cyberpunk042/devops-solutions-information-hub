---
title: "Standardize Extension Proposal — hook-architecture.md REQUIRED-Gates 4th Component"
type: note
note_type: session
domain: log
status: synthesized
confidence: high
created: 2026-05-08
updated: 2026-05-08
sources:
  - id: hook-architecture-rule-target
    type: project
    project: root-ghostproxy
    path: /root/.claude/rules/hook-architecture.md
    description: "PRIMARY target. /root hook-architecture rule with 3-component design pattern (insertion / reason / remediation). This proposal recommends extending with 4th component: REQUIRED-gates declaration per piece #18 stress-testing-as-validation discipline."
  - id: stress-testing-as-validation-lesson
    type: wiki
    file: wiki/lessons/01_drafts/stress-testing-as-validation-the-only-way-to-surface-aspirational-vs-operational-gaps.md
    description: "Source lesson — REQUIRED-gates discipline needs stress-test data per piece #18; without it, hooks are aspirational"
  - id: substitution-pattern-meta-frame
    type: wiki
    file: wiki/lessons/01_drafts/documentation-as-substitute-for-discipline-the-meta-pattern.md
    description: "Meta-frame — hooks without REQUIRED-gates declaration are documentation-as-substitute-for-enforcement"
  - id: comprehensive-13-gate-pattern
    type: wiki
    file: wiki/patterns/01_drafts/comprehensive-agent-action-emission-pipeline-13-gate-composition-architecture.md
    description: "13-gate composition — provides per-gate REQUIRED-gates declaration as concrete exemplar"
  - id: prior-standardize-proposal-1
    type: wiki
    file: wiki/log/2026-05-08-standardize-extension-proposal-operating-principles-16th-principle-infrastructure-must-be-used.md
    description: "Sibling standardize proposal #1 — operating-principles 16th-principle infrastructure-must-be-used"
tags: [standardize-proposal, rule-extension-proposal, hook-architecture, required-gates-4th-component, operator-confirmation-pending, day-arc-2026-05-08, multi-day-pain-point-resolution, mission-2026-05-06]
---

# Standardize Extension Proposal — hook-architecture.md REQUIRED-Gates 4th Component

## Summary

Proposes extending `/root/.claude/rules/hook-architecture.md` 3-component hook design pattern (logical insertion + logical reason + remediation offer) with a 4th component: **REQUIRED-gates declaration**. Per substitution-pattern lesson Insight 1: hooks without explicit declaration of WHICH stress-test gates they have passed AND WHICH gates remain pending ARE recursive substitution — design-without-enforcement. The 4th component closes this gap by mandating each hook declare: (1) the test scenarios it has empirically passed, (2) the test scenarios that remain pending, (3) the composite-compliance contribution per stress-test data per piece #18. This is /root operator-territory; agent CANNOT auto-merge into /root canonical rules. This proposal IS the operator-confirmation gate.

## Operator-confirmation decision points

- **A** — apply REQUIRED-gates 4th component to all hook design (existing 3-component preserved + 4th added)
- **B** — apply selectively (4th component required only for new hooks; existing hooks grandfathered)
- **C** — defer
- **D** — reject + revise

## Why hook-architecture.md specifically

The rule defines the canonical hook design pattern for /root. Currently 3 components: logical insertion + logical reason + remediation. Each component addresses ONE failure mode:
- **Insertion** addresses wrong-event firing
- **Reason** addresses black-box enforcement
- **Remediation** addresses stuck-without-alternative

The 3 components close design failures BUT do NOT address the operational-vs-aspirational gap. A hook with all 3 components can still be ASPIRATIONAL — passing static tests but failing real-session behavior (per piece #1 stress-testing-as-validation lesson). The 4th component closes this final gap.

## Proposed Edit — extend "Hook design pattern (every hook MUST follow)" section

**Insert after the existing "3. Remediation offer" sub-section:**

```markdown
### 4. REQUIRED-gates declaration (NEW per substitution-pattern lesson 2026-05-08)

Per piece #18 stress-testing-as-validation lesson + piece #2 substitution-pattern lesson Insight 1: a hook MUST declare which stress-test gates it has empirically passed AND which remain pending. Without this declaration, the hook is structurally-fixed but behaviorally aspirational — exactly the substitution pattern at the hook layer.

The declaration takes 3 sub-fields:

**(a) Empirically-passed gates** — list of stress-test scenarios with real-session evidence. Format: `<gate-name>: passed <YYYY-MM-DD> via <evidence-source>` (real-session diag log / observed behavior / operator-empirical confirmation).

**(b) Pending gates** — list of stress-test scenarios planned but not yet executed. Format: `<gate-name>: pending — <blocker or planned-trigger>`.

**(c) Composite-compliance contribution** — the hook's share in the composite operational-compliance metric per piece #18. Format: `<gate-axis>: ~<percentage>% per stress-test <YYYY-MM-DD>`.

**Example** (hook-architecture stress-test declaration):

```yaml
required_gates:
  empirically_passed:
    - cross_fire_suppression: passed 2026-05-05 via diag log SB-088
    - real_session_invocation: passed 2026-05-05 via session-restart trace
  pending:
    - high_load_concurrent_invocation: pending — staging-env not yet provisioned
    - operator_bypass_legitimate_use: pending — needs 5+ real REASON= invocations
  composite_compliance: input-discipline-axis ~85% per stress-test 2026-05-05
```

**Why this matters**: a hook without REQUIRED-gates declaration has unknown operational status. P1 quantified gap (prose ~25% / hooks ~100%) is per-axis; without per-hook declaration, the composite is unmeasured. With declaration: agent + operator both see operational vs aspirational at-a-glance.

**Anti-pattern**: declaring "implementation: complete" without paired stress-test gates. Per piece #18: implementation status ≠ operational status. Stress-test data IS the bridge.

**Strictness tier**: Strict (when paired with stress-test execution discipline) / Aspirational (without stress-tests). Tier graduates with stress-test maturity per piece #18.
```

**Diff scope**: ~25 lines added to existing hook-architecture.md.

## Why 4th component specifically

The 3-component pattern closes DESIGN failures (wrong insertion / black-box / stuck-without-alternative). The 4th component closes the OPERATIONAL failure (designed-but-not-stress-tested). Without the 4th component, the rule remains susceptible to substitution-pattern: rules-about-hooks-without-stress-test-gates IS the recursive instance.

The 4 components together close the substitution-pattern at the hook layer for /root.

## Per piece #2 + #18 recursive applicability

Authoring "REQUIRED-gates 4th component" as a rule extension WITHOUT pairing it to stress-test execution discipline IS the recursive instance per piece #2 Insight 2. The cure (this proposal's structural commitment): the 4th component is operationally-meaningful only when stress-tests are actually executed. Without execution, the declaration is aspirational; with execution, the declaration is operational + measured.

Operator-decision: apply Option A (REQUIRED-gates discipline + commit to executing stress-tests) or Option C (defer until stress-test infrastructure exists).

## Composability with sibling standardize-phase proposals

| # | Target rule | Proposal status |
|---|---|---|
| 1 | operating-principles.md — 16th principle (infrastructure-must-be-used) | Proposed (sibling log) |
| **2 (THIS)** | hook-architecture.md — REQUIRED-gates 4th component | Proposed (this log) |
| 3 | methodology.md — stage-class-enforcement extension | Forward-anchor — codifies C10 stage-gate at rule layer |
| 4 | context-engineering.md — gate-mode tiers extension | Forward-anchor — input/decision/correction/severity/regression/drift/stage-class as gate-mode tiers |

Each is a SEPARATE standardize-phase log entry. Operator decides per-proposal.

## Verification of accuracy

Operator-empirical verification recommended:
- Verify existing 3-component pattern matches stated insertion / reason / remediation
- Verify 4th component fits the existing rule structure without rupture
- Verify YAML example structure parses cleanly
- Verify cross-references to piece #18 + piece #2 are accurate

## Sources

- Source rule: `/root/.claude/rules/hook-architecture.md`
- Source lesson (REQUIRED-gates discipline): `stress-testing-as-validation-the-only-way-to-surface-aspirational-vs-operational-gaps.md`
- Source lesson (substitution-pattern meta-frame): `documentation-as-substitute-for-discipline-the-meta-pattern.md`
- Source pattern (per-gate exemplar): `comprehensive-agent-action-emission-pipeline-13-gate-composition-architecture.md`
- Sibling proposal: `2026-05-08-standardize-extension-proposal-operating-principles-16th-principle-infrastructure-must-be-used.md`

## Tags

[standardize-proposal, rule-extension-proposal, hook-architecture, required-gates-4th-component, operator-confirmation-pending, day-arc-2026-05-08, multi-day-pain-point-resolution, mission-2026-05-06]
