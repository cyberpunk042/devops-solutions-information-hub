---
title: "Claude Code settings.local.json hot-reloads; settings.json caches at session start"
type: lesson
domain: ai-agents
status: draft
confidence: high
maturity: seed
created: 2026-05-06
updated: 2026-05-06
sources:
  - id: operator-debugging-session-2026-05-06
    type: directive
    file: raw/notes/2026-05-06-claude-code-hook-stamp-bug-cached-config-vs-settings-local-hot-reload.md
  - id: claude-code-hooks-reference
    type: external
    url: https://code.claude.com/docs/en/hooks
tags: [claude-code, hooks, settings, configuration, hot-reload, caching, lesson, draft]
---

# Claude Code settings.local.json hot-reloads; settings.json caches at session start

## Summary

Claude Code reads hook configuration from multiple settings files with asymmetric reload behavior: `.claude/settings.json` is loaded once at session start and cached for the session's lifetime (edits during a live session do not update the cached config; even `touch`-ing the file does not trigger reload), while `.claude/settings.local.json` is hot-reloaded per prompt (edits take effect on next prompt). This caching asymmetry is undocumented in the official Claude Code hook docs but verifiable via the session log and empirical testing. When iterating hook wiring during an active development session, knowing WHICH file hot-reloads is essential — otherwise edits to the wrong file have no effect for the live session and developers spend hours debugging "why isn't my fix taking effect."

## Context

Claude Code reads hook configuration from multiple settings files. When iterating hook wiring during an active development session, knowing WHICH file hot-reloads is essential — otherwise edits to the wrong file have no effect for the live session, and developers spend hours debugging "why isn't my fix taking effect."

Empirically discovered 2026-05-06 during a multi-hour debugging session of an end-of-cycle stamp hook regression on a `/root` project session.

## Insight

> [!success] **Caching asymmetry: settings.json caches; settings.local.json hot-reloads**
>
> `.claude/settings.json` is **loaded once at session start** and cached for the session's lifetime. Editing it during a live session does not update the cached config. Even `touch`-ing the file (mtime change) does not trigger reload.
>
> `.claude/settings.local.json` is **hot-reloaded per prompt** (or close to it). Edits during a live session take effect on next prompt. This is the escape hatch for fixing hook wiring without requiring `/clear` or session restart.

> [!info] **Undocumented but empirically verifiable**
>
> This caching asymmetry is **undocumented** in the official Claude Code hook docs but verifiable via the session log and empirical testing.

## Evidence

Debugging session 2026-05-06 produced the following empirical sequence:

1. `/root` session loaded with `settings.json` containing a hook MISWIRED to UserPromptSubmit (instead of intended Stop)
2. Multiple corrective edits to `settings.json` made over ~50 iterations — none took effect for the live session
3. File-history forensics confirmed the cached version was the miswired one
4. Adding the correct Stop hook wiring to `settings.local.json` → next prompt fired the Stop hook correctly → bug fixed without session restart

Session log (`.claude/projects/<dir>/<session-id>.jsonl`) recorded the actual hook events firing — confirmed UserPromptSubmit until settings.local.json fix, then Stop after.

## Applicability

**When this lesson applies:**

| Scenario | Apply? |
|---|---|
| Iterating hook wiring during an active Claude Code development session | **YES** — edit `settings.local.json` for live-session iteration |
| Persisting hook configuration across all sessions (machine-wide / project-wide canonical) | **YES** — finalize in `settings.json` after iteration, then `/clear` or restart for it to take effect |
| Mid-session debugging of "why isn't my hook firing" | **YES** — first check whether you're editing the cached file (`settings.json`) or the hot-reload file (`settings.local.json`) |
| One-off scripts or non-Claude-Code tooling | NO — this is Claude-Code-specific behavior |

## Implication / How to apply

| Scenario | File to edit |
|---|---|
| **Iterating hook wiring during active development** | `settings.local.json` (hot-reloaded) |
| **Stable hook config baked into project** | `settings.json` (committed to git) |
| **Per-machine overrides that shouldn't be shared** | `settings.local.json` (typically gitignored) |
| **Need a fix to take effect WITHOUT session restart** | `settings.local.json` |
| **Need to invalidate a cached miswire** | `settings.local.json` (overrides settings.json's cached version) |

### Development pattern

When authoring or debugging hooks in a live session:

1. Wire the hook in `settings.local.json` first
2. Iterate until working (each prompt picks up changes)
3. Once stable, move the wiring to `settings.json` (commit-worthy)
4. Verify next prompt still fires correctly (cache will pick up settings.json on next session start)

Avoid editing `settings.json` mid-session for hot-fixes — the edit will appear correct on disk but the live session ignores it until restart.

## Diagnostic: when uncertain whether a hook is firing

Read the session log directly to see what Claude Code actually recorded:

```python
import json
session_log = '/root/.claude/projects/<dir>/<session-id>.jsonl'
with open(session_log, 'rb') as f:
    f.seek(-50000, 2)  # last 50KB
    tail = f.read().decode('utf-8', errors='replace')
for line in tail.split('\n'):
    try:
        d = json.loads(line)
        if d.get('type') == 'attachment' and d.get('attachment', {}).get('type') == 'hook_system_message':
            ev = d['attachment'].get('hookEvent')
            content = d['attachment'].get('content', '')[:80]
            print(f'{ev}: {content}')
    except Exception:
        pass
```

This shows the literal `hookEvent` Claude Code assigned to each hook output and the content. If `hookEvent` doesn't match what your `settings.json` says — cached miswire confirmed.

## Relationships

- BUILDS ON Claude Code Hooks Reference (https://code.claude.com/docs/en/hooks)
- COMPLEMENTS [[claude-code-hook-additionalcontext-is-event-specific-not-all-events-accept-it|Lesson — Hook output channel is event-specific (`additionalContext` only valid for 6 events)]] — sister lesson from the same 2026-05-06 arc covering the output-channel-validity half (this one covers the caching half)
- COMPLEMENTS [[user-level-settings-json-hook-path-resolution-relative-vs-home-prefixed|Lesson — User-level settings.json hook paths must be `$HOME`-prefixed or absolute]] — sister lesson covering the path-resolution half of the same arc family
- ENABLES rapid hook iteration without session restart
- USED BY any project authoring custom Claude Code hooks during active development
- CONSTRAINS the "edit settings.json during dev" workflow — must use settings.local.json instead

## Cross-references

- Raw note (verbatim debugging arc): `raw/notes/2026-05-06-claude-code-hook-stamp-bug-cached-config-vs-settings-local-hot-reload.md`
- Companion pattern: `wiki/patterns/01_drafts/iterate-hook-wiring-in-settings-local-during-development.md` (to be authored)
- Related architecture: Claude Code's three-layer settings precedence (project, local, user)
