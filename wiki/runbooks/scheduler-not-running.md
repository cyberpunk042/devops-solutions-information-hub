---
title: "Operator runbook — Goldilocks Scheduler not running"
type: reference
domain: ai-agents
layer: 2
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
    note: "Source dump tail lines 18000-18250 (scheduling architecture)"
  - id: selfdef-sdd-031
    type: internal
    project: selfdef
    path: docs/sdd/031-goldilocks-scheduler.md
    note: "SDD-031 Goldilocks Scheduler specification"
  - id: selfdef-ms048
    type: internal
    project: selfdef
    path: backlog/milestones/MS048-goldilocks-scheduler-hardware-aware-resource-routing.md
    note: "Catalog milestone MS048 (247 R-rows)"
tags: [runbook, scheduler, goldilocks, four-watchdog, sain-01, selfdef, ips, routing-layer]
---

# Operator runbook — Goldilocks Scheduler not running

## Symptom

One or more of:

- `selfdefctl scheduler show` reports `audit chain events: chain check failed` OR `(no scheduler decisions in ring buffer)` AND the system has been running for non-trivial time.
- `systemctl status selfdef-scheduler.service` is `inactive (dead)` or `failed`.
- The `selfdefctl trio` four-watchdog set shows `[UNKNOWN     ]` for the scheduler row indefinitely.
- `journalctl -u selfdefd | grep scheduler` shows the WARN line `scheduler: ring buffer read failed` or `scheduler: audit chain check failed`.

## Why this matters

The Goldilocks Scheduler is the **runtime routing layer** between requests and the hardware tiers (RTX PRO 6000 Blackwell oracle + RTX 3090 scout + Ryzen 9900X AVX-512 cortex). When the scheduler is not running:

- No 7-axis objective evaluation per request
- No per-profile rule enforcement (fast vs careful vs production all degrade to first-route-available)
- No backpressure surfaces — Blackwell VRAM / 3090 GPU / CPU PSI / RAM PSI / IO PSI / human-gate-queue thresholds are not measured or applied
- No decision audit log → operators lose the replay/counterfactual capability (MS048 R11393-R11398)

Per the dump's Key Scheduling Law (verbatim, line 18256-18257):

> Never let expensive cognition wait on cheap preparation.
> Never let cheap speculation commit without expensive verification when risk demands it.

Without the scheduler, both halves of that law are unenforced.

## Diagnosis

```bash
systemctl status selfdef-scheduler.service
systemctl is-active selfdef-scheduler.service
journalctl -u selfdef-scheduler.service -n 200 --no-pager
ls -la /usr/local/bin/selfdef-scheduler
ls -la /mnt/vault/context/ 2>/dev/null
ls -la /var/cache/selfdef/scheduler/ring 2>/dev/null
```

1-step-up-the-stack causes:

| Cause | Investigation |
|---|---|
| Binary not installed | `dpkg -l \| grep selfdef-daemon`; reinstall package |
| `/mnt/vault/context` not writable | `ls -la /mnt/vault/context`; ZFS dataset mounted ro? |
| zfs-mount.service not started | `systemctl status zfs-mount.service`; the scheduler After= chain blocks until ZFS mounts |
| Restart loop > StartLimitBurst=10/60s | systemd backed off; check journalctl for the trigger |
| guardian or tetragon not up | scheduler After=selfdef-guardian.service + tetragon.service; check those |
| PSI files missing (kernel without PSI support) | `cat /proc/pressure/cpu` — needs CONFIG_PSI=y |

## Recovery procedure

### 1. Confirm the service status

```bash
systemctl status selfdef-scheduler.service
```

### 2. Restart the scheduler

```bash
sudo systemctl start selfdef-scheduler.service
sudo journalctl -u selfdef-scheduler.service -n 50 --no-pager
```

If it starts, verify ingestion + decision emission is happening:

```bash
selfdefctl scheduler show
selfdefctl trio
```

The scheduler row should populate as requests flow through the routing layer.

### 3. If scheduler refuses to start

Common failure → fix:

| journalctl signature | Likely fix |
|---|---|
| `Permission denied` on `/mnt/vault/context/scheduler_audit.log` | ZFS dataset ro OR ownership wrong. Fix via `chown selfdef:selfdef /mnt/vault/context` and ensure dataset is rw. See [friction-audit-zfs](friction-audit-zfs.md). |
| `start-limit-hit` | Reset with `systemctl reset-failed selfdef-scheduler.service` after the underlying cause is fixed. |
| `/proc/pressure/cpu: No such file` | Kernel lacks PSI support. Recompile with CONFIG_PSI=y or use a kernel ≥ 5.2 with PSI enabled. The scheduler can run without PSI but its backpressure surfaces degrade to always-clean — that defeats the safety invariants. |
| `failed to bind to selfdef-guardian.service` | Guardian must be up. See [guardian-not-running](guardian-not-running.md). |

### 4. Verify the four-watchdog set is healthy

```bash
selfdefctl trio
```

All four rows should report `[OK ...]` or operator-recognized state (UNKNOWN for empty ring is OK on a freshly-booted host).

### 5. Verify audit chain integrity

```bash
selfdefctl scheduler audit-cycle replay
```

Exit 0 + "chain intact" confirms the SHA-256 chain has not been broken. Exit 1 → see [scheduler-audit-log-corruption](scheduler-audit-log-corruption.md).

## Operator decision tree

- **Scheduler crash-looping after kernel upgrade**: pin a kernel version that ships PSI support (≥ 5.2). The scheduler runtime crate is portable; the dependency is on `/proc/pressure/*` availability.
- **Scheduler crash-looping after upgrade**: schema_version drift between the scheduler binary and the mirror crate is the most common cause. Check the OCSF/audit-log entries' `schema_version` field matches what the binary expects.
- **Host shouldn't run the scheduler** (no GPUs, no Blackwell, single-tier inference): disable it with `systemctl disable selfdef-scheduler.service`. The four-watchdog set degrades to a three-watchdog set — friction-audit + perimeter + guardian still enforce; only routing decisions are made by default first-available-route.
- **Repeated restarts in short windows**: don't disable `Restart=always`; that defeats the routing-layer recovery. Diagnose the root cause.

## Relationships

### Cross-references

- SDD-031 §Deliverable 5 (systemd unit)
- SDD-031 §Deliverable 10 (daemon boot observability)
- Sister runbook: [scheduler-backpressure-stuck-open](scheduler-backpressure-stuck-open.md)
- Sister runbook: [scheduler-audit-log-corruption](scheduler-audit-log-corruption.md)
- Four-watchdog set:
  - [friction-audit-pcie](friction-audit-pcie.md) (hardware frame)
  - [perimeter-tetragon-not-running](perimeter-tetragon-not-running.md) (kernel syscall)
  - [guardian-not-running](guardian-not-running.md) (supervisor tier)
