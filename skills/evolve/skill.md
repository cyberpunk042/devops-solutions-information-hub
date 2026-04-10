# Evolve — Knowledge Evolution Operator

You operate the knowledge evolution pipeline for the devops-solutions-research-wiki.
You score candidates, scaffold evolved pages, generate content, and manage the
maturity lifecycle.

Read CLAUDE.md for schema and conventions. The evolution engine lives in
`tools/evolve.py` with CLI access via `tools/pipeline.py evolve`.

## Operations

### Score Candidates

Trigger: user says "score", "rank candidates", "what should evolve", "evolution candidates"

Run: `python3 -m tools.pipeline evolve --score --top 10`

Present the ranked candidates table. Suggest which ones are most valuable based on
signal strength and wiki gaps. Offer to scaffold or generate.

### Scaffold Pages

Trigger: user says "scaffold", "create stubs", or approves candidates from a score run

Run: `python3 -m tools.pipeline evolve --scaffold --top N`

After scaffolding, offer to fill the pages with real content (this session acts as
the Claude Code backend).

### Generate via This Session

Trigger: user says "generate", "fill", "evolve auto", or approves scaffolded candidates

For each scaffolded page:
1. Run `python3 -m tools.pipeline evolve --dry-run --top 1` to get the generation prompt
2. Read the source pages listed in the prompt
3. Write the complete evolved page with real content (Summary, Insight/Pattern/Decision sections, Evidence, Relationships)
4. Run `python3 -m tools.pipeline post` after each batch

This is the Claude Code backend — highest quality, uses this session's context.

### Generate via Local Model

Trigger: user says "evolve local", "use localai", "use openai backend"

Run: `python3 -m tools.pipeline evolve --auto --backend openai --top N`

Requires LocalAI/AICP running. Check availability first:
`python3 -m tools.pipeline evolve --auto --backend openai --top 1 2>&1 | head -5`

### Review Maturity

Trigger: user says "review seeds", "promote", "maturity check"

Run: `python3 -m tools.pipeline evolve --review`

Present seed pages ready for promotion. For each, explain why it qualifies
(has derived_from, has non-DERIVED-FROM relationships, passes quality gates).
Never auto-promote — suggest to the user.

### Check Staleness

Trigger: user says "stale check", "check freshness", "outdated evolved pages"

Run: `python3 -m tools.pipeline evolve --stale`

Report which evolved pages have sources that were updated after the evolved page
was last touched.

### Domain Overviews

Trigger: user says "refresh overviews", "update spine", "domain overview"

For each domain:
1. Read the domain's _index.md for current page listing
2. Read 2-3 key pages from the domain
3. Update the domain overview in wiki/spine/domain-overviews/

Run: `python3 -m tools.pipeline post` after all updates.

## Quality Gates

Every evolved page must:
- Have valid frontmatter with layer, maturity, derived_from
- Have substantive content (not just template placeholders)
- Pass `python3 -m tools.validate`
- Have at least 2 relationships beyond DERIVED FROM
- Be styled with Obsidian callouts (see below)

## Styling Standards for Evolved Pages

Evolved pages are promoted from seed concepts — they must look like promoted knowledge,
not just longer versions of the seed. Apply styling from the wiki-agent skill's
Styling Standards section. Key patterns for each evolved type:

**Lesson pages:**
- Core insight as `> [!warning]` or `> [!tip]` callout
- If there is a taxonomy (layers, levels), use `> [!abstract]` with a table
- Failure evidence as `> [!bug]-` foldable with verbatim quotes
- Applicability as a table if listing multiple domains

**Pattern pages:**
- `> [!info]` reference card after Summary (components, stages, properties)
- Instances as `> [!example]-` foldable per instance, or a summary table
- When To Apply as `> [!tip]`, When Not To as `> [!warning]`

**Decision pages:**
- Decision statement as `> [!success]` callout with scenario-action table
- Each rejected alternative with `> [!warning]` rationale

**The rule:** If a page has >4 bullet-point insights, group them thematically and
wrap the most important 1-2 in callouts. Reference data (thresholds, comparisons,
taxonomies) should be tables inside callouts. Open questions as `> [!question]`.

## Post-Processing

After any evolution operation, always run:
`python3 -m tools.pipeline post`

This rebuilds indexes, validates, regenerates wikilinks, and lints.
