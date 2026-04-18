---
date: 2026-04-17
type: operator-directive
action: ingest
status: in-progress
---

# 2026-04-17 — Directive: Unsloth + LoRA Feasibility Question

## Verbatim operator message

> continue
>
> Oh and this:
> https://github.com/unslothai/unsloth
>
> Is this reallly possible to create LoRA ? I guess it would take forever on my small GPUs ?
> I read that LoRA modification / tweak are really powerfull..

## What this contains

1. Source to ingest: Unsloth repository (the Qwopus training stack already referenced it).
2. Three real questions beyond the ingestion:
   - Is LoRA creation actually feasible *for the operator*?
   - How long does it take on 19 GB VRAM ("small GPUs")?
   - Is the "LoRA is really powerful" claim something to act on?

This is the natural follow-on from Qwopus — Qwopus was trained with Unsloth + LoRA on consumer hardware. The operator is now asking: "can I do that too?"

## Key facts to verify in the fetch

- Unsloth speedup claim: "2x faster, 80% less memory"
- Consumer hardware feasibility threshold (what VRAM minimum?)
- LoRA rank vs full fine-tuning trade-off
- What "powerful" actually means for LoRA (base-model capability inherited; domain adaptation possible)
- Training time estimates for common scenarios

## Action plan

1. Fetch Unsloth README and key docs
2. Create source synthesis
3. Answer the three specific questions with concrete numbers
4. Consider: does Model — Local AI need a "fine-tuning tier" (currently it is inference-only)?
5. Connect to Qwopus (already referenced Unsloth in training pipeline)
6. Principle-4 check: "really powerful" = declaration; what is the verification?
7. Pipeline post.
