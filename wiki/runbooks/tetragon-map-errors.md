---
title: "Operator runbook — Tetragon kernel detection source degrading (BPF map errors / socket-dropout gotcha)"
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
    note: "SelfdefTetragonMapErrors fires on increase(tetragon_map_errors_total[10m]) > 0"
tags: [runbook, observability, tetragon, ebpf, kernel-fence, event-drop, meta-observability, incident-response, selfdef, ips]
---

# Operator runbook — Tetragon kernel detection source degrading (BPF map errors / socket-dropout gotcha)

## Summary

Tetragon — the in-kernel detection source feeding selfdef's collector — is reporting BPF map errors, meaning it is under kernel-resource pressure and may be **silently dropping or mishandling exec/file/socket events before selfdef ever receives them** (the *Tetragon-socket-dropout gotcha*). Unlike a vanished Tetragon socket (covered by `SelfdefGuardianTetragonSocketMissing`), the collector stays connected while the source quietly loses fidelity, so detection degrades with **no signal on selfdef's own event bus** — the external analog of the bus-lag family. Anchored to the `SelfdefTetragonMapErrors` Prometheus alert
(`increase(tetragon_map_errors_total[10m]) > 0`) shipped by the selfdef `observability` module.

## Symptoms

- The `SelfdefTetragonMapErrors` warning alert is firing.
- `tetragon_map_errors_total` is increasing over the last 10 minutes.

## Diagnosis

Tetragon BPF map errors usually mean the process-cache map is full or map update/read operations are failing under load. Cross-check: is `tetragon_events_total` flattening (events not arriving) while host activity is high? Is `tetragon_process_cache_size` pinned at its limit? Check `journalctl -u tetragon` for ringbuffer/map warnings and the host's memory/CPU pressure (PSI).

## Remediation

1. Raise Tetragon's process-cache + ringbuffer/map sizing (Tetragon `--process-cache-size`, perf/ringbuf event map sizing) for the host's event volume. 2. Reduce event volume at the source (tighten noisy TracingPolicies / narrow selectors). 3. Resolve host memory/CPU starvation. 4. After remediation, confirm `tetragon_map_errors_total` stops increasing and `tetragon_events_total` tracks activity again. Until resolved, treat kernel-source detection as **degraded** and lean on the periodic AIDE baseline + auditd/journald collectors for coverage.

## Relationships

- RELATES TO [[metrics-ingest-lag]] — the sibling meta-observability runbook (the original of this family).
- FEEDS INTO selfdef `observability` alert set (`modules/observability/assets/alerts/selfdef.yml.template`).
