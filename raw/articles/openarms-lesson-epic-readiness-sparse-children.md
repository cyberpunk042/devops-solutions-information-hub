---
title: "Epic readiness math is wrong when an epic has implicit goals beyond its current children"
type: lesson
domain: learnings
status: active
confidence: high
maturity: seed
created: 2026-04-14
updated: 2026-04-14
tags: [methodology, epic-readiness, harness, computation, sparse-children, methodology-bug, e013]
related:
  - wiki/backlog/epics/E013-usage-dashboard-statusline.md
  - wiki/domains/architecture/usage-dashboard-research.md
  - wiki/domains/architecture/usage-dashboard-findings.md
  - wiki/domains/learnings/lesson-methodology-battle-tested.md
---

# Epic Readiness Math Is Wrong With Sparse Children

## Summary

The harness computes epic readiness as the average of its child task readiness. This is only correct when the children fully cover the epic's goals. If an epic has implicit goals that have not yet been broken down into child tasks, the average is a mathematical artifact that does not reflect actual progress. **The first child task to complete will flip the epic to 100% even if the epic's real work is barely started.**

This bit me on 2026-04-14 with E013 (Usage Dashboard and Status Line). I wrote a single research spike (T115) as the first concrete step toward unblocking the epic. T115 completed cleanly: `status: done`, `readiness: 100`, both stages (document + design) committed. The harness then recomputed E013's readiness as `100 / 1 = 100%` and flipped the epic from `status: draft` / `readiness: 0` to `status: review` / `readiness: 100`.

The number was correct given the formula. The number was completely wrong as a representation of reality — the epic still had 14 implementation tasks pending across two distinct tracks (Track A status line, Track B dashboard).

## Evidence

The state transition that triggered the lesson:

```
Before T115 launched:
  E013.status = draft
  E013.readiness = 0
  E013.children = []  (epic existed but had no child tasks)

T115 created:
  E013.children = [T115]
  T115.status = active
  T115.readiness = 0
  → E013.readiness = average([0]) = 0  (still correct)

T115 completed (document + design stages):
  T115.status = done
  T115.readiness = 100
  → E013.readiness = average([100]) = 100  ← THE BUG
  → harness flipped E013.status = review
```

The epic's frontmatter went from this:

```yaml
status: draft
readiness: 0
```

to this:

```yaml
status: review
readiness: 100
```

— in a single agent run that produced one research spike. The epic's actual scope (per its body and the operator directives) is "build a status line track AND a separate dashboard command, both with cost/context/cycle/week tracking, exportable data, prior-art integration, single-instance semantics" — none of which T115 implemented or even claimed to.

## Root Cause

`scripts/methodology/recalculate-epic.cjs` (or wherever the recompute lives in the v9 harness — look there) applies the formula `epic.readiness = sum(child.readiness) / count(children)` and flips status thresholds based on the result:

- 0 → `draft` or `active` depending on prior state
- 1-99 → `in-progress` / `active`
- 100 → `review`

The formula assumes children FULLY cover the epic. It has no concept of "the epic has more goals than the current child set covers" because there is no machine-readable representation of those implicit goals. The epic body (markdown, free-form) holds them, but the harness only reads frontmatter and child list.

This is the same class of issue as `lesson-specific-done-when.md` (generic Done When items let agents satisfy criteria trivially) but at a higher level of the hierarchy:

- **Task level**: vague Done When → agent satisfies vaguely → "done" doesn't mean done
- **Epic level**: sparse children → harness averages over empty set → "100%" doesn't mean complete

Both reduce to: **the methodology only knows what is structurally encoded; everything in prose is invisible to it.**

## What is wrong

1. **The flip happens silently.** The harness recomputes readiness on every task completion and writes the new value to the epic file. There is no warning, no concern, no notice that "this epic now reports 100% based on a child set that may not cover its goals." The first sign is the operator opening the epic file and noticing the status changed.

2. **Once flipped, a future task creation will not reverse it.** Adding T116 (Track A1) to E013 doesn't recompute E013 to `(100 + 0) / 2 = 50%` automatically — recompute only fires on task completion, not creation. The `status: review` will linger until an explicit recompute or until T116 also completes (at which point readiness becomes `(100 + 100) / 2 = 100%` again — still wrong).

3. **`select-task --json` keeps reporting `backlog-empty` even though the epic has implicit work pending.** Because the harness sees no eligible tasks (T115 is done, no other children exist), it concludes the backlog is empty. The operator who reads the epic body knows there are 14 more tasks to spec, but the selector does not.

4. **The epic's `status: review` claim is dangerous if downstream tooling consumes it.** A future "ship a release of all epics in review" workflow would treat E013 as ready for human verification when it's not. A future "find epics that need work" workflow would skip E013 entirely.

## What I did about it (immediately)

When I noticed the bug, I rewrote E013's frontmatter manually:

```yaml
status: active # was: review
current_stage: design # was: null
readiness: 15 # was: 100, deliberately picked to reflect "design done, implementation pending"
artifacts: # added the T115 outputs
  - wiki/domains/architecture/usage-dashboard-research.md
  - wiki/domains/architecture/usage-dashboard-findings.md
```

And added a "Status note (2026-04-14, post-T115)" section to the epic body that explicitly explains why the harness number is wrong and warns future readers.

This is a manual override that the harness will overwrite on the next recompute (when T116 completes, the average will become `(100 + 100) / 2 = 100%` again). The override only buys time until the underlying issue is fixed structurally.

## What needs to happen (structural fixes, in order of cost)

### 1. Cheap fix: harness warning when epic flips to 100% with few children

Add a check in the recompute script: if an epic's readiness flips from <100 to 100 AND its child count is below some threshold (3? 5?), emit a warning to the harness log and DO NOT silently flip the status. Require an explicit operator confirmation or an `--allow-sparse-100` flag.

This catches the symptom without changing the model. ~30 lines of code.

### 2. Medium fix: epic-level done-when items independent of children

Allow the epic file to declare its own Done When items that must be satisfied independently of child task readiness. The harness recompute considers BOTH the child average AND the epic's own Done When verification. An epic only reaches 100 when both are satisfied.

This requires extending the schema (add `done_when` to epic frontmatter or a structured section in the body), extending the verifier to handle epic-level items, and extending the recompute to gate on the verification result. Probably a multi-task effort, but it's the right model.

### 3. Expensive fix: implicit-children awareness

Allow the epic to declare "expected child count" or "expected scope" in some structured form so the harness can detect when current children do not yet cover the declared scope. This is the most flexible fix but also the most invasive — it requires inventing a new schema concept and getting agents to populate it correctly during epic creation.

Probably overkill for the current scale. Mention as a future option but don't pursue today.

## Workaround until the structural fix lands

When creating the first child task for a sparse epic:

1. **Manually set the epic's status field to `active`** before launching the agent. Don't trust the auto-recompute.
2. **Add a "Status note" section to the epic body** explaining the actual scope and warning future readers about the readiness number.
3. **Set `readiness` manually** to a small number (15-25) reflecting "design done, implementation pending" rather than letting the harness average it.
4. **After the agent run**, re-check the epic frontmatter and fix anything the harness wrote automatically.
5. **Document the workaround in the next handoff** so future-Claude knows to do the same thing.

These steps are exactly what I did for E013 on 2026-04-14. They are temporary — the structural fix above is the real solution.

## Secondary symptom (T116, 2026-04-14 evening)

The lesson workaround section explicitly predicted: "manual override is temporary, the harness will overwrite it on next recompute." T116 confirmed that prediction within hours, AND surfaced a second methodology bug I didn't anticipate.

After T116 completed (5-stage feature-development task, all stages green, harness committed everything cleanly), E013's frontmatter was overwritten to:

```yaml
status: in-progress
current_stage: test
readiness: 100
stages_completed: [document]
```

Two things are wrong here, not one:

1. **`readiness: 100` returned** — the manual override from earlier today (`readiness: 15`) was overwritten exactly as predicted. This is the primary bug from this lesson, no surprise.

2. **`current_stage: test` and `stages_completed: [document]` disagree with each other** — and both disagree with reality. T116 went through all 5 stages (`document → design → scaffold → implement → test`) and ended in `test`. T115 went through 2 stages (`document → design`) and ended in `design`. Neither child has `stages_completed: [document]` in isolation. The epic-level `stages_completed: [document]` is some intersection / first-stage / arbitrary projection that doesn't correspond to either child or to the epic itself.

Worse: epics don't HAVE stages in the methodology model. Stages are a per-task concept. An epic is a container. The fact that the harness writes `current_stage: test` and `stages_completed: [...]` to an EPIC's frontmatter is a category error — those fields shouldn't exist at the epic level at all, or if they do they should mean something specific (e.g. "the latest stage any child reached" or "the stage all children have reached").

### What this tells us about the underlying bug

The harness's epic recompute logic is doing **two distinct broken things**:

- **Bug A** (the original): `epic.readiness = average(child.readiness)` produces wrong results when child set is sparse.
- **Bug B** (newly observed): epic-level stage fields are populated with last-child or first-child or some-projection-of-child stage data, even though epics don't have stages. The exact derivation is unclear without reading the recompute code, but the symptom is that `current_stage` and `stages_completed` on the epic file are nonsensical.

Both bugs share the same root cause: **the recompute logic treats epic frontmatter as a place to write aggregated child data without thinking about what those fields MEAN at the epic level.** Readiness as average might be defensible at the epic level (with caveats about sparse children); stage-name fields are not — they're a category error.

### Updated structural fix priorities

The original lesson proposed three structural fixes:

1. Cheap: warning when readiness flips to 100 with few children
2. Medium: epic-level done-when items independent of children
3. Expensive: implicit-children awareness

Add a fourth:

4. **Stop writing stage-name fields to epic frontmatter entirely.** `current_stage` and `stages_completed` are per-task concepts. Epics should have NEITHER field, OR they should have explicitly-named aggregate fields like `latest_child_stage` and `all_children_completed_stages` that make their meaning clear. Whichever code path in the harness writes these fields to epic files should be deleted or rewritten with explicit aggregation semantics.

This fourth fix is **independent of the readiness-math bug** and may be cheaper to ship. The recompute should leave epic stage fields alone unless the operator explicitly opts in.

### Updated workaround for sparse-epic scenarios

In addition to the original 5-step workaround, add:

6. **Do NOT manually correct stage-name fields on epic files** — they will be overwritten on the next recompute, AND the manual values will be wrong because epics don't have stages. Better to leave them in their wrong state and address via the structural fix in #4.

7. **The "real" epic state lives in the body markdown, not the frontmatter.** Treat epic frontmatter as untrustworthy after any child task completes. Use the body's "Status note" section as the authoritative source until the methodology is fixed.

### When the methodology will lie to you

After T116, here is what an automated tool reading E013's frontmatter would conclude:

- "Epic E013 is in-progress" ✓ (correct)
- "Epic E013 is at 100% readiness" ✗ (wrong, ~15% in reality)
- "Epic E013 is currently in the test stage" ✗ (epics don't have stages)
- "Epic E013 has completed the document stage" ✗ (meaningless at epic level)

**Three out of four fields are wrong.** That's a 75% lie rate on E013's frontmatter as of 2026-04-14 evening. Any future tooling that reads epic frontmatter must be aware of this until the structural fix lands. Alternatively: the methodology shouldn't WRITE these fields in the first place.

## Third occurrence — T117 (2026-04-14 evening)

T117 completed cleanly as the third consecutive real run on E013. The bug fired again with the same symptom pattern as after T116, PLUS a new symptom I hadn't noticed before:

**Post-T117 E013 frontmatter:**

```yaml
status: review
current_stage: test
readiness: 100
stages_completed: [document]
artifacts:
  - wiki/domains/architecture/usage-dashboard-research.md
  - wiki/domains/architecture/usage-dashboard-findings.md
```

Bugs active:

1. **`readiness: 100`** — same as after T115 and T116. **Three confirmations** that the readiness math overrides any manual correction and always computes average-across-completed-children. When all three children (T115, T116, T117) are `done` at 100%, the average is 100. The epic's implicit scope (14 more tasks across A3-A8 and B1-B6) is invisible to the formula.

2. **`current_stage: test` and `stages_completed: [document]`** — same category error as after T116. Third confirmation.

3. **NEW: `artifacts` field is stuck on T115's output only.** Look at the field. It lists the T115 research + findings docs. It does NOT list T116's 8 design wiki files (`cost-accumulator-window-extension-*.md`), T116's 4 src modifications, T117's 2 new src files, or T117's completion log. **The harness recompute does not aggregate artifacts from child tasks into the epic's artifacts field.** It's stuck on whatever was there first.

This is a FOURTH methodology bug — distinct from the readiness math bug and the stage-name pollution bug — and it means the epic-level `artifacts` list is essentially decorative after the first child completes. Anyone relying on it to find "all deliverables under this epic" will miss everything after the first task.

### Fifth structural fix proposal

Adding to the original 3 + the post-T116 "stop writing stage-name fields" fix:

5. **Aggregate artifacts across ALL completed children.** When the recompute runs, collect `artifacts: [...]` from every child task that is `status: done` and produce a union at the epic level. Preferably deduplicate. Ideally, produce a structured list grouped by child task ID so the provenance is clear (e.g. `artifacts: { T115: [...], T116: [...], T117: [...] }` or a flat list with comments).

Alternatively: **stop writing the `artifacts` field at the epic level entirely.** The canonical source for "all artifacts under an epic" is the union of the child tasks' artifacts — which can be computed on-demand by walking the children. Writing it to the epic frontmatter creates a stale cache that drifts from reality.

### Three-confirmation pattern

As of 2026-04-14 evening, this lesson has evidence from three consecutive real runs (T115, T116, T117) — all on the same epic, all producing the same symptom cluster. The bug is NOT a one-off or an edge case. It fires **every single time a child task completes on a sparse epic**. The structural fix is overdue.

### Updated lie rate

After T117, the lie rate on E013's frontmatter is now:

- `status: review` ✗ (wrong — epic is active with ~14 more tasks pending)
- `current_stage: test` ✗ (category error)
- `readiness: 100` ✗ (wrong — ~25% in reality after 3 of ~17 tasks complete)
- `stages_completed: [document]` ✗ (meaningless at epic level)
- `artifacts: [T115's 2 files]` ✗ (stale — missing T116's 12 + T117's 2 artifacts)

**Five out of five frontmatter fields below the title are now wrong.** 100% lie rate. The epic frontmatter is a pure fiction at this point.

## Fourth occurrence — multi-task run 2026-04-14 evening (NUANCE: bug fires WHEN children are sparse, not always)

The 2026-04-14 multi-task run completed T118 → T119 → T120 in a single autonomous loop on E013. After the run, I expected the readiness bug to fire AGAIN at 100%. **Instead, the harness recomputed E013 to 83% and committed it correctly:**

```
70bdfc6a chore: recalculate E013 readiness → 83%
```

83% is the correct math: at recompute time, 5 of 6 child tasks were at 100% and 1 was in flight (the average works out to ~83% under that distribution).

**This contradicts the original lesson statement that the bug fires "every time a child task completes."** A more accurate statement: **the bug only fires when ALL children (in the current child set) are simultaneously at 100%.** When the child set is sparse and small (1-3 children) AND all are done, average=100. When the child set has at least one in-flight task, the average is meaningfully <100 and approximates real progress.

### Refined symptom diagnosis

The bug surfaces under these conditions, in order of severity:

| Condition                                | Bug fires?            | Why                                                                     |
| ---------------------------------------- | --------------------- | ----------------------------------------------------------------------- |
| 1 child, status `done`                   | ✅ YES                | average = 100/1 = 100%                                                  |
| 2-4 children, all `done`                 | ✅ YES                | average = 100/N = 100%                                                  |
| 5+ children, all `done`                  | ✅ YES (less harmful) | average = 100/N = 100%, but the operator already trusts the number more |
| 2-4 children, some `done` some `active`  | ❌ NO                 | average = (100 × done) / total < 100% — correct                         |
| 5+ children, mixed states                | ❌ NO                 | average matches reality                                                 |
| Epic with implicit goals beyond children | ✅ ALWAYS             | the average can never see implicit work                                 |

The "epic has implicit goals beyond children" condition is the deepest version of the bug — the only fix is structural (epic-level done-when items independent of children, fix #2 from the original lesson).

The "all current children at 100%" condition is the easier version — fix #1 (warning when readiness flips to 100 with few children) catches it.

### Why T118/T119/T120 didn't trigger the worst case

Between T118 and T119 completing, T119 and T120 were still in the "active" or "in flight" buckets. The sparse-children check only looked at `done` children divided by `total children`, and the `total` included T119 and T120. So the average was always <100% during the run. **The bug is masked when there are tasks in flight that aren't yet done.**

The race-condition window is: **the moment between (a) the LAST in-flight child completing and (b) a NEW child task being created on the epic.** In that window, the average is exactly 100% and any tooling reading the epic frontmatter sees `readiness: 100 / status: review`. After a new task is added, the average drops back below 100% and reality is restored — but tooling that consumed the wrong number during the window has already taken action on stale data.

### Updated structural fix priorities (after multi-task observation)

The original 4 fixes plus the post-T117 5th (artifacts aggregation) were:

1. Cheap: warning when readiness flips to 100 with few children
2. Medium: epic-level done-when items independent of children
3. Expensive: implicit-children awareness
4. Independent: stop writing stage-name fields to epic frontmatter
5. Independent: aggregate artifacts across all completed children

Fix #1 (warning) is now even more clearly the right cheap fix because the multi-task run showed the bug is BENIGN when there are in-flight children. The warning would only need to fire in the narrow race-condition window, which is rare in practice. Worth shipping before the more expensive fixes.

### Distilled rule (revised)

**Trust epic readiness numbers when**:

- The epic has 5+ children, AND
- At least one child is in-flight or planned (not all `done`)

**Do NOT trust epic readiness numbers when**:

- The epic has 1-4 children, OR
- All current children are at 100% AND the epic body indicates more work is pending

Use the epic body's "Status note" section (when present) as the authoritative source instead of the frontmatter when the conditions on the right side apply.

## Connection to other lessons

- **`lesson-specific-done-when.md`** — same root failure mode (the methodology only knows what is structurally encoded), one level lower (task done-when instead of epic readiness)
- **`lesson-methodology-battle-tested.md`** — adds another data point: the methodology is mostly working as designed, but the readiness math has a known limitation that surfaces with sparse epics
- **`lesson-investigate-before-designing.md`** — this lesson was discovered by READING the harness output and noticing the number didn't match reality; the natural impulse "just trust the system" would have left the bug undetected for who knows how long

## When this matters most

This bug is **most dangerous early in an epic's lifecycle**, when the child set is small. As an epic accumulates more tasks, the average becomes more representative and the failure mode disappears. So the rule of thumb is:

- **Epic with 1 child**: do not trust readiness, set it manually
- **Epic with 2-4 children**: be skeptical of readiness, especially after the first completion
- **Epic with 5+ children**: readiness is approximately correct, trust with light review
- **Epic with 10+ children**: readiness is reliable

The threshold is intentional — most of OpenArms's current epics have 5+ children precisely because they were created with full task breakdowns. E013 was the exception because it sat in `draft` with zero children for 4 days before T115. The bug surfaces specifically when an epic transitions from "no children" to "one or two children" and the first one completes.

## Relationships

- PRODUCED_BY: 2026-04-14 T115 run — first observed instance
- EVIDENCE: `wiki/backlog/epics/E013-usage-dashboard-statusline.md` (the epic that auto-flipped) + the `674fb04f` commit that manually corrected it
- INFORMS: any future task that creates the first child of a draft epic
- INFORMS: future structural fix to `recalculate-epic.cjs` (or wherever the recompute lives)
- RELATES_TO: `wiki/domains/learnings/lesson-specific-done-when.md` (same failure class at task level)
- RELATES_TO: `wiki/domains/learnings/lesson-methodology-battle-tested.md` (additional data point on methodology limitations)
- RELATES_TO: `wiki/domains/learnings/lesson-investigate-before-designing.md` (the impulse to trust the system would have hidden this)
