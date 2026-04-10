---
title: "The Wiki Is a Hub, Not a Silo"
type: lesson
domain: cross-domain
layer: 4
status: synthesized
confidence: authoritative
maturity: seed
derived_from:
  - "Four-Project Ecosystem"
  - "Model: Ecosystem Architecture"
created: 2026-04-10
updated: 2026-04-10
sources:
  - id: directive-hub-mindset
    type: log
    file: wiki/log/2026-04-09-directive-quality-models-hub-mindset.md
    title: "Quality Models — Hub Mindset — OpenArms Methodology Learnings"
    ingested: 2026-04-09
tags: [lesson, hub, ecosystem, aggregation, cross-project, knowledge-flow]
---

# The Wiki Is a Hub, Not a Silo

## Summary

The research wiki is not a standalone documentation project — it is the central intelligence hub that aggregates knowledge from ALL ecosystem projects (OpenArms, OpenFleet, AICP, devops-control-plane) and feeds processed knowledge back to them. The operator's directive: "we are going to need to the best ways to start acting like this project is really the hub and aggregate the learnings from everywhere." Models must incorporate learnings from sister projects, not just from ingested articles and transcripts.

## Context

This lesson applies whenever the wiki is treated as a self-contained project rather than a cross-project knowledge aggregator. The triggering signal: model pages that reference only ingested web sources without incorporating operational learnings from the ecosystem's own projects.

## Insight

> [!tip] Hub mindset: aggregate in, feed back out
>
> | Direction | What Flows | Mechanism |
> |-----------|-----------|-----------|
> | **Projects → Wiki** | Operational learnings, methodology evolution, failure post-mortems | `pipeline scan ../project/`, manual ingestion of project docs |
> | **Wiki → Projects** | Synthesized models, standards, patterns, decisions | `pipeline export`, LightRAG via kb_sync.py, AICP docs/kb/ |
> | **Wiki → Wiki** | Evolution pipeline promotes seed → growing → mature → canonical | `pipeline evolve`, cross-referencing, gap analysis |

The wiki's value scales with the number of projects feeding it. A wiki that only ingests external articles is a reading digest. A wiki that also ingests operational learnings from 5 ecosystem projects is a compound knowledge engine — each project's experience enriches every other project's models.

The operator specifically pointed to OpenArms' methodology evolution as a source the wiki should deeply ingest — not as an external article, but as insider operational knowledge that should upgrade the Methodology model. This is what hub mindset means: the wiki doesn't just DOCUMENT the ecosystem, it LEARNS from it.

## Evidence

**Date:** 2026-04-09

**The operator's directive:** "this project must act as the real hub and aggregate the learnings from everywhere, like we will do now and you will deepen as we go like your clear lack of understanding of which extent reach openarms."

**The gap:** Model pages referenced ingested web sources (YouTube transcripts, GitHub repos) but not the ecosystem's own operational data. The Methodology model didn't incorporate OpenArms' methodology evolution. The Claude Code model didn't incorporate OpenFleet's agent execution experience.

**Source:** `wiki/log/2026-04-09-directive-quality-models-hub-mindset.md`

## Applicability

- **Model building**: every model should cross-reference operational data from ecosystem projects, not just external sources
- **Evolution pipeline**: `pipeline scan ../project/` should be a regular operation, not a one-time setup
- **Export profiles**: the wiki feeds sister projects — this feedback loop is the hub in action
- **Knowledge flow**: the Four-Project Ecosystem page's knowledge loop (operational work → post-mortem → rules → wiki → LightRAG → agents → better work) IS the hub architecture

## Relationships

- DERIVED FROM: [[Four-Project Ecosystem]]
- RELATES TO: [[Model: Ecosystem Architecture]]
- RELATES TO: [[Knowledge Evolution Pipeline]]
- FEEDS INTO: [[Research Pipeline Orchestration]]

## Backlinks

[[Four-Project Ecosystem]]
[[Model: Ecosystem Architecture]]
[[Knowledge Evolution Pipeline]]
[[Research Pipeline Orchestration]]
