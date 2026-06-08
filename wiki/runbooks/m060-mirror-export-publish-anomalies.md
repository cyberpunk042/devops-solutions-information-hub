---
title: "Operator runbook — M060 mirror-export publish anomalies (failing / stale / wedged)"
type: reference
domain: ai-agents
layer: 2
status: draft
confidence: high
maturity: seed
created: 2026-06-06
updated: 2026-06-06
sources:
  - id: selfdef-prometheus-alerts
    type: internal
    project: selfdef
    path: modules/observability/assets/alerts/selfdef.yml.template
    note: "Three SelfdefM060Publish* alerts (failing / stale / wedged) emitted by selfdefd mirror_export_loop"
  - id: sovereign-os-m060-deployment-guide
    type: external
    url: https://github.com/cyberpunk042/sovereign-os/blob/main/docs/operator/m060-deployment-guide.md
    note: "Canonical M060 deployment-guide troubleshooting section (sovereign-os)"
  - id: selfdef-sdd-061
    type: internal
    project: selfdef
    path: docs/sdd/061-module-system.md
    note: "SDD-061 module system — M060 is the mirror-export module per the SDD-061 module fleet"
tags: [runbook, m060, mirror-export, alert, prometheus, operator-facing, selfdef, sovereign-os]
---

# Operator runbook — M060 mirror-export publish anomalies

## Summary

Operator runbook for the three SelfdefM060Publish* Prometheus alerts (failing / stale / wedged) emitted by selfdefd's mirror_export_loop. Triggers a per-artifact investigation — failed publish in last 5min (warning), no successful publish in 10min (warning), or >5 failures in 30min (critical wedged). Anchored to: `modules/observability/assets/alerts/selfdef.yml.template` group `selfdef-m060-mirror-export`.

## When to use this

- Prometheus fires **SelfdefM060PublishFailing** on a specific artifact (warning, 5m window).
- Prometheus fires **SelfdefM060PublishStale** on a specific artifact (warning, 10m window).
- Prometheus fires **SelfdefM060PublishWedged** on a specific artifact (critical, 30m window with >5 failures).
- An operator notices a stale mirror file on disk and wants the right diagnostic procedure.

The three alerts are a graduated severity ladder for the same underlying class of failure (mirror_export_loop's post-publish outcome check found the file missing, stale, or persistent-failing). The wedged variant is the critical operator-page; the failing / stale variants are warning-tier.

## Triage layer-by-layer

### Layer 1: identify which artifact

Each alert carries `{{ $labels.artifact }}` and `{{ $labels.instance }}`. Read those first — they pinpoint WHICH publisher is wedged without paging on every artifact.

```bash
# Look up the specific failure line in selfdefd logs.
journalctl -u selfdefd | grep "mirror export" | grep -i "<artifact-name>" | tail -20
```

The selfdefd publish_* function logs the underlying error (disk full, permission denied, ENOENT, registry-load failure) before returning. The journal line names the failure class verbatim.

### Layer 2: check mirror_dir health

```bash
ls -la /var/lib/selfdef/mirrors/
df -h /var/lib/selfdef/
```

Common causes per failure class:

| Symptom in logs | Likely cause | Operator action |
|---|---|---|
| `ENOSPC` / `disk full` | Filesystem full | Free space; check `journal_disk` watchdog |
| `Permission denied` | mirror_dir ownership drift | `chown -R selfdef:selfdef /var/lib/selfdef/mirrors/`; verify `selfdefd.service` `User=selfdef` |
| `ENOENT` on the mirror file | atomic-rename never completed; partial write | Re-trigger the publish by restarting `selfdefd` (the mirror-export loop re-publishes all artifacts at startup); confirm with `selfdefctl m060-doctor` |
| `registry-load failure` | resident store corruption | Verify the resident-store path; restore from ZFS snapshot if available |

### Layer 3: cross-check the canonical deployment guide

The sovereign-os deployment guide carries the authoritative M060 troubleshooting matrix (operator-onboarded artifact discovery, per-artifact resident-store paths, registry-load semantics). When the journal line + mirror_dir check don't reach a root cause, escalate to that guide.

Cross-reference: `https://github.com/cyberpunk042/sovereign-os/blob/main/docs/operator/m060-deployment-guide.md#troubleshooting` — the canonical operator deployment-guide for M060.

## When NOT to act on the alert

- **Operator hasn't onboarded the artifact's domain yet**. Per the alerts' design, the gauge is absent on un-onboarded artifacts (honest-offline) so the alert SHOULD NOT fire. If it does, check the `absent()` defense logic — there may be a stale gauge from a previous onboarding that was rolled back.
- **Scrape-startup transient**. The alert has a `for: 2m` (failing) / `for: 5m` (stale, wedged) guard; spurious 1-tick fires shouldn't escape these guards. If they do, the scrape interval may be misconfigured.

## Per-artifact recovery recipe

```bash
# 1. Identify the wedged artifact + the failing publish path.
artifact="$(prometheus-cli query 'topk(1, selfdef_m060_mirror_publish_total{result=\"failed\"})')"

# 2. Inspect the selfdef-side chain state — per-domain (6 mirrors)
#    resident-store presence + published mirror-file presence — to locate
#    the wedged artifact. Filesystem-only; no daemon round-trip.
selfdefctl m060-doctor

# 3. Re-trigger publishing. There is no manual per-artifact export verb:
#    the daemon's mirror-export loop publishes ALL artifacts once at
#    startup (then on its timer), so a restart re-publishes. Atomic
#    tempfile+rename means a prior good publish is untouched (idempotent).
sudo systemctl restart selfdefd

# 4. Confirm the publish landed + re-check the per-artifact counters.
journalctl -u selfdefd -f | grep -i "mirror"   # Ctrl-C once it publishes
selfdefctl m060-metrics
```

If step 3 fails with the same error class as the alert, the underlying substrate problem (disk full, permission, corruption) must be resolved before the alert clears.

## Relationships

### Authority

- **SDD-061** (module system) anchors the M060 = mirror-export module identity.
- **Prometheus alert template**: `selfdef modules/observability/assets/alerts/selfdef.yml.template` group `selfdef-m060-mirror-export` carries the three SelfdefM060Publish* alerts this runbook covers.

### Cross-references

- Canonical sovereign-os deployment guide (external): https://github.com/cyberpunk042/sovereign-os/blob/main/docs/operator/m060-deployment-guide.md#troubleshooting
- Sister runbook: [`storage-degraded.md`](storage-degraded.md) — relevant when the M060 anomaly traces to a fs/log-dir bloat root cause.
- Sister runbook: [`scheduler-not-running.md`](scheduler-not-running.md) — relevant when the M060 publisher depends on a scheduler-active state.
- Companion runbook index: [`_index.md`](_index.md).
