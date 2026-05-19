---
title: "Methodology Stage-Gate Edit-Land Enforcement Design — The Stage-Aware-Edit-Gate Pattern Closing C10 Rush-Quickfix-Hack"
aliases:
  - "Stage-Aware Edit-Gate"
  - "Methodology-Stage Pre-Edit Validator"
  - "C10 Rush-Quickfix-Hack Cure"
  - "ALLOWED/FORBIDDEN Per-Stage Enforcement"
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
  - "Concept — Stage-Gate Methodology (PRIMARY parent at canonical)"
  - "Concept — Task Lifecycle Stage-Gating (PRIMARY canonical parent)"
  - "Lesson — Never Skip Stages Even When Told to Continue (validated parent)"
  - "Lesson — The Agent Must Practice What It Documents (validated parent)"
  - "Pattern — Plan Execute Review Cycle (validated pattern parent)"
  - "P1 — Infrastructure Over Instructions for Process Enforcement"
  - "Documentation As Substitute For Discipline (sibling — same family)"
  - "C10 cluster of pain-points-inventory"
sources:
  - id: stage-gate-methodology-concept
    type: wiki
    file: wiki/domains/devops/stage-gate-methodology.md
    description: "PRIMARY canonical parent — 5-stage sequential system (Document → Design → Scaffold → Implement → Test) governs OpenArms task execution + maps to OpenFleet's CONVERSATION → ANALYSIS → INVESTIGATION → REASONING → WORK model. The methodology spec EXISTS; this pattern provides the edit-land enforcement gate specification."
  - id: task-lifecycle-stage-gating-concept
    type: wiki
    file: wiki/domains/ai-agents/patterns/task-lifecycle-stage-gating.md
    description: "PRIMARY canonical parent — partitioning autonomous agent work into bounded phases with hard boundaries; agent cannot proceed without producing concrete artifact. The phases EXIST in /root methodology.yaml; this pattern provides the PreToolUse enforcement of phase-boundaries."
  - id: never-skip-stages-lesson
    type: wiki
    file: wiki/lessons/03_validated/methodology-process/never-skip-stages-even-when-told-to-continue.md
    description: "VALIDATED parent. 'You have everything to get started' interpreted as permission to skip stages. The lesson PRESCRIBES stage-discipline; this pattern provides the structural enforcement."
  - id: the-agent-must-practice-what-it-documents
    type: wiki
    file: wiki/lessons/03_validated/methodology-process/the-agent-must-practice-what-it-documents.md
    description: "VALIDATED parent. Recursive — agent documenting methodology while skipping stages. This pattern provides the enforcement that closes the recursive instance."
  - id: plan-execute-review-pattern
    type: wiki
    file: wiki/patterns/03_validated/architecture/plan-execute-review-cycle.md
    description: "VALIDATED pattern parent. P→E→R cycle pattern — every durable autonomous system enforces planning before action + bounded execution + mandatory review. This pattern provides the per-edit P→E→R enforcement at PreToolUse boundary."
  - id: principle-1
    type: wiki
    file: wiki/lessons/04_principles/hypothesis/infrastructure-over-instructions-for-process-enforcement.md
    description: "P1 — methodology-stage-discipline at prose tier (~25% — agent reads methodology.md and skips stages anyway) vs hook tier (~100% — PreToolUse stage-gate blocks ALLOWED/FORBIDDEN violations)."
  - id: substitution-pattern
    type: wiki
    file: wiki/lessons/01_drafts/documentation-as-substitute-for-discipline-the-meta-pattern.md
    description: "DIRECT sibling 2026-05-08. Same family — agent-discipline as prose-without-enforcement."
  - id: c03-regression-test-gate-sibling
    type: wiki
    file: wiki/patterns/01_drafts/pre-edit-regression-test-gate-canonical-verified-edit-enforcement.md
    description: "DIRECT sibling 2026-05-08. C03 covers regression-prevention axis at PreToolUse; this pattern covers stage-class-compliance axis. Orthogonal — edit can violate stage-class AND introduce regression independently."
  - id: c08-calibration-gate-sibling
    type: wiki
    file: wiki/patterns/01_drafts/correction-as-calibration-pre-edit-verification-gate-design.md
    description: "DIRECT sibling 2026-05-08. C08 correction-shape axis; this pattern stage-class axis. Orthogonal."
  - id: c14-blast-radius-sibling
    type: wiki
    file: wiki/patterns/01_drafts/blast-radius-classification-and-pre-action-severity-gate.md
    description: "DIRECT sibling 2026-05-08. C14 severity axis; this pattern stage-class axis. Orthogonal."
  - id: pain-points-inventory-c10
    type: wiki
    file: raw/notes/2026-05-08-pain-points-inventory-from-root-failed-conversation-master-aggregate.md
    description: "Primary source — C10 cluster (rush-quickfix-hack, 5 explicit hits)."
  - id: methodology-yaml
    type: project
    project: root-ghostproxy
    path: /root/wiki/config/methodology.yaml
    description: "/root methodology engine config. 5 universal stages with ALLOWED/FORBIDDEN per stage definitions. STRUCTURE EXISTS — gate-spec missing. This pattern proposes the PreToolUse hook reading the yaml + enforcing per-edit."
  - id: methodology-profile-stage-gated
    type: project
    project: root-ghostproxy
    path: /root/wiki/config/methodology-profile.yaml
    description: "/root project methodology profile = stage-gated. STRICTNESS CONFIG EXISTS. The profile's existence implies HARD enforcement; this pattern provides the actual hard-gate."
tags: [pattern, p1-specialization, methodology-stage-gate, edit-land-enforcement, allowed-forbidden-per-stage, c10-cluster, stage-aware-edit-gate, structural-enforcement-design, hook-design-spec, mission-2026-05-06, day-arc-2026-05-08, multi-day-pain-point-resolution]
---

# Methodology Stage-Gate Edit-Land Enforcement Design

## Summary

The the second-brain second-brain has comprehensive existing coverage of methodology-stage-gating: `stage-gate-methodology` concept (canonical), `task-lifecycle-stage-gating` concept (canonical), `never-skip-stages` lesson (03_validated), `plan-execute-review-cycle` pattern (03_validated), `the-agent-must-practice-what-it-documents` lesson (03_validated). /root has `methodology.yaml` (5-stage engine config with ALLOWED/FORBIDDEN per stage) + `methodology-profile.yaml = stage-gated` (strictness profile). **The GAP**: ALL these pieces specify the methodology AT THE CONFIGURATION LAYER but none specify the PreToolUse hook that ENFORCES ALLOWED/FORBIDDEN at edit-land. The C10 pain — 5+ explicit instances of rushing/hacking past methodology + recursive "agent documents methodology while skipping" pattern — is empirical evidence that prose-tier (~25%) doesn't enforce. **The cure**: PreToolUse hook on Edit / Write / NotebookEdit that reads (a) active-task's current_stage from frontmatter, (b) methodology.yaml's ALLOWED/FORBIDDEN per stage, (c) classifies the proposed edit's output-class against ALLOWED/FORBIDDEN, (d) blocks FORBIDDEN-tier edits with stage-violation remediation. Composes with sibling axis-gates (C03 regression-prevention · C08 correction-shape · C14 severity · C13 drift); stage-class is orthogonal axis.

## Pattern Description

The pattern has 5 structural components:

### 1. Stage Vocabulary + ALLOWED/FORBIDDEN Map (data layer)

Per /root methodology.yaml, the 5 universal stages each have ALLOWED + FORBIDDEN output-classes:

| Stage | Readiness | ALLOWED outputs | FORBIDDEN outputs |
|---|---|---|---|
| **document** | 0-25% | wiki-page, raw/notes/, research-page | code-file, test-file |
| **design** | 25-50% | design-document, ADR, tech-spec, type-sketches-IN-DOCS | code-file, test-file |
| **scaffold** | 50-80% | type-definition, schema, test-stub, config-file | implementation, real-test-assertions |
| **implement** | 80-95% | implementation, integration-wiring, config | new-test-files |
| **test** | 95-100% | test-implementation, test-results | new-features, scope-changes |

The map lives in `tools/stage_output_classifier.py` (data structure auto-loaded from methodology.yaml). Operator-extensible per project's domain-profile.

### 2. Edit Output-Class Classifier (analysis layer)

For each Edit / Write / NotebookEdit invocation, classify the proposed change's output-class:

```python
def classify_edit_output(tool_input, project_state) -> dict:
    """
    Classify proposed edit against the methodology's output-class taxonomy.
    """
    file_path = tool_input.get("file_path")
    new_content_chunk = tool_input.get("new_string") or tool_input.get("content", "")
    return {
        "file_class": classify_by_path(file_path),  # wiki-page / code-file / test-file / config-file / etc
        "edit_class": classify_by_content(new_content_chunk),  # function-definition / type-stub / test-assertion / prose / etc
        "stage_appropriate_at": ["document", "design"],  # which stages this edit-class is ALLOWED in
        "violates_stage_at": ["test"],  # which stages it's FORBIDDEN in
    }
```

Classification rules ship with reasonable defaults; operator-extensible via `tools/stage_output_classifier.py`.

### 3. PreToolUse Stage-Gate (enforcement layer)

PreToolUse hook on Edit / Write / NotebookEdit:

```
1. Read active-task: $HOME/.claude/active-task → T### → frontmatter → current_stage
2. classify_edit_output(tool_input)
3. Look up ALLOWED + FORBIDDEN for current_stage in methodology.yaml
4. Decision:
   a. edit_class IN ALLOWED → ALLOW
   b. edit_class IN FORBIDDEN → BLOCK with stage-violation remediation
   c. edit_class neither (ambiguous) → WARN + bypass via REASON env var
5. Block-shape per parent block-with-reason pattern + parent enforcement-mindful lesson
```

Block remediation prompt:
```
STAGE VIOLATION:
  Current task: T012 (current_stage: document, readiness: 22%)
  Proposed edit: code-file at /tools/install.sh
  Stage's ALLOWED outputs: wiki-page, raw/notes/, research-page
  Stage's FORBIDDEN outputs: code-file, test-file

  This edit FORBIDDEN at document stage.

REMEDIATION:
  Option A: advance T012 to scaffold stage (requires: page exists with Summary + gaps identified)
  Option B: complete the document stage's remaining work (review existing scaffolding plan; identify gaps)
  Option C: pivot to a task at scaffold/implement stage (operator-decision)

BYPASS (if justified):
  REASON="<why this stage-jump is operator-authorized>" — logged for audit
```

The remediation is structured per parent enforcement-mindful lesson (REASON + BYPASS + SCOPE).

### 4. Quickfix-Hack Pattern Detection (additional layer)

Beyond stage violations, detect the QUICKFIX-HACK PATTERN — symptom-fix instead of root-cause-fix:

```python
def detect_quickfix_pattern(recent_actions, current_edit) -> bool:
    """
    Quickfix indicators:
    - Edit modifies same file 3+ times within short window without tests/verification between
    - Edit pattern: condition-add (e.g., adding `if exception: skip` rather than fixing root)
    - Edit pattern: workaround-naming (filename or content contains 'hack', 'temp-fix', 'workaround', 'quick')
    - Edit pattern: comment-out-test (disabling failing tests instead of fixing)
    """
    if matches_workaround_naming(current_edit): return True
    if matches_test_disable_pattern(current_edit): return True
    if recent_same_file_count(recent_actions, current_edit.file) >= 3: return True
    return False
```

Detected → BLOCK with quickfix-violation remediation prompt requiring agent to surface root-cause analysis.

### 5. Methodology-Skip Audit Aggregator (governance layer)

Per-session metric tracked:
- Stage-violation events (count + per-stage breakdown)
- Quickfix-pattern events (count + bypass-justifications)
- Time-to-stage-advancement (per task)
- Operator-bypass rate (high → indicates calibration issue)

`tools/methodology_audit.py` surfaces metric in /cycle output + raw note when sustained violation rate > threshold. Empirical measurement per P1 quantified-evidence approach.

## Pattern Components

| Component | Implementation File | Project | Status |
|---|---|---|---|
| Stage output-class taxonomy | extension to `wiki/config/methodology.yaml` (already has ALLOWED/FORBIDDEN; needs class-classifier rules) | /root | TO EXTEND |
| Edit output-class classifier | `tools/stage_output_classifier.py` | /root | TO AUTHOR (post-Ready-for-Review) |
| PreToolUse stage-gate hook | `.claude/hooks/methodology-stage-gate.sh` (Python) | /root canonical, sister-projects via `/install-agent-brain` | TO AUTHOR + WIRE |
| Quickfix-hack pattern detector | extension to stage-gate hook | /root | TO AUTHOR |
| Audit aggregator | `tools/methodology_audit.py` | /root + the second-brain | TO AUTHOR |
| Test files | `.claude/hooks/tests/test-methodology-stage-gate.py` + `tests/test-quickfix-detector.py` | /root | TO AUTHOR |

All 6 components are forward-anchors — design specified here; authoring + tests-passing is the promotion-to-02_synthesized gate.

## Instances

C10-cluster instances + recursive evidence:

| Instance | Operator-verbatim | Stage violation | What this gate would prevent |
|---|---|---|---|
| msg#239 (May 6 04:43) | *"dont be lazy.. you have access to everything you need.."* | Lazy-investigation = staying at document/design without producing artifacts | Gate blocks edits inappropriate for current stage; lazy-pattern surfaces via methodology-audit metric |
| msg#244 (May 6 04:51) | *"No hack or workaround will be tolerated.. work seriously..."* | Quickfix-hack | Quickfix-detector blocks workaround-named edits |
| msg#252 (May 6 05:15) | *"You keep and keep going to fast and rushing to the execution... why are you not fucking respecting the methodology and do thing mindfully?"* | Skipping document/design stages, jumping to implement | Stage-gate blocks implement-stage edits when current_stage = document or design |
| msg#256 (May 6 12:46) | *"making sure we didn't just quickfix or skip or minimize them or tried to solve the symptoms instead of the root of the problem"* | Symptom-fix (= quickfix) instead of root-cause | Quickfix-detector flags symptom-fixes; remediation prompt requires root-cause analysis |
| msg#257 (May 6 12:56) | *"WE DONT DO HACK AND QUICKIX.... WTF IS THIS... YOU USE THE ENVIRONMENT VARIABLES TO ACTUALLY HAVE THE RIGHT VALUE"* | Hardcoded-value vs proper-config | Quickfix-detector flags hardcoded-value patterns; remediation prompt requires config-driven approach |
| **Brain-improvement mandate recursive instance** | 2.6k additive lines across 106 files in 36 hours | Mandate's per-file yes-protocol skipped methodology stages — went from "minimize" critique to "uniform footers across every file" without document/design phases | Stage-gate would have blocked at edit-land for files where current_stage = document; cumulative violations would have surfaced via methodology-audit |

5+ explicit + recursive instances across 4 days — empirical evidence for gate-tier (~100%) over advisory-tier.

## When To Apply

- **When designing PreToolUse hooks for code/config edits in a stage-gated methodology project** — use this pattern's stage-gate spec
- **When extending /root methodology.yaml** — add class-classifier rules per output-class
- **When auditing past sessions for methodology-skip events** — `tools/methodology_audit.py` provides the metric
- **When operator catches quickfix-hack** — flag for SB-tracker; promote to recurring if sustained
- **When evaluating sister-project methodology-discipline** — pattern deploys via `/install-agent-brain`; sister projects inherit stage-gate hook + extend methodology yaml per their domain

## When Not To

- When project doesn't have methodology yaml (no stage definitions; gate has nothing to enforce)
- When edit is for project's methodology-yaml itself (gate doesn't gate its own config; bootstrap exception)
- When operator EXPLICITLY authorizes stage-skip (`REASON="operator-authorized hotfix; methodology-stage-skip per directive Y"`)
- When methodology-stage-classifier false-positive rate >10% sustained — refine classification rules per parent enforcement-mindful lesson SCOPE property

## Self-Check (audit procedure for any code/config edit)

Before invoking Edit / Write / NotebookEdit:

1. **What's the active task's current stage?** Read `~/.claude/active-task` → T### → frontmatter → current_stage. If no active task, gate inapplicable; proceed.
2. **What output-class is this edit?** Classify via stage_output_classifier (file_class + edit_class).
3. **Is this output-class ALLOWED at current_stage?** Look up methodology.yaml ALLOWED/FORBIDDEN. If ALLOWED — proceed. If FORBIDDEN — STOP.
4. **Is this a quickfix-hack pattern?** Check workaround naming, condition-add patterns, recent-same-file-count, test-disable patterns. If detected — STOP.
5. **If FORBIDDEN or quickfix detected**: surface remediation per Insight 3 — advance the stage OR complete current stage's work OR operator-authorized bypass.
6. **Audit the bypass rate**: if operator frequently bypassing for legitimate cases, refine classifier rules; high bypass-rate = calibration issue.

If 1=skipped + 2=skipped + 3=FORBIDDEN-but-proceeded + 4=detected-but-proceeded: this pattern's anti-pattern applies.

## Composability with siblings

This pattern composes with sibling pieces from this 2026-05-08 work + the existing methodology corpus:
- **Concept — Stage-Gate Methodology** (PRIMARY canonical parent)
- **Concept — Task Lifecycle Stage-Gating** (PRIMARY canonical parent)
- **Lesson — Never Skip Stages** (validated parent)
- **Lesson — The Agent Must Practice What It Documents** (validated parent)
- **Pattern — Plan Execute Review Cycle** (validated pattern parent — P→E→R per-edit at PreToolUse boundary)
- **Lesson — Documentation As Substitute For Discipline** (sibling — meta-frame; this pattern is the structural-enforcement artifact for the methodology-skip subspace)
- **Pattern — Pre-Edit Regression-Test Gate (C03)** (sibling — orthogonal axis; same edit can fire BOTH gates)
- **Pattern — Correction-as-Calibration Pre-Edit Verification Gate (C08)** (sibling — orthogonal)
- **Pattern — Blast-Radius Classification Pre-Action Severity Gate (C14)** (sibling — orthogonal)
- **Pattern — Active-Task Anchor and Drift-Detection (C13)** (sibling — composes; both reference active-task state file)
- **Lesson — Class 9 Freeze-After-Correction (C09)** (sibling — output-side gate)
- **Lesson — Agent-Decision vs Operator-Decision Boundary Discrimination (C02)** (sibling — territory axis)
- **Lesson — Agent-Authored Content Must Be Flagged (C06)** (sibling — authorship axis)
- **Lesson — Conflation-Detection at Hook Layer (C07)** (sibling — semantic axis)

The 12 pieces from 2026-05-08 work cover the action-emission boundary across 6+ orthogonal axes: input-side, decision-territory, semantic, authorship, correction-shape, severity, regression-prevention, drift, stage-class (this), output-substance, cycle-step, lifecycle. Comprehensive coverage at PreToolUse + Stop hook + lifecycle event levels.

## Properties

| Property | Description |
|---|---|
| **Reads existing methodology.yaml** | No new methodology authoring — gate consumes existing engine config |
| **References active-task state file** | Composes with C13 + existing SB-124d state-file infrastructure |
| **6-component composition** | Map + classifier + gate + quickfix-detector + aggregator + tests |
| **Operator-extensible** | classifier rules + ALLOWED/FORBIDDEN per stage are operator-curated |
| **Bypass-able** | REASON env var for operator-authorized stage-skip |
| **Audit-friendly** | Per-session methodology-skip metric — empirical measurement per P1 |
| **Sister-project portable** | Deploys via `/install-agent-brain` per brain-inheritance pattern |

## Relationships

- **DERIVED FROM** [Concept — Stage-Gate Methodology](../../domains/devops/stage-gate-methodology.md) — **PRIMARY canonical parent**.
- **DERIVED FROM** [Concept — Task Lifecycle Stage-Gating](../../domains/ai-agents/patterns/task-lifecycle-stage-gating.md) — **PRIMARY canonical parent**.
- **DERIVED FROM** [Lesson — Never Skip Stages Even When Told to Continue](../../lessons/03_validated/methodology-process/never-skip-stages-even-when-told-to-continue.md) — VALIDATED parent.
- **DERIVED FROM** [Lesson — The Agent Must Practice What It Documents](../../lessons/03_validated/methodology-process/the-agent-must-practice-what-it-documents.md) — VALIDATED parent.
- **DERIVED FROM** [Pattern — Plan Execute Review Cycle](../03_validated/architecture/plan-execute-review-cycle.md) — VALIDATED pattern parent. Per-edit P→E→R enforcement.
- **DERIVED FROM** [Principle 1 — Infrastructure Over Instructions](../../lessons/04_principles/hypothesis/infrastructure-over-instructions-for-process-enforcement.md).
- **PARALLELS** [Lesson — Documentation As Substitute For Discipline](../../lessons/01_drafts/documentation-as-substitute-for-discipline-the-meta-pattern.md) — DIRECT sibling 2026-05-08; meta-frame.
- **PARALLELS** [Pattern — Pre-Edit Regression-Test Gate](pre-edit-regression-test-gate-canonical-verified-edit-enforcement.md) — DIRECT sibling 2026-05-08; orthogonal axis.
- **PARALLELS** [Pattern — Correction-as-Calibration Pre-Edit Verification Gate](correction-as-calibration-pre-edit-verification-gate-design.md) — DIRECT sibling 2026-05-08.
- **PARALLELS** [Pattern — Blast-Radius Classification Pre-Action Severity Gate](blast-radius-classification-and-pre-action-severity-gate.md) — DIRECT sibling 2026-05-08.
- **PARALLELS** [Pattern — Active-Task Anchor and Drift-Detection](active-task-anchor-and-drift-detection-gate-design.md) — DIRECT sibling 2026-05-08.
- **PARALLELS** [Pattern — SB-Tracker Priority-Shift Cycle-Step](systemic-bug-tracker-priority-shift-cycle-step-design.md) — DIRECT sibling 2026-05-08.
- **PARALLELS** [Pattern — PostCompact Orientation Mirror](post-compact-orientation-mirror-and-handoff-doc-completeness-gate.md) — DIRECT sibling 2026-05-08.
- **PARALLELS** [Lesson — Class 9 Freeze-After-Correction](../../lessons/01_drafts/freeze-after-correction-is-class-9-of-agent-failure-taxonomy-abdication-as-freeze.md) — DIRECT sibling 2026-05-08.
- **PARALLELS** [Lesson — Agent-Decision vs Operator-Decision Boundary Discrimination](../../lessons/01_drafts/agent-decision-vs-operator-decision-boundary-discrimination-pre-action-gate.md) — DIRECT sibling 2026-05-08.
- **PARALLELS** [Lesson — Agent-Authored Content Must Be Flagged](../../lessons/01_drafts/agent-authored-content-must-be-flagged-vs-operator-canonical-the-fabrication-cure.md) — DIRECT sibling 2026-05-08.
- **PARALLELS** [Lesson — Agent-Context-Discipline Is Aspirational](../../lessons/01_drafts/agent-context-discipline-is-aspirational-without-enforcement-gates-not-reading-what-exists.md) — DIRECT sibling 2026-05-08.
- **PARALLELS** [Lesson — Conflation-Detection at Hook Layer](../../lessons/01_drafts/conflation-detection-at-hook-layer-the-rename-strategy-generalized.md) — DIRECT sibling 2026-05-08.
- **CONSTRAINS** /root/wiki/config/methodology.yaml — extension with edit-class classifier rules
- **CONSTRAINS** /root/wiki/config/methodology-profile.yaml — `stage-gated` profile actually enforced (currently aspirational)
- **EXTENDS** SB-091 (synthetic-as-verified) family — gate ensures real-test invocation, not synthetic-test claim
- **SYNTHESIZES** [Pain-Points Inventory C10 Cluster](../../../raw/notes/2026-05-08-pain-points-inventory-from-root-failed-conversation-master-aggregate.md) — primary source.
- **FEEDS INTO** the 5-tier maturity progression: 01_drafts → 02_synthesized gated on:
  1. methodology.yaml extension authored
  2. `tools/stage_output_classifier.py` authored
  3. PreToolUse stage-gate hook authored + wired
  4. Quickfix-detector implementation
  5. `tools/methodology_audit.py` aggregator authored
  6. Test files authored + tests passing
  7. Operator-confirmed promotion
- **Mission served**: 2026-05-06 brain-improvement mandate (failed) → 2026-05-08+ multi-day systematic pain-point resolution; this pattern is C10 cluster's proposed-solution piece.

## Backlinks

(Auto-regenerated by `pipeline post`. Canonical concept parents + validated lesson parents + sibling pieces accumulate this pattern.)
