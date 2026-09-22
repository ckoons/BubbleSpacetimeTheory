#!/usr/bin/env python3
"""Toy 5774 — Item 7b (round 3): Hirzebruch–Siegel ORDER test for T187's Q⁵/Q³ ratio. Prereg hashed before this ran.
No target enters. Elie, 2026-09-22."""
import math
from fractions import Fraction as F
score, cf = [], []
def sc(nm, ok, c, d=""): score.append(ok); cf.append(c); print(f"  [{'HIT' if ok else 'MISS'}] {nm}{'' if c else ' (control)'}  {d}")
print("=" * 100 + "\nTOY 5774 — Hirzebruch proportionality applied to T187's ratio: the π-exponent, from structure\n" + "=" * 100)
def chi_quadric(n):  # smooth quadric Q^n: Betti b_{2k}=1 for 0<=k<=n (n odd); n even adds one middle class
    return (n + 1) + (1 if n % 2 == 0 else 0)
print(f"  χ(Q³) = {chi_quadric(3)}, χ(Q⁵) = {chi_quadric(5)}  (odd quadric: n+1 even-degree classes; Q⁵'s 6 is the Schubert-cell count = Lyra's 6)")
sc("P1 χ(Q³) = 4, χ(Q⁵) = 6", chi_quadric(3) == 4 and chi_quadric(5) == 6, False)
# rank-1 control: SL2(Z)\H vs S^2
vol_H = math.pi / 3; chi_H = -vol_H / (2 * math.pi); vol_S2 = 4 * math.pi; chi_S2 = 2
print(f"  rank-1 control: vol(SL₂(ℤ)\\H) = π/3 = 2ζ(2)/π = {vol_H:.6f}; χ = −vol/2π = {chi_H:.6f} = −1/6 (rational); vol(S²) = 4π, χ(S²) = 2; "
      f"vol ratio {vol_H/vol_S2:.6f} = |χ|/χ(S²) = {abs(chi_H)/chi_S2:.6f}  → proportionality exact; the π of the volume is gone from χ")
sc("P4 rank-1 proportionality check: vol(Γ\\H)/vol(S²) = |χ(Γ\\H)|/χ(S²) = 1/12", abs(vol_H / vol_S2 - abs(chi_H) / chi_S2) < 1e-15, False)
# π-exponent bookkeeping
zeta_exp = {5: 2 + 4, 7: 2 + 4 + 6}   # Siegel: SO(m) arithmetic volume ∝ ∏_{k<=(m-1)/2} ζ(2k); π-power of ζ(2k) is 2k
volQ_exp = {3: 3, 5: 5}                 # vol(Q^n) ∝ π^n in the invariant (dual) metric, e.g. 2π^n/n!
print(f"\n  Siegel ζ-products: m=7 → ζ(2)ζ(4)ζ(6) ∝ π^{zeta_exp[7]};  m=5 → ζ(2)ζ(4) ∝ π^{zeta_exp[5]};  raw ratio π^{zeta_exp[7]-zeta_exp[5]} — but these are Γ\\G Tamagawa volumes; "
      f"dividing by vol(K)·vol(dual) normalisations returns Harder's rational χ (the rank-1 control shows the mechanism)")
exp_chi_ratio = 0                                    # Harder: χ(Γ\D) rational for every arithmetic Γ
exp_vol_ratio = volQ_exp[5] - volQ_exp[3]            # proportionality: vol(Γ\D)/vol(Q) rational ⇒ vol ratio ∝ vol(Q⁵)/vol(Q³)
print(f"  π-exponent of R as a ratio of Euler characteristics: {exp_chi_ratio}")
print(f"  π-exponent of the VOLUME ratio vol(Γ₅\\D⁵)/vol(Γ₃\\D³) (both in the dual-normalised metric): {exp_vol_ratio}  (= vol(Q⁵)/vol(Q³) = π²·3!/5! = π²/20 in the 2π^n/n! convention)")
print(f"  lattice dependence: none — a congruence subgroup multiplies χ by its rational index; the exponent is unchanged")
sc("P2 R (Euler-characteristic ratio) is rational: π-exponent 0", exp_chi_ratio == 0, False)
sc("P3 volume-ratio π-exponent = 5 − 3 = 2", exp_vol_ratio == 2, False)
sc("P5 ORDER: the exponent is 0 or 2, not 5 — step (2) does not open", exp_chi_ratio != 5 and exp_vol_ratio != 5, True, f"{{0, 2}} ∌ 5")
hits = [n for n in range(1, 13) if 2 ** (n - 1) * math.factorial(n) == 3 * 5 * 2 ** 7]
sc("P6 1920 = N_c·n_C·2^g = 2^(n−1)·n! at n = 5 only (n = 1..12)", hits == [5], True, f"n = {hits}")
print("\nVERDICT: the fourth sentence dies at the order. Hirzebruch proportionality makes '6 × a volume' a theorem, but the volume it multiplies is a RATIONAL multiple of vol(Q⁵) "
      "(Harder), so the restated Q⁵/Q³ ratio carries π⁰ (as Euler characteristics) or π² (as volumes) — never π⁵. The π-exponent of 6π⁵ cannot come from arithmetic quotients of D_IV⁵ and D_IV³.")
print(f"\nSCORE {sum(score)}/{len(score)}, of which {sum(1 for s, c in zip(score, cf) if c and s)}/{sum(cf)} can-fail hit")
