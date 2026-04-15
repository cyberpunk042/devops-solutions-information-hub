"""Timeline — computed cross-project temporal view.

Computes an event timeline on demand from existing data across projects.
No stored artifact; no manual digest. Each invocation reads source of truth.

Scope model:
    self          = invoking project (resolved via --wiki-root)
    brain         = declared second-brain (resolved via --brain)
    all           = every project in the brain's sister-projects registry
    <name>        = explicit project name from the registry
    --scope is comma-separated; composes freely; duplicates collapse.

Default scope differs by caller:
    from brain  -> self (just the wiki)
    from sister -> self,brain (sister + backup config source)

Event sources per project:
    commit          : git log within the project root
    lesson/pattern/... : wiki/**/*.md frontmatter (created, updated)
    epic / task     : wiki/backlog/**/*.md frontmatter + stage transitions
    directive       : raw/notes/YYYY-MM-DD-*.md (filename date + frontmatter)
    session/handoff : docs/SESSION-*.md (wiki) or log/YYYY-MM-DD-*.md (sisters)

See: raw/notes/2026-04-15-directive-timeline-computed-gateway.md
"""

from __future__ import annotations

import json
import re
import subprocess
from dataclasses import dataclass, field, asdict
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Set, Tuple

from tools.common import (
    parse_frontmatter,
    find_wiki_pages,
    get_project_root,
)

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None  # type: ignore


# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------

EVENT_TYPES = {
    "commit",
    "lesson",
    "pattern",
    "decision",
    "synthesis",
    "source-synthesis",
    "concept",
    "deep-dive",
    "comparison",
    "reference",
    "principle",
    "model",
    "standards",
    "epic",
    "module",
    "task",
    "milestone",
    "directive",
    "note",
    "session",
    "handoff",
}

# Wiki page types that correspond 1:1 to timeline event types.
PAGE_TYPE_TO_EVENT: Dict[str, str] = {
    "lesson": "lesson",
    "pattern": "pattern",
    "decision": "decision",
    "source-synthesis": "synthesis",
    "concept": "concept",
    "deep-dive": "deep-dive",
    "comparison": "comparison",
    "reference": "reference",
    "principle": "principle",
    "standards": "standards",
    "epic": "epic",
    "module": "module",
    "task": "task",
    "milestone": "milestone",
    "note": "note",
}


@dataclass
class TimelineEvent:
    date: datetime
    project: str
    type: str
    title: str
    path: str
    subject: List[str] = field(default_factory=list)   # tags or derived subject words
    signal: Optional[str] = None                       # derived: "promoted-to-drafts", "readiness:45→70"
    threads_to: List[str] = field(default_factory=list)  # cross-project links (project:path)
    body_preview: Optional[str] = None                 # first ~240 chars of content
    full_content: Optional[str] = None                 # populated only when --full-content
    commit_sha: Optional[str] = None                   # for commit events
    author: Optional[str] = None                       # for commit events
    # Phase 4: cross-project arc links — populated after all events gathered.
    # Each string describes an event in the timeline that this one threads to:
    # format "YYYY-MM-DD · project · type · title".
    linked_events: List[str] = field(default_factory=list)
    # Phase 5: parent epic for task/module events (from frontmatter `epic:` field).
    # Enables --group-by epic + inline [EXXX] annotation.
    parent_epic: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        d["date"] = self.date.isoformat()
        return d


# ---------------------------------------------------------------------------
# Registry + scope resolution
# ---------------------------------------------------------------------------

@dataclass
class ProjectTarget:
    """One project the timeline will walk. Resolved from scope spec.

    `local_available` indicates whether the project root exists on the local
    filesystem. When False, callers must opt into remote fetch via `--remote`
    (slower — uses gh api) or omit the project from scope.
    """
    name: str            # canonical name (e.g., 'research-wiki', 'openarms')
    root: Path           # project root on local filesystem
    layout: Dict[str, Any]  # paths to walk (backlog, logs, domains, etc.)
    wiki_dir: Optional[str] = None  # subdirectory containing wiki pages, if any
    is_brain: bool = False
    local_available: bool = True  # False if project declared but not locally cloned
    remote: Optional[Dict[str, Any]] = None  # remote block from registry (owner/repo/branch)


def load_registry(brain_root: Path) -> Dict[str, Any]:
    """Load the sister-projects registry from the brain."""
    if yaml is None:
        return {}
    path = brain_root / "wiki" / "config" / "sister-projects.yaml"
    if not path.exists():
        return {}
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def _resolve_project_path(raw_path: str) -> Path:
    """Expand ~/ and resolve. Matches source_resolver.py behavior."""
    return Path(raw_path).expanduser().resolve()


def resolve_scope(
    scope_list: List[str],
    wiki_root: Path,
    brain_root: Path,
    registry: Dict[str, Any],
) -> List[ProjectTarget]:
    """Turn a scope list like ['self', 'brain', 'openarms'] into ProjectTargets.

    Magic names:
        self  -> ProjectTarget rooted at wiki_root
        brain -> ProjectTarget rooted at brain_root (with brain's layout)
        all   -> every project in registry (including the brain itself under its registered key)
    Explicit names resolve via registry lookup (name or alias).
    Dedup by resolved root path.
    """
    targets: List[ProjectTarget] = []
    seen_roots: Set[str] = set()

    def _add(target: Optional[ProjectTarget]) -> None:
        if target is None:
            return
        key = str(target.root)
        if key in seen_roots:
            return
        seen_roots.add(key)
        targets.append(target)

    projects_cfg = registry.get("projects", {}) or {}

    # Figure out which registry entry (if any) IS the brain, so 'self' from the
    # brain gets that project's layout rather than an empty one.
    brain_root_resolved = brain_root.resolve()
    brain_registry_name: Optional[str] = None
    brain_registry_cfg: Optional[Dict[str, Any]] = None
    for name, cfg in projects_cfg.items():
        raw_path = cfg.get("path")
        if not raw_path:
            continue
        try:
            if _resolve_project_path(raw_path) == brain_root_resolved:
                brain_registry_name = name
                brain_registry_cfg = cfg
                break
        except Exception:
            continue

    # The brain itself may not be in its own sister-projects.yaml (it usually isn't —
    # sister-projects.yaml lists OTHERS). Fall back to a self-described target.
    def _brain_target() -> ProjectTarget:
        if brain_registry_cfg is not None:
            return ProjectTarget(
                name=brain_registry_name or "research-wiki",
                root=brain_root_resolved,
                layout=brain_registry_cfg.get("layout", {}) or {},
                wiki_dir=brain_registry_cfg.get("wiki_dir"),
                is_brain=True,
            )
        # The brain is the research-wiki — hardcode the layout we know.
        return ProjectTarget(
            name="research-wiki",
            root=brain_root_resolved,
            layout={
                "backlog": {"epics": "backlog/epics", "tasks": "backlog/tasks", "milestones": "backlog/milestones"},
                "lessons": "lessons",
                "patterns": "patterns",
                "decisions": "decisions",
                "sources": "sources",
                "domains": "domains",
                "spine": "spine",
                "log": "log",
            },
            wiki_dir="wiki",
            is_brain=True,
        )

    def _self_target() -> ProjectTarget:
        wiki_root_resolved = wiki_root.resolve()
        # If self IS the brain, use brain's layout.
        if wiki_root_resolved == brain_root_resolved:
            return _brain_target()
        # Otherwise, look up self in the registry by path match.
        for name, cfg in projects_cfg.items():
            try:
                if _resolve_project_path(cfg.get("path", "")) == wiki_root_resolved:
                    return ProjectTarget(
                        name=name,
                        root=wiki_root_resolved,
                        layout=cfg.get("layout", {}) or {},
                        wiki_dir=cfg.get("wiki_dir"),
                    )
            except Exception:
                continue
        # Not in registry — minimal self target.
        return ProjectTarget(
            name=wiki_root_resolved.name,
            root=wiki_root_resolved,
            layout={},
            wiki_dir=None,
        )

    def _named_target(name: str) -> Optional[ProjectTarget]:
        # Direct key match
        cfg = projects_cfg.get(name)
        # Alias match
        if cfg is None:
            for n, c in projects_cfg.items():
                aliases = c.get("aliases", []) or []
                if name in aliases:
                    cfg = c
                    break
        if cfg is None:
            return None
        raw_path = cfg.get("path")
        if not raw_path:
            return None
        try:
            root = _resolve_project_path(raw_path)
        except Exception:
            return None
        local_available = root.exists()
        return ProjectTarget(
            name=name,
            root=root,
            layout=cfg.get("layout", {}) or {},
            wiki_dir=cfg.get("wiki_dir"),
            is_brain=(root == brain_root_resolved) if local_available else False,
            local_available=local_available,
            remote=cfg.get("remote"),
        )

    for raw in scope_list:
        token = raw.strip().lower()
        if not token:
            continue
        if token == "self":
            _add(_self_target())
        elif token == "brain":
            _add(_brain_target())
        elif token == "all":
            _add(_brain_target())
            for name in projects_cfg.keys():
                t = _named_target(name)
                if t is not None:
                    _add(t)
        else:
            t = _named_target(raw.strip())  # preserve case for registry lookup
            if t is None:
                # Try lowercase too
                t = _named_target(token)
            if t is not None:
                _add(t)

    return targets


# ---------------------------------------------------------------------------
# Since / until parsing
# ---------------------------------------------------------------------------

_DURATION_RE = re.compile(r"^(\d+)([hdwmy])$", re.IGNORECASE)
_ISO_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}(T\d{2}:\d{2}(:\d{2})?)?$")


def parse_when(value: str, now: Optional[datetime] = None) -> datetime:
    """Parse '7d', '24h', '2w', '2026-04-01', '2026-04-01T12:00:00' → datetime (UTC)."""
    if now is None:
        now = datetime.now(timezone.utc)
    if not value:
        return now
    s = value.strip()
    # Relative duration
    m = _DURATION_RE.match(s)
    if m:
        n = int(m.group(1))
        unit = m.group(2).lower()
        delta_map = {
            "h": timedelta(hours=n),
            "d": timedelta(days=n),
            "w": timedelta(weeks=n),
            "m": timedelta(days=n * 30),     # approximate
            "y": timedelta(days=n * 365),    # approximate
        }
        return now - delta_map[unit]
    # ISO date / datetime
    if _ISO_DATE_RE.match(s):
        if "T" in s:
            return datetime.fromisoformat(s).replace(tzinfo=timezone.utc) if "+" not in s and "Z" not in s else datetime.fromisoformat(s.replace("Z", "+00:00"))
        return datetime.fromisoformat(s).replace(tzinfo=timezone.utc)
    # Fallback: try fromisoformat anyway
    try:
        return datetime.fromisoformat(s).replace(tzinfo=timezone.utc)
    except Exception:
        return now


# ---------------------------------------------------------------------------
# Event extractors
# ---------------------------------------------------------------------------

def _git_log(project_root: Path, since: datetime, until: datetime) -> List[Tuple[str, datetime, str, str]]:
    """Run git log; return list of (sha, date, author, subject)."""
    if not (project_root / ".git").exists():
        return []
    since_iso = since.isoformat()
    until_iso = until.isoformat()
    try:
        result = subprocess.run(
            [
                "git", "-C", str(project_root), "log",
                f"--since={since_iso}",
                f"--until={until_iso}",
                "--pretty=format:%H|%ct|%an|%s",
            ],
            capture_output=True, text=True, timeout=30,
        )
    except (subprocess.TimeoutExpired, OSError):
        return []
    if result.returncode != 0:
        return []
    out: List[Tuple[str, datetime, str, str]] = []
    for line in result.stdout.splitlines():
        parts = line.split("|", 3)
        if len(parts) != 4:
            continue
        sha, ts, author, subject = parts
        try:
            dt = datetime.fromtimestamp(int(ts), tz=timezone.utc)
        except Exception:
            continue
        out.append((sha, dt, author, subject))
    return out


def extract_commits(target: ProjectTarget, since: datetime, until: datetime,
                    full_content: bool) -> List[TimelineEvent]:
    """Commits in date range."""
    events: List[TimelineEvent] = []
    for sha, dt, author, subject in _git_log(target.root, since, until):
        events.append(TimelineEvent(
            date=dt,
            project=target.name,
            type="commit",
            title=subject[:140],
            path="",
            subject=[],
            signal=None,
            commit_sha=sha,
            author=author,
            body_preview=None,
            full_content=None,
        ))
    return events


_DATE_PREFIX_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})-(.+?)\.md$")


def _read_page_safely(path: Path) -> Tuple[Dict[str, Any], str]:
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return {}, ""
    return parse_frontmatter(text)


def _page_title(meta: Dict[str, Any], path: Path) -> str:
    t = meta.get("title", "")
    if isinstance(t, str) and t.strip():
        return t.strip()
    return path.stem


def _make_preview(body: str, n: int = 240) -> str:
    # Strip code fences and HTML-ish, compress whitespace.
    cleaned = re.sub(r"```[\s\S]*?```", "", body)
    cleaned = re.sub(r"<[^>]+>", "", cleaned)
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    if len(cleaned) <= n:
        return cleaned
    return cleaned[:n].rstrip() + "…"


def _parse_date_field(v: Any) -> Optional[datetime]:
    if v is None:
        return None
    s = str(v).strip()
    if not s:
        return None
    try:
        if "T" in s:
            return datetime.fromisoformat(s.replace("Z", "+00:00"))
        d = datetime.fromisoformat(s)
        return d.replace(tzinfo=timezone.utc) if d.tzinfo is None else d
    except Exception:
        return None


def _derive_signal(meta: Dict[str, Any], path: Path) -> Optional[str]:
    """Derive a short signal string from frontmatter (e.g., promotion tier, maturity)."""
    signals: List[str] = []
    # Detect maturity tier from path
    p = str(path).lower()
    if "/00_inbox/" in p:
        signals.append("inbox")
    elif "/01_drafts/" in p:
        signals.append("draft")
    elif "/02_synthesized/" in p or "/02_validated/" in p:
        signals.append(p.split("/02_")[1].split("/")[0])  # synthesized or validated
    elif "/03_validated/" in p or "/03_principles/" in p:
        signals.append(p.split("/03_")[1].split("/")[0])
    elif "/04_principles/" in p:
        signals.append("principle")
    maturity = meta.get("maturity")
    if isinstance(maturity, str) and maturity.strip():
        signals.append(f"maturity:{maturity}")
    readiness = meta.get("readiness")
    if readiness is not None:
        signals.append(f"readiness:{readiness}")
    status = meta.get("status")
    if isinstance(status, str) and status.strip() and status not in ("synthesized",):
        signals.append(f"status:{status}")
    return " | ".join(signals) if signals else None


def _extract_threads_to(meta: Dict[str, Any]) -> List[str]:
    """Find cross-project source references (project+path form)."""
    out: List[str] = []
    for src in meta.get("sources", []) or []:
        if not isinstance(src, dict):
            continue
        project = src.get("project")
        path = src.get("path")
        if project and path:
            out.append(f"{project}:{path}")
    return out


def _iter_layout_md_files(target: ProjectTarget) -> Iterable[Path]:
    """Yield .md files from all declared layout paths for the target.

    Layouts can be flat (key -> str path) or nested dicts (key -> {sub: path}).
    Paths resolve under wiki_dir if set, otherwise under the project root.
    """
    seen: Set[Path] = set()
    base = target.root
    if target.wiki_dir:
        base = base / target.wiki_dir

    def _resolve_layout_path(rel: str) -> Path:
        rel_s = rel.strip()
        if rel_s.startswith("../"):
            # wiki_dir-relative; step up via wiki_dir base
            return (base / rel_s).resolve()
        return (base / rel_s).resolve()

    def _walk(d: Any) -> None:
        if isinstance(d, dict):
            for v in d.values():
                _walk(v)
        elif isinstance(d, str):
            root_path = _resolve_layout_path(d)
            if not root_path.exists():
                return
            if root_path.is_file() and root_path.suffix == ".md":
                if root_path not in seen:
                    seen.add(root_path)
                    # Will be yielded by outer loop — but this path is one file
                    return
            if root_path.is_dir():
                for p in root_path.rglob("*.md"):
                    if p not in seen:
                        seen.add(p)

    _walk(target.layout)

    # Also walk the wiki_dir itself for concept/lesson/pattern/decision/source pages
    # that aren't under explicitly-declared layout keys. (Our own wiki has
    # domains/, sources/, lessons/, patterns/, decisions/ whereas sister layouts
    # only explicitly list some.) Be bounded — only go one level down from the
    # wiki_dir.
    if base.exists() and base.is_dir():
        for top in base.iterdir():
            if top.is_dir() and not top.name.startswith("."):
                for p in top.rglob("*.md"):
                    if p not in seen:
                        seen.add(p)

    for p in sorted(seen):
        yield p


def extract_frontmatter_events(target: ProjectTarget, since: datetime, until: datetime,
                                 types_filter: Set[str], full_content: bool) -> List[TimelineEvent]:
    """Walk wiki pages, emit events for created/updated dates in range."""
    events: List[TimelineEvent] = []
    for p in _iter_layout_md_files(target):
        try:
            if p.suffix != ".md":
                continue
            # Skip auto-generated index files from event stream
            if p.name == "_index.md" or p.name == "manifest.json":
                continue
            meta, body = _read_page_safely(p)
            if not meta:
                # No frontmatter — likely a raw dump or README. Skip.
                continue
            page_type = str(meta.get("type", "")).strip().lower()
            event_type = PAGE_TYPE_TO_EVENT.get(page_type, page_type or "page")

            # Type filter
            if types_filter and event_type not in types_filter:
                continue

            title = _page_title(meta, p)
            rel_path = str(p.relative_to(target.root))
            tags = meta.get("tags", []) or []
            subject = [t for t in tags if isinstance(t, str)][:6]
            signal = _derive_signal(meta, p)
            threads = _extract_threads_to(meta)
            preview = _make_preview(body) if body else None
            full = body if full_content else None
            # Phase 5: parent epic for task/module events
            raw_epic = meta.get("epic")
            parent_epic = str(raw_epic).strip() if raw_epic else None

            # Emit one event per distinct date (created and/or updated in range).
            created = _parse_date_field(meta.get("created"))
            updated = _parse_date_field(meta.get("updated"))

            # created in range
            if created and since <= created <= until:
                events.append(TimelineEvent(
                    date=created,
                    project=target.name,
                    type=event_type,
                    title=title,
                    path=rel_path,
                    subject=subject,
                    signal=(signal + " | created") if signal else "created",
                    threads_to=threads,
                    body_preview=preview,
                    full_content=full,
                    parent_epic=parent_epic,
                ))
            # updated in range (and distinct from created)
            if updated and since <= updated <= until:
                if not created or updated.date() != created.date():
                    events.append(TimelineEvent(
                        date=updated,
                        project=target.name,
                        type=event_type,
                        title=title,
                        path=rel_path,
                        subject=subject,
                        signal=(signal + " | updated") if signal else "updated",
                        threads_to=threads,
                        body_preview=preview,
                        full_content=full,
                        parent_epic=parent_epic,
                    ))
        except Exception:
            # Never break the timeline on one bad page.
            continue
    return events


def extract_dated_notes(target: ProjectTarget, since: datetime, until: datetime,
                         types_filter: Set[str], full_content: bool) -> List[TimelineEvent]:
    """Walk raw/notes/YYYY-MM-DD-*.md per project. Filename date is authoritative."""
    if types_filter and "directive" not in types_filter and "note" not in types_filter:
        return []
    events: List[TimelineEvent] = []
    candidates = [
        target.root / "raw" / "notes",
    ]
    for notes_dir in candidates:
        if not notes_dir.exists() or not notes_dir.is_dir():
            continue
        for p in sorted(notes_dir.glob("*.md")):
            m = _DATE_PREFIX_RE.match(p.name)
            if not m:
                continue
            try:
                dt = datetime.fromisoformat(m.group(1)).replace(tzinfo=timezone.utc)
            except Exception:
                continue
            if not (since <= dt <= until):
                continue
            meta, body = _read_page_safely(p)
            note_type = str(meta.get("note_type", "") or meta.get("type", "")).strip().lower()
            event_type = "directive" if note_type == "directive" else "note"
            if types_filter and event_type not in types_filter:
                continue
            title = _page_title(meta, p)
            tags = meta.get("tags", []) or []
            subject = [t for t in tags if isinstance(t, str)][:6]
            preview = _make_preview(body) if body else None
            full = body if full_content else None
            events.append(TimelineEvent(
                date=dt,
                project=target.name,
                type=event_type,
                title=title,
                path=str(p.relative_to(target.root)),
                subject=subject,
                signal=None,
                body_preview=preview,
                full_content=full,
            ))
    return events


def extract_session_logs(target: ProjectTarget, since: datetime, until: datetime,
                         types_filter: Set[str], full_content: bool) -> List[TimelineEvent]:
    """Walk session/handoff artifacts.

    Brain-side: docs/SESSION-*.md (not under wiki_dir; docs/ is a sibling of wiki/).
    Sister-side: the declared `logs` layout path (e.g., `log/` under wiki_dir, which for
    sisters typically resolves to <project>/wiki/log/). Sister projects also often keep
    `log/YYYY-MM-DD-*.md` at wiki_dir/log.
    """
    if types_filter and "session" not in types_filter and "handoff" not in types_filter:
        return []
    events: List[TimelineEvent] = []

    # Brain docs/SESSION-*.md
    docs_dir = target.root / "docs"
    if docs_dir.exists() and docs_dir.is_dir():
        for p in sorted(docs_dir.glob("SESSION-*.md")):
            stat = p.stat()
            dt = datetime.fromtimestamp(stat.st_mtime, tz=timezone.utc)
            # Prefer filename date if present
            m = re.match(r"^SESSION-(\d{4}-\d{2}-\d{2})", p.name)
            if m:
                try:
                    dt = datetime.fromisoformat(m.group(1)).replace(tzinfo=timezone.utc)
                except Exception:
                    pass
            if not (since <= dt <= until):
                continue
            meta, body = _read_page_safely(p)
            title = _page_title(meta, p) if meta else p.stem
            preview = _make_preview(body) if body else None
            full = body if full_content else None
            events.append(TimelineEvent(
                date=dt,
                project=target.name,
                type="handoff",
                title=title,
                path=str(p.relative_to(target.root)),
                body_preview=preview,
                full_content=full,
            ))

    # Sister log/ directory (declared via layout.logs in sister-projects.yaml).
    logs_rel = target.layout.get("logs") if isinstance(target.layout, dict) else None
    if isinstance(logs_rel, str):
        logs_base = target.root / (target.wiki_dir or "") / logs_rel
        if logs_base.exists() and logs_base.is_dir():
            for p in sorted(logs_base.rglob("*.md")):
                m = _DATE_PREFIX_RE.match(p.name)
                if not m:
                    continue
                try:
                    dt = datetime.fromisoformat(m.group(1)).replace(tzinfo=timezone.utc)
                except Exception:
                    continue
                if not (since <= dt <= until):
                    continue
                meta, body = _read_page_safely(p)
                note_type = str(meta.get("note_type", "") or meta.get("type", "")).strip().lower()
                event_type = "session" if note_type in ("session", "handoff", "completion") else "session"
                title = _page_title(meta, p) if meta else p.stem
                preview = _make_preview(body) if body else None
                full = body if full_content else None
                events.append(TimelineEvent(
                    date=dt,
                    project=target.name,
                    type=event_type,
                    title=title,
                    path=str(p.relative_to(target.root)),
                    body_preview=preview,
                    full_content=full,
                ))
    return events


# ---------------------------------------------------------------------------
# Backlog stage-transition deltas (Phase 2a)
# ---------------------------------------------------------------------------
#
# For each backlog file (epic/task/module/milestone) modified in range, diff
# tracked frontmatter fields between revisions and emit delta events.
# Tracked fields: readiness, stages_completed, status, current_stage, maturity,
# progress. Emits one event per (commit, file, field-change) tuple.

TRACKED_DELTA_FIELDS = [
    "readiness",
    "stages_completed",
    "status",
    "current_stage",
    "maturity",
    "progress",
]


def _git_show_file(project_root: Path, sha: str, file_path: str) -> Optional[str]:
    """Return file contents at a given commit. None if file didn't exist."""
    try:
        result = subprocess.run(
            ["git", "-C", str(project_root), "show", f"{sha}:{file_path}"],
            capture_output=True, text=True, timeout=10,
        )
    except (subprocess.TimeoutExpired, OSError):
        return None
    if result.returncode != 0:
        return None
    return result.stdout


def _git_commits_touching_paths(project_root: Path, since: datetime, until: datetime,
                                 path_patterns: List[str]) -> List[Tuple[str, datetime, List[str]]]:
    """Return commits in range that touched any of the given paths.

    Each element: (sha, commit_date, [files_changed_in_commit_matching_patterns]).
    Uses pathspec filtering so git only reports commits that actually touched
    those paths.
    """
    if not (project_root / ".git").exists():
        return []
    since_iso = since.isoformat()
    until_iso = until.isoformat()
    cmd = [
        "git", "-C", str(project_root), "log",
        f"--since={since_iso}",
        f"--until={until_iso}",
        "--name-only",
        "--pretty=format:__COMMIT__|%H|%ct",
        "--",
    ] + path_patterns
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    except (subprocess.TimeoutExpired, OSError):
        return []
    if result.returncode != 0:
        return []
    out: List[Tuple[str, datetime, List[str]]] = []
    current_sha: Optional[str] = None
    current_dt: Optional[datetime] = None
    current_files: List[str] = []
    for line in result.stdout.splitlines():
        if line.startswith("__COMMIT__|"):
            if current_sha is not None:
                out.append((current_sha, current_dt, current_files))
            parts = line.split("|", 2)
            if len(parts) >= 3:
                current_sha = parts[1]
                try:
                    current_dt = datetime.fromtimestamp(int(parts[2]), tz=timezone.utc)
                except Exception:
                    current_dt = None
                current_files = []
        elif line.strip() and current_sha is not None:
            current_files.append(line.strip())
    if current_sha is not None and current_dt is not None:
        out.append((current_sha, current_dt, current_files))
    return out


def _format_delta(field: str, before: Any, after: Any) -> str:
    """Render a single field change as a human-readable signal."""
    def _repr(v: Any) -> str:
        if v is None:
            return "∅"
        if isinstance(v, list):
            return f"[{len(v)}]" if len(v) > 3 else f"[{','.join(str(x) for x in v)}]"
        s = str(v)
        return s if len(s) <= 30 else s[:27] + "…"
    return f"{field}: {_repr(before)} → {_repr(after)}"


def _detect_list_changes(field: str, before: Any, after: Any) -> Optional[str]:
    """For list fields like stages_completed, describe what was added/removed."""
    b = before if isinstance(before, list) else []
    a = after if isinstance(after, list) else []
    b_set = set(b)
    a_set = set(a)
    added = [x for x in a if x not in b_set]
    removed = [x for x in b if x not in a_set]
    if not added and not removed:
        return None
    parts = []
    if added:
        parts.append(f"+{','.join(str(x) for x in added)}")
    if removed:
        parts.append(f"-{','.join(str(x) for x in removed)}")
    return f"{field}: {' '.join(parts)}"


def extract_backlog_deltas(target: ProjectTarget, since: datetime, until: datetime,
                            types_filter: Set[str], full_content: bool) -> List[TimelineEvent]:
    """Emit delta events for backlog files whose tracked frontmatter fields changed.

    Only processes files under backlog/** for the target project. Uses git to
    diff revisions; emits one event per (commit, file, changed-field).
    """
    # Fast path: if caller filtered to types that can't include backlog items, skip.
    if types_filter and not types_filter & {"epic", "task", "module", "milestone", "progress"}:
        return []

    # Build pathspec for backlog files. Respect wiki_dir when present.
    wiki_prefix = f"{target.wiki_dir}/" if target.wiki_dir else ""
    path_patterns = [
        f"{wiki_prefix}backlog/**/*.md",
        f"{wiki_prefix}backlog/*.md",
    ]

    commits = _git_commits_touching_paths(target.root, since, until, path_patterns)
    events: List[TimelineEvent] = []

    for sha, commit_dt, files in commits:
        if commit_dt is None:
            continue
        for rel_file in files:
            if not rel_file.endswith(".md"):
                continue
            # Only .md files under backlog/
            if "/backlog/" not in f"/{rel_file}":
                continue

            # Before: parent commit; After: this commit
            before_text = _git_show_file(target.root, f"{sha}~1", rel_file)
            after_text = _git_show_file(target.root, sha, rel_file)

            before_meta: Dict[str, Any] = {}
            after_meta: Dict[str, Any] = {}
            try:
                if before_text is not None:
                    before_meta, _ = parse_frontmatter(before_text)
            except Exception:
                pass
            try:
                if after_text is not None:
                    after_meta, _ = parse_frontmatter(after_text)
            except Exception:
                pass

            if not after_meta:
                continue

            page_type = str(after_meta.get("type", "")).strip().lower()
            event_type = PAGE_TYPE_TO_EVENT.get(page_type, page_type or "task")
            if types_filter and event_type not in types_filter and "progress" not in types_filter:
                continue

            title = _page_title(after_meta, Path(rel_file))
            tags = after_meta.get("tags", []) or []
            subject = [t for t in tags if isinstance(t, str)][:6]

            # Field-by-field diff
            delta_signals: List[str] = []
            for field in TRACKED_DELTA_FIELDS:
                before_val = before_meta.get(field)
                after_val = after_meta.get(field)
                if before_val == after_val:
                    continue
                # Empty → non-empty / non-empty → empty counts as change
                if (before_val in (None, "", []) and after_val in (None, "", [])):
                    continue
                if isinstance(after_val, list) or isinstance(before_val, list):
                    desc = _detect_list_changes(field, before_val, after_val)
                    if desc:
                        delta_signals.append(desc)
                else:
                    delta_signals.append(_format_delta(field, before_val, after_val))

            if not delta_signals:
                continue

            # When file was newly created in this commit (no prior revision),
            # frontmatter-events extractor already emits a 'created' event.
            # Here we only emit a delta if there was a meaningful transition.
            if not before_meta:
                # File didn't exist before → this is creation, not a transition.
                # Skip to avoid double-counting with extract_frontmatter_events.
                continue

            # Phase 5: parent epic lookup from after_meta (post-change state)
            raw_epic = after_meta.get("epic")
            parent_epic = str(raw_epic).strip() if raw_epic else None

            events.append(TimelineEvent(
                date=commit_dt,
                project=target.name,
                type=event_type,
                title=title,
                path=rel_file,
                subject=subject,
                signal=" | ".join(delta_signals),
                commit_sha=sha,
                body_preview=None,
                full_content=None,
                parent_epic=parent_epic,
            ))
    return events


# ---------------------------------------------------------------------------
# Remote (gh api) extractors — opt-in via --remote flag (slower)
# ---------------------------------------------------------------------------

def _gh_available() -> bool:
    """Check if gh CLI is present and authenticated."""
    import shutil as _shutil
    if _shutil.which("gh") is None:
        return False
    try:
        r = subprocess.run(["gh", "auth", "status"], capture_output=True, text=True, timeout=5)
        return r.returncode == 0
    except (subprocess.TimeoutExpired, OSError):
        return False


def _gh_api_json(endpoint: str, timeout: int = 20) -> Optional[Any]:
    """Invoke `gh api <endpoint>` and return parsed JSON, None on failure."""
    try:
        r = subprocess.run(
            ["gh", "api", endpoint, "--header", "X-GitHub-Api-Version: 2022-11-28"],
            capture_output=True, text=True, timeout=timeout,
        )
    except (subprocess.TimeoutExpired, OSError):
        return None
    if r.returncode != 0:
        return None
    try:
        return json.loads(r.stdout)
    except Exception:
        return None


def extract_commits_remote(target: ProjectTarget, since: datetime, until: datetime) -> List[TimelineEvent]:
    """Remote git log via `gh api repos/{owner}/{repo}/commits?since=...&until=...`."""
    remote = target.remote or {}
    owner = remote.get("owner")
    repo = remote.get("repo")
    if not owner or not repo:
        return []
    endpoint = (
        f"repos/{owner}/{repo}/commits"
        f"?since={since.isoformat()}&until={until.isoformat()}&per_page=100"
    )
    data = _gh_api_json(endpoint)
    if not isinstance(data, list):
        return []
    events: List[TimelineEvent] = []
    for item in data:
        sha = item.get("sha", "")
        commit = item.get("commit", {}) or {}
        author = (commit.get("author") or {}).get("name", "?")
        date_str = (commit.get("author") or {}).get("date", "")
        subject = (commit.get("message") or "").split("\n", 1)[0]
        try:
            dt = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
        except Exception:
            continue
        events.append(TimelineEvent(
            date=dt,
            project=target.name,
            type="commit",
            title=subject[:140],
            path="",
            subject=[],
            signal="[remote]",
            commit_sha=sha,
            author=author,
        ))
    return events


def _gh_walk_dir_md(target: ProjectTarget, rel_dir: str, since: datetime, until: datetime,
                    types_filter: Set[str], full_content: bool,
                    depth: int = 0, max_depth: int = 4) -> List[TimelineEvent]:
    """Walk a directory in the remote repo via gh api; fetch .md files and parse frontmatter."""
    if depth > max_depth:
        return []
    remote = target.remote or {}
    owner = remote.get("owner")
    repo = remote.get("repo")
    if not owner or not repo:
        return []
    endpoint = f"repos/{owner}/{repo}/contents/{rel_dir}"
    entries = _gh_api_json(endpoint)
    if not isinstance(entries, list):
        return []
    events: List[TimelineEvent] = []
    for entry in entries:
        if not isinstance(entry, dict):
            continue
        etype = entry.get("type")
        path = entry.get("path", "")
        name = entry.get("name", "")
        if etype == "dir":
            events.extend(_gh_walk_dir_md(
                target, path, since, until, types_filter, full_content, depth + 1, max_depth
            ))
        elif etype == "file" and name.endswith(".md"):
            # Fetch file content
            content_endpoint = f"repos/{owner}/{repo}/contents/{path}"
            file_data = _gh_api_json(content_endpoint)
            if not isinstance(file_data, dict):
                continue
            try:
                import base64
                raw_b64 = file_data.get("content", "")
                text = base64.b64decode(raw_b64).decode("utf-8", errors="replace")
            except Exception:
                continue
            try:
                meta, body = parse_frontmatter(text)
            except Exception:
                continue
            if not meta:
                # Maybe it's a dated raw-note without frontmatter
                m = _DATE_PREFIX_RE.match(name)
                if m:
                    try:
                        dt = datetime.fromisoformat(m.group(1)).replace(tzinfo=timezone.utc)
                    except Exception:
                        continue
                    if since <= dt <= until:
                        if not types_filter or "directive" in types_filter or "note" in types_filter:
                            events.append(TimelineEvent(
                                date=dt,
                                project=target.name,
                                type="note",
                                title=name,
                                path=path,
                                signal="[remote]",
                                body_preview=_make_preview(text) if text else None,
                                full_content=text if full_content else None,
                            ))
                continue

            page_type = str(meta.get("type", "")).strip().lower()
            event_type = PAGE_TYPE_TO_EVENT.get(page_type, page_type or "page")
            if types_filter and event_type not in types_filter:
                continue

            created = _parse_date_field(meta.get("created"))
            updated = _parse_date_field(meta.get("updated"))
            title = _page_title(meta, Path(name))
            tags = meta.get("tags", []) or []
            subject = [t for t in tags if isinstance(t, str)][:6]
            signal_base = _derive_signal(meta, Path(path)) or ""
            preview = _make_preview(body) if body else None

            if created and since <= created <= until:
                events.append(TimelineEvent(
                    date=created,
                    project=target.name,
                    type=event_type,
                    title=title,
                    path=path,
                    subject=subject,
                    signal=((signal_base + " | ") if signal_base else "") + "created | [remote]",
                    threads_to=_extract_threads_to(meta),
                    body_preview=preview,
                    full_content=(body if full_content else None),
                ))
            if updated and since <= updated <= until:
                if not created or updated.date() != created.date():
                    events.append(TimelineEvent(
                        date=updated,
                        project=target.name,
                        type=event_type,
                        title=title,
                        path=path,
                        subject=subject,
                        signal=((signal_base + " | ") if signal_base else "") + "updated | [remote]",
                        threads_to=_extract_threads_to(meta),
                        body_preview=preview,
                        full_content=(body if full_content else None),
                    ))
    return events


def extract_frontmatter_events_remote(target: ProjectTarget, since: datetime, until: datetime,
                                        types_filter: Set[str], full_content: bool) -> List[TimelineEvent]:
    """Remote frontmatter walk — recursive via gh api. SLOW (1 call per directory + 1 per .md file)."""
    events: List[TimelineEvent] = []
    wiki_dir = target.wiki_dir or ""
    # Walk the wiki_dir if declared
    if wiki_dir:
        events.extend(_gh_walk_dir_md(target, wiki_dir, since, until, types_filter, full_content))
    # Also try raw/notes (directives are usually at project root, not under wiki_dir)
    if not types_filter or "directive" in types_filter or "note" in types_filter:
        notes_events = _gh_walk_dir_md(target, "raw/notes", since, until, types_filter, full_content)
        # Convert matching notes into 'directive' or 'note' event type based on frontmatter note_type
        for e in notes_events:
            # The _gh_walk_dir_md handler doesn't do note_type detection; fix up here
            if e.type == "note":
                # Already tagged as note, leave it
                pass
        events.extend(notes_events)
    return events


# ---------------------------------------------------------------------------
# Main compute function
# ---------------------------------------------------------------------------

def compute_timeline(
    scope: Optional[List[str]] = None,
    since: str = "7d",
    until: Optional[str] = None,
    types: Optional[List[str]] = None,
    wiki_root: Optional[Path] = None,
    brain_root: Optional[Path] = None,
    full_content: bool = False,
    group_by: str = "date",
    output_format: str = "markdown",
    remote: bool = False,
    collapse_arcs: bool = False,
    epic: Optional[str] = None,
    path_filter: Optional[str] = None,
) -> str:
    """Entry point used by CLI + MCP.

    Returns the rendered timeline string.

    Args:
        remote: When True, non-local projects are fetched via gh api (slower).
                When False (default), unavailable projects surface as notices only.
    """
    wiki_root = (wiki_root or get_project_root()).resolve()
    brain_root = (brain_root or get_project_root()).resolve()

    # Default scope depends on whether self == brain.
    if scope is None:
        scope = ["self"] if wiki_root == brain_root else ["self", "brain"]

    now = datetime.now(timezone.utc)
    since_dt = parse_when(since, now=now)
    until_dt = parse_when(until, now=now) if until else now

    types_filter: Set[str] = set()
    if types:
        for t in types:
            t = t.strip().lower()
            if t == "all" or not t:
                continue
            types_filter.add(t)

    registry = load_registry(brain_root)
    targets = resolve_scope(scope, wiki_root, brain_root, registry)

    all_events: List[TimelineEvent] = []
    notices: List[str] = []

    for target in targets:
        if target.local_available:
            all_events.extend(extract_commits(target, since_dt, until_dt, full_content))
            all_events.extend(extract_frontmatter_events(target, since_dt, until_dt, types_filter, full_content))
            all_events.extend(extract_dated_notes(target, since_dt, until_dt, types_filter, full_content))
            all_events.extend(extract_session_logs(target, since_dt, until_dt, types_filter, full_content))
            all_events.extend(extract_backlog_deltas(target, since_dt, until_dt, types_filter, full_content))
        else:
            # Project declared in scope but not locally cloned.
            if not remote:
                notices.append(
                    f"⚠ `{target.name}` not locally accessible at `{target.root}`. "
                    f"Pass `--remote` to fetch via gh api (slower), or omit from scope."
                )
            else:
                # Remote fetch path — slower, uses gh api.
                if not _gh_available():
                    notices.append(
                        f"⚠ `{target.name}` not locally accessible and `gh` CLI is not available/authenticated. "
                        f"Install + authenticate gh, or omit from scope."
                    )
                elif not target.remote:
                    notices.append(
                        f"⚠ `{target.name}` not locally accessible and registry has no `remote:` block — cannot fetch."
                    )
                else:
                    notices.append(
                        f"ℹ `{target.name}` fetched remotely via gh api (slower; backlog deltas not included for remote)."
                    )
                    all_events.extend(extract_commits_remote(target, since_dt, until_dt))
                    all_events.extend(extract_frontmatter_events_remote(
                        target, since_dt, until_dt, types_filter, full_content
                    ))
                    # Backlog deltas over remote would require N+1 gh api calls per file; skip for now.

    # Apply types filter to commits (not filtered above since git log can't filter by type).
    if types_filter:
        all_events = [e for e in all_events if e.type in types_filter]

    # Epic filter: keep events whose parent_epic matches OR whose path is the epic file itself.
    if epic:
        e_norm = epic.strip()
        def _matches_epic(ev: TimelineEvent) -> bool:
            if ev.parent_epic == e_norm:
                return True
            # Epic file itself: path like 'wiki/backlog/epics/E013-*.md' or the full title
            if ev.path and f"/{e_norm}-" in f"/{ev.path}":
                return True
            if ev.path and ev.path.endswith(f"{e_norm}.md"):
                return True
            return False
        all_events = [ev for ev in all_events if _matches_epic(ev)]

    # Path filter: substring match against event path.
    if path_filter:
        all_events = [ev for ev in all_events if path_filter in ev.path]

    # Noise reduction: suppress snapshot events that duplicate delta events.
    # When a file has delta events (with commit_sha) on a date, its bare
    # frontmatter-snapshot event for the same date adds no new information.
    all_events = _suppress_redundant_snapshots(all_events)

    # Cross-project arc linking: when event A's threads_to points at event B
    # (same target project+path) and both are in range, mark the link on both.
    all_events = _link_cross_project_threads(all_events)

    # Optional: collapse same-file same-day events into one arc-summary line.
    if collapse_arcs:
        all_events = _collapse_arcs(all_events)

    # Sort newest-first.
    all_events.sort(key=lambda e: e.date, reverse=True)

    if output_format == "json":
        return render_json(all_events, targets, since_dt, until_dt, notices)
    return render_markdown(all_events, targets, since_dt, until_dt, group_by, full_content, notices)


# ---------------------------------------------------------------------------
# Noise-reduction: suppress redundant snapshots
# ---------------------------------------------------------------------------
#
# Frontmatter-extractor emits a snapshot event per file per (created, updated)
# date. Backlog-delta extractor emits precise transition events with commit_sha
# for the same files. When both exist for the same file on the same date, the
# snapshot is redundant — the delta events already show what changed AND carry
# the commit provenance.
#
# Rule: if a file has ≥1 event with commit_sha on a given date, suppress
# snapshot events (no commit_sha) for that file+date. Keeps the journey visible
# via deltas; drops the "file was touched today" noise.


def _suppress_redundant_snapshots(events: List[TimelineEvent]) -> List[TimelineEvent]:
    """Drop snapshot events that are superseded by same-file same-day delta events."""
    # Build index of (project, path, date) that have at least one commit-attached event.
    has_tracked: Set[Tuple[str, str, str]] = set()
    for e in events:
        if e.commit_sha and e.path:
            key = (e.project, e.path, e.date.date().isoformat())
            has_tracked.add(key)
    if not has_tracked:
        return events
    kept: List[TimelineEvent] = []
    for e in events:
        # Commit and delta events always kept
        if e.commit_sha:
            kept.append(e)
            continue
        # Events without a path (rare) always kept
        if not e.path:
            kept.append(e)
            continue
        key = (e.project, e.path, e.date.date().isoformat())
        if key in has_tracked:
            # Redundant snapshot — drop
            continue
        kept.append(e)
    return kept


# ---------------------------------------------------------------------------
# Cross-project arc linking (Phase 4)
# ---------------------------------------------------------------------------
#
# An event's `threads_to` carries cross-project references (project:path) parsed
# from the wiki page's `sources:` frontmatter. After all events are gathered, we
# do a second pass: for each event with threads_to, check whether any OTHER
# event in the same result set targets the same (project, path). If so, mark
# the link — both the "from" and "to" events get `linked_events` entries that
# describe the counterpart.
#
# This surfaces the ecosystem arc — a wiki lesson synthesized today visibly
# connects to the OpenArms incident it derived from, when both fall in range.


def _link_cross_project_threads(events: List[TimelineEvent]) -> List[TimelineEvent]:
    """Populate linked_events for cross-project arcs visible within the result set."""
    # Index events by (project, path) — both exact and path-prefix lookups
    by_project_path: Dict[Tuple[str, str], List[TimelineEvent]] = {}
    for e in events:
        if not e.path:
            continue
        key = (e.project, e.path)
        by_project_path.setdefault(key, []).append(e)

    # Also index by (project, basename-less path) for fuzzier matches
    # (a wiki source may reference 'wiki/domains/learnings/foo.md' while an
    # event emits the same path; exact-match is the common case).

    def _describe(ev: TimelineEvent) -> str:
        return f"{ev.date.date().isoformat()} · `{ev.project}` · {ev.type} · {ev.title}"

    for e in events:
        if not e.threads_to:
            continue
        for thread in e.threads_to:
            # thread is like "openarms:wiki/domains/learnings/foo.md"
            if ":" not in thread:
                continue
            tgt_project, tgt_path = thread.split(":", 1)
            candidates = by_project_path.get((tgt_project, tgt_path), [])
            if not candidates:
                # Try removing leading 'wiki/' on target path if registry uses wiki_dir
                alt_path = tgt_path[5:] if tgt_path.startswith("wiki/") else f"wiki/{tgt_path}"
                candidates = by_project_path.get((tgt_project, alt_path), [])
            for cand in candidates:
                if cand is e:
                    continue
                desc = _describe(cand)
                if desc not in e.linked_events:
                    e.linked_events.append(desc)
                back_desc = _describe(e)
                if back_desc not in cand.linked_events:
                    cand.linked_events.append(back_desc)
    return events


# ---------------------------------------------------------------------------
# Arc collapse (opt-in via --collapse-arcs)
# ---------------------------------------------------------------------------
#
# A single backlog task going scaffold → implement → test → done in one day
# emits 4 delta events. Operators who want the COMPACT journey view can opt in
# to arc-collapse: same-file same-day events compress into ONE line showing the
# time span + merged signals + event count.
#
# Default is OFF — delta events are more informative than collapsed summaries
# when investigating specific transitions.


def _merge_signals_for_arc(group: List[TimelineEvent]) -> str:
    """Merge per-event signals into an arc-summary signal string.

    Input signals look like:
      - "readiness: 0 → 33 | stages_completed: +scaffold | current_stage: scaffold → implement"
      - "readiness: 33 → 67 | stages_completed: +implement | current_stage: implement → test"
    Output should be:
      - "readiness: 0 → 100 | stages: +scaffold+implement+test | current_stage: → test"
    """
    # Collect per-field first-value and last-value plus list-additions
    field_first: Dict[str, str] = {}
    field_last: Dict[str, str] = {}
    list_adds: Dict[str, List[str]] = {}
    for e in group:
        if not e.signal:
            continue
        for chunk in e.signal.split("|"):
            chunk = chunk.strip()
            if not chunk:
                continue
            m = re.match(r"^([a-z_]+):\s*(.+)$", chunk)
            if not m:
                continue
            field = m.group(1)
            value_str = m.group(2).strip()
            # List-style additions look like "+scaffold" or "+implement"
            if value_str.startswith("+") and " " not in value_str and "→" not in value_str:
                list_adds.setdefault(field, []).append(value_str.lstrip("+"))
                continue
            # Transition style: "0 → 33"
            if "→" in value_str:
                parts = [p.strip() for p in value_str.split("→", 1)]
                if field not in field_first:
                    field_first[field] = parts[0]
                field_last[field] = parts[1] if len(parts) > 1 else parts[0]
            else:
                # Non-transition single value
                if field not in field_first:
                    field_first[field] = value_str
                field_last[field] = value_str

    merged_parts: List[str] = []
    for field in ("readiness", "progress", "current_stage", "status", "maturity"):
        if field in field_first and field in field_last:
            if field_first[field] != field_last[field]:
                merged_parts.append(f"{field}: {field_first[field]} → {field_last[field]}")
    for field, adds in list_adds.items():
        if adds:
            merged_parts.append(f"{field}: +{'+'.join(adds)}")
    return " | ".join(merged_parts)


def _collapse_arcs(events: List[TimelineEvent]) -> List[TimelineEvent]:
    """Collapse same-file same-day event clusters into one representative event.

    Only applies to events with a path. Commits and path-less events pass through.
    Returns a list where clusters of size ≥2 are replaced by a single event.
    """
    from collections import defaultdict
    passthrough: List[TimelineEvent] = []
    groups: Dict[Tuple[str, str, str], List[TimelineEvent]] = defaultdict(list)

    for e in events:
        if not e.path or e.type == "commit":
            passthrough.append(e)
            continue
        key = (e.project, e.path, e.date.date().isoformat())
        groups[key].append(e)

    collapsed: List[TimelineEvent] = []
    for key, grp in groups.items():
        if len(grp) == 1:
            collapsed.append(grp[0])
            continue
        grp_sorted = sorted(grp, key=lambda x: x.date)
        first = grp_sorted[0]
        last = grp_sorted[-1]
        merged_signal = _merge_signals_for_arc(grp_sorted)
        first_t = first.date.strftime("%H:%M")
        last_t = last.date.strftime("%H:%M")
        arc_signal = f"[arc: {len(grp_sorted)} events {first_t}→{last_t}]"
        if merged_signal:
            arc_signal += f" {merged_signal}"
        collapsed.append(TimelineEvent(
            date=last.date,
            project=last.project,
            type=last.type,
            title=last.title,
            path=last.path,
            subject=last.subject,
            signal=arc_signal,
            threads_to=last.threads_to,
            body_preview=last.body_preview,
            full_content=last.full_content,
            commit_sha=last.commit_sha,
            author=last.author,
            parent_epic=last.parent_epic,
            linked_events=list(last.linked_events),
        ))

    return passthrough + collapsed


# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------

def _format_date_header(dt: datetime) -> str:
    return dt.strftime("%Y-%m-%d (%a)")


def _format_time(dt: datetime) -> str:
    return dt.strftime("%H:%M")


def render_markdown(events: List[TimelineEvent], targets: List[ProjectTarget],
                     since: datetime, until: datetime, group_by: str,
                     full_content: bool, notices: Optional[List[str]] = None) -> str:
    lines: List[str] = []
    lines.append(f"# Timeline — {since.date().isoformat()} → {until.date().isoformat()}")
    lines.append("")
    # Scope with local/remote annotations
    scope_parts: List[str] = []
    for t in targets:
        if t.local_available:
            scope_parts.append(t.name)
        else:
            scope_parts.append(f"{t.name} (not local)")
    lines.append(f"**Scope:** {', '.join(scope_parts) or '(none resolved)'}")
    lines.append(f"**Events:** {len(events)}")
    lines.append("")
    if notices:
        lines.append("## Notices")
        lines.append("")
        for notice in notices:
            lines.append(f"- {notice}")
        lines.append("")

    if not events:
        lines.append("_No events in range._")
        return "\n".join(lines)

    if group_by == "date":
        # Group by date (YYYY-MM-DD)
        current_date: Optional[str] = None
        for e in events:
            d = e.date.date().isoformat()
            if d != current_date:
                lines.append("")
                lines.append(f"## {_format_date_header(e.date)}")
                lines.append("")
                current_date = d
            lines.append(_render_event_line(e))
            if full_content and e.full_content:
                lines.append("")
                lines.append("```")
                lines.append(e.full_content.rstrip())
                lines.append("```")
                lines.append("")
    elif group_by == "project":
        by_project: Dict[str, List[TimelineEvent]] = {}
        for e in events:
            by_project.setdefault(e.project, []).append(e)
        for project, evs in by_project.items():
            lines.append("")
            lines.append(f"## {project} ({len(evs)} events)")
            lines.append("")
            for e in evs:
                lines.append(_render_event_line(e, show_date=True))
                if full_content and e.full_content:
                    lines.append("")
                    lines.append("```")
                    lines.append(e.full_content.rstrip())
                    lines.append("```")
                    lines.append("")
    elif group_by == "type":
        by_type: Dict[str, List[TimelineEvent]] = {}
        for e in events:
            by_type.setdefault(e.type, []).append(e)
        for event_type in sorted(by_type.keys()):
            evs = by_type[event_type]
            lines.append("")
            lines.append(f"## {event_type} ({len(evs)} events)")
            lines.append("")
            for e in evs:
                lines.append(_render_event_line(e, show_date=True))
                if full_content and e.full_content:
                    lines.append("")
                    lines.append("```")
                    lines.append(e.full_content.rstrip())
                    lines.append("```")
                    lines.append("")
    elif group_by == "epic":
        # Phase 5: group task/module events by their parent_epic; others by type.
        by_epic: Dict[str, List[TimelineEvent]] = {}
        uncategorized: List[TimelineEvent] = []
        for e in events:
            key = e.parent_epic
            if key:
                by_epic.setdefault(f"{e.project}::{key}", []).append(e)
            else:
                uncategorized.append(e)
        # Epic groups first, sorted by project+epic
        for epic_key in sorted(by_epic.keys()):
            proj, epic_id = epic_key.split("::", 1)
            evs = by_epic[epic_key]
            lines.append("")
            lines.append(f"## `{proj}` · {epic_id} — {len(evs)} events")
            lines.append("")
            for e in sorted(evs, key=lambda x: x.date, reverse=True):
                lines.append(_render_event_line(e, show_date=True))
                if full_content and e.full_content:
                    lines.append("")
                    lines.append("```")
                    lines.append(e.full_content.rstrip())
                    lines.append("```")
                    lines.append("")
        if uncategorized:
            lines.append("")
            lines.append(f"## (no parent epic) — {len(uncategorized)} events")
            lines.append("")
            for e in uncategorized:
                lines.append(_render_event_line(e, show_date=True))
                if full_content and e.full_content:
                    lines.append("")
                    lines.append("```")
                    lines.append(e.full_content.rstrip())
                    lines.append("```")
                    lines.append("")
    else:
        for e in events:
            lines.append(_render_event_line(e, show_date=True))

    return "\n".join(lines)


def _render_event_line(e: TimelineEvent, show_date: bool = False) -> str:
    time = _format_time(e.date) if e.date else ""
    parts: List[str] = []
    date_prefix = f"{e.date.date().isoformat()} " if show_date else ""
    parts.append(f"- **{date_prefix}{time}**  `{e.project}`  _{e.type}_")
    # Phase 5: inline parent-epic tag for task/module events
    epic_tag = f" `[{e.parent_epic}]`" if e.parent_epic else ""
    parts.append(f"  ·{epic_tag} **{e.title}**")
    if e.signal:
        parts.append(f" _(_{e.signal}_)_")
    if e.commit_sha:
        parts.append(f" `{e.commit_sha[:8]}`")
    tail_parts: List[str] = []
    if e.author:
        tail_parts.append(f"by {e.author}")
    if e.path:
        tail_parts.append(f"`{e.path}`")
    if e.threads_to:
        tail_parts.append(f"→ {', '.join(e.threads_to[:3])}")
    if tail_parts:
        parts.append(f"  — {'; '.join(tail_parts)}")
    # Put body preview on continuation line if present
    line = "".join(parts)
    if e.linked_events:
        # Cross-project arc: show the connections
        for linked in e.linked_events[:3]:
            line += f"\n    ↕ {linked}"
        if len(e.linked_events) > 3:
            line += f"\n    ↕ _and {len(e.linked_events) - 3} more_"
    if e.body_preview:
        line += f"\n    > {e.body_preview}"
    return line


def render_json(events: List[TimelineEvent], targets: List[ProjectTarget],
                 since: datetime, until: datetime,
                 notices: Optional[List[str]] = None) -> str:
    doc = {
        "since": since.isoformat(),
        "until": until.isoformat(),
        "scope": [
            {"name": t.name, "local_available": t.local_available}
            for t in targets
        ],
        "event_count": len(events),
        "notices": notices or [],
        "events": [e.to_dict() for e in events],
    }
    return json.dumps(doc, indent=2, default=str)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    import argparse
    p = argparse.ArgumentParser(
        description="Timeline — computed cross-project temporal view."
    )
    p.add_argument("--scope", default=None,
                   help="Comma-separated list. Magic: self, brain, all. Or explicit project names.")
    p.add_argument("--since", default="7d",
                   help="Duration (7d, 24h, 2w) or ISO date. Default: 7d.")
    p.add_argument("--until", default=None,
                   help="Duration or ISO date. Default: now.")
    p.add_argument("--type", dest="types", default=None,
                   help="Comma-separated event types. Default: all.")
    p.add_argument("--group-by", dest="group_by", default="date",
                   choices=["date", "project", "type", "epic", "none"])
    p.add_argument("--format", dest="output_format", default="markdown",
                   choices=["markdown", "json"])
    p.add_argument("--full-content", dest="full_content", action="store_true",
                   help="Include full event bodies (no caps).")
    p.add_argument("--remote", dest="remote", action="store_true",
                   help="Fetch non-local projects via gh api (slower — opt-in). "
                        "Without this flag, unavailable projects surface as notices only.")
    p.add_argument("--collapse-arcs", dest="collapse_arcs", action="store_true",
                   help="Collapse same-file same-day event clusters into one arc-summary line.")
    p.add_argument("--epic", dest="epic", default=None,
                   help="Filter to one epic (e.g. --epic E013). Matches parent_epic OR the epic file itself.")
    p.add_argument("--path", dest="path_filter", default=None,
                   help="Filter events whose path contains this substring (e.g. --path T120).")
    p.add_argument("--wiki-root", dest="wiki_root", default=None,
                   help="Override self project root (default: current project).")
    p.add_argument("--brain", dest="brain", default=None,
                   help="Override second-brain root (default: auto-detect).")
    args = p.parse_args()

    scope_list = None
    if args.scope:
        scope_list = [s.strip() for s in args.scope.split(",") if s.strip()]
    types_list = None
    if args.types:
        types_list = [t.strip() for t in args.types.split(",") if t.strip()]

    wiki_root = Path(args.wiki_root).resolve() if args.wiki_root else None
    brain_root = Path(args.brain).resolve() if args.brain else None

    output = compute_timeline(
        scope=scope_list,
        since=args.since,
        until=args.until,
        types=types_list,
        wiki_root=wiki_root,
        brain_root=brain_root,
        full_content=args.full_content,
        group_by=args.group_by,
        output_format=args.output_format,
        remote=args.remote,
        collapse_arcs=args.collapse_arcs,
        epic=args.epic,
        path_filter=args.path_filter,
    )
    print(output)


if __name__ == "__main__":
    main()
