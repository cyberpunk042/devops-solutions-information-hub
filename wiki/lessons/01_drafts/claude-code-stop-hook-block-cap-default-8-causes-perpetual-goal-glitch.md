---
title: "Claude Code Stop hook block cap defaults to 8 — perpetual `/goal` appears to stop after ~8 rounds"
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
    note: "Operator reported '/goal keeps being removed and conversation stops' glitch during perpetual mandate work; investigation requested"
  - id: claude-code-binary-decompilation-2026-05-18
    type: empirical
    file: /opt/claude-code/bin/claude
    note: "Strings dump + control-flow window around blocking_limit / CLAUDE_CODE_STOP_HOOK_BLOCK_CAP"
  - id: claude-code-hooks-reference
    type: external
    url: https://code.claude.com/docs/en/hooks
tags: [claude-code, hooks, stop-hook, goal, settings, environment, perpetual-mandate, safety-cap, agent-loop]
---

# Claude Code Stop hook block cap defaults to 8 — perpetual `/goal` appears to stop after ~8 rounds

## Summary

Claude Code's `/goal` command sets a session-scoped Stop hook whose condition is the goal text. When the agent's turn would naturally end, the hook fires; if the condition isn't satisfied, the hook **blocks** the stop and the agent continues. The harness has an **undocumented (in `code.claude.com/docs`) consecutive-block cap**, default `8`, controlled by `CLAUDE_CODE_STOP_HOOK_BLOCK_CAP`. After 8 consecutive Stop-hook blocks the harness **overrides** the hook for that turn (`reason: "completed"`, telemetry `tengu_stop_hook_block_count {hit_cap: true}`). The hook itself is NOT cleared — it stays armed in the session — but the turn ends and the operator perceives "the goal was removed". Setting `CLAUDE_CODE_STOP_HOOK_BLOCK_CAP` to a high value (or `0` to fully disable the cap) unlocks long-running perpetual-`/goal` conversations.

## Context

When does this lesson apply?

- You issue a `/goal <condition>` that's intentionally unsatisfiable ("Continue Endlessly", "keep working until X", any perpetual mandate).
- The agent ships rounds in a loop, each round naturally completing → Stop hook fires → blocks → agent re-enters.
- Roughly **every 8 rounds** the conversation ends abruptly with a warning text "A hook blocked the turn from ending N consecutive times — overriding and ending turn." (or just ends silently from the operator's terminal-side view if not surfaced).
- You re-issue `/goal` to keep going, perceive it as "the goal disappeared", and the pattern repeats.

The cap is **per-turn-block-streak**, not per-session. A user message between turns **resets** the counter to 0. So normal back-and-forth conversations never hit the cap; only long uninterrupted agent auto-loops do.

## Insight

> [!warning] Claude Code's Stop-hook safety cap turns "Continue Endlessly" into "continue for 8 blocks, then surrender". The cap exists to protect against runaway broken hooks, but it can't distinguish "intentionally perpetual" from "stuck and broken" — so a working perpetual `/goal` triggers the same kill switch as a misconfigured one.
>
> | Aspect | Before fix (default cap 8) | After fix (cap raised) | Evidence |
> |--------|----------------------------|------------------------|----------|
> | Consecutive Stop-hook blocks before turn ends | 8 | up to `CLAUDE_CODE_STOP_HOOK_BLOCK_CAP` (or unlimited if 0) | Decompiled control flow in `/opt/claude-code/bin/claude`: `B$ = Number.isNaN(l$) ? 8 : l$; if (B$ > 0 && p$ > B$) return ..., {reason: "completed"}` |
> | Telemetry on cap hit | `tengu_stop_hook_block_count {count: N, hit_cap: true}` | (event still fires if cap raised + crossed, just at higher N) | Same source — emitted before the override-and-end-turn return |
> | Apparent symptom | "Goal keeps being removed", conversation stops | `/goal` blocks stops indefinitely up to chosen cap | Operator-observed glitch report |
> | Actual state of the hook | Still armed in session (NOT cleared) | Still armed | Re-issuing `/goal` REPLACES the hook with same text; no functional change |

## The cap mechanism (decompiled)

Approximate JavaScript from `/opt/claude-code/bin/claude` (variable names from the minified bundle):

```js
if (D$.blockingErrors.length > 0) {
  let x$ = R + 1,                   // turn count
      p$ = C + 1;                   // consecutive Stop-hook block count

  // Max-turns kill (separate kill switch)
  if (O && x$ > O)
    return d("tengu_stop_hook_block_count",
             { count: p$, is_subagent: ..., hit_max_turns: true, hit_cap: false }),
           yield AK({ type: "max_turns_reached", maxTurns: O, turnCount: x$ }),
           { reason: "max_turns", turnCount: x$ };

  // Block-cap kill (the glitch under investigation)
  let l$ = parseInt(process.env.CLAUDE_CODE_STOP_HOOK_BLOCK_CAP ?? "", 10),
      B$ = Number.isNaN(l$) ? 8 : l$;
  if (B$ > 0 && p$ > B$)
    return d("tengu_stop_hook_block_count",
             { count: p$, is_subagent: ..., hit_max_turns: false, hit_cap: true }),
           yield kA(
             `A hook blocked the turn from ending ${p$} consecutive times ` +
             `— overriding and ending turn. For Stop/SubagentStop hooks, ` +
             `check stop_hook_active in the input and return success while ` +
             `it's true. Set CLAUDE_CODE_STOP_HOOK_BLOCK_CAP to raise this limit.`,
             "warning"
           ),
           { reason: "completed" };          // ← turn ends, hook NOT cleared

  // Otherwise re-enter the agent loop with incremented counter
  j = { ..., stopHookActive: true, stopHookBlockingCount: p$, ... };
  continue;
}
```

Key observations:

1. **Default is 8** (`Number.isNaN(l$) ? 8 : l$`).
2. **Setting `CLAUDE_CODE_STOP_HOOK_BLOCK_CAP=0` disables the cap entirely** (the guard `B$ > 0 && p$ > B$` short-circuits when `B$` is 0 or negative).
3. **The hook isn't cleared** — only that turn's loop is overridden. State `stopHookActive: true` would carry forward; only `stopHookBlockingCount` matters for the cap.
4. **A user message resets the counter** — the `j.stopHookBlockingCount = p$` carries forward inside one auto-loop; a new prompt creates a fresh query and the counter restarts at 0.
5. **Separate kill switches**: `max_turns` (`reason: "max_turns"`) is independent from the block cap (`reason: "completed"`). Both can fire; the cap's "completed" disguises itself as a normal turn end.

## The operator-perceived "glitch" decomposition

| Operator sees | Actual mechanism |
|---|---|
| "/goal keeps being removed" | Hook isn't removed — it's overridden once per turn after 8 blocks. Next message re-arms it because the session still holds the hook config. Re-issuing `/goal` replaces it with identical text → no functional change. |
| "Conversation stops after some rounds" | After 8 consecutive auto-loops without a user message, `hit_cap: true` fires and `reason: "completed"` ends the turn. |
| "Works at first, then stops" | First user message + 8 agent auto-rounds = 8 blocks = cap hit. Any user message in between resets the count. So "/goal" right before a long unattended session caps out; "/goal" with active back-and-forth doesn't. |
| "Goal command is broken" | Goal command works as designed. The cap is the broken-feeling part — it's a safety against runaway hooks that can't distinguish "perpetual mandate" from "stuck loop". |

## Fix: raise (or disable) the cap

Add to `~/.claude/settings.json` under the `env` block:

```json
{
    "$schema": "https://json.schemastore.org/claude-code-settings.json",
    "env": {
        "CLAUDE_CODE_STOP_HOOK_BLOCK_CAP": "1000"
    },
    "permissions": { ... }
}
```

Three sensible values:

| Value | Behavior | When to use |
|---|---|---|
| `"0"` | Cap fully disabled (`B$ > 0` short-circuits to false). Stop hook blocks indefinitely. | When you genuinely want infinite continuation and trust your hook condition. |
| `"1000"` (recommended) | Cap raised to 1000 consecutive blocks. Practically unlimited for perpetual `/goal`; still kills genuinely-stuck hooks. | Default-safe upgrade. |
| `"8"` (default) | Status quo. | Only if you don't use perpetual mandates. |

**The setting only takes effect at session start** (per Claude Code's settings caching — see sibling lesson `claude-code-settings-local-hot-reload-vs-settings-cache.md`). To activate immediately, restart the session OR for CLI users, export the env var in the shell that launches the harness.

## Adjacent findings from the investigation

- **The `~/.claude/stop-hook-git-check.sh` script is shipped by default** but is NOT wired into any `hooks.Stop` entry in `~/.claude/settings.json` — it's inert unless explicitly registered. (It blocks stops on uncommitted/unpushed git state.) If you're seeing the cap fire AND you have this script wired, fix both.
- **No managed/policy settings interfere** (`disableAllHooks`, `allowManagedHooksOnly`, `policyHelper`) unless explicitly set at the admin layer. Verify with `cat /etc/claude-code/managed-settings.json` and the HKLM registry on Windows.
- **`tengu_stop_hook_block_count`** is the telemetry event name; if you have access to telemetry it's the canonical way to confirm cap hits in production.
- **Binary location for verification**: `strings /opt/claude-code/bin/claude | grep CLAUDE_CODE_STOP_HOOK_BLOCK_CAP` — confirms the env var name + the surrounding control flow.

## What this unlocks

Per the operator's reaction ("this means I could unlock a lot of conversation"):

1. **Perpetual `/goal` mandates work as intended.** Set the cap high (or 0), and a single `/goal Continue Endlessly toward X` can drive thousands of auto-rounds without re-issue.
2. **Long unattended automation runs.** Background-style agent loops (research, refactor pipelines, multi-stage builds) can run their full course without operator re-engagement just to reset the counter.
3. **No more "did the goal clear?" anxiety.** The hook isn't being cleared — the cap is hitting. Once raised, the perceived flakiness disappears.
4. **Compounds with PR-watching subscriptions.** Combined with `subscribe_pr_activity`, an agent can babysit CI / review comments AND keep auto-progressing main-branch work for arbitrary duration.

## Anti-patterns to avoid

- **Don't set the cap absurdly high "just in case"** without also having a genuine kill-switch elsewhere. If the cap is your only safety against runaway hooks, raising it to 1000000 just delays the kill — for misbehaving hooks, that's still a real cost. The recommendation of `1000` is the sweet spot: practically unlimited for perpetual mandates, still finite for true bugs.
- **Don't conflate `max_turns` with `block_cap`**. They're separate. `max_turns` is a session-wide turn ceiling; `block_cap` is a per-loop consecutive-block ceiling. Configure both deliberately.
- **Don't expect editing `~/.claude/settings.json` to take effect mid-session.** The env block is read at session start, per the caching asymmetry. Restart or use `~/.claude/settings.local.json` for hot-reload of env (note: env-var hot-reload behavior of `settings.local.json` was not verified in this investigation; assume cold-only for safety).

## Cross-references

- `wiki/lessons/01_drafts/claude-code-settings-local-hot-reload-vs-settings-cache.md` — settings file caching asymmetry; relevant for understanding when the cap-raise takes effect.
- `wiki/lessons/01_drafts/claude-code-hook-additionalcontext-is-event-specific-not-all-events-accept-it.md` — sibling lesson on Stop hook return-value semantics.
- `wiki/decisions/02_validated/tools/hooks-design-decisions.md` — broader hooks design decisions (validated layer).
- `wiki/lessons/03_validated/tools-architecture/hook-scope-machine-vs-project-level-cross-firing-anti-pattern.md` — hook-scope hygiene.

## Status: draft → ready to synthesize

This lesson is at draft status, layer 4. To promote: empirical verification on a separate machine (set the env var, run a perpetual `/goal`, count rounds before cap hit at default 8 vs raised 1000), check whether `settings.local.json` hot-reloads the env block, and confirm `tengu_stop_hook_block_count` event appears in the local telemetry log.
