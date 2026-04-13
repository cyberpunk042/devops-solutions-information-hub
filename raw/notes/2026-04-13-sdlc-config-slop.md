# Operator Directive: SDLC Config Files Are Slop
Date: 2026-04-13

## Verbatim

"Absolutely.... that's a start... how come that the research didn't make all this surface and that this slop is in place ? was there bad ingestion and reasoning and we have crap artifacts ?"

## Root Cause Analysis

The SDLC chain config files (simplified.yaml, default.yaml, full.yaml) duplicate methodology concerns — they define stages, artifacts, readiness ranges, gate commands. That's methodology.yaml's job.

This happened because:
1. The configs were SCAFFOLDED during a rush phase (the "37 files in one sprint = Mountain tier" incident)
2. The scaffolding was done BEFORE the SDLC vs methodology distinction was properly understood
3. The research (CMMI, Lean Startup, EPAM ADLC, PwC Agentic SDLC) WAS ingested but the SYNTHESIS didn't properly separate the two layers
4. The source synthesis page (src-sdlc-frameworks-research.md) covers phase progression and maturity levels — but the CONFIG FILES were created by copying methodology.yaml's structure and calling it "SDLC"
5. No one reviewed the configs against the research — the scaffold was treated as done

This is exactly the pattern the operator warned about: "volume is not quality" and "hardcoded instances fail." The configs are hardcoded instances of a conflated understanding.

## What Needs to Happen

1. Rewrite SDLC chain configs to define POLICY (phase, scale, enforcement, triggers) not EXECUTION (stages, artifacts, gates)
2. Review the SDLC wiki page to ensure it correctly distinguishes the two layers
3. Check if the conflation leaked into other pages (models, standards, domain chains)
4. The methodology.yaml should be the ONLY place that defines stages and artifacts
