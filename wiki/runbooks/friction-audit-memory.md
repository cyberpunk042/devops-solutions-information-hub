---
title: "Operator runbook — friction-audit memory gate failure"
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
    note: "Source dump §5.1 lines 360-364 — friction-audit memory geometry check via dmidecode"
  - id: selfdef-sdd-027
    type: internal
    project: selfdef
    path: docs/sdd/027-friction-audit-system.md
    note: "SDD-027 Deliverable 1 step 3 memory gate + operator-extended exit code 3 (sain-01 §5.1 left open)"
  - id: selfdef-ms046
    type: internal
    project: selfdef
    path: backlog/milestones/MS046-friction-audit-system-boot-time-hardware-integrity-gate.md
    note: "MS046 R10827-R10833 (memory gate), R10831 + F05491 (exit code 3 operator-extension)"
tags: [runbook, friction-audit, memory, dimm, dmidecode, sain-01, selfdef, ips, boundary-enforcement, znver5, ecc-rdimm]
---

# Operator runbook — friction-audit memory gate failure

## Symptom

`sovereign-guard.service` fails at boot with exit code **3**. `journalctl -u sovereign-guard.service` shows:

```
ARCHITECTURAL FRICTION WARNING: Memory geometry mismatch.
Diagnostic: detected N populated DIMM slot(s); expected ≥ M.
Remediation Check: Verify DIMM seating and slot population per board manual.
```

Where N is the actually-detected `dmidecode -t memory | grep -c "Size: [0-9]"` count and M is the operator-tunable `SELFDEF_FRICTION_AUDIT_MIN_STICKS` (default 1, recommended 4 for ProArt znver5).

## Operator-extension notes

The memory gate IS operator-extended (MS046 R10831, F05491). The sain-01 §5.1 source dump captures the dmidecode count but **does not specify** what threshold counts as "expected". The friction-audit script defaults to a minimum-of-1 threshold (safe for VMs / containers / single-DIMM hosts) and surfaces a tunable env var so hosts that expect a specific count can enforce it.

For the ProArt X870E-Creator SAIN-01 reference:
- 4 DIMM slots on the board
- Operator-recommended populated count = 4 (full quad-channel ECC RDIMM configuration)
- Set `SELFDEF_FRICTION_AUDIT_MIN_STICKS=4` in `/etc/default/friction-audit` (a drop-in env file the systemd unit can source via `EnvironmentFile=`).

## Diagnosis

| Cause | Investigation |
|---|---|
| DIMM physically dislodged from slot | Power down, open chassis, re-seat all 4 DIMMs |
| DIMM died / training failure | `sudo dmidecode -t memory \| grep -E "(Locator\|Size\|Manufacturer\|Part Number\|Serial)"` |
| BIOS skipping a slot due to error correction event | Reboot, enter BIOS, check Memory → Error Correction status |
| EDAC kernel module not loaded → silent ECC errors | `sudo modprobe edac_mce_amd && dmesg \| grep -i edac` |
| `dmidecode` not installed (containers, minimal images) | Gate SKIPs (operator-extension, NOT a failure) |
| Wrong threshold for this host | Re-set `SELFDEF_FRICTION_AUDIT_MIN_STICKS` to the actual expected count |

## Recovery procedure

### 1. Read what dmidecode actually sees

```bash
sudo dmidecode -t memory | grep -A1 "^Memory Device" | grep -E "Size|Locator"
# Each populated slot prints:
#   Size: 32 GB
#   Locator: DIMM 0
# Empty slots print:
#   Size: No Module Installed
#   Locator: DIMM 1
```

Count the `Size: [0-9]` lines — that's what the gate counts.

### 2. Most-likely fix: re-seat or replace

Power down, ground yourself, open chassis, remove + re-insert each DIMM with a firm click. For a SAIN-01 reference board with quad-channel RDIMM, install in the operator-documented order (typically A2 + B2 + C2 + D2 for first 4 sticks per AMD znver5 board manual).

### 3. Check ECC + thermal stability

```bash
sudo modprobe edac_mce_amd
sudo dmesg | grep -iE "edac|memory|correctable|uncorrectable" | tail -20
sudo lscpu | grep -i flags | grep -o ' epyc[^ ]*\| zenver5\| sse4_2'  # confirm AMD ECC-capable
```

If `dmesg` shows correctable errors >> 0 events, the DIMM is degrading even if it still trains. Replace.

### 4. Threshold tuning (operator-supervised)

If the host genuinely has fewer DIMMs than `4` (e.g., partial-population for a dev box), set the threshold to match:

```bash
# /etc/default/friction-audit
SELFDEF_FRICTION_AUDIT_MIN_STICKS=2
```

Then add to `sovereign-guard.service` drop-in:

```bash
sudo mkdir -p /etc/systemd/system/sovereign-guard.service.d
cat | sudo tee /etc/systemd/system/sovereign-guard.service.d/threshold.conf << 'EOF'
[Service]
EnvironmentFile=/etc/default/friction-audit
EOF
sudo systemctl daemon-reload
sudo systemctl restart sovereign-guard.service
```

### 5. Re-test the gate

```bash
sudo selfdefctl friction-audit replay
sudo selfdefctl friction-audit show --json | jq '.[] | select(.gate=="memory")'
# expect "status":{"status":"pass"}
```

## Severity

Memory failures are MEDIUM severity (MS046 F05491, OCSF severity_id=3) — NOT high like PCIe/ZFS. The rationale: a memory-count mismatch is operator-detectable post-boot and rarely a sign of an active attack. The gate-fail prevents container startup (per the systemd ordering invariant) but the operator usually fixes via re-seat + reboot within minutes.

## Operator-signed override

The memory gate is the most-commonly-overridden of the three (a known-degraded DIMM awaiting replacement is a routine state). TTL recommendation: 72h (long enough to procure + install replacement).

```bash
sudo selfdefctl friction-audit override-create \
    --gate memory \
    --reason "DIMM B2 confirmed bad; RMA in flight; ticket #9012" \
    --expires-in 72h \
    --signer-kid <your-MS003-kid> \
    --auditor-kid <auditor-MS003-kid>
```

## Relationships

### Cross-references

- Source: `~/infohub/raw/dumps/2026-05-15-sain-01-master-spec-other-conversation-transposition.md` §5.1 lines 360–364
- Milestone: `selfdef/backlog/milestones/MS046-friction-audit-system-boot-time-hardware-integrity-gate.md` R10827-R10833 + F05491
- Sister gates: `friction-audit-pcie.md`, `friction-audit-zfs.md`, `friction-audit-immutability.md`, `friction-audit-signature.md`
- znver5 ECC reference: SDD-018 hardware-aware modules + sain-01 §1.1 core components
