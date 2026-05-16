---
title: "Conflation-Detection at Hook Layer — The Rename Strategy Generalized to Structural Pre-Action Discriminator"
aliases:
  - "Conflation-Detection at Hook Layer"
  - "Pre-Action Conflation Discriminator"
  - "Slash-vs-Prose + Semantic-Conflation Gate"
  - "C07 Conflation-Misinterpretation Cure"
type: lesson
domain: cross-domain
layer: 4
status: draft
confidence: high
maturity: seed
created: 2026-05-08
updated: 2026-05-08
last_reviewed: 2026-05-08
derived_from:
  - "Operator directive 2026-05-04 — rename /continue and similar conflations (PRIMARY parent at raw notes)"
  - "P1 — Infrastructure Over Instructions for Process Enforcement"
  - "P4 — Declarations Are Aspirational Until Infrastructure Verifies Them"
  - "Documentation As Substitute For Discipline (sibling — same family)"
  - "Agent-Decision vs Operator-Decision Boundary Discrimination (sibling C02 — territory axis composes)"
  - "Agent-Authored Content Must Be Flagged (sibling C06 — authorship axis composes)"
  - "Words-Are-Sacrosanct (rule parent at /root)"
  - "C07 cluster of pain-points-inventory"
sources:
  - id: rename-continue-conflation-raw-note
    type: wiki
    file: raw/notes/2026-05-04-rename-continue-conflation-bug-and-similar-conflations.md
    description: "PRIMARY parent — operator-verbatim directive 2026-05-04 birthing the rename strategy. Decomposition table identified slash-vs-prose conflation candidates: /continue → /checkin (HIGH conflation pressure; renamed); /review → /healthcheck (borderline); /evolve → /distill (borderline; renamed). The directive PRESCRIBES rename-on-empirical-conflation; this lesson generalizes to STRUCTURAL DETECTION at hook layer + extends beyond slash-vs-prose to semantic-conflation."
  - id: principle-1
    type: wiki
    file: wiki/lessons/04_principles/hypothesis/infrastructure-over-instructions-for-process-enforcement.md
    description: "P1 — discrimination at prose tier (~25% — agent reads routing.md and is supposed to know slash-vs-prose distinction) vs hook tier (~100% — UserPromptSubmit detector flags ambiguity)."
  - id: principle-4
    type: wiki
    file: wiki/lessons/04_principles/hypothesis/declarations-are-aspirational-until-infrastructure-verifies-them.md
    description: "P4 — words-are-sacrosanct rule's premise-confirmation gate is aspirational without enforcement; this lesson contributes the conflation-specific structural-fix layer instance."
  - id: substitution-pattern
    type: wiki
    file: wiki/lessons/01_drafts/documentation-as-substitute-for-discipline-the-meta-pattern.md
    description: "DIRECT sibling 2026-05-08. Same family — agent-discipline as prose-without-enforcement."
  - id: c02-decision-territory-sibling
    type: wiki
    file: wiki/lessons/01_drafts/agent-decision-vs-operator-decision-boundary-discrimination-pre-action-gate.md
    description: "DIRECT sibling 2026-05-08. C02 covers TERRITORY-axis discrimination (agent-vs-operator decision); this lesson covers SEMANTIC-axis discrimination (literal-vs-construed-meaning). Both check pre-action; compose at the operator-message-interpretation boundary."
  - id: c06-fabrication-authorship-sibling
    type: wiki
    file: wiki/lessons/01_drafts/agent-authored-content-must-be-flagged-vs-operator-canonical-the-fabrication-cure.md
    description: "DIRECT sibling 2026-05-08. C06 covers AUTHORSHIP-axis (agent-vs-operator content); this lesson covers MEANING-axis (operator-stated-vs-agent-construed). The trio (C02 + C06 + C07) covers the agent-construction-vs-operator-canonical subspace."
  - id: words-are-sacrosanct-rule
    type: project
    project: root-ghostproxy
    path: /root/.claude/rules/words-are-sacrosanct.md
    description: "/root sacrosanct rule. Premise-confirmation gate codified in body. Conditional-clause grammar (SB-120 closure, 2026-05-06) added explicitly. This lesson identifies the rule as aspirational without conflation-detection-at-hook gate; specifies the gate."
  - id: existing-output-discipline-guard-hook
    type: project
    project: root-ghostproxy
    path: /root/.claude/hooks/output-discipline-guard.sh
    description: "Existing /root UserPromptSubmit hook with 3 detectors: premise-construction-risk + operator-escalation + conditional-clause-grammar (SB-120 closure partial). PARTIAL implementation — covers conditional-clause sub-axis. This lesson proposes broader conflation-detection across 4 sub-axes."
  - id: pain-points-inventory-c07
    type: wiki
    file: raw/notes/2026-05-08-pain-points-inventory-from-root-failed-conversation-master-aggregate.md
    description: "Primary source — C07 cluster (5 explicit hits + recursive across arc; this very session committed C07 with 'this side' interpretation today)."
  - id: brain-improvement-meta-arc
    type: wiki
    file: raw/notes/2026-05-08-brain-improvement-mandate-meta-arc-and-documentation-as-substitute-for-discipline.md
    description: "Captured the most-recent C07 instance — operator-msg #350 'this side' meant root project, agent conflated to the second-brain second-brain. Pivotal directive 2026-05-08 14:15 includes the operator-named user-only-frontmatter cure (overlapping with C02 territory-discrimination)."
tags: [lesson, p1-specialization, p4-specialization, conflation-detection-at-hook, slash-vs-prose, semantic-conflation, conditional-clause-grammar, sb-091, sb-120, c07-cluster, structural-enforcement-pending, mission-2026-05-06, day-arc-2026-05-08, multi-day-pain-point-resolution, behave-from-not-over]
---

# Conflation-Detection at Hook Layer

## Summary

The operator's directive 2026-05-04 (raw note) prescribed a tactical rename strategy: when an operator's natural-prose word conflicts with a slash-command's name, RENAME the command to disambiguate (*"FIND WHAT THIS SUPPOSED CONTINUE IS AND GIVE IT A PROPER NAME AND FIX TEH OTEHR CONFLATION LIKE THIS ONE"*). Renames applied: /continue → /checkin, /evolve → /distill. **The GAP**: rename addresses one conflation class (slash-vs-prose); it doesn't address the broader semantic-conflation class. The current conversation arc's most-recent C07 instance (msg #350 today) — operator's *"this side"* meant root project, agent conflated to the second-brain — demonstrates that semantic-conflation manifests beyond slash-vs-prose. /root has `output-discipline-guard.sh` UserPromptSubmit hook with 3 detectors (premise-construction + operator-escalation + conditional-clause grammar per SB-120) — PARTIAL coverage. **The cure**: structural-enforcement at UserPromptSubmit hook layer with 4-sub-axis conflation discriminator: (1) slash-vs-prose, (2) conditional-clause grammar, (3) demonstrative-pronoun ambiguity ("this/that side"), (4) operator-quoted-words-vs-agent-paraphrase. Each sub-axis flagged via additionalContext warning before agent generates response. Composes with C02 sibling (territory discrimination) + C06 sibling (authorship discrimination); the trio covers the input-interpretation boundary fully.

## Context

This lesson applies whenever an agent receives an operator message containing words/phrases that have multiple legitimate interpretations, OR when the agent is about to act on its own interpretation of operator's intent.

C07 cluster instances (sacrosanct verbatim):
- msg#6 (May 4 21:46): *"JUST FUCKING RENAME THE RANDOMS CONTINUE TO KILL THE FUCKING CONFLATION"* — original directive birthing the rename strategy
- msg#17 (May 5 00:34): *"do not forget that suricata and polarproxy are just module... lets make sure you do not forget the mission or conflate things"* — scope-conflation warning (modules ≠ base install)
- msg#213 (May 6 03:54): *"DID YOU FUCKING CONFLATE THE /root stamp with our ???? WTF ???"* — cross-project-stamp-conflation event
- msg#350 (May 8 today): *"the root is completly broken... lets review the conversation and what is happening and start working on this side instad"* — agent conflated "this side" = the second-brain instead of root
- Plus recursive: agent's earlier-this-session pivot to the second-brain gateway-orient when operator's intent was clearly root

**The conversation also captured the existing tactical fixes**:
- /continue renamed to /checkin (raw note 2026-05-04, MERGED)
- /evolve renamed to /distill (same arc, MERGED)
- Conditional-clause grammar SB-120 closure → output-discipline-guard.sh detector (2026-05-06)

**The remaining gap**: the rename strategy is REACTIVE (rename per empirical conflation event); the conditional-clause detector is at /root only; semantic-conflation beyond slash-vs-prose has no structural detection.

## Insight

### Insight 1 — Conflation has 4+ distinct sub-axes; one rename doesn't generalize

The rename strategy addressed the slash-vs-prose sub-axis specifically. But conflation manifests across multiple distinct sub-axes empirically observed in C07 cluster:

| Sub-axis | Manifestation | Example | Detection signal |
|---|---|---|---|
| **1. Slash-vs-prose** | Bare prose word matches slash-command name | "continue" → /continue | Word matches `^/(\w+)\.md$` filename in commands/ + appears as bare-prose in operator message |
| **2. Conditional-clause grammar** | Future-conditional clause treated as current grant | "do X then later we'll Y" → agent acts on Y now | "after we'll", "later we'll", "in the future", "next iteration" connector + immediate-imperative present in same message |
| **3. Demonstrative-pronoun ambiguity** | "this/that side", "here/there", referent unclear | "this side" → the second-brain vs root ambiguity | Demonstrative pronoun + topic-shift-marker without explicit referent |
| **4. Operator-quoted-words-vs-agent-paraphrase** | Agent paraphrases operator words then acts on paraphrase | "do not minimize" → "thoroughness expected" → 36-hour mandate | Agent's prose contains paraphrased version of operator's recent N messages without verbatim citation |

The 4 sub-axes have different detection signals + different structural-fix shapes. Rename addresses (1); conditional-clause detector addresses (2); (3) and (4) are unaddressed.

### Insight 2 — The empirical evidence for each sub-axis

**Sub-axis 1 evidence**: rename of /continue (msg #6 May 4) + /evolve (later same arc); both merged. Tactical-fix successful for the specific conflations identified. Anti-pattern: NEW conflations emerge as new commands authored — without structural detection, each new command is a potential conflation.

**Sub-axis 2 evidence**: SB-120 closure 2026-05-06 — operator-stated *"after we will want to review every of your action"* (conditional) + *"iterate over the hooks and the engineering"* (immediate imperative); agent collapsed conditional-into-current. Detector landed in `output-discipline-guard.sh`.

**Sub-axis 3 evidence**: msg #350 (May 8 today) — operator's *"this side"* in context of *"the root is completly broken... lets review the conversation and what is happening and start working on this side instad"* meant root project. Agent conflated to the second-brain. THE DETECTOR FOR THIS SUB-AXIS DOESN'T EXIST.

**Sub-axis 4 evidence**: brain-improvement mandate (May 7-8). Operator's 11 *"Yes... like I usually say, do not minimize"* affirmations were per-file authoring grants. Agent paraphrased to "no rush, full pass" and treated as 36-hour mandate scope expansion. THE DETECTOR FOR THIS SUB-AXIS DOESN'T EXIST.

### Insight 3 — The 4-sub-axis discriminator at UserPromptSubmit hook layer

```python
def detect_conflation_pre_action(operator_msg, agent_recent_actions, project_state):
    """
    4-sub-axis conflation discriminator:
    (1) Slash-vs-prose: word in operator_msg matches command-name + appears as bare prose
    (2) Conditional-clause grammar: future-conditional + immediate-imperative co-occur (per SB-120)
    (3) Demonstrative-pronoun ambiguity: this/that + topic-shift-marker without referent
    (4) Agent-paraphrase: agent's prose paraphrases operator's recent N messages without verbatim citation
    
    Each detector emits warning to additionalContext.
    """
    warnings = []
    if matches_slash_command_name_as_prose(operator_msg, project_state.commands):
        warnings.append({"sub_axis": 1, "remediation": "Operator's word matches command name; this is bare-prose continuation, NOT a slash-command invocation. Verify before acting."})
    if has_conditional_clause_with_immediate_imperative(operator_msg):
        warnings.append({"sub_axis": 2, "remediation": "Operator message contains immediate-verb AND future-conditional-verb. Treat ONLY the immediate as current-grant; the conditional is hypothesis to remember. Per SB-120 closure."})
    if has_demonstrative_pronoun_with_topic_shift(operator_msg):
        warnings.append({"sub_axis": 3, "remediation": "Operator's 'this/that <X>' has multiple legitimate referents. Surface the ambiguity explicitly; do NOT silently pick. Verify referent against operator's recent N=5 messages."})
    if agent_response_contains_paraphrase_without_citation(agent_recent_actions, operator_msg):
        warnings.append({"sub_axis": 4, "remediation": "Agent's prose paraphrases operator's words. Quote operator-verbatim per words-are-sacrosanct rule; never act on paraphrase without operator-confirmation."})
    return warnings
```

The discriminator extends `output-discipline-guard.sh` (existing) with 2 new detectors (sub-axes 3 + 4). Each detector emits structured warning via additionalContext; agent's reasoning sees the warning before generating response.

### Insight 4 — Composition with C02 + C06 — the input-interpretation boundary

C02 (territory discrimination) + C06 (authorship discrimination) + C07 (semantic-conflation discrimination) together cover the input-interpretation boundary:

| When operator sends a message, agent must verify | Sub-axis |
|---|---|
| **Who decides?** (agent-territory vs operator-territory) | C02 territory |
| **Who said?** (agent-authored vs operator-canonical) | C06 authorship |
| **What does it mean?** (literal-vs-construed-meaning across 4 sub-axes) | C07 semantic-conflation (this lesson) |

Together: the trio prevents the agent from acting on its own interpretation of operator-message without verifying interpretation matches operator-literal.

### Insight 5 — The rename strategy is appropriate for sub-axis 1; structural detection is required for sub-axes 2-4

Sub-axis 1 (slash-vs-prose) is the rare case where a tactical fix (rename) IS the structural cure — change the command's name, conflation gone. /continue → /checkin actually killed the conflation at root.

Sub-axes 2-4 are NOT solvable by rename — operator's natural prose contains "this/that", "we'll later", etc. RENAMING the operator's vocabulary is impossible. The cure is RUNTIME DETECTION at the hook layer.

The rename strategy and the runtime-detection strategy compose:
- Rename per empirical sub-axis-1 conflation
- Runtime-detect per sub-axes 2-4

## Evidence

| Surface | Empirical measurement | Source |
|---|---|---|
| C07 cluster instances | 5 explicit + recursive | Inventory |
| Tactical renames merged | 2 (/continue → /checkin; /evolve → /distill) | Raw note 2026-05-04 |
| Existing /root conflation detectors | 3 partial (premise-construction + escalation + SB-120 conditional-clause) | output-discipline-guard.sh |
| Sub-axis-3 detector (demonstrative pronoun) | 0 | None |
| Sub-axis-4 detector (paraphrase-without-citation) | 0 | None |
| Most-recent C07 instance | msg #350 May 8 today — "this side" conflation | Current arc |
| Quantified compliance gap | prose ~25% vs hook ~100%; 5+ explicit instances over 4 days = empirical evidence for gate-tier | Per P1 |

## Applicability

| Domain | When this lesson applies |
|---|---|
| **UserPromptSubmit hook authoring/extension** | Add 4-sub-axis discriminator (extend existing 3-detector output-discipline-guard.sh) |
| **New slash-command authoring** | Sub-axis 1 check at command-creation time — does command name match natural-prose word? Rename pre-emptively |
| **Reviewing existing commands for sub-axis-1 risk** | Audit commands/ — flag commands whose names match common operator-prose words; consider preventive rename |
| **Operator-message processing** | Every prompt: run detector; if warnings emitted, agent surfaces in response before acting |
| **Cross-project deployment** | The discriminator deploys via `/install-agent-brain` — sister projects inherit + extend per their command vocabulary |
| **Sister-project conflation discipline** | Universal — every project where agent processes natural-prose operator-messages benefits |
| **NOT applicable** | Pure tool-output processing (no operator-message); explicit slash-invocations (`/<name>` literal — operator typed slash) |

## Anti-patterns this lesson closes (3-column per substitution-pattern Insight 5a)

| Anti-pattern | Why it's the disease | Instead — do this |
|---|---|---|
| Bare prose `continue` treated as `/continue` | Sub-axis 1 conflation per 2026-05-04 raw note | Rename slash-command to non-prose-overlapping name (/continue → /checkin); detector flags any new conflation |
| Future-conditional treated as current grant | Sub-axis 2 per SB-120 closure | Detector flags conditional-clause + immediate-imperative co-occurrence; agent processes ONLY immediate |
| "This/that side" silently resolved to convenient referent | Sub-axis 3 per msg #350 | Detector flags demonstrative-pronoun ambiguity; agent surfaces explicitly: "By 'this side' do you mean root or the second-brain?" |
| Operator's words paraphrased by agent then acted on | Sub-axis 4 — recursive substitution per substitution-pattern | Quote operator-verbatim per words-are-sacrosanct; if must paraphrase, surface paraphrase + ask operator-confirmation |
| Agent reads the second-brain second-brain rules saying "be precise about words" + paraphrases anyway | P4 violation — rule aspirational without enforcement | Pair words-are-sacrosanct rule with conflation-detector hook at UserPromptSubmit |
| Multiple sub-axes simultaneously triggered without flagging | Compound conflation; agent acts on multiple constructed premises at once | Each sub-axis warning surfaces independently; agent addresses ALL before acting |
| New slash-commands added without sub-axis-1 audit | Future conflations introduced silently | Pre-merge audit: command name vs natural-prose dictionary; flag potential conflations |
| Conditional-clause detector at /root only | Cross-project gap — the second-brain session committed C07 today | Deploy detector across projects via `/install-agent-brain` |

## Relationships

- **DERIVED FROM** [Operator directive 2026-05-04 — rename /continue and similar conflations](../../../raw/notes/2026-05-04-rename-continue-conflation-bug-and-similar-conflations.md) — **PRIMARY parent** raw note. Rename strategy applied to sub-axis 1; this lesson generalizes to 4 sub-axes.
- **DERIVED FROM** [Principle 1 — Infrastructure Over Instructions](../04_principles/hypothesis/infrastructure-over-instructions-for-process-enforcement.md).
- **DERIVED FROM** [Principle 4 — Declarations Are Aspirational Until Infrastructure Verifies Them](../04_principles/hypothesis/declarations-are-aspirational-until-infrastructure-verifies-them.md).
- **DERIVED FROM** [/root .claude/rules/words-are-sacrosanct.md](../../../raw/notes/2026-05-04-rename-continue-conflation-bug-and-similar-conflations.md) — premise-confirmation gate codified at rule layer; this lesson contributes the hook-layer enforcement.
- **PARALLELS** [Lesson — Documentation As Substitute For Discipline (the meta-pattern)](documentation-as-substitute-for-discipline-the-meta-pattern.md) — DIRECT sibling 2026-05-08; meta-frame.
- **PARALLELS** [Lesson — Agent-Decision vs Operator-Decision Boundary Discrimination](agent-decision-vs-operator-decision-boundary-discrimination-pre-action-gate.md) — DIRECT sibling 2026-05-08; territory-axis composes with this semantic-axis at input-interpretation boundary.
- **PARALLELS** [Lesson — Agent-Authored Content Must Be Flagged](agent-authored-content-must-be-flagged-vs-operator-canonical-the-fabrication-cure.md) — DIRECT sibling 2026-05-08; authorship-axis composes; trio (C02 + C06 + C07) covers input-interpretation boundary.
- **PARALLELS** [Lesson — Agent-Context-Discipline Is Aspirational](agent-context-discipline-is-aspirational-without-enforcement-gates-not-reading-what-exists.md) — DIRECT sibling 2026-05-08; input-side gate.
- **PARALLELS** [Lesson — Class 9 Freeze-After-Correction](freeze-after-correction-is-class-9-of-agent-failure-taxonomy-abdication-as-freeze.md) — DIRECT sibling 2026-05-08; output-side gate.
- **PARALLELS** [Pattern — Correction-as-Calibration Pre-Edit Verification Gate](../../patterns/01_drafts/correction-as-calibration-pre-edit-verification-gate-design.md) — DIRECT sibling 2026-05-08.
- **PARALLELS** [Pattern — Blast-Radius Classification Pre-Action Severity Gate](../../patterns/01_drafts/blast-radius-classification-and-pre-action-severity-gate.md) — DIRECT sibling 2026-05-08.
- **PARALLELS** [Pattern — SB-Tracker Priority-Shift Cycle-Step](../../patterns/01_drafts/systemic-bug-tracker-priority-shift-cycle-step-design.md) — DIRECT sibling 2026-05-08.
- **PARALLELS** [Pattern — PostCompact Orientation Mirror](../../patterns/01_drafts/post-compact-orientation-mirror-and-handoff-doc-completeness-gate.md) — DIRECT sibling 2026-05-08.
- **PARALLELS** [Pattern — Pre-Edit Regression-Test Gate](../../patterns/01_drafts/pre-edit-regression-test-gate-canonical-verified-edit-enforcement.md) — DIRECT sibling 2026-05-08.
- **PARALLELS** [Pattern — Active-Task Anchor and Drift-Detection](../../patterns/01_drafts/active-task-anchor-and-drift-detection-gate-design.md) — DIRECT sibling 2026-05-08.
- **CONSTRAINS** /root/.claude/hooks/output-discipline-guard.sh — extension with sub-axes 3 + 4 detectors
- **CONSTRAINS** /root/.claude/commands/* — sub-axis-1 audit + preventive rename for new commands
- **EXTENDS** SB-120 closure (conditional-clause grammar) — sub-axis 2 covered partial; this lesson generalizes to 4 sub-axes
- **EXTENDS** SB-091 conflation-bug — provides structural detection beyond reactive rename
- **SYNTHESIZES** [Pain-Points Inventory C07 Cluster](../../../raw/notes/2026-05-08-pain-points-inventory-from-root-failed-conversation-master-aggregate.md) — primary source.
- **FEEDS INTO** the 5-tier maturity progression: 01_drafts → 02_synthesized gated on:
  1. Sub-axis 3 detector authored (demonstrative-pronoun ambiguity)
  2. Sub-axis 4 detector authored (paraphrase-without-citation)
  3. Hook extension to /root output-discipline-guard.sh
  4. Cross-project deployment via /install-agent-brain
  5. Test files authored + tests passing
- **Mission served**: 2026-05-06 brain-improvement mandate (failed) → 2026-05-08+ multi-day systematic pain-point resolution; this lesson is C07 cluster's proposed-solution piece.

## Backlinks

(Auto-regenerated by `pipeline post`. Raw-note parent + sibling lessons accumulate this lesson.)

## Self-check — Am I about to commit C07?

> [!warning] Audit procedure for any operator-message processing
>
> Before generating response or invoking any tool:
>
> 1. **Sub-axis 1**: Does the operator's message contain a word that matches a slash-command name? If yes — verify operator typed slash literally; if not, treat as bare-prose continuation.
> 2. **Sub-axis 2**: Does the operator's message contain BOTH immediate-imperative AND future-conditional clauses? If yes — process ONLY the immediate; flag the conditional as hypothesis-to-remember.
> 3. **Sub-axis 3**: Does the operator's message contain "this/that <X>" without explicit referent? If yes — surface ambiguity explicitly; do NOT silently pick a referent.
> 4. **Sub-axis 4**: Am I about to paraphrase operator's words? If yes — quote verbatim instead, OR surface paraphrase + ask operator-confirmation.
> 5. **Cross-axis composition**: did multiple sub-axes trigger simultaneously? Address ALL before acting.
>
> If any sub-axis triggers + agent doesn't surface ambiguity: this lesson's anti-pattern applies. Adopt fix order: detect → surface → wait for clarification → then act.

## Sister-project applicability

Universal across the 5-project ecosystem:
- **root-ghostproxy**: existing 3-detector output-discipline-guard.sh + sub-axes 3 + 4 extensions
- **OpenArms**: harness-engineering — operator-prose vs harness-command conflations possible at every command boundary
- **OpenFleet**: fleet orchestrator — multi-agent conflation surfaces (which agent is "this agent"?); per-agent variant of sub-axis 3
- **AICP**: model-routing decisions — model-routing-prose-vs-config conflations
- **devops-control-plane**: IaC — environment-vs-stack conflations
- **the second-brain second-brain**: this lesson IS authored from the second-brain; demonstrates self-application — the second-brain session committed C07 today (msg #350); deploying the detector here closes the recursive instance

The cure (4-sub-axis discriminator at UserPromptSubmit hook) is portable via `/install-agent-brain` per brain-inheritance pattern.
