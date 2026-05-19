---
title: "Standardize Extension Proposal — Hard Rule 16 Auto-Compact Discipline + Auto-Dream-Only Policy"
type: note
note_type: completion
domain: log
status: synthesized
confidence: high
created: 2026-05-08
updated: 2026-05-08
sources:
  - id: auto-compact-detection-failure-priority-directive
    type: file
    file: raw/notes/2026-05-08-auto-compact-detection-failure-and-auto-compact-must-be-disabled-priority.md
    description: "PRIMARY operator directive (sacrosanct verbatim 2026-05-08): 'make sure auto-compact is off always. only auto-dream can be enabled' — sub-layer 1A artifact"
  - id: auto-compact-disable-impl-spec-fire-107
    type: wiki
    file: wiki/patterns/01_drafts/auto-compact-disable-implementation-spec-prevention-layer-for-impl-spec-10-defense-in-depth.md
    description: "PRIMARY parent (Fire 107) — sub-layer 1A specifies CLAUDE.md + AGENTS.md Hard Rule 16; this Fire 112 authors the rule text"
  - id: prior-standardize-extension-proposals
    type: wiki
    file: wiki/log/2026-05-08-standardize-extension-proposal-operating-principles-16th-principle-infrastructure-must-be-used.md
    description: "Sibling — established standardize-extension proposal pattern; this Fire 112 follows same convention"
  - id: opt-claude-md
    type: file
    file: CLAUDE.md
    description: "the second-brain CLAUDE.md current hot-path; 10 Hard Rules currently; this proposal adds HR 16 (skipping HR 11-15 which are /root-side per /root CLAUDE.md)"
  - id: opt-agents-md
    type: file
    file: AGENTS.md
    description: "the second-brain AGENTS.md universal cross-tool restatement; receives mirror of HR 16"
  - id: tier-elevation-pathway-fire-109
    type: wiki
    file: wiki/patterns/01_drafts/tier-elevation-pathway-pattern-systematic-tier-1-to-tier-4-transitions-per-body-piece.md
    description: "Sibling (Fire 109) — this proposal IS the T0→T1 transition for sub-layer 1A per Fire 109 methodology"
tags: [standardize-extension-proposal, hard-rule-16, auto-compact-discipline, auto-dream-only, sub-layer-1a-artifact, day-arc-2026-05-08, multi-day-pain-point-resolution, fire-112]
---

# Standardize Extension Proposal — Hard Rule 16 Auto-Compact Discipline + Auto-Dream-Only Policy

## Summary

Per Fire 107 auto-compact-disable Layer 1 spec sub-layer 1A: brain-layer Hard Rule 16 in CLAUDE.md hot-path + AGENTS.md. Per operator directive 2026-05-08 (sacrosanct verbatim): *"make sure auto-compact is off always. only auto-dream can be enabled"*. This proposal authors the EXACT text of Hard Rule 16 for operator-confirmation. Per the second-brain work-mode.md: changes to CLAUDE.md / AGENTS.md require operator-approval before execution — this fire surfaces the proposal; operator confirms before agent edits hot-path. Per Fire 109 tier-elevation pathway: this proposal IS the T0→T1 transition for sub-layer 1A (designed-only at this point; agent-DRAFT per SB-095).

## Proposed Hard Rule 16 — exact text

### Variant A — Concise (recommended; matches existing HR style)

```markdown
| 16 | **Auto-compact MUST be disabled. Manual `/compact` only. Auto-dream is the only allowed auto-* mechanism.** Per operator directive 2026-05-08 (sacrosanct verbatim): *"make sure auto-compact is off always. only auto-dream can be enabled"*. Auto-compact triggers without operator-confirmation cause body-of-work continuity loss (per Fire 102 real-session evidence 2026-05-08: 5% threshold fire). | Multi-layer enforcement: brain (this rule) + harness (settings.json disable) + env var + PreCompact-hook block (per Fire 107 4-sub-layer spec). Defense-in-depth with Fire 105 PreCompact handoff + Fire 106 PreToolUse-blocker. |
```

### Variant B — Full (more explicit; alternative)

```markdown
| 16 | **Auto-compact MUST be disabled across all layers. Manual `/compact` only.** Auto-compact triggers WITHOUT operator-confirmation. Per operator directive 2026-05-08 (sacrosanct verbatim): *"make sure auto-compact is off always. only auto-dream can be enabled."* Auto-dream is operator-defined (pending Q4 per Fire 107) — provisionally interpreted as: only operator-explicit auto-* mechanisms allowed; auto-compact NOT included. Real-session evidence (Fire 102, 2026-05-08): auto-compact fired at 5% remaining → body-of-work continuity disrupted → operator-catch was sole mitigation. | Layer 1 multi-sub-layer enforcement (brain + harness + env + PreCompact-block per Fire 107 spec). Layer 2 mitigation (PreCompact handoff per Fire 105). Layer 3 enforcement (PreToolUse-blocker per Fire 106). Combined defense-in-depth: auto-compact structurally impossible. |
```

### Recommended: Variant A

Reasoning:
- Matches existing the second-brain CLAUDE.md HR 1-10 style (concise + verbatim quote + cross-reference)
- Variant B is more explicit but exceeds typical hot-path budget
- Per Fire 105 spec sub-layer 1A: hot-path auto-loaded every prompt; concise preferred
- Reference to Fire 107 spec covers the implementation detail

## Numbering rationale (skipping HR 11-15)

Per /root .claude/rules system:
- /root CLAUDE.md and AGENTS.md include Hard Rules 11-15 (extension principles operationalized; per /root operating-principles.md Hard Rules 11-15 mapping)
- the second-brain CLAUDE.md currently has Hard Rules 1-10
- HR 11-15 numbering reserved for sister-project consistency (cross-tool mirror)

Decision: number this Hard Rule **16** (next available; honors cross-project HR slot reservation).
- Alternative: number 11 (next available at the second-brain) — but breaks /root parity
- Alternative: number 11/16 as separate (one for the second-brain, one for cross-tool mirror) — confusing

Recommended: HR 16 across BOTH the second-brain CLAUDE.md and AGENTS.md.

## Insertion location in CLAUDE.md

```markdown
## Hard Rules (every-message hot path)

| # | Rule | Enforcement |
|---|------|-------------|
| 1 | Read command output IN FULL... |
| 2 | When told to execute, execute... |
| 3 | Use dedicated tools... |
| 4 | Operator words are SACROSANCT... |
| 4a | Adding ≠ discarding... |
| 5 | Use `.venv/bin/python`... |
| 6 | URL ingestion → pipeline fetch... |
| 7 | Status claims must inline verification... |
| 8 | Behave FROM the project, not OVER it... |
| 9 | Don't fabricate... |
| 10 | `pipeline post` after every wiki change... |
| **16** | **Auto-compact MUST be disabled... [Variant A text]** | **[Variant A enforcement]** |
```

Insertion: end of table; numbering 16 (skip 11-15 reserved per above).

## Insertion location in AGENTS.md

Mirror in AGENTS.md at parallel position (universal cross-tool restatement).

## Operator-territory boundary (per the second-brain work-mode.md)

```yaml
operator_approval_required:
  - edit CLAUDE.md hot-path: YES (work-mode.md: "Changes to CLAUDE.md ... root-level docs")
  - edit AGENTS.md: YES (work-mode.md: cross-tool universal)
  - this Fire 112 authoring the proposal: NO (drafts in 01_drafts/ + log/ are agent-territory per SB-095)

operator_confirmations_needed_before_edit:
  - confirm Variant A vs Variant B vs operator-revised text
  - confirm HR numbering (16 with skipped 11-15 vs 11 vs other)
  - confirm timing: edit-now vs edit-after-Q1-resolved (auto-dream definition)
  - confirm cross-reference to Fire 107 spec OR include text inline

operator_alternative_paths:
  - operator may edit hot-path directly (operator-explicit override)
  - operator may extend Variant B with operator-known auto-dream definition
  - operator may defer until Q1 (auto-dream) resolved
```

## Composability with body's other layers

| Layer | Composability |
|---|---|
| Fire 107 Layer 1 spec | Sub-layer 1A artifact: this is THE rule-text |
| Fire 105 PreCompact handoff | Layer 2 — handoff captures state IF compaction occurs |
| Fire 106 PreToolUse-blocker | Layer 3 — enforcement IF post-compact session resumes |
| Fire 108 backlog-decomposition | Module M-AC2 Task T-AC2-1: this Fire 112 produces the artifact |
| Fire 109 tier-elevation pathway | T0→T1 transition for sub-layer 1A (concrete instance) |
| Fire 110 question-registry | Q1 (auto-dream definition) blocks Variant B; Variant A interim acceptable |
| .claude/rules/operating-principles.md | Receives the policy if proposal accepted |

## Tier-progression for this proposal

```
T0 (no policy): PRE-FIRE-112 (auto-compact policy not in the second-brain brain)
  ↓ (this Fire 112 authoring)
T1 (designed only): CURRENT — proposal authored as DRAFT
  ↓ (operator confirms; agent or operator edits hot-path)
T2 (partial): one of CLAUDE.md OR AGENTS.md edited but not both
  ↓ (full implementation)
T3 (implemented but not enforced): both edited; agent reads HR 16 each session;
                                   harness still allows auto-compact
  ↓ (Fire 107 sub-layers 1B + 1C + 1D wiring)
T4 (designed + implemented + enforced): full Layer 1 + Layer 2 + Layer 3 of triplet
```

This proposal advances HR 16 from T0 → T1 only. T2-T4 require subsequent operator-confirmation + execution.

## Anti-patterns this proposal avoids

| Anti-pattern | Why bad | How avoided |
|---|---|---|
| Edit CLAUDE.md without operator-approval | Violates work-mode.md PO approval boundary | Proposal in log/ + operator-territory explicit |
| Author rule without verbatim citation | Loses sacrosanct alignment | Variant A includes operator-verbatim quote |
| Use ambiguous "auto-*" without definition | Unclear scope of allowed | Q1 (Fire 110) surfaces auto-dream definition need |
| Renumber HR 1-10 to insert | Breaks existing cross-references | Append at HR 16 (with HR 11-15 reserved) |
| Add to brain without enforcement layer | T1 plateau; agent can ignore under pressure | Cross-references Fire 107 multi-layer enforcement |
| Dual-edit the second-brain brain without cross-tool mirror | the second-brain and other tools diverge | Both CLAUDE.md and AGENTS.md targeted |

## Required Gates (per hook-architecture proposal #2 4th component)

```yaml
required_gates:
  empirically_passed:
    - 2_variant_proposal_drafting: passed (Variant A + Variant B authored)
    - operator_territory_boundary_honored: passed (no actual edit; proposal only)
    - cross_reference_to_fire_107: passed
    - operator_verbatim_citation: passed (sacrosanct quote in both variants)
  pending:
    - operator_empirical_variant_selection: pending (A vs B vs revised)
    - operator_empirical_numbering_confirmation: pending (16 vs alternative)
    - operator_empirical_timing_confirmation: pending (edit-now vs after-Q1)
    - actual_edits_to_CLAUDE_md_and_AGENTS_md: pending operator-approval
    - cross_tool_mirror_validation: pending
    - composability_with_fires_105+106+107_implementation: pending Tasks #25-29 progress
  composite_compliance: standardize-extension-axis stress-test 0% (forward-anchored;
                       this is T1 transition; T2+ depends on operator-action)
```

## Recommended operator action

```
RECOMMENDED:
  1. Operator picks Variant A (recommended) or Variant B or revises
  2. Operator confirms HR numbering (16 reserved)
  3. Operator confirms timing — option (a) edit-now with Variant A's "auto-dream operator-defined provisional"
                                  option (b) defer until Q1 (auto-dream definition) resolved
  4. Once confirmed: agent OR operator edits CLAUDE.md + AGENTS.md
  5. Pipeline post validates 0 errors
  6. Re-run Fire 103 audit on this piece: T0 → T2 (partial: brain only; harness pending)

Recommended timing: option (a) — edit now with Variant A
  Rationale:
    - Don't gate brain-layer rule on harness-investigation findings
    - Variant A's verbatim quote already preserves operator's intent
    - Harness disable (sub-layers 1B+1C+1D) can land later without delaying brain layer
    - Per /loop directive "no rush" + "do this right": brain first; harness second
```

## Closing framing

Per Fire 107 sub-layer 1A specification: brain-layer Hard Rule 16 needed in the second-brain CLAUDE.md + AGENTS.md. Per operator directive 2026-05-08 sacrosanct: auto-compact disable + auto-dream-only policy. This Fire 112 proposes the EXACT TEXT in 2 variants (concise + full) for operator-empirical selection. Per the second-brain work-mode.md: hot-path edits are operator-territory; this fire surfaces proposal; operator confirms before edit. Per Fire 109 tier-elevation pathway: T0→T1 transition complete; T2-T4 depends on operator-action + Layer 1B+1C+1D wiring.

**The agent stands by per /loop directive. Cron continues at 90s cadence. Proposal awaits operator variant-selection + edit-confirmation.**

## Sources

- Auto-compact priority directive: `raw/notes/2026-05-08-auto-compact-detection-failure-and-auto-compact-must-be-disabled-priority.md`
- Fire 107 auto-compact-disable spec: `wiki/patterns/01_drafts/auto-compact-disable-implementation-spec-prevention-layer-for-impl-spec-10-defense-in-depth.md`
- Fire 109 tier-elevation pathway: `wiki/patterns/01_drafts/tier-elevation-pathway-pattern-systematic-tier-1-to-tier-4-transitions-per-body-piece.md`
- Fire 110 question registry: `wiki/log/2026-05-08-question-registry-instance-6-questions-from-auto-compact-priority-sequence-fires-102-109-formal-surface.md`
- the second-brain CLAUDE.md current state (auto-loaded; 10 Hard Rules)
- the second-brain AGENTS.md current state (universal cross-tool restatement)

## Tags

[standardize-extension-proposal, hard-rule-16, auto-compact-discipline, auto-dream-only, sub-layer-1a-artifact, day-arc-2026-05-08, multi-day-pain-point-resolution, fire-112]
