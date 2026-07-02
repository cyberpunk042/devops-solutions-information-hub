---
title: E100 — Hardware Foundation
aliases:
  - "E100 — Hardware Foundation"
  - "E100 — Hardware Foundation: Iron + PCIe + MOK"
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
  - id: src-zen5-avx512-single-cycle
    type: wiki
    file: "wiki/sources/src-zen5-avx512-single-cycle.md"
  - id: concept-dual-ccd-cache-partitioning-9900x
    type: wiki
    file: "wiki/domains/devops/concept-dual-ccd-cache-partitioning-9900x.md"
tags: [epic, sain-01, hardware, pcie, mok, secure-boot, friction-audit]
---

# E100 — Hardware Foundation

## Summary

Procure, assemble, and verify the physical hardware substrate for SAIN-01. The platform is deterministic: **AMD Ryzen 9 9900X** (12C/24T, dual-CCD, single-cycle 512-bit AVX-512), **ASUS ProArt X870E-Creator** motherboard, **NVIDIA RTX PRO 6000 Blackwell** (96 GB) + **NVIDIA RTX 4090** (24 GB) in PCIEX16_1 + PCIEX16_2 slots respectively, **256 GB DDR5** (initial 128 GB acceptable; expand later), **2× PCIe 5.0 NVMe** in M.2_1 + a *second* M.2 slot that is NOT M.2_2, **Marvell AQC113C 10GbE** + **Intel I226-V 2.5GbE** on the board. The critical platform constraint: **M.2_2 must remain unpopulated** — populating it triggers PCIe-lane bifurcation that drops PCIEX16_2 to x4, destroying the x8/x8 GPU symmetry the rest of the milestone depends on. This epic ends when the `friction-audit` script (delivered by E101) passes at boot: x8/x8 lane symmetry verified, IOMMU groups clean (Blackwell + 4090 in distinct groups), `cppc` preferred-CCD identified, MOK key generated for Secure Boot signing.

## Operator Directive

> "the future custom OS and the new build / hardware of this machine"

> "DO not minimize, do not reduze, do not conflate, do not hack or try to take shortcuts. we do this right all the way"

## Goals

See Done When criteria — each is a verifiable hardware-assembly checkpoint.

## Done When

- [ ] **Procurement complete**: all parts listed in [[src-sain-01-sovereign-node-spec|SAIN-01 spec § 1.1]] received
- [ ] **PCIe slot assignment correct**: Blackwell in PCIEX16_1, 4090 in PCIEX16_2 — verified before first boot
- [ ] **M.2_2 confirmed empty** at the physical level (M.2_1 populated with primary OS NVMe; the second NVMe goes in a slot that does NOT share lanes with PCIEX16_2)
- [ ] **First boot to UEFI** succeeds — both GPUs detected; both NVMe detected; both NICs detected; 128-256 GB RAM detected
- [ ] **BIOS settings configured**: AMD IOMMU enabled, Above 4G Decoding enabled, Re-Size BAR enabled, EXPO/DOCP memory profile set to verified spec (verify via `dmidecode -t memory` post-boot)
- [ ] **MOK key generated** via `openssl req -new -x509 -newkey rsa:2048 -keyout MOK.key -out MOK.crt -nodes -days 3650 -subj "/CN=Sovereign Node/"` and stored at mode 0600
- [ ] **MOK enrolled** via `mokutil --import MOK.crt`; UEFI MOK manager prompted at next boot; key enrolled successfully
- [ ] **PCIe link width verified** via `lspci -vvv -s <blackwell_bdf>` and `lspci -vvv -s <4090_bdf>` — both show `LnkSta: Speed 16GT/s (ok), Width x8 (ok)` (or PCIe 4.0 x8 acceptable for the 4090 since it's Ada Lovelace)
- [ ] **IOMMU groups verified** via `find /sys/kernel/iommu_groups/ -type l | sort` — Blackwell GPU + audio in one group, RTX 4090 GPU + audio in a separate group, no other devices in the GPU groups
- [ ] **Preferred CCD identified** via `cat /sys/devices/system/cpu/cpufreq/policy*/cpuinfo_max_freq` — operator notes which CCD boost-clocks higher (informs E106 Pulse pinning if reassignment needed)
- [ ] **`friction-audit` script passes** at boot (script delivered by E101; this checkpoint is "the audit confirms hardware is correct")
- [ ] **BIOS revision pinned**: operator notes the BIOS version that delivers clean IOMMU groups; locks against firmware drift

## Scale and Model

> [!info] Epic Parameters
>
> | Parameter | Value |
> |---|---|
> | **Model** | integration |
> | **Quality tier** | Skyscraper |
> | **Estimated tasks** | 6-8 (procurement + assembly + BIOS config + MOK + verification × 2 GPUs) |
> | **Dependencies** | None — entry point of the milestone |
> | **Feeds into** | E101 (Sovereign OS Build needs hardware to install onto), E103 (VFIO needs IOMMU groups verified clean), E106 (Pulse pinning depends on CCD layout known) |
> | **Operator gate** | First boot to UEFI is the human-supervised checkpoint; subsequent verification can run via `friction-audit` |

## Handoff Context

> [!info] For a fresh context picking up this epic:
>
> - Read the milestone: [[sain-01-sovereign-node|Milestone — SAIN-01 Sovereign AI Node]]
> - Read the hardware section: [[src-sain-01-sovereign-node-spec|§ 1 Hardware Architecture & Topology Mapping]]
> - Read the dual-CCD concept: [[concept-dual-ccd-cache-partitioning-9900x|Dual-CCD Cache Partitioning]]
> - Read the Zen 5 synthesis: [[src-zen5-avx512-single-cycle|Zen 5 AVX-512 single-cycle]]
> - **The M.2_2 constraint** is the most-likely-to-be-forgotten rule. Confirm it physically before powering on.

## Relationships

- PART OF: [[sain-01-sovereign-node|Milestone — SAIN-01 Sovereign AI Node]]
- ENABLES: [[e101-sovereign-os-build|E101 — Sovereign OS Build]]
- ENABLES: [[e103-vfio-isolation|E103 — VFIO Isolation]]
- ENABLES: [[e106-pulse-vector-runtime|E106 — Pulse Vector Runtime]]
- IMPLEMENTS: [[src-sain-01-sovereign-node-spec|SAIN-01 Sovereign Node Spec]] § 1 (hardware foundation)
- BUILDS ON: [[concept-dual-ccd-cache-partitioning-9900x|Concept — Dual-CCD Cache Partitioning]]
- BUILDS ON: [[src-zen5-avx512-single-cycle|Synthesis — Zen 5 AVX-512 single-cycle]]

## Backlinks

[[sain-01-sovereign-node|Milestone — SAIN-01 Sovereign AI Node]]
[[e101-sovereign-os-build|E101 — Sovereign OS Build]]
[[e103-vfio-isolation|E103 — VFIO Isolation]]
[[e106-pulse-vector-runtime|E106 — Pulse Vector Runtime]]
[[SAIN-01 Sovereign Node Spec]]
[[Concept — Dual-CCD Cache Partitioning]]
[[Synthesis — Zen 5 AVX-512 single-cycle]]
