---
title: "Hermetic Testability Is a Precondition for Test-Backfill Scope — Classify Scanners by Input-Source Knob Before Committing to Coverage"
aliases:
  - "No input knob, no hermetic test"
  - "Classify before you backfill"
  - "Ok-path-only suites are false coverage"
type: lesson
domain: cross-domain
layer: 4
status: draft
confidence: high
maturity: seed
created: 2026-05-27
updated: 2026-05-27
last_reviewed: 2026-05-27
derived_from:
  - "P4 — Declarations Are Aspirational Until Infrastructure Verifies Them (PRIMARY parent — an ok-path-only test is an aspirational coverage declaration that verifies nothing about the alert path)"
  - "Verify Against the Real Data Shape (work-mode discipline — read the scanner's actual input contract before writing test fixtures)"
sources:
  - id: selfdef-main
    type: project
    project: cyberpunk042/selfdef
    path: main
  - id: selfdef-l2-watchdog-suites
    type: project
    project: cyberpunk042/selfdef
    path: packaging/test
  - id: selfdef-dedup-guard
    type: project
    project: cyberpunk042/selfdef
    path: packaging/test/L2-watchdog-dedup-guard.bats
  - id: selfdef-sdd-062
    type: project
    project: cyberpunk042/selfdef
    path: docs/sdd/062-watchdog-severity-routing.md
tags:
  - testing
  - test-coverage
  - hermetic-tests
  - bats
  - scanners
  - input-source-knob
  - false-coverage
  - cross-domain
---

# Hermetic Testability Is a Precondition for Test-Backfill Scope — Classify Scanners by Input-Source Knob Before Committing to Coverage

## Summary

When backfilling tests onto a corpus of scanners/validators that read
system or environment state, hermetic testability is not uniform — and it
gates scope. A scanner is hermetically L2-testable for its FINDING paths
(not just its no-op path) iff it exposes an input-source override (the
path / dir / file / root it scans, via an env knob). Without one, a test
can only exercise the ok-path against the unchanged real system — a
low-value suite that reports "covered" while proving nothing about the
alert path. Empirically validated in the selfdef watchdog L2 arc
(2026-05-27): of ~105 host detection-watchdogs, the 65 module-lib scanners
(config-file inputs, all knob-driven) and 18 integrity scanners WITH input
knobs were fully covered; the 21 integrity scanners that read live
kernel/runtime state (`/proc`, `ss`, the clock) or hardcoded `/etc` with NO
knob were deliberately left uncovered rather than shipped as ok-only suites.
Classify first — then cover (has knob) or defer-with-reason (no knob);
never ship false-coverage suites.

## Context

This lesson activates when ALL of the following hold:

- You are adding test coverage to a CORPUS of similar units (scanners,
  linters, validators, watchdogs) rather than a single module.
- The units read EXTERNAL state — the filesystem, kernel interfaces,
  process tables, the clock, network sockets — not just their arguments.
- The interesting behavior is a non-default verdict (an alert / finding /
  failure), and the default verdict (ok / no-finding) is trivially reached
  against an unmodified host.
- You want the coverage to be a real regression gate, not a green
  checkmark.

It does NOT apply to pure functions (deterministic on their inputs — always
hermetically testable) or to units whose only meaningful output IS the
no-op path.

## Insight

**The test fixture must be able to MANUFACTURE the finding condition in a
sandbox.** That requires controlling the scanner's input. Two failure modes
follow when you don't check first:

1. **Ok-path-only false coverage.** If the scanner hardcodes its input
   (e.g. always reads `/etc/passwd`), the only state you can create without
   mutating the real host is the benign one. The suite passes, reports
   coverage, and silently never exercises the alert branch — a P4 violation
   (declared coverage, unverified behavior).
2. **Destructive testing.** The tempting "fix" — mutate the real system
   state (add a real uid-0 user, weaken a real sysctl) — is non-hermetic,
   order-dependent, and dangerous on any shared/CI host.

The discriminator is cheap to compute and should be computed BEFORE writing
a single fixture: *does the unit expose an input-source override?* This
splits the corpus into **cover-now** (has knob) and **defer-with-reason**
(no knob). For the defer set, the honest output is a documented scope note —
and, if the coverage is later wanted, the prerequisite is a one-line code
change (add the env knob), not a test heroics exercise. Privilege is a
secondary axis: some knob-driven finding conditions still need root (setuid
bit, chown to an unresolved uid, `setcap`) — gate those suites with a
self-skip probe so they degrade gracefully off-root.

A complementary insight: where the corpus SHOULD be uniformly coverable
(the module-lib scanners all consume a shared, knob-driven helper), encode
the coverage requirement as a guard test (selfdef's
`L2-watchdog-dedup-guard.bats` fails if a shared-helper watchdog ships
without a suite). The guard is scoped to exactly the cover-now set — it
must NOT demand suites from the defer set, or it becomes a forcing function
for false-coverage suites.

## Evidence

selfdef watchdog L2 backfill, 2026-05-27 (single session, direct-to-main):

| Class | Input contract | Hermetically testable? | Outcome |
|---|---|---|---|
| 65 module-lib detection-watchdogs | config files via `SELFDEF_<X>_{FILE,DIRS,FILES}` knobs | Yes (non-root) | Covered; locked by a 7th dedup-guard assertion |
| 18 integrity scanners with input knobs | `_ROOTS` / `_FILE` / `_DIRS` knobs | Yes (some need root: setuid/chown/setcap, self-skip otherwise) | Covered |
| 21 integrity scanners without knobs | live `/proc`, `ss`, clock, or hardcoded `/etc` | No (would need syscall faking or real-system mutation) | Deferred with reason; documented in `context.md` + SDD-062 D-4 |

Result: 1154 L2 bats cases across 105 suites + 99 Sigma rule-test cases,
all green; zero ok-path-only suites shipped. The classification step
(grep each scan script for an input-source knob) took minutes and prevented
21 low-value suites.

## Applicability

- Any test-backfill onto a corpus of environment-reading units (security
  scanners, config linters, host-baseline checkers, infra validators).
- Designing NEW such units: add the input-source env knob from the start —
  it is the testability seam. "Reads `/etc/foo`" → "reads
  `${TOOL_FOO_FILE:-/etc/foo}`" is the whole cost.
- Coverage guards / completeness checks: scope the guard to the cover-now
  set; never let it force the defer set into false-coverage suites.
- Reviewing a "we added tests for all N scanners" claim: ask which exercise
  the FINDING path vs only the ok path.

## Relationships

- BUILDS ON [[P4 — Declarations Are Aspirational Until Verified]] — an
  ok-path-only suite is a coverage declaration with no verification of the
  behavior that matters.
- PARALLELS the sovereign-os Layer-3 lesson (*real bugs surface only when
  tests execute actual renderers, not just schema-validate*) — both
  distinguish test SUBSTANCE from test APPEARANCE; this one adds the
  upstream precondition (you must be able to drive the real input at all).
- RELATES TO the selfdef SDD-062 watchdog-severity-routing arc — the L2
  suites this lesson is drawn from lock the per-watchdog functional severity
  that SDD-062 routes to the pager.
- CONSTRAINS test-backfill planning — scope is a function of input
  controllability, decided before fixtures are written.

## Promotion criteria

Promote draft → growing when a SECOND project applies the
classify-by-input-knob step to a scanner/validator corpus and records the
cover-now vs defer split. Promote growing → mature when the
"add the env knob = the testability seam" guidance has shaped the design of
a NEW corpus (knob added up front) in at least one project.

## Backlinks

_None yet — draft. Will be linked from the selfdef testing domain overview
and any future cross-project test-coverage pattern page on first citation._
