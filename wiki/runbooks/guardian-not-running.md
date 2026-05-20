---
title: "Operator runbook — Guardian Daemon not running"
type: reference
domain: ai-agents
layer: 2
status: draft
confidence: high
maturity: seed
created: 2026-05-20
updated: 2026-05-20
sources:
  - id: sain-01-dump-2026-05-15
    type: directive
    project: devops-solutions-information-hub
    path: raw/dumps/2026-05-15-sain-01-master-spec-other-conversation-transposition.md
    note: "Source dump §10 — Guardian Daemon / guardian-core (lines 513-588)"
  - id: selfdef-sdd-029
    type: internal
    project: selfdef
    path: docs/sdd/029-guardian-daemon.md
    note: "SDD-029 guardian-daemon specification"
  - id: selfdef-ms044
    type: internal
    project: selfdef
    path: backlog/milestones/MS044-guardian-daemon-tetragon-ebpf-supervisor.md
    note: "Catalog milestone MS044"
tags: [runbook, guardian, tetragon, supervisor, sigkill, console-alert, zfs, audit-log, sain-01, selfdef, ips]
---

# Operator runbook — Guardian Daemon not running

## Symptom

One or more of:

- `selfdefctl guardian show` displays `tetragon socket: ... (PRESENT)` but no recent verdicts AND the daemon is supposed to be running.
- `systemctl status selfdef-guardian.service` is `inactive (dead)` or `failed`.
- The cockpit M066 panel shows `Guardian — DEGRADED` or no recent verdicts despite known Tetragon-fired SIGKILLs.
- `journalctl -u selfdef-guardian.service` shows crashes or `Restart=always` re-loops without converging.

## Why this matters

Guardian is the supervisor tier of the three-watchdog trio (friction-audit at hardware frame, perimeter at kernel syscall, guardian at supervisor tier). When Guardian is down:

- No `podman kill` fan-out for Tetragon-emitted events
- No atomic ZFS audit log append (`/mnt/vault/context/security_audit.log`)
- No native console alert (`/dev/console` BEL)
- No OCSF Detection 2004 emission for the Guardian response

The in-kernel Tetragon perimeter (MS047) still fires SIGKILL — but the supervisor-tier observability + cross-cgroup containment + audit chain are silent until Guardian comes back.

## Diagnosis

```bash
systemctl status selfdef-guardian.service
systemctl is-active selfdef-guardian.service
journalctl -u selfdef-guardian.service -n 200 --no-pager
ls -la /usr/local/bin/selfdef-guardian
ls -la /var/run/tetragon/tetragon.events 2>/dev/null
ls -la /mnt/vault/context/ 2>/dev/null
```

1-step-up-the-stack causes:

| Cause | Investigation |
|---|---|
| Binary not installed | `dpkg -l \| grep selfdef-daemon`; reinstall package |
| Tetragon socket missing | see [perimeter-tetragon-not-running](perimeter-tetragon-not-running.md) (shared upstream dependency) |
| ZFS pool not mounted | `zpool status tank/vault`; if absent see [friction-audit-zfs](friction-audit-zfs.md) |
| `/mnt/vault/context` not writable | `ls -la /mnt/vault/context`; ZFS dataset mounted ro? |
| Restart loop > StartLimitBurst=10/60s | systemd backed off; check journalctl for the trigger |
| `/dev/console` permission denied | hardening too strict for the host; check DeviceAllow line in unit |

## Recovery procedure

### 1. Confirm the service status

```bash
systemctl status selfdef-guardian.service
```

### 2. Restart Guardian

```bash
sudo systemctl start selfdef-guardian.service
sudo journalctl -u selfdef-guardian.service -n 50 --no-pager
```

If it starts, verify ingestion is happening:

```bash
selfdefctl guardian show
```

The `last verdicts` section should populate as Tetragon emits events.

### 3. If Guardian refuses to start

Common failure → fix:

| journalctl signature | Likely fix |
|---|---|
| `No such file or directory` on `/var/run/tetragon/tetragon.events` | Tetragon not running. See [perimeter-tetragon-not-running](perimeter-tetragon-not-running.md). |
| `Permission denied` on `/dev/console` | The container/VM does not expose the console device. Operator-extension: edit the unit to drop `DeviceAllow=/dev/console rw` for this host. Console alerts will Skip gracefully (not Fail). |
| `Permission denied` on `/mnt/vault/context/security_audit.log` | ZFS dataset is read-only OR ownership wrong. Fix via `chown selfdef:selfdef /mnt/vault/context` and ensure the dataset is mounted read-write. |
| `start-limit-hit` | Reset with `systemctl reset-failed selfdef-guardian.service` after the underlying cause is fixed. |
| Verifier rejected eBPF | Not a Guardian failure — Tetragon is the eBPF loader. See [perimeter-policy-load-failure](perimeter-policy-load-failure.md). |

### 4. Verify the three-watchdog trio is healthy

```bash
selfdefctl friction-audit show   # hardware frame (MS046)
selfdefctl perimeter show         # kernel syscall (MS047)
selfdefctl guardian show          # supervisor tier (MS044)
```

All three should show `PRESENT` / `OK` aggregates.

## Operator decision tree

- **Guardian crash-looping after kernel upgrade**: pin a Tetragon version compatible with the new kernel; Guardian itself rarely has kernel coupling — its UNIX-socket reader is portable.
- **Guardian crash-looping after `selfdef-daemon` upgrade**: check `journalctl -u selfdef-guardian.service` for the actual error. Common: schema_version drift if a partial upgrade left the mirror crate out of sync.
- **Host shouldn't run Guardian** (no Tetragon, no need): disable it with `systemctl disable selfdef-guardian.service`. The in-kernel perimeter doesn't depend on Guardian for the SIGKILL itself — only for the supervisor fan-out.
- **Repeated restarts in short windows**: don't disable `Restart=always`; that defeats the watchdog. Diagnose the root cause.

## Cross-references

- SDD-029 §Deliverable 3 (systemd unit)
- SDD-029 §Deliverable 10 (daemon boot observability)
- Sister runbook: [guardian-socket-unreachable](guardian-socket-unreachable.md)
- Sister runbook: [guardian-console-alert-investigation](guardian-console-alert-investigation.md)
- Trio sibling: [perimeter-tetragon-not-running](perimeter-tetragon-not-running.md)
- Trio sibling: [friction-audit-pcie](friction-audit-pcie.md)
