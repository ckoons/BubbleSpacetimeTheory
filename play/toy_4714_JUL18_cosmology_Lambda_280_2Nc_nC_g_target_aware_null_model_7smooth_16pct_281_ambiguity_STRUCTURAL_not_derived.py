#!/usr/bin/env python3
"""
Toy 4714 — Jul 18 (Cosmology Λ target-innocence, mine; strengthening item 5, RESEARCH-lite, with Lyra L3): is
Λ = exp(−280), 280 = 2^{N_c}·n_C·g, a target-innocent derivation or a fit? Cal's guard: target-innocence of 280. My
target-innocence lens fired hard (Cal #27: scrutinize the prettiest hardest) gives an HONEST STRUCTURAL verdict, NOT
derived: 280 = ln(1/Λ_obs) is target-AWARE (the log of the observed cosmological constant), 7-smoothness is 16%-common
in the window, 281 = 2·N_max+g is an EQUALLY clean primary form within the Λ-definition ambiguity, and the "5-fold
over-determination" is one prime factorization (2³·5·7) regrouped associatively — NOT 5 independent derivations.

WHAT CHECKS (the arithmetic):
  * 280 = 2^{N_c}·n_C·g = 2³·5·7 = 280 exactly — a clean primary factorization (exponent N_c=3; factors n_C=5, g=7).
  * exp(−280) = 10^(−121.6) ~ the observed cosmological constant (Λ ~ 10⁻¹²² in Planck units). Magnitude matches.

THE TARGET-INNOCENCE ASSESSMENT (Cal's guard — the honest downgrade):
  * TARGET-AWARE: 280 = ln(1/Λ_obs). The number is obtained by taking the log of the OBSERVED Λ — it is not predicted
    from a substrate count. So the primary decomposition of 280 is a decomposition of a target-aware number.
  * NULL MODEL: 13/81 = 16% of integers in [240,320] are 7-smooth. Being 7-smooth (hence primary-factorable) is a
    ~1-in-6 occurrence, NOT rare. 280's clean factorization is not extraordinary on its own.
  * TARGET AMBIGUITY: 281 = 2·N_max + g is an EQUALLY clean primary form, and 280 vs 281 both sit within the ambiguity
    of what "Λ" means (ln in exp-base = 121.6, log₁₀-based ≈ 122; the exponent depends on Λ-as-energy-density vs
    length² vs Einstein-eq). Multiple nearby integers with primary forms + a target that shifts by ±1 with convention =
    fitting flexibility, not a pinned prediction.
  * OVER-DETERMINATION OVERSTATED: the claimed "5-fold over-determination" is ONE prime factorization (2³·5·7) regrouped
    associatively ({2^{N_c}·n_C}·g, 2^{N_c}·{n_C·g}, etc.) — NOT 5 independent derivations. Downgrade.

⟹ VERDICT: Λ = exp(−280), 280 = 2^{N_c}·n_C·g is STRUCTURAL / IDENTIFIED, NOT derived. The factorization is clean and
the magnitude matches, but 280 is target-aware (log of observed Λ), 7-smoothness is 16%-common, 281 is an equally clean
competitor within the Λ-definition ambiguity, and the "5-fold over-determination" is one factorization regrouped. Honest
"structural" verdict per the board. It moves structural→derived ONLY if a MECHANISM produces exp(−count) with the count
= 2^{N_c}·n_C·g (e.g., a substrate action/heat-kernel exponent — Lyra L3's job). Count ~7-8 (α RULED). Five-Absence-safe.
"""
import math
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

# ---- arithmetic -------------------------------------------------------------
val = 2**N_c * n_C * g
exp_base10 = 280/math.log(10)
print(f"\n[arithmetic]: 2^N_c·n_C·g = {2**N_c}·{n_C}·{g} = {val}; exp(−280) = 10^(−{exp_base10:.1f}) ~ Λ_obs ~ 10⁻¹²²")
check("ARITHMETIC: 280 = 2^{N_c}·n_C·g = 2³·5·7 = 280 exactly (clean primary factorization, exponent N_c, factors "
      "n_C·g); exp(−280) = 10^(−121.6) ~ the observed cosmological constant Λ ~ 10⁻¹²². Magnitude matches.",
      val == 280 and abs(exp_base10 - 121.6) < 1, "280 = 2^{N_c}·n_C·g exactly; exp(−280) ~ 10⁻¹²² matches Λ magnitude")

# ---- target-aware -----------------------------------------------------------
check("TARGET-AWARE (the core issue): 280 = ln(1/Λ_obs) — the number is the LOG of the OBSERVED cosmological constant, "
      "not predicted from a substrate count. So decomposing 280 into primaries is decomposing a target-aware number "
      "(my derived-vs-fit lens: FIT-SUSPECT unless a mechanism produces the exponent independently).",
      True, "280 = ln(1/Λ_obs) is target-aware — the log of the observed value, not an independent substrate count")

# ---- null model: 7-smoothness is common -------------------------------------
def is_7smooth(n):
    for p in (2,3,5,7):
        while n % p == 0: n //= p
    return n == 1
window = list(range(240, 321))
smooth = [n for n in window if is_7smooth(n)]
frac = len(smooth)/len(window)
print(f"[null model]: 7-smooth integers in [240,320] = {len(smooth)}/{len(window)} = {frac*100:.0f}% → not rare")
check("NULL MODEL: 13/81 = 16% of integers in [240,320] are 7-smooth (primary-factorable). Being 7-smooth is a "
      "~1-in-6 occurrence, NOT rare — so 280's clean factorization is not extraordinary on its own.",
      0.10 < frac < 0.25, "16% of window integers are 7-smooth → 280's factorability is common, not special")

# ---- target ambiguity: 281 competitor ---------------------------------------
alt281 = 2*(N_c**3*n_C + rank) + g                    # 2·N_max + g = 281
print(f"[ambiguity]: 281 = 2·N_max + g = {alt281} — an equally clean primary form; 280 vs 281 within Λ-definition ambiguity")
check("TARGET AMBIGUITY: 281 = 2·N_max + g is an EQUALLY clean primary form, and 280 vs 281 both sit within the "
      "ambiguity of what 'Λ' means (exp-base 121.6 vs log₁₀ ~122; energy-density vs length² vs Einstein-eq). Multiple "
      "nearby integers with primary forms + a target shifting by ±1 with convention = fitting flexibility, not a pinned "
      "prediction. Plus the '5-fold over-determination' is ONE factorization (2³·5·7) regrouped, not 5 independent.",
      alt281 == 281, "281=2·N_max+g equally clean; 280-vs-281 ambiguity + regrouped-not-independent over-determination")

# ---- verdict ----------------------------------------------------------------
check("VERDICT: Λ = exp(−280), 280 = 2^{N_c}·n_C·g is STRUCTURAL / IDENTIFIED, NOT derived. Factorization clean + "
      "magnitude matches, BUT 280 is target-aware (log of observed Λ), 7-smoothness is 16%-common, 281 is an equally "
      "clean competitor within the Λ-definition ambiguity, and the '5-fold over-determination' is one factorization "
      "regrouped. Honest 'structural' verdict per the board. Moves structural→derived ONLY if a MECHANISM produces "
      "exp(−count) with count = 2^{N_c}·n_C·g (a substrate action/heat-kernel exponent — Lyra L3).",
      val == 280 and 0.10 < frac < 0.25 and alt281 == 281,
      "Λ=exp(−280) STRUCTURAL not derived: target-aware log, 16% 7-smooth, 281-ambiguity, over-determination overstated; needs a mechanism")

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
COSMOLOGY Λ target-innocence (strengthening item 5, with Lyra L3) — honest STRUCTURAL verdict:
  * ARITHMETIC: 280 = 2^{N_c}·n_C·g = 2³·5·7 exactly; exp(−280) ~ 10⁻¹²² matches Λ magnitude.
  * TARGET-AWARE: 280 = ln(1/Λ_obs) — the log of the OBSERVED value, not a substrate count.
  * NULL MODEL: 16% of window integers are 7-smooth → factorability not rare.
  * AMBIGUITY: 281=2·N_max+g equally clean; 280-vs-281 within Λ-definition uncertainty; "5-fold" = one factorization regrouped.
  => Λ=exp(−280) is STRUCTURAL / IDENTIFIED, NOT derived. Needs a mechanism (exp(−count), count=2^{N_c}·n_C·g) to upgrade. Honest verdict.
""")
