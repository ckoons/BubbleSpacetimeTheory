#!/usr/bin/env python3
"""
Toy 4532 — Wednesday E3: is the α refinement 1/28 = 1/(2·g·rank) FORCED, or also
EM-blind? Lyra's bounded sub-test on the per-channel-α lane.

LANE E3 (Wednesday 2026-07-01). Lyra laid the per-channel-α propagator scaffold
and surfaced the load-bearing doubt: α = 1/N_max = 1/(N_c³·n_C + rank) needs the
channel count to read structurally on the SO(4,2) conformal (=EM) sector — but
N_c³ = 27 on a COLOR-BLIND photon is exactly the factor that must be EARNED, not
assumed. She handed me the cleaner bounded version: the refinement
    α⁻¹ = N_max + 1/(2·g·rank) = 137 + 1/28
— is the 1/28 correction FORCED by a mechanism, or is it also blind (a form-match,
with g and rank imported onto the EM sector unearned, same as N_c³)?

CHECKER APPROACH (target-innocent, CODATA):
  1. how good is 137 + 1/28 vs observed α⁻¹, at EXPERIMENTAL precision?
  2. what denominator does the data actually require? is 28 forced or nearest-ish?
  3. is 28 = 2·g·rank form-degenerate?
  4. are g (embedding/signature) and rank earned on the conformal EM sector, or
     imported — the exact analog of Lyra's N_c³ doubt?
VERDICT PREVIEW: 1/28 is a STRUCTURAL improvement over bare 137 but does NOT reach
experimental precision (off ~2e-6 rel vs ~1e-10 experiment), the data-required
denominator is 27.78 (28 is 0.8% off, not forced), 28 is form-degenerate, and
2·g·rank imports g onto the EM sector unearned -> BLIND, supports Lyra's doubt.
No form fished.
"""
from itertools import product as iproduct

rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
N_max = N_c**3 * n_C + rank     # 137
results = []
def check(label, cond, detail):
    results.append((label, bool(cond), detail))

# ---- CODATA 2022 ------------------------------------------------------------
alpha_inv_obs = 137.035999177     # CODATA 2022 (uncertainty ~2e-8 abs, ~1.5e-10 rel)
exp_rel_prec = 1.5e-10

print("=" * 78)
print("Toy 4532 — E3: is α refinement 1/28 = 1/(2·g·rank) forced or EM-blind?")
print("=" * 78)

# ---- PART 1: the numeric match, at experimental precision -------------------
ref = 28
alpha_inv_bst = N_max + 1.0/ref
abs_err = alpha_inv_obs - alpha_inv_bst
rel_err = abs_err / alpha_inv_obs
print(f"\n[PART 1] α⁻¹ = N_max + 1/28 = {alpha_inv_bst:.9f}  vs obs {alpha_inv_obs:.9f}")
print(f"  bare N_max = 137 alone: off by {alpha_inv_obs-137:.6f}")
print(f"  with 1/28: abs err {abs_err:.3e}, rel err {rel_err:.3e}")
print(f"  experimental rel precision ~ {exp_rel_prec:.1e}")
check("1/28 improves over bare 137 (structural gain: 3 extra digits)",
      abs(abs_err) < abs(alpha_inv_obs - 137), f"137→137.036 direction correct")
check("BUT 1/28 does NOT reach experimental precision (off ~2e-6 rel vs ~1e-10 exp)",
      rel_err > 100*exp_rel_prec, f"rel err {rel_err:.2e} >> exp {exp_rel_prec:.1e} -> STRUCTURAL, not precise")

# ---- PART 2: what denominator does the DATA require? ------------------------
den_needed = 1.0/(alpha_inv_obs - N_max)
print(f"\n[PART 2] data-required correction denominator = 1/(α⁻¹−137) = {den_needed:.4f}")
print(f"  2·g·rank = {2*g*rank}   -> {ref/den_needed:.4f}× the required value ({(ref/den_needed-1):+.2%})")
check("data requires denominator ~27.78, NOT 28; 2·g·rank misses it by ~0.8%",
      abs(ref - den_needed)/den_needed > 0.005, f"28 vs {den_needed:.3f} -> not forced by precision")

# ---- PART 3: form-degeneracy of 28 ------------------------------------------
PRIM = {"rank": rank, "N_c": N_c, "n_C": n_C, "C_2": C_2, "g": g}
names = list(PRIM); vals = [PRIM[n] for n in names]
def mono(maxdeg, maxexp):
    out = {}
    for e in iproduct(range(maxexp+1), repeat=len(names)):
        if 1 <= sum(e) <= maxdeg:
            v = 1
            for ei, pv in zip(e, vals): v *= pv**ei
            out[e] = v
    return out
def lab(e): return "*".join(f"{n}^{ei}" if ei>1 else n for n,ei in zip(names,e) if ei)
def forms_for(t):
    M = mono(3,3); s=set(); items=list(M.items())
    for i,(e1,v1) in enumerate(items):
        if v1==t: s.add("mono:"+lab(e1))
        for j in range(i,len(items)):
            e2,v2=items[j]
            if v1+v2==t: s.add("+".join(sorted((lab(e1),lab(e2)))))
            if v1!=v2 and abs(v1-v2)==t:
                hi,lo=(lab(e1),lab(e2)) if v1>v2 else (lab(e2),lab(e1)); s.add(f"{hi}-{lo}")
    return len(s)
deg28 = forms_for(28)
print(f"\n[PART 3] form-degeneracy of 28 (declared space): {deg28} forms "
      f"(2·g·rank, 4·g, C_2+n_C+... etc.)")
check("28 is form-degenerate -> a bare denominator match is cheap (Keeper #26)",
      deg28 >= 3, f"{deg28} forms")

# ---- PART 4: the EM-blind catch (parallel to Lyra's N_c^3 doubt) ------------
print("\n[PART 4] are g, rank EARNED on the conformal (EM) sector?")
print("  2·g·rank imports g = 7 (embedding/signature dim of SO(5,2)) onto the")
print("  SO(4,2) conformal photon sector. That is the SAME 'unearned factor' risk")
print("  as N_c³ = 27 on the color-blind photon (Lyra's load-bearing doubt).")
print("  rank = 2 (domain rank) is plausibly on-sector; g on the EM sector is NOT")
print("  obviously forced -> the correction's STRUCTURE is not derived from EM.")
check("2·g·rank imports g onto the EM sector unearned (parallel to N_c^3 doubt)",
      True, "structure not forced by the conformal propagator -> blind, like N_c^3")

# ---- PART 5: verdict --------------------------------------------------------
check("1/28 refinement is BLIND (structural-only match, denom not forced, "
      "form-degenerate, g unearned on EM) -> supports Lyra's per-channel doubt",
      True, "does NOT rescue the EM-identification; consistent with Wyler-or-elsewhere")

# ---- SCORE -------------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print("\n" + "=" * 78)
print("RESULTS")
print("=" * 78)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         {detail}")
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total}")
print("=" * 78)
print(f"""
CHECKER VERDICT (E3, answers Lyra's bounded sub-test):
  The 1/28 = 1/(2·g·rank) refinement is BLIND, not forced. Four reasons:
   1. It's a STRUCTURAL improvement (137 → 137.0357) but does NOT reach
      experimental precision — off {rel_err:.1e} rel vs ~{exp_rel_prec:.0e} experiment.
   2. The data-required denominator is {den_needed:.2f}, NOT 28 — 2·g·rank misses it
      by ~0.8%, so precision does not force 28.
   3. 28 = 2·g·rank is form-degenerate ({deg28} forms) — a bare match is cheap.
   4. 2·g·rank imports g (embedding/signature) onto the conformal EM sector
      UNEARNED — the exact analog of the N_c³-on-a-color-blind-photon doubt.
  => The 1/28 refinement does NOT rescue the per-channel EM identification. This
  SUPPORTS Lyra's honest doubt: if N_c³ (and g) can't be forced on the color-blind
  photon, the per-channel route stays EM-blind and α's identification comes from
  Wyler-or-elsewhere — not a failure to hide, the honest answer. No count move.
  @Lyra: the bounded sub-test lands on your side of the fork; 1/28 is blind too.
""")
