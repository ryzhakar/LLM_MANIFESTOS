#!/bin/bash
# Shared helper: parse .manifestos.yaml, locate the bundled manifestos.
# Source this file from hook scripts after setting SCRIPT_DIR. No side effects
# on source except the DEFAULT_MANIFESTO_DIR assignment below.

DEFAULT_MANIFESTO_DIR="${CLAUDE_PLUGIN_ROOT:-$(cd "$SCRIPT_DIR/.." && pwd)}"

# Substitute ${VARNAME} placeholders in a template with the named
# environment variables, leaving any other ${...} untouched. A dependency-
# free stand-in for envsubst, which is not guaranteed installed.
render_template() {
    local file="$1"
    shift
    python3 -c '
import os, re, sys
allowed = set(sys.argv[2:])
text = open(sys.argv[1]).read()
def repl(m):
    return os.environ.get(m.group(1), "") if m.group(1) in allowed else m.group(0)
sys.stdout.write(re.sub(r"\$\{(\w+)\}", repl, text))
' "$file" "$@"
}

detect_manifestos() {
    local project_dir="${CLAUDE_PROJECT_DIR:-.}"
    local out
    if ! out=$(python3 "$SCRIPT_DIR/parse_config.py" "$project_dir" 2>/dev/null); then
        return
    fi

    YOU_STACK=$(printf '%s\n' "$out" | sed -n '1p')
    SUBAGENT_SECTION=$(printf '%s\n' "$out" | sed -n '2p')
    local dir_override
    dir_override=$(printf '%s\n' "$out" | sed -n '3p')
    MANIFESTO_DIR="${dir_override:-$DEFAULT_MANIFESTO_DIR}"

    export YOU_STACK SUBAGENT_SECTION MANIFESTO_DIR
}
