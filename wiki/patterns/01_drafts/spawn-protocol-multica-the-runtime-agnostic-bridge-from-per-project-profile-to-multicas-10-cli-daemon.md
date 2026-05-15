---
title: "Pattern — Spawn protocol for Multica: bridge a Per-Project Assistant Profile to a running Assistant instance on Multica's 10-CLI daemon (operator-adopted runtime)"
type: pattern
domain: ai-agents
status: synthesized
confidence: high
maturity: seed
layer: 2
created: 2026-05-09
updated: "2026-05-09"
sources:
  - id: companion-profile-pattern
    type: wiki
    file: wiki/patterns/01_drafts/per-project-assistant-profile-pattern-tailored-config-to-spawn-ecosystem-runtimes.md
    description: "Parent pattern — Per-Project Assistant Profile. This spawn protocol is one of several runtime-specific implementations (Multica, generic Agent SDK, OpenClaw, OpenArms, Hermes)"
  - id: src-multica-repo
    type: file
    file: raw/articles/multica-aimultica.md
    description: "Multica README v1.x — open-source managed agents platform; Go+Next.js+pgvector+Daemon architecture; supports 10+ agent CLIs"
  - id: memory-multica-self-hosted
    type: file
    file: ~/.claude/projects/-home-jfortin-devops-solutions-information-hub/memory/project_multica_self_hosted_2026_04_28.md
    description: "Operator memory — Multica self-hosted at /home/jfortin/.multica/server/ with .env + source-level access; custom_env per-agent routing confirmed working 2026-04-28"
  - id: comparison-frontier
    type: wiki
    file: wiki/comparisons/assistant-platforms-and-frameworks-frontier-comparison-claude-os-obsidian-pm-multica-openclaw-command-center-2026-05-09.md
    description: "Frontier comparison identifying Multica as T3 frontier and the operator's already-adopted runtime"
  - id: epic-e024
    type: wiki
    file: wiki/backlog/epics/milestone-v2/e024-per-project-assistant-configurations-to-capture-programmatic-credit-and-enable-ecosystem-spawn.md
    description: "Parent E024 Epic — M004 spawn protocols module; this is the first concrete spawn protocol because Multica is the only operator-adopted runtime"
tags: [pattern, spawn-protocol, multica, runtime-bridge, daemon-cli-auto-detection, per-project-assistant, profile-to-runtime, operator-adopted-runtime, "2026-05-09", ai-agents, "draft", e024-m004]
---

# Pattern — Spawn protocol for Multica

## Summary

Spawn protocol that consumes a [[per-project-assistant-profile-pattern-tailored-config-to-spawn-ecosystem-runtimes|Per-Project Assistant Profile]] and materializes a running Assistant instance on **Multica** — the open-source managed agents platform that operator has self-hosted at `/home/jfortin/.multica/server/` (per 2026-04-28 memory). Multica's daemon auto-detects 10+ agent CLIs on PATH (Claude Code · Codex · OpenClaw · OpenCode · Hermes · Gemini · Pi · Cursor Agent · Kimi · Kiro CLI), exposes them as runtimes, and dispatches tasks to them via per-workspace agents with WebSocket progress streaming. The spawn protocol maps Profile sections → Multica primitives: Profile's runtime_targets → Multica's agent CLI selection; Profile's knowledge_scope → Multica's workspace + MCP wiring; Profile's action_surface → Multica's skills system; Profile's prompt_templates → Multica agent profile/system prompt; Profile's success_criteria → Multica's task completion + telemetry. This is the **first concrete spawn protocol** in E024-M004 because Multica is the only operator-already-adopted runtime — making this the lowest-friction integration path for capturing the 2026-06-15 programmatic credit pool with valuable per-project automation.

## Pattern Description

The spawn protocol is a deterministic mapping: read Profile YAML → render Multica primitives → register via `multica` CLI / API → verify the running instance behaves per Profile. The protocol leaves the **Profile** intact and runtime-agnostic; only this pattern document encodes Multica-specific knowledge.

| Profile section | Multica primitive | How mapped |
|---|---|---|
| **Identity** (name, version, project, owner, runtime_targets) | Multica Agent (Settings → Agents → New Agent) | Profile name → Multica agent display name; runtime_targets must include one of Multica's 10+ CLIs; project → Multica workspace |
| **Knowledge Scope** (wiki paths, raw paths, MCP servers, sister projects) | Multica workspace + agent MCP config + per-agent custom_env | wiki paths → mounted/accessible via daemon; MCP servers → registered in agent config; sister projects → workspace cross-links |
| **Action Surface** (allowed/forbidden tools, escalation triggers) | Multica skills system + per-agent capabilities | allowed tools → registered as Multica skills the agent can invoke; forbidden → blocked at daemon layer; escalation triggers → Multica issue creation + assignment |
| **Model Routing** (primary, fallback, cost ceiling) | Multica agent provider selection + per-agent custom_env routing | primary model → agent's primary CLI provider; fallback → secondary providers; cost ceiling → enforced via daemon-level circuit breakers |
| **Prompt Templates** (system, action, escalation, recovery) | Multica agent profile + system prompt fields | system prompt → agent's "system prompt" field in Multica UI; action/escalation prompts → invocation-time injection via daemon |
| **Success Criteria** (observable outcomes, value-per-month, telemetry) | Multica task completion + WebSocket telemetry + skills metrics | observable outcomes → task completion criteria; telemetry → daemon log streams to `multica issue list` + agent metrics view |

## Instances

| Instance | Profile | Status |
|---|---|---|
| **this project (the research wiki) on Multica** (planned per E024-M003 + this pattern) | [[assistant-profile profile]] | Pending — needs Profile schema (M002) + this spawn protocol |
| **OpenArms-via-Multica** (future) | OpenArms profile | Future per E024-M006 |
| **AICP-via-Multica** (future) | AICP profile | Future per E024-M006 |
| **Any sister project on Multica** | Per-project profile | Future per E024-M006 |

## When To Apply

> [!success] **Apply spawn-protocol-multica when**
>
> - Profile's `runtime_targets:` includes one of Multica's 10+ supported CLIs
> - Operator's already-adopted Multica self-host is the desired runtime layer
> - Multi-agent coordination is needed (Multica's workspace + board model)
> - WebSocket progress streaming is desired (e.g., for the "information surface before public Obsidian" requirement — D10)
> - Per-agent custom_env routing is needed (operator-confirmed working per 2026-04-28 memory)

## When Not To

> [!warning] **Do NOT apply spawn-protocol-multica when**
>
> - Profile is single-shot interactive (use `spawn-protocol-claude-code-cli-p` for `claude -p`)
> - The runtime CLI required is NOT in Multica's supported list (would need to add adapter or use direct spawn)
> - Operator wants to bypass Multica's workspace model (e.g., one-off scripts)
> - Cost-tracking is per-CLI, not per-Multica-agent (use direct CLI spawn)

## The 6-Step Spawn Sequence

```
┌─────────────────────────────────────────────────────────────────┐
│  STEP 1: Validate Profile against schema (T071 — E024-M002)       │
└─────────────┬───────────────────────────────────────────────────┘
              │
              ▼
┌─────────────────────────────────────────────────────────────────┐
│  STEP 2: Verify Multica daemon running + CLI in detected list     │
│    multica daemon status                                          │
│    Settings → Runtimes (check daemon ACTIVE)                      │
│    Settings → Runtimes detail (Profile's runtime_target in list)  │
└─────────────┬───────────────────────────────────────────────────┘
              │
              ▼
┌─────────────────────────────────────────────────────────────────┐
│  STEP 3: Create/update Multica workspace per Profile.project       │
│    multica workspace create <project>                             │
│    (or Settings → Workspaces in UI)                               │
└─────────────┬───────────────────────────────────────────────────┘
              │
              ▼
┌─────────────────────────────────────────────────────────────────┐
│  STEP 4: Create Multica agent from Profile                         │
│    Settings → Agents → New Agent                                  │
│      Name: profile.identity.name                                  │
│      Runtime: profile.runtime_targets[0]                          │
│      Provider: matches runtime (Claude Code, Hermes, etc.)        │
│      System prompt: profile.prompt_templates.system               │
│      Skills: profile.action_surface.allowed (Multica skills)      │
│      Custom env: profile.knowledge_scope.mcp_servers + paths      │
└─────────────┬───────────────────────────────────────────────────┘
              │
              ▼
┌─────────────────────────────────────────────────────────────────┐
│  STEP 5: First task — verify spawn (smoke test)                    │
│    multica issue create --assign <profile.identity.name>          │
│      Title: "Spawn smoke test"                                    │
│      Body: <profile.success_criteria.observable_outcomes[0]>      │
│    Watch via Multica board / multica issue list                   │
└─────────────┬───────────────────────────────────────────────────┘
              │
              ▼
┌─────────────────────────────────────────────────────────────────┐
│  STEP 6: Telemetry + Success Criteria verification                 │
│    Compare WebSocket progress stream vs Profile.success_criteria  │
│    Verify cost ceiling not exceeded                               │
│    Update Profile if drift detected                               │
└─────────────────────────────────────────────────────────────────┘
```

## How To Apply (concrete walkthrough — this project (the research wiki) example)

This walkthrough assumes:
- E024-M002 Profile schema is finalized (T071 done)
- this project (the research wiki) Profile authored at `.assistant/profile.yaml` (T075 done)
- Multica daemon is running at `/home/jfortin/.multica/server/`

### 1. Validate Profile

```bash
.venv/bin/python -m tools.pipeline validate-profile .assistant/profile.yaml
# (Pipeline post extension from T073 — TBD)
```

### 2. Verify Multica daemon + CLI detection

```bash
multica daemon status
# Expected: daemon RUNNING; PATH-detected CLIs include: claude, codex, openclaw, opencode, hermes, gemini, pi, cursor-agent, kimi, kiro-cli
```

### 3. Create workspace (if not exists)

```bash
multica workspace create devops-solutions-information-hub
# (Or use the existing workspace if operator has one)
```

### 4. Create Multica agent from this project Profile

Via Multica UI (Settings → Agents → New Agent) or via `multica` CLI:

| Multica field | Source from Profile |
|---|---|
| Name | `assistant-profile` (from Profile.identity.name) |
| Runtime | The daemon-host (operator's machine) |
| Provider | `claude-code` (from Profile.runtime_targets[0]; can be Hermes/OpenClaw/Claude Code/etc.) |
| System prompt | Profile.prompt_templates.system (verbatim) |
| Skills enabled | Profile.action_surface.allowed (each mapped to Multica skill ID) |
| Custom env | Profile.knowledge_scope.mcp_servers + wiki paths |
| Cost ceiling (Multica-side) | Profile.model_routing.cost_ceiling_usd_per_month ($50/month for this project example) |

### 5. Smoke-test the spawned Assistant

Create a Multica issue and assign to the new agent:

```bash
multica issue create \
  --workspace devops-solutions-information-hub \
  --title "Smoke test: orient + report pipeline status" \
  --body "Run gateway orient + pipeline status; report findings." \
  --assign assistant-profile
```

Watch via:
- Multica web UI board (real-time WebSocket)
- `multica issue list --watch`
- daemon log: `tail -f /home/jfortin/.multica/server/logs/daemon.log`

### 6. Verify telemetry against success criteria

Compare:
- WebSocket progress stream (Multica board) vs Profile.success_criteria.observable_outcomes
- Token consumption / cost vs Profile.model_routing.cost_ceiling_usd_per_month
- Issue completion status vs expected output

If drift detected → update Profile, re-spawn, iterate.

## Why Multica First (vs Other Spawn Protocols)

| Reason | Detail |
|---|---|
| **Operator already adopted** | Self-hosted at `/home/jfortin/.multica/server/` since 2026-04-28; no migration cost |
| **Custom_env routing confirmed working** | Per memory: operator validated per-agent routing on 2026-04-28 |
| **10-CLI breadth** | Same Multica adapter supports Hermes / Claude Code / OpenClaw / etc — one spawn protocol, many runtimes |
| **WebSocket streaming** | Solves D10 "information surface before public Obsidian" naturally — board view streams progress |
| **Self-hosted = data sovereignty** | Aligns with anti-vendor-lock-in mission |
| **Issues + Chat + Skills primitives** | Natural model for Profile-as-Agent: Multica's agent model maps cleanly to Profile's identity + action_surface + success_criteria |

## Trade-offs

| Trade-off | Direction |
|---|---|
| **Multica overhead vs direct CLI spawn** | Multica overhead = workspace/agent setup; direct CLI = simpler but loses board/telemetry/team-coord. ACCEPTED — operator's existing investment justifies. |
| **Multica's cloud vs self-host** | Self-host adds Docker + maintenance burden but ensures data sovereignty. ACCEPTED — already operator-chosen. |
| **Multica's PostgreSQL+pgvector vs lighter SQLite (Claude OS style)** | Heavier stack but team-native; ACCEPTED for this project where multi-context is natural |
| **Cost-tracking coupling** | Multica tracks per-agent cost; depending on Multica version, may not granularly map to Profile.model_routing.cost_ceiling. May need adapter. |

## Anti-Patterns

| Anti-pattern | Why bad |
|---|---|
| Skip Profile validation in step 1 | Schema-violating profiles cause runtime errors; validate first |
| Hard-code provider (e.g., always `claude-code`) | Defeats runtime-agnosticism; Profile's `runtime_targets:` should drive provider selection |
| Skip smoke test (step 5) | Profile may parse but behave unexpectedly; smoke test surfaces config drift |
| Skip telemetry comparison (step 6) | Without verification, success criteria are aspirational (P4 violation) |
| Use one Multica agent for multiple Profiles | Defeats per-project tailoring; one Profile = one Multica agent |
| Couple Multica agent ID to Profile name without versioning | Profile updates require agent re-creation; consider name+version conventions |

## Integration with "Information Surface Before Public Obsidian" (D10)

Multica's WebSocket progress stream + board UI is a natural candidate for the operator's 2026-05-09 directive: *"we will also have to find a way to make the information surface somehow even before it reaches the public obsidian"*.

| Pre-Obsidian surfacing mechanism (via Multica) | What it surfaces |
|---|---|
| Multica board view (real-time WebSocket) | Issue progress, agent activity, comments — all updates as they happen |
| `multica issue list --watch` | CLI-level live feed of issue changes |
| Multica's per-agent custom_env tail | Real-time daemon log |
| Skills metrics view | Performance + cost telemetry per skill invocation |

This means: operator's information surfacing requirement can be addressed by leveraging Multica's existing telemetry, rather than building new infrastructure. The this project wiki content surfaces in Multica's board the moment the Assistant produces it — before any Obsidian sync happens.

## Sister-Project Applicability

| Project | Apply this spawn protocol? |
|---|---|
| **this project (the research wiki)** (this project, E024-M003) | **YES — first concrete instance** |
| **OpenArms / OpenFleet / AICP / dcp / Hermes (the project) / root-ghostproxy** | Plan: yes per E024-M006 (one Multica agent per project) |
| **Any project where Multica daemon is reachable** | Yes — Multica is the unified bridge across the ecosystem |

## Relationships

- IMPLEMENTS: [[per-project-assistant-profile-pattern-tailored-config-to-spawn-ecosystem-runtimes|Pattern — Per-Project Assistant Profile]] for Multica runtime
- PART OF: [[E024-M004 — Spawn Protocols per Runtime]]
- BUILDS ON: [[assistant-platforms-and-frameworks-frontier-comparison-claude-os-obsidian-pm-multica-openclaw-command-center-2026-05-09|Comparison — Assistant Platforms Frontier]] — Multica identified as T3 frontier + operator-adopted
- COMPLEMENTS: [[skill-systems-orchestrator-plus-modular-child-skills-the-architecture-pattern-anthropic-wont-solve-for-you|Pattern — Skill Systems]] — Skill Systems is the Action Surface implementation; this spawn protocol bridges Action Surface to Multica's skills primitive
- DEMONSTRATES: [[anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence|Lesson — Anti-Vendor-Lock-In]] — Multica's 10-CLI breadth means Profile can swap providers without re-authoring

## Cross-references

- Multica self-host: `/home/jfortin/.multica/server/`
- Operator memory: `~/.claude/projects/-home-jfortin-devops-solutions-information-hub/memory/project_multica_self_hosted_2026_04_28.md`
- Multica README: `raw/articles/multica-aimultica.md`
- Multica setup: `multica setup self-host`
- E024-M004 module: TBD (this pattern motivates module page authoring as forward work)

## Backlinks

[[Pattern — Per-Project Assistant Profile]]
[[E024-M004 — Spawn Protocols per Runtime]]
[[Comparison — Assistant Platforms Frontier]]
[[Pattern — Skill Systems]]
[[Lesson — Anti-Vendor-Lock-In]]
