---
type: finding
date: 2026-05-05
status: unreproduced
context: /opt second-brain agent during patterns + lessons promotion loop
tags: [bash, multi-line-for-loop, variable-expansion, sed-i, transient, agent-tooling]
---

# Finding — Bash multi-line for-loop with `\` continuations failed `$f` expansion (not reproduced in isolation)

## What was observed

While renaming `## Cross-references` → `## Relationships` across 15 lesson files using a bash multi-line for-loop with backslash-continuations:

```bash
for f in \
  wiki/lessons/.../file1.md \
  wiki/lessons/.../file2.md \
  ...
  wiki/lessons/.../file15.md ; do
    if [ -f "$f" ]; then
      sed -i 's/^## Cross-references$/## Relationships/' "$f"
      echo "renamed: $f"
    fi
done
```

Result: `sed: $f: No such file or directory` printed ONCE, exit code 1. Loop terminated after first iteration. Variable `$f` was passed literally to sed instead of expanding.

## Operator framing

Operator: *"okay but things like this you registeer and find the source and we fix.. we dont just work around"*

The agent's reflex was to write a `/tmp/<script>.sh` and `bash <script>.sh` (workaround). Operator's correction: don't work around — register and find the source.

## Investigation performed

| Test | Result |
|---|---|
| Simple 3-element multi-line for-loop with `\` continuations + body using `$f` | works |
| Same 3 lesson paths from the failing command, just `if -f` test | works |
| All 15 lesson paths from the failing command, just `if -f` test | works |
| Read of pre-bash.sh hook (/opt) — only checks truncation pipes, no command mutation | source ruled out |
| Read of malware-block.sh (/root) — DENY/ASK logic but no command mutation | source ruled out |
| Cwd verification — `/opt/devops-solutions-information-hub` was correct | source ruled out |

The exact original failing form (with `sed -i ...` in the body) was NOT re-tried with destructive intent because the rename had already succeeded via the workaround.

## Hypotheses (unverified)

1. **Harness command-encoding edge case**: when the multi-line bash command + `sed -i` body crossed some serialization threshold, `$f` may have been double-escaped or stripped. Would only repro at original send-time, not on isolated retest.
2. **Transient bash subshell state**: a previous tool call left `$f` defined in the parent shell as empty or malformed string, and the for-loop unset failed silently. Bash session state persists between Bash tool calls in this harness.
3. **First-iteration race / pipe failure on stdin**: sed -i sometimes has issues if stdin is closed or already consumed; first iteration getting bad-fd → looks like `$f` not expanding.

## Why this matters

The agent's reflex was workaround. Per operator: **register and find the source**. The workaround (writing /tmp/<script>.sh) succeeds but masks the underlying bug. If the bug is in the harness or hook layer, every future agent run hits it again.

## Action

1. **Registered** in this finding (this file).
2. **Source not reproduced** despite controlled retests. Awaits next occurrence with full context.
3. **On next occurrence**: capture the failing command's exact characters (including any invisible chars), the parent-shell state (`set | head`), and the hook outputs (cat /root/.claude/hooks/malware-deny.log + /opt/.../.claude/hooks/ logs).
4. **Lesson distillation**: the meta-pattern (agent reaches for workaround when source is non-obvious) is captured in:
   - `verbal-acknowledgment-is-not-a-fix-bug-fix-requires-structural-artefact.md` (tangent: workarounds are not structural fixes)
   - `agent-bug-fix-flow-must-be-mechanical-log-analyze-identify-fix-verify-confirm.md` (the sequence forbids skipping FIX-AT-SOURCE)

## Cross-references

- Related operator directive (current session): "register and find the source and we fix.. we dont just work around"
- Related lesson: agent-bug-fix-flow-must-be-mechanical (the sequence's IDENTIFY step is "list source files to fix" — workaround skips this)
- Related lesson: verbal-acknowledgment-is-not-a-fix (workarounds are verbal-acknowledgment-equivalents — they make the symptom go away without fixing the source)
