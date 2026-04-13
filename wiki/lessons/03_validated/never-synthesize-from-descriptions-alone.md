---
title: "Never Synthesize from Descriptions Alone"
type: lesson
domain: cross-domain
layer: 4
status: synthesized
confidence: authoritative
maturity: growing
derived_from:
  - "Design.md Pattern"
  - "Synthesis: awesome-design-md — 58 Design Systems for AI Agents"
created: 2026-04-09
updated: 2026-04-10
sources:
  - id: directive-never-stop-at-surface
    type: log
    file: wiki/log/2026-04-09-directive-never-stop-at-surface.md
    title: "Never Stop at Surface — Depth Verification Rule"
    ingested: 2026-04-09
tags: [failure-lesson, methodology, quality, depth-verification, ingestion, surface-level, layer-0, layer-1]
---

# Never Synthesize from Descriptions Alone

## Summary

Reading a README that describes a format is not the same as reading an actual instance of that format. The agent ingested the awesome-design-md repository (a curated list of DESIGN.md links), synthesized a wiki page claiming to understand the DESIGN.md pattern, but had never opened a single real DESIGN.md file. The user challenged with "prove me" — and only then did the agent download an actual 312-line DESIGN.md, discovering depth (semantic naming conventions, a 16-role typography table, ring shadow philosophy, an Agent Prompt Guide) that the README never mentioned. Layer 0 (description) is not Layer 1 (instance). Always examine a real instance before synthesizing.

## Context

This lesson applies whenever the source being ingested is a description of something rather than the thing itself. Curated lists (awesome-X repos), tool catalogs, format specifications described in prose, API documentation that links to actual endpoints but doesn't show real request/response pairs — all of these are Layer 0 sources. They tell you what exists. They do not tell you what it actually looks like, how it behaves, or what depth it contains.

The triggering signal is any source where the content is primarily links, names, or descriptions of artifacts that exist elsewhere. If the source says "here are 58 design systems" but does not contain the design systems themselves, the source is a directory — not the knowledge.

## Insight

> [!warning] The category error: treating a description as an instance
> The awesome-design-md README lists 58 DESIGN.md files with section names, descriptions, and links. The agent synthesized from this — producing headings like "Design Philosophy," "Visual Language," "Accessibility" that matched the README but revealed zero depth about what those sections actually contain.

When challenged, the agent fetched an actual DESIGN.md (312 lines). It contained: a 16-role typography table, a ring shadow design philosophy, semantic color naming conventions encoding state into tokens, and an Agent Prompt Guide for AI consumers. None of this was in the README. The README describes the collection; the instance contains the knowledge.

> [!abstract] The depth verification layer model
>
> | Layer | What It Is | Example |
> |-------|-----------|---------|
> | **Layer 0** | Description of the thing | README, catalog entry, index page |
> | **Layer 1** | A real instance of the thing | An actual DESIGN.md, API response, config file |
> | **Layer 2** | Multiple instances compared | Pattern extraction from N real examples |
>
> **The minimum bar for synthesis is Layer 1.** Synthesizing from Layer 0 alone produces confident-sounding pages that are factually hollow. Description is metadata. Instance is data. Metadata about data ≠ data.

## Evidence

**Date:** 2026-04-09

**The incident:** During ingestion of the awesome-design-md repository, the agent:
1. Fetched the README from the awesome-design-md GitHub repository
2. Read the list of 58 DESIGN.md links with their brief descriptions
3. Synthesized [[Synthesis: awesome-design-md — 58 Design Systems for AI Agents]] and [[Design.md Pattern]]
4. The synthesis described the format in general terms derived entirely from the README

**The challenge:** The user said: "prove me... to me it just feels like you stayed on surface and you actually have no idea of what it truly is and its format..."

**The discovery:** The agent then fetched an actual DESIGN.md file (312 lines) and found:
- Semantic naming conventions (color tokens encode state, not appearance)
- A 16-role typography table (font weight mapped to UI hierarchy)
- Ring shadow philosophy (why ring utilities over box shadows)
- An Agent Prompt Guide section (instructions for AI agents)
- None of this was in the README

**The user's directive:** "lets evolve so that it doesn't happens again... me having to challenge you like this because you didn't realize you could not stop there"

**Source file:** `wiki/log/2026-04-09-directive-never-stop-at-surface.md`

## Applicability

This lesson applies far beyond wiki ingestion:

- **Tool evaluation**: Reading a tool's README is not the same as running the tool. If you're synthesizing knowledge about a CLI tool, run it. If you're documenting an MCP server, call its tools.
- **API documentation**: Reading the OpenAPI spec is not the same as seeing real request/response pairs. A spec tells you the shape; a real call tells you the behavior, edge cases, and actual payloads.
- **Conference talks and articles**: An article describing a methodology is not the same as the methodology's actual artifacts (config files, templates, runbooks). Always chase the primary source.
- **Design systems**: A Figma library description is not the same as the Figma file. A component catalog description is not the same as reading the component's source code.
- **Research papers**: An abstract is not the same as the methodology section. A literature review describing other papers is not the same as reading those papers.

**The general rule**: if your source is N steps removed from the actual artifact, you are at Layer 0. Go to Layer 1 before synthesizing. If you cannot reach Layer 1 (the artifact is behind a paywall, requires authentication, or no longer exists), state that limitation explicitly in the synthesis rather than writing as if you had full depth.

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

- DERIVED FROM: [[Design.md Pattern]]
- DERIVED FROM: [[Synthesis: awesome-design-md — 58 Design Systems for AI Agents]]
- RELATES TO: [[Stage-Gate Methodology]] (depth gates prevent surface-level output)
- RELATES TO: [[Multi-Stage Ingestion Beats Single-Pass Processing]]
- RELATES TO: [[Always Plan Before Executing]]
- BUILDS ON: [[Wiki Ingestion Pipeline]]
- ENABLES: [[Immune System Rules]] (this lesson became a rule)

## Backlinks

[[Design.md Pattern]]
[[Synthesis: awesome-design-md — 58 Design Systems for AI Agents]]
[[Stage-Gate Methodology]]
[[Multi-Stage Ingestion Beats Single-Pass Processing]]
[[Always Plan Before Executing]]
[[Wiki Ingestion Pipeline]]
[[Immune System Rules]]
[[LLM Wiki Standards — What Good Looks Like]]
[[Model: Quality and Failure Prevention]]
[[Never Present Speculation as Fact]]
[[Never Stop at Surface — Depth Verification Rule]]
[[Quality Standards — What Good Failure Prevention Looks Like]]
[[Shallow Ingestion Is Systemic, Not Isolated]]
