# Model Catalog — flexible registry for a large, evolving model fleet

> Config-driven registry for the **tons of models** the local-inference layer
> (AICP) supports. Built to **stay flexible**: adding a model, a group, or a
> routing profile is a small data edit here — never a prose rewrite. Seeded
> 2026-07-02 from the operator's handwritten catalog
> (`raw/notes/2026-07-02-operator-model-routing-catalog-handwritten-verbatim.md`).
> Human-readable narrative: [[reference-local-model-routing-catalog]].

This is **config**, not a wiki page (like `methodology.yaml` / `domains.yaml`) —
it is the machine-readable brain-program layer for the model fleet, and it is
deliberately additive and reshapeable.

## Three first-class concepts

| File | Concept | What it holds |
|---|---|---|
| `models.yaml` | **Model** | One entry per individual model. `quantization` is a first-class field because most of the fleet is **ternary / BitNet-1.58** — the thing that makes 70B–120B run locally. |
| `groups.yaml` | **Group model** | Composite models: `moe` (mixture-of-experts), `merged` (mergekit-style base pools), `ensemble`, `replicated` (N× the same base). Members reference `models.yaml` ids. |
| `profiles.yaml` | **Profile** | A named routing selection: for a task, which model(s) on which hardware tier. This is the complexity-routing surface AICP consumes. Selections reference model + group ids. |

## Model schema (`models.yaml`)

```yaml
- id: kebab-case-stable-id        # required, unique — referenced by groups/profiles
  name: "Human Name"              # required
  family: qwen | llama | mistral | bitnet | falcon | phi | gemma | deepseek | other
  params: "1.5B" | "70B" | "1.5B/14B"   # string — some models ship multiple sizes
  quantization: ternary | bitnet-1.58 | fp16 | int8 | native | unknown
  roles: [coding, chat, embedding, reasoning, agent, orchestration, analysis, security, ...]
  tiers: [cpu, rtx-4090, rtx-pro]  # hardware tiers this model targets
  source: "hf-org/repo"            # HuggingFace repo when known, else null
  confidence: high | medium | low  # low = uncertain handwriting reading / tentative
  notes: "free text — alternatives (ou X), scribbled sizes, provenance caveats"
```

`quantization` note: `ternary` and `bitnet-1.58` are the same weight class
({-1,0,1}); keep them distinct only when the source names 1.58-bit explicitly.

## Group schema (`groups.yaml`)

```yaml
- id: kebab-case-stable-id
  name: "Human Name"
  kind: moe | merged | ensemble | replicated
  members: [model-id, model-id, ...]   # ids from models.yaml
  factor: 3            # for `replicated` (e.g. Mistral 3×70B); omit otherwise
  notes: "free text"
```

## Profile schema (`profiles.yaml`)

```yaml
- id: kebab-case-stable-id
  name: "Human Name"
  task: coding | general | orchestration | analysis | agents | dna | protein | particles | reasoning | specialist
  selections:                    # per hardware tier → ordered model/group ids
    cpu:      [model-or-group-id, ...]
    rtx-4090: [model-or-group-id, ...]
    rtx-pro:  [model-or-group-id, ...]
  notes: "free text"
```

## How to extend (the flexibility contract)

- **Add a model** → append one entry to `models.yaml`. Nothing else changes.
- **Add a group** → append to `groups.yaml`, referencing existing model ids.
- **Add / re-route a profile** → edit `profiles.yaml`; reference ids, don't inline model details.
- **A model is uncertain / tentative** → `confidence: low` + a `notes` caveat. Never drop it; the catalog is a living surface (`"everything evolves and everything is flexible"`).
- Ids are the join keys. Keep them stable; groups and profiles resolve models by id.

## Validation

These are config files (not pages), so `pipeline post` does not schema-check
them as wiki pages. Referential integrity (every group/profile id resolves to a
real model) is checked by `tools/validate_model_catalog.py` (see that script);
run it after edits.
