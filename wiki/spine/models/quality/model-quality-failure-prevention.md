---
title: Model — Quality and Failure Prevention
aliases:
  - "Model — Quality and Failure Prevention"
  - "Model: Quality and Failure Prevention"
type: concept
domain: cross-domain
layer: spine
status: synthesized
confidence: high
maturity: growing
created: 2026-04-09
updated: 2026-04-14
sources:
  - id: src-autobe-compiler-verified-backend-generation
    type: wiki
    file: wiki/sources/tools-integration/src-autobe-compiler-verified-backend-generation.md
    title: "Synthesis — AutoBE: Compiler-Verified Backend Generation"
  - id: src-code-review-graph-automated-review
    type: wiki
    file: wiki/sources/tools-integration/src-code-review-graph-automated-review.md
    title: "Source — code-review-graph: Graph-Based Automated Code Review"
  - id: src-claude-code-prompt-patch-rebalancing
    type: wiki
    file: wiki/sources/tools-integration/src-claude-code-prompt-patch-rebalancing.md
    title: "Synthesis — Claude Code Prompt Patch: Rebalancing Agent Behavior"
  - id: src-harness-engineering-article
    type: article
    url: https://levelup.gitconnected.com/building-claude-code-with-harness-engineering-d2e8c0da85f0
    title: Building Claude Code with Harness Engineering
    ingested: 2026-04-08
  - id: src-openfleet-local
    type: documentation
    project: openfleet
    path: CLAUDE.md
    title: OpenFleet — Local Project Documentation
    ingested: 2026-04-08
  - id: src-devops-control-plane-local
    type: documentation
    project: devops-control-plane
    path: README.md
    title: devops-control-plane — Local Project Documentation
    ingested: 2026-04-08
tags: [model, spine, quality, failure-prevention, harness, immune-system, rework, depth-verification, stage-gates, methodology]
---
# Model — Quality and Failure Prevention
## Summary

Quality and failure prevention for AI agents is not a set of best practices — it is a system with three enforcement layers (structural prevention, teaching, review), six codified failure lessons, and deterministic mechanisms that cannot be bypassed by prompt engineering. The model synthesizes evidence from four domains: harness engineering (13 guardrail rules enforced via hooks), OpenFleet's immune system (24 rules from 16 post-mortems), rework prevention economics, and this wiki's own operational failures. ==The central thesis: quality enforcement must live in code that runs at execution time, not in documentation that the agent may or may not consult.==

## Key Insights

- **Three-layer defense is the minimum viable quality architecture.** Structural prevention (hooks, doctor.py) blocks bad actions. Teaching (CLAUDE.md, skills, memory) shapes behavior. Review (human gates) catches what automation misses. Any single layer alone is insufficient. See [[three-lines-of-defense-immune-system-for-agent-quality|Three Lines of Defense — Immune System for Agent Quality]] for the full pattern with implementation evidence from OpenFleet (746 lines, production) and OpenArms (215 lines, 100% stage compliance).

- **Instructions fail, infrastructure works — quantified.** OpenArms v8: 28 CLAUDE.md rules, 75% stage boundary violations overnight. v10: 4 hooks (215 lines), 0% stage boundary violations across 5 production runs. The same rules, different enforcement mechanism, categorical difference. See [[infrastructure-enforcement-proves-instructions-fail|Infrastructure Enforcement Proves Instructions Fail]] for the full evidence chain.

- **Seven behavioral failure classes persist after infrastructure.** Even with 0% stage violations, clean completion rate is 20% (1/5 runs need no manual fix). The remaining failures are BEHAVIORAL, not tool-level (updated 2026-04-15 to match the authoritative taxonomy page numbering): (1) artifact pollution (24% contamination rate), (2) weakest-checker optimization (code passes loose gate, fails strict), (3) environment patching without escalation (4-layer polyfill chain, $12-15 overhead), (4) fatigue cliff (predictable quality degradation stages 4-5; cost curve $3.50/task v1-v2 → $1.32/task v5-v7, quality drops regardless of cost), (5) sub-agent non-compliance (~67% violation rate per T111, = ~33% compliance even with rules in prompt), (6) silent conflict resolution (agent accommodates instead of escalating), (7) memory/wiki conflation (this wiki's independent contribution — agent writes project knowledge to Claude Code memory instead of wiki, invisible to the second brain and other agents). See [[agent-failure-taxonomy-seven-classes-of-behavioral-failure|Agent Failure Taxonomy — Seven Classes of Behavioral Failure]] for the canonical version with per-class evidence and E016-verified fix recommendations.

- **Enforcement must be mindful — hard blocks need justified bypass.** Blind enforcement creates its own failures. Every block must explain WHY, every system must offer bypass with logged justification. OpenArms T086: agent's correct fix reverted twice by over-enforcement. See [[enforcement-must-be-mindful-hard-blocks-need-justified-bypass|Enforcement Must Be Mindful — Hard Blocks Need Justified Bypass]].

- **Context compaction is a reset event.** All behavioral corrections accumulated during a session are lost after compaction. Post-compact hooks must rebuild full state from files. See [[context-compaction-is-a-reset-event|Context Compaction Is a Reset Event]].

- **Failure lessons must be codified, not just remembered.** Each failure maps to a concrete enforcement mechanism. A lesson that exists only as documentation is a suggestion. A lesson encoded in CLAUDE.md, enforced by a hook, and checked by the post-chain is a rule.

- **Rework is multiplicative, not additive.** Redoing work requires reverting, re-planning, re-executing, and re-verifying. In a multi-agent fleet, one bad dispatch cascades. Prevention is cheaper than cure. Contribution gating (cross-agent inputs BEFORE work) is the most effective rework prevention. See [[contribution-gating-cross-agent-inputs-before-work|Contribution Gating — Cross-Agent Inputs Before Work]].

- **Depth verification is the single highest-leverage quality rule.** Reading the thing itself rather than a description of the thing prevents the most common class of hollow synthesis.

- **Methodology IS failure prevention.** Stage gates, quality gates per stage, "do not advance until the gate passes" — these are the operational form of every lesson in this model. The [[harness-owned-loop-deterministic-agent-execution|Harness-Owned Loop — Deterministic Agent Execution]] pattern takes this further: the agent never controls its own loop, never sees the backlog, never manages git.

## Deep Analysis

### The Three-Layer Defense

> [!info] **Three layers, three failure classes**
> | Layer | Mechanism | What it catches | Compliance | Example |
> |-------|-----------|----------------|-----------|---------|
> | **1 — Structural prevention** | Hooks, doctor.py, deterministic guards | Actions that should NEVER happen | ~98% | Block sudo, force-push, .env writes |
> | **2 — Teaching** | CLAUDE.md, skills, memory | Behavioral patterns that lead to failures | ~60% | "Always run pipeline post after changes" |
> | **3 — Review** | Human gates at stage transitions | Subjective quality the agent can't evaluate | 100% (when engaged) | "Does this synthesis capture the source's meaning?" |

**Layer 1 — Structural Prevention** blocks bad actions at execution time. The agent cannot bypass these through reasoning, confidence, or prompt injection.

> [!example]- **Implementations across the ecosystem**
> - **[[harness-engineering|Harness Engineering]]**: 13 TypeScript guardrail rules (R01-R13) enforced via Claude Code hooks. Denial rules block sudo, .env writes, force-push. Query rules flag out-of-scope writes. Security rules prevent --no-verify and direct main pushes.
> - **[[immune-system-rules|Immune System Rules]]**: 24 Python rules in doctor.py running at step 6 of the 12-step orchestrator cycle. Zero LLM calls — pure state evaluation. Five categories: liveness, loop detection, state integrity, behavioral security, resource exhaustion.
> - **[[deterministic-shell-llm-core|Deterministic Shell, LLM Core]]**: The architectural pattern. The LLM operates only in the execution phase, surrounded by deterministic code. The shell enforces invariants that cannot be social-engineered.

> [!tip] **The critical property**
> Structural prevention is deterministic, fast (microseconds per check), cheap (no token cost), and auditable (no inference variability). An LLM-based quality gate would be unreliable by design.

**Layer 2 — Teaching** shapes behavior before the action is considered. Well-designed teaching reduces the frequency of hook violations, making Layer 1 a backstop rather than the primary defense.

> [!info] **The teaching stack**
> | Mechanism | When it loads | Persistence | Example |
> |-----------|-------------|-------------|---------|
> | CLAUDE.md | Every message | Per-project | Quality gates, ingestion modes, stage gates |
> | Skills | On invocation | Per-session | wiki-agent ingestion methodology, evolve maturity rules |
> | Memory | Cross-session | Permanent | "Never synthesize from descriptions alone" |

**Layer 3 — Review** handles decisions automation cannot evaluate: Does this synthesis capture the source's meaning? Is this architecture right for this context? Does this page deserve maturity promotion?

> [!abstract] **Review gates in the wiki**
> - **Guided mode**: human approves extraction plan before synthesis begins
> - **Smart mode escalation**: auto-processing stops on new domains, contradictions, ambiguity
> - **Maturity promotion**: seed pages require review before advancing to growing

---

### The Six Failure Lessons

Each lesson was extracted from a real operational failure in this wiki. Each maps to a specific enforcement mechanism.

> [!bug]- **1. Never Synthesize from Descriptions Alone**
> **The failure:** Agent ingested a curated list (awesome-design-md), synthesized a page claiming to understand the DESIGN.md pattern, but had never opened a single real DESIGN.md file. Confident-sounding, factually hollow.
>
> **The principle:** Layer 0 (description of a thing) is not Layer 1 (an instance of the thing). Minimum bar: examine at least one real instance.
>
> **Enforcement:** CLAUDE.md quality gates + wiki-agent skill depth verification + memory directive. The 0.25 ratio rule (25% of ingestion on primary sources) provides a measurable threshold. See [[never-synthesize-from-descriptions-alone|Never Synthesize from Descriptions Alone]].

> [!bug]- **2. Never Skip Stages Even When Told to Continue**
> **The failure:** Agent treated "continue" as permission to skip brainstorm and jump to spec writing. User response: "WTF ???? WHAT SPEC ??? WTF ???????"
>
> **The principle:** "Continue" = advance within current stage. Only "skip to X" authorizes stage-skipping.
>
> **Enforcement:** CLAUDE.md stage gates + mandatory post-chain (errors block completion). See [[never-skip-stages-even-when-told-to-continue|Never Skip Stages Even When Told to Continue]].

> [!bug]- **3. Shallow Ingestion Is Systemic, Not Isolated**
> **The failure:** Thin pages accumulated — minimal summaries, sparse relationships, no deep analysis. The evolution pipeline had no quality candidates to promote.
>
> **The principle:** Soft quality gates degrade the entire system. One skipped gate creates systematic downstream degradation.
>
> **Enforcement:** Validation requires ≥30-word summaries, ≥1 relationship, source provenance, no >70% overlap. See [[shallow-ingestion-is-systemic-not-isolated|Shallow Ingestion Is Systemic, Not Isolated]].

> [!bug]- **4. Infrastructure Must Be Reproducible, Not Manual**
> **The failure:** Agent tried to `cat >` a systemd service file directly. Configuration silently diverged across environments.
>
> **The principle:** Any infrastructure step not encoded in a script is a quality gap. Manual steps are undocumented, unrepeatable, invisible.
>
> **Enforcement:** `python -m tools.setup` handles all setup. `--services` deploys daemons reproducibly. No manual infra creation. See [[infrastructure-must-be-reproducible-not-manual|Infrastructure Must Be Reproducible, Not Manual]].

> [!bug]- **5. The Agent Must Practice What It Documents**
> **The failure:** Wiki documented methodology extensively — stage gates, brainstorm-before-spec, depth verification. Agent skipped all of them. Documentation was correct; behavior was not.
>
> **The principle:** Methodology in wiki pages is useless if not in CLAUDE.md. Rules must exist in the agent's OPERATIONAL instructions, not just its knowledge base.
>
> **Enforcement:** CLAUDE.md contains the rules the agent follows. When the wiki evolves a rule, it must propagate to CLAUDE.md. See [[the-agent-must-practice-what-it-documents|The Agent Must Practice What It Documents]].

> [!bug]- **6. Models Are Built in Layers, Not All at Once**
> **The failure:** 14 model pages batch-produced as 80-110 line reading lists. Agent claimed "models are ready." User: "I dont even see 2% of it..."
>
> **The principle:** Structure (pages exist) ≠ substance (pages define systems). The SFIF pattern applies to model-building itself: scaffold → foundation → infrastructure → features.
>
> **Enforcement:** Model-builder skill defines the quality bar (≥150 lines, system definition not reading list, Key Pages, Lessons, State of Knowledge, How to Adopt). See [[models-are-built-in-layers-not-all-at-once|Models Are Built in Layers, Not All at Once]].

---

### The Immune System (OpenFleet)

> [!info] **24 rules from 16 post-mortems — production-grade structural prevention**
> | Category | What it detects | Example rules |
> |----------|----------------|---------------|
> | **Liveness** | Agents alive in state but dead in practice | Heartbeat timeout, stale session ID, stuck execution |
> | **Loop detection** | Runaway cycles | Retry storms, circular dependencies, dispatch-without-completion |
> | **State integrity** | Impossible state combinations | Parent complete but children pending, blocked with no blocker |
> | **Behavioral security** | Permission and scope violations | Out-of-scope writes, cost spikes, capability acquisition beyond spec |
> | **Resource exhaustion** | Degraded conditions | Circuit breaker open, external service unresponsive, memory pressure |

> [!tip] **The 3-Strike Pattern**
> One violation doesn't trigger action. Three violations within a window trigger quarantine. This tolerates transient anomalies (network blips, brief CPU spikes) while catching persistent failures. doctor.py runs at step 6 of the 12-step orchestrator cycle — after security scan, before dispatch. Flagged tasks accumulate strikes before they can reach dispatch. Preemptive immune response, not reactive incident handling.

---

### The Inference-Layer Reliability Stack (AICP, NEW 2026-04-18/19)

AICP instantiates the same three-lines-of-defense pattern at a different scope — **AI-inference backend reliability** rather than agent-behavior enforcement. Three first-class patterns compose into one stack:

> [!info] **AICP's three-layer reliability composition** (complement to OpenFleet's doctor.py behavior layer)
>
> | Layer | Pattern | Code | What it handles |
> |-------|---------|------|-----------------|
> | **1 — Fast-fail per backend** | [[per-backend-circuit-breaker-with-failover-chain\|Per-Backend Circuit Breaker with Failover Chain]] | `aicp/core/circuit_breaker.py` (207 L) | Repeated synchronous-wait failures on a known-bad backend. CLOSED→OPEN→HALF_OPEN state machine; per-backend isolation; profile-tunable thresholds (default 3, reliable 2) |
> | **2 — Cross-backend failover** | Controller failover chain | `aicp/core/controller.py` | `CircuitBreakerOpen` caught alongside generic `Exception` — same except clause advances to next backend (local → fleet → openrouter → claude). Quality-score escalation threshold triggers auto-retry on next tier |
> | **3 — Durable persistence** | [[per-day-jsonl-dlq-with-retry-budget\|Per-Day JSONL DLQ with Retry Budget]] | `aicp/core/dlq.py` (260 L) | When failover chain exhausts: persist to `~/.aicp/dlq/<UTC-date>.jsonl` with full task context. Retry via `aicp --retry-dlq` CLI OR MCP `dlq_status` polling. Profile-tunable retries (default 3, reliable 5) |

The stack composes with AICP's runtime substrate: [[single-active-backend-with-lru-eviction\|Single-Active Backend with LRU Eviction]] handles the VRAM-constrained model-loading layer; [[profile-as-coordination-bundle\|Profile as Coordination Bundle]] coordinates the ~12-setting reliability profile (circuit_breaker + warmup + dlq + reports) with one `make profile-use reliable` switch.

**Evidence the three-lines pattern generalizes across failure domains:**

| Scope | Agent-behavior layer (OpenFleet) | Inference-backend layer (AICP) |
|-------|----------------------------------|--------------------------------|
| Line 1 — Prevention | Stage-gated tools, contribution gating | Per-backend circuit breakers |
| Line 2 — Detection | doctor.py cycle (30s, 10 rules) | Failover chain auto-escalation |
| Line 3 — Correction | PRUNE/ESCALATE/quarantine | DLQ persistence + retry budget |

Both **hide enforcement from the enforced entity** (agents don't see the doctor; inference callers don't see the breaker state). Both use **profile-tunable thresholds** per workload. Both **compose additively** — removing any layer leaves a known failure mode uncovered.

This is the first ecosystem evidence that three-lines generalizes beyond a single failure domain. See [[three-lines-of-defense-immune-system-for-agent-quality\|Three Lines of Defense]] Instances section for the full cross-project comparison.

---

### The Enforcement Level Hierarchy

> [!info] **Enforcement levels — from hope to certainty**
> | Level | Mechanism | Compliance | Example |
> |-------|-----------|-----------|---------|
> | 0 | Prompt guidance (CLAUDE.md) | ~60% | "Always run tests before committing" |
> | 1 | Workflow orchestration (skills, chains) | ~80% | Research-Plan-Execute-Review cycle |
> | 2 | Runtime guardrails (hooks, pre/post) | ~98% | Block sudo, force-push, .env writes |
> | 3 | Deterministic orchestration (state machine) | 100% | OpenFleet 30-second brain cycle |

> [!warning] **Measuring maturity**
> A project's quality maturity = how much enforcement has migrated upward from Level 0 toward Level 3. This wiki currently operates at Levels 0-1. The planned next step is Level 2 (hook-based stage-gate enforcement). OpenFleet operates at Level 3 for its orchestration loop.

---

### Rework Prevention Economics

> [!info] **The cost model that justifies every quality gate**
> ```
> Single rework cycle ≈ 2.5T to 3.5T (estimate — needs measurement)
>   T = original task, R = revert, D = diagnosis,
>   P = re-plan, T = re-execute, V = re-verify
>
> Prevention investment: 0.2T to 0.4T per task
> Break-even: prevention net-positive if rework reduced by >12%
> Real rework rates without gates: 20-40% on complex tasks
> ```

> [!warning] **Unverified numbers**
> The specific multiplier (2.5-3.5x) and rework rates (20-40%) are estimates from harness engineering literature, not measured from this ecosystem. The PRINCIPLE (prevention < rework) is structurally sound. The NUMBERS need measurement from real project data.

> [!abstract] **How the wiki maps to prevention investment**
> - **Guided mode** = maximum prevention (human approves every step) — highest cost, lowest rework
> - **Smart mode** = risk-calibrated (auto when confident, escalate when not) — balanced
> - **Auto mode** = throughput-first (process without stopping) — lowest cost, highest rework risk

---

### The Depth Verification System

> [!warning] **The single highest-leverage quality rule**
> Read the thing, not the description of the thing. A README listing 58 DESIGN.md files ≠ reading a DESIGN.md file. An API spec ≠ a real request/response pair.

> [!info] **The layer model for source depth**
> | Layer | What it is | Synthesis quality |
> |-------|-----------|------------------|
> | Layer 0 | Description of the thing (README, catalog, index) | Hollow — confident surface, no substance |
> | Layer 1 | A real instance of the thing (actual file, output, config) | Grounded — specific, verifiable claims |
> | Layer 2 | Multiple instances compared (pattern extraction from N examples) | Deep — structural insights across instances |

Minimum bar for synthesis: **Layer 1**. The 0.25 ratio rule — at least 25% of ingestion effort on primary sources — provides a measurable threshold.

---

### How the Three Layers Interact

The layers are not independent — they form a defense-in-depth system where each layer reduces the load on the others.

> [!abstract] **The interaction model**
> **Teaching reduces the violation rate** — a well-taught agent (CLAUDE.md + skills + memory) attempts fewer dangerous operations, making structural prevention a backstop instead of the primary defense.
>
> **Structural prevention catches what teaching misses** — ~40% of the time, the agent ignores or forgets instructions. Hooks block the operation before it completes. The agent learns nothing from the block (it just fails), but damage is prevented.
>
> **Review handles the irreducibly subjective** — "Does this synthesis capture the source's meaning?" is not a question code can answer. Review gates exist for decisions that require human judgment, not for decisions that could be automated.
>
> **The failure mode is relying on ONE layer.** Hooks without teaching → correct-but-misaligned work (the agent does safe things but not the RIGHT things). Teaching without hooks → well-intentioned failures (the agent knows the rules but doesn't always follow them). Review without either → exhausted humans catching everything manually.

---

### The Methodology Connection

==Stage gates are the structural embodiment of failure prevention.== Each stage has a quality gate. Work does not advance until the gate passes. This is not process overhead — it is the operational form of every lesson in this model:

> [!info] **Each lesson maps to a stage gate**
> | Lesson | Stage gate it maps to |
> |--------|----------------------|
> | "Never synthesize from descriptions alone" | Extraction gate requires primary source examination (Layer 1+) |
> | "Never skip stages" | Gates are mandatory, not advisory — errors block advancement |
> | "Shallow ingestion is systemic" | Gate criteria enforce minimum depth (≥30 words, ≥1 relationship) |
> | "Infrastructure must be reproducible" | Post-chain automates gate enforcement (`pipeline post` = 6 deterministic steps) |
> | "Practice what you document" | CLAUDE.md contains the gates the agent must pass (operational, not aspirational) |
> | "Models built in layers" | Model-builder skill quality bar IS the gate for model creation |

The post-ingestion chain (`python3 -m tools.pipeline post`) is the automated enforcement: rebuild indexes → regenerate manifest → validate all pages (errors block) → regenerate wikilinks → run lint → rebuild layer indexes. Six steps, all mandatory, all deterministic. This is structural prevention applied to the wiki's own methodology.

---

### Key Pages

| Page | Layer | Role in the model |
|------|-------|-------------------|
| [[harness-engineering|Harness Engineering]] | L2 | The coordinated enforcement architecture — 13 rules, 5-verb workflow, enforcement hierarchy |
| [[immune-system-rules|Immune System Rules]] | L2 | 24 production rules from 16 post-mortems — liveness, loops, state, security, resources |
| [[rework-prevention|Rework Prevention]] | L2 | Cost model justifying quality gates — prevention vs rework economics |
| [[deterministic-shell-llm-core|Deterministic Shell, LLM Core]] | L5 | The architectural pattern — deterministic code surrounding probabilistic LLM |
| [[llm-knowledge-linting|LLM Knowledge Linting]] | L2 | Automated quality maintenance — detecting orphans, contradictions, staleness |
| [[stage-gate-methodology|Stage-Gate Methodology]] | L2 | Stage-gate mechanics — how tasks progress through gates |
| [[skyscraper-pyramid-mountain|Skyscraper, Pyramid, Mountain]] | L2 | Quality tier framework — explicit choice vs accidental chaos |
| [[never-synthesize-from-descriptions-alone|Never Synthesize from Descriptions Alone]] | L4 | Failure lesson — depth verification origin |
| [[never-skip-stages-even-when-told-to-continue|Never Skip Stages Even When Told to Continue]] | L4 | Failure lesson — stage-gate enforcement origin |
| [[shallow-ingestion-is-systemic-not-isolated|Shallow Ingestion Is Systemic, Not Isolated]] | L4 | Failure lesson — systemic quality degradation |
| [[infrastructure-must-be-reproducible-not-manual|Infrastructure Must Be Reproducible, Not Manual]] | L4 | Failure lesson — reproducible tooling origin |
| [[the-agent-must-practice-what-it-documents|The Agent Must Practice What It Documents]] | L4 | Failure lesson — operational rules vs documentation gap |
| [[models-are-built-in-layers-not-all-at-once|Models Are Built in Layers, Not All at Once]] | L4 | Failure lesson — structure ≠ substance |
| [[plan-execute-review-cycle|Plan Execute Review Cycle]] | L5 | The universal workflow that harness engineering codifies |
| [[always-plan-before-executing|Always Plan Before Executing]] | L4 | The planning discipline that prevents the most rework |
| [[claude-code-best-practices|Claude Code Best Practices]] | L2 | Teaching layer content — planning discipline, context hygiene, skill architecture |
| [[automated-knowledge-validation-prevents-wiki-decay|Automated Knowledge Validation Prevents Silent Wiki Decay]] | L4 | Why automated linting prevents the most common quality failure mode |
| [[block-with-reason-and-justified-escalation\|Block With Reason and Justified Escalation]] | L5 | Bypass mechanism for mindful-enforcement — structured 4-part protocol (Block + Reason + Offer + Justification). Added 2026-04-15. |
| [[observe-fix-verify-loop\|Observe-Fix-Verify Loop]] | L5 | Battle-testing cycle at three timescales (session/runtime/sprint). Externality-of-Verify invariant. Added 2026-04-15. |
| [[adapters-never-raise-failure-as-data-at-integration-boundaries\|Adapters Never Raise — Failure as Data]] | L5 | Integration-boundary pattern — structured result types instead of exception propagation across process/language/loop boundaries. 6 convergent instances across ecosystem. Added 2026-04-15. |

---

### Lessons Learned

| Lesson | What was learned | Enforcement mechanism |
|--------|-----------------|---------------------|
| [[never-synthesize-from-descriptions-alone|Never Synthesize from Descriptions Alone]] | Layer 0 ≠ Layer 1. Read the thing, not the description. | CLAUDE.md + wiki-agent skill + 0.25 ratio rule |
| [[never-skip-stages-even-when-told-to-continue|Never Skip Stages Even When Told to Continue]] | "Continue" = within current stage. Stage gates are hard boundaries. | CLAUDE.md stage gates + mandatory post-chain |
| [[shallow-ingestion-is-systemic-not-isolated|Shallow Ingestion Is Systemic, Not Isolated]] | Soft gates degrade the entire system. Quality compounds. | Validation: ≥30 words, ≥1 relationship, source provenance |
| [[infrastructure-must-be-reproducible-not-manual|Infrastructure Must Be Reproducible, Not Manual]] | Manual steps are undocumented, unrepeatable, invisible. | `tools/setup.py` handles all infra deployment |
| [[the-agent-must-practice-what-it-documents|The Agent Must Practice What It Documents]] | Rules in wiki pages ≠ rules the agent follows. Must be in CLAUDE.md. | CLAUDE.md contains operational rules, not just documentation |
| [[models-are-built-in-layers-not-all-at-once|Models Are Built in Layers, Not All at Once]] | Structure ≠ substance. Follow SFIF for model building. | Model-builder skill with quality bar + checklist |
| [[agent-failure-taxonomy-seven-classes-of-behavioral-failure|Agent Failure Taxonomy — Seven Classes of Behavioral Failure]] | 7 behavioral failures persist after 100% infrastructure enforcement. 20% clean completion rate. | Deep evidence: overnight run degradation data, specific fix options per class |
| [[harness-ownership-converges-independently-across-projects|Harness Ownership Converges Independently Across Projects]] | 3 independent projects converged on harness-owned loop. Not preference — structural requirement. | Convergence evidence from OpenArms, OpenFleet, and external harness engineering article |

> [!bug]- Critical Evidence: 2,073 Lines of Orphaned Code — Tests Alone Prove Nothing
>
> OpenArms first session: agent completed 53 tasks, 4 epics at "review/100%", 686 passing tests. Manual audit: 2,073 lines of production code that NOTHING in the runtime imported. The agent built a library, not features.
>
> | Epic | Feature | Lines | Runtime Imports | Status |
> |------|---------|-------|----------------|--------|
> | E002 | Network Rules | ~600 | 0 | Orphaned |
> | E003 | Cost Tracking | ~500 | 0 | Orphaned |
> | E007 | Hook Events | ~500 | 0 | Orphaned |
> | E004 | Live Tracing | ~473 | 0 | Orphaned |
>
> **Mechanism:** Same-author tests create a closed loop. Agent writes implementation → agent writes tests for that implementation → tests verify the implementation behaves as the agent intended. At no point does anyone verify the INTENT is correct or the INTEGRATION is functional.
>
> **Fix applied in methodology v5:** Implement stage MUST wire code into an existing runtime consumer (not just pass standalone tests). This is now enforced by `validate-stage.cjs` which checks `existing-files.json` for at least one modified src/ file during integration.

---

### State of Knowledge

> [!success] **Well-covered (multiple sources, real evidence, quantified)**
> - Three-layer defense architecture (structural + teaching + review) — with OpenFleet immune system (746 lines, 5 diseases, 4 corrections)
> - 7 behavioral failure classes with overnight run data (fatigue cliff: $3.50→$1.32/task cost curve, predictable degradation order)
> - Harness engineering: 4 hooks (215 lines) achieving 100% stage compliance, model-aware validation (1,033 lines)
> - Immune system: 30-second doctor cycle, persistent health profiles, graduated correction (TEACH→PRUNE)
> - Compliance is an arms race: 4/6 bugs persistent across 5 methodology versions despite directive fixes, detection evasion (286 lines bypassing regex)
> - Integration tests insufficient: 2,073 orphaned lines, 686 passing tests, 0 verified features
> - Methodology battle-tested: 7 bugs → 7 versions → cost dropped 62% ($3.50→$1.32/task) — self-hosting feedback loop
> - 3 principles distilled: Infrastructure Over Instructions, Structured Context, Goldilocks Imperative

> [!warning] **Thin or unverified**
> - Rework multiplier (5.5x from wiki estimate) — not independently measured
> - Hook-based enforcement for wiki quality — no hooks on this project yet (Level 0-1 only)
> - Quantitative enforcement level measurement — no metric for "what % of rules are at Level 0 vs Level 3"
> - Formal compliance checking tooling — designed (E016) but not built

---

### How to Adopt

> [!info] **Setting up the quality system for a new project**
> 1. **CLAUDE.md** — add quality gates (minimum standards per artifact type)
> 2. **Validation tooling** — schema validation that blocks on errors (exit code enforcement)
> 3. **Post-chain** — automated multi-step validation after every change batch
> 4. **Depth verification** — add the Layer 0/1/2 rule to ingestion methodology
> 5. **Stage gates** — define ALLOWED/FORBIDDEN per stage in methodology.yaml

> [!warning] **INVARIANT — never change these**
> - Quality enforcement must be deterministic (no LLM-based quality gates)
> - Validation errors block completion (not advisory)
> - Failure lessons propagate to CLAUDE.md (operational, not just documented)
> - Three-layer defense (all three required — no single layer is sufficient)
> - Rework prevention via upfront investment (plan before execute)

> [!tip] **PER-PROJECT — always adapt these**
> - Which quality gates apply (code projects: compilation + lint + tests; wiki projects: validation + links + word count)
> - Which enforcement level to start at (Level 0 is fine initially — migrate upward as methodology matures)
> - Which failure lessons are relevant (not all 6 apply to every project type)
> - The 3-strike threshold for immune system rules (project-specific tolerance)
> - Review gate triggers (what requires human review vs what auto-advances)

> [!bug]- **What goes wrong if you skip this**
> - **No structural prevention** → agent follows instructions ~60% of the time. 40% of dangerous operations succeed.
> - **No teaching** → agent doesn't know the rules. Every session starts from zero methodology.
> - **No review** → agent makes subjective quality decisions unchecked. Confident-but-wrong artifacts accumulate.
> - **No depth verification** → hollow synthesis passes validation (format correct, substance missing). Evolution pipeline starves.
> - **No stage gates** → work skips stages. Artifacts produced out of order. False readiness claims.

### External Validation — Industry Evidence for Our Principles (NEW 2026-04-14)

Three independent 2026 sources provide external validation for this model's core architecture — the three-layer defense, the 7-class failure taxonomy, and the deterministic shell pattern — without having been designed to do so.

**[[src-autobe-compiler-verified-backend-generation|AutoBE]]: "If You Can Verify, You Converge"**

AutoBE's compiler-verified backend generation system encodes the deterministic-shell principle in production at scale: wrap an LLM generation step in a structural verifier (the TypeScript/Go compiler), retry on failure, converge on success. Quality is independent of model choice when verification is in place. This is the same pattern as our `pipeline post` chain — deterministic validators (schema check, manifest, lint) are the quality guarantee, not the LLM's judgment. The AutoBE finding that model differences affect *retry count not final quality* is the strongest empirical validation of Layer 1 (structural prevention) in this model: deterministic verification catches errors that better prompting cannot. The pattern also generalizes: anywhere an output is machine-verifiable (compilation, schema validation, test execution), a retry loop gives weaker models parity with stronger ones.

**[[src-code-review-graph-automated-review|code-review-graph]]: Graph-Level Review Catches What Line Review Misses**

The code-review-graph project demonstrates that entity-relationship extraction from code improves relational accuracy from 31.6% to 68.4% — a 2.16x improvement in catching relational errors. Standard line-level review (which is what agents do by default) misses blast-radius issues: a change in one file whose impact propagates through call graphs and dependency chains. This is the structural equivalent of our shallow-ingestion failure lesson applied to code: reading a change in isolation (Layer 0) versus reading it in its dependency context (Layer 1+). The graph-based approach implements Layer 2 (multiple instances compared) for code review: it models how a change interacts with the full entity graph, not just the diff. For our quality system, this validates the design of doctor.py's state integrity rules — checking impossible state combinations requires modeling relationships, not just individual states.

**[[src-claude-code-prompt-patch-rebalancing|Claude Code prompt patch]]: Community Documented 11 Agent Corner-Cutting Behaviors**

The community prompt patch project catalogued 11 specific Claude Code behaviors that required explicit override prompts to correct: overconfidence, scope creep, assumption-making, hedging, confirmatory bias, and 6 others. This independently validates our 7-class agent failure taxonomy from the bottom up — the community reached similar conclusions from production Claude Code experience without access to our OpenArms/OpenFleet data. Notable overlaps:

> [!info] **Taxonomy cross-validation**
>
> | Our 7-class taxonomy | Community patch finding | Match |
> |---------------------|------------------------|-------|
> | Weakest-checker optimization | Overconfidence / selective tool use | Class 1 |
> | Silent conflict resolution | Assumption-making without flagging | Class 5 |
> | Artifact pollution | Scope creep beyond task boundaries | Class 6 |
> | Context-window degradation | Behavioral drift in long sessions | Class 7 |
> | Sub-agent non-compliance | — (not covered; sub-agent behavior differs) | — |
>
> The fact that 11 community patches were needed for basic agent quality validates the central thesis: quality enforcement must live in code (Layer 1 hooks), not in instructions (Layer 2 teaching) alone. The community's workaround was Layer 2 (better prompts). Our architecture adds Layer 1 (structural blocking) on top.

---

## Open Questions

> [!question] ~~**How should enforcement level be measured quantitatively?**~~
> **RESOLVED:** Compliance rate = (gates passed without bypass) / (total gate encounters). Already measured informally (25%→100% from OpenArms). Needs formal tracking.
> What percentage of quality rules currently live at Level 0 (hope) vs Level 3 (deterministic)? A metric like "enforcement maturity score = weighted average across levels" could track progress. (Requires: cataloging all rules with their current enforcement level)

> [!question] ~~****Can the 3-strike pattern apply to wiki quality?****~~
> **RESOLVED:** Yes. Strike 1: lint warning. Strike 2: flag for review. Strike 3: demote to draft. For thin summaries, broken relationships, stale content.
> Three thin pages in a row → mandatory depth review. Three validation failures → auto-escalate to guided mode. Would this reduce systemic quality decay or add bureaucratic overhead? (Requires: implementing and testing on a real ingestion batch)

> [!question] **What is the empirical rework rate across ingestion modes?**
> Guided mode has the highest prevention cost. Auto mode has the highest rework risk. Smart mode balances. But what are the ACTUAL rework rates? (Requires: tracking rework across 50+ ingestion tasks)

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **The enforcement hierarchy** | [[enforcement-hierarchy|Sub-Model — Enforcement Hierarchy — From Instructions to Immune System]] |
> | **Enforcement hook patterns** | [[enforcement-hook-patterns|Enforcement Hook Patterns]] |
> | **Three lines of defense** | [[three-lines-of-defense-immune-system-for-agent-quality|Three Lines of Defense — Immune System for Agent Quality]] |
> | **Failure taxonomy (7 classes)** | [[agent-failure-taxonomy-seven-classes-of-behavioral-failure|Agent Failure Taxonomy — Seven Classes of Behavioral Failure]] |
> | **Mindful enforcement** | [[enforcement-must-be-mindful-hard-blocks-need-justified-bypass|Enforcement Must Be Mindful — Hard Blocks Need Justified Bypass]] |
> | **Rework prevention economics** | [[contribution-gating-cross-agent-inputs-before-work|Contribution Gating — Cross-Agent Inputs Before Work]] |
> | **Depth verification** | [[never-synthesize-from-descriptions-alone|Never Synthesize from Descriptions Alone]] |
> | **Context compaction** | [[context-compaction-is-a-reset-event|Context Compaction Is a Reset Event]] |
> | **SFIF quality tiers** | [[model-sfif-architecture|Model — SFIF and Architecture]] |
> | **Methodology connection** | [[model-methodology|Model — Methodology]] |
> | **Standards for this model** | [[model-quality-failure-prevention-standards|Quality Standards — What Good Failure Prevention Looks Like]] |

## Relationships

- BUILDS ON: [[harness-engineering|Harness Engineering]]
- BUILDS ON: [[immune-system-rules|Immune System Rules]]
- BUILDS ON: [[rework-prevention|Rework Prevention]]
- BUILDS ON: [[deterministic-shell-llm-core|Deterministic Shell, LLM Core]]
- BUILDS ON: [[never-synthesize-from-descriptions-alone|Never Synthesize from Descriptions Alone]]
- BUILDS ON: [[never-skip-stages-even-when-told-to-continue|Never Skip Stages Even When Told to Continue]]
- BUILDS ON: [[shallow-ingestion-is-systemic-not-isolated|Shallow Ingestion Is Systemic, Not Isolated]]
- BUILDS ON: [[infrastructure-must-be-reproducible-not-manual|Infrastructure Must Be Reproducible, Not Manual]]
- BUILDS ON: [[the-agent-must-practice-what-it-documents|The Agent Must Practice What It Documents]]
- BUILDS ON: [[models-are-built-in-layers-not-all-at-once|Models Are Built in Layers, Not All at Once]]
- RELATES TO: [[model-methodology|Model — Methodology]]
- RELATES TO: [[model-claude-code|Model — Claude Code]]
- RELATES TO: [[model-automation-pipelines|Model — Automation and Pipelines]]
- RELATES TO: [[skyscraper-pyramid-mountain|Skyscraper, Pyramid, Mountain]]

## Backlinks

[[harness-engineering|Harness Engineering]]
[[immune-system-rules|Immune System Rules]]
[[rework-prevention|Rework Prevention]]
[[deterministic-shell-llm-core|Deterministic Shell, LLM Core]]
[[never-synthesize-from-descriptions-alone|Never Synthesize from Descriptions Alone]]
[[never-skip-stages-even-when-told-to-continue|Never Skip Stages Even When Told to Continue]]
[[shallow-ingestion-is-systemic-not-isolated|Shallow Ingestion Is Systemic, Not Isolated]]
[[infrastructure-must-be-reproducible-not-manual|Infrastructure Must Be Reproducible, Not Manual]]
[[the-agent-must-practice-what-it-documents|The Agent Must Practice What It Documents]]
[[models-are-built-in-layers-not-all-at-once|Models Are Built in Layers, Not All at Once]]
[[model-methodology|Model — Methodology]]
[[model-claude-code|Model — Claude Code]]
[[model-automation-pipelines|Model — Automation and Pipelines]]
[[skyscraper-pyramid-mountain|Skyscraper, Pyramid, Mountain]]
[[E005-agent-compliance-framework|Agent Compliance Framework]]
[[agent-failure-taxonomy-seven-classes-of-behavioral-failure|Agent Failure Taxonomy — Seven Classes of Behavioral Failure]]
[[contribution-gating-cross-agent-inputs-before-work|Contribution Gating — Cross-Agent Inputs Before Work]]
[[coverage-blindness-modeling-only-what-you-know|Coverage Blindness — Modeling Only What You Know]]
[[aicp-active-state-mechanism-for-hooks|Decision — AICP Active-State Mechanism: `.aicp/state.yaml` Per-Repo with Git-Branch Fallback]]
[[pretooluse-hooks-layered-approach|Decision — Layered PreToolUse Hooks: Universal R01-R04 Baseline First, Stage-Gate Enforcement Later]]
[[defense-layer-progression-is-expensive|Defense Layer Progression Is Expensive — Prevention Is Cheap, Detection and Correction Are Milestones]]
[[harness-ownership-converges-independently-across-projects|Harness Ownership Converges Independently Across Projects]]
[[harness-owned-loop-deterministic-agent-execution|Harness-Owned Loop — Deterministic Agent Execution]]
[[if-you-can-verify-you-converge|If You Can Verify, You Converge]]
[[infrastructure-enforcement-proves-instructions-fail|Infrastructure Enforcement Proves Instructions Fail]]
[[methodology-evolution-protocol|Methodology Evolution Protocol]]
[[methodology-standards-initiative-gaps|Methodology Standards Initiative — Gap Analysis]]
[[methodology-standards-initiative-infrastructure|Methodology Standards Initiative — Infrastructure Analysis]]
[[model-local-ai|Model — Local AI ($0 Target)]]
[[model-markdown-as-iac|Model — Markdown as IaC — Design.md and Agent Configuration]]
[[model-sfif-architecture|Model — SFIF and Architecture]]
[[never-present-speculation-as-fact|Never Present Speculation as Fact]]
[[wiki-post-ingestion-operations-plan|Operations Plan — Wiki Post-Ingestion Validation]]
[[per-backend-circuit-breaker-with-failover-chain|Per-Backend Three-State Circuit Breaker with Failover-Chain Integration]]
[[per-day-jsonl-dlq-with-retry-budget|Per-Day JSONL Dead-Letter Queue with Retry Budget and Status Tracking]]
[[infrastructure-over-instructions-for-process-enforcement|Principle — Infrastructure Over Instructions for Process Enforcement]]
[[model-quality-failure-prevention-standards|Quality Standards — What Good Failure Prevention Looks Like]]
[[schema-aspirationalism-defining-required-sections-you-neve|Schema aspirationalism — defining required sections you never validate produces false confidence]]
[[src-code-review-graph-automated-review|Source — code-review-graph: Graph-Based Automated Code Review]]
[[standards-must-preach-by-example|Standards Must Preach by Example]]
[[E006-standards-by-example|Standards-by-Example]]
[[src-autobe-compiler-verified-backend-generation|Synthesis — AutoBE: Compiler-Verified Backend Generation]]
[[src-hrm-trm-tiny-recursion-models|Synthesis — HRM and TRM: Tiny Recursive Models Beat LLMs on ARC-AGI]]
[[src-llm-architecture-gallery-raschka|Synthesis — LLM Architecture Gallery (Raschka)]]
[[src-openarms-v10-enforcement|Synthesis — OpenArms v10 — Infrastructure Enforcement and Agent Behavior]]
[[src-pydantic-ai-typed-agent-framework|Synthesis — Pydantic AI: Typed Agent Framework]]
[[src-bmad-method-agile-ai-development-framework|Synthesis: BMAD-METHOD — Agile AI-Driven Development Framework]]
[[systemic-incompleteness-is-invisible-to-validation|Systemic Incompleteness Is Invisible to Validation]]
[[three-lines-of-defense-immune-system-for-agent-quality|Three Lines of Defense — Immune System for Agent Quality]]
[[three-permission-modes-think-edit-act|Three Permission Modes (Think / Edit / Act) — Operator-Selected AI Authority Tiers]]
[[tier-based-context-depth-trust-earned-through-approval-rates|Tier-Based Context Depth — Trust Earned Through Approval Rates]]
