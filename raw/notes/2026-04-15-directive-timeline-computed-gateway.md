---
title: "Operator directive — computed timeline as a gateway command"
type: note
domain: log
status: active
note_type: directive
created: 2026-04-15
updated: 2026-04-15
tags: [operator-directive, verbatim, timeline, gateway, computed-view, cross-project, scope]
---

# Operator Directive — Computed Timeline as a Gateway Command

## Verbatim Operator Messages

> "we should be able to see a timeline. can we compute such a thing ? I would like to see the evolutions of each repo / projects and see them in time and be able to look at the lessons for example and aggregate them all in a timeline and such.
>
> Do you understand the purpose? lets dig it with me. this was just a simple example I want something much more advanced and yet smart and simple.
>
> I would also be able to see the sessions and the logs and the handoffs and such. Specs creations, plan, Epic progress, task deliveries. etc...."

> "not a manual timeline silly... a computed one, one demand, with the given armuments, like the rest via the gateway... you can check only your project or you can check all sister projects. do not minimize or corrupt what I said. But yeah you have pieces of it, just focus and remember what I said."

> "Yesh but just to confirm, self when inside another project is the self no the second-brain, the second-brain then become the backup source of config and for general cases and offer to consume and adapt via the proper channel but from another project beside the obvious multi second-brain integration, for the timeline it counds as a sistem project, although we might also offer them to look at only themselves plus the second-brain or vice versa, we might want to look only at ourself, the second-brain and only one sistem project, e.g. openarms."

> "I confirm. You can get started"

## The Design (confirmed with operator)

### Core concept

A **gateway command** that COMPUTES a timeline on demand from existing data across projects. No manual digest, no stored artifact. Computed each call from source of truth.

### Scope model (position-aware, set-valued)

- `self` = the invoking project (resolved via `--wiki-root`; depends on WHERE the command runs)
- `brain` = the declared second-brain (resolved via `--brain`; from a sister this is `research-wiki`, from the wiki itself `self == brain`)
- `all` = every project in the brain's registry (brain + all sisters)
- Explicit names: `openarms`, `openfleet`, `aicp`, etc.
- **Set-valued** via comma: `--scope self,brain,openarms` composes freely; duplicates collapse.

### Default scope by caller

- From the brain: `self` (just the wiki's own activity)
- From a sister: `self,brain` (sister + its backup config source)

### What sources the timeline reads per project

Uniform across scopes, reusing existing readers:

| Event type | Source |
|---|---|
| commit | `git log` per project root |
| lesson / pattern / decision / synthesis / concept | `wiki/**/*.md` frontmatter `created` / `updated` |
| epic / task | `wiki/backlog/**/*.md` frontmatter + stage transitions |
| directive | `raw/notes/YYYY-MM-DD-*.md` |
| session / handoff | `docs/SESSION-*.md` (wiki) or `log/YYYY-MM-DD-*.md` (sisters) |

Cross-project paths resolved via the existing `sister-projects.yaml` registry. The brain's registry is the source of truth for "what projects exist"; sisters consume it via the proper channel (MCP call back to brain's gateway, or source_resolver fetch).

### CLI shape

```
python3 -m tools.gateway timeline
    [--scope LIST]                 # default: self (from brain) or self,brain (from sister)
    [--since DATE|DURATION]        # default: 7d
    [--until DATE|DURATION]
    [--type LIST]                  # lesson,pattern,decision,synthesis,epic,task,session,directive,commit
    [--group-by date|project|type] # default: date
    [--format markdown|json]
    [--full-content]               # no-caps: include full event body
    [--wiki-root PATH] [--brain PATH]
```

MCP exposure: `wiki_gateway_timeline(scope, since, until, types, group_by, format, full_content)`.

### Delta-event enhancement (Phase 1)

For fields that show progress, emit delta events in addition to snapshot events:
- Epic `readiness: 45 → 70` → its own timeline event
- Task `stages_completed: document,design → document,design,scaffold` → its own timeline event
- Page `maturity: seed → growing` → its own timeline event

Snapshot events (plain `updated`) for anything else.

## Standing Rules Going Forward

1. **Timeline is computed, not stored.** No `wiki/timeline/` artifacts. Each invocation re-reads source of truth.
2. **Scope semantics are position-aware.** `self` means the invoker; `brain` means the declared second-brain.
3. **Registry stays at the brain.** Sisters consume the brain's `sister-projects.yaml` via MCP or source_resolver; they don't duplicate it locally.
4. **Default time window 7 days.** Operator's most common question is "what happened this week."
5. **No-caps applied.** `--full-content` flag surfaces the entire event body; default is title+subject+signal preview.

## Why This Was Logged

Per `feedback_verbatim_always.md` — operator directives logged verbatim in `raw/notes/` BEFORE acting. This file captures the design conversation that led to "confirmed, build it."
