---
title: "Operator runbook — selfdef responder circuit breaker tripped (destructive-action rate cap)"
type: reference
domain: ai-agents
layer: 2
status: draft
confidence: high
maturity: seed
created: 2026-07-02
updated: 2026-07-02
sources:
  - id: selfdef-responder
    type: internal
    project: selfdef
    path: crates/selfdef-responder/src/lib.rs
    note: "The GLOBAL destructive-action rate cap ([responder].max_destructive_actions_per_min) and its dedicated ratecap_tripped counter; journal line 'destructive-action rate cap reached (circuit breaker)'"
  - id: selfdef-metrics-handler
    type: internal
    project: selfdef
    path: crates/selfdef-api/src/metrics.rs
    note: "selfdef_responder_ratecap_tripped_total — the genuine flood-breaker counter, split from the aggregate suppressed_destructive_total per F-2026-114 so routine dedup can no longer raise this alert"
  - id: selfdef-findings-ledger-f114
    type: internal
    project: selfdef
    path: docs/review/99-findings-ledger.md
    note: "F-2026-114 — circuit-breaker alert previously fired on routine dedup; fixed by splitting the signal into a dedicated rate-cap counter"
  - id: selfdef-observability-alerts
    type: internal
    project: selfdef
    path: modules/observability/assets/alerts/selfdef.yml.template
    note: "SelfdefResponderCircuitBreakerTripped warning alert fires on increase(selfdef_responder_ratecap_tripped_total[10m]) > 0"
tags: [runbook, observability, metrics, responder, circuit-breaker, rate-cap, flood, prometheus, incident-response, selfdef, ips]
---

# Operator runbook — selfdef responder circuit breaker tripped

## Summary

Operator runbook for the **SelfdefResponderCircuitBreakerTripped** alert. Anchored to: the responder's GLOBAL destructive-action rate cap (`[responder].max_destructive_actions_per_min`, crates/selfdef-responder) and the dedicated `selfdef_responder_ratecap_tripped_total` counter split out of the aggregate suppression counter by F-2026-114 so that routine per-target dedup can never raise this alert again.

## Symptom

- Prometheus/Alertmanager raises `SelfdefResponderCircuitBreakerTripped` (`warning`): `increase(selfdef_responder_ratecap_tripped_total[10m]) > 0`.
- `journalctl -u selfdefd` shows `destructive-action rate cap reached (circuit breaker)` lines.
- Destructive actions (kill / quarantine / block / isolate / egress-lockdown) stop firing while findings keep arriving; notify/evidence actions continue.

## Why this matters

The rate cap is the responder's flood breaker: once destructive actions hit `[responder].max_destructive_actions_per_min` in a minute, further destructive actions are suppressed so the IPS cannot be driven into mass destruction by an event flood. **Tripping is the SAFE outcome** — but it is never routine. Something upstream produced enough High findings to exhaust the cap: an event burst, a correlation storm, a poisoned/spoofed event stream deliberately provoking responses, or a cap tuned too low for the deployment's normal load. While the breaker is open, real threats also go un-actioned — so the trip itself needs a diagnosis, not just an ack.

This series only exists when a deployment has opted in (`max_destructive_actions_per_min > 0`; default `0` = no cap). Routine per-target dedup (`dedup_window_secs`) bumps the aggregate `selfdef_responder_suppressed_destructive_total` but is EXCLUDED from this alert (F-2026-114).

## Diagnosis

1. **Scale of the flood** — how many findings drove it?
   - `increase(selfdef_findings_total[10m])` and `selfdef_findings_by_rule_total` (which rule spiked?).
   - `increase(selfdef_responder_suppressed_destructive_total[10m])` vs `increase(selfdef_responder_ratecap_tripped_total[10m])` — how much of the suppression is genuine cap vs dedup.
2. **Which actions were suppressed** — `journalctl -u selfdefd | grep -F 'rate cap reached (circuit breaker)'`; each line names the action + event id.
3. **Is the source trustworthy?** Check the triggering rule's event source (auditd / journald / eBPF / Tetragon / Suricata / NATS-federated). A spoofed or crafted stream provoking destructive responses is the adversarial case — correlate with `selfdef_nats_inbound_federated_events_total` if the events are cross-host.
4. **Was it a correlation storm?** One noisy rule matching a benign burst (e.g. a deploy, a scan) — the by-rule series makes this obvious.

## Recovery procedure

1. **Do NOT blindly raise the cap.** First classify the flood via Diagnosis: benign burst / noisy rule / adversarial stream.
2. **Noisy rule** → tune or tier the rule (see the detection-watchdog dual-tier routing, SDD-062) so benign bursts stop producing destructive-class findings.
3. **Benign but legitimate load growth** → raise `[responder].max_destructive_actions_per_min` deliberately, and record why.
4. **Adversarial / spoofed stream** → treat as an incident: verify collector integrity, check NATS transport auth (mTLS/NKey/JWT) if federated, and review what the suppressed actions would have targeted (a flood can be cover for one real action the attacker wants suppressed).
5. The breaker resets per minute-window automatically; no restart is required. Confirm post-recovery: the alert clears and `rate(selfdef_responder_ratecap_tripped_total[10m])` returns to 0.

## Operator decision tree

- Trip + one rule dominates `findings_by_rule` → tune that rule; cap stays.
- Trip + broad multi-rule surge + deploy/scan window → benign burst; consider cap raise with rationale.
- Trip + federated-origin events in the mix → cross-check [[federated-destructive-action-refused]] and peer trust before anything else.
- Repeated trips with no upstream explanation → assume adversarial; escalate per incident process.

## Relationships

- RELATES TO [[metrics-responder-lag]] — the other responder-health signal (dropped findings vs suppressed actions).
- RELATES TO [[federated-destructive-action-refused]] — the federation trust boundary; a poisoned federated stream can drive both alerts.
- DERIVED FROM selfdef F-2026-114 (docs/review/99-findings-ledger.md) — the alert-fatigue fix that made this signal trustworthy.
