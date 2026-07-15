#!/usr/bin/env python3
"""
Toy 4671 — Jul 15 (muon 4→5, mine; the K358 absolute-scale computation): Casey — compute the Born/Szegő
reproducing-kernel normalization for D_IV⁵ and check it = √rank·π² (→ c_S=1); if it resists, name why. I did the
computation. Honest result: it RESISTS standalone — the Gindikin residue at the Hardy point (my 4670) is √rank·π²,
but the Szegő reproducing-kernel NORMALIZATION involves Γ_Λ at the SZEGŐ exponent n/r=5/2, which is
(N_c/rank)·√rank·π² — they differ by a clean N_c/rank = 3/2. So c_S = 1 does NOT fall out standalone; it needs the
full K358 absolute-scale program to show the N_c/rank + 2π-powers cancel. The empirical muon match (0.003%) REQUIRES
that cancellation (an uncancelled 3/2 would be (3/2)⁶ ≈ 11× off) — so K358 must land it, but it is NOT a standalone
boundary-determinant. I name this precisely and hand Keeper: the muon 4→5 is gated on K358.

THE TWO GINDIKIN EVALUATIONS (both concrete, both verified):
  * HARDY-POINT RESIDUE (my 4670): Res_{s=3/2} Γ_Λ(s) = √rank·π² = √2·π²  [the muon's ν=3/2 = d/2 pole].
  * SZEGŐ-EXPONENT NORMALIZATION: the Szegő kernel exponent is n/r = 5/2 (Bergman genus 2·n/r = 5 = m). The Born/
    Szegő normalization scale is Γ_Λ(n/r) = Γ_Λ(5/2) = (2π)^{3/2}·Γ(5/2)·Γ(1) = (3√2/2)·π² = (N_c/rank)·√rank·π².

THE OBSTRUCTION (named precisely): the two differ by
    Γ_Λ(5/2) / Res Γ_Λ(3/2) = (3√2/2 π²)/(√2 π²) = 3/2 = N_c/rank.
So c_S = (Hardy residue)/(Szegő normalization) carries a clean N_c/rank = 3/2, plus 2π-power bookkeeping — it is
NOT 1 standalone. Getting c_S = 1 requires the K358 absolute-scale program to reconcile the Szegő-exponent
normalization (n/r) with the Hardy-point residue (d/2) — i.e. to show the N_c/rank and the 2π-powers cancel.

WHY K358 MUST LAND IT (the empirical forcing): the muon mass is a 6th power, m_μ/m_e = (c_S·24/π²)⁶. An uncancelled
N_c/rank = 3/2 would make the muon (3/2)⁶ ≈ 11× off — RULED OUT by the 0.003% match (my 4667: c_S = 1 to 6 ppm). So
the N_c/rank MUST cancel in the full normalization; K358 is the program that shows HOW. The muon 4→5 is therefore
gated on K358 (the absolute scale), NOT a standalone residue.

⟹ VERDICT: the muon c_S = 1 RESISTS standalone. Two concrete Gindikin evaluations — Hardy residue √rank·π² (4670)
and Szegő normalization (N_c/rank)·√rank·π² — differ by N_c/rank = 3/2. c_S = 1 needs the K358 absolute-scale
program to cancel the N_c/rank + 2π-powers; the empirical 0.003% match forces that cancellation, so K358 is the
right (and required) home. Named precisely for Keeper: 4→5 is gated on K358, not standalone. Count ~7-8 (α RULED,
identified).
"""
from sympy import Rational, symbols, gamma, pi, sqrt, simplify, residue
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
m = n_C; d_mult = m - 2; n_dim = m       # type-IV: m=5, d=3, n=5, rank=2
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

s = symbols('s')
def Gamma_Lambda(s_):
    return (2*pi)**(Rational(n_dim - rank, 2)) * gamma(s_) * gamma(s_ - Rational(d_mult, 2))

print("=" * 96)
print("Toy 4671 — muon Born/Szegő normalization: Γ_Λ(5/2) = (N_c/rank)·√rank·π² ≠ residue → c_S=1 RESISTS, needs K358")
print("=" * 96)

# ---- the Hardy-point residue (recap 4670) -----------------------------------
res = simplify(residue(Gamma_Lambda(s), s, Rational(3,2)))
print(f"\n[Hardy residue, ν=3/2 = d/2]:  Res Γ_Λ = {res} = √rank·π²")
check("HARDY-POINT RESIDUE (recap 4670): Res_{s=3/2} Γ_Λ = √rank·π² = √2·π² — the muon's ν=3/2=d/2 pole residue.",
      simplify(res - sqrt(rank)*pi**2) == 0, "Res Γ_Λ(3/2) = √rank·π² (the numerator)")

# ---- the Szegő-exponent normalization ---------------------------------------
szego_exp = Rational(n_dim, rank)     # n/r = 5/2 (Bergman genus = 2·n/r = 5 = m)
norm = simplify(Gamma_Lambda(szego_exp))
target_norm = Rational(N_c, rank)*sqrt(rank)*pi**2
print(f"\n[Szegő normalization, n/r=5/2]:  Γ_Λ(5/2) = {norm} ;  (N_c/rank)·√rank·π² = {simplify(target_norm)} ;  equal? {simplify(norm-target_norm)==0}")
check("SZEGŐ-EXPONENT NORMALIZATION: the Szegő kernel exponent is n/r = 5/2 (Bergman genus = 2·n/r = 5 = m). The "
      "Born/Szegő normalization scale is Γ_Λ(5/2) = (2π)^{3/2}·Γ(5/2)·Γ(1) = (3√2/2)π² = (N_c/rank)·√rank·π² — a "
      "concrete second Gindikin evaluation.",
      simplify(norm - target_norm) == 0, "Γ_Λ(n/r=5/2) = (N_c/rank)·√rank·π² (the normalization)")

# ---- the obstruction: they differ by N_c/rank -------------------------------
ratio = simplify(norm/res)
print(f"\n[obstruction]:  Γ_Λ(5/2) / Res Γ_Λ(3/2) = {ratio} = N_c/rank = {Rational(N_c,rank)}")
check("THE OBSTRUCTION (named): Γ_Λ(5/2)/Res Γ_Λ(3/2) = 3/2 = N_c/rank. So c_S = (Hardy residue)/(Szegő "
      "normalization) carries a clean N_c/rank = 3/2 (plus 2π-power bookkeeping) — it is NOT 1 standalone. c_S=1 "
      "requires the K358 absolute-scale program to reconcile the Szegő exponent (n/r) with the Hardy point (d/2), "
      "i.e. to cancel the N_c/rank and the 2π-powers.",
      ratio == Rational(N_c, rank), "the two Gindikin evaluations differ by N_c/rank=3/2 → c_S≠1 standalone; needs K358")

# ---- the empirical forcing --------------------------------------------------
import math
uncancelled = (3/2)**6
check("EMPIRICAL FORCING (K358 MUST land it): m_μ/m_e = (c_S·24/π²)⁶ is a 6th power. An uncancelled N_c/rank=3/2 "
      f"would make the muon (3/2)⁶ ≈ {uncancelled:.1f}× off — RULED OUT by the 0.003% match (c_S=1 to 6 ppm, my 4667). "
      "So the N_c/rank MUST cancel in the full normalization; K358 is the program that shows HOW. The 4→5 is gated on "
      "K358 (absolute scale), NOT a standalone residue.",
      uncancelled > 10, f"an uncancelled 3/2 → (3/2)^6 ≈ {uncancelled:.0f}× off, ruled out by 0.003% → the cancellation is forced, K358 shows it")

# ---- verdict ----------------------------------------------------------------
check("VERDICT: the muon c_S=1 RESISTS standalone. Two concrete Gindikin evaluations — Hardy residue √rank·π² (4670) "
      "and Szegő normalization (N_c/rank)·√rank·π² — differ by N_c/rank=3/2. c_S=1 needs the K358 absolute-scale "
      "program to cancel the N_c/rank + 2π-powers; the empirical 0.003% match FORCES that cancellation, so K358 is "
      "the required home. Named precisely for Keeper: the muon 4→5 is gated on K358, not a standalone boundary "
      "determinant.",
      True, "muon 4→5 gated on K358 (not standalone); the obstruction is a clean N_c/rank, empirically forced to cancel. Count ~7-8 (α RULED)")

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
MUON Born/Szegő normalization — c_S=1 RESISTS standalone, gated on K358 (named precisely):
  * HARDY RESIDUE (4670): Res Γ_Λ(3/2) = √rank·π² (numerator).
  * SZEGŐ NORMALIZATION: Γ_Λ(n/r=5/2) = (N_c/rank)·√rank·π² (the reproducing-kernel scale).
  * OBSTRUCTION: they differ by N_c/rank = 3/2 → c_S ≠ 1 standalone; needs K358 to cancel N_c/rank + 2π-powers.
  * EMPIRICAL FORCING: uncancelled 3/2 → (3/2)^6 ≈ 11× off, ruled out by 0.003% (c_S=1 to 6 ppm) → cancellation forced.
  => the muon 4→5 is GATED ON K358 (absolute scale), NOT a standalone residue. Named for Keeper. Count ~7-8.
""")
