#!/bin/bash
# BST PDF builder — converts markdown notes to PDF via pandoc + xelatex
#
# Usage:  ./notes/build_pdfs.sh [file1.md file2.md ...]
#         ./notes/build_pdfs.sh              # builds all .md in notes/
#
# Fonts: STIX Two (text + math) via pandoc variables, Menlo for code.
# Unicode: bst_pdf_header.tex maps ~170 bare Unicode chars to LaTeX.
#
# IMPORTANT: Do NOT load unicode-math or amsmath/amssymb in the header.
# Pandoc's xelatex template already loads them. Double-loading breaks
# display math (\sum, \prod, etc.).

set -euo pipefail
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

ok=0 fail=0 skip=0

build_one() {
    local md="$1"
    local pdf="${md%.md}.pdf"

    # Skip files that are just indexes or too short
    if [[ "$(wc -l < "$md")" -lt 5 ]]; then
        ((skip++))
        return
    fi

    if pandoc "$md" -o "$pdf" "${PANDOC_OPTS[@]}" 2>/tmp/bst_pdf_err.log; then
        local warnings
        warnings=$(grep -c "WARNING\|Missing character" /tmp/bst_pdf_err.log 2>/dev/null || true)
        if [[ "$warnings" -gt 0 ]]; then
            echo "  WARN  $md ($warnings warnings)"
        else
            echo "  OK    $md"
        fi
        ((ok++))
    else
        echo "  FAIL  $md"
        tail -3 /tmp/bst_pdf_err.log | sed 's/^/        /'
        ((fail++))
    fi
}

if [[ $# -gt 0 ]]; then
    # Build specific files
    for f in "$@"; do
        build_one "$f"
    done
else
    # Build all .md files in notes/ (not subdirs by default)
    for f in notes/*.md; do
        [[ -f "$f" ]] || continue
        build_one "$f"
    done
fi

echo ""
echo "Done: $ok ok, $fail failed, $skip skipped"
exit $fail
