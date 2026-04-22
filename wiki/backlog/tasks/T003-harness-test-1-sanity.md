---
title: "T003 — Harness Test 1: `/status` + Identity + Simple Tool Use"
type: task
domain: backlog
status: draft
priority: P0
task_type: task
current_stage: design
readiness: 100
progress: 0
stages_completed: [document, design]
artifacts: []
estimate: XS
epic: "E007"
module: "E007-m002"
depends_on:
  - "T002"
confidence: high
created: 2026-04-22
updated: 2026-04-22
sources:
  - id: e007-m002-harness-interactive-validation
    type: wiki
    file: wiki/backlog/modules/e007-m002-harness-interactive-validation.md
  - id: day-1-setup-procedure
    type: wiki
    file: wiki/log/2026-04-22-openrouter-k2-6-day-1-setup-procedure.md
tags: [task, p0, e007, harness-test, interactive, claude-code-cli, tool-use]
---

# T003 — Harness Test 1: `/status` + Identity + Simple Tool Use

## Summary

First interactive harness test. In a fresh terminal (NOT nested inside another Claude Code session), launch `or-claude` and verify (a) `/status` shows the OpenRouter endpoint, (b) the model self-identifies as Kimi/Moonshot when asked, (c) a single tool call (ls-equivalent) executes without schema errors.

## Done When

- [ ] `or-claude-status` printed inside a fresh Bash terminal shows `ANTHROPIC_BASE_URL = https://openrouter.ai/api`
- [ ] `or-claude` launched successfully (interactive prompt appears)
- [ ] `/status` inside the CC session shows the OpenRouter endpoint as the base URL
- [ ] Asked "Identify yourself: what model are you, and what provider are you routed through?" — response includes "Kimi" or "Moonshot" (not "Claude")
- [ ] Asked "List the files in the current directory." — tool call (Bash `ls` or equivalent) executes and returns directory contents, no `invalid_tool_schema` or `model_not_found` errors
- [ ] Results pasted into `wiki/log/2026-04-22-openrouter-k2-6-day-1-setup-procedure.md` "POC results" section (operator-driven)

## Procedure (operator runs in fresh terminal)

```bash
cd /home/jfortin/devops-solutions-research-wiki
set -a; source /home/jfortin/devops-expert-local-ai/.env; set +a
source tools/claude_openrouter.sh
or-claude-status
or-claude
# Inside CC session:
# /status
# Prompt: "Identify yourself: what model are you, and what provider are you routed through?"
# Prompt: "List the files in the current directory."
# /exit
```

## Rollback

If the session fails to launch or authentication errors surface, run `or-claude-clear` and verify native Claude Code still works (`claude --version`). See the "Expected Pitfalls" table in the Day 1 setup procedure for known issues.

## Relationships

- PART OF: [[e007-m002-harness-interactive-validation|e007-m002-harness-interactive-validation]]
- PART OF: [[E007-openrouter-deadline-de-risk|E007-openrouter-deadline-de-risk]]
- DEPENDS ON: [[T002-run-openrouter-smoke-tests|T002-run-openrouter-smoke-tests]]

## Backlinks

[[e007-m002-harness-interactive-validation|e007-m002-harness-interactive-validation]]
[[E007-openrouter-deadline-de-risk|E007-openrouter-deadline-de-risk]]
[[T002-run-openrouter-smoke-tests|T002-run-openrouter-smoke-tests]]
