---
title: "Peace Machine + Core Law — doctrine clause citation index (pre-page operator-authoring)"
type: reference
domain: ai-agents
layer: 2
status: draft
confidence: high
maturity: seed
created: 2026-06-05
updated: 2026-06-05
sources:
  - id: avx-plus-plus-dump-2026-05-18
    type: directive
    project: devops-solutions-information-hub
    path: raw/dumps/2026-05-18-the-ultimate-exploitation-of-the-tech-stack-AVX-plus-plus.md
    note: "Source dump — Core Law line 18288, Key Scheduling Law lines 18256-18257"
  - id: backward-sweep-review
    type: internal
    project: devops-solutions-information-hub
    path: wiki/log/2026-05-20-avx-plus-plus-dump-tail-backward-sweep-review.md
    note: "Source of the Core Law six-clause enumeration + per-clause milestone mapping"
  - id: selfdef-sdd-031
    type: internal
    project: selfdef
    path: docs/sdd/031-goldilocks-scheduler.md
    note: "SDD-031 line 147: explicitly designates wiki/spine/doctrine/peace-machine-and-core-law.md as operator-supervised authoring scope"
  - id: selfdef-scheduler-runbook
    type: internal
    project: devops-solutions-information-hub
    path: wiki/runbooks/scheduler-not-running.md
    note: "Carries the Key Scheduling Law two-clause verbatim quote"
  - id: selfdef-force-override-runbook
    type: internal
    project: devops-solutions-information-hub
    path: wiki/runbooks/scheduler-force-override-investigation.md
    note: "Carries the Core Law six-clause verbatim quote"
tags:
  - doctrine
  - peace-machine
  - core-law
  - operator-supervised
  - citation-index
---

## What this page IS

A **citation index + status record** for the Peace Machine + Core Law
doctrine. The actual doctrine page at
`wiki/spine/doctrine/peace-machine-and-core-law.md` is **operator-supervised
authoring scope** per `cyberpunk042/selfdef/docs/sdd/031-goldilocks-scheduler.md`
line 147 (verbatim):

> Mark DONE only when all eleven deliverables are in production AND the
> operator-supervised authoring of `wiki/spine/doctrine/peace-machine-and-
> core-law.md` (per backward-sweep review item #4) has landed.

That page does not yet exist. Multiple selfdef runtime artifacts already
cite it as their doctrinal anchor (selfdef-scheduler crate `ocsf_emitter.rs`,
`docs/operator/ms048-scheduler-failure-modes.md`, every MS048 commit message
this session). The citations are correct — the path is the designated home
for the consolidated doctrine — they just point at a target only the operator
can author per the scope rule.

This index makes the verbatim clause set + their dump line refs + the citing
artifacts **discoverable from the info-hub side** until the operator-authored
page lands.

## Verbatim clause inventory (do not paraphrase)

### Core Law (six clauses)

Source: avx-plus-plus dump line 18288, transcribed verbatim in
`wiki/log/2026-05-20-avx-plus-plus-dump-tail-backward-sweep-review.md`
line 81:

> Models propose. Runtime routes. CPU enforces. Tools prove. ZFS remembers. User chooses.

Per-clause milestone mapping (from the same log file, lines 82-87):

| Clause | Milestone(s) |
|---|---|
| Models propose | MS028 + MS029 + MS030 inference modules |
| Runtime routes | MS048 Goldilocks Scheduler |
| CPU enforces | MS046 + MS047 + MS044 three-watchdog trio |
| Tools prove | MS042 tool authority |
| ZFS remembers | MS003 + MS046 audit trails + MS044 atomic log bridge |
| User chooses | MS039 Ring 0 authority + MS040 profile envelope |

### Key Scheduling Law (two clauses)

Source: avx-plus-plus dump lines 18256-18257, transcribed verbatim in
`wiki/runbooks/scheduler-not-running.md` line 51-53:

> Never let expensive cognition wait on cheap preparation.
> Never let cheap speculation commit without expensive verification when risk demands it.

This pair governs MS048 routing specifically (the dump tail's scheduling
architecture). The selfdef-scheduler runtime's `scheduling_law.rs` encodes
the two clauses as `LawClause::ExpensiveCognitionNotDeferred` and
`LawClause::SpeculationRequiresVerification` — runtime carries them as the
LawClause-emitting decision branches.

### Peace Machine — "disciplined enough to explain itself"

Used as a doctrinal anchor in
`cyberpunk042/selfdef/docs/operator/ms048-scheduler-failure-modes.md`
line 5: the failure-mode runbook stance is "every failure mode below is
observable + named + remediated; no silent failure modes." Source of the
phrase: avx-plus-plus dump tail, exact line awaiting operator confirmation
as part of the supervised authoring of the doctrine page.

## Where these clauses are already cited (audit trail)

### `cyberpunk042/selfdef` (production runtime + operator surfaces)

| Artifact | Clause cited |
|---|---|
| `crates/selfdef-scheduler/src/ocsf_emitter.rs` (module doc) | Peace Machine — "disciplined enough to explain itself"; Core Law — "ZFS remembers" |
| `crates/selfdef-scheduler/src/scheduling_law.rs` (module doc) | Key Scheduling Law (both clauses, verbatim) |
| `crates/selfdef-scheduler/src/objective_signals.rs` (module doc) | Core Law — "Models propose / Runtime routes / CPU enforces" |
| `docs/operator/ms048-scheduler-failure-modes.md` | Peace Machine — "disciplined enough to explain itself" |
| `docs/sdd/031-goldilocks-scheduler.md` | Key Scheduling Law (both clauses) + named scope-target for the operator-authored doctrine page |

### `cyberpunk042/devops-solutions-information-hub` (this repo)

| Artifact | Clause cited |
|---|---|
| `wiki/log/2026-05-20-avx-plus-plus-dump-tail-backward-sweep-review.md` | Core Law (six clauses, verbatim) + milestone mapping |
| `wiki/runbooks/scheduler-not-running.md` | Key Scheduling Law (both clauses, verbatim) |
| `wiki/runbooks/scheduler-force-override-investigation.md` | Core Law (six clauses, verbatim) — "User chooses" emphasized |

## What's NOT in this index (operator scope)

- The doctrine page's narrative section (HOW the clauses interlock, what
  each clause implies operationally beyond the milestone mapping)
- Any new doctrinal claim, framing, or extension beyond the verbatim
  clauses above
- A "promotion" of these clauses from `draft` to `verified` maturity
  (operator-authoring required per SDD-031)

This page is the citation/audit layer; the doctrinal layer above it stays
operator-supervised per the scope rule.

## When the operator-authored doctrine page lands

This citation index becomes a back-pointer. The wiki spine page at
`wiki/spine/doctrine/peace-machine-and-core-law.md` will be the
authoritative home; this page links there from its first paragraph. Until
then, this is the discoverable consolidation point.

## Relationships

- USED BY [scheduler-not-running runbook](scheduler-not-running.md) — runbook quotes Key Scheduling Law verbatim, cites doctrine page
- USED BY [scheduler-force-override-investigation runbook](scheduler-force-override-investigation.md) — runbook quotes Core Law verbatim
- DERIVED FROM [backward-sweep review log](../log/2026-05-20-avx-plus-plus-dump-tail-backward-sweep-review.md) — source of the six-clause Core Law enumeration
- ENABLES the operator-supervised authoring of `wiki/spine/doctrine/peace-machine-and-core-law.md` — collects the citation surface area in one place so the doctrine page knows what citing artifacts it will become the anchor for
