---
title: "AICP Stage 3 hardware unlocked 2026-04-17 — 19GB VRAM dual-GPU"
type: note
domain: log
note_type: session
status: synthesized
confidence: medium
created: 2026-04-17
updated: 2026-04-17
sources: []
tags: [contributed, remark]
contributed_by: "aicp-self"
contribution_source: "/home/jfortin/devops-expert-local-ai"
contribution_date: 2026-04-17
contribution_status: accepted
contribution_reason: "Status update on Local AI model open question: 19GB hardware is now in place"
resolution_date: 2026-04-17
resolution_notes: |
  Hardware unlock incorporated into AICP identity profile's State row (phase/scale detail).
  Knowledge-gap entry added: "Empirical routing split with 19 GB dual-GPU hardware (measurements pending)"
  linked to Model — Local AI's "Empirical routing split after Stage 3" open question.
  Aligns with 2026-04-17 strategic synthesis [[2026-consumer-hardware-ai-stack|2026 Consumer-Hardware AI Stack]]
  which names Stage 5 as integration-blocked (no longer hardware-blocked) — this contribution is the
  first concrete confirmation of that trajectory shift.
---

# AICP Stage 3 hardware unlocked 2026-04-17 — 19GB VRAM dual-GPU

## Summary

AICP hardware capacity confirmed at 19GB VRAM (RTX 2080 8GB + RTX 2080 Ti 11GB) on 2026-04-17. This is the planned Stage 3 hardware threshold called out in Model — Local AI: 'The planned upgrade to 19GB unlocks Stage 3: running complex agent reasoning locally, which is the step that moves the routing split from ~40% local to ~80% local.' Status: capacity in place; empirical routing split measurement is the next operational step (still pending, but no longer blocked by hardware). Models now runnable that were previously hardware-blocked: Qwen3-30B-A3B MoE (17GB / 18GB+ VRAM), Gemma 4 26B MoE (16.8GB / 18GB+ VRAM). The dual-gpu profile in config/profiles/dual-gpu.yaml becomes runnable. Open question 'Empirical routing split after Stage 3' from Model — Local AI is now answerable in principle — measurement work tracked under AICP Step 9 of the second-brain adoption plan.

## Relationships

- RELATES TO: [[model-registry|Model Registry]]

## Backlinks

[[model-registry|Model Registry]]
