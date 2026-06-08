---
title: "Operator runbook — selfdef metrics ingest lag (events dropped, /metrics under-counting)"
type: reference
domain: ai-agents
layer: 2
status: draft
confidence: high
maturity: seed
created: 2026-06-08
updated: 2026-06-08
sources:
  - id: selfdef-metrics-handler
    type: internal
    project: selfdef
    path: crates/selfdef-api/src/metrics.rs
    note: "selfdef-api Metrics: record_ingest_lag() + the selfdef_ingest_lag_events_total counter; the ingest task subscribes to the bus broadcast and bumps counters per event"
  - id: selfdef-bus-config
    type: internal
    project: selfdef
    path: crates/selfdef-config/src/lib.rs
    note: "[bus] inproc_capacity — the bounded broadcast channel depth that, when exceeded, causes the ingest subscriber to lag and drop events"
  - id: selfdef-observability-alerts
    type: internal
    project: selfdef
    path: modules/observability/assets/alerts/selfdef.yml.template
    note: "SelfdefMetricsIngestLag warning alert fires on increase(selfdef_ingest_lag_events_total[10m]) > 0"
tags: [runbook, observability, metrics, ingest-lag, bus, prometheus, meta-observability, incident-response, selfdef, ips]
---

# Operator runbook — selfdef metrics ingest lag

## Summary

Operator runbook for **selfdef metrics ingest lag** — the daemon's
metrics-ingest subscriber missed events because the in-process bus
broadcast was over-subscribed, so the values at `/metrics` now
**under-count reality**. This is *meta-observability*: the condition
degrades the trustworthiness of every other counter-based alert, because
those alerts read counters that are now lower than the true event stream.
Anchored to: the selfdef-api `Metrics` handler + the `[bus] inproc_capacity`
bound. Fired by the `SelfdefMetricsIngestLag` warning alert.

## When this fires

`SelfdefMetricsIngestLag` fires when
`increase(selfdef_ingest_lag_events_total[10m]) > 0` — i.e. the ingest task
reported one or more *missed* broadcast messages in the last 10 minutes.

The daemon publishes every event onto a bounded in-process broadcast
channel (`[bus] inproc_capacity`, default 4096). The metrics-ingest task is
one subscriber. If producers outrun that subscriber and the channel
overflows, the broadcast layer reports a lag count for the slow receiver and
the ingest task records it via `record_ingest_lag(n)`, bumping
`selfdef_ingest_lag_events_total`. Those `n` events were **never counted**
into `selfdef_events_*` / `selfdef_findings_*`, so those series are now low
by at least `n`.

Severity is **warning**, not critical: detections still happen (the
correlator + responder subscribe independently); what's degraded is the
*observability* of the rate, not the defense itself. But sustained lag means
your dashboards and counter-based alerts are quietly wrong.

## First-look checklist (under 2 minutes)

1. Confirm it's ongoing, not a one-off burst:
   `curl -s --unix-socket /run/selfdef.sock http://localhost/metrics | grep ingest_lag`
   — note the absolute counter; re-check 30 s later. A flat counter = the
   burst is over (alert will clear); a climbing counter = active overflow.
2. Check current event pressure:
   `curl -s … /metrics | grep -E 'selfdef_events_total|selfdef_store_events'`
   — a fast-climbing `events_total` indicates a genuine event storm.
3. Check the configured bus depth:
   `grep -A2 '\[bus\]' /etc/selfdef/selfdef.toml` — note `inproc_capacity`.

## Likely causes + remediation

- **Event storm (legitimate).** A noisy collector (e.g. an auditd or
  Tetragon flood during an incident, a misconfigured rule firing per-syscall)
  is producing more events than the ingest task drains. Remediate the
  *source*: tune the offending collector's filters, or accept the storm is
  real and size for it. The lag itself is a symptom.
- **Bus under-sized for sustained throughput.** Raise `[bus] inproc_capacity`
  in `/etc/selfdef/selfdef.toml` (e.g. 4096 → 16384) to absorb bursts, then
  `selfdefd --validate /etc/selfdef/selfdef.toml` and restart the daemon.
  Trade-off: a deeper channel uses more memory and lets the ingest task fall
  further behind before dropping — it smooths bursts, it does not fix a
  sustained producer>consumer imbalance.
- **Host CPU starvation.** If the daemon is CPU-starved (sustained scheduler
  backpressure — see `SelfdefSchedulerSustainedBackpressure`), the ingest
  task can't keep up. Resolve the resource pressure first.

## Why it matters (don't dismiss it)

Every counter-based selfdef alert (`SelfdefFrictionAuditFailingGate`,
`SelfdefPerimeterSigkill`, the detection-watchdog finding stream, …) reads a
counter that this condition under-counts. A perimeter sigkill or a watchdog
finding that landed in a dropped batch will **not** be reflected in
`/metrics`, so its alert may not fire even though the event happened. Treat a
non-clearing ingest-lag as "my metrics are lying to me" and fix the source or
the bus depth before trusting the other rate alerts.

## Relationships

- RELATES TO selfdef-api `Metrics` (`record_ingest_lag` /
  `selfdef_ingest_lag_events_total`).
- CONSTRAINED BY `[bus] inproc_capacity` (the overflow threshold).
- FEEDS INTO the trustworthiness of every counter-based selfdef alert.
