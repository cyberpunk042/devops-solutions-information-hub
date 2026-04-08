"""Generate Obsidian [[wikilinks]] from wiki relationship data.

Bridges the ## Relationships format (openfleet-compatible plain text)
to [[wikilinks]] that Obsidian uses for graph view.

Usage:
    python3 tools/obsidian.py              # Generate/update backlinks
    python3 tools/obsidian.py --check      # Dry-run, report changes
    python3 tools/obsidian.py --clean      # Remove all ## Backlinks sections
    python3 tools/obsidian.py --wiki path/ # Custom wiki dir
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Set

from tools.common import (
    find_wiki_pages,
    get_project_root,
    parse_frontmatter,
    parse_relationships,
    parse_sections,
)
from tools.manifest import build_manifest


BACKLINKS_HEADER = "## Backlinks"


def build_title_lookup(manifest: Dict[str, Any]) -> Dict[str, Dict[str, str]]:
    """Build lookup: page title -> {path, slug, source_ids}.

    Also indexes by slug (filename stem) for fuzzy matching.
    """
    lookup: Dict[str, Dict[str, str]] = {}
    for page in manifest.get("pages", []):
        title = page.get("title", "")
        if not title:
            continue
        entry = {
            "path": page.get("path", ""),
            "slug": Path(page.get("path", "")).stem,
            "source_ids": [s.get("id", "") for s in page.get("sources", []) if isinstance(s, dict)],
        }
        lookup[title] = entry
        # Also index by slug for fuzzy matching
        slug = Path(page.get("path", "")).stem
        if slug and slug not in lookup:
            lookup[slug] = entry
    return lookup


def _resolve_target(target: str, lookup: Dict[str, Dict[str, str]]) -> str:
    """Resolve a relationship target to an Obsidian [[wikilink]].

    Priority:
    1. Direct title match
    2. Slug match (kebab-case filename stem)
    3. Source ID match (for DERIVED FROM: src-xxx)
    4. Unresolved -> [[target]] as-is (shows as unresolved in Obsidian)
    """
    # Direct title match
    if target in lookup:
        return f"[[{target}]]"

    # Slug match
    for title, info in lookup.items():
        if info.get("slug") == target:
            return f"[[{title}]]"

    # Source ID match
    if target.startswith("src-"):
        for title, info in lookup.items():
            if target in info.get("source_ids", []):
                return f"[[{title}]]"

    # Unresolved
    return f"[[{target}]]"


def _find_incoming_links(page_title: str, manifest: Dict[str, Any]) -> Set[str]:
    """Find all pages that reference this page in their relationships."""
    incoming: Set[str] = set()
    for page in manifest.get("pages", []):
        if page.get("title") == page_title:
            continue
        for rel in page.get("relationships", []):
            target = rel.get("target", "")
            if target == page_title:
                incoming.add(page["title"])
    return incoming


def generate_backlinks(
    text: str, manifest: Dict[str, Any], lookup: Dict[str, Dict[str, str]]
) -> str:
    """Generate or update ## Backlinks section in a wiki page.

    Parses ## Relationships to get outgoing links, also finds incoming
    links from manifest. Returns the full page text with ## Backlinks
    appended (or replaced if it already exists).
    """
    meta, body = parse_frontmatter(text)
    if not meta:
        return text

    page_title = meta.get("title", "")

    # Collect outgoing targets from ## Relationships
    sections = parse_sections(body)
    rel_text = sections.get("Relationships", "")
    rels = parse_relationships(rel_text)

    outgoing_links: List[str] = []
    for rel in rels:
        for target in rel["targets"]:
            wikilink = _resolve_target(target, lookup)
            if wikilink not in outgoing_links:
                outgoing_links.append(wikilink)

    # Collect incoming links (pages that reference this page)
    incoming_titles = _find_incoming_links(page_title, manifest)
    incoming_links: List[str] = []
    for title in sorted(incoming_titles):
        wl = f"[[{title}]]"
        if wl not in outgoing_links and wl not in incoming_links:
            incoming_links.append(wl)

    all_links = outgoing_links + incoming_links

    if not all_links:
        return text

    # Build backlinks section
    backlinks_content = f"\n\n{BACKLINKS_HEADER}\n\n" + "\n".join(all_links) + "\n"

    # Remove existing backlinks section if present
    text_without_backlinks = _strip_backlinks(text)

    return text_without_backlinks.rstrip() + backlinks_content


def _strip_backlinks(text: str) -> str:
    """Remove existing ## Backlinks section from text."""
    pattern = re.compile(
        r"\n*## Backlinks\n.*",
        re.DOTALL,
    )
    return pattern.sub("", text)


def clean_backlinks(wiki_dir: Path) -> int:
    """Remove ## Backlinks from all wiki pages. Returns count of modified files."""
    count = 0
    for md_file in find_wiki_pages(wiki_dir):
        text = md_file.read_text(encoding="utf-8")
        if BACKLINKS_HEADER in text:
            cleaned = _strip_backlinks(text).rstrip() + "\n"
            md_file.write_text(cleaned, encoding="utf-8")
            count += 1
    return count


def update_all_backlinks(wiki_dir: Path, check_only: bool = False) -> Dict[str, Any]:
    """Generate/update backlinks in all wiki pages.

    Returns report: {updated: [...], unchanged: [...], total: N}
    """
    manifest = build_manifest(wiki_dir)
    lookup = build_title_lookup(manifest)

    updated: List[str] = []
    unchanged: List[str] = []

    for md_file in find_wiki_pages(wiki_dir):
        text = md_file.read_text(encoding="utf-8")
        new_text = generate_backlinks(text, manifest, lookup)

        if new_text != text:
            if not check_only:
                md_file.write_text(new_text, encoding="utf-8")
            updated.append(str(md_file))
        else:
            unchanged.append(str(md_file))

    return {
        "updated": updated,
        "unchanged": unchanged,
        "total": len(updated) + len(unchanged),
    }


def main():
    parser = argparse.ArgumentParser(description="Generate Obsidian wikilinks from relationships")
    parser.add_argument("--check", action="store_true", help="Dry-run, report changes")
    parser.add_argument("--clean", action="store_true", help="Remove all ## Backlinks sections")
    parser.add_argument("--wiki", help="Wiki directory path")
    args = parser.parse_args()

    root = get_project_root()
    wiki_dir = Path(args.wiki) if args.wiki else root / "wiki"

    if args.clean:
        count = clean_backlinks(wiki_dir)
        print(f"Cleaned ## Backlinks from {count} files")
        return

    report = update_all_backlinks(wiki_dir, check_only=args.check)

    prefix = "[DRY RUN] " if args.check else ""
    print(f"{prefix}Backlinks: {len(report['updated'])} updated, {len(report['unchanged'])} unchanged")
    if report["updated"]:
        for f in report["updated"]:
            print(f"  {prefix}{'Would update' if args.check else 'Updated'}: {f}")


if __name__ == "__main__":
    main()
