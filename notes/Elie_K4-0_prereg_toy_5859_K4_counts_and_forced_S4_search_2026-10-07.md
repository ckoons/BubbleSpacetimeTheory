# Elie — PREREG toy 5859 (Round K4-0, Lane C). Wed 2026-10-07 13:52 EDT. Written BEFORE any code.

didwe "K4 S4 forced Weyl group Shilov boundary" → 0 hits. Predictions below are blind. Each item can fail.

## Part A — K4 counts (independent; brute force over vertex permutations, no table copied)
- A1 |Aut(K4)| = 24, faithful on V(4), E(6), triangular faces F(4).
- A2 Hamiltonian cycles: 3 undirected, 6 directed; rooted reads at a fixed frame vertex = 6.
- A3 Perfect matchings = 3; complement of each Ham cycle is a matching, bijectively.
- A4 S4 acts on {Ham cycles} and on {matchings} through S3, kernel = Klein V4 (order 4).
- A5 Cycle space over Z2: dim 3, 8 elements = {0} + 4 triangles + 3 four-cycles; S4 orbits of sizes 1, 4, 3.
- A6 Frame-vertex stabilizer = S3, faithful on the 3 values; its rotation subgroup Z3 splits the 6 rooted reads into 2 orbits of 3 (two handednesses).
- A7 H1(K4; Q) as an S4 rep = std ⊗ sign (character on a transposition −1), det = +1: S4 acts on the loops as the cube's ROTATION group in SO(3).
- Null A: same code on K3 (Aut 6, Ham 1, matchings 0, rank 1) and K5 (Aut 120, Ham 12, matchings 0, rank 6).

## Part B — search for a forced 4 / S4 / A4 / S3 in D_IV^5 (built from root data, exact rationals)
Canonical finite groups: (i) little Weyl group of the restricted roots C2 (interior flat); (ii) W_K of K = SO(5)×SO(2); (iii) W(g_C) = W(B3) for g_C = so(7); (iv) the Šilov Z2.
- B1 |W(C2)| = 8 and |W_K| = 8; neither has an element of order 3 ⇒ no S3, no Z3 triangle orientation, no K3/K4/K5 symmetric action in the interior's real Weyl data.
- B2 |W(B3)| = 48, contains S3 and S4, not S5 (Lagrange); ≅ S4 × Z2.
- B3 No W(B3) weight orbit (vector, spinor, roots) has size 4. K4 appears as one of the TWO tetrahedra in the spinor cube (±½)^3, each an orbit of the index-2 subgroup W(D3) ≅ S4 with full S4 action. Picking one tetrahedron = one sign.
- B4 Dictionary (A3 = D3): K4 vertices ↔ one spin tetrahedron; faces ↔ the other; 6 edges ↔ the 6 vector weights ±e_i (edge midpoints); 3 matchings ↔ 3 axes. Checked equivariantly.
- B5 Null K3: found WITHOUT a sign (W(B3) on the 3 axes, full S3). Null K5: absent from every group.
- B6 n-sweep D_IV^n, n = 3..8, max m with S_m ⊂ W(so(n+2)): 2, 4, 4, 4, 4, 5. K4 is the ceiling for n = 4..7; n = 5 NOT singled out.
- B7 Cap: the smallest faithful real rep of S_m has dim m−1 (hook lengths), so S_m ⊂ O(3) iff m ≤ 4. M ⊃ SO(3) on the short-root spaces (multiplicity a = n−2 = 3) ALLOWS S4 as the largest symmetric group; it forces none.
- Positive controls: the detector finds S_m in W(A_{m−1}) for m = 3, 4, 5 (orders 6, 24, 120); it finds W(C2) order 8 and W(B3) order 48.

## Pre-stated verdict rule
If B1 and B6 hold: the interior real Weyl data carry no S3/S4; S4 lives only in W(g_C) and needs one chirality sign to pick a tetrahedron; "4" is the rank-3 ceiling, generic over n = 4..7. Then **KL1 reads "allowed and capped, not forced"** from my side (R1/R2 are not mine to settle).
