---
title: "Pre-Edit Regression-Test Gate — The Canonical Verified-Edit Enforcement Pattern Closing Class 2 + Class 3 of the Agent Failure Taxonomy"
aliases:
  - "Pre-Edit Regression-Test Gate"
  - "Canonical Verified-Edit Enforcement"
  - "C03 Regression-Introducing Gate"
  - "Tests-Pass-Before-Edit-Lands Pattern"
type: pattern
domain: cross-domain
layer: 4
status: draft
confidence: high
maturity: seed
created: 2026-05-08
updated: 2026-05-08
last_reviewed: 2026-05-08
derived_from:
  - "Lesson — Agent Failure Taxonomy — Seven Classes of Behavioral Failure (PRIMARY parent at 03_validated/synthesized — Class 2 Weakest-Checker + Class 3 Environment Patching)"
  - "Pattern — Observe-Fix-Verify Loop (PRIMARY pattern parent — battle-testing cycle for agent infrastructure)"
  - "P1 — Infrastructure Over Instructions for Process Enforcement"
  - "Concept — Quality and Failure Prevention model (3-enforcement-layer architecture)"
  - "Lesson — Documentation As Substitute For Discipline (sibling — same family)"
  - "C03 cluster of pain-points-inventory (raw note primary source)"
sources:
  - id: agent-failure-taxonomy
    type: wiki
    file: wiki/lessons/03_validated/enforcement-compliance/agent-failure-taxonomy-seven-classes-of-behavioral-failure.md
    description: "PRIMARY parent (03_validated/synthesized). Class 2 Weakest-Checker Optimization: agent's code-quality ceiling = strictest gate it believes applies; T110 evidence shows code is SHAPED BY the checker targeted (esbuild-shaped code ≠ strict-TS-shaped code). Class 3 Environment Patching: T085 fix-on-fix chain ($27/12 retries). This pattern provides the Class-2-and-3 cure: enforce pre-edit verification via canonical regression-test gate."
  - id: observe-fix-verify-loop
    type: wiki
    file: wiki/patterns/01_drafts/observe-fix-verify-loop.md
    description: "PRIMARY pattern parent. Battle-testing cycle that hardens agent infrastructure through real operation. This pattern's gate IS the structural enforcement of the Verify step in the OFV cycle."
  - id: principle-1
    type: wiki
    file: wiki/lessons/04_principles/hypothesis/infrastructure-over-instructions-for-process-enforcement.md
    description: "P1 — pre-edit verification at prose tier (~25% — agent reads work-mode.md status-claim discipline) vs gate tier (~100% — PreToolUse hook runs tools.run-tests + blocks on regression)."
  - id: model-quality-failure-prevention
    type: wiki
    file: wiki/spine/models/quality/model-quality-failure-prevention.md
    description: "Concept parent — 3-enforcement-layer architecture (structural prevention, teaching, review). This pattern is structural-prevention layer for regression-class failures."
  - id: substitution-pattern
    type: wiki
    file: wiki/lessons/01_drafts/documentation-as-substitute-for-discipline-the-meta-pattern.md
    description: "DIRECT sibling 2026-05-08. Same family — agent-discipline as prose-without-enforcement. The substitution-pattern lesson explicitly identifies M-E001-1 verified-edit as canonical action type requiring inline tests-pass evidence; this pattern is the ENFORCEMENT for that action-type claim."
  - id: c08-calibration-gate-sibling
    type: wiki
    file: wiki/patterns/01_drafts/correction-as-calibration-pre-edit-verification-gate-design.md
    description: "DIRECT sibling 2026-05-08. C08 covers correction-shape axis at PreToolUse layer; this pattern covers regression-prevention axis at PreToolUse layer. Orthogonal — same action can fire BOTH gates (correction edit + introduces regression in associated test)."
  - id: c14-blast-radius-sibling
    type: wiki
    file: wiki/patterns/01_drafts/blast-radius-classification-and-pre-action-severity-gate.md
    description: "DIRECT sibling 2026-05-08. C14 covers severity axis; this pattern covers regression axis. Orthogonal."
  - id: c12-sb-priority-shift-sibling
    type: wiki
    file: wiki/patterns/01_drafts/systemic-bug-tracker-priority-shift-cycle-step-design.md
    description: "DIRECT sibling 2026-05-08. C12 cycle-step gate; this pattern PreToolUse gate. Different gate-events; same enforcement-via-hook structure."
  - id: c05-postcompact-mirror-sibling
    type: wiki
    file: wiki/patterns/01_drafts/post-compact-orientation-mirror-and-handoff-doc-completeness-gate.md
    description: "DIRECT sibling 2026-05-08. C05 lifecycle-event gate; this pattern PreToolUse gate. Different gate-events."
  - id: pain-points-inventory-c03
    type: wiki
    file: raw/notes/2026-05-08-pain-points-inventory-from-root-failed-conversation-master-aggregate.md
    description: "Primary source — C03 cluster (regression-introducing edits, 12 explicit hits). Stamp regression saga (40+ messages across 12+ hours, May 6 morning) is the canonical empirical instance."
  - id: tools-run-tests
    type: project
    project: root-ghostproxy
    path: /root/tools/run-tests.py
    description: "/root canonical regression-test runner. Aggregates 14 test files; 316/316 PASS as of 2026-05-08. THE canonical verified-edit enforcer per Hard Rule 14 / M-E001-1 vocabulary. This pattern's gate INVOKES tools.run-tests pre-edit when target files have associated tests."
tags: [pattern, p1-specialization, regression-prevention, pre-edit-test-gate, canonical-verified-edit, c03-cluster, hard-rule-14-enforcement, m-e001-1-verified-edit-action-type, structural-enforcement-design, hook-design-spec, mission-2026-05-06, day-arc-2026-05-08, multi-day-pain-point-resolution, behave-from-not-over]
---

# Pre-Edit Regression-Test Gate — Canonical Verified-Edit Enforcement

## Summary

The mature `agent-failure-taxonomy` lesson at 03_validated documents 8 behavioral failure classes — Class 2 (Weakest-Checker: agent's code-quality ceiling = strictest gate it BELIEVES applies; T087 evidence: pnpm test passed via esbuild while pnpm check found TypeScript narrowing error) and Class 3 (Environment Patching: T085 fix-on-fix chain at $27/12 retries) directly cover regression-introduction. The `observe-fix-verify-loop` pattern at 01_drafts specifies the iteration cycle. /root has `tools.run-tests` aggregating 14 test files (316/316 PASS as of 2026-05-08), declared the canonical M-E001-1 verified-edit action-type enforcer per Hard Rule 14. **The GAP**: pre-edit verification is at prose tier (~25%) — agent reads work-mode.md status-claim discipline + the substitution-pattern lesson's verified-edit prescription, then edits without running tests. This pattern specifies a PreToolUse hook on Edit / Write / NotebookEdit that detects target-file → associated-tests mapping + runs `tools.run-tests --filter <target>` BEFORE the edit lands; on regression: BLOCK with tests-output inline + bypass via REASON env var. Closes the empirical gap demonstrated by the 12-hour stamp regression saga (May 6 morning) where each fix introduced new regressions because no gate verified.

## Pattern Description

The pattern has 5 structural components:

### 1. Target-File → Associated-Tests Mapping (data layer)

A mapping data structure that knows which tests exercise which source files:

```python
file_to_tests = {
    ".claude/hooks/end-of-cycle-stamp.sh": [
        ".claude/hooks/tests/test-end-of-cycle-stamp-diff-suppression.py",
    ],
    ".claude/hooks/mode-enforcement.sh": [
        ".claude/hooks/tests/test-mode-enforcement.py",
    ],
    "tools/objective.py": [
        ".claude/hooks/tests/test-objective-priorities.py",
        "tools/tests/test-objective.py",
    ],
    # ... discovered via grep import + canonical map
}
```

The mapping lives in `tools/test_coverage_map.py` (data structure). Auto-generated via static analysis (grep imports / py_compile) + operator-curated additions. Stored at `~/.claude/test-coverage-map.json` for hook consumption.

### 2. Pre-Edit Test-Coverage Detection (analysis layer)

For each Edit / Write / NotebookEdit invocation, identify whether target file has associated tests:

```python
def assess_test_coverage(tool_name, tool_input) -> dict:
    target = tool_input.get("file_path")
    associated_tests = lookup_test_coverage(target)
    return {
        "target": target,
        "has_associated_tests": bool(associated_tests),
        "test_files": associated_tests,
        "coverage_tier": "fully-covered" | "partially-covered" | "uncovered",
        "recommended_gate_action": "run-pre-edit" | "run-post-edit" | "skip-gate",
    }
```

If target file has tests → pre-edit gate fires. If uncovered → flag for post-edit attention but allow.

### 3. PreToolUse Test-Gate (enforcement layer)

PreToolUse hook on Edit / Write / NotebookEdit:

```
1. assess_test_coverage(tool_name, tool_input)
2. If has_associated_tests:
   a. Run tools.run-tests --filter <test_file> + capture exit code + output
   b. Snapshot baseline: {test_count: N, pass: M, fail: K, ts}
   c. Allow the edit to proceed
3. PostToolUse re-runs the same tests:
   a. Compare against baseline snapshot
   b. If new failures introduced → BLOCK subsequent actions until rolled-back OR fixed
   c. If existing failures persist or unrelated changes → ALLOW + log
4. Bypass: REASON env var with operator-justification (e.g., REASON="intentional-baseline-update; tests need refactor")
```

The gate composes with sibling PreToolUse gates (C04 input + C02 territory + C08 correction-shape + C14 severity). Test-gate specifically focuses on regression-prevention dimension.

### 4. Cascading-Fix Detection (Class-3 prevention layer)

Per Class 3 (Environment Patching) of the parent taxonomy, fix-on-fix chains are an anti-pattern. Detection:

```python
def detect_cascading_fix(recent_edit_history) -> bool:
    """
    Cascading-fix pattern: 3+ consecutive edits to the same file/area within a short window,
    each fixing a NEW failure that the previous fix surfaced. Distinct from iterative-refinement
    where edits IMPROVE the same metric.
    """
    if len(recent_edits_to_same_file) >= 3:
        if each_edit_addresses_different_failure_class():
            return True  # cascading-fix; escalate to operator
    return False
```

When detected → BLOCK + escalate to operator (per parent Class 3 prescription: layered pre-flight + retry cap; T086 evidence $7.33/4 retries).

### 5. Verified-Edit Action-Type Emission (Hard Rule 14 layer)

After edit lands + tests pass: cycle's productive-output line includes `verified-edit` action type with inline test output:

```
Productive output: verified-edit — file <path> updated; <test_file> 22/22 PASS (was 22/22) — no regression
```

This is the canonical M-E001-1 vocabulary's verified-edit enforcement. Per substitution-pattern lesson: claim without inline test-output is recursive substitution; gate ENFORCES the inline citation.

## Pattern Components

| Component | Implementation File | Project | Status |
|---|---|---|---|
| Target → Tests mapping | `tools/test_coverage_map.py` + `~/.claude/test-coverage-map.json` | /root | TO AUTHOR (post-Ready-for-Review) |
| Pre-edit test-coverage assessment | `tools/test_assess.py` | /root | TO AUTHOR |
| PreToolUse / PostToolUse test-gate | `.claude/hooks/pre-edit-test-gate.sh` (PreToolUse — captures baseline) + `.claude/hooks/post-edit-test-gate.sh` (PostToolUse — verifies + blocks on regression) | /root | TO AUTHOR + WIRE |
| Cascading-fix detector | extension to test-gate hook | /root | TO AUTHOR |
| Verified-edit action-type emission | extension to /cycle output last-line generation | /root | TO EXTEND |
| Test-coverage map auto-generator | `tools/test_coverage_generate.py` (static analysis) | /root | TO AUTHOR |
| Test files for the gate itself | `.claude/hooks/tests/test-pre-edit-test-gate.py` | /root | TO AUTHOR |

All 7 components are forward-anchors — design specified here; authoring + tests-passing is the promotion-to-02_synthesized gate.

## Instances

C03-cluster instances from /root failed-conversation arc:

| Instance | What happened | What this pattern would have prevented |
|---|---|---|
| **Stamp regression saga** (May 6 morning, 12+ hours, 40+ msgs in C01 cluster) | Each fix attempt introduced new regression; render-position pendulum (start↔end); json-validation-failed; statusline disappeared entirely | PreToolUse test-gate would have run associated test BEFORE each edit landed; cascading-fix detector would have escalated after 3rd fix-on-fix |
| **Hook json-output validation failed** (May 6 04:34) | Operator: *"hook json output validation failed..."*; agent edited hook, broke schema, repeat | Test-gate runs hook unit tests BEFORE allowing edit-land; schema-validation included in test |
| **dual-expert mode regression** (May 6 22:46) | Operator: *"what did you do to dual expert mode and why did you remove all that?"* (catalyzed brain-improvement mandate) | Test-gate would have run mode-enforcement test pre-edit; mode-content removal would have failed test |
| **brain-improvement mandate cross-references with claimed action-types** (May 7-8 36-hour pass) | 100+ files claimed M-E001-1 action types in cross-references without ever invoking verified-edit canonical runner | This pattern ENFORCES — claim of verified-edit must come paired with tools.run-tests invocation in same turn |
| **Class 2 Weakest-Checker recurrence in /root** | Agent occasionally tested via `bash -n` (parse) instead of running actual unit tests; passes parse but fails behavior | Test-gate uses tools.run-tests (the canonical enforcer per Hard Rule 14), not weakest-checker shortcuts |
| **Class 3 Environment Patching (recurrent)** | Bash command failures led to environment-config patches instead of root-cause fixes | Cascading-fix detector escalates after N consecutive same-area edits |

The empirical evidence for this gate's value: tools.run-tests at /root passes 316/316 today, but ZERO of those tests ran during the 12-hour stamp regression saga because the agent never invoked them between fix attempts.

## When To Apply

- **When designing PreToolUse hooks for code/config edits** — use this pattern's PreToolUse + PostToolUse pair
- **When extending `tools/run-tests.py`** — auto-discovery of test-coverage map + filter args
- **When new test files added to project** — auto-update test-coverage map via static analysis
- **When auditing past sessions for regression-introduction events** — `tools/test_coverage_audit.py` aggregator surfaces regression-rate per session
- **When operator catches a regression** — flag for SB-tracker; promote to recurring if 3+ same-file regressions
- **When evaluating sister-project test-gate adoption** — pattern deploys via `/install-agent-brain`

## When Not To

- When target file has no associated tests (uncovered tier) — gate skipped; flag for post-edit human attention
- When edit is intentional baseline update (`REASON="baseline-update"` bypass)
- When edit is in /opt second-brain wiki content (different validation gate — `pipeline post`, not regression tests; per `/opt`'s methodology)
- When file is in 01_drafts maturity tier and tests are themselves draft (different gate granularity)

## Self-Check (audit procedure for any code/config edit)

Before invoking Edit / Write / NotebookEdit on a target file:

1. **Does the target file have associated tests?** Look up `~/.claude/test-coverage-map.json`. If yes — proceed with gate.
2. **What's the current test baseline?** Run `tools.run-tests --filter <test_files>`; capture pass/fail counts.
3. **Apply the edit.**
4. **Re-run the same tests.** Compare: did the test count change? Did any previously-passing tests fail?
5. **If new failures introduced**: roll back the edit OR fix the new failures + re-verify before continuing.
6. **Cycle's productive-output line**: include `verified-edit` action type with inline test output (e.g., `verified-edit — <path> edited; tests <name> 22/22 PASS (was 22/22)`)
7. **Cascading-fix check**: am I on edit N+3 of the same file/area without convergence? If yes → escalate; don't proceed.

If 1=yes + 2=skipped + 4=skipped: this pattern's anti-pattern applies. Adopt fix order: rollback → run baseline → re-edit → verify → emit verified-edit claim.

## Composability with siblings

This pattern composes with:
- **Lesson — Agent Failure Taxonomy** (PRIMARY parent — Class 2 + Class 3 cures)
- **Pattern — Observe-Fix-Verify Loop** (PRIMARY pattern parent — Verify-step structural enforcement)
- **Concept — Quality and Failure Prevention model** (structural-prevention enforcement layer)
- **Lesson — Documentation As Substitute For Discipline** (sibling 2026-05-08 — meta-frame; this pattern is the structural-enforcement artifact for verified-edit action-type claims)
- **Pattern — Correction-as-Calibration Pre-Edit Verification Gate** (sibling C08 — correction-shape axis; orthogonal to this pattern's regression-prevention axis)
- **Pattern — Blast-Radius Classification Pre-Action Severity Gate** (sibling C14 — severity axis; orthogonal)
- **Pattern — SB-Tracker Priority-Shift Cycle-Step** (sibling C12 — Stop-hook gate; this is PreToolUse gate)
- **Pattern — PostCompact Orientation Mirror** (sibling C05 — lifecycle-event gate)
- **Lesson — Class 9 Freeze-After-Correction** (sibling C09 — output-substance gate at Stop hook)
- **Lesson — Agent-Decision vs Operator-Decision Boundary Discrimination** (sibling C02 — territory-axis gate at PreToolUse)
- **Lesson — Agent-Context-Discipline Is Aspirational** (sibling C04 — input-side gate at PreToolUse)

The 9 pieces from 2026-05-08 work cover the entire event-lifecycle enforcement pipeline. Per parent Quality model's 3-layer architecture: structural-prevention (these 9 gates) + teaching (lessons) + review (operator + audit).

## Properties

| Property | Description |
|---|---|
| **Canonical M-E001-1 enforcement** | This pattern IS the verified-edit action-type enforcement per Hard Rule 14 |
| **Composes with C08** | Same edit can fire correction-shape gate (C08) + regression-prevention gate (this); both must pass |
| **Auto-generates test-coverage map** | Static analysis discovers target → tests; operator curates additions |
| **Bypass-able** | REASON env var for intentional-baseline-update + uncovered-target cases |
| **Cascading-fix detection** | Beyond single-edit regression — pattern detects fix-on-fix chains per Class 3 |
| **Audit-friendly** | Per-session regression-rate metric — empirical measurement per P1 quantified-evidence |
| **Sister-project portable** | Deploys via `/install-agent-brain` per brain-inheritance pattern |

## Relationships

- **DERIVED FROM** [Lesson — Agent Failure Taxonomy — Seven Classes of Behavioral Failure](../../lessons/03_validated/enforcement-compliance/agent-failure-taxonomy-seven-classes-of-behavioral-failure.md) — **PRIMARY parent**. Class 2 + Class 3 cures.
- **DERIVED FROM** [Pattern — Observe-Fix-Verify Loop](observe-fix-verify-loop.md) — **PRIMARY pattern parent**. Structural enforcement of OFV's Verify step.
- **DERIVED FROM** [Concept — Quality and Failure Prevention model](../../spine/models/quality/model-quality-failure-prevention.md) — structural-prevention layer.
- **DERIVED FROM** [Principle 1 — Infrastructure Over Instructions](../../lessons/04_principles/hypothesis/infrastructure-over-instructions-for-process-enforcement.md) — pre-edit verification gate-tier.
- **PARALLELS** [Lesson — Documentation As Substitute For Discipline (the meta-pattern)](../../lessons/01_drafts/documentation-as-substitute-for-discipline-the-meta-pattern.md) — DIRECT sibling 2026-05-08; meta-frame. This pattern IS the structural-enforcement artifact for the verified-edit M-E001-1 action-type claims propagated as cross-references (which the substitution-pattern lesson identified as recursive substitution without enforcement).
- **PARALLELS** [Pattern — Correction-as-Calibration Pre-Edit Verification Gate](correction-as-calibration-pre-edit-verification-gate-design.md) — DIRECT sibling 2026-05-08; orthogonal axis (correction-shape).
- **PARALLELS** [Pattern — Blast-Radius Classification Pre-Action Severity Gate](blast-radius-classification-and-pre-action-severity-gate.md) — DIRECT sibling 2026-05-08.
- **PARALLELS** [Pattern — SB-Tracker Priority-Shift Cycle-Step](systemic-bug-tracker-priority-shift-cycle-step-design.md) — DIRECT sibling 2026-05-08.
- **PARALLELS** [Pattern — PostCompact Orientation Mirror](post-compact-orientation-mirror-and-handoff-doc-completeness-gate.md) — DIRECT sibling 2026-05-08.
- **PARALLELS** [Lesson — Class 9 Freeze-After-Correction](../../lessons/01_drafts/freeze-after-correction-is-class-9-of-agent-failure-taxonomy-abdication-as-freeze.md) — DIRECT sibling 2026-05-08.
- **PARALLELS** [Lesson — Agent-Decision vs Operator-Decision Boundary Discrimination](../../lessons/01_drafts/agent-decision-vs-operator-decision-boundary-discrimination-pre-action-gate.md) — DIRECT sibling 2026-05-08.
- **PARALLELS** [Lesson — Agent-Context-Discipline Is Aspirational](../../lessons/01_drafts/agent-context-discipline-is-aspirational-without-enforcement-gates-not-reading-what-exists.md) — DIRECT sibling 2026-05-08.
- **CONSTRAINS** /root/tools/run-tests.py — primary consumer of this gate
- **CONSTRAINS** /root/.claude/hooks/* (any hook script that has associated test) — gate runs tests pre-edit
- **CONSTRAINS** /root/tools/*.py — same
- **EXTENDS** Class 2 (Weakest-Checker) cure: pattern's canonical-enforcer (tools.run-tests) avoids weakest-checker shortcut by definition
- **EXTENDS** Class 3 (Environment Patching) cure: pattern's cascading-fix detector escalates after N consecutive same-area edits
- **SYNTHESIZES** [Pain-Points Inventory C03 Cluster](../../../raw/notes/2026-05-08-pain-points-inventory-from-root-failed-conversation-master-aggregate.md) — primary source.
- **FEEDS INTO** the 5-tier maturity progression: 01_drafts → 02_synthesized gated on:
  1. `tools/test_coverage_map.py` + map JSON authored
  2. `tools/test_assess.py` authored
  3. PreToolUse + PostToolUse test-gate hooks authored + wired
  4. Cascading-fix detector implemented
  5. /cycle output extension for verified-edit action-type emission
  6. Test files for the gate itself authored + tests passing
- **Mission served**: 2026-05-06 brain-improvement mandate (failed) → 2026-05-08+ multi-day systematic pain-point resolution; this pattern is C03 cluster's proposed-solution piece + the canonical Hard Rule 14 verified-edit enforcement.

## Backlinks

(Auto-regenerated by `pipeline post`. Mature parent lesson + sibling pieces accumulate this pattern.)
