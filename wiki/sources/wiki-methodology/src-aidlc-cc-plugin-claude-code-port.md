---
title: "Synthesis — ijin/aidlc-cc-plugin: Community Claude Code Port of AWS AI-DLC (Grain of Salt)"
aliases:
  - "Synthesis — AIDLC CC Plugin"
  - "ijin/aidlc-cc-plugin"
type: source-synthesis
domain: wiki-methodology
status: synthesized
confidence: low
maturity: seed
created: 2026-04-25
updated: 2026-04-25
layer: 1
sources:
  - id: src-ijin-aidlc-cc-plugin
    type: documentation
    url: https://github.com/ijin/aidlc-cc-plugin
    file: raw/articles/ijinaidlc-cc-plugin.md
    title: "ijin/aidlc-cc-plugin — AI-DLC Plugin for Claude Code"
    ingested: 2026-04-24
tags: [synthesis, aidlc, claude-code, plugin, community-port, low-confidence, grain-of-salt, three-phase-workflow, chat-based-qa, plugin-marketplace, mit-0]
---

# Synthesis — ijin/aidlc-cc-plugin: Community Claude Code Port of AWS AI-DLC

## Summary

> [!warning] **Operator framing (2026-04-24, verbatim):** *"https://github.com/ijin/aidlc-cc-plugin (to take with a grain of salt)"*

`ijin/aidlc-cc-plugin` is a **community port of [[src-aidlc-aws-driven-development-lifecycle|AWS AI-DLC Workflows]] for Claude Code's plugin system**. It packages the upstream `awslabs/aidlc-workflows` methodology (three-phase Inception → Construction → Operations workflow) as an installable Claude Code plugin invokable via `/aidlc:start <intent>` slash command. **Distribution shift:** plugin marketplace install vs upstream's manual rules-file copy. **Material divergence from upstream:** **chat-based Q&A** (questions answered in conversation) instead of upstream's **file-based Q&A** (multi-choice questions in markdown with `[Answer]:` tags). The author tracks upstream releases version-for-version (currently 0.1.8 = upstream 0.1.8). License MIT-0 (same as upstream). **Confidence: low** per operator-flagged "grain of salt" — community-maintained without DCO/formal contribution process; methodology divergences from upstream are unilateral author decisions, not AWS-sanctioned.

> [!info] Source Reference
> | Attribute | Value |
> |---|---|
> | Source | github.com/ijin/aidlc-cc-plugin |
> | Type | Claude Code plugin (community port of awslabs/aidlc-workflows) |
> | Author | ijin (community contributor, not affiliated with AWS) |
> | License | MIT-0 |
> | Latest version | 0.1.8 (2026-04-20) — synced with awslabs/aidlc-workflows v0.1.8 |
> | Trigger | `/aidlc:start <intent>` slash command |
> | Operator stance | "grain of salt" — confidence low |

## Key Insights

### 1. Distribution shift — plugin marketplace vs manual rules-file copy

> [!abstract] How install differs
>
> | Step | Upstream (awslabs) | This plugin (ijin) |
> |---|---|---|
> | 1. Add source | Download zip from GitHub Releases | `/plugin marketplace add ijin/aidlc-cc-plugin` |
> | 2. Install | Manually copy `core-workflow.md` to CLAUDE.md / AGENTS.md / `.cursor/rules/` etc. per platform | `/plugin install aidlc@aidlc-cc-plugin` |
> | 3. Trigger | "Using AI-DLC, ..." prefix in chat | `/aidlc:start <intent>` |
> | 4. Resume | Operator manually re-references state | Auto-detects `aidlc-docs/aidlc-state.md`, offers resume |
>
> **Trade-off:** the plugin path is faster onboarding for Claude Code users specifically, but **only works with Claude Code**. The upstream methodology is multi-platform (Kiro, Q, Cursor, Cline, Claude Code, Copilot, Codex). If you're committed to Claude Code, the plugin is more convenient. If you're cross-tool or evaluating, the upstream is the canonical source.

### 2. The chat-based Q&A divergence — material methodology change

> [!warning] **The most consequential difference from upstream**
>
> Upstream awslabs/aidlc-workflows: **questions go into markdown files** with multiple-choice options + `[Answer]:` tags + X for "other" — see [[src-aidlc-aws-driven-development-lifecycle|AWS AI-DLC synthesis]] §4 for the full pattern.
>
> This plugin: **questions go directly into chat conversation**. From the README:
>
> > "Chat-Based Interaction — Answer questions directly in conversation. No file editing required."
>
> The plugin even asks at startup which Q&A style the user prefers:
>
> | Option | Format |
> |---|---|
> | **Interactive UI** | Clickable buttons via `AskUserQuestion` tool (recommended for ease of use) |
> | **Text responses** | Type answers like "1: A, 2: B" |
>
> **Why this matters:** the upstream's file-based Q&A pattern is one of AIDLC's defining structural choices — it externalizes decisions into durable, version-controllable, team-shareable artifacts. The chat-based replacement loses that property. The conversation history isn't a usable audit substitute for `aidlc-docs/<phase>/<stage>/<question>.md` artifacts because chat history doesn't survive context resets and can't be reviewed by a teammate offline. **The plugin author chose ergonomics over upstream methodology fidelity** — a defensible trade-off for solo Claude Code users, but a deviation worth tracking. The audit trail moves to `aidlc-docs/audit.md` only, with chat conversations as the primary input source.

### 3. Three-phase workflow inherited verbatim from upstream

The plugin uses the same Inception → Construction → Operations flow with the same per-phase artifact decomposition:

```
INCEPTION:    Workspace Detection → Reverse Engineering (brownfield) → Requirements Analysis →
              User Stories (conditional) → Workflow Planning → Application Design (conditional) →
              Units Generation (conditional)

CONSTRUCTION: Per-Unit Loop:
                Functional Design (conditional) → NFR Requirements (conditional) →
                NFR Design (conditional) → Infrastructure Design (conditional) →
                Code Generation (always, with plan approval)
              After All Units: Build and Test

OPERATIONS:   (Placeholder for future)
```

The artifact directory structure is also inherited (mostly):

```
aidlc-docs/
├── aidlc-state.md          # Progress tracking with checkboxes
├── audit.md                # Complete audit trail with timestamps
├── inception/
│   ├── workspace-analysis.md
│   ├── reverse-engineering/  # brownfield only
│   ├── requirements/
│   ├── user-stories/
│   ├── application-design/
│   └── plans/
├── construction/
│   ├── unit-01/
│   │   ├── functional-design/
│   │   ├── nfr-requirements/
│   │   ├── nfr-design/
│   │   └── infrastructure-design/
│   └── build-and-test/
└── operations/             # placeholder
```

### 4. Quality-of-life additions in the plugin

The plugin adds Claude Code-specific niceties that aren't in upstream:

| Addition | What it does |
|---|---|
| **Interactive UI Q&A option** | Clickable buttons via Claude Code's `AskUserQuestion` tool — better UX than typing answers |
| **Auto session resume** | Detects existing `aidlc-docs/aidlc-state.md` on `/aidlc:start` and offers to continue from last checkpoint |
| **ASCII-only diagram enforcement** | Disallows Unicode box-drawing characters in diagrams (`┌` `─` `│` `└`) for maximum cross-platform rendering — enforces basic ASCII (`+` `-` `|`) with character-width validation |
| **Mermaid validation with text fallback** | Validates Mermaid syntax before writing; falls back to text representation if validation fails |
| **`disable-model-invocation: true`** on the skill | Prevents the model from auto-invoking the workflow without operator's explicit `/aidlc:start` |

### 5. Three commit-strategy options for `aidlc-docs/`

The plugin documents three ways to handle the generated artifacts directory:

| Option | When | Trade-off |
|---|---|---|
| **Commit everything** (recommended for team projects) | `git add aidlc-docs/` | Full audit trail + design docs reviewable by team; enables onboarding |
| **Gitignore** (recommended for personal projects) | `echo "aidlc-docs/" >> .gitignore` | Treat as local working notes; reduces repo size; regenerate on demand |
| **Selective commit** | gitignore `audit.md`, `aidlc-state.md`, `workspace-analysis.md` | Commit design docs only; ignore temp artifacts |

This explicit guidance is **a useful addition over upstream**, which doesn't address the question.

### 6. Upstream tracking discipline

The CHANGELOG shows the plugin syncs version-for-version with upstream:

| Plugin version | Upstream sync |
|---|---|
| 0.1.8 (2026-04-20) | awslabs/aidlc-workflows v0.1.8 — opt-in prompts in user's conversation language |
| 0.1.7 (2026-04-02) | awslabs/aidlc-workflows main (30 commits ahead of v0.1.6) — context-optimized extensions, "phase" → "stage" terminology |
| 0.1.6 (2026-03-05) | v0.1.6 — copy-paste error fix, application-design.md consolidation |
| 0.1.5 (2026-02-24) | v0.1.5 — security extensions framework with OWASP Top 10 baseline (15 SECURITY rules) |
| 0.1.2 (2026-02-08) | v0.1.2 — frontend components generation, automation-friendly code rules with `data-testid` |
| 0.1.0 (2026-02-03) | Initial marketplace release; based on AWS AI-DLC Workflows reference impl |

The author skipped upstream v0.1.3 (bug fix reverted, net zero rule changes) and v0.1.4 (path resolution only, not applicable to plugin). This is **diligent tracking**, but every sync is an opportunity for divergence — the chat-based Q&A divergence is the largest example.

### 7. Why "grain of salt" is the right operator stance

> [!warning] **Specific risks worth tracking**
>
> | Risk | Severity |
> |---|---|
> | **Community maintenance** — no DCO, "no formal process required, just good code and clear commit messages" per the README | Medium — bus-factor dependency on a single maintainer |
> | **Methodology divergence from upstream** — chat-based Q&A is a unilateral author decision, not AWS-sanctioned | Medium — using this plugin and citing "AIDLC compliance" is misleading; you're using an AIDLC-shaped community methodology |
> | **License is MIT-0** — same as upstream, so no licensing concern | None |
> | **Plugin lock-in to Claude Code** — only works in Claude Code; upstream is multi-platform | Low — acceptable if Claude Code is the operator's chosen runtime |
> | **Update lag** — plugin lags upstream by N days/weeks during sync windows | Low — historical pattern shows ~2-4 week lag at most |
>
> **For this wiki's purposes:** the upstream `awslabs/aidlc-workflows` is the canonical source for AIDLC methodology study and comparison. This plugin is operationally interesting as **a worked example of porting a methodology to a specific agent runtime** — relevant if the wiki ever publishes its own methodology as a Claude Code plugin (see open question in [[src-aidlc-aws-driven-development-lifecycle|AWS AI-DLC synthesis]]).

## Open Questions

> [!question] Should the wiki publish its methodology as a Claude Code plugin similar to ijin's port?
> ijin proves the pattern works: community packages an upstream methodology as a Claude Code plugin → solves install friction. The wiki's methodology framework (config + standards + spine models) could ship the same way for sister projects: `/plugin install wiki-methodology@<wiki-org>`. Trade-off: the wiki's methodology evolves continuously (no release cadence) — packaging would force versioning discipline. Connects to the upstream-AIDLC-versioning open question. Requires: operator decision on whether to release-engineer the wiki methodology.

> [!question] How does the chat-based vs file-based Q&A trade-off generalize?
> ijin chose chat-based for ergonomics; upstream chose file-based for durability. Both are defensible. The wiki currently uses **operator-directive-in-chat** (closer to chat-based) but logs verbatim to `raw/notes/` after-the-fact. Could the wiki gain from upstream-AIDLC's pre-structured question files? Already noted as an open question in [[src-aidlc-aws-driven-development-lifecycle|AWS AI-DLC synthesis]] §Open Questions.

## Relationships

- DERIVED FROM: [[src-ijin-aidlc-cc-plugin|ijin/aidlc-cc-plugin GitHub Repository]]
- BUILDS ON: [[src-aidlc-aws-driven-development-lifecycle|Synthesis — AWS AI-DLC: AI-Driven Development Lifecycle]] (upstream — this is the canonical reference)
- COMPARES TO: [[src-aidlc-aws-driven-development-lifecycle|AWS AI-DLC]] (the central comparison axis — divergence on Q&A model is the headline)
- COMPARES TO: [[model-skills-commands-hooks|Model — Skills, Commands, and Hooks]] (the plugin uses Claude Code skills as the implementation substrate)
- RELATES TO: [[model-claude-code|Model — Claude Code]] (Claude Code-specific methodology delivery)
- RELATES TO: [[model-methodology|Model — Methodology]] (the wiki's methodology that could be similarly plugin-packaged)

## Backlinks

[[ijin/aidlc-cc-plugin GitHub Repository]]
[[Synthesis — AWS AI-DLC: AI-Driven Development Lifecycle]]
[[AWS AI-DLC]]
[[model-skills-commands-hooks|Model — Skills, Commands, and Hooks]]
[[model-claude-code|Model — Claude Code]]
[[model-methodology|Model — Methodology]]
