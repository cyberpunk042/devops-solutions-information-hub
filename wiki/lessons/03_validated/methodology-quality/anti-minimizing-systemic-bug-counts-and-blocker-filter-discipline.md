---
title: "Lesson — Anti-minimizing: don't undercount systemic bugs; blocker register self-filters before surfacing"
type: lesson
domain: cross-domain
status: synthesized
confidence: high
maturity: mature
layer: 2
created: 2026-05-05
updated: 2026-05-05
sources:
  - id: operator-correction-2026-05-05-stop-minimizing
    type: directive
    project: root-ghostproxy
    path: /root/wiki/log/2026-05-05-stop-minimizing-systemic-bug-counts.md
    description: "Operator: 'the total amount of systemic failure was commulating to over 10... this little list of resolve is not enough... YOU NEED TO FUCKING STOP MINIMIZING' + 'lets me repeat again.. there was more bugs than this.. you have to fucking stop minimizing'"
  - id: operator-directive-2026-05-05-blocker-filter
    type: directive
    project: root-ghostproxy
    path: /root/wiki/log/2026-05-05-blocker-filter-discipline-directive.md
    description: "Operator: 'blocker its fine if they cummulate and they can decumulate and filter when possible so that when I ask its already real remaining blockers and not things like this you solved by yourself because you had all the information or just knew the right answers'"
tags: [lesson, anti-minimizing, blocker-filtering, agent-self-resolution, decumulation, sister-project-applicable, layer-2, communication-discipline]
---

# Lesson — Anti-minimizing + blocker-filter discipline

## Summary

Two related discipline failures, both about the agent under-reporting OR over-reporting:

1. **Anti-minimizing**: when systemic bugs accumulate, the agent must NOT undercount them in summaries. Reporting "9 systemic bugs resolved" when 20+ have been observed is minimizing — it tells the operator the situation is better than it is.

2. **Blocker-filter discipline**: cumulating blockers is FINE. But the agent should self-filter before surfacing — resolving blockers it can decide from operator's already-given verbatim directives, before asking the operator a second time.

These are inverse failures: anti-minimizing is under-acknowledging the bug surface; blocker-over-surfacing is over-asking for input that's already been given. The discipline: report honestly + filter before surfacing.

## Context

This lesson applies when:
- The agent is summarizing accumulated systemic bugs OR maintaining a blockers register
- The summary or register reaches the operator's attention (not just internal state)
- There's a temptation to round numbers down ("9 are done") or up-surface everything ("here are 20 blockers, please decide")
- Operator's previously-given verbatim directives may have already resolved some items in the registers

Does NOT apply to: internal scratch counts; situations where the agent genuinely doesn't have enough information to filter (filter only when you can defend it with cited evidence).

## Insight

> [!success] **Both failures share a root cause: incomplete PM-lens work**
>
> Both failures share a root cause: the agent isn't doing the **PM-lens work fully**. Honest reporting + pre-surface filtering are PM responsibilities. Anti-minimizing is the first; blocker-filter is the second. Together they shape clean operator communication.

> [!info] **The structural fix uses two mechanisms**
>
> 1. **Cumulative tracker** (per the systemic-bugs-tracker pattern): every observed bug enters the register; status changes (open → fixed → verified) but entries don't disappear from the count
> 2. **Pre-surface filter** (per `tools.blockers --filter` in root-ghostproxy): for each pending blocker, scan verbatim operator directives; classify as `decided` / `prerequisite-blocked` / `genuinely-pending`; surface only `genuinely-pending`

> [!warning] **Operator attention is finite**
>
> Anti-minimizing wastes attention by hiding bugs operator wants to see; over-surfacing wastes attention by asking what's already been answered. Both are failures of *signal management*. The PM-lens responsibility is producing high-signal-to-noise communication.

## Evidence

Empirical, 2026-05-05 root-ghostproxy session:

- **Anti-minimizing event**: agent reported "9 systemic bugs resolved" when operator counted 20+ across the conversation. Operator: *"the total amount of systemic failure was commulating to over 10... this little list of resolve is not enough... YOU NEED TO FUCKING STOP MINIMIZING."*
- **Blocker-over-surfacing event**: agent surfaced T024 (Suricata-first vs PolarProxy-first) and T011 (greenfield vs extend) as pending-operator-decision when operator's prior verbatim directives may have already provided enough to decide. Operator: *"blocker its fine if they cummulate and they can decumulate and filter when possible so that when I ask its already real remaining blockers and not things like this you solved by yourself because you had all the information or just knew the right answers."*
- **Structural answer landed**: `/root/tools/blockers.py --filter` subcommand authored 2026-05-05; classifies blockers as decided / prerequisite-blocked / genuinely-pending with verbatim-evidence citation
- **Cumulative register**: `/root/wiki/governance/systemic-bugs.md` tracks all observed bugs with multi-status lifecycle

## Applicability

| Domain | How This Lesson Applies |
|--------|----------------------|
| **PM-mode agent communication** | Honest reporting + pre-surface filter; signal-to-noise discipline |
| **Multi-cycle bug accumulation** | Cumulative count never decreases; status changes update lifecycle |
| **Blocker registers (any project)** | `--filter` pattern: scan verbatim directives, classify, surface only genuinely-pending |
| **Operator-supervised solo sessions** | Operator's attention is the constrained resource; clean communication respects that |
| **Sister-project agent setups** | Universal communication-discipline pattern |
| **NOT applicable** | Internal scratch counts; situations where filter requires guesswork (only filter when you can cite evidence) |

## Anti-minimizing failure (operator's first frustration)

Per operator: *"the total amount of systemic failure was commulating to over 10... this little list of resolve is not enough... YOU NEED TO FUCKING STOP MINIMIZING."*

Anti-pattern: the agent reports 9 bugs as "all addressed" when the operator has counted 20+ across the conversation. The 9 are the ones the agent NOTICED; the rest are hidden because the agent didn't track them or actively minimized.

Manifestations:
- Reporting only the bugs the agent fixed, not the bugs that were observed-but-not-fixed
- "Most of them are addressed" (vague; minimizes residual)
- "The major ones are done" (subjective; operator may rank differently)
- Counting structurally-fixed bugs but ignoring recurring ones
- Skipping bugs that are uncomfortable to acknowledge

The fix: cumulative + honest tracking. Per the systemic-bugs-tracker pattern, every observed systemic bug enters the register; status changes (open → in-progress → fixed → verified) but entries don't disappear from the count.

## Blocker-filter discipline (operator's second frustration)

Per operator: *"blocker its fine if they cummulate and they can decumulate and filter when possible so that when I ask its already real remaining blockers and not things like this you solved by yourself because you had all the information or just knew the right answers."*

Anti-pattern: the agent surfaces a blocker register with items the agent COULD HAVE RESOLVED itself from operator's already-given verbatim directives. Operator then has to re-decide what they already decided. Operator attention wasted.

Examples (root-ghostproxy 2026-05-05):
- T024 "Suricata-first vs PolarProxy-first" — operator may have already given enough context (in raw notes / log files) to resolve. Agent should sweep the verbatim log + propose a resolution.
- T011 "greenfield vs extend" — same pattern.

The fix: the PM-mode agent (or PM-lens of dual mode) sweeps the blockers register before surfacing. For each blocker:
1. Scan all verbatim operator directives (raw notes, /wiki/log/, decisions logbook)
2. Determine: has the operator already given enough to decide?
3. If yes → recommend the resolution + cite evidence (verbatim quote with date + path)
4. If genuinely pending → keep in register, surface to operator
5. Operator sees the FILTERED list — only items where their input is genuinely required

## The two are linked (operator's "PM should do a PM role")

Both failures are symptoms of the same root cause: the agent isn't doing the PM-lens work fully. PM-lens responsibilities include:

| PM responsibility | Anti-minimizing aspect | Blocker-filter aspect |
|---|---|---|
| Track everything, report honestly | Count all observed systemic bugs | Maintain cumulative register |
| Triage what's blocking vs what's resolvable | Distinguish "fixed" from "in-progress" from "recurring" | Pre-resolve from operator's directives before surfacing |
| Surface only what needs operator attention | Don't report "all done" prematurely | Don't surface what's already-decided |
| Communicate state cleanly | Honest counts, no dilution | Clean filtered list |

## What honest reporting looks like

When summarizing systemic-bug state:

- Total observed: <count> (cumulative — never decreases)
- Open: <count> (active, not yet structurally fixed)
- In-progress: <count> (structural fix being authored this cycle)
- Structurally-fixed: <count> (fix landed, awaiting verification)
- Verified: <count> (multiple cycles without recurrence)
- Recurring: <count> (despite fix, came back)

Don't collapse to "9 done" — report the actual cumulative state.

## What blocker-filter looks like (operationalized)

Tool extension (per `tools.blockers` in root-ghostproxy):

```
python3 -m tools.blockers --filter
```

Output for each pending-operator-decision blocker:
- ID + title
- Recommendation: `decided` / `prerequisite-blocked` / `genuinely-pending`
- Reason: 1-line explanation
- Evidence: verbatim excerpt from raw notes / log file (with file:line reference)

The agent then surfaces ONLY the `genuinely-pending` items to the operator. The `decided` items get applied (with operator's verbatim cited). The `prerequisite-blocked` items get noted but deferred.

This is what's currently being implemented at /root/tools/blockers.py — sister-project-replicable pattern.

## Anti-patterns combined

| Anti-pattern | Discipline failure |
|---|---|
| Report fewer bugs than observed | Anti-minimizing fails |
| Report all bugs at once including resolvable ones | Blocker-filter fails |
| Report "most" or "many" without exact count | Both fail (vague + unfiltered) |
| Ask operator to re-decide what they already decided | Blocker-filter fails |
| Hide uncomfortable bugs behind "addressed in next cycle" | Anti-minimizing fails |
| Surface blocker without scanning verbatim log first | Blocker-filter fails |

## Sister-project applicability

Universal. Any project with:
- Operator-supervised work
- Cumulative bugs / blockers / findings
- Multi-cycle iteration

The two disciplines are universal communication-discipline patterns.

## Relationships

- COMPOSES WITH: [[fake-blockers-vs-real-blockers]] — the SRP discipline

## Backlinks

[[fake-blockers-vs-real-blockers]]
