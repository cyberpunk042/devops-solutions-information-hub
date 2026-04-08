"""Wiki watcher service — detects changes and triggers pipeline actions.

Monitors raw/ and wiki/ for changes, then automatically:
- New file in raw/         → log it, report ready for synthesis
- Wiki page created/edited → run post-chain (index, manifest, validate, obsidian)
- Wiki page deleted        → run post-chain to clean up indexes
- Sync trigger             → run sync to Windows if configured

Can run as a foreground daemon or one-shot diff check.

Usage:
    python -m tools.watcher                      # One-shot: report changes since last check
    python -m tools.watcher --watch              # Daemon: watch and react to changes
    python -m tools.watcher --watch --interval 5 # Custom poll interval
    python -m tools.watcher --watch --sync       # Also trigger sync on wiki changes
    python -m tools.watcher --reset              # Reset change tracking baseline

Environment:
    WIKI_WATCH_INTERVAL  Override default poll interval (seconds)
"""

import argparse
import hashlib
import json
import os
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Set

from tools.common import get_project_root


# ---------------------------------------------------------------------------
# State tracking
# ---------------------------------------------------------------------------

STATE_FILE = ".watcher-state.json"


def _file_entry(path: Path, base: Path) -> Dict[str, Any]:
    """Create a file state entry."""
    try:
        stat = path.stat()
        return {
            "path": str(path.relative_to(base)),
            "mtime": stat.st_mtime,
            "size": stat.st_size,
        }
    except OSError:
        return {"path": str(path.relative_to(base)), "mtime": 0, "size": 0}


def scan_directory(directory: Path, base: Path, extensions: Set[str] = None) -> Dict[str, Dict]:
    """Scan a directory and return {relative_path: {mtime, size}} for all files."""
    if extensions is None:
        extensions = {".md", ".txt", ".json", ".yaml", ".yml"}

    entries = {}
    if not directory.exists():
        return entries

    for f in sorted(directory.rglob("*")):
        if not f.is_file():
            continue
        if f.name.startswith("."):
            continue
        if extensions and f.suffix.lower() not in extensions:
            continue
        rel = str(f.relative_to(base))
        entries[rel] = {
            "mtime": f.stat().st_mtime,
            "size": f.stat().st_size,
        }

    return entries


def compute_snapshot(project_root: Path) -> Dict[str, Dict]:
    """Compute full snapshot of raw/ and wiki/."""
    snapshot = {}
    snapshot.update(scan_directory(project_root / "raw", project_root))
    snapshot.update(scan_directory(project_root / "wiki", project_root))
    return snapshot


def load_state(project_root: Path) -> Optional[Dict]:
    """Load previous watcher state."""
    state_path = project_root / STATE_FILE
    if state_path.exists():
        try:
            return json.loads(state_path.read_text())
        except (json.JSONDecodeError, OSError):
            return None
    return None


def save_state(project_root: Path, snapshot: Dict, events: List[Dict] = None):
    """Save current watcher state."""
    state_path = project_root / STATE_FILE
    state = {
        "timestamp": datetime.now().isoformat(),
        "snapshot": snapshot,
        "last_events": events or [],
    }
    state_path.write_text(json.dumps(state, indent=2, default=str))


# ---------------------------------------------------------------------------
# Diff engine
# ---------------------------------------------------------------------------

def diff_snapshots(old: Dict[str, Dict], new: Dict[str, Dict]) -> List[Dict[str, Any]]:
    """Compare two snapshots and return list of change events."""
    events = []
    old_paths = set(old.keys())
    new_paths = set(new.keys())

    # New files
    for path in sorted(new_paths - old_paths):
        events.append({
            "type": "created",
            "path": path,
            "category": _categorize_path(path),
            "timestamp": datetime.now().isoformat(),
        })

    # Deleted files
    for path in sorted(old_paths - new_paths):
        events.append({
            "type": "deleted",
            "path": path,
            "category": _categorize_path(path),
            "timestamp": datetime.now().isoformat(),
        })

    # Modified files
    for path in sorted(old_paths & new_paths):
        if old[path]["mtime"] != new[path]["mtime"] or old[path]["size"] != new[path]["size"]:
            events.append({
                "type": "modified",
                "path": path,
                "category": _categorize_path(path),
                "timestamp": datetime.now().isoformat(),
            })

    return events


def _categorize_path(path: str) -> str:
    """Categorize a file path into an event category."""
    if path.startswith("raw/"):
        return "raw"
    if path.startswith("wiki/domains/"):
        return "wiki-page"
    if path.startswith("wiki/sources/"):
        return "wiki-source"
    if path.startswith("wiki/comparisons/"):
        return "wiki-comparison"
    if path.startswith("wiki/"):
        return "wiki-meta"
    return "other"


# ---------------------------------------------------------------------------
# Event handlers
# ---------------------------------------------------------------------------

def handle_events(events: List[Dict], project_root: Path,
                  auto_post: bool = True, auto_sync: bool = False,
                  verbose: bool = True) -> Dict[str, Any]:
    """Process detected events and trigger appropriate actions."""
    if not events:
        return {"actions": [], "events": 0}

    actions = []
    raw_created = [e for e in events if e["category"] == "raw" and e["type"] == "created"]
    wiki_changed = [e for e in events if e["category"].startswith("wiki") and e["type"] in ("created", "modified", "deleted")]

    # Report new raw files
    if raw_created and verbose:
        print(f"\n  New raw files ({len(raw_created)}):")
        for e in raw_created:
            print(f"    + {e['path']}")
        print("  → Ready for synthesis (use Claude Code to process)")
        actions.append({"action": "report_raw", "count": len(raw_created)})

    # Auto post-chain on wiki changes
    if wiki_changed and auto_post:
        if verbose:
            print(f"\n  Wiki changes ({len(wiki_changed)}):")
            for e in wiki_changed:
                symbol = {"created": "+", "modified": "~", "deleted": "-"}.get(e["type"], "?")
                print(f"    {symbol} {e['path']}")
            print("  → Running post-chain...")

        from tools.pipeline import post_chain
        report = post_chain(project_root, verbose=verbose)
        actions.append({"action": "post_chain", "result": report})

        # Auto sync after post-chain
        if auto_sync:
            if verbose:
                print("  → Syncing to Windows...")
            from tools.sync import get_sync_config, run_sync, save_sync_state
            config = get_sync_config(project_root)
            if config["target"]:
                result = run_sync(config, verbose=False)
                save_sync_state(project_root, result)
                actions.append({"action": "sync", "result": result})
                if verbose:
                    status = "OK" if result["ok"] else "FAILED"
                    print(f"  → Sync {status}")

    return {"actions": actions, "events": len(events)}


# ---------------------------------------------------------------------------
# Watch mode
# ---------------------------------------------------------------------------

def watch(project_root: Path, interval: int = 15,
          auto_post: bool = True, auto_sync: bool = False,
          verbose: bool = True):
    """Watch for changes and react. Runs until interrupted."""
    print(f"Wiki watcher started (interval: {interval}s)")
    print(f"  Watching: raw/, wiki/")
    print(f"  Auto post-chain: {'ON' if auto_post else 'OFF'}")
    print(f"  Auto sync:       {'ON' if auto_sync else 'OFF'}")
    print("  Press Ctrl+C to stop.\n")

    # Initialize baseline
    snapshot = compute_snapshot(project_root)
    save_state(project_root, snapshot)

    try:
        while True:
            time.sleep(interval)

            new_snapshot = compute_snapshot(project_root)
            events = diff_snapshots(snapshot, new_snapshot)

            if events:
                ts = datetime.now().strftime("%H:%M:%S")
                print(f"  [{ts}] {len(events)} change(s) detected")
                handle_events(events, project_root,
                              auto_post=auto_post, auto_sync=auto_sync,
                              verbose=verbose)
                save_state(project_root, new_snapshot, events)
                snapshot = new_snapshot

    except KeyboardInterrupt:
        print("\nWatcher stopped.")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Wiki watcher — detect changes and trigger pipeline actions",
    )
    parser.add_argument("--watch", "-w", action="store_true",
                        help="Watch for changes continuously")
    parser.add_argument("--interval", "-i", type=int,
                        default=int(os.environ.get("WIKI_WATCH_INTERVAL", "15")),
                        help="Poll interval in seconds (default: 15)")
    parser.add_argument("--sync", action="store_true",
                        help="Also trigger sync on wiki changes")
    parser.add_argument("--no-post", action="store_true",
                        help="Don't auto-run post-chain on wiki changes")
    parser.add_argument("--reset", action="store_true",
                        help="Reset change tracking baseline")
    parser.add_argument("--json", action="store_true",
                        help="JSON output")
    parser.add_argument("--quiet", "-q", action="store_true",
                        help="Minimal output")

    args = parser.parse_args()
    root = get_project_root()
    verbose = not args.quiet

    if args.reset:
        snapshot = compute_snapshot(root)
        save_state(root, snapshot)
        if verbose:
            print(f"Baseline reset ({len(snapshot)} files tracked)")
        sys.exit(0)

    if args.watch:
        watch(root, interval=args.interval,
              auto_post=not args.no_post, auto_sync=args.sync,
              verbose=verbose)
        sys.exit(0)

    # One-shot diff check
    state = load_state(root)
    new_snapshot = compute_snapshot(root)

    if state and "snapshot" in state:
        events = diff_snapshots(state["snapshot"], new_snapshot)
    else:
        # No baseline — everything is "new"
        events = []
        if verbose:
            print(f"No baseline. Tracking {len(new_snapshot)} files.")
            print("Run --reset to set baseline, then check again later.")

    save_state(root, new_snapshot, events)

    if args.json:
        print(json.dumps({"events": events, "total": len(events)}, indent=2, default=str))
    elif events:
        if verbose:
            print(f"Changes since last check ({len(events)}):")
            for e in events:
                symbol = {"created": "+", "modified": "~", "deleted": "-"}.get(e["type"], "?")
                print(f"  {symbol} [{e['category']}] {e['path']}")
        handle_events(events, root, auto_post=not args.no_post,
                      auto_sync=args.sync, verbose=verbose)
    else:
        if verbose:
            print("No changes detected.")

    sys.exit(0)


if __name__ == "__main__":
    main()
