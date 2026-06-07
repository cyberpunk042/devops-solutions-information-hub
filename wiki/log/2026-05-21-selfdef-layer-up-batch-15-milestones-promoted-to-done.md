---
title: "selfdef layer-up batch — 15 milestones promoted partial → done"
type: note
domain: ai-agents
layer: 2
status: synthesized
confidence: high
maturity: growing
created: 2026-05-21
updated: 2026-05-21
sources:
  - id: selfdef-commit-log-2026-05-21
    type: directive
    project: selfdef
    path: CHANGELOG.md
    note: "71 commits this session on selfdef main; full block captured in CHANGELOG [Unreleased] under 3 batches (2026-05-21 batch 1 / batch 2 / batch 3)"
  - id: selfdef-index
    type: internal
    project: selfdef
    path: backlog/milestones/INDEX.md
    note: "Final tally 42 done / 6 partial / 0 stage-1 (was ~8 done pre-session)"
tags: [log, selfdef, milestones, layer-up, sdd, production-landing, multi-cycle, second-brain, ips]
---

# selfdef layer-up batch — 15 milestones promoted partial → done (2026-05-21)

## Summary

15 selfdef milestones promoted from `partial` to `done` in a single
multi-cycle session (71 commits on selfdef main). Each promotion
followed the operator's standing rule "**You cannot mark something
done if it hasn't reached Prod**" — every layer-up shipped CLI +
HTTP discovery + L1 gates over already-shipped Rust crate clusters.

Final INDEX tally:

| Status | Count | Change |
|---|---|---|
| done | 42 | +33 over pre-session ~8 |
| partial | 6 | substantive deferred work only |
| stage-1 | 0 | (eliminated) |

## The 15 promotions

| Milestone | Surfaces shipped | Commits |
|---|---|---|
| MS041 commit-authority | selfdefctl CLI + GET /v1/commit-authority | 7c64aec → 9675521 |
| MS042 tool-authority | selfdefctl CLI + GET /v1/tool-authority | eb98cfb → b0493e4 |
| MS035 capability-tokens | selfdefctl + HTTP discovery | 14e12cc |
| MS037 filesystem-boundary | selfdefctl + HTTP discovery | eba43c7 |
| MS038 network-boundary | selfdefctl + HTTP discovery | eba43c7 |
| MS032 sandbox-tiers | selfdefctl + HTTP discovery | aa0f77a |
| MS034 communication-boundary | selfdefctl + HTTP discovery | aa0f77a |
| MS039 + MS040 authority | selfdefctl + HTTP discovery | e99caaf |
| MS036 tool-sandboxes | covered via MS032 cross-coverage | 6f8f088 |
| MS033 policy + trace (36 crates) | selfdefctl + HTTP discovery + SDD-051 | cdd5039 |
| MS028 bitnet-gpu | INDEX status reconciliation | 78c5f64 |
| MS031 wasm-aot-cache | INDEX status reconciliation | 78c5f64 |
| MS014 SSH-wrap | selfdefctl + SDD-052 | ecf212d |
| MS015 NATS | selfdefctl + GET /v1/nats + SDD-053 | ecf212d |

## MS011 — operator dashboard

All 13 Z-vectors reached at least probe/discovery level. Of those:

- Z-1 panel-nav strip (1c4f885) — 14 → 16 anchors as panels grew
- Z-2 inference-backends — backend + CLI + dashboard panel + L1
- Z-3 flex-profile — new `selfdef-flex-profile` crate (322 LOC, 8
  tests) + CLI (schema + show subverbs) + HTTP + dashboard panel + L1
- Z-6 composite health — backend + CLI + dashboard + L1
- Z-7 network state, Z-8 docker install paths, Z-9 RAID, Z-10
  storage — backend + dashboard + L1
- Z-11 MCP-interop foundation — HTTP discovery
- Z-12 multi-tier REPL — HTTP discovery
- Z-13 SD-R83 + SD-R86 dep-readiness — full

Multi-commit follow-up arcs remain: Z-1 full 8-tab UX restructure,
Z-2 shell-out invocation, Z-3 apply+revert mutation surfaces, Z-13
SD-R87 topological install + SD-R86 hardware-gate enrichment.

## MS013 — SDD ledger

12 retroactive Stage-2 SDDs authored or promoted this session:

| SDD | Subject | Action |
|---|---|---|
| SDD-043 | commit-authority | authored |
| SDD-044 | capability-tokens | authored |
| SDD-045 | filesystem-boundary | authored |
| SDD-046 | network-boundary | authored |
| SDD-047 | sandbox-tiers | authored |
| SDD-048 | communication-boundary | authored |
| SDD-049 | authority + profiles | authored |
| SDD-050 | tool authority | authored |
| SDD-051 | policy + trace (36-crate cluster) | authored |
| SDD-052 | SSH-wrap | authored |
| SDD-053 | NATS bridge | authored |
| SDD-032 | eBPF substrate | draft → implemented |

Plus 9 module SDDs batch-promoted draft → implemented (SDD-033 /
034 / 036 / 037 / 038 / 039 / 040 / 041 / 042).

New utility shipped: `scripts/test/sdd-tally.sh` — MS013
charter-tracking drift detector.

Final SDD tally:

| Status | Count |
|---|---|
| implemented | 43 |
| draft | 6 (forward-looking cycle vector specs) |
| review | 2 (SDD-012 sain-01 + SDD-026 operator-dashboard) |
| scoping | 3 (SDD-009/010/011 operator-gated) |
| living | 1 (SDD-000 charter) |
| **total** | **54** |

## Cross-cutting metrics

- Selfdefctl top-level verbs: 27 (was 13 pre-session)
- /v1/* HTTP routes: ~52 (was ~15 pre-session)
- Dashboard panels: 17 (was 14 pre-session) — Composite Health
  + 4 watchdogs + Modules + Audit chains + Alerts + Hardware +
  Network + Storage + RAID + GPU + CPU + Flex profile +
  Inference backends + Findings
- New crate: `selfdef-flex-profile` (Total 535)
- Coherence harness 28/28 layers PASS throughout the session

## Remaining 6 partials — explicit deferred-for-cause

| Milestone | Gating |
|---|---|
| MS002 collector fabric | 3 eBPF kernel programs deferred per SDD-032 |
| MS008 sain-01 integration | SDD-010 scoping; SDD-012 review (operator-gated) |
| MS011 | 4 substantive multi-commit Z-vector arcs |
| MS013 | ongoing SDD charter-tracking |
| MS016 | 4 eBPF kernel programs deferred per SDD-032 |

None of these are catalog drift. Each has explicit
operator-architectural gating or substantive multi-commit work
that doesn't fit a single-session slice.

## Pattern that worked

The "layer-up over crate-already-shipped" pattern was the highest
throughput shape this session:

1. Identify a milestone at `partial` whose Rust crate cluster
   already ships in production.
2. Author the Stage-2 SDD if missing (typically 100-300 lines
   covering: problem / goals / non-goals / recommended design /
   caller contract / implementation status / open questions D-1..D-N).
3. Ship `selfdefctl <verb>` CLI subcommand (typically 50-150 lines,
   single static discovery + optional subverbs).
4. Ship `GET /v1/<route>` HTTP discovery surface (typically 50-100
   lines, static schema + 1 unit test asserting canonical counts).
5. Update L1 gates: `L1-api-endpoints.sh` check_route + (if dashboard
   panel) `L1-dashboard-sections.sh` checks.
6. Update INDEX.md: milestone row partial → done with explicit
   list of shipped surfaces + explicit deferred-for-cause arcs.
7. Coherence harness verifies the whole stack at once.

The shape repeats. 5+ milestones per cycle. Each commit is
self-contained, reverts cleanly, and increments the partial-to-done
ratio.

## Cross-references

- selfdef CHANGELOG.md `[Unreleased]` section captures the
  3 dated batches (2026-05-21 batch 1 / batch 2 / batch 3)
- selfdef backlog/milestones/INDEX.md final tally
- selfdef scripts/test/sdd-tally.sh — drift detector
- info-hub `wiki/log/2026-05-20-four-watchdog-end-to-end-production-landing.md`
  — previous session's landing log (MS044/MS046/MS047/MS048
  four-watchdog set)
