---
title: Milestone — SAIN-01 Sovereign AI Node
aliases:
  - "Milestone — SAIN-01 Sovereign AI Node"
  - "Milestone: SAIN-01 Sovereign AI Node"
  - "SAIN-01 Milestone"
type: milestone
domain: backlog
status: draft
priority: P0
target_date: 2026-Q3
readiness: 15
progress: 0
epics:
  - "E100"
  - "E101"
  - "E102"
  - "E103"
  - "E104"
  - "E105"
  - "E106"
  - "E107"
  - "E108"
  - "E109"
  - "E110"
acceptance_criteria:
  - "Friction-audit passes at boot — x8/x8 GPU lanes verified, M.2_2 empty, IOMMU groups separated"
  - "Custom Zen-5-tuned kernel 6.12+ deployed via bindeb-pkg, MOK-signed for Secure Boot"
  - "ZFS pool with three datasets (tank/models, tank/context with sync=always, tank/agents) operational"
  - "RTX 4090 bound to vfio-pci at boot; Blackwell host-resident via nvidia driver"
  - "Tetragon eBPF TracingPolicy loaded; guardian-core daemon listening on Tetragon socket"
  - "Network split active — Intel 2.5GbE on VLAN 100 (mgmt), Marvell 10GbE on VLAN 200 (data, MTU 9000)"
  - "Pulse module runs bitnet.cpp ternary inference pinned to CCD 0 at 5+ tok/sec"
  - "Weaver atomic-state-write pattern verified — race-free inter-agent state handoff on tank/context"
  - "Three load-balancing profiles (Ultra-Sovereign / Asymmetric-Burst / Deep-Context-Synthesis) deployable via runtime selection"
  - "DFlash block-diffusion speculative decoding integrated for code/math workloads on Blackwell + RTX 4090"
  - "Model catalog deployed — at least one of {Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16, Ling-2.6-flash} resident on Blackwell"
  - "All 11 epics meet their Done When criteria"
  - "Operator confirms node reaches sovereign-deployment-ready state"
confidence: high
created: 2026-05-16
updated: 2026-05-16
sources:
  - id: src-sain-01-sovereign-node-spec
    type: wiki
    file: "wiki/sources/src-sain-01-sovereign-node-spec.md"
    title: "Synthesis — SAIN-01 Sovereign AI Node Master Specification"
  - id: l0-dump
    type: file
    file: "raw/dumps/2026-05-15-sain-01-master-spec-other-conversation-transposition.md"
  - id: operator-directive
    type: directive
    file: "raw/notes/2026-05-15-user-directive-sain01-info-hub-ingestion.md"
  - id: concept-srp-trinity
    type: wiki
    file: "wiki/domains/ai-agents/concept-srp-trinity-pulse-weaver-auditor.md"
tags: [milestone, sain-01, sovereign-os, hardware, kernel, zfs, vfio, tetragon, bitnet, dflash, avx512, zen5, model-catalog]
---

# Milestone — SAIN-01 Sovereign AI Node

## Summary

Transition from operator's planning artifacts to a fully deployable **Sovereign AI Node (SAIN-01)** — a bare-metal AMD Zen 5 + dual-NVIDIA workstation running a custom-tuned Debian 13 (Trixie) host with ZFS-stratified storage, VFIO-isolated dual GPUs, kernel-level Tetragon eBPF perimeter, and a software architecture realizing the [[concept-srp-trinity-pulse-weaver-auditor|SRP Trinity]] (Pulse / Weaver / Auditor). This milestone covers eleven epics across hardware, OS build, storage, isolation, network, runtime, state-fabric, profiles, acceleration, and model catalog. Each epic owns one operational domain. The deliverable is a node that survives the `friction-audit` script at boot and runs the Conductor / Logic Engine / Oracle Core tiers on the right hardware substrate per the L1-L3 layers of the wiki. This is **not** a research deliverable; it is a build specification that another agent or operator session can execute end-to-end.

## Operator Directive

> "I am now going to give you information from another conversation about our future and 1-bit models. lets start with the start though, I will dumb all this. Its important data but keep in mind its AI and contain piece of hallucination and clear ignorance of this context but at the same time there are reality and important points like the future custom OS and the new build / hardware of this machine and then later other things and 1-bit notion and 512bit advantages and ideas"

> "I just pushed the latest information-hub, we can do the ingestion through it and follow the proper workflow and when we are ready we will transpose into the selfdef and the new Development and Epics and Modules and Tasks needed to get there and all the Spec files and requirements and clear vision."

> "I would like large specs and requirements markdown artifact. high standards. lets synthesize all this properly."

> "DO not minimize, do not reduze, do not conflate, do not hack or try to take shortcuts. we do this right all the way"

## Delivery Target

> [!info] Milestone Parameters
>
> | Parameter | Value |
> |-----------|-------|
> | **Target date** | 2026-Q3 (tentative — operator confirms based on hardware procurement + assembly cadence) |
> | **Phase** | Bootstrap → Production |
> | **Chain** | Default (stage-gated with selected artifacts; each epic runs its own document → design → scaffold → implement → test cycle) |
> | **Total epics** | 11 |
> | **Estimated total tasks** | 60-90 (5-10 per epic) |
> | **Hardware status** | Specified (verified via L1 syntheses); procurement gated on operator action |
> | **Software readiness** | Custom kernel, ZFS layout, Tetragon policy, Trinity modules all designed at L1-L3; impl pending |

## Epic Composition

> [!abstract] 11 Epics — Each Is One Operational Domain (SRP)
>
> | Epic | Focus | What It Delivers | Dependencies |
> |------|-------|------------------|--------------|
> | **E100: Hardware Foundation** | Iron procurement + physical assembly + PCIe topology verification | 9900X / ProArt X870E / Blackwell 96GB / 4090 24GB / 256GB DDR5 / 2× PCIe 5 NVMe / Marvell 10GbE + Intel 2.5GbE assembled and `friction-audit`-clean | None — entry point |
> | **E101: Sovereign OS Build** | Custom Zen-5-tuned kernel 6.12+ + Debian 13 live-build + MOK signing for Secure Boot | Bootable Sovereign OS `.iso` with `-march=znver5` kernel, identity-injected motd + os-release, ZFS-DKMS + NVIDIA 560+ drivers | E100 |
> | **E102: ZFS Storage Layout** | Three-dataset stratification on RAID 0 NVMe + ARC tuning | `tank/models` (1M lz4) + `tank/context` (16k zstd-9 copies=2 sync=always) + `tank/agents` (128k zstd-3); ARC clamped to 128GB | E101 |
> | **E103: VFIO Isolation** | RTX 4090 → `vfio-pci` at boot; Blackwell stays host-resident; IOMMU groups verified clean | GRUB `vfio-pci.ids=10de:2204,10de:1ad8` + AMD IOMMU pass-through; host's `nvidia-smi` shows 1 GPU only | E101 |
> | **E104: Tetragon + Guardian Perimeter** | eBPF TracingPolicy + `guardian-core` Python daemon + ZFS audit log | Kernel-space SIGKILL on unauthorized `sys_execve`; userspace post-kill cleanup + atomic audit append | E102 (audit log on tank/context), E103 (containers in VFIO sandbox) |
> | **E105: Network Segregation** | Dual-NIC physical split + VLAN 100/200 routing + jumbo frames on 10GbE | Intel 2.5GbE → mgmt; Marvell 10GbE → data (MTU 9000, no default GW); OPNsense-compatible | E101 |
> | **E106: Pulse Vector Runtime** | bitnet.cpp ternary inference + AOT Wasm compilation pinned to CCD 0 | Pulse module runs `microsoft/bitnet-b1.58-2B-4T` (or 3B) on cores 0-5, achieves ≥5 tok/sec on operator workload | E101, E102 (model weights on tank/models) |
> | **E107: Weaver State Fabric** | Atomic-state-write pattern + four context files + gRPC sub-agent routing | Race-free state transitions on `IDENTITY.md` / `SOUL.md` / `AGENTS.md` / `CLAUDE.md`; Podman sub-agents reach Weaver via gRPC | E102 (sync=always context), E104 (Auditor watches Weaver writes) |
> | **E108: Load-Balancing Profiles** | Three runtime profiles (Ultra-Sovereign Efficiency / Asymmetric-Burst / Deep-Context-Synthesis) | Profile YAML + orchestration switches; operator picks per workload | E106, E107, E103 |
> | **E109: DFlash Integration** | Block-diffusion speculative decoding deployed for code/math workloads on Blackwell + 4090 | vLLM v0.20.1+ with DFlash drafts for resident model; verified 3×+ speedup on code/math benchmarks | E103 (Blackwell + 4090 ready), E108 (profile selection) |
> | **E110: Model Catalog** | Resident-deploy at least one of {Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16, Ling-2.6-flash} on Blackwell | Model weights on `tank/models`; vLLM serves the model; quantization + runtime profile match the model's fit | E102, E108 (profile picks the model) |

## Epic Dependency Graph

```
E100 (Hardware) ──────────────────────────────────────────────────┐
    │                                                             │
    ▼                                                             │
E101 (Sovereign OS) ──┬──→ E102 (ZFS)                            │
                      │       │                                   │
                      │       ├──→ E104 (Tetragon + Guardian) ──┐ │
                      │       │       ▲                         │ │
                      │       │       │                         │ │
                      │       └──→ E107 (Weaver State Fabric) ──┤ │
                      │                                          │ │
                      ├──→ E103 (VFIO) ──┬──→ E109 (DFlash)     │ │
                      │                  │                       │ │
                      ├──→ E105 (Network)│                       │ │
                      │                  │                       │ │
                      └──→ E106 (Pulse)  │                       │ │
                              │          │                       │ │
                              └──────────┴──→ E108 (Profiles)   │ │
                                                  │             │ │
                                                  ▼             │ │
                                              E110 (Model Catalog)│
                                                                  │
            All converge on the milestone Acceptance Criteria ────┘
```

**Critical path**: E100 → E101 → E102 → E104 (kernel-level perimeter) AND E101 → E103 → E108 → E110 (model catalog deployment).

**Parallel tracks after E101**:
- Track A: E102 → E104 (storage + perimeter)
- Track B: E103 → E109 (GPU isolation + acceleration)
- Track C: E105 (network split — independent once OS is up)
- Track D: E106 (Pulse — can run concurrently once ZFS is up for model weights)
- Track E: E107 → E108 → E110 (state fabric + profiles + models — final assembly)

## Acceptance Criteria

- [ ] **Hardware**: `friction-audit` script returns 0 — x8/x8 GPU lanes verified, M.2_2 confirmed empty, IOMMU groups cleanly separated (Blackwell + 4090 in distinct groups)
- [ ] **OS Build**: Sovereign OS `.iso` boots; identity in `/etc/os-release` matches `ID=sovereign`; motd contains the operator's stated text; kernel compiled with `-march=znver5` (`uname -r` includes `znver5` suffix); ZFS-DKMS + NVIDIA modules load cleanly under MOK-signed kernel
- [ ] **Storage**: `zpool status tank` shows healthy; three datasets present with correct `recordsize` + `compression` + `sync` + `copies` properties; `arcstat -s c` shows ARC clamped to 128GB
- [ ] **Isolation**: `lspci -k` shows RTX 4090 + audio bound to `vfio-pci`; `nvidia-smi` reports only the Blackwell; container with `--device /dev/vfio/<group>` successfully attaches to the 4090
- [ ] **Perimeter**: Tetragon daemon active; `TracingPolicy` loaded; test attempt of unauthorized `sys_execve` (e.g., `/bin/sh` inside a container) produces immediate `SIGKILL` + log entry in `tank/context/security_audit.log`
- [ ] **Network**: `ip link show enp5s0` reports MTU 9000; `ip route` shows no default gateway on the Marvell interface; management traffic isolated to Intel 2.5GbE
- [ ] **Pulse Runtime**: `taskset -c 0-5 bitnet-cli ...` runs successfully on a real model; throughput measured at ≥5 tokens/sec on operator workload representative
- [ ] **Weaver Atomicity**: Inter-agent state-handoff test produces no race conditions (write to `CLAUDE.md`, immediate read by another agent, content matches)
- [ ] **Profiles**: All three runtime profiles deploy; profile switch via documented mechanism; per-profile resource allocation verified (CPU cores, GPU memory, model selection)
- [ ] **DFlash**: vLLM v0.20.1+ deployed with DFlash drafts for the resident model; HumanEval / Math500 benchmarks show ≥3× speedup vs baseline vLLM
- [ ] **Model Catalog**: At least one of {Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16 at BF16, Ling-2.6-flash via Q4 or MoE-active-only} resident on Blackwell + serving requests via the Weaver's routing
- [ ] **All 11 epics**: each epic's "Done When" checklist 100% green; operator review approves
- [ ] **Pipeline post**: `python3 -m tools.pipeline post` returns 0 errors against the new milestone + 11 epics

## Dependencies

- **Hardware procurement** — Ryzen 9 9900X + ASUS ProArt X870E-Creator + NVIDIA RTX PRO 6000 Blackwell + RTX 4090 + 256GB DDR5 + 2× PCIe 5.0 NVMe + Marvell AQC113C + Intel I226-V. Procurement gated on operator action; lead time depends on Blackwell availability + budget.
- **OpenZFS 2.2+ for proper `O_DIRECT` semantics** — older versions silently fall back to buffered; the Weaver's atomic-state-writer pattern depends on this. Pin OpenZFS ≥2.2.
- **DFlash backend** — vLLM v0.20.1+ required; older deployments need upgrade before E109 can ship.
- **DFlash drafts** — only ~20 target models have pre-trained drafts as of Q2 2026; the chosen Oracle Core model must be on the list OR the operator accepts EAGLE-3/MEDUSA fallback for E109.
- **NVIDIA license review** for Nemotron-3-Nano-Omni — "other" license requires per-use-case review before commercial deployment (personal sovereign use almost certainly fine; verify).
- **Operator time at multiple gates** — `friction-audit` verification, MOK enrollment, Tetragon policy review, profile selection, model selection.

## Impediments

| Impediment | Type | Blocked Since | Escalated? | Resolution |
|---|---|---|---|---|
| Blackwell RTX PRO 6000 availability | external | (not yet procured) | n/a | Operator-side procurement decision; lead times Q2-Q3 2026 |
| Custom kernel + Secure Boot interaction | technical | n/a (design-stage) | No | MOK enrollment documented in L1 + L2; ship procedure with epic E101 |
| OpenZFS `O_DIRECT` semantics requires 2.2+ | technical | n/a (design-stage) | No | Pin OpenZFS version in E101 + E102; verify at boot |
| DFlash per-target draft training recipe not yet public | external | n/a (Z-Lab roadmap) | No | Use pre-trained drafts for E109; defer custom training until public |
| Concurrent ASUS BIOS revisions may shift IOMMU group composition | external | n/a | No | Pin BIOS version after `friction-audit` confirms clean groups; document in E103 |

## Stage-2 Cross-Repo (Future, Operator-Gated)

After this milestone reaches acceptance, **Stage-2** is the transposition of relevant parts into `cyberpunk042/selfdef`:

- New selfdef epics for daemon-on-SAIN-01 deployment
- Selfdef `agent-guard` Tetragon policy cross-link with SAIN-01's `sovereign-kernel-fence` policy
- Selfdef escalation engine state-fabric integration (`selfdef/escalations.sqlite` resident on `tank/context` with `sync=always`)
- Selfdef notifier on SAIN-01 host (already-shipped 12 channels including wall + write — verify Tetragon allowlist accommodates `/usr/bin/wall` + `/usr/bin/write` invocations)

Stage-2 is **not** part of this milestone. This milestone delivers the host; Stage-2 makes selfdef run cleanly on it.

## Relationships

- CONTAINS: [[e100-hardware-foundation|E100 — Hardware Foundation]]
- CONTAINS: [[e101-sovereign-os-build|E101 — Sovereign OS Build]]
- CONTAINS: [[e102-zfs-storage-layout|E102 — ZFS Storage Layout]]
- CONTAINS: [[e103-vfio-isolation|E103 — VFIO Isolation]]
- CONTAINS: [[e104-tetragon-guardian-perimeter|E104 — Tetragon + Guardian Perimeter]]
- CONTAINS: [[e105-network-segregation|E105 — Network Segregation]]
- CONTAINS: [[e106-pulse-vector-runtime|E106 — Pulse Vector Runtime]]
- CONTAINS: [[e107-weaver-state-fabric|E107 — Weaver State Fabric]]
- CONTAINS: [[e108-load-balancing-profiles|E108 — Load-Balancing Profiles]]
- CONTAINS: [[e109-dflash-integration|E109 — DFlash Integration]]
- CONTAINS: [[e110-model-catalog|E110 — Model Catalog (Ling / Nemotron / etc.)]]
- IMPLEMENTS: [[src-sain-01-sovereign-node-spec|Synthesis — SAIN-01 Sovereign Node Master Spec]]
- IMPLEMENTS: [[concept-srp-trinity-pulse-weaver-auditor|Concept — SRP Trinity (Pulse, Weaver, Auditor)]]
- BUILDS ON: [[src-bitnet-b158-ternary-llm|Synthesis — BitNet b1.58 family]]
- BUILDS ON: [[src-dflash-block-diffusion-spec-dec|Synthesis — DFlash]]
- BUILDS ON: [[src-zen5-avx512-single-cycle|Synthesis — Zen 5 AVX-512]]
- DERIVED FROM: [[2026-05-15-sain-01-master-spec-other-conversation-transposition|L0 verbatim dump]]
- DERIVED FROM: [[2026-05-15-user-directive-sain01-info-hub-ingestion|Operator-directive log]]

## Backlinks

[[e100-hardware-foundation|E100 — Hardware Foundation]]
[[e101-sovereign-os-build|E101 — Sovereign OS Build]]
[[e102-zfs-storage-layout|E102 — ZFS Storage Layout]]
[[e103-vfio-isolation|E103 — VFIO Isolation]]
[[e104-tetragon-guardian-perimeter|E104 — Tetragon + Guardian Perimeter]]
[[e105-network-segregation|E105 — Network Segregation]]
[[e106-pulse-vector-runtime|E106 — Pulse Vector Runtime]]
[[e107-weaver-state-fabric|E107 — Weaver State Fabric]]
[[e108-load-balancing-profiles|E108 — Load-Balancing Profiles]]
[[e109-dflash-integration|E109 — DFlash Integration]]
[[E110 — Model Catalog (Ling / Nemotron / etc.)]]
[[Synthesis — SAIN-01 Sovereign Node Master Spec]]
[[Concept — SRP Trinity (Pulse, Weaver, Auditor)]]
[[Synthesis — BitNet b1.58 family]]
[[Synthesis — DFlash]]
[[Synthesis — Zen 5 AVX-512]]
[[L0 verbatim dump]]
[[Operator-directive log]]
[[e110-model-catalog|E110 — Model Catalog]]
