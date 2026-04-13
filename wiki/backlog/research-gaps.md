---
title: Research Gaps — Empirical Questions Requiring Data
aliases:
  - "Research Gaps — Empirical Questions Requiring Data"
type: reference
domain: backlog
status: active
confidence: high
maturity: growing
created: 2026-04-13
updated: 2026-04-13
sources: []
tags: [backlog, research, gaps, empirical, measurement, open-questions]
---

# Research Gaps — Empirical Questions Requiring Data

## Summary

Open questions across the wiki that cannot be resolved by reasoning alone — they need empirical measurement, benchmarking, external research, or operational data. These are the genuine research gaps that will get answered through new source ingestion (E021), operational measurement, or dedicated research spikes.

## Automation & Pipelines

| # | Question | Source Page | What's Needed |
|---|----------|------------|---------------|
| 1 | Can post-chain steps be parallelized safely? | [[model-automation-pipelines\|Model — Automation and Pipelines]] | Technical analysis of step dependencies |
| 2 | What should failure recovery do — partial repair or halt? | [[model-automation-pipelines\|Model — Automation and Pipelines]] | Design decision after observing failure patterns |
| 3 | What quality score triggers auto-filing from session hooks? | [[model-automation-pipelines\|Model — Automation and Pipelines]] | Threshold design from session crystallization experiments |
| 4 | How many deepening passes before diminishing returns? | [[model-automation-pipelines\|Model — Automation and Pipelines]] | Empirical measurement across multi-pass ingestions |

## Local AI & Routing

| # | Question | Source Page | What's Needed |
|---|----------|------------|---------------|
| 5 | What is the empirical routing split after AICP Stage 3? | [[model-local-ai\|Model — Local AI ($0 Target)]] | Measurement after Stage 3 operational |
| 6 | How should the router handle context window overflow? | [[model-local-ai\|Model — Local AI ($0 Target)]] | Design: split task vs escalate to cloud |
| 7 | Should AICP profile be auto-selected per operation? | [[model-local-ai\|Model — Local AI ($0 Target)]] | Usage pattern analysis after AICP matures |

## Second Brain Theory

| # | Question | Source Page | What's Needed |
|---|----------|------------|---------------|
| 8 | At what relationship density does a wiki become a "second brain"? | [[model-second-brain\|Model — Second Brain]] | Scale data from wiki growth over time |
| 9 | Should stale pages be actively archived or passively marked? | [[model-second-brain\|Model — Second Brain]] | Policy design after observing staleness patterns |
| 10 | At what page count does Zettelkasten emergence start? | [[model-second-brain\|Model — Second Brain]] | Longitudinal observation — wiki is at 296 pages |

## Context Engineering

| # | Question | Source Page | What's Needed |
|---|----------|------------|---------------|
| 11 | What is the optimal block size for agent processing? | [[structured-context-is-proto-programming-for-ai-agents\|Structured Context Is Proto-Programming]] | Empirical testing of different context block sizes |
| 12 | What is the optimal context budget per tier? | [[model-context-engineering\|Model — Context Engineering]] | Measurement of output quality vs context size |

## Knowledge Evolution

| # | Question | Source Page | What's Needed |
|---|----------|------------|---------------|
| 13 | What graph density metric triggers the need for LightRAG? | [[model-knowledge-evolution\|Model — Knowledge Evolution]] | Scale testing: when does keyword search fail? |
| 14 | What is the quality delta between LocalAI and Claude evolution? | [[model-knowledge-evolution\|Model — Knowledge Evolution]] | Side-by-side comparison after AICP Stage 3 |

## Quality & Measurement

| # | Question | Source Page | What's Needed |
|---|----------|------------|---------------|
| 15 | What is the empirical rework rate across ingestion modes? | [[model-quality-failure-prevention\|Model — Quality and Failure Prevention]] | Track rework per mode (auto, guided, smart) over time |

## NotebookLM Operations

| # | Question | Source Page | What's Needed |
|---|----------|------------|---------------|
| 16 | When to archive vs delete vs keep completed research notebooks? | [[model-notebooklm\|Model — NotebookLM]] | Policy design from operational experience |
| 17 | Can wiki export pages as notebook source set for bidirectional grounding? | [[model-notebooklm\|Model — NotebookLM]] | Technical feasibility via notebooklm-py |
| 18 | How much does artifact quality vary across NotebookLM generation types? | [[model-notebooklm\|Model — NotebookLM]] | Systematic comparison of output types |

## How to Use This Page

These gaps get resolved through:
1. **E021 New Source Ingestion** — external research may answer theoretical questions
2. **Operational measurement** — tracking metrics during normal wiki work
3. **Research spikes** — dedicated investigation using the research methodology model
4. **Sister project feedback** — OpenArms/OpenFleet operational data

When a gap is answered, update the source page's `[!question]` callout with RESOLVED + evidence.

## Relationships

- RELATES TO: [[e021-new-source-ingestion-10-15-sources-through-full-pipeline\|E021 — New Source Ingestion]]
- RELATES TO: [[model-methodology\|Model — Methodology]]
- RELATES TO: [[operator-decision-queue\|Operator Decision Queue]]

## Backlinks

[[E021 — New Source Ingestion]]
[[model-methodology|Model — Methodology]]
[[operator-decision-queue|Operator Decision Queue]]
