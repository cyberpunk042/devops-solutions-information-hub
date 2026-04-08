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
        assert "[[Docker Fundamentals]]" in result
