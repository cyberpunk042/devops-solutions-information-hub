---
title: SRP Trinity — Pulse, Weaver, Auditor
aliases:
  - "SRP Trinity — Pulse, Weaver, Auditor"
  - "The Sovereign Trinity"
  - "Pulse Weaver Auditor"
  - "SAIN-01 Trinity"
  - "SRP Hardware Mapping"
type: concept
layer: 2
maturity: growing
domain: ai-agents
status: synthesized
confidence: high
created: 2026-05-15
updated: 2026-05-15
sources:
  - id: src-sain-01-sovereign-node-spec
    type: wiki
    file: "wiki/sources/src-sain-01-sovereign-node-spec.md"
    title: "Synthesis — SAIN-01 Sovereign AI Node Master Specification"
  - id: src-zen5-avx512-single-cycle
    type: wiki
    file: "wiki/sources/src-zen5-avx512-single-cycle.md"
    title: "Synthesis — AMD Zen 5 Single-Cycle 512-bit AVX-512 and Dual-CCD Topology"
  - id: src-bitnet-b158-ternary-llm
    type: wiki
    file: "wiki/sources/src-bitnet-b158-ternary-llm.md"
    title: "Synthesis — BitNet b1.58 Ternary LLM Family and bitnet.cpp Inference"
tags:
  - ai-agents
  - srp
  - single-responsibility-principle
  - hardware-mapping
  - sain-01
  - pulse
  - weaver
  - auditor
  - trinity
  - sovereign-node
  - vector-core
  - sandboxed-fabric
  - immutable-gatekeeper
  - tetragon
  - ebpf
  - zfs
  - vfio
---

# SRP Trinity — Pulse, Weaver, Auditor

## Summary

The **SRP Trinity** is the founding software architecture of the [[src-sain-01-sovereign-node-spec|SAIN-01 Sovereign Node]] — three decoupled modules conceived **before** the hardware was specified, each owning exactly one operational domain, each later mapped to a specific physical hardware boundary. **The Pulse** is the low-level vector core (MASM + Wasm primitives → AVX-512 + `bitnet.cpp` ternary inference, pinned to CCD 0). **The Weaver** is the sandboxed orchestration fabric (Wasm-isolated sub-agents → Rootless Podman + state-fabric writes on `tank/context`, pinned to CCD 1). **The Auditor** is the immutable kernel-level gatekeeper (eBPF + ZFS audit log → Tetragon `TracingPolicy` + `guardian-core` Python supervisor, kernel-space SIGKILL). This concept matters because the SAIN-01 hardware choices — Ryzen 9 9900X (single-cycle 512-bit AVX-512 + dual-CCD), dual NVIDIA GPU asymmetry (Blackwell host + 3090 VFIO sandbox), ZFS dataset stratification (`tank/models` / `tank/context` / `tank/agents`), Tetragon eBPF — are *physical instantiations* of this prior software design. The architecture is not "fast hardware seeking a use case"; it is "software responsibilities seeking the right physical substrate." Understanding the Trinity is the precondition for evaluating which SAIN-01 design points are load-bearing vs negotiable.

## Key Insights

- **The Trinity predates the hardware.** From the operator's prior conversation captured in the L0 dump's Block 6 (`raw/dumps/2026-05-15-sain-01-master-spec-other-conversation-transposition.md`): *"Before we discussed motherboard lanes, dual-GPU bifurcation, or specific kernel flags, this ecosystem was conceived as a pure, decoupled software trinity."* The 9900X selection, the Blackwell-3090 pairing, the ZFS dataset profiles, and the Tetragon perimeter are downstream — they exist *because* the Trinity required a substrate that supported each module's responsibilities cleanly. ([[src-sain-01-sovereign-node-spec|SAIN-01 synthesis]])

- **Each module owns exactly one responsibility.** Single Responsibility Principle (SRP) at the system level, not just the function level. The Pulse: bit-plane transposition + vector matrix math. The Weaver: stateful agent orchestration + decoupled execution paths. The Auditor: integrity gating + immutable audit logging. Crossing the responsibility boundary between modules is an architectural smell — e.g., if state-routing logic creeps into the Auditor, the Auditor is no longer purely an integrity gate. ([[src-sain-01-sovereign-node-spec|SAIN-01 synthesis]])

- **The Pulse maps to CCD 0 + AVX-512 + bitnet.cpp.** The "Pulse Core" is pinned to cores 0-5 of the [[concept-dual-ccd-cache-partitioning-9900x|9900X's CCD 0]] (thread mask `0xfff`). Runtime: natively-compiled [[concept-1bit-ternary-weights|ternary models]] executing via `bitnet.cpp` on the single-cycle 512-bit AVX-512 datapath, with VPDPBUSD-accelerated lookup-table matmul. The justification is latency-driven: state routing requires instantaneous branching for small context blocks, which the CPU's lower scheduling overhead delivers better than GPU context-switching. ([[src-sain-01-sovereign-node-spec|SAIN-01 synthesis]], [[src-zen5-avx512-single-cycle|Zen 5 synthesis]])

- **The Weaver maps to CCD 1 + Rootless Podman + the state fabric.** The "Weaver" handles the state engine (`CLAUDE.md`, `SOUL.md`, `IDENTITY.md`, `AGENTS.md` on `tank/context` with `sync=always`), parses gRPC streams from Tetragon, and routes I/O between sub-agents. It's pinned to cores 6-9 of CCD 1 (thread mask `0xff000`). The substrate maps the Wasm-sandbox concept onto **Rootless Podman containers** + the [[concept-vfio-gpu-isolation-amd-iommu|VFIO-isolated RTX 3090]] for sandboxed agent fleets. ([[src-sain-01-sovereign-node-spec|SAIN-01 synthesis]])

- **The Auditor maps to kernel-level Tetragon + `guardian-core`.** The Auditor is the most architecturally pure of the three — it has the smallest user-space surface, runs primarily in kernel space via Tetragon's eBPF policies, and uses a tiny Python daemon (`guardian-core`) only to catch SIGKILL events and append to the ZFS audit log at `tank/context/security_audit.log`. The integrity contract: any containerized agent attempting an unauthorized `sys_execve` is killed by the kernel before user-space sees it. ([[src-sain-01-sovereign-node-spec|SAIN-01 synthesis]])

- **The CCD partition is the physical realization of the software SRP boundary.** The 9900X is 2× CCDs of 6 cores each, each with 32MB local L3, separated by AMD Infinity Fabric. Cross-CCD memory access incurs an Infinity-Fabric round-trip — ~80-120ns vs ~10-15ns for local L3 hits. Pinning related work to a single CCD avoids the fabric tax. The SRP partition (Pulse on CCD 0, Weaver+Auditor on CCD 1, kernel on cores 10-11) makes this physical: each module's hot data stays cache-resident in its local L3. ([[concept-dual-ccd-cache-partitioning-9900x|Dual-CCD synthesis]])

- **Storage stratification reflects per-module access patterns.** Three ZFS datasets, each shaped by its module's workload: `tank/models` (1M recordsize + lz4) for the Oracle/Logic Engine's 100GB+ weight files; `tank/context` (16k recordsize + zstd-9 + `copies=2` + **`sync=always`**) for the Weaver's state fabric where atomic transitions matter; `tank/agents` (128k + zstd-3) for the agents' runtime cache. The `sync=always` on `tank/context` is the load-bearing choice — it's what makes inter-agent state handoffs race-free. ([[concept-zfs-tiered-storage-llm-inference|ZFS tiered storage synthesis]])

- **The Auditor is the direct ancestor of the legacy `SecureToast.ps1`.** The operator's pre-Sovereign-OS toolkit included a Windows-side PowerShell circuit breaker for security events. The Auditor purged the Windows dependency entirely — moving from user-space PowerShell to kernel-space eBPF, from polling-based monitoring to event-driven streaming on `/var/run/tetragon/tetragon.events`. The transition is architectural improvement, not just porting. ([[src-sain-01-sovereign-node-spec|SAIN-01 synthesis]])

> [!success] Software-First, Hardware-Second
> The Trinity is the SAIN-01 design's keystone. It establishes that the hardware exists to serve the software architecture, not the other way around. The 9900X is the only consumer chip with single-cycle 512-bit AVX-512 that satisfies the Pulse's vector pipeline requirements. The dual-GPU layout is a sandbox boundary, not a VRAM count. The ZFS datasets are per-tier access patterns, not generic fast storage. Treat the Trinity as the immutable axiom from which to evaluate any future SAIN-01 design changes.

## Deep Analysis

### The genesis — software trinity, predating hardware

The L0 dump's Block 6 establishes the timeline explicitly. The operator's prior conversation had already specified three SRP-decoupled modules before any motherboard or CPU was selected:

- **The Pulse:** low-level, high-performance assembly kernel using MASM + WebAssembly primitives. Sole responsibility: bit-plane transposition + accelerating low-bit mathematical matrices directly on bare iron, completely bypassing heavy runtime environments. The original conception is hardware-agnostic — what mattered was that the substrate had to support packed-bit SIMD execution.

- **The Weaver:** lightweight orchestration engine. Used structured Wasm-based sandboxing to dynamically isolate and weave together multiple agent execution contexts — avoiding the bloat of bare-metal VMs or full OS images per sub-agent.

- **The Auditor:** security, logging, and validation framework. Single responsibility: ensure no executing agent could deviate from the system manifest's rules. Operated as automated, immediate circuit breaker against code regressions or unauthorized execution escapes.

When the hardware procurement decision came, **each module shaped one hardware choice**:

```
SOFTWARE GENESIS                            HARDWARE INSTANTIATION
────────────────                            ──────────────────────

The Pulse (low-bit vector kernel)    →      Ryzen 9 9900X (single-cycle 512-bit AVX-512)
                                            + bitnet.cpp + AOT-compiled Wasm via Cranelift
                                            + CCD 0 pinning (cores 0-5)

The Weaver (Wasm-sandboxed             →    Rootless Podman + VFIO-isolated RTX 3090
            orchestration)                  + ZFS tank/context sync=always
                                            + CCD 1 pinning (cores 6-9)

The Auditor (immutable gatekeeper)   →      Kernel-level eBPF (Tetragon TracingPolicy)
                                            + guardian-core Python daemon
                                            + tank/context/security_audit.log atomic append
```

The instantiation is unfaked — each hardware choice exists because a module needed exactly that property:

- **9900X over 9950X**: not a price/perf choice — the SRP partition needs 12 cores split 6/4/2 across CCDs; the 9950X's extra cores don't reshape the partition.
- **Blackwell + 3090 asymmetry**: not "two GPUs for more VRAM" — the 3090's VFIO sandbox is the Weaver's isolated execution path for sub-agents, structurally distinct from the Blackwell's host-resident inference role.
- **ZFS `sync=always` on `tank/context`**: not generic durability — the Weaver's atomic-state-handoff property requires this exact knob.
- **Tetragon eBPF**: not "good security" — the Auditor's responsibility as an immediate circuit breaker requires kernel-space enforcement, not user-space monitoring.

### Module-level deep dives

#### The Pulse (vector core)

**Sole responsibility:** bit-plane transposition + low-bit matrix math at maximum throughput.

**Physical location:** Cores 0-5 (CCD 0) on the Ryzen 9 9900X. Thread mask `0xfff` (24 logical threads / 12 cores per CCD × dual SMT, here 6 cores × 2 threads = 12 logical, hence `0xfff` = 12 bits).

**Runtime:** Natively-compiled [[concept-1bit-ternary-weights|ternary models]] via `bitnet.cpp` (microsoft/bitnet-b1.58-2B-4T or microsoft/bitnet_b1_58-3B as the canonical recommendations). Alternative: AOT-compiled WebAssembly via Cranelift + Wasmtime, targeting native Zen 5 machine code.

**Why CPU, not GPU:** State orchestration requires instantaneous branching and low latency for small context blocks. CPU scheduling overhead is lower than GPU context-switching for sub-millisecond decisions. Plus, the [[concept-1bit-ternary-weights|ternary CPU inference]] path is uniquely well-suited to Zen 5's single-cycle 512-bit AVX-512 + VNNI VPDPBUSD instruction.

**Interface contract:** The Pulse reads from `/mnt/vault/context/CLAUDE.md` (active session context) and `/mnt/vault/context/SOUL.md` (core behavioral logic) atomically; writes to neither directly. State mutations go through the Weaver.

#### The Weaver (sandboxed fabric)

**Sole responsibility:** Stateful agent orchestration + decoupled execution paths + atomic state transitions.

**Physical location:** Cores 6-9 (CCD 1) on the 9900X. Thread mask `0xff000` (cores 6-9 × 2 threads = 8 logical, bits 12-19, hence `0xff000`).

**Runtime:** Rootless Podman containers for sub-agents. The asymmetric load-balancing profiles (Profile 1 / 2 / 3 in the SAIN-01 spec) live here. Sub-agents that require GPU access route to the VFIO-isolated RTX 3090 (sandbox tier) or to the Blackwell (host tier).

**State fabric:** Reads + writes the four context files (`IDENTITY.md`, `SOUL.md`, `AGENTS.md`, `CLAUDE.md`) on `tank/context`. Uses atomic-rename + `O_DIRECT` + `O_SYNC` to commit state transitions before broadcasting to sub-agents via gRPC. The ZFS `sync=always` knob on the dataset guarantees the commit is on physical NVMe before the next reader observes it. ⚠️ Caveat from L1: full `O_DIRECT` support requires OpenZFS 2.2+; older ZoL silently falls back to buffered. The atomic-rename + `sync=always` combination is the robust pattern.

**Interface contract:** The Weaver is the only module that mutates the state fabric. The Pulse reads (RO); the Auditor reads (RO); the Weaver writes (atomic).

#### The Auditor (immutable gatekeeper)

**Sole responsibility:** Verify execution boundary integrity, log violations, terminate violators.

**Physical location:** Primarily kernel-space (Tetragon eBPF programs). User-space surface limited to the `guardian-core` Python daemon on the remaining cores (10-11 of CCD 1, mask `0xf00000`).

**Runtime:** Tetragon `TracingPolicy` allowlists ~4 binaries for `sys_execve` (python3, nvidia-smi, vllm, podman); any other syscall in a containerized agent triggers an immediate kernel-space `SIGKILL`. The `guardian-core` daemon listens on `/var/run/tetragon/tetragon.events`, catches kill events, kills the offending Podman container, appends to `tank/context/security_audit.log`, and optionally rings the PC speaker (audible alert for the operator at the console).

**Why kernel-space:** A user-space supervisor can be racy (between detection and intervention, the violating agent can do damage). Kernel-space enforcement happens before user-space resumes execution; the kill is atomic with the syscall attempt. This is the architectural improvement over the legacy `SecureToast.ps1` model.

**Interface contract:** The Auditor reads all four state-fabric files (RO) to know the expected agent rules. It writes only to `tank/context/security_audit.log` (append-only). It never mutates the Pulse's or Weaver's state.

### Why this is "Trinity," not "team"

The three modules are intentionally **not interchangeable** and **not redundant**. Each has a unique responsibility that's load-bearing for the system:

- **Pulse outage** → no vector math; the orchestration tier slows to GPU-context-switch speeds for every state decision.
- **Weaver outage** → no state fabric; the Pulse's reads are stale; sub-agents can't be coordinated.
- **Auditor outage** → no integrity gate; unauthorized syscalls go un-killed; the security perimeter is open.

This is structurally different from a "redundant agent team." Each module is a different system function with a unique failure mode, not three instances of the same function. The Trinity language captures the architectural commitment that all three must exist for the system to work — not just that there are three of them.

### What the Trinity does NOT include

To clarify the boundary, several functions deliberately fall outside the Trinity:

- **Inference workloads on the Blackwell** are not part of the Trinity. The "Oracle Core" (deep reasoning on the 96GB Blackwell) is a *consumer* of the Trinity's services — the Weaver routes work to it, the Auditor monitors it, the Pulse provides state context — but it isn't a Trinity module.
- **Network I/O** is not Trinity-internal. The Marvell 10GbE + Intel 2.5GbE split is infrastructure that the Trinity uses but doesn't own.
- **The "Vibe Managing Platform"** (operator-jargon for the top-level orchestration shell) is *above* the Trinity, not a fourth module — it composes the three. It may warrant its own concept page once formalized.

### The architecture's load-bearing axiom

The Trinity establishes one architectural axiom: **the hardware exists to serve the software's SRP boundaries**. Any future hardware change must be evaluated against whether it preserves or violates this mapping:

- A single-CCD CPU (no SRP partition possible) → violates.
- Single-GPU (no VFIO sandbox boundary) → violates the Weaver's isolation.
- ext4 instead of ZFS (no `sync=always` atomic state) → violates the Weaver's contract.
- User-space monitoring instead of eBPF → violates the Auditor's immediacy.

This is the lens through which any SAIN-01 hardware or OS variant is reviewed.

## Open Questions

- The "Vibe Managing Platform" terminology used in the L0 dump's Section 5 — is this a fourth module above the Trinity (composing them), or a re-naming of the Weaver's orchestration shell? Operator clarification would land this as either its own concept page or fold it into the Weaver's responsibility surface. (Requires: operator interview / future SAIN-01 epic.)
- The Pulse's runtime is described as "bitnet.cpp OR Wasm AOT via Cranelift" — but these are different runtimes with different deployment models. Is the intent to run *both* simultaneously, or to pick one based on workload? The dual-runtime case adds operational complexity. (Requires: runtime-selection decision; would land as an L6 decision page.)
- Cross-Trinity state handoff timing — when the Weaver writes a state mutation, how long until the Pulse and Auditor see it? `sync=always` guarantees physical commit, but doesn't bound the read latency. (Requires: empirical measurement; may inform sub-millisecond orchestration requirements.)
- The Auditor's allowlist of ~4 binaries (python3 / nvidia-smi / vllm / podman) — is this list final, or expected to grow? Each addition is a security surface increase. (Requires: scope discipline + per-binary justification.)
- Composition with the existing `cyberpunk042/selfdef` daemon's `agent-guard` module — both use Tetragon TracingPolicies. Coexistence requires a shared policy authority; conflict would manifest as either redundant kills or missed enforcement. (Requires: Stage-2 cross-repo integration design.)

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **The Pulse's runtime** | [[concept-1bit-ternary-weights\|1-bit Ternary Weights]] |
> | **The Pulse's hardware substrate** | [[concept-dual-ccd-cache-partitioning-9900x\|Dual-CCD Cache Partitioning]] |
> | **The Weaver's isolation substrate** | [[concept-vfio-gpu-isolation-amd-iommu\|VFIO GPU Isolation]] |
> | **The Weaver's state-fabric substrate** | [[concept-zfs-tiered-storage-llm-inference\|ZFS Tiered Storage]] |
> | **GPU acceleration for Logic/Oracle tiers** | [[concept-speculative-decoding-block-diffusion\|Speculative Decoding via Block Diffusion]] |
> | **Source synthesis (genesis story)** | [[src-sain-01-sovereign-node-spec\|SAIN-01 Sovereign Node Spec]] |

## Relationships

- DERIVED FROM: [[src-sain-01-sovereign-node-spec|SAIN-01 Sovereign Node Spec]] (Block 6 "The Genesis: Trinity Framework")
- ENABLED BY: [[concept-dual-ccd-cache-partitioning-9900x|Dual-CCD Cache Partitioning]]
- ENABLED BY: [[concept-vfio-gpu-isolation-amd-iommu|VFIO GPU Isolation]]
- ENABLED BY: [[concept-zfs-tiered-storage-llm-inference|ZFS Tiered Storage for LLM Inference]]
- RELATES TO: [[concept-1bit-ternary-weights|1-bit Ternary Weights]] (the Pulse's runtime)
- RELATES TO: [[concept-speculative-decoding-block-diffusion|Speculative Decoding via Block Diffusion]] (deployed by the Weaver on the Logic Engine + Oracle Core tiers)

## Backlinks

[[SAIN-01 Sovereign Node Spec]]
[[Dual-CCD Cache Partitioning]]
[[VFIO GPU Isolation]]
[[concept-zfs-tiered-storage-llm-inference|ZFS Tiered Storage for LLM Inference]]
[[concept-1bit-ternary-weights|1-bit Ternary Weights]]
[[concept-speculative-decoding-block-diffusion|Speculative Decoding via Block Diffusion]]
