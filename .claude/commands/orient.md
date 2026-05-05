Run the deterministic intel-gathering chain for the second brain.

> Slash-invoked. Operator types `/orient` literally. Also auto-directed via
> `.claude/hooks/session-orient.sh` (SessionStart) and `.claude/hooks/post-orient.sh`
> (PostCompact). The hook output adds a directive to your context; this file
> defines the chain you execute.

## Why this command exists

Auto-loaded brain text (CLAUDE.md, AGENTS.md) is passive context. A fresh
or post-compaction session entering /opt with text-only access defaults to
generic-greeter behavior — the broken-and-idle failure mode (see
[lesson](../../wiki/lessons/03_validated/context-engineering/broken-and-idle-fresh-sessions-need-active-orientation-not-passive-context-loading.md)).

This command is the deterministic intel-gathering chain that converts a cold
session into project-aware behavior on the first turn. Pair pattern: hook
~85% (directs to invoke this) + command 100% per invocation (does the work)
+ structured ORIENT REPORT (operator-visible status output).

## On `/orient`

Execute the chain in order. Read full output of each step. Synthesize at the
end into the ORIENT REPORT format.

### 1. Verify brain layer health

```bash
ls /opt/devops-solutions-information-hub/CLAUDE.md /opt/devops-solutions-information-hub/AGENTS.md /opt/devops-solutions-information-hub/CONTEXT.md
ls /opt/devops-solutions-information-hub/.claude/rules/
```

Expected: CLAUDE.md, AGENTS.md, CONTEXT.md present; rules/ has 7+ files
(routing.md, methodology.md, self-reference.md, work-mode.md, learnings.md,
ingestion.md, hook-architecture.md). If any missing — flag in report.

### 2. Read CONTEXT.md (active milestones / identity)

```
Read /opt/devops-solutions-information-hub/CONTEXT.md
```

Surface: active milestones, current epics, identity profile (type / domain /
phase / scale / PM level / trust tier).

### 3. Read recent operator directives (raw/notes/)

```bash
ls -t /opt/devops-solutions-information-hub/raw/notes/2026-*.md | head -7
```

Read the 5-7 most recent. These are sacrosanct primary sources. Surface in
report: file name + 1-line summary + verbatim quote of the headline directive
(if any).

### 4. Read recent session work (wiki/log/)

```bash
ls -t /opt/devops-solutions-information-hub/wiki/log/2026-*.md | head -3
```

Read the 3 most recent. Surface: what was being worked on, what landed, any
unresolved threads.

### 5. Methodology engine health

```bash
.venv/bin/python -m tools.gateway health
```

Read full output. Surface: composite score, pass/fail, any flagged areas.

### 6. Pipeline state

```bash
.venv/bin/python -m tools.pipeline status
```

Read full output. Surface: pages count, lessons / patterns / principles
counts, recent changes, outstanding validation issues.

### 7. Adoption tier (compliance)

```bash
.venv/bin/python -m tools.gateway compliance
```

Read full output. Surface: super-model adoption tier + identified gaps.

### 8. Maturity-tier flow signals

```bash
ls /opt/devops-solutions-information-hub/wiki/lessons/01_drafts/ | wc -l
ls /opt/devops-solutions-information-hub/wiki/lessons/02_synthesized/ | wc -l
ls /opt/devops-solutions-information-hub/wiki/lessons/02_synthesized/contributed/ 2>/dev/null | wc -l
find /opt/devops-solutions-information-hub/wiki/lessons/03_validated/ -name "*.md" -type f | wc -l
ls /opt/devops-solutions-information-hub/wiki/lessons/04_principles/hypothesis/ 2>/dev/null | wc -l
ls /opt/devops-solutions-information-hub/wiki/lessons/04_principles/validated/ 2>/dev/null | wc -l
ls /opt/devops-solutions-information-hub/wiki/patterns/01_drafts/ | wc -l
ls /opt/devops-solutions-information-hub/wiki/patterns/02_synthesized/ | wc -l
find /opt/devops-solutions-information-hub/wiki/patterns/03_validated/ -name "*.md" -type f | wc -l
```

Surface counts in report. Flag tiers that are growing without downstream flow
(many drafts, few synthesized = velocity stalled).

### 9. Pending ingestions

```bash
ls /opt/devops-solutions-information-hub/raw/transcripts/ 2>/dev/null | head -10
ls /opt/devops-solutions-information-hub/raw/articles/ 2>/dev/null | head -10
ls /opt/devops-solutions-information-hub/raw/papers/ 2>/dev/null | head -10
```

Compare against synthesis pages (`wiki/sources/`) to identify raws without
synthesis. Surface count of un-synthesized raws.

### 10. Sister-project pulse

```bash
.venv/bin/python -c "import yaml; d = yaml.safe_load(open('/opt/devops-solutions-information-hub/wiki/config/sister-projects.yaml')); print(yaml.dump(d, default_flow_style=False))" 2>/dev/null || ls /opt/devops-solutions-information-hub/wiki/config/sister-projects.yaml
```

Surface: sister projects registered, last-touched / status if available.

### 11. Mode detection (forward-compat for when modes adopted)

```bash
cat /opt/devops-solutions-information-hub/.claude/active-mode 2>/dev/null || echo "(no mode active)"
```

If a mode is active, the report should reflect it. Currently /opt has no
modes — expect "(no mode active)" until adopted.

### 12. Git state

```bash
cd /opt/devops-solutions-information-hub && git log --oneline -5 && echo "---" && git status --short
```

Surface: 5 most recent commits + uncommitted changes.

## ORIENT REPORT (the structured output)

After running the chain above, emit this report. Use the exact section
headings; fill in observed values. If a section is empty, say so explicitly
(don't omit).

```markdown
# ORIENT REPORT — Research Wiki / Second Brain (<DATE>)

## Brain-health
<Status of CLAUDE.md / AGENTS.md / CONTEXT.md / 7 rules — pass or flag>

## Active milestones / epics (from CONTEXT.md)
<bullets>

## Recent operator directives (last 5-7 from raw/notes/)
| Date | File | Headline directive (verbatim) |
|---|---|---|
<rows>

## Recent session work (last 3 from wiki/log/)
<bullets>

## Pipeline / methodology health
- Composite score: <N>
- Pages: <N>
- Validation errors: <N> (status: PASS / FAIL)
- Lint issues: <N>

## Adoption tier
<from gateway compliance>

## Maturity flow
| Tier | Lessons | Patterns |
|---|---|---|
| 01_drafts | <N> | <N> |
| 02_synthesized | <N> | <N> |
| 03_validated | <N> | <N> |
| 04_principles | <N> | (n/a) |

<Flags: any tier stuck or growing-without-downstream-flow>

## Pending ingestions
<count of raws without synthesis pages, with examples>

## Sister-project pulse
<list from sister-projects.yaml>

## Active mode
<from .claude/active-mode>

## Git state
- Recent commits: <5 oneline>
- Uncommitted: <count + summary>

## Next-best-actions (synthesis-driven)
1. <action with reasoning>
2. <action with reasoning>
3. <action with reasoning>

## Status
Brain loaded. Ready for operator direction.
```

## Discipline

- Read every step's full output. NO `| head` / `| tail` truncation without
  REASON env. Pre-bash hook will block reflexive truncation per Hard Rule 1.
- /orient is read-only — does NOT mutate state. No file writes during the chain.
- The report's "Next-best-actions" is recommendation, not commitment. Operator
  decides what to act on.
- Per workblock-priority discipline: if /orient surfaces a systemic-bug-shaped
  finding, that becomes the next workblock; not a side-note.

## Composition with /loop /cycle (forward-compat)

When modes + /cycle are adopted for /opt, `/cycle` will run a similar but
narrower chain per fire (mode-specific). `/orient` remains the canonical
cold-start + post-compact intel load. Different lifecycle events; same
determinism-ladder approach.

## Cross-references

- Pattern: [session-orientation pair](../../wiki/patterns/03_validated/architecture/session-orientation-pair-sessionstart-hook-and-orient-command-with-orient-report.md)
- Lesson: [broken-and-idle](../../wiki/lessons/03_validated/context-engineering/broken-and-idle-fresh-sessions-need-active-orientation-not-passive-context-loading.md)
- Hooks that direct here: `.claude/hooks/session-orient.sh`, `.claude/hooks/post-orient.sh`
- Adoption decision log: `wiki/log/2026-05-05-orient-pair-adoption-decision.md`
