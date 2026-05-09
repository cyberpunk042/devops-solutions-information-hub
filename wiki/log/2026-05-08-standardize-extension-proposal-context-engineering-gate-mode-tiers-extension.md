---
title: "Standardize Extension Proposal — context-engineering.md Gate-Mode Tiers Extension"
type: note
note_type: session
domain: log
status: synthesized
confidence: high
created: 2026-05-08
updated: 2026-05-08
sources:
  - id: context-engineering-rule-target
    type: project
    project: root-ghostproxy
    path: /root/.claude/rules/context-engineering.md
    description: "PRIMARY target. /root context-engineering rule with 4 injection modes (auto/pre/on-demand/facultative). This proposal extends with new sub-section: Gate-Mode Tiers — input/decision/correction/severity/regression/drift/stage-class as 7 distinct gate axes mapping to the 13-gate composition."
  - id: comprehensive-13-gate-pattern
    type: wiki
    file: wiki/patterns/01_drafts/comprehensive-agent-action-emission-pipeline-13-gate-composition-architecture.md
    description: "Source pattern — 13-gate unified composition with 9 PreToolUse axes; this proposal maps the gate-axes to context-engineering's gate-mode-tiers extension"
  - id: substitution-pattern-meta-frame
    type: wiki
    file: wiki/lessons/01_drafts/documentation-as-substitute-for-discipline-the-meta-pattern.md
    description: "Meta-frame — context-engineering rule documenting injection modes WITHOUT documenting gate-mode tiers IS partial coverage of the discipline substrate"
  - id: prior-standardize-proposals
    type: wiki
    file: wiki/log/2026-05-08-standardize-extension-proposal-methodology-stage-class-enforcement-extension.md
    description: "Sibling proposal #3 — methodology stage-class extension; this proposal #4 is final in standardize-phase"
  - id: stress-testing-as-validation-lesson
    type: wiki
    file: wiki/lessons/01_drafts/stress-testing-as-validation-the-only-way-to-surface-aspirational-vs-operational-gaps.md
    description: "Promotion-mechanism — gate-mode tiers compliance per stress-test data per piece #18"
tags: [standardize-proposal, rule-extension-proposal, context-engineering, gate-mode-tiers, 7-axis-extension, operator-confirmation-pending, day-arc-2026-05-08, multi-day-pain-point-resolution, mission-2026-05-06]
---

# Standardize Extension Proposal — context-engineering.md Gate-Mode Tiers Extension

## Summary

Proposes extending `/root/.claude/rules/context-engineering.md` with a new sub-section **Gate-Mode Tiers** that maps the 7 distinct gate axes from the 13-gate composition (input / decision-territory / correction-shape / severity-blast-radius / regression-test / drift-detection / stage-class) into the existing 4-mode injection framework (auto/pre/on-demand/facultative). The current rule documents WHEN context lands in agent's window (timing axis); the proposed extension documents WHAT enforcement gates fire on that context (axis axis). Together: timing × axis = the structural enforcement plane. This is /root operator-territory; agent CANNOT auto-merge into /root canonical rules. This proposal IS the operator-confirmation gate.

## Operator-confirmation decision points

- **A** — apply gate-mode tiers extension (7-axis taxonomy + per-axis injection-mode mapping)
- **B** — apply selectively (subset of axes most operationally relevant)
- **C** — defer
- **D** — reject + revise

## Why context-engineering.md specifically

The existing rule answers "WHEN does context reach the agent?" (4 injection modes). It does NOT answer "WHAT enforcement gate fires on the context once it arrives?" (gate-axis taxonomy). The 13-gate composition pattern (sister piece) supplies the latter; this rule extension makes the answer canonical at /root rule layer.

The rule's existing 4-mode framework + the proposed 7-axis gate-mode-tiers compose into a 4×7 enforcement matrix:
- 4 injection modes × 7 enforcement axes = 28 distinct enforcement contexts
- Each cell is either applicable (axis fires at this injection-mode timing) or not-applicable
- The matrix exposes COVERAGE GAPS empirically — cells where rule says "axis applies" but no hook implements the enforcement IS substitution-pattern recursive instance

## Proposed Edit — add new section after "Mode → context profile mapping"

**Insert as new sub-section before "Cross-references":**

```markdown
## Gate-Mode Tiers (NEW per 13-gate composition 2026-05-08)

Per piece #1 (comprehensive-13-gate-pattern) + piece #18 (stress-testing-as-validation): the 4 injection modes (timing axis: WHEN context lands) compose with 7 enforcement axes (axis axis: WHAT gate fires on context) into the structural enforcement plane.

**The 7 gate-axes**:

| # | Axis | What it gates | Per-axis cluster |
|---|---|---|---|
| 1 | **input-discipline** | What agent reads BEFORE acting (recent operator messages, brain files, raw notes) | C04 |
| 2 | **decision-territory** | Whether decision is agent-territory or operator-territory | C02 |
| 3 | **correction-shape** | Whether correction is one-notch or extreme-swing (calibration discipline) | C08 |
| 4 | **severity-blast-radius** | Action's reversibility + scope (T1 catastrophic / T2 high / T3 medium / T4 low) | C14 |
| 5 | **regression-test** | Whether tests pass before+after edit (verified-edit enforcement) | C03 |
| 6 | **drift-detection** | Whether action drifts from active task scope | C13 |
| 7 | **stage-class** | Whether edit respects methodology stage (document/design/scaffold/implement/test) | C10 |

**Each axis × each injection-mode**:

| Gate-axis | Auto-injection | Pre-injection | On-demand | Facultative |
|---|---|---|---|---|
| input-discipline | session-start banner | /orient pre-load | per-topic load | mode-specific brain pieces |
| decision-territory | (n/a) | territory-check at /cycle | (n/a) | mode-specific authority profile |
| correction-shape | (n/a) | post-correction sentinel state-file | (n/a) | (n/a) |
| severity-blast-radius | settings.json deny rules | severity-classifier at PreToolUse | per-action class lookup | mode-specific override authority |
| regression-test | tools.run-tests baseline | post-edit verify | per-edit gate | (n/a) |
| drift-detection | active-task state-file | task-anchor banner per-prompt | (n/a) | (n/a) |
| stage-class | engine config auto-load | stage-aware /cycle | per-edit lookup | mode-specific stage authority |

**Empirically-passed cells** (per stress-test data 2026-05-05 → 2026-05-08): 2 of 28 (input-discipline auto + drift-detection pre via active-task banner). Remaining 26 cells: forward-anchor for hook implementation per piece #18 stress-test execution discipline.

**Per piece #2 substitution-pattern recursive applicability**: documenting the matrix above WITHOUT implementing the cells IS the recursive instance. Documenting + implementing closes the substitution at context-engineering layer.

**Strictness tier**: Strict per cell (when implemented + stress-tested) / Aspirational per cell (when documented but not implemented). Tier graduates per cell.

**Composite-compliance metric**: per piece #18 stress-test data, target ≥85% per-cell operational-compliance. Cell-level granularity exposes gaps; row-level (per axis) reveals coverage; column-level (per injection-mode) reveals timing strategy fitness.

**Anti-pattern**: declaring the 28-cell matrix as the discipline substrate WITHOUT per-cell stress-test data. The matrix becomes substitution-pattern at meta-meta-meta layer (rule-extension-without-enforcement).

**Empirical evidence**: 64-hour /root failed-conversation arc 2026-05-04 → 2026-05-08 — agent operated with ~2 of 28 cells operationally enforced (input-discipline auto-banner + drift-detection task-anchor). Remaining 26 cells: aspirational. Result: 180 pain-point instances across 15 clusters mapped predominantly to the 26 unenforced cells.

**Pairing with sibling rule extensions**:
- Sibling proposal #1 (operating-principles 16th principle) — meta-principle that infrastructure must be used; gate-mode tiers IS the implementation substrate
- Sibling proposal #2 (hook-architecture REQUIRED-gates 4th component) — per-hook stress-test declaration; gate-mode tiers IS the cell where each hook lives
- Sibling proposal #3 (methodology stage-class-enforcement) — the stage-class axis row above; sibling proposal codifies one row of the matrix
```

**Diff scope**: ~50 lines added to existing context-engineering.md.

## Why gate-mode tiers specifically

The 4-mode framework is necessary but not sufficient — it answers timing-axis but leaves enforcement-axis underspecified. The 7-axis gate taxonomy from piece #1 supplies the enforcement-axis vocabulary; the cross-product (4 × 7 = 28 cells) exposes coverage empirically.

Without gate-mode-tiers extension, the rule remains susceptible to substitution-pattern: the rule documents timing comprehensively but leaves enforcement implicit, allowing aspirational-without-operational pattern to recur.

## Per piece #2 + #18 recursive applicability

Authoring "gate-mode tiers extension" WITHOUT pairing it to per-cell hook implementation IS the recursive instance per piece #2 Insight 2. The cure (this proposal's structural commitment): rule extension is operationally meaningful only when hooks per-cell are actually implemented + stress-tested per piece #18.

Operator-decision: apply Option A (extension + commitment to implement per-cell) or Option C (defer until hook infrastructure for cell coverage exists).

## Composability with sibling standardize-phase proposals (CLOSES standardize-phase)

| # | Target rule | Proposal status |
|---|---|---|
| 1 | operating-principles.md — 16th principle (infrastructure-must-be-used) | Proposed (sibling log) |
| 2 | hook-architecture.md — REQUIRED-gates 4th component | Proposed (sibling log) |
| 3 | methodology.md — stage-class-enforcement extension | Proposed (sibling log) |
| **4 (THIS, FINAL)** | context-engineering.md — gate-mode tiers extension | Proposed (this log) |

Standardize-phase complete with 4 proposals. Each is operator-confirmation territory; agent CANNOT auto-merge into /root canonical rules. **Forward-anchor**: teach-phase (learning-paths) → offer-phase (gateway-contribute pathway).

## Verification of accuracy

Operator-empirical verification recommended:
- Verify 7-axis taxonomy matches piece #1 (comprehensive-13-gate-pattern) gate-axes
- Verify 28-cell matrix is well-formed (no duplicate cells; n/a marks consistent)
- Verify "2 of 28 empirically passed" matches forensic measurements
- Verify composite-compliance metric formula matches piece #18

## Sources

- Source rule: `/root/.claude/rules/context-engineering.md`
- Source pattern (13-gate composition): `comprehensive-agent-action-emission-pipeline-13-gate-composition-architecture.md`
- Source lesson (substitution-pattern meta-frame): `documentation-as-substitute-for-discipline-the-meta-pattern.md`
- Source lesson (stress-testing): `stress-testing-as-validation-the-only-way-to-surface-aspirational-vs-operational-gaps.md`
- Sibling proposals: 2026-05-08 standardize #1 / #2 / #3

## Tags

[standardize-proposal, rule-extension-proposal, context-engineering, gate-mode-tiers, 7-axis-extension, operator-confirmation-pending, day-arc-2026-05-08, multi-day-pain-point-resolution, mission-2026-05-06]
