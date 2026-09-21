#!/usr/bin/env python3
"""Toy 5770 — Item 7 step 1 (K1915 §2, round-2 prompt): the three mechanism sentences the corpus holds for
m_p/m_e = 6π⁵, each EVALUATED from its own named inputs, target-innocent (no measured value enters).
(a) T187 sketch: K_{Q⁵}(0,0)/K_{Q³}(0,0), "volume ratio of the 5D to 3D domains".
(b) Vol 2 Ch 6: "Bergman heat-kernel coefficient a₁(D_IV⁵) = C₂·π^{n_C}" vs the corpus's a₁ = −1875 (F63).
(c) T2487 × T2488: (n_C+1) cells × π^{n_C} bulk volume; T2351's K-type (1,0) Casimir.
Elie, 2026-09-21. Investigate, not gate. Lyra's reading is the other half."""
import math, os, re
π = math.pi; rank, N_c, n_C, C_2, g, N_max = 2, 3, 5, 6, 7, 137
score, cf = [], []
def sc(nm, ok, d=""): score.append(ok); cf.append(False); print(f"  [{'HIT' if ok else 'MISS'}] {nm}  {d}")
print("=" * 100 + "\nTOY 5770 — where does 6π⁵ live? the three sentences, evaluated\n" + "=" * 100)
claim = C_2 * π ** n_C
print(f"the claim's number (never compared to a measurement here): C_2·π^n_C = {claim:.6f}")

print("\n(a) T187's sketch — Hua volumes, vol(D_IV^n) = π^n / (2^(n−1)·n!)  [Hua 1963; T187 quotes π⁵/1920 for n=5]")
vol = lambda n: π ** n / (2 ** (n - 1) * math.factorial(n))
v5, v3 = vol(5), vol(3)
print(f"    vol(D_IV⁵) = π⁵/1920 = {v5:.6f}     vol(D_IV³) = π³/24 = {v3:.6f}")
print(f"    K(0,0) = 1/vol.  K₅/K₃ = vol₃/vol₅ = 80/π² = {v3/v5:.6f};  vol₅/vol₃ = π²/80 = {v5/v3:.6f}")
print(f"    factor the sentence would need: 6π⁵ / (80/π²) = 3π⁷/40 = {claim/(v3/v5):.4f};  6π⁵ / vol₅ = 6·1920 = {claim/v5:.1f}")
sc("(a) T187's volume ratio equals π²/80 (Keeper's number), not 6π⁵", abs(v5 / v3 - π ** 2 / 80) < 1e-12 and abs(v5 / v3 - claim) > 1)
sc("(a) the only part of the sentence that survives is the π-EXPONENT of vol(D_IV⁵) = n_C; its rational part 1/1920 is dropped", True)

print("\n(b) Vol 2 Ch 6's 'a₁ = C₂·π^{n_C}' — the Seeley–DeWitt expansion on a Riemannian manifold of real dim d:")
print("    tr e^{−tΔ} ~ (4πt)^{−d/2} [ a₀ + a₁ t + … ],  a₀ = vol,  a₁ = (1/6)∫R   (universal: Gilkey; the 6 is 1/6, for EVERY manifold)")
d = 2 * n_C; p = n_C  # Bergman metric of D_IV⁵ is Kähler–Einstein with Ric = −p·g, p = genus = n_C (T2334 pin; toy 3661)
R = -p * d
print(f"    D_IV⁵: d = 2n_C = {d}; Bergman metric Einstein constant −p = −{p} (T2334 pin, toy 3661) ⟹ R = −p·d = {R} (Riemannian), −p·n_C = {-p*n_C} (Kähler convention)")
print(f"    per unit volume: a₁/a₀ = R/6 = {R/6:.4f}; the π-power of the trace prefactor is (4π)^{{−n_C}} = π^{{−5}}/1024")
print("    ⟹ the heat kernel DOES contain a 6 and a π⁵ — as 1/6 and 1/(4π)⁵, both in the DENOMINATOR, times a curvature.")
print(f"    the corpus's own a₁ = −1875 = −N_c·n_C⁴ (F63, scalar K-Casimir coefficient) is a different object; check: −N_c·n_C⁴ = {-N_c*n_C**4}")
here = os.path.dirname(os.path.abspath(__file__))
t541 = open(os.path.join(here, "toy_541_five_integers_to_everything.py")).read()
m = re.search(r"mass_ratio\s*=\s*([^\n]+)", t541)
print(f"    retained instrument for T187 (toy 541, line with 'mass_ratio ='): `{m.group(0).strip() if m else 'NOT FOUND'}`  — Vol is computed there and NOT used in it")
sc("(b) no toy in play/ computes a₁(D_IV⁵) by Faraut–Korányi; toy 541 writes the number down", m is not None and "pi" in m.group(1) and "Vol" not in m.group(1))
sc("(b) 6 and π⁵ appear in the universal heat trace inverted (1/6, (4π)^−5), not as C₂·π^n_C", True)

print("\n(c) T2487 × T2488 — cells × bulk volume; T2351's K-type Casimir")
vB10 = π ** n_C / math.factorial(n_C)
cas = lambda m1, m2: m1 * (m1 + n_C) + m2 * (m2 + N_c)
print(f"    vol(unit ball ℝ^10) = π⁵/5! = {vB10:.6f} (T2487: π-exponent = complex dim = n_C);  vol(D_IV⁵) = π⁵/1920 = {v5:.6f}")
print(f"    6 = n_C + 1 (T2488 Z₂ bit) = C_2 = rank·N_c = {rank*N_c};  T2351 K-type (1,0) Casimir m₁(m₁+n_C) = {cas(1,0)}; its Dirac² = Casimir − n_C·g/4 = {cas(1,0) - n_C*g/4:.2f} (not 6)")
print(f"    products with the measures kept: 6·vol(B¹⁰) = {6*vB10:.4f};  6·vol(D_IV⁵) = {6*v5:.4f};  6·π⁵ = {claim:.2f} — the number obtains only after the rational normalisation (1/120 or 1/1920) is set to 1")
print("    what carries m_e: nothing in the sentence — 'mass = cells × π^{n_C} × m_e' names m_e as the unit by hand.")
sc("(c) the three readings of '6' coincide at n_C = 5 (n_C+1 = rank·N_c = Casimir(1,0))", n_C + 1 == rank * N_c == cas(1, 0))
sc("(c) 6·π⁵ is obtained from banked measures only by discarding their rational parts (no banked measure has π⁵ with coefficient 1)", abs(6*vB10 - claim) > 1 and abs(6*v5 - claim) > 1)

print("\n(residual, stated, not fitted) CODATA 2022 − 6π⁵ over CODATA = −1.88e-5. Its ORDER is Lyra's to state before any value (round-2 §7.3); no candidate is printed here.")
print(f"\nSCORE {sum(score)}/{len(score)} (all checks of arithmetic; nothing can-fail — this toy is an enumeration, not a prediction)")
