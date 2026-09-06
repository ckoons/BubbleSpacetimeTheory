#!/usr/bin/env python3
"""Toy 5712 — E5. G_km = ∫_0^∞ {x/k}{x/m} dx/x², b_k = ∫_1^∞ {x/k} dx/x², d_N² = 1 − bᵀG⁻¹b (K1862 G).
Method (independent of Cal §863's trigamma reduction): exact piecewise-quadratic integration over the first K0 periods
P = lcm(k,m), then the tail Σ_{n≥K0} ∫_0^P f(u)(u+nP)^{-2} du expanded in moments M_j = ∫_0^P f u^j du with Hurwitz zetas.
Control: Cal's three entries and ‖ρ₁‖² = log 2π − γ. Prediction stated in the post: entries agree to 25 digits; d_N² log N at N = 60 near Keeper's 1.02·C."""
import mpmath as mp, math, json, os, sys, time
from math import gcd
mp.mp.dps = 40; HERE = os.path.dirname(os.path.abspath(__file__)); t0 = time.time()
K0 = 3; JMAX = 60
def pieces(k, m):
    P = k * m // gcd(k, m)
    bps = sorted(set([0, P] + [k * i for i in range(1, P // k + 1)] + [m * i for i in range(1, P // m + 1)]))
    out = []
    for a, b in zip(bps[:-1], bps[1:]):
        # on (a,b): {u/k} = u/k - fk, {u/m} = u/m - fm  with floors constant
        fk = a // k; fm = a // m
        # product = (u/k - fk)(u/m - fm) = u^2/(km) - u(fk/m + fm/k) + fk fm
        out.append((mp.mpf(a), mp.mpf(b), mp.mpf(1) / (k * m), -(mp.mpf(fk) / m + mp.mpf(fm) / k), mp.mpf(fk * fm)))
    return P, out
def int_quad_over_shifted_sq(a, b, A, B, C, s):
    # ∫_a^b (A u^2 + B u + C)/(u+s)^2 du, closed form
    def F(u):
        v = u + s
        return A * (v - 2 * s * mp.log(v) - s * s / v) + B * (mp.log(v) + s / v) - C / v
    return F(b) - F(a)
def gram(k, m):
    P, pcs = pieces(k, m)
    tot = mp.mpf(0)
    for n in range(K0):                       # first K0 periods exactly
        for (a, b, A, B, C) in pcs:
            if n == 0 and a == 0:              # near 0 the integrand is A u^2/u^2 = A on the first piece (fk=fm=0): handle as ∫ (A u^2+Bu+C)/u^2 with B=C=0
                tot += A * (b - a) if (B == 0 and C == 0) else int_quad_over_shifted_sq(a, b, A, B, C, mp.mpf(0))
            else:
                tot += int_quad_over_shifted_sq(a, b, A, B, C, mp.mpf(n * P))
    # tail: Σ_{n>=K0} ∫_0^P f(u) (u+nP)^{-2} du = Σ_j (-1)^j (j+1) M_j P^{-2-j} ζ(2+j, K0)
    M = []
    for j in range(JMAX + 1):
        s = mp.mpf(0)
        for (a, b, A, B, C) in pcs:
            s += A * (b ** (j + 3) - a ** (j + 3)) / (j + 3) + B * (b ** (j + 2) - a ** (j + 2)) / (j + 2) + C * (b ** (j + 1) - a ** (j + 1)) / (j + 1)
        M.append(s)
    tail = mp.fsum((-1) ** j * (j + 1) * M[j] * mp.mpf(P) ** (-2 - j) * mp.zeta(2 + j, K0) for j in range(JMAX + 1))
    return tot + tail
def bvec(k):
    # b_k = ∫_1^∞ {x/k} dx/x² = ln(k)/k + (1/k) Σ_{n≥1} [ln((n+1)/n) − 1/(n+1)] = (ln k + 1 − γ)/k  (exact; ∫_0^k u/(u+nk)^2 du in closed form)
    return (mp.log(k) + 1 - mp.euler) / k
print("controls vs Cal §863")
c11 = gram(1, 1); c12 = gram(1, 2); c23 = gram(2, 3); c13 = gram(1, 3)
ref = {'11': mp.log(2 * mp.pi) - mp.euler, '12': mp.mpf('0.772209255990873139861302506682'), '23': mp.mpf('0.441103509279402176327335920469'), '13': mp.mpf('0.57500346946218395431513196827')}
for name, v in (('11', c11), ('12', c12), ('23', c23), ('13', c13)):
    print(f"  G{name} = {mp.nstr(v, 28)}  ref {mp.nstr(ref[name], 28)}  |diff| {mp.nstr(abs(v - ref[name]), 3)}", flush=True)
# b_1 control: ∫_1^∞ {x} dx/x² = 1 − γ  (classical)
print(f"  b_1 = {mp.nstr(bvec(1), 25)}  (1 − γ = {mp.nstr(1 - mp.euler, 25)})", flush=True)
C = 2 + mp.euler - mp.log(4 * mp.pi)
for N in (int(a) for a in (sys.argv[1:] or ['60'])):
    G = mp.matrix(N, N); b = mp.matrix(N, 1)
    for k in range(1, N + 1):
        b[k - 1] = bvec(k)
        for m in range(1, k + 1):
            G[k - 1, m - 1] = G[m - 1, k - 1] = gram(k, m)
    x = mp.lu_solve(G, b); d2 = 1 - (b.T * x)[0]
    print(f"  N = {N}: d_N² = {mp.nstr(d2, 12)}, d_N² log N = {mp.nstr(d2 * mp.log(N), 8)}, /C = {mp.nstr(d2 * mp.log(N) / C, 6)}  (C = 2+γ−log 4π = {mp.nstr(C, 10)})  [{time.time()-t0:.0f}s]", flush=True)
    json.dump({'N': N, 'dN2': mp.nstr(d2, 20), 'dN2logN_over_C': mp.nstr(d2 * mp.log(N) / C, 10)}, open(os.path.join(HERE, f'.nb_gram_5712_N{N}.json'), 'w'))
