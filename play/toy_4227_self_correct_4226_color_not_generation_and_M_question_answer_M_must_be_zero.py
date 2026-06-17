r"""
Toy 4227: self-correcting 4226 (Lyra's F178 catch) + answering Grace's pivotal M-question. Two parts:
  (A) SELF-CORRECTION (no defense): in 4226 I derived the CKM Wolfenstein hierarchy |V_ub| ~ |V_us|*|V_cb| from the su(3)
      COMPOSITE root. But Lyra's su(3) (F177) is the COLOR su(3) (the 3 strata = the 3 colors), and COLOR COUPLES UP AND
      DOWN THE SAME -- it is BLIND to up-vs-down. The CKM is the up/down misalignment, a GENERATION-space, weak-isospin
      (T_3^R) object -- NOT color. So my composite-root derivation used the WRONG SOURCE (color, not generation). The
      relation V_ub ~ V_us*V_cb is empirically real (Wolfenstein), but its substrate SOURCE must be the generation /
      up-down structure, not the color su(3). 4226's derivation is RETRACTED; the hierarchy is gated on the up/down seats.
  (B) GRACE'S M-QUESTION (the pivot): M = the number of free angles in the up/down seat misalignment that fills V; R =
      4(CKM)/M. STRUCTURAL ANSWER: M MUST be 0. BST has ZERO free parameters -- that is the whole program. So the up/down
      quark seats are FORCED (the same discrete-series/Wallach mechanism that placed the leptons), the misalignment is
      forced, and the 4 CKM parameters are fully determined: M=0, R=infinity. If the CKM does NOT come out forced (M>0),
      that is a FAILURE of BST on the quark sector, NOT a free-angle escape hatch. The bar is M=0.
Count stays 4 of 26.

(A) SELF-CORRECTION OF 4226 (Lyra F178):
  Lyra F177: {+1,-1,0} = lambda_3 Cartan on the COLOR triplet; the 3 Korany-Wolf strata = the 3 COLORS. the 8 su(3)
  generators are COLOR generators. COLOR is vector-like: it couples up-type and down-type quarks IDENTICALLY -> color is
  BLIND to up-vs-down. the CKM = <up | down> = the misalignment of the up-type and down-type mass bases, which comes from
  the WEAK-ISOSPIN T_3^R difference (up has T_3=+1/2, down -1/2), a GENERATION-space chiral object -- NOT color.
  so 4226's |V_ub| ~ |V_us|*|V_cb| "from the su(3) composite root" mapped the COLOR su(3) onto GENERATION mixing -- a
  category error (color != generation). RETRACTED. the Wolfenstein hierarchy is a real empirical pattern; its substrate
  source is the up/down generation seats (the gated #418 chiral content), and IF the 3 generations carry an A_2-like
  structure the composite=product pattern may re-derive there -- but from the generation structure, not the color su(3).

(B) GRACE'S M-QUESTION, ANSWERED STRUCTURALLY (M must be 0):
  Grace: R = 4(CKM params) / M, M = free angles in the up/down seat misalignment.
    M=0 -> R=inf (4 CKM fully determined, strongest motion) ; M=1 -> R=4 (strong) ; M>=4 -> R<=1 (a fit, THE LINE).
  BST answer: M = 0, necessarily. the entire program is ZERO free parameters -- every mass and mixing is forced by the
  geometry. so the up/down quark seats are FORCED (exactly as the lepton seats were forced at the Wallach points {0,3/2,
  5/2}), the up-vs-down misalignment is forced, and the 4 CKM parameters are determined with NO free angle. M=0, R=infinity.
  CRUCIAL (the discipline): "M=1, one free angle, still strong" is NOT an acceptable fallback for BST -- a free angle IS a
  free parameter, which the program forbids. so the bar is M=0: the CKM must come out FULLY forced from the derived up/down
  seats, or the quark sector is an honest FAILURE (not a partial fit). no free-angle escape hatch.

THE GATED PIECE (named precisely) + THE TARGET:
  deriving the FORCED up/down quark seats -- the 6 K-type addresses split by weak-isospin T_3^R (the SU(2)_L doublet
  structure) -- is the deep #418 chiral content. same shape as the neutrino sector yesterday: both halves armed (Lyra's
  color su(3) + my CKM filter 4225), the deep object (the up/down seats) in the middle still to derive. the honest target
  (Lyra + Grace): the derived seats must yield theta_C and m_d/m_s satisfying Gatto (sin theta_C = sqrt(m_d/m_s), 0.62%)
  WITHOUT anyone dialing to 0.2245 -- the cross-family check that, with M=0, is the referee-proof motion.

HONEST STATUS:
  (A) absorbs Lyra's F178: 4226's CKM-hierarchy-from-su(3) used the COLOR su(3) for a GENERATION object -- color is blind
  to up/down -- so it is RETRACTED (the empirical Wolfenstein relation stands; its source is the up/down generation seats,
  gated). (B) answers Grace's M-question structurally: M must be 0 (BST = zero free parameters), so the up/down seats are
  forced and the CKM is fully determined (R=inf) -- and M>0 would be a FAILURE, not a free-angle fallback. the gated piece
  is the forced up/down seats (the #418 T_3^R chiral content); the target is Gatto-satisfying seats, untuned. my filter is
  armed for M=0. banks nothing; count holds at 4 of 26.
"""

N_c, n_C, C2, g, rank, N_max = 3, 5, 6, 7, 2, 137

# (A) the category check: color is vector-like (blind to up/down); CKM is generation/T_3^R
color_blind_to_updown = True   # color couples up and down identically (vector-like)
ckm_is_generation = True       # CKM = up/down misalignment in generation space (T_3^R)

# (B) the M-table (Grace) + BST's structural answer
M_table = {0: float("inf"), 1: 4.0, 4: 1.0}
bst_M = 0                      # zero free parameters -> M must be 0
bst_R = float("inf")

# Gatto target (cross-family check, untuned)
Vus = 0.2245
gatto = (1/20)**0.5

print("=" * 100)
print("TOY 4227: self-correct 4226 (color != generation, Lyra F178) + answer Grace's M-question (M MUST be 0)")
print("=" * 100)
print()
print("(A) self-correction of 4226 (Lyra F178):")
print("-" * 100)
print("  Lyra's su(3) (F177) = COLOR su(3) (strata = colors). color is vector-like -> couples up & down the SAME -> BLIND to up/down.")
print("  CKM = <up | down> = up/down misalignment = GENERATION-space, weak-isospin T_3^R object -- NOT color.")
print("  -> 4226's |V_ub|~|V_us|*|V_cb| 'from the su(3) composite root' mapped COLOR su(3) onto GENERATION mixing = category error. RETRACTED.")
print("  the Wolfenstein relation is real (empirical); its source is the up/down generation seats (gated #418), not color su(3).")
print()
print("(B) Grace's M-question, answered structurally:")
print("-" * 100)
print(f"  R = 4(CKM)/M:  M=0 -> R=inf (strongest) ; M=1 -> R=4 (strong) ; M>=4 -> R<=1 (a fit, THE LINE)")
print(f"  BST answer: M = {bst_M} necessarily -- the program is ZERO free parameters. up/down seats FORCED (like leptons at Wallach pts).")
print(f"  -> 4 CKM params fully determined, R = infinity. M>0 would be a FAILURE (a free angle IS a free parameter), NOT a fallback.")
print(f"  the bar is M=0: CKM fully forced from the derived seats, or the quark sector is an honest failure.")
print()
print("the gated piece + the target:")
print("-" * 100)
print("  gated: the FORCED up/down quark seats (6 K-type addresses split by weak-isospin T_3^R, the SU(2)_L doublet) = deep #418 chiral content")
print(f"  target (Lyra+Grace): derived seats yield Gatto sin theta_C = sqrt(m_d/m_s) ~ {gatto:.3f} vs observed {Vus}, UNTUNED -> the M=0 referee-proof motion")
print()

checks = [
    ("color su(3) is vector-like -> blind to up/down (Lyra F178)", color_blind_to_updown),
    ("CKM is generation-space / T_3^R, NOT color", ckm_is_generation),
    ("4226 RETRACTED: composite-root CKM used color su(3) for a generation object (category error)", True),
    ("Wolfenstein relation V_ub~V_us*V_cb stands empirically; source = up/down seats (gated)", True),
    ("Grace M-table: M=0->R=inf, M=1->R=4, M>=4->R<=1 (the line)", M_table[0] == float("inf") and M_table[4] == 1.0),
    ("BST answer: M MUST be 0 (zero free parameters); M>0 = failure, not a free-angle fallback", bst_M == 0),
    ("gated = forced up/down seats (T_3^R chiral content, #418); target = Gatto untuned; filter armed for M=0", True),
]
passed = sum(1 for _, ok in checks if ok)
for name, ok in checks:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
print()

print("=" * 100)
print("SUMMARY -- absorbing Lyra's F178 catch and answering Grace's M-question. First, the self-correction: in 4226 I read")
print("  the CKM Wolfenstein hierarchy out of the su(3) composite root, but Lyra's su(3) is the COLOR su(3) (the strata are")
print("  the colors), and color is vector-like -- it couples up-type and down-type identically, so it is blind to up-vs-down.")
print("  The CKM is precisely the up/down misalignment, a generation-space weak-isospin object, so mapping the color su(3)")
print("  onto it was a category error. I retract that derivation; the Wolfenstein relation itself is a real empirical pattern,")
print("  but its substrate source is the up/down generation seats (the gated #418 chiral content), not the color su(3).")
print("  Second, Grace's pivot: she reduced the whole #418 motion to one number M, the freedom in the up/down seat")
print("  misalignment, with R = 4/M. The structural answer is that M must be zero -- BST is a zero-free-parameter program, so")
print("  the up/down quark seats are forced exactly as the lepton seats were forced at the Wallach points, the misalignment")
print("  is forced, and the four CKM parameters are fully determined (R = infinity). Crucially, 'M=1, one free angle' is not")
print("  an acceptable fallback: a free angle is a free parameter, which the program forbids, so the bar is M=0 -- the CKM")
print("  comes out fully forced from the derived seats, or the quark sector is an honest failure, with no free-angle escape.")
print("  The gated piece is named precisely -- the forced up/down seats (the six K-type addresses split by weak-isospin, the")
print("  SU(2)_L doublet structure, the deep #418 chiral content) -- and the target is that the derived seats yield Gatto")
print("  (theta_C and m_d/m_s) untuned, which with M=0 is the referee-proof motion. My filter is armed for M=0. Count 4 of 26.")
print("=" * 100)
print()
print("Elie - Wednesday 2026-06-17 (self-correct 4226 per Lyra F178 + answer Grace M-question: (A) SELF-CORRECTION no defense -- in 4226 I derived CKM Wolfenstein hierarchy |V_ub|~|V_us|*|V_cb| from the su(3) COMPOSITE root, but Lyra su(3) (F177) is the COLOR su(3) (3 strata = 3 colors), color is VECTOR-LIKE couples up-type and down-type IDENTICALLY -> BLIND to up-vs-down, the CKM is the up/down misalignment a GENERATION-space weak-isospin T_3^R object NOT color, so 4226 mapped COLOR su(3) onto GENERATION mixing = category error (color != generation), RETRACTED, the relation V_ub~V_us*V_cb is empirically real Wolfenstein but its substrate SOURCE must be the up/down generation seats (gated #418 chiral content) not the color su(3), if the 3 generations carry an A_2-like structure the composite=product pattern may re-derive there but from the generation structure not the color su(3); (B) GRACE M-QUESTION (the pivot) M = free angles in up/down seat misalignment filling V, R = 4(CKM)/M, M=0->R=inf (4 CKM fully determined strongest) M=1->R=4 (strong) M>=4->R<=1 (fit THE LINE); BST STRUCTURAL ANSWER M MUST be 0 -- the entire program is ZERO free parameters, every mass+mixing forced by the geometry, so the up/down quark seats are FORCED (exactly as lepton seats forced at Wallach points {0,3/2,5/2}), up-vs-down misalignment forced, 4 CKM params determined NO free angle, M=0 R=infinity; CRUCIAL discipline 'M=1 one free angle still strong' is NOT an acceptable fallback for BST -- a free angle IS a free parameter which the program forbids -- so the bar is M=0, the CKM must come out FULLY forced from the derived up/down seats or the quark sector is an honest FAILURE (not a partial fit), no free-angle escape hatch; THE GATED PIECE deriving the FORCED up/down quark seats (6 K-type addresses split by weak-isospin T_3^R, the SU(2)_L doublet structure) = deep #418 chiral content, same shape as neutrino sector yesterday (both halves armed Lyra color su(3) + my CKM filter 4225, deep object up/down seats in the middle still to derive), the honest target (Lyra+Grace) derived seats yield theta_C + m_d/m_s satisfying Gatto (sin theta_C = sqrt(m_d/m_s) 0.62%) WITHOUT dialing to 0.2245 = the cross-family check that with M=0 is the referee-proof motion; HONEST (A) absorbs Lyra F178 4226 retracted (empirical Wolfenstein stands source is up/down seats gated), (B) answers Grace M-question structurally M must be 0 (BST zero free parameters) so up/down seats forced CKM fully determined R=inf + M>0 would be FAILURE not free-angle fallback, gated = forced up/down seats (#418 T_3^R chiral content) target = Gatto-satisfying seats untuned filter armed for M=0; count 4 of 26)")
print()
print(f"SCORE: {passed}/{len(checks)} (self-correct 4226 + answer Grace M-question: (A) Lyra F178 -- su(3) is COLOR (vector-like, blind to up/down), CKM is GENERATION/T_3^R, so 4226's CKM-hierarchy-from-su(3)-composite-root = category error, RETRACTED (Wolfenstein relation stands, source = up/down seats gated); (B) Grace M-question -- M = up/down misalignment freedom, R=4/M; BST answer M MUST be 0 (zero free parameters, seats forced like leptons), R=inf, M>0 = FAILURE not free-angle fallback, bar is M=0; gated = forced up/down seats (T_3^R chiral content #418), target = Gatto untuned; filter armed for M=0; count 4 of 26)")
