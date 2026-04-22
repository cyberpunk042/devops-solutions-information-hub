---
title: "E009 M004 — Harness Contract Document (harness-neutral invariants)"
type: module
domain: backlog
status: draft
priority: P1
task_type: module
current_stage: design
readiness: 85
progress: 0
stages_completed: [document]
artifacts:
  - wiki/spine/standards/harness-contract.md
epic: "E009"
depends_on:
  - "E009-m002"
  - "E009-m003"
confidence: high
created: 2026-04-22
updated: 2026-04-22
sources:
  - id: e009-harness-neutrality-and-opencode-parity
    type: wiki
    file: wiki/backlog/epics/pre-milestone/E009-harness-neutrality-and-opencode-parity.md
tags: [module, p1, e009, harness, contract, standard, consumer-property-doctrine, doctrine]
---

# E009 M004 — Harness Contract Document

## Summary

Author `wiki/spine/standards/harness-contract.md` — the invariants any future harness (Claude Code, OpenCode, Gemini CLI, a custom wrapper) must provide for the wiki + pipeline + skills ecosystem to remain functional. This is the conceptual heart of E009: it turns "harness-neutral" from an aspiration into a measurable contract. Operator's directive: "every `.agents` or `.gemini` or `.claude` can be treated as equivalent to us. Every ecosystem needs one and to us it's the same thing."

## Tasks

| Task | Title | Readiness | Progress | Status |
|------|-------|-----------|----------|--------|
| T055 | Draft the Harness Contract outline (tools, hooks, skills, memory, MCP, cost) | 100% | 0% | draft |
| T056 | Fill each section with concrete requirements + current-harness mapping | 85% | 0% | draft |
| T057 | Side-by-side session log at wiki/log/2026-04-25-harness-neutrality-proof.md | 80% | 0% | draft |

## Dependencies

- **E009 M002** — MCP continuity results inform the MCP section.
- **E009 M003** — Skill portability findings inform the Skills section.
- Existing Consumer-Property Doctrine (if documented elsewhere in the wiki — cross-link).

## Done When

- [ ] `wiki/spine/standards/harness-contract.md` exists with full frontmatter (type: standard, domain: methodology, status: growing)
- [ ] Page length ≥300 lines (standards tier per operator's size minimums)
- [ ] Six sections present, each with "Requirement" + "Current harness mapping" + "Minimum test" subsections:
  1. Tool semantics (Read, Edit, Write, Glob, Grep equivalents)
  2. Hook event model (PreToolUse, PostToolUse, SessionStart, UserPromptSubmit adapters)
  3. Skill invocation convention (markdown+frontmatter, name-based lookup, args passthrough)
  4. Memory / persistence contract (ephemeral vs durable; where state lives; size limits)
  5. MCP integration (server list format, transport, auth, tool discovery)
  6. Cost tracking contract (per-request cost attribution, rollup interface, provider fields)
- [ ] Mapping table: Claude Code ↔ OpenCode ↔ (hypothetical Gemini CLI) for each section
- [ ] Compliance test suite outlined (how a new harness proves it meets the contract)
- [ ] Cross-linked from CLAUDE.md, AGENTS.md, and the milestone page
- [ ] Side-by-side session log at `wiki/log/2026-04-25-harness-neutrality-proof.md` with concrete evidence
- [ ] `python3 -m tools.pipeline post` passes
- [ ] All child tasks at status: done

## Procedure (reference)

### Step 1 — Outline

Write the six-section outline as a draft file. Each section uses the structure:

```markdown
## N. <Section Name>

### Requirement
Prose describing what the harness MUST provide, in harness-neutral terms.

### Current harness mapping
| Harness | Implementation | Gap |
|---------|---------------|-----|
| Claude Code | ... | ... |
| OpenCode    | ... | ... |
| Gemini CLI  | ... (hypothetical) | unknown |

### Minimum compliance test
How to verify a candidate harness meets this requirement.
```

### Step 2 — Draft each section

Draw on E009 M002 + M003 findings for sections 3, 4, 5. Sections 1, 2, 6 are largely drawn from Claude Code and OpenCode docs + common sense. Where OpenCode lacks a feature (e.g., fine-grained hook events), mark as a gap and name the adapter work needed.

### Step 3 — Mapping table + compliance test suite

At the end of the document, a single table summarizes harness → contract compliance. An explicit test list (12–20 items) that a new harness runs to prove compliance.

### Step 4 — Cross-link

```bash
$EDITOR CLAUDE.md       # add a link: "See [harness-contract.md](wiki/spine/standards/harness-contract.md)"
$EDITOR AGENTS.md       # same
$EDITOR wiki/backlog/milestones/post-anthropic-self-autonomous-stack.md
```

### Step 5 — Validate + log the side-by-side proof

```bash
python3 -m tools.pipeline post

python3 -m tools.pipeline scaffold note "2026-04-25-harness-neutrality-proof"
$EDITOR wiki/log/2026-04-25-harness-neutrality-proof.md
# Cite: OpenCode version, Claude Code version, tasks run, artifacts produced, diffs
python3 -m tools.pipeline post
```

## Rollback

```bash
rm wiki/spine/standards/harness-contract.md
rm wiki/log/2026-04-25-harness-neutrality-proof.md
# Revert CLAUDE.md / AGENTS.md edits
git checkout -- CLAUDE.md AGENTS.md
python3 -m tools.pipeline post
```

## Impediments

| Impediment | Type | Blocked Since | Escalated? | Resolution |
|-----------|------|---------------|-----------|------------|
| Contract can drift as harnesses evolve | doc | 2026-04-22 | no | Status: growing (living doc); quarterly review ritual |
| Some invariants may be aspirational (not yet met by any harness) | scope | 2026-04-22 | no | Mark as "target" vs "met"; track in open-questions |
| AGENTS.md and CLAUDE.md may need careful minimal edits | existing-work | 2026-04-22 | no | Small additive links, no restructure |

## Relationships

- PART OF: [[E009-harness-neutrality-and-opencode-parity|E009-harness-neutrality-and-opencode-parity]]
- DEPENDS ON: [[e009-m002-mcp-server-continuity|e009-m002-mcp-server-continuity]]
- DEPENDS ON: [[e009-m003-skill-portability|e009-m003-skill-portability]]

## Backlinks

[[E009-harness-neutrality-and-opencode-parity|E009-harness-neutrality-and-opencode-parity]]
[[e009-m002-mcp-server-continuity|e009-m002-mcp-server-continuity]]
[[e009-m003-skill-portability|e009-m003-skill-portability]]
