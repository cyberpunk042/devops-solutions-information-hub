---
title: "Operator runbook — selfdef correlator bus lag (raw events dropped, missed detections)"
type: reference
domain: ai-agents
layer: 2
status: draft
confidence: high
maturity: seed
created: 2026-06-09
updated: 2026-06-09
sources:
  - id: selfdef-metrics-handler
    type: internal
    project: selfdef
    path: crates/selfdef-api/src/metrics.rs
    note: "selfdef-api Metrics: the selfdef_correlator_lag_events_total counter; the correlator subscribes to the bus broadcast and a lag means raw events were never rule-evaluated"
  - id: selfdef-bus-config
    type: internal
    project: selfdef
    path: crates/selfdef-config/src/lib.rs
    note: "[bus] inproc_capacity — the bounded broadcast channel depth that, when exceeded, causes a slow subscriber (here the correlator) to lag and drop events"
  - id: selfdef-observability-alerts
    type: internal
    project: selfdef
    path: modules/observability/assets/alerts/selfdef.yml.template
    note: "SelfdefCorrelatorBusLag warning alert fires on increase(selfdef_correlator_lag_events_total[10m]) > 0"
tags: [runbook, observability, metrics, correlator-lag, bus, prometheus, detection, incident-response, selfdef, ips]
---

# Operator runbook — selfdef correlator bus lag

## Summary

Operator runbook for **selfdef correlator bus lag** — the daemon's
**correlator** subscriber fell behind the in-process bus broadcast and raw
events were dropped before the Sigma/correlation rules ever saw them. Unlike
metrics-ingest lag (which only degrades the `/metrics` counters), correlator
lag is a **detection gap**: the dropped events are never rule-evaluated, so a
real attack pattern carried in a dropped batch produces **no finding at
all**. Anchored to: the selfdef-api `Metrics` handler
(`selfdef_correlator_lag_events_total`) + the `[bus] inproc_capacity` bound.
Fired by the `SelfdefCorrelatorBusLag` warning alert.

## When this fires

`SelfdefCorrelatorBusLag` fires when
`increase(selfdef_correlator_lag_events_total[10m]) > 0` — i.e. the
correlator reported one or more *missed* broadcast messages in the last 10
minutes.

The daemon publishes every event onto a bounded in-process broadcast channel
(`[bus] inproc_capacity`, default 4096). The correlator is one subscriber. If
producers outrun the correlator and the channel overflows, the broadcast
layer reports a lag count for the slow receiver and the correlator records it
into `selfdef_correlator_lag_events_total`. Those `n` events were **never run
through the rules** — any detection they would have triggered did not happen.

Severity is **warning** at the metric level, but treat a non-clearing
correlator lag as a **detection-availability incident**: the defense itself
is degraded, not merely its observability.

## First-look checklist (under 2 minutes)

1. Confirm it's ongoing, not a one-off burst:
   `curl -s --unix-socket /run/selfdef.sock http://localhost/metrics | grep correlator_lag`
   — note the absolute counter; re-check 30 s later. A flat counter = the
   burst is over (alert will clear); a climbing counter = active overflow.
2. Check current event pressure:
   `curl -s … /metrics | grep -E 'selfdef_events_total|selfdef_store_events'`
   — a fast-climbing `events_total` indicates a genuine event storm.
3. Check the configured bus depth:
   `grep -A2 '\[bus\]' /etc/selfdef/selfdef.toml` — note `inproc_capacity`.

## Likely causes + remediation

- **Event storm (legitimate).** A noisy collector (auditd / Tetragon flood
  during an incident, a misconfigured rule firing per-syscall) produces more
  events than the correlator drains. Remediate the *source*: tune the
  offending collector's filters, or size for the real load. The lag is a
  symptom.
- **Bus under-sized for sustained throughput.** Raise `[bus] inproc_capacity`
  in `/etc/selfdef/selfdef.toml` (e.g. 4096 → 16384), then
  `selfdefd --validate /etc/selfdef/selfdef.toml` and restart the daemon. A
  deeper channel absorbs bursts; it does not fix a sustained
  producer>consumer imbalance.
- **Correlator CPU starvation.** If the daemon is CPU-starved (sustained
  scheduler backpressure — see `SelfdefSchedulerSustainedBackpressure`), the
  correlator can't keep up. Resolve the resource pressure first.
- **A single rule is pathologically expensive.** A correlation rule with a
  huge window or unbounded state can slow the correlator enough to lag.
  Profile recent rule changes; revert or bound the offending rule.

## Why it matters (don't dismiss it)

Correlator lag means raw events bypassed detection entirely. During an active
incident — exactly when event volume spikes — this is when you are *most*
likely to drop the events that matter and *least* able to afford it. A
sustained `selfdef_correlator_lag_events_total` is a signal that your
detection coverage has a hole proportional to the drop count. Restore
correlator throughput (source tuning or bus depth) before trusting that
"no finding" means "no attack".

## Relationships

- RELATES TO selfdef-api `Metrics` (`selfdef_correlator_lag_events_total`).
- CONSTRAINED BY `[bus] inproc_capacity` (the overflow threshold).
- PARALLELS [[metrics-ingest-lag]] (same bus-overflow mechanism; ingest lag
  degrades observability, correlator lag degrades detection).
- FEEDS INTO the trustworthiness of the entire detection pipeline.
