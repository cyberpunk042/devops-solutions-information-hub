#!/usr/bin/env python3
# Stop hook — emit end-of-cycle status stamp via systemMessage for the
# second-brain project, wherever it lives on disk. Adapted from the parallel
# root-modules hook pattern (see /root/.claude/hooks/end-of-cycle-stamp.sh)
# to second-brain's data model (no tools.cycle/state — uses gateway/stats/
# file-scan instead).
#
# Operator directive 2026-05-05: "we could have our stamp here too. adapted
# to us... like with hooks. some commons and some of our own and we keep
# evolving them and all".
#
# Operator directive 2026-05-06 (verbatim): "we are coming from another
# system that the second-brain is inside /opt... we should just support it..
# we have a relative / flexible strategy.. we need to fix this now. usualy
# there is the $HOME variable for example." — PROJECT_ROOT now resolves from
# CLAUDE_PROJECT_DIR env (Claude Code's canonical project-root variable),
# falling back to $HOME/devops-solutions-information-hub. NEVER hardcoded
# absolute paths (operator directive 2026-05-16: "THERE IS NO SUCH THING AS
# AN ABSOLUTE PATH IN SOFTWARE PROGRAMMING... ITS ALWAYS FUCKING $home").
#
# Self-gates via {PROJECT_ROOT}/CLAUDE.md presence + cwd/CLAUDE_PROJECT_DIR
# check so this fires only for second-brain sessions, not sister-project
# sessions on the same host.

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

PROJECT_ROOT = Path(
    os.environ.get("CLAUDE_PROJECT_DIR")
    or str(Path.home() / "devops-solutions-information-hub")
)
TRACE_LOG = "/tmp/hook-fire-trace.log"

# Operator stamp preference — shared across all root-user sessions via
# Path.home()/.claude/stamp-config.json (matches /root/tools/stamp.py
# CONFIG_PATH). Schema: {layout: horizontal|vertical, enabled: on|off|auto}.
# Defaults: layout=vertical, enabled=auto (mode-conditional; this project has
# no active-mode mechanism so auto = on).
STAMP_CONFIG_PATH = Path.home() / ".claude" / "stamp-config.json"
STAMP_DEFAULTS = {"layout": "vertical", "enabled": "auto"}


def _load_stamp_config() -> dict:
    cfg = dict(STAMP_DEFAULTS)
    try:
        if STAMP_CONFIG_PATH.exists():
            data = json.loads(STAMP_CONFIG_PATH.read_text())
            if isinstance(data, dict):
                if data.get("layout") in ("horizontal", "vertical"):
                    cfg["layout"] = data["layout"]
                if data.get("enabled") in ("on", "off", "auto"):
                    cfg["enabled"] = data["enabled"]
    except Exception:
        pass
    return cfg


def _trace(tag: str, extra: str = "") -> None:
    try:
        with open(TRACE_LOG, "a") as f:
            f.write(
                f"[{time.strftime('%Y-%m-%dT%H:%M:%S')}] hook=opt-end-of-cycle-stamp.sh "
                f"path={tag} cwd={os.getcwd()} home={os.environ.get('HOME', '')} "
                f"claude_proj={os.environ.get('CLAUDE_PROJECT_DIR', '<unset>')} {extra}\n"
            )
    except Exception:
        pass


def _is_project_context() -> bool:
    """Fire only for second-brain sessions (matches PROJECT_ROOT)."""
    project_dir = os.environ.get("CLAUDE_PROJECT_DIR", "").strip().rstrip("/")
    target = str(PROJECT_ROOT).rstrip("/")
    if project_dir:
        return project_dir == target or project_dir.startswith(target + "/")
    cwd = os.getcwd().rstrip("/")
    return cwd == target or cwd.startswith(target + "/")


def _count_files(glob_pattern: str) -> int:
    try:
        return sum(1 for _ in PROJECT_ROOT.glob(glob_pattern))
    except Exception:
        return 0


def _smart_trim(text: str, max_len: int) -> str:
    """Trim to max_len at last word boundary; no orphan trailing punctuation."""
    if len(text) <= max_len:
        return text
    cut = text[:max_len]
    # Walk back to last word boundary
    if " " in cut or "-" in cut or "_" in cut:
        # Prefer space, then dash, then underscore
        for sep in (" ", "-", "_"):
            i = cut.rfind(sep)
            if i > max_len // 2:
                return cut[:i].rstrip("- _") + "…"
    return cut.rstrip("- _") + "…"


def _recent_notes(n: int = 5) -> list[tuple[str, str]]:
    """Return list of (date, slug) tuples for the n most-recent raw/notes/."""
    notes_dir = PROJECT_ROOT / "raw" / "notes"
    try:
        files = sorted(notes_dir.glob("*.md"), key=lambda p: p.stat().st_mtime, reverse=True)[:n]
        out = []
        for p in files:
            stem = p.stem
            m = re.match(r"^(\d{4}-\d{2}-\d{2})-(.+)$", stem)
            if m:
                out.append((m.group(1), m.group(2)))
            else:
                out.append(("", stem))
        return out
    except Exception:
        return []


def _count_open_decisions() -> int:
    """Count open Q-decisions in operator-decision-queue.md (rows without
    ~~strike~~ markers)."""
    queue = PROJECT_ROOT / "wiki" / "backlog" / "operator-decision-queue.md"
    try:
        text = queue.read_text()
        # Match rows starting with `| <number-or-range> | ` (not ~~strike~~)
        return len(re.findall(r"^\| [0-9][0-9-]* \| ", text, re.MULTILINE))
    except Exception:
        return 0


def _count_research_gaps() -> int:
    gaps = PROJECT_ROOT / "wiki" / "backlog" / "research-gaps.md"
    try:
        text = gaps.read_text()
        # Heuristic: count "## " section headers (each gap typically has one)
        return len(re.findall(r"^## ", text, re.MULTILINE))
    except Exception:
        return 0


def _epic_state() -> tuple[int, int, int]:
    """Return (active, draft, in-progress) epic counts from _index.md."""
    idx = PROJECT_ROOT / "wiki" / "backlog" / "_index.md"
    try:
        text = idx.read_text()
        # Format: `| <id> | <link> | <prio> | <status> | <readiness> |`
        active = sum(1 for _ in re.finditer(r"\| active \|", text))
        draft = sum(1 for _ in re.finditer(r"\| draft \|", text))
        inprog = sum(1 for _ in re.finditer(r"\| in-progress \|", text))
        return (active, draft, inprog)
    except Exception:
        return (0, 0, 0)


def _phase() -> str:
    """Read 'Phase' value from CONTEXT.md table."""
    ctx = PROJECT_ROOT / "CONTEXT.md"
    try:
        text = ctx.read_text()
        m = re.search(r"\|\s*\*\*Phase\*\*\s*\|\s*([^|]+?)\s*\|", text)
        return m.group(1).strip() if m else "unknown"
    except Exception:
        return "unknown"


def _count_lessons() -> tuple[int, int, int]:
    """Return (drafts, validated, candidates) lesson counts."""
    base = PROJECT_ROOT / "wiki" / "lessons"
    try:
        drafts = sum(1 for _ in (base / "01_drafts").glob("*.md")) if (base / "01_drafts").exists() else 0
        validated = sum(1 for _ in (base / "03_validated").glob("**/*.md")) if (base / "03_validated").exists() else 0
        candidates = sum(1 for _ in (base / "02_candidates").glob("*.md")) if (base / "02_candidates").exists() else 0
        return (drafts, candidates, validated)
    except Exception:
        return (0, 0, 0)


def _module_state() -> tuple[int, int, int]:
    """Return (active, draft, in-progress) module counts via _index.md scan."""
    idx = PROJECT_ROOT / "wiki" / "backlog" / "modules" / "_index.md"
    try:
        text = idx.read_text()
        active = sum(1 for _ in re.finditer(r"\| active \|", text))
        draft = sum(1 for _ in re.finditer(r"\| draft \|", text))
        inprog = sum(1 for _ in re.finditer(r"\| in-progress \|", text))
        return (active, draft, inprog)
    except Exception:
        return (0, 0, 0)


def _task_state() -> tuple[int, int, int, int]:
    """Return (done, in-progress, draft, blocked) task counts."""
    tasks_dir = PROJECT_ROOT / "wiki" / "backlog" / "tasks"
    if not tasks_dir.exists():
        return (0, 0, 0, 0)
    done = inprog = draft = blocked = 0
    try:
        for f in tasks_dir.glob("T*.md"):
            try:
                head = f.read_text()[:1024]
                m = re.search(r"^status:\s*(\S+)", head, re.MULTILINE)
                if not m:
                    continue
                s = m.group(1).lower()
                if s == "done":
                    done += 1
                elif s in ("in-progress", "active"):
                    inprog += 1
                elif s == "draft":
                    draft += 1
                elif s == "blocked":
                    blocked += 1
            except Exception:
                continue
    except Exception:
        pass
    return (done, inprog, draft, blocked)


def build_stamp_horizontal() -> str:
    """Horizontal layout matching /root/tools/cycle.py emit_status_block_ansi_horizontal:
    6 single-line-per-section rows with glyph + padded label + grouped fields.
    Separator conventions: ` · ` within logical group, `║` between groups.
    Per SB-114 sub-req (a) + SB-116 UX iteration. Adapted to this project's
    data model (pages/epics/modules/tasks/lessons/notes/decisions/gaps; no
    tools.cycle).
    """
    pages = _count_files("wiki/**/*.md")
    notes = _recent_notes(5)
    open_decisions = _count_open_decisions()
    research_gaps = _count_research_gaps()
    epic_active, epic_draft, epic_inprog = _epic_state()
    epic_total = epic_active + epic_draft + epic_inprog
    mod_active, mod_draft, mod_inprog = _module_state()
    mod_total = mod_active + mod_draft + mod_inprog
    t_done, t_inprog, t_draft, t_blocked = _task_state()
    t_total = t_done + t_inprog + t_draft + t_blocked
    lesson_drafts, _lesson_candidates, lesson_validated = _count_lessons()
    phase = _phase()

    R = "\033[31m"; G = "\033[32m"; Y = "\033[33m"; B = "\033[34m"
    M = "\033[35m"; K = "\033[36m"; BO = "\033[1m"; D = "\033[2m"; X = "\033[0m"
    ts = time.strftime("%H:%M:%S")

    LABEL_WIDTH = 8  # widest = "Progress" (matches /root pattern)
    GLYPHS = {
        "Status":   "●",
        "Journey":  "↺",
        "Plan":     "◆",
        "Blocked":  "⊘",
        "Progress": "▰",
        "Cursor":   "▶",
    }
    def lbl(name: str) -> str:
        glyph = GLYPHS.get(name, "·")
        return f"{M}{BO}{glyph} {name:<{LABEL_WIDTH}}{X}"

    L = ["```ansi"]

    # Status — timestamp · type · phase
    L.append(f"{lbl('Status')}  {D}{ts}{X}  ·  type=second-brain  ·  {G}phase={phase}{X}")

    # Journey — top 3 recent raw/notes/ slugs, smart-trimmed
    journey_slugs = []
    for date, slug in notes[:3]:
        journey_slugs.append(_smart_trim(slug, 35))
    journey_line = f"{D}" + "  ·  ".join(journey_slugs) + f"{X}" if journey_slugs else f"{D}(none){X}"
    L.append(f"{lbl('Journey')}  {journey_line}")

    # Plan — pages + epics counts ║ epic state breakdown
    L.append(
        f"{lbl('Plan')}  {Y}pages {pages}{X}  ·  {Y}epics {epic_total}{X}  ·  {Y}modules {mod_total}{X}  "
        f"{D}║{X}  {D}({epic_active} active · {epic_inprog} in-progress · {epic_draft} draft){X}"
    )

    # Blocked — operator decisions ║ research gaps · blocked tasks
    def _flag(n: int, label: str, color: str) -> str:
        return f"{G}0 {label}{X}" if n == 0 else f"{color}{n} {label}{X}"
    L.append(
        f"{lbl('Blocked')}  {_flag(open_decisions, 'open decisions', R)}  "
        f"{D}║{X}  {_flag(research_gaps, 'research gaps', Y)}  ·  {_flag(t_blocked, 'blocked tasks', R)}"
    )

    # Progress — lessons + tasks done/total ║ task breakdown
    L.append(
        f"{lbl('Progress')}  {B}lessons{X}  {G}validated={lesson_validated}{X}  ·  {Y}drafts={lesson_drafts}{X}  "
        f"{D}║{X}  {G}tasks {t_done}/{t_total}{X}  {D}({t_inprog} in-progress · {t_draft} draft · {t_blocked} blocked){X}"
    )

    # Cursor — most recent activity + reference paths
    if notes:
        latest = _smart_trim(notes[0][1], 50)
        L.append(f"{lbl('Cursor')}  {Y}↪{X} {latest}  {D}· raw/notes/ + wiki/backlog/{X}")
    else:
        L.append(f"{lbl('Cursor')}  {D}(no recent activity){X}")

    L.append("```")
    return "\n".join(L)


def build_stamp() -> str:
    # Gather all data once
    pages = _count_files("wiki/**/*.md")
    notes = _recent_notes(5)
    open_decisions = _count_open_decisions()
    research_gaps = _count_research_gaps()
    epic_active, epic_draft, epic_inprog = _epic_state()
    epic_total = epic_active + epic_draft + epic_inprog
    mod_active, mod_draft, mod_inprog = _module_state()
    mod_total = mod_active + mod_draft + mod_inprog
    t_done, t_inprog, t_draft, t_blocked = _task_state()
    t_total = t_done + t_inprog + t_draft + t_blocked
    lesson_drafts, lesson_candidates, lesson_validated = _count_lessons()
    phase = _phase()

    # ```ansi fenced block — full color palette (red/green/yellow/blue/magenta/
    # cyan/dim/bold). Operator-verified to render in Claude Code chat per
    # /root pattern (see /root/tools/cycle.py emit_status_block_ansi).
    R = "\033[31m"; G = "\033[32m"; Y = "\033[33m"; B = "\033[34m"
    M = "\033[35m"; K = "\033[36m"; BO = "\033[1m"; D = "\033[2m"; X = "\033[0m"
    bar = "═" * 63
    ts = time.strftime("%H:%M:%S")

    L = []  # accumulated lines
    L.append("```ansi")
    L.append(f"{D}{bar}{X}")
    L.append(f"{BO}{K}SECOND-BRAIN · STATUS · {ts} · type=system · phase={phase}{X}")
    L.append(f"{D}{bar}{X}")
    L.append("")
    L.append(f"{G}LOOP   alive{X}    {BO}PAGES   {pages}{X}    {BO}EPICS   {epic_total}{X}    {BO}MODELS   16{X}")
    L.append("")
    L.append(f"{M}{BO}@@ JOURNEY (recent raw/notes/) @@{X}")
    if notes:
        for date, slug in notes:
            slug_short = _smart_trim(slug, 56)
            date_part = f"{D}{date}{X}  " if date else ""
            L.append(f"{D}·{X} {date_part}{slug_short}")
    else:
        L.append(f"{D}· (none){X}")
    L.append("")
    L.append(f"{M}{BO}@@ BACKLOG @@{X}")
    L.append(f"{G}epics    {epic_total:>3}{X}    {D}({epic_active} active · {epic_inprog} in-progress · {epic_draft} draft){X}")
    L.append(f"{G}modules  {mod_total:>3}{X}    {D}({mod_active} active · {mod_inprog} in-progress · {mod_draft} draft){X}")
    L.append(f"{G}tasks    {t_total:>3}{X}    {D}({t_done} done · {t_inprog} in-progress · {t_draft} draft · {t_blocked} blocked){X}")
    L.append("")
    L.append(f"{M}{BO}@@ KNOWLEDGE EVOLUTION @@{X}")
    L.append(f"{B}lessons{X}  {G}validated={lesson_validated}{X}  {Y}candidates={lesson_candidates}{X}  {D}drafts={lesson_drafts}{X}")
    L.append("")
    L.append(f"{M}{BO}@@ ⊘ BLOCKED · ATTENTION @@{X}")
    if open_decisions > 0:
        L.append(f"{R}{open_decisions} open operator decisions{X}    {D}(wiki/backlog/operator-decision-queue.md){X}")
    else:
        L.append(f"{G}0 open operator decisions{X}")
    if research_gaps > 0:
        L.append(f"{Y}{research_gaps} research gaps{X}    {D}(wiki/backlog/research-gaps.md){X}")
    else:
        L.append(f"{G}0 research gaps{X}")
    if t_blocked > 0:
        L.append(f"{R}{t_blocked} blocked tasks{X}")
    L.append("")
    L.append(f"{G}{BO}✓ PROGRESS{X} · pages={pages} · epics={epic_total} · modules={mod_total} · tasks={t_total}")
    L.append(f"{G}            lessons validated={lesson_validated} · drafts={lesson_drafts}{X}")
    L.append("")
    L.append(f"{M}{BO}@@ → CURSOR · NEXT @@{X}")
    if notes:
        L.append(f"{Y}recent activity:{X}  {_smart_trim(notes[0][1], 56)}")
    if open_decisions > 0 or research_gaps > 0:
        attention = []
        if open_decisions > 0:
            attention.append(f"{R}{open_decisions} decision(s){X}")
        if research_gaps > 0:
            attention.append(f"{Y}{research_gaps} research gap(s){X}")
        L.append(f"{BO}needs attention:{X} {' · '.join(attention)}")
    L.append(f"{B}parallel branches:{X}  {D}wiki/backlog/{{epics,modules,tasks}}/ · raw/notes/ · wiki/lessons/{X}")
    L.append(f"{D}{bar}{X}")
    L.append("```")
    return "\n".join(L)


def main() -> None:
    _trace("entered")

    # Drain stdin (avoid SIGPIPE on parent)
    try:
        sys.stdin.read()
    except Exception:
        pass

    if not (PROJECT_ROOT / "CLAUDE.md").exists():
        _trace("exit-claude-md-missing")
        sys.exit(0)

    if not _is_project_context():
        _trace("exit-suppress-on-mismatch")
        sys.exit(0)

    # Route per shared stamp-config (Path.home()/.claude/stamp-config.json,
    # written by /root/tools/stamp.py via /stamp-* slash commands).
    cfg = _load_stamp_config()
    if cfg["enabled"] == "off":
        _trace("exit-disabled-by-config")
        sys.exit(0)

    # enabled=auto → mode-conditional (SB-114 sub-req c: default-hide-when-no-mode).
    # Active-mode is PER-PROJECT state (each project has its own mode files).
    # This project's active-mode lives at {PROJECT_ROOT}/.claude/active-mode
    # (project-local), NOT at Path.home()/.claude/active-mode (which is /root's
    # mode for the /root project). Stamp-config is shared (operator-preference)
    # but active-mode is per-project (project-state).
    if cfg["enabled"] == "auto":
        active_mode = ""
        try:
            mode_file = PROJECT_ROOT / ".claude" / "active-mode"
            if mode_file.exists():
                active_mode = mode_file.read_text().strip()
        except Exception:
            pass
        if not active_mode:
            _trace("exit-auto-no-mode")
            sys.exit(0)
    # enabled=on falls through to render unconditionally.

    layout = cfg["layout"]
    try:
        if layout == "horizontal":
            stamp = build_stamp_horizontal()
        else:
            stamp = build_stamp()
    except Exception as exc:
        _trace("exit-build-error", f"err={exc!r} layout={layout}")
        sys.exit(0)

    if not stamp.strip():
        _trace("exit-empty-stamp")
        sys.exit(0)

    print(json.dumps({"systemMessage": stamp}))
    _trace("fired-systemMessage", f"stamp_len={len(stamp)} layout={layout}")
    sys.exit(0)


if __name__ == "__main__":
    main()
