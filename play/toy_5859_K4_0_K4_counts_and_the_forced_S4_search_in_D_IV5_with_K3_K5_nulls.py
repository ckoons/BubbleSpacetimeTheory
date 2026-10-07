#!/usr/bin/env python3
"""
Toy 5859 — Round K4-0, Lane C (Elie, 2026-10-07). Prereg: notes/Elie_K4-0_prereg_toy_5859_* (commit c2455ce6).

Part A: K4's counts, computed by brute force (no table copied), with K3 and K5 as nulls.
Part B: search for a forced 4 / S4 / S3 / Z3 in D_IV^5's canonical finite groups, built from
        root data in exact rationals. Positive controls: W(A_{m-1}) contains S_m for m = 3, 4, 5;
        so(5,2) built from 7x7 matrices recovers its restricted roots and multiplicities.
        Nulls: the same search for K3 (S3) and K5 (S5). n-sweep D_IV^n, n = 3..8.
"""
from fractions import Fraction as F
from itertools import permutations, combinations, product
from math import factorial
import sympy as sp

RESULTS = []
def score(tag, ok, msg):
    RESULTS.append((tag, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {tag}: {msg}")

def perm_sign(p):
    s, seen = 1, set()
    for i in range(len(p)):
        if i in seen: continue
        j, L = i, 0
        while j not in seen:
            seen.add(j); j = p[j]; L += 1
        s *= (-1) ** (L - 1)
    return s

# ---------------------------------------------------------------- Part A: graph counts
def graph_data(m):
    V = list(range(m))
    E = [frozenset(e) for e in combinations(V, 2)]
    Aut = [p for p in permutations(V)]                       # complete graph: every perm preserves E
    Aut = [p for p in Aut if all(frozenset(p[x] for x in e) in E for e in E)]
    tri = [frozenset(t) for t in combinations(V, 3)]
    # Hamiltonian cycles: undirected = set of edge-sets
    ham = set()
    for seq in permutations(V[1:]):
        cyc = (0,) + seq
        ham.add(frozenset(frozenset((cyc[i], cyc[(i + 1) % m])) for i in range(m)))
    ham = list(ham) if m >= 3 else []
    match = [frozenset(M) for M in combinations(E, m // 2)
             if m % 2 == 0 and len(set().union(*M)) == m]
    # cycle space over Z2: edge subsets with all degrees even
    cyc_space = []
    for mask in range(1 << len(E)):
        S = [E[i] for i in range(len(E)) if mask >> i & 1]
        deg = [sum(v in e for e in S) for v in V]
        if all(d % 2 == 0 for d in deg): cyc_space.append(frozenset(S))
    return V, E, Aut, tri, ham, match, cyc_space

def induced_group(Aut, objs, act):
    idx = {o: i for i, o in enumerate(objs)}
    imgs = set()
    kernel = 0
    for p in Aut:
        im = tuple(idx[act(p, o)] for o in objs)
        imgs.add(im)
        if im == tuple(range(len(objs))): kernel += 1
    return len(imgs), kernel

act_set = lambda p, s: frozenset(p[x] for x in s)
act_eset = lambda p, S: frozenset(frozenset(p[x] for x in e) for e in S)

print("PART A — K4 counts (brute force), K3/K5 nulls")
summary = {}
for m in (3, 4, 5):
    V, E, Aut, tri, ham, match, cs = graph_data(m)
    summary[m] = dict(aut=len(Aut), E=len(E), F=len(tri), ham=len(ham), dham=2 * len(ham),
                      match=len(match), cs_dim=len(cs).bit_length() - 1, euler=len(V) - len(E) + len(tri))
    print(f"  K{m}: {summary[m]}")

V, E, Aut, tri, ham, match, cs = graph_data(4)
score("A1", len(Aut) == 24 and induced_group(Aut, V, lambda p, v: p[v]) == (24, 1)
      and induced_group(Aut, E, act_set) == (24, 1) and induced_group(Aut, tri, act_set) == (24, 1),
      "|Aut K4| = 24, faithful on V(4), E(6), F(4)")
frame = 0
rooted = [(frame,) + s for s in permutations([1, 2, 3])]
score("A2", len(ham) == 3 and len(rooted) == 6 and
      len({frozenset(frozenset((r[i], r[(i + 1) % 4])) for i in range(4)) for r in rooted}) == 3,
      "Ham cycles 3 undirected / 6 directed; 6 rooted reads at the frame vertex cover all 3")
comp = {h: frozenset(E) - h for h in ham}
score("A3", len(match) == 3 and set(comp.values()) == set(match),
      "3 perfect matchings = complements of the 3 Ham cycles (bijection)")
gH = induced_group(Aut, ham, act_eset); gM = induced_group(Aut, match, act_eset)
score("A4", gH == (6, 4) and gM == (6, 4),
      f"S4 acts on Ham cycles {gH} and matchings {gM} as (image order, kernel order) = (6 = S3, 4 = V4)")
orbs = {}
for c in cs:
    orbs.setdefault(frozenset(act_eset(p, c) for p in Aut), None)
sizes = sorted(len(o) for o in orbs)
score("A5", len(cs) == 8 and sizes == [1, 3, 4],
      f"Z2 cycle space: 8 elements, S4-orbit sizes {sizes} (0; 3 four-cycles; 4 triangles)")
stab = [p for p in Aut if p[frame] == frame]
rot = [p for p in stab if perm_sign(p) == 1]
def orbits_on(G, X, act):
    seen, out = set(), []
    for x in X:
        if x in seen: continue
        o = {act(g, x) for g in G}; seen |= o; out.append(o)
    return out
act_seq = lambda p, r: (p[r[0]],) + tuple(p[x] for x in r[1:])
o_stab = orbits_on(stab, rooted, act_seq); o_rot = orbits_on(rot, rooted, act_seq)
score("A6", len(stab) == 6 and induced_group(stab, [1, 2, 3], lambda p, v: p[v]) == (6, 1)
      and [len(o) for o in o_stab] == [6] and sorted(len(o) for o in o_rot) == [3, 3],
      "frame stabilizer S3 faithful on 3 values; Z3 splits 6 rooted reads into 2 orbits of 3 (two handednesses)")
# H1(K4;Q): virtual character C1 - C0 + H0 ; det_H1 = det_C1 / det_C0
Eor = [tuple(sorted(e)) for e in E]
def c1_matrix(p):
    M = sp.zeros(6, 6)
    for j, (a, b) in enumerate(Eor):
        pa, pb = p[a], p[b]
        i = Eor.index(tuple(sorted((pa, pb))))
        M[i, j] = 1 if pa < pb else -1
    return M
def c0_matrix(p):
    M = sp.zeros(4, 4)
    for j in range(4): M[p[j], j] = 1
    return M
chiH1 = {p: c1_matrix(p).trace() - c0_matrix(p).trace() + 1 for p in Aut}
chi_stdsgn = {p: (sum(p[i] == i for i in range(4)) - 1) * perm_sign(p) for p in Aut}
norm = sum(chiH1[p] ** 2 for p in Aut) / 24
detH1 = {p: c1_matrix(p).det() / c0_matrix(p).det() for p in Aut}
score("A7", all(chiH1[p] == chi_stdsgn[p] for p in Aut) and norm == 1 and all(d == 1 for d in detH1.values()),
      f"H1(K4;Q) = std(x)sign, irreducible (<chi,chi> = {norm}), det = +1 on all 24: S4 acts on the loops inside SO(3)")
s3, s5 = summary[3], summary[5]
score("A-null", (s3['aut'], s3['ham'], s3['match'], s3['cs_dim']) == (6, 1, 0, 1)
      and (s5['aut'], s5['ham'], s5['match'], s5['cs_dim']) == (120, 12, 0, 6)
      and summary[4]['euler'] == 2,
      "K3: Aut 6, Ham 1, matchings 0, rank 1 | K5: Aut 120, Ham 12, matchings 0, rank 6 | K4 V-E+F = 2")

# ---------------------------------------------------------------- Part B: groups from root data
def refl(alpha):
    n = len(alpha); aa = sum(x * x for x in alpha)
    return tuple(tuple((F(1) if i == j else F(0)) - F(2) * alpha[i] * alpha[j] / aa for j in range(n)) for i in range(n))
def mul(A, B):
    n = len(A)
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)) for i in range(n))
def closure(gens):
    n = len(gens[0]); I = tuple(tuple(F(int(i == j)) for j in range(n)) for i in range(n))
    G, frontier = {I}, [I]
    while frontier:
        nxt = []
        for g in frontier:
            for s in gens:
                h = mul(g, s)
                if h not in G: G.add(h); nxt.append(h)
        frontier = nxt
    return G
def apply(A, v): return tuple(sum(A[i][k] * v[k] for k in range(len(v))) for i in range(len(v)))
def e(i, n, c=1): return tuple(F(c) if k == i else F(0) for k in range(n))
def add(*vs): return tuple(sum(x) for x in zip(*vs))
def neg(v): return tuple(-x for x in v)

def roots_B(r):  return [e(i, r, s) for i in range(r) for s in (1, -1)] + roots_D(r)
def roots_C(r):  return [e(i, r, 2 * s) for i in range(r) for s in (1, -1)] + roots_D(r)
def roots_D(r):  return [add(e(i, r, s), e(j, r, t)) for i, j in combinations(range(r), 2) for s in (1, -1) for t in (1, -1)]
def roots_A(m):  return [add(e(i, m, 1), e(j, m, -1)) for i in range(m) for j in range(m) if i != j]
def weyl(roots):
    pos = {tuple(abs(x) for x in a): a for a in roots}
    return closure([refl(a) for a in pos.values()])

def order(g, G=None):
    n = len(g); I = tuple(tuple(F(int(i == j)) for j in range(n)) for i in range(n))
    k, h = 1, g
    while h != I: h = mul(h, g); k += 1
    return k

def contains_Sm(G, m):
    """Find Coxeter generators s1..s_{m-1} (A_{m-1} relations) generating a group of order m!."""
    if m <= 1: return True
    if len(G) % factorial(m): return False
    n = len(next(iter(G))); I = tuple(tuple(F(int(i == j)) for j in range(n)) for i in range(n))
    inv = [g for g in G if g != I and mul(g, g) == I]
    if m == 2: return bool(inv)
    def ordk(x, k):  # x^k == I and smallest
        h = x
        for t in range(1, k + 1):
            if h == I: return t == k
            h = mul(h, x)
        return False
    def ext(chain):
        if len(chain) == m - 1:
            return len(closure(chain)) == factorial(m)
        last = chain[-1]
        for s in inv:
            if s in chain: continue
            if not ordk(mul(last, s), 3): continue
            if any(mul(c, s) != mul(s, c) for c in chain[:-1]): continue
            if ext(chain + [s]): return True
        return False
    return any(ext([s]) for s in inv)

def max_m(G, top=6):
    best = 1
    for m in range(2, top + 1):
        if contains_Sm(G, m): best = m
    return best

print("\nPART B — positive control on the detector: W(A_{m-1}) must contain S_m")
pc = []
for m in (3, 4, 5):
    W = weyl(roots_A(m))
    pc.append((m, len(W), contains_Sm(W, m)))
print("  ", pc)
score("PC1", all(sz == factorial(m) and ok for m, sz, ok in pc), "detector finds S3, S4, S5 in W(A2), W(A3), W(A4)")

print("\nPART B — positive control on the geometry: so(5,2) from 7x7 matrices")
eta = sp.diag(1, 1, 1, 1, 1, -1, -1)
basis = []
for i, j in combinations(range(7), 2):
    X = sp.zeros(7, 7); X[i, j] = 1; X[j, i] = -1 if eta[i, i] == eta[j, j] else 1
    basis.append(X)
assert all((X.T * eta + eta * X) == sp.zeros(7, 7) for X in basis)
H1m = sp.zeros(7, 7); H1m[0, 5] = H1m[5, 0] = 1
H2m = sp.zeros(7, 7); H2m[1, 6] = H2m[6, 1] = 1
assert H1m * H2m - H2m * H1m == sp.zeros(7, 7)
Bmat = sp.Matrix([list(X) for X in basis]).T          # 49 x 21
def coords(Y): return Bmat.solve_least_squares(sp.Matrix(list(Y)))
adH = [sp.Matrix.hstack(*[coords(H * X - X * H) for X in basis]) for H in (H1m, H2m)]
# joint eigen-decomposition: adH1, adH2 commute and are diagonalizable over Q (real roots)
P, _ = (adH[0] + 3 * adH[1]).diagonalize()          # generic combination separates the joint eigenspaces
D1 = P.inv() * adH[0] * P
D2 = P.inv() * adH[1] * P
assert D1.is_diagonal()
roots_found = {}
for k in range(21):
    lam = (D1[k, k], D2[k, k])
    roots_found[lam] = roots_found.get(lam, 0) + 1
assert D2.is_diagonal()
mult = {r: c for r, c in roots_found.items() if r != (0, 0)}
print("   restricted roots (mult):", dict(sorted(mult.items())))
short = [r for r in mult if sum(x * x for x in r) == 1]
long_ = [r for r in mult if sum(x * x for x in r) == 2]
kbasis = [X for X in basis if X == -X.T]               # compact part: antisymmetric
# general centralizer of a in k (span), by linear algebra
cvars = sp.symbols('c0:%d' % len(kbasis))
Xg = sum((c * X for c, X in zip(cvars, kbasis)), sp.zeros(7, 7))
eqs = list(Xg * H1m - H1m * Xg) + list(Xg * H2m - H2m * Xg)
dim_m = len(kbasis) - sp.Matrix([[sp.diff(q, c) for c in cvars] for q in eqs if q != 0]).rank()
score("PC2", len(short) == 4 and len(long_) == 4 and all(mult[r] == 3 for r in short)
      and all(mult[r] == 1 for r in long_) and roots_found[(0, 0)] == 2 + dim_m and dim_m == 3,
      f"B2 restricted roots: short mult {sorted(set(mult[r] for r in short))} (= n-2), long mult "
      f"{sorted(set(mult[r] for r in long_))}; dim m = {dim_m}; dim p = 2 + sum(pos mult) = {2 + sum(c for r, c in mult.items() if r > (0, 0))}")

print("\nPART B — canonical finite groups of D_IV^5")
W_res = weyl(roots_C(2)); W_res_B = weyl([tuple(F(x) for x in r) for r in mult])
W_K = weyl([r + (F(0),) for r in roots_B(2)])          # so(5) on e1,e2 ; so(2) = e3 contributes nothing
W_G = weyl(roots_B(3))
for name, G in (("W(restricted C2)", W_res), ("W(restricted, from matrices)", W_res_B), ("W_K", W_K), ("W(g_C)=W(B3)", W_G)):
    ords = sorted({order(g) for g in G})
    print(f"   {name}: |G| = {len(G)}, element orders {ords}")
no3 = lambda G: all(order(g) % 3 for g in G)
score("B1", len(W_res) == 8 and len(W_res_B) == 8 and len(W_K) == 8 and no3(W_res) and no3(W_K)
      and not contains_Sm(W_res, 3) and not contains_Sm(W_K, 3),
      "interior real Weyl group and W_K: order 8, NO element of order 3 -> no S3, no Z3 orientation, no K3/K4/K5 action")
rotG = [g for g in W_G if sp.Matrix(g).det() == 1]
diag = [(F(1, 2), F(s), F(t)) for s, t in ((F(1, 2), F(1, 2)), (F(1, 2), F(-1, 2)), (F(-1, 2), F(1, 2)), (F(-1, 2), F(-1, 2)))]
diag = [tuple(F(x) for x in (F(1, 2), a, b)) for (_, a, b) in diag]
def line(v): return frozenset({v, neg(v)})
Ldiag = [line(v) for v in diag]
gd = induced_group(rotG, Ldiag, lambda g, L: line(apply(g, next(iter(L)))))
score("B2", len(W_G) == 48 and contains_Sm(W_G, 3) and contains_Sm(W_G, 4) and not contains_Sm(W_G, 5)
      and len(rotG) == 24 and gd == (24, 1) and any(g == tuple(tuple(F(-int(i == j)) for j in range(3)) for i in range(3)) for g in W_G),
      "W(B3): order 48, contains S3, S4, not S5; rotation half = S4 (faithful, full on the 4 cube diagonals); -1 central -> S4 x Z2")
vec = [e(i, 3, s) for i in range(3) for s in (1, -1)]
spin = [tuple(F(s, 2) for s in sg) for sg in product((1, -1), repeat=3)]
rts = roots_B(3)
def orbit_sizes(G, X): return sorted(len(o) for o in orbits_on(G, X, apply))
osz = {k: orbit_sizes(W_G, X) for k, X in (("vector", vec), ("spinor", spin), ("roots", rts))}
W_D3 = weyl(roots_D(3))
Tset = orbits_on(W_D3, spin, apply)
T = sorted(Tset, key=lambda o: -sum(1 for v in o if sum(1 for x in v if x < 0) % 2 == 0))[0]
T = sorted(T); Tbar = sorted(neg(v) for v in T)
gT = induced_group(list(W_D3), T, apply)
score("B3", all(4 not in s for s in osz.values()) and len(W_D3) == 24 and sorted(len(o) for o in Tset) == [4, 4]
      and gT == (24, 1),
      f"no W(B3) weight orbit of size 4 {osz}; W(D3) splits the spinor cube into 2 tetrahedra, full S4 on each; picking one = one sign")
# dictionary
mid = {frozenset((a, b)): tuple((x + y) / 2 for x, y in zip(a, b)) for a, b in combinations(T, 2)}
half_vec = {tuple(x / 2 for x in v) for v in vec}
cent = {frozenset(f): tuple(sum(c) / 3 for c in zip(*f)) for f in combinations(T, 3)}
face_dual = {tuple(3 * x for x in c) for c in cent.values()}
axes_ok = all(line(mid[e1]) == line(mid[e2]) for e1, e2 in
              [(frozenset((T[a], T[b])), frozenset((T[c], T[d]))) for a, b, c, d in ((0, 1, 2, 3), (0, 2, 1, 3), (0, 3, 1, 2))])
score("B4", set(mid.values()) == half_vec and len(set(mid.values())) == 6 and face_dual == set(Tbar) and axes_ok
      and len({line(v) for v in mid.values()}) == 3,
      "dictionary: 6 edge midpoints = the 6 vector weights/2; face centroids x3 = the other tetrahedron; opposite-edge pairs = the 3 axes")
axes = [line(e(i, 3)) for i in range(3)]
ga = induced_group(list(W_G), axes, lambda g, L: line(apply(g, next(iter(L)))))
score("B5", ga[0] == 6 and not contains_Sm(W_G, 5) and not contains_Sm(W_res, 5) and not contains_Sm(W_K, 5),
      f"null K3: W(B3) acts on the 3 axes as full S3 (image {ga[0]}) with NO sign chosen; null K5: absent from every group")

print("\nPART B — n-sweep D_IV^n: max m with S_m in W(so(n+2))")
sweep = {}
for n in range(3, 9):
    r = (n + 2) // 2
    W = weyl(roots_D(r)) if (n + 2) % 2 == 0 else weyl(roots_B(r))
    sweep[n] = (len(W), max_m(W, 6))
    print(f"   n={n}: so({n+2}) |W| = {sweep[n][0]}, max m = {sweep[n][1]}")
score("B6", [sweep[n][1] for n in range(3, 9)] == [2, 4, 4, 4, 4, 5],
      "K4 is the ceiling for n = 4..7; n = 5 is not singled out")
def hook_dims(m):
    def parts(k, mx):
        if k == 0: yield (); return
        for i in range(min(k, mx), 0, -1):
            for p in parts(k - i, i): yield (i,) + p
    out = []
    for lam in parts(m, m):
        conj = [sum(1 for x in lam if x > j) for j in range(lam[0])]
        h = 1
        for i, row in enumerate(lam):
            for j in range(row): h *= (row - j - 1) + (conj[j] - i - 1) + 1
        out.append(factorial(m) // h)
    return sorted(out)
d5 = hook_dims(5)
score("B7", d5 == [1, 1, 4, 4, 5, 5, 6] and sum(d * d for d in d5) == 120 and min(d for d in d5 if d > 1) == 4
      and len(rotG) == 24 and gd == (24, 1),
      "S5's nonlinear irreps all have dim >= 4 -> no S5 in O(3); S4 sits in SO(3) (cube rotations). SO(3) in M allows S4, forces none")

passed = sum(ok for _, ok in RESULTS)
print(f"\nSCORE: {passed}/{len(RESULTS)}")
