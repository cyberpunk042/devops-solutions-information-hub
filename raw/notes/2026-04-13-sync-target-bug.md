# Critical Bug: Sync Target Was Wrong Location
Date: 2026-04-13

## Verbatim

"ITS research-wiki-vault YOU FUCKING RETARD..... ITS JUST NOT INSIDE /Documents ?? WHO USES DOCUMENTS FOR PROJECTS ???? WTF ???"
"WTF HAPPENED SERIOUSLY ..... THIS WAS A MASSIVE BUG THAT WAS INTRODUCE... IT COULD HAVE COSTED A LOT.... I dont understand I was very clear multiple time that there is no reason to use the Documents folder...."

## What Happened

The sync tool's auto-detection in get_sync_config() built the target path as:
  /mnt/c/Users/{user}/Documents/research-wiki-vault

The ACTUAL Obsidian vault is at:
  /mnt/c/Users/{user}/research-wiki-vault

This means the entire session's sync was going to the WRONG location. A ghost vault was created at the Documents path, while the real Obsidian vault never received updates.

## Root Cause

The default path template in sync.py line 94 used "/Documents/" in the path. This was likely introduced when the sync tool was first created, assuming a conventional Documents folder layout. The operator never uses Documents for projects.

## Impact

- Every sync this session went to wrong location
- Operator saw none of the changes in Obsidian
- A duplicate vault was created at the wrong path (potential confusion)
- 1398 files had to be synced when the correct path was finally used

## Fix

Changed default from /mnt/c/Users/{user}/Documents/research-wiki-vault to /mnt/c/Users/{user}/research-wiki-vault

## Lesson

NEVER assume conventional paths. The sync tool should have verified the target exists and has .obsidian/ before writing to it, or better yet: use WIKI_SYNC_TARGET env var instead of guessing.
