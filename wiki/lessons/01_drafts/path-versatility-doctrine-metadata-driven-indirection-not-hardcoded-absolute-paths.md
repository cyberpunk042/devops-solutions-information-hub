---
title: "Lesson — Path-versatility doctrine: configs must work across machines via metadata-driven indirection (env vars, relative paths, parameters), not hardcoded absolute paths"
aliases:
  - "Path-Versatility Doctrine"
  - "Metadata-Driven Path Indirection"
  - "Configs Across Machines Lesson"
  - "Hardcoded Absolute Paths Anti-Pattern"
type: lesson
domain: cross-domain
layer: 2
status: synthesized
confidence: high
maturity: seed
created: 2026-05-06
updated: 2026-05-06
last_reviewed: 2026-05-06
sources:
  - id: operator-directive-2026-05-05-versatility
    type: file
    file: raw/notes/2026-05-05-thorough-review-context-engineering-versatility-and-network-spec-note.md
    description: "Operator-explicit 2026-05-05 directive — versatility / metadata-driven-configs / *'we do configs smart with proper metadata and parameters and relatives info and logic'*; named at least 1 lesson at `wiki/lessons/` as the deliverable"
  - id: operator-directive-2026-05-06-fix-now
    type: file
    file: wiki/log/2026-05-06-session-handoff-pre-compaction-multi-arc-research-sweep-and-infrastructure-wiring.md
    description: "Operator-explicit 2026-05-06 — *'we are coming from another system that the second-brain is inside the second-brain... we should just support it.. we have a relative / flexible strategy.. we need to fix this now. usualy there is the $HOME variable for example'*; triggered Stop hook fix using ${CLAUDE_PROJECT_DIR} env-indirection"
  - id: empirical-stop-hook-fix
    type: wiki
    file: .claude/hooks/end-of-cycle-stamp.sh
    description: "Empirical anchor — line 35 changed from `Path('$HOME/devops-solutions-information-hub')` to `Path(os.environ.get('CLAUDE_PROJECT_DIR', '$HOME/devops-solutions-information-hub'))`; settings.json line 164 updated in parallel; loop bug ended"
  - id: empirical-six-hook-completion
    type: wiki
    file: .claude/settings.json
    description: "Empirical anchor — 6 additional hook command paths (PreWebFetch, PreBash, SessionStart×2, PostCompact×2) swapped to ${CLAUDE_PROJECT_DIR}; PostCompact failure on /compact event revealed the gap; pre-bash hook live-fired post-fix proving env-indirection works"
  - id: principle-1
    type: wiki
    file: wiki/lessons/04_principles/hypothesis/infrastructure-over-instructions-for-process-enforcement.md
    description: "P1 — env-indirection IS infrastructure (resolved by harness/shell deterministically); 'remember to fix paths' would be prose at ~25% compliance"
  - id: principle-4
    type: wiki
    file: wiki/lessons/04_principles/hypothesis/declarations-are-aspirational-until-infrastructure-verifies-them.md
    description: "P4 — the Stop hook fix declared 'use env-indirection' but didn't verify all hooks did; PostCompact failure was the verification gap; completing the fix verified P4"
  - id: feedback-root-propagates
    type: notes
    file: ~/.claude/projects/-home-jfortin-devops-solutions-information-hub/memory/feedback_root_propagates_agent_config_dont_author_project_local.md
    description: "Companion memory — when root-ghostproxy propagates agent-config across machines, the propagated configs themselves need path-flexibility; this lesson is the doctrine that propagated configs must implement"
tags: [lesson, path-versatility, metadata-driven-configs, env-indirection, hardcoded-paths-anti-pattern, cross-machine-portability, sister-project-applicable, layer-2, p1-application, p4-application, infrastructure-not-instructions, mission-2026-05-06, "${CLAUDE_PROJECT_DIR}", $HOME]
---

# Lesson — Path-versatility doctrine: configs must work across machines via metadata-driven indirection, not hardcoded absolute paths

## Summary

Hardcoded absolute paths in agent-config files (`.claude/settings.json` hook commands, shell-snippet command files, Python scripts that compute project paths, CLAUDE.md path references in operator-injection blocks) violate cross-machine portability. When a project moves between hosts — e.g., `$HOME/devops-solutions-information-hub` on a `root` user vs `/home/jfortin/devops-solutions-information-hub` on an unprivileged user — every absolute path becomes wrong-on-this-machine and downstream behavior breaks (hook scripts not found → error fed back as user message → reflexive "Standing by" agent response → another hook fire → hard infinite loop, observed empirically 2026-05-06). The fix is **metadata-driven indirection**: declare WHAT the config means structurally (e.g., "the project root"), let the runtime resolve WHERE that is via env var (`${CLAUDE_PROJECT_DIR}` for Claude Code, `$HOME` for user-relative), relative path from a known anchor, or schema field. Operator-explicit 2026-05-05: *"we do configs smart with proper metadata and parameters and relatives info and logic"*. Operator-explicit 2026-05-06 (verbatim, after the loop bug surfaced): *"we are coming from another system that the second-brain is inside the second-brain... we should just support it.. we have a relative / flexible strategy.. we need to fix this now. usualy there is the $HOME variable for example."* This lesson generalizes both directives into a doctrine: hardcoded absolute paths are an anti-pattern; metadata-driven indirection is infrastructure-not-instructions (P1) and must be applied uniformly across ALL configs in the same family (P4 — declaring "use env-indirection" without verifying every config does so leaves a gap).

## Context

> [!info] **When this lesson applies**
>
> | Configuration class | Apply this doctrine? |
> |---|---|
> | Project-internal absolute paths in `.claude/settings.json` hook command lines | **YES** — use `${CLAUDE_PROJECT_DIR}` |
> | Project-internal absolute paths in shell snippets inside `.claude/commands/*.md` | **YES** — use `${CLAUDE_PROJECT_DIR}` |
> | Project-internal paths in Python scripts that the project ships | **YES** — `os.environ.get("CLAUDE_PROJECT_DIR", fallback)` with documented fallback |
> | Path strings in CLAUDE.md / AGENTS.md / instructional banners injected into agent context | **YES** — but hold off if operator-authored content; flag for operator-decision |
> | Genuine fixed external system paths (e.g., `/var/log/syslog`, `/etc/hosts`) | NO — these are not project-relative; the absolute path IS the resource identity |
> | Paths inside `.gitignore` / `.gitattributes` / repo-config files (paths there are repo-relative by tooling) | NO — git tooling already handles relative-to-repo resolution |
>
> The doctrine is specifically about **project-internal paths declared in agent-config layers that travel with the project** (settings, hooks, commands, project-shipped scripts).

## Insight

> [!tip] **Hardcoded absolute paths are a portability anti-pattern. Configs declare WHAT, runtime resolves WHERE.**
>
> A config file that ships with a project should declare its intent in a way the runtime can resolve correctly on any host where the project is installed. Hardcoded absolute paths bake one host's filesystem into the config; metadata-driven indirection (env var, relative resolution, schema field) decouples the structural meaning ("the project root") from the host-specific manifestation (`$HOME/devops-solutions-information-hub` vs `/home/jfortin/...`).
>
> The deeper insight: this is a **P1 (Infrastructure Over Instructions)** application. Env-indirection is infrastructure — the shell/harness resolves the placeholder deterministically every fire. Prose-level guidance ("remember to fix the paths when you move the project") is ~25% reliable. Env-indirection is ~100% reliable.
>
> And it's a **P4 (Declarations Aspirational Until Verified)** application: declaring "use env-indirection" once on the loop-causing hook (Stop) without verifying all sibling hooks do too leaves a verification gap that surfaces only when the next sibling fires (PostCompact on `/compact`). The fix isn't complete until ALL configs in the same family are verified.

## Evidence

> [!success]- **Evidence 1 — 2026-05-06 Stop hook hard-loop bug (the trigger event)**
>
> Per [2026-05-06 session handoff](../../log/2026-05-06-session-handoff-pre-compaction-multi-arc-research-sweep-and-infrastructure-wiring.md): the operator's setup imported `.claude/settings.json` from another machine where the second-brain was at `$HOME/devops-solutions-information-hub/`. On the new machine ($HOME=/home/jfortin/, project at `/home/jfortin/devops-solutions-information-hub/`), the Stop hook command `python3 $HOME/devops-solutions-information-hub/.claude/hooks/end-of-cycle-stamp.sh` resolved to a non-existent path. The Python invocation errored; the harness fed the error back as an injected user message; the agent reflexively responded "Standing by" each time; that triggered another Stop event; **hard infinite loop**.
>
> Operator's verbatim diagnosis: *"Wow ... the AI just entered a hard loop bug lol"* — surfaced after several cycles.
>
> Operator's verbatim fix directive: *"we are coming from another system that the second-brain is inside the second-brain... we should just support it.. we have a relative / flexible strategy.. we need to fix this now. usualy there is the $HOME variable for example."*
>
> **The empirical pattern**: hardcoded absolute path → cross-machine breakage → cascading loop. The cost was substantial (multiple cycles before operator caught the loop signature).

> [!success]- **Evidence 2 — Stop hook fix landing first; sibling hooks still hardcoded (the P4 verification gap)**
>
> Initial fix landed at one place:
>
> ```diff
> # .claude/settings.json:164
> - "command": "python3 $HOME/devops-solutions-information-hub/.claude/hooks/end-of-cycle-stamp.sh"
> + "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/end-of-cycle-stamp.sh"
>
> # .claude/hooks/end-of-cycle-stamp.sh:35
> - PROJECT_ROOT = Path("$HOME/devops-solutions-information-hub")
> + PROJECT_ROOT = Path(os.environ.get("CLAUDE_PROJECT_DIR", "$HOME/devops-solutions-information-hub"))
> ```
>
> Loop ended. But the operator's directive was *systemic* (*"we have a relative / flexible strategy"*) — the same pattern applied to ALL hooks, not just Stop. The PreWebFetch + PreBash + 2× SessionStart + 2× PostCompact still had hardcoded `/opt/` paths. **The verification gap surfaced when `/compact` fired post-fix and both PostCompact hooks failed with `No such file or directory`** — same root cause, different lifecycle event.

> [!success]- **Evidence 3 — Six-hook completion (the doctrine applied uniformly)**
>
> Post-PostCompact-failure, all 6 remaining hardcoded `/opt/` occurrences in `.claude/settings.json` were swapped in one Edit operation:
>
> ```diff
> # .claude/settings.json — 6 hook command paths
> - bash $HOME/devops-solutions-information-hub/.claude/hooks/pre-webfetch-corpus-check.sh
> + bash ${CLAUDE_PROJECT_DIR}/.claude/hooks/pre-webfetch-corpus-check.sh
> - bash $HOME/devops-solutions-information-hub/.claude/hooks/pre-bash.sh
> + bash ${CLAUDE_PROJECT_DIR}/.claude/hooks/pre-bash.sh
> - bash $HOME/devops-solutions-information-hub/.claude/hooks/session-start.sh
> + bash ${CLAUDE_PROJECT_DIR}/.claude/hooks/session-start.sh
> - python3 $HOME/devops-solutions-information-hub/.claude/hooks/session-orient.sh
> + python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/session-orient.sh
> - bash $HOME/devops-solutions-information-hub/.claude/hooks/post-compact.sh
> + bash ${CLAUDE_PROJECT_DIR}/.claude/hooks/post-compact.sh
> - python3 $HOME/devops-solutions-information-hub/.claude/hooks/post-orient.sh
> + python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/post-orient.sh
> ```
>
> JSON validity verified post-edit. **Empirical confirmation of working env-indirection**: pre-bash hook live-fired during the same session immediately after, blocking a reflexive `| head -40` truncation pipe — the hook script was found, executed, and reported correctly. Path-versatility was verified end-to-end on the running machine.

> [!success]- **Evidence 4 — Operator's verbatim doctrine (2026-05-05, broader than just hooks)**
>
> Per [raw/notes/2026-05-05-thorough-review-context-engineering-versatility-and-network-spec-note.md](../../../raw/notes/2026-05-05-thorough-review-context-engineering-versatility-and-network-spec-note.md): *"we also need to make sure that we make things versatile, e.g. on this system the second-brain is at $HOME/devops-solutions-information-hub and right now for example I am as root instead of a normal user so the path is different and stuff and if I had both the /home/jfortin and /root setup they can both connect to the second-brain, we do configs smart with proper metadata and parameters and relatives info and logic like for the system project config with the repo config / data for example."*
>
> The doctrine extends beyond `.claude/settings.json`: ANY config file that travels with the project must accept multiple installation contexts — root user with homedir `/root`, unprivileged user with homedir `/home/<user>`, system-level install at `$HOME/devops-solutions-information-hub`. Metadata + parameters + relatives + logic, not hardcoded absolutes.

## Applicability

> [!info] **Decision matrix — apply where, hold where**
>
> | Stance | Apply this doctrine? |
> |---|---|
> | Agent-config that travels with the project (`.claude/settings.json`, `.claude/hooks/*.sh`, `.claude/commands/*.md`, project-shipped Python scripts that resolve paths) | YES — use env-indirection or relative paths |
> | Operator-authored instructional banners that mention `$HOME/devops-solutions-information-hub` or other paths descriptively (e.g., `session-orient.sh`'s DIRECTIVE string) | OPERATOR-DECISION — fix is symmetrical but content is operator-authored; surface for explicit authorization rather than unilateral edit |
> | Cross-project sister-projects.yaml `path: ~/...` declarations | YES — `~` is canonical; `Path.expanduser()` resolves at runtime per user |
> | Genuine fixed external resources (`/var/log/syslog`, `/etc/hosts`, `/proc/cpuinfo`) | NO — those paths ARE the resource identity, not project-relative |
> | Repo-internal paths that git already handles (`.gitignore`, `.gitattributes`) | NO — git tooling makes them repo-relative implicitly |
> | Documentation that cites the project's expected install path as one example | NO — but flag the example as illustrative, not normative |
>
> The boundary: when the path travels WITH the project (config file inside `.claude/` or `tools/`), apply. When the path identifies a fixed external resource, don't. When the path is operator-authored instructional content, defer to operator.

## How to Apply

> [!tip] **Concrete steps to audit + fix path-versatility in any project**
>
> 1. **Inventory**: `grep -nrE '/opt/|/home/|/root/|/Users/' .claude/ tools/` to find absolute-path occurrences in agent-config layers.
> 2. **Classify each**: (a) genuine fixed external — leave; (b) project-internal path — parameterize.
> 3. **Substitute**:
>    - For shell command lines in `.claude/settings.json` and `.claude/commands/*.md`: `${CLAUDE_PROJECT_DIR}` (Claude Code's canonical project-root env var)
>    - For Python that the project ships: `os.environ.get("CLAUDE_PROJECT_DIR", "$HOME/devops-solutions-information-hub")` — env var with documented fallback for backward compat on the original-install machine
>    - For shell user-relative paths (e.g., `~/some-tool/`): leave as `~/...` and use `Path.expanduser()` or shell tilde-expansion
>    - For schema fields (e.g., `path:` in YAML): use `~/...` form; the loader handles expansion
> 4. **Verify each substitution structurally** (P4 discipline): for every substitution, confirm the resolved path on the current machine; for projects with multi-machine deploy, run a test on each.
> 5. **Audit completeness uniformly** (P4 discipline): for every change to one file in a family (e.g., one hook entry), check ALL siblings in the same file class. If you fix the Stop hook, also check PreToolUse + SessionStart + PostCompact. The Stop fix is incomplete if siblings are still hardcoded.
> 6. **Document the fallback semantics** in a comment block at the substitution point so future maintainers understand the intent (env var preferred; fallback for compat).
> 7. **Test cross-machine** when feasible: `CLAUDE_PROJECT_DIR=/different/path` should still resolve correctly to that path's `.claude/hooks/...`.

> [!warning] **Anti-patterns to avoid**
>
> - **Hardcoded absolute paths in any config file that travels with the project** — first-machine-move breaks them
> - **Two duplicate paths in two configs** ("one for the second-brain, one for /home/jfortin") — diverges over time; env-indirection unifies
> - **Forgetting fallback** when env var is unset — the lookup must have a documented default
> - **Fixing one occurrence and leaving siblings hardcoded** — P4 violation; the fix is incomplete until verified uniformly
> - **Fixing the symptom (the failing hook) without fixing the doctrine (all hooks)** — operator's 2026-05-06 directive was systemic, not specific
> - **Treating descriptive path strings the same as operational paths** — descriptive content is operator-authored; defer rather than auto-edit

## Open Questions

> [!question] Should descriptive instructional banners (like `session-orient.sh`'s DIRECTIVE string) also be parameterized?
> The string says "the research wiki at $HOME/devops-solutions-information-hub" — operationally fine on the original machine, wrong-as-fact on this machine. Symmetrical fix exists (compute the path at runtime via env var). But the content is operator-authored from /root work; defer to operator for explicit authorization. Default proposal: leave for now; surface in next operator-batch.

> [!question] Should `tools/*.py` modules audit their path-handling for the same pattern?
> Many wiki tools (`pipeline.py`, `gateway.py`, `view.py`, etc.) likely have implicit path assumptions. An audit would identify whether they handle multiple install contexts gracefully. Engineering cost: ~2-4 hours systematic. Defer to operator-batch.

> [!question] Does the Goldilocks Protocol's Type=root + Group=operating-system-setup extension imply specific path-handling rules for type=root projects?
> Per [project-self-identification-protocol](../../domains/cross-domain/methodology-framework/project-self-identification-protocol.md) (2026-05-04 update): root-type projects sit at $HOME (the homedir IS the repo root). This implies their path-handling is fundamentally different from non-root projects (which sit at $HOME/<projectname>). Worth surfacing as an addendum to this lesson once root-ghostproxy install demonstrates the pattern.

> [!question] What's the right Markdown convention for documenting env vars in cross-references and prose?
> This lesson uses `${CLAUDE_PROJECT_DIR}` consistently. Some docs use `$CLAUDE_PROJECT_DIR` (no braces), some use `<env:CLAUDE_PROJECT_DIR>`. Convention proposal: braces always (matches shell-substitution syntax + visually distinct from prose).

## Self-Check — Am I About to Make This Mistake?

> [!warning] Ask yourself before authoring or accepting any agent-config:
>
> 1. **Are there absolute paths in this config?** If yes, classify each.
> 2. **For project-internal paths, am I using env-indirection?** If no, why not?
> 3. **For env vars, did I provide a documented fallback?** If no, the config breaks when the env is unset.
> 4. **Did I check ALL siblings in the same config family?** If I fixed one hook entry, did I check the other 6?
> 5. **Did I verify the substitution structurally** (the resolved path actually works on the current machine)?
> 6. **For multi-machine projects, will this work on the next machine without manual intervention?** If no, the fix is incomplete.

## How This Connects — Navigate From Here

> [!abstract] From This Lesson → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **The principles this demonstrates** | [[infrastructure-over-instructions-for-process-enforcement\|Principle 1 — Infrastructure Over Instructions]] · [[declarations-are-aspirational-until-infrastructure-verifies-them\|Principle 4 — Declarations Aspirational Until Verified]] |
> | **The mission this supports** | Cross-machine portability for the second-brain ecosystem; preserves operator's flexibility-discipline for sister-project deployment |
> | **The Goldilocks dimension this clarifies** | Type=root projects (per [protocol](../../domains/cross-domain/methodology-framework/project-self-identification-protocol.md)) must especially honor this — they sit at $HOME, which varies per user |
> | **The companion memory** | [feedback_root_propagates_agent_config_dont_author_project_local](file:///home/jfortin/.claude/projects/-home-jfortin-devops-solutions-information-hub/memory/feedback_root_propagates_agent_config_dont_author_project_local.md) — when root propagates agent-config, the propagated configs themselves must implement this doctrine |
> | **The hook architecture rule** | [.claude/rules/hook-architecture.md](../../../.claude/rules/hook-architecture.md) — hooks are the primary place this lesson lands; consider folding a path-versatility check into the hook design pattern |

## Sister-Project-Applicability

This lesson applies to **every** project in the operator's ecosystem:

| Project | Why this applies |
|---|---|
| **Research wiki** (this) | Empirical anchor — settings.json fix landed here 2026-05-06 |
| **OpenArms** | Has `.claude/settings.json` + hooks; same pattern would apply on cross-machine deploy |
| **OpenFleet** | Same |
| **AICP** | Same; plus AICP at `~/devops-expert-local-ai/` is user-relative |
| **devops-control-plane** | Same |
| **root-ghostproxy** (when installed) | **Especially applicable** — type=root means the project sits at $HOME directly; path-versatility is structural |

For sister-project consumers: the substitution pattern is the same (`${CLAUDE_PROJECT_DIR}` for shell, `os.environ.get("CLAUDE_PROJECT_DIR", fallback)` for Python). The fallback values may differ per project's original-install path; the env var name is universal.

## Relationships

- DERIVED FROM: [[infrastructure-over-instructions-for-process-enforcement|Principle 1 — Infrastructure Over Instructions]] — env-indirection is infrastructure, not prose
- DERIVED FROM: [[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4 — Declarations Aspirational Until Verified]] — declaring "use env-indirection" without uniform verification leaves gaps
- BUILDS ON: [[fake-blockers-vs-real-blockers-empirical-verification-required|Lesson — Fake Blockers Vs Real Blockers]] — sibling discipline lesson; same operator-explicit "register lesson in second brain" demand pattern
- BUILDS ON: [[broken-and-idle-fresh-sessions-need-active-orientation-not-passive-context-loading|Lesson — Broken-and-Idle]] — sibling Layer-2 lesson; both are agent-config-layer cross-machine concerns
- BUILDS ON: [[agent-modes-three-mode-pattern-with-mode-aware-loop-cycles|Pattern — Agent Modes]] — modes propagated via root-ghostproxy will themselves contain path-strings that must follow this doctrine
- RELATES TO: [[project-self-identification-protocol|Project Self-Identification Protocol]] — Goldilocks Type=root projects (sit at $HOME) need this doctrine especially
- FEEDS INTO: [[root-ghostproxy-sfif-rollout-and-second-brain-integration-2026-05|root-ghostproxy SFIF Rollout Epic]] — propagation channel from root must propagate path-versatile configs

## Backlinks

[[infrastructure-over-instructions-for-process-enforcement|Principle 1 — Infrastructure Over Instructions]]
[[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4 — Declarations Aspirational Until Verified]]
[[Lesson — Fake Blockers Vs Real Blockers]]
[[Lesson — Broken-and-Idle]]
[[Pattern — Agent Modes]]
[[Project Self-Identification Protocol]]
[[root-ghostproxy SFIF Rollout Epic]]
