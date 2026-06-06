---
title: "Operator runbook — Guardian audit log corruption / chain break"
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
    note: "Source dump §10 lines 531-533 + Trinity Genesis Auditor dump 977-981 (atomic ZFS append)"
  - id: selfdef-sdd-029
    type: internal
    project: selfdef
    path: docs/sdd/029-guardian-daemon.md
    note: "SDD-029 guardian-daemon specification — Deliverable 2 audit chain"
  - id: selfdef-ms044
    type: internal
    project: selfdef
    path: backlog/milestones/MS044-guardian-daemon-tetragon-ebpf-supervisor.md
    note: "Catalog milestone MS044 R10470 (audit chain integrity)"
tags: [runbook, guardian, audit-log, zfs, sha256-chain, integrity, corruption, incident-response, selfdef, ips]
---

# Operator runbook — Guardian audit log corruption / chain break

## Symptom

- `selfdefctl guardian show` displays `OCSF audit chain events: chain check failed (see logs)`.
- `selfdef-guardian.service` journal shows `audit chain break at line <N>: prev_event_sha256=...` errors.
- Cockpit M066 panel aggregates as `ALERT` despite no Failed-step verdicts.
- `zpool status` shows checksum errors on `tank/vault/context`.

## Why this matters

The Guardian OCSF audit chain (`/var/log/selfdef/guardian.ocsf.jsonl`) is **append-only with SHA-256 chained `prev_event_sha256` fields**. A chain break means one of:

1. **Storage corruption** — bit-flip on disk, fsync ignored by underlying hw, ZFS pool degraded.
2. **Tampering** — someone (intruder or operator) edited the audit log in place. The append-only invariant is enforced at the Guardian level by `OpenOptions::append(true)`; an attacker with write access bypassed that.
3. **Concurrent writer** — another process wrote to the audit log path. Should never happen — Guardian is the only authorized writer per MS044 R10471-R10480.

In any case, the audit trail's integrity is in question. Treat as a **CRITICAL signal**.

## Diagnosis

```bash
# 1. Read the chain check result.
selfdefctl guardian show --json | python3 -c "import json,sys; print(json.load(sys.stdin)['audit_chain_events_seen'])"

# 2. Inspect the journal for the specific break line.
journalctl -u selfdef-guardian.service | grep "audit chain break"

# 3. Manually walk the chain to confirm where it broke.
python3 - <<'PY'
import hashlib, json, sys
prev = None
with open("/var/log/selfdef/guardian.ocsf.jsonl") as f:
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

# 5. Compare event count to ring buffer (cross-check).
ls /var/cache/selfdef/guardian/ring/ | wc -l
wc -l /var/log/selfdef/guardian.ocsf.jsonl
```

## Diagnosis triage

| Pattern | Classification | Action |
|---|---|---|
| `zpool status` shows checksum errors | Storage corruption | ZFS resilver per [friction-audit-zfs](friction-audit-zfs.md) |
| Chain break is at a SPECIFIC line + ZFS clean | Possible tampering | Treat as INCIDENT — operator IR playbook |
| Whole file is gone or zero bytes | Catastrophic loss | INCIDENT — preserve any backup, escalate |
| Many events missing but chain intact at file head | Log rotation issue (not yet shipped — Guardian does not currently rotate) | Audit the rotator if operator added one |

## Recovery procedure

### 1. Preserve the corrupted state

Before any repair, snapshot the current state for forensics:

```bash
sudo cp /var/log/selfdef/guardian.ocsf.jsonl \
    /var/log/selfdef/guardian.ocsf.jsonl.corrupted-$(date +%s)
sudo cp -r /var/cache/selfdef/guardian/ring \
    /var/cache/selfdef/guardian/ring.corrupted-$(date +%s)
```

If a ZFS snapshot is available, capture one:

```bash
sudo zfs snapshot tank/vault/context@guardian-corruption-$(date +%s)
```

### 2. Identify the break point

From the Python walk above, you know the line N at which the chain broke. Everything **before** line N is verified; everything **after** is unverified.

### 3. Decide on rebuild strategy

The append-only invariant means you can't safely "patch" the corrupted file — that would itself violate the chain. Two options:

**Option A: Truncate at last verified line, start fresh chain**
- Pros: keeps verified history, no further chain interaction
- Cons: ALL events after the break are administratively lost from the chain (still in the ring buffer + OCSF sink downstream if those exist)

**Option B: Rotate the corrupted file aside, start a new chain**
- Pros: nothing destructive; corrupted file remains for forensics
- Cons: cockpit / API operators see two "eras" of audit trail — one closed (corrupted), one open (new)

Recommend **Option B** for any incident classification (tampering, ZFS-degraded).

```bash
# Option B
sudo systemctl stop selfdef-guardian.service
sudo mv /var/log/selfdef/guardian.ocsf.jsonl \
        /var/log/selfdef/guardian.ocsf.jsonl.rotated-$(date +%s)
sudo systemctl start selfdef-guardian.service
```

### 4. Log the incident

The audit chain break IS itself a security event. Log it:

```bash
cat > "raw/notes/$(date +%F)-guardian-audit-chain-break.md" <<EOF
# Guardian audit chain break — $(date +%F)

Operator: <handle>
Classification: <storage / tampering / concurrent-writer / unknown>
Break point: line <N> of /var/log/selfdef/guardian.ocsf.jsonl
ZFS status:
$(zpool status tank | head -20)

Preserved corrupted file: /var/log/selfdef/guardian.ocsf.jsonl.corrupted-<ts>
ZFS snapshot: tank/vault/context@guardian-corruption-<ts>

Action taken: <Option A truncate | Option B rotate | other>
Follow-up: <vendor escalation / forensics / nothing if storage>
EOF
```

### 5. Restore three-watchdog trio health

```bash
selfdefctl guardian show
# audit chain events: <new count> (chain intact)
```

The cockpit M066 panel should clear to GREEN (or OK aggregate) once new clean events accumulate.

## Operator decision tree

- **Repeated chain breaks on same hardware**: that's not transient. Failing disk or RAM. Replace + rerun friction-audit memory + ZFS gates.
- **Chain breaks correlated with `selfdef-daemon` restarts**: there may be a fsync race during shutdown; file an issue. Don't disable the audit chain — that defeats the audit-chain invariant.
- **Chain break with no other signal**: treat as low-confidence tampering until proven otherwise.

## Relationships

### Cross-references

- SDD-029 §Deliverable 2 (audit chain check + atomic append discipline)
- MS044 R10441-R10480 (OCSF emission + ZFS log bridge)
- Sister runbook: [friction-audit-zfs](friction-audit-zfs.md) (upstream ZFS health)
- Sister runbook: [guardian-not-running](guardian-not-running.md)
- Sister runbook: [perimeter-sigkill-investigation](perimeter-sigkill-investigation.md)
