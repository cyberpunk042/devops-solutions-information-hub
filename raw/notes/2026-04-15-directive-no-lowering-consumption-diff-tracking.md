---
title: "Operator directive — no lowering to sister level, consumption-diff tracking by default"
type: note
domain: log
status: active
note_type: directive
created: 2026-04-15
updated: 2026-04-15
tags: [operator-directive, verbatim, higher-ground, consumption-tracking, flexible-tools, differential]
---

# Operator Directive — No Lowering to Sister Level, Consumption-Diff Tracking By Default

## Context

Mid-session 2026-04-15 — after demonstrating an end-to-end cross-project contribute flow by pulling a specific OpenArms lesson (`lesson-investigate-before-designing.md`) via the fixed MCP `wiki_sister_project` tool and ingesting it verbatim into `wiki/lessons/00_inbox/` via `wiki_gateway_contribute`. Operator corrected the approach mid-task.

## Verbatim Operator Message

> "Do not lower yourself to the a sister projects either, we only use to grow and evolve. we find a way to track what lessons were not consumed yet so that we can only get the differencial next time by default if we dont add an arg to see it all anyway... flexible tools"

## The Two Directives Distilled

### 1. Higher ground — not verbatim mirroring

The wiki does NOT copy sister-project lessons into its own tree. Sister content is INPUT to evolution, not output to store. Sister lessons feed convergent-evidence synthesis where multiple sources (ours + sisters + external research) CONVERGE on a higher-ground truth. The verbatim-copy pattern is lowering — it makes this wiki a derivative of the sisters. The wiki exists to aggregate, cross-validate, and synthesize ABOVE the sister projects.

Aligns with the existing framing: *"openarms was just discovering things and making assumption, we have a much higher ground"* — from the 2026-04-14 session. Operator's 2026-04-12 goldilocks-higher-ground directive was the same principle.

### 2. Consumption-diff tracking by default — flexible tools

We need tooling that tracks which sister-project lessons have already been CONSUMED (absorbed into our synthesized knowledge) vs which remain UNCONSUMED. The default behavior when listing a sister's lessons should be the DIFFERENTIAL — only show what we have not yet incorporated. An argument toggles the full view. The design pattern: **new-by-default, all-opt-in, flexible-by-toggle**.

Aligns with the wiki's Flexibility Principle ("the wiki is a menu, not a law") applied to its own consumption of external material — we pull only what we haven't already absorbed, not the whole pile every time.

## Standing Rules Going Forward

1. **Never ingest a sister lesson verbatim into a permanent layer.** Raw-copy into 00_inbox is the wrong primitive. If we want to reference a sister lesson, do it via `sources:` frontmatter pointing at the sister path — not by duplicating the body.

2. **Synthesis ≥ source count.** Any wiki page that incorporates a sister lesson must be a SYNTHESIS that combines that lesson with at least one other data point (other sister, external research, our own observation). Single-source pages that just restate a sister lesson are not synthesis — they are mirroring.

3. **Consumption must be tracked structurally.** Whether via derived_from, sources, or a dedicated consumption registry — the wiki must know, for each sister lesson, whether it has been absorbed. Manual tracking is not tracking; unconsumed-by-default differential listing is the bar.

4. **Default to differential, flag to see all.** The sister-project tool's list-family actions (learnings, epics, tasks) should default to showing only unconsumed items, with an explicit flag to show everything. Infrastructure over instructions: the tool enforces the higher-ground discipline structurally.

## Fix Applied This Session

- Deleted the verbatim-copy at `wiki/lessons/00_inbox/investigate-before-designing-—-dont-reason-from-assumptions-.md` (wrong primitive per Rule 1 above)
- Adding `--new` / `--all` flag surface to `tools/sister_project.py` and mirroring in `tools/mcp_server.py`
- Detection mechanism: scan all wiki pages' `sources:`, `derived_from:`, `contribution_source:`, and body-text references to sister-project paths; a sister lesson is "consumed" if any wiki page references it
- Default behavior on list actions: only unconsumed items returned; pass `--all` to see everything

## Why This Was Logged Verbatim

Per memory rule `feedback_verbatim_always.md` and `feedback_no_caps_no_compact_read_full.md`: operator directives are logged verbatim in `raw/notes/` BEFORE acting, proactively. This file is the real-time record.
