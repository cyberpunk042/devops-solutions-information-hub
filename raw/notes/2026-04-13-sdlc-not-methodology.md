# Operator Directive: SDLC Is NOT Methodology
Date: 2026-04-13

## Verbatim

"Bad start... you are conflating methodology with sdlc... you cannot duplicate what methodology does in sdlc lol... do you even know what sdlc is ??? do did you forget everything ?"

## What This Means

SDLC and methodology are DIFFERENT LAYERS:

- SDLC = the SOFTWARE DEVELOPMENT LIFECYCLE — the overall project lifecycle. Phases (POC → MVP → Staging → Production), scale, chain selection (simplified/default/full). It's ABOVE methodology.
- Methodology = HOW work proceeds WITHIN an SDLC phase. Stage gates (document → design → scaffold → implement → test), task types, models.

The SDLC config is NOT "parent of methodology.yaml." It's a DIFFERENT concern:
- SDLC defines: what phases exist, what chain level applies, when to upgrade chains, what readiness gates exist at the project level
- Methodology defines: what stages exist within a task, what artifacts each stage produces, what models apply

You don't put methodology artifacts inside SDLC config. They're separate configs for separate layers.
