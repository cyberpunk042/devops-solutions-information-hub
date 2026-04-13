---
title: Never Stop at Surface — Depth Verification Rule
aliases:
  - "Never Stop at Surface — Depth Verification Rule"
type: note
domain: log
note_type: directive
status: active
confidence: high
created: 2026-04-09
updated: 2026-04-09
sources: []
tags: [log, directive, methodology, quality, depth]
---

# Never Stop at Surface — Depth Verification Rule

## Summary

When ingesting a source, reading a README about a format is NOT the same as reading an actual instance of that format. The agent must verify depth by examining real artifacts, not just their descriptions.

## Operator Directive (verbatim)

> prove me..... to me it just feels like you stayed on surface and you actually have no idea of what it trully is and its format...

> lets evolve so that it doesn't happens again.... me having to challenge you like this because you didn't realize you could not stop there

## The Pattern That Failed

1. Fetched awesome-design-md README (list of links + section names)
2. Synthesized a page from the README description
3. Claimed to understand the format without ever reading an actual DESIGN.md file
4. User had to challenge: "prove me... you have no idea of what it truly is"
5. Only then downloaded an actual 312-line DESIGN.md and discovered the real depth

## The Rule

When ingesting a source that DESCRIBES a format, tool, or pattern:
- The description is Layer 0 (surface)
- An actual INSTANCE of the thing is Layer 1 (evidence)
- You MUST reach Layer 1 before synthesizing

Examples:
- Ingesting a DESIGN.md collection → download and read an actual DESIGN.md file
- Ingesting an MCP server → check its actual tool list, not just the README
- Ingesting a skill repo → read the actual SKILL.md content
- Ingesting a methodology → read the actual config/artifacts, not just the docs about them

This is the same principle as "read the full file" but at a higher level: read the actual THING, not just the description of the thing.

## Relationships

- FEEDS INTO: [[never-synthesize-from-descriptions-alone|Never Synthesize from Descriptions Alone]]

## Backlinks

[[never-synthesize-from-descriptions-alone|Never Synthesize from Descriptions Alone]]
