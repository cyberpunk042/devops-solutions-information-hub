---
title: wall(1) vs write(1) vs Tetragon eBPF — Operator-Perimeter Mechanisms
aliases:
  - "wall(1) vs write(1) vs Tetragon eBPF — Operator-Perimeter Mechanisms"
  - "Operator Perimeter Comparison"
  - "Notification vs Enforcement"
type: comparison
layer: 3
maturity: growing
domain: devops
status: synthesized
confidence: high
created: 2026-05-16
updated: 2026-05-16
sources:
  - id: src-sain-01-sovereign-node-spec
    type: wiki
    file: "wiki/sources/src-sain-01-sovereign-node-spec.md"
    title: "Synthesis — SAIN-01 Sovereign Node Master Spec"
  - id: concept-srp-trinity-pulse-weaver-auditor
    type: wiki
    file: "wiki/domains/ai-agents/concept-srp-trinity-pulse-weaver-auditor.md"
    title: "Concept — SRP Trinity (Pulse, Weaver, Auditor)"
  - id: concept-vfio-gpu-isolation-amd-iommu
    type: wiki
    file: "wiki/domains/devops/concept-vfio-gpu-isolation-amd-iommu.md"
    title: "Concept — VFIO GPU Isolation with AMD IOMMU"
  - id: selfdef-notify-channels
    type: project
    project: "selfdef"
    path: "docs/operator/channels.md"
    title: "selfdef — notification channels (wall + write among 12 channels)"
  - id: tetragon-docs
    type: documentation
    url: "https://tetragon.io/docs/"
    title: "Tetragon documentation — eBPF-based runtime security"
tags:
  - comparison
  - devops
  - perimeter
  - operator-notification
  - kernel-enforcement
  - tetragon
  - ebpf
  - wall
  - write
  - selfdef
  - sain-01
  - security
  - defense-in-depth
---

# wall(1) vs write(1) vs Tetragon eBPF — Operator-Perimeter Mechanisms

## Summary

Three mechanisms used in the [[src-sain-01-sovereign-node-spec|SAIN-01]] + `cyberpunk042/selfdef` ecosystems for **operator perimeter enforcement and notification**, each operating at a structurally different layer: **`wall(1)`** is a userspace broadcast — writes a one-line attention banner to every logged-in TTY (system-wide, no filtering); **`write(1)`** is a userspace per-user message — writes the same banner to a specific user's TTY (allowlist-targeted, sibling of wall); **Tetragon eBPF** is kernel-space enforcement — `TracingPolicy` rules trigger `SIGKILL` on unauthorized syscalls (no notification primitive at all; pure control). These are **not interchangeable** — they answer different questions: "did the operator notice?" (wall, write) vs "did the unauthorized action happen?" (Tetragon). The SAIN-01 Auditor module uses Tetragon as its kernel-level enforcement substrate; the SAIN-01 Weaver could use wall/write to notify the operator when high-severity events fire; the existing selfdef notifier already ships wall + write as 2 of its 12 outbound channels. **Headline insight**: defense-in-depth requires layering all three (Tetragon for prevention, wall/write for human attention) — picking one without the others leaves either the perimeter leaky (no kernel kill) or invisible (no operator notification).

## Comparison Matrix

> [!abstract] wall(1) vs write(1) vs Tetragon eBPF
>
> | Dimension | `wall(1)` | `write(1)` | Tetragon eBPF |
> |---|---|---|---|
> | **Layer** | Userspace subprocess | Userspace subprocess | **Kernel space** (eBPF programs) |
> | **Primary purpose** | **Operator notification** (broadcast) | **Operator notification** (per-user) | **Action enforcement** (no notification) |
> | **Action on event** | Writes one-line banner to all TTYs | Writes one-line banner to one user's TTY | **SIGKILL** (or `Sigkill`/`Override`/`NotifyKiller`/mask actions) |
> | **Target audience** | **All logged-in users** | **Specific allowlisted users** | The offending process (kills it) |
> | **Filtering mechanism** | None (system-wide) — `mesg n` from receiver to opt out | **Username allowlist** ([a-zA-Z0-9._-]+ regex-validated) | TracingPolicy `matchArgs` rules (per-syscall, per-binary, per-arg) |
> | **Notification reaches operator?** | Yes, if at a TTY | Yes, if at a TTY in the allowlist | **No** (kernel-internal; needs companion daemon to surface event) |
> | **Prevents action?** | **No** (purely informational) | **No** (purely informational) | **Yes** (atomic with syscall attempt) |
> | **Where deployed in SAIN-01** | Possible (Weaver could fire on high-severity events) | Possible (Weaver could fire to operator account allowlist) | **Mandatory — the Auditor's substrate** |
> | **Where deployed in selfdef** | 1 of 12 notifier channels (`[notifier.wall]`) | 1 of 12 notifier channels (`[notifier.write]`) | `agent-guard` module's TracingPolicies (independent of notifier) |
> | **Severity floor (default)** | `high` (loud-by-design; routine events shouldn't broadcast) | `high` (same posture) | n/a (every match-event is enforced) |
> | **Binary path** | `/usr/bin/wall` | `/usr/bin/write` | Kernel eBPF programs loaded by Tetragon daemon |
> | **Daemon required?** | No (subprocess per-event) | No (subprocess per-user, per-event) | **Yes** (Tetragon must be running) |
> | **Latency from event to action** | ~milliseconds (subprocess spawn + TTY write) | ~milliseconds × N users | **Microseconds** (kernel-space, atomic with syscall) |
> | **Reliability** | Depends on user being at TTY (`mesg n` defaults) | Same, but narrower target = higher hit rate | High (no user-side cooperation required) |
> | **Composability** | Composes with anything (output is a string) | Same as wall | Composes with userspace logger (`guardian-core` in SAIN-01; selfdef daemon's escalation engine) |
> | **Operator can suppress?** | Yes (`mesg n` on their TTY) | Yes (mesg n; or removal from allowlist) | **No** (operator IS the policy author; not "suppressible by the target") |
> | **Audit trail** | Banner appears in user's terminal scrollback (transient) | Same (transient + per-user) | **Persistent** (Tetragon logs via stream + `guardian-core` appends to `tank/context/security_audit.log`) |
> | **Network surface required?** | None | None | None (kernel-internal) — but the audit log is consumed locally by `guardian-core` |

## Key Insights

> [!abstract] These three are NOT alternatives — they answer different questions
>
> The "vs" framing of this page is misleading by the standards of normal comparison pages. wall, write, and Tetragon are not three implementations of the same thing — they are **three different layers of the perimeter**. Tetragon prevents; wall + write notify. A complete perimeter has Tetragon (to make the action atomically impossible) and wall/write (to make the human aware that the attempt happened, the policy fired, etc.). Picking one without the others = an incomplete perimeter. ([[concept-srp-trinity-pulse-weaver-auditor|SRP Trinity concept]])

> [!warning] wall(1) has no per-user filtering — write(1) is the per-user sibling
>
> A common mistake: assuming `wall(1)` accepts a `users=` filter. It does not. `wall(1)` broadcasts to every logged-in TTY where the receiver hasn't `mesg n`'d. The `[notifier.wall].users` knob **intentionally does not exist** in the selfdef config (D-024 from selfdef's decisions log). The per-user transport is `write(1)`, which IS what `[notifier.write].users` configures. If your use case wants "notify only Alice and Bob," that's `write`, not `wall`. ([[selfdef-notify-channels|selfdef notification channels doc]])

> [!success] Tetragon is the only mechanism that can stop an attempt
>
> wall and write tell the operator "something happened"; Tetragon makes the something not happen. In kernel space, before user-space resumes execution. For perimeter integrity, this is categorically different from notification. The SAIN-01 Auditor uses Tetragon for exactly this reason — a user-space supervisor can be racy (between detection and intervention, the violating agent can do damage). Kernel-space `SIGKILL` is atomic with the syscall attempt. ([[src-sain-01-sovereign-node-spec|SAIN-01 synthesis]])

> [!tip] Defense-in-depth layers all three (plus more)
>
> The most-defensible operator-perimeter posture is to layer:
>
> 1. **Tetragon** (kernel enforcement) — kills unauthorized syscalls atomically
> 2. **write(1)** (per-user notification) — tells the operator a kill happened, on their specific TTY
> 3. **wall(1)** (broadcast notification) — louder fallback for severity-critical events; alerts anyone at any TTY
> 4. **`guardian-core`** (Python daemon) — bridges Tetragon's kernel events to userspace + ZFS audit log + Podman container kill
> 5. **selfdef notifier chain** (12 channels) — escalation beyond the host (SMS, email, PagerDuty, etc.) if the operator isn't at a TTY
>
> Each layer fails independently without compromising the others. Tetragon failure = unauthorized syscalls go through; wall/write failure = operator unaware but action still prevented; guardian-core failure = no Podman cleanup but kernel kill still happened.

> [!info] The same wall/write binaries are used in both projects
>
> Notable architectural symmetry: the SAIN-01 Weaver's (hypothetical) notification path uses `/usr/bin/wall` + `/usr/bin/write` — the same binaries selfdef's notifier already invokes for its `[notifier.wall]` + `[notifier.write]` channels. The two systems can coexist (each fires the binary independently); duplicate banners on the operator's TTY is the only conflict, and severity-floor tuning resolves it. ([[selfdef-notify-channels|selfdef channels]])

## Deep Analysis

### Layer-by-layer

#### Userspace notification layer (wall + write)

`wall(1)` and `write(1)` are POSIX-standard userspace utilities. They are subprocess-invoked, not daemon-resident. Each invocation:

1. The caller (Tetragon supervisor, selfdef notifier, manual operator) spawns the binary
2. The binary opens the target TTYs (all logged-in TTYs for wall; the configured user's TTY for write)
3. Writes the banner to those TTYs
4. Exits

**Strengths:**
- Zero dependencies — POSIX-standard, present on every Linux/Unix system
- No daemon to fail
- Composable with anything (input via stdin or argv)
- Transparent to the operator at the receiving end (banner just appears)

**Weaknesses:**
- **Cannot prevent actions** — purely informational
- Subprocess spawn overhead per-event (milliseconds-class; not suitable for high-frequency events)
- TTY-bound — if the operator isn't at a TTY (locked screen, headless server, remote SSH not active), the banner is invisible
- `mesg n` opt-out is a per-user setting that disables wall (no operator-side override)

#### Kernel enforcement layer (Tetragon)

[Tetragon](https://tetragon.io/) is the Cilium-project's eBPF-based runtime security framework. It loads kernel-level programs (eBPF) that hook into syscall paths and execute policy decisions in kernel space.

For the SAIN-01 Auditor, the policy is a `TracingPolicy` that allowlists ~4 binaries for `sys_execve`:

```yaml
apiVersion: cilium.io/v1alpha1
kind: TracingPolicy
metadata:
  name: "sovereign-kernel-fence"
spec:
  kprobes:
  - call: "sys_execve"
    syscall: true
    args:
    - index: 0
      type: "string"
    selectors:
    - matchArgs:
      - index: 0
        operator: "NotIn"
        values:
        - "/usr/bin/python3"
        - "/usr/bin/nvidia-smi"
        - "/usr/local/bin/vllm"
        - "/usr/bin/podman"
      matchActions:
      - action: Sigkill
```

When a containerized agent attempts `execve("/bin/bash", ...)`, the eBPF program fires; the policy's `NotIn` selector matches; the `Sigkill` action is applied to the calling thread atomically — the syscall never returns to user space.

**Strengths:**
- **Prevention, not just notification** — the unauthorized action never happens
- **Atomic** with the syscall attempt — no race window between detection and intervention
- **Microsecond-class latency** — kernel-space execution is faster than userspace subprocess spawn
- **No user cooperation required** — the target process doesn't get a vote
- Composes with arbitrary policy complexity (per-binary, per-arg, per-container)

**Weaknesses:**
- Requires Tetragon daemon running (eBPF program loader + event streamer)
- Steeper operational complexity than wall/write (TracingPolicy YAML, eBPF debugging, IOMMU/container interactions)
- No notification primitive — needs a companion userspace daemon to surface events to the operator
- Policy authoring requires expertise (YAML schema, syscall coverage, false-positive avoidance)

#### Companion bridging layer (`guardian-core` for SAIN-01)

The SAIN-01 Auditor pairs Tetragon with `guardian-core` — a small Python daemon listening on `/var/run/tetragon/tetragon.events`. When Tetragon fires a `Sigkill`, `guardian-core`:

1. Parses the kernel event JSON
2. Kills the offending Podman container (cleanup)
3. Appends a row to `tank/context/security_audit.log` (audit trail)
4. Optionally rings `/dev/console` (PC speaker — local operator audible alert)

`guardian-core` is **not** a third notification mechanism; it's the bridge between Tetragon's kernel events and the userspace world that wall + write live in. The right framing: Tetragon enforces, guardian-core orchestrates post-kill cleanup + audit logging, wall/write surfaces the event to the operator's attention.

### Where each fits in the SAIN-01 Trinity

| Trinity module | Layer | Mechanism |
|---|---|---|
| **The Pulse** (CPU vector core) | none — Pulse doesn't enforce or notify | n/a |
| **The Weaver** (state orchestration) | Userspace notification — when high-severity state events fire | `wall(1)` + `write(1)` (via selfdef's notifier or a Weaver-side fire mechanism) |
| **The Auditor** (immutable gatekeeper) | Kernel enforcement + bridging | **Tetragon eBPF** + `guardian-core` daemon |

Importantly: **the Auditor uses Tetragon, not wall/write.** wall/write notify; the Auditor's job is enforcement. The Auditor would only fire wall/write *secondarily* (via the audit log → guardian-core → operator notification path).

### Where each fits in selfdef's notifier chain

selfdef's notifier ships [12 outbound channels](https://github.com/cyberpunk042/selfdef/blob/main/docs/operator/channels.md) — wall and write are 2 of them, alongside ntfy, signal, slack, discord, smtp, twilio, pagerduty, loki, opensearch, thehive. The 12 channels are all *notification* mechanisms; selfdef does NOT use them for enforcement (its enforcement is via the `agent-guard` module's TracingPolicies, parallel to but separate from the notifier).

The architectural symmetry between selfdef and SAIN-01 is intentional:

- selfdef's `agent-guard` module = Tetragon enforcement (parallel to SAIN-01's Auditor)
- selfdef's notifier (wall/write/+10 others) = userspace notification (parallel to what the SAIN-01 Weaver could plug into)
- both systems can coexist on the same host running the same Tetragon daemon (with merged TracingPolicy)

The eventual Stage-2 cross-repo transposition will formalize this — selfdef's daemon running on the SAIN-01 host with cross-link between selfdef's `agent-guard` policies and SAIN-01's `sovereign-kernel-fence` policy.

### Latency comparison

Approximate event-to-effect latencies for each mechanism:

| Mechanism | Detection | Action | Notification reach |
|---|---|---|---|
| **wall(1)** | n/a (caller pre-decides) | ~5-20 ms subprocess + TTY write | 0-30s depending on operator attention |
| **write(1)** | n/a (caller pre-decides) | ~5-20 ms × N target users | 0-30s per user |
| **Tetragon SIGKILL** | ~1-10 μs (kernel hook) | **atomic with syscall** | not applicable (no notification) |
| **guardian-core post-kill cleanup** | ~1-10 ms (event-stream read) | ~10-100 ms (Podman kill + ZFS append) | n/a |
| **selfdef notifier escalation** | n/a (caller pre-decides) | ~50-500 ms (HTTP-class) per channel; 5-30 min via escalation profile rungs | seconds to minutes |

Tetragon is fundamentally faster than the userspace mechanisms because it operates in the kernel before user-space resumes. wall/write are not slow — they're milliseconds — but they're milliseconds AFTER the action has happened. For prevention, Tetragon's microsecond-class is the only path.

### When each is the right pick

| Situation | Best fit |
|---|---|
| Unauthorized `execve` attempt in a container needs to be stopped | **Tetragon** (only mechanism that prevents) |
| Operator at TTY, severity-critical event, want fastest userspace notification | **wall(1)** (broadcast — reaches all logged-in TTYs) |
| Operator allowlist exists, want to notify only specific users | **write(1)** (per-user; respects allowlist) |
| Need audit-log trail of kernel-killed events | **guardian-core** + Tetragon (kernel kill + ZFS append) |
| Operator may be off-host (phone, SMS, email) | **selfdef notifier** (12 channels including SMS via Twilio, push via ntfy, etc.) |
| Need defense-in-depth (prevent + notify + escalate + log) | **All five mechanisms layered** (Tetragon + guardian-core + wall + write + selfdef notifier) |
| Wall is too loud; want filtered notification only to specific users | **write(1)** + operator-allowlist (don't use wall + filtering — wall has no filtering) |
| Kernel module / policy authoring complexity not available | **wall(1) + write(1) + selfdef notifier** (no kernel-side requirements; userspace-only acceptable for non-prevention use cases) |

## Recommendation

> [!success] Layer them; don't pick one
>
> | Your perimeter need | Mechanism(s) |
> |---|---|
> | **Prevent unauthorized action** | Tetragon (mandatory; only mechanism that prevents) |
> | Surface kernel kill to operator at TTY | wall(1) for broadcast, write(1) for per-user — pick by audience scope |
> | Surface kernel kill to operator off-host | selfdef notifier chain — Twilio SMS, ntfy push, PagerDuty, etc. |
> | Audit trail of kills | guardian-core → ZFS `tank/context/security_audit.log` |
> | Container cleanup post-kill | guardian-core → `podman kill` |
> | Coordinate enforcement across SAIN-01 + selfdef | Single Tetragon daemon; merged TracingPolicy authored jointly |
> | Lower-severity events not worth wall/write | selfdef notifier with `severity_floor` per channel |

> [!warning] Common anti-patterns
>
> - **Picking wall/write as the perimeter.** They're notifications, not enforcement. An unauthorized action still happens; the operator just learns about it after.
> - **Picking Tetragon without notification.** The kill happens silently; the operator doesn't know an attempt happened. Audit log helps post-hoc but human-attention paths are needed in real time.
> - **Using wall when you wanted write.** wall is broadcast; if you wanted "notify only operator account", write is the right choice. The `[notifier.wall].users` filter intentionally does not exist; trying to invent it is wrong.
> - **Using two enforcement mechanisms.** SAIN-01's `sovereign-kernel-fence` TracingPolicy + selfdef's `agent-guard` TracingPolicy can both fire on the same `sys_execve` if not coordinated. Co-design the policy authority or merge into one policy.
> - **Treating guardian-core as a third notification channel.** It's a bridge layer, not a parallel channel. It augments Tetragon with userspace cleanup + ZFS append; it doesn't replace wall/write/notifier.

## Relationships

- COMPARES TO: Tetragon eBPF kernel enforcement framework
- BUILDS ON: [[concept-srp-trinity-pulse-weaver-auditor|SRP Trinity concept]] (Auditor module = Tetragon substrate)
- BUILDS ON: [[concept-vfio-gpu-isolation-amd-iommu|VFIO GPU Isolation]] (kernel-space isolation pattern; Tetragon enforces inside the VFIO-sandboxed container)
- COMPLEMENTS: [[cmp-bitnet-vs-fp16-execution-cost|BitNet vs FP16]] (orthogonal — execution-cost choice; this is perimeter choice)
- USED BY: [[src-sain-01-sovereign-node-spec|SAIN-01 Sovereign Node Spec]] (Auditor = Tetragon; Weaver could fire wall/write)

## Backlinks

[[Tetragon eBPF kernel enforcement framework]]
[[SRP Trinity concept]]
[[VFIO GPU Isolation]]
[[BitNet vs FP16]]
[[SAIN-01 Sovereign Node Spec]]
