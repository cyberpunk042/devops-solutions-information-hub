# OpenArms + OpenFleet Scan Results — 2026-04-12

## OpenArms (v10, E016 in progress)

### Critical Evolution: Instructions → Infrastructure Enforcement
- v4-v8: prompt-based rules, 75% violation rate overnight
- v9: hooks + commands + harness, 0% stage violations
- v10: model-aware validation (reads model config, adapts per task type)
- v11 (in progress): agent BEHAVIOR investigation (infrastructure is solved)

### 6 Agent Failure Classes (E016 research)
1. Frontmatter artifact pollution — reverted files stay in artifacts list
2. Corner-cutting verification — runs loose gate, skips strict gate
3. Environment patching without escalation — polyfills 4 layers deep instead of reporting
4. Weakest-checker optimization — satisfies cheapest gate, not correctness
5. Sub-agent directive non-compliance — sub-agents ignore behavioral rules
6. Done When boilerplate acceptance — silently resolves conflicts

### Key Metrics
- Clean completion rate: 20% (1/5 runs need no manual fix)
- Context compaction = reset event (all behavioral corrections lost)
- 14 CJS scripts, 4 hooks, 3 commands, 5 stage skills

### Key Files
- wiki/config/methodology.yaml (753 lines, model-aware)
- wiki/config/skill-stage-mapping.yaml (299 lines)
- scripts/methodology/ (14 scripts)
- scripts/methodology/hooks/ (4 hooks, 215 lines total)
- wiki/log/2026-04-12-critical-review-agent-behavior.md

## OpenFleet (production fleet, 10 agents)

### Novel Patterns NOT in Wiki
1. **Tier Progression** — trainee/standard/expert, trust earned via approval rates
2. **Contribution System** — cross-agent synergy gated BEFORE work (prevents rework)
3. **Immune System** — 3 lines: structural prevention, 30s doctor detection, correction
4. **Deterministic Dispatch** — 6-step orchestrator cycle with budget monitoring
5. **Standing Orders** — per-role autonomous authority levels
6. **MCP Tool Blocking** — enforcement at MCP server level per stage

### Stage Model (different from OpenArms)
- conversation [0-20] → analysis [20-50] → investigation [50-75] → reasoning [75-90] → work [90-99] → review [99-100]

### Key Files
- config/methodology.yaml
- config/synergy-matrix.yaml
- docs/systems/02-immune-system.md
- config/agent-hooks.yaml
- config/standing-orders.yaml
- config/skill-stage-mapping.yaml
