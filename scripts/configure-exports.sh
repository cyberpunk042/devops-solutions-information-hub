#!/usr/bin/env bash
# Configure export directories in sister projects.
source "$(dirname "$0")/lib.sh"

OPENFLEET_DIR="${PROJECT_ROOT}/../openfleet"
AICP_DIR="${PROJECT_ROOT}/../devops-expert-local-ai"

log_info "=== Configuring sister project exports ==="

# openfleet
if check_dir "$OPENFLEET_DIR" "openfleet"; then
    EXPORT_DIR="${OPENFLEET_DIR}/docs/knowledge-map/kb/research-wiki"
    mkdir -p "$EXPORT_DIR"
    log_info "openfleet export dir ready: $EXPORT_DIR"

    log_info "Dry-run openfleet export..."
    cd "$PROJECT_ROOT"
    python3 -m tools.export openfleet --dry
else
    log_warn "openfleet not found — skipping export configuration"
fi

echo ""

# AICP
if check_dir "$AICP_DIR" "AICP (devops-expert-local-ai)"; then
    EXPORT_DIR="${AICP_DIR}/docs/kb/research-wiki"
    mkdir -p "$EXPORT_DIR"
    log_info "AICP export dir ready: $EXPORT_DIR"

    log_info "Dry-run AICP export..."
    cd "$PROJECT_ROOT"
    python3 -m tools.export aicp --dry
else
    log_warn "AICP not found — skipping export configuration"
fi

log_info "=== Export configuration complete ==="
log_info "Run 'python3 tools/export.py openfleet' or 'python3 tools/export.py aicp' to export."
