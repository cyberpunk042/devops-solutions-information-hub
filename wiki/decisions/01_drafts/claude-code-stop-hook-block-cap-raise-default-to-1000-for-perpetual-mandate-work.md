---
title: "Decision: raise CLAUDE_CODE_STOP_HOOK_BLOCK_CAP to 1000 (default 8) for any operator using perpetual `/goal` mandates"
type: decision
domain: ai-agents
layer: 6
status: draft
confidence: high
maturity: seed
derived_from:
  - "wiki/lessons/01_drafts/claude-code-stop-hook-block-cap-default-8-causes-perpetual-goal-glitch.md"
reversibility: easy
created: 2026-05-18
updated: 2026-05-18
sources:
  - id: operator-decision-2026-05-18
    type: directive
    project: devops-solutions-information-hub
    path: wiki/log/
    note: "Operator selected 'Raise the cap to 1000 (Recommended)' option in live AskUserQuestion during the perpetual /goal investigation session"
tags: [claude-code, stop-hook, goal, settings, environment, decision, operator-directive]
---

# Decision: raise `CLAUDE_CODE_STOP_HOOK_BLOCK_CAP` to 1000 (default 8) for any operator using perpetual `/goal` mandates

## Summary

The Claude Code harness's Stop-hook consecutive-block cap defaults to **8** — perpetual `/goal` mandates ("Continue Endlessly") hit the cap after ~8 auto-rounds and the conversation appears to stop. **Recommended: set `CLAUDE_CODE_STOP_HOOK_BLOCK_CAP="1000"` in `~/.claude/settings.json` under the `env` block.** This keeps a runaway-hook safety net (truly stuck hooks still kill at 1000) while making the cap practically unlimited for perpetual operator mandates. Alternative `"0"` fully disables the cap; alternative `"8"` (status quo) is fine only if you never use perpetual `/goal`.

## Decision

| Option | When to choose | Trade-off |
|--------|----------------|-----------|
| `"1000"` ⭐ **default for perpetual-mandate operators** | You use `/goal` with unsatisfiable conditions (Continue Endlessly, "keep working until X", etc.) but want a safety floor against truly broken hooks. | Loses ~3 orders of magnitude of safety margin vs default 8, but in exchange the perceived "glitch" disappears entirely. |
| `"0"` | You're confident no other hook will runaway-loop AND you want truly unlimited perpetual behavior. | Removes the safety net entirely. If a different Stop hook (not `/goal`) ever breaks and always-blocks, you'll have to kill the session to escape. |
| `"8"` (default) | You never use perpetual mandates. | Status quo; perpetual `/goal` users hit the glitch every ~8 rounds. |
| Other (e.g., `"50"`, `"100"`) | You want a tighter safety margin than 1000 but more than 8. | Reasonable; pick whatever gives you confidence. The lint-mechanization mandate in our operator-named workflow uses `≥50%` thresholds — `100` would echo that. |

**The operator's chosen value: `"1000"`** (per 2026-05-18 live AskUserQuestion).

## Rationale

1. **The cap's purpose** is to prevent infinite agent-side loops caused by misconfigured Stop hooks. That purpose is still served by `"1000"` — a genuinely-stuck hook still gets killed, just after 1000 attempts instead of 8.
2. **Perpetual `/goal` is operator-authorized behavior**, not a bug to be capped. The harness can't tell intent; `"1000"` lets the operator state intent via configuration.
3. **`"0"` is too aggressive** as a default recommendation — it removes ALL protection. If a third-party plugin ever ships a buggy Stop hook, `"0"` means infinite loop until manual session kill.
4. **`"1000"` matches operator-named workflow norms** — far above any realistic single-turn work, but bounded.

## How to apply

Add to `~/.claude/settings.json` under the `env` block (preserving existing keys):

```json
{
    "$schema": "https://json.schemastore.org/claude-code-settings.json",
    "env": {
        "CLAUDE_CODE_STOP_HOOK_BLOCK_CAP": "1000"
    },
    "permissions": { ... }
}
```

**Activation**: takes effect at next session start (the env block is read at session boot, not hot-reloaded — per `wiki/lessons/01_drafts/claude-code-settings-local-hot-reload-vs-settings-cache.md`). To activate the current session, restart Claude Code OR (CLI) export the env var in the launching shell before invoking `claude`.

## Reversibility

**fully-reversible** — remove the env key from settings.json and restart. No on-disk state, no migrations, no upstream coupling. The cap is a runtime guard read from process.env at every Stop-hook block; removing it reverts to the default 8.

## What this unlocks

1. **Perpetual `/goal` mandates work as intended.** Cap reaches 1000 before override; long-running agent loops complete naturally.
2. **Long unattended automation runs.** Background-style agent loops (research, multi-stage builds, doc generation, refactor pipelines) finish without operator re-engagement to reset the counter.
3. **PR babysitting + main-branch progression in parallel.** Combined with `subscribe_pr_activity`, an agent can watch CI events AND keep shipping rounds without artificial turn-end ceilings.
4. **No more re-issuing `/goal`.** The hook stays armed across the now-effectively-unbounded loop. Operator-perceived flakiness disappears.

## What this does NOT change

- **`max_turns`** is a SEPARATE kill switch. The cap-raise doesn't affect `max_turns`. If you want unlimited turns too, that's a different setting.
- **Manual kill (Ctrl-C / session close)** still works at all times. Raising the cap doesn't trap the operator.
- **Tool denial / permission prompts** still gate on the same per-tool rules. The cap only governs Stop-hook block iteration count.
- **`/goal clear`** still clears the hook on demand. The cap-raise doesn't make `/goal` "sticky" beyond operator intent.

## Anti-patterns

- ❌ Setting `"0"` as the default recommendation. It removes ALL safety; only choose it if you've audited your hooks and accept the trade-off.
- ❌ Editing settings.json mid-session and expecting immediate effect. The env block is cold-read at session start.
- ❌ Combining cap-raise with a known-broken hook. If a hook always-blocks erroneously, raise the cap LAST, after fixing the hook.

## Alternatives

Three values were live-considered (operator chose option 2 via AskUserQuestion):

| Option | Value | Trade-off |
|---|---|---|
| 1. Disable cap | `"0"` | Fully unlimited; loses the runaway-hook safety entirely. Choose if you've audited all hooks and accept the risk. |
| 2. Raise cap (chosen) | `"1000"` ⭐ | Practically unlimited for perpetual `/goal`; keeps a safety floor for truly stuck hooks. |
| 3. Keep default | `"8"` | Status quo; perpetual `/goal` operators hit the glitch every 8 rounds. |

Adjacent alternatives (not chosen but reasonable):
- `"50"` / `"100"`: tighter safety margin than 1000 but more permissive than 8. Reasonable if the operator wants the cap to be a meaningful kill-switch within a single auto-loop.
- `max_turns`: a SEPARATE kill switch. Not an alternative to this cap; can be configured independently for a different protection layer.

## Dependencies

- **Requires**: Claude Code harness that honors `CLAUDE_CODE_STOP_HOOK_BLOCK_CAP` env var. Verified in `/opt/claude-code/bin/claude` (May 2026 build). Earlier builds may not honor it.
- **Requires**: settings.json `env` block reading at session start (cold-load semantics — see sibling lesson on settings caching).
- **Does NOT depend on**: any specific `/goal` text, any specific Stop hook implementation, any plugin or MCP server. Pure runtime config.
- **Coordinates with**: `max_turns` (separate per-session turn ceiling), `/goal clear` (manual hook cleanup), `subscribe_pr_activity` (webhook-driven session wakes — independent of cap).

## Relationships


## Cross-references

- `wiki/lessons/01_drafts/claude-code-stop-hook-block-cap-default-8-causes-perpetual-goal-glitch.md` — the underlying lesson (full mechanism + decompiled control flow).
- `wiki/lessons/01_drafts/claude-code-settings-local-hot-reload-vs-settings-cache.md` — explains why the env block requires session restart to activate.
- `wiki/lessons/01_drafts/claude-code-hook-additionalcontext-is-event-specific-not-all-events-accept-it.md` — sibling Stop-hook return-value semantics.
- `wiki/decisions/02_validated/tools/hooks-design-decisions.md` — broader hooks design decisions.

## Status: draft → ready to validate

To promote to validated:
1. Apply on a second machine; verify the round-count-before-stop changes from 8 → 1000+ on a perpetual `/goal`.
2. Verify the `tengu_stop_hook_block_count {hit_cap: false}` telemetry path stays clean up to the new ceiling.
3. Confirm no interaction with `max_turns` (set both high, verify they remain independent).
