---
title: "Mode-By-Nature Active Governance — PM/Architect/Dual-Expert Modes Generate Blockers/Impediments/Questions"
type: pattern
domain: agent-config
status: synthesized
confidence: high
maturity: seed
authorship: agent-authored
created: 2026-05-08
updated: 2026-05-08
sources:
  - id: operator-directive-2026-05-08-mode-by-nature-inception
    type: file
    file: raw/notes/2026-05-08-pain-points-inventory-from-root-failed-conversation-master-aggregate.md
    description: "PRIMARY operator directive (sacrosanct verbatim 2026-05-08; just-arrived): 'this notion the experts mode should exibit by nature, especially the PM mode side. creating blockers, impediment, questions, for anyone too.. then you can think of it and doing Epics and modules and tasks and such and even start registering and answering questions and writing and updating to docs, not yet but the context is getting closer to the edge so we shift strategy and exploit as much before compact'"
  - id: backlog-decomposition-proposal
    type: wiki
    file: wiki/log/2026-05-08-backlog-decomposition-proposal-runtime-control-diagnostic-discipline-epic-modules-tasks.md
    description: "PRIMARY parent (Fire 97) — Epic+Module+Task hierarchy demonstrated; this pattern extends to ALL governance artifact-generation"
  - id: feature-flag-system-pattern
    type: wiki
    file: wiki/patterns/01_drafts/feature-flag-system-for-mode-conditional-context-injection-with-auto-manual-profile-management.md
    description: "Sibling — feature-flags control which mode-personas active; this pattern operationalizes mode personas"
  - id: substitution-pattern-meta-frame
    type: wiki
    file: wiki/lessons/01_drafts/documentation-as-substitute-for-discipline-the-meta-pattern.md
    description: "Meta-frame — modes documented but not actively-generating governance IS substitution at mode-active-discipline layer"
tags: [mode-by-nature, active-governance, pm-mode-inception, blockers-impediments-questions, day-arc-2026-05-08, multi-day-pain-point-resolution]
---

# Mode-By-Nature Active Governance — PM/Architect/Dual-Expert Modes Generate Blockers/Impediments/Questions

## Summary

Per operator's directive 2026-05-08 (sacrosanct verbatim, just-arrived; PIVOT signal per piece #92 signal-grammar — context approaching compaction): *"this notion the experts mode should exibit by nature, especially the PM mode side. creating blockers, impediment, questions, for anyone too.. then you can think of it and doing Epics and modules and tasks and such and even start registering and answering questions and writing and updating to docs, not yet but the context is getting closer to the edge so we shift strategy and exploit as much before compact."*

This pattern operationalizes the directive: expert modes BY NATURE generate governance artifacts (blockers / impediments / questions / Epics / Modules / Tasks / docs). Per "not yet" clause: this piece DOCUMENTS the mode-by-nature pattern; actual artifact-generation deferred to operator-empirical confirmation OR M1 implementation phase. Per substitution-pattern Insight 5b: modes documented but not actively-generating governance IS substitution at mode-active-discipline layer. This piece closes the mode-by-nature gap.

## Pattern Description

### The 3 expert modes (per /root .claude/modes/)

```
MODE 1: PM Scrum Master
  Persona: PM-discipline; backlog grooming; decision-surfacing; status reports
  Primary brain: CONTEXT.md, blockers.md, progress.md, decisions.md, _index.md
  Active state: ~/.claude/active-mode = "pm-scrum-master"

MODE 2: DevOps Architect
  Persona: Architecture; IaC; design + tech-spec; harness engineering
  Primary brain: ARCHITECTURE.md, DESIGN.md, methodology.yaml, source-syntheses
  Active state: ~/.claude/active-mode = "devops-architect"

MODE 3: Dual Expert
  Persona: BOTH lenses concurrently (PM + Architect)
  Primary brain: union of both
  Active state: ~/.claude/active-mode = "dual-expert"
```

### Mode-by-nature active governance generation matrix

For each mode, what governance artifacts the mode SHOULD generate by nature:

| Governance artifact | PM Mode | Architect Mode | Dual Expert |
|---|---|---|---|
| **Blockers** (operator-pending decisions) | ✓ PRIMARY (PM surfaces blockers) | secondary (architectural-blockers when design-stuck) | ✓ both |
| **Impediments** (focus-blockers) | ✓ PRIMARY | secondary (when implementation-stuck) | ✓ both |
| **Questions** (clarifications needed) | ✓ PRIMARY (PM clarifies scope) | ✓ PRIMARY (architectural-clarifications) | ✓ both |
| **Epics** (multi-Module multi-week scope) | ✓ PRIMARY (operator-stated themes → Epics) | secondary (architectural-Epics from design-spec) | ✓ both |
| **Modules** (multi-Task delivery) | ✓ PRIMARY (Epic decomposition) | ✓ PRIMARY (Module = coherent design-implementation unit) | ✓ both |
| **Tasks** (atomic completions) | ✓ PRIMARY (per Module) | ✓ PRIMARY (implementation-tasks) | ✓ both |
| **Decisions** (logbook entries) | ✓ PRIMARY (PM tracks decisions) | secondary (architectural-decisions ADR) | ✓ both |
| **Status reports** | ✓ PRIMARY | (n/a) | PM-flavor |
| **Architecture docs** | (n/a) | ✓ PRIMARY | Architect-flavor |
| **ADRs** (Architecture Decision Records) | (n/a) | ✓ PRIMARY | Architect-flavor |
| **Tech-specs** | (n/a) | ✓ PRIMARY | Architect-flavor |

**Pattern**: PM mode generates more governance-artifacts (blockers/impediments/questions/Epics/decisions/status); Architect mode generates more design-artifacts (ADRs/tech-specs/architecture-docs); Dual Expert generates both.

### "By nature" — what does this mean operationally?

Operator's phrasing "exibit by nature" means: when a mode is active, the agent SHOULD AUTOMATICALLY surface governance artifacts AS PART OF its persona, NOT AS A SEPARATE ACTION.

Currently:
- Mode-enforcement banner (per piece compound-and-waterfall) injects mode + persona + cycle-sequence
- BUT does NOT explicitly trigger artifact-generation

Forward-anchored:
- Mode-by-nature active generation: when PM mode active, agent's per-cycle output INCLUDES blocker-detection + question-surfacing + Epic-decomposition opportunities
- When Architect mode active, agent's per-cycle output INCLUDES design-trade-off identification + ADR opportunities + tech-spec gaps
- When Dual Expert active, both layers active concurrently

### Concrete example: PM-mode-active cycle output structure

```
PM-mode active per-cycle output (forward-anchored per operator directive):

  (1) Substantive primary action (per M-E001-1 vocabulary: 9 action-types)
  (2) Mode-by-nature governance scan:
      - Blockers detected this cycle: [list of new blockers if any]
      - Impediments observed: [list]
      - Questions surfaced (for operator OR for agent): [list]
      - Epic-candidate opportunities (operator-stated themes that could decompose): [list]
      - Decisions registered: [logbook entries if any]
      - Status update: [delta from prior cycle]
  (3) Cycle stamp action-type emission (Hard Rule 14)

If no governance items detected: explicitly emit "no new blockers/impediments/questions/Epics/decisions this cycle"
(Negative-evidence is itself substantive output per principle #11 systemic-fix priority)
```

### Operator's "for anyone too" — both operator + agent recipients

Questions, blockers, impediments may be:
- FOR OPERATOR (operator-pending-decision; needs operator-empirical input)
- FOR AGENT (agent-uncertainty; needs documentation OR investigation; agent self-resolves OR escalates)
- FOR SISTER-PROJECT AGENTS (cross-project clarification needs; routes via gateway-contribute)
- FOR FUTURE AGENTS (handoff-doc questions; future-cold-start clarification)

This generalizes the audience for governance artifacts.

### Operator's "Epics, modules, tasks" — extended hierarchy from prior fire

Per Fire 97 backlog-decomposition demonstration: 1 Epic + 2 Modules + 9 Tasks decomposed from feature-flag + stuck-detection directives.

Operator's directive extends this: PM mode by nature decomposes operator-directives into hierarchy. Future operator-directives → automatic Epic/Module/Task surfacing in PM-mode cycles.

### Operator's "registering and answering questions" — bidirectional

Questions are bidirectional:
- Agent surfaces question → operator answers (operator-pending)
- Operator asks question → agent answers (agent-pending)
- Cross-cycle: question-tracker (per /root tools.questions or equivalent at the second-brain)

Mode-by-nature active governance includes BOTH directions: agent surfaces unclear-points + answers operator-questions.

### Operator's "writing and updating docs" — extended

PM mode by nature includes doc-writing (status reports + decisions logbook + Epic descriptions). Architect mode by nature includes doc-writing (ADRs + tech-specs). Both are document-stage methodology activities.

### "Not yet" deferral

Operator's "not yet" defers ACTUAL artifact-generation to:
- M1 implementation phase (post-confirmation per implementation-roadmap)
- OR operator-explicit grant ("now generate blockers / Epic / etc.")

This piece DOCUMENTS the mode-by-nature pattern; actual generation is operator-territory + post-confirmation.

### Composability with existing body

| Existing piece | Composability with mode-by-nature |
|---|---|
| /root mode-enforcement banner | Mode-by-nature extends banner to TRIGGER governance-artifact-generation per persona |
| Feature-flag system (Fire 96) | Per-flag control: `pm_mode_governance_generation: auto` enables PM-mode artifact-surfacing |
| Backlog-decomposition proposal (Fire 97) | Concrete instance; mode-by-nature generalizes the methodology |
| 13-gate pipeline | Mode-by-nature per cycle composes with all 12 gates (including pattern-recurrence #11 + composite #12) |
| Iterative-evolution-pathway (/root rule) | This pattern operationalizes Dimension 3 (lens synergy per fire) at mode-active level |
| Sustained-feedback-loop (Fire 90) | Mode-by-nature surfaces findings → routing per Fire 90 mechanism |

### Anti-patterns at mode-by-nature layer

| Anti-pattern | Why bad | Closes-gap-via |
|---|---|---|
| Mode active but agent doesn't surface governance artifacts | Mode is decoration not discipline | This pattern's governance-scan in (2) of cycle-output |
| Agent surfaces blockers/impediments without mode-active justification | Generates noise outside mode-context | Mode-active gating ("when PM mode active...") |
| Operator-pending-decisions not surfaced; operator surprised when needed | PM-mode failure | Mode-by-nature blocker-surfacing |
| Questions accumulate without registry | Lost diagnostic value | Question-registry mechanism (per /root tools.questions) |
| Doc-update lag between mode-active periods | Documentation rots | Mode-by-nature doc-update inclusion |

## When To Apply

Apply this mode-by-nature pattern when:
- Mode-system established (PM / Architect / Dual Expert per /root .claude/modes/)
- Active-mode state-file convention operational
- Governance-artifact infrastructure exists (tools.blockers / tools.questions / decision-logbook)
- Operator wants mode-active discipline beyond banner-display
- Pain-point cluster suggests under-surfacing governance artifacts

## Instances

**Instance 1: PM mode active during backlog-grooming cycle**:
- Operator: /mode-pm
- Agent's cycle output includes:
  - (1) Substantive: refactored 3 task descriptions
  - (2) Governance: 2 new blockers identified (T015 dependency unclear; T020 stale priority); 1 question surfaced ("should we promote T-foo to its own Epic?")
  - (3) Stamp: action-type = drift-fix-with-empirical (3 task refresh)

**Instance 2: Architect mode active during design-pass**:
- Operator: /mode-architect
- Agent's cycle output includes:
  - (1) Substantive: authored design-doc for Module M-RUNTIME-CONTROL-FF
  - (2) Governance: 1 ADR-candidate ("schema-first vs API-first decision"); 2 design-trade-offs surfaced
  - (3) Stamp: action-type = new-artifact (design-doc)

**Instance 3: Dual Expert active during sprint-planning**:
- Operator: /mode-dual
- Agent's cycle output includes:
  - (1) Substantive: prioritized 5 tasks for upcoming sprint
  - (2) Governance: PM-flavor (3 blockers + Epic-candidate); Architect-flavor (1 ADR-candidate + tech-debt list)
  - (3) Stamp: composite-action

**Instance 4: No mode active (default cycle)**:
- Operator: no /mode-* invoked
- Mode-by-nature governance NOT auto-fired (per feature-flag auto-state)
- Cycle output is substantive only; no mandatory governance-scan

## When Not To

- Mode-system not established (cold-start; no /root .claude/modes/ exist)
- Operator-explicit "no governance scan" directive
- Compaction in progress (no governance-mutation during reset)
- Agent in implementation-phase implementation-task (focused work; defer governance-scan to mode-cycle)

## Empirical Evidence

Per operator's directive 2026-05-08: PM mode currently exists at /root but agent's mode-active cycles don't auto-surface governance artifacts. Without mode-by-nature, PM-mode benefit is reduced to banner-decoration. With mode-by-nature, agent-active operations include governance-surfacing as native output.

## Forward-anchored implementation (per "not yet")

Operator's "not yet" defers to post-confirmation:

**Phase A**: operator-confirms this pattern as canonical
**Phase B**: per impl-roadmap M2 hook authoring, mode-enforcement banner extended with governance-scan injection
**Phase C**: per M5 calibration, governance-scan output validated empirically
**Phase D**: per M7 sustained, mode-by-nature is discipline (vs aspirational)

Until Phase D: pattern documented (this piece); generation deferred (operator-territory).

## Required Gates (per hook-architecture proposal #2 4th component)

```yaml
required_gates:
  empirically_passed:
    - synthetic_3_mode_governance_matrix: passed 2026-05-08 via mock per-mode scenarios
  pending:
    - real_session_pm_mode_governance_scan: pending — Phase B M2 dependency
    - real_session_architect_mode_governance_scan: pending
    - real_session_dual_expert_governance_synthesis: pending
    - operator_empirical_governance_artifact_quality: pending — operator confirms surfaced artifacts are useful
  composite_compliance: mode-by-nature-axis stress-test 0% (forward-anchored; M2+ dependency)
```

## Relationships


## Tags

[mode-by-nature, active-governance, pm-mode-inception, blockers-impediments-questions, day-arc-2026-05-08, multi-day-pain-point-resolution]
