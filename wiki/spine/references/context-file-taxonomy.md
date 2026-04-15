---
title: Context File Taxonomy — The 8 Dimensions of Agent Context
aliases:
  - "Context File Taxonomy — The 8 Dimensions of Agent Context"
  - "Context File Taxonomy"
type: reference
domain: cross-domain
layer: spine
status: synthesized
confidence: high
maturity: growing
created: 2026-04-14
updated: 2026-04-14
sources:
  - id: three-layer-pattern
    type: wiki
    file: wiki/patterns/01_drafts/three-layer-agent-context-architecture.md
  - id: three-layer-synthesis
    type: wiki
    file: wiki/sources/src-skillmd-claudemd-agentsmd-three-layer-context.md
  - id: openarms-v10
    type: wiki
    file: wiki/sources/ecosystem-projects/src-openarms-v10-enforcement.md
    description: Source of the original "five cognitive contexts" framing
  - id: openfleet
    type: wiki
    file: wiki/sources/ecosystem-projects/src-openfleet-fleet-architecture.md
    description: Source of the workspace-expansion pattern (tasks/heartbeat/feed folders)
tags: [reference, context, taxonomy, agents, configuration, cognitive-contexts, agent-config, multi-dimensional, flexibility]
---

# Context File Taxonomy — The 8 Dimensions of Agent Context

> [!tip] Quick Orient
>
> This page answers: "I have a context file — what IS it?" and "My agent sees 20 files at once — how do they compose?"
> Looking for WHICH files exist? → [[root-documentation-map|Root Documentation Map]]
> Looking for the three-layer PATTERN? → [[three-layer-agent-context-architecture|Three-Layer Agent Context Architecture]]

## Summary

The complexity of agent context is NOT captured by a fixed number of "cognitive contexts." OpenArms identified 5 reader types sharing one CLAUDE.md. BMAD has layers of personas and workflows. A provisioned fleet agent sees dozens of files from 4+ origins simultaneously. The problem with framing context as a count (5, 8, 12) is that it flattens independent variation into a list — what matters is that every context file varies along 8 INDEPENDENT dimensions: how it loads, who controls it, what scope it applies at, what responsibility it owns, who reads it, how it aggregates with others, whether deeper content backs it, and how it structurally expands. This page formalizes those 8 dimensions as a complete taxonomy, catalogs every context source in the research wiki ecosystem, shows how files compose per agent type, and gives worked examples for 5 agent archetypes from solo operator sessions to provisioned fleet agents.

## Key Insights

> [!info] The 8 Key Takeaways
>
> - **Not a fixed count — 8 independent dimensions.** "Five cognitive contexts" (OpenArms) describes audience variation (dimension 5 only). The full picture requires all 8 coordinates. A file can be auto-injected + operator-origin + project-scope + rules-responsibility + Claude-Code-audience + authoritative + no-wiki-depth + flat-expansion — that is one specific point in an 8-dimensional space, not just "one context."
> - **"Root doc + companion folder" is a first-class expansion pattern.** SKILLS.md + `.claude/skills/*.md` is a canonical instance. OpenFleet's SOUL.md + `tasks/` + `heartbeat/` + `feed/` is another. The root doc provides orientation and convention; the companion folder allows accumulation and depth. You can have either without the other, and the pattern supports runtime-generated trees as the companion.
> - **Different agent types see different subsets at different scopes.** A solo operator session auto-loads CLAUDE.md + AGENTS.md. A provisioned fleet agent auto-loads its workspace SOUL.md + workspace AGENTS.md. A sub-agent dispatched from Claude inherits nothing reliably — it sees only its spawn prompt. Scope (project vs. workspace vs. task) determines which files are even visible, not just which are loaded.
> - **Loading order matters — auto-injected before directed before facultative before JIT.** Files loaded first establish identity and rules. Later-loaded files fill in specifics. Override precedence (which wins when two files disagree) is orthogonal to loading order. You can load a low-precedence file early and a high-precedence file late — the late file still wins on conflict.
> - **Flexibility comes from conventions, not rigidity.** The companion folder pattern is not enforced by any tool — it works because every contributor knows the convention. The YAML `description` field in SKILL.md files is the trigger surface for JIT loading — no special API, just convention. Good taxonomy captures conventions explicitly so they can be taught, enforced, and extended.
> - **The wiki itself is just another context source — JIT, via MCP/gateway/search.** The 267+ pages in `wiki/` are not auto-injected. They load when an agent makes a gateway query, uses an MCP tool, or runs a search. This means wiki depth is free at session start (no context cost) but requires a deliberate load action. The root docs provide the condensed form; the wiki provides the authoritative deep form behind it.
> - **Workspace scope is real for provisioned agents.** In OpenFleet, each agent operates in a git worktree that IS the workspace. The worktree has its own SOUL.md, its own task dispatch folder, its own heartbeat log. The repo-level files are still visible but exist "from a distance" — workspace scope takes precedence. This scope transition is architectural, not just a naming convention.

## Deep Analysis

### The 8 Dimensions

Every context file has exactly one value per dimension. Together, 8 values define what the file IS and how it behaves in a composed context environment.

> [!abstract] The 8 Dimensions — Complete Reference
>
> | # | Dimension | Values | Why It Matters |
> |---|-----------|--------|---------------|
> | 1 | **Loading mode** | Auto-injected / Directed / Facultative / Just-in-time (JIT) | Determines WHEN the file affects behavior |
> | 2 | **Origin / Authority** | Operator / Repository / Workspace / Agent-specific / External import / Runtime | Determines WHO the content is accountable to |
> | 3 | **Scope / Perspective** | Global / Project / Workspace / Session / Task | Determines WHERE the content applies |
> | 4 | **Responsibility** | Identity / Rules / Methodology / Tools / Knowledge / State / Navigation | Determines WHAT concern the file owns |
> | 5 | **Audience** | Operator / Any-AI / Claude-Code / Sub-agent / Provisioned-agent / MCP-client | Determines WHO reads it |
> | 6 | **Aggregation role** | Authoritative / Synthesis / Index / Override / Pointer | Determines HOW the content relates to others |
> | 7 | **Depth relationship** | Condensed / Authoritative / Index / Orphan (to wiki knowledge) | Determines whether deeper content exists behind it |
> | 8 | **Expansion pattern** | Flat file / File + companion folder / Folder (README-indexed) / Runtime-generated tree | Determines STRUCTURAL expansion |

**Dimension 1 — Loading Mode.** The most operationally critical dimension. *Auto-injected* files load at session start without any explicit instruction — CLAUDE.md, AGENTS.md, .mcp.json. *Directed* files load because the agent is explicitly told to read them — "read raw/notes/ for history." *Facultative* files load when the agent judges them relevant — TOOLS.md when a tool question arises. *Just-in-time (JIT)* files load via active tool calls — wiki pages via gateway query, skills via trigger match, task files via dispatch. The implication: auto-injected files ALWAYS consume context window; JIT files cost nothing until needed.

**Dimension 2 — Origin / Authority.** *Operator* origin means the content was written by the human with authority over this project — raw/notes/ entries, explicit session directives. This is the highest-precedence origin. *Repository* origin means the content lives in the repo and is controlled by the team — AGENTS.md, CLAUDE.md, skills. *Workspace* origin is repo content that is specific to one agent's worktree scope (OpenFleet SOUL.md). *Agent-specific* origin is content generated or owned by a specific agent persona. *External import* is content pulled in from another project's wiki via `--wiki-root`. *Runtime* is content generated during execution — task dispatch files, heartbeat logs.

**Dimension 3 — Scope.** *Global* scope means the content applies everywhere, regardless of project or context — operator mental models, principles, hard rules. *Project* scope means the content applies to this repo. *Workspace* scope means it applies to one agent's working environment within the project. *Session* scope means it is specific to the current conversation. *Task* scope means it applies to a single dispatched unit of work.

**Dimension 4 — Responsibility.** Files with mixed responsibility are a design smell — they are harder to update, harder to discover, and harder to reason about when they conflict. The root doc refactor on 2026-04-14 was precisely a separation-of-concerns exercise: one 315-line CLAUDE.md mixed identity + rules + methodology + tools + knowledge → split into 8 single-responsibility files. The responsibility dimension is the diagnostic axis for this problem.

**Dimension 5 — Audience.** Not all files are for AI agents. TOOLS.md is primarily for human operators running CLI commands. DESIGN.md is for humans and agents creating wiki pages. AGENTS.md is intentionally written for "any AI" (60k+ repos use this cross-tool standard). CLAUDE.md is Claude-Code-specific. OpenFleet's SOUL.md is written exclusively for its provisioned agent. The audience dimension governs what assumptions the author can make about the reader.

**Dimension 6 — Aggregation Role.** *Authoritative* means this file IS the source of truth for its content. *Synthesis* means this file condenses content from multiple sources (most wiki source-synthesis pages). *Index* means this file catalogues other content without being the source of truth for any item. *Override* means this file explicitly supersedes or extends another file (CLAUDE.md overrides AGENTS.md on Claude-specific behavior). *Pointer* means this file mainly says "go here" — a thin redirect.

**Dimension 7 — Depth Relationship.** Every file stands in some relationship to the wiki knowledge base. *Condensed* means the file is a summary of deeper wiki pages — the reader can get more from the wiki. *Authoritative* means the file IS the deep content — no separate wiki page expands it further. *Index* means the file is a navigation entry to wiki pages. *Orphan* means no wiki page corresponds to this file — it stands alone (historical logs, runtime-generated files).

**Dimension 8 — Expansion Pattern.** Structural, not semantic. *Flat file* — one file, no companion. *File + companion folder* — a root file plus a folder containing expansion entries. *Folder (README-indexed)* — a directory whose README orients the reader to all sub-contents. *Runtime-generated tree* — a folder whose contents accumulate at runtime with entries created by agents or harnesses. *Manifest with imports* — a root file that is itself a list of `@`-include statements aggregating sibling files at load time (observed in Cline's CLAUDE.md: `@.clinerules/general.md` + others).

---

### The "Root Doc + Companion Folder" Pattern — Dimension 8 Detail

The expansion pattern dimension reveals a recurring structural idiom that appears in multiple independent contexts. It is worth naming explicitly because it encodes a real design principle: **orientation is always bounded; expansion is potentially unbounded**.

> [!info] Four Expansion Patterns — Concrete Examples
>
> | Pattern | Structure | Example |
> |---------|-----------|---------|
> | **Flat file** | Single file, no companion | `README.md`, `CONTEXT.md`, `ARCHITECTURE.md` |
> | **File + companion folder** | Root file + sibling folder containing depth entries | `SKILLS.md` (root) + `.claude/skills/*.md` (individual skills) |
> | **Folder (README-indexed)** | Directory with `README.md` explaining contents | `wiki/config/sdlc-profiles/` + `wiki/config/README.md` |
> | **Runtime-generated tree** | Static root doc + companion folders accumulating at runtime | OpenFleet `SOUL.md` (static) + `tasks/` (per-dispatch) + `heartbeat/` (per-tick) + `feed/` (streaming) |
> | **Manifest with imports** | Root file is a list of `@`-include statements; real content lives in sibling files resolved at load time | Cline's `CLAUDE.md`: `@.clinerules/general.md` + `@.clinerules/network.md` + `@.clinerules/cli.md` (root is 3 lines; content is in the imported files). See [[src-cline-agentic-coding-ide-extension\|Synthesis — Cline]] |

**Why the pattern works:**

The root file provides *orientation, summary, conventions* — bounded, controlled, always current. Reading it tells you what the system IS and how to navigate it. It functions like a map.

The companion folder provides *accumulation, drilling-down, extension* — unbounded, growing, detailed. Each entry in the folder is a self-contained unit that expands one aspect of the root. It functions like a filing cabinet with labeled drawers.

Three key properties:

1. You can have the root file without the companion folder when the system is small enough. SKILLS.md works fine before there are any skills — it just catalogs conventions for future use.
2. You can have the companion folder even if the root file stays minimal. As the folder grows, the root file does not need to grow with it — it just says "see companion folder."
3. Runtime-generated companion folders (OpenFleet) extend this to live systems. The SOUL.md is static configuration. The `tasks/`, `heartbeat/`, and `feed/` folders accumulate over time. The root doc never ages; the companion grows continuously.

This pattern is distinct from a *folder with README* because the root file lives at a higher level (often the repo root or workspace root) and serves as a first-class entry point, not just a folder index.

---

### Complete Catalog — All Context Sources in the Ecosystem

Organized by origin tier. Each entry is classified across all 8 dimensions. Workspace-scope entries (OpenFleet) are marked as aspirational for this wiki but real in OpenFleet.

#### Repo-Level Files — The 8 Root Docs

> [!abstract] Root Doc 8-Dimension Catalog
>
> | Source | Load | Origin | Scope | Responsibility | Audience | Aggregation | Depth | Expansion |
> |--------|------|--------|-------|---------------|----------|-------------|-------|-----------|
> | `README.md` | Facultative | Repo | Project | Navigation | First-visitor (human/AI) | Index | Orphan | Flat |
> | `AGENTS.md` | Auto-injected | Repo | Project | Rules + methodology | Any-AI | Authoritative | Condensed | Flat |
> | `CLAUDE.md` | Auto-injected | Repo | Project | Claude-specific overrides | Claude-Code | Override | Authoritative (no wiki mirror) | Flat |
> | `CONTEXT.md` | Facultative | Repo | Project | Identity + state | Any human/AI | Authoritative | Condensed | Flat |
> | `ARCHITECTURE.md` | Facultative | Repo | Project | Data flow + topology | Anyone modifying structure | Authoritative | Condensed | Flat |
> | `DESIGN.md` | Facultative | Repo | Project | Visual design conventions | Page creators | Authoritative | Condensed | Flat |
> | `TOOLS.md` | Facultative | Repo | Project | CLI reference | Operators | Index + Reference | Condensed (wiki has gateway-tools-reference + model-automation-pipelines) | Flat |
> | `SKILLS.md` | Facultative | Repo | Project | Skills catalog + conventions | Skill users/authors | Index + Authoritative | Condensed | **File + companion folder** (`.claude/skills/`) |

**Notes on specific entries:**

`AGENTS.md` is auto-injected by Claude Code and honored by every tool implementing the Linux Foundation Agentic AI Foundation standard (60k+ repos). The "condensed" depth relationship means AGENTS.md summarizes rules that are defined in full in wiki methodology pages — a reader who wants to understand WHY can follow the condensed rule into the wiki.

`CLAUDE.md` has "Authoritative / no wiki mirror" because its content is Claude-Code-specific operational configuration. There is no separate wiki page that explains it in more depth — it IS the depth for its narrow domain.

`SKILLS.md` has the File + companion folder expansion because it catalogs skills that each live as individual files in `.claude/skills/`. The root file is the index and convention guide; the companion folder is the implementation.

#### Hidden Config and Runtime Files

> [!abstract] Config + Runtime 8-Dimension Catalog
>
> | Source | Load | Origin | Scope | Responsibility | Audience | Aggregation | Depth | Expansion |
> |--------|------|--------|-------|---------------|----------|-------------|-------|-----------|
> | `.mcp.json` | Auto-loaded (by Claude Code) | Repo | Project | MCP server registry | Claude-Code runtime | Authoritative | Orphan | Flat |
> | `.claude/settings.json` | Auto-loaded | Repo | Project | Claude permissions + hooks | Claude-Code | Authoritative | Orphan | Flat |
> | `.claude/settings.local.json` | Auto-loaded | Repo (local-only) | Project | Local operator overrides | Claude-Code | Override | Orphan | Flat |
> | `wiki/config/*.yaml` | Directed (by tools, not agent directly) | Repo | Project | Schema + methodology definitions | Tools (agent accesses via gateway) | Authoritative | Authoritative (wiki/config/README.md explains) | **Folder (README-indexed)** |

`wiki/config/` is an interesting case: the agent does not typically read these YAML files directly, but they are the source of truth for what the gateway and pipeline tools enforce. The agent accesses this content through gateway commands (`python3 -m tools.gateway config methodology.models`) which render config sections as readable markdown. The config folder is the machine-executable layer; the wiki pages are the human-explanation layer.

#### Skills — Conditional Layer

> [!abstract] Skills 8-Dimension Catalog
>
> | Source | Load | Origin | Scope | Responsibility | Audience | Aggregation | Depth | Expansion |
> |--------|------|--------|-------|---------------|----------|-------------|-------|-----------|
> | `.claude/skills/<name>/SKILL.md` (project skills) | JIT (YAML `description` trigger match) | Repo | Task | Workflow-specific rules + steps | Claude-Code | Authoritative for its task | Orphan or Condensed | Flat |
> | `.claude/skills/<name>/` (superpowers) | JIT (explicit invocation) | External (agentskills.io) | Task | General capability patterns | Claude-Code | Authoritative | Orphan | Flat |

Skills are the purest example of JIT loading. The YAML frontmatter `description` field is the only trigger surface — Claude Code matches the incoming task against descriptions and injects matching skills. No API call, no explicit instruction needed. This means skill descriptions must be precise enough to match the right tasks but not so broad they trigger unnecessarily (reducing token efficiency).

#### Operator-Level Files

> [!abstract] Operator Files 8-Dimension Catalog
>
> | Source | Load | Origin | Scope | Responsibility | Audience | Aggregation | Depth | Expansion |
> |--------|------|--------|-------|---------------|----------|-------------|-------|-----------|
> | `raw/notes/*.md` (directive logs) | Directed | Operator | Global | Identity / rules / directives | Any-agent (historical) | Authoritative (highest) | Orphan | **Folder (dated entries accumulate)** |
> | `raw/articles/*.md` (source dumps) | Directed | External (saved by operator) | Project | Raw source material | Agent (ingestion) | Orphan (pre-synthesis) | Orphan | Folder |
> | `raw/transcripts/*.txt` | Directed | External (saved by operator) | Project | Raw transcript material | Agent (ingestion) | Orphan (pre-synthesis) | Orphan | Folder |

`raw/notes/` entries are the highest-precedence origin in the ecosystem. When the operator writes a directive there, it is sacrosanct. The folder expands indefinitely with dated entries — there is no cleanup, no archiving. The historical record persists permanently for provenance.

#### Wiki Knowledge — JIT Deep Content

> [!abstract] Wiki Knowledge 8-Dimension Catalog
>
> | Source | Load | Origin | Scope | Responsibility | Audience | Aggregation | Depth | Expansion |
> |--------|------|--------|-------|---------------|----------|-------------|-------|-----------|
> | `wiki/spine/**/*.md` | JIT (gateway query / MCP / search) | Repo | Project | Knowledge (methodology, models, principles) | Anyone | Authoritative | Authoritative | **Folder (README-indexed)** |
> | `wiki/domains/**/*.md` | JIT (gateway query / MCP / search) | Repo | Project | Domain-specific knowledge | Anyone | Authoritative | Authoritative | Folder (maturity-based sub-structure) |
> | `wiki/sources/**/*.md` | JIT (gateway query / MCP / search) | Repo | Project | Source syntheses (L1 knowledge) | Anyone | Synthesis | Condensed (of raw source) | Folder |
> | `wiki/patterns/**/*.md` | JIT | Repo | Project | Patterns (≥2 instances, L5 knowledge) | Anyone | Synthesis | Authoritative | Folder (maturity stages) |
> | `wiki/lessons/**/*.md` | JIT | Repo | Project | Lessons (≥3 evidence items, L4 knowledge) | Anyone | Synthesis | Authoritative | Folder (maturity stages) |
> | `wiki/decisions/**/*.md` | JIT | Repo | Project | Decisions (alternatives + rationale, L6) | Anyone | Synthesis | Authoritative | Folder (maturity stages) |

The wiki's folder structure encodes maturity: `00_inbox → 01_drafts → 02_synthesized → 03_validated → 04_principles`. This is itself a dimension-8 expansion pattern — the folder accumulates entries at all maturity levels simultaneously, and the subfolder structure reflects confidence, not just topic.

#### Wiki Operational Files — Temporal State

> [!abstract] Wiki Operational 8-Dimension Catalog
>
> | Source | Load | Origin | Scope | Responsibility | Audience | Aggregation | Depth | Expansion |
> |--------|------|--------|-------|---------------|----------|-------------|-------|-----------|
> | `wiki/log/*.md` (session logs) | JIT (directed for history) | Session (written), Repo (read) | Session / Historical | State + history | Future agents | Authoritative for past events | Orphan | Folder (dated entries) |
> | `wiki/backlog/*.md` | JIT | Repo | Project | Work items + queue | Agent + operator | Index + Authoritative | Orphan | Folder |

Session logs are interesting: at write time, they are session-scoped (what happened this session). At read time, they are historical records accessible to future agents. This time-shifted scope makes them unique — the write-time origin and read-time use serve different purposes.

#### Workspace-Level Files — Provisioned Agents (OpenFleet)

> [!warning] Aspirational for This Wiki — Real in OpenFleet
>
> This section describes the workspace-scope pattern as implemented in OpenFleet. It is not currently implemented in this wiki. Include it to understand the full taxonomy space and the architectural intent.

> [!abstract] Workspace Files 8-Dimension Catalog (OpenFleet)
>
> | Source | Load | Origin | Scope | Responsibility | Audience | Aggregation | Depth | Expansion |
> |--------|------|--------|-------|---------------|----------|-------------|-------|-----------|
> | `workspace/SOUL.md` | Auto-injected (in worktree) | Agent-specific | Workspace | Identity + rules (per-agent) | Provisioned-agent | Authoritative for agent | Condensed (extends repo-level) | **File + companion folder** (tasks/, heartbeat/, feed/) |
> | `workspace/AGENTS.md` | Auto-injected (in worktree) | Workspace | Workspace | Cross-agent rules at workspace scope | Provisioned-agent | Authoritative | Condensed | Flat |
> | `workspace/tasks/*.md` | JIT (dispatched per task) | Runtime | Task | Per-task instructions + state | Provisioned-agent | Authoritative for one task | Orphan | **Runtime-generated tree** |
> | `workspace/heartbeat/*` | JIT (each tick) | Runtime | Session | Current tick state + signals | Provisioned-agent | Authoritative for current state | Orphan | Runtime-generated tree |
> | `workspace/feed/*` | JIT (streamed events) | Runtime | Session | Incoming events + fleet signals | Provisioned-agent | Authoritative for incoming | Orphan | Runtime-generated tree |
> | `workspace/tier-context.md` | JIT (earned by approval rate) | Runtime | Workspace | Depth of context awarded per trust tier | Provisioned-agent | Authoritative | Orphan | Flat |

The workspace-level pattern is the most sophisticated application of the expansion dimension. SOUL.md is the static root doc — written by the project, rarely changing, encoding the agent's persona, authority, and standing orders. Its companion folders (`tasks/`, `heartbeat/`, `feed/`) are *all runtime-generated* — they accumulate during live operation. The fleet harness dispatches task files, logs heartbeat ticks, and streams incoming events. SOUL.md orients; the companion folders are the live nervous system.

The `tier-context.md` file is unique: it is the only example of a context file that changes based on an agent's measured behavior (approval rate). As an agent earns trust through correctly executed approvals, it unlocks progressively deeper context. This is dimension-2 (origin: runtime earned through agent behavior) meeting dimension-4 (responsibility: depth-of-context access control).

#### External Imports — Cross-Project

> [!abstract] External Import 8-Dimension Catalog
>
> | Source | Load | Origin | Scope | Responsibility | Audience | Aggregation | Depth | Expansion |
> |--------|------|--------|-------|---------------|----------|-------------|-------|-----------|
> | Sister project's `AGENTS.md` (via `--wiki-root`) | Directed | External | Global | Cross-project rules | Any-AI via gateway | Authoritative for that project | varies | varies |
> | Sister project wiki pages (via MCP gateway) | JIT | External | Global | Cross-project knowledge | Any agent with MCP access | Synthesis | Authoritative | varies |

External imports are the cross-project integration layer. The gateway's `--wiki-root` flag allows any gateway query to target another project's wiki instead of this one. This means a sister project agent can query our methodology wiki directly, and we can query an openfleet or aicp wiki if it existed. The authority chain for external imports is: the external project's local config takes precedence over their AGENTS.md read by us — we are reading their docs as reference, not adopting their overrides.

---

### Composition — Override Precedence and Loading Order

The 8 dimensions describe individual files. Composition describes what happens when an agent sees multiple files simultaneously and they contradict each other.

#### Override Precedence (Highest Wins on Conflict)

> [!warning] Override Chain — When Two Files Disagree
>
> | Priority | Source | Why |
> |----------|--------|-----|
> | 1 (highest) | Operator directives (raw/notes/ + explicit session instructions) | Sacrosanct — human authority, cannot be overridden by any file |
> | 2 | `CLAUDE.md` / `AGENTS.md` (project-level) | Always-loaded project contract |
> | 3 | Workspace-level files (SOUL.md, workspace AGENTS.md) | Agent-specific scope narrows project rules |
> | 4 | Repo-level thematic docs (CONTEXT, ARCHITECTURE, DESIGN, TOOLS, SKILLS) | On-demand depth, consistent with root contract |
> | 5 | Skills (`.claude/skills/*.md`) | Task-scoped, but bounded by project contract |
> | 6 | Wiki configs (`wiki/config/*.yaml`) | Machine-readable, tools enforce them |
> | 7 | Wiki knowledge (`wiki/spine/`, `wiki/domains/`) | JIT-loaded reference, not operating instructions |
> | 8 (lowest) | External imports (sister project configs) | Read as reference, not adopted as authority |

The key insight: override precedence says which file WINS on conflict. Loading order says which file is read FIRST. These are independent. An operator directive written in `raw/notes/` is typically read mid-session (directed), but it has priority-1 authority — it overrides everything loaded at session start. The agent must apply it retroactively to everything already loaded.

#### Loading Order (Earliest First)

> [!info] Temporal Loading Sequence
>
> | Phase | What Loads | Trigger |
> |-------|-----------|---------|
> | 1 — Session start | `CLAUDE.md` + `AGENTS.md` + `.mcp.json` + `.claude/settings*.json` | Auto-injected by Claude Code |
> | 2 — Workspace entry | Workspace `SOUL.md` + workspace `AGENTS.md` (if applicable) | Auto-injected when working in a worktree |
> | 3 — Directed | `raw/notes/` history, specific files the operator points to | Explicit instruction |
> | 4 — Facultative | `TOOLS.md`, `DESIGN.md`, `CONTEXT.md`, `ARCHITECTURE.md`, `SKILLS.md` | Agent judges them relevant |
> | 5 — Just-in-time | Wiki pages (gateway/MCP/search), skills (trigger match), task files (dispatch) | Active tool call or trigger match |

**Why loading order matters:** The files loaded in Phase 1 establish the agent's operating identity for the session. If AGENTS.md says "you are a second brain agent with 7 hard rules," the agent enters every subsequent action with that framing already active. Later-loaded files (wiki knowledge, skills) operate within the identity already established. If loading order were reversed — wiki pages first, then AGENTS.md — the agent's rules would be established after some work had already begun. The sequence is intentional.

**Why override precedence is separate:** Two rules can conflict even when one was loaded before the other. A skill loaded in Phase 5 says "do X." AGENTS.md loaded in Phase 1 says "never do X." Override precedence resolves this: AGENTS.md (priority 2) wins over a skill (priority 5) regardless of load order. Without a precedence model, the last-loaded rule would silently win — a dangerous default.

---

### Worked Examples — Context Composition Per Agent Type

The following examples show how the 8 dimensions compose for 5 distinct agent archetypes. Each example shows: which files load, in what order, at what scope, and how the override chain resolves when rules conflict.

#### Example 1: Solo Operator Session (This Wiki, Today)

**Agent type:** Claude Code in a solo human-AI conversation, no harness.

**Files that load:**

| Phase | File | Mode | Precedence |
|-------|------|------|------------|
| Auto | `CLAUDE.md` | Auto-injected | 2 |
| Auto | `AGENTS.md` | Auto-injected | 2 |
| Auto | `.mcp.json` | Auto-loaded (Claude Code) | — (registry, not rules) |
| Auto | `.claude/settings.json` | Auto-loaded | — (permissions, not rules) |
| Facultative | `TOOLS.md` | When tool question arises | 4 |
| Facultative | `DESIGN.md` | When creating wiki pages | 4 |
| Facultative | `CONTEXT.md` | When identity/state question arises | 4 |
| Directed | `raw/notes/` | When operator says "log this" or "check history" | 1 |
| JIT | Gateway queries, wiki pages | Via MCP tool calls | 7 |
| JIT | Skill (e.g., `wiki-agent`, `evolve`) | Via trigger match or invocation | 5 |

**Override chain when conflict:** Operator current-session directive → CLAUDE.md/AGENTS.md → thematic root docs → skills → wiki knowledge.

**Key note:** In this archetype, the operator IS present. Real-time directives take effect immediately. When the operator says "from now on, always X" — that is a Priority-1 override of anything CLAUDE.md says. It also gets logged to raw/notes/ for persistence.

---

#### Example 2: Harness-Managed Agent (OpenArms v10 Model)

**Agent type:** Agent managed by a stage-gate harness. The harness injects stage-specific skills at stage boundaries and de-emphasizes CLAUDE.md.

**Files that load:**

| Phase | File | Mode | Precedence |
|-------|------|------|------------|
| Auto | `AGENTS.md` | Auto-injected | 2 |
| Auto | `.mcp.json` + `.claude/settings.json` | Auto-loaded | — |
| Harness-injected | Stage-specific skill (e.g., `implement-stage.md`) | Injected by harness at stage boundary | 5 |
| NOT loaded | `CLAUDE.md` | Harness de-emphasizes it — stage skill is primary | (bypassed) |
| JIT | Task inputs, harness-owned context files | Provided per task | varies |

**Override chain when conflict:** Harness runtime context > stage-specific skill > AGENTS.md > wiki.

**Key insight:** In harness-managed architectures, CLAUDE.md's role shrinks dramatically. The harness is the authority — it decides what context to inject at each stage. The AGENTS.md remains because it is cross-tool and may be read even when Claude Code is not the executor. The five cognitive contexts identified in OpenArms v10 (interactive operator, solo run-mode agent, sub-agents, persona templates, provisioned agents) are all audience variations on the same project context — the solution is not a single file trying to serve all five, but stage-skill injection that addresses each archetype directly.

---

#### Example 3: Provisioned Fleet Agent (OpenFleet Architecture)

**Agent type:** One of 10 specialized OpenFleet agents running in a git worktree, receiving dispatch via task files, generating heartbeat ticks on a cadence.

**Files that load:**

| Phase | File | Mode | Scope | Precedence |
|-------|------|------|-------|------------|
| Auto (workspace) | `workspace/SOUL.md` | Auto-injected in worktree | Workspace | 3 |
| Auto (workspace) | `workspace/AGENTS.md` | Auto-injected | Workspace | 3 |
| Auto (workspace) | Agent persona file | Auto-injected for this agent type | Workspace | 3 |
| Visible (distant) | Repo `AGENTS.md` | Visible from worktree, lower precedence | Project | 2 |
| JIT (dispatch) | `workspace/tasks/<id>.md` | Dispatched by orchestrator | Task | 3 (task-scope override) |
| JIT (tick) | `workspace/heartbeat/<tick>.md` | Generated each tick | Session | — (state) |
| JIT (streamed) | `workspace/feed/<event>.md` | Incoming fleet signals | Session | — (state) |
| JIT (earned) | `workspace/tier-context.md` | Unlocked by approval rate tier | Workspace | 3 |

**Override chain when conflict:** `tasks/<id>.md` (per-task authority) → `SOUL.md` (agent identity) → workspace `AGENTS.md` → repo `AGENTS.md` → wiki knowledge.

**Key insight:** The workspace scope creates a genuine scope boundary. The agent operates "inside" the workspace — the repo-level docs exist but are lower-precedence than the workspace-level configuration. This is the architectural expression of "agents need their own operating environment, not just a role in the shared one." The heartbeat and feed files are not rules — they are state. They accumulate without creating override conflicts because they describe what IS, not what to DO.

---

#### Example 4: Sub-Agent Dispatched From Claude

**Agent type:** A sub-agent spawned via the Agent tool in a Claude Code session. Sub-agents have minimal context inheritance.

**Files that load:**

| Phase | File | Mode | Notes |
|-------|------|------|-------|
| Spawn | Spawn prompt (only) | Provided by parent | The only reliable context |
| Uncertain | `CLAUDE.md` / `AGENTS.md` | Possibly inherited | Inheritance behavior is NOT guaranteed |
| JIT | Whatever sub-agent queries | Via MCP tools | Sub-agent must explicitly request |

**Override chain when conflict:** Spawn prompt dominates. Everything else is potentially absent.

> [!warning] The Sub-Agent Context Problem
>
> Sub-agents have minimal guaranteed context. Unlike a full Claude Code session that auto-loads CLAUDE.md and AGENTS.md, a spawned sub-agent receives only its spawn prompt reliably. The practical implication: **include all critical rules IN the spawn prompt** — do not rely on AGENTS.md inheritance. Use structured formats (tables, MUST/MUST NOT blocks) in spawn prompts because they are more reliably parsed than prose.
>
> This is not a limitation to route around — it is an architectural fact. The spawn prompt IS the sub-agent's Layer 1 and Layer 2. Design it accordingly: include identity, scope, hard rules, and the specific task. Keep it under 200 tokens to avoid context pollution. If the sub-agent needs wiki knowledge, give it explicit MCP gateway access and specific query instructions.

---

#### Example 5: External MCP Client (Sister Project Agent)

**Agent type:** An agent from a sister project (openfleet, aicp, dspd) that connects to our wiki's MCP server to query knowledge.

**Files that load:**

| Phase | File | Source | Mode | Notes |
|-------|------|--------|------|-------|
| Auto | Sister project's own `CLAUDE.md` + `AGENTS.md` | Their repo | Auto-injected | Their operating contract |
| Directed | Our `AGENTS.md` | Our repo (via `--wiki-root`) | Read as reference | Not adopted as authority |
| JIT | Our wiki pages | Our repo (via MCP tools) | On-demand queries | Authoritative for the content queried |

**Override chain when conflict:** Sister project's local config → our AGENTS.md (read as reference, not binding) → our wiki knowledge.

**Key insight:** External MCP clients are reading our content as a library, not adopting our rules. Our AGENTS.md says "run pipeline post after wiki changes" — that rule applies to US, not to an openfleet agent that happens to query our wiki. The gateway query tools return knowledge content, not instructions. This distinction (knowledge vs. instructions) maps to dimension-4 (responsibility: Knowledge vs. Rules). External consumers receive Knowledge; Rules only bind internal agents.

---

## Open Questions

> [!question] Can the taxonomy be encoded as YAML frontmatter on each context file for machine-readable discovery?
> Each root doc (`AGENTS.md`, `CLAUDE.md`, `TOOLS.md`, etc.) could have YAML frontmatter encoding its 8-dimension profile. A `context-audit` tool could then read all frontmatter-tagged files and render the complete catalog automatically. The challenge: these files (AGENTS.md, CLAUDE.md) are plain markdown intended for cross-tool consumption — adding frontmatter may confuse tools that don't know how to parse it. A separate `.context-catalog.yaml` sidecar file might be the right solution.

> [!question] How do we detect origin/authority automatically vs having to declare it?
> Origin is currently implicit — there is no machine-readable field that says "this file is operator-authority." The taxonomy captures this analytically, but there is no enforcement. A `pipeline validate` rule could check that files in `raw/notes/` are never referenced as optional and that runtime-generated files are never treated as authoritative rules. The taxonomy creates the vocabulary; tooling would need to encode it.

> [!question] When auto-injection limits are reached (large files), which gets truncated?
> Claude Code loads CLAUDE.md and AGENTS.md at session start. If both are large (combined 300+ lines), the context window cost at session start is non-trivial. When the window fills later, earlier-loaded content may be deprioritized by the model's attention mechanism (not truncated but less salient). There is no documented truncation behavior for auto-injected files. The ETH Zurich research finding (3% success drop for AI-generated context files) may partly reflect this — large auto-injected files dilute attention on the actual task.

> [!question] For provisioned agents, is there a formal scope transition that should trigger explicit re-loading?
> In OpenFleet, an agent entering a new task (`tasks/<id>.md` dispatched) represents a task-scope transition. Should the agent explicitly re-read its SOUL.md at each task boundary (in case SOUL.md has been updated by a harness)? Currently implicit. A formal "scope transition hook" (analogous to `pre-task`, `post-task`) could solve this — the harness injects a re-read instruction at each dispatch.

> [!question] What is the right granularity for the "Responsibility" dimension as systems grow?
> The current 7 responsibility values (Identity / Rules / Methodology / Tools / Knowledge / State / Navigation) are adequate for this wiki. In OpenFleet, some files own compound responsibilities (SOUL.md owns identity + rules + methodology for one agent). Does compound responsibility indicate a design smell, or is it appropriate for a per-agent config file that must be self-contained? The dimension may need a "compound" value for inherently multi-responsibility files.

---

## How This Connects — Navigate From Here

> [!abstract] From This Taxonomy → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **The three-layer pattern this builds on** | [[three-layer-agent-context-architecture|Three-Layer Agent Context Architecture]] |
> | **The 8 root docs catalyzed** | [[root-documentation-map|Root Documentation Map — Repository-Level Files]] |
> | **Agent context model (broader)** | [[model-context-engineering|Model — Context Engineering]] |
> | **Claude Code context behaviors** | [[model-claude-code|Model — Claude Code]] |
> | **Skills subsystem (Layer 3 detail)** | [[model-skills-commands-hooks|Model — Skills, Commands, and Hooks]] |
> | **Original source for three-layer synthesis** | [[src-skillmd-claudemd-agentsmd-three-layer-context|Three-Layer Context Synthesis — SKILL.md vs CLAUDE.md vs AGENTS.md]] |
> | **Source of the five-cognitive-contexts framing** | [[src-openarms-v10-enforcement|OpenArms v10 — Enforcement Architecture Synthesis]] |
> | **Source of the workspace expansion pattern** | [[src-openfleet-fleet-architecture|OpenFleet Fleet Architecture Synthesis]] |
> | **System-level map** | [[super-model|Super-Model — Research Wiki as Ecosystem Intelligence Hub]] |

## Relationships

- BUILDS ON: [[three-layer-agent-context-architecture|Three-Layer Agent Context Architecture]]
- BUILDS ON: [[root-documentation-map|Root Documentation Map]]
- RELATES TO: [[model-context-engineering|Model — Context Engineering]]
- RELATES TO: [[model-claude-code|Model — Claude Code]]
- RELATES TO: [[model-skills-commands-hooks|Model — Skills, Commands, and Hooks]]
- EXTENDS: [[src-openarms-v10-enforcement|OpenArms v10 — Five Cognitive Contexts]]
- DERIVED FROM: [[src-openfleet-fleet-architecture|OpenFleet Fleet Architecture]]
- PART OF: [[super-model|Super-Model — Research Wiki as Ecosystem Intelligence Hub]]

## Backlinks

[[three-layer-agent-context-architecture|Three-Layer Agent Context Architecture]]
[[Root Documentation Map]]
[[model-context-engineering|Model — Context Engineering]]
[[model-claude-code|Model — Claude Code]]
[[model-skills-commands-hooks|Model — Skills, Commands, and Hooks]]
[[OpenArms v10 — Five Cognitive Contexts]]
[[OpenFleet Fleet Architecture]]
[[super-model|Super-Model — Research Wiki as Ecosystem Intelligence Hub]]
