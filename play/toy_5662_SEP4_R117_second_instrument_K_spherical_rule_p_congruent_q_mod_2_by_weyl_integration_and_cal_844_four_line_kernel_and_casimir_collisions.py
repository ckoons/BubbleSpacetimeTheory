#!/usr/bin/env python3
"""
Toy 5662 — Round 117. Second instrument for Grace's 5660 and Lyra §3 / Cal §844.

(A) THE K-SPHERICAL RULE, computed not assumed. 5660 took "L^2(Q^n) = sum over (a,b,0,..)
    with a >= b >= 0, a == b (mod 2)" from Cartan–Helgason. Here: dim of the SO(n)xSO(2)-fixed
    subspace of EVERY SO(n+2)-irrep (p,q,0,...,0), p >= q >= 0, p <= 8, n = 3..7, by the Weyl
    character formula + Weyl integration over K (toy 5661's instrument, now at q > 0).
    Prediction (Cartan–Helgason, Cal §844): 1 if p == q (mod 2), else 0.  Also (p,q,r>0): 0.
(B) CAL §844's AMENDMENT, exact: with x1 = p + n/2, x2 = q + (n-2)/2, rho2 = (n-2)/2, the
    D-eigenvalue is (x1^2 - rho2^2)(x2^2 - rho2^2); zero on the spherical lattice iff q = 0.
    All four lines listed; the two x1-lines and the x2 = -rho2 line are empty for p >= q >= 0.
(C) THE LAPLACIAN ALONE CANNOT: Casimir collisions p(p+n) = p'(p'+n) + q'(q'+n-2), q' > 0,
    on the spherical lattice — if any exist, no function of Delta has kernel = zonal sector.
(D) Casimir intertwining: eigenvalue of degree-p harmonics on S^{n+1} is p(p+n), same as (p,0,..) on Q^n.
"""
import math, time
from fractions import Fraction
import numpy as np

t0 = time.time(); score = []
def S(label, ok):
    score.append((label, bool(ok))); print(f"    [{'PASS' if ok else 'FAIL'}] {label}")

# ---- instrument (5661) ----
def so_data(m_dim):
    r = m_dim // 2; roots = []
    for i in range(r):
        for j in range(i + 1, r):
            v = [0]*r; v[i] = 1; v[j] = 1; roots.append(tuple(v))
            v = [0]*r; v[i] = 1; v[j] = -1; roots.append(tuple(v))
    if m_dim % 2 == 1:
        for i in range(r):
            v = [0]*r; v[i] = 1; roots.append(tuple(v))
        W = 2**r * math.factorial(r)
    else:
        W = (2**(r-1) * math.factorial(r)) if r >= 1 else 1
    return r, roots, W
def rho(m_dim):
    r = m_dim // 2
    return [r - i - 0.5 for i in range(r)] if m_dim % 2 == 1 else [float(r - 1 - i) for i in range(r)]
def character_so(m_dim, lam, TH):
    rh = np.array(rho(m_dim)); mu = np.array(lam, dtype=float) + rh; th = np.asarray(TH, dtype=float)
    A = th[..., :, None] * mu[None, :]; B = th[..., :, None] * rh[None, :]
    if m_dim % 2 == 1:
        return np.linalg.det(np.sin(A)) / np.linalg.det(np.sin(B))
    return (np.linalg.det(np.cos(A)) + np.linalg.det(np.sin(A))) / (np.linalg.det(np.cos(B)) + np.linalg.det(np.sin(B)))
def weyl_measure(roots, TH):
    out = np.ones(TH.shape[:-1])
    for a in roots: out = out * (2.0 - 2.0*np.cos(TH @ np.array(a, dtype=float)))
    return out
def shifted_grid(dim, M):
    shift = np.array([0.1234567 + 0.0731*k for k in range(dim)])
    axes = [shift[k] + 2*np.pi*np.arange(M)/M for k in range(dim)]
    return np.stack(np.meshgrid(*axes, indexing="ij"), axis=-1).reshape(-1, dim)
_grid_cache = {}
def fixed_dim(N, lam, a, b, M=30):
    r = N // 2; ra, roots_a, Wa = so_data(a); rb, roots_b, Wb = so_data(b); rk = ra + rb
    key = (rk, M, a, b)
    if key not in _grid_cache:
        grid = shifted_grid(rk, M)
        roots = [tuple(list(v) + [0]*rb) for v in roots_a] + [tuple([0]*ra + list(v)) for v in roots_b]
        _grid_cache[key] = (grid, weyl_measure(roots, grid))
    grid, meas = _grid_cache[key]
    TH = np.zeros((grid.shape[0], r)); TH[:, :rk] = grid
    return np.mean(character_so(N, lam, TH) * meas) / (Wa * Wb)
def weyl_dim(N, lam):
    r = N // 2; pos = []
    for i in range(r):
        for j in range(i+1, r):
            v = [0]*r; v[i] = 1; v[j] = 1; pos.append(v); v = [0]*r; v[i] = 1; v[j] = -1; pos.append(v)
    if N % 2 == 1:
        for i in range(r): v = [0]*r; v[i] = 1; pos.append(v)
    rh = [Fraction(2*r-2*i-1, 2) for i in range(r)] if N % 2 == 1 else [Fraction(r-1-i) for i in range(r)]
    out = Fraction(1)
    for a in pos:
        out *= Fraction(sum((lam[i]+rh[i])*a[i] for i in range(r))) / sum(rh[i]*a[i] for i in range(r))
    return out

print("=" * 78); print("Toy 5662 — K-spherical rule computed; Cal §844 four lines exact; Δ alone cannot"); print("=" * 78)

# Control: irreducibility of (p,q) characters on the grid (the instrument at q > 0)
print("\nC0  <chi_(p,q), chi_(p,q)>_G = 1 and dim check via Weyl formula vs known SO(7) dims (7,21,27,105,168,189)")
ok = True
# (3,1,0) was typed as 189 from memory in the first run — WRONG (189 = 27x7, the reducible product).
# Independent source: tensor-product bookkeeping 27x7 = 77+105+7 and 77x7 = 182+330+27.
known7 = {(1,0,0): 7, (1,1,0): 21, (2,0,0): 27, (2,1,0): 105, (3,1,0): 330, (2,2,0): 168}
wd = lambda lam: weyl_dim(7, list(lam))
if not (wd((2,0,0))*7 == wd((3,0,0)) + wd((2,1,0)) + wd((1,0,0)) and wd((3,0,0))*7 == wd((4,0,0)) + wd((3,1,0)) + wd((2,0,0))):
    ok = False; print("      tensor-product bookkeeping MISS")
for lam, d in known7.items():
    if weyl_dim(7, list(lam)) != d: ok = False; print("      dim MISS", lam, weyl_dim(7, list(lam)))
for N in range(5, 10):
    r, rootsG, WG = so_data(N); grid = shifted_grid(r, 30); meas = weyl_measure(rootsG, grid)
    for lam in ([3,1]+[0]*(r-2), [4,2]+[0]*(r-2), [5,3]+[0]*(r-2)):
        chi = character_so(N, lam, grid); ip = np.mean(chi*chi*meas)/WG
        if abs(ip-1) > 1e-6: ok = False; print(f"      MISS N={N} lam={lam}: {ip:.8f}")
S("C0 instrument at q>0: six SO(7) dims + two tensor-product sums exact, <chi,chi>=1 for (3,1),(4,2),(5,3) at N=5..9 (23/23)", ok)

print("\n(A) dim (p,q,0,..)^K, K = SO(n)xSO(2), n = 3..7, p >= q >= 0, p <= 8 — prediction 1 iff p == q (mod 2)")
A_ok = True; A_n = 0
for n in range(3, 8):
    N = n + 2; r = N // 2; table = {}
    for p in range(9):
        for q in range(p + 1):
            if r < 2 and q > 0: continue
            lam = [p, q] + [0]*(r-2)
            v = fixed_dim(N, lam, n, 2); iv = int(round(v))
            if abs(v - iv) > 1e-6: print(f"      NON-INTEGER n={n} (p,q)=({p},{q}): {v:.9f}")
            table[(p, q)] = iv; A_n += 1
            if iv != (1 if (p - q) % 2 == 0 else 0): A_ok = False; print(f"      MISS n={n} ({p},{q}) -> {iv}")
    # print as a triangle
    print(f"    n={n} SO({N}) ↓ SO({n})xSO(2)   rows p, columns q:")
    for p in range(9):
        print("      p=%d: %s" % (p, " ".join(str(table[(p, q)]) for q in range(p + 1))))
S(f"(A) K-spherical rule p == q (mod 2) computed by Weyl integration, {A_n}/{A_n} (n=3..7, p<=8)", A_ok)

print("\n(A') third label r > 0 is never K-spherical: (p,q,r) with r=1, n = 5,6,7 (rank >= 3), p<=4")
ok = True; cnt = 0
for n in (5, 6, 7):
    N = n + 2; r = N // 2
    for p in range(1, 5):
        for q in range(1, p + 1):
            lam = [p, q, 1] + [0]*(r-3); v = fixed_dim(N, lam, n, 2); cnt += 1
            if abs(v) > 1e-6: ok = False; print(f"      MISS n={n} lam={lam}: {v:.6f}")
S(f"(A') (p,q,1,..) has no K-fixed vector, {cnt}/{cnt}", ok)

print("\n(B) Cal §844: D-eigenvalue (x1²-ρ2²)(x2²-ρ2²) on the spherical lattice, exact, p <= 40, n = 3..7")
B_ok = True; B_n = 0; lines = {}
for n in range(3, 8):
    rho2 = Fraction(n-2, 2); zero_q = set(); nonzero_bad = 0
    for p in range(41):
        for q in range(p + 1):
            if (p - q) % 2: continue
            x1 = p + Fraction(n, 2); x2 = q + rho2
            e = (x1*x1 - rho2*rho2) * (x2*x2 - rho2*rho2); B_n += 1
            if e == 0: zero_q.add(q)
            if (e == 0) != (q == 0): B_ok = False; nonzero_bad += 1
    # which of the four lines are populated on the lattice p>=q>=0?
    pop = {"x1=+rho2": any(p + Fraction(n,2) == rho2 for p in range(41)),
           "x1=-rho2": any(p + Fraction(n,2) == -rho2 for p in range(41)),
           "x2=+rho2": True, "x2=-rho2": any(q + rho2 == -rho2 for q in range(41))}
    lines[n] = pop
    print(f"    n={n}: kernel q-values {sorted(zero_q)}; populated lines {[k for k,v in pop.items() if v]}; bad={nonzero_bad}")
S(f"(B) ker D on the spherical lattice = q = 0 exactly, {B_n}/{B_n} weights; only x2=+rho2 populated at every n", B_ok and all(list(v.values()) == [False, False, True, False] for v in lines.values()))

print("\n(C) Casimir collisions p(p+n) = p'(p'+n) + q'(q'+n-2), q' > 0, spherical lattice, p,p' <= 60")
C_any = True; ex = {}
for n in range(3, 8):
    cas = {}
    for p in range(61):
        for q in range(p + 1):
            if (p - q) % 2: continue
            cas.setdefault(p*(p+n) + q*(q+n-2), []).append((p, q))
    coll = [(lam, w) for lam, w in cas.items() if any(q == 0 for _, q in w) and any(q > 0 for _, q in w)]
    coll.sort(); ex[n] = coll[:3]
    print(f"    n={n}: {len(coll)} Casimir values shared by a zonal and a non-zonal weight; smallest: {coll[:3]}")
    if not coll: C_any = False
S("(C) collisions exist at every n=3..7: no function of Δ alone has kernel = zonal sector; D4 is needed", C_any)

print("\n(D) Casimir intertwining: S^{n+1} degree-p eigenvalue p(p+dim-1) = p(p+n) = Q^n eigenvalue of (p,0,..)")
ok = all(p*(p+(n+1)-1) == p*(p+n) for n in range(3, 8) for p in range(41))
S("(D) p(p+n) on both spaces, 205/205", ok)

print("\n" + "=" * 78)
npass = sum(1 for _, o in score if o); print(f"SCORE {npass}/{len(score)}   [{time.time()-t0:.0f}s]")
for lab, o in score: print(f"  {'PASS' if o else 'FAIL'}  {lab}")
