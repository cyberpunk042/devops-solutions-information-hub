---
title: "Operator runbooks — index"
type: index
domain: ai-agents
layer: 2
status: active
confidence: high
maturity: growing
created: 2026-06-06
updated: 2026-06-06
sources:
  - id: selfdef-sdd-027-thru-031
    type: internal
    project: selfdef
    path: docs/sdd/
    note: "Source SDDs anchoring each runbook (SDD-027 friction-audit, SDD-028 perimeter, SDD-029 guardian, SDD-030 ux-coherence-harness, SDD-031 goldilocks-scheduler)"
  - id: operator-directive-runbook-discipline
    type: directive
    project: devops-solutions-information-hub
    path: raw/notes/
    note: "Operator standing direction — runbooks are the operator-facing layer where SDD contracts meet operational reality"
tags: [index, runbook, operator-facing, selfdef, sovereign-os, friction-audit, perimeter, guardian, scheduler, ux-coherence]
---

# Operator runbooks — index

## Summary

Operator-facing runbook navigation home for the selfdef + sovereign-os production-progression arc. Each runbook is anchored to a specific SDD section + verbatim source dump line range, walks the operator from "summary line says FAIL" to "root cause + fix", and lists sister runbooks under § Relationships. Twenty-four runbooks cover the four-watchdog enforcement trio (friction-audit, perimeter, guardian, scheduler) plus cross-cutting surfaces (network, storage, UX-coherence). One doctrine citation index (Peace Machine + Core Law) and one detection-watchdog alert-finding runbook complete the set.

## When to use this

- An operator-facing harness exited non-zero — pick the runbook matching the named layer.
- A systemd unit `selfdef-*.service` failed — pick the `*-not-running` runbook for that engine.
- An MS003-signed manifest is being authored, rotated, or revoked — pick the relevant `perimeter-*` or `scheduler-weight-matrix-rotation` runbook.
- Audit-log chain broke on the host — pick the `*-audit-log-corruption` runbook for the affected daemon.
- An operator-investigated incident needs a forensic procedure — pick the relevant `*-investigation` or `*-false-positive-rollback` runbook.

## Friction-audit trio (SDD-027 + MS046)

| Runbook | Trigger |
|---|---|
| [friction-audit immutability gate failure](friction-audit-immutability.md) | Boot-time immutability hash mismatch |
| [friction-audit memory gate failure](friction-audit-memory.md) | RAM-substrate integrity check failed |
| [friction-audit PCIe gate failure](friction-audit-pcie.md) | PCIe-topology drift detected |
| [friction-audit signature gate failure](friction-audit-signature.md) | Operator-signed manifest fails minisign verify |
| [friction-audit ZFS gate failure](friction-audit-zfs.md) | ZFS pool integrity / dataset stratification anomaly |

## Perimeter (SDD-028 + MS047)

| Runbook | Trigger |
|---|---|
| [perimeter audit log corruption / chain break](perimeter-audit-log-corruption.md) | SHA-256-chained audit log gap or hash mismatch |
| [perimeter allowlist extension (signed, multi-sig)](perimeter-extension-create.md) | New container-runtime or operator-tool path needs allowlisting |
| [perimeter MS003 key rotation](perimeter-key-rotation.md) | Operator / auditor key rotation cadence or compromise |
| [perimeter TracingPolicy load failure](perimeter-policy-load-failure.md) | `sovereign-kernel-fence` TracingPolicy refused to load |
| [perimeter SIGKILL investigation](perimeter-sigkill-investigation.md) | Unexpected kprobe SIGKILL on the host |
| [perimeter Tetragon not running](perimeter-tetragon-not-running.md) | `tetragon.service` not active |

## Guardian (SDD-029 + MS044)

| Runbook | Trigger |
|---|---|
| [Guardian audit log corruption / chain break](guardian-audit-log-corruption.md) | Guardian audit chain integrity anomaly |
| [Guardian console alert investigation](guardian-console-alert-investigation.md) | Operator-facing console alert needs root-cause |
| [Guardian false-positive rollback](guardian-false-positive-rollback.md) | Confirmed false-positive needs operator-supervised rollback |
| [Guardian Daemon not running](guardian-not-running.md) | `selfdef-guardian.service` not active |
| [Guardian Tetragon socket unreachable](guardian-socket-unreachable.md) | Guardian cannot reach Tetragon's UNIX socket |

## Scheduler (SDD-031 + MS048)

| Runbook | Trigger |
|---|---|
| [scheduler audit log corruption / chain break](scheduler-audit-log-corruption.md) | `scheduler_audit.log` chain integrity anomaly |
| [scheduler backpressure stuck open](scheduler-backpressure-stuck-open.md) | Backpressure indicator remains asserted past expected window |
| [scheduler force-override investigation](scheduler-force-override-investigation.md) | `selfdefctl scheduler force` recorded with override_signer_kid |
| [Goldilocks Scheduler not running](scheduler-not-running.md) | `selfdef-scheduler.service` not active |
| [scheduler weight matrix rotation (MS003 multi-sig)](scheduler-weight-matrix-rotation.md) | Per-profile 7-axis weight matrix needs operator-tunable evolution |

## UX coherence harness (SDD-030 + MS045)

| Runbook | Trigger |
|---|---|
| [UX coherence harness failures](ux-coherence-failures.md) | `bash scripts/test/coherence.sh` (or `make coherence`) exited non-zero |

## Cross-cutting surfaces (sovereign-os)

| Runbook | Trigger |
|---|---|
| [network state degraded](network-degraded.md) | Internet / DNS / cloudflared / tailscale / Traefik anomaly |
| [Storage state degraded](storage-degraded.md) | Filesystem fill, log dir bloat |

## Detection-watchdog + doctrine

| Page | Role |
|---|---|
| [selfdef detection-watchdog alert finding](selfdef-watchdog-alert-finding.md) | Detection-watchdog alert investigation procedure |
| [Peace Machine + Core Law — doctrine clause citation index](peace-machine-and-core-law-doctrine-citation-index.md) | Authoritative citation registry mapping each Core Law clause to runtime enforcement points |

## Relationships

### Authority

- **SDD-027** (friction-audit) · **SDD-028** (perimeter) · **SDD-029** (guardian) · **SDD-030** (ux-coherence-harness) · **SDD-031** (goldilocks-scheduler) in `selfdef docs/sdd/`.
- **MS044** (Guardian Daemon) · **MS045** (UX coherence harness) · **MS046** (Friction Audit) · **MS047** (Real-time security perimeter engine) · **MS048** (Goldilocks Scheduler) in `selfdef backlog/milestones/`.
- **MS003** (selfdef-signing chain-of-trust) — anchors all multi-sig procedures.

### Cross-references

- Companion canonical index: [`wiki/ecosystem/two-ultimate-solutions-canonical-index.md`](../ecosystem/two-ultimate-solutions-canonical-index.md) — operator-stated "two ultimate solutions" identification (selfdef + sovereign-os); this runbook fleet covers the operator-facing layer of those two ultimate solutions.
- Companion pattern: [`wiki/patterns/01_drafts/ms5a-state-journal-vs-enforcement-layer-separation.md`](../patterns/01_drafts/ms5a-state-journal-vs-enforcement-layer-separation.md) — implementation pattern referenced by several runbooks for the MS5a-state-journal / MS5a-enforcement split.
- Companion pattern: [`wiki/patterns/01_drafts/paired-enforcement-primitive-five-milestone-architecture.md`](../patterns/01_drafts/paired-enforcement-primitive-five-milestone-architecture.md) — five-milestone architecture that anchors the SDD-065..078 IPS-quattuordectet runbook fleet (forthcoming).
- Companion decision: [`wiki/decisions/01_drafts/in-memory-backend-as-ms1-substrate.md`](../decisions/01_drafts/in-memory-backend-as-ms1-substrate.md) — MS1 in-memory backend substrate that backs each primitive's runbook.
- Companion session log: [`wiki/log/2026-05-29-selfdef-enforcement-layer-pivot-sdd-065-sdd-066.md`](../log/2026-05-29-selfdef-enforcement-layer-pivot-sdd-065-sdd-066.md) — selfdef enforcement-layer pivot session log (SDD-065 + SDD-066 ready-for-review).
