---
title: "Synthesis: Suricata IDS/IPS/NSM engine"
type: source-synthesis
domain: infrastructure
status: synthesized
confidence: high
maturity: seed
created: 2026-05-04
updated: 2026-05-04
sources:
  - id: oisf-suricata-readme
    type: documentation
    url: "https://github.com/OISF/suricata"
tags:
  - suricata
  - ids
  - ips
  - nsm
  - network-security
  - root-ghostproxy
  - module
layer: 1
---

# Synthesis: Suricata IDS/IPS/NSM engine

## Summary

Suricata is an open-source network IDS, IPS, and NSM (Network Security Monitoring) engine maintained by the Open Information Security Foundation (OISF). It inspects live traffic or PCAP files against a signature ruleset, generates alerts, and — in IPS mode — actively drops or rejects flows that match malicious patterns. For root-ghostproxy, Suricata is the IPS module that consumes traffic from the transparent L2 bridge, applies signature-based detection (TLS, HTTP, DNS, SMB, and many more app-layer protocols), and either alerts (IDS mode) or blocks (IPS mode). Its high-stakes failure surface — IPS crashes can knock a network offline, missed detections allow undetected compromise — drives an extensive multi-stage QA process that this synthesis captures so the root-ghostproxy build has explicit visibility into what "Suricata as a module" means operationally.

> [!info] Source Reference
> | Attribute | Value |
> |-----------|-------|
> | Source | OISF/suricata GitHub repository |
> | Type | documentation (README + 6 deep-fetch files) |
> | Maintainer | Open Information Security Foundation (OISF) |
> | License | GPL-2.0 |
> | Project home | https://suricata.io |
> | User guide | https://docs.suricata.io |
> | Bug tracker | https://redmine.openinfosecfoundation.org/projects/suricata |
> | Forum | https://forum.suricata.io |
> | Ingested | 2026-05-04 |

## Key Insights

> [!abstract] Three operational roles in one engine
> Suricata is simultaneously an IDS (passive detection + alerting), an IPS (inline blocking), and an NSM platform (flow logging, app-layer metadata, file extraction). For root-ghostproxy the relevant mode is IPS — inline on the bridge between OPNsense and the LAN — but the IDS and NSM outputs (eve.json, fast.log, files/) remain valuable observability artefacts even when blocking is the primary purpose.

1. **High-stakes failure surface drives an unusually extensive QA process.** OISF explicitly enumerates three failure classes: an IPS crash can knock a network offline, a passive-IDS compromise leaks critical data, and missed detections allow undetected compromise. This framing matters for root-ghostproxy because Suricata sits inline on the bridge and a crash takes the whole inspected segment down — bypass logic in the bridge layer (failopen vs failclosed) is therefore not a "nice-to-have" but a deployment-defining choice.

2. **Multi-stage QA: GitHub-CI + community review + private QA + Coverity.** Pull requests pass through automated CI checks, then human review by team and community, then private OISF QA setups (kept private because the test traffic itself is sensitive), and post-merge Coverity Scan submissions limited to one per day by the free-tier service. Means: contributing custom rules or custom output modules upstream is a multi-week-to-multi-month process; for time-sensitive root-ghostproxy customizations, the path is local rule files and local C/Lua modules, not upstream PRs.

3. **QA acceptance tests cover build, static analysis, runtime analysis, regression, and traffic-replay.** Routine acceptance includes: builds across multiple OS / compiler / optimization-level matrices, cppcheck + scan-build static analysis, valgrind + ASAN + LSAN runtime analysis, regression suite for past bugs, output validation, unix-socket testing, pcap fuzz testing, and traffic-replay-based IDS+IPS tests. Manual escalation tests cover multi-gigabit traffic replay, multi-terabyte pcap collection processing, fuzz runs measured in days/weeks, and live performance tests.

4. **Reserved Signature ID (SID) ranges are pre-allocated per protocol/component.** The repo's `rules/README.md` reserves 1000 SIDs per component or app-layer protocol — Decoder 2200000–2200999, Stream 2210000–2210999, HTTP 2221000–2221999, TLS 2230000–2230999, DNS 2240000–2240999, etc. Custom local rules for root-ghostproxy must use SIDs OUTSIDE these reserved ranges (typically 1000000–1999999 for local/site-specific rules per the broader ET/Snort convention) to avoid collisions with upstream signature updates.

5. **Severity-tiered security policy with a 4-level support taxonomy.** SECURITY.md defines CRITICAL (Tier-1, default-on, traffic-triggerable RCE/crash/evasion → kept private + immediate release across all supported versions), HIGH (lower-risk Tier-1 or Tier-2/Community → kept private up to ~1 month), MODERATE (Tier-2/Community, not default → rolled into next release), and LOW (CLI utilities, unlikely configurations → fixed in development versions). Code areas are classified Tier 1 / Tier 2 / Community / Unmaintained — only Tier 1 carries the strongest support guarantees. For root-ghostproxy this means: lean on Tier-1 features (default-on app-layer parsers, default rule loaders) and treat Community/Unmaintained features as "investigate but do not depend on."

6. **App-layer protocol coverage is broad.** Reserved SID ranges enumerate the protocols Suricata parses natively: SMTP, HTTP, NTP, NFS, IPsec, SMB, Kerberos, DHCP, SSH, MQTT, TLS, QUIC, FTP, POP3, LDAP, DNS, PGSQL, mDNS, MODBUS, DNP3, HTTP/2. For an inline appliance this is foundational — the engine sees not just IP/TCP but the application-layer semantics, enabling rules that match on HTTP request headers, TLS SNI, DNS queries, etc.

7. **Library mode (libsuricata) supports embedding.** The repo ships three example library integrations: `examples/lib/custom/` (custom packets and threads), `examples/lib/live/` (live capture with custom packet handling, supports up to 16 interfaces simultaneously, separate worker thread per interface), `examples/lib/simple/`. Embedding pattern: `make install-library && make install-headers`, then build against `libsuricata-config`. This matters for advanced root-ghostproxy module designs where Suricata is invoked programmatically rather than as a standalone daemon — but for the initial scaffold the daemon mode is canonical.

8. **CLA required for upstream contribution.** OISF requires a contributor license agreement to keep ownership consolidated under the foundation (see http://suricata.io/about/contribution-agreement/). Means: any patches, custom output plugins, or rule format extensions intended for upstream merge must go through CLA signing first.

> [!warning] In IPS mode a Suricata crash takes the inspected segment offline
> Source statement: "in IPS mode a crash may knock a network offline." For root-ghostproxy this is the load-bearing operational risk. The bridge layer (br0 + ebtables/nftables) MUST have a failopen mechanism — either kernel-level (bridge continues forwarding when Suricata is dead) or systemd-orchestrated (watchdog flips bridge to direct-forward on Suricata exit) — or downtime of the box equals downtime of the LAN. This is a scaffold-stage architectural decision, not a feature-stage detail.

## Deep Analysis

### Suricata's role inside root-ghostproxy

Operator framing (verbatim from prior session): root-ghostproxy "is basically a IPS sitting in between the Edge firewall (OPNSense) and the first switch / the local network... So its not just an IPS its a system AI safety setup project and the IPS tools (suricata and [polarproxy]) as modules." Suricata is one of the two named modules. Its job in this architecture:

- Receive packets from the L2 bridge (br0 with enp2s0 + enp4s0 as members).
- Apply rule-based detection at the IDS/IPS engine — both default-shipped community rules (Emerging Threats Open ruleset is the typical default) and any local rules authored for root-ghostproxy's specific threat model.
- Emit alerts via `eve.json` (structured JSON, the canonical output for downstream tooling) and `fast.log` (legacy text format).
- In IPS mode, drop / reject flows matching `drop` or `reject` rules.
- Optionally extract files from HTTP/SMTP traffic for downstream malware analysis.

PolarProxy (the second module) handles a different problem: it terminates and re-encrypts TLS so that the resulting cleartext can be inspected. Suricata does NOT decrypt TLS — it can match on TLS handshake metadata (SNI, JA3 hash, certificate issuer), but the encrypted payload is opaque. The architectural pairing is therefore: PolarProxy decrypts → writes PCAP-over-IP or local PCAP → Suricata reads that PCAP as one of its capture sources. This is the "Sniffing Decrypted TLS Traffic with Security Onion" / "Capturing Decrypted TLS Traffic with Arkime" pattern referenced in the PolarProxy docs and corroborated by the third-party writeup on forwarding decrypted TLS from PolarProxy to Suricata (Nils Hanke's honeypot+IDS+ELK setup).

### Build/QA implications for root-ghostproxy

The QA framing tells us that production Suricata is hardened by extensive automated and manual testing — meaning the stable releases are reliable in supported configurations. Untested or self-hacked builds (custom flags, out-of-tree patches, experimental rule formats) lose this guarantee. For root-ghostproxy the path of least operational risk is:

1. Use distribution packages (Debian's suricata package) for the engine binary, OR build from a tagged release via the upstream documented build instructions.
2. Custom logic (site rules, custom output handlers) goes in clearly separated config files and rule directories — never in patches against the engine source.
3. Every Suricata release upgrade in root-ghostproxy gets verified against a baseline pcap replay before going live (the same pattern OISF uses upstream, scaled to the appliance).

### What this README does NOT cover

A README is Layer 0 (description). The depth-verification rule says synthesis must reach Layer 1 (instance). This README does not include — and root-ghostproxy work will need from `https://docs.suricata.io` directly:

- Concrete `suricata.yaml` configuration (the master config). The README references the engine but the actual configuration surface lives in the user guide.
- The eve.json output format and the per-event-type schemas (alert, anomaly, http, dns, tls, flow, fileinfo).
- IPS-specific configuration (afpacket vs nfqueue vs netmap capture, drop/reject rule syntax, hardware offload caveats).
- Rule language reference (suricata-rules format, content/pcre/dsize/byte_test/etc., flow keywords, app-layer keywords).
- Performance tuning (CPU pinning, runmodes, packet acquisition methods, buffer sizing).

These are follow-up ingestions for subsequent slices of root-ghostproxy preparation.

## Open Questions

- Which Suricata version does the root-ghostproxy box currently have installed (or plan to install)? Debian 13 trixie ships a specific package version; upstream is likely ahead. Verification needed when the suricata module work begins.
- IPS deployment method on the box: af-packet IPS mode (peer-paired interfaces) vs nfqueue (netfilter integration) vs netmap (zero-copy)? This is a function of the bridge topology + kernel features available on Debian 13. Open architectural decision.
- Failopen mechanism for the bridge layer when Suricata is down — kernel-level vs systemd-watchdog vs explicit nftables fallback rules. Scaffold-stage decision.
- Local rule SID range allocation policy for root-ghostproxy. The reserved upstream ranges are documented; the project's own range is not yet decided.
- Default ruleset choice: ET Open (free), ET Pro (paid), Talos (paid), or a custom curation?
- Integration with PolarProxy for decrypted-TLS inspection: PCAP file polling, PCAP-over-IP socket, or a tee from PolarProxy's pcapoverip listener? Performance and reliability differ.

## Operational scaffold notes for root-ghostproxy

These notes feed directly into the Suricata module's scaffold-stage decisions; they are NOT implementation, only the surface to be made explicit before any engine config lands on the box:

- **Capture-method decision** — `af-packet` IPS mode with peer interfaces is the typical Linux IPS pattern; `nfqueue` integrates with netfilter rules; `netmap` is highest-throughput but requires kernel/driver support. The bridge topology (br0 with enp2s0 + enp4s0 already members) constrains the choice — `af-packet` peering would short-circuit the bridge, so `nfqueue` (queue traffic out of the bridge into Suricata) is the architecturally cleaner path on a transparent bridge appliance. Verification needed against current kernel + driver capabilities.
- **Rule directory layout** — separate `rules/upstream/` (ET Open or chosen vendor ruleset, replaced wholesale on update), `rules/local/` (root-ghostproxy site rules with SIDs in 1000000–1999999), and `rules/disabled/` (rules pinned off due to known false positives in this network). Suricata's `suricata.yaml` rule-files list orders these so local/upstream precedence is explicit.
- **Output sink** — `eve.json` rotated daily, shipped to a downstream collector (Loki, Elasticsearch, or a local SQLite via a sidecar). Local rotation policy on the box must cap disk usage (`logrotate` config), since IPS appliances generate large per-day eve volumes.
- **Update cadence** — rule updates daily (suricata-update with the configured sources); engine updates only on tagged-release verification. Distinguish these two upgrade paths in systemd timers / IaC.
- **Verification artefact** — every config change is replayed against a baseline pcap (clean traffic + a known-malicious pcap) before activation. The OISF QA pattern, scaled to the appliance.

## Relationships

