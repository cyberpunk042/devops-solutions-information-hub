---
title: "Lesson — Structural-but-not-surfaced failure mode: a fix that lands in a register but isn't visible at use-time recurs as a symptom"
type: lesson
domain: cross-domain
status: synthesized
confidence: high
maturity: mature
layer: 2
created: 2026-05-05
updated: 2026-05-05
sources:
  - id: operator-directive-2026-05-05-journey-plan-cursor-recurrence
    type: directive
    project: root-ghostproxy
    path: /root/wiki/log/2026-05-05-journey-plan-cursor-not-surfaced-symptom-recurrence.md
    description: "Operator: 'this again reveal one other symtom I had talked about where the journey and plan and cursor in them does not seem clear'"
  - id: companion-lesson-verbal-acknowledgment
    type: wiki
    file: wiki/lessons/03_validated/enforcement-compliance/verbal-acknowledgment-is-not-a-fix-bug-fix-requires-structural-artefact.md
    description: "Composes with verbal-acknowledgment lesson — that lesson says 'verbal isn't structural'; this one says 'structural-but-invisible-at-use-time isn't a fix either'"
tags: [lesson, structural-not-surfaced, symptom-recurrence, surface-discipline, status-block, journey-plan-cursor, sister-project-applicable, layer-2, agent-self-discipline]
---

# Lesson — Structural-but-not-surfaced failure mode

## Summary

A fix that lands as STRUCTURE (file authored, register updated, doc created) but isn't SURFACED at the operator's moment of interaction is **not a fix**. The symptom recurs because the operator can't see what was supposedly fixed. This is a third failure variant beyond verbal-only fixes and unaddressed-bugs: the fix EXISTS in project state but the operator can't reach it inline.

The discipline: structural fixes must be paired with surface mechanisms — inline status blocks, /orient reports, hook output, slash-command emit — so the fix is REACHABLE at use-time, not just findable by file read.

## Context

This lesson applies when:
- A previous operator directive resulted in authoring a register/doc/governance file (structural fix landed)
- The same symptom recurs in a later session/turn — operator says "this again" or "I told you about this"
- Investigation reveals: the fix EXISTS in project state but isn't surfaced at the moment of operator interaction
- Common shape: governance docs at `wiki/governance/<topic>.md` with rich content, but cycle status blocks don't echo them

Does NOT apply to: cases where the structural fix wasn't actually authored (those are unaddressed-bug shape); cases where the fix is genuinely surfaced but operator hasn't read it (different problem — operator-state, not agent-state).

## Insight

> [!success] **Three distinct failure-variants of the fix-shape spectrum**
>
> | Variant | Structural artefact? | Surfaced at use-time? | Shape of recurrence |
> |---|---|---|---|
> | **Verbal-only fix** | No | No | Operator: *"you didn't fix it"* — bug stays in state |
> | **Structural-but-not-surfaced** | Yes | No | Operator: *"this AGAIN"* — fix exists but invisible at use-time |
> | **Genuine fix** | Yes | Yes | Operator sees the fix in cycle output → no recurrence |
>
> The structural-but-not-surfaced variant is subtle because the agent CAN truthfully say *"I authored the fix."* But the operator's experience hasn't changed — the symptom presents identically. The bug is in the SURFACE layer, not the structural layer.

> [!tip] **Structural artefacts have two reach modes**
>
> Structural artefacts have **two reach modes** — findable (operator can navigate to it via file path / search) and inline (visible at the moment of relevant interaction). Findable-only is sufficient for some content (reference material, deep technical detail). Inline is required for content the operator needs at decision-time (current state, pending blockers, journey position). Decide PER ARTEFACT which reach mode matters.

## Evidence

Empirical, 2026-05-05 root-ghostproxy session (multiple cycles):

- **Earlier directive**: *"there should be a clear channel of the blockers that cummulate that require my inputs and the tracking of the progress and the view of journey and current position and planning"*
- **Structural fix landed**: authored `governance/blockers.md`, `governance/progress.md`, `governance/decisions.md`; authored `/blockers`, `/progress`, `/decisions` slash commands
- **But**: end-of-cycle status blocks emitted by autopilot didn't echo journey/plan/cursor — operator had to invoke commands or read files to see position
- **Symptom recurred**: operator: *"this again reveal one other symtom I had talked about where the journey and plan and cursor in them does not seem clear"*
- **Diagnosis**: structural was correct; surface was missing
- **Fix**: extend `tools/cycle.py` status block emit with JOURNEY / PLAN / CURSOR sections; status blocks now SURFACE the structural register inline

Registered in /root as SB-075 in the systemic-bugs tracker.

## Applicability

| Domain | How This Lesson Applies |
|--------|----------------------|
| **Governance registers** | Auditable file is necessary; inline-surface in cycle reports is needed for items the operator decides on |
| **Pending operator decisions** | File at `governance/blockers.md` is reference; inline surfacing in status blocks + decision-package format is what reaches operator |
| **Progress / journey / cursor** | `governance/progress.md` is reference; inline JOURNEY/PLAN/CURSOR sections in status blocks are what operator sees |
| **Hook fixes** | Hook script in `.claude/hooks/` is structural; hook OUTPUT (status I/O, additionalContext) is the surface |
| **Brain-file rules** | Rule file at `.claude/rules/<topic>.md` is structural; the agent's behavior CITING the rule when relevant is the surface |
| **Lesson / pattern fixes** | Lesson at `wiki/lessons/03_validated/<topic>.md` is structural; agent referencing it at relevant moments is the surface |
| **NOT applicable** | Reference material that doesn't need to be inline (deep technical detail, source-syntheses); cases where the operator has already read and acted on the fix |

## The discipline (operationalized)

When authoring a structural fix:

1. **Author the structural artefact** (file, register, hook, rule) — necessary
2. **Decide reach mode** — findable-only or inline?
3. **If inline**: identify the surface mechanism — cycle status block, /orient report, hook output, slash-command emit
4. **Author the surface** — extend the relevant tool/hook/command to echo the structural content at the moment of operator interaction
5. **Verify the loop**: operator's next interaction with the relevant context shows the fix's content inline

Skipping step 3-4 produces structural-but-not-surfaced. Operator notices the symptom recurrence eventually; the fix has to be re-surfaced reactively.

## Distinguishing the three failure variants

| If operator says... | Most likely failure variant | Right next move |
|---|---|---|
| "You didn't fix it" / "I told you to do X" | Verbal-only | Author the structural artefact (file, register, hook, rule) |
| "This AGAIN" / "I told you about this" | Structural-but-not-surfaced | Find the existing artefact + add surface mechanism |
| "What about Y from earlier?" | Possibly structural-but-not-surfaced (tracker not surfaced) OR sidetrack-recovery | Check if the artefact exists; if yes, surface it; if no, author it |
| "How is X doing?" | Possibly findable-only when inline expected | Surface in status block + answer with content |

The operator's word choice signals the variant. Read carefully.

## Surface mechanisms (catalog)

| Surface mechanism | Where | When to use |
|---|---|---|
| Cycle status block | End of `/cycle` execution | Recurring autopilot state (pending decisions, blockers, journey, cursor, progress) |
| ORIENT REPORT | `/orient` command output | Cold-start + post-compact intelligence |
| Slash-command emit | `/blockers`, `/progress`, `/decisions`, `/status` | Operator-on-demand surfacing |
| Hook additionalContext | SessionStart / PostCompact / etc. | Lifecycle-event-driven directive injection |
| Hook stdout | SessionStart / SessionEnd / etc. | Operator-visible status output (security envelope, summary) |
| Mode brain-piece content | Active-mode cycle steps | Mode-aware surfacing per lens |
| Inline citation in agent response | Agent's prose | Single-turn surfacing of relevant rule/lesson |

A structural fix should be paired with at LEAST ONE surface mechanism for any content the operator needs at decision-time.

## Anti-patterns

| Anti-pattern | Why bad |
|---|---|
| Author file + assume operator will navigate to it | Operator can't be expected to file-traverse for inline-required content |
| "It's in the register / governance / docs" | If symptom recurs, register-only didn't reach |
| Surface ONCE then drop | Surfacing should be PERSISTENT for inline-required content (every cycle, every orient) |
| Surface in wrong moment (e.g., end-of-session for during-session decisions) | Timing matters; surface AT use-time, not after |
| Surface mechanism doesn't match content reach mode | Don't put deep reference content inline (clutter); don't put decision-blocking content in deep reference (invisible) |

## Sister-project applicability

Universal. Every project where structural fixes land in registers/files/hooks faces this risk. The structural fix discipline (author + decide reach + add surface) applies to:
- root-ghostproxy (first empirical case)
- /opt second-brain (governance-register adoption candidate; same principle applies if /opt adopts those)
- OpenArms, OpenFleet, AICP, devops-control-plane (universal)

## Relationships

