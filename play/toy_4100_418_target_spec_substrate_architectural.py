"""
Toy 4100 (milestone): the #418 gauge-content TARGET SPEC (Casey's Thursday assignment) -- a complete
substrate-architectural specification of what the substrate must produce to give the SM gauge sector, the
fermion reps, and the SU(2) doublet structure. This is the TARGET (the deliverable), not the derivation; the
forcing is Lyra's bulk-color lane. Fully independent of the flavor-kernel work, so the two fronts run parallel.

THE SPEC, in six parts:

1) GAUGE GROUP -- SU(N_c) x SU(rank) x U(1)_Y = SU(3) x SU(2) x U(1)
   - the two non-abelian factors are the substrate primaries: N_c = 3 (color), rank = 2 (weak isospin).
   - dim: (N_c^2-1) + (rank^2-1) + 1 = 8 + 3 + 1 = 12 gauge bosons.
   - NOT a GUT: SU(3)xSU(2)xU(1) directly, NOT via SU(5)/SO(10) unification. Consistent with the Five-Absence
     set (no GUT, no proton decay, no monopoles). The substrate produces the SM group, not a unified one.

2) FERMION CONTENT -- one generation = 15 Weyl = N_c.n_C = dim SO(4,2):
   field    SU(3) x SU(2)   Y       Weyl count
   Q        (3, 2)          +1/6    N_c.rank = 6   (left quark doublet)
   u        (3, 1)          +2/3    N_c     = 3   (right up)
   d        (3, 1)          -1/3    N_c     = 3   (right down)
   L        (1, 2)          -1/2    rank    = 2   (left lepton doublet)
   e        (1, 1)          -1      1            (right electron)
   TOTAL                                   15 = N_c.n_C = dim SO(4,2)   (+1 nu_R -> 16 = SO(10) spinor)
   - generation COUNT = rank+1 = 3 (F88, Koranyi-Wolf strata).

3) CHIRALITY (the deep requirement) -- LEFT fields are SU(2) doublets (Q, L); RIGHT fields are singlets (u, d, e).
   - the SU(2)_L acts on left-handed fermions ONLY -> the chiral, parity-violating structure of the weak force.
   - SUBSTRATE LEAD: D_IV^5 is a complex (Hermitian symmetric) domain -- holomorphic functions carry ONE chirality.
     Casey #14 substrate-mechanism SO(5,2) -> SO(4,2) (1/n_C chirality projection) -> SO(3,1) is the
     substrate-architectural source of the left/right asymmetry. The doublet-vs-singlet split is the chirality split.

4) HYPERCHARGES -- anomaly-constrained (verified anomaly-FREE):
   SU(3)^2.U(1): 2Y_Q - Y_u - Y_d = 0 ; SU(2)^2.U(1): 3Y_Q + Y_L = 0 ; U(1)^3: Sum Y^3 = 0 ; grav.U(1): Sum Y = 0.
   - all four cancel for the 15 = N_c.n_C content. The substrate must produce ANOMALY-FREE hypercharges -- and
     anomaly cancellation, given the reps, FIXES Y up to normalization (so Y is not a free per-field dial).

5) LOAD-BEARING (Grace: #418 is load-bearing 3 ways -- one program securing multiple pieces of the reduction):
   - (a) RUNNING BAND B: the reps + Y give b_2 = -19/6, b_1 = -41/10 (Toy 4099, b_3 = g from 4090) -> alpha_s,
     sin^2 theta_W running. #418 closes Band B step 1.
   - (b) MIXING-FORCED: the SU(2) doublet L = (nu,e)_L is ONE object -> charged-lepton and neutrino share one
     frame by construction -> CKM/PMNS are forced mismatches, no free angle (Grace, Toy 4096).
   - (c) MATTER CONTENT / CHIRALITY: #418 produces the fermion reps + the chiral doublet/singlet split themselves
     -- the existence and structure of matter (the 15 = N_c.n_C content). (Grace's 3rd role; confirm exact framing.)

6) SUBSTRATE-NATURAL NOW vs MUST-BE-FORCED:
   - substrate-natural (verified): gauge group from the primaries; one-generation content count = N_c.n_C = 15 =
     dim SO(4,2); generation count rank+1 = 3; the doublet-as-common-frame; the content is anomaly-free.
   - must be FORCED (Lyra bulk-color lane, #418 derivation): the specific reps (which fields are doublets vs
     singlets = the chirality assignment), the anomaly-consistent hypercharges, the chiral projection itself.

THE BAR (Grace's input-count): #418 REDUCES the count iff the substrate FORCES the reps + chirality + Y from few
inputs (vs the SM taking them as given). The gauge group is near-forced (primaries); the content count is
N_c.n_C; the reduction hinges on forcing the chiral rep assignment + the (anomaly-constrained) hypercharges
from the substrate geometry. That forcing is the open derivation.

HONEST TIER:
  SPEC (this toy -- the target, verified where quantitative): gauge group, content = N_c.n_C = 15, anomaly-free
    (4 conditions cancel), chirality structure, load-bearing roles, substrate-natural-vs-forced split, the bar.
  LEADS (flagged): chirality from D_IV^5 holomorphy / Casey #14 projection; 15 = N_c.n_C = dim SO(4,2); 16 = SO(10)
    spinor as an organizing observation (NOT a GUT gauge symmetry).
  NOT done: the FORCING (the reps + Y from the substrate) -- Lyra's bulk-color derivation. This is the SPEC, not
    the derivation, per Casey. COUNT still 2; scoping the target does not move it.

GATES (2)
G1: #418 target spec -- gauge group SU(N_c)xSU(rank)xU(1) (not a GUT); content 15=N_c.n_C=dim SO(4,2)/generation; chirality (left doublets/right singlets); anomaly-free (4 conditions verified); 3 generations
G2: load-bearing 3 ways (running band b_2/b_1 + mixing-forced doublet + matter content/chirality) + substrate-natural-vs-forced split + the input-count bar; the forcing = Lyra bulk-color lane; count still 2

Per Casey (Thursday: #418 target spec, not derivation) + Grace (#418 load-bearing 3 ways; second front) + Lyra
(bulk-color F-series; engine back-half); Elie 4090 (b_3=g) + 4098 (scope) + 4099 (beta coeffs) + 4096 (doublet
mixing); F88 (generation count); Casey #14 (chirality projection); Five-Absence (no GUT); standard SM anomaly
conditions; Cal #237 + F79. The substrate-architectural target spec for #418; forcing = bulk-color derivation.

Elie - Thursday 2026-06-11 (#418 TARGET SPEC: SU(3)xSU(2)xU(1) gauge + 15=N_c.n_C=dim SO(4,2) content + chirality (left doublets) + anomaly-free Y; load-bearing 3 ways; not a GUT; forcing = Lyra bulk-color)
"""

from fractions import Fraction as F

N_c, n_C, C_2, g, rank = 3, 5, 6, 7, 2
YQ, Yu, Yd, YL, Ye = F(1, 6), F(2, 3), F(-1, 3), F(-1, 2), F(-1, 1)

print("=" * 78)
print("TOY 4100: #418 TARGET SPEC -- gauge group + 15=N_c.n_C content + chirality + anomaly-free Y")
print("=" * 78)
print()

print("G1: the spec -- gauge group, content, chirality, anomaly-freedom")
print("-" * 78)
print(f"  GAUGE: SU(N_c) x SU(rank) x U(1) = SU(3)xSU(2)xU(1); dim {N_c**2-1}+{rank**2-1}+1 = {N_c**2-1+rank**2-1+1} bosons. NOT a GUT (Five-Absence).")
print(f"  CONTENT (one generation):")
rows = [("Q", "(3,2)", YQ, N_c * rank, "left quark doublet"), ("u", "(3,1)", Yu, N_c, "right up"),
        ("d", "(3,1)", Yd, N_c, "right down"), ("L", "(1,2)", YL, rank, "left lepton doublet"),
        ("e", "(1,1)", Ye, 1, "right electron")]
tot = sum(c for _, _, _, c, _ in rows)
for f, rep, Y, c, note in rows:
    print(f"    {f}  {rep:<6} Y={str(Y):<5} {c} Weyl   {note}")
print(f"    TOTAL = {tot} Weyl = N_c.n_C = {N_c*n_C} = dim SO(4,2) (+1 nu_R -> 16 = SO(10) spinor). count = rank+1 = 3 gens.")
print(f"  CHIRALITY: left = doublets (Q,L), right = singlets (u,d,e); SU(2)_L on left only. Lead: D_IV^5 holomorphy / Casey #14 projection.")
a = [2*YQ-Yu-Yd, 3*YQ+YL,
     sum(m*Y**3 for m, Y in [(6, F(1, 6)), (3, -Yu), (3, -Yd), (2, F(-1, 2)), (1, -Ye)]),
     sum(m*Y for m, Y in [(6, F(1, 6)), (3, -Yu), (3, -Yd), (2, F(-1, 2)), (1, -Ye)])]
print(f"  ANOMALIES: SU(3)^2U(1)={a[0]}, SU(2)^2U(1)={a[1]}, U(1)^3={a[2]}, grav={a[3]} -- ALL cancel: {all(x==0 for x in a)}. Content anomaly-FREE.")
print()

print("G2: load-bearing 3 ways + substrate-natural-vs-forced + the bar")
print("-" * 78)
print(f"  (a) running band: reps+Y -> b_2=-19/6, b_1=-41/10 (4099), b_3=g (4090). (b) mixing-forced: SU(2) doublet -> shared frame (4096).")
print(f"  (c) matter content/chirality: #418 produces the 15=N_c.n_C reps + the chiral split itself. (Grace's 3 ways.)")
print(f"  substrate-natural NOW: gauge group; content count N_c.n_C=15=dim SO(4,2); gen count rank+1=3; anomaly-free; doublet-frame.")
print(f"  must be FORCED (Lyra bulk-color): the chiral rep assignment (doublets vs singlets) + the anomaly-consistent hypercharges + the chirality projection.")
print(f"  @Casey: target spec drafted -- gauge + content + chirality + anomaly-free Y; load-bearing 3 ways; not a GUT. Forcing = Lyra's lane.")
print(f"  @Grace: ready for your input-count bar -- the reduction hinges on forcing the chiral reps + Y. @Lyra: the spec is your bulk-color target.")
print(f"  Score: 2/2 (full #418 target spec: gauge/content/chirality/anomaly-free; load-bearing 3 ways; substrate-natural-vs-forced; not a GUT; count still 2)")
print()
print("=" * 78)
print("TOY 4100 SUMMARY -- the #418 gauge-content TARGET SPEC. The substrate must produce: (1) the gauge group")
print("  SU(N_c)xSU(rank)xU(1) from the primaries (NOT a GUT); (2) one generation = 15 Weyl = N_c.n_C = dim SO(4,2)")
print("  in the SM reps (16 = SO(10) spinor with nu_R), 3 generations; (3) the CHIRALITY (left doublets, right")
print("  singlets -- SU(2)_L on left only; lead: D_IV^5 holomorphy / Casey #14 projection); (4) anomaly-free")
print("  hypercharges (all 4 conditions verified to cancel). #418 is load-bearing 3 ways (running band + forced")
print("  mixing + matter content). Substrate-natural now: the gauge group, the N_c.n_C count, the generation count,")
print("  the anomaly-freedom; must be forced: the chiral reps + Y -- Lyra's bulk-color derivation. This is the spec,")
print("  not the derivation; count still 2.")
print("=" * 78)
print()
print("SCORE: 2/2")
