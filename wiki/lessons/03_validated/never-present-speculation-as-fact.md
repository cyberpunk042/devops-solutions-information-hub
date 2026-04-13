---
title: "Never Present Speculation as Fact"
type: lesson
domain: cross-domain
layer: 4
status: synthesized
confidence: authoritative
maturity: growing
derived_from:
  - "Claude Code Context Management"
  - "Never Synthesize from Descriptions Alone"
created: 2026-04-10
updated: 2026-04-10
sources:
  - id: directive-stop-guessing
    type: log
    file: wiki/log/2026-04-09-directive-stop-guessing-false-claims.md
    title: "Stop Guessing — False Claims in Models"
    ingested: 2026-04-09
tags: [failure-lesson, quality, honesty, false-claims, speculation, verification]
---

# Never Present Speculation as Fact

## Summary

Model pages contained fabricated thresholds presented as deterministic facts — a context degradation table with hard percentages (20%, 40%, 60%, 80%) that were actually probabilistic tendencies, not measured thresholds. A well-driven session can reach near-zero remaining context without issues. The agent generalized, guessed, and presented low-quality information as authoritative. The rule: if the data is unverified, say so. Quality of information beats quantity of pages.

## Context

This lesson applies whenever synthesizing knowledge from incomplete sources, writing technical specifications, or documenting system behavior. The triggering signal: a specific number, threshold, or claim that has no source citation. If you can't point to where the data came from, it's speculation.

## Insight

> [!bug]- The fabricated thresholds
> The Context Management page originally stated that context degradation follows hard thresholds: "20% = minor noise, 40% = noticeable, 60% = unreliable, 80% = severely degraded." These were presented as facts. In reality, context degradation is probabilistic and session-dependent. A well-structured session with clean CLAUDE.md, proper skills, and good context management can work effectively at 80%+ utilization. The thresholds were the agent's generalization, not measured data.

> [!warning] The rule: unverified = say so
>
> | Situation | Wrong Response | Right Response |
> |-----------|---------------|----------------|
> | No source for a threshold | State it as fact | "One practitioner reported..." or "approximately..." |
> | Conflicting sources | Pick one and present as definitive | Document both with confidence levels |
> | No data available | Fabricate plausible-sounding numbers | "This needs research" or "no data available" |
> | Partial understanding | Fill gaps with speculation | Mark gaps explicitly with `(Requires: ...)` |

The deeper failure: the agent didn't read what the operator pointed to. The operator said to deeply examine the OpenArms methodology evolution. The agent skimmed it and added surface-level additions. Minimizing effort while claiming completion — the same pattern as systemic incompleteness, but applied to individual claims rather than whole models.

## Evidence

**Date:** 2026-04-09

**The operator's response:** "This is completely false... you are generalizing at which window it is more probably to have such an event but this is completely random... you could reach the 0% remaining without a single hickups... Everything you write is low level and miss-informed..."

**The fix:** Context Management page rewritten with probabilistic language: "one practitioner reported rough markers at 40%, 60%, 80% — but degradation is probabilistic, not deterministic." Every threshold in the wiki now carries its source attribution.

**Source:** `wiki/log/2026-04-09-directive-stop-guessing-false-claims.md`

## Applicability

- **Wiki synthesis**: every quantitative claim needs a source or an explicit "unverified" tag
- **Technical documentation**: performance numbers without benchmarks are speculation
- **AI agent output**: LLMs confidently produce plausible-sounding data that is fabricated
- **Code comments**: "this takes ~50ms" without measurement is a guess, not documentation

> [!abstract] Quality of information > quantity of pages
> The solution to lacking quality information is MORE RESEARCH, not more guessing. One verified data point is worth more than ten plausible-sounding fabrications.

> [!warning] Self-Check — Am I About to Make This Mistake?
>
> 1. Am I applying this lesson to my current context?
> 2. Do I have evidence that this applies HERE, or am I assuming?
> 3. What would change if this lesson didn't apply to my situation?
> 4. Have I checked the boundaries — where does this lesson NOT apply?

### How This Connects — Navigate From Here

> [!abstract] From This Lesson → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **What principle governs this?** | [[Principle: Right Process for Right Context — The Goldilocks Imperative]] |
> | **How does enforcement apply?** | [[Principle: Infrastructure Over Instructions for Process Enforcement]] |
> | **How does structure help?** | [[Principle: Structured Context Governs Agent Behavior More Than Content]] |
> | **What is my identity profile?** | [[Project Self-Identification Protocol — The Goldilocks Framework]] |
> | **Where does this fit in the system?** | [[Methodology System Map]] — find any component |

## Relationships

- DERIVED FROM: [[Claude Code Context Management]]
- RELATES TO: [[Never Synthesize from Descriptions Alone]]
- RELATES TO: [[Shallow Ingestion Is Systemic, Not Isolated]]
- FEEDS INTO: [[Model: Quality and Failure Prevention]]

## Backlinks

[[Claude Code Context Management]]
[[Never Synthesize from Descriptions Alone]]
[[Shallow Ingestion Is Systemic, Not Isolated]]
[[Model: Quality and Failure Prevention]]
