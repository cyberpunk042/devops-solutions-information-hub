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

## Summary

In a SDD+TDD-gated build pipeline, schema-conformance tests (Layer 1) and unit tests (Layer 2) both passing does NOT prove the wired-up system works. Substantive Layer 3 tests — running actual renderers / scripts / CLI commands against fake-but-real filesystems and asserting on observable side-effects — catch the wiring bugs that Layers 1+2 cannot detect by construction. Empirically validated in the sovereign-os arc (2026-05-16): one round of Layer 3 testing surfaced 2 production-breaking bugs (whitelabel render emitting no file; orchestrator help truncating) that schema-validation passed clean. Layer 3 is the cheapest tier that validates whole-behavior; for any SDD+TDD project shipping scripts the operator will rely on, Layer 3 substantive tests are required, not optional.

## Context

This lesson activates when ALL of the following hold:

- Project ships build / install / configuration / orchestration scripts the operator will run
- SDD+TDD methodology is in use (specs gate scaffold; failing tests gate Green per `wiki/config/methodology-profiles/test-driven.yaml`)
- A test harness is being designed (or evaluated) for the project
- Layer 1 (schema/lint) tests already exist and pass; question is whether harness is complete
- The artifacts produced are CONSUMED by downstream code (renderers, packagers, CLI commands) that schema validation cannot reach into

The sovereign-os arc shipped a complete OS-build pipeline (charter through Stage-2 onset) in one operator session, gated by SDD+TDD throughout. Layer 1 schema-conformance tests (~37 cases) and Layer 2 unit tests (~51 cases) both passed for the entire run. **Two bugs that the schema layer could not detect surfaced only when Layer 3 substantive tests (~36 assertions) executed the actual renderers against fake filesystems**:

1. **Whitelabel render template paths**: `whitelabel/default.yaml` declared template paths relative to `whitelabel/` (e.g., `templates/os-release.tmpl`) but the content files lived at `whitelabel/default/templates/...`. Schema-validation passed — the schema only required a string in the `template:` field. The render engine succeeded with a warning ("template not found") but emitted no file. A Layer 1 schema test would never catch this; only running the renderer against fake `/etc/` and asserting the file's content surfaced the gap.

2. **Orchestrator help truncation**: `scripts/build/orchestrate.sh` had a `cmd_help()` using `sed '1,/^Usage:/!d'` which deleted everything outside the 1..Usage range — accidentally stopping AT the Usage line and never emitting the Commands / Steps / Env-vars sections. Schema-validation cannot test sed behavior. Layer 2 unit tests of `classify()` or merger logic cannot test bash sed. Only a Layer 3 test that **ran the help command and asserted on its output** caught it.

## Insight

> [!warning] Schema-conformance is necessary but not sufficient
>
> A complete TDD harness needs three sufficiency tiers, each catching a class of bug invisible to the layer below. A schema-only TDD harness IS a silent compression: it declares "tests pass" while letting runtime regressions ship. The sovereign-os arc empirically confirmed: **the two bugs caught in one round of Layer 3 work would have shipped as a broken build** if the harness had stopped at Layer 1+2 — silently emitting nothing for the whitelabel render; silently truncating the help command. Both are exactly the kind of "silent quality degradation" the operator's verbatim quality bar rejects: *"Do not rush anything and do not minimize anything nor should you compress or conflate or hallucinate anything"* + *"we do this clean and right and professional"*.

| Layer | Catches | Cannot catch |
|---|---|---|
| **Layer 1 (schema/lint)** | Typos · missing required fields · invalid enums · forbidden patterns | Semantic correctness of declared content; runtime behavior of code that *reads* the declarations |
| **Layer 2 (unit)** | Function-level logic errors in pure code (router rules, merger conflicts, template substitution) | Integration between functions; behavior when invoked from shell; file-system side effects |
| **Layer 3 (stage acceptance)** | Real bugs in the wired-up system (paths, file emission, help-text generation, hook resolution, command-surface invariants) | Boot-time invariants (Layer 4 QEMU) and hardware-conformance (Layer 5) |

### Mechanism — why Layer 3 catches what Layer 1+2 cannot

Layer 1 (schema/lint) operates on **declarations**: the input YAML/config. It cannot reach into the renderer that *consumes* the declaration. Layer 2 (unit) operates on **functions in isolation**: it mocks the file system, the package manager, the network. It cannot validate that the chain of function calls produces the expected on-disk state.

Layer 3 substantive tests **run the actual code against fake but real filesystems** (`mktemp -d` instead of `/`). They assert on observable on-disk side effects: "after invoking the render engine, does `<tmpdir>/etc/os-release` exist? Does it contain the operator's chosen ID?" This is the cheapest level of testing that validates the **whole behavior**, not just the parts.

The cost is moderate: ~50 lines of bash per test, ~5 seconds per CI run. The leverage is high: two real bugs caught in one session.

## Evidence

The lesson originates from one session's work on `cyberpunk042/sovereign-os` (2026-05-16). Documented in `docs/sdd/008-test-harness.md` § Layer 3 + verified in 3 independent test files, each catching a distinct wiring bug class:

1. **`tests/nspawn/test_whitelabel_render_to_disk.sh`** (7 assertions) — caught the **template-path bug**: schema-validation declared `template: <path-string>` valid; render engine consumed the path but emitted no file because the relative-path declared in `whitelabel/default.yaml` resolved to a non-existent location. Schema/unit layers had no way to detect this; only running the renderer against a tmpdir and asserting on the produced file caught the gap. Source: [cyberpunk042/sovereign-os docs/sdd/008-test-harness.md](https://github.com/cyberpunk042/sovereign-os) § Layer 3.

2. **`tests/nspawn/test_orchestrator_status.sh`** (14 assertions) — caught the **help-truncation bug** in `scripts/build/orchestrate.sh`: a `sed '1,/^Usage:/!d'` pattern was deleting all content after the Usage line, silently truncating Commands/Steps/Env-vars output. Pure shell behavior unreachable by schema or unit tests; only invoking the actual `--help` flag and asserting on stdout caught it. Source: same SDD § Layer 3.

3. **`tests/nspawn/test_profile_hooks_resolve.sh`** (26 assertions across 2 profiles) — validated that 15+11 hook scripts in the two declared profiles actually resolve to existing files with correct permissions. Hook-resolution wiring is exactly the integration-between-declaration-and-disk that Layer 3 is designed for. Source: same SDD § Layer 3.

Convergent finding: each of the 3 tests caught a bug class invisible to schema/unit tests. The 2-bug yield from a single Layer 3 round (37 + 51 + 36 = 124 test cases total; 2 bugs caught at Layer 3 only) demonstrates Layer 3 is the leverage point for wiring-bug detection.

## Applicability

> [!tip] The rule
>
> For every SDD+TDD project that ships scripts the operator will rely on, the TDD harness MUST include Layer 3 substantive tests, not just Layer 1 schema-validation.

Concretely, every script that:

| Script behavior | Required Layer 3 test |
|---|---|
| Reads a configuration file and produces on-disk artifacts | Run the script against fake config in a tmpdir + assert on produced artifacts (paths, content, permissions) |
| Exposes a CLI surface (help/list/status/etc.) | Invoke each subcommand + assert on observable output (stdout, exit code, side-effect files) |
| Resolves paths from configuration to disk | Run the resolver + assert the path is what was intended (NOT just that schema validation passed) |
| Chains multiple functions across module boundaries | Test the chain end-to-end against a tmpdir; mocking each function in isolation cannot prove the chain works |
| Generates files consumed by downstream tools | Render the file + invoke the downstream tool against it + assert the downstream tool succeeds |

**Where this lesson does NOT apply:**

- Pure-logic libraries with no filesystem / CLI / external-process side effects — Layer 2 unit tests already cover the whole behavior; Layer 3 is no-leverage there
- Documentation-only projects (no scripts to ship) — schema-validation IS the whole behavior; Layer 3 doesn't exist
- Boot-time / hardware-conformance assertions — those are Layer 4 (QEMU) and Layer 5 (real hardware); separate concern beyond this lesson's scope
- Throwaway prototypes — Layer 3 cost not justified if the script will not ship

Schema validation alone catches typo bugs. Unit tests alone catch logic bugs. Layer 3 catches wiring bugs — the most common operationally-painful class for scripts that wire declarations to disk.

## Relationships

- DERIVED FROM: [[declarations-are-aspirational-until-infrastructure-verifies-them|P4 — Declarations Are Aspirational Until Verified]] — schema-conformance is a declaration; runtime behavior is the verification. Layer 3 is the P4 cascade at the test-harness layer.
- DERIVED FROM: [[models-are-built-in-layers-not-all-at-once|Models Are Built in Layers, Not All at Once]] — SFIF specialization: Layer 1 schema ships first; Layer 3 ships during Infrastructure tier, not deferred to "post-Gate-5".
- BUILDS ON: [[the-agent-must-practice-what-it-documents|The Agent Must Practice What It Documents]] — A harness that declares Layer 3 coverage but ships only Layer 1+2 fails this principle.
- RELATES TO: [[infrastructure-must-be-reproducible-not-manual|Infrastructure Must Be Reproducible]] — the tested artifact must be reproducibly buildable in CI for Layer 3 to be repeatable.

## Promotion criteria

This draft promotes to `02_synthesized` after:

- A second project (not sovereign-os) applies the rule and reports whether Layer 3 substantive tests catch bugs the schema+unit layers missed. If yes → synthesized. If no over 3 projects → re-examine the lesson.
- The arc's Stage-2 follow-up rounds confirm Layer 3 keeps catching wiring bugs as scripts evolve (not a one-time fluke).
- The selfdef Stage-2 work (SDDs 013-016) similarly applies the rule.

## Backlinks

[[P4 — Declarations Are Aspirational Until Verified]]
[[models-are-built-in-layers-not-all-at-once|Models Are Built in Layers, Not All at Once]]
[[the-agent-must-practice-what-it-documents|The Agent Must Practice What It Documents]]
[[Infrastructure Must Be Reproducible]]
