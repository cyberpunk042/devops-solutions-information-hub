---
title: "Operator runbook — friction-audit immutability gate failure"
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
    note: "Source dump §5 line 339 'immutable boot-time script' — the underlying invariant"
  - id: selfdef-sdd-027
    type: internal
    project: selfdef
    path: docs/sdd/027-friction-audit-system.md
    note: "SDD-027 Deliverable 6 Debian postinst chattr +i + IMA-appraise hash, operator-extension for tampering resistance"
  - id: selfdef-ms046
    type: internal
    project: selfdef
    path: backlog/milestones/MS046-friction-audit-system-boot-time-hardware-integrity-gate.md
    note: "MS046 R10803-R10806 (chattr +i + IMA), F05405-F05409 (immutability enforcement), F05635 (P8 code), R11183 (CRITICAL severity)"
tags: [runbook, friction-audit, immutability, chattr, ima-appraise, tampering, sain-01, selfdef, ips, ring-0, critical]
---

# Operator runbook — friction-audit immutability gate failure

## Severity: **CRITICAL** (P8, exit code 5, OCSF severity_id=5)

The immutability gate failing means **someone modified `/usr/local/bin/friction-audit` after install**. This is treated as an active-tampering signal, not an operational glitch. Investigate before reverting.

## Symptom

`sovereign-guard.service` fails at boot OR `selfdefctl friction-audit show` flags an Immutability FAIL. The chattr immutable attribute (`+i`) on the script binary OR its IMA-appraise extended-attribute hash has been removed or modified. The friction-audit script body itself may also have changed.

OCSF Detection 2004 event class with severity_id=5 (CRITICAL) is emitted to `/var/log/selfdef/friction-audit.ocsf.jsonl`. The Guardian Daemon (MS044) consumes this event and additionally emits a console alert via `/dev/console`.

## Diagnosis

| Cause | Investigation | Severity |
|---|---|---|
| Legitimate package upgrade applying new script (postinst ran) | `dpkg -l selfdef-daemon` shows recent timestamp; `journalctl -u dpkg` confirms | LOW (transient — re-applies chattr) |
| Operator manually edited the script (forbidden — modify via package only) | `last \| head`, `journalctl /var/log/auth.log \| grep sudo` | MEDIUM (operator discipline) |
| Attacker with root privilege removed chattr +i + modified script | unexpected auth.log entries, unfamiliar SSH sessions, unexplained sudo events | **CRITICAL** (active compromise) |
| Filesystem corruption (rare; manifests as random chattr loss) | `dmesg \| grep -E "EXT[234]\|btrfs\|zfs"`, `e2fsck` on /usr partition | HIGH (compromised storage) |
| IMA appraise policy not loaded (kernel-side rather than file-side) | `cat /sys/kernel/security/integrity/ima/policy 2>/dev/null` empty | MEDIUM (config drift) |

## Recovery procedure — **OPERATOR-ONLY**

This gate cannot be auto-recovered by the daemon. The remediation procedure REQUIRES operator action by design (MS046 R11013 — never auto-mutates the script).

### 1. Confirm the failure

```bash
sudo lsattr /usr/local/bin/friction-audit
# Expect:
#   ----i--------------- /usr/local/bin/friction-audit
# If the 'i' is missing, chattr +i was removed.

sudo getfattr -d -m security.ima /usr/local/bin/friction-audit
# If empty or missing → IMA-appraise hash stripped.

sudo sha256sum /usr/local/bin/friction-audit
# Compare against /usr/share/selfdef/friction-audit.sha256
sudo cat /usr/share/selfdef/friction-audit.sha256
```

If the script's `sha256sum` differs from the package-known good, **the script body was modified**. Do NOT just re-chattr — the modification itself is the attack signal.

### 2. Investigate the attack surface

```bash
# Audit log of root-level actions:
sudo journalctl --since "24 hours ago" | grep -E "sudo:|chattr|/usr/local/bin/friction-audit"

# Active SSH sessions:
sudo who; sudo last | head -20

# Recent root login attempts:
sudo grep -E "Accepted|Failed" /var/log/auth.log | tail -30

# selfdef OCSF event chain (Detection 2004 + Audit 1003):
sudo tail -100 /var/log/selfdef/friction-audit.ocsf.jsonl | jq

# Tetragon eBPF perimeter logs (MS047 sister gate):
sudo journalctl -u tetragon | grep -i sigkill | tail
```

If anything suspicious surfaces → **isolate the host first** before remediation:

```bash
sudo systemctl stop podman docker containerd
sudo systemctl stop sshd  # cuts attacker out
# then investigate from console / out-of-band only
```

### 3. Restoration (only after investigation is complete)

If the modification was confirmed legitimate (package upgrade) or operator-attributable (signed by your audit trail), restore the canonical state:

```bash
# Re-install from package (overwrites the script with package-shipped version):
sudo apt-get install --reinstall selfdef-daemon

# OR manually if package not available:
sudo install -m 0755 -o root -g root \
    /usr/share/selfdef/friction-audit.sh \
    /usr/local/bin/friction-audit

# Re-apply chattr +i:
sudo chattr +i /usr/local/bin/friction-audit

# Verify IMA-appraise hash is now in extended attributes:
sudo getfattr -d -m security.ima /usr/local/bin/friction-audit

# Verify:
sudo lsattr /usr/local/bin/friction-audit
sudo sha256sum /usr/local/bin/friction-audit
```

### 4. Re-test the gate

```bash
sudo selfdefctl friction-audit replay
sudo selfdefctl friction-audit show --json | jq '.[] | select(.gate=="immutability")'
```

### 5. Record the incident

Even a benign cause (package upgrade) should be recorded for cross-cutting audit chain integrity (MS046 R10890, R11086):

```bash
# Use the operator-runbook contribute path in info-hub:
.venv/bin/python -m tools.gateway contribute \
    --type lesson \
    --title "Friction-audit immutability incident YYYY-MM-DD <hostname>" \
    --content "$(cat <<EOF
Date: $(date -u +%Y-%m-%dT%H:%M:%SZ)
Host: $(hostname -f)
Cause classification: (operator-attributable | package-upgrade | suspected-tampering | filesystem-corruption | ima-policy-drift)
Detection: <how it was detected>
Forensic trail: <commands + outputs>
Remediation: <what fixed it>
Lessons: <preventive controls if any>
EOF
)"
```

## Operator-signed override

**Strongly discouraged** for immutability failures. Overriding this gate tells the IPS to allow boot while the integrity of the IPS itself is broken — that's the worst kind of override. Use ONLY if you have isolated investigation evidence that the failure is benign + cannot be remediated in <24h.

```bash
sudo selfdefctl friction-audit override-create \
    --gate immutability \
    --reason "Investigation #INC-2026-XXXX confirms benign cause; remediation pending RMA" \
    --expires-in 24h \
    --signer-kid <your-MS003-kid> \
    --auditor-kid <auditor-MS003-kid> \
    --legal-review-kid <legal-review-MS003-kid>   # mandatory for immutability (must-not-touch tier)
```

The legal-review signer is mandatory per the audit/Whitelabel "must-not-touch" doctrine (MS046 F05452 + sovereign-os M081 F06785). Operator + auditor alone cannot honor an immutability failure.

## Relationships

### Cross-references

- Source: `~/infohub/raw/dumps/2026-05-15-sain-01-master-spec-other-conversation-transposition.md` §5 line 339 "immutable boot-time script"
- Milestone: `selfdef/backlog/milestones/MS046-friction-audit-system-boot-time-hardware-integrity-gate.md` R10803, R11183
- Sister gates: `friction-audit-pcie.md`, `friction-audit-zfs.md`, `friction-audit-memory.md`, `friction-audit-signature.md`
- Guardian Daemon (alert consumer): selfdef MS044 (Tetragon → Guardian → SIGKILL + console alert)
- eBPF perimeter (kernel sibling gate): selfdef MS047 (Tetragon TracingPolicy sovereign-kernel-fence)
- IMA-appraise reference: kernel.org/doc/Documentation/security/IMA-appraisal.txt
