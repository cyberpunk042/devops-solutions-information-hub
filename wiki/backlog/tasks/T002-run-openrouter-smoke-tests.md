---
title: "T002 — Run OpenRouter Smoke Tests (K2.6 + Opus + GPT-5.4)"
type: task
domain: backlog
status: done
priority: P0
task_type: task
current_stage: test
readiness: 100
progress: 100
stages_completed: [document, design, scaffold, implement, test]
artifacts:
  - tools/claude_openrouter.sh
estimate: XS
epic: "E007"
module: "E007-m002"
depends_on: []
confidence: high
created: 2026-04-22
updated: 2026-04-22
sources:
  - id: e007-m002-harness-interactive-validation
    type: wiki
    file: wiki/backlog/modules/e007-m002-harness-interactive-validation.md
tags: [task, p0, done, e007, smoke-test, openrouter, kimi-k2-6, opus, gpt]
---

# T002 — Run OpenRouter Smoke Tests

## Summary

Validate via curl that OpenRouter's Anthropic-Skin endpoint is reachable, authenticates with the operator's key, and returns well-formed Messages API responses for three target models: Kimi K2.6, Claude Opus 4.6, GPT-5.4. Proves the HTTP path works before attempting interactive harness tests.

## Done When

- [x] `or-claude-smoke moonshotai/kimi-k2.6` returns a `200 OK` with a `message` object containing `content[].type == "thinking"` and `content[].type == "redacted_thinking"` blocks — confirmed 2026-04-22, cost $0.00047, model id returned as `moonshotai/kimi-k2.6-20260420`
- [x] `or-claude-smoke anthropic/claude-opus-4.6` returns a `200 OK` with `"I'm Claude, made by Anthropic"` text content — confirmed 2026-04-22, cost $0.000635, provider = Amazon Bedrock
- [x] `or-claude-smoke openai/gpt-5.4` returns a `200 OK` with `"I'm ChatGPT"` text content — confirmed 2026-04-22, cost $0.00027, provider = OpenAI
- [x] Total smoke-test spend < $0.01 — confirmed ($0.00137 total)

## Relationships

- PART OF: [[E007-openrouter-deadline-de-risk|E007-openrouter-deadline-de-risk]]
- PART OF: [[e007-m002-harness-interactive-validation|e007-m002-harness-interactive-validation]]

## Backlinks

[[E007-openrouter-deadline-de-risk|E007-openrouter-deadline-de-risk]]
[[e007-m002-harness-interactive-validation|e007-m002-harness-interactive-validation]]
