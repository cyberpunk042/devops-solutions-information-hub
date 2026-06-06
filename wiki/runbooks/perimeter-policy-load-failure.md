---
title: "Operator runbook — perimeter TracingPolicy load failure"
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
tags: [runbook, perimeter, tetragon, tracingpolicy, yaml, sigkill, selfdef, ips]
---

# Operator runbook — perimeter TracingPolicy load failure

## Summary

Operator runbook for **perimeter TracingPolicy load failure**.  Anchored to: Source dump §6 — Tetragon sovereign-kernel-fence TracingPolicy (lines 380-411); SDD-028 perimeter-engine specification. Also references: Catalog milestone MS047. Page metadata: status=draft; maturity=seed; confidence=high; tags=[runbook, perimeter, tetragon, tracingpolicy, yaml].

## Symptom

`/etc/tetragon/tracing-policies/sovereign-perimeter.yaml` exists on disk but Tetragon refuses to load it. One or more of:

- `journalctl -u tetragon.service | grep -i "sovereign-perimeter"` shows `failed to parse` or `validation rejected`.
- `tetra tracingpolicy list` (when available) does NOT list `sovereign-kernel-fence`.
- `bash /usr/share/selfdef/scripts/test/L1-perimeter-yaml-lint.sh` exits non-zero (the local YAML on disk does not match the spec-locked structure).
- `selfdefctl perimeter show` shows `policy: ... (PRESENT)` but verdicts never appear.

## Why this matters

Without a loaded policy, Tetragon is running but **the kernel-fence kprobe is not attached**. Every `sys_execve` succeeds regardless of binary path. This is the same effective state as Tetragon not running, but harder to diagnose because the service appears healthy.

## Diagnosis

```bash
# 1. Is the file on disk and what's its current state?
ls -la /etc/tetragon/tracing-policies/sovereign-perimeter.yaml
lsattr /etc/tetragon/tracing-policies/sovereign-perimeter.yaml   # expect immutable bit

# 2. Does it parse?
python3 -c "import yaml; yaml.safe_load(open('/etc/tetragon/tracing-policies/sovereign-perimeter.yaml'))"

# 3. Does it match the spec-locked structure?
sha256sum /etc/tetragon/tracing-policies/sovereign-perimeter.yaml \
          /usr/share/selfdef/sovereign-perimeter.yaml

# 4. What does Tetragon say?
journalctl -u tetragon.service -n 500 --no-pager | grep -iE "sovereign|tracingpolicy|kprobe"
```

1-step-up-the-stack causes:

| Cause | Investigation |
|---|---|
| YAML hand-edited despite chattr +i lift | `lsattr` shows no `i`; compare sha256 vs `/usr/share/selfdef/sovereign-perimeter.yaml`; restore from package |
| Tetragon version doesn't support the kprobe shape | `tetra version`; the v1alpha1 / Sigkill matchAction needs Tetragon ≥ 0.10 |
| Kernel lacks `sys_execve` kprobe surface | `cat /sys/kernel/debug/tracing/available_filter_functions \| grep sys_execve` — requires `CONFIG_FTRACE_SYSCALLS=y` and `CONFIG_KPROBES=y` |
| Disk-corrupt YAML | `python3 -c "import yaml; ..."` raises ScannerError; reinstall the package: `sudo dpkg-reconfigure selfdef-daemon` |
| Conflicting policy with same metadata.name | `tetra tracingpolicy list \| grep sovereign-kernel-fence`; remove the duplicate |

## Recovery procedure

### 1. Restore the spec-locked YAML

```bash
# Lift the immutable bit (operator-trusted action; verbatim).
sudo chattr -i /etc/tetragon/tracing-policies/sovereign-perimeter.yaml

# Restore from the package-shipped copy.
sudo install -m 0644 -o root -g root \
    /usr/share/selfdef/sovereign-perimeter.yaml \
    /etc/tetragon/tracing-policies/sovereign-perimeter.yaml

# Re-lock.
sudo chattr +i /etc/tetragon/tracing-policies/sovereign-perimeter.yaml
```

### 2. Verify the YAML matches the spec

If a checkout of the selfdef repo is available:

```bash
bash /path/to/selfdef/scripts/test/L1-perimeter-yaml-lint.sh
```

The L1 gate verifies kind / metadata.name / kprobe.call / NotIn operator / Sigkill action / verbatim sain-01 §6 4-entry allowlist. If any drift, the script names which row.

### 3. Reload Tetragon

```bash
sudo systemctl reload tetragon.service \
  || sudo systemctl kill -s HUP tetragon.service \
  || sudo systemctl restart tetragon.service

# Check the load result.
journalctl -u tetragon.service -n 100 --no-pager | grep sovereign
```

### 4. Verify the kprobe is attached

```bash
# Tetra CLI when installed.
tetra tracingpolicy list

# Generic eBPF surface inspection.
sudo bpftool prog list | grep -i kprobe
```

You should see one kprobe program loaded that corresponds to `sys_execve`.

### 5. Smoke-test the fence

```bash
# Attempt a non-allowlisted execve.
sudo -u nobody /tmp/expected-to-die 2>&1 || true
selfdefctl perimeter history --limit 1
```

A `SIGKILL` verdict should appear.

## Operator decision tree

- **YAML drift caused by a botched manual edit**: do NOT hand-edit `/etc/tetragon/tracing-policies/sovereign-perimeter.yaml`. The default allowlist is sain-01 §6 verbatim and frozen. Operator extensions go via `selfdefctl perimeter extend --signed <manifest>`.
- **Tetragon version too old**: pin a Tetragon version that supports `matchActions.action: Sigkill` (≥ 0.10). Downgrade is an operator-decision; document the version pin in the incident log.
- **Kernel lacks the necessary ftrace surface**: this is a kernel-recompile-or-replace-host event; escalate.

## Relationships

### Cross-references

- SDD-028 §Deliverable 1 (TracingPolicy YAML)
- SDD-028 §Deliverable 5 (Debian packaging — postinst install + chattr +i)
- selfdef `scripts/test/L1-perimeter-yaml-lint.sh` (L1 gate)
- Sister runbook: [perimeter-tetragon-not-running](perimeter-tetragon-not-running.md)
- Sister runbook: [perimeter-extension-create](perimeter-extension-create.md)
