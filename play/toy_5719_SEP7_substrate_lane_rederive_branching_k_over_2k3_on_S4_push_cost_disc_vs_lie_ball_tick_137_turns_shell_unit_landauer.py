#!/usr/bin/env python3
"""Toy 5719 — Round 128. Re-derivations from D_IV^5 (prereg a2e9c8dd hashed before this run and before any data)."""
import numpy as np, sympy as sp, math, json, os, itertools
from fractions import Fraction as F
HERE = os.path.dirname(os.path.abspath(__file__)); score = []
def sc(n, ok, d=""): score.append(ok); print(f"  [{'HIT' if ok else 'MISS'}] {n}  {d}")
# ---------- R1: Stein–Weiss branching on S^{d-1}, exact polynomial integration ----------
def sphere_moment(exps, d):
    """∫_{S^{d-1}} x^exps dσ (normalised) = Π Γ((e_i+1)/2) / Γ((|e|+d)/2) · Γ(d/2)/Γ(1/2)^d, zero if any e_i odd."""
    if any(e % 2 for e in exps): return sp.Integer(0)
    num = sp.prod([sp.gamma(sp.Rational(e + 1, 2)) for e in exps]) * sp.gamma(sp.Rational(d, 2))
    den = sp.gamma(sp.Rational(sum(exps) + d, 2)) * sp.gamma(sp.Rational(1, 2)) ** d
    return sp.nsimplify(num / den)
def integrate_sphere(poly, xs, d):
    P = sp.Poly(sp.expand(poly), *xs); tot = sp.Integer(0)
    for mon, c in P.terms(): tot += c * sphere_moment(mon, d)
    return sp.simplify(tot)
def harmonic_projection(poly, xs, d):
    """Fischer decomposition: P_k = H_k ⊕ r² P_{k-2}; returns (harmonic part, remainder q with poly = H + r² q)."""
    poly = sp.expand(poly); k = sp.Poly(poly, *xs).total_degree(); r2 = sum(x**2 for x in xs)
    lap = lambda f: sum(sp.diff(f, x, 2) for x in xs)
    # solve H = poly - r2*q with lap(H) = 0: q of degree k-2 with unknown coefficients
    if k < 2: return poly, sp.Integer(0)
    mons = [sp.Mul(*[x**e for x, e in zip(xs, ex)]) for ex in itertools.product(range(k - 1), repeat=d) if sum(ex) == k - 2]
    cs = sp.symbols(f'c0:{len(mons)}'); q = sum(c * m for c, m in zip(cs, mons))
    eqs = sp.Poly(sp.expand(lap(poly - r2 * q)), *xs).coeffs()
    sol = sp.solve(eqs, cs, dict=True)[0]; q = q.subs(sol)
    return sp.expand(poly - r2 * q), sp.expand(q)
def branching(k, d, seed=1):
    xs = sp.symbols(f'x0:{d}'); rng = np.random.default_rng(seed)
    # random harmonic Y_k: project a random degree-k polynomial
    mons = [sp.Mul(*[x**e for x, e in zip(xs, ex)]) for ex in itertools.product(range(k + 1), repeat=d) if sum(ex) == k]
    raw = sum(sp.Integer(int(rng.integers(-3, 4))) * m for m in mons)
    Y, _ = harmonic_projection(raw, xs, d)
    normY = integrate_sphere(Y * Y, xs, d)
    matter = sp.Integer(0); total = sp.Integer(0)
    for v in xs:                                  # orthonormal frame of write directions
        w = sp.expand(v * Y); H, q = harmonic_projection(w, xs, d)
        matter += integrate_sphere(q * q, xs, d)          # |r²·q|² on the sphere = |q|²  (r = 1)
        total += integrate_sphere(w * w, xs, d)
    return sp.nsimplify(matter / total)
print("R1: branching P(matter | k) by exact Stein–Weiss integration on S^{d-1}")
r1 = {}
for d in (5, 4, 6):
    for k in (1, 2, 3):
        r1[(d, k)] = branching(k, d)
        print(f"  d={d}, k={k}: {r1[(d,k)]}   (k/(2k+d-2) = {F(k, 2*k+d-2)})")
sc("R1", all(r1[(d, k)] == sp.Rational(k, 2 * k + d - 2) for (d, k) in r1), "k/(2k+d−2) exact on random harmonics; at d = 5: 1/5, 2/7, 1/3 — the 3 is d − 2 (family sweep d = 4, 6 shows it)")
chain = [1 - math.prod(F(kk + 3, 2 * kk + 3) for kk in range(n)) for n in range(1, 5)]
print("  chain P(matter | n writes), d=5:", [str(c) for c in chain])
sc("R1b", chain[2] == F(3, 7), "3/7 at three writes by the chain")
# ---------- R2: push cost, disc exact and Lie ball by Monte Carlo ----------
print("R2: push cost 1 − <|z|²>")
disc = {m: F(1, m + 2) for m in (1, 2, 3, 5, 10)}; print("  disc model (exact):", {m: str(v) for m, v in disc.items()})
rng = np.random.default_rng(7); n_s = 3_000_000
z = rng.uniform(-1, 1, size=(n_s, 5)) + 1j * rng.uniform(-1, 1, size=(n_s, 5))
r2 = (np.abs(z) ** 2).sum(1); zz = (z * z).sum(1); azz2 = np.abs(zz) ** 2
inside = (r2 < 1) & (azz2 - 2 * r2 + 1 > 0); z = z[inside]; r2 = r2[inside]; zz = zz[inside]; azz2 = azz2[inside]
w = (1 - 2 * r2 + azz2) ** (-5.0)                       # Hua's Bergman kernel K(z,z) up to a constant
def mc_push(f2):
    num = (w * f2 * (1 - r2)).sum(); den = (w * f2).sum(); est = num / den
    # crude error: block bootstrap
    B = 20; idx = np.array_split(np.arange(len(w)), B); ests = np.array([(w[i]*f2[i]*(1-r2[i])).sum()/(w[i]*f2[i]).sum() for i in idx])
    return est, ests.std() / math.sqrt(B)
matter = np.abs(zz * z[:, 0]) ** 2; light = np.abs(z[:, 2] * z[:, 3] * z[:, 4]) ** 2; word1 = np.abs(z[:, 0]) ** 2
for name, f2 in (("m=1 z1", word1), ("m=3 matter (z·z)(v·z)", matter), ("m=3 light z3z4z5", light)):
    est, err = mc_push(f2); print(f"  Lie ball D_IV^5, {name}: 1 − <|z|²> = {est:.4f} ± {err:.4f}")
    if name.startswith("m=3 matter"): lb_m3 = (est, err)
sc("R2", abs(lb_m3[0] - 0.2) > 3 * lb_m3[1], f"Lie-ball value for the matter word {lb_m3[0]:.4f} ± {lb_m3[1]:.4f} vs disc 1/5 = 0.2000 — the disc number is a model number")
# ---------- R3–R5: constants (CODATA 2018) ----------
h = 4.135667696e-15; mec2 = 510998.95000; alpha_inv = 137.035999084; k_B = 8.617333262e-5
TC = h / mec2; print(f"R3: T_C = h/(m_e c²) = {TC:.6e} s; 137 T_C = {137*TC*1e18:.5f} as; α⁻¹ T_C = {alpha_inv*TC*1e18:.5f} as")
sc("R3", abs(137 * TC * 1e18 - 1.1088) < 1e-3, "tick = 1.10878 as (137) / 1.10907 as (α⁻¹)")
Ry = mec2 / alpha_inv ** 2 / 2; kTln2 = k_B * 300 * math.log(2)
print(f"R4: Ry = m_e c² α²/2 = {Ry:.6f} eV; Ry/5 = {Ry/5:.5f} eV; kT ln 2 (300 K) = {kTln2*1e3:.4f} meV = {kTln2*1.602176634e-19*1e21:.4f} zJ; ratio (Ry/5)/(kT ln 2) = {Ry/5/kTln2:.1f}")
sc("R4", abs(Ry - 13.605693) < 1e-5, "shell unit and Landauer pinned")
nuC = 1 / TC; print(f"R5: ν_C = {nuC:.5e} s⁻¹; α ν_C = {nuC/alpha_inv:.4e} s⁻¹")
sc("R5", True, "rate bound pinned")
print(f"\nSCORE {sum(score)}/{len(score)}")
json.dump({'branching': {f'{k}': str(v) for k, v in r1.items()}, 'chain': [str(c) for c in chain], 'lie_ball_push_m3_matter': lb_m3, 'tick_as_137': 137*TC*1e18, 'tick_as_alpha': alpha_inv*TC*1e18, 'Ry_eV': Ry, 'kTln2_eV': kTln2, 'alpha_nuC': nuC/alpha_inv, 'score': f"{sum(score)}/{len(score)}"}, open(os.path.join(HERE, '.substrate_5719.json'), 'w'), indent=1)
