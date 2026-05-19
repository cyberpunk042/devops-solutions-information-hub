---
title: "research-watch — Opus 4.7 source-synthesis SHIPPED (end-to-end execution per cron 19:11 ET)"
type: note
domain: log
note_type: completion
status: active
confidence: high
created: 2026-05-15
updated: 2026-05-15
sources: []
tags: [log, completion]
---

# research-watch — Opus 4.7 source-synthesis SHIPPED (end-to-end execution per cron 19:11 ET)

## Summary

Cron tick `continuous-research-frontier-delta-check` at 2026-05-15 19:11 ET executed the
`on_significant_change_detected` recipe end-to-end for the highest-impact frontier delta
(Claude Opus 4.7) rather than deferring to a future run. Prior 2026-05-15 logs surfaced
6 deltas but explicitly deferred synthesis — this run inverts that pattern per the
cron directive's anti-pattern warning ("don't write diary entries deferring").

## What was executed

| Step | Action | Result |
|---|---|---|
| 1 | `wiki_fetch` Anthropic Newsroom + MarkTechPost Opus 4.7 articles | 2 raws saved (`raw/articles/introducing-claude-opus-47-anthropic.md`, `raw/articles/anthropic-releases-claude-opus-47-a-major-upgrade-for-agentic-coding-high-resolu.md`) |
| 2 | Read raws IN FULL (Hard Rule 1) | wc -l confirmed; both raws read in full via `Read` tool |
| 3 | Authored `wiki/sources/ai-models/src-anthropic-claude-opus-4-7-release-2026-04-16.md` | 197 lines, 9 frontmatter fields, all required sections, 2 sources cited with file refs |
| 4 | `pipeline crossref` | 1324 RELATES TO + 810 BUILDS ON across corpus; 549 comparison candidates surfaced |
| 5 | `pipeline post` | Status: indexes rebuilt, 873 pages, 4080 relationships, **3 pre-existing validation errors in unrelated files** (NOT introduced by this synthesis — see "Validation note" below) |
| 6 | Affected-page flags identified | 8 pages flagged in synthesis "Pages Affected" section — operator-queue entry below |

## Synthesis page highlights

Title: **Claude Opus 4.7 — 2026-04-16 GA Release**

- Position: top of Claude GA tier (below restricted Mythos Preview)
- Pricing: $5/$25 per MTok input/output — UNCHANGED from Opus 4.6
- Tokenizer change: same input → 1.0–1.35× more tokens (operational economic risk to measure)
- Headline benchmarks: +13% on 93-task coding · CursorBench 70% vs 58% · XBOW visual-acuity 98.5% vs 54.5% · Rakuten-SWE-Bench 3× more resolved · Notion +14% at fewer tokens and 1/3 tool errors
- New levers: `xhigh` effort level, task budgets (public beta), `/ultrareview` slash command, auto-mode for Max users in Claude Code
- Vision: 3× resolution (2,576 px long edge, ~3.75 MP) — model-level change, not API opt-in
- Behavioral shift: self-verification — model devises ways to verify own outputs before reporting (8 of 28 testers independently surfaced this)
- Migration warning: literal instruction-following sharper than Opus 4.6 → existing prompts/harnesses need re-tuning
- 3rd-party harness signal (MarkTechPost sidebar): Cline CLI 74.2% on Terminal Benchmark 2.0 vs Claude Code 69.4% on same Opus 4.7 → harness layer still extracts value even with self-verifying model

## Pages flagged for update (operator-decision-queue P2)

The synthesis identified 8 existing pages whose claims may now be outdated:

1. [[model-registry]] — top GA tier reference doesn't mention Opus 4.7
2. [[ai-models-domain-overview]] — model tier landscape
3. [[ai-infrastructure-decision-framework-2026]] — capability comparison table needs new row
4. [[model-claude-code]] — `xhigh` default raise, `/ultrareview`, auto mode, instruction-following re-tune
5. [[T002-run-openrouter-smoke-tests]] — model strings outdated (K2.6 + Opus 4.x + GPT-5.4 → add Opus 4.7 + GPT-5.5 Instant)
6. [[src-anthropic-programmatic-credit-pool-policy-change-2026-06-15]] — credit pool covers Opus 4.7
7. [[src-rethinking-ai-agents-harness-engineering-rise]] — self-verification is new evidence (thesis still holds; needs amendment)
8. [[src-anthropic-effective-harnesses-long-running-agents]] — tokenizer/xhigh/file-system-memory addendum

These are FLAGGED, not edited — operator approves any edits to existing synthesis pages and operator-territory references.

## Other deltas — handoff (NOT processed this tick)

Per cron budget (5 min model time), only the highest-impact delta was processed end-to-end.
Remaining deltas surfaced in prior 2026-05-15 logs that still need full synthesis:

| Delta | Source URLs | Rationale for next-run priority |
|---|---|---|
| **GPT-5.5 Instant** (OpenAI 2026-05-05 new ChatGPT default) | https://techcrunch.com/2026/05/05/openai-releases-gpt-5-5-instant-a-new-default-model-for-chatgpt/ · https://beginnersinai.org/whats-new-chatgpt-2026/ | HIGH — direct comparison target to Opus 4.7 in our smoke tests; affects model-registry and decision framework |
| **Microsoft Agent Governance Toolkit** (2026-04-02) | https://opensource.microsoft.com/blog/2026/04/02/introducing-the-agent-governance-toolkit-open-source-runtime-security-for-ai-agents/ | MEDIUM — agent-runtime security; touches openclaw / harness pages; OWASP-10 agentic risks coverage |
| **Cline SDK / `@cline/sdk` open-source** (MarkTechPost sidebar 2026-05-14) | https://www.marktechpost.com (Cline SDK announcement); needs separate fetch | MEDIUM — agent-runtime; Cline outperformed Claude Code 74.2% vs 69.4% on Opus 4.7 — harness-engineering evidence |
| Claude Mythos Preview, GPT-Rosalind, Claude Design, Claude Managed Agents v2 | (per prior 2026-05-15 frontier-delta log) | LOW — restricted / niche / already-noted-but-low-vision-impact for this project |

## Validation note

`pipeline post` reports 3 validation errors — ALL in files predating this tick:
- `wiki/log/2026-05-08-PRE-COMPACT-HANDOFF-MANUAL-imminent-compaction-state-snapshot.md` (operator-authored, missing Summary section)
- `wiki/patterns/01_drafts/finish-smoothly-custom-idempotent-pre-compact-handoff-with-existing-doc-detection.md` (missing source ref, missing "When Not To" section)

Per stay-in-lane and don't-pollute-operator-territory, these are NOT fixed in this run.
Surfaced for operator awareness only. The Opus 4.7 synthesis itself validates cleanly.

## Compliance check

- ✅ Hard Rule 1 (read raws in full) — `wc -l` first, both raws read end-to-end
- ✅ Hard Rule 6 (no WebFetch on corpus URLs) — `wiki_fetch` for both URLs
- ✅ ≥0.25 raw-to-synthesis ratio — raws ~17k words, synthesis 197 lines of dense structured content
- ✅ 9 frontmatter fields + required sections (Summary, Key Insights, Deep Analysis, Open Questions, Relationships)
- ✅ Stayed in lane — surfaced 8 affected pages; did NOT auto-edit any
- ✅ Did NOT auto-promote maturity tier (synthesis lands at `maturity: seed` per template default)
- ✅ Operator-decision-queue path: surfaced in this log + recommend P2 entry by operator
- ✅ Budget honored — single end-to-end synthesis + handoff log, ~5 min target

## Tags
log, completion, continuous-research, opus-4-7, source-synthesis-shipped, frontier-delta-executed
