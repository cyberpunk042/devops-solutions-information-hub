---
title: "Synthesis: Hanke honeypot — Suricata + PolarProxy integration via dummy interface"
type: source-synthesis
domain: infrastructure
status: synthesized
confidence: high
maturity: seed
created: 2026-05-04
updated: 2026-05-04
sources:
  - id: nirusu-honeypot-readme
    type: documentation
    url: "https://github.com/Nirusu/how-to-setup-a-honeypot"
tags:
  - polarproxy
  - suricata
  - integration
  - dummy-interface
  - tcpreplay
  - pcap-over-ip
  - elk
  - filebeat
  - logstash
  - kibana
  - layer-1
  - root-ghostproxy
  - module
layer: 1
---

# Synthesis: Hanke honeypot — Suricata + PolarProxy integration via dummy interface

## Summary

Nils Hanke's "how-to-setup-a-honeypot" (associated with his master's thesis at Ruhr University Bochum) is the canonical end-to-end writeup for combining PolarProxy (TLS decryption) with Suricata (IDS), feeding into an ELK stack (Elasticsearch + Filebeat/Packetbeat + Kibana + Logstash). For root-ghostproxy M005, the load-bearing technical pattern is **routing decrypted PolarProxy output to a Linux dummy network interface that Suricata listens on** — Suricata then sees the cleartext as if it were native plaintext traffic, with no protocol gymnastics. The mechanism: `ip link add polarproxytls type dummy` creates the virtual interface; PolarProxy emits a `--pcapoverip` stream; `nc localhost 4430 | tcpreplay -i polarproxytls -t -` replays that stream into the dummy; Suricata's af-packet config lists `polarproxytls` alongside the real internet-facing NIC. The honeypot's surrounding infrastructure (VLAN-per-VM Proxmox routing, ELK pipeline, Falco for VM-level events) is not directly applicable to root-ghostproxy's transparent-bridge appliance, but the dummy-interface integration pattern is.

> [!info] Source Reference
> | Attribute | Value |
> |-----------|-------|
> | Source | Nirusu/how-to-setup-a-honeypot README + netplan.yaml + audit-rules.conf + logstash-suricata.conf |
> | Author | Nils Hanke (Ruhr University Bochum) |
> | Type | documentation (master's-thesis-derived honeypot setup writeup) |
> | License | MIT |
> | Honeypot scale | Two physical servers (Gateway + Proxmox), /24 IPv4 subnet, up to 254 VMs via VLAN tagging |
> | Referenced by | netresec.com PolarProxy product page (canonical integration pattern) |
> | Ingested | 2026-05-04 |

## Key Insights

> [!abstract] The pattern that matters for root-ghostproxy: dummy interface + tcpreplay
> Disregard the Proxmox / Gateway / VLAN-per-VM / ELK-cluster scaffolding — those are honeypot-specific. The reusable pattern is: PolarProxy emits decrypted PCAP-over-IP → `tcpreplay` replays into a Linux dummy network interface → Suricata's af-packet config lists the dummy interface alongside the real NIC → Suricata processes decrypted traffic as if it were plaintext.

1. **Linux dummy network interface — the integration bridge.** Created with one command:
   ```
   sudo ip link add polarproxytls type dummy
   ```
   The dummy interface is not persistent across reboots (netplan doesn't support dummy devices), so it must be re-created on boot via systemd-networkd, a one-shot service, or an `ip link add` line in the unit file `ExecStartPre=` of the Suricata or PolarProxy service. The interface name is arbitrary; `polarproxytls` is descriptive convention.

2. **PolarProxy's `--pcapoverip` flag emits the decrypted PCAP stream as a TCP listener.** PolarProxy listens on `localhost:4430` (configurable port) and serves the cleartext PCAP-over-IP stream to any consumer. From src-polarproxy this was already known; the Hanke writeup confirms this is the canonical hookup point.

3. **`tcpreplay` consumes the stream and replays into the dummy interface.** The bridge command:
   ```
   nc localhost 4430 | sudo tcpreplay -i polarproxytls -t -
   ```
   `-t` flag tells tcpreplay to replay at original timestamps; `-` reads PCAP from stdin. This needs to run continuously alongside PolarProxy and Suricata. **Make this a systemd service** so a crash auto-restarts.

4. **Suricata's af-packet config lists the dummy interface as an additional capture source.** From the writeup's suricata.yaml excerpt:
   ```yaml
   af-packet:
     - interface: enp4s0f0           # internet-facing NIC
       cluster-id: 1
       cluster-type: cluster_flow
       defrag: yes
       buffer-size: 131072
     - interface: polarproxytls       # dummy interface receiving decrypted TLS
       cluster-id: 2
       cluster-type: cluster_flow
       defrag: yes
   ```
   Note: `cluster-id` MUST differ between interfaces (per the IPS Mode chapter constraint). For root-ghostproxy, the `interface: polarproxytls` block is identical to Hanke's; the real-NIC block depends on the chosen IPS mode (Phase-1 NFQUEUE on br0 vs Phase-2 AF_PACKET IPS on enp2s0/enp4s0).

5. **PolarProxy needs CAP_NET_BIND_SERVICE for sub-1024 ports without root:**
   ```
   sudo setcap 'cap_net_bind_service=+ep' /path/to/PolarProxy
   ```
   This is the same pattern as the PolarProxy product page documents (with slightly different syntax). Either form works.

6. **Two PolarProxy modes used depending on the upstream service's TLS posture:**
   - **Termination Proxy** (`--terminate`) — when the backend service does NOT speak TLS (or accepts cleartext on a different port). PolarProxy terminates TLS and forwards plaintext to the backend.
     ```
     ./PolarProxy -p 198.51.100.XX,YY,YY,ZZ -cn "<TLS CN>" -o /mnt/data/pcaps/ \
       --terminate --connect 192.168.XX.2 --nosni 198.51.100.XX -v
     ```
     `-p IP,LISTEN-PORT,DECRYPTED-PORT-IN-PCAP,UPSTREAM-PORT`. `-cn` sets the dynamic CA's CN value (avoids advertising "PolarProxy" in cert metadata — useful for honeypot stealth, not directly relevant to root-ghostproxy).
   - **Reverse Proxy** (no `--terminate`) — when the backend service speaks TLS. PolarProxy decrypts, re-encrypts to the backend's TLS endpoint. Same `-p` shape but UPSTREAM-PORT == LISTEN-PORT (or whatever the backend listens on with TLS).
     ```
     ./PolarProxy -p 198.51.100.XX,YY,YY,YY -o /mnt/data/pcaps/ \
       --connect 192.168.XX.2 --nosni 192.168.XX.2 -v \
       --servercert 198.51.100.XX,192.168.XX.2:/path/to/cert.p12:12345
     ```
     `--servercert` loads a static certificate (.p12 PKCS12 format with cert+key) instead of using PolarProxy's dynamic CA. **For root-ghostproxy** this is irrelevant unless inspecting connections to specific local services with their own certs.

7. **For the transparent-bridge appliance use case, neither Termination nor Reverse mode is the natural fit.** root-ghostproxy is a forward proxy for outbound LAN-to-internet traffic — the natural mode is **Transparent Forward Proxy** (per src-polarproxy "Transparent Forward Proxy" mode #1). That mode isn't covered in detail here but the dummy-interface + tcpreplay + Suricata pattern works identically for it.

8. **Loopback iptables rules required for tcpreplay → PCAP-over-IP socket:**
   ```
   sudo iptables -A INPUT -i lo -j ACCEPT
   sudo iptables -A OUTPUT -o lo -j ACCEPT
   ```
   Or specifically for the PCAP-over-IP port: `sudo iptables -A INPUT -i lo -p tcp --dport 4430 -j ACCEPT`. For nftables (Debian 13 default), the equivalent rule must exist on the loopback chain.

9. **Filebeat ingests Suricata eve.json natively.** The ELK side of Hanke's setup is mostly orthogonal to root-ghostproxy's micro-scale (no need for Elasticsearch cluster), but the Suricata-eve-to-Filebeat module integration is reusable if the operator later wants centralized log shipping:
   ```
   sudo filebeat modules enable suricata
   ```
   Default config at `/etc/filebeat/modules/suricata.yml` already points at `/var/log/suricata/eve.json`. Filebeat then ships to whichever output (Elasticsearch, Logstash, file) is configured globally.

10. **Logstash + Slack alerting on high-severity Suricata events** — Hanke's `logstash-suricata.conf` example wires Suricata `Level 1` severity alerts to a Slack channel. Operator notes "it can be quite noisy and therefore might need further adjustments." Pattern is reusable for any Suricata-alert-to-anywhere wiring; not a Phase-1 root-ghostproxy concern.

> [!warning] What does NOT translate from Hanke to root-ghostproxy
> - The Proxmox + 254-VLANs-per-VM scaffolding is for a multi-VM honeypot. root-ghostproxy is one box bridging two segments. Skip all of: Proxmox VLAN-aware Linux Bridge, vmbr1.1, per-VLAN /30 subnet allocation, per-VM PolarProxy instance.
> - The /24 public-IP subnet assumption is honeypot-specific (each VM = a publicly routed IP). root-ghostproxy is on a private LAN; not relevant.
> - The Falco-on-VM + Auditbeat/Filebeat/Metricbeat-with-API-keys stack is honeypot endpoint-monitoring. root-ghostproxy is the sensor itself, not endpoints; skip.
> - The TShark capture-filter incantations are for excluding redundant traffic from PCAPs in the honeypot setup. Not generally needed.

## Operational scaffold notes for root-ghostproxy M005 PolarProxy + Suricata pairing

Drawing from this synthesis, the canonical setup for root-ghostproxy:

1. **Persistent dummy interface** — systemd-networkd `[NetDev]` config OR a oneshot service running `ip link add polarproxytls type dummy && ip link set polarproxytls up` on boot.
2. **PolarProxy as systemd service** — Transparent Forward Proxy mode (`-p 443,80,443` for HTTPS), `--pcapoverip 4430`, output dir `/var/log/polarproxy/` (rotated), `--bypass <chrome-bypass-list>` for cert-pinned domains, `--nontls forward` if needing to allow non-TLS through.
3. **tcpreplay bridge as systemd service** — `nc localhost 4430 | tcpreplay -i polarproxytls -t -` wrapped in a unit with `Restart=always`. Depends on PolarProxy.service being up.
4. **Suricata config** — the af-packet block lists BOTH the real-NIC interface (per chosen IPS mode) AND `polarproxytls` dummy. Distinct cluster-ids. Run as a single Suricata daemon.
5. **CA distribution** — PolarProxy's dynamic CA (or operator-supplied CA via `--cacert load`) installed as trusted root on every LAN device whose TLS gets decrypted. Document the install procedure for OS / browser / mobile.
6. **Bypass list** — start with PolarProxy's chrome-bypass list (per src-polarproxy); add operator-flagged domains (banking, healthcare).
7. **Loopback nftables rule** — allow tcp/4430 on lo for tcpreplay → PolarProxy.

**Service dependency chain for systemd:**
- `dummy-iface@polarproxytls.service` (creates the dummy interface on boot)
- `polarproxy.service` (depends on the dummy-iface; emits PCAP-over-IP)
- `polarproxy-tcpreplay.service` (depends on polarproxy; bridges to dummy interface)
- `suricata.service` (independent of the above; reads from real-NIC + dummy interface)

Order: dummy interface UP → suricata starts (it's tolerant of missing traffic) → polarproxy starts → tcpreplay bridges. Suricata picks up traffic on the dummy as soon as tcpreplay starts feeding it.

## Open Questions

- Will the dummy-interface + tcpreplay path keep up at LAN-rate throughput (~100 Mbps to 1 Gbps)? tcpreplay is single-process; the IPS mode of Suricata on the real NIC is the bottleneck most operators hit, but the tcpreplay bridge could be its own bottleneck under heavy decrypted-traffic load. Performance-test in M005 implementation.
- Does PolarProxy's free-tier 10 GB/day cap include the encrypted side or only decrypted-side bytes? Hanke writeup doesn't address this; likely product-page authoritative (src-polarproxy notes the cap is decryption-side).
- For root-ghostproxy's bridge topology, should PolarProxy run as Transparent Forward Proxy on br0's traffic (with nftables redirect tcp/443 → 10443) OR sit in path with `--connect` mode? Architectural decision tied to br0-vs-AF_PACKET-IPS choice in src-suricata-ips-mode-linux.
- ELK / SIEM is out of scope for Phase-1 (single-box appliance). For Phase-2 if shipping logs to a remote SIEM, Filebeat is the natural choice but isn't installed by default — flag as separate epic.
- Hanke's writeup uses iptables; Debian 13 defaults to nftables. nftables equivalents need to be authored; iptables-translate may help but custom rules merit hand-writing.

## Relationships

- BUILDS ON: [[src-suricata|Suricata source-synthesis (Layer 0)]]
- BUILDS ON: [[src-polarproxy|PolarProxy source-synthesis (Layer 0)]]
- BUILDS ON: [[src-suricata-install-quickstart|Suricata install + quickstart]]
- BUILDS ON: [[src-suricata-ips-mode-linux|Suricata IPS Mode for Linux]]
- BUILDS ON: [[src-suricata-yaml-config|Suricata.yaml config navigation]]
- USED BY: [[root-ghostproxy-m005-first-specialized-feature-module|M005 — First specialized feature module]] — direct pattern for Suricata + PolarProxy integration
- USED BY: [[root-ghostproxy-sfif-rollout-and-second-brain-integration-2026-05|Epic — root-ghostproxy SFIF Rollout]]

## Backlinks

[[Suricata source-synthesis (Layer 0)]]
[[PolarProxy source-synthesis (Layer 0)]]
[[Suricata install + quickstart]]
[[Suricata IPS Mode for Linux]]
[[Suricata.yaml config navigation]]
[[M005 — First specialized feature module]]
[[Epic — root-ghostproxy SFIF Rollout]]
