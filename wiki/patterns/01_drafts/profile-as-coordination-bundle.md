---
title: "Profile as Coordination Bundle"
aliases:
  - "Profile as Coordination Bundle"
  - "Coordination Bundle Pattern"
type: pattern
domain: cross-domain
layer: 5
status: synthesized
confidence: high
maturity: seed
derived_from: []
instances:
  - page: "config/profiles/default.yaml (AICP)"
    context: "Balanced everyday profile coordinating backends + router thresholds + RAG depth + budget + cache + Docker envs via one switch"
  - page: "config/profiles/reliable.yaml (AICP)"
    context: "Production profile aggregating circuit_breaker + warmup + dlq + reports — 4 reliability subsystems coordinated by one profile name"
  - page: "config/profiles/dual-gpu.yaml (AICP)"
    context: "19 GB VRAM profile coordinating qwen3-30b-a3b primary + asymmetric KV cache + Docker envs + router failover chain — hardware-coupled bundle"
  - page: "config/profiles/benchmark.yaml (AICP)"
    context: "Deterministic evaluation profile coordinating temperature=0 + seed=42 + cache disabled + escalation_threshold=0 + budget unlimited across all subsystems"
  - page: "SDLC profiles (simplified / default / full)"
    context: "Brain's own SDLC profile system coordinates methodology stages + artifact requirements + PM level + trust tier — coordination bundle at the methodology layer"
  - page: "Context injection profiles (Expert / Capable / Lightweight)"
    context: "Per tier, coordinates context depth + token budget + tool-call depth + compaction behavior — bundle at the context engineering layer"
created: 2026-04-18
updated: 2026-04-18
sources:
  - id: aicp-profiles-impl
    type: file
    file: aicp/core/profiles.py
    description: "600-line profile loader/validator/resolver/diff engine with `extends:` inheritance, deep merge, circular-detection (AICP project)"
  - id: aicp-profile-tests
    type: file
    file: tests/test_profiles.py
    description: "49 tests covering load order, inheritance, deep merge, circular detection (AICP project)"
  - id: aicp-makefile
    type: file
    file: Makefile
    description: "profile-list / profile-show / profile-diff / profile-validate / profile-use Make targets (AICP project)"
  - id: aicp-contribution
    type: wiki
    file: raw/articles/from-aicp/patterns/01_drafts/profile-as-coordination-bundle.md
    description: "Original contribution from AICP 2026-04-18, staged in raw/ before ingestion here"
tags: [pattern, profile, coordination, configuration, bundling, cross-subsystem, aicp]
contributed_by: "aicp"
contribution_source: "/home/jfortin/devops-expert-local-ai"
contribution_date: "2026-04-18"
contribution_status: accepted
---

# Profile as Coordination Bundle

## Summary

A **profile** is a single named handle that simultaneously coordinates settings across multiple subsystems whose tuning must move together. Switching profile (e.g., `make profile-use PROFILE=fast`) changes backends, router thresholds, RAG depth, budget, cache, timeouts, circuit-breaker config, warmup config, DLQ config, metrics config, reports config, AND Docker environment vars in one atomic operation. The pattern works because the bundled settings have **shared meaning** — calling something "the fast profile" is more honest than asking the operator to tune 12 parameters consistently. Contributed from AICP's 2026-04-18 profile implementation (`aicp/core/profiles.py`, 600 lines, 49 tests), generalized to cross-domain with two brain-native instances already visible: SDLC profiles (simplified / default / full) and Context Engineering tier profiles (Expert / Capable / Lightweight).

> [!info] Pattern Reference Card
>
> | Subsystem | What the profile controls | Why it must move together |
> |-----------|--------------------------|---------------------------|
> | backends | Primary model, failover chain | A "fast" profile can't pair 30B primary with low-latency expectations |
> | router | Complexity thresholds, escalation cutoff, force_cloud_modes | Aggressive escalation needs aggressive cloud routing |
> | RAG | Retrieval depth, reranker on/off | Long-context profiles want deep RAG; latency profiles want shallow |
> | budget | Token budget per request | "Thorough" wants larger; "fast" wants smaller |
> | cache | TTL, max size, key strategy | Benchmark disables cache; reliable enables |
> | timeouts | Request, cold start, retries | Heartbeat wants short; thorough wants long |
> | circuit_breaker | failure_threshold, recovery_timeout | Aggressive threshold=2; permissive threshold=5 |
> | warmup | enabled, model list | Production wants warmup; ephemeral doesn't |
> | dlq | max_retries, retry_delay | Production retries 5x; benchmark retries 0 |
> | metrics | persist, snapshot interval | Production persists; benchmark doesn't |
> | reports | enabled, interval, ntfy notification | Production reports every 4h; ephemeral doesn't |
> | Docker envs | CONTEXT_SIZE, LLAMACPP_PARALLEL, THREADS | Coupled — per-slot context requires container restart |

## Pattern Description

A **coordination bundle** is a named configuration grouping where the elements MUST move together to be coherent. The pattern recurs whenever a single tuning decision (e.g., "optimize for latency") propagates across multiple independent subsystems with their own native config formats. Without bundling, the operator must hand-coordinate N settings across N config files, hoping not to introduce inconsistency. With bundling, the operator picks ONE name and the system applies the consistent setting set everywhere.

> [!warning] Recognition signal — a config has settings that are individually valid but combinations are not
>
> Example: setting `failover_chain: [local]` (offline) while also setting `force_cloud_modes: [edit, act]` is incoherent — the chain says "no cloud" but the modes say "always cloud for edit/act." Each setting validates in isolation; only the combination is broken. **This is the signature of a bundle that should be coordinated.**

A profile bundle has three properties:

1. **Atomic switch** — one command changes all bundled settings at once. No intermediate state where some subsystems use the new setting and others don't.
2. **Validation across subsystems** — coherence checked between bundled settings (incompatible combinations rejected before they reach runtime).
3. **Inheritance with deep merge** — profiles `extends:` other profiles. `reliable extends default` means "everything from default plus the reliability-specific overrides." Avoids copy-paste of common settings across many profile files.

> [!abstract] Profile lifecycle (shape AICP's implementation demonstrates)
>
> | Stage | What happens | Mechanism |
> |-------|-------------|-----------|
> | Define | Operator authors `config/profiles/<name>.yaml` | YAML with optional `extends:` chain |
> | Validate | `make profile-validate` checks schema + cross-subsystem coherence | profile-validator module |
> | Resolve | `make profile-show PROFILE=<name>` renders merged final config | Resolver walks `extends:` chain, deep merges |
> | Compare | `make profile-diff PROFILE_A=fast PROFILE_B=offline` | Diff engine reports per-subsystem deltas |
> | Activate | `make profile-use PROFILE=<name>` writes `.env` + restarts containers | Atomic — Docker compose restart picks up new envs |
> | Override | CLI flag (`--profile fast`) or env var | Per-request override without rewriting `.env` |

## Instances

### Instance 1: AICP `default` profile — balanced everyday use

AICP's `config/profiles/default.yaml` coordinates: qwen3-8b as primary backend, full failover chain (local → fleet → openrouter → claude), complexity thresholds `[0.3, 0.6]`, escalation threshold `< 0.25`, RAG depth = 3 chunks, request timeout = 60s, circuit breaker threshold = 5, warmup disabled, DLQ retries = 3, metrics persist = true, Docker `LLAMACPP_PARALLEL=2 CONTEXT_SIZE=16384`. The 12 settings are individually valid but tuning them by hand requires understanding the interactions. The profile name "default" carries the shared meaning ("balanced everyday").

### Instance 2: AICP `reliable` profile — production fleet operation

`config/profiles/reliable.yaml` aggregates 4 reliability subsystems: aggressive circuit breaker (threshold=2 vs default 5), auto-warmup (qwen3-8b + nomic-embed pre-loaded), DLQ with max_retries=5 (vs default 3) and 30s retry_delay, health reports every 4 hours with ntfy notification. Each subsystem has its own config section (`circuit_breaker:`, `warmup:`, `dlq:`, `reports:`) but they make sense ONLY together — enabling warmup without aggressive breaker is wasteful (warmup prevents the failures the breaker would catch); enabling DLQ retries without breaker means failed tasks pile up against a dead backend.

### Instance 3: AICP `dual-gpu` profile — 19 GB VRAM MoE inference

`config/profiles/dual-gpu.yaml` coordinates the qwen3-30b-a3b MoE model + asymmetric KV cache (q4_0 quantization on the smaller GPU) + expanded Docker context (CONTEXT_SIZE=32768) + tier dispatch that prefers the larger model. Hardware constraint: requires both RTX 2080 (8 GB) and RTX 2080 Ti (11 GB) to be present. Profile validation rejects this profile when only one GPU is detected. **Hardware-coupled profiles are a sub-pattern**: the bundle's coherence depends on the host environment, not just the config files. Became operational 2026-04-17 per [[aicp|AICP]] Stage 3 hardware unlock.

### Instance 4: AICP `benchmark` profile — deterministic evaluation

`config/profiles/benchmark.yaml` enforces deterministic outputs across the entire stack: `temperature: 0` + `seed: 42` + `escalation_threshold: 0` (never escalate, return whatever local produces) + `cache: disabled` (no cache hits skewing measurement) + `budget: unlimited` (don't truncate for cost reasons during benchmarking). This is the classic anti-coordination problem: benchmarking requires that NO subsystem make non-deterministic choices, but each subsystem has its own determinism knob. The profile bundles all the knobs into one named "benchmark mode."

### Instance 5: Brain's own SDLC profiles (simplified / default / full)

The [[sdlc-customization-framework|SDLC Customization Framework]] defines three SDLC profiles. Each coordinates: methodology stages (3 vs 5 vs 6), artifact requirements (none vs selected vs full), PM level (L1 vs L2 vs L3), trust tier expectations, gate strictness (advisory vs blocking). A project cannot consistently say "I'm POC/micro" while running 6 enforced stages — the bundling at the methodology layer is what keeps the Goldilocks protocol coherent.

### Instance 6: Context engineering tier profiles (Expert / Capable / Lightweight)

The [[model-context-engineering|Model — Context Engineering]] tier system coordinates: context depth in tokens (5-10K / 2-5K / 500-1K), tool-call depth allowed, compaction behavior, memory write frequency, injection latency budget. These are tuned together because a "Lightweight" model with "Expert" token depth OOMs; an "Expert" model with "Lightweight" token depth underperforms. The tier name carries the shared meaning across the bundled dimensions.

## When To Apply

- **Multiple subsystems with shared tuning intent.** If switching from "production mode" to "debug mode" should change 5+ config sections at once, you need a profile.
- **Operator-facing knob count > 5.** When the operator must remember 5+ settings to make a coherent change, the cognitive load is too high — bundle them.
- **Subsystems can be combined into incoherent states.** If invalid combinations exist, validate at the bundle level, not per-setting.
- **Settings live in multiple files / formats.** YAML + `.env` + Docker compose envs + Makefile vars — a bundle abstracts over the format split.
- **Environment-coupled overrides** (dev vs staging vs production). Profiles let `extends: default` add only the deltas per environment, no copy-paste.

## When Not To

- **Single-subsystem tuning.** If only one config section changes, a CLI flag or single env var is simpler. Don't bundle one setting.
- **Truly orthogonal settings.** If two settings genuinely don't interact (logging verbosity vs network port), bundling creates false coupling.
- **Operator knows exactly which N settings they want.** If the operator is an expert tuning 12 settings consistently, bundles slow them down. Profiles target the common case, not expert mode.
- **Settings change at different cadences.** If setting A changes every request and setting B changes once a week, bundling forces them to a single cadence.

## Tradeoffs

> [!warning] The bundling cost
>
> | Cost | Mitigation |
> |------|-----------|
> | Profile files multiply (AICP has 9; future could have 30) | Use `extends:` to share common settings; name profiles by use case not by setting combination |
> | New settings must be added to all relevant profiles | Validator flags missing settings; CI check fails when a profile lacks a required field |
> | Profile semantics drift over time ("fast" becomes "default") | Document profile intent in the YAML's `description:` field; `make profile-diff` surfaces drift |
> | Operators may use profiles ritualistically without understanding | Standards: every profile has `description:`; `make profile-show` renders the resolved settings |

## Relationships

- BUILDS ON: [[sdlc-customization-framework|SDLC Customization Framework]] (profile-as-bundle at the methodology layer)
- BUILDS ON: [[model-context-engineering|Model — Context Engineering]] (tier-profiles as coordination bundles at the context layer)
- RELATES TO: [[goldilocks-protocol|Sub-Model — Goldilocks Protocol]] (identity → profile selection is the upstream mechanism)
- RELATES TO: [[model-local-ai|Model — Local AI ($0 Target)]] (AICP's 9 profiles configure routing-layer bundles)
- RELATES TO: [[aicp|AICP]] (canonical implementation)
- RELATES TO: [[three-layer-autocomplete-chain-validated-in-production-fleet|Three-Layer Autocomplete Chain Validated]] (per-tier context budgets are profile-coupled — same pattern, context-layer scope)
- RELATES TO: [[[[boilerplate-skill-anti-pattern-at-scale:-47%-of-aicps-78-ski|Boilerplate Skill Anti-Pattern at Scale]] (skills load conditionally per task; profiles configure conditionally per deployment — same per-context-config principle, different scope)]]
- FEEDS INTO: [[model-registry|Model Registry]]

## Backlinks

[[SDLC Customization Framework]]
[[model-context-engineering|Model — Context Engineering]]
[[Sub-Model — Goldilocks Protocol]]
[[model-local-ai|Model — Local AI ($0 Target)]]
[[aicp|AICP]]
[[Three-Layer Autocomplete Chain Validated]]
[[Boilerplate Skill Anti-Pattern at Scale]]
[[model-registry|Model Registry]]
[[boilerplate-skill-anti-pattern-at-scale:-47%-of-aicps-78-ski|Boilerplate skill anti-pattern at scale: 47% of AICP's 78 skills are identical instruction dumps]]
