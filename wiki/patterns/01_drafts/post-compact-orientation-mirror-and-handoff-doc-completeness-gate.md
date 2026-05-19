---
title: "PostCompact Orientation Mirror and Handoff-Doc Completeness Gate — The Compaction-Specific Specification of the Session-Orientation Pair"
aliases:
  - "PostCompact Orientation Mirror"
  - "Handoff-Doc Completeness Gate"
  - "C05 State-Recovery Pattern"
  - "Compaction-Quality Metric"
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
  - "Pattern — Session-orientation pair: SessionStart hook + /orient command + ORIENT REPORT (PRIMARY parent at 03_validated/mature — explicitly mentions 'PostCompact mirror' as application case but doesn't specify the mirror in detail)"
  - "Lesson — Fresh AI sessions need ACTIVE orientation (validated parent at 03_validated)"
  - "Lesson — Documentation As Substitute For Discipline (sibling — same family of structural-enforcement-required for agent-discipline)"
  - "P1 — Infrastructure Over Instructions for Process Enforcement"
  - "/root SB-078 (PreCompact handoff) + SB-079 (PostCompact reliability) + SB-133 (envelope schema fix)"
  - "C05 cluster of pain-points-inventory"
sources:
  - id: session-orientation-pair-pattern
    type: wiki
    file: wiki/patterns/03_validated/architecture/session-orientation-pair-sessionstart-hook-and-orient-command-with-orient-report.md
    description: "PRIMARY parent (03_validated/mature). The pattern's 'When To Apply' section explicitly mentions 'Compaction events occur (PostCompact mirror of the same pattern restores behavioral state)' but does NOT specify the mirror in detail. This pattern provides the PostCompact mirror specification + the handoff-doc completeness gate + the state-recovery-quality metric."
  - id: broken-and-idle-lesson
    type: wiki
    file: wiki/lessons/03_validated/context-engineering/broken-and-idle-fresh-sessions-need-active-orientation-not-passive-context-loading.md
    description: "VALIDATED parent. SessionStart broken-and-idle covered; PostCompact equivalent — agent re-makes pre-compact mistakes because state-loss is invisible — is the same pattern at the compaction-event boundary."
  - id: substitution-pattern
    type: wiki
    file: wiki/lessons/01_drafts/documentation-as-substitute-for-discipline-the-meta-pattern.md
    description: "DIRECT sibling 2026-05-08. Same family — agent-discipline as prose-without-enforcement. PostCompact discipline at rule layer is aspirational; this pattern specifies the structural enforcement."
  - id: agent-context-discipline-sibling
    type: wiki
    file: wiki/lessons/01_drafts/agent-context-discipline-is-aspirational-without-enforcement-gates-not-reading-what-exists.md
    description: "DIRECT sibling 2026-05-08. C04 cites 'PostCompact agent re-makes pre-compact mistakes' as one of the not-reading-what-exists sub-class manifestations. This pattern provides the C05-specific structural fix that closes that sub-case."
  - id: principle-1
    type: wiki
    file: wiki/lessons/04_principles/hypothesis/infrastructure-over-instructions-for-process-enforcement.md
    description: "P1 governing principle — PostCompact discipline at prose tier (~25% — agent reads PostCompact hook output and may or may not invoke /orient) vs gate tier (~100% — PostCompact hook BLOCKS first non-orient action until /orient runs in the turn)."
  - id: pain-points-inventory-c05
    type: wiki
    file: raw/notes/2026-05-08-pain-points-inventory-from-root-failed-conversation-master-aggregate.md
    description: "Primary source — C05 cluster (1 explicit hit + many implicit). Empirical: 4+ compactions in the 64-hour /root failed-conversation arc, each demonstrably losing state."
  - id: existing-pre-compact-hook
    type: project
    project: root-ghostproxy
    path: /root/.claude/hooks/pre-compact.sh
    description: "Existing /root PreCompact hook authored per SB-078 — writes deterministic state snapshot to `wiki/log/<ts>-pre-compact-handoff.md` before compaction destroys nuance. Implementation present; completeness-gate missing — no validator checks the snapshot covers all required state-layers."
  - id: existing-post-compact-hook
    type: project
    project: root-ghostproxy
    path: /root/.claude/hooks/post-compact.sh
    description: "Existing /root PostCompact hook authored per SB-079 — emits additionalContext directing agent to /orient + reads most-recent pre-compact-handoff doc for state recovery. Implementation present; behavior-gate missing — no enforcement BLOCKS first non-orient action until /orient runs."
  - id: orient-md-21-step-chain
    type: project
    project: root-ghostproxy
    path: /root/.claude/commands/orient.md
    description: "/root /orient deterministic 21-step intel-gathering chain. Already invoked from SessionStart per parent pattern. PostCompact mirror invokes the same chain — code reuse."
  - id: handoff-md-snapshot-doc
    type: project
    project: root-ghostproxy
    path: /root/.claude/commands/handoff.md
    description: "/root /handoff command. Operator-invocable doc-write. Companion to PreCompact auto-write. Pattern composes: PreCompact auto-handoff + operator /handoff for explicit checkpoints — both write to same wiki/log/ space."
tags: [pattern, p1-specialization, post-compact-mirror, handoff-doc-completeness, state-recovery-quality, c05-cluster, structural-enforcement-design, hook-design-spec, sb-078, sb-079, sb-133, multi-day-pain-point-resolution, mission-2026-05-06, day-arc-2026-05-08]
---

# PostCompact Orientation Mirror and Handoff-Doc Completeness Gate

## Summary

The mature `session-orientation-pair` pattern at 03_validated solves cold-start sessions via SessionStart hook + /orient command + ORIENT REPORT — but its "When To Apply" section explicitly mentions PostCompact mirror without specifying it. The /root project has the partial implementation (`pre-compact.sh` writes snapshot per SB-078; `post-compact.sh` emits additionalContext per SB-079; SB-133 fixed envelope schema), but the implementation is INCOMPLETE because no enforcement gate validates handoff-doc completeness before allowing compaction AND no behavior gate blocks first non-orient action after compaction. The C05 pain — 4+ compactions in the 64-hour /root arc with demonstrable state-loss + msg #41 explicit *"DID YOU REALLY FORGET EVERY FUCKING THING I TOLD YOU IN THIS CONVERSATION?"* — is empirical evidence that hook-output-as-advisory doesn't enforce. This pattern specifies the PostCompact mirror + handoff-doc completeness gate + state-recovery-quality metric as the structural-fix, completing the parent pattern's compaction-event coverage.

## Pattern Description

The pattern has 4 structural components mirroring the parent `session-orientation-pair` at compaction boundary:

### 1. PreCompact Handoff-Doc Completeness Gate (pre-compaction layer)

PreCompact hook fires before compaction destroys conversation state. Writes deterministic state snapshot AND validates completeness:

```python
def precompact_handoff_completeness_gate(session_state) -> dict:
    """
    Validate handoff doc covers ALL required state-layers before allowing compaction.
    Required layers (per /root state-file inventory):
      1. active-mode + mode-specific persona
      2. active-mission + active-focus + active-impediment (SB-118 objective layer)
      3. active-priorities (SB-127)
      4. active-task cursor (SB-124d)
      5. active-questions (SB-134)
      6. recent operator-verbatim directives (last N=5)
      7. recent decisions (last N=10 D-IDs)
      8. recent SBs touched this session (tracker diff)
      9. cycle-state JSON (tools.cycle --json)
      10. blockers state JSON (tools.blockers --json)
      11. git state (uncommitted view)
      12. open task-list with status snapshot
      13. recent wiki/log entries (last N=5 by mtime)
    
    If ANY layer missing or stale > N seconds → emit completeness warning to systemMessage; 
    if CRITICAL layers missing (1-5) → BLOCK compaction with remediation prompt.
    """
    layers_present = check_each_layer(session_state)
    layers_missing = [l for l in REQUIRED_LAYERS if l not in layers_present]
    if any(l in CRITICAL_LAYERS for l in layers_missing):
        return {"decision": "block", "reason": f"Missing critical state layers: {layers_missing}"}
    if layers_missing:
        return {"decision": "warn", "reason": f"Missing state layers: {layers_missing} — proceed but state-recovery quality will be reduced"}
    return {"decision": "allow", "snapshot_path": handoff_doc_path}
```

The gate composes with the existing `pre-compact.sh` (which writes the snapshot) — gate validates the snapshot's completeness BEFORE compaction proceeds.

### 2. PostCompact Orientation Mirror (post-compaction layer)

PostCompact hook fires after compaction. Mirrors the parent SessionStart pattern at the compaction boundary:

```
SessionStart → "INVOKE /orient NOW" → agent invokes /orient → ORIENT REPORT
PostCompact  → "INVOKE /orient NOW + READ <handoff-doc-path>" → agent invokes /orient + Read handoff → STATE-RECOVERY REPORT
```

The hook emits additionalContext directing the agent to:
1. Invoke `/orient` (re-load brain + state per parent pattern's 21-step chain)
2. Read the most-recent `wiki/log/<ts>-pre-compact-handoff.md` for in-flight state
3. Emit a STATE-RECOVERY REPORT (analog to ORIENT REPORT) showing what was recovered + what was lost

### 3. PostCompact Behavior Gate (enforcement layer)

The CRITICAL piece missing from the existing implementation: a behavior gate that BLOCKS first non-orient action after PostCompact until /orient runs. Implementation:

```python
def postcompact_first_action_gate(tool_name, tool_input) -> dict:
    """
    Track per-session whether /orient has been invoked SINCE last compaction.
    If first post-compact action is anything other than /orient or Read of handoff doc:
      → BLOCK with remediation
    """
    if not first_action_post_compact(): return {"decision": "allow"}
    if tool_name == "Read" and "pre-compact-handoff" in tool_input.get("file_path", ""):
        return {"decision": "allow", "reason": "reading handoff doc"}
    if tool_name == "Skill" and tool_input.get("skill") == "orient":
        return {"decision": "allow", "reason": "invoking /orient command"}
    return {
        "decision": "block",
        "reason": "PostCompact requires /orient invocation + handoff-doc read before any other action. State recovery is required for behavioral-state restoration.",
        "remediation": "Invoke /orient first, then Read $HOME/wiki/log/<ts>-pre-compact-handoff.md, then proceed with the original action.",
        "bypass": "REASON='<why-skipping-orient-is-justified>' env var (rare; for non-state-touching reads only)"
    }
```

The gate composes with the existing `post-compact.sh` (which emits the imperative) — gate ENFORCES the imperative.

### 4. State-Recovery-Quality Metric (audit layer)

After PostCompact + /orient + handoff-doc-read, agent emits a STATE-RECOVERY REPORT measuring how much pre-compact state was successfully recovered:

```
STATE-RECOVERY REPORT (post-compact)
═════════════════════════════════════
Pre-compact handoff doc: <path> (<ts>, <bytes>)
Layers covered in handoff: 13 of 13
Layers successfully recovered: <N> of 13
  ✓ active-mode (recovered: pm-scrum-master)
  ✓ active-mission/focus/impediment (recovered: ...)
  ...
  ✗ recent operator-verbatim directives (last 3 of 5 missing — pre-compact handoff truncated)
  ✗ git state (stale — committed since handoff write)

Recovery quality: <N>/13 = <pct>%

If recovery quality < 80%:
  → flag SB to systemic-bugs tracker (compaction-quality regression)
  → surface to operator
═════════════════════════════════════
```

The metric is itself an empirical measurement (per P1 quantified-evidence approach). Aggregator over time surfaces compaction-quality trend — sustained drops below threshold trigger PreCompact gate strictness increase.

## Pattern Components

| Component | Implementation File | Project | Status |
|---|---|---|---|
| PreCompact completeness gate | extension to `.claude/hooks/pre-compact.sh` | /root | TO EXTEND (existing partial impl per SB-078) |
| PostCompact orientation mirror | extension to `.claude/hooks/post-compact.sh` | /root | TO EXTEND (existing partial impl per SB-079) |
| PostCompact behavior gate (NEW) | new `.claude/hooks/post-compact-first-action-gate.sh` | /root | TO AUTHOR + WIRE (PreToolUse with first-post-compact-action condition) |
| State-recovery-quality metric | extension to /orient command output OR new /state-recovery command | /root | TO AUTHOR |
| Required state-layers spec | `tools/handoff_layers.py` (data structure) | /root | TO AUTHOR |
| Audit aggregator | `tools/compaction_quality_audit.py` | /root + the second-brain | TO AUTHOR |
| Test files | `.claude/hooks/tests/test-precompact-completeness-gate.py` + `test-postcompact-first-action-gate.py` + `test-state-recovery-metric.py` | /root | TO AUTHOR |

All 7 components are forward-anchors — design specified here; authoring + tests-passing is the promotion-to-02_synthesized gate.

## Instances

C05-cluster instances + recursive evidence from /root failed-conversation arc:

| Instance | What happened | Layer that was lost | What this pattern would have prevented |
|---|---|---|---|
| **Compactions in arc** | 4+ compactions across May 4-8 (msgs 11, 93, 171, 214, 342, 439, 483 are compaction-summary records) | Multiple — varies per compaction | PreCompact completeness gate would have validated coverage; PostCompact behavior gate would have forced /orient |
| **msg #41 (May 5 10:58)** | *"DID YOU REALLY FORGET EVERY FUCKING THING I TOLD YOU IN THIS CONVERSATION??? WTF HOW IS THAT POSSIBLE?????"* | recent operator-verbatim directives + active-mission + active-focus | Layer 6 + 2 — both critical-tier; would have blocked compaction |
| **Brain-improvement mandate post-compact recovery (current arc 2026-05-07/08)** | Agent picked up post-compact and continued mandate work without re-orienting; pivoted to the second-brain instead of root when operator said "this side" | active-mission/focus + recent-operator-context | PostCompact behavior gate would have BLOCKED first action until /orient ran; /orient would have surfaced active-mission-still-set-to-mandate; agent wouldn't have pivoted away |
| **Multiple "did I not say" / "I already told you" recurrences** | Implicit pattern — operator re-explains; agent treats as new context | recent operator-verbatim directives | Layer 6 missing/stale; PreCompact completeness gate would have blocked compaction without those directives in handoff |
| **Stale-cached settings.json across compactions** (per `claude-code-hook-stamp-bug-cached-config-vs-settings-local-hot-reload` raw note) | Agent operated on cached settings post-compact | Sister-issue: Claude Code itself caches settings; orthogonal to handoff state but related | Pattern's STATE-RECOVERY REPORT would surface stale-cached-state warning |

5+ explicit + recursive instances across 4 days of conversation. Pattern-recurrence is empirical evidence for gate-tier (~100%) over advisory-tier (~70-85%).

## When To Apply

- **When designing PreCompact / PostCompact hooks** — use this pattern's gate specifications (completeness + behavior)
- **When extending existing /root pre-compact.sh / post-compact.sh** — add the gate logic
- **When auditing past sessions for compaction-quality** — `tools/compaction_quality_audit.py` provides the metric
- **When operator reports state-loss recurrence** — measure recovery-quality first; investigate which layers lost
- **When evaluating sister-project compaction discipline** — this pattern deploys via `/install-agent-brain`

## When Not To

- When project doesn't experience compactions (short sessions only)
- When state is purely conversational (no state files / governance / tracker exists)
- When handoff completeness gate cost exceeds compaction frequency value
- When operator explicitly suspends for a single compaction (`REASON="<why>"` bypass justified)

## Self-Check (audit procedure for any post-compact action)

Immediately after a PostCompact event:

1. **Have I invoked /orient yet THIS turn?** If no — stop; invoke /orient first.
2. **Have I read the most-recent pre-compact-handoff doc?** If no — find via `ls -t $HOME/wiki/log/*pre-compact-handoff*.md`; Read it.
3. **What's the recovery quality?** Compute: layers in handoff / layers active pre-compact. <80% = degradation; flag SB.
4. **What state-layers are missing or stale?** Surface in STATE-RECOVERY REPORT.
5. **Does the original task still apply?** Re-read recent operator messages. Does pre-compact mission still match? If divergence: surface to operator before continuing.

If 1=no or 2=no: this pattern's anti-pattern applies. Adopt fix order: /orient → handoff-read → STATE-RECOVERY REPORT → original action.

## Composability with siblings

This pattern composes with:
- **Pattern — Session-orientation pair** (PRIMARY parent — covers SessionStart; this pattern covers PostCompact mirror; together they cover BOTH cold-start events)
- **Lesson — Fresh AI sessions need ACTIVE orientation** (PRIMARY validated parent — broken-and-idle-after-compaction is the same pattern at compaction boundary)
- **Lesson — Documentation As Substitute For Discipline** (sibling 2026-05-08 — meta-frame)
- **Lesson — Agent-Context-Discipline Is Aspirational** (sibling 2026-05-08 — C04 explicitly cites "PostCompact agent re-makes pre-compact mistakes" anti-pattern; this pattern provides the cure)
- **Pattern — Blast-Radius Classification Pre-Action Severity Gate** (sibling 2026-05-08 — different gate-event but same enforcement-discipline-via-hook structure)
- **Pattern — SB-Tracker Priority-Shift Cycle-Step** (sibling 2026-05-08 — different gate-event; both are Stop-hook-style enforcement gates)
- **Lesson — Class 9 Freeze-After-Correction** (sibling 2026-05-08 — output-side substance gate composes with this pattern's STATE-RECOVERY REPORT shape)

The 8 pieces from 2026-05-08 work cover:
- SessionStart orientation (parent pattern at 03_validated)
- PostCompact orientation mirror (this pattern)
- 4 PreToolUse axis gates (C04 input + C02 territory + C08 correction-shape + C14 severity)
- 2 Stop-hook gates (C09 output substance + C12 SB-iteration substance)
- 1 cross-cutting meta (substitution-pattern)

Together: comprehensive event-lifecycle enforcement coverage.

## Properties

| Property | Description |
|---|---|
| **Mirrors mature parent** | Architecture mirrors SessionStart pattern; differs only in gate-event (SessionStart vs PostCompact) + state-recovery report output |
| **Two gates compose** | PreCompact completeness gate (preventive) + PostCompact behavior gate (corrective); together they bracket the compaction event |
| **Required-state-layers spec is data** | `tools/handoff_layers.py` is operator-extensible; new layers added per empirical observation |
| **State-recovery quality is measurable** | Quantified per recovery vs handoff coverage; per P1 quantified-evidence approach |
| **Bypass-able** | REASON env var for legitimate skip cases (rare) |
| **Sister-project portable** | Deploys via `/install-agent-brain` — operational tooling per brain-inheritance pattern |

## Relationships

- **DERIVED FROM** [Pattern — Session-orientation pair: SessionStart hook + /orient command + ORIENT REPORT](../03_validated/architecture/session-orientation-pair-sessionstart-hook-and-orient-command-with-orient-report.md) — **PRIMARY parent**. Mature pattern covers SessionStart; this pattern provides the PostCompact mirror that the parent's "When To Apply" section explicitly mentions but doesn't specify.
- **DERIVED FROM** [Lesson — Fresh AI sessions need ACTIVE orientation](../../lessons/03_validated/context-engineering/broken-and-idle-fresh-sessions-need-active-orientation-not-passive-context-loading.md) — VALIDATED parent. Broken-and-idle at compaction boundary is the same pattern.
- **DERIVED FROM** [Principle 1 — Infrastructure Over Instructions](../../lessons/04_principles/hypothesis/infrastructure-over-instructions-for-process-enforcement.md) — PostCompact discipline at advisory tier vs gate tier.
- **PARALLELS** [Lesson — Documentation As Substitute For Discipline (the meta-pattern)](../../lessons/01_drafts/documentation-as-substitute-for-discipline-the-meta-pattern.md) — DIRECT sibling 2026-05-08; meta-frame.
- **PARALLELS** [Lesson — Agent-Context-Discipline Is Aspirational](../../lessons/01_drafts/agent-context-discipline-is-aspirational-without-enforcement-gates-not-reading-what-exists.md) — DIRECT sibling 2026-05-08; C04 cites PostCompact-re-makes-mistakes anti-pattern; this pattern is the cure.
- **PARALLELS** [Pattern — Blast-Radius Classification Pre-Action Severity Gate](blast-radius-classification-and-pre-action-severity-gate.md) — DIRECT sibling 2026-05-08.
- **PARALLELS** [Pattern — SB-Tracker Priority-Shift Cycle-Step](systemic-bug-tracker-priority-shift-cycle-step-design.md) — DIRECT sibling 2026-05-08.
- **PARALLELS** [Pattern — Correction-as-Calibration Pre-Edit Verification Gate](correction-as-calibration-pre-edit-verification-gate-design.md) — DIRECT sibling 2026-05-08.
- **PARALLELS** [Lesson — Agent-Decision vs Operator-Decision Boundary Discrimination](../../lessons/01_drafts/agent-decision-vs-operator-decision-boundary-discrimination-pre-action-gate.md) — DIRECT sibling 2026-05-08.
- **PARALLELS** [Lesson — Class 9 Freeze-After-Correction](../../lessons/01_drafts/freeze-after-correction-is-class-9-of-agent-failure-taxonomy-abdication-as-freeze.md) — DIRECT sibling 2026-05-08.
- **CONSTRAINS** /root/.claude/hooks/pre-compact.sh — extension with completeness gate
- **CONSTRAINS** /root/.claude/hooks/post-compact.sh — extension with behavior gate
- **CONSTRAINS** /root/.claude/commands/orient.md — extension with STATE-RECOVERY REPORT shape
- **CONSTRAINS** /root/.claude/commands/handoff.md — companion to PreCompact auto-write
- **EXTENDS** SB-078 (PreCompact handoff) + SB-079 (PostCompact reliability) + SB-133 (envelope schema) — all three SBs marked structurally-fixed but BEHAVIOR-VERIFICATION still pending; this pattern is the verification-with-gate
- **SYNTHESIZES** [Pain-Points Inventory C05 Cluster](../../../raw/notes/2026-05-08-pain-points-inventory-from-root-failed-conversation-master-aggregate.md) — primary source.
- **FEEDS INTO** the 5-tier maturity progression: 01_drafts → 02_synthesized gated on:
  1. PreCompact completeness gate authored + tests
  2. PostCompact behavior gate authored + wired + tests
  3. Required-state-layers spec (`tools/handoff_layers.py`) authored
  4. STATE-RECOVERY REPORT format implemented in /orient
  5. `tools/compaction_quality_audit.py` aggregator authored
  6. Operator-confirmed promotion
- **Mission served**: 2026-05-06 brain-improvement mandate (failed) → 2026-05-08+ multi-day systematic pain-point resolution; this pattern is C05 cluster's proposed-solution piece.

## Backlinks

(Auto-regenerated by `pipeline post`. Mature parent pattern + sibling pieces accumulate this pattern.)
