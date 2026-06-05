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

## Summary

Operational citation registry for the Peace Machine + Core Law doctrine page
at `wiki/spine/doctrine/peace-machine-and-core-law.md` (authored on this same
branch, commit `0c2a673`, shipped via PR #17). The doctrine page itself is
the authoritative source; this registry is the **citation index** — a
discoverable list of every artifact across `cyberpunk042/selfdef` +
`cyberpunk042/devops-solutions-information-hub` that cites a Core Law or Key
Scheduling Law clause, so future doctrine evolution can audit blast radius
before changes land. Verbatim clause anchors (Core Law six-clause from dump
line 18288; Key Scheduling Law two-clause from dump lines 18256-18257) are
duplicated here as a back-reference convenience only — the doctrine page is
the source of truth.

## What this page IS

An **operational citation registry** — the discoverable list of every
artifact across the ecosystem that cites a Peace Machine + Core Law clause.
The doctrine page itself lives at
[`wiki/spine/doctrine/peace-machine-and-core-law.md`](../spine/doctrine/peace-machine-and-core-law.md)
(`status: synthesized`, `confidence: authoritative`, `maturity: growing`,
authored 2026-05-29 per backward-sweep review Action 4) and is the
authoritative source for the doctrinal statements + their per-clause milestone
mapping.

This registry exists because the citation surface area is wide: selfdef-
scheduler crate modules, MS048 operator failure-modes runbook, every MS048
commit message, multiple info-hub runbooks. When the doctrine page evolves
(future operator amendments, new dump material) this registry is the audit
surface for "what needs updating downstream."

Per `cyberpunk042/selfdef/docs/sdd/031-goldilocks-scheduler.md` line 147:

> Mark DONE only when all eleven deliverables are in production AND the
> operator-supervised authoring of `wiki/spine/doctrine/peace-machine-and-
> core-law.md` (per backward-sweep review item #4) has landed.

That authoring landed on this branch (commit `0c2a673`); PR #17 ships it.
This registry is the operational layer beneath the doctrinal page.

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

## What's NOT in this index (scope)

- The doctrine page's narrative (HOW the clauses interlock, what each clause
  implies operationally beyond the milestone mapping) — that's the doctrine
  page at `wiki/spine/doctrine/peace-machine-and-core-law.md`, this index
  back-points there.
- Any new doctrinal claim, framing, or extension beyond the verbatim clauses
  the doctrine page carries — this index never amends doctrine.
- A "promotion" of these clauses from `draft` to `verified` maturity — the
  doctrine page itself owns its maturity lifecycle.

This page is the citation/audit layer beneath the doctrinal page above it.

## Maintenance

When a new selfdef or sovereign-os artifact starts citing a Core Law or Key
Scheduling Law clause, append it to the corresponding row in the audit-trail
table above. When the doctrine page evolves (operator amendment, new dump
material), use the audit trail to find every downstream artifact that may
need a corresponding update.

## Relationships

- USED BY [scheduler-not-running runbook](scheduler-not-running.md) — runbook quotes Key Scheduling Law verbatim, cites doctrine page
- USED BY [scheduler-force-override-investigation runbook](scheduler-force-override-investigation.md) — runbook quotes Core Law verbatim
- DERIVED FROM [backward-sweep review log](../log/2026-05-20-avx-plus-plus-dump-tail-backward-sweep-review.md) — source of the six-clause Core Law enumeration
- ENABLES the operator-supervised authoring of `wiki/spine/doctrine/peace-machine-and-core-law.md` — collects the citation surface area in one place so the doctrine page knows what citing artifacts it will become the anchor for
