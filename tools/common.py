"""Shared utilities for wiki tools.

Provides YAML frontmatter parsing, section extraction, relationship parsing,
and config file loading. Used by validate.py, manifest.py, lint.py, export.py,
and stats.py.
"""

import json
import os
import re
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import yaml


# ---------------------------------------------------------------------------
# Consumer runtime signaling
# ---------------------------------------------------------------------------
#
# Per `wiki/decisions/00_inbox/consumer-runtime-signaling-via-mcp-config.md`:
# a consumer (harness/fleet/solo) declares its runtime identity via the
# `MCP_CLIENT_RUNTIME` environment variable, which MCP clients pass through
# via their `.mcp.json` entry's `env:` block.
#
# Solo is the default. The wiki cannot detect non-default modes from inside
# the project — only the consumer's runtime knows. See also:
# `wiki/lessons/00_inbox/execution-mode-is-consumer-property-not-project-property.md`

CONSUMER_RUNTIME_ENV = "MCP_CLIENT_RUNTIME"
CONSUMER_RUNTIME_DEFAULT = "solo"


def get_consumer_runtime() -> str:
    """Return the consumer's declared runtime identity.

    Reads the MCP_CLIENT_RUNTIME env var that an MCP client can set via its
    `.mcp.json` entry's `env:` block. Falls back to `"solo"` when unset or empty
    — solo is the default for every project; non-default must be declared
    by the consumer.
    """
    value = os.environ.get(CONSUMER_RUNTIME_ENV, "").strip()
    return value or CONSUMER_RUNTIME_DEFAULT


def consumer_runtime_is_declared() -> bool:
    """True if the consumer explicitly declared a non-default runtime."""
    return bool(os.environ.get(CONSUMER_RUNTIME_ENV, "").strip())


# ---------------------------------------------------------------------------
# Context detection — shared by gateway orient + what-do-i-need (E022)
# Design: wiki/backlog/modules/e022-m002-gateway-orient-subcommand.md
# ---------------------------------------------------------------------------

SESSION_STATE_PATH = Path.home() / ".cache" / "research-wiki" / "session-state.json"
SESSION_STALENESS_MINUTES = 30


def detect_context(
    wiki_root: Path = None,
    brain_root: Path = None,
    orient_as: str = None,
    fresh: bool = False,
) -> dict:
    """Detect (location, freshness) context for gateway output branching.

    Priority stack (highest first):
      1. orient_as flag (explicit override)
      2. MCP_CLIENT_RUNTIME env (consumer-declared)
      3. wiki_root resolution (brain has sister-projects.yaml; sisters don't)
      4. CWD heuristic (sanity-check only)

    Design: wiki/backlog/modules/e022-m002-gateway-orient-subcommand.md
    """
    # --- Location detection ---
    if orient_as:
        location = orient_as
    elif consumer_runtime_is_declared():
        runtime = get_consumer_runtime()
        # External consumers typically declare "harness-*" or "fleet-*"
        # Brain-self is solo or brain-specific; sister has project-specific names
        if any(kw in runtime for kw in ("external", "mcp-client")):
            location = "external"
        elif any(kw in runtime for kw in ("harness-", "fleet-")):
            location = "sister"
        else:
            location = "second-brain"
    else:
        # Resolve from filesystem: brain has sister-projects.yaml
        check_root = wiki_root or _try_project_root()
        if check_root and (check_root / "wiki" / "config" / "sister-projects.yaml").exists():
            location = "second-brain"
        elif check_root and (check_root / "wiki").is_dir():
            location = "sister"
        else:
            location = "external"

    # --- Freshness detection ---
    # F3 fix: orient should only shortcircuit if orient ITSELF ran recently.
    # Running `gateway status` or `gateway health` does NOT mean you're oriented.
    # Freshness = "returning" ONLY if last_subcommand was "orient" AND within 5 min.
    # Freshness = "task-bound" ONLY if a task type was explicitly set.
    # Everything else = "fresh" (safe default: over-orient is better than under-orient).
    if fresh:
        freshness = "fresh"
    else:
        state = read_session_state()
        if state is None:
            freshness = "fresh"
        elif state.get("current_task_type"):
            freshness = "task-bound"
        elif state.get("last_subcommand") == "orient":
            # Only "returning" if orient specifically ran recently (5-min window)
            try:
                last = datetime.fromisoformat(state.get("last_invocation", ""))
                if datetime.now() - last < timedelta(minutes=5):
                    freshness = "returning"
                else:
                    freshness = "fresh"
            except (ValueError, TypeError):
                freshness = "fresh"
        else:
            # Any other gateway command ran (status, health, query) — NOT oriented
            freshness = "fresh"

    return {
        "location": location,
        "freshness": freshness,
        "consumer_runtime": get_consumer_runtime(),
    }


def _try_project_root() -> Optional[Path]:
    """Best-effort project root detection without raising."""
    try:
        return get_project_root()
    except Exception:
        return None


def read_session_state() -> Optional[dict]:
    """Read session-state from SESSION_STATE_PATH.

    Returns dict or None if file absent, unreadable, or stale (>30 min).
    """
    if not SESSION_STATE_PATH.exists():
        return None
    try:
        data = json.loads(SESSION_STATE_PATH.read_text(encoding="utf-8"))
        last_str = data.get("last_invocation", "")
        if last_str:
            last = datetime.fromisoformat(last_str)
            if datetime.now() - last > timedelta(minutes=SESSION_STALENESS_MINUTES):
                return None
        return data
    except (json.JSONDecodeError, ValueError, KeyError, OSError):
        return None


def write_session_state(
    context: dict,
    subcommand: str = "orient",
    task_type: str = None,
) -> None:
    """Write session-state after a gateway invocation."""
    try:
        SESSION_STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
        data = {
            "last_invocation": datetime.now().isoformat(),
            "last_subcommand": subcommand,
            "location": context.get("location", "unknown"),
            "freshness": context.get("freshness", "unknown"),
            "current_task_type": task_type,
            "consumer_runtime": context.get("consumer_runtime", "solo"),
        }
        SESSION_STATE_PATH.write_text(json.dumps(data, indent=2), encoding="utf-8")
    except OSError:
        pass  # Non-critical — session-state is a cache, not authoritative


def parse_frontmatter(text: str) -> Tuple[Dict[str, Any], str]:
    """Parse YAML frontmatter from markdown text.

    Returns (metadata_dict, body_text). If no frontmatter found,
    returns ({}, full_text).
    """
    if not text.startswith("---"):
        return {}, text

    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text

    yaml_str = parts[1].strip()
    body = parts[2].strip()

    if not yaml_str:
        return {}, body

    try:
        meta = yaml.safe_load(yaml_str)
        if not isinstance(meta, dict):
            return {}, text
        return meta, body
    except yaml.YAMLError:
        return {}, text


def parse_sections(body: str) -> Dict[str, str]:
    """Parse markdown body into {section_name: content} dict.

    Splits on ## headings. The heading text becomes the key,
    everything until the next ## becomes the value.
    """
    sections: Dict[str, str] = {}
    current_section = None
    current_lines: List[str] = []

    for line in body.split("\n"):
        match = re.match(r"^## (.+)$", line)
        if match:
            if current_section is not None:
                sections[current_section] = "\n".join(current_lines).strip()
            current_section = match.group(1).strip()
            current_lines = []
        elif current_section is not None:
            current_lines.append(line)

    if current_section is not None:
        sections[current_section] = "\n".join(current_lines).strip()

    return sections


_REL_PATTERN = re.compile(r"^-\s*([A-Z][A-Z /\-]+?):\s*(.+)$")


def parse_relationships(text: str) -> List[Dict[str, Any]]:
    """Parse ## Relationships section content into structured list.

    Each line like '- VERB: target1, target2 (context)' becomes:
    {"verb": "VERB", "targets": ["target1", "target2 (context)"], "raw": "..."}

    Comma splitting is smart: only splits on commas NOT inside parentheses.
    """
    rels: List[Dict[str, Any]] = []
    for line in text.split("\n"):
        line = line.strip()
        match = _REL_PATTERN.match(line)
        if match:
            verb = match.group(1).strip()
            targets_raw = match.group(2).strip()
            # Strip trailing comments that appear AFTER a wikilink close.
            # Commas inside explanatory comments would otherwise create fake targets.
            # We must only strip AFTER ]] — em-dashes INSIDE wikilink titles are valid
            # (e.g. "Model — Methodology" is a real title).
            for sep in ["]] — ", "]] – ", "]] - "]:
                if sep in targets_raw:
                    targets_raw = targets_raw.split(sep, 1)[0].strip() + "]]"
                    break
            targets = _split_targets(targets_raw)
            rels.append({
                "verb": verb,
                "targets": targets,
                "raw": line,
            })
    return rels


def _split_targets(text: str) -> List[str]:
    """Split comma-separated targets, respecting parentheses and [[wikilinks]]."""
    targets: List[str] = []
    current: List[str] = []
    paren_depth = 0
    in_wikilink = False

    i = 0
    while i < len(text):
        # Track [[ ]] wikilink boundaries
        if text[i:i+2] == "[[":
            in_wikilink = True
            current.append("[")
            current.append("[")
            i += 2
            continue
        elif text[i:i+2] == "]]":
            in_wikilink = False
            current.append("]")
            current.append("]")
            i += 2
            continue
        elif text[i] == "(":
            paren_depth += 1
            current.append(text[i])
        elif text[i] == ")":
            paren_depth -= 1
            current.append(text[i])
        elif text[i] == "," and paren_depth == 0 and not in_wikilink:
            targets.append("".join(current).strip())
            current = []
        else:
            current.append(text[i])
        i += 1

    if current:
        targets.append("".join(current).strip())

    # Strip [[ ]] wikilink brackets from targets
    # Handles: [[Target]], [[file|Target]], [[Target]] (context note)
    cleaned = []
    for t in targets:
        t = t.strip()
        # Extract target from [[...]] even if followed by (context)
        wl_match = re.match(r'\[\[(.+?)\]\]', t)
        if wl_match:
            inner = wl_match.group(1).strip()
            # Handle [[filename|Display Title]] — use display title for matching
            if '|' in inner:
                inner = inner.split('|', 1)[1].strip()
            t = inner
        cleaned.append(t)
    return [t for t in cleaned if t]


def load_config(path: Path) -> Optional[Dict[str, Any]]:
    """Load a YAML config file. Returns None if file doesn't exist."""
    if not path.exists():
        return None
    with open(path) as f:
        return yaml.safe_load(f)


_SKIP_DIRS = {"config", ".obsidian", ".evolve-queue"}


def find_wiki_pages(wiki_dir: Path) -> List[Path]:
    """Find all .md files in wiki/ excluding _index.md and non-content dirs."""
    pages = []
    for md_file in sorted(wiki_dir.rglob("*.md")):
        if md_file.name == "_index.md":
            continue
        if any(d in _SKIP_DIRS for d in md_file.relative_to(wiki_dir).parts):
            continue
        pages.append(md_file)
    return pages


def find_all_wiki_files(wiki_dir: Path) -> List[Path]:
    """Find all .md files in wiki/ including _index.md but excluding non-content dirs."""
    pages = []
    for md_file in sorted(wiki_dir.rglob("*.md")):
        if any(d in _SKIP_DIRS for d in md_file.relative_to(wiki_dir).parts):
            continue
        pages.append(md_file)
    return pages


def get_project_root() -> Path:
    """Get the project root (directory containing CLAUDE.md or .git)."""
    current = Path.cwd()
    for parent in [current] + list(current.parents):
        if (parent / "CLAUDE.md").exists() or (parent / ".git").exists():
            return parent
    return current


def word_count(text: str) -> int:
    """Count words in text, stripping markdown formatting."""
    clean = re.sub(r"[#*_`\[\]\(\)]", "", text)
    return len(clean.split())


def detect_source_type(filename: str) -> str:
    """Detect source type from filename and extension.

    Returns a source_type enum value matching config/wiki-schema.yaml.
    """
    lower = filename.lower()
    ext = Path(filename).suffix.lower()

    if ext == ".pdf":
        return "paper"
    if ext in (".mp3", ".wav", ".ogg"):
        return "podcast-transcript"
    if "transcript" in lower:
        return "youtube-transcript"
    if ext in (".md", ".txt", ".html", ".htm"):
        if any(kw in lower for kw in ("note", "journal", "thought", "idea")):
            return "notes"
        return "article"
    return "article"


def rebuild_domain_index(domain_dir: Path, domain_name: str, description: str) -> str:
    """Rebuild a domain _index.md from its wiki pages.

    Scans all .md files in domain_dir (excluding _index.md),
    returns the regenerated _index.md content.

    If the existing _index.md has curated content above ## Pages,
    that content is preserved. Only the ## Pages and ## Tags sections
    are regenerated.
    """
    pages_info = []
    all_tags: list = []

    for md_file in sorted(domain_dir.rglob("*.md")):
        if md_file.name == "_index.md":
            continue
        text = md_file.read_text(encoding="utf-8")
        meta, body = parse_frontmatter(text)
        if not meta:
            continue
        title = meta.get("title", md_file.stem)
        sections = parse_sections(body)
        summary = sections.get("Summary", "").split(".")[0].strip()
        if len(summary) > 120:
            summary = summary[:117] + "..."
        rel_path = md_file.relative_to(domain_dir)
        pages_info.append({"file": str(rel_path), "title": title, "summary": summary})
        for tag in meta.get("tags", []):
            all_tags.append(tag)

    # Preserve curated content above ## Pages if it exists
    curated_header = ""
    index_path = domain_dir / "_index.md"
    if index_path.exists():
        existing = index_path.read_text(encoding="utf-8")
        pages_marker = "\n## Pages\n"
        if pages_marker in existing:
            curated_header = existing[:existing.index(pages_marker)]
        elif "\n## Pages" in existing:
            # Handle ## Pages without trailing newline
            idx = existing.index("\n## Pages")
            curated_header = existing[:idx]

    if curated_header.strip():
        # Use existing curated header
        lines = [curated_header.rstrip(), "", "## Pages", ""]
    else:
        # Generate default header
        lines = [
            f"# {domain_name.replace('-', ' ').title()}",
            "",
            description,
            "",
            "## Pages",
            "",
        ]

    if pages_info:
        for p in pages_info:
            lines.append(f"- [{p['title']}]({p['file']}) — {p['summary']}")
    else:
        lines.append("<!-- Pages added during ingestion -->")

    lines.extend(["", "## Tags", ""])
    if all_tags:
        tag_counts = {}
        for t in all_tags:
            tag_counts[t] = tag_counts.get(t, 0) + 1
        sorted_tags = sorted(tag_counts.items(), key=lambda x: x[1], reverse=True)
        lines.append(", ".join(f"`{t}`" for t, _ in sorted_tags[:20]))
    else:
        lines.append("<!-- Tag cloud generated during ingestion -->")

    return "\n".join(lines) + "\n"


def rebuild_layer_index(layer_dir: Path, layer_name: str, description: str) -> str:
    """Rebuild a layer _index.md (lessons/, patterns/, decisions/, spine/).

    Same logic as rebuild_domain_index but for non-domain directories.
    """
    return rebuild_domain_index(layer_dir, layer_name, description)


def rebuild_backlog_index(backlog_dir: Path) -> None:
    """Rebuild wiki/backlog/_index.md and wiki/backlog/tasks/_index.md.

    Scans epics/, modules/, and tasks/ for .md files (excluding _index.md).
    Reads frontmatter and rebuilds table-based indexes.
    """
    milestones_dir = backlog_dir / "milestones"
    epics_dir = backlog_dir / "epics"
    tasks_dir = backlog_dir / "tasks"
    today = __import__("datetime").date.today().isoformat()

    # --- Collect milestones ---
    milestones = []
    if milestones_dir.exists():
        for md_file in sorted(milestones_dir.glob("*.md")):
            if md_file.name == "_index.md":
                continue
            text = md_file.read_text(encoding="utf-8")
            meta, _ = parse_frontmatter(text)
            if not meta:
                continue
            milestones.append({
                "title": meta.get("title", md_file.stem),
                "target_date": meta.get("target_date", ""),
                "status": meta.get("status", ""),
                "file": md_file.name,
                "epics": ", ".join(meta.get("epics", [])),
            })

    # --- Collect epics ---
    epics = []
    if epics_dir.exists():
        for md_file in sorted(epics_dir.rglob("*.md")):
            if md_file.name == "_index.md":
                continue
            text = md_file.read_text(encoding="utf-8")
            meta, _ = parse_frontmatter(text)
            if not meta:
                continue
            # Derive ID from filename (e.g. E001-foo.md → E001)
            stem = md_file.stem
            epic_id = stem.split("-")[0].upper() if "-" in stem else stem.upper()
            epics.append({
                "id": epic_id,
                "title": meta.get("title", stem),
                "priority": meta.get("priority", ""),
                "status": meta.get("status", ""),
                "readiness": meta.get("readiness", ""),
            })

    # --- Collect tasks ---
    tasks = []
    if tasks_dir.exists():
        for md_file in sorted(tasks_dir.rglob("*.md")):
            if md_file.name == "_index.md":
                continue
            text = md_file.read_text(encoding="utf-8")
            meta, _ = parse_frontmatter(text)
            if not meta:
                continue
            stem = md_file.stem
            task_id = stem.split("-")[0].upper() if "-" in stem else stem.upper()
            tasks.append({
                "id": task_id,
                "title": meta.get("title", stem),
                "priority": meta.get("priority", ""),
                "status": meta.get("status", ""),
                "stage": meta.get("stage", ""),
                "readiness": meta.get("readiness", ""),
                "epic": meta.get("epic", ""),
            })

    # --- Rebuild wiki/backlog/_index.md ---
    # Build filename lookup for epics
    epic_files = {}
    if epics_dir.exists():
        for md_file in sorted(epics_dir.rglob("*.md")):
            if md_file.name != "_index.md":
                text = md_file.read_text(encoding="utf-8")
                meta, _ = parse_frontmatter(text)
                if meta and meta.get("title"):
                    # Use relative path from epics_dir for subfolder support
                    epic_files[meta["title"]] = str(md_file.relative_to(epics_dir))

    epic_rows = "\n".join(
        f"| {e['id']} | [{e['title']}](epics/{epic_files.get(e['title'], '')}) | {e['priority']} | {e['status']} | {e['readiness']} |"
        if e['title'] in epic_files else
        f"| {e['id']} | {e['title']} | {e['priority']} | {e['status']} | {e['readiness']} |"
        for e in epics
    ) or "<!-- No epics yet -->"

    milestone_rows = "\n".join(
        f"| [{m['title']}](milestones/{m['file']}) | {m['target_date']} | {m['status']} | {m['epics']} |"
        for m in milestones
    ) or "<!-- No milestones yet -->"

    milestones_section = f"""## Milestones

| Milestone | Target | Status | Epics |
|-----------|--------|--------|-------|
{milestone_rows}

""" if milestones else ""

    # --- Collect loose reference pages at backlog root ---
    loose_pages = []
    for md_file in sorted(backlog_dir.glob("*.md")):
        if md_file.name == "_index.md":
            continue
        text = md_file.read_text(encoding="utf-8")
        meta, _ = parse_frontmatter(text)
        if meta and meta.get("title"):
            loose_pages.append({
                "title": meta["title"],
                "file": md_file.name,
            })

    loose_section = ""
    if loose_pages:
        loose_rows = "\n".join(
            f"- [{p['title']}]({p['file']})" for p in loose_pages
        )
        loose_section = f"""## References

{loose_rows}

"""

    backlog_index_content = f"""---
title: "Backlog"
type: index
domain: backlog
status: active
confidence: high
created: 2026-04-09
updated: {today}
sources: []
tags: [backlog, planning, epics, roadmap]
---

# Backlog

All planned work, organized by milestones, epics, modules, and tasks.

{milestones_section}## Epics

| ID | Epic | Priority | Status | Readiness |
|----|------|----------|--------|-----------|
{epic_rows}

{loose_section}## Modules

See [modules/](modules/)

## Tasks

See [tasks/_index.md](tasks/_index.md)
"""
    backlog_index_path = backlog_dir / "_index.md"
    backlog_index_path.write_text(backlog_index_content, encoding="utf-8")

    # --- Rebuild wiki/backlog/tasks/_index.md ---
    # Build filename lookup for tasks
    task_files = {}
    if tasks_dir.exists():
        for md_file in sorted(tasks_dir.rglob("*.md")):
            if md_file.name != "_index.md":
                text = md_file.read_text(encoding="utf-8")
                meta, _ = parse_frontmatter(text)
                if meta and meta.get("title"):
                    task_files[meta["title"]] = str(md_file.relative_to(tasks_dir))

    task_rows = "\n".join(
        f"| {t['id']} | [{t['title']}]({task_files.get(t['title'], '')}) | {t['priority']} | {t['status']} | {t['stage']} | {t['readiness']} | {t['epic']} |"
        if t['title'] in task_files else
        f"| {t['id']} | {t['title']} | {t['priority']} | {t['status']} | {t['stage']} | {t['readiness']} | {t['epic']} |"
        for t in tasks
    ) or "<!-- No tasks yet -->"

    tasks_index_content = f"""---
title: "Tasks"
type: index
domain: backlog
status: active
confidence: high
created: 2026-04-09
updated: {today}
sources: []
tags: [backlog, tasks]
---

# Tasks

| ID | Task | Priority | Status | Stage | Readiness | Epic |
|----|------|----------|--------|-------|-----------|------|
{task_rows}
"""
    tasks_index_path = tasks_dir / "_index.md"
    tasks_index_path.write_text(tasks_index_content, encoding="utf-8")


def rebuild_log_index(log_dir: Path) -> None:
    """Rebuild wiki/log/_index.md with a chronological table of log entries.

    Scans log_dir for .md files (excluding _index.md). Reads frontmatter.
    Table columns: Date, Title, Type (note_type), Tags.
    """
    today = __import__("datetime").date.today().isoformat()

    entries = []
    for md_file in sorted(log_dir.rglob("*.md"), reverse=True):
        if md_file.name == "_index.md":
            continue
        text = md_file.read_text(encoding="utf-8")
        meta, _ = parse_frontmatter(text)
        if not meta:
            continue
        date = str(meta.get("created", md_file.stem[:10] if len(md_file.stem) >= 10 else ""))
        title = meta.get("title", md_file.stem)
        note_type = meta.get("note_type", meta.get("type", ""))
        tags = meta.get("tags", [])
        tags_str = ", ".join(f"`{t}`" for t in tags) if tags else ""
        rel_path = str(md_file.relative_to(log_dir))
        entries.append({
            "date": date,
            "title": title,
            "type": note_type,
            "tags": tags_str,
            "file": rel_path,
        })

    rows = "\n".join(
        f"| {e['date']} | [{e['title']}]({e['file']}) | {e['type']} | {e['tags']} |"
        for e in entries
    ) or "<!-- No log entries yet -->"

    content = f"""---
title: "Log"
type: index
domain: log
status: active
confidence: high
created: 2026-04-09
updated: {today}
sources: []
tags: [log, directives, sessions]
---

# Log

Operator directives, session summaries, and task completion notes.

## Entries

| Date | Title | Type | Tags |
|------|-------|------|------|
{rows}
"""
    log_index_path = log_dir / "_index.md"
    log_index_path.write_text(content, encoding="utf-8")
