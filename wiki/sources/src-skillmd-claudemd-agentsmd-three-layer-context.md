---
title: "Synthesis — SKILL.md vs CLAUDE.md vs AGENTS.md — Three-Layer Agent Context Architecture"
type: source-synthesis
domain: ai-agents
status: synthesized
confidence: high
maturity: seed
created: 2026-04-14
updated: 2026-04-14
sources:
  - id: src-skillmd-claudemd-agentsmd-termdock
    type: article
    url: https://www.termdock.com/blog/skill-md-vs-claude-md-vs-agents-md
    title: "SKILL.md vs CLAUDE.md vs AGENTS.md — Compared (Termdock)"
tags:
  [
    agents-md,
    claude-md,
    skill-md,
    three-layer-architecture,
    context-engineering,
    cross-tool,
    agent-config,
    ai-agents,
    eth-zurich-research,
    linux-foundation,
    context-loading,
    source-synthesis,
  ]
---

# Synthesis — SKILL.md vs CLAUDE.md vs AGENTS.md — Three-Layer Agent Context Architecture

## Summary

This source compares the three primary agent configuration file types in the modern AI development ecosystem — CLAUDE.md (Claude Code session context), AGENTS.md (cross-tool universal context endorsed by 60,000+ repos and the Linux Foundation), and SKILL.md (on-demand task workflow files) — and proposes a three-layer architecture that combines all three to maximize context efficiency while maintaining cross-tool portability. A critical empirical finding from ETH Zurich (Feb 2026) challenges naive use: AI-generated context files reduce task success by ~3% compared to no file at all, while carefully hand-written files improve success by only 4%. The article establishes concrete size boundaries, names five common implementation errors, and provides a decision flowchart for placement decisions.

---

## Key Insights

- **Three files, three distinct scopes.** CLAUDE.md is Claude Code–specific and per-session (always loaded). AGENTS.md is cross-tool and per-session (always loaded by multiple runtimes). SKILL.md is per-task (loaded conditionally by description match). They are not interchangeable — each occupies a different layer in the context stack.

- **AGENTS.md has achieved de facto standard status.** 60,000+ open-source repositories have adopted AGENTS.md, now under Linux Foundation stewardship as part of the Agentic AI Foundation initiative. Compatible tools span the entire CLI agent ecosystem: Codex CLI, Copilot CLI, Gemini CLI, Cursor, and Claude Code (which reads BOTH CLAUDE.md and AGENTS.md simultaneously).

- **ETH Zurich (Feb 2026): AI-written context files hurt performance.** AI-generated CLAUDE.md / AGENTS.md files reduced task success rates by approximately 3% compared to no context file. Human-written files improved success by only ~4%. This narrow margin means context files must earn their presence — bloat actively costs performance.

- **The three-layer architecture provides the composable answer.** Layer 1: AGENTS.md under 100 lines for always-on cross-tool universal context. Layer 2: CLAUDE.md under 20 lines for minimal Claude-specific deltas. Layer 3: SKILL.md files up to 500 lines each for detailed on-demand task workflows. This architecture maximizes portability at Layer 1, minimizes session startup cost at Layer 2, and enables rich task-specific depth at Layer 3 without polluting the baseline session.

- **Five named implementation errors are common enough to warrant naming.** Oversized CLAUDE.md (300+ lines degrade performance), neglected skills (missing specialized workflows), content duplication across files, AI-generated context files (the ETH Zurich finding), and tool lock-in from CLAUDE.md exclusivity (forgoing AGENTS.md portability). These errors are structural, not incidental — they emerge from misunderstanding the three-file architecture.

- **SKILL.md is the only layer that can execute scripts.** AGENTS.md and CLAUDE.md are passive context injection. SKILL.md files can contain structured YAML frontmatter (name, description for trigger matching) and active script execution workflows. This is why on-demand loading matters: script-capable workflows should never be in the always-on layers.

- **Claude Code's dual-read behavior enables migration strategies.** Because Claude Code reads both CLAUDE.md and AGENTS.md, teams can maintain AGENTS.md as the canonical cross-tool source of truth and use CLAUDE.md as a thin delta layer containing only Claude-specific overrides. This allows gradual migration away from CLAUDE.md exclusivity without losing Claude-specific functionality.

---

## Deep Analysis

### The Three Files Compared

> [!info] **Comparison Matrix — All Three Config File Types**
>
> | Aspect | SKILL.md | CLAUDE.md | AGENTS.md |
> |--------|----------|-----------|-----------|
> | **Primary purpose** | Task capability | Project context (Claude) | Project context (all tools) |
> | **Scope** | Per-task, conditional | Per-session, always | Per-session, always |
> | **Location** | `.claude/skills/` | Project root | Project root |
> | **Read by** | Claude Code, Codex CLI, Copilot CLI, Gemini CLI | Claude Code only | All major AI CLI tools |
> | **Script execution** | Yes | No | No |
> | **Auto-trigger mechanism** | Yes (description match) | Always active | Always active |
> | **Recommended size** | <500 lines per skill | <20 lines (three-layer model) | <100 lines |
> | **Cross-tool portable** | Partially | No | Yes |

#### CLAUDE.md — Claude Code Session Identity

CLAUDE.md is the project brain injected into every Claude Code session. It defines project overview, architecture, conventions, hard constraints, and command references. In the three-layer model, CLAUDE.md shrinks drastically — from the common 200–400 line usage to under 20 lines — because everything that can be expressed cross-tool moves to AGENTS.md, and everything task-specific moves to skills.

The original single-file use case (one 300-line CLAUDE.md doing everything) fails for two reasons: it occupies full context for the entire session regardless of task relevance, and it produces tool lock-in because the content is Claude Code–specific. Every line in CLAUDE.md that could live in AGENTS.md is a portability tax paid at every session.

See [[model-claude-code|Model — Claude Code]] for the full Claude Code extension system and [[claude-md-structural-patterns|CLAUDE.md Structural Patterns for Agent Compliance]] for the structural formatting techniques that make smaller CLAUDE.md files more compliant per line.

#### AGENTS.md — The Cross-Tool Standard

AGENTS.md has emerged as the de facto cross-tool project context format. With 60,000+ repository adoptions and Linux Foundation stewardship (Agentic AI Foundation), it has crossed from convention into standard.

The strategic implication is clear: AGENTS.md should be the canonical single source of truth for project context. Teams using multiple AI tools (Claude Code + Copilot + Codex CLI) can maintain one well-written AGENTS.md rather than per-tool context files that diverge over time and require synchronization. Claude Code's willingness to read AGENTS.md removes the only friction point.

> [!tip] **Claude Code reads both files — use this**
>
> Claude Code reads CLAUDE.md AND AGENTS.md. This means:
> - Maintain AGENTS.md as canonical (cross-tool, always current)
> - CLAUDE.md becomes a thin override: "See AGENTS.md. Claude-specific: [2-3 items]"
> - When you drop a tool, your context doesn't need rewriting

The 100-line limit is non-negotiable. The ETH Zurich finding applies at full force to AGENTS.md: a 400-line AI-generated AGENTS.md is measurably worse than no file at all.

#### SKILL.md — On-Demand Task Depth

Skills are the escape valve for the context-efficiency constraint. Where AGENTS.md and CLAUDE.md must stay lean because they load unconditionally, SKILL.md files can be up to 500 lines each because they load only when their description matches the task being invoked.

The YAML frontmatter schema is standardized:

```yaml
name: database-migration
description: Run, create, and verify PostgreSQL database migrations using Drizzle ORM
```

The description field is the trigger surface — Claude Code matches incoming task descriptions against skill descriptions to determine which skills to inject. This makes the description field a first-class architectural concern, not documentation metadata.

The `agentskills.io` SKILL.md format provides cross-tool portability for skills as well: the same SKILL.md file works in Claude Code, Codex CLI, OpenCode, Cursor, and any system-prompt-configurable agent. Format choice compounds over time through distribution.

See [[model-skills-commands-hooks|Model — Skills, Commands, and Hooks]] for the complete four-level extension hierarchy (CLAUDE.md → Skills → Commands → Hooks) and how skills compose with hooks for compliance enforcement.

---

### The Three-Layer Architecture

> [!info] **Three-Layer Architecture — Placement Rules**
>
> | Layer | File | Size | Loading | Purpose |
> |-------|------|------|---------|---------|
> | **Layer 1** | AGENTS.md | <100 lines | Always, all tools | Universal cross-tool project context |
> | **Layer 2** | CLAUDE.md | <20 lines | Always, Claude only | Minimal Claude-specific delta |
> | **Layer 3** | SKILL.md (×N) | <500 lines each | On-demand per task | Detailed task workflows |

**Layer 1 (AGENTS.md)** carries the project essentials that every tool needs: architecture overview, tech stack, core conventions, hard constraints, key commands. Written by humans, reviewed for density, under 100 lines. This is the file that 60,000+ repos have standardized on. Treat it as the canonical source of truth.

**Layer 2 (CLAUDE.md)** contains only what AGENTS.md cannot: Claude Code–specific extensions, harness configuration references, hook behavior notes, MCP tool instructions. In the extreme, this could be 3 lines: `See AGENTS.md for project context. Claude-specific: [hooks are configured at X, skills are at Y, compaction behavior is Z].`

**Layer 3 (Skills)** is where depth lives. A database migration skill can be 500 lines covering every edge case because it only loads when someone invokes a database task. The skill loading cost model (zero until invoked) enables richness that would be catastrophic in Layer 1 or Layer 2. The 12x cost differential measured for Playwright CLI vs MCP in the research wiki ecosystem confirms this: deferred loading is not just elegant, it is measurably cheaper.

The architecture mirrors the research wiki's own structure: CLAUDE.md is the always-on identity file (this wiki's CLAUDE.md is ~270 lines at the operator's direction for a production second brain), skills are the domain-specific depth, and the gateway provides the cross-tool interface. The wiki demonstrates that the three-layer principle holds even at production scale, though size limits require judgment relative to system complexity.

---

### ETH Zurich Research Finding — Context Files Must Earn Presence

The ETH Zurich finding (February 2026) is the most operationally critical piece of this source:

> AI-generated context files reduced task success rates by approximately 3% compared to no context file at all. Human-written files improved success by only ~4%.

The implications:

1. **The margin is thin.** A 4% improvement means even good human-written files only modestly help. Bad files (AI-generated, bloated, redundant) actively harm.

2. **AI-generated files fail at a structural level.** When an LLM generates your CLAUDE.md, it tends to: over-specify (covering edge cases that rarely apply), use vague prose instead of enumerable constraints, and produce token-expensive descriptions that consume context without providing proportional guidance value.

3. **The baseline is brutal.** The zero-file baseline beats AI-generated files. This means: writing a CLAUDE.md is a commitment. If you cannot write it well, you are better off without one.

4. **Structural patterns matter more than content.** The [[claude-md-structural-patterns|CLAUDE.md Structural Patterns for Agent Compliance]] research confirms this from the compliance side: tables beat prose, ALLOWED/FORBIDDEN lists beat descriptions, numbered sequences beat paragraphs. The ETH Zurich finding adds the quantity dimension: even well-structured content degrades at high volume.

The three-layer architecture enforces the ETH Zurich lesson through structure: the hard size limits (100 / 20 / 500) make bloat physically difficult. A CLAUDE.md that hits 20 lines before covering everything forces the author to prioritize ruthlessly — which is exactly what produces the human-written quality that the ETH Zurich data rewards.

See [[model-context-engineering|Model — Context Engineering]] for the full structured context model and why context files behave as proto-programming inputs to AI agents.

---

### Common Implementation Errors

> [!warning] **Five Failure Modes — Structural, Not Incidental**
>
> | Error | Root Cause | Fix |
> |-------|-----------|-----|
> | **Oversized CLAUDE.md** (300+ lines) | Treating CLAUDE.md as a document, not a config file | Move cross-tool content to AGENTS.md, task content to skills |
> | **Neglected skills** | "One file to rule them all" mindset | Every recurring multi-step workflow → skill |
> | **Content duplication** | Files added over time without coordination | AGENTS.md as canonical; CLAUDE.md references it |
> | **AI-generated context files** | Convenience shortcut that backfires | Human-written, density-reviewed, size-bounded |
> | **Tool lock-in via CLAUDE.md exclusivity** | Not knowing AGENTS.md exists or that Claude reads it | Adopt AGENTS.md as Layer 1 canonical |

Error 5 (tool lock-in) is the most systemic. Teams that have invested heavily in a 400-line CLAUDE.md are locked to Claude Code. When team members use Copilot or Codex CLI, they get no project context. The three-layer architecture solves this at design time: start with AGENTS.md as canonical and CLAUDE.md becomes a thin override layer from day one.

Error 4 (AI-generated files) connects to the ETH Zurich finding directly. The temptation to ask Claude to generate its own CLAUDE.md is understandable — it knows the project. But the output will be over-comprehensive and prose-heavy, landing squarely in the −3% zone.

Error 1 (oversized CLAUDE.md) is the most common. The research wiki's own CLAUDE.md is intentionally large (operator-directed for a production second brain with 267+ pages of synthesized methodology), which is a justified exception at high system complexity. At project scale, 100 lines for AGENTS.md + 20 for CLAUDE.md is the defensible norm.

---

### Decision Flowchart — Where Does This Content Live?

> [!info] **Placement Decision Tree**
>
> ```
> Does it apply to every session, for every tool?
> ├─ YES → AGENTS.md (Layer 1)
> │         Keep under 100 lines total
> └─ NO → Does it only apply to Claude Code?
>          ├─ YES → CLAUDE.md (Layer 2)
>          │         Keep under 20 lines; reference AGENTS.md
>          └─ NO → Is it a specialized multi-step task workflow?
>                   ├─ YES → SKILL.md (Layer 3)
>                   │         Up to 500 lines; write frontmatter description carefully
>                   └─ NO → Does it need script execution?
>                            ├─ YES → SKILL.md with active workflow
>                            └─ NO → Reconsider whether context is needed at all
> ```

The "NO" exit at the bottom is the ETH Zurich lesson operationalized: if content doesn't clearly fit a layer, it probably shouldn't be in a context file.

---

### Cross-Tool Ecosystem Context

The cross-tool compatibility picture is now mature:

> [!info] **Tool Compatibility Matrix**
>
> | Tool | CLAUDE.md | AGENTS.md | SKILL.md |
> |------|-----------|-----------|----------|
> | **Claude Code** | Yes (primary) | Yes (also reads) | Yes (`.claude/skills/`) |
> | **Codex CLI** | No | Yes | Yes |
> | **GitHub Copilot CLI** | No | Yes | Yes |
> | **Gemini CLI** | No | Yes | Yes |
> | **Cursor** | No (.cursorrules) | Yes | Yes |
> | **OpenCode** | No | Yes | Yes |

The pattern is unambiguous: AGENTS.md is the only file that works across the entire tool landscape. CLAUDE.md is a Claude Code–specific extension. SKILL.md achieves broad portability via the agentskills.io format.

For teams committed to Claude Code only: the three-layer architecture still applies because it separates concerns structurally. AGENTS.md holds what is universally true about the project (and does not need to be Claude-specific). CLAUDE.md holds what is Claude-specific. Skills hold what is task-specific. The separation prevents the organic entropy that turns a 50-line CLAUDE.md into a 400-line catch-all over twelve months of project evolution.

See [[model-markdown-as-iac|Model — Markdown as IaC — Design.md and Agent Configuration]] for the companion file ecosystem view (CLAUDE.md, DESIGN.md, AGENTS.md, SOUL.md) and how markdown-as-IaC governs agent behavior across all four dimensions.

---

### Working Examples from the Source

**CLAUDE.md example structure (project-appropriate, not three-layer minimized):**
1. Project overview with scale indicators (e.g., "e-commerce API, 50k DAU")
2. Architecture stack (Node.js 22, Fastify 5, PostgreSQL 16, Drizzle ORM)
3. Code conventions (Result pattern, Zod schemas, repository organization)
4. Hard constraints (migration file restrictions, no default exports)
5. Command references

This example is a reasonable CLAUDE.md for a team not yet using the three-layer architecture. In the three-layer model, items 1–4 migrate to AGENTS.md (tool-agnostic), item 5 stays in CLAUDE.md (Claude-specific commands).

**Database migration SKILL.md frontmatter pattern:**
```yaml
name: database-migration
description: Run, create, and verify PostgreSQL database migrations using Drizzle ORM
```

The description is the critical field — it must be precise enough to trigger on relevant tasks and non-overlapping enough to not trigger on unrelated work.

---

## Open Questions

- Does the ETH Zurich research control for context file size, or is the −3% finding attributable to size rather than origin (AI vs human)? If size is the confound, the finding points more directly to the size limits than to the human-written requirement. (Requires: ETH Zurich paper methodology inspection — external.)
- ~~How does the three-layer architecture interact with multi-agent setups? Sub-agents in Claude Code do not inherit CLAUDE.md rules reliably (~33% compliance per Class 5 agent failure taxonomy). Does AGENTS.md fare better in sub-agent contexts?~~ **RESOLVED (2026-04-15):** **AGENTS.md is designed for cross-tool inheritance; CLAUDE.md is not.** This wiki's own CLAUDE.md explicitly documents the sub-agent dispatch problem: *"Sub-agents inherit AGENTS.md context but NOT CLAUDE.md"* — per CLAUDE.md's "Flow Per Mode" section. The architecture intentionally separates universal context (AGENTS.md, inheritance-friendly) from Claude-specific context (CLAUDE.md, session-local). AGENTS.md therefore DOES fare better in sub-agent contexts, but only to the extent it contains universal rules. See [[agent-failure-taxonomy-seven-classes-of-behavioral-failure|Agent Failure Taxonomy]] Class 5 for the ~33% baseline problem; the mitigation is to include critical rules in the sub-agent's spawn prompt explicitly rather than rely on file-inheritance.
- ~~At what project complexity threshold does the three-layer architecture require a Layer 2+ (a secondary CLAUDE.md section) rather than strict minimalism?~~ **RESOLVED (2026-04-15):** **File-size-driven, not complexity-driven.** This wiki's own CLAUDE.md explicitly targets `<100 lines` (currently ~95 lines) per the ETH Zurich finding that context files ≥300 lines reduce task success by ~3%. When content exceeds that sweet spot, the wiki splits into thematic files: AGENTS.md (universal), CONTEXT.md (identity), ARCHITECTURE.md, DESIGN.md, TOOLS.md, SKILLS.md — see [[root-documentation-map|Root Documentation Map]] for the full 8-doc layout. The threshold is **not project-complexity but CLAUDE.md size** — when the single-file budget is exhausted, split by concern rather than grow the file. The research wiki's "270+ lines" mentioned in the question is outdated; current CLAUDE.md is 95 lines because the wiki already adopted the split-by-concern approach that answers its own question.
- The Linux Foundation Agentic AI Foundation's AGENTS.md standard — what is its normative spec URL and version history? Is this a format spec or governance standard? (Requires: external research on the AAF organization and their standards repo.)

### Answered Open Questions

**Resolved by wiki cross-reference** (2026-04-15):

- **AGENTS.md vs CLAUDE.md in sub-agent contexts** — AGENTS.md inherits (designed for it); CLAUDE.md does not. Mitigation for sub-agent non-compliance is explicit spawn-prompt rules, not file inheritance.
- **Three-layer complexity threshold** — file-size-driven (CLAUDE.md `<100 lines` target per ETH Zurich `<300 lines` finding). Split by concern into thematic files when budget exhausted. This wiki did this — [[root-documentation-map|8 root docs]].

**Genuinely deferred** (require external research):

- ETH Zurich methodology confound (size vs origin)
- Linux Foundation AAF AGENTS.md standard version/URL

---

## Relationships

- BUILDS ON: [[model-claude-code|Model — Claude Code]] — extends the four-level extension system with cross-tool portability architecture
- BUILDS ON: [[model-skills-commands-hooks|Model — Skills, Commands, and Hooks]] — applies the context-loading cost model to the three-layer placement decision
- BUILDS ON: [[model-context-engineering|Model — Context Engineering]] — ETH Zurich finding is empirical evidence for structured context discipline
- RELATES TO: [[model-markdown-as-iac|Model — Markdown as IaC — Design.md and Agent Configuration]] — AGENTS.md as part of the companion file ecosystem (CLAUDE.md, DESIGN.md, AGENTS.md, SOUL.md)
- VALIDATES: [[claude-md-structural-patterns|CLAUDE.md Structural Patterns for Agent Compliance]] — the structural pattern research gains size-limit support from the ETH Zurich finding

## Backlinks

[[model-claude-code|Model — Claude Code]]
[[model-skills-commands-hooks|Model — Skills, Commands, and Hooks]]
[[model-context-engineering|Model — Context Engineering]]
[[model-markdown-as-iac|Model — Markdown as IaC — Design.md and Agent Configuration]]
[[claude-md-structural-patterns|CLAUDE.md Structural Patterns for Agent Compliance]]
