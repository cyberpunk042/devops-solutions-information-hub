# JuliusBrussee/cavekit

Source: https://github.com/JuliusBrussee/cavekit
Ingested: 2026-05-04
Type: documentation

---

# README

<h1 align="center">cavekit</h1>

<p align="center">
  <strong>compressed spec-driven development for claude code</strong><br/>
  <sub>one file · three commands · zero sub-agents</sub>
</p>

---

## what this is

Plan-then-execute forgets. SDD remembers — but most SDD frameworks bury
that value under agent swarms, dashboards, and ceremony that costs more
tokens than it saves.

Cavekit 4 is a rewrite from the ground up. It keeps only what earns its
place:

- **durable spec** — `SPEC.md` at repo root survives context resets.
- **caveman encoding** — ~75% fewer tokens than prose. Symbols, fragments,
  pipe tables for repeating records.
- **backprop reflex** — every test failure becomes a `§B` entry; classes
  of bug become `§V` invariants the spec never forgets.

That's the whole pitch.

## commands

| cmd | job |
|---|---|
| `/ck:spec` | create / amend / backprop `SPEC.md`. Sole mutator. |
| `/ck:build` | native plan → execute against spec. Auto-backprops on failure. |
| `/ck:check` | read-only drift report. Lists §V / §I / §T violations. |

## install

One line, via the `skills` CLI:

```bash
npx skills add JuliusBrussee/cavekit
```

Installs five skills into `~/.claude/skills/`: `spec`, `build`, `check`
(the workflow) plus `caveman` and `backprop` (the utilities). Claude
activates each when its trigger context matches — e.g. "write a spec
for…" invokes `spec`, "build the next task" invokes `build`. Claude Code
picks them up on next launch.

Or via the Claude Code marketplace (also adds `/ck:spec`, `/ck:build`,
`/ck:check` slash commands):

```bash
/plugin marketplace add juliusbrussee/cavekit
/plugin install ck@cavekit
```

Or clone directly:

```bash
git clone https://github.com/juliusbrussee/cavekit.git ~/.claude/plugins/cavekit
```

## format

See [`FORMAT.md`](./FORMAT.md). Fixed sections: §G goal, §C constraints,
§I interfaces, §V invariants, §T tasks (pipe table), §B bugs (pipe table).

## files

```
FORMAT.md             spec schema + caveman encoding rules
commands/             three slash-command entry points (/ck:spec, /ck:build, /ck:check)
skills/spec           spec mutator (mirrors commands/spec.md as a skill)
skills/build          plan-execute skill (mirrors commands/build.md)
skills/check          drift report skill (mirrors commands/check.md)
skills/caveman        encoding utility
skills/backprop       bug → spec protocol (six steps)
```

## non-goals

- no sub-agents. Main Claude does the work.
- no dashboards. `cat SPEC.md` is the dashboard.
- no parallel workers. One thread, one spec, one diff.
- no JSON / YAML spec bodies. Markdown + pipe tables.
- no hooks, no orchestration binaries, no TypeScript helpers.

---

## older cavekit (the Hunt lifecycle, v3.1.0 and earlier)

The previous generation is **not deprecated** — it is frozen at tag
[`v3.1.0`](https://github.com/juliusbrussee/cavekit/tree/v3.1.0) and
remains a fully working plugin.

**What it is**:

> Spec-driven AI development with an autonomous execution loop. Four-command
> Hunt lifecycle (`/ck:sketch` → `/ck:map` → `/ck:make` → `/ck:check`),
> plus `/ck:ship`, `/ck:review`, `/ck:revise`, `/ck:status`, `/ck:design`,
> `/ck:research`, `/ck:init`, `/ck:config`, `/ck:resume`, `/ck:help` — 16
> slash commands total. 12 named sub-agents. Per-task token budgets,
> stop-hook state machine, model-tier routing, auto-backpropagation from
> test failures, tool-result caching, Codex peer review, Karpathy
> behavioral guardrails, caveman token compression, knowledge-graph
> integration, and design-system enforcement. Parallel wave execution and
> team mode.

**Pick v3.1.0** if you want the full autonomous loop, parallel agents,
peer review, or design-system workflow. **Pick v4** if you want the
distilled core — one spec, three commands, no orchestration.

### install the older version

Marketplace:

```bash
/plugin marketplace add juliusbrussee/cavekit@v3.1.0
/plugin install ck@cavekit
```

Git:

```bash
git clone -b v3.1.0 https://github.com/juliusbrussee/cavekit.git
```

Full docs live at the tag — `git checkout v3.1.0` and read the README
there for command reference, skill catalog, and the Hunt lifecycle guide.

### choosing, or moving

See [`UPGRADE.md`](./UPGRADE.md). Honest framing:
- Stay on v3.1.0 if your project has active `context/kits/` investment.
- Move to v4 if you want fewer moving parts and smaller token bills.
- It is a **two-way door** — `SPEC.md` is plain markdown; nothing traps
  you in either direction.

## philosophy

> The spec is the only artifact that earns its tokens. Everything else
> that costs tokens must either save more tokens later, or the user's
> attention, or it gets cut.

See [`CHANGELOG.md`](./CHANGELOG.md) for the full v3 → v4 break.

## license

MIT.



> **Deep fetch: 9 key files fetched beyond README.**



---

# FILE: CHANGELOG.md

# CHANGELOG

## v4.0.0 — the rewrite

Full rewrite. Not backward compatible with v3.x. Different shape, same name.

### philosophy

Kept only what earned its tokens:

- `SPEC.md` — durable, addressable, caveman-encoded
- three commands — `/ck:spec`, `/ck:build`, `/ck:check`
- two skills — `caveman` encoding, `backprop` protocol

### added

- single `SPEC.md` format with six addressable sections (§G §C §I §V §T §B)
- pipe-table encoding for §T (tasks) and §B (bugs)
- caveman symbol set (→ ∴ ∀ ∃ ! ? ⊥ ≠ ∈ ∉ ≤ ≥ & |) as default for spec writes
- bug → §B → §V backprop reflex wired into `/ck:build` failure path
- `/ck:spec from-code` — distill spec from existing codebase
- `/ck:check` — read-only drift report (replaces five v3 review flavors)
- `npx skills add JuliusBrussee/cavekit` one-line install path (commands + skills)

### removed (relative to v3.1.0)

- 13 of 16 commands (sketch/map/make/ship/review/revise/status/init/config/resume/help/design/research/team/make-parallel)
- all 12 named sub-agents
- 19 of 21 skills
- Go binary and source (`cmd/`, `internal/`, `bin/`, `cavekit` executable)
- shell hooks (`hooks/`, `scripts/cavekit-launch-session.sh`, stop-hook state machine)
- TS tooling (`scripts/cavekit-picker.ts`, `scripts/cavekit-router.cjs`)
- Codex peer-review bridge (`.codex-plugin/`)
- `context/kits/`, `context/plans/`, `context/impl/`, `context/refs/` directories
- autonomous loop, per-task budgets, model-tier routing
- design-system `DESIGN.md` workflow
- knowledge-graph `graphify-out/` integration
- parallel wave execution and team mode
- `install.sh` (216 lines → 0)

### changed

- caveman was opt-in for inter-agent chatter in v3; default for spec writes in v4
- version: 3.1.0 → 4.0.0 (major rewrite, semver respected)
- README, plugin metadata, marketplace entry

### migration

See [`UPGRADE.md`](./UPGRADE.md). No automated migrator — the v3 kit
shape does not map cleanly to v4's single file. Recommended path: run
`/ck:spec from-code` on your existing v3 project to distill a v4 spec
from your built code.

### v3 reachability

v3 is frozen at tag `v3.1.0`. Stays installable and documented. Fixes
only for critical bugs; no new features.

---

## v3.1.0 and prior

See git log before the `v4.0.0` commit, or check out `v3.1.0`:

```bash
git checkout v3.1.0
```



---

# FILE: FORMAT.md

# SPEC.md FORMAT

Single file. Project root. Every cavekit command reads it.

## SECTIONS

Fixed order. Fixed headers. Addressable.

```
# SPEC

## §G GOAL
one line. what code must do.

## §C CONSTRAINTS
- bullet. non-negotiable boundary.
- bullet. tech/lang/lib locked in.

## §I INTERFACES
external surface. what world sees.
- cmd: `foo bar` → stdout JSON
- api: POST /x → 200 {id}
- file: `config.yaml` schema …
- env: `FOO_KEY` required

## §V INVARIANTS
numbered. testable. each ! MUST hold.
V1: ∀ req → auth check before handler
V2: token expiry ≤ ⊥ allowed
V3: DB write ! in transaction

## §T TASKS
pipe table. ids monotonic (never reused). status: `x` done / `~` wip / `.` todo.
id|status|task|cites
T1|.|scaffold repo|-
T2|.|impl §I.api POST /x|V2
T3|x|add §V.1 middleware|V1,I.api

## §B BUGS
pipe table. backprop log. each row = bug + invariant that catches recurrence.
id|date|cause|fix
B1|2026-04-20|token `<` not `≤`|V2
B2|2026-04-21|race on write|V3
```

**Table cell rules**: literal `|` → escape as `\|`. Backticks OK. Cells trimmed. Empty = `-`.

## ADDRESSING

`§<S>.<n>` = section.item. `§V.2` = invariants section, item 2.
Commands, commits, PRs all reference by §. Zero ambiguity.

## CAVEMAN ENCODING

Default for every section. Rules:

- Drop articles (a, an, the). Drop filler.
- Drop aux verbs (is, are, was) where fragment works.
- Short synonyms (fix > implement).
- Fragments fine.

**Preserve verbatim**: code, paths, identifiers, URLs, numbers, error strings, SQL, regex.

**Symbols** (save tokens, machine-readable):

```
→   leads to / becomes / triggers
∴   therefore / fix
∀   for all / every
∃   exists / some
!   must
?   may / optional
⊥   never / impossible / forbidden
≠   not equal / differs from
∈   in / member of
∉   not in
≤   at most
≥   at least
&   and
|   or
```

**Bad** (v1 prose):

> The authentication middleware must verify the token expiry on every request before allowing the handler to execute.

**Good** (v2 caveman):

> V1: ∀ req → auth check before handler

**Bad** (prose bug note):

> Fixed a bug where token expiry comparison used strict less-than instead of less-than-or-equal, causing tokens to be rejected exactly at their expiry timestamp.

**Good** (v2 caveman):

> B1: token `<` not `<=` ∴ tokens rejected @ expiry. §V.2 now ! `≤`.

## WHY CAVEMAN FOR SPECS

Spec loaded every invocation. 75% fewer tokens = 75% fewer dollars & faster reads.
Human skims fast too. Symbols unambiguous.

## ONE FILE RULE

Big project → more sections, not more files. grep ceremony kills agent speed.
If SPEC.md > 500 lines, compact §B (old bugs drop oldest) before splitting.

## WRITES

| command | writes | section |
|---|---|---|
| `/spec new` | creates | all |
| `/spec amend` | edits | chosen |
| `/spec bug` | appends | §B + §V |
| `/build` | flips | §T status cell `.` → `~` → `x` |
| `/check` | — | read only |

That is whole format.



---

# FILE: LAUNCH-POST.md

# cavekit v4: I wrote a framework, then I killed most of it

**TL;DR**: spec-driven development is still the right idea. my v3
implementation buried it under ceremony. v4 is the rewrite. three
commands, one file, no sub-agents. v3 stays reachable at tag `v3.1.0`
for anyone it still works for.

---

I built cavekit v3 to prove that spec-driven development could give AI
agents enough context to stop guessing. On that, it delivered. The part
I got wrong is everything else I wrapped around it.

## what was slop

Cavekit v3 had 16 slash commands. Twelve named sub-agents. Twenty-one
skills, several of them 20KB each. A Go binary. Shell hooks. A stop-hook
state machine. An autonomous execution loop. Per-task token budgets.
Model-tier routing. A Codex peer-review bridge. Knowledge-graph
integration. Design-system enforcement. Team mode with path-scoped
claims. Parallel wave execution.

Every feature had a reason when I added it. Stacked up, they became a
framework you had to learn before you could write a spec. Invocations
loaded thousands of tokens of meta-philosophy (karpathy-guardrails,
validation-first, methodology, context-architecture, convergence-monitoring)
that Claude already knows, re-read in prose every single time.

Parallel agents were the worst of it. They look impressive. In practice
they shatter flow, coordinate via tedious ledger files, and need a
separate review agent to merge their disagreements. I'd rather plan
once, execute serially, and ship.

Native Claude Code plan-then-execute is already good. It's the baseline
cavekit v3 was supposed to beat. After enough sessions I realized it
was often *losing* to the baseline — same work, more ceremony, more
tokens.

## what actually earned its keep

One thing. The spec as a durable artifact. That's the only thing SDD
gives you over plan-then-execute — a spec survives context resets,
diffs against code, absorbs bugs back into itself. Everything else in
cavekit existed to serve that, and most of it did more harm than good.

The other thing I actually liked: caveman compression. It worked. It
just wasn't applied where it mattered — I used it for inter-agent
chatter, not the artifacts that get loaded every invocation.

## v4

Rewrote from the ground up. Here's the whole surface:

- `SPEC.md` at repo root. Six sections (§G §C §I §V §T §B), addressable
  by section.id. Caveman-encoded by default — ~75% fewer tokens than
  prose. §T (tasks) and §B (bugs) are pipe tables because that's the
  efficient shape for repeating records.
- Three commands:
  - `/ck:spec` — the sole mutator. Create, amend, or backprop a bug.
  - `/ck:build` — native plan-then-execute against the spec. On test
    failure, calls `/ck:spec bug:` before retrying. Backprop is a
    reflex, not a dashboard.
  - `/ck:check` — read-only drift report.
- Two skills: `caveman` (the encoding), `backprop` (the six-step
  bug→spec protocol).

That's it. No sub-agents. No autonomous loop. No parallel workers. No
hooks, no Go binary, no TypeScript helpers. No `install.sh`.

4,977 lines of commands and agents in v3 → 226 lines of commands in v4.
21 skills → 2. A 5MB binary → none.

## is this just native claude code with extra steps

Basically yes. That's the point. The one thing it adds is the spec
format and the backprop reflex. Those two earn their tokens. Nothing
else gets to.

If you look at v4 and think "this is just a markdown file and a
convention," you're right. That's the shape a working version of this
idea was supposed to have all along. I just had to build the overbuilt
version first to find it out.

## for existing users

v3 is frozen at tag `v3.1.0`. Still installable:

```bash
/plugin marketplace add juliusbrussee/cavekit@v3.1.0
/plugin install ck@cavekit
```

If your project has a live `context/kits/` investment, or you rely on
the autonomous loop, or your team has muscle memory on the Hunt
lifecycle: stay on v3.1.0. It's frozen, not abandoned. It still works.

If you want the distilled version, install the default branch. See
`UPGRADE.md` for the migration (short version: run `/ck:spec from-code`
on your existing project — your built code becomes the source of truth,
your old kits live in git history).

It is a two-way door. `SPEC.md` is plain markdown. Nothing traps you in
either direction.

## install

One line:

```bash
npx skills add JuliusBrussee/cavekit
```

Or via the Claude Code marketplace:

```bash
/plugin marketplace add juliusbrussee/cavekit
/plugin install ck@cavekit
```

## what I'm not doing

- Not claiming v4 is strictly better than v3 for everyone. Different
  shape, different tradeoffs.
- Not promising parallel/autonomous features will come back. If I need
  them again, they belong in a separate tool, not the spec framework.
- Not apologizing for the rewrite. The overbuilt version was how I
  learned which parts were real.

---

GitHub: https://github.com/juliusbrussee/cavekit
Default branch is v4. v3 lives at tag `v3.1.0`.



---

# FILE: SECURITY.md

# Security Policy

## Reporting a Vulnerability

If you discover a security vulnerability in this project, please report it responsibly.

**Do not open a public issue.** Instead, email **security@juliusbr.com** with:

- A description of the vulnerability
- Steps to reproduce
- Any relevant logs or screenshots

You can expect an initial response within 72 hours. We will work with you to understand the issue and coordinate a fix before any public disclosure.

## Supported Versions

| Version | Supported |
| ------- | --------- |
| latest  | Yes       |

## Disclosure Policy

We follow coordinated disclosure. Once a fix is available, we will publish a security advisory and credit the reporter (unless they prefer to remain anonymous).



---

# FILE: UPGRADE.md

# UPGRADE v3.1.0 → v4.0.0

Honest answer: v4 is not a minor version of v3. It is a different shape
with the same name. This doc helps you decide whether to move, and if so,
how.

## SHOULD YOU UPGRADE?

**Stay on v3.1.0 if**:
- Your project has a large `context/kits/` investment you actively iterate on
- You rely on the autonomous loop, parallel wave execution, or peer review
- Your team has shared muscle memory on `/ck:sketch → /ck:map → /ck:make`
- Your hooks / scripts integrate with the v3 state machine

**Move to v4 if**:
- You want fewer moving parts
- You find yourself fighting the framework more than you use it
- Token cost of invoking v3 commands outweighs the value
- You start a fresh project and want the distilled version

Either is a valid answer. v3.1.0 is not abandoned — it is frozen. Frozen
code does not rot as fast as it looks like it does.

## WHAT CHANGED

| v3.1.0 | v4.0.0 |
|---|---|
| 16 slash commands | 3 (`/ck:spec`, `/ck:build`, `/ck:check`) |
| 12 named sub-agents | 0 — main Claude does the work |
| 21 skills | 2 (`caveman`, `backprop`) |
| `context/kits/` directory | single `SPEC.md` at repo root |
| Hunt lifecycle (sketch/map/make/check) | flat spec → build → check |
| Go binary, shell hooks, TS picker | none |
| Autonomous loop with stop-hook | native Claude Code plan-then-execute |
| Design system, knowledge graph, Codex review | cut |
| Parallel wave execution | single-thread |
| Caveman opt-in for internal chatter | caveman default for spec writes |

## MIGRATION PATH

There is no automated migrator. The v3 `kits/` structure does not map
cleanly to `SPEC.md` — the point of v4 is that caveman + pipe tables
replace that tree. A script would produce lossy nonsense.

**Recommended path** for an in-flight v3 project that has working code:

1. Check out a fresh branch off your current v3 branch: `git checkout -b v4-migration`.
2. Install cavekit v4 (the default branch, or plugin `v4.0.0`).
3. Run `/ck:spec from-code`. v4 will walk your built code and produce
   a `SPEC.md`. **The code is the source of truth**, not your old kits.
4. Review the generated spec. Amend with `/ck:spec amend §X`.
5. Your old `context/kits/` stays in git history. If you ever need the
   original reasoning, `git log -- context/kits/`.
6. Delete the old directory on the v4-migration branch once you trust
   the spec. Commit. Merge when ready.

**If you have not built anything yet** (still in sketch phase): you have
the easiest migration. Scrap the kit, start with `/ck:spec <your idea>`.

## WHAT YOU LOSE

- **Autonomous loop**: v4 has no stop-hook state machine. Each
  `/ck:build` invocation is one plan-then-execute. If you liked "leave
  it running for an hour," v4 does not do that. Use a shell loop or stay
  on v3.
- **Parallel execution**: v4 is deliberately single-thread. Big projects
  take linear wall-clock time. This was a considered trade.
- **Peer review via Codex**: cut. If you want a second model on a diff,
  run it manually or install a peer-review skill separately.
- **Design system, knowledge graph, team mode**: cut. Separate tools if
  you need them.
- **Dashboards**: cut. `cat SPEC.md | grep §T` replaces them.

## WHAT YOU GAIN

- Drastically smaller context footprint on every invocation
- A spec you can read in 30 seconds
- No more "which agent should I invoke?"
- No more orphaned state files
- Backprop as a reflex in every build, not an opt-in

## v3 REACHABILITY

v3.1.0 is frozen at its tag. Always installable:

```bash
/plugin marketplace add juliusbrussee/cavekit@v3.1.0
/plugin install ck@cavekit
```

or:

```bash
git clone -b v3.1.0 https://github.com/juliusbrussee/cavekit.git
```

No v3 code is destroyed — `git log v3.1.0` shows every commit. v3
documentation stays at that tag.

## ONE-WAY DOOR?

No. You can switch back. `SPEC.md` is plain markdown — nothing stops you
from re-exporting it into `context/kits/*.md` if you decide v3 was right
for your project. The work is not trapped.

## QUESTIONS

Open an issue on GitHub. Label `v3` for v3 bugs (fixes only for critical
issues), `v4` for v4 questions.



---

# FILE: skills/backprop/SKILL.md

---
name: backprop
description: |
  Bug → spec protocol. When a bug is found or a test fails, trace the cause,
  decide whether a new §V invariant would catch recurrence, append to §B.
  This is the one non-obvious thing SDD does that plan-then-execute doesn't.
  Triggers on test failure, bug report, post-mortem, or explicit user ask.
---

# backprop — bug → spec

Plan-then-execute fixes the code & forgets.
SDD fixes the code AND edits spec so recurrence is impossible.
That edit is backprop.

## WHEN TO BACKPROP

- Test failed at `/build` verification.
- User reports bug.
- Post-mortem after production incident.
- `/check` flags VIOLATE with root cause found.

## SIX STEPS

### 1. TRACE
Read failure output / bug report.
Find exact file:line of wrong behavior.
Name root cause in one caveman sentence.

### 2. ANALYZE
Ask three questions:
- Would a new §V invariant catch this class of bug? (most common: yes)
- Is §I wrong — did spec claim shape the code cannot deliver? (sometimes)
- Is §T wrong — did we build the wrong thing? (rare but real)

### 3. PROPOSE
Draft the spec change. Never skip §B; §V/§I/§T are case-by-case.

Template:
```
§B row: B<next>|<date>|<root cause>|V<N>
§V line: V<next>: <testable rule that would have caught it>
```

Example:
```
§B row: B3|2026-04-20|refund job ran twice on retry|V7
§V line: V7: ∀ refund → idempotency key check before charge reversal
```

### 4. GENERATE TEST
New invariant without test = lie. Add failing test first.
Name test so it cites the invariant: `TestV7_RefundIdempotent`.

### 5. VERIFY
Fix code. Run test. Must pass. Run full suite. Must not regress.

### 6. LOG
Commit spec edit + test + code fix together.
Commit msg: `backprop §B.<n> + §V.<N>: <one-line cause>`.

## WHAT MAKES A GOOD INVARIANT

- Testable in code (grep-able or assert-able).
- Scoped to a behavior, not a file.
- Stated positively when possible (`! hold` over `⊥ forbid`).
- References §I surface where it applies.

**Bad**: V8: code should be correct.
**Good**: V8: ∀ pg_query ! params interpolated via driver, ⊥ string concat.

## WHEN NOT TO ADD §V

- Bug was purely mechanical typo with no class (`i++` vs `i--` in throwaway).
- Fix is a one-time migration.
- Root cause is external dep (upgrade deps instead, note in §C).

Still append §B entry — record that this failure mode was considered. Future bug with same smell → §B search shows precedent.

## OUTPUT SHAPE

Every backprop run produces:
1. §B entry (always).
2. §V entry (usually).
3. Test file (when §V added).
4. Code fix.
5. One commit.

No dashboards. No log files. SPEC.md + git is the full history.



---

# FILE: skills/caveman/SKILL.md

---
name: caveman
description: |
  Caveman encoding for SPEC.md and spec-adjacent writes. Loaded by /spec, /build,
  /check. Cuts tokens ~75% vs prose while staying precise. Triggers on any write
  to SPEC.md or when user says "caveman", "compress this", "be brief".
---

# caveman — spec encoding

Applies to SPEC.md writes, spec-referencing prose, backprop entries.
Does NOT apply to code, error strings, commit messages, PR descriptions.

## GRAMMAR

- Drop articles (a, an, the).
- Drop filler (just, really, basically, simply, actually).
- Drop aux verbs where fragment works (is, are, was, were, being).
- Drop pleasantries.
- No hedging (skip "might", "perhaps", "could be worth").
- Fragments fine.
- Short synonyms: fix > implement, big > extensive, run > execute.

## SYMBOLS

Prefer over words:

```
→   leads to / becomes / on <x>
∴   therefore / fix
∀   for all / every
∃   exists / some
!   must / required
?   may / optional / unknown
⊥   never / forbidden / nil
≠   not equal
∈   in
∉   not in
≤   at most
≥   at least
&   and
|   or
§   section reference
```

## PRESERVE VERBATIM

Never compress:

- Code blocks, snippets, one-liners with backticks.
- Paths: `src/auth/mw.go`.
- URLs.
- Identifiers: function names, variable names, env vars.
- Numbers and versions.
- Error message strings.
- SQL, regex, JSON, YAML.
- Quoted strings.

## SHAPES

**Invariant**:
```
V<n>: <subject> <relation> <condition>
V1: ∀ req → auth check before handler
V2: token expiry ≤ current_time → reject
```

**Bug row** (pipe table under §B):
```
id|date|cause|fix
B1|2026-04-20|token `<` not `≤`|V2
```

**Task row** (pipe table under §T):
```
id|status|task|cites
T3|x|add auth mw|V1,I.api
```
Status: `x` done, `~` wip, `.` todo. Escape literal `|` as `\|`.

**Interface**:
```
<kind>: <name> → <shape>
api: POST /x → 200 {id:string}
cmd: `foo bar <arg>` → stdout JSON
env: FOO_KEY ! set
```

## EXAMPLES

**Bad**:
> The system should ensure that every incoming request is properly authenticated before being forwarded to its corresponding handler function.

**Good**:
> V1: ∀ req → auth check before handler

**Bad**:
> We discovered that the token expiration check in the middleware was using a strict less-than comparison operator, which meant tokens were being rejected at the exact moment of their expiry.

**Good**:
> B1: token `<` not `≤` → reject @ expiry boundary.

**Bad**:
> The POST endpoint at /x accepts a JSON body and returns a 200 response with an object containing the created id.

**Good**:
> api: POST /x → 200 {id}

## BOUNDARIES

- User asks for prose explanation → switch to normal English.
- Spec documents for external review (RFC, pitch) → normal English.
- Commit message → normal English (git readers expect it).
- Diff comment in code → normal English.

## WHEN UNSURE

If cutting a word loses a fact, keep it. Caveman is compression, not amputation.



---

# FILE: skills/check/SKILL.md

---
name: check
description: |
  Read-only drift detector. Diffs SPEC.md against current code and reports
  violations grouped by severity. Writes nothing — suggests remedies via
  the spec or build skills but never invokes them. Triggers when the user
  asks to check drift, audit the spec, verify invariants, or ask whether
  code still matches the spec. Phrasings: "check drift", "audit the spec",
  "does the code still match §V", "check invariants", "spec vs code".
---

# check — drift report

Pure diagnostic. Reports violations. Writes nothing. User decides remedy.

## LOAD

1. Read `SPEC.md`. If missing → "no spec, nothing to check." Stop.
2. Parse invocation args:
   - `§V` → check invariants only (default)
   - `§I` → check interfaces
   - `§T` → audit task status vs code
   - `--all` → all three

## CHECK §V — invariants

For each V<n>:

1. Translate invariant into verifiable claim about code.
2. Grep / read relevant files.
3. Classify: **HOLD** / **VIOLATE** / **UNVERIFIABLE**.
4. Record address + file:line evidence.

## CHECK §I — interfaces

For each I item:

1. Locate implementation.
2. Classify:
   - **MATCH** — shape in code = shape in spec.
   - **DRIFT** — impl exists, shape differs.
   - **MISSING** — impl absent.
   - **EXTRA** — code exposes surface not in §I.

## CHECK §T — tasks

For each T<n>:

1. If `x`: verify claimed work present.
2. If `~`: note as in-progress.
3. If `.`: note as pending.
4. Flag `x` rows with no evidence as **STALE**.

## REPORT

Caveman. Grouped by severity.

```
## §V drift
V2 VIOLATE: auth/mw.go:47 uses `<` not `≤`. see §B.1.
V5 UNVERIFIABLE: no test covers ∀ req path.

## §I drift
I.api DRIFT: POST /x returns `{result}` not `{id}`. route.go:112.
I.cmd MISSING: `foo bar` absent from cli/*.go.

## §T drift
T3 STALE: status `x`, no middleware file exists.

## summary
2 violate. 1 missing. 1 stale. 1 unverifiable.
next: spec skill with `bug:` or fix code at cited lines.
```

## REMEDY HINTS (not actions)

End report with one-line hint per class:
- VIOLATE / DRIFT → invoke spec skill `bug: <V.n>` or fix code.
- MISSING → invoke build skill on `§T.n` if task exists; else spec skill `amend §T`.
- STALE → spec skill `amend §T` to uncheck.
- EXTRA → spec skill `amend §I` to document, or delete code.

Never invoke fixes. Report only.

## NON-GOALS

- Zero writes. No SPEC.md edits. No code edits.
- No sub-agents. Main thread reads.
- No scores, no grades. Binary per item: holds or drifts.



---

# FILE: skills/spec/SKILL.md

---
name: spec
description: |
  Create, amend, or backprop bugs into SPEC.md at repo root. Sole mutator
  of the project spec. Triggers when the user asks to write a spec, start
  a new spec, distill a spec from existing code, add invariants, amend
  sections (§G, §C, §I, §V, §T, §B), or record a bug via backprop.
  Common phrasings: "write the spec for...", "new spec", "bug: ...",
  "amend §V.3", "distill spec from code", "spec this idea". Reads and
  follows FORMAT.md for the caveman encoding rules and pipe-table shape
  of §T and §B.
---

# spec — spec mutator

Read `FORMAT.md` at repo root if not already loaded. Caveman skill applies to all writes here.

## DISPATCH

Inspect user request and project state:

1. No `SPEC.md` at repo root AND args describe idea → **NEW**
2. No `SPEC.md` AND `from-code` in args → **DISTILL**
3. `SPEC.md` exists AND args start `bug:` → **BACKPROP**
4. `SPEC.md` exists AND args start `amend` → **AMEND**
5. `SPEC.md` exists, no args → ask user which mode

## NEW — idea → spec

Input: user idea.

Steps:
1. Extract goal (1 line, caveman). → §G.
2. List constraints user stated or implied. → §C.
3. List external surfaces user named. → §I.
4. Propose initial invariants. → §V (numbered V1…).
5. Break goal into ordered tasks. → §T pipe table, all status `.`, ids T1…
6. §B section with header row only (`id|date|cause|fix`).

Write to `SPEC.md`. Show user full file. Ask: "spec OK? suggest edits or invoke build."

## DISTILL — code → spec

Walk repo. Produce §G (infer from README/package.json/main entry), §C (infer from stack), §I (enumerate public APIs/CLIs/configs), §V (derive from tests and assertions), §T (one task per known TODO or missing test), §B (empty).

Caveman everywhere. Flag uncertain items with `?` in text so user can confirm.

## BACKPROP — bug → §B + §V

Input: `bug: <description>`.

Steps:
1. Parse bug description.
2. Find root cause (read relevant code).
3. Decide: would a new invariant catch recurrence? If yes → draft `V<next>`.
4. Append §B row: `B<next>|<date>|<cause>|V<N>`.
5. Append new invariant to §V.
6. If fix also changes behavior → add/update §T rows.
7. Show diff. Apply only on user OK.

Rule: every bug gets a §B entry. Invariant optional but preferred.

## AMEND — targeted edit

Input: `amend §V.3` or `amend §T` etc.

Read that section. Show current. Ask user what changes. Write. Show diff.

Never silently rewrite sections user did not name.

## OUTPUT RULES

- Caveman format per `FORMAT.md`.
- Preserve identifiers, paths, code verbatim.
- Numbering monotonic — never reuse §V.N or §B.N.
- §T row `cites` column ! list §V/§I deps: `T5|.|impl auth mw|V2,I.api`.

## NON-GOALS

- No sub-agents. Main thread writes.
- No dashboards, no logs, no state files beyond SPEC.md itself.
- No auto-build after spec. User invokes build explicitly.
