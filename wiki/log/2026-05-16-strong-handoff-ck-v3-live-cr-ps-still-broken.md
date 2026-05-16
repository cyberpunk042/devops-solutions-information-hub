---
title: "2026-05-16 — Strong handoff: CK v3 live (autonomous + R20-compliant); CR + PS still on v1 (broken); RGP uninstalled; full requirements framework"
type: note
domain: log
note_type: session
status: active
confidence: high
created: 2026-05-16
updated: 2026-05-16
sources:
  - id: session-2026-05-16
    type: directive
    description: "Multi-hour session: bootstrap CK v3 rewrite + uninstall all 4 prior profiles + patch bin/assistant + verbatim operator directives across the session"
tags: [handoff, session, ck-v3, retroactive-cleanup, profile-requirements, r20-sacrosanct, autonomous-assistant, cr-pending, ps-pending, rgp-uninstalled]
---

# Strong handoff — 2026-05-16

## TL;DR

| Profile | Version | Installed | State |
|---|---|---|---|
| **circular-knowledge** | **v3** | YES | Bootstrap one-shot firing now; autonomous untracked-removal + tracked-batch surface |
| continuous-research | v1 | NO | Profile YAML preserved at `.assistant/continuous-research.yaml`; STILL HAS THE TRASH BUGS |
| pipeline-synthesis | v1 | NO | Profile YAML preserved at `.assistant/pipeline-synthesis.yaml`; STILL HAS THE TRASH BUGS |
| root-ghostproxy-rollout | v2 | NO | Profile YAML preserved at `.assistant/root-ghostproxy-rollout.yaml`; the 3min sprint-tick agent; NOT a CK target |

Only `circular-knowledge` is fixed. **CR and PS still produce the same trash they always did.** Re-installing them as-is will resume pollution. They need v3 treatment first.

## The 21 requirements framework (applies to ALL profiles)

Validated by operator across the session (2026-05-15 + 2026-05-16). Every profile must meet ALL of these or it is NOT VALID.

| # | Requirement | Source |
|---|---|---|
| R1 | Multi-vision discipline (## Context Boundaries + ## Alternative Visions when applicable) | 2026-05-15 |
| R2 | Self-first cascade (self → second-brain → ecosystem, no inversion) | 2026-05-15 |
| R3 | Goldilocks per-proposal AND per-tick | 2026-05-15 + 2026-05-16 |
| R4 | Stage discipline (Layer N → N+1 only) | 2026-05-15 |
| R5 | Never auto-promote past 01_drafts/ | 2026-05-15 |
| R6 | No garbage, no mindless promote | 2026-05-16 |
| R7 | Flow: ingest → synthesize → level-up | 2026-05-16 |
| R8 | Cadence matches scope (sprint vs weekly steady-state) — NOT pattern-copy | 2026-05-16 |
| R9 | Autonomous within bounded criteria; no per-item approval freeze | 2026-05-16 |
| R10 | Build forward; never revert + restart | 2026-04-24 |
| R11 | No freeze, no slow, no stop-with-work-remaining | 2026-05-16 |
| R12 | Pause = ready-for-review (not freeze in disguise) | 2026-05-16 |
| R13 | Anti-pollution gate (growth > 5× operator-accept → pause production) | 2026-05-16 |
| R14 | Retroactive capability (audit + clean past trash) | 2026-05-16 |
| R15 | Online research allowed when applies (verify/anchors/cross-ref); NOT mass ingestion | 2026-05-16 |
| R16 | No cross-project work without operator directive | inferred |
| R17 | No brain audits without operator directive | inferred |
| R18 | No self-documentation pages in wiki/ | 2026-05-16 |
| R19 | No drafts to wiki/spine/01_drafts/ | inferred |
| **R20** | **NEVER auto-delete COMMITTED or STAGED files without operator agreement** | **2026-05-16 sacrosanct** |
| R21 | No AI slop (boilerplate, over-engineering, dead-code sections) | 2026-05-16 |

## Sacrosanct operator-verbatim quotes (NEVER paraphrase)

```
2026-05-15:
  "weight everything in the balance and make we learnings are properly
   shared and in the end the knowledge evolve starting with the self and
   then the second-brain and then it cascade, or progress delta little or
   not toward the new standards and models and etc..."

  "It can happen within a project and cross-project and multiple vision
   can be true and often for different reasons. Goldilock is important...
   always toward knowledge and intelligence. often starting with information
   and always through the proper stages."

2026-05-16 — trash diagnosis:
  "the circular agent wrote a lot of trash... as if it needed to ingest
   everything about every project for now fucking reason"

  "we will upgrade / evolve the Ai assistant circular knowledge so that
   its not trash but proper work like I required"

2026-05-16 — flow:
  "after ingest you synthesize and then it continue to level up...
   no garbage, no random mindless promote"

2026-05-16 — autonomy:
  "WHY WOULD THE AI HAVE TO PROPOSE TO REMOVE THE TRASH IT ADDED ITSELF??
   ITS SUPPOSED TO BE A FUCKING AUTONOMOUS ASSISTANT"

  "I SHOULD NOT NEED TO APPROVE WTF... LETS REPROCESS THE REQUIREMENTS
   FOR THE AI ASSISTANT PROFILE TO BE A VALID ONE.... IF IT FREEZE
   ITS NOT VALID..."

2026-05-16 — cadence:
  "wtf what is every 3 min lol ???? WHAT THE FUCK ON EARTH IS THIS ???
   THE ONLY FUCKING THING WHICH COULD BE FAST LIKE THIS IS THE
   root-ghostproxy ai assistant"

2026-05-16 — sacrosanct R20:
  "THE AI ASSISTANT IS NOT GOING TO DELETE ANYTHING THAT IS ALREADY
   COMMITED OR STAGED WITHOUT MY AGREEMENT.. STOP TRYING TO RUSH AND
   HACK AND QUICKFIX. WORK PROPERLY."

2026-05-16 — online research:
  "there can even be online research when it apply... we love online
   researches"

2026-05-16 — anti-freeze:
  "I would not want it to freeze for not reason for example"
  "I would not want it to work slow either"
  "or do little change and stop"
  "pause when the work is really ready for review and nothing else can
   be done"

2026-04-24 — behave from the project:
  "behave FROM the project, not OVER it"
  "the project is intelligent. the intelligence comes from USING the project"
  "INSTEAD OF TRYING TO GO BACKWARD. WHY DONT YOU FOCUS ON GOING FORWARD?"
```

## What's done this session

### CK v3 (live)

- Profile rewritten: yaml 1127→525 lines, cron 424→122, json5 212→147 (total −55% slop)
- 3 cron jobs (down from 6 in v2; sprint-tick removed, daily/monthly-brain dead jobs removed)
- 7 sub-agents (down from 9; work_completion_detector + anti_pattern_diagnostician removed as RGP-pattern slop)
- R20 enforced structurally: `git-commit` in tools.deny; workflow gates every rm with `git ls-files --error-unmatch` check; tracked-removal requires prior accepted Q##
- Bootstrap one-shot firing now (cron id `d554ea1e`, delete-after-run)
- Expected deliverable in ~20-30 min: `wiki/log/2026-05-16-ck-bootstrap-execution-batch-1.md` with untracked-already-rm'd + tracked-batch Q## + ambiguous Q##s

### tools/assistant.py patches (committed via working-tree changes only — NOT yet committed)

| Patch | What | Why |
|---|---|---|
| `translate_schedule()` | Added `every:Xm` (interval) + `first-fire` (return None, handled elsewhere) | v1 didn't translate these; cron jobs silently skipped |
| `cmd_install()` step 4 | Added first-fire one-shot fire loop (post cron-registration) | Bootstrap jobs need to fire on install, not wait for next cron |
| `cmd_uninstall()` | Calls `openclaw agents delete --force` FIRST (canonical prune); then manual fallback rm of agent dir + openclaw.json entry; removes per-profile cron jobs; cleans `.assistant/_state/<profile>-*.md` | v1 left orphaned cron jobs (21 of them), agent dirs, session history |

### Profiles uninstalled cleanly (idempotent via patched cmd_uninstall)

- continuous-research
- pipeline-synthesis
- circular-knowledge (then reinstalled as v3)
- root-ghostproxy-rollout

### Trash audit done (CK v2 batch report; not yet executed)

[wiki/log/2026-05-16-ck-bootstrap-pile-depile-batch-1.md](2026-05-16-ck-bootstrap-pile-depile-batch-1.md) — produced by CK v2 (now superseded by v3). Identified:
- Pile ratio 5.35× = NEVER_DEPILED
- 66 untracked agent-authored files in pile (clear-trash signatures)
- ~250 tracked agent-authored files (mostly fire-N tier-elevation logs from 2026-05-08)
- KEEP list: Microsoft AGT synthesis (Q74-Q76, Q83), Opus 4.7 dupes (Q85), AlphaEvolve (Q77-79), cascade-candidate-root-ghostproxy (Q86-Q89), agt-cascade-trio (Q84), metered-economics lesson (Q82), this audit batch report itself
- 13 untracked files explicitly in B1.1 (research-watch logs, purge-summary logs, CK self-log, ephemeral handoff)
- 1 untracked self-doc page (B1.3 profile-circular-knowledge — multi-vision case)

CK v3 bootstrap (running now) will:
- Re-classify per v3 criteria (UNTRACKED-only autonomy)
- Autonomously rm the untracked clear-trash (NO operator approval needed)
- Surface tracked clear-trash as ONE batch Q## per signature class
- Surface ambiguous per-class

## What's pending

### Immediate (next session start here)

1. **Wait for CK bootstrap to complete** (~30 min from install at 12:12 UTC = ready ~12:45 UTC)
2. **Read** [wiki/log/2026-05-16-ck-bootstrap-execution-batch-1.md](wiki/log/2026-05-16-ck-bootstrap-execution-batch-1.md) when it appears
3. **Verify** the untracked files were actually rm'd (check `git status` for missing untracked files; check operator-decision-queue for new batch Q##)
4. **Review the tracked-batch Q##** — decide whether to `bin/assistant resolve Q## accept` (= authorize CK to `git rm` the batch next tick) or reject
5. **Commit** the working-tree changes when ready (operator-territory — agent never commits per R20)

### Short-term (this/next session)

1. **Apply v3 pattern to continuous-research** — current CR v1 has these violations:
   - Mass external fetching (the news articles, claude managed agents docs, etc.)
   - Fabrication audit hits (claims work but no file modifications)
   - Timeout issues (model-call-started hangs)
   - No retroactive capability
   - No R20-style boundary on the raws it creates
   Approach: rewrite CR with the 21 requirements + R20 boundary + tighter scope (only fetch when operator-stated relevance / Q## directive)

2. **Apply v3 pattern to pipeline-synthesis** — current PS v1 has these violations:
   - Bulk synthesis of every raw without operator-stated relevance filter
   - The `wiki/sources/ecosystem-projects/src-openarms-*` mass (operator named trash)
   - Same fabrication/timeout patterns as CR
   Approach: rewrite PS with a relevance gate before synthesizing each raw

3. **Decide on root-ghostproxy-rollout** — RGP v2 is uninstalled. The 3min sprint-tick was operator-authorized FOR RGP (different from CK). Decide:
   - Reinstall RGP v2 as-is once CR + PS are clean (RGP needs CR + PS infrastructure working first)
   - Or: v3 RGP with R20 + autonomy refinements
   Operator-stated mission for RGP (from 2026-05-15 PRE-COMPACT-HANDOFF): work on the root-ghostproxy sister project's CLAUDE.md / AGENTS.md / SFIF modules

### Medium-term

1. **Build `bin/assistant apply-retroactive-batch <Q##>` slash command** — operator-triggered execution path for tracked-batch removals. Currently CK surfaces Q##, operator hand-edits queue to mark accepted, next CK tick reads accepted Q## and executes `git rm`. Slash command would parse batch report path + execute directly.

2. **Audit `.assistant/_state/` evolution** — when profile re-installs, state files are removed. Decide if some state should persist across re-install (e.g., per-profile config tuning history).

3. **Audit the `_global` cron timers** — 8 systemd timers at `/home/jfortin/.config/systemd/user/assistant-cron-_global-*.timer`. These run shell tasks (pipeline-post hourly, gateway-health daily, etc.). Operator hasn't said yes/no to these — they're separate from per-profile assistants. Decide retention.

### Long-term

1. **CR fabrication root cause** — 22:25 ET 2026-05-15 CR fire produced summary claiming work but auditor flagged "no files modified in 264s window". Need to investigate whether this is:
   - Agent claiming work it didn't do (true fabrication)
   - Agent doing work but in isolated workspace (not project root) — audit false-positive
   - Tool failure that the agent narrated as success
   Session at [.openclaw/agents/continuous-research/sessions/d0b131ff-...](isolated)

2. **CR/PS timeout root cause** — 1109s and 830s "model-call-started" phase hangs. Investigate:
   - Is it the model API hanging?
   - Is it gateway routing?
   - Is the prompt too long to even start streaming?

3. **Profile validity self-check** — write a tool that audits any profile YAML against the 21 requirements. Run before any install.

## Files / locations (where to find everything)

### Profile sources of truth

```
.assistant/circular-knowledge.yaml          # v3 source
.assistant/circular-knowledge.cron.yaml     # 3 jobs
.assistant/circular-knowledge.openclaw.json5 # vendor config
.assistant/circular-knowledge.openclaw.json  # deployable (auto-generated from .json5)
.assistant/circular-knowledge-*.openclaw.*   # ditto for other profiles
.assistant/_state/circular-knowledge-*.md   # inbox + operator-directives (runtime)
.assistant/_global/cron.yaml                # cross-profile cron config
.assistant/_global/surfaces.yaml            # surface integrations
.assistant/_templates/                       # template files (assistant.service, cron.service, etc.)
.assistant/README.md                         # high-level architecture doc
```

### OpenClaw runtime state

```
~/.openclaw/openclaw.json                            # gateway config (agents + MCP + auth)
~/.openclaw/agents/<profile>/agent/                  # per-agent auth-profiles, state
~/.openclaw/agents/<profile>/workspace/              # materialized markdown (IDENTITY, AGENTS, WORKFLOW, etc.)
~/.openclaw/agents/<profile>/sessions/*.jsonl       # session traces
~/.openclaw/agents/<profile>/sessions/*.trajectory.jsonl # full model interaction trace
~/.config/systemd/user/assistant-<profile>.service   # systemd unit (reboot persistence)
~/.config/systemd/user/assistant-cron-_global-*.timer # global cron timers (NOT per-profile)
```

### Tooling

```
tools/assistant.py                          # ~3500 lines — install/uninstall/status/activity (PATCHED this session)
bin/assistant                               # 775-byte wrapper
.venv/bin/python                            # venv (has pyjson5 + youtube-transcript-api + other deps)
```

### Wiki state

```
wiki/backlog/operator-decision-queue.md     # Q## entries (operator-pending decisions)
wiki/log/2026-05-16-ck-bootstrap-*.md       # CK audit reports
wiki/log/2026-05-08-fire-*-tier-elevation-* # ~40 tracked orphan logs (in pile, awaiting tracked-batch Q##)
wiki/sources/ecosystem-projects/src-*       # CR/PS mass ingestion (in pile, operator-named trash)
wiki/sources/tools-integration/src-aicp-*   # AICP mass docs (in pile)
```

## What I patched in `tools/assistant.py` (not yet committed)

```diff
def translate_schedule(schedule: str) -> tuple[str, str] | None:
    # Added support for:
    + every:Xm / every:Xs / every:Xh / every:Xd  → pass-through to openclaw --every
    + first-fire  → return None (intentional; handled by cmd_install one-shot loop)

def cmd_install(args):
    # After cron-job registration loop, added:
    + first_fire_jobs = [j for j in jobs if j.get("schedule") == "first-fire"]
    + for j in first_fire_jobs:
    +     fire as `openclaw cron add --at 5s --delete-after-run --agent <name> ...`

def cmd_uninstall(args):
    # Rewritten with proper sequence:
    + 1. Remove per-profile cron jobs (find agentId == name OR name startswith <profile>-)
    + 2. openclaw agents delete <name> --force (CANONICAL prune of workspace + state + registry)
    + 3. Manual fallback: rm openclaw.json entry + rm ~/.openclaw/agents/<name>/
    + 4. Stop + remove systemd unit
    + 5. Remove .assistant/_state/<name>-*.md
    + 6. Worktree-mode workspace (--remove-workspace flag for worktree/own-workspace)
    # Preserves: .assistant/<name>.{yaml,cron.yaml,openclaw.json5,openclaw.json}
```

These patches are essential for any clean re-install of any profile. Without them, install/uninstall leaves orphaned state.

## What NOT to do (mistakes I made this session)

| Mistake | Operator response |
|---|---|
| Added `every:3m` sprint-tick to CK profile (pattern-copied from RGP) | "wtf what is every 3 min lol ???? THE ONLY FUCKING THING WHICH COULD BE FAST LIKE THIS IS THE root-ghostproxy ai assistant" |
| Added `filesystem-rm` allow for tracked files (auto-delete committed) | "THE AI ASSISTANT IS NOT GOING TO DELETE ANYTHING THAT IS ALREADY COMMITED OR STAGED WITHOUT MY AGREEMENT" (sacrosanct) |
| Added `git commit` to agent tools.allow | (same sacrosanct quote — operator commits, agent never) |
| Surfaced trash-removal batch for "per-file operator approval" | "WHY WOULD THE AI HAVE TO PROPOSE TO REMOVE THE TRASH IT ADDED ITSELF?? ITS SUPPOSED TO BE A FUCKING AUTONOMOUS ASSISTANT" |
| Made surgical patches when proper rewrite was needed | "STOP TRYING TO RUSH AND HACK AND QUICKFIX. WORK PROPERLY" |
| Added verbose comments, version-history markers, dead-code sections | "STOP PUTTING AI SLOP IN THE PROJECT LIKE A RETARD" |
| Surfaced "Approve this plan?" at every step | "I SHOULD NOT NEED TO APPROVE WTF" |
| Blocked online_research (web_search/hf_paper_search) entirely | "there can even be online research when it apply... we love online researches" |
| Treated CK like RGP (3min cadence, sprint-mode prompts) | (same wtf-every-3-min quote) |

## Anti-patterns observed mid-session (also encoded in CK v3 yaml)

- `deletion_of_committed_without_agreement` (R20 violation)
- `surface_when_should_auto_remove` (freeze disguised as careful)
- `over_proposing` (> 1 level-up draft per weekly tick)
- `mass_ingestion_overreach` (online research used as mass-ingestion)
- `self_documentation_in_wiki` (CK v1 wrote profile-circular-knowledge-*.md)
- `brain_audit_without_directive` (CK v1 had monthly-brain-audit cron)
- `cross_project_modification_attempt` (writing outside the repo)
- `pollution_growth_without_acceptance` (> 5× growth-vs-accept ratio)

## How to verify CK v3 is working (post-bootstrap)

```bash
# 1. Check bootstrap session
ls -la ~/.openclaw/agents/circular-knowledge/sessions/
# Expect: at least one fresh .jsonl + .trajectory.jsonl from the bootstrap fire

# 2. Check execution log
ls wiki/log/2026-05-16-ck-bootstrap-execution-batch-*.md
# Expect: at least batch-1.md authored within ~30 min of install

# 3. Check what was rm'd autonomously (untracked clear-trash)
git status --porcelain | wc -l
# Expect: fewer untracked files than before install (the trash signatures rm'd)

# 4. Check operator-decision-queue for tracked-batch Q##
grep -A 5 "ck retroactive" wiki/backlog/operator-decision-queue.md
# Expect: at least one Q## with "Tracked clear-trash batch" + signature list

# 5. Verify R20 was respected (no commits by agent)
git log -5 --format="%an %s"
# Expect: NO commits authored by an agent profile name (only operator commits)

# 6. Check inbox declaration
cat .assistant/_state/circular-knowledge-inbox.md
# Expect: HH:MM ET | BOOTSTRAP | pile_state_pre:NEVER_DEPILED:5.35× | untracked_removed:<n> | surfaced_tracked_batch:1 | ... | post:ok
```

## Recommended next-session start sequence

```bash
# 1. Orient
.venv/bin/python -m tools.gateway orient

# 2. Read this handoff in full

# 3. Check CK bootstrap completion
bin/assistant activity --hours 4

# 4. Read the execution log
cat wiki/log/2026-05-16-ck-bootstrap-execution-batch-1.md   # if it exists

# 5. Read operator-decision-queue for new Q##
bin/assistant promotions list

# 6. Decide on tracked-batch Q##: accept | reject | defer
#    If accept: `bin/assistant resolve Q## accept "remove the fire-N tier-elevation pile"`
#    Then next CK retroactive tick (Sunday 09:00 ET) will execute git rm

# 7. If pile_state still NEVER_DEPILED post-untracked-cleanup, the retroactive
#    cron will surface pollution-pause HIGH urgency. Read + decide.

# 8. Then move on to CR rewrite (apply 21 requirements + R20)
```

## Honest acknowledgements

- This session involved many false-starts. Operator had to redirect me 6+ times (3min cadence, slop, over-surfacing for approval, R20 deletion boundary, mass-ingestion-overreach reframing, etc.)
- The v2 → v3 jump was a proper rewrite, not a surgical patch — the v2 was inheriting too much from RGP's sprint pattern and lacked R20 enforcement
- The `bin/assistant apply-retroactive-batch` command is still TBD. For now the workflow is: operator hand-edits operator-decision-queue.md to mark Q## accepted; next CK tick reads the accepted Q## and executes `git rm`. This is workable but clunky — building the slash command would simplify.
- The auditor's "FABRICATED" false-positives (when agent correctly short-circuits a no-op tick) need their own fix in `_audit_run_for_pseudo_work`. Not done this session.

---

# THE OTHER PROFILES (CR, PS, RGP) — detail

The handoff above is CK-heavy. This section adds the rest.

## continuous-research (CR) — STILL BROKEN

### Current state
- **Uninstalled** (clean via patched `cmd_uninstall`)
- **Profile YAML** at `.assistant/continuous-research.yaml` (v1, ~360 lines)
- **Cron** at `.assistant/continuous-research.cron.yaml` (6 jobs)
- **Vendor configs** preserved
- **Sessions preserved** at `~/.openclaw/agents/continuous-research/sessions/` — 15 .jsonl (forensic value)

### What v1 was doing
Stated role: "external novelty → Layer 1 source-synthesis". 6 cron jobs: `frontier-delta-check every:1h`, `morning-scan` 08:00, `evening-report` 20:00, `start-of-week-deep-dive` Mon 09:00, `end-of-week-summary` Fri 17:00, `monthly-budget-audit` 1st 12:00.

24h output before uninstall:
- 9 `raw/articles/*.md` (Anthropic/OpenAI/Claude news — operator-flagged trash)
- Multiple `wiki/log/2026-05-15-research-watch-*.md` (operator-flagged trash)
- Source-syntheses: Opus 4.7, Mythos, GPT-5.5 ×2, Colossus, AGT, AlphaEvolve
- 2 fabricated audit hits + 2 timeout hits in last 4h

### Bugs

| # | Bug | Evidence |
|---|---|---|
| CR-B1 | Mass external fetching, no operator-relevance filter | 9 untracked news articles never solicited |
| CR-B2 | Fabrication: claims work in 264s window with 0 file mods | Session `d0b131ff` (22:25 ET); 27 tool calls but mismatch summary↔artifacts |
| CR-B3 | Timeout on frontier-delta-check (830s, model-call-started phase) | Session `61730425` (23:17 ET); 45 tool calls mid-flight cut |
| CR-B4 | Mass sister-project README ingestion | ecosystem-projects/src-openarms-* ×13 (operator-named trash) |
| CR-B5 | No retroactive capability | Structural |
| CR-B6 | No anti-pollution gate | Structural |
| CR-B7 | Auditor FABRICATED false-positives on legitimate short-circuits | `tools/assistant.py` `_audit_run_for_pseudo_work` |

### v3 fix plan (applied to CR)

| Req | CR-specific |
|---|---|
| R3 Goldilocks | Cap 1-3 raws per cron firing; daily total cap |
| R6 No garbage | Every raw needs operator-stated relevance OR Q##-mapped trigger. No proactive frontier-scan without trigger. |
| R7 Flow | CR is INGEST lane. Don't author summaries/logs/syntheses (PS+CK's lanes). |
| R11 No freeze | Anti-fabrication: if no operator-relevant signal, inbox 'nothing relevant' + END |
| R13 Anti-pollution | raw/articles/ growth > 5× operator-accept → pause CR |
| R14 Retroactive | CR cleans its own orphan untracked raws (per R20) |
| R15 Online research | CR's lane BY DESIGN, but scoped to operator-stated topics / Q## refs. NOT mass news-feed. |
| R20 Sacrosanct | CR's raws are typically untracked initially → autonomous purge of orphans OK. Tracked raws (operator committed) → NEVER auto-delete. |

**CR-specific addition**: every raw fetched must have `operator_relevance` field in frontmatter linking Q## / operator-directive / current epic.

### CR fix sequence
1. Read sessions `d0b131ff` + `61730425` to confirm bugs
2. Read CR v1 yaml + cron + json5 in full
3. Rewrite v3 (CK v3 pattern: 21 reqs + R20 + tight scope + per-tick caps + retroactive)
4. Install + verify
5. Watch for fabrication/timeout recurrence

---

## pipeline-synthesis (PS) — STILL BROKEN

### Current state
- **Uninstalled**
- **YAML** at `.assistant/pipeline-synthesis.yaml` (v1, ~360 lines)
- **Cron** at `.assistant/pipeline-synthesis.cron.yaml` (6 jobs)
- **Sessions** at `~/.openclaw/agents/pipeline-synthesis/sessions/` — 7 .jsonl

### What v1 was doing
Stated role: "raw backlog → Layer 1 source-synthesis". Cron jobs: `backlog-process-top every:1h`, `morning-batch` 07:00, `evening-backlog-report` 21:00, `start-of-week` Mon 10:00, `end-of-week` Fri 17:30, `monthly` 1st 13:00.

24h output: **75+ trash source-syntheses** at `wiki/sources/*` — the bulk of the operator-named pile.

### Bugs

| # | Bug | Evidence |
|---|---|---|
| PS-B1 | Bulk synthesis with NO operator-relevance filter | 23:31 ET fire synthesized 9 raws ALL in operator-flagged trash zones |
| PS-B2 | No quality gate before synthesizing | FIFO drain, no judgment per raw |
| PS-B3 | Timeout on backlog-process-top (1109s = 18.5min) | Session `d2383d00` (22:24 ET); 61 tool calls mid-flight cut |
| PS-B4 | pipeline_post FAIL (1 pre-existing error) but PS didn't check before adding | 23:31 ET inbox declaration |
| PS-B5 | No retroactive capability | Structural |
| PS-B6 | No anti-pollution gate | Structural |
| PS-B7 | No orphan-detection on its own outputs | Syntheses become orphan (0 inbound) — signal that the raw wasn't worth synthesizing |

### v3 fix plan

| Req | PS-specific |
|---|---|
| R3 Goldilocks | Cap 1-3 syntheses per cron; daily cap 5-10 |
| R6 No garbage | **Relevance gate** before synthesizing: check operator-decision-queue for Q## referencing raw OR raw frontmatter `operator_relevance`. If neither → defer to orphan-raws backlog. |
| R7 Flow | PS is SYNTH lane only. Doesn't ingest, doesn't level-up. |
| R13 Anti-pollution | wiki/sources/ growth > 5× operator-accept → pause PS |
| R14 Retroactive | PS scans its own syntheses; 0-inbound + 0-queue + 30+ days = propose purge per R20 |
| R20 Sacrosanct | PS's syntheses TYPICALLY become tracked (operator commits). Untracked-recent ones → autonomous rm. Tracked → batch Q## for agreement. |

**PS-specific addition**: orphan-detection cron (weekly) that scans PS's past syntheses and proposes purge of unreferenced ones.

### PS fix sequence
1. Read sessions `444df6f9` (23:31 successful but 9 trash) + `d2383d00` (22:24 timeout)
2. Read PS v1 yaml + cron + json5 in full
3. Rewrite v3 (relevance gate first, per-tick caps, R20, retroactive orphan-detection)
4. Install + verify
5. Monitor first weekly retroactive: does PS detect its own orphans?

---

## root-ghostproxy-rollout (RGP) — UNINSTALLED, mission preserved

### Current state
- **Uninstalled**
- **YAML** at `.assistant/root-ghostproxy-rollout.yaml` (v2, ~750 lines)
- **Cron** at `.assistant/root-ghostproxy-rollout.cron.yaml` (6 jobs including the operator-authorized 3min sprint-tick)
- **Sessions preserved**: 2 sessions (`aff6b0b3` morning-briefing fire + `3d523b84` sprint-tick fire)

### What RGP is (DIFFERENT FROM CK/CR/PS)

RGP is a **cross-project cascade-driver** — its purpose is to **fix the root-ghostproxy sister project** (separate repo at `~/`). Operator-stated mission per `wiki/log/2026-05-15-PRE-COMPACT-HANDOFF-three-profiles-live-plus-root-ghostproxy-profile-spec.md`:
- OBSERVE the second brain's existing record of root-ghostproxy (2 directive notes + 10 backlog modules + 1 epic)
- AUTHOR cascade-candidates LOCALLY at `wiki/domains/cross-domain/cascade-candidate-root-ghostproxy-*.md`
- NEVER edit root-ghostproxy directly (cross-project boundary)
- SURFACE proposals so operator copies approved cascade-candidates into actual root-ghostproxy repo

### Operator-authorized 3min sprint-tick (NOT a bug for RGP)

Operator 2026-05-15: *"PUT IT EVERY 3min if we need"* — for RGP's overnight sprint scenario.

Operator 2026-05-16: *"THE ONLY FUCKING THING WHICH COULD BE FAST LIKE THIS IS THE root-ghostproxy ai assistant"* — confirms 3min is RGP-only.

The 3min cadence is the bug WHEN PASTED ONTO OTHER PROFILES. For RGP it's correct.

### What RGP produced in its short run
- 4 cascade-candidate files (Q86-Q89 in operator-decision-queue):
  - `cascade-candidate-root-ghostproxy-m001-reframe-as-audit-of-existing-agents-md-claude-md-2026-05-16.md`
  - `cascade-candidate-root-ghostproxy-scope-clarification-selfdef-boundary-2026-05-16.md`
  - `cascade-candidate-root-ghostproxy-self-update-observe-upstream-head-before-drafting-modules-2026-05-16.md`
  - `cascade-candidate-root-ghostproxy-state-divergence-upstream-already-advanced-2026-05-16.md`
- 1 morning briefing log

### Bugs

| # | Bug | Status |
|---|---|---|
| RGP-B1 | Bootstrap `first-fire` unrecognized on first install | FIXED in `cmd_install` patch (first-fire one-shot handler) |
| RGP-B2 | Sprint-tick `every:3m` unrecognized | FIXED in `translate_schedule` patch |
| RGP-B3 | R20 not enforced — RGP could in theory auto-delete its own cascade-candidate files (cross-project boundary already prevents touching ~/root-ghostproxy directly) | Need v3-style R20 retrofit |
| RGP-B4 | No coordination with CR/PS — if their pollution isn't fixed, RGP's drafts reference polluted Layer-1 sources | Sequencing dependency |

### RGP fix plan (after CR + PS clean)

Most of RGP v2 is OK. Additions:
- R20 retrofit on cascade-candidate files (untracked autonomous rm OK; tracked needs operator agreement)
- Coordination check: RGP reads Layer-1 wiki/sources/ as observation substrate. If wiki/sources/ contains trash, RGP's drafts will be bad. CR + PS + pile-cleanup MUST come first.

### RGP install sequence (AFTER CR + PS v3 verified)
1. Verify CK has depiled the trash + operator-approved tracked-batch
2. Verify CR + PS v3 producing proper output for a week
3. Add R20 retrofit to RGP v2 yaml + cron + json5
4. Re-install RGP
5. Watch first bootstrap

---

# REPO CLEANUP STATE (the pile)

CK v2 bootstrap audit identified the pile:

| Category | Count | Action |
|---|---|---|
| **Total agent-authored in pile** | **316** | NEVER_DEPILED verdict, ratio 5.35× |
| Operator-resolved (queue accept OR operator hand-edit) | 59 | KEEP |
| **Untracked clear-trash** | **66 files** | CK v3 bootstrap autonomously rm's (running now) |
| **Tracked clear-trash** | **~250 files** (mostly fire-N tier-elevation logs 2026-05-08) | CK v3 surfaces as ONE batch Q## per signature class → needs operator `bin/assistant resolve Q## accept` |
| Q##-pending (unresolved in queue) | 7-10 | KEEP-PENDING |
| Load-bearing (≥1 inbound link OR operator-territory) | rest | KEEP |

### The 13 specific untracked clear-trash (B1.1 from v2 batch)
- wiki/log/2026-05-15-purge-summary*.md (×3)
- wiki/log/2026-05-15-research-watch-*.md (×5)
- wiki/log/2026-05-16-research-watch-morning.md
- wiki/log/2026-05-15-ck-weekly-distillation-surfacings.md
- wiki/log/2026-05-15-2026-05-15-pipeline-synthesis-evening-backlog-status-report.md
- wiki/log/2026-05-15-PRE-COMPACT-HANDOFF-three-profiles-live-plus-root-ghostproxy-profile-spec.md
- wiki/log/2026-05-16-root-ghostproxy-rollout-sprint-morning-briefing.md

### The tracked pile (~250 files)
- `wiki/log/2026-05-08-fire-*-tier-elevation-candidate-*.md` (~40 — bulk spam)
- `wiki/log/2026-05-08-sustained-feedback-loop-*` / `pareto-*` / `tier-promotion-readiness-*` (~10)
- `wiki/log/2026-05-15-research-watch-{frontier-delta,lightweight-scan-*}.md` (4 tracked)
- `wiki/log/2026-04-28-session-log-post-anthropic-3-layer-stack-*` (1)
- `wiki/patterns/01_drafts/*.md` (88 MIXED — needs per-file pass)
- `wiki/lessons/01_drafts/*.md` (36 MIXED)
- `wiki/decisions/01_drafts/*.md` (11 MIXED)
- `wiki/sources/src-*.md` (109 tracked sources — MIXED; some load-bearing, some dupes)

MIXED categories will need per-file or per-signature operator judgment. CK v3 surfaces as per-class Q## when heuristics insufficient.

---

# SESSION TIMELINE (6 phases)

| Phase | What happened |
|---|---|
| **1. Orient + understand state** | Read brain + spine + models + principles. Demonstrated comprehension. |
| **2. Build RGP profile** | 3min sprint, autonomous overnight cleanup. Built yaml + cron + json5. Operator approved install A. Discovered `first-fire` + `every:3m` weren't translated. Patched `translate_schedule`. Re-installed. Produced 4 cascade-candidates + morning briefing. |
| **3. Discover AI assistant profiles broken** | Operator: "the AI assistants are completely broken, focus". Investigated sessions: CR fabrication (22:25 ET, 264s, 0 mods), CR timeout (23:17, 13min50s), PS timeout (22:24, 18.5min). Root cause: isolated workspace + agent fabricating when tools fail silently. |
| **4. "kil remove all openclaw"** | Uninstalled 4 profiles. Discovered `cmd_uninstall` left 21 orphaned cron jobs. Patched `cmd_uninstall` (call `openclaw agents delete --force` + cleanup). Clean state achieved. |
| **5. "Fix CK first, then CR/PS"** | Rewrote CK v2 (tighter scope, retroactive). Bootstrap produced PROPOSAL not EXECUTION. Operator angry: "WHY WOULD THE AI HAVE TO PROPOSE TO REMOVE THE TRASH IT ADDED ITSELF?? AUTONOMOUS!" Rewrote v3 (autonomous untracked-rm + tracked-batch surface + R20). Removed 3min sprint-tick (RGP slop). |
| **6. CK v3 install + handoff** | Installed CK v3. Bootstrap fires delete-after-run. Wrote handoff (CK-only). Operator: "is this all about circular knowledge?" → appending other-profiles half (this section). |

---

# OPERATOR PREFERENCES LEARNED THIS SESSION

| # | Preference | Pattern |
|---|---|---|
| OP-1 | NEVER paraphrase operator-directives | Quote verbatim everywhere |
| OP-2 | AUTONOMOUS within bounds, not approval-gated | Agent acts on clear cases; surfaces only AMBIGUOUS / tracked-for-agreement |
| OP-3 | NO AI slop | Tight files, single statement of each principle, no version markers / dead-code |
| OP-4 | DO THE WORK, don't surface for approval at every step | When operator approved direction, EXECUTE |
| OP-5 | Cadence matches scope, NOT pattern-copy | RGP=3min (authorized). CR/PS=hourly. CK=weekly. Don't paste. |
| OP-6 | Online research IS desired | For verification + anchors + cross-reference. NOT mass ingestion. |
| OP-7 | R20 SACROSANCT | Untracked autonomous. Tracked = batch Q## → operator accept → agent executes git rm → operator commits. |
| OP-8 | Build forward, never revert + restart | SUPERSEDES drafts, not restarts |
| OP-9 | Goldilocks twice | Per-proposal AND per-tick |
| OP-10 | No garbage, no mindless promote | Gate fails → defer (correct outcome) |

---

# FAILURE PATTERNS CALLED OUT THIS SESSION

| Anti-pattern | Operator's exact response |
|---|---|
| Pattern-copy 3min cron from RGP to CK | "wtf what is every 3 min lol ????" |
| Surface untracked clear-trash for approval | "WHY WOULD THE AI HAVE TO PROPOSE TO REMOVE THE TRASH IT ADDED ITSELF??" |
| Add git rm + git commit to agent tools | "AI ASSISTANT IS NOT GOING TO DELETE ANYTHING COMMITED OR STAGED WITHOUT MY AGREEMENT" |
| Surface every plan for approval | "I SHOULD NOT NEED TO APPROVE WTF" |
| Surgical patches instead of proper rewrite | "STOP TRYING TO RUSH AND HACK AND QUICKFIX. WORK PROPERLY." |
| Verbose comments / version markers / dead sections | "STOP PUTTING AI SLOP IN THE PROJECT LIKE A RETARD" |
| Block online research entirely | "we love online researches" |
| Make handoff CK-only | "is this all about circular knowledge ? wtf ????" |

---

# WORK QUEUE — PROPER ORDER OF OPERATIONS

```
1. CK bootstrap completes (~30min from 12:12 UTC install)
   ↓
2. Operator reviews bootstrap execution log + tracked-batch Q##
   ↓
3. Operator accepts/rejects tracked-batch Q##
   ↓
4. Operator commits the changes (CK never commits per R20)
   ↓
5. Apply v3 pattern to CR
   - Read sessions d0b131ff (fabricated) + 61730425 (timeout)
   - Read CR v1 yaml + cron + json5 in full
   - Rewrite v3 (21 reqs + R20 + relevance gate + per-tick caps + retroactive)
   - Install + verify
   ↓
6. Apply v3 pattern to PS
   - Read sessions 444df6f9 (trash synth) + d2383d00 (timeout)
   - Rewrite v3 (relevance gate FIRST, per-tick caps, R20, orphan-detection)
   - Install + verify
   ↓
7. Reinstall RGP (after CR + PS verified)
   - Add R20 retrofit to v2
   - Install
   - 3min sprint OK (operator-authorized)
   ↓
8. Build `bin/assistant apply-retroactive-batch <Q##>` slash command
   ↓
9. Fix `_audit_run_for_pseudo_work` false-positives
   - Distinguish "no work to do" (correct short-circuit) from "claimed work but no artifacts" (true fabrication)
   ↓
10. Investigate model-call-started timeout root cause
    - 13-18 min hangs on CR + PS
    - Anthropic API? Gateway routing? Prompt too long?
```

---

# CRITICAL REFERENCE FILES (read first on next session)

1. **This handoff** (you're reading)
2. **CK v3 profile** — `.assistant/circular-knowledge.yaml` (gold-standard pattern)
3. **CK v3 cron** — `.assistant/circular-knowledge.cron.yaml`
4. **CK v3 json5** — `.assistant/circular-knowledge.openclaw.json5`
5. **CK v2 audit batch** — `wiki/log/2026-05-16-ck-bootstrap-pile-depile-batch-1.md`
6. **CK v3 execution batch** (when ready) — `wiki/log/2026-05-16-ck-bootstrap-execution-batch-1.md`
7. **2026-05-15 PRE-COMPACT-HANDOFF** — `wiki/log/2026-05-15-PRE-COMPACT-HANDOFF-three-profiles-live-plus-root-ghostproxy-profile-spec.md` (RGP mission)
8. **CR v1 forensic sessions** — `~/.openclaw/agents/continuous-research/sessions/{d0b131ff,61730425}*.jsonl`
9. **PS v1 forensic sessions** — `~/.openclaw/agents/pipeline-synthesis/sessions/{d2383d00,444df6f9}*.jsonl`
10. **Patched `tools/assistant.py`** — `tools/assistant.py` (translate_schedule + first-fire + cmd_uninstall)

---

## Relationships

