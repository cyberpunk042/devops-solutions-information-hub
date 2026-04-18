---
date: 2026-04-17
type: operator-directive
action: ingest
status: in-progress
---

# 2026-04-17 — Directive: Ingest AirLLM + NVMe SSD question

## Verbatim operator message

> new thing to ingest:
> https://github.com/lyogavin/airllm (https://datasharepro.in/airllm/)
>
> Also we now technically have 19 GB VRAM. I will soon be restarting work in localAI too. but now as I see this I wounder if the best solution is not to use my nvme ssd space!?
> Anyway. take the time to properly ingest and process

## What this contains

1. Ingestion target: two sources about AirLLM (lyogavin/airllm GitHub + datasharepro.in article).
2. Hardware state update: 19 GB VRAM is now ACTUAL (previously planned; see `project_hardware_upgrade` memory).
3. An emergent question the operator is raising: should the $0 local-inference path use NVMe SSD space rather than (or in addition to) VRAM-bound models? AirLLM is exactly a library about this — layer-by-layer streaming of model weights from disk so 70B+ models run on low-VRAM GPUs.
4. Context: operator will soon restart work in Local AI (the AICP-adjacent $0-target subsystem). This ingestion feeds directly into that decision.

## Action plan

1. Fetch both sources with `pipeline fetch` (auto-tries curl, playwright, raw save).
2. Multi-pass ingestion (per `feedback_iterative_depth`): extract → cross-ref → gaps → deepen.
3. Depth verification: fetch the actual repository README and a real code example — not just the marketing article.
4. Cross-reference: Model — Local AI · hardware-upgrade memory · $0 target subsystem · AICP project profile.
5. Answer the operator's implicit question about NVMe SSD — AirLLM's whole value proposition IS disk-offload, so the question has a real answer worth making explicit.
6. Update `project_hardware_upgrade` memory: 19 GB VRAM is now actual.
7. Run `pipeline post` → 0 errors.
