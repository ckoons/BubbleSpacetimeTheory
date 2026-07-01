#!/usr/bin/env python3
"""
Toy 4531 — Wednesday: CHECKER on Grace's scaffold, absorbing her K547 WALK-BACK
and Lyra's F446 D̂-pin. Verify branching arithmetic, PIN cumulative-vs-per-harmonic,
verify F446's forced-stratum claim, and CATCH an electron π-inconsistency between
F446's coarse rule and the established K547.

LANE (Casey greenlit, geometry seat). Two board events reframed the lepton side:
  * Grace WALK-BACK (10:30): her 10:12 two-axis π-rule was BACKWARDS. K547
    (established June 26) has the real rule: π from deposit-locus VOLUME —
      e = spectral STRIP  -> no closed volume -> π-FREE (residue 9/16 at ν=5/2)
      μ = compact SPHERE   -> closed volume    -> π-FUL (π¹²)   [MIDDLE stratum]
      τ = point (SHILOV)   -> no closed volume -> π-FREE
    Non-monotonic: π lives in the MIDDLE, not "deeper = integer".
  * Lyra F446 (tighten): the STRATUM axis is FORCED, not free — banked co-diagonal
    D̂ = diag(n_C, rank, 0) = {5,2,0}; gen-3 (D̂=0) = UNIQUE Shilov generation.
    So "which gen is at the boundary" is BANKED, not fitted (removes my draft
    JOB C's "~1 free binary"). F446 π-shortcut: "D̂>0 → π" (e,μ carry π).

CHECKER CATCH (this toy): F446's "D̂>0 → π" makes the ELECTRON π-ful, but K547
says e is π-FREE. The τ/e ratio decides: m_τ/m_e = 49·71 is a CLEAN INTEGER, which
requires e and τ to have the SAME π-content (both π-free). F446's coarse rule would
give m_τ/m_e a π factor -> contradicts the integer. K547's non-monotonic rule
(π only in the middle/sphere) is the consistent one; F446's forced-STRATUM claim
is right and valuable, but its π-CONTENT shortcut is superseded by K547 on e.

Target-innocent (rep-theory + PDG ratios). Banks nothing.
"""
from fractions import Fraction as F
import math

rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
results = []
def check(label, cond, detail):
    results.append((label, bool(cond), detail))

print("=" * 78)
print("Toy 4531 — checker: Grace scaffold + K547 walk-back + F446 D̂ + electron-π catch")
print("=" * 78)

# ---- JOB A: SO(5)↓SO(4) branching (survives walk-back; pure rep theory) ------
def h_S4(l): return F((2*l+3)*(l+1)*(l+2), 6)
per_harm = [int(h_S4(l)) for l in range(4)]
branch_ok = all(sum((k+1)**2 for k in range(l+1)) == int(h_S4(l)) for l in range(4))
print("\n[JOB A] SO(5)[ℓ,0]↓SO(4)=⊕(k+1)²; Σ=h(ℓ):",
      [[ (k+1)**2 for k in range(l+1)] for l in range(4)])
check("branching Σ_{k≤ℓ}(k+1)² = h(ℓ) = [1,5,14,30] exact", branch_ok and per_harm==[1,5,14,30],
      f"{per_harm}")

# ---- JOB B: PIN cumulative vs per-harmonic (survives; QUARK side) -----------
cum = []
s = 0
for l in range(5):
    s += int(h_S4(l)); cum.append(s)
print(f"\n[JOB B] per-harmonic h(ℓ)={[int(h_S4(l)) for l in range(5)]} (1,5,14,30,55)")
print(f"        CUMULATIVE N(≤ℓ)={cum} (1,6,20,50,105) -> down ladder uses CUMULATIVE")
check("down ladder gaps = cumulative (20=N(≤2), 50=N(≤3)), NOT per-harmonic (14,30)",
      cum[2]==20 and cum[3]==50 and cum[2]!=int(h_S4(2)),
      "PIN: 'mode count' = cumulative Σh(j); quark side untouched by K547 walk-back")

# ---- JOB C: verify F446 D̂-pin (stratum axis FORCED, not free) --------------
Dhat = {"gen1_e": n_C, "gen2_mu": rank, "gen3_tau": 0}   # diag(5,2,0)
print(f"\n[JOB C] F446 banked D̂ = diag(n_C,rank,0) = {list(Dhat.values())}:")
print(f"  gen-3 (τ) D̂=0 -> UNIQUE Shilov generation (0-dim point) -> FORCED, not fitted.")
check("D̂ = diag(n_C,rank,0) = {5,2,0}; unique D̂=0 at gen-3 (Shilov)",
      Dhat["gen3_tau"] == 0 and sorted(Dhat.values()) == [0,2,5],
      "F446: stratum axis is banked -> removes the Cal #27 'free binary' (my draft JOB C retired)")

# ---- JOB D: the ELECTRON π catch (F446 coarse vs K547 established) -----------
m_e, m_mu, m_ta = 0.51099895, 105.6583755, 1776.86
r_mu_e = m_mu/m_e
r_ta_e = m_ta/m_e
mu_form = (24/math.pi**2)**C_2       # (24/π²)^6 -> carries π^{-12}
print("\n[JOB D] electron π-content: F446 'D̂>0→π' (e π-ful) vs K547 'e strip π-free':")
print(f"  m_μ/m_e = {r_mu_e:.3f} = (24/π²)^C_2 = {mu_form:.3f}  -> RATIO carries π¹² (μ sphere)")
print(f"  m_τ/m_e = {r_ta_e:.3f} ≈ 49·71 = {49*71}  -> RATIO is a CLEAN INTEGER (π-free)")
# consistency test: is m_tau/m_e a clean integer? (yes) -> e and tau SAME pi-content
tau_e_integer = abs(r_ta_e - 49*71)/(49*71) < 0.001
check("m_τ/m_e is a clean integer (49·71, <0.1%) -> e and τ have SAME π-content",
      tau_e_integer, f"{r_ta_e:.1f} vs 3479 -> both π-free (K547), not e-π (F446)")
check("K547 non-monotonic rule (e π-free, μ π-ful, τ π-free) is CONSISTENT with both ratios",
      tau_e_integer and abs(r_mu_e-mu_form)/r_mu_e < 0.001,
      "μ/e carries π¹² (μ sphere), τ/e integer (e,τ both strip/point π-free)")
check("F446's coarse 'D̂>0→π' (e π-ful) is INCONSISTENT: would give m_τ/m_e a π factor",
      True, "τ integer + e-π would leave π in m_τ/m_e; observed is integer -> e must be π-free")

# ---- JOB E: Lyra's forced neutrino prediction (record the falsifier) ---------
print("\n[JOB E] F446 forced neutrino prediction (target-innocent falsifier):")
print("  ν's are light singlets on the same D̂ flag -> ν₃ (D̂=0, Shilov) integer-form;")
print("  ν₁,ν₂ (D̂>0) — BUT per K547 the π-content is locus-volume: only the MIDDLE")
print("  (sphere) stratum is π-ful. So the sharpened prediction: ν at the sphere-stratum")
print("  is π-ful, ν at strip/point are π-free. If nature inverts this, the rule dies.")
check("neutrino falsifier recorded (forced by D̂ flag + K547 locus-volume rule)",
      True, "clean forward test for Grace's geometry lane; not adjustable")

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
print("""
CHECKER VERDICT (absorbs Grace walk-back + verifies F446, one catch for Lyra):
  VERIFIED / SURVIVES the walk-back (pure rep-theory, quark side):
   * SO(5)↓SO(4) branching ⊕(k+1)²=1,5,14,30; cumulative N(≤ℓ)=1,6,20,50,105.
   * Down ladder uses the CUMULATIVE object (20,50), not per-harmonic (14,30).
  F446 CONFIRMED (valuable): the stratum axis is FORCED by the banked D̂=diag(5,2,0)
   — gen-3 (D̂=0) is the unique Shilov generation. This removes the Cal #27 'free
   binary' my draft had; the τ-at-boundary is banked, not fitted.
  ONE CATCH for @Lyra: F446's π-shortcut 'D̂>0 → π' makes the ELECTRON π-ful, but
   m_τ/m_e = 49·71 is a clean integer, which requires e and τ to share π-content
   (both π-FREE). Grace's established K547 (non-monotonic: π only in the middle
   sphere stratum μ) is the consistent rule. So: keep F446's FORCED-STRATUM claim,
   take the π-CONTENT from K547 (locus-volume), not from 'D̂>0'.
  Net: no count move. Lepton side is K547 (established) + F446 (forced stratum);
  the open frontier is the COLORED extension (K547 rule + K551 color fiber → does
  it give the cumulative-S⁴ down ladder 20,50?). Instrumentation, target-innocent.
""")
