"""Shared helpers for cross-project tools (cross_project_note, cross_project_task).

Per operator directive 2026-05-05: a tool to add a TASK (and a NOTE) into
other projects via designated channels. This module factors common
plumbing — registry resolution, slug cleaning, frontmatter helpers — used
by both tools.

Boundary preservation: these tools write to specific designated paths in
sister projects (wiki/log/ for notes, wiki/backlog/tasks/ for tasks).
They do NOT modify other paths.
"""

from __future__ import annotations

import datetime as dt
import re
import sys
from pathlib import Path
from typing import Tuple

import yaml

REGISTRY = (
    Path(__file__).resolve().parent.parent
    / "wiki" / "config" / "sister-projects.yaml"
)


def load_registry():
    with open(REGISTRY) as f:
        return yaml.safe_load(f)


def resolve_target(name: str) -> Tuple[Path, str, dict]:
    """Resolve target project name to (path, canonical_name, registry_entry)."""
    reg = load_registry()
    projects = reg.get("projects", {})

    if name in projects:
        entry = projects[name]
        canon = name
    else:
        # Alias match
        canon = None
        entry = None
        for proj_name, proj in projects.items():
            if name in proj.get("aliases", []):
                entry = proj
                canon = proj_name
                break
        if entry is None:
            sys.exit(
                f"target '{name}' not in sister-projects registry. "
                f"Known: {sorted(projects.keys())}"
            )

    raw_path = entry.get("path")
    if not raw_path:
        sys.exit(f"target '{canon}' has no path in registry")

    target = Path(raw_path).expanduser().resolve()
    if not target.exists():
        sys.exit(f"target '{canon}' path does not exist locally: {target}")

    return target, canon, entry


def slug_clean(s: str) -> str:
    """Sanitize slug: lowercase, alnum + hyphens only, no leading/trailing hyphens."""
    s = re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
    if not s:
        sys.exit("slug is empty after cleaning")
    return s


def today_iso() -> str:
    return dt.date.today().isoformat()


def read_content(content_file: Path | None) -> str:
    """Read body content from --content-file or stdin."""
    if content_file:
        if not content_file.exists():
            sys.exit(f"content-file not found: {content_file}")
        return content_file.read_text()
    if sys.stdin.isatty():
        sys.exit("no --content-file and stdin is a tty; pipe content or use --content-file")
    return sys.stdin.read()


def find_task_dir(target_path: Path, target_entry: dict) -> Path:
    """Locate the target's tasks/ directory per its layout."""
    candidates = [
        target_path / "wiki" / "backlog" / "tasks",
        target_path / target_entry.get("wiki_dir", "wiki") / "backlog" / "tasks",
        target_path / "backlog" / "tasks",
    ]
    for c in candidates:
        if c.exists():
            return c
    sys.exit(
        f"target '{target_path}' has no wiki/backlog/tasks/ directory at "
        f"{candidates[0]} or alternates. This tool requires the target to "
        f"have a backlog/tasks layer."
    )


def find_log_dir(target_path: Path, target_entry: dict) -> Path:
    """Locate the target's log/ directory per its layout."""
    candidates = [
        target_path / target_entry.get("wiki_dir", "wiki") / "log",
        target_path / "wiki" / "log",
        target_path / "log",
        target_path / "docs" / "log",
    ]
    for c in candidates:
        if c.exists():
            return c
    sys.exit(
        f"target '{target_path}' has no wiki/log/ directory. "
        f"This tool requires the target to have a project-iteration log layer."
    )


def next_task_number(tasks_dir: Path) -> int:
    """Scan existing T###-*.md filenames; return next available number."""
    pattern = re.compile(r"^T(\d{3,4})-.*\.md$")
    nums = []
    for p in tasks_dir.iterdir():
        m = pattern.match(p.name)
        if m:
            nums.append(int(m.group(1)))
    return max(nums) + 1 if nums else 1
