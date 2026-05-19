---
title: "CK Bootstrap — Pile Depile Batch 1 (NEVER_DEPILED verdict)"
aliases:
  - "CK Bootstrap Pollution Audit 2026-05-16"
type: note
domain: cross-domain
status: review
confidence: medium
maturity: seed
created: 2026-05-16
updated: 2026-05-16
sources: []
tags: [ck-bootstrap, pollution-audit, pile-depile, retroactive, operator-decision, batch-1]
contributed_by: circular-knowledge
contribution_source: cron:bootstrap-pollution-audit:2026-05-16T07:16-04:00
contribution_status: pending-review
---

# CK Bootstrap — Pile Depile Batch 1

## Summary

First-run CK v2 bootstrap audit. Computed pile-state metric on operator-flagged
trash zones; verdict: **NEVER_DEPILED (5.35×)** — confirms operator-stated
intuition ("a pile that piled up and never depiled", 2026-05-16). Surfaces a
right-sized first batch of orphan trash for operator decision, plus a phased
plan for the legacy accumulation. No file removed by CK; this is DRAFT +
SURFACE only.

## Pile-state verdict

| Metric | Value |
|---|---|
| Total agent-authored (operator-flagged scope) | **316** |
| Total operator-resolved (struck-through Q in operator-decision-queue.md) | 59 |
| **Pile ratio** | **5.35 ×** |
| Threshold DEPILED | ≤ 2 |
| Threshold PILING_UP | ≤ 5 |
| Threshold NEVER_DEPILED | > 5 |
| **Verdict** | **NEVER_DEPILED** |
| Recommended action | **depile-pile-sprint** |

Per the bootstrap directive, NEVER_DEPILED triggers `scope_full_pile` — the
ENTIRE pile is in scope (no past-7d cap). This batch establishes the census;
subsequent batches (B2…BN) chunk the trash into operator-reviewable slices.

> [!important] Operator-verbatim trigger (sacrosanct, 2026-05-16)
>
> *"make sure everything and it is ready for a proper run that will also
> realize there is a need for retroactive work in this case... as if one pile
> had piled up and never depiled"*
>
> The pile-state metric materializes the intuition. 5.35× is the empirical
> instantiation of "piled up and never depiled."

## Inventory summary (per-category)

### Untracked (working-tree, this audit's primary trash signature)

| Category | Count | Orphan? | In queue? | Notes |
|---|---:|---|---|---|
| `wiki/sources/ecosystem-projects/src-*.md` (mass) | **20** | yes (0 inbound) | 0 of 20 | Mass ingestion of sister-project files; operator-flagged trash zone |
| `wiki/sources/tools-integration/src-aicp-*.md` (mass) | 8 | yes | 0 of 8 | AICP mass ingestion |
| `wiki/sources/ai-models/src-*.md` | 6 | yes | 4 of 6 in queue | Q85 (dup Opus 4.7) + 2 surfaced |
| `wiki/sources/claude-code/src-*.md` | 3 | yes | 0 | Single anchors |
| `wiki/sources/obsidian-notebooklm/src-*.md` | 4 | yes | 0 | Tooling references |
| `wiki/sources/tools-integration/src-{alphaevolve,claude-managed-agents-*,claude-os-*}.md` | 3 | yes | AlphaEvolve in queue (Q77-79) | Mixed |
| `wiki/sources/wiki-methodology/src-*.md` | 3 | yes | 0 | Methodology research |
| `wiki/lessons/01_drafts/metered-programmatic-agentic-economics-...md` | 1 | yes | yes (Q82) | Layer-2 draft, pending operator review |
| `wiki/domains/cross-domain/cascade-candidate-root-ghostproxy-*` | 4 | yes | yes (Q86-Q89) | Recent cross-project candidates |
| `wiki/domains/cross-domain/profile-circular-knowledge-*.md` | 1 | yes | yes (Q81 APPLIED) | Self-doc (anti-pattern per CK v2 — see Vision B below) |
| `wiki/domains/cross-domain/agt-cascade-trio-*.md` | 1 | yes | yes (Q84) | Cross-project consolidation candidate |
| `wiki/log/2026-05-15-research-watch-*.md` | 5 | yes | 0 of 5 | Log-noise (operator-flagged trash zone) |
| `wiki/log/2026-05-15-purge-summary*.md` | 3 | yes | 0 of 3 | Log-noise (operator-flagged trash zone) |
| `wiki/log/2026-05-15-ck-weekly-distillation-surfacings.md` | 1 | yes | 0 | CK self-log (operator-flagged trash zone) |
| `wiki/log/2026-05-15-PRE-COMPACT-HANDOFF-*.md` | 1 | yes | 0 | Session-handoff log |
| `wiki/log/2026-05-15-2026-05-15-pipeline-synthesis-evening-backlog-status-report.md` | 1 | yes | 0 | Status-report log (double-dated filename) |
| `wiki/log/2026-05-16-research-watch-morning.md` | 1 | yes | 0 | Log-noise |
| `wiki/log/2026-05-16-root-ghostproxy-rollout-sprint-morning-briefing.md` | 1 | yes | 0 | Log-noise |
| **Untracked subtotal** | **66** | | | |

### Tracked (already committed; legacy accumulation)

| Category | Count | Orphan? (sampled) | Notes |
|---|---:|---|---|
| `wiki/log/2026-05-08-fire-*-tier-elevation-candidate-*.md` (+ adjacent fire-N variants) | **≈40** | 100% orphan | Bulk tier-elevation-spam from 2026-05-08 |
| `wiki/log/2026-05-08-sustained-feedback-loop-*` / `pareto-*` / `tier-promotion-readiness-*` | ≈10 | 100% orphan | Same trash arc |
| `wiki/log/2026-05-15-research-watch-{frontier-delta,lightweight-scan-*}.md` | 4 | 100% orphan | Same research-watch trash signature as untracked set |
| `wiki/log/2026-04-28-session-log-post-anthropic-3-layer-stack-*.md` | 1 | orphan | Session-log noise |
| `wiki/patterns/01_drafts/*.md` | 88 | 100% orphan (sampled 30/30) | **MIXED** — many are legitimate WIP drafts; not all are trash |
| `wiki/lessons/01_drafts/*.md` (incl. `contributed/`) | 36 | 100% orphan (sampled) | **MIXED** — same mixed status |
| `wiki/decisions/01_drafts/*.md` | 11 | 100% orphan (sampled) | **MIXED** — same mixed status |
| `wiki/sources/src-*.md` (tracked) | 109 | 100% orphan (sampled 30/30) | **MIXED** — source-syntheses; some load-bearing, some duplicates |
| **Tracked-pile subtotal** | **≈250** | | |

> [!note] Why "MIXED" matters (Goldilocks discipline)
>
> 100% orphan rate inside `01_drafts/` and `wiki/sources/` is **not** a
> trash signal by itself — drafts are unbacklinked by design, and source
> pages are leaves in the synthesis graph. The trash discriminator is the
> COMBINATION of: agent-authored AND orphan AND (matches operator-flagged
> trash zone like `fire-N`/`research-watch`/`purge-summary`/mass-sister
> mass OR clearly duplicates other content). Tracked `01_drafts/` and
> tracked `wiki/sources/` will need a separate per-file audit pass before
> mass classification.

## PROPOSE-REMOVAL — Batch 1 (this report)

**Right-sized for one operator review session.** Scope: orphan + 0-queue +
matches operator-flagged trash zone. **No file ambiguity.** Goldilocks-narrow.

### B1.1 — Untracked log-noise (13 files, never committed, zero risk)

These are all untracked (never landed in git), 0 inbound links, 0 references
in operator-decision-queue.md, and match the explicit trash-zone signatures
in the bootstrap directive (`2026-*-research-watch-*`, `2026-*-purge-summary*`,
`2026-*-ck-*`, ephemeral status/handoff briefings).

| # | Path | Author | mtime | Size | Rationale |
|---|---|---|---|---:|---|
| 1 | `wiki/log/2026-05-15-purge-summary.md` | CR? | 2026-05-15 23:28 | 4.3KB | Purge-summary log-noise; trash zone |
| 2 | `wiki/log/2026-05-15-purge-summary-2026-05-15-ephemeral-raws-cleaned-post-synthes.md` | CR | 2026-05-15 20:09 | 3.1KB | Purge-summary, truncated filename; trash zone |
| 3 | `wiki/log/2026-05-15-purge-summary-alphaevolve-raws-cleaned-post-synthesis-2026-0.md` | CR | 2026-05-15 20:56 | 3.6KB | Purge-summary, truncated filename; trash zone |
| 4 | `wiki/log/2026-05-15-research-watch-agt-shipped-pages-flagged.md` | CR | 2026-05-15 19:56 | 8.9KB | Research-watch log; trash zone (operator-flagged) |
| 5 | `wiki/log/2026-05-15-research-watch-alphaevolve-source-synthesis-shipped-flagged.md` | CR | 2026-05-15 21:01 | 9.6KB | Same |
| 6 | `wiki/log/2026-05-15-research-watch-anthropic-spacex-colossus-1-claude-code-limit.md` | CR | 2026-05-15 23:27 | 7.5KB | Same |
| 7 | `wiki/log/2026-05-15-research-watch-gpt-5-5-instant-chatgpt-default-swap-synthesi.md` | CR | 2026-05-15 20:09 | 7.5KB | Same |
| 8 | `wiki/log/2026-05-15-research-watch-opus-4-7-source-synthesis-shipped-end-to-end.md` | CR | 2026-05-15 19:18 | 7.0KB | Same |
| 9 | `wiki/log/2026-05-16-research-watch-morning.md` | CR | 2026-05-15 22:18 | 10.8KB | Research-watch log; trash zone |
| 10 | `wiki/log/2026-05-15-ck-weekly-distillation-surfacings.md` | CK v1 | 2026-05-15 22:50 | 14.9KB | CK self-log; trash zone (operator-flagged `ck-*`) |
| 11 | `wiki/log/2026-05-15-2026-05-15-pipeline-synthesis-evening-backlog-status-report.md` | PS | 2026-05-15 21:19 | 9.6KB | Double-dated status-report log; trash zone |
| 12 | `wiki/log/2026-05-15-PRE-COMPACT-HANDOFF-three-profiles-live-plus-root-ghostproxy-profile-spec.md` | mixed | 2026-05-15 22:26 | 19.1KB | Session-handoff log; ephemeral by nature |
| 13 | `wiki/log/2026-05-16-root-ghostproxy-rollout-sprint-morning-briefing.md` | RGP/CR? | 2026-05-15 23:57 | 10.4KB | Morning-briefing log; trash zone |

**B1.1 net:** 116KB across 13 files, all replaceable signals (the actual
surfacings landed in operator-decision-queue.md as Q-entries, which is the
load-bearing artifact; the logs themselves are duplicative narrative).

### B1.2 — Untracked tier-elevation orphan logs (none currently — all in tracked B2 scope)

Skipped — see B2 below.

### B1.3 — Optional: profile-circular-knowledge self-doc page (1 file, multi-vision)

`wiki/domains/cross-domain/profile-circular-knowledge-evolution-layer-and-brain-self-improvement.md`

- 0 inbound links
- Q81 in queue marked **APPLIED 2026-05-15** (CK v1 self-authored it under
  full_autonomous bound)
- **CK v2 explicit anti-pattern:** AGENTS.md forbids "Author wiki pages about
  CK itself (self-doc anti-pattern)" — this file's existence is the v1 trash
  bug v2 explicitly forbids.

> [!warning] Multi-vision — keep vs remove (DO NOT decide unilaterally)
>
> - **Vision A (CK v2 anti-pattern, remove):** The file is exactly what CK v2
>   AGENTS.md/TOOLS.md prohibit. v1 wrote it; v2 must not own it. Remove +
>   document the v1 mistake in CK self-improvement log.
> - **Vision B (sibling-parity, keep):** Continuous Research and Pipeline
>   Synthesis HAVE profile-pages in `wiki/domains/cross-domain/`. Removing
>   CK's creates asymmetry. The anti-pattern was about FUTURE self-pages;
>   the existing one already serves operator-discoverability.
> - **Vision C (transmute, neither):** Move content (verbatim) to
>   `IDENTITY.md`/`AGENTS.md`/`SOUL.md` in the agent workspace (where it
>   belongs per CK v2's "self-improvement stays in `.assistant/`" rule);
>   then remove from wiki.
>
> **CK recommendation: Vision C** — transmute then remove. Preserves the
> documented identity, returns wiki to the v2 boundary. But operator decides.

## REVIEW-NEEDED — Batch 1

These are agent-authored, orphan, AND have queue references — i.e., the
operator-decision-queue is already tracking them as pending decisions. NOT
trash candidates because the operator may still want them.

| # | Path | In queue | Disposition |
|---|---|---|---|
| R1 | `wiki/domains/cross-domain/cascade-candidate-root-ghostproxy-state-divergence-...md` | Q86 (HIGH) | KEEP-PENDING-Q86 |
| R2 | `wiki/domains/cross-domain/cascade-candidate-root-ghostproxy-m001-reframe-...md` | Q87 | KEEP-PENDING-Q87 |
| R3 | `wiki/domains/cross-domain/cascade-candidate-root-ghostproxy-scope-clarification-selfdef-boundary-2026-05-16.md` | Q88 | KEEP-PENDING-Q88 |
| R4 | `wiki/domains/cross-domain/cascade-candidate-root-ghostproxy-self-update-observe-upstream-head-...md` | Q89 | KEEP-PENDING-Q89 |
| R5 | `wiki/domains/cross-domain/agt-cascade-trio-adopt-as-substrate-...md` | Q84 | KEEP-PENDING-Q84 |
| R6 | `wiki/lessons/01_drafts/metered-programmatic-agentic-economics-...md` | Q82 | KEEP-PENDING-Q82 (Layer-2 promotion candidate, multi-vision present) |
| R7 | `wiki/sources/ai-models/src-anthropic-claude-opus-4-7-release-2026-04-16.md` | Q85 (HIGH) | KEEP-PENDING-Q85 (one of the two-parallel-Opus-4.7 dupes; operator picks canonical) |
| R8 | `wiki/sources/ai-models/src-claude-opus-4-7-anthropic-frontier-2026-04-16.md` | Q85 (HIGH) | KEEP-PENDING-Q85 (the other) |
| R9 | `wiki/sources/ai-models/src-anthropic-spacex-colossus-claude-code-limits-doubled-2026-05-06.md` | indirectly | KEEP (load-bearing for two-track economics arc) |
| R10 | `wiki/sources/tools-integration/src-alphaevolve-...md` | Q77-79 | KEEP-PENDING-Q77/78/79 |
| R11-R30 | other untracked `wiki/sources/` mass (ecosystem-projects, AICP, etc.) | 0 of ~28 | **REVIEW-NEEDED per Q80** — operator already asked "what's the correct disposition for the 12 from-aicp drafts?"; same question applies to other src files |

## KEEP — Batch 1 (explicit retention rationale)

| Path | Reason |
|---|---|
| `wiki/backlog/operator-decision-queue.md` | Load-bearing — this is the operator-decision substrate |
| `wiki/sources/ai-agents/src-microsoft-agent-governance-toolkit-...md` | Reference target of Q74-Q76, Q83 (in 4+ queue rows) |
| `wiki/spine/**` | Operator-territory — CK READS, never proposes removal |

## Operator action — pile_state=NEVER_DEPILED (HIGH URGENCY)

**Decision tree:**

1. **OPTION A — Bulk-approve B1.1 (the safe 13-file untracked log-noise sweep).**
   - Cost: one decision. Risk: zero (never committed; pure working-tree noise).
   - Effect: removes 116KB of orphan trash; pile ratio drops modestly.
   - Slash-command: operator may instruct `/ck depile-execute b1.1` (CK
     does NOT auto-execute).

2. **OPTION B — Issue sprint directive `run depile-pile cleanup now`.**
   - Effect: shifts CK to sprint cadence (cron every 3-5min, per-tick cap
     raised to 1-3 retroactive batches). Goldilocks per-proposal still
     holds. Each tick produces B2, B3, …, BN until full pile audited.
   - Likely needed because B2+ batches require per-file judgment that
     can't fit into one operator decision (e.g., the 109 tracked sources
     and ≈40 tracked fire-N logs).

3. **OPTION C — Do both** (recommended). Approve B1.1 now (immediate
   pile relief); issue sprint directive (depile B2+ over the next
   tick-chain).

> [!info] CK recommendation
>
> **OPTION C — bulk-approve B1.1 + issue sprint directive.** The pile
> ratio 5.35× confirms the operator's intuition; one batch barely moves
> the needle. The sprint cadence is the mechanism designed for exactly
> this case (per AGENTS.md `OPERATOR-DIRECTED SPRINT MODE`).

## Stage discipline & convergence checks

- **Convergence floor (≥3 anchors)** — not applicable to retroactive audit
  (this is REMOVE, not PROMOTE). Floor enforced strictly on `level-up`
  drafts, which CK is NOT producing this tick (would be polluting on a
  pollution-audit tick).
- **Multi-vision** — applied to the only ambiguous file (B1.3 / Q81 self-doc);
  three visions documented.
- **Stage discipline** — N/A (no promotion this tick).
- **Goldilocks per-proposal** — B1.1 = 13 files, one decision shape ("delete
  the log-noise sweep"). Right-sized for one operator review.
- **Goldilocks per-tick** — 1 batch (this one). At v2 cap (0-1 retroactive
  per weekly tick). NEVER_DEPILED + sprint directive would raise to 1-3
  per tick.
- **Anti-pollution gate** — CK is in pollution-AUDIT mode this tick, not
  distillation mode. Zero new wiki/level-up pages produced. Score: clean.

## Anti-pattern surveillance (boundary_guard)

- [x] No sister-project edits (read-only inventory only)
- [x] No mass ingestion (CK does not ingest; CR's lane)
- [x] No self-doc pages authored (this is a log entry in `wiki/log/`, not a
      domain/cross-domain page about CK)
- [x] No operator-territory edits (CLAUDE.md/AGENTS.md/methodology.yaml/spine
      untouched)
- [x] No auto-promotion (DRAFT + SURFACE only)
- [x] No auto-removal (proposes; operator decides)
- [x] No single-truth (Vision A/B/C for the one ambiguous file)
- [x] No skipped pipeline_post (will run after this commit)

## Bootstrap-tick declaration

```
07:16 ET | BOOTSTRAP | pile_state:NEVER_DEPILED | ratio:5.35× |
  total_agent_authored:316 | total_operator_resolved:59 |
  propose_remove:14 (B1.1=13 + B1.3=1) |
  review_needed:30+ (queue-pending + tracked-mixed-status) |
  keep:230+ (operator-resolved, load-bearing, operator-territory) |
  surfaced:1 (this Q via queue append) |
  post:<pending — runs after wiki write>
```

## Relationships

- RELATES TO: [[operator-decision-queue|Operator Decision Queue]]

## Backlinks

[[operator-decision-queue|Operator Decision Queue]]
