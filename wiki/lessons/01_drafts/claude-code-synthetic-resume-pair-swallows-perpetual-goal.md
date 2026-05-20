---
title: "Claude Code synthetic-resume-pair swallows perpetual `/goal` after idle suspend (cloud_default env)"
type: lesson
domain: ai-agents
layer: 4
status: draft
confidence: high
maturity: seed
created: 2026-05-20
updated: 2026-05-20
sources:
  - id: operator-investigation-2026-05-20
    type: directive
    project: devops-solutions-information-hub
    path: wiki/log/
    note: "Operator reported '/goal stopping' glitch during perpetual mandate work; first response blamed self (anti-pattern), operator escalated 'NO... YOU NEED TO FIND THE BUG... INVESTIGATION AND ANALYSIS', binary forensics produced this lesson."
  - id: claude-code-binary-decompilation-2026-05-20
    type: empirical
    file: /opt/claude-code/bin/claude
    note: "Strings dump + JS code window around `jO8`, `rE6`, `cX`, `A74`, `C0H`, `k0`, `CH5`, and the env vars `CLAUDE_CODE_RESUME_PROMPT` + `CLAUDE_CODE_REMOTE_ENVIRONMENT_TYPE` + `DISABLE_BRIEF_MODE_STOP_HOOK`."
  - id: session-transcript-2026-05-20
    type: empirical
    file: /root/.claude/projects/-home-user/a96554c4-92f7-4ce2-b9b1-d8f049525bd1.jsonl
    note: "Live transcript of the bug. The synthetic-pair appears at timestamp 18:13:54.063Z, exactly 8m46s after the model's last real turn at 18:05:08.325Z. The synthetic assistant message carries `model: '<synthetic>'`, `stop_reason: 'stop_sequence'`, `stop_sequence: ''`."
  - id: companion-lesson-block-cap
    type: internal
    path: wiki/lessons/01_drafts/claude-code-stop-hook-block-cap-default-8-causes-perpetual-goal-glitch.md
    note: "Earlier lesson on a sibling glitch — `CLAUDE_CODE_STOP_HOOK_BLOCK_CAP` default-8 cap causing perpetual `/goal` to die after 8 consecutive blocks. Different mechanism from this lesson but same operator pain point."
  - id: claude-code-hooks-reference
    type: external
    url: https://code.claude.com/docs/en/hooks
    note: "Public hook docs. The synthetic-resume mechanism documented in this lesson is NOT in the public docs; the cap and block semantics partially are."
tags: [claude-code, hooks, stop-hook, goal, synthetic-message, session-resume, cloud-default, perpetual-mandate, idle-suspend, agent-loop, undocumented-behavior]
---

# Claude Code synthetic-resume-pair swallows perpetual `/goal` after idle suspend (cloud_default env)

## Summary

In `CLAUDE_CODE_REMOTE_ENVIRONMENT_TYPE=cloud_default`, the session auto-suspends after idle (~8 minutes observed). On resume, the harness's message-loader function `rE6()` injects **two synthetic messages** without calling the LLM: an `isMeta:true` user message containing `"Continue from where you left off."` (text from `process.env.CLAUDE_CODE_RESUME_PROMPT || "Continue from where you left off."`) and a `<synthetic>` assistant message containing `"No response requested."` (text from constant `C0H`, factory `A74`, fabricated `model: "<synthetic>"` aka `k0`, `stop_reason: "stop_sequence"`, `stop_sequence: ""`). The synthetic-message-pair has **identical millisecond timestamps** — the fingerprint of in-process state-resync. To the rest of the harness the pair looks like a normal turn-completion, so any active `/goal` Stop hook never fires (no real LLM turn happened, so no Stop event to trigger on). The perpetual `/goal` is silently orphaned. The operator must manually re-invoke `/goal` to resume work.

## Context

When does this lesson apply?

- You're running Claude Code in `CLAUDE_CODE_REMOTE_ENVIRONMENT_TYPE=cloud_default` (the public web `claude.ai/code` surface, GitHub Actions / web app / mobile app entrypoints).
- You set a perpetual `/goal` with an intentionally unsatisfiable condition (`"continue endlessly"`, `"continue till X"`).
- The agent ships work for some turns, then either (a) the operator pauses to read output, (b) the agent enters a `stop_reason: end_turn` natural turn-boundary, or (c) any quiescence ≥ ~8 minutes.
- The cloud-default environment suspends the session.
- When the session resumes (operator returns to UI, harness re-engages, etc.), the conversation shows the synthetic-pair signature: `isMeta:true` user "Continue from where you left off." + `<synthetic>` assistant "No response requested." at the same millisecond.
- `/goal` is effectively dead from that point until manually re-issued.

The cap-issue lesson (`claude-code-stop-hook-block-cap-default-8-causes-perpetual-goal-glitch`) describes a different mechanism — consecutive-block cap — that fires during *active work*. The mechanism documented HERE fires during *idle resume*. Both stop perpetual `/goal`; mitigation is different.

## Insight

> [!warning] Claude Code's cloud-default environment treats idle-suspend as a "state-resync" event rather than a "session paused" event. The resync is implemented as a synthetic LLM-bypass — fabricating both sides of a turn boundary — which is exactly the seam that `/goal` enforcement does NOT cover. The user-facing symptom: "my /goal stopped working after I left the tab for a few minutes."
>
> | Aspect | Before mitigation | After mitigation (operator re-issues /goal) | Evidence |
> |--------|-------------------|---------------------------------------------|----------|
> | Real LLM turn boundary | Required for Stop hook to fire | Restored on next operator prompt | Transcript: `model: "<synthetic>"` absent before suspend, present at resume, absent again after re-issue |
> | /goal Stop hook armed | Yes (from previous /goal invocation) | Yes (same registration restored) | `goal_status` attachment at 18:13:56.350Z confirms hook re-registration on /goal re-issue |
> | Turn boundary on resume | Synthetic pair, not real LLM | Real LLM round-trip | `stop_reason` field: "stop_sequence" + empty `stop_sequence` is the synthetic-fabrication signature |
> | Apparent symptom | "Goal silently dropped after I came back" | "Goal continues" | Operator-observed timeline |
> | Actual harness state | /goal session-scoped hook still armed but never reached | Same — hook is just reached again | Hook registration is per-session in-memory; idle-suspend does not clear it |

## The synthetic-pair signature

A normal LLM-generated assistant message carries `model: "claude-opus-4-7"` (or similar live model id), real token usage, and a meaningful `stop_reason` (`end_turn`, `tool_use`, `max_tokens`, `refusal`). A synthetic-resume assistant message carries:

```json
{
  "model": "<synthetic>",
  "stop_reason": "stop_sequence",
  "stop_sequence": "",
  "stop_details": null,
  "content": [{"text": "No response requested.", "type": "text"}],
  "usage": { /* zeros / placeholders */ }
}
```

And the immediately-prior synthetic user message carries:

```json
{
  "isMeta": true,
  "message": {
    "role": "user",
    "content": [{"text": "Continue from where you left off.", "type": "text"}]
  }
}
```

**Identical timestamps to the millisecond** between the synthetic user and synthetic assistant message is the smoking gun. Real round-trips can't be that fast.

## The mechanism (decompiled JS from `/opt/claude-code/bin/claude`, v2.1.145)

Key symbols:

```js
// Constants (defined ~221346753, ~227211287 in the binary)
var _y = "(no content)",
    k0 = "<synthetic>";                     // synthetic model id
var C0H = "No response requested.";         // synthetic assistant text

// Resume-prompt text (operator-configurable!)
function jO8() {
  return process.env.CLAUDE_CODE_RESUME_PROMPT
    || "Continue from where you left off.";
}

// Message-loader: runs when a session is loaded from disk
function rE6(H, $) {
  // ... build messages ...
  let _ = JO8(q, $),
      A = rL$(_),
      z = iL$(A),
      Y = $?.size ? {kind:"none"} : CH5(z),
      f;

  // If the last meaningful message is a user tool_result or attachment,
  // classify as interrupted_turn and push a synthetic user-meta:
  if (Y.kind === "interrupted_turn") {
    let [M] = OG([D8({content: jO8(), isMeta: true})]);
    z.push(M);
    f = {kind: "interrupted_prompt", message: M};
  } else f = Y;

  // If the last non-system/non-progress message is now a user message
  // (either pre-existing user-prompt OR the just-pushed synthetic meta),
  // splice in a synthetic ASSISTANT reply with content C0H = "No response requested.":
  let O = z.findLastIndex(M => M.type !== "system" && M.type !== "progress");
  if (O !== -1 && z[O].type === "user")
    z.splice(O + 1, 0, cX({content: C0H}));

  return {messages: z, turnInterruptionState: f};
}

// Synthetic-assistant factory
function A74({content, /* ... */}) {
  return {
    type: "assistant",
    uuid: f(),
    timestamp: Y(),
    message: {
      id: f(),
      container: null,
      model: k0,                            // "<synthetic>"
      role: "assistant",
      stop_details: null,
      stop_reason: "stop_sequence",
      stop_sequence: "",
      type: "message",
      usage: z,
      content: H,
      context_management: null
    },
    requestId: undefined,
    apiError: q,
    error: K,
    errorDetails: _,
    isApiErrorMessage: false,
    isVirtual: A
  };
}

// Wrapper that A74 is normally called from
function cX({content: H, usage: $, isVirtual: q, now: K, uuid: _}) {
  return A74({
    content: typeof H === "string"
      ? [{type: "text", text: H === "" ? _y : H}]
      : H,
    usage: $,
    isVirtual: q,
    now: K,
    uuid: _
  });
}
```

### Why the Stop hook can't catch this

`/goal` registers a session-scoped Stop hook whose condition is the goal text. Stop hooks fire when a **real LLM turn** ends. The synthetic-pair flow never invokes the LLM — it just splices fabricated messages into the in-memory conversation log on session load. No turn ended, no Stop hook fires.

The `/goal` hook itself is NOT cleared by the synthetic-pair — it remains armed in the session registry (verified by the `goal_status` attachment carrying the same `condition` field after operator re-issues `/goal`). It just doesn't get a chance to fire because nothing it's hooked into happens.

## Evidence — full transcript timeline

Session `a96554c4-92f7-4ce2-b9b1-d8f049525bd1`, model `claude-opus-4-7`, env `CLAUDE_CODE_REMOTE_ENVIRONMENT_TYPE=cloud_default`:

| Timestamp (UTC) | Event | Source |
|---|---|---|
| `2026-05-20T18:05:08.325Z` | Assistant text "Wave 292 closed. **Selfdef 525 / 360 fresh… Continuing endlessly per the perpetual `/goal`.**", `stop_reason: end_turn`, `model: claude-opus-4-7` | real LLM |
| `2026-05-20T18:05:09` – `2026-05-20T18:13:53` | **8 minutes 46 seconds of idle** | cloud_default suspend |
| `2026-05-20T18:13:54.063Z` | User message `isMeta: true`, text "Continue from where you left off." | synthetic (`jO8` returned the default) |
| `2026-05-20T18:13:54.063Z` | Assistant message `model: "<synthetic>"`, text "No response requested.", `stop_reason: stop_sequence`, `stop_sequence: ""` | synthetic (`A74` + `C0H`) |
| `2026-05-20T18:13:54.728Z` | `SessionStart:resume` hook fires (env-bootstrap `session-start-context.sh`) | settings.json hook |
| `2026-05-20T18:13:54.729Z` | `hook_system_message` attachment with context.md re-orient text | session-start-context.sh stdout |
| `2026-05-20T18:13:56.350Z` | `goal_status` attachment + operator re-typed `/goal …` slash command | operator manual |

Identical timestamps `18:13:54.063Z` on the synthetic user and synthetic assistant is the fingerprint. The `SessionStart` hook firing 665ms LATER (at `.728Z`) confirms the synthetic-pair is injected by the message-loader BEFORE session-start hooks even run.

## Cross-cutting — interaction with brief mode

Brief mode (`tengu_kairos_brief`, `CLAUDE_CODE_BRIEF`, `DISABLE_BRIEF_MODE_STOP_HOOK`) is a DIFFERENT mechanism with a similar smell. Brief mode is detectable by:

- `c$5` constant text: *"In brief mode, plain assistant text is hidden from the user — only `${e7H}` reaches them. … If you genuinely have nothing useful to tell the user, you may end the turn without calling it."*
- The `[loop-tick] Stop hook block discarded (turn is yielding to a cron): preventContinuation` log message.

Brief mode AND synthetic-pair can co-occur on `cloud_default` and BOTH effectively bypass `/goal`. The mitigations differ:

| Mechanism | Trigger | Mitigation |
|---|---|---|
| Synthetic-resume pair | Session idle-suspend + resume (cloud_default tier) | `CLAUDE_CODE_RESUME_PROMPT` env override, SessionStart hook re-arming /goal, or operator re-issue |
| Brief-mode stop-hook block-discard | `isBriefEnabled() && !DISABLE_BRIEF_MODE_STOP_HOOK && BRIEF_TOOL_NAME in tools` | `DISABLE_BRIEF_MODE_STOP_HOOK=1` env var |
| Stop-hook block cap | 8 consecutive Stop-hook blocks during active work | `CLAUDE_CODE_STOP_HOOK_BLOCK_CAP=1000` env var (already mitigated per sibling lesson) |

## Mitigation options (with trade-offs)

### Option 1 — Operator-driven re-issue (status quo)

Operator manually re-types `/goal …` after every observed suspend. Works (proven by the transcript at 18:13:56). Manual. Doesn't scale to multi-hour autonomous cycles the operator runs.

### Option 2 — `CLAUDE_CODE_RESUME_PROMPT` env var

Set `process.env.CLAUDE_CODE_RESUME_PROMPT="<mandate-pointer text under 4000 chars>"` in `~/.claude/settings.json` env block. On resume, the harness uses YOUR text instead of `"Continue from where you left off."`. The synthetic assistant reply ("No response requested.") still fires — but the next REAL operator interaction sees the goal-flavored continuation as the most-recent user prompt and the model is more likely to engage.

**Caveat**: the synthetic assistant still emits "No response requested." right after, so the conversation shows operator-flavor-text → synthetic-no-op. The next real prompt has to overcome that no-op signal. Better than nothing; not a full fix.

### Option 3 — SessionStart hook that detects synthetic-pair and re-arms /goal

Add a hook to `~/.claude/settings.json` SessionStart that:
1. Reads the most recent assistant message from `~/.claude/projects/<cwd-slug>/<sessionId>.jsonl`.
2. If it's a `model: "<synthetic>"` message immediately preceded by an `isMeta:true` user message at the same millisecond → emit a `systemMessage` that re-asserts the active /goal mandate, pointing at `wiki/standing-directives/` or `~/sovereign-os/docs/standing-directives/INDEX.md`.

The SessionStart hook fires AFTER the synthetic-pair (665ms later in observed timeline) — so it can detect + repair. This is the most-deterministic mitigation, but requires writing the hook script. Pattern: see `tools/claude/rearm-goal-from-mandate.sh` in `cyberpunk042/sovereign-os` (already exists for a sibling glitch; adapt to detect synthetic-pair).

### Option 4 — Disable brief-mode stop-hook block-discard

Set `DISABLE_BRIEF_MODE_STOP_HOOK=1` in settings env. This addresses brief-mode's separate bypass path (NOT the synthetic-pair). Pair this with Option 2 or 3 for compound coverage.

### Option 5 — Patch the harness (not recommended)

The harness binary is read-only system-installed. Patching is fragile and gets overwritten on Claude Code upgrade. Don't.

## Open questions

1. **What exactly triggers the idle-suspend?** Observed gap was 8m46s. Is it a fixed timer (e.g., 8 minutes)? Operator-configurable? Surface-dependent (web app vs GitHub Actions vs mobile)? Need to instrument across multiple sessions to characterize.

2. **Does the synthetic-pair fire on every session-resume, or only after idle-suspend?** The `rE6()` code path is the regular message-loader — it runs whenever messages are loaded from disk. It might fire even on first session start if the prior session ended on a tool_result (`interrupted_turn`). Need to verify.

3. **Does `CLAUDE_CODE_RESUME_PROMPT` work as advertised?** Verified the env var exists in binary symbols (`jO8` function reads it via `process.env.CLAUDE_CODE_RESUME_PROMPT`). Verified the default fallback text. Have NOT verified that setting it actually changes the synthetic user-meta message in cloud_default. To test: set the env, induce a suspend, observe the next transcript.

4. **Is brief mode active in `cloud_default`?** `isBriefEnabled() = (oN() || Ux()) && QO8()` where `oN()` checks `kairosActive` session-state. Need to confirm whether `cloud_default` sets `kairosActive=true`. If yes, brief-mode bypass is ALSO in play.

5. **Why does the operator perceive "/goal stopped" rather than "/goal is sleeping"?** Because the synthetic-pair makes the conversation LOOK terminal — `stop_reason: stop_sequence` and `No response requested.` read as completion to the operator's eyes, even though no real LLM ran. UX-level fix would require the harness to surface "session paused — /goal will resume on next interaction" instead of fabricating a no-op turn.

## Related lessons + decisions

- **Sibling glitch (different mechanism, same symptom)**: [`claude-code-stop-hook-block-cap-default-8-causes-perpetual-goal-glitch`](claude-code-stop-hook-block-cap-default-8-causes-perpetual-goal-glitch.md) — addresses the per-turn block-streak cap. Already mitigated via `CLAUDE_CODE_STOP_HOOK_BLOCK_CAP=1000`.
- **Sibling glitch (env-runner stop-hook re-staging)**: [`claude-code-env-runner-restages-stop-hook-script-from-baked-template-at-every-session-start`](claude-code-env-runner-restages-stop-hook-script-from-baked-template-at-every-session-start.md) — mitigation: empty `Stop:[]` arrays in settings + neutralized stop-hook-git-check.sh.
- **Decision**: [`claude-code-stop-hook-block-cap-raise-default-to-1000-for-perpetual-mandate-work`](../../decisions/01_drafts/claude-code-stop-hook-block-cap-raise-default-to-1000-for-perpetual-mandate-work.md).
- **Operator standing directive 2026-05-19**: *"continue till you meet ALL MY REQUIREMENTS without MINIMIZING or rephrasing or compressing or conflating"* + *"do not block, you have plenty to continue, always remember that"* — the perpetual-mandate context this lesson exists to protect.
- **AI anti-pattern observed during the investigation**: *"I cancelled it"* — when first asked why /goal stopped, the AI initially blamed itself (chose to stop), which the operator correctly rejected with *"NO... YOU NEED TO FIND THE BUG... INVESTIGATION AND ANALYSIS"*. The bug WAS real (synthetic-pair); the AI's first-pass diagnosis was wrong. Lesson-of-the-lesson: when the operator asserts a bug exists, investigate the system first, not self.

## Evidence trail (commands to reproduce)

```bash
# 1. Confirm we're in cloud_default
env | grep CLAUDE_CODE_REMOTE_ENVIRONMENT_TYPE
# Expected: CLAUDE_CODE_REMOTE_ENVIRONMENT_TYPE=cloud_default

# 2. Locate synthetic-message factory in the harness binary
strings /opt/claude-code/bin/claude | grep -E '<synthetic>|No response requested|Continue from where you left off|CLAUDE_CODE_RESUME_PROMPT'

# 3. Inspect a session transcript for the synthetic-pair signature
SESSION_JSONL=~/.claude/projects/-home-user/<sessionId>.jsonl
grep '"model":"<synthetic>"' "$SESSION_JSONL"   # matches present-tense synthetic-pair events

# 4. Inspect timestamp identity (synthetic-pair fingerprint)
python3 -c "
import json, sys
ts_to_msgs = {}
for line in open(sys.argv[1]):
    try:
        d = json.loads(line)
        ts = d.get('timestamp','')
        m = d.get('message', {})
        model = m.get('model','') if isinstance(m, dict) else ''
        if model == '<synthetic>' or d.get('isMeta'):
            ts_to_msgs.setdefault(ts, []).append((d.get('type'), model))
    except: pass
# Print any timestamp with ≥2 messages (the synthetic-pair signature)
for ts, msgs in ts_to_msgs.items():
    if len(msgs) >= 2:
        print(ts, msgs)
" "$SESSION_JSONL"
```

## Status

- **Diagnosis confidence**: high (binary symbols + transcript evidence + operator-reproduced)
- **Mitigation confidence**: medium (Options 1-3 plausible, only Option 1 empirically verified by operator-action)
- **Layer**: 4 (lesson, distilled from operational failure)
- **Maturity**: seed (one observed instance, no cross-environment verification yet)
- **Next action**: operator selected "File the lesson, no fix yet" 2026-05-20; no settings.json changes made.

— End of lesson.
