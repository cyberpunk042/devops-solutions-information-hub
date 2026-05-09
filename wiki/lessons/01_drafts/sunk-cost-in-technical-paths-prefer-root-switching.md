---
title: "Lesson — Sunk-cost in technical paths: prefer root switching to adjacent switching when recovering from failure"
aliases:
  - "Sunk-Cost Root vs Adjacent Switching"
  - "Recovery: Root Switch over Adjacent Switch"
  - "Sunk-Cost in Technical Paths"
type: lesson
domain: cross-domain
layer: 4
status: synthesized
confidence: high
maturity: growing
created: 2026-04-27
updated: "2026-05-09"
last_reviewed: "2026-05-09"
derived_from: []
sources:
  - id: aicp-postmortem-k2-6-wrong-path
    type: project
    project: aicp
    path: docs/POSTMORTEM-2026-04-24-k26-local-wrong-path.md
    description: "AICP postmortem documenting the sglang+kt-kernel adjacent switch that crashed Windows; 929GB cumulative bandwidth waste"
  - id: aicp-retrospective-2026-04-27
    type: project
    project: aicp
    path: docs/retros/RETRO-post-anthropic-2026-04-27.md
    description: "AICP Post-Anthropic mission retrospective"
  - id: principle-4
    type: wiki
    file: wiki/lessons/04_principles/hypothesis/declarations-are-aspirational-until-infrastructure-verifies-them.md
    description: "P4 — the prior infrastructure's fit-for-purpose was aspirational until the dead-end empirically verified its off-spec status"
tags: [contributed, lesson, recovery, sunk-cost, root-switching, decision-making, multi-component-pipeline, layer-4, contributed-from-aicp]
contributed_by: "jfortin@WORKSTATION-JFM"
contribution_source: "/home/jfortin/devops-expert-local-ai"
contribution_date: "2026-04-27"
contribution_status: accepted
---

# Lesson — Sunk-cost in technical paths: prefer root switching to adjacent switching when recovering from failure

## Summary

When a build / run / serving step fails after prior infrastructure has been built, the choice of how to recover decides whether the work realigns with the original spec or drifts further from it. **Adjacent switch**: change a small thing (weight format, config flag, version pin) to preserve prior infrastructure (serving stack, runtime, framework already installed). The temptation: *"I already invested time setting up X; let me find a different input that fits X."* **Root switch**: change the root thing (the serving stack itself) to realign with the original specification. The cost: discard the adjacent work that was built on the wrong foundation. **The pattern matters when the original spec was correct and the adjacent decision took you off-spec**; if the original spec was itself wrong, root-switching is also wrong (different problem). Empirically validated 2026-04-22 → 2026-04-24 in AICP K2.6 deployment: sglang+kt-kernel infrastructure built in earlier session, dead-end on Unsloth GGUF support, adjacent switch chosen (Moonshot RAWINT4 555GB safetensors) → 50GB peak RAM crashed Windows on second attempt. **Root switch** (discard sglang+kt-kernel, install llama.cpp from source, serve existing Unsloth Q2 GGUF) would have restored the brain's spec on the hardware sized for it. ~929GB cumulative bandwidth wasted on a path that was never going to work.

## Context

> [!info] **When this lesson applies**
>
> | Decision class | Apply this doctrine? |
> |---|---|
> | Failed step in multi-component pipeline (build, deploy, serve, integrate) | **YES** — name BOTH options; evaluate alignment |
> | Recovery from a single-component failure (no prior infrastructure to preserve) | NO — no sunk cost; just fix and proceed |
> | Original spec is itself in question | NO — different problem; surface the spec question first |
> | Multiple adjacent decisions already made | **YES, with extra urgency** — pattern compounds; root-switch sooner before further drift |
> | Operator-supervised solo session with one-shot workflow | **YES** — same applies; agent must surface BOTH options |

## Insight

> [!tip] **The adjacent option preserves prior infrastructure but drifts from the original spec; the root option discards prior infrastructure but realigns with the original spec.**
>
> When facing a failed step:
>
> 1. Does my proposed fix PRESERVE the prior infrastructure or REPLACE it?
> 2. If preserve: is the prior infrastructure aligned with the ORIGINAL spec, or did I land on it via earlier adjacent decisions?
> 3. If the prior infrastructure was itself an adjacent decision, the pattern says: prefer root switching now, before further adjacent-switches accumulate.
>
> **Sunk cost is the antagonist.** *"I already invested time setting up X"* is a textbook sunk-cost argument — and it produces wrong recommendations when the prior X was off-spec.

## Evidence

> [!success]- **Evidence — AICP K2.6 deployment, 2026-04-22 → 2026-04-24**
>
> - **Original spec** (brain): Kimi K2.6 Q2_K_XL (318GB GGUF, Unsloth) served via llama.cpp on operator's Tier 0 hardware (64GB RAM). Memory headroom: 30-40GB. Proven on identical hardware tier by thousands of users.
> - **Earlier session** built sglang + kt-kernel infrastructure for K2.6.
> - **Dead-end hit**: Unsloth GGUF not supported by sglang's transformers backend.
> - **Adjacent switch chosen**: switch the weight format (Unsloth Q2 → Moonshot RAWINT4 555GB safetensors) to preserve the sglang+kt-kernel setup.
> - **Result**: Moonshot weights need ~50GB peak RAM at startup → margin-of-zero on the 48GB WSL cap. Crashed catastrophically; took down the whole Windows machine on second attempt. ~929GB cumulative bandwidth spent on a path that was never going to work for this hardware.
> - **Root switch would have done**: discard sglang+kt-kernel, install llama.cpp from source, serve the existing Unsloth Q2 GGUF. The brain's spec, intact, on the hardware sized for it.
>
> The model recommending the adjacent switch did so explicitly on the rationale of *"preserve today's setup"* — a textbook sunk-cost argument. The recommendation was wrong because the prior setup itself was off-spec.

## Applicability

> [!info] **Recovery decision matrix**
>
> | Situation | Recommendation |
> |---|---|
> | Original spec sound + prior infrastructure on-spec | Adjacent switch (small fix) |
> | Original spec sound + prior infrastructure off-spec (adjacent earlier) | **Root switch** (realign) |
> | Original spec questionable | Surface spec question to operator BEFORE proposing either |
> | Adjacent decisions accumulated 2+ deep | Root switch with high urgency |

## How to Apply

> [!tip] **When recommending recovery from a failed step:**
>
> 1. **Name BOTH options explicitly:**
>    - (a) adjacent switch — preserves prior setup, moves further from original spec
>    - (b) root switch — discards prior setup, realigns with original spec
> 2. **Evaluate which spec each option aligns with.**
>    - If the original spec was sound, root-switching is the recommendation.
>    - If the original spec is now in question, surface that question to the operator BEFORE proposing either option.
> 3. **Quantify the discarded cost** (time, bandwidth, dependencies) of root-switching. This is the operator's data for the decision.
> 4. **Quantify the projected divergence** of adjacent-switching. This is the operator's data for the decision.

> [!warning] **What this is NOT**
>
> - Not *"always discard prior work."* Sometimes the adjacent option is correct (e.g., the original spec really was wrong; the adjacent option was always going to be better).
> - Not *"ignore costs of replacement."* Root-switching may be expensive; that cost is real and should be compared against the cost of further failures on the off-spec path.
> - Not a rule about software architecture. The pattern is about decision-making during recovery from failure, applicable to any multi-component pipeline.

## Source

AICP Post-Anthropic mission retrospective (2026-04-27), `docs/retros/RETRO-post-anthropic-2026-04-27.md`. Postmortem: `docs/POSTMORTEM-2026-04-24-k26-local-wrong-path.md`.

## Relationships

- RELATES TO: [[fake-blockers-vs-real-blockers-empirical-verification-required|Fake Blockers vs Real Blockers]] — sister discipline; both require empirical verification before assumption
- RELATES TO: [[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4 — Declarations Aspirational Until Verified]] — the prior infrastructure's *"fit for purpose"* was aspirational until the dead-end empirically verified its off-spec status
- RELATES TO: [[the-agent-must-practice-what-it-documents|The Agent Must Practice What It Documents]] — sunk-cost recommendations come from agents that haven't practiced root-cause discipline

## Backlinks

[[Fake Blockers vs Real Blockers]]
[[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4 — Declarations Aspirational Until Verified]]
[[the-agent-must-practice-what-it-documents|The Agent Must Practice What It Documents]]
