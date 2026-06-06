---
title: "Operator runbook — friction-audit ZFS gate failure"
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
    note: "Source dump §5.1 — friction-audit ZFS gate lines 354-359 (zpool status -x equality check)"
  - id: selfdef-sdd-027
    type: internal
    project: selfdef
    path: docs/sdd/027-friction-audit-system.md
    note: "SDD-027 Deliverable 1 step 2 ZFS gate"
  - id: selfdef-ms046
    type: internal
    project: selfdef
    path: backlog/milestones/MS046-friction-audit-system-boot-time-hardware-integrity-gate.md
    note: "MS046 R10820-R10826 (ZFS gate behavior) + R10881-R10890 (ZFS log bridge)"
tags: [runbook, friction-audit, zfs, hardware-integrity, sain-01, selfdef, ips, boundary-enforcement, zpool, tank-vault]
---

# Operator runbook — friction-audit ZFS gate failure

## Symptom

`sovereign-guard.service` fails at boot with exit code **2**. `journalctl -u sovereign-guard.service` shows verbatim:

```
CRITICAL ARCHITECTURAL FRICTION ERROR: Storage Pool Anomalies Discovered.
```

`podman.service` / `docker.service` / `containerd.service` cannot start until the pool returns to `all pools are healthy` OR an operator-signed override is recorded (MS003 multi-sig, MS046 R10869-R10880).

## Diagnosis

The gate runs `zpool status -x` and requires the output to equal the literal string `"all pools are healthy"`. ANY other output fails. The most common causes:

| Cause | Investigation |
|---|---|
| Pool DEGRADED — drive offline or read-error threshold exceeded | `sudo zpool status -v` — look for `state: DEGRADED` and per-vdev state |
| Pool SUSPENDED — total I/O loss (pull-cable / multipath flap) | `sudo zpool status` shows `state: SUSPENDED`; `dmesg \| grep -i zfs` |
| Resilver in progress (post-replacement, post-power-cycle scrub-resume) | `sudo zpool status` shows `scan: resilver in progress` — `zpool status -x` does NOT return healthy until done |
| Scrub found checksum errors | `sudo zpool status -v` lists individual files; `zpool errors` is non-zero |
| Operator-extension SKIP triggered (zpool not installed) | `command -v zpool` returns non-zero — gate emits SKIP via OCSF Audit 1003 (NOT a fail) |
| `tank/vault/context` dataset specifically degraded | `sudo zfs list -o name,health,mountpoint tank/vault/context` |

## Recovery procedure

### 1. Identify which pool / vdev is unhealthy

```bash
sudo zpool status -x          # summary: which pool
sudo zpool status -v          # verbose: which vdev + error counts
sudo zpool history -i tank    # internal events leading up to it
```

### 2. Most-likely-route fix per state

#### State: DEGRADED (drive offline)

```bash
sudo zpool status                                # find the OFFLINE/FAULTED dev
sudo zpool online tank <vdev-id>                 # if it's a transient I/O blip
# or, for replacement:
sudo zpool replace tank <old-id> <new-device>
# wait for resilver to complete:
watch -n 5 'sudo zpool status'
```

#### State: SUSPENDED (total I/O loss)

```bash
# Check the underlying device first:
ls -la /dev/disk/by-id/ | grep <expected-id>
sudo dmesg | tail -50
# Once paths are restored:
sudo zpool clear tank
```

#### Resilver in progress

Wait. The gate will pass automatically once `zpool status -x` returns to `"all pools are healthy"`. Optionally accelerate via:

```bash
echo 4 | sudo tee /sys/module/zfs/parameters/zfs_resilver_min_time_ms
echo 0 | sudo tee /sys/module/zfs/parameters/zfs_scan_idle
```

(Revert to defaults `3000` and `50` once done.)

#### Checksum errors

```bash
sudo zpool status -v          # which files corrupted
sudo zpool clear tank         # clear counters after investigation
sudo zpool scrub tank         # full re-scrub
# wait, then re-check:
sudo zpool status -x
```

### 3. Re-test the gate

```bash
sudo systemctl start sovereign-guard.service
journalctl -u sovereign-guard.service --since "1 minute ago"
```

Or via the CLI mirror:

```bash
sudo selfdefctl friction-audit replay
sudo selfdefctl friction-audit show --json
```

### 4. Confirm tank/vault/context is writable

Since selfdef's OCSF event log bridge (`tank/vault/context/friction.log`, MS046 R10881-R10889) and sovereign-os state fabric (per sain-01 §7) both depend on this dataset:

```bash
sudo zfs get health,sync,primarycache,logbias tank/vault/context
# expect:
#   health    healthy
#   sync      always         (MS046 R10882 invariant)
#   logbias   latency
```

If `sync != always`, re-set per the SAIN-01 spec:

```bash
sudo zfs set sync=always tank/context
sudo zfs set logbias=latency tank/context
sudo zfs set primarycache=all tank/context
```

## Operator-extension SKIP (non-ZFS hosts)

The gate is operator-extended (MS046 R10932, R11107) to **SKIP cleanly** when `zpool` is not installed. This is NOT a failure — it lets selfdef ship on hosts that don't run ZFS (containers, non-SAIN-01 deployments). The OCSF event class_uid=1003 (Audit, severity 1) is emitted with `"note":"zpool not installed; skipped"`. The CLI mirror shows `Zfs SKIP (operator-extended SKIP …)`.

To verify the SKIP is happening:

```bash
sudo selfdefctl friction-audit show --json | jq '.[] | select(.gate=="zfs")'
# expect "status":{"status":"skipped","detail":"operator-extended SKIP (tool absent)"}
```

## Operator-signed override (deferred fix)

Same procedure as the PCIe runbook (`friction-audit-pcie.md`):

```bash
sudo selfdefctl friction-audit override-create \
    --gate zfs \
    --reason "Pool tank-2 resilver running 18h; ticket #5678" \
    --expires-in 24h \
    --signer-kid <your-MS003-kid> \
    --auditor-kid <auditor-MS003-kid>
```

ZFS overrides are dangerous — they tell the gate to allow boot even though the storage substrate is unhealthy. Use sparingly. Default TTL recommendation: 24h, not 7d (the script's max). Always pair with an open incident ticket.

## Relationships

### Cross-references

- Source: `~/infohub/raw/dumps/2026-05-15-sain-01-master-spec-other-conversation-transposition.md` §5.1 lines 354–359 + §7 ZFS transactional optimizations
- Milestone: `selfdef/backlog/milestones/MS046-friction-audit-system-boot-time-hardware-integrity-gate.md` R10820-R10826 + R10881-R10890
- Sister gates: `friction-audit-pcie.md`, `friction-audit-memory.md`, `friction-audit-immutability.md`, `friction-audit-signature.md`
- Sovereign-OS dependency: M068 ZFS storage architecture (tank/vault dataset configuration)
- Atomic state binding: sovereign-os M071 Atomic State Transition Protocol (POSIX append-only fd over sync=always)
