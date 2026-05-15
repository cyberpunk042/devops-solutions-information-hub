---
title: "T078 — Author spawn-protocol-generic-agent-sdk (the first runtime spawn protocol; foundation for OpenClaw/OpenArms/Hermess variants)"
type: task
domain: backlog
status: draft
priority: P1
task_type: task
current_stage: document
readiness: 25
progress: 0
stages_completed: []
artifacts: []
estimate: M
epic: "E024"
module: "E024-M004"
depends_on:
  - T071                                  # needs schema first
confidence: high
created: 2026-05-09
updated: "2026-05-09"
sources:
  - id: parent-epic
    type: wiki
    file: wiki/backlog/epics/milestone-v2/e024-per-project-assistant-configurations-to-capture-programmatic-credit-and-enable-ecosystem-spawn.md
    description: "Parent Epic E024 — M004 spawn protocols"
  - id: anthropic-policy
    type: wiki
    file: wiki/sources/ai-models/src-anthropic-programmatic-credit-pool-policy-change-2026-06-15.md
    description: "Anthropic Programmatic Credit Pool — `claude -p` CLI is one valid Agent SDK consumer + drives credit consumption"
tags: [task, "T078", spawn-protocol, generic-agent-sdk, runtime-binding, "2026-05-09", "draft"]
---

# T078 — Author spawn-protocol-generic-agent-sdk

## Summary

Author the first spawn protocol — for the generic Claude Agent SDK runtime (including `claude -p` CLI, GitHub Actions, and any SDK-compatible third-party app per Anthropic's 2026-06-15 credit pool definition). The protocol documents how a Per-Project Assistant Profile is consumed to instantiate a running assistant on this runtime: read Profile → render system prompt + tool list → invoke Agent SDK with composed args. Once this is operable, the /opt Profile (T075) can be spawned for the first time — closing the loop from Profile → Assistant. Subsequent spawn protocols (OpenClaw, OpenArms, Hermess) follow this template.

## Done When

- [ ] `wiki/patterns/01_drafts/spawn-protocol-generic-agent-sdk.md` exists with the full protocol
- [ ] Protocol explicitly maps each of the 6 Profile sections to its Agent SDK consumption point:
  - Identity → SDK agent name/version
  - Knowledge Scope → tool list + MCP server registration
  - Action Surface → allowed/forbidden tool list enforcement
  - Model Routing → SDK model selection logic
  - Prompt Templates → system prompt + recovery prompts
  - Success Criteria → telemetry hooks
- [ ] Protocol covers the `claude -p` CLI variant explicitly (consumes Anthropic programmatic credit pool per 2026-06-15)
- [ ] Protocol includes a runnable example invoking the /opt profile (T075 prerequisite)
- [ ] `.venv/bin/python -m tools.pipeline post` returns 0 errors

## Relationships

- PART OF: [[E024-M004 — Spawn Protocols per Runtime]]
- DEPENDS ON: [[T071-author-per-project-assistant-profile-schema-formal-definition|T071 — Profile Schema]]
- IMPLEMENTS: [[per-project-assistant-profile-pattern-tailored-config-to-spawn-ecosystem-runtimes|Pattern — Per-Project Assistant Profile]] (the spawn protocol bridge layer)
- RELATES TO: [[src-anthropic-programmatic-credit-pool-policy-change-2026-06-15|Anthropic Programmatic Credit Pool Policy Synthesis]] — `claude -p` variant consumes the new credit

## Backlinks

[[E024-M004 — Spawn Protocols per Runtime]]
[[T071 — Profile Schema]]
[[Pattern — Per-Project Assistant Profile]]
[[Anthropic Programmatic Credit Pool Policy Synthesis]]
