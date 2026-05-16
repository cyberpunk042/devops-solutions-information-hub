Deterministic brain-load tree walk for the research wiki / second brain.

> Slash-invoked. Operator types `/load-brain` literally. This is the
> heavy companion to `/orient` — `/orient` does situational orientation
> (recent state, pipeline health), `/load-brain` does the PERMANENT
> BRAIN LOAD (every principle, every model, every super-model, every
> standard, every methodology config).

## Why this command exists

`/orient` covers session state. `CLAUDE.md` + `AGENTS.md` auto-load
identity + hot-path rules. Neither of those guarantees the agent has
internalized the FULL brain — the 5 governing principles, the 6-page
super-model, the 17 model pages, the 3 methodology engine YAMLs, the
28 standards, the SFIF / SDLC / aidlc framing.

Without this, agents drift toward generic-LLM behavior when work
requires deep self-referential awareness. This command is the
unavoidable, deterministic, tree-walk re-load that GUARANTEES
brain-resident knowledge by the end of execution.

Pair: `/load-brain` (PERMANENT brain — laws, topology, models,
standards) + `/load-context` (SESSION state — handoffs, recent notes,
diffs). Use both together for a cold-start or post-compact full warm.

## Discipline — DO NOT STOP

1. Execute every level in order. Within a level, read in parallel.
2. Read each file IN FULL by default. EXCEPTION: large reference pages
   (>500 lines) marked `# core sections` in the level instructions MAY
   read Summary + Key Insights + Deep Analysis + Open Questions only,
   skipping the trailing Relationships + Backlinks (catalog data, not
   learning content). Full reads of those pages available via topic-args.
   Pre-bash hook blocks reflexive truncation pipes; respect it.
3. AT REFLECTION CHECKPOINTS (after L3, L4, L5), emit the structured
   reflection block as instructed. This is the HIGHWAY-BUILDING step —
   NOT atomized summaries but synthesis that CONNECTS what was just
   loaded. Reflections are operator-visible (they verify comprehension).
4. BETWEEN reflection checkpoints, do NOT emit ad-hoc summaries.
   Read. Walk. Reach the next reflection.
5. If a file is missing where the tree expected it, that's a brain-bug.
   Log it (one line per missing file) and continue. Do not abort.
6. No file writes during the walk. Read-only.
7. **Topic-args layer DEEPER reads on top of the default walk — they
   DO NOT replace the default.** `/load-brain methodology` runs the
   full default walk (~42 reads + 3 reflections) AND adds full reads of
   methodology-related files (including the demoted ones not in default).

The tree IS the order. If you get lost reading random files, the
tree is buggy — that's the bug to fix, not your behavior.

This is the **Goldilocks default** (remastered 2026-05-16) — ~42 reads
at ~500K tokens producing 4/4 comprehension via order + reflection
(was: 76 reads at ~800K producing 4/4 catalog with no inter-level
synthesis). Design rationale: see `docs/SESSION-2026-05-16-handoff.md`
Part 1.

## Argument modes

| Invocation | Behavior |
|---|---|
| `/load-brain` (no args) | **Goldilocks default** — the 7-level tree below + 3 reflection blocks (~42 reads, ~500K tokens) |
| `/load-brain <topic>` | Default walk + DEEPER on that topic (loads topic's full files, including ones demoted from default) |
| `/load-brain <topic1> <topic2> ...` | Default walk + deeper on each named topic (union of deeper-reads layered on the default) |

**Topic-args are ADDITIVE, not replacements**: `/load-brain standards` runs the default 7-level walk AND adds full reads of all 28 standards (default only loads 6 universal ones). This was a 2026-05-16 reshape — operator-doctrine: topic should narrow direction without losing the foundation.

For the LIGHT essentials-only re-warm (no reflections, ~11 reads), use `/load-brain-light` instead.

### Topic vocabulary

Topic-args layer DEEPER reads on top of the default walk (see Argument modes above). `In default?` column shows whether the topic's files are ALREADY in the default Goldilocks walk (so the topic-arg adds full reads of any sub-files not in default) or DEMOTED (default doesn't load them; topic-arg restores).

| Topic | Aliases | What it loads (reads) | In default? |
|---|---|---|---|
| `rules` | `claude-rules`, `identity` | 7 files in `.claude/rules/*.md` | YES (L0) |
| `principles` | `laws` | 5 files in `wiki/lessons/04_principles/hypothesis/` | YES (L1) |
| `super-model` | `topology`, `center` | `wiki/spine/super-model/*.md` (6 files: root + 5 sub-super-models) | YES (L2) |
| `registry` | `index` | `wiki/spine/references/model-registry.md` (1) | YES (L2) |
| `engine` | `yaml`, `configs` | `wiki/config/{methodology,wiki-schema,artifact-types}.yaml` (3) | YES (L3) |
| `methodology-profiles` | `sdd-tdd`, `profiles` | `wiki/config/methodology-profiles/{spec-driven,test-driven}.yaml` (2) | YES (L3) |
| `goldilocks` | `flow`, `selection` | goldilocks-flow + goldilocks-protocol + sdlc-customization-framework (3) | PARTIAL (goldilocks-flow + goldilocks-protocol in default; sdlc-customization-framework demoted) |
| `foundation` | | `wiki/spine/models/foundation/*.md` (3 models, FULL reads incl. Relationships+Backlinks) | YES (L4 — core-sections in default; topic-arg restores full reads) |
| `quality` | `sfif` | `wiki/spine/models/quality/*.md` (2 models, full reads) | YES (L4 — core-sections in default; topic-arg restores full) |
| `agent-config` | | `wiki/spine/models/agent-config/*.md` (4 models — adds markdown-as-iac) | PARTIAL (3 of 4 in default; markdown-as-iac demoted) |
| `depth` | | `wiki/spine/models/depth/*.md` (5 models — adds second-brain + local-ai + notebooklm) | PARTIAL (2 of 5 in default; 3 demoted) |
| `ecosystem` | | `wiki/spine/models/ecosystem/*.md` (3 models — adds mcp-cli-integration + automation-pipelines) | PARTIAL (1 of 3 in default; 2 demoted) |
| `standards` | | All 28 in `wiki/spine/standards/` | PARTIAL (6 of 28 universal in default; 22 demoted) |
| `sdlc` | `aidlc`, `process` | sdlc-customization-framework + src-sdlc-frameworks + src-aidlc (3) | DEMOTED (was L9 in v1; operator-decision context, on-demand only) |
| `<model-name>` | | The named model's page + companion `*-standards.md` if it exists (1-2) | varies |

Valid `<model-name>` values: `llm-wiki`, `methodology`, `wiki-design`, `sfif`, `quality-failure-prevention`, `markdown-as-iac`, `claude-code`, `skills-commands-hooks`, `per-project-assistant-profile`, `second-brain`, `knowledge-evolution`, `context-engineering`, `local-ai`, `notebooklm`, `ecosystem`, `mcp-cli-integration`, `automation-pipelines`.

### Resolution rules

- Topic names are case-insensitive
- Spaces or hyphens are equivalent (e.g. "LLM Wiki" → `llm-wiki`)
- `and` between topics is a separator (e.g. `/load-brain llm-wiki and methodology` loads both)
- Unknown topic → ask the operator to clarify, do NOT guess
- For focused loads, emit a small FOCUSED attestation at the end (not the full BRAIN LOADED report). Format:
  ```
  FOCUSED BRAIN LOAD complete — Topic(s): <name>
  Files read: <N>
  Status: ready for operator direction.
  ```

## The Tree — 7 levels, ~42 reads, 3 reflection blocks

The **Goldilocks remaster** (2026-05-16). Fewer reads (76 → ~42) at deeper comprehension via inter-level reflection blocks that turn atomized reads into a connected map. Token cost: ~500K (was ~800K). See `docs/SESSION-2026-05-16-handoff.md` Part 1 for the design rationale (4 main trim levers + 3 supplementary + 3 reflection stops).

### Level 0 — Identity layer (7)

The 7 `.claude/rules/*.md` files. NOT re-reading CLAUDE.md / AGENTS.md / CONTEXT.md (they auto-load at session start; re-reading wastes ~30K tokens). The rules files are NOT auto-loaded — they're the depth that informs every subsequent level.

```
Read .claude/rules/routing.md
Read .claude/rules/methodology.md
Read .claude/rules/self-reference.md
Read .claude/rules/work-mode.md
Read .claude/rules/learnings.md
Read .claude/rules/ingestion.md
Read .claude/rules/hook-architecture.md
```

### Level 1 — The 5 Governing Principles (LAWS) (5)

Foundational laws. Every model + standard + workflow operates within them.

```
Read wiki/lessons/04_principles/hypothesis/infrastructure-over-instructions-for-process-enforcement.md
Read wiki/lessons/04_principles/hypothesis/structured-context-governs-agent-behavior-more-than-content.md
Read wiki/lessons/04_principles/hypothesis/right-process-for-right-context-the-goldilocks-imperative.md
Read wiki/lessons/04_principles/hypothesis/declarations-are-aspirational-until-infrastructure-verifies-them.md
Read wiki/lessons/04_principles/hypothesis/spec-driven-evolution-the-project-evolves-its-own-spec-to-fix-bugs-it-exhibits.md
```

### Level 2 — System topology (7)

The super-model + 5 sub-super-models + model-registry. The MAP of the brain. After this, you know what models EXIST and how they relate.

```
Read wiki/spine/super-model/super-model.md
Read wiki/spine/super-model/knowledge-architecture.md
Read wiki/spine/super-model/goldilocks-protocol.md
Read wiki/spine/super-model/enforcement-hierarchy.md
Read wiki/spine/super-model/integration-ecosystem.md
Read wiki/spine/super-model/work-management.md
Read wiki/spine/references/model-registry.md
```

### Level 3 — Methodology engine + selection (6)

The 3 engine YAMLs + the 2 methodology profiles (SDD + TDD per operator-doctrine 2026-05-16: "do proper Spec Driven Development combined with Test Driven Development") + the Goldilocks selection mechanism. This is the OPERATING SYSTEM.

```
Read wiki/config/methodology.yaml
Read wiki/config/wiki-schema.yaml
Read wiki/config/artifact-types.yaml
Read wiki/config/methodology-profiles/spec-driven.yaml
Read wiki/config/methodology-profiles/test-driven.yaml
Read wiki/spine/goldilocks-flow.md
```

### 🔄 REFLECTION 1 — Laws · Topology · Engine

**After Level 3, before Level 4, emit a structured reflection (~200 words). Operator-visible. This is the FIRST highway.**

Answer in your reflection block:

1. **What are the 5 laws (P1-P5)**, in one sentence each (from memory after the reads — verify against your loaded knowledge).
2. **Where does each principle LIVE in the super-model?** Which sub-super-model covers which principle? (e.g., P1 Infrastructure > Instructions → enforcement-hierarchy.)
3. **How does the methodology engine IMPLEMENT the laws?** Trace 2-3 concrete examples (e.g., P1 → methodology.yaml's ALLOWED/FORBIDDEN per stage = infrastructure-level enforcement; P3 Goldilocks → goldilocks-flow → SDLC profile selection by phase × scale).
4. **What's the OPERATING CONTRACT** that emerges from laws + topology + engine? In 2-3 sentences.

The connections you emit here turn 25 atomized reads (L0-L3) into one connected map. If the reflection feels shallow, re-read the most relevant page before proceeding to L4.

### Level 4 — Foundation + Quality + Agent-config models (8)

The 8 spine models that constitute the brain's working core. For large reference pages (>500 lines, marked `# core sections`), read Summary + Key Insights + Deep Analysis + Open Questions; skip the trailing Relationships + Backlinks (catalog data, not learning content). Full reads available via topic-args (`/load-brain methodology` etc.).

Foundation (3):
```
Read wiki/spine/models/foundation/model-llm-wiki.md                   # full (573 lines)
Read wiki/spine/models/foundation/model-methodology.md                # core sections (898 lines)
Read wiki/spine/models/foundation/model-wiki-design.md                # full (413 lines)
```

Quality (2):
```
Read wiki/spine/models/quality/model-sfif-architecture.md             # full (268 lines)
Read wiki/spine/models/quality/model-quality-failure-prevention.md    # core sections (526 lines)
```

Agent-config (3) — markdown-as-iac demoted to topic-arg:
```
Read wiki/spine/models/agent-config/model-claude-code.md              # core sections (617 lines)
Read wiki/spine/models/agent-config/model-skills-commands-hooks.md    # core sections (456 lines)
Read wiki/spine/models/agent-config/model-per-project-assistant-profile.md   # full (201 lines)
```

### 🔄 REFLECTION 2 — Model composition

**After Level 4, before Level 5. Operator-visible. SECOND highway.**

Answer:

1. **How do the 8 models compose?** Where's SFIF recursive (project / feature / task / sub-component levels)?
2. **Where does the per-project-assistant-profile model INTERSECT with model-claude-code + model-skills-commands-hooks?** (Hint: profile defines WHAT, the others define HOW.)
3. **What's the methodology model's GOVERNANCE role over the other 7?** (Hint: it's the super-model that governs all work-process; the other models operate within its stages + gates.)
4. **Trace one work-shape end-to-end**: e.g., a `feature_authoring` task → methodology model picks `feature-development` → SFIF says which tier (Foundation/Infrastructure/Features) → per-type page standards say what GOOD looks like → quality-failure-prevention + agent-config models say HOW to enforce → result: a fix landed in the target project, audit-anchored, R20-respected.

Connects L1 (laws) + L2 (topology) + L3 (engine) + L4 (models) into one operational flowchart.

### Level 5 — Universal standards (6)

The 6 standards that apply broadly — every authoring / handoff / decision touches at least one. Per-type standards for less-frequent page types (concept / source-synthesis / comparison / reference / deep-dive / pattern / decision / domain-overview / evolution / learning-path / operations-plan / epic / note) available via `/load-brain standards`. Per-model standards for wiki-design / quality-failure-prevention / claude-code / skills-commands-hooks / context-engineering / knowledge-evolution also via topic-args.

```
Read wiki/spine/standards/session-handoff-standards.md
Read wiki/spine/standards/per-project-assistant-profile-standards.md
Read wiki/spine/standards/model-standards/model-methodology-standards.md
Read wiki/spine/standards/model-standards/model-llm-wiki-standards.md
Read wiki/spine/standards/task-page-standards.md
Read wiki/spine/standards/lesson-page-standards.md
```

### 🔄 REFLECTION 3 — Operational contract

**After Level 5, before Level 6. Operator-visible. THIRD highway.**

Answer:

1. **What does GOOD look like** at every layer of output? (frontmatter / required-sections / content thresholds / per-type quality bars / methodology stage gates / profile success criteria.)
2. **How does P4 (declarations aspirational until verified) CASCADE** through: schema enforcement (wiki-schema.yaml) → per-type quality bars (page-standards.md) → methodology gate commands (`pipeline post`, `install.sh --check`) → profile success criteria + telemetry?
3. **Name the operational contract end-to-end**: what verifies what, at what stage, with what command? In 3-5 sentences.
4. **What anti-patterns are encoded across the standards?** (vague Done When, missing Evidence in lessons, single-RELATES-TO instead of precise verbs, methodology-theater, scope invention, etc.)

By here, the agent has a working model of WHAT to build, HOW to process, what GOOD looks like, and HOW to VERIFY. The third highway connects standards (L5) back to principles (L1) via P4's cascade.

### Level 6 — Depth + Ecosystem (trimmed) (3)

The 3 models that bridge into adjacent territory: how knowledge evolves, how context is engineered, how the ecosystem composes. Other depth + ecosystem models (`second-brain`, `local-ai`, `notebooklm`, `mcp-cli-integration`, `automation-pipelines`) available via topic-args.

```
Read wiki/spine/models/depth/model-knowledge-evolution.md             # full (326 lines)
Read wiki/spine/models/depth/model-context-engineering.md             # core sections (449 lines)
Read wiki/spine/models/ecosystem/model-ecosystem.md                   # core sections (391 lines)
```

## END — BRAIN LOADED attestation

After the walk + 3 reflections, emit:

```markdown
# BRAIN LOADED (Goldilocks remaster) — Research Wiki / Second Brain (<DATE>)

## Reads completed (~42 total)
- L0 (identity layer / 7 `.claude/rules/*.md`): 7 files
- L1 (5 governing principles): 5 files
- L2 (topology — super-model + 5 sub-super-models + registry): 7 files
- L3 (engine — methodology + schema + artifact-types + SDD + TDD + goldilocks-flow): 6 files
- L4 (foundation + quality + agent-config models): 8 files (5 full + 3 core-sections)
- L5 (6 universal standards): 6 files
- L6 (depth + ecosystem trimmed): 3 files
- **Total: 42 reads** (was 76 pre-remaster; ~45% reduction; ~500K tokens vs ~800K)

## Reflection blocks emitted
- REFLECTION 1 (laws · topology · engine synthesis): ✓
- REFLECTION 2 (model composition + governance): ✓
- REFLECTION 3 (operational contract + P4 cascade): ✓

## 5 Principles internalized (by name)
1. <P1 name — Infrastructure Over Instructions for Process Enforcement>
2. <P2 name — Structured Context Governs Agent Behavior More Than Content>
3. <P3 name — Right Process for Right Context (Goldilocks Imperative)>
4. <P4 name — Declarations Are Aspirational Until Infrastructure Verifies Them>
5. <P5 name — Spec-driven evolution: the project evolves its own spec to fix bugs>

## 8 working-core models internalized (by tier)
- Foundation: llm-wiki · methodology · wiki-design
- Quality: sfif-architecture · quality-failure-prevention
- Agent-config: claude-code · skills-commands-hooks · per-project-assistant-profile
- (also loaded: depth knowledge-evolution + context-engineering, ecosystem model-ecosystem)

## Methodology engine
- methodology.yaml: <N> models, <N> stages, <N> ALLOWED/FORBIDDEN protocols
- wiki-schema.yaml: <N> required fields, <N> page types, <N> relationship verbs
- artifact-types.yaml: <N> types, <N> artifact classes (document / artifact / documentation)
- methodology-profiles: spec-driven (45% document weight, [NEEDS CLARIFICATION], checklist-as-unit-tests) + test-driven (Red→Green→Refactor, bug-test-first)

## Standards loaded (universal — 6)
session-handoff · per-project-assistant-profile · model-methodology · model-llm-wiki · task-page · lesson-page

## Demoted-to-topic-arg (not loaded at default; available on demand)
- 14 per-type standards: concept · source-synthesis · comparison · reference · deep-dive · pattern · decision · domain-overview · evolution · learning-path · operations-plan · epic · note · cursor-state-folder + gateway-output-contract + harness-contract
- 6 per-model standards: wiki-design · quality-failure-prevention · claude-code · skills-commands-hooks · context-engineering · knowledge-evolution
- 3 depth models: second-brain · local-ai · notebooklm
- 2 ecosystem models: mcp-cli-integration · automation-pipelines
- 1 agent-config model: markdown-as-iac
- 3 SDLC/aidlc files: sdlc-customization-framework · src-sdlc-frameworks · src-aidlc
- 2 spine indexes: wiki/spine/_index · wiki/lessons/_index

## Missing-file flags (if any)
<one line per file the tree expected but didn't find — else "(none)">

## Status
BRAIN LOADED (Goldilocks remaster). 42 reads + 3 highway-building reflections at ~500K tokens vs ~800K pre-remaster. Comprehension verified inline via reflections. Ready for operator direction.
```

## Composition with /orient and /load-context

- `/orient` — situational orientation (recent state, pipeline health,
  active milestones). Lightweight. Run on every fresh session.
- `/load-brain` — THIS command. PERMANENT brain. Goldilocks default (~42 reads + 3 reflections, ~500K tokens). Run on a cold-start, after compaction, or whenever you need to re-warm the full self-referential awareness. Topic-args ADD deeper reads on top.
- `/load-context` — (planned, separate) SESSION state — last handoff,
  recent operator notes, recent log entries, recent diffs. Lightweight.
  Pair with `/load-brain` for a fully-warmed brain + situational
  awareness.

## Mechanism

100% deterministic per operator 2026-04-24 doctrine
(commands = 100% deterministic, skills = ~70%, hooks = logical).
The tree IS the program. The agent executes it without judgment.

## Cross-references

- 5 Principles: [wiki/lessons/04_principles/hypothesis/](../../wiki/lessons/04_principles/hypothesis/)
- Super-model: [wiki/spine/super-model/super-model.md](../../wiki/spine/super-model/super-model.md)
- Model registry: [wiki/spine/references/model-registry.md](../../wiki/spine/references/model-registry.md)
- Sister command: [orient.md](orient.md) (situational orient)
- Self-reference (this project IS the second brain): [../rules/self-reference.md](../rules/self-reference.md)
- Mechanism-determinism doctrine: [../rules/hook-architecture.md](../rules/hook-architecture.md)
