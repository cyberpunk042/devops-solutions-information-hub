---
title: "Operator runbook — Guardian Tetragon socket unreachable"
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
    note: "Source dump §10 lines 524 + 540-552 (UNIX socket ingestion contract)"
  - id: selfdef-sdd-029
    type: internal
    project: selfdef
    path: docs/sdd/029-guardian-daemon.md
    note: "SDD-029 guardian-daemon specification — Deliverable 2 (event ingester)"
  - id: selfdef-ms044
    type: internal
    project: selfdef
    path: backlog/milestones/MS044-guardian-daemon-tetragon-ebpf-supervisor.md
    note: "Catalog milestone MS044 R10326-R10380 (UNIX socket event ingester)"
tags: [runbook, guardian, tetragon, unix-socket, ingestion, sain-01, selfdef, ips]
---

# Operator runbook — Guardian Tetragon socket unreachable

## Symptom

- `selfdefctl guardian show` displays `tetragon socket: ... (MISSING)`.
- `selfdef-guardian.service` is running BUT no verdicts populate the ring buffer.
- `journalctl -u selfdef-guardian.service` shows `connect: No such file or directory` or similar on `/var/run/tetragon/tetragon.events`.
- Cockpit M066 panel aggregates as `DEGRADED`.

## Why this matters

Guardian's input contract IS the Tetragon UNIX socket (`/var/run/tetragon/tetragon.events` per sain-01 §10 dump 524). Without it, Guardian has nothing to classify and no 3-step response to execute. The in-kernel perimeter (MS047) still SIGKILLs because that's a kprobe, not Guardian — but the supervisor-tier observability layer is blind.

## Diagnosis

```bash
ls -la /var/run/tetragon/tetragon.events
systemctl status tetragon.service
journalctl -u tetragon.service -n 100 --no-pager | grep -i socket
```

1-step-up-the-stack causes:

| Cause | Investigation |
|---|---|
| Tetragon not running | `systemctl is-active tetragon.service` — see [perimeter-tetragon-not-running](perimeter-tetragon-not-running.md) |
| Tetragon socket at non-default path | Tetragon config — `cat /etc/tetragon/tetragon.yaml` (or wherever the deployment puts it); selfdef expects `/var/run/tetragon/tetragon.events` per sain-01 §10 verbatim |
| Socket permissions | `ls -la /var/run/tetragon/`; Guardian runs as root so should have access, but in containerized deployments the socket may be group-restricted to `tetragon` group |
| `/var/run` cleared at boot | systemd-tmpfiles + Tetragon's `RuntimeDirectory=tetragon` should re-create on Tetragon start |
| Container/namespace isolation | If Guardian is in a different namespace from Tetragon, the socket isn't visible. Run both in the same network/mount namespace (host services, not containerized). |

## Recovery procedure

### 1. Confirm Tetragon is the upstream issue

```bash
selfdefctl guardian show
# tetragon socket MISSING

systemctl is-active tetragon.service
# inactive ← root cause
```

If Tetragon is inactive, route to [perimeter-tetragon-not-running](perimeter-tetragon-not-running.md). Guardian comes back automatically once Tetragon is up + the socket appears.

### 2. If Tetragon is running but the socket isn't where Guardian looks

The default selfdef expectation is `/var/run/tetragon/tetragon.events` (sain-01 §10 verbatim). To override (Stage-2 escape hatch, not standard):

```bash
sudo systemctl edit selfdef-guardian.service
# Add:
# [Service]
# Environment="SELFDEF_GUARDIAN_SOCKET_PATH=/path/to/your/tetragon.events"
sudo systemctl daemon-reload
sudo systemctl restart selfdef-guardian.service
```

(Note: the env-var override is honored by CLI/HTTP read paths. The runtime daemon's actual ingester uses `DEFAULT_SOCKET_PATH` directly today; full override-via-env wiring is a future-round R10380 capability.)

### 3. Permission troubleshooting

If `selfdef` group can't read the socket:

```bash
# Inspect.
ls -la /var/run/tetragon/

# If Tetragon group-restricts and you want selfdef in that group:
sudo usermod -aG tetragon selfdef
sudo systemctl restart selfdef-guardian.service
```

Note: Guardian is supposed to run as root per its systemd unit hardening (Ring 0 IPS service). If you've operator-edited the unit to drop User=root, group membership matters; on default deploys, root reads the socket fine.

### 4. Verify recovery

```bash
selfdefctl guardian show
# tetragon socket PRESENT
```

The ring buffer will start populating as soon as Tetragon emits its first event Guardian classifies.

## Operator decision tree

- **Long-term Tetragon-less deployment**: disable Guardian (`systemctl disable --now selfdef-guardian.service`). The supervisor layer is moot without an event source. Document in incident log.
- **Socket appears intermittently**: probably Tetragon crash-looping; check Tetragon's own logs.
- **Need to test Guardian without real Tetragon**: there's no first-party mock for the socket today. The runtime crate's Effector trait is mockable for unit tests, but no end-to-end harness ships yet (MS044 R10540 future-round).

## Relationships

### Cross-references

- SDD-029 §Deliverable 2 (runtime crate — event ingester contract)
- MS044 R10326-R10380 (UNIX socket event ingester)
- Upstream sibling: [perimeter-tetragon-not-running](perimeter-tetragon-not-running.md)
- Sister runbook: [guardian-not-running](guardian-not-running.md)
