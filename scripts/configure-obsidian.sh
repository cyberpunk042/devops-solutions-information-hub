#!/usr/bin/env bash
# Configure Obsidian vault settings in wiki/.obsidian/
source "$(dirname "$0")/lib.sh"

OBSIDIAN_DIR="${WIKI_DIR}/.obsidian"

log_info "=== Configuring Obsidian vault ==="

mkdir -p "$OBSIDIAN_DIR"

# app.json
cat > "${OBSIDIAN_DIR}/app.json" << 'EOF'
{
  "vimMode": false,
  "strictLineBreaks": true,
  "showFrontmatter": true,
  "foldHeading": true,
  "foldIndent": true,
  "defaultViewMode": "preview"
}
EOF
log_info "Created app.json"

# appearance.json
cat > "${OBSIDIAN_DIR}/appearance.json" << 'EOF'
{
  "theme": "obsidian",
  "translucency": false,
  "baseFontSize": 16
}
EOF
log_info "Created appearance.json"

# core-plugins.json
cat > "${OBSIDIAN_DIR}/core-plugins.json" << 'EOF'
[
  "graph",
  "backlink",
  "tag-pane",
  "outgoing-links",
  "search",
  "file-explorer",
  "page-preview"
]
EOF
log_info "Created core-plugins.json"

# graph.json
cat > "${OBSIDIAN_DIR}/graph.json" << 'EOF'
{
  "collapse-filter": false,
  "search": "",
  "showTags": false,
  "showAttachments": false,
  "hideUnresolved": false,
  "showOrphans": true,
  "collapse-color-groups": false,
  "colorGroups": [
    {"query": "path:domains/ai-agents", "color": {"a": 1, "rgb": 4886754}},
    {"query": "path:domains/knowledge-systems", "color": {"a": 1, "rgb": 2470655}},
    {"query": "path:domains/automation", "color": {"a": 1, "rgb": 16750848}},
    {"query": "path:domains/tools-and-platforms", "color": {"a": 1, "rgb": 8388352}},
    {"query": "path:sources", "color": {"a": 1, "rgb": 10066329}}
  ],
  "collapse-display": false,
  "lineSizeMultiplier": 1,
  "nodeSizeMultiplier": 1,
  "textFadeMultiplier": 0,
  "centerStrength": 0.5,
  "repelStrength": 10,
  "linkStrength": 1,
  "linkDistance": 250
}
EOF
log_info "Created graph.json with domain color groups"

# Generate wikilinks
log_info "Generating Obsidian wikilinks..."
cd "$PROJECT_ROOT"
python3 -m tools.manifest
python3 -m tools.obsidian
log_info "Wikilinks generated"

log_info "=== Obsidian vault configured at ${WIKI_DIR} ==="
log_info "Open Obsidian → Open folder as vault → select: ${WIKI_DIR}"
