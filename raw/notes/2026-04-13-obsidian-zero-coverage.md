# Operator Directive: Obsidian Near-Zero Coverage
Date: 2026-04-13

## Verbatim

"WHy would you resrun the sync that's retard... WILL YOU FUCKING FOCUS ON THE TASK ALREADY...."
"Like I told you its almost all the links and pages I need.... i just gave you a bunch at it was basically 100%. there was only 4 links over 150+ in the entire pages... you are minizing the situation.. its more like we have a 0.01% coverage right now...."

## Examples Given

- Artifact Chain — TypeScript-Node Domain
- Artifact Chain — Python-Wiki Domain
- Artifact Chain — Infrastructure-IaC Domain
- Artifact Chain — Knowledge-Evolution Domain
- Methodology Standards — What Good Execution Looks Like
- [[Model — LLM Wiki]]
- [[Methodology Framework]]
- [[Methodology System Map]]
- [[Methodology Adoption Guide]]

## Root Cause

Obsidian resolves [[wikilinks]] by FILENAME not by title or alias. Our filenames are kebab-case (model-llm-wiki.md) but our wikilinks use full titles ([[Model — LLM Wiki]]). The aliases I added to frontmatter haven't synced yet, and even if they did, the operator is saying the navigation experience is fundamentally broken — nearly 0% of links work from their perspective browsing in Obsidian.

The problem is NOT link resolution code — it's that the CONTENT references concepts by their full title, and Obsidian can't match those to the kebab-case filenames. This has been the problem from the start and I kept working around it instead of solving it.
