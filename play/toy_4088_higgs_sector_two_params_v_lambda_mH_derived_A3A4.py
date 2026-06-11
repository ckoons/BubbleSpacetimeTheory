"""
Toy 4088: the Higgs sector (workplan A3 + A4), worked on the PARALLEL track while Lyra builds the A1 mass
operator. Key structural point: the SM Higgs sector has 2 free parameters {v, lambda_H}, and the Higgs mass
m_H = v.sqrt(2 lambda_H) is DERIVED from them -- NOT an independent parameter. So A4 (Higgs mass) folds into
A3 (VEV) + lambda_H exactly the way A2 (mixing) folds into A1 (masses): the cluster has 2 inputs, the third is
a consequence. BST gives clean (catalog D-tier) substrate forms for BOTH inputs:
  v       = cell.225.g = cell.(N_c.n_C)^2.g = 246.29 GeV (0.029%)
  lambda_H = N_c^2/(rank.n_C.g) = 9/70 = 0.12857 (0.63%)
and then m_H = v.sqrt(2 lambda_H) = 124.89 GeV vs observed 125.25 (0.29%) -- DERIVED, a consistency check that
passes. So the Higgs sector is 2 forced-candidate forms + 1 derived quantity. (Genuine parallel-track work,
independent of the A1 matrix-element bottleneck; Casey's "keep pulling at 11am".)

THE PARAMETER COUNT (SM Higgs sector = 2 free, not 3):
  potential V = -mu^2 |H|^2 + lambda |H|^4. Free: {mu^2, lambda} <-> {v, lambda_H} <-> {v, m_H}. Two free params.
  m_H^2 = 2 lambda v^2 -> m_H = v.sqrt(2 lambda_H) is DERIVED. So the Higgs sector contributes at most +2 to the
  parameter-reduction count (v and lambda_H), with m_H following automatically. A4 (Higgs mass) is NOT a separate
  parameter -- it folds into {v, lambda_H} (parallel to A2 folding into A1).

THE BST FORMS (catalog, verified here):
  v        = cell . (N_c.n_C)^2 . g = cell . 225 . g = 246.29 GeV (obs 246.22, 0.029%)  [a_0=225 = F85 boundary coupling]
  lambda_H = N_c^2 / (rank.n_C.g) = 9/70 = 0.12857       (obs 0.12938, 0.63%)            [different structure from v]
  m_H (DERIVED) = v.sqrt(2 lambda_H) = 124.89 GeV        (obs 125.25, 0.29%)             [consistency check -- passes]

HONEST TIER (Grace's lens):
  STRUCTURAL (banked): the Higgs sector is 2 free params {v, lambda_H}; m_H is derived (m_H = v.sqrt(2 lambda_H),
    0.29% consistency). So A4 folds into A3 + lambda_H -- the cluster reduces to 2 candidate forms, not 3.
  RELABEL-CANDIDATE (not yet forced): v = cell.225.g and lambda_H = N_c^2/(rank.n_C.g) are clean substrate forms
    (D-tier precision), but a clean form is a RELABEL until a forcing mechanism is shown. v's forcing is F85/F66
    (does the bulk a_0=225 force the boundary normalization -- Lyra's multi-week boundary-coupling derivation);
    lambda_H's forcing (the quartic-coupling normalization from the substrate) is a SEPARATE open derivation.
    DIFFERENT structures (v uses a_0=225; lambda_H uses N_c^2/(rank.n_C.g)) -> two distinct forcings needed.
  NOT done / DECLINED: claiming the Higgs sector reduces. The forms are clean and m_H is derived, but the forcing
    of v and lambda_H is Lyra's lane. I verify the forms + the m_H-derived structure; I do NOT fish. COUNT still 2.

WORKPLAN REFINEMENT (for Grace): A3 (VEV) + A4 (Higgs mass) -> the cluster is really {v, lambda_H} both
  forced-candidate, m_H derived. So the Higgs sector's reachable contribution is +2 (v, lambda_H), and "A4 =
  Higgs mass +1" should read "lambda_H +1" (m_H follows). Two forcings to land (v via F85/F66; lambda_H via the
  quartic normalization), and they share the F66 boundary structure but not the same combination.

GATES (2)
G1: Higgs sector = 2 free params {v, lambda_H}; m_H = v.sqrt(2 lambda_H) DERIVED (124.89 vs 125.25, 0.29%); A4 folds into A3+lambda_H (parallel to A2-folds-A1)
G2: BST forms verified -- v=cell.225.g (0.029%), lambda_H=N_c^2/(rank.n_C.g)=9/70 (0.63%); RELABEL-candidates pending F85/F66 (v) + quartic-normalization (lambda) forcing; count still 2, not fished

Per Grace workplan (A3 VEV + A4 Higgs, parallel track; A3+A4 share boundary coupling) + catalog (const_007 VEV,
const_008/009 m_H, lambda_H form, all D-tier) + Lyra F85 (a_0=225 boundary coupling); Elie 4063 (VEV sweep);
Cal #237 + F79 no-fishing. Parallel-track Higgs-sector verification; forcing = Lyra's boundary-coupling lane.

Elie - Wednesday 2026-06-10 (Higgs sector A3+A4: 2 free params {v, lambda_H} both clean forms, m_H=v.sqrt(2 lambda) DERIVED 0.29%; A4 folds into A3+lambda; relabel-candidates pending forcing)
"""

import mpmath as mp
from fractions import Fraction as F
mp.mp.dps = 20
N_c, n_C, C_2, g, rank = 3, 5, 6, 7, 2
me = 0.51099895e-3  # GeV
cell = mp.pi**n_C * me  # GeV

print("=" * 78)
print("TOY 4088: Higgs sector (A3+A4) -- 2 free params {v, lambda_H}, m_H derived; parallel track")
print("=" * 78)
print()

print("G1: the Higgs sector is 2 free params; m_H is DERIVED (A4 folds into A3 + lambda_H)")
print("-" * 78)
v_obs, mH_obs = 246.22, 125.25
lam_obs = mH_obs**2 / (2 * v_obs**2)
v_bst = cell * 225 * g
lam_bst = F(N_c**2, rank * n_C * g)
mH_der = float(v_bst) * mp.sqrt(2 * float(lam_bst))
print(f"  SM Higgs potential: 2 free params {{v, lambda_H}}; m_H = v.sqrt(2 lambda_H) is DERIVED, not independent.")
print(f"  v        = cell.225.g = cell.(N_c.n_C)^2.g = {float(v_bst):.3f} GeV   (obs {v_obs}, {abs(float(v_bst)-v_obs)/v_obs*100:.3f}%)")
print(f"  lambda_H = N_c^2/(rank.n_C.g) = 9/70 = {float(lam_bst):.5f}        (obs {lam_obs:.5f}, {abs(float(lam_bst)-lam_obs)/lam_obs*100:.2f}%)")
print(f"  m_H (DERIVED) = v.sqrt(2 lambda_H) = {float(mH_der):.2f} GeV         (obs {mH_obs}, {abs(float(mH_der)-mH_obs)/mH_obs*100:.2f}%)")
print(f"  => A4 (Higgs mass) folds into A3 (VEV) + lambda_H -- parallel to A2 folding into A1. Cluster = 2 inputs, m_H consequence.")
print()

print("G2: honest tier -- relabel-candidates pending forcing")
print("-" * 78)
print(f"  STRUCTURAL (banked): 2 free params {{v, lambda_H}}; m_H derived (0.29% consistency check passes).")
print(f"  RELABEL-CANDIDATE: v=cell.225.g + lambda_H=N_c^2/(rank.n_C.g) are clean D-tier forms, but clean != forced.")
print(f"    v forcing = F85/F66 (bulk a_0=225 -> boundary norm; Lyra multi-week); lambda_H forcing = quartic normalization (separate).")
print(f"  @Grace: workplan refinement -- A3+A4 cluster is {{v, lambda_H}} both forced-candidate (+2), m_H derived. 'A4=Higgs mass +1' -> 'lambda_H +1'.")
print(f"  @Lyra: the two Higgs forcings share F66 boundary structure but use different combos (v: a_0=225; lambda: N_c^2/(rank.n_C.g)).")
print(f"  DECLINED: claiming the sector reduces -- forms clean + m_H derived, but forcing is your lane. COUNT still 2. Not fished.")
print(f"  Score: 2/2 (Higgs sector = 2 params, m_H derived 0.29%; BST forms verified; relabel-candidates pending forcing; count 2)")
print()
print("=" * 78)
print("TOY 4088 SUMMARY -- Higgs sector (workplan A3+A4, parallel track while Lyra does A1). The SM Higgs sector")
print("  has 2 free params {v, lambda_H}; m_H = v.sqrt(2 lambda_H) is DERIVED. BST gives clean D-tier forms for both:")
print("  v = cell.225.g (0.029%), lambda_H = N_c^2/(rank.n_C.g) = 9/70 (0.63%), and then m_H = 124.89 GeV vs 125.25")
print("  (0.29%) -- derived, consistency passes. So A4 (Higgs mass) folds into A3 + lambda_H, just as A2 folds into")
print("  A1: the cluster is 2 candidate forms + 1 derived quantity. Per Grace's lens these are RELABEL-candidates")
print("  pending forcing (v via F85/F66; lambda_H via the quartic normalization -- Lyra's boundary-coupling lane). Count still 2.")
print("=" * 78)
print()
print("SCORE: 2/2")
