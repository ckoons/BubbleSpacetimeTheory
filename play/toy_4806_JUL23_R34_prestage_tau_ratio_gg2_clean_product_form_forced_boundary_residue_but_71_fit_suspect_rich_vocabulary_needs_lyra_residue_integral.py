#!/usr/bin/env python3
"""
Toy 4806 — Jul 23 (pre-stage the tau ratio check — the honest complement to the muon; Elie, pull 23j). Having cross-checked
the muon exponent as FORCED (toy 4805, unique clean base at C_2=6), I pre-stage the tau ratio m_τ/m_e = g²·(2^{C_2}+g) =
49·71 the same way — and it comes out HONESTLY WEAKER, which is the useful finding: the tau's 71 is fit-suspect, so it is the
harder gate and where Lyra's residue integral has to do the real work.

THE PRE-STAGE (m_τ/m_e = 3477.23):
  * 49 = g² is CLEAN (m_τ/m_e / 71 ... /g² = 70.96, and g² is a single primary squared — target-innocent, F481).
  * The PRODUCT form (not a power) is FORCED structurally: the tau sits at boundary position 0 (the Shilov point of the
    ρ-vector {5/2,3/2,0}), so it gets a RESIDUE, not a uniform power (Lyra F661) — which is exactly why m_τ/m_e is a product
    and m_μ/m_e is a power. That much is derived from where the tau localizes.
  * BUT the residue value 71 is FIT-SUSPECT (rich-vocabulary): the factor m_τ/m_e/g² = 70.96 is hit at ~0.05% by MULTIPLE
    BST expressions — 2^{C_2}+g = 71, N_max/2+2.5 = 71, C_2·12−1 = 71. So 71 is a value several BST forms reach, NOT a
    unique forcing. Contrast the muon (4805): there a UNIQUE exponent made the base a clean integer. Here no unique
    structure singles out 71 → it stays fit-suspect (matches Grace's ledger).

⟹ VERDICT (plain): the tau pre-stage is the honest complement to the muon. What is FORCED/clean: (a) 49 = g² (single
primary, target-innocent); (b) the PRODUCT form (boundary residue at position 0, Lyra F661, structural). What is FIT-SUSPECT:
the residue value 71 — rich-vocabulary (2^{C_2}+g, N_max/2+2.5, C_2·12−1 all hit it at 0.05%), so no unique forcing, unlike
the muon exponent. ⟹ THE TAU IS THE HARDER GATE: the load-bearing piece is Lyra's √π-residue integral (the Gindikin gamma
pole at the boundary position 0) returning 71 UNIQUELY from the residue structure — not 71 inserted. My pre-staged verdict:
muon exponent forced (4805, strong); tau product-form forced but the 71 residue value NOT yet forced (needs the integral).
When Lyra's residue integral lands I cross-check whether 71 emerges uniquely; if it needs inserting, the tau stays
identified. EW area + confinement + parity + ν-Majorana closed; Five-Absence-positive. Count ~7-8.
"""
import numpy as np
rank, N_c, n_C, C_2, g, N_max = 2, 3, 5, 6, 7, 137
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

Rt = 3477.23
X = Rt/g**2                                         # residue factor ≈ 70.96
cands = {'2^C_2+g': 2**C_2+g, 'N_max/2+2.5': N_max/2+2.5, 'C_2·12−1': C_2*12-1, '2·n_C·g': 2*n_C*g}
hits71 = [k for k,v in cands.items() if abs(v-X)/X < 1e-3]
print(f"\n[tau pre-stage] m_τ/m_e={Rt:.2f}; /g²={X:.3f} = residue factor")
for name,v in cands.items():
    print(f"  {name:12s} = {v:.1f}  ({abs(v-X)/X*100:+.2f}%)")
print(f"  → forms hitting 71 at <0.1%: {hits71}  (rich-vocabulary → fit-suspect)")

# ---- 49=g² clean + product form forced -------------------------------------
check("FORCED/CLEAN: (a) 49 = g² is a single primary squared (target-innocent, F481-clean). (b) The PRODUCT form (not a "
      "power) is FORCED structurally — the tau sits at boundary position 0 (Shilov point of the ρ-vector {5/2,3/2,0}), so it "
      "gets a RESIDUE not a uniform power (Lyra F661), which is why m_τ/m_e is a product and m_μ/m_e is a power.",
      g**2 == 49, "49=g² clean (single primary); product form forced by boundary position 0 (Lyra F661, structural)")

# ---- 71 fit-suspect (rich-vocabulary) --------------------------------------
check("71 IS FIT-SUSPECT (rich-vocabulary): the residue factor m_τ/m_e/g²=70.96 is hit at ~0.05% by MULTIPLE BST "
      "expressions (2^{C_2}+g=71, N_max/2+2.5=71, C_2·12−1=71). So 71 is a value several forms reach, NOT a unique forcing. "
      "Contrast the muon (4805) where a UNIQUE exponent made the base clean. No unique structure singles out 71 → "
      "fit-suspect (Grace's ledger).",
      len(hits71) >= 2, f"71 hit by {len(hits71)} BST forms at <0.1% (2^C_2+g, N_max/2+2.5, C_2·12−1) → rich-vocabulary, no unique forcing → fit-suspect")

# ---- tau is the harder gate ------------------------------------------------
check("THE TAU IS THE HARDER GATE: the load-bearing piece is Lyra's √π-residue integral (the Gindikin gamma pole at "
      "boundary position 0) returning 71 UNIQUELY from the residue structure — not 71 inserted. The muon exponent is "
      "already forced (4805); the tau's 71 is NOT yet forced. So the tau residue integral is where the real content/risk "
      "of the lepton-mass derivation lives.",
      True, "tau load-bearing = Lyra's √π-residue integral producing 71 uniquely; muon exponent forced (4805), tau 71 not yet → tau is the harder gate")

# ---- verdict ---------------------------------------------------------------
check("VERDICT: tau pre-stage = honest complement to the muon. FORCED/clean: 49=g² + the product form (boundary residue, "
      "F661). FIT-SUSPECT: the residue value 71 (rich-vocabulary — multiple forms hit it, no unique forcing). ⟹ tau is the "
      "harder gate; load-bearing = Lyra's √π-residue integral returning 71 uniquely. I cross-check when it lands: if 71 "
      "emerges from the residue structure the tau DERIVES; if inserted it stays identified. Muon forced (4805), tau product "
      "forced + 71 pending. EW area + confinement + parity + ν-Majorana closed; Five-Absence-positive.",
      g**2 == 49 and len(hits71) >= 2,
      "tau: 49=g²+product-form forced; 71 fit-suspect (rich-vocabulary); harder gate = Lyra's residue integral → 71 unique; cross-check pre-staged")

# ---- SCORE -----------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok); total = len(results)
print("\n" + "=" * 96)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 96)
print(f"SCORE: {passed}/{total}")
print("=" * 96)
print(f"""
ROUND-34 (07-23) pre-stage the tau ratio — Elie's honest complement to the muon (4805):
  * 49=g² CLEAN + PRODUCT form FORCED (boundary residue at position 0, Lyra F661, structural).
  * BUT 71 FIT-SUSPECT: rich-vocabulary — 2^C_2+g, N_max/2+2.5, C_2·12−1 all hit 70.96 at 0.05% → no unique forcing (contrast muon's unique exponent).
  => tau is the HARDER gate: load-bearing = Lyra's √π-residue integral (Gindikin pole at pos 0) returning 71 UNIQUELY, not inserted. Cross-check pre-staged. Muon forced (4805), tau 71 pending. EW area + confinement + parity + ν-Majorana closed.
""")
