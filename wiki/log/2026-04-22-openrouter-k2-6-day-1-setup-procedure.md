---
title: "Day 1 — OpenRouter + Kimi K2.6 via Claude Code CLI (Setup + POC Procedure)"
type: note
layer: 0
domain: ai-models
status: draft
confidence: medium
maturity: seed
created: 2026-04-22
updated: 2026-04-22
sources:
  - id: src-kimi-k2-6-moonshot-agent-swarm
    type: wiki
    file: wiki/sources/tools-integration/src-kimi-k2-6-moonshot-agent-swarm.md
    title: "Synthesis — Kimi K2.6"
  - id: openrouter-claude-code-docs
    type: api-documentation
    url: https://openrouter.ai/docs/guides/coding-agents/claude-code-integration
    title: "OpenRouter — Claude Code Integration"
    ingested: 2026-04-22
tags: [log, openrouter, kimi-k2-6, claude-code, harness, self-autonomous, 5-day-plan, poc, procedure]
---

# Day 1 — OpenRouter + Kimi K2.6 via Claude Code CLI

## Summary

Procedure + POC test plan for routing Claude Code CLI through OpenRouter's Anthropic Skin to Kimi K2.6, executed on 2026-04-22 as Day 1 of the 5-day self-autonomous-workstation plan. Confirms the `ANTHROPIC_BASE_URL` + `ANTHROPIC_AUTH_TOKEN` + empty `ANTHROPIC_API_KEY` env-var setup, documents the `moonshotai/kimi-k2.6` model-id format, stages a reusable wrapper script ([tools/claude_openrouter.sh](tools/claude_openrouter.sh)) with `or-claude` / `or-claude-smoke` / `or-claude-opus` / `or-claude-gpt` helpers, and specifies a 6-test POC (smoke → harness sanity → three wiki-typical workloads → optional quality A/B). Pending: operator's OpenRouter API key and test execution in a non-nested shell. Outcome-gate: if all tests pass, the Claude Code subscription deadline (2026-04-27) is de-risked and the harness stays unchanged. If multi-step tool-use breaks, fall back to OpenCode or `claude-code-router` proxy.

## Purpose

De-risk operator's **2026-04-27 Claude Code subscription transition** by validating that the existing Claude Code CLI harness can route through OpenRouter to Kimi K2.6 *before* the deadline lands. If this works, the harness stays, the backend changes, and the week's plan becomes "optimize" rather than "survive."

## Context

- Operator plan: 5 days (2026-04-22 → 2026-04-27) to make workstation self-autonomous.
- [[src-kimi-k2-6-moonshot-agent-swarm|Kimi K2.6]] released 2026-04-20; leads Opus 4.6 on agentic benchmarks; OpenRouter pricing ~1/20th of Opus.
- OpenRouter exposes an **Anthropic Skin** endpoint (`https://openrouter.ai/api`) that speaks Claude Code's native protocol. No proxy required.
- Claude Code CLI version 2.1.94 on operator's workstation (WSL2, Bash).

## Authoritative Setup (verified 2026-04-22 from OpenRouter docs)

### Environment variables

| Variable | Value | Notes |
|---|---|---|
| `ANTHROPIC_BASE_URL` | `https://openrouter.ai/api` | **NO `/v1` suffix.** Anthropic Skin endpoint. |
| `ANTHROPIC_AUTH_TOKEN` | `<openrouter-api-key>` | Preferred over `ANTHROPIC_API_KEY` for third-party providers. |
| `ANTHROPIC_API_KEY` | `""` (empty string) | **Must be explicitly empty** to prevent Claude Code native-auth collision. |
| `ANTHROPIC_DEFAULT_OPUS_MODEL` | `moonshotai/kimi-k2.6` | Routes Claude Code's "Opus-tier" requests to K2.6. |
| `ANTHROPIC_DEFAULT_SONNET_MODEL` | `moonshotai/kimi-k2.6` | Same model for Sonnet-tier to avoid mixed routing during POC. |
| `CLAUDE_CODE_SUBAGENT_MODEL` | `moonshotai/kimi-k2.6` | Sub-agents use K2.6 too. |
| `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` | `1` | Disable telemetry (no native Anthropic dependency). |

### Wrapper script

Committed at [tools/claude_openrouter.sh](tools/claude_openrouter.sh). Sourced from Bash; provides `or-claude`, `or-claude-opus`, `or-claude-gpt`, `or-claude-smoke`, `or-claude-status`, `or-claude-clear` functions.

**Source the script once per session** (or add to `~/.bashrc` if operator wants persistent):

```bash
export OPENROUTER_API_KEY="sk-or-v1-<your-key>"
source /home/jfortin/devops-solutions-research-wiki/tools/claude_openrouter.sh
```

## POC Test Plan

Run each test in a **separate terminal from this current Claude Code session** to avoid nested-harness confusion.

### Test 0 — Smoke test (HTTP only, no harness)

```bash
export OPENROUTER_API_KEY="sk-or-v1-<your-key>"
source /home/jfortin/devops-solutions-research-wiki/tools/claude_openrouter.sh
or-claude-smoke
or-claude-smoke anthropic/claude-opus-4.6   # control
or-claude-smoke openai/gpt-5.4              # control
```

**Pass criteria**: All three return a well-formed Anthropic Messages API response with the model's self-identification text. If K2.6 works but Opus/GPT don't, the issue is model-id formatting. If none work, the issue is auth or endpoint.

### Test 1 — Harness interactive sanity

```bash
or-claude
# In Claude Code session:
/status
# Ask: "Identify yourself: what model are you, and what provider are you routed through?"
# Ask: "List the files in the current directory."   (tool-use check)
```

**Pass criteria**: `/status` shows the OpenRouter endpoint. Model identifies as K2.6 or Moonshot. `ls`-equivalent tool call executes without schema errors.

### Test 2 — Wiki-typical workload A (file read + synthesis)

Prompt in Claude Code session (after `or-claude`):

> Read `wiki/spine/super-model/super-model.md` and report (a) current page count and relationship count from the metrics row, (b) the four guiding principles, (c) the ten knowledge-project verbs. Keep the response under 200 words.

**Pass criteria**: File read succeeds via tool call. Response contains accurate page/relationship count (392/2571 as of 2026-04-22), the four principles, and the ten verbs.

### Test 3 — Wiki-typical workload B (multi-step tool use)

> Use Grep to find all files in `wiki/patterns/03_validated/` that mention "three lines of defense". Then Read the first matching file's frontmatter and report the maturity and confidence values. Finally report whether the page uses the schema-compliant `## When To Apply` or the non-compliant `## When to apply` variant.

**Pass criteria**: Grep → Read → Grep chain executes without tool-schema errors. Correct frontmatter values extracted. Correct schema compliance detected.

### Test 4 — Wiki-typical workload C (scaffold + validate)

> Scaffold a new draft pattern page titled "OpenRouter as Harness-Neutral Backend" at `wiki/patterns/01_drafts/openrouter-as-harness-neutral-backend.md`. Include placeholder sections: Summary, When To Apply, When Not To, Mechanism, Instances, Anti-Patterns, Relationships. Match the existing pattern schema exactly. Then run `python3 -m tools.pipeline post` and report any validation errors.

**Pass criteria**: File created with correct frontmatter. Pipeline post runs. Validation passes or reports accurate errors.

### Test 5 — Quality A/B vs Claude (optional, if time allows)

Same prompt sent to `or-claude` (K2.6) and `or-claude-opus` (Opus 4.6). Compare:
- Latency to first token
- Latency to completion
- Response quality (subjective)
- Tool-use fidelity (any schema mismatches?)
- Token count (OpenRouter activity dashboard)

**Pass criteria**: K2.6 response is comparable in quality for wiki workloads; cost is ~5% of Opus; tool use equivalent.

## Expected Pitfalls (pre-known, with mitigations)

| Pitfall | Symptom | Mitigation |
|---|---|---|
| `/v1` suffix in base URL | `model_not_found` errors | Use `https://openrouter.ai/api` exactly, no suffix |
| `ANTHROPIC_API_KEY` not empty | Interactive auth loop on startup | Must set to `""` explicitly, not unset |
| Cached Anthropic OAuth credentials interfering | Session uses native Anthropic instead of OpenRouter | Run `/logout` in a native Claude Code first, or clear `~/.claude/.credentials.json` (backup first) |
| Model ID typo | `invalid_model_id` error | OpenRouter format is `moonshotai/kimi-k2.6` (lowercase, dot, hyphen-6) |
| Tool-use schema mismatch | Claude Code tool calls fail | OpenRouter's Anthropic Skin handles translation; if this fails, test with a simpler prompt first. Document the exact failing call in this log. |
| 2.1.94 CLI lacks env-var support | env vars ignored | Verify via `or-claude-status` after start; if env vars not honored, upgrade CLI first |

## Decision Gate (end of Day 1)

After completing Tests 0–4:

- **✅ All pass**: proceed to Day 2 as planned. Subscription deadline is effectively de-risked.
- **⚠️ Tests 0–1 pass, Tests 2–4 fail**: OpenRouter reaches the model but tool-use or multi-step chains break. Options: (a) claude-code-router proxy for custom translation, (b) OpenCode as alternate harness, (c) pin to a specific OpenRouter provider, (d) direct Moonshot API.
- **❌ Test 0 fails**: OpenRouter account / key / endpoint problem. Fix auth before proceeding.

## Cost tracking

OpenRouter activity dashboard: <https://openrouter.ai/activity>. Budget: **$20 initial** (covers ~6M K2.6 input tokens or ~1.4M K2.6 output tokens). Expected Day-1 test burn: **< $1** total.

## Cross-References

- Synthesis: [[src-kimi-k2-6-moonshot-agent-swarm]]
- Strategic context: [[2026-consumer-hardware-ai-stack]] — K2.6 Addendum (2026-04-22)
- Routing model: [[model-local-ai]] — K2.6 dual-slot section (2026-04-22)
- Custom model strategy reshape: [[second-brain-custom-model-strategy]] — Addendum
- Directive: `raw/notes/2026-04-22-directive-kimi-k2-6-ingest.md`

## Next Log Entry

Once operator has OpenRouter API key + test results, a **follow-up log entry** will document:
- Actual latency / tok/s / cost measurements
- Which tests passed/failed and why
- Quality A/B observations
- Decision on proceeding to Day 2 or pivoting to OpenCode / claude-code-router / direct Moonshot API
