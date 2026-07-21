#!/usr/bin/env python3
"""
Toy 4769 — Jul 21 (Round-8, CAPSTONE gate (a), Elie's fish-detector job at peak convergence): Keeper's K802 brake — which
ratifies my own tautology-catch — sets the non-negotiable test: m_s/m_d = 20 = rank²·n_C is the ANCHOR (it's what pinned
the addresses), NOT the test; reproducing it is circular. Gate (a) is the NON-tautological version: actually EVALUATE the
Gindikin/Faraut-Koranyi radial overlap at the DERIVED parameters (the spinor K-type at radial levels n=0,1,2 on D_IV⁵) and
check whether 20 falls out TUNING-FREE. I evaluated it, and the honest result confirms the brake by computation: with the
derived parameters the natural Gindikin norm ratios are {5, 6, 17.5, 21, 27} — NONE is 20; forcing 20 requires an
UN-DERIVED parameter. So "20 = rank²·n_C = strata dims" is NOT (yet) a tuning-free Gindikin output — it's the decomposition
Keeper flagged. Gate (a) NOT passed at the natural parameters; the burden is on Lyra's specific derived O-overlap
construction to output 20 without tuning.

THE DERIVED PARAMETERS (Faraut-Koranyi, no tuning): D_IV⁵ = type-IV Lie ball, dimension 5, RANK r = 2, characteristic
multiplicity a = n−2 = 3, genus p = 2 + a(r−1) = 5 = n_C, Bergman parameter ν = genus = n_C = 5. The rank-2 generalized
Pochhammer is (ν)_(m₁,m₂) = (ν)_{m₁}·(ν − a/2)_{m₂} = (ν)_{m₁}·(ν − 3/2)_{m₂}.
THE COMPUTATION (natural radial one-step NORM ratios at the derived ν = 5): (1,0)/(0,0) = 5; (2,0)/(1,0) = 6; (1,1)/(0,0)
= 17.5; (2,1)/(1,0) = 21; (2,2)/(1,1) = 27. NONE equals 20 = rank²·n_C. (Nearest: (2,1)/(1,0) = 21, +5%; (1,1) = 17.5,
−12.5%.)
THE RETROFIT CHECK: to force a natural one-step to equal exactly 20 needs an UN-DERIVED ν — (2,0)/(1,0) = ν+1 = 20 → ν=19;
(1,1) = ν(ν−3/2) = 20 → ν = 5.28 (not the derived 5). So 20 is NOT a tuning-free output of the derived Gindikin norms.
⟹ GATE (a) NOT PASSED at the natural parameters — confirms K802 by computation: "20 = rank²·n_C" is the ANCHOR/
decomposition (strata dims restated), not a computed tuning-free Gindikin output.
HONEST CAVEAT (fair to Lyra): the FULL mass ratio is the O-overlap matrix element ⟨f_n|O|f_n⟩ (the radial matrix element of
the VECTOR condensate O between spinor radial levels), NOT just the norm ratio — that full Faraut-Koranyi/Gindikin
computation is Lyra's and I have NOT evaluated it here. So this does NOT disprove the capstone; it shows the SIMPLEST
reading (norm ratio) does not give 20 at the derived ν, so the burden is on the specific derived O-overlap construction to
output 20 WITHOUT tuning. If it does → gate (a) passes; if it needs un-derived choices (a shifted ν, a hand-picked
partition, an ad-hoc point-shift) → it's the circular retrofit Keeper warned about → pivot-exit.

⟹ VERDICT: gate (a) is NOT met by the natural derived Gindikin norms — they give {5,6,17.5,21,27}, not 20, and forcing 20
needs an un-derived ν. This confirms Keeper's K802 brake BY COMPUTATION: "20 = rank²·n_C" is the anchor, not a tuning-free
Gindikin output. Do NOT bank the capstone. The remaining path: Lyra evaluates the FULL O-overlap matrix element ⟨f_n|O|f_n⟩
at n=0,1,2 with the DERIVED ν = n_C = 5 and NO ad-hoc shifts; gate (a) passes ONLY if that OUTPUTS 20; then gate (b)
(predict a SECOND independent quantity — V_cb / m_c/m_u / ν Δm²) is the real win. Pivot-exit stands if the overlap needs
tuning. Fired hardest at the prettiest result, as required. Count ~7-8. Five-Absence-safe.
"""
import math
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

a = n_C - 2          # multiplicity = 3
nu = n_C             # derived Bergman parameter = genus = n_C = 5
def poch(x, k):
    p = 1.0
    for i in range(k): p *= (x + i)
    return p
def gind(m1, m2):    # rank-2 generalized Pochhammer (nu)_(m1,m2)
    return poch(nu, m1) * poch(nu - a/2, m2)

# ---- the computation: natural norm ratios don't give 20 ---------------------
ratios = {"(1,0)/(0,0)": gind(1,0)/gind(0,0), "(2,0)/(1,0)": gind(2,0)/gind(1,0),
          "(1,1)/(0,0)": gind(1,1)/gind(0,0), "(2,1)/(1,0)": gind(2,1)/gind(1,0),
          "(2,2)/(1,1)": gind(2,2)/gind(1,1)}
none_is_20 = all(abs(v - 20) > 0.5 for v in ratios.values())
print(f"\n[derived params] D_IV⁵: rank={rank}, mult a={a}, genus=ν={nu}; target (tuning-free) = rank²·n_C = {rank**2*n_C}")
print("  natural radial NORM ratios: " + ", ".join(f"{k}={v:.1f}" for k, v in ratios.items()))
check("THE COMPUTATION (natural Gindikin norm ratios at the DERIVED ν = n_C = 5): {(1,0)/(0,0)=5, (2,0)/(1,0)=6, "
      "(1,1)/(0,0)=17.5, (2,1)/(1,0)=21, (2,2)/(1,1)=27}. NONE equals 20 = rank²·n_C (nearest 21, +5%; 17.5, −12.5%). So "
      "the natural derived Gindikin norms do NOT output 20 tuning-free.",
      none_is_20, "natural Gindikin norm ratios at derived ν=5 = {5,6,17.5,21,27} — none is 20 → 20 not a tuning-free norm-ratio output")

# ---- retrofit check ---------------------------------------------------------
import numpy as np
nu_11 = max(np.roots([1, -1.5, -20]))    # nu(nu-3/2)=20
print(f"[retrofit] forcing 20: (2,0)/(1,0)=ν+1=20 → ν=19; (1,1)=ν(ν−3/2)=20 → ν={nu_11:.2f} (both ≠ derived 5)")
check("THE RETROFIT CHECK: to force a natural one-step ratio to equal exactly 20 needs an UN-DERIVED ν — (2,0)/(1,0)=ν+1=20 "
      "→ ν=19; (1,1)=ν(ν−3/2)=20 → ν=5.28 (not the derived 5). So 20 is NOT a tuning-free output of the derived Gindikin "
      "norms — reproducing it requires a shifted ν (circular retrofit). Confirms K802: 20 is the anchor, not a computed "
      "output.",
      abs(nu_11 - 5) > 0.2, "forcing 20 needs an un-derived ν (19 or 5.28, not the derived 5) → 20 is anchor/decomposition, not tuning-free Gindikin output")

# ---- honest caveat (fair to Lyra) -------------------------------------------
check("HONEST CAVEAT (fair to Lyra): the FULL mass ratio is the O-overlap matrix element ⟨f_n|O|f_n⟩ (the radial matrix "
      "element of the VECTOR condensate O between spinor radial levels), NOT just the norm ratio — that full FK/Gindikin "
      "computation is Lyra's and I have NOT evaluated it here. So this does NOT disprove the capstone; it shows the "
      "SIMPLEST reading doesn't give 20 at the derived ν, so the burden is on the specific derived O-overlap construction "
      "to output 20 WITHOUT tuning (a shifted ν / hand-picked partition / ad-hoc point-shift = the circular retrofit).",
      True, "the full O-overlap ⟨f_n|O|f_n⟩ is Lyra's, not evaluated here → this holds gate (a) at natural params, doesn't disprove; burden on the derived O-overlap to output 20 tuning-free")

# ---- verdict ----------------------------------------------------------------
check("VERDICT: gate (a) is NOT met by the natural derived Gindikin norms — {5,6,17.5,21,27}, not 20; forcing 20 needs an "
      "un-derived ν. Confirms Keeper's K802 brake BY COMPUTATION: '20 = rank²·n_C' is the anchor, not a tuning-free "
      "Gindikin output. Do NOT bank the capstone. Remaining path: Lyra evaluates the FULL O-overlap ⟨f_n|O|f_n⟩ at n=0,1,2 "
      "with the DERIVED ν=n_C=5 and NO ad-hoc shifts; gate (a) passes ONLY if that OUTPUTS 20; then gate (b) (predict a "
      "SECOND independent quantity — V_cb / m_c/m_u / ν Δm²) is the win. Pivot-exit stands if the overlap needs tuning.",
      none_is_20 and abs(nu_11 - 5) > 0.2,
      "gate (a) NOT met at natural params (norms give {5,6,17.5,21,27}, forcing 20 needs un-derived ν) → K802 confirmed by computation; burden on Lyra's O-overlap; don't bank")

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
ROUND-8 CAPSTONE gate (a) — Elie's fish-detector evaluation (confirms K802 by computation):
  * DERIVED params: D_IV⁵ rank=2, mult a=n_C−2=3, genus=ν=n_C=5. Rank-2 Gindikin Pochhammer (ν)_(m₁,m₂)=(ν)_{{m₁}}(ν−3/2)_{{m₂}}.
  * NATURAL norm ratios = {{5, 6, 17.5, 21, 27}} — NONE is 20. Forcing 20 needs an un-derived ν (19 or 5.28).
  * => gate (a) NOT met at the natural parameters: "20=rank²·n_C" is the ANCHOR/decomposition, not a tuning-free Gindikin output. K802 confirmed by computation.
  * CAVEAT: the full O-overlap ⟨f_n|O|f_n⟩ (Lyra's) not evaluated — burden on it to OUTPUT 20 without tuning; then gate (b) predict a 2nd quantity. Pivot-exit stands.
""")
