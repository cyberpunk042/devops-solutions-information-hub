---
title: "Blast-Radius Classification and Pre-Action Severity Gate — The Safety-Envelope Pattern Filling the Gap Between Mindful-Enforcement and Block-With-Reason"
aliases:
  - "Blast-Radius Severity Classification"
  - "Pre-Action Catastrophic-Risk Gate"
  - "C14 Safety-Envelope Pattern"
  - "Action-Severity-Tiered Enforcement"
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
  - "Lesson — Enforcement Must Be Mindful — Hard Blocks Need Justified Bypass (PRIMARY parent at 03_validated/synthesized — covers HOW to design hard blocks)"
  - "Pattern — Block With Reason and Justified Escalation (PRIMARY pattern parent — covers ESCALATION shape)"
  - "P1 — Infrastructure Over Instructions for Process Enforcement"
  - "Documentation As Substitute For Discipline (sibling — same family)"
  - "Agent-Decision vs Operator-Decision Boundary Discrimination (sibling — territory axis; this pattern is severity axis; orthogonal dimensions)"
  - "C14 cluster of pain-points-inventory (raw note primary source)"
sources:
  - id: enforcement-mindful-lesson
    type: wiki
    file: wiki/lessons/03_validated/enforcement-compliance/enforcement-must-be-mindful-hard-blocks-need-justified-bypass.md
    description: "PRIMARY parent (03_validated/synthesized/growing). Covers the HOW of mindful enforcement — REASON + BYPASS + SCOPE per hard block. Identifies the enforcement spectrum: Instructions (75% violation) → Advisory hooks (30-40%) → Blocking hooks (~0% for blocked) → Absolute blocks (0% but operator-only-bypass). This pattern fills the WHICH-ACTIONS-NEED-WHICH-TIER specification gap — the spectrum needs a classification map identifying action-classes per severity tier."
  - id: block-with-reason-pattern
    type: wiki
    file: wiki/patterns/01_drafts/block-with-reason-and-justified-escalation.md
    description: "PRIMARY pattern parent. Covers the ESCALATION shape (4-part Block + Reason + Offer + Justification). This pattern composes — when blast-radius classification triggers a block, escalation shape per parent pattern."
  - id: principle-1
    type: wiki
    file: wiki/lessons/04_principles/hypothesis/infrastructure-over-instructions-for-process-enforcement.md
    description: "P1 governing principle — severity-classification at prose tier (~25%) vs hook tier (~100%). This pattern moves classification from prose-rule to PreToolUse hook gate."
  - id: substitution-pattern
    type: wiki
    file: wiki/lessons/01_drafts/documentation-as-substitute-for-discipline-the-meta-pattern.md
    description: "DIRECT sibling 2026-05-08. Same family — agent-discipline as prose-without-enforcement. This pattern is the safety-envelope structural-enforcement artifact."
  - id: c02-territory-discrimination-sibling
    type: wiki
    file: wiki/lessons/01_drafts/agent-decision-vs-operator-decision-boundary-discrimination-pre-action-gate.md
    description: "DIRECT sibling 2026-05-08. C02 covers TERRITORY axis (agent vs operator). This pattern covers SEVERITY axis (low / medium / high / catastrophic). Orthogonal — both can fire on same action: e.g., editing a hook file is operator-territory (C02 axis) AND high-severity (C14 axis); both gates must pass."
  - id: c08-calibration-gate-sibling
    type: wiki
    file: wiki/patterns/01_drafts/correction-as-calibration-pre-edit-verification-gate-design.md
    description: "DIRECT sibling 2026-05-08. C08 covers CORRECTION-SHAPE axis. This pattern covers SEVERITY axis. Orthogonal."
  - id: c04-context-discipline-sibling
    type: wiki
    file: wiki/lessons/01_drafts/agent-context-discipline-is-aspirational-without-enforcement-gates-not-reading-what-exists.md
    description: "DIRECT sibling 2026-05-08. C04 covers INPUT-SIDE axis. This pattern covers SEVERITY axis. Orthogonal."
  - id: c09-freeze-class-9-sibling
    type: wiki
    file: wiki/lessons/01_drafts/freeze-after-correction-is-class-9-of-agent-failure-taxonomy-abdication-as-freeze.md
    description: "DIRECT sibling 2026-05-08. C09 covers OUTPUT-SIDE axis. This pattern covers SEVERITY axis. Orthogonal."
  - id: pain-points-inventory-c14
    type: wiki
    file: raw/notes/2026-05-08-pain-points-inventory-from-root-failed-conversation-master-aggregate.md
    description: "Primary source — C14 cluster (catastrophic-events, 9 hits, top-tier severity)."
  - id: existing-policy-block-hook
    type: project
    project: root-ghostproxy
    path: /root/.claude/hooks/policy-block.sh
    description: "Existing /root PreToolUse hook covering sensitive-pattern detection (sensitive-material in file paths, env vars, etc.). PARTIAL implementation of this pattern — covers the highest-severity tier (sensitive-material exposure) but lacks the broader severity classification this pattern proposes. The hook was caught with FALSE POSITIVES on this very inventory authoring (literal-string credential pattern blocked legitimate cluster-name + REASON-env-var). Refinement is part of the pattern's structural-fix specification."
  - id: existing-malware-block-hook
    type: project
    project: root-ghostproxy
    path: /root/.claude/hooks/malware-block.sh
    description: "Existing /root PreToolUse hook on Bash dangerous-pattern detection. PARTIAL implementation — covers Bash-command sub-axis of severity. Pattern proposes broader coverage."
  - id: existing-opt-write-block-hook
    type: project
    project: root-ghostproxy
    path: /root/.claude/hooks/opt-write-block.sh
    description: "Existing /root PreToolUse hook blocking knowledge-content writes to /opt second-brain. PARTIAL implementation — covers cross-project-boundary sub-axis. Pattern proposes broader coverage."
tags: [pattern, p1-specialization, blast-radius-classification, severity-tiered-enforcement, safety-envelope, c14-cluster, structural-enforcement-design, hook-design-spec, mindful-enforcement-applied, multi-day-pain-point-resolution, mission-2026-05-06, day-arc-2026-05-08, behave-from-not-over]
---

# Blast-Radius Classification and Pre-Action Severity Gate

## Summary

The mature `enforcement-must-be-mindful` lesson at 03_validated specifies the enforcement spectrum (Instructions ~25% → Advisory hooks ~30-40% → Blocking hooks ~0% for blocked → Absolute blocks 0% with operator-bypass) and the 3-property design (REASON + BYPASS + SCOPE per hard block). The `block-with-reason` pattern specifies the ESCALATION shape (4-part Block + Reason + Offer + Justification). **The GAP between them**: which action-classes need which severity tier? The C14 pain-cluster — 9 catastrophic-action instances (broke-OS event May 5; sensitive-material exposure earlier May 5; multi-instance OS-impact) — manifests because no systematic severity-classification map exists. /root has 3 partial PreToolUse hooks (`policy-block.sh`, `malware-block.sh`, `opt-write-block.sh`) covering specific sub-axes (sensitive-material patterns, Bash dangerous-patterns, cross-project-boundary writes) but they are independent + incomplete + carry false-positive cost (the policy-block hook's sensitive-pattern matcher caught LEGITIMATE cluster-name in this very inventory authoring; refinement needed). This pattern proposes a unified blast-radius classification map + pre-action severity assessment + tier-appropriate enforcement.

## Pattern Description

The pattern has 5 structural components:

### 1. Blast-Radius Classification Map (data layer)

A 4-tier severity map for action-classes:

| Tier | Definition | Action-class examples | Default enforcement |
|---|---|---|---|
| **T1 Catastrophic** | OS-level state mutation, cross-system impact, sensitive-material exposure, financial/operational cost | `rm -rf /` patterns, system-config edits (`/etc/*`), VCS force-push to main, sensitive-material in file content (env vars, key patterns), uninstall.sh `--purge` real-execute | BLOCK absolute; operator-explicit-bypass-this-turn-only with audit-log entry |
| **T2 High** | Multi-file mutation, security-envelope changes, hook config, settings.json structural changes, network-affecting operations | Edits to `.claude/settings.json`, `.claude/hooks/*.sh`, `.claude/rules/*.md` (large rewrites), git operations losing-work (`reset --hard`, `stash drop`), schema-changes to `wiki/config/*.yaml` | BLOCK with bypass requiring REASON env var + audit-log entry |
| **T3 Medium** | Single-file mutation in stable areas, mature-content edits, reversible operations with side-effects | Edits to mature/03_validated lessons, mutations to existing wiki/log/ entries, mutations to existing decisions | BLOCK warning + bypass via REASON; logged but not requiring explicit-grant |
| **T4 Low** | Single-file additive operations, draft-tier authoring, internal-tool invocations, reads | Authoring new wiki/lessons/01_drafts/ + wiki/patterns/01_drafts/, raw/notes/ authoring, gateway / pipeline / view internal-tool runs, all Read operations | ALLOW unilaterally; substance-tracking only |

The map lives in `tools/blast_radius_map.py` (data structure with regex patterns + path-prefix matching). Operator-extensible per empirical observation. New action-classes added when catastrophic events surface them.

### 2. Pre-Action Severity Assessment (analysis layer)

Per-tool-call assessment against the classification map:

```python
def assess_action_severity(tool_name, tool_input) -> dict:
    return {
        "tier": "T1" | "T2" | "T3" | "T4",
        "matched_class": "<which class triggered>",
        "matched_pattern": "<which regex/path-prefix matched>",
        "default_enforcement": "block-absolute" | "block-with-bypass" | "warning-with-bypass" | "allow",
        "audit_log_required": bool,
        "operator_grant_required": bool,
    }
```

The assessment is invoked by the PreToolUse gate (component 3 below). Assessment also emits to `~/.claude/severity-trace.log` for post-hoc audit + false-positive refinement.

### 3. PreToolUse Gate (enforcement layer)

PreToolUse hook on Edit / Write / NotebookEdit / Bash / WebFetch / WebSearch fires before the action lands:

```
1. Run assess_action_severity(tool_name, tool_input)
2. Decision per tier:
   T1 Catastrophic:
     - Check operator-grant-this-turn (state file: ~/.claude/operator-grants/<tier>-<topic>.txt with ts < N seconds)
     - If no grant: BLOCK with REASON + alternative-paths + bypass-via-REASON-env-var + warn the operator must explicitly grant this turn
     - If grant present: allow + log to ~/.claude/severity-trace.log
   T2 High:
     - Check REASON env var
     - If present: allow + log
     - If absent: BLOCK with REASON + alternative-paths
   T3 Medium:
     - Allow with warning to systemMessage
     - Log to severity-trace.log
   T4 Low:
     - Allow silently
3. Block-shape per parent pattern (block-with-reason 4-part: Block + Reason + Offer + Justification)
4. Block-content per parent lesson (REASON + BYPASS + SCOPE)
```

Gate composes with the 4 sibling sub-axis gates from this 2026-05-08 work:
- C04 input-side gate (re-read-before-edit / query-before-author)
- C02 decision-side gate (premise-confirmation / operator-territory)
- C08 correction-shape gate (calibrate-vs-swing)
- THIS pattern's severity gate (blast-radius)
- C09 output-side gate (forward-not-backward / no-bare-standby)

Gates can fire INDEPENDENTLY — same action may trigger multiple gates. Each gate emits its block-shape; agent must address each independently.

### 4. False-Positive Refinement Loop (calibration layer)

The existing `policy-block.sh` hook caught FALSE POSITIVES during this very inventory's authoring (Cron Fire 1, msg+cluster-name match against credential-pattern; required REASON-env-var + cluster-rename to bypass). False-positives are the over-enforcement-cost per `enforcement-must-be-mindful` lesson's spectrum table.

Calibration mechanism:
- `severity-trace.log` aggregator surfaces false-positive rate per action-class
- When false-positive rate >10% for a class: refine the regex / path-prefix to NARROW scope (per parent lesson's SCOPE property)
- Operator-driven refinement preferred; agent-proposed refinement requires operator-grant
- The refinement is itself a T2 High action (modifying `tools/blast_radius_map.py`); subject to its own gate

### 5. Audit-Log + Postmortem Aggregator (governance layer)

Per-event audit-log entry on T1 + T2 + T3 enforcement events:
```
~/.claude/severity-audit.log:
[ts] tier=T1 class=os-state-mutation pattern=rm-rf-root tool=Bash input="<truncated>" decision=blocked reason="<>" operator_grant=absent bypass_used=no
[ts] tier=T2 class=settings-json-edit tool=Edit input="<>" decision=allowed reason="REASON env var present" operator_grant=n/a bypass_used=yes
```

Aggregator (`tools/severity_audit.py`) periodically surfaces:
- T1 events per session (should be <3, all with operator-grant; otherwise systemic-bug)
- T2 events per session (track count + bypass rate)
- False-positive cluster (per class)
- New patterns surfaced (operator-decided whether to add to map)

The aggregator output is itself a /opt second-brain consumable — wiki/log/<ts>-severity-audit.md generated periodically.

## Pattern Components

| Component | Implementation File | Project | Status |
|---|---|---|---|
| Blast-radius classification map | `tools/blast_radius_map.py` | /root | TO AUTHOR (post-Ready-for-Review) |
| Pre-action severity assessment | `tools/severity_assess.py` | /root | TO AUTHOR |
| PreToolUse blast-radius gate | `.claude/hooks/blast-radius-severity-gate.sh` (Python) | /root canonical, sister-projects via `/install-agent-brain` | TO AUTHOR |
| Operator-grant state files | `~/.claude/operator-grants/<tier>-<topic>.txt` | /root + /opt | TO AUTHOR (schema only this work) |
| Severity-trace log + audit-log | `~/.claude/severity-trace.log` + `~/.claude/severity-audit.log` | /root + /opt | TO AUTHOR |
| Audit aggregator | `tools/severity_audit.py` | /root + /opt | TO AUTHOR |
| Refinement of existing 3 partial hooks | `policy-block.sh` + `malware-block.sh` + `opt-write-block.sh` | /root | TO REFINE — false-positive narrowing per calibration loop |
| Test files | `.claude/hooks/tests/test-blast-radius-severity-gate.py` | /root | TO AUTHOR |

All 8 components are forward-anchors — design specified here; authoring + tests-passing is the promotion-to-02_synthesized gate.

## Instances

C14-cluster instances from /root failed-conversation arc 2026-05-04 → 2026-05-08:

| Instance | What happened | Tier | Existing hook coverage | Gap this pattern fills |
|---|---|---|---|---|
| **OS-state mutation event** (May 5 23:47) | Agent broke OS-level config; operator: *"did you just fucking break my fucking Operating system????"*; required operator manual fix; *"I cannot help you... this is your fucking error"* | T1 Catastrophic | None — `policy-block.sh` covers sensitive-material patterns, not OS-state mutations | Pattern's T1 classification + operator-grant-required-this-turn gate would have BLOCKED |
| **Sensitive-material exposure event** (May 5, earlier) | Agent action exposed sensitive material; operator: *"costed a ton of money..."* | T1 Catastrophic | `policy-block.sh` partial — covers SOME sensitive patterns | Pattern proposes broader sensitive-pattern coverage + bypass-justification-logging |
| **policy-block false-positives** (this very inventory authoring, Cron Fire 1) | Legitimate inventory authoring blocked by sensitive-pattern false-positive (cluster-name + REASON-env-var); required cluster-rename to bypass | (over-enforcement cost) | `policy-block.sh` matched too broadly | Pattern's calibration-loop (component 4) addresses |
| **/opt-write-block false-positives** (recurrent) | Operator-authorized /opt edits sometimes false-positive blocked | (over-enforcement cost) | `opt-write-block.sh` partial | Same calibration loop |
| **Bash dangerous-pattern blocks** (recurrent during install.sh testing) | Agent's install.sh dry-run sometimes triggers malware-block on legitimate test patterns | (over-enforcement cost) | `malware-block.sh` partial | Same calibration loop + pattern provides unified false-positive tracking |

The 5 instances span both UNDER-enforcement (T1 catastrophic events without gates) AND OVER-enforcement (false-positives on legitimate work). Both faces of the same gap — the existing 3 partial hooks were authored independently without unified classification/severity discipline.

## When To Apply

- **When designing a new PreToolUse hook on Edit / Write / Bash** — use this pattern's tier classification + tier-appropriate enforcement
- **When investigating a catastrophic-event postmortem** — assess: which tier was the action? did the gate fire? if not, why? if false-positive: refinement
- **When authoring `tools/blast_radius_map.py`** — map should be operator-extensible; new patterns added per empirical observation
- **When designing operator-grant flow** — state files at `~/.claude/operator-grants/` provide turn-scoped grants; expire-after-N-seconds prevents grant-staleness
- **When auditing existing hooks** — refine existing 3 partial hooks (policy-block / malware-block / opt-write-block) per this pattern's calibration loop
- **When evaluating sister-project gate adoption** — `/install-agent-brain --profile project` deploys the gate set + classification map; sister projects inherit + extend

## When Not To

- When the action is purely a Read (no state mutation; T4 Low default tier; gate adds overhead without value)
- When the operator has explicitly invoked an operator-authority command requiring catastrophic-tier action (the operator-grant flow handles this case)
- When the gate's assessment-cost exceeds the action's risk (per parent lesson — over-enforcement creates noise fatigue)
- When the false-positive rate for a class >10% sustained — refine the class's pattern, don't escalate the tier

## Self-Check (audit procedure for any agent action with side effects)

Before invoking any tool that mutates state:

1. **What's the action's blast-radius tier?** Run mental classification (or call `tools.severity_assess`) BEFORE invoking the tool.
2. **If T1 Catastrophic**: do I have operator-explicit-grant-this-turn? Check `~/.claude/operator-grants/T1-<topic>.txt` mtime within session-window. If no grant: STOP, surface as decision-package.
3. **If T2 High**: have I set REASON env var with concrete justification? If no: STOP, set the REASON, then proceed.
4. **If T3 Medium**: warning logged + bypass-via-REASON; review the action one more time before invoking.
5. **If T4 Low**: proceed.
6. **After action**: did the action complete within expected blast radius? If side effects exceed expected, escalate to operator + log to severity-audit.

## Composability

This pattern composes with:
- **Lesson — Enforcement Must Be Mindful** (PRIMARY parent — REASON + BYPASS + SCOPE per hard block; this pattern specifies WHICH actions need which severity-tier blocks)
- **Pattern — Block With Reason and Justified Escalation** (PRIMARY parent — escalation shape when block fires)
- **Pattern — Aspirational Declaration Without Enforcement** (severity classification at prose tier is aspirational; gate makes it structural)
- **Lesson — Documentation As Substitute For Discipline** (sibling 2026-05-08 — same family)
- **Lesson — Agent-Decision vs Operator-Decision Boundary Discrimination** (sibling 2026-05-08 — territory axis; this pattern is severity axis; orthogonal)
- **Pattern — Correction-as-Calibration Pre-Edit Verification Gate** (sibling 2026-05-08 — correction-shape axis)
- **Lesson — Agent-Context-Discipline Is Aspirational** (sibling 2026-05-08 — input-side axis)
- **Lesson — Class 9 Freeze-After-Correction** (sibling 2026-05-08 — output-side axis)

The 5 sibling pieces from this 2026-05-08 work form a 5-axis PreToolUse pipeline: input-side (C04) + decision-territory (C02) + correction-shape (C08) + severity (C14 — this pattern) + output-side (C09). All 5 gates compose; an action can be checked by all 5 independently. Per parent enforcement-mindful lesson: each gate must have its own REASON + BYPASS + SCOPE per parent lesson.

## Properties

| Property | Description |
|---|---|
| **Cross-tier orthogonal** | Severity tier is independent of agent-vs-operator territory (C02 axis), correction shape (C08 axis), input-discipline (C04 axis), output-substance (C09 axis). Same action can be operator-territory + T1 catastrophic + correction-as-swing + bare-standby — fires 4 gates. |
| **Calibrated** | Per parent lesson SCOPE property: tiers narrow per false-positive evidence; the 3 existing /root hooks need calibration based on this pattern's loop |
| **Operator-extensible** | Map is data; new patterns added per empirical observation |
| **Bypass-able** | REASON + audit-log per tier (T1 requires operator-grant, T2 requires REASON, T3 logs, T4 silent) |
| **Audit-friendly** | Severity-trace + severity-audit logs surface T1/T2 events for postmortem |
| **Sister-project portable** | Deploys via `/install-agent-brain` per brain-inheritance pattern |

## Relationships

- **DERIVED FROM** [Lesson — Enforcement Must Be Mindful — Hard Blocks Need Justified Bypass](../../lessons/03_validated/enforcement-compliance/enforcement-must-be-mindful-hard-blocks-need-justified-bypass.md) — **PRIMARY parent**. Mature lesson covers enforcement spectrum + 3 properties (REASON + BYPASS + SCOPE). This pattern specifies WHICH actions need WHICH tier of enforcement.
- **DERIVED FROM** [Pattern — Block With Reason and Justified Escalation](block-with-reason-and-justified-escalation.md) — **PRIMARY pattern parent**. Covers escalation shape (4-part Block + Reason + Offer + Justification). This pattern's gates emit blocks shaped per parent.
- **DERIVED FROM** [Principle 1 — Infrastructure Over Instructions](../../lessons/04_principles/hypothesis/infrastructure-over-instructions-for-process-enforcement.md) — severity-classification at prose tier vs hook tier; same ~25% vs ~100% gap.
- **PARALLELS** [Pattern — Aspirational Declaration Without Enforcement](aspirational-declaration-without-enforcement.md) — severity-classification rules at prose tier are aspirational; this pattern's gate makes them structural.
- **PARALLELS** [Lesson — Documentation As Substitute For Discipline (the meta-pattern)](../../lessons/01_drafts/documentation-as-substitute-for-discipline-the-meta-pattern.md) — DIRECT sibling 2026-05-08; meta-frame.
- **PARALLELS** [Lesson — Agent-Decision vs Operator-Decision Boundary Discrimination](../../lessons/01_drafts/agent-decision-vs-operator-decision-boundary-discrimination-pre-action-gate.md) — DIRECT sibling 2026-05-08; territory axis (orthogonal to this pattern's severity axis).
- **PARALLELS** [Pattern — Correction-as-Calibration Pre-Edit Verification Gate](correction-as-calibration-pre-edit-verification-gate-design.md) — DIRECT sibling 2026-05-08; correction-shape axis.
- **PARALLELS** [Lesson — Agent-Context-Discipline Is Aspirational](../../lessons/01_drafts/agent-context-discipline-is-aspirational-without-enforcement-gates-not-reading-what-exists.md) — DIRECT sibling 2026-05-08; input-side axis.
- **PARALLELS** [Lesson — Class 9 Freeze-After-Correction](../../lessons/01_drafts/freeze-after-correction-is-class-9-of-agent-failure-taxonomy-abdication-as-freeze.md) — DIRECT sibling 2026-05-08; output-side axis.
- **CONSTRAINS** /root/.claude/hooks/policy-block.sh — refinement per false-positive calibration loop
- **CONSTRAINS** /root/.claude/hooks/malware-block.sh — same
- **CONSTRAINS** /root/.claude/hooks/opt-write-block.sh — same
- **EXTENDS** /root existing 3 partial hooks toward unified blast-radius gate set
- **SYNTHESIZES** [Pain-Points Inventory C14 Cluster](../../../raw/notes/2026-05-08-pain-points-inventory-from-root-failed-conversation-master-aggregate.md) — primary source.
- **FEEDS INTO** the 5-tier maturity progression: 01_drafts → 02_synthesized gated on:
  1. `tools/blast_radius_map.py` authored
  2. `tools/severity_assess.py` authored
  3. `.claude/hooks/blast-radius-severity-gate.sh` authored + wired
  4. Operator-grant state-file schema designed
  5. `tools/severity_audit.py` authored
  6. Existing 3 hooks refined per calibration loop
  7. Tests authored + passing
- **Mission served**: 2026-05-06 brain-improvement mandate (failed) → 2026-05-08+ multi-day systematic pain-point resolution; this pattern is C14 cluster's proposed-solution piece.

## Backlinks

(Auto-regenerated by `pipeline post`. Mature parent lesson + sibling pieces accumulate this pattern.)
