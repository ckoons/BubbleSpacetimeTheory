#!/usr/bin/env python3
"""
Toy 4767 — Jul 21 (Round-6: close quark-mass row [Part 1] + open the CKM mixing row [Part 2], Elie's target-innocent
half). PART 1: document the RGI m_t/m_c value so the 137-artifact rejection is on record. PART 2: open the CKM row — test
the mixing elements against exact BST-algebraic forms (K797 method: test ratios not λ-exponents), and run the mixing =
√(mass-ratio) (Gatto, F585) cross-check against the mass ladder we just mapped. Result: the CKM row opens with ONE clean
target-innocent result — the Cabibbo angle |V_us| = 1/(rank·√n_C) = 1/√20 (0.62%), which is √(m_d/m_s) with the BST-exact
m_d/m_s = rank²·n_C = 20 (T2513) — a mixing↔mass cross-check that GROUNDS the June geometric-√ Cabibbo in the banked mass
ratio, using NO new integers. A = |V_cb|/λ² ≈ n_C/C_2 = 5/6 is a candidate; the 2-3 sector does NOT follow simple Gatto
(honest). Same discipline as the mass row: one clean rung, candidates flagged, don't over-claim.

PART 1 — m_t/m_c ARTIFACT DOCUMENTED: at a CONSISTENT scale (both at M_Z) m_t/m_c = 171.7/0.619 = 277, NOT 136 — the "137
= N_max" match was a pole/running mixing artifact (m_t(pole) with m_c(2GeV)). Rejection documented.
PART 2 — THE CABIBBO, target-innocent (the clean CKM result): Gatto (F585) gives |V_us| = √(m_d/m_s); the BST-exact mass
ratio is m_d/m_s = 1/(rank²·n_C) = 1/20 (T2513); therefore |V_us| = 1/(rank·√n_C) = 1/√20 = 0.22361 vs observed 0.22500
(0.62%, within the Gatto up-sector-correction size). TARGET-INNOCENT: no new integers — it chains the already-banked mass
ratio through the structural Gatto relation. This GROUNDS the June geometric-√ Cabibbo as = 1/(rank·√n_C), and it is the
mixing↔mass cross-consistency the row was set up to test (Gatto ties the two ladders, both from the same D_IV⁵ geometry).
Tier-1 IDENTIFICATION candidate (radial-overlap computation still owed for full D-tier).
CANDIDATE (not banked): A = |V_cb|/λ² = 0.826 ≈ n_C/C_2 = 5/6 = 0.833 (0.9%) — clean 2-primary form, but A carries ~2%
error and the match is ~1% → candidate, not a bank (the m_c/m_u=588 lesson).
HONEST NEGATIVES: |V_ub/V_cb| = 0.088 has no clean target-innocent form (1/(rank·C_2)=1/12=0.083 is 5.6% off). And the
Gatto √(mass-ratio) relation is a 1-2 (Cabibbo) relation ONLY — it FAILS for 2-3: √(m_s/m_b) ≈ 0.14 ≫ V_cb ≈ 0.042. So the
mixing hierarchy is NOT uniformly √(mass-ratio); only the Cabibbo follows it. Report straight.

⟹ VERDICT: PART 1 — m_t/m_c = 277 at a consistent scale documents the 137-artifact rejection. PART 2 — the CKM row opens
with ONE clean target-innocent result: |V_us| = 1/(rank·√n_C) = 1/√20 (0.62%) = √(m_d/m_s) via Gatto + the banked
m_d/m_s = rank²·n_C = 20 — a mixing↔mass cross-check grounding the geometric-√ Cabibbo, no new integers (Tier-1
identification candidate). A = n_C/C_2 = 5/6 is a candidate (0.9%, not banked); |V_ub/V_cb| and the 2-3 Gatto relation are
honest negatives (Gatto is 1-2 only). Discipline carried from the mass row: test ratios not exponents, mechanism ⊥
precision, target-innocent, one clean rung + flagged candidates. Count ~7-8. Five-Absence-safe.
"""
import math
rank, N_c, n_C, C_2, g, N_max = 2, 3, 5, 6, 7, 137
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

# ---- Part 1: m_t/m_c artifact ------------------------------------------------
mtmc_consistent = 171.7/0.619
print(f"\n[Part 1] m_t/m_c at consistent M_Z scale = {mtmc_consistent:.0f} (NOT 136 → the '137=N_max' was a pole/running artifact)")
check("PART 1 — m_t/m_c ARTIFACT DOCUMENTED: at a CONSISTENT scale (both M_Z) m_t/m_c = 277, NOT 136 — the '137 = N_max' "
      "match was a pole/running mixing artifact (m_t(pole) with m_c(2GeV)). Rejection on record.",
      mtmc_consistent > 250, "m_t/m_c = 277 at consistent scale → the 137 match was a pole/running artifact (documented)")

# ---- Part 2: the Cabibbo via Gatto + banked mass ratio ----------------------
Vus = 0.22500
lam_bst = 1/(rank*math.sqrt(n_C))     # = sqrt(1/(rank^2 n_C)) = sqrt(m_d/m_s), m_d/m_s = 1/20 (T2513)
print(f"[Part 2] |V_us| = {Vus:.5f}; BST 1/(rank·√n_C) = 1/√20 = {lam_bst:.5f} ({abs(lam_bst-Vus)/Vus*100:.2f}%) = √(m_d/m_s), Gatto+T2513")
check("PART 2 — THE CABIBBO (clean, target-innocent): Gatto (F585) → |V_us| = √(m_d/m_s); BST-exact m_d/m_s = 1/(rank²·n_C) "
      "= 1/20 (T2513); so |V_us| = 1/(rank·√n_C) = 1/√20 = 0.22361 vs 0.22500 (0.62%, within Gatto up-sector corrections). "
      "TARGET-INNOCENT — no new integers, chains the banked mass ratio through the structural Gatto relation. Grounds the "
      "June geometric-√ Cabibbo as 1/(rank·√n_C); the mixing↔mass cross-consistency. Tier-1 identification candidate.",
      abs(lam_bst - Vus)/Vus < 0.01, "|V_us| = 1/(rank·√n_C) = 1/√20 (0.62%) = √(m_d/m_s) via Gatto + banked m_d/m_s=20 → mixing↔mass cross-check, no new integers")

# ---- candidate: A = n_C/C_2 -------------------------------------------------
Vcb = 0.04182; A = Vcb/Vus**2
print(f"[candidate] A = |V_cb|/λ² = {A:.4f} ≈ n_C/C_2 = 5/6 = {5/6:.4f} ({abs(5/6-A)/A*100:.1f}%)")
check("CANDIDATE (not banked): A = |V_cb|/λ² = 0.826 ≈ n_C/C_2 = 5/6 = 0.833 (0.9%) — clean 2-primary form, but A carries "
      "~2% error and the match is ~1% → candidate, not a bank (the m_c/m_u=588 lesson: don't bank a ~1% hit that the error "
      "band + a plausible primary product can absorb).",
      abs(5/6 - A)/A < 0.02, "A = n_C/C_2 = 5/6 (0.9%) — clean candidate but within error band → flagged, not banked")

# ---- honest negatives -------------------------------------------------------
Vub = 0.00369; r_ubcb = Vub/Vcb
gatto23 = math.sqrt(1/48)   # sqrt(m_s/m_b), m_s/m_b ~ 1/48
print(f"[negatives] |V_ub/V_cb| = {r_ubcb:.4f} (1/12={1/12:.4f}, 5.6% off — no clean form); Gatto 2-3: √(m_s/m_b)={gatto23:.3f} ≫ V_cb={Vcb:.3f}")
check("HONEST NEGATIVES: |V_ub/V_cb| = 0.088 has no clean target-innocent form (1/(rank·C_2)=1/12=0.083 is 5.6% off). And "
      "the Gatto √(mass-ratio) relation is a 1-2 (Cabibbo) relation ONLY — it FAILS for 2-3 (√(m_s/m_b) ≈ 0.14 ≫ V_cb ≈ "
      "0.042). So the mixing hierarchy is NOT uniformly √(mass-ratio); only the Cabibbo follows it. Reported straight.",
      abs(1/12 - r_ubcb)/r_ubcb > 0.03 and gatto23 > 2*Vcb, "V_ub/V_cb no clean form (5.6% off); Gatto is 1-2 only (fails for V_cb) → honest negatives, mixing not uniformly √-ratio")

# ---- verdict ----------------------------------------------------------------
check("VERDICT: PART 1 — m_t/m_c = 277 (consistent scale) documents the 137-artifact rejection. PART 2 — the CKM row opens "
      "with ONE clean target-innocent result: |V_us| = 1/(rank·√n_C) = 1/√20 (0.62%) = √(m_d/m_s) via Gatto + the banked "
      "m_d/m_s = rank²·n_C = 20, a mixing↔mass cross-check grounding the geometric-√ Cabibbo with NO new integers (Tier-1 "
      "identification candidate). A = n_C/C_2 = 5/6 is a candidate (0.9%); |V_ub/V_cb| + the 2-3 Gatto relation are honest "
      "negatives (Gatto is 1-2 only). Discipline carried: test ratios not exponents, mechanism ⊥ precision, "
      "target-innocent, one clean rung + flagged candidates.",
      mtmc_consistent > 250 and abs(lam_bst - Vus)/Vus < 0.01,
      "CKM opens: |V_us|=1/(rank·√n_C)=1/√20 (0.62%, Gatto+banked m_d/m_s) clean+target-innocent; A=5/6 candidate; 2-3 Gatto fails; m_t/m_c=277 documented")

# ---- SCORE -------------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print("\n" + "=" * 96)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 96)
print(f"SCORE: {passed}/{total}")
print("=" * 96)
print(f"""
ROUND-6 close quark row (Part 1) + open CKM row (Part 2) — Elie's target-innocent half:
  * PART 1: m_t/m_c = 277 at a consistent scale → documents the '137=N_max' pole/running-artifact rejection.
  * PART 2 (the clean result): |V_us| = 1/(rank·√n_C) = 1/√20 = 0.2236 (0.62%) = √(m_d/m_s) via Gatto + the banked m_d/m_s=rank²·n_C=20 → grounds the geometric-√ Cabibbo, NO new integers (mixing↔mass cross-check).
  * CANDIDATE: A = |V_cb|/λ² ≈ n_C/C_2 = 5/6 (0.9%) — flagged, not banked (within error band).
  * NEGATIVES: |V_ub/V_cb| no clean form; Gatto is 1-2 only (fails for V_cb). Mixing not uniformly √(mass-ratio).
  => CKM row opens with one clean target-innocent rung (Cabibbo tied to the mass ladder); candidates + negatives flagged straight. Same discipline as the mass row.
""")
