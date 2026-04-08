# Claude Code Research & Content Pipeline

> Compiled from two video transcripts: "Claude + NotebookLM = Your 24/7 Content Team" (by Jay) and "Andrej Karpathy Just 10x'd Everyone's Claude Code" (by Nate/Herk)

---

## Overview

This guide documents a two-layer AI-powered research and content system:

1. **Knowledge Layer** — Karpathy's LLM Wiki method: Claude Code builds and maintains an interlinked markdown knowledge base in Obsidian
2. **Content Layer** — Claude Code + NotebookLM: automated generation of slides, podcasts, videos, and summaries from that knowledge base

Together, they create a pipeline where knowledge compounds over time and content is generated on autopilot.

---

## Architecture

```
[Raw Sources]           [LLM Wiki / Obsidian Vault]           [NotebookLM]
  Articles   ──┐            ┌─ wiki/                          ┌─ Slide Decks
  YouTube     ──┤  Claude    │    ├─ topic-a.md ──────┐       ├─ Audio Podcasts
  Web pages   ──┼──Code────> │    ├─ topic-b.md       │Claude ├─ Video Overviews
  PDFs        ──┤  ingests   │    └─ topic-c.md ──────┼─Code──├─ Mind Maps
  Notes       ──┘            ├─ raw/                   │       ├─ Flashcards
                             ├─ index.md               │       └─ Reports
                             ├─ hot.md (cache)         │
                             └─ CLAUDE.md (schema)     └──────> [Notebooks]
```

---

## Part 1: The LLM Wiki (Karpathy Method)

### What it is

Instead of using a vector database or RAG pipeline, you give Claude well-organized markdown files with an index and interlinks. Claude navigates them like a human would — reading indexes, following links, understanding relationships.

### Why it works

- Finds info by reading indexes and following links (not similarity search)
- Deeper understanding of relationships because they're explicit links
- Claude can identify gaps and suggest new research
- Lower token usage than stuffing raw context files
- Works well up to hundreds of pages with good indexes

### When NOT to use it

- Millions of documents → use traditional RAG/semantic search instead
- Enterprise-scale data → cost becomes prohibitive with pure LLM approach

### Karpathy's LLM Wiki vs Traditional RAG

| Aspect | LLM Wiki | Semantic Search RAG |
|--------|----------|-------------------|
| Retrieval | Reads indexes, follows links | Vector similarity search |
| Relationships | Explicit links between notes | Implicit chunk similarity |
| Scale sweet spot | Hundreds of pages | Thousands to millions |
| Setup complexity | Paste a prompt, done | Embeddings pipeline, vector DB |
| Maintenance | Claude lints and updates | Re-indexing, chunk tuning |
| Cost at scale | Grows with token usage | More predictable |

### Folder structure

```
vault/
├── CLAUDE.md          # Schema + instructions for Claude
├── index.md           # Master index of all topics
├── hot.md             # Hot cache (~500 chars of most recent context)
├── raw/               # Unprocessed source material
│   ├── article-1.md
│   └── article-2.md
└── wiki/              # Processed, interlinked knowledge pages
    ├── topic-a.md
    ├── topic-b.md
    └── subtopic-a1.md
```

### Setup steps

1. **Install Obsidian** (free) from obsidian.md
2. **Create a new vault** — name it whatever you want (e.g., "my-brain", "research-wiki")
3. **Open the vault folder in Claude Code**
4. **Paste Karpathy's LLM wiki prompt** into Claude Code — it will scaffold the entire structure
5. **Install "Obsidian Web Clipper"** browser extension — configure it to save to `raw/` folder

### Ingesting sources

Drop a file into `raw/`, then tell Claude Code:

```
Hey, I just dropped an article called "AI 2027" into raw/. Can you ingest that?
```

Claude will:
- Read the raw source
- Ask clarifying questions (what to emphasize, how granular, your focus area)
- Break it into multiple interlinked wiki pages (a single article might become 10-25 pages)
- Create relationships/links between new and existing pages
- Update the index

### Querying the wiki

Claude Code can navigate the wiki to answer questions:

```
What do we know about compute scaling trends across all the sources I've ingested?
```

It reads the index → follows relevant links → synthesizes an answer grounded in your sources.

### Linting / health checks

Karpathy recommends periodic LLM health checks over the wiki:
- Find inconsistent data
- Impute missing data with web searches
- Discover interesting connections for new article candidates
- Ensure everything is properly structured and linked

Run manually or schedule (daily/weekly).

### Hot cache

Optional `hot.md` file (~500 chars) that stores the most recent/relevant context. Useful for:
- Executive assistant use cases (saves crawling wiki pages for recent context)
- Not needed for pure research/transcript projects

---

## Part 2: Claude Code + NotebookLM Integration

### What it is

Claude Code controls Google NotebookLM programmatically — creating notebooks, loading sources, and generating assets without you touching the NotebookLM UI.

### Prerequisites

- Claude Code (via desktop app, terminal, or IDE extension)
- Google account (NotebookLM is free)
- The **NotebookLM skill** (markdown file with instructions)
- `notebooklm-py` Python package (by Tang Li) — installed automatically by the skill

### Setup

1. **Get the NotebookLM skill** — available in Jay's "Robo Nuggets" community
2. **Give the skill to Claude Code** — it will:
   - Install the `notebooklm-py` package
   - Open Chrome for Google account login
   - Save credentials for future use
3. **Verify**: "Hey Claude, can you list my latest 3 notebooks in NotebookLM?"

### Capabilities once connected

| Category | What Claude can do |
|----------|-------------------|
| Notebook management | Create, list, rename, delete notebooks |
| Sources | Pull from web, YouTube; upload local files |
| Chat | Interact with notebook sources from Claude Code |
| Slide decks | Generate branded presentations |
| Audio | Podcast-style MP3 overviews |
| Video | Cinematic video summaries |
| Other | Mind maps, flashcards, reports, quizzes, infographics |

### Basic usage

```
Hey Claude, can you use NotebookLM to do research on [TOPIC]?
Load sources from YouTube and the web, and generate a slide deck for me.
```

Claude will:
1. Create a new notebook
2. Search and load relevant sources
3. Generate the requested assets (slides, audio, video, etc.)

### Custom slide design

The skill markdown contains a slide generation section that controls design. You can:

1. **Ask Claude to tweak it directly**:
   ```
   I want more blue-tone colors, still dark mode, but more corporate.
   Can you refine the skill and submit a new prompt to NotebookLM?
   ```

2. **Feed it a brand book image** — Claude analyzes it and updates the skill to match your palette

3. **Save multiple styles** — e.g., "blackboard" (orange/black/slab fonts) and "corporate navy" as selectable options in the skill

### Example slide prompt (what Claude sends under the hood)

Claude constructs a prompt like:
- Create a 7-slide presenter deck
- Design guidance (colors, layout, fonts)
- Title content per slide
- Based on the research in the source material

---

## Part 3: Scheduling & Automation

### Local scheduled tasks

Use Claude Code's **schedule tab** (left sidebar):

1. Add new task
2. Name it (e.g., "cybersecurity research daily")
3. Write the prompt:
   ```
   Use NotebookLM and the skill I provided to research cybersecurity
   trends. Generate slides in the blackboard design. Run at 12:00 noon
   Sydney time daily.
   ```
4. Set permissions (bypass for low-risk tasks)
5. Select workspace
6. Define cron schedule

**Important**: Local tasks only run when your machine is on.

### Remote scheduled tasks

For tasks that run even when your machine is off:

- Uses **Anthropic's remote task feature**
- Requires a GitHub account
- Workspace must be on GitHub
- Runs on Anthropic's cloud

### Alternative: Long-running Claude Code sessions

As shown in Video 2, you can run persistent Claude Code sessions (e.g., in terminal tabs) that act as always-on agents. These can be configured with a cron registry (JSON file) listing scheduled tasks.

---

## Part 4: Connecting Both Systems

### The full pipeline

1. **Accumulate knowledge** → Ingest articles, videos, web pages into your Obsidian LLM Wiki
2. **Query and synthesize** → Ask Claude to analyze your wiki, find patterns, identify gaps
3. **Generate content** → Push wiki research into NotebookLM for slides, podcasts, videos
4. **Automate** → Schedule daily research ingestion and content generation
5. **Iterate** → Claude lints the wiki, suggests new sources, fills gaps

### Example daily automation

```
Schedule: Every day at 8am
1. Search for latest articles on [your topics]
2. Ingest new sources into the LLM Wiki
3. Run a wiki lint to check for gaps
4. Push today's research into a NotebookLM notebook
5. Generate a podcast summary for my morning commute
6. Generate a slide deck for my team standup
```

---

## Key Tools & Resources

| Tool | Purpose | Cost | URL |
|------|---------|------|-----|
| Claude Code | AI agent that orchestrates everything | Claude Pro/Max subscription | claude.com/download |
| Obsidian | Markdown knowledge base with graph view | Free | obsidian.md |
| NotebookLM | Google's AI research tool for content generation | Free | notebooklm.google.com |
| Obsidian Web Clipper | Browser extension to clip articles to vault | Free | Obsidian community plugins |
| notebooklm-py | Python package for programmatic NotebookLM access | Free/open source | GitHub (Tang Li) |

---

## Claude Code access methods

| Method | Description |
|--------|-------------|
| Desktop app — Chat tab | Like ChatGPT, conversational |
| Desktop app — Co-work tab | File organization, web browsing |
| Desktop app — Code tab | Most capable, build integrations |
| Terminal | `claude` command, full functionality |
| IDE extension | VS Code, IntelliJ — integrated with editor |

Jay recommends **Claude Code** (code tab or terminal) for this integration as it's the most capable mode.

---

## Tips from the videos

- **Skills are just markdown files** — text instructions that teach Claude how to use tools and follow design patterns
- **Ask Claude clarifying questions** — use Q&A format to align intent before big operations
- **Start simple** — get the wiki working first, then add NotebookLM, then automation
- **The wiki reduces token usage** — compared to raw context files, the indexed wiki structure is more efficient
- **Graph view is your friend** — Obsidian's graph view lets you visually explore knowledge relationships
- **Linting is important** — periodic health checks keep the wiki accurate and well-structured

---

*Compiled from NoteGPT transcripts, April 2026*
