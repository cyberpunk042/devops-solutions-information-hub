---
title: "Lesson — Claude Code hook output channel is event-specific; `hookSpecificOutput.additionalContext` is valid for only 6 events (PostCompact / Stop / SessionEnd / others reject it)"
type: lesson
domain: ai-agents
status: synthesized
confidence: high
maturity: seed
layer: 2
created: 2026-05-09
updated: "2026-05-09"
sources:
  - id: claude-code-hooks-reference
    type: file
    file: raw/articles/claude-code-hooks-reference.md
    description: "Official Claude Code hooks reference compiled 2026-04-09 — line 23 enumerates the 5 documented events that accept additionalContext (SessionStart / UserPromptSubmit / PreToolUse / PostToolUse / SubagentStart). PostToolBatch added later, also accepts additionalContext (verified empirically 2026-05-09 via schema-rejection error)."
  - id: empirical-2026-05-06-stamp-bug
    type: empirical
    file: raw/notes/2026-05-06-claude-code-hook-stamp-bug-cached-config-vs-settings-local-hot-reload.md
    description: "Operator's 10x debugging arc on /root: Stop hook miswire to UserPromptSubmit + cached settings.json + the schema validity table at lines 122-128. Operator-stated 10x synthesis directive line 42 verbatim: \"its a lot of little details.. lets make sure we properly ingest and digest and synthesize all the knowledge about this an the 10x level of it.\""
  - id: empirical-2026-05-09-postcompact-orient
    type: empirical
    project: devops-solutions-information-hub
    path: .claude/hooks/post-orient.sh
    description: "Same class of bug re-encountered 2026-05-09: post-orient.sh wires PostCompact event to use hookSpecificOutput.additionalContext — fails with 'Hook JSON output validation failed — (root): Invalid input' because PostCompact is not in the whitelist of events that accept additionalContext."
  - id: companion-settings-local-hot-reload
    type: wiki
    file: wiki/lessons/01_drafts/claude-code-settings-local-hot-reload-vs-settings-cache.md
    description: "Sister lesson — same 2026-05-06 arc, caching half (settings.json caches at session start; settings.local.json hot-reloads per prompt)"
  - id: companion-user-level-path-resolution
    type: wiki
    file: wiki/lessons/01_drafts/user-level-settings-json-hook-path-resolution-relative-vs-home-prefixed.md
    description: "Sister lesson — same arc family, path-resolution half (user-level hook commands must use $HOME-prefixed or absolute paths, never relative)"
tags: [claude-code, hooks, hookSpecificOutput, additionalContext, systemMessage, schema-validation, event-output-validity, postcompact, stop-hook, lesson, draft, ai-agents, "2026-05-09"]
---

# Lesson — Claude Code hook output channel is event-specific

## Summary

In Claude Code, **the JSON output channel a hook can use is constrained per lifecycle event**, not free-form. `hookSpecificOutput.additionalContext` is valid for exactly **6 events** — SessionStart, UserPromptSubmit, PreToolUse, PostToolUse, PostToolBatch, SubagentStart — and emitting it for any other event (Stop, PostCompact, PreCompact, SessionEnd, Notification, SubagentStop, ConfigChange, etc.) causes Claude Code to reject the hook output with `"Hook JSON output validation failed — (root): Invalid input"`. The right channel for events outside the 6-event whitelist is typically `systemMessage` (display-only) or plain stdout (no schema validation, always works for command-type hooks). This is the **same class of bug** that hit /root's stamp regression on 2026-05-06 (Stop hook miswired to use `additionalContext`); it re-surfaced 2026-05-09 in /opt's `post-orient.sh` PostCompact hook. The schema-validity table at the heart of the fix was captured in the 2026-05-06 raw note but not previously promoted to a lesson — operator-stated 10x synthesis directive (sacrosanct, 2026-05-06): *"its a lot of little details.. lets make sure we properly ingest and digest and synthesize all the knowledge about this an the 10x level of it."* This lesson discharges that synthesis directive.

## Context

This lesson applies when:
- Authoring or debugging a Claude Code hook (any event)
- Choosing an output channel for hook JSON (`additionalContext` vs `systemMessage` vs `decision: "block"` vs plain stdout)
- A hook runs but Claude Code rejects the output with `"Hook JSON output validation failed — (root): Invalid input"`
- Diagnosing why a hook's output is not surfacing for the user despite the hook running successfully
- Migrating a hook between events (e.g., Stop → UserPromptSubmit) — the output channel constraints change

Does NOT apply to:
- Hook command **exit codes** (separate enforcement axis — `exit 2` blocks; `exit 0` allows)
- Hook **input** format (always stdin JSON regardless of event)
- Plain-text **stdout** output (works for any hook; the schema is only about JSON-structured outputs)

## Insight

> [!success] **The output channel a hook can use is determined by the event, not by the hook author**
>
> Each lifecycle event whitelists specific top-level fields in its JSON output schema. Picking the wrong channel is a schema violation, not a runtime failure — Claude Code rejects the entire hook output before processing it. The hook may as well not have run.

> [!warning] **`hookSpecificOutput.additionalContext` is the most-misused channel; only 6 events accept it**
>
> Whitelist (verified 2026-05-09): **SessionStart · UserPromptSubmit · PreToolUse · PostToolUse · PostToolBatch · SubagentStart**. Using it for **Stop / PostCompact / PreCompact / SessionEnd / Notification / SubagentStop / ConfigChange / TaskCreated / TaskCompleted** fails validation. The error message — `"(root): Invalid input"` — is opaque; it doesn't name the offending field, which is why this bug class wastes debugging time.

> [!info] **Mnemonic — `additionalContext` is for events that inject context into the agent's reasoning**
>
> The 6 whitelisted events all fire **while the agent is reasoning or about to reason**: SessionStart (top of session), UserPromptSubmit (start of prompt), PreToolUse (before tool), PostToolUse / PostToolBatch (after tool, agent still reasoning), SubagentStart (subagent starting). For events that fire **after** the agent has already acted (Stop, PostCompact, SubagentStop, SessionEnd) — the agent isn't reasoning anymore, so injecting context is meaningless. Use `systemMessage` (display-only) instead.

> [!tip] **The right default for non-`additionalContext` events is `systemMessage`**
>
> `systemMessage` is "shown to user" per the Claude Code docs. For end-of-cycle stamps (Stop), post-compact reminders (PostCompact), pre-compact handoffs (PreCompact), idle notifications, and similar — `systemMessage` is the universal-safe channel. Plain stdout also works for any command-type hook.

## The schema-validity table (the core artifact)

Distilled from [raw/articles/claude-code-hooks-reference.md](../../../raw/articles/claude-code-hooks-reference.md) line 23 + [raw/notes/2026-05-06-claude-code-hook-stamp-bug-cached-config-vs-settings-local-hot-reload.md](../../../raw/notes/2026-05-06-claude-code-hook-stamp-bug-cached-config-vs-settings-local-hot-reload.md) lines 122-128 + empirical 2026-05-09 PostCompact rejection:

| Event | `hookSpecificOutput.additionalContext` | `systemMessage` | `decision: "block"` + `reason` | Plain stdout | Other event-specific fields |
|---|---|---|---|---|---|
| **SessionStart** | ✅ | ✅ | — | ✅ | — |
| **UserPromptSubmit** | ✅ | ✅ | ✅ (block prompt) | ✅ | — |
| **PreToolUse** | ✅ | ✅ | ✅ (block tool) | ✅ | `permissionDecision` (`allow`/`deny`/`ask`/`defer`), `updatedInput` |
| **PostToolUse** | ✅ | ✅ | — | ✅ | — |
| **PostToolBatch** | ✅ | ✅ | — | ✅ | — |
| **SubagentStart** | ✅ | ✅ | — | ✅ | — |
| **Stop** | ❌ | ✅ | ✅ (block stop, force continuation) | ✅ | `continue`, `stopReason` |
| **SubagentStop** | ❌ | ✅ | ✅ (block subagent stop) | ✅ | `continue` |
| **PreCompact** | ❌ | ✅ | — | ✅ | — |
| **PostCompact** | ❌ | ✅ | — | ✅ | — |
| **Notification** | ❌ | ✅ | — | ✅ | — |
| **PermissionRequest** | ❌ | — | ✅ | ✅ | `permissionDecision` |
| **ConfigChange** | ❌ | — | ✅ | ✅ | — |
| **TaskCreated** / **TaskCompleted** | ❌ | ✅ | ✅ | ✅ | — |
| **SessionEnd** | ❌ | — | — | ✅ | — |

Universal output fields (any event): `continue` (bool), `suppressOutput` (bool).

## Evidence

### 2026-05-06 — /root stamp regression (Stop hook miswire)

Operator's 10x debugging arc (50+ iterations). `end-of-cycle-stamp.sh` was authored to emit `hookSpecificOutput.additionalContext` for the Stop event. Result: stamp didn't render at end of response. Adding `systemMessage` channel — and moving the wiring to `settings.local.json` to escape the cached-settings.json miswire — fixed it.

Operator verbatim (sacrosanct, 2026-05-06):
- *"it worked... finally..."* (resolution moment)
- *"its a lot of little details.. lets make sure we properly ingest and digest and synthesize all the knowledge about this an the 10x level of it."* (the synthesis directive this lesson discharges)
- *"I should be a choice if we want start or end... not an uncontrolled bug.... we need to better master the hooks and tools and command integrations"*

Captured in [[2026-05-06-claude-code-hook-stamp-bug-cached-config-vs-settings-local-hot-reload]] (raw note, primary empirical source) lines 119, 122-128.

### 2026-05-09 — /opt post-orient.sh PostCompact bug (re-encounter)

Same class of bug, different event, this very session. After `/compact` ran, the second post-compaction hook (`post-orient.sh`) failed:

```
PostCompact [python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/post-orient.sh] failed:
Hook JSON output validation failed — (root): Invalid input

The hook's output was: {
  "hookSpecificOutput": {
    "hookEventName": "PostCompact",
    "additionalContext": "═══...POST-COMPACTION — RE-ORIENT THE SECOND BRAIN..."
  }
}
```

The hook was correctly wired (PostCompact event fires when expected), and the JSON shape was syntactically valid — but the **channel** (`additionalContext`) is not whitelisted for PostCompact. The companion `post-compact.sh` hook in the same chain ran fine because it uses plain stdout output, not structured JSON.

**Why it re-surfaced**: the schema-validity table existed in the raw note from 2026-05-06 but had not been promoted to a lesson. The empirical evidence stayed in raw/, so post-compact agent re-encountered the same bug class without recognition.

## Applicability

| Scenario | Apply this lesson? |
|---|---|
| Authoring a new hook for any non-`additionalContext` event | **YES** — pick channel from the table above before writing code |
| Debugging "Hook JSON output validation failed — (root): Invalid input" | **YES** — first hypothesis: wrong output channel for the event |
| Migrating hooks across events (e.g., Stop → UserPromptSubmit) | **YES** — output channel constraints change with the event |
| Iterating hook wiring during a live session | Pair with [[claude-code-settings-local-hot-reload-vs-settings-cache]] — write to `settings.local.json` for hot-reload |
| Hooks that emit only plain text on stdout | NO — plain stdout has no schema validation; always works |
| Hook **input** problems (stdin JSON malformed) | NO — different debugging axis |
| Hook **exit code** problems (block vs allow) | NO — different debugging axis |

## How to apply

1. **Pick the lifecycle event by semantics** (what state does the rule need to enforce at?), not by output convenience. The event determines what channels are available — design choice cascades from there.
2. **Look up the output channels** the event supports in the table above (or [Claude Code docs](https://code.claude.com/docs/en/hooks)).
3. **Pick the channel that fits the intent**:
   - Inject context into agent reasoning → `additionalContext` (only the 6 whitelisted events)
   - Display text to user without changing reasoning → `systemMessage`
   - Block the action → `decision: "block"` + `reason` (only events that allow blocking)
   - Free-form output (typically debugging or compatibility) → plain stdout
4. **Test in a real session** before committing. Empirical verification beats schema reading — Claude Code's schema rejection messages are opaque (`"(root): Invalid input"` doesn't name the offending field).
5. **If validation fails, read the session log**: `~/.claude/projects/<dir>/<session-id>.jsonl` records the actual `hookEvent` Claude Code assigned + content. If the recorded event ≠ the wired event → cached-miswire (sister bug; see [[claude-code-settings-local-hot-reload-vs-settings-cache]]). If the validation error fires on a correctly-wired event → output-channel mismatch (this lesson).

## Anti-patterns

| Anti-pattern | Why bad |
|---|---|
| Default to `hookSpecificOutput.additionalContext` for any structured-output hook | Only 6 events accept it; for the other ~20 events it fails validation |
| Treat `"(root): Invalid input"` as a transient/runtime issue | It's a structural schema mismatch — the entire output is rejected, the hook may as well not have run |
| Iterate hook fixes by editing `settings.json` mid-session | settings.json is cached at session start; edits don't take effect (sister bug — [[claude-code-settings-local-hot-reload-vs-settings-cache]]) |
| Cycle through invoker prefixes (`bash` → `python3` → ...) when validation fails | Misses the channel-mismatch root cause; wastes iterations |
| Fail to ingest empirical debugging arcs into lesson layer | Knowledge stays in raw/ → re-encountered → re-debugged. Operator's 10x synthesis directive exists for this reason |

## The discipline

When debugging or designing a Claude Code hook:

1. **Recognize the schema constraint**: output channels are event-specific, not free-form. The event sets the channels available, not the other way around.
2. **Search the wiki first**: `wiki_search "hook event additionalContext"` or grep — the knowledge may already exist as a lesson, raw note, or settings/path companion.
3. **Read the empirical raw note**: [[2026-05-06-claude-code-hook-stamp-bug-cached-config-vs-settings-local-hot-reload]] is the canonical detailed source for the broader hook-debugging arc.
4. **Use `systemMessage` as the safe default** for events that don't support `additionalContext`. Use plain stdout when in any doubt.
5. **When a hook fails validation, check the channel before changing the wiring**. The fix is usually a one-line channel swap, not a re-architecture.

## Sister-project applicability

Universal across any project using Claude Code hooks:

| Project | Risk and applicability |
|---|---|
| **root-ghostproxy** | High — propagates global hook config to all sister projects per [[2026-05-05-opt-in-transcension-of-root-features-to-individual-projects-directive]]; the validity table needs to be enforced at the propagation source so downstream projects don't re-encounter the bug |
| **/opt second-brain** (this) | Empirical evidence captured here; this lesson lives here per the boundary correction (knowledge = /opt; harness/ecosystem config propagation = root-ghostproxy) |
| **OpenArms / OpenFleet / AICP / devops-control-plane** | Inherit Claude Code config from root-ghostproxy propagation; rely on the same validity table; this lesson available cross-project via wiki sync |

## Relationships

- BUILDS ON: [[claude-code-hooks-reference|Claude Code Hooks Reference]] — the canonical 26-event lifecycle + 4 handler types + output channel reference
- BUILDS ON: [[2026-05-06-claude-code-hook-stamp-bug-cached-config-vs-settings-local-hot-reload|2026-05-06 Stamp Bug Empirical Note]] — primary empirical source; the schema validity table at lines 122-128 is distilled here as the core artifact
- DEMONSTRATED BY: [[audit-on-distillation-discipline-when-promoting-a-bug-class-to-lesson-layer-audit-codebase-immediately|Lesson — Audit-on-distillation discipline]] — this lesson's authoring 2026-05-09 was the empirical demonstration of the audit-on-distillation discipline (lesson + audit + fix in one arc, 1 instance found out of 7 hooks scanned)
- COMPLEMENTS: [[claude-code-settings-local-hot-reload-vs-settings-cache|Lesson — settings.local.json hot-reloads; settings.json caches]] — sister lesson covering the caching half of the same arc; pair when iterating hooks during a live session
- COMPLEMENTS: [[user-level-settings-json-hook-path-resolution-relative-vs-home-prefixed|Lesson — User-level settings.json hook paths must be `$HOME`-prefixed or absolute]] — sister lesson covering the path-resolution half of the same arc family
- DEMONSTRATES: [[infrastructure-over-instructions-for-process-enforcement|Principle 1 — Infrastructure Over Instructions]] — schema-validity is structural enforcement; learning the table is necessary infrastructure for hook design
- DEMONSTRATES: [[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4 — Declarations Aspirational Until Verified]] — declaring "the hook does X" without verifying the channel matches the event is aspirational; empirical run is the gate

## Cross-references

- Raw note (verbatim debugging arc, primary empirical source): `raw/notes/2026-05-06-claude-code-hook-stamp-bug-cached-config-vs-settings-local-hot-reload.md`
- Canonical hooks reference: `raw/articles/claude-code-hooks-reference.md`
- Companion lesson (caching): `wiki/lessons/01_drafts/claude-code-settings-local-hot-reload-vs-settings-cache.md`
- Companion lesson (path resolution): `wiki/lessons/01_drafts/user-level-settings-json-hook-path-resolution-relative-vs-home-prefixed.md`
- Hook architecture rules: `.claude/rules/hook-architecture.md`
- Live evidence: `.claude/hooks/post-orient.sh` (the 2026-05-09 PostCompact reproduction)

## Backlinks

[[Claude Code Hooks Reference]]
[[2026-05-06 Stamp Bug Empirical Note]]
[[Lesson — Audit-on-distillation discipline]]
[[Lesson — settings.local.json hot-reloads; settings.json caches]]
[[Lesson — User-level settings.json hook paths must be `$HOME`-prefixed or absolute]]
[[infrastructure-over-instructions-for-process-enforcement|Principle 1 — Infrastructure Over Instructions]]
[[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4 — Declarations Aspirational Until Verified]]
