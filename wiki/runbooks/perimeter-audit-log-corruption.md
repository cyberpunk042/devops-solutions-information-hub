---
title: "Operator runbook — Perimeter audit log corruption / chain break"
type: reference
domain: ai-agents
layer: 2
status: draft
confidence: high
maturity: seed
created: 2026-05-21
updated: 2026-05-21
sources:
  - id: sain-01-dump-2026-05-15
    type: directive
    project: devops-solutions-information-hub
    path: raw/dumps/2026-05-15-sain-01-master-spec-other-conversation-transposition.md
    note: "Source dump §10 lines 531-533 + Trinity Genesis Auditor dump 977-981 (atomic ZFS append)"
  - id: selfdef-sdd-028
    type: internal
    project: selfdef
    path: docs/sdd/028-perimeter-engine.md
    note: "SDD-028 perimeter-engine specification — Deliverable 2 audit chain"
  - id: selfdef-ms047
    type: internal
    project: selfdef
    path: backlog/milestones/MS047-real-time-security-perimeter-engine-tetragon-kernel-fence.md
    note: "Catalog milestone MS047 (perimeter audit chain integrity)"
tags: [runbook, perimeter, audit-log, zfs, sha256-chain, integrity, corruption, incident-response, selfdef, ips, tetragon]
---

# Operator runbook — Perimeter audit log corruption / chain break

## Summary

Operator runbook for **Perimeter audit log corruption / chain break**.  Anchored to: Source dump §10 lines 531-533 + Trinity Genesis Auditor dump 977-981 (atomic ZFS append); SDD-028 perimeter-engine specification — Deliverable 2 audit chain.

## Symptom

- `SelfdefPerimeterChainBroken` Prometheus alert is firing (severity: critical).
- `selfdef_perimeter_audit_chain_events == -1` (the sentinel value the perimeter exports when the most-recent chain check failed).
- `selfdefctl perimeter audit-cycle replay` returns non-zero with a `chain break at line <N>: prev_event_sha256=...` diagnostic.
- `selfdefctl perimeter show --json | jq .audit_chain_state` returns `"broken"`.
- `zpool status` may show checksum errors on the dataset hosting `/var/log/selfdef/perimeter.ocsf.jsonl`.

## Why this matters

The MS047 Perimeter OCSF audit chain (`/var/log/selfdef/perimeter.ocsf.jsonl`) is **append-only with SHA-256 chained `prev_event_sha256` fields**. The chain backs the perimeter's Sigkill verdict trail — every kernel-side denial Tetragon emits gets persisted via the chained writer. A chain break means one of:

1. **Storage corruption** — bit-flip on disk, fsync ignored by underlying hw, ZFS pool degraded.
2. **Tampering** — someone (intruder or operator) edited the audit log in place. The append-only invariant is enforced by `OpenOptions::append(true)` on the writer; an attacker with write access bypassed that.
3. **Concurrent writer** — another process wrote to the audit log path. Should never happen — the perimeter writer is the only authorized writer per MS047.
4. **Extension misbehavior** — an operator-signed MS047 perimeter extension misused the chain handle (e.g., manual seek+write). Modern extension API forbids this, but legacy extensions may be broken.

In any case, the audit trail's integrity is in question. The perimeter is the **kernel-syscall fence** for the four-watchdog set — when its audit chain breaks, the operator has lost the ability to prove which kills happened and when. Treat as a **CRITICAL signal**.

## Diagnosis

```bash
# 1. Read the chain check result.
selfdefctl perimeter audit-cycle replay 2>&1 | tee /tmp/perimeter-chain-check.out

# 2. Inspect the journal for the specific break line.
journalctl _SYSTEMD_UNIT=tetragon.service _SYSTEMD_UNIT=selfdefd.service \
  --since "24 hours ago" | grep -E "audit chain break|prev_event_sha256"

# 3. Manually walk the chain to confirm where it broke.
python3 - <<'PY'
import hashlib, json, sys
prev = None
with open("/var/log/selfdef/perimeter.ocsf.jsonl") as f:
    for i, line in enumerate(f, 1):
        line = line.rstrip("\n")
        if not line.strip():
            continue
        try:
            event = json.loads(line)
        except json.JSONDecodeError as e:
            print(f"line {i}: MALFORMED JSON — {e}")
            sys.exit(1)
        claimed_prev = event.get("prev_event_sha256")
        if prev and claimed_prev != prev:
            print(f"line {i}: CHAIN BREAK — claimed prev={claimed_prev}, actual prev={prev}")
            sys.exit(2)
        prev = hashlib.sha256(line.encode()).hexdigest()
print("chain intact")
PY

# 4. ZFS health.
zpool status tank
zpool status -x

# 5. Cross-check with the Prometheus alert state.
curl -s http://127.0.0.1:9090/api/v1/alerts | \
  jq '.data.alerts[] | select(.labels.alertname == "SelfdefPerimeterChainBroken")'

# 6. List active perimeter extensions (signed manifests).
selfdefctl perimeter status --json | jq .extensions
```

## Diagnosis triage

| Pattern | Classification | Action |
|---|---|---|
| `zpool status` shows checksum errors | Storage corruption | ZFS resilver per [friction-audit-zfs](friction-audit-zfs.md) |
| Chain break is at a SPECIFIC line + ZFS clean | Possible tampering | Treat as INCIDENT — operator IR playbook |
| Whole file is gone or zero bytes | Catastrophic loss | INCIDENT — preserve any backup, escalate |
| Many events missing but chain intact at file head | Log rotation issue (not yet shipped — the perimeter writer does not currently rotate) | Audit the rotator if operator added one |
| Break follows an operator-signed extension activation | Extension misbehavior | Disable extension via [perimeter-extension-create](perimeter-extension-create.md) recovery, then escalate to extension author |

## Recovery procedure

### 1. Preserve the corrupted state

Before any repair, snapshot the current state for forensics:

```bash
sudo cp /var/log/selfdef/perimeter.ocsf.jsonl \
    /var/log/selfdef/perimeter.ocsf.jsonl.corrupted-$(date +%s)
sudo cp -r /var/cache/selfdef/perimeter/ring \
    /var/cache/selfdef/perimeter/ring.corrupted-$(date +%s)
```

If a ZFS snapshot is available, capture one:

```bash
sudo zfs snapshot tank/vault/context@perimeter-corruption-$(date +%s)
```

### 2. Identify the break point

From the Python walk above, you know the line N at which the chain broke. Everything **before** line N is verified; everything **after** is unverified.

### 3. Decide on rebuild strategy

The append-only invariant means you can't safely "patch" the corrupted file — that would itself violate the chain. Two options:

**Option A: Truncate at last verified line, start fresh chain**
- Pros: keeps verified history, no further chain interaction
- Cons: ALL Sigkill verdicts after the break are administratively lost from the chain (still in the ring buffer + OCSF sink downstream if those exist)

**Option B: Rotate the corrupted file aside, start a new chain**
- Pros: nothing destructive; corrupted file remains for forensics
- Cons: cockpit / API operators see two "eras" of audit trail — one closed (corrupted), one open (new)

Recommend **Option B** for any incident classification (tampering, ZFS-degraded). The perimeter is too security-critical to lose forensic evidence.

```bash
# Option B
sudo systemctl stop selfdefd.service
sudo mv /var/log/selfdef/perimeter.ocsf.jsonl \
        /var/log/selfdef/perimeter.ocsf.jsonl.rotated-$(date +%s)
sudo systemctl start selfdefd.service

# Verify Tetragon is still running — the perimeter fence depends on it.
systemctl is-active tetragon.service
```

### 4. Log the incident

The audit chain break IS itself a security event. Log it:

```bash
cat > "raw/notes/$(date +%F)-perimeter-audit-chain-break.md" <<EOF
# Perimeter audit chain break — $(date +%F)

Operator: <handle>
Classification: <storage / tampering / concurrent-writer / extension-misbehavior / unknown>
Break point: line <N> of /var/log/selfdef/perimeter.ocsf.jsonl
ZFS status:
$(zpool status tank | head -20)

Active extensions at break:
$(selfdefctl perimeter status --json | jq .extensions)

Preserved corrupted file: /var/log/selfdef/perimeter.ocsf.jsonl.corrupted-<ts>
ZFS snapshot: tank/vault/context@perimeter-corruption-<ts>

Action taken: <Option A truncate | Option B rotate | other>
Follow-up: <vendor escalation / forensics / extension author / nothing if storage>
EOF
```

### 5. Restore four-watchdog set health

```bash
selfdefctl perimeter audit-cycle replay
# expected: "chain intact (0 verdicts; new chain)"

selfdefctl trio
# the perimeter row should aggregate as OK once the alert clears
```

The `SelfdefPerimeterChainBroken` Prometheus alert should clear within `for: 1m` of the new chain reading as intact.

## Operator decision tree

- **Repeated chain breaks on same hardware**: that's not transient. Failing disk or RAM. Replace + rerun friction-audit memory + ZFS gates.
- **Chain breaks correlated with `selfdefd` restarts**: there may be a fsync race during shutdown; file an issue. Don't disable the audit chain — that defeats the audit-chain invariant.
- **Chain break correlated with a specific extension activation**: disable that extension via `selfdefctl perimeter revoke <ext-id>` and escalate to the extension author per the [perimeter-extension-create](perimeter-extension-create.md) revocation procedure.
- **Chain break with no other signal**: treat as low-confidence tampering until proven otherwise. Cross-reference the journal around the break time for unexpected processes touching `/var/log/selfdef/`.

## Relationships

### Cross-references

- SDD-028 §Deliverable 2 (audit chain check + atomic append discipline)
- MS047 catalog rows on perimeter audit chain integrity
- Sister runbook: [friction-audit-zfs](friction-audit-zfs.md) (upstream ZFS health)
- Sister runbook: [perimeter-sigkill-investigation](perimeter-sigkill-investigation.md) (the audit chain backs the Sigkill verdict trail)
- Sister runbook: [perimeter-policy-load-failure](perimeter-policy-load-failure.md) (companion: TracingPolicy load failures)
- Sister runbook: [guardian-audit-log-corruption](guardian-audit-log-corruption.md) (the parallel runbook for guardian; same chain pattern)
- Sister runbook: [scheduler-audit-log-corruption](scheduler-audit-log-corruption.md) (the parallel runbook for scheduler)
