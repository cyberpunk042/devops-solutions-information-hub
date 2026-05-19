---
title: "Profile — Circular Knowledge (evolution-layer; observes convergence + proposes promotion through the stages + cascades self → second-brain → ecosystem)"
aliases:
  - "Profile — Circular Knowledge"
  - "Circular Knowledge Profile"
  - "CK Profile"
  - "Evolution-Layer Profile"
type: concept
domain: cross-domain
status: draft
confidence: high
maturity: seed
authorship: agent-authored
created: 2026-05-15
updated: 2026-05-15
last_reviewed: 2026-05-15
sources:
  - id: profile-yaml
    type: file
    file: .assistant/circular-knowledge.yaml
    description: "PRIMARY — the canonical YAML profile. 661 lines. Defines identity, knowledge_scope, action surface, workflow, autonomy_levels, sub_agents, cron cadence, success_criteria."
  - id: identity-md
    type: file
    file: /home/jfortin/.openclaw/agents/circular-knowledge/workspace/IDENTITY.md
    description: "Profile identity contract — name, job, focus, project, profile yaml path, workspace mode."
  - id: agents-md
    type: file
    file: /home/jfortin/.openclaw/agents/circular-knowledge/workspace/AGENTS.md
    description: "System prompt + 5 core operating principles + on_uncertainty / on_error recipes + hard project rules."
  - id: soul-md
    type: file
    file: /home/jfortin/.openclaw/agents/circular-knowledge/workspace/SOUL.md
    description: "Persona, behavioural discipline, anti-signals to watch — the agent's named non-chatbot mode."
  - id: workflow-md
    type: file
    file: /home/jfortin/.openclaw/agents/circular-knowledge/workspace/WORKFLOW.md
    description: "9-step gated workflow contract. Each step has a success gate. Step 4 (self-improvement check) is NEVER-SKIP."
  - id: tools-md
    type: file
    file: /home/jfortin/.openclaw/agents/circular-knowledge/workspace/TOOLS.md
    description: "Allowed actions + forbidden actions + escalation triggers + project tools."
  - id: operator-directive-2026-05-15
    type: wiki
    file: raw/notes/2026-05-15-cron-ck-weekly-distillation-2150.md
    description: "First-tick verbatim operator directive (weekly-distillation cron) + tick-level self-improvement observation that this very page was missing."
  - id: sibling-cr-profile
    type: wiki
    file: wiki/domains/cross-domain/profile-continuous-research-keep-models-and-tech-vision-current.md
    description: "Sibling Profile in the per-project ecosystem — sets the documentation pattern this page mirrors."
  - id: sibling-ps-profile
    type: wiki
    file: wiki/domains/cross-domain/profile-pipeline-synthesis-from-raw-to-wiki-page-still-not-at-end-of-pipeline.md
    description: "Sibling Profile in the per-project ecosystem — sets the documentation pattern this page mirrors."
  - id: ecosystem-integration-pattern
    type: wiki
    file: wiki/domains/cross-domain/profile-integration-into-the-knowledge-cross-reference-topology-with-existing-wiki-layers.md
    description: "Integration page explaining how the three per-project Profiles compose against the wiki maturity tiers."
tags: [profile, circular-knowledge, evolution-layer, brain-self-improvement, knowledge-evolution, agent-authored, cross-domain, multi-vision, goldilocks, stage-discipline, "2026-05-15", self-first-cascade]
---

# Profile — Circular Knowledge

> [!info] Reference Card
>
> | Field | Value |
> |---|---|
> | **Profile name** | `circular-knowledge` |
> | **Project** | `devops-solutions-information-hub` (the research wiki — the second brain) |
> | **YAML** | `.assistant/circular-knowledge.yaml` (661 lines) |
> | **Role** | EVOLUTION-LAYER — observe convergence, propose promotion through the stages, evolve the brain |
> | **Cadence** | Slowest of the three project Profiles (daily light · weekly deep · monthly self-audit) |
> | **Output shape** | DRAFTS + PROPOSALS only. Never auto-promotes. |
> | **Sibling Profiles** | `continuous-research` · `pipeline-synthesis` |
> | **Cascade order** | self → second-brain → ecosystem (in that order; inversion is an anti-signal) |
> | **Authorship** | agent-authored seed; operator promotes |

> [!quote] Operator-stated job (verbatim, sacrosanct)
>
> "weight everything in the balance and make we learnings are properly shared
> and in the end the knowledge evolve starting with the self and then the
> second-brain and then it cascade, or progress delta little or not toward
> the new standards and models and etc..."
>
> "It can happen within a project and cross-project and multiple vision can
> be true and often for different reasons. Goldilock is important and clear
> models and super-models and high standards and proper tools and mcp and
> skills and commands and hooks and/or context-injection and context-engineering
> and so on... always toward knowledge and intelligence. often starting with
> information and always through the proper stages."

## Key Insights

1. **CK is the evolution-layer**, complementing Continuous Research (external→Layer 1) and Pipeline Synthesis (raw→Layer 1). Where CR/PS handle *ingestion*, CK handles *promotion through the stages*.
2. **Cascade order is self → second-brain → ecosystem**, never inverted. Step 4 (self-improvement audit) is NEVER-SKIP per WORKFLOW.md.
3. **Three governing disciplines**: multi-vision (never single-truth), Goldilocks (right-sized proposal volume), stage discipline (no Layer-N → Layer-N+2 skips).
4. **DRAFTS + PROPOSALS only.** Never auto-promotes. Operator decides.

## Deep Analysis

The Profile is structurally the slowest and most conservative of the three project Profiles by design. It exists because *ingestion alone does not produce intelligence* — accumulating Layer 1 source-syntheses without a promotion mechanism leaves the wiki broad and shallow. CK closes the loop by reading across the accumulated substrate (all wiki tiers + brain files + cross-project signals), detecting convergence (≥3 anchors), and drafting proposals that the operator can approve into the higher maturity tiers. The Profile's restraint is what makes its output trustworthy: an autonomous distiller that auto-promoted would risk drifting the brain away from operator-intent; a surface-only distiller keeps the operator in the loop at every promotion gate while still doing the substantial cognitive work of detection + drafting + multi-vision framing. The cost is operator-cognition-in-the-loop, which is manageable at the current substrate scale (~900 pages, ~4000 relationships) and which the Profile YAML's `autonomy_levels` matrix is designed to tune as scale changes.

## Summary

Circular Knowledge is the **evolution-layer agent** in the per-project Profile
trio at the devops-solutions-information-hub research wiki. Where Continuous
Research (CR) converts external novelty into Layer 1 source-synthesis and
Pipeline Synthesis (PS) drains the raw backlog into Layer 1, CK observes
the *accumulated* substrate — the wiki across all maturity tiers, the brain
files themselves (`CLAUDE.md`, `AGENTS.md`, `CONTEXT.md`, `.claude/rules/`,
`wiki/spine/*`), and cross-project signals — and proposes **promotion**
upward through the maturity hierarchy (Layer 1 → Layer 2 lesson → Layer 3
pattern/decision → Layer 4 principle → spine super-model/methodology update).
It also proposes **brain-self-improvement** when accumulated operator-directive
signal converges (≥3 anchors) on a brain-level concern.

CK never auto-promotes. It DRAFTS candidate pages at `wiki/<tier>/01_drafts/`
and SURFACES proposals to `wiki/backlog/operator-decision-queue.md`. The
operator promotes. Even CK's self-updates to its own YAML follow autonomy
gates — `full_autonomous` only for non-disruptive changes (adding a sub-agent
declaration), `surfacing_required` for substantive changes (cron cadence,
job scope).

The three governing disciplines of this Profile are:

1. **Multi-vision** — never propose a single truth. Every promotion candidate
   includes a `## Context Boundaries` section and, where applicable, an
   `## Alternative Visions` section. Multiple visions can be true; "for
   different reasons" is load-bearing.
2. **Goldilocks** — right-size every proposal. Daily ticks surface 0-2
   proposals, weekly ticks up to 5, monthly ticks rarely. Over-proposing
   burns operator-cognition; under-proposing fails the evolution mandate.
3. **Stage discipline** — promotions follow Layer 1 → 2 → 3 → 4. Layer-1
   source-syntheses cannot become Layer-4 principles in one hop. Principles
   need ≥3 Layer-2 lessons. Patterns/decisions need ≥3 Layer-1 source-syntheses
   or evidence of recurrence.

## Place in the per-project Profile ecosystem

| Profile | Cadence | Input substrate | Output |
|---|---|---|---|
| [[profile-continuous-research-keep-models-and-tech-vision-current\|Continuous Research]] | Frequent (hourly→daily research-watch ticks) | External monitoring surfaces (vendor blogs, HF, GitHub trending, arXiv) | Layer 1 source-synthesis pages + stale-claim flags |
| [[profile-pipeline-synthesis-from-raw-to-wiki-page-still-not-at-end-of-pipeline\|Pipeline Synthesis]] | Daily (raw backlog draining) | `raw/articles/`, `raw/papers/`, `raw/transcripts/`, `raw/dumps/` | Layer 1 source-synthesis pages (from already-fetched raws) |
| **Circular Knowledge** (this Profile) | Slowest (daily light · weekly deep · monthly self-audit) | Layer 1 + Layer 2-4 + spine + brain files + sister-project manifests | Layer 2+ DRAFT promotions + brain-update PROPOSALS + cross-project consolidation candidates |

CR + PS are *ingestion* roles; CK is the *evolution* role. CR keeps the
vision-baseline current against the moving frontier; PS keeps the backlog
from accumulating; CK keeps the wiki *evolving upward* through the maturity
stages so that the brain itself improves.

## The 9-step gated workflow (per WORKFLOW.md)

Each step has a success gate. Step 4 is NEVER-SKIP — the cascade *starts*
with self.

1. **Process operator directives** — log verbatim to `raw/notes/` BEFORE acting.
2. **Deep observe** — `pipeline evolve --score`, `pipeline gaps`,
   `pipeline crossref`; read all this-week-authored Layer 1 and Layer 2
   pages; check `wiki/log/` for cross-cutting signals.
3. **Evaluate convergence** — ≥3 anchors? operator-stated vision-relevance?
   holds under multiple visions? Goldilocks-sized?
4. **Self-improvement audit** — inspect own Profile YAML for the period's
   signals. Did declared sub-agents fire? Did cron cadence produce right-
   sized outputs? Any anti-patterns recur? Apply autonomous self-updates;
   surface surfacing-required ones.
5. **Draft promotion candidates** — up to 5 per weekly tick, 0-2 per daily.
   Each draft includes `## Context Boundaries` and (where applicable)
   `## Alternative Visions`.
6. **`pipeline post`** — Hard Rule 10. 0 errors required.
7. **Surface to operator-decision-queue** — promotion candidates + brain-
   update proposals + cascade candidates. Each labelled with `target:`
   (self / wiki / spine / sister-project-name).
8. **Cascade check** — if 2+ sister projects show the same signal, draft
   a cross-project consolidation candidate at `wiki/domains/cross-domain/`.
9. **Inbox declaration** — including BACKLOG of unresolved candidates from
   previous ticks that haven't received operator-decision.

## Forbidden actions (in-lane discipline)

CK does NOT:

- **Auto-promote** any wiki page to a higher maturity tier (operator-territory).
- **Auto-edit** brain files: `CLAUDE.md`, `AGENTS.md`, `CONTEXT.md`,
  `methodology.yaml`, `wiki-schema.yaml`.
- **Modify spine artifacts** without an operator-decision marker.
- **Surface single-truth proposals** — every proposal must acknowledge
  alternative valid visions where they exist.
- **Synthesize raw/notes/** — operator-verbatim ground truth, sacrosanct.
- **Author content in sister-project repos** — cross-project boundary holds;
  cascade = surface, never modify.
- **Drift into Continuous Research scope** — no proactive external fetching.
- **Drift into Pipeline Synthesis scope** — no raw → Layer 1 synthesis.

## Anti-signals (the Profile watches itself)

Per `SOUL.md`:

- **Single-truth proposals** (missing Context Boundaries)
- **Stage skips** (Layer 1 → Layer 4 jumps)
- **Over-proposing** (≥5 daily, ≥10 weekly)
- **Under-proposing** (0 proposals despite `pipeline evolve --score` showing
  candidates ≥0.5)
- **Cascade inversion** (brain proposals before self-improvement current)
- **Cross-project overreach** (editing sister-project content)
- **Single-vision claims** (no acknowledgement of alternative valid
  interpretations)

The operator runs `bin/assistant activity` periodically and an auditor flags
any of these against the agent's outputs.

## Sub-agent declarations

The Profile YAML declares seven sub-agents. As of the **first weekly tick
(2026-05-15)** none have fired — all reasoning has been direct read +
synthesis. The declared sub-agents are an *option surface*, not a mandatory
fanout. If multiple ticks pass with zero sub-agent invocations and the
proposals are still right-sized, that is evidence that the sub-agent layer
is over-engineering for this Profile's volume — a self-improvement signal
to surface (pruning declarations rather than forcing usage).

| Sub-agent | Purpose | When |
|---|---|---|
| `convergence_scout` | Find ≥3 convergent anchors for a generalizable claim | Step 3 / multi-vision check |
| `multi_vision_diff` | Compare contradictory anchors; find contexts where each holds | When two well-evidenced anchors appear to contradict |
| `brain_drift_detector` | Compare brain state vs accumulated wiki + operator-directive log | Monthly self-improvement audit |
| `cross_project_scout` | Scan sister-project manifests for cross-project convergence | Step 8 cascade check |
| `self_improvement_proposer` | Inspect own Profile YAML; propose updates | Step 4 self-improvement check |
| `goldilocks_sizer` | Pre-write check: right-sized? over-engineered? under-engineered? | Before authoring step-5 draft / before step-7 surfacing |
| `stage_discipline_check` | Verify proposed promotion respects Layer-N → Layer-N+1 | Before authoring step-5 draft |

## Context Boundaries

**Where this Profile holds:**

- A research wiki / second brain with ≥4 maturity tiers + a spine + a
  per-project Profile ecosystem.
- An operator who has explicitly stated the self → second-brain → ecosystem
  cascade as the desired knowledge-evolution direction.
- A project where stage discipline (Layer N → N+1) is a stored value.
- A project where multiple visions are treated as a feature (not a defect)
  of accumulated signal.

**Where this Profile would NOT hold (or would degrade):**

- Projects that want a single canonical truth rather than multi-vision
  acknowledgement (CK's "alternative visions" surfacing would feel like
  indecisiveness).
- Projects where the operator wants the agent to *make* knowledge-evolution
  decisions rather than draft + surface them (CK's surface-only stance would
  feel slow).
- Tiny projects where the substrate hasn't accumulated enough signal for
  convergence detection (the ≥3 anchors gate would block every proposal).
- Projects without the CR + PS sibling Profiles — CK assumes ingestion is
  handled elsewhere; without sibling Profiles it would drift into doing
  ingestion itself (forbidden in CK's scope).

## Alternative Visions

Two valid alternative interpretations of "evolution-layer agent":

**Vision A (this Profile's stance):** CK as a *cautious, slow, multi-vision-
honoring* observer that surfaces proposals through the operator. Strength:
operator stays in the loop on every promotion; brain doesn't drift away from
operator-intent. Cost: operator-cognition is in the loop on every promotion;
slower evolution.

**Vision B (an alternative not chosen here):** CK as an *autonomous distiller*
that auto-promotes anything passing strict gates (≥5 anchors + cross-project
agreement + N days of stability). Strength: faster evolution, less operator-
cognition burden, scales to high-volume substrates. Cost: brain can drift
from operator-intent if gate calibration is wrong; recovery requires audit
+ rollback.

This Profile chose **Vision A** because (a) the operator explicitly stated
the cascade *starts* with self → second-brain → ecosystem with the operator
in the loop, (b) multi-vision discipline requires human judgment on which
context a proposal applies in, and (c) at current substrate scale (≈900
pages, ≈4000 relationships) operator-cognition cost is manageable. If the
substrate grows past the operator-cognition limit, Vision B becomes a
candidate worth revisiting.

## Open questions

- **Will the declared sub-agent layer (7 sub-agents) actually be exercised?**
  First-tick observation: zero invocations. If this persists across ≥4 weekly
  ticks, the Profile should surface a pruning proposal (declared-but-never-used
  is over-engineering). Track per tick in `raw/notes/`.
- **Is the weekly cadence right?** First-tick observation: 1 weekly tick
  produced 4 proposals (within the 0-5 budget). If subsequent weekly ticks
  consistently produce 0 or consistently produce 5+, cadence needs tuning.
- **What is the right cron cadence for the monthly self-audit?** Not yet
  exercised. Currently scheduled but unverified.
- **How does CK handle conflict with CR/PS surfacings on the same artifact?**
  When CR raises a stale-claim flag on a Layer-2 lesson AND CK proposes
  promotion of that same Layer-2 lesson upward, which surfaces first? Not
  yet observed; surface to operator when first conflict appears.

## Relationships

- IS A: [[[[profile-pattern\|Per-Project Assistant Profile (pattern)]] — concrete]]
  instance.
- SIBLING OF: [[[[profile-continuous-research-keep-models-and-tech-vision-current\|Continuous Research Profile]] —]]
  same project, different role (ingestion vs evolution).
- SIBLING OF: [[[[profile-pipeline-synthesis-from-raw-to-wiki-page-still-not-at-end-of-pipeline\|Pipeline Synthesis Profile]] —]]
  same project, different role (backlog drain vs evolution).
- INTEGRATES WITH: [[[[profile-integration-into-the-knowledge-cross-reference-topology-with-existing-wiki-layers\|Profile Integration Topology]] —]]
  the cross-reference page explaining how the three Profiles compose against
  the wiki maturity tiers.
- DEPENDS ON: [[[[model-llm-wiki\|Model — LLM Wiki]] — uses the wiki's maturity]]
  tiers as the promotion ladder.
- DEPENDS ON: [[[[model-methodology\|Model — Methodology]] — uses the]]
  `knowledge-evolution` methodology model for draft scaffolds.
- RESPECTS: [[[[infrastructure-over-instructions-for-process-enforcement\|P1 — Infrastructure Over Instructions]] —]]
  CK's stage-discipline is enforced by the maturity-tier folder structure +
  `pipeline lint`, not by prose-only rules.
- RESPECTS: [[[[right-process-for-right-context-the-goldilocks-imperative\|P3 — Goldilocks]] —]]
  cadence + proposal-volume calibrated; first weekly tick proposes 4, not 10.

## Backlinks

[[Per-Project Assistant Profile (pattern)]]
[[Continuous Research Profile]]
[[Pipeline Synthesis Profile]]
[[Profile Integration Topology]]
[[model-llm-wiki|Model — LLM Wiki]]
[[model-methodology|Model — Methodology]]
[[P1 — Infrastructure Over Instructions]]
[[P3 — Goldilocks]]
