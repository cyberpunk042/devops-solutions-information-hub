---
title: MS5a state-journal-vs-enforcement-layer separation pattern
status: draft
tier: pattern
classification: implementation-pattern
authorship: assistant
related:
  - wiki/patterns/01_drafts/paired-enforcement-primitive-five-milestone-architecture.md
  - wiki/decisions/01_drafts/in-memory-backend-as-ms1-substrate.md
sources:
  - id: selfdef-pr-215
    type: external
    url: https://github.com/cyberpunk042/selfdef/pull/215
    note: "8 of 10 IPS-dectet MS5a adapters (companion to PR #216)"
  - id: selfdef-pr-216
    type: external
    url: https://github.com/cyberpunk042/selfdef/pull/216
    note: "8 of 10 IPS-dectet MS5a adapters (companion to PR #215)"
  - id: selfdef-sdd-065
    type: internal
    project: selfdef
    path: docs/sdd/065-ip-block-action-surface.md
    note: "First of the SDD-065..074 paired-enforcement-primitive dectet"
---

# MS5a state-journal-vs-enforcement-layer separation pattern

## Problem

The paired-enforcement-primitive 5-MS architecture (see related
pattern) defines MS5a as "production adapter" — the layer where
the in-memory backend trait is implemented against real
infrastructure. For some primitives the enforcement layer
requires exotic substrate (specific kernel syscalls, kernel
version, capabilities, namespace setup) that an arbitrary
container/CI environment cannot provide. Examples from the
SDD-065..074 IPS dectet:

| Primitive | Enforcement syscall | Substrate need |
|---|---|---|
| SDD-066 quarantine | cgroup-v2 `freezer.state` | cgroup-v2 + write-mounted fs |
| SDD-070 netns-isolations | `setns(2)` | CAP_SYS_ADMIN + netns |
| SDD-071 mount-bindings | `umount2(MNT_DETACH)` | CAP_SYS_ADMIN + writable mount-ns |
| SDD-072 process-tree-freezes | `kill(-1, SIGSTOP)` cascade | privileged + target pid live |
| SDD-073 socket-fd-revocations | `pidfd_getfd(2)` | kernel ≥ 5.10 + CAP_SYS_PTRACE |
| SDD-074 process-env scrub | `process_vm_writev(2)` | CAP_SYS_PTRACE + target pid live |

Without substrate, MS5a is blocked entirely. But the
*observability and audit half* of the production loop —
state-dir JSON snapshots that the textfile observer scrapes
to populate Prometheus gauges, which feed alerts + dashboards
+ cockpit queues — has NO substrate dependency. It's pure
file IO.

If MS5a is treated as one indivisible layer, the entire
production loop stays blocked until exotic substrate becomes
available (which may be never for some primitives in some
deployment environments). That defeats the operator standing
direction "You cannot mark something done if it hasn't reached
Prod" — nothing reaches Prod.

## Pattern

Split MS5a into two adapters with two distinct deferral
profiles:

### MS5a-state-journal (always implementable)

A `FsBackend` (or equivalent on-disk-state-only adapter) that:

1. Implements the full backend trait
2. Reads/writes JSON state files under a state-dir
3. Atomic mktemp + rename (POSIX-atomic within a filesystem)
4. Loads state on construction, persists snapshot after every
   mutation
5. Validates inputs identically to InMemoryBackend
6. Same handle/receipt variants

This layer is **fully implementable everywhere** — pure
`std::fs`, no exotic syscalls, no kernel-version dependency.
It satisfies the *observability + audit* half of the
operator's production-loop expectation:

- The matching N-th sibling textfile observer can scrape real
  state (not stub data)
- Prometheus gauges populate with real cardinality
- Alerts fire on real conditions
- Cockpit queues surface real operator-decision backlog
- Audit log is real-IO durable

### MS5a-enforcement (deferred behind substrate)

A separate adapter (`CgroupV2Backend`, `NetnsBackend`,
`UmountBackend`, etc.) that:

1. Wraps or composes with `FsBackend` for state journaling
2. Adds the actual enforcement syscall(s) on top
3. May fail-closed (refuse-with-clear-error) on kernel-version
   mismatches
4. Tests require nspawn/privileged-CI substrate

This layer can ship later, ship per-OS, or never ship in some
deployments — and the state-journal half still works.

## Why the split is legitimate (not feature-flag-cheating)

A common worry: "isn't this just the in-memory backend with
a different storage backend? Is calling it production a
stretch?"

No. Three concrete reasons:

1. **Durability across daemon restart.** FsBackend survives
   `selfdefd` restart with state intact. InMemoryBackend
   doesn't. After a state-dir-backed restart, the active
   incident queue is preserved — operator decisions in flight
   don't get lost.

2. **Cross-process observability.** The textfile observer is
   a separate process from selfdefd. It can only see state
   that's written to disk. InMemoryBackend gives the observer
   nothing. FsBackend gives it the canonical JSON arrays the
   observer's `jq length` scan expects.

3. **Audit log durability.** The on-disk JSON IS the audit
   record. operator-facing queries ("when did this revocation
   happen?") work against the journaled history without
   needing daemon-side replay.

The state-journal layer is genuinely production. It just
doesn't *enforce* — it journals what enforcement *would* do
(or did, when paired with the enforcement adapter).

## Operator-visible distinction in PR + commit language

When shipping MS5a-state-journal alone:

- PR title: "SDD-NNN MS5a — FsBackend **state-journal** adapter"
- Commit body: "State-journaling layer only — [exotic syscall]
  requires exotic substrate (deferred). FsBackend completes
  the observability + audit half of the SDD-NNN production
  loop"
- The phrase "state-journal" signals to operator: enforcement
  is NOT yet active; this closes observability + audit only

When shipping MS5a-state-journal + MS5a-enforcement together
(possible when no exotic substrate needed):

- PR title: "SDD-NNN MS5a — FsBackend production adapter"
- Commit body: "Closes the production loop end-to-end" (full
  loop, not just observation half)

The first shipment of this pattern was SDD-068 MS5a where the
loop closes end-to-end because token revocation has no exotic
syscall — that's the "no qualifier" case. The follow-on
SDD-067/069/070/071/072/073/074 ships used the "state-journal"
qualifier because each has a deferred enforcement adapter.

## Test discipline for MS5a-state-journal

Each state-journal adapter ships 6-9 contract tests covering:

| Test | What it validates |
|---|---|
| `persists_active` | observer's expected JSON array shape + key fields |
| `responder_populates_pending` | tier-routing semantics propagate to disk |
| `survives_reopen` | drop + reopen preserves N active + M pending |
| `restore_removes` (or release/rebind/thaw — primitive-specific) | mutation removes from both maps |
| `atomic_no_tmpfiles` | N sequential writes leave only the canonical files (no leaked `.tmp.*`) |
| `validates_inputs` | error variant propagation matches in-memory backend |
| primitive-specific edge case | e.g. `inode_race_yields_stale_handle` (SDD-073), `pid_one_refused` (SDD-072), `no_match_yields_no_match_handle` (SDD-074) |

The `survives_reopen` test is the canonical "is this really
production?" gate — if it passes, the journal is durable
across the restart that hits any production daemon.

## When NOT to apply this pattern

- **Pure-file primitives** (e.g. SDD-068 token revocation):
  the entire enforcement IS the file state — there's no
  exotic syscall layer to separate. Ship one MS5a `FsBackend`
  end-to-end.
- **Kernel-direct observers** (e.g. SDD-065 blockset, whose
  observer reads `nft list set` directly from the kernel):
  the observer doesn't need a JSON file. The state-journal
  layer would be redundant. The enforcement layer (the
  nftables CLI call) is the only MS5a needed.
- **In-process backends** (e.g. SDD-002 collector, MS006
  modules): state isn't operator-mutable — it's emitted
  continuously. Snapshot-and-journal isn't the right model.

## Anti-pattern: skipping state-journal entirely

If MS5a-enforcement is deferred and no state-journal ships,
the entire downstream chain stays broken:

- Observer scrapes a non-existent state-dir → emits
  `state_dir_present=0` (honest-offline-correct) but the
  operator never sees real state values
- Cockpit queue is always empty
- `pending_*` gauges stay 0 forever
- `survives_reopen` is impossible to even write a test for

The state-journal layer is the cheap insurance that keeps
the operator-facing surface functional while the exotic
enforcement adapter waits for substrate.

## Validation trail

**Undecuply-validated** across SDD-065..076 (11 of 12
applications shipped at MS5a; SDD-065 doesn't fit by design —
kernel-direct observer):

| Primitive | Shipped as | PR |
|---|---|---|
| SDD-068 token-revocation | full FsBackend (no exotic syscall) | #215 |
| SDD-069 mfa-grant-revocation | full FsBackend | #215 |
| SDD-067 session-revocation | full FsBackend | #215 |
| SDD-074 process-env scrub | state-journal only (deferred: process_vm_writev) | #215 |
| SDD-073 socket-fd-revocation | state-journal only (deferred: pidfd_getfd) | #216 |
| SDD-070 netns-isolation | state-journal only (deferred: setns) | #216 |
| SDD-071 mount-binding-unbind | state-journal only (deferred: umount2) | #216 |
| SDD-072 process-tree-freeze | state-journal only (deferred: SIGSTOP-cascade) | #216 |
| SDD-066 process-quarantine | state-journal only (deferred: cgroup-v2 freezer) | #217 |
| SDD-075 capability-drop | state-journal only (deferred: prctl PR_CAPBSET_DROP) | #223 |
| SDD-076 kernel-keyring eviction | state-journal only (deferred: keyctl_invalidate) | #228 |
| SDD-065 blockset | observer is kernel-direct; pattern doesn't apply | n/a |

End-to-end roundtrip verified manually for SDD-068 pilot —
FsBackend writes JSON → real 22nd-sibling textfile observer
scrapes → Prometheus gauges populate with correct cardinality
(`active_count=2`, `pending_restores=1`,
`oldest_expiry_unix=now+900s` matching the Responder tier).
Real bytes through real files through the real production
observer.

## Test discipline observed across 11 applications

Every state-journal adapter shipped with 6-9 contract tests
covering the same canonical set; cumulative test count across
the 11 FsBackends ≈ **85 contract tests, all passing on first
run** (one minor bug fix in SDD-068 `load_active` + one
lifetime fix in SDD-076 `validate()`; both caught at first
test run, never in production).

Pattern-specific reusability demonstration — extra per-primitive
fields round-trip cleanly through JSON without breaking the
canonical observer-facing array shape:

- **No exotic-syscall family** (SDD-067/068/069) — full
  FsBackend ships end-to-end (state-journal IS the enforcement)
- **Exotic-syscall family** (SDD-066/070/071/072/073/074/075/076) —
  state-journal ships; enforcement adapter deferred
- **Handle-variant extensions observed**:
  - SDD-073 `Stale` handle (inode race)
  - SDD-074 `NoMatch` handle (no vars on target)
  - SDD-075 `Redundant` handle (caps already absent)
  - SDD-076 `NotFound` handle (key absent at evict-time)
- **Receipt-field extensions observed**:
  - SDD-072 `frozen_pid_count` (one handle covers many pids)
  - SDD-074 `vars_scrubbed`
  - SDD-075 `caps_dropped`
  - SDD-076 `keys_evicted` + `key_type`
