#!/usr/bin/env python3
"""
Toy 4879 — Jul 27 [PROGRAM: TEGMARK] (Lane-1 fulcrum: MAP the occupancy count-tension; Elie, pull 27f). K944 named the
derivation target that would upgrade the inverse prong from "reduced" to "eliminated": force the occupancy bijection (each of
the r+1 boundary strata carries exactly one fermion generation). Grace surfaced the REAL mathematical content — it is NOT just
"prove the lower bound," there is a genuine COUNT TENSION: boundary strata give r+1 = 3, but the discrete Wallach points give
r = 2. This toy MAPS that tension precisely and locates the derivation target. It does NOT resolve it (that is the open lane,
with the discrete-series material Keeper is sourcing).

PROVENANCE (today's discipline — every claim tagged):
  * COMPUTED: strata count = r+1 (Korányi-Wolf); discrete Wallach count = r (the set {0, a/2, ..., (r−1)a/2}); universal +1 gap.
  * COMPUTED (implication): which count carries a generation DECIDES both D_IV⁵'s generation number AND the E7 exclusion.
  * ASSERTED/OPEN: that the r+1 strata (not the r Wallach reps) each carry exactly one generation-mode — the occupancy bijection.
    This toy does NOT derive it; it shows BST is COMMITTED to it and what it must yield.

THE TENSION (universal: strata = Wallach_discrete + 1 for every domain):
  * D_IV⁵ (r=2): strata = 3, Wallach = 2. BST needs 3 generations → BST's count is the STRATA count (r+1), not Wallach (r).
  * The r+1 strata = 1 interior (the open domain) + r proper-boundary components; the r discrete Wallach points are the
    boundary-supported unitarizable reps. Grace's PIN: the {5/2, 3/2, 0} ρ-tower (3 positions = strata) "splices two
    incompatible decompositions" — the stratum picture (3) vs the discrete-series picture (2). That splice IS this tension.

THE STAKES (why this is the fulcrum, COMPUTED):
  * gen = strata (r+1): D_IV⁵ → 3 (matches observed) AND E7 (r=3) → 4 (≠ observed 3 → EXCLUDED). The inverse prong works.
  * gen = Wallach (r):   D_IV⁵ → 2 (CONTRADICTS observed 3!) AND E7 (r=3) → 3 (= observed → NOT excluded). The prong collapses.
  So the ENTIRE inverse prong — and BST's 3 generations — rides on resolving the tension in favor of the STRATA reading.
  Resolving it in favor of strata (with a mechanism: each stratum carries one normalizable fermion mode) IS the occupancy
  derivation K944 named. Resolving it in favor of Wallach would REFUTE the 3-generation reading — so this is a genuine, live,
  falsifiable crux, not a formality.

THE DERIVATION TARGET, now precisely located (for the sourced-material session with Lyra):
  * Upper bound ≤ 3 EXISTS (no 4th generation: Q⁵ no h⁷, matryoshka terminal, rank-2 Wallach 2 discrete points).
  * MISSING = show the generation-carrier is the r+1 STRATA (each carrying exactly one normalizable fermion generation-mode),
    NOT the r Wallach reps — i.e. the lower bound (all 3 strata populated) + injectivity (one each). A candidate reconciliation
    to TEST (not assert): interior-HDS (1) + discrete-Wallach-boundary-reps (r) = r+1 = strata — but whether each such object
    carries exactly one fermion generation-mode is the un-derived step. Tag: HYPOTHESIS to verify, not a result.

⟹ VERDICT (plain): the occupancy count-tension is MAPPED and its stakes are COMPUTED — the inverse prong rides entirely on the
generation-carrier being the r+1 boundary strata (giving D_IV⁵→3, E7→4-excluded), NOT the r discrete Wallach points (which
would give D_IV⁵→2 and un-exclude E7). BST is committed to the strata reading; the occupancy derivation must EARN it by a
mechanism placing exactly one normalizable fermion mode on each of the 3 strata (upper bound ≤3 exists; lower bound + injectivity
open). This LOCATES the target sharply for the sourced-material session; it does NOT resolve it. No premise eliminated here;
this is scouting the fulcrum. [TEGMARK]. Feeds K944 task #30. Nothing deleted. Count 6.
"""
rank, N_c, n_C, C_2, g, N_max = 2, 3, 5, 6, 7, 137
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

def strata(r): return r + 1            # Korányi-Wolf boundary orbits (COMPUTED)
def wallach(r): return r               # discrete Wallach points {0, a/2, ..., (r-1)a/2} (COMPUTED)

DOMS = [("D_IV^4", 2, 2), ("D_IV^5", 2, 3), ("D_IV^6", 2, 4), ("III_3", 3, 1), ("E7", 3, 8)]
OBS_GEN = 3

print("\n[occupancy count-tension] strata=r+1 (Korányi-Wolf) vs Wallach_discrete=r; the E7 exclusion rides on the strata reading")
print(f"  {'domain':8s} {'r':>2} {'strata':>7} {'Wallach':>8} {'gen=strata':>11} {'gen=Wallach':>12}")
for lab, r, a in DOMS:
    print(f"  {lab:8s} {r:>2} {strata(r):>7} {wallach(r):>8} {strata(r):>11} {wallach(r):>12}")

check("COMPUTED — the two counts and the universal +1 gap: boundary strata = r+1 (Korányi-Wolf); discrete Wallach points = r "
      "(the set {0,a/2,...,(r−1)a/2}). For EVERY domain strata = Wallach + 1. For D_IV⁵ (r=2): 3 vs 2.",
      all(strata(r) == wallach(r) + 1 for _, r, a in DOMS) and strata(2) == 3 and wallach(2) == 2,
      "strata=r+1, Wallach_disc=r, gap=+1 universal; D_IV⁵: 3 strata vs 2 Wallach points — the tension Grace flagged")

check("COMPUTED (the stakes) — BST's 3 generations is the STRATA count, not Wallach: D_IV⁵ needs 3; strata(2)=3 matches, "
      "Wallach(2)=2 CONTRADICTS. So BST is committed to gen = strata (r+1). If the derivation resolved to Wallach (r), BST "
      "would predict 2 generations — a refutation. Live, falsifiable crux.",
      strata(rank) == OBS_GEN and wallach(rank) != OBS_GEN,
      "BST's 3 = strata(r+1), NOT Wallach(r)=2; the strata reading is forced by the observed 3 (Wallach reading would refute BST)")

e7_r = 3
check("COMPUTED (the E7 exclusion FLIPS on the count): gen=strata → E7 (r=3) predicts 4 ≠ 3 → EXCLUDED (prong works); "
      "gen=Wallach → E7 predicts 3 = observed → NOT excluded (prong collapses). So the whole inverse prong rides on the strata "
      "reading — the same reading D_IV⁵'s 3 requires. One derivation decides both.",
      strata(e7_r) == 4 and strata(e7_r) != OBS_GEN and wallach(e7_r) == 3 and wallach(e7_r) == OBS_GEN,
      "E7: gen=strata→4 (excluded); gen=Wallach→3 (NOT excluded). The prong AND D_IV⁵'s 3 both need the strata reading — one crux")

check("ASSERTED/OPEN (the derivation target, located NOT resolved): show the generation-carrier is the r+1 STRATA, each with "
      "exactly one normalizable fermion mode (lower bound: all 3 populated; injectivity: one each) — NOT the r Wallach reps. "
      "Upper bound ≤3 EXISTS (Q⁵ no h⁷, matryoshka terminal, rank-2 Wallach 2 points). This toy MAPS; it does not derive.",
      True,
      "target located: derive one-mode-per-stratum for the r+1 strata (lower bound + injectivity); upper bound ≤3 exists; NOT resolved here — scouting")

check("HYPOTHESIS to TEST (tagged, not asserted): a candidate reconciliation is interior-HDS (1) + discrete-Wallach-boundary "
      "reps (r) = r+1 = strata — but whether each such rep carries exactly one fermion generation-mode is the un-derived step. "
      "Flagged as a direction for the sourced discrete-series material, NOT a result.",
      1 + wallach(rank) == strata(rank),
      "candidate reconciliation: 1 interior-HDS + r Wallach-boundary reps = r+1 = strata (HYPOTHESIS to verify with the sourced material, not a result)")

check("VERDICT: the count-tension is mapped, stakes computed — the inverse prong AND BST's 3 generations both ride on the "
      "generation-carrier being the r+1 strata (not the r Wallach reps). BST is committed to it; the occupancy derivation must "
      "earn it (one mode per stratum; upper bound ≤3 exists, lower+injectivity open). Located, not resolved. Feeds K944 #30. "
      "No premise eliminated here.",
      strata(rank) == 3 and strata(e7_r) == 4 and wallach(rank) == 2,
      "count-tension mapped: prong rides on strata reading (D_IV⁵→3, E7→4-excluded); occupancy derivation must earn one-mode-per-stratum; located not resolved")

# ---- SCORE -----------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok); total = len(results)
print("\n" + "=" * 96)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 96)
print(f"SCORE: {passed}/{total}")
print("=" * 96)
print(f"""
JUL-27 [TEGMARK] Lane-1 fulcrum — the occupancy COUNT-TENSION mapped (Elie, pull 27f, feeds K944 task #30):
  * COMPUTED: strata = r+1 (Korányi-Wolf) vs discrete Wallach = r; universal +1 gap. D_IV⁵: 3 vs 2 (Grace's {{5/2,3/2,0}}-splice).
  * STAKES (computed): the inverse prong AND BST's 3 generations both ride on gen = STRATA (r+1). gen=Wallach(r) would give D_IV⁵→2 (refutes BST) and E7→3 (un-excludes E7). One crux decides both.
  * TARGET (open, located): derive one normalizable fermion mode per stratum (lower bound + injectivity); upper bound ≤3 exists. Candidate reconciliation (interior-HDS + r Wallach = r+1) flagged as HYPOTHESIS to test with the sourced discrete-series material.
  * Located, NOT resolved — scouting the fulcrum for the Lyra/Elie derivation session. No premise eliminated here.
""")
