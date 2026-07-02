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
  source: "hf-org/repo"            # HuggingFace repo of THIS model, when it exists, else null
  base_model: "hf-org/repo"        # for a quantized/derived variant: the real base to quantize
  confidence: high | medium | low  # low = uncertain handwriting reading / tentative
  status: real | aspirational | unverified   # does this model actually EXIST?
  notes: "free text — alternatives (ou X), scribbled sizes, provenance caveats"
  # ---- optional perf dimensions (OMIT when unmeasured; absent = unknown) ----
  # Do NOT guess these — leave absent until measured/sourced. The routing layer
  # treats absent as "unknown" and falls back to param-size ordering.
  vram_gb: 24                     # approx GPU memory footprint at its quantization
  context_window: 132000          # max context tokens
  throughput_tok_s: 44            # approx tokens/sec on its primary tier
```

`quantization` note: `ternary` and `bitnet-1.58` are the same weight class
({-1,0,1}); keep them distinct only when the source names 1.58-bit explicitly.

The three perf fields are **optional and honest**: omit them rather than invent
a number. They exist so measured values have a home and so the routing layer can
prefer a model that fits VRAM / needs the context window when the data is present.

`base_model` records the confirmed-real upstream for a `-ternary` / quantized
entry whose own quantized artifact isn't (yet) a published repo: the base exists,
the quant is a target. Such an entry keeps `status: unverified` (the variant
itself is unconfirmed) but is *actionable* — you know exactly what to quantize.

`status` is the **reality check** for a handwriting-seeded catalog:
`real` (confirmed to exist upstream — HF repo or famous research model),
`aspirational` (a target/wishlist name with no known upstream yet), or
`unverified` (default — not yet checked). When the field is absent the loader
**derives** it honestly: a model with a non-null `source` (a real HF repo id)
counts as `real`; everything else is `unverified`. The `unverified` set is firmed
up by a Hugging Face existence check via the HF MCP tools (operator-approved,
since outbound HF access is gated) — set an explicit `status` + `source` on each
model the check confirms or refutes. Status is deliberately **not** asserted
from memory; it is only ever set from a real source or a live check.

## Complexity bands (the routing vocabulary)

Complexity-routed inference picks the **smallest sufficient** model for a task's
difficulty. Bands are a shared, ordered vocabulary (numeric range on a 0–1
task-complexity score); profiles map each band to a preferred model:

| Band | Score | Typical size | Meaning |
|---|---|---|---|
| `trivial` | 0.00–0.20 | ≤2B / inline | autocomplete, boilerplate, single-line |
| `simple` | 0.20–0.40 | 3–8B | short, well-specified tasks |
| `moderate` | 0.40–0.65 | 8–15B | multi-step, some reasoning |
| `hard` | 0.65–0.85 | 30–70B | deep reasoning, long context |
| `expert` | 0.85–1.00 | 70B+ / groups | hardest / highest-stakes |

Band→size mapping is the **default heuristic** (bigger model = higher band);
per-profile `routing` overrides it with the operator's actual choices.

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
  selections:                    # per hardware tier → ordered model/group ids (availability)
    cpu:      [model-or-group-id, ...]
    rtx-4090: [model-or-group-id, ...]
    rtx-pro:  [model-or-group-id, ...]
  routing:                       # complexity band → the model that fires (the routing signal)
    - {band: trivial,  prefer: model-or-group-id}
    - {band: moderate, prefer: model-or-group-id}
    - {band: expert,   prefer: model-or-group-id}
  notes: "free text"
```

`selections` says *what is available* on each tier; `routing` says *which model
fires at which task-complexity*. A `routing` entry's `prefer` must be a model or
group id that also appears in this profile's `selections`. Bands may be sparse
(list only the ones this profile distinguishes); AICP rounds a task's complexity
score to the nearest defined band at or below it.

## How to extend (the flexibility contract)

- **Add a model** → append one entry to `models.yaml`. Nothing else changes.
- **Add a group** → append to `groups.yaml`, referencing existing model ids.
- **Add / re-route a profile** → edit `profiles.yaml`; reference ids, don't inline model details.
- **A model is uncertain / tentative** → `confidence: low` + a `notes` caveat. Never drop it; the catalog is a living surface (`"everything evolves and everything is flexible"`).
- Ids are the join keys. Keep them stable; groups and profiles resolve models by id.

## Consuming the catalog (AICP contract)

`tools/model_catalog.py` is the shared loader/resolver. It reads the three
YAMLs, checks referential integrity, and produces a single **resolved** object
(profiles with their `routing` bands expanded to full model records). AICP —
the complexity-routed local-inference layer — consumes that resolved form:

```
python3 -m tools.model_catalog validate           # referential-integrity gate
python3 -m tools.model_catalog export [OUT.json]   # write the resolved JSON contract
```

`export` writes `wiki/config/model-catalog/model-catalog.generated.json` by
default (a stable machine contract: `{models, groups, profiles}` with routing
resolved). AICP pulls that JSON (or imports `tools.model_catalog.load_resolved()`
directly when co-located). The generated JSON is a build artifact — regenerate it
after edits; the YAMLs are the source of truth.

## Validation

These are config files (not pages), so `pipeline post` does not schema-check
them as wiki pages. Referential integrity — every group member, profile
selection, and `routing.prefer` id resolves, and every `routing.prefer` is also
in that profile's `selections` — is enforced by `tools/model_catalog.py`
(hard fail on a dangling ref; advisory warnings on unknown enum values so the
catalog stays extensible). `tools/validate_model_catalog.py` remains as a thin
alias. Run after every edit.
