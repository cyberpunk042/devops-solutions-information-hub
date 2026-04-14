# CONTEXT.md — Project Identity, Phase, and Constraints

> This file is the identity and constraint surface for the DevOps Solutions Research Wiki.
> Audience: any human or AI agent trying to understand the project's current state, scope, and limits.
> For architecture and data flow, see [ARCHITECTURE.md](ARCHITECTURE.md).
> For Claude-specific methodology enforcement, see [CLAUDE.md](CLAUDE.md).
> For universal cross-tool context, see [AGENTS.md](AGENTS.md).

---

## 1. Project Identity — Goldilocks Profile

> [!info] Goldilocks: Right Scale × Right Phase × Right Trust
>
> These 9 dimensions determine which SDLC profile applies, how strict enforcement
> should be, and how much autonomy is delegated to AI. They are not aspirational —
> they reflect the actual operational reality of this project today.

| Dimension | Value | Why It Matters |
|-----------|-------|---------------|
| **Type** | system (framework + instance + second brain) | It IS the methodology engine AND uses it on itself — self-referential |
| **Execution Mode** | solo — human + Claude in conversation, no harness | No automated loop; every action is human-supervised in session |
| **Domain** | knowledge (Python/wiki tools) | Not a web app or API; the artifact IS structured knowledge |
| **Phase** | production | Used daily, blocking real decisions, must not break |
| **Scale** | medium (316+ pages, growing) | Dense enough for LightRAG; too large for manual maintenance |
| **PM Level** | L1 (wiki backlog + CLAUDE.md directives) | Operator drives priorities; AI executes within stage gates |
| **Trust Tier** | operator-supervised | AI has high autonomy within stages; 99→100% transitions require human review |
| **SDLC Profile** | Default (stage-gated with selected artifacts) | Not simplified (no POC shortcuts); not full (no fleet immune system yet) |
| **Second Brain** | IS the second brain (self-referential) | The wiki documents its own methodology; AI consults it before acting |

SDLC profile full definition: `wiki/config/sdlc-profiles/default.yaml`
Identity protocol: `wiki/domains/cross-domain/project-self-identification-protocol.md`

---

## 2. Current State

> [!success] Production Health — April 2026
>
> 0 validation errors. 0 lint issues. Daily use in active research.

| Metric | Value |
|--------|-------|
| **Pages** | 316 |
| **Relationships** | 2074 |
| **Validation errors** | 0 |
| **Lint issues** | 0 |
| **Named models** | 16 (+ 9 methodology models) |
| **Standards pages** | 22 (all have annotated exemplars) |
| **Sub-super-models** | 5 |
| **Validated lessons** | 40+ |
| **Validated patterns** | 16+ |
| **Validated decisions** | 16+ |
| **Principles** | 3 |
| **Ecosystem project profiles** | 5 |

### The Three Validated Principles

These govern all agent behavior and wiki design. Derived from ≥3 independent evidence sources:

1. **Infrastructure Over Instructions** — hooks and validators achieve ~100% compliance; CLAUDE.md rules alone achieve ~25%. Enforce through tooling.
2. **Structured Context Governs Agent Behavior More Than Content** — markdown structure (tables, headers, callouts, YAML) programs agent behavior 2-3× more effectively than equivalent prose.
3. **Right Process for Right Context (Goldilocks)** — methodology depth must adapt to phase × scale × trust. POC + micro = simplified profile. Production + large + fleet = full profile with immune system.

Principles folder: `wiki/lessons/04_principles/`

---

## 3. Active Epic Portfolio

Current milestone: **Second Brain Complete System — v2.0**
Target date: 2026-05-15
Milestone page: `wiki/backlog/milestones/second-brain-complete-system-v2-0.md`

### In Progress (stage: implement, readiness 70–80%)

| Epic | Title | Priority | Progress |
|------|-------|----------|----------|
| E010 | Model Updates — All 16 Models Reflect Current Knowledge | P0 | 75% |
| E011 | Standards Exemplification — All 15 Per-Type Standards with Inline Annotated Exemplars | P0 | 80% |
| E012 | Template Enrichment — Rich Proto-Programming Examples | P0 | 70% |
| E014 | Goldilocks Navigable System — Identity to Action in Continuous Flow | P0 | 60% |
| E015 | Gateway Tools Completion — All Requirements Implemented with MCP Integration | P1 | 65% |
| E017 | Context Engineering Framework — Formalized as Model with Standards | P1 | 75% |
| E021 | New Source Ingestion — 10–15 Sources Through Full Pipeline | P1 | 75% |

### Draft / Early Stage (readiness 5–40%)

| Epic | Title | Priority | Stage |
|------|-------|----------|-------|
| E013 | Super-Model Evolution — v2.0 with Sub-Super-Models | P0 | document (75% done) |
| E016 | Integration Chain Proof — End to End with OpenArms | P1 | document (20% done) |
| E018 | Global Standards Implementation — Actual Adherence Not Just Reference | P2 | document (0% done) |
| E019 | Obsidian Navigation — Complete Browse Experience with Folder Cleanup | P1 | document (30% done) |
| E020 | Knowledge Sweep — Global Quality Confirmation by Human Review | P2 | document (0% done) |

All epics: `wiki/backlog/epics/milestone-v2/`

---

## 4. Operator Context

> [!note] Who runs this system
>
> Single human operator. DevOps engineer. Operates at ecosystem scale — not project scale.

**Profile:**
- DevOps engineer running a 5-project ecosystem
- Thinks at scale: decisions made here affect all downstream projects
- Expects full tool capabilities used proactively, not described
- Daily use pattern: research + synthesis + methodology refinement

**The 5-Project Ecosystem:**

| Project | Role | Relationship to Wiki |
|---------|------|---------------------|
| **Research Wiki** (this) | Central intelligence hub | IS the second brain |
| **OpenArms** | Harness engineering; advanced agent runtime | Feeds operational lessons back; uses wiki methodology |
| **OpenFleet** | Agent fleet orchestrator | Consumes wiki as LightRAG knowledge source |
| **AICP** | Local-AI complexity-routed inference ($0 target) | Implements patterns documented in wiki |
| **devops-control-plane** | Infrastructure governance | Uses wiki's methodology for decision tracking |

**Hardware:**
- Platform: WSL2 on Windows
- VRAM: 8GB currently (19GB upgrade planned — unlocks Subsystem 3: local inference)
- Obsidian vault: Windows-side, auto-synced via `tools/sync.py`

**Communication style:**
- Directive-first: operator states intent, AI executes
- Verbatim logging is required: operator directives logged in `raw/notes/` before action
- "Fix it at the root" — blockers solved with tooling, never handed back manually

---

## 5. Constraints

> [!warning] These are hard constraints, not preferences
>
> Violating these creates real failures — broken methodology, lost provenance,
> inconsistent state. They are enforced by tooling, not just by instruction.

### Non-Negotiable Constraints

**No manual infrastructure.** All operational patterns must be expressed as reproducible tooling. Never create systemd units, cron jobs, or infrastructure by hand. If you need automation, build it into `tools/` or `skills/`.

**No hardcoded solutions.** Build frameworks, not instances. A config file with specific values is not a framework — it is an instance. The wiki must teach the meta-level pattern, not just record a single example.

**Verbatim directive logging.** Every operator directive is logged verbatim in `raw/notes/` BEFORE acting. This is core methodology — proactive, not reactive. Paraphrasing is forbidden.

**Quality gates are blocking, not advisory.** `pipeline post` must return 0 errors before any commit. Validation errors block completion. Lint issues block completion. "Done" requires evidence.

**Stage gates are enforced.** No code during document/design. No feature additions during test. Readiness tracks definition; progress tracks execution. They move independently.

**Depth before synthesis.** A README is not understanding. When ingesting a format or tool, you must read a real INSTANCE — not just the description. Source DESCRIBES a thing → you MUST read that thing.

### Quality Thresholds

| Artifact | Minimum Size |
|----------|-------------|
| Wiki pages (general) | 150 lines minimum |
| Standards pages | 300+ lines |
| Real documentation pages | 500+ lines |
| Summary section | 30 words minimum |
| Relationships | 1 minimum per page |

Per-type thresholds: `wiki/config/artifact-types.yaml`

---

## 6. Phase Trajectory

### Where We Started

- **First commits:** ~April 5, 2026 (9 days ago relative to current date)
- **Initial scope:** Research ingestion + basic wiki structure
- **First milestone:** Knowledge framework established (100+ pages)

### Current Phase: Production Consolidation

- Phase: Production (in daily use, blocking real decisions)
- Active milestone: Second Brain Complete System v2.0 (12 epics)
- Focus: System-level integration — not more pages, but making the whole navigable, proven, and exemplified
- Operator directive: *"This is not incremental improvement — it's the system-level integration that makes the whole greater than the parts."*

### Next Phase: External Validation

- E016: Integration Chain Proof — end-to-end with OpenArms (first external consumer)
- When E016 ships: the wiki transitions from self-contained to ecosystem-integrated
- What that unlocks: OpenFleet LightRAG ingestion, AICP pattern consumption, devops-control-plane methodology adoption
- Hardware milestone: 19GB VRAM → Subsystem 3 (local inference, $0 target validation)

---

## 7. What This Is NOT

> [!caution] Common misreadings of this project

**Not a static documentation project.** Every page is a living artifact. Sources drive model updates. Lessons promote through maturity stages. Decisions accumulate evidence. Nothing here is "write once, read forever."

**Not a collection of tutorials.** The wiki synthesizes — it does not reproduce source material. A source-synthesis page is not a summary; it is a cross-referenced insight extraction with relationship mapping.

**Not a replacement for live experimentation.** The wiki DOCUMENTS lessons from experimentation. The actual experiments happen in OpenArms, OpenFleet, AICP. Knowledge flows back here after validation.

**Not a closed system.** It is explicitly designed for bi-directional contribution. Sister projects consume via gateway and export; they contribute back via `gateway contribute`. External agents can write lessons into `wiki/lessons/00_inbox/` via the MCP server.

**Not a one-shot sprint.** The operator has explicitly planned for 20+ epics across multiple months. The wiki grows continuously through the knowledge evolution pipeline, not through periodic big-bang additions.

---

## 8. Key Reference Pages

| What you need | Where to look |
|---------------|--------------|
| All 16 models with status | `wiki/spine/references/model-registry.md` |
| System topology (super-model) | `wiki/spine/super-model/super-model.md` |
| Methodology stage gates | `wiki/spine/models/foundation/model-methodology.md` |
| Knowledge architecture | `wiki/spine/super-model/knowledge-architecture.md` |
| Goldilocks protocol | `wiki/spine/super-model/goldilocks-protocol.md` |
| Enforcement hierarchy | `wiki/spine/super-model/enforcement-hierarchy.md` |
| Integration & ecosystem | `wiki/spine/super-model/integration-ecosystem.md` |
| Gateway tools reference | `wiki/spine/references/gateway-tools-reference.md` |
| Second brain integration chain | `wiki/spine/references/second-brain-integration-chain.md` |
| Artifact taxonomy (78 types) | `wiki/domains/cross-domain/methodology-artifacts/categories/methodology-artifact-taxonomy.md` |

---

*Last updated: 2026-04-14. Source of truth for all metrics: `python3 -m tools.pipeline status`*
