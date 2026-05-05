---
title: "Synthesis: Suricata IPS Mode for Linux (Layer-1 instance)"
type: source-synthesis
domain: infrastructure
status: synthesized
confidence: high
maturity: seed
created: 2026-05-04
updated: 2026-05-04
sources:
  - id: suricata-docs-ips-linux
    type: documentation
    url: "https://docs.suricata.io/en/latest/ips/setting-up-ipsinline-for-linux.html"
tags:
  - suricata
  - ips-mode
  - nfqueue
  - af-packet
  - dpdk
  - netmap
  - inline
  - layer-1
  - root-ghostproxy
  - module
  - architectural-decision
layer: 1
---

# Synthesis: Suricata IPS Mode for Linux (Layer-1 instance)

## Summary

Suricata supports five distinct IPS deployment modes on Linux: **NFQUEUE with iptables**, **NFQUEUE with nftables**, **AF_PACKET Layer-2 inline**, **DPDK Layer-2 inline**, and **Netmap Layer-2 inline (with optional host-stack single-interface mode)**. Each mode trades off configuration complexity, performance, and topological assumptions differently. For root-ghostproxy — a transparent Layer-2 bridge appliance with two Ethernet ports (enp2s0, enp4s0) currently bridged via br0 — **AF_PACKET IPS mode is the architecturally cleanest match**: it requires no iptables/nftables NAT rules at all; Suricata itself bridges packets between paired interfaces with `copy-mode: ips`, honoring `drop` keywords on rule matches. **This conflicts with the existing br0 setup** — using AF_PACKET IPS mode means removing the kernel bridge and letting Suricata be the bridge. M005 Suricata-first design must explicitly choose: keep br0 (then NFQUEUE on br0's forward path) OR retire br0 (then AF_PACKET IPS mode owns the inline path).

> [!info] Source Reference
> | Attribute | Value |
> |-----------|-------|
> | Source | docs.suricata.io chapter 23.2 (Suricata 9.0.0-dev) |
> | Sub-chapters | 23.2.1 Netfilter (NFQUEUE) · 23.2.2 Layer-2 (AF_PACKET / DPDK / Netmap) |
> | Type | documentation (Layer-1 IPS deployment instance) |
> | Maintainer | OISF |
> | Ingested | 2026-05-04 |

## Key Insights

> [!abstract] Two architectural families: Layer-3 (NFQUEUE) and Layer-2 (AF_PACKET / DPDK / Netmap)
> Layer-3 modes route packets through iptables/nftables → NFQUEUE → Suricata → kernel verdict (DROP/ACCEPT/MARK). Layer-2 modes bypass netfilter entirely; Suricata copies packets directly between paired interfaces. For a transparent-bridge appliance, Layer-2 modes are simpler and lower-overhead but require dedicating two interfaces. For a routing/firewall host, NFQUEUE integrates with existing firewall rules.

1. **NFQUEUE + iptables** — the Layer-3 classic.
   - Build Suricata with NFQ support (`./configure --enable-nfqueue`); verify with `suricata --build-info | grep NFQ`.
   - Run with `-q 0` (queue 0 by default); multi-queue with `-q 3 -q 4 -q 5`.
   - Forwarded gateway: `sudo iptables -I FORWARD -j NFQUEUE`.
   - Host-protect: `sudo iptables -I INPUT -j NFQUEUE` + `sudo iptables -I OUTPUT -j NFQUEUE`.
   - Per-protocol/per-port filter: combine with `-p tcp --dport 80` etc.
   - **Failopen risk**: by default, if no userspace listener (Suricata down), netfilter DROPS queued packets. Use the `bypass` option (see #4) to convert to ACCEPT-on-no-listener.

2. **NFQUEUE + nftables** — the modern Layer-3 path. nftables hook integration:
   ```
   nft> add chain filter IPS { type filter hook forward priority 10 ; }
   nft> add rule filter IPS queue
   ```
   Mix firewall rules and IPS — the dedicated IPS chain runs after the filter chain. Per-interface filtering supported via `iif`/`oif` matches: `nft> add rule filter IPS iif eth0 oif eth1 queue`.

3. **NFQUEUE advanced options — `fanout` + `bypass` (load-bearing for production)**.
   ```
   nft add rule filter IPS queue num 3-5 options fanout,bypass
   ```
   - `fanout`: load-balances across queues by CPU ID (instead of connection hash) — pair with one queue per CPU for best throughput.
   - `bypass`: when no listener, treat as ACCEPT (rather than DROP). **This is the failopen pattern for NFQUEUE-based IPS** — converts Suricata-down from "network outage" to "blocking disabled, traffic still flows."

> [!warning] Layer-3 modes default to fail-CLOSED — explicit `bypass` makes them fail-open
> Without `bypass`, a Suricata crash takes down the inspected segment. For root-ghostproxy this is the documented "in IPS mode a crash may knock a network offline" risk. nftables `bypass` option is the canonical mitigation.

4. **AF_PACKET IPS mode — the Layer-2 transparent bridge replacement.** No iptables/nftables config at all. Two interfaces with `copy-mode: ips` and reciprocal `copy-iface` settings:
   ```yaml
   af-packet:
     - interface: eth0
       threads: 1
       defrag: no
       cluster-type: cluster_flow
       cluster-id: 98
       copy-mode: ips
       copy-iface: eth1
       buffer-size: 64535
     - interface: eth1
       threads: 1
       cluster-id: 97
       defrag: no
       cluster-type: cluster_flow
       copy-mode: ips
       copy-iface: eth0
       buffer-size: 64535
   ```
   - **MTU must match on both interfaces** (Suricata copies packets directly; oversized packets get kernel-dropped).
   - **`cluster-id` must differ** between the two interfaces (otherwise conflict).
   - **Disable hardware offloading** (GRO, LRO, TSO) — these create super-MTU datagrams the transmit path can't handle.
   - **Set `stream.inline: yes`** (or `auto`) so Suricata switches to blocking mode.
   - **`copy-mode` values**: `ips` (drop on rule match) or `tap` (no drop, just inspect — degraded IPS, useful for testing).

5. **AF_PACKET IPS at multi-thread + eBPF load balancing — the production-throughput pattern.**
   ```yaml
   - interface: eth0
     threads: 16
     defrag: no
     cluster-type: cluster_ebpf
     ebpf-lb-file: /usr/libexec/suricata/ebpf/lb.bpf
     cluster-id: 98
     copy-mode: ips
     copy-iface: eth1
     buffer-size: 64535
   ```
   The eBPF file `/usr/libexec/suricata/ebpf/lb.bpf` may not be present in default install — see "eBPF and XDP" chapter for build steps. Without eBPF LB, multi-threaded AF_PACKET IPS suffers from defrag-disabled-imbalance: IP fragments and full packets land on different threads.

6. **DPDK IPS mode — high-performance NIC bypass path.** Same `copy-mode: ips` + `copy-iface` pattern but via DPDK PMD. NIC identified by PCI address (e.g. `0000:3b:00.1`). Requires:
   - DPDK toolchain installed; Suricata built with `--enable-dpdk`
   - CPU affinity explicit: `threading.set-cpu-affinity: yes` + `worker-cpu-set` listing cores per thread
   - `mempool-size`, `rx-descriptors`, `tx-descriptors`, `mtu` all explicit per interface
   - Promiscuous + multicast + checksum offloads configured
   For root-ghostproxy at micro-scale, DPDK is overkill. Reserve for >1 Gbps inspection requirements.

7. **Netmap IPS mode — the BSD/Linux zero-copy alternative.** Same `copy-mode: ips` + `copy-iface` pattern. Two flavors:
   - **Native mode** (paired physical interfaces): `interface: enp6s0f0` → `copy-iface: enp6s0f1` and reciprocal.
   - **Host-stack mode (single-interface)**: interface name suffixed with `^` (e.g. `enp6s0f0^`) — Netmap creates host-stack rings; packets flow through host OS network stack between Suricata and the NIC. Lets root-ghostproxy use ONE physical interface and still inspect everything. Useful as a fallback when only one interface is available; less common for transparent-bridge appliances.
   Zero-copy is enabled when runmode is `workers`. Same MTU/offload caveats as AF_PACKET.

8. **The five modes ranked for root-ghostproxy's transparent-bridge appliance:**

   | Mode | Topology fit | Throughput | Failopen story | M005 default? |
   |---|---|---|---|---|
   | NFQUEUE + nftables + `bypass` | Keep br0; NFQUEUE on FORWARD path | Lower (kernel queue overhead) | Explicit `bypass` option | Recommended for Phase-1 |
   | NFQUEUE + iptables | Same; legacy firewall stack | Same | `--queue-bypass` | Skip (Debian 13 nftables-default) |
   | AF_PACKET IPS | Retire br0; Suricata IS the bridge | Higher | Suricata-down = no copy = packets dropped at NIC, fail-CLOSED at L2 | Phase-2 / production |
   | DPDK IPS | Retire br0; DPDK NIC bypass | Highest | Same as AF_PACKET (no copy = drop) | Skip (overkill at micro-scale) |
   | Netmap IPS | Retire br0 (or host-stack on one NIC) | High | Same as AF_PACKET | Skip unless DPDK denied |

> [!warning] The br0-vs-AF_PACKET-IPS architectural decision
> root-ghostproxy currently has `br0` with `enp2s0` + `enp4s0` as members (per the operator's prior-session memory). AF_PACKET IPS mode requires the two physical interfaces to NOT be in a kernel bridge — Suricata copies between them itself. **You can't have both.** Choose: (a) keep br0, use NFQUEUE on FORWARD path with `bypass` option for failopen — simpler, works with existing topology; (b) retire br0, use AF_PACKET IPS — tighter integration, no NAT rules at all, but requires breaking the existing bridge and rebuilding inline-via-Suricata. M005 design doc must capture this decision explicitly.

## Operational scaffold notes for root-ghostproxy M005 Suricata-first

**Phase-1 recommendation (lowest disruption to existing topology):**
- Keep `br0` with `enp2s0` + `enp4s0` as bridge members.
- Add nftables FORWARD chain hooking to NFQUEUE on br0 traffic with `bypass` enabled.
- Run Suricata with `-q 0` reading from queue 0.
- Failopen via `bypass` option — Suricata down = traffic still flows, just not inspected (or blocked).
- Rule effect: `drop` keywords honored via NFQUEUE verdict.

**Phase-2 upgrade path (production):**
- Retire `br0` (the kernel bridge).
- Configure AF_PACKET IPS mode with `enp2s0` and `enp4s0` paired via `copy-mode: ips`.
- Add eBPF load balancer if multi-thread (`/usr/libexec/suricata/ebpf/lb.bpf`).
- Disable NIC offloads (GRO/LRO/TSO) on both interfaces.
- Match MTU on both interfaces.
- Set `stream.inline: yes`.
- Bridge functionality is now Suricata's; bridge failure = inspection failure = traffic stops at NIC level (fail-closed at L2). Compensate with watchdog/health-check.

**Common to both phases:**
- `suricata --build-info` must show NFQ (Phase-1) or AF_PACKET-IPS-mode (Phase-2) capability.
- Test with SID 2100498 + `curl http://testmynids.org/uid/index.html` (per src-suricata-install-quickstart).
- Rule with `drop ip ...` verb to test inline blocking; passive `alert` rule confirms IDS path; both must work.

## Open Questions

- Does the existing `/root/install.sh` already configure br0? If yes, AF_PACKET IPS mode is a **destructive** topology change; phase plan must reflect that.
- Is eBPF load balancer file (`/usr/libexec/suricata/ebpf/lb.bpf`) shipped in Debian's suricata package, or must it be built? Affects Phase-2 readiness.
- For Phase-1 nftables-with-bypass: does the existing /root nftables config already define a filter table? If yes, M005 just adds a chain; if no, the table itself must be authored.
- Does root-ghostproxy ever need to inspect host-generated traffic (the box's own outbound), or only forwarded traffic? `INPUT/OUTPUT` chains vs `FORWARD` chain decision.
- Failopen choice: NFQUEUE `bypass` (network keeps working when Suricata is down — recommended for an inspection-not-firewall appliance) OR fail-closed (Suricata down = network down — recommended for high-trust environments). Operator's threat model decides.

## Relationships

- BUILDS ON: [[src-suricata|Suricata source-synthesis (Layer 0)]]
- BUILDS ON: [[src-suricata-install-quickstart|Suricata install + quickstart (Layer-1 install instance)]]
- USED BY: [[root-ghostproxy-m005-first-specialized-feature-module|M005 — First specialized feature module]] — DIRECT design-document input
- USED BY: [[root-ghostproxy-sfif-rollout-and-second-brain-integration-2026-05|Epic — root-ghostproxy SFIF Rollout]]
- RELATES TO: [[src-polarproxy|PolarProxy synthesis]] — both modules' inline-on-bridge design choices interlock

## Backlinks

[[Suricata source-synthesis (Layer 0)]]
[[Suricata install + quickstart (Layer-1 install instance)]]
[[M005 — First specialized feature module]]
[[Epic — root-ghostproxy SFIF Rollout]]
[[PolarProxy synthesis]]
