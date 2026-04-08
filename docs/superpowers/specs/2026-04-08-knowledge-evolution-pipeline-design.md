# Knowledge Evolution Pipeline — Design Spec

## Problem

The Knowledge Layer System (Subsystem 1) created the architecture: templates, schema, scaffold command, validation, 6 new page types. But evolved pages are still created manually — a human reads source pages, identifies an insight, scaffolds a page, and writes the content. This doesn't scale. With 48 Layer 1-3 pages and 205 open questions, the wiki has far more evolution candidates than any manual process can address.

The user's directive: "All these things ingest are not meant to be dump but to be smart and give birth to other layers, to evolutions of ideas and aggregations and filterings and orderings and annotatings and enriching."

## Solution

A three-layer evolution engine (`tools/evolve.py`) that:
1. **Scores** existing pages to identify evolution candidates (deterministic, $0)
2. **Builds prompts** from source pages + templates (deterministic, $0)
3. **Generates** evolved page content via pluggable LLM backends (Claude Code session, OpenAI-compatible API for LocalAI, or AICP MCP)

Default mode is deterministic-only (score + scaffold). `--auto` flag triggers LLM generation. Quality gates prevent bad pages from polluting the wiki.

## Architecture

```
tools/evolve.py
├── CandidateScorer         # Reads manifest/gaps/crossref, outputs ranked candidates
├── PromptBuilder           # Reads source pages + template, builds generation prompt
├── LLMBackend (abstract)   # generate(prompt, model) → str
│   ├── ClaudeCodeBackend   # Writes .prompt files to queue for session execution
│   ├── OpenAIBackend       # Calls OpenAI-compatible API (LocalAI, AICP proxy)
│   └── AICPBackend         # Calls AICP MCP chat tool, falls back to OpenAI
└── evolve()                # Orchestrator: score → scaffold → generate → validate
```

Pipeline.py calls `evolve.py` functions. The evolve module is self-contained and testable.

## Candidate Scoring Engine

### Signals

All signals are deterministic, derived from existing manifest/gaps/crossref data.

| Signal | What it detects | Target type | Weight |
|--------|----------------|-------------|--------|
| Tag co-occurrence | 3+ pages share 2+ tags | pattern | 0.25 |
| Cross-source convergence | Multiple source pages reference same concept | lesson | 0.25 |
| Relationship hub | Page with 5+ inbound relationships | lesson | 0.15 |
| Domain layer gap | Domain has Layer 1-2 pages but no Layer 4-6 | lesson, pattern | 0.15 |
| Open question density | Pages with 3+ open questions | decision | 0.10 |
| Orphaned references | Referenced but non-existent pages | lesson | 0.10 |

### Scoring Algorithm

```python
def score_candidates(manifest: dict, gaps: dict, crossref: dict) -> List[Candidate]:
    """Score all pages/combinations for evolution readiness.
    
    Returns candidates sorted by score (0.0-1.0), each with:
    - type: lesson | pattern | decision
    - title: suggested evolved page title
    - score: weighted composite score
    - signals: list of which signals fired and their individual scores
    - source_pages: list of page titles to synthesize from
    - domain: target domain for the evolved page
    """
```

### Deduplication

Before scoring, check existing Layer 4-6 pages. If a candidate's `source_pages` are already covered by an existing evolved page's `derived_from`, skip it. Prevents re-generating pages that already exist.

### Output Format

```json
[
  {
    "type": "lesson",
    "title": "Guardrails Must Be Framework-Level Not Model-Level",
    "score": 0.82,
    "signals": [
      {"name": "cross_source_convergence", "score": 0.9, "detail": "3 sources converge"},
      {"name": "relationship_hub", "score": 0.7, "detail": "AICP has 8 inbound rels"}
    ],
    "source_pages": ["AICP", "Harness Engineering", "Claude Code"],
    "domain": "ai-agents"
  }
]
```

## Prompt Builder

### What It Does

Given a scored candidate:
1. Reads each page listed in `source_pages` (full content: frontmatter + all sections)
2. Reads the appropriate template from `config/templates/{type}.md`
3. Extracts relevant content per source: Summary, Key Insights, relevant Relationships
4. Assembles a structured generation prompt

### Prompt Structure

```
You are writing a {type} page for a research wiki.

## Target Page
- Title: {candidate.title}
- Type: {candidate.type}
- Domain: {candidate.domain}
- Template sections required: {list from template}

## Why This Page
This candidate was identified because: {candidate.signals explained}

## Source Material

### Source 1: {page_title}
{extracted summary, key insights, relevant relationships}

### Source 2: {page_title}
{extracted summary, key insights, relevant relationships}

...

## Quality Requirements
- Summary: minimum 30 words (50 for pattern/decision)
- {type-specific section}: minimum {N} words
- Must include Relationships section with ALL_CAPS verbs
- derived_from must list: {source_pages}
- Frontmatter must match schema exactly

## Template
{full template content with placeholders}

Write the complete page. Output only the markdown content (frontmatter + body). No explanation.
```

### Prompt Quality

The prompt is deterministic and inspectable. `pipeline evolve --dry-run --top 3` outputs the prompts without sending them to any backend — useful for debugging and evaluating whether the local model can handle the task.

## LLM Backends

### Interface

```python
class LLMBackend:
    """Abstract interface for LLM generation."""
    
    name: str  # "claude-code", "openai", "aicp"
    
    def generate(self, prompt: str, model: str = None) -> str:
        """Send prompt, return generated markdown content."""
        raise NotImplementedError
    
    def is_available(self) -> bool:
        """Check if this backend is reachable."""
        raise NotImplementedError
```

### Backend 1: Claude Code (default)

- Does NOT call an API
- Writes a `.prompt` file per candidate to `wiki/.evolve-queue/`
- Each file contains: target scaffold path, full generation prompt, candidate metadata
- During a Claude Code session, `pipeline evolve --execute` reads the queue and Claude Code fills each page
- `pipeline evolve --execute --clear` processes and removes prompt files after completion

**File format** (`wiki/.evolve-queue/{slug}.prompt.md`):
```yaml
---
target: wiki/lessons/guardrails-framework-level.md
type: lesson
candidate_score: 0.82
generated: 2026-04-08
---

{full generation prompt}
```

### Backend 2: OpenAI-compatible API

- Calls `WIKI_LLM_ENDPOINT` (default: `http://localhost:8080/v1/chat/completions`)
- `WIKI_LLM_MODEL` env var selects the model (default: configurable)
- System message: "You are a research wiki writer. Output only valid markdown with YAML frontmatter."
- User message: the assembled prompt
- Parses response, writes directly to the scaffold file
- Timeout: 120s (large models on consumer hardware are slow)
- On failure: logs error, leaves scaffold file with template content, continues to next candidate

### Backend 3: AICP MCP

- Calls AICP's MCP `chat` tool via subprocess: `python -m aicp.mcp chat --prompt "..."`
- Benefits from AICP's backend routing (could auto-escalate complex pages to Claude if configured)
- Falls back to Backend 2 (direct OpenAI API) if AICP is unavailable or errors
- `WIKI_AICP_ENDPOINT` env var (default: `http://localhost:3000`)

### Backend Selection

```
--backend claude-code   (default) Write prompt queue for session execution
--backend openai        Direct LocalAI / OpenAI-compatible API call
--backend aicp          AICP MCP chat tool with fallback to openai
```

### Configuration

Environment variables (can be set in `.env`):
```
WIKI_LLM_ENDPOINT=http://localhost:8080/v1/chat/completions
WIKI_LLM_MODEL=qwen3-30b-moe
WIKI_AICP_ENDPOINT=http://localhost:3000
WIKI_EVOLVE_BACKEND=claude-code
WIKI_EVOLVE_TOP=5
```

## Pipeline Integration

### CLI Commands

`evolve` becomes a first-class pipeline command (like `post`, `fetch`, `gaps`), replacing the current skeletal chain entry. It is NOT a chain — it is a direct command with its own flags.

```bash
# Candidate scoring (deterministic)
pipeline evolve --score                    # Show all candidates ranked
pipeline evolve --score --top 10           # Top 10 candidates
pipeline evolve --score --type lesson      # Only lesson candidates
pipeline evolve --score --domain ai-agents # Only for a specific domain
pipeline evolve --score --json             # JSON output

# Scaffold only (deterministic)
pipeline evolve --scaffold --top 5         # Scaffold top 5 candidates

# Dry run (show prompts without sending)
pipeline evolve --dry-run --top 3          # Output prompts for inspection

# Auto-generate (LLM-powered)
pipeline evolve --auto --top 5                          # Use default backend
pipeline evolve --auto --backend openai --top 5         # Use local model
pipeline evolve --auto --backend aicp --top 3           # Use AICP routing
pipeline evolve --auto --backend claude-code --top 5    # Write prompt queue

# Execute prompt queue (Claude Code session)
pipeline evolve --execute                  # Process queue, fill pages
pipeline evolve --execute --clear          # Process and remove prompts

# Review seed pages for promotion
pipeline evolve --review                   # List seed pages meeting growing criteria
```

### Chain Updates

**`evolve` chain (updated):**
```
gaps → score candidates → scaffold top N → post-chain
```
Default: deterministic only. With `--auto`: also generates content.

**`evolve-auto` chain (new):**
```
gaps → score → scaffold → generate (openai backend) → post-chain
```
Convenience chain for full local-model loop.

**`spine-refresh` chain (updated):**
```
score domain-overview candidates → scaffold/update → generate → post-chain
```
Specifically rebuilds `wiki/spine/domain-overviews/` pages. Most mechanical evolved pages — good early target for local model.

**`health` chain (updated):**
```
post → gaps → crossref → evolve --score (append candidate count to health report)
```

### File Structure

```
tools/
├── evolve.py              # NEW: scorer, prompt builder, backend abstraction
├── pipeline.py            # MODIFIED: evolve chain calls evolve.py
├── ...existing...
wiki/
├── .evolve-queue/         # NEW: prompt files for claude-code backend
│   └── {slug}.prompt.md
```

## Quality & Maturity Lifecycle

### Initial Maturity

All auto-generated pages start at `maturity: seed` regardless of backend quality. Even Claude Code output starts as seed. Maturity upgrades are a separate human judgment.

### Maturity Promotion Criteria

| Level | How you get there |
|-------|-------------------|
| `seed` | Auto-generated or scaffolded. Exists but unvalidated. |
| `growing` | Human-reviewed and accepted. Has real `derived_from` links. Passes all quality gates. |
| `mature` | Cross-referenced by other pages. Referenced in 2+ inbound relationships. Content stable 30+ days. |
| `canonical` | Marked manually. Authoritative reference for its domain. |

### No Auto-Promotion

The pipeline can *suggest* promotions but never changes maturity automatically. `pipeline evolve --review` lists seed pages that meet `growing` criteria:
- All quality gates pass (min word counts, required sections)
- `derived_from` pages all exist
- Has at least 1 relationship beyond `DERIVED FROM`

### Staleness Detection

If a source page listed in an evolved page's `derived_from` gets updated (detected via `updated` field comparison), the evolved page is flagged as potentially stale. The `health` chain reports stale evolved pages. No auto-demotion — just flagged for human review.

## Tool Changes

### tools/evolve.py (NEW)

The core module. Contains:
- `CandidateScorer` class with `score()` method
- `PromptBuilder` class with `build()` method
- `LLMBackend` base class + 3 implementations
- `evolve()` orchestrator function
- `review_seeds()` for maturity promotion suggestions
- `detect_stale()` for staleness checking

### tools/pipeline.py (MODIFIED)

- Import and call `evolve.py` functions from `evolve` chain
- Add `evolve` CLI subcommand with flags: `--score`, `--scaffold`, `--auto`, `--dry-run`, `--execute`, `--review`, `--backend`, `--top`, `--type`, `--domain`
- Update `evolve`, `spine-refresh`, `health` chains
- Add `evolve-auto` chain

### config/schema.yaml (NO CHANGES)

Already has all needed types and fields from Subsystem 1.

### .gitignore (MODIFIED)

Add `wiki/.evolve-queue/` — prompt files are ephemeral, not tracked.

### .env.example (NEW)

Document all `WIKI_*` env vars for backend configuration.

## Success Criteria

- `pipeline evolve --score` outputs ranked candidates from existing 52 pages
- `pipeline evolve --score --top 5 --json` returns valid JSON with scores, signals, source_pages
- `pipeline evolve --scaffold --top 3` creates 3 new scaffold files that pass validation
- `pipeline evolve --dry-run --top 1` outputs a complete, inspectable generation prompt
- `pipeline evolve --auto --backend openai --top 1` generates a page via local model (if available)
- `pipeline evolve --auto --backend claude-code --top 3` writes 3 prompt files to queue
- `pipeline evolve --execute` processes prompt queue (Claude Code fills pages)
- `pipeline evolve --review` lists seed pages eligible for maturity promotion
- `pipeline chain health` includes candidate count in report
- Generated pages pass validation with 0 errors
- Post-chain runs cleanly after any evolution operation

## Relationship to Subsystem 3

Subsystem 3 (Local/Deterministic Inference Engine) will optimize the LLM backends:
- Better local models (32B on 19GB VRAM)
- AICP routing improvements (complexity-based backend selection)
- Prompt optimization for smaller models
- Batch processing for efficiency

This subsystem builds the pipeline and backend abstraction. Subsystem 3 improves what runs behind it.
