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
updated: 2026-04-09
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

The specific failure was mechanical: the Read tool has a default line limit. When a subagent reads a raw file without specifying an offset or increased limit, it gets the first N lines (approximately 60 lines of content after the tool's overhead). For a 200-line file, this captures most of the content. For a 1,057-line file, it captures roughly 6% of the content — the introduction and maybe the first section heading.

The subagent does not know it is missing content. There is no error, no warning, no truncation indicator in the tool output. The subagent receives what looks like a complete read, synthesizes from that partial content, and produces a page that sounds authoritative but covers only the surface. The page passes validation (it has frontmatter, a summary, relationships, minimum word counts) because quality gates check structure, not depth relative to source.

The user discovered this when reviewing a source-synthesis page about context mode that seemed suspiciously thin compared to the raw transcript they had provided. The raw file was 1,057 lines. The wiki page covered content from approximately the first 60 lines.

The deeper lesson is about defect propagation in automated systems. The user's immediate reaction was not "fix this page" but "we have a systemic issue." This is the correct response. If the tool limitation affected one subagent, it affected every subagent dispatched with the same instructions. The investigation confirmed this: multiple source-synthesis pages created from long transcripts (YouTube transcripts of 500-1000+ lines) were shallow in the same way. Four pages required complete rewrites.

The fix had to operate at three levels:
1. **Immediate**: Rewrite the affected pages with full-file reads
2. **Methodology**: Add an explicit rule — subagent prompts must instruct to read the FULL file with multiple offset reads for files longer than the default limit
3. **Tooling**: Consider adding a quality check to the pipeline comparing raw file length vs. wiki page length as a depth heuristic

A per-instance fix (rewrite this one page) would have left the other affected pages undetected and the root cause unaddressed. Only a systemic fix (audit all similar artifacts + change the methodology + change the tool instructions) prevents recurrence.

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
[[[[Stage-Gate Methodology]] (depth gates should catch truncation)]]
[[[[Never Synthesize from Descriptions Alone]] (same depth-verification principle)]]
[[[[Immune System Rules]] (this lesson became a rule)]]
