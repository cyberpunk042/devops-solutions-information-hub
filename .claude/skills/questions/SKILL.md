---
name: questions
description: Interactive queue for pending design questions. Surfaces unanswered questions from project docs (SDDs / RFCs / handoffs / wiki), drills into one at a time with options + tradeoffs, records the operator's answer by editing the source doc AND appending a chronological decision log entry. Argument shape — `show` (default) | `<selector>` | `solve <selector>` | `solve-all` | `answer <selector> <option>`. Selector — `Q-N` | `first` | `last` | `all` | `N` | `N,M`. Use when the user types /questions or asks to "resolve / answer / decide on the open questions."
---

# /questions — interactive question-resolution layer

Companion to `/view`. Where `/view` *renders* the unanswered queue,
`/questions` **resolves it** — one question at a time, interactively,
with the operator's decision committed to the source doc and to a
chronological log.

## When to invoke

- User typed `/questions` (any subcommand).
- User said "let's resolve / answer / decide / work through the open questions."
- User said "answer Q-X" or similar.
- Coming out of `/view` and the user wants to act on the Unanswered section.

## Arguments

| Form | Meaning |
|---|---|
| `/questions` | Default: `show` — render the queue |
| `/questions show` | Same as above, explicit |
| `/questions <selector>` | Shortcut for `solve <selector>` |
| `/questions solve <selector>` | Enter solving-mode for the selected question(s) |
| `/questions solve` (no selector) | Render queue + ask which to enter (two-hop) |
| `/questions solve-all` | **Alias for `solve all`** — walk every Q sequentially |
| `/questions answer <selector> <option>` | Fast-path: pick a known option |
| `/questions detail <selector>` | Read-only deep render of one question |

### Selector syntax

| Selector | Means |
|---|---|
| `Q-1` (or `Q1`, `1`) | The first question in the rendered queue |
| `Q-3` | The third question |
| `first` / `last` / `all` | Self-explanatory |
| `N,M` (e.g. `1,3,5`) | Subset by index |

## Project-shape detection

Same as `/view`. Sources for the queue, by precedence:

- **SDD "Open questions" sections** — `- **Q-X — …**` rows not marked
  answered/closed/shipped.
- **SDD impl-status rows** marked `deferred` / `open` / `pending`.
- **Latest handoff doc** — items flagged as needing user input.
- **Wiki backlog / lessons** if the repo uses that pattern.
- **Open GitHub issues** labelled `question` if MCP scope permits.

## Verb: `show`

Render a compact queue table (#, ID, source, one-line gist, stakes).
End with: "Solve any with `/questions <N>` or `/questions solve-all`."

## Verb: `solve <selector>`

### Step 1 — render the mini-RFC

Same shape as `/view`'s UNANSWERED section, for ONE question:

```
### Q-N (id) — <Question as a question>

**Status**: open | deferred | blocked | waiting on user
**Why it's open**: <2-3 sentences>
**What it gates**: <downstream impact>
**Stakes**: <low | medium | high>

**Options**:
  A) <name>
     • Pros / Cons / Effort / Risk
  B) <name>
     ...

**My recommendation**: <Option X — why>
**What unblocks**: <what's needed to land a decision>
**Source**: <doc path>:<line>
```

Synthesize options from surrounding context if the source doesn't enumerate them.
**Always say so** ("options synthesized — correct me if framing's off").

### Step 2 — operator picks

Use the **AskUserQuestion tool** with 2-4 options. Always include the
recommendation as option A. Always allow `Other` for free-text or
"keep deferred + log the rationale."

If the operator picks **Other**, capture the free-text answer verbatim.

### Step 3 — propose the diff

Render the proposed change set:

1. **Source-doc edit**: before (Q-X row as-is) and after (with
   `**answered (D-NNN)** — <decision>` prepended; original preserved
   for history).
2. **docs/decisions.md entry**: new D-NNN to be appended.

Then ask: **"Ship this as a PR, leave it uncommitted, or cancel?"**

### Step 4 — apply (only if confirmed)

- **"Ship as PR"**: branch off `main`, commit, push, draft PR.
- **"Leave uncommitted"**: working-tree edits only.
- **"Cancel"**: revert anything provisional; question stays open.

## Verb: `answer <selector> <option>`

Fast-path. Operator already knows their pick (`A`/`B`/`C`/`D` or "defer"
or "Other: <text>"). Agent still produces the mini-RFC (for rationale
capture) and still shows the diff before applying.

## Verb: `detail <selector>`

Read-only. Like `solve <selector>` Step 1 — no picker, no edits.

---

## File formats

### Source-doc inline edit pattern

For a Q-X row like:

```
- **Q-C** (TracingPolicy signing shape): deferred. Tracked as
  the F-2026-024 follow-up known gap; a future SDD scopes...
```

The agent rewrites it to:

```
- **Q-C** (TracingPolicy signing shape): **answered (D-NNN, 2026-05-15)** —
  <decision>. _Original framing for history_: deferred. Tracked as the
  F-2026-024 follow-up known gap; a future SDD scopes...
```

Original context is **preserved verbatim** — never deleted, only annotated.

### `docs/decisions.md` entry format

Create the file if it doesn't exist with a header explaining the
append-only audit-log discipline. Per-entry shape:

```markdown
## D-NNN — YYYY-MM-DD — <one-line summary>

**Decision**: <operator's choice — verbatim if free-text>
**Question**: <full question, copied from source doc>
**Source**: `docs/<path>.md`:<line> (Q-X row)
**Rationale**: <why this beats alternatives — synthesis + operator commentary>
**Affected items**: <files / future SDDs / impl artifacts>
**Reversibility**: fully-reversible | partial | locked
**Linked**: PR #<n> (if shipped)
```

D-NNN numbering: scan existing entries, take max + 1. Start at D-001 if
the file is fresh. Pad to 3 digits.

### Branch + commit + PR naming

- Branch: `claude/questions-D-NNN-<short-slug>`
- Commit: `docs(questions): D-NNN — <decision summary>`
- PR title: `docs(questions): D-NNN — <decision summary>`

---

## Composition with `/view`

When `/view` renders UNANSWERED, every question shown is solvable via
`/questions <Q-N>` using the same numbering.

- `/view` = orientation layer (read).
- `/questions` = resolution layer (read → decide → write).

## Style rules

- **Render-then-pick**. Always show the mini-RFC before the picker.
- **Always include "Other"** in the picker for free-text or "keep deferred."
- **Show the diff before applying**.
- **Never apply edits without confirmation**.
- **Preserve original Q-X framing** — annotate, don't delete.
- **One question at a time** in interactive solve.
- **No model identifier** in any committed artifact.

## Failure modes to avoid

- Picking for the operator.
- Applying edits before confirmation.
- Dropping original Q-X context.
- Inventing D-NNN numbers that conflict with existing entries.
- Pushing without explicit operator confirmation.
- Treating `defer` as a non-answer. "Keep deferred + log the rationale"
  IS an answer; it produces a D-NNN entry too.
