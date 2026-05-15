---
title: "Decision — Strategic response to Anthropic Programmatic Credit Pool (2026-06-15): adopt per-project Assistant Profiles as the value-capture mechanism for the $200/month Max 20x credit"
type: decision
domain: ai-models
status: draft
confidence: high
maturity: seed
created: 2026-05-09
updated: "2026-05-09"
decision_owner: operator
decided: false
sources:
  - id: operator-directive-2026-05-09
    type: directive
    file: raw/notes/2026-05-09-operator-directive-per-project-assistant-configs-spawn-openclaw-openarms-hermess-and-anthropic-programmatic-budget-policy-research.md
    description: "Operator directive 2026-05-09 framing the strategic response — per-project Assistant configurations as the value-capture mechanism"
  - id: policy-synthesis
    type: wiki
    file: wiki/sources/ai-models/src-anthropic-programmatic-credit-pool-policy-change-2026-06-15.md
    description: "Anthropic Programmatic Credit Pool 2026-06-15 policy change — $200/month Max 20x value-at-risk + use-it-or-lose-it forcing function"
  - id: epic-e024
    type: wiki
    file: wiki/backlog/epics/milestone-v2/e024-per-project-assistant-configurations-to-capture-programmatic-credit-and-enable-ecosystem-spawn.md
    description: "Epic E024 — the implementation scope for this decision"
tags: [decision, strategy, anthropic-policy, per-project-assistant, value-capture, "$200-month", max-20x, "2026-06-15", anti-vendor-lock-in-strategic-alignment, "2026-05-09", "draft", ai-models]
---

# Decision — Adopt Per-Project Assistant Profiles as Strategic Response to Anthropic Programmatic Credit Pool

## Summary

In response to Anthropic's 2026-06-15 Programmatic Credit Pool policy — which introduces a $200/month metered, non-rolling credit for Max 20x subscribers for Claude Agent SDK + `claude -p` CLI + GitHub Actions + third-party Agent SDK apps — adopt a strategy of building **per-project Assistant Profiles** (runtime-agnostic configurations, one tailored to each repo) that spawn assistant instances on OpenClaw / OpenArms / Hermess / generic Agent-SDK consumers. Each instance consumes part of the programmatic credit on valuable per-project automation, converting use-it-or-lose-it credit into project value. Beyond credit capture, the Profile design preserves runtime-agnosticism — supporting future routing to local-AI (AICP), other-provider models (Kimi K2.6 via OpenRouter, Ollama Cloud), and custom-tailored model groups — keeping anti-vendor-lock-in mission alignment intact even while consuming Anthropic credit in the short term.

## Context

> [!info] What's forcing the decision
>
> | Element | Value |
> |---|---|
> | **Trigger** | Anthropic 2026-06-15 Programmatic Credit Pool policy (see [[src-anthropic-programmatic-credit-pool-policy-change-2026-06-15|policy synthesis]]) |
> | **Operator subscription** | Max 20x — $200/month programmatic credit allocation |
> | **Use-it-or-lose-it** | Credits reset monthly; expire if unused; $2,400/year value-at-risk |
> | **Operator directive (verbatim)** | *"the goal is to be able to use those [profiles] to spawn an OpenClaw or OpenArms or Hermess and whatever and have high quality definitions and features... so on max x20 its equivalent of 240$ lost if not used with something like such Assistant or our advanced systems which are not finished"* (2026-05-09) |
> | **Time pressure** | Each unused billing cycle after 2026-06-15 loses $200 |
> | **Strategic alignment constraint** | Must NOT violate [[anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence|anti-vendor-lock-in mission]] — profiles must remain runtime-agnostic |
> | **Quality bar** | Operator-stated "high quality definitions and features" — profiles must follow rigorous schema, not improvised configs |

## Decision

**Adopt Per-Project Assistant Profiles as the value-capture mechanism** for Anthropic's 2026-06-15 Programmatic Credit Pool ($200/month at Max 20x). Build one tailored Profile per project (starting with /opt second-brain as the canonical example), spawn runtime-agnostic instances on OpenClaw / OpenArms / Hermess / generic Agent-SDK consumers, and use the spawned instances to consume the programmatic credit on valuable per-project automation. This is Option A from the alternatives below; phased delivery puts Phase 1+2 on track to be operable before 2026-06-15 to start capturing credit on the first billing cycle.

## Alternatives

### Option A — Per-Project Assistant Profiles (RECOMMENDED)

Build one tailored Profile per project; spawn instances on multiple runtimes (OpenClaw, OpenArms, Hermess, generic Agent SDK); each instance consumes programmatic credit on valuable per-project automation.

**Pros**:
- Captures the $200/month credit directly (each spawned instance uses Agent SDK = drains the credit pool)
- Aligns with operator's explicit direction
- Runtime-agnostic — profile portable to non-Anthropic runtimes as alternatives mature
- Scales across the 5-project ecosystem (each project gets its own profile)
- Quality bar is enforceable via schema validation
- Drives operator-level navigation across ecosystem assistants

**Cons**:
- Implementation work required (Epic E024, ~18-24 tasks)
- Time pressure (2026-06-15 effective date — 5 weeks)
- Per-seat credits don't pool — multi-project means operator-level allocation discipline
- Adds complexity vs ad-hoc Claude Code interactive use

### Option B — Accept the value-at-risk

Don't build anything; let the $200/month credit expire each cycle; continue interactive Claude Code use as before.

**Pros**:
- Zero implementation effort
- No additional complexity

**Cons**:
- $2,400/year sunk loss
- No structural value capture — relies on future operator initiatives to recoup
- Misses opportunity to systematize per-project assistant patterns (which the operator wants regardless of credit capture)
- Doesn't address "high quality definitions and features" directive

### Option C — Single mega-profile for all use cases

Build one profile that handles all programmatic automation across all projects.

**Pros**:
- Less authoring overhead than per-project profiles

**Cons**:
- Violates operator-stated *"in the knowledge/information-hub we will have one taillored to the needs"* — operator wants per-project tailoring
- Reduces specialization value (each project has different needs)
- Single-profile architecture is harder to evolve without breaking dependent consumers

### Option D — Build only the runtimes (OpenClaw / OpenArms / Hermess), no profile layer

Skip the profile abstraction; configure each runtime directly per project.

**Pros**:
- Skip schema design

**Cons**:
- Operator explicitly named "configurations / profiles" as the abstraction
- Loses reusability — config in OpenClaw repo not portable to Hermess
- Violates runtime-agnosticism principle

## Recommendation

**Option A — Per-Project Assistant Profiles** with phased delivery:

| Phase | Timeline | Deliverable |
|---|---|---|
| Phase 1 (Document — 2 weeks) | by 2026-05-23 | Profile pattern + schema design + /opt example + strategic decision (this page) + spawn protocol design |
| Phase 2 (Implement — 2 weeks) | by 2026-06-08 | /opt profile authored · 1 spawn protocol operable (generic Agent SDK or OpenClaw) · profile template + scaffold tool |
| Phase 3 (Test — 1 week) | by 2026-06-15 | First Assistant instance spawned · `claude -p` consumption observed against $200 credit (cycle starts 2026-06-15) |
| Phase 4 (Cross-project — ongoing) | 2026-06 → 2026-09 | One profile per sister project (5 projects); spawn protocols for OpenArms, Hermess, etc. |

## Rationale

The recommendation flows from four constraints layered together:

1. **Use-it-or-lose-it asymmetry** (Anthropic policy) — $200/month evaporates if unused; doing nothing = $2,400/year sunk loss
2. **Operator-stated direction** (sacrosanct) — *"the goal is to be able to use those to spawn an OpenClaw or OpenArms or Hermess and whatever and have high quality definitions and features"* — operator explicitly named Profiles as the abstraction
3. **Anti-vendor-lock-in mission** — Profiles must remain runtime-agnostic to preserve future routing to local-AI / other-providers / custom-tailored model groups; this rules out Option D (runtime-coupled config)
4. **Per-project tailoring** — operator-stated *"tailored to the needs"* per project; this rules out Option C (mega-profile)

Phase 1+2 delivery before 2026-06-15 is the recommended cadence because the first billing cycle starting after that date is where credit capture begins; missing it loses $200 on cycle one with no recovery.

## Trade-offs Made Explicit

| Trade-off | Direction | Rationale |
|---|---|---|
| Implementation speed vs design rigor | Lean toward rigor | Operator-stated "high quality definitions and features" |
| Coverage breadth (all projects fast) vs depth (/opt example deep) | Depth-first | /opt as canonical example → projects follow with pattern in hand |
| Runtime support (many runtimes) vs runtime support (one done well) | One-done-well first | Generic Agent SDK + OpenClaw first; OpenArms, Hermess, others follow |
| Profile schema flexibility vs strict validation | Strict validation | Quality bar requires schema enforcement; flexibility added later via versioning |

## Reversibility

**Partially reversible**. The Profile pattern + schema + /opt example are knowledge-layer artifacts that survive even if the strategy pivots — they document the assistant-architecture approach independently of the credit-capture rationale. The runtime-specific spawn protocols are also reusable beyond the Anthropic credit context (they bridge Profile to any Agent-SDK runtime).

**Hard-to-reverse elements**:
- Sister-project profile authoring (M006) commits operator attention across 5 projects — if pivoting, sister profiles may be partial
- Schema versioning policy decisions (T074) lock in early — schema evolution requires migration

**Recovery path if abandoned**:
- Profiles remain valid documentation of project-specific assistance needs (reusable)
- The wider /opt knowledge layer is unaffected
- No deletion of artifacts; status flip to `superseded`

## Dependencies

Beyond Anthropic's policy (which IS the trigger), this decision has soft dependencies:

- **Soft (benefits, not required)**: [[custom-tailored-senior-engineer-tier-model-group-with-recreated-intelligence-layer-research-synthesis|Custom-Tailored Model Group]] — when mature, profiles can route to local models. Decision is independent.
- **Soft (benefits, not required)**: [[root-ghostproxy-sfif-rollout-and-second-brain-integration-2026-05|root-ghostproxy SFIF Rollout]] — harness layer may host spawned instances. Decision is independent.
- **Operator-decision dependency**: D1-D5 (Open Operator Decisions below) — some block specific modules but not the overall direction.

## Constraints

- **Operator-territory items** (not /opt scope):
  - Hermess identity clarification (operator-decision)
  - Max plan tier confirmation (operator-decision)
  - Actual spawning + running of Assistants (runtime-territory, lives in runtime repos)
  - Credit pool monitoring at Anthropic billing dashboard (operator-territory)
- **/opt scope** (this Epic's work):
  - Profile schema + pattern
  - /opt tailored profile (the canonical example)
  - Spawn protocols (the bridge from profile to runtime — documentation)
  - Cross-project profile catalog (the navigation layer)
  - Strategic decisions (this page + future decisions)
- **Don't conflate** the Profile (declarative config) with the Assistant (running instance) — different layers.

## Open Operator Decisions

| # | Decision | Block on | Recommendation |
|---|---|---|---|
| **D1** | Hermess clarification — typo for Hermes, or new project name? | M004 + M006 in E024 | Operator-clarify; if new project, add to `sister-projects.yaml` |
| **D2** | Plan tier confirmation — Max 5x or Max 20x? ($100 or $200) | Sizing the value-capture mechanism | Confirm Max 20x ($200/month) per the operator's 2026-05-09 directive context |
| **D3** | Timeline pressure — should Phase 1+2 hit 2026-06-15 effective date? | Implementation pacing | Recommendation: YES if value-capture matters short-term; flex if other priorities (root-ghostproxy + AVX512) take precedence |
| **D4** | Quality bar specifics — concrete success criteria beyond "schema passes" | Profile validation rules | Suggested: profile passes `pipeline post`; spawn protocol produces runnable instance; instance has measurable per-month value-output |
| **D5** | Multi-seat operator handling — single seat or multiple seats? | Credit allocation strategy | Per Anthropic policy, credits per-seat with no pooling; if multi-seat, allocate each seat to specific project(s) |

## Relationships

- IMPLEMENTS: [[2026-05-09-operator-directive-per-project-assistant-configs-spawn-openclaw-openarms-hermess-and-anthropic-programmatic-budget-policy-research|Operator directive 2026-05-09]]
- BUILDS ON: [[src-anthropic-programmatic-credit-pool-policy-change-2026-06-15|Anthropic Programmatic Credit Pool Policy Synthesis]]
- ENABLES: [[E024 — Per-Project Assistant Configurations]]
- DEMONSTRATES: [[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4 — Declarations Aspirational Until Verified]] — operator's $240 framed as verified-against $200 actual; this decision reflects the verified figure
- COMPLEMENTS: [[anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence|Lesson — Anti-Vendor-Lock-In as empirical claim]] — runtime-agnosticism preserves mission alignment
- CONSTRAINED BY: Anthropic policy effective date 2026-06-15 (time-box)

## Backlinks

[[Operator directive 2026-05-09]]
[[Anthropic Programmatic Credit Pool Policy Synthesis]]
[[E024 — Per-Project Assistant Configurations]]
[[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4 — Declarations Aspirational Until Verified]]
[[Lesson — Anti-Vendor-Lock-In as empirical claim]]
[[Anthropic policy effective date 2026-06-15 (time-box)]]
