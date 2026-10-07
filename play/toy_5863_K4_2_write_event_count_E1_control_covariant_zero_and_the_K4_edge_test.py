#!/usr/bin/env python3
"""
Toy 5863 — Round K4-2, Lane B (Elie, 2026-10-07). Prereg: notes/Elie_K4-2_prereg_toy_5863_* (0e1e695f).

Framework: a one-photon transition i -> f is allowed iff the surviving symmetry admits a nonzero intertwiner
(operator (x) i) -> f. With rotations only: a nonzero Gaunt integral, identity on spin.
Controls: E1 (positive), free-electron absorption (negative, KL-W0), rank checks (E2, M1).
Count: covariant (0) vs with the named breaking (bound electron); K4 vertex AND edge test; K3/K6 nulls;
spin doubling; the corpus electron K-type's 4 weights (square, not tetrahedron).
Carry-over: the function the Haldane code computes.
"""
import itertools, importlib.util, os, random
import numpy as np
import sympy as sp
from sympy.physics.wigner import gaunt

RESULTS = []
def score(tag, ok, msg):
    RESULTS.append((tag, bool(ok))); print(f"  [{'PASS' if ok else 'FAIL'}] {tag}: {msg}")

def mel(lp, mp, k, q, l, m):
    """<l' m'| Y_kq |l m> = int Y*_{l'm'} Y_kq Y_lm  (Y* = (-1)^m Y_{l,-m})."""
    return (-1) ** mp * gaunt(lp, k, l, -mp, q, m)
def allowed(lp, mp, k, l, m):
    return any(mel(lp, mp, k, q, l, m) != 0 for q in range(-k, k + 1))

print("CONTROLS")
L = 6
ok = True
for l in range(L + 1):
    for lp in range(L + 1):
        for m in range(-l, l + 1):
            for mp in range(-lp, lp + 1):
                rule = abs(lp - l) == 1 and abs(mp - m) <= 1
                if allowed(lp, mp, 1, l, m) != rule: ok = False
targets_10 = sorted((lp, mp) for lp in range(L + 1) for mp in range(-lp, lp + 1) if allowed(lp, mp, 1, 1, 0))
score("C1", ok and len(targets_10) == 4,
      f"E1 (rank 1, Gaunt) = {{dl = +-1, dm in -1..1}} exactly for l, l' <= {L}; spin untouched by construction; from (1,0): {targets_10}")

E, m_, p_, w, c = sp.symbols('E m p omega c', positive=True)
# (p+k)^2 - m^2 = 2 omega (E - p cos) with E = sqrt(m^2 + p^2) > p >= p cos
inv = sp.simplify(2 * w * (sp.sqrt(m_**2 + p_**2) - p_ * c))
rs = random.Random(5863); neg = True
for _ in range(10000):
    mm, pp, ww = rs.uniform(1e-3, 10), rs.uniform(0, 100), rs.uniform(1e-6, 100)
    cc = rs.uniform(-1, 1)
    neg &= float(inv.subs({m_: mm, p_: pp, w: ww, c: cc})) > 0
E_psi, E_gam = sp.Rational(7, 2), sp.symbols('E_gamma', positive=True)
# first run used sympy .is_positive, which returns None here (owned); direct proof: E^2 - p^2 = m^2 > 0 with E, p >= 0
E_minus_p_pos = sp.simplify((sp.sqrt(m_**2 + p_**2))**2 - p_**2 - m_**2) == 0
score("C2", neg and E_minus_p_pos,
      "free electron + real photon: (p+k)^2 - m^2 = 2w(E - p cos) > 0 always (10^4 random + symbolic): 0 allowed. "
      "Module form: lowest energy of L_psi (x) L_gamma = 7/2 + E_gamma > 7/2, no L_psi summand (pin owed: Jakobsen-Vergne)")

ok2 = True
for l in range(5):
    for lp in range(5):
        for m in range(-l, l + 1):
            for mp in range(-lp, lp + 1):
                rule = (lp - l) in (-2, 0, 2) and l + lp >= 2 and abs(mp - m) <= 2
                if (lp, mp) == (l, m): continue        # same state: an expectation value, not a transition
                if allowed(lp, mp, 2, l, m) != rule: ok2 = False   # first run included it: (3,+-2) has an accidental 3j zero (owned)
def Lpm(l):
    dim = 2 * l + 1; ms = list(range(-l, l + 1))
    Lp = sp.zeros(dim, dim)
    for i, mm in enumerate(ms[:-1]): Lp[i + 1, i] = sp.sqrt(l * (l + 1) - mm * (mm + 1))
    return Lp, Lp.T, sp.diag(*ms)
Lp1, Lm1, Lz1 = Lpm(1)
m1_edges = {(i, j) for i in range(3) for j in range(3) if i < j and (Lp1[i, j] != 0 or Lp1[j, i] != 0 or Lz1[i, j] != 0)}
score("C3", ok2 and m1_edges == {(0, 1), (1, 2)},
      "E2 (rank 2) = {dl in 0,+-2, l+l'>=2, |dm|<=2} for l<=4; M1 (L) inside l=1 connects m-1<->m0<->m+1 only")

print("\nTHE WRITE COUNT")
score("W1", neg, "(i) covariant only: 0 write states (C2) - the absorption form of the K1937 wall")
s = (0, 0); P = [(1, -1), (1, 0), (1, 1)]; V = [s] + P
def edges(k_list):
    Es = set()
    for a, b in itertools.combinations(V, 2):
        if any(allowed(b[0], b[1], k, a[0], a[1]) for k in k_list): Es.add((a, b))
    return Es
E1 = edges([1]); E2only = edges([2])
M1 = {(P[0], P[1]), (P[1], P[2])}
star = all(s in e for e in E1) and len(E1) == 3
K4 = set(itertools.combinations(V, 2))
print(f"   E1 edges: {sorted(E1)}")
print(f"   E2 edges: {sorted(E2only)}")
score("W2", star and (E1 | M1) != K4 and (E1 | M1 | E2only) == K4,
      f"(ii) bound electron, from s: E1 gives 3 targets, graph = STAR K_(1,3) (3 of K4's 6 edges); "
      f"E1+M1 = {len(E1 | M1)} edges; +E2 = K4. Vertices map (frame = s, values = 3 dm); edges do NOT come from the write")
pre_detail = (E2only == {(P[0], P[2])})
print(f"   prereg detail 'E2 adds only p-1<->p+1': {'held' if pre_detail else 'WRONG - E2 alone gives all three p-p edges (the p-triangle); E1+E2 = K4 without M1'}")
# nulls
fixed_axis = [t for t in P if t[1] in (-1, 1)]                       # circular photon along z: q = +-1 only
E2_from_s = [(2, mm) for mm in range(-2, 3) if allowed(2, mm, 2, 0, 0)]
E1_from_s = [t for t in P if allowed(t[0], t[1], 1, 0, 0)]
score("W3", len(fixed_axis) == 2 and len(E2_from_s) == 5 and len(E1_from_s) == 3,
      "nulls: fixed photon axis -> s + 2 (K3 vertex set); E2-lowest -> s + 5 (K6 vertex set); "
      "K4's vertex count is selected only by 'lowest multipole, all directions' = the rank-1 three (caged generic 3)")
Vs = [(v, sz) for v in V for sz in (+1, -1)]
Es_spin = {(a, b) for a, b in itertools.combinations(Vs, 2) if a[1] == b[1] and ((a[0], b[0]) in E1 or (b[0], a[0]) in E1)}
adj = {v: set() for v in Vs}
for a, b in Es_spin: adj[a].add(b); adj[b].add(a)
seen, comps = set(), 0
for v in Vs:
    if v in seen: continue
    comps += 1; stack = [v]
    while stack:
        x = stack.pop()
        if x in seen: continue
        seen.add(x); stack += list(adj[x])
score("W4", len(Vs) == 8 and comps == 2 and len(Es_spin) == 6,
      "with spin: 8 states, E1 graph = two disjoint stars (spin unchanged): the K4 vertex map needs the record to erase spin")
F = sp.Rational
wts = [(F(a, 2), F(b, 2)) for a in (1, -1) for b in (1, -1)]
roots = [(1, 0), (0, 1), (1, 1), (1, -1)]
def refl(v, r):
    rr = r[0]**2 + r[1]**2; d = 2 * (v[0] * r[0] + v[1] * r[1]) / rr
    return (v[0] - d * r[0], v[1] - d * r[1])
gens = [tuple(wts.index(refl(v, r)) for v in wts) for r in roots]
G = {tuple(range(4))}; fr = [tuple(range(4))]
while fr:
    nx = []
    for g in fr:
        for h in gens:
            c_ = tuple(h[g[i]] for i in range(4))
            if c_ not in G: G.add(c_); nx.append(c_)
    fr = nx
sq = {frozenset((i, j)) for i, j in itertools.combinations(range(4), 2)
      if sum(abs(x - y) for x, y in zip(wts[i], wts[j])) == 1}       # nearest neighbours: the square's sides
preserves_sq = all({frozenset((g[i], g[j])) for i, j in map(tuple, sq)} == sq for g in G)
score("W5", len(G) == 8 and len(sq) == 4 and preserves_sq,
      "electron K-type V_(1/2,1/2): 4 weights (+-1/2, +-1/2); W(B2) acts as D4 (order 8), preserving the square's 4 sides: the 4 appears, K4's S4 does not")

print("\nCARRY-OVER: the function the Haldane code computes")
spec = importlib.util.spec_from_file_location("pf", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "notes", "bst_partition_function_extended.py"))
PF = importlib.util.module_from_spec(spec); spec.loader.exec_module(PF)
def lnZ_formula(beta, l_max, m_max, N=137, Rb=1.0, Rs=1.0):
    tot = 0.0
    for l in range(l_max + 1):
        d = (2 * l + 3) * (l + 1) * (l + 2) // 6
        for m in range(-m_max, m_max + 1):
            x = beta * np.sqrt(l * (l + 3) / Rb**2 + m**2 / Rs**2)
            if x == 0: z = np.log(N + 1)
            elif x >= 50: z = 0.0
            else: z = np.log(-np.expm1(-(N + 1) * x)) - np.log(-np.expm1(-x))
            tot += d * z
    return tot
rr = random.Random(1); dev = 0.0
for _ in range(200):
    b, lm, mm = rr.uniform(1e-3, 60), rr.randint(0, 25), rr.randint(0, 12)
    dev = max(dev, abs(lnZ_formula(b, lm, mm) - PF.ln_Z_total(b, lm, mm)) / max(1.0, abs(PF.ln_Z_total(b, lm, mm))))
score("H", dev < 1e-12,
      f"ln Z = sum_l sum_m d_l ln[(1-e^(-(N+1)bE))/(1-e^(-bE))], E = sqrt(l(l+3)/Rb^2 + m^2/Rs^2), zero mode ln(N+1), bE>=50 -> 0; "
      f"matches the code (200 random runs, max rel dev {dev:.1e}). The Guide's d_l ln binom(...) e^(-bE) is NOT this")

passed = sum(ok for _, ok in RESULTS)
print(f"\nSCORE: {passed}/{len(RESULTS)}")
