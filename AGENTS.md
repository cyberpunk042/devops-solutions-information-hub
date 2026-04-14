# AGENTS.md — Universal Agent Context

This file is the **cross-tool universal context** for this project. Read by Claude Code, Codex CLI, Copilot CLI, Gemini CLI, Cursor, OpenCode, and any other tool that supports the [Agentic AI Foundation AGENTS.md standard](https://agents-standard.org).

Claude Code reads this AND CLAUDE.md. Other tools read only this file.

## What This Project Is

This is a **research-grade knowledge synthesis system** — the central intelligence hub for a 5-project DevOps ecosystem. It is a production system (used daily, 316+ pages) maintained by an LLM agent through structured markdown with graph-based relationships.

See [README.md](README.md) for full project overview. See [CONTEXT.md](CONTEXT.md) for identity profile and current phase.

## Sacrosanct Operator Directives (Verbatim — Never Paraphrase)

> "not only not dumb raw dump but smart content and then to the full requirements / standards"
> "we need to establish a strong method of work with the Wiki LLM structure and Methodology"
> "do not confuse everything. the words are important. goldilock is not model and model is not standard and standard is not example and example is not template and none of this is knowledge but knowledge is at all their layers."
> "fix it at the root instead.. its not hard" — solve problems with tooling, not manual work
> "Preach by example."

## Hard Rules (MANDATORY — numbered, no exceptions)

1. **NEVER skip stages.** Document before Design. Design before Scaffold. Scaffold before Implement. Implement before Test.
2. **NEVER write code during document/design.** Understanding first, then building.
3. **ALWAYS log operator directives verbatim** in `raw/notes/` BEFORE acting. Core methodology, proactive, not reactive.
4. **ALWAYS read full files before synthesizing.** `wc -l` first. Offset reads for >200 lines. Page ≥0.25× source length.
5. **ALWAYS verify depth.** Source DESCRIBES a thing → you MUST read a real INSTANCE. README ≠ understanding.
6. **ALWAYS run `python3 -m tools.pipeline post`** after wiki changes. 6-step validation chain. 0 errors required.
7. **NEVER claim done without evidence.** Run the command. Show the output. 0 errors = done.

## Stage Gates (Enforced)

| Stage | Readiness | ALLOWED | FORBIDDEN |
|-------|-----------|---------|-----------|
| **Document** | 0→25% | Wiki pages, raw/notes/ logs, research | Implementation code, tool modifications |
| **Design** | 25→50% | Design docs, decision pages, specs | Implementation code, tool modifications |
| **Scaffold** | 50→80% | Templates, config files, schema changes, empty stubs | Business logic, real implementations |
| **Implement** | 80→95% | Code, config, wiki pages, tool changes | Test modifications |
| **Test** | 95→100% | Test implementations, validation runs | New features, scope changes |

"Continue" = advance within CURRENT stage. NOT skip to next stage.

## Methodology Models (Choose the Right One)

| Task Type | Model | Stages |
|-----------|-------|--------|
| epic/module/task | feature-development | document → design → scaffold → implement → test |
| bug | bug-fix | document → implement → test |
| research/spike | research | document → design |
| docs | documentation | document |
| refactor | refactor | document → scaffold → implement → test |
| hotfix | hotfix | implement → test |
| integration | integration | scaffold → implement → test |
| evolve | knowledge-evolution | document → implement |

Full model definitions: `wiki/config/methodology.yaml`. Artifact details: `wiki/config/artifact-types.yaml`.

## Page Schema (Every Wiki Page)

YAML frontmatter required:
```yaml
title, type, domain, status, confidence, created, updated, sources, tags
```

Section order:
```
# Title
## Summary          ← 2-3 sentences min
## Key Insights     ← condensed
## Deep Analysis    ← full resolution
## Open Questions   ← optional
## Relationships    ← VERB: target format
```

Types: `concept, source-synthesis, comparison, reference, deep-dive, index, lesson, pattern, decision, principle, domain-overview, learning-path, evolution, operations-plan, milestone, epic, module, task, note`

Every type has a template in `wiki/config/templates/`. Scaffold: `python3 -m tools.pipeline scaffold <type> "<title>"`.

## Relationship Conventions

ALL_CAPS verbs. One per line. Comma-separated targets allowed. Use `[[filename|title]]` format for Obsidian resolution:

```
- BUILDS ON: [[model-methodology|Model — Methodology]]
- RELATES TO: [[model-claude-code|Model — Claude Code]]
- DERIVED FROM: [[src-openspec-spec-driven-development-framework|Synthesis: OpenSpec]]
```

Verbs: BUILDS ON, ENABLES, COMPARES TO, CONTRADICTS, USED BY, RELATES TO, FEEDS INTO, DERIVED FROM, SUPERSEDES, IMPLEMENTS, EXTENDS, CONTAINS, PART OF

## Quality Gates (Enforced by `pipeline post`)

- Complete frontmatter per `wiki/config/wiki-schema.yaml`
- Summary ≥30 words
- ≥1 relationship (unless first in new domain)
- Reachable from domain `_index.md`
- Source provenance (URL or file reference)
- No >70% concept overlap with existing pages
- Per-type content thresholds from `wiki/config/artifact-types.yaml`
- Evolved pages (lesson, pattern, decision, principle) require Obsidian callouts
- Every stage transition: previous stage's artifacts exist

Validation: `python3 -m tools.pipeline post` (runs all 6 steps). Detail: [TOOLS.md](TOOLS.md).

## When You Don't Know Something

1. Search the wiki FIRST: `python3 -m tools.view search "query"`
2. Check existing pages: `python3 -m tools.view refs "Page Title"`
3. Check the manifest: `wiki/manifest.json` for page metadata
4. Research online SECOND — only after checking what the wiki already knows

## Work Hierarchy

```
Milestone → Epic → Module → Task
```

Live in `wiki/backlog/`. Each tracks `readiness` (definition) AND `progress` (execution) independently. 99→100 on either dimension = human review required.

## Core Principles

1. **Infrastructure Over Instructions** — hooks achieve 100%; rules alone ~25%.
2. **Structured Context Governs Agent Behavior More Than Content** — tables beat prose 2-3x.
3. **Right Process for Right Context (Goldilocks)** — methodology depth adapts to phase × scale × trust.

## How to Use the Second Brain

This wiki IS the second brain — it's self-referential.

**Before starting ANY work:**
1. Check `wiki/spine/models/foundation/model-methodology.md` — understand which model applies
2. Check `wiki/spine/references/methodology-system-map.md` — find any component
3. Check the per-type standards in `wiki/spine/standards/` — know what GOOD looks like BEFORE writing

**Before producing ANY artifact:**
1. Identify the artifact class: DOCUMENT (constraining), ARTIFACT (by-product), DOCUMENTATION (explaining)?
2. Check `wiki/domains/cross-domain/methodology-artifacts/categories/methodology-artifact-taxonomy.md` — 78 types
3. Check the domain chain for your domain (TypeScript, Python/Wiki, Infrastructure, Knowledge)
4. Check `wiki/spine/standards/{type}-page-standards.md` for the quality bar

## Contribution Back

When you learn something the wiki doesn't know:
```bash
python3 -m tools.gateway contribute --type lesson --title "Title" --content "..."
```

Creates `wiki/lessons/00_inbox/` page — start of the maturity pipeline.

## Key Entry Points

- Full command reference: [TOOLS.md](TOOLS.md)
- Architecture + data flow: [ARCHITECTURE.md](ARCHITECTURE.md)
- Visual/page design: [DESIGN.md](DESIGN.md)
- Skills directory: [SKILLS.md](SKILLS.md)
- Identity + scope: [CONTEXT.md](CONTEXT.md)
- Models: `wiki/spine/references/model-registry.md`
- Standards: `wiki/spine/standards/`
- Gateway tools: `wiki/spine/references/gateway-tools-reference.md`
