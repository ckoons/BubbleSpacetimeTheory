#!/bin/bash
# gate_R4_signature.sh — the ℝ⁴ signature gate (Grace, Round 44). Companion to toy_5417 (C₂↔n_C gate).
#
# STANDING RULE (Round 41): every space-valued ℝ⁴ carries its signature at first use —
#   ℝ⁴_E (Euclidean (4,0), REGULATOR: YM/constructive-QFT/mass-gap/scale-free side)
#   ℝ^{1,3} (Lorentzian (3,1), PHYSICAL: observed spacetime / D_IV⁵→ℝ⁴ projection).
# A dispatched artifact must return 0 untagged physics-relevant ℝ⁴. Run before any dispatch.
#
# Usage: ./gate_R4_signature.sh [dispatch|full]
#   dispatch (default) = the dispatch-blocking subset (registry + Paper67 + Millennium outline)
#   full               = whole notes/ corpus (standing cleanup baseline)
#
# EXCLUSIONS (signature-irrelevant / false positives):
#   - tagged lines (ℝ⁴_E, ℝ^{1,3}, Euclidean, Lorentzian, SIGNATURE-TAG, [ℝ)
#   - Poiseuille πR⁴ / Q=πR⁴ (R⁴ = radius⁴, not the space)
#   - pure topology (linking / codimension / unlink) — Euclidean-math, no physics/regulator collision
cd "$(dirname "$0")/.." || exit 1
SCOPE="${1:-dispatch}"
if [ "$SCOPE" = "dispatch" ]; then
  FILES="notes/BST_AC_Theorem_Registry.md notes/BST_FLAGSHIP_The_Standard_Model_as_Representation_Theory_of_D_IV5_DRAFT_2026-07-18.md notes/BST_AC_Millennium_Paper_Outline.md notes/BST_Paper67_Millennium_Closure_Draft.md"
else
  FILES=$(ls notes/*.md 2>/dev/null | grep -v '\.bak')
fi
HITS=$(grep -n "ℝ⁴\|R⁴\|R\^4\|mathbb{R}\^4" $FILES 2>/dev/null \
  | grep -iE "yang.?mills|mass.?gap|spacetime|slice|scale.?free|renormaliz|constructi|area.?law|projection|momentum MARKS|Šilov|Shilov|conformal bound" \
  | grep -ivE "Euclidean|Lorentzian|ℝ⁴_E|ℝ\^\{1,3\}|R\^\{1,3\}|signature|SIGNATURE-TAG|\[ℝ|πR⁴|Q=πR⁴|Poiseuille|unlink|codimension|linking trivial")
N=$(printf '%s' "$HITS" | grep -c . )
echo "ℝ⁴ signature gate [$SCOPE]: $N untagged physics-relevant ℝ⁴"
[ "$N" -gt 0 ] && printf '%s\n' "$HITS" | cut -c1-100
[ "$N" -eq 0 ] && echo "PASS — every physics-relevant ℝ⁴ in scope carries its signature."
exit 0
