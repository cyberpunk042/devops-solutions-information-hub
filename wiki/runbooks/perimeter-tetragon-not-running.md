---
title: "Operator runbook — perimeter Tetragon not running"
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
    note: "Source dump §6 — Tetragon sovereign-kernel-fence TracingPolicy (lines 380-411)"
  - id: selfdef-sdd-028
    type: internal
    project: selfdef
    path: docs/sdd/028-perimeter-engine.md
    note: "SDD-028 perimeter-engine specification"
  - id: selfdef-ms047
    type: internal
    project: selfdef
    path: backlog/milestones/MS047-real-time-security-perimeter-engine-tetragon-kernel-fence.md
    note: "Catalog milestone MS047"
tags: [runbook, perimeter, tetragon, sovereign-kernel-fence, sigkill, ips, kernel-fence, sain-01, selfdef]
---

# Operator runbook — perimeter Tetragon not running

## Summary

Operator runbook for **perimeter Tetragon not running**.  Anchored to: Source dump §6 — Tetragon sovereign-kernel-fence TracingPolicy (lines 380-411); SDD-028 perimeter-engine specification. Also references: Catalog milestone MS047. Page metadata: status=draft; maturity=seed; confidence=high; tags=[runbook, perimeter, tetragon, sovereign-kernel-fence, sigkill].

## Symptom

One or more of the following:

- `selfdefctl perimeter show` displays `policy: /etc/tetragon/tracing-policies/sovereign-perimeter.yaml (PRESENT)` but the verdict ring buffer is empty and no events appear in `/var/log/selfdef/perimeter.ocsf.jsonl` despite recent `execve` activity.
- `journalctl -u selfdefd | grep -i perimeter` shows the WARN line `perimeter: sovereign-kernel-fence TracingPolicy NOT present — kernel-fence is OFF` or `perimeter: extension store load failed`.
- `systemctl status tetragon.service` is `inactive (dead)` or `failed`.
- An execve of a non-allowlisted binary (e.g. `/usr/bin/curl`) succeeds when it should have been killed by the in-kernel fence.

## Why this matters

When Tetragon is not running, the `sovereign-kernel-fence` TracingPolicy is **not loaded into the kernel**. That means no `sys_execve` kprobe is firing, no `Sigkill` matchAction is being evaluated, and **any binary** can be executed by any process with the relevant capabilities. The perimeter is OFF until Tetragon comes back.

This is the highest-severity loss-of-enforcement event short of the kernel itself being compromised.

## Diagnosis

```bash
systemctl status tetragon.service
systemctl is-active tetragon.service
journalctl -u tetragon.service -n 200 --no-pager
ls -la /etc/tetragon/tracing-policies/sovereign-perimeter.yaml
lsattr /etc/tetragon/tracing-policies/sovereign-perimeter.yaml   # expect '----i---------e----' (immutable)
```

1-step-up-the-stack causes:

| Cause | Investigation |
|---|---|
| Tetragon package not installed | `dpkg -l \| grep tetragon` — install via `apt install tetragon` if absent |
| Tetragon service masked / disabled | `systemctl is-enabled tetragon.service`; `unmask` if masked |
| Tetragon crash loop | `journalctl -u tetragon.service` — look for OOM or eBPF verifier rejection |
| Kernel too old for the eBPF programs | `uname -r` vs Tetragon's minimum supported (5.10+ for full kprobe set) |
| `bpffs` not mounted | `mount \| grep bpf` — Tetragon needs `/sys/fs/bpf` mounted |
| Conflict with another eBPF tracer | check `bpftool prog list` for conflicting loaded programs |

## Recovery procedure

### 1. Confirm Tetragon is the failing component

```bash
systemctl status tetragon.service
selfdefctl perimeter show
```

If `policy: ... (PRESENT)` is true but no verdicts arrive, Tetragon is the failure point.

### 2. Restart Tetragon

```bash
sudo systemctl start tetragon.service
sudo systemctl status tetragon.service
```

If it starts, verify the policy is loaded:

```bash
# Tetragon's tracing-policy listing (via tetra CLI when available)
tetra tracingpolicy list 2>/dev/null | grep sovereign-kernel-fence

# Fallback — confirm the file is on disk and Tetragon is watching the dir
ls -la /etc/tetragon/tracing-policies/sovereign-perimeter.yaml
journalctl -u tetragon.service -n 50 --no-pager | grep -i "policy.*load"
```

### 3. If Tetragon refuses to start

Capture the failure:

```bash
journalctl -u tetragon.service -n 500 --no-pager > /tmp/tetragon-failure-$(date +%s).log
```

Common failure → fix:

| journalctl signature | Likely fix |
|---|---|
| `verifier rejected program` | Kernel is too old or BPF JIT is disabled; check `cat /proc/sys/net/core/bpf_jit_enable` (should be 1) |
| `cannot mount bpffs` | `sudo mount -t bpf bpf /sys/fs/bpf` then retry |
| `permission denied` reading policy | `ls -la /etc/tetragon/tracing-policies/`; YAML must be world-readable (mode 0644) |
| `failed to parse TracingPolicy` | Run `bash scripts/test/L1-perimeter-yaml-lint.sh` from selfdef checkout; the YAML is chattr +i so any drift requires `chattr -i` first |

### 4. Verify perimeter is back online

```bash
# Trigger a controlled SIGKILL by attempting a non-allowlisted binary.
# Replace with a binary you control and don't actually need to run:
sudo -u nobody /tmp/expected-to-die 2>&1 || true

# Then inspect the verdict ring:
selfdefctl perimeter history --limit 5
```

You should see a `SIGKILL` verdict appear for the test binary.

### 5. Re-engage the watchdog

If `selfdef-guardian-daemon` (MS044) is deployed, ensure it is running so Tetragon outages get alerted in the future:

```bash
sudo systemctl status selfdef-guardian.service
```

## Operator decision tree

- **Tetragon refuses to start AND the host needs to come up NOW**: there is no SDD-028 escape hatch. The TracingPolicy is the perimeter; without Tetragon there IS no perimeter. The friction-audit gate (MS046) is independent and still fires at boot; that is the only remaining hardware-frame discipline. Operator should weigh: bring host up un-fenced (document in incident log) vs. wait for Tetragon repair.
- **Tetragon repeatedly crashes after kernel upgrade**: pin Tetragon version compatible with the new kernel; downgrade Tetragon if needed.
- **Long-term Tetragon outage**: file an incident, escalate to vendor; sovereign-os cockpit M061 panel will continue showing the perimeter as `policy PRESENT` but with no recent verdicts (gray state).

## Relationships

### Cross-references

- SDD-028 §Deliverable 1 (TracingPolicy YAML)
- SDD-028 §Deliverable 10 (daemon boot observability)
- `selfdef-guardian-daemon` (MS044) — Tetragon watchdog
- Sister runbook: [perimeter-policy-load-failure](perimeter-policy-load-failure.md)
- Sister runbook: [perimeter-sigkill-investigation](perimeter-sigkill-investigation.md)
- Hardware-frame sibling: [friction-audit-pcie](friction-audit-pcie.md) (MS046)
