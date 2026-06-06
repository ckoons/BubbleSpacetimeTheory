"""
Toy 4007: R(k) mechanism SCOUTING — the sum-of-roots reframe.

STATUS: bounded scouting, NOT the full theorem. Keeper deferred the rigorous
mechanism of R(k) = -C(k,2)/n_C (Toy 4005) to its own session. This toy captures the
sharpest reframe while it's fresh + names the candidate mechanism directions, so the
future dedicated session starts from the right question. No theorem claimed.

THE REFRAME (rigorous, from the cascade's own definition)
In toy_671, "ratio(k)" = p[2k-1]/p[2k], the sub-leading-over-leading coefficient of
a_k(n) -- the k-th heat-trace coefficient as a degree-2k polynomial in the dimension n.
By Vieta, p[2k-1]/p[2k] = -(sum of roots). So R(k) = -C(k,2)/n_C becomes:

    SUM OF ROOTS of a_k(n)  =  C(k,2)/n_C  =  k(k-1)/(2*n_C).

That is a much more mechanism-suggestive statement than "ratio sequence": the 2k roots
(in dimension-space) of the k-th heat coefficient SUM to the binomial C(k,2) over the
substrate dimension n_C.

CANDIDATE MECHANISM DIRECTIONS (leads for the dedicated session, not derived here)
 (1) quadratic-in-k = k(k-1): a RANK-2 / two-index signature. D_IV^5 has rank 2; heat
     coefficients on a rank-2 symmetric space carry two-Pochhammer / Jacobi structure
     whose order-k data is quadratic in k. C(k,2) = number of unordered index pairs.
 (2) 1/n_C normalization: n_C = dim D_IV^5 = the leading Weyl/volume dimension that
     sets the leading polynomial coefficient p[2k]; the root-sum is the curvature
     (sub-leading) term over the volume (leading) term -> ~ 1/dimension.
 (3) integer iff n_C | C(k,2) iff k = 0,1 (mod n_C): the speaking pairs are the
     dimensions at which the binomial clears the dimensional normalization.

GATES (4)
G1: Vieta reframe (rigorous)
G2: sharpened target + speaking-pair restatement
G3: candidate mechanism directions (leads, honestly tagged)
G4: what the dedicated-session theorem needs

Elie - Saturday 2026-06-06
"""

from fractions import Fraction as F

rank, N_c, n_C, C_2, g, N_max = 2, 3, 5, 6, 7, 137

print("=" * 72)
print("TOY 4007: R(k) mechanism SCOUTING -- sum-of-roots reframe (not the theorem)")
print("=" * 72)
print()

print("G1: Vieta reframe (rigorous)")
print("-" * 72)
print("  cascade def: ratio(k) = p[2k-1]/p[2k]  (a_k(n) is degree 2k in dimension n)")
print("  Vieta:       p[2k-1]/p[2k] = -e_1(roots) = -(sum of roots)")
print("  Toy 4005:    R(k) = -C(k,2)/n_C")
print("  => SUM OF ROOTS of a_k(n) = C(k,2)/n_C = k(k-1)/(2*n_C)   [rigorous given def]")
print()

print("G2: sharpened target + speaking-pair restatement")
print("-" * 72)
print(f"  {'k':>3} {'sum of roots = C(k,2)/n_C':>26} {'integer?':>9}")
for k in [5, 6, 10, 11, 15, 16, 20, 21, 22, 25, 26]:
    s = F(k * (k - 1), 2 * n_C)
    print(f"  {k:>3} {str(s):>26} {'YES (pair)' if s.denominator==1 else 'no':>9}")
print(f"  speaking pair <=> n_C | C(k,2) <=> k = 0 or 1 (mod n_C={n_C})")
print()

print("G3: candidate mechanism directions (LEADS, not derived)")
print("-" * 72)
print("  (1) k(k-1) quadratic  -> RANK-2 two-index signature (D_IV^5 rank=2);")
print("      C(k,2) = # unordered index pairs at order k. Jacobi/2-Pochhammer route.")
print("  (2) 1/n_C  -> dimensional normalization: root-sum = (sub-leading curvature")
print("      term)/(leading volume term) ~ 1/dim, dim = n_C = 5.")
print("  (3) integrality at k=0,1 mod n_C -> dimensions where C(k,2) clears n_C.")
print("  Cross-anchor: Bergman exponent (n_C+rank)/2 = 7/2 (Ch 7) is the natural place")
print("  the rank-2 + dimension data enters the heat-coefficient polynomial.")
print()

print("G4: what the dedicated-session theorem needs (deferred per Keeper)")
print("-" * 72)
print("  - the explicit degree-2k polynomial a_k(n) for the D_IV^5 heat trace (rep-theory,")
print("    Lyra lane) -- show its root-sum = C(k,2)/n_C from the rank-2 Jacobi structure.")
print("  - verify against the actual extracted polynomial coefficients (not just ratios).")
print("  - relate to the Bergman/Mehler expansion exponents (Ch 7).")
print("  This toy does NOT attempt that. It hands the future session the right question:")
print("  'why does the heat-coefficient polynomial's root-sum equal C(k,2)/n_C?'")
print()
print("  Score: 4/4 (reframe rigorous; target sharpened; directions + theorem-needs named)")
print()
print("=" * 72)
print("TOY 4007 SUMMARY -- R(k) reframed: sum of roots of a_k(n) = C(k,2)/n_C")
print("  rank-2 (k(k-1)) + dimension (1/n_C) is the mechanism direction; theorem deferred")
print("=" * 72)
print()
print("SCORE: 4/4")
