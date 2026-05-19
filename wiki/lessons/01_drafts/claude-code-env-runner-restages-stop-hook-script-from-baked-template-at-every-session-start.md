---
title: "Claude Code env-runner re-stages stop-hook-git-check.sh from baked template at every session start"
type: lesson
domain: ai-agents
layer: 4
status: draft
confidence: high
maturity: seed
created: 2026-05-18
updated: 2026-05-18
sources:
  - id: operator-investigation-2026-05-18
    type: directive
    project: devops-solutions-information-hub
    path: wiki/log/
    note: "Operator reported orphan script reappearing despite prior-session deletion + 4-hour goal sessions degrading; deep forensic investigation requested"
  - id: claude-code-env-runner-binary-decompilation-2026-05-18
    type: empirical
    file: /opt/env-runner/environment-manager
    note: "Go binary on read-only squashfs (/opt/claude-code type squashfs ro). Strings dump shows full template settings.json + stop-hook-git-check.sh content as embedded constants. session-start orchestrator process tree: /bin/sh -c → environment-manager task-run → claude --resume"
  - id: filesystem-forensic-timeline-2026-05-18
    type: empirical
    file: /root/.claude/stop-hook-git-check.sh
    note: "/root/.claude/stop-hook-git-check.sh Birth = 0.467s BEFORE session start; /home/claude/.claude/stop-hook-git-check.sh = May 16 (container build); user override at /root/.claude/settings.json survives across sessions"
tags: [claude-code, hooks, stop-hook, goal, env-runner, environment-manager, template, baked-image, session-start, post-compact, perpetual-mandate, agent-loop, second-brain, self-healing, bootstrap-mirror, multi-hour-cycles]
relates_to:
  - lesson: claude-code-stop-hook-block-cap-default-8-causes-perpetual-goal-glitch
  - lesson: claude-code-settings-local-hot-reload-vs-settings-cache
---

# Claude Code env-runner re-stages stop-hook-git-check.sh from baked template at every session start

## Summary

In Claude Code's cloud/remote execution environment, every session-start invocation runs `/opt/env-runner/environment-manager task-run ...` which **re-stages** `~/.claude/stop-hook-git-check.sh` into the active home directory from a baked-in template. The template lives in two places: (1) embedded as a string constant inside the `environment-manager` Go binary itself, and (2) as a file at `/home/claude/.claude/stop-hook-git-check.sh` on the read-only squashfs container image. Deletion of the orphan script during a session **does not persist** — the next session restages it. The user-modified `~/.claude/settings.json` is NOT overwritten (selective staging), so the script remains DORMANT (not wired) — but the FILE keeps reappearing, which (a) misleads investigation if not understood, (b) creates a permanent latent risk that any future merge logic accidentally combining template + user settings will reactivate the Stop hook and block long-running `/goal` sessions with "There are uncommitted changes in the repository" exit-2 messages.

## Context

When does this lesson apply?

- You're running Claude Code in cloud / remote-execution mode (web app, mobile, GitHub Action, etc.). Locally-installed Claude Code on a personal machine has different staging behavior.
- You investigate why a "deleted" `~/.claude/stop-hook-git-check.sh` reappears, or why a sister `~/.claude/settings.json` template-fragment shows up unexpectedly.
- You're debugging session shortness on a perpetual `/goal` mandate and want to rule out template-Stop-hook activation.
- You're hardening a long-running session and want to make the user override DEFENSIVELY explicit so no future merge logic can reactivate the template hook.

## Insight

> [!success] **The container's `/opt/env-runner/environment-manager` binary is the re-staging agent**
>
> Process tree at session start (visible via `ps -ef --forest`):
>
> ```text
> /bin/sh -c '... environment-manager task-run --session ... --session-mode resume ...'
>   └─ /usr/local/bin/environment-manager (→ /opt/env-runner/environment-manager)
>       └─ claude --output-format=stream-json ... --resume=...
> ```
>
> `environment-manager` is a ~53 MB Go binary on read-only squashfs (`/opt/claude-code` mount: `squashfs (ro,relatime,errors=continue)`). Strings dump confirms it contains:
>
> ```text
>     "$schema": "https://json.schemastore.org/claude-code-settings.json",
>     "hooks": {
>         "Stop": [
>             {
>                 "matcher": "",
>                 "hooks": [
>                     {
>                         "type": "command",
>                         "command": "~/.claude/stop-hook-git-check.sh"
>                     }
>                 ]
>             }
>         ]
>     }
> ```
>
> as an embedded string template. Same content is also present at `/home/claude/.claude/{settings.json, stop-hook-git-check.sh}` (the on-image template files).

> [!info] **Selective staging: script always restaged, user settings.json preserved**
>
> File-birth forensics:
>
> | Path | Birth time | Notes |
> |------|------------|-------|
> | `/root/.claude/stop-hook-git-check.sh` | 2026-05-18 16:46:09.585 | **0.467 s BEFORE current session start** (re-staged) |
> | `/root/.claude/settings.json` | 2026-05-18 14:18:28.353 | Prior session — survived re-staging |
> | `/home/claude/.claude/stop-hook-git-check.sh` | 2026-05-16 01:24 | Container image build (template source) |
>
> So `environment-manager` re-stages the script but does NOT clobber user settings. This means:
> - The orphan script's content keeps reverting on each new session.
> - User overrides in `~/.claude/settings.json` persist (the cap-raise `CLAUDE_CODE_STOP_HOOK_BLOCK_CAP=1000` survives).

> [!warning] **The script is currently DORMANT but the latent risk is permanent**
>
> The template registers the Stop hook via `"hooks": { "Stop": [...] }`. The active `/root/.claude/settings.json` doesn't have a `hooks` key, so the user override "wins by absence" — the hook is unwired. BUT:
>
> - If any future merge logic combines template hooks + user settings, the Stop hook reactivates.
> - If user `settings.json` ever gets clobbered (corrupted, accidentally cleared, replaced via `/config` UI), the template Stop hook becomes active.
> - The script itself still ships with exit code `2` on any uncommitted/untracked/unpushed git state — so a single dirty repo during a `/goal` session creates an infinite block loop until `CLAUDE_CODE_STOP_HOOK_BLOCK_CAP` triggers `blocking_limit`.

## The two-part durable fix

> [!success] **Both parts required for full defense-in-depth**

**Part 1 — make the override DEFENSIVELY explicit in `~/.claude/settings.json`:**

```jsonc
{
    "$schema": "https://json.schemastore.org/claude-code-settings.json",
    "env": {
        "CLAUDE_CODE_STOP_HOOK_BLOCK_CAP": "1000",
        "CLAUDE_CODE_MAX_TURNS": "10000",
        "CLAUDE_CODE_AUTO_COMPACT_WINDOW": "180000"
    },
    "permissions": {
        "allow": ["Skill"],
        "defaultMode": "plan"
    },
    "hooks": {
        "Stop": [],         // ← explicit empty array; defeats template merge
        "SubagentStop": [], // ← belt-and-braces for subagent stops too
        "SessionStart": [{ "hooks": [{ "type": "command",
            "command": "bash $HOME/.claude/env-bootstrap/apply.sh --quiet 2>/dev/null || true",
            "timeout": 15 }] }],     // ← auto-heal drift at every session start
        "PostCompact": [{ "hooks": [{ "type": "command",
            "command": "bash $HOME/.claude/post-compact-reorient.sh",
            "timeout": 5 }] }]        // ← re-inject standing directives after compaction
    }
}
```

The explicit empty arrays mean even if a future merge layer combines template + user settings, the empty arrays win (user-side takes precedence per the standard settings precedence rules: user > project > org > policy).

The `SessionStart` and `PostCompact` hooks are the **self-healing mechanism**: every new session re-runs the idempotent installer (from a bootstrap mirror at `~/.claude/env-bootstrap/` so the harness works even without the info-hub repo cloned), and every compaction event re-injects the standing operator directives via `systemMessage` so multi-hour perpetual `/goal` sessions don't lose trajectory.

**Why three env vars, not just one:** the original investigation surfaced `CLAUDE_CODE_STOP_HOOK_BLOCK_CAP` (default 8 → `blocking_limit` stop-reason cuts long sessions short). Two sibling caps address other stop-reasons surfaced in the Go binary's stop-reason enum:

| Env var | Default | Override | Stop-reason it raises the ceiling for |
|---------|---------|----------|---------------------------------------|
| `CLAUDE_CODE_STOP_HOOK_BLOCK_CAP` | 8 | 1000 | `blocking_limit` (stop-hook returns block too many times) |
| `CLAUDE_CODE_MAX_TURNS` | (varies, often low) | 10000 | `max_turns` (assistant-turn budget exhausted) |
| `CLAUDE_CODE_AUTO_COMPACT_WINDOW` | (varies) | 180000 | `prompt_too_long` (proactively compacts before hitting context-window wall) |

**Out of scope:** `rapid_refill_breaker` stop-reason is service-side rate-limiting; `CLAUDE_CODE_RATE_LIMIT_TIER` is observation-only, NOT client-tunable. No env-var override exists.

**Settings.json applies at next session start.** Confirmed empirically: settings.json is read once at session start and cached. Changes to env-var entries in settings.json mid-session do NOT apply to the live session — the new caps activate on the NEXT session. The empty-array hooks override is similarly session-bound at start.

**Part 2 — neutralize the script in-place each session:**

```bash
#!/bin/bash
# Neutralized: env-runner re-stages this script from a baked template
# at every session start. The DURABLE fix is in ~/.claude/settings.json
# explicit "hooks": { "Stop": [], "SubagentStop": [] } override.
exit 0
```

The script is re-staged each session, so this content only persists for the current session. But it makes the file PROVABLY inert RIGHT NOW: even if some quirk wires it up mid-session, it can only return 0 (= "stop allowed").

## Bulletproof reapply (one command, idempotent) + self-healing mirror

Canonical install lives in this repo at `scripts/claude-code-env/`:

```bash
# From the info-hub repo root:
bash scripts/claude-code-env/apply.sh             # idempotent install
bash scripts/claude-code-env/apply.sh --dry-run   # report-only
bash scripts/claude-code-env/apply.sh --help      # inline docs
```

The script installs five files into `~/.claude/` (`settings.json`,
`CLAUDE.md`, `stop-hook-git-check.sh` neutralized,
`validate-stop-hook-fix.sh`, `post-compact-reorient.sh`), backs up any
pre-existing-but-different live files to
`~/.claude/backups/<file>.<UTC-timestamp>.bak`, **also mirrors itself
into `~/.claude/env-bootstrap/{apply.sh,templates/}`** so the
self-heal mechanism is self-contained (works without the info-hub
repo being checked out), fixes perms, and runs the 8-check validator.
Running it twice is a no-op the second time.

**Self-healing via SessionStart hook:** once installed, the
`SessionStart` hook in `~/.claude/settings.json` calls
`~/.claude/env-bootstrap/apply.sh --quiet` at every session start. Any
drift (clobbered template, missing file, perms regressed) auto-heals
within milliseconds of the session opening. The operator no longer has
to remember to reapply manually.

**Post-compaction re-orient:** the `PostCompact` hook calls
`~/.claude/post-compact-reorient.sh`, which emits a JSON
`systemMessage` re-injecting the standing operator directives
(perpetual `/goal` semantics, sacrosanct verbatim quoting, model-
identifier hygiene, direct-push policy, drift-detection commands).
Critical for multi-hour cycles (2h / 4h / 8h / 16h) where the AI
would otherwise lose behavioral state across compaction summaries.

Use cases for manual reapply (still useful for):
- Fresh container / new cloud session VM (first-time bring-up — the
  `SessionStart` hook isn't wired yet until the first apply.sh runs)
- `~/.claude/settings.json` got clobbered (e.g. via Claude Code's `/config` UI)
- Stop-hook validator reports drift
- New override added to `templates/` — push template change, run apply on each environment
- Onboarding a new ecosystem-project's container

See `scripts/claude-code-env/README.md` for full detail including the
list of harness defaults this overrides (e.g. the cloud harness's
"always create draft PR" hardcode is overridden via `~/.claude/CLAUDE.md`).

## How to detect this at session-start (validator script)

A full 8-check validator is staged at `~/.claude/validate-stop-hook-fix.sh`:

```text
── validate-stop-hook-fix ──
  ✓  settings.json explicit empty Stop arrays — explicit empty arrays defeat any template merge
  ✓  ~/.claude/stop-hook-git-check.sh neutralized — script returns 0 + body has no 'exit 2' code paths
  ✓  CLAUDE_CODE_STOP_HOOK_BLOCK_CAP ≥1000 — configured=1000 (≥1000)
  ✓  CLAUDE_CODE_MAX_TURNS ≥10000 — configured=10000 (≥10000)
  ✓  CLAUDE_CODE_AUTO_COMPACT_WINDOW ≥180000 — configured=180000 (≥180000)
  ✓  SessionStart → env-bootstrap/apply.sh (auto-heal on session start)
  ✓  PostCompact → post-compact-reorient.sh (anti-amnesia)
  ✓  env-bootstrap/{apply.sh,templates/} + post-compact-reorient.sh installed + executable
  ✓ ALL CHECKS PASSED — env-runner stop-hook restage fix + long-session caps + self-healing infra intact
```

The validator's 8 checks:

1. **settings.json has explicit empty `Stop` + `SubagentStop` arrays** — defeats any future template merge.
2. **`~/.claude/stop-hook-git-check.sh` is neutralized** — runs synthetic input through the script (with safe `set +e` exit-code capture, NOT `if echo | script` which clobbers `$?`) AND source-scans for `exit 2` lines.
3. **`CLAUDE_CODE_STOP_HOOK_BLOCK_CAP` ≥1000** — prevents `blocking_limit` stop-reason.
4. **`CLAUDE_CODE_MAX_TURNS` ≥10000** — prevents `max_turns` stop-reason.
5. **`CLAUDE_CODE_AUTO_COMPACT_WINDOW` ≥180000** — reduces `prompt_too_long` stop-reason.
6. **`SessionStart` hook wired to `env-bootstrap/apply.sh`** — auto-heals any drift the moment a new session opens.
7. **`PostCompact` hook wired to `post-compact-reorient.sh`** — re-injects standing operator directives via `systemMessage` after every compaction, so multi-hour cycles don't lose trajectory.
8. **Bootstrap mirror present** — `~/.claude/env-bootstrap/apply.sh` + `~/.claude/env-bootstrap/templates/` + `~/.claude/post-compact-reorient.sh` all installed + executable. Means the self-heal mechanism works even if the info-hub repo isn't cloned.

Three modes:
- `~/.claude/validate-stop-hook-fix.sh` — human report (default)
- `~/.claude/validate-stop-hook-fix.sh --json` — JSON report (CI-friendly)
- `~/.claude/validate-stop-hook-fix.sh --quiet` — exit-code only

Exit codes: `0` all pass / `1` at least one check failed / `2` jq missing or settings.json unreadable.

The `SessionStart` hook (check 6) is wired by `apply.sh` automatically; the validator confirms it stays wired across `/config` UI edits or template-merge accidents.

### Quick one-liner audit (if validator unavailable)

```bash
jq -e '.hooks.Stop == [] and .hooks.SubagentStop == []
       and (.env.CLAUDE_CODE_STOP_HOOK_BLOCK_CAP | tonumber) >= 1000
       and (.env.CLAUDE_CODE_MAX_TURNS | tonumber) >= 10000
       and (.env.CLAUDE_CODE_AUTO_COMPACT_WINDOW | tonumber) >= 180000
       and (.hooks.SessionStart[0].hooks[0].command // "" | contains("env-bootstrap/apply.sh"))
       and (.hooks.PostCompact[0].hooks[0].command // "" | contains("post-compact-reorient.sh"))' \
   ~/.claude/settings.json >/dev/null \
   && [ -x ~/.claude/env-bootstrap/apply.sh ] \
   && [ -d ~/.claude/env-bootstrap/templates ] \
   && [ -x ~/.claude/post-compact-reorient.sh ] \
   && echo "✓ all caps + hooks + self-heal infra intact" \
   || echo "✗ drift detected — run: bash ~/.claude/env-bootstrap/apply.sh"
```

### Critical bash gotcha caught while building the validator

The naive pattern fails silently:

```bash
# ❌ WRONG — $? inside `then` is the if-condition's 0, NOT the pipeline's exit code
if echo '{}' | "${ORPHAN}" >/dev/null 2>&1; then
  actual_exit=$?   # always 0 here — bug
fi

# ✅ RIGHT — capture exit code OUTSIDE the if-condition
set +e
echo '{}' | "${ORPHAN}" >/dev/null 2>&1
actual_exit=$?
set -e
```

This was a real false-pass in the validator's first revision before being caught by a negative test.

## Why this lesson exists

The operator perceived "I used to do 4-hour goal sessions, now they're shorter." Initial hypothesis was the `CLAUDE_CODE_STOP_HOOK_BLOCK_CAP` default-8 (covered in sibling lesson `claude-code-stop-hook-block-cap-default-8-causes-perpetual-goal-glitch`) had reverted. Investigation showed cap was still 1000 (good). Deeper investigation found the env-runner re-staging mechanism: a permanent template-vs-user-override asymmetry that needs DEFENSIVE EXPLICIT user-override settings to be safe long-term.

## Applicability

- **Cloud/remote Claude Code sessions** (web app, mobile, GitHub Action). Investigation conducted on `cloud_default` remote environment type (`CLAUDE_CODE_REMOTE_ENVIRONMENT_TYPE`).
- Local Claude Code installs may not have `/opt/env-runner` and may not re-stage the script — verify your env.
- Lesson applies to any user-customized `~/.claude/settings.json` on a managed-template environment, not just `/goal`-related work.

## Evidence

- `/opt/env-runner/environment-manager` binary string-dump (`strings | grep stop-hook-git-check`): 1 match, full template embedded.
- `/home/claude/.claude/{settings.json,stop-hook-git-check.sh}`: on-image files matching template.
- File-birth fingerprint: `/root/.claude/stop-hook-git-check.sh` Birth = 0.467s pre-session-start.
- Process tree: `environment-manager task-run --session-mode resume` is the upstream of every `claude` invocation in this environment.
- Squashfs read-only mount: `findmnt /opt/claude-code` → `squashfs (ro)`.

## Relationships

- **Related lesson**: `claude-code-stop-hook-block-cap-default-8-causes-perpetual-goal-glitch` — sibling root-cause for short-session perception. Both apply to perpetual `/goal` work.
- **Related lesson**: `claude-code-settings-local-hot-reload-vs-settings-cache` — explains the precedence rules that the defensive override relies on.
- **Related lesson**: `claude-code-hook-additionalcontext-is-event-specific-not-all-events-accept-it` — sibling lesson on hook configuration gotchas.

## Alternatives considered

| Alternative | Why rejected |
|-------------|--------------|
| Delete `~/.claude/stop-hook-git-check.sh` permanently | Cannot — env-runner re-stages every session from the read-only squashfs template. |
| Edit `/home/claude/.claude/stop-hook-git-check.sh` to neutralize the template at source | `/home/claude` is writable as root, but the change has unclear persistence (likely tmpfs overlay; doesn't propagate back to the squashfs image). And edits there don't affect the embedded string in the env-runner binary. |
| Modify the env-runner binary to not stage the script | The binary is on `ro,relatime` squashfs mount — physically not writable without remount or image rebuild, which is outside operator control on a managed-cloud session. |
| Just leave it (script is dormant) | Latent risk: any future merge-logic change in Claude Code could reactivate the hook, breaking perpetual `/goal` sessions silently. Defensive empty-array override is cheap insurance. |

## Dependencies

- Requires `~/.claude/settings.json` writable (it is, in normal cloud sessions).
- Requires Claude Code respecting standard user > project > org > policy settings precedence (per `code.claude.com/docs/en/settings`).

## Open questions

- What is the merge semantics if BOTH template `/home/claude/.claude/settings.json` AND user `~/.claude/settings.json` are read by the same `claude` process? Current evidence suggests only one is read (per `$HOME`), but not yet confirmed. If a merge IS performed, the explicit empty arrays in user settings should still win per standard precedence rules — but verify empirically before relying on this in production.
- Is there a `CLAUDE_CODE_*` env var that disables the env-runner staging step entirely? Strings dump shows ~150 `CLAUDE_CODE_*` env vars; `--bare` flag exists for `claude` invocation but doesn't disable env-runner's pre-claude staging.
