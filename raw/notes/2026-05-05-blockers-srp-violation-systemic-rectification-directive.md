---
title: "2026-05-05 — Operator directive: SYSTEMIC FAILURE in blockers register — blockers must NOT be a dumping ground for random items"
type: note
domain: cross-domain
status: raw
confidence: high
created: 2026-05-05
updated: 2026-05-05
sources:
  - id: operator-directive-2026-05-05-blockers-srp-violation-rectify
    type: directive
tags: [note, operator-directive, sacrosanct, verbatim, blockers, srp-violation, systemic-failure, rectification-required, governance, srp]
---

# Operator directive — 2026-05-05 STRONG rectification of blockers SRP violation

## Verbatim

> "a massive systemic failure was just notice, you can look at it and promote after... I hate to see retard blockers... blockers a not made to put random things.... I think we need to strongly rectify that..."

## Decomposition

### A — Sequencing
- "you can look at it and promote after"
- FIRST: look at + diagnose the systemic failure
- THEN: rectify
- THEN ONLY: consider promoting F-evals
- Don't promote F-evals into a broken structure.

### B — Severity
- "a massive systemic failure"
- Not a minor bug. Systemic. Affects the architecture.

### C — Operator's verdict on the current blockers
- "I hate to see retard blockers"
- "blockers a not made to put random things"
- The current blockers register has RANDOM things mixed in.
- Random ≠ blocker. The SRP of blockers.md is violated.

### D — Required action
- "we need to strongly rectify that"
- STRONG rectification — not a soft adjustment.

## Diagnosis (the systemic failure I introduced)

I authored `wiki/governance/blockers.md` with two sections:
1. "Active blockers" — B001-B006 (legit; these are pending-operator-decision tasks blocking active SFIF stage)
2. "Future-decision items" — F001-F011 (NOT blockers; a dumping ground)

The F-items are a **conflation of multiple distinct categories**:
- F001-F003: deferred atomic-task authoring for M011/M012/M013 — NOT blockers, deferred-by-design
- F004: first git commit — NOT a blocker, operator-discretionary state choice
- F005: milestone restructure — refactor opportunity, NOT a blocker
- F006: sub-agent profiles per mode — future enhancement, NOT a blocker
- F007: ✓ resolved
- F008-F011: future enhancements / harness-dependencies / refactor proposals — NOT blockers

**Putting these in `blockers.md` violates the SRP I declared at the top of the file**: *"ONLY tracks items requiring operator input to unblock work."* These items don't require operator input to unblock active work; they're future-state options.

Same conflation now repeated in the test-session agent's F-eval findings: F-eval-3 (M011/M012/M013 have no tasks — observation, not blocker), F-eval-6/7 (NEW Epics — new work, not blockers), F-eval-8 (gap finding — enhancement, not blocker), F-eval-9 (tradeoff observation, not blocker). I was about to promote these into the same broken structure.

## Why this matters (operator's framing)

A blockers register that's a dumping ground:
- Loses operator attention (signal-to-noise drops)
- Hides real blockers behind ceremony entries
- Makes the `/blockers` command useless ("look how much there is to do" when most isn't actionable)
- Defeats the perspective-gap fix the governance layer was supposed to deliver

## Action plan (rectification)

1. Log this directive — done (this file).
2. **Refactor `blockers.md`** to STRICTLY contain items currently blocking work (B001-B006 only). Tighten the SRP to: *"items where operator input is REQUIRED RIGHT NOW to unblock CURRENTLY ACTIVE work."*
3. **Author a new home for the displaced items** — a separate governance doc with its own SRP. Candidate names:
   - `wiki/governance/future-work.md` — deferred work, enhancements, refactor proposals
   - `wiki/governance/findings.md` — observations / gaps / improvements identified during cycles
   - Both? (TBD per category cleanliness)
4. **Move F001-F011 + iteration F-evals to their proper homes** — explicitly NOT blockers.
5. **Update `tools.blockers` + `/blockers` command + mode brain pieces** to reflect the strict definition.
6. **Update the operating-principles "remediation+explanation" pattern** with this lesson (keep registers clean per their SRP — don't let them become dumping grounds).
7. **Register lesson in second brain**: SRP-discipline failure case + correction. Sister-project-applicable.
8. THEN consider F-eval promotion (now moot per the rectified SRP — most F-evals don't belong as blockers either).

## No-conflate guard

- "look at it and promote after" = first rectify, then promote (don't promote into a broken structure).
- "blockers a not made to put random things" = SRP statement. Rectify the SRP.
- "strongly rectify" = thorough fix; don't half-measure.
- Operator did NOT name what the dumping-ground items are; agent diagnoses + cleans up.
