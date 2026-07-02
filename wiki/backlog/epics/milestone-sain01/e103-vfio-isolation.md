---
title: E103 — VFIO Isolation
aliases:
  - "E103 — VFIO Isolation"
  - "E103 — VFIO Isolation: RTX 4090 Sandbox + AMD IOMMU"
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
  - id: concept-vfio-gpu-isolation-amd-iommu
    type: wiki
    file: "wiki/domains/devops/concept-vfio-gpu-isolation-amd-iommu.md"
tags: [epic, sain-01, vfio, iommu, amd-iommu, gpu-isolation, rtx-4090, blackwell, sandbox, podman]
---

# E103 — VFIO Isolation

## Summary

Configure **VFIO passthrough of the RTX 4090** at boot via GRUB kernel parameters, so the secondary GPU is **invisible to the host** and reserved as the [[concept-srp-trinity-pulse-weaver-auditor|Weaver]]'s sandbox substrate. The Blackwell stays host-resident under the NVIDIA driver for the Oracle Core's primary inference. The mechanism: GRUB parameters `amd_iommu=on iommu=pt vfio-pci.ids=10de:2204,10de:1ad8` bind `vfio-pci` to the 4090 (GPU `10de:2204` + audio companion `10de:1ad8`) at boot, before `nvidia.ko` enumerates devices. Verifies clean IOMMU group separation (Blackwell + 4090 in distinct groups; confirmed at E100). The end-state is that sandboxed Podman containers can attach to the 4090 via `--device /dev/vfio/<group_id>` while the host's `nvidia-smi` reports only the Blackwell. The L1/L2 grounding (see [[concept-vfio-gpu-isolation-amd-iommu|VFIO GPU isolation concept]]) covers the IOMMU-group-must-separate constraint, the MOK-signing interaction with Secure Boot, and the "all-or-nothing device binding" reality.

## Operator Directive

> "the 24GB 4090 (VFIO Sandbox)"

> "The RTX 4090 is bound to vfio-pci at boot, rendering it invisible to the host OS and reserved exclusively for the sandboxed agent fleet."

## Goals

See Done When criteria — verifiable kernel-isolation checkpoints.

## Done When

- [ ] **GRUB updated** with `GRUB_CMDLINE_LINUX_DEFAULT="quiet splash amd_iommu=on iommu=pt kvm_amd.npt=1 kvm_amd.avic=1 vfio-pci.ids=10de:2204,10de:1ad8 nvidia-drm.modeset=1 nvidia.NVreg_EnableGpuFirmware=1"`; `update-grub` succeeds
- [ ] **Reboot succeeds** under MOK-signed kernel (Secure Boot does not reject the kernel image)
- [ ] **`lspci -k`** shows: PCIEX16_2 device (the 4090) bound to `vfio-pci`; PCIEX16_2 audio companion also bound to `vfio-pci`; PCIEX16_1 device (the Blackwell) bound to `nvidia.ko`
- [ ] **`nvidia-smi`** reports ONE GPU (the Blackwell). The 4090 is invisible to the host.
- [ ] **`find /sys/kernel/iommu_groups/ -type l | sort`** confirms: Blackwell GPU + audio in one IOMMU group; 4090 GPU + audio in a separate IOMMU group; no other devices share these groups
- [ ] **`dmesg | grep -i iommu`** shows AMD IOMMU initialization at boot; pass-through mode (`iommu=pt`) engaged
- [ ] **`/dev/vfio/<group_id>`** exists for the 4090's IOMMU group; permissions allow the sovereign user's container runtime
- [ ] **Test container** with `podman run --device /dev/vfio/<group_id> --device-cgroup-rule='c 195:* rmw' nvidia/cuda:12.6.0-runtime-ubuntu22.04 nvidia-smi` successfully sees the 4090 inside the container
- [ ] **Host integrity check**: `nvidia-smi` still reports only the Blackwell after the test container exits — the 4090 stays bound to `vfio-pci`
- [ ] **PCI device IDs verified**: confirm `lspci -nn -s <bdf>` returns the GPU's real id via `lspci -nn` — the `10de:2204`/GA102 value here is the earlier RTX 3090 assumption; the RTX 4090 is AD102 (typically `10de:2684`). Update the GRUB `vfio-pci.ids` line to the actual 4090 GPU + audio ids
- [ ] **BIOS revision pinned** (already from E100); if the operator updates BIOS later, re-verify IOMMU group composition (firmware can shift groups)

## Scale and Model

> [!info] Epic Parameters
>
> | Parameter | Value |
> |---|---|
> | **Model** | integration |
> | **Quality tier** | Skyscraper |
> | **Estimated tasks** | 4-6 |
> | **Dependencies** | E100 (hardware + IOMMU groups verified), E101 (kernel with AMD IOMMU + VFIO support) |
> | **Feeds into** | E104 (Tetragon perimeter applies to sandboxed containers), E107 (Weaver routes sub-agents to the sandbox), E108 (Profile 2 + 3 use the 4090), E109 (DFlash deploys on the sandbox), E110 (model catalog can run on either GPU) |
> | **Critical** | All-or-nothing — once bound to vfio-pci, the 4090 cannot be reclaimed by the host without rebooting. Operator-confirmed irreversibility within a session. |

## Handoff Context

> [!info] For a fresh context picking up this epic:
>
> - Milestone: [[sain-01-sovereign-node|Milestone — SAIN-01 Sovereign AI Node]]
> - VFIO concept (mechanism + IOMMU-group rationale): [[concept-vfio-gpu-isolation-amd-iommu|VFIO GPU Isolation with AMD IOMMU]]
> - L1 spec section: [[src-sain-01-sovereign-node-spec|§ 4.3 VFIO Subsystem Isolation]]
> - **The PCI device ids `10de:2204` (GA102) + `10de:1ad8` were the earlier RTX 3090 (Ampere) values** — the actual card is an RTX 4090 (AD102, GPU id typically `10de:2684`); re-derive both from `lspci -nn` on the installed 4090. Both go in the same `vfio-pci.ids=` argument because they're in the same IOMMU group.
> - **The M.2_2-must-be-empty rule** (from E100) is what guarantees the IOMMU group separation works. If a later operator decides to populate M.2_2, this epic's outcome breaks.

## Relationships

- PART OF: [[sain-01-sovereign-node|Milestone — SAIN-01 Sovereign AI Node]]
- DEPENDS ON: [[e100-hardware-foundation|E100 — Hardware Foundation]]
- DEPENDS ON: [[e101-sovereign-os-build|E101 — Sovereign OS Build]]
- ENABLES: [[e104-tetragon-guardian-perimeter|E104 — Tetragon + Guardian Perimeter]]
- ENABLES: [[e107-weaver-state-fabric|E107 — Weaver State Fabric]]
- ENABLES: [[e108-load-balancing-profiles|E108 — Load-Balancing Profiles]]
- ENABLES: [[e109-dflash-integration|E109 — DFlash Integration]]
- ENABLES: [[e110-model-catalog|E110 — Model Catalog]]
- IMPLEMENTS: [[concept-vfio-gpu-isolation-amd-iommu|Concept — VFIO GPU Isolation with AMD IOMMU]]
- IMPLEMENTS: [[src-sain-01-sovereign-node-spec|SAIN-01 Sovereign Node Spec]] § 4.3

## Backlinks

[[sain-01-sovereign-node|Milestone — SAIN-01 Sovereign AI Node]]
[[e100-hardware-foundation|E100 — Hardware Foundation]]
[[e101-sovereign-os-build|E101 — Sovereign OS Build]]
[[e104-tetragon-guardian-perimeter|E104 — Tetragon + Guardian Perimeter]]
[[e107-weaver-state-fabric|E107 — Weaver State Fabric]]
[[e108-load-balancing-profiles|E108 — Load-Balancing Profiles]]
[[e109-dflash-integration|E109 — DFlash Integration]]
[[e110-model-catalog|E110 — Model Catalog]]
[[Concept — VFIO GPU Isolation with AMD IOMMU]]
[[SAIN-01 Sovereign Node Spec]]
