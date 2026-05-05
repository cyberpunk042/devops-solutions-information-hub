---
title: "Synthesis: Suricata install + quickstart (Layer-1 instance)"
type: source-synthesis
domain: infrastructure
status: synthesized
confidence: high
maturity: seed
created: 2026-05-04
updated: 2026-05-04
sources:
  - id: suricata-docs-install
    type: documentation
    url: "https://docs.suricata.io/en/latest/install.html"
  - id: suricata-docs-quickstart
    type: documentation
    url: "https://docs.suricata.io/en/latest/quickstart.html"
tags:
  - suricata
  - install
  - quickstart
  - debian
  - ubuntu
  - layer-1
  - root-ghostproxy
  - module
  - network-security
layer: 1
---

# Synthesis: Suricata install + quickstart (Layer-1 instance)

## Summary

Distills the official Suricata 9.0.0-dev `install.html` and `quickstart.html` documentation into the concrete commands, config edits, and verification steps needed to bring up a working Suricata on Debian/Ubuntu — the path most directly applicable to root-ghostproxy's M005 Suricata module work. Where `src-suricata.md` was Layer-0 (README + repo metadata), this is Layer 1: the real `apt`/`./configure`/`make`/`systemctl` commands, the real `suricata.yaml` HOME_NET + af-packet snippets, the real test alert (SID 2100498, the ET Open canary rule), and the real `eve.json | jq` patterns. M005 design + integration can lean on this page directly without re-reading the docs site.

> [!info] Source Reference
> | Attribute | Value |
> |-----------|-------|
> | Sources | `docs.suricata.io/en/latest/install.html` + `quickstart.html` |
> | Suricata version target | 9.0.0-dev (current development); 8.0.3 cited as recent release in install docs |
> | Type | documentation (consolidated Layer-1 install + quickstart instance) |
> | Maintainer | OISF |
> | Built with | Sphinx + Read the Docs theme |
> | Ingested | 2026-05-04 |

## Key Insights

> [!abstract] Three install paths, three different control levels
> - **Binary packages** (Ubuntu PPA / Debian official+backports / RPM COPR / Arch / etc) — fastest, package-manager-managed, but Suricata version lags upstream by weeks-to-months.
> - **Source build** with `./configure && make && make install` — full control over compile flags (DPDK, GeoIP, GCC march, install paths), at the cost of manual dependency management.
> - **Auto-setup variants** — `make install-conf` (auto-creates suricata.yaml + dirs), `make install-rules` (also fetches ET Open ruleset), `make install-full` (everything, ready-to-run).

1. **Ubuntu PPA quickstart path is the simplest and most quoted.**
   ```
   sudo apt-get install software-properties-common
   sudo add-apt-repository ppa:oisf/suricata-stable
   sudo apt update
   sudo apt install suricata jq
   ```
   `jq` is recommended at install time because Suricata's eve.json output is the canonical structured output and jq is how you read it. **For Debian 13 (root-ghostproxy's host)**, the path is: Debian official packages OR backports (the PPA is Ubuntu-specific). Per Suricata install.html, the install paths split per `3.2.1` (Ubuntu PPA), `3.2.2` (Debian official+backports), `3.2.3` (RPM COPR), `3.2.4` (Arch + others). The actual Debian instructions live behind another doc page that wasn't ingested in this slice — follow-up.

2. **Minimal source-build dependencies for Debian/Ubuntu:**
   ```
   sudo apt -y install autoconf automake build-essential cargo \
     libjansson-dev libpcap-dev libpcre2-dev libtool \
     libyaml-dev make pkg-config rustc zlib1g-dev
   ```
   For RPM-based: `cargo gcc jansson-devel libpcap-devel libyaml-devel make pcre2-devel zlib-devel`. Plus `epel-release` and a `powertools` / `crb` / `codeready_builder` extra repository depending on the distro version.

3. **Default install layout when building from source:**
   - Binary: `/usr/local/bin/suricata`
   - Config: `/usr/local/etc/suricata/`
   - Logs: `/usr/local/var/log/suricata/`
   - Override with `--prefix=/usr/`, `--sysconfdir=/etc`, `--localstatedir=/var` to land FHS-standard paths (`/usr/bin/suricata`, `/etc/suricata/`, `/var/log/suricata/`) — preferable for systemd-managed packaging.

4. **Build-time flags worth knowing:**
   - `--disable-gccmarch-native` — required for portable binary (VM, multi-host fleet)
   - `--enable-geoip` — GeoIP lookups in detection
   - `--enable-dpdk` — DPDK packet capture (high-throughput); requires DPDK toolchain
   - Additional via `./configure --help` (not exhaustively documented in the ingested page)

5. **Rust dependency is mandatory.** Suricata's protocol parsers are partly Rust-implemented. Repo Rust may be too old → install from rustup directly, plus `cargo install --force cbindgen`. PATH must include `~/.cargo/bin/`.

6. **The minimum suricata.yaml edits to deploy:** HOME_NET + interface name. From quickstart `2.2`:
   ```yaml
   af-packet:
     - interface: enp1s0
       cluster-id: 99
       cluster-type: cluster_flow
       defrag: yes
       tpacket-v3: yes
   ```
   `HOME_NET` defaults already include RFC 1918 (10/8, 172.16/12, 192.168/16). For root-ghostproxy's bridge topology, the interfaces are `enp2s0` + `enp4s0` (bridged via br0); decision: monitor at the bridge level (`interface: br0`) OR at the physical interfaces individually (af-packet IPS-mode peering). Quickstart shows IDS-mode single-interface only — IPS-mode topology is in chapter 23 (not ingested in this slice). Follow-up.

7. **suricata-update is the rule-management tool.** Default `sudo suricata-update` fetches ET Open and writes to `/var/lib/suricata/rules/suricata.rules`. The default suricata.yaml's `rule-files:` entry already points at `suricata.rules`. Subsequent runs of `suricata-update` refresh; cron + systemd-timer integration is standard.

8. **The canary test alert: SID 2100498.** From ET Open ruleset, ships with default install:
   ```
   alert ip any any -> any any (msg:"GPL ATTACK_RESPONSE id check returned root";
     content:"uid=0|28|root|29|"; classtype:bad-unknown; sid:2100498; rev:7; ...)
   ```
   Trigger by `curl http://testmynids.org/uid/index.html`. Watch `/var/log/suricata/fast.log` for the alert. **For root-ghostproxy's M005 smoke test, this is the standard "is Suricata actually running and inspecting traffic" verification command — no need to invent a custom test.**

9. **Verification commands after install:**
   - `sudo suricata --build-info` — shows compile-time flags + linked libs
   - `sudo systemctl status suricata` — service state
   - `sudo tail /var/log/suricata/suricata.log` — startup log; success = "all N packet processing threads, M management threads initialized, engine started"
   - `sudo tail -f /var/log/suricata/stats.log` — runtime stats every 8s
   - `sudo tail -f /var/log/suricata/eve.json | jq 'select(.event_type=="alert")'` — alert stream as structured JSON
   - `sudo tail -f /var/log/suricata/eve.json | jq 'select(.event_type=="stats")|.stats.capture.kernel_packets'` — kernel packet counter

> [!warning] The quickstart shows IDS mode; root-ghostproxy needs IPS mode
> Quickstart's af-packet snippet (single interface, IDS-mode) does NOT cover the IPS topology root-ghostproxy needs (inline on the bridge, drop on rule match). IPS configuration lives in chapter 23 ("IPS Mode") + capture-method choice between `af-packet` IPS-peer-pairs, `nfqueue`, `netmap`. M005 Suricata-first design needs that chapter ingested as a separate Layer-1 follow-up before the design doc lands.

## Operational scaffold notes for root-ghostproxy M005

If M005 picks Suricata-first:

- **Install path decision** — Debian 13 official packages are the simplest; verify version is recent enough (Suricata 7.x+ for current rules format). If too old, build from source with `--prefix=/usr --sysconfdir=/etc --localstatedir=/var --disable-gccmarch-native` for FHS-standard layout + portable binary.
- **Rust toolchain** — confirm rustup-installed Rust + cbindgen on the build host BEFORE attempting source build.
- **suricata.yaml edits** — interface set to `br0` (or per-physical with af-packet peering, depending on M005 topology decision); HOME_NET reflects the LAN segment(s) inspected; runmode set per IPS chapter (not in this slice's ingestion).
- **Rule sync** — `suricata-update` initial run via install.sh integration; subsequent runs via systemd timer (e.g. daily at 03:00).
- **Smoke test** — SID 2100498 + `curl testmynids.org/uid/index.html` is the standard verification command.
- **IPS mode** — NOT covered by this synthesis; ingest chapter 23 of the docs before M005 design.

## Open Questions (ingestion-level, not module-level)

- Suricata IPS Mode chapter (23) — not yet ingested. M005 design blocker for Suricata-first path.
- Suricata Configuration chapter (12) — `suricata.yaml` master config schema — needed for any non-trivial deployment beyond quickstart.
- Suricata EVE JSON Output reference — schema of every event_type — needed for downstream tooling (Loki, Elasticsearch, custom log shippers).
- Debian-specific package install instructions (the doc page behind link `3.2.2`) — needed for clean install on Debian 13.
- `suricata-update` CLI reference — for non-default ruleset choices and ruleset filtering.

## Relationships

- BUILDS ON: [[src-suricata|Suricata source-synthesis (Layer 0)]] — this page is the Layer-1 instance the parent flagged as needed
- USED BY: [[root-ghostproxy-m005-first-specialized-feature-module|M005 — First specialized feature module]]
- USED BY: [[root-ghostproxy-sfif-rollout-and-second-brain-integration-2026-05|Epic — root-ghostproxy SFIF Rollout]]
- RELATES TO: [[src-polarproxy|PolarProxy synthesis]] — both are root-ghostproxy modules; install + integration paths interlock

## Backlinks

[[Suricata source-synthesis (Layer 0)]]
[[M005 — First specialized feature module]]
[[Epic — root-ghostproxy SFIF Rollout]]
[[PolarProxy synthesis]]
