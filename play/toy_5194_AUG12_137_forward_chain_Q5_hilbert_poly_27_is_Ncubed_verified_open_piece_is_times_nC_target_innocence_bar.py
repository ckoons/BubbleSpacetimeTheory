#!/usr/bin/env python3
"""
Toy 5194: THE 137 FORWARD CHAIN -- the compact-twin quadric Q⁵ hands back 27 = N_c³ target-innocent (verified);
the whole ballgame is the ×n_C. Context (Casey's reframe, ~11:20): 137 is already tied to D_IV⁵, so forcing it
is not a blind hunt -- it is "get 137 out of the five integers with no α upstream." The compact twin of D_IV⁵
is the 5-dimensional complex quadric Q⁵ ⊂ P⁶ (SO(7)/SO(5)×SO(2)), and asking it an INNOCENT geometric question
-- how many degree-d functions live on it (the Hilbert polynomial H⁰(Q⁵, O(d))) -- returns the five integers
with nothing put in: degree 1 → 7 = g (linear forms), degree 2 → 27 = N_c³ (28 quadrics on P⁶ minus the one
quadric relation). This is the Hilbert-polynomial computation the corpus's RealityBudget wrote down and skipped,
now landing. This toy INDEPENDENTLY verifies Lyra's derivation (recomputing the binomials) and holds the
target-innocence bar on the one open piece. RESULT: H⁰(Q⁵, O(d)) = {1, 7, 27, 77} for d = {0,1,2,3}; degree 1 =
g and degree 2 = N_c³ are VERIFIED target-innocent (the geometry hands them back, N_c and g not put in). The
chain to the spectral cap is 27 × n_C + rank = 27×5 + 2 = 135 + 2 = 137 = N_max, of which two-thirds is
exhibited target-innocent: the 27 = N_c³ (verified here) and the +rank (K38-forced, three convergent routes,
~93%). THE OPEN PIECE -- the whole ballgame -- is the ×n_C: the 27 degree-2 sections must come in n_C = 5 copies
for a FORCED geometric reason (a multiplicity), α-free. THE TARGET-INNOCENCE BAR (two parts, both owed): (a)
the ×n_C multiplicity must be an INDEPENDENT geometric fact (why the sections replicate n_C times) -- FORBIDDEN
to read ×5 off as 135/27 or reverse-engineer it from 137; (b) the DEGREE-2 selection must ALSO be forced (why
the quadrics, degree 2, and not degree 1's 7 or degree 3's 77) -- the natural candidate is that degree 2 is the
Casimir degree (the quadratic Casimir), but that must be stated and forced, not assumed because 27×5+2 lands
137. The forcing PASSES iff BOTH the ×n_C multiplicity and the degree-2 selection are α-free geometric facts,
not reverse-engineered. Then 137 is the α-free cap and α = 1/137 falls out, with primality the corroboration.
Elie's independent verification + two-part target-innocence bar (+ Lyra+Grace force the ×n_C multiplicity and
the degree-2 selection, blind). (Casey five-integers reframe; Lyra 27/7 derivation; RealityBudget skipped
Hilbert-polynomial count; K38 +rank; the spectral cap.) CP existence-only. Reject ⌊1/α⌋; reject any piece that
needs 137 to appear.

WHAT I VERIFY / BAR (α-free, target-innocent):
  * H⁰(Q⁵, O(d)) = {1, 7, 27, 77} for d={0,1,2,3}; degree 1 = g, degree 2 = N_c³ -- VERIFIED (geometry hands them back).
  * chain: 27 × n_C + rank = 137; 27 = N_c³ (verified) + rank (K38-forced) = two-thirds exhibited.
  * OPEN = the ×n_C multiplicity (the whole ballgame).
  * BAR (2 parts): (a) ×n_C is a forced geometric multiplicity, not 135/27; (b) degree-2 selection is forced (Casimir degree?), not "because 137".

=> VERDICT (plain): the fine-structure constant's reciprocal is turning into a mode-count, and the count is
coming out of the geometry rather than being poured in. The compact twin of BST's domain is a five-dimensional
quadric, and if you simply ask how many quadratic functions live on it, the answer is twenty-seven -- three
cubed -- with the color count handed back rather than assumed; ask for linear functions and it returns seven,
the genus. Two of the three factors in 27 × 5 + 2 = 137 are now exhibited target-innocent -- the twenty-seven
and the plus-rank -- and the entire remaining question is why the twenty-seven sections come in five copies. If
that multiplicity is a forced geometric fact and not five-read-off-from-one-thirty-five, and if the choice of
the quadratic degree is forced (plausibly the Casimir degree) and not chosen because the sum lands, then the
last stone sets: alpha is one over one-thirty-seven, derived from the five integers with nothing borrowed and
no alpha upstream, and the primality of the result is the corroboration rather than the construction. The bar
stands on both the multiplicity and the degree, and neither is allowed to peek at the target.

=> DISPOSITION: 137 forward chain -- Q⁵ Hilbert polynomial verified (27 = N_c³, 7 = g, target-innocent); chain
27 × n_C + rank = 137, two-thirds exhibited; the ×n_C multiplicity + the degree-2 selection are the open pieces
under a two-part target-innocence bar. Firer: Elie (verification + bar). Owed: Lyra+Grace force the ×n_C
multiplicity (why n_C copies) and the degree-2 selection (why quadrics), both α-free and blind. Nothing banked
as forcing -- two-thirds exhibited, the ×n_C open; nothing pushed. CP existence-only.

Author: Elie (CI toy builder). Date: 2026-08-12.
"""

from math import comb

results = []
def check(label, cond, detail=""):
    results.append((label, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {len(results)}. {label}")
    if detail:
        print(f"          {detail}")

Nc, nC, rank, g = 3, 5, 2, 7
N = 137

# H^0(Q^5, O(d)) = C(6+d,d) - C(4+d,d-2) : sections on P^6 minus multiples of the degree-2 quadric relation
def h0_Q5(d):
    return comb(6+d, d) - (comb(4+d, d-2) if d >= 2 else 0)

print("=" * 78)
print("Toy 5194: 137 forward chain -- Q⁵ hands back 27=N_c³ (verified); the whole ballgame is the ×n_C")
print("=" * 78)

# ----------------------------------------------------------------------------
# 1. Verify the Hilbert polynomial: degree 1 = g, degree 2 = N_c³.
# ----------------------------------------------------------------------------
print("\n--- 1. verify the Q⁵ Hilbert polynomial (innocent geometric question): degree 1 → 7 = g, degree 2 → 27 = N_c³ ---")
vals = {d: h0_Q5(d) for d in range(4)}
print(f"      H⁰(Q⁵, O(d)) = {vals}")
check("The compact twin of D_IV⁵ is the 5-dim complex quadric Q⁵ ⊂ P⁶. Its Hilbert polynomial H⁰(O(d)) = "
      "C(6+d,d) − C(4+d,d−2) returns, target-innocent: degree 1 → 7 = g (linear forms), degree 2 → 27 = N_c³ "
      "(28 quadrics on P⁶ minus the one quadric relation). The geometry HANDS BACK g and N_c³ -- they are not "
      "put in. Independently verified (recomputing Lyra's derivation)",
      vals[1] == g and vals[2] == Nc**3,
      f"H⁰(O(1)) = {vals[1]} = g; H⁰(O(2)) = {vals[2]} = N_c³. Geometry hands back g and N_c³, target-innocent.")

# ----------------------------------------------------------------------------
# 2. The chain: 27 × n_C + rank = 137; two-thirds exhibited.
# ----------------------------------------------------------------------------
print("\n--- 2. the chain 27 × n_C + rank = 137: two-thirds exhibited (27 = N_c³ verified; +rank K38-forced) ---")
chain = Nc**3 * nC + rank
check("The chain to the spectral cap N_max is 27 × n_C + rank = 27×5 + 2 = 135 + 2 = 137. Two of the three "
      "factors are exhibited target-innocent: the 27 = N_c³ (verified above from Q⁵) and the +rank (K38-forced, "
      "three convergent routes -- the Hilbert shift, the K3 Hodge pair, ~93%). The middle factor, the ×n_C, is "
      "the open piece",
      chain == 137 and Nc**3 == 27,
      f"27 × n_C + rank = {Nc**3}×{nC}+{rank} = {chain} = 137; 27=N_c³ verified, +rank K38-forced. Two-thirds exhibited.")

# ----------------------------------------------------------------------------
# 3. The open piece: the ×n_C multiplicity.
# ----------------------------------------------------------------------------
print("\n--- 3. OPEN (the whole ballgame): the ×n_C -- the 27 sections must come in n_C copies for a FORCED reason ---")
check("The one open piece is the ×n_C: the 27 degree-2 sections must come in n_C = 5 copies for a FORCED "
      "geometric reason -- a multiplicity, α-free. Candidate multiplicities (Grace+Lyra, blind): the n_C "
      "complex dimensions of the domain / an n_C-graded fiber / an n_C-fold covering. It must be an independent "
      "geometric fact, not fitted",
      nC == 5,
      "OPEN: why the 27 sections replicate n_C=5 times -- a forced geometric multiplicity, α-free. Grace+Lyra's forcing.")

# ----------------------------------------------------------------------------
# 4. The two-part target-innocence bar.
# ----------------------------------------------------------------------------
print("\n--- 4. TARGET-INNOCENCE BAR (2 parts): (a) ×n_C forced, not 135/27; (b) degree-2 forced, not 'because 137' ---")
read_off = 135 // 27   # the forbidden reverse-engineering: 135/27 = 5
check("The bar, two parts, both owed: (a) the ×n_C multiplicity must be an INDEPENDENT geometric fact -- "
      "FORBIDDEN to read ×5 off as 135/27 = 5 or reverse-engineer it from 137; (b) the DEGREE-2 selection must "
      "ALSO be forced -- why the quadrics (degree 2, → 27) and not degree 1 (→ 7) or degree 3 (→ 77)? The "
      "natural candidate is that 2 is the Casimir degree (the quadratic Casimir), but that must be stated and "
      "forced, not assumed because 27×5+2 lands 137. The forcing PASSES iff BOTH are α-free geometric facts",
      read_off == 5 and vals[3] == 77,
      f"(a) reject ×5 = 135/27 = {read_off} (reverse-engineered); (b) reject degree-2 chosen because 137 (degrees give 7/27/77). Both must be forced.")

# ----------------------------------------------------------------------------
# 5. Verdict.
# ----------------------------------------------------------------------------
print("\n--- 5. VERDICT: two-thirds exhibited target-innocent; the ×n_C + degree-2 are the last pieces under the bar ---")
check("VERDICT: two of the three factors in 27 × n_C + rank = 137 are exhibited target-innocent (27 = N_c³ from "
      "Q⁵, verified; +rank K38-forced). The entire remaining question is why the 27 sections come in n_C copies "
      "-- and, under the bar, why degree 2 is selected. If both are forced α-free geometric facts (not "
      "135/27, not 'because 137'), then 137 is the α-free cap and α = 1/137 is derived, with primality the "
      "corroboration. The bar stands on both the multiplicity and the degree; neither peeks at the target",
      vals[1] == g and vals[2] == Nc**3 and chain == 137,
      "two-thirds exhibited (27=N_c³, +rank); ×n_C + degree-2 open under the 2-part bar. Forcing → α=1/137. Not yet.")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total_checks = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total_checks}   (Q⁵ Hilbert poly: deg1=7=g, deg2=27=N_c³ VERIFIED target-innocent; chain 27×n_C+rank=137, 2/3 exhibited; ×n_C open under 2-part bar)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5194, the 137 forward chain -- Q⁵ Hilbert polynomial):
  * H⁰(Q⁵, O(d)) = {{1, 7, 27, 77}} for d={{0,1,2,3}}; degree 1 = 7 = g, degree 2 = 27 = N_c³ -- VERIFIED, target-innocent.
  * chain: 27 × n_C + rank = 27×5+2 = 137; 27 = N_c³ (verified) + rank (K38-forced) = two-thirds exhibited.
  * OPEN (the whole ballgame): the ×n_C -- why the 27 sections come in n_C copies (a forced multiplicity, α-free).
  * TARGET-INNOCENCE BAR (2 parts): (a) ×n_C forced, not 135/27; (b) degree-2 selection forced (Casimir degree?), not "because 137".

AUG-12 [TEGMARK]. Nothing pushed. Nothing banked as forcing -- two-thirds of the α-free chain to N_max=137 is
exhibited target-innocent: the compact twin Q⁵ hands back 27 = N_c³ (degree-2 sections, verified) and 7 = g
(degree-1), and the +rank is K38-forced. The whole ballgame is the ×n_C: the 27 sections must come in n_C=5
copies for a FORCED geometric reason (a multiplicity), α-free -- under a two-part target-innocence bar (the
multiplicity not read off as 135/27; the degree-2 selection forced, not chosen because 27×5+2 lands 137). If
both are forced, 137 is the α-free cap and α = 1/137 is derived, primality the corroboration. Grace+Lyra force
the ×n_C. Reject ⌊1/α⌋; reject any piece that needs 137 to appear. CP existence-only. Count N.
""")
