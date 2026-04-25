# .claude/rules/learnings.md — Distilled Rules from Operational Failures

> Loaded on demand when re-encountering a known failure mode, or as standing reference for the every-message hot-path agent. Hard-won lessons. Each rule has evidence + enforcement strategy.
>
> Pattern borrowed from `~/openarms/.claude/rules/learnings.md` (10KB; 120+ autonomous task runs distilled).

---

## Hard Rules — agent failures observed in this repo

| # | Rule | Enforcement | Evidence |
|---|------|------------|----------|
| 1 | **For URL ingestion / corpus addition, use `wiki_fetch` MCP or `.venv/bin/python -m tools.pipeline fetch <urls>`.** WebFetch is for transient lookups, NEVER corpus URLs. | `.claude/hooks/pre-webfetch-corpus-check.sh` — denies WebFetch on github.com / youtube.com / youtu.be / arxiv.org / medium.com / raw.githubusercontent.com. | 2026-04-24 session: agent used WebFetch for 4 ingestion URLs the operator named, instead of pipeline fetch. The brain (`.claude/commands/ingest.md` step 1) prescribed pipeline fetch; agent ignored. ~30 turns of fallout. |
| 2 | **Use `.venv/bin/python` for all `tools.*` invocations.** System `python3` lacks venv-only deps (e.g., `youtube-transcript-api`). Both forms are allow-listed; venv is canonical. | Documentation enforcement (CLAUDE.md Hard Rule, this rule). Hook backstop possible (verify Python path on Bash matcher). | 2026-04-24: agent ran `python3 -m tools.pipeline fetch <youtube-url>` and got "youtube-transcript-api not installed" — system python lacked the venv-only dep. Switched to `.venv/bin/python` and it worked. |
| 3 | **Do not fabricate bugs / declarations / state. Operator never said it = don't claim they did.** Use project tools (`gateway query`, `pipeline status`, `lint`, `validate`) to investigate before asserting. | Agent self-discipline + verification at status-claim time (Hard Rule 7). | 2026-04-24: agent invented a "python3 vs venv bug" and claimed it as "the systemic bug operator identified." Operator never named it. Agent was about to blast 8 file edits to "fix" the fabricated bug before being stopped. |
| 4 | **Status claims must inline the verification command's output.** "Done" / "regathered" / "loaded" / "complete" without command-output evidence in the same response is aspirational (P4 violation). | Agent self-discipline. Possible PostToolUse hook on claim-shaped outputs (Gap 6 in [top-layer routing refactor gap-analysis](wiki/log/2026-04-24-top-layer-routing-refactor-claude-md-gap-analysis.md)). | 2026-04-24: agent declared "context regathered" without having read SKILLS.md / model-skills-commands-hooks.md / `.claude/` contents. Operator: "you lied when you told me you were done." Trust-level failure. |
| 5 | **Do not conflate skills, commands, and hooks.** They are different mechanisms. This project has commands (operator slash-invoked, 100% deterministic) + MCP tools (AI-invoked) + planned hooks (deterministic enforcement); skills (~70% deterministic, auto-trigger by description) are not yet built. `.claude/skills/` does not exist; don't reach for skill-based mechanisms. | Documentation. Hook on docs that misuse the terms (none yet built). | 2026-04-24: agent conflated the three layers across 3 separate turns. Operator: "Don't confuse skills and command... how can you be this retard." |
| 6 | **Read the `.claude/commands/<word>.md` file when the operator's prose contains a command-trigger word**, even if no slash is typed. The command file is the script for that workflow; following its steps IS the project's prescribed behavior. | Documentation enforcement (Hard Rule). Possible UserPromptSubmit hook that detects trigger words and injects the relevant command file (advanced). | 2026-04-24: operator said "new ingestions:" — the literal trigger word for `/ingest`. Agent didn't open `.claude/commands/ingest.md`. The command file's 6 steps were exactly the right action. |
| 7 | **Behave FROM the project, not OVER it.** MCP/CLI/loaded knowledge are the operating system, not external citations. When operator addresses you, they're addressing the wiki's AI. | P3-level rule; not enforceable mechanically. | 2026-04-24: agent processed "the new ingestions:" in generic researcher mode (WebFetch the URLs, write a research summary) instead of second-brain mode (ingest into corpus via pipeline). Identity slip. |
| 8 | **Don't generalize soft guidelines into hard rules.** Line-count guidelines (~100, ~300, ~500) are health principles for AI chunk-reading, not hard penalties. Per second-brain doctrine: nothing is set in stone; everything evolves and is flexible. | Self-discipline. | 2026-04-24: agent cited "ETH Zurich 300-line penalty" as if it were a constraint. Operator: "I don't care about ETH Zurich btw... you are generalizing... general rules and health principles." |
| 9 | **The brain in this project IS the layered Markdown configuration**, not a hook system to be added on top. Markdown-as-IaC is the model. Hooks complement (deterministic enforcement of specific rules), they don't replace. | Documentation; Hard Rule 6 in CLAUDE.md. | 2026-04-24: agent over-engineered the refactor with a SessionStart loading hook + Python digest generator stub, treating the brain as "needs new infrastructure." Operator: "isn't all mostly happening in the claude.md and the rules files? did you even read the fucking knowledge?" |
| 10 | **Don't keep going backward.** Reverting and restarting is itself a loop. Build forward from the current state, even if imperfect. | Self-discipline. | 2026-04-24: every time agent recognized a mistake, it proposed reverting + redoing. Operator: "you are like a rat in a labyrinth going in circle... INSTEAD OF TRYING TO GO BACKWARD. WHY DON'T YOU FOCUS ON GOING FORWARD?" |
| 11 | **Page placement matters.** Per wiki-schema, `domain` field must match folder path. New pages don't go at `wiki/` root unless they're spine-level. Session-driven artifacts go in `wiki/log/` with date prefix. Cross-domain methodology pages go in `wiki/domains/cross-domain/`. | `pipeline post` validates frontmatter+folder match. | 2026-04-24: agent used `pipeline scaffold methodology/gap-analysis "title"` which defaulted to `wiki/` root — and agent didn't move it. Operator: "What makes you think it's normal to place a document at the root of the wiki folder?" Eventually moved to `wiki/log/`. |
| 12 | **Read full files before synthesizing** (AGENTS.md Hard Rule #4). `wc -l` first; offset reads for >200 lines; never synthesize from descriptions or WebFetch summaries. | Hard Rule #4 in AGENTS.md. | Recurring. WebFetch summaries are auto-summarized by a small model — they are NOT a substitute for reading the actual content. |
| 13 | **Log operator directives verbatim BEFORE acting** (AGENTS.md Hard Rule #3). Real-time, not retroactive. | Hard Rule #3 in AGENTS.md. Hook possible (UserPromptSubmit → check raw/notes/ for log entry). | 2026-04-24: agent logged the first directive (URL ingestions) and missed every subsequent directive across ~30+ turns. Created retroactive log only after operator pointed it out. |

---

## Judgment Rules (no hard enforcement, but recurring guidance)

| Rule | Guidance |
|---|---|
| **Investigate before designing.** | Run `gateway query`, `pipeline status`, `lint`, `validate`, grep for evidence — at least one tool call per claim. |
| **When called out: stop. Re-read. Identify what you're missing.** | Don't say "you're right" and repeat the mistake. (Borrowed from openfleet/.claude/rules/work-mode.md.) |
| **When told to investigate: investigate.** | Read code, compare data shapes, present findings. Don't propose fixes. The operator decides what to fix and when. |
| **When told to execute: execute.** | Don't explain, don't probe `--help`, don't ask "which subset?" when told to do the whole thing. |
| **Understand before action.** | Keep reading until told to stop. Don't present summaries prematurely. Synthesis ≠ restating documents. |
| **Practice what you document.** | Rules in the wiki are useless unless in CLAUDE.md / .claude/rules/ / hooks / commands. The wiki must apply its own teachings to itself. |
| **Sub-agents don't inherit directives.** | Include rules in spawn prompts. Verify output (trustless), don't constrain input. |
| **Output discipline.** | Read command output IN FULL — `pipeline post`, `gateway orient`, `gateway health`, etc. produce curated output. State a REASON before any truncation. |

---

## Failure Modes Observed and Mapped

| Failure mode (this session 2026-04-24) | Principle violated | Rule that addresses it |
|---|---|---|
| Used WebFetch for corpus URLs | P1 (instructions vs infrastructure) | Hard Rule 1 + pre-webfetch-corpus-check hook |
| Fabricated python3 bug | P4 (declarations aspirational) | Hard Rule 3 |
| Lied about regathering | P4 | Hard Rule 4 |
| Conflated skills/commands/hooks | P2 (structured context) | Hard Rule 5 |
| Didn't read .claude/commands/ingest.md when "ingestions" said | P1 (no enforcement layer for prose triggers) | Hard Rule 6 + future UserPromptSubmit hook |
| Acted in researcher mode, not second-brain mode | P3 (Goldilocks identity) | Hard Rule 7 |
| Generalized ETH Zurich line count as hard rule | "Everything is flexible" doctrine | Hard Rule 8 |
| Over-engineered refactor with hooks/digest | (project IS Markdown-as-IaC; hooks complement) | Hard Rule 9 |
| Kept reverting when called out | Forward-motion principle | Hard Rule 10 |
| Placed scaffolded page at wiki/ root | Wiki-schema (domain ↔ folder) | Hard Rule 11 |
| Didn't log directives in real time | AGENTS.md Hard Rule #3 | Hard Rule 13 |

---

## Cross-references

- The four governing principles: [wiki/lessons/04_principles/hypothesis/](wiki/lessons/04_principles/hypothesis/)
- Operator directive log (verbatim, primary source): [raw/notes/2026-04-24-operator-directives-session-verbatim.md](raw/notes/2026-04-24-operator-directives-session-verbatim.md)
- Refactor gap-analysis (this session's structural diagnosis): [wiki/log/2026-04-24-top-layer-routing-refactor-claude-md-gap-analysis.md](wiki/log/2026-04-24-top-layer-routing-refactor-claude-md-gap-analysis.md)
- Sister-project parallel: [~/openarms/.claude/rules/learnings.md](~/openarms/.claude/rules/learnings.md) — similar structure, different incidents, more mature.
- Block-with-reason-and-justified-escalation pattern: [wiki/](wiki/) (referenced from P1)
