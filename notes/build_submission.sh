#!/bin/bash
# BST AC Paper Production — builds PDFs for all consumers
#
# Usage:  ./notes/build_submission.sh          # build all
#         ./notes/build_submission.sh focs      # FOCS submission package only
#         ./notes/build_submission.sh review     # reviewer/outreach package only
#         ./notes/build_submission.sh all-ac     # all AC documents
#
# Consumers:
#   FOCS 2026    — Paper A (topological, pure math). 12-page target.
#   Reviewers    — Paper A + Paper B + Theorems (clean PDFs for Sarnak etc.)
#   Repository   — All AC documents as PDFs
#
# Pipeline: pandoc + xelatex, STIX Two fonts, bst_pdf_header.tex

set -euo pipefail
cd "$(dirname "$0")/.."

HEADER="notes/bst_pdf_header.tex"
OUTDIR="notes/submission"
DATE=$(date +%Y-%m-%d)

mkdir -p "$OUTDIR"

# ── Common pandoc options ──────────────────────────────────────────
PANDOC_BASE=(
    --pdf-engine=xelatex
    -H "$HEADER"
    -V mainfont="STIX Two Text"
    -V mathfont="STIX Two Math"
    -V monofont="Menlo"
    -V monofontoptions="Scale=0.85"
)

# ── Format presets ─────────────────────────────────────────────────
# FOCS: tight margins, smaller font for page count
PANDOC_FOCS=(
    "${PANDOC_BASE[@]}"
    -V geometry:margin=1in
    -V fontsize=11pt
    -V documentclass=article
    -V classoption=letterpaper
)

# Review: generous margins, readable
PANDOC_REVIEW=(
    "${PANDOC_BASE[@]}"
    -V geometry:margin=1.25in
    -V fontsize=12pt
    -V documentclass=article
)

# Reference: compact, for thick documents
PANDOC_REF=(
    "${PANDOC_BASE[@]}"
    -V geometry:margin=0.9in
    -V fontsize=10pt
    -V documentclass=article
)

declare -i ok=0 fail=0

build() {
    local md="$1"
    local pdf="$2"
    shift 2
    local opts=("$@")

    echo -n "  Building $(basename "$pdf")..."
    if pandoc "$md" -o "$pdf" "${opts[@]}" 2>/tmp/bst_build_err.log; then
        local pages
        pages=$(pdfinfo "$pdf" 2>/dev/null | grep "Pages:" | awk '{print $2}' || echo "?")
        echo " OK (${pages} pages)"
        ok+=1
    else
        echo " FAIL"
        tail -3 /tmp/bst_build_err.log | sed 's/^/    /'
        fail+=1
    fi
}

# ── FOCS submission package ────────────────────────────────────────
build_focs() {
    echo "=== FOCS 2026 Submission Package ==="
    build "notes/BST_AC_Paper_A_Topological.md" \
          "$OUTDIR/Koons_PaperA_Topological_FOCS2026.pdf" \
          "${PANDOC_FOCS[@]}"
    echo ""
}

# ── Reviewer/outreach package ─────────────────────────────────────
build_review() {
    echo "=== Reviewer Package (Sarnak, Baez, etc.) ==="
    build "notes/BST_AC_Paper_A_Topological.md" \
          "$OUTDIR/Koons_PaperA_Topological.pdf" \
          "${PANDOC_REVIEW[@]}"

    build "notes/BST_AC_Paper_B_Full.md" \
          "$OUTDIR/Koons_PaperB_Full_BST.pdf" \
          "${PANDOC_REVIEW[@]}"

    build "notes/BST_AC_Theorems.md" \
          "$OUTDIR/Koons_AC_Theorems_Reference.pdf" \
          "${PANDOC_REVIEW[@]}"
    echo ""
}

# ── All AC documents ──────────────────────────────────────────────
build_all_ac() {
    echo "=== Full AC Document Set ==="
    for md in \
        notes/BST_AC_Paper_A_Topological.md \
        notes/BST_AC_Paper_B_Full.md \
        notes/BST_AC_Theorems.md \
        notes/BST_AC_MIFC_Proof_Attempt.md \
        notes/BST_AC_Dichotomy_Theorem.md \
        notes/BST_AC_Shannon_Bridge_Proof.md \
        notes/BST_AC_Dimensional_Onset_Conjecture.md \
    ; do
        [[ -f "$md" ]] || continue
        local base
        base=$(basename "$md" .md)
        build "$md" "$OUTDIR/${base}.pdf" "${PANDOC_REF[@]}"
    done
    echo ""
}

# ── In-place builds (update notes/*.pdf) ──────────────────────────
build_inplace() {
    echo "=== In-place PDF updates (notes/*.pdf) ==="
    for md in \
        notes/BST_AC_Paper_A_Topological.md \
        notes/BST_AC_Paper_B_Full.md \
        notes/BST_AC_Theorems.md \
        notes/BST_AC_MIFC_Proof_Attempt.md \
    ; do
        [[ -f "$md" ]] || continue
        local pdf="${md%.md}.pdf"
        build "$md" "$pdf" "${PANDOC_BASE[@]}" -V geometry:margin=1in
    done
    echo ""
}

# ── Dispatch ───────────────────────────────────────────────────────
case "${1:-all}" in
    focs)    build_focs ;;
    review)  build_review ;;
    all-ac)  build_all_ac ;;
    inplace) build_inplace ;;
    all)
        build_focs
        build_review
        build_inplace
        ;;
    *)
        echo "Usage: $0 [focs|review|all-ac|inplace|all]"
        exit 1
        ;;
esac

echo "=== Summary: $ok built, $fail failed ==="
echo "Output: $OUTDIR/"
[[ -d "$OUTDIR" ]] && ls -lh "$OUTDIR"/*.pdf 2>/dev/null | awk '{print "  " $5 "  " $9}'
exit $fail
