---
title: "Synthesis: PolarProxy TLS inspection proxy"
type: source-synthesis
domain: infrastructure
status: synthesized
confidence: high
maturity: seed
created: 2026-05-04
updated: 2026-05-04
sources:
  - id: netresec-polarproxy-product-page
    type: article
    url: "https://www.netresec.com/?page=PolarProxy"
tags:
  - polarproxy
  - tls
  - ssl-inspection
  - mitm
  - pcap
  - network-security
  - root-ghostproxy
  - module
layer: 1
---

# Synthesis: PolarProxy TLS inspection proxy

## Summary

PolarProxy is a transparent TLS/SSL inspection proxy from Netresec, designed for incident responders, malware analysts, and security researchers. It decrypts TLS traffic by acting as a man-in-the-middle (with a CA root cert that clients must trust), re-encrypts the stream toward the original destination, and writes the cleartext to a PCAP file consumable by Wireshark or any IDS. For root-ghostproxy, PolarProxy is the TLS-decryption module that sits inline on the bridge and produces the cleartext stream that Suricata then inspects — without PolarProxy, Suricata can match only on TLS handshake metadata (SNI, JA3) since the encrypted payload is opaque. PolarProxy supports eight distinct modes of operation (transparent forward, reverse, termination, in-line, mTLS, SOCKS, HAProxy, HTTP CONNECT) plus a TLS-firewall rule mode, runs as a Linux/macOS/Windows binary or Docker/Podman container, and is licensed under CC BY-ND 4.0 with a 10 GB / 10 000 sessions per day cap on the free tier.

> [!info] Source Reference
> | Attribute | Value |
> |-----------|-------|
> | Source | PolarProxy product page |
> | Type | article (vendor product page with embedded docs + FAQ) |
> | Vendor | Netresec |
> | License | CC BY-ND 4.0 (free up to 10 GB / 10 000 sessions / 10 000 rule-matches per day) |
> | Distribution | Single binary; Linux x64 / musl x64 / ARM / ARM64; macOS x64 / ARM64; Windows x64 |
> | Container | Docker + Podman supported (separate Netresec blog posts) |
> | Project URL | https://www.netresec.com/?page=PolarProxy |
> | Ingested | 2026-05-04 |

## Key Insights

> [!abstract] PolarProxy decrypts and re-encrypts; it does not modify
> Critical distinction from mitmproxy / Burp / Fiddler / Charles / Bettercap: PolarProxy is "not designed to interfere with the data inside the encrypted stream." It MITMs to inspect, then forwards the unmodified payload re-encrypted to the destination. The output is a PCAP of the cleartext, not a script-modifiable interception channel. This makes PolarProxy correct for IDS/IPS feeding (root-ghostproxy's use case) and wrong for active-attack tooling.

1. **Eight modes of operation, each with a distinct deployment shape.**
   - **Transparent Forward Proxy** — connects to external TLS servers on behalf of internal clients. Default for outbound HTTPS inspection from a malware sandbox or a network egress point. The mode for root-ghostproxy.
   - **Reverse Proxy** — connects to local TLS servers on behalf of external clients. For monitoring incoming TLS (web app receiving traffic). Uses `--leafcert load` to import server certs.
   - **TLS Termination Proxy** — terminates TLS for incoming connections, forwards application-layer cleartext to a local server. `--terminate`.
   - **Transparent In-Line Proxy** — decrypts, re-encrypts, forwards all TLS to a downstream proxy / NGFW. `--connect <host>`.
   - **mTLS Proxy** — performs mTLS handshakes with client certificates on behalf of clients lacking native mTLS support. `--clientcert DOMAINS:FILE:PWD`.
   - **SOCKS Proxy** — local SOCKS server; all TLS through it gets decrypted regardless of port. `--socks`. Combine with `--nontls allow` for non-TLS pass-through.
   - **HAProxy** — local HAProxy PROXY-protocol-v1 server. `--haproxy 7654`.
   - **HTTP CONNECT Proxy** — local HTTP-CONNECT-only proxy. `--httpconnect`.

2. **TLS Firewall mode is rule-driven.** Any of the eight modes above can run with `--ruleset FILE` (path or URL to JSON). The ruleset determines block / bypass / inspect / encrypt / terminate decisions per session — typical pairing with Transparent In-Line for an inspection appliance. This is the mode root-ghostproxy will likely run in production: inline on the bridge, with a curated ruleset that bypasses banking / healthcare / chrome-pinned domains and inspects everything else.

3. **License tiers gate volume, not features.** Free tier: 10 GB / 10 000 sessions / 10 000 rule-matches per day. Paid tiers (contact Netresec): L1 100 GB / 100 K each, L2 300 GB / 300 K each, L3 1 TB / 1 M each, Offline tier with no online license-server requirement and unlimited limits. Free vetted licenses available for security researchers / pro-bono malware analysts. **Past the free cap PolarProxy keeps forwarding TLS but stops decrypting it** — fail-open at the inspection layer, not fail-closed.

4. **Dynamic per-instance root CA generation.** PolarProxy generates a unique private CA on first run; this defends against MITM-by-impersonation if the CA from one instance leaked to another. The CA is exportable via `-x <file>` (DER) or via an HTTP server on `--certhttp <port>`. Clients trust this CA either by OS-level installation, browser-level installation, or — for centrally managed networks — Active Directory Group Policy. **The CA must be installed on every client that will have its traffic decrypted, OR the root-ghostproxy threat model accepts that untrusted clients see cert errors and won't traverse the proxy cleanly.**

5. **Three routing patterns to direct HTTPS traffic to PolarProxy.**
   - **Option 1 — PolarProxy on the gateway/firewall.** iptables `REDIRECT --to 10443` on the inside-facing interface for traffic destined to TCP/443.
   - **Option 2 — PolarProxy on a separate machine.** iptables `DNAT --to <ppx-ip>:10443` on the gateway, with optional MASQUERADE if reverse traffic doesn't pass back through the gateway.
   - **Option 3 — PolarProxy on the client PC.** iptables OUTPUT-chain redirect for a specific uid; PolarProxy must run as a different uid to avoid endless loop.

   Root-ghostproxy is Option 1 specialized: PolarProxy on the bridge appliance itself, with nftables (Debian default) instead of iptables, redirecting tcp/443 from the inside interface to a local 10443.

6. **PCAP-over-IP enables real-time downstream consumption.** Three output modes for cleartext: `-w file.pcap` (single file, no rotation), `-o directory` (hourly rotated PCAP files), `--pcapoverip [IP:]PORT` (TCP listener that streams pcap to consumers like Wireshark or NetworkMiner), and `--pcapoveripconnect HOST:PORT` (PolarProxy connects out to a remote pcap-over-IP listener). For Suricata integration, `--pcapoverip` is the canonical pattern: Suricata reads the cleartext stream live from a local TCP socket — no on-disk staging.

7. **Real-time pipe to analysis tools is supported via stdout.** `-w -` writes pcap to stdout; pipe to Wireshark with `wireshark -k -i -`, or to tcpdump/tshark, or to an arbitrary processor. For a scripted root-ghostproxy build, this enables a one-liner systemd service that pipes PolarProxy's output directly into a downstream analyzer without intermediate files.

8. **Run as systemd service or as command-line app.** Systemd wiring is documented: create system user `proxyuser`, create `/var/log/PolarProxy/`, drop the shipped `PolarProxy.service` into `/etc/systemd/system/`, `systemctl enable && start`. To bind sub-1024 ports without root: `setcap CAP_NET_BIND_SERVICE=+eip /home/proxyuser/PolarProxy/PolarProxy`.

9. **Protocol coverage is broad — anything TLS-wrapped.** Decrypts HTTPS (HTTP/1, HTTP/2, WebSocket), DNS-over-TLS (853), FTPS (990), SMTPS (465), IMAPS (993), POP3S (995), SIP-TLS (5061), MQTTS (8883). Does NOT support opportunistic STARTTLS / explicit TLS (SMTP STARTTLS, FTPS AUTH TLS, etc.) — those would need a different proxy strategy.

10. **No FIPS, no ESNI, limited Android certificate-pinning bypass.** Three operational gotchas to surface in the root-ghostproxy threat model:
    - PolarProxy uses non-FIPS-compliant crypto; will refuse to start on FIPS-enabled hosts.
    - Encrypted-SNI (ESNI / ECH) is not supported. Sessions using ESNI will not be decryptable.
    - Cert pinning on Android requires Frida-based unpinning scripts (`frida-multiple-unpinning`, `Universal Android SSL Pinning Bypass`), apk-mitm, or APK Patcher. Out of scope for a transparent network appliance unless there's a corresponding device-level deployment.

> [!warning] PolarProxy's free-tier ceiling fails OPEN, not closed
> If root-ghostproxy traffic exceeds 10 GB / 10 000 sessions / 10 000 rule-matches per day, PolarProxy stops decrypting but keeps forwarding encrypted TLS through. From a defender perspective this means inspection silently degrades; from a network-operator perspective this means the network keeps working. The implication for monitoring: alert on the rate of "TLS sessions seen vs decrypted" — divergence after the cap is the signal that a paid license is needed (or that the box is processing more traffic than design intent).

## Deep Analysis

### PolarProxy's role inside root-ghostproxy

In the operator's framing, root-ghostproxy "is basically a IPS sitting in between the Edge firewall (OPNSense) and the first switch / the local network... So its not just an IPS its a system AI safety setup project and the IPS tools (suricata and [polarproxy]) as modules." PolarProxy is one of the two named modules. Its responsibility:

- Receive TCP/443 traffic redirected from the bridge layer (nftables NAT rule).
- Terminate TLS using a per-instance dynamically generated root CA (or a pre-loaded CA via `--cacert load`).
- Re-encrypt toward the original destination.
- Emit cleartext via either rotated PCAP files or `--pcapoverip` socket.
- Optionally apply TLS-firewall rules (`--ruleset`) for block / bypass / inspect / encrypt / terminate decisions per session.

Suricata then consumes the cleartext stream — either by reading the rotated PCAPs as a capture source, or by connecting to PolarProxy's pcap-over-IP listener as a live tap. The architectural pairing PolarProxy → Suricata is the load-bearing decrypted-TLS-inspection pattern this appliance exists to deliver.

### The "intercepting all TLS" decision is a privacy decision, not just a technical one

Decrypting TLS traffic of clients on the LAN is functionally an enterprise / family / personal-network policy choice. PolarProxy makes it technically straightforward, but the deployment must account for:

- Banking, healthcare, government TLS (e.g., HSTS, Certificate Transparency, public-key pinning) — bypassing these is the right default. PolarProxy supports `--bypass <regex-file>` and `--bypassexact <file>` (exact string matching) for this.
- Apps with hard cert pinning (Chrome devices, mobile banking apps, some IoT) — these will break under inspection regardless of CA trust. Use the recommended Chrome bypass list.
- Per-user opt-in vs blanket household policy — out of scope for the proxy itself but in scope for the threat model.

### What this product page does NOT cover

The product page is Layer 0/1 (vendor description with embedded usage). Depth-verification follow-ups for root-ghostproxy work:

- A real `ruleset.json` example for the TLS-firewall mode — schema and supported match conditions need to come from Netresec's documentation or example repos, not this product page.
- Integration with Suricata documented end-to-end — the page references the third-party Hanke writeup; that writeup itself is the Layer-1 instance to ingest later.
- Performance characteristics under load — throughput, CPU/memory profile under 10/100/1000 concurrent TLS sessions, the impact of `--writeall` vs cleartext-only output.
- Container deployment specifics — Docker and Podman blog posts are referenced but not ingested here.

These are follow-up ingestions for subsequent slices of root-ghostproxy preparation.

## Operational scaffold notes for root-ghostproxy

- **Mode choice** — Transparent In-Line (`--connect`) with a TLS-firewall ruleset is the production target. For initial scaffold, Transparent Forward without ruleset is simplest.
- **Listener port** — bind to 10443; use nftables NAT to redirect 443 → 10443 on the inside bridge interface. `setcap CAP_NET_BIND_SERVICE` to avoid running as root.
- **Output** — `--pcapoverip 57012` on localhost, consumed by Suricata as live capture source. Avoids on-disk PCAP staging during normal operation; rotated `-o /var/log/polarproxy/` as a fallback for forensics.
- **CA distribution** — dynamic per-instance CA generated on first run, exposed on `--certhttp 10080` for client pickup (LAN-internal only). Document the CA install procedure for each OS used in the LAN; expect device-level cert-pinning failures on a subset of apps.
- **License path** — start free (10 GB / 10 K sessions / day). Add monitoring on decrypted-vs-seen ratio to detect when paid tier is needed.
- **Bypass list** — start with the chrome-bypass list referenced in PolarProxy docs; add banking/healthcare patterns explicitly.

## Open Questions

- Which routing pattern matches root-ghostproxy's bridge topology cleanly — nftables `redirect` on the inside bridge member, or `dnat` to a local tcp/10443? Both work; the difference is whether PolarProxy sees the original client IP or a rewritten one.
- For Suricata integration: is `--pcapoverip` (live socket) or rotated PCAP consumption (`-o`) more reliable under load? Performance-test required.
- License plan — free tier is sufficient for low-traffic LAN; paid tier required at moderate-traffic LAN (>10 GB/day). Volume estimate for the operator's network needed.
- mTLS handling for IoT devices on the LAN that authenticate to cloud services with client certs — does the current device population include any? If yes, `--clientcert` may be needed for those domains.
- ESNI / ECH adoption rate on the LAN's outbound destinations — non-decryptable sessions degrade inspection silently.

## Relationships

