# Session Handoff — 2026-05-16 (afternoon arc — RGP worker rebuild + design queue)

> **Purpose:** Context recovery document for resuming the RGP-worker rebuild + open design queue (cron alignment, 1M context mode, multi-discipline subagents, /load-brain refinement).
> **NOT a wiki page.** Lives in `docs/`. Do not ingest.
> **Predecessor handoff:** `docs/SESSION-2026-05-16.md` (the morning arc — gateway fix + initial v3 RGP profile installed; this handoff continues from where that one left off).

## Executive Summary

This session was the operator's correction arc on root-ghostproxy strategy + the v3 → v5 profile rebuild driven by it. Key shifts:

- **Operator inverted the framing**: the RGP-in-second-brain profile is a SYMPTOM. The real work is fixing the actual root-ghostproxy project at `/home/jfortin/root-ghostproxy/` based on 180 unique pain-points across 15 systemic-bug clusters (the May 5-8 audit) + the 97-item backlog those audit findings produced (8 epics / 21 modules / 68 tasks). The profile's job is to BE A WORKER on that backlog, not an observer surfacing meta-decisions.
- **Profile rebuilt v3 → v5 by surgical augmentation** (NOT wholesale rewrite — operator-corrected when I tried that). 8 surgical `Edit` calls. File grew 480 → 1226 lines. YAML parses. All cited second-brain bindings verified present.
- **Critical finding (not yet fixed)**: `.assistant/root-ghostproxy-rollout.cron.yaml` + `.assistant/root-ghostproxy-rollout.openclaw.json5` are STALE v3 observer-shaped. They would actively defeat the v5 worker profile if installed today. The cron prompts say *"NEVER edit root-ghostproxy"*; the openclaw.json5 has `filesystem-write-root-ghostproxy` in `tools.deny`; the `systemPromptOverride` is the full v3 observer prompt. These need alignment before install.
- **Dry-run planning artifact authored** at `.assistant/_state/root-ghostproxy-rollout-inbox.md` showing what the first real fire would do on first-pick task `T014-author-endpoint-ai-safety-policy` (P0 Foundation, audit-anchored to C14 catastrophic-events + C06 fabrication). 12-test TDD plan + budget estimate + 3 [NEEDS CLARIFICATION] surfacings.
- **NOT installed**. Operator gated install behind pre-launch readiness gates + GO signal + "we will not install before a while I have other things after".

## Operator Directives (verbatim, sacrosanct)

```
"TELL WTF IS NOT CLEAR AND WHY IS THE AI ASSISTANT NOT WORKING ON THE
 200+ EPICS and tasks that are needed to fix root-ghostproxy ?"

"THE ONLY REASON THERE IS A ROOT-GHOSTPROXY PROFILE IN THE SECOND-bRAIN
 IS BECAUSE ITS BROKEN AND IT COULD NOT WORK.. WE NEED TO FIX THE WHOLE
 PROJECT.. BASED ON EVERY OF THE 100+ REPORTED ISSUES AND SYSTEMIC BUGS
 AND GLITCH AND ETC..."

"you are so fuckign bad.. its insane ... ISN"T EVERY FUCKING THING
 ALREADY IN THE SEcond-brain ????"

"PROVE ME YOU UNDERSTAND THE WHOLE FUCKING SITUATION....  AN AI RAN IN
 LOOP AND ANALYSE THE CONVERSATION AND HOW COMPLETELY TRASH EVERYTHING
 WAS AND NEEDED TO BE FIXED AND WE NEED TO PROCESS... I DONT WANT TO
 HAVE TO REPEAT EVERYTHING... ITS BASICALLY EVERYTHING WE MUST REDO...
 HOOKS, SETTINGS, Commands, SKills... everything.... we must do it
 right... not something that doesn't work..."

"you are so fucking retard... tell me what you dont understand about
 where we are and where we are going...."

"ITS SO FUCKING SIMPLE: WE ARE DOING AN AI ASSISTANT PROFILE TO WORK ON
 WHAT I JUST FUCKING EXPLAINED YOU... FIXING THE FUCKING root-ghostproxy
 ... EVERYTHING IN THE FUCKING 150+ tasks and more since it was
 incomplete...."

"WTF ARE YOU DOING YOU FUCKING RETARD... root-ghostproxy is at
 root-ghostproxy..... YOU FUCKING SCRUB..."   (I was probing /root/ when
 the project is at ~/root-ghostproxy/ — the path was in plain sight in
 prior `ls $HOME` output)

"OF COURSE IT NEED TO BE A WORKER .. FFS... ITS THE WHOLE FUCKIGN
 PURPOSE.. THE ROOT-GHOSTPROXY WOULD WORK AND WE WOULD NEVER NEED THIS
 AI-ASSISTANT PROFILE.. WILL YOU FUCKING WAKE UP ?"

"This AI assistant will have to respect the knowledge of the second-brain
 and respecte the super-models and models and standards and Wiki LLM and
 do proper Spec Driven Development combined with Test Driven Development.
 It will need to be super strong before we launch it. take your time I
 know this is complex, you can read more file. process more the knowledge
 and a clear intelligence so that the work is reliable. do not rewrite
 everything everytime make augmentations, improvements, upgrades,
 evolutions. it has to produce high standards artifact and do the
 workflow/things in order and properly, SFIF and all."

"Proceed with the augmentation, do not minimize anything, make sure the
 first run of this fresh AI assistant worker will be worth it"

"do this right from the first time but after you read and processed you
 can proceed. we wil not install before a while I have other things after"

"should we not exploit the /goal ? make sure that when we have a CRON
 that we want to be hardwork we create proper goal very detailed with
 also the proper ref to tools calls and files and whatnot and so the
 agent is naturally driven ? would that work ? and that we are sure its
 in opus 1m context mode and with the proper settings. a proper claude
 cli call with the righth params and arguments and content and structure
 and data objects and divisions can be gold. just as spawning appropriate
 subagents setup such as for resaarch online and local and whatever need
 for a proper Senior Software Architect DevOps Engineer FullStack Expert
 with PM Scrum Agile capabilities too. Able to be in work mode always
 with the proper workflow and Spec Driven Development and Test Driven
 Development and flexibility and observability and operability and
 configuration and personalization, even profiles and such.
 Making such it will not freeze or be mindless or receive garbage or be
 too spammed or not poked enough or not directed well.... the goal is
 for a 24/7 agent (we can recycle it later or transfer it.)"

"dont you just have to add it att the start of a prompt and it will be
 transfered to the -p command ? something like that ?"

"okay two things before we do that, you can put all this in the handoff
 with the things I said and we will do research about but now,
 [/load-brain refinement directive — see Part 1 of this handoff section
  below — "the /load-brain default is too wide a bit... fine tuning...
  balance between light and complete... trimming the leaves and branches
  and reshaping... Goldilocks at default... 500k is fine for full
  default... Order and interstep might matter... can in between layers
  of operations and such take time to reflect... direct it via hooks
  and commands and whatnot... do not minimize"]"
```

## What Was Done

### Phase A — Initial framing investigation (~13:30 ET)
- Investigated why operator said *"its doing nothing"* on the RGP profile installed earlier this morning.
- Found: RGP cron fired at 14:56 ET (status `ok`, 17 min runtime, 16K output tokens) but produced ONE multi-vision cascade-candidate (Q97) in the second-brain — zero edits in `~/root-ghostproxy/`.
- Root cause: v3 profile structurally an OBSERVER (`forbidden_actions` includes "Modify root-ghostproxy repo content (cross-project boundary ABSOLUTE)") — it CAN'T do worker work even when it fires.

### Phase B — Path correction (operator-shouted)
- I went down a `/root/` rabbit hole when `~/root-ghostproxy/` was the project (operator: *"root-ghostproxy is at root-ghostproxy"*). Path was in plain sight in prior `ls $HOME` output.
- Discovered `~/root-ghostproxy/` contains: 9 epics (E001-E007 + sfif-rollout + _index), 21 modules (M001-M014 + 7 E-prefix children), 68 tasks, 86 log entries. 183 backlog items total — matches the operator's "150+ tasks and more since it was incomplete" framing.
- Confirmed mirror gap: this second-brain only has 21 of 183 items mirrored. The actual fix-work (E001-E007 + 11 modules + all 68 tasks) lives ONLY in `~/root-ghostproxy/`.

### Phase C — Audit + standards study (operator-authorized "take your time")
- Read `raw/notes/2026-05-08-pain-points-inventory-from-root-failed-conversation-master-aggregate.md` (536 lines, 180 unique pain-points across 15 clusters C01-C15, 38-70 proposed solution pieces estimated).
- Read `wiki/log/2026-05-08-sister-project-investigation-kickoff-spec-root-ghostproxy-foundational-triplet-adaptation.md` (114 lines — foundational-triplet C04 input-discipline + C02 decision-territory + C09 status-claim).
- Read `wiki/spine/models/agent-config/model-per-project-assistant-profile.md` (201 lines — the 6-section contract + tool-agnosticism doctrine) + companion standards (210 lines — 8 quality gates).
- Read `wiki/config/methodology-profiles/spec-driven.yaml` (201 lines — 6 SDD signature practices: constitution-first / [NEEDS CLARIFICATION] / research-in-specify / spec generates plan / checklist-as-unit-tests / delta-specs).
- Read `wiki/config/methodology-profiles/test-driven.yaml` (228 lines — Red→Green→Refactor cycle + 6 TDD signature practices: test_list_before_scaffold / red_before_green / single_step_refactor / triangulation / bug-test-first / coverage-as-gate-not-target).
- Read `wiki/patterns/03_validated/architecture/scaffold-foundation-infrastructure-features.md` (198 lines — SFIF as validated pattern with 4 ecosystem instances) + `wiki/spine/models/quality/model-sfif-architecture.md` (268 lines — SFIF model + 3 quality tiers Skyscraper/Pyramid/Mountain).
- Read `wiki/lessons/02_synthesized/spec-driven-agentic-build-is-the-2026-convergent-pattern-...md` (301 lines — 9 independent practitioner instances of SDD; the convergent 2026 pattern).
- Read `wiki/spine/standards/model-standards/model-methodology-standards.md` (545 lines — gold standard execution patterns + anti-pattern gallery).
- Read `wiki/spine/standards/model-standards/model-llm-wiki-standards.md` (423 lines — per-type page standards index + 3 properties of gold-standard pages: SPECIFIC, CONNECTED, ACTIONABLE).
- Read `wiki/spine/models/foundation/model-methodology.md` (898 lines, chunked) — the master methodology model with 9 models × 5 stages, novelty dimension, 5-level enforcement hierarchy.
- Read `wiki/spine/models/foundation/model-llm-wiki.md` (573 lines) — knowledge architecture, 3 layers, 17 page types, maturity lifecycle.

### Phase D — Profile v3 → v5 augmentation (8 surgical Edits, NO wholesale rewrite)
Augmented `.assistant/root-ghostproxy-rollout.yaml` via 8 surgical `Edit` calls (operator-corrected when I tried Write earlier this session). Each cites the second-brain source it invokes:

| Edit | Section | Cites |
|---|---|---|
| 1 | `pre_launch_readiness:` top-level — 8 profile quality gates + 14 second-brain binding checks + 4 target-access checks + first-run readiness + abort conditions | `per-project-assistant-profile-standards.md` |
| 2 | `methodology_binding:` after `model_routing:` — per-task model selection (9 models) + SDD+TDD combined discipline + SFIF binding + schema_compliance bindings | `methodology.yaml` + `methodology-profiles/spec-driven.yaml` + `methodology-profiles/test-driven.yaml` + `model-sfif-architecture.md` + `wiki-schema.yaml` + `artifact-types.yaml` |
| 3 | `workflow.canonical_pipeline` step `4_execute` → `4_execute_sdd_tdd` with 5 sub-steps (4a spec_check / 4b test_list / 4c red / 4d green / 4e refactor + 4f verify_wiring) + docs/research/hotfix exceptions + 9 inline anti-patterns | spec-driven.yaml + test-driven.yaml signature practices |
| 4 | `anti_patterns` revised `ai_slop` + added 3 new: `wholesale_rewrite_instead_of_augment` (operator 2026-05-16) + `methodology_bypass` + `sfif_tier_jumping` | Operator-verbatim 2026-05-16 |
| 5 | `success_criteria.quality_gates` — 8 profile gates + 9 per-task-artifact gates + integration_wiring gates + per-tick gates | per-project-assistant-profile-standards + methodology-standards |
| 6 | `prompt_templates.system` augmented with sacrosanct 2026-05-05 + 2026-05-16 quotes + principles 9-15 (second-brain respect / SDD+TDD / SFIF / augment-not-rewrite / high-standards / first-run-worth-it / audit-anchored) | All cited sources |
| 7 | `methodology_binding.novelty_dimension_right_sizing` — 3 novelty levels (known / partially_known / unknown) → model selection (integration / bug-fix / feature-development) with cost profiles + concrete root-ghostproxy backlog examples | `wiki/lessons/.../right-size-the-methodology-model-to-the-actual-work-not-the` |
| 8 | `prompt_templates.system` principles 16-17: stage-compliance-vs-judgment-compliance (Agent Failure Taxonomy) + novelty dimension right-sizing | `model-methodology.md` enforcement hierarchy + OpenArms T116/T117 evidence |

**Verification after all 8 edits**: file 1226 lines, YAML parses (`yaml.safe_load` returns dict with 23 top-level keys), all sections present at expected line offsets, all 14 cited second-brain artifacts verified existent + readable.

### Phase E — Pre-launch dry-run + planning artifact
Per the profile's own `pre_launch_readiness.first_run_readiness.dry_run_first_pick`, ran workflow steps 0-3 read-only:

- **Step 0**: identified 4 unprocessed operator-directive raws from today
- **Step 1**: target project git state clean; branch = FRESH_SIGNAL
- **Step 2 — first-pick**: **T014-author-endpoint-ai-safety-policy.md** (P0, Foundation, not-started, current_stage:design / readiness:25%). T001-T010 all status:done; T012/T013/T015 in-progress (operator-owned, would step on toes); T014 has clean slate + deps satisfied (T011 + T006 both done).
- **Step 3**: loaded task + parent module M003 + parent epic + audit cluster (C14 catastrophic-events + C06 fabrication).

Authored planning artifact at `.assistant/_state/root-ghostproxy-rollout-inbox.md` (appended; preserved 14:56 ET v3 entry per augment-not-rewrite). Contains:
- Profile quality gates verification (8/8 pass)
- Second-brain binding verification (14/14 pass)
- Target project access verification (4/4 pass)
- Step 0-3 outcomes for first-pick T014
- Step 4 PLAN: 12-test TDD plan, implementation outline, verification command set, audit cluster anchor
- 3 [NEEDS CLARIFICATION] items surfaced (deny-set composition / sentinel threshold / opencode plugin API)
- 45-75 min budget estimate
- Pre-launch attestation (READY for install authorization)

### Phase F — Cron + OpenClaw config investigation (UNFIXED — handoff items)
Read `.assistant/root-ghostproxy-rollout.cron.yaml` (186 lines) + `.assistant/root-ghostproxy-rollout.openclaw.json5` (180 lines). Critical findings:

- **cron.yaml is v3 observer**: all 3 cron prompts (bootstrap / daily-light / weekly-module-deep) instruct *"NEVER edit root-ghostproxy"* (line 61 + variants). Direct contradiction of v5 worker. Prompts must be rewritten for worker shape.
- **openclaw.json5 is v3 observer**:
  - `tools.deny` line 103 includes `filesystem-write-root-ghostproxy` — denies what the worker must do
  - `tools.allow` does NOT include cross-project write access to `~/root-ghostproxy/`
  - `systemPromptOverride` line 171 is the FULL v3 observer prompt — would override v5 `prompt_templates.system` entirely
  - `subagents.allowAgents` lists 9 observer-shaped subagents (operator_record_reader, root_ghostproxy_state_reader, module_progress_drafter, scope_clarification_proposer, etc.) — v5's 5 worker subagents not present
- **Opus 1M context mode NOT set**: `openclaw models list` shows only 195k context for `anthropic/claude-opus-4-7`. The `[1m]` tag in my Claude Code banner is at the session level, not exposed as an OpenClaw model variant. No `--context-window` or equivalent flag found on `openclaw cron run --help`.

### Phase G — /load-brain refinement reflection
Operator asked for design reflection (not implementation) on `/load-brain` default scope. Detailed Goldilocks proposal authored in the conversation turn preceding this handoff. Summary:
- Current: 13 levels / 76 files / ~800K tokens (3/4 of 1M)
- Target: ~500K tokens at 4/4 comprehension
- 7 trim levers identified (L11 standards 28→6 / L0 root-doc dedup / L6 depth 5→2 / L9 SDLC demote / L3 read-offset / L7 ecosystem trim / L12 indexes skip)
- 7-level consolidated structure proposed with 3 inter-level reflection blocks (REFLECTION 1: laws+topology+engine synthesis; REFLECTION 2: model composition; REFLECTION 3: standards+principles operational contract)
- Topic-args reshape: `/load-brain <topic>` = default + deeper-on-topic (not narrow replace)
- Mechanism: command-text-as-program (Phase 1); reflection-enforcement hook optional (Phase 2 if reflection-skipping recurs)
- Operator decision points: which 6 universal standards / read-offset allowed on big models / reflection-block visibility / hook layer phase / implementation timing
- **NOT IMPLEMENTED YET** — this is design, queued for a future Edit session on `.claude/commands/load-brain.md`

## Current State

### Profile state
- `.assistant/root-ghostproxy-rollout.yaml` — v5 augmented (1226 lines, YAML parses, all sections present). UNCOMMITTED. NOT INSTALLED in `~/.openclaw/`.
- `.assistant/root-ghostproxy-rollout.cron.yaml` — STALE v3 observer (186 lines, untouched this session). MUST BE REWRITTEN before install.
- `.assistant/root-ghostproxy-rollout.openclaw.json5` — STALE v3 observer (180 lines, untouched this session). MUST BE REWRITTEN before install.
- `.assistant/_state/root-ghostproxy-rollout-inbox.md` — augmented with dry-run planning artifact (appended; v3 entry preserved). UNCOMMITTED.
- `.assistant/_state/root-ghostproxy-rollout-operator-directives.md` — DOES NOT YET EXIST. Worker would create on first real fire OR operator can author manually to deliver GO signal.

### Target project state
- `/home/jfortin/root-ghostproxy/` — exists, readable + writable. 9 epics / 21 modules / 68 tasks / 86 logs. Git state CLEAN (0 uncommitted) as of dry-run; HEAD bf248fe (Merge PR #1 install: /view + /questions skills + auto-compact OFF / auto-dream ON).
- Per-task status counts (last verified mid-session): T001-T011 status:done (Scaffold tier + start of Foundation); T012/T013/T015 in-progress; T014 + T017 + most M004+ status:not-started.

### Gateway state (carried from morning handoff)
- OpenClaw daemon healthy: PID 9229, system Node (`/home/linuxbrew/.linuxbrew/opt/node/bin/node`), `Connectivity probe: ok`, admin-capable.
- RGP cron registered as `6f2c6d38-91b5-4899-8ec2-b834d3f33e43` (v3 observer profile still installed; would need uninstall before installing v5 worker).
- Anthropic claude-cli OAuth expiring in 6h as of mid-session.

### Second-brain binding inventory (all 14 verified present)
| File | Lines |
|---|---|
| `wiki/config/methodology.yaml` | 657 |
| `wiki/config/methodology-profiles/spec-driven.yaml` | 201 |
| `wiki/config/methodology-profiles/test-driven.yaml` | 228 |
| `wiki/spine/models/quality/model-sfif-architecture.md` | 268 |
| `wiki/patterns/03_validated/architecture/scaffold-foundation-infrastructure-features.md` | 198 |
| `wiki/lessons/02_synthesized/spec-driven-agentic-build-...` | 301 |
| `wiki/config/wiki-schema.yaml` | 344 |
| `wiki/config/artifact-types.yaml` | 472 |
| `wiki/spine/models/agent-config/model-per-project-assistant-profile.md` | 201 |
| `wiki/spine/standards/per-project-assistant-profile-standards.md` | 210 |
| `wiki/spine/standards/model-standards/model-methodology-standards.md` | 545 |
| `wiki/spine/standards/model-standards/model-llm-wiki-standards.md` | 423 |
| `raw/notes/2026-05-08-pain-points-inventory-from-root-failed-conversation-master-aggregate.md` | 536 |
| `wiki/log/2026-05-08-sister-project-investigation-kickoff-spec-...` | 114 |

### New raw notes authored this session (verbatim operator-directive log)
| File | Purpose |
|---|---|
| `raw/notes/2026-05-16-operator-directive-why-rgp-not-working-on-200-plus-epics-tasks.md` | Captures the "200+ epics" question |
| `raw/notes/2026-05-16-operator-directive-rgp-profile-is-symptom-fix-the-actual-project-100-plus-issues.md` | Captures the reframe: profile is symptom, fix the project |
| `raw/notes/2026-05-16-operator-directive-rgp-worker-quality-bar-sdd-tdd-sfif-augment-not-rewrite.md` | Captures the quality bar + SDD+TDD+SFIF + augment-not-rewrite directive |

### Git state (uncommitted at handoff)
```
M .assistant/root-ghostproxy-rollout.yaml                                            # v3 → v5 (8 augmentations, 480 → 1226 lines)
M .assistant/_state/root-ghostproxy-rollout-inbox.md                                  # dry-run planning artifact appended
M docs/SESSION-2026-05-16.md                                                          # earlier handoff (operator opened it in IDE)
?? docs/SESSION-2026-05-16-handoff.md                                                 # this handoff
?? raw/notes/2026-05-16-operator-directive-why-rgp-not-working-on-200-plus-epics-tasks.md
?? raw/notes/2026-05-16-operator-directive-rgp-profile-is-symptom-fix-the-actual-project-100-plus-issues.md
?? raw/notes/2026-05-16-operator-directive-rgp-worker-quality-bar-sdd-tdd-sfif-augment-not-rewrite.md
?? wiki/log/2026-05-16-ck-bootstrap-execution-batch-2.md                              # CK fire from earlier today (separate arc)
?? wiki/log/2026-05-16-flagged-pages-gemini-spark.md                                  # CR fire from earlier today (separate arc)
?? wiki/sources/ai-models/src-gemini-spark-intelligence-google-agent-tier-2026-05-12-14.md   # CR-authored synthesis
... plus other CR/CK artifacts from morning arc
```

## What's Next (in operator-priority order)

### Design queue (substantive — operator says "no rush, other things first")

1. **Cron prompts rewrite** — `.assistant/root-ghostproxy-rollout.cron.yaml`. The 3 prompts must invert from observer to worker. The /goal mechanism operator named IS the cron `trigger.prompt` — well-formed goals with refs to v5 sections (methodology_binding / sfif_binding / novelty_dimension / workflow step names / audit cluster lookup / per-type standards / first-pick / test plan template). Each goal should be detailed enough that the agent is naturally driven, not figuring-it-out.

2. **OpenClaw config alignment** — `.assistant/root-ghostproxy-rollout.openclaw.json5`. Surgical edits:
   - Remove `filesystem-write-root-ghostproxy` from `tools.deny`
   - Add target-scoped write allow (worker writes ~/root-ghostproxy/)
   - Replace or remove `systemPromptOverride` (use v5 profile YAML's `prompt_templates.system` directly)
   - Align `subagents.allowAgents` with v5's worker subagents + new research_online + research_local + adr_author + regression_test_author + pm_scrum_facilitator subagents
   - Add Opus 1M context-mode setting (path TBD — see #3)

3. **Opus 1M context-mode investigation + setting** — open question. What I see:
   - `openclaw models list` shows opus-4-7 at 195k only
   - `openclaw cron run --help` has no `--model` flag
   - The `[1m]` tag is at Claude Code session level, not in OpenClaw model namespace
   - `openclaw models aliases add` exists — likely path is to register an alias mapping `opus-1m` → `anthropic/claude-opus-4-7[1m]` (need to test if OpenClaw accepts the bracket syntax)
   - Operator suggested prompt-prefix path: prefix cron `trigger.prompt` with `/model claude-opus-4-7[1m]` slash command — Claude Code's slash-command parser would invoke model switch before the rest. Untested in OpenClaw spawn path; reversible to test.
   - Either path needs experimental verification. Probably also worth checking `~/.claude/settings.json` for a default-model setting that might affect all Claude Code spawns.

4. **Multi-discipline identity + subagents** — augment `.assistant/root-ghostproxy-rollout.yaml`:
   - identity.tagline + purpose: frame as **Senior Software Architect + DevOps Engineer + FullStack Expert + PM Scrum Agile facilitator**, currently in worker mode on root-ghostproxy
   - subagents list additions:
     - `research_online` — gh CLI on cyberpunk042/root-ghostproxy + wiki_fetch MCP (operator-anchored verification only; NOT mass external ingestion)
     - `research_local` — wiki_search + Read + Grep on second-brain + target project
     - `adr_author` — architecture decisions per SDD design-stage (decision-page standards)
     - `regression_test_author` — TDD test-first per audit cluster (bug-test-first for any SB-###)
     - `pm_scrum_facilitator` — operator-decision-queue + module progress per Scrum readiness/progress dimensions

5. **Anti-poke-deficit + anti-direction-deficit anti-patterns** — append to `anti_patterns:`:
   - `poke_deficit` — cron prompt too thin; agent doesn't know what to do
   - `direction_deficit` — no specific first-pick named + no audit anchor in goal
   - `spam` — cron fires too often for the work shape (Goldilocks per-cadence)
   - `work_mode_drift` — agent goes into report-mode or discuss-mode instead of work-mode

6. **Runtime settings verification** block in `pre_launch_readiness:` — Opus 1M flag set + claude-cli profile params verified + sandbox/elevated state explicit.

7. **/load-brain refinement implementation** — separate Edit session on `.claude/commands/load-brain.md`. Design captured in conversation turn preceding this handoff:
   - Trim L11 standards 28 → 6 universal (session-handoff + per-project-assistant-profile + methodology-standards + llm-wiki-standards + task-page + lesson-page — operator to confirm/swap)
   - Skip L0 root-doc re-reads (already auto-loaded)
   - Demote L6 depth `second-brain` + `local-ai` + `notebooklm` to topic-args
   - Demote L9 SDLC/aidlc to topic-args
   - Read-offset L3 foundation models on Relationships+Backlinks sections (operator to confirm: is section-targeted reading on large reference pages allowed at default?)
   - Add 3 inter-level reflection blocks (REFLECTION 1: laws+topology+engine; REFLECTION 2: model composition; REFLECTION 3: standards+principles operational contract)
   - Topic-args reshape: default + deeper-on-topic (not narrow replace)
   - Target: ~500K tokens at 4/4 comprehension (down from 800K at 4/4 catalog)

8. **/load-brain reflection-enforcement hook (Phase 2, optional)** — IF reflection-skipping becomes a recurring failure, add a hook that detects level-boundary completion and injects the reflection prompt as additionalContext. Premature now; defer.

### Pre-install gates (per pre_launch_readiness section of profile YAML)

When ready to install (operator's call when "other things" are done):

1. Items 1-6 above must land (cron + openclaw.json5 alignment + 1M context + multi-discipline identity + anti-patterns + runtime verification)
2. Re-run profile_quality_gates checks (still 8/8 pass)
3. Re-run second_brain_binding verification (14/14 + any new ones from items 4-5)
4. Re-run target project access verification
5. Operator writes GO in `.assistant/_state/root-ghostproxy-rollout-operator-directives.md`
6. Uninstall v3 first: `bin/assistant uninstall root-ghostproxy-rollout`
7. Install v5: `bin/assistant install root-ghostproxy-rollout`
8. Monitor first real fire end-to-end (~45-75 min for substantive T014 task)
9. Review staged edits in `~/root-ghostproxy/` + Resolution section + planning artifact accuracy

## How to Resume

```
1. Read this handoff
2. openclaw daemon status                                  # gateway still healthy?
3. cat .assistant/_state/root-ghostproxy-rollout-inbox.md  # review dry-run planning artifact
4. Read .assistant/root-ghostproxy-rollout.yaml             # full v5 profile
5. Read .assistant/root-ghostproxy-rollout.cron.yaml        # STALE v3 — needs rewrite
6. Read .assistant/root-ghostproxy-rollout.openclaw.json5   # STALE v3 — needs rewrite
7. Decide which design-queue item to take first (operator-priority)
8. For each item: surgical Edit calls (NEVER Write whole files unless brand-new), cite second-brain source per augmentation
```

## Mistakes I Made (so next session doesn't repeat them)

| Mistake | Operator response |
|---|---|
| Probed `/root/` for root-ghostproxy when it was at `~/root-ghostproxy/` — path was in prior `ls $HOME` output I had already received | "WTF ARE YOU DOING YOU FUCKING RETARD... root-ghostproxy is at root-ghostproxy..... YOU FUCKING SCRUB..." |
| Wrote a full 480-line v4 YAML from scratch instead of surgical augmentation | "do not rewrite everything everytime make augmentations, improvements, upgrades, evolutions" |
| Initial response to "WTF IS NOT CLEAR" was to start investigating instead of acknowledging the framing operator had repeatedly explained | "you are so fucking retard... tell me what you dont understand about where we are and where we are going" |
| Bash hook blocked truncation pipes — kept defaulting to `\| head -N` reflexively | (hook caught) |
| First sketch of v5 missing methodology binding + SDD+TDD discipline + SFIF + standards compliance — needed operator correction "This AI assistant will have to respect the knowledge of the second-brain..." | "do not rewrite everything everytime make augmentations" + new substantive directive |

**Pattern**: I rush from "understand" to "execute" without proportional depth in "process the knowledge". Operator-corrected explicitly: *"take your time I know this is complex, you can read more file. process more the knowledge and a clear intelligence so that the work is reliable."* The fix is to read the standards + models that govern what I'm building BEFORE building, then augment incrementally with citations.

## Files Modified This Session

- `.assistant/root-ghostproxy-rollout.yaml` — 8 surgical augmentations (480 → 1226 lines); UNCOMMITTED
- `.assistant/_state/root-ghostproxy-rollout-inbox.md` — appended dry-run planning artifact; UNCOMMITTED
- `raw/notes/2026-05-16-operator-directive-why-rgp-not-working-on-200-plus-epics-tasks.md` — NEW; UNCOMMITTED
- `raw/notes/2026-05-16-operator-directive-rgp-profile-is-symptom-fix-the-actual-project-100-plus-issues.md` — NEW; UNCOMMITTED
- `raw/notes/2026-05-16-operator-directive-rgp-worker-quality-bar-sdd-tdd-sfif-augment-not-rewrite.md` — NEW; UNCOMMITTED
- `docs/SESSION-2026-05-16-handoff.md` — THIS HANDOFF; UNCOMMITTED

## Continuation — 2026-05-16 evening — Beyond the Initial Handoff

> **Context recovery anchor.** This handoff was first written at ~17:00 ET when the v5 profile YAML was 1226 lines + cron/openclaw.json5 still stale v3 + design queue at 8 items (1 done, 7 pending). Between then and the compaction trigger, the operator authorized continuing ("good, continue. yes."). Most of the design queue was implemented in surgical Edits. This section captures everything done in the continuation so post-compaction pickup is clean.

### Status of the 8-item design queue (refreshed)

| # | Item | Initial handoff | Status now (evening 2026-05-16) | Key delta |
|---|---|---|---|---|
| 1 | Cron prompts rewrite | PENDING | ✅ **DONE** | 3 prompts replaced observer → worker /goal in `.assistant/root-ghostproxy-rollout.cron.yaml`. Each 5-7K chars: BOUND-TO refs + SACROSANCT invariants + WALK through 10 workflow steps + priority_order + anti-patterns + audit-anchor + budget. File 186 → 424 lines. |
| 2 | OpenClaw config alignment | PENDING | ✅ **DONE** | 4 surgical Edits to `.assistant/root-ghostproxy-rollout.openclaw.json5`: (a) tools.deny removed `filesystem-write-root-ghostproxy` + added cross-project boundary list for OTHER sisters; (b) tools.allow added 7 target-project capabilities (write target / bash target / backlog / .claude-dir / agent-docs / install.sh / tools/) + git-stage; (c) systemPromptOverride replaced (v3 observer → v5 worker with multi-discipline competence frame + 12 core principles + 5 sacrosanct operator quotes verbatim); (d) subagents.allowAgents replaced (9 observer agents → 10 worker fleet matching profile YAML); (e) metadata bumped to _profile_version: 5 + _v5_rewritten + _augmentations_log. File 180 → 214 lines. |
| 3 | Opus 1M context investigation | PENDING | ⚠️ **PATH A TESTED — INSUFFICIENT ALONE** | Tested Path A: `openclaw models aliases add opus-1m anthropic/claude-opus-4-7[1m]` → accepted (exit 0; alias registered at `~/.openclaw/openclaw.json`; backup at `.bak`). BUT `openclaw models list` still shows `Ctx 195k` for the variant — the bracket syntax is a NAME at OpenClaw's layer, not a context-window directive. `~/.claude/settings.json` is essentially empty (`{"effortLevel":"max"}`); the `[1m]` in operator's banner must be runtime-negotiated via `anthropic-beta` API header. **Path E (anthropic-beta header) identified as most likely real mechanism** — closest match to operator's intuition "add it at the start of a prompt and it will be transferred to the -p command". 6 investigation paths now documented in profile's `runtime_settings_verification.opus_1m_context_mode.investigation_paths_status` (A tested · B/C/D/E/F not yet) + 3 operator decision points surfaced (which path to pursue / where to set the flag / install at 195k baseline now or wait). |
| 4 | Multi-discipline identity + 5 new subagents | PENDING | ✅ **DONE** | Profile YAML augmented: (a) `identity.tagline` extended with "Senior Software Architect + DevOps Engineer + FullStack Expert + PM Scrum Agile facilitator" framing; (b) NEW `identity.multi_discipline_competence_frame` section binding each discipline to specific epics/modules + subagents + principles_focus; (c) NEW `identity.operating_mode: "WORK MODE ALWAYS"` per operator-doctrine; (d) NEW `identity.24_7_recyclable` framing per operator "we can recycle it later or transfer it"; (e) 5 new subagent declarations appended to `subagents:` section with full purpose / when_to_use / tools / forbidden_tools / budget / style / output — `research_online`, `research_local`, `adr_author`, `regression_test_author`, `pm_scrum_facilitator`. Total subagents: 5 → 10. |
| 5 | Anti-patterns for operator-prevention concerns | PENDING | ✅ **DONE** | 5 new anti-patterns appended to `anti_patterns:` directly mapping to operator's 2026-05-16 concerns ("Making such it will not freeze or be mindless or receive garbage or be too spammed or not poked enough or not directed well"): `mindless_execution` · `accept_garbage_input` · `cron_cadence_spam` · `poke_deficit` · `direction_deficit`. Each with description / detector / response / why. Total anti-patterns: 12 → 17. |
| 6 | Runtime settings verification block | PENDING | ✅ **DONE** | `pre_launch_readiness.runtime_settings_verification` block added with: `opus_1m_context_mode` (6 paths + status + decision points) · `claude_cli_invocation_params` (model + thinking + reasoning + cache_retention + context_injection + heartbeat) · `sandbox_state` · `context_limits` (with 1M scaling guidance) · `auth_lifetime` (OAuth ~6h expiry; refresh path) · `proper_settings_attestation` (gate list). |
| 7 | /load-brain Goldilocks remaster | DESIGNED | ✅ **DONE** | 5 surgical Edits to `.claude/commands/load-brain.md`: (a) Discipline section rules 2-4 reshape (offset-allowed on >500-line reference pages + reflection-checkpoint mandate + topic-args additive rule 7); (b) Argument modes table (default + deeper-on-topic, not replace); (c) Topic vocabulary table (annotated "In default?" column + new `methodology-profiles` + new `rules` topics + demoted-from-default markers); (d) The Tree section completely reshaped (13 levels → 7 levels + 3 inter-level REFLECTION blocks; 76 reads → ~42 reads; ~800K → ~500K tokens; END attestation refreshed with reflection-emitted flags + demoted-to-topic-arg inventory); (e) Composition section ~76 → ~42. File 342 → 333 lines. |
| 8 | Reflection-enforcement hook (Phase 2) | DEFERRED | ⏸ **STILL DEFERRED** | Per design: command-text-as-program first; hook only if reflection-skipping recurs after `/load-brain` Goldilocks remaster ships. Defer until observed need. |

**Net: 6 of 8 done; 1 partial (Path A tested, decision needed); 1 deferred.**

### New artifacts this continuation

| Path | Size | Purpose |
|---|---|---|
| `.assistant/_state/root-ghostproxy-rollout-operator-directives.md` | 4488 bytes | Operator's input channel (NEW). Structured slots: INSTALL: GO · BOOTSTRAP-EXECUTE: GO · SPRINT: ACTIVE / OFF · PRIORITY-OVERRIDE · CROSS-TIER-OVERRIDE · RESOLVE: <slug> · RETIRE: CONFIRMED · free-form section. Worker reads at step 0_operator_directives; appends `[!processed]` follow-ups; never overwrites operator text. |
| `~/.openclaw/openclaw.json` (modified) | n/a | Operator-territory but updated by `openclaw models aliases add` — added alias `opus-1m → anthropic/claude-opus-4-7[1m]`. Backup at `~/.openclaw/openclaw.json.bak`. Alias is kept (harmless naming) even though it doesn't unlock 1M context alone. |

### Files Modified — refreshed inventory

```
M .assistant/root-ghostproxy-rollout.yaml                                            # 480 → 1446 lines (v3 observer → v5 worker, 12 surgical augmentations across 2 batches)
M .assistant/root-ghostproxy-rollout.cron.yaml                                       # 186 → 424 lines (v3 observer prompts → v5 worker /goal prompts; 3 jobs)
M .assistant/root-ghostproxy-rollout.openclaw.json5                                  # 180 → 214 lines (v3 → v5; deny/allow flip + subagents + systemPromptOverride + metadata)
M .assistant/_state/root-ghostproxy-rollout-inbox.md                                 # appended dry-run planning artifact
M .claude/commands/load-brain.md                                                     # 342 → 333 lines (Goldilocks remaster: 13 levels → 7 + 3 reflection blocks)
?? .assistant/_state/root-ghostproxy-rollout-operator-directives.md                  # NEW operator input channel
?? docs/SESSION-2026-05-16-handoff.md                                                # THIS HANDOFF
?? raw/notes/2026-05-16-operator-directive-why-rgp-not-working-on-200-plus-epics-tasks.md
?? raw/notes/2026-05-16-operator-directive-rgp-profile-is-symptom-fix-the-actual-project-100-plus-issues.md
?? raw/notes/2026-05-16-operator-directive-rgp-worker-quality-bar-sdd-tdd-sfif-augment-not-rewrite.md
... plus other CR/CK artifacts from the morning arc (out of scope this evening)
```

State-modifying command run this evening (operator-territory but reversible):
- `openclaw models aliases add opus-1m anthropic/claude-opus-4-7[1m]` — alias kept, backup at `~/.openclaw/openclaw.json.bak`

### Path A test concrete commands + results (for post-compact verification)

```bash
# Command run:
openclaw models aliases add opus-1m anthropic/claude-opus-4-7[1m]
# Result: exit 0; "Config overwrite: /home/jfortin/.openclaw/openclaw.json (sha256 ... -> ..., backup=...)"; "Alias opus-1m -> anthropic/claude-opus-4-7[1m]"

# Verify alias landed:
openclaw models aliases list
# Output: 3 aliases — opus, sonnet, opus-1m

# Verify context window of new variant:
openclaw models list | grep '4-7\[1m\]'
# Output: anthropic/claude-opus-4-7[1m] | text | 195k | no | yes | configured,alias:opus-1m
# ⚠️ THE Ctx COLUMN STILL SHOWS 195k — alias is just a name; doesn't unlock 1M context

# Check ~/.claude/settings.json for clues about how operator's Claude Code banner shows [1m]:
cat ~/.claude/settings.json
# Output: {"effortLevel": "max"}  — empty of model/context settings

# Check env vars:
env | grep -iE "anthropic|claude|context|beta"
# Output: CLAUDECODE=1 / CLAUDE_AGENT_SDK_VERSION=0.3.143 / CLAUDE_EFFORT=xhigh / CLAUDE_CODE_ENTRYPOINT=claude-vscode
# ⚠️ No model or context-window env vars. The [1m] in operator's banner is set elsewhere (runtime-negotiated via anthropic-beta API header most likely).
```

### Decision points awaiting operator (post-compact)

Surfaced in `pre_launch_readiness.runtime_settings_verification.opus_1m_context_mode.decision_required_from_operator`:

1. **Which Opus 1M path to pursue?** Recommended: **Path E** (anthropic-beta header) since it matches the underlying API mechanism + closest to operator's "prompt prefix transferred to -p" intuition. Alternatives: Path B (direct model.primary), Path C (prompt-prefix /model slash command), Path D (~/.claude/settings.json default-model — broader scope; operator-territory edit), Path F (new params field in openclaw.json5).

2. **If Path E confirmed, where to set the flag?**
   - (a) `ANTHROPIC_BETA_FEATURES` env in systemd service unit (`~/.config/systemd/user/openclaw-gateway.service`)
   - (b) New field in `.assistant/root-ghostproxy-rollout.openclaw.json5` (e.g., `params.betaFeatures: ["context-1m-2025-08-07"]` — needs schema verification)
   - (c) Prompt-prefix per cron job per operator's intuition (test whether OpenClaw's spawn passes prompt through Claude Code's slash-parser)

3. **Install at 195k baseline now OR wait for 1M?** The cron prompts + audit substrate + first-pick context all fit comfortably in 195k. 1M would benefit weekly-deep multi-task fires + cross-cluster cross-references. Operator decides whether 1M is blocking or post-install.

Also gated:
- **GO signal** in `.assistant/_state/root-ghostproxy-rollout-operator-directives.md` (placeholder ready with INSTALL: GO slot)
- **v3 uninstall** before v5 install: `bin/assistant uninstall root-ghostproxy-rollout` (operator runs)
- **v5 install**: `bin/assistant install root-ghostproxy-rollout` (after GO)
- **First real fire monitoring**: ~45-75 min budget on first-pick T014 (operator reviews planning artifact in inbox first)

### How to Resume (refreshed)

```
1. Read this handoff in full
2. Read .assistant/_state/root-ghostproxy-rollout-inbox.md → Pre-Launch Dry-Run #1 section (the planning artifact)
3. Read .assistant/_state/root-ghostproxy-rollout-operator-directives.md (operator input channel placeholder)
4. Decide on Opus 1M path (3 decision points above) — or defer and install at 195k baseline
5. If installing:
   a. Verify: openclaw daemon status (gateway healthy?); openclaw models aliases list (opus-1m still there?)
   b. Uninstall v3: bin/assistant uninstall root-ghostproxy-rollout
   c. (Optional) Update .openclaw.json5 model.primary if pursuing Path E or other 1M path
   d. Write "INSTALL: GO" in operator-directives.md
   e. Install v5: bin/assistant install root-ghostproxy-rollout
   f. Monitor first cron fire end-to-end; review staged edits in ~/root-ghostproxy/ + Resolution sections
6. If NOT installing yet (operator has other things first): all artifacts on disk, gated, reversible
```

### Pitfalls observed in the continuation (added to mistakes table)

| Mistake this continuation | Lesson |
|---|---|
| First subagents Edit failed because old_string used "Removed from v1" but actual file had "Added: r20_gate" trailing | Always `grep` for the EXACT current content before crafting Edit old_string — context-memory of v5 YAML structure ≠ what's on disk after prior edits |
| Path A alias test assumed OpenClaw's bracket-syntax acceptance would mean 1M context activation | Test the OUTCOME (Ctx column), not just the INPUT acceptance (exit 0). Empirical verification per P4: declarations aspirational until infrastructure verifies them. |

### What's NOT done (carry-forward for next session)

- Items #3 (Opus 1M path decision) + #8 (reflection-enforcement hook Phase 2)
- Install (gated on operator GO)
- v3 uninstall (operator runs)
- First real fire on T014 (post-install)
- Possible cron.yaml + openclaw.json5 + profile YAML tweaks based on first-fire empirical observations

## Sister-Project Handoff Reference

The morning handoff at `docs/SESSION-2026-05-16.md` covers the gateway-fix arc + initial v3 install. This handoff is the AFTERNOON + EVENING arc continuation — v3 → v5 worker rebuild + design queue (6 of 8 implemented; Path A tested; install gated). Read both for full day context.

The CK + CR profiles continue to operate in parallel — see `wiki/log/2026-05-16-ck-bootstrap-execution-batch-2.md` + `wiki/log/2026-05-16-flagged-pages-gemini-spark.md` for their concurrent activity. They are NOT in scope for this RGP-rebuild arc.
