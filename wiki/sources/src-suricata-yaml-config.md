---
title: "Synthesis: Suricata.yaml master configuration (navigation + key sections)"
type: source-synthesis
domain: infrastructure
status: synthesized
confidence: medium
maturity: seed
created: 2026-05-04
updated: 2026-05-04
sources:
  - id: suricata-docs-config-yaml
    type: documentation
    url: "https://docs.suricata.io/en/latest/configuration/suricata-yaml.html"
tags:
  - suricata
  - suricata-yaml
  - configuration
  - layer-1
  - root-ghostproxy
  - module
  - navigation
layer: 1
---

# Synthesis: Suricata.yaml master configuration

## Summary

Maps the Suricata.yaml master configuration chapter (chapter 12.1 of docs.suricata.io, with sub-sections 12.1.1 through 12.1.22 plus parallel chapters 12.2 through 12.9). The chapter is too large for a single source-synthesis (the raw scrape is ~43K tokens) — this page therefore acts as a **navigation map** plus concrete coverage of the highest-priority sections for root-ghostproxy M005 module work: action-order semantics, event output, threading, packet acquisition, application-layer parsers (especially TLS), and security hardening (drop privileges + Landlock LSM). Sections covered in depth elsewhere or deferred to per-section ingestions are flagged.

> [!info] Source Reference
> | Attribute | Value |
> |-----------|-------|
> | Source | docs.suricata.io chapter 12.1 (Suricata 9.0.0-dev) |
> | Type | documentation (master config schema, navigation-style synthesis) |
> | Maintainer | OISF |
> | Format | YAML 1.1 (the file starts with `%YAML 1.1`) |
> | Companion sub-chapters | 12.2 Global-Thresholds · 12.3 Exception Policies · 12.4 Snort→Suricata · 12.5 Multi-Tenancy · 12.6 Dropping Privileges · 12.7 Landlock LSM · 12.8 systemd notification · 12.9 Includes |
> | Ingested | 2026-05-04 (raw too large for single read; navigation synthesis only) |

## Section Map (the 22 sub-sections of 12.1)

| § | Topic | M005 priority | Notes |
|---|---|---|---|
| 12.1.1 | max-pending-packets | low | Throughput vs RAM trade-off; default 1024. Scale up if multi-CPU + idle cores observed. |
| 12.1.2 | Runmodes | **HIGH** | Default `autofp`; alternatives via `--list-runmodes`. IPS vs IDS choice + interaction with capture method. |
| 12.1.3 | default-packet-size | low | Default 1514. Larger packets still processed (slower). |
| 12.1.4 | User and group | medium | `run-as: { user: suri, group: suri }` for privilege drop. |
| 12.1.5 | PID file | low | `/var/run/suricata.pid` in daemon mode. Multiple instances need distinct paths. |
| 12.1.6 | **action-order** | **HIGH** | The 4 actions: pass / drop / reject / alert. Order determines which fires first when multiple signatures match. Default: `pass, drop, reject, alert`. **For root-ghostproxy IPS this is load-bearing** — drop before reject before alert. |
| 12.1.7 | Packet alert queue | medium | Engine-behaviour impact + discarded/suppressed alert stats. |
| 12.1.8 | Splitting config in multiple files | medium | Useful for environment-specific overlays. |
| 12.1.9 | **Event output** | **HIGH** | Default logging dir, stats, fast.log, EVE JSON, tls.log, http.log, pcap-log, alert-debug.log, syslog, file-store. **EVE (12.1.9.5) is the canonical structured output.** |
| 12.1.10 | Detection engine | medium | Inspection config, prefilter engines, thresholding, pattern-matcher tuning. |
| 12.1.11 | **Threading** | **HIGH** | cpu-affinity for IDS mode (12.1.11.1) vs IPS mode (12.1.11.2); interface-specific affinity (12.1.11.3); automatic NUMA-aware pinning (12.1.11.4). |
| 12.1.12 | IP defrag | medium | Disabled in some IPS modes (AF_PACKET multi-thread sans eBPF). |
| 12.1.13 | Flow and stream handling | **HIGH** | Flow settings, timeouts, stream-engine. `stream.inline: yes` is the IPS-mode requirement (per IPS Mode chapter). |
| 12.1.14 | Host tracking | low | |
| 12.1.15 | **Application Layer Parsers** | **HIGH** | FTP, HTTP/libhtp, SMB, DCERPC, HTTP/2, **SSL/TLS (12.1.15.7)**, SSH, Modbus, MQTT, SMTP. SSL/TLS section is critical for PolarProxy-decrypted-stream integration. |
| 12.1.16 | Engine logging | medium | Engine internal logging (NOT alert/event output) — for debugging. |
| 12.1.17 | **Packet Acquisition** | **HIGH** | DPDK · Pf-ring · NFQ · Ipfw. The capture-method config that pairs with the IPS mode chosen in chapter 23. |
| 12.1.18 | **Rules** | **HIGH** | Rule files (default `suricata.rules`), threshold file, classifications, rule-vars, host-os-policy. |
| 12.1.19 | Engine analysis and profiling | low | Performance-debugging features. |
| 12.1.20 | Decoder | medium | Teredo, VXLAN, recursion-level. |
| 12.1.21 | Advanced options | low | Stacktrace toggles. |
| 12.1.22 | **Configuration hardening** | **HIGH** | Lua restrictions, security-relevant toggles. |

| Sub-chapter | Topic | M005 priority |
|---|---|---|
| 12.2 | Global-Thresholds | medium |
| 12.3 | Exception Policies | medium |
| 12.4 | Snort.conf → Suricata.yaml | low |
| 12.5 | Multi-Tenancy | low (single appliance) |
| 12.6 | **Dropping Privileges After Startup** | **HIGH** |
| 12.7 | **Using Landlock LSM** | **HIGH** (Linux 5.13+ filesystem sandboxing) |
| 12.8 | systemd notification | medium (used by the systemd unit) |
| 12.9 | Includes | medium (config splitting) |

## Key Insights

### 1. Action-order (12.1.6) — load-bearing for IPS semantics

Suricata supports four actions per signature:

| Action | Effect | Notes |
|---|---|---|
| **pass** | Stop scanning packet, skip remaining rules. On TCP, entire flow is passed but flow details still logged. | Whitelisting / explicit allow. |
| **drop** | IPS/inline only. Signature matches → packet not forwarded. **No notice to receiver** → typically results in TCP timeout. Alert generated. | The hammer. For known-bad. |
| **reject** | Active rejection. Both endpoints receive a reject packet (TCP RST or ICMP error). In IPS mode, packet is also dropped. Alert generated. | Cleaner than drop for legitimate clients accidentally caught. |
| **alert** | Packet treated as benign (forwarded normally), but alert is logged. | Pure IDS; the default. |

The **action-order** setting determines which action fires when multiple matching rules disagree. Default: `pass → drop → reject → alert`. Rules are LOADED in file order but PROCESSED by signature priority. **For root-ghostproxy** the default order is sane: explicit pass-rules win (whitelist), then drops (block known-bad), then rejects (clean reject for legitimate-looking misbehavior), then alerts (purely passive).

### 2. Event output (12.1.9) — EVE is the canonical structured format

The chapter enumerates 12 output sinks. Production-relevant ones:

- **fast.log** — line-based, human-readable, legacy. One-line-per-alert.
- **EVE JSON (12.1.9.5)** — Extensible Event Format, JSON Lines. The canonical output for downstream tooling (SIEM, log shippers, custom analyzers). Per-event-type streams (alert, anomaly, http, dns, tls, flow, fileinfo, stats, etc.).
- **stats** — engine statistics every 8s by default. Aliased into eve.json `event_type=stats`.
- **tls.log / http.log / alert-debug.log** — protocol-specific text logs. Use eve.json instead for structured.
- **pcap-log** — periodic packet captures (NOT decrypted). Useful for forensics.
- **file-store (12.1.9.12)** — extracted files from HTTP/SMTP/etc traffic, for downstream malware analysis.

For root-ghostproxy: **enable EVE JSON output, disable redundant text logs**. Pair eve.json with logrotate (per src-suricata operational scaffold notes) for disk discipline.

### 3. Threading (12.1.11) — IDS mode and IPS mode have different affinity needs

Two distinct cpu-affinity profiles:
- **IDS mode** (12.1.11.1) — packet workers + management thread; explicit pinning for low-jitter inspection.
- **IPS mode** (12.1.11.2) — typically more cores per worker because copy-mode adds latency on the packet path; affinity helps cache locality.
- **Interface-specific** (12.1.11.3) — different interfaces get different worker pools.
- **NUMA-aware automatic pinning** (12.1.11.4) — for multi-socket hosts; root-ghostproxy is single-socket so this section is moot.

### 4. SSL/TLS application-layer parser (12.1.15.7) — the PolarProxy integration touch-point

The TLS parser sees TLS handshake metadata even on encrypted streams (SNI, JA3 fingerprint, certificate chain, protocol version). When PolarProxy supplies a decrypted PCAP/PCAP-over-IP stream, the TLS parser sees the cleartext as if it were native HTTP/HTTP2/etc. The `tls.log` output (12.1.9.6) captures TLS-handshake events specifically; for the decrypted-stream case, those events come from the encrypted leg AND the decrypted leg gets HTTP/SMTP/etc parser coverage. For M005 PolarProxy + Suricata pairing, the TLS parser config needs no special handling — it's about which TLS features are tracked, not about whether decryption is on.

### 5. Packet acquisition (12.1.17) — must align with the IPS mode chosen in chapter 23

This section configures: DPDK, Pf-ring, NFQ (for nfqueue-based IPS), Ipfw (BSD only). The chapter does NOT cover AF_PACKET in this section — AF_PACKET config is at the YAML root (per the IPS Mode chapter and quickstart examples). The capture-method choice in chapter 23 determines which sub-section here is in play:
- IPS mode = **NFQUEUE** → fill in 12.1.17.3 NFQ config.
- IPS mode = **AF_PACKET** → fill in root-level `af-packet:` block.
- IPS mode = **DPDK** → fill in 12.1.17.1 DPDK config.

### 6. Configuration hardening (12.1.22) — Lua restrictions

Lua support (chapter 16) lets rules call out to Lua scripts. 12.1.22.1 documents how to restrict Lua's available APIs (filesystem access, network access, etc.) to prevent rule-author privilege escalation. **For root-ghostproxy**: disable Lua entirely unless a specific use case justifies it (Lua adds attack surface; the appliance is OS-setup-tier, simpler is better).

### 7. Privilege drop + Landlock LSM (12.6 + 12.7) — defense-in-depth

After startup, Suricata runs as a non-root user (configured via `run-as` in 12.1.4). 12.6 documents the privilege-drop mechanism. 12.7 enables Linux Landlock LSM (kernel 5.13+) for filesystem sandboxing — restricts which directories Suricata can read/write even if compromised. **For root-ghostproxy on Debian 13** (kernel 6.12+): Landlock IS available; enabling it is a Phase-2 hardening win. Phase-1 acceptance is privilege-drop only.

## Operational scaffold notes for root-ghostproxy M005

- Phase-1 minimum suricata.yaml edits (in priority order):
  1. **12.1.2 runmode** — set to `workers` for IPS mode (per IPS Mode chapter recommendation), or `autofp` for IDS-default.
  2. **12.1.6 action-order** — keep default unless specific reason.
  3. **12.1.9.5 EVE** — enable; disable fast.log + tls.log + http.log to reduce duplication.
  4. **12.1.11 threading** — set cpu-affinity per the host's CPU count; pin worker cores away from management.
  5. **12.1.13.3 stream.inline** — `yes` (required for IPS mode per chapter 23).
  6. **12.1.17 packet acquisition** — NFQ block IF Phase-1 nftables-NFQUEUE chosen; else AF_PACKET block IF Phase-2 Layer-2 inline chosen.
  7. **12.1.18 rules** — `rule-files` lists `suricata.rules` (auto-managed by suricata-update).
  8. **12.6 drop privileges** — `run-as: { user: suricata, group: suricata }` (Debian package usually pre-creates the user).
  9. **12.1.22 hardening** — disable Lua unless needed.

- Phase-2 hardening:
  - Enable 12.7 Landlock LSM.
  - Tune 12.1.10 detection-engine prefilter settings for throughput.
  - Tune 12.1.11.4 NUMA-aware affinity if multi-socket host appears.

## Open Questions

- The 22 sections are too dense for a single synthesis; this page is navigation-only. Per-section deeper Layer-1 syntheses warranted before specific config edits land:
  - EVE JSON output schema (per event_type) — the structured-log contract for downstream tooling.
  - Application-layer parser tuning (HTTP libhtp options especially — cookie length limits, request-line length, etc., relevant for malware inspection).
  - Threading/cpu-affinity examples for the specific host CPU count.
  - Rule format reference (rule-files / classifications / metadata).
  - Performance chapter (chapter 11) for tuning patterns.
- Does Debian 13's `suricata` package ship a pre-tuned `/etc/suricata/suricata.yaml` that aligns with package conventions (run-as user, log dirs, etc.)? Verify before authoring custom edits.

## Relationships

- BUILDS ON: [[src-suricata|Suricata source-synthesis (Layer 0)]]
- BUILDS ON: [[src-suricata-install-quickstart|Suricata install + quickstart]]
- BUILDS ON: [[src-suricata-ips-mode-linux|Suricata IPS Mode for Linux]] — packet acquisition section pairs with IPS mode chapter
- USED BY: [[root-ghostproxy-m005-first-specialized-feature-module|M005 — First specialized feature module]]
- USED BY: [[root-ghostproxy-sfif-rollout-and-second-brain-integration-2026-05|Epic — root-ghostproxy SFIF Rollout]]

## Backlinks

[[Suricata source-synthesis (Layer 0)]]
[[Suricata install + quickstart]]
[[Suricata IPS Mode for Linux]]
[[M005 — First specialized feature module]]
[[Epic — root-ghostproxy SFIF Rollout]]
