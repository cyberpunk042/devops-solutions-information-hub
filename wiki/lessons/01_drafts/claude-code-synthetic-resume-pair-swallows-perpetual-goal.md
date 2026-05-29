---
title: "Claude Code synthetic-resume-pair swallows perpetual `/goal` after idle suspend (cloud_default env)"
type: lesson
domain: ai-agents
layer: 4
status: draft
confidence: high
maturity: growing
created: 2026-05-20
updated: 2026-05-26
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
  - id: session-transcript-2026-05-26
    type: empirical
    file: /root/.claude/projects/-home-user/8a4031f2-68e1-4375-8ad0-19e44feecdd9.jsonl
    note: "End-to-end confirmation. 3 idle-resume events (11:41/13:50/16:01Z, ~2h gaps) each producing a same-ms `model:<synthetic>` `No response requested.` paired with an isMeta user message carrying the CLAUDE_CODE_RESUME_PROMPT override text; each recovered ONLY by a manual operator /goal re-issue (rows 682/1746/1911). Both SessionStart systemMessages fired but triggered no real turn. Confirms Outcome 3 + corrects the 'model emits the no-op' misconception."
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

## Mitigations applied 2026-05-20 (operator approved)

After filing this lesson, operator re-engaged with *"yes lets go with your suggestions and made sure we record it too"* and approved applying mitigations 2 + 3 + 4 simultaneously (compound coverage). Changes landed in `scripts/claude-code-env/templates/` + `scripts/claude-code-env/apply.sh` so they survive container rebuilds + are mirrored to `~/.claude/env-bootstrap/templates/` automatically.

### Change 1 — env vars added to `templates/settings.json`

```json
"env": {
    "CLAUDE_CODE_STOP_HOOK_BLOCK_CAP": "1000",
    "CLAUDE_CODE_MAX_TURNS": "10000",
    "DISABLE_AUTOCOMPACT": "1",
    "CLAUDE_CODE_IDLE_THRESHOLD_MINUTES": "9999",
    "CLAUDE_CODE_RESUME_PROMPT": "Resume the perpetual /goal mandate immediately. ..."
}
```

- `CLAUDE_CODE_IDLE_THRESHOLD_MINUTES=9999` — defeats the in-binary `idle_prompt` (75-minute default).
- `CLAUDE_CODE_RESUME_PROMPT` — replaces the generic `"Continue from where you left off."` that `jO8()` would otherwise inject. The model now sees mandate-flavored text instead of a no-op-friendly placeholder.

### Change 2 — new SessionStart hook script `rearm-goal-on-resume.sh`

Lives at `~/.claude/rearm-goal-on-resume.sh` (installed by `apply.sh`). On every `SessionStart` event it:

1. Locates the current session transcript via `$CLAUDE_CODE_SESSION_ID` under `~/.claude/projects/`.
2. Greps for the `"model":"<synthetic>"` signature — the smoking-gun marker for synthetic-resume-pair injection.
3. Greps for evidence of an active `/goal` (look for `goal_status` attachment OR `/goal` command OR `activeGoal`).
4. If BOTH conditions hold, emits a `systemMessage` JSON on stdout explicitly telling the model: synthetic-resume was just detected, the operator did NOT stop, re-read `context.md`, pick the next unit, do NOT emit another `"No response requested."`.
5. Else exits silently (no false-trigger on fresh sessions or no-goal sessions).

The hook fires AFTER the synthetic-pair injection (~665ms later in observed timeline) — so detection works post-fact, and the systemMessage reaches the model on the next real turn.

Wired in `templates/settings.json` as the third SessionStart command, after `apply.sh --quiet` (auto-heal) and `session-start-context.sh` (context.md pointer).

### Change 3 — `apply.sh` FILES array extended

Added `session-start-context.sh:755` (was previously orphan — managed manually but not by apply.sh) and `rearm-goal-on-resume.sh:755` so both are now part of the idempotent install set. Container rebuild + fresh-clone reapply both ship the new hook automatically.

### Verification

`~/.claude/validate-stop-hook-fix.sh` 8 checks all green post-apply. Hook tested against the actual buggy session transcript (`a96554c4-92f7-4ce2-b9b1-d8f049525bd1`) — produced the expected `systemMessage` JSON on stdout, exit 0.

### Open empirical questions (post-mitigation)

The mitigations are deployed but the FULL CYCLE (idle-suspend → resume → operator sees mandate continuation, not "No response requested.") has NOT yet been observed end-to-end. Operator should test by walking away from the tab for ~10 minutes during the next perpetual /goal session. Three possible outcomes:

1. **Best case**: model engages on resume with mandate work
2. **Partial case**: synthetic "No response requested." still emits, but next real interaction sees mandate-flavored history + systemMessage banner → engages then
3. **No improvement**: synthetic-pair injected BEFORE systemMessage hook fires (timing race) AND synthetic reply masks the mandate sufficiently

Outcome 3 would require a deeper intervention (e.g. an `UserPromptSubmit` hook that filters out synthetic "No response requested." messages, or a periodic-poke daemon outside the harness).

## 2026-05-26 empirical confirmation (session `8a4031f2-68e1-4375-8ad0-19e44feecdd9`)

Operator reported again: *"the goal command is getting broken / stopped."* A live perpetual `/goal` selfdef session (108→111 modules shipped) was forensically examined. The full cycle is now observed end-to-end and **Outcome 3 is confirmed** — with one important correction to the earlier mental model.

### What the transcript proves

Three idle-resume events this session (`11:41:02Z`, `13:50:06Z`, `16:01:21Z` — ~2h gaps, operator-away duration, NOT the 8-min idle of the original capture). At each, the message-loader fabricated the synthetic pair:

| Resume | synthetic-user (isMeta) ts | synthetic-assistant ts | model | stop_reason | stop_sequence | same-ms |
|---|---|---|---|---|---|---|
| #1 (row 678) | 11:41:02.596Z | 11:41:02.596Z | `<synthetic>` | `stop_sequence` | `""` | YES |
| #2 (row 1740) | 13:50:06.718Z | 13:50:06.718Z | `<synthetic>` | `stop_sequence` | `""` | YES |
| #3 (row 1905) | 16:01:21.538Z | 16:01:21.539Z | `<synthetic>` | `stop_sequence` | `""` | +1ms |

Each recovery (rows 682, 1746, 1911) was a **manual operator `/goal` re-issue** (`<command-name>/goal</command-name>` → `Goal set: …`). Both SessionStart systemMessages fired and are present in the transcript (`SESSION-START RE-ORIENT` + `SYNTHETIC-RESUME DETECTED`) — yet **neither triggered a real turn**; the session sat dead until the operator typed `/goal`.

### Correction to the model (important)

Earlier framing (and the model's own in-session narration) treated the `"No response requested."` as *something the model emitted and should stop emitting* — the resume-prompt even contains the instruction *"Do NOT emit a 'No response requested.' no-op."* **The forensics prove this is wrong.** All three no-ops carry `model:"<synthetic>"` — they are **harness fabrications by `rE6()`/`A74`/`C0H`, not model output.** The model never got a turn. Instructing the model not to emit it is therefore inert: there is no model turn in which to obey. (This is itself a fresh instance of the §"AI anti-pattern" below — the in-session model kept "acknowledging the bug and correcting" as if it had authored the no-op, when in fact it had not.)

### CLAUDE_CODE_RESUME_PROMPT override: confirmed landing, but insufficient

The synthetic isMeta user message now carries OUR mandate text (verified: `prev.text` begins `"Resume the perpetual /goal mandate immediately. The operator did NOT stop…"`), not the bland default. So `jO8()` reads our env override correctly. **But** the hardcoded `C0H = "No response requested."` assistant splice still fires unconditionally after the trailing user message and terminates the turn. The override improves *content* the operator sees on return; it does not prevent the orphaning.

### Root-cause conclusion (refined)

The goal "stops" because **nothing converts the synthetic resync into a real LLM turn**, and the `/goal` Stop hook can only fire when a real turn ends:

1. cloud_default idle-suspends the session.
2. `rE6()` fabricates user-meta (our resume prompt) + `<synthetic>` `C0H` no-op at the same ms — no LLM call.
3. SessionStart hooks fire ~665ms later and queue their systemMessages **for the next turn** — but a SessionStart/PostCompact hook can only inject *context*; it **cannot synthesize a user turn or invoke the LLM.**
4. The conversation now ends on a fabricated assistant message → harness considers the turn complete → idles.
5. `/goal` Stop hook never fires (no real turn ended) → mandate orphaned.
6. Only a real user prompt restarts it. The operator's manual `/goal` is that prompt.

**Therefore the residual manual re-issue is architecturally irreducible inside cloud_default using hooks alone.** Options 2+3 are the maximal hook-layer mitigation; they cannot close the gap fully because no hook can manufacture a turn.

### Feasibility of the candidate "deeper" fixes (re-assessed)

| Candidate | Verdict | Why |
|---|---|---|
| `UserPromptSubmit` hook to suppress/replace the synthetic no-op | **Won't fire** | The synthetic user-meta is injected by the message-LOADER (`rE6`), not *submitted*. Only `SessionStart` fired in both captures; `UserPromptSubmit` does not fire for loader-injected meta. |
| In-container periodic-poke daemon (systemd timer / cron) that detects orphan-tail + injects a prompt | **Infeasible in cloud_default** | The container itself is suspended during idle, so an in-container timer is suspended too; and cloud_default exposes no supported "inject a real prompt into the live session" API. |
| Out-of-band poker on a NON-suspended host driving the session via the web/API | **Feasible but external** | Requires infra outside the suspended container (operator's machine or a separate always-on host). The only mechanism that can manufacture a real turn during/after suspension. |
| Reduce the trigger via `CLAUDE_CODE_IDLE_THRESHOLD_MINUTES` | **Already set (9999); does not help** | That env governs the in-binary `idle_prompt` (75-min), NOT the cloud platform's container suspension (~minutes–hours). No env stops the platform suspend. |
| Harness patch | **Not recommended** (unchanged) | Read-only, overwritten on upgrade. |
| Simplify `CLAUDE_CODE_RESUME_PROMPT` (drop the now-known-inert "Do NOT emit…No response requested." clause; make it a crisp first-action mandate) | **Low-value polish; needs operator approval (settings.json)** | The clause is inert (model never gets the turn) and the verbatim no-op string arguably primes that token sequence on the *next* real turn. Harmless to keep; cleaner to drop. Settings change → operator approval per work-mode. |

### Bottom line for the operator

This is a **Claude Code cloud_default harness limitation, not a config error on our side and not a model behavior we can prompt away.** The deployed mitigations (resume-prompt override + rearm SessionStart hook) are correct and maximal for the hook layer. The irreducible remainder — a single manual `/goal` after a long idle gap — can only be eliminated by (a) Claude Code making resume trigger a real turn, or (b) an out-of-band poker on an always-on host, or (c) a surface that suspends less aggressively. Recommend: keep current mitigations; optionally simplify the resume prompt (operator-approved); do NOT invest in in-container daemons (infeasible).

## Status

- **Diagnosis confidence**: high (binary symbols + transcript evidence + operator-reproduced + 2026-05-26 end-to-end confirmation)
- **Mitigation confidence**: high that the deployed mitigations are MAXIMAL for the hook layer; high that they are PARTIAL by construction (no hook can manufacture a real LLM turn). Residual manual `/goal` is architecturally irreducible in cloud_default with hooks alone.
- **Layer**: 4 (lesson, distilled from operational failure + applied mitigation + end-to-end confirmation)
- **Maturity**: growing (mechanism + mitigation + full-cycle behavior all observed; cross-surface characterization of suspend timing still open)
- **Resolved 2026-05-26**: full idle-resume cycle observed in session `8a4031f2`; Outcome 3 confirmed; "model emits the no-op" misconception corrected (it is harness-fabricated, `model:"<synthetic>"`); candidate deeper fixes re-assessed for feasibility (only an out-of-band poker on an always-on host can manufacture a turn).
- **Next action (operator decision)**: (1) accept the irreducible-remainder conclusion and keep current mitigations as-is, OR (2) approve a one-line `CLAUDE_CODE_RESUME_PROMPT` simplification (drop the inert "Do NOT emit…No response requested." clause), OR (3) stand up an out-of-band poker on an always-on host if the manual re-issue friction is unacceptable for long unattended cycles.

— End of lesson.
