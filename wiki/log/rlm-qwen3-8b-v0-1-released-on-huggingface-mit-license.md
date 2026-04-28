---
title: "rlm-qwen3-8b-v0-1-released-on-huggingface-mit-license"
type: note
domain: log
note_type: session
status: synthesized
confidence: medium
created: 2026-04-27
updated: 2026-04-27
sources: []
tags: [contributed, remark]
contributed_by: "jfortin@WORKSTATION-JFM"
contribution_source: "/home/jfortin/devops-expert-local-ai"
contribution_date: 2026-04-27
contribution_status: pending-review
---

# rlm-qwen3-8b-v0-1-released-on-huggingface-mit-license

## Summary

# RLM-Qwen3-8B Checkpoint Released on Hugging Face — Brain Open Question Resolved

## What

The RLM-Qwen3-8B checkpoint named in the [tier-0 candidate comparison](../comparisons/rlm-qwen3-8b-vs-qwen3-6-27b-tier-0-long-context-candidate.md) and the [RLM paper deep-dive](../sources/tools-integration/src-rlm-paper-deep-dive-table-1-training-recipe-six-observations.md) **is released and stable on Hugging Face** under `mit-oasys/rlm-qwen3-8b-v0.1`.

Empirically verified via HF API on 2026-04-27:

```
modelId: mit-oasys/rlm-qwen3-8b-v0.1
license: MIT
base_model: Qwen/Qwen3-8B (finetune)
arxiv: 2512.24601
created: 2026-01-15T03:20:45.000Z
modified: 2026-02-20T02:57:23.000Z
downloads: 367
likes: 61
files: 4-shard safetensors (config.json, generation_config.json, chat_template.jinja, model-00001-of-00004.safetensors, ...)
```

## Why this matters for the brain

The tier-0 candidate comparison says under "Risks and Open Questions":

> 1. **Has Hugging Face released the RLM-Qwen3-8B checkpoint?** The paper's "code is available at https://github.com/alexzhang13/rlm" links the SDK, not the model weights. Need to check Hugging Face / paper-author releases.

That open question is now answered: **yes, released by `mit-oasys` org** (the OASYS lab — Zhang/Kraska/Khattab — exactly the paper authors).

## Downstream wiki updates this enables

1. **[tier-0 comparison](../comparisons/rlm-qwen3-8b-vs-qwen3-6-27b-tier-0-long-context-candidate.md)** "Operator decision tree for T-0" Question 2 ("Has RLM-Qwen3-8B checkpoint been released to Hugging Face?") can branch to **Yes** path. The decision tree's Option (a) "deploy Qwen3.6-27B as interim AND commit to RLM-Qwen3-8B self-training" no longer needs the self-training commitment — pulling weights is sufficient.

2. **[RLM-Qwen3.6-27B operations plan](../domains/cross-domain/rlm-qwen3-6-27b-fine-tune-operations-plan.md)** Step 1 prerequisite "Teacher RLM access (Qwen3-Coder-480B-A35B as RLM, OR alternative ≥30B coding-capable model)" — the released `mit-oasys/rlm-qwen3-8b-v0.1` is a viable cheaper teacher candidate (8B fits operator's RTX 2080 Ti for self-hosted teacher inference).

3. **Hardware compatibility note**: 4-shard safetensors at BF16 ≈ 16GB total (~4GB per shard). On operator's RTX 2080 Ti (11GB), full BF16 won't fit; INT8 quantization (~8GB) or layer offload to system RAM is needed. The brain's tier-0 comparison estimate "INT8 + LoRA: comfortable fit" is empirically supportable now.

## License correction

The tier-0 comparison hedged on RLM-Qwen3-8B license: *"Inherited from Qwen3-8B base + paper-released checkpoint"*. The HF API confirms the released checkpoint is **MIT** licensed (not Apache 2.0). Qwen3-8B base is Apache 2.0; the post-trained RLM checkpoint shifts to MIT. Both permissive, both compatible with anti-vendor-lock-in framing — but the precise license is MIT for citation accuracy.

## Empirical adoption signal

367 downloads + 61 likes (as of 2026-04-27) is modest absolute volume for a research checkpoint, but the artifact has been live ~3 months (released 2026-01-15) with a v0.1 → updated cycle (last modified 2026-02-20). It's not abandoned. Downloads/month ≈ 120, indicating sustained interest beyond the initial paper release.

## How to apply

Brain agents working on the RLM thread can:
- Update tier-0 comparison Question 2 from "unverified" to "released, mit-oasys/rlm-qwen3-8b-v0.1, MIT license, 16GB BF16 / ~8GB INT8".
- Move RLM-Qwen3-8B from "speculative-after-training" to "deployable-after-quantization" in tier-0 hardware compatibility analysis.
- Use `mit-oasys/rlm-qwen3-8b-v0.1` as the teacher RLM in the RLM-Qwen3.6-27B operations plan if operator's compute budget tightens (8B teacher cheaper than 480B Qwen3-Coder teacher).

## Source

AICP (`~/devops-expert-local-ai/`) — empirical HF API verification 2026-04-27 in response to operator's directive *"look at the second-brain... RLM for example"*.
Verification command:
```
curl -sS https://huggingface.co/api/models/mit-oasys/rlm-qwen3-8b-v0.1
```

## Relationships

- RELATES TO: [[model-registry|Model Registry]]

## Backlinks

[[model-registry|Model Registry]]
