---
title: E105 — Network Segregation
aliases:
  - "E105 — Network Segregation"
  - "E105 — Network Segregation: Marvell 10GbE + Intel 2.5GbE"
type: epic
domain: backlog
status: draft
priority: P1
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
tags: [epic, sain-01, network, marvell, intel, opnsense, vlan, jumbo-frames, atlantic, igc, mgmt-vs-data]
---

# E105 — Network Segregation

## Summary

Physically + logically segregate management traffic from data traffic at the dual-NIC hardware boundary. The ProArt X870E-Creator has **two asymmetric NICs**: Intel I226-V 2.5GbE + Marvell AQC113C 10GbE. The split: **Intel 2.5GbE → VLAN 100 (management)** — host SSH, Tetragon log streams, system updates, `apt-get`, OpenSSH inbound. **Marvell 10GbE → VLAN 200 (data)** — isolated container bridge, model-weight pulls from local NAS, MTU 9000 jumbo frames, **NO default gateway** (no outbound WAN access from the data plane). The OPNsense / SD-WAN firewall enforces per-VLAN policy. The L1 synthesis identified that the L0 dump's `CONFIG_AQC111` is wrong for the AQC113C — the correct kernel driver symbol is `CONFIG_ATLANTIC` (already corrected in E101). `guardian-core.service` declares `BindsTo=tetragon.service` so network reconfiguration events that disrupt the Tetragon socket trigger a clean restart (rather than a stalled read loop).

## Operator Directive

> "Marvell AQC113C 10GbE | Native high-speed model ingestion from local storage."

> "Network traffic is physically segregated at the hardware boundary."

## Goals

See Done When — verifiable network-isolation checkpoints.

## Done When

- [ ] **Both NICs driver-loaded**: `lspci -k` confirms `atlantic` bound to the Marvell AQC113C, `igc` bound to the Intel I226-V
- [ ] **`/etc/network/interfaces`** authored per [[src-sain-01-sovereign-node-spec|§ 8.1]]:
  - Intel 2.5GbE (`enp6s0`): static `10.0.100.50/24`, gateway `10.0.100.1`, DNS `10.0.100.1`
  - Marvell 10GbE (`enp5s0`): static `10.0.200.50/24`, NO gateway, MTU 9000
- [ ] **`networkd` or `ifupdown` activated**: both interfaces come up cleanly at boot
- [ ] **`ip link show enp5s0`** confirms `mtu 9000` is set on the 10GbE
- [ ] **`ip route`** shows: default gateway via Intel 2.5GbE; NO default gateway via Marvell 10GbE
- [ ] **VLAN 100 policy on OPNsense**: management traffic allowed (SSH inbound, apt-get outbound, NTP, syslog); data plane denied
- [ ] **VLAN 200 policy on OPNsense**: container bridge + NAS access allowed (Marvell traffic only); WAN egress denied
- [ ] **Throughput test on Marvell**: `iperf3` to local NAS achieves ≥ 5 Gbps sustained (10 GbE realistic — line-rate minus protocol overhead)
- [ ] **Jumbo frames verified**: `ping -M do -s 8972 <nas_ip>` succeeds (8972 = 9000 MTU − 28 header overhead); fragmentation does NOT occur
- [ ] **Management plane verified**: SSH from operator workstation reaches the SAIN-01 host on `10.0.100.50:22`; `apt-get update` succeeds through Intel 2.5GbE
- [ ] **Data plane isolation verified**: from the SAIN-01 host, `curl https://example.com` via the Marvell interface fails (no default GW); model-weight pull from NAS via Marvell succeeds
- [ ] **Tetragon socket survival**: simulate OPNsense reload (`service networkd restart` on OPNsense side) — `guardian-core` does NOT enter a stall; the systemd `BindsTo=tetragon.service` restart pattern engages cleanly

## Scale and Model

> [!info] Epic Parameters
>
> | Parameter | Value |
> |---|---|
> | **Model** | integration |
> | **Quality tier** | Skyscraper |
> | **Estimated tasks** | 5-7 |
> | **Dependencies** | E101 (kernel has both `CONFIG_ATLANTIC` + `CONFIG_IGC` drivers) |
> | **Feeds into** | E110 (model catalog pulls weights via the Marvell 10GbE), E108 (profiles route compute traffic through the data plane) |
> | **External dependency** | OPNsense / SD-WAN firewall configured with VLAN 100 + VLAN 200 policies; operator confirms before this epic can complete |

## Handoff Context

> [!info] For a fresh context picking up this epic:
>
> - Milestone: [[sain-01-sovereign-node|Milestone — SAIN-01 Sovereign AI Node]]
> - L1 spec section: [[src-sain-01-sovereign-node-spec|§ 8 Network Infrastructure & Perimeter Segregation]]
> - **Driver correction from L1**: the AQC113C uses `CONFIG_ATLANTIC`, NOT `CONFIG_AQC111` (the L0 dump's wrong symbol)
> - **The "no default gateway" rule on Marvell** is the load-bearing isolation — operators sometimes set it for convenience and break the data-plane isolation. Verify with `ip route` at every config change.
> - OPNsense policy authoring is operator-side; the SAIN-01 host's `/etc/network/interfaces` is the in-host half of the contract.

## Relationships

- PART OF: [[sain-01-sovereign-node|Milestone — SAIN-01 Sovereign AI Node]]
- DEPENDS ON: [[e101-sovereign-os-build|E101 — Sovereign OS Build]]
- ENABLES: [[e110-model-catalog|E110 — Model Catalog]] (model weight pulls via Marvell 10GbE)
- ENABLES: [[e108-load-balancing-profiles|E108 — Load-Balancing Profiles]] (sub-agent traffic routes per data plane)
- IMPLEMENTS: [[src-sain-01-sovereign-node-spec|SAIN-01 Sovereign Node Spec]] § 8
- RELATES TO: [[infrastructure-as-code-patterns|Infrastructure as Code Patterns]] (interfaces config as declarative state)

## Backlinks

(will be populated by `tools/obsidian.py backlinks` after pipeline post)
