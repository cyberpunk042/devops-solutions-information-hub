---
title: "Operations Plan: {{title}}"
type: operations-plan
domain: {{domain}}
status: synthesized
confidence: medium
maturity: seed
created: {{date}}
updated: {{date}}
sources: []
tags: [operations-plan]
---

# Operations Plan: {{title}}

## Summary

<!-- 2-3 sentences: what this plan executes and what the end state is.
     An operations plan is DETERMINISTIC — any agent following it produces the same result.
     This is NOT a design plan. No alternatives analysis, no trade-offs.
     If judgment is required, this should be a design plan (concept type) instead. -->

## Prerequisites

<!-- What must be true BEFORE step 1. Existing state, tools installed,
     access required, prior artifacts that must exist.
     Format: - [ ] Prerequisite (how to verify) -->

## Steps

<!-- Sequential steps. Each step is independently verifiable.
     A "dumb" agent should be able to follow these mechanically.

### Step 1: {{action_title}}

- **Action:** What to do (specific command, file to create, config to change)
- **Expected output:** What success looks like
- **Validation:** How to verify this step worked (command to run, file to check)
- **Rollback:** What to do if this step fails

### Step 2: ...
-->

## Rollback

<!-- Global rollback procedure if the plan fails partway through.
     How to restore the system to pre-plan state. -->

## Completion Criteria

<!-- How to verify the ENTIRE plan succeeded.
     Format: - [ ] Verifiable criterion -->



### Step 1: {{Action title}}

<!-- EXAMPLE step (replace with your content): -->

- **Action:** Run the gateway auto-detection on your project
- **Command:** `python3 -m tools.gateway what-do-i-need`
- **Expected output:** Detected identity with recommended chain and first steps
- **Validation:** Domain and scale match your project. Execution mode says "unknown" (correct — can't auto-detect)
- **Rollback:** No state changed — this is a read-only query

### Step 2: {{Next action}}

## Relationships

- IMPLEMENTS: {{what_this_plan_executes}}
