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

A **per-project Assistant Profile** is the abstract per-project assistant definition — a declarative artifact (one per repository) that defines what the assistant IS for this project: identity, knowledge scope, action surface, model preferences, prompt templates, and success criteria. A Profile is **way more than just setting for one tool** (operator-doctrinal 2026-05-09, sacrosanct). It is tool-agnostic by definition; tools come and go around it. Tools may consume or reference a Profile through their native mechanisms (Claude Code's CLAUDE.md / AGENTS.md ambient loading, Multica's agent + workspace config, OpenClaw's agent personality, Claude OS's Memory MCP, Hermes's skill subsystem, OpenCode's similar mechanism, etc.) but the Profile does NOT change shape to fit any tool. The pattern enables: (1) per-project tailoring of the assistant's definition without coupling to specific runtimes; (2) tool portability — the same Profile remains valid as tools evolve, are added, or are deprecated; (3) cross-project consistency (operator can navigate assistants across the ecosystem); (4) quality of both DEFINITIONS (precision of identity/scope/surface) and FEATURES (what the assistant actually delivers). Profiles must remain tool-agnostic to preserve [[anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence|anti-vendor-lock-in mission alignment]] — *"support but not vendor lock ourself"* (operator 2026-05-09).

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

A **Per-Project Assistant Profile** is a declarative YAML artifact with 6 required sections (Identity, Knowledge Scope, Action Surface, Model Routing, Prompt Templates, Success Criteria). The Profile defines the abstract assistant for this project. Any tool that respects the abstract shape may consume the Profile through its native mechanism — but the Profile does NOT depend on, embed, or accommodate any specific tool's configuration shape. Per-project tailoring means each repository has its own Profile reflecting that project's actual needs; the shared 6-section structure makes Profiles navigable, comparable, and migrable across the ecosystem. The Profile is the abstract definition; tool configs are separate, derivative artifacts.

## Instances

> [!warning] **2026-05-09 boundary correction (operator-stated, sacrosanct)**: *"every project will do their own Profiles... this is per project"*. /opt does NOT author sister-project Profiles. The only Profile instance authored at /opt is /opt's own (eat-our-own-dogfood); every other project authors its own Profile in its own repo.

| Instance | Where authored | Status |
|---|---|---|
| **opt-second-brain-assistant** (this project — /opt's own Profile) | `wiki/domains/cross-domain/opt-second-brain-assistant-profile-...md` (THIS project's wiki) | ✅ authored 2026-05-09 |
| **Per-sister-project Profiles** (OpenArms · OpenFleet · AICP · devops-control-plane · OpenClaw · root-ghostproxy · others) | Each project's OWN repo (typically `.assistant/profile.yaml`) | NOT /opt's authoring scope. /opt provides standards + model + integration + super-model (E024-M006) that those projects consume. |

## Pattern Structure

> [!success] **A Profile is the abstract per-project assistant definition — way more than just settings for one tool**
>
> A Profile defines WHAT the assistant IS for this project: its identity, knowledge scope, action surface, model preferences, prompts, success criteria. It is **tool-independent** by definition. Any tool (Claude Code, Multica, OpenClaw, Claude OS, OpenCode, Hermes, etc.) may consume or reference the Profile through its own mechanism — but the Profile does NOT change shape to fit any tool. Treating a Profile as a synonym for tool config is a vendor-lock corruption.

### The 6 Profile sections

A valid Per-Project Assistant Profile MUST have these sections:

| Section | Content | Why |
|---|---|---|
| **1. Identity** | name, version, project, owner, tagline, purpose | Declares what the assistant IS — its abstract definition, independent of any runtime |
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
# NOTE: A Profile is the abstract assistant definition. It is NOT a tool config.
# It is NOT coupled to any specific runtime (Multica / Claude Code / OpenClaw / etc).
# Tool configs are SEPARATE artifacts that may consume / reference the Profile.
# Any spawn protocol documents HOW a tool consumes a Profile — never the other way around.
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

## How Tools Consume a Profile (NOT how a Profile is shaped by tools)

> [!info] **The Profile is the source; each tool consumes it through its own mechanism**
>
> The Profile is independent and abstract. Each tool that may instantiate or reference an assistant from a Profile does so through ITS native mechanism. The Profile never changes shape to fit any tool. Spawn protocols (per-tool documents) describe how each tool consumes a Profile — never how the Profile depends on the tool.

| Tool / runtime | How it can consume a Profile (via its native mechanism) |
|---|---|
| **Claude Code** (interactive) | Reads `.assistant/profile.yaml` as ambient context; Claude inherits Identity + Knowledge Scope + Prompt Templates via CLAUDE.md / AGENTS.md / MCP wiring |
| **`claude -p` CLI** (programmatic) | A wrapper composes the Profile's Prompt Templates + Action Surface into `claude -p` args; consumes Anthropic programmatic credit pool |
| **Multica** | Multica agent's system prompt + workspace + skills reference the Profile; daemon-level routing respects Profile.model_routing |
| **OpenClaw** | OpenClaw agent personality is built from the Profile; gateway-level configuration mirrors Profile.action_surface |
| **OpenCode** | OpenCode reads the Profile as ambient config (same approach as Claude Code) |
| **Claude OS** | Claude OS's Memory MCP + Real-Time Learning consume Profile.knowledge_scope; skills library aligned with Profile.action_surface |
| **Hermes Agent** (Nous Research) | Hermes consumes the Profile via its skill / memory subsystem |
| **Other / Future** | Any Agent-SDK-compatible runtime; Profile remains stable as tools evolve |

**Critical**: a Profile does NOT enumerate "supported" tools. Any tool that respects the Profile's abstract shape can consume it. The list above is illustrative, not exhaustive, and never bounding.

## Why Tool-Agnosticism Is Constitutive (Not Optional)

> [!warning] **A Profile coupled to one tool violates the anti-vendor-lock-in mission**
>
> Operator-doctrinal (2026-05-09, sacrosanct): *"A PROFILE IS WAY MORE THAN JUST SETTING FOR ONE TOOL"* + *"support but not vendor lock ourself"*. The Profile is the per-project assistant definition; tools come and go around it. If the Profile's shape depends on Claude Agent SDK / Multica / any specific runtime, the operator's investment becomes captive to that vendor's lifecycle. Tool-agnosticism is constitutive of what a Profile IS.

Concrete examples:
- A Profile says "the assistant has copywriting capability" — different tools realize this differently (skill.md, system prompt section, Multica skill, etc.); the Profile doesn't say HOW
- A Profile says "primary model preference is high-capability for synthesis" — the runtime picks the actual model (Claude Opus / Qwen / custom LoRA)
- A Profile says "must have access to the wiki knowledge base" — different tools wire it via MCP / file mount / API; the Profile doesn't specify the wiring mechanism
- A Profile says "cost ceiling $50/month equivalent value" — the runtime tracks consumption in whatever unit its provider uses

## When To Apply

> [!tip] **Project gets a Profile when**
>
> 1. The project has recurring assistance needs (curation, automation, scheduled tasks)
> 2. The needs are project-specific (not generic — generic = no profile needed, ad-hoc tool use suffices)
> 3. The operator wants ecosystem-wide consistency (the multi-project navigability)
> 4. High-quality definitions and features are wanted — Profile is the artifact that captures both

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
