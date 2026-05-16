---
title: "2026-05-16 — Operator GO: proceed with all gates A/B/C/D for root-ghostproxy-rollout first real install"
type: note
note_type: directive
domain: log
status: active
confidence: authoritative
created: 2026-05-16
updated: 2026-05-16
sources:
  - id: operator-directive-2026-05-16-proceed-with-everything-go
    type: directive
tags: [operator-directive, root-ghostproxy, install-go, gate-a, gate-b, gate-c, gate-d, opus-1m, gateway-node, v5-systemprompt, "2026-05-16"]
---

# Operator GO — proceed with everything, all 4 gates for first real install

## Verbatim operator words (sacrosanct, 2026-05-16)

> "Proceed with everything, GO"

## Context

In response to my status update enumerating 4 gates (A v5 systemPromptOverride activation / B Opus 1M context via Path G / C gateway nvm-Node concern / D INSTALL: GO operator signal), operator authorized **all four** with "everything, GO".

## Execution order (dependency-driven)

1. **C — Gateway infrastructure first** (`openclaw gateway install --force`) — affects all agents; do BEFORE agent re-registration so the gateway is stable.
2. **B — Opus 1M context config** — patch `~/.openclaw/openclaw.json` to add `models.providers.anthropic.models[]` entry with `headers: {"anthropic-beta": "..."}` + `contextWindow: 1000000`; switch agent's primary model from `anthropic/claude-opus-4-7` → `anthropic/claude-opus-4-7[1m]` in `.assistant/root-ghostproxy-rollout.openclaw.json5`.
3. **A — v5 systemPromptOverride activation** — `openclaw agents delete root-ghostproxy-rollout` (removes the stale 13:20 ET v3-registration; isolated workspace + target project both untouched per cross_project_target safety) then `bin/assistant install root-ghostproxy-rollout` (registers fresh with v5 worker prompt, registers cron jobs, propagates auth, materializes v5 workspace files).
4. **D — `INSTALL: GO`** marker in `.assistant/_state/root-ghostproxy-rollout-operator-directives.md` (formal worker-readable authorization — written BEFORE install command so the worker reads it on first fire).
5. **First-fire bootstrap** — per cron yaml `bootstrap-observation: first-fire` is one-shot; trigger after install completes.
6. **Verification** — re-run `bin/assistant status`, dry-run cron, validate systemPromptOverride contains v5 worker prompt + multi-discipline frame, validate model alias resolves to opus-1m.

## Acceptance criteria

- `bin/assistant status root-ghostproxy-rollout` shows: 6/6 cron jobs registered, agent v5-registered, gateway active
- `openclaw models list` shows opus-1m with Ctx 1M (NOT 195k) — if Anthropic beta flag is accepted
- Bootstrap first-fire produces planning artifact in `.assistant/_state/root-ghostproxy-rollout-inbox.md` (the Pre-Launch Dry-Run #1 reasoning shows it would pick T014)
- No deletions to `/home/jfortin/root-ghostproxy/` (R20 sacrosanct hold)
- No deletions to wiki/ or .assistant/ tracked files (R20 sacrosanct hold)

## Risks acknowledged

- **Anthropic beta-flag string** — current value per Anthropic public docs is `context-1m-2025-08-07` (I'll verify in the second-brain corpus before applying; if not present, surface as [NEEDS OPERATOR REVIEW] and best-faith with that value)
- **Node ≥22/24 requirement for `gateway install --force`** — if not on PATH as system Node (vs nvm-managed), defer Gate C with documented workaround rather than installing Node (out of scope)
- **`openclaw agents delete` blast radius** — per tools/assistant.py SAFETY note, deletes the agent's isolated workspace (which is OpenClaw's scratch space, NOT the target project). cross_project_target's target is `/home/jfortin/root-ghostproxy/` and is untouched by `agents delete`.
- **Sessions history loss** — `~/.openclaw/agents/root-ghostproxy-rollout/sessions/` (today's v3 fire sessions) will be deleted. Those v3 sessions surfaced Q97; the artifact (Q97 in queue) survives in `wiki/backlog/operator-decision-queue.md`. Acceptable loss.
- **1M context cost ~2×** — operator-acknowledged via "everything GO".

## Status

Logged. Executing in dependency order.
