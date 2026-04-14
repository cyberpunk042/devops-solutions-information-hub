# SKILLS.md — Skills Ecosystem Directory

Audience: anyone using, creating, or dispatching skills in this project.
Source authority: [Model — Skills, Commands, and Hooks](wiki/spine/models/agent-config/model-skills-commands-hooks.md) ·
[Three-Layer Agent Context Architecture](wiki/patterns/01_drafts/three-layer-agent-context-architecture.md) ·
[Model — Markdown as IaC](wiki/spine/models/agent-config/model-markdown-as-iac.md)

---

## What Are Skills

Skills are on-demand, task-specific instruction sets that load into context **only when invoked**.
They are the primary extension mechanism for this wiki's agent — carrying rich workflow knowledge
that would be too expensive to load unconditionally.

A skill is a markdown file (or folder) that defines:
- When to use it (trigger description)
- What inputs it expects
- What steps to follow
- What outputs or side effects it produces

Skills are the correct default for extending agent capabilities. They cost nothing when unused
and provide full workflow depth when invoked.

---

## Three-Layer Context Architecture

This project uses a three-layer architecture for agent configuration:

| Layer | File | Scope | Loading | Max size |
|-------|------|-------|---------|----------|
| 1 — Universal | `AGENTS.md` | Cross-tool, always-on | Every session | <100 lines |
| 2 — Tool-specific | `CLAUDE.md` | Claude Code only, always-on | Every session | <200 lines (target: <100) |
| 3 — Conditional | Skills / commands | Per-task, on-demand | On invocation | <500 lines each |

**Layer 1 (AGENTS.md):** Project identity and core conventions — true regardless of which AI tool
is used. Absent from this project currently (identified gap — CLAUDE.md carries both L1 and L2).

**Layer 2 (CLAUDE.md):** This project's CLAUDE.md is the primary always-on context. It contains
methodology, stage gates, tooling commands, second brain usage, and quality gates. At ~400 lines,
it is above the ideal target — the three-layer model suggests splitting universal content into
AGENTS.md.

**Layer 3 (Skills):** The `.claude/commands/` directory contains this project's skill triggers.
These are thin slash-command files that invoke workflow steps. Rich workflow depth lives in the
referenced skill logic.

**Loading cost matters:** CLAUDE.md tokens load permanently for every message in the session.
Skill tokens load once on invocation and do not persist. This is why skills exist — context that
is needed for 10% of tasks should not occupy context for 100% of messages.

---

## Skill Catalog — This Project

Skills in `.claude/commands/`:

| Command | Trigger | What it does |
|---------|---------|-------------|
| `/ingest` | Source ingestion | Fetch URLs, process raw files into wiki source-synthesis pages, run post-chain, run crossref |
| `/continue` | Session resume | Run `pipeline chain continue`, check MEMORY.md, check service status, present state + options |
| `/evolve` | Knowledge evolution | Score evolution candidates, scaffold, generate, review maturity promotions |
| `/build-model` | Model work | Build, review, or evolve a wiki model using SFIF stages and LLM Wiki Standards |
| `/log` | Directive logging | Create a log entry in `wiki/log/` — directive, session summary, or completion note |
| `/status` | State check | Run `pipeline status`, `tools.stats`, `setup --services`, report everything |
| `/review` | Health review | Run `pipeline chain review` — validation errors, maturity promotions, stale pages, gaps |
| `/backlog` | Backlog management | Show epic/task summary, completion %, ask what to work on |
| `/gaps` | Gap analysis | Run `pipeline gaps` + `crossref`, prioritize, suggest next research targets |

**Format:** These are plain markdown files in `.claude/commands/`. Each is a numbered instruction
list — concise triggers, not full skill implementations. The Skill tool in Claude Code invokes
these when the user types the `/command-name`.

---

## Superpowers Skills (Active in This Project)

The superpowers skill pack provides meta-process capabilities — they determine **how** work is
done before implementation skills determine **what** is done.

| Skill | When to use |
|-------|------------|
| `superpowers:brainstorming` | **Before any creative or design decision.** Questions → approaches → design sections → approval on each. Required by operator directive when the path is unclear. |
| `superpowers:using-superpowers` | At the start of any complex multi-phase task — surfaces which other superpowers apply. |
| `superpowers:systematic-debugging` | When encountering unexpected failures or broken behavior. Hypothesis-driven, not trial-and-error. |
| `superpowers:writing-plans` | When work has multiple steps and dependencies — produce a plan before executing. |
| `superpowers:executing-plans` | When a plan exists — structured execution with checkpoints, not free-form. |
| `superpowers:dispatching-parallel-agents` | When 2+ independent tasks can run concurrently. |
| `superpowers:subagent-driven-development` | When executing a large plan with parallelizable components. |
| `superpowers:test-driven-development` | When implementing features that need verification. |
| `superpowers:writing-skills` | When creating new wiki content — quality and completeness standards. |
| `superpowers:verification-before-completion` | Before claiming a task is done — run the command, show the output. |
| `superpowers:finishing-a-development-branch` | When wrapping up a work session — commit, validate, summarize state. |

**Skill priority order:** Process skills first (brainstorming, debugging) — they determine HOW
to approach the work. Implementation skills second — they execute. "Let's build X" → invoke
`brainstorming` first, then implementation skills.

---

## When to Use Which Skill

```
Task is unclear or design decisions ahead?
  → superpowers:brainstorming (questions → approaches → approval)

Unexpected failure or broken behavior?
  → superpowers:systematic-debugging

Multi-step work with dependencies?
  → superpowers:writing-plans first, then superpowers:executing-plans

New source to ingest?
  → /ingest

Resuming a session?
  → /continue

Promoting lessons/patterns/decisions?
  → /evolve

Building or reviewing a wiki model?
  → /build-model

Checking what to work on next?
  → /status or /backlog

Finding knowledge gaps?
  → /gaps

Logging a directive verbatim?
  → /log

Weekly health check?
  → /review
```

---

## Skill Format (SKILL.md Standard)

Skills following the agentskills.io SKILL.md format work across Claude Code, Codex CLI,
OpenCode, Cursor, and any system-prompt-configurable agent.

A full skill is a folder:

```
skill-name/
  SKILL.md          — trigger description, prerequisites, instructions, exit criteria
  references/       — domain knowledge, schemas, API docs (loaded on demand)
  scripts/          — executable scripts the skill invokes
  examples/         — example inputs/outputs for few-shot guidance
```

### SKILL.md Frontmatter

```yaml
name: kebab-case-identifier
description: |
  When to use this skill. This field drives auto-invocation — strong,
  specific description = correct auto-selection. Weak description = missed triggers.
inputs:
  - name: url
    description: Source URL to ingest
    required: false
outputs:
  - type: wiki-page
    description: Source-synthesis page created in wiki/sources/
side_effects:
  - manifest.json updated
  - wiki/index.md updated
```

### Skill Body Structure

```markdown
## Prerequisites
- CLAUDE.md loaded (always true for project skills)
- pipeline tools available: `python3 -m tools.pipeline --help`

## Instructions
1. Step one — concrete action with exact command
2. Step two — decision point: if X do Y, else do Z
3. Step three — verification: run command, show output

## MUST
- Log directives verbatim before acting
- Run `pipeline post` after wiki changes

## MUST NOT
- Skip pipeline post after creating pages
- Claim done without showing command output

## Exit Criteria
- [ ] All pages pass `python3 -m tools.validate`
- [ ] `pipeline post` exits with 0 errors
- [ ] Relationships are bidirectional
```

---

## Skill Authoring Guidelines

**Description field is the most important field.** Auto-invocation depends on Claude matching
the user's request to the skill's description. Vague descriptions cause missed triggers.
Strong descriptions are specific: "Use when ingesting external URLs or pasted content into the
research wiki" beats "Source ingestion."

**Keep under 500 lines per skill file.** This is the Layer 3 ceiling — rich enough for full
workflow depth, small enough to not pollute baseline sessions.

**MUST/MUST NOT format for constraints.** Prose constraints are ignored. `MUST` and `MUST NOT`
sections with bullet points are executed.

**Include exit criteria.** A skill without exit criteria is a skill that never ends. Checklist
items give the agent a clear completion signal.

**Reference wiki pages for deeper context.** Skills are not reference documents — they are
workflows. Point to wiki pages for the underlying knowledge: "See
`[[model-methodology|Model — Methodology]]` for stage gate definitions."

**Test the description trigger.** After writing a skill, ask: "If a user says [natural language
trigger], will this description match?" If not, rewrite the description.

---

## Skills vs Commands vs Hooks

The full extension hierarchy has four levels:

| Level | Mechanism | Loading | Cost | Use for |
|-------|-----------|---------|------|---------|
| 0 | CLAUDE.md / AGENTS.md | Always (session start) | Permanent | Project identity, core methodology |
| 1 | Skills (SKILL.md) | On invocation | Temporary | Task-specific workflow depth |
| 2 | Hooks (settings.json) | At lifecycle boundaries | Near-zero | Structural enforcement, stage gates |
| 3 | Commands (`.claude/commands/`) | On `/invoke` | One-time injection | User-facing triggers that load skills |

Commands invoke skills, not replace them. `/ingest` is a thin trigger; the wiki-agent skill
carries the knowledge. Commands are role-appropriate workflow guides — the user types `/ingest`,
the command loads the ingestion workflow.

Hooks are not skills — they enforce what skills can only request. A hook blocking a forbidden
file write achieves 100% compliance. A skill instruction to avoid forbidden writes achieves ~60%.
See [Model — Skills, Commands, and Hooks](wiki/spine/models/agent-config/model-skills-commands-hooks.md)
for the full compliance data.

---

## Skill Distribution

The agentskills.io SKILL.md format is portable across agent runtimes:

| Runtime | How it loads skills |
|---------|-------------------|
| Claude Code | `.claude/commands/` + Skill tool invocation |
| Codex CLI | System prompt injection |
| OpenCode | Workflow file loading |
| Cursor | `.cursorrules` + skill injection |
| Any system-prompt-configurable agent | Direct context injection |

Format once, distribute across runtimes. The `name` and `description` fields are the portability
interface — keep them runtime-agnostic.

---

## Related Wiki Pages

| Page | What it covers |
|------|---------------|
| [Model — Skills, Commands, and Hooks](wiki/spine/models/agent-config/model-skills-commands-hooks.md) | Full four-level extension hierarchy with compliance data |
| [Three-Layer Agent Context Architecture](wiki/patterns/01_drafts/three-layer-agent-context-architecture.md) | AGENTS.md / CLAUDE.md / Skills separation pattern |
| [Model — Markdown as IaC](wiki/spine/models/agent-config/model-markdown-as-iac.md) | Markdown files as infrastructure — companion file ecosystem |
| [Model — Context Engineering](wiki/spine/models/) | Context window management, eager vs deferred loading |
| [Skills Architecture Is the Dominant LLM Extension Pattern](wiki/lessons/) | Why skills beat MCP for project-internal tooling |
