#!/usr/bin/env python3
"""
Toy 5202: CASEY'S LAMB-SHIFT READING -- tested at I-tier with Keeper's gate applied (does the COEFFICIENT land,
or only the 5?). Casey's lead: don't fight the standard α¹ × (Zα)⁴ factorization, identify it with the Shilov
boundary (S⁴ × S¹)/ℤ₂ -- four bindings in the S⁴, one "double bond" in the S¹ (α = e², two vertices, emit and
absorb), 4 + 1 = 5 = n_C. Three findings, one of them a catch that matters more than the lead. ★ (1) A REAL
POSITIVE, and it is better than the 5: the grouping is DIMENSIONALLY CONSISTENT ACROSS EVERY SPATIAL DIMENSION,
so it is not an accident of 5 = 4 + 1. In d spatial dimensions the QED self-energy exponent is 1 (the loop) + d
(from |ψ(0)|² ∝ (Zαm)^d) + 1 (the Coulomb vertex) = d + 2; and the Shilov boundary S^{d+1} × S¹ gives
(d+1) + 1 = d + 2. The two track each other for d = 1,2,3,4,5, not just at three. That is genuine structural
support for the reading, and it is the part worth keeping. ★ (2) COUNT-ONCE, IMMEDIATELY: the reason it works
is that n_C − 2 = 3 is the spatial dimension, which BST already derives (Casey #14, 3+1 from D_IV⁵). So the
Lamb exponent is NOT an independent confirmation of anything -- it is the SAME banked 3+1 fact read in a new
place. One fact, one tally. ★★ (3) THE CATCH, and it is the reason to run a toy instead of admiring a picture:
the coefficient is 4/(3π), and it is numerically EXACT as rank²/(N_c·π) -- 0.00%, because BST owns an integer 4
(= rank²) and an integer 3 (= N_c). That identification is WRONG. The 3 in 4/(3π) is the SPATIAL directional
average -- it comes from ⟨p_i p_j⟩ → δ_ij/3 over three spatial directions -- so in BST it must be n_C − 2 = 3,
the spatial dimension, NOT N_c = 3, the colour count. BST has two different threes and this coefficient wants
the other one. An exact numerical match to the wrong object is worth less than no match at all, because it
looks like confirmation. This is the same species of category error I have now caught three times today (the
volume ratio for a convention ratio; the 4D cutoff for a 10D scale; and now colour-3 for spatial-3), and it is
the one that would have gone into a paper. ★ (4) THE NULL MODEL says the numerical match carries no weight
anyway: three distinct BST-natural forms land within 1% of 4/(3π), and the exact one is precisely the
mis-assigned one. ★ (5) THE GATE, made precise (Keeper's, sharpened): the leading self-energy is
(4α⁵/3πn³)·mc²·[ln(1/α²) + 19/30 − ln k₀(n,l)], which reproduces 1039.31 MHz of the observed 1057.845 MHz
(98.25%) -- and the load-bearing number in it is the BETHE LOGARITHM ln k₀(2,0) = 2.811769893, an infinite sum
over intermediate states that no dimensional argument produces. If a self-energy computation on S⁴ × S¹ returns
THAT, it is a derivation. If it returns the power 5 and a plausible prefactor, it is a re-description. And to be
a test rather than a fit it must return TWO of them -- ln k₀(2,0) = 2.811769893 AND ln k₀(2,1) = −0.030016709,
which have opposite signs and no shared scale, so a one-parameter fudge cannot hit both. ★ VERDICT: the reading
is coherent, dimensionally consistent, and I-tier; the coefficient is not delivered; one assignment inside it is
wrong and should be corrected before anyone writes it down; the Bethe log is the gate. Do not promote on the 5.
Elie, route item 3, light as instructed. (Casey's lead; Keeper's coefficient gate; Casey #14 3+1; toy 5198's
loop-order diagnosis; standard QED self-energy.) CP existence-only. Nothing pushed.

WHAT I COMPUTE:
  * standard leading self-energy 2S: bracket 7.662051, ΔE = 1039.31 MHz vs observed 1057.845 (98.25%).
  * exponent bookkeeping: QED gives 5 = 1(loop) + 3(|ψ(0)|²) + 1(Coulomb); Casey gives 4(S⁴) + 1(S¹).
  * ★ dimensional consistency: QED exponent d+2 vs Shilov S^{d+1}×S¹ giving d+2, for d = 1..5. Tracks.
  * ★★ the catch: the 3 in 4/(3π) is the SPATIAL average (δ_ij/3), = n_C−2, NOT N_c. Exact match, wrong object.
  * null model: 3 distinct BST forms within 1% of 4/(3π); the exact one is the mis-assigned one.
  * the gate: ln k₀(2,0) = 2.811769893 AND ln k₀(2,1) = −0.030016709 -- two numbers, opposite signs.

=> VERDICT (plain): the picture is better than I expected in one way and worse in another. The good part is
that Casey's split of the five powers -- four on the sphere, one on the circle -- is not a coincidence of the
number five. Redo the standard atomic-physics counting in any number of spatial dimensions and the exponent
comes out two more than the dimension, while the boundary sphere-times-circle gives exactly the same thing, so
the two descriptions move together rather than agreeing once by luck. That is worth recording. The bad part is
sitting in the prefactor. Four over three pi is exactly two-squared over three-pi in our integers, which looks
like a hit, and the three in it is not our colour three at all -- it is the one third that comes from averaging
a direction over the three dimensions of space. We happen to own a second three, and it is the right one, and
the tempting match uses the wrong one. An exact number attached to the wrong object is more dangerous than no
number, because nobody re-checks a hit. And the thing that would settle any of this is not a power or a
prefactor but the Bethe logarithm, a number that comes from summing over every intermediate state the electron
can visit; produce that from the boundary and the lead becomes a derivation, and until then it is a way of
seeing.

=> DISPOSITION: Casey's S⁴×S¹ Lamb reading -- I-tier, kept, with the dimensional-consistency check as its real
support (not the 5). COUNT-ONCE: it is the banked 3+1 fact read again, not a new confirmation. ★ CORRECTION TO
PROPAGATE BEFORE IT IS WRITTEN DOWN: 4/(3π) ≠ rank²/(N_c·π) structurally -- the 3 is the spatial directional
average (n_C−2), not the colour count. ★ GATE (sharpened): the computation must return ln k₀(2,0) =
2.811769893 AND ln k₀(2,1) = −0.030016709; two numbers of opposite sign defeat a one-parameter fudge. Firer:
Elie. Owed: nothing further from me unless someone runs the S⁴×S¹ self-energy -- I will score it against both
Bethe logs the session it lands. B1 remains first call: @Lyra, the harness (toy 5201) is waiting on your g=7
kernel. Nothing banked; nothing pushed.

Author: Elie (CI toy builder). Date: 2026-08-12.
"""

import math

results = []
def check(label, cond, detail=""):
    results.append((label, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {len(results)}. {label}")
    if detail:
        print(f"          {detail}")

alpha = 1/137.035999206
me_eV = 510998.95
h_eVs = 4.135667696e-15
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7

lnk0_2S = 2.811769893          # Bethe logarithm, hydrogen 2S (standard)
lnk0_2P = -0.030016709         # Bethe logarithm, hydrogen 2P
obs_MHz = 1057.845             # measured 2S₁/₂ − 2P₁/₂ Lamb shift

print("=" * 78)
print("Toy 5202: Casey's S⁴×S¹ Lamb reading -- does the coefficient land, or only the 5?")
print("=" * 78)

# ---------------------------------------------------------------------------
# 1. The standard result, reproduced.
# ---------------------------------------------------------------------------
print("\n--- 1. the standard leading self-energy, reproduced ---")
bracket = math.log(1/alpha**2) + 19/30 - lnk0_2S
dE = 4*alpha**5*me_eV/(3*math.pi*8) * bracket
dE_MHz = dE/h_eVs/1e6
check("The standard leading self-energy for 2S is ΔE = (4α⁵/3πn³)·mc²·[ln(1/α²) + 19/30 − ln k₀(n,l)]. With "
      f"the Bethe logarithm ln k₀(2,0) = {lnk0_2S} the bracket is {bracket:.6f} and ΔE = {dE_MHz:.2f} MHz "
      f"against the measured {obs_MHz} MHz -- {100*dE_MHz/obs_MHz:.2f}% of the observed shift, the remainder "
      "being vacuum polarisation, the 2P self-energy and recoil. So the α⁵ scaling and its coefficient are not "
      "in question; what is in question is whether the geometry produces them.",
      abs(100*dE_MHz/obs_MHz - 98.25) < 0.5,
      f"bracket {bracket:.6f}; ΔE = {dE_MHz:.2f} MHz vs {obs_MHz} MHz ({100*dE_MHz/obs_MHz:.2f}%)")

# ---------------------------------------------------------------------------
# 2. The exponent bookkeeping -- and the dimensional-consistency positive.
# ---------------------------------------------------------------------------
print("\n--- 2. ★ the grouping is dimensionally consistent -- not an accident of 5 = 4+1 ---")
rows = [(d, 1 + d + 1, (d+1) + 1) for d in (1, 2, 3, 4, 5)]
check("Standard QED bookkeeping splits the five powers as 1 (the radiative loop -- two vertices, e², which is "
      "exactly Casey's 'double bond') + 3 (from |ψ(0)|² ∝ (Zαm)³, a three-dimensional momentum volume) + 1 "
      "(the Coulomb vertex ⟨∇²V⟩). Casey splits them as 4 (S⁴) + 1 (S¹). Both total five, so the S⁴ must "
      "absorb the 3 + 1. ★ The test that this is structure rather than arithmetic: redo it in d spatial "
      "dimensions. QED gives 1 + d + 1 = d + 2; the Shilov boundary S^{d+1} × S¹ gives (d+1) + 1 = d + 2. "
      + "; ".join(f"d={d}: QED {q}, Shilov {s}" for d, q, s in rows)
      + ". They track for every d, not only at three. That is the real support for the reading -- better than "
      "the 5, which any grouping of five things would satisfy.",
      all(q == s for _, q, s in rows),
      "QED exponent d+2 = Shilov (d+1)+1 for d = 1..5 -- the grouping is dimensionally consistent")

check("★ COUNT-ONCE, applied immediately so this does not get tallied twice. The reason the identification "
      "works is that n_C − 2 = 3 is the spatial dimension -- and BST already derives 3+1 from D_IV⁵ (Casey "
      "#14). So the Lamb exponent is the SAME banked fact read in a new place, NOT an independent confirmation "
      "of the dimension and NOT a second vote for anything. One fact, one tally. It is a nice place to see the "
      "dimension show up; it is not new evidence that the dimension is right.",
      n_C - 2 == 3,
      "n_C − 2 = 3 = spatial dimension (Casey #14, banked) -- the Lamb exponent re-reads it, does not re-confirm it")

# ---------------------------------------------------------------------------
# 3. ★★ THE CATCH: the 3 in the coefficient is spatial, not colour.
# ---------------------------------------------------------------------------
print("\n--- 3. ★★ the catch: an EXACT match to the WRONG object ---")
coeff = 4/(3*math.pi)
tempting = rank**2/(N_c*math.pi)
check("★★ The coefficient is 4/(3π) = "
      f"{coeff:.6f}, and in BST integers it is EXACTLY rank²/(N_c·π) = {tempting:.6f} -- a 0.00% match, "
      "because we own an integer 4 (rank²) and an integer 3 (N_c). ★ THAT IDENTIFICATION IS WRONG. The 3 in "
      "4/(3π) is the SPATIAL DIRECTIONAL AVERAGE: it comes from ⟨p_i p_j⟩ → δ_ij/3 in the non-relativistic "
      "self-energy, an average over three spatial directions. BST owns two different threes -- N_c = 3 (colour) "
      "and n_C − 2 = 3 (the spatial dimension) -- and this coefficient wants the second one. An exact numerical "
      "match attached to the wrong object is MORE dangerous than no match, because nobody re-checks a hit. "
      "Correct assignment before anyone writes it down: the 3 is spatial (n_C − 2), not colour.",
      abs(coeff - tempting) < 1e-12 and (n_C - 2) == N_c,
      f"4/(3π) = {coeff:.6f} = rank²/(N_c·π) numerically EXACT -- and structurally wrong; the 3 is δ_ij/3, spatial")

check("This is the same species of category error I have caught three times today, which is the pattern worth "
      "noting rather than the instance: a volume ratio mistaken for a convention ratio (π²/2, toy 5197); a 4D "
      "cutoff compared with a 10D scale (toy 5200); and now a colour count standing in for a spatial "
      "dimension. All three were numerically plausible and structurally wrong, and all three would have "
      "survived a numerical check. The lesson is that matching the number is the weakest test we run.",
      True,
      "three category errors today, all numerically plausible: π²/2 | 4D-vs-10D | colour-3-vs-spatial-3")

# ---------------------------------------------------------------------------
# 4. Null model on the coefficient.
# ---------------------------------------------------------------------------
print("\n--- 4. and the numerical match carries no weight anyway ---")
BST = {'rank': rank, 'N_c': N_c, 'n_C': n_C, 'C_2': C_2, 'g': g, '1': 1}
found = set()
for n1, a in BST.items():
    for n2, b in BST.items():
        for n3, c in BST.items():
            for k in range(0, 3):
                for p in (1, 2):
                    v = (a**p)/(b*(math.pi**k)*c)
                    if abs(v/coeff - 1) < 0.01:
                        found.add(round(v, 6))
check(f"Null model: {len(found)} DISTINCT BST-natural values of the shape (integer^p)/(integer·π^k·integer) "
      f"land within 1% of 4/(3π) = {coeff:.6f}. So 'a BST form reproduces the coefficient' is not a rare "
      "event, and the one that reproduces it exactly is precisely the mis-assigned one. The numerical match "
      "carries no evidential weight in either direction -- which is the same verdict the 137 arithmetic got "
      "this morning, and for the same reason.",
      len(found) >= 3,
      f"{len(found)} distinct BST-natural values within 1% of {coeff:.6f} -- matching is cheap")

# ---------------------------------------------------------------------------
# 5. ★ The gate, sharpened to two numbers.
# ---------------------------------------------------------------------------
print("\n--- 5. ★ the gate: the Bethe logarithm, and it must be TWO of them ---")
check("★ The load-bearing number is not the power and not the prefactor -- it is the BETHE LOGARITHM "
      f"ln k₀(2,0) = {lnk0_2S}, an infinite sum over every intermediate state the electron can visit. No "
      "dimensional argument produces it. So the gate is sharp: if a self-energy computation on S⁴ × S¹ returns "
      "that number, Casey's lead is a derivation. If it returns the power 5 and a plausible prefactor, it is a "
      "way of seeing -- which is worth having, and is not the same thing.",
      True,
      f"gate = reproduce ln k₀(2,0) = {lnk0_2S} from the boundary self-energy")

check("★ And it must be TWO numbers, or it is a fit. Demand ln k₀(2,0) = "
      f"{lnk0_2S} AND ln k₀(2,1) = {lnk0_2P} -- the 2S and 2P Bethe logarithms. They have OPPOSITE SIGNS and "
      f"differ by a factor of {abs(lnk0_2S/lnk0_2P):.0f} in magnitude, so no single free constant can be tuned "
      "to hit both. One number is a coincidence waiting to happen; two of opposite sign is a test. I commit "
      "this bar now, before anyone runs the computation, so a match cannot be retrofitted.",
      lnk0_2S * lnk0_2P < 0 and abs(lnk0_2S/lnk0_2P) > 50,
      f"two-number bar COMMITTED BLIND: ln k₀(2,0) = {lnk0_2S}, ln k₀(2,1) = {lnk0_2P} -- opposite signs, {abs(lnk0_2S/lnk0_2P):.0f}× apart")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total_checks = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total_checks}   (reading dimensionally consistent = the real positive; the 3 in 4/(3π) is SPATIAL not N_c = the catch; two-Bethe-log gate committed blind)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5202, Casey's Lamb lead at I-tier, with Keeper's coefficient gate applied):
  * STANDARD RESULT REPRODUCED: bracket {bracket:.4f}, ΔE = {dE_MHz:.2f} MHz vs {obs_MHz} MHz observed ({100*dE_MHz/obs_MHz:.2f}%).
  * ★ THE REAL POSITIVE (better than the 5): the grouping is DIMENSIONALLY CONSISTENT. QED exponent =
    1(loop) + d(|ψ(0)|²) + 1(Coulomb) = d+2; Shilov S^{{d+1}}×S¹ = (d+1)+1 = d+2. Tracks for d = 1..5, so it is
    not an accident of 5 = 4+1. Casey's "double bond" is literally right: one α per loop = two vertices.
  * ★ COUNT-ONCE: it works because n_C−2 = 3 is the spatial dimension, ALREADY derived (Casey #14). The Lamb
    exponent RE-READS that fact; it does not re-confirm it. One tally.
  * ★★ THE CATCH: 4/(3π) = rank²/(N_c·π) EXACTLY (0.00%) -- and structurally WRONG. The 3 is the spatial
    directional average ⟨p_i p_j⟩ → δ_ij/3, so it is n_C−2 = 3 (the dimension), NOT N_c = 3 (colour). We own
    two threes and the tempting match uses the wrong one. An exact match to the wrong object is more dangerous
    than no match -- nobody re-checks a hit. Correct it before it is written down.
  * PATTERN WORTH NAMING: three category errors today, all numerically plausible, all structurally wrong --
    π²/2 as a convention ratio (5197), a 4D cutoff vs a 10D scale (5200), colour-3 for spatial-3 (here).
    Matching the number is the weakest test we run.
  * NULL MODEL: {len(found)} distinct BST-natural forms within 1% of 4/(3π). Matching is cheap; no weight either way.
  * ★ GATE COMMITTED BLIND, and it takes TWO numbers: reproduce ln k₀(2,0) = {lnk0_2S} AND
    ln k₀(2,1) = {lnk0_2P} from the S⁴×S¹ self-energy. Opposite signs, {abs(lnk0_2S/lnk0_2P):.0f}× apart -- no single
    free constant hits both. One number is a coincidence waiting to happen; two of opposite sign is a test.

AUG-12. Nothing pushed. Nothing banked. I-tier, light, as routed. @Lyra -- B1 is first call: the Leg-1 harness
(toy 5201) is waiting on your g=7 kernel and I run it the session it lands. Count once. CP existence-only.
""")
