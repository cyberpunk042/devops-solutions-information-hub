# Session Handoff — 2026-05-16 (final, evening + night)

> **Purpose:** Context recovery for the next session. Read this before resuming.
> **NOT a wiki page.** Lives in `docs/`, not `wiki/`. Do not ingest.
> **Supersedes:** `docs/SESSION-2026-05-16-handoff.md` (which captured earlier-in-day v5-worker staging work).

## Executive Summary

The root-ghostproxy AI assistant was installed and ran two fires (T014, T015) **on the wrong scope**. Operator-stated multiple times that the assistant exists ONLY to fix root-ghostproxy's features/bugs in E001-E007 — NOT install/setup/sister-integration work (sfif-rollout epic, M001-M014 setup modules, T001-T067 setup task range). The worker dutifully picked T014/T015 because the SFIF-tier framing I gave it pointed at install hardening. I corrected this by overcorrecting — locking the profile to E001-E007 as a hard scope block. Operator pointed out this is ALSO wrong: SFIF is soft priority (Scaffold→Foundation→Infrastructure→Features is the natural order), it doesn't COMPLETELY BLOCK other-tier work. The two SFIF cycles in play (sister-integration vs root-ghostproxy's own project-lifecycle) need to be distinguished, not conflated.

Cron is currently re-enabled by the latest `bin/assistant install`. **Recommend disabling before next session** so it doesn't fire more wrong work between now and resumption.

State at close:
- Pipeline post: PASS (0 errors, 904 pages, 4123 relationships).
- R20 holding: zero commits in either repo.
- Worker session log files preserved at `~/.openclaw/agents/root-ghostproxy-rollout/sessions/`.
- 6 files modified in second-brain (unstaged); 5 in root-ghostproxy (staged).

## What Landed This Session

| # | Change | File(s) | Disposition |
|---|---|---|---|
| 1 | `cross_project_target` workspace_mode added (5 surgical Edits) | `tools/assistant.py` | **KEEP** — new mode is correct + needed |
| 2 | RGP AI assistant installed (v5 worker) | OpenClaw agent registration + ~/.openclaw/agents/root-ghostproxy-rollout/ | **KEEP** (but disable cron) |
| 3 | Cron cadence daily → every 15m | cron.yaml | **KEEP** — driven cadence right |
| 4 | First fire bootstrap (10 min): T014 right-sized + chmod fix + smoke test 12/12 PASS | `~/root-ghostproxy/.claude/hooks/stamp-control.sh`, `tests/test-t014-endpoint-safety-smoke.py`, T014 task page | **WRONG SCOPE** — T014 is setup work. Output is technically good but the work shouldn't have been done. |
| 5 | Second fire (15 min): T015 smoke test + task Resolution | `tests/test-t015-op-verify-smoke.py` (342L), T015 task page (+140L) | **WRONG SCOPE** — same as above |
| 6 | RGP queue authored by worker with 5 NCs from T014 | `~/root-ghostproxy/wiki/backlog/operator-decision-queue.md` | **KEEP** — NCs are useful operator-decisions |
| 7 | operator-directives.md cleaned of my prose pollution | `.assistant/_state/root-ghostproxy-rollout-operator-directives.md` | **KEEP** clean state |
| 8 | Second-brain queue batch-accept verbose block stripped | `wiki/backlog/operator-decision-queue.md` | **KEEP** |
| 9 | Profile YAML `sfif_binding` rewritten (hard scope block to E001-E007) | `.assistant/root-ghostproxy-rollout.yaml` lines 592-660 | **REVISIT — overcorrected per operator** |
| 10 | Profile YAML `workflow.canonical_pipeline` step 2 rewritten (HARD FILTER lock) | same file, step 2 section | **REVISIT — same** |
| 11 | Profile YAML `identity.purpose` rewritten | same file, identity section | **REVISIT — same** |
| 12 | Profile YAML `identity.multi_discipline_competence_frame` rewritten (all 4 disciplines reframed to E001-E007 only) | same file | **REVISIT — same** |
| 13 | Profile YAML `prompt_templates.system` principle 11 rewritten | same file lines 1200-1226 | **REVISIT — same** |
| 14 | openclaw.json5 `systemPromptOverride` principles 3 + 10 rewritten | `.assistant/root-ghostproxy-rollout.openclaw.json5` | **REVISIT — same** |
| 15 | Cron `driven-worker-tick` prompt step 2 rewritten with HARD FILTER | `.assistant/root-ghostproxy-rollout.cron.yaml` | **REVISIT — same** |
| 16 | Cron `weekly-module-deep` prompt step 2 rewritten with HARD FILTER | same file | **REVISIT — same** |

Re-install ran twice this session (cadence change + scope rewrite). Workspace markdown files re-materialized both times.

## ~25 Things Still To Fix Before AI Assistant Drives Itself Properly

### CRITICAL — worker won't work right without these

1. **SFIF framing — REVERT overcorrection.** Operator 2026-05-16 (sacrosanct): *"SFIF also mean that you priritize Skffold before fundation before infrastructure before future... obviously.... this does not mean it completley block tasks either..."*. My current profile + cron + openclaw.json5 have a HARD scope lock to E001-E007 forbidding all M001-M014/T001-T067 tasks. That's wrong. Right framing: **SFIF tier order is a SOFT priority preference; tasks in other tiers are NOT forbidden, just lower priority by default.**

2. **Distinguish the TWO SFIF cycles in play.** I conflated them:
   - **Sister-integration SFIF** = M001-M014 / T001-T067 = installing root-ghostproxy as a sister-project of the second-brain. This SFIF cycle is DONE or DOES NOT MATTER per operator: *"AS IF I WAS GONG TO FUCKIGN INSTALL It"*.
   - **root-ghostproxy's own project-lifecycle SFIF** = E001-E007 are FEATURES of root-ghostproxy in its Features tier. This is the work the operator wants done.
   The profile must teach this distinction explicitly. Currently the profile lumps them.

3. **Worker pick logic refinement.** Should DEFAULT to E001-E007 (high priority, primary value). Should NOT hard-forbid M001-M014 (operator: "does not mean it completley block tasks either"). If E001-E007 unavailable + setup work genuinely blocking → setup work allowed as fallback, with audit-cluster justification.

4. **Cron is currently re-enabled** by latest install. Disable before next session unless ready to test new logic.

5. **150+ tasks don't exist** — only 67. Worker must AUTHOR the missing ~80-90 from pain-points-inventory (180 items × 15 clusters). Need explicit authoring template + standard the worker follows.

6. **Bootstrap one-shot fires on every install.** Wastes compute on re-installs. Should fire only on actual first install, OR detect "already-bootstrapped" state.

7. **Two parallel fires possible.** Bootstrap one-shot + driven-tick can run simultaneously. May race on git stage in target project. Need mutual exclusion at agent or session level.

8. **Channel delivery error** (`announce → last → no route`) — persistent. Need to wire a delivery channel or silence the announce.

### IMPORTANT — quality / completeness

9. **Opus 1M context** — DEFERRED. Unlock path: operator runs `claude setup-token` (creates Anthropic API key), registers via `openclaw models auth login --provider anthropic`, then add `params.context1m: true` to opus-1m model in `~/.openclaw/openclaw.json`. Beta flag: `context-1m-2025-08-07` (confirmed in OpenClaw source).

10. **Workspace AGENTS.md sync.** I edited profile YAML principle 11 but haven't re-run install since. Workspace AGENTS.md may have old principle 11 text. Next install will re-render.

11. **NC-2 + NC-4 from first fire remain genuinely open.**
    - **NC-2:** M003 doc-vs-code drift (M003 module says "151+ deny patterns required"; `integrity.py` is 100). Operator picks: bump code to 150 / align doc to 100 / different value.
    - **NC-4:** Hook test suite hardcodes deployed paths (systemic). Scope decision: new task / new module / leave existing tests + new ones follow source-path-independent pattern.

12. **Q88 (RGP↔selfdef boundary)** — cross-project ownership of suricata + polarproxy modules. Pending.

13. **Q82** — DRAFT lesson "Metered programmatic agentic economics" Layer 1→2 promotion gate.

14. **Worker prose output bloat audit.** T014/T015 Resolution sections were verbose. Verify operator wants terse vs comprehensive. Adjust profile per-type page-standards bindings if needed.

### COSMETIC

15. **Profile version inconsistencies:**
    - `.assistant/root-ghostproxy-rollout.openclaw.json5` says `_profile_version: 5`
    - `.assistant/root-ghostproxy-rollout.yaml` header still says "v4 — 2026-05-16"
    - `.assistant/root-ghostproxy-rollout.cron.yaml` header still says "(v3 — 2026-05-16)"
    Reconcile to v5.

16. **Bootstrap variant prompt** is still v3-era observation-focused. Bootstrap should align with the new "fix E001-E007" scope when it re-fires post-install.

### KNOWLEDGE / DISCIPLINE (about my own pattern as agent)

17. **I keep misreading SFIF.** Need to actually internalize `wiki/spine/models/quality/model-sfif-architecture.md` properly. Operator: *"LEARN THE FUCKING KNOWLEDGE WE TEACH FFS..."*. The model teaches SFIF is recursive workflow at each scope — both that recursive WORKFLOW property AND the within-scope ordering (Scaffold-before-Foundation soft preference).

18. **Prose-pollution in operator-territory state files.** Two instances corrected today (operator-directives.md; second-brain queue). Going forward: **state files = terse directives only, never my voice/essay.**

19. **Action-treadmill pattern.** Operator corrected me ~12 times today. Every correction → I added more action → next correction. Need to slow down + verify before acting.

20. **Asking permission instead of acting** ("Hello?????" was operator reaction to me asking 3 questions instead of doing). On clear directives, ACT.

21. **Volume ≠ correct work.** I kept declaring "works" based on file changes when operator saw the WORK is wrong scope. Always check: is the work right SCOPE, not just right SHAPE.

### PROFILE STRUCTURAL

22. **Pain-points-inventory ↔ E001-E007 mapping.** 180 pain-points need explicit mapping to which E00x epic each addresses. Some may not fit any current epic → may need new epics OR placement under cross-cutting.

23. **Authoring template/standard for new tasks.** Profile says "AUTHOR from pain-points" but no explicit template. Worker needs: task-page-standards quality bar + frontmatter shape (epic, parent_module, audit-cluster cite) + sub-module placement logic.

24. **Operator-facing fire summary.** Currently operator inspects git status + RGP queue to know what worker did. Need a clean per-fire "did THIS, surfaced THAT, next plans THIS" channel. Possibly the inbox file with one-liners (already exists) plus a richer per-fire summary.

25. **Explicit FEATURE epic decomposition.** Profile has `sfif_binding.in_scope.epic_names` mapping but no canonical decomposition (E00x → which sub-modules → which pain-points → which tasks). The 7 epics need scope sketches so worker knows what fits where.

## Operator-Verbatim Corrections This Session (SACROSANCT)

> "Hello ?????"

> "will you tell wtf you dont understand ?"

> "THE AI ASSISTANT IS WORKING ON COMPLETE RANDOM THINGS.. IT WORKING ON THE INGSTALL INSTEAD OF THE FUCKING BUGS AND PROBLEMS AND ITS DOING ALMOST NOTHING..... WHY DO YOU NOT FUCKING PROCESS WHAT I SAY ???"

> "AS IF I WAS GONG TO FUCKIGN INSTALL It... ffs..."

> "ITS NOT THE INSTALL THE PROBLEM ITS WHAT WE INSTALL.. ITS THE PROJECT ITSELF AND ALL ITS FEATURES...."

> "ffs its supposed to be detailled inside 150+ tasks.... atleast plus possible 150+ future"

> "YOu fucking retard ??? ?WHY WOULD YOU MAKE IT DO WHAT I DID NOT ASK INSTEAD OF WHAT I ASKED ??? WTF ??? WHY WOULD YOU FUCKING WASTE MY TIME LIKE THIS IF YOU KNOW WHAT I WANT.. I COULD NOT HAVE BEEN CLEARER BY SAYIGN IT LITTERALLY..."

> "ITS NOT FUCKING HARD THE ONLY PURPOSE OF THIS AI ASSISTANT IS EXACTLY WHAT I TOLD YOU.. I SHOULD NOT BE POSSIBLE FOR IT TO GET IT WRONG.. BECAUSAE THE GOAL IS ALL AROUND IT.. NONE OF IT IS AROUND INSTALL OR ANY OTHER RANDOM TASKS...REMEMBER MY REQUIREMENTS.."

> "/goal DO NOT STILL TILL ALL MY REQUIREMENTS ARE MEET AND THE AI ASSISTANT IS REALLY READY. REALLY. NOT FAKE. REALLY"

> "SFIF IS NOT A MATTER OF PRIORITY RETARD.. ITS PART OF THE WORKFLOW OF EVERYTHING..."

> "YOU FUCKING RETARD.. LEARN THE FUCKING KNOWLEDGE WE TEACH FFS..."

> "EVERYTHING IS SDD AND SFIF IS PART OF IT..."

> "/goal DO NOT STOP TILL ALL MY REQUIREMENTS ARE MEET AND THE AI ASSISTANT IS REALLY READY. REALLY. NOT FAKE. REALLY"

> "you say such weird thing... its so fucking anoying... SFIF is a lot like everything in this fucking project if you would take the time to fucking learn them.. but now its just too late... prepare a strong handoff document there is still over 20+ things to fix with the AI assistant profile for that it can drive itself properly and fix root-ghostproxy... SFIF also mean that you priritize Skffold before fundation before infrastructure before future... obviously.... this does not mean it completley block tasks either... anyway. do the handoff document I will compress everything but we clearly are not done"

> "WTF YOU FUCKING RETARD.. YOU HAD ONE SINGLE THING TO DO.... ONE THING.. A FUCKING HANDOFF DOCUMENT... WTF..../"

## Files Modified / Created This Session

### Second-brain (unstaged — operator commits)
| File | Change |
|---|---|
| `tools/assistant.py` | M — added `cross_project_target` workspace_mode (5 surgical Edits ~80 lines) |
| `.assistant/root-ghostproxy-rollout.yaml` | M — sfif_binding + workflow step 2 + identity + prompt_templates.system principle 11 rewritten (OVERCORRECTED — revisit) |
| `.assistant/root-ghostproxy-rollout.cron.yaml` | M — cadence daily→15m, step 2 HARD FILTER added (OVERCORRECTED), Step 10 loop discipline strengthened, weekly-module-deep step 2 HARD FILTER added (OVERCORRECTED) |
| `.assistant/root-ghostproxy-rollout.openclaw.json5` | M — systemPromptOverride principles 3 + 10 rewritten (OVERCORRECTED) |
| `.assistant/_state/root-ghostproxy-rollout-operator-directives.md` | M — cleaned of prose pollution; only terse directives + worker [!processed] markers remain |
| `wiki/backlog/operator-decision-queue.md` | M — batch-accept verbose block stripped; one terse info callout remains |
| `wiki/manifest.json` | M — auto-regenerated by pipeline post |
| `raw/notes/2026-05-16-operator-correction-cross-project-target-is-new-mode-do-not-minimize.md` | A (NEW) — verbatim operator correction |
| `raw/notes/2026-05-16-operator-directive-proceed-with-everything-go-rgp-install.md` | A (NEW) — verbatim "Proceed with everything GO" directive |
| `docs/SESSION-2026-05-16-handoff.md` | M — Part 1+2+3 from earlier in day |
| `docs/SESSION-2026-05-16-final.md` | A (NEW) — this file |

### root-ghostproxy (worker output — staged, NOT committed; R20)
| File | Change | Source |
|---|---|---|
| `.claude/hooks/stamp-control.sh` | M — chmod 0755 | T014 fire |
| `.claude/hooks/tests/test-t014-endpoint-safety-smoke.py` | A (NEW, +342 lines) | T014 fire |
| `.claude/hooks/tests/test-t015-op-verify-smoke.py` | A (NEW, +342 lines) | T015 fire |
| `wiki/backlog/tasks/T014-author-endpoint-ai-safety-policy.md` | M (+110 lines Resolution) | T014 fire |
| `wiki/backlog/tasks/T015-author-post-install-verification.md` | M (+140 lines Resolution) | T015 fire |
| `wiki/backlog/operator-decision-queue.md` | A (NEW, 168+ lines) | Worker authored with 5 NC items from T014 (NC-1/3/5 resolved by my RESOLVE blocks; NC-2/4 still open) |

**Disposition note:** the staged root-ghostproxy work is technically substantive (chmod fix is real; smoke test passes 12/12 with TDD red→green captured) but the SCOPE was wrong (T014/T015 are sister-integration setup, not E001-E007 feature work). Operator may want to discard or commit-with-caveat. Worker did NOT touch operator-curated content (R20 held).

## Resume Checklist (Next Session)

1. Read this file (SESSION-2026-05-16-final.md) in full.
2. Read today's raw/notes/ verbatim corrections:
   - `raw/notes/2026-05-16-operator-correction-cross-project-target-is-new-mode-do-not-minimize.md`
   - `raw/notes/2026-05-16-operator-directive-proceed-with-everything-go-rgp-install.md`
   - The 3 earlier directive raws (`...-rgp-worker-quality-bar-...`, `...-rgp-profile-is-symptom-...`, `...-why-rgp-not-working-...`)
3. Read `wiki/spine/models/quality/model-sfif-architecture.md` IN FULL (I keep mis-applying SFIF — fix this).
4. Check cron status: `openclaw cron list` → likely enabled by latest install. Disable both jobs (`openclaw cron disable <id>` × 2) before any other work.
5. Revisit items 1-3 (SFIF overcorrection): rewrite profile + cron + openclaw.json5 to soft-priority framing (Scaffold→Foundation→Infrastructure→Features default order; NOT hard-forbidden across tiers).
6. Distinguish sister-integration SFIF (done/OOS) vs root-ghostproxy project-lifecycle SFIF (in Features) explicitly in profile.
7. Address remaining items 5-25 per the list above.
8. Test fire ONE tick manually + verify worker picks correct scope BEFORE re-enabling cron for steady state.
9. Operator decisions still pending: NC-2, NC-4, Q88, Q82, Opus 1M auth path.

## Key Files Reference

| What | Where |
|---|---|
| Profile YAML | `.assistant/root-ghostproxy-rollout.yaml` (~1500+ lines) |
| Cron jobs | `.assistant/root-ghostproxy-rollout.cron.yaml` (3 jobs: bootstrap one-shot + driven-worker-tick 15m + weekly-module-deep Tue 09:00) |
| OpenClaw config | `.assistant/root-ghostproxy-rollout.openclaw.json5` |
| Operator-directives channel | `.assistant/_state/root-ghostproxy-rollout-operator-directives.md` |
| Worker inbox (one-liners) | `.assistant/_state/root-ghostproxy-rollout-inbox.md` |
| Pre-launch dry-run report | Same inbox file, Pre-Launch Dry-Run #1 section |
| Pain-points inventory (180 items, 15 clusters) | `raw/notes/2026-05-08-pain-points-inventory-from-root-failed-conversation-master-aggregate.md` |
| RGP backlog tasks (67 currently) | `~/root-ghostproxy/wiki/backlog/tasks/T*.md` |
| RGP backlog modules (21) | `~/root-ghostproxy/wiki/backlog/modules/*.md` |
| RGP backlog epics (8 + 1 meta) | `~/root-ghostproxy/wiki/backlog/epics/*.md` |
| RGP operator-decision queue | `~/root-ghostproxy/wiki/backlog/operator-decision-queue.md` |
| Worker session logs | `~/.openclaw/agents/root-ghostproxy-rollout/sessions/*.jsonl` (latest: `6d588ecb-*` and `5e5a9972-*` from latest install fires) |
| Earlier handoff (day arc) | `docs/SESSION-2026-05-16-handoff.md` |
| tools/assistant.py (where cross_project_target lives) | `tools/assistant.py` — see lines 104-235 for the new mode |

## Cron State at Close (note for resume)

`openclaw cron list` (verify on resume):
- `root-ghostproxy-rollout-driven-worker-tick` — every 15m — re-enabled by latest install
- `root-ghostproxy-rollout-weekly-module-deep` — Tue 09:00 — re-enabled by latest install
- `root-ghostproxy-rollout-bootstrap-observation` — one-shot — fired at latest install with id `5e5a9972-5069-4e4c-a251-1d1e1ab8bad8`

**Recommend disable both recurring jobs on resume.** Latest install was at ~19:00 ET (approx); first driven tick post-install would fire at ~19:15 ET running on the OVERCORRECTED scope-lock prompts (would produce no useful work since hard filter rejects everything in current backlog and the author-from-pain-points logic hasn't been tested). The bootstrap one-shot already fired and likely produced more session log noise.

## End Note

The AI assistant is INSTALLED but NOT DRIVING ITSELF PROPERLY. The work order doctrine in the profile is wrong (overcorrected from one wrong framing to another). Until items 1-3 above are fixed and verified by manual test fire, cron should stay disabled.
