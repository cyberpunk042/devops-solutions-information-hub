---
title: Stop Guessing — False Claims in Models
aliases:
  - "Stop Guessing — False Claims in Models"
type: note
domain: log
note_type: directive
status: active
confidence: high
created: 2026-04-09
updated: 2026-04-13
sources: []
tags: [log, directive, quality, honesty, false-claims, context-management]
---

# Stop Guessing — False Claims in Models

## Summary

The models contain fabricated claims presented as facts. The context degradation curve table states hard thresholds (20%, 40%, 60%, 80%) as if they're deterministic, when in reality context degradation is probabilistic and a well-driven session can reach 0% remaining without issues. The agent is generalizing, guessing, and presenting low-quality information as authoritative.

## Operator Directive (verbatim)

> This is completley false... you are generalizing at which window it is more probably to have such an event but this is completly random... you could reach the 0% remaining without a single hickups.... especialy well driven and wired.....
>
> Everything you write is low level and miss-informed... clearly we lack quality of information still.
>
> No you are minizing and guessing everything and you didn't even look at what I told you and document it properly....

## What Failed

1. **The context degradation table is fabricated** — it presents probabilistic tendencies as deterministic thresholds. "Unreliable at 60%" is false — a well-structured session with clean CLAUDE.md, proper skills, and good context management can work effectively at 80%+ utilization.
2. **The agent didn't read what the user pointed to** — the user said to look at OpenArms methodology evolution, but the agent skimmed it and added surface-level additions instead of deeply understanding and integrating the learnings.
3. **Minimizing** — instead of doing deep work, the agent declared models "done" after shallow additions and asked to move to the next one.
4. **Guessing** — presenting speculation as knowledge. If the agent doesn't have verified data, it must say so, not fabricate thresholds.

## The Rule

- NEVER present speculation as fact
- NEVER fabricate data points or thresholds without sources
- If the information is not verified, say "this is unverified" or "this needs research"
- Quality of information > quantity of pages
- We clearly LACK quality information — the solution is MORE RESEARCH, not more guessing

## Relationships

- FEEDS INTO: [[never-present-speculation-as-fact|Never Present Speculation as Fact]]

- RELATES TO: [[model-registry|Model Registry]]

## Backlinks

[[never-present-speculation-as-fact|Never Present Speculation as Fact]]
[[model-registry|Model Registry]]
