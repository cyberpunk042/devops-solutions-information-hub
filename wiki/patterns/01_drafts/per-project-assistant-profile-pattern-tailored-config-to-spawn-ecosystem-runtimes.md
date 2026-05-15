---
title: "Pattern — Per-Project Assistant Profile: tailored declarative configuration that spawns runtime-agnostic assistant instances on OpenClaw / OpenArms / Hermes / generic Agent SDK consumers"
type: pattern
domain: ai-agents
status: synthesized
confidence: high
maturity: seed
layer: 2
created: 2026-05-09
updated: "2026-05-09"
sources:
  - id: operator-directive-2026-05-09
    type: directive
    file: raw/notes/2026-05-09-operator-directive-per-project-assistant-configs-spawn-openclaw-openarms-hermess-and-anthropic-programmatic-budget-policy-research.md
    description: "Operator directive — per-project assistant configurations/profiles to spawn ecosystem-project instances"
  - id: anthropic-policy-context
    type: wiki
    file: wiki/sources/ai-models/src-anthropic-programmatic-credit-pool-policy-change-2026-06-15.md
    description: "Anthropic 2026-06-15 policy creating the credit pool this pattern is designed to consume"
  - id: decision-strategic-response
    type: wiki
    file: wiki/decisions/01_drafts/strategic-response-to-anthropic-programmatic-credit-pool-via-per-project-assistant-profiles.md
    description: "Strategic decision selecting this pattern as the response approach"
  - id: epic-e024
    type: wiki
    file: wiki/backlog/epics/milestone-v2/e024-per-project-assistant-configurations-to-capture-programmatic-credit-and-enable-ecosystem-spawn.md
    description: "Epic E024 implementing this pattern across the 5-project ecosystem"
tags: [pattern, per-project-assistant, assistant-profile, runtime-agnostic, declarative-config, openclaw, openarms, hermess, agent-sdk, spawn-protocol, schema, ai-agents, "2026-05-09", "draft"]
---

# Pattern — Per-Project Assistant Profile

## Summary

A **per-project Assistant Profile** is a declarative configuration artifact (one per repository) that defines an assistant's identity, knowledge scope, action surface, model routing, MCP wiring, prompt templates, and success criteria — in a runtime-agnostic format. The Profile is consumed by a **spawn protocol** to materialize a running assistant instance on a specific runtime (OpenClaw, OpenArms, Hermes, generic Agent SDK consumer, future runtimes). The Profile is the **spec**; the spawned instance is the **product**. The pattern enables: (1) per-project tailoring without re-authoring runtime-specific config; (2) runtime portability (same Profile → different runtimes); (3) operator-level navigation across ecosystem assistants; (4) capture of Anthropic's programmatic credit pool ($200/month at Max 20x, effective 2026-06-15). Profiles must remain runtime-agnostic to preserve [[anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence|anti-vendor-lock-in mission alignment]] — future routing to local-AI (AICP), other-provider models, and custom-tailored model groups must be supported by the schema.

## Context

This pattern applies when:
- A project needs a recurring assistant (curation, automation, scheduled tasks, on-demand specialist)
- The assistant should be tailored to the project's specific needs (knowledge, terminology, workflows)
- The assistant runtime is one of OpenClaw / OpenArms / Hermes / generic Agent SDK (or any future Agent-SDK-compatible runtime)
- Cross-project consistency matters (operator wants to navigate assistants across the 5-project ecosystem)
- Anthropic's programmatic credit pool should be consumed via productive automation (effective 2026-06-15)

Does NOT apply to:
- Single-shot scripts (use `claude -p` directly without Profile)
- Interactive Claude Code use (interactive draws from subscription pool, not credit pool — Profile abstraction is overhead with no benefit)
- Project-runtime where the assistant is the runtime itself (e.g., OpenClaw's own internal assistants — those are runtime-territory, not Profile-territory)

## Pattern Description

A **Per-Project Assistant Profile** is a declarative YAML configuration with 6 required sections (Identity, Knowledge Scope, Action Surface, Model Routing, Prompt Templates, Success Criteria). The Profile is the **spec** the assistant inherits; the assistant runtime (OpenClaw, OpenArms, Hermes, generic Agent SDK consumer) is the **execution layer** that consumes the spec at spawn time. The pattern separates declarative configuration from execution mechanics — the same Profile can spawn on multiple runtimes via runtime-specific spawn protocols. Per-project tailoring means each repository has its own Profile reflecting that project's actual needs; the schema enforces that all Profiles use the same 6-section structure so they remain navigable, comparable, and migrable across the ecosystem.

## Instances

| Instance | Project | Status | Notes |
|---|---|---|---|
| **opt-second-brain-assistant** | devops-solutions-information-hub (this) | planned (E024-M003 / T075) | The canonical example — knowledge curation, methodology stewardship, source ingestion, lesson distillation |
| **openarms-assistant** | OpenArms | future (E024-M006) | Fleet-agent runtime engineering, harness compliance, methodology enforcement |
| **openfleet-assistant** | OpenFleet | future (E024-M006) | Fleet orchestration, LightRAG knowledge consumption, task dispatch |
| **aicp-assistant** | AICP | future (E024-M006) | Local-AI inference, complexity routing, $0 target enforcement |
| **dcp-assistant** | devops-control-plane | future (E024-M006) | Infrastructure governance, decision tracking |
| **root-ghostproxy-assistant** | root-ghostproxy | future (E024-M006) | Harness/ecosystem maintenance, global config propagation, IPS rule curation |
| **hermes-assistant** | Hermes | future (E024-M006) — Hermes confirmed 2026-05-09 (Greek messenger god) |

## Pattern Structure

> [!success] **Profile is the spec; Assistant is the spawned instance**
>
> Declarative artifact → spawn protocol → running instance. The pattern enforces the separation so the same Profile can spawn on multiple runtimes and projects can swap runtimes without re-authoring the Profile.

### The 6 Profile sections

A valid Per-Project Assistant Profile MUST have these sections:

| Section | Content | Why |
|---|---|---|
| **1. Identity** | name, version, project, owner, tagline, runtime-targets supported | Declares what the assistant IS and which runtimes accept it |
| **2. Knowledge Scope** | wiki paths, raw paths, file globs, MCP server access, sister-project links | Bounds what the assistant can/should know — prevents knowledge bloat |
| **3. Action Surface** | allowed tool calls, forbidden tool calls, escalation triggers, approval gates | The MUST/MUST NOT list — programs assistant behavior structurally (P2) |
| **4. Model Routing** | primary model, fallback chain, complexity-to-tier mapping, cost ceilings | Runtime-agnostic preferences for which model serves which workload |
| **5. Prompt Templates** | system prompt, action prompts, escalation prompts, error-recovery prompts | The actual prose the assistant inherits when spawned |
| **6. Success Criteria** | observable outcomes, measurable per-month value-output, quality gates, telemetry hooks | How to know the assistant is delivering value (gates against the $200/month credit waste) |

### Profile schema (YAML-style — exact format TBD in M002 of E024)

```yaml
---
profile_version: 1                       # schema version
profile_name: opt-second-brain-assistant
project: devops-solutions-information-hub
owner: operator
tagline: "Knowledge curation, methodology stewardship, source ingestion, lesson distillation for the research wiki"
runtime_targets:                         # which runtimes this Profile can spawn on
  - openclaw
  - openarms
  - generic-agent-sdk
  - claude-code-cli-p                    # the `claude -p` non-interactive mode
knowledge_scope:
  wiki_paths:
    - wiki/spine/                        # foundation knowledge
    - wiki/lessons/03_validated/         # validated lessons
    - wiki/config/                       # methodology engine
  raw_paths:
    - raw/notes/                         # operator directives (sacrosanct)
  mcp_servers:                           # which MCP servers the assistant uses
    - research-wiki                      # the existing wiki MCP server
  sister_projects:                       # cross-project knowledge links
    - openarms
    - root-ghostproxy
action_surface:
  allowed:
    - wiki_search
    - wiki_read_page
    - wiki_log
    - wiki_gateway_orient
    - pipeline_post
  forbidden:
    - WebFetch                           # use wiki_fetch instead (per CLAUDE.md Hard Rule 6)
    - destructive_git_ops                # no force-push, no reset --hard
  escalation_triggers:
    - operator_directive_received        # log verbatim, escalate to operator
    - schema_change_proposed             # operator-approval territory
model_routing:
  primary: anthropic-claude-opus-4-7    # for complex synthesis
  fallback:
    - anthropic-claude-haiku-4-5         # for simple lookups
    - ollama-cloud-qwen3                 # for cost optimization
  complexity_to_tier:
    high: primary
    medium: primary
    low: fallback[1]
  cost_ceiling_usd_per_month: 50         # caps credit consumption per profile
prompt_templates:
  system: |
    You are the /opt second-brain Assistant. You curate, synthesize,
    and steward the research wiki at devops-solutions-information-hub.
    Behave FROM the project, not OVER it. Use MCP tools as your operating
    system. Operator words are sacrosanct — quote verbatim, never paraphrase.
  on_directive_received: |
    Operator just gave a directive. Log to raw/notes/ verbatim BEFORE acting
    (AGENTS.md Hard Rule #3). Then decompose into actions per the routing table.
  on_error: |
    State what failed, what was investigated, what the next step is. Don't
    bypass safety checks. Don't claim "done" without inline verification.
success_criteria:
  observable_outcomes:
    - "raw/notes/ has verbatim log entries for each operator directive received"
    - "wiki/lessons/ shows monthly net-new lessons or promotions"
    - "pipeline post returns 0 errors after each session"
  measurable_value_per_month:
    target_credit_consumption_usd: 30-50  # consume $30-50/month of the $200 budget productively
    quality_proxy: "operator review checkboxes per delivered artifact"
  telemetry:
    log_to: /tmp/opt-second-brain-assistant-telemetry.jsonl
---
```

## The Spawn Protocol

> [!info] **One Profile, many spawn protocols (one per runtime)**
>
> The Profile is runtime-agnostic. A separate **spawn protocol** documents (per runtime) how the Profile is consumed to instantiate a running assistant. Spawn protocols live as their own pattern pages.

| Runtime | Spawn protocol (planned) |
|---|---|
| **Generic Agent SDK** | [[spawn-protocol-generic-agent-sdk]] — read Profile → construct Agent SDK config → instantiate Agent → expose CLI/HTTP endpoint |
| **OpenClaw** | [[spawn-protocol-openclaw]] — read Profile → map to OpenClaw harness config → register profile as OpenClaw "personality" → expose Discord/Telegram/HTTP front-end |
| **OpenArms** | [[spawn-protocol-openarms]] — read Profile → map to OpenArms fleet-agent spec → register in fleet → schedule per cron/event triggers |
| **Hermes** | [[spawn-protocol-hermes]] — planned per E024-M004 (Hermes confirmed 2026-05-09) |
| **`claude -p` CLI** | [[spawn-protocol-claude-code-cli-p]] — read Profile → render system prompt + tool list → invoke `claude -p` with composed args (consumes programmatic credit per Anthropic 2026-06-15 policy) |

## Why Runtime-Agnostic Matters

> [!warning] **A Profile coupled to one runtime violates the anti-vendor-lock-in mission**
>
> If the Profile schema only supports Claude Agent SDK, the operator's investment in profiles becomes a sunk cost when Claude alternatives mature (local models, Ollama Cloud, Kimi K2.6 via OpenRouter, custom-tailored model groups). Runtime-agnosticism preserves portability.

Concrete examples:
- A Profile says "use the primary model for complex synthesis" — the runtime decides which actual model (Claude Opus, Qwen3.5, custom LoRA)
- A Profile says "must have access to wiki_search MCP" — the runtime ensures that MCP is wired regardless of host
- A Profile says "cost ceiling $50/month" — the runtime tracks consumption regardless of pricing model

## When To Apply

> [!tip] **Project gets a Profile when**
>
> 1. The project has recurring assistance needs (curation, automation, scheduled tasks)
> 2. The needs are project-specific (not generic — generic = no profile needed, use `claude -p` ad-hoc)
> 3. The operator wants ecosystem-wide consistency (the 5-project navigability)
> 4. The credit-capture frame matters (consuming $200/month at Max 20x)

## When Not To

> [!warning] **Don't apply this pattern for**
>
> - **Single-shot tasks**: use `claude -p` directly — profile abstraction is overkill
> - **Interactive coding**: interactive Claude Code draws from subscription pool, not credit pool — Profile adds friction with no benefit
> - **Runtime-internal assistants** (e.g., OpenClaw's own internal agents): those are runtime-territory; Profile applies to user-spawned instances
> - **Projects without recurring needs**: a Profile is overhead for one-time work

## Anti-Patterns

| Anti-pattern | Why bad |
|---|---|
| Conflate Profile (config) with Assistant (running instance) | Loses the abstraction; can't swap runtimes |
| Couple Profile schema to one runtime's API | Violates runtime-agnosticism; breaks anti-vendor-lock-in alignment |
| Build a single mega-profile for all projects | Loses per-project tailoring; operator-stated *"tailored to the needs"* per project |
| Profile without success criteria section | Can't measure value-output; can't gate against $200/month waste |
| Profile prompts that aren't sacrosanct-aware | Mistreats operator words; misses verbatim-logging discipline |
| Skip schema validation | Profile becomes ad-hoc; quality bar erodes |

## How to Apply

1. **Per-project**: in each repo, author the Profile at a well-known path (e.g., `.assistant/profile.yaml` or `wiki/assistant-profile.yaml` — TBD in E024 M002)
2. **Validate**: extend `pipeline post` to validate Profile schema (mandatory sections, well-formed fields)
3. **Bind to runtime**: pick a spawn protocol per intended runtime; document the binding
4. **Spawn**: invoke the spawn protocol; verify the resulting instance behaves per the Profile
5. **Observe**: telemetry hooks → measure credit consumption + value-output per month
6. **Iterate**: profile is versioned; updates go through normal review

## Sister-Project Applicability

| Project | Profile expectation |
|---|---|
| **/opt second-brain** (this) | Profile tailored to knowledge curation, methodology stewardship, source ingestion, lesson distillation |
| **OpenArms** | Profile tailored to fleet-agent runtime engineering, harness compliance, methodology enforcement |
| **OpenFleet** | Profile tailored to fleet orchestration, LightRAG knowledge consumption, task dispatch |
| **AICP** | Profile tailored to local-AI inference, complexity routing, $0 target enforcement |
| **devops-control-plane** | Profile tailored to infrastructure governance, decision tracking |
| **root-ghostproxy** | Profile tailored to harness/ecosystem maintenance, global config propagation, IPS rule curation |
| **Hermes** | Profile tailored to Hermes's purpose (operator-confirmed 2026-05-09 as Greek-messenger-god-themed) — scope TBD |

## Relationships

- IMPLEMENTS: [[Strategic Response to Anthropic Programmatic Credit Pool]]
- BUILDS ON: [[src-anthropic-programmatic-credit-pool-policy-change-2026-06-15|Anthropic Programmatic Credit Pool Policy Synthesis]] — the policy context that makes this pattern time-relevant
- BUILDS ON: [[model-skills-commands-hooks|Model — Skills, Commands, Hooks]] — leverages the mechanism-determinism layers
- COMPLEMENTS: [[agent-modes-three-mode-pattern-with-mode-aware-loop-cycles|Pattern — Agent Modes (three-mode pattern)]] — mode pattern is /root-harness-territory; Profile pattern is per-project-assistant-territory. They compose: a Profile may declare which mode the spawned Assistant runs in.
- COMPLEMENTS: [[session-orientation-pair-sessionstart-hook-and-orient-command-with-orient-report|Pattern — Session Orientation Pair]] — orientation is per-project too; Profile may declare session-orient behavior
- DEMONSTRATES: [[infrastructure-over-instructions-for-process-enforcement|Principle 1 — Infrastructure Over Instructions]] — Profile is structural (schema-validated), not prose
- DEMONSTRATES: [[structured-context-governs-agent-behavior-more-than-content|Principle 2 — Structured Context Governs Agent Behavior]] — Profile sections are YAML-structured = programmatic
- COMPLEMENTS: [[anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence|Lesson — Anti-Vendor-Lock-In]] — runtime-agnosticism preserves the mission

## Backlinks

[[Strategic Response to Anthropic Programmatic Credit Pool]]
[[Anthropic Programmatic Credit Pool Policy Synthesis]]
[[Model — Skills, Commands, Hooks]]
[[Pattern — Agent Modes (three-mode pattern)]]
[[Pattern — Session Orientation Pair]]
[[infrastructure-over-instructions-for-process-enforcement|Principle 1 — Infrastructure Over Instructions]]
[[structured-context-governs-agent-behavior-more-than-content|Principle 2 — Structured Context Governs Agent Behavior]]
[[Lesson — Anti-Vendor-Lock-In]]
