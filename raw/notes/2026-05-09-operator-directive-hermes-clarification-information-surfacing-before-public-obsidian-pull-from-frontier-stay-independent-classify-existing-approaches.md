---
title: "2026-05-09 — Operator directive (turn 2): Hermes clarification (typo), information must surface before public Obsidian, pull from frontier + stay independent, ingest 7 URLs (1 YouTube + 6 GitHub/web) and classify by type/frontier at high standards"
type: note
note_type: directive
domain: cross-domain
status: raw
confidence: high
created: 2026-05-09
updated: "2026-05-09"
sources:
  - id: operator-directive-2026-05-09-turn-2
    type: directive
    description: "Operator-stated directive 2026-05-09 (turn 2 of E024 arc) — Hermes is Greek messenger god typo correction; new information-surface-before-public-obsidian requirement; ingest YouTube + 6 GitHub/web examples of assistants/profiles; classify by type and frontier"
tags: [operator-directive, sacrosanct, verbatim, "2026-05-09", hermes-clarification, information-surfacing, pre-public-obsidian, frontier-pulling, anti-vendor-lock-in-strategic, classify-existing-approaches, claude-os, obsidian-pm, multica, openclaw-command-center, ocmc, raw-note, ai-agents]
---

# Operator directive — 2026-05-09 (turn 2): Hermes clarification + information-surfacing + classify existing approaches

## Verbatim (operator, sacrosanct)

> "obviously i meant hermes lol.. how ridiculous is this doubt XD...
> continue, we will also have to find a way to make the information surface somehow even before it reaches the public obsidian.
>
> There are few thing happening and I think this video to injest explain a bit of the situation:
> https://www.youtube.com/watch?v=RrMTtG1ZccI
>
> Claude / anthropic and etc are going to improve, they might even deliver feature that render doing something yourelf manually outdated and such and we have to keep up and find the right way to adapt and still remain non vendor lock. Pull the level from the frontier and remain independant.
>
> So now I see a few examples:
> https://thebob.dev/ai/tools/productivity/2025/10/31/why-we-built-claude-os-and-what-it-actually-is/
> https://github.com/brobertsaz/claude-os
>
> https://github.com/StepanKropachev/obsidian-pm
>
> https://github.com/multica-ai/multica
>
> for assistants:
> https://github.com/jontsai/openclaw-command-center
>
> https://github.com/cyberpunk042/ocmc-backup
>
> We need to see them all and which is the frontier of each type and then classify them and document this properly with a grids / tables and everything at high standards.
> We can even find more, this is only what I found.
>
> And for doing what I want to do right now there are probably also already defined ways we can integrate and adapt. and yes this is also about the AI Assistants profiles and sub-agents and skills(+chains)."

## Decomposition

### A — Hermes clarification (resolved)
- "obviously i meant hermes lol.. how ridiculous is this doubt XD..." → Hermes is the Greek messenger god (operator-flagged as obvious; my earlier doubt was the over-cautious pattern); typo "Hermess" should not have surfaced as a clarification question
- Action: artifacts updated (Epic, Decision, Pattern, Source-synthesis, Task) to use "Hermes"; raw-note primary verbatim preserves "Hermess [operator typo — clarified as Hermes]" for historical record
- **Lesson candidate**: when operator typos resemble common-word/known-pattern (e.g., classical-name-with-extra-letter), assume the intended common word rather than flag as ambiguous

### B — Information must surface before public Obsidian
- "we will also have to find a way to make the information surface somehow even before it reaches the public obsidian"
- The /opt wiki content currently surfaces to operator via the **public Obsidian** vault (the published vault — see `wiki_sync` MCP / `tools.sync`)
- Operator wants an EARLIER surfacing mechanism — information accessible BEFORE the Obsidian sync completes
- Possible mechanisms (TBD per operator-direction):
  - Real-time wiki query MCP (already exists — operator may want to expose more)
  - Pre-sync intermediate view (web dashboard, API endpoint, RSS feed)
  - Per-project assistant integration that surfaces fresh content directly
  - Live "what just changed" stream
- Capture as a forward-direction; not an immediate-build directive

### C — Frontier-pulling + non-vendor-lock-in (strategic frame)
- "Claude / anthropic and etc are going to improve, they might even deliver feature that render doing something yourelf manually outdated and such and we have to keep up and find the right way to adapt and still remain non vendor lock"
- "Pull the level from the frontier and remain independant"
- The strategic doctrine: **consume from the frontier of AI capabilities, but stay independent**
- Implication: Profile/Assistant architecture must remain pluggable — if Anthropic ships a feature that obsoletes our manual approach, we adopt it; if a non-Anthropic alternative is better, we route there
- Confirms the runtime-agnostic pattern of E024 + the [[anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence|anti-vendor-lock-in mission claim]]
- The YouTube ingestion (skill-chaining-in-claude-os) is operator's evidence frame for "Claude features that may render manual approaches outdated"

### D — Ingest 7 URLs (done — 6 fetched, multica pre-existed)
1. https://www.youtube.com/watch?v=RrMTtG1ZccI — "Skill chaining in claude-os is insane don't fall behind" (YouTube)
2. https://thebob.dev/ai/tools/productivity/2025/10/31/why-we-built-claude-os-and-what-it-actually-is/ — Claude OS author article
3. https://github.com/brobertsaz/claude-os — Claude OS repo (12,518 lines)
4. https://github.com/StepanKropachev/obsidian-pm — Obsidian PM (5,293 lines)
5. https://github.com/multica-ai/multica — Multica (23,363 lines; already in raw/)
6. https://github.com/jontsai/openclaw-command-center — Original OpenClaw Command Center (assistants category)
7. https://github.com/cyberpunk042/ocmc-backup — Operator's backup of OCMC (assistants category)

### E — Classify by type + frontier + grids/tables at high standards
- Comparison page with structured tables comparing each tool/approach
- Identify the FRONTIER of each type (best-in-class within a category)
- Categories to discover (preliminary): Claude OS pattern · Obsidian PM-in-vault · Multi-agent orchestration · Assistant Mission Control
- "everything at high standards" → use proper schema, admonition styling, ratio-respecting, cross-referenced

### F — Find more
- "We can even find more, this is only what I found"
- Inviting additional research candidates beyond the 7 named — but bounded by current arc (don't expand indefinitely)

### G — Integration paths + Profiles + sub-agents + skills+chains
- "for doing what I want to do right now there are probably also already defined ways we can integrate and adapt"
- The existing approaches (Claude OS, Obsidian PM, Multica, OCMC) likely have patterns we can adopt rather than reinvent
- "yes this is also about the AI Assistants profiles and sub-agents and skills(+chains)"
- The Profile pattern (E024) IS about assistants; sub-agents and skills+chains are adjacent abstractions
- Skills + chains: existing pattern in the wiki ([[model-skills-commands-hooks|Model — Skills, Commands, Hooks]]); pair with Profiles

## Action plan

| # | Action | Type | Status |
|---|---|---|---|
| 1 | Log verbatim BEFORE acting (this file) | hard rule | ✅ done |
| 2 | Pipeline fetch 7 URLs | ingestion | ✅ done (6 fetched, 1 pre-existed) |
| 3 | Update artifacts: Hermes typo correction (Epic, Decision, Pattern, Source, T078) | cleanup | ✅ done |
| 4 | Read all 6 new raws + 1 pre-existing (Multica) | reading | pending |
| 5 | Author comparison/classification page with grids/tables at high standards | synthesis | pending |
| 6 | Identify frontier of each type | analysis | pending |
| 7 | Update E024 with cross-references to the comparison page + frontier findings | epic update | pending |
| 8 | Capture "information surface before public Obsidian" as a forward-direction item | direction note | pending |
| 9 | Capture "frontier-pulling + stay independent" as a doctrinal extension | doctrine note | pending |
| 10 | Pipeline post + report | gate | pending |

## No-conflate guard

- **"obviously i meant hermes lol"** — operator-clarified meaning; not authorization to flag every typo as ambiguous; common-word-typo pattern = assume intent
- **"information surface before public obsidian"** — this is a NEW requirement direction, not part of E024; capture separately, address later
- **"Pull the level from the frontier and remain independant"** — strategic doctrine, not immediate-build directive. Inform the Profile design (runtime-agnostic preserves it) but don't expand E024 scope
- **"a few examples" + "We can even find more"** — bounded research; don't expand indefinitely. Comparison is across the 7 named tools + 1-2 additional if found in their cross-refs
- **"already defined ways we can integrate and adapt"** — pointer to use existing approaches as inputs to the Profile design, not as replacements
- **"AI Assistants profiles and sub-agents and skills(+chains)"** — three related but distinct concepts. Profiles = E024 (declarative). Sub-agents = within an assistant's runtime. Skills+chains = composable workflow units. Keep distinct in the analysis.

## Forward chain (this arc)

- BUILDS ON: [[2026-05-09-operator-directive-per-project-assistant-configs-spawn-openclaw-openarms-hermess-and-anthropic-programmatic-budget-policy-research|2026-05-09 directive turn 1]]
- EXTENDS: [[e024-per-project-assistant-configurations-to-capture-programmatic-credit-and-enable-ecosystem-spawn|E024 Epic]] — research inputs for Profile design
- RELATES TO: [[anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence|Lesson — Anti-Vendor-Lock-In as empirical claim]] — strategic frame
