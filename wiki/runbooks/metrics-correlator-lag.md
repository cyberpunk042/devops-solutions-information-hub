---
title: "Operator runbook — selfdef correlator bus lag (raw events dropped before detection)"
type: reference
domain: ai-agents
layer: 2
status: draft
confidence: high
maturity: seed
created: 2026-06-10
updated: 2026-06-10
sources:
  - id: selfdef-observability-alerts
    type: internal
    project: selfdef
    path: modules/observability/assets/alerts/selfdef.yml.template
    note: "SelfdefCorrelatorBusLag fires on increase(selfdef_correlator_lag_events_total[10m]) > 0"
tags: [runbook, observability, correlator, bus-lag, detection-gap, meta-observability, incident-response, selfdef, ips]
---

# Operator runbook — selfdef correlator bus lag (raw events dropped before detection)

## Summary

The selfdef correlator's bus subscriber over-subscribed the in-process broadcast and **dropped raw events before they were run through the Sigma/correlation rules** — a detection gap proportional to the drop count, which spikes exactly when event volume does (during an incident). This degrades the DEFENSE, not just the metrics (F-2026-094). Anchored to the `SelfdefCorrelatorBusLag` Prometheus alert
(`increase(selfdef_correlator_lag_events_total[10m]) > 0`) shipped by the selfdef `observability` module.

## Symptoms

- The `SelfdefCorrelatorBusLag` warning alert is firing.
- `selfdef_correlator_lag_events_total` is increasing over the last 10 minutes.

## Diagnosis

`selfdef_correlator_lag_events_total` rises when the correlator can't keep up with the bus broadcast — either an event storm or correlator CPU starvation. Correlate the rise with overall `selfdef_events_*` rate and host CPU/PSI. A burst during an incident is the dangerous case (an attacker can flood to bury a real detection).

## Remediation

1. Raise `[bus] inproc_capacity` (the bounded broadcast depth) so the correlator's ring tolerates bursts. 2. Remediate the event-storm source (noisy collector / TracingPolicy). 3. Resolve correlator CPU starvation (host load, scheduling). 4. Confirm the counter stops increasing.

## Relationships

- RELATES TO [[metrics-ingest-lag]] — the sibling meta-observability runbook (the original of this family).
- FEEDS INTO selfdef `observability` alert set (`modules/observability/assets/alerts/selfdef.yml.template`).
