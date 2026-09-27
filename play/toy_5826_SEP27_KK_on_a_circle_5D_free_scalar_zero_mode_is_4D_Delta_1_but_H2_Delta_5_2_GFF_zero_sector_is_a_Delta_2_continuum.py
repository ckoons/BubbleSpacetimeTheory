#!/usr/bin/env python3
"""
Toy 5826 — route (a), Kaluza–Klein on a circle of radius R (Elie, 2026-09-27, round 11 item 1). Prereg 2fac2431.
Antecedent (prompt): "Then the same with a Δ = 5/2 (H²) generalized free field. State what its zero mode is. Keeper's expectation,
NOT verified: a continuum (a generalized free field in 4D), not a single massless particle."
INVARIANTS: 4D unitarity boundary Δ = 1 (D_IV^4 Wallach λ = 1); Källén–Lehmann: δ(M²) = one massless particle ⇔ |x|^{-2};
a density on (0,∞) = continuum. Euclidean; R is an INPUT scale (it breaks SO(5,2)); nothing here says BST forces the circle.
"""
import mpmath as mp
mp.mp.dps = 30
score = []
def check(name, ok, detail=""):
    score.append(bool(ok)); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}")
def G0(D, r): return mp.gamma(mp.mpf(D)/2 - 1)/(4*mp.pi**(mp.mpf(D)/2)) * r**(2 - D)      # massless, D dims
def G4m(m, r): return m/(4*mp.pi**2*r)*mp.besselk(1, m*r) if m > 0 else G0(4, r)
def G3m(m, r): return mp.e**(-m*r)/(4*mp.pi*r)
R = mp.mpf(1)
def images(G, x, y, D):
    return mp.nsum(lambda k: G(D, mp.sqrt(x**2 + (y + 2*mp.pi*R*k)**2)), [-mp.inf, mp.inf])
def modes4(x, y, N=160):   # run 1: N = 60 left e^{-60·0.7} ~ 6e-19 > tolerance (truncation, not physics)
    return (G4m(0, x) + 2*mp.fsum(mp.cos(n*y/R)*G4m(n/R, x) for n in range(1, N)))/(2*mp.pi*R)
def modes3(x, y, N=160):
    return (1/(4*mp.pi*x) + 2*mp.fsum(mp.cos(n*y/R)*G3m(n/R, x) for n in range(1, N)))/(2*mp.pi*R)
# (i) 5D free massless (Δ5 = 3/2)
pts = [(mp.mpf('0.7'), mp.mpf('0.3')), (mp.mpf(2), mp.mpf(1)), (mp.mpf(5), mp.mpf('2.5'))]
err = max(abs(images(G0, x, y, 5)/modes4(x, y) - 1) for x, y in pts)
check("(i) 5D free scalar on S¹_R: image sum = KK mode sum (4D masses n/R), 3 points", err < 1e-20, f"max rel err {mp.nstr(err, 3)}")
zm = [images(G0, x, 0, 5)/(G0(4, x)/(2*mp.pi*R)) - 1 for x in (mp.mpf(4), mp.mpf(8), mp.mpf(12))]
check("(i) far field → (1/2πR)·G4_massless ∝ |x|^{-2}: the ZERO MODE is a 4D Δ = 1 massless scalar; remainder ∝ e^{-|x|/R}",
      abs(zm[2]) < abs(zm[1]) < abs(zm[0]) and abs(mp.log(zm[1]/zm[2]) - 4) < 0.3, f"remainders {[mp.nstr(z, 3) for z in zm]} (ratio e^{{-Δx/R}})")
avg = mp.quad(lambda y: images(G0, mp.mpf(2), y, 5), [0, 2*mp.pi*R])/(2*mp.pi*R)
check("(i) the y-averaged (n = 0) sector equals (1/2πR)·G4_massless EXACTLY (δ(M²) density: one massless particle)",
      abs(avg/(G0(4, mp.mpf(2))/(2*mp.pi*R)) - 1) < 1e-15)
# (ii) CONTROL 4D → 3D
err3 = max(abs(images(G0, x, y, 4)/modes3(x, y) - 1) for x, y in pts)
avg3 = mp.quad(lambda y: images(G0, mp.mpf(2), y, 4), [0, 2*mp.pi*R])/(2*mp.pi*R)
check("(ii) CONTROL 4D Δ=1 on S¹: image = mode sum, zero mode = (1/2πR)·G3_massless ∝ |x|^{-1} (3D Δ = 1/2)",
      err3 < 1e-20 and abs(avg3/(1/(4*mp.pi*2)/(2*mp.pi*R)) - 1) < 1e-15, f"err {mp.nstr(err3, 3)}")
# (iii) Δ5 = 5/2 (H²'s field): 5D GFF, correlator |X|^{-5}
F = lambda x, y: mp.nsum(lambda k: (x**2 + (y + 2*mp.pi*R*k)**2)**mp.mpf(-2.5), [-mp.inf, mp.inf])
Z = lambda x: mp.quad(lambda y: F(x, y), [0, 2*mp.pi*R])/(2*mp.pi*R)        # n = 0 sector
exact = lambda x: (mp.mpf(4)/3)/(2*mp.pi*R)*x**-4                               # images unfold: (1/2πR)∫_R (x²+y²)^{-5/2} dy
zs = [Z(x)/exact(x) - 1 for x in (mp.mpf('0.5'), mp.mpf(2), mp.mpf(6))]
check("(iii) Δ5 = 5/2: the n = 0 sector is EXACTLY (4/3)/(2πR)·|x|^{-4} at every |x| (no |x|^{-2} piece at any distance)",
      max(abs(z) for z in zs) < 1e-15, f"{[mp.nstr(z, 3) for z in zs]}")
# KL content of |x|^{-4} in 4D: flat density ρ(M²) = const reproduces it (5812's rule, exponent Δ − 2 = 0); δ(M²) gives |x|^{-2}
KL = lambda x: mp.quad(lambda M2: G4m(mp.sqrt(M2), x), [0, 1/x**2, 10/x**2, mp.inf])
sl = (mp.log(KL(mp.mpf(2))) - mp.log(KL(mp.mpf(1))))/mp.log(2)
check("(iii) 4D Källén–Lehmann: a FLAT density on (0,∞) gives exactly |x|^{-4} (slope −4): the zero sector is a Δ4 = 2 CONTINUUM",
      abs(sl + 4) < 1e-12, f"slope {mp.nstr(sl, 12)}")
print("   [restatement, not scored — run 1 scored it]  PREREG DIRECTION (Keeper's expectation, adopted): H²'s KK zero sector is a 4D GFF continuum at Δ = 2 (D_IV^4's Hardy point), "
      "NOT a massless particle; route (a) yields λ = 1 only from the Rac (Δ5 = 3/2): HOLDS by the two checks above")
print("\nREADING: KK on a circle turns the Rac's 5D free field into ONE 4D massless scalar (Δ = 1, λ = 1) plus a tower n/R; it turns H²'s")
print("Δ = 5/2 field into a Δ = 2 continuum (D_IV^4's Hardy point, ρ4 flat), not a particle. So if route (a) is BST's photon route,")
print("the 4D massless piece comes from the RAC, and the circle (radius R) is an input until BST forces it.")
print(f"\nSCORE: {sum(score)}/{len(score)}")
