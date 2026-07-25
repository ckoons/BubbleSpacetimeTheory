#!/usr/bin/env python3
"""
Toy 4851 — Jul 25 (the REAL D_IV^5 s→1 Shilov-boundary Toeplitz spectrum — closes the lane 4850 left open; Elie, pull 25e).
Toy 4850 validated Casey's boundary fingerprint (gap-ratio baseline 1.710 model-independent; observed 1.889 forces electron
extra-suppression) but used the rank-1 DISK stand-in λ_n=Γ(n+2)/Γ(n+2−s), whose s→1 limit gives exponent p=1 (not the g-fold
amplification the data wants), and PUNTED the real spectrum to "FK-book territory." I now build the REAL rank-2 D_IV^5 boundary
Toeplitz from standard Faraut–Koranyi / Gindikin machinery (NOT fabricated: the multiplicities a=n−2=3, genus=n_C=5, rank=2 are
the domain's, and the Toeplitz eigenvalue of a power-of-norm symbol N^{−s} on a weighted Bergman space is the standard ratio of
Gindikin cone-Gammas). The pre-registered gate: does it FORCE bulk exponent = g=7 and electron-excess = 5/3 = n_C/N_c?

THE DECISIVE RESULT — INTEGRABILITY CAPS THE EXPONENT BELOW g (the gate FAILS on the bulk exponent):
  * The symbol N^{−s} (singular at the Shilov boundary) is square-pairable against the D_IV^5 Bergman kernel (∝ N^{−genus})
    only for s < genus = n_C = 5. A symbol MORE singular than the kernel is non-integrable → the Toeplitz operator is not
    even defined. This bound is convention-INDEPENDENT (symbol must be less singular than the kernel).
  * Sharper, mode-resolved: the generation modes are the (n,0) spherical ladder; their eigenvalue is Γ_Ω(m+ν)/Γ_Ω(m+ν−s)
    with rank-2 Gindikin Γ_Ω(x)=Γ(x_1)Γ(x_2−a/2). The SECOND (smaller) component forces s < genus − a/2 = 5 − 3/2 = 7/2.
  * So the boundary singularity strength the GENERATIONS can feel is capped at s ≲ 7/2…5. The achievable μ→τ bulk exponent
    p23 = ln(λ(3,0)/λ(2,0))/ln(3/2) RUNS from ~0.6 up to a MAXIMUM ≈ 1.70 as s→7/2 — right at the pure-power-law baseline,
    NEVER near the observed p = 6.96 = g. Reaching p=g=7 needs s=7 > genus=5: OUTSIDE the domain of definition.
  ⟹ D_IV^5 does not merely fail to force p=g — it FORBIDS it. g=7 is geometrically UNREACHABLE by the boundary Toeplitz.

THE ELECTRON / k=1 EXCESS (the one honest positive, held as a candidate): 5/3 = n_C/N_c = genus/a IS a genuine D_IV^5 ratio
(the ratio of the bulk genus-5 falloff to the boundary multiplicity a=3) and matches the required E=1.66 to 0.4%. That is a
plausible MECHANISM candidate for the flattened k=1 contact (bulk genus falloff replaced by boundary-multiplicity falloff). But
(i) it is a candidate needing a derived flattening mechanism + a free flattening DEPTH (a 2nd modulus W(D₅) does not pin —
toy 4848 Prong 2), and (ii) it cannot rescue the gate because the bulk exponent already fails.

⟹ VERDICT (pre-registered gate = NO → STRUCTURAL STANDS, K898/K899). The s→1 D_IV^5 boundary Toeplitz spectrum does NOT force
the lepton hierarchy from geometry + one external scale. The bulk exponent is CAPPED by integrability at ≲ genus = 5 < 7, so
the observed p≈g is geometrically UNREACHABLE (not a free-but-unpinned modulus — a FORBIDDEN one). g=7 is therefore an FF-20
post-hoc coincidence with no target-innocent geometric source (the geometry actively excludes it). The electron-excess
5/3 = n_C/N_c is a real geometric ratio and a legitimate mechanism CANDIDATE, but held (needs mechanism + free depth). To
reproduce the hierarchy one must supply the exponent p BY HAND (not from D_IV^5) PLUS the overall scale ≥ 2 free inputs, more
than the "one external scale" the gate allows. This SHARPENS 4848: not "s unpinned" but "s capped below the needed value."
Durable wins untouched (why-three Paper #138, hierarchy MECHANISM = singular boundary, flavor skeleton, CKM ordering F684, EW,
muon (24/π²)⁶). Five-Absence-positive. Peak-convergence discipline held: the elegant integers did not get banked. Count ~6.
"""
import numpy as np, math
from scipy.special import gammaln
rank, N_c, n_C, C_2, g, N_max = 2, 3, 5, 6, 7, 137
a, genus = n_C - 2, n_C              # type IV_5: multiplicity a=n-2=3 (=N_c), genus=n_C=5, rank=2
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

# ---- observed lepton data + the K900 fingerprint arithmetic ----
me, mmu, mtau = 0.51099895, 105.6583755, 1776.86
G1, G2 = math.log(mmu/me), math.log(mtau/mmu)          # log-gaps (K900, verified): 5.332, 2.822
gap_ratio = G1/G2                                       # 1.889
baseline = math.log(2)/math.log(1.5)                    # 1.7095 param-free (any bulk power law, 3 modes)
p_obs = G2/math.log(1.5)                                # exponent the data wants from μ→τ: 6.96
E_obs = math.exp(G1 - p_obs*math.log(2))               # electron excess: 1.660

# ---- REAL rank-2 D_IV^5 boundary Toeplitz: Gindikin/FK spectrum ----
# symbol N^{-s} (Shilov-boundary singular); eigenvalue on spherical mode m=(m1,m2):
#   λ_m ∝ Γ_Ω(m+ν)/Γ_Ω(m+ν-s),  ν=genus (Bergman weight),  Γ_Ω(x)=Γ(x1)Γ(x2 - a/2)  (rank-2 cone)
def lnGam2(m1, m2, shift):
    x1, x2 = m1 + shift, m2 + shift - a/2.0
    return None if (x1 <= 0 or x2 <= 0) else gammaln(x1) + gammaln(x2)
def lnlam(m1, m2, s, nu=genus):
    A, B = lnGam2(m1, m2, nu), lnGam2(m1, m2, nu - s)
    return None if (A is None or B is None) else A - B
def p23(s):                                             # μ(2,0)→τ(3,0) local bulk exponent
    l2, l3 = lnlam(2, 0, s), lnlam(3, 0, s)
    return None if (l2 is None or l3 is None) else (l3 - l2)/math.log(1.5)

s_ground_cap   = genus                                  # ground-mode integrability: s < genus = 5
s_ladder_cap   = genus - a/2                            # (n,0)-ladder integrability: s < 7/2 = 3.5
p_at_cap       = p23(s_ladder_cap - 0.01)               # max achievable μ→τ exponent (just under the cap)
undefined_at_g = (lnlam(0, 0, g) is None)               # is the g=7 symbol non-integrable on the ground mode?
elec_excess_geom = genus / a                            # 5/3 = n_C/N_c candidate

print(f"\n[K900 fingerprint] G1={G1:.3f} G2={G2:.3f} gap-ratio={gap_ratio:.3f}  baseline(param-free)={baseline:.3f}  "
      f"=> data wants p={p_obs:.3f}(≈g=7) and E={E_obs:.3f}(≈5/3={5/3:.3f})")
print(f"[integrability] ground-mode cap s<genus={s_ground_cap}; (n,0)-ladder cap s<genus-a/2={s_ladder_cap};  "
      f"symbol at s=g=7 non-integrable on ground mode: {undefined_at_g}")
print(f"[achievable exponent] μ→τ p23 runs {p23(1.5):.3f}(s=1.5) → {p_at_cap:.3f}(s→{s_ladder_cap}) ; observed needs {p_obs:.2f} → UNREACHABLE")
print(f"[electron excess] geom ratio n_C/N_c=genus/a={elec_excess_geom:.4f} vs required E={E_obs:.3f} (candidate mechanism)")

check("PRE-REGISTERED GATE, bulk exponent: does the D_IV^5 s→1 boundary Toeplitz FORCE p = g = 7? NO — INTEGRABILITY caps it. "
      "The symbol N^{-s} is pairable against the Bergman kernel (∝N^{-genus}) only for s<genus=n_C=5 (a symbol more singular "
      "than the kernel is non-integrable → operator undefined). The (n,0) generation ladder is capped tighter at s<genus-a/2="
      "7/2. So the achievable μ→τ exponent maxes at p≈1.70 (the baseline), a factor ~4 below the observed p=6.96=g. g=7 needs "
      "s=7>genus=5: OUTSIDE the domain of definition.",
      undefined_at_g and (p_at_cap < 2.0) and (s_ladder_cap < g),
      f"boundary Toeplitz caps s<genus=5 (ladder s<7/2); max μ→τ exponent≈{p_at_cap:.2f}≪p_obs={p_obs:.2f}=g; g=7 non-integrable → UNREACHABLE, not merely un-forced")

check("So g=7 is FF-20 post-hoc coincidence with NO target-innocent geometric source — the geometry actively EXCLUDES it. "
      "(3/2)^g=17.09 vs m_τ/m_μ=16.82 is a 1.6% leading-order FORM many σ off precise masses; and the exponent that form "
      "encodes is unreachable by the D_IV^5 boundary spectrum. Not banked.",
      abs((1.5**g)/(mtau/mmu) - 1) < 0.03 and (p_at_cap < g),
      "(3/2)^g=17.09 vs 16.82 = 1.6% form, many σ off; encoded exponent g=7 geometrically unreachable → FF-20 coincidence, HELD not banked")

check("ELECTRON / k=1 excess — the one honest positive (candidate, not banked): 5/3 = n_C/N_c = genus/a IS a genuine D_IV^5 "
      "ratio (bulk genus-5 falloff ÷ boundary multiplicity a=3) and matches the required E=1.66 to 0.4%. A plausible MECHANISM "
      "candidate for the flattened k=1 Shilov contact. BUT it needs a derived flattening + a free flattening DEPTH (2nd modulus "
      "W(D₅) does not pin — 4848 Prong 2), and cannot rescue the gate since the bulk exponent already fails.",
      abs(elec_excess_geom/E_obs - 1) < 0.01,
      "5/3=n_C/N_c=genus/a matches E=1.66 to 0.4% — genuine geom ratio, legitimate mechanism CANDIDATE; held (needs mechanism + free depth); doesn't rescue the failed bulk exponent")

check("FREE-INPUT TALLY: to reproduce the hierarchy from the boundary spectrum one must supply (1) the bulk exponent p BY HAND "
      "(NOT from D_IV^5 — capped at ≲genus=5<7) PLUS (2) the overall mass scale (m_e / seesaw M_R). That is ≥2 free inputs, "
      "MORE than the single external scale the gate allows (gravity-taking-m_Planck status requires everything else forced). "
      "So NOT conditionally-derived.",
      (p_at_cap < g),
      "≥2 free inputs (exponent supplied by hand + overall scale) > the one external scale allowed → fails the conditional-derive bar")

check("VERDICT (pre-registered gate = NO → STRUCTURAL STANDS, K898/K899): the s→1 D_IV^5 Shilov boundary Toeplitz does NOT "
      "force the lepton hierarchy. Bulk exponent capped by integrability at ≲genus=5<7 → g=7 UNREACHABLE (FF-20 coincidence, "
      "geometry excludes it). Electron-excess 5/3=n_C/N_c is a real geometric ratio, a mechanism CANDIDATE, held. This SHARPENS "
      "4848: not 's unpinned' but 's capped below the needed value.' Durable wins untouched (why-three, hierarchy mechanism, "
      "flavor skeleton, CKM F684, EW, muon (24/π²)⁶). Peak-convergence discipline held — elegant integers not banked.",
      undefined_at_g and (p_at_cap < g) and abs(elec_excess_geom/E_obs - 1) < 0.01,
      "gate=NO: exponent capped <genus=5<7 (g unreachable), 5/3=n_C/N_c candidate held; structural stands K899; sharpens 4848 (capped not merely unpinned); durable wins untouched")

# ---- SCORE -----------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok); total = len(results)
print("\n" + "=" * 96)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 96)
print(f"SCORE: {passed}/{total}")
print("=" * 96)
print(f"""
ROUND-5 (07-25) the REAL D_IV^5 s→1 Shilov boundary Toeplitz spectrum — closes the 4850-open lane (Elie, pull 25e, K899):
  * Built the rank-2 Gindikin/FK boundary spectrum (mult a=n-2=3, genus=n_C=5, rank=2) — the real thing, not the disk stand-in.
  * PRE-REGISTERED GATE = NO: integrability caps the boundary singularity strength at s<genus=5 (ladder s<genus-a/2=7/2), so the
    achievable μ→τ bulk exponent maxes at p≈1.70 ≪ observed p=6.96=g. g=7 needs s=7>genus=5 → NON-INTEGRABLE → UNREACHABLE.
    The geometry does not merely fail to force g=7 — it FORBIDS it. FF-20 coincidence, not banked.
  * Electron/k=1 excess 5/3 = n_C/N_c = genus/a is a GENUINE D_IV^5 ratio matching E=1.66 to 0.4% — a mechanism CANDIDATE (bulk
    genus falloff ÷ boundary multiplicity), held not banked (needs mechanism + free flattening depth; doesn't rescue the gate).
  => STRUCTURAL STANDS (K898/K899); sharpens 4848 (s CAPPED below the needed value, not merely unpinned). ≥2 free inputs > one
     external scale allowed. Durable wins untouched (why-three, hierarchy mechanism, flavor skeleton, CKM F684, EW, muon).
""")
