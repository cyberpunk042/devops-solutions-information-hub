---
date: 2026-04-17
type: operator-directive
action: ingest-and-build-framework
status: in-progress
---

# 2026-04-17 — Directive: Model Evaluation Framework + Qwopus v3

## Verbatim operator message

> What about models like those:
> https://decrypt.co/364047/want-claude-opus-ai-potato-pc-next-best-bet
> (https://huggingface.co/Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled)
> https://huggingface.co/Jackrong/Qwopus3.5-27B-v3-GGUF
>
> At some point I dont know here to look and what to expect of what I see

## What this contains

1. Three sources about Jackrong's Qwopus distilled model — the article and two HuggingFace model pages (the base reasoning-distilled model AND the v3-GGUF specifically).
2. A meta-question: **the operator is lost in the flood of open-model announcements**. "I don't know where to look and what to expect."

## This is the more important gap

The second half of the message is a framework gap, not just an ingestion request. Across this session we ingested AirLLM, gpt-oss, Qwopus — each time with ad-hoc synthesis. The operator is asking: **what is the stable evaluation framework so future model announcements are not individually exhausting?**

This requires a wiki artifact — a reference / guide that codifies:
- Where to look when a new model drops (authoritative sources, not marketing)
- What to extract in a standard order (size, active params, license, quantization, context, benchmarks, agentic features, deployment maturity)
- What to expect vs what to be suspicious of (red flags, aspirational claims, latency-math traps)
- How to slot it into the routing table / decide to test it
- When to ignore vs when to integrate

## Action plan

1. Fetch the three sources.
2. Verify / update Qwopus synthesis if v3 or the distilled-reasoning model bring new facts.
3. Build an evaluation framework as a wiki reference page — consumable artifact the operator can re-use.
4. Update Model — Local AI to point at the new framework.
5. Pipeline post.
