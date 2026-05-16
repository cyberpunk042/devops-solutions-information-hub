Deep comprehensive session-state load for the research wiki / second brain.

> Slash-invoked. Operator types `/load-context-deep` literally. Heavy sibling
> of `/load-context` (which does the light ~10-op walk). Use this for:
> - Multi-day break — full arc reconstruction
> - Post-compaction recovery with heavy session loss
> - Onboarding to an in-progress mission with operator-named complexity
> - Pre-handoff audit (verify the agent has the FULL recent picture before
>   handing off to operator)

## Why this command exists

`/load-context` (light, ~10 ops) is enough for routine session-start.
But sometimes the agent needs to reconstruct a multi-day arc:
- 7-10 operator directives (not just 3) — the full corrective trajectory
- 5-7 session logs (not just 2) — the recent arc shape
- Full backlog state — active epics + modules + impediments
- Pending ingestions audit — raws without synthesis pages
- Maturity flow signals — drafts vs synthesized vs validated counts
- Sister-project pulse — cross-project state
- Recent draft additions — what's been authored but not promoted

`/load-context-deep` delivers that — ~30 ops, 2-5 minutes.

Pair pattern with the other 3 commands:
- `/load-brain` (heavy, ~76) — timeless intelligence, full
- `/load-brain-light` (~11) — timeless intelligence, essentials
- `/load-context` (light, ~10) — session state, quick
- `/load-context-deep` (this, ~30) — session state, comprehensive

Cold-start recovery combo for a multi-day return:
- `/load-brain-light` (re-warm brain essentials)
- `/load-context-deep` (reconstruct full session arc)

## Argument modes

| Invocation | Behavior |
|---|---|
| `/load-context-deep` (no args) | Full deep walk (~30 reads) |
| `/load-context-deep <surface>` | Deep dive on one surface only |
| `/load-context-deep <s1> <s2> ...` | Union of deep surfaces |

### Surface vocabulary (deep depth)

Same names as `/load-context`, but deeper depth per surface:

| Surface | Light depth (load-context) | Deep depth (here) |
|---|---|---|
| `handoff` | most recent 1 | all handoffs in last 30 days |
| `notes` | last 3 | last 10 |
| `log` | last 2 | last 7 |
| `queue` | the file | the file + all Q-items + Q-history |
| `pipeline` | `status` output | `status` + `gateway health` + `gateway compliance` |
| `git` | `log -5` + `status` | `log -15` + `status` + `diff --stat HEAD~10` |
| `backlog` | _index + recent | _index + all active epics + modules + impediments |
| `ingestion` | recent raws list | full raws-vs-sources audit |
| `sister` | `sister-projects.yaml` | + cross-project recent activity scan |
| `mode` | active-mode file | + mode history |
| `maturity` | (new — deep only) | tier counts: lessons/patterns/principles drafts→validated→canonical |
| `drafts` | (new — deep only) | last 5 entries in `wiki/lessons/01_drafts/` + `wiki/patterns/01_drafts/` |
| `sources` | (new — deep only) | last 5 source-synthesis pages in `wiki/sources/` |

## Discipline

- Read each file in full. Read command output in full. Pre-bash hook blocks
  reflexive truncation pipes — respect it.
- raw/notes/ are SACROSANCT verbatim. Never paraphrase.
- The output is a DEEP SESSION STATE report (format below), not a wiki page.
  Don't ingest.
- Heavy walk — expect 2-5 minutes total runtime. Operator authorized this depth
  by invoking this command.

## The Deep Default Walk — ~30 ops

### 1. Recent operator directives (last 10 from raw/notes/)

```bash
ls -t raw/notes/2026-*.md
```

Then `Read` the 10 most recent. Surface each with verbatim headline.

### 2. Recent session work (last 7 from wiki/log/)

```bash
ls -t wiki/log/2026-*.md
```

Then `Read` the 7 most recent. Surface: what landed, themes, open threads.

### 3. Operator decision queue (full)

```
Read wiki/backlog/operator-decision-queue.md
```

Surface ALL Q-items (pending + recent resolutions) for arc context.

### 4. Pipeline + health + compliance

```bash
.venv/bin/python -m tools.pipeline status
.venv/bin/python -m tools.gateway health
.venv/bin/python -m tools.gateway compliance
```

Read full output of each.

### 5. Git state (extended)

```bash
git log --oneline -15
git status --short
git diff --stat HEAD~10..HEAD 2>/dev/null || git diff --stat
```

Surface: recent arc of commits, uncommitted state, file change distribution.

### 6. Backlog active state

```bash
ls wiki/backlog/epics/pre-milestone/ 2>/dev/null
ls wiki/backlog/modules/ 2>/dev/null | head -20
```

Then `Read wiki/backlog/_index.md` + the 3 most recently modified epics
+ any module flagged with impediment.

### 7. Sister-project pulse

```bash
.venv/bin/python -c "import yaml; d=yaml.safe_load(open('wiki/config/sister-projects.yaml')); print(yaml.dump(d, default_flow_style=False))" 2>/dev/null || Read wiki/config/sister-projects.yaml
```

Surface: registered sister projects + last-touched/status.

### 8. Maturity-tier flow signals

```bash
ls wiki/lessons/01_drafts/ | wc -l
ls wiki/lessons/02_synthesized/ | wc -l
find wiki/lessons/03_validated/ -name "*.md" -type f | wc -l
ls wiki/lessons/04_principles/hypothesis/ | wc -l
ls wiki/patterns/01_drafts/ | wc -l
ls wiki/patterns/02_synthesized/ | wc -l
find wiki/patterns/03_validated/ -name "*.md" -type f | wc -l
```

Flag tiers growing without downstream flow (many drafts, few promoted).

### 9. Pending ingestions check

```bash
ls -t raw/articles/ 2>/dev/null
ls -t raw/transcripts/ 2>/dev/null
ls -t raw/papers/ 2>/dev/null
```

Compare against `wiki/sources/` to identify raws without synthesis pages.
Surface count + recent examples.

### 10. Recent draft activity (3-5 most recent in 01_drafts)

```bash
ls -t wiki/lessons/01_drafts/*.md
ls -t wiki/patterns/01_drafts/*.md
```

Then `Read` the 3-5 most recent across both. Surface: what's being authored
but not promoted, evolution trajectory.

### 11. Recent source syntheses

```bash
ls -t wiki/sources/**/*.md
```

(use find if shell glob fails)

Read the 3-5 most recent source-synthesis pages. Surface: recent ingestion
themes, source diversity.

### 12. Active mode (forward-compat)

```bash
cat .claude/active-mode 2>/dev/null || echo "(no mode active)"
```

## Then: apply surface args (if any)

If the operator passed surface arguments, FOCUS on those (skip the rest of
the default walk). Apply the deep depth per the table above. Examples:

- `/load-context-deep handoff` → all handoffs in last 30 days
- `/load-context-deep notes log` → 10 raw/notes/ + 7 wiki/log/
- `/load-context-deep backlog ingestion` → full backlog state + full raws-vs-sources audit
- `/load-context-deep maturity drafts` → tier counts + recent draft additions

### Resolution rules

- Surface names are case-insensitive
- `and` between surfaces is a separator
- Unknown surface → ask the operator to clarify, do NOT guess

## DEEP SESSION STATE report (the structured output)

After the walk, emit this report:

```markdown
# DEEP SESSION STATE — <DATE>

## Operator directive arc (last 10 from raw/notes/)
| Date | File | Headline (verbatim quote) |
|---|---|---|
<rows>

## Themes detected in operator arc
<1-3 bullets — what trajectory the operator has been on>

## Recent session work (last 7 from wiki/log/)
| Date | File | What landed |
|---|---|---|
<rows>

## Pending operator decisions (queue full state)
- Pending: <count>
- Recently resolved: <count>
- Top 3 open Q-items: <headlines>

## Pipeline / health / compliance
- Pipeline: <pages>, <raws>, <relationships>, <errors>
- Health composite: <score>
- Compliance tier: <super-model tier> + <gaps>

## Git state (extended)
- Recent commits: <15 oneline>
- Uncommitted: <count + summary>
- File change distribution: <top changed paths>

## Backlog active state
- Active epics: <list>
- Active modules: <list>
- Impediments: <list, or "(none)">

## Sister-project pulse
<list from sister-projects.yaml + last-touched indicators>

## Maturity flow
| Tier | Lessons | Patterns |
|---|---|---|
| 01_drafts | <N> | <N> |
| 02_synthesized | <N> | <N> |
| 03_validated | <N> | <N> |
| 04_principles | <N> | (n/a) |
<flags: tiers stuck or growing-without-downstream-flow>

## Pending ingestions
- Recent raws: <count by type>
- Without synthesis: <count + examples>

## Recent draft activity
<3-5 most recent 01_drafts entries with 1-line summary each>

## Recent source syntheses
<3-5 most recent wiki/sources/ pages with 1-line summary>

## Active mode
<from .claude/active-mode, or "(no mode active)">

## Synthesized active arc
<2-3 sentences describing the trajectory across operator directives,
session work, and recent drafts. This is the value-added synthesis —
not a restatement of the data above but an interpretation of WHAT is
happening RIGHT NOW.>

## Status
Deep session state loaded. Ready for operator direction.
```

## Composition with other commands

Recommended cold-restart combos:

| Scenario | Combo |
|---|---|
| Fresh cold session (you don't know the project yet) | `/load-brain` then `/load-context` |
| Quick re-engagement (post-break < 1 day) | `/load-context` alone |
| Multi-day break, full reconstruction | `/load-brain-light` then `/load-context-deep` |
| Post-compaction recovery | `/load-brain-light` then `/load-context-deep` |
| Focused dive on one model + recent activity around it | `/load-brain-light <model>` then `/load-context queue notes` |

## Mechanism

100% deterministic per operator 2026-04-24 doctrine. The walk IS the program.
Surface arguments are documented extension points.

## Cross-references

- [load-brain.md](load-brain.md) — permanent brain (full)
- [load-brain-light.md](load-brain-light.md) — permanent brain (light)
- [load-context.md](load-context.md) — session state (light)
- AGENTS.md Hard Rule 3 — log operator directives verbatim BEFORE acting
- `/orient` (predecessor) — mixed identity + state; superseded by the
  brain/context split
