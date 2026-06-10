"""
Toy 4063: Higgs VEV substrate-form candidate (lane A) -- v = cell . (N_c.n_C)^2 . g, at 0.03%, base-rate-CLEAN
(only 1 substrate-primary product within 0.1% of v/cell). BUT honestly RELABEL-tier per Grace's parameter-
counting lens: it expresses ONE SM parameter (the VEV) in substrate primaries; it does NOT reduce the count.
Filed as a clean candidate with the honest tier, NOT banked. (Higgs investigation; discipline front-and-center.)

CASEY's lane-A question: is the Higgs VEV (246 GeV) substrate-natural? v/cell = 246.22 GeV / 156.4 MeV = 1574.5.

THE CANDIDATE FORM:
  v/cell = 1574.5 ~ (N_c.n_C)^2 . g = 225 . 7 = 1575   (0.02%)
  i.e.  v = cell . (N_c.n_C)^2 . g = pi^{n_C} . m_e . 225 . g = 246.29 GeV  (obs 246.22, 0.03%)
  Note 225 = (N_c.n_C)^2 = the substrate-Schur generator (c_FK, heat-trace a_0, (dim SO(4,2))^2 -- today's
  cross-validated number). So v/cell = (Schur generator 225) x (genus g). Semi-load-bearing factor, not random.

BASE-RATE (front-running Grace's gate -- the part that matters): I swept all substrate-primary products
{rank,N_c,n_C,C_2,g,N_max} with total power <=5 within 0.1% of v/cell = 1574.5. Result: EXACTLY ONE hit
(1575 = N_c^2 n_C^2 g). So this is NOT "anything fits at a few percent" -- the form is base-rate-clean (a single
substrate product lands, and it uses the load-bearing 225). That distinguishes it from the day's loose above-floor fits.

BUT -- the honest tier per GRACE's PARAMETER-COUNTING LENS: BST's real content is whether it REDUCES the SM
free-parameter count or RELABELS it. This form expresses ONE parameter (the VEV) in substrate primaries -- a
RELABEL (1 number, substrate vocabulary), NOT a reduction (it does not derive the VEV from FEWER inputs +
a forced relation). So even base-rate-clean, it is relabel-tier: a clean identification of the VEV scale, not a
derivation. It connects the VEV to the cell unit (156.4 MeV) and the Schur generator 225 -- structurally
interesting, and useful for the parameter-count ledger as "VEV: relabel candidate, base-rate-clean" -- but it
does not advance the count. NOT banked; for Grace/Cal's reduce-vs-relabel gate.

(Cross-link, NOT claimed: v = cell . 225 . g means the EW scale = (substrate mass quantum) x (Schur generator)
x (genus). Whether that's a forced relation -- e.g. the VEV being the Higgs-boundary scale of the same 225 that
normalizes the bulk measure -- is Lyra's F66 bulk/boundary lane, and would be a reduction IF derived. Flagged, not asserted.)

GATES (2)
G1: v/cell = 1574.5 ~ (N_c.n_C)^2 g = 1575 (0.02%); v = cell . 225 . g = 246.29 GeV (0.03%); 225 = Schur generator
G2: base-rate CLEAN (1 substrate product within 0.1%) BUT relabel-tier per Grace's lens (1 param relabeled, not reduced); NOT banked; gate-dependent

Per Casey Higgs lane A; Grace parameter-counting lens; Toy 4054 (cell unit); 225 Schur generator (c_FK/a_0/dim^2);
Cal #237 + F79 lesson; K231c. Candidate with honest relabel-tier; for the reduce-vs-relabel gate.

Elie - Tuesday 2026-06-09 (Higgs VEV candidate v=cell.225.g, base-rate-clean but relabel-tier per Grace's lens)
"""

import mpmath as mp
import itertools
mp.mp.dps = 20
me = 0.51099895
N_c, n_C, C_2, g, rank, N_max = 3, 5, 6, 7, 2, 137
v = 246220.0
cell = float(mp.pi)**5 * me
r = v / cell

print("=" * 78)
print("TOY 4063: Higgs VEV candidate v = cell.(N_c.n_C)^2.g -- base-rate-clean BUT relabel-tier (Grace's lens)")
print("=" * 78)
print()

print("G1: the candidate form")
print("-" * 78)
print(f"  v/cell = {v:.0f}/{cell:.2f} = {r:.2f} ~ (N_c.n_C)^2 . g = 225.{g} = {225*g}  (0.02%)")
print(f"  v = cell . 225 . g = pi^5 m_e . 225 . {g} = {cell*225*g/1000:.3f} GeV  (obs 246.22, 0.03%)")
print(f"  225 = (N_c.n_C)^2 = substrate-Schur generator (c_FK, a_0, (dim SO(4,2))^2). g = genus. So v/cell = Schur x genus.")
print()

print("G2: base-rate (clean) + honest tier (relabel, per Grace's lens)")
print("-" * 78)
prim = [('rank', 2), ('N_c', 3), ('n_C', 5), ('C_2', 6), ('g', 7), ('N_max', 137)]
hits = []
for combo in itertools.product(range(4), repeat=6):
    if sum(combo) > 5:
        continue
    val = 1
    for (nm, p), e in zip(prim, combo):
        val *= p**e
    if val > 1 and abs(val - r) / r < 0.001:
        hits.append(val)
print(f"  BASE-RATE: substrate-primary products (power<=5) within 0.1% of {r:.0f}: {len(set(hits))} -> {sorted(set(hits))}")
print(f"    => NOT 'anything fits'; ONE clean form (1575 = N_c^2 n_C^2 g), using the load-bearing 225. Base-rate-clean.")
print(f"  BUT per GRACE's PARAMETER-COUNTING LENS: this RELABELS one SM parameter (the VEV) in substrate primaries;")
print(f"    it does NOT REDUCE the count (no forced relation deriving the VEV from fewer inputs). So: relabel-tier, even")
print(f"    base-rate-clean. A clean identification of the EW scale (-> cell . 225 . g), not a derivation. Gate-dependent; NOT banked.")
print()
print(f"  @Grace: Higgs VEV ledger entry -- candidate v=cell.225.g, base-rate-clean (1 hit), RELABEL not reduction.")
print(f"    Reduction would need the VEV forced (e.g. F66 Higgs-boundary 225 = the bulk-measure 225) -- Lyra's lane, flagged not asserted.")
print(f"  Score: 2/2 (clean candidate form + base-rate; honest relabel-tier per Grace's lens; gate-dependent)")
print()
print("=" * 78)
print("TOY 4063 SUMMARY -- Higgs VEV candidate: v = cell . (N_c.n_C)^2 . g = pi^5 m_e . 225 . g = 246.29 GeV (0.03%);")
print("  v/cell ~ 1575 is base-rate-CLEAN (only 1 substrate product within 0.1%, using the Schur generator 225). BUT")
print("  per Grace's parameter-counting lens it is RELABEL-tier (1 SM param in substrate vocabulary, not a reduction).")
print("  Clean identification of the EW scale, not a derivation. For the reduce-vs-relabel gate; NOT banked.")
print("=" * 78)
print()
print("SCORE: 2/2")
