---
title: "Operator runbook — Guardian false-positive rollback"
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
    note: "Source dump §10 + Trinity Genesis Auditor dump 977-981 (rollback discipline)"
  - id: selfdef-sdd-029
    type: internal
    project: selfdef
    path: docs/sdd/029-guardian-daemon.md
    note: "SDD-029 guardian-daemon specification — Deliverable 4 (rollback)"
  - id: selfdef-ms044
    type: internal
    project: selfdef
    path: backlog/milestones/MS044-guardian-daemon-tetragon-ebpf-supervisor.md
    note: "Catalog milestone MS044 (rollback engine — module M01140)"
  - id: selfdef-ms003
    type: internal
    project: selfdef
    note: "MS003 selfdef-signing chain-of-trust"
  - id: selfdef-ms009
    type: internal
    project: selfdef
    note: "MS009 audit cycles + replay invariants"
tags: [runbook, guardian, false-positive, rollback, ms003, ms009, ring-0, audit, selfdef, ips]
---

# Operator runbook — Guardian false-positive rollback

## When to use this

A SIGKILL was issued by the in-kernel perimeter and Guardian fanned out the supervisor response (audit-log + console alert) — but on operator review, the targeted process was **legitimate**. Examples:

- A new operator-authored automation script tried to execve `/opt/llm/inference-server` BEFORE an allowlist extension was installed (race condition during deploy).
- An emergency-response binary ran outside its expected cgroup and looked anomalous to the classifier.
- A vendor binary path moved between versions; the previously-allowlisted path no longer matches.

The rollback is **NOT undoing the SIGKILL** — that already happened in kernel space; the process is dead, no resurrection. Rollback is the **audit-anchor for "operator reviewed; this was a false positive"** so future investigators see the verdict context correctly.

## Rollback semantics

Per sain-01 §10 audit invariants (and MS009 replay discipline):

| Property | Behavior |
|---|---|
| Original verdict | Preserved in audit log (append-only — never edited or deleted) |
| Rollback record | Recorded for downstream consumers (cockpit, OCSF sink, audit replay) |
| Future similar events | NOT auto-allowlisted — operator must explicitly extend allowlist via [perimeter-extension-create](perimeter-extension-create.md) |
| MS003 signing | Required: Ring 0 + operator-signed (Stage-2 wire is via the CLI today; full multi-sig is future-round R10540) |

The rollback is administrative. The kernel-level enforcement is unchanged.

## Procedure

### 1. Identify the verdict

```bash
selfdefctl guardian history --limit 32
```

Find the event_id of the false-positive verdict. The event_id is the Tetragon UUID — look for the target_binary_path + ts_ms that matches the incident.

### 2. Verify it really was a false positive

Cross-check the OCSF event for full context:

```bash
grep "<event_id>" /var/log/selfdef/guardian.ocsf.jsonl | python3 -m json.tool
```

Confirm:
- Process cmdline, parent_pid, cgroup — was this a legitimate workflow?
- Binary path — should it have been allowlisted?
- Time correlation — was there a scheduled job / deployment in flight?

If you find any doubt, treat as a real incident, not a false positive. See [perimeter-sigkill-investigation](perimeter-sigkill-investigation.md).

### 3. Record the rollback

```bash
sudo selfdefctl guardian rollback <event_id>
```

Expected output (human mode):

```
guardian rollback: event_id=<id>
  original verdict preserved (append-only audit invariant).
  Ring 0 + MS003 multi-sig gating wires through selfdefd's authority
  dispatcher in a future round; today's surface records the operator
  intent for downstream consumers.
```

JSON mode (`--json`) returns the structured rollback record for downstream pipelines.

### 4. Author the corresponding allowlist extension (if applicable)

If the false positive happened because a legitimate binary wasn't allowlisted, follow up by adding it:

```bash
# See perimeter-extension-create.md for the full MS003-signed flow.
sudo selfdefctl perimeter extend --signed /tmp/<your-extension>.json
sudo systemctl reload tetragon.service
```

### 5. Log the incident

The operator standing direction (verbatim — `wiki/log/`) requires logging significant security decisions:

```bash
cat > "raw/notes/$(date +%F)-guardian-rollback-<event-id-short>.md" <<EOF
# Guardian rollback — <date> — <event_id>

Operator: <handle>
Reason: <why this was a false positive — be specific>
Original event: see /var/log/selfdef/guardian.ocsf.jsonl event_id=<id>
Follow-up: <e.g., "issued perimeter extension <ext-id> for /path/to/binary">

Verbatim cmdline of the killed process:
<cmdline>
EOF
```

## Operator decision tree

- **Rollback rate climbing**: that's a signal the perimeter allowlist is incomplete. Build a sustainable extension manifest set instead of rolling back per-event.
- **Many rollbacks all hit the same binary**: definitely needs an allowlist extension. Issue one immediately per [perimeter-extension-create](perimeter-extension-create.md).
- **Rolled back a verdict and then realized it WAS malicious**: rollback records are themselves auditable. Append a follow-up note correcting the assessment; do NOT delete the rollback record.
- **Need to roll back a verdict from days ago**: the ring buffer is bounded (~16 most recent in the cockpit view; the OCSF log is the canonical archive). `selfdefctl guardian rollback` works as long as the verdict still appears in `guardian history`; for older verdicts, the rollback workflow operates on the OCSF log directly (future-round R10540).

## Cross-references

- SDD-029 §Deliverable 4 (CLI: `selfdefctl guardian rollback`)
- MS009 audit cycles + replay invariants
- MS003 selfdef-signing chain-of-trust
- Sister runbook: [perimeter-extension-create](perimeter-extension-create.md)
- Sister runbook: [perimeter-sigkill-investigation](perimeter-sigkill-investigation.md)
- Sister runbook: [guardian-audit-log-corruption](guardian-audit-log-corruption.md)
