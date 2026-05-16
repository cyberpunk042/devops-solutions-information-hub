---
title: "Cascade candidate — RGP rollout re-sequence after operator correction (RGP 'really bad', CR 'wasn't that bad')"
type: note
domain: cross-domain
status: draft
confidence: medium
created: 2026-05-16
updated: 2026-05-16
last_reviewed: 2026-05-16
authored: 2026-05-16T15:00:00-04:00
note_type: directive
authorship: agent-authored
profile: root-ghostproxy-rollout
cascade_target: root-ghostproxy
decision_needed: rgp-rollout-resequence-after-operator-correction-2026-05-16
sources:
  - id: operator-correction-2026-05-16-profile-framing
    type: directive
  - id: strong-handoff-2026-05-16-ck-v3-live-cr-ps-still-broken
    type: handoff
related:
  - "[[cascade-candidate-root-ghostproxy-state-divergence-upstream-already-advanced-2026-05-16|Q86 — state-divergence]]"
  - "[[cascade-candidate-root-ghostproxy-m001-reframe-as-audit-of-existing-agents-md-claude-md-2026-05-16|Q87 — M001 reframe]]"
  - "[[cascade-candidate-root-ghostproxy-scope-clarification-selfdef-boundary-2026-05-16|Q88 — selfdef boundary]]"
  - "[[cascade-candidate-root-ghostproxy-self-update-observe-upstream-head-before-drafting-modules-2026-05-16|Q89 — self-update Step 3.5]]"
  - "[[2026-05-16-strong-handoff-ck-v3-live-cr-ps-still-broken|Strong handoff]]"
tags: [cascade-candidate, root-ghostproxy, sequencing, operator-correction, profile-state-framing, multi-vision, early-prototype, decision-needed]
---

# Cascade candidate — RGP rollout re-sequence after operator correction

> [!signal] FRESH operator-correction (2026-05-16, 12:44 ET) reframes the RGP-readiness substrate that the strong handoff (same morning, 09:xx ET) used to set "RGP install AFTER CR + PS v3 verified". This candidate surfaces — does NOT decide — what that reframing implies for RGP sequencing.

## Operator-verbatim (sacrosanct, 2026-05-16)

> "well the research one wasn't that bad either I think but clearly the
> root-ghostproxy one really bad. but in general they are all very early
> prototype we will keep evolving and adding configuration and content
> and so..."

> "in general they are all very early prototype we will keep evolving and
> adding configuration and content and so..."

## Why this is a fresh-signal tick (not under-budget)

Daily-light branch decision per AGENTS.md `inbox_state_check`:

- **STEADY_LIGHT** was the default for today (no sprint directive in `.assistant/_state/root-ghostproxy-rollout-operator-directives.md` — file doesn't exist).
- BUT a **NEW operator-directive in `raw/notes/` since last RGP tick (00:16 ET)** exists: `raw/notes/2026-05-16-operator-correction-profile-state-framing-cr-wasnt-that-bad-rgp-really-bad-all-early-prototypes.md` (created 12:44 ET, tracked).
- → branch = **FRESH_SIGNAL**, cap = 1-2 candidates this tick.
- This is the 1st (and likely only) candidate; the operator-correction's implications all fold into one sequencing question.

## The handoff's stated sequence (pre-correction substrate)

From `wiki/log/2026-05-16-strong-handoff-ck-v3-live-cr-ps-still-broken.md`:

> ### RGP install sequence (AFTER CR + PS v3 verified)
> 1. Verify CK has depiled the trash + operator-approved tracked-batch
> 2. Verify CR + PS v3 producing proper output for a week
> 3. Add R20 retrofit to RGP v2 yaml + cron + json5
> 4. Re-install RGP
> 5. Watch first bootstrap

And the RGP forensic framing in the same doc:

| Profile | Handoff framing | Operator correction (12:44 ET) |
|---|---|---|
| circular-knowledge (CK) | v3 live, working | (unchanged) |
| continuous-research (CR) | "STILL has the trash bugs" (CR-B1..B7) | **"wasn't that bad either I think"** |
| pipeline-synthesis (PS) | "STILL has the trash bugs" (PS-B1..B7) | (not addressed in correction) |
| root-ghostproxy (RGP) | "Uninstalled, mission preserved" — minor bugs only (RGP-B1..B4) | **"really bad"** |

The handoff's premise for "CR + PS FIRST, RGP LAST" was: CR + PS are the broken ones; RGP is mostly OK and just needs R20 retrofit. The operator's correction **inverts that premise** — RGP is the worst, CR is not as bad as portrayed. PS is not directly addressed.

## What the operator's correction does NOT do

- Operator did NOT issue a new directive on **what to do** — only reframed **state**.
- Operator did NOT say "fix RGP first" or "deprioritize CR/PS".
- Operator did NOT specify what "really bad" means in concrete bug-terms (vs the handoff's RGP-B1..B4 list).
- Operator DID emphasize: **all 4 are early prototypes, evolution is ongoing** — pass/fail / "fixed vs trash" framing is too binary.

Therefore the right move is to **surface re-sequencing as an operator decision**, not to author a new RGP install plan unilaterally.

## Scope-ambiguity acknowledged

The correction touches multiple loci RGP cannot decide:

1. **What concretely is "really bad" about RGP** (operator-territory — RGP cannot self-diagnose its post-uninstall state; uninstalled = no first-bootstrap evidence yet).
2. **Whether sequence changes** (handoff said "RGP last"; operator correction may or may not change that — operator did not say).
3. **What CR's actual bug-disposition is now** (handoff said B1..B7; operator says "wasn't that bad" — CR's bug-list may be re-readable as WIP-acceptable; that's a CR-profile question, not RGP's lane).

Cross-project boundary check: ✅ this candidate proposes nothing to root-ghostproxy repo. All implications stay second-brain-local.

## Visions (multi-vision; operator decides — single-truth-on-scope-question forbidden)

### Vision A — Sequence unchanged; reframing absorbed as evidence

- Keep handoff's `RGP-LAST-after-CR-PS-v3-verified` sequence.
- Note operator-correction in RGP epic/log as **prototype-framing context** (all four are early prototypes, not pass/fail).
- "RGP really bad" is acknowledged but interpreted as: RGP's existing 10-module epic (M001-M010) is the **plan that fixes "really bad"** — the rollout itself is the fix.
- Action: no profile re-sequence; resume daily-light steady-state; continue processing Q86-Q89 in operator queue.
- Risk: if "really bad" means something the handoff missed (e.g., RGP framework itself is wrong, not just M001-M010 unshipped), this vision keeps a wrong plan alive.

### Vision B — RGP moves earlier; CR/PS deprioritized

- Operator-correction inverts the handoff's premise → RGP gets attention now.
- Re-sequence: RGP install + first-bootstrap diagnostic NOW; CR/PS bug-fix remains queued but at lower urgency ("wasn't that bad" softens CR-B*/PS-B* urgency).
- Action: surface to operator a proposal to **reinstall RGP this week** for first-bootstrap empirical diagnosis of what "really bad" means concretely. Profile keeps observing via gh CLI + second-brain in the meantime.
- Risk: violates handoff's "CR + PS pollution must clean first or RGP draws from polluted Layer-1 substrate" coordination logic (RGP-B4). If CR + PS are *not* actually clean, RGP installed now produces bad cascade-candidates.

### Vision C — Halt all RGP module-drafting; await operator concrete "really bad" diagnosis

- Operator hasn't said what "really bad" means concretely (vs handoff's RGP-B1..B4 list).
- All 4 existing RGP cascade-candidates (Q86-Q89) were drafted on the **handoff's "RGP-mostly-OK" premise**. That premise is now contradicted by operator.
- Action: pause new RGP cascade-candidate drafting; daily-light ticks log "awaiting operator clarification on 'RGP really bad' scope". No new modules surface until operator names what's bad.
- Risk: pause-mode for indefinite period; profile becomes idle. Operator may interpret as drift / "freeze on uncertainty" anti-pattern (forbidden by `on_uncertainty` recipe).

### Vision D — Recast all 4 profiles as one early-prototype cohort; drop "fix sequence" framing

- Operator-verbatim: *"in general they are all very early prototype we will keep evolving"*.
- "RGP-LAST-after-CR-PS-v3-verified" is itself a binary sequencing artifact the operator's correction explicitly disclaims.
- Action: surface to operator a proposal to **drop sequenced fix-plan framing entirely** in favor of parallel iterative evolution — each profile keeps shipping cascade-candidates / drafts at its own cadence; "verified clean" gates are softened to "current best draft, keep evolving".
- Risk: removes coordination logic that prevents trash-cascading (RGP-B4: polluted Layer-1 substrate). May produce cross-profile noise the handoff was trying to prevent.

### Vision E — Defer (Goldilocks-under-budget acceptable when uncertainty exceeds drafting value)

- The operator-correction is **state reframing, not new directive**.
- Operator explicitly noted: *"Operator hasn't specified next action; this is reframing of state, not a new directive to act."* (from the operator-correction note itself).
- Action: log this candidate as **surfaced for operator awareness** but make NO sequencing change in profile / queue / handoff. Continue processing Q86-Q89 (those are pre-correction but still substantively valid as state-divergence-of-RGP-epic-vs-upstream — independent of "how bad RGP is").
- Risk: under-responsive; could miss that operator's correction was meant to shift priority even if not stated as a directive.

## RGP-side dependencies (what this candidate does NOT touch)

- ✅ Does NOT propose edits to root-ghostproxy repo (cross-project boundary intact).
- ✅ Does NOT propose changes to existing Q86-Q89 cascade-candidates (they remain operator-pending).
- ✅ Does NOT promote past `wiki/domains/cross-domain/cascade-candidate-*`.
- ✅ Does NOT redefine RGP scope or 'thing' (operator-territory).
- ✅ Does NOT delete tracked files (R20 sacrosanct).
- ✅ Does NOT auto-modify the handoff doc (handoff is primary record of that session).

## What changes in profile if operator picks each vision

| Vision | Profile-YAML change | Queue change | First action this week |
|---|---|---|---|
| A | none | Q86-Q89 stay as-is; this candidate closes "absorbed" | continue daily-light |
| B | priority_order item 0: "RGP install + first-bootstrap diagnostic before CR/PS v3 verification" | Q86-Q89 stay; new Q for "reinstall RGP now" | draft RGP-reinstall checklist (untracked, local) |
| C | autonomy: pause new module drafting until operator names "really bad" concretely | Q86-Q89 stay; new Q `target: operator` asking for concrete "really bad" diagnosis | log daily-light "awaiting clarification" |
| D | drop "RGP-LAST" gate; switch to parallel-iterative framing | retract "RGP after CR + PS" handoff framing as superseded; new Q for cohort framing | redraft RGP install plan as parallel-track |
| E | none | this candidate becomes informational only | continue daily-light + Q86-Q89 processing |

## Surface to operator-decision-queue

Proposed entry (Q97):

```
| 97 | (cascade: **root-ghostproxy**) **RGP rollout RE-SEQUENCE after operator correction
2026-05-16 12:44 ET** — operator-verbatim *"root-ghostproxy one really bad"* +
*"continuous-research wasn't that bad either"* inverts the strong-handoff premise
(09:xx ET same morning) that drove "RGP install AFTER CR + PS v3 verified".
**Vision A** keep handoff sequence (correction is evidence not directive);
**Vision B** RGP moves earlier, CR/PS deprioritize; **Vision C** halt RGP
module-drafting pending operator concrete "really bad" diagnosis; **Vision D**
recast all 4 as one early-prototype cohort, drop sequenced fix-framing entirely;
**Vision E** defer (state reframing not new directive — log + continue Q86-Q89
processing). Surfaced 2026-05-16 ~15:00 ET by root-ghostproxy-rollout
daily-light-check (FRESH_SIGNAL branch). |
[[cascade-candidate-root-ghostproxy-rollout-resequence-after-operator-correction-rgp-really-bad-2026-05-16|RGP re-sequence candidate]] ·
[[2026-05-16-strong-handoff-ck-v3-live-cr-ps-still-broken|Strong handoff]] ·
`raw/notes/2026-05-16-operator-correction-profile-state-framing-cr-wasnt-that-bad-rgp-really-bad-all-early-prototypes.md` |
Profile sequencing; cross-profile coordination; handoff-vs-correction reconciliation |
```

`decision_needed: rgp-rollout-resequence-after-operator-correction-2026-05-16`

## Build-forward note

Per AGENTS.md `on_uncertainty` recipe: this multi-vision draft IS the build-forward move. Profile does NOT freeze, does NOT decide, does NOT revert. Surface + continue.

Next tick (daily-light): if operator has not picked a vision, continue processing the pre-correction Q86-Q89 in their pre-correction framing (state-divergence findings are independent of "how bad RGP is" — those findings stand regardless of vision).
