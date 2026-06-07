---
title: "Four-watchdog set (MS046+MS047+MS044+MS048) — end-to-end production landing"
type: note
domain: ai-agents
layer: 1
status: draft
confidence: high
maturity: seed
created: 2026-05-20
updated: 2026-05-20
sources:
  - id: avx-plus-plus-dump-2026-05-18
    type: directive
    project: devops-solutions-information-hub
    path: raw/dumps/2026-05-18-the-ultimate-exploitation-of-the-tech-stack-AVX-plus-plus.md
    note: "Source dump tail lines 18000-18250 (Goldilocks scheduler) + §5/§6/§10 (friction-audit / perimeter / guardian) from sain-01 transposition"
  - id: operator-directive-2026-05-19
    type: directive
    project: devops-solutions-information-hub
    path: wiki/log/
    note: "'You cannot mark something done if it hasn't reached Prod' / 'do not get stuck at the cataloging step' / 'Knowledge is the second-brain'"
tags: [four-watchdog, ms046, ms047, ms044, ms048, friction-audit, perimeter, guardian, scheduler, production, selfdef, ips, milestone-landing]
---

# Four-watchdog set — end-to-end production landing (2026-05-20)

## Summary

### What landed

Four cooperating boundary-enforcement layers are now production-shipped end-to-end across the selfdef + sovereign-os + info-hub repos:

| Layer | Milestone | Source | Role |
|---|---|---|---|
| hardware frame | MS046 | sain-01 §5 | boot-time PCIe/ZFS/memory gate via `sovereign-guard.service` |
| kernel syscall | MS047 | sain-01 §6 | in-kernel `sys_execve` allowlist via Tetragon `sovereign-perimeter.yaml` |
| supervisor tier | MS044 | sain-01 §10 | Tetragon-event 3-step Responder via `selfdef-guardian.service` |
| routing layer | MS048 | avx-plus-plus dump tail 18000-18250 | Goldilocks 7-axis objective + 5 backpressure surfaces via `selfdef-scheduler.service` |

This page is the second-brain record of the landing so future sessions can pick up at the right level of abstraction. Per the operator's *"Knowledge is the second-brain / information-hub"* standing direction.

## End-to-end production surfaces (operator entry points)

Every operator entry point now surfaces the four-watchdog set:

| Surface | Entry point |
|---|---|
| Package metadata | `dpkg -s selfdef-daemon` → extended-description names all 4 |
| Top-level docs | `README.md` § "Four-watchdog set (IPS spine)" |
| Architecture | `ARCHITECTURE.md` § "Four-watchdog set" with layered ASCII diagram |
| Security narrative | `SECURITY.md` § "Four-watchdog set" with adversary-class table |
| Changelog | `CHANGELOG.md` [Unreleased] — 2026-05-20 entry |
| First-run wizard | `selfdefctl wizard` Step 5 |
| First-run checklist | `selfdefctl init checklist` Step 12 |
| Operator CLI | per-watchdog `selfdefctl <watchdog> {...}` + `selfdefctl trio [--watch N]` + `selfdefctl trio-tail` |
| Diagnostic | `selfdefctl doctor` → `watchdog-set` category (deployability + audit-chain integrity) |
| HTTP API | 11 routes under `/v1/{friction-audit,perimeter,guardian,scheduler}` |
| PWA dashboard | `/dashboard/index.html` 4 panels with auto-refresh + runbook links |
| Grafana | 9 four-watchdog panels + 15 Prometheus gauges via `selfdef-api/metrics` |
| Cockpit mirror (sovereign-os) | 4 read-only typed-mirror crates with project-boundary discipline |
| Periodic health | `selfdef-doctor.timer` hourly cadence |
| Operator runbooks | this wiki's `runbooks/` directory — 20 total (5 per watchdog) |

## Surface-lock harness (10 layers)

`scripts/test/coherence.sh` in the selfdef repo runs on demand + in CI on every push/PR + in release on every tag push. 10 layers exercised:

- L1: perimeter YAML lint (sain-01 §6 verbatim)
- L1: CLI surface (4 watchdog commands × subverb counts)
- L1: HTTP API endpoint declarations (11 routes)
- L1: dashboard sections (HTML + JS + CSS + cargo-deb shipping)
- L1: Grafana template (11 four-watchdog series)
- L2: L2-{friction-audit,guardian,perimeter,scheduler,doctor-timer}.bats (~120 tests)
- cargo: 9 four-watchdog crates' unit suites (~140 tests)

Surface contract drift fails the harness; CI fails the PR; release fails the tag push.

## Cross-repo discipline (sacrosanct)

Per the operator's standing direction *"if I talk about an IPS feature its obviously not in Sovereign-OS. Respect the projects."*:

- selfdef OWNS the four watchdogs (binaries, CLIs, runtimes, HTTP API, Prometheus emission, audit chains)
- sovereign-os CONSUMES via the 4 cockpit panel crates at the filesystem boundary (zero selfdef dep; reads selfdef-emitted JSON only)
- info-hub HOSTS the operator runbooks (read-only knowledge surface)

## What's NOT done (multi-year horizon)

The four-watchdog set is **Stage-1** end-to-end production. Per the operator's *"Take your time, its a multi-year project and we want it done right"*, future rounds will address:

- L3 nspawn boot-replay tests (operator-hardware-gated)
- L4 znver5 full-stack hardware tests
- L5 chaos tests (kill watchdog mid-flight, verify Restart=always)
- Tetragon hot-reload pipeline so MS047 extension manifests actually mutate the kernel allowlist (today they record the operator intent but the in-kernel kprobe uses the static YAML — see `wiki/runbooks/perimeter-sigkill-investigation.md` Stage-2-caveat block)
- DCGM source bridge for scheduler Blackwell VRAM measurement (today the scheduler bin reads `/proc/pressure/*` for CPU/RAM/IO but uses 0.0 stubs for GPU surfaces)
- Human-gate queue tracker bridge for scheduler human-attention axis
- Per-watchdog Stage-2 catalog expansion (each MS04x has ~240 R-rows; some will need elaboration as deployment learnings land)

## Cross-references

- Backward-sweep review that created MS048: `wiki/log/2026-05-20-avx-plus-plus-dump-tail-backward-sweep-review.md`
- Operator runbooks: `wiki/runbooks/{friction-audit,perimeter,guardian,scheduler}-*.md`
- UX coherence failures runbook: `wiki/runbooks/ux-coherence-failures.md`
- selfdef SDDs: `~/selfdef/docs/sdd/{027,028,029,031}-*.md`
- selfdef milestone catalogs: `~/selfdef/backlog/milestones/MS04{4,6,7,8}-*.md`
- selfdef CHANGELOG entry: `~/selfdef/CHANGELOG.md` [Unreleased] — 2026-05-20
