---
title: "Repo Documentation Overhaul — README + Root Docs Polish for Hyper-Clean, Sell-Worthy, Navigation-Coherent Repo (2026-04-28)"
aliases:
  - "Repo Docs Overhaul Epic"
  - "README + Root Docs Polish 2026-04-28"
  - "Documentation Polish Epic"
type: epic
domain: backlog
status: active
priority: P0
task_type: epic
current_stage: document
readiness: 25
progress: 5
stages_completed:
  - "document"
artifacts: []
confidence: high
created: 2026-04-28
updated: 2026-04-28
last_reviewed: 2026-04-28
sources:
  - id: operator-directive
    type: directive
    file: wiki/log/2026-04-28-session-log-post-anthropic-3-layer-stack-assembly-multica-adoption.md
    description: "Operator verbatim 2026-04-28 — *'we will also need to do a massive github markdown upgrade and make the project / repo hyper clear and clean and working and lean and smooth and strong. Yeah the readme is serving a purpose but I have to be able to find my track into the real documentation and what I want to see as a user and whatnot or how I want to sell / praise this tool and whatnot.'* The session log captures the day-arc verbatim directives; this directive is the latest one driving net-new mission scope."
  - id: current-readme
    type: file
    file: README.md
    description: "412 lines — current README state. Has substance but mixes setup detail with conceptual content; stale page count (339+ → actual 523); no sell/praise framing; no scan-and-find optimization."
  - id: current-root-docs
    type: file
    file: ARCHITECTURE.md
    description: "Root docs total: 3044 lines (README 412 + CLAUDE 119 + AGENTS 178 + CONTEXT 234 + ARCHITECTURE 632 + DESIGN 355 + TOOLS 839 + SKILLS 275). ARCHITECTURE.md (632 lines) is the largest single root doc; representative anchor for this source entry. Substantial total — operator-stated need: lean."
tags: [epic, p0, documentation, readme, repo-polish, github-markdown, sell-praise, user-facing, navigation, lean, mission-2026-04-28, refactor-model]
---

# Epic — Repo Documentation Overhaul (README + Root Docs Polish)

## Summary

The operator stated 2026-04-28 a milestone-class workstream: **make the project / repo hyper clear, clean, working, lean, smooth, and strong** at the GitHub-facing layer. Current state: README is 412 lines, 8 root docs total **3044 lines** (CLAUDE 119 · AGENTS 178 · CONTEXT 234 · ARCHITECTURE 632 · DESIGN 355 · TOOLS 839 · SKILLS 275 + README 412). The README has substance but mixes setup detail with conceptual content, has a stale page count (339+ vs actual 523), and lacks both **navigation-track-to-real-documentation** AND **sell/praise framing**. Operator's directive captures three distinct concerns: (1) **user-facing first impression** — what someone sees on GitHub, can they find what they need; (2) **navigation** — track from README into the deeper documentation efficiently; (3) **sell/praise** — convey the substantive value of what's built (3-layer post-Anthropic stack · 523 pages · 25 standards · 16 models · 4 principles · 6 P4-instances closed via gateway audit · empirically-traceable mission claim at 3 layers · self-host Multica + AICP + 3090-incoming · etc.). This epic captures the work as backlog with module breakdown so it doesn't get lost between sessions.

## Operator Directive (verbatim, sacrosanct)

> *"we will also need to do a massive github markdown upgrade and make the project / repo hyper clear and clean and working and lean and smooth and strong."*

> *"Yeah the readme is serving a purpose but I have to be able to find my track into the real documentation and what I want to see as a user and whatnot or how I want to sell / praise this tool and whatnot."*

The two-part framing: (a) operator-as-user navigating into deeper docs; (b) operator-as-promoter conveying the project's substance to others.

## Goals

- **README rewrite** — top of repo, scan-and-find optimized. ~150 lines max (currently 412). Lead with what this IS (one sentence) + headline numbers (live state, not stale) + two clear navigation tracks (user / agent / contributor). Sell/praise framing in opening — what's been built that's substantively impressive.

- **Root-doc audit + lean pass** — across 7 other root docs (CLAUDE · AGENTS · CONTEXT · ARCHITECTURE · DESIGN · TOOLS · SKILLS), identify and remove redundancy / stale claims / over-elaborated sections. Target: total root-doc footprint reduced by 25-40% without losing substance. Goal isn't "shorter for shorter's sake" — it's "lean enough that operator can actually find what they need."

- **Navigation track from README → real documentation** — explicit reading paths for: (a) user-evaluating-tool · (b) operator-returning-to-codebase · (c) AI-agent-onboarding · (d) contributor-considering-PR · (e) sister-project-integrator. Each path = ordered link sequence with annotations. Path A from the [3-layer stack learning path](../../spine/learning-paths/post-anthropic-3-layer-stack-2026-04-28.md) is the model.

- **Sell / praise framing** — opening section conveys the substantive achievements without being marketing-fluff. Concrete: 523 pages · 16 models · 4 principles · 6 P4-instances closed via wiki's own audit · empirically-traceable anti-vendor-lock-in mission claim at 3 structural layers · post-Anthropic stack assembly · etc. **Show, don't tell** — link to specific artifacts that demonstrate substance.

- **Visual / structural polish** — proper heading hierarchy, scan-and-find tables, consistent callout vocabulary per [DESIGN.md](../../../DESIGN.md), no broken wikilinks, no dead anchors. Possibly diagrammatic representation of the 5-project ecosystem + 3-layer stack architecture (Mermaid diagrams render natively on GitHub).

- **Working** — every command / link / reference in the docs actually works. No stale tool references, no dead links, no commands that fail.

- **Strong** — the reading experience conveys confidence in the system. Quality bar set by the wiki's own [Wiki Design Standards](../../../wiki/spine/standards/) and per the existing root-docs (DESIGN.md captures the design language; the README and root docs should embody it).

## Done When

- [ ] README rewritten — ≤150 lines, scan-and-find optimized, opens with sell/praise framing + 5 navigation tracks
- [ ] Headline numbers in README are LIVE (computed or auto-updated, not hardcoded stale)
- [ ] CLAUDE.md / AGENTS.md / CONTEXT.md / ARCHITECTURE.md / DESIGN.md / TOOLS.md / SKILLS.md each audited; redundancies removed; broken links fixed; stale claims updated
- [ ] Total root-doc footprint reduced by 25-40% from 3044 lines (target: ~1800-2300 lines) WITHOUT loss of substance
- [ ] Navigation tracks documented for 5 user types (user · operator · AI agent · contributor · sister-project)
- [ ] Sell/praise opening references the 2026-04 milestone achievements (3-layer stack · 6 P4 closures · empirical mission claim · etc.) with concrete page links
- [ ] Mermaid or equivalent diagram(s) of (a) 5-project ecosystem · (b) 3-layer post-Anthropic stack architecture
- [ ] Every command in setup section verified to work end-to-end
- [ ] Every wikilink / anchor verified non-broken
- [ ] `python3 -m tools.pipeline post` returns 0 validation errors after all changes commit
- [ ] Operator final review: opens README on GitHub, can scan in <30 seconds and know what this is + how to navigate

## Scale and Model

> [!info] Epic Parameters
>
> | Parameter | Value |
> |---|---|
> | **Methodology model** | refactor (document → scaffold → implement → test) — restructure without changing the wiki's behavior; root docs are the artifact |
> | **Quality tier** | Skyscraper — operator stated this as substantial workstream; operator-final-review gate |
> | **Estimated modules** | 5 |
> | **Estimated tasks** | 15-25 |
> | **Cash budget** | $0 — all work is documentation editing |
> | **Hardware budget** | $0 — no hardware impact |
> | **Critical-path target** | TBD — operator decides timing relative to other priorities |

## Module Breakdown

| Module | Delivers | Est. Tasks |
|---|---|---|
| **M001 — README Rewrite** | New README ≤150 lines · sell/praise opening · 5 navigation tracks · live headline numbers · Mermaid diagrams · scan-and-find optimization | 4-5 |
| **M002 — Root-Doc Audit + Lean Pass** | 7 root docs audited; redundancies / stale claims / dead links removed; ~25-40% footprint reduction without substance loss | 6-8 |
| **M003 — Navigation Coherence** | Cross-references between root docs verified; entry points clear; no dead-end docs; navigation paths documented | 3-4 |
| **M004 — Sell/Praise Section + Achievements Showcase** | Opening sell/praise with 2026-04 milestone references; "Why this exists" framing; concrete substance links | 2-3 |
| **M005 — Verification Pass** | Every command runs; every link works; mermaid diagrams render on GitHub; operator-final-review gate | 2-3 |

## Dependencies

- **External**: Operator's review/feedback at the end of each module (final-review gate per operator's "what I want to see as a user" framing)
- **Wiki**: existing [DESIGN.md](../../../DESIGN.md) — design language reference for the rewrite
- **Wiki**: existing learning paths ([3-layer stack](../../spine/learning-paths/post-anthropic-3-layer-stack-2026-04-28.md) · [RLM thread](../../spine/learning-paths/rlm-thread-evidence-chain-2026-04-27.md)) — model for navigation-track structure
- **Wiki**: existing per-type standards ([wiki/spine/standards/](../../spine/standards/)) — quality bar reference
- **Hardware**: NOT blocked

## Open Questions

> [!question] Should headline numbers in README be auto-computed (live) or written prose?
> Auto-computed (e.g., a build step that reads `pipeline status` and substitutes into README) is more durable but adds tooling. Prose is simpler but goes stale. Recent wiki history shows page counts in CLAUDE.md and CONTEXT.md going stale repeatedly — auto-computation may be the durable answer. (Resolution: M001 module designs this.)

> [!question] Mermaid diagrams: how detailed?
> 5-project ecosystem has 5 nodes + ~7 edges (manageable). 3-layer stack has orchestrator × harness × provider (3 nested groups + leaves). Both render on GitHub. Risk: over-detailed diagrams become unreadable; under-detailed don't add value. (Resolution: M001 module iterates.)

> [!question] Should sell/praise framing reference the operator's specific mission (anti-vendor-lock-in / post-Anthropic) or stay general?
> Operator-specific framing is more authentic and concrete; general framing is more reusable. The repo IS operator-specific (and self-referential — it's the operator's second brain). Operator-specific framing wins. (Resolution: write opening for the operator first; if a separate "general/marketing" version is needed, that's a separate doc.)

> [!question] What's the right line-count target for total root-doc footprint?
> Currently 3044. Operator said "lean." 25-40% reduction = 1800-2300 target. Need operator agreement on the target — too aggressive may cut substance; too modest may leave bloat. (Resolution: M002 module surfaces specific cut candidates per file; operator decides per file.)

> [!question] How does this epic intersect with the post-Anthropic 3-layer stack epic?
> The 3-layer stack epic captured an architectural milestone. This epic is about communicating that milestone (and prior milestones) effectively at the repo's user-facing layer. The 3-layer epic's outputs (Multica synth, decision page, learning path, etc.) are SOURCES the README rewrite cites. They're parallel, not blocking each other.

## Mission Framing

This epic addresses the **GitHub-facing presentation layer** of the wiki — what a visitor (or returning operator) sees first. Per the operator's framing, the wiki has substantive achievements (3-layer stack · 6 P4 closures · empirical mission claim · 523 pages of structured knowledge) that the current README under-conveys. The epic's success metric is operator-stated: *"I have to be able to find my track into the real documentation"* — when operator returns to the repo and scans the README, they should know in seconds where to go for what they need.

Per [Saturation Lesson Hard Rule #11](../../lessons/01_drafts/saturation-declarations-are-p4-aspirational-test-by-attempting-forward-work.md): the wiki-side completeness of the post-Anthropic 3-layer stack work doesn't mean wiki-side mission work is done. **The presentation layer is its own scope** that wasn't covered by prior epics. Operator surfacing it as a mission item validates that prior "saturation" claims were within-scope-of-prior-work, not stack-wide.

## Relationships

- IMPLEMENTS: [[post-anthropic-self-autonomous-stack|Milestone — Post-Anthropic Self-Autonomous Stack]] (presentation-layer counterpart to the architectural milestones)
- BUILDS ON: [[post-anthropic-stack-3-layer-assembly-multica-aicp-3090|Epic — Post-Anthropic 3-Layer Stack Assembly]] (sources the substance the new README will cite)
- BUILDS ON: [[root-documentation-map|Root Documentation Map]] (existing reference for what root docs exist)
- DEMONSTRATES: [[structured-context-governs-agent-behavior-more-than-content|Principle 2 — Structured Context > Content]] (README structure is structured-context for human + agent visitors)
- DEMONSTRATES: [[infrastructure-over-instructions-for-process-enforcement|Principle 1]] (auto-computed headline numbers = infrastructure, not stale prose)
- RELATES TO: [[post-anthropic-3-layer-stack-2026-04-28|Learning Path — Post-Anthropic 3-Layer Stack]] (model for navigation-track structure)
- RELATES TO: [[rlm-thread-evidence-chain-2026-04-27|Learning Path — RLM Thread Evidence Chain]] (parallel learning-path artifact)
- FEEDS INTO: [[2026-consumer-hardware-ai-stack|2026 Consumer Hardware AI Stack]] (the README's sell/praise opening references this spine doc)

## Backlinks

[[Milestone — Post-Anthropic Self-Autonomous Stack]]
[[Epic — Post-Anthropic 3-Layer Stack Assembly]]
[[root-documentation-map|Root Documentation Map]]
[[Principle 2 — Structured Context > Content]]
[[infrastructure-over-instructions-for-process-enforcement|Principle 1]]
[[Learning Path — Post-Anthropic 3-Layer Stack]]
[[Learning Path — RLM Thread Evidence Chain]]
[[2026 Consumer Hardware AI Stack]]
