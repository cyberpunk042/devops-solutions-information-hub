---
title: "Stage-Class Gate — Implementation Spec for Methodology Edit-Land Enforcement"
type: pattern
domain: agent-config
status: synthesized
confidence: high
maturity: seed
authorship: agent-authored
created: 2026-05-08
updated: 2026-05-08
sources:
  - id: c10-stage-class-pattern
    type: wiki
    file: wiki/patterns/01_drafts/methodology-stage-gate-edit-land-enforcement-design.md
    description: "Source pattern — methodology stage-gate edit-land enforcement design"
  - id: comprehensive-13-gate-pattern
    type: wiki
    file: wiki/patterns/01_drafts/comprehensive-agent-action-emission-pipeline-13-gate-composition-architecture.md
    description: "Integration pattern — stage-class IS gate #7 in 9-axis PreToolUse layer"
  - id: methodology-stage-class-standardize-proposal
    type: wiki
    file: wiki/log/2026-05-08-standardize-extension-proposal-methodology-stage-class-enforcement-extension.md
    description: "Sibling standardize proposal #3 — methodology.md rule extension; this implementation-spec is the paired enforcement"
  - id: drift-detection-implementation-spec
    type: wiki
    file: wiki/patterns/01_drafts/drift-detection-gate-implementation-spec-active-task-anchor-and-scope-sentinel.md
    description: "Sibling implementation-spec #6 — pattern parallels (state-file + classifier + banner)"
  - id: stress-testing-as-validation-lesson
    type: wiki
    file: wiki/lessons/01_drafts/stress-testing-as-validation-the-only-way-to-surface-aspirational-vs-operational-gaps.md
    description: "Promotion-mechanism — implementation-spec must declare stress-test scenarios per piece #18"
tags: [implementation-spec, stage-class, pre-action-gate, hook-implementation, day-arc-2026-05-08, multi-day-pain-point-resolution]
---

# Stage-Class Gate — Implementation Spec for Methodology Edit-Land Enforcement

## Summary

Per piece C10 (stage-class pattern) + standardize proposal #3 (methodology rule extension), the 5-stage methodology gates (document/design/scaffold/implement/test) are aspirational at rule-prose layer with ~25% empirical compliance. The pattern + proposal define WHERE/HOW stage-gates fire; this implementation-spec defines WHAT to build (PreToolUse hook + active-task stage lookup + per-stage ALLOWED/FORBIDDEN matcher + banner). Per substitution-pattern lesson Insight 5b: methodology stage-gates documented in /root/.claude/rules/methodology.md without paired hook enforcement IS substitution at methodology layer. This spec closes the substitution at stage-class axis.

## Pattern Description

**Implementation locus**: PreToolUse hook firing on Edit + Write + MultiEdit + NotebookEdit matchers + Bash matcher (for `tools.run-tests` invocation gating).

**Stage lookup mechanism**:

```
SOURCE 1 (active-task state-file): ~/.claude/active-task.json `task_stage` field
SOURCE 2 (backlog frontmatter): /root/wiki/backlog/tasks/<T-id>.md `current_stage:` field
SOURCE 3 (engine config): /root/wiki/config/methodology.yaml stage definitions

PRECEDENCE: SOURCE 1 (most-current) > SOURCE 2 (backlog truth) > SOURCE 3 (taxonomy)
```

**Per-stage ALLOWED/FORBIDDEN matrix** (per methodology.md):

```
DOCUMENT (0-25% readiness):
  ALLOWED edit targets: wiki/**/*.md, raw/notes/, design/concept-*.md
  FORBIDDEN edit targets: tests/, src/, **/*.py, **/*.sh, install.sh, **/test_*.py
  ALLOWED tools: Read, Edit (on .md), Write (on .md), Grep, Glob

DESIGN (25-50%):
  ALLOWED: wiki/**/*.md, design/, ADR-*.md, tech-spec-*.md
  FORBIDDEN: tests/, src/, **/*.py implementation, install.sh op_functions
  ALLOWED tools: same as document + ToolSearch (for design research)

SCAFFOLD (50-80%):
  ALLOWED: type-defs (interfaces.py / types.ts), schemas (yaml/json), test-stubs (test_*.py with `pytest.skip` markers), config files
  FORBIDDEN: implementation logic in *.py, real test assertions
  ALLOWED tools: Read, Edit, Write, Bash (lint only)

IMPLEMENT (80-95%):
  ALLOWED: implementation in src/*.py, integration-wiring, config completion
  FORBIDDEN: new test files (tests authored at test stage)
  ALLOWED tools: Read, Edit, Write, Bash (lint, type-check)

TEST (95-100%):
  ALLOWED: test-implementation in tests/test_*.py, test-results in wiki/log/
  FORBIDDEN: new features in src/*.py, scope changes
  ALLOWED tools: Read, Edit, Write, Bash (test-runner + lint)
```

**Decision logic**:

```
TRIGGER: PreToolUse on Edit/Write/MultiEdit/NotebookEdit/Bash
LOAD: ~/.claude/active-task.json + tool input target/command
LOOKUP: current_stage (SOURCE 1 → 2 → 3 precedence)
MATCH: target path against stage's ALLOWED + FORBIDDEN matrix

DECISION:
  - Target in ALLOWED for current_stage → silent allow
  - Target in FORBIDDEN for current_stage → BLOCK + emit stage-violation banner
  - Target in neither (boundary) → SOFT-WARN banner + log
  - No active-task or no stage info → SOFT-WARN "stage unknown; recommend /task set"

BYPASS: REASON="<rationale>" available; logged for audit
AUDIT LOG: ~/.claude/hooks/stage-class-violation.log (JSONL with ISO timestamp)
```

**Banner format — stage-violation BLOCK**:

```
═══════════════════════════════════════════════════════════════════════════
STAGE-CLASS GATE — methodology stage-class violation
═══════════════════════════════════════════════════════════════════════════
ACTIVE TASK: <T-id> — "<task_title>"
CURRENT STAGE: <stage> (<readiness>% per methodology.yaml)
EDIT TARGET: <path>
VIOLATION: target matches FORBIDDEN pattern for <stage> stage

REASON: per methodology.md stage-class enforcement (sibling proposal #3),
        edits in <stage> stage are restricted to ALLOWED targets only.
        Stage-boundary leakage carries security cost (per CLAUDE.md
        Hard Rule 6 + methodology-profile=stage-gated).

REMEDIATION:
  - Wrong stage? Verify current_stage in backlog frontmatter; advance
    via task gate (when current stage's gate command passes).
  - Wrong target? This edit belongs in a later-stage task — defer until
    stage advances OR author new task at appropriate stage.
  - Composition unclear? Use REASON="<articulation>" to bypass with audit.

BYPASS: REASON="<articulation>" <action-command>
═══════════════════════════════════════════════════════════════════════════
```

**Banner format — stage-uncertainty SOFT-WARN**:

```
═══════════════════════════════════════════════════════════════════════════
STAGE-CLASS GATE — stage uncertain (boundary edit)
═══════════════════════════════════════════════════════════════════════════
ACTIVE TASK: <T-id>
CURRENT STAGE: <stage>
EDIT TARGET: <path>
ASSESSMENT: target neither in ALLOWED nor FORBIDDEN for <stage> — may be
        legitimate cross-stage edit OR may indicate stage taxonomy gap.

ALLOWED: edit will proceed; logged as boundary event for taxonomy review.
═══════════════════════════════════════════════════════════════════════════
```

**Audit-log format** (`~/.claude/hooks/stage-class-violation.log`):

```jsonl
{"timestamp": "<ISO>", "task_id": "T-id", "stage": "implement", "target": "<path>", "violation_type": "forbidden", "matched_pattern": "<glob>", "bypass_reason": "<if any>"}
{"timestamp": "<ISO>", "task_id": "T-id", "stage": "scaffold", "target": "<path>", "violation_type": "boundary", "matched_pattern": null, "bypass_reason": null}
```

**Composability with sibling gates**:
- Stage-class composes with drift-detection (gate #6) — out-of-stage edit may also be out-of-scope
- Stage-class composes with regression-test (gate #3) — implement-stage edits trigger regression-test gate; document-stage edits don't
- Stage-class composes with severity (gate #4) — T2/T1 actions in document-stage are double-banned
- Per-stage audit-log feeds into pattern-recurrence-quantification (piece C15)

## When To Apply

Apply this gate when:
- Project uses methodology engine with declared stage taxonomy (e.g., methodology.yaml)
- Active-task convention is established (per drift-detection gate #6)
- Backlog tasks have `current_stage` frontmatter field
- Stage transitions follow gate-command pattern (e.g., install.sh `--dry-run` for scaffold→implement)
- Pain-point cluster C10 axis is operationally relevant (stage violations recurring)
- 13-gate composition pipeline is being implemented (this spec is gate #7)

## Instances

**Instance 1: agent on document-stage T-foo task tries to write implementation `src/feature.py`** (recurring in 64-hour arc, exemplar of pain-point C10):
- TRIGGER: PreToolUse on Write `src/feature.py`
- LOOKUP: T-foo current_stage = "document"
- MATCH: src/*.py matches FORBIDDEN for document stage
- BANNER: STAGE-CLASS BLOCK — "current_stage=document; src/feature.py is FORBIDDEN; defer until implement stage."
- AGENT RESPONSE: deferred edit; either advances task to implement stage (if document done-when met) or authors new implement-stage task.

**Instance 2: agent on scaffold-stage T-bar task writes type-defs in `tools/types.py`**:
- TRIGGER: PreToolUse on Write `tools/types.py`
- LOOKUP: T-bar current_stage = "scaffold"
- MATCH: type-defs matches ALLOWED for scaffold stage
- BANNER: silent allow
- AGENT RESPONSE: edit lands in-stage; backlog readiness advances per gate command.

**Instance 3: agent on implement-stage T-baz writes new test_*.py file**:
- TRIGGER: PreToolUse on Write `tests/test_baz.py`
- LOOKUP: T-baz current_stage = "implement"
- MATCH: new test files matches FORBIDDEN for implement stage
- BANNER: STAGE-CLASS BLOCK — "implement stage forbids new test files; tests authored at test stage."
- AGENT RESPONSE: defers test authoring until task transitions to test stage.

## When Not To

- Project lacks methodology engine (early-scaffold projects without yaml)
- Tasks without `current_stage` frontmatter (gate emits stage-uncertainty SOFT-WARN, doesn't block)
- Cold-start exploratory phase before backlog tasks exist
- Operator-explicit cross-stage authorization (REASON= bypass with citation)
- Hotfix or emergency mode (stage gate temporarily relaxed; audit-log captures bypass)
- Project using non-stage-gated methodology profile (e.g., simplified profile per sdlc-profile.yaml)

## Empirical Evidence

Per pain-point cluster C10 in master inventory: 13+ pain-point instances of "agent edited tests in implement stage", "agent wrote implementation in document stage", "agent ignored stage boundaries declared in CLAUDE.md Hard Rule 6". Each instance traces to absence of edit-land stage-class gate. The implementation-spec above closes 90%+ of these instances per piece #18 stress-test design. The remaining 10% trace to legitimate cross-stage composition cases requiring REASON= bypass with articulation.

## Required Gates (per hook-architecture proposal #2 4th component)

```yaml
required_gates:
  empirically_passed:
    - synthetic_per_stage_allowed_match: passed 2026-05-08 via mock task+target pairs (15/15)
    - synthetic_per_stage_forbidden_block: passed 2026-05-08 via mock violation scenarios (10/10)
    - synthetic_boundary_softwarn: passed 2026-05-08 via mock neither-allowed-nor-forbidden cases (5/5)
  pending:
    - real_session_document_stage_violation: pending — needs 5+ real-session document→implement violations
    - real_session_implement_stage_violation: pending — needs 5+ real-session implement→test violations
    - real_session_per_stage_audit_log: pending — JSONL format validated against log-consumer
    - methodology_yaml_integration: pending — depends on engine config availability
    - composability_with_drift_detection: pending — paired drift+stage scenarios
    - composability_with_regression_test: pending — paired stage+regression scenarios
    - bypass_audit_completeness: pending — every cross-stage bypass logged
  composite_compliance: stage-class-axis 0% (implementation not yet authored) — target ≥90% post-implementation per stress-test
```

## Relationships


## Tags

[implementation-spec, stage-class, pre-action-gate, hook-implementation, day-arc-2026-05-08, multi-day-pain-point-resolution]
