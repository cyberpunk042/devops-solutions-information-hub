---
title: "Operator runbook — scheduler audit log corruption / chain break"
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
    note: "Source dump tail (audit-trail discipline derived from sain-01 §10 + scheduling architecture)"
  - id: selfdef-sdd-031
    type: internal
    project: selfdef
    path: docs/sdd/031-goldilocks-scheduler.md
    note: "SDD-031 Goldilocks Scheduler spec — Deliverable 2 audit chain"
  - id: selfdef-ms048
    type: internal
    project: selfdef
    path: backlog/milestones/MS048-goldilocks-scheduler-hardware-aware-resource-routing.md
    note: "MS048 R11366-R11392 (audit chain integrity + invariants)"
tags: [runbook, scheduler, audit-log, sha256-chain, zfs, integrity, corruption, incident-response, selfdef, ips]
---

# Operator runbook — scheduler audit log corruption / chain break

## Summary

Operator runbook for **scheduler audit log corruption / chain break**.  Anchored to: Source dump tail (audit-trail discipline derived from sain-01 §10 + scheduling architecture); SDD-031 Goldilocks Scheduler spec — Deliverable 2 audit chain.

## Symptom

- `selfdefctl scheduler audit-cycle replay` reports `CHAIN BROKEN` and points at this runbook.
- `selfdefctl scheduler show` displays `audit chain events: chain check failed (see logs)`.
- `selfdefctl trio` shows scheduler `[OK]` aggregate but the daemon-level boot log warns `scheduler: audit chain check failed`.
- `zpool status` shows checksum errors on `tank/vault/context`.

## Why this matters

The scheduler audit log (`/mnt/vault/context/scheduler_audit.log`) is **append-only with SHA-256 chained `prev_event_sha256` fields** per MS048 R11367. A chain break means one of:

1. **Storage corruption** — bit-flip on disk, fsync ignored, ZFS pool degraded
2. **Tampering** — someone (intruder or operator) edited the audit log in place; the append-only `O_APPEND` invariant was bypassed
3. **Concurrent writer** — another process wrote to the audit log path (should never happen — scheduler is the only authorized writer per R11371)
4. **Log rotation outside MS003** — per R11378, audit log evolves only via MS003-signed log-rotation operator action; manual rotation breaks the chain

In any case, the audit trail's integrity is in question. The Goldilocks Scheduler's replay invariant (R11393) depends on chain integrity. Treat as a **CRITICAL signal**.

## Diagnosis

This is the **same pattern as the Guardian audit log corruption procedure**; the only diffs are file paths and runbook anchors. The mechanism + diagnostic flow are identical because the SHA-256 chain implementation is shared (lifted from the Guardian/perimeter pattern per MS048 R11367).

```bash
# 1. Read the chain check result.
selfdefctl scheduler show --json | jq .audit_chain_events
# null means chain check failed; integer means events seen.

# 2. Inspect the journal for the specific break line.
journalctl -u selfdef-scheduler.service | grep "audit chain break"

# 3. Manually walk the chain.
python3 - <<'PY'
import hashlib, json, sys
prev = None
with open("/mnt/vault/context/scheduler_audit.log") as f:
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

# 5. Cross-check entry count vs ring buffer.
wc -l /mnt/vault/context/scheduler_audit.log
ls /var/cache/selfdef/scheduler/ring/ | wc -l
```

## Diagnosis triage

| Pattern | Classification | Action |
|---|---|---|
| `zpool status` shows checksum errors | Storage corruption | ZFS resilver per [friction-audit-zfs](friction-audit-zfs.md) |
| Chain break at specific line + ZFS clean | Possible tampering | INCIDENT — operator IR playbook |
| Whole file zero or gone | Catastrophic loss | INCIDENT — preserve any backup, escalate |
| Replay engine produces nonsense decision deltas | Suspect chain (re-run audit-cycle replay; if clean, the actual issue is decision-emitter bug not chain) | File issue against `selfdef-scheduler` |

## Recovery procedure

### 1. Preserve the corrupted state

```bash
sudo cp /mnt/vault/context/scheduler_audit.log \
    /mnt/vault/context/scheduler_audit.log.corrupted-$(date +%s)
sudo cp -r /var/cache/selfdef/scheduler/ring \
    /var/cache/selfdef/scheduler/ring.corrupted-$(date +%s)

# If ZFS snapshot is available, capture one for forensics.
sudo zfs snapshot tank/vault/context@scheduler-corruption-$(date +%s)
```

### 2. Identify the break point

From the Python walk above, you know line N. Lines 1..N-1 are verified; N..end are unverified.

### 3. Decide on rebuild strategy

Same two options as guardian-audit-log-corruption:

**Option A — Truncate at last verified line**
- Pros: keeps verified history, no further chain interaction
- Cons: events after the break are administratively lost from the chain

**Option B — Rotate aside, start fresh chain (recommended)**
- Pros: nothing destructive; corrupted file remains for forensics
- Cons: cockpit / API operators see two "eras" of audit trail

Recommend **Option B**:

```bash
sudo systemctl stop selfdef-scheduler.service
sudo mv /mnt/vault/context/scheduler_audit.log \
        /mnt/vault/context/scheduler_audit.log.rotated-$(date +%s)
sudo systemctl start selfdef-scheduler.service
```

### 4. Log the incident

```bash
cat > "raw/notes/$(date +%F)-scheduler-audit-chain-break.md" <<EOF
# Scheduler audit chain break — $(date +%F)

Operator: <handle>
Classification: <storage / tampering / concurrent-writer / unknown>
Break point: line <N> of /mnt/vault/context/scheduler_audit.log
ZFS status:
$(zpool status tank | head -20)

Preserved corrupted file: /mnt/vault/context/scheduler_audit.log.corrupted-<ts>
ZFS snapshot: tank/vault/context@scheduler-corruption-<ts>

Action taken: <Option A | Option B>
Follow-up: <vendor escalation / forensics / nothing if storage>

Replay impact: <list any in-flight counterfactual replay sessions>
EOF
```

### 5. Restore four-watchdog set health

```bash
selfdefctl trio
# Scheduler row should return to OK or UNKNOWN (empty ring after rotation)
selfdefctl scheduler audit-cycle replay
# Should return "chain intact" with a small event count
```

## Operator decision tree

- **Repeated chain breaks on same hardware**: not transient. Failing disk or RAM. Replace + rerun friction-audit memory + ZFS gates.
- **Chain breaks correlated with selfdef-daemon restart**: there may be an fsync race during shutdown; file an issue. Don't disable the audit chain — that defeats the replay invariant (MS048 R11393).
- **Chain break with no other signal**: treat as low-confidence tampering until proven otherwise.

## Relationships

### Cross-references

- SDD-031 §Deliverable 2 (audit_chain_check + emit_audit_entry)
- MS048 R11366-R11392 (audit chain integrity + invariants)
- Sister runbook: [guardian-audit-log-corruption](guardian-audit-log-corruption.md) — same mechanism, different file
- Sister runbook: [friction-audit-zfs](friction-audit-zfs.md) — upstream ZFS health
- Sister runbook: [scheduler-not-running](scheduler-not-running.md)
