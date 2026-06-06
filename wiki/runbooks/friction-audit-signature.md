---
title: "Operator runbook — friction-audit signature gate failure"
type: reference
domain: ai-agents
layer: 2
status: draft
confidence: high
maturity: seed
created: 2026-05-20
updated: 2026-05-20
sources:
  - id: selfdef-sdd-027
    type: internal
    project: selfdef
    path: docs/sdd/027-friction-audit-system.md
    note: "SDD-027 Deliverable 1 + 6 — signature verification before script body executes (MS003 chain-of-trust)"
  - id: selfdef-ms003
    type: internal
    project: selfdef
    path: backlog/milestones/MS003-correlator-store-responder-signing.md
    note: "MS003 selfdef-signing — minisign-verify chain-of-trust"
  - id: selfdef-ms046
    type: internal
    project: selfdef
    path: backlog/milestones/MS046-friction-audit-system-boot-time-hardware-integrity-gate.md
    note: "MS046 R10805-R10807 (signature path + verification + CRITICAL severity), F05407-F05409, R11254-R11258"
tags: [runbook, friction-audit, signature, ms003, minisign, key-rotation, sain-01, selfdef, ips, ring-0, critical]
---

# Operator runbook — friction-audit signature gate failure

## Summary

Operator runbook for **friction-audit signature gate failure**.  Anchored to: SDD-027 Deliverable 1 + 6 — signature verification before script body executes (MS003 chain-of-trust); MS003 selfdef-signing — minisign-verify chain-of-trust. Also references: MS046 R10805-R10807 (signature path + verification + CRITICAL severity), F05407-F05409, R11254-R11258.

## Severity: **CRITICAL** (P6, exit code 6, OCSF severity_id=5)

The signature gate failing means the MS003-signed manifest at `/etc/selfdef/manifests/friction-audit.sig` does not verify against the operator's trust roots. Treated as either active tampering OR a botched key rotation. Investigate before any remediation.

## Symptom

`sovereign-guard.service` fails at boot OR `selfdefctl friction-audit show` flags a Signature FAIL. The friction-audit script does NOT execute its body — the gate is the first thing the script does (per SDD-027 Deliverable 1 F05407-F05409).

`/var/log/selfdef/friction-audit.ocsf.jsonl` carries a Detection 2004 event with severity_id=5 + gate=signature + `metadata.signature.public_key_id` matching the kid that was attempted.

## Diagnosis

| Cause | Investigation |
|---|---|
| MS003 key rotation in progress (old kid signed manifest, new kid is active trust root) | Cross-ref `selfdef-key-rotation-set` state via `selfdefctl keys list` |
| Manifest file corrupted (partial copy, fs issue) | `sudo file /etc/selfdef/manifests/friction-audit.sig`, `sudo wc -c` vs known-good size |
| Manifest replaced with attacker-signed version (signing-key compromise) | Compare current `signer_kid_policy` value to MS003 trust-anchor allowlist |
| Trust roots list missing/wiped (likely systemic) | `ls /etc/selfdef/trust-roots/`, `selfdefctl doctor` |
| Script binary modified — sig no longer matches sha256 (overlaps Immutability gate) | `sudo sha256sum /usr/local/bin/friction-audit` vs signed `sha256` in manifest |
| Time-skew preventing signed-at vs verify-at comparison | `timedatectl status`, NTP sync state |

## Recovery procedure — **OPERATOR-ONLY**

### 1. Diagnostic surface

```bash
# Look at the manifest itself:
sudo cat /etc/selfdef/manifests/friction-audit.sig
sudo cat /etc/selfdef/manifests/friction-audit.sig.json    # if JSON-wrapped manifest

# Compare the manifest's claimed signer_kid to the trust roots:
selfdefctl keys list

# Run the doctor across all signing-related state:
sudo selfdefctl doctor

# OCSF event for this incident:
sudo tail /var/log/selfdef/friction-audit.ocsf.jsonl | jq 'select(.gate=="signature")'
```

### 2. Likely-cause: key rotation incomplete

If `selfdefctl keys list` shows a recent rotation event (new kid registered as Signing, old kid Verifying or Retired), the manifest was likely signed by the old kid that's now Retired. Re-sign the manifest with the current Signing key:

```bash
# (Operator-supervised re-sign — MS003-canonical procedure)
sudo selfdefctl keys sign \
    --in /usr/local/bin/friction-audit \
    --out /etc/selfdef/manifests/friction-audit.sig \
    --signer-kid <current-signing-kid>

# Verify locally before re-running gate:
selfdefctl keys verify \
    --target /usr/local/bin/friction-audit \
    --manifest /etc/selfdef/manifests/friction-audit.sig
```

### 3. Likely-cause: corrupted manifest

```bash
# Re-install from package (the postinst will re-drop the manifest):
sudo apt-get install --reinstall selfdef-daemon

# OR manually if you have a known-good manifest backup:
sudo install -m 0644 -o root -g root \
    /var/backups/selfdef/manifests/friction-audit.sig.YYYY-MM-DD \
    /etc/selfdef/manifests/friction-audit.sig
```

### 4. Suspicious-cause: kid mismatch with trust anchors

Compare the kid in the manifest against the operator-authorized trust roots:

```bash
sudo cat /etc/selfdef/trust-roots/*.pub
sudo cat /etc/selfdef/manifests/friction-audit.sig | head -3   # contains the signer kid
```

If the kid is NOT in the trust roots, the manifest was signed by a key NOT authorized by the operator. **Treat as active compromise**:

1. Isolate the host (`sudo systemctl stop podman docker containerd sshd`)
2. Investigate from console / out-of-band only
3. Audit MS003 key store for unauthorized issued kids
4. Rotate ALL MS003 signing keys (cross-ref `selfdef-key-rotation-set` crate)
5. Re-sign all dependent manifests (friction-audit, sovereign-perimeter.yaml, etc.)

### 5. Verify after remediation

```bash
sudo selfdefctl friction-audit replay
sudo selfdefctl friction-audit show --json | jq '.[] | select(.gate=="signature")'
# expect "status":{"status":"pass"}
```

### 6. Time-skew check (often-missed cause)

```bash
sudo timedatectl status
# NTP service: active
# System clock synchronized: yes
# Time zone: UTC

# If skew > 60s, sync first then re-test:
sudo systemctl restart systemd-timesyncd
```

## Cross-cutting — key rotation discipline

The friction-audit signature is one of MANY MS003-signed manifests in selfdef. When you rotate a key, you MUST re-sign:

| Surface | Manifest path | Re-sign command |
|---|---|---|
| friction-audit script | `/etc/selfdef/manifests/friction-audit.sig` | `selfdefctl keys sign --target friction-audit` |
| sovereign-perimeter.yaml (eBPF) | `/etc/selfdef/manifests/sovereign-perimeter.sig` | `selfdefctl keys sign --target sovereign-perimeter.yaml` |
| detection rules | `/etc/selfdef/manifests/rules/*.sig` | `selfdefctl keys verify-dir --rotate-kid <new>` |
| allowlist extensions | `/etc/selfdef/perimeter-extensions/*.json` | individually per active extension |

Use `selfdefctl keys rotate --new-kid <id>` to automate (when implemented; tracked in `selfdef-key-rotation-set` crate runtime crate, MS046 D4).

## Operator-signed override

**Never override the signature gate** unless you've manually verified the script binary's sha256 against an out-of-band-trusted source (e.g., the GitHub release page checksum). The signature gate IS the chain-of-trust root for friction-audit — if you override it, you're saying "I personally vouch for this binary out-of-band."

```bash
# Minimum-trust override (use sparingly):
sudo selfdefctl friction-audit override-create \
    --gate signature \
    --reason "Out-of-band-verified sha256=<HASH> matches GitHub release v<VERSION>" \
    --expires-in 24h \
    --signer-kid <your-MS003-kid> \
    --auditor-kid <auditor-MS003-kid> \
    --legal-review-kid <legal-review-MS003-kid>
```

Same multi-sig + legal-review requirement as the immutability gate (MS046 F05452 + sovereign-os M081 F06785 must-not-touch tier).

## Relationships

### Cross-references

- Source: derived from the MS003 selfdef-signing pattern (no specific sain-01 dump section; signature is operator-extended for chain-of-trust)
- Milestone: `selfdef/backlog/milestones/MS046-friction-audit-system-boot-time-hardware-integrity-gate.md` R10805-R10807, R11254-R11258
- MS003 selfdef-signing: `selfdef/crates/selfdef-signing/`
- Key rotation set: `selfdef/crates/selfdef-key-rotation-set/` (Cycle-2 catalog)
- Sister gates: `friction-audit-pcie.md`, `friction-audit-zfs.md`, `friction-audit-memory.md`, `friction-audit-immutability.md`
- Sovereign-OS dependency: M081 Whitelabel Architecture must-not-touch tier (legal-review co-signature)
