"""Wiki health checks CLI.

Checks for dead relationships, stale pages, thin content, orphan pages,
and domain health. Outputs structured JSON or human-readable reports.

Usage:
    python3 tools/lint.py                         # Human-readable summary
    python3 tools/lint.py --report                # JSON report
    python3 tools/lint.py --summary               # Human-readable summary
    python3 tools/lint.py --config path/to/config # Custom config
    python3 tools/lint.py --fix                   # Auto-fix where possible

Exit code: 0 if no issues, 1 if issues found.
"""

import argparse
import json
import sys
from dataclasses import dataclass
from datetime import date, timedelta
from pathlib import Path
from typing import Any, Dict, List, Optional, Set

from tools.common import (
    find_wiki_pages,
    get_project_root,
    load_config,
    parse_frontmatter,
    parse_relationships,
    parse_sections,
    word_count,
)


@dataclass
class LintConfig:
    stale_threshold_days: int
    min_summary_words: int
    min_deep_analysis_words: int
    min_relationships: int
    min_domain_pages: int
    min_cross_domain_rels: int
    similarity_threshold: float


def _collect_page_titles(pages: List[Path]) -> Set[str]:
    """Build a set of all page titles from frontmatter."""
    titles: Set[str] = set()
    for page in pages:
        try:
            text = page.read_text(encoding="utf-8")
            meta, _ = parse_frontmatter(text)
            title = meta.get("title", "")
            if title:
                titles.add(title.strip())
            # Also add the stem as a fallback
            titles.add(page.stem)
        except Exception:
            pass
    return titles


def _strip_context(target: str) -> str:
    """Extract the canonical page reference from a relationship target.

    Handles:
    - Parenthetical context: 'Serverless Patterns (different trade-offs)' -> 'Serverless Patterns'
    - Em-dash comments: '[[slug|Title]] — explanation' -> '[[slug|Title]]'
    - Hyphen comments: '[[slug|Title]] - explanation' -> '[[slug|Title]]'
    - Wikilink display titles: '[[slug|Title]]' -> 'Title' (for title lookup)
    - Bare wikilinks: '[[Title]]' -> 'Title'
    """
    target = target.strip()

    # Strip em-dash or hyphen trailing comment (after wikilink ends or plain text)
    # Look for ] ] followed by space-dash-space or space-emdash-space
    for sep in [" — ", " - ", " – "]:
        if sep in target:
            target = target.split(sep, 1)[0].strip()
            break

    # Strip parenthetical context
    paren_idx = target.find("(")
    if paren_idx > 0:
        target = target[:paren_idx].strip()

    # Extract title/slug from wikilink [[slug|title]] or [[title]]
    if target.startswith("[[") and target.endswith("]]"):
        inner = target[2:-2]
        # If [[slug|title]], return the TITLE side for title lookup
        if "|" in inner:
            return inner.split("|", 1)[1].strip()
        return inner.strip()

    return target


def _check_dead_relationships(
    pages: List[Path], known_titles: Set[str]
) -> List[Dict[str, str]]:
    """Find relationship targets that don't resolve to any known page title."""
    dead: List[Dict[str, str]] = []
    for page in pages:
        try:
            text = page.read_text(encoding="utf-8")
            meta, body = parse_frontmatter(text)
            if not meta:
                continue
            source_title = meta.get("title", page.stem)
            sections = parse_sections(body)
            rel_text = sections.get("Relationships", "")
            if not rel_text:
                continue
            rels = parse_relationships(rel_text)
            for rel in rels:
                # Extract slugs from the raw line's wikilinks — _split_targets strips them
                raw_line = rel.get("raw", "")
                raw_slugs = set()
                for wl_match in re.finditer(r'\[\[([^\]]+?)\]\]', raw_line):
                    inner = wl_match.group(1)
                    if "|" in inner:
                        raw_slugs.add(inner.split("|", 1)[0].strip())

                for target in rel["targets"]:
                    full_target = target.strip()
                    clean_target = _strip_context(target)

                    # If any wikilink slug on this line resolves, consider the target valid
                    if any(s in known_titles for s in raw_slugs):
                        # Only skip if the line has ONE target or all targets resolve
                        # Simple heuristic: if slugs resolve and this target's clean form is a display title, skip
                        if clean_target in [t.split("|")[1].strip() if "|" in t else t for t in [inner for wl in re.finditer(r'\[\[([^\]]+?)\]\]', raw_line) for inner in [wl.group(1)]]]:
                            continue

                    # Match if any form resolves
                    if full_target in known_titles or clean_target in known_titles:
                        continue
                    # Skip bare source IDs (not in wikilink format)
                    if clean_target.startswith("src-") or full_target.startswith("src-"):
                        continue

                    dead.append({
                        "source": source_title,
                        "verb": rel["verb"],
                        "target": clean_target,
                    })
        except Exception:
            pass
    return dead


def _check_stale_pages(
    pages: List[Path], threshold_days: int
) -> List[Dict[str, str]]:
    """Find pages not updated within threshold_days that aren't marked stale."""
    stale: List[Dict[str, str]] = []
    cutoff = date.today() - timedelta(days=threshold_days)
    for page in pages:
        try:
            text = page.read_text(encoding="utf-8")
            meta, _ = parse_frontmatter(text)
            if not meta:
                continue
            status = meta.get("status", "")
            if status == "stale":
                continue
            updated = meta.get("updated")
            if updated is None:
                continue
            # updated may be a date object or string
            if isinstance(updated, str):
                try:
                    updated_date = date.fromisoformat(updated)
                except ValueError:
                    continue
            elif isinstance(updated, date):
                updated_date = updated
            else:
                continue
            if updated_date < cutoff:
                stale.append({
                    "title": meta.get("title", page.stem),
                    "updated": str(updated_date),
                })
        except Exception:
            pass
    return stale


def _check_thin_pages(
    pages: List[Path],
    min_summary_words: int,
    min_deep_analysis_words: int,
) -> List[Dict[str, Any]]:
    """Find pages with insufficient content in key sections."""
    thin: List[Dict[str, Any]] = []
    # Types that require Deep Analysis
    deep_analysis_types = {"concept", "deep-dive", "comparison"}
    # Types that are intentionally thin — skip thin-page checks
    # (OpenArms correction 2026-04-16: task pages are 20-50 lines by design)
    thin_exempt_types = {"task", "note", "module"}
    for page in pages:
        try:
            text = page.read_text(encoding="utf-8")
            meta, body = parse_frontmatter(text)
            if not meta:
                continue
            page_type = meta.get("type", "")
            title = meta.get("title", page.stem)
            # Skip thin-page checks for types that are intentionally brief
            if page_type in thin_exempt_types:
                continue
            sections = parse_sections(body)

            # Check Summary word count
            summary = sections.get("Summary", "")
            summary_wc = word_count(summary) if summary else 0
            if summary_wc < min_summary_words and summary_wc > 0:
                thin.append({
                    "title": title,
                    "type": page_type,
                    "issue": "thin_summary",
                    "summary_words": summary_wc,
                    "deep_analysis_words": None,
                })

            # Check Deep Analysis word count for relevant types
            if page_type in deep_analysis_types:
                deep = sections.get("Deep Analysis", "")
                deep_wc = word_count(deep) if deep else 0
                if deep_wc < min_deep_analysis_words:
                    thin.append({
                        "title": title,
                        "type": page_type,
                        "issue": "thin_deep_analysis",
                        "summary_words": summary_wc,
                        "deep_analysis_words": deep_wc,
                    })
        except Exception:
            pass
    return thin


def _check_filename_hygiene(
    pages: List[Path],
) -> List[Dict[str, Any]]:
    """Find pages with non-ASCII or non-standard characters in filenames."""
    import re
    issues: List[Dict[str, Any]] = []
    for page in pages:
        name = page.name
        # Check for non-ASCII (em-dash, special chars)
        if not name.isascii():
            issues.append({"file": name, "issue": "non-ASCII characters"})
        # Check for plus signs
        elif "+" in name:
            issues.append({"file": name, "issue": "plus sign in filename"})
        # Check for parentheses (except in titles like "($0 Target)" which are ok in frontmatter but bad in filenames)
        elif "(" in name or ")" in name:
            issues.append({"file": name, "issue": "parentheses in filename"})
    return issues


def _check_queue_drift(
    pages: List[Path],
    queue_path: Path,
) -> List[Dict[str, Any]]:
    """Detect drift between the operator-decision-queue and home-page resolutions.

    The queue at wiki/backlog/operator-decision-queue.md tracks operator
    decisions across the wiki. Each entry links to a "source page" where
    the question is load-bearing. Resolutions can land in either place:

    1. In the queue table (struck-through with `~~N~~` and `**RESOLVED:**`)
    2. In the home page (struck-through `[!question] ~~...~~ **RESOLVED:**`
       callout)

    Drift = the two are out of sync. Specifically, this check flags:

    - **drift_home_resolved_queue_open**: the queue lists question N as OPEN
      (no strikethrough on the row number), but the linked source page
      contains `[!question] ~~...~~ **RESOLVED:**` callouts. Operator should
      verify whether one of those resolved callouts corresponds to the open
      queue entry and sync if so.

    Returns advisory issues — not blocking. Designed to prevent recurrence
    of the queue-drift pattern observed during the 2026-04-15 session
    (P2-P5 questions were all already resolved inline; queue had not been
    synced — 36 entries needed propagation).
    """
    if not queue_path.exists():
        return []

    import re as _re
    issues: List[Dict[str, Any]] = []

    try:
        queue_text = queue_path.read_text(encoding="utf-8")
    except Exception:
        return []

    # Build slug → page-path mapping for source-page resolution
    slug_to_path: Dict[str, Path] = {}
    for page in pages:
        slug_to_path[page.stem] = page

    # Parse queue rows. Each row looks like:
    #   | <number_or_~~strikethrough~~> | <question or RESOLVED text> | [[slug|title]] |
    # An OPEN row has a bare integer between pipes:  | 9 |
    # A RESOLVED row has strikethrough:              | ~~9~~ |
    open_row_re = _re.compile(r"^\|\s*(\d+[a-z]?)\s*\|", _re.MULTILINE)
    open_numbers: List[str] = open_row_re.findall(queue_text)

    def _normalize(text: str) -> str:
        """Lowercase + strip punctuation + collapse whitespace for fuzzy matching."""
        lower = _re.sub(r"[^\w\s]", " ", text.lower())
        return _re.sub(r"\s+", " ", lower).strip()

    def _token_overlap(a: str, b: str, min_ratio: float = 0.5) -> bool:
        """True if normalized `a` and `b` share at least min_ratio of a's content words.

        Content words = tokens ≥4 chars (filters out stop-words like "the",
        "is", "a"). Useful for matching a queue question ("Optimal context
        budget per tier") against a callout's strikethrough text.
        """
        a_tokens = {t for t in _normalize(a).split() if len(t) >= 4}
        b_tokens = {t for t in _normalize(b).split() if len(t) >= 4}
        if not a_tokens:
            return False
        overlap = len(a_tokens & b_tokens) / len(a_tokens)
        return overlap >= min_ratio

    # For each line that starts with "| <bare-number> |", capture the row
    # and its wikilink target (last `[[...]]` on the line is the source page)
    for line in queue_text.split("\n"):
        m = _re.match(r"^\|\s*(\d+[a-z]?)\s*\|(.*)$", line)
        if not m:
            continue
        number = m.group(1)
        rest = m.group(2)
        # Find the last wikilink on the row — it's the source-page link
        wikilinks = _re.findall(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]", rest)
        if not wikilinks:
            continue
        source_slug = wikilinks[-1]

        # Extract the question text from the row (first pipe-separated cell after number)
        # Row shape: | N | QUESTION TEXT | [[slug|...]] | ... |
        row_cells = [c.strip() for c in rest.split("|")]
        question_text = row_cells[0] if row_cells else ""

        # Resolve to a page path
        page = slug_to_path.get(source_slug)
        if page is None:
            continue

        # Read source page; look for resolved-question callouts
        try:
            page_text = page.read_text(encoding="utf-8")
        except Exception:
            continue

        # `> [!question] ~~...~~` — extract the strikethrough text from each callout
        callout_re = _re.compile(
            r"^>\s*\[!question\]\s*(?:\**)~~([^~]+)~~", _re.MULTILINE
        )
        strikethrough_texts = callout_re.findall(page_text)

        # Match ONLY if a strikethrough callout's text overlaps the queue question.
        # Reduces false positives when the page has OTHER resolved questions.
        matching = [t for t in strikethrough_texts if _token_overlap(question_text, t)]
        resolved_count = len(matching)

        if resolved_count > 0:
            issues.append({
                "queue_number": number,
                "source_page": source_slug,
                "resolved_callouts_in_page": resolved_count,
                "matched_callout_text": matching[0][:80] + ("..." if len(matching[0]) > 80 else ""),
                "hint": (
                    f"Queue Q{number} ('{question_text[:60]}...') is OPEN but {source_slug} "
                    f"contains a matching resolved [!question] callout ('{matching[0][:60]}...'). "
                    f"Verify if one of them resolves Q{number} and sync the queue."
                ),
            })

    return issues


def _check_unstyled_pages(
    pages: List[Path],
    min_lines: int = 80,
) -> List[Dict[str, Any]]:
    """Find content pages above min_lines with zero Obsidian callouts."""
    # Types that should have callout styling when long enough
    styled_types = {
        "concept", "pattern", "lesson", "decision", "comparison",
        "deep-dive", "domain-overview",
    }
    unstyled: List[Dict[str, Any]] = []
    for page in pages:
        try:
            text = page.read_text(encoding="utf-8")
            meta, body = parse_frontmatter(text)
            if not meta:
                continue
            page_type = meta.get("type", "")
            if page_type not in styled_types:
                continue
            lines = text.count("\n") + 1
            if lines < min_lines:
                continue
            # Check for Obsidian callouts
            if "> [!" not in body:
                unstyled.append({
                    "title": meta.get("title", page.stem),
                    "type": page_type,
                    "lines": lines,
                })
        except Exception:
            pass
    return unstyled


def _check_orphan_pages(
    pages: List[Path], wiki_dir: Path
) -> List[str]:
    """Find pages not listed in any _index.md file."""
    # Collect all page titles referenced in _index.md files
    # Check both markdown links [Title](file.md) and wikilinks [[Title]]
    referenced_files: Set[str] = set()
    referenced_titles: Set[str] = set()

    import re
    for index_file in wiki_dir.rglob("_index.md"):
        try:
            content = index_file.read_text(encoding="utf-8")
            # Markdown link patterns: [Title](filename.md)
            for match in re.finditer(r"\[([^\]]+)\]\(([^)]+\.md)\)", content):
                linked_file = match.group(2)
                resolved = (index_file.parent / linked_file).resolve()
                referenced_files.add(str(resolved))
                referenced_titles.add(match.group(1).strip())
            # Wikilink patterns: [[Page Title]] or [[filename|Page Title]]
            for match in re.finditer(r"\[\[([^\]]+)\]\]", content):
                inner = match.group(1).strip()
                if '|' in inner:
                    # [[filename|title]] — index both filename stem and display title
                    parts = inner.split('|', 1)
                    referenced_titles.add(parts[0].strip())
                    referenced_titles.add(parts[1].strip())
                else:
                    referenced_titles.add(inner)
        except Exception:
            pass

    # Structural files that are not expected to be in any _index.md
    structural_names = {"index.md", "agent-directive.md"}

    orphans: List[str] = []
    for page in pages:
        if page.name in structural_names:
            continue
        resolved = str(page.resolve())
        try:
            text = page.read_text(encoding="utf-8")
            meta, _ = parse_frontmatter(text)
            title = meta.get("title", page.stem) if meta else page.stem
        except Exception:
            title = page.stem
        # Check both file path and title references
        if resolved not in referenced_files and title not in referenced_titles:
            orphans.append(title)
    return orphans


def _check_domain_health(
    pages: List[Path],
    min_domain_pages: int,
    min_cross_domain_rels: int,
) -> List[Dict[str, Any]]:
    """Check domain-level health: page counts and cross-domain relationships."""
    # Group pages by domain
    domain_pages: Dict[str, List[Path]] = {}
    domain_titles: Dict[str, Set[str]] = {}

    for page in pages:
        try:
            text = page.read_text(encoding="utf-8")
            meta, _ = parse_frontmatter(text)
            if not meta:
                continue
            domain = meta.get("domain", "unknown")
            title = meta.get("title", page.stem)
            domain_pages.setdefault(domain, []).append(page)
            domain_titles.setdefault(domain, set()).add(title)
        except Exception:
            pass

    # Build a global title->domain map
    title_to_domain: Dict[str, str] = {}
    for domain, titles in domain_titles.items():
        for t in titles:
            title_to_domain[t] = domain

    domain_health: List[Dict[str, Any]] = []
    for domain, dpages in domain_pages.items():
        issues: List[str] = []
        page_count = len(dpages)

        if page_count < min_domain_pages:
            issues.append(f"too_few_pages ({page_count} < {min_domain_pages})")

        # Count cross-domain relationships
        cross_domain_count = 0
        for page in dpages:
            try:
                text = page.read_text(encoding="utf-8")
                meta, body = parse_frontmatter(text)
                if not meta:
                    continue
                sections = parse_sections(body)
                rel_text = sections.get("Relationships", "")
                if not rel_text:
                    continue
                rels = parse_relationships(rel_text)
                for rel in rels:
                    for target in rel["targets"]:
                        clean = _strip_context(target)
                        if clean.startswith("src-"):
                            continue
                        target_domain = title_to_domain.get(clean)
                        if target_domain and target_domain != domain:
                            cross_domain_count += 1
            except Exception:
                pass

        if cross_domain_count < min_cross_domain_rels:
            issues.append(
                f"too_few_cross_domain_relationships ({cross_domain_count} < {min_cross_domain_rels})"
            )

        if issues:
            domain_health.append({
                "domain": domain,
                "page_count": page_count,
                "cross_domain_relationships": cross_domain_count,
                "issues": issues,
            })

    return domain_health


def lint_wiki(wiki_dir: Path, config: LintConfig) -> Dict[str, Any]:
    """Run all wiki health checks and return a structured report.

    Args:
        wiki_dir: Directory containing wiki markdown files.
        config: LintConfig with thresholds and limits.

    Returns:
        Dict with keys: orphan_pages, dead_relationships, stale_pages,
        thin_pages, domain_health, summary.
    """
    skip_dirs = {"config", ".obsidian", ".evolve-queue"}
    pages = []
    for md_file in sorted(wiki_dir.rglob("*.md")):
        if md_file.name == "_index.md":
            continue
        if any(d in skip_dirs for d in md_file.relative_to(wiki_dir).parts):
            continue
        pages.append(md_file)

    known_titles = _collect_page_titles(pages)

    dead_relationships = _check_dead_relationships(pages, known_titles)
    stale_pages = _check_stale_pages(pages, config.stale_threshold_days)
    thin_pages = _check_thin_pages(
        pages,
        config.min_summary_words,
        config.min_deep_analysis_words,
    )
    orphan_pages = _check_orphan_pages(pages, wiki_dir)
    domain_health = _check_domain_health(
        pages,
        config.min_domain_pages,
        config.min_cross_domain_rels,
    )
    unstyled_pages = _check_unstyled_pages(pages)
    filename_issues = _check_filename_hygiene(pages)
    standards_issues = _check_standards_exemplars(pages)
    queue_drift = _check_queue_drift(
        pages,
        wiki_dir / "backlog" / "operator-decision-queue.md",
    )
    unsolicited_caps = _check_unsolicited_caps(wiki_dir.parent / "tools")

    total_issues = (
        len(dead_relationships)
        + len(stale_pages)
        + len(thin_pages)
        + len(orphan_pages)
        + sum(len(d["issues"]) for d in domain_health)
    )
    # Unstyled pages, standards issues, queue drift, unsolicited caps are
    # advisory — not counted in total_issues (won't cause `pipeline post` to fail)

    return {
        "orphan_pages": orphan_pages,
        "dead_relationships": dead_relationships,
        "stale_pages": stale_pages,
        "thin_pages": thin_pages,
        "unstyled_pages": unstyled_pages,
        "filename_issues": filename_issues,
        "standards_issues": standards_issues,
        "queue_drift": queue_drift,
        "unsolicited_caps": unsolicited_caps,
        "domain_health": domain_health,
        "summary": {
            "pages_scanned": len(pages),
            "total_issues": total_issues,
            "dead_relationships": len(dead_relationships),
            "stale_pages": len(stale_pages),
            "thin_pages": len(thin_pages),
            "orphan_pages": len(orphan_pages),
            "unstyled_pages": len(unstyled_pages),
            "standards_issues": len(standards_issues),
            "queue_drift": len(queue_drift),
            "unsolicited_caps": len(unsolicited_caps),
            "domain_health_issues": sum(len(d["issues"]) for d in domain_health),
        },
    }


def _check_unsolicited_caps(tools_dir: Path) -> List[Dict[str, str]]:
    """Advisory lint — flag Python function parameters that default to caps.

    Scans tools/*.py for function parameter defaults whose NAME matches common
    cap-semantic patterns (max_*, limit, truncate, head_limit, cap_*) and whose
    DEFAULT VALUE is a positive integer or truthy literal. Such defaults violate
    the 2026-04-15 operator directive:

        "no caps, no compacting, read full content always"
        (see raw/notes/2026-04-15-directive-no-caps-no-compact-read-full.md)

    Caps must be OPT-IN by caller, never defaulted in the function signature.
    This is the Infrastructure-Over-Instructions implementation of the directive
    — the rule becomes a standing structural check, not a prose memory.

    Known allowlisted cases: pagination params in API-adjacent code where
    caller-opt-out is impractical (e.g. external GitHub API calls). These can
    be suppressed with a `# noqa: nocaps` trailing comment on the param line
    or with `# lint:allow-default-cap` on the line above the def.

    Returns: list of advisory issues. NEVER BLOCKING.
    """
    import re as _re
    issues: List[Dict[str, str]] = []
    if not tools_dir.exists() or not tools_dir.is_dir():
        return issues

    # Pattern: param name matches cap-semantic AND default is int > 0 or True
    # Captures: (param_name)(: type_annotation)?\s*=\s*(default)
    #   - max_foo: int = 100
    #   - limit=50
    #   - truncate: bool = True
    #   - head_limit: Optional[int] = 20
    cap_name = _re.compile(
        r'\b('
        r'max_[a-z_]+'     # max_files, max_bytes, max_results, ...
        r'|limit'
        r'|truncate'
        r'|head_limit'
        r'|cap_[a-z_]+'
        r'|max_section_[a-z_]+'
        r')\b'
    )
    # Find `name: ... = value` inside function signatures
    param_re = _re.compile(
        r'\b([a-z_][a-z0-9_]*)\s*(?::\s*[^=,)]+)?\s*=\s*([^,)\n]+)'
    )
    # Truthy default = any positive int literal, True, or a string
    truthy_int = _re.compile(r'^\s*([1-9]\d*|True)\s*$')

    for py_file in sorted(tools_dir.rglob("*.py")):
        # Skip the lint checker itself and venv
        if py_file.name == "lint.py":
            continue
        if ".venv" in py_file.parts or "__pycache__" in py_file.parts:
            continue
        try:
            text = py_file.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        lines = text.split("\n")
        # Walk line by line, tracking multi-line function signatures
        in_def = False
        def_buffer: List[str] = []
        def_start_line = 0
        prev_line = ""
        def_allow_suppress = False
        for i, line in enumerate(lines, 1):
            stripped = line.rstrip()
            if not in_def:
                if _re.match(r'^\s*def\s+\w+\s*\(', stripped):
                    in_def = True
                    def_buffer = [stripped]
                    def_start_line = i
                    # Check previous line for suppression pragma
                    def_allow_suppress = "lint:allow-default-cap" in prev_line
                    if stripped.rstrip().endswith(")") or stripped.rstrip().endswith("):"):
                        # Single-line def — process immediately
                        _scan_def_sig(
                            "\n".join(def_buffer), def_start_line,
                            py_file, cap_name, param_re, truthy_int,
                            def_allow_suppress, issues,
                        )
                        in_def = False
                        def_buffer = []
                prev_line = stripped
                continue
            # In multi-line def
            def_buffer.append(stripped)
            if stripped.endswith(")") or stripped.endswith("):") or stripped.endswith(") -> None:") or ") ->" in stripped:
                _scan_def_sig(
                    "\n".join(def_buffer), def_start_line,
                    py_file, cap_name, param_re, truthy_int,
                    def_allow_suppress, issues,
                )
                in_def = False
                def_buffer = []
    return issues


def _scan_def_sig(
    sig_text: str, start_line: int, py_file: Path,
    cap_name: "re.Pattern", param_re: "re.Pattern", truthy_int: "re.Pattern",
    suppress: bool, issues: List[Dict[str, str]],
) -> None:
    """Helper — scan a single function signature for unsolicited cap defaults."""
    if suppress:
        return
    for m in param_re.finditer(sig_text):
        name, default = m.group(1), m.group(2).strip()
        if not cap_name.search(name):
            continue
        if "nocaps" in default.lower():
            continue  # trailing noqa-style suppression
        if not truthy_int.match(default):
            continue  # e.g. = None, = False, = 0 — those are explicit no-default
        issues.append({
            "file": str(py_file.relative_to(py_file.parents[1])),
            "line": start_line,
            "param": name,
            "default": default,
            "rule": "unsolicited-cap-default",
            "message": (
                f"Parameter '{name}' has default value '{default}' — violates "
                f"no-caps directive (2026-04-15). Caps must be opt-in by caller. "
                f"Either remove the default, set it to None/0/False, or add "
                f"'# lint:allow-default-cap' above the def with justification."
            ),
        })


def _check_standards_exemplars(
    pages: List[Path],
) -> List[Dict[str, str]]:
    """Check that standards pages reference exemplars that exist.

    Finds standards pages (model-*-standards.md) and checks that
    [[Page Title]] references in Gold Standard sections resolve to
    existing wiki pages. Returns advisory issues — not blocking.
    """
    import re as _re
    issues: List[Dict[str, str]] = []

    known = _collect_page_titles(pages)

    # Check standards pages
    for page in pages:
        if "model-" not in page.name or "standards" not in page.name:
            continue
        try:
            text = page.read_text(encoding="utf-8")
            meta, body = parse_frontmatter(text)
            if not meta:
                continue
            title = meta.get("title", "")
            in_gold_section = False
            in_backlinks = False
            for line in body.split("\n"):
                if line.startswith("### Gold Standard"):
                    in_gold_section = True
                elif line.startswith("## Backlinks"):
                    in_backlinks = True
                elif line.startswith("## ") and not line.startswith("### "):
                    in_gold_section = False
                if in_gold_section and not in_backlinks:
                    refs = _re.findall(r"\[\[([^\]]+)\]\]", line)
                    for ref in refs:
                        if "|" in ref:
                            slug, display = ref.split("|", 1)
                            slug, display = slug.strip(), display.strip()
                            if slug in known or display in known:
                                continue
                        elif ref.strip() in known:
                            continue
                        issues.append({
                            "standards_page": title,
                            "missing_exemplar": ref,
                        })
        except Exception:
            continue
    return issues


def _config_from_quality_standards(path: Path) -> Optional[LintConfig]:
    """Load LintConfig from a quality-standards.yaml file."""
    data = load_config(path)
    if data is None:
        return None
    pq = data.get("page_quality", {})
    dh = data.get("domain_health", {})
    dd = data.get("duplicate_detection", {})
    return LintConfig(
        stale_threshold_days=pq.get("stale_threshold_days", 30),
        min_summary_words=pq.get("min_summary_words", 30),
        min_deep_analysis_words=pq.get("min_deep_analysis_words", 100),
        min_relationships=pq.get("min_relationships", 1),
        min_domain_pages=dh.get("min_pages", 3),
        min_cross_domain_rels=dh.get("min_cross_domain_relationships", 2),
        similarity_threshold=dd.get("similarity_threshold", 0.70),
    )


def _print_human_report(report: Dict[str, Any]) -> None:
    """Print a human-readable lint report."""
    s = report["summary"]
    print(f"\nWiki Lint Report")
    print(f"{'=' * 40}")
    print(f"Pages scanned:    {s['pages_scanned']}")
    print(f"Total issues:     {s['total_issues']}")
    print()

    if report["dead_relationships"]:
        print(f"Dead Relationships ({len(report['dead_relationships'])}):")
        for d in report["dead_relationships"]:
            print(f"  [{d['source']}] {d['verb']}: '{d['target']}' (not found)")
        print()

    if report["stale_pages"]:
        print(f"Stale Pages ({len(report['stale_pages'])}):")
        for p in report["stale_pages"]:
            print(f"  {p['title']} (updated: {p['updated']})")
        print()

    if report["thin_pages"]:
        print(f"Thin Pages ({len(report['thin_pages'])}):")
        for p in report["thin_pages"]:
            if p["issue"] == "thin_deep_analysis":
                print(f"  {p['title']} [{p['type']}]: Deep Analysis {p['deep_analysis_words']} words")
            else:
                print(f"  {p['title']} [{p['type']}]: Summary {p.get('summary_words', '?')} words")
        print()

    if report["orphan_pages"]:
        print(f"Orphan Pages ({len(report['orphan_pages'])}):")
        for title in report["orphan_pages"]:
            print(f"  {title}")
        print()

    if report["domain_health"]:
        print(f"Domain Health Issues ({len(report['domain_health'])}):")
        for d in report["domain_health"]:
            print(f"  {d['domain']} ({d['page_count']} pages):")
            for issue in d["issues"]:
                print(f"    - {issue}")
        print()

    if report.get("filename_issues"):
        print(f"Filename Issues ({len(report['filename_issues'])}):")
        for p in report["filename_issues"]:
            print(f"  {p['file']}: {p['issue']}")
        print()

    if report.get("standards_issues"):
        print(f"Standards Self-Validation ({len(report['standards_issues'])}) [advisory]:")
        for p in report["standards_issues"]:
            print(f"  {p['standards_page']}: exemplar '{p['missing_exemplar']}' not found")
        print()

    if report.get("unstyled_pages"):
        print(f"Unstyled Pages ({len(report['unstyled_pages'])}) [advisory]:")
        for p in report["unstyled_pages"]:
            print(f"  {p['title']} [{p['type']}]: {p['lines']} lines, no callouts")
        print()

    if report.get("queue_drift"):
        print(f"Queue Drift ({len(report['queue_drift'])}) [advisory]:")
        print(f"  Operator-decision-queue entries that may be out-of-sync with home-page resolutions.")
        print(f"  Verify each: if the home-page resolved-callout corresponds to the queue entry, sync the queue.")
        for d in report["queue_drift"]:
            print(f"  Q{d['queue_number']} (open) → {d['source_page']} ({d['resolved_callouts_in_page']} resolved callout(s) in page)")
        print()

    status = "PASS" if s["total_issues"] == 0 else "FAIL"
    print(f"{status}: {s['total_issues']} issue(s) found")
    if s.get("unstyled_pages", 0) > 0:
        print(f"  ({s['unstyled_pages']} unstyled pages — advisory, not blocking)")
    if s.get("queue_drift", 0) > 0:
        print(f"  ({s['queue_drift']} queue-drift candidates — advisory, not blocking)")


def main():
    parser = argparse.ArgumentParser(description="Run wiki health checks")
    parser.add_argument(
        "--report",
        action="store_true",
        help="Output full JSON report",
    )
    parser.add_argument(
        "--summary",
        action="store_true",
        help="Output human-readable summary (default)",
    )
    parser.add_argument(
        "--fix",
        action="store_true",
        help="Attempt to auto-fix issues where possible",
    )
    parser.add_argument(
        "--config",
        help="Path to quality-standards.yaml (default: config/quality-standards.yaml)",
    )
    parser.add_argument(
        "wiki_dir",
        nargs="?",
        help="Path to wiki directory (default: wiki/)",
    )
    args = parser.parse_args()

    root = get_project_root()

    config_path = Path(args.config) if args.config else root / "wiki" / "config" / "quality-standards.yaml"
    lint_config = _config_from_quality_standards(config_path)
    if lint_config is None:
        # Use sensible defaults if config is missing
        lint_config = LintConfig(
            stale_threshold_days=30,
            min_summary_words=30,
            min_deep_analysis_words=100,
            min_relationships=1,
            min_domain_pages=3,
            min_cross_domain_rels=2,
            similarity_threshold=0.70,
        )

    wiki_dir = Path(args.wiki_dir) if args.wiki_dir else root / "wiki"
    report = lint_wiki(wiki_dir, lint_config)

    if args.fix:
        print("Auto-fix is not yet implemented.", file=sys.stderr)

    if args.report:
        print(json.dumps(report, indent=2))
    else:
        # Default to human-readable summary
        _print_human_report(report)

    sys.exit(0 if report["summary"]["total_issues"] == 0 else 1)


if __name__ == "__main__":
    main()
