# .claude/rules/methodology.md — Methodology, Stages, Models, Schema

> Loaded on demand when work involves methodology decisions or page authoring. CLAUDE.md has the summary; this file has the operational detail.

## 5 Universal Stages

| Stage | Readiness | ALLOWED outputs | FORBIDDEN outputs | Gate |
|---|---|---|---|---|
| **document** | 0–25% | wiki-page, raw/notes/, research notes | code-file, test-file | Page exists with Summary + gaps identified |
| **design** | 25–50% | design-document, ADR, tech-spec, type sketches IN DOCS | code-file, test-file | Spec reviewed; no code yet |
| **scaffold** | 50–80% | type-definition, schema, test-stub, config-file | implementation, real test assertions | Types compile, no business logic |
| **implement** | 80–95% | implementation, integration-wiring, config | new test files | Code compiles, lint passes, ≥1 existing file imports new code |
| **test** | 95–100% | test-implementation, test-results | new features, scope changes | 0 test failures, health check clean |

**Rules:**
- "Continue" = advance within CURRENT stage. NEVER skip ahead.
- One commit per stage. Don't advance without the stage's quality gate passing.
- Stage boundaries are ALLOWED/FORBIDDEN, not suggestions (OpenArms Bug 5: scaffold produced 135 lines of business logic — boundary now hard).

## 9 Methodology Models

| task_type / context | Model | Stages | Selected when |
|---|---|---|---|
| `epic` / `module` | **feature-development** | document → design → scaffold → implement → test | Solution not yet known; design required. Default for complex work. |
| `bug` | **bug-fix** | document → implement → test | Restore correct behavior; no new architecture. No design stage by design. |
| `research` / `spike` | **research** | document → design (cap 50%) | Investigation without implementation. 50% IS completion. |
| `docs` | **documentation** | document only | Single-stage; done when page passes quality gates. |
| `refactor` | **refactor** | document → scaffold → implement → test | Restructure without behavior change. Skips design — target defined in document. |
| (urgent + known) | **hotfix** | implement → test | Quality tier: pyramid. Deliberate compression. Problem and solution already understood. |
| (wire existing) | **integration** | scaffold → implement → test | Bridge pattern. ~$1.20/task vs $9.07 for feature-dev (OpenArms T116/T117 evidence). |
| `evolve` | **knowledge-evolution** | document → implement | Distill higher-layer pages from existing wiki knowledge. |
| project-level | **project-lifecycle (SFIF)** | scaffold → foundation → infrastructure → features | Macro-level. Other models nest inside its stages. |

**Selection conditions** (multi-dimensional):
- `task_type` (primary)
- `novelty` (known pattern → integration; unknown → feature-development) — **86.8% cost reduction by right-sizing** (OpenArms 2026-04-16 evidence)
- Project phase (POC → Production)
- Domain (knowledge / code / infra)
- Scale (single function vs new subsystem)
- Urgency (critical → hotfix model)

Full engine: [wiki/config/methodology.yaml](wiki/config/methodology.yaml).

## Page Schema Essentials

### Required Frontmatter (9 fields, every page)
`title` · `type` · `domain` · `status` · `confidence` · `created` · `updated` · `sources` · `tags`

### 19 Page Types
**Knowledge layer:** `concept`, `source-synthesis`, `comparison`, `reference`, `deep-dive`, `index`
**Evolved layer:** `lesson`, `pattern`, `decision`, `principle`
**Navigation layer:** `domain-overview`, `learning-path`, `evolution`
**Backlog layer:** `epic`, `module`, `task`, `note`, `milestone`, `operations-plan`

### 17 Relationship Verbs (ALL_CAPS)
`BUILDS ON` · `ENABLES` · `COMPARES TO` · `CONTRADICTS` · `USED BY` · `RELATES TO` · `FEEDS INTO` · `DERIVED FROM` · `SUPERSEDES` · `IMPLEMENTS` · `EXTENDS` · `CONSTRAINS` · `CONSTRAINED BY` · `PARALLELS` · `SYNTHESIZES` · `ENABLED BY` · `CONTRASTS WITH`

### Source Provenance
Every `sources` entry has `id` + `type` + at least one of (`url`, `file`, `project`+`path`).

### Maturity Lifecycle (no auto-promotion; human confirms)
`seed` (auto-generated/scaffolded) → `growing` (reviewed) → `mature` (cross-referenced 30+ days) → `canonical` (authoritative)

### Status Lifecycle
- **Knowledge pages:** `raw` → `processing` → `synthesized` → `verified` → `stale`
- **Backlog items:** `draft` → `active` → `in-progress` → `review` → `done` → `archived` / `blocked`

## 3 Artifact Classes (every output belongs to one)

| Class | Purpose | Quality rule | Examples |
|---|---|---|---|
| **document** | Constrains future work — binding | Must be binding (read as instructions, not suggestions) | requirements-spec, ADR, tech-spec, decision, principle, milestone, epic, task |
| **artifact** | By-product of work | Must exist + pass gate command (structural validity) | source-code, test-results, git-commits, deployment-packages |
| **documentation** | Explanatory for users / maintainers | Must be accurate + useful | concept, source-synthesis, lesson, pattern, domain-overview |

## Quality Gates (must pass `pipeline post`)

1. Complete frontmatter per `wiki-schema.yaml`
2. All required sections for the page type present (per `artifact-types.yaml`)
3. Summary ≥30 words
4. ≥1 relationship (unless first page in new domain)
5. Title field matches `# Heading`
6. Domain field matches folder path
7. Source provenance (URL or file or project+path)
8. No >70% concept overlap with existing pages (update instead of create)
9. Source-synthesis pages: ≥0.25 line ratio to raw source

## 3 Quality Tiers (explicit choice — never accidental)

- **Skyscraper** — full process, every stage, every gate, every artifact. Default for epics + new subsystems.
- **Pyramid** — deliberate compression with documented reasoning. Hotfix is by definition pyramid.
- **Mountain** — accidental chaos. NEVER choose. The anti-pattern. Skip = aware, document why = pyramid; skip silently = mountain.

## 3 Lines of Defense (compliance architecture)

1. **Prevention** — hooks block forbidden actions before execution. ~100% on stage boundaries.
2. **Detection** — validators / linters / health checks find violations after they happen.
3. **Correction** — methodology evolution; failures become lessons → patterns → principles.

## Methodology Engine Configs

| File | What it defines |
|---|---|
| [wiki/config/methodology.yaml](wiki/config/methodology.yaml) | 9 models, 5 stages, ALLOWED/FORBIDDEN, gates, end conditions, modes, quality tiers, composition rules |
| [wiki/config/artifact-types.yaml](wiki/config/artifact-types.yaml) | 17+ page types with content thresholds, styling directives, verification methods, methodology templates |
| [wiki/config/wiki-schema.yaml](wiki/config/wiki-schema.yaml) | Frontmatter schema, required sections per type, relationship verbs, source rules |
| [wiki/config/templates/](wiki/config/templates/) | Page templates (lesson, pattern, decision, etc.) + methodology subtemplates (requirements-spec, ADR, tech-spec, gap-analysis, etc.) |
| [wiki/config/sdlc-profiles/](wiki/config/sdlc-profiles/) | Simplified / Default / Full profiles |
| [wiki/config/domain-profiles/](wiki/config/domain-profiles/) | Per-domain overrides (path patterns, gate commands) |

## Cross-references

- Super-model + 16 named models: [wiki/spine/super-model/super-model.md](wiki/spine/super-model/super-model.md), [wiki/spine/references/model-registry.md](wiki/spine/references/model-registry.md)
- Foundation models in detail: [wiki/spine/models/foundation/](wiki/spine/models/foundation/)
- Methodology system map: [wiki/domains/cross-domain/methodology-system-map.md](wiki/domains/cross-domain/methodology-system-map.md)
- 4 Principles: [wiki/lessons/04_principles/hypothesis/](wiki/lessons/04_principles/hypothesis/)
- Goldilocks identity protocol: [wiki/domains/cross-domain/project-self-identification-protocol.md](wiki/domains/cross-domain/project-self-identification-protocol.md)
- Routing for operator intents: [.claude/rules/routing.md](.claude/rules/routing.md)
