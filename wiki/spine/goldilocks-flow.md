---
title: Goldilocks Flow — From Identity to Action
aliases:
  - "Goldilocks Flow — From Identity to Action"
type: reference
domain: cross-domain
layer: spine
status: synthesized
confidence: high
maturity: growing
created: 2026-04-12
updated: 2026-04-13
sources:
  - id: goldilocks-protocol
    type: wiki
    file: wiki/domains/cross-domain/project-self-identification-protocol.md
  - id: operator-directive
    type: directive
    file: raw/notes/2026-04-12-goldilocks-higher-ground-directive.md
tags: [goldilocks, flow, navigation, identity, routing, reference]
---

# Goldilocks Flow — From Identity to Action

> [!tip] This Is the Flow You FOLLOW — Not a Page You READ
>
> Start at Step 1. Each step tells you what to decide, what the default is, how to override, and where to go next. Works from CLI (`gateway`), Obsidian (follow wikilinks), or MCP (tool calls).
>
> **CLI shortcut:** `python3 -m tools.gateway what-do-i-need` runs Steps 1-3 automatically.

## Summary

The complete decision flow from "who am I?" to "what do I do next?" — every decision point with criteria, defaults, alternatives, and override instructions. Follow this flow once to configure your project. Return to any step when your context changes (phase upgrade, scale growth, new team members).

## Reference Content

### Step 1: DETECT — What Can Be Seen?

> [!info] Auto-Detectable (the gateway reads your project)
>
> | Dimension | How Detected | Override |
> |-----------|-------------|---------|
> | **Domain** | package.json → typescript. pyproject.toml → python. main.tf → infrastructure. wiki/config/ → knowledge. | `--domain <value>` |
> | **Scale** | Source file count. <50=micro, <500=small, <5000=medium, <20000=large, 20000+=massive. | Declare in CLAUDE.md |
> | **Phase** | CI present + tests + Docker → production. Tests only → mvp. Neither → poc. | Declare in CLAUDE.md |
> | **Second brain** | wiki/config/methodology.yaml + manifest.json → self. Sibling dir found → connected. | `--brain <path>` |

> [!warning] NOT Auto-Detectable (you must declare these)
>
> | Dimension | Why It Can't Be Detected | How to Declare |
> |-----------|------------------------|---------------|
> | **Execution mode** | The harness decides its own version at RUNTIME — project files can't know. | Add to CLAUDE.md Identity Profile or pass at launch. |
> | **PM level** | Infrastructure may exist but not be active. | Declare based on what you actually USE. |
> | **Trust tier** | Requires operational data (approval rates) or operator judgment. | Declare in CLAUDE.md or let fleet data decide. |

**CLI:** `python3 -m tools.gateway what-do-i-need` → shows detected + "unknown — declare"

**Next:** → Step 2

---

### Step 2: DECLARE — Complete Your Identity Profile

Add to your CLAUDE.md:

```yaml
## Identity Profile (Goldilocks)

| Dimension | Value |
|-----------|-------|
| **Type** | {{system / project / library}} |
| **Execution Mode** | {{solo / harness v1 / harness v2 / harness v3 / full system}} |
| **Domain** | {{auto-detected or declared}} |
| **Phase** | {{poc / mvp / staging / production}} |
| **Scale** | {{auto-detected or declared}} |
| **PM Level** | {{L1 / L2 / L3}} |
| **Trust Tier** | {{operator-supervised / trainee / standard / expert}} |
| **SDLC Profile** | {{determined in Step 3}} |
| **Second Brain** | {{self / connected / none}} |
```

**Verify:** `python3 -m tools.gateway query --identity` → shows your declared profile

**Next:** → Step 3

---

### Step 3: SELECT PROFILE — How Much Process?

> [!abstract] SDLC Profile Selection Matrix
>
> | Your Phase + Scale | Recommended Profile | Readiness Gate | Enforcement |
> |-------------------|-------------------|---------------|-------------|
> | POC + micro/small | **Simplified** | 30 | Advisory (CLAUDE.md only) |
> | MVP + small/medium | **Default** | 80 | Hooks optional |
> | Staging + medium | **Default → Full** | 80-99 | Hooks + commands |
> | Production + medium/large | **Full** | 99 | Full infrastructure |
> | Production + massive | **Full** | 99 | Full + immune system |
> | Any + fleet | **Full** | 99 | Full system |

**CLI:** `python3 -m tools.gateway query --profiles` → list all three | `query --profile default` → details

**Override:** You can use a lighter profile than recommended if you document why (Decision page).
**Upgrade triggers:** See the profile config for when to upgrade (`wiki/config/sdlc-profiles/`).

**Next:** → Step 4

---

### Step 4: SELECT MODEL — What Kind of Work?

> [!abstract] Model Selection by Task Type
>
> | Task Type | Model | Stages |
> |-----------|-------|--------|
> | New feature, solution unknown | **feature-development** | document → design → scaffold → implement → test |
> | Research, investigation | **research** | document → design (caps at 50%) |
> | Bug fix | **bug-fix** | document → implement → test |
> | Emergency, solution known | **hotfix** | implement → test |
> | Refactoring | **refactor** | document → scaffold → implement → test |
> | Integration, wiring | **integration** | scaffold → implement → test |
> | Wiki/docs only | **documentation** | document |
> | Evolve lessons/patterns | **knowledge-evolution** | document → implement |

**CLI:** `python3 -m tools.gateway query --models` → list all | `query --model feature-development --full-chain` → artifacts per stage

**Next:** → Step 5

---

### Step 5: ENTER STAGE — What Does This Stage Need?

> [!info] The 5 Universal Stages
>
> | Stage | Readiness Range | What You Produce | What's Forbidden |
> |-------|----------------|-----------------|-----------------|
> | **Document** | 0-25% | Wiki pages, research, requirements | Code, tests, configs |
> | **Design** | 25-50% | Design docs, decisions, tech specs | Code, tests |
> | **Scaffold** | 50-80% | Types, stubs, schemas (≤3 lines per body) | Business logic, test assertions |
> | **Implement** | 80-95% | Business logic, wired into runtime | Test files |
> | **Test** | 95-100% | Real assertions, verification | New features, scope changes |

**CLI:** `python3 -m tools.gateway query --stage document` → rules for that stage | add `--domain typescript` → domain-specific overrides

**Templates:** `python3 -m tools.gateway template methodology/requirements-spec` → get the template for this stage's artifact

**Next:** → Step 6

---

### Step 6: PRODUCE — Follow the Artifact Chain

For your model + stage, produce the required artifacts:

**CLI:** `python3 -m tools.gateway query --model feature-development --full-chain` → shows what every stage needs

For each artifact:
1. Get the template: `gateway template <type>`
2. Fill it following the per-type standard: `wiki/spine/standards/{type}-page-standards.md`
3. Validate: `python3 -m tools.pipeline post`
4. Do NOT advance until artifacts exist and pass validation

**Next:** → Step 7

---

### Step 7: TRACK — Readiness and Progress

> [!info] Two Dimensions
>
> | Field | What It Tracks | Range | Who Sets It |
> |-------|---------------|-------|------------|
> | `readiness` | Definition completeness (is it DEFINED?) | 0-100 | Derived for containers. Computed from stages for tasks. |
> | `progress` | Execution completeness (is it BUILT?) | 0-100 | Derived for containers. Agent reports for tasks. |

Readiness advances through Document + Design stages. Progress advances through Scaffold + Implement + Test.
**99→100 = human review only.** Always. No exceptions.

**CLI:** `python3 -m tools.gateway query --field readiness` → field explanation

**Next:** → Step 8

---

### Step 8: FEEDBACK — Contribute Back

When you learn something the second brain doesn't know:

**CLI:** `python3 -m tools.gateway contribute --type lesson --title "What I Learned" --content "..."`

This creates a new lesson in `wiki/lessons/00_inbox/` — the start of the maturity pipeline.

When blocked:
- Set `impediment_type` in your task frontmatter (technical / dependency / decision / environment / clarification / scope / external / quality)
- Each type has a different response: see [[backlog-hierarchy-rules|Backlog Hierarchy Rules]]

---

### At Any Point: Navigate

> [!tip] You Can Always
>
> | You Want | CLI | Obsidian |
> |----------|-----|---------|
> | See the full tree | `gateway navigate` | Open super-model → follow sub-model links |
> | Check your identity | `gateway query --identity` | Read CLAUDE.md Identity Profile table |
> | Find a specific component | `gateway query --field <name>` | Methodology System Map page |
> | Get a template | `gateway template <type>` | wiki/config/templates/ folder |
> | See what's recommended | `gateway what-do-i-need` | Goldilocks concept page |
> | Explore enforcement options | — | Sub-Model: Enforcement Hierarchy |
> | Understand knowledge layers | — | Sub-Model: Knowledge Architecture |

---

## Worked Walkthroughs — Three Real Profiles

These are not hypothetical — each profile exists in the ecosystem. Follow along to see how the flow adapts.

> [!example]- Walkthrough A: Solo Agent on This Wiki (Research Wiki)
>
> **Step 1 — DETECT:** Gateway auto-detects: `domain=knowledge` (wiki/config/ found), `scale=medium` (297 pages), `phase=production` (CI + tests + daily use). Second brain = `self` (this IS the second brain).
>
> **Step 2 — DECLARE:** CLAUDE.md already has the identity profile:
> `Type=system, Execution Mode=solo, Domain=knowledge, Phase=production, Scale=medium, PM Level=L1, Trust Tier=operator-supervised`
>
> **Step 3 — SELECT CHAIN:** Production + medium → **Default** chain. Stage-gated with selected artifacts. Readiness gate = 80. Hooks optional (solo mode, operator present).
>
> **Flexibility:** This wiki could use Simplified (operator is always present, low risk). Default was chosen because the wiki IS the methodology — it should practice what it preaches.
>
> **Step 4 — SELECT MODEL:** Depends on the task. Research about a new topic → `research` model. New wiki page → `documentation` model. New tool feature → `feature-development` model. Evolving lessons → `knowledge-evolution` model. Most work here is `documentation` or `knowledge-evolution`.
>
> **Step 5 — ENTER STAGE:** For a `documentation` model task: Document stage only. For `feature-development`: all 5 stages. Stage rules are in CLAUDE.md's ALLOWED/FORBIDDEN table.
>
> **Step 6 — PRODUCE:** For wiki pages: scaffold from template (`pipeline scaffold concept "Title"`), fill content, run `pipeline post`, verify 0 errors. Artifact chain from `domain-chain-knowledge.md`.
>
> **Step 7 — TRACK:** This wiki uses L1 PM (wiki backlog + CLAUDE.md directives). Readiness/progress tracked in epic frontmatter. No fleet, no harness — operator reviews everything.
>
> **Step 8 — FEEDBACK:** This wiki IS the second brain, so feedback is self-referential. Lessons go directly into `wiki/lessons/00_inbox/`. The evolution pipeline scores and promotes them.

> [!example]- Walkthrough B: Harness v2 Agent on OpenArms (TypeScript)
>
> **Step 1 — DETECT:** Gateway auto-detects: `domain=typescript` (package.json found), `scale=medium` (src/ + tests/ + hooks/), `phase=production` (CI + Docker + systemd). Second brain = `connected` (sibling directory found).
>
> **Step 2 — DECLARE:** OpenArms CLAUDE.md declares:
> `Type=project, Execution Mode=harness v2, Domain=typescript, Phase=production, Scale=medium, PM Level=L2, Trust Tier=standard`
>
> Note: Execution mode is `harness v2` because the harness code EXISTS and is ACTIVE — hooks enforce stage gates, skill-stage-mapping controls injection, post-compact hooks restore state. The harness DISCOVERED its own version from available infrastructure.
>
> **Step 3 — SELECT CHAIN:** Production + medium + harness → **Full** chain. All 5 stages required for feature-dev. Readiness gate = 99. Full infrastructure enforcement (4 hooks, 215 lines).
>
> **Flexibility:** OpenArms COULD use Default (hooks exist but could be advisory). Full was chosen because overnight autonomous runs need enforcement — an unattended agent WILL skip stages without hooks.
>
> **Step 4 — SELECT MODEL:** Harness dispatches based on `task_type` frontmatter. `feature-development` for new features, `bug-fix` for defects, `hotfix` for emergencies. The harness selects the model, not the agent.
>
> **Step 5 — ENTER STAGE:** Stage skills injected by harness via `skill-stage-mapping.yaml` (299 lines, 3 layers). Each stage skill contains MUST/MUST NOT lists, recommended tools, artifact requirements. Agent receives stage-specific context — not the whole methodology.
>
> **Step 6 — PRODUCE:** TypeScript artifact chain: types → stubs → implementation → wiring → tests. Each artifact validated by domain-specific gate commands (`pnpm tsgo`, `pnpm vitest`). Contribution gating: harness checks that previous-stage artifacts exist before allowing next stage.
>
> **Step 7 — TRACK:** L2 PM — harness owns the backlog loop. Readiness/progress updated by harness after each stage gate. 99→100 escalates to operator for review. Fleet logs to `stage-files.log`.
>
> **Step 8 — FEEDBACK:** Harness runs `gateway contribute` for lessons discovered during execution. Contributions enter `wiki/lessons/00_inbox/` in the second brain. Post-run: harness generates a completion note in `raw/notes/`.

> [!example]- Walkthrough C: Full System — OpenFleet (10-Agent Fleet)
>
> **Step 1 — DETECT:** Gateway auto-detects per-agent: `domain=typescript`, `scale=large` (10 concurrent agents, 50k+ LOC across workspaces). `phase=production`. Second brain = `connected` via `kb_sync.py` + LightRAG.
>
> **Step 2 — DECLARE:** Each agent workspace has AGENTS.md:
> `Type=fleet-agent, Execution Mode=full system, Domain=typescript, Phase=production, Scale=large, PM Level=L3, Trust Tier=standard/expert (per agent approval rates)`
>
> Fleet-level identity is in the orchestrator config, not per-agent CLAUDE.md. The orchestrator declares system identity; agents inherit with overrides.
>
> **Step 3 — SELECT PROFILE:** Production + large + fleet → **Full** profile. All 5 stages. Readiness gate = 99. Full immune system: doctor.py (24 rules), MCP tool blocking (1033-line validator), heartbeat enforcement, budget limits.
>
> **Flexibility:** Fleet agents cannot downgrade their profile — the orchestrator enforces Full for all dispatched work. An agent CAN receive a `hotfix` model (implement→test only) but the profile wrapper is always Full.
>
> **Step 4 — SELECT MODEL:** Orchestrator selects model based on task metadata dispatched from Plane (PM tool). `task_type` is set in Plane, synced to the fleet. Agent receives the model as part of task context — it doesn't choose.
>
> **Step 5 — ENTER STAGE:** Per-stage skills injected by orchestrator with tier-based depth. Expert-tier agents get full protocol (5k-10k tokens). Standard-tier get capable (2k-5k). Lightweight-tier get minimal (500-1k). Same structure at every tier — content varies.
>
> **Step 6 — PRODUCE:** Same artifact chain as OpenArms but with cross-agent contributions. Agent A's design doc becomes Agent B's input. Contribution gating: orchestrator validates that contributions are received BEFORE dispatching dependent tasks.
>
> **Step 7 — TRACK:** L3 PM — Plane integration. Readiness/progress synced bidirectionally: Plane → orchestrator → agent → orchestrator → Plane. Dashboards show fleet-wide progress. Anomaly detection flags stuck or regressing agents.
>
> **Step 8 — FEEDBACK:** Fleet generates operational data continuously. `kb_sync.py` aggregates lessons into LightRAG. The wiki's evolution pipeline scores fleet-generated content alongside human-generated content. Immune system rules (doctor.py) update from post-mortem lessons.

---

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **Identity protocol (the questions)** | [[project-self-identification-protocol|Project Self-Identification Protocol]] |
> | **SDLC framework (phase x scale)** | [[sdlc-customization-framework|SDLC Customization Framework]] |
> | **Super-model (all models)** | [[super-model|Super-Model]] |
> | **Methodology model** | [[model-methodology|Model — Methodology]] |
> | **Integration chain (full walkthrough)** | [[second-brain-integration-chain|Second Brain Integration Chain]] |
> | **Gateway tools reference** | [[gateway-tools-reference|Gateway Tools Reference]] |

## Relationships

- PART OF: [[goldilocks-protocol|Sub-Model — Goldilocks Protocol — Identity and Adaptation]]
- BUILDS ON: [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]]
- BUILDS ON: [[sdlc-customization-framework|SDLC Customization Framework — Phases, Scale, and Profile Selection]]
- RELATES TO: [[model-methodology|Model — Methodology]]
- RELATES TO: [[second-brain-integration-chain|Operations Plan — Second Brain Integration Chain — Complete Walkthrough]]
- FEEDS INTO: [[wiki-gateway-tools-unified-knowledge-interface|Wiki Gateway Tools — Unified Knowledge Interface]]

## Backlinks

[[goldilocks-protocol|Sub-Model — Goldilocks Protocol — Identity and Adaptation]]
[[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]]
[[sdlc-customization-framework|SDLC Customization Framework — Phases, Scale, and Profile Selection]]
[[model-methodology|Model — Methodology]]
[[second-brain-integration-chain|Operations Plan — Second Brain Integration Chain — Complete Walkthrough]]
[[wiki-gateway-tools-unified-knowledge-interface|Wiki Gateway Tools — Unified Knowledge Interface]]
[[gateway-tools-reference|Gateway Tools Reference — Complete Command Documentation]]
[[model-context-engineering|Model — Context Engineering]]
