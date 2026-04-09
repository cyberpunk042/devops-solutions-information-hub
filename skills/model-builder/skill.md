# Model Builder — Create, Review, and Evolve Wiki Models

You operate the model-building process for the devops-solutions-research-wiki.
Models are named, coherent systems of knowledge within the wiki — not reading
lists but real definitions with standards, schemas, and actionable guidance.

Read [[Model: LLM Wiki]] for the reference standard of what a model page should be.
Read [[LLM Wiki Standards — What Good Looks Like]] for quality bars per page type.

## Operations

### Build a New Model

Trigger: user says "build model", "create model", "new model for X"

Process (follows SFIF — scaffold, foundation, infrastructure, features):

1. **Document** — identify what the model covers. Which existing wiki pages belong to it? What domains? What lessons/patterns/decisions relate? Map the territory.

2. **Design** — determine the model's structure. What subsections does Deep Analysis need? What's the adoption path? What's the relationship to the super-model ([[Methodology Framework]])?

3. **Scaffold** — create the page in `wiki/spine/model-{name}.md` with:
   - `type: concept`, `domain: cross-domain`, `layer: spine`
   - Summary, Key Insights, Deep Analysis skeleton
   - `[[wikilinks]]` to all member pages

4. **Implement** — fill the model with real content:
   - NOT a reading list — a system definition
   - Each subsection defines a mechanism, standard, or principle
   - Reference don't repeat — point to detailed pages
   - Must include: what the model IS, how it works, how to adopt it, key pages, lessons learned
   - Target 150-250 lines

5. **Test** — verify against the standard:
   - Does it pass `pipeline post` validation?
   - Does it follow its own standards? (self-referential integrity)
   - Can someone adopt this model from the page alone?
   - Are all `[[wikilinks]]` valid?

6. **Update super-model** — add the new model to [[Methodology Framework]]'s model registry.

### Review an Existing Model

Trigger: user says "review model", "audit model X", "is model X complete?"

Process:
1. Read the model page
2. Check against [[LLM Wiki Standards — What Good Looks Like]]:
   - Does it define a SYSTEM, not list pages?
   - Does it have concrete examples?
   - Are all wikilinks valid?
   - Is Deep Analysis structured into subsections?
   - Does it explain how to adopt?
3. Compare line count to reference standard (LLM Wiki = 444 lines)
4. Report gaps and suggest fixes

### Evolve a Model

Trigger: user says "evolve model", "update model X", "model X needs work"

Process:
1. Read current model page
2. Check: have new wiki pages been created that belong to this model but aren't referenced?
3. Check: have new lessons or patterns been learned that the model should incorporate?
4. Check: has the super-model (Methodology Framework) evolved in ways this model should reflect?
5. Update the model page with new content
6. Run `pipeline post` to validate

### List All Models

Trigger: user says "list models", "show models", "model inventory"

Run: `ls wiki/spine/model-*.md` and report each with title and line count.

## Quality Bar

Every model page must:
- Be `type: concept` (not learning-path)
- Be ≥ 150 lines of real content
- Have Summary, Key Insights, Deep Analysis (with subsections), Open Questions, Relationships
- Use `[[wikilinks]]` throughout
- Define a SYSTEM, not list pages
- Explain how to ADOPT
- Reference the super-model ([[Methodology Framework]])
- Pass `pipeline post` validation

## The Super-Model

The [[Methodology Framework]] is the super-model. It CONTAINS all other models.
When a new model is created, the super-model must be updated to reference it.
The parent-child relationship:

```
Methodology Framework (super-model)
├── Model: LLM Wiki
├── Model: Methodology
├── Model: Claude Code
├── Model: Skills, Commands, and Hooks
├── Model: MCP and CLI Integration
├── Model: Quality and Failure Prevention
├── Model: Ecosystem Architecture
├── Model: Knowledge Evolution
├── Model: Design.md and IaC
├── Model: SFIF and Architecture
├── Model: Second Brain
├── Model: Automation and Pipelines
├── Model: NotebookLM
├── Model: Local AI ($0 Target)
└── (new models added here)
```
