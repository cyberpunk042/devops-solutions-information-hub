---
title: "E024 — Per-Project Assistant Configurations to Capture Programmatic Credit & Enable Ecosystem-Project Spawn (OpenClaw / OpenArms / Hermes)"
type: epic
domain: backlog
status: draft
priority: P1
task_type: epic
current_stage: document
readiness: 15
progress: 0
stages_completed: []
artifacts:
  - wiki/sources/ai-models/src-anthropic-programmatic-credit-pool-policy-change-2026-06-15.md
  - raw/notes/2026-05-09-operator-directive-per-project-assistant-configs-spawn-openclaw-openarms-hermess-and-anthropic-programmatic-budget-policy-research.md
confidence: high
created: 2026-05-09
updated: "2026-05-09"
sources:
  - id: operator-directive-2026-05-09
    type: directive
    file: raw/notes/2026-05-09-operator-directive-per-project-assistant-configs-spawn-openclaw-openarms-hermess-and-anthropic-programmatic-budget-policy-research.md
    description: "Operator-stated 2026-05-09 directive — per-project assistant configurations/profiles to spawn OpenClaw/OpenArms/Hermes; capture programmatic credit budget; high quality definitions and features"
  - id: anthropic-policy-synthesis
    type: wiki
    file: wiki/sources/ai-models/src-anthropic-programmatic-credit-pool-policy-change-2026-06-15.md
    description: "Anthropic Programmatic Credit Pool 2026-06-15 policy change — confirms $200/month value-at-risk on Max 20x; defines the credit pool the per-project Assistants will consume"
tags: [epic, "E024", per-project-assistant, assistant-profile, openclaw, openarms, hermess, programmatic-credit-capture, anthropic-policy-response, "2026-05-09", "2026-06-15-deadline", value-capture, ecosystem-spawn, P1, milestone-v2, "draft"]
---

# E024 — Per-Project Assistant Configurations to Capture Programmatic Credit & Enable Ecosystem-Project Spawn

## Summary

Build per-project assistant configurations / profiles — one per repo, tailored to each project's needs — that are runtime-agnostic enough to spawn assistant instances on OpenClaw, OpenArms, Hermes (Greek messenger god — operator-confirmed 2026-05-09), or any future Agent-SDK-compatible harness. The strategic context is **time-boxed**: Anthropic's new programmatic credit pool (effective 2026-06-15) provides $200/month at Max 20x that **does not roll over** — making proactive value-capture via per-project Assistants a $2,400/year forcing function for the operator. Beyond the value-capture frame, the architecture serves the broader anti-vendor-lock-in mission: profiles are runtime-agnostic, enabling future routing to local-AI subsystems (AICP), other-provider models (Kimi K2.6, Ollama Cloud), and custom-tailored model groups as those alternatives mature.

## Operator Directive

> "Now repos / projects will have assistants configurations / profiles.. e.g. in the knowledge/information-hub we will have one taillored to the needs. the goal is to be able to use those to spawn an OpenClaw or OpenArms or Hermes and whatever and have high quality definitions and features."

> "I think Anthropic changed that the -p option which was our workaround to not be treated as programmatical is now counted as programmatic use and now also considered credit budget but at the same time now they would give each month the equivalent of the month of budget in token for the programmatic uses ? I think thats what I read. so on max x20 its equivalent of 240$ lost if not used with something like such Assistant or our advanced systems which are not finished."

> "but we can confirm all that, do our research. record what I said, plan what is needed and create all the neeed tasks, Epics and documents."

*— Operator directive 2026-05-09; full verbatim + decomposition in [[2026-05-09-operator-directive-per-project-assistant-configs-spawn-openclaw-openarms-hermess-and-anthropic-programmatic-budget-policy-research|raw note]].*

**Research confirmed** (see [[src-anthropic-programmatic-credit-pool-policy-change-2026-06-15|policy synthesis]]):
- ✅ `claude -p` flag now classified as programmatic use (effective 2026-06-15)
- ✅ Programmatic use has separate metered credit pool at API rates
- ✅ Monthly credit per plan: Pro $20, Max 5x $100, Max 20x $200 (operator said $240 — actual is $200; small discrepancy)
- ✅ Use-it-or-lose-it (no roll-over)
- ✅ Covers Claude Agent SDK, `claude -p`, GitHub Actions, third-party Agent SDK apps (incl. OpenClaw)

## Goals

- **Per-project Assistant Profile schema** — runtime-agnostic format defining assistant identity, knowledge scope, allowed/forbidden actions, model preferences, MCP wiring, prompt templates, success criteria. One schema, many instances.
- **/opt second-brain Assistant Profile** — the tailored example for THIS project (knowledge curation, methodology stewardship, source ingestion, lesson distillation, gateway-driven orientation). Demonstrates the schema by exemplary instance.
- **Spawn protocols per runtime** — concrete instructions for how a Profile materializes as a running instance on OpenClaw / OpenArms / Hermes / generic Agent-SDK consumer. Each runtime has its conventions; the spawn protocol bridges Profile → runtime.
- **Programmatic credit budget allocation strategy** — decide how to consume the $200/month Max 20x credit across projects (each project's share; cross-project pooling not supported by Anthropic so cannot be done at the credit layer; pool at the operator-decision layer).
- **Cross-project Profile catalog** — once /opt's profile is exemplary, each sister project (OpenArms, OpenFleet, AICP, devops-control-plane, root-ghostproxy) gets its own tailored Profile. The catalog enables operator-level navigation.
- **Quality bar enforcement** — "high quality definitions and features" per operator. Profiles must have specific structural sections (identity, knowledge scope, action surface, model routing, success criteria); validators enforce.

## Done When

- [ ] `wiki/sources/ai-models/src-anthropic-programmatic-credit-pool-policy-change-2026-06-15.md` exists and passes `pipeline post` with 0 errors (research evidence)
- [ ] `wiki/decisions/01_drafts/strategic-response-to-anthropic-programmatic-credit-pool-via-per-project-assistant-profiles.md` exists with operator approval (strategy decision)
- [ ] `wiki/patterns/01_drafts/per-project-assistant-profile-pattern-tailored-config-to-spawn-ecosystem-runtimes.md` exists with schema definition (pattern)
- [ ] `wiki/config/templates/assistant-profile.md` template exists (operationalizes the pattern)
- [ ] `wiki/concepts/opt-second-brain-assistant-profile.md` (or domain-overview placement) exists — the tailored /opt example
- [ ] At least 3 spawn protocol pages: `wiki/patterns/01_drafts/spawn-protocol-{openclaw,openarms,generic-agent-sdk}.md`
- [ ] Operator confirms "Hermes" identity — typo for Hermes, or new project name; if new, add to `wiki/config/sister-projects.yaml`
- [ ] All 6 sister projects have draft assistant profiles in `wiki/concepts/sister-project-profiles/` (one per project)
- [ ] Cost-tracking pattern documented (treat Claude credit like AWS/GCP per InfoWorld synthesis)
- [ ] Pipeline post returns 0 errors after all changes
- [ ] Operator confirms deliverables are findable (discoverability test)

## Scale and Model

> [!info] Epic Parameters
>
> | Parameter | Value |
> |-----------|-------|
> | **Model** | feature-development (5 stages: document → design → scaffold → implement → test) |
> | **Quality tier** | Skyscraper (operator-specified "high quality definitions and features") |
> | **Estimated modules** | 6 |
> | **Estimated tasks** | ~18-24 |
> | **Dependencies** | None blocking; benefits from Custom-Tailored Model Group + AVX512 plan + root-ghostproxy maturation but does not require them |
> | **Time-box constraint** | 2026-06-15 effective date for Anthropic credit pool — Profile + spawn protocol minimum-viable should be operable before this date to start capturing $200/month |
> | **Identity** | type=system, domain=ai-agents + cross-domain (Profile schema), backlog (this Epic) |

## Stage Artifacts (per feature-development methodology)

> [!abstract] Stage → Artifact Map
>
> | Stage | Required Artifacts | Status |
> |-------|--------------------|--------|
> | **Document** | Research synthesis (Anthropic policy) · Directive log · This Epic · Strategic decision page · Profile pattern page | ✅ Mostly done (this turn) |
> | **Design** | Profile schema (formal) · Spawn protocol per runtime · /opt profile design · Credit allocation strategy · Cross-project profile design | Pending |
> | **Scaffold** | `wiki/config/templates/assistant-profile.md` · Profile scaffold script (`pipeline scaffold assistant-profile`) · Profile validator (`pipeline post` extension) | Pending |
> | **Implement** | /opt profile authored · Sister-project profiles authored · Spawn protocols documented · Profile catalog page | Pending |
> | **Test** | Profile validates · Spawn protocol runnable on OpenClaw test · `claude -p` consumption observed against $200 credit | Pending (requires 2026-06-15 effective date for `claude -p` consumption test) |

## Module Breakdown

| Module ID | Module | Delivers | Est. Tasks |
|---|---|---|---|
| **E024-M001** | Anthropic Policy Synthesis | Research-confirmed source-synthesis page; clarifies the credit pool mechanics + value-at-risk | ✅ done this turn (1 task) |
| **E024-M002** | Per-Project Assistant Profile Pattern + Schema | Pattern page defining the Profile schema (identity, knowledge scope, action surface, model routing, success criteria); operator-reviewable schema | 3-4 tasks |
| **E024-M003** | /opt Second-Brain Assistant Profile (the tailored example) | The tailored profile for /opt — knowledge curation, methodology stewardship, source ingestion, lesson distillation; demonstrates schema by exemplary instance | 2-3 tasks |
| **E024-M004** | Spawn Protocols per Runtime | Pattern pages for spawn-on-OpenClaw, spawn-on-OpenArms, spawn-on-Hermes (pending clarification), spawn-on-generic-Agent-SDK; bridges Profile → runtime | 4 tasks |
| **E024-M005** | Strategic Decision + Credit Budget Allocation | Decision page on the strategic response to Anthropic policy + how to allocate the $200/month across projects + cost-tracking pattern | 2-3 tasks |
| **E024-M006** | Cross-Project Profile Catalog | One profile per sister project (OpenArms, OpenFleet, AICP, devops-control-plane, root-ghostproxy, Hermes) + catalog page enabling operator navigation | 6 tasks |

## Dependencies

- **None blocking** — all 6 modules can be authored at /opt without external dependencies
- **Benefits from but does not require**:
  - [[custom-tailored-senior-engineer-tier-model-group-with-recreated-intelligence-layer-research-synthesis|Custom-Tailored Model Group]] — once mature, profiles can route to local models instead of Claude
  - [[root-ghostproxy-sfif-rollout-and-second-brain-integration-2026-05|root-ghostproxy SFIF rollout]] — harness propagation provides the runtime layer that consumes profiles
  - [[post-anthropic-stack-3-layer-assembly-multica-aicp-3090|Post-Anthropic 3-Layer Stack]] — alternative provider routing supports profile-driven runtime selection

## Open Questions

> [!success] **Hermes identity — RESOLVED 2026-05-09** — Operator clarified: Hermes (Greek messenger god). The original "Hermess" in the verbatim directive was a typo. M004 spawn-protocol-hermes + M006 sister-project-profile-hermes unblocked. Open: should Hermes be added to `wiki/config/sister-projects.yaml`? (Depends on whether the project repo exists yet — operator decision.)

> [!question] **Plan tier confirmation** — Operator said "max x20" with $240 value claim. Research confirms actual Max 20x = $200/month. Confirm operator is on Max 20x (not 5x).

> [!question] **Cross-project credit pool** — Anthropic does NOT allow pooling credits across team seats. If operator has multiple seats (e.g., one per project), each seat has its own $200/month — pooling happens at the operator-decision layer (which project's automation consumes which seat's credit). If single-seat operator, the $200/month must be split conceptually but is a single credit pool technically.

> [!question] **2026-06-15 effective-date readiness** — Should the M002 Profile pattern + M003 /opt profile + at least one spawn protocol (M004) be ready by 2026-06-15 to start capturing credit immediately? If yes, that's a ~5-week timeline — operator decision.

> [!question] **Quality bar definition** — Operator-stated "high quality definitions and features". Concrete quality criteria? Suggested: profile passes `pipeline post`; profile uses schema-required sections (identity, scope, surface, routing, criteria); spawn protocol produces runnable instance; instance demonstrably consumes < $200/month with measurable value-output.

## Anti-Patterns to Avoid

| Anti-pattern | Why bad |
|---|---|
| Build the runtime (OpenClaw/OpenArms/Hermes code) at /opt | /opt = knowledge; runtimes live in their own repos. /opt produces the **profile** + **spawn protocol**; the runtime CONSUMES |
| Conflate Profile (configuration artifact) with Assistant (running instance) | Profile is the spec; Assistant is the spawned process. Schema discipline matters |
| Build a single mega-profile for all projects | Operator said "one tailored to the needs" per project. One profile per project — each tailored |
| Defer to 2026-06-15+ to start capturing credit | Use-it-or-lose-it begins billing-cycle-after-2026-06-15. Each unused month = $200 expired |
| Tightly couple Profile schema to Claude Agent SDK | Profile must be runtime-agnostic — also spawnable on Ollama / local models / future harnesses per the anti-vendor-lock-in mission |

## Relationships

- IMPLEMENTS: [[2026-05-09-operator-directive-per-project-assistant-configs-spawn-openclaw-openarms-hermess-and-anthropic-programmatic-budget-policy-research|Operator directive 2026-05-09 turn 1]]
- IMPLEMENTS: [[2026-05-09-operator-directive-hermes-clarification-information-surfacing-before-public-obsidian-pull-from-frontier-stay-independent-classify-existing-approaches|Operator directive 2026-05-09 turn 2]] — frontier-pulling + classify-existing-approaches + Hermes clarification (Hermes confirmed as real CLI per Multica evidence)
- BUILDS ON: [[src-anthropic-programmatic-credit-pool-policy-change-2026-06-15|Anthropic Programmatic Credit Pool Policy Synthesis]] — the research evidence + value-at-risk frame
- BUILDS ON: [[assistant-platforms-and-frameworks-frontier-comparison-claude-os-obsidian-pm-multica-openclaw-command-center-2026-05-09|Comparison — Assistant Platforms & Frameworks Frontier]] — empirical inputs from Claude OS / Obsidian PM / Multica / OCMC; Hermes confirmed as real agent-CLI runtime via Multica's supported-CLI list
- BUILDS ON: [[declarative-agent-programming-spectrum-five-layers-spec-skill-context-hook-harness-unified-and-integration-matrix-across-tools|Concept — Declarative Agent Programming Spectrum]] — the foundational synthesis unifying SDD · Skills · Context/Context-Injection · Hooks · Harness across all tools (Claude OS · Multica · OpenClaw · Claude Code · OpenCode · Hermes · Codex · Gemini). Profile compiles all 5 layers into one runtime-agnostic spec.
- COMPLEMENTS: [[anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence|Lesson — Anti-Vendor-Lock-In as empirical claim]] — Profile design preserves runtime-agnosticism, supporting future routing to non-Anthropic
- COMPLEMENTS: [[post-anthropic-self-autonomous-stack|Milestone — Post-Anthropic Self-Autonomous Stack]] — strategic alignment with reducing Anthropic dependency
- RELATES TO: [[custom-tailored-senior-engineer-tier-model-group-with-recreated-intelligence-layer-research-synthesis|Custom-Tailored Model Group Concept]] — Profile-driven routing can target this once it crystallizes
- RELATES TO: [[root-ghostproxy-sfif-rollout-and-second-brain-integration-2026-05|root-ghostproxy SFIF Rollout]] — harness layer that may host spawned Assistants

## Backlinks

[[Operator directive 2026-05-09 turn 1]]
[[Operator directive 2026-05-09 turn 2]]
[[Anthropic Programmatic Credit Pool Policy Synthesis]]
[[Comparison — Assistant Platforms & Frameworks Frontier]]
[[Concept — Declarative Agent Programming Spectrum]]
[[Lesson — Anti-Vendor-Lock-In as empirical claim]]
[[Milestone — Post-Anthropic Self-Autonomous Stack]]
[[custom-tailored-senior-engineer-tier-model-group-with-recreated-intelligence-layer-research-synthesis|Custom-Tailored Model Group Concept]]
[[root-ghostproxy SFIF Rollout]]
