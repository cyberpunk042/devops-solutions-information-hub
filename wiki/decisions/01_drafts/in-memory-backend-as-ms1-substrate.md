---
title: In-memory backend as MS1 substrate for selfdef enforcement primitives
type: decision
domain: ai-agents
status: draft
confidence: medium
maturity_tier: 01_drafts
created: '2026-05-29'
updated: '2026-05-29'
sources:
  - id: selfdef-sdd-065
    type: internal
    project: selfdef
    path: docs/sdd/065-ip-block-action-surface.md
    note: SDD-065 IP-block action surface — MS1 in-memory backend
  - id: selfdef-sdd-066
    type: internal
    project: selfdef
    path: docs/sdd/066-process-quarantine-action-surface.md
    note: SDD-066 process-quarantine action surface — MS1 in-memory backend
tags:
  - decision
  - selfdef
  - ms1
  - in-memory-backend
  - enforcement-primitive
  - sdd-065
  - sdd-066
  - ai-drafted
decided_in_session: claude-code 2026-05-29 perpetual /goal
applies_to:
  - selfdef-blockset-backend (SDD-065 MS1)
  - selfdef-process-quarantine-backend (SDD-066 MS1)
  - future enforcement primitive crates
authorship_class: ai_drafted_session_synthesis
---

# In-memory backend as MS1 substrate

## Summary

Decision page for the MS1 substrate choice for selfdef enforcement primitives: every new primitive following the paired-enforcement-primitive five-milestone architecture ships an `InMemoryBackend` first; the production adapter (MS1b — nftables-set, cgroupv2-freezer) lands separately and is feature-gated. Applies to SDD-065 + SDD-066.

## Decision

For every new selfdef enforcement primitive following the
**paired enforcement primitive five-milestone architecture**
pattern, MS1 ships an `InMemoryBackend` as the first
implementation of the backend trait. The production adapter
(MS1b — nftables-set, cgroupv2-freezer, etc.) is feature-gated
and lands separately.

## Rationale

### Why

#### 1. CI-substrate compatibility

The CI environment for selfdef + sovereign-os does NOT have:

- nftables kernel module loaded with selfdef-blocks table
  bootstrapped.
- cgroupv2 freezer cgroups created under selfdef.slice.
- `CAP_NET_ADMIN` or `CAP_SYS_ADMIN`.
- Permission to mutate `/sys/fs/cgroup/`.

If MS1 went straight to a production backend, **the entire
cargo test suite for the action runner + CLI verbs would
require a real kernel substrate** — meaning either:

- All enforcement-primitive tests get gated to L3
  (nspawn-style) → slow, can't run in PR-check tier 1.
- All tests skip silently → low confidence the surface
  actually works.

InMemoryBackend lets MS2 + MS3 + the trait-default `pending_*()`
queue + the cockpit `MS5b` consumer all be unit-testable at
L1 in CI tier 1 with **zero infrastructure setup**.

#### 2. Test-first discipline

The MS1 pattern is "write 9–13 contract tests FIRST, then
implementation just enough to pass." This is only honest
when the implementation is fully under test control.
InMemoryBackend gives the test author full control over
state visibility (`active_count()`, `pending_releases()`,
direct introspection of the Mutex<State>).

A production backend would force tests like "block IP,
then verify by parsing `nft list ruleset` output" —
fragile, slow, environment-dependent.

#### 3. Cross-action operator-familiarity

When SDD-065 and SDD-066 use the same `InMemoryBackend`
substrate pattern, the operator + future contributors
read **one shape** and recognize it everywhere. The
PendingExtension / PendingRelease structs, the
`mark_*_decided()` semantics, the
sorted-ASC-by-seconds-remaining invariant — all carry
across primitives because the InMemoryBackend forces
each crate to implement the same shape clearly.

#### 4. Production-adapter swap-in stays clean

MS1b adapters implement the same trait and pass the same
contract tests (plus their own adapter-specific tests like
"`nft_add_element_args` builds the correct vector"). The
selfdef-responder + selfdefctl + cockpit consumers don't
need to know which backend is in use — they take
`Arc<dyn <Primitive>Backend>` and the operator's
selfdefd config picks the adapter at startup.

## Alternatives

The alternative considered was: **MS1 ships the production adapter directly** (nftables-set for SDD-065, cgroupv2-freezer for SDD-066), with no in-memory layer. Rejected because the CI substrate does not have the required kernel modules, capabilities, or cgroup hierarchy bootstrapped — see § Rationale 1 (CI-substrate compatibility) — and because test-first discipline (Rationale 2) requires Mutex-state introspection that a real adapter cannot offer cleanly.

### Trade-offs accepted

- **Two implementations per primitive** instead of one.
  Mitigated by the small surface area (InMemoryBackend is
  ~100 LoC including Mutex<State>).
- **MS1 InMemoryBackend doesn't survive CLI restart.**
  Documented in MS3 dispatch: `selfdefctl release-pid h-bogus`
  prints "no active block for h-bogus (MS3 stateless backend)"
  rather than silently succeeding. Once MS4 (textfile observer
  + selfdefd-backed persistent state) lands, the CLI can wire
  to the daemon-side persistent backend over the existing
  selfdef-bus channel.

## Reversibility

Fully reversible per primitive. The decision constrains MS1 only; MS1b ships the production adapter behind a feature flag and consumers (selfdef-responder + selfdefctl + cockpit) take `Arc<dyn <Primitive>Backend>` so the substrate swap is invisible at the call site. To reverse, drop the InMemoryBackend re-export and switch the daemon config to instantiate the production adapter — both crates already implement the trait. Once MS4 (textfile observer + selfdefd-backed persistent state) lands, the CLI can wire to the daemon-side persistent backend over the existing selfdef-bus channel, completing the swap-in.

## Dependencies

- **SDD-065** `docs/sdd/065-ip-block-action-surface.md` — first enforcement primitive implementing this decision (`selfdef-blockset-backend` crate).
- **SDD-066** `docs/sdd/066-process-quarantine-action-surface.md` — sibling enforcement primitive (`selfdef-process-quarantine-backend` crate).
- **Pattern** `paired-enforcement-primitive-five-milestone-architecture.md` — the five-milestone architecture this decision applies to.
- **MS4** (selfdef textfile observer + selfdefd-backed persistent state) — required before the CLI can swap to a persistent backend.
- **selfdef-bus** channel — required for daemon ↔ CLI persistent-backend wiring.

### When this decision does NOT apply

- Pure observability surfaces (no enforcement state to mock —
  they just emit gauges).
- Stateless verbs (e.g., `selfdefctl doctor`) — no backend at
  all.
- Configuration primitives — these compose on top of
  selfdef-config which has its own substrate.

## Replication recipe

When starting a new enforcement primitive following this
decision:

```bash
cd selfdef/crates
cargo new --lib selfdef-<primitive>-backend
# Cargo.toml: async-trait + serde + thiserror as deps,
# tokio + serde_json as dev-deps, optional tokio with
# `process` feature behind <primitive>-backend feature
# for MS1b.
```

Write `tests/contract.rs` FIRST (13 tests target — match the
list in the paired-enforcement-primitive pattern doc), then
fill `src/lib.rs` to pass.

When all green: cargo fmt → cargo clippy --tests -D warnings →
commit → push.

## Relationships

### Cross-references

- `wiki/patterns/01_drafts/paired-enforcement-primitive-five-milestone-architecture.md`
- selfdef `crates/selfdef-blockset-backend/src/lib.rs` (reference impl)
- selfdef `crates/selfdef-process-quarantine-backend/src/lib.rs` (sibling)
