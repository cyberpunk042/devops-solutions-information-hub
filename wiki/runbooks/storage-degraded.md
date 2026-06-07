---
title: "Operator runbook — Storage state degraded (filesystem fill, log dir bloat)"
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
    note: "SDD-026 Z-10 storage state surface specification"
  - id: selfdef-ms011
    type: internal
    project: selfdef
    path: backlog/milestones/MS011-operator-dashboard-and-flex-profile.md
    note: "Catalog milestone MS011 Z-10 (filesystem usage + log dirs)"
  - id: selfdef-storage-handler
    type: internal
    project: selfdef
    path: crates/selfdef-api/src/storage.rs
    note: "selfdef-api storage probe handler (df + log-dir walk)"
tags: [runbook, storage, filesystem, df, logs, log-rotate, incident-response, selfdef, ips, ms011, sdd-026]
---

# Operator runbook — Storage state degraded

## Summary

Operator runbook for **Storage state degraded (filesystem fill, log dir bloat)**.  Anchored to: SDD-026 Z-10 storage state surface specification; Catalog milestone MS011 Z-10 (filesystem usage + log dirs). Also references: selfdef-api storage probe handler (df + log-dir walk).

## Symptom

- `selfdefctl health` worst is `WARN` or `CRITICAL` and the `storage` row is the contributor.
- `GET /v1/storage` returns at least one mount with `state` `yellow` (used 70-89 %) or `red` (used ≥ 90 %).
- Dashboard "Storage state" panel shows the offending mount with its used-pct as the aggregate label.
- Sustained log dir growth: `/var/log/selfdef/`, `/var/cache/selfdef/`, or `/var/lib/selfdef/` consuming surprising disk.

## Why this matters

When a mount hits ≥ 90 % the daemon's own audit chains (perimeter, guardian, scheduler — each `append(true)` to `/var/log/selfdef/*.ocsf.jsonl`) start failing to append, which:

1. **Breaks the chain integrity invariant** — the next event's `prev_event_sha256` references the last event that successfully landed, so a write failure here is recoverable, BUT
2. **Costs operator visibility** — Sigkill verdicts (MS047 perimeter), supervisor events (MS044 guardian), routing decisions (MS048 scheduler) are dropped on the floor until the disk recovers. These are exactly the moments the daemon's incident-response capability needs to be working.

The selfdef thresholds (per `crates/selfdef-api/src/storage.rs::classify_used_pct`):
- `< 70 %`  → **green** (healthy)
- `70-89 %` → **yellow** (operator warning — investigate before it gets worse)
- `≥ 90 %`  → **red** (impending audit-chain write failure)

## Diagnosis

```bash
# 1. Pull the structured storage state from the daemon.
curl -s --unix-socket /run/selfdef.sock http://localhost/v1/storage | jq

# 2. Or via the CLI:
selfdefctl health   # composite — includes storage row

# 3. Per-mount usage independent verification:
df -h
df -h /var/log/selfdef /var/cache/selfdef /var/lib/selfdef

# 4. Top consumers under each selfdef-managed dir:
du -sh /var/log/selfdef/* 2>/dev/null | sort -h
du -sh /var/cache/selfdef/* 2>/dev/null | sort -h
du -sh /var/lib/selfdef/* 2>/dev/null | sort -h

# 5. Look for runaway logs:
find /var/log -size +100M -mtime -7 -ls 2>/dev/null

# 6. ZFS-specific (if /var/log/selfdef is on a ZFS dataset):
zpool list
zfs list -o name,used,avail,refer
```

## Diagnosis triage

| Pattern | Classification | Action |
|---|---|---|
| One specific dataset/mount at ≥ 90 % | Targeted issue on that mount | See dataset-specific recovery below |
| Multiple mounts climbing together | Likely whole-pool issue (ZFS pool low on space) | `zpool list`, `zfs list`; consider snapshot pruning |
| `/var/log/selfdef/` is the heavy consumer | Daemon writing faster than logrotate clears | Check logrotate config; consider rotation cadence change |
| `/var/log/selfdef/` heavy + Sigkill verdicts very frequent | Operator-side attack/misconfig flooding the perimeter | See sister runbook `perimeter-sigkill-investigation.md` |
| `/var/cache/selfdef/` growing without bound | Ring-buffer not being trimmed | Check `selfdef.toml` ring-buffer caps |
| `/var/lib/selfdef/state.sqlite` huge | Hot-event store wasn't migrated to cold storage | Run `selfdefctl events archive` (operator-driven) |
| Whole disk full + nothing in `/var` is the culprit | Look elsewhere — `du -sh /*` to find it | Investigate root, /home, etc. |

## Recovery procedures

### 1. Free space immediately on a single mount

```bash
# Preview what's eating the mount:
ncdu /<mountpoint>   # if installed
# OR fallback:
du -h -d 2 /<mountpoint> 2>/dev/null | sort -h | tail -20

# Common emergency recovery moves:
sudo journalctl --vacuum-size=200M       # cap systemd journal at 200 MB
sudo apt clean                           # clear apt cache
sudo find /var/log -name "*.gz" -mtime +14 -delete   # old rotated logs
sudo docker system prune                 # if docker is installed
```

### 2. selfdef log dir bloat

```bash
# Inspect logrotate config:
cat /etc/logrotate.d/selfdef 2>/dev/null   # may not be shipped yet
# Force a rotation pass:
sudo logrotate -f /etc/logrotate.conf

# Manually trim selfdef logs that aren't covered by logrotate:
sudo mv /var/log/selfdef/old-events.jsonl.bak{,.$(date +%s)}   # archive aside
sudo systemctl reload selfdefd.service   # daemon re-opens its log fd

# DO NOT truncate audit-chain files (perimeter/guardian/scheduler
# .ocsf.jsonl) in place — that breaks the chain integrity invariant.
# Use the rotation procedure from the matching *-audit-log-corruption
# runbook instead (Option B: rotate aside, start a new chain).
```

### 3. ZFS pool nearly full (if applicable)

```bash
# Recent snapshots may be holding space that's no longer referenced.
zfs list -t snapshot -o name,used,creation -s creation

# Destroy old snapshots cautiously (operator-confirmed):
sudo zfs destroy <pool>/<dataset>@<snap-name>

# If a dataset has reservation/refreservation that's now excessive:
zfs get reservation,refreservation <dataset>
```

### 4. Verify the alert clears

```bash
# After the recovery action, re-probe.
curl -s --unix-socket /run/selfdef.sock http://localhost/v1/storage | \
  jq '.worst, .mounts[] | select(.state != "green")'

# Should see worst="green" and the offending mount returned to <70%.
selfdefctl health   # composite should clear
```

## Operator decision tree

- **Filling because of legitimate growth** (model checkpoints, datasets, training runs): expand the pool/disk; don't keep trimming logs to compensate. Storage was sized too small.
- **Filling because of attack noise** (e.g. perimeter Sigkill verdicts at sustained rate): see `perimeter-sigkill-investigation.md`. The disk isn't the problem; the attack is.
- **Filling because of an exporter/integration loop** (e.g. observability module re-importing the same metrics): disable the misbehaving integration; file an issue.
- **Filling because logrotate is broken**: that's a packaging bug — file an issue against the selfdef-daemon postinst.

## Log the incident

```bash
cat > "raw/notes/$(date +%F)-storage-degraded.md" <<EOF
# Storage degraded — $(date +%F)

Operator: <handle>
Mount(s) red: <list with used_pct values>
Mount(s) yellow: <list>
Top consumers identified: <paths + sizes>
Root cause: <legitimate growth / log bloat / attack / integration loop / etc>
Action taken: <vacuum journal / rotate logs / destroy ZFS snapshot / expand disk / etc>
Worst → after recovery: <e.g. red → yellow → green over 30 min>
Follow-up: <expand disk plan / fix logrotate / file issue against integration X>
EOF
```

## Relationships

### Cross-references

- SDD-026 § Z-10 (storage state surface specification)
- MS011 catalog rows on Z-10 (M00277 dashboard tab Logs)
- Sister runbook: [`network-degraded`](network-degraded.md) (parallel pattern for network state)
- Sister runbooks: [`perimeter-audit-log-corruption`](perimeter-audit-log-corruption.md), [`guardian-audit-log-corruption`](guardian-audit-log-corruption.md), [`scheduler-audit-log-corruption`](scheduler-audit-log-corruption.md) (what to do when the chain DOES break because of disk fill)
- Sister runbook: [`friction-audit-zfs`](friction-audit-zfs.md) (when the pool itself is degraded, not just full)
- selfdef code: `crates/selfdef-api/src/storage.rs` (probe implementation: df + log dir walk)
- selfdef code: `dashboard/app.js::refreshStorage()` (frontend consumer)
