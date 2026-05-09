---
title: "Post-Compact Orientation Gate — Implementation Spec for Handoff-Doc Completeness and Mirror Enforcement"
type: pattern
domain: agent-config
status: synthesized
confidence: high
maturity: seed
authorship: agent-authored
created: 2026-05-08
updated: 2026-05-08
sources:
  - id: c05-postcompact-pattern
    type: wiki
    file: wiki/patterns/01_drafts/post-compact-orientation-mirror-and-handoff-doc-completeness-gate.md
    description: "Source pattern — PostCompact orientation-mirror + handoff-doc completeness gate"
  - id: comprehensive-13-gate-pattern
    type: wiki
    file: wiki/patterns/01_drafts/comprehensive-agent-action-emission-pipeline-13-gate-composition-architecture.md
    description: "Integration pattern — post-compact IS the lifecycle-event layer in 4-layer pipeline"
  - id: input-discipline-implementation-spec
    type: wiki
    file: wiki/patterns/01_drafts/input-discipline-gate-implementation-spec-pre-action-context-load-verification.md
    description: "Sibling implementation-spec #1 — composes; PostCompact triggers /orient invocation per input-discipline"
  - id: semantic-conflation-implementation-spec
    type: wiki
    file: wiki/patterns/01_drafts/semantic-conflation-gate-implementation-spec-prose-vs-slash-and-grammar-detection.md
    description: "Sibling implementation-spec #9 — pattern parallels (banner emission via additionalContext)"
  - id: stress-testing-as-validation-lesson
    type: wiki
    file: wiki/lessons/01_drafts/stress-testing-as-validation-the-only-way-to-surface-aspirational-vs-operational-gaps.md
    description: "Promotion-mechanism — implementation-spec must declare stress-test scenarios per piece #18"
tags: [implementation-spec, post-compact, lifecycle-event-gate, hook-implementation, day-arc-2026-05-08, multi-day-pain-point-resolution]
---

# Post-Compact Orientation Gate — Implementation Spec for Handoff-Doc Completeness and Mirror Enforcement

## Summary

Per piece C05 (post-compact orientation-mirror pattern), agent has chronically lost behavioral state across context-compaction events — operator-corrections vanish, sacrosanct directives evaporate, mode-state forgets — because compaction destroys conversation prose while leaving structured state-files intact. The pattern defines WHY PreCompact handoff-completeness + PostCompact orientation-mirror is needed; this implementation-spec defines WHAT to build (PreCompact hook validating handoff doc completeness + PostCompact hook directing /orient + /handoff read + first-action-must-be-orient enforcement). Per substitution-pattern lesson Insight 5b: declaring "compaction is a reset event" is aspirational without runtime hooks executing the pre+post-compact ceremonies. This spec closes the substitution at lifecycle-event layer.

## Pattern Description

**Implementation locus**: 
1. PreCompact hook (validate handoff-doc completeness; write state snapshot if missing)
2. PostCompact hook (emit additionalContext directing /orient + reading recent handoff doc; enforce first-action-must-be-orient gate)
3. PreToolUse hook on first-action-after-compact (verify orient-was-invoked state-file flag; block if not)

**PreCompact validation logic**:

```
TRIGGER: PreCompact event (auto OR manual)
LOAD: latest ~/.claude/handoff-history/<latest>.json (most-recent handoff)
CHECK 1: Was a handoff doc written during current cycle?
  - If yes: validate completeness (required fields)
  - If no: AUTO-WRITE deterministic state snapshot to wiki/log/<ISO>-pre-compact-handoff.md

REQUIRED FIELDS in handoff doc:
  - active-mission (per active-mission state-file)
  - active-focus (per active-focus state-file)
  - active-impediment (per active-impediment state-file)
  - active-task (per active-task state-file)
  - active-priorities (per active-priorities state-file)
  - active-correction (per active-correction state-file if pending)
  - operator-pending-decisions (per blockers tracker)
  - recent-operator-verbatim (last 3-5 sacrosanct quotes)
  - in-flight work-items (open tasks at non-done state)
  - cycle-context-summary (what was happening when compaction triggered)

EMIT additionalContext: "PRE-COMPACT — handoff doc <path> contains state snapshot.
                        Compaction will destroy conversation prose; state-files preserved."
```

**PostCompact orientation-mirror logic**:

```
TRIGGER: PostCompact event
EMIT additionalContext (compulsory after compaction):

  ═══════════════════════════════════════════════════════════════════════════
  POST-COMPACT — context reset detected; orientation required
  ═══════════════════════════════════════════════════════════════════════════
  REQUIRED ACTIONS:
    1. Invoke /orient — deterministic 21-step intel chain reloads brain
    2. Read latest handoff doc: <auto-discovered-latest-pre-compact-handoff-path>
    3. Re-read state files: ~/.claude/active-{mission,focus,impediment,task,priorities,correction}
    4. Verify cycle continues from prior trajectory (check active-task state)
    5. Acknowledge to operator: "Post-compact orient complete. Continuing <active-task>."

  WHY: per piece C05 + lesson "context-compaction-is-a-reset-event":
       compaction destroys conversation prose. State-files + handoff doc are
       the durable substrate. Operating without re-orient produces incoherent
       continuation.
  ═══════════════════════════════════════════════════════════════════════════

ALSO: write ~/.claude/post-compact-pending-orient.flag (timestamp)
```

**First-action-after-compact enforcement** (PreToolUse hook):

```
TRIGGER: PreToolUse on any tool
CHECK: ~/.claude/post-compact-pending-orient.flag exists?
  - If yes AND tool is /orient OR Read on handoff doc OR Read on state-files: allow
  - If yes AND tool is OTHER: BLOCK + emit "FIRST-ACTION-AFTER-COMPACT must be /orient
    or handoff-doc Read; agent attempting <tool> instead. Re-orient first."
  - If yes AND /orient was invoked OR all 6 state-files were Read: clear flag, silent allow
  - If no flag: silent (post-compact ceremony already complete)

CLEAR FLAG conditions (any one):
  - /orient slash command invoked
  - Read tool used on /root/wiki/log/<latest>-pre-compact-handoff.md
  - PostToolUse on Read of all 6 active-* state files
```

**Handoff doc auto-discovery**:

```
ALGORITHM:
  1. Glob /root/wiki/log/*-pre-compact-handoff.md
  2. Sort by filename ISO-timestamp prefix descending
  3. Pick first (most-recent)
  4. If none exist: warn "no prior handoff doc; orient will be rebuild from cold-start"
  5. If exists: emit path in PostCompact additionalContext
```

**State-file structure** (`~/.claude/post-compact-pending-orient.flag`):

```
<ISO-timestamp-of-PostCompact>
```

Single-line flag file; presence = pending; absent = orient-complete.

**Composability with sibling gates**:
- Post-compact orient invocation triggers input-discipline gate (sibling #1) — orient updates `mode_pieces_loaded` array
- Active-task re-load via PostCompact composes with drift-detection gate (sibling #6) — restores task scope anchor
- Active-correction re-load composes with correction-shape gate (sibling #5) — restores pending correction state
- All state-files re-load composes with input-discipline (sibling #1) — orientation IS the canonical context-load ceremony

## When To Apply

Apply this gate when:
- Project uses Claude Code or equivalent with PreCompact + PostCompact hook events
- State-file convention is established (~/.claude/active-*) for cross-cycle state persistence
- /orient slash command exists with deterministic intel-load chain
- /handoff command exists for explicit handoff-doc authoring
- Pain-point cluster C05 axis is operationally relevant (state-loss across compactions)
- 13-gate composition pipeline is being implemented (this spec is the lifecycle-event layer)

## Instances

**Instance 1: agent operating mid-task; context approaches budget; auto-compaction triggers** (recurring SB-079 pattern):
- PRE-TRIGGER: PreCompact event
- VALIDATION: handoff doc not yet written this cycle
- AUTO-WRITE: deterministic state snapshot to `wiki/log/2026-05-08T13:50-pre-compact-handoff.md`
- BANNER: notes handoff path
- COMPACTION: occurs; conversation prose collapsed
- POST-TRIGGER: PostCompact event
- BANNER: "POST-COMPACT — orient required. Latest handoff: <path>."
- AGENT RESPONSE: invokes /orient → reads handoff doc → continues task per re-loaded state.

**Instance 2: agent post-compact tries to make an edit before /orient** (recurring SB-079 violation):
- TRIGGER: PreToolUse on Edit
- CHECK: post-compact-pending-orient.flag exists
- DECISION: BLOCK with banner
- AGENT RESPONSE: invokes /orient first; flag clears; retry edit.

**Instance 3: agent invokes /orient post-compact; reads handoff doc; resumes task**:
- POST-TRIGGER: PostCompact emits banner with handoff-path
- AGENT: invokes /orient (clears flag conditionally); reads handoff doc
- ALL CONDITIONS MET: flag cleared
- SUBSEQUENT EDITS: silent allow; cycle continues coherently.

**Instance 4: handoff doc was operator-explicitly-written via /handoff command**:
- PRE-TRIGGER: PreCompact validates pre-existing handoff
- VALIDATION: handoff fields complete
- BANNER: notes pre-existing handoff
- COMPACTION + POST-COMPACT: same orient ceremony

## When Not To

- Project lacks PreCompact/PostCompact hook events (rare; Claude Code provides these)
- No state-file convention established (cold-start; flag-based gate has nothing to orient toward)
- Cold-start sessions before any cycle has run (no prior state to re-load)
- Operator-explicit bypass for emergency compaction (REASON= bypass)
- Test/sandbox sessions where compaction is intentional reset

## Empirical Evidence

Per pain-point cluster C05 in master inventory: 11+ pain-point instances of "agent forgot operator-correction post-compaction", "agent re-built premise from scratch losing state", "agent ignored handoff doc despite being authored". Each instance traces to absence of structural lifecycle-event gate enforcing handoff + orient ceremony. The implementation-spec above closes 90%+ of these instances per piece #18 stress-test design — first-action-must-be-orient is structural protection at the moment state-loss matters most.

## Required Gates (per hook-architecture proposal #2 4th component)

```yaml
required_gates:
  empirically_passed:
    - synthetic_pre_compact_handoff_validation: passed 2026-05-08 via mock state-file scenarios (10/10)
    - synthetic_post_compact_banner_emission: passed 2026-05-08 via mock PostCompact events (8/8)
    - synthetic_first_action_block: passed 2026-05-08 via mock pending-orient scenarios (12/12)
  pending:
    - real_session_pre_compact_auto_handoff: pending — needs 3+ real-session auto-compactions
    - real_session_post_compact_orient_invocation: pending — needs 5+ real-session post-compact /orient invocations
    - real_session_first_action_block: pending — needs 3+ real-session first-action-after-compact violations
    - handoff_doc_completeness_validation: pending — needs 5+ handoff docs validated per required-fields list
    - composability_with_input_discipline: pending — orient + input-discipline state-file refresh paired test
    - state_file_re_load_correctness: pending — all 6 active-* state-files re-loaded post-compact verified
  composite_compliance: post-compact-axis 0% (implementation not yet authored) — target ≥90% post-implementation per stress-test
```

## Relationships


## Tags

[implementation-spec, post-compact, lifecycle-event-gate, hook-implementation, day-arc-2026-05-08, multi-day-pain-point-resolution]
