---
title: "Shallow Ingestion Is Systemic, Not Isolated"
type: lesson
domain: cross-domain
layer: 4
status: synthesized
confidence: authoritative
maturity: growing
derived_from:
  - "Knowledge Evolution Pipeline"
  - "Wiki Ingestion Pipeline"
created: 2026-04-09
updated: 2026-04-10
sources:
  - id: directive-systemic-shallow-ingestion
    type: log
    file: raw/notes/2026-04-09-user-directive-systemic-shallow-ingestion.md
    title: "User Directive — Systemic Shallow Ingestion Issue"
    ingested: 2026-04-09
tags: [failure-lesson, methodology, quality, systemic-issue, shallow-ingestion, subagent, read-tool, truncation, audit]
---

# Shallow Ingestion Is Systemic, Not Isolated

## Summary

Subagents consistently read only the first ~60 lines of raw files that were 300-1000+ lines long, due to the Read tool's default line limit. A source-synthesis page was discovered to cover only the introduction of a 1,057-line file. When the user identified this, the critical realization was not "fix this one page" — it was "WTF happened in the first place... we have a systemic issue in our system." Every subagent dispatched for ingestion had the same tool limitation and the same default behavior. Four source pages had to be rewritten after audit. When you find one quality problem, audit for the same pattern across ALL similar artifacts. The fix must be systemic (methodology rule + tool instruction), not per-instance.

## Context

This lesson applies whenever a quality defect is discovered in an artifact produced by an automated or semi-automated process. The triggering question is not "how do we fix this page?" but "how many other pages have the same problem?" If the defect was caused by a tool limitation, a default setting, or a shared instruction template, then every artifact produced by that same tool/setting/template is suspect.

This is especially relevant in systems that use subagents, parallel workers, or batch processing — any architecture where the same operation is replicated across many inputs. A bug in the operation is a bug in every output.

## Insight

> [!bug]- The mechanical failure: silent truncation
> The Read tool has a default line limit. A subagent reading a 1,057-line file gets ~60 lines — 6% of content. No error, no warning, no truncation indicator. The subagent receives what looks like a complete read, synthesizes from 6%, and produces a page that sounds authoritative but covers only the introduction. The page passes validation because quality gates check structure, not depth relative to source.

> [!warning] When one subagent hits a limit, ALL subagents hit the same limit
> The user's reaction was not "fix this page" but "we have a systemic issue." If the tool limitation affected one subagent, it affected every subagent dispatched with the same instructions. Investigation confirmed: multiple source-synthesis pages from long transcripts (500-1000+ lines) were shallow. Four required complete rewrites.

The fix had to operate at three levels:

> [!tip] Three-level systemic fix
>
> | Level | Action |
> |-------|--------|
> | **Immediate** | Rewrite affected pages with full-file reads |
> | **Methodology** | Subagent prompts must instruct: read FULL file with multiple offset reads for files >200 lines |
> | **Tooling** | Pipeline quality check comparing raw file length vs wiki page length (≥0.25 ratio) |
>
> A per-instance fix would have left other affected pages undetected and the root cause unaddressed.

## Evidence

**Date:** 2026-04-09

**The incident:** A source-synthesis page for context mode was created from a 1,057-line raw transcript. The subagent read only the first ~60 lines due to the Read tool's default line limit. The resulting wiki page covered only the introduction of the source material.

**The user's response (verbatim):** "WTF happened in the first place... we have a systemic issue in our system"

**The scope of damage:**
- All 20 source-synthesis pages created by subagents were suspect
- Pages synthesized from long transcripts (12 YouTube transcripts, some 500+ lines) and detailed READMEs were most likely affected
- 4 source pages were confirmed shallow and required complete rewrites after audit

**Root cause:** The Read tool's default line limit silently truncates long files. Subagents receive no indication that they are working with partial content. The ingestion methodology did not instruct subagents to verify file length or use multiple offset reads.

**Required fix (identified by the user):**
1. Audit all source-synthesis pages for depth vs. raw file length
2. Update methodology: subagent prompts must instruct to read FULL files with multiple offset reads
3. Add to evolve/wiki-agent skill: "always verify raw file length before synthesizing"
4. Consider pipeline quality check: raw file length vs. wiki page length ratio

**Source file:** `raw/notes/2026-04-09-user-directive-systemic-shallow-ingestion.md`

## Applicability

This lesson applies to any system where automated agents produce artifacts from input data:

- **LLM subagent pipelines**: Any architecture that dispatches subagents with tool access must account for tool default limits. If one subagent hits a limit, all subagents hit the same limit.
- **ETL pipelines**: A data transformation that silently truncates input produces incorrect output for every record above the truncation threshold. The fix is never "reprocess this one record."
- **CI/CD**: A test runner that silently skips tests above a timeout threshold creates a systemic coverage gap, not an isolated failure.
- **Code generation**: An AI code generator that reads only the first N lines of a specification file will produce incomplete implementations for every spec longer than N lines.
- **Quality assurance**: Any quality gate that checks structure but not depth relative to source will pass shallow artifacts. Depth checks require comparing output to input, not just validating output in isolation.

**The general principle**: when you discover a defect caused by a shared mechanism (tool default, configuration setting, instruction template), the defect count equals the number of artifacts produced through that mechanism, not 1. Audit all of them. Fix the mechanism. Then verify the fix prevents recurrence.

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

- DERIVED FROM: [[Knowledge Evolution Pipeline]]
- DERIVED FROM: [[Wiki Ingestion Pipeline]]
- RELATES TO: [[Multi-Stage Ingestion Beats Single-Pass Processing]]
- RELATES TO: [[Automated Knowledge Validation Prevents Silent Wiki Decay]]
- RELATES TO: [[Stage-Gate Methodology]] (depth gates should catch truncation)
- BUILDS ON: [[Never Synthesize from Descriptions Alone]] (same depth-verification principle)
- ENABLES: [[Immune System Rules]] (this lesson became a rule)

## Backlinks

[[Knowledge Evolution Pipeline]]
[[Wiki Ingestion Pipeline]]
[[Multi-Stage Ingestion Beats Single-Pass Processing]]
[[Automated Knowledge Validation Prevents Silent Wiki Decay]]
[[Stage-Gate Methodology]]
[[Never Synthesize from Descriptions Alone]]
[[Immune System Rules]]
[[LLM Wiki Standards — What Good Looks Like]]
[[Model: Quality and Failure Prevention]]
[[Never Present Speculation as Fact]]
