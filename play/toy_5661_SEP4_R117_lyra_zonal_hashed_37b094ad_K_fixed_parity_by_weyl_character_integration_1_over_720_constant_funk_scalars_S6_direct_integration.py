#!/usr/bin/env python3
"""
Toy 5661 — Round 117, Lyra's §4 (note sha256 37b094ad, hashed BEFORE this run).

Three hashed predictions:
  P1  Q^n = SO(n+2)/(SO(n)xSO(2)), n = 3..7, p <= 12: the K-fixed subspace of the
      SO(n+2)-irrep (p,0,...,0) has dimension 1 for p even, 0 for p odd.
      Method here (independent of Lyra's polynomial argument): Weyl character formula
      from the highest weight, then Weyl integration over K on a shifted torus grid
      (exact constant-term extraction for trigonometric polynomials of bounded degree).
  P2  n = 5: sum_{p<=P, p even} dim(p,0,0) / (P(P+5))^3 -> 1/720.   Exact rationals.
  P3  Funk scalars c_p/pi at n = 5 (S^6, Gegenbauer index 5/2), p = 0,2,4,6:
      2, 5/6, 35/64, 105/256 by direct numerical integration of the great-circle
      integral of the zonal harmonic.
Controls (machinery must pass before P1 is read):
  C1  chi(theta->0) = dim(p,0,...,0) = C(N+p-1,p) - C(N+p-3,p-2).
  C2  irreducibility: <chi,chi>_G = 1 by Weyl integration over G itself.
  C3  the sphere: H = SO(n+1) gives one fixed vector for EVERY p (the instrument
      must separate K from H — Lyra's "not (a)").
Family sweep (beyond the hash; labelled): K = SO(a) x SO(b), a+b = n+2, b >= 1.
Extra (beyond the hash; labelled): Fourier-cosine positivity of C_p^{(n/2)} for p <= 12,
  n = 3..7 (the ingredient of Lemma 3's "c_p > 0 for all even p").
"""
import itertools, math, sys, time
from fractions import Fraction
import numpy as np
import mpmath as mp

t0 = time.time()
score = []   # (label, ok)

def S(label, ok):
    score.append((label, bool(ok)))
    print(f"    [{'PASS' if ok else 'FAIL'}] {label}")

# ----------------------------------------------------------------------------- roots / Weyl
def so_data(m_dim):
    """Torus rank, positive roots (as coefficient vectors on torus coords), |W| for SO(m_dim)."""
    r = m_dim // 2
    roots = []
    for i in range(r):
        for j in range(i + 1, r):
            v = [0] * r; v[i] = 1; v[j] = 1; roots.append(tuple(v))
            v = [0] * r; v[i] = 1; v[j] = -1; roots.append(tuple(v))
    if m_dim % 2 == 1:
        for i in range(r):
            v = [0] * r; v[i] = 1; roots.append(tuple(v))
        W = 2 ** r * math.factorial(r)
    else:
        W = (2 ** (r - 1) * math.factorial(r)) if r >= 1 else 1
    return r, roots, W

def rho(m_dim):
    r = m_dim // 2
    if m_dim % 2 == 1:
        return [r - i - 0.5 for i in range(r)]
    return [float(r - 1 - i) for i in range(r)]

def character_so(m_dim, lam, TH):
    """Weyl character of SO(m_dim) irrep with highest weight lam (list of length r),
    evaluated at torus angles TH: array (..., r). Uses the determinantal forms:
      B_r: det[sin(mu_j th_i)] / det[sin(rho_j th_i)]
      D_r: (det[cos(mu_j th_i)] + det[sin(mu_j th_i)]) / (det[cos(rho_j th_i)] + det[sin(rho_j th_i)])
    (D_r: even sign changes = half the sum of the two hyperoctahedral sums; sin-part vanishes
     when the last coordinate of the weight is 0, which is our case, but keep it general.)"""
    r = m_dim // 2
    rh = np.array(rho(m_dim))
    mu = np.array(lam, dtype=float) + rh
    th = np.asarray(TH, dtype=float)
    # matrices M[..., i, j] = f(mu_j * th_i)
    A = th[..., :, None] * mu[None, :]
    B = th[..., :, None] * rh[None, :]
    if m_dim % 2 == 1:
        num = np.linalg.det(np.sin(A)); den = np.linalg.det(np.sin(B))
    else:
        num = np.linalg.det(np.cos(A)) + np.linalg.det(np.sin(A))
        den = np.linalg.det(np.cos(B)) + np.linalg.det(np.sin(B))
    return num / den

def dim_harmonic(N, p):
    c = math.comb
    return c(N + p - 1, p) - (c(N + p - 3, p - 2) if p >= 2 else 0)

def weyl_measure(roots, TH):
    """prod over positive roots of |1 - e^{i alpha(theta)}|^2 = 2 - 2 cos(alpha.theta)."""
    out = np.ones(TH.shape[:-1])
    for a in roots:
        out = out * (2.0 - 2.0 * np.cos(TH @ np.array(a, dtype=float)))
    return out

def shifted_grid(dim, M):
    shift = np.array([0.1234567 + 0.0731 * k for k in range(dim)])
    axes = [shift[k] + 2 * np.pi * np.arange(M) / M for k in range(dim)]
    mesh = np.meshgrid(*axes, indexing="ij")
    return np.stack(mesh, axis=-1).reshape(-1, dim)

def fixed_dim(N, p, a, b, M=40):
    """dim of SO(a)xSO(b)-fixed subspace of (p,0,..,0) of SO(N), a+b=N, by Weyl integration."""
    r = N // 2
    ra, roots_a, Wa = so_data(a)
    rb, roots_b, Wb = so_data(b)
    rk = ra + rb                      # K torus rank; == r unless a,b both odd (then r-1)
    grid = shifted_grid(rk, M)        # (M^rk, rk)
    # K roots in G-torus coordinates: SO(a) on coords 0..ra-1, SO(b) on ra..ra+rb-1
    roots = [tuple(list(v) + [0] * rb) for v in roots_a] + [tuple([0] * ra + list(v)) for v in roots_b]
    meas = weyl_measure(roots, grid)
    TH = np.zeros((grid.shape[0], r)); TH[:, :rk] = grid
    lam = [p] + [0] * (r - 1)
    chi = character_so(N, lam, TH)
    val = np.mean(chi * meas) / (Wa * Wb)
    return val

# ============================================================================ CONTROLS
print("=" * 78)
print("Toy 5661 — Lyra §4 (37b094ad): parity by Weyl integration · 1/720 · Funk scalars")
print("=" * 78)
print("\nC1  Weyl dimension formula prod <lam+rho,a>/<rho,a> for lam=(p,0,..,0) = C(N+p-1,p) - C(N+p-3,p-2)   [N = 5..9, p = 0..12]")
print("    (the exact theta->0 limit of the determinantal character; the raw ratio at theta~1e-3 is a 0/0 that")
print("     loses all digits at rank >= 3 — first version of this control failed for that reason, fixed here)")
def weyl_dim(N, lam):
    r = N // 2
    pos = []
    for i in range(r):
        for j in range(i + 1, r):
            v = [0]*r; v[i] = 1; v[j] = 1; pos.append(v)
            v = [0]*r; v[i] = 1; v[j] = -1; pos.append(v)
    if N % 2 == 1:
        for i in range(r):
            v = [0]*r; v[i] = 1; pos.append(v)
    rh = [Fraction(2*r - 2*i - 1, 2) for i in range(r)] if N % 2 == 1 else [Fraction(r - 1 - i) for i in range(r)]
    out = Fraction(1)
    for a in pos:
        num = sum((lam[i] + rh[i]) * a[i] for i in range(r)); den = sum(rh[i] * a[i] for i in range(r))
        out *= Fraction(num) / den
    return out
ok = True
for N in range(5, 10):
    r = N // 2
    for p in range(13):
        wd = weyl_dim(N, [p] + [0]*(r-1)); d = dim_harmonic(N, p)
        if wd != d:
            ok = False; print(f"      MISS N={N} p={p}: Weyl {wd} vs harmonic {d}")
S("C1 highest weight (p,0,..,0) IS the harmonic-polynomial rep: Weyl dim = C(N+p-1,p)-C(N+p-3,p-2), 65/65 exact", ok)

print("\nC1b grid orthogonality <chi_p, chi_q>_G = delta_pq on the shifted grid   [N = 5..9, (p,q) in {0,1,2,3,7}^2]")
ok = True; cnt = 0
for N in range(5, 10):
    r, rootsG, WG = so_data(N)
    grid = shifted_grid(r, 40 if r < 4 else 36)
    meas = weyl_measure(rootsG, grid)
    chis = {p: character_so(N, [p] + [0]*(r-1), grid) for p in (0, 1, 2, 3, 7)}
    for p in chis:
        for q in chis:
            ip = np.mean(chis[p] * chis[q] * meas) / WG; cnt += 1
            if abs(ip - (1 if p == q else 0)) > 1e-6:
                ok = False; print(f"      MISS N={N} p={p} q={q}: {ip:.8f}")
S(f"C1b grid orthogonality delta_pq, {cnt}/{cnt}", ok)

print("\nC2  irreducibility <chi,chi>_G = 1 by Weyl integration over G   [N = 5..9, p = 0,1,2,5,12]")
ok = True
for N in range(5, 10):
    r, rootsG, WG = so_data(N)
    grid = shifted_grid(r, 40 if r < 4 else 36)
    meas = weyl_measure(rootsG, grid)
    for p in (0, 1, 2, 5, 12):
        chi = character_so(N, [p] + [0] * (r - 1), grid)
        ip = np.mean(chi * chi * meas) / WG
        if abs(ip - 1) > 1e-6:
            ok = False; print(f"      MISS N={N} p={p}: <chi,chi>={ip:.8f}")
S("C2 irreducibility control <chi,chi>_G = 1, 25/25", ok)

# ============================================================================ P1 + C3 + family
print("\nP1  K = SO(n) x SO(2) fixed dimension in (p,0,...,0) of SO(n+2), n = 3..7, p = 0..12")
print("    prediction (hashed): 1 for p even, 0 for p odd")
p1_ok = True; rows = {}
for n in range(3, 8):
    N = n + 2
    vals = []
    for p in range(13):
        v = fixed_dim(N, p, n, 2)
        iv = int(round(v))
        if abs(v - iv) > 1e-6:
            print(f"      NON-INTEGER n={n} p={p}: {v:.9f}")
        vals.append(iv)
        if iv != (1 if p % 2 == 0 else 0):
            p1_ok = False
    rows[n] = vals
    print(f"    n={n} SO({N}) ↓ SO({n})xSO(2): {vals}")
S("P1 parity/multiplicity-one, 65/65 (n=3..7, p<=12)", p1_ok)

print("\nC3  the sphere H = SO(n+1): fixed dimension must be 1 for EVERY p (separates K from H)")
c3_ok = True
for n in range(3, 8):
    N = n + 2
    vals = [int(round(fixed_dim(N, p, n + 1, 1))) for p in range(13)]
    print(f"    n={n} SO({N}) ↓ SO({n+1}):        {vals}")
    if vals != [1] * 13: c3_ok = False
S("C3 sphere control all-ones, 65/65", c3_ok)

print("\nFAMILY SWEEP (beyond the hash): K = SO(a) x SO(b), a+b = n+2, b >= 1, p = 0..8")
print("    expectation from Lyra's Lemma-1 argument generalised: b = 1 -> all ones; b >= 2 -> parity")
fam_ok = True; fam_n = 0
for n in range(3, 8):
    N = n + 2
    for b in range(1, N // 2 + 1):
        a = N - b
        vals = [int(round(fixed_dim(N, p, a, b, M=32))) for p in range(9)]
        exp = [1] * 9 if b == 1 else [1 if p % 2 == 0 else 0 for p in range(9)]
        fam_n += 1
        flag = "" if vals == exp else "   <-- DEVIATES"
        if vals != exp: fam_ok = False
        print(f"    SO({N}) ↓ SO({a})xSO({b}): {vals}{flag}")
S(f"family sweep SO(a)xSO(b): parity is the b>=2 property, {fam_n}/{fam_n} as expected", fam_ok)

# ============================================================================ P2
print("\nP2  n = 5: sum_{p<=P, p even} dim(p,0,0) / (P(P+5))^3 -> 1/720  (exact rationals)")
def dim7(p): return dim_harmonic(7, p)
prev = None; p2_rows = []
for P in (200, 400, 800, 1600, 3200, 6400):
    s_even = sum(dim7(p) for p in range(0, P + 1, 2))
    s_all = sum(dim7(p) for p in range(0, P + 1))
    ratio_even = Fraction(s_even, (P * (P + 5)) ** 3)
    ratio_all = Fraction(s_all, (P * (P + 5)) ** 3)
    inv_even = 1 / ratio_even; inv_all = 1 / ratio_all
    p2_rows.append((P, inv_even, inv_all))
    print(f"    P={P:5d}: 1/ratio_even = {float(inv_even):.4f}   1/ratio_all = {float(inv_all):.4f}")
# Richardson: error ~ 1/P  => extrapolate 2*f(2P) - f(P)
rich = [2 * float(p2_rows[i + 1][1]) - float(p2_rows[i][1]) for i in range(len(p2_rows) - 1)]
rich2 = [2 * float(p2_rows[i + 1][2]) - float(p2_rows[i][2]) for i in range(len(p2_rows) - 1)]
print(f"    Richardson (1/P) on even:  {['%.4f' % x for x in rich]}")
print(f"    Richardson (1/P) on all :  {['%.4f' % x for x in rich2]}")
# exact limit via leading term: dim(p,0,0) = 2p^5/120 + O(p^4); sum over even p<=P ~ (1/60)(1/2)P^6/6 = P^6/720
p2_ok = abs(rich[-1] - 720) < 0.5 and abs(float(p2_rows[-1][1]) - 720) < 2
S(f"P2 constant -> 1/720 (last 1/ratio = {float(p2_rows[-1][1]):.3f}, Richardson {rich[-1]:.3f}); "
  f"odd-included neighbour -> 1/360 ({rich2[-1]:.3f})", p2_ok and abs(rich2[-1] - 360) < 0.5)
# closed-form statement of the leading coefficient, exact:
lead = Fraction(2, 120) * Fraction(1, 2) * Fraction(1, 6)
S(f"P2 leading coefficient exact: 2/5! * 1/2 * 1/6 = {lead} = 1/720", lead == Fraction(1, 720))

# ============================================================================ P3
print("\nP3  Funk scalars c_p/pi = (1/pi) ∫_0^{2pi} C_p^{(n/2)}(cos t) dt / C_p^{(n/2)}(1), direct quadrature")
mp.mp.dps = 30
def funk_ratio(n, p):
    lam = mp.mpf(n) / 2
    f = lambda t: mp.gegenbauer(p, lam, mp.cos(t))
    I = mp.quad(f, [0, mp.pi / 2, mp.pi, 3 * mp.pi / 2, 2 * mp.pi])
    return I / mp.gegenbauer(p, lam, 1) / mp.pi
target5 = {0: Fraction(2), 2: Fraction(5, 6), 4: Fraction(35, 64), 6: Fraction(105, 256)}
target3 = {0: Fraction(2), 2: Fraction(3, 4), 4: Fraction(15, 32), 6: Fraction(175, 512)}
p3_ok = True
for p in (0, 1, 2, 3, 4, 5, 6):
    v = funk_ratio(5, p)
    if p % 2 == 0:
        t = target5[p]; hit = abs(v - mp.mpf(t.numerator) / t.denominator) < mp.mpf('1e-20')
        p3_ok &= hit
        print(f"    n=5 p={p}: c_p/pi = {mp.nstr(v, 18)}   target {t}   {'ok' if hit else 'MISS'}")
    else:
        hit = abs(v) < mp.mpf('1e-20'); p3_ok &= hit
        print(f"    n=5 p={p}: c_p/pi = {mp.nstr(v, 5)}   target 0 (odd)   {'ok' if hit else 'MISS'}")
S("P3 Funk scalars n=5, p=0,2,4,6 = 2, 5/6, 35/64, 105/256 (and odd p = 0), 7/7", p3_ok)
c_ok = True
for p in (0, 2, 4, 6):
    v = funk_ratio(3, p); t = target3[p]
    c_ok &= abs(v - mp.mpf(t.numerator) / t.denominator) < mp.mpf('1e-20')
S("P3 control n=3: 2, 3/4, 15/32, 175/512 (Lyra's control values), 4/4", c_ok)

# Lyra's closed form 2 [(n/2)_k / k!]^2 / C_{2k}^{(n/2)}(1) vs quadrature, n=3..7, p<=12 even (beyond hash)
def closed(n, p):
    k = p // 2; lam = Fraction(n, 2)
    poch = Fraction(1)
    for i in range(k): poch *= (lam + i)
    coef = (poch / math.factorial(k)) ** 2
    # C_{2k}^{(lam)}(1) = (2 lam)_{2k} / (2k)!
    c1 = Fraction(1)
    for i in range(2 * k): c1 *= (2 * lam + i)
    c1 /= math.factorial(2 * k)
    return 2 * coef / c1
cf_ok = True; cf_n = 0
for n in range(3, 8):
    for p in range(0, 13, 2):
        v = funk_ratio(n, p); t = closed(n, p); cf_n += 1
        if abs(v - mp.mpf(t.numerator) / t.denominator) > mp.mpf('1e-18'):
            cf_ok = False; print(f"      closed-form MISS n={n} p={p}: {v} vs {t}")
S(f"closed form 2[(n/2)_k/k!]^2 / C_2k^(n/2)(1) = quadrature, n=3..7, even p<=12, {cf_n}/{cf_n} (beyond hash)", cf_ok)

print("\nEXTRA (beyond the hash): Fourier-cosine coefficients of C_p^{(n/2)}(cos t) all >= 0, n=3..7, p<=12")
pos_ok = True; cnt = 0; zero_bad = 0
for n in range(3, 8):
    lam = mp.mpf(n) / 2
    for p in range(13):
        for m in range(p + 1):
            a = mp.quad(lambda t: mp.gegenbauer(p, lam, mp.cos(t)) * mp.cos(m * t), [0, mp.pi]) / mp.pi
            cnt += 1
            if (m - p) % 2 == 0:
                if a <= mp.mpf('1e-15'): pos_ok = False; print(f"      NONPOS n={n} p={p} m={m}: {a}")
            else:
                if abs(a) > mp.mpf('1e-15'): zero_bad += 1
S(f"Gegenbauer cosine coefficients positive on the parity lattice, {cnt} coefficients, n=3..7, p<=12; off-parity zeros bad={zero_bad}", pos_ok and zero_bad == 0)

# ============================================================================ SCORE
print("\n" + "=" * 78)
npass = sum(1 for _, o in score if o)
print(f"SCORE {npass}/{len(score)}   [{time.time()-t0:.0f}s]")
hashed = [s for s in score if s[0][:2] in ("P1", "P2", "P3")]
print(f"  hashed lines: {sum(1 for _, o in hashed if o)}/{len(hashed)}   "
      f"controls+family+extra: {npass - sum(1 for _, o in hashed if o)}/{len(score) - len(hashed)}")
for lab, o in score:
    print(f"  {'PASS' if o else 'FAIL'}  {lab}")
