---
title: "Operator runbook — selfdef responder bus lag (findings dropped, no action fired)"
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
    note: "selfdef-api Metrics: the selfdef_responder_lag_events_total counter; the responder subscribes to the bus broadcast and a lag means findings were dropped before any autonomous action fired"
  - id: selfdef-bus-config
    type: internal
    project: selfdef
    path: crates/selfdef-config/src/lib.rs
    note: "[bus] inproc_capacity — the bounded broadcast channel depth that, when exceeded, causes a slow subscriber (here the responder) to lag and drop findings"
  - id: selfdef-observability-alerts
    type: internal
    project: selfdef
    path: modules/observability/assets/alerts/selfdef.yml.template
    note: "SelfdefResponderBusLag warning alert fires on increase(selfdef_responder_lag_events_total[10m]) > 0"
tags: [runbook, observability, metrics, responder-lag, bus, prometheus, response, incident-response, selfdef, ips]
---

# Operator runbook — selfdef responder bus lag

## Summary

Operator runbook for **selfdef responder bus lag** — the daemon's
**responder** subscriber fell behind the in-process bus broadcast and
findings were dropped before any autonomous response could fire. This is a
**response gap**: detection may have happened (the correlator produced the
finding), but the responder never received it, so no block / quarantine /
notify action was dispatched for those `n` findings. Anchored to: the
selfdef-api `Metrics` handler (`selfdef_responder_lag_events_total`) + the
`[bus] inproc_capacity` bound. Fired by the `SelfdefResponderBusLag` warning
alert.

## When this fires

`SelfdefResponderBusLag` fires when
`increase(selfdef_responder_lag_events_total[10m]) > 0` — i.e. the responder
reported one or more *missed* broadcast messages in the last 10 minutes.

The daemon publishes findings onto a bounded in-process broadcast channel
(`[bus] inproc_capacity`, default 4096). The responder is one subscriber. If
findings arrive faster than the responder drains them (slow action backend,
a flood of high-severity findings) and the channel overflows, the broadcast
layer reports a lag count and the responder records it into
`selfdef_responder_lag_events_total`. For those `n` findings **no autonomous
action fired**.

Severity is **warning** at the metric level, but treat a non-clearing
responder lag as a **response-availability incident**: findings were raised
and then silently went un-acted-upon.

## First-look checklist (under 2 minutes)

1. Confirm it's ongoing, not a one-off burst:
   `curl -s --unix-socket /run/selfdef.sock http://localhost/metrics | grep responder_lag`
   — note the absolute counter; re-check 30 s later. A climbing counter =
   active overflow; a flat counter = the burst is over (alert will clear).
2. Check the finding rate driving it:
   `curl -s … /metrics | grep -E 'selfdef_findings_total|selfdef_findings_by_severity_total'`
   — a spike in findings is the usual trigger.
3. Check whether the responder is throttled or its floor is misconfigured:
   `curl -s … /metrics | grep selfdef_responder_min_severity_floor` and
   `grep -A3 '\[responder\]' /etc/selfdef/selfdef.toml`.

## Likely causes + remediation

- **Finding storm.** A genuine attack or a misconfigured rule produces
  findings faster than the responder can dispatch actions. Confirm the
  findings are real; if a rule is over-firing, tune it. If the storm is real,
  the lag is telling you the response backend is the bottleneck.
- **Slow action backend.** If each response makes a slow external call
  (firewall API, notify webhook, quarantine mount), the responder drains
  slowly and lags under load. Make the action path faster or asynchronous, or
  raise the responder's concurrency.
- **Bus under-sized for finding bursts.** Raise `[bus] inproc_capacity` in
  `/etc/selfdef/selfdef.toml`, then `selfdefd --validate` and restart. This
  absorbs bursts; it does not fix a sustained finding-rate > dispatch-rate
  imbalance.
- **Responder CPU starvation.** Resolve sustained scheduler backpressure
  (`SelfdefSchedulerSustainedBackpressure`) first if present.

## Why it matters (don't dismiss it)

Responder lag means findings were raised and then **no action was taken** for
them — the gap between "we detected it" and "we did something about it". An
attacker generating a flood of low-value findings to bury one high-value one
under responder lag is a plausible evasion. Restore responder throughput
(faster/async actions or bus depth) so that every finding that crosses the
`selfdef_responder_min_severity_floor` actually gets dispatched.

## Relationships

- RELATES TO selfdef-api `Metrics` (`selfdef_responder_lag_events_total`).
- CONSTRAINED BY `[bus] inproc_capacity` (the overflow threshold).
- RELATES TO `selfdef_responder_min_severity_floor` (the floor a finding must
  clear to be dispatched at all; lag drops findings regardless of floor).
- PARALLELS [[metrics-correlator-lag]] and [[metrics-ingest-lag]] (same
  bus-overflow mechanism at different pipeline stages).
- FEEDS INTO the trustworthiness of the autonomous-response guarantee.
