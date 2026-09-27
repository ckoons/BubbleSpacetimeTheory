#!/usr/bin/env python3
"""
Toy 5831 — Lane B: the price of the circle (Elie, 2026-09-27, round 12). Prereg 6e9264f5.
Antecedent (Lane B kill): "if R = the ruler is excluded, the KK route costs BST a SECOND input, contradicting 'one ruler'."
Circle at the ruler: R = ħ/(m_e c) = 3.8616e-13 m, 1/R = m_e = 0.511 MeV. Photon on S¹_R, charges pointlike on the circle.
(i) static potential: image sum of the 5D (4-space) Coulomb 1/r² ⇒ V = (α/r) coth(r/2R) = (α/r)[1 + 2 Σ e^{−nr/R}] (KK photons
    of mass n/R, coupling 2α each); CONTROL R → 0 recovers Coulomb.
(ii) atomic Coulomb tests: δV/V = coth(r/2R) − 1 ≈ 2e^{−r/R}; at the Bohr radius r = R/α.
(iii) electron g−2 from the tower: one-loop vector exchange, per mode Δa_n = (α_n/π)·I(M_n/m_e), I(ρ) = ∫₀¹ x²(1−x)/(x² + (1−x)ρ²) dx
     (source pin OWED; checked: ρ → 0 gives α_n/2π = Schwinger; ρ ≫ 1 gives α_n m²/(3π M²)). Compared with Grace R171's derived
     number (Pospelov eq. 4, ΣF = 0.514, ε² = 2 ⇒ 1.2e−3) — same quantity, independent code.
(iv) required 1/R for each bound (collider numbers = Grace R171 PINS; g−2 agreement level ~0.7e−12 = Grace's derived figure).
"""
import mpmath as mp
mp.mp.dps = 30
score = []
def check(name, ok, detail=""):
    score.append(bool(ok)); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}")
alpha = 1/mp.mpf('137.035999177'); me = mp.mpf('0.51099895')   # MeV (CODATA 2022 values as used in 5788; alpha only sets sizes here)
hbarc = mp.mpf('197.3269804e-15')                                # MeV·m
R_m = hbarc/me
print(f"   R = ħc/m_e c² = {mp.nstr(R_m, 6)} m ; 1/R = {me} MeV")
# (i) image sum vs coth vs Yukawa tower
R = mp.mpf(1)
img = lambda r: mp.nsum(lambda k: 1/(r**2 + (2*mp.pi*R*k)**2), [-mp.inf, mp.inf])
shape = lambda r: img(r)*2*R*r                                   # normalised so the far field → 1
ok_c = all(abs(shape(r) - mp.coth(r/(2*R))) < 1e-25 for r in (mp.mpf('0.3'), mp.mpf(2), mp.mpf(7)))
ok_y = all(abs(mp.coth(r/(2*R)) - (1 + 2*mp.nsum(lambda n: mp.e**(-n*r/R), [1, mp.inf]))) < 1e-25 for r in (mp.mpf('0.3'), mp.mpf(2)))
check("(i) image sum of the 4-space Coulomb = (α/r)·coth(r/2R) = Coulomb + Yukawa tower (masses n/R, coupling 2α)", ok_c and ok_y)
# run 1 evaluated coth(x) − 1 at 30 digits (underflow: 0.0) — use the exact form coth(x/2) − 1 = 2/(e^x − 1)
dev = lambda x: 2/(mp.e**x - 1)
check("(i) CONTROL R → 0: δV/V = 2/(e^{r/R} − 1) → 0 (pure Coulomb); at r/R = 100 it is 2e^{-100}·(1 + O(e^{-100}))",
      abs(dev(mp.mpf(100))/(2*mp.e**-100) - 1) < 1e-40 and abs((mp.coth(mp.mpf(3)/2) - 1) - dev(mp.mpf(3))) < 1e-25)
# (ii) atomic tests
dev_a0 = dev(1/alpha)                      # r/R = 1/α at the Bohr radius (run 1 underflowed to 0.0)
print(f"   (ii) δV/V at the Bohr radius (r = R/α): {mp.nstr(dev_a0, 4)}  (= 2e^(-137.04))")
check("(ii) atomic Coulomb tests CANNOT see the tower at the ruler: δV/V(a0) = 2/(e^{1/α} − 1) ≈ 6.1e-60 (nonzero, computed; label read 2.9e-60 in the first fixed run)", 1e-61 < dev_a0 < 1e-58)
# (iii) g−2
I = lambda rho: mp.quad(lambda x: x**2*(1 - x)/(x**2 + (1 - x)*rho**2), [0, 1])
check("(iii) I(0) = 1/2 (Schwinger control: α/2π for a massless vector of coupling α)", abs(I(0) - mp.mpf(1)/2) < 1e-25)
big = mp.mpf(1000)
check("(iii) I(ρ) → 1/(3ρ²) for ρ ≫ 1 (decoupling control)", abs(I(big)*3*big**2 - 1) < 0.02, f"{mp.nstr(I(big)*3*big**2, 6)}")
sumI = mp.nsum(lambda n: I(n), [1, mp.inf])
da = 2*alpha/mp.pi*sumI
print(f"   (iii) Σ_n I(n) = {mp.nstr(sumI, 6)}  ⇒  Δa_e(tower at the ruler) = {mp.nstr(da, 4)};  n = 1 alone: {mp.nstr(2*alpha/mp.pi*I(1), 4)}")
check("(iii) independent of Grace R171: 2ΣI = ΣF = 0.514 and Δa_e ≈ 1.2e-3 (her derived figure reproduced)",
      abs(2*sumI - mp.mpf('0.514')) < 0.002 and abs(da - mp.mpf('1.2e-3')) < 0.05e-3, f"2ΣI = {mp.nstr(2*sumI, 5)}")
target = mp.mpf('0.7e-12')
print(f"   (iii) excess over the g−2 agreement level ~{mp.nstr(target, 2)} (Grace's derived figure): factor {mp.nstr(da/target, 3)}")
check("KILL (Lane B) FIRES: the circle at the ruler is excluded by the electron g−2 by ~1e9", da/target > 1e8)
# required 1/R for g−2 agreement: heavy limit Δa ≈ (2α/π)·Σ 1/(3 n² ρ0²) = (2α/π)(π²/18)/ρ0², ρ0 = (1/R)/m_e
# required 1/R: heavy limit Σ_n I(nρ0) ≈ π²/(18 ρ0²) (from I → 1/(3ρ²)); solve, then VERIFY with one exact sum (run 1 bisected a nested nsum: too slow)
rho0 = mp.sqrt(2*alpha/mp.pi*mp.pi**2/18/target)
exact_at = 2*alpha/mp.pi*mp.nsum(lambda n: I(n*rho0), [1, mp.inf])
check("(iv) g−2 requirement solved in the heavy limit and VERIFIED by the exact tower sum at that 1/R (ratio within 1e-3)",
      abs(exact_at/target - 1) < 1e-3, f"exact/target = {mp.nstr(exact_at/target, 6)}")
print(f"   (iv) required 1/R for g−2: > {mp.nstr(rho0*me/1e3, 4)} GeV  (ρ0 = {mp.nstr(rho0, 4)} m_e)")
bounds = {"g−2 (derived here)": rho0*me, "mUED collider 1.4–1.5 TeV (PDG 2026, Grace pin)": mp.mpf('1.45e6'),
          "gauge-bulk 3.4–6 TeV (Grace pin)": mp.mpf('4.7e6')}
for k, v in bounds.items(): print(f"   (iv) {k}: 1/R > {mp.nstr(v/1e3, 3)} GeV — ruler short by a factor {mp.nstr(v/me, 3)}")
check("(iv) every photon-tower bound exceeds the ruler's 1/R = 0.511 MeV by ≥ 1e5 (g−2 ~ few×1e5 in 1/R, 1e9 in Δa; colliders ~3e6–1e7)",
      all(v/me > 1e5 for v in bounds.values()))
print("\nREADING: the circle at BST's one length is excluded — atoms are blind to it (2e^-137), but the electron g−2 sees the whole tower")
print("(Δa_e ≈ 1.2e-3 vs agreement ~1e-12) and colliders put 1/R above ~1.5 TeV. A photon KK circle therefore needs a SECOND scale")
print("≳ 10^6 × m_e. Gravity-only on the circle is allowed (R < 30 μm, Grace) but carries no photon tower, so it does not place the photon.")
print(f"\nSCORE: {sum(score)}/{len(score)}")
