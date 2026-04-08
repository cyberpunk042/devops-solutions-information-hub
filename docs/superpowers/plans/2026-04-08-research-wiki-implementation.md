# Research Wiki Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a research-grade knowledge synthesis system with ingestion pipeline, validation tooling, export capabilities, and a wiki-agent skill — then prove it works by ingesting the two existing transcripts.

**Architecture:** Monorepo with `raw/` intake, `wiki/` knowledge store organized by domains, `tools/` Python utilities for validation/manifest/lint/export/stats, `skills/` for the wiki-agent skill, and `config/` for schema/domains/export-profiles/quality-standards. YAML frontmatter on all wiki pages, `## Relationships` sections compatible with openfleet's `kb_sync.py` regex, multi-resolution content via section markers.

**Tech Stack:** Python 3.8+, PyYAML, standard library (pathlib, json, re, argparse, datetime, collections, math). No external dependencies beyond PyYAML.

**Spec:** `docs/superpowers/specs/2026-04-08-research-wiki-design.md`

---

## File Structure

```
devops-solutions-research-wiki/
├── CLAUDE.md                                    # Project brain — schema, conventions, modes
├── .claude/
│   └── settings.json                            # Project-level Claude settings
├── .gitignore                                   # Python, editor, OS ignores
├── requirements.txt                             # PyYAML only
│
├── config/
│   ├── schema.yaml                              # Frontmatter schema + enums + required sections
│   ├── domains.yaml                             # Domain registry with descriptions
│   ├��─ export-profiles.yaml                     # Per-project export transforms + filters
│   └── quality-standards.yaml                   # Lint thresholds
│
├─�� tools/
│   ├── __init__.py                              # Empty, makes tools a package
│   ├── common.py                                # Shared: YAML frontmatter parser, config loader
│   ├── validate.py                              # Schema enforcement CLI
│   ├���─ manifest.py                              # manifest.json builder CLI
│   ├── lint.py                                  # Wiki health checks CLI
│   ├── export.py                                # Sister project export CLI
│   └── stats.py                                 # Coverage & growth reporting CLI
│
├── tests/
���   ├── __init__.py
│   ├── test_common.py                           # Tests for frontmatter parser, config loader
│   ├── test_validate.py                         # Tests for schema validation
│   ├── test_manifest.py                         # Tests for manifest generation
│   ���── test_lint.py                             # Tests for lint checks
│   ├��─ test_export.py                           # Tests for export transforms
│   └── fixtures/                                # Test wiki pages, configs
│       ├── valid-concept.md                     # A valid concept page
│       ├── valid-source-synthesis.md            # A valid source-synthesis page
│       ├── invalid-missing-fields.md            # Missing required frontmatter
│       ├── invalid-bad-verb.md                  # Invalid relationship verb
│       └── test-schema.yaml                     # Test config
│
├── skills/
│   └── wiki-agent/
│       └── skill.md                             # Master skill for wiki operations
│
├── raw/
│   ├── transcripts/                             # YouTube/podcast transcripts
│   │   ├── claude-notebooklm-content-team.txt   # Existing transcript (moved)
│   │   └── karpathy-claude-code-10x.txt         # Existing transcript (moved)
│   ├── articles/
│   ├── papers/
│   ├─�� notes/
│   └── dumps/
│
├── wiki/
│   ├── index.md                                 # Master index
│   ├── manifest.json                            # Machine-readable graph (generated)
│   ├── domains/
│   │   ├── _index.md                            # Domain registry index
│   │   ├── ai-agents/
│   │   │   └── _index.md
│   │   └── knowledge-systems/
│   │       └── _index.md
│   ├── sources/
│   └── comparisons/
│
└─��� docs/
    └── superpowers/
        ├── specs/
        │   └── 2026-04-08-research-wiki-design.md
        └── plans/
            └── 2026-04-08-research-wiki-implementation.md  # This file
```

---

## Phase 1: Foundation (Tasks 1-4)

Scaffold the project, set up config files, build the shared library, write CLAUDE.md.

### Task 1: Project Scaffold & Git Init

**Files:**
- Create: `.gitignore`
- Create: `requirements.txt`
- Create: `raw/transcripts/.gitkeep`
- Create: `raw/articles/.gitkeep`
- Create: `raw/papers/.gitkeep`
- Create: `raw/notes/.gitkeep`
- Create: `raw/dumps/.gitkeep`
- Create: `wiki/domains/.gitkeep`
- Create: `wiki/sources/.gitkeep`
- Create: `wiki/comparisons/.gitkeep`
- Create: `tools/__init__.py`
- Create: `tests/__init__.py`
- Create: `tests/fixtures/.gitkeep`
- Create: `skills/wiki-agent/.gitkeep`
- Move: existing transcripts to `raw/transcripts/`

- [ ] **Step 1: Create `.gitignore`**

```
# Python
__pycache__/
*.py[cod]
*$py.class
*.egg-info/
dist/
build/
.eggs/
*.egg
.venv/
venv/

# Editor
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Project
*.pyc
```

- [ ] **Step 2: Create `requirements.txt`**

```
PyYAML>=6.0
```

- [ ] **Step 3: Create all directory scaffolding with `.gitkeep` files**

Create empty `.gitkeep` files in:
- `raw/transcripts/`
- `raw/articles/`
- `raw/papers/`
- `raw/notes/`
- `raw/dumps/`
- `wiki/domains/`
- `wiki/sources/`
- `wiki/comparisons/`
- `tools/` (create `__init__.py` instead of `.gitkeep`)
- `tests/` (create `__init__.py`)
- `tests/fixtures/`
- `skills/wiki-agent/`

Both `__init__.py` files are empty.

- [ ] **Step 4: Move existing transcripts to `raw/transcripts/`**

```bash
mv "NoteGPT_TRANSCRIPT_Claude + NotebookLM = Your 247 Content Team.txt" raw/transcripts/claude-notebooklm-content-team.txt
mv NoteGPT_TRANSCRIPT_Andrej* raw/transcripts/karpathy-claude-code-10x.txt
```

Also move the early draft guide (it will be superseded by the wiki):
```bash
mv claude-code-research-pipeline-guide.md docs/
```

- [ ] **Step 5: Install dependencies**

```bash
pip3 install -r requirements.txt
```

- [ ] **Step 6: Commit**

```bash
git add .gitignore requirements.txt raw/ wiki/ tools/__init__.py tests/ skills/ docs/
git commit -m "feat: scaffold research wiki project structure

Create raw/, wiki/, tools/, tests/, skills/, config/ directories.
Move existing transcripts to raw/transcripts/.
Add .gitignore and requirements.txt."
```

---

### Task 2: Configuration Files

**Files:**
- Create: `config/schema.yaml`
- Create: `config/domains.yaml`
- Create: `config/quality-standards.yaml`
- Create: `config/export-profiles.yaml`

- [ ] **Step 1: Create `config/schema.yaml`**

```yaml
# Wiki page frontmatter schema definition
# Used by tools/validate.py to enforce page structure

required_fields:
  - title
  - type
  - domain
  - status
  - confidence
  - created
  - updated
  - sources
  - tags

optional_fields:
  - subdomain
  - aliases
  - complexity
  - resolution

enums:
  type:
    - concept
    - source-synthesis
    - comparison
    - reference
    - deep-dive
    - index
  status:
    - raw
    - processing
    - synthesized
    - verified
    - stale
  confidence:
    - low
    - medium
    - high
    - authoritative
  complexity:
    - beginner
    - intermediate
    - advanced
    - expert
  source_type:
    - article
    - youtube-transcript
    - paper
    - documentation
    - notes
    - paste
    - book
    - podcast-transcript

required_sections:
  concept:
    - Summary
    - Key Insights
    - Deep Analysis
    - Relationships
  source-synthesis:
    - Summary
    - Key Insights
    - Relationships
  comparison:
    - Summary
    - Key Insights
    - Deep Analysis
    - Relationships
  reference:
    - Summary
    - Relationships
  deep-dive:
    - Summary
    - Key Insights
    - Deep Analysis
    - Relationships
  index: []

relationship_verbs:
  - BUILDS ON
  - ENABLES
  - COMPARES TO
  - CONTRADICTS
  - USED BY
  - RELATES TO
  - FEEDS INTO
  - DERIVED FROM
  - SUPERSEDES
  - IMPLEMENTS
  - EXTENDS

source_required_fields:
  - id
  - type

source_needs_one_of:
  - url
  - file
```

- [ ] **Step 2: Create `config/domains.yaml`**

```yaml
# Domain registry — grows organically as topics emerge
# Each domain gets a wiki/domains/{name}/ folder with _index.md

domains:
  ai-agents:
    description: "Multi-agent systems, orchestration, fleet management, agent memory"
  ai-models:
    description: "LLMs, embeddings, training, fine-tuning, model evaluation"
  infrastructure:
    description: "Containers, networking, cloud, databases, storage"
  devops:
    description: "CI/CD, deployment, monitoring, IaC, SRE"
  security:
    description: "AppSec, infrastructure security, threat modeling, compliance"
  knowledge-systems:
    description: "RAG, knowledge graphs, wikis, embeddings, search, synthesis"
  automation:
    description: "Scheduling, pipelines, workflow automation, cron, task orchestration"
  tools-and-platforms:
    description: "Software tools, platforms, IDEs, CLI tools, SaaS products"
```

- [ ] **Step 3: Create `config/quality-standards.yaml`**

```yaml
# Quality thresholds for linting and export decisions

page_quality:
  min_summary_words: 30
  min_deep_analysis_words: 100
  min_relationships: 1
  max_open_questions_ratio: 0.5
  stale_threshold_days: 30

domain_health:
  min_pages: 3
  min_cross_domain_relationships: 2

export_readiness:
  min_confidence: medium
  min_status: synthesized
  require_source_provenance: true

duplicate_detection:
  similarity_threshold: 0.70
```

- [ ] **Step 4: Create `config/export-profiles.yaml`**

```yaml
# Export profiles for sister project integration

openfleet:
  description: "Export for LightRAG ingestion via kb_sync.py"
  target_format: openfleet-kb
  output_dir: ../openfleet/docs/knowledge-map/kb/research-wiki/
  transforms:
    frontmatter: strip
    type_map:
      concept: "Research"
      source-synthesis: "Research"
      comparison: "Research Synthesis"
      reference: "Research"
      deep-dive: "Research Synthesis"
    add_metadata:
      - key: "Type"
        value: "{type_mapped}"
      - key: "Source Project"
        value: "devops-solutions-research-wiki"
      - key: "Date"
        value: "{updated}"
    relationship_format: preserve
    resolution: full
  filters:
    min_confidence: medium
    min_status: synthesized
    exclude_domains: []

aicp:
  description: "Export for LocalAI Collections KB"
  target_format: aicp-kb
  output_dir: ../devops-expert-local-ai/docs/kb/research-wiki/
  transforms:
    frontmatter: markdown-headers
    type_map:
      concept: "Research Finding"
      source-synthesis: "Research Finding"
      comparison: "Research Finding"
      reference: "Infrastructure Reference"
      deep-dive: "Research Finding"
    status_map:
      synthesized: "RESEARCHED"
      verified: "VERIFIED"
      stale: "OUTDATED"
    add_metadata:
      - key: "Type"
        value: "{type_mapped}"
      - key: "Date"
        value: "{updated}"
      - key: "Status"
        value: "{status_mapped}"
      - key: "Sources"
        value: "{source_urls}"
    resolution: condensed
  filters:
    min_confidence: medium
    min_status: synthesized
    domains:
      - infrastructure
      - devops
      - ai-models
      - ai-agents
      - security
      - knowledge-systems
```

- [ ] **Step 5: Commit**

```bash
git add config/
git commit -m "feat: add configuration files

schema.yaml defines frontmatter validation rules.
domains.yaml registers initial knowledge domains.
quality-standards.yaml sets lint thresholds.
export-profiles.yaml configures openfleet and AICP exports."
```

---

### Task 3: Shared Library (`tools/common.py`)

**Files:**
- Create: `tools/common.py`
- Create: `tests/test_common.py`
- Create: `tests/fixtures/valid-concept.md`
- Create: `tests/fixtures/valid-source-synthesis.md`
- Create: `tests/fixtures/invalid-missing-fields.md`
- Create: `tests/fixtures/invalid-bad-verb.md`
- Create: `tests/fixtures/test-schema.yaml`

- [ ] **Step 1: Create test fixtures**

Create `tests/fixtures/test-schema.yaml` — a minimal copy of `config/schema.yaml` for isolated testing:

```yaml
required_fields:
  - title
  - type
  - domain
  - status
  - confidence
  - created
  - updated
  - sources
  - tags

enums:
  type: [concept, source-synthesis, comparison, reference, deep-dive, index]
  status: [raw, processing, synthesized, verified, stale]
  confidence: [low, medium, high, authoritative]
  source_type: [article, youtube-transcript, paper, documentation, notes, paste, book, podcast-transcript]

required_sections:
  concept: [Summary, Key Insights, Deep Analysis, Relationships]
  source-synthesis: [Summary, Key Insights, Relationships]
  comparison: [Summary, Key Insights, Deep Analysis, Relationships]
  reference: [Summary, Relationships]
  deep-dive: [Summary, Key Insights, Deep Analysis, Relationships]
  index: []

relationship_verbs:
  - BUILDS ON
  - ENABLES
  - COMPARES TO
  - CONTRADICTS
  - USED BY
  - RELATES TO
  - FEEDS INTO
  - DERIVED FROM
  - SUPERSEDES
  - IMPLEMENTS
  - EXTENDS

source_required_fields: [id, type]
source_needs_one_of: [url, file]
```

Create `tests/fixtures/valid-concept.md`:

```markdown
---
title: "Container Orchestration Patterns"
type: concept
domain: infrastructure
status: synthesized
confidence: high
created: 2026-04-08
updated: 2026-04-08
sources:
  - id: src-k8s-patterns
    type: article
    url: "https://example.com/k8s-patterns"
    title: "Kubernetes Patterns"
    ingested: 2026-04-08
tags: [kubernetes, orchestration]
---

# Container Orchestration Patterns

## Summary

Container orchestration patterns define how containerized applications are deployed,
scaled, and managed across clusters. These patterns have evolved from simple
single-host deployments to sophisticated multi-cluster management strategies.

## Key Insights

- Declarative configuration beats imperative scripting for reproducibility
- Health checks and readiness probes are non-negotiable for production
- Horizontal pod autoscaling should be based on custom metrics, not just CPU

## Deep Analysis

Orchestration patterns fall into three categories: scheduling (where containers run),
networking (how they communicate), and storage (how data persists). Each category
has mature solutions but the integration between them remains challenging.

The sidecar pattern has emerged as the dominant approach for cross-cutting concerns
like logging, monitoring, and service mesh proxies. This pattern keeps the main
container focused on business logic while sidecars handle infrastructure concerns.

## Open Questions

- How do serverless containers (Fargate, Cloud Run) change orchestration patterns?
- What is the practical limit of cluster size before federation becomes necessary?

## Relationships

- BUILDS ON: Docker Fundamentals, Linux Namespaces
- ENABLES: Microservice Architecture, Auto-Scaling Strategies
- COMPARES TO: Serverless Patterns (different trade-offs at scale)
- RELATES TO: CI/CD Pipelines, Service Mesh
```

Create `tests/fixtures/valid-source-synthesis.md`:

```markdown
---
title: "Synthesis: Karpathy LLM Wiki Post"
type: source-synthesis
domain: knowledge-systems
status: synthesized
confidence: high
created: 2026-04-08
updated: 2026-04-08
sources:
  - id: src-karpathy-llm-wiki
    type: article
    url: "https://x.com/karpathy/status/example"
    title: "Karpathy on LLM Knowledge Bases"
    ingested: 2026-04-08
tags: [karpathy, llm, knowledge-base, markdown]
---

# Synthesis: Karpathy LLM Wiki Post

## Summary

Andrej Karpathy proposed using well-organized markdown files with indexes and
interlinks as knowledge bases for LLMs, instead of traditional RAG with vector
databases. The approach leverages the LLM's ability to read indexes and follow
links, producing deeper understanding than similarity-based chunk retrieval.

## Key Insights

- LLMs navigate markdown wikis by reading indexes and following links
- Explicit relationships via links produce deeper understanding than similarity search
- Scales well to hundreds of pages with good indexes
- The LLM can identify gaps and suggest new research directions
- Periodic linting keeps the wiki accurate and structured

## Relationships

- ENABLES: LLM Wiki Pattern, Agent Memory Systems
- DERIVED FROM: src-karpathy-llm-wiki
- RELATES TO: RAG Architecture, Knowledge Graph Approaches
```

Create `tests/fixtures/invalid-missing-fields.md`:

```markdown
---
title: "Missing Fields Page"
type: concept
---

# Missing Fields Page

## Summary

This page is missing required frontmatter fields.
```

Create `tests/fixtures/invalid-bad-verb.md`:

```markdown
---
title: "Bad Verb Page"
type: concept
domain: infrastructure
status: synthesized
confidence: high
created: 2026-04-08
updated: 2026-04-08
sources:
  - id: src-test
    type: article
    url: "https://example.com"
tags: [test]
---

# Bad Verb Page

## Summary

This page has an invalid relationship verb.

## Key Insights

- Test insight

## Deep Analysis

Test analysis content that meets the minimum word count for a concept page.

## Relationships

- BUILDS ON: Something Valid
- YOLO CONNECTS: Invalid Verb Target
```

- [ ] **Step 2: Write the failing tests for `tools/common.py`**

Create `tests/test_common.py`:

```python
"""Tests for tools/common.py — YAML frontmatter parser and config loader."""

import os
import sys
from pathlib import Path

# Add project root to path so tools package is importable
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
        # parse_relationships returns all verbs; validation checks allowed list
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
        # Create a mock domain dir with one page
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
```

- [ ] **Step 3: Run tests to verify they fail**

```bash
cd /home/jfortin/devops-solutions-research-wiki && python3 -m pytest tests/test_common.py -v
```

Expected: FAIL — `ModuleNotFoundError: No module named 'tools.common'`

- [ ] **Step 4: Implement `tools/common.py`**

```python
"""Shared utilities for wiki tools.

Provides YAML frontmatter parsing, section extraction, relationship parsing,
and config file loading. Used by validate.py, manifest.py, lint.py, export.py,
and stats.py.
"""

import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import yaml


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


# Regex matching openfleet kb_sync.py pattern: ^([A-Z][A-Z /\-]+?):\s*(.+)$
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
            targets = _split_targets(targets_raw)
            rels.append({
                "verb": verb,
                "targets": targets,
                "raw": line,
            })
    return rels


def _split_targets(text: str) -> List[str]:
    """Split comma-separated targets, respecting parentheses.

    'Topic A, Topic B (context), Topic C' ->
    ['Topic A', 'Topic B (context)', 'Topic C']
    """
    targets: List[str] = []
    current: List[str] = []
    depth = 0

    for char in text:
        if char == "(":
            depth += 1
            current.append(char)
        elif char == ")":
            depth -= 1
            current.append(char)
        elif char == "," and depth == 0:
            targets.append("".join(current).strip())
            current = []
        else:
            current.append(char)

    if current:
        targets.append("".join(current).strip())

    return [t for t in targets if t]


def load_config(path: Path) -> Optional[Dict[str, Any]]:
    """Load a YAML config file. Returns None if file doesn't exist."""
    if not path.exists():
        return None
    with open(path) as f:
        return yaml.safe_load(f)


def find_wiki_pages(wiki_dir: Path) -> List[Path]:
    """Find all .md files in wiki/ excluding _index.md files."""
    pages = []
    for md_file in sorted(wiki_dir.rglob("*.md")):
        if md_file.name == "_index.md":
            continue
        pages.append(md_file)
    return pages


def find_all_wiki_files(wiki_dir: Path) -> List[Path]:
    """Find all .md files in wiki/ including _index.md files."""
    return sorted(wiki_dir.rglob("*.md"))


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

    Returns a source_type enum value matching config/schema.yaml.
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
    """
    pages_info = []
    all_tags: list = []

    for md_file in sorted(domain_dir.glob("*.md")):
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
        pages_info.append({"file": md_file.name, "title": title, "summary": summary})
        for tag in meta.get("tags", []):
            all_tags.append(tag)

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
```

- [ ] **Step 5: Run tests to verify they pass**

```bash
cd /home/jfortin/devops-solutions-research-wiki && python3 -m pytest tests/test_common.py -v
```

Expected: All 14 tests PASS (including detect_source_type and rebuild_domain_index).

- [ ] **Step 6: Commit**

```bash
git add tools/common.py tests/test_common.py tests/fixtures/
git commit -m "feat: add shared library with frontmatter parser, section parser, relationship parser

tools/common.py provides parse_frontmatter(), parse_sections(),
parse_relationships(), load_config(), and utility functions.
Full test coverage with fixtures for valid and invalid pages."
```

---

### Task 4: CLAUDE.md

**Files:**
- Create: `CLAUDE.md`

- [ ] **Step 1: Create `CLAUDE.md`**

Write the full CLAUDE.md as specified in Section 6 of the design spec. The content is defined verbatim in the spec at `docs/superpowers/specs/2026-04-08-research-wiki-design.md` lines 457-579.

```markdown
# DevOps Solutions Research Wiki

A research-grade knowledge synthesis system and second brain. Central intelligence
spine for the devops ecosystem (openfleet, AICP, DSPD, devops-control-plane).

## What This Is

A monorepo containing:
- An interlinked wiki of synthesized knowledge across domains
- An ingestion pipeline that processes any source type into structured wiki pages
- Tooling for validation, linting, export, and integration with sister projects
- A skill that teaches Claude how to operate the entire system

## Project Structure

- `raw/` — Unprocessed source material (transcripts, articles, papers, notes, dumps)
- `wiki/` — Processed knowledge (domains/, sources/, comparisons/, index.md, manifest.json)
- `tools/` — Python utilities (lint, manifest, export, validate, stats)
- `skills/` — Claude skill definitions
- `config/` — Schema, domain registry, export profiles, quality standards
- `docs/` — Project documentation and specs

## Page Schema

Every wiki page uses YAML frontmatter with these required fields:

  title, type, domain, status, confidence, created, updated, sources, tags

Page types: concept, source-synthesis, comparison, reference, deep-dive, index

Status lifecycle: raw → processing → synthesized → verified → stale

Confidence levels: low, medium, high, authoritative

## Page Structure

Every page follows this section order:

  # Title
  ## Summary          ← minimal resolution (2-3 sentences min, used for LightRAG description)
  ## Key Insights     ← condensed resolution boundary
  ## Deep Analysis    ← full resolution (concept, comparison, deep-dive types)
  ## Open Questions   ← gaps to fill (optional but encouraged)
  ## Relationships    ← VERB: target format, one per line

## Relationship Conventions

Use ALL_CAPS verbs. One relationship per line. Comma-separated targets allowed.

  BUILDS ON, ENABLES, COMPARES TO, CONTRADICTS, USED BY,
  RELATES TO, FEEDS INTO, DERIVED FROM, SUPERSEDES, IMPLEMENTS, EXTENDS

Format: `- VERB: Target Name (optional context)`

Compatible with openfleet kb_sync.py regex: ^([A-Z][A-Z /\-]+?):\s*(.+)$

## Ingestion Modes

Three modes, user specifies or defaults to smart:

- `auto` — Process without stopping. Report summary after.
- `guided` — Show extraction plan. Wait for approval. Review each page.
- `smart` (default) — Auto when confident. Escalate when: new domain,
  contradictions, ambiguity, expert-level complexity, low-quality source.

## Ingestion Sources

Accept any of:
- Files dropped in raw/ (any subfolder)
- URLs (fetch via WebFetch, save to raw/, then process)
- Pasted content (save to raw/dumps/, then process)

## Quality Gates

Every page must have:
- Complete frontmatter with valid values per config/schema.yaml
- Summary (min 30 words)
- At least 1 relationship (unless first in new domain)
- Reachable from domain _index.md
- Source provenance (URL or file reference)
- No >70% concept overlap with existing pages (update instead of create)
- title field matches # Heading
- domain field matches folder path

## Post-Ingestion

After every ingestion:
1. Update affected _index.md files
2. Regenerate manifest.json via tools/manifest.py
3. Run tools/validate.py — errors block completion
4. Flag stale pages affected by new information
5. Report summary of changes

## Integration

This wiki feeds sister projects via file-based export:
- openfleet — LightRAG graph via ## Relationships (kb_sync.py compatible)
- AICP — docs/kb/ via export (tools/export.py)
- DSPD, control-plane — future

Export profiles defined in config/export-profiles.yaml.
Export transforms YAML frontmatter to markdown headers for compatibility.

## Tooling

- `python3 tools/validate.py` — Schema validation (exit 0 = clean, 1 = errors)
- `python3 tools/manifest.py` — Regenerate wiki/manifest.json
- `python3 tools/lint.py [--report|--summary|--fix]` — Health checks
- `python3 tools/export.py [openfleet|aicp]` — Export for sister projects
- `python3 tools/stats.py [--json]` — Coverage & growth reporting

## Conventions

- kebab-case filenames
- One concept per page
- Update existing pages rather than creating duplicates
- Domains grow organically — create new domain folders as needed
- _index.md in every domain folder, auto-maintained
- manifest.json regenerated after every wiki change
- raw/ files kept permanently for provenance
- Sources prefixed with src- in wiki/sources/
```

- [ ] **Step 2: Commit**

```bash
git add CLAUDE.md
git commit -m "feat: add CLAUDE.md project brain

Defines page schema, relationship conventions, ingestion modes,
quality gates, tooling commands, and integration surface."
```

---

## Phase 2: Core Tooling (Tasks 5-9)

Build the five Python tools that power the system: validate, manifest, lint, export, stats.

### Task 5: `tools/validate.py`

**Files:**
- Create: `tools/validate.py`
- Create: `tests/test_validate.py`

- [ ] **Step 1: Write failing tests**

Create `tests/test_validate.py`:

```python
"""Tests for tools/validate.py — schema enforcement."""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tools.validate import validate_page, validate_wiki

FIXTURES = Path(__file__).resolve().parent / "fixtures"
SCHEMA = Path(__file__).resolve().parent / "fixtures" / "test-schema.yaml"


class TestValidatePage:
    def test_valid_concept_passes(self):
        result = validate_page(FIXTURES / "valid-concept.md", SCHEMA)
        assert result["errors"] == []

    def test_valid_source_synthesis_passes(self):
        result = validate_page(FIXTURES / "valid-source-synthesis.md", SCHEMA)
        assert result["errors"] == []

    def test_missing_fields_detected(self):
        result = validate_page(FIXTURES / "invalid-missing-fields.md", SCHEMA)
        errors = [e["code"] for e in result["errors"]]
        assert "missing_field" in errors

    def test_bad_verb_warned(self):
        result = validate_page(FIXTURES / "invalid-bad-verb.md", SCHEMA)
        warnings = [w["code"] for w in result["warnings"]]
        assert "invalid_verb" in warnings

    def test_missing_sections_detected(self):
        result = validate_page(FIXTURES / "invalid-missing-fields.md", SCHEMA)
        errors = [e["code"] for e in result["errors"]]
        # concept type requires Summary, Key Insights, Deep Analysis, Relationships
        assert "missing_section" in errors


class TestValidateWiki:
    def test_validates_fixtures_dir(self):
        results = validate_wiki(FIXTURES, SCHEMA)
        assert len(results) > 0
        # Should find both valid and invalid files
        all_errors = [e for r in results for e in r["errors"]]
        assert len(all_errors) > 0  # From invalid fixtures
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
python3 -m pytest tests/test_validate.py -v
```

Expected: FAIL — `ModuleNotFoundError: No module named 'tools.validate'`

- [ ] **Step 3: Implement `tools/validate.py`**

```python
"""Schema validation for wiki pages.

Validates YAML frontmatter against config/schema.yaml, checks required
sections per page type, and validates relationship verbs.

Usage:
    python3 tools/validate.py                    # Validate all wiki/ pages
    python3 tools/validate.py path/to/page.md    # Validate one page
    python3 tools/validate.py --json             # JSON output

Exit code: 0 if no errors, 1 if errors found.
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, List

from tools.common import (
    find_wiki_pages,
    get_project_root,
    load_config,
    parse_frontmatter,
    parse_relationships,
    parse_sections,
    word_count,
)


def validate_page(
    page_path: Path, schema_path: Path
) -> Dict[str, Any]:
    """Validate a single wiki page against schema.

    Returns {"file": str, "errors": [...], "warnings": [...]}.
    Each error/warning has "code", "message", and optional "field".
    """
    errors: List[Dict[str, str]] = []
    warnings: List[Dict[str, str]] = []
    result = {
        "file": str(page_path),
        "errors": errors,
        "warnings": warnings,
    }

    schema = load_config(schema_path)
    if schema is None:
        errors.append({"code": "schema_missing", "message": f"Schema not found: {schema_path}"})
        return result

    text = page_path.read_text(encoding="utf-8")
    meta, body = parse_frontmatter(text)

    # Check frontmatter exists
    if not meta:
        errors.append({"code": "no_frontmatter", "message": "No YAML frontmatter found"})
        return result

    # Check required fields
    for field in schema.get("required_fields", []):
        if field not in meta:
            errors.append({
                "code": "missing_field",
                "message": f"Required field missing: {field}",
                "field": field,
            })
        elif meta[field] is None or meta[field] == "":
            errors.append({
                "code": "empty_field",
                "message": f"Required field is empty: {field}",
                "field": field,
            })

    # Check enum values
    enums = schema.get("enums", {})
    for field, allowed in enums.items():
        if field in meta and meta[field] not in allowed:
            errors.append({
                "code": "invalid_enum",
                "message": f"Invalid value for {field}: '{meta[field]}' (allowed: {allowed})",
                "field": field,
            })

    # Check sources
    sources = meta.get("sources", [])
    if isinstance(sources, list):
        src_required = schema.get("source_required_fields", [])
        src_needs_one = schema.get("source_needs_one_of", [])
        for i, src in enumerate(sources):
            if not isinstance(src, dict):
                errors.append({"code": "invalid_source", "message": f"Source {i} is not a dict"})
                continue
            for sf in src_required:
                if sf not in src:
                    errors.append({
                        "code": "source_missing_field",
                        "message": f"Source {i} missing required field: {sf}",
                    })
            if src_needs_one and not any(sf in src for sf in src_needs_one):
                errors.append({
                    "code": "source_missing_ref",
                    "message": f"Source {i} needs at least one of: {src_needs_one}",
                })
            # Validate source type enum
            if "type" in src and src["type"] not in enums.get("source_type", []):
                warnings.append({
                    "code": "invalid_source_type",
                    "message": f"Source {i} has unrecognized type: '{src['type']}'",
                })

    # Check required sections
    page_type = meta.get("type", "")
    required_secs = schema.get("required_sections", {}).get(page_type, [])
    sections = parse_sections(body)
    for sec in required_secs:
        if sec not in sections:
            errors.append({
                "code": "missing_section",
                "message": f"Required section missing for type '{page_type}': ## {sec}",
            })

    # Check title consistency
    title = meta.get("title", "")
    first_heading = None
    for line in body.split("\n"):
        if line.startswith("# ") and not line.startswith("## "):
            first_heading = line[2:].strip()
            break
    if title and first_heading and title != first_heading:
        warnings.append({
            "code": "title_mismatch",
            "message": f"Frontmatter title '{title}' != heading '{first_heading}'",
        })

    # Check relationships
    rel_text = sections.get("Relationships", "")
    if rel_text:
        rels = parse_relationships(rel_text)
        allowed_verbs = schema.get("relationship_verbs", [])
        for rel in rels:
            if rel["verb"] not in allowed_verbs:
                warnings.append({
                    "code": "invalid_verb",
                    "message": f"Unrecognized relationship verb: '{rel['verb']}'",
                })

    # Check summary word count
    summary = sections.get("Summary", "")
    if summary and word_count(summary) < 10:
        warnings.append({
            "code": "thin_summary",
            "message": f"Summary is very short ({word_count(summary)} words)",
        })

    return result


def validate_wiki(
    wiki_dir: Path, schema_path: Path
) -> List[Dict[str, Any]]:
    """Validate all .md files in a directory."""
    results = []
    for md_file in sorted(wiki_dir.rglob("*.md")):
        if md_file.name.startswith("_"):
            continue
        results.append(validate_page(md_file, schema_path))
    return results


def main():
    parser = argparse.ArgumentParser(description="Validate wiki pages against schema")
    parser.add_argument("path", nargs="?", help="Page or directory to validate")
    parser.add_argument("--json", action="store_true", help="JSON output")
    parser.add_argument("--schema", help="Path to schema.yaml")
    args = parser.parse_args()

    root = get_project_root()
    schema_path = Path(args.schema) if args.schema else root / "config" / "schema.yaml"

    if args.path:
        target = Path(args.path)
        if target.is_file():
            results = [validate_page(target, schema_path)]
        else:
            results = validate_wiki(target, schema_path)
    else:
        results = validate_wiki(root / "wiki", schema_path)

    total_errors = sum(len(r["errors"]) for r in results)
    total_warnings = sum(len(r["warnings"]) for r in results)

    if args.json:
        print(json.dumps({"results": results, "total_errors": total_errors, "total_warnings": total_warnings}, indent=2))
    else:
        for r in results:
            if r["errors"] or r["warnings"]:
                print(f"\n{r['file']}:")
                for e in r["errors"]:
                    print(f"  ERROR [{e['code']}]: {e['message']}")
                for w in r["warnings"]:
                    print(f"  WARN  [{w['code']}]: {w['message']}")
        print(f"\n{'PASS' if total_errors == 0 else 'FAIL'}: {len(results)} files, {total_errors} errors, {total_warnings} warnings")

    sys.exit(0 if total_errors == 0 else 1)


if __name__ == "__main__":
    main()
```

- [ ] **Step 4: Run tests to verify they pass**

```bash
python3 -m pytest tests/test_validate.py -v
```

Expected: All 6 tests PASS.

- [ ] **Step 5: Smoke test on fixtures**

```bash
python3 tools/validate.py tests/fixtures/ --schema tests/fixtures/test-schema.yaml
```

Expected: errors from invalid fixtures, passes for valid ones.

- [ ] **Step 6: Commit**

```bash
git add tools/validate.py tests/test_validate.py
git commit -m "feat: add wiki page validator

tools/validate.py enforces frontmatter schema, required sections per
page type, relationship verb validation, source provenance checks.
Returns JSON or human-readable report. Exit code 1 on errors."
```

---

### Task 6: `tools/manifest.py`

**Files:**
- Create: `tools/manifest.py`
- Create: `tests/test_manifest.py`

- [ ] **Step 1: Write failing tests**

Create `tests/test_manifest.py`:

```python
"""Tests for tools/manifest.py — manifest.json builder."""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tools.manifest import build_manifest

FIXTURES = Path(__file__).resolve().parent / "fixtures"


class TestBuildManifest:
    def test_builds_from_fixtures(self):
        manifest = build_manifest(FIXTURES)
        assert "generated" in manifest
        assert "stats" in manifest
        assert "pages" in manifest
        assert "domains" in manifest
        assert "tags" in manifest
        assert manifest["stats"]["pages"] > 0

    def test_extracts_page_metadata(self):
        manifest = build_manifest(FIXTURES)
        pages_by_title = {p["title"]: p for p in manifest["pages"]}
        assert "Container Orchestration Patterns" in pages_by_title
        page = pages_by_title["Container Orchestration Patterns"]
        assert page["type"] == "concept"
        assert page["domain"] == "infrastructure"
        assert "kubernetes" in page["tags"]

    def test_extracts_relationships(self):
        manifest = build_manifest(FIXTURES)
        pages_by_title = {p["title"]: p for p in manifest["pages"]}
        page = pages_by_title["Container Orchestration Patterns"]
        verbs = [r["verb"] for r in page["relationships"]]
        assert "BUILDS ON" in verbs

    def test_builds_tag_index(self):
        manifest = build_manifest(FIXTURES)
        assert "kubernetes" in manifest["tags"]

    def test_builds_domain_index(self):
        manifest = build_manifest(FIXTURES)
        assert "infrastructure" in manifest["domains"]
        assert manifest["domains"]["infrastructure"]["page_count"] >= 1

    def test_finds_orphaned_refs(self):
        manifest = build_manifest(FIXTURES)
        # "Docker Fundamentals" is a relationship target but not a page
        orphan_targets = [o["target"] for o in manifest["orphaned_refs"]]
        assert "Docker Fundamentals" in orphan_targets
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
python3 -m pytest tests/test_manifest.py -v
```

Expected: FAIL — `ModuleNotFoundError`

- [ ] **Step 3: Implement `tools/manifest.py`**

```python
"""Build manifest.json from wiki content.

Scans all .md files, parses frontmatter and relationships,
produces a machine-readable graph index.

Usage:
    python3 tools/manifest.py                   # Build from wiki/
    python3 tools/manifest.py path/to/dir       # Build from specific dir
    python3 tools/manifest.py --output out.json  # Custom output path
"""

import argparse
import json
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List

from tools.common import (
    find_wiki_pages,
    get_project_root,
    parse_frontmatter,
    parse_relationships,
    parse_sections,
)


def build_manifest(wiki_dir: Path) -> Dict[str, Any]:
    """Build manifest dict from all .md files in wiki_dir."""
    pages: List[Dict[str, Any]] = []
    domains: Dict[str, Dict[str, int]] = defaultdict(lambda: {"page_count": 0, "relationship_count": 0})
    tags: Dict[str, List[str]] = defaultdict(list)
    all_page_titles: set = set()
    all_rel_targets: set = set()

    for md_file in sorted(wiki_dir.rglob("*.md")):
        if md_file.name.startswith("_"):
            continue

        text = md_file.read_text(encoding="utf-8")
        meta, body = parse_frontmatter(text)

        if not meta or "title" not in meta:
            continue

        title = meta["title"]
        all_page_titles.add(title)

        sections = parse_sections(body)
        rel_text = sections.get("Relationships", "")
        rels = parse_relationships(rel_text)

        relationships = []
        for rel in rels:
            for target in rel["targets"]:
                relationships.append({"verb": rel["verb"], "target": target})
                # Strip parenthetical for matching
                clean_target = target.split("(")[0].strip() if "(" in target else target
                all_rel_targets.add(clean_target)

        domain = meta.get("domain", "unknown")
        domains[domain]["page_count"] += 1
        domains[domain]["relationship_count"] += len(relationships)

        page_tags = meta.get("tags", [])
        if isinstance(page_tags, list):
            file_slug = md_file.stem
            for tag in page_tags:
                tags[tag].append(file_slug)

        source_ids = []
        for src in meta.get("sources", []):
            if isinstance(src, dict) and "id" in src:
                source_ids.append(src["id"])

        pages.append({
            "path": str(md_file.relative_to(wiki_dir)) if wiki_dir in md_file.parents or wiki_dir == md_file.parent else str(md_file),
            "title": title,
            "type": meta.get("type", "unknown"),
            "domain": domain,
            "subdomain": meta.get("subdomain"),
            "status": meta.get("status", "unknown"),
            "confidence": meta.get("confidence", "unknown"),
            "created": str(meta.get("created", "")),
            "updated": str(meta.get("updated", "")),
            "tags": page_tags if isinstance(page_tags, list) else [],
            "complexity": meta.get("complexity"),
            "source_ids": source_ids,
            "relationships": relationships,
        })

    # Find orphaned refs (targets that don't match any page title)
    orphaned_refs = []
    for target in sorted(all_rel_targets):
        if target not in all_page_titles:
            referenced_by = []
            for p in pages:
                for r in p["relationships"]:
                    clean = r["target"].split("(")[0].strip() if "(" in r["target"] else r["target"]
                    if clean == target:
                        referenced_by.append(p["title"])
            orphaned_refs.append({
                "target": target,
                "referenced_by": list(set(referenced_by)),
            })

    # Count sources and comparisons
    source_count = sum(1 for p in pages if p["type"] == "source-synthesis")
    comparison_count = sum(1 for p in pages if p["type"] == "comparison")
    total_rels = sum(len(p["relationships"]) for p in pages)

    manifest = {
        "generated": datetime.now(timezone.utc).isoformat(),
        "stats": {
            "pages": len(pages),
            "domains": len(domains),
            "sources": source_count,
            "comparisons": comparison_count,
            "relationships": total_rels,
            "tags_unique": len(tags),
        },
        "pages": pages,
        "domains": dict(domains),
        "tags": dict(tags),
        "orphaned_refs": orphaned_refs,
    }

    return manifest


def main():
    parser = argparse.ArgumentParser(description="Build manifest.json from wiki content")
    parser.add_argument("path", nargs="?", help="Wiki directory to scan")
    parser.add_argument("--output", "-o", help="Output path (default: wiki/manifest.json)")
    args = parser.parse_args()

    root = get_project_root()
    wiki_dir = Path(args.path) if args.path else root / "wiki"
    output = Path(args.output) if args.output else wiki_dir / "manifest.json"

    manifest = build_manifest(wiki_dir)

    output.parent.mkdir(parents=True, exist_ok=True)
    with open(output, "w") as f:
        json.dump(manifest, f, indent=2)

    stats = manifest["stats"]
    print(f"Manifest built: {stats['pages']} pages, {stats['domains']} domains, "
          f"{stats['relationships']} relationships, {stats['tags_unique']} tags")
    print(f"Orphaned refs: {len(manifest['orphaned_refs'])}")
    print(f"Written to: {output}")


if __name__ == "__main__":
    main()
```

- [ ] **Step 4: Run tests to verify they pass**

```bash
python3 -m pytest tests/test_manifest.py -v
```

Expected: All 6 tests PASS.

- [ ] **Step 5: Commit**

```bash
git add tools/manifest.py tests/test_manifest.py
git commit -m "feat: add manifest.json builder

tools/manifest.py scans wiki pages, extracts metadata and relationships,
builds machine-readable graph index with page list, domain index, tag
index, and orphaned reference detection."
```

---

### Task 7: `tools/lint.py`

**Files:**
- Create: `tools/lint.py`
- Create: `tests/test_lint.py`

- [ ] **Step 1: Write failing tests**

Create `tests/test_lint.py`:

```python
"""Tests for tools/lint.py — wiki health checks."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tools.lint import lint_wiki, LintConfig

FIXTURES = Path(__file__).resolve().parent / "fixtures"


class TestLintWiki:
    def test_detects_dead_relationships(self):
        config = LintConfig(stale_threshold_days=30, min_summary_words=30,
                            min_deep_analysis_words=100, min_relationships=1,
                            min_domain_pages=3, min_cross_domain_rels=2,
                            similarity_threshold=0.70)
        report = lint_wiki(FIXTURES, config)
        # "Docker Fundamentals" etc. are relationship targets with no page
        assert len(report["dead_relationships"]) > 0

    def test_returns_structured_report(self):
        config = LintConfig(stale_threshold_days=30, min_summary_words=30,
                            min_deep_analysis_words=100, min_relationships=1,
                            min_domain_pages=3, min_cross_domain_rels=2,
                            similarity_threshold=0.70)
        report = lint_wiki(FIXTURES, config)
        assert "orphan_pages" in report
        assert "dead_relationships" in report
        assert "stale_pages" in report
        assert "thin_pages" in report
        assert "domain_health" in report
        assert "summary" in report
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
python3 -m pytest tests/test_lint.py -v
```

Expected: FAIL — `ModuleNotFoundError`

- [ ] **Step 3: Implement `tools/lint.py`**

```python
"""Wiki health checks beyond schema validation.

Checks: orphan pages, dead relationships, stale pages, thin pages,
domain balance, isolated clusters.

Usage:
    python3 tools/lint.py                    # Summary report
    python3 tools/lint.py --report           # JSON report
    python3 tools/lint.py --fix              # Auto-fix where possible
"""

import argparse
import json
import sys
from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Dict, List, Set

from tools.common import (
    get_project_root,
    load_config,
    parse_frontmatter,
    parse_relationships,
    parse_sections,
    word_count,
)


@dataclass
class LintConfig:
    stale_threshold_days: int = 30
    min_summary_words: int = 30
    min_deep_analysis_words: int = 100
    min_relationships: int = 1
    min_domain_pages: int = 3
    min_cross_domain_rels: int = 2
    similarity_threshold: float = 0.70


def lint_wiki(wiki_dir: Path, config: LintConfig) -> Dict[str, Any]:
    """Run all lint checks on wiki directory. Returns structured report."""
    pages_data: List[Dict[str, Any]] = []
    all_titles: Set[str] = set()
    indexed_pages: Set[str] = set()

    # Parse all pages
    for md_file in sorted(wiki_dir.rglob("*.md")):
        if md_file.name.startswith("_"):
            # Read index files to track which pages they reference
            text = md_file.read_text(encoding="utf-8")
            for line in text.split("\n"):
                if line.strip().startswith("- [") or line.strip().startswith("- **"):
                    # Extract referenced page names from index
                    indexed_pages.add(line.strip())
            continue

        text = md_file.read_text(encoding="utf-8")
        meta, body = parse_frontmatter(text)
        if not meta:
            continue

        sections = parse_sections(body)
        rels = parse_relationships(sections.get("Relationships", ""))

        pages_data.append({
            "path": str(md_file),
            "title": meta.get("title", md_file.stem),
            "type": meta.get("type", "unknown"),
            "domain": meta.get("domain", "unknown"),
            "status": meta.get("status", "unknown"),
            "updated": str(meta.get("updated", "")),
            "sections": sections,
            "relationships": rels,
            "meta": meta,
        })
        all_titles.add(meta.get("title", md_file.stem))

    # Check: dead relationships
    dead_rels: List[Dict[str, str]] = []
    for page in pages_data:
        for rel in page["relationships"]:
            for target in rel["targets"]:
                clean = target.split("(")[0].strip() if "(" in target else target
                if clean not in all_titles:
                    dead_rels.append({
                        "source": page["title"],
                        "verb": rel["verb"],
                        "target": clean,
                    })

    # Check: stale pages
    stale: List[Dict[str, str]] = []
    cutoff = datetime.now() - timedelta(days=config.stale_threshold_days)
    for page in pages_data:
        if page["status"] == "stale":
            continue
        updated_str = page["updated"]
        if updated_str:
            try:
                updated = datetime.strptime(updated_str[:10], "%Y-%m-%d")
                if updated < cutoff:
                    stale.append({"title": page["title"], "updated": updated_str})
            except ValueError:
                pass

    # Check: thin pages
    thin: List[Dict[str, Any]] = []
    for page in pages_data:
        ptype = page["type"]
        if ptype in ("concept", "deep-dive", "comparison"):
            analysis = page["sections"].get("Deep Analysis", "")
            wc = word_count(analysis)
            if wc < config.min_deep_analysis_words:
                thin.append({"title": page["title"], "type": ptype, "deep_analysis_words": wc})
        summary = page["sections"].get("Summary", "")
        swc = word_count(summary)
        if swc < config.min_summary_words:
            thin.append({"title": page["title"], "section": "Summary", "words": swc})

    # Check: orphan pages (not in any _index.md) — simplified check
    orphans: List[str] = []
    # In a full wiki this checks _index.md files; for now flag pages in flat dirs

    # Check: domain health
    domain_counts: Dict[str, int] = {}
    domain_cross_rels: Dict[str, Set[str]] = {}
    for page in pages_data:
        d = page["domain"]
        domain_counts[d] = domain_counts.get(d, 0) + 1
        if d not in domain_cross_rels:
            domain_cross_rels[d] = set()
        for rel in page["relationships"]:
            for target in rel["targets"]:
                # Check if target is in a different domain
                for other in pages_data:
                    clean = target.split("(")[0].strip() if "(" in target else target
                    if other["title"] == clean and other["domain"] != d:
                        domain_cross_rels[d].add(other["domain"])

    domain_health: List[Dict[str, Any]] = []
    for d, count in domain_counts.items():
        issues = []
        if count < config.min_domain_pages:
            issues.append(f"underdeveloped ({count} pages, min {config.min_domain_pages})")
        cross = len(domain_cross_rels.get(d, set()))
        if cross < config.min_cross_domain_rels:
            issues.append(f"isolated ({cross} cross-domain relationships, min {config.min_cross_domain_rels})")
        if issues:
            domain_health.append({"domain": d, "page_count": count, "issues": issues})

    total_issues = len(dead_rels) + len(stale) + len(thin) + len(orphans) + len(domain_health)

    return {
        "orphan_pages": orphans,
        "dead_relationships": dead_rels,
        "stale_pages": stale,
        "thin_pages": thin,
        "domain_health": domain_health,
        "summary": {
            "pages_scanned": len(pages_data),
            "total_issues": total_issues,
            "dead_rels": len(dead_rels),
            "stale": len(stale),
            "thin": len(thin),
            "orphans": len(orphans),
            "unhealthy_domains": len(domain_health),
        },
    }


def main():
    parser = argparse.ArgumentParser(description="Wiki health checks")
    parser.add_argument("path", nargs="?", help="Wiki directory to lint")
    parser.add_argument("--report", action="store_true", help="JSON report")
    parser.add_argument("--summary", action="store_true", help="Human-readable summary")
    parser.add_argument("--fix", action="store_true", help="Auto-fix where possible")
    parser.add_argument("--config", help="Path to quality-standards.yaml")
    args = parser.parse_args()

    root = get_project_root()
    wiki_dir = Path(args.path) if args.path else root / "wiki"

    # Load config
    config_path = Path(args.config) if args.config else root / "config" / "quality-standards.yaml"
    raw_config = load_config(config_path) or {}
    pq = raw_config.get("page_quality", {})
    dh = raw_config.get("domain_health", {})
    dd = raw_config.get("duplicate_detection", {})

    config = LintConfig(
        stale_threshold_days=pq.get("stale_threshold_days", 30),
        min_summary_words=pq.get("min_summary_words", 30),
        min_deep_analysis_words=pq.get("min_deep_analysis_words", 100),
        min_relationships=pq.get("min_relationships", 1),
        min_domain_pages=dh.get("min_pages", 3),
        min_cross_domain_rels=dh.get("min_cross_domain_relationships", 2),
        similarity_threshold=dd.get("similarity_threshold", 0.70),
    )

    report = lint_wiki(wiki_dir, config)

    if args.report:
        print(json.dumps(report, indent=2))
    else:
        s = report["summary"]
        print(f"Wiki Lint: {s['pages_scanned']} pages scanned")
        print(f"  Dead relationships: {s['dead_rels']}")
        print(f"  Stale pages: {s['stale']}")
        print(f"  Thin pages: {s['thin']}")
        print(f"  Orphan pages: {s['orphans']}")
        print(f"  Unhealthy domains: {s['unhealthy_domains']}")
        print(f"  Total issues: {s['total_issues']}")

        if report["dead_relationships"]:
            print("\nDead relationships:")
            for dr in report["dead_relationships"][:10]:
                print(f"  {dr['source']} --{dr['verb']}--> {dr['target']} (no page)")

        if report["domain_health"]:
            print("\nDomain health:")
            for dh_item in report["domain_health"]:
                print(f"  {dh_item['domain']}: {', '.join(dh_item['issues'])}")


if __name__ == "__main__":
    main()
```

- [ ] **Step 4: Run tests to verify they pass**

```bash
python3 -m pytest tests/test_lint.py -v
```

Expected: All 2 tests PASS.

- [ ] **Step 5: Commit**

```bash
git add tools/lint.py tests/test_lint.py
git commit -m "feat: add wiki linter

tools/lint.py checks for dead relationships, stale pages, thin content,
orphan pages, and domain health. Reports in JSON or human-readable format."
```

---

### Task 8: `tools/export.py`

**Files:**
- Create: `tools/export.py`
- Create: `tests/test_export.py`

- [ ] **Step 1: Write failing tests**

Create `tests/test_export.py`:

```python
"""Tests for tools/export.py — sister project export."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tools.export import transform_page, export_wiki
from tools.common import parse_frontmatter, load_config

FIXTURES = Path(__file__).resolve().parent / "fixtures"
EXPORT_PROFILES = Path(__file__).resolve().parent.parent / "config" / "export-profiles.yaml"


class TestTransformPage:
    def test_openfleet_strips_yaml_frontmatter(self):
        text = (FIXTURES / "valid-concept.md").read_text()
        profiles = load_config(EXPORT_PROFILES) or {}
        profile = profiles.get("openfleet", {})
        result = transform_page(text, profile)
        assert not result.startswith("---")
        assert "**Type:** Research" in result

    def test_openfleet_preserves_relationships(self):
        text = (FIXTURES / "valid-concept.md").read_text()
        profiles = load_config(EXPORT_PROFILES) or {}
        profile = profiles.get("openfleet", {})
        result = transform_page(text, profile)
        assert "## Relationships" in result
        assert "BUILDS ON" in result

    def test_openfleet_adds_source_project_header(self):
        text = (FIXTURES / "valid-concept.md").read_text()
        profiles = load_config(EXPORT_PROFILES) or {}
        profile = profiles.get("openfleet", {})
        result = transform_page(text, profile)
        assert "**Source Project:** devops-solutions-research-wiki" in result

    def test_aicp_converts_to_markdown_headers(self):
        text = (FIXTURES / "valid-concept.md").read_text()
        profiles = load_config(EXPORT_PROFILES) or {}
        profile = profiles.get("aicp", {})
        result = transform_page(text, profile)
        assert not result.startswith("---")
        assert "**Type:** Research Finding" in result
        assert "**Status:** RESEARCHED" in result

    def test_aicp_uses_condensed_resolution(self):
        text = (FIXTURES / "valid-concept.md").read_text()
        profiles = load_config(EXPORT_PROFILES) or {}
        profile = profiles.get("aicp", {})
        result = transform_page(text, profile)
        # Condensed = Summary + Key Insights, no Deep Analysis
        assert "## Summary" in result
        assert "## Key Insights" in result
        assert "## Deep Analysis" not in result
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
python3 -m pytest tests/test_export.py -v
```

Expected: FAIL — `ModuleNotFoundError`

- [ ] **Step 3: Implement `tools/export.py`**

```python
"""Export wiki pages for sister projects.

Transforms frontmatter and content to match target project conventions.
All mappings are config-driven via config/export-profiles.yaml.

Usage:
    python3 tools/export.py openfleet         # Export for openfleet
    python3 tools/export.py aicp              # Export for AICP
    python3 tools/export.py openfleet --dry   # Preview without writing
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

from tools.common import (
    find_wiki_pages,
    get_project_root,
    load_config,
    parse_frontmatter,
    parse_sections,
)


# Resolution defines which sections to include
_RESOLUTION_SECTIONS = {
    "full": None,  # None means include all sections
    "condensed": ["Summary", "Key Insights", "Relationships"],
    "minimal": ["Summary", "Relationships"],
}


def transform_page(text: str, profile: Dict[str, Any]) -> str:
    """Transform a wiki page for export using profile config.

    Profile-driven: type_map, status_map, add_metadata, and resolution
    are all read from the profile dict (loaded from export-profiles.yaml).
    """
    meta, body = parse_frontmatter(text)
    if not meta:
        return text

    transforms = profile.get("transforms", {})
    type_map = transforms.get("type_map", {})
    status_map = transforms.get("status_map", {})
    add_metadata = transforms.get("add_metadata", [])
    resolution = transforms.get("resolution", "full")

    page_type = meta.get("type", "concept")
    mapped_type = type_map.get(page_type, page_type)
    status = meta.get("status", "synthesized")
    mapped_status = status_map.get(status, status.upper())
    updated = str(meta.get("updated", ""))

    # Collect source URLs
    source_urls = []
    for src in meta.get("sources", []):
        if isinstance(src, dict) and "url" in src:
            source_urls.append(src["url"])

    # Build markdown metadata headers
    header_lines = [f"# {meta.get('title', '')}", ""]

    for entry in add_metadata:
        key = entry.get("key", "")
        value_template = entry.get("value", "")
        # Resolve template variables
        value = value_template.replace("{type_mapped}", mapped_type)
        value = value.replace("{status_mapped}", mapped_status)
        value = value.replace("{updated}", updated)
        value = value.replace("{source_urls}", ", ".join(source_urls))
        header_lines.append(f"**{key}:** {value}")

    header_lines.extend(["", "---", ""])

    # Apply resolution filter
    sections = parse_sections(body)
    allowed_sections = _RESOLUTION_SECTIONS.get(resolution)

    if allowed_sections is None:
        # Full resolution: include everything after # Title
        body_lines = body.split("\n")
        content_start = 0
        for i, line in enumerate(body_lines):
            if line.startswith("# "):
                content_start = i + 1
                break
        remaining = "\n".join(body_lines[content_start:]).strip()
        return "\n".join(header_lines) + remaining + "\n"
    else:
        # Filtered resolution
        content_parts = []
        for sec_name in allowed_sections:
            if sec_name in sections:
                content_parts.append(f"## {sec_name}\n\n{sections[sec_name]}")
        return "\n".join(header_lines) + "\n\n".join(content_parts) + "\n"


def _passes_filters(meta: Dict[str, Any], filters: Dict[str, Any]) -> bool:
    """Check if a page passes export filters."""
    confidence_order = ["low", "medium", "high", "authoritative"]
    status_order = ["raw", "processing", "synthesized", "verified"]

    min_conf = filters.get("min_confidence", "medium")
    if meta.get("confidence", "low") in confidence_order:
        if confidence_order.index(meta["confidence"]) < confidence_order.index(min_conf):
            return False

    min_status = filters.get("min_status", "synthesized")
    if meta.get("status", "raw") in status_order:
        if status_order.index(meta["status"]) < status_order.index(min_status):
            return False

    allowed_domains = filters.get("domains")
    if allowed_domains and meta.get("domain") not in allowed_domains:
        return False

    excluded = filters.get("exclude_domains", [])
    if meta.get("domain") in excluded:
        return False

    return True


def export_wiki(wiki_dir: Path, profile_name: str, profiles_path: Path,
                dry_run: bool = False) -> Dict[str, Any]:
    """Export wiki pages for a target project."""
    profiles = load_config(profiles_path)
    if not profiles or profile_name not in profiles:
        return {"error": f"Profile '{profile_name}' not found"}

    profile = profiles[profile_name]
    output_dir = Path(profile.get("output_dir", f"export/{profile_name}"))
    filters = profile.get("filters", {})
    status_map = profile.get("transforms", {}).get("status_map", {})

    transform_profile = profile

    exported = []
    skipped = []

    for md_file in find_wiki_pages(wiki_dir):
        text = md_file.read_text(encoding="utf-8")
        meta, _ = parse_frontmatter(text)
        if not meta:
            skipped.append({"file": str(md_file), "reason": "no frontmatter"})
            continue

        if not _passes_filters(meta, filters):
            skipped.append({"file": str(md_file), "reason": "failed filters"})
            continue

        transformed = transform_page(text, transform_profile)

        if not dry_run:
            out_path = output_dir / md_file.name
            out_path.parent.mkdir(parents=True, exist_ok=True)
            out_path.write_text(transformed, encoding="utf-8")

        exported.append({"file": str(md_file), "output": str(output_dir / md_file.name)})

    return {
        "profile": profile_name,
        "output_dir": str(output_dir),
        "exported": len(exported),
        "skipped": len(skipped),
        "exported_files": exported,
        "skipped_files": skipped,
        "dry_run": dry_run,
    }


def main():
    parser = argparse.ArgumentParser(description="Export wiki for sister projects")
    parser.add_argument("profile", help="Export profile name (openfleet, aicp)")
    parser.add_argument("--wiki", help="Wiki directory path")
    parser.add_argument("--profiles", help="Path to export-profiles.yaml")
    parser.add_argument("--dry", action="store_true", help="Preview without writing")
    args = parser.parse_args()

    root = get_project_root()
    wiki_dir = Path(args.wiki) if args.wiki else root / "wiki"
    profiles_path = Path(args.profiles) if args.profiles else root / "config" / "export-profiles.yaml"

    result = export_wiki(wiki_dir, args.profile, profiles_path, dry_run=args.dry)

    if "error" in result:
        print(f"Error: {result['error']}")
        sys.exit(1)

    prefix = "[DRY RUN] " if result["dry_run"] else ""
    print(f"{prefix}Export '{result['profile']}': {result['exported']} pages exported, {result['skipped']} skipped")
    print(f"{prefix}Output: {result['output_dir']}")

    if result["skipped_files"]:
        print("\nSkipped:")
        for s in result["skipped_files"]:
            print(f"  {s['file']}: {s['reason']}")


if __name__ == "__main__":
    main()
```

- [ ] **Step 4: Run tests to verify they pass**

```bash
python3 -m pytest tests/test_export.py -v
```

Expected: All 5 tests PASS (now config-driven via export-profiles.yaml).

- [ ] **Step 5: Commit**

```bash
git add tools/export.py tests/test_export.py
git commit -m "feat: add wiki export tool

tools/export.py transforms wiki pages for openfleet (LightRAG-compatible)
and AICP (LocalAI Collections). Handles frontmatter conversion, type
mapping, status mapping, resolution filtering, and domain-based filtering."
```

---

### Task 9: `tools/stats.py`

**Files:**
- Create: `tools/stats.py`

- [ ] **Step 1: Implement `tools/stats.py`**

```python
"""Wiki coverage and growth reporting.

Usage:
    python3 tools/stats.py             # Human-readable report
    python3 tools/stats.py --json      # JSON output
"""

import argparse
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict

from tools.common import get_project_root, load_config
from tools.manifest import build_manifest


def build_stats(wiki_dir: Path) -> Dict[str, Any]:
    """Build statistics from wiki content."""
    manifest = build_manifest(wiki_dir)
    pages = manifest["pages"]

    # Counts by dimension
    by_type = Counter(p["type"] for p in pages)
    by_domain = Counter(p["domain"] for p in pages)
    by_status = Counter(p["status"] for p in pages)
    by_confidence = Counter(p["confidence"] for p in pages)

    # Relationship density
    rel_counts = [(p["title"], len(p["relationships"])) for p in pages]
    rel_counts.sort(key=lambda x: x[1], reverse=True)
    avg_rels = sum(c for _, c in rel_counts) / max(len(rel_counts), 1)

    # Tag cloud
    all_tags: list = []
    for p in pages:
        all_tags.extend(p.get("tags", []))
    tag_counts = Counter(all_tags).most_common(20)

    # Freshness buckets
    from datetime import datetime, timedelta
    now = datetime.now()
    freshness = {"<7d": 0, "<30d": 0, "<90d": 0, ">90d": 0, "unknown": 0}
    for p in pages:
        updated = p.get("updated", "")
        if not updated:
            freshness["unknown"] += 1
            continue
        try:
            dt = datetime.strptime(updated[:10], "%Y-%m-%d")
            age = (now - dt).days
            if age < 7:
                freshness["<7d"] += 1
            elif age < 30:
                freshness["<30d"] += 1
            elif age < 90:
                freshness["<90d"] += 1
            else:
                freshness[">90d"] += 1
        except ValueError:
            freshness["unknown"] += 1

    # Gap scores per domain
    domain_gaps: Dict[str, Dict[str, Any]] = {}
    orphaned = manifest.get("orphaned_refs", [])
    orphan_by_referrer_domain: Dict[str, int] = defaultdict(int)
    for o in orphaned:
        for ref_title in o["referenced_by"]:
            for p in pages:
                if p["title"] == ref_title:
                    orphan_by_referrer_domain[p["domain"]] += 1

    for domain, count in by_domain.items():
        total_rels = sum(len(p["relationships"]) for p in pages if p["domain"] == domain)
        orphan_count = orphan_by_referrer_domain.get(domain, 0)
        gap_score = orphan_count / max(total_rels, 1)
        domain_gaps[domain] = {
            "pages": count,
            "relationships": total_rels,
            "orphaned_refs": orphan_count,
            "gap_score": round(gap_score, 3),
        }

    return {
        "total_pages": len(pages),
        "by_type": dict(by_type),
        "by_domain": dict(by_domain),
        "by_status": dict(by_status),
        "by_confidence": dict(by_confidence),
        "relationship_density": {
            "average_per_page": round(avg_rels, 1),
            "most_connected": rel_counts[:5] if rel_counts else [],
            "least_connected": rel_counts[-5:] if rel_counts else [],
        },
        "tag_cloud": tag_counts,
        "freshness": freshness,
        "domain_gaps": domain_gaps,
        "orphaned_refs_total": len(orphaned),
    }


def main():
    parser = argparse.ArgumentParser(description="Wiki coverage and growth report")
    parser.add_argument("--json", action="store_true", help="JSON output")
    parser.add_argument("--wiki", help="Wiki directory path")
    args = parser.parse_args()

    root = get_project_root()
    wiki_dir = Path(args.wiki) if args.wiki else root / "wiki"

    stats = build_stats(wiki_dir)

    if args.json:
        print(json.dumps(stats, indent=2))
    else:
        print(f"=== Wiki Stats ===")
        print(f"Total pages: {stats['total_pages']}")
        print(f"\nBy type: {json.dumps(stats['by_type'], indent=2)}")
        print(f"\nBy domain: {json.dumps(stats['by_domain'], indent=2)}")
        print(f"\nBy status: {json.dumps(stats['by_status'], indent=2)}")
        print(f"\nBy confidence: {json.dumps(stats['by_confidence'], indent=2)}")
        print(f"\nRelationship density: {stats['relationship_density']['average_per_page']} avg/page")
        if stats['relationship_density']['most_connected']:
            print(f"  Most connected: {stats['relationship_density']['most_connected'][:3]}")
        print(f"\nTop tags: {stats['tag_cloud'][:10]}")
        print(f"\nFreshness: {json.dumps(stats['freshness'], indent=2)}")
        print(f"\nOrphaned refs: {stats['orphaned_refs_total']}")
        print(f"\nDomain gaps:")
        for d, g in stats["domain_gaps"].items():
            print(f"  {d}: {g['pages']} pages, gap score {g['gap_score']}")


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Smoke test**

```bash
python3 tools/stats.py --wiki tests/fixtures --json
```

Expected: JSON output with stats from fixtures.

- [ ] **Step 3: Commit**

```bash
git add tools/stats.py
git commit -m "feat: add wiki stats reporting tool

tools/stats.py reports page counts by dimension, relationship density,
tag cloud, freshness distribution, and domain gap scores."
```

---

## Phase 3: Wiki-Agent Skill & Seed Content (Tasks 10-12)

### Task 10: Wiki-Agent Skill

**Files:**
- Create: `skills/wiki-agent/skill.md`

- [ ] **Step 1: Create `skills/wiki-agent/skill.md`**

Write the full skill as specified in Section 7 of the design spec. The content is defined verbatim in the spec at `docs/superpowers/specs/2026-04-08-research-wiki-design.md` lines 587-711.

```markdown
# Wiki Agent — Research Wiki Operator

You are operating the devops-solutions-research-wiki. You ingest sources,
query knowledge, maintain quality, and export for sister projects.

Read CLAUDE.md for schema and conventions. Read config/schema.yaml for
validation rules. Read config/domains.yaml for the domain registry.

## Operations

### Ingest

Trigger: user says "ingest", provides a URL, drops a file, or pastes content.
Mode: auto | guided | smart (default: smart)

Pipeline:
1. EXTRACT — read raw source, classify type, normalize formatting
2. ANALYZE — identify domains, concepts, claims, relationships to existing pages
3. SYNTHESIZE — generate wiki pages with full frontmatter and all sections
4. WRITE — save pages to wiki/ (source-synthesis in sources/, concepts in domains/)
5. INTEGRATE — update _index.md files, rebuild manifest.json, validate

For guided mode: present the full extraction plan between ANALYZE and SYNTHESIZE.
Include: source page name, concept pages to create (with domains), concept pages
to update (with what changes), new domains needed, estimated relationship count.
Wait for user approval before proceeding.

For smart mode: decide based on these escalation triggers:
- New domain creation needed → guided
- Contradictions with existing knowledge → guided
- Source is ambiguous or multi-interpretation → guided
- Complexity is expert-level → guided
- Source is low-quality or off-topic → flag and ask
- Everything else → auto

Quality gates (every page):
- Complete frontmatter per config/schema.yaml
- Summary >= 30 words
- At least 1 relationship (unless first in new domain)
- Page listed in domain _index.md
- Source provenance present
- No >70% concept overlap with existing page (update instead)
- title matches # Heading, domain matches folder

Post-ingestion (every time):
1. Update affected _index.md files
2. Run: python3 tools/manifest.py
3. Run: python3 tools/validate.py
4. Flag stale pages needing review
5. Report summary: sources processed, pages created/updated, domains affected,
   relationships added, any warnings

### Query

Trigger: user asks a question about wiki content.

Process:
1. Read wiki/index.md for domain overview
2. Identify relevant domain(s)
3. Read domain _index.md for topic inventory
4. Read relevant pages
5. Synthesize answer
6. Cite which wiki pages informed the answer with file paths

If the answer requires information not in the wiki, say so and offer to research
and ingest new sources.

### Lint

Trigger: user says "lint", "health check", or "check wiki".

Run: python3 tools/lint.py --report

Checks:
- Orphan pages (exist in wiki/ but not in any _index.md)
- Dead relationships (targets that don't resolve to any page)
- Stale pages (updated > 30 days ago, status != stale)
- Thin pages (< 100 words in Deep Analysis for concept/deep-dive types)
- Duplicate detection (>70% Summary overlap between pages)
- Domain balance (domains with < 3 pages flagged as underdeveloped)
- Open Questions density (Open Questions > Deep Analysis word count)
- Isolated clusters (domains with no cross-domain relationships)

Report findings. Offer to fix autonomously or in guided mode.

### Gap Analysis

Trigger: user says "gaps", "what's missing", or "research priorities".

Process:
1. Parse manifest.json for the full relationship graph
2. Find relationship targets that don't have their own wiki page
3. Find domains with few pages or low relationship density
4. Aggregate Open Questions sections across all pages
5. Identify domains with no cross-domain connections

Output: prioritized list of research opportunities with suggested sources.

### Export

Trigger: user says "export for {target}" where target is openfleet, aicp, etc.

Process:
1. Read config/export-profiles.yaml for target configuration
2. Filter pages by min_confidence, min_status, domain filters
3. Transform frontmatter per profile (YAML → markdown headers, type mapping)
4. Copy to target output_dir
5. Report: pages exported, pages skipped (with reasons)

### Stats

Trigger: user says "stats", "status", or "dashboard".

Run: python3 tools/stats.py

Report:
- Total pages by type, domain, status, confidence
- Relationship density (edges per page, most/least connected pages)
- Tag cloud (top 20 tags)
- Freshness (pages by last-updated bucket: <7d, <30d, <90d, >90d)
- Growth over time (pages added per week, from git history)
- Gap score per domain (orphaned refs / total refs ratio)
- Export readiness (% of pages passing each export profile's filters)
```

- [ ] **Step 2: Commit**

```bash
git add skills/wiki-agent/skill.md
git commit -m "feat: add wiki-agent skill

Master skill defining all wiki operations: ingest (3 modes), query,
lint, gap analysis, export, and stats."
```

---

### Task 11: Wiki Seed Structure

**Files:**
- Create: `wiki/index.md`
- Create: `wiki/domains/_index.md`
- Create: `wiki/domains/ai-agents/_index.md`
- Create: `wiki/domains/knowledge-systems/_index.md`
- Create: `wiki/domains/automation/_index.md`
- Create: `wiki/domains/tools-and-platforms/_index.md`

- [ ] **Step 1: Create `wiki/index.md`**

```markdown
# Research Wiki — Master Index

Central knowledge base for the devops ecosystem. Synthesized from research
across articles, transcripts, papers, and hands-on experience.

## Domains

See [domains/_index.md](domains/_index.md) for the full domain registry.

## Quick Stats

Run `python3 tools/stats.py` for current coverage and health metrics.

## Recent Activity

<!-- Auto-updated by wiki-agent after ingestion -->

## Navigation

- **By domain**: `wiki/domains/{domain}/_index.md`
- **By source**: `wiki/sources/src-{slug}.md`
- **Cross-cutting**: `wiki/comparisons/`
- **Machine-readable**: `wiki/manifest.json`
```

- [ ] **Step 2: Create `wiki/domains/_index.md`**

```markdown
# Domain Registry

| Domain | Description | Pages |
|--------|-------------|-------|
| [ai-agents](ai-agents/_index.md) | Multi-agent systems, orchestration, fleet management, agent memory | 0 |
| [knowledge-systems](knowledge-systems/_index.md) | RAG, knowledge graphs, wikis, embeddings, search, synthesis | 0 |
| [automation](automation/_index.md) | Scheduling, pipelines, workflow automation, cron, task orchestration | 0 |
| [tools-and-platforms](tools-and-platforms/_index.md) | Software tools, platforms, IDEs, CLI tools, SaaS products | 0 |

<!-- More domains added as topics emerge -->
```

- [ ] **Step 3: Create domain `_index.md` files**

Create `wiki/domains/ai-agents/_index.md`:
```markdown
# AI Agents

Multi-agent systems, orchestration, fleet management, agent memory.

## Pages

<!-- Pages added during ingestion -->

## Tags

<!-- Tag cloud generated during ingestion -->
```

Create `wiki/domains/knowledge-systems/_index.md`:
```markdown
# Knowledge Systems

RAG, knowledge graphs, wikis, embeddings, search, synthesis.

## Pages

<!-- Pages added during ingestion -->

## Tags

<!-- Tag cloud generated during ingestion -->
```

Create `wiki/domains/automation/_index.md`:
```markdown
# Automation

Scheduling, pipelines, workflow automation, cron, task orchestration.

## Pages

<!-- Pages added during ingestion -->

## Tags

<!-- Tag cloud generated during ingestion -->
```

Create `wiki/domains/tools-and-platforms/_index.md`:
```markdown
# Tools and Platforms

Software tools, platforms, IDEs, CLI tools, SaaS products.

## Pages

<!-- Pages added during ingestion -->

## Tags

<!-- Tag cloud generated during ingestion -->
```

- [ ] **Step 4: Commit**

```bash
git add wiki/
git commit -m "feat: add wiki seed structure

Master index, domain registry, and initial domain _index.md files
for ai-agents, knowledge-systems, automation, tools-and-platforms."
```

---

### Task 12: Proof of Life — Ingest the Two Transcripts

**Files:**
- Create: `wiki/sources/src-claude-notebooklm-content-team.md`
- Create: `wiki/sources/src-karpathy-claude-code-10x.md`
- Create: wiki concept pages (determined during ingestion)
- Update: domain `_index.md` files
- Generate: `wiki/manifest.json`

This task is executed by Claude using the wiki-agent skill, not by writing code. It proves the entire system works end-to-end.

- [ ] **Step 1: Ingest first transcript in guided mode**

```
Ingest raw/transcripts/claude-notebooklm-content-team.txt — guided mode
```

Review the extraction plan. Verify:
- Source-synthesis page created in `wiki/sources/`
- Concept pages created in appropriate domains
- Frontmatter is complete and valid
- Relationships link to other pages and source page

- [ ] **Step 2: Ingest second transcript in guided mode**

```
Ingest raw/transcripts/karpathy-claude-code-10x.txt — guided mode
```

This transcript should produce cross-references to pages created from the first transcript.

- [ ] **Step 3: Run validation**

```bash
python3 tools/validate.py
```

Expected: exit code 0, all pages pass.

- [ ] **Step 4: Build manifest**

```bash
python3 tools/manifest.py
```

Verify `wiki/manifest.json` contains all pages, relationships, and identifies orphaned refs.

- [ ] **Step 5: Run lint**

```bash
python3 tools/lint.py
```

Review any issues. Fix what makes sense.

- [ ] **Step 6: Run stats**

```bash
python3 tools/stats.py
```

Verify: multiple domains populated, relationships mapped, no critical gaps.

- [ ] **Step 7: Commit all wiki content**

```bash
git add wiki/ raw/
git commit -m "feat: seed wiki with two transcript ingestions

Proof-of-life: ingested Claude+NotebookLM and Karpathy+Claude Code
transcripts. Created source-synthesis pages, concept pages across
multiple domains, with cross-references and full frontmatter."
```

---

## Phase 4: Verification (Task 13)

### Task 13: End-to-End Verification

- [ ] **Step 1: Run full test suite**

```bash
python3 -m pytest tests/ -v
```

Expected: All tests pass.

- [ ] **Step 2: Run validate on entire wiki**

```bash
python3 tools/validate.py
```

Expected: exit code 0.

- [ ] **Step 3: Run lint on entire wiki**

```bash
python3 tools/lint.py
```

Expected: no blocking issues (warnings acceptable for new wiki).

- [ ] **Step 4: Test export dry-run for openfleet**

```bash
python3 tools/export.py openfleet --dry
```

Expected: pages listed for export, correct transforms shown.

- [ ] **Step 5: Test export dry-run for AICP**

```bash
python3 tools/export.py aicp --dry
```

Expected: pages listed with condensed resolution, correct status mapping.

- [ ] **Step 6: Verify manifest completeness**

```bash
python3 -c "import json; m=json.load(open('wiki/manifest.json')); print(f'Pages: {m[\"stats\"][\"pages\"]}, Rels: {m[\"stats\"][\"relationships\"]}, Orphans: {len(m[\"orphaned_refs\"])}')"
```

Expected: Pages > 5, Relationships > 10, some orphaned refs (expected for new wiki).

- [ ] **Step 7: Final commit if any fixes needed**

```bash
git add -A
git commit -m "fix: address verification findings"
```

Only if there are uncommitted fixes from steps 1-6.
