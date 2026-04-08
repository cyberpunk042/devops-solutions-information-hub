"""Tests for tools/common.py — YAML frontmatter parser and config loader."""

import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tools.common import (
    parse_frontmatter,
    parse_relationships,
    parse_sections,
    load_config,
    detect_source_type,
    rebuild_domain_index,
)

FIXTURES = Path(__file__).resolve().parent / "fixtures"


class TestParseFrontmatter:
    def test_valid_concept(self):
        text = (FIXTURES / "valid-concept.md").read_text()
        meta, body = parse_frontmatter(text)
        assert meta["title"] == "Container Orchestration Patterns"
        assert meta["type"] == "concept"
        assert meta["domain"] == "infrastructure"
        assert meta["status"] == "synthesized"
        assert meta["confidence"] == "high"
        assert len(meta["sources"]) == 1
        assert meta["sources"][0]["id"] == "src-k8s-patterns"
        assert len(meta["tags"]) == 2
        assert "# Container Orchestration Patterns" in body

    def test_valid_source_synthesis(self):
        text = (FIXTURES / "valid-source-synthesis.md").read_text()
        meta, body = parse_frontmatter(text)
        assert meta["type"] == "source-synthesis"
        assert meta["domain"] == "knowledge-systems"

    def test_no_frontmatter(self):
        meta, body = parse_frontmatter("# Just a heading\n\nSome text.")
        assert meta == {}
        assert "# Just a heading" in body

    def test_empty_frontmatter(self):
        meta, body = parse_frontmatter("---\n---\n# Heading")
        assert meta == {}


class TestParseSections:
    def test_concept_sections(self):
        text = (FIXTURES / "valid-concept.md").read_text()
        _, body = parse_frontmatter(text)
        sections = parse_sections(body)
        assert "Summary" in sections
        assert "Key Insights" in sections
        assert "Deep Analysis" in sections
        assert "Open Questions" in sections
        assert "Relationships" in sections
        assert "Container orchestration patterns" in sections["Summary"]

    def test_source_synthesis_sections(self):
        text = (FIXTURES / "valid-source-synthesis.md").read_text()
        _, body = parse_frontmatter(text)
        sections = parse_sections(body)
        assert "Summary" in sections
        assert "Key Insights" in sections
        assert "Relationships" in sections


class TestParseRelationships:
    def test_valid_relationships(self):
        text = (FIXTURES / "valid-concept.md").read_text()
        _, body = parse_frontmatter(text)
        sections = parse_sections(body)
        rels = parse_relationships(sections.get("Relationships", ""))
        assert len(rels) >= 4
        verbs = [r["verb"] for r in rels]
        assert "BUILDS ON" in verbs
        assert "ENABLES" in verbs
        assert "COMPARES TO" in verbs
        targets = [t for r in rels for t in r["targets"]]
        assert "Docker Fundamentals" in targets

    def test_invalid_verb_detected(self):
        text = (FIXTURES / "invalid-bad-verb.md").read_text()
        _, body = parse_frontmatter(text)
        sections = parse_sections(body)
        rels = parse_relationships(sections.get("Relationships", ""))
        verbs = [r["verb"] for r in rels]
        assert "YOLO CONNECTS" in verbs

    def test_comma_separated_targets(self):
        rels = parse_relationships("- BUILDS ON: Topic A, Topic B, Topic C")
        assert len(rels) == 1
        assert rels[0]["targets"] == ["Topic A", "Topic B", "Topic C"]

    def test_parenthetical_context_preserved(self):
        rels = parse_relationships("- COMPARES TO: Serverless (different trade-offs)")
        assert rels[0]["targets"] == ["Serverless (different trade-offs)"]


class TestLoadConfig:
    def test_load_schema(self):
        config = load_config(FIXTURES / "test-schema.yaml")
        assert "required_fields" in config
        assert "title" in config["required_fields"]
        assert "concept" in config["enums"]["type"]
        assert "BUILDS ON" in config["relationship_verbs"]

    def test_load_nonexistent(self):
        config = load_config(FIXTURES / "nonexistent.yaml")
        assert config is None


class TestDetectSourceType:
    def test_pdf(self):
        assert detect_source_type("attention-paper.pdf") == "paper"

    def test_transcript(self):
        assert detect_source_type("karpathy-transcript.txt") == "youtube-transcript"
        assert detect_source_type("NoteGPT_TRANSCRIPT_foo.txt") == "youtube-transcript"

    def test_article(self):
        assert detect_source_type("great-blog-post.md") == "article"
        assert detect_source_type("docs-page.html") == "article"

    def test_notes(self):
        assert detect_source_type("my-notes-on-rag.md") == "notes"
        assert detect_source_type("idea-for-fleet.txt") == "notes"


class TestRebuildDomainIndex:
    def test_generates_index_content(self, tmp_path):
        page = tmp_path / "test-topic.md"
        page.write_text(
            '---\ntitle: "Test Topic"\ntype: concept\ndomain: test\n'
            'status: synthesized\nconfidence: high\ncreated: 2026-04-08\n'
            'updated: 2026-04-08\nsources:\n  - id: src-test\n    type: article\n'
            '    url: "https://example.com"\ntags: [foo, bar]\n---\n\n'
            '# Test Topic\n\n## Summary\n\nThis is a test summary.\n'
        )
        result = rebuild_domain_index(tmp_path, "test", "Test domain description.")
        assert "# Test" in result
        assert "Test Topic" in result
        assert "`foo`" in result
