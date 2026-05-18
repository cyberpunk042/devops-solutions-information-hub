---
title: E101 — Sovereign OS Build
aliases:
  - "E101 — Sovereign OS Build"
  - "E101 — Custom Zen-5-Tuned Kernel + live-build ISO"
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
tags: [epic, sain-01, kernel, debian, trixie, live-build, znver5, gcc14, dkms]
---

# E101 — Sovereign OS Build

## Summary

Build the custom Zen-5-tuned Linux kernel (6.12+) compiled with `-march=znver5 -O3` via GCC 14, package via `bindeb-pkg` for clean DKMS integration, sign with the MOK key from E100 for Secure Boot compatibility, and assemble the bootable Sovereign OS `.iso` via Debian 13 (Trixie) `live-build`. The kernel build runs entirely in a 64 GB `tmpfs` ramdisk to maximize compilation throughput + protect NVMe longevity. The resulting OS image carries verbatim identity injection (`/etc/os-release` ID `sovereign`, motd with the operator-stated text), pre-baked ZFS-DKMS + NVIDIA 560+ open-kernel-dkms drivers, and the `friction-audit` script for boot-time hardware verification. Hallucinated kernel-config symbols flagged in the L0 dump (`CONFIG_MNATIVE_AMD`, `CONFIG_AQC111`, `bwarw tools-compiler` apt package) must be **corrected during implementation** — use `CONFIG_ATLANTIC` for the Marvell 10GbE driver, omit the non-existent `CONFIG_MNATIVE_AMD` symbol, replace `bwarw tools-compiler` with the real packages from the dump's apt-get line.

## Operator Directive

> "the future custom OS and the new build / hardware of this machine"

> "DO not minimize, do not reduze, do not conflate, do not hack or try to take shortcuts. we do this right all the way"

## Goals

See Done When criteria — each is a verifiable build-pipeline checkpoint.

## Done When

- [ ] **Minimal Debian 13 (Trixie) Netinst** flashed to USB; expert install runs; all desktop environments unchecked in `tasksel`; only SSH server + standard utilities installed
- [ ] **DEB822 sources configured** at `/etc/apt/sources.list.d/debian.sources` per the spec § Phase I Step 1.3
- [ ] **GCC 14 + build toolchain installed** — corrected from the L0 dump's hallucinated `bwarw tools-compiler`; real packages: `build-essential libncurses-dev bison flex libssl-dev libelf-dev bc git rsync debhelper pahole gcc-14 g++-14`
- [ ] **64 GB tmpfs ramdisk mounted** at `/mnt/kernel_forge`; kernel source extracted there
- [ ] **Linux Kernel 6.12+ stable** cloned from `cdn.kernel.org`
- [ ] **`.config` configured** with `KCFLAGS="-march=znver5 -O3 -pipe -mabm -madx -mavx512f -mavx512dq -mavx512bw -mavx512vl -mavx512bf16 -mavx512fp16"` + `KCPPFLAGS="-march=znver5"`
- [ ] **Kernel config corrections applied**: `CONFIG_MNATIVE_AMD` **omitted** (not a real symbol — bare `-march=znver5` via KCFLAGS suffices); `CONFIG_AQC111` **replaced with `CONFIG_ATLANTIC`** for the Marvell AQC113C 10GbE
- [ ] **Compilation succeeds** via `make -j24 KCFLAGS="-march=znver5 -O3" KCPPFLAGS="-march=znver5 -O3" bindeb-pkg`
- [ ] **`.deb` packages installed** via `dpkg -i linux-image-6.12.*-znver5_*.deb linux-headers-6.12.*-znver5_*.deb`
- [ ] **MOK signing** applied to the new kernel image + DKMS-built ZFS + NVIDIA modules using the key from E100
- [ ] **`live-build` directory tree** created per [[src-sain-01-sovereign-node-spec|spec § 3.1]]
- [ ] **package-lists/sovereign.list.chroot** includes the canonical set: `nvidia-open-kernel-dkms`, `nvidia-driver`, `nvidia-smi`, `nvidia-container-toolkit`, `zfsutils-linux`, `zfs-dkms`, `podman`, `git`, `curl`, `tmux`, `python3-minimal`, `python3-pip`
- [ ] **Identity injection** in `/etc/os-release` (`ID=sovereign`, `PRETTY_NAME="Sovereign OS v1.0 (Zen 5 Trixie Deployment Node)"`)
- [ ] **motd** contains the verbatim operator-stated text: *"We want quality over quantity and honesty over cheats and lies. We do not want hacks, quick fixes, and shortcuts."*
- [ ] **`friction-audit` script** installed at `/usr/local/bin/friction-audit`; corrected from L0 dump (scope the lane-width check to GPU BDFs via `lspci -s <bdf>`, not `lspci -vvv | grep -c "Width x8"`)
- [ ] **`sovereign-guard.service` systemd unit** installed; runs `friction-audit` before `podman.service` + `docker.service`
- [ ] **`.iso` builds** successfully via `live-build`
- [ ] **First boot from `.iso`** succeeds on the E100 hardware; `uname -r` shows `6.12.x-znver5`; `cat /etc/os-release | grep ID=` returns `ID=sovereign`
- [ ] **DKMS status verified** via `dkms status` — ZFS + NVIDIA modules built + loaded against the new kernel
- [ ] **AVX-512 + VNNI + BF16 + FP16 verified** via `grep --color=always -E "avx512_vnni|avx512_bf16|avx512_fp16" /proc/cpuinfo` — all three present

## Scale and Model

> [!info] Epic Parameters
>
> | Parameter | Value |
> |---|---|
> | **Model** | feature-development (full document → design → scaffold → implement → test) |
> | **Quality tier** | Skyscraper — kernel-level work; mistakes are reboot-loops |
> | **Estimated tasks** | 10-12 (kernel-build pipeline + live-build pipeline + verification × multiple subsystems) |
> | **Dependencies** | E100 (hardware ready + MOK key generated) |
> | **Feeds into** | E102, E103, E104, E105, E106, E107 (every subsequent epic needs the OS booted) |
> | **Operator gate** | First boot of custom kernel; MOK manager UEFI prompt; live-build ISO validation |
> | **Hallucination corrections** | `bwarw tools-compiler` → real apt packages; `CONFIG_MNATIVE_AMD` → omit; `CONFIG_AQC111` → `CONFIG_ATLANTIC`; `friction-audit` lane check → scope to GPU BDFs |

## Handoff Context

> [!info] For a fresh context picking up this epic:
>
> - Read the milestone: [[sain-01-sovereign-node|Milestone — SAIN-01 Sovereign AI Node]]
> - Read the OS build section: [[src-sain-01-sovereign-node-spec|§ 2 Stage 1 Bootstrap Forge]] + [[src-sain-01-sovereign-node-spec|§ 3 Stage 2 Sovereign OS Artifact]]
> - Read the Zen 5 synthesis: [[src-zen5-avx512-single-cycle|Zen 5 AVX-512 single-cycle]] — explains why `-march=znver5` matters
> - **Critical hallucinations to correct** during implementation (do NOT copy-paste from the L0 dump verbatim):
>   - `bwarw tools-compiler` — replace with real packages from the apt-get line
>   - `CONFIG_MNATIVE_AMD` — not a real symbol; `-march=znver5` via KCFLAGS does the job
>   - `CONFIG_AQC111` — wrong; the AQC113C is under `CONFIG_ATLANTIC`
>   - `friction-audit` `Width x8` check — scope to GPU BDFs to avoid false-pass

## Relationships

- PART OF: [[sain-01-sovereign-node|Milestone — SAIN-01 Sovereign AI Node]]
- DEPENDS ON: [[e100-hardware-foundation|E100 — Hardware Foundation]]
- ENABLES: [[e102-zfs-storage-layout|E102 — ZFS Storage Layout]]
- ENABLES: [[e103-vfio-isolation|E103 — VFIO Isolation]]
- ENABLES: [[e104-tetragon-guardian-perimeter|E104 — Tetragon + Guardian Perimeter]]
- ENABLES: [[e105-network-segregation|E105 — Network Segregation]]
- ENABLES: [[e106-pulse-vector-runtime|E106 — Pulse Vector Runtime]]
- ENABLES: [[e107-weaver-state-fabric|E107 — Weaver State Fabric]]
- IMPLEMENTS: [[src-sain-01-sovereign-node-spec|SAIN-01 Sovereign Node Spec]] §§ 2-3
- BUILDS ON: [[src-zen5-avx512-single-cycle|Synthesis — Zen 5 AVX-512 single-cycle]]

## Backlinks

[[sain-01-sovereign-node|Milestone — SAIN-01 Sovereign AI Node]]
[[e100-hardware-foundation|E100 — Hardware Foundation]]
[[e102-zfs-storage-layout|E102 — ZFS Storage Layout]]
[[e103-vfio-isolation|E103 — VFIO Isolation]]
[[e104-tetragon-guardian-perimeter|E104 — Tetragon + Guardian Perimeter]]
[[e105-network-segregation|E105 — Network Segregation]]
[[e106-pulse-vector-runtime|E106 — Pulse Vector Runtime]]
[[e107-weaver-state-fabric|E107 — Weaver State Fabric]]
[[SAIN-01 Sovereign Node Spec]]
[[Synthesis — Zen 5 AVX-512 single-cycle]]
