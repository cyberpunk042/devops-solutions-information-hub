---
title: "Operator directive — project-based source mechanism with git-remote fallback"
type: note
domain: log
status: active
note_type: directive
created: 2026-04-15
updated: 2026-04-15
tags: [operator-directive, verbatim, source-mechanism, project-based, git-remote, aliases, portability, handoff]
---

# Operator Directive — Project-Based Source Mechanism with Git-Remote Fallback

## Context

Mid-long-session 2026-04-15 — after ~10 rounds of "continue" during which the session produced 3 new patterns, drift fixes across multiple spine models, a no-caps lint, and 21 cross-sister live-path citations. Operator flags that the current source mechanism (absolute paths with `/home/jfortin/...`) is not portable and should be restructured.

## Verbatim Operator Message

> "The source mechanism should also to work by project with optional additonal aliases. and instead of using the absolute path with the username we can produce the right logic since they logically all share the same parent folder (user profile in this case but that shuld not matter) fonctionning by project allow to add the git remote and when the project is not there we can do queries using gh and curl or curl equivalents and whatnot.. (something robust)
>
> Lets also start thinking of the handoff document, (commit already done), and then we can continue working till the max context but we will keep the handoff up to date as we continue"

## The Directives Distilled

### 1. Project-based source mechanism with optional aliases

Replace absolute paths in `sources:` entries with a project-based identifier. The current form:

```yaml
sources:
  - id: openarms-e016-environment-patching
    type: observation
    file: /home/jfortin/openarms/wiki/domains/architecture/agent-behavior-environment-patching-findings.md
```

Becomes:

```yaml
sources:
  - id: openarms-e016-environment-patching
    type: observation
    project: openarms
    path: wiki/domains/architecture/agent-behavior-environment-patching-findings.md
    aliases: [env-patching-t107, e016-spike-107]   # optional
```

The resolver reads `wiki/config/sister-projects.yaml` to resolve `project: openarms → /home/jfortin/openarms` (or whatever the registry says). The parent-folder assumption is LOGICAL (sisters share a parent) but MUST NOT be hardcoded — the registry is the source of truth.

### 2. Git-remote fallback when local project missing

When the local project path isn't accessible (not cloned, fresh machine, different operator), the source mechanism must fall back to the git remote. Registry extends to include remote info:

```yaml
openarms:
  path: /home/jfortin/openarms
  remote:
    type: github
    owner: Cyberpunk042        # or whichever account
    repo: openarms
    default_branch: main
```

Resolution order:
1. Try local path (fastest, highest-fidelity)
2. Try `gh api repos/{owner}/{repo}/contents/{path}` (if gh CLI authenticated)
3. Try `curl https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{path}` (if public)
4. Return structured failure receipt per the Adapters-Never-Raise pattern

"Robust" — multiple fallbacks, each clearly signalled. No silent failures.

### 3. Handoff document — start now, keep updated as we continue

Session context is being consumed. Handoff document is the artifact that preserves this session's work for the next session. Start it NOW, keep it updated as work proceeds, not wait until context is exhausted.

## Fix Plan

**Phase 1 (immediate):** Log this directive. Start handoff doc with current cumulative state.

**Phase 2 (design):** Design project-resolution module in `tools/common.py` or new `tools/source_resolver.py`. Schema extension in `wiki/config/wiki-schema.yaml` to accept `project: X, path: Y` as source form (alongside existing `url` and `file` forms for external/legacy content).

**Phase 3 (registry extension):** Add `remote:` block to each sister in `sister-projects.yaml`.

**Phase 4 (resolver):** Implement local-path → gh → curl fallback chain. Return structured receipts per Adapters-Never-Raise.

**Phase 5 (migration):** Migrate existing `/home/jfortin/...` source entries to new form. There are ~21 of them across the wiki (all added this session). Each converts cleanly.

**Phase 6 (handoff kept current):** Every 2-3 substantive work units, update the handoff doc with the incremental state.

## Standing Rules Going Forward

1. **NO hardcoded home paths in sources.** Use `project: X, path: Y`. The registry is the single source of truth for project locations.
2. **Local-first, remote-fallback is the norm** for any cross-project read. Not "local only" (breaks portability). Not "remote only" (slow, online-dependent).
3. **Handoff docs are LIVING during long sessions** — write now, update as work lands, don't wait for context pressure.
4. **Git remote info belongs in the registry**, not the source entry — one place to update when ownership/repo moves.
5. **Aliases are optional** — only add them when cross-referencing benefit justifies the extra field.

## Why This Was Logged Verbatim

Per `feedback_verbatim_always.md` — operator directives logged verbatim in raw/notes/ BEFORE acting, proactively. This is directive #3 of today's session (first two: no-caps, no-lowering/consumption-diff, openarms-is-dumb).
