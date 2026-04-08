# Design.md Pattern — Research Notes

Compiled: 2026-04-08
Sources: GitHub VoltAgent/awesome-design-md, MindStudio blog, Google Stitch blog

## What is DESIGN.md?

A plain-text design system document that AI agents read to generate consistent UI. Introduced by Google Stitch (Google Labs). Enables developers to communicate design specifications to AI coding assistants without specialized tools or exports.

## 9-Section Structure (from awesome-design-md)

1. Visual Theme & Atmosphere — Design philosophy and mood
2. Color Palette & Roles — Semantic colors with hex values and functional purposes
3. Typography Rules — Font families and complete type hierarchy
4. Component Stylings — Button, card, input, and navigation specs with states
5. Layout Principles — Spacing scales, grids, whitespace approaches
6. Depth & Elevation — Shadow systems and surface hierarchies
7. Do's and Don'ts — Design guardrails and anti-patterns
8. Responsive Behavior — Breakpoints, touch targets, collapse strategies
9. Agent Prompt Guide — Quick color references and ready-to-use prompts

## How Google Stitch Uses It

When you submit a prompt to Stitch, it passes your prompt PLUS the full design.md as context to Gemini. The model treats the design file as binding constraints.

## Ecosystem

- 58 DESIGN.md files in awesome-design-md repo (Claude, Stripe, Vercel, Linear, Figma, Spotify, Tesla, etc.)
- Companion: AGENTS.md (how to build) vs DESIGN.md (how it should look)
- Preview files: preview.html and preview-dark.html visual catalogs
- Tools: Google Stitch, Claude Code, Cursor, Gemini CLI, Antigravity

## Relationship to CLAUDE.md

CLAUDE.md = project instructions for coding agent behavior
DESIGN.md = visual design system for UI consistency
AGENTS.md = build instructions (how to construct, not how it looks)

These are complementary markdown files that together give an AI agent complete context.

## Key Insight

The broader pattern: project-root markdown files as persistent AI context. CLAUDE.md was first, DESIGN.md extends it to visual design, AGENTS.md extends it to build processes. The ecosystem is converging on "markdown as AI configuration."
