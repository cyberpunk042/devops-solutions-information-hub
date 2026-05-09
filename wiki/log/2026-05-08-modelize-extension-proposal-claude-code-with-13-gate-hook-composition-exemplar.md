---
title: "Modelize Extension Proposal — Extend model-claude-code with 13-Gate Hook-Composition Exemplar"
type: note
note_type: session
domain: log
status: synthesized
confidence: high
created: 2026-05-08
updated: 2026-05-08
sources:
  - id: model-claude-code-canonical
    type: wiki
    file: wiki/spine/models/agent-config/model-claude-code.md
    description: "PRIMARY target. Mature canonical model — agent architecture + extension system + harness engineering + context management. This proposal extends with 13-gate Claude Code hook-composition as concrete production-scale exemplar of multi-axis enforcement."
  - id: comprehensive-13-gate-pattern
    type: wiki
    file: wiki/patterns/01_drafts/comprehensive-agent-action-emission-pipeline-13-gate-composition-architecture.md
    description: "Source pattern — 13-gate Claude Code hook-composition specification across 8 lifecycle events"
  - id: agent-context-discipline-c04
    type: wiki
    file: wiki/lessons/01_drafts/agent-context-discipline-is-aspirational-without-enforcement-gates-not-reading-what-exists.md
    description: "Demonstrates Claude Code PreToolUse + UserPromptSubmit + Read-tool-tracking composition"
  - id: postcompact-orientation-mirror-c05
    type: wiki
    file: wiki/patterns/01_drafts/post-compact-orientation-mirror-and-handoff-doc-completeness-gate.md
    description: "Demonstrates Claude Code PreCompact + PostCompact + state-file communication composition"
  - id: agent-authored-content-flagging
    type: wiki
    file: wiki/lessons/01_drafts/agent-authored-content-must-be-flagged-vs-operator-canonical-the-fabrication-cure.md
    description: "Authorship-flagging discipline — operator-confirmation required"
  - id: prior-modelize-proposals
    type: wiki
    file: wiki/log/2026-05-08-modelize-extension-proposal-skills-commands-hooks-with-13-gate-composition.md
    description: "Sibling modelize proposal #1 — skills-commands-hooks model"
tags: [modelize-proposal, extension-proposal, model-claude-code, 13-gate-hook-composition, hook-lifecycle-events, operator-confirmation-pending, day-arc-2026-05-08, multi-day-pain-point-resolution, mission-2026-05-06]
---

# Modelize Extension Proposal — Extend model-claude-code with 13-Gate Hook-Composition Exemplar

## Summary

Extension proposal for `wiki/spine/models/agent-config/model-claude-code.md` (mature canonical model — Claude Code agent architecture + extension system + harness engineering + context management). Proposes 3 surgical insertions integrating the 2026-05-08 multi-day work as concrete Claude Code hook-composition exemplar: (1) extend "The Extension System" with multi-axis hook composition example, (2) extend "Harness Engineering" with 8-lifecycle-event coverage map, (3) update "State of Knowledge" with 2026-05-08 work. Per agent-authored-content-flagging discipline: agent CANNOT auto-promote canonical content; this proposal IS the operator-confirmation gate.

## Operator-confirmation decision points

Same 4-option set as sibling modelize proposals:
- **A** — apply all 3 proposed extensions
- **B** — apply selectively
- **C** — defer
- **D** — reject + revise

## Why extend model-claude-code specifically

The model is the canonical Claude-Code-specific spine document. Its existing structure documents:
- Agent architecture (the harness engineering)
- Extension system (skills/commands/hooks)
- Context management discipline
- Harness engineering patterns

The 13-gate composition is the production-scale CLAUDE-CODE-SPECIFIC exemplar of how the extension system composes — uses 8 of Claude Code's 26 lifecycle events (SessionStart, UserPromptSubmit, PreToolUse, PostToolUse, Stop, PreCompact, PostCompact, plus existing skills/commands/agent dispatch events). The 13-gate pipeline IS what the extension system enables when scaled to comprehensive agent-discipline enforcement.

## Proposed Edit 1 — Extend "The Extension System" with 13-gate exemplar

**Insert after the existing "Extension System — Summary" sub-section:**

```markdown
### Multi-Axis Hook Composition Exemplar — The 13-Gate Pipeline (NEW 2026-05-08)

A production-scale exemplar of the extension system: 13 hooks composed across 8 of Claude Code's 26 lifecycle events to form a comprehensive multi-axis agent-discipline enforcement pipeline.

**Lifecycle event coverage**:

| Event | Hook(s) | Axis |
|---|---|---|
| SessionStart | session-orient.sh (existing) | Cold-start orientation |
| UserPromptSubmit | mode-enforcement.sh + output-discipline-guard.sh + drift-anchor extension + frustration-quantification extension | Banner state · semantic-conflation detector · drift-anchor framing · frustration measurement |
| PreToolUse | 9 distinct hooks composing across orthogonal axes | input · territory · authorship · severity · regression · drift-audit · stage-class · correction-shape · semantic |
| PostToolUse | post-tool-drift-audit + post-edit-test-gate | drift-event logging · regression-test verification |
| Stop | end-of-cycle-stamp + substance-gate + sb-iteration-gate | output-substance · SB-iteration substance |
| PreCompact | pre-compact.sh + completeness-gate extension | handoff-doc completeness validation |
| PostCompact | post-compact.sh + behavior-gate extension | first-action-must-be-orient enforcement |
| SessionEnd | session-summary.sh (existing) | Closure |

**Composition properties** unique to Claude Code:
- State-file communication via `~/.claude/<file>` (Claude Code's per-user config dir)
- REASON env var bypass (Claude Code permission model)
- Hook output via JSON envelope (additionalContext / systemMessage / hookSpecificOutput)
- Multi-hook ordering per matcher per event

Pattern doc: `wiki/patterns/01_drafts/comprehensive-agent-action-emission-pipeline-13-gate-composition-architecture.md`

The 13-gate pipeline IS the production-scale answer to "how does the Claude Code extension system actually compose for comprehensive enforcement?" beyond the existing Plannotator pattern (1 command + 1 hook).
```

**Diff scope**: ~30 lines added.

## Proposed Edit 2 — Extend "Harness Engineering" with 8-lifecycle-event coverage map

**Insert in "Harness Engineering" section:**

```markdown
### Lifecycle-Event Coverage Map (NEW 2026-05-08)

A harness engineering pattern that emerged 2026-05-08: comprehensive lifecycle-event coverage as a measure of harness maturity. Naive harness = 1-2 events covered. Production harness = 8+ events covered with multi-hook composition per event.

| Maturity tier | Events covered | Example |
|---|---|---|
| Naive | 1-2 (e.g., PreToolUse only) | Simple security envelope |
| Intermediate | 3-5 (PreToolUse + UserPromptSubmit + Stop) | Output discipline + state surfacing |
| Production | 6-8 events with multi-hook composition | 13-gate pipeline (this work) |
| Comprehensive | 8+ events with cross-hook state-file communication + composite metrics | Production scale at autopilot-loop methodology |

The 13-gate pipeline operates at Comprehensive tier — 8 lifecycle events covered + 13 hooks composing + state-file communication contracts + composite operational-compliance metric.

**Empirical evidence**: P1 quantified gap (~25% prose, ~100% hooks) is per-axis; multi-axis Comprehensive-tier pipeline composite is the system-level metric per stress-test.
```

**Diff scope**: ~20 lines added.

## Proposed Edit 3 — Update "State of Knowledge"

**Add after existing entries:**

```markdown
### State of Knowledge — 2026-05-08 update

Multi-day pain-point resolution work (2026-05-08) authored 21+ wiki artifacts addressing a 64-hour /root failed-conversation arc. Specifically demonstrates Claude Code-specific findings:
- 13 hooks composing across 8 of 26 Claude Code lifecycle events
- State-file communication via `~/.claude/<file>` (per-user config dir) for cross-hook state
- REASON env var bypass protocol consistent across all 13 hooks
- Hook output via JSON envelope (additionalContext / systemMessage)
- Multi-hook ordering per matcher per event

Closes empirical evidence gap on production-scale Claude Code hook composition.

Sister-project propagation via `/install-agent-brain` (operator-opt-in cross-project deployment) per brain-inheritance pattern.
```

**Diff scope**: ~15 lines added.

## Composability with prior + future modelize proposals

| Modelize proposal | Target | Status |
|---|---|---|
| #1 — model-skills-commands-hooks extension | `wiki/spine/models/agent-config/model-skills-commands-hooks.md` | Proposed |
| #2 — model-quality-failure-prevention extension | `wiki/spine/models/quality/model-quality-failure-prevention.md` | Proposed |
| **#3 (THIS)** — model-claude-code extension | `wiki/spine/models/agent-config/model-claude-code.md` | Proposed (this log) |
| #4 — super-model integration note | `wiki/spine/super-model/super-model.md` | Forward-anchor — dashboard update |

## Why these specific 3 edits

Per same incremental discipline: model's existing structure preserved; 3 surgical insertions. Operator decides which apply.

## Sources

- Source pattern: `comprehensive-agent-action-emission-pipeline-13-gate-composition-architecture.md`
- Source piece (PostCompact): `post-compact-orientation-mirror-and-handoff-doc-completeness-gate.md`
- Source piece (input-discipline): `agent-context-discipline-is-aspirational-without-enforcement-gates-not-reading-what-exists.md`
- Authorship-flagging gate: `agent-authored-content-must-be-flagged-vs-operator-canonical-the-fabrication-cure.md`
- Sibling proposals: prior #1 + #2 modelize proposals (paths in source list above)
- Target canonical model: `wiki/spine/models/agent-config/model-claude-code.md`

## Tags

[modelize-proposal, extension-proposal, model-claude-code, 13-gate-hook-composition, hook-lifecycle-events, operator-confirmation-pending, day-arc-2026-05-08, multi-day-pain-point-resolution, mission-2026-05-06]
