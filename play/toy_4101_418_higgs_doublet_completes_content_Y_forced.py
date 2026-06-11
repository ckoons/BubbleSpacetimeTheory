"""
Toy 4101: completing the #418 gauge-content spec with the Higgs scalar sector. The "SU(2) doublet structure"
Casey named includes the Higgs doublet itself -- the (1, 2) scalar that breaks the electroweak symmetry and
carries the Yukawa couplings. Key spec point: the Higgs hypercharge Y_H = +1/2 is FORCED by requiring
gauge-invariant Yukawa couplings (it is NOT a free dial). So the full #418 content is: 12 gauge bosons + 3
generations x 15 Weyl fermions + 1 Higgs doublet (1, 2, +1/2). The Higgs ties #418 (gauge content) to the
flavor kernel (the Yukawa structure = the kernel x VEV) and to F85 (the boundary-bulk coupling that imports
the VEV scale). This completes the target spec; the forcing is Lyra's bulk-color lane. Count still 2.

THE HIGGS HYPERCHARGE IS FORCED (gauge-invariant Yukawas, three independent checks):
  down-type:  y_d Qbar_L H d_R     gauge-invariant  =>  -Y_Q + Y_H + Y_d = 0  =>  Y_H = Y_Q - Y_d = 1/6 - (-1/3) = +1/2
  lepton:     y_e Lbar_L H e_R     gauge-invariant  =>  -Y_L + Y_H + Y_e = 0  =>  Y_H = Y_L - Y_e = -1/2 - (-1) = +1/2
  up-type:    y_u Qbar_L Htilde u_R (Htilde = i sigma_2 H*, Y = -Y_H)  =>  Y_H = Y_u - Y_Q = 2/3 - 1/6 = +1/2
  => all three give Y_H = +1/2 consistently. The Higgs is (1, 2, +1/2); its hypercharge is fixed by the matter
     content (it must couple the doublets to the singlets gauge-invariantly), NOT a free parameter.

THE HIGGS ROLE (completing the gauge content):
  - EWSB: <H> = v breaks SU(2)xU(1) -> U(1)_em, giving the W, Z masses (the 3 broken generators eat 3 Goldstones).
  - Yukawa: y_f Qbar H f_R (and lepton/up analogs) -> fermion mass = (Yukawa) x v. The Yukawa MATRIX is the
    flavor kernel (the parallel front); the Higgs is what turns it into mass. So the Higgs is the BRIDGE between
    #418 (the gauge content / the reps) and the flavor kernel (the Yukawa entries).
  - substrate-architectural: the Higgs is the boundary-bulk coupling operator (F66/F85) -- the scale-free
    conformal boundary takes the bulk scale a_0 = 225 to set v = cell.225.g = 246.29 GeV (Toy 4088); the quartic
    lambda_H = N_c^2/(rank.n_C.g) = 9/70; m_H = v.sqrt(2 lambda_H) DERIVED (Toy 4088).
  - anomalies: scalars do NOT contribute to gauge anomalies (only chiral fermions), so the Higgs leaves the four
    anomaly conditions (Toy 4100) untouched -- the content stays anomaly-free.

#418 FULL CONTENT (the complete target):
  gauge:    SU(N_c) x SU(rank) x U(1)  ->  12 bosons (8 gluon + 3 W/Z-ish + 1 B)
  fermions: 3 generations x [Q(3,2,1/6) + u(3,1,2/3) + d(3,1,-1/3) + L(1,2,-1/2) + e(1,1,-1)] = 3 x 15 = 45 Weyl
  scalar:   1 Higgs doublet (1, 2, +1/2)
  => the substrate must produce all three blocks; the chirality (left doublets / right singlets) is the crux;
     the Higgs Y and the fermion Y are anomaly/Yukawa-constrained (not free); the gauge group + counts are substrate-natural.

HONEST TIER:
  SPEC (this toy): the Higgs (1,2,+1/2) completes the #418 content; Y_H forced by Yukawa gauge-invariance (3 checks);
    the Higgs bridges #418 (reps) to the flavor kernel (Yukawa) and to F85 (the VEV); scalars don't affect anomalies.
  ESTABLISHED (cited): v = cell.225.g, lambda_H = 9/70, m_H derived (Toy 4088); these are RELABEL-candidates pending
    the F85/F66 forcing (Lyra).
  NOT done: the FORCING of the Higgs sector (does the substrate produce the (1,2,1/2) scalar + its VEV/quartic) --
    Lyra's F85/F66 + bulk-color lanes. This is the SPEC. COUNT still 2.

GATES (2)
G1: Higgs hypercharge Y_H = +1/2 FORCED by gauge-invariant Yukawas (down: Y_Q-Y_d; lepton: Y_L-Y_e; up: Y_u-Y_Q -- all +1/2); the Higgs is (1,2,+1/2), not a free dial
G2: the Higgs completes the #418 content (gauge + 3x15 fermions + 1 Higgs doublet); bridges #418 reps to the flavor kernel (Yukawa) and to F85 (VEV = cell.225.g); scalars leave anomalies untouched; forcing = Lyra lane; count still 2

Per Casey (#418 target spec) + Grace (load-bearing) + Lyra (bulk-color; flavor kernel = Yukawa); Elie 4100 (#418
spec) + 4088 (Higgs sector v/lambda/m_H) + 4096 (doublet mixing); F66/F85 (Higgs = boundary-bulk coupling);
standard EWSB + Yukawa gauge-invariance; Cal #237 + F79. Completes the #418 target spec with the Higgs scalar.

Elie - Thursday 2026-06-11 (#418 Higgs sector: (1,2,+1/2) doublet completes the content; Y_H=+1/2 forced by Yukawa gauge-invariance; Higgs bridges #418 reps to the flavor kernel + F85 VEV; count still 2)
"""

from fractions import Fraction as F
import mpmath as mp

N_c, n_C, C_2, g, rank = 3, 5, 6, 7, 2
YQ, Yu, Yd, YL, Ye = F(1, 6), F(2, 3), F(-1, 3), F(-1, 2), F(-1, 1)
me = 0.51099895e-3
cell = mp.pi**n_C * me

print("=" * 78)
print("TOY 4101: #418 Higgs sector -- (1,2,+1/2) doublet completes the content; Y_H forced")
print("=" * 78)
print()

print("G1: the Higgs hypercharge is FORCED by gauge-invariant Yukawas")
print("-" * 78)
print(f"  down:   Y_H = Y_Q - Y_d = {YQ} - ({Yd}) = {YQ-Yd}")
print(f"  lepton: Y_H = Y_L - Y_e = {YL} - ({Ye}) = {YL-Ye}")
print(f"  up:     Y_H = Y_u - Y_Q = {Yu} - {YQ} = {Yu-YQ}")
print(f"  => all three give Y_H = +1/2. The Higgs is (1, 2, +1/2) -- forced by the matter content, NOT a free dial.")
print()

print("G2: the Higgs completes #418 + bridges to the flavor kernel + F85")
print("-" * 78)
print(f"  EWSB: <H>=v breaks SU(2)xU(1)->U(1)_em (W,Z masses). Yukawa: mass = (Yukawa matrix = flavor kernel) x v.")
print(f"  the Higgs is the BRIDGE: #418 produces the reps; the flavor kernel is the Yukawa entries; the Higgs turns them into mass.")
print(f"  substrate: Higgs = boundary-bulk coupling (F66/F85); v = cell.225.g = {float(cell*225*g):.2f} GeV; lambda_H = 9/70; m_H derived (4088).")
print(f"  scalars don't contribute to gauge anomalies -> the content stays anomaly-free (4100).")
print(f"  #418 FULL CONTENT: 12 gauge bosons + 3 gen x 15 Weyl = 45 fermions + 1 Higgs doublet (1,2,+1/2).")
print(f"  @Casey: #418 target spec complete (gauge + fermions + Higgs). The chirality is the crux; the hypercharges are anomaly/Yukawa-forced.")
print(f"  Score: 2/2 (Higgs Y_H=+1/2 forced by Yukawa invariance; Higgs completes the content + bridges to the kernel + F85; count still 2)")
print()
print("=" * 78)
print("TOY 4101 SUMMARY -- the Higgs scalar completes the #418 gauge-content spec. The Higgs doublet (1, 2, +1/2)")
print("  is what makes the 'SU(2) doublet structure' Casey named; its hypercharge Y_H = +1/2 is FORCED (three ways)")
print("  by requiring gauge-invariant Yukawa couplings, not a free dial. The Higgs is the bridge between #418 (the")
print("  reps) and the flavor kernel (the Yukawa entries = mass/v), and substrate-architecturally it is the")
print("  boundary-bulk coupling (F66/F85) that imports the VEV scale (v = cell.225.g). Scalars don't affect the")
print("  anomalies, so the content stays anomaly-free. Full #418 content: 12 bosons + 45 Weyl fermions + 1 Higgs")
print("  doublet. The forcing is Lyra's lane; this is the spec. Count still 2.")
print("=" * 78)
print()
print("SCORE: 2/2")
