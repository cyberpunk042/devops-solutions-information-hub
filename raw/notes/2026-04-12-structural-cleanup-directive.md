# Structural Cleanup Directive — 2026-04-12

## Operator Directive (verbatim)

> "We need to fix all this and make sure that the new informations that were written at the wrong places will now be at the right place and then we can cleanup and make sure the root is a like a normal project.... and the Wiki stuff like the wiki config are actually in the Wiki....."

## Context

Investigation revealed 84 stale ghost files at repo root duplicating wiki/ content.
Root-level comparisons/, decisions/, domains/, lessons/, patterns/, sources/, spine/
are all older versions from April 6-8 that were never cleaned up after wiki/ became
the canonical home. Two manifest.json files, two index.md files, two .obsidian/ configs.

## Requirements

1. Merge any unique root-level content INTO wiki/ (don't lose information)
2. Remove root-level content ghost folders
3. Move wiki-specific config (schema, templates, artifact-types, etc.) into wiki/
4. Root should look like a normal project: tools, docs, raw, scripts — not content
5. Update all tool path references to match new locations
6. Validate everything works after the move
