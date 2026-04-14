# wiki/config/ — Configuration Reference

This directory contains the **machine-readable definitions** that drive the entire research
wiki system. Config here is not documentation (that lives in `wiki/`), and it is not code
(that lives in `tools/`). It is the **schema, methodology, domain overrides, and policy
definitions** that both agents and tools read at runtime.

Every tool in `tools/`, every skill in `skills/`, and every agent directive in
`wiki/config/agent-directive.md` derives its behavior from files in this directory.
Changing a value here changes the system's behavior everywhere that file is consumed.

---

## The 4-Layer Configuration Architecture

Configs compose in layers. Lower layers define universals; higher layers narrow to
specifics. When two layers disagree, the higher-numbered layer wins at runtime.

```
Layer 0 — Schema / Catalog
  wiki-schema.yaml         ← required fields, enums, valid section names, relationship verbs
  artifact-types.yaml      ← 78 artifact types, content thresholds, callout maps
  domains.yaml             ← domain registry (which domains exist and what they mean)
  quality-standards.yaml   ← numeric quality thresholds for linting and export

Layer 1 — Methodology Definitions
  methodology.yaml         ← 9 named models, 5 stages, chains, quality tiers, end conditions

Layer 2 — Methodology Profiles
  methodology-profiles/    ← execution STYLE (which artifacts emphasized, stage weights)
    stage-gated.yaml       ← balanced 5-stage — the Goldilocks default
    (spec-driven, agile-ai, test-driven — to be added)

Layer 3 — Domain Profiles
  domain-profiles/         ← RESOLUTION — concrete paths and gate commands per stack
    infrastructure.yaml
    python-wiki.yaml
    typescript.yaml

Layer 4 — SDLC Profiles
  sdlc-profiles/           ← PROJECT-LEVEL POLICY — how much methodology a project needs
    simplified.yaml
    default.yaml
    full.yaml
```

**Composition diagram:**

```
wiki-schema.yaml  +  artifact-types.yaml
        ↓
  methodology.yaml  (models reference artifact categories from artifact-types)
        ↓
  methodology-profiles/  (style — which artifacts emphasized for this project type)
        ↓
  domain-profiles/  (resolution — how artifact categories map to real paths + commands)
        ↓
  sdlc-profiles/  (policy — enforcement level, stage gate strictness, tracking requirements)
        ↓
  CLAUDE.md / agent-directive.md  (project override — always highest priority)
```

Override precedence at runtime: `CLAUDE.md` > `sdlc-profile` > `methodology-profile` >
`domain-profile` > `methodology.yaml` > `artifact-types.yaml` + `wiki-schema.yaml`.

---

## File-by-File Reference

---

### `wiki-schema.yaml` — Page Type Schema

**Purpose:** Defines the valid structure of every wiki page's YAML frontmatter.

**What it contains:** Nine sections that together specify what a valid page looks like:
- `required_fields` — the 9 frontmatter keys every page must have (`title`, `type`, `domain`,
  `status`, `confidence`, `created`, `updated`, `sources`, `tags`)
- `optional_fields` — 30+ additional frontmatter keys available for specific types (`readiness`,
  `progress`, `maturity`, `reversibility`, `impediment_type`, `depends_on`, etc.)
- `enums` — valid values for every enumerated field: 19 page types, 11 statuses, 4 confidence
  levels, 5 complexity levels, 4 maturity levels, 8 task types, 8 stages, 8 impediment types
- `required_sections` — per-type section structure (e.g., `concept` requires Summary, Key
  Insights, Deep Analysis, Relationships; `lesson` requires Summary, Context, Insight, Evidence,
  Applicability, Relationships)
- `relationship_verbs` — 17 valid ALL_CAPS relationship verbs (BUILDS ON, ENABLES, COMPARES TO,
  CONTRADICTS, FEEDS INTO, DERIVED FROM, SUPERSEDES, etc.)

**Consumed by:** `tools/validate.py` (schema validation), `tools/pipeline.py` (post-chain
validation step 3), `tools/gateway.py` (field queries via `--field`), `tools/lint.py`
(section checking).

**Overrides / Layered on by:** `artifact-types.yaml` adds `required_frontmatter` extensions
per type (e.g., `decision` requires `reversibility`, `principle` requires `derived_from`).
Domain profiles may add stage-specific frontmatter conventions.

**Example snippet:**
```yaml
required_fields:
  - title
  - type
  - domain
  - status
  - confidence
  - created
  - updated
  - sources
  - tags

enums:
  type:
    - concept
    - source-synthesis
    - comparison
    - lesson
    - pattern
    - decision
    - epic
    - task
    # ... 11 more

required_sections:
  lesson:
    - Summary
    - Context
    - Insight
    - Evidence
    - Applicability
    - Relationships
```

**Related wiki pages:** [[frontmatter-field-reference|Frontmatter Field Reference]],
[[e003-artifact-type-system|E003 Artifact Type System]]

**Modification notes:** Update when adding a new page type (add to `enums.type`, add a
`required_sections` entry), a new valid status, a new relationship verb, or a new optional
frontmatter field. Any change here immediately affects validation — run `python3 -m tools.pipeline post`
after editing. The operator should approve changes that remove valid values (breaking change).

---

### `artifact-types.yaml` — 78 Artifact Types Across 11 Categories

**Purpose:** Extends `wiki-schema.yaml` with content thresholds, styling requirements,
verification methods, and template references for every wiki page type.

**What it contains:**
- `categories` — 5 categories: knowledge-pages (concept, comparison, deep-dive, reference,
  source-synthesis), evolved-pages (lesson, pattern, decision, principle), navigation-pages
  (domain-overview, evolution, learning-path, index), backlog-pages (milestone, epic, module,
  task, note), methodology-documents (operations-plan)
- `artifact_classes` — the 3 fundamental output classes: `document` (binding, constrains future
  work), `artifact` (tangible by-product), `documentation` (explanatory)
- `types` — per-type definitions with `content_thresholds`, `styling` (callouts required/
  recommended, callout maps), `verification`, and `required_frontmatter` extensions
- `methodology_templates` — 6 specialized templates (requirements-spec, infrastructure-analysis,
  gap-analysis, design-plan, tech-spec, test-plan) that use existing wiki types but with
  methodology-specific structure; scaffolded via `pipeline scaffold methodology/<name> "Title"`
- `stage_artifacts` — generic artifact categories (wiki-page, type-definition, implementation,
  test-stub, etc.) used by methodology.yaml chain definitions; domain profiles resolve these
  to concrete paths and gate commands

**Consumed by:** `tools/validate.py` (content threshold checking), `tools/lint.py`
(callout advisory checks), `tools/pipeline.py scaffold` (template selection),
`tools/gateway.py` (artifact type queries).

**Overrides / Layered on by:** Domain profiles override `stage_artifacts` resolution
(the `domain_resolved: true` flag on artifacts means path and gate come from the domain profile,
not here). Methodology profiles may emphasize or deprioritize specific artifact types.

**Example snippet:**
```yaml
types:
  lesson:
    category: evolved-pages
    artifact_class: documentation
    template: config/templates/lesson.md
    content_thresholds:
      summary_min_words: 30
      insight_min_words: 50
      min_relationships: 2
      min_evidence_items: 3
    styling:
      callouts_required: true
      callout_map:
        Insight: "[!warning] or [!tip]"
        Evidence: "[!bug]- for failures, [!success] for validated"
        Applicability: "table, optionally in [!abstract]"

  decision:
    artifact_class: document   # decisions are BINDING
    required_frontmatter:
      - reversibility
    content_thresholds:
      min_alternatives: 2
```

**Related wiki pages:** [[e003-artifact-type-system|E003 Artifact Type System]],
[[methodology-artifact-taxonomy|Methodology Artifact Taxonomy]]

**Modification notes:** Update when adding a new page type (add type definition with at
minimum `category`, `template`, `content_thresholds`, `verification`), adding a new
methodology template (add under `methodology_templates`), or adjusting quality thresholds.
Adding a type here requires a matching entry in `wiki-schema.yaml` enums and a template in
`config/templates/`.

---

### `domains.yaml` — Domain Registry

**Purpose:** Defines the canonical list of knowledge domains that wiki pages may belong to.

**What it contains:** A flat registry of domain keys with descriptions. These keys are the
valid values for the `domain` frontmatter field and determine where pages live under
`wiki/domains/`. The registry is deliberately minimal — domains grow organically and are
added here when a new knowledge area is established.

Current domains: `ai-agents`, `ai-models`, `infrastructure`, `devops`, `security`,
`knowledge-systems`, `automation`, `tools-and-platforms`.

**Consumed by:** `tools/validate.py` (validates `domain` field against registry),
`tools/pipeline.py` (gaps analysis uses domain list), `tools/stats.py` (per-domain
coverage reporting), `tools/export.py` (domain-scoped export filtering).

**Overrides / Layered on by:** Domain profiles in `domain-profiles/` map domain keys to
concrete execution rules. The `cross-domain` convention (used in `wiki/domains/cross-domain/`)
is a directory pattern, not a registry entry — it's used for methodology and multi-domain pages.

**Example snippet:**
```yaml
domains:
  ai-agents:
    description: "Multi-agent systems, orchestration, fleet management, agent memory"
  knowledge-systems:
    description: "RAG, knowledge graphs, wikis, embeddings, search, synthesis"
```

**Related wiki pages:** [[root-documentation-map|Root Documentation Map]]

**Modification notes:** Add a new entry when establishing a new knowledge domain (after
at least 2-3 pages are confirmed to belong to it). The domain key must be kebab-case,
match the folder name under `wiki/domains/`, and have a `_index.md` created alongside it.
Do not add domains speculatively — let them emerge from content.

---

### `quality-standards.yaml` — Quality Thresholds

**Purpose:** Defines the numeric quality bar for linting decisions and export eligibility.

**What it contains:** Four sections:
- `page_quality` — minimum word counts (summary: 30), relationship minimums (1),
  open questions ratio cap (0.5), stale threshold in days (30)
- `domain_health` — minimum pages per domain (3), minimum cross-domain relationships (2)
- `export_readiness` — minimum confidence (`medium`), minimum status (`synthesized`),
  require source provenance (`true`)
- `duplicate_detection` — similarity threshold (0.70) above which pages are flagged
  as potential duplicates

**Consumed by:** `tools/lint.py` (page quality checks), `tools/export.py` (export
eligibility filtering), `tools/pipeline.py gaps` (domain health analysis).

**Overrides / Layered on by:** `artifact-types.yaml` overrides per-type thresholds —
the values in `quality-standards.yaml` are defaults for types that don't specify their
own. Export profiles in `export-profiles.yaml` also set their own `min_confidence` and
`min_status` per export target (which may be stricter or looser than the global default).

**Example snippet:**
```yaml
page_quality:
  min_summary_words: 30
  min_relationships: 1
  stale_threshold_days: 30

export_readiness:
  min_confidence: medium
  min_status: synthesized
  require_source_provenance: true

duplicate_detection:
  similarity_threshold: 0.70
```

**Related wiki pages:** [[e003-artifact-type-system|E003 Artifact Type System]]

**Modification notes:** Raising thresholds here increases the quality bar across the
entire wiki. Lower values allow more pages through export. The `stale_threshold_days`
value is worth reviewing as the wiki matures — 30 days may be aggressive for stable
reference pages vs. research pages that should stay fresh.

---

### `export-profiles.yaml` — Sister Project Export Definitions

**Purpose:** Defines how to transform and filter wiki knowledge for export to each
sister project.

**What it contains:** Three named profiles:
- `openfleet` — exports for LightRAG ingestion via `kb_sync.py`; strips frontmatter,
  maps wiki types to openfleet-kb types (concept → "Research"), adds metadata headers,
  filters to `min_confidence: medium` + `min_status: synthesized`
- `aicp` — exports for LocalAI Collections KB; converts frontmatter to markdown headers,
  maps types and statuses to AICP vocabulary, restricts to infrastructure/devops/ai domains
- `methodology` — bundles the methodology engine configs (methodology.yaml,
  artifact-types.yaml, domain profiles, wiki-schema.yaml) plus companion wiki pages
  for consumer projects to adopt the methodology system

**Consumed by:** `tools/export.py` when invoked as `python3 -m tools.export openfleet`,
`python3 -m tools.export aicp`, or `python3 -m tools.export methodology`.

**Overrides / Layered on by:** Nothing overrides export profiles — they are standalone
per-destination configurations. However, they reference and depend on `quality-standards.yaml`
for baseline thresholds which they can tighten but not loosen per destination.

**Example snippet:**
```yaml
openfleet:
  output_dir: ../openfleet/docs/knowledge-map/kb/research-wiki/
  transforms:
    frontmatter: strip
    type_map:
      concept: "Research"
      deep-dive: "Research Synthesis"
  filters:
    min_confidence: medium
    min_status: synthesized

methodology:
  bundle_files:
    - config/methodology.yaml
    - config/artifact-types.yaml
    - config/domain-profiles/typescript.yaml
    - config/wiki-schema.yaml
```

**Related wiki pages:** [[root-documentation-map|Root Documentation Map]]

**Modification notes:** Update `output_dir` if a sister project moves its KB location.
Update `type_map` when wiki page types are renamed or new types need to map to sister
project vocabulary. The `methodology` bundle file list must be kept current as new
domain profiles are added.

---

### `methodology.yaml` — The Methodology Engine

**Purpose:** Defines the 9 named models, 5 universal stages, artifact chains, execution
modes, quality tiers, and end conditions that govern all work in this system.

**What it contains:** Six major sections:

- `stages` — 5 universal stages with readiness ranges, allowed/forbidden outputs:
  `document` (0–25%, understanding), `design` (25–50%, decisions), `scaffold` (50–80%,
  structure), `implement` (80–95%, behavior), `test` (95–100%, proof)

- `models` — 9 named sequences, each with `stages`, `readiness_cap`, and a per-stage
  `chain` definition listing required/optional artifacts, `depends_on` relationships,
  and `gate.checks`:
  - `feature-development` — full 5-stage, solution unknown
  - `research` — document + design, produces understanding (50% = done)
  - `knowledge-evolution` — document + implement, distills lessons/patterns/decisions
  - `documentation` — document only, single page
  - `bug-fix` — document + implement + test, restore correct behavior
  - `refactor` — document + scaffold + implement + test, restructure without changing behavior
  - `hotfix` — implement + test, emergency fix (solution already known)
  - `integration` — scaffold + implement + test, wire existing modules
  - `project-lifecycle` — macro SFIF model, nested model composition

- `model_selection` — maps `task_type` to default model; includes override conditions
  for context (scale, solution_known)

- `modes` — 7 execution modes: `autonomous`, `semi-autonomous`, `document-only`,
  `design-only`, `scaffold-only`, `plan` (alias for design-only), `custom`

- `end_conditions` — 5 stop conditions: `backlog-empty`, `stage-reached`, `task-count`,
  `time-limit`, `cost-limit`

- `quality_tiers` — 3 tiers: `skyscraper` (full process), `pyramid` (documented
  compression), `mountain` (anti-pattern — never choose)

**Consumed by:** `tools/gateway.py` (model and chain queries), `tools/pipeline.py`
(stage awareness, scaffold template selection), `wiki/config/agent-directive.md`
(the autonomous agent reads this as law), all domain profiles (they override stage
definitions defined here).

**Overrides / Layered on by:** Domain profiles resolve `type-definition`, `implementation`,
`test-implementation`, etc. to concrete path patterns and gate commands. Methodology
profiles adjust artifact emphasis and stage weights. SDLC profiles determine which models
are available and how strictly gates are enforced.

**Example snippet:**
```yaml
stages:
  document:
    description: "Understand the problem. Map what exists. Identify gaps."
    readiness_range: [0, 25]
    allowed_outputs: [wiki-page]
    forbidden_outputs: [code-file, test-file]

models:
  feature-development:
    stages: [document, design, scaffold, implement, test]
    chain:
      scaffold:
        required:
          - artifact: type-definition
            count: "1+"
            depends_on: [design.design-document]
          - artifact: test-stub
            count: "1+"
        forbidden: [implementation, test-implementation]
        gate:
          checks: [types-compile, no-business-logic, test-stubs-exist]

quality_tiers:
  skyscraper:
    description: "Full process. Every stage, every gate, every artifact."
  mountain:
    description: "Accidental chaos. NEVER choose this — it's the anti-pattern."
```

**Related wiki pages:** [[model-methodology|Model — Methodology]],
[[sdlc-customization-framework|SDLC Customization Framework]],
[[methodology-system-map|Methodology System Map]]

**Modification notes:** This is the most critical config file. Changes here affect every
agent that reads it. Adding a new model requires: model definition under `models`,
`model_selection` entry, and a chain with per-stage artifact requirements. Modifying an
existing stage's `allowed_outputs` or `forbidden_outputs` immediately changes what agents
can and cannot do at that stage. Version-bump the header comment when making non-trivial changes.

---

### `agent-directive.md` — Autonomous Agent Operating Procedure

**Purpose:** Defines the 14-step work loop, stage enforcement rules, git discipline, and
hard prohibition list for autonomous agents working on this wiki.

**What it contains:** Unlike YAML configs, this is a Markdown document designed to be
read by AI agents as direct operating instructions. It covers: the 14-step task execution
loop (find task → read it → determine stage → execute stage → update frontmatter → commit
→ verify → repeat), required frontmatter fields and status lifecycle, commit message format,
quality gates per stage, item hierarchy rules (epic > module > task), and 14 things the
agent must never do.

**Consumed by:** Autonomous agents operating on this wiki (invoked via the `wiki-agent`
skill or harness). It IS the agent's operating manual, not metadata about the wiki.

**Related wiki pages:** [[model-methodology|Model — Methodology]]

**Modification notes:** Update when the work loop changes, when new hard prohibitions are
discovered through operator feedback, or when frontmatter fields evolve. This is distinct
from CLAUDE.md (project directives) — agent-directive.md is the procedural how-to;
CLAUDE.md is the operator-level what and why.

---

## Subdirectories

---

### `domain-profiles/` — Per-Domain Stage Resolution

Domain profiles are the bridge between the generic model definitions in `methodology.yaml`
and the concrete toolchain of a specific project. They translate abstract artifact categories
(type-definition, test-stub, implementation) into real file paths and real gate commands.

Three profiles exist:

#### `domain-profiles/infrastructure.yaml`

**Domain:** Infrastructure as Code (Terraform, Docker, CI/CD — e.g., devops-control-plane)

**Resolves:**
- `type-definition` → `**/*.tf` (Terraform variable/output/data declarations)
- `implementation` → `**/*.tf` (resource blocks, modules)
- `test-implementation` → `tests/**/*.tf` or Terratest Go files
- Gate commands: `terraform validate` (scaffold), `terraform plan` (implement), `terraform apply`
  against test environment (test)

**Conventions section** adds infrastructure-specific norms: remote state in S3/GCS with
locking, separate tfvars per environment, module pattern (`modules/` + `environments/`),
never commit secrets.

#### `domain-profiles/python-wiki.yaml`

**Domain:** Python tool projects and knowledge wikis (e.g., this wiki itself)

**Resolves:**
- `type-definition` → `config/**/*.yaml` (schemas, configs ARE the scaffold for this domain)
- `implementation` → `tools/**/*.py` (Python with real logic) + `wiki/**/*.md` (content pages)
- `test-implementation` → `tests/**/*.py`
- Gate command for every stage: `python3 -m tools.pipeline post`
- Additional gate at implement: `python3 -m tools.validate`

Also contains a `knowledge_operations` section unique to wiki projects: ingestion pipeline
(fetch → post), evolution pipeline (evolve --score → scaffold → generate → post), curation
pipeline (post → gaps → crossref).

Includes a real example section tracing E003 Artifact Type System through all 5 stages to
show where each artifact landed.

#### `domain-profiles/typescript.yaml`

**Domain:** TypeScript/Node.js projects with pnpm toolchain (e.g., OpenArms, OpenFleet)

**Resolves:**
- `type-definition` → `src/**/*.ts`
- `test-stub` → `src/**/*.test.ts`
- `implementation` → `src/**/*.ts`
- Gate commands: `pnpm tsgo` (scaffold + implement), `pnpm check` (implement), `pnpm test -- {test_file}` (test)

**Forbidden patterns** at scaffold stage: no control flow, no function bodies > 3 lines.

Includes a `patterns` section with the `bridge-module` pattern (< 80 LOC adapter between
new module and existing consumer — the recommended approach for the integration model).

#### Adding a new domain profile

Create `domain-profiles/<name>.yaml` with at minimum:
```yaml
domain: <name>
description: "..."
stage_overrides:
  document:
    gate_commands: []
    path_patterns:
      wiki-page: "..."
    forbidden_zones: [...]
  scaffold:
    gate_commands: [...]
    path_patterns:
      type-definition: "..."
  implement:
    gate_commands: [...]
    path_patterns:
      implementation: "..."
  test:
    gate_commands: [...]
    path_patterns:
      test-implementation: "..."
```

Then register the domain in `domains.yaml`.

---

### `sdlc-profiles/` — Project-Level Policy Profiles

SDLC profiles define HOW MUCH methodology a project needs — the enforcement level, tracking
requirements, and available models. They do NOT define how tasks are executed (that is
`methodology.yaml`). They define the governance envelope around task execution.

Three profiles exist on a spectrum from exploration to production:

#### `sdlc-profiles/simplified.yaml`

**Profile:** Minimum viable process for exploration and rapid iteration.

- **Applicability:** POC, early-MVP; micro to small scale (< 100k lines)
- **Execution mode:** Solo (human + agent in conversation, no harness)
- **Enforcement:** Advisory — CLAUDE.md rules only, no hooks, no blocking gates
- **Stage policy:** document optional, design/scaffold skip, implement+test required
- **Tracking:** readiness gate 30, no milestone tracking
- **Upgrade triggers:** agent violates stage boundaries, project moves to MVP with real users,
  codebase > 100k lines

#### `sdlc-profiles/default.yaml`

**Profile:** Stage-gated process with selected artifacts — the Goldilocks default.

- **Applicability:** MVP through staging; small to medium scale (10k–1M lines)
- **Execution mode:** Solo or harness (optional)
- **Enforcement:** Hooks recommended, stage gates enforced, compliance measured
- **Stage policy:** all stages required (design can be skipped for bug-fix/hotfix)
- **Tracking:** readiness gate 80, operator reviews completions, milestone tracking optional
- **Upgrade triggers:** first paying customer/SLA, codebase > 1M lines, compliance requirements appear

#### `sdlc-profiles/full.yaml`

**Profile:** Complete process for production systems with full enforcement and traceability.

- **Applicability:** Production/maintenance; medium to massive scale (100k–15M+ lines)
- **Execution mode:** Harness v2/v3 or full fleet orchestration (harness required)
- **Enforcement:** Full infrastructure — pre_bash, pre_write, post_write, post_compact hooks;
  /stage-complete, /task-done, /concern commands; harness owns the loop, git, and budget
- **Immune system:** Enabled (doctor cycle 30s, detects deviation/laziness/scope_creep)
- **Stage policy:** no exceptions, all stages required, artifact_depth comprehensive
- **Tracking:** readiness gate 99, adversarial review, milestones required, full hierarchy
  (milestone > epic > module > task) required
- **Downgrade rule:** NEVER silently — always a decision page documenting why and who approved

**Example snippet (`default.yaml`):**
```yaml
enforcement:
  level: hooks-optional
  stage_gates: enforced
  compliance_target: measured

tracking:
  readiness_gate: 80
  human_final_gate: true
```

**Related wiki pages:** [[sdlc-customization-framework|SDLC Customization Framework]]

---

### `methodology-profiles/` — Methodology Execution Styles

Methodology profiles define execution STYLE — which artifacts to emphasize, stage weights,
and signature practices. They sit between SDLC profiles (policy) and domain profiles
(resolution). A project can combine any SDLC profile with any methodology profile and any
domain profile independently.

Currently only one profile exists:

#### `methodology-profiles/stage-gated.yaml`

**Profile:** Balanced 5-stage execution with gates — the Goldilocks default.

This profile makes the implicit style of `methodology.yaml` explicit so it can be
selected and compared against future profiles. It defines:
- Stage emphasis weights: document 20%, design 20%, scaffold 20%, implement 25%, test 15%
- Primary artifacts per stage (e.g., requirements-spec + gap-analysis at document stage,
  type-definition + test-stub pair always at scaffold)
- Artifact preferences (preferred: integration-wiring, deprioritized: operational-runbook)
- Signature practices: gate-before-advance, forbidden-zone enforcement,
  integration-wiring requirement, iterative depth
- Compatible with all three SDLC profiles (simplified/default/full)
- Adoption notes including migration back from other profiles

**Related wiki pages:** [[model-methodology|Model — Methodology]]

Three additional profiles are planned (spec-driven, agile-ai, test-driven) and will be
added to this directory as they are defined.

---

### `templates/` — Page Scaffolds Per Type

Templates are Markdown files used by `python3 -m tools.pipeline scaffold <type> "Title"`.
Every template includes:
- YAML frontmatter with `{{title}}`, `{{date}}`, `{{domain}}` placeholders
- Required section headings per `wiki-schema.yaml`
- Inline guidance comments explaining what GOOD content looks like
- Example content showing the standard to aim for (not just instructions)

**Root-level templates (19 types):**

| Template | Type | Key sections |
|----------|------|-------------|
| `concept.md` | concept | Summary, Key Insights, Deep Analysis, Relationships |
| `source-synthesis.md` | source-synthesis | Summary, Key Insights, Relationships |
| `comparison.md` | comparison | Summary, Comparison Matrix, Key Insights, Deep Analysis, Relationships |
| `reference.md` | reference | Summary, Relationships |
| `deep-dive.md` | deep-dive | Summary, Key Insights, Deep Analysis, Relationships |
| `lesson.md` | lesson | Summary, Context, Insight, Evidence, Applicability, Relationships |
| `pattern.md` | pattern | Summary, Pattern Description, Instances, When To Apply, When Not To, Relationships |
| `decision.md` | decision | Summary, Decision, Alternatives, Rationale, Reversibility, Dependencies, Relationships |
| `principle.md` | principle | Summary, Statement, Derived From, Application, Boundaries, Relationships |
| `domain-overview.md` | domain-overview | Summary, State of Knowledge, Maturity Map, Gaps, Priorities, Key Pages, Relationships |
| `learning-path.md` | learning-path | Summary, Prerequisites, Sequence, Outcomes, Relationships |
| `evolution.md` | evolution | Summary, Timeline, Key Shifts, Current State, Relationships |
| `epic.md` | epic | Summary, Goals, Done When, Relationships (+ backlog frontmatter) |
| `module.md` | module | Summary, Goals, Done When, Relationships |
| `task.md` | task | Summary, Done When |
| `milestone.md` | milestone | Summary, Delivery Target, Epic Composition, Acceptance Criteria, Relationships |
| `operations-plan.md` | operations-plan | Summary, Prerequisites, Steps, Rollback, Completion Criteria, Relationships |
| `note.md` | note | Summary |
| `principle.md` | principle | Summary, Statement, Derived From, Application, Boundaries, Relationships |

**`templates/methodology/` — Methodology Document Templates (6 templates):**

These are specialized templates for documents produced during methodology stage execution.
They use existing wiki page types but with methodology-specific structure.

| Template | Wiki type used | Stage | Purpose |
|----------|---------------|-------|---------|
| `requirements-spec.md` | concept | document | Functional/non-functional requirements + acceptance criteria |
| `infrastructure-analysis.md` | concept | document | Mapping of existing infrastructure — files, components, data flow |
| `gap-analysis.md` | concept | document | Gap identification — current vs required, impact, complexity |
| `design-plan.md` | concept | design | Problem analysis, alternatives, trade-offs, decisions, rationale |
| `tech-spec.md` | reference | design | Component specs, API tables, interface definitions |
| `test-plan.md` | reference | design | Test strategy, test cases with IDs, inputs, expected outputs |

**Scaffold commands:**
```bash
# Regular page types
python3 -m tools.pipeline scaffold concept "My New Concept"
python3 -m tools.pipeline scaffold lesson "Lesson Title"
python3 -m tools.pipeline scaffold decision "Decision Title"

# Methodology documents (for stage-specific artifacts)
python3 -m tools.pipeline scaffold methodology/requirements-spec "E018 Requirements Spec"
python3 -m tools.pipeline scaffold methodology/gap-analysis "E018 Gap Analysis"
```

---

## How to Add a New Config

### Adding a new page type

1. Add the type to `enums.type` in `wiki-schema.yaml`
2. Add `required_sections.<type>` in `wiki-schema.yaml`
3. Add a type definition under `types` in `artifact-types.yaml` with `category`, `template`,
   `content_thresholds`, `styling`, `verification`
4. Create `config/templates/<type>.md` with frontmatter + sections + guidance comments
5. If the type has additional required frontmatter fields, add `required_frontmatter` in
   `artifact-types.yaml` (e.g., `decision` requires `reversibility`)
6. Run `python3 -m tools.pipeline post` to validate

### Adding a new artifact type (methodology template)

1. Add an entry under `methodology_templates` in `artifact-types.yaml` with `wiki_type`,
   `template`, `produced_at_stage`, `description`
2. Create `config/templates/methodology/<name>.md`
3. Optionally reference the template in `methodology.yaml` model chain `templates` lists
4. Run `python3 -m tools.pipeline post` to validate

### Adding a new domain

1. Add an entry to `domains.yaml` with the domain key and description
2. Create `wiki/domains/<domain-key>/` directory with `_index.md`
3. Create `config/domain-profiles/<domain-key>.yaml` with stage overrides
4. Optionally add the domain profile to `export-profiles.yaml` methodology bundle if needed
5. Run `python3 -m tools.pipeline post` to validate

### Adding a new SDLC profile

1. Create `config/sdlc-profiles/<name>.yaml`
2. Define: `profile`, `description`, `applicability`, `execution`, `enforcement`,
   `methodology` (available_models, stage_policy, artifact_depth), `tracking`,
   and `upgrade_to_*` / `downgrade_to_*` triggers
3. Reference the new profile in project CLAUDE.md when adopting it
4. No tools changes needed — SDLC profiles are policy, not code

### Adding a new methodology profile

1. Create `config/methodology-profiles/<name>.yaml`
2. Define: `profile`, `description`, `style`, `applicability`, `stage_emphasis` (weight
   per stage, primary_artifacts, key_gate_checks), `artifact_preferences`,
   `models`, `signature_practices`, `adoption`
3. Reference the new profile in project CLAUDE.md when adopting it

---

## Configuration Precedence at Runtime

When two configs provide conflicting guidance, the following order determines which wins
(1 = highest priority, 6 = lowest):

| Priority | Source | Scope |
|----------|--------|-------|
| 1 | `CLAUDE.md` / operator directives | Project override — always highest |
| 2 | `sdlc-profiles/<active>.yaml` | Policy — which models allowed, enforcement level |
| 3 | `methodology-profiles/<active>.yaml` | Style — artifact emphasis, stage weights |
| 4 | `domain-profiles/<stack>.yaml` | Resolution — concrete paths and gate commands |
| 5 | `methodology.yaml` | Base — universal chain definitions, model sequences |
| 6 | `artifact-types.yaml` + `wiki-schema.yaml` | Schema — foundational structure |

**Practical examples:**

- The `full` SDLC profile sets `readiness_gate: 99`. The `default` profile sets 80.
  If a project uses `full`, the gate is 99 regardless of what methodology.yaml says.
- The `typescript` domain profile sets gate command to `pnpm tsgo`. The `python-wiki`
  profile sets it to `python3 -m tools.pipeline post`. These resolve the same generic
  `gate_commands` slot from `methodology.yaml` with stack-specific commands.
- An operator directive in CLAUDE.md saying "always use smart ingestion mode" overrides
  the `autonomous` mode default in `methodology.yaml`.

---

## Related Wiki Pages

| Config | Explaining wiki page |
|--------|---------------------|
| `methodology.yaml` | [[model-methodology\|Model — Methodology]] |
| `artifact-types.yaml` | [[e003-artifact-type-system\|E003 Artifact Type System]] |
| `sdlc-profiles/` | [[sdlc-customization-framework\|SDLC Customization Framework]] |
| `wiki-schema.yaml` | [[frontmatter-field-reference\|Frontmatter Field Reference]] |
| Root configs architecture | [[root-documentation-map\|Root Documentation Map]] |
| All methodology models | `wiki/spine/models/foundation/model-methodology.md` |
| System map | `wiki/spine/references/methodology-system-map.md` |
| Domain chains | `wiki/domains/cross-domain/methodology-artifacts/chains/` |

---

## Validation

All configs are consumed by tools that validate them implicitly. To verify your changes:

```bash
# Full 6-step chain — the standard post-change check
python3 -m tools.pipeline post

# Schema validation only (checks wiki pages against wiki-schema.yaml)
python3 -m tools.validate

# Lint check with summary
python3 -m tools.lint --summary

# Query specific config sections via gateway
python3 -m tools.gateway query --models
python3 -m tools.gateway query --model feature-development --full-chain
python3 -m tools.gateway query --field readiness
python3 -m tools.gateway query --chains
```

YAML files should load without parse errors and be internally consistent (e.g., templates
referenced in `artifact-types.yaml` must exist in `config/templates/`; domains referenced
in export profiles must exist in `domains.yaml`).

---

## Current State (snapshot — 2026-04-14)

| Category | Count | Files |
|----------|-------|-------|
| Root-level YAMLs | 6 | wiki-schema, artifact-types, domains, quality-standards, export-profiles, methodology |
| Additional root | 1 | agent-directive.md |
| Domain profiles | 3 | infrastructure, python-wiki, typescript |
| SDLC profiles | 3 | simplified, default, full |
| Methodology profiles | 1 | stage-gated (spec-driven, agile-ai, test-driven pending) |
| Root templates | 19 | concept, source-synthesis, comparison, reference, deep-dive, lesson, pattern, decision, principle, domain-overview, learning-path, evolution, epic, module, task, milestone, operations-plan, note, + 1 duplicate |
| Methodology templates | 6 | requirements-spec, infrastructure-analysis, gap-analysis, design-plan, tech-spec, test-plan |

Total: 39 config files defining every rule, standard, type, threshold, gate, and convention
the wiki system enforces.
