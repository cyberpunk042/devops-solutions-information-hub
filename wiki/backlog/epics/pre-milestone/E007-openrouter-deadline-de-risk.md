---
title: "E007 — OpenRouter Deadline De-Risk (Claude Code CLI \u2192 K2.6)"
type: epic
domain: backlog
status: in-progress
priority: P0
task_type: epic
current_stage: implement
readiness: 75
progress: 45
stages_completed: [document, design, scaffold]
artifacts:
  - tools/claude_openrouter.sh
  - wiki/log/2026-04-22-openrouter-k2-6-day-1-setup-procedure.md
  - wiki/sources/tools-integration/src-kimi-k2-6-moonshot-agent-swarm.md
confidence: high
created: 2026-04-22
updated: 2026-04-22
sources:
  - id: operator-directive
    type: file
    file: raw/notes/2026-04-22-directive-post-anthropic-self-autonomous-plan.md
  - id: src-kimi-k2-6-synthesis
    type: wiki
    file: wiki/sources/tools-integration/src-kimi-k2-6-moonshot-agent-swarm.md
    title: "Synthesis — Kimi K2.6"
  - id: openrouter-claude-code-docs
    type: api-documentation
    url: https://openrouter.ai/docs/guides/coding-agents/claude-code-integration
    title: "OpenRouter — Claude Code Integration"
    ingested: 2026-04-22
tags: [epic, p0, openrouter, kimi-k2-6, claude-code-cli, harness, subscription-deadline, deadline-2026-04-27, post-anthropic]
---

# E007 — OpenRouter Deadline De-Risk (Claude Code CLI → K2.6)

## Summary

Route the operator's existing Claude Code CLI through OpenRouter's Anthropic-Skin endpoint to Moonshot AI's **Kimi K2.6** as the primary inference backend, so that the 2026-04-27 Claude Code subscription transition is a **non-event** — same harness, different backend, ~6-7× cheaper per token, equal-or-better agentic quality. Proves that the operator's daily workflow continues unchanged even as Anthropic's access terms shift.

## Operator Directive

> "In 5 days everything will most likely be happening on this computer with the 19GB VRAM... we will make this workstation self-autonomous and also integrate the OpenRouter like the rest."

> "I don't want to have to deal with Anthropic and Claude and Opus in the future."

## Goals

- Claude Code CLI (2.1.94) routes cleanly to OpenRouter's Anthropic Skin endpoint via environment variables — zero proxy, zero plugin.
- Kimi K2.6 is the primary inference backend; Opus 4.6 and GPT-5.4 are reachable as one-command fallbacks (`or-claude-opus`, `or-claude-gpt`).
- Interactive harness tool-use works end-to-end (file read, Grep, Edit, multi-step tool chains, scaffold + validate).
- Cost baseline measured after 1 week of real use — ratio vs Anthropic-direct Opus documented.
- Provider pinning strategy documented: which OpenRouter provider to pin K2.6 to when the default routing introduces variance.
- Post-deadline retrospective log entry (2026-04-28) confirming the transition was uneventful.

## Done When

- [ ] `tools/claude_openrouter.sh` exists and passes `bash -n` (DONE 2026-04-22)
- [ ] `or-claude-smoke moonshotai/kimi-k2.6` returns a well-formed Anthropic Messages response with thinking blocks preserved (DONE 2026-04-22, cost $0.00047)
- [ ] `or-claude-smoke anthropic/claude-opus-4.6` and `or-claude-smoke openai/gpt-5.4` controls both return successful responses (DONE 2026-04-22)
- [ ] **Interactive harness test (Test 1)**: operator runs `or-claude` in a fresh terminal; `/status` shows OpenRouter endpoint; model identifies as Kimi/Moonshot; single-turn tool use (ls-equivalent) succeeds
- [ ] **Wiki-typical workload test (Test 2)**: K2.6 reads `wiki/spine/super-model/super-model.md` and reports correct page count + four principles + ten verbs in <200 words
- [ ] **Multi-step tool-chain test (Test 3)**: K2.6 chains Grep → Read → Grep on pattern pages and reports schema compliance; no tool-schema errors
- [ ] **Scaffold + validate test (Test 4)**: K2.6 scaffolds a new draft pattern page; `python3 -m tools.pipeline post` PASSES on the scaffolded file
- [ ] **Quality A/B test (Test 5)**: same prompt sent via `or-claude` (K2.6) and `or-claude-opus` — response quality compared on at least 3 wiki-typical workloads; results logged
- [ ] **Provider pinning documented**: `wiki/log/` entry explains how to pin K2.6 to a specific OpenRouter provider via request parameters, with tested command
- [ ] **Cost baseline report**: after 1 week of real use (~2026-05-03), total spend + average cost-per-workload documented in `wiki/log/`
- [ ] **Post-deadline retrospective**: `wiki/log/2026-04-28-*-subscription-transition-retrospective.md` confirms the transition was a non-event
- [ ] **Fallback path documented**: if OpenRouter becomes unavailable, `wiki/log/` entry documents (a) `claude-code-router` proxy setup, (b) direct Moonshot API setup, (c) OpenCode-based path
- [ ] `python3 -m tools.pipeline post` returns 0 validation errors after all E007 work commits

## Scale and Model

> [!info] Epic Parameters
>
> | Parameter | Value |
> |-----------|-------|
> | **Model** | feature-development |
> | **Quality tier** | Skyscraper (critical-path deadline de-risk) |
> | **Estimated modules** | 4 |
> | **Estimated tasks** | 12-15 |
> | **Dependencies** | OpenRouter account (DONE), Claude Code CLI 2.1.94 honoring env vars |

## Stage Artifacts (per methodology model)

> [!abstract] Stage → Artifact Map
>
> | Stage | Required Artifacts | Location |
> |-------|--------------------|----------|
> | Document | Directive log, K2.6 synthesis, OpenRouter integration research | `raw/notes/`, `wiki/sources/tools-integration/` |
> | Design | Setup procedure + 6-test POC plan + expected pitfalls | `wiki/log/2026-04-22-openrouter-k2-6-day-1-setup-procedure.md` (DONE) |
> | Scaffold | Wrapper script with 6 helper functions | `tools/claude_openrouter.sh` (DONE) |
> | Implement | Env-var config, smoke test, harness validation runs | Shell commands + wiki log entries |
> | Test | 6-test POC results + cost baseline + retrospective | `wiki/log/` entries |

## Module Breakdown

| Module | Delivers | Est. Tasks |
|--------|----------|-----------|
| [[e007-m001-openrouter-access-and-wrapper]] | Account, key, wrapper script with `or-claude` + controls + smoke helper | 4 (3 done) |
| [[e007-m002-harness-interactive-validation]] | 6-test POC executed end-to-end; results logged; quality A/B captured | 6 |
| [[e007-m003-provider-pinning-and-fallbacks]] | Pin K2.6 to specific provider; document fallback paths (claude-code-router, direct Moonshot, OpenCode) | 3 |
| [[e007-m004-cost-baseline-and-retrospective]] | 1-week cost report, post-deadline retrospective, ratio validation | 3 |

## Dependencies

- **OpenRouter availability** (external) — E007 entirely depends on OpenRouter's Anthropic Skin remaining functional and K2.6 staying listed.
- **Claude Code CLI 2.1.94 env-var support** (tool) — if a future CLI update breaks env-var honoring, pivot to `claude-code-router` or OpenCode (escalates E009).
- **E010 M010.1** (64 GB RAM) is *not* a dependency — E007 is cloud-route-only.

## Open Questions

> [!question] Does K2.6's tool-use format round-trip cleanly through OpenRouter's Anthropic Skin for all Claude Code CLI tools (Edit, Write, Grep, Glob, Bash, etc.)?
> Smoke test confirms basic Messages API works. Tests 1-4 under M007.2 resolve this empirically.

> [!question] Which OpenRouter provider should K2.6 be pinned to for quality + latency consistency?
> Default routing may introduce variance. Resolved during M007.3 once we observe first week's behavior.

> [!question] Does K2.6 preserve the "extended thinking" control Claude Code CLI relies on for some deep-reasoning flows?
> Smoke test returned thinking blocks. Tests 1-4 will confirm programmatic controllability.

> [!question] Is there a meaningful quality difference between K2.6 and Opus 4.6 on operator's actual workloads (wiki synthesis, gap analysis, multi-step methodology reasoning)?
> Resolved empirically via M007.2 Test 5 (A/B run) and M007.4 (1-week baseline).

## Relationships

- PART OF: [[post-anthropic-self-autonomous-stack|Milestone: Post-Anthropic Self-Autonomous AI Stack]]
- BUILDS ON: [[src-kimi-k2-6-moonshot-agent-swarm|Synthesis — Kimi K2.6]]

## Backlinks

[[post-anthropic-self-autonomous-stack|Milestone: Post-Anthropic Self-Autonomous AI Stack]]
[[Synthesis — Kimi K2.6]]
