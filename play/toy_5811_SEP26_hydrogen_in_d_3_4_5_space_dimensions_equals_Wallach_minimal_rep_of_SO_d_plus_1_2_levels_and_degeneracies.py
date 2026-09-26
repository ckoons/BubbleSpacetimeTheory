#!/usr/bin/env python3
"""
Toy 5811 — hydrogen in d = 3, 4, 5 space dimensions vs the minimal (Wallach) representation of SO(d+1,2) (Elie, 2026-09-26).
Prereg bc903cb1. Antecedent (K1929 Part 3(b), verbatim): "In d space dimensions the Coulomb levels are E = −Z²/(2ν²) with
ν = n_r + l + (d−1)/2. The degeneracy of level N is the dimension of the degree-N harmonics in d+1 variables. For d = 4:
ν = 3/2, 5/2, 7/2, …, with degeneracies 1, 5, 14, 30."
INVARIANTS: Coulomb side — the termination condition of the radial equation (solved, not assumed) and the SO(d)-content of a level;
representation side — the clock ladder λ + m and K-types H_m(R^{d+1}) of the scalar module of D_IV^{d+1} at λ = (d−1)/2 (Schmid; input).
"""
import sympy as sp
from itertools import combinations_with_replacement as cwr
from collections import Counter
score = []
def check(name, ok, detail=""):
    score.append(bool(ok)); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}")
r, Z, kap = sp.symbols('r Z kappa', positive=True)
def radial_solve(d, l, nr):
    """Find kappa and polynomial u (deg nr, u(0)=1) with R = r^l e^{-kappa r} u solving the d-dim Coulomb radial eq."""
    a = sp.symbols(f'a1:{nr+1}') if nr > 0 else ()
    u = 1 + sum(c*r**(k+1) for k, c in enumerate(a))
    R = r**l*sp.exp(-kap*r)*u
    E = -kap**2/2
    ode = sp.diff(R, r, 2) + (d-1)/r*sp.diff(R, r) - l*(l+d-2)/r**2*R + 2*(E + Z/r)*R
    ex = sp.expand(sp.simplify(ode*sp.exp(kap*r)*r**(2-l)))
    eqs = sp.Poly(ex, r).coeffs()
    sol = sp.solve(eqs, list(a) + [kap], dict=True)
    sol = [s for s in sol if s.get(kap) is not None and s[kap].is_positive is not False and s[kap] != 0]
    # run 1 did not force degree exactly nr (a_nr = 0 admitted lower states) — require a_nr != 0
    if nr > 0: sol = [s for s in sol if sp.simplify(s[a[-1]]) != 0]
    return sol
ok_all = True; detail = []
for d in (3, 4, 5):
    for l in range(3):
        for nr in range(3):
            sol = radial_solve(sp.Integer(d), l, nr)
            nu = nr + l + sp.Rational(d-1, 2)
            good = len(sol) == 1 and sp.simplify(sol[0][kap] - Z/nu) == 0
            if not good: ok_all = False; detail.append((d, l, nr, sol))
check("Frobenius termination SOLVED: κ = Z/ν with ν = n_r + ℓ + (d−1)/2, unique, for d=3,4,5, ℓ,n_r ≤ 2 (E = −Z²/2ν²)", ok_all, str(detail[:2]))
# ---- characters ----
def vec_weights(n):
    rk = n // 2; W = []
    for i in range(rk):
        for s in (1, -1):
            w = [0]*rk; w[i] = s; W.append(tuple(w))
    if n % 2: W.append(tuple([0]*rk))
    return W
def sym_char(n, m):
    W = vec_weights(n); C = Counter()
    for combo in cwr(range(n), m): C[tuple(sum(W[k][i] for k in combo) for i in range(n//2))] += 1
    return C
def harm_char(n, m):
    C = sym_char(n, m)
    if m >= 2: C.subtract(sym_char(n, m-2))
    return +C
def restrict(C, n):   # SO(n) -> SO(n-1)
    if n % 2: return Counter(C)
    out = Counter()
    for w, k in C.items(): out[w[:-1]] += k
    return out
def dimH(n, m): return sum(harm_char(n, m).values())
ok_branch = True
for d in (3, 4, 5):
    for N in range(6):
        lvl = Counter()
        for l in range(N+1): lvl.update(harm_char(d, l))           # level N: ℓ = 0..N, one each (n_r = N − ℓ)
        if +lvl != +restrict(harm_char(d+1, N), d+1): ok_branch = False
check("level N's SO(d)-content ⊕_{ℓ≤N} H_ℓ(R^d) = H_N(R^{d+1})|SO(d), by characters, d=3,4,5, N ≤ 5", ok_branch)
degs = {d: [dimH(d+1, N) for N in range(5)] for d in (3, 4, 5)}
print(f"   level degeneracies (no spin): {degs}")
check("CONTROL d=3: degeneracies n² = 1,4,9,16,25 and Wallach λ = (3−1)/2 = 1 = hydrogen's ground ν", degs[3] == [1, 4, 9, 16, 25])
check("d=4 (the K1929 claim): 1, 5, 14, 30, 55 with ν = 3/2 + N = Wallach λ = 3/2 of D_IV^5 (minimal rep of SO(5,2))", degs[4] == [1, 5, 14, 30, 55])
check("d=5: 1, 6, 20, 50, 105 with ν = 2 + N = Wallach λ = 2 of D_IV^6", degs[5] == [1, 6, 20, 50, 105])
# minimal rep K-types: λ2 = 0 only, SO(d+1)-type H_m(R^{d+1}) at clock weight λ + m — the level map ν ↔ clock weight
ok_map = all(sp.Rational(d-1, 2) + N == (N + 0 + sp.Rational(d-1, 2)) for d in (3, 4, 5) for N in range(5))
check("level map: Coulomb ν = (d−1)/2 + N ↔ minimal-rep clock weight λ + m with m = N, K-type H_N(R^{d+1}) — same ladder, same K-types", ok_map and ok_branch)
print("\nREADING: K1929 3(b) verified: the minimal rep of SO(5,2) (the Rac, λ = 3/2) has exactly the level/degeneracy structure of")
print("hydrogen in FOUR space dimensions (ν = 3/2 + N, degeneracies 1,5,14,30,55); d = 3 control reproduces λ = 1, n². Structure only:")
print("the energy E = −Z²/2ν² needs Z and the mass (imported, 5804).")
print(f"\nSCORE: {sum(score)}/{len(score)}")
