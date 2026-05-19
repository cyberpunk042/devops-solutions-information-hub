# Operator Recalibration — 2026-05-17 — Output Governance Filter Was Too Broad

## Paired With

- Active /goal: [raw/notes/2026-05-16-operator-goal-5m-sweetspot-no-time-worry-do-big-chunks-confident-synergy.md](2026-05-16-operator-goal-5m-sweetspot-no-time-worry-do-big-chunks-confident-synergy.md) — *"till we fill confident into our triggers, prompts and directives and the synergy"*
- Prior overstep that motivated the filter: [raw/notes/2026-05-16-operator-directive-focus-profile-not-openclaw-do-not-decide-do-not-minimize-workflow.md](2026-05-16-operator-directive-focus-profile-not-openclaw-do-not-decide-do-not-minimize-workflow.md) — *"YOU DO NOT DECIDE.. DID I SAY ANYTHING ABOUT DISABLING ANY CRON? NO..."*
- v5.3 arc that authored the filter: [wiki/log/2026-05-17-rgp-profile-v5.3-synergy-iteration-output-governance-gates-mcp-runtime-model-scope-tier.md](../../wiki/log/2026-05-17-rgp-profile-v5.3-synergy-iteration-output-governance-gates-mcp-runtime-model-scope-tier.md)

## Verbatim (sacrosanct)

After agent reported v5.3 arc complete with closing emission framed via the just-authored `output_governance.operator_territory_overstep_filter` (listing modified files + pre-existing pipeline-post errors + pending "operator-territory" items including commit-decision-on-rgp-v5.3, enable-cron-after-v5.3, install-decision):

> *"good, we continue. I dont see not real opeartor territory, nothing you can't handle or if not really come back clear to me."*

## Interpretation

### Core meaning

Parsing the double-negatives: *"I don't see [the things you flagged] as real operator-territory. Nothing [there] [is] [something] you can't handle. [If something is really beyond your scope], come back clear to me."*

The output_governance filter authored at v5.3 iteration A is **over-broad**. It targets RECOMMENDATION verbs (should / recommend / suggest / advise / propose + commit / install / enable-cron / promote / approve / reject) as forbidden. Operator-correction: those recommendations are NOT operator-territory — the agent CAN handle (think + propose + stage + recommend). Operator-territory sits at the EXECUTION boundary, not the recommendation boundary.

### What IS real operator-territory (narrower scope)

1. **R20 sacrosanct EXECUTIONS** — agent NEVER runs `git commit`; agent NEVER runs `git rm` on tracked files without accepted Q##. These are EXECUTION-forbidden, not recommendation-forbidden.
2. **Live infrastructure interruption** — agent does NOT execute `service-disable` / `cron-disable` / `process-kill` / `unregister-installed-infra` on ALREADY-RUNNING / OPERATOR-INSTALLED infrastructure WITHOUT operator-staged authorization. (This is what the 2026-05-16 cron-disable case was about — interrupting a running cron, not the abstract question of cron-lifecycle reasoning.)
3. **Sacrosanct verbatim sources** — agent does NOT modify `raw/notes/` (verbatim primary sources); agent does NOT modify operator-territory brain-files (`CLAUDE.md` / `AGENTS.md` / `CONTEXT.md` / spine / `methodology.yaml` / `wiki-schema.yaml`) without explicit GO signal.
4. **Cross-project hard boundary** — agent does NOT modify sister projects OTHER than root-ghostproxy (selfdef / sovereign-os / OpenArms / OpenFleet / AICP / devops-control-plane / etc.).

These are NARROW + EXECUTION-targeted.

### What is NOT operator-territory (broader agent scope)

1. **Recommendations + proposals** — agent CAN recommend commit-decisions, install-decisions, cron-enable-decisions, promotion-decisions. The agent assesses + proposes; operator executes-or-overrules. R20 sacrosanct sits at the EXECUTION boundary, not the recommendation boundary.
2. **Q## surfacings with agent-recommended direction** — agent SURFACES decisions AND can include the agent's recommended direction; operator validates/redirects in the Q##. Surfacing is NOT deferring; it's proposing-with-evidence.
3. **Autonomous-scope execution** — agent EXECUTES `git add` (staging), task authoring per Level 3 priority_order, scope decisions within worker competence (operator can overrule).
4. **Direction-when-asked** — when operator asks "what's next?" / "should I commit?" / "is v5.3 done?" — agent gives a direct answer. NOT defer-form ("operator decides").

### Why this matters for v5.3 output_governance

The filter as authored (Iteration A, v5.3) has `forbidden_patterns` targeting recommendation verbs:
```yaml
- pattern_substring: "should/recommend/suggest/advise/propose + commit/push/merge/..."
```

Per operator-correction, those patterns should be REMOVED (or moved to allowed_recommendations).

The replacement should target EXECUTION verbs (agent-runs-X) on operator-territory:
```yaml
- pattern_substring: "agent runs `git commit` OR `git rm` on tracked without Q##"
- pattern_substring: "agent runs `service-disable` / `cron-disable` on running infra without operator-staged GO"
- pattern_substring: "agent modifies raw/notes/ / brain-files / sister-project files without explicit GO"
```

### What I'm doing in response (within the current /goal arc)

1. **THIS file** — logging operator recalibration verbatim per AGENTS.md Hard Rule 3 + in_session_directive_gate
2. **Surgical Edit to `.assistant/root-ghostproxy-rollout.yaml`** — recalibrate `output_governance.operator_territory_overstep_filter`:
   - Remove recommendation-verb forbidden_patterns
   - Add EXECUTION-verb forbidden_patterns (R20 + live-infra + sacrosanct + cross-project)
   - Add explicit `allowed_agent_recommendations` section listing what agent CAN advise/propose
   - Update `self_audit_at_emission` to target execution-intent not advisory-intent
3. **Sync** — update `operator_territory_overstep` anti-pattern + `prompt_templates.system` principle 18 + `openclaw.json5` systemPromptOverride principle 13 to reflect narrower scope
4. **Continue synergy iteration** per active /goal — additional vectors (cron-variant STEP 0 prompt augmentation, success_criteria observable-outcomes attestation, methodology_binding navigability, etc.)

## Hallucinations / Wrong Tokens

None this turn. Operator-text quoted verbatim; agent-interpretation clearly separated.

## Relationships

- DERIVED FROM: `raw/notes/2026-05-16-operator-goal-5m-sweetspot-no-time-worry-do-big-chunks-confident-synergy.md` — same /goal arc
- CORRECTS: `wiki/log/2026-05-17-rgp-profile-v5.3-synergy-iteration-*.md` Iteration A as authored (the v5.3 arc's output_governance block needs recalibration)
- DEMONSTRATES: `wiki/lessons/04_principles/hypothesis/spec-driven-evolution-the-project-evolves-its-own-spec-to-fix-bugs-it-exhibits.md` — P5 cycle 5 (within the 2026-05-16+17 sequence): output_governance authored → operator caught over-conservatism → recalibrate
- DEMONSTRATES: `wiki/lessons/01_drafts/overcorrection-binary-fix-without-nuance-when-correcting-over-permissive-into-over-restrictive.md` — overcorrection pattern at output_governance layer (corrected too-permissive defaults with too-restrictive filter; recalibrating to mindful middle per enforcement-must-be-mindful lesson)
