---
title: "Synthesis — Claude Mythos Preview (Anthropic, restricted; April 2026): named successor-tier-above-Opus-4.7 model deliberately withheld from GA under Project Glasswing, deployed only to a small set of enterprise cybersecurity partners; serves as alignment-benchmark anchor (lowest misaligned-behavior score Anthropic has trained) and as the capability ceiling against which Opus 4.7's safeguards are calibrated — strategic indicator of Anthropic's intent to broker capability gating per use case rather than ship peak capability publicly"
type: source-synthesis
domain: ai-models
status: synthesized
confidence: medium
maturity: seed
layer: 1
created: 2026-05-15
updated: 2026-05-15
sources:
  - id: anthropic-newsroom-opus-4-7-2026-04-16
    type: article
    url: https://www.anthropic.com/news/claude-opus-4-7
    file: raw/articles/introducing-claude-opus-47-anthropic.md
    description: "Anthropic's Opus 4.7 launch post — the canonical primary source on Mythos Preview, naming it as the most-capable model Anthropic has trained, the best-aligned per evaluations, and the explicit reason Opus 4.7's cyber capabilities were 'differentially reduced' during training. Confirms Mythos is referenced in the model-family page (Mythos Preview / Opus / Sonnet / Haiku tier list)."
  - id: cnbc-capoot-2026-04-16
    type: article
    url: https://www.cnbc.com/2026/04/16/anthropic-claude-opus-4-7-model-mythos.html
    file: raw/articles/httpswwwcnbccom20260416anthropic-claude-opus-4-7-model-mythoshtml.md
    description: "CNBC (Ashley Capoot, 2026-04-16) — Mythos rollout context: 'select group of companies as part of a new cybersecurity initiative called Project Glasswing earlier this month,' high-profile meetings between Trump administration, tech CEOs, and bank chief executives about the security risks of powerful AI models; explicit Anthropic statement that 'Anthropic does not plan to make Claude Mythos Preview generally available' though the goal is to learn how to deploy Mythos-class models at scale eventually."
  - id: venturebeat-franzen-2026-04-16
    type: article
    url: https://venturebeat.com/technology/anthropic-releases-claude-opus-4-7-narrowly-retaking-lead-for-most-powerful-generally-available-llm
    file: raw/articles/anthropic-releases-claude-opus-47-narrowly-retaking-lead-for-most-powerful-gener.md
    description: "VentureBeat (Carl Franzen, 2026-04-16) — Mythos as the 'even more powerful successor, restricted to a small number of external enterprise partners for cybersecurity testing and patching vulnerabilities,' plus CyberGym benchmark anchor: Mythos Preview 83.1% vs Opus 4.7 73.1% vs GPT-5.4 66.3%."
  - id: cnbc-capoot-2026-04-23-gpt-5-5
    type: article
    url: https://www.cnbc.com/2026/04/23/openai-announces-latest-artificial-intelligence-model.html
    file: raw/articles/httpswwwcnbccom20260423openai-announces-latest-artificial-intelligence-modelhtml.md
    description: "CNBC (Ashley Capoot, 2026-04-23) on GPT-5.5 — confirms Mythos discourse continues a week after Opus 4.7: 'OpenAI is racing to keep up with rivals including Google and Anthropic, whose latest model, Claude Mythos Preview, has captivated Wall Street'; OpenAI's GPT-5.5 explicitly does NOT cross 'Critical' cybersecurity risk threshold but does meet 'High' classification — the threshold Mythos exceeded."
tags: [anthropic, claude-mythos-preview, frontier-restricted, project-glasswing, cybergym, capability-gating, alignment-benchmark, cyber-verification-program, "2026-04-16", strategic-indicator, vendor-pipeline-visibility, source-synthesis, "2026-05-15", frontier-delta-2026-05-15]
---

# Claude Mythos Preview — Anthropic's Restricted Frontier-Above-Frontier, April 2026

> [!info] Reference Card
>
> | Field | Value |
> |---|---|
> | **Status** | Restricted; not generally available; no GA plan |
> | **First confirmed mention** | 2026-04-06 (Project Glasswing announcement, ~10 days before Opus 4.7 GA) |
> | **Public posture** | Available only to a "select group of companies" under Project Glasswing for cybersecurity testing/patching |
> | **Position in family** | Above Opus in Anthropic's model tier list (Mythos Preview / Opus / Sonnet / Haiku per anthropic.com model menu) |
> | **CyberGym** | 83.1% (vs Opus 4.7 73.1%, GPT-5.4 66.3%) — the cyber-capability ceiling Anthropic is gating |
> | **Alignment posture** | Anthropic's automated behavioral audit shows Mythos Preview with the **lowest rate of misaligned behavior of any model Anthropic has trained** |
> | **Stated rationale for withholding** | "Risks—and benefits—of AI models for cybersecurity" — capability sufficient to be dual-use weaponizable |
> | **Stated future** | Anthropic's goal is to "eventually deploy Mythos-class models at scale" — Opus 4.7's automated cyber safeguards are the public testbed for the safeguards that would gate that release |

## Summary

Mythos Preview is Anthropic's **publicly-named but deliberately withheld** frontier model, sitting above Opus 4.7 in the model family hierarchy and deployed only to a small set of enterprise cybersecurity partners through a research-and-patching initiative called **Project Glasswing** (announced approximately a week before Opus 4.7's 2026-04-16 GA). Two facts shape its strategic significance for this project's vision tracking: **(1) it is the most-aligned model Anthropic has trained** per their automated behavioral audit — lower rates of misalignment than Opus 4.7 and Sonnet 4.6 — and **(2) its cyber capability ceiling is materially above Opus 4.7's** — CyberGym 83.1% vs Opus 4.7's 73.1%, the explicit reason Anthropic "differentially reduced" cyber capabilities during Opus 4.7's training and shipped automated request-blockers for prohibited cybersecurity uses. Anthropic's stated trajectory is that Opus 4.7's safeguards are the *testbed* for the safeguards that would eventually gate a broader Mythos-class release; the Cyber Verification Program is the bridge product that lets pentesters/red-teamers/vulnerability researchers apply for verified access to Opus-4.7-level cyber capability today. For this project's stored vision: **Mythos is a tracked-but-undeployable indicator** — it tells us where the frontier ceiling is, how Anthropic intends to broker peak capability (credentialed verification, not universal access), and that the era of "the most capable AI is universally available" is formally over for the Anthropic stack. The discourse signal is also material: CNBC's GPT-5.5 coverage (2026-04-23, one week after Opus 4.7 GA) explicitly frames OpenAI's release as "racing to keep up with rivals including Google and Anthropic, whose latest model, Claude Mythos Preview, has captivated Wall Street" — Mythos shapes capital-markets perception of Anthropic's frontier position regardless of whether it ever ships to GA.

## Key Insights

> [!abstract] The "named but withheld" pattern is itself a strategic instrument
> Mythos has zero customer-facing distribution, no API, no Bedrock/Vertex/Foundry
> presence, and no announced GA roadmap — yet Anthropic publicly names it on the
> model-family page, references it 14 times in the Opus 4.7 launch post, and
> bases regulatory + capital-markets narratives on its existence. This is *naming
> as positioning*: signaling capability ceiling without distributing it.

1. **Mythos is alignment-leader and capability-leader simultaneously** — the same model that scores lowest on misaligned behavior also scores highest on CyberGym. This is the empirical refutation of the simple "more capable = less safe" framing inside Anthropic's lab — it argues for tighter pairing, not categorical tradeoff. For this project's vision baselines, this is a notable data point against any rule that ranks frontier-tier candidates strictly on capability without an alignment dimension.

2. **CyberGym 83.1% is the load-bearing capability number** — it is the cyber-capability score Opus 4.7 deliberately falls short of (73.1%) and that triggered Project Glasswing's existence. No other Mythos benchmarks have been publicly disclosed, which means Mythos's actual *general* capability ceiling is inferred-only.

3. **Project Glasswing is the deployment vehicle, not the model** — Anthropic frames Glasswing as a cybersecurity research initiative for select enterprise partners to "test cyber safeguards and patch vulnerabilities Mythos exposes rapidly" (VentureBeat). The Trump administration + tech CEOs + bank CEOs meeting cycle CNBC describes happens through Glasswing, not direct Mythos API access.

4. **"Anthropic does not plan to make Claude Mythos Preview generally available"** — CNBC's direct paraphrase. But the same paragraph says the company's goal is "to learn how it could eventually deploy Mythos-class models at scale." Reading these together: the model in its current form is permanently restricted, but a successor with refined safeguards is the eventual GA target. Operator-decision implication: don't plan on Mythos as a candidate model; do plan on a Mythos-class GA release in some future window.

5. **Mythos is the explicit *reason* Opus 4.7 is shaped the way it is** — Anthropic states: "during [Opus 4.7's] training we experimented with efforts to differentially reduce these capabilities." Without Mythos as the anchor, Opus 4.7's particular shape (rigor + agentic autonomy + literal instruction-following + cyber-restraint) wouldn't exist as the deliberate engineering output it is.

6. **Mythos shapes capital-markets perception even though it's not deployed** — CNBC (GPT-5.5 coverage, 2026-04-23): "OpenAI is racing to keep up with rivals including Google and Anthropic, whose latest model, Claude Mythos Preview, has captivated Wall Street." This is a frontier-narrative effect: an undeployed model can still set valuation expectations. Relevant context for Anthropic's $800B valuation environment (VentureBeat).

7. **GPT-5.5's safety-class disclosure is calibrated against Mythos** — OpenAI explicitly states GPT-5.5 does NOT cross "Critical" cybersecurity risk threshold but does meet "High" classification (CNBC 2026-04-23). The discourse this disclosure exists inside is the Mythos discourse. OpenAI is positioning itself as "below the line Mythos crossed."

> [!warning] No independent verification of Mythos capabilities or alignment claims
> All Mythos claims trace to Anthropic's own statements + reportage of those
> statements. No external benchmark suite has independently tested Mythos
> Preview. This is exactly the situation P4 ("Declarations Aspirational Until
> Verified") was written for — every Mythos statement in this synthesis is
> conditional on Anthropic's own published evaluations.

8. **Mythos is a vendor-pipeline-visibility indicator, not a model to evaluate** — operator's vision tracks frontier-tier candidates. Mythos exists as a named entity in the vendor's pipeline. The right operational treatment is to record its existence + monitor for any GA announcement + treat its capability claims as soft signals to investigate, not hard baselines to mirror.

## Deep Analysis

### Why this project tracks Mythos at all

The operator-stated research scope is "make sure the models are up to date and our vision of the technologies are still acquire" (verbatim). Mythos doesn't fit the deployable-model column — there is no API ID to add to T002 smoke tests, no pricing to compare, no integration to flag. But it fits two other vision-tracking columns directly:

1. **Frontier ceiling** — the "senior engineer tier model group" research synthesis assumes a knowable ceiling for frontier capability. Mythos sets a public reference point for that ceiling (CyberGym 83.1% as the concrete number, alignment-leader claim as the qualitative companion).
2. **Vendor-strategy posture** — Anthropic's choice to *name and withhold* Mythos rather than either (a) ship it or (b) not name it tells us how Anthropic intends to behave with future frontier capability. This shapes the anti-vendor-lock-in calculus: a vendor that gates peak capability behind credentials introduces a new lock-in vector (the credential itself, not the API).

### Mapping to this project's lesson framework

| This project's lesson | Mythos evidence |
|---|---|
| `anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence` | Anthropic's gating reinforces lock-in risk: peak capability not API-accessible without verification → cannot empirically benchmark Mythos vs alternatives |
| `end-to-end-compression-across-the-ai-stack-composes-multiplicatively` | Not directly affected — Mythos is a single-layer signal |
| `never-synthesize-from-descriptions-alone` | **Honored here**: this synthesis explicitly flags that all Mythos claims are Anthropic-sourced; nothing claimed without source attribution |
| `agent-orchestration-is-highest-connected-concept` | Indirect: Mythos's existence shapes how Opus 4.7 was tuned for agentic orchestration (rigor + self-verification), which propagates into every agent harness |

### What to do about Mythos in this project's stored vision

| Action | Yes/No | Reason |
|---|---|---|
| Add to OpenRouter T002 smoke tests | **No** | No API endpoint |
| Add to AI Infrastructure Decision Framework 2026 capability tiers | **Yes, as "restricted-tier indicator"** | Sets the ceiling explicitly |
| Flag in `wiki/backlog/research-gaps.md` as "watch for GA announcement" | **Yes** | Concrete tracked-but-unverified gap |
| Update `wiki/lessons/02_synthesized/anti-vendor-lock-in-...` with Mythos as evidence | **Yes (operator approval needed)** | Lock-in risk vector concrete instance |
| Treat Mythos benchmark claims as ground truth | **No (P4)** | Vendor-sourced only; no independent verification |
| Wait for next Mythos disclosure before re-synthesizing | **Yes** | More to learn from Project Glasswing publications + any GA roadmap |

## Open Questions

- What are the actual conditions of Project Glasswing partnership? Which enterprises have Mythos access? (Not disclosed in any source fetched.)
- Has any third-party security researcher independently confirmed the CyberGym 83.1% claim, or any Mythos behavioral claim?
- What is the timeline for "Mythos-class GA"? Anthropic states the goal but provides no horizon; the Opus-4.7-as-testbed framing suggests months, not weeks.
- If Mythos's alignment leadership comes from a training-time intervention not yet applied to Opus 4.7, can that intervention propagate downward, or is it tied to Mythos's larger scale?
- How does the Cyber Verification Program approval bar compare to legitimate research workflows in this project's `wiki/domains/cybersecurity/` scope (Suricata, Honeypot/PolarProxy, etc.)?

## Relationships

- SUCCESSOR-TIER ABOVE: Claude Opus 4.7 — see `src-claude-opus-4-7-anthropic-frontier-2026-04-16.md`. Opus 4.7's shape (rigor + cyber-restraint + automated blockers) is calibrated against Mythos as ceiling.

## Backlinks

[[Claude Opus 4.7 — see `src-claude-opus-4-7-anthropic-frontier-2026-04-16.md`. Opus 4.7's shape (rigor + cyber-restraint + automated blockers) is calibrated against Mythos as ceiling.]]
