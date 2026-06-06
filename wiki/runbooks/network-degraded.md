---
title: "Operator runbook — network state degraded (internet / DNS / cloudflared / tailscale / Traefik)"
type: reference
domain: ai-agents
layer: 2
status: draft
confidence: high
maturity: seed
created: 2026-05-21
updated: 2026-05-21
sources:
  - id: selfdef-sdd-026
    type: internal
    project: selfdef
    path: docs/sdd/026-operator-dashboard-and-flex-profile.md
    note: "SDD-026 Z-7 network-state surface specification"
  - id: selfdef-ms011
    type: internal
    project: selfdef
    path: backlog/milestones/MS011-operator-dashboard-and-flex-profile.md
    note: "Catalog milestone MS011 Z-7 (network state)"
  - id: selfdef-network-handler
    type: internal
    project: selfdef
    path: crates/selfdef-api/src/network.rs
    note: "selfdef-api network probe handler (5 components, per-request)"
tags: [runbook, network, internet, dns, cloudflared, tailscale, traefik, incident-response, selfdef, ips, ms011, sdd-026]
---

# Operator runbook — Network state degraded

## Summary

Operator runbook for **network state degraded (internet / DNS / cloudflared / tailscale / Traefik)**.  Anchored to: SDD-026 Z-7 network-state surface specification; Catalog milestone MS011 Z-7 (network state). Also references: selfdef-api network probe handler (5 components, per-request).

## Symptom

- `selfdefctl health` worst is `WARN` or `CRITICAL` and the `network` row is the contributor.
- `GET /v1/network` returns `{worst: "yellow"|"red", components: [...]}` with at least one component not `green`.
- Dashboard "Network state" panel shows at least one row in degraded color (yellow / red).
- One or more of: external connectivity intermittent or absent; DNS resolution slow or failing; tailscale / cloudflared / traefik services in `inactive` / `failed` state.

## Why this matters

The selfdef daemon's network surface (`/v1/network`) probes the 5 components the operator cares about for a sovereign AI workstation:

1. **internet** — reachability to a configurable external host (default `1.1.1.1`, no DNS dependency)
2. **dns** — `getent hosts <name>` against a configurable name (default `cloudflare.com`)
3. **cloudflared** — `systemctl is-active cloudflared` (Cloudflare Tunnel service unit)
4. **tailscale** — `systemctl is-active tailscaled`
5. **traefik** — `systemctl is-active traefik`

The MS011 Z-7 design rule (verbatim per SDD-026): a component the operator hasn't installed degrades to **`unknown`**, NOT to **`red`** — the panel must not lie about a component you don't have. So a `red` or `yellow` here ALWAYS means a real degradation in something the host is supposed to be providing.

## Diagnosis

```bash
# 1. Pull the structured network state from the daemon.
curl -s --unix-socket /run/selfdef.sock http://localhost/v1/network | jq

# 2. Or via the CLI / dashboard.
selfdefctl health
# In a browser: http://localhost:8443/dashboard/ (or your TCP bind)

# 3. Per-component independent verification (don't trust just the daemon's probe):
ping -c 3 -W 2 1.1.1.1                      # internet
getent hosts cloudflare.com                  # DNS
systemctl status cloudflared.service         # cloudflared
systemctl status tailscaled.service          # tailscale
systemctl status traefik.service             # traefik

# 4. If multiple components are degraded simultaneously, check upstream.
ip route show                                # default gateway sane?
ip addr show                                 # primary interface up?
cat /etc/resolv.conf                         # resolver list intact?
journalctl -p err --since "10 minutes ago"   # recent kernel / network errors?
```

## Diagnosis triage

| Pattern | Classification | Action |
|---|---|---|
| `internet` red + `dns` red + every systemd unit red | Upstream interface or default route down | `ip link`, check NIC + cabling + DHCP lease |
| `internet` red + `dns` green | Routing problem (DNS still cached); `ip route show`, check gateway | Restore default route |
| `internet` green + `dns` red | Resolver misconfig — `/etc/resolv.conf` empty, all listed servers unreachable | Fix resolver — fall back to `1.1.1.1` temporarily |
| `internet` + `dns` green, individual systemd unit red | That unit failed but rest of host is fine | `journalctl -u <unit>.service -n 50`, restart, file issue if persistent |
| `tailscale` red but operator never installed it | Operator override needed: probe is reporting a unit the operator opted out of | See override section below |

## Recovery procedures

### Internet down

```bash
# Confirm physical/virtual link state.
ip link show
# Restart networking subsystem (Debian 13).
sudo systemctl restart systemd-networkd.service
# Or with NetworkManager:
sudo systemctl restart NetworkManager.service
# Force DHCP renew on the primary interface:
sudo dhclient -r && sudo dhclient
# Verify gateway reachable:
ip route get 1.1.1.1
ping -c 3 -W 2 $(ip route | awk '/default/ {print $3; exit}')
```

### DNS resolution failing

```bash
# Inspect current resolver chain.
resolvectl status
# OR (older / minimal):
cat /etc/resolv.conf

# Try a known-good resolver directly:
dig @1.1.1.1 cloudflare.com +short
dig @8.8.8.8 cloudflare.com +short

# If systemd-resolved is in use, restart it:
sudo systemctl restart systemd-resolved.service

# If a stub-resolver is being bypassed, force it:
sudo resolvectl flush-caches
```

### cloudflared / tailscaled / traefik unit failed

```bash
# Look at the journal first — root cause is almost always there.
journalctl -u <unit>.service -n 100 --no-pager

# Common patterns:
#   "ERROR config validation failed"       → config typo; verify the unit-specific config
#   "ERROR ... no such tunnel" (cf)        → credential file mismatch; re-pull
#   "tailscale connection refused" (ts)    → tailscaled restart, then `tailscale up`
#   "address already in use" (traefik)     → port collision; check `ss -tlnp`

# Restart the unit once journal is understood:
sudo systemctl restart <unit>.service

# Persistent failure: disable + investigate.
sudo systemctl stop <unit>.service
sudo systemctl disable <unit>.service
```

## Operator override — opting out of a component

If your host does NOT run one of the 5 probed components (e.g. you don't use traefik), the probe currently shows `red` because `systemctl is-active` returns `inactive` for the missing unit. There are three operator options:

1. **Mask the unit** — `sudo systemctl mask traefik.service`. The probe will read `masked` (an unrecognized state) and classify as `unknown`, not `red`.
2. **Override the probe entirely** — set `SELFDEF_NETWORK_SKIP=traefik,cloudflared` in the daemon environment (planned operator-knob; not yet shipped — file an issue if needed).
3. **Accept the yellow** — leave the probe honest about what's missing. Operator visibility is the point of MS011 Z-7.

Recommend option 1 (mask) for permanent opt-outs.

## Log the incident

If the degradation is a real outage rather than a misconfig:

```bash
cat > "raw/notes/$(date +%F)-network-degraded.md" <<EOF
# Network degraded — $(date +%F)

Operator: <handle>
Components red: <list>
Components yellow: <list>
Root cause: <upstream ISP / resolver / unit-specific>
Duration: <start time> → <end time>
Action taken: <restart unit / DHCP renew / failover / etc>
Follow-up: <vendor escalation / nothing / monitoring tweak>
EOF
```

## Relationships

### Cross-references

- SDD-026 § Z-7 (network state surface specification)
- MS011 catalog rows on Z-7 (M00276 dashboard tab Network)
- Sister runbook: [`storage-degraded`](storage-degraded.md) (parallel pattern for filesystem fill)
- Sister runbook: [`ux-coherence-failures`](ux-coherence-failures.md) (when the coherence harness fails because of a network probe drift)
- selfdef code: `crates/selfdef-api/src/network.rs` (probe implementation, 5 components, per-request)
- selfdef code: `dashboard/app.js::refreshNetwork()` (frontend consumer)
