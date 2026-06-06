---
title: "Operator runbook — scheduler weight matrix rotation (MS003 multi-sig)"
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
    note: "Source dump lines 18204-18211 (7-axis objective) + 18000-18100 (per-profile rules)"
  - id: selfdef-sdd-031
    type: internal
    project: selfdef
    path: docs/sdd/031-goldilocks-scheduler.md
    note: "SDD-031 Goldilocks Scheduler spec"
  - id: selfdef-ms048
    type: internal
    project: selfdef
    path: backlog/milestones/MS048-goldilocks-scheduler-hardware-aware-resource-routing.md
    note: "MS048 R11291-R11332 (per-profile weight matrix), R11353 (multi-sig gate)"
  - id: selfdef-ms003
    type: internal
    project: selfdef
    path: backlog/milestones/MS003-correlator-store-responder-signing.md
    note: "MS003 selfdef-signing chain-of-trust"
tags: [runbook, scheduler, weight-matrix, ms003, multi-sig, operator-tuning, profile-evolution, selfdef]
---

# Operator runbook — scheduler weight matrix rotation (MS003 multi-sig)

## When to use this

Per MS048 R11327, the per-profile 7-axis weight matrix is **operator-tunable** — the weights encoded in `selfdef-scheduler::AxisWeights::for_profile()` (R11291-R11326) are the **default baseline** matching the avx-plus-plus dump verbatim; operators may need to evolve them when:

- A new workload pattern emerges (e.g. heavy embeddings → embedding workloads now dominate, so cost-weight in `fast` should rise)
- Hardware changes (a 3090 → 4090 upgrade shifts the cost-vs-latency frontier)
- Cost envelope changes (operator transitions from owned hardware to shared GPU)
- Operator feedback through `audit log → bad/good tags` (R11389-R11390) shows the current weights consistently mis-rank decisions

Per **R11353**: weight matrix change requires **MS003 multi-sig** for production-tier values (signer + auditor). The same gate that protects friction-audit override manifests + perimeter extension manifests + guardian rollback records.

## Procedure

### 1. Read the current weights

```bash
# All six profiles' weight matrices.
selfdefctl scheduler weights --json | jq .

# A single profile.
selfdefctl scheduler weights --profile careful --json | jq .
```

The output structure (per `WeightsEntry`):

```json
[
  {
    "profile": "fast",
    "weights": {
      "latency": 1.0,
      "cost": 0.3,
      "risk": 0.3,
      "energy": 0.2,
      "human_attention": 0.2,
      "hardware_pressure": 0.5
    },
    "sum": 2.5
  }
]
```

### 2. Identify the change

Define the delta you intend to make:

```bash
cat > /tmp/scheduler-weight-rotation-$(date +%F).md <<'EOF'
# Scheduler weight rotation — $(date +%F)

Operator: <handle>
Profile: careful
Change:
  latency:           0.5 → 0.7   (workload became latency-sensitive after Q2 LLM rollout)
  risk:              1.0 → 1.0   (unchanged)
  cost:              0.5 → 0.3   (cloud cost ratio dropped after self-hosting)
  energy:            0.5 → 0.5
  human_attention:   0.9 → 0.9
  hardware_pressure: 0.9 → 0.9

Rationale: <why — be specific, audit-anchor>
Ticket: OPS-1234
EOF
```

### 3. Author the signed config snippet

The scheduler reads `/etc/selfdef/scheduler.toml` (R11352). Weight overrides go in the `[scheduler.weights.<profile>]` section:

```bash
# Stage-1 scaffold — the actual config-loader wiring in the runtime
# crate lands in a future round per SDD-031 D3 implementation note.
# For today's operator surface, the rotation is recorded for downstream
# audit + the eventual config-loader will honor it.

cat > /tmp/scheduler-weights-careful-2026q3.toml <<'EOF'
[scheduler.weights.careful]
latency = 0.7
cost = 0.3
risk = 1.0
energy = 0.5
human_attention = 0.9
hardware_pressure = 0.9
EOF
```

### 4. Generate MS003 signatures (operator + auditor)

```bash
# Operator (signer) signs.
minisign -S -s ~/.config/minisign/operator.key \
         -m /tmp/scheduler-weights-careful-2026q3.toml \
         -x /tmp/scheduler-weights-careful-2026q3.toml.minisig
# Auditor co-signs (separate key, separate person/role).
minisign -S -s ~/.config/minisign/auditor.key \
         -m /tmp/scheduler-weights-careful-2026q3.toml \
         -x /tmp/scheduler-weights-careful-2026q3.toml.auditor.minisig
```

Both KIDs must be present in `/etc/selfdef/trust-roots/*.pub` (the same trust-roots dir used by friction-audit + perimeter + guardian). See [perimeter-key-rotation](perimeter-key-rotation.md) for the trust-roots layout.

### 5. Install (Ring 0 + MS003 verification — Stage-1 surface)

```bash
sudo install -m 0644 -o root -g selfdef \
    /tmp/scheduler-weights-careful-2026q3.toml \
    /etc/selfdef/scheduler.toml
sudo install -m 0644 -o root -g selfdef \
    /tmp/scheduler-weights-careful-2026q3.toml.minisig \
    /etc/selfdef/scheduler.toml.minisig
sudo install -m 0644 -o root -g selfdef \
    /tmp/scheduler-weights-careful-2026q3.toml.auditor.minisig \
    /etc/selfdef/scheduler.toml.auditor.minisig
```

The Stage-1 surface captures the operator intent. The runtime config-loader wires the verification + hot-reload in a future round (per SDD-031 D3 implementation note).

### 6. Restart the scheduler to apply

```bash
sudo systemctl restart selfdef-scheduler.service
selfdefctl scheduler weights --profile careful --json | jq .
```

Verify the new weights are in effect.

### 7. Log the change to ZFS audit

Per R11332: weight matrix mutation MUST be logged to ZFS audit (`/mnt/vault/context/scheduler_audit.log`). The scheduler runtime appends an entry automatically on next startup with the active weight matrix (when the config-loader wires this in a future round).

For Stage-1, manually log it via `wiki/log/`:

```bash
cat > "raw/notes/$(date +%F)-scheduler-weight-rotation-careful.md" <<EOF
# Scheduler weight rotation — careful profile — $(date +%F)
[copy contents from step 2]
Signers:
  operator: <kid>
  auditor: <kid>
Installed: /etc/selfdef/scheduler.toml (sha256: $(sha256sum /etc/selfdef/scheduler.toml | cut -d ' ' -f 1))
EOF
```

## Operator decision tree

- **Need to evolve weights more often than monthly**: that's a signal of workload churn. Consider per-workload profiles instead of mutating the existing 6 (operator-supervised; would expand the Profile enum and be a Stage-2 catalog amendment).
- **Auditor key compromised mid-rotation**: stop. Rotate auditor key first (per [perimeter-key-rotation](perimeter-key-rotation.md)). Re-issue the weight rotation after.
- **Weights drift away from dump verbatim AND nobody can explain why**: revert to baseline via `selfdef-scheduler::AxisWeights::for_profile(p)` defaults. The dump's verbatim values are the operator-recoverable known-good state.
- **Replay shows old vs new compound deltas across the board**: that's the expected counterfactual surface. Per R11393-R11398, `selfdefctl scheduler replay <request-id> --profile careful` shows how every past decision would have routed under the new weights.

## Cross-references

- SDD-031 §Deliverable 2 (AxisWeights::for_profile)
- MS048 R11291-R11332 (per-profile weight matrix)
- MS048 R11353 (MS003 multi-sig gate for production-tier values)
- MS003 selfdef-signing chain-of-trust
- Sister runbook: [perimeter-key-rotation](perimeter-key-rotation.md) (trust-roots discipline)
- Sister runbook: [perimeter-extension-create](perimeter-extension-create.md) (MS003 multi-sig pattern reference)
