---
title: "Cursor State Folder Standards (`.cursor/`) — Common Cross-Project Runtime State Surface for /view · /questions · vision · focus · trace"
aliases:
  - "Cursor State Folder Standards"
  - ".cursor/ Standards"
  - "Cross-Project State Surface Standards"
type: concept
domain: cross-domain
layer: spine
status: synthesized
confidence: high
maturity: seed
created: 2026-05-09
updated: "2026-05-09"
sources:
  - id: operator-directive-2026-05-09-turn-8
    type: directive
    file: raw/notes/2026-05-09-operator-directive-common-cross-project-cursor-surface-folder-for-view-questions-vision-focus-trace-with-auto-regeneration-from-assistants.md
    title: "Operator turn 8 — common cross-project user surface; gitignored; auto-regenerated; aligned with root-ghostproxy cursor files"
  - id: state-py-tool
    type: file
    file: tools/state.py
    title: "tools/state.py — the regeneration tool"
  - id: cursor-readme
    type: file
    file: .cursor/README.md
    title: ".cursor/README.md — operator-facing meta-doc"
  - id: global-cron
    type: file
    file: .assistant/_global/cron.yaml
    title: "Global CRON jobs (regenerate-cursor-state job lives here)"
  - id: profile-standards
    type: wiki
    file: wiki/spine/standards/per-project-assistant-profile-standards.md
    title: "Per-Project Assistant Profile Standards (sibling /opt meta-layer artifact)"
tags: [standards, cursor-state-folder, runtime-state-cache, view-snapshot, questions-snapshot, vision-mission-tracking, gitignored-per-system, root-ghostproxy-alignment, auto-regenerated, spine-level, "2026-05-09"]
---

# Cursor State Folder Standards (`.cursor/`)

## Summary

The **`.cursor/` folder** is a per-system, gitignored, auto-regenerated runtime state cache that holds pre-rendered project state for fast consumption by `/view`, `/questions`, and any other operator/AI surface that needs to know "where the project is" without re-synthesizing from source each time. Per operator directive 2026-05-09 turn 8 (sacrosanct, verbatim): *"common user surface across project... gitignored folder so that we are aware its a temp folder... per-system, not across multiple computer... avoid git conflict... overlaps with cursor files of root-ghostproxy"*. The folder is **not the source of truth** — it's a CACHE rebuildable from project sources (`wiki/` + `git` + `raw/notes/` + `.assistant/`). It is **the standard** every project should have so that the same operator slash commands (`/view`, `/questions`, etc. — root-propagated) render consistently across the ecosystem. Multi-consumer alignment: content is plain markdown + JSON metadata so any agent (Claude Code · OpenClaw · Multica · operator directly · etc.) can read it.

## Key Insights

1. **`.cursor/` is a CACHE, not a database.** Source of truth is `wiki/` + `git` + `raw/notes/`. Deleting `.cursor/` is fully recoverable — the regenerator rebuilds from sources.

2. **Per-system temp, not cross-machine.** Gitignored. Operator-stated rationale: avoid git conflicts when the same project is opened on multiple computers (each rebuilds its own cache).

3. **Auto-regenerated** — by a CRON job (every 30min default), by an assistant Profile's Action Surface, or manually via `tools/state.py regenerate`. Operator does NOT manually maintain.

4. **Slash commands consume; the folder provides.** `/view` and `/questions` (operator-owned, root-propagated) read `.cursor/<file>.md` for fast render. They MAY fall back to live-synthesis from sources if the cache is stale or missing.

5. **Cross-project convention** — every project SHOULD have `.cursor/` with the same file shape. This is what makes the slash commands render consistently across the ecosystem.

6. **Alignment with root-ghostproxy** — operator stated overlap. The folder name `.cursor/` follows the cursor-files pattern root-ghostproxy propagates. As root-ghostproxy formalizes the convention, /opt's regenerator may need updates.

## Deep Analysis

### Required files in `.cursor/`

| File | Format | Purpose | Regenerated from |
|---|---|---|---|
| `README.md` | markdown | Operator-facing meta-doc (what this folder is) | static; updated when convention changes |
| `_meta.json` | JSON | Regeneration metadata (timestamps · regenerator · file sizes) | every regen |
| `view-snapshot.md` | markdown | Pre-rendered 7-section `/view` snapshot | git log · wiki/log/ · wiki/backlog/ · in-code TODOs |
| `questions-snapshot.md` | markdown | Pre-rendered `/questions` mini-RFC content (open + answered) | wiki/backlog/operator-decision-queue.md · research-gaps.md · wiki/log/ |
| `vision.md` | markdown | Long-term mission + strategic direction | wiki/lessons/02_synthesized/anti-vendor-lock-in · custom-tailored-model-group concept · milestones |
| `focus.md` | markdown | Current session focus / active multi-session arc | raw/notes/ (latest 5) · wiki/log/ (latest 1) · active-arc indicators |
| `trace.md` | markdown | Recent operator-AI interaction trace summary | raw/notes/ (recent 10) · git log (recent 15) |
| `snapshots/` | dir of markdown | Timestamped historical (for `/view --diff` and trend analysis) | daily snapshot of view-snapshot.md retained |

### File-format discipline (sister-project consumable)

- **Markdown** for all content files (operator-readable + AI-readable; no special parser needed)
- **JSON** for `_meta.json` (programmatic regeneration tracking)
- **Sources cited as relative paths** in every snapshot, so the consumer can pivot to live source when needed
- **Timestamp + regenerator** stamped at top of each file (operator can see staleness)

### Regeneration tool

Standardized at `tools/state.py` (Python; venv-respecting per Hard Rule 5). Subcommands:

| Command | What |
|---|---|
| `regenerate` (or `regenerate all`) | Rebuild every file |
| `regenerate view` / `questions` / `vision` / `focus` / `trace` | Rebuild one file |
| `status` | Show last-regenerated + size per file |
| `show <file>` | Cat a cached file (operator inspection) |

The regenerator is **side-effect-free outside `.cursor/`** — reads project sources, writes only to `.cursor/`. No mutations to `wiki/` or other tracked content.

### CRON integration

Project's `.assistant/_global/cron.yaml` ships:

| Job | Schedule | Effect |
|---|---|---|
| `regenerate-cursor-state` | every 30min | Rebuild all `.cursor/` files |
| `daily-vision-refresh` | daily 06:00 | Rebuild just `vision.md` (lower frequency; vision changes less) |

Both ship `enabled: false`; operator opts in.

### Gitignore discipline

`.gitignore` MUST include `.cursor/`. Operator-stated reason: avoid git conflicts across systems. The cache is per-system.

### Multi-consumer alignment

Per operator: *"all Agent mode and AI Assistant mode and platform driven agent can know and agrees on this"*. Implications:

- **Format = markdown** (universal)
- **Source-of-truth pointers in every snapshot** so consumers can pivot to live data when freshness matters
- **`_meta.json` stamps** let consumers detect staleness
- **No proprietary parsing required** — any agent (Claude Code with `Read`, OpenClaw skill, Multica agent, etc.) can consume

### Root-ghostproxy alignment

Operator stated: *"this overlap a bit or connect rather with the cursor files of the root-ghostproxy"*. The folder name `.cursor/` aligns with root's existing cursor-files convention. As root-ghostproxy propagates the canonical convention (file names · schema · regeneration triggers), /opt's regenerator may need updates to match — operator-driven.

### Per-project authoring rules

| Question | Answer |
|---|---|
| Who authors a project's `.cursor/` files? | Auto-regenerated by `tools/state.py`. No manual authoring. |
| Who authors `tools/state.py`? | Project-territory — each project has its own (or inherits via root-ghostproxy propagation when that lands). |
| Does `/opt`'s `tools/state.py` apply to sister projects? | NO — each project's regenerator is project-specific (knows that project's wiki/backlog/sources/etc. layout). |
| Are the file NAMES standardized across projects? | YES — `view-snapshot.md`, `questions-snapshot.md`, `vision.md`, `focus.md`, `trace.md`. Operator slash commands rely on these names. |
| Is the CONTENT standardized? | The SECTIONS in each file are standardized (per the `/view` skill's 7-section spec); the SOURCES vary per project. |

### Anti-patterns this standard rejects

| Anti-pattern | Why bad |
|---|---|
| Committing `.cursor/` to git | Violates gitignore convention; causes cross-machine conflicts |
| Editing `.cursor/` files manually | They're auto-regenerated; manual edits get overwritten on next regen |
| Treating `.cursor/` as source of truth | It's a cache; source is `wiki/` + `git` + `raw/notes/` |
| Adding tool-specific fields (e.g., Claude-Code-only sections) | Folder must remain multi-consumer readable |
| Skipping the source citations in snapshots | Consumers can't pivot to live data without source pointers |
| Auto-regenerating during operator interaction | Avoid mid-conversation churn; CRON-driven background regen is the discipline |

### Lifecycle

```
Source change (wiki/ · git · raw/notes/)
        ↓
CRON fires (every 30m via `regenerate-cursor-state`)
   OR assistant action (per Profile.action_surface)
   OR operator manual: `.venv/bin/python -m tools.state regenerate`
        ↓
tools/state.py reads sources → synthesizes → writes .cursor/<file>.md
        ↓
Updates .cursor/_meta.json (timestamp · regenerator · size)
        ↓
/view, /questions, other consumers read .cursor/ for fast render
   (or fall back to live source if cache too stale)
```

### Forward extensibility

When root-ghostproxy propagates:

- More files (e.g., `progress.md`, `position.md` as separate files if `/view` evolves)
- A canonical regeneration schedule
- A canonical schema for `_meta.json`
- Cross-project lifecycle hooks (e.g., "regenerate on git commit")

The /opt regenerator updates to match. The standard remains stable; the implementation evolves.

## How a new project adopts this standard

1. Create `.cursor/` directory at project root
2. Add `.cursor/` to `.gitignore`
3. Author `.cursor/README.md` documenting the convention locally
4. Author `tools/state.py` (or equivalent) that regenerates the 5+ files from THAT project's sources
5. Add `regenerate-cursor-state` to project's CRON catalog (per-project or via global mechanism)
6. Wire to operator's `/view` / `/questions` slash commands (via root-ghostproxy propagation)
7. Test: delete `.cursor/`, run regenerator, confirm rebuild

## Relationships

- IMPLEMENTS: [[2026-05-09-operator-directive-common-cross-project-cursor-surface-folder-for-view-questions-vision-focus-trace-with-auto-regeneration-from-assistants|Operator directive 2026-05-09 turn 8]]
- COMPLEMENTS: [[per-project-assistant-profile-standards|Per-Project Assistant Profile Standards]] — sibling /opt meta-layer artifact (this one is for state cache; that one is for assistant Profiles)
- DEMONSTRATES: [[infrastructure-over-instructions-for-process-enforcement|Principle 1 — Infrastructure Over Instructions]] — state cache is structural; the slash-command convention is enforced by file naming, not prose advice

## Backlinks

[[Operator directive 2026-05-09 turn 8]]
[[per-project-assistant-profile-standards|Per-Project Assistant Profile Standards]]
[[infrastructure-over-instructions-for-process-enforcement|Principle 1 — Infrastructure Over Instructions]]
