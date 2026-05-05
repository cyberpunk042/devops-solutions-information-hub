---
type: directive
date: 2026-05-05
session: /opt second-brain agent (this conversation)
operator: jfm.devops.expert@gmail.com
status: active
tags: [directive, opt-in, feature-transcension, root-to-projects, sister-project-propagation, second-brain-itself, sacrosanct]
---

# Operator directive — opt-in transcension of root-project features to individual projects

## Verbatim (sacrosanct)

> "continue. we are also going to find a way to opt in into feature of the root project that start to be interesting that could transcend down into the individual project when desired such as now."

## Decomposition (additive to the active /loop directive)

| Segment | Meaning |
|---|---|
| "continue" | Keep iterating the active /loop ("till we finished ingesting and processing and evolving") |
| "we are also going to find a way to opt in" | New mechanism layer: opt-in (operator-or-project-controlled), NOT auto-applied |
| "into feature of the root project" | Source of the features = root-ghostproxy at /root |
| "that start to be interesting" | Selection criterion = features that have proven valuable in /root |
| "that could transcend down into the individual project" | Direction: /root → individual project (transcension is propagation) |
| "when desired such as now" | "Such as now" indicates **the second brain is currently a target** for some transcended features (this very session) |

## What this means

root-ghostproxy is itself a project, but it has been the **most heavily exercised** in this conversation arc — its agent-behavior bugs surfaced first, and the structural fixes landed there first. The fixes include:

- **Modes**: PM Scrum Master / DevOps Architect / Dual Expert (with `/mode-pm`, `/mode-architect`, `/mode-dual`, `/mode-clear`, `/mode-status`)
- **`/cycle` autopilot**: mode-aware deterministic cycle dispatch
- **SessionStart hook → /orient command**: active orientation on cold start
- **Operating principles** rule with 12 numbered principles
- **systemic-bugs.md** governance register integrated with /cycle
- **`tools.blockers --filter`** subcommand for blocker SRP discipline
- **loop-cron-lifecycle.md** with 7 scenarios + autonomous-cancellation grant + trigger refinement
- **Three-layer file-handling**: .gitignore + .claudeignore + permissions.deny
- **Two-layer hook architecture** (with cross-firing lesson)
- **Compound-waterfall input retention** rule
- **Workblock-priority** discipline (systemic fix interrupts feature work)
- **Bug-fix flow**: log → analyze → identify → fix → verify → confirm
- **Spec-driven-evolution** doctrine (the 5th governing principle)
- **Verbatim-log layer** at `/root/wiki/log/`

Many of these are **universal patterns** — they apply to any agent-driven project, not just root-ghostproxy. The operator's directive: design an opt-in channel so individual projects (including the second-brain itself) can adopt these features when desired.

## "Such as now" — what the second brain currently desires

The second brain (this project, /opt) does NOT yet have:
- A `/cycle` command or autopilot infrastructure
- Modes (PM / Architect / Dual)
- A `systemic-bugs.md` governance register
- A `governance/` folder with blockers / decisions / progress / future-work
- A `loop-cron-lifecycle` rule
- An `operating-principles.md` rule with the 12 principles
- A `compound-waterfall` rule
- A SessionStart `/orient` command + hook (it has session-start.sh but no /orient)
- A `tools.blockers --filter` equivalent

The second brain DOES have:
- CLAUDE.md, AGENTS.md, .claude/rules/*.md (8 rules), .claude/commands/ (some)
- pipeline / gateway / view / stats / lint / validate tools
- Wiki content, methodology engine, source syntheses, lessons, patterns, principles
- The ingestion layer (raw → synthesis → post → crossref)

So **the second brain could opt-in to**: governance register pattern, modes pattern (with adapted lenses for ingestion vs synthesis vs distillation), /cycle pattern, operating-principles structure, compound-waterfall, etc. Each is a distinct opt-in.

## Design space for the opt-in mechanism

| Option | What | Pros | Cons |
|---|---|---|---|
| **A: Pattern in second brain** | Each transcendable feature lives as a pattern in `/opt/.../wiki/patterns/03_validated/`; consuming projects pull when they opt in | Already partially done (three-mode-pattern is there); reuses existing infrastructure | Pattern → adoption gap is currently manual |
| **B: Adoption Guide section** | Each pattern has an "Adoption" subsection: prerequisites, files to copy, settings to add, verification | Concrete checklist per feature | Verbose; per-pattern maintenance |
| **C: Slash command in /root** | `/transcend <feature> --target <project>` writes the pattern's files into the target | Mechanical; reproducible | Requires /root agent to operate cross-project (boundary issue) |
| **D: tools.adopt at /opt** | `tools.adopt --feature <name> --target <path>` reads the pattern + scaffolds the target | /opt is the second brain — feature catalog lives here naturally | Per-feature implementation needed |
| **E: Manifest-driven** | Each transcendable feature has a YAML manifest (`feature-manifests/<feature>.yaml`); a tool reads + applies | Declarative; testable; per-target customization via yaml overrides | Most engineering up-front but most scalable |

Operator's directive doesn't specify. Likely the right answer is some combo of A (catalog in patterns) + Adoption Guide section per pattern (B) + a tooling layer (D or E) for mechanical scaffolding. Operator-input desired before building.

## Workblock discipline (this directive doesn't pivot the loop)

Per sidetrack-detection-and-recovery and compound-waterfall:
- Original loop directive: "lets loop till we finished ingesting and processing and evolving... pass through gates"
- New directive: opt-in transcension of /root features
- Treat as **additive within active loop** — loop iterations now also surface transcension candidates and propose adoption mechanisms

NOT a pivot — the loop continues with this added context.

## Action queue (this iteration)

1. Capture this directive verbatim — DONE (this file)
2. Identify the **most-immediately-transcendable** features (highest leverage for second brain)
3. Surface to operator: list of transcendable features + opt-in mechanism options
4. Operator decides which mechanism + which features to adopt first
5. Continue loop iteration
