---
title: "E008 epic — internal stack-vs-format inconsistency caused 2-day wrong-path execution"
type: note
domain: log
note_type: session
status: synthesized
confidence: medium
created: 2026-04-25
updated: 2026-04-25
sources: []
tags: [contributed, correction]
contributed_by: "jfortin@WORKSTATION-JFM"
contribution_source: "/home/jfortin/devops-expert-local-ai"
contribution_date: 2026-04-25
contribution_status: pending-review
contribution_reason: "Forensic audit of 2026-04-24 incident — E008 ambiguity led to 2 days of wrong-path execution, WSL crash, and 555GB wrong download. Captured by the AICP session that recovered the milestone via llama.cpp + Unsloth Q2."
---

# E008 epic — internal stack-vs-format inconsistency caused 2-day wrong-path execution

## Summary

The E008 epic has three modules whose specifications are mutually
incompatible on consumer hardware:

- E008-M001 directs `pip install ktransformers`. Since Oct 2025, this
  meta-package installs sglang+kt-kernel (high-RAM datacenter stack),
  NOT the original classic ktransformers tool the brain was written
  against.
- E008-M002 specifies Unsloth Q2_K_XL GGUF (318GB consumer quant).
- E008-M004 expects the classic `ktransformers.server.main --gguf-path`
  interface, which sglang+kt-kernel does not provide.

Empirical 2026-04-24 outcome: sglang+kt-kernel + Q2 GGUF + 64GB consumer
hardware does not work. Memory math: ~50GB peak startup vs 48-56GB WSL
cap. Crashes WSL VM unrecoverably (forced Windows reboot).

The combination that DOES work on consumer hardware (verified, running):
  llama.cpp built from source with CUDA + Unsloth Q2_K_XL GGUF (318GB) + -ngl 0
  Memory: ~22GB peak startup. Throughput: 0.045 tok/s thinking-on,
  0.10 tok/s thinking-off (Tier 0: X299 + DDR4-2666 + WSL + PCIe 3.0).

Recommendation:
- M001: replace with "Build llama.cpp from source with CUDA support;
  Unsloth GGUF is its native format. sglang/kt-kernel is for datacenter
  hardware (128GB+ RAM, AMX-capable CPU)."
- M004: replace `ktransformers.server.main` invocation with `llama-server`
  invocation (canonical: aicp/scripts/llama-serve.sh).
- Add explicit hardware-class gate on each path (consumer vs workstation
  vs datacenter).

Source artifacts in the AICP repo:
- docs/POSTMORTEM-2026-04-24-k26-local-wrong-path.md (full forensic)
- docs/EXPLORATION-LOG-LOCAL-K26-EMPIRICAL-2026-04-24.md (measured numbers)
- scripts/llama-serve.sh (working canonical launcher)

## Relationships

- RELATES TO: [[model-registry|Model Registry]]

## Backlinks

[[model-registry|Model Registry]]
