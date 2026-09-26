#!/usr/bin/env python3
"""
Toy 5817 — exchange shape of a gapless Δ field in 4D (Elie, 2026-09-26, round 8 item 2). Prereg 75daf52b. NO strengths.
Antecedent (K1930 Part 2, verbatim): "A coupling to the stress tensor gives Newton × (R/r)^{2Δ−1} (Goldberg–Nath's 'ungravity' form),
which is 1/r⁵ in total … Eöt-Wash k = 5."  Source pin (data/sources_elie_2026-09-26/arXiv_0706.3898_Goldberg_Nath.txt):
Eq. (6): f_dU(r) = 4π ∫ d³q/(2π)³ e^{−iq·r}/(q²)^{2−dU};  Eq. (7): V = −(m1 m2 G/r)[1 + (R_G/r)^{2dU−2}];  abstract: "(R_G/r)^{2dU−1}".
INVARIANT: the 4D spectral density ρ4 ∝ (M²)^{Δ−2} of the restricted boundary field (toy 5812 (e)).
Two independent routes to the shape: (A) Källén–Lehmann Yukawa superposition ∫ dM² ρ4 e^{−Mr}/(4πr);
(B) the 3D Fourier transform of |q|^{2Δ−4} (G–N's f_dU), analytic continuation checked against direct quadrature where convergent.
Eöt-Wash parametrisation: V = −G M_a M_b/r · β_k (1 mm/r)^{k−1}  ⇒ total power r^{−k}.
"""
import mpmath as mp
mp.mp.dps = 30
score = []
def check(name, ok, detail=""):
    score.append(bool(ok)); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}")
def V_KL(D, r):
    a = D - 2
    return mp.quad(lambda M2: M2**a * mp.e**(-mp.sqrt(M2)*r)/(4*mp.pi*r), [0, 1/r**2, 10/r**2, mp.inf])
def slope(f, r1=1, r2=2): return (mp.log(abs(f(r2))) - mp.log(abs(f(r1))))/mp.log(mp.mpf(r2)/r1)
# (A) KL route
for D, exp_ in ((2, -3), (2.5, -4), (3, -5)):
    s = slope(lambda r: V_KL(D, r))
    check(f"(A) KL route: Δ = {D}: V ∝ r^{exp_}", abs(s - exp_) < 1e-12, f"slope {mp.nstr(s, 15)}")
# (B) Fourier route: f(r) = (2/(π r)) ∫_0^∞ q^{s-1} sin(qr) dq with s = 2Δ-2; continuation Γ(s) sin(πs/2) r^{-s}
def f_cont(D, r):
    s = 2*D - 2
    pref = mp.pi/2 if s == 0 else mp.gamma(s)*mp.sin(mp.pi*s/2)
    return 2/(mp.pi*r) * pref / r**s
# verify the continuation formula by direct oscillatory quadrature where it converges (0 < s < 1)
okq = True
for s in (mp.mpf('0.3'), mp.mpf('0.7')):
    # run 1 started quadosc at 0 and lost ~4e-7 to the q^(s-1) endpoint singularity — split at q = 1
    direct = mp.quad(lambda q: q**(s-1)*mp.sin(2*q), [0, 1]) + mp.quadosc(lambda q: q**(s-1)*mp.sin(q*2), [1, mp.inf], omega=2)
    if abs(direct - mp.gamma(s)*mp.sin(mp.pi*s/2)/2**s) > 1e-15: okq = False
check("(B) ∫_0^∞ q^{s−1} sin(qr) dq = Γ(s) sin(πs/2)/r^s verified by direct quadrature (s = 0.3, 0.7; r = 2)", okq)
check("(B) CONTROL Δ = 1: f = 1/r exactly (Newton; G–N's own check 'dU = 1 … fdU(r) = 1/r')", abs(f_cont(1, mp.mpf(3)) - 1/mp.mpf(3)) < 1e-25)
for D, k in ((2, 3), (2.5, 4), (3, 5)):
    s = slope(lambda r: f_cont(D, r))
    check(f"(B) Fourier route: Δ = {D}: f_dU ∝ r^−{k}", abs(s + k) < 1e-20, f"slope {mp.nstr(s, 12)}")
# routes agree up to one constant
ratio = [V_KL(2.5, r)/f_cont(2.5, r) for r in (mp.mpf(1), mp.mpf(2), mp.mpf('3.5'))]
check("(A) and (B) agree in SHAPE at Δ = 5/2 (constant ratio at r = 1, 2, 3.5)", max(ratio) - min(ratio) < 1e-20*abs(ratio[0]) + 1e-25,
      f"ratio {mp.nstr(ratio[0], 10)}")
# vertex independence: static sources, q = (0, q⃗): the spin-1/2 projector piece P^{00} = −η^{00} + q^0 q^0/q² is q-independent
import sympy as sp
q1, q2, q3 = sp.symbols('q1 q2 q3', real=True)
eta = sp.diag(1, -1, -1, -1); qv = sp.Matrix([0, q1, q2, q3]); q2s = (qv.T*eta*qv)[0]
Pmn = lambda m, n: -eta[m, n] + (eta*qv)[m]*(eta*qv)[n]/q2s
P00 = sp.simplify(Pmn(0, 0))
P0000 = sp.simplify(sp.Rational(1, 2)*(Pmn(0, 0)*Pmn(0, 0) + Pmn(0, 0)*Pmn(0, 0)) - sp.Rational(1, 3)*Pmn(0, 0)*Pmn(0, 0))
check("vertex: for static sources the tensor structure (G–N's P^{μν}, P^{μνσρ}) contracts to a CONSTANT (P^{00} = −1, P^{0000} = 2/3): "
      "the stress-tensor/trace vertex rescales strength, the shape is f_dU for every vertex", P00.is_number and P0000.is_number, f"P00={P00}, P0000={P0000}")
k_direct = 2*2.5 - 1; k_T = 1 + (2*2.5 - 2)
print(f"   Eöt-Wash k: direct scalar vertex k = {k_direct:.0f}; stress-tensor/trace vertex (G–N Eq. 7: Newton × (R/r)^(2dU−2)) k = {k_T:.0f}")
check("PREREG DIRECTION: total exponent 4 at Δ = 5/2 for BOTH vertices ⇒ Eöt-Wash k = 4 (K1930's k = 5 comes from G–N's abstract, which contradicts their Eq. 7)",
      k_direct == 4 and k_T == 4)
print("   note: G–N (body) require dU >= 2 for a spin-0 operator coupled to the trace and dU > 3 for spin 2; BST's boundary field is a")
print("   Δ = 5/2 SCALAR, so only scalar/trace couplings are admissible; unitarity-allowed. Strength (Λ_U, κ*) not computed — the ruler.")
print(f"\nSCORE: {sum(score)}/{len(score)}")
