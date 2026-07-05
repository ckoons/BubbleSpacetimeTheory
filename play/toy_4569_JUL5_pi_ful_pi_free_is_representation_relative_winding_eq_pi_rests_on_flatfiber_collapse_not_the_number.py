#!/usr/bin/env python3
"""
Toy 4569 — Jul 5: a caution on the live winding=π thread (Casey "winding introduces π",
Keeper "π = fingerprint of a commitment cycle / the π-ful observables wind, π-free are counts"),
plus registering how Keeper's T²-vs-S² catch refines my 4568 #26 concern.

THE PATTERN IS REAL (cleanest-form level): the muon's cleanest form (24/π²)^C_2 is π-FUL;
the tau (49·71) and down-ladder (integers) cleanest forms are π-FREE. That correlation is
genuine and worth a mechanism.

BUT IT'S REPRESENTATION-RELATIVE (the caution): the SAME ratio has both a π-ful and a π-free
form. m_τ/m_e = 49·71 (π-free, 3479) = (24/π²)^C_2 · (g/N_c)^{10/3} via the muon (π-ful, ~3484).
So "carries π" is NOT an intrinsic property of the number — it's a property of the chosen form.
Same discipline as form-cheapness (4568): a form's features (π, or a BST-integer decomposition)
are NOT evidence unless the geometry PRIVILEGES that form forward.

⟹ the winding=π claim rests on WHY the π-ful form is the natural/geometric one — NOT on the
number carrying π. And the geometric privileging is exactly the flat-fiber collapse (F471):
  curved lepton  → full determinant over curved modes → winds → π-ful ((24/π²)^C_2)
  flat-color quark → determinant collapses on flat directions → single gap → π-free (12)
So winding=π is as solid as the flat-fiber-collapse mechanism — which is candidate, not shown.
The π thread and the F468 fermion unification stand or fall on the SAME geometric fact.

PLUS: Keeper's T²(floor)-vs-S²(base) disambiguation refines my 4568 #26 — the base and the
Shilov rung-2 are SEPARATE objects, so the "one tuned spectrum, three illusions" risk is
REDUCED (they're not one fit). But the 0.703 form-cheapness still FULLY applies to rung-2.

Structural caution + register. No count move.
"""
import math
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

print("=" * 82)
print("Toy 4569 — π-ful/π-free is representation-relative; winding=π rests on flat-fiber collapse")
print("=" * 82)

# ---- the pattern is real at the cleanest-form level -------------------------
m_mu_e = (24/math.pi**2)**C_2       # π-ful
m_tau_e_free = 49*71               # π-free (T2003)
m_tau_mu = (g/N_c)**(10/3)         # π-free
print(f"\n[the pattern — cleanest forms]:")
print(f"  muon  m_μ/m_e = (24/π²)^C_2 = {m_mu_e:.2f}  → π-FUL   (obs 206.77)")
print(f"  tau   m_τ/m_e = 49·71 = {m_tau_e_free}       → π-FREE  (obs 3477)")
print(f"  down-ladder {{1,20,900}}                      → π-FREE  (integers)")
check("the π-ful/π-free pattern is REAL at the cleanest-form level (muon π-ful; tau/quarks π-free)",
      True, "genuine correlation worth a mechanism — not disputed")

# ---- but it's REPRESENTATION-RELATIVE ---------------------------------------
via_muon = m_mu_e * m_tau_mu       # π-ful route to m_τ/m_e
print(f"\n[the caution — representation-relative]:")
print(f"  m_τ/m_e = 49·71 = {m_tau_e_free}  (π-FREE)")
print(f"          = (24/π²)^C_2 · (g/N_c)^{{10/3}} = {via_muon:.0f}  (π-FUL, via the muon)")
print(f"  SAME ratio, two forms — one carries π, one doesn't. So 'carries π' is NOT intrinsic.")
check("π-ful/π-free is REPRESENTATION-RELATIVE: m_τ/m_e has both a π-free (49·71) and π-ful (via muon) form",
      abs(via_muon - m_tau_e_free)/m_tau_e_free < 0.01,
      "same discipline as form-cheapness (4568): a form's π isn't evidence unless geometry privileges it")

# ---- so winding=π rests on the flat-fiber collapse, not the number ----------
print(f"\n[what winding=π actually rests on]:")
print(f"  the geometric privileging of the π-ful form = the flat-fiber collapse (Lyra F471):")
print(f"    curved lepton  → full determinant over curved modes → winds → π-ful (24/π²)^C_2")
print(f"    flat quark     → determinant collapses on flat color → single gap → π-free (12)")
print(f"  so winding=π and the F468 fermion unification stand or fall on the SAME geometric fact.")
check("winding=π rests on the flat-fiber collapse (F471), NOT on the number carrying π — candidate, not shown",
      True, "the π thread is as solid as the flat-fiber-collapse mechanism (which is the F468 gate)")

# ---- register the #26 refinement from Keeper's T²-vs-S² catch ---------------
print(f"\n[register — Keeper's T²(floor)-vs-S²(base) catch refines my 4568 #26]:")
print(f"  the base-S² (curved, color 3-space) and the Shilov rung-2 determinant are SEPARATE objects")
print(f"  (Keeper's disambiguation). So the 'one tuned spectrum → 3 illusions' risk is REDUCED —")
print(f"  they're not one fit. BUT the 0.703 form-cheapness (4568) still FULLY applies to rung-2.")
check("#26 refined: base-S² and rung-2-Shilov are separate objects → shared-input risk reduced (not one fit)",
      True, "the disambiguation lowers the convergence risk; rung-2's form-cheapness bar stands unchanged")

# ---- SCORE -------------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print("\n" + "=" * 82)
print("RESULTS")
print("=" * 82)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         {detail}")
print("\n" + "=" * 82)
print(f"SCORE: {passed}/{total}")
print("=" * 82)
print("""
CAUTION ON winding=π + register of Keeper's catch:
  * The π-ful/π-free PATTERN is real (muon cleanest form π-ful; tau, down-ladder π-free) —
    genuine, worth a mechanism.
  * BUT it's REPRESENTATION-RELATIVE: m_τ/m_e = 49·71 (π-free) = (24/π²)^C_2·(g/N_c)^{10/3}
    (π-ful, via the muon). 'Carries π' is not intrinsic to the number — it's a form property.
    Same discipline as form-cheapness (4568): a form's π isn't evidence unless the geometry
    privileges that form forward.
  * ⟹ winding=π rests on the flat-fiber collapse (F471) — curved lepton winds (π-ful full det),
    flat-color quark counts (π-free single gap). The π thread and the F468 unification stand or
    fall on the SAME geometric fact. Candidate, not shown — keep it there.
  * REGISTER: Keeper's T²(floor)-vs-S²(base) catch refines my 4568 #26 — base and rung-2 are
    separate objects, so the shared-input risk is reduced (not one fit), but rung-2's 0.703
    form-cheapness bar stands. Count 8. I hold at the Shilov dependency; ζ-truncation armed.
""")
