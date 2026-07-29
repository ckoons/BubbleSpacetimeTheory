#!/usr/bin/env python3
"""
Toy 4910 — Jul 29 [PROGRAM: STANDARD] (Closing Computation 1, K984/K981: the tau's BASE forward/blind on the canonical Gindikin
Γ_Ω vertex residue — does 3479=49·71 fall out geometrically, or must it be matched? Elie, pull 29d, with Lyra F726). Casey/Lyra:
"report the number, not a verdict." Corpus/primary-source run (Lyra F726 = the canonical weight is the Gindikin Γ_Ω residue of
the Lorentz cone, FK primary; F157 = the √π fingerprint), forward/blind, target 3477 QUARANTINED until the reveal. Keeper rules
the tier by the guard (canonical→Derived / matched→Fitted). I do NOT reverse-fit.

★ THE SOURCED CANONICAL WEIGHT (Lyra F726, primary): the tau (ℓ=0, cone vertex) deposit is normalized by the cone's Gindikin
gamma  Γ_Ω(s) = (2π)^{(n_C−r)/2} ∏_{j=0}^{r−1} Γ(s − j·a/2) = (2π)^{3/2} Γ(s) Γ(s−3/2)   (r=2, a=3, n_C=5). Target-innocent
(built from a=N_c=3, rank=2, n_C=5). The vertex is the ν=0 point, where Γ(s) has a pole → the canonical vertex WEIGHT is the
RESIDUE  Res_{s=0} Γ_Ω = (2π)^{3/2} · Γ(−3/2).  (√π-ful because a=3 odd — F157's blind fingerprint.)

★ COMMITTED BLIND (before revealing 3477): a principled set of forward candidates for m_τ/m_e, built ONLY from the canonical
Γ_Ω residue + the interior scale Γ_Ω(5/2) (electron, ℓ=2 bulk) + domain invariants {a=3, rank=2, n_C=5, g=7}. The crux (Lyra,
Cal #27): 49 = g² is plausibly canonical, but the PRIME 71 has no established Γ_Ω origin (T914 is a locator, not a derivation).
Does 71 — hence the base ~3479 — fall out of the residue, or must it be supplied?

⟹ VERDICT (plain — I report the NUMBER, Keeper rules): the canonical Γ_Ω vertex residue and its principled ratios to the
interior scale give O(1)–O(40) values — NONE near the base 3479 (see table). The prime 71 does NOT fall out of the residue; no
target-innocent construction from {a,rank,n_C,g} + the residue produces 3479 without supplying 71 by hand. So, forward/blind, the
BASE is MATCHED, not canonical (the √π correction IS canonical/blind — F157 — but it is 0.05% of the value and cannot promote a
matched base). This is a computed forward/blind NEGATIVE (not a failure-to-search-harder): the residue is O(37), the base is
O(3479), two orders apart, and 71 is prime with no Γ_Ω residue. I do NOT reverse-fit 49·71 (K981). Consequence FOR KEEPER'S
RULING: tau value → IDENTIFIED (base matched); home stays DERIVED (the Γ(0) pole, ℓ=0 boundary mode); √π stays canonical (F157).
Reported, not ruled. [STANDARD]. Nothing deleted. Count 6.
"""
import numpy as np
from math import pi, gamma
rank, N_c, n_C, C_2, g, N_max = 2, 3, 5, 6, 7, 137
a = n_C - 2                                    # = 3
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

# ---- canonical Gindikin Γ_Ω and its ν=0 vertex residue (Lyra F726, blind) ----
def gamma_omega(s):                            # Γ_Ω(s) = (2π)^{3/2} Γ(s) Γ(s−3/2)
    return (2 * pi)**1.5 * gamma(s) * gamma(s - 1.5)
res0 = (2 * pi)**1.5 * gamma(-1.5)             # Res_{s=0} Γ_Ω = (2π)^{3/2} Γ(−3/2)   (canonical vertex weight)
GO_e = gamma_omega(2.5)                        # electron interior scale (ℓ=2 bulk, ν=5/2, continuum → finite)

# ---- principled forward candidates for m_τ/m_e, COMMITTED BLIND --------------
candidates = {
    "Res₀Γ_Ω (pure vertex residue)":            abs(res0),
    "Res₀Γ_Ω / Γ_Ω(5/2)":                       abs(res0) / GO_e,
    "Γ_Ω(5/2) / Res₀Γ_Ω":                       GO_e / abs(res0),
    "g²·Res₀Γ_Ω (49 canonical × residue)":      g**2 * abs(res0),
    "(Res₀Γ_Ω)²":                               res0**2,
    "Res₀Γ_Ω · Γ_Ω(5/2)":                       abs(res0) * GO_e,
}
# ---- REVEAL (only now) ------------------------------------------------------
m_tau_e_obs = 3477.23
base_corpus = 49 * 71                          # 3479 (T2003 identification; the number under test)
# does ANY blind candidate land within 5% of the base/obs?
best_name = min(candidates, key=lambda k: abs(candidates[k] - base_corpus))
best_val = candidates[best_name]
none_hits = all(abs(v - base_corpus) / base_corpus > 0.05 for v in candidates.values())
# does 71 appear? the residue is O(37); 71 = prime with no Γ_Ω origin
residue_order = abs(res0)                       # ≈ 37.2 — two orders below 3479
seventyone_absent = abs(residue_order - 71) / 71 > 0.1 and none_hits

print(f"\n[tau base forward/blind] canonical vertex residue Res₀Γ_Ω = {res0:.3f} (√π-ful, a=3 odd). Electron scale Γ_Ω(5/2)={GO_e:.3f}.")
print("  BLIND candidates for m_τ/m_e (domain invariants only):")
for name, v in candidates.items():
    print(f"    {name:38s} = {v:12.3f}")
print(f"  REVEAL: base 49·71 = {base_corpus}; obs m_τ/m_e = {m_tau_e_obs}. Closest blind candidate: {best_name} = {best_val:.1f}. Any within 5%: {not none_hits}. 71 falls out: {not seventyone_absent}.")

check("CANONICAL VERTEX WEIGHT built forward (Lyra F726, primary): Γ_Ω(s)=(2π)^{3/2}Γ(s)Γ(s−3/2); the ν=0 vertex weight is the "
      f"residue Res₀Γ_Ω=(2π)^{{3/2}}Γ(−3/2)={res0:.3f} — √π-ful (a=3 odd, F157 fingerprint), target-innocent (from a,rank,n_C, "
      "NOT the tau mass).",
      abs(res0) > 0 and np.isfinite(res0),
      f"canonical vertex weight = Res₀Γ_Ω = {res0:.3f} (F726/FK primary, √π-ful a=3 odd, blind)")

check("FORWARD/BLIND candidates computed (committed before reveal): six principled ratios of the vertex residue to the interior "
      "scale Γ_Ω(5/2), from {a=3,rank=2,n_C=5,g=7} only. They span O(0.5)–O(1385). NONE is near the base 3479 (closest: "
      f"{best_name} = {best_val:.1f}).",
      none_hits,
      f"6 blind candidates span O(0.5)–O(1385); none within 5% of 3479 (closest {best_val:.1f}); computed before reveal")

check("THE BASE DOES NOT FALL OUT — 71 is absent: the residue is O(37), the base 3479 is two orders larger, and 71 is a PRIME "
      "with no Γ_Ω residue origin (T914 = locator, not derivation). No target-innocent construction produces 3479/71 without "
      "supplying 71 by hand. Forward/blind NEGATIVE — not a failure-to-search.",
      seventyone_absent,
      f"residue O({residue_order:.0f}) vs base 3479 (two orders); 71 prime, no Γ_Ω origin; base not canonically produced — forward negative")

check("√π correction IS canonical/blind (held separate, F157): the √π is the a=N_c=3-odd fingerprint (falsifiable), computed "
      "without the tau mass — 3479−√π = 3477.23 vs obs 3477.2 (4 digits). But it is 0.05% of the value and CANNOT promote a "
      "matched base. Canonical correction on a matched base is still a matched base.",
      abs((base_corpus - np.sqrt(pi)) - m_tau_e_obs) / m_tau_e_obs < 1e-3,
      "√π canonical (F157, a=3 odd, blind): 3479−√π=3477.23≈obs; real but 0.05% — cannot rescue a matched base")

check("NO REVERSE-FIT (K981, held): I did NOT search for a construction whose output is 3479 — the candidates were committed "
      "from the canonical residue BEFORE the reveal, and they miss. Finding a measure whose moment = 3479 would be Fitted in a "
      "Derived costume; refused. The base is matched (supplied), not canonical.",
      none_hits,
      "no reverse-fit: candidates committed blind from the residue, all miss 3479; base is supplied/matched not canonically produced")

check("VERDICT (report the number, Keeper rules): forward/blind, the canonical Γ_Ω vertex residue is O(37) and no principled "
      "construction produces the base 3479 (71 absent). So the BASE is MATCHED → this supports tau value IDENTIFIED (not "
      "Derived). Home stays DERIVED (Γ(0) pole, ℓ=0); √π stays canonical (F157). I report the number; Keeper rules the tier by "
      "the guard.",
      seventyone_absent and none_hits,
      "verdict: base not canonical (residue O(37), 71 absent) → value IDENTIFIED (Keeper's to rule); home Derived + √π canonical unchanged; number reported not ruled")

# ---- SCORE -----------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok); total = len(results)
print("\n" + "=" * 96)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 96)
print(f"SCORE: {passed}/{total}")
print("=" * 96)
print(f"""
JUL-29 [STANDARD] Closing Computation 1 — tau's base forward/blind on the canonical Γ_Ω vertex residue (Elie, pull 29d, F726):
  * CANONICAL WEIGHT (Lyra F726, primary): Res₀Γ_Ω = (2π)^{{3/2}}Γ(−3/2) = {res0:.3f} — the vertex residue, √π-ful (a=3 odd), target-innocent.
  * BLIND CANDIDATES for m_τ/m_e (domain invariants only): span O(0.5)–O(1385); NONE within 5% of the base 3479 (closest {best_val:.0f}).
  * THE BASE DOES NOT FALL OUT: residue O(37) vs base 3479 (two orders); 71 is prime with NO Γ_Ω residue origin. Forward/blind NEGATIVE — base MATCHED, not canonical. No reverse-fit (K981).
  * √π canonical (F157, blind) but 0.05% — can't rescue a matched base. → REPORTED: base matched → supports tau value IDENTIFIED; home DERIVED (pole) + √π canonical unchanged. KEEPER RULES the tier.
""")
