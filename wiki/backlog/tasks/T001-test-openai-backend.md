---
title: "Test OpenAI backend with LocalAI"
type: task
domain: backlog
status: blocked
priority: P1
epic: E001
task_type: task
current_stage: scaffold
readiness: 0
stages_completed: []
artifacts: []
depends_on: []
confidence: high
created: 2026-04-09
updated: 2026-04-09
estimate: M
sources: []
tags: [local-inference, openai-backend, testing, blocked]
---

# Test OpenAI backend with LocalAI

## Summary

Run `pipeline evolve --auto --backend openai --top 1` against a running LocalAI instance. Verify the generated page passes validation. Requires 19GB VRAM hardware.

## Done When

- [ ] LocalAI running with a 30B+ model
- [ ] `pipeline evolve --auto --backend openai --top 1` completes without error
- [ ] Generated page passes `pipeline post` validation
- [ ] Token count and generation time documented
