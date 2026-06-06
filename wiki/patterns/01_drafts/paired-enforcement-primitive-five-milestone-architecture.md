---
title: Paired enforcement primitive — five-milestone architecture for selfdef IPS actions
type: pattern
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
    note: SDD-065 IP-block action surface — first of paired-enforcement-primitive dectet
  - id: selfdef-sdd-066
    type: internal
    project: selfdef
    path: docs/sdd/066-process-quarantine-action-surface.md
    note: SDD-066 process-quarantine action surface — second of paired-enforcement-primitive dectet
tags:
  - pattern
  - selfdef
  - paired-enforcement-primitive
  - five-milestone
  - ips-dectet
  - sdd-065
  - sdd-066
  - ai-drafted
origin_session: claude-code 2026-05-29 perpetual /goal
companions:
  - selfdef docs/sdd/065-ip-block-action-surface.md
  - selfdef docs/sdd/066-process-quarantine-action-surface.md
authorship_class: ai_drafted_session_synthesis
---

# Paired enforcement primitive — five-milestone architecture

## Summary

Reusable five-milestone shape for adding a new IPS enforcement primitive to selfdef + sovereign-os, captured from the convergent independent implementations of SDD-065 (IP-block) and SDD-066 (process-quarantine). The pattern lets a primitive land end-to-end across all architectural layers (backend trait + production adapter + dispatch CLI verbs + textfile observer + cockpit consumer) in five distinct slices without any one slice becoming unbounded.

## Pattern Description

### What this pattern is

A reusable shape for adding a new IPS enforcement primitive to
selfdef + sovereign-os. Captured from the SDD-065 (IP-block) and
SDD-066 (process-quarantine) implementations, which converged on
the same 5-milestone structure independently.

The pattern lets a new primitive land **end-to-end across all
architectural layers** in five distinct slices without any one
slice becoming unbounded.

## When To Apply

### When to apply

Use this pattern when:

- Selfdef needs a new operator-actionable enforcement primitive
  (block-something, freeze-something, revoke-something).
- The primitive has a "buy time, then operator decides" tier
  (responder-tier handles get queued for operator review).
- The primitive needs kernel-side or process-side state that
  persists across selfdefd restarts (TTL via kernel mechanism).
- The primitive should be queryable + composable with other
  primitives (paired-handle correlator output).

## When Not To

Do NOT use this pattern for:

- Pure observability surfaces (those follow the sibling-observer
  pattern in the 18-sibling family).
- Configuration changes (those go through selfdef-config + the
  modules.toml overlay).
- Operator-direct CLI tools without persistence (no MS5b needed).

## Instances

Two convergent independent implementations validate the five-milestone shape:

- **SDD-065 IP-block** (`selfdef-blockset-backend` crate) — first canonical instance; primitive type = network address block-set with `Active(String)` handle keyed by CIDR + scope.
- **SDD-066 process-quarantine** (`selfdef-process-quarantine-backend` crate) — sibling instance arrived at the same 5-MS structure independently; primitive type = process freeze via cgroupv2-freezer with handle keyed by pid + cgroup path.

Subsequent applications of the closely-related state-journal subdivision pattern (see companion pattern `ms5a-state-journal-vs-enforcement-layer-separation.md`) extended the validation set to **11 IPS-dectet primitives** across selfdef PRs #215 + #216, demonstrating the architecture's reusability beyond the original pair.

## The five milestones

### MS1 — Backend trait + InMemoryBackend (TDD-first)

Crate: `selfdef-<primitive>-backend` (e.g.,
`selfdef-blockset-backend`, `selfdef-process-quarantine-backend`).

Surface (mandatory):

- `AuthorityTier` enum with `max_duration()` matrix per SDD §4.
- Request struct with mandatory `reason`, `duration`, `authority`,
  `idempotency_key`.
- `Handle` enum (typically `Active(String)` only initially;
  extensible).
- `Receipt` struct returning the active handle + scope counts.
- `Error` enum with `InvalidRequest`, `AuthorityInsufficient`,
  `BackendUnreachable` variants.
- Async trait with `apply / release / pending_queue /
  mark_decided` methods. Default impls of `pending_queue` +
  `mark_decided` return empty/false so non-tracking backends
  stay correct.
- `InMemoryBackend` implementation with `Mutex<State>` interior.

Contract tests (10–13 typical):

- Apply returns receipt with active handle.
- Empty reason → `InvalidRequest`.
- Invalid request shape (negative pid, link-local addr, etc.) →
  `InvalidRequest`.
- Duration > tier max → `AuthorityInsufficient`.
- Idempotent re-apply returns same handle, no duplicate stack.
- Release clears handle.
- Responder-tier apply enqueues pending decision.
- Other tiers do NOT enqueue.
- Pending queue sorted by `seconds_remaining` ASC (most urgent
  first).
- `mark_decided` removes from queue (underlying state stays).
- Request JSON round-trip (for cockpit consumer).
- Tier-max-duration matrix lock test (verifies SDD §4 values).

### MS1b — Production adapter (feature-gated)

Add real-world-IO adapter behind a cargo feature flag so the
default build stays compilable + testable on hosts without the
required kernel feature / capability:

```toml
[features]
default = []
<primitive>-backend = ["dep:tokio"]
```

The pure helpers (path construction, argument vectors, bootstrap
scripts) stay always-on and unit-testable without root/kernel.

Examples shipped:

- SDD-065: nftables-set adapter (`feature = "nftables-backend"`,
  needs CAP_NET_ADMIN).
- SDD-066: cgroupv2-freezer + signal fallback (`feature =
  "cgroup-backend"` + `feature = "signal-backend"`, needs
  CAP_SYS_ADMIN).

### MS2 — Action runner integration

Crate: `selfdef-responder` (existing).

Add a new `<Primitive>Action` struct implementing the existing
`Action` trait. Take `Arc<dyn <Primitive>Backend>` +
`AuthorityTier` + `Duration` + scope/extra + `reason_prefix`.

Reuse:

- `pid_from_event` / `addr_from_event` helpers for source-data
  extraction.
- `Status::Skipped` pattern when event lacks the required field.
- `dry_run` path that doesn't touch the backend.
- `ActionError::Exec(format!(...))` propagation for backend
  errors (avoids panics in the runner loop).

5 typical tests:

- Dry-run renders address + duration; backend untouched.
- Real apply hits backend; count increments.
- Skipped when no input data in event.
- Authority-insufficient propagates as `ActionError::Exec`.
- `name()` returns stable string for action registry.

### MS3 — Operator-facing CLI verbs

Crate: `selfdef-cli` (existing). Add 2–3 new top-level
`Command` variants:

- `selfdefctl <apply-verb> <target> --reason <text> --duration
  <human> [--authority <tier>] [--scope <variant>] [--dry-run]`
- `selfdefctl <release-verb> <target-or-handle> [--force]`
- Optional: `selfdefctl <terminate-verb>` (for SDD-066 kill
  path).

Implementation:

- `CliAuthority` value-enum with `From` conversion to the
  backend's `AuthorityTier` (multiple SDDs share the enum
  shape but require distinct types because each backend's
  `AuthorityTier` is its own enum).
- `parse_duration_str()` helper (bare seconds, `Ns/Nm/Nh/Nd`
  suffixes) — pure, unit-testable.
- Dispatch arm enforces tier-max BEFORE backend call (anyhow
  `bail` with operator-hint message naming the higher tier).
- Dry-run path prints the plan + returns Ok.
- MS3 default backend = InMemoryBackend (stateless across CLI
  invocations); MS4 wires the persistent process-lifetime
  adapter once the daemon-side selfdef-<primitive>-d
  publishes a snapshot.

5–7 verb tests + smoke verification on dev container:

- Operator + dry-run path: prints plan, backend untouched.
- Operator + real apply: prints handle.
- Autonomous + over-tier-max: rejected with clear
  `--authority operator-overridden` hint.
- Each parse-duration mode (bare/Ns/Nm/Nh/Nd) + rejection of
  unknown suffix.

### MS4 — 19th+ sibling textfile observer

Add the primitive's kernel/runtime state to the textfile
observability fleet. Wrapper script + systemd service + timer +
deb-assets row + Rust unit-file contract tests. The OnBootSec
offset extends the existing sibling sequence (see info-hub
pattern `sibling-observer-boot-offset-discipline.md` for the
rule).

Canonical gauges: `<primitive>_present`, per-family counts, a
total/rollup, oldest-expiry-unix (when applicable), the
standard `_last_run_unix` + `_textfile_emit_failed` sentinels.

The corresponding sovereign-os consumer surface (alerts +
dashboard + observability-status vertical) follows the
established consumer-pattern.

### MS5 — Operator-UX cockpit queue

Sovereign-os cockpit side (R10212-compliant — pure consumer of
the selfdef-side `pending_*()` JSON snapshot):

**MS5a (selfdef-side producer):**

- `<Primitive>Backend` trait gains `pending_*() ->
  Vec<PendingEntry>` and `mark_*_decided(&Handle) -> bool`.
- `PendingEntry` struct serializes to JSON with handle, target,
  original authority, original reason, seconds remaining,
  scope/extra fields.
- InMemoryBackend enqueues on responder-tier apply; clears on
  release or decision-marked.
- Pending list sorted ASC by `seconds_remaining` (most urgent
  first) — stable contract.
- selfdefd polls + dumps to `/var/lib/selfdef/<primitive>/
  pending-*.json` at conventional path.

**MS5b (sovereign-os cockpit consumer):**

- New `scripts/cockpit/<primitive>-queue.py` — stdlib-only
  reader. `--json` mode for dashboard card; default human mode
  with pre-rendered operator commands per entry (copy-paste-
  ready until the cockpit auth surface ships).
- Path overridable via `SOVEREIGN_OS_<PRIMITIVE>_PENDING_PATH`
  env var for testing.
- Honest-offline: missing/invalid JSON → empty queue + exit 0.
- bash-safe `'...'` quoting with `'\''` escape pattern for any
  user-controlled string interpolated into the rendered
  command.
- New `card_<primitive>_queue` in `scripts/dashboard/serve.py`
  invoking via `_run_json_at()` helper. Registered in `CARDS`
  list adjacent to peer enforcement queues so operator sees
  paired-decision rows together.

10–11 typical tests:

- Script present + executable.
- Default snapshot path is canonical.
- Honest-offline on missing + invalid JSON.
- `--json` shape with real entries (count + pre-rendered
  commands).
- Sorted by urgency ASC.
- Apostrophe / special-char escape in commands.
- Human mode shows all action variants (release / kill-TERM /
  kill-KILL when applicable).
- serve.py registers card + canonical title.

## Anti-patterns to avoid

- **Skipping MS1 InMemoryBackend.** Going straight to MS1b
  (real adapter) leaves the action runner + CLI verbs
  untestable on hosts without the required cap. Always ship
  MS1 first.
- **Coupling MS1 to MS1b implementation details.** The trait
  shape must be storage-agnostic. The InMemoryBackend exists
  to prove the trait is implementable without I/O.
- **Per-primitive `AuthorityTier` enums diverging from SDD §4
  values.** The tier-max-duration matrix lock test catches
  this — if the test fails, the SDD spec is wrong or the
  implementation is.
- **Letting MS5b auto-shell `selfdefctl` without operator
  authentication.** Until the cockpit auth surface ships
  (separate SDD), MS5b emits copy-paste commands; operator
  shells them after reading.
- **Adding the primitive to the wrong project.** Per R10212,
  enforcement primitives live in selfdef; sovereign-os
  consumes via cockpit + alerts + dashboard.

## Relationships

### Cross-references

- `wiki/decisions/01_drafts/in-memory-backend-as-ms1-substrate.md`
- selfdef `docs/sdd/065-ip-block-action-surface.md`
- selfdef `docs/sdd/066-process-quarantine-action-surface.md`
- selfdef `crates/selfdef-blockset-backend/` (reference impl)
- selfdef `crates/selfdef-process-quarantine-backend/` (sibling impl)
- sovereign-os `scripts/cockpit/blockset-queue.py` (MS5b reference)
- sovereign-os `scripts/cockpit/quarantine-queue.py` (sibling MS5b)
