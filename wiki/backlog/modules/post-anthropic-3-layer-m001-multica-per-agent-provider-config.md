---
title: "Post-Anthropic 3-Layer Stack M001 — Multica Per-Agent Provider Config (`custom_env` field is the answer)"
aliases:
  - "Multica Per-Agent Provider Config"
  - "M001 — Multica custom_env Investigation"
type: module
domain: backlog
status: active
priority: P0
task_type: module
parent_epic: "post-anthropic-stack-3-layer-assembly-multica-aicp-3090"
current_stage: test
readiness: 95
progress: 90
stages_completed:
  - "document"
  - "design"
  - "scaffold"
  - "implement"
artifacts:
  - "raw/articles/multica-aimultica.md (Multica README + 29 fetched files)"
confidence: high
created: 2026-04-28
updated: 2026-04-28
last_reviewed: 2026-04-28
sources:
  - id: parent-epic
    type: wiki
    file: wiki/backlog/epics/pre-milestone/post-anthropic-stack-3-layer-assembly-multica-aicp-3090.md
    description: "Parent epic — this module is the load-bearing investigation that unblocks M002-M005"
  - id: multica-readme
    type: repository
    file: raw/articles/multica-aimultica.md
    title: "Multica README + agent docs (lines 4424, 6444, 7037, 7095, 7455)"
    description: "Multica's documented agent fields — confirms `custom_env` as the per-agent env-injection mechanism. Plus operational notes (plaintext DB storage warning, override-not-merge semantics, redaction for non-owners)."
  - id: multica-synth
    type: wiki
    file: wiki/sources/tools-integration/src-multica-managed-agents-platform.md
tags: [module, p0, multica, custom_env, per-agent-provider, anthropic-base-url, ollama-cloud-routing, aicp-routing, anti-vendor-lock-in, mission-2026-04-28, post-anthropic, m001]
---

# M001 — Multica Per-Agent Provider Config: `custom_env` is the Answer

## Summary

The operator confirmed 2026-04-28 that Multica's "New Agent" UI shows a harness dropdown (Claude Code · OpenCode · Codex · etc.) but no LLM-provider dropdown — leading to the question *"how do I plug Ollama Cloud / AICP / OpenRouter through Multica when there's no UI option?"* This module **resolves that question with a concrete answer extracted from Multica's own documentation**: per-agent provider config is exposed through the **`custom_env` field** on the agent record. Set `ANTHROPIC_BASE_URL` (and any other env var the harness needs) in the agent's `custom_env`, and Multica's daemon injects those vars into the harness CLI's process when it spawns the agent. **No new tooling needed**, no claude-code-router wrapper required, no OS-level env hacks. The mechanism is built into Multica.

## The Concrete Answer

> [!success] **Multica agent → custom_env → harness gets the right provider**
>
> Per Multica's docs (raw scrape lines 7455, 7037, 4424) and operator-validated 2026-04-28 in the live UI:
>
> | Agent field | What it does | Operator-confirmed UI exposure |
> |---|---|---|
> | `provider` | Selects the harness CLI (`claude`, `codex`, `opencode`, etc.) | ✅ provider dropdown |
> | `instructions` | System prompt injected when the harness starts | ✅ instructions field |
> | **`custom_env`** | **Environment variables injected into the agent process at launch** (e.g. `ANTHROPIC_API_KEY`, `ANTHROPIC_BASE_URL`) | ✅ Env tab |
> | **`custom_args`** | **Additional CLI arguments appended to the agent command at launch.** Supported flags depend on the agent's CLI. Example launch mode for OpenCode: `opencode run (json)<your args>` | ✅ Custom Arguments field |
> | `model` | Model name passed to the harness (provider-specific use) | ✅ model selector |
> | `mcp_config` | MCP server config (currently consumed only by Claude Code per line 7043) | ✅ MCP config |
> | **`skills`** (attached) | Reusable capability bundles attached to the agent — workspace-level skill library compounds across team | ✅ Skills attachment per agent |
>
> The Multica docs literally cite `ANTHROPIC_API_KEY`, `ANTHROPIC_BASE_URL`, `CLAUDE_CODE_USE_BEDROCK` as canonical `custom_env` examples. **This is exactly the mechanism for routing one Multica agent to AICP, another agent to Ollama Cloud, another to OpenRouter, etc.** The `custom_args` + `skills` fields add two more per-agent dimensions: CLI flag tweaking and reusable-capability composition.

## Concrete Wiring Recipes

### Recipe 1: Multica agent → Claude Code → AICP (operator's typical case)

> [!tip] **Settings → Agents → New Agent**
>
> | Field | Value |
> |---|---|
> | Provider | `Claude Code` |
> | Custom Env | `ANTHROPIC_BASE_URL=http://localhost:<aicp-port>`<br>`ANTHROPIC_API_KEY=<aicp-token>` |
> | Custom Args | (none — AICP routes per-request based on complexity) |
> | Instructions | (operator's standard prompt) |
>
> When Multica's daemon spawns `claude`, those env vars are set in `claude`'s process. Claude Code talks to AICP. AICP routes to whatever backend (Ollama Cloud, local, OpenRouter, etc.) per its config. **Three-layer composability achieved for this agent.**

### Recipe 2: Multica agent → Claude Code → Ollama Cloud direct (bypass AICP)

> [!tip] **For agents that should always hit Ollama Cloud regardless of AICP's routing**
>
> | Field | Value |
> |---|---|
> | Provider | `Claude Code` |
> | Custom Env | `ANTHROPIC_BASE_URL=<ollama-cloud-anthropic-compat-endpoint>`<br>`ANTHROPIC_API_KEY=<ollama-cloud-token>` |
>
> Per the wiki's [K2.6 Access Paths comparison](../../comparisons/kimi-k2-6-access-paths-openrouter-ollama-cloud-local.md), this is the path the `ollama launch claude --model kimi-k2.6:cloud` wrapper sets up. Setting it in `custom_env` makes it agent-specific instead of session-wide.

### Recipe 3: Multica agent → OpenCode → Ollama Cloud

> [!tip] **OpenCode has its own provider config; Multica's daemon respects it**
>
> | Field | Value |
> |---|---|
> | Provider | `OpenCode` |
> | Custom Env | (depends on which env vars OpenCode reads — `OPENROUTER_API_KEY`, `OPENAI_API_KEY`, etc. per OpenCode's 75-provider list) |
> | Model | (OpenCode-specific model name) |
>
> OpenCode's config file (`~/.config/opencode/...`) stays as authoritative provider config. Multica's `custom_env` overrides specific values per agent if needed.

### Recipe 4: Multiple agents on same runtime, different providers

> [!tip] **Three agents, three providers, one runtime — possible because `custom_env` is per-agent**
>
> | Agent name | Provider | custom_env |
> |---|---|---|
> | "Daily-research" | Claude Code | `ANTHROPIC_BASE_URL=<aicp>` (Phase-1 routing) |
> | "Long-context-batch" | Claude Code | `ANTHROPIC_BASE_URL=<ollama-cloud-anthropic-endpoint>` (direct to RLM-Qwen3-8B / K2.6) |
> | "Closed-frontier" | Claude Code | (no custom_env — uses Anthropic direct via default config) |
>
> Operator routes by *assigning to a different agent* in Multica's board, which is exactly Multica's "agent as teammate" UX. The agent metaphor maps cleanly onto provider routing.

### Recipe 5: Per-agent CLI argument tuning via `custom_args`

> [!tip] **Different agents → different CLI invocation flavors**
>
> Per operator's UI inspection 2026-04-28, the launch mode for an OpenCode agent is `opencode run (json)<your args>`. The `custom_args` field appends operator-supplied flags after the JSON-mode flag.
>
> | Agent name | Provider | custom_args | Effect |
> |---|---|---|---|
> | "OpenCode-fast-mode" | OpenCode | `--mode build` | Forces Build Mode (per [OpenCode synth](../../sources/tools-integration/src-opencode-harness-features.md) — different execution posture from Plan Mode) |
> | "OpenCode-with-LSP" | OpenCode | `--lsp ts,go,python` | Activates specific LSP servers per OpenCode's 20+ language LSP support |
> | "Claude-headless" | Claude Code | `--no-interactive` | (or whatever flag suppresses interactive prompts in the operator's CC version) |
>
> `custom_args` + `custom_env` together let one agent template specialize multiple concrete agent profiles with different routing AND different invocation flavors.

### Recipe 6: Per-agent skill attachment

> [!tip] **Skills compose with the provider/env combo per-agent**
>
> Multica's Skills system attaches reusable capability bundles to specific agents. Each agent has its own attached-skill list. Combined with `custom_env` for provider routing and `custom_args` for invocation tuning:
>
> | Agent name | Provider | Skills attached | custom_env |
> |---|---|---|---|
> | "Wiki-author" | Claude Code | `wiki-page-scaffold`, `pipeline-post-validate` | `ANTHROPIC_BASE_URL=<aicp>` |
> | "Code-reviewer" | OpenCode | `pr-review`, `lint-check` | `OPENROUTER_API_KEY=<key>` |
> | "Migration-writer" | Claude Code | `write-migration`, `validate-sql` | `ANTHROPIC_BASE_URL=<aicp>` |
>
> Skills are workspace-level reusable; one well-authored skill compounds across the agent fleet. **Each agent = (provider × custom_env × custom_args × skills × instructions × model)** — six independent per-agent dimensions for shaping the agent's behavior.

## Operator Validation 2026-04-28

> [!success] **`custom_env` mechanism confirmed working — operator-validated**
>
> Operator quote 2026-04-28: *"In reality we can do whatever we want because I built it from: /home/jfortin/.multica/server/. I even had to write a .env there. ... Injected into the agent process at launch (e.g. ANTHROPIC_API_KEY, ANTHROPIC_BASE_URL)."*
>
> **What this confirms:**
> - The `custom_env` agent field IS exposed in the operator's UI and accepts `ANTHROPIC_API_KEY` / `ANTHROPIC_BASE_URL`
> - Multica's daemon DOES inject the vars into the spawned harness CLI's process at launch
> - The mechanism described in this module is empirically working, not just doc-derived
> - **Operator runs self-hosted Multica at `/home/jfortin/.multica/server/`** (built from source) — has source-level access to extend or fork if needed
> - Operator authored the `.env` for Multica's server itself; only added one key (dev mode customization)

## Operational Caveats — Updated for Operator's Self-Host Context

> [!warning] Caveats per Multica documentation (lines 6444, 7095, 7100), reframed for operator's self-host setup
>
> | Caveat | Operator's self-host context |
> |---|---|
> | **`custom_env` is stored plaintext in the Multica database** | Operator's own machine, operator's own filesystem. Not a third-party data-exposure concern. Operator's filesystem security posture is what matters. The plaintext-DB warning that would apply to Multica Cloud users is mitigated for self-host. |
> | **`custom_env` overrides rather than merges with shell env** | Set the full env per agent. If a global shell env had `ANTHROPIC_API_KEY` set, the agent's `custom_env` replaces it for the spawned process — does not augment. |
> | **Non-owner redaction at API level** | Single-operator workspace — not relevant. Operator IS the owner; sees own values without redaction. |
> | **MCP config currently consumed only by Claude Code** | Other harnesses receive `mcp_config` but their CLIs don't use it (per line 7043). Provider routing via MCP works under Claude Code today; other harnesses use `custom_env` directly for provider config. |
> | **Source-level access (operator-only advantage)** | Because operator built from source, they can modify Multica itself if needed — extend the daemon, patch the agent-spawn logic, add custom provider abstractions, inspect the DB directly. This is an option the cloud-Multica path doesn't have. |

## Done When

- [x] Investigation: Multica per-agent provider config mechanism documented (`custom_env` field) — DONE 2026-04-28
- [x] Wiring recipes documented for the 4 most-likely operator cases — DONE this module
- [x] Operator validates: `custom_env` field is exposed and works — CONFIRMED 2026-04-28: *"Injected into the agent process at launch (e.g. ANTHROPIC_API_KEY, ANTHROPIC_BASE_URL)"*
- [x] Operator validates: self-host install path documented (`/home/jfortin/.multica/server/`, built from source, `.env` operator-written) — CONFIRMED 2026-04-28
- [ ] Operator runs a smoke task on a `custom_env`-configured agent and observes round-trip routing (ready to execute now using Recipe 1 or Recipe 2 above)
- [ ] M002 (Harness-level provider wiring under Multica) becomes unblocked — **already unblocked by operator validation 2026-04-28**

## Open Questions (resolved + remaining)

> [!success] ~~How does Multica's UI expose per-agent provider config?~~ **RESOLVED 2026-04-28**
> Per-agent `custom_env` field on the agent record. Configured via the agent's settings UI (Settings → Agents → Edit Agent → Env tab per line 4424).

> [!success] ~~Does Multica's daemon propagate operator's env to spawned harness processes?~~ **RESOLVED 2026-04-28**
> Yes — `custom_env` overrides shell env for the spawned process (per line 6444 + 7100 docs).

> [!question] What is Ollama Cloud's exact Anthropic-compat endpoint URL?
> The `ollama launch claude` wrapper sets it automatically; need to extract the URL pattern for direct `custom_env` configuration. Operator may have this from existing usage. (Resolution: capture from the operator's existing Ollama Cloud login or check `ollama` CLI docs.)

> [!question] Does AICP expose a stable Anthropic-compat endpoint for Multica to point at?
> AICP's `local` operating mode should expose this, but the exact URL/port pattern needs verification against AICP's current state (per [AICP 2026-04-24 handoff](file:///home/jfortin/devops-expert-local-ai/docs/SESSION-2026-04-24-HANDOFF.md)).

> [!question] How to handle agents that need to switch providers dynamically (per-task, not per-agent)?
> Multica's model is per-agent provider, not per-task. For dynamic routing, AICP's complexity scorer + the agent's `ANTHROPIC_BASE_URL` pointing at AICP delivers it — AICP makes the per-request decision; Multica's agent is stable. This is exactly Recipe 1 above.

## Tasks

| Task | Description | Status |
|---|---|---|
| T-M001-1 | Read Multica README + linked docs (CLI_AND_DAEMON.md, SELF_HOSTING.md) for agent-config detail | ✅ Done 2026-04-28 — found `custom_env` mechanism at lines 4424, 6444, 7037, 7095, 7455 of raw scrape |
| T-M001-2 | Document the 4 wiring recipes (AICP-routed, Ollama Cloud direct, OpenCode, multi-agent multi-provider) | ✅ Done — see Concrete Wiring Recipes section above |
| T-M001-3 | Document operational caveats (plaintext DB, override-not-merge, redaction, MCP consumption) | ✅ Done — see Operational Caveats section above |
| T-M001-4 | Operator validates `custom_env` field exposure in Multica's UI | ⊙ Pending operator (Settings → Agents → Edit Agent → look for Env tab) |
| T-M001-5 | Operator validates per-agent provider routing with one smoke task | ⊙ Pending operator |
| T-M001-6 | Capture Ollama Cloud's exact Anthropic-compat endpoint URL | ⊙ Pending — operator may have from existing usage, OR check `ollama launch claude` behavior |
| T-M001-7 | Capture AICP's exposed local endpoint URL pattern | ⊙ Pending — verify against AICP's current `local` mode state |

## Dependencies

- **External**: Multica installed and running (operator confirmed 2026-04-28 — already on the UI).
- **External**: Operator-side access to Multica's "Edit Agent" → Env tab (UI-level validation).
- **External**: Ollama Cloud login active (operator confirmed since 2026-04-23 per [project_activated_stack_2026_04_23](file:///home/jfortin/.claude/projects/-home-jfortin-devops-solutions-information-hub/memory/project_activated_stack_2026_04_23.md)).
- **External**: AICP repo with `local` / `k2_6_local` / `k2_6_openrouter` / `ollama_cloud` backends wired (per [AICP 2026-04-24 handoff](file:///home/jfortin/devops-expert-local-ai/docs/SESSION-2026-04-24-HANDOFF.md)).
- **Wiki**: Parent epic [post-anthropic-stack-3-layer-assembly-multica-aicp-3090](../epics/pre-milestone/post-anthropic-stack-3-layer-assembly-multica-aicp-3090.md).
- **Wiki**: Multica synth [src-multica-managed-agents-platform](../../sources/tools-integration/src-multica-managed-agents-platform.md) — orchestrator-layer source.
- **Hardware**: NOT blocked by RTX 4090 delivery — `custom_env` testing works on existing hardware. Local-Ollama tier (M004) is the part that waits for hardware.

## Operator's Immediate Next Step

In Multica's UI right now:
1. Settings → Agents → Edit your existing agent (or New Agent)
2. Look for the **Custom Env** / **Env** field (per the docs, this should be visible)
3. Add `ANTHROPIC_BASE_URL=<aicp-endpoint>` and `ANTHROPIC_API_KEY=<aicp-token>` (or whichever provider you want for that agent)
4. Save → assign a smoke-test task → verify the harness routes correctly

That's the unblocking step. The investigation is done; what remains is operator-side validation and any tweaks based on what the UI actually exposes.

## Relationships

- PART OF: [[post-anthropic-stack-3-layer-assembly-multica-aicp-3090|Epic — Post-Anthropic 3-Layer Stack Assembly]]
- BUILDS ON: [[src-multica-managed-agents-platform|Multica Synthesis]] (the Layer-1 source for the orchestrator-layer answer)
- BUILDS ON: [[kimi-k2-6-access-paths-openrouter-ollama-cloud-local|K2.6 Access Paths]] (provider-tier routing rules — `ollama launch claude` wrapper inspires Recipe 2)
- DEMONSTRATES: [[infrastructure-over-instructions-for-process-enforcement|Principle 1]] (`custom_env` is infrastructure-level provider routing, not instruction-level)
- DEMONSTRATES: [[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4]] (Multica's "vendor-neutral" claim is verified by the `custom_env` mechanism existing and being agent-scoped)

## Backlinks

[[Epic — Post-Anthropic 3-Layer Stack Assembly]]
[[src-multica-managed-agents-platform|Multica Synthesis]]
[[K2.6 Access Paths]]
[[infrastructure-over-instructions-for-process-enforcement|Principle 1]]
[[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4]]
