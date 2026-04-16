---
title: "Research — Claude Code 2.1.94→2.1.111 + Opus 4.7 launch"
type: note
domain: log
status: active
note_type: directive
created: 2026-04-16
updated: 2026-04-16
tags: [research, claude-code, opus-4.7, changelog, effort, adaptive-thinking, multi-model, upgrade]
---

# Research — Claude Code 2.1.94→2.1.111 + Opus 4.7 Launch

## Operator Directive

> "The claude code cli has updated / release a new version but I want to make sure we backup the current version first. openarms and openfleet might fail after an update so we need to make sure a return to the old cli or even a parralel existant with the old version is possible."

> "This also probably mean that we are going to think about how we handle multiple model, we already had a dsicussion on this about backends and models tiers and such... so that things dont break for old version and so that we can even possibly use multiple in parralel so that they all work the way adapted to them. like the notion of context injection and size or type or size of directives and such."

## Current State

- **Current version:** 2.1.94
- **Latest version:** 2.1.111 (stable tag: 2.1.97)
- **Versions between:** 12 (2.1.95, 96, 97, 98, 100, 101, 104, 105, 107, 108, 109, 110, 111)
- **Backup location:** `~/.claude-code-backups/2.1.94/`
- **Parallel run:** `ln -s ~/.claude-code-backups/2.1.94/claude ~/.local/bin/claude-old`

## Claude Opus 4.7 — The Model Generation Shift

### What it IS

New model ID: `claude-opus-4-7`. Most capable GA model. 1M context window, 128K max output tokens. Excels at long-horizon agentic work, knowledge work, vision, and memory tasks.

### Breaking API changes

| Change | Old (4.6) | New (4.7) | Impact |
|---|---|---|---|
| **Extended thinking removed** | `thinking: {type: "enabled", budget_tokens: N}` | Returns 400 error | Any code using budget_tokens BREAKS |
| **Adaptive thinking only** | Extended OR adaptive | Adaptive only, OFF by default | Must set `thinking: {type: "adaptive"}` explicitly |
| **Thinking content omitted** | Included by default | Omitted by default | Products streaming reasoning see a long pause. Set `display: "summarized"` to restore |
| **Sampling params removed** | `temperature`, `top_p`, `top_k` | Returns 400 on non-default | Remove these params entirely |
| **New tokenizer** | Old tokenizer | ~1-1.35x more tokens (up to 35% more) | Update max_tokens, compaction triggers, budgets |

### New features

| Feature | What it does | Impact on ecosystem |
|---|---|---|
| **`xhigh` effort level** | Between high and max. Recommended for coding/agentic | New tier for harness cost optimization |
| **Task budgets (beta)** | Advisory token budget across full agentic loop. Model sees countdown. | Harness can control agent scope without hard cuts |
| **High-res images** | 2576px/3.75MP (was 1568px/1.15MP). 1:1 coordinate mapping | Better for computer use, screenshots |
| **Better memory** | Improved at writing/using file-system-based memory | Scratchpad/notes across turns more reliable |

### Behavior changes (NOT API-breaking but prompt-affecting)

- **More literal instruction following** — won't silently generalize. If you say "fix file A" it won't also fix file B even if B has the same bug
- **Response length calibrates to perceived task complexity** — not fixed verbosity
- **Fewer tool calls by default** — more reasoning. Raising effort increases tool usage
- **More direct, opinionated tone** — less validation-forward, fewer emoji
- **Fewer subagents spawned by default** — steerable through prompting
- **More regular progress updates** during long agentic traces

## Claude Code CLI Changes (2.1.95-2.1.111)

### New commands

| Command | What it does | Version |
|---|---|---|
| `/effort` interactive slider | Opens slider when called without args, includes xhigh | 2.1.111 |
| `/ultrareview` | Comprehensive parallel multi-agent code review | 2.1.111 |
| `/less-permission-prompts` | Scan transcripts, propose permission allowlists | 2.1.111 |
| `/tui` | Flicker-free rendering mode | 2.1.110 |
| `/team-onboarding` | Generate teammate ramp-up guide | 2.1.101 |
| `/proactive` | Alias for `/loop` | 2.1.105 |
| `/undo` | Alias for `/rewind` | 2.1.108 |

### New environment variables

| Variable | Purpose | Version |
|---|---|---|
| `ENABLE_PROMPT_CACHING_1H` | 1-hour prompt cache TTL | 2.1.108 |
| `FORCE_PROMPT_CACHING_5M` | Force 5-minute cache TTL | 2.1.108 |
| `CLAUDE_CODE_USE_POWERSHELL_TOOL` | Opt-in PowerShell tool (Windows) | 2.1.111 |
| `CLAUDE_CODE_PERFORCE_MODE` | Read-only file hints for Perforce | 2.1.98 |
| `CLAUDE_CODE_SCRIPT_CAPS` | Limit session script invocations | 2.1.98 |
| `OTEL_LOG_RAW_API_BODIES` | Debug API bodies | 2.1.111 |

### Key infrastructure changes

- **Default effort changed from medium to HIGH** (2.1.95) — affects cost/quality baseline
- **Auto mode no longer requires `--enable-auto-mode` flag** (2.1.111) — enabled for Max subscribers on 4.7
- **PreCompact hook support with block capability** via exit code 2 (2.1.105) — can now PREVENT compaction
- **Session recap feature** for returning to sessions (2.1.108) — context when resuming
- **Model can discover and invoke built-in slash commands** via Skill tool (2.1.108)
- **Monitor tool** for streaming background script events (2.1.98)
- **Push notifications** for Remote Control (2.1.110)
- **Subagents now inherit dynamic MCP tool servers** (2.1.101 fix) — was broken before
- **Plan files named after prompt** instead of random words (2.1.111)
- **Plugin background monitors** via `monitors` manifest key (2.1.105)
- **MCP tool result persistence override** up to 500K via `_meta` annotation (2.1.111)

### Security fixes (relevant to harness)

- Fixed Bash tool backslash-escaped flag permission bypass (2.1.98)
- Fixed compound Bash commands bypassing forced permission prompts (2.1.98)
- Fixed redirects to `/dev/tcp/...` or `/dev/udp/...` auto-allowing (2.1.98)
- Hardened "Open in editor" against command injection (2.1.110)
- Linux sandbox ships apply-seccomp helper (2.1.111)
- Subprocess sandboxing with PID isolation on Linux (2.1.98)

## Risks for OpenArms / OpenFleet

### HIGH risk

1. **Tokenizer change (+35%)** — OpenArms turnCount thresholds (already buggy at 150/200) will fire even earlier. Cost budgets underestimate by up to 35%. Compaction triggers shift.

2. **Behavior change: fewer tool calls** — harness prompts calibrated for 4.6's tool-calling frequency may produce different execution traces on 4.7. Tasks that relied on specific tool-calling patterns may need prompt adjustment.

3. **Extended thinking removal** — if ANY harness code, skill, or MCP tool uses `budget_tokens`, it fails on 4.7. Must audit before switching model.

### MEDIUM risk

4. **Effort default changed to high** — 2.1.95 changed default from medium to high. OpenArms multi-task runs already cost-sensitive. Higher effort = higher cost per task but better quality.

5. **More literal instruction following** — harness stage skills that rely on the agent inferring additional work (e.g., "run tests" implying "also run lint") may produce less complete results on 4.7.

6. **Fewer subagents** — tasks that benefit from subagent parallelism may run slower or less thoroughly on 4.7. Steerable through prompting but needs prompt update.

### LOW risk

7. **Auto mode change** — auto mode no longer needs flag. Not a problem unless harness explicitly disabled it.

8. **Session recap** — new feature, additive. May add context cost on resume.

## The Multi-Model Architecture Question

### What the operator is pointing at

The upgrade isn't just "update CLI and hope." It's a trigger for thinking about how the ecosystem handles multiple models:

1. **Opus 4.6 and 4.7 coexist** — 4.6 is still available. Some tasks may work better on 4.6 (with extended thinking budgets). Some work better on 4.7 (with task budgets, better memory, adaptive thinking).

2. **Effort levels as a routing dimension** — the existing AICP complexity scorer routes simple/complex tasks. The new effort levels (`low→medium→high→xhigh→max`) add ANOTHER routing dimension: task complexity → model + effort.

3. **Context injection must adapt per model** — 4.7's new tokenizer uses 35% more tokens. A 200-line CLAUDE.md costs 35% more on 4.7. Context budgets (Model — Context Engineering's tier system: expert/capable/lightweight) must account for model-specific token economics.

4. **Harness prompts are model-specific** — 4.7's "more literal" behavior means prompts that worked on 4.6 (with generous inference) may need explicit statements for 4.7. The harness should know which model it's targeting and adjust prompt style.

5. **Backward compatibility** — OpenArms harness-v2 was built for 4.6. A 4.7 upgrade path needs to preserve 4.6 compatibility until prompts are adjusted. Running both in parallel (via the backup) is the safety net.

### The connection to existing wiki knowledge

| Existing model/concept | How multi-model affects it |
|---|---|
| **Model — Context Engineering** (tier system) | Token budgets per tier must be model-specific. 4.7's tokenizer changes the math. |
| **Model — Local AI ($0 Target)** (AICP routing) | The routing stack gains a model dimension: simple→local, moderate→4.6, complex→4.7 |
| **Cost Optimization Stack** (new pattern) | First-order (right-size model) now includes MODEL CHOICE as well as methodology model |
| **Model — Skills, Commands, and Hooks** (extension system) | Skills/hooks may need model-awareness. A 4.6 skill and a 4.7 skill could differ. |
| **Enforcement Hook Patterns** | PreCompact hook can now BLOCK compaction (2.1.105) — new enforcement capability |
| **Harness-Owned Loop** | Harness needs to declare which model it targets and adapt prompt style |

### What the ecosystem should build

1. **Model-aware harness dispatch** — harness declares target model in task frontmatter or at dispatch time. Prompt builder adjusts style per model.

2. **Per-model context budgets** — the Context Engineering tier system (expert: 5-10K, capable: 2-5K, lightweight: 500-1K) needs a model multiplier: `budget × tokenizer_factor`. 4.7 factor: 1.35.

3. **Effort-aware cost model** — the Cost Optimization Stack's first-order savings (right-size methodology model) compounds with effort level selection. For known-pattern tasks: `integration` model + `high` effort. For novel tasks: `feature-development` + `xhigh`. For harness maintenance: `documentation` + `medium`.

4. **Extended thinking → adaptive thinking migration** — audit all harness code for `budget_tokens` references. Replace with `thinking: {type: "adaptive"}` + effort level. Test on 4.7 before switching production.

5. **Task budget integration** — 4.7's task budgets (advisory token cap across agentic loop) could replace or complement the harness's own budget tracking. The harness currently tracks cost externally; task budgets let the MODEL self-moderate internally.

## Sources

- [Claude Code Changelog](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) — full changelog for all versions
- [What's New in Claude Opus 4.7](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-6) — model launch docs
- [Adaptive Thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking) — replaces extended thinking
- [Claude Code Model Config](https://code.claude.com/docs/en/model-config) — effort levels and model settings
- [Claude Code Effort Triggers](https://kentgigger.com/posts/claude-code-thinking-triggers) — ultrathink, /effort guide
- [DEV Community: Claude Code Updates Broke Engineering](https://dev.to/shuicici/claude-codes-feb-mar-2026-updates-quietly-broke-complex-engineering-heres-the-technical-5b4h) — community impact analysis
