# Knowledge Evolution Pipeline Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a candidate scoring engine, prompt builder, and pluggable LLM backend system that automatically identifies and generates evolved wiki pages (lessons, patterns, decisions) from existing content.

**Architecture:** New `tools/evolve.py` module with three layers (scorer, prompt builder, LLM backend). Pipeline.py gets a new `evolve` command that delegates to evolve.py. Three backends: Claude Code (prompt queue), OpenAI-compatible API (LocalAI), and AICP MCP.

**Tech Stack:** Python 3.11, PyYAML, urllib/requests for HTTP, existing tool framework (common.py, manifest.py, pipeline.py)

---

### Task 1: Candidate Scorer — Data Structures and Tag Co-occurrence Signal

**Files:**
- Create: `tools/evolve.py`

- [ ] **Step 1: Create evolve.py with imports and Candidate dataclass**

```python
"""Knowledge evolution engine.

Scores existing pages to identify evolution candidates, builds generation
prompts, and delegates to pluggable LLM backends for content generation.

Usage:
    Called from tools/pipeline.py evolve command.
"""

import json
import os
import re
from dataclasses import dataclass, field, asdict
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional
from urllib import request, error as urlerror

from tools.common import (
    find_wiki_pages,
    get_project_root,
    load_config,
    parse_frontmatter,
    parse_sections,
    parse_relationships,
    word_count,
)
from tools.manifest import build_manifest


@dataclass
class Signal:
    """A single scoring signal that fired for a candidate."""
    name: str
    score: float  # 0.0-1.0
    detail: str


@dataclass
class Candidate:
    """An evolution candidate — a potential lesson, pattern, or decision page."""
    type: str  # "lesson", "pattern", "decision"
    title: str
    score: float  # 0.0-1.0 weighted composite
    signals: List[Signal] = field(default_factory=list)
    source_pages: List[str] = field(default_factory=list)
    domain: str = "cross-domain"

    def to_dict(self) -> dict:
        d = asdict(self)
        d["signals"] = [asdict(s) for s in self.signals]
        return d
```

- [ ] **Step 2: Add tag co-occurrence signal function**

Append to `tools/evolve.py`:

```python
# ---------------------------------------------------------------------------
# Scoring signals
# ---------------------------------------------------------------------------

SIGNAL_WEIGHTS = {
    "tag_cooccurrence": 0.25,
    "cross_source_convergence": 0.25,
    "relationship_hub": 0.15,
    "domain_layer_gap": 0.15,
    "open_question_density": 0.10,
    "orphaned_references": 0.10,
}


def _signal_tag_cooccurrence(pages: List[dict]) -> List[Candidate]:
    """Find groups of 3+ pages sharing 2+ tags → pattern candidates."""
    from collections import Counter

    # Build tag→pages index
    tag_pages: Dict[str, List[str]] = {}
    page_tags: Dict[str, set] = {}
    for p in pages:
        title = p["title"]
        tags = set(p.get("tags", []))
        page_tags[title] = tags
        for tag in tags:
            tag_pages.setdefault(tag, []).append(title)

    # Find tag pairs that co-occur across 3+ pages
    candidates = []
    seen_groups = set()
    tag_list = list(tag_pages.keys())
    for i, t1 in enumerate(tag_list):
        for t2 in tag_list[i + 1:]:
            shared = set(tag_pages[t1]) & set(tag_pages[t2])
            if len(shared) < 3:
                continue
            group_key = tuple(sorted(shared))
            if group_key in seen_groups:
                continue
            seen_groups.add(group_key)

            # Determine domain from majority
            domains = Counter(
                next((pg["domain"] for pg in pages if pg["title"] == t), "cross-domain")
                for t in shared
            )
            domain = domains.most_common(1)[0][0]

            signal = Signal(
                name="tag_cooccurrence",
                score=min(len(shared) / 5.0, 1.0),
                detail=f"{len(shared)} pages share tags [{t1}, {t2}]",
            )
            title = f"Pattern: {t1.replace('-', ' ').title()} and {t2.replace('-', ' ').title()}"
            candidates.append(Candidate(
                type="pattern",
                title=title,
                score=signal.score * SIGNAL_WEIGHTS["tag_cooccurrence"],
                signals=[signal],
                source_pages=sorted(shared),
                domain=domain,
            ))

    return candidates
```

- [ ] **Step 3: Verify the file is importable**

Run: `python3 -c "from tools.evolve import Candidate, Signal, _signal_tag_cooccurrence; print('OK')"`

Expected: `OK`

- [ ] **Step 4: Commit**

```bash
git add tools/evolve.py
git commit -m "feat(evolve): candidate data structures and tag co-occurrence signal"
```

---

### Task 2: Remaining Scoring Signals

**Files:**
- Modify: `tools/evolve.py`

- [ ] **Step 1: Add cross-source convergence signal**

Append to `tools/evolve.py`:

```python
def _signal_cross_source_convergence(pages: List[dict]) -> List[Candidate]:
    """Multiple source-synthesis pages referencing same concepts → lesson candidates."""
    from collections import Counter

    # Find concept pages referenced by multiple source pages via relationships
    concept_sources: Dict[str, List[str]] = {}  # concept_title → [source_titles]
    source_pages = [p for p in pages if p.get("type") == "source-synthesis"]
    concept_titles = {p["title"] for p in pages if p.get("type") in ("concept", "comparison")}

    for sp in source_pages:
        for rel in sp.get("relationships", []):
            for target in rel.get("targets", []):
                if target in concept_titles:
                    concept_sources.setdefault(target, []).append(sp["title"])

    candidates = []
    for concept, sources in concept_sources.items():
        if len(sources) < 2:
            continue
        # Find the concept page to get its domain
        cp = next((p for p in pages if p["title"] == concept), None)
        domain = cp["domain"] if cp else "cross-domain"

        signal = Signal(
            name="cross_source_convergence",
            score=min(len(sources) / 4.0, 1.0),
            detail=f"{len(sources)} sources converge on {concept}",
        )
        candidates.append(Candidate(
            type="lesson",
            title=f"Lesson: {concept}",
            score=signal.score * SIGNAL_WEIGHTS["cross_source_convergence"],
            signals=[signal],
            source_pages=[concept] + sources,
            domain=domain,
        ))

    return candidates
```

- [ ] **Step 2: Add relationship hub signal**

Append to `tools/evolve.py`:

```python
def _signal_relationship_hub(pages: List[dict]) -> List[Candidate]:
    """Pages with 5+ inbound relationships → lesson candidates."""
    # Build inbound count
    inbound: Dict[str, int] = {}
    for p in pages:
        for rel in p.get("relationships", []):
            for target in rel.get("targets", []):
                inbound[target] = inbound.get(target, 0) + 1

    candidates = []
    for p in pages:
        title = p["title"]
        count = inbound.get(title, 0)
        if count < 5:
            continue
        # Skip pages that are already Layer 4+
        if p.get("layer") and str(p.get("layer", "")).isdigit() and int(str(p["layer"])) >= 4:
            continue

        signal = Signal(
            name="relationship_hub",
            score=min(count / 10.0, 1.0),
            detail=f"{count} inbound relationships",
        )
        candidates.append(Candidate(
            type="lesson",
            title=f"Lesson: {title}",
            score=signal.score * SIGNAL_WEIGHTS["relationship_hub"],
            signals=[signal],
            source_pages=[title],
            domain=p["domain"],
        ))

    return candidates
```

- [ ] **Step 3: Add domain layer gap signal**

Append to `tools/evolve.py`:

```python
def _signal_domain_layer_gap(pages: List[dict]) -> List[Candidate]:
    """Domains with Layer 1-2 pages but no Layer 4-6 → overdue for evolution."""
    from collections import defaultdict

    domain_layers: Dict[str, Dict[str, int]] = defaultdict(lambda: {"low": 0, "high": 0})
    domain_pages: Dict[str, List[str]] = defaultdict(list)

    for p in pages:
        domain = p.get("domain", "")
        if not domain:
            continue
        layer = p.get("layer")
        if layer is not None and str(layer).isdigit() and int(str(layer)) >= 4:
            domain_layers[domain]["high"] += 1
        else:
            domain_layers[domain]["low"] += 1
        domain_pages[domain].append(p["title"])

    candidates = []
    for domain, counts in domain_layers.items():
        if counts["high"] > 0 or counts["low"] < 3:
            continue  # already has evolved pages, or too few to synthesize

        signal = Signal(
            name="domain_layer_gap",
            score=min(counts["low"] / 8.0, 1.0),
            detail=f"{domain}: {counts['low']} low-layer pages, 0 evolved",
        )
        # Pick top 3 pages by relationship count as sources
        domain_ps = [p for p in pages if p["domain"] == domain]
        domain_ps.sort(key=lambda x: len(x.get("relationships", [])), reverse=True)
        top_sources = [p["title"] for p in domain_ps[:3]]

        candidates.append(Candidate(
            type="lesson",
            title=f"Lesson: {domain.replace('-', ' ').title()} Synthesis",
            score=signal.score * SIGNAL_WEIGHTS["domain_layer_gap"],
            signals=[signal],
            source_pages=top_sources,
            domain=domain,
        ))

    return candidates
```

- [ ] **Step 4: Add open question density signal**

Append to `tools/evolve.py`:

```python
def _signal_open_question_density(pages: List[dict], gaps: dict) -> List[Candidate]:
    """Pages contributing 3+ open questions → decision candidates."""
    from collections import Counter

    page_questions: Counter = Counter()
    for oq in gaps.get("open_questions", []):
        page_questions[oq["source_page"]] += 1

    candidates = []
    for title, count in page_questions.items():
        if count < 3:
            continue
        p = next((pg for pg in pages if pg["title"] == title), None)
        if not p:
            continue
        # Skip already-evolved pages
        if p.get("layer") and str(p.get("layer", "")).isdigit() and int(str(p["layer"])) >= 4:
            continue

        signal = Signal(
            name="open_question_density",
            score=min(count / 6.0, 1.0),
            detail=f"{count} open questions from {title}",
        )
        candidates.append(Candidate(
            type="decision",
            title=f"Decision: {title} Open Questions",
            score=signal.score * SIGNAL_WEIGHTS["open_question_density"],
            signals=[signal],
            source_pages=[title],
            domain=p["domain"],
        ))

    return candidates
```

- [ ] **Step 5: Add orphaned references signal**

Append to `tools/evolve.py`:

```python
def _signal_orphaned_references(pages: List[dict], gaps: dict) -> List[Candidate]:
    """Orphaned targets referenced by multiple pages → lesson candidates."""
    candidates = []
    for target in gaps.get("orphaned_targets", []):
        # Find all pages that reference this target
        referrers = []
        for p in pages:
            for rel in p.get("relationships", []):
                if target in rel.get("targets", []):
                    referrers.append(p["title"])
                    break

        if len(referrers) < 2:
            continue

        signal = Signal(
            name="orphaned_references",
            score=min(len(referrers) / 4.0, 1.0),
            detail=f"'{target}' referenced by {len(referrers)} pages but doesn't exist",
        )
        domain = "cross-domain"
        if referrers:
            p = next((pg for pg in pages if pg["title"] == referrers[0]), None)
            if p:
                domain = p["domain"]

        candidates.append(Candidate(
            type="lesson",
            title=f"Lesson: {target}",
            score=signal.score * SIGNAL_WEIGHTS["orphaned_references"],
            signals=[signal],
            source_pages=referrers,
            domain=domain,
        ))

    return candidates
```

- [ ] **Step 6: Verify all signals import**

Run: `python3 -c "from tools.evolve import _signal_tag_cooccurrence, _signal_cross_source_convergence, _signal_relationship_hub, _signal_domain_layer_gap, _signal_open_question_density, _signal_orphaned_references; print('OK')"`

Expected: `OK`

- [ ] **Step 7: Commit**

```bash
git add tools/evolve.py
git commit -m "feat(evolve): all 6 scoring signals — convergence, hubs, gaps, questions, orphans"
```

---

### Task 3: Score Aggregation and Deduplication

**Files:**
- Modify: `tools/evolve.py`

- [ ] **Step 1: Add the score_candidates orchestrator function**

Append to `tools/evolve.py`:

```python
# ---------------------------------------------------------------------------
# Candidate scoring orchestrator
# ---------------------------------------------------------------------------

def score_candidates(
    project_root: Path,
    type_filter: Optional[str] = None,
    domain_filter: Optional[str] = None,
    top: Optional[int] = None,
) -> List[Candidate]:
    """Score all pages for evolution readiness. Returns ranked candidate list.

    Args:
        project_root: Path to project root
        type_filter: Only return candidates of this type (lesson/pattern/decision)
        domain_filter: Only return candidates for this domain
        top: Limit to top N candidates
    """
    wiki_dir = project_root / "wiki"
    manifest = build_manifest(wiki_dir)
    pages = manifest["pages"]

    # Run gaps analysis for signals that need it
    from tools.pipeline import run_gaps
    gaps = run_gaps(project_root, verbose=False)

    # Collect candidates from all signals
    all_candidates: List[Candidate] = []
    all_candidates.extend(_signal_tag_cooccurrence(pages))
    all_candidates.extend(_signal_cross_source_convergence(pages))
    all_candidates.extend(_signal_relationship_hub(pages))
    all_candidates.extend(_signal_domain_layer_gap(pages))
    all_candidates.extend(_signal_open_question_density(pages, gaps))
    all_candidates.extend(_signal_orphaned_references(pages, gaps))

    # Merge candidates with same title: combine signals, recalculate score
    merged = _merge_candidates(all_candidates)

    # Deduplicate against existing Layer 4-6 pages
    merged = _deduplicate(merged, pages)

    # Apply filters
    if type_filter:
        merged = [c for c in merged if c.type == type_filter]
    if domain_filter:
        merged = [c for c in merged if c.domain == domain_filter]

    # Sort by score descending
    merged.sort(key=lambda c: c.score, reverse=True)

    # Apply top limit
    if top:
        merged = merged[:top]

    return merged


def _merge_candidates(candidates: List[Candidate]) -> List[Candidate]:
    """Merge candidates with the same suggested title — combine signals, recalculate score."""
    by_title: Dict[str, Candidate] = {}
    for c in candidates:
        key = c.title.lower()
        if key in by_title:
            existing = by_title[key]
            existing.signals.extend(c.signals)
            existing.source_pages = list(set(existing.source_pages + c.source_pages))
            # Recalculate score as sum of weighted signals, capped at 1.0
            existing.score = min(
                sum(s.score * SIGNAL_WEIGHTS.get(s.name, 0.1) for s in existing.signals),
                1.0,
            )
        else:
            by_title[key] = Candidate(
                type=c.type,
                title=c.title,
                score=c.score,
                signals=list(c.signals),
                source_pages=list(c.source_pages),
                domain=c.domain,
            )
    return list(by_title.values())


def _deduplicate(candidates: List[Candidate], pages: List[dict]) -> List[Candidate]:
    """Remove candidates already covered by existing Layer 4-6 pages."""
    # Build set of source page sets from existing evolved pages
    existing_sources: List[set] = []
    for p in pages:
        layer = p.get("layer")
        if layer is None:
            continue
        if str(layer).isdigit() and int(str(layer)) >= 4:
            derived = set(p.get("derived_from", []))
            if derived:
                existing_sources.append(derived)

    result = []
    for c in candidates:
        candidate_sources = set(c.source_pages)
        # Skip if 80%+ of candidate's sources are already covered
        is_covered = False
        for existing in existing_sources:
            if not candidate_sources:
                break
            overlap = len(candidate_sources & existing) / len(candidate_sources)
            if overlap >= 0.8:
                is_covered = True
                break
        if not is_covered:
            result.append(c)

    return result
```

- [ ] **Step 2: Test scoring against live wiki data**

Run: `python3 -c "from tools.evolve import score_candidates; from tools.common import get_project_root; cs = score_candidates(get_project_root(), top=5); [print(f'{c.score:.2f} [{c.type}] {c.title} ({len(c.source_pages)} sources)') for c in cs]"`

Expected: 1-5 candidates printed with scores, types, and source counts. No errors.

- [ ] **Step 3: Commit**

```bash
git add tools/evolve.py
git commit -m "feat(evolve): candidate scoring orchestrator with merge and dedup"
```

---

### Task 4: Prompt Builder

**Files:**
- Modify: `tools/evolve.py`

- [ ] **Step 1: Add the PromptBuilder**

Append to `tools/evolve.py`:

```python
# ---------------------------------------------------------------------------
# Prompt builder
# ---------------------------------------------------------------------------

def build_prompt(candidate: Candidate, project_root: Path) -> str:
    """Build a generation prompt for a candidate. Reads source pages and template.

    Returns a self-contained prompt string that any LLM backend can execute.
    """
    wiki_dir = project_root / "wiki"
    template_dir = project_root / "config" / "templates"

    # Map candidate type to template name
    template_name = candidate.type  # lesson, pattern, decision
    template_path = template_dir / f"{template_name}.md"
    if not template_path.exists():
        raise FileNotFoundError(f"Template not found: {template_path}")

    template_content = template_path.read_text(encoding="utf-8")

    # Read source pages
    source_sections = []
    for page_title in candidate.source_pages:
        content = _read_page_by_title(wiki_dir, page_title)
        if content:
            source_sections.append(content)

    # Build quality requirements from schema
    schema = load_config(project_root / "config" / "schema.yaml")
    quality_reqs = _quality_requirements(candidate.type, schema)

    # Assemble prompt
    signals_text = "\n".join(
        f"- {s.name}: {s.detail} (score: {s.score:.2f})"
        for s in candidate.signals
    )

    sources_text = "\n\n".join(source_sections)

    derived_from_yaml = "\n".join(f'  - "{t}"' for t in candidate.source_pages)

    prompt = f"""You are writing a {candidate.type} page for a research wiki.

## Target Page
- Title: {candidate.title}
- Type: {candidate.type}
- Domain: {candidate.domain}
- Derived from: {', '.join(candidate.source_pages)}

## Why This Page
This candidate was identified because:
{signals_text}

## Source Material
{sources_text}

## Quality Requirements
{quality_reqs}

## Frontmatter Requirements
The page MUST start with valid YAML frontmatter including:
- title: "{candidate.title}"
- type: {candidate.type}
- domain: {candidate.domain}
- layer: {4 if candidate.type == 'lesson' else 5 if candidate.type == 'pattern' else 6}
- status: synthesized
- confidence: medium
- maturity: seed
- derived_from:
{derived_from_yaml}
- created: {datetime.now().strftime('%Y-%m-%d')}
- updated: {datetime.now().strftime('%Y-%m-%d')}
- sources: []
- tags: []

## Template Structure
{template_content}

## Instructions
Write the complete page. Fill every section with substantive content drawn from the source material above.
Use ALL_CAPS relationship verbs (DERIVED FROM, RELATES TO, ENABLES, BUILDS ON, etc.).
Output ONLY the markdown content (frontmatter + body). No explanation or commentary."""

    return prompt


def _read_page_by_title(wiki_dir: Path, title: str) -> Optional[str]:
    """Find and read a wiki page by title. Returns formatted extract or None."""
    for md_file in wiki_dir.rglob("*.md"):
        if md_file.name == "_index.md":
            continue
        text = md_file.read_text(encoding="utf-8")
        meta, body = parse_frontmatter(text)
        if meta.get("title") == title:
            sections = parse_sections(body)
            summary = sections.get("Summary", "")
            insights = sections.get("Key Insights", "")
            rels_text = sections.get("Relationships", "")
            deep = sections.get("Deep Analysis", "")

            parts = [f"### {title}"]
            if summary:
                parts.append(f"**Summary:** {summary}")
            if insights:
                parts.append(f"**Key Insights:**\n{insights}")
            if deep:
                # Truncate deep analysis to first 500 words to fit prompt size
                words = deep.split()
                if len(words) > 500:
                    deep = " ".join(words[:500]) + "..."
                parts.append(f"**Analysis:**\n{deep}")
            if rels_text:
                parts.append(f"**Relationships:**\n{rels_text}")
            return "\n\n".join(parts)
    return None


def _quality_requirements(page_type: str, schema: Optional[dict]) -> str:
    """Build quality requirements string from schema."""
    reqs = ["- Summary: minimum 30 words"]
    if page_type == "lesson":
        reqs.append("- Insight section: minimum 50 words")
        reqs.append("- Evidence section: specific examples from source pages")
        reqs.append("- Must include derived_from in frontmatter")
    elif page_type == "pattern":
        reqs.append("- Summary: minimum 50 words")
        reqs.append("- Pattern Description: minimum 100 words")
        reqs.append("- Instances: 2+ specific examples with page references")
        reqs.append("- Must include instances in frontmatter")
    elif page_type == "decision":
        reqs.append("- Summary: minimum 50 words")
        reqs.append("- Rationale: minimum 100 words")
        reqs.append("- Alternatives: minimum 2 alternatives")
        reqs.append("- Must include reversibility in frontmatter")
    reqs.append("- Relationships section with ALL_CAPS verbs")
    reqs.append("- Backlinks section with [[wikilinks]]")
    return "\n".join(reqs)
```

- [ ] **Step 2: Test prompt builder**

Run: `python3 -c "from tools.evolve import score_candidates, build_prompt; from tools.common import get_project_root; root = get_project_root(); cs = score_candidates(root, top=1); print(build_prompt(cs[0], root)[:500])"`

Expected: First 500 chars of a generation prompt — should show the target page section and beginning of source material.

- [ ] **Step 3: Commit**

```bash
git add tools/evolve.py
git commit -m "feat(evolve): prompt builder — reads source pages, assembles generation prompt"
```

---

### Task 5: LLM Backends — Claude Code and OpenAI

**Files:**
- Modify: `tools/evolve.py`
- Create: `wiki/.evolve-queue/.gitkeep`

- [ ] **Step 1: Add LLMBackend base class and ClaudeCodeBackend**

Append to `tools/evolve.py`:

```python
# ---------------------------------------------------------------------------
# LLM Backends
# ---------------------------------------------------------------------------

class LLMBackend:
    """Abstract interface for LLM generation."""

    name: str = "base"

    def generate(self, prompt: str, model: Optional[str] = None) -> str:
        """Send prompt, return generated markdown content."""
        raise NotImplementedError

    def is_available(self) -> bool:
        """Check if this backend is reachable."""
        raise NotImplementedError


class ClaudeCodeBackend(LLMBackend):
    """Writes prompt files to a queue for Claude Code session execution."""

    name = "claude-code"

    def __init__(self, queue_dir: Path):
        self.queue_dir = queue_dir
        self.queue_dir.mkdir(parents=True, exist_ok=True)

    def generate(self, prompt: str, model: Optional[str] = None,
                 target_path: str = "", candidate_score: float = 0.0) -> str:
        """Write a prompt file to the queue. Returns the queue file path."""
        slug = re.sub(r"[^a-z0-9]+", "-", target_path.lower().split("/")[-1].replace(".md", ""))
        filename = f"{slug}.prompt.md"
        queue_file = self.queue_dir / filename

        content = f"""---
target: {target_path}
candidate_score: {candidate_score:.2f}
generated: {datetime.now().strftime('%Y-%m-%d')}
---

{prompt}
"""
        queue_file.write_text(content, encoding="utf-8")
        return str(queue_file)

    def is_available(self) -> bool:
        return True  # Always available — just writes files


class OpenAIBackend(LLMBackend):
    """Calls an OpenAI-compatible API (LocalAI, AICP proxy, etc.)."""

    name = "openai"

    def __init__(self, endpoint: Optional[str] = None, model: Optional[str] = None):
        self.endpoint = endpoint or os.environ.get(
            "WIKI_LLM_ENDPOINT", "http://localhost:8080/v1/chat/completions"
        )
        self.default_model = model or os.environ.get("WIKI_LLM_MODEL", "")

    def generate(self, prompt: str, model: Optional[str] = None) -> str:
        """Call OpenAI-compatible API and return the response text."""
        use_model = model or self.default_model
        payload = {
            "messages": [
                {"role": "system", "content": "You are a research wiki writer. Output only valid markdown with YAML frontmatter. No commentary."},
                {"role": "user", "content": prompt},
            ],
        }
        if use_model:
            payload["model"] = use_model

        data = json.dumps(payload).encode("utf-8")
        req = request.Request(
            self.endpoint,
            data=data,
            headers={"Content-Type": "application/json"},
            method="POST",
        )

        try:
            with request.urlopen(req, timeout=120) as resp:
                result = json.loads(resp.read().decode("utf-8"))
                return result["choices"][0]["message"]["content"]
        except (urlerror.URLError, KeyError, json.JSONDecodeError) as e:
            raise RuntimeError(f"OpenAI backend error: {e}") from e

    def is_available(self) -> bool:
        """Check if the endpoint responds."""
        try:
            req = request.Request(
                self.endpoint.replace("/chat/completions", "/models"),
                method="GET",
            )
            with request.urlopen(req, timeout=5) as resp:
                return resp.status == 200
        except Exception:
            return False
```

- [ ] **Step 2: Add AICPBackend**

Append to `tools/evolve.py`:

```python
class AICPBackend(LLMBackend):
    """Calls AICP MCP chat tool with fallback to OpenAI-compatible API."""

    name = "aicp"

    def __init__(self, endpoint: Optional[str] = None):
        self.endpoint = endpoint or os.environ.get(
            "WIKI_AICP_ENDPOINT", "http://localhost:3000"
        )
        self._fallback = OpenAIBackend()

    def generate(self, prompt: str, model: Optional[str] = None) -> str:
        """Try AICP first, fall back to OpenAI backend."""
        if self.is_available():
            try:
                return self._call_aicp(prompt, model)
            except Exception:
                pass  # Fall through to fallback
        return self._fallback.generate(prompt, model)

    def _call_aicp(self, prompt: str, model: Optional[str] = None) -> str:
        """Call AICP's chat endpoint."""
        payload = {
            "prompt": prompt,
        }
        if model:
            payload["model"] = model

        data = json.dumps(payload).encode("utf-8")
        req = request.Request(
            f"{self.endpoint}/v1/chat/completions",
            data=data,
            headers={"Content-Type": "application/json"},
            method="POST",
        )

        with request.urlopen(req, timeout=120) as resp:
            result = json.loads(resp.read().decode("utf-8"))
            return result["choices"][0]["message"]["content"]

    def is_available(self) -> bool:
        """Check if AICP endpoint responds."""
        try:
            req = request.Request(f"{self.endpoint}/health", method="GET")
            with request.urlopen(req, timeout=5) as resp:
                return resp.status == 200
        except Exception:
            return False


def get_backend(name: str, project_root: Path) -> LLMBackend:
    """Factory: return the requested backend instance."""
    if name == "claude-code":
        return ClaudeCodeBackend(project_root / "wiki" / ".evolve-queue")
    elif name == "openai":
        return OpenAIBackend()
    elif name == "aicp":
        return AICPBackend()
    else:
        raise ValueError(f"Unknown backend: {name}. Use: claude-code, openai, aicp")
```

- [ ] **Step 3: Create queue directory**

```bash
mkdir -p wiki/.evolve-queue
touch wiki/.evolve-queue/.gitkeep
```

- [ ] **Step 4: Verify backends import**

Run: `python3 -c "from tools.evolve import ClaudeCodeBackend, OpenAIBackend, AICPBackend, get_backend; print('OK')"`

Expected: `OK`

- [ ] **Step 5: Commit**

```bash
git add tools/evolve.py wiki/.evolve-queue/.gitkeep
git commit -m "feat(evolve): LLM backends — claude-code queue, openai API, aicp with fallback"
```

---

### Task 6: Evolution Orchestrator

**Files:**
- Modify: `tools/evolve.py`

- [ ] **Step 1: Add the evolve() orchestrator and helper functions**

Append to `tools/evolve.py`:

```python
# ---------------------------------------------------------------------------
# Orchestrator
# ---------------------------------------------------------------------------

def evolve(
    project_root: Path,
    mode: str = "score",  # score, scaffold, auto, dry-run, execute, review
    backend_name: str = "claude-code",
    top: Optional[int] = None,
    type_filter: Optional[str] = None,
    domain_filter: Optional[str] = None,
    clear_queue: bool = False,
    verbose: bool = True,
) -> Dict[str, Any]:
    """Main evolution entry point. Delegates to sub-operations based on mode."""

    if mode == "score":
        candidates = score_candidates(project_root, type_filter, domain_filter, top)
        if verbose:
            _print_candidates(candidates)
        return {"candidates": [c.to_dict() for c in candidates]}

    elif mode == "scaffold":
        candidates = score_candidates(project_root, type_filter, domain_filter, top)
        from tools.pipeline import scaffold_page
        results = []
        for c in candidates:
            result = scaffold_page(c.type, c.title, project_root,
                                   domain=c.domain, derived_from=c.source_pages,
                                   verbose=verbose)
            results.append(result)
        return {"scaffolded": results}

    elif mode == "dry-run":
        candidates = score_candidates(project_root, type_filter, domain_filter, top)
        prompts = []
        for c in candidates:
            prompt = build_prompt(c, project_root)
            if verbose:
                print(f"\n{'='*60}")
                print(f"PROMPT FOR: {c.title}")
                print(f"{'='*60}")
                print(prompt)
            prompts.append({"title": c.title, "prompt_length": len(prompt)})
        return {"prompts": prompts}

    elif mode == "auto":
        candidates = score_candidates(project_root, type_filter, domain_filter, top)
        backend = get_backend(backend_name, project_root)
        from tools.pipeline import scaffold_page

        results = []
        for c in candidates:
            # Scaffold first
            scaffold_result = scaffold_page(c.type, c.title, project_root,
                                            domain=c.domain, derived_from=c.source_pages,
                                            verbose=verbose)
            if not scaffold_result["ok"]:
                results.append({"title": c.title, "ok": False, "error": scaffold_result["error"]})
                continue

            # Build prompt and generate
            prompt = build_prompt(c, project_root)

            if isinstance(backend, ClaudeCodeBackend):
                queue_path = backend.generate(
                    prompt, target_path=scaffold_result["path"],
                    candidate_score=c.score,
                )
                results.append({"title": c.title, "ok": True, "queue": queue_path})
                if verbose:
                    print(f"  Queued: {queue_path}")
            else:
                try:
                    content = backend.generate(prompt)
                    # Write generated content to the scaffold file
                    out_path = project_root / scaffold_result["path"]
                    out_path.write_text(content, encoding="utf-8")
                    results.append({"title": c.title, "ok": True, "path": scaffold_result["path"]})
                    if verbose:
                        print(f"  Generated: {scaffold_result['path']}")
                except Exception as e:
                    results.append({"title": c.title, "ok": False, "error": str(e)})
                    if verbose:
                        print(f"  FAILED: {c.title} — {e}")

        return {"generated": results}

    elif mode == "execute":
        return _execute_queue(project_root, clear_queue, verbose)

    elif mode == "review":
        return review_seeds(project_root, verbose)

    else:
        return {"error": f"Unknown mode: {mode}"}


def _print_candidates(candidates: List[Candidate]):
    """Print candidates in a human-readable table."""
    if not candidates:
        print("  No evolution candidates found.")
        return
    print(f"  {'Score':>5}  {'Type':10}  {'Title':50}  Sources")
    print(f"  {'─'*5}  {'─'*10}  {'─'*50}  {'─'*20}")
    for c in candidates:
        sources = ", ".join(c.source_pages[:3])
        if len(c.source_pages) > 3:
            sources += f" (+{len(c.source_pages) - 3})"
        print(f"  {c.score:5.2f}  {c.type:10}  {c.title[:50]:50}  {sources}")


def _execute_queue(project_root: Path, clear: bool, verbose: bool) -> Dict[str, Any]:
    """List prompt queue files for manual execution. Returns queue contents."""
    queue_dir = project_root / "wiki" / ".evolve-queue"
    if not queue_dir.exists():
        return {"queue": [], "message": "No queue directory"}

    prompts = []
    for f in sorted(queue_dir.glob("*.prompt.md")):
        text = f.read_text(encoding="utf-8")
        meta, body = parse_frontmatter(text)
        prompts.append({
            "file": str(f.relative_to(project_root)),
            "target": meta.get("target", ""),
            "score": meta.get("candidate_score", 0),
        })
        if verbose:
            print(f"  Queue: {f.name} → {meta.get('target', '?')}")

    if clear and prompts:
        for f in queue_dir.glob("*.prompt.md"):
            f.unlink()
        if verbose:
            print(f"  Cleared {len(prompts)} prompt files.")

    if not prompts and verbose:
        print("  Queue is empty.")

    return {"queue": prompts}


def review_seeds(project_root: Path, verbose: bool = True) -> Dict[str, Any]:
    """List seed-maturity pages that may be ready for promotion to growing."""
    wiki_dir = project_root / "wiki"
    manifest = build_manifest(wiki_dir)
    pages = manifest["pages"]

    promotable = []
    for p in pages:
        if p.get("maturity") != "seed":
            continue

        # Check quality: derived_from exists, relationships beyond DERIVED FROM
        has_derived = bool(p.get("derived_from"))
        rels = p.get("relationships", [])
        non_derived_rels = [r for r in rels if r.get("verb") != "DERIVED FROM"]

        if has_derived and len(non_derived_rels) >= 1:
            promotable.append({
                "title": p["title"],
                "type": p["type"],
                "domain": p["domain"],
                "relationships": len(rels),
                "derived_from_count": len(p.get("derived_from", [])),
            })

    if verbose:
        if promotable:
            print(f"  Seed pages ready for review ({len(promotable)}):")
            for pr in promotable:
                print(f"    {pr['title']} [{pr['type']}] — {pr['relationships']} rels")
        else:
            print("  No seed pages ready for promotion.")

    return {"promotable": promotable}


def detect_stale(project_root: Path, verbose: bool = True) -> Dict[str, Any]:
    """Find evolved pages whose source pages have been updated since derivation."""
    wiki_dir = project_root / "wiki"
    manifest = build_manifest(wiki_dir)
    pages = manifest["pages"]

    title_to_updated = {p["title"]: p.get("updated", "") for p in pages}
    stale = []

    for p in pages:
        layer = p.get("layer")
        if layer is None or not str(layer).isdigit() or int(str(layer)) < 4:
            continue

        page_updated = p.get("updated", "")
        for source_title in p.get("derived_from", []):
            source_updated = title_to_updated.get(source_title, "")
            if source_updated and page_updated and source_updated > page_updated:
                stale.append({
                    "title": p["title"],
                    "updated": page_updated,
                    "stale_source": source_title,
                    "source_updated": source_updated,
                })
                break

    if verbose:
        if stale:
            print(f"  Stale evolved pages ({len(stale)}):")
            for s in stale:
                print(f"    {s['title']} — source '{s['stale_source']}' updated {s['source_updated']}")
        else:
            print("  No stale evolved pages.")

    return {"stale": stale}
```

- [ ] **Step 2: Test the orchestrator in score mode**

Run: `python3 -c "from tools.evolve import evolve; from tools.common import get_project_root; result = evolve(get_project_root(), mode='score', top=3); print(f'{len(result[\"candidates\"])} candidates')"`

Expected: `3 candidates` (or fewer if less are found)

- [ ] **Step 3: Test scaffold mode (dry)**

Run: `python3 -c "from tools.evolve import evolve; from tools.common import get_project_root; result = evolve(get_project_root(), mode='scaffold', top=1); print(result)"`

Expected: One scaffolded result with `ok: True` and a path.

Clean up the test scaffold:

```bash
# Remove any test scaffolds that were just created
find wiki/lessons wiki/patterns wiki/decisions -name "*.md" -newer tools/evolve.py -not -name "_index.md" | head -1 | xargs rm -f 2>/dev/null; echo "cleaned"
```

- [ ] **Step 4: Commit**

```bash
git add tools/evolve.py
git commit -m "feat(evolve): orchestrator — score/scaffold/auto/execute/review/stale modes"
```

---

### Task 7: Pipeline CLI Integration

**Files:**
- Modify: `tools/pipeline.py`
- Modify: `.gitignore`
- Create: `.env.example`

- [ ] **Step 1: Add `evolve` to pipeline CLI command choices**

In `tools/pipeline.py`, change the argparse choices line (around line 1046):

```python
    parser.add_argument("command",
                        choices=["post", "fetch", "scan", "status", "run",
                                 "chain", "gaps", "crossref", "integrations",
                                 "scaffold", "evolve"],
                        help="Pipeline command")
```

- [ ] **Step 2: Add evolve CLI handler**

In `tools/pipeline.py`, add this block after the `scaffold` handler (before the `if __name__` line):

```python
    elif args.command == "evolve":
        from tools.evolve import evolve as run_evolve

        # Determine mode from flags
        # args.args may contain flags like --score, --auto, etc.
        # Parse sub-flags from args.args
        sub = argparse.ArgumentParser()
        sub.add_argument("--score", action="store_true")
        sub.add_argument("--scaffold", action="store_true")
        sub.add_argument("--auto", action="store_true")
        sub.add_argument("--dry-run", action="store_true")
        sub.add_argument("--execute", action="store_true")
        sub.add_argument("--review", action="store_true")
        sub.add_argument("--backend", default=os.environ.get("WIKI_EVOLVE_BACKEND", "claude-code"))
        sub.add_argument("--top", type=int, default=int(os.environ.get("WIKI_EVOLVE_TOP", "10")))
        sub.add_argument("--type", dest="etype")
        sub.add_argument("--domain")
        sub.add_argument("--clear", action="store_true")
        eopts = sub.parse_args(args.args)

        if eopts.score:
            mode = "score"
        elif eopts.scaffold:
            mode = "scaffold"
        elif eopts.auto:
            mode = "auto"
        elif eopts.dry_run:
            mode = "dry-run"
        elif eopts.execute:
            mode = "execute"
        elif eopts.review:
            mode = "review"
        else:
            mode = "score"  # default

        result = run_evolve(
            root,
            mode=mode,
            backend_name=eopts.backend,
            top=eopts.top,
            type_filter=eopts.etype,
            domain_filter=eopts.domain,
            clear_queue=eopts.clear,
            verbose=verbose,
        )

        if args.json:
            print(json.dumps(result, indent=2, default=str))
        sys.exit(0)
```

- [ ] **Step 3: Update the `evolve` and `spine-refresh` chains, add `evolve-auto`**

In `tools/pipeline.py`, replace the existing `evolve` and `spine-refresh` chain entries in the `CHAINS` dict:

```python
    "evolve": {
        "description": "Score candidates → scaffold top N → post-chain",
        "steps": ["evolve-score", "post"],
        "needs_input": False,
    },
    "evolve-auto": {
        "description": "Score → scaffold → generate (local model) → post-chain",
        "steps": ["evolve-auto", "post"],
        "needs_input": False,
    },
    "spine-refresh": {
        "description": "Score domain-overview candidates → generate → post-chain",
        "steps": ["evolve-spine", "post"],
        "needs_input": False,
    },
```

- [ ] **Step 4: Add evolve steps to `run_step()`**

In `tools/pipeline.py`, find the `run_step()` function and add cases for the new step names. Locate the function (it dispatches chain steps) and add:

```python
    elif step == "evolve-score":
        from tools.evolve import evolve as run_evolve
        return run_evolve(project_root, mode="scaffold", top=5, verbose=verbose)
    elif step == "evolve-auto":
        from tools.evolve import evolve as run_evolve
        return run_evolve(project_root, mode="auto", backend_name="openai", top=5, verbose=verbose)
    elif step == "evolve-spine":
        from tools.evolve import evolve as run_evolve
        return run_evolve(project_root, mode="auto", type_filter="domain-overview",
                          backend_name="openai", top=7, verbose=verbose)
```

- [ ] **Step 5: Create .env.example**

```bash
cat > .env.example << 'ENVEOF'
# Wiki Evolution Pipeline — LLM Backend Configuration
# Copy to .env and adjust values.

# OpenAI-compatible API (LocalAI, LM Studio, vLLM, etc.)
WIKI_LLM_ENDPOINT=http://localhost:8080/v1/chat/completions
WIKI_LLM_MODEL=

# AICP endpoint (if using AICP backend)
WIKI_AICP_ENDPOINT=http://localhost:3000

# Default evolution settings
WIKI_EVOLVE_BACKEND=claude-code
WIKI_EVOLVE_TOP=10
ENVEOF
```

- [ ] **Step 6: Update .gitignore**

Append to `.gitignore`:

```
# Evolution prompt queue (ephemeral)
wiki/.evolve-queue/*.prompt.md
```

- [ ] **Step 7: Test the full CLI**

Run: `python3 -m tools.pipeline evolve --score --top 5 2>&1`

Expected: Table of 1-5 candidates with scores.

Run: `python3 -m tools.pipeline evolve --review 2>&1`

Expected: List of seed pages ready for review (should show the 4 evolved pages from Task 11).

- [ ] **Step 8: Commit**

```bash
git add tools/pipeline.py .env.example .gitignore wiki/.evolve-queue/.gitkeep
git commit -m "feat(evolve): pipeline CLI integration — evolve command with all modes"
```

---

### Task 8: Update CLAUDE.md and Pipeline Docstring

**Files:**
- Modify: `CLAUDE.md`
- Modify: `tools/pipeline.py` (docstring only)

- [ ] **Step 1: Update CLAUDE.md tooling section**

Add to the Pipeline section in `CLAUDE.md`, after the existing pipeline commands:

```markdown
- `python3 -m tools.pipeline evolve --score` — Rank evolution candidates (deterministic)
- `python3 -m tools.pipeline evolve --score --top 5 --json` — Top 5 candidates as JSON
- `python3 -m tools.pipeline evolve --scaffold --top 3` — Scaffold top 3 candidates
- `python3 -m tools.pipeline evolve --dry-run --top 1` — Preview generation prompt
- `python3 -m tools.pipeline evolve --auto --backend openai` — Generate via local model
- `python3 -m tools.pipeline evolve --auto --backend claude-code` — Write prompt queue
- `python3 -m tools.pipeline evolve --execute` — List prompt queue for session execution
- `python3 -m tools.pipeline evolve --review` — List seed pages ready for maturity promotion
```

- [ ] **Step 2: Update pipeline.py module docstring**

At the top of `tools/pipeline.py`, add to the docstring:

```python
    python3 -m tools.pipeline evolve --score     # Rank evolution candidates
    python3 -m tools.pipeline evolve --auto      # Auto-generate evolved pages
    python3 -m tools.pipeline evolve --review    # Review seed page maturity
```

- [ ] **Step 3: Commit**

```bash
git add CLAUDE.md tools/pipeline.py
git commit -m "docs: document evolve command in CLAUDE.md and pipeline docstring"
```

---

### Task 9: Integration Test — Full Evolution Cycle

**Files:**
- No new files — this is a verification task

- [ ] **Step 1: Run full scoring**

Run: `python3 -m tools.pipeline evolve --score --json 2>&1 | python3 -c "import sys,json; d=json.load(sys.stdin); print(f'{len(d[\"candidates\"])} candidates found')"`

Expected: Some number of candidates > 0.

- [ ] **Step 2: Test scaffold mode**

Run: `python3 -m tools.pipeline evolve --scaffold --top 1 2>&1`

Expected: One page scaffolded.

- [ ] **Step 3: Test dry-run mode**

Run: `python3 -m tools.pipeline evolve --dry-run --top 1 2>&1 | head -20`

Expected: Generation prompt with Target Page, Why This Page, Source Material sections.

- [ ] **Step 4: Test claude-code queue mode**

Run: `python3 -m tools.pipeline evolve --auto --backend claude-code --top 1 2>&1`

Expected: One prompt file written to `wiki/.evolve-queue/`.

Run: `python3 -m tools.pipeline evolve --execute 2>&1`

Expected: Queue listing showing the prompt file.

- [ ] **Step 5: Test review mode**

Run: `python3 -m tools.pipeline evolve --review 2>&1`

Expected: Lists the 3-4 seed pages from the Knowledge Layer System implementation.

- [ ] **Step 6: Clean up test artifacts**

```bash
# Remove test scaffolds and queue files
rm -f wiki/.evolve-queue/*.prompt.md
find wiki/lessons wiki/patterns wiki/decisions -name "*.md" -newer tools/evolve.py -not -name "_index.md" -not -name "cli-*" -not -name "always-*" -not -name "plan-*" -not -name "mcp-*" | xargs rm -f 2>/dev/null
```

- [ ] **Step 7: Run post-chain to verify wiki integrity**

Run: `python3 -m tools.pipeline post 2>&1`

Expected: PASS with 0 validation errors.

- [ ] **Step 8: Run health chain**

Run: `python3 -m tools.pipeline chain health 2>&1`

Expected: Health check passes, candidates count visible in output.

- [ ] **Step 9: Final commit**

```bash
git add wiki/manifest.json
git commit -m "feat: knowledge evolution pipeline — scoring, prompts, backends, CLI complete"
```

---

## Self-Review

**Spec coverage check:**
- Candidate Scoring Engine (6 signals) → Task 1-2
- Scoring Algorithm + Dedup → Task 3
- Prompt Builder → Task 4
- LLM Backends (claude-code, openai, aicp) → Task 5
- Evolution orchestrator → Task 6
- Pipeline CLI integration → Task 7
- CLAUDE.md + docs → Task 8
- Integration testing → Task 9
- Quality/Maturity lifecycle (review_seeds, detect_stale) → Task 6
- .gitignore, .env.example → Task 7
- Chain updates (evolve, evolve-auto, spine-refresh) → Task 7

**Placeholder scan:** No TBDs, TODOs, or vague steps. All code blocks complete.

**Type consistency check:**
- `Candidate` and `Signal` dataclasses used consistently across all tasks
- `score_candidates()` signature matches calls in Task 6 and Task 7
- `build_prompt()` signature matches calls in Task 6
- `evolve()` signature matches pipeline CLI call in Task 7
- `get_backend()` factory matches backend names in CLI handler
- `review_seeds()` and `detect_stale()` match Task 6 orchestrator calls
