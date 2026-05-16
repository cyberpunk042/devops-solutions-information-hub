Light essentials-only brain load for the research wiki / second brain.

> Slash-invoked. Operator types `/load-brain-light` literally. Lightweight
> sibling of `/load-brain` (which does the full 76-read tree walk).

## Why this command exists

`/load-brain` is the unavoidable full load (~76 reads). It's the right tool
for a cold-start where the agent needs to internalize EVERYTHING. But sometimes
all you need is the load-bearing core — the laws, the topology entry, the
16-model index, the engine YAMLs, and the selection mechanism. That's what
`/load-brain-light` delivers: ~11 reads, the minimum viable brain.

After light load, the agent knows:
- The 5 governing principles (laws)
- That a super-model exists with sub-super-models
- That 16 named models exist (by name, from the registry)
- The methodology engine (9 models × 5 stages, schema, artifact types)
- How to select via Goldilocks flow

What the agent does NOT know after light load:
- The detailed content of any specific model page
- The per-type or per-model standards
- The depth / ecosystem / agent-config model details

Use `/load-brain-light <topic>` to layer specific topic detail on top of the
essentials — that's the design.

## Argument modes

| Invocation | Behavior |
|---|---|
| `/load-brain-light` (no args) | 11 essential reads |
| `/load-brain-light <topic>` | 11 essentials + that topic's full files |
| `/load-brain-light <t1> <t2> ...` | 11 essentials + union of topic files |

### Topic vocabulary

Same as `/load-brain`. See `.claude/commands/load-brain.md` for the full topic
table. Examples:

| Invocation | Adds |
|---|---|
| `/load-brain-light llm-wiki` | + `model-llm-wiki.md` + `model-llm-wiki-standards.md` |
| `/load-brain-light methodology` | + `model-methodology.md` (2 chunks) + `model-methodology-standards.md` |
| `/load-brain-light llm-wiki and methodology` | both pairs added |
| `/load-brain-light claude-code` | + `model-claude-code.md` + `model-claude-code-standards.md` |
| `/load-brain-light super-model` | + 5 sub-super-models (super-model.md already in essentials) |
| `/load-brain-light standards` | + all 28 standards files |

## Discipline

- Read every file in FULL. No `| head` / `| tail` without REASON env.
- No intermediate summaries between reads. Save synthesis for the end.
- If a file is missing where the tree expected it, log + continue.
- No file writes during the walk (read-only).

## The Essentials Walk — 11 reads

### Level 1 — The 5 Governing Principles (LAWS)

```
Read wiki/lessons/04_principles/hypothesis/infrastructure-over-instructions-for-process-enforcement.md
Read wiki/lessons/04_principles/hypothesis/structured-context-governs-agent-behavior-more-than-content.md
Read wiki/lessons/04_principles/hypothesis/right-process-for-right-context-the-goldilocks-imperative.md
Read wiki/lessons/04_principles/hypothesis/declarations-are-aspirational-until-infrastructure-verifies-them.md
Read wiki/lessons/04_principles/hypothesis/spec-driven-evolution-the-project-evolves-its-own-spec-to-fix-bugs-it-exhibits.md
```

### Level 2 — Super-model entry (topology center)

```
Read wiki/spine/super-model/super-model.md
```

### Level 3 — Model registry (16-model index)

```
Read wiki/spine/references/model-registry.md
```

### Level 4 — Methodology engine (yaml programs)

```
Read wiki/config/methodology.yaml
Read wiki/config/wiki-schema.yaml
Read wiki/config/artifact-types.yaml
```

### Level 5 — Goldilocks flow (selection mechanism)

```
Read wiki/spine/goldilocks-flow.md
```

## Then: apply topic args (if any)

For each topic the operator passed, resolve via the topic table in
`load-brain.md` and read the corresponding files. Examples:

- `llm-wiki` → `wiki/spine/models/foundation/model-llm-wiki.md` + `wiki/spine/standards/model-standards/model-llm-wiki-standards.md`
- `methodology` → `wiki/spine/models/foundation/model-methodology.md` (likely needs 2 offset reads — 898 lines) + `wiki/spine/standards/model-standards/model-methodology-standards.md`
- `claude-code` → `wiki/spine/models/agent-config/model-claude-code.md` + `wiki/spine/standards/model-standards/model-claude-code-standards.md`
- `sfif` → `wiki/spine/models/quality/model-sfif-architecture.md`
- `super-model` → already loaded super-model.md; add 5 sub-super-models: `knowledge-architecture.md`, `goldilocks-protocol.md`, `enforcement-hierarchy.md`, `integration-ecosystem.md`, `work-management.md`
- `standards` → all 28 in `wiki/spine/standards/` and `wiki/spine/standards/model-standards/`

### Resolution rules

- Topic names are case-insensitive
- Spaces or hyphens are equivalent (e.g. "LLM Wiki" → `llm-wiki`)
- `and` between topics is a separator
- Unknown topic → ask the operator to clarify, do NOT guess

## LIGHT BRAIN LOADED attestation

After the walk (essentials + any topic args), emit:

```markdown
# LIGHT BRAIN LOADED — Research Wiki / Second Brain (<DATE>)

## Essentials loaded (11 reads)
- 5 principles: P1, P2, P3, P4, P5
- super-model.md (system topology)
- model-registry.md (16-model index by name)
- methodology.yaml + wiki-schema.yaml + artifact-types.yaml (engine)
- goldilocks-flow.md (selection mechanism)

## Topic args applied
<list of topics + files added per topic, or "(none)">

## Total reads
<N>

## What the agent now knows
- 5 governing principles (laws)
- Super-model topology + 16-model map
- Methodology engine (9 models × 5 stages, schema, artifact types)
- Goldilocks selection (identity → profile → model → stage)
<+ topic-specific knowledge per loaded topic>

## What the agent does NOT know
- Detail on models not loaded via topic args
- Standards not loaded via topic args
- (To go deeper: re-run with more topic args, or run `/load-brain` for full)

## Status
LIGHT BRAIN LOADED. Ready for operator direction.
```

## Composition with other commands

- `/load-brain` (full ~76) — for cold-start, post-compaction, or maximum mastery
- `/load-brain-light` (this) — for quick re-warm, focused work, or low-context budget
- `/load-context` — session state (handoff, notes, queue) — sibling, not redundant
- `/orient` — situational orientation (predecessor, mixed identity + state)

## Mechanism

100% deterministic per operator 2026-04-24 doctrine. The essentials list IS
the program. The topic resolution table is the extension point.

## Cross-references

- [load-brain.md](load-brain.md) — full walk + topic vocabulary table
- [load-context.md](load-context.md) — session state (light)
- [load-context-deep.md](load-context-deep.md) — session state (deep)
- 5 Principles: [wiki/lessons/04_principles/hypothesis/](../../wiki/lessons/04_principles/hypothesis/)
- Super-model: [wiki/spine/super-model/super-model.md](../../wiki/spine/super-model/super-model.md)
- Model registry: [wiki/spine/references/model-registry.md](../../wiki/spine/references/model-registry.md)
