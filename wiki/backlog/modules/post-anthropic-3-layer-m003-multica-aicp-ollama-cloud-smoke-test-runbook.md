---
title: "Post-Anthropic 3-Layer Stack M003 — Multica → Claude Code → AICP → Ollama Cloud Smoke-Test Runbook"
aliases:
  - "M003 — 3-Layer Smoke Test"
  - "Multica AICP Ollama Cloud Round-Trip Runbook"
type: module
domain: backlog
status: active
priority: P0
task_type: module
parent_epic: "post-anthropic-stack-3-layer-assembly-multica-aicp-3090"
current_stage: scaffold
readiness: 75
progress: 30
stages_completed:
  - "document"
  - "design"
artifacts:
  - "wiki/backlog/modules/post-anthropic-3-layer-m001-multica-per-agent-provider-config.md"
  - "wiki/sources/tools-integration/src-multica-managed-agents-platform.md"
confidence: high
created: 2026-04-28
updated: 2026-04-28
last_reviewed: 2026-04-28
sources:
  - id: parent-epic
    type: wiki
    file: wiki/backlog/epics/pre-milestone/post-anthropic-stack-3-layer-assembly-multica-aicp-3090.md
    description: "Parent epic — this module is the operator-actionable smoke-test that validates 3-layer composability empirically"
  - id: m001
    type: wiki
    file: wiki/backlog/modules/post-anthropic-3-layer-m001-multica-per-agent-provider-config.md
    description: "Predecessor module — established the `custom_env` mechanism this runbook exercises"
  - id: aicp-handoff
    type: external
    file: ~/devops-expert-local-ai/docs/SESSION-2026-04-24-HANDOFF.md
    description: "AICP authoritative state — `local`, `k2_6_local`, `k2_6_openrouter`, `ollama_cloud` backends wired"
tags: [module, p0, smoke-test, runbook, multica, aicp, ollama-cloud, claude-code, opencode, 3-layer-validation, operator-actionable, pre-4090, mission-2026-04-28, m003]
---

# M003 — Multica → Harness → AICP → Ollama Cloud Smoke-Test Runbook

## Summary

Operator-actionable runbook for empirically validating the post-Anthropic 3-layer stack composability documented in [M001](post-anthropic-3-layer-m001-multica-per-agent-provider-config.md) and the parent [epic](../epics/pre-milestone/post-anthropic-stack-3-layer-assembly-multica-aicp-3090.md). The runbook walks through pre-flight checks, the round-trip smoke test (Multica orchestrates Claude Code → Claude Code talks to AICP → AICP routes to Ollama Cloud → result observed in Multica's activity timeline), expected outputs at each step, and failure-mode diagnostics. **Executable on operator's existing hardware now (no 4090 dependency)** — this runbook predates the local-Ollama tier (M004, post-4090). Two test variants documented: **Variant A** (full 3-layer through AICP routing) and **Variant B** (2-layer direct, Multica → Claude Code → Ollama Cloud, bypassing AICP). Both should pass independently before claiming 3-layer composability empirically validated.

## Pre-flight Checks (verify before running smoke test)

> [!info] Run these first — each should succeed before proceeding to the smoke test

| Check | Command / UI step | Expected result |
|---|---|---|
| Multica daemon running | `multica daemon status` | "Daemon is running" or equivalent |
| Multica self-host server up | `curl -fsS http://localhost:<multica-port>/api/health` (or check operator's web UI) | 200 OK |
| AICP backend reachable | `curl -fsS http://localhost:<aicp-port>/v1/models` | JSON list of available models |
| AICP `ollama_cloud` backend enabled | `aicp --check` (or AICP's status command) | `[OK] ollama_cloud: OK` |
| Ollama Cloud authentication active | `ollama whoami` (operator's existing login) | shows operator's account |
| Claude Code installed and detectable by Multica | Multica UI Settings → Runtimes → operator's machine shows `claude` in detected CLIs | Listed |

If any check fails, fix it before running the smoke test — the smoke test diagnoses the round-trip, not the components themselves.

## Variant A — Full 3-Layer Round-Trip (Multica → Claude Code → AICP → Ollama Cloud)

### Step A1: Create the test agent in Multica

> [!tip] Multica UI: Settings → Agents → New Agent
>
> | Field | Value |
> |---|---|
> | Name | `smoke-test-3-layer` |
> | Provider | `Claude Code` |
> | Runtime | (operator's machine) |
> | Custom Env | `ANTHROPIC_BASE_URL=http://localhost:<aicp-port>`<br>`ANTHROPIC_API_KEY=<aicp-token-if-required>` |
> | Custom Args | (none) |
> | Instructions | `You are a test agent. Respond concisely.` |
> | Skills | (none for the smoke test) |

### Step A2: Configure AICP to prefer `ollama_cloud` for this test

> [!tip] AICP-side configuration
>
> Either:
> - **Force routing to `ollama_cloud`** for this test by adjusting AICP's complexity-tier mapping (or temporarily disabling other backends in `default.yaml`), OR
> - **Use AICP's natural routing** if the smoke-test prompt's complexity score routes to `ollama_cloud` by default
>
> The simpler test path: temporarily set `ollama_cloud` as the only enabled backend in AICP for the duration of the test.

### Step A3: Create and assign a smoke-test issue

> [!tip] Multica UI: New Issue
>
> | Field | Value |
> |---|---|
> | Title | `3-layer smoke test 2026-04-28` |
> | Description | `Reply with one sentence confirming you can hear me. Tell me which provider answered.` |
> | Assignee | `smoke-test-3-layer` (the agent created in A1) |

### Step A4: Watch the activity timeline

> [!success] Expected behavior
>
> - Multica's daemon spawns `claude` with the configured `custom_env`
> - Claude Code talks to `ANTHROPIC_BASE_URL=http://localhost:<aicp-port>` (= AICP)
> - AICP routes the request to `ollama_cloud` backend
> - Ollama Cloud's hosted model responds
> - Response flows back: Ollama Cloud → AICP → Claude Code → Multica activity timeline
> - Operator sees a comment from `smoke-test-3-layer` in the issue's timeline within seconds

### Step A5: Verify each layer's role with logs/observability

> [!info] Where to confirm each layer participated
>
> | Layer | Confirmation source |
> |---|---|
> | Multica daemon spawned `claude` | Multica's daemon logs (likely `/home/jfortin/.multica/server/logs/` or via `multica daemon logs`) |
> | Claude Code received request, hit AICP | Claude Code's own logs (terminal output if foreground, or wherever Multica captured stderr/stdout) |
> | AICP received request, routed to `ollama_cloud` | AICP's request logs (per `aicp routing-report` if implemented, or AICP's stderr) |
> | Ollama Cloud answered | AICP's response logs + Ollama Cloud's web dashboard usage stats |

If all four confirmations align: **Variant A passes — 3-layer composability empirically validated.**

## Variant B — 2-Layer Direct (Multica → Claude Code → Ollama Cloud, bypass AICP)

### Step B1: Create a second test agent

> [!tip] Multica UI: Settings → Agents → New Agent
>
> | Field | Value |
> |---|---|
> | Name | `smoke-test-direct-ollama-cloud` |
> | Provider | `Claude Code` |
> | Custom Env | `ANTHROPIC_BASE_URL=<ollama-cloud-anthropic-compat-endpoint>`<br>`ANTHROPIC_API_KEY=<ollama-cloud-token>` |

The exact Ollama Cloud Anthropic-compat URL: **operator may extract from `ollama launch claude` behavior** — when `ollama launch claude --model kimi-k2.6:cloud` runs, it sets `ANTHROPIC_BASE_URL` for the spawned shell. Inspect the launched env (e.g., `ollama launch claude --model kimi-k2.6:cloud --print-env` if such flag exists, OR check Ollama's docs for the cloud Anthropic-compat URL pattern).

### Step B2: Smoke-test issue + assign + observe

Same as A3-A5, but with the new agent. Expected: response comes back faster (one fewer hop) but routes through Ollama Cloud directly without AICP's complexity scoring.

If Variant B passes: **2-layer Multica + Ollama Cloud composability validated as the simpler fallback path.**

## Diagnostics — common failure modes

> [!warning] What to check when the smoke test fails

| Symptom | Likely cause | Diagnostic |
|---|---|---|
| Agent never spawns | Multica daemon not running OR `claude` not on daemon's PATH | `multica daemon status`; check daemon's environment for PATH coverage |
| Agent spawns but Claude Code uses default Anthropic endpoint | `custom_env` not propagating | Check Multica's daemon log for the spawn command's env; verify `custom_env` field saved correctly in Multica UI |
| Claude Code reaches AICP but AICP returns error | AICP not running OR `ollama_cloud` backend unhealthy | `aicp --check`; check AICP logs |
| Request reaches AICP but routed to wrong backend | AICP complexity scorer routes elsewhere | Force `ollama_cloud` via temporary backend-disable, OR adjust AICP `tier_map` |
| Ollama Cloud returns 503 / timeout | Known Ollama Cloud reliability issue (per [GitHub #15453](https://github.com/ollama/ollama/issues/15453)) | Re-try; OR fail over to `k2_6_openrouter` backend in AICP |
| Multica timeline shows agent crashed | Harness-side error (Claude Code rejected the env / API key invalid / etc.) | Check Multica daemon log + Claude Code stderr capture |

## Tasks

| Task | Description | Status |
|---|---|---|
| T-M003-1 | Document Variant A (full 3-layer through AICP) | ✅ Done in this module |
| T-M003-2 | Document Variant B (2-layer direct to Ollama Cloud) | ✅ Done in this module |
| T-M003-3 | Document pre-flight checks | ✅ Done in this module |
| T-M003-4 | Document failure-mode diagnostics | ✅ Done in this module |
| T-M003-5 | Operator runs Variant A smoke test | ⊙ Pending operator |
| T-M003-6 | Operator runs Variant B smoke test | ⊙ Pending operator |
| T-M003-7 | Operator captures the actual Ollama Cloud Anthropic-compat URL pattern | ⊙ Pending operator (extract from `ollama launch claude` behavior) |
| T-M003-8 | Operator captures AICP's local endpoint URL pattern | ⊙ Pending operator (verify against AICP's current `local` mode state) |
| T-M003-9 | If both variants pass, add the captured URLs back to M001 / this module for future reference | ⊙ Pending |
| T-M003-10 | If either variant fails, document the failure mode + workaround | ⊙ Pending |

## Done When

- [ ] Variant A passes: round-trip Multica → Claude Code → AICP → Ollama Cloud → Multica timeline observed
- [ ] Variant B passes: round-trip Multica → Claude Code → Ollama Cloud (direct) → Multica timeline observed
- [ ] Concrete Ollama Cloud Anthropic-compat URL captured + documented (resolves M001 open question)
- [ ] Concrete AICP local endpoint URL captured + documented
- [ ] At least one failure mode + workaround tested (resilience smoke test partial — full resilience smoke is M005-adjacent)
- [ ] Module marked `current_stage: test` → `done` upon operator validation
- [ ] Findings flow back to: M001 recipes (concrete URLs), epic acceptance criteria (3-layer composability concrete), parent milestone (assembly empirically validated)

## Dependencies

- **Predecessor**: [M001](post-anthropic-3-layer-m001-multica-per-agent-provider-config.md) (`custom_env` mechanism documented + operator-validated)
- **External**: Multica self-hosted at `/home/jfortin/.multica/server/` (operator-confirmed)
- **External**: AICP repo at `~/devops-expert-local-ai/` with backends wired
- **External**: Ollama Cloud subscription active
- **External**: Operator-side time to run the smoke tests (estimated 30-60 minutes for both variants)
- **Hardware**: NOT blocked by RTX 4090 — this runbook works on existing hardware (the local-Ollama tier waits for hardware in M004)

## Why This Matters

This module is **the empirical verification gate** for the parent epic's "3-layer composability achieved" claim. Per [Saturation Lesson](../../lessons/01_drafts/saturation-declarations-are-p4-aspirational-test-by-attempting-forward-work.md) and [Principle 4](../../lessons/04_principles/hypothesis/declarations-are-aspirational-until-infrastructure-verifies-them.md), the architecture documentation is aspirational until operator runs the round-trip and confirms each layer participated. **This runbook IS that verification gate.** Once Variant A passes, the [[anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence|anti-vendor-lock-in lesson Evidence 10]] graduates from "documented" to "operator-validated" — same pattern as the wiki's prior P4 verifications.

## Relationships

- PART OF: [[post-anthropic-stack-3-layer-assembly-multica-aicp-3090|Epic — Post-Anthropic 3-Layer Stack Assembly]]
- BUILDS ON: [[post-anthropic-3-layer-m001-multica-per-agent-provider-config|M001 — Multica Per-Agent Provider Config]]
- BUILDS ON: [[src-multica-managed-agents-platform|Multica Synthesis]]
- BUILDS ON: [[kimi-k2-6-access-paths-openrouter-ollama-cloud-local|K2.6 Access Paths Comparison]] (Variant B is the `ollama launch claude` path)
- DEMONSTRATES: [[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4]] — runbook IS the verification gate for the architecture's claim
- DEMONSTRATES: [[saturation-declarations-are-p4-aspirational-test-by-attempting-forward-work|Saturation Lesson]] — testing the empirical-validation claim by running the smoke test
- FEEDS INTO: [[anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence|Anti-Vendor-Lock-In Lesson]] § Evidence 10 — orchestrator-layer empirical confirmation upgrades from "documented" to "operator-validated"

## Backlinks

[[Epic — Post-Anthropic 3-Layer Stack Assembly]]
[[M001 — Multica Per-Agent Provider Config]]
[[src-multica-managed-agents-platform|Multica Synthesis]]
[[K2.6 Access Paths Comparison]]
[[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4]]
[[Saturation Lesson]]
[[Anti-Vendor-Lock-In Lesson]]
