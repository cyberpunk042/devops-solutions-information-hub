# Knowledge Systems

The foundational domain of this wiki — where the wiki documents how it works. Covers the LLM Wiki pattern, PKM theory (PARA, Zettelkasten), evolution pipeline, knowledge graphs, memory lifecycle, ingestion, and retrieval-augmented generation.

**Model:** [[model-llm-wiki|Model — LLM Wiki]] | **Standards:** [[model-llm-wiki-standards|LLM Wiki Standards — What Good Looks Like]]

### Start Here

1. [[llm-wiki-pattern|LLM Wiki Pattern]] — The core pattern: LLMs maintain structured markdown wikis
2. [[second-brain-architecture|Second Brain Architecture]] — The PKM architecture this wiki implements
3. [[knowledge-evolution-pipeline|Knowledge Evolution Pipeline]] — How pages promote from seed to canonical

### Wiki Architecture

| Page | What it covers |
|------|---------------|
| [[llm-wiki-pattern|LLM Wiki Pattern]] | Karpathy's approach to LLM-maintained knowledge bases |
| [[wiki-ingestion-pipeline|Wiki Ingestion Pipeline]] | How raw sources become structured wiki pages |
| [[wiki-knowledge-graph|Wiki Knowledge Graph]] | Entity-relationship layer over the wiki |
| [[wiki-backlog-pattern|Wiki Backlog Pattern]] | Wiki as both knowledge base and project tracker |
| [[memory-lifecycle-management|Memory Lifecycle Management]] | Knowledge validity, staleness, and decay |
| [[knowledge-evolution-pipeline|Knowledge Evolution Pipeline]] | Maturity promotion: seed to canonical |

### PKM Theory

| Page | What it covers |
|------|---------------|
| [[second-brain-architecture|Second Brain Architecture]] | Externalized thinking systems (Forte, Karpathy) |
| [[para-methodology|PARA Methodology]] | Tiago Forte's action-oriented PKM framework |
| [[zettelkasten-methodology|Zettelkasten Methodology]] | Luhmann's atomic-note slip-box system |

### Scale and Retrieval

| Page | What it covers |
|------|---------------|
| [[llm-wiki-vs-rag|LLM Wiki vs RAG]] | Side-by-side comparison of wiki navigation vs vector search |
| [[lightrag|LightRAG]] | Graph-based RAG framework (HKU, EMNLP 2025) |

## Pages

- [Knowledge Evolution Pipeline](knowledge-evolution-pipeline.md) — The knowledge evolution pipeline is the mechanism by which this wiki promotes raw synthesized pages through increasin...
- [LightRAG](lightrag.md) — LightRAG is a graph-based Retrieval-Augmented Generation framework from HKU Data Science (EMNLP 2025) that incorporat...
- [LLM Wiki Pattern](llm-wiki-pattern.md) — The LLM Wiki Pattern is Andrej Karpathy's approach to building personal knowledge bases using LLMs and plain markdown...
- [LLM Wiki vs RAG](llm-wiki-vs-rag.md) — This comparison examines Karpathy's LLM Wiki approach against traditional semantic search RAG, based on a side-by-sid...
- [Memory Lifecycle Management](memory-lifecycle-management.md) — Memory Lifecycle Management is the practice of treating knowledge in an LLM-maintained wiki as having variable validi...
- [PARA Methodology](para-methodology.md) — PARA is Tiago Forte's action-oriented personal knowledge management framework that organizes all information into fou...
- [Second Brain Architecture](second-brain-architecture.md) — A second brain is a personal knowledge management system designed to externalize thinking: capturing, organizing, dis...
- [Wiki Backlog Pattern](wiki-backlog-pattern.md) — The Wiki Backlog Pattern is an approach to project management where the wiki knowledge base also serves as the comple...
- [Wiki Ingestion Pipeline](wiki-ingestion-pipeline.md) — The wiki ingestion pipeline is the workflow by which raw source documents are transformed into structured, interlinke...
- [Wiki Knowledge Graph](wiki-knowledge-graph.md) — The Wiki Knowledge Graph is an architectural extension to the LLM Wiki pattern that layers typed entity-relationship ...
- [Zettelkasten Methodology](zettelkasten-methodology.md) — Zettelkasten (German: "slip box") is Niklas Luhmann's personal knowledge management system built on three principles:...

## Tags

`second-brain`, `knowledge-graph`, `entity-extraction`, `hybrid-search`, `llm-wiki`, `pkm`, `knowledge-management`, `pipeline`, `rag`, `openfleet`, `knowledge-base`, `markdown`, `para`, `zettelkasten`, `atomic-notes`, `evolution`, `knowledge-systems`, `maturity`, `scoring`, `llm-automation`
