---
title: "Synthesis — OpenAI GPT-5.5 (2026-04-23): rapid-cadence frontier-tier successor to GPT-5.4 (released ~7 weeks prior), explicitly positioned 'better at coding, computer use, deeper research,' rolling out to Plus/Pro/Business/Enterprise in ChatGPT and Codex with API arrival 'very soon' but staged via 'different safeguards'; safety-disclosure-class is 'High' (not 'Critical') — calibrated against Anthropic's Claude Mythos Preview restriction; first OpenAI release framed in industry discourse as 'racing to keep up with Anthropic' rather than setting the pace"
type: source-synthesis
domain: ai-models
status: synthesized
confidence: high
maturity: seed
layer: 1
created: 2026-05-15
updated: 2026-05-15
sources:
  - id: cnbc-capoot-2026-04-23
    type: article
    url: https://www.cnbc.com/2026/04/23/openai-announces-latest-artificial-intelligence-model.html
    file: raw/articles/httpswwwcnbccom20260423openai-announces-latest-artificial-intelligence-modelhtml.md
    description: "CNBC (Ashley Capoot, 2026-04-23) — the canonical primary-source article for GPT-5.5 launch. Includes direct quotes from OpenAI President Greg Brockman ('how much more it can do with less guidance' / 'setting the foundation for how we're going to use computers'), Mia Glaese VP Research ('extensive third-party safeguard testing and red teaming for cyber and bio risks'), CNBC's strategic framing of OpenAI 'racing to keep up with rivals including Google and Anthropic, whose latest model Claude Mythos Preview has captivated Wall Street,' explicit safety-class disclosure (not 'Critical' threshold, meets 'High' classification), rollout cadence (ChatGPT + Codex 2026-04-23; API 'very soon' with 'different safeguards')."
  - id: marktechpost-razzaq-2026-04-18-opus-47
    type: article
    url: https://www.marktechpost.com/2026/04/18/anthropic-releases-claude-opus-4-7-a-major-upgrade-for-agentic-coding-high-resolution-vision-and-long-horizon-autonomous-tasks/
    file: raw/articles/anthropic-releases-claude-opus-47-a-major-upgrade-for-agentic-coding-high-resolu.md
    description: "MarkTechPost (Asif Razzaq, 2026-04-18) — secondary corroborating data: 'GPT-5.5 tops Terminal-Bench at 82.7%' and 'Claude Code leads on code quality at 87.6% SWE-bench Verified' from MarkTechPost's separate roundup article ('Best AI Agents for Software Development Ranked'); also flags SWE-bench-Verified-was-declared-contaminated-by-OpenAI-in-February-2026 caveat that affects how to read GPT-5.5's coding-benchmark claims."
  - id: anthropic-newsroom-opus-4-7-2026-04-16
    type: article
    url: https://www.anthropic.com/news/claude-opus-4-7
    file: raw/articles/introducing-claude-opus-47-anthropic.md
    description: "Anthropic Opus 4.7 newsroom (April 16, 2026) — direct comparative data: Opus 4.7's GDPVal-AA Elo 1753 vs GPT-5.4 1674 (the predecessor); CodeRabbit (David Loker) reports Opus 4.7 is 'a bit faster than GPT-5.4 xhigh on our harness' — establishes the baseline GPT-5.5 supersedes. No direct GPT-5.5 benchmarks from Anthropic since GPT-5.5 released 1 week after Opus 4.7."
tags: [openai, gpt-5-5, gpt-5-4, chatgpt, codex, frontier-llm, agentic-coding, computer-use, deep-research, terminal-bench-82-7, safety-class-high, cybersecurity-risk-threshold, novo-nordisk-partnership-context, "2026-04-23", source-synthesis, "2026-05-15", frontier-delta-2026-05-15]
---

# GPT-5.5 — OpenAI Frontier Release, 2026-04-23

> [!info] Reference Card
>
> | Field | Value |
> |---|---|
> | **Launch date** | 2026-04-23 |
> | **Predecessor** | GPT-5.4 (released early March 2026 — ~7 weeks prior) |
> | **Cadence implication** | OpenAI shipping a major version every ~6–8 weeks; faster than Anthropic (Opus 4.6 → 4.7 was ~10 weeks) |
> | **Stated improvements** | "Better at coding, using computers, deeper research capabilities" |
> | **Rollout — Day 1** | ChatGPT (Plus/Pro/Business/Enterprise) + Codex |
> | **Rollout — API** | "Very soon" with "different safeguards" (per Mia Glaese, VP Research) |
> | **Safety classification (OpenAI's framework)** | Below "Critical" threshold; meets "High" classification — "could amplify existing pathways to severe harm" |
> | **Discourse framing (CNBC)** | "OpenAI is racing to keep up with rivals including Google and Anthropic, whose latest model, Claude Mythos Preview, has captivated Wall Street" |
> | **Standout external benchmark** | Terminal-Bench 82.7% (highest in field per MarkTechPost roundup) |
> | **Codex distribution** | Day-one rollout in OpenAI's coding-assistant Codex |

## Summary

GPT-5.5 is OpenAI's 2026-04-23 frontier release — a **rapid-cadence successor** to GPT-5.4 (released ~7 weeks earlier) explicitly engineered to recapture narrative leadership from Anthropic following the Opus 4.7 GA (2026-04-16) and the Claude Mythos Preview restricted-tier disclosure that was actively "captivating Wall Street" per CNBC. OpenAI's stated improvements over GPT-5.4 are concentrated in three areas — **coding, computer use, deeper research** — and OpenAI President Greg Brockman frames the core capability shift as "how much more it can do with less guidance ... it can look at an unclear problem and figure out just what needs to happen next," positioning the release as a foundation for autonomous computer-work workflows. The model rolled out **same-day to ChatGPT (Plus/Pro/Business/Enterprise tiers) and to Codex** (OpenAI's coding assistant), with API arrival staged for "very soon" pending "different safeguards" (Mia Glaese, VP Research) — an explicit acknowledgement that the API surface needs more guardrails than the chat surface before frontier release. Most strategically: OpenAI's safety disclosure is **calibrated against Anthropic's Mythos restriction** — OpenAI explicitly states GPT-5.5 does NOT cross the "Critical" cybersecurity risk threshold (which "could bring unprecedented new pathways to severe harm") but does meet the "High" classification (which "could amplify existing pathways"). This is OpenAI positioning *below the line Anthropic crossed with Mythos*, claiming the same release-the-frontier-publicly strategy Anthropic abandoned with Project Glasswing. Independent benchmark data is limited but MarkTechPost reports GPT-5.5 **tops Terminal-Bench at 82.7%** (highest in the field) while Claude Code leads on SWE-bench Verified at 87.6% — a benchmark OpenAI itself declared contaminated in February 2026. For this project's stored vision: GPT-5.5 supersedes GPT-5.4 in the OpenRouter T002 smoke-test list, re-baselines the AI Infrastructure Decision Framework 2026's GPT tier-0 candidate, and provides empirical evidence that **the frontier race is now a 6-week cycle** with vendor-positioning (Anthropic gates, OpenAI publishes) as the differentiating axis rather than capability per se.

## Key Insights

> [!abstract] OpenAI's stated value proposition is autonomy with less guidance
> Brockman's framing — "how much more it can do with less guidance ... look at an
> unclear problem and figure out just what needs to happen next" — is the exact
> capability shape Opus 4.7 also targets (self-verification + rigor + long-horizon
> autonomy). Two frontier vendors converged on the same target capability in the
> same week. This is the strongest empirical evidence in this synthesis cycle
> that **agentic autonomy is the new frontier-tier capability**, replacing
> raw-reasoning-on-benchmarks as the differentiating axis.

1. **Rollout cadence is ChatGPT-and-Codex first, API later** — Day-1: Plus/Pro/Business/Enterprise users in ChatGPT and Codex. API: "very soon" with "different safeguards." This is a deliberate sequencing: surface where OpenAI controls UX (chat + coding assistant) gets the model first; surface where developers can chain it autonomously (API) waits for additional guardrails. Practical implication: **harnesses that depend on GPT-5.5 via API have an unknown wait window**; harnesses that consume it via ChatGPT/Codex interfaces had Day-1 access.

2. **Safety classification "High" but not "Critical" is positioned against Mythos** — CNBC explicitly connects this to Anthropic: "The cybersecurity risks presented by AI have been top of mind for tech executives and government officials since Anthropic announced its Mythos model earlier this month. The company decided to limit Mythos' rollout because of its ability to identifying weaknesses and security flaws within software." OpenAI's choice to publish a model at "High" classification *while disclosing that classification* is the differentiated strategic posture vs Anthropic's gate-and-restrict approach.

3. **Cadence is 6–8 weeks vendor-vs-vendor in 2026** — GPT-5.4 → GPT-5.5 in ~7 weeks; Opus 4.6 → 4.7 in ~10 weeks; Sonnet 4.6 launched mid-Feb, Opus 4.5 in late November 2025. **For this project's stored vision, "current SOTA" has a half-life measured in weeks**, not months. This re-frames how the OpenRouter T002 smoke-test list and the AI Infrastructure Decision Framework 2026 should be maintained — by date-stamped snapshots, not by stable rankings.

4. **Codex integration is Day-1 — GPT-5.5 lands directly in the coding-assistant workflow** — this matters because OpenAI's coding-assistant story is the most direct competitor to Claude Code. Codex on GPT-5.5 + the NVIDIA-mentioned "Codex on GPT-5.5" co-marketing represents a structural product-bundle change.

5. **"Different safeguards" for API release is the load-bearing operational claim** — OpenAI is explicitly telling developers that the API isn't ready Day-1 because the safety surface is different. This is the *opposite* of OpenAI's historical "API-first, ChatGPT later" pattern. It signals that frontier-tier safety engineering is now release-blocking even at OpenAI, which is the same constraint that produced Anthropic's Mythos restriction. **Two vendors, two different strategies for managing the same constraint.**

6. **Terminal-Bench 82.7% positions GPT-5.5 as the new SOTA on terminal-based coding** — per MarkTechPost roundup. This matters because Opus 4.7's strength is *agentic* coding (SWE-bench Pro 64.3%, CursorBench 70%), while raw-terminal coding was a category where GPT-5.4 still led Opus 4.7 (per VentureBeat). GPT-5.5 reinforces that lead.

7. **MarkTechPost's benchmark roundup flags SWE-bench contamination — OpenAI's own February 2026 disclosure** — "The benchmark OpenAI itself declared contaminated in February 2026 is still being used to rank these tools — including by the labs publishing their own scores." This is a P4-relevant caveat: **GPT-5.5's coding-benchmark numbers must be read with awareness that the standard benchmark suite has known contamination**.

> [!warning] No public capability disclosure from OpenAI beyond CNBC's reporting
> OpenAI's launch on 2026-04-23 was via reporter briefing rather than a full
> technical post comparable to Anthropic's Opus 4.7 newsroom write-up. The
> benchmark numbers + capability claims in this synthesis trace to CNBC's
> reporting of the briefing + MarkTechPost's roundup, not a primary OpenAI
> technical document. This is the inverse of the Opus 4.7 situation where
> Anthropic published a long-form technical breakdown.

8. **Vendor-narrative positioning has now flipped** — CNBC's framing — "OpenAI is racing to keep up with rivals including Google and Anthropic, whose latest model, Claude Mythos Preview, has captivated Wall Street" — would have been inconceivable two years ago. For this project's anti-vendor-lock-in lesson, the empirical record is now: **no single vendor holds narrative leadership for more than ~6 weeks**, and capital-markets narrative (Mythos captivating Wall Street while restricted) is a distinct axis from product capability.

9. **The Novo Nordisk + GPT-Rosalind context surrounds this release** — OpenAI's same-week activity also included the Novo Nordisk partnership and the GPT-Rosalind life-sciences model. GPT-5.5 is the general-purpose flagship; GPT-Rosalind is the specialized-vertical companion (per `src-gpt-rosalind-openai-life-sciences-2026-04-17.md`). Together they show OpenAI executing on both **general frontier escalation** and **vertical-specialization** in the same window.

## Deep Analysis

### Comparative table — GPT-5.5 vs Opus 4.7 vs predecessors (where data available)

| Dimension | GPT-5.5 (2026-04-23) | Opus 4.7 (2026-04-16) | GPT-5.4 (~Mar 2026) | Notes |
|---|---|---|---|---|
| **GDPVal-AA Elo** | — (not disclosed) | 1753 | 1674 | Anthropic's benchmark; not run on GPT-5.5 yet |
| **Terminal-Bench 2.0** | **82.7%** | passed tasks 4.6 couldn't (Zach Lloyd, Warp) | — | MarkTechPost roundup: GPT-5.5 highest |
| **SWE-bench Verified** | reported but contaminated | 87.6% (per MTP roundup, with same caveat) | — | OpenAI declared contaminated Feb 2026 |
| **Coding (general)** | "better at coding" (CNBC) | SWE-bench Pro 64.3% (+13% on internal 93-task) | baseline | No direct head-to-head |
| **Computer use** | "better at using computers" (CNBC) | XBOW 98.5% (vs 4.6's 54.5%) | 89.3% agentic search lead | Both vendors targeted this category |
| **Deep research** | "deeper research capabilities" (CNBC) | research-agent 0.715 avg (6 modules) | baseline | Convergent capability push |
| **Pricing (per M-tok)** | not disclosed at launch | $5 / $25 (input/output) | baseline | OpenAI pricing typically disclosed at API release |
| **Safety class disclosed** | "High" (below Critical) | comparable to 4.6 with cyber-block additions | — | Different disclosure frameworks |
| **Cybersecurity ceiling** | not crossing Critical | CyberGym 73.1% (deliberate restraint) | CyberGym 66.3% | Both vendors below Mythos's 83.1% |
| **API availability** | "very soon" with different safeguards | Day-1 | Day-1 | OpenAI staging this release; deviation from pattern |

### What changes for this project's stored vision

1. **`wiki/backlog/tasks/T002-run-openrouter-smoke-tests.md`** — `openai/gpt-5-5` replaces `openai/gpt-5-4` as the OpenAI tier-0 candidate **once API rollout completes**. Until then, GPT-5.4 remains the API-accessible OpenAI candidate. Need to monitor for API GA announcement.

2. **`wiki/spine/references/ai-infrastructure-decision-framework-2026.md`** — capability-tier reference should be updated to name `openai/gpt-5-5` as the current OpenAI frontier, with the "API rollout pending" caveat explicit. The framework should also incorporate the **cadence observation** (6-8-week vendor releases) as a maintenance-velocity input.

3. **Anti-vendor-lock-in lesson** (`wiki/lessons/02_synthesized/anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence.md`) — GPT-5.5's release reinforces the lesson empirically: GPT-5.4 was current ~7 weeks; SOTA leadership trades positions inside a single quarter. The cost of lock-in is now visibly larger than it was when frontier releases were annual.

4. **Custom-tailored senior-engineer-tier model group research synthesis** — GPT-5.5 should be added to the tier-0 candidate list alongside Opus 4.7, with the explicit observation that both vendors converged on the same capability shape (less-guidance, more-autonomy, longer-horizon).

### Strategic claim — the frontier-vendor differentiation axis has moved from capability to release strategy

Throughout late 2024 and 2025, vendor differentiation was primarily **capability** (which model scores higher on which benchmark). In 2026-Q2, with Opus 4.7 and GPT-5.5 launched 7 days apart and converging on the same target capability shape (autonomy + verification + computer use + deep research), the meaningful differentiation has shifted to **release strategy**: Anthropic ships Opus 4.7 broadly and restricts Mythos to enterprise cybersecurity partners; OpenAI ships GPT-5.5 broadly through ChatGPT/Codex but stages the API behind "different safeguards." Both vendors recognize that frontier capability now creates novel risks; they diverge in **whether to gate peak capability institutionally (Anthropic via Project Glasswing) or to publish at a stated safety-class with rollout sequencing (OpenAI via High-not-Critical classification + delayed API)**. For this project's stored vision, this is the relevant strategic shift to record — not "which model is better" but "which release strategy fits our risk posture."

## Open Questions

- When does GPT-5.5 API become generally available? CNBC says "very soon" with "different safeguards" — no concrete date.
- What are the GPT-5.5 API pricing tiers vs GPT-5.4 + Opus 4.7? Not disclosed at chat-launch.
- Has any independent body benchmarked GPT-5.5 head-to-head against Opus 4.7 using uncontaminated evaluation sets? The SWE-bench contamination caveat makes most public comparisons unreliable.
- What does OpenAI's "Critical" vs "High" cybersecurity-risk threshold actually mean operationally? The framework is referenced but not fully documented in the launch material.
- How does GPT-5.5 interact with the Anthropic-OpenAI-Apple Siri legal dispute and Microsoft-OpenAI dependency tensions noted in adjacent CNBC coverage? Distribution risk is rising in parallel with capability.

## Relationships

- SUPERSEDES (in OpenAI frontier slot): GPT-5.4 (early March 2026) — predecessor model in this project's existing T002 references.
- PEER COMPETITOR (released 7 days earlier): Claude Opus 4.7 — see `src-claude-opus-4-7-anthropic-frontier-2026-04-16.md`. Both vendors converge on autonomy + computer use + deep research as the 2026-Q2 capability target.
- COMPLEMENTS (same OpenAI release window): GPT-Rosalind (life sciences, 2026-04-17) — see `src-gpt-rosalind-openai-life-sciences-2026-04-17.md`. OpenAI executing simultaneously on general-frontier and vertical-specialization tracks.
