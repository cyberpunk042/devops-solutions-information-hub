# .claude/rules/hook-architecture.md — Hook Design + Mechanism-Determinism Levels

> Loaded on demand when designing, debugging, or invoking hooks. CLAUDE.md has the summary.

## Mechanism-Determinism Levels (operator directive 2026-04-24)

| Mechanism | Determinism | Trigger | Use when |
|---|---|---|---|
| **Hook** | Logical (block + reason + remediation) | Tool-call lifecycle event | Structural enforcement: rule MUST hold at this point. |
| **Command** (`.claude/commands/`) | **100% deterministic** | Operator types `/<name>` | Workflow with predictable, scripted steps; operator-driven. |
| **Skill** (`.claude/skills/`) | **~70% deterministic** | Auto-triggered by description-match on operator prose | Workflow where auto-trigger is desirable; description quality determines reliability. **Not yet built in this project.** |
| **MCP tool** | Programmatic | AI invokes during reasoning | Discrete operations; deferred load via ToolSearch. |
| **CLI** | Programmatic | AI runs via Bash | Shell-mediated operations; chaining or piping needed. |

The operator's clarification: "commands = 100% deterministic and skills = 70%. Hooks have to be logical insertions or orders and logical reasons and remediations offers."

## Hook Design Pattern (every hook MUST follow)

A hook in this project has three load-bearing components:

### 1. Logical insertion point

The hook must fire at the right Claude Code lifecycle event with the right matcher. Wrong insertion = either misses the rule or false-positives unrelated calls.

| Event | When it fires | Use for |
|---|---|---|
| `PreToolUse` | Before a tool call executes | Block forbidden actions; modify inputs in-flight |
| `PostToolUse` | After a tool call completes | Validate outputs; trigger downstream actions |
| `SessionStart` | At session start | Inject ambient context; print reminders |
| `PostCompact` | After context compaction | Restore behavioral state lost during compaction |
| `UserPromptSubmit` | When operator submits a prompt | Detect prose triggers; inject command-file content |
| `Stop` / `SubagentStop` | When agent finishes | Force continuation if completion is premature |

Pick the event whose semantics match the rule being enforced. Wrong event = wrong enforcement.

### 2. Logical reason

The hook must explain WHY it acted. Operator and AI both need to understand the rule being enforced. A hook that blocks with no reason is a black box; an AI that can't explain the block can't learn from it.

Convention in this project's hooks:
- Hook prints: `BLOCKED: <action>. REASON: <rule>. <citation>`
- Citation references the rule's home (CLAUDE.md Hard Rule N, or `.claude/rules/<topic>.md`).

### 3. Remediation offer

The hook must offer the correct alternative. "Don't do X" without "do Y instead" leaves the AI stuck. The whole point of `block-with-reason-and-justified-escalation` (cited in P1's relationship graph) is that enforcement must be MINDFUL.

Convention:
- Hook prints: `INSTEAD: <correct command>. BYPASS: <how to legitimately escalate if needed>`

## Bypass / Escalation

Hooks must offer a documented bypass for legitimate cases. Blind enforcement creates its own failures (OpenArms T086: correct fix reverted twice because hook looked like scope creep).

Bypass patterns:
- **Env-var bypass**: `REASON=<reason>` env var on the bash call documents why a normally-blocked action is justified.
- **Operator override**: hook deferes to operator approval if operator-PR-approved.
- **Logged exception**: hook allows but logs to `wiki/log/` for audit.

## Hooks in This Project

### Built (planned) for the corrupted-brain refactor

| Hook | Event | Matcher | Reason | Remediation | Bypass |
|---|---|---|---|---|---|
| `pre-webfetch-corpus-check.sh` | PreToolUse | WebFetch | Corpus URLs (github.com / youtube.com / youtu.be / arxiv.org / medium.com / raw.githubusercontent.com) must route through `wiki_fetch` MCP or `pipeline fetch` for proper raw/ ingestion + provenance + ratio gate. (CLAUDE.md Hard Rule 6, learnings.md #1.) | "Use `.venv/bin/python -m tools.pipeline fetch <url>` or `wiki_fetch` MCP tool." | `REASON=transient-lookup` env var to bypass for non-ingestion lookups. |
| `pre-bash.sh` | PreToolUse | Bash | Truncation pipes (`\| head`, `\| tail`, `\| grep`) violate Hard Rule 1 (read internal-tool output in full). Curated output is meant to be read entirely. (CLAUDE.md Hard Rule 1, learnings.md.) | "Run command without truncation. Internal tools (`gateway`, `view`, `pipeline`) produce curated output." | `REASON=<reason>` env var to bypass. |
| `session-start.sh` | SessionStart | — | Agent enters session without the loaded knowledge ambient (super-model / 4 principles / methodology). Reminder needed to invoke `gateway orient`. | "Run `.venv/bin/python -m tools.gateway orient` before first work action." | None — pure reminder. |
| `post-compact.sh` | PostCompact | — | Compaction loses behavioral corrections + sacrosanct directives. State must be restored from authoritative files. (Per [[context-compaction-is-a-reset-event]] lesson.) | "Re-print sacrosanct directives + Hard Rules + reference to `wiki/log/`." | None — restoration is mandatory. |

### Settings.json wiring (proposed)

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "WebFetch",
        "hooks": [{"type": "command", "command": "bash .claude/hooks/pre-webfetch-corpus-check.sh", "timeout": 5}]
      },
      {
        "matcher": "Bash",
        "hooks": [{"type": "command", "command": "bash .claude/hooks/pre-bash.sh", "timeout": 5}]
      }
    ],
    "SessionStart": [
      {"hooks": [{"type": "command", "command": "bash .claude/hooks/session-start.sh", "timeout": 10}]}
    ],
    "PostCompact": [
      {"hooks": [{"type": "command", "command": "bash .claude/hooks/post-compact.sh", "timeout": 10}]}
    ]
  }
}
```

## Anti-Patterns (what NOT to do)

| Anti-pattern | Why bad |
|---|---|
| **Hook that blocks without a reason** | AI can't learn; operator confused; black-box enforcement. |
| **Hook with no remediation** | AI stuck; "what should I do instead" unanswered. |
| **Hook with no bypass** | Legitimate cases (transient lookups, debugging) blocked; AI starts circumventing structurally. |
| **Hook that fires on the wrong event** | Either misses the rule or false-positives unrelated calls. |
| **Replacing commands with hooks** | Commands are 100% deterministic operator UI. Hooks enforce. Different mechanisms, different purposes. Don't replace. |
| **Replacing skills with hooks** | Skills auto-trigger on operator prose for high-level workflows; hooks enforce at tool-call boundary. Different layers. |

## Cross-references

- Block-with-reason-and-justified-escalation: [wiki/lessons/](wiki/lessons/) (cited in P1's relationship graph)
- Enforcement-must-be-mindful-hard-blocks-need-justified-bypass: [wiki/lessons/](wiki/lessons/)
- P1 (Infrastructure > Instructions): [wiki/lessons/04_principles/hypothesis/infrastructure-over-instructions-for-process-enforcement.md](wiki/lessons/04_principles/hypothesis/infrastructure-over-instructions-for-process-enforcement.md)
- Skills/commands/hooks model: [wiki/spine/models/agent-config/model-skills-commands-hooks.md](wiki/spine/models/agent-config/model-skills-commands-hooks.md)
- OpenArms hook reference (production): `~/openarms/.claude/settings.json` + `~/openarms/scripts/methodology/hooks/`
