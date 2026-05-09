---
title: "Standardize Extension Proposal — methodology.md Stage-Class-Enforcement Extension"
type: note
note_type: session
domain: log
status: synthesized
confidence: high
created: 2026-05-08
updated: 2026-05-08
sources:
  - id: methodology-rule-target
    type: project
    project: root-ghostproxy
    path: /root/.claude/rules/methodology.md
    description: "PRIMARY target. /root methodology rule with 5-stage gates (document/design/scaffold/implement/test) + 9 models. This proposal recommends extending with stage-class-enforcement section: declares which actions are stage-gated AT EDIT-LAND TIME via hook-layer, not just rule-prose."
  - id: stage-class-enforcement-pattern
    type: wiki
    file: wiki/patterns/01_drafts/methodology-stage-gate-edit-land-enforcement-design.md
    description: "Source pattern (C10) — methodology stage-gate edit-land enforcement design specifies WHERE stage-gates fire + WHAT they block + HOW remediation surfaces"
  - id: substitution-pattern-meta-frame
    type: wiki
    file: wiki/lessons/01_drafts/documentation-as-substitute-for-discipline-the-meta-pattern.md
    description: "Meta-frame — methodology stage-gates documented in rule but unenforced at edit-land time IS substitution-pattern at methodology layer"
  - id: comprehensive-13-gate-pattern
    type: wiki
    file: wiki/patterns/01_drafts/comprehensive-agent-action-emission-pipeline-13-gate-composition-architecture.md
    description: "13-gate composition — stage-class-enforcement is gate #9 in the unified pipeline"
  - id: prior-standardize-proposals
    type: wiki
    file: wiki/log/2026-05-08-standardize-extension-proposal-hook-architecture-required-gates-4th-component.md
    description: "Sibling proposal #2 — REQUIRED-gates 4th component (which this proposal pairs with for stage-class hook implementation)"
tags: [standardize-proposal, rule-extension-proposal, methodology, stage-class-enforcement, edit-land-gate, operator-confirmation-pending, day-arc-2026-05-08, multi-day-pain-point-resolution, mission-2026-05-06]
---

# Standardize Extension Proposal — methodology.md Stage-Class-Enforcement Extension

## Summary

Proposes extending `/root/.claude/rules/methodology.md` with a **Stage-Class-Enforcement** section that codifies C10 stage-gate-edit-land-enforcement pattern at the rule layer. The current methodology rule documents 5 stage gates (document/design/scaffold/implement/test) with ALLOWED/FORBIDDEN per stage — but the rule lives at PROSE layer, achieving ~25% compliance per P1. The proposed extension declares: each stage-class transition MUST have a paired hook-layer enforcement at edit-land time (PreToolUse on Edit/Write matchers); without paired enforcement, stage-class declarations are aspirational per P4. This is /root operator-territory; agent CANNOT auto-merge into /root canonical rules. This proposal IS the operator-confirmation gate.

## Operator-confirmation decision points

- **A** — apply stage-class-enforcement extension (rule extension + commitment to implement edit-land hooks per piece C10)
- **B** — apply selectively (extension at rule layer; hook implementation deferred per task-priority)
- **C** — defer
- **D** — reject + revise

## Why methodology.md specifically

The rule is the canonical methodology engine surface for /root. Its existing structure documents:
- 5 universal stages with readiness % bands
- ALLOWED/FORBIDDEN per stage
- 9 methodology models
- Engine config at `wiki/config/methodology.yaml`

The methodology stage-gates are **the most-frequently-violated rule in /root operational history** per pain-point cluster C10 evidence: 13+ instances of edit-stage-class-violation in 64-hour conversation arc (e.g., implementation in document-stage tasks, tests in implement-stage tasks). The rule prose says "stage boundaries are HARD"; empirical reality shows ~25% compliance.

The cure is per piece C10: edit-land enforcement at hook-layer, not just rule-prose. The rule extension below codifies WHEN/WHERE/HOW stage-class-enforcement fires.

## Proposed Edit — add new section after "Stage-boundary discipline"

**Insert as new sub-section after existing "Stage-boundary discipline":**

```markdown
## Stage-Class-Enforcement (NEW per C10 pattern 2026-05-08)

Per piece C10 + piece #18 stress-testing-as-validation: the 5-stage methodology gates are aspirational at the rule-prose layer (P1: ~25% compliance) and operational ONLY when paired with edit-land hook-layer enforcement.

The canonical enforcement design:

**Trigger event**: PreToolUse on Edit + Write + NotebookEdit + MultiEdit matchers.

**Decision logic per stage**:

| Active task stage | ALLOWED edit targets | FORBIDDEN edit targets | Remediation |
|---|---|---|---|
| document (0-25%) | wiki/, raw/notes/, design/*.md | tests/, src/, install.sh op_functions | "Edit blocked: document-stage. Move to design or implement task first." |
| design (25-50%) | wiki/, design/*.md, ADR, tech-spec | tests/, src/, install.sh op_functions | "Edit blocked: design-stage. ALLOWED: design docs only. FORBIDDEN: code/tests." |
| scaffold (50-80%) | type-defs, schema, test-stubs, config-files | implementation logic, real test assertions | "Edit blocked: scaffold-stage. Real assertions in test stage; implementation in implement stage." |
| implement (80-95%) | implementation, integration-wiring | new test files | "Edit blocked: implement-stage. Tests authored at test stage." |
| test (95-100%) | test-implementation, test-results | new features, scope changes | "Edit blocked: test-stage. New features require new task in document stage." |

**Bypass mechanism** (per principle #4 remediation+explanation):

```bash
REASON="<justification>" <edit-command>
```

The bypass is logged to `~/.claude/hooks/stage-class-bypass.log` with timestamp + task-id + reason for audit. Frequent bypasses indicate stage-class taxonomy mismatch — surface to operator for revision.

**Composite-compliance metric**: per piece C10 stress-test evidence, this gate contributes the stage-class axis to the composite operational-compliance metric per piece #18. Target: ≥85% stage-respect at edit-land time.

**Pairing with rule layer**: this enforcement design ASSUMES the methodology engine config (`wiki/config/methodology.yaml`) provides authoritative stage definitions. Without engine config, hook has nothing to evaluate; with engine config, hook becomes operationally meaningful.

**Anti-pattern**: documenting stage-class boundaries in this rule WITHOUT the paired hook implementation IS substitution-pattern (per piece #2). The substitution at methodology layer manifests as: rule says "stage boundaries are HARD"; reality shows ~25% compliance; rule-author cites the rule as evidence stage-respect EXISTS while the empirical instances of violations accumulate.

**Strictness tier**: Strict (when paired with hook implementation + stress-tests) / Aspirational (without). Tier graduates with implementation status.

**Empirical evidence**: 64-hour /root failed-conversation arc 2026-05-04 → 2026-05-08 — 13+ edit-stage-class-violation instances accumulated despite rule-prose stating "stage boundaries are HARD" (per pain-point cluster C10 in master inventory).
```

**Diff scope**: ~40 lines added to existing methodology.md.

## Why stage-class-enforcement specifically

The existing methodology rule + engine config are aspirational at rule-prose layer. Pain-point cluster C10 evidence: stage-class violations are the most-frequent methodology violation in /root operational history. Without edit-land enforcement, the 5-stage gate framework remains aspirational regardless of how much rule-prose detail accumulates (per substitution-pattern lesson).

The stage-class-enforcement extension closes the substitution at methodology layer.

## Per piece #2 + #18 recursive applicability

Authoring "stage-class-enforcement" extension to the methodology rule WITHOUT pairing it to hook implementation IS the recursive instance per piece #2 Insight 2. The cure (this proposal's structural commitment): rule extension is operationally meaningful only when hooks are actually implemented + stress-tested per piece #18.

Operator-decision: apply Option A (extension + commitment to implement) or Option C (defer until hook infrastructure exists).

## Composability with sibling standardize-phase proposals

| # | Target rule | Proposal status |
|---|---|---|
| 1 | operating-principles.md — 16th principle (infrastructure-must-be-used) | Proposed (sibling log) |
| 2 | hook-architecture.md — REQUIRED-gates 4th component | Proposed (sibling log) |
| **3 (THIS)** | methodology.md — stage-class-enforcement extension | Proposed (this log) |
| 4 | context-engineering.md — gate-mode tiers extension | Forward-anchor — input/decision/correction/severity/regression/drift/stage-class as gate-mode tiers |

Each is a SEPARATE standardize-phase log entry. Operator decides per-proposal.

## Verification of accuracy

Operator-empirical verification recommended:
- Verify existing 5-stage table matches stated readiness % bands
- Verify ALLOWED/FORBIDDEN per stage matches piece C10 specification
- Verify bypass mechanism format matches existing hook-architecture pattern
- Verify cross-references to piece C10 + piece #18 + piece #2 are accurate

## Sources

- Source rule: `/root/.claude/rules/methodology.md`
- Source pattern (C10 enforcement design): `methodology-stage-gate-edit-land-enforcement-design.md`
- Source lesson (substitution-pattern meta-frame): `documentation-as-substitute-for-discipline-the-meta-pattern.md`
- Source lesson (stress-testing): `stress-testing-as-validation-the-only-way-to-surface-aspirational-vs-operational-gaps.md`
- Sibling proposals: 2026-05-08 standardize #1 (operating-principles 16th) + #2 (hook-architecture 4th component)

## Tags

[standardize-proposal, rule-extension-proposal, methodology, stage-class-enforcement, edit-land-gate, operator-confirmation-pending, day-arc-2026-05-08, multi-day-pain-point-resolution, mission-2026-05-06]
