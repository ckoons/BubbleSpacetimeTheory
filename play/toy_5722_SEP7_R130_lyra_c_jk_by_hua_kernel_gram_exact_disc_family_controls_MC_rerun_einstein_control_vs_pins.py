#!/usr/bin/env python3
"""Toy 5722 — Lyra c657a24f scored on Hua's kernel (exact Gram), controls, MC re-run, Einstein control vs pins."""
import itertools, math, json, os, time
from fractions import Fraction as F
import numpy as np, sympy as sp
from sympy.polys.matrices import DomainMatrix
from sympy import QQ
HERE = os.path.dirname(os.path.abspath(__file__)); score = []; canfail = []
def sc(n, ok, cf, d=""): score.append(ok); canfail.append(cf); print(f"  [{'HIT' if ok else 'MISS'}] {n}{'' if cf else ' (not can-fail)'}  {d}")
def poch(a, N): return math.prod(a + i for i in range(N)) if N else 1
def mono_list(n, m): return [e for e in itertools.product(range(m + 1), repeat=n) if sum(e) == m]
def multinom(N, parts): return math.factorial(N) // math.prod(math.factorial(p) for p in parts)
def kernel_coeff(n, a, b, al, be):
    """[z^al wbar^be] of s^a q^b qbar^b, s = z.wbar, q = z.z."""
    tot = 0
    for gam in mono_list(n, b):
        eps = tuple(al[i] - 2 * gam[i] for i in range(n))
        if min(eps) < 0: continue
        delta = tuple((be[i] - eps[i]) // 2 if (be[i] - eps[i]) >= 0 and (be[i] - eps[i]) % 2 == 0 else -1 for i in range(n))
        if min(delta) < 0: continue
        tot += multinom(b, gam) * multinom(b, delta) * multinom(a, eps)
    return tot
GRAM = {}
def gram(n, m):
    """Gram matrix of monomials of degree m for Bergman space of D_IV^n (kernel exponent -n), as dict (al,be)->Fraction; up to a common constant."""
    if (n, m) in GRAM: return GRAM[(n, m)]
    mons = mono_list(n, m); idx = {e: i for i, e in enumerate(mons)}
    C = {}
    for al in mons:
        for be in mons:
            if any((al[i] - be[i]) % 2 for i in range(n)): continue
            v = 0
            for b in range(0, m // 2 + 1):
                N = m - b; a = N - b
                if a < 0: continue
                v += F(poch(n, N), math.factorial(N)) * math.comb(N, b) * 2**a * (-1)**b * kernel_coeff(n, a, b, al, be)
            if v: C[(al, be)] = v
    # parity blocks
    blocks = {}
    for e in mons: blocks.setdefault(tuple(x % 2 for x in e), []).append(e)
    G = {}
    for par, es in blocks.items():
        M = DomainMatrix([[QQ(C.get((x, y), F(0)).numerator, C.get((x, y), F(0)).denominator) for y in es] for x in es], (len(es), len(es)), QQ)
        Minv = M.inv().to_Matrix()
        for i, x in enumerate(es):
            for j, y in enumerate(es):
                if Minv[i, j] != 0: G[(x, y)] = F(int(Minv[i, j].p), int(Minv[i, j].q))
    GRAM[(n, m)] = G; return G
def poly_dict(expr, zs):
    P = sp.Poly(sp.expand(expr), *zs); return {tuple(int(x) for x in mon): F(int(c.p), int(c.q)) for mon, c in zip(P.monoms(), P.coeffs())}
def norm2(pd, n, m):
    G = gram(n, m); return sum(ca * cb * G[(a, b)] for a, ca in pd.items() for b, cb in pd.items() if (a, b) in G)
def harmonic_part(poly, k, zs):
    zz = sum(v**2 for v in zs)
    if k < 2: return sp.expand(poly)
    n = len(zs); mons = [sp.Mul(*[v**e for v, e in zip(zs, ex)]) for ex in mono_list(n, k - 2)]
    cs = sp.symbols(f'c0:{len(mons)}'); q = sum(c * mm for c, mm in zip(cs, mons))
    lap = lambda f: sum(sp.diff(f, v, 2) for v in zs)
    sol = sp.solve(sp.Poly(sp.expand(lap(poly - zz * q)), *zs).coeffs(), cs, dict=True)[0]
    return sp.expand(poly - zz * q.subs(sol))
def cost(n, j, k):
    zs = sp.symbols(f'z0:{n}'); zz = sum(v**2 for v in zs); m = 2 * j + k
    psi = sp.expand(zz**j * harmonic_part(zs[0]**k, k, zs)) if n > 1 else zs[0]**m
    pd = poly_dict(psi, zs); N0 = norm2(pd, n, m)
    N1 = sum(norm2(poly_dict(zs[i] * psi, zs), n, m + 1) for i in range(n))
    return 1 - N1 / N0
t0 = time.time()
print("Q1: Lyra's twelve rationals by the Hua-kernel Gram route (n=5)")
lyra = {(0,0):F(1,2),(0,1):F(10,21),(0,2):F(45,98),(0,3):F(25,56),(1,0):F(5,12),(1,1):F(25,63),(1,2):F(55,144),(1,3):F(10,27),(2,0):F(5,14),(2,1):F(15,44),(2,2):F(65,198),(2,3):F(7,22)}
mine = {}
for (j, k) in lyra:
    mine[(j, k)] = cost(5, j, k); print(f"  ({j},{k}) m={2*j+k}: kernel-Gram c = {mine[(j,k)]} = {float(mine[(j,k)]):.4f}   Lyra {lyra[(j,k)]}   [{time.time()-t0:.0f}s]")
sc("Q1", all(mine[w] == lyra[w] for w in lyra), True, f"{sum(mine[w]==lyra[w] for w in lyra)}/12 exact matches")
print("Q2: disc control n=1")
disc = [cost(1, 0, m) for m in range(8)]; print("  ", [str(d) for d in disc])
sc("Q2", all(disc[m] == F(1, m + 2) for m in range(8)), False, "c = 1/(m+2), m = 0..7")
print("Q3: family n=3..7 — constant and matter word (1,1)")
fam = {n: (cost(n, 0, 0), cost(n, 1, 1)) for n in range(3, 8)}
for n, (c0, c11) in fam.items(): print(f"  n={n}: const {c0} = {float(c0):.4f}; (1,1) {c11} = {float(c11):.4f}")
lyra_fam = {3: 0.3429, 4: 0.3750, 5: 0.3968, 6: 0.4125, 7: 0.4242}
sc("Q3", all(fam[n][0] == F(1, 2) for n in fam) and all(abs(float(fam[n][1]) - lyra_fam[n]) < 6e-5 for n in fam), True, "const 1/2 at every n; (1,1) to four digits")
print("Q4: MC re-run at (1,1), ~10x sample")
rng = np.random.default_rng(1130); keep = []
for chunk in range(120):
    w = rng.uniform(-1, 1, size=(6_000_000, 5)) + 1j * rng.uniform(-1, 1, size=(6_000_000, 5))
    r2 = (np.abs(w)**2).sum(1); ww = (w*w).sum(1); msk = (r2 < 1) & (np.abs(ww)**2 - 2*r2 + 1 > 0); keep.append(w[msk])
W = np.concatenate(keep); R2 = (np.abs(W)**2).sum(1); WW = (W*W).sum(1)
zs5 = sp.symbols('z0:5'); Y1 = W[:, 0]; f2 = np.abs(WW * Y1)**2
B = 25; idx = np.array_split(np.arange(len(f2)), B); est = np.array([(f2[i]*R2[i]).sum()/f2[i].sum() for i in idx]); cmc = 1 - est.mean(); smc = est.std()/math.sqrt(B)
print(f"  samples {len(W)}: c_MC(1,1) = {cmc:.5f} ± {smc:.5f};  25/63 = {25/63:.5f};  pull {(cmc-25/63)/smc:+.2f}σ   [{time.time()-t0:.0f}s]")
sc("Q4", abs(cmc - 25/63) <= 2*smc, True, f"pull {(cmc-25/63)/smc:+.2f}σ")
print("Q5: Einstein control against the pins (Millikan 1916 l.309/l.1188/l.2001; Huang 2020 l.264-267)")
cmin, cmax = float(min(lyra.values())), float(max(lyra.values()))
print(f"  (D2) slope = (1-c) h/e, c in [{cmin:.3f}, {cmax:.3f}] -> photoelectric h would read {6.57*(1-cmax):.2f}..{6.57*(1-cmin):.2f} e-27 vs Planck radiation 6.55e-27 (Millikan: 6.57, 0.3%); deficit {cmin*100:.0f}-{cmax*100:.0f}% vs 0.5% stated precision -> refuted; Huang 2020: max rel. deviation of h 1.6e-5 -> c-drift between words (0.318..0.5) refuted at 1e4x")
print("  (D1) W = fixed shell turns: no ν-dependence by construction -> empty")
sc("Q5", True, False, "D2 REFUTED, D1 EMPTY (pre-known; scored, not discovered)")
print("Q6: threshold law — pinned Wigner form sigma ~ (E-E0)^(l+1/2), l = R^3 outgoing partial wave (Andersen eq.5); dictionary carries no excess-energy variable -> outcome (c)")
sc("Q6", True, False, "nothing compared")
print(f"\nSCORE {sum(score)}/{len(score)}, of which {sum(1 for s,c in zip(score,canfail) if c)}/{sum(canfail)} can-fail lines hit")
json.dump({'kernel_gram_c': {f"{j},{k}": str(v) for (j,k), v in mine.items()}, 'family': {n: (str(a), str(b)) for n,(a,b) in fam.items()}, 'mc_11': [cmc, smc, len(W)], 'score': f"{sum(score)}/{len(score)}"}, open(os.path.join(HERE, '.record_5722.json'), 'w'), indent=1)
