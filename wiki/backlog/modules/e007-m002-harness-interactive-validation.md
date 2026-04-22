---
title: "E007 M002 — Harness Interactive Validation (Tests 1-5)"
type: module
domain: backlog
status: draft
priority: P0
task_type: module
current_stage: scaffold
readiness: 60
progress: 0
stages_completed: [document, design]
artifacts:
  - wiki/log/2026-04-22-openrouter-k2-6-day-1-setup-procedure.md
  - tools/claude_openrouter.sh
epic: "E007"
depends_on:
  - "E007-m001"
confidence: high
created: 2026-04-22
updated: 2026-04-22
sources:
  - id: e007-openrouter-deadline-de-risk
    type: wiki
    file: wiki/backlog/epics/pre-milestone/E007-openrouter-deadline-de-risk.md
  - id: day-1-setup-procedure
    type: wiki
    file: wiki/log/2026-04-22-openrouter-k2-6-day-1-setup-procedure.md
tags: [module, p0, e007, harness-test, interactive, tool-use, claude-code-cli, openrouter, kimi-k2-6]
---

# E007 M002 — Harness Interactive Validation (Tests 1-5)

## Summary

Execute the 5-test POC plan from the Day 1 setup procedure to prove Claude Code CLI routes through OpenRouter to Kimi K2.6 end-to-end — not just via curl (smoke test, already DONE), but through the full harness: `/status`, tool use, multi-step chains, scaffold + validate, and quality A/B vs Opus. This module is the critical gate that turns "the smoke test passed" into "the deadline is really de-risked."

## Tasks

| Task | Title | Readiness | Progress | Status |
|------|-------|-----------|----------|--------|
| T002 | Run smoke tests (K2.6 + Opus + GPT controls) | 100% | 100% | done |
| T003 | Run Test 1 — harness sanity (`/status` + identity + simple tool use) | 100% | 0% | draft |
| T004 | Run Test 2 — file read + synthesis workload | 100% | 0% | draft |
| T005 | Run Test 3 — multi-step tool chain (Grep → Read → Grep) | 100% | 0% | draft |
| T006 | Run Test 4 — scaffold + pipeline-post validate | 100% | 0% | draft |
| T007 | Run Test 5 — K2.6 vs Opus quality A/B (3 wiki-typical workloads) | 100% | 0% | draft |

## Dependencies

- [[e007-m001-openrouter-access-and-wrapper]] — provides the wrapper script + verified key
- Operator-driven execution in a **fresh terminal** (cannot nest inside current Claude Code session)

## Done When

- [ ] All 5 tests executed end-to-end and results logged in `wiki/log/2026-04-22-openrouter-k2-6-day-1-setup-procedure.md` or a follow-up log dated the execution day
- [ ] Test 1 — `/status` shows OpenRouter endpoint; model self-identifies; simple tool use succeeds (no schema errors)
- [ ] Test 2 — K2.6 reads `wiki/spine/super-model/super-model.md` and reports correct page count + four principles + ten verbs
- [ ] Test 3 — Grep → Read → Grep chain on pattern pages works without tool-schema errors
- [ ] Test 4 — K2.6 scaffolds a pattern page; `python3 -m tools.pipeline post` PASSES on the file
- [ ] Test 5 — at least 3 wiki-typical workloads run via `or-claude` (K2.6) and `or-claude-opus` (Opus 4.6); quality + cost + latency documented side-by-side
- [ ] All child tasks at status: done

## Impediments

| Impediment | Type | Blocked Since | Escalated? | Resolution |
|-----------|------|---------------|-----------|------------|
| Operator needs to open a fresh terminal outside this CC session (can't nest) | environment | 2026-04-22 | no | Operator action: fresh terminal, source .env + wrapper, run `or-claude` |

## Relationships

- PART OF: [[E007-openrouter-deadline-de-risk|E007-openrouter-deadline-de-risk]]

## Backlinks

[[E007-openrouter-deadline-de-risk|E007-openrouter-deadline-de-risk]]
