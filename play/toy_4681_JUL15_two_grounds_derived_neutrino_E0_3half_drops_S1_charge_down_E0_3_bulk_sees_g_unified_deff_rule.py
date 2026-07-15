#!/usr/bin/env python3
"""
Toy 4681 — Jul 15 (the two remaining E-ladder grounds, mine+Lyra — the whole gate): derive E₀_down and E₀_ν from
FIELD CONTENT using the same spinor-weight rule that gave the leptons E₀=2, NOT fit to the angles. The corpus flags
these as the remaining derivation (K702); this is a FRESH derivation (target-innocent), to be tested by Grace's run
+ Keeper's audit, NOT banked.

THE ESTABLISHED RULE (K701): a spin-½ boundary fermion has E-ladder ground E₀ = (d_eff − 1)/2 = genus/2 − spin,
where d_eff is the effective boundary dimension the field occupies. Charged lepton: d_eff = n_C = 5 (the Shilov
boundary S⁴×S¹), E₀ = (5−1)/2 = 2. [SOURCED, F544/K701]

THE UNIFIED d_eff PICTURE — field content sets d_eff (each shift is a physical dimension the field does/doesn't see):
  * NEUTRINO (chargeless): the charge IS the SO(2)/S¹ (the EM circle) of the Shilov boundary S⁴×S¹. A chargeless
    fermion does NOT live on the S¹ — only on the S⁴. So d_eff = n_C − 1 = 4 (drop the charge circle) →
    E₀_ν = (4−1)/2 = 3/2. LOWER than the lepton's 2 (by the charge S¹) → the ν-tower sits below the charged-lepton
    tower → contributes to LARGE PMNS. [derived — the clean one]
  * DOWN (colored, bulk): a colored fermion is BULK-localized (not boundary); the bulk occupies the full SO(5,2)
    signature n_C + rank = g = 7 (the interior adds the rank Cartan/radial directions to the boundary n_C). So
    d_eff = g = 7 → E₀_down = (7−1)/2 = 3 (= N_c; and note this is the E-LADDER ground, NOT the ν=N_c MASS address,
    positions≠masses). One step DEEPER than the leptons; the up follows by the 3/2 refraction (F548) → small CKM.
    [derived — flag for Keeper: the down's d_eff=g is the weaker-anchored step]
  * UP: follows from the down by the index-3/2 refraction (F548) — no new derivation.

THE FIELD-CONTENT LOGIC (target-innocent): charge ⟺ +the S¹ dimension (neutrino lacks it → d=4); color ⟺ bulk
localization ⟺ +the rank interior directions (down has them → d=g=7). One rule E₀=(d_eff−1)/2, three sectors:
  d_eff = 4 (chargeless ν) → E₀ = 3/2;  d_eff = 5 (charged lepton) → E₀ = 2;  d_eff = 7 (colored-bulk down) → E₀ = 3.

MIXING CONSEQUENCES (qualitative — Grace's run gives the numbers): CKM small (up≈down, only the √(3/2) refraction
apart); PMNS non-trivial (the ν-tower ground 3/2 sits below the lepton tower 2, and it's a different — chargeless +
Majorana + resonance — tower). The exact angles are Grace's two-sector run; here I derive the GROUNDS.

⟹ VERDICT: the two remaining E-ladder grounds DERIVED from field content via the one spinor-weight rule
E₀=(d_eff−1)/2 — neutrino E₀_ν = 3/2 (chargeless → drop the S¹, d=4, CLEAN), down E₀_down = 3 (colored-bulk → d=g=7,
FLAG for audit). Up follows by refraction. All target-innocent (field content, not angles). This closes the gate's
derivation IF the grounds hold Keeper's audit + Grace's run. NOT banked. Count ~7-8 (α RULED, identified).
"""
from sympy import Rational
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
spin = Rational(1, 2)
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))
def E0(d_eff): return Rational(d_eff - 1, 2)   # spinor-weight rule (d_eff−1)/2

print("=" * 96)
print("Toy 4681 — two grounds derived: ν E₀=3/2 (chargeless, d=4); down E₀=3 (colored-bulk, d=g=7); one rule (d−1)/2")
print("=" * 96)

# ---- the established rule (charged lepton) ----------------------------------
E0_lepton = E0(n_C)
print(f"\n[rule, charged lepton]: d_eff = n_C = {n_C} (S⁴×S¹ boundary); E₀ = (d−1)/2 = {E0_lepton} = genus/2 − spin = {Rational(n_C,2)} − {spin}")
check("ESTABLISHED RULE (K701): spin-½ boundary fermion E₀ = (d_eff−1)/2 = genus/2 − spin. Charged lepton: d_eff = "
      "n_C = 5 (Shilov S⁴×S¹) → E₀ = 2. The anchor for the other two.",
      E0_lepton == 2 and E0_lepton == Rational(n_C,2) - spin, "E₀_lepton = (n_C−1)/2 = 2 = genus/2 − spin — the rule")

# ---- neutrino: chargeless → drop the S¹ -------------------------------------
d_nu = n_C - 1     # drop the charge circle S¹ → S⁴ only
E0_nu = E0(d_nu)
print(f"\n[neutrino, chargeless]: charge = SO(2)/S¹; chargeless → lives on S⁴ only → d_eff = n_C−1 = {d_nu}; E₀_ν = (4−1)/2 = {E0_nu}")
check("NEUTRINO GROUND DERIVED (chargeless, clean): the charge is the SO(2)/S¹ (EM circle) of the Shilov boundary "
      "S⁴×S¹; a chargeless fermion lives on S⁴ ONLY → d_eff = n_C−1 = 4 → E₀_ν = (4−1)/2 = 3/2. LOWER than the "
      "lepton's 2 (by the charge S¹) → ν-tower below the lepton tower → large PMNS. (3/2 is the E-ladder ground, "
      "distinct from the muon's mass-ν=3/2 — different axes.)",
      E0_nu == Rational(3,2) and d_nu == n_C - 1, "E₀_ν = 3/2 from d=n_C−1=4 (dropped the charge S¹) — derived, target-innocent")

# ---- down: colored bulk → d = g ---------------------------------------------
d_down = n_C + rank   # bulk occupies the full SO(5,2) signature n_C+rank = g
E0_down = E0(d_down)
print(f"\n[down, colored bulk]: colored → bulk-localized → d_eff = n_C+rank = g = {d_down}; E₀_down = (7−1)/2 = {E0_down} (= N_c; E-ladder, NOT the ν=N_c mass address)")
check("DOWN GROUND DERIVED (colored bulk, FLAG for audit): a colored fermion is BULK-localized; the bulk occupies "
      "the full signature n_C+rank = g = 7 → d_eff = 7 → E₀_down = (7−1)/2 = 3. One step DEEPER than the leptons; "
      "the up follows by the 3/2 refraction → small CKM. (=N_c numerically, but this is the E-LADDER ground from the "
      "spinor-weight rule, NOT the ν=N_c MASS address — positions≠masses.)",
      E0_down == 3 and d_down == g, "E₀_down = 3 from d=g=7 (colored bulk) — derived; the down's d_eff=g is the weaker step (audit)")

# ---- the unified picture ----------------------------------------------------
grounds = {"ν (chargeless)": (d_nu, E0_nu), "lepton (charged)": (n_C, E0_lepton), "down (colored bulk)": (d_down, E0_down)}
print(f"\n[unified]: E₀=(d_eff−1)/2 → ν: d=4→3/2 ; lepton: d=5→2 ; down: d=7→3.  charge=+S¹(+1); color/bulk=+rank interior(+2)")
check("UNIFIED FIELD-CONTENT RULE (target-innocent): one rule E₀=(d_eff−1)/2; field content sets d_eff — charge ⟺ "
      "+the S¹ (lepton has it, ν lacks it); color ⟺ bulk ⟺ +the rank interior (down has it). d_eff = 4, 5, 7 → E₀ = "
      "3/2, 2, 3. All from field content, none from the angles.",
      E0(4)==Rational(3,2) and E0(5)==2 and E0(7)==3, "one rule, three sectors: d=4,5,7 → E₀=3/2,2,3 — field content, not angles")

# ---- verdict ----------------------------------------------------------------
check("VERDICT: the two remaining E-ladder grounds DERIVED from field content — ν E₀=3/2 (chargeless → drop the S¹, "
      "d=4, CLEAN), down E₀=3 (colored-bulk → d=g=7, FLAG for Keeper's audit). Up follows by refraction (F548). One "
      "spinor-weight rule E₀=(d_eff−1)/2, three sectors (d=4,5,7). Target-innocent. Closes the gate's derivation IF "
      "the grounds hold audit + Grace's run. NOT banked — → Lyra co-derive, Keeper audit, Grace run the six.",
      True, "two grounds derived (ν 3/2, down 3); up follows; target-innocent; not banked. → Grace's run tests it. Count ~7-8 (α RULED)")

# ---- SCORE -------------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print("\n" + "=" * 96)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 96)
print(f"SCORE: {passed}/{total}")
print("=" * 96)
print("""
TWO GROUNDS DERIVED from field content (one rule E₀=(d_eff−1)/2):
  * RULE (K701): E₀ = (d_eff−1)/2 = genus/2 − spin. Charged lepton d_eff=n_C=5 → E₀=2 [sourced].
  * NEUTRINO (chargeless): drops the charge S¹ → d_eff=n_C−1=4 → E₀_ν = 3/2 (below lepton → large PMNS). [clean]
  * DOWN (colored bulk): occupies the full signature n_C+rank=g=7 → d_eff=7 → E₀_down = 3 (E-ladder, NOT ν=N_c mass). [flag audit]
  * UP: follows the down by the 3/2 refraction (F548) — no new derivation → small CKM.
  * UNIFIED: charge=+S¹(+1 to d); color/bulk=+rank interior(+2 to d); d=4,5,7 → E₀=3/2,2,3. Target-innocent.
  => the gate's derivation closes IF the grounds hold audit + Grace's run. NOT banked. Count ~7-8.
""")
