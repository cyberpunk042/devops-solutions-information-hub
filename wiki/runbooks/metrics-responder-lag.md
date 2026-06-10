---
title: "Operator runbook — selfdef responder bus lag (findings dropped before any action)"
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
    note: "SelfdefResponderBusLag fires on increase(selfdef_responder_lag_events_total[10m]) > 0"
tags: [runbook, observability, responder, bus-lag, response-gap, meta-observability, incident-response, selfdef, ips]
---

# Operator runbook — selfdef responder bus lag (findings dropped before any action)

## Summary

The selfdef responder's bus subscriber over-subscribed the in-process broadcast and **dropped findings before any autonomous response fired** (no block/quarantine/notify). Detection happened; the gap is between detecting and acting — an attacker flooding low-value findings to bury a high-value one under responder lag is a plausible evasion (F-2026-094). Anchored to the `SelfdefResponderBusLag` Prometheus alert
(`increase(selfdef_responder_lag_events_total[10m]) > 0`) shipped by the selfdef `observability` module.

## Symptoms

- The `SelfdefResponderBusLag` warning alert is firing.
- `selfdef_responder_lag_events_total` is increasing over the last 10 minutes.

## Diagnosis

`selfdef_responder_lag_events_total` rises when the responder's action path can't drain findings fast enough — typically a slow/blocking action (operator script, loginctl, Velociraptor) or responder CPU starvation. Correlate with finding rate + which actions are enabled.

## Remediation

1. Make the action path faster / async (the responder already bounds each action with a deadline; check for a wedged subprocess). 2. Raise `[bus] inproc_capacity`. 3. Resolve responder CPU starvation. 4. Confirm the counter stops increasing.

## Relationships

- RELATES TO [[metrics-ingest-lag]] — the sibling meta-observability runbook (the original of this family).
- FEEDS INTO selfdef `observability` alert set (`modules/observability/assets/alerts/selfdef.yml.template`).
