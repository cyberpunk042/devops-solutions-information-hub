---
title: VFIO GPU Isolation with AMD IOMMU
aliases:
  - "VFIO GPU Isolation with AMD IOMMU"
  - "VFIO Passthrough"
  - "GPU Sandboxing via vfio-pci"
type: concept
layer: 2
maturity: growing
domain: devops
status: synthesized
confidence: high
created: 2026-05-15
updated: 2026-05-15
sources:
  - id: src-sain-01-sovereign-node-spec
    type: wiki
    file: "wiki/sources/src-sain-01-sovereign-node-spec.md"
    title: "Synthesis — SAIN-01 Sovereign AI Node Master Specification"
  - id: vfio-kernel-docs
    type: documentation
    url: "https://docs.kernel.org/driver-api/vfio.html"
    title: "Linux kernel VFIO documentation"
tags:
  - devops
  - vfio
  - gpu-isolation
  - amd-iommu
  - iommu
  - pci-passthrough
  - vfio-pci
  - sandboxing
  - sain-01
  - rtx-3090
  - blackwell
  - hardware-isolation
  - kernel
  - grub
---

# VFIO GPU Isolation with AMD IOMMU

## Summary

**VFIO (Virtual Function I/O) with AMD IOMMU** is the Linux kernel mechanism for binding a physical PCIe device to a userspace driver at boot, removing it from the host kernel's purview entirely. On the [[src-sain-01-sovereign-node-spec|SAIN-01 Sovereign Node]], this is the technique that **isolates the secondary RTX 3090 GPU as a sandboxed agent-fleet substrate** while the primary RTX PRO 6000 Blackwell remains host-resident for primary inference. The mechanism: GRUB kernel parameters (`amd_iommu=on iommu=pt` + `vfio-pci.ids=10de:2204,10de:1ad8`) bind the `vfio-pci` driver to the GPU and its companion audio device by **PCI vendor:device ID** at boot, before the NVIDIA host driver loads. The host OS never sees the 3090; it can be passed through to a sandboxed container or VM as if it were a private device. The [[concept-srp-trinity-pulse-weaver-auditor|Trinity's Weaver]] uses this to give sub-agent fleets GPU compute without exposing them to the host's primary inference path or context. The IOMMU enforces this at the hardware level — a misbehaving sub-agent cannot DMA into host memory because the IOMMU translates every device memory access through its own page tables, isolated from the host kernel's. This is the architectural equivalent of "VLAN for PCIe devices."

## Key Insights

- **VFIO binds a device to userspace at the PCI bus, not at boot device discovery.** The kernel parameter `vfio-pci.ids=<vendor>:<device>,...` is processed during PCI enumeration — the `vfio-pci` driver claims the device by ID before any other driver gets the chance. The NVIDIA host driver loads later and sees no GPU at that BDF. This is what makes the host OS structurally unaware of the 3090: it isn't unbinding it after boot, it never bound it in the first place. ([[src-sain-01-sovereign-node-spec|SAIN-01 synthesis]])

- **PCI vendor:device IDs are stable and platform-independent.** The SAIN-01 spec's `10de:2204,10de:1ad8` are: `10de:2204` = NVIDIA GA102 (RTX 3090 GPU core); `10de:1ad8` = NVIDIA GA102 HD Audio Controller (the GPU's companion audio output). Both must be bound together — devices in the same IOMMU group can't be split between host and sandbox. The vendor IDs are stable across motherboards and Linux distributions; the same `vfio-pci.ids` line works on any AMD-IOMMU-capable system with the same GPU. ([[src-sain-01-sovereign-node-spec|SAIN-01 synthesis]])

- **`amd_iommu=on iommu=pt` enables hardware-level isolation.** `amd_iommu=on` activates the AMD IOMMU hardware (present on Ryzen Pro / Threadripper / Ryzen 9 since Zen 2; standard on Zen 5). `iommu=pt` enables **pass-through mode** — IOMMU page-table translation is bypassed for host-attached devices (preserving performance) but enforced for VFIO-isolated devices. The combination delivers: full hardware isolation for the sandboxed GPU + zero performance cost for the host-resident GPU + normal device access for everything else. ([[src-sain-01-sovereign-node-spec|SAIN-01 synthesis]])

- **The asymmetric dual-GPU layout is structurally distinct, not just "two cards."** The Blackwell stays in the host's nvidia driver — the [[concept-srp-trinity-pulse-weaver-auditor|Oracle Core]] tier's deep-reasoning workloads run directly. The 3090 lives entirely outside the host's perception — sandboxed agent fleets get a private GPU. This isolation is the Weaver's contract; sub-agents can be malicious or buggy without compromising the host or the Oracle Core's models. ([[src-sain-01-sovereign-node-spec|SAIN-01 synthesis]])

- **IOMMU groups constrain what can be isolated.** PCIe devices in the same IOMMU group share isolation boundaries — all bound to vfio-pci together, or none. The 3090's GPU + audio companion form one group typically; the Blackwell forms its own. Operator must verify via `find /sys/kernel/iommu_groups/ -type l | sort` after boot that the intended group separation is real. Some motherboards collapse multiple slots into one IOMMU group (e.g., via PCIe switches without ACS); this would prevent the asymmetric isolation. The ASUS ProArt X870E-Creator's chipset layout supports the split per the SAIN-01 spec. ([[src-sain-01-sovereign-node-spec|SAIN-01 synthesis]])

- **NVIDIA's `nvidia-drm.modeset=1` + `nvidia.NVreg_EnableGpuFirmware=1` cooperate cleanly.** The host driver loads with modeset enabled (for the Blackwell's display + compute paths) and GpuFirmware-signing checks enabled. The vfio-pci-bound 3090 is invisible to nvidia.ko, so these settings don't conflict. The Blackwell can use the latest 560+ NVIDIA driver stack while the 3090 runs whatever the sandboxed container brings (potentially a different driver version or none — e.g., a CUDA-toolkit-only image without `nvidia-modprobe`). ([[src-sain-01-sovereign-node-spec|SAIN-01 synthesis]])

- **MOK (Machine Owner Key) enrollment is required for Secure Boot compatibility.** Custom kernels + VFIO + DKMS modules need cryptographic signing for Secure Boot UEFI firmware. The SAIN-01 spec includes generating an MOK pair via `openssl req -new -x509 ...` + enrolling with `mokutil --import MOK.crt`. Without this, Secure Boot rejects the kernel + signed modules and the system fails to boot. ([[src-sain-01-sovereign-node-spec|SAIN-01 synthesis]])

- **VFIO performance is near-native.** Once the device is bound and passed through, the userspace driver (or container's CUDA stack) accesses the GPU at near-native speed. IOMMU page-table translation adds nanoseconds per memory access; for compute-bound workloads like LLM inference, the overhead is unmeasurable. The tradeoff is **isolation strength, not throughput cost**. ([[src-sain-01-sovereign-node-spec|SAIN-01 synthesis]])

> [!warning] All-or-Nothing Device Binding
> A device is either bound to vfio-pci or to its host driver — there is no "partial" binding. Switching a device's binding requires a reboot (because PCI enumeration runs once at boot) OR a runtime unbind/rebind dance via `/sys/bus/pci/drivers/` which is fragile under load. Plan the isolation layout up-front; runtime reconfiguration is a footgun.

## Deep Analysis

### The boot-time binding sequence

When the SAIN-01 system boots, the following sequence executes:

```
1. UEFI firmware loads the GRUB bootloader
   └─ Verifies kernel signature against MOK if Secure Boot enabled

2. GRUB loads the Linux kernel with parameters:
   GRUB_CMDLINE_LINUX_DEFAULT="
     quiet splash
     amd_iommu=on iommu=pt           # Enable AMD IOMMU + pass-through mode
     kvm_amd.npt=1 kvm_amd.avic=1    # KVM nested paging + advanced virtual interrupt controller
     vfio-pci.ids=10de:2204,10de:1ad8  # Bind RTX 3090 + audio to vfio-pci
     nvidia-drm.modeset=1            # Enable NVIDIA DRM modeset for Blackwell
     nvidia.NVreg_EnableGpuFirmware=1 # Require firmware signature checks
   "

3. Kernel initializes:
   - AMD IOMMU hardware activated; pass-through mode for host devices
   - PCI bus enumerated
   - For each PCIe device, drivers register interest based on vendor:device ID:
       * Blackwell (10de:????) → matched by nvidia.ko (loaded later); claimed by NVIDIA host driver
       * RTX 3090 (10de:2204) → matched by vfio-pci (loaded early); claimed by vfio-pci
       * RTX 3090 audio (10de:1ad8) → matched by vfio-pci; claimed by vfio-pci
       * Everything else → matched by their respective drivers

4. systemd starts user-space services:
   - The host's nvidia driver initializes the Blackwell; nvidia-smi reports 1 GPU
   - The Trinity's Pulse + Weaver + Auditor begin
   - Sandboxed sub-agents launch Podman containers with --device=/dev/vfio/<group_id>
     → Access the RTX 3090 inside the container; the host never sees device traffic
```

The host kernel's `lspci` shows the RTX 3090 as bound to `vfio-pci`; `nvidia-smi` shows only the Blackwell. The 3090 is structurally invisible to the host except as a passthrough endpoint.

### IOMMU groups — the unit of isolation

The IOMMU enforces isolation in **groups** — sets of PCIe devices that share the same isolation domain. A single device cannot be partially isolated; all devices in its IOMMU group are bound together.

On the SAIN-01 hardware (ASUS ProArt X870E-Creator + Ryzen 9 9900X):

```
$ find /sys/kernel/iommu_groups/ -type l | sort
  /sys/kernel/iommu_groups/0/devices/0000:00:00.0   (Root Complex)
  ...
  /sys/kernel/iommu_groups/14/devices/0000:01:00.0  (Blackwell GPU)
  /sys/kernel/iommu_groups/14/devices/0000:01:00.1  (Blackwell HDA)
  /sys/kernel/iommu_groups/15/devices/0000:02:00.0  (RTX 3090 GPU)
  /sys/kernel/iommu_groups/15/devices/0000:02:00.1  (RTX 3090 HDA)
  ...
```

(The actual group numbers depend on the boot; what matters is the separation of the two GPUs into distinct groups.)

The Blackwell occupies one group (host-resident); the 3090 occupies a separate group (VFIO-bound). The PCIe topology of the ProArt X870E-Creator delivers this cleanly — each x16 slot has its own root port, hence its own IOMMU group.

**If the GPUs landed in the same IOMMU group**, the operator would have to either bind both to vfio-pci (losing the Blackwell as a host inference target) or neither (losing the 3090 sandbox). The SAIN-01 hardware specifically supports the asymmetric split because of the ProArt's topology.

### The PCIe x8/x8 link rule + M.2_2 constraint

The PCIe topology that enables IOMMU group separation also creates the M.2_2 constraint documented in the [[src-sain-01-sovereign-node-spec|SAIN-01 spec]]:

```
Ryzen 9 9900X — 24 PCIe Gen 5 lanes from CPU
  │
  ├─ 16 lanes split between PCIEX16_1 + PCIEX16_2
  │     └─ When both slots populated: x8 / x8 electrical
  │     └─ This is the SAIN-01 dual-GPU configuration
  │
  ├─ 4 lanes to M.2_1 (primary NVMe — OS + tank pool)
  │
  └─ 4 lanes that COULD go to M.2_2 (secondary NVMe)
        └─ BUT: M.2_2 SHARES with PCIEX16_2
        └─ Populating M.2_2 → bifurcation → PCIEX16_2 drops to x4
        └─ M.2_2 MUST REMAIN EMPTY for the dual-GPU symmetry
```

The constraint is platform-level: the ProArt board's lane sharing means M.2_2 occupies lanes that would otherwise serve the 3090. Empty M.2_2 = symmetric x8/x8 dual-GPU + clean IOMMU group separation. The `friction-audit` script in the SAIN-01 spec exists specifically to verify this at boot.

### How the Weaver uses the sandboxed 3090

The [[concept-srp-trinity-pulse-weaver-auditor|Weaver]] orchestrates sub-agents and routes work between hardware tiers. For agents that need GPU compute but are not trusted with host-level access:

```
1. Operator approves a sub-agent (e.g., a code-completion agent for the Logic Engine).
2. Weaver launches a Podman container:
   podman run --device /dev/vfio/<group_id> \
     --device-cgroup-rule='c 195:* rmw' \
     -v /mnt/vault/agents:/agents \
     <agent-image>
3. The container sees the RTX 3090 as if it were a private device.
4. The host kernel does NOT see GPU memory accesses from the container —
   IOMMU page tables isolate the container's DMA from host memory.
5. The Auditor's Tetragon policies still enforce sys_execve allowlists inside the container.
6. The Weaver writes the agent's runtime cache to tank/agents
   (a separate ZFS dataset from the host's tank/context).
```

The sandbox is **defense-in-depth**:

- IOMMU isolates GPU memory access at hardware level
- Container namespace isolates filesystem + processes
- Tetragon allowlists syscalls
- ZFS dataset stratification keeps agent runtime separate from host state
- Network split (Marvell 10GbE bridge for agent traffic) isolates network egress

Each layer can fail independently without compromising the others.

### Composition with the host-resident Blackwell

The Blackwell stays in the host nvidia driver path. The Oracle Core tier's deep-reasoning workloads use it directly via vLLM / llama.cpp / CUDA. Key composition properties:

| Concern | Blackwell (host-resident) | RTX 3090 (VFIO-sandboxed) |
|---|---|---|
| Driver | Host's nvidia-open-kernel-dkms 560+ | Sandbox-provided (could be different version) |
| Memory access | Direct (no IOMMU translation overhead, `iommu=pt`) | IOMMU-translated (negligible perf impact, hardware isolation) |
| Visible to host | Yes (`nvidia-smi` shows 1 GPU = Blackwell) | No (host has no `nvidia-smi` entry for it) |
| CUDA compute capability | 12.0 (Blackwell) | 8.6 (Ampere) |
| VRAM | 96GB GDDR7 | 24GB GDDR6X |
| Workload tier | Oracle Core (deep reasoning, large models) | Logic Engine (mid-scale quantized, sandboxed) |
| Trusted level | Host-trust | Sub-agent-trust (lower) |

The two GPUs are **architecturally different tiers**, not just "more GPUs." The VFIO split is what makes them different — they're separated by trust boundary, not by VRAM count.

### Failure modes + diagnostics

| Failure | Symptom | Diagnosis | Remediation |
|---|---|---|---|
| IOMMU not enabled | `vfio-pci.ids` ignored; both GPUs bound to nvidia.ko | `dmesg \| grep AMD-Vi` shows no IOMMU init | Verify `amd_iommu=on` in GRUB, BIOS IOMMU enabled |
| Wrong device ID | RTX 3090 still bound to nvidia.ko | `lspci -k` shows nvidia.ko driver on 02:00.0 | Verify `lspci -nn -s 02:00.0` returns expected `10de:2204` (check for revision differences) |
| IOMMU group includes Blackwell | Cannot bind 3090 without losing Blackwell | `find /sys/kernel/iommu_groups/ -type l \| sort` shows both in same group | Different motherboard / firmware update; or BIOS ACS Override (security risk) |
| MOK not enrolled, Secure Boot blocking | System fails to boot the custom kernel | UEFI screen reports unsigned kernel | `mokutil --import MOK.crt` from a recovery boot; reboot + enroll in MOK manager UI |
| `iommu=pt` mistyped as `iommu=pt1` etc. | IOMMU active but pass-through not engaged; perf regression on host devices | `dmesg \| grep "Setting up IOMMU"` shows wrong mode | Fix GRUB parameter; regenerate config; reboot |
| Container can't see device | Podman start fails with cgroup error | `ls -l /dev/vfio/` shows expected group; `--device-cgroup-rule` syntax error | Verify cgroup rule character device match (vfio is 195:*) |

## Open Questions

- Does the ASUS ProArt X870E-Creator's specific PCIe topology consistently deliver clean IOMMU group separation across BIOS revisions? Firmware updates have been known to change IOMMU group composition. (Requires: deployment verification + BIOS version pinning.)
- The Weaver's Podman launch command should include `--security-opt no-new-privileges` + appropriate cgroup limits to prevent the sandboxed agent from privilege-escalating inside the container. The SAIN-01 spec doesn't address container-side hardening. (Requires: container-security policy decision.)
- For multi-tenant agent fleets (multiple sub-agents sharing the 3090 sequentially), is the 3090's memory cleared between handoffs? GPU memory is not automatically zeroed on driver detach; a malicious agent could leave secrets in VRAM. (Requires: explicit memory-clear protocol or NVIDIA MIG-style isolation; not natively supported on consumer Ampere.)
- Live migration / hot-plug of VFIO devices — generally not supported on consumer hardware. Does the SAIN-01 deployment require runtime GPU reassignment? If yes, the operator needs a different topology (e.g., GPU per VM rather than per container). (Requires: lifecycle requirements clarification.)
- Backup path for the sandboxed agent's state — if the 3090 is exclusively container-bound, host-side ZFS snapshots can't capture in-flight GPU computation. State persistence must be explicit (write to `tank/agents` before yielding). (Requires: state-persistence pattern documentation.)
- Composition with `selfdef`'s `agent-guard` Tetragon module — both modules write Tetragon TracingPolicies. Conflict resolution when both target `sys_execve`? (Requires: cross-repo policy coordination at Stage 2.)

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **Why it exists (the Weaver's contract)** | [[concept-srp-trinity-pulse-weaver-auditor\|SRP Trinity (Pulse, Weaver, Auditor)]] |
> | **The host-resident GPU side** | [[concept-speculative-decoding-block-diffusion\|Speculative Decoding via Block Diffusion]] (Oracle Core workload on Blackwell) |
> | **Sandboxed agent runtime storage** | [[concept-zfs-tiered-storage-llm-inference\|ZFS Tiered Storage]] (`tank/agents`) |
> | **CPU partitioning for I/O threads** | [[concept-dual-ccd-cache-partitioning-9900x\|Dual-CCD Cache Partitioning]] |
> | **Source synthesis** | [[src-sain-01-sovereign-node-spec\|SAIN-01 Sovereign Node Spec]] (§ 4.3, § 1.2) |

## Relationships

- DERIVED FROM: [[src-sain-01-sovereign-node-spec|SAIN-01 Sovereign Node Spec]] (§ 4.3 VFIO isolation, § 1.2 PCIe topology)
- IMPLEMENTS: Hardware-level GPU isolation via Linux VFIO + AMD IOMMU
- ENABLES: [[concept-srp-trinity-pulse-weaver-auditor|SRP Trinity (Weaver)]] (sub-agent sandboxing on isolated GPU)
- USED BY: [[concept-zfs-tiered-storage-llm-inference|ZFS Tiered Storage]] (`tank/agents` is the sandboxed agents' runtime dataset)
- RELATES TO: [[infrastructure-as-code-patterns|Infrastructure as Code Patterns]] (GRUB parameters as declarative isolation state)

## Backlinks

[[SAIN-01 Sovereign Node Spec]]
[[Hardware-level GPU isolation via Linux VFIO + AMD IOMMU]]
[[SRP Trinity (Weaver)]]
[[ZFS Tiered Storage]]
[[infrastructure-as-code-patterns|Infrastructure as Code Patterns]]
