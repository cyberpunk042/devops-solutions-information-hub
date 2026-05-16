---
title: E104 — Tetragon + Guardian Perimeter
aliases:
  - "E104 — Tetragon + Guardian Perimeter"
  - "E104 — Tetragon + Guardian: Kernel-Level Auditor"
type: epic
domain: backlog
status: draft
priority: P0
task_type: epic
current_stage: document
readiness: 30
progress: 0
stages_completed: []
artifacts: []
confidence: high
created: 2026-05-16
updated: 2026-05-16
sources:
  - id: milestone
    type: file
    file: "wiki/backlog/milestones/sain-01-sovereign-node.md"
  - id: src-sain-01-sovereign-node-spec
    type: wiki
    file: "wiki/sources/src-sain-01-sovereign-node-spec.md"
  - id: concept-srp-trinity-pulse-weaver-auditor
    type: wiki
    file: "wiki/domains/ai-agents/concept-srp-trinity-pulse-weaver-auditor.md"
  - id: cmp-wall-vs-write-vs-tetragon
    type: wiki
    file: "wiki/comparisons/cmp-wall-vs-write-vs-tetragon-for-perimeter.md"
tags: [epic, sain-01, tetragon, ebpf, guardian, auditor, kernel-perimeter, sigkill, security-audit-log, defense-in-depth]
---

# E104 — Tetragon + Guardian Perimeter

## Summary

Deploy the **Auditor** module (third in the [[concept-srp-trinity-pulse-weaver-auditor|SRP Trinity]]) — a kernel-level perimeter implemented via **Tetragon eBPF** + a user-space **`guardian-core`** Python supervisor + **atomic-append audit log** on the ZFS context dataset. Tetragon loads a `TracingPolicy` named `sovereign-kernel-fence` that allowlists ~4 binaries for `sys_execve` (`/usr/bin/python3`, `/usr/bin/nvidia-smi`, `/usr/local/bin/vllm`, `/usr/bin/podman`); any other syscall in a containerized agent triggers **kernel-space `SIGKILL`** atomically with the syscall attempt. `guardian-core` listens on `/var/run/tetragon/tetragon.events`, catches kill events, kills the offending Podman container, appends to `tank/context/security_audit.log`, optionally rings `/dev/console`. The combination is the SAIN-01 perimeter's prevention layer — wall(1) + write(1) are the notification layer (deployed separately at E108 via the Weaver's profile selection); see [[cmp-wall-vs-write-vs-tetragon-for-perimeter|wall vs write vs Tetragon comparison]]. Includes `BindsTo=tetragon.service` on the guardian-core systemd unit so a Tetragon outage automatically restarts the guardian loop.

## Operator Directive

> "We reject 'bridges' and 'hacks.' Security is enforced at the kernel level using eBPF."

> "Unauthorized system calls within an AI agent's container trigger an immediate SIGKILL by the kernel."

## Goals

See Done When — verifiable kernel-perimeter integrity checkpoints.

## Done When

- [ ] **Tetragon installed** via official Debian package or release binary; LLVM + Clang available for eBPF compilation (`apt-get install -y llvm clang`)
- [ ] **`/etc/tetragon/sovereign-perimeter.yaml`** authored from [[src-sain-01-sovereign-node-spec|§ 6]]'s `TracingPolicy` definition (allowlist: `/usr/bin/python3`, `/usr/bin/nvidia-smi`, `/usr/local/bin/vllm`, `/usr/bin/podman`; NotIn match → Sigkill action)
- [ ] **`systemctl start tetragon`** succeeds; `systemctl status tetragon` shows active + enabled at boot
- [ ] **eBPF programs loaded** — `bpftool prog show` lists the Tetragon-loaded programs
- [ ] **`/var/run/tetragon/tetragon.events`** socket exists + readable by the guardian-core service account
- [ ] **`guardian-core` script** deployed at `/usr/local/bin/guardian-core` (Python 3.11+, mode 0755); content matches [[src-sain-01-sovereign-node-spec|§ 10.1]] verbatim
- [ ] **`guardian-core.service`** systemd unit at `/etc/systemd/system/guardian-core.service`; includes `After=tetragon.service`, `Requires=tetragon.service`, `BindsTo=tetragon.service`, `Restart=always`, `RestartSec=1`
- [ ] **`systemctl enable --now guardian-core`** succeeds; daemon is active
- [ ] **Audit log target ready**: `tank/context/security_audit.log` exists, append-only ACL applied (`chattr +a` or equivalent)
- [ ] **Perimeter test 1** — *allowed syscall*: `podman run --rm <image> /usr/bin/python3 -c "print(1)"` succeeds + does NOT appear in audit log
- [ ] **Perimeter test 2** — *unauthorized syscall*: `podman run --rm <image> /bin/sh -c 'echo hi'` is killed by Tetragon SIGKILL; container exits with code 137; `tank/context/security_audit.log` shows a VIOLATION line
- [ ] **Guardian post-kill cleanup**: the Podman container is removed by guardian-core; `podman ps -a` shows no zombie
- [ ] **PC speaker bell** fires on `/dev/console` for the violation event (operator-verified)
- [ ] **Tetragon outage test**: `systemctl stop tetragon` triggers `guardian-core` to fail (per `BindsTo`); `systemctl status guardian-core` shows the binding failure; `systemctl start tetragon` restarts both cleanly

## Scale and Model

> [!info] Epic Parameters
>
> | Parameter | Value |
> |---|---|
> | **Model** | integration |
> | **Quality tier** | Skyscraper |
> | **Estimated tasks** | 6-8 |
> | **Dependencies** | E101 (kernel with eBPF support), E102 (audit log target on `tank/context`), E103 (containerized agents to enforce against) |
> | **Feeds into** | E107 (Weaver's writes are observable but uncontested; Auditor watches sub-agents), E108 (profiles run sub-agents — Auditor is always on), E110 (resident models run via the allowlisted binaries) |
> | **Critical** | The Auditor is the prevention layer. Failure here = unauthorized syscalls go unblocked. No partial deployment acceptable. |

## Handoff Context

> [!info] For a fresh context picking up this epic:
>
> - Milestone: [[sain-01-sovereign-node|Milestone — SAIN-01 Sovereign AI Node]]
> - L1 spec section: [[src-sain-01-sovereign-node-spec|§ 6 Real-Time Security Perimeter Engine + § 10 Native Guardian Event Loop]]
> - Trinity concept (the Auditor's role): [[concept-srp-trinity-pulse-weaver-auditor|SRP Trinity]] — the Auditor is the only Trinity module operating primarily in kernel space
> - Wall/write/Tetragon comparison ([[cmp-wall-vs-write-vs-tetragon-for-perimeter|comparison page]]) — Tetragon prevents; wall + write notify; do not collapse them into a single "perimeter" mechanism
> - **Composition with selfdef's `agent-guard` module**: both Tetragon-based; eventual Stage-2 transposition will merge policies. For now, deploy `sovereign-kernel-fence` standalone; selfdef coexistence is a future epic.

## Relationships

- PART OF: [[sain-01-sovereign-node|Milestone — SAIN-01 Sovereign AI Node]]
- DEPENDS ON: [[e101-sovereign-os-build|E101 — Sovereign OS Build]]
- DEPENDS ON: [[e102-zfs-storage-layout|E102 — ZFS Storage Layout]] (audit log destination)
- DEPENDS ON: [[e103-vfio-isolation|E103 — VFIO Isolation]] (sandboxed agents to enforce against)
- ENABLES: [[e107-weaver-state-fabric|E107 — Weaver State Fabric]] (Auditor watches Weaver writes)
- ENABLES: [[e108-load-balancing-profiles|E108 — Load-Balancing Profiles]] (Auditor is always on across profiles)
- IMPLEMENTS: [[concept-srp-trinity-pulse-weaver-auditor|Concept — SRP Trinity (Auditor)]]
- IMPLEMENTS: [[src-sain-01-sovereign-node-spec|SAIN-01 Sovereign Node Spec]] §§ 4.1, 6, 10
- RELATES TO: [[cmp-wall-vs-write-vs-tetragon-for-perimeter|Comparison — wall vs write vs Tetragon]] (Tetragon is the only prevention mechanism)
- CONSTRAINS: future Stage-2 selfdef integration (selfdef `agent-guard` policies must merge cleanly with `sovereign-kernel-fence`)

## Backlinks

(will be populated by `tools/obsidian.py backlinks` after pipeline post)
