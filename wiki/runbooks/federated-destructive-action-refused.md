---
title: "Operator runbook — selfdef federated destructive action refused (fail-closed federation gate)"
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
    note: "The fail-closed federation gate ([responder].act_on_federated = false) and the federated_refused counter; journal line 'refusing destructive action for a federated-origin finding'"
  - id: selfdef-nats-bridge-config
    type: internal
    project: selfdef
    path: crates/selfdef-config/src/lib.rs
    note: "[nats] signing_key_file + peer_keys (F-2026-111 option c, minisign envelopes) — a signature-verified federated finding bypasses the fail-closed gate; selfdef_nats_inbound_federated_verified_total counts the verified subset"
  - id: selfdef-findings-ledger-f111
    type: internal
    project: selfdef
    path: docs/review/99-findings-ledger.md
    note: "F-2026-111 — remote-driven local destructive response; a compromised broker or peer could forge a finding naming a local pid/user"
  - id: selfdef-observability-alerts
    type: internal
    project: selfdef
    path: modules/observability/assets/alerts/selfdef.yml.template
    note: "SelfdefFederatedDestructiveActionRefused warning alert fires on increase(selfdef_responder_federated_refused_total[10m]) > 0"
tags: [runbook, observability, metrics, responder, federation, nats, fail-closed, trust-boundary, prometheus, incident-response, selfdef, ips]
---

# Operator runbook — selfdef federated destructive action refused

## Summary

Operator runbook for the **SelfdefFederatedDestructiveActionRefused** alert. Anchored to: the responder's fail-closed federation gate (`[responder].act_on_federated = false`, crates/selfdef-responder) which refuses destructive actions for findings whose triggering event arrived from ANOTHER host over the NATS bridge, and F-2026-111's signed-envelope escape hatch (`[nats].signing_key_file` + `peer_keys`) that lets signature-verified peers through.

## Symptom

- Prometheus/Alertmanager raises `SelfdefFederatedDestructiveActionRefused` (`warning`): `increase(selfdef_responder_federated_refused_total[10m]) > 0`.
- `journalctl -u selfdefd` shows `refusing destructive action for a federated-origin finding ([responder].act_on_federated is off — fail-closed)` lines.
- A destructive action (kill / quarantine / isolate / egress-lockdown) that a finding would normally drive did NOT fire; alerts/evidence/escalation for the same finding still did.

## Why this matters

`event.actor` fields in a federated event are only as trustworthy as the peer and the broker that relayed them. F-2026-111: a compromised NATS broker or peer can forge a finding naming a LOCAL pid or user — turning this daemon's own response capability into the attacker's weapon (kill a local service, lock out the operator). With `act_on_federated = false` the responder refuses that class outright. **Refusal is the SAFE outcome — but it is a trust-boundary event, not noise.** Unless you run an intentional cross-host response workflow, someone or something remote just tried to drive a local destructive action.

Defaults, verified against `selfdef-config`: `act_on_federated` defaults to `true` (prior cross-host behavior preserved); `false` is the recommended fail-closed posture for any deployment NOT relying on cross-host response. Operator-commanded `selfdefctl` actions are never refused by this gate.

## Diagnosis

1. **Identify the event + intended action** — `journalctl -u selfdefd | grep -F 'refusing destructive action for a federated-origin finding'`; each line names the action + event id.
2. **Which peer sent it?** Correlate `selfdef_nats_inbound_federated_events_total` (overall cross-host ingress) with the sender `host_tag` in the event envelope.
3. **Verified or unverified?** Compare against `selfdef_nats_inbound_federated_verified_total` (the minisign-verified subset — dashboard panel "federated ingress — verified vs total"). A refused action from an UNVERIFIED peer when `peer_keys` is configured is the strongest forged-stream indicator.
4. **Is the finding itself plausible?** Check whether the named local pid/user/target actually matches suspicious local activity (auditd/journald/eBPF series for the same window). A finding that references a target with no local corroboration is likely forged or misattributed.
5. **Broker integrity** — verify NATS transport auth (mTLS/NKey/JWT) and that only expected peers can publish on the subject prefix.

## Recovery procedure

1. **Expected cross-host workflow, trusted peer** → enroll the peer properly instead of opening the gate: give it a minisign identity (`minisign -G -W`), set `[nats].signing_key_file` on the sender and map its `.pub` in this host's `[nats].peer_keys`. Verified findings then bypass the fail-closed gate per F-2026-111 (c) — no blanket `act_on_federated = true` needed.
2. **Unexpected / unverified sender** → treat as an incident: capture the refused events (evidence chain already has them), audit the broker's account/permission map, rotate NATS credentials if compromise is plausible, and check the other federated hosts for the same pattern.
3. **Misattributed but benign** (a legitimate peer whose events are unsigned) → same as 1: sign, don't loosen.
4. Confirm post-recovery: the alert clears; if peers were enrolled, the verified-vs-total dashboard gap closes.

## Operator decision tree

- Refusal + sender in `peer_keys` but unverified → key mismatch or forged envelope; verify the peer's signing key before anything else.
- Refusal + sender unknown → forged/compromised stream until proven otherwise; incident path.
- Refusal + intentional cross-host response design → enroll peer keys (F-2026-111 c); never flip `act_on_federated = true` as a shortcut on a fail-closed deployment.
- Repeated refusals naming the operator account or selfdefd's own pid → active weaponization attempt (compare F-2026-120/121 lockout family); escalate immediately.

## Relationships

- RELATES TO [[responder-circuit-breaker-tripped]] — a forged federated stream can drive both alerts (flood + refusal).
- RELATES TO [[metrics-responder-lag]] — the third responder-health signal.
- DERIVED FROM selfdef F-2026-111 (docs/review/99-findings-ledger.md) — remote-driven local destructive response, and its option-(c) signed-envelope fix.
