---
title: "Operator runbook — friction-audit PCIe gate failure"
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
    note: "Source dump §5.1 — Native Guard Script Architecture friction-audit lines 338-353 PCIe gate"
  - id: selfdef-sdd-027
    type: internal
    project: selfdef
    path: docs/sdd/027-friction-audit-system.md
    note: "SDD-027 friction-audit-system specification"
  - id: selfdef-ms046
    type: internal
    project: selfdef
    path: backlog/milestones/MS046-friction-audit-system-boot-time-hardware-integrity-gate.md
    note: "Catalog milestone MS046 (240 requirements + 26 modules + 10 epics)"
tags: [runbook, friction-audit, pcie, hardware-integrity, sain-01, selfdef, ips, boundary-enforcement, znver5, m2-slot, bifurcation]
---

# Operator runbook — friction-audit PCIe gate failure

## Summary

Operator runbook for **friction-audit PCIe gate failure**.  Anchored to: Source dump §5.1 — Native Guard Script Architecture friction-audit lines 338-353 PCIe gate; SDD-027 friction-audit-system specification. Also references: Catalog milestone MS046 (240 requirements + 26 modules + 10 epics).

## Symptom

`sovereign-guard.service` fails at boot with exit code **1**. `journalctl -u sovereign-guard.service` shows three lines verbatim:

```
CRITICAL ARCHITECTURAL FRICTION ERROR: PCIe Bus Degradation Detected.
Diagnostic: One or more slots running below symmetric x8 configuration parameters.
Remediation Check: Verify if M.2_2 slot is populated, interfering with lane paths.
```

`podman.service` / `docker.service` / `containerd.service` cannot start until `sovereign-guard.service` either passes or operator-signs an override. This is by design (MS046 R10866 ordering invariant).

## Diagnosis

The gate runs `lspci -vvv | grep -c "LnkSta:.*Width x8"` and requires the result to be ≥ 2. The ProArt X870E-Creator reference hardware (sain-01) provides two physical PCIe 5.0 x16 slots that operate at x8/x8 when bifurcation symmetry is honored. The 1-step-up-the-stack cause is almost always one of:

| Cause | Investigation |
|---|---|
| M.2_2 slot populated and stealing lanes | `lspci -vv \| grep -B1 "Width x"` — look for an M.2 device sharing PCIe with the slot |
| BIOS PCIe bifurcation set to x16/0 (single-slot mode) | BIOS → Advanced → PCI Subsystem → PCIe Bifurcation, must be x8/x8 |
| Card seated incorrectly | Physical re-seat both PCIe cards (the GPUs in sain-01 reference) |
| Cable damage or riser fault | If on a mining/extender riser, replace the riser cable |
| BIOS firmware downgrade | `dmidecode -s bios-version` vs vendor-released latest; older BIOS sometimes mis-trains lanes |

## Recovery procedure

### 1. Confirm the diagnosis

```bash
sudo lspci -vvv 2>/dev/null | grep -E "^\\S|LnkSta:" | grep -B1 "Width x"
```

You should see two PCIe devices reporting `Width x8`. If you see `Width x16` on one and `Width x0` on another, or `Width x4` on the GPU, the gate is correctly flagging lane degradation.

### 2. Most-likely fix (per sain-01 §5.1 remediation hint)

Power down. Open the chassis. Check whether M.2_2 (the second M.2 NVMe slot, usually adjacent to the second PCIe slot) has a drive. On the ProArt X870E-Creator board:

| Slot | Lanes if M.2_2 empty | Lanes if M.2_2 populated |
|---|---|---|
| PCIe 5.0 x16 #1 (top) | x8 | x8 |
| PCIe 5.0 x16 #2 (bottom) | x8 | x4 (lanes stolen) |
| M.2_2 | empty | x4 |

If M.2_2 is populated and the operator needs both GPUs at x8/x8, move the M.2 NVMe to M.2_1 (which uses CPU lanes that don't overlap with the PCIe slots) or M.2_3/M.2_4 (chipset lanes).

### 3. BIOS bifurcation verification

If M.2_2 is empty and lanes are still degraded:

1. Reboot, enter BIOS (Del at POST).
2. **Advanced → PCI Subsystem → PCIe Bifurcation**.
3. Set to `[x8/x8]` (NOT `[x16/0]` or `[x4/x4/x4/x4]`).
4. Save + exit.

### 4. Re-test the gate

```bash
sudo systemctl start sovereign-guard.service
journalctl -u sovereign-guard.service --since "1 minute ago"
```

Or run the script directly:

```bash
sudo /usr/local/bin/friction-audit
```

Exit code 0 = gate passes; container runtimes can start.

### 5. Confirm via mirror

The CLI mirror shows the latest verdict:

```bash
sudo selfdefctl friction-audit show --json
```

The output should carry `"status":"pass"` for `gate: pcie`. Sovereign-os M060 cockpit panel "Friction Audit" should turn green within 1000ms (MS046 R10971).

## Operator-signed override (deferred fix)

If lanes are genuinely degraded (e.g. hardware fault awaiting RMA) and the operator needs to keep the system running with the gate disabled, an MS003-signed override manifest is required. **This is NOT a recommended path — it weakens the IPS boundary.**

```bash
sudo selfdefctl friction-audit override-create \
    --gate pcie \
    --reason "RMA in progress; slot 2 confirmed bad; ticket #1234" \
    --expires-in 7d \
    --signer-kid <your-MS003-kid> \
    --auditor-kid <auditor-MS003-kid>
```

Both signer + auditor must hold Ring 0 authority (MS039). The override is logged to the OCSF audit chain (MS046 R10877 + R10878) and surfaces as a yellow countdown banner in the MS043 TUI authority panel until expiry.

## Relationships

### Cross-references

- Source: `~/infohub/raw/dumps/2026-05-15-sain-01-master-spec-other-conversation-transposition.md` §5.1 lines 346–353
- Milestone: `selfdef/backlog/milestones/MS046-friction-audit-system-boot-time-hardware-integrity-gate.md`
- Sister gates: `friction-audit-zfs.md`, `friction-audit-memory.md`, `friction-audit-immutability.md`, `friction-audit-signature.md`
- Guardian Daemon (consumer of these verdicts): `selfdef/docs/sdd/` MS044
- Authority + commit chain: MS039 (Ring 0), MS040 (six-profile authority matrix), MS041 (commit authority)
