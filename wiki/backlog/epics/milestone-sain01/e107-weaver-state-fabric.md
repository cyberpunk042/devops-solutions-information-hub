---
title: E107 — Weaver State Fabric
aliases:
  - "E107 — Weaver State Fabric"
  - "E107 — Weaver: Atomic State + Sub-Agent Routing"
type: epic
domain: backlog
status: draft
priority: P0
task_type: epic
current_stage: document
readiness: 30
progress: 0
stages_completed: []
artifacts: []
confidence: high
created: 2026-05-16
updated: 2026-05-16
sources:
  - id: milestone
    type: file
    file: "wiki/backlog/milestones/sain-01-sovereign-node.md"
  - id: src-sain-01-sovereign-node-spec
    type: wiki
    file: "wiki/sources/src-sain-01-sovereign-node-spec.md"
  - id: concept-srp-trinity-pulse-weaver-auditor
    type: wiki
    file: "wiki/domains/ai-agents/concept-srp-trinity-pulse-weaver-auditor.md"
  - id: concept-zfs-tiered-storage-llm-inference
    type: wiki
    file: "wiki/domains/devops/concept-zfs-tiered-storage-llm-inference.md"
tags: [epic, sain-01, weaver, state-fabric, atomic-writes, sync-always, podman, grpc, ccd-pinning, claude-md, soul-md, identity-md, agents-md]
---

# E107 — Weaver State Fabric

## Summary

Deploy the **Weaver** module — the second in the [[concept-srp-trinity-pulse-weaver-auditor|SRP Trinity]] — as a stateful orchestration layer on CCD 1 (cores 6-9, thread mask `0xff000`). The Weaver owns: the four context files (`IDENTITY.md` immutable persona, `SOUL.md` core behavioral logic, `AGENTS.md` routing table, `CLAUDE.md` active session — all on `tank/context` with `sync=always`), the atomic-state-transition protocol ([[src-sain-01-sovereign-node-spec|§ 21]] — `O_DIRECT | O_SYNC` write to `.tmp` + atomic `rename()`), Rootless Podman container management for sub-agent fleets, gRPC routing between sub-agents and the host. **L1 caveat**: full `O_DIRECT` semantics require OpenZFS 2.2+ (older silently falls back to buffered) — pin the version + verify at boot. The atomic-rename + `sync=always` combination is the load-bearing pattern even on older OpenZFS; the `O_DIRECT` flag is additive correctness, not a hard requirement.

## Operator Directive

> "the Weaver coordinates session state within CCD 1, driving synchronous, lockless file transactions straight onto a highly specialized ZFS layout"

## Goals

See Done When — verifiable atomic-state + sub-agent-routing checkpoints.

## Done When

- [ ] **Weaver daemon authored** as a long-running process pinned to CCD 1 cores 6-9 via systemd `CPUAffinity=6-9`
- [ ] **Atomic state writer implemented** per [[src-sain-01-sovereign-node-spec|§ 21.1]] — `O_DIRECT | O_SYNC` flags on the `.tmp` write + `rename()` to final path; 4K-aligned buffer allocation
- [ ] **OpenZFS version pinned** to ≥2.2 (verify via `zfs --version`); document fallback behavior if running older OpenZFS
- [ ] **Four context files** initialized on `tank/context`: `IDENTITY.md` (chmod 0444 — read-only), `SOUL.md` (writable via Weaver only), `AGENTS.md` (read-only to sub-agents, writable via Weaver), `CLAUDE.md` (atomic append-only)
- [ ] **Race-condition test**: launch two concurrent agents — one writes to `CLAUDE.md` 1000 times, the other reads 1000 times; **zero partial reads, zero stale reads**; verify via instrumented test harness
- [ ] **Podman Rootless** configured: `apt-get install -y podman uidmap`; user namespace mapping verified
- [ ] **Container storage on `tank/agents`**: Podman's graph driver mapped to `/mnt/vault/agents` via `containers.conf` or equivalent
- [ ] **gRPC interface** running: Weaver exposes a local-only gRPC endpoint for sub-agent state queries + mutation requests; protocol buffers schema documented
- [ ] **Sub-agent test**: launch a sandboxed Podman container (with `--device /dev/vfio/<3090_group>` to use the [[e103-vfio-isolation|VFIO 3090]]); container connects to Weaver gRPC; Weaver routes a state update; verified end-to-end
- [ ] **CCD locality preserved**: `taskset -p <weaver_pid>` shows mask `0xff000`; no thread migration off CCD 1 under load
- [ ] **Auditor integration**: Weaver's Podman container launches respect Tetragon allowlist (the launched binaries match `sovereign-kernel-fence` policy); zero false-positive kills
- [ ] **Snapshot strategy documented**: Weaver's state changes can be snapshot-rolled-back via `zfs snapshot tank/context@<timestamp>` cadence agreed with operator
- [ ] **Restart resilience**: kill the Weaver daemon mid-write; restart; verify `CLAUDE.md` is either pre-write or post-write content (atomic rename guarantee holds); no partial-write artifact

## Scale and Model

> [!info] Epic Parameters
>
> | Parameter | Value |
> |---|---|
> | **Model** | feature-development |
> | **Quality tier** | Skyscraper |
> | **Estimated tasks** | 10-12 |
> | **Dependencies** | E102 (ZFS `tank/context` with `sync=always`), E103 (VFIO sandbox for sub-agents), E104 (Auditor watches Weaver activity) |
> | **Feeds into** | E108 (Profile 2 / 3 require Weaver to route between tiers), E110 (Weaver routes model queries to the right resident model) |
> | **Substrate** | CCD 1 cores 6-9 (Weaver) + cores 10-11 (kernel/IRQ/ZFS-compression — outside Weaver's pin) |

## Handoff Context

> [!info] For a fresh context picking up this epic:
>
> - Milestone: [[sain-01-sovereign-node|Milestone — SAIN-01 Sovereign AI Node]]
> - L1 spec sections: [[src-sain-01-sovereign-node-spec|§ 7 State Fabric Map + § 21 Atomic State Transition Protocol]]
> - L2 Trinity concept (Weaver's responsibilities): [[concept-srp-trinity-pulse-weaver-auditor|SRP Trinity]]
> - L2 ZFS substrate: [[concept-zfs-tiered-storage-llm-inference|ZFS Tiered Storage]] — `tank/context` `sync=always` is the load-bearing knob
> - **OpenZFS 2.2+ caveat**: pre-2.2 silently falls back to buffered for `O_DIRECT`. The atomic-rename + `sync=always` pattern still works without `O_DIRECT`; the cleanest combination requires 2.2+.
> - **Auditor coordination**: every binary the Weaver launches in a container must be on the [[e104-tetragon-guardian-perimeter|Tetragon allowlist]]; coordinate policy updates at the same time as Weaver capability extensions

## Relationships

- PART OF: [[sain-01-sovereign-node|Milestone — SAIN-01 Sovereign AI Node]]
- DEPENDS ON: [[e102-zfs-storage-layout|E102 — ZFS Storage Layout]]
- DEPENDS ON: [[e103-vfio-isolation|E103 — VFIO Isolation]]
- DEPENDS ON: [[e104-tetragon-guardian-perimeter|E104 — Tetragon + Guardian Perimeter]]
- DEPENDS ON: [[e106-pulse-vector-runtime|E106 — Pulse Vector Runtime]] (Pulse is a state-input producer)
- ENABLES: [[e108-load-balancing-profiles|E108 — Load-Balancing Profiles]] (profiles operationalize Weaver routing)
- ENABLES: [[e110-model-catalog|E110 — Model Catalog]] (Weaver routes queries to the right model)
- IMPLEMENTS: [[concept-srp-trinity-pulse-weaver-auditor|Concept — SRP Trinity (Weaver module)]]
- IMPLEMENTS: [[concept-zfs-tiered-storage-llm-inference|Concept — ZFS Tiered Storage]] (writes to `tank/context`)
- IMPLEMENTS: [[src-sain-01-sovereign-node-spec|SAIN-01 Sovereign Node Spec]] §§ 7, 21

## Backlinks

(will be populated by `tools/obsidian.py backlinks` after pipeline post)
