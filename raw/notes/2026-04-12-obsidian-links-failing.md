# Operator Directive: Obsidian Links Failing
Date: 2026-04-12

## Verbatim

"do you think you are done ??? we have almost progress.. I the first three link I tried failed..."
"Almost all of them are failing... all over the place... less than 15% are working... I already told you what I was expecting for all this, do I need to repeat myself ?"

## What This Means

The wikilink fix approach was WRONG. Renaming titles doesn't fix Obsidian resolution because Obsidian resolves wikilinks by FILENAME, not by title. Every [[Title]] wikilink needs either:
1. A matching filename (we use kebab-case, so titles don't match filenames)
2. An alias in frontmatter that matches what the wikilink says
3. Or the wikilinks themselves need to use filenames instead of titles

The operator already told us: "Every empty links / links that lead to creating a new page in obsidian should be filled." Less than 15% working means the fundamental resolution mechanism is broken.
