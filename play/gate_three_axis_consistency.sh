#!/bin/bash
# gate_three_axis_consistency.sh — the permanent pre-dispatch consistency gate (Grace+Elie, 2026-08-22).
# Companion to toy_5417 (C₂↔n_C) and gate_R4_signature.sh.
#
# DESIGN (honest): a pure-grep gate CANNOT do the READ step, so it is a DELTA-DETECTOR, not a
# claim-counter. "A count between grep and READ is a candidate count in disguise." So:
#   - it prints the CANDIDATE SURFACE (grep), tightened to the crossing/elimination/forcing SHAPE;
#   - it fires the POSITIVE CONTROLS (the known crossings must re-appear, proving it works);
#   - it HASHES the candidate surface and compares to the READ-CONFIRMED BASELINE below.
# CLEAN  = positive controls fire AND hash == baseline (no NEW candidate entered since the last full
#          READ pass — grace_three_axis_exhaustive_sweep_readout_2026-08-22.md, which confirmed
#          A=2 / B=1 / C=4, all tracked). The hashed clean run is the dispatch artifact Keeper gates.
# CHANGED = hash != baseline → a candidate entered/left; READ the delta before dispatch.
#
# Three hygiene features (this round): (1) SELF-EXCLUSION of the sweep's own declaration files;
# (2) POSITIVE-CONTROL label (known crossings are the control, not "N problems"); (3) HASH the run.
cd "$(dirname "$0")/.." || exit 1

# READ-CONFIRMED BASELINE (set from the clean run after the Round-47 READ pass). Update ONLY after a
# new full READ pass re-confirms the surface. Empty on first run → prints the current hash to adopt.
# Baseline = T-ID-set hash as of the Round-47/48 READ pass (confirmed claims A=2/B=1/C=4, all tracked;
# remaining IDs READ as non-crossing-shape). A NEW theorem-ID entering the crossing surface changes
# this hash → READ the delta. Update ONLY after a fresh READ pass re-confirms the surface.
BASELINE="ed3e032f3e677fb36b1e3fd96d9610eda938d8f7335214e9dedf3fb539565b50"

SELF='grace_forbiddance_collision_sweep|grace_elimination_scope_shed|grace_three_axis|_sweep_gate_|_sweep_readout|WITHDRAWN_claims_registry|signature_sweep_C2_nC_collision_correction'
FILES=$(ls notes/*.md 2>/dev/null | grep -v '\.bak' | grep -ivE "$SELF")

# TIGHT SHAPES (match the crossing/elimination/forcing form, not any keyword co-occurrence):
#  A: SU(3)/color CONFINEMENT claimed derived/forced from geometry (the T2523 shape)
A_ALL=$(grep -rn "SU(3)\|colou\?r" $FILES 2>/dev/null \
  | grep -iE "confin" | grep -iE "derive[ds]?|forced|from the geometr|geometr.*confin" \
  | grep -ivE "imported|NOT |re-scoped|withdrawn|two-row|\(A1\)|dynamics is imported|does not|topological stability")
#  B: STRUCTURAL elimination of a load-bearing object (drop/retire Γ/regulator/premise), benign excluded
B_ALL=$(grep -rn "drop Γ\| Γ dropped\|drop the Γ\|retire.*regulator\|regulator.*not needed\|premise.*dropped" $FILES 2>/dev/null \
  | grep -ivE "arithmetic|not dropped|demote|regulator, not")
#  C: geometry FORCES a named contingent fact (the pentadactyly shape)
C_ALL=$(grep -rn "force[ds]" $FILES 2>/dev/null \
  | grep -iE "pentadactyl|finger|digit|\b11.organ\b|organ architecture|endotherm|germ layer|genetic code.*forc|body plan.*forc" \
  | grep -ivE "contingen|null-model|more than chance|not forced|small-integer|appears more")

# POSITIVE CONTROLS: the known crossings MUST appear somewhere in the corpus (as re-scoped rows).
PC_A=$(grep -rlE "T2523|T2526" notes/BST_AC_Theorem_Registry.md 2>/dev/null | wc -l | tr -d ' ')
PC_C=$(grep -rlE "T379|pentadactyl" notes/*.md 2>/dev/null | grep -ivE "$SELF" | wc -l | tr -d ' ')

echo "=============================================================="
echo " THREE-AXIS CONSISTENCY GATE (delta-detector; self-excluded)"
echo "=============================================================="
nA=$(printf '%s\n' "$A_ALL" | grep -c .); nB=$(printf '%s\n' "$B_ALL" | grep -c .); nC=$(printf '%s\n' "$C_ALL" | grep -c .)
echo " AXIS A (SU(3)/color-confinement derived-from-geometry) candidate lines: $nA"
[ "$nA" -gt 0 ] && printf '%s\n' "$A_ALL" | grep -oE "[^/]+:[0-9]+" | head -6 | sed 's/^/     /'
echo " AXIS B (structural elimination of a load-bearing object) candidate lines: $nB"
[ "$nB" -gt 0 ] && printf '%s\n' "$B_ALL" | grep -oE "[^/]+:[0-9]+" | head -6 | sed 's/^/     /'
echo " AXIS C (geometry-forces-a-named-contingent-fact) candidate lines: $nC"
[ "$nC" -gt 0 ] && printf '%s\n' "$C_ALL" | grep -oE "[^/]+:[0-9]+" | head -6 | sed 's/^/     /'
echo ""
echo " POSITIVE CONTROLS (instrument works iff these fire):"
echo "   A: T2523/T2526 present in registry (re-scoped) : $([ "$PC_A" -ge 1 ] && echo FIRES || echo BROKEN)"
echo "   C: T379/pentadactyl present in corpus          : $([ "$PC_C" -ge 1 ] && echo FIRES || echo BROKEN)"
echo ""
echo " CANDIDATE SURFACE = $((nA+nB+nC)) lines (grep). These REQUIRE a READ pass to become claims —"
echo " the READ-confirmed finding set is A=2 / B=1 / C=4 (all tracked), per the exhaustive readout."

# Hash the SORTED SET OF THEOREM-IDs on the crossing surface (robust to prose edits; sensitive to a
# NEW theorem entering the crossing/forcing shape — the real regression signal).
IDSET=$( printf '%s\n' "$A_ALL$B_ALL$C_ALL" | grep -oE "T[0-9]+" | sort -u | tr '\n' ',' )
RUNHASH=$( printf '%s' "$IDSET" | shasum -a 256 2>/dev/null | cut -d' ' -f1 )
NIDS=$( printf '%s' "$IDSET" | tr ',' '\n' | grep -c . )
echo "--------------------------------------------------------------"
echo " CROSSING-SURFACE T-ID SET: $NIDS distinct theorem-IDs"
echo " T-ID-SET HASH: $RUNHASH"
if [ -z "$BASELINE" ]; then
  echo " (no baseline set — adopt this hash as BASELINE after a READ pass confirms the surface.)"
elif [ "$RUNHASH" = "$BASELINE" ]; then
  echo " GATE: CLEAN — hash == READ-confirmed baseline; no new candidate entered. Dispatch artifact."
else
  echo " GATE: CHANGED — hash != baseline; a candidate entered/left. READ the delta before dispatch."
fi
exit 0
