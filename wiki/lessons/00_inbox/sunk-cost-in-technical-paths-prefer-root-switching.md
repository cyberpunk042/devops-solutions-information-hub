---
title: "sunk-cost-in-technical-paths-prefer-root-switching"
type: lesson
domain: cross-domain
layer: 4
status: synthesized
confidence: medium
maturity: seed
derived_from: []
created: 2026-04-27
updated: 2026-04-27
sources: []
tags: [contributed, inbox]
contributed_by: "jfortin@WORKSTATION-JFM"
contribution_source: "/home/jfortin/devops-expert-local-ai"
contribution_date: 2026-04-27
contribution_status: pending-review
---

# sunk-cost-in-technical-paths-prefer-root-switching

## Summary

# Sunk-Cost in Technical Paths — Prefer Root Switching to Adjacent Switching

## Pattern

When a build/run/serving step fails after prior infrastructure has been built, the
choice of how to recover decides whether the work realigns with the original spec or
drifts further from it.

**Adjacent switch**: change a small thing (weight format, config flag, version pin)
to preserve the prior infrastructure (serving stack, runtime, framework already
installed). The temptation: "I already invested time setting up X; let me find a
different input that fits X."

**Root switch**: change the root thing (the serving stack itself) to realign with
the original specification. The cost: discard the adjacent work that was built on
the wrong foundation.

## When this pattern matters

The pattern matters when the original spec was correct and the adjacent decision
took you off-spec. If the original spec was itself wrong, root-switching is also
wrong — that's a different problem.

In the evidence case below, the brain's original specification was sound; the
adjacent-switch decision moved away from the sound spec. Root-switching would have
restored alignment.

## Evidence: AICP Post-Anthropic mission, 2026-04-22 to 2026-04-24

- **Original spec** (brain): Kimi K2.6 Q2_K_XL (318GB GGUF, Unsloth) served via
  llama.cpp on operator's Tier 0 hardware (64GB RAM). Memory headroom: 30-40GB.
  Proven on identical hardware tier by thousands of users.
- **Earlier session** built sglang + kt-kernel infrastructure for K2.6.
- **Dead-end hit**: Unsloth GGUF not supported by sglang's transformers backend.
- **Adjacent switch chosen**: switch the weight format (Unsloth Q2 → Moonshot
  RAWINT4 555GB safetensors) to preserve the sglang+kt-kernel setup.
- **Result**: Moonshot weights need ~50GB peak RAM at startup → margin-of-zero on
  the 48GB WSL cap. Crashed catastrophically; took down the whole Windows machine
  on second attempt. ~929GB cumulative bandwidth spent on a path that was never
  going to work for this hardware.
- **Root switch would have done**: discard sglang+kt-kernel, install llama.cpp from
  source, serve the existing Unsloth Q2 GGUF. The brain's spec, intact, on the
  hardware sized for it.

The model recommending the adjacent switch did so explicitly on the rationale of
"preserve today's setup" — a textbook sunk-cost argument. The recommendation was
wrong because the prior setup itself was off-spec.

## Detection

When facing a failed step in a multi-component pipeline, ask:

1. Does my proposed fix preserve the prior infrastructure or replace it?
2. If preserve: is the prior infrastructure aligned with the ORIGINAL spec, or did
   I land on it via earlier adjacent decisions?
3. If the prior infrastructure was itself an adjacent decision, the pattern says:
   prefer root switching now, before further adjacent-switches accumulate.

## How to apply

When recommending recovery from a failed step, name BOTH options:
- (a) adjacent switch (preserves prior setup, moves further from original spec)
- (b) root switch (discards prior setup, realigns with original spec)

Then explicitly evaluate which spec each option aligns with. If the original spec
was sound, root-switching is the recommendation. If the original spec is now in
question, surface that question to the operator BEFORE proposing either option.

## What this is NOT

- Not "always discard prior work". Sometimes the adjacent option is correct (e.g.,
  the original spec really was wrong; the adjacent option was always going to be
  better).
- Not "ignore costs of replacement". Root-switching may be expensive; that cost is
  real and should be compared against the cost of further failures on the
  off-spec path.
- Not a rule about software architecture. The pattern is about decision-making
  during recovery from failure, applicable to any multi-component pipeline.

## Source

AICP Post-Anthropic mission retrospective (2026-04-27),
docs/retros/RETRO-post-anthropic-2026-04-27.md.
Postmortem: docs/POSTMORTEM-2026-04-24-k26-local-wrong-path.md.

## Context

<!-- When does this lesson apply? -->

## Insight

<!-- The core learning -->

## Evidence

<!-- What evidence supports this? -->

## Applicability

Contributed from /home/jfortin/devops-expert-local-ai. Applicability to be assessed during promotion review.

## Relationships

- RELATES TO: [[model-registry|Model Registry]]

## Backlinks

[[model-registry|Model Registry]]
