---
title: "Build Pipeline via SDD+TDD — Real Bugs Surface Only When Tests Execute Actual Renderers (Not Just Schema-Validate)"
aliases:
  - "Substantive vs scaffold tests"
  - "Layer 3 catches what Layer 1 cannot"
  - "Sovereign-OS arc Lesson 1"
type: lesson
domain: cross-domain
layer: 4
status: draft
confidence: high
maturity: seed
created: 2026-05-16
updated: 2026-05-16
last_reviewed: 2026-05-16
derived_from:
  - "P4 — Declarations Are Aspirational Until Infrastructure Verifies Them (PRIMARY parent — schema-conformance is a declaration; runtime behavior is the verification)"
  - "Models Are Built in Layers, Not All at Once (SFIF specialization — Layer 1 schema before Layer 3 execution; both must ship)"
  - "Infrastructure Must Be Reproducible, Not Manual (build pipeline as the manifestation)"
sources:
  - id: sovereign-os-main
    type: project
    project: cyberpunk042/sovereign-os
    path: main
  - id: sain-01-milestone
    type: wiki
    file: "wiki/backlog/milestones/sain-01-sovereign-node.md"
  - id: sdd-008-test-harness
    type: project
    project: cyberpunk042/sovereign-os
    path: docs/sdd/008-test-harness.md
  - id: directive-2026-05-16
    type: directive
    file: "raw/notes/2026-05-16-user-directive-sovereign-os-arc-opening.md"
tags:
  - sdd
  - tdd
  - layer-3-tests
  - substantive-tests
  - schema-vs-runtime
  - quality-bar
  - sovereign-os-arc
  - cross-domain
---

# Build Pipeline via SDD+TDD — Real Bugs Surface Only When Tests Execute Actual Renderers (Not Just Schema-Validate)

## Trigger

The sovereign-os arc shipped a complete OS-build pipeline (charter through Stage-2 onset) in one operator session, gated by SDD+TDD throughout. Layer 1 schema-conformance tests (~37 cases) and Layer 2 unit tests (~51 cases) both passed for the entire run. **Two bugs that the schema layer could not detect surfaced only when Layer 3 substantive tests (~36 assertions) executed the actual renderers against fake filesystems**:

1. **Whitelabel render template paths**: `whitelabel/default.yaml` declared template paths relative to `whitelabel/` (e.g., `templates/os-release.tmpl`) but the content files lived at `whitelabel/default/templates/...`. Schema-validation passed — the schema only required a string in the `template:` field. The render engine succeeded with a warning ("template not found") but emitted no file. A Layer 1 schema test would never catch this; only running the renderer against fake `/etc/` and asserting the file's content surfaced the gap.

2. **Orchestrator help truncation**: `scripts/build/orchestrate.sh` had a `cmd_help()` using `sed '1,/^Usage:/!d'` which deleted everything outside the 1..Usage range — accidentally stopping AT the Usage line and never emitting the Commands / Steps / Env-vars sections. Schema-validation cannot test sed behavior. Layer 2 unit tests of `classify()` or merger logic cannot test bash sed. Only a Layer 3 test that **ran the help command and asserted on its output** caught it.

## Finding

**Schema-conformance is necessary but not sufficient.** A complete TDD harness needs three sufficiency tiers, each catching a class of bug invisible to the layer below:

| Layer | Catches | Cannot catch |
|---|---|---|
| **Layer 1 (schema/lint)** | Typos · missing required fields · invalid enums · forbidden patterns | Semantic correctness of declared content; runtime behavior of code that *reads* the declarations |
| **Layer 2 (unit)** | Function-level logic errors in pure code (router rules, merger conflicts, template substitution) | Integration between functions; behavior when invoked from shell; file-system side effects |
| **Layer 3 (stage acceptance)** | Real bugs in the wired-up system (paths, file emission, help-text generation, hook resolution, command-surface invariants) | Boot-time invariants (Layer 4 QEMU) and hardware-conformance (Layer 5) |

The sovereign-os arc empirically confirmed: **the two bugs caught in one round of Layer 3 work would have shipped to the operator as a broken build** if the harness had stopped at Layer 1+2. The whitelabel render would silently emit nothing; the help command would silently truncate. Both are exactly the kind of "silent quality degradation" the operator's verbatim quality bar rejects:

> *"Do not rush anything and do not minimize anything nor should you compress or conflate or hallucinate anything"*
> *"we do this clean and right and professional"*

A schema-only TDD harness IS a silent compression: it declares "tests pass" while letting runtime regressions ship.

## Mechanism — why Layer 3 catches what Layer 1+2 cannot

Layer 1 (schema/lint) operates on **declarations**: the input YAML/config. It cannot reach into the renderer that *consumes* the declaration. Layer 2 (unit) operates on **functions in isolation**: it mocks the file system, the package manager, the network. It cannot validate that the chain of function calls produces the expected on-disk state.

Layer 3 substantive tests **run the actual code against fake but real filesystems** (`mktemp -d` instead of `/`). They assert on observable on-disk side effects: "after invoking the render engine, does `<tmpdir>/etc/os-release` exist? Does it contain the operator's chosen ID?" This is the cheapest level of testing that validates the **whole behavior**, not just the parts.

The cost is moderate: ~50 lines of bash per test, ~5 seconds per CI run. The leverage is high: two real bugs caught in one session.

## Action — the rule

**For every SDD+TDD project that ships scripts the operator will rely on, the TDD harness MUST include Layer 3 substantive tests, not just Layer 1 schema-validation.**

Concretely, every script that:
- Reads a configuration file and produces on-disk artifacts → needs a Layer 3 test that runs the script against a fake config in a tmpdir + asserts on the produced artifacts.
- Exposes a CLI surface (help/list/status/etc.) → needs a Layer 3 test that invokes each subcommand + asserts on its observable output (stdout, exit code, side-effect files).
- Resolves paths from configuration to disk → needs a Layer 3 test that runs the resolver + asserts the path is what was intended.

Schema validation alone catches typo bugs. Unit tests alone catch logic bugs. Layer 3 catches wiring bugs — which are the most common operationally-painful class.

The sovereign-os arc's harness applied this rule and surfaced two real wiring bugs within one Layer 3 test round. The discipline is general: it should apply to every project the wiki touches that ships scripts.

## Relationships

- BUILDS ON: [[the-agent-must-practice-what-it-documents|The Agent Must Practice What It Documents]] — A harness that declares Layer 3 coverage but ships only Layer 1+2 fails this principle.
- BUILDS ON: [[SFIF / [[models-are-built-in-layers-not-all-at-once|Models Are Built in Layers]] — Layer 1 ships first; Layer 3 ships during Infrastructure tier, not deferred to "post-Gate-5".]]
- RELATES TO: [[infrastructure-must-be-reproducible-not-manual|Infrastructure Must Be Reproducible]] — the tested artifact must be reproducibly buildable in CI for Layer 3 to be repeatable.

## Source — the sovereign-os arc concrete instance

The lesson originates from one session's work on `cyberpunk042/sovereign-os` (2026-05-16). Documented in `docs/sdd/008-test-harness.md` § Layer 3 + verified in:

- `tests/nspawn/test_whitelabel_render_to_disk.sh` (7 assertions caught the template-path bug)
- `tests/nspawn/test_orchestrator_status.sh` (14 assertions caught the help-truncation bug)
- `tests/nspawn/test_profile_hooks_resolve.sh` (26 assertions across 2 profiles validated 15+11 hook scripts resolve)

The arc's full inventory (build pipeline 9 steps + 19 hook scripts + render engine + sovereign-osctl + inference stack + selfdef integration design) shipped because the SDD-008-specified Layer 3 harness was treated as Stage-2-blocking, not Stage-2-deferred.

## Promotion criteria

This draft promotes to `02_synthesized` after:

- A second project (not sovereign-os) applies the rule and reports whether Layer 3 substantive tests catch bugs the schema+unit layers missed. If yes → synthesized. If no over 3 projects → re-examine the lesson.
- The arc's Stage-2 follow-up rounds confirm Layer 3 keeps catching wiring bugs as scripts evolve (not a one-time fluke).
- The selfdef Stage-2 work (SDDs 013-016) similarly applies the rule.

## Backlinks

[[the-agent-must-practice-what-it-documents|The Agent Must Practice What It Documents]]
[[Models Are Built in Layers]]
[[Infrastructure Must Be Reproducible]]
