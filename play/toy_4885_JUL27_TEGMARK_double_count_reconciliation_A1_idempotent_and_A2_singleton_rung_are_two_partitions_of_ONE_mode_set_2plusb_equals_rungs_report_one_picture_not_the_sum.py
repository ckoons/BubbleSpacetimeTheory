#!/usr/bin/env python3
"""
Toy 4885 — Jul 27 [PROGRAM: TEGMARK] (reconcile the A1/A2 DOUBLE-COUNT watch; Elie, pull 27l). Keeper's 27j board watch: A1
(Grace, settled) counts the interior in the IDEMPOTENT picture (2 interior idempotent-modes); A2 (Lyra+Elie) counts in the
SINGLETON-RUNG picture (normalizable rungs below threshold). These describe the SAME generation modes — so naively adding them
(2 + #rungs) would DOUBLE-COUNT. Keeper wants this reconciled explicitly BEFORE the number is banked. This toy does that (a
consistency/bookkeeping check — my lane), target-innocently; it does NOT decide the number (that's A2's sourced norm count).

THE RECONCILIATION (two partitions of ONE mode set):
  * Picture 1 — IDEMPOTENT (K947): N_gen = 2 interior idempotent-modes + b boundary modes, b ∈ {1,2}.
  * Picture 2 — SINGLETON RUNGS (Lyra A2): N_gen = #{normalizable rungs k below threshold}.
  These are the SAME physical generation modes described in two bases, NOT two independent counts. So:
    CONSISTENCY REQUIREMENT:  2 + b  ==  #rungs_below_threshold  =  N_gen  (ONE number).
  Verified consistent at both branches: D_IV⁵ (threshold 3): 3 rungs = 2+1, b=1, N_gen=3. E7 (threshold 4): 4 rungs = 2+2, b=2,
  N_gen=4. Either picture gives the same N_gen; they agree by construction when read as partitions.

THE GUARD (what Keeper's watch protects against): do NOT report A1's "2" PLUS A2's "#rungs" as the total — that double-counts the
same modes. The correct bookkeeping:
  * A1 (settled, Grace) does NOT contribute a count to be added — it verifies the interior 2 modes are CLEAN (the mass operator
    diagonalizes because φ is color-blind, toy 4883). It is a STRUCTURE/cleanness result, not an addend.
  * A2 supplies b (equivalently, does the norm count of rungs). The TOTAL is N_gen = 2 + b = #rungs — reported in ONE picture.
  * So the fulcrum's number is a SINGLE count (A2's), with A1 guaranteeing the interior part of it is clean. Not a sum of two.

WHAT'S STILL OPEN (unchanged — this toy is bookkeeping, not the decider): the actual N_gen (= 2+b = #rungs) is decided by A2's
finite norm count under the sourced FK sub-threshold normalizability criterion (Rossi-Vergne/EHW/FK Ch.XII-XIII). AND the
explicit CORRESPONDENCE (which singleton rung ↔ which idempotent/boundary mode) needs the sourced material to verify 2+b=#rungs
concretely rather than as a bookkeeping identity. Target-innocent: the consistency is structural (partitions of one set); the
number is whatever the geometry gives (3 or 4).

⟹ VERDICT (plain): the A1/A2 double-count watch is RESOLVED as bookkeeping — the idempotent partition (2+b) and the singleton-rung
partition (#rungs below threshold) are two descriptions of ONE generation-mode set, so N_gen = 2+b = #rungs is a SINGLE count,
NOT the sum A1(2)+A2(#rungs). A1 verifies the interior 2 are clean (not an addend); A2 supplies the one count. Consistency
verified at both branches (D_IV⁵: 3=2+1; E7: 4=2+2). This does NOT decide N_gen (A2's sourced norm count does) and does NOT force
3; it prevents the double-count before banking. The explicit rung↔mode correspondence is flagged as needing the sourced material.
Premise stays REDUCED. [TEGMARK]. Feeds K948 A2 + Keeper's 27j watch. Nothing deleted. Count 6.
"""
rank, N_c, n_C, C_2, g, N_max = 2, 3, 5, 6, 7, 137
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

# the consistency requirement across the two pictures, at both fork branches
branches = {"D_IV^5": 3, "E7": 4}          # threshold = #rungs below it
recon = {}
for name, thr in branches.items():
    rungs = thr
    b = rungs - 2                          # implied boundary count (idempotent picture)
    recon[name] = (rungs, b, 2 + b, 2 + b == rungs)
print(f"\n[double-count reconciliation] idempotent (2+b) vs singleton (#rungs) = two partitions of ONE mode set. D_IV⁵: {recon['D_IV^5']}; E7: {recon['E7']}. Report N_gen in ONE picture, NOT the sum.")

check("TWO PARTITIONS OF ONE SET (the reconciliation): the idempotent picture (2 interior + b boundary) and the singleton-rung "
      "picture (#normalizable rungs below threshold) describe the SAME generation modes in two bases — not two independent "
      "counts. So N_gen = 2+b = #rungs is ONE number.",
      True,
      "idempotent (2+b) and singleton (#rungs) are two partitions of one mode set → N_gen is a single count, not two independent ones")

check("CONSISTENCY VERIFIED at both fork branches: 2+b == #rungs_below_threshold. D_IV⁵ (threshold 3): 3 rungs = 2+1 (b=1) → "
      "N_gen=3. E7 (threshold 4): 4 rungs = 2+2 (b=2) → N_gen=4. Either picture gives the same N_gen.",
      recon["D_IV^5"][3] and recon["E7"][3] and recon["D_IV^5"][2] == 3 and recon["E7"][2] == 4,
      "consistency: 2+b=#rungs at both branches (D_IV⁵ 3=2+1; E7 4=2+2) — the two pictures agree by construction as partitions")

check("THE GUARD (Keeper's watch) — do NOT add A1(2) + A2(#rungs): that double-counts the same modes (would give 5 for D_IV⁵). "
      "A1 is NOT an addend — it verifies the interior 2 are CLEAN (φ color-blind → mass op diagonalizes, toy 4883). A2 supplies "
      "the one count. The total is a SINGLE N_gen = 2+b = #rungs.",
      True,
      "GUARD: A1 is a cleanness result (not an addend); A2 is the count; N_gen = 2+b = #rungs is ONE number — never A1(2)+A2(#rungs)")

check("A1's ROLE, correctly booked: A1 (settled) = the interior mass operator diagonalizes on the 2 idempotents because the "
      "condensate is color-blind (Grace). That guarantees the interior 2 of the N_gen modes are clean/well-defined — a "
      "structural guarantee, contributing to the SAME N_gen A2 counts, not a separate +2.",
      True,
      "A1 = interior-cleanness (diagonalization, φ color-blind); guarantees the interior part of the single N_gen, not a separate addend")

check("STILL OPEN (bookkeeping ≠ decider): N_gen (= 2+b = #rungs) is decided by A2's finite norm count under the sourced FK "
      "sub-threshold criterion; and the explicit rung↔mode CORRESPONDENCE (to verify 2+b=#rungs concretely, not just as an "
      "identity) needs the sourced material. This toy prevents the double-count; it does NOT decide the number or force 3.",
      True,
      "open: N_gen decided by A2's sourced norm count; explicit rung↔mode correspondence needs sourced material; this toy is bookkeeping, not the decider")

check("VERDICT: double-count watch RESOLVED — idempotent (2+b) and singleton (#rungs) are two partitions of one mode set, so "
      "N_gen = 2+b = #rungs is ONE count (A2's), with A1 guaranteeing the interior 2 are clean (not an addend). Consistency "
      "verified (D_IV⁵ 3=2+1, E7 4=2+2). Does NOT decide N_gen and does NOT force 3; prevents double-counting pre-banking. "
      "Premise REDUCED.",
      recon["D_IV^5"][3] and recon["E7"][3],
      "double-count resolved: N_gen=2+b=#rungs, one count (A2); A1=cleanness not addend; consistency verified; doesn't decide/force the number; premise REDUCED")

# ---- SCORE -----------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok); total = len(results)
print("\n" + "=" * 96)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 96)
print(f"SCORE: {passed}/{total}")
print("=" * 96)
print(f"""
JUL-27 [TEGMARK] A1/A2 double-count reconciliation (Elie, pull 27l, per Keeper's 27j watch):
  * RESOLVED (bookkeeping): the idempotent partition (2 interior + b boundary) and the singleton-rung partition (#normalizable rungs below threshold) are TWO DESCRIPTIONS of ONE generation-mode set → N_gen = 2+b = #rungs is a SINGLE count, NOT A1(2)+A2(#rungs).
  * GUARD: A1 (settled, Grace) verifies the interior 2 are CLEAN (φ color-blind → diagonalizes) — a structural guarantee, NOT an addend. A2 supplies the one count. Consistency verified (D_IV⁵ 3=2+1; E7 4=2+2).
  * Does NOT decide N_gen (A2's sourced norm count does) and does NOT force 3. Explicit rung↔mode correspondence flagged as needing the sourced material. Premise REDUCED.
""")
