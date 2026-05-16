---
title: "purge-summary 2026-05-16 — Cline SDK ephemeral raws"
type: note
domain: log
status: active
confidence: high
maturity: growing
created: 2026-05-16
updated: 2026-05-16
sources: []
tags: [purge-summary, lifecycle, ephemeral-raws, continuous-research, cline-sdk]
---

# Purge Summary — 2026-05-16 — Cline SDK ephemeral raws (continuous-research)

## Summary

Three ephemeral `raw/articles/` files corresponding to the Cline SDK source-synthesis shipped this tick (cron 2026-05-16 14:34 ET) have been purged per LIFECYCLE.md policy. Combined synthesis-to-raw line ratio 7.42 ⋙ 0.25 floor; pipeline post 0-error confirmed pre-purge. Synthesis frontmatter retains `sources[].file` provenance references; source URLs remain in frontmatter for re-fetch if needed.

## Context

Per LIFECYCLE.md ephemeral-raw policy. Synthesis `wiki/sources/tools-integration/src-cline-sdk-open-source-agent-runtime-2026-05-13.md` shipped this tick (cron 14:34 ET); pipeline post 0-error confirmed; all five purge criteria met for each raw below.

## Purged

| Purged raw | Domain | Raw lines | Synthesis line-ratio | Lifecycle list | Rationale |
|---|---|---|---|---|---|
| `raw/articles/introducing-cline-sdk-the-upgraded-agent-runtime-and-we-rebuilt-cline-upon-it-cl.md` | cline.bot (vendor blog) | 8 | 178/24 = 7.42 (combined) | path-default ephemeral (raw/articles/) | Primary vendor announcement; signal fully extracted into source-synthesis Key Insights §1, §2, §3, §7, §8 + Reference card |
| `raw/articles/cline-releases-cline-sdk-an-open-source-agent-runtime-now-powering-its-cli-and-k.md` | marktechpost.com | 8 | 178/24 = 7.42 (combined) | path-default ephemeral (raw/articles/) | Trade press; signal extracted into Key Insights §2 (layer detail), §3 (benchmark numbers), §4-§5 (multi-agent + plugin detail) |
| `raw/articles/cline-releases-open-source-agent-runtime-sdk.md` | testingcatalog.com | 8 | 178/24 = 7.42 (combined) | path-default ephemeral (raw/articles/) | Trade press; signal extracted into §1 (architectural shift quote), §3 (benchmark corroboration), §7 (session-portability claim), §8 (connector channels) |

## Purge criteria audit (all 5 must hold — verified for each above)

1. ✅ Raw path matches `ephemeral` retention (raw/articles/ path-default)
2. ✅ Corresponding synthesis at `wiki/sources/tools-integration/src-cline-sdk-open-source-agent-runtime-2026-05-13.md`
3. ✅ Combined ratio 7.42 ≥ 0.25 floor (single synthesis cites all three raws via frontmatter `file:` links)
4. ✅ Pipeline post this tick = 0 validation errors
5. ✅ No `lifecycle: keep` frontmatter on any of the three raws

## Synthesis provenance retained

The synthesis frontmatter `sources[].file` fields retain references to the purged raw paths as provenance markers — standard practice (cf. prior purge logs `2026-05-15-purge-summary*`). Auditor can reconstruct via the source URL fields if re-fetch needed.

## Addendum — NLA tick (2026-05-16 14:45 ET)

Second synthesis shipped this date: `wiki/sources/ai-models/src-anthropic-natural-language-autoencoders-interpretability-2026-05-07.md` (Anthropic Natural Language Autoencoders, 2026-05-07). Pipeline post: 0 errors / PASS / 903 pages / 4121 relationships. Two raws fetched; one purged, one retained per always-keep list.

| Purged raw | Domain | Raw lines | Synthesis line-ratio | Lifecycle list | Rationale |
|---|---|---|---|---|---|
| `raw/articles/anthropic-introduces-natural-language-autoencoders-that-convert-claude039s-inter.md` | marktechpost.com | 8 | 103/16 = 6.44 (combined) | path-default ephemeral (raw/articles/) | Trade press; signal fully extracted into NLA source-synthesis Key Insights + Reference card; no always-keep override |

| Retained raw | Domain | Reason |
|---|---|---|
| `raw/articles/natural-language-autoencoders-anthropic.md` | www.anthropic.com/research | LIFECYCLE.md `always_keep` list (anthropic.com/research) — reference-value, retained |

Purge criteria check for the marktechpost raw: (1) path/domain ephemeral ✓ (raw/articles/ + marktechpost.com not on always-keep) (2) corresponding synthesis exists ✓ (3) line-ratio 6.44 ≥ 0.25 ✓ (4) pipeline_post 0-error this tick ✓ (5) no `lifecycle: keep` frontmatter ✓. All five hold.

## Relationships

- RELATES TO: [[src-cline-sdk-open-source-agent-runtime-2026-05-13|Cline SDK Synthesis]]
- RELATES TO: [[2026-05-16-flagged-pages-cline-sdk|Cline SDK flagged-pages log]]
- RELATES TO: [[src-anthropic-natural-language-autoencoders-interpretability-2026-05-07|Anthropic NLA Interpretability Synthesis]]
- RELATES TO: [[2026-05-16-flagged-pages-anthropic-nla-interpretability|Anthropic NLA flagged-pages log]]

## Backlinks

[[Cline SDK Synthesis]]
[[Cline SDK flagged-pages log]]
[[Anthropic NLA Interpretability Synthesis]]
[[Anthropic NLA flagged-pages log]]
