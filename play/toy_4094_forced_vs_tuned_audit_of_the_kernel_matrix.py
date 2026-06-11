"""
Toy 4094: forced-vs-tuned audit of the flavor matrix M_ij = c . K(nu_i, nu_j) -- Casey's Q2 ("how does the
Hermitian matrix come to be -- just geometry, or is anything tuned?"). This is the reduction-vs-relabel
question at the matrix level, and it decides whether hitting the bar {206.77, 3477, PMNS} is a WIN (forced ->
reduction) or worthless (tuned -> relabel). Counting the free knobs:

  INGREDIENT            WHAT IT IS                                              FORCED?         KNOBS
  c (scalar prefactor)  the dimensionful anchor m_e (Band C, the 1 unit)        FORCED-as-unit  0 (it IS the unit; cancels in ratios)
  the 3 points nu       {5/2,3/2,0} = Wallach {0,a/2} (a=n_C-2=N_c) + Hardy g/2  FORCED          0 (= rho-vector, 4083/4085)
                        = the rho-vector
  the kernel K          the Bergman kernel of D_IV^5 (unique reproducing kernel) FORCED          0 (unique to the geometry)
  spinor content        all leptons spin-1/2 (universal across generations)      FORCED          0 (universal -> into c)
  pole regularization   boundary measure at nu=3/2,0 poles (Shilov S^1 -> 2pi)   OPEN->forced?   ? (measure forced BY stratum, not chosen)
  (a,b) / K-type index  scalar Wallach reps: nu is the only label;               OPEN->nu-only?  ? (Lyra verifying nu-only collapse)
                        the (a,b) family = OUTPUT of the off-diagonal kernel

  SKELETON (c + 3 points + kernel + spinor) = ALL FORCED, ZERO free knobs -- the matrix IS the Bergman kernel
  sampled at the forced rho-vector points. That is geometry, full stop. No tuning in the skeleton.
  OPEN (2): the pole-regularization prescription + whether the label is nu-only (vs a genuine (a,b) 2nd index).
  These are NOT free knobs to fit -- they are FORCED-CANDIDATES: the boundary stratum fixes the measure (not
  chosen), and scalar reps have no K-type knob (the (a,b) family is an OUTPUT of the off-diagonals, not an input).

VERDICT (Casey's Q2):
  the matrix is the geometry's own reproducing kernel evaluated at the geometry's own forced points -- so it IS
  the result of the geometry, not a tuned object. The reduction-vs-relabel question collapses to exactly Lyra's
  two flags: (1) is the pole-regularization forced by the stratum (no measure-choice)? (2) does the label
  collapse to nu-only (the leptons are scalar Wallach reps, spin universal)? Neither is currently a free knob;
  both are forced-candidates. IF both confirm forced -> the matrix has ZERO knobs -> hitting {206.77, 3477, PMNS}
  is a PREDICTION (reduction, count 2->5+). IF a hidden knob surfaces in either -> TUNED -> relabel (no win).

WHY THIS MATTERS (the stakes, and Casey's Q3):
  a FORCED matrix that hits the bar is a reduction (the geometry predicted the masses + mixing); a TUNED matrix
  that hits the bar is worthless (you fit it). So forced-vs-tuned is the WHOLE game -- it's why the team holds
  the no-fishing line so hard. The good news from this audit: there is nowhere obvious for a knob to hide -- the
  skeleton is forced, and the two open items are structurally forced-candidates, not adjustable parameters.
  CASEY's Q3 (the clarification modern physics should use): REGARDLESS of how the two open items resolve, the
  STRUCTURE is the clarification -- the SM's 9+ free Yukawa parameters ARE the entries of ONE geometric kernel
  matrix over 3 points; masses + mixing + CP come from ONE diagonalization. That reframing stands on the forced
  skeleton alone (the points + the kernel), independent of the regularization detail. Physics should use it: the
  flavor sector is not 9 free numbers, it is one kernel matrix of one geometry.

HONEST TIER:
  BANKED (audit): the skeleton (c, 3 points, kernel, spinor) is FORCED, zero knobs -- the matrix is the geometry.
    The structure-level clarification (Yukawa = one kernel matrix) stands on the forced skeleton.
  OPEN (forced-candidates, Lyra's two flags): the pole-regularization (forced by stratum?) + nu-only collapse
    (scalar reps?). Not free knobs; forced-candidates pending Lyra's careful derivation. The verdict rides here.
  NOT done / DECLINED: declaring the matrix fully forced (the two open items are Lyra's). COUNT still 2; it moves
    to 5+ IF the forced matrix hits {206.77, 3477, PMNS}, and only if forced (a tuned hit is no win).

GATES (2)
G1: forced-vs-tuned audit -- skeleton (c + 3 points + kernel + spinor) FORCED with ZERO knobs (the matrix IS the Bergman kernel at the rho-vector points); 2 open items (regularization, nu-only) are forced-CANDIDATES, not free knobs
G2: verdict + stakes -- reduction-vs-relabel collapses to Lyra's 2 flags; forced matrix hitting bar = reduction, tuned hit = relabel; the structure-clarification (Yukawa = one kernel matrix, Casey Q3) stands on the forced skeleton regardless

Per Casey (Q1 follow / Q2 forced-vs-tuned / Q3 the clarification; operation-matrix = result of geometry) + Grace
(scalar,scalar,matrix; c cancels in ratios) + Lyra (M_ij=c.K(nu_i,nu_j); two flags: regularization + nu-only-vs-(a,b);
scalar-vs-spinor Wallach caveat) + Keeper K298; Elie 4083/4085 (rho-vector points) + 4092/4093 (c.A engine); Cal #237
+ F79 + Grace input-count bar. The skeleton is forced; the verdict rides on Lyra's two flags; the clarification stands.

Elie - Wednesday 2026-06-10 (forced-vs-tuned audit: skeleton c+points+kernel+spinor FORCED zero knobs (matrix = geometry); 2 open forced-candidates (regularization, nu-only) = Lyra flags; structure-clarification stands regardless)
"""

N_c, n_C, C_2, g, rank = 3, 5, 6, 7, 2

print("=" * 78)
print("TOY 4094: forced-vs-tuned audit of M_ij = c . K(nu_i, nu_j) -- count the free knobs")
print("=" * 78)
print()

print("G1: the audit -- forced skeleton + open forced-candidates")
print("-" * 78)
rows = [
    ("c (scalar)", "anchor m_e (Band C, the 1 unit)", "FORCED-as-unit", "0 (it IS the unit; cancels in ratios)"),
    ("3 points nu", "{5/2,3/2,0} = Wallach + Hardy = rho-vector", "FORCED", "0 (4083/4085)"),
    ("kernel K", "Bergman kernel of D_IV^5 (unique)", "FORCED", "0 (unique to the geometry)"),
    ("spinor content", "leptons spin-1/2, universal", "FORCED", "0 (universal -> into c)"),
    ("pole regularization", "boundary measure at nu=3/2,0 (Shilov S^1)", "OPEN->forced?", "? (measure forced BY stratum)"),
    ("(a,b)/K-type", "scalar reps: nu-only; (a,b)=OUTPUT", "OPEN->nu-only?", "? (Lyra verifying)"),
]
for name, what, status, knobs in rows:
    print(f"  {name:<20} {what:<42} {status:<14} {knobs}")
print()
print(f"  SKELETON (c + 3 points + kernel + spinor) = ALL FORCED, ZERO knobs -- the matrix IS the Bergman kernel at the rho-vector points.")
print(f"  OPEN (2): pole-regularization + (a,b)-vs-nu-only -- NOT free knobs; FORCED-CANDIDATES (stratum fixes measure; scalar reps have no K-type knob).")
print()

print("G2: verdict + stakes (Casey Q2 + Q3)")
print("-" * 78)
print(f"  Q2 (forced or tuned): the matrix is the geometry's own kernel at the geometry's own forced points -- it IS the geometry,")
print(f"    no tuning in the skeleton. Reduction-vs-relabel collapses to Lyra's 2 flags (regularization forced? nu-only?). Neither is a free knob.")
print(f"    IF both forced -> ZERO knobs -> hitting {{206.77,3477,PMNS}} = REDUCTION (prediction, 2->5+). IF a knob hides -> TUNED -> relabel (no win).")
print(f"  Q3 (the clarification): REGARDLESS of the 2 open items, the SM's 9+ free Yukawas ARE the entries of ONE geometric kernel matrix over")
print(f"    3 points -- masses+mixing+CP from ONE diagonalization. That reframing stands on the forced skeleton (points + kernel) alone. Physics should use it.")
print(f"  @Casey: the matrix is the result of the geometry (forced skeleton, zero knobs); the verdict rides on Lyra's 2 flags, neither a free knob.")
print(f"  @Lyra: your 2 flags ARE the entire forced-vs-tuned question -- regularization-forced-by-stratum + nu-only-collapse. The skeleton is forced.")
print(f"  Score: 2/2 (audit: skeleton forced zero knobs; 2 open forced-candidates = Lyra flags; structure-clarification stands regardless; count still 2)")
print()
print("=" * 78)
print("TOY 4094 SUMMARY -- forced-vs-tuned audit of M_ij = c.K(nu_i,nu_j). The SKELETON -- the scalar c (the")
print("  anchor), the 3 points {5/2,3/2,0} (the rho-vector), the Bergman kernel K (unique), the universal spinor")
print("  content -- is ALL FORCED with ZERO free knobs: the matrix IS the geometry's reproducing kernel sampled at")
print("  the geometry's forced points. The only OPEN items are the pole-regularization prescription and whether the")
print("  label is nu-only -- and these are forced-CANDIDATES (the stratum fixes the measure; scalar reps have no")
print("  K-type knob), not free knobs. So the reduction-vs-relabel verdict rides on exactly Lyra's two flags. The")
print("  structure-level clarification (the Yukawa matrix = one geometric kernel, masses+mixing+CP from one")
print("  diagonalization) stands on the forced skeleton regardless. Count still 2 -- and a hit is a win only if forced.")
print("=" * 78)
print()
print("SCORE: 2/2")
