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
2. Read each file IN FULL. No `offset` reads under 200 lines.
   Pre-bash hook blocks reflexive truncation; respect it.
3. Do NOT emit intermediate summaries between levels. Read. Walk.
4. Do NOT propose interpretations during the walk. Save synthesis
   for the END attestation only.
5. If a file is missing where the tree expected it, that's a brain-bug.
   Log it (one line per missing file) and continue. Do not abort.
6. No file writes during the walk. Read-only.

The tree IS the order. If you get lost reading random files, the
tree is buggy — that's the bug to fix, not your behavior.

## Argument modes

| Invocation | Behavior |
|---|---|
| `/load-brain` (no args) | Full deterministic walk — the 13-level tree below, ~76 reads |
| `/load-brain <topic>` | Focused load — just the topic's files (vocabulary below) |
| `/load-brain <topic1> <topic2> ...` | Union of multiple topics |

For the LIGHT essentials-only set, use `/load-brain-light` instead.

### Topic vocabulary

| Topic | Aliases | What it loads (reads) |
|---|---|---|
| `principles` | `laws` | 5 files in `wiki/lessons/04_principles/hypothesis/` |
| `super-model` | `topology`, `center` | `wiki/spine/super-model/*.md` (6 files: root + 5 sub-super-models) |
| `foundation` | | `wiki/spine/models/foundation/*.md` (3 models) |
| `quality` | `sfif` | `wiki/spine/models/quality/*.md` (2 models) |
| `agent-config` | | `wiki/spine/models/agent-config/*.md` (4 models) |
| `depth` | | `wiki/spine/models/depth/*.md` (5 models) |
| `ecosystem` | | `wiki/spine/models/ecosystem/*.md` (3 models) |
| `registry` | `index` | `wiki/spine/references/model-registry.md` (1) |
| `engine` | `yaml`, `configs` | `wiki/config/{methodology,wiki-schema,artifact-types}.yaml` (3) |
| `sdlc` | `aidlc`, `process` | sdlc-customization-framework + src-sdlc-frameworks + src-aidlc (3) |
| `standards` | | All 28 in `wiki/spine/standards/` |
| `goldilocks` | `flow`, `selection` | goldilocks-flow + goldilocks-protocol + sdlc-customization-framework (3) |
| `<model-name>` | | The named model's page + companion `*-standards.md` if it exists (1-2) |

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

## The Tree — 13 levels, ~76 reads

### Level 0 — Identity & operational rules (10)

Verify presence + re-read for context warmth:

```
Read CLAUDE.md
Read AGENTS.md
Read CONTEXT.md
Read .claude/rules/routing.md
Read .claude/rules/methodology.md
Read .claude/rules/self-reference.md
Read .claude/rules/work-mode.md
Read .claude/rules/learnings.md
Read .claude/rules/ingestion.md
Read .claude/rules/hook-architecture.md
```

### Level 1 — The 5 Governing Principles (LAWS) (5)

Foundational laws that constrain everything below.

```
Read wiki/lessons/04_principles/hypothesis/infrastructure-over-instructions-for-process-enforcement.md
Read wiki/lessons/04_principles/hypothesis/structured-context-governs-agent-behavior-more-than-content.md
Read wiki/lessons/04_principles/hypothesis/right-process-for-right-context-the-goldilocks-imperative.md
Read wiki/lessons/04_principles/hypothesis/declarations-are-aspirational-until-infrastructure-verifies-them.md
Read wiki/lessons/04_principles/hypothesis/spec-driven-evolution-the-project-evolves-its-own-spec-to-fix-bugs-it-exhibits.md
```

### Level 2 — Super-model (system topology) (6)

What this system IS, at the highest abstraction.

```
Read wiki/spine/super-model/super-model.md
Read wiki/spine/super-model/knowledge-architecture.md
Read wiki/spine/super-model/goldilocks-protocol.md
Read wiki/spine/super-model/enforcement-hierarchy.md
Read wiki/spine/super-model/integration-ecosystem.md
Read wiki/spine/super-model/work-management.md
```

### Level 3 — Foundation models (substrate) (3)

The 3 foundational models everything else builds on.

```
Read wiki/spine/models/foundation/model-llm-wiki.md
Read wiki/spine/models/foundation/model-methodology.md
Read wiki/spine/models/foundation/model-wiki-design.md
```

### Level 4 — Quality + SFIF (architecture lifecycle) (2)

SFIF (Scaffold → Foundation → Infrastructure → Features) and the
quality/failure-prevention model.

```
Read wiki/spine/models/quality/model-sfif-architecture.md
Read wiki/spine/models/quality/model-quality-failure-prevention.md
```

### Level 5 — Agent-config models (how AI runs) (4)

How agents are configured, extended, and integrated.

```
Read wiki/spine/models/agent-config/model-markdown-as-iac.md
Read wiki/spine/models/agent-config/model-claude-code.md
Read wiki/spine/models/agent-config/model-skills-commands-hooks.md
Read wiki/spine/models/agent-config/model-per-project-assistant-profile.md
```

### Level 6 — Depth models (5)

Models that add depth to the foundation.

```
Read wiki/spine/models/depth/model-second-brain.md
Read wiki/spine/models/depth/model-knowledge-evolution.md
Read wiki/spine/models/depth/model-context-engineering.md
Read wiki/spine/models/depth/model-local-ai.md
Read wiki/spine/models/depth/model-notebooklm.md
```

### Level 7 — Ecosystem models (3)

How multiple projects compose into an ecosystem.

```
Read wiki/spine/models/ecosystem/model-ecosystem.md
Read wiki/spine/models/ecosystem/model-mcp-cli-integration.md
Read wiki/spine/models/ecosystem/model-automation-pipelines.md
```

### Level 8 — Model registry (master index) (1)

The canonical 16-model registry — confirms the map.

```
Read wiki/spine/references/model-registry.md
```

### Level 9 — SDLC / aidlc (process framework) (3)

Process customization framework + source syntheses for SDLC and aidlc.

```
Read wiki/domains/cross-domain/methodology-framework/sdlc-customization-framework.md
Read wiki/sources/wiki-methodology/src-sdlc-frameworks-research.md
Read wiki/sources/wiki-methodology/src-aidlc-aws-driven-development-lifecycle.md
```

### Level 10 — Methodology engine (YAML programs) (3)

The yaml programs that compile the methodology model into runtime.

```
Read wiki/config/methodology.yaml
Read wiki/config/wiki-schema.yaml
Read wiki/config/artifact-types.yaml
```

### Level 11 — Standards (per-type + per-model) (28)

Per-type page quality contracts (20):

```
Read wiki/spine/standards/concept-page-standards.md
Read wiki/spine/standards/source-synthesis-page-standards.md
Read wiki/spine/standards/comparison-page-standards.md
Read wiki/spine/standards/reference-page-standards.md
Read wiki/spine/standards/deep-dive-page-standards.md
Read wiki/spine/standards/lesson-page-standards.md
Read wiki/spine/standards/pattern-page-standards.md
Read wiki/spine/standards/decision-page-standards.md
Read wiki/spine/standards/domain-overview-page-standards.md
Read wiki/spine/standards/evolution-page-standards.md
Read wiki/spine/standards/learning-path-page-standards.md
Read wiki/spine/standards/operations-plan-page-standards.md
Read wiki/spine/standards/epic-page-standards.md
Read wiki/spine/standards/task-page-standards.md
Read wiki/spine/standards/note-page-standards.md
Read wiki/spine/standards/session-handoff-standards.md
Read wiki/spine/standards/per-project-assistant-profile-standards.md
Read wiki/spine/standards/gateway-output-contract.md
Read wiki/spine/standards/harness-contract.md
Read wiki/spine/standards/cursor-state-folder-standards-common-cross-project-runtime-state-surface.md
```

Per-model standards (8) — what good looks like for each model:

```
Read wiki/spine/standards/model-standards/model-llm-wiki-standards.md
Read wiki/spine/standards/model-standards/model-methodology-standards.md
Read wiki/spine/standards/model-standards/model-wiki-design-standards.md
Read wiki/spine/standards/model-standards/model-quality-failure-prevention-standards.md
Read wiki/spine/standards/model-standards/model-claude-code-standards.md
Read wiki/spine/standards/model-standards/model-skills-commands-hooks-standards.md
Read wiki/spine/standards/model-standards/model-context-engineering-standards.md
Read wiki/spine/standards/model-standards/model-knowledge-evolution-standards.md
```

### Level 12 — Goldilocks flow + indexes (selection mechanism) (3)

The selection mechanism + spine map + lessons map.

```
Read wiki/spine/goldilocks-flow.md
Read wiki/spine/_index.md
Read wiki/lessons/_index.md
```

## END — BRAIN LOADED attestation

After the walk completes, emit a single attestation:

```markdown
# BRAIN LOADED — Research Wiki / Second Brain (<DATE>)

## Reads completed
- Level 0 (identity + rules): <N> files
- Level 1 (principles): 5 files — P1, P2, P3, P4, P5
- Level 2 (super-model): 6 files
- Level 3 (foundation models): 3 files
- Level 4 (SFIF + quality): 2 files
- Level 5 (agent-config models): 4 files
- Level 6 (depth models): 5 files
- Level 7 (ecosystem models): 3 files
- Level 8 (model registry): 1 file
- Level 9 (SDLC / aidlc): 3 files
- Level 10 (methodology engine yaml): 3 files
- Level 11 (standards): 28 files (20 per-type + 8 per-model)
- Level 12 (selection mechanism): 3 files
- Total: <N> reads

## 5 Principles internalized (by name)
1. <P1 name>
2. <P2 name>
3. <P3 name>
4. <P4 name>
5. <P5 name>

## 17 spine models internalized (by name + tier)
Foundation: <names>
Quality: <names>
Agent-config: <names>
Depth: <names>
Ecosystem: <names>

## Methodology engine
- methodology.yaml: <N> models, <N> stages
- wiki-schema.yaml: <N> required fields, <N> page types, <N> relationship verbs
- artifact-types.yaml: <N> types, <N> classes

## Standards loaded
- Per-type page standards: 20
- Per-model quality standards: 8

## Missing-file flags (if any)
<one line per file the tree expected but didn't find — else "(none)">

## Status
BRAIN LOADED. The agent has internalized the full system — 5
principles, super-model + 5 sub-super-models, 17 models across
5 tiers, 28 standards, 3 methodology engine YAMLs, SDLC/aidlc
process framework, and Goldilocks selection mechanism. Ready
for operator direction.
```

## Composition with /orient and /load-context

- `/orient` — situational orientation (recent state, pipeline health,
  active milestones). Lightweight. Run on every fresh session.
- `/load-brain` — THIS command. PERMANENT brain. Heavy (~76 reads).
  Run on a cold-start, after compaction, or whenever you need to
  re-warm the full self-referential awareness.
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
