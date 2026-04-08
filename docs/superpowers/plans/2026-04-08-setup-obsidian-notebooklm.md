# Setup Scripts + Obsidian + NotebookLM Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a modular setup script system that installs Obsidian, configures the wiki vault with graph view, generates Obsidian-compatible wikilinks, wires sister project exports, and preps NotebookLM integration.

**Architecture:** `scripts/` directory with `lib.sh` shared functions sourced by all sub-scripts, `setup.sh` master orchestrator with flag-based selection, and a new `tools/obsidian.py` that bridges `## Relationships` to `[[wikilinks]]` for Obsidian graph view. Each script is idempotent and standalone.

**Tech Stack:** Bash (scripts), Python 3.8+ (tools/obsidian.py), standard library only.

**Spec:** `docs/superpowers/specs/2026-04-08-setup-obsidian-notebooklm-design.md`

---

## File Structure

```
scripts/
├── lib.sh                       # Shared: logging, checks, constants
├── setup.sh                     # Master orchestrator (--all, --obsidian, etc.)
├── install-deps.sh              # Python + system deps
├── install-obsidian.sh          # Download + install Obsidian .deb
├── configure-obsidian.sh        # wiki/.obsidian/ vault config + run obsidian.py
├── configure-exports.sh         # Sister project export dir setup + dry-run
└── setup-notebooklm.sh          # notebooklm-py + stub skill

tools/
├── obsidian.py                  # Wikilink generator (NEW)

tests/
├── test_obsidian.py             # Tests for obsidian.py (NEW)

Modify:
├── CLAUDE.md                    # Add obsidian.py to tooling + post-ingestion
├── skills/wiki-agent/skill.md   # Add obsidian.py to post-ingestion steps
├── .gitignore                   # Add Obsidian workspace excludes
└── skills/notebooklm/skill.md   # Stub skill (NEW, created by setup-notebooklm.sh)
```

---

## Phase 1: Foundation (Tasks 1-2)

### Task 1: `scripts/lib.sh` — Shared Functions

**Files:**
- Create: `scripts/lib.sh`

- [ ] **Step 1: Create `scripts/lib.sh`**

```bash
#!/usr/bin/env bash
# Shared functions for setup scripts.
# Source this at the top of every sub-script:
#   source "$(dirname "$0")/lib.sh"

# Auto-detect project root (parent of scripts/)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
WIKI_DIR="${PROJECT_ROOT}/wiki"
CONFIG_DIR="${PROJECT_ROOT}/config"

# Global flag — set by setup.sh --yes
YES_FLAG="${YES_FLAG:-false}"

# --- Logging ---

log_info() {
    echo -e "\033[0;32m[INFO]\033[0m $1"
}

log_warn() {
    echo -e "\033[0;33m[WARN]\033[0m $1"
}

log_error() {
    echo -e "\033[0;31m[ERROR]\033[0m $1" >&2
}

# --- Checks ---

check_command() {
    local cmd="$1"
    if command -v "$cmd" &>/dev/null; then
        log_info "$cmd is available"
        return 0
    else
        log_warn "$cmd is not installed"
        return 1
    fi
}

check_dpkg() {
    local pkg="$1"
    if dpkg -l "$pkg" &>/dev/null; then
        log_info "$pkg is installed"
        return 0
    else
        log_warn "$pkg is not installed"
        return 1
    fi
}

check_dir() {
    local dir="$1"
    local label="$2"
    if [ -d "$dir" ]; then
        log_info "$label found at $dir"
        return 0
    else
        log_warn "$label not found at $dir"
        return 1
    fi
}

# --- Interaction ---

confirm_action() {
    local prompt="$1"
    if [ "$YES_FLAG" = "true" ]; then
        return 0
    fi
    read -rp "$prompt [y/N] " response
    case "$response" in
        [yY][eE][sS]|[yY]) return 0 ;;
        *) return 1 ;;
    esac
}
```

- [ ] **Step 2: Make executable**

```bash
chmod +x scripts/lib.sh
```

- [ ] **Step 3: Verify it sources cleanly**

```bash
cd /home/jfortin/devops-solutions-research-wiki && bash -c 'source scripts/lib.sh && log_info "lib.sh loaded" && echo "PROJECT_ROOT=$PROJECT_ROOT"'
```

Expected: `[INFO] lib.sh loaded` and correct project root path.

- [ ] **Step 4: Commit**

```bash
git add scripts/lib.sh
git commit -m "feat: add scripts/lib.sh shared functions

Provides log_info/warn/error, check_command/dpkg/dir, confirm_action,
and PROJECT_ROOT/WIKI_DIR/CONFIG_DIR constants. Sourced by all sub-scripts.

Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>"
```

---

### Task 2: `scripts/install-deps.sh`

**Files:**
- Create: `scripts/install-deps.sh`

- [ ] **Step 1: Create `scripts/install-deps.sh`**

```bash
#!/usr/bin/env bash
# Install Python and system dependencies.
source "$(dirname "$0")/lib.sh"

log_info "=== Installing dependencies ==="

# System deps
if check_command wget; then
    log_info "wget already available"
else
    log_info "Installing wget..."
    sudo apt-get update && sudo apt-get install -y wget
fi

if check_command python3; then
    log_info "python3 already available"
else
    log_error "python3 not found — please install Python 3.8+"
    exit 1
fi

if check_command pip3; then
    log_info "pip3 already available"
else
    log_info "Installing pip3..."
    sudo apt-get update && sudo apt-get install -y python3-pip
fi

# Python deps
log_info "Installing Python dependencies from requirements.txt..."
pip3 install -r "${PROJECT_ROOT}/requirements.txt"

# Verify
python3 -c "import yaml; print('PyYAML', yaml.__version__)" && log_info "PyYAML OK" || log_error "PyYAML import failed"

log_info "=== Dependencies installed ==="
```

- [ ] **Step 2: Make executable**

```bash
chmod +x scripts/install-deps.sh
```

- [ ] **Step 3: Test**

```bash
./scripts/install-deps.sh
```

Expected: all checks pass, PyYAML OK.

- [ ] **Step 4: Commit**

```bash
git add scripts/install-deps.sh
git commit -m "feat: add scripts/install-deps.sh

Installs wget, python3-pip, and PyYAML from requirements.txt.
Idempotent — skips already-installed packages.

Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>"
```

---

## Phase 2: Obsidian (Tasks 3-6)

### Task 3: `scripts/install-obsidian.sh`

**Files:**
- Create: `scripts/install-obsidian.sh`

- [ ] **Step 1: Create `scripts/install-obsidian.sh`**

```bash
#!/usr/bin/env bash
# Download and install Obsidian .deb package.
source "$(dirname "$0")/lib.sh"

OBSIDIAN_VERSION="${OBSIDIAN_VERSION:-1.12.7}"
DEB_FILE="/tmp/obsidian_${OBSIDIAN_VERSION}.deb"
URL="https://github.com/obsidianmd/obsidian-releases/releases/download/v${OBSIDIAN_VERSION}/obsidian_${OBSIDIAN_VERSION}_amd64.deb"

log_info "=== Installing Obsidian v${OBSIDIAN_VERSION} ==="

# Check if already installed
if check_dpkg obsidian; then
    INSTALLED_VER=$(dpkg -l obsidian 2>/dev/null | grep obsidian | awk '{print $3}')
    log_info "Obsidian ${INSTALLED_VER} already installed"
    exit 0
fi

# Download
if [ -f "$DEB_FILE" ]; then
    log_info "Using cached download at $DEB_FILE"
else
    log_info "Downloading Obsidian v${OBSIDIAN_VERSION}..."
    wget -q --show-progress -O "$DEB_FILE" "$URL"
    if [ $? -ne 0 ]; then
        log_error "Download failed from $URL"
        exit 1
    fi
fi

# Install
log_info "Installing Obsidian..."
if ! confirm_action "This requires sudo to install the .deb package. Continue?"; then
    log_warn "Skipped Obsidian installation"
    exit 0
fi

sudo dpkg -i "$DEB_FILE"
if [ $? -ne 0 ]; then
    log_info "Fixing missing dependencies..."
    sudo apt-get install -f -y
fi

# Verify
if check_dpkg obsidian; then
    log_info "=== Obsidian installed successfully ==="
else
    log_error "Obsidian installation failed"
    exit 1
fi
```

- [ ] **Step 2: Make executable**

```bash
chmod +x scripts/install-obsidian.sh
```

- [ ] **Step 3: Commit**

```bash
git add scripts/install-obsidian.sh
git commit -m "feat: add scripts/install-obsidian.sh

Downloads and installs Obsidian .deb from GitHub releases.
Version pinned via OBSIDIAN_VERSION env var (default 1.12.7).
Idempotent — skips if already installed.

Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>"
```

---

### Task 4: `tools/obsidian.py` — Wikilink Generator

**Files:**
- Create: `tools/obsidian.py`
- Create: `tests/test_obsidian.py`

- [ ] **Step 1: Write failing tests**

Create `tests/test_obsidian.py`:

```python
"""Tests for tools/obsidian.py — Obsidian wikilink generator."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tools.obsidian import generate_backlinks, build_title_lookup
from tools.manifest import build_manifest

FIXTURES = Path(__file__).resolve().parent / "fixtures"


class TestBuildTitleLookup:
    def test_builds_from_manifest(self):
        manifest = build_manifest(FIXTURES)
        lookup = build_title_lookup(manifest)
        assert "Container Orchestration Patterns" in lookup
        assert lookup["Container Orchestration Patterns"]["path"].endswith("valid-concept.md")

    def test_slug_lookup(self):
        manifest = build_manifest(FIXTURES)
        lookup = build_title_lookup(manifest)
        # Slug-based lookup (filename stem)
        slugs = {info.get("slug", "") for info in lookup.values()}
        assert any("valid-concept" in s for s in slugs)


class TestGenerateBacklinks:
    def test_generates_backlinks_for_page(self):
        manifest = build_manifest(FIXTURES)
        lookup = build_title_lookup(manifest)
        text = (FIXTURES / "valid-concept.md").read_text()
        result = generate_backlinks(text, manifest, lookup)
        assert "## Backlinks" in result
        assert "[[" in result

    def test_preserves_relationships_section(self):
        manifest = build_manifest(FIXTURES)
        lookup = build_title_lookup(manifest)
        text = (FIXTURES / "valid-concept.md").read_text()
        result = generate_backlinks(text, manifest, lookup)
        assert "## Relationships" in result
        assert "- BUILDS ON:" in result

    def test_idempotent(self):
        manifest = build_manifest(FIXTURES)
        lookup = build_title_lookup(manifest)
        text = (FIXTURES / "valid-concept.md").read_text()
        first = generate_backlinks(text, manifest, lookup)
        second = generate_backlinks(first, manifest, lookup)
        assert first == second

    def test_unresolved_targets_become_wikilinks(self):
        manifest = build_manifest(FIXTURES)
        lookup = build_title_lookup(manifest)
        text = (FIXTURES / "valid-concept.md").read_text()
        result = generate_backlinks(text, manifest, lookup)
        # "Docker Fundamentals" is a relationship target with no page
        assert "[[Docker Fundamentals]]" in result
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
python3 -m pytest tests/test_obsidian.py -v
```

Expected: FAIL — `ModuleNotFoundError`

- [ ] **Step 3: Implement `tools/obsidian.py`**

```python
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
    """Build lookup: page title → {path, slug, source_ids}.

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
    4. Unresolved → [[target]] as-is (shows as unresolved in Obsidian)
    """
    # Direct title match
    if target in lookup:
        return f"[[{target}]]"

    # Slug match — target might be a kebab-case slug
    for title, info in lookup.items():
        if info.get("slug") == target:
            return f"[[{title}]]"

    # Source ID match — for "DERIVED FROM: src-xxx"
    if target.startswith("src-"):
        for title, info in lookup.items():
            if target in info.get("source_ids", []):
                return f"[[{title}]]"

    # Unresolved — still useful in Obsidian (shows as hollow node)
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
```

- [ ] **Step 4: Run tests to verify they pass**

```bash
python3 -m pytest tests/test_obsidian.py -v
```

Expected: All 6 tests PASS.

- [ ] **Step 5: Smoke test on real wiki**

```bash
python3 tools/obsidian.py --check
```

Expected: reports pages that would be updated.

- [ ] **Step 6: Commit**

```bash
git add tools/obsidian.py tests/test_obsidian.py
git commit -m "feat: add Obsidian wikilink generator

tools/obsidian.py generates ## Backlinks sections with [[wikilinks]]
from ## Relationships data. Bridges openfleet-compatible format to
Obsidian graph view. Supports --check (dry-run) and --clean modes.

Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>"
```

---

### Task 5: `scripts/configure-obsidian.sh`

**Files:**
- Create: `scripts/configure-obsidian.sh`

- [ ] **Step 1: Create `scripts/configure-obsidian.sh`**

```bash
#!/usr/bin/env bash
# Configure Obsidian vault settings in wiki/.obsidian/
source "$(dirname "$0")/lib.sh"

OBSIDIAN_DIR="${WIKI_DIR}/.obsidian"

log_info "=== Configuring Obsidian vault ==="

mkdir -p "$OBSIDIAN_DIR"

# app.json — Editor settings
cat > "${OBSIDIAN_DIR}/app.json" << 'EOF'
{
  "vimMode": false,
  "strictLineBreaks": true,
  "showFrontmatter": true,
  "foldHeading": true,
  "foldIndent": true,
  "defaultViewMode": "preview"
}
EOF
log_info "Created app.json"

# appearance.json — Dark mode
cat > "${OBSIDIAN_DIR}/appearance.json" << 'EOF'
{
  "theme": "obsidian",
  "translucency": false,
  "baseFontSize": 16
}
EOF
log_info "Created appearance.json"

# core-plugins.json — Enable useful core plugins
cat > "${OBSIDIAN_DIR}/core-plugins.json" << 'EOF'
[
  "graph",
  "backlink",
  "tag-pane",
  "outgoing-links",
  "search",
  "file-explorer",
  "page-preview"
]
EOF
log_info "Created core-plugins.json"

# graph.json — Graph view with domain-colored nodes
cat > "${OBSIDIAN_DIR}/graph.json" << 'EOF'
{
  "collapse-filter": false,
  "search": "",
  "showTags": false,
  "showAttachments": false,
  "hideUnresolved": false,
  "showOrphans": true,
  "collapse-color-groups": false,
  "colorGroups": [
    {"query": "path:domains/ai-agents", "color": {"a": 1, "rgb": 4886754}},
    {"query": "path:domains/knowledge-systems", "color": {"a": 1, "rgb": 2470655}},
    {"query": "path:domains/automation", "color": {"a": 1, "rgb": 16750848}},
    {"query": "path:domains/tools-and-platforms", "color": {"a": 1, "rgb": 8388352}},
    {"query": "path:sources", "color": {"a": 1, "rgb": 10066329}}
  ],
  "collapse-display": false,
  "lineSizeMultiplier": 1,
  "nodeSizeMultiplier": 1,
  "textFadeMultiplier": 0,
  "centerStrength": 0.5,
  "repelStrength": 10,
  "linkStrength": 1,
  "linkDistance": 250
}
EOF
log_info "Created graph.json with domain color groups"

# Generate wikilinks for graph view
log_info "Generating Obsidian wikilinks..."
cd "$PROJECT_ROOT"
python3 -m tools.manifest
python3 -m tools.obsidian
log_info "Wikilinks generated"

log_info "=== Obsidian vault configured at ${WIKI_DIR} ==="
log_info "Open Obsidian → Open folder as vault → select: ${WIKI_DIR}"
```

- [ ] **Step 2: Make executable**

```bash
chmod +x scripts/configure-obsidian.sh
```

- [ ] **Step 3: Commit**

```bash
git add scripts/configure-obsidian.sh
git commit -m "feat: add scripts/configure-obsidian.sh

Creates wiki/.obsidian/ with app settings, dark mode, core plugins,
and graph view with domain-based color groups. Generates wikilinks.

Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>"
```

---

### Task 6: Update `.gitignore`, `CLAUDE.md`, and wiki-agent skill

**Files:**
- Modify: `.gitignore`
- Modify: `CLAUDE.md`
- Modify: `skills/wiki-agent/skill.md`

- [ ] **Step 1: Update `.gitignore`**

Add to the end of `.gitignore`:

```
# Obsidian workspace (user-specific, not portable)
wiki/.obsidian/workspace.json
wiki/.obsidian/workspace-mobile.json
```

- [ ] **Step 2: Update `CLAUDE.md`**

Add to the Tooling section (after the `tools/stats.py` line):

```
- `python3 tools/obsidian.py` — Regenerate [[wikilinks]] for Obsidian graph view
```

Update the Post-Ingestion section — add step 6 before "Report summary of changes":

```
6. Regenerate wikilinks via tools/obsidian.py
```

The full Post-Ingestion section should read:
```
After every ingestion:
1. Update affected _index.md files
2. Regenerate manifest.json via tools/manifest.py
3. Run tools/validate.py — errors block completion
4. Flag stale pages affected by new information
5. Regenerate wikilinks via tools/obsidian.py
6. Report summary of changes
```

- [ ] **Step 3: Update `skills/wiki-agent/skill.md`**

Update the post-ingestion steps to include obsidian.py. The block should read:

```
Post-ingestion (every time):
1. Update affected _index.md files
2. Run: python3 tools/manifest.py
3. Run: python3 tools/validate.py
4. Run: python3 tools/obsidian.py
5. Flag stale pages needing review
6. Report summary: sources processed, pages created/updated, domains affected,
   relationships added, any warnings
```

- [ ] **Step 4: Commit**

```bash
git add .gitignore CLAUDE.md skills/wiki-agent/skill.md
git commit -m "feat: integrate obsidian.py into workflow

Add Obsidian workspace files to .gitignore.
Add tools/obsidian.py to CLAUDE.md tooling and post-ingestion steps.
Update wiki-agent skill with obsidian.py in post-ingestion pipeline.

Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>"
```

---

## Phase 3: Sister Projects + NotebookLM (Tasks 7-9)

### Task 7: `scripts/configure-exports.sh`

**Files:**
- Create: `scripts/configure-exports.sh`

- [ ] **Step 1: Create `scripts/configure-exports.sh`**

```bash
#!/usr/bin/env bash
# Configure export directories in sister projects.
source "$(dirname "$0")/lib.sh"

OPENFLEET_DIR="${PROJECT_ROOT}/../openfleet"
AICP_DIR="${PROJECT_ROOT}/../devops-expert-local-ai"

log_info "=== Configuring sister project exports ==="

# openfleet
if check_dir "$OPENFLEET_DIR" "openfleet"; then
    EXPORT_DIR="${OPENFLEET_DIR}/docs/knowledge-map/kb/research-wiki"
    mkdir -p "$EXPORT_DIR"
    log_info "openfleet export dir ready: $EXPORT_DIR"

    log_info "Dry-run openfleet export..."
    cd "$PROJECT_ROOT"
    python3 -m tools.export openfleet --dry
else
    log_warn "openfleet not found — skipping export configuration"
fi

echo ""

# AICP
if check_dir "$AICP_DIR" "AICP (devops-expert-local-ai)"; then
    EXPORT_DIR="${AICP_DIR}/docs/kb/research-wiki"
    mkdir -p "$EXPORT_DIR"
    log_info "AICP export dir ready: $EXPORT_DIR"

    log_info "Dry-run AICP export..."
    cd "$PROJECT_ROOT"
    python3 -m tools.export aicp --dry
else
    log_warn "AICP not found — skipping export configuration"
fi

log_info "=== Export configuration complete ==="
log_info "Run 'python3 tools/export.py openfleet' or 'python3 tools/export.py aicp' to export."
```

- [ ] **Step 2: Make executable**

```bash
chmod +x scripts/configure-exports.sh
```

- [ ] **Step 3: Commit**

```bash
git add scripts/configure-exports.sh
git commit -m "feat: add scripts/configure-exports.sh

Creates export target directories in openfleet and AICP sister projects.
Runs dry-run exports to verify the pipeline. Non-destructive.

Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>"
```

---

### Task 8: `scripts/setup-notebooklm.sh`

**Files:**
- Create: `scripts/setup-notebooklm.sh`
- Create: `skills/notebooklm/skill.md`

- [ ] **Step 1: Create `scripts/setup-notebooklm.sh`**

```bash
#!/usr/bin/env bash
# Install notebooklm-py and create stub skill for NotebookLM integration.
source "$(dirname "$0")/lib.sh"

log_info "=== Setting up NotebookLM integration ==="

# Attempt to install notebooklm-py
log_info "Attempting to install notebooklm-py..."
if pip3 install notebooklm-py 2>/dev/null; then
    log_info "notebooklm-py installed successfully"
else
    log_warn "notebooklm-py not available via pip"
    log_warn "Try manual install: pip3 install git+https://github.com/nicktang/notebooklm-py.git"
    log_warn "Or check: https://github.com/nicktang/notebooklm-py"
fi

# Check for existing auth
if [ -f "$HOME/.notebooklm/credentials.json" ]; then
    log_info "NotebookLM credentials found at ~/.notebooklm/credentials.json"
else
    log_warn "NotebookLM not authenticated"
    log_warn "After installing notebooklm-py, run: notebooklm auth"
    log_warn "This will open Chrome for Google account login"
fi

# Create stub skill if not present
SKILL_DIR="${PROJECT_ROOT}/skills/notebooklm"
SKILL_FILE="${SKILL_DIR}/skill.md"

if [ -f "$SKILL_FILE" ]; then
    log_info "NotebookLM skill already exists at $SKILL_FILE"
else
    mkdir -p "$SKILL_DIR"
    cat > "$SKILL_FILE" << 'SKILL'
# NotebookLM Integration — Stub

This skill will connect the research wiki to Google NotebookLM.

## Status: Not yet configured

To set up:
1. Install: `pip3 install notebooklm-py`
2. Authenticate: `notebooklm auth` (opens Chrome for Google login)
3. Replace this stub with the full NotebookLM skill

## Planned Capabilities

- Push wiki pages as NotebookLM sources
- Create notebooks organized by domain
- Query wiki content through NotebookLM's grounded chat
- Generate audio/video summaries of research domains

## Usage (once configured)

```
Hey Claude, push the knowledge-systems domain into a NotebookLM notebook.
Hey Claude, create a NotebookLM notebook from my latest research.
```
SKILL
    log_info "Created stub skill at $SKILL_FILE"
fi

log_info "=== NotebookLM setup complete ==="
```

- [ ] **Step 2: Make executable**

```bash
chmod +x scripts/setup-notebooklm.sh
```

- [ ] **Step 3: Commit**

```bash
git add scripts/setup-notebooklm.sh skills/notebooklm/skill.md
git commit -m "feat: add scripts/setup-notebooklm.sh + stub skill

Attempts notebooklm-py install, checks auth status, creates stub skill
at skills/notebooklm/skill.md with setup instructions and planned capabilities.

Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>"
```

---

### Task 9: `scripts/setup.sh` — Master Orchestrator

**Files:**
- Create: `scripts/setup.sh`

- [ ] **Step 1: Create `scripts/setup.sh`**

```bash
#!/usr/bin/env bash
# Master setup script — orchestrates all sub-scripts.
source "$(dirname "$0")/lib.sh"

usage() {
    cat << 'USAGE'
Usage: ./scripts/setup.sh [OPTIONS]

Options:
  --all           Run everything
  --deps          Install Python + system dependencies
  --obsidian      Install Obsidian + configure vault + generate wikilinks
  --exports       Configure sister project export directories
  --notebooklm    Install notebooklm-py + create stub skill
  --yes           Skip confirmation prompts
  -h, --help      Show this help

With no flags: interactive mode.
USAGE
}

# Parse flags
RUN_DEPS=false
RUN_OBSIDIAN=false
RUN_EXPORTS=false
RUN_NOTEBOOKLM=false
INTERACTIVE=true

while [[ $# -gt 0 ]]; do
    case "$1" in
        --all)
            RUN_DEPS=true; RUN_OBSIDIAN=true; RUN_EXPORTS=true; RUN_NOTEBOOKLM=true
            INTERACTIVE=false; shift ;;
        --deps)
            RUN_DEPS=true; INTERACTIVE=false; shift ;;
        --obsidian)
            RUN_OBSIDIAN=true; INTERACTIVE=false; shift ;;
        --exports)
            RUN_EXPORTS=true; INTERACTIVE=false; shift ;;
        --notebooklm)
            RUN_NOTEBOOKLM=true; INTERACTIVE=false; shift ;;
        --yes)
            export YES_FLAG=true; shift ;;
        -h|--help)
            usage; exit 0 ;;
        *)
            log_error "Unknown option: $1"; usage; exit 1 ;;
    esac
done

# Interactive mode
if [ "$INTERACTIVE" = "true" ]; then
    log_info "=== Research Wiki Setup ==="
    echo ""
    confirm_action "Install Python/system dependencies?" && RUN_DEPS=true
    confirm_action "Install and configure Obsidian?" && RUN_OBSIDIAN=true
    confirm_action "Configure sister project exports?" && RUN_EXPORTS=true
    confirm_action "Set up NotebookLM integration?" && RUN_NOTEBOOKLM=true
    echo ""
fi

SCRIPTS_DIR="$(dirname "$0")"

# Execute in order
if [ "$RUN_DEPS" = "true" ]; then
    bash "${SCRIPTS_DIR}/install-deps.sh"
    echo ""
fi

if [ "$RUN_OBSIDIAN" = "true" ]; then
    bash "${SCRIPTS_DIR}/install-obsidian.sh"
    echo ""
    bash "${SCRIPTS_DIR}/configure-obsidian.sh"
    echo ""
fi

if [ "$RUN_EXPORTS" = "true" ]; then
    bash "${SCRIPTS_DIR}/configure-exports.sh"
    echo ""
fi

if [ "$RUN_NOTEBOOKLM" = "true" ]; then
    bash "${SCRIPTS_DIR}/setup-notebooklm.sh"
    echo ""
fi

log_info "=== Setup complete ==="
```

- [ ] **Step 2: Make executable**

```bash
chmod +x scripts/setup.sh
```

- [ ] **Step 3: Test help**

```bash
./scripts/setup.sh --help
```

Expected: usage text displayed.

- [ ] **Step 4: Commit**

```bash
git add scripts/setup.sh
git commit -m "feat: add scripts/setup.sh master orchestrator

Supports --all, --deps, --obsidian, --exports, --notebooklm flags.
Interactive mode when no flags. Orchestrates all sub-scripts in order.

Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>"
```

---

## Phase 4: Verification (Task 10)

### Task 10: End-to-End Verification

- [ ] **Step 1: Run full test suite**

```bash
python3 -m pytest tests/ -v
```

Expected: All tests pass (previous 36 + new obsidian tests).

- [ ] **Step 2: Run wikilink generation on real wiki**

```bash
python3 tools/obsidian.py
```

Expected: wiki pages updated with ## Backlinks sections.

- [ ] **Step 3: Verify wikilinks were added**

```bash
grep -l "## Backlinks" wiki/domains/*/*.md wiki/sources/*.md | wc -l
```

Expected: 11 files (all wiki pages except _index.md files).

- [ ] **Step 4: Verify Obsidian config created by configure-obsidian.sh**

```bash
./scripts/configure-obsidian.sh
ls -la wiki/.obsidian/
```

Expected: app.json, appearance.json, core-plugins.json, graph.json all present.

- [ ] **Step 5: Test setup.sh --help**

```bash
./scripts/setup.sh --help
```

Expected: usage text.

- [ ] **Step 6: Test configure-exports.sh**

```bash
./scripts/configure-exports.sh
```

Expected: finds openfleet and AICP, creates export dirs, dry-runs succeed.

- [ ] **Step 7: Commit all generated content**

```bash
git add wiki/ scripts/
git commit -m "feat: generate initial Obsidian backlinks + vault config

Run obsidian.py on all wiki pages, creating ## Backlinks sections.
Configure wiki/.obsidian/ vault for graph view with domain colors.

Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>"
```
