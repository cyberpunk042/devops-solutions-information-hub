---
name: view
description: Project command center — Progress, Position, Done, TODO, Questions (answered + unanswered with options & recommendations), Way forward. Each section is augmented with reasoning, tradeoffs, and concrete next steps. Use when the user types /view or asks orientation questions ("where are we?", "what's the status?", "what's left?", "how far have we come?", "what's the way forward?").
---

# /view — augmented project command center

Render seven sections, **each substantially augmented** with reasoning,
options, tradeoffs, and concrete next steps. The render is the deliverable —
the user is using it to decide what to do next. Thin renders fail the job.

```
1. PROGRESS     — trajectory + trend analysis + what the trend predicts
2. POSITION     — current state + what it enables + what to watch
3. DONE         — shipped items, grouped, with significance + what each unlocked
4. TODO         — remaining work with priority + effort + blockers + dependencies
5. QUESTIONS    — ★ ANSWERED (decision + rationale + when) ★
                  ★ UNANSWERED (details + options + tradeoffs + recommendation) ★
6. WAY FORWARD  — threads with concrete first step + effort + tradeoff vs others
7. SIGNPOSTS    — where to find what (always include)
```

The **Unanswered** subsection is the most-augmented part of the entire view.
Treat every unanswered question as a mini-RFC: state the question, explain why
it's open, list options with explicit tradeoffs, name a recommendation with
reasoning, and identify what unblocks the decision. **Never list an unanswered
question with just a one-line gloss.**

## When to invoke

- User typed `/view`.
- Orientation questions: "where are we?", "what's the status?", "what's left?",
  "how far have we come?", "what's the way forward?", "what's pending?",
  "what's done?", "what's next?".
- Cold-start of a session where the user wants the lay of the land.

## Project-shape detection

Run these checks **in parallel** at the start:

1. `ls docs/handoff/*.md 2>/dev/null | sort | tail -3` — recent handoffs
2. `ls docs/review/phase-*/99-findings-ledger.md 2>/dev/null` — audit ledgers
3. `ls docs/sdd/*.md docs/plan/*.md docs/rfc/*.md 2>/dev/null` — design docs
4. `ls ARCHITECTURE.md SECURITY.md README.md ROADMAP.md TODO.md CHANGELOG.md 2>/dev/null`
5. `git log --oneline -25` — recent commit cadence
6. `git branch --show-current && git status --short` — current branch + WIP
7. `rg -i 'TODO|FIXME|XXX' -n -g '!target' -g '!node_modules' | head -50` — in-code TODOs
8. Open GitHub issues if a `cyberpunk042/<repo>` is in MCP scope

Detect one of:

- **Shape A**: audit ledgers + SDDs both present (e.g. selfdef)
- **Shape B**: design docs only (SDDs / RFCs, no audit ledgers)
- **Shape C**: TODO.md / ROADMAP.md driven, no SDDs
- **Shape D**: vanilla git repo
- **Shape E**: not a git repo at all — synthesize from filesystem

The seven sections render for every shape. Only the **sources** vary.

---

## Section-by-section augmentation spec

### 1. PROGRESS

Wide trajectory table or timeline + a **trend annotation paragraph**.

Trend annotation must answer:
- Is the cadence accelerating, decelerating, or steady?
- What's the dominant work-type (features / fixes / audit / refactor)?
- What does the trajectory **predict** — convergence, expansion, plateau?

### 2. POSITION

Concrete facts table + **two augmentations**:

1. **What this state enables** — what becomes possible now that wasn't before?
2. **What to watch** — what's fragile, what's drifting, what could regress?

Always include: branch, status-short, last commit subject/age, open-PR status,
the single most-important fact.

### 3. DONE

Grouped punch list of shipped items. **Each group gets a one-line significance
note**: why did this batch matter; what did it unlock for downstream work.

### 4. TODO

Punch list with **four augmentation columns**:

| Item | Priority | Effort | Blocker | Pointer |

- **Priority**: `★ now` / `near` / `later` / `someday`
- **Effort**: `S` (≤1 PR) / `M` (≤3 PRs) / `L` (own SDD/cycle)
- **Blocker**: who/what gates it; `—` if nothing
- **Pointer**: file:line so the user can navigate

After the table, render a **dependency note** — which items unblock others.

### 5. QUESTIONS — answered + unanswered

#### 5a. ANSWERED — decisions made

Table with **four columns**:

| Question | Decision | Rationale | When/where |

`Rationale` is **mandatory** — never just the decision.

#### 5b. UNANSWERED — decisions pending  ★ HIGH-DEPTH ★

**Every unanswered question is a mini-RFC.** Render each as:

```
### Q-N: <Question stated as a question>

**Status**: <open / deferred / blocked / waiting on user>
**Why it's open**: <2-3 sentences>
**What it gates**: <what's blocked downstream>
**Stakes**: <low / medium / high>

**Options**:

  A) <Option name>
     • Pros / Cons / Effort / Risk

  B) <Option name>
     ...

**Recommendation**: <Option X — why this beats the others>
**What unblocks the decision**: <user input / spike / prerequisite>
```

If options aren't enumerated in source docs, **synthesize them** and say so.

### 6. WAY FORWARD

2-5 candidate threads. **Each thread is augmented** with:

```
N. <Thread name>
   Concrete first step: <one specific command/file/action>
   Effort: <S / M / L>
   Prerequisites: <none / Q-X answered / Y shipped>
   Tradeoff vs other threads: <why pick this over thread N+1>
   My read: <recommended / optional / wait>
```

Pull from the latest handoff's "what to ask first" if present — that's authoritative.

### 7. SIGNPOSTS

Compact reference table. Always include:

```
Handoff (latest)      docs/handoff/<latest>.md
Design docs           docs/sdd/... or wiki/...
Root context          ARCHITECTURE.md · README.md · CONTEXT.md · DESIGN.md
Recent commits        git log --oneline -20
```

---

## Style rules

- **Generous ASCII**: wide tables, strong headings, monospace blocks.
- **File:line pointers** for every fact.
- **Don't invent status.** Empty sections render `_(none — nothing to report)_`.
- **Mark synthesis explicitly** when options/recommendations are *your* synthesis.
- **No clarifying questions before rendering.**
- **Cap at ~2 screens of dense content.**

## Read-only

`/view` never edits files. Pure read + synthesis + render.

## Failure modes to avoid

- Rendering Unanswered as a one-line bullet list. Mini-RFC treatment for each.
- Listing decisions without the **Rationale** column.
- Rendering DONE as just counts; always include significance.
- Rendering TODO without priority / effort / blocker columns.
- Skipping the trend annotation under PROGRESS.
- Audit-programme framing leaking into non-audit projects. Detect first.
