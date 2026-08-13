#!/bin/bash
# Keeper's incremental PDF builder — rebuilds PDFs ONLY for new/modified .md files.
# Owner: Keeper. Intended to become part of the EOD process once verified.
#
# "Modified" = the sibling .pdf is missing OR older than the .md (mtime).
# Uses the SAME pandoc invocation as notes/build_pdfs.sh so the styling is identical.
#
# Usage:
#   ./notes/build_modified_pdfs.sh                 # curated dirs (Curriculum Working_Paper), stale only
#   ./notes/build_modified_pdfs.sh --dry-run       # list what WOULD build; build nothing
#   ./notes/build_modified_pdfs.sh --all           # every content dir (Curriculum Working_Paper notes data)
#   ./notes/build_modified_pdfs.sh --dir <dir>     # scan one specific directory (recursive)
#   ./notes/build_modified_pdfs.sh a.md b.md       # explicit files (forced, ignores mtime)
#
# NOT `set -e`: one file's failure must not abort the batch; ((x++)) returns 1 at 0.
set -uo pipefail
cd "$(dirname "$0")/.."

HEADER="notes/bst_pdf_header.tex"
PANDOC_OPTS=(
    --pdf-engine=xelatex
    -H "$HEADER"
    -V geometry:margin=1in
    -V mainfont="STIX Two Text"
    -V mathfont="STIX Two Math"
    -V monofont="Menlo"
    -V monofontoptions="Scale=0.85"
)

CURATED=(Curriculum Guide)
ALL=(Curriculum Guide notes data)

DRY_RUN=0
FILES=()
DIRS=()
MODE="curated"

while [[ $# -gt 0 ]]; do
    case "$1" in
        --dry-run) DRY_RUN=1; shift ;;
        --all)     MODE="all"; shift ;;
        --dir)     DIRS+=("$2"); MODE="dirs"; shift 2 ;;
        -h|--help) grep '^#' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
        *.md)      FILES+=("$1"); MODE="files"; shift ;;
        *)         echo "unknown arg: $1" >&2; exit 2 ;;
    esac
done

ok=0; fail=0; skip=0; uptodate=0

is_buildable() {   # skip indexes/stubs (<5 lines) and backup files
    local md="$1"
    [[ "$md" == *.bak* || "$md" == *~ ]] && return 1
    [[ "$(wc -l < "$md" 2>/dev/null || echo 0)" -lt 5 ]] && return 1
    return 0
}

needs_build() {    # true if .pdf missing or older than .md
    local md="$1"; local pdf="${md%.md}.pdf"
    [[ ! -f "$pdf" ]] && return 0
    [[ "$md" -nt "$pdf" ]] && return 0
    return 1
}

build_one() {
    local md="$1"; local pdf="${md%.md}.pdf"
    if ! is_buildable "$md"; then skip=$((skip+1)); return; fi
    if [[ $DRY_RUN -eq 1 ]]; then echo "  WOULD BUILD  $md"; ok=$((ok+1)); return; fi
    if pandoc "$md" -o "$pdf" "${PANDOC_OPTS[@]}" 2>/tmp/bst_pdf_err.log; then
        local w; w=$(grep -c "WARNING\|Missing character" /tmp/bst_pdf_err.log 2>/dev/null || true)
        if [[ "${w:-0}" -gt 0 ]]; then echo "  WARN  $md ($w warnings)"; else echo "  OK    $md"; fi
        ok=$((ok+1))
    else
        echo "  FAIL  $md"; tail -3 /tmp/bst_pdf_err.log | sed 's/^/        /'; fail=$((fail+1))
    fi
}

# --- collect the target .md list ---
targets=()
case "$MODE" in
    files)   targets=("${FILES[@]}") ;;                       # explicit = forced
    dirs)    for d in "${DIRS[@]}"; do while IFS= read -r f; do targets+=("$f"); done < <(find "$d" -name '*.md' 2>/dev/null); done ;;
    all)     for d in "${ALL[@]}";  do while IFS= read -r f; do targets+=("$f"); done < <(find "$d" -name '*.md' 2>/dev/null); done ;;
    curated) for d in "${CURATED[@]}"; do while IFS= read -r f; do targets+=("$f"); done < <(find "$d" -name '*.md' 2>/dev/null); done ;;
esac

echo "PDF sync — mode:$MODE  dry-run:$DRY_RUN  candidates:${#targets[@]}"
for md in "${targets[@]}"; do
    [[ -f "$md" ]] || continue
    if [[ "$MODE" == "files" ]]; then
        build_one "$md"                       # explicit files always build
    elif needs_build "$md"; then
        build_one "$md"
    else
        uptodate=$((uptodate+1))
    fi
done

echo ""
echo "Done: $ok built/would-build, $fail failed, $skip skipped(stub/bak), $uptodate already current"
exit $fail
