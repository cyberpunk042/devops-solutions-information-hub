"""Sister-project browser — structured access to ecosystem projects' wikis.

Resolves the "how does the research wiki communicate with sister projects" gap.
Before this module, agents browsed OpenArms / OpenFleet / AICP / control-plane
with one-off Bash commands (ls, grep, cat) — manual, error-prone, and not
composable with the rest of the wiki's tooling.

This module reads sister projects declared in wiki/config/sister-projects.yaml
and exposes structured queries: list epics/tasks/logs/learnings, filter by
frontmatter fields (status, readiness, stage, tags), read specific docs with
truncation limits, and summarize across many files without blowing context.

Design:
- READ-ONLY. This wiki never writes to sister projects via this tool.
- Composable with gateway subcommands and MCP tools.
- Respects per-project layout (OpenArms uses wiki/; AICP uses docs/kb/).
- Applies read limits from sister-projects.yaml to prevent runaway reads.

CLI usage:
    python3 -m tools.sister_project list                        # list all sisters
    python3 -m tools.sister_project <name> info                 # show config
    python3 -m tools.sister_project <name> epics [--status X]   # list epics
    python3 -m tools.sister_project <name> tasks [--status X]   # list tasks
    python3 -m tools.sister_project <name> logs [--since DATE] [--limit N]
    python3 -m tools.sister_project <name> learnings            # list learning pages
    python3 -m tools.sister_project <name> read <path>          # read one file (truncated)
    python3 -m tools.sister_project <name> find <pattern>       # grep by filename pattern
    python3 -m tools.sister_project <name> grep <text>          # grep content
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

try:
    import yaml
except ImportError:
    print("PyYAML not installed. Run: pip3 install pyyaml", file=sys.stderr)
    sys.exit(1)

from tools.common import get_project_root, parse_frontmatter


def load_registry() -> Dict[str, Any]:
    """Load sister-projects.yaml registry."""
    root = get_project_root()
    registry_path = root / "wiki" / "config" / "sister-projects.yaml"
    if not registry_path.exists():
        return {"projects": {}, "limits": {}}
    return yaml.safe_load(registry_path.read_text(encoding="utf-8")) or {}


def resolve_project(name: str, registry: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """Look up a sister project by name; returns None if unknown."""
    return registry.get("projects", {}).get(name)


def _project_root(project_cfg: Dict[str, Any]) -> Path:
    """Return absolute path to the sister project's root directory."""
    return Path(project_cfg["path"]).expanduser().resolve()


def _wiki_root(project_cfg: Dict[str, Any]) -> Path:
    """Return absolute path to the sister project's wiki directory."""
    return _project_root(project_cfg) / project_cfg.get("wiki_dir", "wiki")


def _layout_dir(project_cfg: Dict[str, Any], dotted_key: str) -> Optional[Path]:
    """Resolve a dotted layout key like 'backlog.epics' to an absolute path."""
    layout = project_cfg.get("layout", {})
    parts = dotted_key.split(".")
    node: Any = layout
    for part in parts:
        if isinstance(node, dict) and part in node:
            node = node[part]
        else:
            return None
    if isinstance(node, str):
        return _wiki_root(project_cfg) / node
    return None


def list_projects(registry: Dict[str, Any]) -> List[Dict[str, Any]]:
    """List all registered sister projects with their description + accessibility."""
    result = []
    for name, cfg in registry.get("projects", {}).items():
        path = _project_root(cfg)
        result.append({
            "name": name,
            "description": cfg.get("description", ""),
            "path": str(path),
            "accessible": path.exists(),
            "wiki_dir": str(_wiki_root(cfg)) if path.exists() else None,
        })
    return result


def project_info(project_cfg: Dict[str, Any]) -> Dict[str, Any]:
    """Return full config for a sister project + accessibility check."""
    path = _project_root(project_cfg)
    wiki_path = _wiki_root(project_cfg)
    return {
        "description": project_cfg.get("description", ""),
        "path": str(path),
        "path_exists": path.exists(),
        "wiki_dir": str(wiki_path),
        "wiki_exists": wiki_path.exists(),
        "layout": project_cfg.get("layout", {}),
        "queryable_frontmatter": project_cfg.get("queryable_frontmatter", []),
        "patterns": project_cfg.get("patterns", {}),
    }


def _read_frontmatter(path: Path) -> Dict[str, Any]:
    """Safe frontmatter parse; returns empty dict on any failure."""
    try:
        text = path.read_text(encoding="utf-8")
        meta, _ = parse_frontmatter(text)
        return meta or {}
    except Exception:
        return {}


def _list_md_files(directory: Path, max_files: int, pattern: Optional[str] = None) -> List[Path]:
    """List .md files in a directory, optionally filtered by regex pattern."""
    if not directory.exists():
        return []
    files = []
    pat = re.compile(pattern) if pattern else None
    for f in sorted(directory.iterdir()):
        if not f.is_file() or f.suffix != ".md":
            continue
        if f.name == "_index.md":
            continue
        if pat and not pat.search(f.name):
            continue
        files.append(f)
        if len(files) >= max_files:
            break
    return files


def _summarize_page(path: Path, queryable_fields: List[str]) -> Dict[str, Any]:
    """Return a compact summary: name + queryable frontmatter fields + title."""
    meta = _read_frontmatter(path)
    summary = {"file": path.name, "title": meta.get("title", path.stem)}
    for field in queryable_fields:
        if field in meta:
            summary[field] = meta[field]
    return summary


def list_epics(project_cfg: Dict[str, Any], status_filter: Optional[str] = None, max_files: int = 50) -> List[Dict[str, Any]]:
    """List epics; optionally filter by status.

    When a filter is active, scan ALL files first and apply max_files AFTER
    filtering (otherwise a filter that matches late-sorted files returns 0).
    """
    epics_dir = _layout_dir(project_cfg, "backlog.epics")
    if epics_dir is None:
        return []
    fields = project_cfg.get("queryable_frontmatter", [])
    scan_cap = 1000 if status_filter else max_files
    files = _list_md_files(epics_dir, scan_cap)
    result = []
    for f in files:
        summary = _summarize_page(f, fields)
        if status_filter and summary.get("status") != status_filter:
            continue
        result.append(summary)
        if len(result) >= max_files:
            break
    return result


def list_tasks(project_cfg: Dict[str, Any], status_filter: Optional[str] = None, epic_filter: Optional[str] = None, max_files: int = 50) -> List[Dict[str, Any]]:
    """List tasks; optionally filter by status and/or epic.

    When any filter is active, scan ALL files first and apply max_files AFTER
    filtering (otherwise an epic filter matching late-sorted tasks like T107+
    returns 0 because the first 50 T-files don't include them).
    """
    tasks_dir = _layout_dir(project_cfg, "backlog.tasks")
    if tasks_dir is None:
        return []
    fields = project_cfg.get("queryable_frontmatter", [])
    has_filter = bool(status_filter or epic_filter)
    scan_cap = 1000 if has_filter else max_files
    files = _list_md_files(tasks_dir, scan_cap)
    result = []
    for f in files:
        summary = _summarize_page(f, fields)
        if status_filter and summary.get("status") != status_filter:
            continue
        if epic_filter and summary.get("epic") != epic_filter:
            continue
        result.append(summary)
        if len(result) >= max_files:
            break
    return result


def list_logs(project_cfg: Dict[str, Any], since: Optional[str] = None, limit: int = 20) -> List[Dict[str, Any]]:
    """List dated logs; optionally filter to entries on/after `since` (YYYY-MM-DD)."""
    logs_dir = _layout_dir(project_cfg, "logs")
    if logs_dir is None:
        return []
    fields = project_cfg.get("queryable_frontmatter", [])
    files = sorted(
        (f for f in logs_dir.iterdir() if f.is_file() and f.suffix == ".md" and f.name != "_index.md"),
        reverse=True,  # newest first
    )
    result = []
    for f in files:
        date_match = re.match(r"(\d{4}-\d{2}-\d{2})", f.name)
        file_date = date_match.group(1) if date_match else None
        if since and file_date and file_date < since:
            continue
        summary = _summarize_page(f, fields)
        summary["date"] = file_date
        result.append(summary)
        if len(result) >= limit:
            break
    return result


def list_learnings(project_cfg: Dict[str, Any], max_files: int = 50) -> List[Dict[str, Any]]:
    """List distilled learnings (lessons, patterns, agent-behavior findings).

    OpenArms keeps these in wiki/domains/learnings/; the layout key is
    `domains.learnings`. Returns a compact summary per file.
    """
    learnings_dir = _layout_dir(project_cfg, "domains.learnings")
    if learnings_dir is None:
        return []
    fields = project_cfg.get("queryable_frontmatter", [])
    files = _list_md_files(learnings_dir, max_files)
    return [_summarize_page(f, fields) for f in files]


def read_doc(project_cfg: Dict[str, Any], relative_path: str, max_bytes: int = 20000) -> Dict[str, Any]:
    """Read a single doc from the sister project, capped at max_bytes.

    `relative_path` is interpreted relative to the project root (NOT wiki root),
    so callers can read CLAUDE.md, AGENTS.md, wiki/...,
    docs/... transparently.
    """
    root = _project_root(project_cfg)
    target = (root / relative_path).resolve()
    # Safety: reject paths that escape the project root
    try:
        target.relative_to(root)
    except ValueError:
        return {"error": f"Path escapes project root: {relative_path}", "path": relative_path}
    if not target.exists():
        return {"error": "Not found", "path": str(target)}
    if not target.is_file():
        return {"error": "Not a file (is a directory?)", "path": str(target)}

    raw = target.read_bytes()
    size = len(raw)
    truncated = size > max_bytes
    content = raw[:max_bytes].decode("utf-8", errors="replace")

    meta = _read_frontmatter(target) if target.suffix == ".md" else {}
    return {
        "path": str(target.relative_to(root)),
        "size_bytes": size,
        "truncated": truncated,
        "bytes_returned": min(size, max_bytes),
        "frontmatter": meta,
        "content": content,
    }


def find_by_filename(project_cfg: Dict[str, Any], pattern: str, max_results: int = 50) -> List[str]:
    """Find files under the sister project whose filenames match `pattern` (regex)."""
    root = _project_root(project_cfg)
    if not root.exists():
        return []
    pat = re.compile(pattern)
    results = []
    max_depth = 4
    for md in root.rglob("*"):
        if not md.is_file():
            continue
        # depth guard
        depth = len(md.relative_to(root).parts)
        if depth > max_depth:
            continue
        if pat.search(md.name):
            results.append(str(md.relative_to(root)))
            if len(results) >= max_results:
                break
    return results


def grep_content(project_cfg: Dict[str, Any], text: str, max_results: int = 20) -> List[Dict[str, Any]]:
    """Grep sister-project .md files for literal `text`; returns path + matching lines.

    Scope: wiki_dir only (not full project root — avoids code files, dist/, node_modules/).
    """
    wiki = _wiki_root(project_cfg)
    if not wiki.exists():
        return []
    results = []
    text_lower = text.lower()
    for md in wiki.rglob("*.md"):
        try:
            content = md.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        matches = []
        for i, line in enumerate(content.split("\n"), 1):
            if text_lower in line.lower():
                matches.append({"line": i, "text": line.strip()[:200]})
                if len(matches) >= 3:  # cap per file
                    break
        if matches:
            results.append({
                "path": str(md.relative_to(_project_root(project_cfg))),
                "matches": matches,
            })
            if len(results) >= max_results:
                break
    return results


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Sister-project browser — structured access to ecosystem projects' wikis",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("project", nargs="?", help="Sister project name (or 'list' to list all)")
    parser.add_argument("action", nargs="?", help="Action: info, epics, tasks, logs, learnings, read, find, grep")
    parser.add_argument("arg", nargs="?", help="Argument for the action (path, pattern, or text)")
    parser.add_argument("--status", help="Filter by status (for epics/tasks)")
    parser.add_argument("--epic", help="Filter tasks by epic")
    parser.add_argument("--since", help="Filter logs to entries on/after this date (YYYY-MM-DD)")
    parser.add_argument("--limit", type=int, default=20, help="Max results to return")
    parser.add_argument("--json", action="store_true", help="Output JSON instead of human-readable")
    args = parser.parse_args()

    registry = load_registry()

    if args.project in (None, "list", "--help"):
        projects = list_projects(registry)
        if args.json:
            print(json.dumps(projects, indent=2, default=str))
        else:
            print(f"\nSister Projects ({len(projects)})")
            print("=" * 60)
            for p in projects:
                status = "✓" if p["accessible"] else "✗ (not accessible)"
                print(f"  {status}  {p['name']:20s}  {p['description']}")
            print()
            print("Usage: python3 -m tools.sister_project <name> <action>")
            print("Actions: info | epics | tasks | logs | learnings | read <path> | find <pattern> | grep <text>")
        return

    project_cfg = resolve_project(args.project, registry)
    if project_cfg is None:
        print(f"Unknown sister project: {args.project}", file=sys.stderr)
        print(f"Known: {', '.join(registry.get('projects', {}).keys())}", file=sys.stderr)
        sys.exit(1)

    if not _project_root(project_cfg).exists():
        print(f"Sister project '{args.project}' path does not exist: {_project_root(project_cfg)}", file=sys.stderr)
        sys.exit(1)

    limits = registry.get("limits", {})
    max_files = limits.get("max_files_listed", 50)
    max_bytes = limits.get("max_file_bytes", 20000)

    action = args.action or "info"

    if action == "info":
        result = project_info(project_cfg)
    elif action == "epics":
        result = list_epics(project_cfg, status_filter=args.status, max_files=max_files)
    elif action == "tasks":
        result = list_tasks(project_cfg, status_filter=args.status, epic_filter=args.epic, max_files=max_files)
    elif action == "logs":
        result = list_logs(project_cfg, since=args.since, limit=args.limit)
    elif action == "learnings":
        result = list_learnings(project_cfg, max_files=max_files)
    elif action == "read":
        if not args.arg:
            print("Usage: sister_project <name> read <relative/path.md>", file=sys.stderr)
            sys.exit(1)
        result = read_doc(project_cfg, args.arg, max_bytes=max_bytes)
    elif action == "find":
        if not args.arg:
            print("Usage: sister_project <name> find <regex-pattern>", file=sys.stderr)
            sys.exit(1)
        result = find_by_filename(project_cfg, args.arg, max_results=args.limit)
    elif action == "grep":
        if not args.arg:
            print("Usage: sister_project <name> grep <text>", file=sys.stderr)
            sys.exit(1)
        result = grep_content(project_cfg, args.arg, max_results=args.limit)
    else:
        print(f"Unknown action: {action}", file=sys.stderr)
        sys.exit(1)

    if args.json:
        print(json.dumps(result, indent=2, default=str))
    else:
        # Human-readable output per action shape
        if isinstance(result, list):
            print(f"\n{args.project} / {action} — {len(result)} item(s)")
            print("=" * 60)
            for item in result:
                if isinstance(item, dict):
                    # Epics/tasks/logs summary
                    title = item.get("title", item.get("file", "?"))
                    bits = [title]
                    for f in ("status", "readiness", "current_stage", "epic", "date"):
                        if f in item:
                            bits.append(f"{f}={item[f]}")
                    print(f"  {' | '.join(bits)}")
                else:
                    print(f"  {item}")
            print()
        elif isinstance(result, dict) and "content" in result:
            # read action
            print(f"\n=== {result['path']} ({result['size_bytes']} bytes, truncated={result['truncated']}) ===\n")
            if result.get("frontmatter"):
                print(f"Frontmatter: {json.dumps(result['frontmatter'], default=str)}\n")
            print(result["content"])
        else:
            print(json.dumps(result, indent=2, default=str))


if __name__ == "__main__":
    main()
