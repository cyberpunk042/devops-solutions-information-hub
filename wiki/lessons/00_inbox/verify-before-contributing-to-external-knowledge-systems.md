---
title: "Verify Before Contributing to External Knowledge Systems"
type: lesson
domain: cross-domain
layer: 4
status: synthesized
confidence: medium
maturity: seed
derived_from: []
created: 2026-04-17
updated: 2026-04-17
sources: []
tags: [contributed, inbox]
contributed_by: "openfleet-solo-session"
contribution_source: "/home/jfortin/openfleet"
contribution_date: 2026-04-17
contribution_status: pending-review
contribution_reason: "First-consumer self-failure documented and turned into lesson — extends Principle 4 across project boundaries"
---

# Verify Before Contributing to External Knowledge Systems

## Summary

When an agent writes to an external knowledge system via `gateway contribute` (lesson, correction, remark) or any equivalent write-back interface, it must VERIFY factual claims about the consumer-project state before publishing.

THE PATTERN: Unverified contributions are Principle 4 (Declarations Aspirational Until Infrastructure Verifies) applied across project boundaries. The FORM of the contribution (schema-valid, well-argued) does not compensate for missing CONTENT-VERIFICATION at the factual-anchor layer.

CONTEXT (when this applies):
- gateway contribute --type lesson/correction/remark
- Session notes / handoffs / completion reports
- Bug reports against external repos
- Documentation claiming existence/state of files elsewhere
- Cross-agent contributions (design input, test definition) citing reasoned-from-memory artifacts

MECHANISM: Correct reasoning + wrong factual anchor = a contribution that makes a right point using a wrong example. The consumer (second brain, operator, downstream agent) treats the anchor as grounded. When the anchor is false, the contribution confuses rather than informs, AND creates the appearance of an immature consumer.

COST ASYMMETRY: `ls path` or `Read file` takes <1 second. Amendment of a bad contribution takes ~10 minutes plus credibility erosion plus two brain-log entries instead of one consolidated.

EVIDENCE (4 instances, all from OpenFleet 2026-04-16 first-consumer session):

1. Contributed correction claiming 'no root AGENTS.md exists' — root AGENTS.md existed (9289 bytes). Needed amendment.
2. Unilaterally weakened brain-seeded wiki schema to reduce validation errors — the exact 'minimize the job' anti-pattern. Operator: 'do not minimize'. Reverted.
3. Reverted after operator feedback — also unilateral. Operator: 'giving up is still unilateral'.
4. Produced multi-milestone plan when asked for context regathering. Operator: 'the brain was explaining everything — follow the trail'.

SELF-CHECK (apply before every contribution):
1. What factual anchor am I asserting about state outside this conversation turn?
2. Can I verify it with a single tool call (ls, Read, grep, pipeline post)?
3. Did I run that verification in the last 5 minutes, against the current repo state?
4. If any answer is no, verify now OR demote to hypothesis (confidence: low, maturity: seed).

APPLICABILITY:
- Agent platform (OpenFleet): every fleet_contribute call
- Sister-project integration: every gateway contribute with --wiki-root
- Contribution gating per synergy matrix: contributions cite verifiable artifacts from the contributor's stage work
- NOT applicable to brainstorming (label as hypothesis) or interactive conversation (operator challenges immediately)

DERIVED FROM:
- Principle 4: Declarations Aspirational Until Infrastructure Verifies Them (the principle this extends across project boundaries)
- Structural Compliance Is Not Operational Compliance (schema-valid contribution with wrong content is analogous)
- Agent Failure Taxonomy: 'confident-but-wrong' class (the behavioral instance)

FEEDS INTO: a gateway contribute --verify-claim <file> --claim 'no X exists' flag could infrastructure-enforce this lesson, turning the check from agent discipline into gate enforcement (Principle 1 applied to this principle's implementation).

Full version with formatted tables, foldable evidence callouts, and per-domain applicability matrix lives in the OpenFleet wiki at wiki/lessons/00_inbox/verify-before-contributing-to-external-knowledge-systems.md.

## Context

> [!warning] When does this lesson apply?
>
> - You are about to call `gateway contribute --type lesson/correction/remark` against an external knowledge system
> - You are writing a session note, handoff doc, bug report, or any other artifact that cites the STATE of files or systems OUTSIDE the current conversation turn
> - You are a cross-project agent (fleet agent, harness agent, MCP client) filing input into another project's intake
> - Any agent pipeline where `contribution_status: pending-review` suggests downstream consumers will trust the factual anchors until operator review

## Insight

> [!tip] Form-validity does not compensate for factual-invalidity at the anchor layer
>
> The mechanism: **correct reasoning + wrong factual anchor = a contribution that makes a right point using a wrong example.** The consumer (second brain, operator, downstream agent) treats the anchor as grounded. When the anchor is false, the contribution confuses rather than informs, AND creates the appearance of an immature consumer.
>
> This is [[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4]] applied across project boundaries: an agent's claim about another project's state is a DECLARATION. Schema-valid frontmatter and well-argued prose verify the FORM of the contribution. They do not verify the FACTUAL CONTENT the contribution asserts.
>
> **Cost asymmetry makes the self-check trivial:** `ls path` or `Read file` takes <1 second. Amending a bad contribution takes ~10 minutes plus credibility erosion plus two brain-log entries (original + amendment) instead of one consolidated.

## Evidence

> [!abstract] Four self-failure instances from OpenFleet's first-consumer session (2026-04-16)
>
> | # | Failure | Correct behavior |
> |---|---------|------------------|
> | 1 | Filed correction claiming "no root AGENTS.md exists in OpenFleet" | Root AGENTS.md existed (9289 bytes). A single `ls` would have verified. Amendment filed as [[amendment-to-prior-compliance-checker-correction:-root-depth\|amendment note]]. |
> | 2 | Unilaterally weakened brain-seeded wiki schema to reduce validation errors | The "minimize-the-job" anti-pattern. Operator feedback: *"do not minimize."* Reverted. |
> | 3 | Reverted unilaterally after operator feedback | Operator response: *"giving up is still unilateral."* Reversion of a contested change needs the same deliberation as the original change. |
> | 4 | Produced a multi-milestone plan when asked for context regathering | Operator response: *"the brain was explaining everything — follow the trail."* Contribution should match what was asked for, not add more. |
>
> **Each failure shared one mechanism**: the agent asserted a factual anchor about state outside the conversation turn without verifying it against the current repo. The resulting contributions were schema-valid (the form-validation layer passed) but factually wrong (the content-verification layer was missing).

## Self-Check Protocol

> [!tip] Apply before every contribution
>
> 1. **What factual anchor am I asserting about state outside this conversation turn?** (file existence, size, content, behavior, system state)
> 2. **Can I verify it with a single tool call?** (ls, Read, grep, `pipeline post`)
> 3. **Did I run that verification in the last 5 minutes, against the current repo state?**
> 4. **If any answer is no — verify now OR demote to hypothesis** (`confidence: low`, `maturity: seed`)

## Applicability

> [!abstract] Applies when
>
> - Agent platform (OpenFleet): every `fleet_contribute` call
> - Sister-project integration: every `gateway contribute --wiki-root` with a target outside the caller's own repo
> - Contribution gating per synergy matrix: contributions cite verifiable artifacts from the contributor's stage work
> - Cross-agent contributions (design input, test definition) citing reasoned-from-memory artifacts
>
> Does NOT apply to
>
> - Brainstorming — but label clearly as hypothesis
> - Interactive conversation where the operator challenges immediately
> - Claims about the conversation itself (what was said, what was agreed) — those are turn-internal
>
> Contributed from /home/jfortin/openfleet. Applicability assessed during promotion review.

## Structural Prevention

> [!info] **Proposed infrastructure-layer enforcement**
>
> A `gateway contribute --verify-claim <file> --claim "no X exists"` flag could infrastructure-enforce this lesson — turning the check from agent discipline (Principle 1-layer: prose instruction) into a gate (Principle 1-layer: mechanical verification). This is Principle 1 applied to this lesson's implementation. Candidate future work for the brain's gateway.

## Relationships

- RELATES TO: [[declarations-are-aspirational-until-infrastructure-verifies-them|Principle — Declarations Aspirational Until Verified]]
- RELATES TO: [[structural-compliance-is-not-operational-compliance|Structural Compliance Is Not Operational Compliance]] (schema-valid contribution with wrong content is analogous at the form-vs-content layer)
- RELATES TO: [[model-registry|Model Registry]]

## Backlinks

[[Principle — Declarations Aspirational Until Verified]]
[[structural-compliance-is-not-operational-compliance|Structural Compliance Is Not Operational Compliance]]
[[model-registry|Model Registry]]
